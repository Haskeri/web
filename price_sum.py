import csv
from pathlib import Path


def main() -> None:
    file_path = Path(__file__).with_name("products.csv")
    adults_total = 0.0
    pensioners_total = 0.0
    children_total = 0.0

    with file_path.open(encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            adults_total += float(row["Взрослый"])
            pensioners_total += float(row["Пенсионер"])
            children_total += float(row["Ребенок"])

    print(f"{adults_total:.2f} {pensioners_total:.2f} {children_total:.2f}")


if __name__ == "__main__":
    main()
