import csv
import sys
from pathlib import Path


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "customer_id" not in reader.fieldnames:
            raise ValueError(
                f"{path} must contain a customer_id column"
            )

        records = {}
        for row in reader:
            customer_id = row["customer_id"]
            if customer_id in records:
                raise ValueError(
                    f"Duplicate customer_id {customer_id} in {path}"
                )
            records[customer_id] = row

        return records


def compare_data(source, target):
    source_ids = set(source)
    target_ids = set(target)

    missing = sorted(source_ids - target_ids)
    extra = sorted(target_ids - source_ids)
    mismatches = []

    for customer_id in sorted(source_ids & target_ids):
        for column in source[customer_id]:
            if source[customer_id][column] != target[customer_id].get(column):
                mismatches.append(
                    (customer_id, column,
                     source[customer_id][column],
                     target[customer_id].get(column))
                )

    print(f"Source records: {len(source)}")
    print(f"Target records: {len(target)}")
    print(f"Missing target records: {len(missing)}")
    print(f"Extra target records: {len(extra)}")
    print(f"Field mismatches: {len(mismatches)}")

    for customer_id in missing:
        print(f"Missing customer_id: {customer_id}")

    for customer_id in extra:
        print(f"Unexpected customer_id: {customer_id}")

    for customer_id, column, source_value, target_value in mismatches:
        print(
            f"Mismatch for {customer_id}, column {column}: "
            f"source={source_value!r}, target={target_value!r}"
        )

    return not missing and not extra and not mismatches


if __name__ == "__main__":
    folder = Path(__file__).parent
    try:
        source = load_csv(folder / "source_data.csv")
        target = load_csv(folder / "target_data.csv")
        valid = compare_data(source, target)
    except (OSError, ValueError, csv.Error) as error:
        print(f"Validation error: {error}")
        sys.exit(2)

    sys.exit(0 if valid else 1)
