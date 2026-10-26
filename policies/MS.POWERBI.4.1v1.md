# MS.POWERBI.4.1v1: Service principals with access to APIs SHOULD be restricted to specific security groups.
Product: Power BI · Baseline: powerbi · Group: 4. Power BI Service Principals · Criticality: SHOULD

## Policy
Service principals with access to APIs SHOULD be restricted to specific security groups.

- _Rationale:_ Unwanted access to APIs is possible if service principals are unrestricted. Allowing service principals through security groups (where necessary) mitigates this risk.
- _Last modified:_ April 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-4, AC-6(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1059: Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
    - [T1059.009: Cloud API](https://attack.mitre.org/techniques/T1059/009/)

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
Organizations with service principals needing to access Power BI APIs can configure the settings per the instructions below.
If there is not a need to grant service principals access, configure the setting to **Disabled**.

1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Developer settings**.

4. Click on **Service principals can call Fabric public APIs**.

5. If there are not service principals needing access to Power BI APIs, configure the setting to **Disabled**. Otherwise, go to step 6.

6. If there are service principals needing access to Power BI APIs, configure the setting to **Enabled**.

7. Select the specific security groups that contain the service principals authorized to call the APIs.
