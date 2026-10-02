#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

try:
    from rdflib import Graph, URIRef
    from rdflib.namespace import OWL, RDF
except ImportError as exc:
    raise SystemExit("rdflib is required: pip install rdflib") from exc

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "ontology" / "natdd-core.ttl"
EXAMPLE = ROOT / "examples" / "data-template.ttl"
BASE = "https://lindas.admin.ch/fobl/kbob/dd-fm/vocab/"
RELEASE_HASHES = {
    ROOT / "releases" / "0.1.0" / "natdd-core.ttl":
        "5fa610376f600f3a966daf86204afddcffb758ec6bebeeb45730687d62023b92",
}
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


for path in (CURRENT, EXAMPLE, *RELEASE_HASHES):
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    graph = Graph()
    graph.parse(path, format="turtle")
    print(f"parsed {path.relative_to(ROOT)}: {len(graph)} triples")

for path, expected_hash in RELEASE_HASHES.items():
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != expected_hash:
        fail(f"immutable release changed: {path.relative_to(ROOT)}")
    print(f"verified immutable release: {path.relative_to(ROOT)}")

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
