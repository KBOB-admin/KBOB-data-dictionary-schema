# NatDD Core Vocabulary 0.1

Status: **Public Review Draft**

NatDD provides the small structural layer that is missing from the standard vocabularies reused by National Data Dictionary publications.

## Model

```text
DataDictionary
├── hasClass ──────────────────> rdfs:Class
├── hasProperty ───────────────> rdf:Property
├── hasGroupOfProperties ──────> GroupOfProperties
├── hasEnumerationScheme ──────> EnumerationScheme
├── hasDocument ───────────────> Document
└── hasDataTemplate ───────────> DataTemplate
                                   ├── appliesToClass ──────> rdfs:Class
                                   ├── includesGroupOfProperties
                                   └── hasPropertyRequirement
                                              ├── requiresProperty
                                              ├── inGroupOfProperties
                                              ├── usesEnumerationScheme
                                              └── allowedValue
```

`PropertyRequirement` is a contextual association resource. It is not a second semantic definition of a Property. Labels, definitions and base semantics remain on the canonical Property; the requirement records only template-specific information.

## Core classes

| Class | Purpose |
|---|---|
| `dd:DataDictionary` | A versioned Data Dictionary publication unit |
| `dd:GroupOfProperties` | A logical group of Properties |
| `dd:EnumerationScheme` | A controlled value scheme |
| `dd:EnumerationValue` | A value belonging to an Enumeration Scheme |
| `dd:Document` | A document referenced by dictionary resources |
| `dd:DocumentType` | A terminal, deliverable class in a document-type taxonomy |
| `dd:TaxonomyNode` | A non-terminal class used for taxonomy navigation |
| `dd:DataTemplate` | A contextual collection of information requirements |
| `dd:PropertyRequirement` | A contextual use of a canonical Property in a Data Template |

`dd:AllowedValue` is retained as a deprecated compatibility class for already
published data. New data should use `dd:EnumerationValue`.

The complete normative term declarations are in [`../ontology/natdd-core.ttl`](../ontology/natdd-core.ttl).

## Semantic layers

- NatDD core describes dictionary structure.
- SKOS describes controlled values and semantic mappings.
- DCAT and Dublin Core describe datasets and publication metadata.
- PROV-O describes attribution and derivation.
- QUDT identifies units.
- IFC/bSDD identifiers provide external alignment anchors.

These layers must not be conflated. For example, an IFC implementation binding does not by itself establish a broader/narrower business-concept relationship.
