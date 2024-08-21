---
termi: COVENANT
---

Mekanismi, joka mahdollistaa tiettyjen ehtojen asettamisen sille, miten tietty valuuttamäärä voidaan käyttää, mukaan lukien tulevissa transaktioissa. UTXO:n skriptikielen yleensä sallimien ehtojen lisäksi covenant asettaa lisärajoituksia sille, miten tätä Bitcoinia voidaan käyttää myöhemmissä transaktioissa. Teknisesti covenantin perustaminen tapahtuu, kun UTXO:n `scriptPubKey` määrittelee rajoituksia transaktion tulosteiden `scriptPubKey`-arvoille, jotka käyttävät kyseistä UTXO:a. Skriptin soveltamisalan laajentamisen myötä covenantit mahdollistaisivat useita kehityksiä Bitcoinissa, kuten drivechainien kahdenvälisen ankkuroinnin, holvien toteuttamisen tai overlay-järjestelmien, kuten Lightningin, parantamisen. Covenant-ehdotukset eroavat toisistaan kolmen kriteerin perusteella:
* Niiden soveltamisala;
* Niiden toteutus;
* Niiden rekursiivisuus.

On monia ehdotuksia, jotka mahdollistaisivat covenantien käytön Bitcoinissa. Kehittyneimmät toteutusprosessissa ovat: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) ja `OP_VAULT`. Muiden ehdotusten joukossa ovat: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` jne.

Ymmärtääksesi covenant-käsitteen paremmin, harkitse tätä analogiaa: kuvittele kassakaappi, joka sisältää 500€ pieninä seteleinä. Jos onnistut avaamaan tämän kassakaapin oikealla avaimella, olet vapaa käyttämään näitä rahoja haluamallasi tavalla. Tämä on normaali tilanne Bitcoinin kanssa. Kuvittele nyt, että sama kassakaappi ei sisälläkään 500€ seteleinä, vaan vastaavan arvon ateriakuponkeina. Jos onnistut avaamaan tämän kassakaapin, voit käyttää tätä summaa. Kuitenkin vapauttasi käyttää rahoja on rajoitettu, sillä voit käyttää näitä kuponkeja maksamiseen vain tietyissä ravintoloissa. Näin ollen on ensimmäinen ehto rahojen käyttämiseen, joka on onnistua avaamaan kassakaappi sopivalla avaimella. Mutta on myös lisäehto tulevalle rahojen käytölle: summa on käytettävä yksinomaan yhteistyökumppaniravintoloissa, eikä vapaasti. Tämä tulevien transaktioiden rajoitusten järjestelmä on sitä, mitä kutsutaan covenantiksi.

> ► *Ranskaksi ei ole termiä, joka tarkasti vangitsisi sanan "covenant" merkityksen. Voitaisiin puhua "lausekkeesta", "sopimuksesta" tai "sitoumuksesta", mutta nämä eivät täsmälleen vastaisi termiä "covenant". Tämä termi on lainattu oikeudellisesta terminologiasta, joka mahdollistaa sopimuslausekkeen kuvaamisen, joka asettaa pysyviä velvoitteita omaisuudelle.*