# Public Technical Consultation 2026

## Purpose and status

This repository hosts an open technical consultation on the NatDD Core
Vocabulary. KBOB will proactively invite approximately five to ten specialists,
while submissions from any other interested person remain welcome.

This is a project and industry consultation. It is not presented as a formal
federal consultation under the Swiss Consultation Procedure Act.

Deutsch: Dieses Repository dient einer öffentlichen Fachkonsultation zum NatDD-
Kernvokabular. KBOB lädt gezielt eine kleine Gruppe fachkundiger Personen ein;
weitere interessierte Personen können sich ebenfalls beteiligen. Es handelt sich
um eine fachliche Projektkonsultation und nicht um ein formelles eidgenössisches
Vernehmlassungsverfahren.

## Period and milestones

- Opening: publication of tag `v0.2.0-consultation-2026`
- First consolidation: end of October 2026
- Second consolidation: end of November 2026
- Preliminary final consolidation: December 2026
- Submission deadline: **31 December 2026, 23:59 CET**
- Final disposition of late-December submissions and results report: January 2027

Exact workshop dates and access details will be communicated separately. Each
monthly cut-off is represented by a GitHub milestone.

## Scope

In scope:

- classes, properties, definitions, domains, ranges, and identifiers;
- reuse of external vocabularies;
- semantic consistency and RDF modelling;
- BIM and data-dictionary interoperability;
- implementation feasibility and migration effects;
- examples and normative documentation.

Out of scope unless the scope is formally extended:

- product-specific user interfaces;
- unrelated data-dictionary content;
- operational deployment of SchemaForge or other repositories;
- bulk terminology proposals without a demonstrated NatDD use case.

## Submission channels

1. **GitHub consultation issue — preferred.** Use one issue per subject.
2. **Pull request — for concrete amendments.** Every PR must link to an issue.
3. **Offline comment sheet — accessibility fallback.** Submitters may complete
   `docs/consultation-comment-sheet.csv`; the consultation chair will transfer
   the submission into the public register with its provenance.

GitHub submissions, account names, affiliations voluntarily provided, comments,
and decisions are public. Participants must not include confidential or personal
information that is unnecessary for the consultation.

## Processing and decisions

The consultation chair checks completeness, scope, duplication, and readiness.
Substantive proposals are discussed during a consolidation workshop or resolved
in the public issue when discussion is unnecessary.

Every in-scope submission receives one disposition:

- accepted;
- accepted with modification;
- rejected;
- deferred to a future release;
- duplicate;
- out of scope.

The disposition, rationale, meeting date, and implementing pull request or commit
are recorded in the issue and in `docs/consultation-disposition-register.csv`.
The number of comments or supporters does not determine acceptance. Decisions
are based on semantic correctness, evidence, practical relevance,
interoperability, compatibility, and coherent scope.

The consultation chair is responsible for the final repository decision and
consistent implementation. The expert group advises and supports consolidation;
participation does not confer merge or repository-administration rights.

## Languages

English and German are accepted. English is the authoritative language for the
technical schema when translations diverge. German is fully accepted for
consultation comments and workshop discussion.

## Consultation outputs

After closure, the repository will publish:

- the completed disposition register;
- a concise, neutral consultation results report;
- the resulting candidate or release tag;
- migration notes for breaking changes.
