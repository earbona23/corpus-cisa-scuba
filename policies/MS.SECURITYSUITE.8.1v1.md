# MS.SECURITYSUITE.8.1v1: IP allow lists SHOULD NOT be created.
Product: securitysuite · Baseline: securitysuite · Group: 8. IP Allow Lists · Criticality: SHOULD

## Policy
IP allow lists SHOULD NOT be created.

- _Rationale:_ Messages sent from IP addresses on an allow list bypass important
security mechanisms, including spam filtering and sender authentication checks. Avoiding use of IP allow lists prevents potential threats from circumventing security mechanisms.
- _Last modified:_ March 2026
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
To modify the connection filters, follow the instructions found in [Use
the Microsoft 365 Defender portal to modify the default connection
filter
policy](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/connection-filter-policies-configure?view=o365-worldwide#use-the-microsoft-365-defender-portal-to-modify-the-default-connection-filter-policy).

1. Sign in to **Microsoft 365 Defender portal**.

2. From the left-hand menu, find **Email & collaboration** and select **Policies & rules**.

3. Select **Threat policies** from the list of policy names.

4. Under **Policies**, select **Anti-spam**.

5. Select **Connection filter policy (Default)**.

6. Click **Edit connection filter policy**.

7. Ensure no addresses are specified under **Always allow messages from
   the following IP addresses or address range**.

8. Ensure **Turn on safe list** is not selected.
