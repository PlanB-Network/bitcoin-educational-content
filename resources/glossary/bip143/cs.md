---
term: BIP143
---

Představuje nový způsob hashování transakce pro ověření podpisu v post-SegWit skriptech. Cílem je minimalizovat redundantní operace během ověřování a zahrnout hodnotu UTXO na vstupu do podpisu. To řeší dva hlavní problémy s původním algoritmem hashování transakcí:
* Kvadratický růst hashování dat s počtem podpisů;
* Absence zahrnutí hodnoty vstupu v podpisu, což představovalo riziko pro hardwarové peněženky, zejména pokud jde o znalost transakčních poplatků.
Od aktualizace SegWit, vysvětlené v BIP141, která představuje novou formu transakcí, jejichž skript nebude ověřen starými uzly, BIP143 využívá této příležitosti k řešení tohoto problému bez nutnosti tvrdého forku. Proto je BIP143 součástí měkkého forku SegWit.