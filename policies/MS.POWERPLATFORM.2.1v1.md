# MS.POWERPLATFORM.2.1v1: A DLP policy SHALL be created to restrict connector access in the default Power Platform environment.
Product: Power Platform · Baseline: powerplatform · Group: 2. Power Platform Data Loss Prevention Policies · Criticality: SHALL

## Policy
A DLP policy SHALL be created to restrict connector access in the default Power Platform environment.

- _Rationale:_ All tenant users have access to the default Power Platform environment. Those users may inadvertently use connectors that share sensitive information with others who should not have access. Users requiring Power Apps should be directed to conduct development in other Power Platform environments with DLP connector policies customized to suit the user's needs, while also maintaining the agency's security posture.
- _Last Modified:_ June 2023
- _Note:_ The following connectors drive core Power Platform functionality and enable core Office customization scenarios: Approvals, Dynamics 365 Customer Voice, Excel Online (Business), Microsoft Dataverse, Microsoft Dataverse (legacy), Microsoft Teams, Microsoft To-Do (Business), Office 365 Groups, Office 365 Outlook, Office 365 Users, OneDrive for Business, OneNote (Business), Planner, Power Apps Notification, Power BI, SharePoint, Shifts for Microsoft Teams, and Yammer. As such, these connectors remain non-blockable to maintain core user scenario functions.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-7(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)

## Resources
- [Data Policies for Power Automate and Power Apps \| Digital
  Transformation Agency of
  Australia](https://desktop.gov.au/blueprint/office-365.html#power-apps-and-power-automate)

- [Create a data loss prevention (DLP) policy \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/create-dlp-policy)

- [DLP connector classification \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/dlp-connector-classification?source=recommendations)

- [DLP for custom connectors \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity?WT.mc_id=ppac_inproduct_datapol)

## License Requirements
- N/A

## Implementation
1.  Sign in to your tenant environment's respective [Power Platform admin
    center](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-us-government#power-apps-us-government-service-urls).

2.  On the left pane, select **Security** -\> **Data and privacy.**

3.  Select **Data policy,** then select the **+ New Policy** icon to create a new policy.

4.  Give the policy a suitable agency name and click **Next.**

5.  In the **Prebuilt connectors** section, search for and select the connectors currently in the **Non-business | default** tab that contain sensitive data which could be utilized to create flows and applications.

6.  Click **Move to Business.** Connectors added to this group cannot share data with connectors in other groups because connectors can only reside in one data group at a time.

7.  If necessary (and possible) for the connector, click **Configure connector** at the top of the screen to change connector permissions. This allows the agency to allow and block certain connector actions for additional customization.

8.  For the default environment, move all other connectors to the **Blocked** category. For non-blockable connectors noted above, the "Block" action will be grayed out and a warning will appear.

9.  At the bottom of the screen, select **Next** to move on.

10.  Add a custom connector pattern. Custom connectors allow administrators to specify an ordered list of "Allow" and "Deny" URL patterns for custom connectors. View [DLP for custom connectors \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity?WT.mc_id=ppac_inproduct_datapol) for more information.

11.  Click **Next**.

12.  In the **Scope** section for the default environment, select **Add multiple environments**, then click **Next**.

13.  Select the default environment, then select the **+ Add to policy** button at the top of the screen. Then select **Next**.

14. Select **Next** and **Create policy** to finish.
