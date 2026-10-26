# MS.AAD.7.4v1: Permanent active role assignments SHALL NOT be allowed for highly privileged roles.
Product: Microsoft Entra ID · Baseline: aad · Group: 7. Highly Privileged User Access · Criticality: SHALL

## Policy
Permanent active role assignments SHALL NOT be allowed for highly privileged roles.

- _Rationale:_ Instead of giving users permanent assignments to privileged roles, provisioning access when the roles are needed (i.e. "just in time") lessens exposure if those accounts become compromised. In Microsoft Entra ID PIM or an alternative PAM system, "just in time" access can be provisioned by assigning users to roles as eligible instead of perpetually active.
- _Last modified:_ June 2023
- _Note:_ Exceptions to this policy include
  - Emergency access accounts that need perpetual access to the tenant in the rare event of system degradation or other scenarios
  - Some types of service accounts that require a user account with privileged roles (since these accounts are used by software programs, they cannot perform role activation)
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-2
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
1. In **Microsoft Entra admin center**, select **Roles and admins**. Perform the steps below for each highly privileged role. We reference the Global Administrator role as an example.

2. Select the **Global Administrator** role.

3. Under **Manage**, select **Assignments** and click the **Active assignments** tab.

4. Verify there are no users or groups with a value of **Permanent** in the **End time** column. If there are any, recreate those assignments to have an expiration date using Microsoft Entra ID PIM or an alternative PAM system. If a group is identified and it is enrolled in PIM for Groups, see the exception cases below for details.

Exception cases:
- Emergency access accounts that require perpetual active assignment
- Service accounts that require perpetual active assignment
- If using PIM for Groups, a group that is enrolled in PIM is allowed to have a perpetual active assignment to a role because activation is handled by PIM for Groups.
