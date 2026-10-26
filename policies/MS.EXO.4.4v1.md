# MS.EXO.4.4v1: An agency point of contact SHOULD be included for aggregate and failure reports.
Product: Exchange Online · Baseline: exo · Group: 4. Domain-Based Message Authentication, Reporting, and Conformance (DMARC) · Criticality: SHOULD

## Policy
An agency point of contact SHOULD be included for aggregate and failure reports.

- _Rationale:_ Email spoofing attempts are not inherently visible to domain
owners. DMARC provides a mechanism to receive reports of spoofing attempts.
Including an agency point of contact gives the agency insight into attempts
to spoof their domains.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-4(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1562: Impair Defenses](https://attack.mitre.org/techniques/T1562/)

## Resources
- [Binding Operational Directive 18-01 - Enhance Email and Web Security
  \| DHS](https://cyber.dhs.gov/bod/18-01/)

- [Trustworthy Email \| NIST 800-177 Rev.
  1](https://csrc.nist.gov/publications/detail/sp/800-177/rev-1/final)

- [Domain-based Message Authentication, Reporting, and Conformance
  (DMARC) \| RFC 7489](https://datatracker.ietf.org/doc/html/rfc7489)

- [Best practices for implementing DMARC in Office 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide#best-practices-for-implementing-dmarc-in-microsoft-365)

- [How Office 365 handles outbound email that fails DMARC \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide#how-microsoft-365-handles-inbound-email-that-fails-dmarc)

## License Requirements
- N/A

## Implementation
See [MS.EXO.4.1v1 Instructions](#msexo41v1-instructions) for an overview of how to publish and check a DMARC record. Ensure the record published includes:
- A point of contact specific to your agency in the RUA field.
- <reports@dmarc.cyber.dhs.gov> as one of the emails in the RUA field.
- One or more agency-defined points of contact in the RUF field.
