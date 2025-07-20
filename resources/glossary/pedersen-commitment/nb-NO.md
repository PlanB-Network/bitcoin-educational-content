---
term: Pedersen commitment
---

En Pedersen commitment er en type kryptografisk Commitment med den egenskapen at den er homomorfisk i forhold til addisjonsoperasjonen. Dette betyr at det er mulig å validere summen av to forpliktelser uten å avsløre de individuelle verdiene.


Formelt sett, hvis :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


da :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Denne egenskapen er nyttig, for eksempel for å skjule mengden tokens som utveksles i kryptovaluta-systemer, som RGB, samtidig som det er mulig å verifisere totalsummene.