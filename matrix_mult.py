import sys


def multiply_matrices(matrix_a, matrix_b, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = matrix_a[i][k]
            if aik == 0:
                continue
            for j in range(n):
                result[i][j] += aik * matrix_b[k][j]
    return result


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    index = 1

    matrix_a = []
    for _ in range(n):
        row = list(map(int, data[index : index + n]))
        matrix_a.append(row)
        index += n

    matrix_b = []
    for _ in range(n):
        row = list(map(int, data[index : index + n]))
        matrix_b.append(row)
        index += n

    result = multiply_matrices(matrix_a, matrix_b, n)
    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
