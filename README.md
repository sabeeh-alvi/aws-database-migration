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

**Implemented
