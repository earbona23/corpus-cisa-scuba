# MS.EXO.1.1v2: Automatic forwarding to external domains SHALL be disabled.
Product: Exchange Online · Baseline: exo · Group: 1. Automatic Forwarding to External Domains · Criticality: SHALL

## Policy
Automatic forwarding to external domains SHALL be disabled.

- _Rationale:_ Adversaries can use automatic forwarding to gain
persistent access to a victim's email. Disabling forwarding to
external domains prevents this technique when the adversary is
external to the organization but does not impede legitimate
internal forwarding.
- _Last modified:_ March 2025
- _Note:_ Automatic forwarding MAY be enabled with specific, agency-approved domains.
There may be cases where an external domain is operationally needed and has an acceptable
degree of risk, e.g., a domain controlled by the same agency that hasn't been added
as an accepted domain in M365.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-4
- _MITRE ATT&CK TTP Mapping:_
  - [T1567: Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567/)
  - [T1048: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)
    - [T1566.001: Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)

## Resources
- [Reducing or increasing information flow to another company \|
  Microsoft
  Learn](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/remote-domains/remote-domains#reducing-or-increasing-information-flow-to-another-company)

## License Requirements
- N/A

## Implementation
To disable automatic forwarding to external domains:

1.  Sign in to the **Exchange admin center**.

2.  Select **Mail flow**, then select **Remote domains**.

3.  Select **Default**.

4.  Under **Email reply types**, select **Edit reply types**.

5.  Clear the checkbox next to **Allow automatic forwarding**, then
    click **Save**.

6.  Return to **Remote domains** and review each
    additional remote domain in the list, ensuring that automatic forwarding
    is only allowed for approved domains.
