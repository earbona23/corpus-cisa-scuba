# MS.EXO.6.2v1: Calendar details SHALL NOT be shared with all domains.
Product: Exchange Online · Baseline: exo · Group: 6. Calendar and Contact Sharing · Criticality: SHALL

## Policy
Calendar details SHALL NOT be shared with all domains.

- _Rationale:_ Calendar details may contain information that should not be shared by default with all domains. Disabling sharing with all domains closes an avenue for data exfiltration while still allowing
legitimate use as needed.
- _Last modified:_ June 2023
- _Note:_ Calendar details MAY be shared with specific domains.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, SC-7(10)(a)
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)

## Resources
- [Sharing in Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/sharing/sharing)

- [Organization relationships in Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/sharing/organization-relationships/organization-relationships)

- [Sharing policies in Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/sharing/sharing-policies/sharing-policies)

## License Requirements
- N/A

## Implementation
To restrict sharing calendar details with all domains:

1. Refer to step 5 in [MS.EXO.6.1v1 Instructions](#msexo61v1-instructions) to implement
this policy.
