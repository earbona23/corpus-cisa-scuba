# MS.SHAREPOINT.2.1v1: File and folder default sharing scope SHALL be set to "Specific people (only the people the user specifies)."
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 2. File and Folder Default Sharing Settings · Criticality: SHALL

## Policy
File and folder default sharing scope SHALL be set to "Specific people (only the people the user specifies)."

- _Rationale:_ By making the default sharing the most restrictive, administrators prevent accidentally sharing information too broadly.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6
- _MITRE ATT&CK TTP Mapping:_
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
  - [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)
    - [T1213.002: SharePoint](https://attack.mitre.org/techniques/T1213/002/)
  - [T1565: Data Manipulation](https://attack.mitre.org/techniques/T1565/)
    - [T1565.001: Stored Data Manipulation](https://attack.mitre.org/techniques/T1565/001/)

## Resources
- [File and folder links \| Microsoft
  Documents](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off#file-and-folder-links)

## License Requirements
- N/A

## Implementation
1.  Sign in to the **SharePoint admin center**.

2.  Select **Policies** \> **Sharing**

3.  Under **File and folder links**, set the default link type to **Specific people (only the people the user specifies)**.

4.  Select **Save**.
