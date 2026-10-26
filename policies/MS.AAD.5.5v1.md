# MS.AAD.5.5v1: Application password addition SHOULD be blocked.
Product: Microsoft Entra ID · Baseline: aad · Group: 5. Application Registration and Consent · Criticality: SHOULD

## Policy
Application password addition SHOULD be blocked.

- _Rationale:_ Applications that use client secrets might store them in configuration files, hardcode them in scripts, or risk exposure in other ways. The complexities of secret management make client secrets susceptible to leaks and attractive to attackers. Blocking password addition forces the use of more secure certificate-based authentication.
- _Last modified:_ April 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-5
- _MITRE ATT&CK TTP Mapping:_
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.001: Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/)
  - [T1528: Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)

## Resources
- [Restrict Application Registration for Non-Privileged Users](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-register-applications.html)

- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)
- [Configure restrictions on how applications can be configured](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-app-management-policies)
- [Tutorial: Enforce secret and certificate standards using application management policies](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards)
- [Application Management Policies API Overview](https://learn.microsoft.com/en-us/graph/api/resources/applicationauthenticationmethodpolicy)

## License Requirements
- N/A

## Implementation
1. In the **Microsoft Entra admin center**, select **Enterprise apps**.

2. Under **Security**, select **Application policies**.

3. Select **Block password addition**.

4. Set status to **On**. Ensure **Applies to** is set to **All applications**.

5. Leave **Only apply to apps created after** blank. Setting a date allows apps created before that date to bypass this restriction.

6. Click **Save**.
