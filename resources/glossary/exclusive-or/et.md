---
term: EXCLUSIVE VÕI

---
Boole'i loogika põhifunktsioon. Eksklusiivne või XOR ("*Eksklusiivne või*") võtab kaks boolaarset operandit, millest kumbki on tõene või väär, ja annab tõese tulemuse ainult siis, kui need kaks operandit on erinevad. Teisisõnu, operatsiooni "XOR" väljund on tõene, kui täpselt üks (kuid mitte mõlemad) operandid on tõesed. Näiteks `XOR` operatsioon `1` ja `0` vahel annab tulemuseks `1`. Märgime: $1 \oplus 0 = 1$. Samamoodi saab `XOR`-operatsiooni teha ka pikemate bitide jadadega. Näiteks $10110 \oplus 01110 = 11000$. Iga biti jadas võrreldakse oma vastandiga ja rakendatakse operatsiooni `XOR`. Siin on tõesustabel `XOR` operatsiooni jaoks:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

XOR-operatsiooni kasutatakse paljudes arvutiteaduse valdkondades, eriti krüptograafias, selle huvitavate omaduste tõttu, näiteks:


- Selle kommutatiivsus: operandide järjestus ei mõjuta tulemust. Kahe antud muutuja $D$ ja $E$ puhul: $D \oplus E = E \oplus D$;
- Selle assotsiatiivsus: operandide rühmitamine ei mõjuta tulemust. Kolme antud muutuja $A$, $B$ ja $C$ puhul: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Sellel on neutraalne element `0`: 0-ga xoreeritud operand on alati võrdne operandiga. Antud muutuja $A$ puhul: $A \oplus 0 = A$;
- Iga element on oma inversioon. Antud muutuja $A$ puhul: $A \oplus A = 0$.

Bitcoini kontekstis kasutatakse ilmselt paljudes kohtades operatsiooni `XOR`. Näiteks `XOR` on massiliselt kasutusel funktsioonis `SHA256`, mida kasutatakse laialdaselt Bitcoini protokollis. Mõned protokollid, nagu Coldcardi *SeedXOR*, kasutavad seda primitiivi ka muudes rakendustes. Seda leidub ka BIP47-s, et krüpteerida korduvkasutatavat maksekoodi selle edastamise ajal.

Laiemas krüptograafia valdkonnas võib `XOR` kasutada sümmeetrilise krüpteerimisalgoritmina. Seda algoritmi nimetatakse "One-Time Pad" või "Vernam Cipher", mis on nimetatud selle leiutaja järgi. Kuigi see algoritm on võtme pikkuse tõttu ebapraktiline, on see üks ainsatest tingimusteta turvaliseks tunnistatud krüpteerimisalgoritmidest.