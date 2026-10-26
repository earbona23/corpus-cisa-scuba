# MS.SECURITYSUITE.3.3v1: The action for the DLP policy SHOULD be set to block sharing sensitive information with everyone.
Product: securitysuite · Baseline: securitysuite · Group: 3. Data Loss Prevention · Criticality: SHOULD

## Policy
The action for the DLP policy SHOULD be set to block sharing sensitive information with everyone.

- _Rationale:_ Access to sensitive information should be prohibited unless
               explicitly allowed. Specific exemptions can be made based
               on agency policies and valid business justifications.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, SC-7(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)
  - [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)

## Resources
- [Plan for data loss prevention (DLP) \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp?view=o365-worldwide)

- [Data loss prevention in Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/security-and-compliance/data-loss-prevention/data-loss-prevention)

- [Personally identifiable information (PII) \|
  NIST](https://csrc.nist.gov/glossary/term/personally_identifiable_information#:~:text=NISTIR%208259,2%20under%20PII%20from%20EGovAct)

- [Sensitive information \|
  NIST](https://csrc.nist.gov/glossary/term/sensitive_information)

- [Get started with Endpoint data loss prevention - Microsoft Purview
  (compliance) \| Microsoft Learn](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started?view=o365-worldwide)

## License Requirements
- DLP for Teams requires an E5 or G5 license. See [Microsoft Purview Data Loss Prevention: Data Loss Prevention for Teams \| Microsoft
  Learn](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#microsoft-purview-data-loss-prevention-data-loss-prevention-dlp-for-teams)
  for more information. However, this requirement can also be met through a third-party solution. If a third-party solution is used, then an E5 or G5 license is not required for the respective policies.

- DLP for Endpoint, needed for MS.SECURITYSUITE.3.5v1, requires an E5 or G5 license. See [Get started with
  Endpoint data loss prevention - Microsoft Purview (compliance) \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started?view=o365-worldwide)
  for more information. However, this requirement can also be met through a compliant third-party solution. If a third-party solution is used, then an E5 or G5 license is not required for the respective policies.

## Implementation
See [MS.SECURITYSUITE.3.1v1 Instructions](#mssecuritysuite31v1-instructions) steps
   16-18 for details on configuring DLP policy to block sharing sensitive
   information with everyone.
