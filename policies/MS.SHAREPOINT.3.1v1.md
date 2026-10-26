# MS.SHAREPOINT.3.1v1: Expiration days for "Anyone" links SHALL be set to 30 days or less.
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 3. Securing "Anyone" Links and Verification Code Users · Criticality: SHALL

## Policy
Expiration days for "Anyone" links SHALL be set to 30 days or less.

- _Rationale:_ Links may be used to provide access to information for a short period of time. Without expiration, however, access is indefinite. By setting expiration timers for links, administrators can prevent unintended sustained access to the link.
- _Last modified:_ March 2025
- _Note:_ This policy is only applicable if the external sharing slider in the SharePoint admin center is set to **Anyone**.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, AC-21b
- _MITRE ATT&CK TTP Mapping:_
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
  - [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)
    - [T1213.002: Sharepoint](https://attack.mitre.org/techniques/T1213/002/)
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)

## Resources
- [Secure external sharing recipient experience \| Microsoft
  Documents](https://learn.microsoft.com/en-us/sharepoint/what-s-new-in-sharing-in-targeted-release)

## License Requirements
- N/A

## Implementation
1.  Sign in to the **SharePoint admin center**.

2.  Select **Policies** \> **Sharing**.

3.  Scroll to the section titled, **Choose expiration and permissions options for Anyone links**.

4.  Select the checkbox labeled **These links must expire within this many days**.

5.  Enter **30** days or less.

6.  Select **Save**.
