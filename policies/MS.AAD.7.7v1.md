# MS.AAD.7.7v1: Eligible and active highly privileged role assignments SHALL trigger an alert.
Product: Microsoft Entra ID · Baseline: aad · Group: 7. Highly Privileged User Access · Criticality: SHALL

## Policy
Eligible and active highly privileged role assignments SHALL trigger an alert.

- _Rationale:_ Closely monitor highest privileged role assignments for signs of compromise. Send assignment alerts to enable the security monitoring team to detect compromise attempts.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-2(1)
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
1.  In **Microsoft Entra admin center**, under **Identity Governance**, select **Privileged Identity Management (PIM)**, and then select **Microsoft Entra roles**.

2. Under **Manage**, select **Roles**. Perform the steps below for each highly privileged role. We reference the Global Administrator role as an example:

  1. Click the **Global Administrator** role.
  2. Click **Role settings** and then click **Edit**.
  3. Click the **Notifications** tab.
  4. Under **Send notifications when members are assigned as eligible to this role**, in the **Role assignment alert > Additional recipients** textbox, enter the email address of the security monitoring mailbox configured to receive privileged role assignment alerts.
  5. Under **Send notifications when members are assigned as active to this role**, in the **Role assignment alert > Additional recipients** textbox, enter the email address of the security monitoring mailbox configured to receive privileged role assignment alerts.
  6. Click **Update**.

3. For each of the highly privileged roles, if a user has any PIM groups actively assigned to them, apply the same configurations as steps 2-8 above to each PIM group's **Member** settings.
