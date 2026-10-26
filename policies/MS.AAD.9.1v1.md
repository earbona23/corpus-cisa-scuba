# MS.AAD.9.1v1: Risky AI agents SHALL be blocked.
Product: Microsoft Entra ID · Baseline: aad · Group: 9. AI Security · Criticality: SHALL

## Policy
Risky AI agents SHALL be blocked.

- _Rationale:_ AI agents may access tenant resources and can perform actions autonomously. Blocking agents that exhibit risky behaviors reduces the risk of unauthorized access and automated misuse of resources.
- _Last modified:_ March 2026
- _Note:_ This policy is not applicable to Government Community Cloud (GCC) High, and Department of Defense (DoD) tenants.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-3, AC-6, CM-7(4)
- _MITRE ATT&CK TTP Mapping:_
  - [T1078: Valid Accounts](https://attack.mitre.org/techniques/T1078/)
    - [T1078.004: Cloud Account](https://attack.mitre.org/techniques/T1078/004/)

## Resources
- [Block access by high-risk agent identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-agent-block-high-risk)

## License Requirements
- Requires a Microsoft Entra ID P2 license and either Microsoft Agent 365 or Microsoft 365 E7.

## Implementation
1. Create a conditional access policy blocking High Risk AI Agents. Configure the following policy settings in the new conditional access policy, per the values below:

<pre>
  Assignments > Users, agents (preview) or workload identities > What does this policy apply to? > Agents (preview) > Include > <b>All agent identities (preview) </b>

  Target resources > Include > <b>All resources (formerly 'All cloud apps') </b>

  Conditions > Agent risk (preview) > Configure > Yes > Configure agent risk levels needed for policy to be enforced > <b>High </b>
</pre>

# Appendix A: Microsoft Entra ID hybrid Guidance

Most of this document does not focus on securing Microsoft Entra ID hybrid environments. CISA released a separate [Hybrid Identity Solutions Architecture](https://www.cisa.gov/sites/default/files/2023-03/csso-scuba-guidance_document-hybrid_identity_solutions_architecture-2023.03.22-final.pdf) document addressing the unique implementation requirements of Microsoft Entra ID hybrid infrastructure.

# Appendix B: Cross-tenant Access Guidance

Some of the conditional access policies contained in this security baseline, if implemented as described, will impact guest user access to a tenant. For example, to gain access, the policies require users to perform MFA and originate from a managed device. These requirements are also enforced for guest users. For these policies to work effectively with guest users, both the home tenant (the one the guest user belongs to) and the resource tenant (the target tenant) may need to configure their Microsoft Entra ID cross-tenant access settings.

Microsoft’s [Authentication and Conditional Access for External ID](https://learn.microsoft.com/en-us/entra/external-id/authentication-conditional-access) provides an understanding of how MFA and device claims are passed from the home tenant to the resource tenant. To configure the inbound and outbound cross-tenant access settings in Microsoft Entra External ID, refer to Microsoft’s [Overview: Cross-tenant access with Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview).

**`TLP:CLEAR`**
