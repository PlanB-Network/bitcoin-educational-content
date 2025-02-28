---
term: ROHTRANSAKTION

---
Eine Bitcoin-Transaktion, die erstellt und signiert wurde und in ihrer binären Form vorliegt. Eine Rohtransaktion (*raw TX*) ist die endgültige Darstellung einer Transaktion, kurz bevor sie an das Netzwerk gesendet wird. Diese Transaktion enthält alle notwendigen Informationen für ihre Aufnahme in einen Block:


- Die Version;
- Die Flagge;
- Die Eingaben;
- Die Ergebnisse;
- Die Sperrzeit;
- Der Zeuge.

Eine so genannte "*Raw-Transaktion*" besteht aus den Rohdaten, die zweimal durch die SHA256-Hash-Funktion geleitet werden, um die TXID der Transaktion zu generieren. Diese Daten werden dann im Merkle-Baum des Blocks verwendet, um die Transaktion in die Blockchain zu integrieren.

> ► *Dieses Konzept wird manchmal auch als "Serialized Transaction" bezeichnet. Im Französischen könnten diese Begriffe mit "transaction brute" bzw. "transaction sérialisée" übersetzt werden.*