---
term: P2PK
---

P2PK steht für *Pay to Public Key*. Es handelt sich um ein standardisiertes Skriptmodell, das bei Bitcoin verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen. Es ermöglicht das Sperren von Bitcoins direkt auf einen öffentlichen Schlüssel, anstatt auf eine Adresse.
Technisch enthält das P2PK-Skript einen öffentlichen Schlüssel und eine Anweisung, die eine entsprechende digitale Signatur verlangt, um die Mittel freizugeben. Wenn der Besitzer die Bitcoins ausgeben möchte, muss er eine Signatur vorlegen, die mit dem zugehörigen privaten Schlüssel erzeugt wurde. Diese Signatur wird mit dem ECDSA (*Elliptic Curve Digital Signature Algorithm*) verifiziert. P2PK wurde oft in den frühen Versionen von Bitcoin verwendet, insbesondere von Satoshi Nakamoto. Heute wird es fast nicht mehr verwendet.