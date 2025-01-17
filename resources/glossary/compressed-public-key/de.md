---
term: KOMPRIMIERTER ÖFFENTLICHER SCHLÜSSEL

---
Ein öffentlicher Schlüssel wird in Skripten verwendet (entweder direkt in Form eines öffentlichen Schlüssels oder als Adresse), um Bitcoins zu erhalten und zu sichern. Ein roher öffentlicher Schlüssel wird durch einen Punkt auf einer elliptischen Kurve dargestellt, der aus zwei Koordinaten (x, y) mit jeweils 256 Bit besteht. Im Rohformat misst ein öffentlicher Schlüssel also 512 Bits, ohne das zusätzliche Byte zur Identifizierung des Formats mitzuzählen. Ein komprimierter öffentlicher Schlüssel hingegen ist eine kompaktere Form der Darstellung eines öffentlichen Schlüssels. Er verwendet nur die `x`-Koordinate und ein Präfix (`02` oder `03`), das die Parität der `y`-Koordinate angibt (gerade oder ungerade).

Vereinfacht man dies auf den Bereich der reellen Zahlen, so ist die elliptische Kurve symmetrisch zur x-Achse, und für jeden Punkt $P$ (`x, y`) auf der Kurve gibt es einen Punkt $P'$ (`x, -y`), der ebenfalls auf dieser Kurve liegt. Das bedeutet, dass es für jedes "x" nur zwei mögliche Werte für "y" gibt, nämlich positiv und negativ. Zum Beispiel gäbe es für eine gegebene Abszisse `x` zwei Punkte $P1$ und $P2$ auf der elliptischen Kurve, die dieselbe Abszisse haben, aber mit entgegengesetzten Ordinaten:

![](../../dictionnaire/assets/29.webp)

Um zwischen den beiden möglichen Punkten auf der Kurve zu wählen, wird zu "x" ein Präfix hinzugefügt, das angibt, welches "y" gewählt werden soll. Mit dieser Methode lässt sich die Größe eines öffentlichen Schlüssels von 520 Bits auf nur 264 Bits reduzieren (8 Bits Präfix + 256 Bits für "x"). Diese Darstellung wird als komprimierte Form des öffentlichen Schlüssels bezeichnet.

Im Zusammenhang mit der Kryptographie elliptischer Kurven verwenden wir jedoch nicht die reellen Zahlen, sondern ein endliches Feld der Ordnung "p" (eine Primzahl). In diesem Zusammenhang wird das "Vorzeichen" von "y" durch seine Parität bestimmt, das heißt, ob "y" gerade oder ungerade ist. Die Vorsilbe `0x02` steht dann für ein gerades `y`, während `0x03` für ein ungerades `y` steht.

Betrachten Sie das folgende Beispiel eines rohen öffentlichen Schlüssels (ein Punkt auf der elliptischen Kurve) in hexadezimaler Darstellung:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Wir können das Präfix, "x" und "y" isolieren:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Basis 16 (hexadezimal): f

Basis 10 (dezimal): 15

y ist ungerade

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```