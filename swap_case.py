import sys


def main() -> None:
    text = sys.stdin.read()
    if text.endswith("\n"):
        text = text[:-1]
    print(text.swapcase())


if __name__ == "__main__":
    main()
