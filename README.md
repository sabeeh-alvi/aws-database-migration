[![Migration Validation Tests](https://github.com/sabeeh-alvi/aws-database-migration/actions/workflows/validation-tests.yml/badge.svg)](https://github.com/sabeeh-alvi/aws-database-migration/actions/workflows/validation-tests.yml)

# AWS Database Migration and Modernization

## Project Overview

This portfolio project demonstrates database migration planning and source-to-target data validation using Python and synthetic CSV datasets. It documents a proposed migration workflow using AWS Database Migration Service (AWS DMS), including migration architecture, source and target database configuration, replication concepts, validation, security, and troubleshooting.

The project is designed to demonstrate practical understanding of database migration concepts and operational planning relevant to AWS cloud roles.

## Objectives

- Document a source-to-target database migration architecture.
- Explain the roles of AWS DMS and its replication instance.
- Describe full-load and change data capture (CDC) migration approaches.
- Identify networking, IAM, database permissions, and connectivity requirements.
- Implement a reproducible source-to-target data validation demonstration.
- Test validation logic against matching records, missing records, extra records, and field mismatches.
- Handle invalid CSV inputs, including duplicate customer IDs, missing required headers, and empty files.
- Automate validation tests with GitHub Actions.
- Document common migration errors, security considerations, and cost controls.

## Planned Architecture

**Proposed AWS migration architecture:**

Source database → AWS DMS replication instance → Target database

The final design depends on the source and target database engines, connectivity, permissions, and available AWS resources.

**Implemented portfolio demonstration:**

Synthetic source CSV + synthetic target CSV → Python validation script → Record comparison and discrepancy report → Automated tests in GitHub Actions

The CSV demonstration illustrates validation concepts without requiring an AWS database migration or creating AWS resources.

## Project Documentation

| Document | Description |
|---|---|
| [Architecture](docs/architecture.md) | Proposed migration flow and AWS component responsibilities |
| [Prerequisites Checklist](docs/prerequisites-checklist.md) | Compatibility, permissions, connectivity, and readiness checks |
| [IAM and Security](docs/iam-security.md) | Least privilege, credentials, networking, and data protection |
| [Data Validation Plan](docs/data-validation.md) | Record comparisons, validation rules, automated tests, and future migration verification |
| [Troubleshooting Guide](docs/troubleshooting.md) | Diagnostic guidance for permissions, connectivity, loading, and replication issues |
| [Sample Migration Validation Report](docs/sample-validation-report.md) | Expected results, detected discrepancy, validation scope, and limitations |
| [Project Walkthrough](docs/project-walkthrough.md) | End-to-end explanation of the migration scenario, validation process, automated tests, security, and future implementation |

## Current Status

**Initial portfolio milestone complete: migration planning and automated data validation demonstration.**

The repository includes:

- A proposed AWS DMS migration architecture and supporting planning documentation.
- A Python CSV validation script that compares source and target records.
- Synthetic source and target datasets containing an intentional data discrepancy.
- Seven automated unit tests covering matching records, changed fields, missing records, extra records, duplicate customer IDs, missing required headers, and empty CSV files.
- A GitHub Actions workflow that runs the unit tests and verifies that the sample discrepancy is detected.
- A sample validation report and project walkthrough.
- Documentation covering security, prerequisites, troubleshooting, and validation planning.

The GitHub Actions workflow has passed. This verifies the automated checks in the repository; it does not establish that an AWS database migration has been performed.

**AWS implementation status:** No AWS DMS task, endpoint, database migration, or cutover is claimed as deployed or tested.

## Next Milestone

Potential future improvements include:

- Expanding automated validation scenarios and edge-case coverage.
- Improving structured validation reports and error handling.
- Documenting engine-specific migration requirements.
- Planning implementation steps after AWS permissions, service availability, and cost constraints have been verified.
- Recording any future AWS deployment or migration only after it has actually been performed and verified.

## Tools and Technologies

- **Python** — CSV loading, record comparison, discrepancy detection, and unit testing.
- **CSV** — Synthetic source and target datasets.
- **Python unittest** — Automated validation tests.
- **GitHub Actions** — Continuous integration for automated testing.
- **GitHub** — Source control and portfolio documentation.
- **AWS Database Migration Service (AWS DMS)** — Proposed migration service.
- **Amazon RDS** — Potential target or source database, depending on the migration scenario.
- **AWS Identity and Access Management (IAM)** — Access control and security planning.
- **Amazon VPC and security groups** — Network connectivity and security planning.

## Learning Outcomes

This project demonstrates understanding of:

- Database migration architecture and planning.
- AWS migration service concepts.
- Source-to-target data validation.
- Missing, extra, and mismatched record detection.
- Input validation and duplicate record handling.
- Automated testing and continuous integration.
- IAM, networking, and data protection considerations.
- Migration troubleshooting and cost awareness.

## Disclaimer

This is a learning and portfolio project. The validation demonstration uses synthetic CSV data and does not require a live database. AWS migration architecture and implementation plans are documented for educational purposes.

No live AWS migration or production deployment is claimed. Any future deployment must be evaluated against account permissions, service availability, security requirements, and current AWS pricing before resources are created.
