---
term: WALLET FOOTPRINT
---

Sada charakteristických rysů pozorovatelných v transakcích prováděných stejnou Bitcoinovou peněženkou. Tyto charakteristiky mohou zahrnovat podobnosti ve využívání typů skriptů, opětovné použití adres, pořadí UTXO, umístění výstupů pro změnu, signalizaci RBF (*Replace-by-Fee*), číslo verze, pole `nSequence` a pole `nLockTime`.

Stopy peněženek jsou využívány analytiky k sledování aktivit konkrétní entity na blockchainu identifikací opakujících se vzorců v jejích transakcích. Například uživatel, který systematicky posílá svou změnu na adresy P2TR (`bc1p…`), vytváří charakteristickou stopu, která může být použita k sledování jeho budoucích transakcí.

Jak vysvětluje LaurentMT v Space Kek #19 (francouzsky mluvící podcast), užitečnost stop peněženek v analýze řetězců výrazně roste s časem. Skutečně, rostoucí počet typů skriptů a postupné zavádění těchto nových funkcí softwary peněženek zvýrazňuje rozdíly. Je dokonce možné přesně identifikovat software používaný sledovanou entitou. Proto je důležité pochopit, že studium stopy peněženky je zvláště relevantní pro nedávné transakce, více než pro ty, které byly zahájeny na počátku 2010s.