# MS.AAD.8.3v1: Guest invites SHOULD only be allowed to be sent to specific external domains that have been authorized by the agency for legitimate business purposes.
Product: Microsoft Entra ID · Baseline: aad · Group: 8. Guest User Access · Criticality: SHOULD

## Policy
Guest invites SHOULD only be allowed to be sent to specific external domains that have been authorized by the agency for legitimate business purposes.

- _Rationale:_ Limiting which domains can be invited to create guest accounts in the tenant helps reduce the risk of users from unauthorized external organizations gaining access.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.001: Default Accounts](https://attack.mitre.org/techniques/T1078/001/)

## Resources
- [Configure external collaboration settings for B2B in Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure)

- [Compare member and guest default permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#compare-member-and-guest-default-permissions)

## License Requirements
- N/A

## Implementation
1. Open the **Microsoft Entra admin center**.

2. Select **External Identities > External collaboration settings**.

3. Under **Collaboration restrictions**, select **Allow invitations
    only to the specified domains (most restrictive)**.

4. Select **Target domains** and enter the names of the external domains authorized by the agency for guest user access.

5. Click **Save**.
