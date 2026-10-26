# MS.SECURITYSUITE.5.1v1: Unified audit logging SHALL be enabled.
Product: securitysuite · Baseline: securitysuite · Group: 5. Audit Logging · Criticality: SHALL

## Policy
Unified audit logging SHALL be enabled.

- _Rationale:_ Responding to incidents without detailed information about activities that took place slows response actions. Enabling unified audit logging helps ensure agencies have visibility into user actions.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AU-12
- _MITRE ATT&CK TTP Mapping:_
  - [T1562: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
    - [T1562.008: Disable or Modify Cloud Logs](https://attack.mitre.org/techniques/T1562/008/)

## Resources
- [OMB M-26-14, Ensuring Effective and Efficient Agency Logging and Network Visibility to
Defend Against Evolving Cyber Threats \| Office of Management and
  Budget](https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf)

- [Turn auditing on or off \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable?view=o365-worldwide)

- [Create an audit log retention policy \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies?view=o365-worldwide#create-an-audit-log-retention-policy)

- [Search the audit log in the compliance center \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/audit-log-search?view=o365-worldwide)

- [Audit log activities \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/audit-log-activities)

- [Expanding cloud logging to give customers deeper security visibility \|
  Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2023/07/19/expanding-cloud-logging-to-give-customers-deeper-security-visibility/)

- [Export, configure, and view audit log records | Microsoft Learn](https://learn.microsoft.com/en-us/purview/audit-log-export-records)

- [Untitled Goose Tool Fact Sheet | CISA.](https://www.cisa.gov/resources-tools/resources/untitled-goose-tool-fact-sheet)

- [Manage audit log retention policies | Microsoft Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies?tabs=microsoft-purview-portal#before-you-create-an-audit-log-retention-policy)

## License Requirements
- The creation of a custom audit log retention policy requires E5/G5 licenses or E3/G3 licenses with add-on compliance licenses.
- To maintain logs in M365 for longer than 180 days, the user generating the logs must have an Office 365 E5 or Microsoft 365 E5 license or a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) or E5 eDiscovery and Audit add-on license.

## Implementation
To enable auditing via the **Microsoft Purview portal**:

1. Sign in to the **Microsoft Purview portal**.

2. Under **Solutions**, select **Audit**.

3. If auditing is not enabled, a banner is displayed to notify the
administrator to start recording user and administrator activity.

4. Click the **Start recording user and admin activity**.
