import sys


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    intervals = []
    index = 1

    for _ in range(n):
        start = data[index]
        end = data[index + 1]
        intervals.append((start, end))
        index += 2

    moment = data[index] if index < len(data) else 0
    passengers = sum(1 for start, end in intervals if start <= moment <= end)
    print(passengers)


if __name__ == "__main__":
    main()
