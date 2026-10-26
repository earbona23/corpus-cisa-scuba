# MS.AAD.6.1v1: User passwords SHALL NOT expire.
Product: Microsoft Entra ID · Baseline: aad · Group: 6. Passwords · Criticality: SHALL

## Policy
User passwords SHALL NOT expire.

- _Rationale:_ The National Institute of Standards and Technology (NIST), OMB, and Microsoft have published guidance indicating mandated periodic password changes make user accounts less secure. For example, OMB-22-09 states, "Password policies must not require use of special characters or regular rotation."
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ IA-5(1)
- _MITRE ATT&CK TTP Mapping:_
  - None

## Resources
- [Password expiration requirements for users](https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations?view=o365-worldwide#password-expiration-requirements-for-users)

- [passwordValidityPeriodInDays property](https://learn.microsoft.com/en-us/graph/api/resources/domain?view=graph-rest-1.0#properties)

- [Eliminate bad passwords using Microsoft Entra Password Protection](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-password-ban-bad)

- [NIST Special Publication 800-63B - Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)

## License Requirements
- N/A

## Implementation
> **Note:** Tenants created after October 2021 have password expiration disabled by default (`passwordValidityPeriodInDays = null`), which Microsoft treats as equivalent to "never expire." Tenants created before October 2021, or any tenant where the policy was explicitly configured and then reverted, will show `2147483647` (INT_MAX). ScubaGear treats both values as compliant. The M365 admin center password expiration checkbox applies to all managed domains in the tenant. If a tenant has **multiple root domains**, use the PowerShell in Step 2 to audit all of them and remediate any that have a finite expiration period set.

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) and [configure the **Password expiration policy** to **Set passwords to never expire**](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/set-password-expiration-policy?view=o365-worldwide#set-password-expiration-policy).

2. Optionally, verify and remediate all root domains via PowerShell. This is useful if any domain had a finite expiration configured explicitly. This uses `Invoke-MgGraphRequest`, which is included with the `Microsoft.Graph.Authentication` module already required by ScubaGear. To audit only, connect with `Domain.Read.All`. To remediate, use `Domain.ReadWrite.All`.

  ```powershell
  Connect-MgGraph -Scopes "Domain.ReadWrite.All" # or alternatively "Domain.Read.All" for determining which domains are in a non-compliant state.

  $NonCompliantDomains = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/domains").value | Where-Object {
    $_.isRoot -and $_.isVerified -and
    $null -ne $_.passwordValidityPeriodInDays -and
    $_.passwordValidityPeriodInDays -ne [int32]::MaxValue
  }

  Write-Host $NonCompliantDomains | Format-List

  # Remediate each non-compliant domain
  Invoke-MgGraphRequest -Method PATCH -Uri "https://graph.microsoft.com/v1.0/domains/example.com" `
    -Body @{ passwordValidityPeriodInDays = [int32]::MaxValue }

  # Verify domain configurations
  $AllDomains = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/domains").value | Where-Object {
    $_.isRoot -and $_.isVerified
  }

  Write-Host "All current domain password expiration policies"
  foreach ($Domain in $AllDomains) {
    Write-Host "Domain passwordValidityPeriodInDays: $($Domain.id) $($Domain.passwordValidityPeriodInDays)"
  }
  ```
