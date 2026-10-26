# MS.AAD.5.1v1: Only administrators SHALL be allowed to register applications.
Product: Microsoft Entra ID · Baseline: aad · Group: 5. Application Registration and Consent · Criticality: SHALL

## Policy
Only administrators SHALL be allowed to register applications.

- _Rationale:_ Application access for the tenant presents a heightened security risk compared to interactive user access because applications are typically not subject to critical security protections, such as MFA policies. Reduce risk of unauthorized users installing malicious applications into the tenant by ensuring that only specific privileged users can register applications.
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
1.  In the **Microsoft Entra admin center**, select **Users**.

2. Select **User settings**.

3. For **Users can register applications**, select **No**.

4. Click **Save**.
