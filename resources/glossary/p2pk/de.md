---
term: P2PK

---
P2PK steht für *Pay to Public Key*. Es ist ein Standard-Skriptmodell, das bei Bitcoin verwendet wird, um die Ausgabenbedingungen für einen UTXO festzulegen. Es ermöglicht das Sperren von Bitcoins direkt an einen öffentlichen Schlüssel, anstatt an eine Adresse.

Technisch gesehen enthält das P2PK-Skript einen öffentlichen Schlüssel und eine Anweisung, die eine entsprechende digitale Signatur verlangt, um die Gelder freizuschalten. Wenn der Besitzer die Bitcoins ausgeben möchte, muss er eine Signatur vorlegen, die mit dem zugehörigen privaten Schlüssel erstellt wurde. Diese Unterschrift wird mit dem ECDSA-Verfahren (*Elliptic Curve Digital Signature Algorithm*) überprüft. P2PK wurde in den frühen Versionen von Bitcoin häufig verwendet, insbesondere von Satoshi Nakamoto. Heute wird es fast nicht mehr verwendet.