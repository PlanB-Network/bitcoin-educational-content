---
term: UTXO

---
Akronym für *Unspent Transaction Output*. Ein UTXO ist ein Transaktionsoutput, der noch nicht ausgegeben wurde, d.h. er wurde noch nicht als Input für eine neue Transaktion verwendet. UTXOs stellen den Anteil der Bitcoins dar, die ein Benutzer besitzt und die derzeit zum Ausgeben zur Verfügung stehen. Jeder UTXO ist mit einem bestimmten Ausgabeskript (`scriptPubKey`) verbunden, das die notwendigen Bedingungen zum Ausgeben der Bitcoins definiert. Transaktionen in Bitcoin verbrauchen diese UTXOs als Input und erzeugen neue UTXOs als Output. Das UTXO-Modell ist für Bitcoin von grundlegender Bedeutung, da es eine einfache Überprüfung ermöglicht, dass Transaktionen nicht versuchen, Bitcoins auszugeben, die nicht existieren oder bereits ausgegeben wurden.