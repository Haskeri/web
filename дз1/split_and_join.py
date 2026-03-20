import sys


def main() -> None:
    line = sys.stdin.read()
    if line.endswith("\n"):
        line = line[:-1]
    print("-".join(line.split()))


if __name__ == "__main__":
    main()
