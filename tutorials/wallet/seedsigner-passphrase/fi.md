---
name: BIP-39 passphrase Siemenen allekirjoittaja
description: Miten lisään passphrase:n SeedSigner-salkkuuni?
---

![cover](assets/cover.webp)



passphrase BIP39 on valinnainen salasana, joka yhdessä Mnemonic-lauseen kanssa tarjoaa Layer lisäturvaa deterministisille ja hierarkkisille Bitcoin-lompakoille. Tässä opetusohjelmassa selvitämme yhdessä, miten passphrase voidaan määrittää Bitcoin Wallet:een, jota käytetään SeedSignerin kanssa.



![Image](assets/fr/01.webp)



## Edellytykset ennen passphrase:n lisäämistä



Ennen tämän opetusohjelman aloittamista, jos et tunne passphrase-käsitettä, sen toimintaa ja sen vaikutuksia Bitcoin Wallet:een, suosittelen, että tutustut tähän toiseen teoreettiseen artikkeliin, jossa selitän kaiken (tämä on erittäin tärkeää, koska passphrase:n käyttäminen ilman, että ymmärrät täysin, miten se toimii, voi vaarantaa bitcoinisi) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Varmista ennen tämän ohjeen aloittamista, että olet jo alustanut SeedSignerisi ja luonut Mnemonic-lauseen. Jos et ole vielä alustanut ja SeedSignerisi on aivan uusi, seuraa Plan ₿ Academyn ohjetta. Kun olet suorittanut tämän vaiheen, voit palata tähän opetusohjelmaan:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Miten lisään passphrase:n SeedSigneriin?



passphrase:n lisääminen SeedSignerin kautta hallinnoituun salkkuun luo täysin uuden salkun, joka luo täysin erillisen avainsarjan. Jos sinulla on jo salkku, joka sisältää Satssin, et voi enää käyttää sitä passphrase:llä, koska se luo täysin erilaisen salkun.



Jos haluat soveltaa passphrase:tä SeedSigneriin, kytke laite päälle ja skannaa SeedQR tavalliseen tapaan. SeedSigner näyttää tämän jälkeen nykyisen Wallet:n sormenjäljen, joka vastaa sitä, jossa ei ole passphrase:tä**. Wallet:lla, jossa on passphrase, on eri sormenjälki.



Napsauta painiketta "BIP-39 passphrase".



![Image](assets/fr/02.webp)



Kirjoita sitten valitsemasi passphrase-numero näyttöön tulevan näppäimistön avulla sille varattuun kenttään. Muista tehdä yksi tai useampi fyysinen varmuuskopio (paperi tai metalli): passphrase:n menettäminen johtaa siihen, että bitcoinisi eivät ole enää pysyvästi käytettävissä. ** Wallet:n palauttamiseksi sekä Mnemonic että passphrase ovat välttämättömiä ** Jos jompikumpi niistä katoaa, bitcoinisi estetään peruuttamattomasti.



Kun olet tehnyt merkintääsi, vahvista se painamalla `KEY3`-painiketta SeedSignerin oikeassa alakulmassa.



![Image](assets/fr/03.webp)



*Tässä esimerkissä käytin passphrase:ta `pba`. Varmista kuitenkin, että valitset sinun tapauksessasi vankan passphrase:n. Optimaalisen passphrase:n määrittelystä saat tietoa tästä toisesta artikkelista: *



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner näyttää sitten passphrase Wallet:n uuden sormenjäljen. Tee tästä sormenjäljestä useita kopioita: se on tärkeää, kun käytät Wallet:tä passphrase:n kanssa, sillä sen avulla voit joka kerta, kun syötät passphrase:n, tarkistaa, ettet ole tehnyt kirjoitusvirheitä ja että käytät oikeaa Wallet:tä.



Jos esimerkiksi minun tapauksessani kirjoitan virheellisesti passphrase `Pba` SeedSigneria käynnistäessäni `pba`:n sijasta, tämä yksinkertainen muutos pienestä isoon kirjaimeen johtaa siihen, että luodaan täysin eri salkku kuin se, jota haluan käyttää.



Tämä sormenjälki ei vaaranna Wallet:n turvallisuutta tai luottamuksellisuutta. Se ei paljasta mitään julkisia tai yksityisiä tietoja avaimista. Toisin kuin Mnemonic:ssä ja passphrase:ssa, voit tallentaa sormenjäljen digitaaliselle tietovälineelle. Suosittelen, että säilytät kopion useissa paikoissa: paperilla, salasanahallinnassa jne.



Kun olet tallentanut sormenjälkesi, napsauta `Done`.



![Image](assets/fr/04.webp)



Tämän jälkeen sinulla on pääsy kaikkiin salkkusi toimintoihin, aivan kuten perinteisessä SeedSignerissä.



![Image](assets/fr/05.webp)



Voit nyt tuoda avainsäilön Sparrow wallet:ään ja käyttää Wallet:tä normaalisti. Joka kerta kun käynnistät uudelleen, sinun on skannattava SeedQR ja syötettävä passphrase uudelleen näppäimistöllä, kuten tässä tehtiin.



Ennen kuin käytät Wallet:ääsi passphrase:n kanssa, suosittelen, että teet täydellisen tyhjän palautustestin. Näin voit varmistaa, että Mnemonic-lauseesi ja passphrase:n varmuuskopiot ovat voimassa. Katso seuraava opetusohjelma, jossa kerrotaan, miten tämä tarkistus tehdään:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895