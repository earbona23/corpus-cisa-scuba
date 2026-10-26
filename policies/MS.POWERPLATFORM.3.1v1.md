# MS.POWERPLATFORM.3.1v1: Power Platform tenant isolation SHALL be enabled.
Product: Power Platform · Baseline: powerplatform · Group: 3. Power Platform Tenant Isolation · Criticality: SHALL

## Policy
Power Platform tenant isolation SHALL be enabled.

- _Rationale:_ Enabling Power Platform tenant isolation provides an additional tenant isolation control on top of Microsoft Entra ID tenant isolation, specifically for Power Platform applications. This control helps prevent accidental or malicious cross-tenant information sharing.
- _Last modified:_ April 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, SC-7(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.004: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)
  - [T1190: Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

## Resources
- [Enable tenant isolation and configure allowlist \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/cross-tenant-restrictions#enable-tenant-isolation-and-configure-allowlist)

## License Requirements
- N/A

## Implementation
1.  Sign in to your tenant environment's respective [Power Platform admin
    center](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-us-government#power-apps-us-government-service-urls).

2.  On the left pane, select **Policies -\> Tenant isolation**.

3.  Set the slider labeled **Restrict cross-tenant connections** and move it to **On,** then click **Save**
    at the bottom of the screen.
