import pygame
import random
import time

FPS    = 60
HUD_H  = 64

MAX_MAZE_W = 840
MAX_MAZE_H = 680

# Colors
WHITE    = (255, 255, 255)
DARK     = (30,  30,  30)
WALL     = (55,  55,  75)
WALL_H   = (80,  80, 105)
FLOOR    = (195, 190, 205)
PLAYER_C = (80,  160, 255)
EXIT_C   = (80,  220, 100)
HUD_BG   = (20,  20,  30)
TEXT     = (220, 220, 230)
SUBTEXT  = (140, 140, 160)
WIN_C    = (80,  220, 100)
TRAIL_C  = (170, 165, 180)
DANGER   = (220,  80,  80)
YELLOW   = (255, 200,  50)
MENU_BG  = (15,  15,  25)
MENU_SEL = (45,  55,  80)
EASY_C   = (80,  210, 110)
MED_C    = (220, 185,  50)
HARD_C   = (220,  70,  70)

DIFF_COLORS = {"Easy": EASY_C, "Medium": MED_C, "Hard": HARD_C}

# base_cols / base_rows: starting maze cell count (must be odd)
# cell:       base pixel size of one cell
# loops_pct:  fraction of interior walls randomly removed after generation
#             0.0 = perfect maze (one solution), 0.25 = many loops
# show_trail: whether breadcrumb trail is drawn
# time_limit: seconds allowed (0 = unlimited)
# size_inc:   cell-count increase per level (added to both cols & rows)
DIFFICULTIES = {
    "Easy":   dict(base_cols=15, base_rows=11, cell=42,
                   loops_pct=0.00, show_trail=True,  time_limit=0,   size_inc=2),
    "Medium": dict(base_cols=23, base_rows=17, cell=30,
                   loops_pct=0.12, show_trail=True,  time_limit=0,   size_inc=4),
    "Hard":   dict(base_cols=31, base_rows=23, cell=22,
                   loops_pct=0.25, show_trail=False, time_limit=120, size_inc=6),
}
DIFF_ORDER = ["Easy", "Medium", "Hard"]


# ---------------------------------------------------------------------------
# Maze generation
# ---------------------------------------------------------------------------

def _odd(n):
    return n if n % 2 == 1 else n - 1

