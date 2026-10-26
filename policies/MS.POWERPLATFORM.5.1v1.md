# MS.POWERPLATFORM.5.1v1: The ability to create Power Pages sites SHOULD be restricted to administrators.
Product: Power Platform · Baseline: powerplatform · Group: 5. Power Pages Creation · Criticality: SHOULD

## Policy
The ability to create Power Pages sites SHOULD be restricted to administrators.

- _Rationale:_ Users may unintentionally misconfigure their Power Pages, exposing sensitive information or leaving the website in a vulnerable state.
- _Last Modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1190: Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

## Resources
- [Control Portal Creation \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-apps/maker/portals/control-portal-creation)

## License Requirements
- N/A

## Implementation
1.  This setting can currently only be enabled through the [Power Apps PowerShell modules](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-powershell#installation).

2. After installing the Power Apps PowerShell modules, run `Add-PowerAppsAccount -Endpoint $YourTenantsEndpoint` to authenticate to your tenant's Power Platform.
Discover the valid endpoint parameter [here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powerapps.administration.powershell/add-powerappsaccount?view=pa-ps-latest#-endpoint). Commercial tenants use `-Endpoint prod`, while GCC tenants use `-Endpoint usgov`.

3. Run the following PowerShell command to disable the creation of Power Pages sites by non-administrative users:

    ```
    Set-TenantSettings -RequestBody @{ “disablePortalsCreationByNonAdminUsers” = $true }
    ```
