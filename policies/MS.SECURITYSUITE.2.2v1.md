# MS.SECURITYSUITE.2.2v1: Domain impersonation protection SHOULD be enabled for domains owned by the agency.
Product: securitysuite · Baseline: securitysuite · Group: 2. Impersonation Protection · Criticality: SHOULD

## Policy
Domain impersonation protection SHOULD be enabled for domains owned by the agency.

- _Rationale:_ Configuring domain impersonation protection for agency-owned domains
reduces the risk of a user being deceived by a look-alike domain.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
    - [T1566.002: Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)
  - [T1656: Impersonation](https://attack.mitre.org/techniques/T1656/)

## Resources
- [Impersonation settings in anti-phishing policies in Microsoft Defender for Office 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-phishing-policies-about?view=o365-worldwide#impersonation-settings-in-anti-phishing-policies-in-microsoft-defender-for-office-365)
- [Use the Microsoft 365 Defender portal to assign Standard and Strict preset security policies to users \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/preset-security-policies?view=o365-worldwide#use-the-microsoft-365-defender-portal-to-assign-standard-and-strict-preset-security-policies-to-users)
- [User impersonation protection \| Microsoft Learn](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about#user-impersonation-protection)

## License Requirements
- Impersonation protection and advanced phishing thresholds require
  Defender for Office 365 Plan 1 or 2. These are included with E5 and G5
  and are available as add-ons for E3 and G3. As of January 2026,
  anti-phishing for user and domain impersonation and spoof intelligence
  are not yet available in M365 Government Community Cloud (GCC High) and Department of Defense (DoD) environments. See [Platform features \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-us-government/office-365-us-government#platform-features)
  for current offerings.

## Implementation
1.  Sign in to **Microsoft 365 Defender**.
2.  Under **Email & collaboration**, select **Policies & rules**.
3.  Select **Threat policies**.
4.  Under **Policies**, select **Anti-phishing**.
5.  Select the **Office365 Anti-phish Default (Default)** policy.
6.  Click **Edit protection settings**.
7.  Under **Impersonation**, check **Enable domains to protect** and **Include domains I own**.
8.  Click **Save**.
9. Click **Edit actions**.
10. Under **If a message is detected as domain impersonation**, select one of the following:
    - **Redirect the message to other email addresses**
    - **Move the message to the recipients' Junk Email folders**
    - **Quarantine the message**
    - **Delete the message before it's delivered**
11.  Click **Done**, then click **Save**.
