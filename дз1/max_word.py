import re
from pathlib import Path


def main() -> None:
    file_path = Path(__file__).with_name("example.txt")
    text = file_path.read_text(encoding="utf-8")
    words = re.findall(r"[0-9A-Za-zА-Яа-яЁё]+", text)

    if not words:
        return

    max_length = max(len(word) for word in words)
    for word in words:
        if len(word) == max_length:
            print(word)


if __name__ == "__main__":
    main()
