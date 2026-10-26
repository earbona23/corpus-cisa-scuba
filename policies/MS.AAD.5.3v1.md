# MS.AAD.5.3v1: An administrative consent workflow SHALL be configured for applications.
Product: Microsoft Entra ID · Baseline: aad · Group: 5. Application Registration and Consent · Criticality: SHALL

## Policy
An administrative consent workflow SHALL be configured for applications.

- _Rationale:_ Configuring an administrative consent workflow reduces the risk of the previous policy by setting up a process for users to securely request access to applications necessary for business purposes. Administrators can review the permissions requested by new applications and approve or deny access based on a risk assessment.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-4
- _MITRE ATT&CK TTP Mapping:_
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.001: Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/)
    - [T1098.003: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)

## Resources
- [Restrict Application Registration for Non-Privileged Users](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-register-applications.html)

- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)
- [Configure restrictions on how applications can be configured](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-app-management-policies)
- [Tutorial: Enforce secret and certificate standards using application management policies](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards)
- [Application Management Policies API Overview](https://learn.microsoft.com/en-us/graph/api/resources/applicationauthenticationmethodpolicy)

## License Requirements
- N/A

## Implementation
1.  In the **Microsoft Entra admin center**, create a new Microsoft Entra ID Group that contains administrative users responsible for reviewing and adjudicating application consent requests. Group members will be notified when users request consent for new applications.

2. Then, in **Microsoft Entra admin center** under **Applications**, select **Enterprise apps**.

3. Under **Security**, select **Consent and permissions**. Then select **Admin consent settings**.

4. Under **Admin consent requests**, navigate to **Users can request admin consent to apps they are unable to consent to** and select **Yes**.

5. Under **Who can review admin consent requests**, select **+ Add groups** and select the group responsible for reviewing and adjudicating applications requests (created in step one, above).

6. Click **Save**.
