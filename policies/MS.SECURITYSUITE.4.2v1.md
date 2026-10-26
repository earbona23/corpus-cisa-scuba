# MS.SECURITYSUITE.4.2v1: The alerts SHOULD be sent to a monitored address or incorporated into a Security Information and Event Management (SIEM).
Product: securitysuite · Baseline: securitysuite · Group: 4. Alerts · Criticality: SHOULD

## Policy
The alerts SHOULD be sent to a monitored address or incorporated into a Security Information and Event Management (SIEM).

- _Rationale:_ If not resolved promptly, suspicious or malicious events may have an even greater impact on users/the agency. Sending alerts to a monitored email address or SIEM system helps ensure events are acted upon in a timely manner to limit overall impact.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-4(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1562: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
    - [T1562.006: Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)

## Resources
- [Alert policies in Microsoft 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/alert-policies?view=o365-worldwide)

## License Requirements
- N/A

## Implementation
For each enabled alert, to add one or more email recipients:

1. Sign in to **Microsoft 365 Defender**.

2. Under **Email & collaboration**, select **Policies & rules**.

3. Select **Alert Policy**.

4. Click the alert policy to modify.

5. Click the pencil icon next to **Set your recipients**.

6. Check the **Opt-In for email notifications** box.

7. Add one or more email addresses to the **Email recipients** text box.

8. Click **Next**.

9. On the **Review** page, click **Submit** to save the notification settings.
