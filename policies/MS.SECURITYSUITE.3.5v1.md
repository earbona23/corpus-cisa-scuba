# MS.SECURITYSUITE.3.5v1: The DLP policy SHOULD include an action to block access to sensitive information by restricted applications
Product: securitysuite · Baseline: securitysuite · Group: 3. Data Loss Prevention · Criticality: SHOULD

## Policy
The DLP policy SHOULD include an action to block access to sensitive information by restricted applications
and unwanted Bluetooth applications.

- _Rationale:_ Some applications may inappropriately share accessed files or not conform to agency policies
               for access to sensitive information. Defining a DLP policy with an action to block
               access from restricted applications and unwanted Bluetooth applications prevents unauthorized
               disclosure by those programs.
- _Last modified:_ March 2026
- _Note:_
  - This action can only be included if at least one device is onboarded
    to the agency tenant. Otherwise, the option to block restricted applications will
    not be available.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-19a
- _MITRE ATT&CK TTP Mapping:_
  - [T1565: Data Manipulation](https://attack.mitre.org/techniques/T1565/)
  - [T1485: Data Destruction](https://attack.mitre.org/techniques/T1485/)
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)
  - [T1486: Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/)

## Resources
- [Plan for data loss prevention (DLP) \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp?view=o365-worldwide)

- [Data loss prevention in Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/security-and-compliance/data-loss-prevention/data-loss-prevention)

- [Personally identifiable information (PII) \|
  NIST](https://csrc.nist.gov/glossary/term/personally_identifiable_information#:~:text=NISTIR%208259,2%20under%20PII%20from%20EGovAct)

- [Sensitive information \|
  NIST](https://csrc.nist.gov/glossary/term/sensitive_information)

- [Get started with Endpoint data loss prevention - Microsoft Purview
  (compliance) \| Microsoft Learn](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started?view=o365-worldwide)

## License Requirements
- DLP for Teams requires an E5 or G5 license. See [Microsoft Purview Data Loss Prevention: Data Loss Prevention for Teams \| Microsoft
  Learn](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#microsoft-purview-data-loss-prevention-data-loss-prevention-dlp-for-teams)
  for more information. However, this requirement can also be met through a third-party solution. If a third-party solution is used, then an E5 or G5 license is not required for the respective policies.

- DLP for Endpoint, needed for MS.SECURITYSUITE.3.5v1, requires an E5 or G5 license. See [Get started with
  Endpoint data loss prevention - Microsoft Purview (compliance) \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started?view=o365-worldwide)
  for more information. However, this requirement can also be met through a compliant third-party solution. If a third-party solution is used, then an E5 or G5 license is not required for the respective policies.

## Implementation
These implementation steps are only applicable if at least one device has been onboarded with
Defender for Endpoint.

1. Sign in to the **Microsoft Purview portal**.
2. Under **Settings**, select **Data Loss Prevention**.
3. (Optional) Select **Restricted apps and app groups**. Add or edit restricted applications per agency
  discretion.
4. Select **Unallowed Bluetooth apps**, then click **Add or edit unallowed Bluetooth apps**.
5. Ensure **Include Bluetooth apps recommended by Microsoft** is **On**.
6. (Optional) Add other apps to restrict, per agency discretion.
7. Click **Save**.
8. Return to the main menu. Under **Solutions**, select **Data Loss Prevention**.
9. Select **Policies** from the top of the page.
10. Find the custom DLP policy configured under
   [MS.SECURITYSUITE.3.1v1 Instructions](#mssecuritysuite31v1-instructions) in the list
   and click the Policy name to select.
11. Select **Edit policy**.
12. Click **Next** on each page in the policy wizard until you reach the
   **Advanced DLP rules page**.
13. Select the relevant rule and click the pencil icon to edit it.
14. Under **Actions**, click **Add an action**.
15. Choose **Audit or restrict activities on device**.
16. Under **File activities for all apps**, select
    **Apply restrictions to specific activity**.
17. Check the box next to **Copy or move using unallowed Bluetooth app**
    and set its action to **Block**.
18. Under **App access restrictions**, check the **Access by restricted apps** box
   and set the action drop-down to **Block**.
19. Click **Save** to save the changes.
20. Click **Next** on each page until reaching the
    **Review your policy and create it** page.
21. Review the policy and click **Submit** to complete the policy changes.
