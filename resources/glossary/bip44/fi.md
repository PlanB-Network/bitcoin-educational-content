---
term: BIP44

---
Parannusehdotus, jossa otetaan käyttöön vakiomuotoinen hierarkkinen johdannaisrakenne HD-lompakoille. BIP44 perustuu BIP32:ssa vahvistettuihin periaatteisiin avainten johtamisen osalta ja BIP43:een "purpose"-kentän käytön osalta. Siinä otetaan käyttöön viisitasoinen johdannaisrakenne: `m / purpose' / coin_type' / account' / change / address_index`. Seuraavassa on kunkin syvyyden yksityiskohdat:


- `m /` tarkoittaa yksityistä pääavainta. Se on ainutlaatuinen lompakolle, eikä sillä voi olla sisaruksia samalla syvyydellä. Pääavain johdetaan suoraan lompakon siemenestä;
- `m / purpose' /` ilmaisee johdannaistarkoituksen, joka auttaa tunnistamaan noudatettavan standardin. Tämä kenttä on kuvattu BIP43:ssa. Jos lompakko esimerkiksi noudattaa BIP84-standardia (SegWit V0), indeksi on `84'`;
- `m / purpose' / coin-type' /` ilmaisee kryptovaluutan tyypin. Tämä mahdollistaa selkeän erottelun yhdelle kryptovaluutalle ja toiselle kryptovaluutalle omistettujen haarojen välillä usean kolikon lompakossa. Bitcoinille omistettu indeksi on `0'`;
- `m / purpose' / coin-type' / account' /` ilmaisee tilinumeron. Tämä syvyys mahdollistaa lompakon helpon erottelun ja organisoinnin eri tileihin. Nämä tilit numeroidaan alkaen `0'`. Laajennetut avaimet (`xpub`, `xprv`...) löytyvät tästä syvyydestä;
- `m / tarkoitus' / kolikkotyyppi' / tili' / vaihtorahat /` osoittaa ketjun. Kullakin syvyydessä 3 määritellyllä tilillä on syvyydessä 4 kaksi ketjua: ulkoinen ketju ja sisäinen ketju (jota kutsutaan myös "muutokseksi"). Ulkoisesta ketjusta saadaan osoitteet, jotka on tarkoitettu julkisesti välitettäviksi, eli osoitteet, joita tarjotaan meille, kun klikkaamme lompakko-ohjelmistossamme "vastaanottaa". Sisäisessä ketjussa on osoitteita, joita ei ole tarkoitus vaihtaa julkisesti, eli pääasiassa muutososoitteita. Ulkoinen ketju tunnistetaan indeksillä `0` ja sisäinen ketju indeksillä `1`. Huomaat, että tästä syvyydestä lähtien emme enää tee karkaistua derivaatiota, vaan tavallista derivaatiota (ei ole apostrofia). Tämän mekanismin ansiosta pystymme johtamaan kaikki julkiset lapsiavaimet niiden `xpub`:sta;
- `m / purpose' / coin-type' / account' / change / address-index` ilmoittaa yksinkertaisesti vastaanottavan osoitteen numeron ja sen avainparin, jotta se voidaan erottaa samassa haarassa samassa syvyydessä olevista sisaruksista. Esimerkiksi ensimmäisellä johdetulla osoitteella on indeksi `0`, toisella osoitteella on indeksi `1` ja niin edelleen...

Jos esimerkiksi vastaanottavassa osoitteessani on derivaatiopolku `m / 86' / 0' / 0' / 0 / 5`, voimme päätellä seuraavat tiedot:


- `86'` tarkoittaa, että noudatamme BIP86:n johdannaisstandardia (Taproot tai SegWitV1);
- `0'` tarkoittaa, että kyseessä on Bitcoin-osoite;
- `0'` tarkoittaa, että olemme lompakon ensimmäisellä tilillä;
- "0" tarkoittaa, että kyseessä on ulkoinen osoite;
- "5" tarkoittaa, että kyseessä on tämän tilin kuudes ulkoinen osoite.

![](../../dictionnaire/assets/18.webp)