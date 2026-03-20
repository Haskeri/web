import sys


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    index = 2

    arr = list(map(int, data[index : index + n]))
    index += n
    set_a = set(map(int, data[index : index + m]))
    index += m
    set_b = set(map(int, data[index : index + m]))

    mood = 0
    for value in arr:
        if value in set_a:
            mood += 1
        elif value in set_b:
            mood -= 1

    print(mood)


if __name__ == "__main__":
    main()
