[![Migration Validation Tests](https://github.com/sabeeh-alvi/aws-database-migration/actions/workflows/validation-tests.yml/badge.svg)](https://github.com/sabeeh-alvi/aws-database-migration/actions/workflows/validation-tests.yml)

# AWS Database Migration and Modernization

## Project Overview

This portfolio project documents a database migration workflow using AWS Database Migration Service (AWS DMS). It focuses on migration planning, source and target database configuration, replication tasks, data validation, security, and troubleshooting.

The project is designed to demonstrate understanding of database migration concepts and operational planning relevant to AWS cloud roles.

## Objectives

- Document a source-to-target database migration architecture.
- Explain the roles of AWS DMS and its replication instance.
- Describe full-load and change data capture (CDC) migration approaches.
- Identify networking, IAM, database permissions, and connectivity requirements.
- Define a data validation and post-migration verification plan.
- Document common migration errors and troubleshooting procedures.
- Consider cost controls and migration security.

## Planned Architecture

**Source database → AWS DMS replication instance → Target database**

The final design depends on source and target database engines, connectivity, permissions, and available AWS resources.

## Project Documentation

| Document | Description |
|---|---|
| [Architecture](docs/architecture.md) | Proposed migration flow and AWS component responsibilities |
| [Prerequisites Checklist](docs/prerequisites-checklist.md) | Compatibility, permissions, connectivity, and readiness checks |
| [IAM and Security](docs/iam-security.md) | Least privilege, credentials, networking, and data protection |
| [Data Validation Plan](docs/data-validation.md) | Row counts, record comparisons, CDC verification, and cutover criteria |
| [Troubleshooting Guide](docs/troubleshooting.md) | Diagnostic steps for permissions, connectivity, load, and replication issues |
| [Sample Migration Validation Report](docs/sample-validation-report.md) — expected results, validation scope, and project limitations |
| [Project Walkthrough](docs/project-walkthrough.md) — end-to-end explanation of the migration scenario, validation process, automated tests, security, and future implementation |

## Current Status

**Documentation and planning complete for this initial portfolio milestone.**

The repository contains a proposed architecture and supporting migration plans. No AWS DMS task, endpoint, database migration, or cutover is claimed as deployed or tested.

## Next Milestone

The next milestone is to add a small, reproducible demonstration using synthetic sample data to illustrate source-to-target validation. This can be developed and reviewed in GitHub without creating AWS resources.

## Scope and Status

**Current status:** Documentation and planning.

No database migration or AWS deployment is claimed as completed by this repository overview. Actual implementation, testing, and AWS DMS availability will be recorded only after verification.

## Tools and Services

- AWS Database Migration Service (AWS DMS)
- Amazon RDS, where applicable
- AWS Identity and Access Management (IAM)
- Amazon VPC and security groups
- GitHub for project documentation and version control

## Learning Outcomes

This project aims to demonstrate understanding of database migration planning, cloud networking, security, data validation, troubleshooting, and operational cost awareness.

## Disclaimer

This is a learning and portfolio project. Any future deployment must be checked against account permissions, service availability, and current AWS pricing before resources are created.
