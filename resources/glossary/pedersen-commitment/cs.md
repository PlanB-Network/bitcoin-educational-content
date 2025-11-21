---
term: Pedersen commitment
---

Pedersen commitment je typ kryptografického Commitment s vlastností homomorfnosti vůči operaci sčítání. To znamená, že je možné ověřit součet dvou závazků, aniž by byly odhaleny jednotlivé hodnoty.


Formálně platí, že pokud :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


pak :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Tato vlastnost je užitečná například pro utajení množství tokenů vyměněných v kryptoměnových systémech, jako je RGB, a zároveň je možné ověřit celkové částky.