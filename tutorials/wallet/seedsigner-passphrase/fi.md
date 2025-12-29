---
name: BIP-39 Passphrase SeedSigner
description: Miten lisään passphrase:n SeedSigner-salkkuuni?
---

![cover](assets/cover.webp)



passphrase BIP39 on valinnainen salasana, joka yhdistettynä muistilausekkeeseen tarjoaa lisäturvan deterministisille ja hierarkkisille Bitcoin-lompakoille. Tässä opetusohjelmassa selvitämme yhdessä, miten passphrase voidaan asentaa Bitcoin wallet:ään, jota käytetään SeedSignerin kanssa.



![Image](assets/fr/01.webp)



## Edellytykset ennen salasanan lisäämistä



Ennen tämän opetusohjelman aloittamista, jos et tunne passphrase-käsitettä, sen toimintaa ja sen vaikutuksia Bitcoin wallet:ään, suosittelen, että tutustut tähän toiseen teoreettiseen artikkeliin, jossa selitän kaiken (tämä on erittäin tärkeää, koska passphrase:n käyttäminen ilman, että ymmärrät täysin, miten se toimii, voi vaarantaa bitcoinisi) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Varmista ennen tämän ohjeen aloittamista, että olet jo alustanut SeedSignerisi ja luonut muistilauseen. Jos et ole vielä alustanut ja SeedSignerisi on aivan uusi, seuraa Plan ₿ Academyn opetusohjelmaa. Kun olet suorittanut tämän vaiheen, voit palata tähän opetusohjelmaan:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Miten lisään passphrase:n SeedSigneriin?



passphrase:n lisääminen SeedSignerin kautta hallinnoituun salkkuun luo täysin uuden salkun, joka luo täysin erillisen avainsarjan. Jos sinulla on jo salkku, joka sisältää satssin, et voi enää käyttää sitä passphrase:llä, koska se luo täysin erilaisen salkun.



Jos haluat soveltaa passphrase:tä SeedSigneriin, kytke laite päälle ja skannaa SeedQR tavalliseen tapaan. Sen jälkeen SeedSigner näyttää nykyisen wallet:n sormenjäljen, joka vastaa sormenjälkeä, jossa ei ole passphrase:tä**. wallet:llä, jossa on passphrase, on eri sormenjälki.



Napsauta painiketta `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Kirjoita sitten haluamasi passphrase-numero näyttöön tulevan näppäimistön avulla sille varattuun kenttään. Muista tehdä yksi tai useampi fyysinen varmuuskopio (paperi tai metalli): passphrase:n menettäminen johtaa siihen, että bitcoinisi eivät ole enää pysyvästi käytettävissä. ** wallet:n palauttamiseksi sekä muistisääntö että passphrase ovat välttämättömiä ** Jos jompikumpi niistä katoaa, bitcoinisi estetään peruuttamattomasti.



Kun olet tehnyt merkintääsi, vahvista se painamalla `KEY3`-painiketta SeedSignerin oikeassa alakulmassa.



![Image](assets/fr/03.webp)



*Tässä esimerkissä käytin passphrase `pba`. Varmista kuitenkin, että valitset sinun tapauksessasi vankan passphrase:n. Optimaalisen passphrase:n määrittelystä saat tietoa tästä toisesta artikkelista: *



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sen jälkeen SeedSigner näyttää passphrase wallet:n uuden sormenjäljen. Tee tästä sormenjäljestä useita kopioita: se on tärkeää, kun käytät wallet:ää passphrase:n kanssa, sillä sen avulla voit tarkistaa joka kerta, kun syötät passphrase:n, ettet ole tehnyt kirjoitusvirheitä ja että käytät oikeaa wallet:ää.



Jos esimerkiksi minun tapauksessani kirjoitan SeedSigneria käynnistäessäni virheellisesti passphrase `Pba` eikä `pba`, tämä yksinkertainen muutos pienistä kirjaimista isoihin kirjaimiin johtaa siihen, että luodaan täysin eri salkku kuin se, jota haluan käyttää.



Tämä sormenjälki ei vaaranna wallet:n turvallisuutta tai luottamuksellisuutta. Se ei paljasta mitään julkisia tai yksityisiä tietoja avaimista. Toisin kuin muistitikun ja passphrase:n, voit siis tallentaa sormenjäljen digitaaliselle tietovälineelle. Suosittelen, että säilytät kopion useissa paikoissa: paperilla, salasanahallinnassa jne.



Kun olet tallentanut sormenjälkesi, napsauta `Done`.



![Image](assets/fr/04.webp)



Tämän jälkeen sinulla on pääsy kaikkiin salkkusi toimintoihin, aivan kuten perinteisessä SeedSignerissä.



![Image](assets/fr/05.webp)



Voit nyt tuoda avainsäilön Sparrow:een Wallet:een ja käyttää wallet:tä normaalisti. Aina kun käynnistät järjestelmän uudelleen, sinun on skannattava SeedQR ja syötettävä passphrase uudelleen näppäimistöllä, kuten teimme tässä.



Ennen kuin käytät wallet:ta passphrase:n kanssa, suosittelen, että teet täyden tyhjän palautustestin. Näin voit varmistaa, että muistilauseen ja passphrase:n varmuuskopiot ovat voimassa. Katso seuraava opetusohjelma, jossa opit, miten tämä tarkistus tehdään:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895