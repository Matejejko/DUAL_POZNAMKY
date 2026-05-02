import sys

def sort_lines(lines):
    # Strip newlines and remove empty lines
    cleaned = [line.rstrip("\n") for line in lines if line.strip() != ""]

    # Sort by first visible character, case-insensitive
    return sorted(
        cleaned,
        key=lambda line: line.lstrip()[0].lower()
    )

def main():
    lines = sys.stdin.read().splitlines()

    sorted_lines = sort_lines(lines)

    for line in sorted_lines:
        print(line)

if __name__ == "__main__":
    main()
