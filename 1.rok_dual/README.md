# 📚 1. rok — Duálne štúdium

> **⚠️ Pred použitím akýchkoľvek materiálov si prečítaj vyhlásenie o vylúčení zodpovednosti.**

---

## ⚠️ Vyhlásenie o vylúčení zodpovednosti

Tento repozitár som vytvoril ako osobný archív poznámok, cvičení, testov a materiálov z prvého roka duálneho štúdia. Zverejnil som ho s cieľom uľahčiť prístup k študijným materiálom ostatným študentom dualu.

**Použitie materiálov**
Materiály sú poskytované výlučne na študijné účely. Za akékoľvek zneužitie obsahu — vrátane opisovania, podvádzania alebo porušenia školského poriadku — nesie plnú zodpovednosť osoba, ktorá sa tohto konania dopustila. Ja ako autor za takéto konanie nezodpovedám.

**Cudzie materiály a autorské práva**
Časť obsahu pôvodne vytvorili moji spolužiaci alebo učitelia. Tieto materiály sú zverejnené výlučne v rámci zdieľania v uzavretej študentskej komunite rovnakej školy a odboru. Nie je dovolené ich ďalej šíriť, vydávať za vlastné ani inak využívať mimo štúdia bez súhlasu pôvodného autora.

**Žiadosť o odstránenie obsahu**
Ak ste autorom niektorého z materiálov a nesúhlasíte s jeho zverejnením v tomto repozitári, kontaktujte ma prostredníctvom GitHubu alebo slocialných médií pripojených k tomuto účtu. Obsah bude na základe vašej žiadosti bezodkladne odstránený.

---

## 👥 Pre koho je tento repozitár

Určené pre študentov duálneho štúdia SPŠE košice a Telekomu — ako doplnkový študijný materiál, pomôcka pri učení alebo rýchla rekapitulácia pred testom.

**Prečo sú tu testy?**
Materiály v priečinku TESTY/ sú určené výlučne na prípravu — ako ukážka formátu otázok a rozsahu učiva. Ich použitie na opisovanie alebo akúkoľvek formu akademického podvodu je na výhradnú zodpovednosť osoby, ktorá sa tohto konania dopustila. Ja ako autor repozitára za takéto konanie nenesiem žiadnu zodpovednosť.

**Prečo sú tu prezentácie spolužiakov?**
Slúžia ako ukážka toho, čo a ako ostatní spracovali — inšpirácia, referencia, alebo jednoducho materiál na doplnenie si medzier. Nie sú tu na kopírovanie.

---

Repozitár obsahuje poznámky, rekapitulácie, cvičenia a testy z prvého školského roka (1. a 2. semester) duálneho štúdia v IT odbore.

---

## 🗂️ Štruktúra

```
1.rok/
├── programovanie/       # Python cvičenia, Java zadania, testy
└── skola/
    ├── Angličtina (APA)
    ├── Linux (ZIL)
    ├── Nemčina (APN)
    ├── Programovanie a skriptovanie (PaS)
    ├── Spracovanie informácií (SIN)
    ├── Zákaznícka orientácia (ZOR)
    ├── Základy IKT systémov - hardware (ZIH)
    ├── Základy IKT systémov - windows (ZIW)
    ├── Základy počítačových sietí (ZPS)
    ├── Základy procesného riadenia (ZPR)
    ├── Základy riadenia podnikov a projektov (ZRP)
    └── cisco packet tracer/
```

---

## 📖 Predmety

### 🐧 Linux (ZIL)
Poznámky z každej hodiny, rekapitulácie pred testami, vizuálne schémy. Témy zahŕňajú: základné príkazy, súborový systém, oprávnenia, používatelia a skupiny, LVM, siete, SSH, systemd, sudo/visudo.
- Obsahuje materiály od učiteľa (PDF série 01–40) a prezentácie spolužiakov (bash, Kali, cloud, vim...)

### 🪟 Windows (ZIW)
Poznámky zo Windows Servera: Active Directory, GPO, DNS, DHCP, PowerShell, IIS, zálohovanie, Load Balancing.
- Priečinok `TESTY/` obsahuje zadania testov aj riešenia (AD, PowerShell, sieťové protokoly)
- Priložený `PowerShell CheatSheet.txt`

### 🌐 Počítačové siete (ZPS)
Poznámky z OSI/ISO modelu, smerovania (statické, OSPF, VLAN, STP) a sieťových protokolov.
- Priečinok `cisco packet tracer/` obsahuje `.pkt` súbory so všetkými praktickými cvičeniami zo semestra

### 💻 Programovanie a skriptovanie (PaS) + `programovanie/`
Python od základov (premenné, podmienky, cykly, zoznamy, reťazce, výnimky) a Java (OOP, triedy).
- Cvičenia zoradené podľa dátumu hodiny
- Obsahuje testy (`prvy test/`, `test 16.1/`) a riešenia spolužiaka na porovnanie (`denis z 5.12/`)

### 🖥️ Hardware (ZIH)
Základné súčasti PC, pamäte, magnetické médiá, RAID, kompresia, zálohovanie a archivácia.
- Priečinok `final test/` obsahuje materiály na prípravu na záverečný test

### ⚙️ Procesné riadenie (ZPR)
ITIL framework — Service Strategy, Design, Transition, Operation, CSI.
- Poznámky z hodín a PDF materiály ku každej fáze ITIL

### 🏢 Riadenie podnikov a projektov (ZRP)
Základy podnikania, s.r.o., SWOT analýza, outsourcing, SCRUM, projektové riziká.
- Obsahuje skupinové projekty (PayPal IKT prezentácia, outsourcing AWS)

### 📊 Spracovanie informácií (SIN)
Excel — adresovanie, textové funkcie, IF/AND, kontingenčné tabuľky, cvičenia s Employee list.

### 🇩🇪 Nemčina (APN)
Poznámky z každej hodiny, slovíčka (lekcie 1–6) vo formáte PNG, rekapitulácie pred testami.

### 🇬🇧 Angličtina (APA)
Poznámky a dokumenty vrátane prezentácie o Lockheed Martin.

### 👥 Zákaznícka orientácia (ZOR)
Firemná kultúra, typológia zákazníka, konflikt manažment, prezentácie.

---

## 🛠️ Použité nástroje

| Nástroj | Použitie |
|---|---|
| Python | PaS cvičenia a testy |
| Java | OOP zadania |
| PowerShell | ZIW skriptovanie |
| Cisco Packet Tracer | Sieťové cvičenia (ZPS) |
| Excalidraw | Vizuálne rekapitulácie |
| Microsoft Office | Poznámky, tabuľky, prezentácie |

---

## ℹ️ Poznámka

Poznámky sú písané prevažne po slovensky. Organizácia súborov odráža chronológiu školského roka, nie tematickú hierarchiu.
