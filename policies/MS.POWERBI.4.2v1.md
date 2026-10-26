# MS.POWERBI.4.2v1: Service principals' ability to create and use profiles SHOULD be restricted to specific security groups.
Product: Power BI · Baseline: powerbi · Group: 4. Power BI Service Principals · Criticality: SHOULD

## Policy
Service principals' ability to create and use profiles SHOULD be restricted to specific security groups.

- _Rationale:_ When unrestricted service principals create or use profiles, there is risk of an unauthorized user using a profile with more permissions than should be allowed. Restricting service principals through security groups can mitigate this risk.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-4, AC-6(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.003: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)

## Resources
- [Automate Premium workspace and dataset tasks with service principal
  \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-service-principal)

- [Embed Power BI content with service principal and an application
  secret \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal)

- [Embed Power BI content with service principal and a certificate \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal-certificate)

- [Enable service principal authentication for read-only admin APIs \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/enterprise/read-only-apis-service-principal-authentication)

- [Microsoft Power BI Embedded Developer Code Samples \| Microsoft
  GitHub](https://github.com/microsoft/PowerBI-Developer-Samples/blob/master/Python/Encrypt%20credentials/README.md)

- [Azure security baseline for Power BI \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/power-bi-security-baseline)

## License Requirements
- N/A

## Implementation
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Developer settings**.

4. Click on **Allow service principals to create and use profiles**.

5. If there are not service principals needing to create and use profiles, then configure the setting to **Disabled**. Otherwise, go to step 6.

6. If there are service principals needing to create and use profiles, then configure the setting to **Enabled**.

7. Select the specific security groups that contain the service principals authorized to create and use profiles.
