import sys
from collections import Counter


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return

    first = lines[0].strip()
    second = lines[1].strip()
    print("YES" if Counter(first) == Counter(second) else "NO")


if __name__ == "__main__":
    main()
