# MS.SECURITYSUITE.8.2v1: Safe lists SHOULD NOT be enabled.
Product: securitysuite · Baseline: securitysuite · Group: 8. IP Allow Lists · Criticality: SHOULD

## Policy
Safe lists SHOULD NOT be enabled.

- _Rationale:_ Messages sent from allowed safe list addresses bypass important
security mechanisms, including spam filtering and sender authentication checks.
Avoiding use of safe lists prevents potential threats from circumventing
security mechanisms. While blocking all malicious senders is not feasible,
blocking specific known, malicious IP addresses may reduce the threat from
specific senders.
- _Last modified:_ March 2026
- _Note:_ A connection filter MAY be implemented to create an IP block list.
- _NIST SP 800-53 Rev. 5 FedRAMP High Baseline Mapping:_ AC-4
- _MITRE ATT&CK TTP Mapping:_
  - None

## Resources
- [Use the IP Allow List \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/create-safe-sender-lists-in-office-365?view=o365-worldwide#use-the-ip-allow-list)

- [Configure connection filtering \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/connection-filter-policies-configure?view=o365-worldwide)

- [Use the Microsoft 365 Defender portal to modify the default
  connection filter policy \| Microsoft
  Learn](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/connection-filter-policies-configure?view=o365-worldwide#use-the-microsoft-365-defender-portal-to-modify-the-default-connection-filter-policy)

## License Requirements
- N/A

## Implementation
1. Sign in to **Microsoft 365 Defender portal**.

2. From the left-hand menu, find **Email and collaboration** and select **Policies and rules**.

3. Select **Threat policies** from the list of policy names.

4. Under **Policies**, select **Anti-spam**.

5. Select **Connection filter policy (Default)**.

6. Click **Edit connection filter policy**.

7. (Optional) Enter addresses under **Always block messages from the following
   IP addresses or address range** as needed.

8. Ensure **Turn on safe list** is not selected.

# Appendix A: Adding Users to the Preset Security Policies
As many controls in this baseline can be satisfied by adding users to the standard
or strict security policies, this process is described once rather than in
duplicative sections for each applicable control.

To add users to the standard policy:
1. Sign in to **Microsoft 365 Defender**.
2. In the left-hand menu, click on **Email & collaboration**, then click on **Policies & rules**.
3. Select **Threat policies**.
4. From the **Templated policies** section, select **Preset security policies**.
5. Under **Standard protection**, enable the toggle so that it reads "Standard protection is on."
6. Under **Standard protection is on**, select **Manage protection settings**.
7. On the **Apply Exchange Online Protection** page, select **All recipients**.
8. (Optional) Under **Exclude these recipients**, add **Users** and **Groups**
   to be exempted from the preset policies.
9. Select **Next**, then on the **Apply Defender for Office 365 protection** page, select **All recipients**.
10. (Optional) Under **Exclude these recipients**, add **Users** and **Groups**
   to be exempted from the preset policies.
11. Select **Next** on each page until the **Review and confirm your changes** page appears.
12. On the **Review and confirm your changes** page, select **Confirm**.

To add users to the strict policy:
1. Sign in to **Microsoft 365 Defender**.
2. In the left-hand menu, click on **Email & collaboration**, then click on **Policies & rules**.
3. Select **Threat policies**.
4. From the **Templated policies** section, select **Preset security policies**.
5. Under **Strict protection**, ensure the toggle is enabled so that it reads "Strict protection is on."
6. Under **Strict protection is on**, select **Manage protection settings**.
7. On the **Apply Exchange Online Protection** page, select **All recipients**.
8. (Optional) Under **Exclude these recipients**, add **Users** and **Groups**
   to be exempted from the preset policies.
9. Select **Next**, then on the **Apply Defender for Office 365 protection** page, select **All recipients**.
10. (Optional) Under **Exclude these recipients**, add **Users** and **Groups**
   to be exempted from the preset policies.
11. Select **Next** on each page until the **Review and confirm your changes** page appears.
12. On the **Review and confirm your changes** page, select **Confirm**.

See [Recommended email and collaboration threat policy settings for cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365) to understand the
differences between the two preset policies.

Note that a user can be added to multiple policies. In that case, the policies
are applied in order of precedence, as described by the
[order of precedence for preset security policies and other threat policies](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies#order-of-precedence-for-preset-security-policies-and-other-threat-policies).

**`TLP:CLEAR`**
