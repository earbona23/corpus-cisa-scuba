# MS.TEAMS.4.1v1: Microsoft Teams email integration SHALL be disabled.
Product: Teams · Baseline: teams · Group: 4. Teams Email Integration · Criticality: SHALL

## Policy
Microsoft Teams email integration SHALL be disabled.

- _Rationale:_ Microsoft Teams email integration associates a Microsoft (not tenant domain) email address with a Teams channel. Channel emails are addressed using the Microsoft-owned domain <code>&lt;teams.ms&gt;</code>. By disabling Teams email integration, the agency prevents potentially sensitive Teams messages from being sent through external email gateways.
- _Last modified:_ July 2023
- _Note:_ Teams email integration availability may vary by Microsoft 365 environment and tenant, particularly within Government Community Cloud (GCC), GCC High, and Department of Defense (DoD) tenants.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8, SC-7(10)(a), AC-4
- _MITRE ATT&CK TTP Mapping:_
  - [T1204: User Execution](https://attack.mitre.org/techniques/T1204/)
    - [T1204.001: Malicious Link](https://attack.mitre.org/techniques/T1204/001/)
    - [T1204.002: Malicious File](https://attack.mitre.org/techniques/T1204/002/)

## Resources
- [Email Integration \| Microsoft
Learn](https://learn.microsoft.com/en-us/microsoftteams/settings-policies-reference#email-integration)

## License Requirements
- N/A

## Implementation
To ensure users cannot send emails and their contents to a channel email address:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **Teams** > **Teams Settings**.

3.  Under the **Email integration** section, ensure **Users can send emails to a channel email address** is set to the **Off** position.

4. Under the same section, ensure the **Accept channel email from these SMTP domains** field has no domains entered and that it remains empty.

5.  Select **Save** (if applicable).
