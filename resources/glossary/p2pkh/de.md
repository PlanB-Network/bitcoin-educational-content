---
term: P2PKH
---

P2PKH steht für *Pay to Public Key Hash*. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen. Es ermöglicht das Sperren von Bitcoins auf einem Hash eines öffentlichen Schlüssels, das heißt, auf einer Empfangsadresse. Dieses Skript ist mit dem Legacy-Standard verbunden und wurde in den frühen Versionen von Bitcoin von Satoshi Nakamoto eingeführt.

Im Gegensatz zu P2PK, wo der öffentliche Schlüssel explizit im Skript enthalten ist, verwendet P2PKH einen kryptografischen Fingerabdruck des öffentlichen Schlüssels. Dieses Skript beinhaltet den `RIPEMD160`-Hash des `SHA256` des öffentlichen Schlüssels und legt fest, dass der Empfänger, um auf die Mittel zugreifen zu können, einen öffentlichen Schlüssel vorlegen muss, der mit diesem Hash übereinstimmt, sowie eine gültige digitale Signatur, die mit dem zugehörigen privaten Schlüssel generiert wurde. P2PKH-Adressen werden unter Verwendung des `Base58Check`-Formats kodiert, was ihnen durch die Verwendung einer Prüfsumme Robustheit gegenüber Tippfehlern verleiht. Diese Adressen beginnen immer mit der Zahl `1`.