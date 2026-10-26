# MS.AAD.2.1v1: Users detected as high risk SHALL be blocked.
Product: Microsoft Entra ID · Baseline: aad · Group: 2. Risk-based Policies · Criticality: SHALL

## Policy
Users detected as high risk SHALL be blocked.

- _Rationale:_ Blocking high-risk users may prevent compromised accounts from accessing the tenant.
- _Last modified:_ June 2023
- _Note:_ Users identified as high-risk by Microsoft Entra ID Identity Protection can be blocked from accessing the system via a Microsoft Entra ID Conditional Access policy. A high-risk user will be blocked until an administrator remediates their account.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-2(12), AC-2(13)
- _MITRE ATT&CK TTP Mapping:_
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.004: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)

## Resources
- [What are risk detections?](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)

- [Simulating risk detections in Identity Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk)

- [Self-remediation experience with Microsoft Entra ID Protection and Conditional Access](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-user-experience)

## License Requirements
- Requires a Microsoft Entra ID P2 license

## Implementation
1.  Create a conditional access policy blocking users categorized as high-risk by the Identity Protection service. Configure the following policy settings in the new conditional access policy per the values below:

<pre>
  Users > Include > <b>All users</b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Conditions > User risk > <b>High</b>

  Access controls > Grant > <b>Block access</b>
</pre>
