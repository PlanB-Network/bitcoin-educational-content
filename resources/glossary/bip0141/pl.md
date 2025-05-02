---
term: BIP0141
---

Wprowadzono koncepcję Segregated Witness (SegWit), która dała nazwę protokołowi SegWit Soft Fork. BIP141 wprowadza istotną modyfikację do protokołu Bitcoin, mającą na celu rozwiązanie problemu podatności transakcji na manipulacje. SegWit oddziela świadka (dane podpisu) od reszty danych transakcji. Oddzielenie to osiąga się poprzez wstawienie świadków do oddzielnej struktury danych, zatwierdzonej w nowym Merkle Tree, do którego odwołuje się w bloku za pośrednictwem Coinbase Transaction, dzięki czemu SegWit jest kompatybilny ze starszymi wersjami protokołu.