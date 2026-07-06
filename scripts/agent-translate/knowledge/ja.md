# Lessons — ja

## 2026-07-03
- In Simplicity material, keep algebraic/effect names such as `Failure effect`, `Reader effect`, `State effect`, `Writer effect`, and `Continuation effect` as English term + 「エフェクト」 (e.g. `Failure エフェクト`) rather than translating the names.
- Keep `Commitment Merkle Root (CMR)` in English with the acronym; translate generic `Merkle root` as 「マークルルート」 when it is not the formal CMR name.
- For Simplicity identifiers and jets (`take`, `drop`, `iden`, `bip0340-verify`, `sig-all-hash`, `TxEnv`, `PrecomputedTransactionData`), keep the identifier verbatim and translate only the surrounding explanation.
- Use glossary canonical 「シュノア」 for Schnorr in Japanese (`シュノア署名`) even when nearby source text keeps the English `Schnorr`.
- Simplicityの型用語は、sum type＝「和型」、product type＝「積型」、unit type＝「unit型」、combinator＝「コンビネータ」で統一する。
- Simplicityの識別子（iden、unit、comp、pair、case、take、drop、injl、injr、scribe、and、xor）と真理値リテラル（false/true）は翻訳せず、そのまま保持する。
- directed acyclic graphは既存用語に合わせて「有向非巡回グラフ」とし、略語がある場合は「有向非巡回グラフ（DAG）」と表記する。
- Simplicityのjetは固有技術用語として「jet」のまま保持し、「ジェット」と片仮名化しない。
- Simplicity combinator names (`take`, `drop`, `iden`, `comp`, `pair`, `case`, `injl`, `injr`) and the word "witness" stay verbatim English inside Japanese prose; surround them with spaces (e.g. `take コンビネータ`, `witness 値`).
- Established scr403 renderings: product type = 積型 / 積, sum type = 和型 / 和, combinator = コンビネータ, parallel composition = 並列合成, conditional composition = 条件付き合成, sequential composition = 逐次合成, dual = 双対, prune = 刈り取る, tag = タグ. "Commitment Merkle Root (CMR)" kept English as `Commitment Merkle Root（CMR）`.
- In `>-` folded scalars YAML folds each newline into a space, so break lines only right after 。/、 or immediately before/after an ASCII token — never between two kana/kanji, or a stray space appears mid-word.
- If a YAML quiz value would begin with a single-quote token (e.g. the question about `'take'`), wrap the whole value in double quotes so it isn't parsed as a quoted scalar.
- Simplicity の式・プリミティブ名（`case`, `iden`, `take`, `drop`, `pair`, `injl`, `injr`, `comp`, `unit`, `scribe` など）と記号式は翻訳せず、周辺の説明だけを日本語化する。
- Simplicity 固有の “jet” は「jet」を保持し、必要に応じて「jet になる」「単一の jet」のように日本語の助詞で接続する。
- “unitary/unitarity” は効果の文脈では「単位的/単位性」と訳す。
- Taproot 用語は既存 glossary に合わせ、「内部キー」「鍵パス」「スクリプトパス」「シュノア署名」を使い、`key-spend` は文脈上「鍵支出」と訳す。
- Simplicity関連の日本語では、プロトコル名・実装名・識別子（Simplicity、Taproot、CMR、jets、witness、SIGHASH_ALL、`PrecomputedTransactionData`など）は英字のまま保持し、説明語だけを日本語化する。
- Type theory用語は「combinator→コンビネータ」「sum type→和型」「product type→積型」「unit type→unit型」「sequent calculus→シークエント計算」を使う。
- Failure/Reader/Writerは効果名として英字を保持し、「Failureエフェクト」「Readerエフェクト」の形で訳す。

