---
term: EXKLUSIV ODER

---
Eine grundlegende Funktion der Booleschen Logik. Das "Exklusiv-Oder" oder XOR ("*Exclusive or*") nimmt zwei boolesche Operanden, die jeweils wahr oder falsch sind, und erzeugt nur dann eine wahre Ausgabe, wenn sich die beiden Operanden unterscheiden. Mit anderen Worten, die Ausgabe der "XOR"-Operation ist wahr, wenn genau einer (aber nicht beide) der Operanden wahr ist. Zum Beispiel ergibt die `XOR'-Operation zwischen `1` und `0` das Ergebnis `1`. Wir halten fest: $1 \oplus 0 = 1$. In ähnlicher Weise kann die `XOR'-Verknüpfung auch mit längeren Bitfolgen durchgeführt werden. Zum Beispiel: $10110 \oplus 01110 = 11000$. Jedes Bit der Folge wird mit seinem Gegenstück verglichen, und die "XOR"-Operation wird durchgeführt. Hier ist die Wahrheitstabelle für die "XOR"-Operation:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

Die XOR-Verknüpfung wird in vielen Bereichen der Informatik, insbesondere in der Kryptographie, aufgrund ihrer interessanten Eigenschaften verwendet:


- Seine Kommutativität: Die Reihenfolge der Operanden hat keinen Einfluss auf das Ergebnis. Für zwei gegebene Variablen $D$ und $E$ gilt: $D \oplus E = E \oplus D$;
- Seine Assoziativität: Die Gruppierung der Operanden hat keinen Einfluss auf das Ergebnis. Für drei gegebene Variablen $A$, $B$ und $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Es hat ein neutrales Element "0": ein mit 0 verknüpfter Operand ist immer gleich dem Operanden. Für eine gegebene Variable $A$ gilt: $A \oplus 0 = A$;
- Jedes Element ist sein eigenes Inverses. Für eine gegebene Variable $A$ gilt: $A \oplus A = 0$.

Im Zusammenhang mit Bitcoin wird die "XOR"-Operation offensichtlich an vielen Stellen verwendet. Zum Beispiel wird "XOR" massiv in der Funktion "SHA256" verwendet, die im Bitcoin-Protokoll weit verbreitet ist. Einige Protokolle wie Coldcards *SeedXOR* verwenden dieses Primitiv auch für andere Anwendungen. Sie findet sich auch in BIP47 zur Verschlüsselung des wiederverwendbaren Zahlungscodes während seiner Übertragung.

Im weiteren Bereich der Kryptographie kann "XOR" als symmetrischer Verschlüsselungsalgorithmus verwendet werden. Dieser Algorithmus wird "One-Time Pad" oder "Vernam Cipher" genannt, benannt nach seinem Erfinder. Obwohl dieser Algorithmus aufgrund der Länge des Schlüssels unpraktisch ist, ist er einer der einzigen Verschlüsselungsalgorithmen, die als bedingungslos sicher anerkannt sind.