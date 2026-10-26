# MS.SECURITYSUITE.2.4v1: User warnings, comparable to the user safety tips included with EOP, SHOULD be displayed.
Product: securitysuite · Baseline: securitysuite · Group: 2. Impersonation Protection · Criticality: SHOULD

## Policy
User warnings, comparable to the user safety tips included with EOP, SHOULD be displayed.

- _Rationale:_ Some tasks are better suited for automated processes, such as identifying
unusual characters in the `FROM` address or identifying a first-time sender.
User warnings can handle these tasks, reducing the burden on end users and the risk of
successful phishing attempts.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AT-2b, SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
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
5.  Select the **Office365 AntiPhish Default (Default)** policy.
6.  Click **Edit actions**.
7.  Under **Safety tips & indicators**, enable each safety tip and indicator.
8.  Click **Save**.
