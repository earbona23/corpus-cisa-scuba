# MS.TEAMS.1.2v2: Anonymous users SHALL NOT be enabled to start Microsoft Teams meetings.
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHALL

## Policy
Anonymous users SHALL NOT be enabled to start Microsoft Teams meetings.

- _Rationale:_ This policy protects against anonymous users starting Microsoft Teams meetings and potentially scraping internal contacts. The policy is beneficial for agencies that have implemented custom policies, providing flexibility for some users to automatically admit "everyone" to an Microsoft Teams meeting.
- _Last modified:_ August 2025
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy, and custom meeting policies if they exist.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-15a
- _MITRE ATT&CK TTP Mapping:_
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.001: Default Accounts](https://attack.mitre.org/techniques/T1078/001/)

## Resources
- [Manage who can present and request control in Microsoft Teams \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoftteams/meeting-who-present-request-control)
- [Meeting policy settings \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/settings-policies-reference#meetings)

- [Teams cloud meeting recording \| Microsoft
Learn ](https://learn.microsoft.com/en-us/microsoftteams/cloud-recording)

- [Assign policies in Teams – getting started \| Microsoft
Learn](https://learn.microsoft.com/en-us/microsoftteams/policy-assignment-overview)
- [Live Event Recording Policies \| Microsoft
Learn](https://learn.microsoft.com/en-us/microsoftteams/teams-live-events/live-events-recording-policies)

## License Requirements
- N/A

## Implementation
To configure settings for anonymous users so that they cannot start meetings:

1.	Sign in to the **Microsoft Teams admin center**.

2.	Select **Meetings** > **Meeting policies**.

3.	Select the **Global (Org-wide default)** policy.

4.	Under the **Meeting join and lobby** section, ensure the **Anonymous users and dial-in callers can start a meeting** setting remains in the default **Off** position.

5.  Select **Save** (if applicable).

6.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
