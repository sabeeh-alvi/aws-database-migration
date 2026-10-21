import unittest

from validate_migration import compare_data


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


if __name__ == "__main__":
    unittest.main()
