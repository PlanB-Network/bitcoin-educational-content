---
term: NVERSION

---
Pole `nVersion` v transakci Bitcoinu slouží k označení použité verze formátu transakce. Umožňuje síti rozlišovat mezi různými vývojovými verzemi formátu transakce v průběhu času a uplatňovat odpovídající pravidla. Toto pole nemá žádný vliv na pravidla konsensu. To znamená, že jakákoli hodnota přiřazená tomuto poli nemá za následek zneplatnění transakce. Pole `nVersion` má však standardizační pravidla, která v současné době akceptují pouze hodnoty `1` a `2`. Prozatím je toto pole užitečné pouze pro aktivaci pole `nSequence`.