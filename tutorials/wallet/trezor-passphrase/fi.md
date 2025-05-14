---
name: passphrase BIP39 Trezor
description: Miten lisään passphrase:n Trezor-salkkuuni?
---
![cover](assets/cover.webp)



passphrase BIP39 on valinnainen salasana, joka yhdessä Mnemonic-lauseen kanssa tarjoaa Layer lisäturvaa deterministisille ja hierarkkisille Bitcoin-salkuille. Tässä opetusohjelmassa selvitämme yhdessä, miten passphrase asetetaan turvalliseen Bitcoin Wallet Trezoriin (Safe 3, Safe 5 ja Model One).



![Image](assets/fr/01.webp)



Ennen tämän opetusohjelman aloittamista, jos et tunne passphrase-käsitettä, sen toimintaa ja sen vaikutuksia Bitcoin Wallet:ään, suosittelen, että tutustut tähän toiseen teoreettiseen artikkeliin, jossa selitän kaiken (tämä on erittäin tärkeää, koska passphrase:n käyttäminen ilman, että ymmärrät täysin, miten se toimii, voi vaarantaa bitcoinisi) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase Trezorissa käsitellään klassisella tavalla, jos olet valinnut BIP39-standardin määrityksen aikana (mitä suosittelen, jos et tarvitse *Multi-share Backup*). Trezorissa on erikoista se, että voit syöttää passphrase:n joko suoraan Hardware Wallet:ssä tai tietokoneen näppäimistön kautta Trezor Suite -ohjelmiston avulla. Jälkimmäinen vaihtoehto on huomattavasti vähemmän turvallinen, koska tietokoneella on huomattavasti suurempi hyökkäyspinta kuin Hardware Wallet:llä. Monimutkaisen passphrase:n kirjoittaminen voi kuitenkin olla nopeampaa tavallisella näppäimistöllä kuin Hardware Wallet:llä, mikä voi kannustaa käyttämään vahvoja salasanoja. On siis aina parempi käyttää passphrase:tä, vaikka se jouduttaisiinkin kirjoittamaan, kuin olla käyttämättä sitä lainkaan. On kuitenkin tärkeää olla tietoinen siitä, että tämä lisää numeeristen hyökkäysten riskiä.



Nämä vaihtoehdot eivät ole käytettävissä kaikissa Trezor-yhteensopivissa salkunhallintaohjelmistoissa. Esimerkiksi Model One -mallissa passphrase voidaan syöttää Sparrow Wallet:n näppäimistön kautta. Model T-, Safe 3- ja Safe 5 -malleissa on joko käytettävä Trezor Suite -ohjelmaa tai syötettävä passphrase suoraan Hardware Wallet:een, koska HWI poisti Sparrow'n kautta tapahtuvan syötön mahdollisuuden käytöstä muutama vuosi sitten.



![Image](assets/fr/02.webp)



Trezor Suitessa on kaksi eri tapaa hallita passphrase-kysyntää. Voit aktivoida "*passphrase*"-vaihtoehdon "*Laite*"-välilehdellä. Jos se on aktivoitu, Trezor Suite ja kaikki muut salkunhallintaohjelmistot pyytävät sinua järjestelmällisesti syöttämään passphrase:n aina käynnistyksen yhteydessä. Jos haluat passphrase:n käyttöä huomaamattomammin, voit pitää asetuksen "*Standard*". Tässä tapauksessa sinun on mentävä manuaalisesti Hardware Wallet:n valikkoon vasemmassa yläkulmassa ja napsautettava "*+ passphrase*"-painiketta joka kerta, kun käynnistät sen.



Varmista ennen tämän ohjeen aloittamista, että olet jo alustanut Trezorin ja luonut Mnemonic-lauseen. Jos et ole vielä aloittanut ja Trezorisi on uusi, noudata Plan ₿ Network:stä löytyvää mallikohtaista ohjetta. Kun olet suorittanut tämän vaiheen, voit palata tähän opetusohjelmaan.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## passphrase:n lisääminen Safe 3:een tai Safe 5:een



Kun olet luonut Wallet:n, tallentanut Mnemonic:n ja asettanut PIN-koodin, pääset Trezor Suiten kotivalikkoon. Vasemmassa yläkulmassa pitäisi näkyä ikkuna, jossa sinua kehotetaan aktivoimaan passphrase BIP39.



![Image](assets/fr/03.webp)



Jos tämä ikkuna ei tule näkyviin, sinun on aktivoitava "*passphrase*"-vaihtoehto manuaalisesti "*Laite*"-asetukset-välilehdellä.



![Image](assets/fr/04.webp)



Tässä ikkunassa sinua pyydetään syöttämään passphrase. Valitse vahva passphrase ja tee välittömästi fyysinen varmuuskopio esimerkiksi paperille tai metallille. Tässä esimerkissä olen valinnut passphrase:n: `fH3&kL@9mP#2sD5qR!82`. Tämä on esimerkki; suosittelen kuitenkin, että valitset hieman pidemmän passphrase:n. Ihanteellinen olisi 30-40 merkkiä (kuten hyvä salasana).



