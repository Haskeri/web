import random


def circle_square_mk(r, n):
    if n <= 0:
        raise ValueError("n должно быть положительным")
    if r < 0:
        raise ValueError("r должно быть неотрицательным")

    rng = random.Random(0)
    inside = 0
    side = 2 * r

    for _ in range(n):
        x = rng.uniform(-r, r)
        y = rng.uniform(-r, r)
        if x * x + y * y <= r * r:
            inside += 1

    return (inside / n) * (side**2)


# Погрешность метода Монте-Карло в среднем убывает примерно как 1/sqrt(n):
# при увеличении n в 100 раз типичная ошибка снижается примерно в 10 раз.
