VOWELS = set("AEIOU")


def main() -> None:
    text = input().strip().upper()
    text_length = len(text)
    kevin_score = 0
    stuart_score = 0

    for index, char in enumerate(text):
        points = text_length - index
        if char in VOWELS:
            kevin_score += points
        else:
            stuart_score += points

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
