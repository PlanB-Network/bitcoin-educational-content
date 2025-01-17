---
term: JOHDANNAISPOLKU

---
Hierarkkisen deterministisen (HD) lompakon yhteydessä derivaatiopolulla tarkoitetaan indeksien sarjaa, jota käytetään johdettaessa pääavaimesta lapsiavaimia. BIP32:ssa kuvattu polku määrittää puurakenteen, josta johdetaan lapsiavaimet. Derivointipolku on sarja viivaimilla erotettuja indeksejä, ja se alkaa aina pääavaimella (merkintä "m/"). Tyypillinen polku voi olla esimerkiksi `m/84'/0'/0'/0'/0/0`. Jokaiseen derivaatiotasoon liittyy tietty syvyys:


- `m /` tarkoittaa yksityistä pääavainta. Se on ainutlaatuinen lompakolle, eikä sillä voi olla sisaruksia samalla syvyydellä. Pääavain johdetaan suoraan siemenestä;
- `m / purpose' /` ilmaisee johdannaistarkoituksen, joka auttaa tunnistamaan noudatetun standardin. Tämä kenttä on kuvattu BIP43:ssa. Jos lompakko esimerkiksi noudattaa BIP84-standardia (SegWit V0), indeksi on `84'`;
- `m / purpose' / coin-type' /` ilmaisee kryptovaluutan tyypin. Tämä mahdollistaa selkeän erottelun yhdelle kryptovaluutalle ja toiselle kryptovaluutalle omistettujen haarojen välillä usean kolikon lompakossa. Bitcoinille omistettu indeksi on `0'`;
- `m / purpose' / coin-type' / account' /` ilmaisee tilinumeron. Tämä syvyys helpottaa lompakon erottamista ja järjestämistä eri tileihin. Nämä tilit numeroidaan alkaen `0'`. Laajennetut avaimet (`xpub`, `xprv`...) löytyvät tältä syvyystasolta;
- `m / purpose' / coin-type' / account' / change /` osoittaa polun. Kullakin syvyydellä 3 määritellyllä tilillä on kaksi polkua syvyydellä 4: ulkoinen ketju ja sisäinen ketju (jota kutsutaan myös "muutokseksi"). Ulkoinen ketju johtaa osoitteet, jotka on tarkoitettu jaettavaksi julkisesti, eli osoitteet, joita meille tarjotaan, kun klikkaamme "vastaanottaa" lompakko-ohjelmistossamme. Sisäisessä ketjussa on osoitteita, joita ei ole tarkoitus vaihtaa julkisesti, eli lähinnä muutososoitteita. Ulkoinen ketju tunnistetaan indeksillä `0` ja sisäinen ketju indeksillä `1`. Huomaat, että tästä syvyydestä alkaen emme enää tee karkaistua derivaatiota, vaan tavallista derivaatiota (ei ole apostrofia). Tämän mekanismin ansiosta pystymme johtamaan kaikki julkiset lapsiavaimet niiden `xpub`:sta;
- `m / purpose' / coin-type' / account' / change / address-index` ilmoittaa yksinkertaisesti vastaanottavan osoitteen numeron ja sen avainparin, jotta se voidaan erottaa samassa haarassa samassa syvyydessä olevista sisaruksista. Esimerkiksi ensimmäisellä johdetulla osoitteella on indeksi `0`, toisella osoitteella on indeksi `1` ja niin edelleen...

Jos esimerkiksi vastaanottavassa osoitteessani on derivaatiopolku `m / 86' / 0' / 0' / 0 / 5`, voimme päätellä seuraavat tiedot:


- `86'` tarkoittaa, että noudatamme BIP86:n johdannaisstandardia (Taproot / SegWit V1);
- `0'` tarkoittaa, että kyseessä on Bitcoin-osoite;
- `0'` tarkoittaa, että olemme lompakon ensimmäisellä tilillä;
- "0" tarkoittaa, että kyseessä on ulkoinen osoite;
- "5" tarkoittaa, että kyseessä on tämän tilin kuudes ulkoinen osoite.

![](../../dictionnaire/assets/18.webp)