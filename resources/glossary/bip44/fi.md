---
termi: BIP44
---

Ehdotus parannukseksi, joka esittelee standardoidun hierarkkisen johdannaisrakenteen HD-lompakoille. BIP44 rakentuu BIP32:n periaatteille avainjohdannaisista ja BIP43:n käytöstä "tarkoitus"-kentässä. Se esittelee viisitasoisen johdannaisrakenteen: `m / tarkoitus' / kolikkotyyppi' / tili' / vaihto / osoiteindeksi`. Tässä ovat kunkin tason yksityiskohdat:
* `m /` osoittaa pääyksityisavaimen. Se on lompakolle ainutlaatuinen eikä voi olla samalla tasolla sisaruksia. Pääavain johdetaan suoraan lompakon siemenestä;
* `m / tarkoitus' /` osoittaa johdannaisen tarkoituksen, joka auttaa tunnistamaan noudatetun standardin. Tämä kenttä on kuvattu BIP43:ssa. Esimerkiksi, jos lompakko noudattaa BIP84 (SegWit V0) -standardia, indeksi olisi silloin `84'`;
* `m / tarkoitus' / kolikkotyyppi' /` osoittaa kryptovaluutan tyypin. Tämä mahdollistaa selvän erottelun yhden kryptovaluutan omistautuneiden haarojen ja toisen kryptovaluutan omistautuneiden haarojen välillä monikolikkolompakossa. Bitcoinille omistettu indeksi on `0'`;
* `m / tarkoitus' / kolikkotyyppi' / tili' /` osoittaa tilinumeron. Tämä taso mahdollistaa lompakon helpon erottelun ja järjestämisen eri tileihin. Nämä tilit on numeroitu alkaen `0'`. Laajennetut avaimet (`xpub`, `xprv`...) löytyvät tältä tasolta;
* `m / tarkoitus' / kolikkotyyppi' / tili' / vaihto /` osoittaa ketjun. Kuten tasolla 3 määritellyllä tilillä, tasolla 4 on kaksi ketjua: ulkoinen ketju ja sisäinen ketju (jota kutsutaan myös "vaihdoksi"). Ulkoinen ketju johtaa osoitteisiin, jotka on tarkoitettu julkisesti kommunikoitaviksi, eli osoitteisiin, jotka meille tarjotaan, kun klikkaamme "vastaanota" lompakko-ohjelmistossamme. Sisäinen ketju johtaa osoitteisiin, joita ei ole tarkoitettu vaihdettavaksi julkisesti, eli pääasiassa vaihto-osoitteisiin. Ulkoinen ketju tunnistetaan indeksillä `0` ja sisäinen ketju indeksillä `1`. Huomaat, että tästä tasosta lähtien emme enää suorita kovennettua johdannaista, vaan normaalin johdannaisen (ei ole heittomerkkiä). Juuri tämän mekanismin ansiosta pystymme johtamaan kaikki lapsen julkiset avaimet niiden `xpub`-avaimista;
* `m / tarkoitus' / kolikkotyyppi' / tili' / vaihto / osoiteindeksi` yksinkertaisesti osoittaa vastaanotto-osoitteen numeron ja sen avainparin, jotta se voidaan erottaa sen sisaruksista samalla tasolla samassa haarassa. Esimerkiksi ensimmäinen johdettu osoite on indeksissä `0`, toinen osoite on indeksissä `1`, ja niin edelleen...
Esimerkiksi, jos vastaanotto-osoitteeni johdannaispolku on `m / 86' / 0' / 0' / 0 / 5`, voimme päätellä seuraavat tiedot:
* `86'` osoittaa, että noudatamme BIP86:n (Taproot tai SegWitV1) johdannaisstandardia;
* `0'` osoittaa, että kyseessä on Bitcoin-osoite;
* `0'` osoittaa, että olemme lompakon ensimmäisellä tilillä;
* `0` osoittaa, että kyseessä on ulkoinen osoite;
* `5` osoittaa, että kyseessä on tämän tilin kuudes ulkoinen osoite.