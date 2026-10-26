# MS.EXO.13.1v1: Mailbox auditing SHALL be enabled.
Product: Exchange Online · Baseline: exo · Group: 13. Mailbox Auditing · Criticality: SHALL

## Policy
Mailbox auditing SHALL be enabled.

- _Rationale:_ Exchange Online user accounts can be compromised or misused. Enabling mailbox auditing provides a valuable source of information to detect and respond to mailbox misuse.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AU-12c
- _MITRE ATT&CK TTP Mapping:_
  - [T1070: Indicator Removal](https://attack.mitre.org/techniques/T1070/)
    - [T1070.008: Clear Mailbox Data](https://attack.mitre.org/techniques/T1070/008/)
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.002: Additional Email Delegate Permissions](https://attack.mitre.org/techniques/T1098/002/)
  - [T1562: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
    - [T1562.008: Disable or Modify Cloud Logs](https://attack.mitre.org/techniques/T1562/008/)
  - [T1586: Compromise Accounts](https://attack.mitre.org/techniques/T1586/)
    - [T1586.002: Email Accounts](https://attack.mitre.org/techniques/T1586/002/)
  - [T1564: Hide Artifacts](https://attack.mitre.org/techniques/T1564/)
  - [T1564.008: Email Hiding Rules](https://attack.mitre.org/techniques/T1564/008/)

## Resources
- [Manage mailbox auditing in Office 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/compliance/audit-mailboxes?view=o365-worldwide)

- [Supported mailbox types \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/compliance/audit-mailboxes?view=o365-worldwide&viewFallbackFrom=o365-worldwide%22%20%5Cl%20%22supported-mailbox-types)

- [Microsoft Purview Compliance Manager - Microsoft 365 Compliance \|Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/compliance/compliance-manager?view=o365-worldwide)

## License Requirements
- N/A

## Implementation
Mailbox auditing can be managed from the Exchange Online PowerShell.
Follow the instructions listed on [Manage mailbox auditing in Office
365](https://learn.microsoft.com/en-us/microsoft-365/compliance/audit-mailboxes?view=o365-worldwide).

To check the current mailbox auditing status for your organization via PowerShell:

1.  Connect to the Exchange Online PowerShell.

2.  Run the following command:

    `Get-OrganizationConfig | Format-List AuditDisabled`

3.  An `AuditDisabled : False` result indicates mailbox auditing is enabled.

To enable mailbox auditing by default for your organization via PowerShell:

1.  Connect to the Exchange Online PowerShell.

2.  Run the following command:

    `Set-OrganizationConfig –AuditDisabled $false`

**`TLP:CLEAR`**