def generate_maze(cols, rows, loops_pct=0.0):
    """Recursive-backtracker maze with optional extra loops.

    cols / rows must be odd.
    loops_pct: fraction of interior wall cells to randomly knock down
               after the perfect maze is built (creates multiple paths).
    """
    grid = [[1] * cols for _ in range(rows)]  # 1 = wall, 0 = floor

    # --- Recursive backtracker ---
    def carve(cx, cy):
        grid[cy][cx] = 0
        dirs = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 1:
                grid[cy + dy // 2][cx + dx // 2] = 0
                carve(nx, ny)

    carve(1, 1)

    # --- Add loops by removing extra interior walls ---
    if loops_pct > 0:
        # Collect candidate walls: interior cells that are walls and have
        # exactly two opposite floor neighbours (horizontal or vertical pair).
        candidates = []
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 1:
                    # horizontal pair
                    if grid[r][c - 1] == 0 and grid[r][c + 1] == 0:
                        candidates.append((r, c))
                    # vertical pair
                    elif grid[r - 1][c] == 0 and grid[r + 1][c] == 0:
                        candidates.append((r, c))

        random.shuffle(candidates)
        knock_down = int(len(candidates) * loops_pct)
        for r, c in candidates[:knock_down]:
            grid[r][c] = 0

    return grid


def build_maze(diff_name, level):
    """Return (grid, cols, rows, cell_size) for a given difficulty & level."""
    d = DIFFICULTIES[diff_name]
    inc = (level - 1) * d["size_inc"]
    cols = _odd(min(d["base_cols"] + inc, 63))
    rows = _odd(min(d["base_rows"] + inc, 47))

    # Scale cell size down if the maze would exceed the max window
    cell = d["cell"]
    cell = min(cell, MAX_MAZE_W // cols, MAX_MAZE_H // rows)
    cell = max(cell, 14)

    grid = generate_maze(cols, rows, loops_pct=d["loops_pct"])
    return grid, cols, rows, cell


# ---------------------------------------------------------------------------
# Player
# ---------------------------------------------------------------------------

class Player:
    MAX_TRAIL = 60

    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.trail = []

    def try_move(self, dcol, drow, grid):
        nc, nr = self.col + dcol, self.row + drow
        if 0 <= nc < len(grid[0]) and 0 <= nr < len(grid) and grid[nr][nc] == 0:
            self.trail.append((self.col, self.row))
            if len(self.trail) > self.MAX_TRAIL:
                self.trail.pop(0)
            self.col, self.row = nc, nr
            return True
        return False

    def rect(self, cell):
        m = max(4, cell // 6)
        return pygame.Rect(self.col * cell + m, self.row * cell + m,
                           cell - m * 2, cell - m * 2)


# ---------------------------------------------------------------------------
# Game
# ---------------------------------------------------------------------------

class Game:
    # States
    MENU    = "menu"
    PLAYING = "playing"
    WON     = "won"
    DEAD    = "dead"   # time ran out

    def __init__(self):
        pygame.init()
        self.font_big   = pygame.font.SysFont("monospace", 36, bold=True)
        self.font_med   = pygame.font.SysFont("monospace", 24)
        self.font_small = pygame.font.SysFont("monospace", 16)

        self.diff    = "Easy"
        self.level   = 1
        self.state   = self.MENU
        self.screen  = None
        self.clock   = pygame.time.Clock()

        self._init_menu_screen()

    # ------------------------------------------------------------------
    # Screen management
    # ------------------------------------------------------------------

    def _init_menu_screen(self):
        w, h = 560, 460
        if self.screen is None or self.screen.get_size() != (w, h):
            self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Maze Runner")

    def _init_game_screen(self):
        w = self.mcols * self.cell
        h = self.mrows * self.cell + HUD_H
        if self.screen is None or self.screen.get_size() != (w, h):
            self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(f"Maze Runner – {self.diff}  Lv {self.level}")

    # ------------------------------------------------------------------
    # Reset / new level
    # ------------------------------------------------------------------

    def reset(self):
        self.grid, self.mcols, self.mrows, self.cell = build_maze(self.diff, self.level)
        self.player   = Player(1, 1)
        self.exit_col = self.mcols - 2
        self.exit_row = self.mrows - 2
        self.grid[self.exit_row][self.exit_col] = 0
        self.start_time   = time.time()
        self.move_cd      = 0.0
        self.state        = self.PLAYING
        self._init_game_screen()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def elapsed(self):
        return time.time() - self.start_time

    def time_left(self):
        tl = DIFFICULTIES[self.diff]["time_limit"]
        if tl == 0:
            return None
        return max(0.0, tl - self.elapsed())

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------

    def draw_maze(self):
        cell = self.cell
        for r in range(self.mrows):
            for c in range(self.mcols):
                rect = pygame.Rect(c * cell, r * cell, cell, cell)
                if self.grid[r][c] == 1:
                    pygame.draw.rect(self.screen, WALL, rect)
                    pygame.draw.rect(self.screen, WALL_H, rect, 1)
                else:
                    pygame.draw.rect(self.screen, FLOOR, rect)

    def draw_exit(self):
        cell = self.cell
        m = max(3, cell // 8)
        rect = pygame.Rect(self.exit_col * cell + m, self.exit_row * cell + m,
                           cell - m * 2, cell - m * 2)
        pygame.draw.rect(self.screen, EXIT_C, rect, border_radius=max(3, cell // 8))
        pulse = int(3 + 2 * abs((self.elapsed() % 1) - 0.5) * 2)
        pygame.draw.rect(self.screen, WHITE, rect, pulse, border_radius=max(3, cell // 8))

    def draw_trail(self):
        if not DIFFICULTIES[self.diff]["show_trail"]:
            return
        cell = self.cell
        n = len(self.player.trail)
        if n == 0:
            return
        size = max(4, cell - cell // 3)
        off  = (cell - size) // 2
        for i, (tc, tr) in enumerate(self.player.trail):
            alpha = int(90 * (i + 1) / n)
            s = pygame.Surface((size, size), pygame.SRCALPHA)
            s.fill((*TRAIL_C, alpha))
            self.screen.blit(s, (tc * cell + off, tr * cell + off))

    def draw_player(self):
        cell = self.cell
        r = self.player.rect(cell)
        pygame.draw.ellipse(self.screen, PLAYER_C, r)
        hl = pygame.Rect(r.x + r.w // 4, r.y + r.h // 5,
                         max(3, r.w // 3), max(3, r.h // 3))
        pygame.draw.ellipse(self.screen, WHITE, hl)

    def draw_hud(self):
        cell = self.cell
        y0   = self.mrows * cell
        w    = self.mcols * cell
        pygame.draw.rect(self.screen, HUD_BG, (0, y0, w, HUD_H))

        dc   = DIFF_COLORS[self.diff]
        lvl  = self.font_med.render(f"Lv {self.level}  [{self.diff}]", True, dc)
        self.screen.blit(lvl, (12, y0 + 8))

        t_str = f"{self.elapsed():.1f}s"
        tl    = self.time_left()
        if tl is not None:
            col = DANGER if tl < 20 else (YELLOW if tl < 45 else TEXT)
            t_str = f"Time left: {tl:.0f}s"
        else:
            col = TEXT
        t_surf = self.font_med.render(t_str, True, col)
        self.screen.blit(t_surf, (w // 2 - t_surf.get_width() // 2, y0 + 8))

        help_s = self.font_small.render(
            "Arrow/WASD – move   R – restart   M – menu", True, SUBTEXT)
        self.screen.blit(help_s, (12, y0 + 38))

    def draw_overlay(self, title, title_col, lines):
        """Generic semi-transparent overlay with title + message lines."""
        w, h = self.screen.get_size()
        ov = pygame.Surface((w, h), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 170))
        self.screen.blit(ov, (0, 0))

        msg = self.font_big.render(title, True, title_col)
        self.screen.blit(msg, (w // 2 - msg.get_width() // 2, h // 2 - 80))
        for i, (text, color) in enumerate(lines):
            s = self.font_med.render(text, True, color)
            self.screen.blit(s, (w // 2 - s.get_width() // 2,
                                 h // 2 - 20 + i * 38))

    def draw_win(self):
        self.draw_overlay(
            "YOU ESCAPED!", WIN_C,
            [(f"Time: {self.elapsed():.2f}s", TEXT),
             ("N – next level    R – restart    M – menu", SUBTEXT)],
        )

    def draw_dead(self):
        self.draw_overlay(
            "TIME'S UP!", DANGER,
            [("The maze won this round.", TEXT),
             ("R – try again    M – menu", SUBTEXT)],
        )

    # ------------------------------------------------------------------
    # Menu screen
    # ------------------------------------------------------------------

    def draw_menu(self):
        w, h = self.screen.get_size()
        self.screen.fill(MENU_BG)

        title = self.font_big.render("MAZE  RUNNER", True, WHITE)
        self.screen.blit(title, (w // 2 - title.get_width() // 2, 60))

        sub = self.font_small.render("Choose difficulty", True, SUBTEXT)
        self.screen.blit(sub, (w // 2 - sub.get_width() // 2, 115))

        descriptions = {
            "Easy":   "Small maze · one solution · no time limit",
            "Medium": "Bigger maze · multiple paths · no time limit",
            "Hard":   "Large maze · many loops · 120 s limit · no trail",
        }
        keys = ["1", "2", "3"]

        box_w, box_h = 420, 72
        box_x = w // 2 - box_w // 2
        for i, name in enumerate(DIFF_ORDER):
            box_y  = 160 + i * (box_h + 14)
            is_sel = (name == self.diff)
            bg     = MENU_SEL if is_sel else (25, 28, 40)
            border = DIFF_COLORS[name] if is_sel else (50, 55, 70)

            pygame.draw.rect(self.screen, bg,     (box_x, box_y, box_w, box_h), border_radius=10)
            pygame.draw.rect(self.screen, border, (box_x, box_y, box_w, box_h), 2, border_radius=10)

            label = self.font_med.render(f"[{keys[i]}]  {name}", True, DIFF_COLORS[name])
            desc  = self.font_small.render(descriptions[name], True, SUBTEXT)
            self.screen.blit(label, (box_x + 18, box_y + 10))
            self.screen.blit(desc,  (box_x + 18, box_y + 42))

        start = self.font_med.render("Press ENTER or a number to start", True, TEXT)
        self.screen.blit(start, (w // 2 - start.get_width() // 2, h - 60))

    # ------------------------------------------------------------------
    # Input
    # ------------------------------------------------------------------

    def handle_menu_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        key_map = {pygame.K_1: "Easy", pygame.K_2: "Medium", pygame.K_3: "Hard"}
        if event.key in key_map:
            self.diff = key_map[event.key]
        if event.key == pygame.K_UP:
            idx = DIFF_ORDER.index(self.diff)
            self.diff = DIFF_ORDER[max(0, idx - 1)]
        if event.key == pygame.K_DOWN:
            idx = DIFF_ORDER.index(self.diff)
            self.diff = DIFF_ORDER[min(len(DIFF_ORDER) - 1, idx + 1)]
        if event.key in (pygame.K_RETURN, pygame.K_SPACE,
                          pygame.K_1, pygame.K_2, pygame.K_3):
            self.level = 1
            self.reset()

    def handle_playing_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_r:
            self.reset()
        if event.key == pygame.K_m:
            self.state = self.MENU
            self._init_menu_screen()
        if event.key == pygame.K_n and self.state == self.WON:
            self.level += 1
            self.reset()

    def handle_movement(self, dt):
        if self.move_cd > 0:
            self.move_cd -= dt
            return
        keys = pygame.key.get_pressed()
        moved = False
        if   keys[pygame.K_UP]    or keys[pygame.K_w]: moved = self.player.try_move( 0, -1, self.grid)
        elif keys[pygame.K_DOWN]  or keys[pygame.K_s]: moved = self.player.try_move( 0,  1, self.grid)
        elif keys[pygame.K_LEFT]  or keys[pygame.K_a]: moved = self.player.try_move(-1,  0, self.grid)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]: moved = self.player.try_move( 1,  0, self.grid)
        if moved:
            self.move_cd = 0.10

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self.state == self.MENU:
                    self.handle_menu_event(event)
                else:
                    self.handle_playing_event(event)

            if self.state == self.PLAYING:
                self.handle_movement(dt)
                if (self.player.col == self.exit_col and
                        self.player.row == self.exit_row):
                    self.state = self.WON
                tl = self.time_left()
                if tl is not None and tl <= 0:
                    self.state = self.DEAD

            # --- Draw ---
            if self.state == self.MENU:
                self.draw_menu()
            else:
                self.screen.fill(DARK)
                self.draw_maze()
                self.draw_trail()
                self.draw_exit()
                self.draw_player()
                self.draw_hud()
                if self.state == self.WON:
                    self.draw_win()
                elif self.state == self.DEAD:
                    self.draw_dead()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()