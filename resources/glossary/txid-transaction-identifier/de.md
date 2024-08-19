---
term: TXID (TRANSACTION IDENTIFIER)
---

Ein einzigartiger Identifikator, der mit jeder Bitcoin-Transaktion verbunden ist. Er wird generiert, indem der `SHA256d` Hash der Transaktionsdaten berechnet wird. Der TXID dient als Referenz, um eine spezifische Transaktion innerhalb der Blockchain zu finden. Er wird auch verwendet, um auf ein UTXO zu verweisen, was im Wesentlichen die Verkettung des TXID einer vorherigen Transaktion und des Index des bestimmten Outputs (auch "vout" genannt) ist. Für Transaktionen nach SegWit berücksichtigt der TXID nicht mehr den Transaktionszeugen, was die Veränderlichkeit eliminiert.