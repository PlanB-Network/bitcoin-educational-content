# Lessons — fi

## 2026-07-03
- Simplicity term rendering (from `courses/scr403/fi.md`): `combinator`→kombinaattori (core→ydinkombinaattori), `jet`→jetti, `carry bit`→muistibitti, `sum bit`→summabitti, `sum/product/unit type`→summa-/tulo-/yksikkötyyppi, `buffer`→puskuri, `side effect`→sivuvaikutus, `completeness theorem`→täydellisyyslause, `lookup table`→hakutaulu, `premise/conclusion`→premissi/johtopäätös.
- Keep English verbatim: `half-adder`/`full-adder`, `Bit Machine`, effect names `Failure`/`Reader`/`Writer` (+`-sivuvaikutus`), `Taproot`, `CMR`, `witness`, `Rocq`, `SimplicityHL`, `NUMS`-piste (leave the acronym gloss 'Nothing-Up-My-Sleeve' untranslated), combinator/jet identifiers (`iden`, `comp`, `scribe`, `bip0340-verify`, `sig-all-hash`, etc.).
- Attach Finnish case endings to code/identifier tokens with a colon so the token stays intact: `push-<n:n`, `pop-<n:lle`, `CMR:ään`/`CMR:istä`, `SimplicityHL:n`, `f:ltä`, `g:lle`, `OR:n`, `XOR:ää`; hyphen when the base is vowel-final (`push-lle`). Backtick-wrapped tokens: put the suffix after the closing backtick (`` `bip0340-verify` ``-kutsun).
- Taproot/commitment vocabulary: `prune`→karsia, `verifier`→varmentaja, `spender`→kuluttaja, `commitment`→sitoumus, `committed`→sidottu, `on-chain`→lohkoketjuun, `Merkle root/tree`→Merkle-juuri/-puu, `key-path spend`→avainpolkukulutus, `script path`→skriptipolku, `internal key`→sisäinen avain, `discrete log`→diskreetti logaritmi, `midstate`→välitila.
- Quiz YAML quoting: only double-quote a `question`/`answer`/`wrong_answers` value when it contains a colon-space (`": "`) at top level (e.g. after `unitaarinen:` or a leading `#ᶜ(...)` line); values with only in-token colons (`CMR:t`, `push-<n:n`) or semicolons stay unquoted, matching the EN source's quoting.
- Simplicity type-theory terms: `sum type` → summatyyppi, `product type` → tulotyyppi (math "tulo" = product), `unit type` → yksikkötyyppi, `boolean type` → totuusarvotyyppi, `tagged union` → tunnistettu unioni. Keep consistent within a file.
- Keep all combinator names verbatim (iden, unit, comp, pair, case, take, drop, injl, injr) and inflect surrounding Finnish, e.g. "comp-kombinaattori", "take iden poimii". `combinator` → kombinaattori; `accessor/extractor` → poimija.
- Protocol/proper names stay English: Simplicity, Bitcoin Script, Liquid Network, Ethereum, Merkle (→ Merkle-juuri), Rocq (→ Rocq-todistusassistentti), SHA-256, DAG (inflect as DAG:eina).
- `jet`/`jets` → jet / jetit (treat as a loaned Finnish noun, inflect normally: jetien, jeteillä).
- Domain vocab: `hash` → tiiviste, `half-adder` → puolisummain, `carry (bit)` → muistibitti, `sum bit` → summabitti, `gas model` → kaasumalli, `denial-of-service` → palvelunestohyökkäys, `lookup table` → hakutaulu, `empty tuple` → tyhjä monikko, `power-of-two` → kahden potenssi, `left/right-tagged` → vasemmalle/oikealle merkitty.
- Quiz answers/wrong_answers are noun phrases completing "What does X produce/compute?"; render as Finnish partitive/genitive object phrases (e.g. "Yhden yhdistetyn operaation…") to stay grammatical, not full sentences.
- Simplicityn ydintermit: käytä `kombinaattori`, `kompositio`, `summatyyppi`, `tulotyyppi` ja `yksikkötyyppi`; pidä itse kombinaattorien nimet (`iden`, `unit`, `case`, jne.) aina englanninkielisinä.
- Käsittele `Failure`, `Reader` ja `Writer` nimettyinä vaikutuksina: sujuva muoto on `Failure-vaikutus`, `Reader-vaikutus`, `Writer-vaikutus`; yleinen `side effect` on `sivuvaikutus`.
- Bitcoin/Simplicity-kontekstissa `witness` kannattaa pitää teknisenä lainaterminä yhdyssanoissa (`witness-data`, `witness-lauseke`, `witness-arvo`), jotta se ei sekoitu yleiskielen todistajaan.
- Pidä vakiintuneet protokolla- ja sovellustermit kuten `Taproot`, `Simplicity`, `Liquid Network`, `jet`, `CMR`, `key-spend`, `on-chain` ja `off-chain` pääosin englanniksi; taivuta ne tarvittaessa suomen yhdyssanasäännöillä.
- Named computational effects: render as `<Name>-efekti`, keeping the English effect name verbatim (Failure-efekti, Reader-efekti, State-efekti, IO-efekti). Generic "side effect" → `sivuvaikutus`.
- `witness` → `todistaja` (per glossary `transaction-witness`); "witness values" → `todistaja-arvot`, "witness expressions" → `todistaja-lausekkeet`.
- Simplicity/Bitcoin code identifiers stay verbatim: `case`, `iden`, `take`, `drop`, `O`/`I`/`H`, `bip0340-verify`, `sig-all-hash`, `TxEnv`, `PrecomputedTransactionData`, `CMR`, `TapLeaf`, `0xbe`, `SimplicityHL`. Proper names kept: `Bit Machine`, `Curry-Howard`, `De Bruijn`, `Gentzen`, `Taproot`, `Tapscript`, `Schnorr`.
- Standard FP/crypto renderings used consistently: `combinator` → kombinaattori; `jet` → jet (pl. jetit); `hash` (noun) → tiiviste, (verb) → tiivistää; `sum/product` types → summatyyppi/tulo; `tagged` → tunnisteellinen; `batch verification` → eräverifiointi; `boolean` → totuusarvo; `scope` → näkyvyysalue.
- `recursive covenant` → `rekursiivinen covenant` / pl. `rekursiiviset covenantit` (glossary term keeps English "covenant").

