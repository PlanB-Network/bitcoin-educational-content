---
termi: OUTPUT SCRIPT DESCRIPTORS
---

Output script descriptorit eli yksinkertaisesti descriptorit ovat rakenteellisia ilmaisuja, jotka kuvaavat täydellisesti ulostulon skriptin (`scriptPubKey`) ja tarjoavat kaikki tarvittavat tiedot tiettyyn skriptiin liittyvien transaktioiden seuraamiseksi. Nämä descriptorit helpottavat avainten hallintaa HD-lompakoissa tarjoamalla standardikuvauksen käytettyjen osoitteiden rakenteesta ja tyypeistä.

Descriptorien päätarkoitus on niiden kyky kapseloida kaikki olennainen tieto lompakon palauttamiseksi yhteen merkkijonoon (lisäksi palautuslausekkeeseen). Tallentamalla descriptor vastaavien mnemonic-lauseiden kanssa on mahdollista palauttaa ei ainoastaan yksityiset avaimet, vaan myös tarkka lompakon rakenne ja siihen liittyvät skriptiparametrit. Todellakin, lompakon palauttaminen vaatii ei ainoastaan alkuperäisen siemenen tuntemista, vaan myös tiettyjä indeksejä lapsiavainparien johdannaisille sekä `xpub` kunkin tekijän tapauksessa multisig-lompakossa. Aiemmin oletettiin, että tämä tieto oli kaikkien tiedossa implisiittisesti. Kuitenkin, skriptien monipuolistuessa ja monimutkaisempien konfiguraatioiden esiin tullessa, tämä tieto voisi tulla vaikeaksi ekstrapoloida, muuttaen nämä tiedot yksityisiksi ja vaikeiksi bruteforce-tiedoksi. Descriptorien käyttö huomattavasti yksinkertaistaa prosessia: riittää tietää palautuslause(et) ja vastaava descriptor kaiken luotettavasti ja turvallisesti palauttamiseksi.

Descriptor koostuu useista elementeistä:
* Skriptifunktiot kuten `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Moniallekirjoitus), ja `sortedmulti` (Moniallekirjoitus järjestetyillä avaimilla);
* Johdannaispolkuja, esimerkiksi `[d34db33f/44h/0h/0h]` osoittaen johdetun polun ja tietyn pääavaimen sormenjäljen;
* Avaimia eri muodoissa kuten heksadesimaaliset julkiset avaimet tai laajennetut julkiset avaimet (`xpub`);
* Tarkistussumma, jota edeltää hajautus, descriptorin eheyden varmistamiseksi.

Esimerkiksi descriptor P2WPKH-lompakolle voisi näyttää tältä:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
Tässä descriptorissa johdannaisfunktio `wpkh` osoittaa Pay-to-Witness-Public-Key-Hash skriptityypin. Sitä seuraa johdannaispolku, joka sisältää:
* `cdeab12f`: pääavaimen sormenjäljen;
* `84h`: joka merkitsee BIP84 tarkoitusta, tarkoitettu SegWit v0 osoitteille;
* `0h`: joka osoittaa, että kyseessä on BTC-valuutta pääverkossa;
* `0h`: joka viittaa lompakossa käytettyyn tiettyyn tilinumeroon.

Descriptor sisältää myös tässä lompakossa käytetyn laajennetun julkisen avaimen:
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

Seuraavaksi merkintä `/<0;1>/*` määrittelee, että kuvaaja voi generoida osoitteita ulkoisesta (`0`) ja sisäisestä (`1`) ketjusta, ja jokerimerkki (`*`) mahdollistaa useiden osoitteiden sekventiaalisen johdannan konfiguroitavalla tavalla, samankaltaisesti kuin perinteisen lompakko-ohjelmiston "gap limitin" hallinnassa.

Lopuksi, `#jy0l7nr4` edustaa tarkistussummaa, jolla varmistetaan kuvaajan eheyden.