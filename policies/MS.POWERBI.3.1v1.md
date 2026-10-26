# MS.POWERBI.3.1v1: The "Invite external users to your organization" feature SHOULD be disabled unless agency mission requires the capability.
Product: Power BI · Baseline: powerbi · Group: 3. Power BI External Invitations · Criticality: SHOULD

## Policy
The "Invite external users to your organization" feature SHOULD be disabled unless agency mission requires the capability.

- _Rationale:_ Disabling this feature prevents internal users from inviting guest users, helping limit guest user access to potentially risky data/APIs. If an agency needs to allow guest access, the agency can limit the invitation feature to users in specific security groups to help limit risk.
- _Last modified:_ April 2026
> Note:
> If this feature is disabled, existing guest users in the tenant will continue to have access to Power BI items they already had access to and will continue to be listed in user picker experiences. After the feature is disabled, external users who are not already guest users cannot be added to the tenant through Power BI.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7, AC-6
- _MITRE ATT&CK TTP Mapping:_
  - [T1485: Data Destruction](https://attack.mitre.org/techniques/T1485/)
  - [T1565: Data Manipulation](https://attack.mitre.org/techniques/T1565/)
    - [T1565.001: Stored Data Manipulation](https://attack.mitre.org/techniques/T1565/001/)
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.001: Default Accounts](https://attack.mitre.org/techniques/T1078/001/)
  - [T1199: Trusted Relationship](https://attack.mitre.org/techniques/T1199/)

## Resources
- [About Power BI Tenant settings \| Microsoft
  Docs](https://learn.microsoft.com/en-us/power-bi/admin/service-admin-portal-about-tenant-settings)

- [Distribute Power BI content to external guest users with Microsoft Entra B2B \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-azure-ad-b2b)

- [Power BI Security Baseline v2.0 \| Microsoft benchmarks GitHub
  repo](https://github.com/MicrosoftDocs/SecurityBenchmarks/blob/master/Azure%20Offer%20Security%20Baselines/2.0/power-bi-security-baseline-v2.0.xlsx)

## License Requirements
- N/A

## Implementation
To disable completely:
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Export and sharing settings**.

4. Click on **Users can invite guest users to collaborate through item sharing and permissions** and set it to **Disabled**.

To enable with security groups:
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Export and sharing settings**.

4. Click on **Users can invite guest users to collaborate through item sharing and permissions** and set it to **Enabled**.

5. Select the security group(s) needed.
> Note:
> You may need to make a specific security group(s).
