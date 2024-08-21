---
termi: LUCK
---

Indikaattori, jota käytetään louhintapoolien suorituskyvyn mittaamiseen suhteessa niiden teoreettisiin odotuksiin. Nimensä mukaisesti se arvioi poolin onnea lohkon löytämisessä. Onni lasketaan vertaamalla teoreettisesti tarvittavien osuuksien määrää, joka perustuu Bitcoinin nykyiseen vaikeustasoon, todelliseen osuuksien määrään, joka tuotettiin kyseisen lohkon löytämiseksi. Odotettua pienempi osuuksien määrä osoittaa hyvää onnea, kun taas suurempi määrä osoittaa huonoa onnea.

Yhdistämällä Bitcoinin vaikeustason sen sekunnissa tuottamien osuuksien määrään ja kunkin osuuden vaikeustasoon, pooli voi laskea teoreettisesti tarvittavien osuuksien määrän validin lohkon löytämiseksi. Esimerkiksi, oletetaan teoreettisesti, että poolin tarvitsee tuottaa 100,000 osuutta löytääkseen lohkon. Jos pooli todellisuudessa tuottaa 200,000 ennen lohkon löytämistä, sen onni on 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Päinvastaisesti, jos tämä pool löytää validin lohkon tuottamalla vain 50,000 osuutta, sen onni on 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Onni on indikaattori, jota voidaan päivittää vain sen jälkeen, kun pool on löytänyt lohkon, tehden siitä staattisen indikaattorin, jota päivitetään ajoittain.