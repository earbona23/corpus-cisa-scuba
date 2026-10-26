# MS.SECURITYSUITE.6.1v1: Emails detected as spam and phishing SHALL NOT be delivered to the user's inbox.
Product: securitysuite · Baseline: securitysuite · Group: 6. Inbound Anti-Spam Protections · Criticality: SHALL

## Policy
Emails detected as spam and phishing SHALL NOT be delivered to the user's inbox.

- _Rationale:_ Spam is a constant threat because junk mail can reduce user productivity, fill up mailboxes unnecessarily, and potentially include malicious links or attachments.
Moving spam messages to a separate junk or quarantine folder helps users filter out spam while still giving them the ability to review messages in case a message is filtered incorrectly.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

## Resources
- [Configure anti-spam policies in EOP \| Microsoft Learn](https://learn.microsoft.com/en-us/defender-office-365/anti-spam-policies-configure?view=o365-worldwide)

## License Requirements
- N/A

## Implementation
Both the standard and strict preset policies meet this baseline policy requirement,
so no further actions are needed for users added to those policies. See
[Adding Users to the Preset Security Policies](#appendix-a-adding-users-to-the-preset-security-policies)
for instructions on adding users to these policies.

Because the steps for MS.SECURITYSUITE.6.1v1 and MS.SECURITYSUITE.6.2v1 share similarities,
steps for both policies are included in this section. Steps that do not strictly apply to
MS.SECURITYSUITE.6.1v1 are followed by the applicable SCuBA policy in parentheses.

For users not added to the standard or strict preset policies:
1.  Sign in to **Microsoft 365 Defender**.
2.  Under **Email & collaboration**, select **Policies & rules**.
3.  Select **Threat policies**.
4.  Under **Policies**, select **Anti-spam**.
5.  If modifying an existing policy:
    1. Click the name of the policy from the policy list to open the policy summary. Note: be sure to
    select an *inbound* policy. If it's a custom policy, it will say "Custom anti-spam policy"
    under **Type** instead of **Custom output spam policy**.
    2. Click **Edit users, groups, and domains**. Note: The **Anti-spam inbound (Default)** policy applies to all users, so skip this step if modifying the default policy.
      - Add users, groups, and domains as needed. To make the policy apply to all users, under
        **Domains**, enter all the tenant domains.
      - (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
        to be exempted from this policy.
      - Click **Save**.
    3. Click **Edit spam threshold and properties**. See [Recommended email and collaboration threat policy settings for cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365)
    for configuration guidance. We recommend mirroring the values used for either the standard or
    strict preset policies. Click **Save**.
    4. Click **Edit actions**.
    5. For each email classification (**Spam**, **High confidence spam**, **Phishing**, and **High confidence phishing**), select one of the following options:
      - **Move message to junk email folder**
      - **Redirect message to email address**
      - **Delete message**
      - **Quarantine message**

     Note: **Delete message** is not available for **High confidence phishing**; choose one of the other three options for that classification.
    
    6. If you selected **Redirect message to email address**, also fill in an appropriate email for
      the **Redirect to this email address** field, such as a mailbox set up for monitoring incoming
      spam and phishing messages.
    7. Click **Edit allowed and blocked senders and domains**.
    8. Under **Allowed**, click **Allow domains**. Select any domains that have been allowed, then
        click **Delete** (the trash icon). (_MS.SECURITYSUITE.6.2v1_)
    9. Click **Save**.
7.  If creating a new policy:
    1. Click **Create**, then **Inbound**.
    2. After naming the policy, click **Next**.
    3. Add users, groups, and domains as needed. To make the policy apply to all users, under
       **Domains**, enter all the tenant domains.
    4. (Optional) Under **Exclude these users, groups, and domains**, add **Users** and **Groups**
       to be exempted from this policy.
    5. Click **Next**.
    6. On the **Bulk email threshold & spam properties** page, see [Recommended email and collaboration threat policy settings for cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365)
    for configuration guidance. We recommend mirroring the values used for either the standard or
    strict preset policies.
    7. For each email classification (**Spam**, **High confidence spam**, **Phishing**, and **High confidence phishing**), select one of the following options:
      - **Move message to junk email folder**
      - **Redirect message to email address**
      - **Delete message**
      - **Quarantine message**
    8. If you selected **Redirect message to email address**, also fill in an appropriate email for
      the **Redirect to this email address** field, such as a mailbox set up for monitoring incoming
      spam and phishing messages.
    9. Click **Next**.
    10. On the **Allow & block list** page, do not click **Allow domains** under **Allowed**. It
    should read **Domains (0)** under **Allowed**. (_MS.SECURITYSUITE.6.2v1_)
    11. Click **Next**, then click **Submit**.
