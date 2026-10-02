# NatDD Core Vocabulary

Public review repository for the core RDF vocabulary used to publish National Data Dictionary (NatDD) data.

Status: **Public technical consultation / öffentliche Fachkonsultation — 2026**

The consultation is open to all interested participants. KBOB will also invite a
small group of specialists in metadata schemas, Linked Data, BIM
standardisation, and data-dictionary implementation to review the proposal.

- Consultation baseline: to be tagged `v0.2.0-consultation-2026` when this setup is approved
- Submission deadline: **31 December 2026, 23:59 CET**
- Working languages: **English and German**
- Process and schedule: [`CONSULTATION.md`](CONSULTATION.md)
- Governance and human-accountability rules: [`GOVERNANCE.md`](GOVERNANCE.md)
- How to contribute: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Maintainer launch checklist: [`docs/github-consultation-admin-checklist.md`](docs/github-consultation-admin-checklist.md)

Vocabulary namespace: `https://lindas.admin.ch/fobl/kbob/dd-fm/vocab/` **(provisional; migration planned after formal namespace approval)**

Preferred prefix: `dd`

The namespace is provisional while an authoritative federal schema namespace is being reviewed. It may change before version 1.0. The current namespace will not be silently reused with different meanings; a migration mapping will be published when a final namespace is approved.

## Scope

This release defines only the core structure needed for Data Dictionaries, classes, properties, groups, enumerations, documents, Data Templates, and contextual Property Requirements.

It deliberately excludes:

- ConceptUsage and downstream relationship-governance records;
- IDS export extensions;
- SHACL application profiles;
- application-specific UI and persistence terms.

NatDD reuses RDF, RDFS, OWL, DCAT, Dublin Core, SKOS, PROV-O and QUDT terms where those vocabularies already express the required semantics.

## Repository

- [`ontology/natdd-core.ttl`](ontology/natdd-core.ttl) — current core vocabulary
- [`releases/0.1.0/natdd-core.ttl`](releases/0.1.0/natdd-core.ttl) — immutable release snapshot
- [`docs/index.md`](docs/index.md) — vocabulary overview and term groups
- [`docs/external-vocabulary-usage.md`](docs/external-vocabulary-usage.md) — policy for reusing standard vocabularies
- [`docs/namespace-policy.md`](docs/namespace-policy.md) — provisional namespace and migration policy
- [`examples/data-template.ttl`](examples/data-template.ttl) — compact worked example
- [`scripts/check_vocabulary.py`](scripts/check_vocabulary.py) — release consistency checks

## Use

```turtle
@prefix dd: <https://lindas.admin.ch/fobl/kbob/dd-fm/vocab/> .
```

The prefix is only an abbreviation. The complete HTTP IRIs are the identifiers.

## Validation

```bash
python3 scripts/check_vocabulary.py
```

## Feedback

Use the structured GitHub consultation form for comments. Concrete amendments
may additionally be proposed through pull requests linked to a consultation
issue. An offline CSV comment sheet is available at
[`docs/consultation-comment-sheet.csv`](docs/consultation-comment-sheet.csv).

Pull requests are proposals; only a recorded consultation decision authorises a
merge. Breaking changes are permitted during the `0.x` public-review phase and
will be recorded in the changelog.

## License

CC0 1.0 Universal. See [`LICENSE`](LICENSE).
