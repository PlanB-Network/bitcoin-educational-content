---
term: TXID (TRANSAKTIONSBEZEICHNER)

---
Eine eindeutige Kennung, die mit jeder Bitcoin-Transaktion verbunden ist. Sie wird durch die Berechnung des `SHA256d`-Hashes der Transaktionsdaten erzeugt. Die TXID dient als Referenz, um eine bestimmte Transaktion in der Blockchain zu finden. Sie wird auch verwendet, um auf eine UTXO zu verweisen, die im Wesentlichen aus der Verkettung der TXID einer früheren Transaktion und dem Index des vorgesehenen Ausgangs (auch "vout" genannt) besteht. Bei Post-SegWit-Transaktionen berücksichtigt die TXID nicht mehr den Transaktionszeugen, was die Verfälschbarkeit ausschließt.