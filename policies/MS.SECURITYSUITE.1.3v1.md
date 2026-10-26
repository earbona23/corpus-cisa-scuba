# MS.SECURITYSUITE.1.3v1: Emails identified as containing malware SHALL be quarantined or dropped.
Product: securitysuite · Baseline: securitysuite · Group: 1. Malware Protection · Criticality: SHALL

## Policy
Emails identified as containing malware SHALL be quarantined or dropped.

- _Rationale:_ Email can be used as a mechanism for delivering malware.
Preventing emails with known malware from reaching user mailboxes helps ensure
users cannot interact with those emails.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)

## Resources
- [Anti-malware protection for cloud mailboxes \| Microsoft Learn](https://learn.microsoft.com/en-us/defender-office-365/anti-malware-protection-about)
- [Set up Safe Attachments policies in Microsoft Defender for Office 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-attachments-policies-configure?view=o365-worldwide)

## License Requirements
Safe attachments require Defender for Office 365 Plan 1 or 2. These are included with
  E5 and G5 and are available as add-ons for E3 and G3.

## Implementation
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

For users not added to the standard or strict preset policies:
1.  Sign in to **Microsoft 365 Defender**.
2.  Under **Email & collaboration**, select **Policies & rules**.
3.  Select **Threat policies**.
4.  Under **Policies**, select **Safe attachments**.
5.  If modifying an existing policy:
    1. Click the name of the policy from the policy list to open the policy summary.
    2. Click **Edit user and domains**. _Note:_ The **Default (default)** policy applies to all users. Skip this step if modifying the default policy.
        - Add users, groups, and domains as needed. To make the policy apply to all users, under
          **Domains**, enter all the tenant domains.
        - (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
          to be exempted from this policy.
        - Click **Save**.
    3. Click **Edit settings**.
    4. Under **Safe Attachments unknown malware response**, select **Block** or **Dynamic delivery**.
    5. Click **Save**.
6.  If creating a new policy:
    1. Click **Create**.
    2. After naming the policy, click **Next**.
    3. Add users, groups, and domains as needed. To make the policy apply to all users, under
       **Domains**, enter all the tenant domains.
    4. (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
       to be exempted from this policy.
    5. Click **Next**.
    6. Under **Safe Attachments unknown malware response**, select **Block** or **Dynamic delivery**.
    7. Click **Next**, then click **Submit**.
