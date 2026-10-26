# MS.AAD.5.7v1: Application certificate lifetime SHOULD be restricted to 365 days or less.
Product: Microsoft Entra ID · Baseline: aad · Group: 5. Application Registration and Consent · Criticality: SHOULD

## Policy
Application certificate lifetime SHOULD be restricted to 365 days or less.

- _Rationale:_ While certificates provide more secure authentication than passwords, long-lived certificates can still be compromised. Limiting certificate lifetime to 365 days reduces the risk of exploitation while balancing operational overhead. Regular certificate rotation is a security best practice that minimizes exposure from compromised keys.
- _Note:_ Due to how Microsoft Entra ID evaluates the MaxLifetime restriction using "less than" (not "less than or equal to"), the portal setting must be configured to **366 days** to enforce the requirement of "365 days or less."
- _Last modified:_ April 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-12, IA-5
- _MITRE ATT&CK TTP Mapping:_
  - [T1649: Steal or Forge Authentication Certificates](https://attack.mitre.org/techniques/T1649/)

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

3. Select **Restrict max certificate lifetime**.

4. Set status to **On**. Set maximum lifetime to **366 days**. Ensure **Applies to** is set to **All applications**.

5. Leave **Only apply to apps created after** blank. Setting a date allows apps created before that date to bypass this restriction.

6. Click **Save**.
