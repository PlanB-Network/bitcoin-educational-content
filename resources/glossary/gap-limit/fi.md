---
term: GAP LIMIT

---
Parametri, jota käytetään Bitcoin-lompakko-ohjelmistossa määrittämään, kuinka monta peräkkäistä käyttämätöntä osoitetta voidaan luoda, ennen kuin uusien transaktioiden etsiminen lopetetaan. Tämän parametrin säätäminen on usein tarpeen, kun lompakkoa palautetaan sen varmistamiseksi, että kaikki transaktiot löytyvät. Riittämätön Gap Limit -raja voi johtaa joidenkin transaktioiden puuttumiseen, jos osoitteita on jätetty väliin derivointivaiheiden aikana. Jos Gap Limit -rajaa kasvatetaan, lompakko voi hakea osoitteita pidemmälle, jotta kaikki transaktiot saadaan talteen.

Yksittäinen `xpub` voi teoriassa johtaa yli 4 miljardia vastaanottavaa osoitetta (sekä sisäisiä että ulkoisia osoitteita). Lompakko-ohjelmisto ei kuitenkaan pysty johtamaan ja tarkistamaan niitä kaikkia käytön varalta ilman valtavia käyttökustannuksia. Näin ollen ne etenevät indeksijärjestyksessä, koska kaikki lompakko-ohjelmistot tuottavat osoitteet yleensä tässä järjestyksessä. Ohjelmisto tallentaa jokaisen käytetyn osoitteen ennen kuin se siirtyy seuraavaan, ja se lopettaa haun, kun se löytää useita peräkkäisiä tyhjiä osoitteita. Tätä lukua kutsutaan Gap Limitiksi.

Jos esimerkiksi Gap Limit on asetettu arvoon `20` ja osoite `m/84'/0'/0'/0/15/` on tyhjä, lompakko johtaa osoitteet osoitteeseen `m/84'/0'/0'/0'/0/34/` asti. Jos tämä osoitealue jää käyttämättä, haku pysähtyy siihen. Näin ollen transaktiota, jossa käytetään osoitetta `m/84'/0'/0'/0'/0/40/`, ei havaittaisi tässä esimerkissä.