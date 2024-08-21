---
termi: AVG. ROUND DURATION
---

Keskimääräinen kierroksen kesto on indikaattori, jota käytetään arvioimaan aikaa, jonka louhintapooli tarvitsee lohkon löytämiseen, perustuen verkon vaikeustasoon ja poolin hashrateen. Se lasketaan ottamalla lohkon löytämiseen odotettavien osuuksien määrä ja jakamalla se poolin hashratella. Esimerkiksi, jos louhintapoolissa on 200 louhijaa, ja kukin tuottaa keskimäärin 4 osuutta sekunnissa, poolin kokonaislaskentateho on 800 osuutta sekunnissa:

```text
200 * 4 = 800
```

Olettaen, että keskimäärin tarvitaan 1 miljoona osuutta validin lohkon löytämiseen, poolin *Avg. Round Duration* olisi 1,250 sekuntia, eli noin 21 minuuttia:

```text
1,000,000 / 800 = 1,250
```

Käytännön termein tämä tarkoittaa, että keskimäärin louhintapoolin pitäisi löytää lohko noin joka 21. minuutti. Tämä indikaattori vaihtelee poolin hashraten muutosten myötä: hashraten kasvu lyhentää *Avg. Round Durationia*, kun taas lasku pidentää sitä. Se myös vaihtelee Bitcoinin vaikeustason periodisen säätelyn (joka 2016 lohkon jälkeen) myötä. Tämä mittari ei ota huomioon muiden poolien löytämiä lohkoja ja keskittyy ainoastaan tutkittavan poolin sisäiseen suorituskykyyn.