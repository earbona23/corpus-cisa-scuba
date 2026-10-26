# MS.SHAREPOINT.1.2v1: External sharing for OneDrive SHALL be limited to "Existing guests" or "Only people in your organization."
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 1. External Sharing · Criticality: SHALL

## Policy
External sharing for OneDrive SHALL be limited to "Existing guests" or "Only people in your organization."

- _Rationale:_ Sharing files outside of the organization via OneDrive increases the risk of unauthorized access. By limiting external sharing, administrators decrease the risk of unauthorized access to information.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-2, AC-3, IA-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
  - [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)
    - [T1213.002: SharePoint](https://attack.mitre.org/techniques/T1213/002/)
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)

## Resources
- [Overview of external sharing in SharePoint and OneDrive in Microsoft 365 \| Microsoft Documents](https://learn.microsoft.com/en-us/sharepoint/external-sharing-overview)

- [Manage sharing settings for SharePoint and OneDrive in Microsoft 365 \| Microsoft Documents](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)

## License Requirements
- N/A

## Implementation
1.  Sign in to the **SharePoint admin center**.

2.  Select **Policies** \> **Sharing**.

3.  Adjust external sharing slider for OneDrive to **Existing Guests** or **Only people in your organization**.

4. Select **Save**.
