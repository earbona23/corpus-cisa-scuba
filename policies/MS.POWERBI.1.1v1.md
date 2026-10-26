# MS.POWERBI.1.1v1: The "Publish to Web" feature SHOULD be disabled unless the agency mission requires the capability.
Product: Power BI · Baseline: powerbi · Group: 1. Publish to Web · Criticality: SHOULD

## Policy
The "Publish to Web" feature SHOULD be disabled unless the agency mission requires the capability.

- _Rationale:_ A publicly accessible web URL can be accessed by everyone, including malicious actors. This policy limits information available on the public web that is not specifically allowed to be published.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7, SC-7(10)(a)
- _MITRE ATT&CK TTP Mapping:_
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)

## Resources
- [About Power BI Tenant settings \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/admin/service-admin-portal-about-tenant-settings)

- [Power BI Security Baseline v2.0 \| Microsoft benchmarks GitHub
  repo](https://github.com/MicrosoftDocs/SecurityBenchmarks/blob/master/Azure%20Offer%20Security%20Baselines/2.0/power-bi-security-baseline-v2.0.xlsx)

## License Requirements
- N/A

## Implementation
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Export and sharing settings**.

4. Click **Publish to web** and set it to **Disabled**.
