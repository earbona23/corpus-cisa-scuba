# MS.AAD.3.5v2: The authentication methods of short message service (SMS), voice call, and email one-time passcode (OTP) SHALL be disabled.
Product: Microsoft Entra ID · Baseline: aad · Group: 3. Strong Authentication and a Secure Registration Process · Criticality: SHALL

## Policy
The authentication methods of short message service (SMS), voice call, and email one-time passcode (OTP) SHALL be disabled.

- _Rationale:_ SMS, voice call, and email OTP are the weakest authenticators. This policy forces users to use stronger MFA methods.
- _Last modified:_ February 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7b, IA-5c
- _MITRE ATT&CK TTP Mapping:_
  - [T1621: Multifactor Authentication Request Generation](https://attack.mitre.org/techniques/T1621/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.002: Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)

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
1. In **Microsoft Entra admin center**, click **Authentication methods**
2. Click on the **SMS**, **voice call**, and **email OTP** authentication methods and disable each of them. Their statuses should be **Enabled > No** on the **Authentication methods > Policies** page.
