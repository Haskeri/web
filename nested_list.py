import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0].strip())
    students = []
    index = 1

    for _ in range(n):
        name = lines[index]
        score = float(lines[index + 1].strip())
        students.append((name, score))
        index += 2

    unique_scores = sorted({score for _, score in students})
    target_score = unique_scores[1] if len(unique_scores) >= 2 else unique_scores[0]
    names = sorted(name for name, score in students if score == target_score)
    print("\n".join(names))


if __name__ == "__main__":
    main()
