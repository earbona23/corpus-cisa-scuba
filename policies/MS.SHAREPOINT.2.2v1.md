# MS.SHAREPOINT.2.2v1: File and folder default sharing permissions SHALL be set to view only.
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 2. File and Folder Default Sharing Settings · Criticality: SHALL

## Policy
File and folder default sharing permissions SHALL be set to view only.

- _Rationale:_ Edit access to files and folders could allow a user to make unauthorized changes. By restricting default permissions to view only, administrators prevent unintended or malicious modification.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6
- _MITRE ATT&CK TTP Mapping:_
  - [T1080: Taint Shared Content](https://attack.mitre.org/techniques/T1080/)
  - [T1565: Data Manipulation](https://attack.mitre.org/techniques/T1565/)
    - [T1565.001: Stored Data Manipulation](https://attack.mitre.org/techniques/T1565/001/)

## Resources
- [File and folder links \| Microsoft
  Documents](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off#file-and-folder-links)

## License Requirements
- N/A

## Implementation
1.  Sign in to the **SharePoint admin center**.

2. Select **Policies** \> **Sharing**.

3. Under **File and folder links**, set the permission that is selected by default for sharing links to **View**.

4. Select **Save**.
