# Sample Database Migration Validation Report

## 1. Purpose

This report demonstrates how source and target datasets can be compared during a database migration validation process.

The report uses synthetic CSV files included in this repository. It demonstrates validation logic and is not evidence of a live AWS Database Migration Service (AWS DMS) migration.

## 2. Validation Scope

The sample validation checks:

- Source and target record counts
- Missing records in the target dataset
- Extra records in the target dataset
- Differences in field values for matching records
- Duplicate customer IDs
- Automated test execution through GitHub Actions

## 3. Test Environment

| Item | Description |
|---|---|
| Source dataset | `examples/source_data.csv` |
| Target dataset | `examples/target_data.csv` |
| Validation script | `examples/validate_migration.py` |
| Unit tests | `examples/test_validate_migration.py` |
| Automation | GitHub Actions |
| Data type | Synthetic sample data |

## 4. Expected Results

The target dataset intentionally contains a discrepancy to demonstrate that the validation script can detect inconsistent data.

| Validation check | Expected result |
|---|---|
| Source and target comparison | Discrepancy detected |
| Unit tests | Pass |
| Expected-discrepancy workflow check | Pass when a discrepancy is detected |
| Live AWS DMS migration | Not performed |
| Production database validation | Not performed |

## 5. Interpretation

A successful GitHub Actions run confirms that the unit tests pass and that the workflow detects a discrepancy in the committed sample datasets.

A green workflow does not mean that the source and target datasets are identical. In this demonstration, detecting the intentional discrepancy is the expected outcome.

## 6. Limitations

This project currently demonstrates migration validation using synthetic CSV data. It does not validate a live database, an AWS DMS replication task, transaction consistency, database schema compatibility, or production cutover readiness.

## 7. Next Steps

Potential future improvements include:

- Generate a detailed report containing actual record counts and mismatch details.
- Add tests for duplicate identifiers and malformed CSV files.
- Validate larger datasets.
- Integrate database-level checks if an authorized test environment becomes available.

**Project status:** Portfolio demonstration with automated tests. No live AWS migration is claimed.
