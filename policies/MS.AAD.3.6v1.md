# MS.AAD.3.6v1: Phishing-resistant MFA SHALL be required for highly privileged roles.
Product: Microsoft Entra ID · Baseline: aad · Group: 3. Strong Authentication and a Secure Registration Process · Criticality: SHALL

## Policy
Phishing-resistant MFA SHALL be required for highly privileged roles.

- _Rationale:_ This is a backup security policy to help protect privileged access to the tenant if the conditional access policy, which requires MFA for all users, is disabled or misconfigured.
- _Last modified:_ June 2023
- _Note:_ Refer to the "Highly Privileged Roles" section at the top of this baseline for a reference list of roles considered highly privileged.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-2(1), IA-5c, IA-5g, IA-2(8)
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
    - [T1566.002: Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.004: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)

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
1. Create a conditional access policy enforcing phishing-resistant MFA for highly privileged roles. Configure the following policy settings in the new conditional access policy, per the values below:

<pre>
  Users > Include > Select users and groups > Directory roles > <b>Select each of the roles listed in the "Highly Privileged Roles" section at the top of this document</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Access controls > Grant > Grant Access > Require authentication strength > <b>Phishing-resistant MFA</b>
</pre>
