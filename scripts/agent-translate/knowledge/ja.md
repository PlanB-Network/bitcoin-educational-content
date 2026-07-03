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
