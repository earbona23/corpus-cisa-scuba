# MS.AAD.3.3v2: If Microsoft Authenticator is enabled, it SHALL be configured to show login context information.
Product: Microsoft Entra ID · Baseline: aad · Group: 3. Strong Authentication and a Secure Registration Process · Criticality: SHALL

## Policy
If Microsoft Authenticator is enabled, it SHALL be configured to show login context information.

- _Rationale:_ This policy helps protect the tenant when Microsoft Authenticator is used by showing user context information, reducing MFA phishing compromises.
- _Last modified:_ March 2025
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-2(1), IA-2(2), IA-5c, IA-5g, IA-2(8), IA-2(13)
- _MITRE ATT&CK TTP Mapping:_
  - [T1110: Brute Force](https://attack.mitre.org/techniques/T1110/)
    - [T1110.001: Password Guessing](https://attack.mitre.org/techniques/T1110/001/)
    - [T1110.002: Password Cracking](https://attack.mitre.org/techniques/T1110/002/)
    - [T1110.003: Password Spraying](https://attack.mitre.org/techniques/T1110/003/)

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
If Microsoft Authenticator is in use, configure Authenticator to display context information to users when they log in.

1. In **Microsoft Entra admin center**, click **Authentication methods > Microsoft Authenticator**.
2. Click the **Configure** tab.
3. For **Allow use of Microsoft Authenticator OTP**, select *No*.
4. Under **Show application name in push and passwordless notifications**, select **Status > Enabled** and **Target > Include > All users**.
5. Under **Show geographic location in push and passwordless notifications**, select **Status > Enabled** and **Target > Include > All users**.
6. Select **Save**.
