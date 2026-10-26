# MS.TEAMS.1.7v2: "Record an event" SHOULD NOT be set to "Always record."
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHOULD

## Policy
"Record an event" SHOULD NOT be set to "Always record."

- _Rationale:_ Limiting recording permissions to only the organizer minimizes the security risk for live events, limiting recording to the organizer's discretion. This setting helps reduce data leakage and other security risks. Administrators can also disable recording for all live events.
- _Last modified:_ March 2025
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy. Custom policies MAY be created to allow more flexibility for specific users.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-21a
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
To configure the settings that control "live events" meeting recordings:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **Meetings** > **Live events policies**.

3.  Select **Global (Org-wide default)** policy.

4.  Set **Record an event** to either  **Organizer can record** or **Never record**.

5.  Select **Save** (if applicable).

6.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
