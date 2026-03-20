import sys


def parse_item(line: str):
    parts = line.split()
    if len(parts) < 3:
        return None
    name = " ".join(parts[:-2])
    weight = float(parts[-2])
    value = float(parts[-1])
    return name, weight, value


def format_number(value: float) -> str:
    if abs(value) < 0.0005:
        value = 0.0
    return f"{value:.2f}"


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    first_line = lines[0].split()
    capacity = float(first_line[0])
    items_count = int(first_line[1])

    items = []
    for line in lines[1 : 1 + items_count]:
        parsed = parse_item(line)
        if parsed is None:
            continue
        name, weight, value = parsed
        ratio = float("inf") if weight == 0 and value > 0 else (value / weight if weight else 0.0)
        items.append((name, weight, value, ratio))

    items.sort(key=lambda item: (item[3], item[2]), reverse=True)

    selected = []
    for name, weight, value, _ in items:
        if weight == 0:
            if value > 0:
                selected.append((name, 0.0, value))
            continue

        if capacity <= 0:
            break

        taken_weight = min(weight, capacity)
        if taken_weight <= 0:
            continue
        taken_value = value * (taken_weight / weight)
        selected.append((name, taken_weight, taken_value))
        capacity -= taken_weight

    selected.sort(key=lambda item: item[2], reverse=True)
    for name, taken_weight, taken_value in selected:
        print(f"{name} {format_number(taken_weight)} {format_number(taken_value)}")


if __name__ == "__main__":
    main()
