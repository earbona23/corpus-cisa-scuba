# MS.POWERPLATFORM.4.1v1: Content Security Policy (CSP) SHALL be enforced for model-driven and canvas Power Apps.
Product: Power Platform · Baseline: powerplatform · Group: 4. Power Apps Content Security Policy · Criticality: SHALL

## Policy
Content Security Policy (CSP) SHALL be enforced for model-driven and canvas Power Apps.

- _Rationale:_ Enforcing CSP for model-driven and canvas Power Apps adds a defense mechanism against common website attacks.
- _Last Modified:_ April 2026
- _Note:_ This policy is only applicable to environments using Dataverse.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ SI-10
- _MITRE ATT&CK TTP Mapping:_
  - [T1190: Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

## Resources
- [Content Security Policy \| Microsoft
  Learn](https://learn.microsoft.com/en-us/power-platform/admin/content-security-policy)

## License Requirements
- N/A

## Implementation
1.  Sign in to your tenant environment's respective [Power Platform admin
center](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-us-government#power-apps-us-government-service-urls).

2.  On the left-hand pane, click on **Environments**, then select an environment from the list.

3.  Select the **Settings** icon at the top of the page.

4.  Click on **Product**, then click on **Privacy + Security** from the options that appear.

5.  At the bottom of the page, under the **Content security policy** section, set **Enforce content security policy** to **On** for **Model-driven** and **Canvas**.

6.  Set **Enable reporting** to **On** and add an appropriate endpoint for reporting CSP violations.

7.  Repeat steps two through six for all active Power Platform environments.
