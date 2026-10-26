# MS.TEAMS.1.1v1: External meeting participants SHOULD NOT be enabled to request control of shared desktops or windows.
Product: Teams · Baseline: teams · Group: 1. Meeting Policies · Criticality: SHOULD

## Policy
External meeting participants SHOULD NOT be enabled to request control of shared desktops or windows.

- _Rationale:_ An external participant with control of a shared screen could potentially perform unauthorized actions on the shared screen. This policy reduces that risk by removing an external participant's ability to request control. However, if an agency has a legitimate use case to grant this control, it may be done on a case-by-case basis.
- _Last modified:_ July 2023
- _Note:_ This policy applies to the Global (Org-wide default) meeting policy, as well as custom meeting policies.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-17a
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
To help ensure external participants do not have the ability to request
control of the shared desktop or window in the meeting:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **Meetings** > **Meeting policies**.

3.  Select the **Global (Org-wide default)** policy.

4.  Under the **Content sharing** section, ensure **External participants can give or request control** is set to the **Off** position.

5.  Select **Save** (if applicable).

6.  If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
