# MS.EXO.4.2v1: The DMARC message rejection option SHALL be p=reject.
Product: Exchange Online · Baseline: exo · Group: 4. Domain-Based Message Authentication, Reporting, and Conformance (DMARC) · Criticality: SHALL

## Policy
The DMARC message rejection option SHALL be p=reject.

- _Rationale:_ Of the three policy options (i.e., none, quarantine, and reject),
reject provides the strongest protection. BOD 18-01 requires the "reject" level of protection
for FCEB agencies.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1598: Phishing for Information](https://attack.mitre.org/techniques/T1598/)
  - [T1656: Impersonation](https://attack.mitre.org/techniques/T1656/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

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
See [MS.EXO.4.1v1 Instructions](#msexo41v1-instructions) for an overview of how to publish and check a DMARC record. Ensure the record published includes `p=reject`.
