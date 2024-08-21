---
term: EXCLUSIVE OR
---

Põhiline funktsioon Boole'i loogikas. "Eksklusiivne VÕI" ehk XOR ("*Eksklusiivne või*") võtab kaks Boole'i operandi, millest igaüks võib olla tõene või väär, ja toodab tõese väljundi ainult siis, kui kaks operandi erinevad. Teisisõnu, `XOR` operatsiooni väljund on tõene, kui täpselt üks (aga mitte mõlemad) operandidest on tõene. Näiteks `XOR` operatsioon `1` ja `0` vahel annab tulemuseks `1`. Me märkime: $1 \oplus 0 = 1$. Samamoodi saab `XOR` operatsiooni teostada pikemate bittide jadade peal. Näiteks $10110 \oplus 01110 = 11000$. Iga jada bitti võrreldakse vastava bitiga ja rakendatakse `XOR` operatsiooni. Siin on tõeväärtustabel `XOR` operatsiooni jaoks:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

`XOR` operatsiooni kasutatakse paljudes arvutiteaduse valdkondades, eriti krüptograafias, selle huvitavate omaduste tõttu, nagu:
* Selle kommutatiivsus: operandide järjekord ei mõjuta tulemust. Kahe antud muutuja $D$ ja $E$ puhul: $D \oplus E = E \oplus D$;
* Selle assotsiatiivsus: operandide grupeerimine ei mõjuta tulemust. Kolme antud muutuja $A$, $B$ ja $C$ puhul: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Sellel on neutraalne element `0`: operand, mis on xored 0-ga, on alati võrdne operandiga. Antud muutuja $A$ puhul: $A \oplus 0 = A$;
* Iga element on oma enda invers. Antud muutuja $A$ puhul: $A \oplus A = 0$.

Bitcoini kontekstis kasutatakse `XOR` operatsiooni ilmselgelt paljudes kohtades. Näiteks `XOR` on massiliselt kasutusel `SHA256` funktsioonis, mida laialdaselt kasutatakse Bitcoini protokollis. Mõned protokollid nagu Coldcardi *SeedXOR* kasutavad seda primitiivi ka teistes rakendustes. Samuti leidub see BIP47-s, et krüpteerida korduvkasutatavat maksekoodi selle edastamise ajal.
Laiemas krüptograafia valdkonnas saab `XOR`-i kasutada sellisena nagu see on, sümmeetrilise krüpteerimisalgoritmina. Seda algoritmi nimetatakse "Ühekordseks Pad'iks" või "Vernami šifriks", oma leiutaja järgi. Kuigi see on ebapraktiline võtme pikkuse tõttu, on see algoritm üks väheseid krüpteerimisalgoritme, mida tunnustatakse tingimusteta turvalisena.