# MS.SHAREPOINT.3.2v1: The allowable file and folder permissions for links SHALL be set to view only.
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 3. Securing "Anyone" Links and Verification Code Users · Criticality: SHALL

## Policy
The allowable file and folder permissions for links SHALL be set to view only.

- _Rationale:_ Unauthorized changes to files can be made if link permissions allow editing by anyone. By restricting permissions on links to view only, administrators can prevent anonymous file changes.
- _Last modified:_ March 2025
- _Note:_ This policy is only applicable if the external sharing slider in the SharePoint admin center is set to **Anyone**.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6
- _MITRE ATT&CK TTP Mapping:_
  - [T1080: Taint Shared Content](https://attack.mitre.org/techniques/T1080/)
  - [T1565: Data Manipulation](https://attack.mitre.org/techniques/T1565/)
    - [T1565.001: Stored Data Manipulation](https://attack.mitre.org/techniques/T1565/001/)

## Resources
- [Secure external sharing recipient experience \| Microsoft
  Documents](https://learn.microsoft.com/en-us/sharepoint/what-s-new-in-sharing-in-targeted-release)

## License Requirements
- N/A

## Implementation
1.  Sign in to the **SharePoint admin center**.

2.  Select **Policies** \> **Sharing**.

3.  Scroll to the section titled, **Choose expiration and permissions options for Anyone links**.

4.  Set the configuration items in the section to **These links can give these permissions**.

5.  Set the **Files** option to **View**.

6.  Set the **Folders** option to **View**.

7.  Select **Save**.
