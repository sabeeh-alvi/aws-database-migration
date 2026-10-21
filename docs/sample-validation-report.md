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

## 4. Validation Results

The sample validation compared four source records against four target records.

| Validation check | Actual result |
|---|---|
| Source records | 4 |
| Target records | 4 |
| Missing target records | 0 |
| Extra target records | 0 |
| Field mismatches | 1 |
| Overall data comparison | Discrepancy detected |

### Detected discrepancy

| Customer ID | Field | Source value | Target value |
|---|---|---|---|
| 1002 | city | Mississauga | Milton |

All four customer IDs are present in both datasets. However, customer `1002` has a different city value in the target dataset.

### Interpretation

The validation script should return exit code `1` because the source and target datasets are not identical. This is the expected outcome for the intentionally inconsistent sample data.

These results were calculated from the CSV contents in the repository. They are not represented as a captured execution log from the script.

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

## 8. Console Output Example

The following output is derived from the committed sample CSV contents and the validation script's logic. It is an illustrative example, not a captured execution log.

```text
Source records: 4
Target records: 4
Missing target records: 0
Extra target records: 0
Field mismatches: 1
Mismatch for 1002, column city: source='Mississauga', target='Milton'
```

### Expected Exit Code

The validation script returns exit code `1` because a field mismatch was detected.

- `0` — Source and target records match.
- `1` — Data comparison found a discrepancy.
- `2` — A validation error prevented normal comparison, such as a missing file or duplicate customer ID.

### Why This Matters

A useful migration validation process must report discrepancies clearly and return an appropriate status so automated workflows can respond to the outcome.
