# MS.POWERBI.5.1v1: ResourceKey-based authentication SHOULD be blocked unless a specific use case (e.g., streaming and/or "push" datasets) merits its use.
Product: Power BI · Baseline: powerbi · Group: 5. Power BI Resource Key Authentication · Criticality: SHOULD

## Policy
ResourceKey-based authentication SHOULD be blocked unless a specific use case (e.g., streaming and/or "push" datasets) merits its use.

- _Rationale:_ If resource keys are allowed, a user could move data without a Microsoft Entra ID OAuth bearer token, potentially storing malicious or junk data. Disabling resource keys reduces the risk that an unauthorized individual will make changes.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7, IA-5g
- _MITRE ATT&CK TTP Mapping:_
  - [T1134: Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)
    - [T1134.001: Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001/)
    - [T1134.003: Make and Impersonate Token](https://attack.mitre.org/techniques/T1134/003/)

## Resources
- [Power BI Tenant settings \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/admin/service-admin-portal-about-tenant-settings)

- [Real-time streaming in Power BI \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/service-real-time-streaming)

## License Requirements
- N/A

## Implementation
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Developer settings**.

4. Click on **Block ResourceKey authentication** and set it to **Enabled**.