## 2026-07-06
- Political-philosophy terms in SOC104: `statism` → `etatismi`, `statist` → `etatisti`; `libertarian` → `libertaristi`, `libertarianism` → `libertarismi`.
- Render subtypes as compounds: `paleo-libertarianism` → `paleolibertarismi`, `neo-libertarianism` → `neolibertarismi`.
- Hayek's `spontaneous order` → `spontaani järjestys`; keep institutional names such as `Cato Institute`, `Mises Institute`, and `Libertarian Party` in English and inflect the surrounding Finnish.
- In Nolan/political-compass prose, `sensibilities` works naturally as `arvomaailma` when it means values/preferences someone wants to impose via the state.
- Political-spectrum terms in SOC/Nolan contexts: `left-right axis/divide` → `vasemmisto–oikeisto-akseli/-jako`; `Nolan diagram` → `Nolanin kaavio`, but `Nolan diamond` → `Nolanin timantti`.
- Libertarian terminology: `libertarianism` → `libertarismi`, adjective/group forms → `libertaari/libertaarinen`; `anarcho-capitalists` → `anarkokapitalistit`; `minarchists` → `minarkistit`.
- `statism/statists` in political-theory quiz prose can be rendered as `etatismi/etatistit` when contrasting with libertarianism; keep it consistent within the file.
- SOC/political-theory quizzes: render `libertarian(s)` as `libertaari(t)` / `libertaarinen`, `centrist(s)` as `keskustalainen/keskustalaiset` when used as a generic political family, not as a party label.
- Economics term `moral hazard` → `moraalikato` in subsidy/bailout contexts.
- `secular religion(s)` in totalitarianism context → `maallinen uskonto` / `maalliset uskonnot`; `single-party rule` → `yksipuoluevalta`.
- SOC/poliittisen filosofian perustermeissä käytä `libertarian` → `libertaari`/`libertaarinen`, `centrist` → `sentristi`/`sentristinen`, `constructivism` → `konstruktivismi`, `spontaneous order` → `spontaani järjestys`, `central planning` → `keskussuunnittelu`.
- `pro-business`/`pro-market`-vastakkainasettelu kannattaa kääntää `yritysmyönteinen`/`markkinamyönteinen`, jotta ero tiettyjen yritysten suojelemisen ja markkinaprosessin puolustamisen välillä säilyy.
- Kantin `minority` (*Sapere aude*) → `alaikäisyys`; moton selitys `Dare to think for yourself` → `Uskalla ajatella itse`.
- In soc/political theory quizzes, distinguish French socialist-anarchist `libertaires` as `libertairet` from English/American libertarians as `libertaarit`; `libertarianism` → `libertarismi`.
- Political philosophy terms: `libertarian` → `libertaari`, `libertarianism` → `libertarismi`, `minarchist` → `minarkisti`, `anarcho-capitalist` → `anarkokapitalisti`.
- Libertarian ethics: `non-aggression principle` → `hyökkäämättömyysperiaate`, `self-ownership` → `itseomistus`.
- Ideology terms in SOC quizzes: `centrism` → `keskustalaisuus`, `technocracy` → `teknokratia`, `public utility` → `julkinen hyöty`.
- Market-policy contrast: `pro-business` → `yritysmyönteisyys`, `pro-market` → `markkinamyönteisyys`.
- Monetary terms: keep `Federal Reserve` in English; `sound money` → `terve raha`, `gold standard` → `kultakanta`.
- SOC/cypherpunk quizzes: keep exact historical strings and slogans verbatim inside quotes when they identify canonical artifacts, e.g. the Genesis block headline `"The Times 03/Jan/2009 Chancellor on the brink of a second bank bailout."` and `"Cypherpunks write code"`; translate only the surrounding prose.
- Use glossary-backed forms `Cypherpunkit` for the community and `Fiat` as the term; in prose, `cypherpunkit`, `Cypherpunk-...`, `fiat-valuutta` and `fiat-raha` read naturally.
- Political vocabulary used here: `libertarian` → `libertaari`/`libertaarinen`, `constructivism` → `konstruktivismi`, `welfare state` → `hyvinvointivaltio`, `consent` → `suostumus`.
