# External vocabulary usage

NatDD follows a reuse-before-invention policy. A `dd:` term is introduced only when established vocabularies do not express the required Data Dictionary structure.

| Meaning | Term | Vocabulary | Guidance |
|---|---|---|---|
| RDF classification | `rdf:type` | RDF | State the class of a resource |
| Human-readable name | `rdfs:label` | RDFS | Use language-tagged literals |
| Definition | `skos:definition` | SKOS | Use for definitions of dictionary concepts |
| Dataset publication | `dcat:Dataset`, `dcat:DatasetSeries` | DCAT | Describe dictionary releases and series |
| Stable identifier | `dcterms:identifier` | Dublin Core | Use the publisher-assigned identifier |
| General source/reference | `dcterms:source` | Dublin Core | Cite the source without asserting a derivation process |
| Derived entity | `prov:wasDerivedFrom` | PROV-O | Use when an entity was generated from another entity |
| Responsible agent | `prov:wasAttributedTo` | PROV-O | Link an entity to the responsible agent |
| Value-list membership | `skos:inScheme` | SKOS | Link an Enumeration Value to its scheme |
| Semantic mapping | `skos:exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch` | SKOS | Use only after reviewing mapping direction and strength |
| Unit | `qudt:hasUnit` | QUDT | Use an approved QUDT unit IRI |
| Release version | `owl:versionInfo`, `owl:versionIRI` | OWL | Identify the vocabulary release |

## Source versus derivation

`prov:wasDerivedFrom` is a PROV-O term, not a Dublin Core term.

```turtle
:dictionary-0.1.0
    a dcat:Dataset, dd:DataDictionary, prov:Entity ;
    dcterms:source :source-workbook ;
    prov:wasDerivedFrom :source-workbook .

:source-workbook
    a prov:Entity ;
    dcterms:identifier "NatDD-example.xlsx" .
```

Use `dcterms:source` for a general source or citation. Add `prov:wasDerivedFrom` when the published entity was actually produced by transforming the source entity.

NatDD does not copy external vocabulary definitions and does not use `owl:imports` merely to acknowledge them.
