import sys

def swap_line(line: str) -> str:
    line = line.rstrip("\n")

    # Only process lines containing the indicator
    if "-" not in line:
        return line

    left, right = line.split("-", 1)

    # Strip spaces and swap
    left = left.strip()
    right = right.strip()

    return f"{right} - {left}"


def main():
    for line in sys.stdin:
        if line.strip() == "":
            print("")
            continue

        print(swap_line(line))


if __name__ == "__main__":
    main()
