---
term: Commitment
---

Ein Commitment (im kryptographischen Sinne) ist ein mathematisches Objekt, bezeichnet mit $C$, das deterministisch aus einer Operation auf strukturierten Daten $m$ (der Nachricht) und einem Zufallswert $r$ abgeleitet wird. Wir schreiben :


$$
C = \text{commit}(m, r)
$$


Dieser Mechanismus umfasst zwei Hauptvorgänge:




- Commit: Wir wenden eine kryptographische Funktion auf eine Nachricht $m$ und einen Zufallswert $r$ an, um $C$ zu erzeugen;
- Verify: Wir verwenden $C$, die $m$-Nachricht und den $r$-Wert, um zu prüfen, ob dieser Commitment korrekt ist. Die Funktion gibt `True` oder `False` zurück.


Ein Commitment muss zwei Eigenschaften erfüllen:




- Bindung: Es muss unmöglich sein, zwei verschiedene Nachrichten zu finden, die das gleiche $C$ ergeben:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Zum Beispiel:


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Verstecken: Die Kenntnis von $C$ darf den Inhalt von $m$ nicht preisgeben.


Im Falle des RGB-Protokolls wird ein Commitment in eine Bitcoin-Transaktion aufgenommen, um die Existenz einer bestimmten Information zu einem bestimmten Zeitpunkt nachzuweisen, ohne die Information selbst offen zu legen.