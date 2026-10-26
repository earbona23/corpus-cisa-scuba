# MS.TEAMS.1.6v1: Meeting recording SHOULD be disabled.
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHOULD

## Policy
Meeting recording SHOULD be disabled.

- _Rationale:_ Allowing any user to record an Microsoft Teams meeting may lead to unauthorized disclosure of shared information, including audio, video, and shared screens. By disabling the meeting recording setting in the Global (Org-wide default) meeting policy, the agency limits information exposure.
- _Last modified:_ March 2025
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy. Custom policies MAY be created to allow more flexibility for specific users.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7
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
To configure the settings that control meeting recordings:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **Meetings** > **Meeting policies**.

3.  Select the **Global (Org-wide default)** policy.

4.  Under the **Recording & transcription** section, ensure **Meeting recording** is set to the **Off** position.

5.  Select **Save** (if applicable).

6.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
