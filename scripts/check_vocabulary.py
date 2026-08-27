#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    from rdflib import Graph, URIRef
    from rdflib.namespace import OWL, RDF
except ImportError as exc:
    raise SystemExit("rdflib is required: pip install rdflib") from exc

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "ontology" / "natdd-core.ttl"
SNAPSHOT = ROOT / "releases" / "0.1.0" / "natdd-core.ttl"
EXAMPLE = ROOT / "examples" / "data-template.ttl"
BASE = "https://lindas.admin.ch/fobl/kbob/dd-fm/vocab/"
FORBIDDEN = (
    "ConceptUsage",
    "usageSubject",
    "usageTarget",
    "usageType",
    "idsSpecification",
    "idsIfcVersion",
    "https://lindas.admin.ch/vocab/data-dictionary/",
    "https://schema.ld.admin.ch/data-dictionary",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for path in (CURRENT, SNAPSHOT, EXAMPLE):
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    graph = Graph()
    graph.parse(path, format="turtle")
    print(f"parsed {path.relative_to(ROOT)}: {len(graph)} triples")

if CURRENT.read_bytes() != SNAPSHOT.read_bytes():
    fail("current ontology and 0.1.0 snapshot differ")

text = CURRENT.read_text(encoding="utf-8")
for token in FORBIDDEN:
    if token in text:
        fail(f"forbidden deferred or transitional term found: {token}")

graph = Graph().parse(CURRENT, format="turtle")
ontology = URIRef(BASE)
if (ontology, RDF.type, OWL.Ontology) not in graph:
    fail("vocabulary base is not declared owl:Ontology")

terms = {s for s, _, _ in graph if str(s).startswith(BASE) and s != ontology}
if not terms:
    fail("no NatDD terms declared")
required_production_terms = {
    "AllowedValue",
    "DocumentType",
    "TaxonomyNode",
    "documentItemReference",
}
missing = {
    term for term in required_production_terms if URIRef(BASE + term) not in terms
}
if missing:
    fail(f"production vocabulary terms are undefined: {', '.join(sorted(missing))}")
print(f"validated {len(terms)} NatDD terms")
