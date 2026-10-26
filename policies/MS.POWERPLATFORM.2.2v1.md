# MS.POWERPLATFORM.2.2v1: Non-default environments SHOULD have at least one DLP policy.
Product: Power Platform · Baseline: powerplatform · Group: 2. Power Platform Data Loss Prevention Policies · Criticality: SHOULD

## Policy
Non-default environments SHOULD have at least one DLP policy.

- _Rationale:_ Users may inadvertently use connectors that share sensitive information with others who should not have access. DLP policies enable agencies to detect and prevent unauthorized disclosures.
- _Last Modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SC-7(10)
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)

## Resources
- [Data Policies for Power Automate and Power Apps \| Digital
  Transformation Agency of
  Australia](https://desktop.gov.au/blueprint/office-365.html#power-apps-and-power-automate)

- [Create a data loss prevention (DLP) policy \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/create-dlp-policy)

- [DLP connector classification \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/dlp-connector-classification?source=recommendations)

- [DLP for custom connectors \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity?WT.mc_id=ppac_inproduct_datapol)

## License Requirements
- N/A

## Implementation
1.  Repeat steps one through 11 in the MS.POWERPLATFORM.2.1v1 instructions.

2.  In the **Scope** section for the default environment, select **Add multiple environments** and select the non-default environments that you wish to enforce a DLP policy upon. If you wish to apply the DLP policy for all environments, including environments created in the future, select **Add all environments**.

3.  Select **Next** and **Create policy** to finish.
