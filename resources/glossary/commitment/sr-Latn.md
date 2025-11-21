---
term: Commitment
---

Commitment (u kriptografskom smislu) je matematički objekat, označen sa $C$, izveden deterministički iz operacije na strukturisanim podacima $m$ (poruka) i nasumične vrednosti $r$. Pišemo :


$$
C = \text{commit}(m, r)
$$


Ovaj mehanizam obuhvata dve glavne operacije:




- Commit: primenjujemo kriptografsku funkciju na poruku $m$ i slučajni $r$ da bismo proizveli $C$ ;
- Verifikuj: koristimo $C$, $m$ poruku i $r$ vrednost da proverimo da li je ovaj Commitment tačan. Funkcija vraća `True` ili `False`.


Commitment mora poštovati dva svojstva:




- Vezivanje: mora biti nemoguće pronaći dve različite poruke koje proizvode isti $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Kao što su :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Skrivanje: znanje o $C$ ne sme otkriti sadržaj $m$.


U slučaju protokola RGB, Commitment je uključen u Bitcoin transakciju kako bi se dokazalo postojanje određene informacije u datom trenutku, bez otkrivanja same informacije.