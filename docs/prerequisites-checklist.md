# AWS DMS Migration Prerequisites Checklist

## Purpose

Use this checklist before attempting an AWS Database Migration Service (AWS DMS) migration. The checklist helps identify compatibility, permissions, networking, validation, and cost issues before resources are created.

**Status:** Planning checklist. Items are not marked complete until verified.

## 1. Migration Scope

- [ ] Identify the source database engine and version.
- [ ] Identify the target database engine and version.
- [ ] Confirm whether the migration is homogeneous (same engine family) or heterogeneous (different engine families).
- [ ] Estimate database size and expected change rate.
- [ ] Decide whether full load, CDC, or full load plus CDC is required.
- [ ] Identify downtime limits and the planned cutover window.
- [ ] Confirm that the selected source and target are supported for the intended migration.

## 2. Source Database

- [ ] Confirm the source database is available and healthy.
- [ ] Create or identify a migration user with the required permissions.
- [ ] Verify network reachability from the planned replication instance.
- [ ] Check source-specific requirements for full load and CDC.
- [ ] Confirm that backups or another recovery method are available.
- [ ] Identify sensitive data and any requirements for protecting it.

## 3. Target Database

- [ ] Confirm the target engine, version, and configuration.
- [ ] Ensure sufficient storage and compute capacity.
- [ ] Determine whether schemas and database objects must be created before migration.
- [ ] Verify target permissions for creating or modifying required objects.
- [ ] Confirm connectivity from the planned replication instance.
- [ ] Define how existing target data will be handled.

## 4. AWS DMS and IAM

- [ ] Verify access to AWS DMS in the intended AWS account and Region.
- [ ] Confirm that the account is authorized to create or use the required resources.
- [ ] Review the required IAM roles and policies.
- [ ] Confirm whether a replication instance or serverless replication is appropriate and supported.
- [ ] Verify that the selected migration approach supports the required features.
- [ ] Review current AWS pricing before starting any resources.

## 5. Networking

- [ ] Identify the VPC and subnets for the migration components.
- [ ] Verify routing between AWS DMS and the source and target databases.
- [ ] Review security groups and network access controls.
- [ ] Verify DNS resolution and database port connectivity.
- [ ] Determine whether VPN, Direct Connect, peering, or another connectivity method is needed.
- [ ] Avoid exposing database ports publicly as a shortcut.

## 6. Validation and Cutover

- [ ] Define source-to-target row-count checks.
- [ ] Identify important tables and business-level validation queries.
- [ ] Define how data discrepancies will be investigated.
- [ ] Establish acceptable replication lag, if CDC is used.
- [ ] Define cutover criteria and who approves the switch.
- [ ] Prepare a rollback plan.
- [ ] Define post-migration application and monitoring checks.

## 7. Cost and Cleanup

- [ ] Confirm the cost implications of replication, storage, networking, and target database resources.
- [ ] Confirm whether any applicable free usage or credits cover the planned services.
- [ ] Set a budget alert where appropriate.
- [ ] Identify all resources that must be stopped or deleted after testing.
- [ ] Verify that cleanup will not delete data that must be retained.
- [ ] Check the account after cleanup for remaining billable resources.

## Completion Criteria

The migration is ready to be attempted only when the required compatibility, permission, connectivity, validation, recovery, and cost checks have been verified.

This checklist documents readiness criteria. It does not mean a migration has been executed or that AWS DMS permissions are available in a particular account.
