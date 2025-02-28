---
term: BYSANTIN KENRAALIEN ONGELMA

---
Leslie Lamport, Robert Shostak ja Marshall Pease muotoilivat ongelman ensimmäisen kerran *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"] (https://lamport.azurewebsites.net/pubs/byz.pdf) -erikoislehdessä heinäkuussa 1982. Sitä käytetään nykyään havainnollistamaan päätöksenteon haasteita silloin, kun hajautettu järjestelmä ei voi luottaa yhteenkään toimijaan.

Tässä vertauskuvassa joukko bysanttilaisia kenraaleja ja heidän armeijansa leiriytyvät kaupungin ympärille, johon he haluavat hyökätä tai jonka he haluavat piirittää. Kenraalit ovat maantieteellisesti erillään toisistaan, ja heidän on kommunikoitava viestinviejän välityksellä koordinoidakseen strategiaansa. Sillä, hyökkäävätkö vai vetäytyvätkö he, ei ole väliä, kunhan kaikki kenraalit pääsevät yhteisymmärrykseen.

Näin ollen voimme ottaa huomioon seuraavat vaatimukset:


- Kunkin kenraalin on tehtävä päätös: hyökätä tai vetäytyä (kyllä tai ei);
- Kun päätös on tehty, sitä ei voi enää muuttaa;
- Kaikkien kenraalien on sovittava samasta päätöksestä ja pantava se täytäntöön samanaikaisesti.

Lisäksi kenraali voi kommunikoida toisen kanssa vain kuriirin lähettämien viestien välityksellä, jotka voivat viivästyä, tuhoutua, muuttua tai kadota. Ja vaikka viesti toimitettaisiinkin onnistuneesti, yksi tai useampi kenraali voi päättää (mistä tahansa syystä) pettää luottamuksen ja lähettää väärennetyn viestin ja kylvää kaaoksen.

Sovellettaessa tätä dilemmaa Bitcoin-lohkoketjun kontekstiin, jokainen yleinen edustaa verkon solmua, jonka on päästävä yksimielisyyteen järjestelmän tilasta. Toisin sanoen hajautetun verkon osallistujien enemmistön on päästävä yhteisymmärrykseen ja suoritettava sama toimenpide, jotta vältetään täydellinen epäonnistuminen. Ainoa tapa päästä konsensukseen tämäntyyppisessä hajautetussa järjestelmässä on, että vähintään 2/3 verkon solmuista on luotettavia ja rehellisiä. Jos siis enemmistö verkon solmuista päättää toimia ilkivaltaisesti, järjestelmä on haavoittuva.

> ► *Tätä ongelmaa kutsutaan joskus myös "luotettavan lähetyksen ongelmaksi "*