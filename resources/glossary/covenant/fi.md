---
term: COVENANT

---
Mekanismi, joka mahdollistaa tiettyjen ehtojen asettamisen sille, miten tietty valuutta voidaan käyttää, myös tulevissa transaktioissa. UTXO:n käsikirjoituskielen tavallisesti sallimien ehtojen lisäksi liitto asettaa lisärajoituksia sille, miten tämä Bitcoin voidaan käyttää myöhemmissä transaktioissa. Teknisesti ottaen sopimus syntyy, kun UTXO:n `scriptPubKey` määrittelee rajoituksia UTXO:n käyttävän transaktion tuotosten `scriptPubKey`:lle. Laajentamalla käsikirjoituksen soveltamisalaa liitot mahdollistaisivat lukuisia Bitcoinin kehityskohteita, kuten drivechainsin kahdenvälisen ankkuroinnin, holvien toteuttamisen tai Lightningin kaltaisten overlay-järjestelmien parantamisen. Covenant-ehdotukset erotellaan kolmen kriteerin perusteella:


- Niiden soveltamisala;
- Niiden täytäntöönpano;
- Niiden toistuvuus.

On monia ehdotuksia, jotka mahdollistaisivat Bitcoin-kovenanttien käytön. Toteutuksessa pisimmälle edenneet ovat: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) ja `OP_VAULT`. Muita ehdotuksia ovat mm: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` jne.

Jotta ymmärtäisit paremmin liiton käsitteen, ajattele seuraavaa analogiaa: kuvittele kassakaappi, jossa on 500 euroa pieninä seteleinä. Jos onnistut avaamaan kassakaapin oikealla avaimella, voit käyttää rahat haluamallasi tavalla. Tämä on normaali tilanne Bitcoinin kanssa. Kuvittele nyt, että samassa kassakaapissa ei ole 500€ seteleinä, vaan samanarvoisia ateriakuponkeja. Jos onnistut avaamaan tämän kassakaapin, voit käyttää tämän summan. Kulutusvapautesi on kuitenkin rajoitettu, sillä voit käyttää näitä arvoseteleitä vain tietyissä ravintoloissa maksamiseen. Rahan käyttämiselle on siis ensimmäinen edellytys, eli sinun on onnistuttava avaamaan kassakaappi asianmukaisella avaimella. Mutta on myös lisäehto, joka koskee tämän summan tulevaa käyttöä: se on käytettävä yksinomaan kumppaniravintoloissa, eikä vapaasti. Tätä tulevia liiketoimia koskevien rajoitusten järjestelmää kutsutaan sopimukseksi (covenant).

> ► *Ranskaksi ei ole olemassa termiä, joka täsmällisesti kuvaisi sanan "liitto" merkitystä. Voidaan puhua "lausekkeesta", "sopimuksesta" tai "sitoumuksesta", mutta ne eivät vastaa täsmälleen termiä "liitto". Tämä termi on lainattu oikeusterminologiasta, jonka avulla voidaan kuvata sopimuslauseketta, jolla asetetaan kiinteistölle pysyviä velvoitteita*