# MS.SECURITYSUITE.3.1v1: A DLP policy SHALL be configured to protect PII and sensitive information, as defined by the agency, blocking at a minimum: credit card numbers, U.S. Individual Taxpayer Identification Numbers (ITIN), and U.S. Social Security numbers (SSN).
Product: securitysuite · Baseline: securitysuite · Group: 3. Data Loss Prevention · Criticality: SHALL

## Policy
A DLP policy SHALL be configured to protect PII and sensitive information, as defined by the agency, blocking at a minimum: credit card numbers, U.S. Individual Taxpayer Identification Numbers (ITIN), and U.S. Social Security numbers (SSN).

- _Rationale:_ Users may inadvertently share sensitive information with
               others who should not have access to it. DLP policies
               provide a way for agencies to detect and prevent
               unauthorized disclosures.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-7(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1530: Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)
  - [T1213: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)

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
DLP is _not_ covered by the preset policies, so these steps need to be taken even if the standard
or strict policies are used.

Since the steps for MS.SECURITYSUITE.3.1v1, MS.SECURITYSUITE.3.2v1, MS.SECURITYSUITE.3.3v1, and
MS.SECURITYSUITE.3.4v1 share similarities, steps for all of these policies are included in
this section. Steps that do not strictly apply to MS.SECURITYSUITE.3.1v1 are followed by the
applicable SCuBA policy in parentheses.

1. Sign in to the **Microsoft Purview portal**.

2. Under the **Solutions** section on the left-hand menu, select **Data loss
   prevention**.

3. Select **Policies** from the top of the page.

4. Select **Create policy**.

5. From the **Categories** list, select **Custom**.

6. From the **Regulations** list, select **Custom policy**, then click
   **Next**.

7. Edit the name and description of the policy if desired, then click
   **Next**.

8. Under **Assign admin units**, ensure **Admin units** is set to **Full directory** by default, then click **Next**.

9. Under **Choose where to apply the policy**, set **Status** to **On**
   for at least the Exchange email, OneDrive accounts, SharePoint
   sites, Teams chat and channel messages, and Devices locations. Then
   click **Next**. (_MS.SECURITYSUITE.3.2v1_)

10. Under **Define policy settings**, select **Create or customize advanced
   DLP rules**, then click **Next**.

11. Click **Create rule**. Assign the rule an appropriate name and
   description.

12. Click **Add condition**, then click **Content contains**.

13. Click **Add**, then click **Sensitive info types**.

14. Add information types that protect information sensitive to the agency.
    At a minimum, the agency should protect:

    - Credit card numbers
    - U.S. Individual Taxpayer Identification Numbers (ITIN)
    - U.S. Social Security Numbers (SSN)
    - All agency-defined PII and sensitive information

15. Click **Add**.

16. Under **Actions**, click **Add an action**.

17. Check **Restrict Access or encrypt the content in Microsoft 365
    locations**.

18. Under this action, select **Block everyone**. (_MS.SECURITYSUITE.3.3v1_)

19. Under **User notifications**, turn on **Use notifications to inform your users and help educate them on the proper use of sensitive info**. (_MS.SECURITYSUITE.3.4v1_)

20. Under **Microsoft 365 services** if using a GCC environment or under **Microsoft 365 files and Microsoft Fabric items** if using a Commercial environment, a section that appears after user notifications are turned on, check the box next to **Notify users in Office 365 service with a policy tip or email notifications**. (_MS.SECURITYSUITE.3.4v1_)

21. Click **Save**, then click **Next**.

22. Select **Turn the policy on immediately**, then click **Next**.

23. Click **Submit**.
