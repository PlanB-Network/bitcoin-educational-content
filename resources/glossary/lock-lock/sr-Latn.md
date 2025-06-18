---
term: LOCK (.LOCK)
---

Datoteka korišćena u Bitcoin Core za zaključavanje direktorijuma sa podacima. Kreira se kada bitcoind ili Bitcoin-qt počne sa radom kako bi se sprečilo da više instanci softvera istovremeno pristupi istom direktorijumu sa podacima. Cilj je sprečiti sukobe i oštećenje podataka. Ako softver neočekivano prestane sa radom, .lock datoteka može ostati i mora se ručno obrisati pre ponovnog pokretanja Bitcoin Core.