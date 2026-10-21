# AWS DMS Troubleshooting Guide

## Purpose

This guide describes common AWS Database Migration Service (AWS DMS) problem categories, possible causes, and a structured approach to investigation.

**Status:** Reference documentation. The issues below are troubleshooting scenarios, not failures observed or resolved in a deployment for this project.

## 1. Access Denied or Insufficient Permissions

**Possible symptoms**
- The AWS console refuses to create or modify a resource.
- An API request returns an authorization error.
- A migration task cannot access a required resource.

**Possible causes**
- Missing IAM permissions.
- A restrictive permissions boundary, service control policy, or resource policy.
- Missing or incorrect service-role trust configuration.
- Insufficient database privileges.

**Investigation**
1. Record the exact error and identify the denied action.
2. Determine whether the failure involves AWS IAM or database authorization.
3. Review the relevant identity policy, resource policy, permissions boundary, and organizational restrictions as applicable.
4. Confirm that the required service role can be assumed.
5. Request only the additional permissions needed, through the account administrator.

Do not attempt to bypass organizational controls or grant administrator access as a routine fix.

## 2. Source or Target Endpoint Connection Failure

**Possible symptoms**
- An endpoint connection test fails.
- A replication task cannot connect to a database.
- The task reports connection or network errors.

**Possible causes**
- Incorrect hostname, port, database name, or credentials.
- Security-group rules blocking traffic.
- Missing routes or incorrect subnet configuration.
- DNS resolution failures.
- Database service unavailable or listening on a different port.

**Investigation**
1. Verify endpoint settings without exposing credentials.
2. Confirm that the database is available.
3. Check routing, security groups, network ACLs, and DNS resolution.
4. Verify the database port and required network path.
5. Check the endpoint test result and relevant logs.

Avoid making a database publicly accessible simply to resolve connectivity problems.

## 3. Authentication or Database Permission Errors

**Possible symptoms**
- Connection tests fail despite network reachability.
- The task cannot read source tables or write target data.
- CDC initialization or log access fails.

**Possible causes**
- Incorrect or expired credentials.
- Missing table-level or schema-level privileges.
- Engine-specific CDC prerequisites not met.
- Missing access to required transaction logs.

**Investigation**
1. Confirm the correct database user is configured.
2. Verify the user's required privileges for the selected migration method.
3. Check engine-specific AWS DMS prerequisites.
4. Review database-side logs where available.
5. Retest after an authorized correction.

## 4. Full-Load Errors

**Possible symptoms**
- Some tables fail to load.
- Table counts differ between source and target.
- Records are rejected or truncated.

**Possible causes**
- Incompatible data types or schema definitions.
- Insufficient target capacity.
- Unsupported or problematic data.
- Incorrect table mappings or filters.
- Target constraints or permissions preventing writes.

**Investigation**
1. Review table-level statistics and task logs.
2. Identify the affected tables and error messages.
3. Compare source and target schemas.
4. Inspect mappings, filters, data types, and target constraints.
5. Correct the root cause and repeat the appropriate load or validation step.

## 5. CDC Lag or Incomplete Change Replication

**Possible symptoms**
- The target falls behind the source.
- Replication latency increases.
- Recent changes do not appear at the target.

**Possible causes**
- High source change volume.
- Replication instance capacity limitations.
- Slow target writes or database contention.
- Source transaction-log retention or configuration problems.
- Network interruptions.

**Investigation**
1. Review task status and available CDC latency metrics.
2. Check source log availability and CDC configuration.
3. Assess replication instance capacity and target performance.
4. Review recent errors and transaction volume.
5. Confirm synchronization before cutover.

Do not switch applications to the target until the agreed consistency and cutover criteria are satisfied.

## 6. Data Mismatches

**Possible symptoms**
- Row counts differ.
- Selected records have different values.
- Application queries return unexpected results.

**Possible causes**
- Incomplete load or unapplied changes.
- Table mappings or filters.
- Type conversion, precision, or timezone differences.
- Duplicate or missing records.
- Source changes occurring during validation.

**Investigation**
1. Compare counts for the affected tables.
2. Select records using primary keys.
3. Compare relevant column values and transformations.
4. Review task errors and mapping rules.
5. Document the cause and repeat validation after correction.

Equal row counts alone do not prove data consistency.

## 7. Resource Creation or Quota Errors

**Possible symptoms**
- AWS refuses to create a replication resource.
- Resource creation fails despite valid configuration.

**Possible causes**
- Missing service permissions.
- Account or Region quotas.
- Unsupported resource configuration.
- Organization-level restrictions.
- Resource availability constraints.

**Investigation**
1. Record the exact error code and message.
2. Identify the required resource, Region, and requested configuration.
3. Review the account's permissions and applicable quotas.
4. Confirm current service support and resource availability.
5. Consult the authorized account administrator when required.

Before retrying, check whether the failed attempt left any resources that could incur charges.

## 8. Cost and Cleanup Issues

**Possible symptoms**
- Resources remain after a test.
- Charges continue after a migration exercise.

**Investigation**
1. Inventory the resources created for the exercise.
2. Identify which resources are still running or retained.
3. Review the current pricing and billing information.
4. Delete only resources that are no longer needed and are safe to remove.
5. Confirm cleanup and review the account for remaining billable resources.

Deleting a replication resource does not necessarily delete associated databases, storage, logs, or networking resources.

## General Troubleshooting Record

For each incident, record:

- **Symptom:** What happened?
- **Error:** Exact message with secrets removed.
- **Scope:** Which endpoint, task, table, or resource was affected?
- **Evidence:** Relevant logs, metrics, and configuration.
- **Root cause:** Confirmed cause, or clearly marked hypothesis.
- **Resolution:** Action taken or recommended.
- **Validation:** How recovery would be verified.

## Disclaimer

These are general diagnostic procedures. The correct resolution depends on the database engines, AWS DMS configuration, account permissions, and current service behavior. No AWS deployment or troubleshooting resolution is claimed as completed by this document.
