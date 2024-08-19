---
term: ÖFFENTLICHER SCHLÜSSEL
---

Der öffentliche Schlüssel ist ein Element, das in der asymmetrischen Kryptographie verwendet wird. Er wird aus einem privaten Schlüssel mittels einer irreversiblen mathematischen Funktion generiert. Bei Bitcoin werden öffentliche Schlüssel von ihrem zugehörigen privaten Schlüssel durch die digitalen Signaturalgorithmen der elliptischen Kurve ECDSA oder Schnorr abgeleitet. Im Gegensatz zum privaten Schlüssel kann der öffentliche Schlüssel frei geteilt werden, ohne die Sicherheit der Mittel zu gefährden. Innerhalb des Bitcoin-Protokolls dient der öffentliche Schlüssel als Grundlage für die Erstellung einer Bitcoin-Adresse, die dann verwendet wird, um Ausgabenbedingungen auf einem UTXO mittels eines `scriptPubKey` zu erstellen. Öffentliche Schlüssel werden oft mit dem Master-Schlüssel oder mit erweiterten Schlüsseln (xpub...) verwechselt. Diese Elemente sind jedoch ganz unterschiedlich.

> ► *Auf Englisch wird ein öffentlicher Schlüssel "public key" genannt. Dieser Begriff wird manchmal als "pubkey" oder "PK" abgekürzt.*