# MS.SECURITYSUITE.1.4v1: SharePoint, OneDrive, and Teams message attachments SHOULD be scanned for malware.
Product: securitysuite · Baseline: securitysuite · Group: 1. Malware Protection · Criticality: SHOULD

## Policy
SharePoint, OneDrive, and Teams message attachments SHOULD be scanned for malware.

- _Rationale:_ Files shared through Teams or hosted on SharePoint/OneDrive can be used as a mechanism for delivering malware. In many cases, malware can be detected through scanning, reducing the risk for end users.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)

## Resources
- [Anti-malware protection for cloud mailboxes \| Microsoft Learn](https://learn.microsoft.com/en-us/defender-office-365/anti-malware-protection-about)
- [Set up Safe Attachments policies in Microsoft Defender for Office 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-attachments-policies-configure?view=o365-worldwide)

## License Requirements
Safe attachments require Defender for Office 365 Plan 1 or 2. These are included with
  E5 and G5 and are available as add-ons for E3 and G3.

## Implementation
This baseline policy is _not_ covered by the preset policies, so these steps
need to be taken even if the standard or strict policies are used.

1.  Sign in to **Microsoft 365 Defender**.

2.  Under **Email and collaboration**, select **Policies and rules**.

3.  Select **Threat policies**.

4.  Under **Policies**, select **Safe attachments**.

5.  Select **Global settings**.

6.  Toggle the **Turn on Defender for Office 365 for SharePoint, OneDrive, and Microsoft Teams**
    slider to **On**.

7. Click **Save**.
