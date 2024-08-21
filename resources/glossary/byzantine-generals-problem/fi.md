---
termi: BYSANTTILAISTEN KENRAALIEN ONGELMA
---

Ongelman muotoili ensimmäisen kerran Leslie Lamport, Robert Shostak ja Marshall Pease erikoislehdessä *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["Bysanttisten kenraalien ongelma"](https://lamport.azurewebsites.net/pubs/byz.pdf) heinäkuussa 1982. Sitä käytetään nykyään kuvaamaan haasteita päätöksenteossa, kun hajautetussa järjestelmässä ei voida luottaa mihinkään toimijaan.

Tässä metaforassa joukko Bysantin kenraaleja ja heidän vastaavat armeijansa ovat leiriytyneet kaupungin ympärille, jota he haluavat hyökätä tai piirittää. Kenraalit ovat maantieteellisesti erillään toisistaan ja heidän on kommunikoitava viestinviejän kautta koordinoidakseen strategiaansa. Ei ole väliä hyökkäävätkö he vai perääntyvätkö, kunhan kaikki kenraalit pääsevät yksimielisyyteen.

Näin ollen voimme harkita seuraavia vaatimuksia:
* Jokaisen kenraalin on tehtävä päätös: hyökätä tai perääntyä (kyllä tai ei);
* Kun päätös on tehty, sitä ei voi muuttaa;
* Kaikkien kenraalien on oltava samaa mieltä samasta päätöksestä ja toteutettava se synkronisesti.

Lisäksi kenraali voi kommunikoida toisen kanssa vain viestien välityksellä, jotka lähetti voi viivästyttää, tuhota, muuttaa tai kadottaa. Ja vaikka viesti toimitettaisiin onnistuneesti, yksi tai useampi kenraali voi valita (mistä syystä tahansa) pettää vallitsevan luottamuksen ja lähettää petollisen viestin, kylväen kaaosta.

Sovellettaessa dilemmaa Bitcoin-lohkoketjun kontekstiin, jokainen kenraali edustaa verkoston solmua, joka tarvitsee saavuttaa yksimielisyyden järjestelmän tilasta. Toisin sanoen, hajautetun verkon enemmistön osallistujien on oltava samaa mieltä ja toteutettava sama toiminto välttääkseen täydellisen epäonnistumisen. Ainoa tapa saavuttaa yksimielisyys tämäntyyppisessä hajautetussa järjestelmässä on, että vähintään 2/3 verkon solmuista on luotettavia ja rehellisiä. Siksi, jos verkon enemmistö päättää toimia pahantahtoisesti, järjestelmä on haavoittuvainen.

> ► *Tätä dilemmaa kutsutaan joskus myös "Luotettavan lähetysongelman" nimellä.*