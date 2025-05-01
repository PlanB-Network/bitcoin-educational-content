---
term: Commitment
---

Commitment (krüptograafilises mõttes) on matemaatiline objekt, mida tähistatakse $C$ ja mis saadakse deterministlikult struktureeritud andmete $m$ (sõnum) ja juhusliku väärtuse $r$ põhjal. Kirjutame :


$$
C = \text{commit}(m, r)
$$


See mehhanism koosneb kahest peamisest toimingust:




- Commit: rakendame krüptofunktsiooni sõnumi $m$ ja juhusliku $r$ suhtes, et saada $C$ ;
- Kontrollimine: kasutame $C$, $m$ sõnumit ja $r$ väärtust, et kontrollida, kas see Commitment on õige. Funktsioon tagastab `True` või `False`.


Commitment peab järgima kahte omadust:




- Sidumine: peab olema võimatu leida kahte erinevat sõnumit, mis toodavad sama $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Näiteks :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Varjamine: $C$ teadmine ei tohi paljastada $m$ sisu.


RGB protokolli puhul lisatakse Commitment Bitcoin tehingusse, et tõestada teatava teabe olemasolu teataval ajal, ilma et see teave ise avalikustataks.