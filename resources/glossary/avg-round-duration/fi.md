---
term: AVG. KIERROKSEN KESTO

---
Keskimääräinen kierroksen kesto on indikaattori, jota käytetään arvioimaan aikaa, joka louhintapoolilta kuluu lohkon löytämiseen verkon vaikeusasteen ja poolin hashraten perusteella. Se lasketaan ottamalla lohkon löytämiseen odotettavissa olevien osuuksien määrä ja jakamalla se poolin hashratella. Jos esimerkiksi louhintapooliin kuuluu 200 louhijaa, joista kukin tuottaa keskimäärin 4 osaketta sekunnissa, poolin laskentateho on 800 osaketta sekunnissa:

```text
200 * 4 = 800
```

Jos oletetaan, että kelvollisen lohkon löytäminen vie keskimäärin 1 miljoona osaketta, pooli *Avg. Round Duration* olisi 1250 sekuntia eli noin 21 minuuttia:

```text
1,000,000 / 800 = 1,250
```

Käytännössä tämä tarkoittaa, että louhintapooli löytää lohkon keskimäärin noin 21 minuutin välein. Tämä indikaattori vaihtelee poolin hashraten muutosten mukaan: hashraten kasvu vähentää *Avg. Round Duration*, kun taas lasku pidentää sitä. Se vaihtelee myös jokaisen Bitcoin-vaikeustavoitteen säännöllisen mukauttamisen yhteydessä (joka 2016 lohko). Tässä mittarissa ei oteta huomioon muiden poolien löytämiä lohkoja, vaan siinä keskitytään ainoastaan tutkittavan poolin sisäiseen suorituskykyyn.