## 2026-07-06
- SOC/Nolan diagram material: render `Nolan diagram` as 「ノーラン・チャート」 and `Nolan diamond` as 「ノーランのダイヤモンド」.
- Political philosophy terms: use 「古典的自由主義」 for classical liberalism, 「リバタリアニズム」 for libertarianism, 「リバタリアン」 for libertarians, 「国家主義」 for statism.
- For `fiat money/currency`, follow glossary canonical 「法定通貨 (Fiat)」 on first mention and 「法定通貨 (Fiat)」 or 「法定通貨」 as context requires.
- Political-spectrum terms in this course: render `statism/statist` as 「国家統制主義／国家統制主義者」 to avoid confusion with nationalism, and `centrism/centrist` as 「中道主義／中道主義者」.
- Keep the French distinction in the libertarian chapter explicit: `libertarian` = 「リバタリアン」, French `libertaire` = 「リベルテール」, and `libertine` = 「リベルタン」.
- For Hayek/Rothbard vocabulary, use 「自生的秩序」 for `spontaneous order`, 「構成主義」 for `constructivism`, 「不可侵原則」 for `non-aggression principle`, and 「自己所有権」 for `self-ownership`.
- In SOC104 Japanese, keep the existing rendering `minarchist` = 「ミナキスト」 and `anarcho-capitalist` = 「無政府資本主義者」.
- Render `non-aggression principle` as 「不可侵原則」 in libertarian political-philosophy contexts.
- For centrism material, use 「企業寄り」 for `pro-business` and 「市場寄り」 for `pro-market`, matching the course’s distinction between state-corporate alliance and free competition.
- In SOC104, distinguish French socialist-anarchist `libertaires` as 「リベルテール」 from American/market `libertarians` as 「リバタリアン」/「リバタリアニズム」.
- Translate `spoliation` in Bastiat/Friedman policy critiques as 「収奪」, not generic 「搾取」, to preserve the legal-political sense of taking property by force.
- Use standard Japanese political-philosophy terms: `utopian socialism`＝「空想的社会主義」, `scientific socialism`＝「科学的社会主義」, `historical materialism`＝「史的唯物論」, `class struggle`＝「階級闘争」.
- In SOC104 political-family material, keep the course’s existing Japanese renderings: totalitarianism＝「全体主義」, statism＝「国家統制主義」, conservatism＝「保守主義」, libertarian/libertarianism＝「リバタリアン／リバタリアニズム」, centrism＝「中道主義」.
- For SOC104 economic/social debate terms, use 「指令経済」 for directed economy, 「世俗宗教」 for secular religions, 「モラルハザード」 for moral hazard, and 「砂糖入り飲料」 for sugary drinks.
- In Nolan-chart/social-control contexts, render `statism` as 「国家統制主義」 and `statist` as 「国家統制主義者」 to avoid the nationalist sense of 「国家主義」.
- For libertarianism variants, use 「リバタリアン」, 「リバタリアニズム」, 「パレオ・リバタリアニズム」, and 「ネオ・リバタリアニズム」.
- In U.S. politics material, translate `states' rights` as 「州権」 and `federal states`/`states` in federalism contexts as 「州」.
- In SOC104 political-philosophy quizzes, follow the existing course renderings: spontaneous order = 「自生的秩序」, constructed order = 「構成された秩序」, constructivism = 「構成主義」.
- Render pro-business / pro-market consistently as 「企業寄り」/「市場寄り」, matching existing SOC104 Japanese phrasing.
- For Popper, use 「開かれた社会」/「閉じた社会」 and keep 「共同体的保護」「コミュニタリアン的衝動」 for communal/communitarian vulnerability language.
- For SOC104 political material, use existing Japanese course/glossary renderings: `Cypherpunk(s)` → 「サイファーパンク」 in prose, but keep the proper list name as `Cypherpunk メーリングリスト` when source capitalizes it as a title.
- Render `fiat currency/money` as 「法定通貨」, `welfare state` as 「福祉国家」, and `libertarian(s)` as 「リバタリアン」.
- For Hayek/political theory terms in SOC104, use `constructivism` → 「構成主義」 and `spontaneous market order` → 「自生的な市場秩序」.
