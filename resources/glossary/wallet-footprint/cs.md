---
term: OTISK PENĚŽENKY

---
Soubor charakteristických znaků pozorovatelných u transakcí provedených stejnou peněženkou Bitcoin. Tyto charakteristiky mohou zahrnovat podobnosti v použití typů skriptů, opakovaném použití adres, pořadí UTXO, umístění výstupů změn, signalizaci RBF (*Replace-by-Fee*), číslo verze, pole `nSequence` a pole `nLockTime`.

Stopy peněženek využívají analytici ke sledování aktivit konkrétního subjektu v blockchainu tím, že identifikují opakující se vzorce v jeho transakcích. Například uživatel, který systematicky posílá své drobné na adresy P2TR (`bc1p...`), vytváří charakteristický otisk, který lze použít ke sledování jeho budoucích transakcí.

Jak vysvětluje LaurentMT ve Space Kek #19 (francouzsky mluvící podcast), užitečnost otisků peněženek při analýze řetězců se v čase výrazně zvyšuje. Rostoucí počet typů skriptů a stále postupnější zavádění těchto nových funkcí softwarem peněženek totiž rozdíly zvýrazňuje. Dokonce je možné přesně identifikovat software používaný sledovaným subjektem. Proto je důležité si uvědomit, že studium otisku peněženky je relevantní zejména pro nedávné transakce, a to více než pro transakce iniciované na počátku roku 2010.