---
term: BIP156

---
Ehdotus, joka tunnetaan nimellä Dandelion ja jonka tarkoituksena on parantaa transaktioiden reitityksen yksityisyyttä Bitcoin-verkossa deanonymisoinnin torjumiseksi. Bitcoinin tavanomaisessa toiminnassa transaktiot lähetetään välittömästi useisiin solmuihin. Jos tarkkailija pystyy näkemään jokaisen verkon jokaisen solmun välittämät transaktiot, hän saattaa olettaa, että ensimmäisenä transaktion lähettänyt solmu on myös kyseisen transaktion lähettäjäsolmu ja että transaktio on siis peräisin kyseisen solmun operaattorilta. Tämän ilmiön ansiosta tarkkailijat voivat mahdollisesti yhdistää normaalisti anonyymit transaktiot IP-osoitteisiin.

BIP156:n tavoitteena on puuttua tähän ongelmaan. Tätä varten siinä otetaan käyttöön lähetyksen lisävaihe anonymiteetin säilyttämiseksi ennen julkista levittämistä. Dandelion käyttää siis ensin "stem"-vaihetta, jossa tapahtuma lähetetään satunnaisen solmupolun kautta, ennen kuin se lähetetään koko verkkoon "fluff"-vaiheessa. Varsi ja pörrö ovat viittauksia transaktion käyttäytymiseen verkon kautta tapahtuvassa levityksessä, ja ne muistuttavat voikukan muotoa (*a dandelion* englanniksi).

Tämä reititysmenetelmä peittää lähdesolmuun johtavan polun, jolloin on vaikea jäljittää tapahtumaa verkon kautta takaisin sen alkuperään. Dandelion parantaa siten yksityisyyttä rajoittamalla vastustajien mahdollisuuksia poistaa verkon nimettömyys. Menetelmä on vieläkin tehokkaampi, kun tapahtuma kulkee "varsi"-vaiheessa solmun kautta, joka salaa verkkoviestintänsä, kuten Tor tai *P2P Transport V2*. BIP156:ta ei ole vielä lisätty Bitcoin Coreen.

![](../../dictionnaire/assets/36.webp)