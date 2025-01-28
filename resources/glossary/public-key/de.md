---
term: PUBLIC KEY

---
Der öffentliche Schlüssel ist ein Element, das in der asymmetrischen Kryptographie verwendet wird. Er wird aus einem privaten Schlüssel mit Hilfe einer irreversiblen mathematischen Funktion erzeugt. Bei Bitcoin werden öffentliche Schlüssel von ihrem zugehörigen privaten Schlüssel durch die digitalen Signaturalgorithmen der elliptischen Kurve ECDSA oder Schnorr abgeleitet. Im Gegensatz zum privaten Schlüssel kann der öffentliche Schlüssel frei weitergegeben werden, ohne die Sicherheit des Geldes zu gefährden. Innerhalb des Bitcoin-Protokolls dient der öffentliche Schlüssel als Grundlage für die Erstellung einer Bitcoin-Adresse, die dann verwendet wird, um mit einem `scriptPubKey` Ausgabenbedingungen für einen UTXO zu schaffen. Öffentliche Schlüssel werden oft mit dem Master Key oder mit erweiterten Schlüsseln (xpub...) verwechselt. Diese Elemente sind jedoch völlig unterschiedlich.

> ► *Im Englischen wird ein öffentlicher Schlüssel "public key" genannt Dieser Begriff wird manchmal mit "pubkey" oder "PK" abgekürzt