# MS.EXO.3.1v1: DKIM SHOULD be enabled for all domains.
Product: Exchange Online · Baseline: exo · Group: 3. DomainKeys Identified Mail · Criticality: SHOULD

## Policy
DKIM SHOULD be enabled for all domains.

- _Rationale:_ An adversary may modify email headers, such as the `MAIL FROM` field, so the email appears to be a legitimate email sent by an
agency, facilitating phishing attacks. Enabling DKIM is another means for
recipients to detect spoofed emails and verify the integrity of email content.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1598: Phishing for Information](https://attack.mitre.org/techniques/T1598/)
  - [T1656: Impersonation](https://attack.mitre.org/techniques/T1656/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

## Resources
- [Binding Operational Directive 18-01 - Enhance Email and Web Security
  \| DHS](https://cyber.dhs.gov/bod/18-01/)

- [Trustworthy Email \| NIST 800-177 Rev.
  1](https://csrc.nist.gov/publications/detail/sp/800-177/rev-1/final)

- [Use DKIM to validate outbound email sent from your custom domain \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-configure?view=o365-worldwide)

- [Support for validation of DKIM signed messages \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-support-about?view=o365-worldwide)

- [What is EOP? \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/eop-faq?view=o365-worldwide#what-is-eop-)

## License Requirements
- N/A

## Implementation
1. To enable DKIM, follow the instructions listed on [Steps to Create,
enable and disable DKIM from Microsoft 365 Defender portal \| Microsoft
Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-configure?view=o365-worldwide#steps-to-create-enable-and-disable-dkim-from-microsoft-365-defender-portal).
