# MS.SECURITYSUITE.6.2v1: Allowed domains SHALL NOT be added to inbound anti-spam protection policies.
Product: securitysuite · Baseline: securitysuite · Group: 6. Inbound Anti-Spam Protections · Criticality: SHALL

## Policy
Allowed domains SHALL NOT be added to inbound anti-spam protection policies.

- _Rationale:_ Legitimate emails may be incorrectly filtered
by spam protections. Adding allowed senders is an acceptable method of
combating these false positives. However, allowing an entire domain, especially
a common domain like office.com, could allow a large number of
potentially unknown users to bypass spam protections.
- _Last modified:_ March 2026
- _Note:_ Allowed senders MAY be added.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

## Resources
- [Configure anti-spam policies in EOP \| Microsoft Learn](https://learn.microsoft.com/en-us/defender-office-365/anti-spam-policies-configure?view=o365-worldwide)

## License Requirements
- N/A

## Implementation
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

For users not added to the standard or strict preset policies, see [MS.SECURITYSUITE.6.1v1 Instructions](#mssecuritysuite61v1-instructions).
