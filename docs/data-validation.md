# Database Migration Data Validation Plan

## Purpose

This plan describes how to assess data consistency after a database migration using AWS Database Migration Service (AWS DMS).

**Status:** Planned validation approach. No source-to-target comparison has been executed for this project.

## 1. Validation Objectives

The validation process should establish whether:

- Expected tables and records exist at the target.
- Important column values match between source and target.
- Data types and transformations behave as intended.
- Relationships and application-critical constraints remain valid.
- Ongoing changes have been replicated when CDC is used.
- The target application behaves correctly before cutover.

## 2. Pre-Migration Baseline

Before starting a migration:

1. Identify critical tables and business entities.
2. Record source row counts for selected tables.
3. Identify primary keys and important relationships.
4. Record known data-quality issues that should not be mistaken for migration errors.
5. Identify columns requiring special treatment, such as timestamps, decimals, binary data, or transformed values.
6. Define acceptable validation tolerances and who approves the results.

Baseline queries should be read-only wherever possible.

## 3. Full-Load Validation

After the initial load:

- Confirm that the migration task reports the expected completion status.
- Review table-level load statistics and any reported errors.
- Compare source and target row counts for selected tables.
- Check for missing or unexpected tables.
- Compare selected records using primary keys.
- Investigate differences caused by filters, transformations, or concurrent source changes.

Equal row counts alone do not prove that all column values are correct.

## 4. Data Comparison Methods

### Row counts

Compare counts for critical tables on both systems. For example, if the source contains 1,000 customer records and the target contains 1,000, the counts agree, but individual records still need validation.

### Key-based comparisons

Select representative records by primary key and compare important column values.

### Aggregate checks

Compare suitable totals, such as invoice totals or quantities, where the source and target use equivalent business rules and numeric precision.

### Checksums or hashes

For selected datasets, compare normalized row values or hashes. The normalization process must account for data types, nulls, character encoding, and timestamp representation.

### Application-level validation

Run representative application queries or business workflows against the target in a controlled test environment.

## 5. CDC Validation

When change data capture is used:

- Review the task status and table-level statistics.
- Monitor replication latency and pending changes.
- Generate controlled test changes in an approved test environment.
- Verify that inserts, updates, and deletes are reflected at the target as expected.
- Check the final synchronization state before cutover.

CDC support and behavior depend on the database engine, logging configuration, and migration task settings.

## 6. Discrepancy Investigation

For every mismatch:

1. Identify the affected table and primary key.
2. Compare source and target values.
3. Check migration logs and table-level error details.
4. Review mappings, filters, data types, and transformations.
5. Determine whether the difference is expected or requires correction.
6. Record the root cause and corrective action.
7. Repeat the relevant validation after correction.

Do not modify production data merely to make validation counts match without understanding the discrepancy.

## 7. Cutover Acceptance Criteria

Cutover should proceed only after the responsible team confirms that:

- Critical tables meet the agreed validation criteria.
- No unresolved migration errors violate the acceptance criteria.
- CDC has caught up, if applicable.
- Application tests pass against the target.
- Security and access controls are in place.
- A rollback plan is available and understood.

## 8. Validation Record Template

| Check | Expected result | Actual result | Status |
|---|---|---|---|
| Migration task | Successful completion | Not run | Not verified |
| Critical table row counts | Within agreed criteria | Not run | Not verified |
| Key-based record checks | Values agree | Not run | Not verified |
| CDC synchronization | Within agreed lag target, if applicable | Not run | Not verified |
| Application smoke tests | Pass | Not run | Not verified |

## Limitations

Validation methods must be adapted to the source and target database engines. This plan documents intended checks; it does not claim that migration or validation has occurred.

## Automated Test Results

The migration validation logic is covered by automated Python unit tests executed through GitHub Actions.

The test suite covers:

- Matching source and target records.
- Detection of changed field values.
- Detection of records missing from the target.
- Detection of unexpected extra target records.
- Duplicate customer ID rejection: Confirms that the CSV loader raises a validation error when a customer ID appears more than once.
- Required CSV header validation: Confirms that the CSV loader rejects files that do not contain the required `customer_id` column.

**Latest recorded result:** Passed (green GitHub Actions check).

These unit tests use synthetic sample records. They validate the comparison logic but do not demonstrate a live AWS DMS migration or verify the actual CSV datasets against a deployed database.

## Automated CSV Validation in GitHub Actions

The GitHub Actions workflow runs the migration-validation unit tests and verifies that the committed sample source and target CSV datasets contain a detectable discrepancy.

The workflow succeeds when:
- The migration-validation unit tests pass.
- A discrepancy between the sample datasets is detected as expected.

This demonstrates automated validation of sample migration data in a repeatable CI workflow. The datasets are synthetic examples; this result does not represent a live AWS DMS migration or a production database validation.

**Status:** Successfully executed in GitHub Actions.
