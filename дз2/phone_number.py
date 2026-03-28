def normalize_phone(number):
    digits = "".join(ch for ch in number if ch.isdigit())
    if len(digits) < 10:
        raise ValueError(f"Некорректный номер: {number}")
    core = digits[-10:]
    return f"+7 ({core[:3]}) {core[3:6]}-{core[6:8]}-{core[8:]}"


def wrapper(f):
    def fun(l):
        normalized = [normalize_phone(number) for number in l]
        return f(normalized)
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
