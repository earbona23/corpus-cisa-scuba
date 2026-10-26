# MS.TEAMS.1.3v1: Anonymous users and dial-in callers SHOULD NOT be admitted automatically.
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHOULD

## Policy
Anonymous users and dial-in callers SHOULD NOT be admitted automatically.

- _Rationale:_ Automatically allowing admittance to anonymous and dial-in users diminishes control of meeting participation and invites a potential data breach. This policy reduces that risk by requiring all anonymous and dial-in users to wait in a lobby until admitted by an authorized meeting participant. If the agency has a use case to admit members of specific trusted organizations and/or B2B guests automatically, custom policies may be created and assigned to authorized meeting organizers.
- _Last modified:_ July 2023
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy. Custom meeting policies MAY be created to allow specific users more flexibility. For example, B2B guest users and trusted partner members may be admitted automatically into meetings organized by authorized users.
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
To configure settings for anonymous users so that they are not admitted automatically:

1.	Sign in to the **Microsoft Teams admin center**.

2.	Select **Meetings** > **Meeting policies**.

3.	Select the **Global (Org-wide default)** policy.

4.	Under the **Meeting join & lobby** section, ensure **Who can bypass the lobby** is **not** set to **Everyone**. Bypassing the lobby should be set to **People in my org**, though other options may be used if needed or approved.

5.	In the same section, ensure **People dialing in can bypass the lobby** is set to the **Off** position.

6.  Select **Save** (if applicable).

7.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
