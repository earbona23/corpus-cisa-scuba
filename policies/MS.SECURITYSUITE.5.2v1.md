# MS.SECURITYSUITE.5.2v1: Audit logs SHALL be retained and searchable for a minimum of 3 months and retrievable for a minimum of 12 months.
Product: securitysuite · Baseline: securitysuite · Group: 5. Audit Logging · Criticality: SHALL

## Policy
Audit logs SHALL be retained and searchable for a minimum of 3 months and retrievable for a minimum of 12 months.

- _Rationale:_ Audit logs may not be available when needed if they are not retained for a sufficient time. Increased log retention time gives an agency the necessary visibility to investigate incidents that occurred in the past.
- _Last modified:_ September 2026
- _Note:_ Retaining logs in M365 for longer than 180 days requires meeting the license requirement described below. Without the necessary licenses, data is retained according to the highest priority retention policy. This retention might be either the default retention policy for the user's license or the highest priority policy that matches the user and its record type.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AU-11
- _MITRE ATT&CK TTP Mapping:_
  - [T1070: Indicator Removal](https://attack.mitre.org/techniques/T1070/)

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
One option for controlling log retention times in M365 is to create one or more custom audit
retention policies. For more details, see [Create an audit log retention policy](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies?view=o365-worldwide#create-an-audit-log-retention-policy)
instructions.

As noted in the [License Requirements](https://github.com/cisagov/ScubaGear/baselines/securitysuite.md#license-requirements-1)
section above, the creation of a custom audit log retention policy and its retention in the M365
environment requires E5/G5 licenses or E3/G3 licenses with add-on compliance licenses. However, no
additional license is required to export logs. To export audit logs, follow
[Export, configure, and view audit log records | Microsoft Learn](https://learn.microsoft.com/en-us/purview/audit-log-export-records)
and/or [Untitled Goose Tool Fact Sheet | CISA.](https://www.cisa.gov/resources-tools/resources/untitled-goose-tool-fact-sheet).
