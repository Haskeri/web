def classify_number(n: int) -> str:
    if n % 2 == 1:
        return "Weird"
    if 2 <= n <= 5:
        return "Not Weird"
    if 6 <= n <= 20:
        return "Weird"
    return "Not Weird"


if __name__ == "__main__":
    number = int(input().strip())
    print(classify_number(number))
