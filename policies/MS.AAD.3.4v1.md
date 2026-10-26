# MS.AAD.3.4v1: The "Authentication methods manage migration" feature SHALL be set to "Migration complete."
Product: Microsoft Entra ID · Baseline: aad · Group: 3. Strong Authentication and a Secure Registration Process · Criticality: SHALL

## Policy
The "Authentication methods manage migration" feature SHALL be set to "Migration complete."

- _Rationale:_ To disable the legacy authentication methods screen for the tenant, configure the "Manage migration" feature to "Migration complete." The MFA and Self-Service Password Reset (SSPR) authentication methods are both managed from a central administrator page, thereby reducing administrative complexity and potential security misconfigurations.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7
- _MITRE ATT&CK TTP Mapping:_
  - None

## Resources
- [What authentication and verification methods are available in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods)

- [Use additional context in Authenticator notifications - Authentication methods policy](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-additional-context#enable-additional-context-in-the-portal)

- [M-22-09 Federal Zero Trust Architecture Strategy](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf)

- [Configure Microsoft Entra hybrid join](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join)

- [Microsoft Entra joined devices](https://learn.microsoft.com/en-us/entra/identity/devices/concept-directory-join)

- [Set up automatic enrollment for Windows devices (for Intune)](https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enroll)

- [Enable passkeys (FIDO2) for your organization](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-enable-passkey-fido2)

- [Storm-2372 conducts device code phishing campaign](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/)

- [Microsoft 365 Device Code Phishing Cyber Attack – Demonstration, Analysis and Mitigation](https://github.com/cisagov/ScubaGear/issues/1599)

- [Block device code flow](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies#block-device-code-flow)

## License Requirements
- Policies related to managed devices require Microsoft Intune.

## Implementation
1. Follow the process for [How to migrate MFA and SSPR policy settings to the Authentication methods policy for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage).
2. Once ready to finish the migration, [set the **Manage migration** option to **Migration complete**](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage#finish-the-migration).
