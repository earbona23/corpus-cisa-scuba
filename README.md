# CISA SCuBA M365 Secure Configuration Baselines (corpus mirror)

Pinned Markdown mirror of the **CISA SCuBA Secure Configuration Baselines for
Microsoft 365**, built for the [XERJ Corpus Hub](https://github.com/xerj-org/xerj/tree/corpus-hub)
as reference-retrieval material for "what does this M365 / Entra ID security
policy actually require, and how is it implemented" questions.

- Source: the [cisagov/ScubaGear](https://github.com/cisagov/ScubaGear) repository
  (`PowerShell/ScubaGear/baselines/*.md`), repository licence **CC0-1.0**.
- Pinned commit: see [PROVENANCE.txt](PROVENANCE.txt). The commit of *this* repository
  is the snapshot; re-snapshotting a newer upstream release is a new commit, never a
  force-push.
- Shape: **one Markdown file per SCuBA policy** — `policies/MS.<ID>.md`, **109 policies**
  across seven product baselines (Entra ID, Exchange Online, SharePoint, Teams, Power BI,
  Power Platform, and the Defender/Security Suite). Each file carries a one-line
  breadcrumb (product, baseline, policy group, criticality), then the verbatim policy
  statement, its rationale and its NIST SP 800-53 and MITRE ATT&CK mappings, the policy's
  resources, its licence requirements, and its implementation instructions.
- Shape limits: no file over 150 KB (largest is ~6 KB). Shields.io status badges are
  dropped and HTML metadata comments are folded into the breadcrumb; everything else is
  the upstream text unchanged.

## Why per policy

A SCuBA baseline is one long document per product, but an agent auditing or configuring
M365 almost always needs a single policy — "MS.AAD.3.1v1, phishing-resistant MFA" — not
the whole Entra baseline. One file per policy keeps each retrieval unit to the question a
reader actually asks, and the policy ID is the natural key.

## Licence

These baselines are U.S. Government work distributed from a CC0-1.0 repository and marked
**TLP:CLEAR** ("Recipients may share this information without restriction"). Portions are
adapted from Microsoft M365/Azure documentation under the **Creative Commons Attribution
4.0 International** licence. The full notices, verbatim, are in
[LICENSE-TERMS](LICENSE-TERMS), which satisfies the CC BY 4.0 attribution condition; this
mirror adds no restriction of its own.

For non-federal users the baselines are provided "as is" for informational purposes only
and do not supersede any law or regulation (see LICENSE-TERMS).

## Regeneration

Exact steps to rebuild this mirror from upstream (run in a directory holding
`split_scuba.py` from this repository):

```sh
# 1. Fetch the seven baseline Markdown files at the pinned commit (see PROVENANCE.txt)
#    from cisagov/ScubaGear into ./src :
#    PowerShell/ScubaGear/baselines/{aad,exo,powerbi,powerplatform,securitysuite,sharepoint,teams}.md
# 2. Split them into one file per policy:
python3 split_scuba.py src policies
```
