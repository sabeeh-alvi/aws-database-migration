# AWS Database Migration — Project Walkthrough

## 1. Project Overview

This portfolio project demonstrates core database migration planning and data validation concepts using a simulated migration scenario.

The goal is to show how an engineer can plan a migration, document security requirements, compare source and target datasets, and automate validation checks with GitHub Actions.

**Current status:** Portfolio demonstration. No live AWS DMS migration or production database migration has been performed.

## 2. Business Scenario

An organization needs to migrate customer data from a source database to a target database.

The migration must preserve data accuracy and identify discrepancies before the target is accepted. A reliable validation process helps reduce the risk of missing records, unexpected values, and incomplete migrations.

## 3. Proposed AWS Architecture

The documented architecture considers these AWS services:

- **AWS Database Migration Service (AWS DMS):** Proposed mechanism for replicating data between supported source and target databases.
- **Amazon RDS:** Proposed managed relational database target.
- **AWS Identity and Access Management (IAM):** Controls permissions for migration resources and operators.
- **Amazon CloudWatch:** A potential source of operational monitoring and logs.

These services are part of the proposed architecture; they have not been deployed as part of this portfolio demonstration.

See [architecture.md](architecture.md) for the architecture details.

## 4. Sample Data

The repository contains two synthetic datasets:

- `examples/source_data.csv`
- `examples/target_data.csv`

The target dataset intentionally contains a discrepancy. This provides a reproducible example for testing whether the validation logic detects inconsistent data.

## 5. Validation Process

The validation script is located at `examples/validate_migration.py`.

The demonstration checks for:

1. Duplicate customer identifiers.
2. Records missing from the target dataset.
3. Unexpected extra target records.
4. Field-value differences between matching records.
5. Errors that prevent the comparison from completing.

The unit tests in `examples/test_validate_migration.py` exercise representative comparison scenarios.

## 6. Automated Testing

GitHub Actions runs the Python unit tests and verifies that the sample datasets contain a detectable discrepancy.

The workflow is designed to succeed when the tests pass and the intentional discrepancy is detected.

**Important:** A green workflow confirms that the expected checks behaved as designed. It does not mean that the source and target datasets match, nor does it prove that an AWS DMS task has completed successfully.

See [data-validation.md](data-validation.md) and [sample-validation-report.md](sample-validation-report.md).

## 7. Security Considerations

A real migration would require appropriately scoped IAM permissions, secure database credentials, network connectivity, encryption, and access controls.

Permissions should follow least-privilege principles. Database credentials should not be committed to GitHub.

See [iam-security.md](iam-security.md) for the project's security considerations.

## 8. Troubleshooting Approach

A real migration may fail because of insufficient permissions, network connectivity, incompatible data types, schema differences, or replication errors.

A structured troubleshooting process should identify the failing component, examine relevant logs, verify configuration and permissions, and repeat validation after corrective action.

See [troubleshooting.md](troubleshooting.md).

## 9. What Would Be Needed for a Real Migration?

A production implementation would require an authorized AWS environment and a suitable test plan. Typical additional steps include:

1. Confirm source and target database compatibility.
2. Configure secure connectivity and required permissions.
3. Create and test migration endpoints.
4. Configure an AWS DMS replication instance or suitable supported replication compute.
5. Create and run a migration task.
6. Validate schema, records, and ongoing changes.
7. Plan cutover, rollback, monitoring, and operational acceptance.

These steps are future implementation work, not completed project activities.

## 10. Skills Demonstrated

- AWS migration architecture planning
- IAM security and least-privilege concepts
- Python-based data validation
- CSV processing and error handling
- Unit testing
- GitHub Actions continuous integration
- Technical documentation and troubleshooting

## Conclusion

This project demonstrates how migration planning, synthetic data comparison, automated tests, and clear technical documentation can be combined into a reproducible portfolio exercise.

It provides a foundation for future hands-on database migration work in an authorized environment.
