# MS.POWERBI.6.1v1: Python and R interactions SHOULD be disabled.
Product: Power BI · Baseline: powerbi · Group: 6. Python and R Visual Sharing · Criticality: SHOULD

## Policy
Python and R interactions SHOULD be disabled.

- _Rationale:_ External code poses a security and privacy risk as there are limited ways to regulate use of data or integrations. Disabling this feature reduces the risk of a data leak or malicious threat activity.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7, SI-3
- _MITRE ATT&CK TTP Mapping:_
  - [T1059: Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
    - [T1059.009: Cloud API](https://attack.mitre.org/techniques/T1059/009/)
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)

## Resources
- [Create Power BI visuals with Python \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-visuals)

## License Requirements
- N/A

## Implementation
1. Navigate to the **Power BI admin portal**.

2. Click on **Tenant settings**.

3. Scroll to **R and Python visuals settings**.

4. Click on **Interact with and share R and Python visuals** and set it to **Disabled**.
