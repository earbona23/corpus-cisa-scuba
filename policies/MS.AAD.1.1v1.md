# MS.AAD.1.1v1: Legacy authentication SHALL be blocked.
Product: Microsoft Entra ID · Baseline: aad · Group: 1. Legacy Authentication · Criticality: SHALL

## Policy
Legacy authentication SHALL be blocked.

- _Rationale:_ Allowing legacy authentication protocols can present a security risk because they do not support MFA. Blocking legacy protocols reduces the impact of user credential theft.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7
- _MITRE ATT&CK TTP Mapping:_
  - [T1110: Brute Force](https://attack.mitre.org/techniques/T1110/)
    - [T1110.001: Password Guessing](https://attack.mitre.org/techniques/T1110/001/)
    - [T1110.002: Password Cracking](https://attack.mitre.org/techniques/T1110/002/)
    - [T1110.003: Password Spraying](https://attack.mitre.org/techniques/T1110/003/)
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.004: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)

## Resources
- [Block legacy authentication with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-block-legacy)

- [Five steps to securing your identity infrastructure](https://learn.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity)

## License Requirements
- N/A

## Implementation
1. [Determine if an agency’s existing applications use legacy authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/block-legacy-authentication#identify-legacy-authentication-use) before blocking legacy authentication across the entire application base.

2. Create a Conditional Access policy to block legacy authentication, following the steps below:

<pre>
  Users > Include > <b>All users</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Conditions > Client apps > Configure > <b>Yes</b> > Legacy authentication clients > Select only <b>Exchange ActiveSync clients</b> and <b>Other clients</b>

  Access controls > Grant > <b>Block access</b>
</pre>
