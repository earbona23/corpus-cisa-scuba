# MS.EXO.7.1v1: External sender warnings SHALL be implemented.
Product: Exchange Online · Baseline: exo · Group: 7. External Sender Warnings · Criticality: SHALL

## Policy
External sender warnings SHALL be implemented.

- _Rationale:_ Alerting users when emails originate from outside their organization can encourage them to exercise increased caution, especially if they expected to receive the email from an internal sender.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

## Resources
- [Mail flow rules (transport rules) in Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules)

- [Capacity Enhancement Guide: Counter-Phishing Recommendations for
  Federal Agencies \|
  CISA](https://www.cisa.gov/sites/default/files/publications/Capacity_Enhancement_Guide-Counter-Phishing_Recommendations_for_Federal_Agencies.pdf)

- [Actions To Counter Email-Based Attacks On Election-Related Entities
  \|
  CISA](https://www.cisa.gov/sites/default/files/publications/CISA_Insights_Actions_to_Counter_Email-Based_Attacks_on_Election-Related_S508C.pdf)

## License Requirements
- N/A

## Implementation
To create a mail flow rule to produce external sender warnings:

1.  Sign in to the **Exchange admin center**.

2.  Under **Mail flow**, select **Rules**.

3.  Click the plus (**+**) button to create a new rule.

4.  Select **Modify messages…**.

5.  Give the rule an appropriate name.

6.  Under **Apply this rule if…,** select **The sender is external/internal**.

7.  Under **Select sender location**, select **Outside the organization**, then click **OK**.

8.  Under **Do the following…,** select **Prepend the subject of the message with…**.

9.  Under **Specify subject prefix**, enter a message such as
    "\[External\]" (without the quotation marks), then click **OK**.

10. Click **Next**.

11. Under **Choose a mode for this rule**, select **Enforce**.

12. Leave the **Severity** level as **Not specified**.

13. Leave the **Match sender address in message** as **Header** and click **Next**.

14. Click **Finish**, then click **Done**.

15. The new rule will be disabled. Re-select the new rule to show its
    settings and slide the **Enable or disable rule** slider to the right
    until it shows as **Enabled**.
