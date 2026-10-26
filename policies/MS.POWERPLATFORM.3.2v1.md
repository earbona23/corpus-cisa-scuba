# MS.POWERPLATFORM.3.2v1: An inbound/outbound connection allowlist SHOULD be configured.
Product: Power Platform · Baseline: powerplatform · Group: 3. Power Platform Tenant Isolation · Criticality: SHOULD

## Policy
An inbound/outbound connection allowlist SHOULD be configured.

- _Rationale:_ Depending on agency needs, an allowlist can be configured to allow cross-tenant collaboration via connectors.
- _Last modified:_ April 2026
- Note: The allowlist may be empty if the agency has no need for cross-tenant collaboration.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, SC-7(5)
- _MITRE ATT&CK TTP Mapping:_
  - None

## Resources
- [Enable tenant isolation and configure allowlist \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/cross-tenant-restrictions#enable-tenant-isolation-and-configure-allowlist)

## License Requirements
- N/A

## Implementation
1.  Follow steps one and two in the **MS.POWERPLATFORM.3.1v1 instructions** to
arrive at the "Tenant isolation" page.

2.  The tenant isolation exceptions can be configured by clicking **+ Add exceptions**
on the "Tenant isolation" page.

3.  Select the direction of the rule and add the tenant domain or ID to which the rule applies.

4.  If "tenant isolation" is switched to **Off**, these rules will not be enforced until "tenant
isolation" is turned **On**.
