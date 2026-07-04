# Lessons — bg

## 2026-07-03
- В SCR403/bg запазвай Simplicity термините и идентификаторите като CMR, NUMS, key-spend/key-path, Taproot, unit, sum/product, Reader/Failure/Writer, `iden`, `comp`, `case`, `pair` на английски; превеждай само околния пояснителен текст.
- За `commitment/committed` в контекста на CMR използвай „ангажимент/ангажиран“, а `Merkle root/tree` предавай като „Merkle корен/дърво“.
- При half-adder/full-adder превеждай `carry` като „пренос“ и `sum` като „сума/сумарен бит“.
- scr403 (Simplicity) established BG terms: `product` and `sum` are kept in English (often glossed as `product (двойка)` / `sum (тагнато обединение)`); `tag`→`таг`, `combinator`→`комбинатор`, combinator names (`pair`, `case`, `comp`, `take`, `drop`, `iden`, `unit`, `injl`, `injr`) verbatim.
- Composition terms: sequential→`последователна композиция`, parallel→`паралелна композиция`, conditional→`условна композиция`.
- `witness`→`свидетелски (стойности/изрази)`; `to spend/spending`→`харчене`; `prune`→`орязвам`; `on-chain` kept verbatim.
- Numbering gotcha: existing scr403 `bg.yml` quiz files were offset by one vs `en.yml` (e.g. `026/bg.yml` == `027/en.yml`). Translate strictly the `en.yml` in the SAME folder; don't trust the neighbour's number, but reuse its wording when the source text genuinely matches.
- За SCR403 на български запазвай имената на ефектите `Failure` и `Reader` на английски и ги използвай като „ефектът Failure/Reader“, съгласно вече преведения курс.
- Запазвай `Commitment Merkle Root`, `CMR`, `SimplicityHL`, `TapLeaf`, `Taproot`, `Tapscript`, `bip0340-verify`, `sig-all-hash`, `TxEnv` и `PrecomputedTransactionData` непреведени; превеждай само околния описателен текст.
- Превеждай `witness values/expressions/data` като „свидетелски стойности/изрази/данни“, а `covenants` като „covenant-и“, за консистентност с `courses/scr403/bg.md`.
- For SCR403 Bulgarian, mirror the existing course terminology: keep `unit`, `sum`, and `product` as English technical type names in Bulgarian prose (`unit тип`, `sum тип`, `product тип`) rather than translating them.
- Translate Simplicity `jets` as `джетове`, and render DAG plurals as `DAG-ове` with the expanded form `насочени ациклични графи`.
- За Simplicity материали запазвай имената на ефектите и примитивите като `Failure`, `Reader`, `Writer`, `unit`, `sum`, `product`, `witness`, `jet`/„джет“ и `CMR`, когато са термини от езика или спецификацията; превеждай само обяснителния текст около тях.
- Превеждай `witness data/expression/value` като „свидетелски данни/израз/стойност“, но оставяй `witness` непроменено, когато е име на комбинатор или част от код/стандартен термин.
- За `Commitment Merkle Root` може да се запази английският термин с абревиатурата `CMR`; при общо обяснение „ангажимент“ е подходящ превод за `commitment`.
