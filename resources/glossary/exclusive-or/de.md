---
term: EXKLUSIVES ODER
---

Eine grundlegende Funktion der Booleschen Logik. Das "Exklusive Oder" oder XOR ("*Exklusives Oder*") nimmt zwei Boolesche Operanden, die jeweils wahr oder falsch sind, und produziert eine wahre Ausgabe nur dann, wenn die beiden Operanden unterschiedlich sind. Mit anderen Worten, die Ausgabe der `XOR`-Operation ist wahr, wenn genau einer (aber nicht beide) der Operanden wahr ist. Zum Beispiel wird die `XOR`-Operation zwischen `1` und `0` in `1` resultieren. Wir notieren: $1 \oplus 0 = 1$. Ähnlich kann die `XOR`-Operation auf längere Bitfolgen angewendet werden. Zum Beispiel: $10110 \oplus 01110 = 11000$. Jedes Bit der Sequenz wird mit seinem Gegenstück verglichen, und die `XOR`-Operation wird angewendet. Hier ist die Wahrheitstabelle für die `XOR`-Operation:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

Die `XOR`-Operation wird in vielen Bereichen der Informatik verwendet, insbesondere in der Kryptographie, aufgrund ihrer interessanten Eigenschaften wie:
* Ihre Kommutativität: Die Reihenfolge der Operanden beeinflusst das Ergebnis nicht. Für zwei gegebene Variablen $D$ und $E$: $D \oplus E = E \oplus D$;
* Ihre Assoziativität: Die Gruppierung der Operanden beeinflusst das Ergebnis nicht. Für drei gegebene Variablen $A$, $B$ und $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Sie hat ein neutrales Element `0`: Ein Operand, der mit 0 ge-xort wird, ist immer gleich dem Operanden. Für eine gegebene Variable $A$: $A \oplus 0 = A$;
* Jedes Element ist sein eigenes Inverses. Für eine gegebene Variable $A$: $A \oplus A = 0$.

Im Kontext von Bitcoin wird die `XOR`-Operation offensichtlich an vielen Stellen verwendet. Zum Beispiel wird `XOR` massiv in der `SHA256`-Funktion verwendet, die im Bitcoin-Protokoll weit verbreitet ist. Einige Protokolle wie Coldcards *SeedXOR* nutzen dieses Primitiv auch für andere Anwendungen. Es findet sich auch in BIP47 für die Verschlüsselung des wiederverwendbaren Zahlungscodes während seiner Übertragung.
Im breiteren Feld der Kryptographie kann `XOR` als symmetrischer Verschlüsselungsalgorithmus verwendet werden. Dieser Algorithmus wird als "One-Time Pad" oder "Vernam-Chiffre" bezeichnet, benannt nach seinem Erfinder. Obwohl aufgrund der Länge des Schlüssels unpraktisch, ist dieser Algorithmus einer der wenigen Verschlüsselungsalgorithmen, der als bedingungslos sicher anerkannt ist.