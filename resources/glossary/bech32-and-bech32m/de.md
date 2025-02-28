---
term: BECH32 UND BECH32M

---
bech32" und "Bech32m" sind zwei Adresskodierungsformate für den Empfang von Bitcoins. Sie basieren auf einer leicht modifizierten Basis 32. Sie enthalten eine Prüfsumme, die auf einem Fehlerkorrekturalgorithmus namens BCH (*Bose-Chaudhuri-Hocquenghem*) basiert. Im Vergleich zu den "Legacy"-Adressen, die in "Base58check" kodiert sind, verfügen die "Bech32"- und "Bech32m"-Adressen über eine effizientere Prüfsumme, die die Erkennung und potenzielle automatische Korrektur von Tippfehlern ermöglicht. Ihr Format bietet auch eine bessere Lesbarkeit, da es nur Kleinbuchstaben enthält. Hier ist die Additionsmatrix für dieses Format zur Basis 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 und Bech32m sind Kodierungsformate, die zur Darstellung von SegWit-Adressen verwendet werden. Bech32 ist ein Adresskodierungsformat, das 2017 von BIP173 eingeführt wurde. Es verwendet einen bestimmten Zeichensatz, der aus Zahlen und Kleinbuchstaben besteht, um Tippfehler zu minimieren und das Lesen zu erleichtern. Bech32-Adressen beginnen in der Regel mit "bc1", um anzuzeigen, dass sie für SegWit nativ sind. Dieses Format wird nur bei SegWit V0-Adressen mit den Skripten P2WPKH (Pay to Witness Public Key Hash) und P2WSH (Pay to Witness Script Hash) verwendet. Es gibt jedoch einen kleinen, unerwarteten Fehler, der speziell das Bech32-Format betrifft. Wenn das letzte Zeichen der Adresse ein "p" ist, führt das Hinzufügen oder Entfernen einer beliebigen Anzahl von "q"-Zeichen unmittelbar davor nicht zur Ungültigkeit der Prüfsumme. Dies hat keine Auswirkungen auf bestehende Verwendungen von SegWit-V0-Adressen (BIP173), da diese auf zwei definierte Längen beschränkt sind. Dies könnte sich jedoch auf zukünftige Verwendungen der Bech32-Kodierung auswirken. Das Bech32m-Format ist einfach ein Bech32-Format, bei dem dieser Fehler korrigiert wurde. Es wurde mit BIP350 im Jahr 2020 eingeführt. Bech32m-Adressen beginnen ebenfalls mit "bc1", sind aber speziell für die Kompatibilität mit SegWit V1 (Taproot) und späteren Versionen mit dem Skript P2TR (Pay to TapRoot) konzipiert.