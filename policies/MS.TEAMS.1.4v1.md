# MS.TEAMS.1.4v1: Internal users SHOULD be admitted to Microsoft Teams meetings automatically.
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHOULD

## Policy
Internal users SHOULD be admitted to Microsoft Teams meetings automatically.

- _Rationale:_ Requiring internal users to wait in the lobby for explicit admission can lead to admission fatigue. This policy enables internal users to be automatically admitted to the meeting through global policy.
- _Last modified:_ July 2023
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy. Custom meeting policies MAY be created to allow specific users more flexibility.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3
- _MITRE ATT&CK TTP Mapping:_
  - None

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
To configure settings so that internal users are admitted automatically:

1.	Sign in to the **Microsoft Teams admin center**.

2.	Select **Meetings** > **Meeting policies**.

3.	Select the **Global (Org-wide default)** policy.

4.	Under the **Meeting join and lobby** section, ensure **Who can bypass the lobby** is set to **People in my org**.

5.	In the same section, ensure **People dialing in can bypass the lobby** is set to the **Off** position.

6.  Select **Save** (if applicable).

7.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
