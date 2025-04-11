---
term: P2PKH

---
P2PKH steht für *Pay to Public Key Hash*. Es handelt sich dabei um ein Standard-Skriptmodell, das verwendet wird, um Ausgabenbedingungen für einen UTXO festzulegen. Es ermöglicht das Sperren von Bitcoins auf einen Hash eines öffentlichen Schlüssels, d.h. auf eine Empfängeradresse. Dieses Skript ist mit dem Legacy-Standard verbunden und wurde in den frühen Versionen von Bitcoin von Satoshi Nakamoto eingeführt.

Im Gegensatz zu P2PK, bei dem der öffentliche Schlüssel ausdrücklich im Skript enthalten ist, verwendet P2PKH einen kryptografischen Fingerabdruck des öffentlichen Schlüssels. Dieses Skript enthält den `RIPEMD160`-Hash des `SHA256` des öffentlichen Schlüssels und legt fest, dass der Empfänger einen öffentlichen Schlüssel, der mit diesem Hash übereinstimmt, sowie eine gültige digitale Signatur, die aus dem zugehörigen privaten Schlüssel generiert wurde, vorlegen muss, um auf das Geld zuzugreifen. P2PKH-Adressen werden mit dem Format "Base58Check" kodiert, das ihnen durch die Verwendung einer Prüfsumme Robustheit gegenüber Tippfehlern verleiht. Diese Adressen beginnen immer mit der Zahl "1".