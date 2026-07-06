# Lessons — ro

## 2026-07-03
- Keep Simplicity/Bitcoin technical terms in English as loanwords per existing `courses/scr403/ro.md`: "combinator(i)", "jet(s)", "witness", "case", "take"/"drop", "buffer(e)", "input"/"output", "covenant-uri", "sandbox".
- Standard renderings used elsewhere in this course: "efect Failure"/"efect Reader" (not translated), "compunere condițională"/"compunere paralelă" for conditional/parallel composition, "Commitment Merkle Root (CMR)" left as-is, "sistem de tipuri", "computație" for computation.
- "verification-in-batch" → "verificare în lot"; "unbounded recursion/iteration" → "recursivitate/iterație nemărginită"; "loop unrolling" → "desfășurarea buclelor".
- Plural of English loanwords follows Romanian agglutination with hyphen where natural (e.g. "jets-urile", "covenant-uri", "input-uri") — but bare "jets"/"combinatori" also occur in the reference doc; prefer the Romanian plural "combinatori" (native plural exists) over "combinators".
- Simplicity DSL combinator names (`iden`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `copair`, `fold-right-n`, `map`, `zip`, `push-<n`, `pop-<n`) and system terms (`jet`, `CMR`, `Bit Machine`, `NUMS`, `Reader`/`Writer`/`Failure` effects) stay in English verbatim — treated as code/identifiers, not prose.
- English jargon with no crisp 1:1 Romanian equivalent (e.g. "bookkeeping", "midstate", "key-spend", "padding") is translated with a natural Romanian phrase followed by the English term in parentheses on first use in that file, e.g. "contabilizare (bookkeeping)", "stare intermediară (midstate)", "cheltuire prin cheie (key-spend)".
- "half-adder"/"full-adder" rendered as "semi-sumator"/"sumator complet", with the English term kept in parentheses on first mention.
- Diacritics/mathematical notation (⟨⟩, ▵, ⨾, ᶜ, ᑉⁿ, ⊢, ×, ₊/₋ superscripts) copied byte-identical from source, never re-typeset.
- Simplicity domain terms kept in English (verbatim, lowercase): combinator names `iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`; also `jet(s)`, `Merkle`, `DAG`, `Bitcoin Script`, `Liquid`, `Rocq`, `SHA-256`, `AND`/`OR`/`XOR`/`NOT`.
- "jet" → "jet-ul"/"jet-urile" (Romanian agglutination with hyphen), same pattern for other English tech nouns needing RO articles/plurals (e.g. "DAG-uri", "buffere").
- "half-adder" rendered as "semi-sumator (half-adder)" — gloss the RO term once, keep English in parens for searchability.
- "static analysis" → "analiză statică"; "dynamic gas model" → "model dinamic de gas" (gas stays English as an Ethereum-specific term).
- "denial-of-service" kept verbatim (established English term in RO tech writing).
- "Combinator" translates as "combinator" (identical CS/math term in Romanian); keep all nine combinator names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`) verbatim as code, never translate them.
- No `ro.md` glossary entries exist yet for Taproot/witness/script family terms in this repo — kept "Taproot", "witness", "jet(s)", "NUMS", "TapLeaf", "TapTweak", "Bech32m" verbatim (standard practice for untranslated Bitcoin protocol terms in ro content).
- "tweak"/"tweaking" (BIP-341 key tweaking) rendered as "twist-ui/'twist-uire' (tweaking)" with the English term parenthesized on first use per occurrence, since no established Romanian equivalent exists.
- "sequent calculus" → "calculul secvenților"; "sum type"/"product type" → "tip sumă"/"tip produs"; kept mathematical notation (⟦⟧, σᴸ, σᴿ, ⊢, ▵, ⨾) untouched as required.

## 2026-07-06
- "rabbit hole" (Bitcoin meme idiom) kept verbatim as an embedded English phrase in the Romanian sentence (e.g. "în călătoria ta prin rabbit hole", "am căzut în rabbit hole") — no established RO gloss found in glossary or other professor bios; other languages (e.g. si) also embed it verbatim.
- Job/role descriptors in prose bios (e.g. "Infrastructure Tech Developer") are translated naturally into Romanian rather than left verbatim, since they're plain prose, not the `author`/metadata field.
- Institution and product proper nouns (University of Nicosia, Radboud University Nijmegen, University of Waterloo, Kedge Bordeaux, Bitcoin Institute, ENS, ENC Blomet, Actu-Philosophia, Revue Conflits, Looking Glass, Bittr, Specter Wallet, Specter DIY, Blockstream, Simplicity, Liquid Network, Taproot, Tether) left untranslated verbatim.
- "signal" in "Bitcoin lessons, guides and other signal" (meaning valuable/relevant content) rendered as "conținut relevant", not a literal "semnal".
- Some "en.yml" professor bios/short_bios contain source text already in French or Spanish (e.g. `gloirekw/en.yml` short_bio "Cofondateur...", `jona-ramos/en.yml` short_bio "Me encanta Bitcoin..."). Treat these as prose to translate into Romanian like any other value — the "en.yml" filename doesn't guarantee English content.
- "sound money" left untranslated (verbatim English loanword) in `jimmy-song` bio — no established Romanian equivalent and no glossary entry found under `resources/glossary/`.
- "shitcoin(s)" kept verbatim — no `ro.md` exists yet under `resources/glossary/shitcoin/`.
- Avoid the colloquial "ca și consultant/antreprenor" construction (common but non-standard Romanian); use "ca consultant"/"ca antreprenor" without "și" before the noun.
- "Developer Advocate" (job title) kept in English, only preposition translated ("Developer Advocate la Lightning Labs") — consistent with keeping established English tech job titles verbatim.
- Typos/inconsistencies in source proper nouns (e.g. `jim/en.yml`: "Attakai" in bio vs "Attakaï" in short_bio) reproduced verbatim per field, not normalized.
