# MS.SHAREPOINT.3.3v2: Reauthentication days for people who use a verification code SHALL be set to 30 days or less.
Product: SharePoint Online and OneDrive · Baseline: sharepoint · Group: 3. Securing "Anyone" Links and Verification Code Users · Criticality: SHALL

## Policy
Reauthentication days for people who use a verification code SHALL be set to 30 days or less.

- _Rationale:_ By setting expiration timers for verification code access, administrators can prevent unintended sustained access to documents.
- _Last modified:_ April 2026
- _Note:_ This policy is only applicable if the external sharing slider in the SharePoint admin center is set to **Anyone**, **New and existing guests**, or **Existing guests.**
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-11
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

3.  Expand **More external sharing settings**.

4. Select **People who use a verification code must reauthenticate after this many days**.

5.  Enter **30** days or less.

6. Select **Save**.

**`TLP:CLEAR`**
