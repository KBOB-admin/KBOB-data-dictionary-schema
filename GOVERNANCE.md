# Governance / Governance-Regeln

## Roles and authority

### Schema Maintainer and Consultation Chair

One designated maintainer administers the repository and consultation. The
maintainer performs triage, organises and moderates workshops, records decisions,
edits the schema, merges accepted changes, and publishes consultation outputs.

### Participants

Invited experts and other interested persons may open issues, comment, review,
and submit pull requests from forks. Participants receive no write or
administrative rights. A contribution or review does not itself authorise a
merge.

Deutsch: Der Schema-Maintainer leitet die Konsultation, führt das Repository,
dokumentiert Entscheide und setzt angenommene Änderungen um. Teilnehmende können
Eingaben und Pull Requests einreichen, erhalten dadurch aber keine Schreib- oder
Administrationsrechte.

## Decision principles

Decisions consider:

- semantic and technical correctness;
- demonstrated user or implementation need;
- reuse of established vocabularies;
- interoperability with BIM and public-data ecosystems;
- backward compatibility and migration cost;
- internal consistency and defined project scope;
- evidence and expert reasoning rather than submission volume.

Every in-scope submission receives a recorded disposition and concrete rationale.
Conflicts of interest should be disclosed in the relevant issue. The maintainer
may request additional expert input before deciding.

## Human accountability for AI-assisted contributions

The responsible use of artificial intelligence may support research,
translation, analysis, drafting, and technical validation. AI systems are not
recognised as participants, authors, experts, or decision-makers in this
consultation.

Every issue, comment, and pull request must be submitted and owned by an
identifiable human participant. By submitting, the participant confirms that
they:

- personally reviewed and understood the complete submission;
- remain responsible for its factual accuracy and normative intent;
- can explain the problem and proposed change in their own words;
- can provide evidence, practical experience, or a concrete use case;
- can discuss and defend the proposal before the expert group when requested;
- will correct or withdraw unsupported statements.

Material AI use must be disclosed briefly, for example as AI-assisted drafting,
translation, schema analysis, or code generation.

Unsupervised agent submissions, automatically generated batches of comments,
synthetic consensus, repetitive mass submissions, and contributions whose
submitter cannot explain their content are inadmissible. The consultation chair
may close or consolidate them without substantive processing.

AI assistance is neither a reason for automatic rejection nor evidence of
technical validity. All contributions are assessed by the same substantive
criteria.

### Menschliche Verantwortung bei KI-Unterstützung

KI darf Recherche, Übersetzung, Analyse, Redaktion oder technische Prüfung
unterstützen. KI-Systeme gelten jedoch nicht als Teilnehmende, Autorinnen bzw.
Autoren, Fachpersonen oder Entscheidungsträger.

Jede Eingabe muss von einer identifizierbaren Person eingereicht und verantwortet
werden. Die einreichende Person muss die vollständige Eingabe persönlich geprüft
und verstanden haben, für Inhalt und Auswirkungen einstehen und den Vorschlag bei
Bedarf vor der Expertengruppe in eigenen Worten erläutern und vertreten können.
Wesentliche KI-Unterstützung ist kurz offenzulegen.

Unbeaufsichtigte Agenteneingaben, automatisch erzeugte Serien- oder
Masseneingaben, künstlich erzeugter Konsens und Eingaben, deren Inhalt die
einreichende Person nicht erklären kann, sind unzulässig. KI-Unterstützung ist
weder ein automatischer Ablehnungsgrund noch ein Qualitätsnachweis.

## Repository controls

- The public may contribute through issues and fork-based pull requests.
- Only the maintainer merges changes.
- Changes to `main` require a pull request and successful validation.
- Review conversations must be resolved before merge.
- Files below `releases/` are immutable.
- Accepted changes are normally squash-merged for a clear history.
- Monthly decisions and final consultation results remain publicly traceable.
