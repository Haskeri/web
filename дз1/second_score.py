import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    scores = list(map(int, data[1 : 1 + n]))
    unique_scores = sorted(set(scores))

    if len(unique_scores) >= 2:
        print(unique_scores[-2])
    elif unique_scores:
        print(unique_scores[0])


if __name__ == "__main__":
    main()
