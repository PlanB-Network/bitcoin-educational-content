---
term: KOMPRIMIERTER ÖFFENTLICHER SCHLÜSSEL
---

Ein öffentlicher Schlüssel wird in Skripten verwendet (entweder direkt in Form eines öffentlichen Schlüssels oder als Adresse), um Bitcoins zu empfangen und zu sichern. Ein roher öffentlicher Schlüssel wird durch einen Punkt auf einer elliptischen Kurve dargestellt, bestehend aus zwei Koordinaten (`x, y`), jede mit 256 Bits. Im Rohformat misst ein öffentlicher Schlüssel daher 512 Bits, ohne das zusätzliche Byte zur Identifizierung des Formats zu zählen. Ein komprimierter öffentlicher Schlüssel hingegen ist eine kompaktere Form der Darstellung des öffentlichen Schlüssels. Er verwendet nur die `x`-Koordinate und ein Präfix (`02` oder `03`), das die Parität der `y`-Koordinate (gerade oder ungerade) angibt.

Wenn wir dies auf das Feld der reellen Zahlen vereinfachen, gegeben die elliptische Kurve ist symmetrisch in Bezug auf die x-Achse, für jeden Punkt $P$ (`x, y`) auf der Kurve, existiert ein Punkt $P'$ (`x, -y`), der auch auf dieser gleichen Kurve sein wird. Das bedeutet, dass für jedes `x` nur zwei mögliche Werte von `y`, positiv und negativ, existieren. Zum Beispiel, für eine gegebene Abszisse `x`, gäbe es zwei Punkte $P1$ und $P2$ auf der elliptischen Kurve, die die gleiche Abszisse teilen, aber mit entgegengesetzten Ordinaten:

![](../../dictionnaire/assets/29.png)
Um zwischen den zwei potenziellen Punkten auf der Kurve zu wählen, wird ein Präfix hinzugefügt, das angibt, welches `y` zu wählen ist. Diese Methode ermöglicht es, die Größe eines öffentlichen Schlüssels von 520 Bits auf nur 264 Bits zu reduzieren (8 Bits des Präfixes + 256 Bits für `x`). Diese Darstellung ist als die komprimierte Form des öffentlichen Schlüssels bekannt.

Jedoch verwenden wir im Kontext der elliptischen Kurvenkryptografie nicht die reellen Zahlen, sondern ein endliches Feld der Ordnung `p` (eine Primzahl). In diesem Kontext wird das "Zeichen" von `y` durch seine Parität bestimmt, das heißt, ob `y` gerade oder ungerade ist. Das Präfix `0x02` zeigt dann ein gerades `y`, während `0x03` ein ungerades `y` anzeigt.

Betrachten Sie das folgende Beispiel eines rohen öffentlichen Schlüssels (ein Punkt auf der elliptischen Kurve) in Hexadezimal:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Wir können das Präfix, `x` und `y` isolieren:
```plaintext
Präfix = 04
Um die Parität von `y` zu bestimmen, untersuchen wir das letzte hexadezimale Zeichen von `y`:
```plaintext
Basis 16 (hexadezimal): f
Basis 10 (dezimal): 15
y ist ungerade
```

Das Präfix für den komprimierten öffentlichen Schlüssel wird `03` sein. Der komprimierte öffentliche Schlüssel in Hexadezimal wird:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```