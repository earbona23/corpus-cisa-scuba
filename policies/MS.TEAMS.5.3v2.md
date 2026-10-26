# MS.TEAMS.5.3v2: Agencies SHOULD only allow installation of custom applications approved by the agency.
Product: Teams · Baseline: teams · Group: 5. App Management · Criticality: SHOULD

## Policy
Agencies SHOULD only allow installation of custom applications approved by the agency.

- _Rationale:_ Allowing Teams integration with custom applications can expose the agency to potential vulnerabilities present in an application not managed by the agency. By allowing only specific applications approved by the agency and blocking all others, the agency can limit its exposure to custom application vulnerabilities.
- _Last modified:_ August 2026
- _Note:_ This policy applies to the Global (Org-wide default) policy, all custom policies if they exist, and the org-wide settings. Custom policies MAY be created to allow more flexibility for specific users. Custom apps may not be available in the Government Community Cloud (GCC), GCC High, and Department of Defense (DoD) regions.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-11
- _MITRE ATT&CK TTP Mapping:_
  - [T1195: Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/)
  - [T1528: Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)

## Resources
- [Use app permission policies to control user access to apps \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/teams-app-permission-policies)

- [Upload your app in Microsoft Teams \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/apps-upload)

## License Requirements
- N/A

## Implementation
To ensure users can only install custom apps approved by the agency:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **Teams apps** > **Manage apps**.

3.  In the upper right-hand corner select **Actions**.

4.  Select **Org-wide app settings**.

5.  Under the **Custom apps** section, ensure it is set to the **Off** position.

6.  Click **Save** (if applicable).

    **NOTE:** This will make all "Custom apps" in the application list available to "No one." If custom adjustments are needed, on an app by app basis, follow the remaining instructions below. Additionally, previously configured availability settings for individual apps may persist after changing the global toggle and should be reviewed to ensure they remain appropriate.

##### Optional:

7. Close the **Org-wide app settings** settings screen.

8. Select the individual app.

    **NOTE:** To filter out the application list so it is easier to see the relevant apps, click on the **Filter** icon to the left of the search bar. In this screen set **App type** to the **Custom apps**, then click **Apply** to save your choices. You can press **Add more** to consider other criteria, such as **App status** (Blocked, Unblocked).

9. Press the **Edit availability** button at the top of the app list, while the app is selected.

10. Ensure the correct app is reflecting on the edit screen and then change the value in the **Available to** dropdown box to the appropriate setting for your organization (**Everyone, Specific users or groups, or No one**).

11. Click **Apply** (if applicable).

12. Repeat steps 8 to 11 for each application.

# Appendix A - Custom Meeting Policies (Recordings)

If there is a legitimate business need, custom meeting policies can be defined with _specific_ users assigned to them for narrowly scoped purposes. For example, custom meeting policies can be configured for _specific_ users granting them permission to record meetings. To allow _specific_ users the ability to record meetings:

1.  Sign in to the **Microsoft Teams admin center**.

2.  Select **Meetings** > **Meeting policies**.

3.  Create a new policy by selecting the **Add** button. Give this new policy a name and an appropriate description (inclusion of the scoped users is recommended).

4.  Under the **Recording & transcription** section, set **Meeting recording** to the **On** position.

5.  Select **Save** (if applicable).

6.  After selecting **Save**, you're returned to the table displaying all of your tenant's policies. Select the checkbox on the row containing the new policy you just created, then select **Manage users** in the actions area above the table.

7.  On the **Manage users** screen, assign the users to this policy who need the ability to record meetings.

8.  Select **Apply**. Once saved, your custom policy will go into effect following a short delay.

# Appendix B - Legacy Policy Implementation (App Management)
