---
term: SEED (BITCOIN)

---
Im Kontext von Bitcoin ist ein Seed ein 512-Bit-Wert, der verwendet wird, um alle privaten und öffentlichen Schlüssel abzuleiten, die mit einer HD (Hierarchical Deterministic) Wallet verbunden sind. Technisch gesehen ist der Seed ein anderer Wert als die Recovery Phrase (oder Mnemonic). Die Phrase, die in der Regel aus 12 oder 24 Wörtern besteht, wird pseudozufällig aus einer Entropiequelle erzeugt und durch eine Prüfsumme ergänzt. Diese Phrase erleichtert die Sicherung durch den Menschen, indem sie eine textuelle Darstellung des Wertes in der Basis der Brieftasche liefert.

Um den eigentlichen Seed zu erhalten, wird die Wiederherstellungsphrase, möglicherweise zusammen mit einer optionalen Passphrase, durch den PBKDF2-Algorithmus (*Password-Based Key Derivation Function 2*) verarbeitet. Das Ergebnis dieser Berechnung ist ein 512-Bit-Seed. Dieser Seed wird zur deterministischen Generierung des Hauptschlüssels und dann des gesamten Schlüsselsatzes für die HD-Wallet gemäß BIP32 verwendet.

![](../../dictionnaire/assets/31.webp)

> im allgemeinen Sprachgebrauch beziehen sich die meisten Bitcoiner jedoch auf die mnemonische Phrase, wenn sie vom "Seed" sprechen, und nicht auf den Zwischenzustand der Ableitung, der zwischen der mnemonischen Phrase und dem Master Key liegt