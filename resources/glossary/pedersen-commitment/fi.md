---
term: Pedersen commitment
---

Pedersen commitment on eräänlainen kryptografinen Commitment, jolla on ominaisuus olla homomorfinen yhteenlaskuoperaatiolle. Tämä tarkoittaa sitä, että kahden sitoumuksen summa on mahdollista vahvistaa paljastamatta yksittäisiä arvoja.


Muodollisesti, jos :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


sitten :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Tämä ominaisuus on hyödyllinen esimerkiksi kryptovaluuttajärjestelmissä, kuten RGB:ssa, vaihdettujen tokenien määrien salaamiseksi, mutta summat voidaan silti todentaa.