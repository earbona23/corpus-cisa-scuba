# MS.AAD.5.6v1: Application password lifetime SHOULD be restricted to 180 days or less.
Product: Microsoft Entra ID · Baseline: aad · Group: 5. Application Registration and Consent · Criticality: SHOULD

## Policy
Application password lifetime SHOULD be restricted to 180 days or less.

- _Rationale:_ Long-lived credentials increase the window of opportunity for attackers to exploit compromised secrets. Enforcing a maximum password lifetime of 180 days ensures regular credential rotation, reducing the impact of credential theft and improving overall security hygiene.
- _Last modified:_ April 2026
- _Note:_ Due to how Microsoft Entra ID evaluates the MaxLifetime restriction using "less than" (not "less than or equal to"), the portal setting must be configured to **181 days** to enforce the requirement of "180 days or less."
- _Note:_ This policy applies only if password credentials are permitted. Microsoft and CISA recommend blocking password addition entirely (MS.AAD.5.5v1) as the preferred approach.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-5, SC-12
- _MITRE ATT&CK TTP Mapping:_
  - [T1552: Unsecured Credentials](https://attack.mitre.org/techniques/T1552/)
    - [T1552.001: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/)

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

3. Select **Restrict max password lifetime**.

4. Set status to **On**. Set maximum lifetime to **181 days**. Ensure **Applies to** is set to **All applications**.

5. Leave **Only apply to apps created after** blank. Setting a date allows apps created before that date to bypass this restriction.

6. Click **Save**.
