# MS.POWERBI.2.1v1: Guest user access to the Power BI tenant SHOULD be disabled unless the agency mission requires the capability.
Product: Power BI · Baseline: powerbi · Group: 2. Power BI Guest Access · Criticality: SHOULD

## Policy
Guest user access to the Power BI tenant SHOULD be disabled unless the agency mission requires the capability.

- _Rationale:_ Disabling external access to Power BI helps keep guest users from accessing potentially risky data and application programming interfaces (APIs). If an agency needs to allow guest access, this can be limited to users in specific security groups to curb risk.
- _Last modified:_ April 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7, AC-6
- _MITRE ATT&CK TTP Mapping:_
  - [T1485: Data Destruction](https://attack.mitre.org/techniques/T1485/)
  - [T1565: Data Manipulation](https://attack.mitre.org/techniques/T1565/)
    - [T1565.001: Stored Data Manipulation](https://attack.mitre.org/techniques/T1565/001/)
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.001: Default Accounts](https://attack.mitre.org/techniques/T1078/001/)

## Resources
- [About Power BI Tenant settings \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/admin/service-admin-portal-about-tenant-settings)

- [Power BI Security Baseline v2.0 \| Microsoft benchmarks GitHub
  repo](https://github.com/MicrosoftDocs/SecurityBenchmarks/blob/master/Azure%20Offer%20Security%20Baselines/2.0/power-bi-security-baseline-v2.0.xlsx)

## License Requirements
- N/A

## Implementation
To disable completely:
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Export and sharing settings**.

4. For **commercial** tenants, click on **Guest users can access Microsoft Fabric** and set it to **Disabled**.

5. For **GCC, GCC High and DoD** tenants, click on **Allow Azure Active Directory guest users to access Power BI** and set it to **Disabled**.

To enable with security group(s):
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Export and sharing settings**.

4. For **commercial** tenants, click on **Guest users can access Microsoft Fabric** and set it to **Enabled**.

5. For **GCC, GCC High and DoD** tenants, click on **Allow Azure Active Directory guest users to access Power BI** and set it to **Enabled**.

6. Select the security group(s) you want to have access to the Power BI tenant.
> Note:
> You may need to make a specific security group(s).
