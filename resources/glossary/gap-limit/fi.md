---
termi: GAP LIMIT
---

Parametri, jota käytetään Bitcoin-lompakko-ohjelmistossa määrittämään maksimimäärä peräkkäisiä käyttämättömiä osoitteita, jotka generoidaan ennen kuin lisätransaktioiden etsintä lopetetaan. Tämän parametrin säätäminen on usein tarpeellista lompakon palauttamisen yhteydessä varmistamaan, että kaikki transaktiot löytyvät. Riittämätön Gap Limit voi johtaa joidenkin transaktioiden puuttumiseen, jos osoitteita on ohitettu johdannaisvaiheiden aikana. Gap Limitin kasvattaminen mahdollistaa lompakon etsiä pidemmälle osoitesarjassa, jotta kaikki liitetyt transaktiot voidaan palauttaa.

Itse asiassa yksittäinen `xpub` voi teoriassa johtaa yli 4 miljardiin vastaanotto-osoitteeseen (sekä sisäisiin että ulkoisiin osoitteisiin). Kuitenkin, lompakko-ohjelmistot eivät voi johtaa ja tarkistaa kaikkia niitä käytön varalta ilman, että se aiheuttaisi suuria operatiivisia kustannuksia. Näin ollen ne etenevät indeksijärjestyksessä, koska tämä on yleensä järjestys, jossa kaikki lompakko-ohjelmistot generoivat osoitteita. Ohjelmisto tallentaa kunkin käytetyn osoitteen ennen siirtymistä seuraavaan, ja se lopettaa etsintänsä, kun se kohtaa joukon peräkkäin tyhjiä osoitteita. Tätä lukumäärää kutsutaan Gap Limitiksi.

Jos esimerkiksi Gap Limit on asetettu arvoon `20`, ja osoite `m/84'/0'/0'/0/15/` on tyhjä, lompakko johtaa osoitteita aina `m/84'/0'/0'/0/34/` asti. Jos tämä osoitealue pysyy käyttämättömänä, etsintä pysähtyy siihen. Täten transaktio, joka käyttää osoitetta `m/84'/0'/0'/0/40/`, ei tulisi havaituksi tässä esimerkissä.