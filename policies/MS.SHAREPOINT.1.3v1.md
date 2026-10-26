# MS.SHAREPOINT.1.3v1: External sharing SHALL be restricted to approved external domains and/or users in approved security groups per interagency collaboration needs.
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 1. External Sharing · Criticality: SHALL

## Policy
External sharing SHALL be restricted to approved external domains and/or users in approved security groups per interagency collaboration needs.

- _Rationale:_ By limiting sharing to domains or approved security groups used for interagency collaboration purposes, administrators can help prevent sharing with unknown organizations and individuals.
- _Last modified:_ September 2026
- _Note:_ This policy is only applicable if the external sharing slider in the SharePoint admin center is not set to **Only people in your organization** OR **External guests**.
- _Note:_ The approved-domain and approved-security-group restrictions are applied by SharePoint only when sharing files with external users that do not have an existing user account in the tenant's Entra directory. Sharing files with an external user that already has a user account in Entra is not restricted by the SharePoint settings described in this Scuba policy.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, AC-6(10)
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
Note: If SharePoint external sharing is set to its most restrictive setting of "Only people in your organization," then no external sharing is allowed and no implementation changes are required for this policy item.

1.  Sign in to the **SharePoint admin center**.

2.  Select **Policies** \> **Sharing**.

3.  Expand **More external sharing settings**.

4.  Select **Limit external sharing by domain**.

5.  Select **Add domains**.

6.  Add each approved external domain with which users are allowed to share files.

7.  Select **Manage security groups**.

8. Add each approved security group. Members of these groups will be allowed to share files externally.

9.  Select **Save**.
