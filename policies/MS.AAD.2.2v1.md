# MS.AAD.2.2v1: A notification SHOULD be sent to the administrator when high-risk users are detected.
Product: Microsoft Entra ID · Baseline: aad · Group: 2. Risk-based Policies · Criticality: SHOULD

## Policy
A notification SHOULD be sent to the administrator when high-risk users are detected.

- _Rationale:_ Notification enables the administrator to monitor the event and remediate the risk. This helps organizations proactively respond to cyber intrusions as they occur.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-2(12)
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
1.  [Configure Microsoft Entra ID Protection to send a regularly monitored security mailbox email notification](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-notifications#configure-users-at-risk-detected-alerts) when user accounts are determined to be high-risk.
