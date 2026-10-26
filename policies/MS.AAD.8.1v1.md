# MS.AAD.8.1v1: Guest users SHOULD have limited or restricted access to Microsoft Entra ID directory objects.
Product: Microsoft Entra ID · Baseline: aad · Group: 8. Guest User Access · Criticality: SHOULD

## Policy
Guest users SHOULD have limited or restricted access to Microsoft Entra ID directory objects.

- _Rationale:_ Limiting the amount of object information available to guest users in the tenant reduces malicious reconnaissance exposure if a guest account is compromised or created by an adversary.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6
- _MITRE ATT&CK TTP Mapping:_
  - [T1087: Account Discovery](https://attack.mitre.org/techniques/T1087/)
    - [T1087.003: Email Account](https://attack.mitre.org/techniques/T1087/003/)
    - [T1087.004: Cloud Account](https://attack.mitre.org/techniques/T1087/004/)
  - [T1526: Cloud Service Discovery](https://attack.mitre.org/techniques/T1526/)

## Resources
- [Configure external collaboration settings for B2B in Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure)

- [Compare member and guest default permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#compare-member-and-guest-default-permissions)

## License Requirements
- N/A

## Implementation
1. Open the **Microsoft Entra admin center**.

2. Select **External Identities > External collaboration settings**.

3. Under **Guest user access**, select either **Guest users have limited access to properties and memberships of directory objects** or **Guest user access is restricted to properties and memberships of their own directory objects (most restrictive)**.

4. Click **Save**.
