# MS.AAD.7.8v1: User activation of the Global Administrator role SHALL trigger an alert.
Product: Microsoft Entra ID · Baseline: aad · Group: 7. Highly Privileged User Access · Criticality: SHALL

## Policy
User activation of the Global Administrator role SHALL trigger an alert.

- _Rationale:_ Activation of the Global Administrator role needs to be closely monitored for signs of compromise. Send activation alerts to enable the security monitoring team to detect compromise attempts.
- _Last modified:_ June 2023
- _Note:_ It is recommended to prioritize user activation of Global Administrator as one of the most important events for both monitoring and response.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(9)
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
1. In **Microsoft Entra admin center**, under **Identity Governance**, select **Privileged Identity Management (PIM)**. Select **Microsoft Entra roles**.

2. Click the **Global Administrator** role.

3. Click **Role settings** then click **Edit**.

4. Click the **Notifications** tab.

5. Under **Send notifications when eligible members activate this role** in the **Role activation alert**, select the **Additional recipients** textbox and enter the email address of the security monitoring mailbox configured to receive Global Administrator activation alerts.

6. Click **Update**.

7. If the Global Administrator role has any PIM groups actively assigned to it, then also apply the same configurations per the steps above to each PIM group's **Member** settings.
