
import csv
import tempfile
import unittest
from pathlib import Path

from validate_migration import compare_data, load_csv


class TestMigrationValidation(unittest.TestCase):

    def test_matching_records_pass(self):
        source = {
            "1": {"customer_id": "1", "city": "Toronto"},
            "2": {"customer_id": "2", "city": "Ottawa"},
        }
        target = {
            "1": {"customer_id": "1", "city": "Toronto"},
            "2": {"customer_id": "2", "city": "Ottawa"},
        }

        self.assertTrue(compare_data(source, target))

    def test_changed_field_fails(self):
        source = {
            "1": {"customer_id": "1", "city": "Toronto"},
        }
        target = {
            "1": {"customer_id": "1", "city": "Montreal"},
        }

        self.assertFalse(compare_data(source, target))

    def test_missing_record_fails(self):
        source = {
            "1": {"customer_id": "1", "city": "Toronto"},
            "2": {"customer_id": "2", "city": "Ottawa"},
        }
        target = {
            "1": {"customer_id": "1", "city": "Toronto"},
        }

        self.assertFalse(compare_data(source, target))

    def test_extra_record_fails(self):
        source = {
            "1": {"customer_id": "1", "city": "Toronto"},
        }
        target = {
            "1": {"customer_id": "1", "city": "Toronto"},
            "2": {"customer_id": "2", "city": "Ottawa"},
        }

        self.assertFalse(compare_data(source, target))

    def test_duplicate_customer_id_is_rejected(self):
        
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "duplicate_customers.csv"

            with csv_path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["customer_id", "city"])
                writer.writerow(["1", "Toronto"])
                writer.writerow(["1", "Ottawa"])

            with self.assertRaisesRegex(
                ValueError, "Duplicate customer_id 1"
            ):
                load_csv(csv_path)

    def test_missing_customer_id_column_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "invalid_header.csv"

            with csv_path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["first_name", "city"])
                writer.writerow(["Amina", "Toronto"])

            with self.assertRaisesRegex(
                ValueError, "must contain a customer_id column"
            ):
                load_csv(csv_path)


if __name__ == "__main__":
    unittest.main()
