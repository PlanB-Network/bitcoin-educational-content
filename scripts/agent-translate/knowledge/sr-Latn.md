# Lessons — sr-Latn

## 2026-07-03
- Simplicity/scr403 (Simplicity language) domain: keep effect names (`Failure`, `Reader`, `State`, `Writer`, `IO`, `Memory`, `Continuation`, `Nondeterminism`) verbatim in English, adding `efekat`/`efekta` — e.g. "Failure efekat", "kroz jet-ove". Keep combinator names (`case`, `take`, `drop`, `iden`, `bip0340-verify`, `sig-all-hash`), `jet`, `CMR`, `TapLeaf`, `TxEnv`, `PrecomputedTransactionData` verbatim.
- `covenant`: follow glossary — keep English word ("rekurzivni covenant-i"), do not translate as "savez" in course prose.
- `witness`: kept English as attributive term ("witness vrednosti", "witness izrazi") in Simplicity/Taproot context, even though the glossary noun entry is "svedok transakcije".
- Foreign language name `Simplicity` declined with hyphen: gen. `Simplicity-ja`, loc. `Simplicity-ju`, poss. adj. `Simplicity-jev`.
- Term renderings used consistently: combinator → `kombinator`; sequent calculus → `sekventni račun`; hash → `heš`; batch verification → `grupna verifikacija`; boolean → `logička vrednost`; prune → `orezati`/`orezivanje`; sum/product/tagged union → `suma`/`proizvod`/`označena unija`; I/O → `U/I`; unit type → `jedinični tip`.
- Type-theory terms (scr403 / Simplicity course): `sum type` → "zbirni tip", `product type` → "proizvodni tip", `unit type` → "jedinični tip", `boolean type` → "Bulov tip". Keep sum/product paired as zbir/proizvod for consistency.
- `tagged union` → "označena unija"; `left-tagged`/`right-tagged` → "levo označen"/"desno označen"; `tag` (the bit) → "oznaka".
- `combinator` → "kombinator", `accessor` → "pristupnik", `half-adder` → "polusabirač", `carry` → "prenos", `truth table` → "tablica istinitosti".
- Keep verbatim as identifiers/proper names: Simplicity, Bitcoin Script, Liquid Network, Ethereum, SHA-256, Merkle, Rocq, DAG, and all combinator names (iden, unit, comp, pair, case, take, drop, injl, injr, scribe), plus operators AND/XOR/OR/NOT and the term "jet" (declined "jet-ovi").
- Foreign proper nouns take Serbian case endings via hyphen: "Simplicity-ju" (loc.), "Ethereum-a" (gen.), "DAG-ovi" (pl.). Keep math glyphs (𝟙, 𝟚, ▵, ⟨⟩, σᴸ, σᴿ, A², A⁴, →, ×, +) byte-identical.
- Za Simplicity imenovane efekte zadržavati engleske nazive i pisati ih kao `Failure efekat`, `Reader efekat` i `Writer efekat`, jer funkcionišu kao tehnički nazivi, ne kao obične reči.
- U Bitcoin/Simplicity kontekstu zadržavati `witness` kao nepreveden tehnički termin: `witness podaci`, `witness izraz`, `witness vrednost`.
- Za type-theory termine koristiti `jedinični tip`, `tip sume` i `tip proizvoda`; za `tagged union` koristiti `tagovana unija`.
- `Commitment Merkle Root` i skraćenicu `CMR` ostaviti neprevedene; `Merkle root` van tog formalnog naziva može biti `Merkle koren` prema glossary terminologiji.
- scr403 (Simplicity) terminology, consistent with existing sr-Latn quizzes 000–014: `kombinator`, `jezgarni kombinator/jezik` (core), `proizvodni tip` (product), `zbirni tip` (sum), `jedinični tip` (unit), `bafer` (buffer), `vektor`, `polusabirač` (half-adder), `puni sabirač` (full-adder), `prenos` (carry), `bit zbira` (sum bit), `Merkle koren`/`Merkle stablo`, `Bit mašina`.
- Keep verbatim: combinator/identifier tokens (`iden`, `comp`, `take`, `drop`, `pair`, `case`, `injl`, `injr`, `unit`, `scribe`, `copair`, `fold`, `map`, `zip`, `push-<n`, `pop-<n`), effect names (`Reader`, `Writer`, `Failure`), `jet`, `Rocq`, `SimplicityHL`, `midstate`, `tag`, `CMR`, `NUMS`, `tweak`, `witness`, `sig-all-hash`, and all inline Simplicity/math expressions (e.g. `O O H ▵ (... ⨾ half-adder)`, `half-adder⟨1,1⟩`) even when they embed the word "half-adder".
- Foreign nouns take hyphenated case endings: `jet-ovi`, `jet-u`, `CMR-om`, `CMR-ove`, `Rocq-u`, `Failure-ov`, `fold-ove`, `Simplicity-jevi/Simplicity-ju`.
- `commit`/`committed`/`commitment` → `obavezati`/`obavezan`/`obavezivanje` (+ `obaveza UTXO-a`); `pruned`/`prune` → `potkresan`/`potkresivanje`; effect-algebra `commutative/idempotent/unitary` → `komutativan/idempotentan/unitaran` (`unitarnost`).
- Taproot spend paths: `key-spend`/`key-path` → `trošenje putem ključa`, `script path` → `putanja skripte`; keep the English acronym gloss `NUMS ('Nothing-Up-My-Sleeve')` untranslated.
