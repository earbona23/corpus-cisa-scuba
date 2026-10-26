# MS.EXO.5.1v1: SMTP AUTH SHALL be disabled.
Product: Exchange Online · Baseline: exo · Group: 5. Simple Mail Transfer Protocol Authentication · Criticality: SHALL

## Policy
SMTP AUTH SHALL be disabled.

- _Rationale:_ SMTP AUTH is not used or needed by modern email clients.
Therefore, disabling it as the global default conforms to the principle of
least functionality.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ CM-7
- _MITRE ATT&CK TTP Mapping:_
  - None

## Resources
- [Enable or disable authenticated client SMTP submission (SMTP AUTH) in
  Exchange Online \| Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission)

## License Requirements
- N/A

## Implementation
To disable SMTP AUTH for the organization:

1. Sign in to the **Exchange admin center**.

2. On the left-hand pane, select **Settings**. Then select **Mail flow** from the settings list.

3. Make sure the setting **Turn off SMTP AUTH protocol for your organization** is checked.
