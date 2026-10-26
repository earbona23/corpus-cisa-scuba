# MS.SECURITYSUITE.1.2v1: Email scanning SHALL be capable of reviewing emails after delivery.
Product: securitysuite · Baseline: securitysuite · Group: 1. Malware Protection · Criticality: SHALL

## Policy
Email scanning SHALL be capable of reviewing emails after delivery.

- _Rationale:_ As known malware signatures are updated, it is possible for an email to be retroactively identified as containing malware after delivery. By scanning emails, the number of malware-infected in users' mailboxes can be reduced.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)

## Resources
- [Anti-malware protection for cloud mailboxes \| Microsoft Learn](https://learn.microsoft.com/en-us/defender-office-365/anti-malware-protection-about)
- [Set up Safe Attachments policies in Microsoft Defender for Office 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-attachments-policies-configure?view=o365-worldwide)

## License Requirements
Safe attachments require Defender for Office 365 Plan 1 or 2. These are included with
  E5 and G5 and are available as add-ons for E3 and G3.

## Implementation
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

For users not added to the standard or strict preset policies, see [MS.SECURITYSUITE.1.2v1 Instructions](#mssecuritysuite12v1-instructions).
