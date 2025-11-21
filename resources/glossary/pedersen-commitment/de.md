---
term: Pedersen commitment
---

Ein Pedersen commitment ist eine Art kryptographischer Commitment mit der Eigenschaft, homomorph zur Additionsoperation zu sein. Dies bedeutet, dass es möglich ist, die Summe von zwei Verpflichtungen zu validieren, ohne die einzelnen Werte zu offenbaren.


Formal gesehen, wenn :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


dann:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Diese Eigenschaft ist z. B. nützlich, um die Menge der in Kryptowährungssystemen wie RGB ausgetauschten Token zu verbergen, während die Gesamtsummen immer noch verifiziert werden können.