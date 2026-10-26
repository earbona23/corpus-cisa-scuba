# MS.AAD.3.1v1: Phishing-resistant MFA SHALL be enforced for all users.
Product: Microsoft Entra ID · Baseline: aad · Group: 3. Strong Authentication and a Secure Registration Process · Criticality: SHALL

## Policy
Phishing-resistant MFA SHALL be enforced for all users.

The phishing-resistant methods of **Microsoft Entra ID certificate-based authentication (CBA)**, **FIDO2 Security Key**, **Windows Hello for Business**, and **device-bound passkeys** (in the authenticator application of choice) are the recommended authentication options since they offer forms of MFA with the fewest weaknesses. For federal agencies, Microsoft Entra ID CBA supports federal PIV card authentication directly to Microsoft Entra ID.

If on-premises PIV authentication and federation to Microsoft Entra ID is used, [enforce PIV logon via the Microsoft Active Directory group policy](https://www.idmanagement.gov/implement/scl-windows/).

- _Rationale:_ Weaker forms of MFA do not protect against sophisticated phishing attacks. By enforcing phishing-resistant MFA methods, those risks are minimized.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-2(1), IA-2(2), IA-5c, IA-5g, IA-2(8)
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
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
1. Create a conditional access policy enforcing phishing-resistant MFA for all users. Configure the following policy settings in the new conditional access policy, per the values below:

<pre>
  Users > Include > <b>All users</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Access controls > Grant > Grant Access > Require authentication strength > <b>Phishing-resistant MFA</b>
</pre>