tietenkään sinun ei pitäisi koskaan jakaa passphrase:täsi Internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkiä Wallet:stä käytetään vain Testnet:ssa, ja se poistetaan ohjeen lopussa.**_



Jos haluat tarkempia suosituksia passphrase:n valinnasta, pyydän sinua jälleen kerran tutustumaan tähän toiseen artikkeliin:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jos haluat syöttää passphrase:n tietokoneen näppäimistöllä, syötä se sille varattuun kenttään ja napsauta sitten "*Access passphrase Wallet*".



![Image](assets/fr/05.webp)



Hardware Wallet näyttää sitten passphrase:n. Varmista, että se vastaa fyysistä varmuuskopiotasi (paperia tai metallia), ennen kuin napsautat näyttöä jatkaaksesi.



![Image](assets/fr/06.webp)



Näin pääset käsiksi passphrase-suojattuun salkkuusi.



![Image](assets/fr/07.webp)



Jos haluat parantaa turvallisuutta syöttämällä passphrase:n vain Trezoriin, napsauta kehotettaessa "*Enter passphrase on Trezor*".



![Image](assets/fr/08.webp)



Trezoriin ilmestyy T9-näppäimistö, jonka avulla voit syöttää passphrase:n. Kun olet saanut syöttösi valmiiksi, napsauta Green-rastia soveltaaksesi passphrase:tä Wallet:een.



![Image](assets/fr/09.webp)



Sen jälkeen sinulla on pääsy passphrase:n turvalliseen Wallet:ään.



![Image](assets/fr/10.webp)



Sparrow Wallet:n käyttämiseksi menettely on samanlainen, mutta mallien T, Safe 3 ja Safe 5 osalta passphrase on syötettävä Hardware Wallet:llä eikä tietokoneen näppäimistöllä.



Aina kun Sparrow Wallet vaatii pääsyä Trezoriin, eikä passphrase:a ole vielä sovellettu edellisen käynnistyksen jälkeen, sinun on syötettävä se T9-näppäimistöllä.



![Image](assets/fr/11.webp)



## passphrase:n lisääminen Model One -malliin



Model One -mallissa passphrase BIP39:n käyttö on lähes välttämätöntä. Koska tässä laitteessa ei ole turvallista elementtiä, arkaluonteisten tietojen poimiminen on suhteellisen helppoa. Se ei siis ole fyysisten hyökkäysten kestävä. Koska passphrase ei kuitenkaan säily laitteessa sen jälkeen, kun se on sammutettu, vahvan (ei murtokelpoisen) passphrase:n käyttö voi suojata useimpia tunnettuja fyysisiä hyökkäyksiä vastaan tässä mallissa.



Model One -mallissa passphrase:aan ei voi syöttää suoraan Hardware Wallet:ää. Se on syötettävä tietokoneen näppäimistön kautta.



Kun olet luonut Wallet:n, tallentanut Mnemonic:n ja asettanut PIN-koodin, pääset Trezor Suiten aloitusvalikkoon. Vasemmassa yläkulmassa pitäisi näkyä ikkuna, jossa sinua pyydetään aktivoimaan passphrase BIP39.



![Image](assets/fr/12.webp)



Jos tämä ikkuna ei tule näkyviin, sinun on aktivoitava "*passphrase*"-vaihtoehto asetusten "*Laite*"-välilehdellä.



![Image](assets/fr/13.webp)



Tässä ikkunassa sinua pyydetään syöttämään passphrase. Valitse vahva passphrase ja tee välittömästi fyysinen varmuuskopio esimerkiksi paperille tai metallille. Tässä esimerkissä olen valinnut passphrase:n: `fH3&kL@9mP#2sD5qR!82`. Tämä on vain esimerkki; suosittelen kuitenkin, että valitset hieman pidemmän passphrase:n. Ihanteellinen olisi 30-40 merkkiä (kuten hyvä salasana).



Jos haluat tarkempia suosituksia passphrase:n valinnasta, pyydän sinua jälleen kerran tutustumaan tähän toiseen artikkeliin:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kirjoita passphrase-korttisi sille varattuun kenttään ja napsauta sitten "*Access passphrase Wallet*" -painiketta.



![Image](assets/fr/14.webp)



Hardware Wallet näyttää passphrase:n. Varmista, että se vastaa fyysistä varmuuskopiotasi (paperi tai metalli), ja jatka sitten klikkaamalla oikeanpuoleista painiketta.



![Image](assets/fr/15.webp)



Tämä vie sinut passphrase-suojattuun salkkuusi.



![Image](assets/fr/16.webp)



Sparrow Wallet:n käyttö tämän jälkeen tapahtuu samalla tavalla. Aina kun Sparrow vaatii pääsyä Hardware Wallet:een, eikä passphrase:tä ole syötetty laitteen viimeisimmän käynnistyksen jälkeen, sinun on syötettävä se.



![Image](assets/fr/17.webp)



Onneksi olkoon, olet nyt valmis käyttämään passphrase BIP39:ää Trezor-laitteiston lompakoissa. Jos haluat viedä Wallet:n turvallisuuden askeleen pidemmälle, tutustu tähän Trezorin *Multi-share*-varmuuskopiointijärjestelmiä käsittelevään oppaaseen (*Shamirin salainen jakojärjestelmä*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!