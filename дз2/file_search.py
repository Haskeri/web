import os
import sys
from pathlib import Path


def find_file(filename, start_dir=None):
    root_dir = Path(__file__).resolve().parent if start_dir is None else Path(start_dir)

    for current_root, dirs, files in os.walk(root_dir):
        dirs.sort()
        files.sort()
        if filename in files:
            return Path(current_root) / filename
    return None


def read_first_lines(file_path, line_count=5):
    with Path(file_path).open(encoding="utf-8") as source:
        lines = []
        for _ in range(line_count):
            line = source.readline()
            if line == "":
                break
            lines.append(line.rstrip("\n"))
        return lines


def search_and_read(filename, start_dir=None):
    found_path = find_file(filename, start_dir=start_dir)
    if found_path is None:
        return f"Файл {filename} не найден"
    return "\n".join(read_first_lines(found_path, 5))


def main(argv=None):
    arguments = sys.argv[1:] if argv is None else argv
    if not arguments:
        return ""
    result = search_and_read(arguments[0])
    print(result)
    return result


if __name__ == "__main__":
    main()
