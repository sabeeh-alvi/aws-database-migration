# AWS DMS IAM and Security Considerations

## Purpose

This document describes the security controls to review when planning a database migration with AWS Database Migration Service (AWS DMS).

**Status:** Security planning documentation. The policies and permissions described here have not been validated against a specific AWS account or migration.

## 1. Least-Privilege Access

Use only the permissions required for the migration.

- Separate permissions to administer AWS resources from permissions to access database data.
- Limit access to the intended AWS account, Region, and resources where supported.
- Avoid routinely using administrator-level policies.
- Review and remove temporary permissions when they are no longer needed.

## 2. AWS IAM Roles

AWS DMS may require service roles to perform operations on behalf of the migration service. The exact roles depend on the selected configuration and features.

Before implementation:

- Verify which service roles AWS DMS requires for the chosen migration setup.
- Confirm that the service can assume the required roles.
- Review the role trust policies and attached permissions.
- Avoid copying policies from unrelated projects without checking their purpose.
- Do not modify account-level security controls without authorization.

## 3. Database Credentials

Database endpoint credentials should be protected.

- Use dedicated migration database accounts where possible.
- Grant only the database privileges required for the selected migration method.
- Use an approved secrets-management method when supported by the design.
- Never commit passwords, access keys, tokens, or connection strings containing secrets to GitHub.
- Avoid placing credentials in screenshots, logs, or public documentation.
- Rotate or revoke temporary credentials after use when appropriate.

## 4. Source and Target Permissions

Source and target permissions depend on the database engine and whether the task uses full load, CDC, or both.

Verify engine-specific requirements for:

- Reading source tables and metadata.
- Accessing transaction logs or change records for CDC.
- Creating or modifying target tables and indexes, when required.
- Reading metadata needed by the migration.
- Performing any additional operations required by the selected task configuration.

Do not assume that a permission set for one database engine applies to another.

## 5. Network Security

- Prefer private network connectivity where feasible.
- Restrict security-group rules to the required sources, destinations, and ports.
- Confirm routing and DNS resolution rather than opening access broadly.
- Use encryption in transit where supported and appropriately configured.
- Avoid exposing database ports to `0.0.0.0/0` as a troubleshooting shortcut.

## 6. Data Protection

- Identify sensitive or regulated data before migration.
- Protect backups and exported data.
- Limit access to migration logs and validation results.
- Apply encryption at rest and in transit where appropriate.
- Follow applicable data-retention and deletion requirements.
- Use non-sensitive sample data for portfolio demonstrations.

## 7. Logging and Auditability

- Record migration configuration changes and execution outcomes.
- Review available AWS CloudTrail events and service logs.
- Avoid logging passwords, secrets, or unnecessary personal data.
- Document errors with sensitive values removed.
- Record who approved the migration and cutover when relevant.

## 8. Security Review Checklist

- [ ] Required IAM roles and trust policies verified.
- [ ] IAM permissions reviewed for least privilege.
- [ ] Source and target database permissions verified.
- [ ] Credentials stored securely and excluded from Git.
- [ ] Network access restricted to necessary endpoints.
- [ ] Encryption and data-retention requirements reviewed.
- [ ] Logging and audit requirements identified.
- [ ] Temporary access and cleanup plan documented.

## Disclaimer

Actual role names, policy requirements, and database privileges must be confirmed against the selected AWS DMS configuration and current AWS documentation. This document is a planning guide, not evidence that the controls have been implemented or tested.
