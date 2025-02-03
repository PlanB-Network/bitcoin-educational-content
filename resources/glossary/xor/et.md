---
term: XOR

---
Akronüüm operatsioonile "Exclusive or", prantsuse keeles "Ou exclusif" See on Boole'i loogika põhifunktsioon. See operatsioon võtab kaks Boole'i operandit, millest kumbki on $tõene$ või $vale$, ja annab tulemuseks $tõene$ ainult siis, kui need kaks operandit erinevad. Teisisõnu, XOR-operatsiooni väljund on $tõene$, kui täpselt üks (kuid mitte mõlemad) operandid on $tõene$. Näiteks XOR-operatsioon $1$ ja $0$ vahel annab tulemuseks $1$. Märgime:

$$
1 \oplus 0 = 1
$$

Samamoodi saab XOR-operatsiooni teostada pikemate bitide jadadega. Näiteks:

$$
10110 \oplus 01110 = 11000
$$

Iga bit järjestuses võrreldakse oma vastaskirjega ja rakendatakse XOR-operatsiooni. Siin on XOR-operatsiooni tõesustabel:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

XOR-operatsiooni kasutatakse paljudes arvutiteaduse valdkondades, eelkõige krüptograafias, selle huvitavate omaduste tõttu, näiteks:


- Selle kommutatiivsus: operandide järjestus ei mõjuta tulemust. Kahe antud muutuja $D$ ja $E$ puhul: $D \oplus E = E \oplus D$;
- Selle assotsiatiivsus: operandide rühmitamine ei mõjuta tulemust. Kolme antud muutuja $A$, $B$ ja $C$ puhul: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Sellel on neutraalne element $0$: operand, mis on xoreeritud $0$-ga, on alati võrdne operandiga. Antud muutuja $A$ puhul: $A \oplus 0 = A$;
- Iga element on oma inversioon. Antud muutuja $A$ puhul: $A \oplus A = 0$.

Bitcoini kontekstis kasutatakse XOR-operatsiooni ilmselt paljudes kohtades. Näiteks kasutatakse XOR-operatsiooni massiliselt SHA256-funktsioonis, mida kasutatakse laialdaselt Bitcoini protokollis. Mõned protokollid, nagu Coldcardi *SeedXOR*, kasutavad seda primitiivi ka muudes rakendustes. Seda leidub ka BIP47-s, et krüpteerida korduvkasutatavat maksekoodi selle edastamise ajal.

Laiemas krüptograafia valdkonnas saab XOR-i kasutada sümmeetrilise krüpteerimisalgoritmina. Seda algoritmi nimetatakse "One-Time Pad" või "Vernam Cipher", mis on nime saanud selle leiutaja järgi. Kuigi see algoritm on võtme pikkuse tõttu ebapraktiline, on see üks ainsatest tingimusteta turvaliseks tunnistatud krüpteerimisalgoritmidest.