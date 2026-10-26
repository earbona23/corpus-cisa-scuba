# MS.SECURITYSUITE.7.3v1: User click tracking SHOULD be enabled.
Product: securitysuite · Baseline: securitysuite · Group: 7. Link Protection · Criticality: SHOULD

## Policy
User click tracking SHOULD be enabled.

- _Rationale:_ Users may click on malicious links in emails, leading to compromise or unauthorized data disclosure. Enabling user click tracking lets agencies know after the fact if a malicious link may have been visited, helping to tailor a potential incident response.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-3, AU-12c
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.002: Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)

## Resources
- [Set up Safe Links policies in Microsoft Defender for Office 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/defender-office-365/safe-links-policies-configure)

## License Requirements
Safe links require Defender for Office 365 Plan 1 or 2. These are included with
E5 and G5 and are available as add-ons for E3 and G3.

## Implementation
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

For users not added to the standard or strict preset policies, see [MS.SECURITYSUITE.7.1v1 Instructions](#mssecuritysuite71v1-instructions).
