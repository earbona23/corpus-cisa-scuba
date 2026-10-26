# MS.TEAMS.1.5v1: Dial-in users SHOULD NOT be enabled to bypass the lobby.
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHOULD

## Policy
Dial-in users SHOULD NOT be enabled to bypass the lobby.

- _Rationale:_ Automatically admitting dial-in users reduces control over who can participate in a meeting and increases the potential for data breaches. This policy reduces the risk by requiring all dial-in users to wait in a lobby until they are admitted by an authorized meeting participant.
- _Last modified:_ July 2023
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy, as well as custom meeting policies.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-15a
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
To configure settings for anonymous users so that they are not able to bypass the lobby:

1.	Sign in to the **Microsoft Teams admin center**.

2.	Select **Meetings** > **Meeting policies**.

3.	Select the **Global (Org-wide default)** policy.

4.	Under the **Meeting join & lobby** section, ensure **People dialing in can bypass the lobby** is set to the **Off** position.

5.  Select **Save** (if applicable).

6.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
