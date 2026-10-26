# MS.EXO.2.2v3: An SPF policy SHALL be published for each domain that fails all non-approved senders.
Product: Exchange Online · Baseline: exo · Group: 2. Sender Policy Framework · Criticality: SHALL

## Policy
An SPF policy SHALL be published for each domain that fails all non-approved senders.

- _Rationale:_ An adversary may modify email headers so the email appears to be a legitimate email sent by an
agency, facilitating phishing attacks. Publishing an SPF policy for each agency domain mitigates this by providing a means for recipients to detect emails spoofed in this way. SPF is required for FCEB agencies by Binding Operational Directive (BOD) 18-01, "Enhance Email and Web Security."
- _Last modified:_ October 2025
- _Note:_ SPF defines two different "fail" mechanisms: fail (indicated by `-`, sometimes referred to as hardfail) and softfail (indicated by `~`). Either hardfail or softfail may be used to comply with this baseline policy.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-2d
- _MITRE ATT&CK TTP Mapping:_
  - [T1656: Impersonation](https://attack.mitre.org/techniques/T1656/)
  - [T1566: Phishing](https://attack.mitre.org/techniques/T1566/)

## Resources
- [Binding Operational Directive 18-01 - Enhance Email and Web Security
  \| DHS](https://cyber.dhs.gov/bod/18-01/)

- [Trustworthy Email \| NIST 800-177 Rev.
  1](https://csrc.nist.gov/publications/detail/sp/800-177/rev-1/final)

- [Set up SPF to help prevent spoofing \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-spf-configure?view=o365-worldwide)

- [How Microsoft 365 uses Sender Policy Framework (SPF) to prevent
  spoofing \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-anti-spoofing?view=o365-worldwide)

## License Requirements
- N/A

## Implementation
First, identify any approved senders specific to your agency, e.g., any on-premises mail servers. SPF allows you to indicate approved senders by IP address or CIDR range. However, note that SPF allows you to [include](https://www.rfc-editor.org/rfc/rfc7208#section-5.2) the IP addresses indicated by a separate SPF policy, referred to by domain name. See [External DNS records required for SPF](https://learn.microsoft.com/en-us/microsoft-365/enterprise/external-domain-name-system-records?view=o365-worldwide#external-dns-records-required-for-spf) for inclusions required for M365 to send email on behalf of your domain.

SPF is not configured through the Exchange admin center but rather via
DNS records hosted by the agency's domain. The exact steps needed
to set up SPF varies from agency to agency. See [Add or edit an SPF TXT record to help prevent email spam (Outlook, Exchange Online) \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-or-edit-an-spf-txt-record-to-help-prevent-email-spam-outlook-exchange-online) for more details.

To test your SPF configuration, consider using a web-based tool, such as
those listed under [How can I validate SPF records for my domain? \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq?view=o365-worldwide#how-can-i-validate-spf-records-for-my-domain).
Additionally, SPF records can be requested using the
PowerShell tool `Resolve-DnsName`. For example:

```
Resolve-DnsName example.onmicrosoft.com txt
```

If SPF is configured, you will see a response resembling `v=spf1 include:spf.protection.outlook.com -all`
returned. The contents of the SPF
policy may vary by agency. In this example, the SPF policy indicates
the IP addresses listed by the policy for "spf.protection.outlook.com" are
the only approved senders for "example.onmicrosoft.com." These IPs can be determined
via an additional SPF lookup, this time for "spf.protection.outlook.com." Ensure the IP addresses listed as approved senders for your domain are correct. Additionally, ensure that each policy either ends in `-all` or `~all`, or [redirects](https://www.rfc-editor.org/rfc/rfc7208#section-6.1) to one that does. This directive indicates that all IPs that don't match the policy should fail. See [SPF TXT record syntax for Microsoft 365 \| Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-anti-spoofing?view=o365-worldwide#spf-txt-record-syntax-for-microsoft-365) for a more in-depth discussion
of SPF record syntax.
