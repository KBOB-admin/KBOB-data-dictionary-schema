# Contributing / Mitwirkung

NatDD 0.x is open for public technical consultation. Contributions are welcome
in English or German. The technical schema is maintained in English; relevant
labels and definitions may also be provided in German.

## Preferred process / Bevorzugter Ablauf

1. Open one structured consultation issue per subject.
2. Describe the current model, the problem, the requested change, the rationale,
   and a concrete use case.
3. For a concrete file change, fork the repository and open a pull request that
   links to the issue.
4. Keep unrelated changes in separate submissions.
5. Respond to clarification requests and, when requested, explain the proposal
   during a consolidation workshop.

Deutsch: Pro Thema ist eine strukturierte Konsultationseingabe zu eröffnen.
Konkrete Dateiänderungen können zusätzlich als Pull Request aus einem Fork
eingereicht werden. Jeder Pull Request muss auf die zugehörige Eingabe verweisen.

## Required content / Erforderliche Angaben

Every proposed term change must state:

1. the affected term, IRI, or document section;
2. the business or interoperability requirement;
3. why an established vocabulary does not already cover the requirement;
4. the proposed class/property IRI, wording, domain, range, or other semantics;
5. at least one practical use case or RDF example;
6. migration and compatibility effects;
7. the participant's capacity or organisational affiliation, if relevant;
8. any material AI assistance.

Terms must not be added merely as aliases for RDF, RDFS, OWL, DCAT, Dublin
Core, SKOS, PROV-O, QUDT, or another suitable established vocabulary.

## Human responsibility / Menschliche Verantwortung

AI may assist research, drafting, translation, analysis, or code generation, but
it cannot be the author, participant, or decision-maker. The human submitter must
personally review and understand the complete contribution, remain responsible
for it, and be able to explain and defend it before the expert group. Material AI
assistance must be disclosed.

Unsupervised agent submissions, automatically generated batches, repetitive mass
comments, synthetic consensus, and submissions whose author cannot explain their
content may be closed without substantive processing. See
[`GOVERNANCE.md`](GOVERNANCE.md) for the complete policy.

Deutsch: KI darf unterstützend eingesetzt werden. Die einreichende Person bleibt
jedoch vollständig verantwortlich, muss die Eingabe selbst geprüft und verstanden
haben und sie vor der Expertengruppe erläutern und vertreten können. Wesentliche
KI-Unterstützung ist offenzulegen. Unbeaufsichtigte Agenteneingaben und
automatisch erzeugte Masseneingaben sind unzulässig.

## Pull requests

- Link the consultation issue using `Related consultation issue: #…`.
- Do not modify an immutable file below `releases/`.
- Run `python3 scripts/check_vocabulary.py` before requesting review.
- Explain tests and compatibility effects in the pull-request template.
- Prefer small, reviewable commits. The maintainer may squash them when merging.
- A pull request is a proposal and may not be merged until its consultation
  disposition has been recorded.

By contributing, the participant confirms that they have the right to submit the
material under the repository's CC0 licence.
