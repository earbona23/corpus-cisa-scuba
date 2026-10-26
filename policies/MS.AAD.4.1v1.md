# MS.AAD.4.1v1: Security logs SHALL be sent to the agency's security operations center for monitoring.
Product: Microsoft Entra ID · Baseline: aad · Group: 4. Centralized Log Collection · Criticality: SHALL

## Policy
Security logs SHALL be sent to the agency's security operations center for monitoring.

- _Rationale:_ The security risk posed by lacking visibility into cyber attacks is reduced by collecting logs in the agency’s centralized security detection infrastructure. This makes security events available for auditing, query, and incident response.
- _Last modified:_ June 2023
- _Note:_ The following Microsoft Entra ID logs (configured in diagnostic settings), are required: `AuditLogs, SignInLogs, RiskyUsers, UserRiskEvents, NonInteractiveUserSignInLogs, ServicePrincipalSignInLogs, ADFSSignInLogs, RiskyServicePrincipals, ServicePrincipalRiskEvents, EnrichedOffice365AuditLogs, MicrosoftGraphActivityLogs`. If managed identities are used for Azure resources, also send the `ManagedIdentitySignInLogs` log type. If the Microsoft Entra ID Provisioning Service is used to provision users to software as a service (SaaS) applications or other systems, also send the `ProvisioningLogs` log type.
- _Note:_ Agencies can benefit from security detection capabilities offered by CISA’s Cloud Log Aggregation Warehouse (CLAW) system. Agencies are encouraged to send the logs to CLAW. Contact CISA at [cyberliaison@cisa.dhs.gov](mailto:cyberliaison@cisa.dhs.gov) to request integration instructions.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AU-4
- _MITRE ATT&CK TTP Mapping:_
  - [T1562: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
    - [T1562.008: Disable or Modify Cloud Logs](https://attack.mitre.org/techniques/T1562/008/)

## Resources
- [Everything you wanted to know about Security and Audit Logging in Office 365](https://thecloudtechnologist.com/2021/10/15/everything-you-wanted-to-know-about-security-and-audit-logging-in-office-365/)

- [What are Microsoft Entra sign-in logs??](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins)

- [National Cybersecurity Protection System-Cloud Interface Reference Architecture Volume One: General Guidance](https://www.cisa.gov/sites/default/files/publications/NCPS%20Cloud%20Interface%20RA%20Volume%20One%20%282021-05-14%29.pdf)

## License Requirements
- An Azure subscription may be required to send logs to an external system, such as the agency's Security Information and Event Management (SIEM).

## Implementation
Follow the configuration instructions unique to the products and integration patterns at your organization to send the security logs to the security operations center for monitoring.
