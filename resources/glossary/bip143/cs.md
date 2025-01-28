---
term: BIP143

---
Zavádí nový způsob hashování transakce pro ověření podpisu ve skriptech po zavedení SegWit. Cílem je minimalizovat nadbytečné operace při ověřování a zahrnout hodnotu UTXO na vstupu do podpisu. Tím se řeší dva hlavní problémy původního algoritmu hašování transakcí:


- Kvadratický růst hashování dat s počtem podpisů;
- Absence zahrnutí vstupní hodnoty do podpisu, což představovalo riziko pro hardwarové peněženky, zejména pokud jde o znalost vzniklých transakčních poplatků.

Vzhledem k tomu, že aktualizace SegWit, vysvětlená v BIP141, zavádí novou formu transakcí, jejichž skript nebude ověřen starými uzly, využívá BIP143 této příležitosti k řešení tohoto problému, aniž by bylo nutné provést hard fork. Proto je BIP143 součástí soft forku SegWit.