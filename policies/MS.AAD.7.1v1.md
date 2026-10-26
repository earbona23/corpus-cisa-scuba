# MS.AAD.7.1v1: A minimum of two users and a maximum of eight users SHALL be provisioned with the Global Administrator role.
Product: Microsoft Entra ID · Baseline: aad · Group: 7. Highly Privileged User Access · Criticality: SHALL

## Policy
A minimum of two users and a maximum of eight users SHALL be provisioned with the Global Administrator role.

- _Rationale:_ The Global Administrator role provides unfettered access to the tenant. Limiting the number of users with this access level makes tenant compromise more challenging. Microsoft recommends fewer than five users in the Global Administrator role. However, additional user accounts (up to eight) may be necessary to support emergency access and some operational scenarios.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.003: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)

## Resources
- [Limit number of Global Administrators to less than 5](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices#5-limit-the-number-of-global-administrators-to-less-than-5)

- [Implement Privilege Access Management](https://learn.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#implement-privilege-access-management)

- [Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user)

- [Privileged Identity Management (PIM) for Groups](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups)

- [Approve or deny requests for Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-approval-workflow)

- [Configure security alerts for Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts)

## License Requirements
- Policies [MS.AAD.7.4v1](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md#msaad74v1), [MS.AAD.7.5v1](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md#msaad75v1), [MS.AAD.7.6v1](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md#msaad76v1), [MS.AAD.7.7v1](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md#msaad77v1), [MS.AAD.7.8v1](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md#msaad78v1), and [MS.AAD.7.9v1](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md#msaad79v1) require a Microsoft Entra ID P2 license. However, a third-party Privileged Access Management (PAM) solution may also be used to satisfy the requirements. If a third-party solution is used, then a P2 license is not required for the respective policies.

## Implementation
When counting the number of users assigned to the Global Administrator role, count each user only once.

1. In the **Microsoft Entra admin center**, count the number of users assigned to the **Global Administrator** role. Count users that are assigned directly to the role and users assigned via group membership. If you have Microsoft Entra ID PIM, count both the **Eligible assignments** and **Active assignments**. If any of the groups assigned to Global Administrator are enrolled in PIM for Groups, also count the number of group members from the PIM for Groups portal **Eligible** assignments.

2. Validate that there are a total of two to eight users assigned to the Global Administrator role.
