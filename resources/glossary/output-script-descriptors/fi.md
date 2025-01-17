---
term: OUTPUT SCRIPT DESCRIPTORS

---
Tulostusskriptin kuvaajat tai yksinkertaisesti kuvaajat ovat jäsenneltyjä lausekkeita, jotka kuvaavat täysin tulostusskriptin (`scriptPubKey`) ja antavat kaikki tarvittavat tiedot tiettyyn skriptiin tai tietystä skriptistä tapahtuvien tapahtumien seuraamiseksi. Nämä kuvaajat helpottavat avainten hallintaa HD-lompakoissa käyttämällä vakiomuotoista kuvausta rakenteesta ja käytetyistä osoitetyypeistä.

Kuvaajien tärkein etu on niiden kyky sisällyttää kaikki lompakon palauttamisen kannalta olennaiset tiedot yhteen merkkijonoon (palautuslausekkeen lisäksi). Tallentamalla kuvaaja ja vastaavat muistilausekkeet on mahdollista palauttaa yksityisten avainten lisäksi myös lompakon tarkka rakenne ja siihen liittyvät komentosarjaparametrit. Lompakon palauttaminen edellyttää nimittäin paitsi alkuperäisen siemenen tuntemista myös erityisiä indeksejä lapsiavainparien johtamista varten sekä kunkin tekijän `xpub`, jos kyseessä on multisig-lompakko. Aiemmin oletettiin, että kaikki tietävät nämä tiedot epäsuorasti. Skriptien monipuolistuessa ja monimutkaisempien kokoonpanojen syntyessä näitä tietoja voi kuitenkin olla vaikea ekstrapoloida, mikä tekee näistä tiedoista yksityisiä ja vaikeasti murrettavissa olevia tietoja. Kuvaajien käyttö yksinkertaistaa prosessia huomattavasti: riittää, että tunnet palautuslauseen (-lauseet) ja vastaavan kuvaajan, jotta voit palauttaa kaiken luotettavasti ja turvallisesti.

Kuvaaja koostuu useista elementeistä:


- Skriptitoiminnot kuten `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) ja `sortedmulti` (Multisignature lajitelluilla avaimilla);
- Johdannaispolut, esimerkiksi `[d34db33f/44h/0h/0h]`, joka osoittaa johdetun polun ja tietyn pääavaimen sormenjäljen;
- Avaimet eri muodoissa, kuten heksadesimaaliset julkiset avaimet tai laajennetut julkiset avaimet (`xpub`);
- Tarkastussumma, jota edeltää hash, kuvaajan eheyden tarkistamiseksi.

Esimerkiksi P2WPKH-lompakon kuvaaja voisi näyttää seuraavalta:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

Tässä kuvaajassa johdannaisfunktio `wpkh` tarkoittaa Pay-to-Witness-Public-Key-Hash-skriptityyppiä. Sitä seuraa johdannaispolku, joka sisältää:


- `cdeab12f`: pääavaimen sormenjälki;
- `84h`: tarkoittaa BIP84-tarkoituksen käyttöä, joka on tarkoitettu SegWit v0 -osoitteille;
- `0h`: mikä osoittaa, että kyseessä on BTC-valuutta pääverkossa;
- `0h`: viittaa lompakossa käytettyyn tilinumeroon.

Kuvaus sisältää myös tässä lompakossa käytetyn laajennetun julkisen avaimen:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Seuraavaksi merkintä `/<0;1>/*` määrittää, että kuvaaja voi luoda osoitteita ulkoisesta (`0`) ja sisäisestä (`1`) ketjusta, ja jokerimerkki (`*`) mahdollistaa useiden osoitteiden peräkkäisen johtamisen konfiguroitavissa olevalla tavalla, joka on samanlainen kuin perinteisen lompakko-ohjelmiston "aukkorajan" hallinta.

Lopuksi `#jy0l7nr4` edustaa tarkistussummaa, jolla tarkistetaan kuvaajan eheys.