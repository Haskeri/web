cube = lambda x: x**3

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    values = [0, 1]
    while len(values) < n:
        values.append(values[-1] + values[-2])
    return values

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
