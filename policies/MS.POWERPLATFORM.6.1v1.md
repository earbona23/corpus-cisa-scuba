# MS.POWERPLATFORM.6.1v1: The "Share with everyone" feature SHOULD be disabled.
Product: Power Platform · Baseline: powerplatform · Group: 6. Power Apps Sharing Controls · Criticality: SHOULD

## Policy
The "Share with everyone" feature SHOULD be disabled.

- _Rationale:_ Disabling the "Share with everyone" feature prevents tenant-wide application exposure with unintended users. If enabled, this setting grants application access to the "Everyone" group for an organization. Its membership contains all users present in the directory, including B2B guest accounts and internal members. The "Everyone" group is not a standard Microsoft Entra ID security group and can't be edited or viewed, complicating auditing and access governance. The configuration setting is disabled by default. However, this is a defense-in-depth policy to protect against misconfigurations or malicious actors.
- _Last Modified:_ October 2025
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-6(5), AC-6(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.004: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)
  - [T1098: Account Manipulation](https://attack.mitre.org/techniques/T1098/)
    - [T1098.007: Additional Local or Domain Groups](https://attack.mitre.org/techniques/T1098/007/)

## Resources
- [Limit Sharing with Everyone \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/secure-default-environment#limit-sharing-with-everyone)

## License Requirements
- N/A

## Implementation
1.  This setting can currently only be enabled through the [Power Apps PowerShell modules](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-powershell#installation).

2. After installing the Power Apps PowerShell modules, run `Add-PowerAppsAccount -Endpoint $YourTenantsEndpoint` to authenticate to your tenant's Power Platform.
Discover the valid endpoint parameter [here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powerapps.administration.powershell/add-powerappsaccount?view=pa-ps-latest#-endpoint). Commercial tenants use `-Endpoint prod`, while GCC tenants use `-Endpoint usgov`.

3. Run the following PowerShell commands to get the settings object and set the variable `disableShareWithEveryone` to `$true`.

    ```
    $tenantSettings = Get-TenantSettings
    $tenantSettings.powerPlatform.powerApps.disableShareWithEveryone = $true
    Set-TenantSettings $tenantSettings
    ```

**`TLP:CLEAR`**
