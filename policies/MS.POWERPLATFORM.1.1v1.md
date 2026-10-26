# MS.POWERPLATFORM.1.1v1: The ability to create production and sandbox environments SHALL be restricted to administrators.
Product: Power Platform · Baseline: powerplatform · Group: 1. Creation of Power Platform Environments · Criticality: SHALL

## Policy
The ability to create production and sandbox environments SHALL be restricted to administrators.

- _Rationale:_ Users creating new Power Platform environments may inadvertently bypass data loss prevention (DLP) policy settings or misconfigure their environment's security settings.
- _Last Modified:_ April 2026
- Note: This control restricts the ability to create environments to users with Global administrator, Dynamics 365 service administrator, Power Platform service administrator, or Delegated administrator roles.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)

## Resources
- [Control who can create and manage environments in the Power Platform
  admin center \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/control-environment-creation)

- [Power Platform \| Digital Transformation Agency of
  Australia](https://desktop.gov.au/blueprint/office-365.html#power-platform)

- [Microsoft Power Apps Documentation \| Power
  Apps](https://learn.microsoft.com/en-us/power-apps/)

## License Requirements
- N/A

## Implementation
1.  Sign in to your tenant environment's respective [Power Platform admin
    center](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-us-government#power-apps-us-government-service-urls).

2.  In the upper-right corner of the Microsoft Power Platform site,
    select the **Gear icon** (Settings icon).

3.  Select **Power Platform settings**.

4.  Under **Production environment assignments**, select
    **Only specific admins.**
