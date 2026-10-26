# MS.SECURITYSUITE.1.1v1: Emails with click-to-run file attachments SHALL be blocked including, at a minimum, .exe, .cmd, and .vbe files.
Product: securitysuite · Baseline: securitysuite · Group: 1. Malware Protection · Criticality: SHALL

## Policy
Emails with click-to-run file attachments SHALL be blocked including, at a minimum, .exe, .cmd, and .vbe files.

- _Rationale:_ Malicious attachments often take the form of click-to-run files.
When necessary to share high risk file types, it is better to share them via a means other
than email. The dangers of allowing high risk file types to be sent over email outweigh
any potential benefits. Filtering email attachments based on file types can
prevent the spread of malware distributed via click-to-run email attachments.
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
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

Because the steps for MS.SECURITYSUITE.1.1v1 and MS.SECURITYSUITE.1.2v1 share similarities,
steps for both policies are included in this section. Steps that do not strictly apply to
MS.SECURITYSUITE.1.1v1 are followed by the applicable SCuBA policy in parentheses.

For users not added to the standard or strict preset policies:
1.  Sign in to **Microsoft 365 Defender**.
2.  Under **Email & collaboration**, select **Policies & rules**.
3.  Select **Threat policies**.
4.  Under **Policies**, select **Anti-malware**.
5.  If modifying an existing policy:
    1. Click the name of the policy from the policy list to open the policy summary.
    2. Click **Edit user and domains**. _Note:_ The **Default (default)** policy applies to all users, so skip this step if modifying the default policy.
        - Add users, groups, and domains as needed. To make the policy apply to all users, under
          **Domains**, enter all the tenant domains.
        - (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
          to be exempted from this policy.
        - Click **Save**.
    3. Click **Edit protection settings**.
    4. Check **Enable zero-hour auto purge for malware (Recommended)**. (_MS.SECURITYSUITE.1.2v1_)
    5. Check **Enable the common attachments filter**.
    6. Click **Customize file types** and select at a minimum .exe, .cmd, and .vbe.
    7. Click **Save**.
6.  If creating a new policy:
    1. Click **Create**.
    2. After naming the policy, click **Next**.
    3. Add users, groups, and domains as needed. To make the policy apply to all users, under
       **Domains**, enter all the tenant domains.
    4. (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
       to be exempted from this policy.
    5. Click **Next**.
    6. Check **Enable zero-hour auto purge for malware (Recommended)**. (_MS.SECURITYSUITE.1.2v1_)
    7. Check **Enable the common attachments filter**.
    8. Click **Select file types** and select, at a minimum, .exe, .cmd, and .vbe. Then click **Done**.
    9. Click **Next**, then click **Submit**.
