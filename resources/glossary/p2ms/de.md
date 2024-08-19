---
term: P2MS
---

P2MS steht für *Pay to Multisig*, was "Zahlung an mehrere Signaturen" bedeutet. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen. Es ermöglicht das Sperren von Bitcoins mit mehreren öffentlichen Schlüsseln. Um diese Bitcoins auszugeben, wird eine Signatur mit einer vordefinierten Anzahl von zugehörigen privaten Schlüsseln benötigt. Zum Beispiel erfordert ein `P2MS 2/3` `3` öffentliche Schlüssel mit `3` zugehörigen geheimen privaten Schlüsseln. Um die mit diesem P2MS-Skript gesperrten Bitcoins auszugeben, wird eine Signatur mit mindestens `2` aus den `3` privaten Schlüsseln benötigt. Dies ist ein Schwellenwertsicherheitssystem.

Dieses Skript wurde 2011 von Gavin Andresen erfunden, als er die Wartung des Haupt-Bitcoin-Clients übernahm. Heute wird P2MS nur noch am Rande von einigen Anwendungen genutzt. Die überwiegende Mehrheit der modernen Multisignaturen verwendet andere Skripte wie P2SH oder P2WSH. Im Vergleich dazu ist P2MS extrem trivial. Die öffentlichen Schlüssel, aus denen es besteht, werden bei Erhalt der Transaktion offenbart. Die Verwendung eines P2MS ist auch teurer als andere Multisignaturskripte.

> ► *P2MS werden oft als "bare-multisig" bezeichnet, was als "nackte Multisignatur" oder "rohe Multisignatur" übersetzt werden könnte. Anfang 2023 standen P2MS-Skripte im Mittelpunkt einer Kontroverse aufgrund ihres Missbrauchs innerhalb des Stamps-Protokolls. Ihr Einfluss auf den UTXO-Satz wurde besonders hervorgehoben.*