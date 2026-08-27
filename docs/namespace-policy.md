# Namespace and version policy

## Public-review namespace

Version 0.1 uses:

```text
https://lindas.admin.ch/fobl/kbob/dd-fm/vocab/
```

This is a provisional, KBOB-scoped namespace already used by NatDD demonstration data. It is not presented as the final federal schema namespace.

## Stability

- Breaking changes are permitted in `0.x` releases and must be documented.
- Released snapshots remain in `releases/<version>/`.
- Existing IRIs will not be silently assigned different meanings.
- The namespace and term IRIs are intended to be frozen when version 1.0 is approved.

## Federal namespace migration

If a final namespace is approved under `schema.ld.admin.ch`, the project will publish:

1. a term-by-term migration table;
2. `owl:equivalentClass` or `owl:equivalentProperty` only where meanings are genuinely equivalent;
3. deprecation annotations on replaced provisional terms;
4. a SPARQL migration script;
5. a transition period in which tools recognize both namespaces.

The old namespace will remain documented and will not be repurposed.
