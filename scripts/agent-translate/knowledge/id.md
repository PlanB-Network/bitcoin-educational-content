# Lessons — id

## 2026-07-03
- Simplicity/Rust-Bitcoin technical jargon (jets, combinators: iden, unit, comp, pair, case, take, drop, injl, injr, DAG, Merkle root) stays in English verbatim — no glossary entries exist for these; Indonesian technical readers expect the original terms.
- "sum type" -> "tipe jumlah", "product type" -> "tipe produk", "tagged union" -> "union bertanda", "sequential/parallel composition" -> "komposisi sekuensial/paralel" — used consistently across the quiz set.
- Math symbols (𝟙, 𝟚, σᴸ⟨⟩, ⟨a,b⟩, ▵) and formulas kept byte-identical; only surrounding prose translated.
- Simplicity/Bit Machine core terms kept in English (not transliterated): combinator, jet, Bit Machine, midstate, node, environment, buffer, writer/reader effect, key-path/key-spend, script path, witness.
- Kept English technical nouns as-is: kombinator, jet, buffer, environment, node, midstate, key-path/key-spend, script path, witness, cache, encode, error, overflow, unroll — natural in ID technical prose, avoid forced Indonesian equivalents (e.g. not "efek penulis" for writer effect).
- "unitary"/"unitarity" → "uniter"/"uniteritas" (consistent with commutative→komutatif, idempotent→idempoten pattern).
- "carry"/"sum" (adder bits) left untranslated — standard in ID digital-logic vocabulary.
- Formula/pseudocode fragments (case, pair, comp, iden, take, drop, injl, injr, scribe, CMR, etc.) left verbatim as code-like identifiers even though not in fenced code blocks.
- "smart contract" → "kontrak pintar" (per `resources/glossary/smart-contract/id.md`); course titles/headings ARE translated per existing convention in other `courses/*/id.md` files (e.g. dev303), so `name`/`title`/headings got Indonesian renderings even for proper-noun-like course names.
- Highly technical/mathematical CS jargon (combinator, sum type, product type, sequent calculus terms like "sum", "product", "environment", "buffer", "stack", "jet", "witness", "commitment", "pruning") kept in English inline within Indonesian prose — no established Indonesian rendering exists in the glossary and forcing a translation would hurt clarity for this expert audience; only surrounding connective prose was translated.
- Formal named effect properties (Commutative, Idempotent, Unitary → "komutatif", "idempoten", "uniter") were translated as adjectives but the table header row (English) was left untouched since it's tabular/structural content mirroring the source exactly.
- "Taproot" and BIP/CMR/TapLeaf/TapTweak jargon stay verbatim per `resources/glossary/taproot/id.md` convention (proper nouns/protocol names never transliterated).
- Simplicity/Bitcoin technical terms (Simplicity, combinator, jet, side effect, witness, Reader/Failure effect, Taproot, TapLeaf, batch verification, sequent calculus) stay in English — no Indonesian coinage found in glossary or existing corpus.
- "recursive covenant" → "kovenan rekursif" per `resources/glossary/recursive-covenant/id.md`; "Taproot" stays untranslated per `resources/glossary/taproot/id.md`.
- Standard math/CS jargon kept English with Indonesian connective prose: "produk" (product), "sum", "pair", "tagged union", "fixed-point", "loop unrolling" — these read naturally to an Indonesian technical audience and have no established local equivalent in this glossary.
- "commit"/"men-commit" and "redemption"/"penebusan" used as verbs — kept the English loanword "commit" (conjugated with Indonesian prefix meN-) since it's the standard usage in Indonesian crypto/dev writing.
