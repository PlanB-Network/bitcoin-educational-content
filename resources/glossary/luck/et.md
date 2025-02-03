---
term: LUCK

---
Näitaja, mida kasutatakse kaevandamisbasseinides, et mõõta basseini tulemuslikkust võrreldes selle teoreetiliste ootustega. Nagu nimigi ütleb, hindab see koondise õnne ploki leidmisel. Õnne arvutatakse, võrreldes kehtiva ploki leidmiseks teoreetiliselt vajalike aktsiate arvu, mis põhineb Bitcoini praegusel raskusastmel, selle ploki leidmiseks toodetud aktsiate tegeliku arvuga. Oodatust väiksem aktsiate arv näitab head õnne, suurem arv aga halba õnne.

Korreleerides Bitcoini raskusastet iga sekundis toodetud aktsiate arvu ja iga aktsia raskusastmega, saab bassein arvutada aktsiate arvu, mis on teoreetiliselt vajalik kehtiva ploki leidmiseks. Näiteks oletame, et teoreetiliselt on vaja 100 000 aktsiat, et bassein leiaks ploki. Kui bassein toodab tegelikult 200 000 enne bloki leidmist, on tema õnn 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Seevastu, kui see bassein leidis kehtiva ploki pärast ainult 50 000 aktsia tootmist, siis on tema õnn 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Õnne on näitaja, mida saab uuendada ainult pärast seda, kui plokk on leitud, mistõttu on tegemist staatilise näitajaga, mida uuendatakse perioodiliselt.