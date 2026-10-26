# MS.TEAMS.2.2v2: Unmanaged users SHALL NOT be enabled to initiate contact with internal users.
Product: Teams · Baseline: teams · Group: 2. External User Access · Criticality: SHALL

## Policy
Unmanaged users SHALL NOT be enabled to initiate contact with internal users.

- _Rationale:_ Allowing contact from unmanaged users can expose users to email and contact address harvesting. The policy provides protection against this type of harvesting.
- _Last modified:_ August 2026
- _Note:_ This policy's availability may vary by Microsoft 365 environment and tenant, particularly within Government Community Cloud (GCC), GCC High, and Department of Defense (DoD) tenants.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7, SI-8
- _MITRE ATT&CK TTP Mapping:_
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
To ensure unmanaged users cannot initiate contact with internal users:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **External collaboration** > **External access** > **Policies** (Tab).

3.  Select **Global (Org-wide Default)**.

4.  On the **Edit policy details** screen, set **People in my org can chat and have meetings with external users who have unmanaged Microsoft accounts** to one of the following:
    1. To completely block contact with unmanaged users, toggle the setting to the **Off** position.
    2. To allow contact with unmanaged users only if the internal user initiates the contact:
        - Toggle the setting to the **On** position.
        - Clear the check next to **People in my org can join external meetings and receive new chats from users who have unmanaged Microsoft accounts.**.

5.  Click **Save** and then **Confirm**.

    **NOTE:** You'll receive a pop-up at this stage stating **Changes will take time to take effect - Changes to Global (Org-wide default) will have an impact across the organization and can't be rolled back immediately.** This is an expected message.

6.	If custom policies exist on the tenant, repeat these steps for each policy, selecting the appropriate policy in step 3.
