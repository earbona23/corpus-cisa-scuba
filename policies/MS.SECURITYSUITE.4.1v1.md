# MS.SECURITYSUITE.4.1v1: At a minimum, the following alerts SHALL be enabled:
Product: securitysuite · Baseline: securitysuite · Group: 4. Alerts · Criticality: SHALL

## Policy
At a minimum, the following alerts SHALL be enabled:

  a. **Suspicious email sending patterns detected.**

  b. **Suspicious Connector Activity.**

  c. **Suspicious Email Forwarding Activity.**

  d. **Messages have been delayed.**

  e. **Tenant restricted from sending unprovisioned email.**

  f. **Tenant restricted from sending email.**

  g. **A potentially malicious URL click was detected.**

- _Rationale:_ Potentially malicious or service-impacting events may go undetected without a means of detecting these events. Setting up a mechanism to alert administrators to the list of events linked above draws attention to the events and can help minimize user/agency impact.
- _Last modified:_ March 2026
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-4(5)
- _MITRE ATT&CK TTP Mapping:_
  - [T1562: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
    - [T1562.006: Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)

## Resources
- [Alert policies in Microsoft 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/purview/alert-policies?view=o365-worldwide)

## License Requirements
- N/A

## Implementation
1. Sign in to **Microsoft 365 Defender**.

2. Under **Email & collaboration**, select **Policies & rules**.

3. Select **Alert policy**.

4. Select the checkbox next to each alert to enable, as determined by the
   agency and at a minimum the following:

   a. **Suspicious email sending patterns detected.**

   b. **Suspicious connector activity.**

   c. **Suspicious Email Forwarding Activity.**

   d. **Messages have been delayed.**

   e. **Tenant restricted from sending unprovisioned email.**

   f. **Tenant restricted from sending email.**

   g. **A potentially malicious URL click was detected.**

5. Click the pencil icon from the top menu.

6. Select the **Enable selected policies** action from the **Bulk actions**
   menu.
