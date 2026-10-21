# Database Migration Architecture

## 1. Overview

This document describes a planned migration architecture using AWS Database Migration Service (AWS DMS). The design separates the source database, replication infrastructure, and target database so each component's responsibilities are clear.

**Status:** Proposed architecture. No AWS resources have been deployed as part of this documentation.

## 2. Logical Architecture

```text
Source Database
      |
      | Read source data and changes
      v
AWS DMS Replication Instance
      |
      | Apply migrated data and changes
      v
Target Database
      |
      v
Data Validation and Application Verification
```

The source and target may be on-premises databases, Amazon RDS databases, or other supported database environments. Exact compatibility depends on the selected engines and AWS DMS support.

## 3. Component Responsibilities

### Source Database

- Stores the original application data.
- Must be reachable from the AWS DMS replication instance.
- Requires suitable database permissions and, for CDC, the appropriate change logging or transaction-log configuration.

### AWS DMS Replication Instance

- Provides the compute resources used by AWS DMS replication tasks.
- Connects to source and target endpoints.
- Performs full-load migration, change data capture (CDC), or both, depending on task configuration.
- Requires appropriate network connectivity, IAM permissions, and capacity planning.

### Target Database

- Receives migrated data.
- Must have compatible schema objects and sufficient storage.
- Requires appropriate permissions for the migration task.
- Must be validated before an application is switched over.

### Validation

- Compares source and target data using appropriate counts, checksums, or business-level checks.
- Identifies missing, duplicated, or inconsistent records.
- Confirms application functionality before cutover.

## 4. Migration Approaches

**Full load:** Copies existing data from the source to the target.

**Full load plus CDC:** Loads existing data and then replicates supported ongoing changes. This can reduce the time needed to synchronize a changing source before cutover.

**CDC only:** Replicates ongoing changes when the target has already been initialized appropriately.

Supported behavior and prerequisites vary by database engine and migration configuration.

## 5. Networking and Security

The planned design must account for:

- Routing between the replication instance and both database endpoints.
- Security-group rules and network access controls.
- DNS resolution and database port accessibility.
- Encryption in transit and appropriate credential handling.
- Least-privilege database users and IAM policies.
- Private connectivity where appropriate.

Database ports should not be exposed publicly simply to make a migration work.

## 6. Cutover Plan

1. Confirm source and target readiness.
2. Verify initial load completion.
3. Check CDC status and replication lag, if CDC is used.
4. Validate data and application behavior.
5. Define a write-freeze or synchronization strategy.
6. Switch application connections only after agreed validation criteria are met.
7. Monitor the target and retain a documented rollback plan.

## 7. Constraints and Assumptions

The final architecture depends on the database engines, source location, target location, account permissions, supported AWS DMS features, network connectivity, and cost limits. These details must be verified before implementation.

## 8. Verification Status

This document describes a proposed architecture. It does not establish that endpoints, replication tasks, data migration, CDC, or cutover have been tested.
