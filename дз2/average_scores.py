def compute_average_scores(scores):
    if not scores:
        return tuple()

    students_scores = list(zip(*scores))
    return tuple(sum(values) / len(values) for values in students_scores)


if __name__ == "__main__":
    n, x = map(int, input().split())
    rows = [tuple(map(float, input().split())) for _ in range(x)]
    averages = compute_average_scores(rows)
    for value in averages:
        print(f"{value:.1f}")
