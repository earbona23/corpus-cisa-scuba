# MS.EXO.4.1v1: A DMARC policy SHALL be published for every second-level domain.
Product: Exchange Online · Baseline: exo · Group: 4. Domain-Based Message Authentication, Reporting, and Conformance (DMARC) · Criticality: SHALL

## Policy
A DMARC policy SHALL be published for every second-level domain.

- _Rationale:_ Without a DMARC policy available for each domain, recipients
may improperly handle SPF and DKIM failures. This mishandling could allow spoofed
emails to reach end users' mailboxes. Publishing DMARC records at the
second-level domain protects the second-level domains and all subdomains.
- _Last modified:_ June 2023
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-8
- _MITRE ATT&CK TTP Mapping:_
  - [T1598: Phishing for Information](https://attack.mitre.org/techniques/T1598/)
  - [T1656: Impersonation](https://attack.mitre.org/techniques/T1656/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

## Resources
- [Binding Operational Directive 18-01 - Enhance Email and Web Security
  \| DHS](https://cyber.dhs.gov/bod/18-01/)

- [Trustworthy Email \| NIST 800-177 Rev.
  1](https://csrc.nist.gov/publications/detail/sp/800-177/rev-1/final)

- [Domain-based Message Authentication, Reporting, and Conformance
  (DMARC) \| RFC 7489](https://datatracker.ietf.org/doc/html/rfc7489)

- [Best practices for implementing DMARC in Office 365 \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide#best-practices-for-implementing-dmarc-in-microsoft-365)

- [How Office 365 handles outbound email that fails DMARC \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide#how-microsoft-365-handles-inbound-email-that-fails-dmarc)

## License Requirements
- N/A

## Implementation
DMARC is not configured through the Exchange admin center, but rather via
DNS records hosted by the agency's domain. As such, implementation varies
depending on how an agency manages its DNS records. See [Form the DMARC TXT record for your domain \| Microsoft
Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide#step-4-form-the-dmarc-txt-record-for-your-domain)
for Microsoft guidance.

A DMARC record published at the second-level domain will protect all subdomains.
In other words, a DMARC record published for `example.com` will protect both
`a.example.com` and `b.example.com`, but a separate record would need to be
published for `c.example.gov`.

To test your DMARC configuration, consider using one of many publicly available
web-based tools. Additionally, DMARC records can be requested using the
PowerShell tool `Resolve-DnsName`. For example:

```
Resolve-DnsName _dmarc.example.com txt
```

If DMARC is configured, a response resembling `v=DMARC1; p=reject; pct=100; rua=mailto:reports@dmarc.cyber.dhs.gov, mailto:reports@example.com; ruf=mailto:reports@example.com`
will be returned. Though, by necessity, the contents of the record will vary
by agency. In this example, the policy indicates all emails failing the
SPF/DKIM checks are to be rejected and aggregate reports sent to
reports@dmarc.cyber.dhs.gov and reports@example.com. Failure reports will be
sent to reports@example.com.
