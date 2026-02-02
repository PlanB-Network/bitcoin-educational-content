---
term: OP_2ROT (0X71)

definition: Opcode, der das 5. und 6. Element vom Stack nach oben verschiebt.
---
Verschiebt die beiden Elemente, die sich an der sechsten und fünften Position befinden, vom oberen Ende des Stapels nach oben. Zum Beispiel, wenn der Stapel ist:

```text
A
B
C
D
E
F
```

oP_2ROT" wird erzeugt:

```text
E
F
A
B
C
D
```