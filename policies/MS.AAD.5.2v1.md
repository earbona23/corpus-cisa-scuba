# MS.AAD.5.2v1: User consent to applications SHALL be restricted.
Product: Microsoft Entra ID · Baseline: aad · Group: 5. Application Registration and Consent · Criticality: SHALL

## Policy
User consent to applications SHALL be restricted.

- _Rationale:_ Restricting user consent for applications reduces risk of users giving insecure applications access to their data via [consent grant attacks](https://learn.microsoft.com/en-us/defender-office-365/detect-and-remediate-illicit-consent-grants?view=o365-worldwide).
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(10), CM-5
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
There are a couple of configuration options to restrict user consent. Each option is described below, followed by its respective instructions.

- **Option 1** - Most restrictive - Do not allow user consent for applications. An administrator is required to consent for all applications. Users can submit requests to use an application via the admin consent workflow but they cannot perform the consent themselves.
- **Option 2** - More flexible - Allow users to consent to applications from Microsoft verified publishers that use low-risk permissions. When selecting this option, an administrator must configure a set of permissions considered low risk in the **Consent and permissions** > **Permission classifications** page in the Microsoft Entra admin center.

**Option 1**. Do not allow user consent.

1.  In the **Microsoft Entra admin center**, select **Enterprise apps**.

2. Under **Security**, select **Consent and permissions**. Then select **User consent settings**.

3. Under **User consent for applications**, select **Do not allow user consent**.

4. Click **Save**.

**Option 2**. Allow restricted user consent.

1.  In the **Microsoft Entra admin center**, select **Enterprise apps**.

2. Under **Security**, select **Consent and permissions**. Then select **User consent settings**.

3. Under **User consent for applications**, select **Allow user consent for apps from verified publishers, for selected permissions**.

4. Click **Save**.

5. In the page navigation menu, select **Permission classifications**.

6. Click on the **Low** tab.

7. [Add a list of low risk application permissions that users will be able to consent to](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-permission-classifications). We recommend only including permissions that provide minimal access to a user's data. For a reference of permissions that are considered risky and should be avoided [go to this JSON file and examine the permissions listed](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/schemas/RiskyAppPermissions.json) in the **Delegated** sections under Microsoft Graph and other apps.
