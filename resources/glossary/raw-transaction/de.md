---
term: ROHTRANSAKTION
---

Eine Bitcoin-Transaktion, die erstellt und signiert wurde und in ihrer binären Form existiert. Eine Rohtransaktion (*raw TX*) ist die endgültige Darstellung einer Transaktion, kurz bevor sie im Netzwerk verbreitet wird. Diese Transaktion enthält alle notwendigen Informationen für ihre Aufnahme in einen Block:
* Die Version;
* Das Flag;
* Die Eingaben;
* Die Ausgaben;
* Die Sperrzeit;
* Der Zeuge.

Was als "*Rohtransaktion*" bezeichnet wird, repräsentiert die rohen Daten, die zweimal durch die SHA256-Hashfunktion geleitet werden, um die Transaktions-ID (TXID) der Transaktion zu generieren. Diese Daten werden dann im Merkle-Baum des Blocks verwendet, um die Transaktion in die Blockchain zu integrieren.

> ► *Dieses Konzept wird manchmal auch als "Serialisierte Transaktion" bezeichnet. Auf Französisch könnten diese Begriffe jeweils als "transaction brute" und "transaction sérialisée" übersetzt werden.*