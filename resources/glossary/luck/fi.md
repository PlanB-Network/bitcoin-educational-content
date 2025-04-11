---
term: LUCK

---
Indikaattori, jota käytetään kaivospooleissa mittaamaan poolin suorituskykyä suhteessa sen teoreettisiin odotuksiin. Kuten nimestä voi päätellä, sillä arvioidaan poolin onnea lohkojen löytämisessä. Onnellisuus lasketaan vertaamalla kelvollisen lohkon löytämiseen teoreettisesti tarvittavien osakkeiden määrää Bitcoinin nykyisen vaikeusasteen perusteella lohkon löytämiseksi tuotettujen osakkeiden todelliseen määrään. Odotettua alhaisempi osakkeiden määrä tarkoittaa hyvää onnea, kun taas korkeampi määrä tarkoittaa huonoa onnea.

Korreloimalla Bitcoinin vaikeusaste ja sen sekunnissa tuotettujen osakkeiden määrä sekä kunkin osakkeen vaikeusaste, pooli voi laskea osakkeiden määrän, joka on teoriassa tarpeen kelvollisen lohkon löytämiseksi. Oletetaan esimerkiksi, että pooli tarvitsee teoreettisesti 100 000 osaketta löytääkseen lohkon. Jos pooli tuottaa todellisuudessa 200 000 osaketta ennen lohkon löytämistä, sen onni on 50 %:

```text
100,000 / 200,000 = 0.5 = 50%
```

Jos taas tämä pool löysi kelvollisen lohkon tuotettuaan vain 50 000 osaketta, sen onni on 200 %:

```text
100,000 / 50,000 = 2 = 200%
```

Luck on indikaattori, joka voidaan päivittää vasta sen jälkeen, kun pooli on löytänyt lohkon, joten se on staattinen indikaattori, joka päivitetään säännöllisesti.