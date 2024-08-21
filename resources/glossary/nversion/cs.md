---
term: NVERSION
---

Pole `nVersion` v Bitcoinové transakci se používá k indikaci verze používaného formátu transakce. Umožňuje síti rozlišovat mezi různými vývojovými stádii formátu transakce v průběhu času a aplikovat odpovídající pravidla. Toto pole nemá vliv na pravidla konsensu. To znamená, že jakákoli hodnota přiřazená tomuto poli nezpůsobí neplatnost transakce. Nicméně, pole `nVersion` má pravidla standardizace, která v současnosti akceptují pouze hodnoty `1` a `2`. Zatím je toto pole užitečné pouze pro aktivaci pole `nSequence`.