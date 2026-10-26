# MS.TEAMS.2.1v2: External access for users SHALL only be enabled on a per-domain basis.
Product: Teams · Baseline: teams · Group: 2. External User Access · Criticality: SHALL

## Policy
External access for users SHALL only be enabled on a per-domain basis.

- _Rationale:_ The default configuration allows members to communicate with all external users with similar access permissions. Unrestricted access can lead to data breaches and other security threats. This policy provides protection against threats posed by unrestricted access, allowing communication with only trusted domains.
- _Last modified:_ August 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1199: Trusted Relationship](https://attack.mitre.org/techniques/T1199/)
  - [T1204: User Execution](https://attack.mitre.org/techniques/T1204/)
    - [T1204.001: Malicious Link](https://attack.mitre.org/techniques/T1204/001/)

## Resources
- [IT Admins - Manage external meetings and chat with people and organizations using Microsoft identities \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoftteams/manage-external-access)

- [Teams settings and policies reference \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoftteams/meeting-settings-in-teams#allow-anonymous-users-to-join-meetings)

- [Use guest access and external access to collaborate with people
  outside your organization \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoftteams/communicate-with-users-from-other-organizations)

- [Manage chat with external Teams users not managed by an organization
\| Microsoft
Learn](https://learn.microsoft.com/en-us/microsoftteams/manage-external-access#manage-chat-with-external-teams-users-not-managed-by-an-organization)

## License Requirements
- N/A

## Implementation
To enable external access for specific domains only:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **External collaboration** > **External access** > **Organization settings** (Tab).

3.  Next to **Teams and Skype for Business users in external organizations**, select **Allow only specific external domains**.

4.  Select **Add a domain**. Enter the allowed domain in the text box, press **Add**, and then select **Done** to save your changes.

    **NOTE:** Domains will need to be added in this step in order for users to communicate with them. Ensure only currently allowed domains remain present in the list.

5.  Click **Save** and then **Confirm**.

    **NOTE:** You'll receive a pop-up at this stage stating **Changes will take time to take effect - Changes to External access will have an impact across the organization and can't be rolled back immediately.** This is an expected message.
