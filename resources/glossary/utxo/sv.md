---
term: UTXO
definition: Ospenderad transaktionsoutput som representerar en del av bitcoins som är tillgängliga för att användas som input.
---

Akronym för *Unspent Transaction Output*. En UTXO är en transaktionsutgång som ännu inte har spenderats, vilket innebär att den inte har använts som input för en ny transaktion. UTXO:er representerar den del av bitcoins som en användare äger och som för närvarande är tillgängliga för att spenderas. Varje UTXO är associerad med ett specifikt utdataskript (`scriptPubKey`), som definierar de nödvändiga villkoren för att spendera bitcoins. Transaktioner i Bitcoin konsumerar dessa UTXO:er som input och skapar nya UTXO:er som output. UTXO-modellen är grundläggande för Bitcoin, eftersom den gör det möjligt att enkelt verifiera att transaktioner inte försöker spendera bitcoins som inte existerar eller redan har spenderats.