import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0].strip())
    commands = lines[1 : 1 + n]
    arr = []
    output = []

    for command_line in commands:
        parts = command_line.split()
        if not parts:
            continue

        command = parts[0]

        if command == "insert":
            arr.insert(int(parts[1]), int(parts[2]))
        elif command == "print":
            output.append(str(arr))
        elif command == "remove":
            try:
                arr.remove(int(parts[1]))
            except ValueError:
                pass
        elif command == "append":
            arr.append(int(parts[1]))
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            if arr:
                arr.pop()
        elif command == "reverse":
            arr.reverse()

    if output:
        print("\n".join(output))


if __name__ == "__main__":
    main()
