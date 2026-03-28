def process_list(arr):
    # List comprehension обычно быстрее цикла с append за счет оптимизаций CPython.
    return [i**2 if i % 2 == 0 else i**3 for i in arr]


def process_list_gen(arr):
    # Генератор экономит память и удобен для потоковой обработки.
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3
