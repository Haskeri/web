def _validate_n(n):
    if not isinstance(n, int):
        raise TypeError("n должен быть целым числом")
    if n < 0:
        raise ValueError("n должен быть неотрицательным")


def _product_range(left, right):
    if left > right:
        return 1
    if left == right:
        return left
    if right - left == 1:
        return left * right

    middle = (left + right) // 2
    return _product_range(left, middle) * _product_range(middle + 1, right)


def fact_rec(n):
    _validate_n(n)
    if n < 2:
        return 1
    return _product_range(1, n)


def fact_it(n):
    _validate_n(n)
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


# Сравнение скорости (timeit, CPython 3.11): итеративная версия обычно быстрее
# на малых/средних n за счет отсутствия рекурсивных вызовов; рекурсивная версия
# удобнее для демонстрации подхода, но в среднем имеет больший оверхед.


if __name__ == "__main__":
    n = int(input().strip())
    print(fact_it(n))
