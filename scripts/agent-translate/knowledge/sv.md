# Lessons — sv

## 2026-07-03
- Simplicity combinator/primitive names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `and`, `xor`) stay verbatim as code identifiers — never translated or declined.
- Math notation (𝟙, 𝟚, ⟨⟩, ▵, σᴸ, σᴿ, superscripts) kept byte-identical.
- "carry bit" → "minnessiffra-biten" (adder context); "half-adder" → "halvadderare".
- "Rocq proof assistant" → "beviskontrollsystemet Rocq" (adds a generic Swedish descriptor before the proper name, kept the name itself in English/unchanged).
- "gas model" (Ethereum) → "gasmodell"; "denial-of-service via resource exhaustion" → "överbelastningsattacker via resursuttömning".
- Keep Simplicity/Bitcoin protocol jargon untranslated: "kombinator" (combinator, Swedish CS term), but "jet", "Failure effect"/"Reader effect" (as "Failure-effekten"/"Reader-effekten" with Swedish suffix -en), "case", "take"/"drop"/"iden", "covenant" (as "rekursiva covenants", per glossary `recursive-covenant` which uses "avtal"/"covenant" interchangeably but source docs favor keeping "covenant").
- "Merkle Root", "Taproot", "TapLeaf", "Tapscript", "Schnorr" stay in English per `resources/glossary/*/sv.md` convention (borrowed English terms, capitalized as proper nouns).
- "witness values" -> "vittnesvärden" (per glossary `transaction-witness` -> "vittne").
- Formal notation (⊢, ×, +, Xᑉ⁸, superscripts) copied verbatim — never touch math/type-theory symbols.
- "jets" kept as-is (untranslated technical noun, no Swedish plural suffix needed since it functions as a loanword in this domain).
- No glossary entries exist for Simplicity-specific CS/type-theory jargon (combinator, sum/product/unit type, sequent calculus). Rendered as: "kombinator", "summtyp", "produkttyp", "unit-typ", "sekvenskalkyl", "typinferens", "föravtryck" (pre-image). Kept as-is in English where Swedish CS usage typically does too: "jet", "witness", "buffer" (as "buffert"), "CMR", "TapLeaf/TapTweak/TapTree".
- Reference tables (`| Combinator | Purpose |` etc.) have their header row and prose cell values translated, but code-identifier cells (tag pre-images, CMR formulas, hex values) stay verbatim. Watch for the `|---|---|` separator row directly below the header — easy to drop by accident when swapping just the header line.
- "Failure effect" / "Reader effect" / "Writer effect" kept in English as proper names (capitalized), consistent with how "Bit Machine" is also left untranslated as a proper name.
- "block space" left untranslated (established English loanword in Swedish Bitcoin writing); "standardness" also left untranslated as a technical term with no established Swedish rendering.
- Simplicity core-combinator identifiers (`iden`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `unit`, `scribe`, `copair`, `fold-right-n`, `map`, `zip`), formal type judgements (`A × B ⊢ B × A`), and expression fragments like `case (injl iden) (injr iden)` are treated as code/notation and left byte-identical even outside fenced/inline code markup — only surrounding prose is translated.
- Domain jargon (`carry`, `jet`, `NUMS point`, `CMR`, `Reader`/`Writer`/`Failure` effects, `Bit Machine`, `key-path`/`key-spend`, `half-adder`/`full-adder`, `push-<n`/`pop-<n`, `midstate`) is kept in English inline within Swedish prose (established convention in Bitcoin/crypto Swedish technical writing); compose Swedish grammar around them with hyphenation, e.g. "carry-bitarna", "half-adderns", "key-path-signatur".
- "hand off / hand to" in a computation-trace context → "skicka vidare till"; "stage" → "steg".

## 2026-07-06
- For SOC104 Swedish political/philosophical quiz prose, render “welfare state” as “välfärdsstaten”, “fiscal system” as “skattesystemet”, and “monetary monopoly” as “det monetära monopolet”.
- Keep Cypherpunk proper-noun phrases in English when they are titles or slogans (`Cypherpunk Manifesto`, `Cypherpunks write code`), but use Swedish compounds in prose such as “Cypherpunk-sändlistan” and “cypherpunk-imperativet”.
- In this course context, render “privacy” as “privatliv” when referring to moral/political liberty, and “privacy properties” as “integritetsegenskaper” when referring to technical properties.
- In economic/political-theory quiz prose, keep "moral hazard" in English as a technical term rather than forcing "moralisk risk"; explain it in Swedish around the term.
- In political-economy quiz contexts, keep `pro-business` and `pro-market` as English loan terms and build Swedish compounds around them with hyphenation, e.g. `pro-business-positionen`, `pro-market-synen`.
- For Kant, render `minority` as `omyndighet` and `Sapere aude` as `Våga tänka själv` while keeping the Latin motto unchanged.
- Render Hayekian `spontaneous order` as `spontan ordning`; use `central planering` for `central planning`.
- Political-family term "libertarian" kept as the Swedish loanword "libertarian"/"libertarianer"; French *libertaire* kept verbatim and contrasted explicitly with Swedish prose.
- In political-philosophy passages, "constructivism" kept as the established loanword "constructivism" rather than localizing to "konstruktivism", to preserve the Hayekian term used by the source.
- Bitcoin/cypherpunk jargon follows the Swedish glossary for linked terms: `cryptocurrency` → "Kryptovaluta", `peertopeer-p2p` → "P2P (Peer-to-peer)", `foss` → "FOSS", `white-paper` → "Vitbok", `cryptography` → "Kryptografi"; unlinked established terms like "sound money" and "Genesis block" can remain English loanwords.
- In Swedish political-economy prose, render "free-market" compounds as Swedish compounds where natural: "frimarknadsprinciper", "frimarknadssystemet", "frimarknadsideologi".
- "crony capitalism" can be translated as "svågerkapitalism" in non-Bitcoin political theory contexts.
- In SOC/political-philosophy material, keep named US institutions and parties in English (`Cato Institute`, `Mises Institute`, `Libertarian Party`) and add Swedish grammar around them rather than translating the names.
- Render `statism` as `statism`/`statistisk` in Swedish political-philosophy context.
- Keep Hayek’s term `spontaneous order` in English when presented as a named concept; translate the surrounding explanation as `spontan ordning` only if the source is not naming the concept.
- In political-philosophy context, distinguish French socialist-anarchist “libertaires” as “libertärer” from Anglophone/free-market “libertarians” as “libertarianer”; use derived forms “libertärerna” and “libertarianska” where Swedish grammar requires it.
- “spoliation” in Bastiat/Friedman redistribution context rendered as “plundring” rather than a legalistic “expropriation,” preserving the moral-economics sense.
- Nolan diagram/diamond -> "Nolan-diagrammet"/"Nolan-diamanten".
- Political-theory terms used here: "statism" -> "etatism", "anarcho-capitalists" -> "anarkokapitalister", "minarchists" -> "minarkister".
