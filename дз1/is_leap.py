import sys


def is_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main() -> None:
    data = sys.stdin.read().strip()
    if not data:
        return
    print(is_leap(int(data)))


if __name__ == "__main__":
    main()
