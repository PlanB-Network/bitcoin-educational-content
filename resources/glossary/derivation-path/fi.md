---
termi: DERIVATION PATH
---

Hierarkkisten Determinististen (HD) lompakoiden kontekstissa derivation path viittaa indeksien sekvenssiin, jota käytetään johdettujen lasten avainten luomiseen pääavaimesta. BIP32:ssa kuvattu polku tunnistaa puurakenteen lasten avainten johdattamiseen. Derivation path esitetään indeksien sarjana, jotka on erotettu kauttaviivoilla, ja alkaa aina pääavaimesta (merkitty `m/`). Esimerkiksi tyypillinen polku voisi olla `m/84'/0'/0'/0/0`. Jokainen johdannon taso liittyy tiettyyn syvyyteen:
* `m /` osoittaa pääyksityisavaimen. Se on uniikki lompakolle eikä voi olla sisaruksia samalla syvyydellä. Pääavain johdetaan suoraan siemenestä;
* `m / purpose' /` osoittaa johdannon tarkoituksen, joka auttaa tunnistamaan noudatetun standardin. Tämä kenttä on kuvattu BIP43:ssa. Esimerkiksi, jos lompakko noudattaa BIP84-standardia (SegWit V0), indeksi olisi silloin `84'`;
* `m / purpose' / coin-type' /` osoittaa kryptovaluutan tyypin. Tämä mahdollistaa selvän erottelun yhden kryptovaluutan omistautuneiden haarojen ja toisen omistautuneiden haarojen välillä monivaluuttalompakossa. Bitcoinille omistettu indeksi on `0'`;
* `m / purpose' / coin-type' / account' /` osoittaa tilinumeron. Tämä syvyys tekee helpoksi erottaa ja järjestää lompakko eri tileihin. Nämä tilit on numeroitu alkaen `0'`. Laajennetut avaimet (`xpub`, `xprv`...) löytyvät tästä syvyydestä;
* `m / purpose' / coin-type' / account' / change /` osoittaa polun. Jokaisella syvyyden 3 määritellyllä tilillä on kaksi polkua syvyydessä 4: ulkoinen ketju ja sisäinen ketju (kutsutaan myös "vaihto"). Ulkoinen ketju johtaa osoitteisiin, jotka on tarkoitettu jaettavaksi julkisesti, eli osoitteisiin, jotka tarjotaan meille, kun klikkaamme "vastaanota" lompakko-ohjelmistossamme. Sisäinen ketju johtaa osoitteisiin, joita ei ole tarkoitettu vaihdettavaksi julkisesti, pääasiassa vaihto-osoitteisiin. Ulkoinen ketju tunnistetaan indeksillä `0` ja sisäinen ketju indeksillä `1`. Huomaat, että tästä syvyydestä lähtien emme enää suorita kovennettua johdantoa, vaan normaalin johdannon (ei ole heittomerkkiä). Tämän mekanismin ansiosta pystymme johtamaan kaikki lasten julkiset avaimet niiden `xpub`-avaimista;

* `m / purpose' / coin-type' / account' / change / address-index` yksinkertaisesti osoittaa vastaanottavan osoitteen numeron ja sen avainparin, jotta se voidaan erottaa sen sisaruksista samalla syvyydellä samassa haarassa. Esimerkiksi ensimmäinen johdettu osoite on indeksillä `0`, toinen osoite on indeksillä `1`, ja niin edelleen...

Esimerkiksi, jos vastaanottava osoitteeni on johdatuspolulla `m / 86' / 0' / 0' / 0 / 5`, voimme päätellä seuraavat tiedot:
* `86'` osoittaa, että noudatamme BIP86:n (Taproot / SegWit V1) johdatusstandardia;
* `0'` osoittaa, että kyseessä on Bitcoin-osoite;
* `0'` osoittaa, että olemme lompakon ensimmäisellä tilillä;
* `0` osoittaa, että kyseessä on ulkoinen osoite;
* `5` osoittaa, että kyseessä on tämän tilin kuudes ulkoinen osoite.

![](../../dictionnaire/assets/18.png)