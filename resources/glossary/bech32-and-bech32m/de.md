---
term: BECH32 UND BECH32M
---

`Bech32` und `Bech32m` sind zwei Adresskodierungsformate für den Empfang von Bitcoins. Sie basieren auf einem leicht modifizierten Basis-32-System. Sie integrieren eine Prüfsumme, die auf einem fehlerkorrigierenden Algorithmus namens BCH (*Bose-Chaudhuri-Hocquenghem*) basiert. Im Vergleich zu Legacy-Adressen, die in `Base58check` kodiert sind, haben die `Bech32`- und `Bech32m`-Adressen eine effizientere Prüfsumme, die die Erkennung und potenziell automatische Korrektur von Tippfehlern ermöglicht. Ihr Format bietet auch eine bessere Lesbarkeit, mit ausschließlich Kleinbuchstaben. Hier ist die Additionsmatrix für dieses Format von Basis 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 und Bech32m sind Kodierungsformate, die verwendet werden, um SegWit-Adressen darzustellen. Bech32 ist ein Adresskodierungsformat, das 2017 durch BIP173 eingeführt wurde. Es verwendet eine spezifische Zeichengruppe, bestehend aus Zahlen und Kleinbuchstaben, um Tippfehler zu minimieren und die Lesbarkeit zu erleichtern. Bech32-Adressen beginnen in der Regel mit `bc1`, um anzuzeigen, dass sie nativ zu SegWit gehören. Dieses Format wird nur bei SegWit V0-Adressen verwendet, mit den Skripten P2WPKH (Pay to Witness Public Key Hash) und P2WSH (Pay to Witness Script Hash). Es gibt jedoch einen kleinen, unerwarteten Fehler spezifisch für das Bech32-Format. Wann immer der letzte Buchstabe der Adresse ein `p` ist, führt das Hinzufügen oder Entfernen einer beliebigen Anzahl von `q`-Buchstaben unmittelbar davor nicht zur Ungültigkeit der Prüfsumme. Dies beeinträchtigt nicht die bestehenden Verwendungen von SegWit V0-Adressen (BIP173) aufgrund ihrer Beschränkung auf zwei definierte Längen. Dies könnte jedoch zukünftige Verwendungen der Bech32-Kodierung beeinflussen. Das Bech32m-Format ist einfach ein Bech32-Format mit diesem Fehler korrigiert. Es wurde mit BIP350 im Jahr 2020 eingeführt. Bech32m-Adressen beginnen ebenfalls mit `bc1`, sind aber speziell so konzipiert, dass sie mit SegWit V1 (Taproot) und späteren Versionen kompatibel sind, mit dem Skript P2TR (Pay to TapRoot).