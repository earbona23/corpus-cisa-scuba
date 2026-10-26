# MS.AAD.8.2v1: Only users with the "Guest Inviter" role SHOULD be able to invite guest users.
Product: Microsoft Entra ID · Baseline: aad · Group: 8. Guest User Access · Criticality: SHOULD

## Policy
Only users with the "Guest Inviter" role SHOULD be able to invite guest users.

- _Rationale:_ By allowing only authorized individuals to invite external users to create guest accounts in the tenant, an agency can enforce a guest user account approval process, reducing the risk of unauthorized account creation.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.003: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)

## Resources
- [Configure external collaboration settings for B2B in Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure)

- [Compare member and guest default permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#compare-member-and-guest-default-permissions)

## License Requirements
- N/A

## Implementation
1. Open the **Microsoft Entra admin center**.

2. Select **External Identities > External collaboration settings**.

3. Under **Guest invite settings**, select **Only users assigned to specific admin roles can invite guest users**.

4. Click **Save**.
