def main() -> None:
    a = int(input().strip())
    b = int(input().strip())

    if b == 0:
        print("Division by zero")
        print("Division by zero")
        return

    print(a // b)
    print(a / b)


if __name__ == "__main__":
    main()
