---
term: ÕNN
---

Indikaator, mida kasutatakse kaevandusbasseinides, et mõõta basseini sooritust võrreldes selle teoreetiliste ootustega. Nagu nimigi viitab, hindab see basseini õnne leidmaks plokki. Õnn arvutatakse, võrreldes teoreetiliselt vajalike aktsiate (share) arvu, mis on vajalik kehtiva ploki leidmiseks, lähtudes Bitcoin'i praegusest raskusastmest, tegelikult toodetud aktsiate arvuga, mis olid vajalikud selle ploki leidmiseks. Oodatust väiksem aktsiate arv näitab head õnne, samas kui suurem arv näitab halba õnne.

Võrreldes Bitcoin'i raskusastet selle aktsiate tootmisega iga sekundi järel ja iga aktsia raskusastet, saab bassein arvutada teoreetiliselt vajalike aktsiate arvu, mis on vajalik kehtiva ploki leidmiseks. Näiteks, eeldades teoreetiliselt, et basseinil on vaja leida plokk 100,000 aktsiaga. Kui bassein tegelikult toodab 200,000 aktsiat enne ploki leidmist, on selle õnn 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Vastupidiselt, kui see bassein leiab kehtiva ploki pärast ainult 50,000 aktsia tootmist, siis on selle õnn 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Õnn on indikaator, mida saab uuendada ainult pärast seda, kui bassein on ploki avastanud, muutes selle staatiliseks indikaatoriks, mida uuendatakse perioodiliselt.