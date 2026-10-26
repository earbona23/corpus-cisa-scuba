# MS.AAD.7.2v1: Privileged users SHALL be provisioned with finer-grained roles instead of the Global Administrator role.
Product: Microsoft Entra ID · Baseline: aad · Group: 7. Highly Privileged User Access · Criticality: SHALL

## Policy
Privileged users SHALL be provisioned with finer-grained roles instead of the Global Administrator role.

- _Rationale:_ Many privileged administrative users do not need unfettered access to the tenant to perform their duties. By assigning them to roles based on least privilege, the risks associated with potential account compromises are reduced.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-5
- _MITRE ATT&CK TTP Mapping:_
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.003: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)
  - [T1651: Cloud Administration Command](https://attack.mitre.org/techniques/T1651/)
  - [T1136: Create Account](https://attack.mitre.org/techniques/T1136/)
    - [T1136.003: Cloud Account](https://attack.mitre.org/techniques/T1136/003/)

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
This policy is based on the ratio below:

`X = (Number of users assigned to the Global Administrator role) / (Number of users assigned to other highly privileged roles)`

1. Follow the instructions for policy MS.AAD.7.1v1, above, to get a count of users assigned to the Global Administrator role.

2. Follow the instructions for policy MS.AAD.7.1v1 above but get a count of users assigned to the other highly privileged roles (not Global Administrator). If a user is assigned to both Global Administrator and other roles, only count that user for the Global Administrator assignment.

3. Divide the value from step 2 from the value from step 1 to calculate X. If X is less than or equal to one, then the tenant is compliant with the policy.
