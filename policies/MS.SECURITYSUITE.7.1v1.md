# MS.SECURITYSUITE.7.1v1: URL comparison with a block-list SHOULD be enabled for URLs in emails, Teams messages, and Office documents.
Product: securitysuite · Baseline: securitysuite · Group: 7. Link Protection · Criticality: SHOULD

## Policy
URL comparison with a block-list SHOULD be enabled for URLs in emails, Teams messages, and Office documents.

- _Rationale:_ Links in email may direct users to malicious websites. Blocking access to known, malicious URLs can prevent users from accessing known malicious websites.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.002: Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)

## Resources
- [Set up Safe Links policies in Microsoft Defender for Office 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/defender-office-365/safe-links-policies-configure)

## License Requirements
Safe links require Defender for Office 365 Plan 1 or 2. These are included with
E5 and G5 and are available as add-ons for E3 and G3.

## Implementation
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

Because the steps for MS.SECURITYSUITE.7.1v1, MS.SECURITYSUITE.7.2v1, and MS.SECURITYSUITE.7.3v1 share
similarities, steps for all three policies are included in this section. Steps that do not
strictly apply to MS.SECURITYSUITE.7.1v1 are followed by the applicable SCuBA policy in parentheses.

For users not added to the standard or strict preset policies:
1.  Sign in to **Microsoft 365 Defender**.
2.  Under **Email & collaboration**, select **Policies & rules**.
3.  Select **Threat policies**.
4.  Under **Policies**, select **Safe links**.
5.  If modifying an existing policy:
    1. Click the name of the policy from the policy list to open the policy summary.
    2. Click **Edit users and domains**.
        - Add users, groups, and domains as needed. To make the policy apply to all users, under
          **Domains**, enter all the tenant domains.
        - (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
          to be exempted from this policy.
        - Click **Save**.
    3. Click **Edit protection settings**.
    4. Under **Email**, select the following options:
        - **On: Safe Links checks a list of known, malicious links when users click links in email. URLs are rewritten by default.**
        - **Apply Safe Links to email messages sent within the organization**
        - **Apply real-time URL scanning for suspicious links and links that point to files** (_MS.SECURITYSUITE.7.2v1_)
        - **Wait for URL scanning to complete before delivering the message** (_MS.SECURITYSUITE.7.2v1_)
    5. Under **Teams**, select **On: Safe Links checks a list of known, malicious links when users click links in Microsoft Teams. URLs are not rewritten.**
    6. Under **Office 365 apps**, select **On: Safe Links checks a list of known, malicious links when users click links in Microsoft Office apps. URLs are not rewritten.**
    7. Under **Click protection settings**, select **Track user clicks**. (_MS.SECURITYSUITE.7.3v1_)
    8. Click **Save**.
6. If creating a new policy:
    1. Click **Create**.
    2. After naming the policy, click **Next**.
    3. Add users, groups, and domains as needed. To make the policy apply to all users, under
       **Domains**, enter all the tenant domains.
    4. (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
       to be exempted from this policy.
    5. Click **Next**.
    6. Under **Email**, select the following options:
        - **On: Safe Links checks a list of known, malicious links when users click links in email. URLs are rewritten by default.**
        - **Apply Safe Links to email messages sent within the organization**
        - **Apply real-time URL scanning for suspicious links and links that point to files** (_MS.SECURITYSUITE.7.2v1_)
        - **Wait for URL scanning to complete before delivering the message** (_MS.SECURITYSUITE.7.2v1_)
    7. Under **Teams**, select **On: Safe Links checks a list of known, malicious links when users click links in Microsoft Teams. URLs are not rewritten.**
    8. Under **Office 365 apps**, select **On: Safe Links checks a list of known, malicious links when users click links in Microsoft Office apps. URLs are not rewritten.**
    9. Under **Click protection settings**, select **Track user clicks**. (_MS.SECURITYSUITE.7.3v1_)
    10. Click **Next**, then click **Submit**.
