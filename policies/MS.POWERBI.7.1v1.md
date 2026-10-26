# MS.POWERBI.7.1v1: Sensitivity labels SHOULD be enabled for Power BI and employed for sensitive data per enterprise data protection policies.
Product: Power BI · Baseline: powerbi · Group: 7. Power BI Sensitive Data · Criticality: SHOULD

## Policy
Sensitivity labels SHOULD be enabled for Power BI and employed for sensitive data per enterprise data protection policies.

- _Rationale:_ A document without sensitivity labels may be opened unknowingly, potentially exposing data to someone who is not supposed to have access. This policy will help organize and classify data, making it easier to keep data away from unauthorized users.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-21b, SC-7(10)(a)
- _MITRE ATT&CK TTP Mapping:_
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
  - [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)
    - [T1213.002: SharePoint](https://attack.mitre.org/techniques/T1213/002/)
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)

## Resources
- [Enable sensitivity labels in Power BI \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-enable-data-sensitivity-labels)

- [Data loss prevention policies for Power BI \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-dlp-policies-for-power-bi-overview)

- [Data Protection in Power BI \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-data-protection-overview)

- [Power BI Security Baseline v2.0 \| Microsoft benchmarks GitHub
  repo](https://github.com/MicrosoftDocs/SecurityBenchmarks/blob/master/Azure%20Offer%20Security%20Baselines/2.0/power-bi-security-baseline-v2.0.xlsx)

## License Requirements
- A Microsoft Purview Information Protection Premium P1 or Premium P2 license is required to apply or view
  Microsoft Information Protection sensitivity labels in Power BI. Azure Information Protection can be purchased either standalone or through one of the Microsoft licensing suites. See [Microsoft Purview Information Protection
  service description](https://azure.microsoft.com/services/information-protection/) for
  details.

- Microsoft Purview Information Protection sensitivity labels need to be migrated to
  the Microsoft Information Protection Unified Labeling platform to be
  used in Power BI.

- To apply labels to Power BI content and files, a user must
  have a Power BI Pro or Premium Per User (PPU) license, in addition to
  one of the previously mentioned Azure Information Protection licenses.

- Before enabling sensitivity labels on the agency's tenant, ensure sensitivity labels have been defined and published for relevant
  users and groups. See [Create and configure sensitivity labels and
  their
  policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)
  for details.

## Implementation
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **Information protection**.

4. Click on **Allow users to apply sensitivity labels for content** and set it to **Enabled**. Define who can apply and change sensitivity labels in Power BI assets.

**`TLP:CLEAR`**
