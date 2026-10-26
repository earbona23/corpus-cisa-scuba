# MS.AAD.3.2v2: MFA SHALL be enforced for all users.
Product: Microsoft Entra ID · Baseline: aad · Group: 3. Strong Authentication and a Secure Registration Process · Criticality: SHALL

## Policy
MFA SHALL be enforced for all users.

- _Rationale:_ This policy helps protect the tenant for guest users or any other group with multifactor authentication where phishing-resistant MFA is not enforceable due to technical limitations. It protects against the weaknesses inherent in single factor authentication.
- _Last modified:_ February 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-2(1), IA-2(2)
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
There are a few different options to implement a conditional access policy that enforces MFA. Each option is described below, followed by our recommendation and the respective instructions for each option.

- **Option 1** - Create a custom authentication strength that includes the specific multifactor authentication methods supported by your organization and then create a policy that enforces your custom authentication strength.
- **Option 2** - Create a policy that enforces multifactor authentication (no specific method).
- **Option 3** - Create a policy that enforces the built-in authentication strength named "multifactor authentication" (no specific method).

We recommend using a custom authentication strength to enforce the specific methods that offer the highest security. We recommend that you require the "passwordless" authentication strength Microsoft Authenticator (phone sign-in) in lieu of alternative MFA methods, since it removes passwords from the sign-in flow, reducing the exposure to credential compromise.

**Option 1**. [Follow the instructions at this link](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-advanced-options#create-a-custom-authentication-strength) to create a custom authentication strength. Create a conditional access policy that enforces your custom authentication. Configure the following policy settings in the new conditional access policy, per the values below:

<pre>
  Users > Include > <b>All users</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Access controls > Grant > Grant Access > <b>Require authentication strength</b> > <b>YOUR_CUSTOM_AUTHENTICATION_STRENGTH</b>
</pre>

**Option 2**. Create a conditional access policy that enforces MFA but does not dictate a specific MFA method. Configure the following policy settings in the new conditional access policy, per the values below:

<pre>
  Users > Include > <b>All users</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Access controls > Grant > Grant Access > <b>Require multifactor authentication</b>
</pre>

**Option 3**. Create a conditional access policy that enforces the built-in authentication strength named "Multifactor authentication" and does not dictate a specific MFA method. Configure the following policy settings in the new conditional access policy, per the values below:

<pre>
  Users > Include > <b>All users</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Access controls > Grant > Grant Access > <b>Require authentication strength</b> > <b>Multifactor authentication</b>
</pre>
