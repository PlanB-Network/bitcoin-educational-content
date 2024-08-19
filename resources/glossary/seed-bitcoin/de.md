---
term: SEED (BITCOIN)
---

Im Kontext von Bitcoin ist ein Seed ein 512-Bit-Wert, der verwendet wird, um alle privaten und öffentlichen Schlüssel abzuleiten, die mit einer HD (Hierarchisch Deterministischen) Wallet verbunden sind. Technisch gesehen ist der Seed ein anderer Wert als die Wiederherstellungsphrase (oder Mnemonik). Die Phrase, die typischerweise aus 12 oder 24 Wörtern besteht, wird auf pseudo-zufällige Weise aus einer Entropiequelle generiert und durch eine Prüfsumme vervollständigt. Diese Phrase erleichtert das menschliche Backup, indem sie eine textuelle Darstellung des Werts an der Basis der Wallet bietet.

Um den eigentlichen Seed zu erhalten, wird die Wiederherstellungsphrase, möglicherweise begleitet von einer optionalen Passphrase, durch den PBKDF2-Algorithmus (*Password-Based Key Derivation Function 2*) verarbeitet. Das Ergebnis dieser Berechnung ist ein 512-Bit-Seed. Dieser Seed wird verwendet, um den Master-Schlüssel deterministisch zu generieren und dann das gesamte Schlüsselset für die HD-Wallet gemäß BIP32.

![](../../dictionnaire/assets/31.png)

> ► *Jedoch beziehen sich im allgemeinen Sprachgebrauch die meisten Bitcoin-Nutzer auf die mnemonische Phrase, wenn sie vom "Seed" sprechen, und nicht auf den Zwischenzustand der Ableitung, der zwischen der mnemonischen Phrase und dem Master-Schlüssel liegt.*