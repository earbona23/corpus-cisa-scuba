# MS.SECURITYSUITE.3.4v1: Notifications to inform users and help educate them on the proper use of sensitive information SHOULD be enabled in the DLP policy.
Product: securitysuite · Baseline: securitysuite · Group: 3. Data Loss Prevention · Criticality: SHOULD

## Policy
Notifications to inform users and help educate them on the proper use of sensitive information SHOULD be enabled in the DLP policy.

- _Rationale:_ Some users may not be aware of agency policies regarding
               proper use of sensitive information. Enabling
               notifications provides positive feedback to users when
               accessing sensitive information.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AT-2b
- _MITRE ATT&CK TTP Mapping:_
  - None

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
   19-20 for details on configuring DLP policy to notify users when accessing
   sensitive information.
