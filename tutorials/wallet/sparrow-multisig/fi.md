---
name: Varpunen Wallet - Multisig
description: Luo monen allekirjoituksen salkku Sparrow'ssa
---
![cover](assets/cover.webp)



Usean allekirjoituksen Wallet (usein "Multisig*") on Bitcoin Wallet-rakenne, joka vaatii useita kryptografisia allekirjoituksia eri avaimilla menon hyväksymiseksi. Toisin kuin tavanomaisessa ("*singlesig*") Wallet:ssä, jossa yksi yksityinen avain riittää UTXO:n avaamiseen, Multisig perustuu **m-of-n**-malliin: Wallet:ään liittyvistä _n_ avaimesta _m_:n on ehdottomasti allekirjoitettava jokainen tapahtuma.



Tämän mekanismin avulla salkun hallinta voidaan jakaa useiden yksiköiden tai laitteiden kesken. Esimerkiksi 2-of-3-kokoonpanossa luodaan kolme erillistä avainsarjaa, mutta varojen vapauttamiseen tarvitaan vain kaksi. Tämä arkkitehtuuri vähentää huomattavasti avaimen vaarantumiseen tai katoamiseen liittyviä riskejä: varas, jolla on pääsy vain yhteen avaimeen, ei voi tyhjentää Wallet:ta, ja käyttäjä, joka menettää yhden avaimen, pääsee silti käsiksi varoihinsa kahdella muulla avaimella.



![Image](assets/fr/01.webp)



Suurempi turvallisuus merkitsee kuitenkin myös suurempaa monimutkaisuutta. Multisig Wallet:n perustaminen edellyttää useiden Mnemonic-lauseiden (yksi kutakin allekirjoitustekijää kohti) ja laajennettujen julkisten avainten ("*xpub*") varmistamista. Jos käytät Multisig 2-of-3 Wallet:ää, Wallet:n hakeminen edellyttää, että sinulla on joko kaikki kolme Mnemonic-lausetta tai vähintään kaksi näistä kolmesta lausekkeesta. Mutta jos sinulla on vain kaksi kolmesta lausekkeesta, tarvitset myös pääsyn kolmeen *xpubiin*, joita ilman on mahdotonta hakea julkisia avaimia, joita tarvitaan niiden suojaamien bitcoinien käyttämiseen.



Yhteenvetona voidaan todeta, että Multisig-salkun palauttamiseksi sinun on :




- Tai tutustu kaikkiin Mnemonic-lauseisiin, jotka liittyvät kuhunkin allekirjoitustekijään;
- Joko sinulla on kynnysarvon edellyttämä vähimmäismäärä Mnemonic-lauseita, jotta voit allekirjoittaa, ja sinulla on myös pääsy kaikkien tekijöiden xpubeihin, jotta voit hakea tarvittavat julkiset avaimet.



![Image](assets/fr/02.webp)



Multisig-salkun varmuuskopioiden hallintaa helpottavat *Output Script Descriptors*, jotka kokoavat yhteen kaikki julkiset tiedot, joita tarvitaan rahastojen käyttöön. Tätä toimintoa ei kuitenkaan ole vielä toteutettu kaikissa salkunhallintaohjelmistoissa.



Multisig soveltuu erityisesti bitcoin-käyttäjille, jotka haluavat parantaa turvallisuutta tai hallinnoida varoja kollektiivisesti: yrityksille, yhdistyksille, perheille tai yksittäisille käyttäjille, joilla on hallussaan merkittävä määrä bitcoineja. Sitä voidaan käyttää hajautettujen hallintojärjestelmien luomiseen, esimerkiksi allekirjoitusvaltuuksien jakamiseen useiden johtajien tai tiimin jäsenten kesken.



Tässä opetusohjelmassa opimme luomaan ja käyttämään klassista Wallet-monimerkkistä Wallet:tä **Sparrow Wallet**:llä. Jos haluat luoda räätälöidyn monimerkkisen salkun, jossa on aikamerkkejä, suosittelen sen sijaan Liana:n käyttöä:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Edellytykset



Tässä opetusohjelmassa näytän, miten Multisig tehdään [Sparrow Wallet -salkunhallintaohjelmistolla](https://sparrowwallet.com/download/). Jos et ole vielä asentanut tätä ohjelmistoa, tee se nyt. Jos tarvitset apua, meillä on myös yksityiskohtainen ohje Sparrow Wallet -ohjelmiston konfiguroinnista :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Usean allekirjoituksen Wallet:n perustamiseen tarvitset eri laitteistolompakoita. Esimerkiksi Multisig 2-de-3:ssa voit käyttää :




- Trezor Model One;
- Ledger Flex;
- Coldcard MK3.



![Image](assets/fr/03.webp)



Multisig-kokoonpanossa kannattaa käyttää eri Hardware Wallet-merkkisiä laitteita. Näin varmistetaan, että jos tietyssä mallissa ilmenee vakava ongelma, se ei vaikuta Multisig:n kokonaisturvallisuuteen. Lisäksi voit hyödyntää kunkin laitteen erityiset edut. Esimerkiksi minun kokoonpanossani :





- Trezor Model One on täysin avoimen lähdekoodin malli, mikä mahdollistaa seed-sukupolven tarkistamisen. Koska sitä ei kuitenkaan ole varustettu Secure Elementillä, se on edelleen altis fyysisille hyökkäyksille;





- Ledger Flex -laitteessa taas on tarkistamaton oma laiteohjelmisto, mutta siinä on Secure Element -järjestelmä, joka tarjoaa erinomaisen fyysisen suojan;





- Coldcard on varustettu Secure Elementillä, ja sen koodi on haettavissa. Se on mielenkiintoinen valinta kokoonpanoomme, sillä se tarjoaa todentamisominaisuuksia, joita muissa malleissa ei ole.



Varmista ennen Multisig Wallet:n konfigurointia, että jokainen Hardware Wallet on konfiguroitu oikein (Mnemonic:n luominen ja tallentaminen, PIN-koodin määrittely). Yksityiskohtaiset ohjeet saat kunkin Hardware Wallet:n ohjeista, esimerkiksi :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Kuten näemme myöhemmin tässä oppaassa, Multisig-konfiguraatioon on mahdollista liittää myös tekijä, joka ei ole yhteydessä Hardware Wallet:een, mutta jonka yksityiset avaimet on tallennettu tietokoneellesi. Tämä menetelmä on selvästi vähemmän turvallinen kuin laitteistolompakoiden yksinomainen käyttö, mutta se voi olla tarkoituksenmukainen tietyissä tapauksissa. Esimerkiksi Multisig 2-de-3 -järjestelmässä voit valita kaksi laitteistolompakkoa ja yhden Software Wallet:n.



## Multisig-salkun luominen



Avaa Sparrow Wallet, napsauta välilehteä "*File*" ja valitse sitten "*New Wallet*".



![Image](assets/fr/04.webp)



Määritä nimi monialakirjoitussalkullesi ja vahvista se napsauttamalla "*Luo Wallet*".



![Image](assets/fr/05.webp)



Valitse pudotusvalikosta "*Policy Type*" vaihtoehto "*Multi Signature*".



![Image](assets/fr/06.webp)



Oikeassa yläkulmassa voit nyt määritellä Multisig:n avainten kokonaismäärän sekä kulujen hyväksymiseen vaadittavien kanssakirjoittajien määrän. Esimerkissäni tämä on 2:sta 3:een -järjestelmä.



![Image](assets/fr/07.webp)



Ikkunan alareunassa Sparrow Wallet näyttää kolme "*Keystore*". Kukin edustaa avainsarjaa. Tässä käytän kolmea laitteistosalkkua, joten jokainen "*Keystore*" vastaa yhtä niistä. Määritämme nyt ne.



Aloitan Coldcardilla. "*Keystore 1*" -välilehdeltä valitsen vaihtoehdon "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Coldcardissa, kun laitteen lukitus on avattu, menen "*Settings*"-valikkoon ja sitten "*Multisig Wallets*" -valikkoon.



![Image](assets/fr/09.webp)



Tässä valikossa voit hallita Multisig-salkkuja, joihin Coldcard osallistuu. Haluan luoda uuden, joten valitsen "*Export XPUB*".



![Image](assets/fr/10.webp)



Jos hallinnoit vain yhtä tiliä, voit jättää kentän "*Tilin numero*" tyhjäksi ja vahvistaa sen suoraan painamalla vahvistuspainiketta.



![Image](assets/fr/11.webp)



Tämän jälkeen Coldcard generate tallentaa Micro SD-kortille tiedoston, joka sisältää xpubin.



![Image](assets/fr/12.webp)



Aseta tämä Micro SD tietokoneeseen. Napsauta Sparrow Wallet:ssa "*Import File...*"-painiketta "*Coldcard Multisig*" vieressä ja valitse sitten Coldcard-kortilla kortilla luotu tiedosto.



![Image](assets/fr/13.webp)



Xpub on onnistuneesti tuotu. Toistamme nyt menettelyn kahdella muulla laitteistolompakolla.



![Image](assets/fr/14.webp)



Ledger Flexin osalta valitsen "*Keystore 2*" ja napsautan sitten "*Connected Hardware Wallet*". Varmista, että Ledger on kytketty tietokoneeseen, lukitus on avattu ja että Bitcoin-sovellus on auki.



![Image](assets/fr/15.webp)



Napsauta sitten "*Scan...*"-painiketta.



![Image](assets/fr/16.webp)



Klikkaa laitteistosalkun nimen vieressä "*Import Keystore*".



![Image](assets/fr/17.webp)



Toinen allekirjoittaja on nyt rekisteröity oikein Sparrow Wallet:ään.



![Image](assets/fr/18.webp)



Toistan täsmälleen saman menettelyn Trezor One -laitteen kanssa viimeistelläkseni Multisig-konfiguraation.



![Image](assets/fr/19.webp)



Kokoonpanossani emme käsittele tätä tapausta, mutta jos haluat sisällyttää allekirjoituksen Software Wallet:n kautta Sparrow'ssa (Hot Wallet) Multisig:een, napsauta yksinkertaisesti "*Uusi tai tuotu Software Wallet*" -painiketta.



Nyt kun kaikki allekirjoituslaitteesi on tuotu Sparrow Wallet:een, voit viimeistellä Multisig:n luomisen napsauttamalla "*Apply*".



![Image](assets/fr/20.webp)



Valitse vahva salasana, jolla varmistat pääsyn Sparrow Wallet Wallet -laitteeseen. Tämä salasana suojaa julkisia avaimia, osoitteita, tarroja ja tapahtumahistoriaa luvattomalta käytöltä.



Muista tallentaa salasana turvalliseen paikkaan, esimerkiksi salasanahallintaan, jotta se ei katoa.



![Image](assets/fr/21.webp)



## Multisig-salkun varmuuskopiointi



Tallennamme nyt *Output Script Descriptor* -komentosarjan Coldcard-kortille (tämä koskee vain käyttäjiä, joilla on Coldcard Multisig:ssä), ja ennen kaikkea pidämme siitä varmuuskopion riippumattomalla tietovälineellä.



*Descriptor* sisältää kaikki Multisig-portfoliosi xpubit sekä avainten generate-alkuisiin johdannaispolut. Muista, mitä näimme osassa 1: Multisig-salkun palauttamiseksi sinulla on oltava joko **kaikki** Mnemonic-lausekkeet tai vain vähimmäismäärä, joka tarvitaan allekirjoituksen kynnysarvon saavuttamiseen. Jälkimmäisessä tapauksessa on kuitenkin välttämätöntä saada myös **puuttuvien allekirjoittajien xpubs**. *Descriptor* sisältää kaikki Multisig:n xpubit.



Jos tämä ei ole selvää, muista vain tämä: Multisig:n hakemiseen tarvitaan vähimmäismäärä Mnemonic-lauseita kutakin käytettyä Hardware Wallet:tä kohti, riippuen kynnysarvosta (minun tapauksessani: 2 lausetta), sekä *Descriptor*.



Tämä *Descriptor* ei sisällä yksityisiä avaimia, vain julkisia. Tämä tarkoittaa, että se ei anna pääsyä varoihin. Se ei siis ole yhtä kriittinen kuin Mnemonic-lauseet, jotka antavat täyden pääsyn bitcoineihisi. *Descriptor*:n riski liittyy ainoastaan luottamuksellisuuteen: vaarantuessaan kolmas osapuoli voisi nähdä kaikki tapahtumasi, mutta ei voisi käyttää varojasi.



Suosittelen vahvasti, että luot useita kopioita tästä *Descriptorista* ja säilytät niitä Multisig:n jokaisessa allekirjoittavassa laitteessa. Esimerkiksi omassa tapauksessani tulostan *Descriptorin* paperille ja säilytän yhden kopion Coldcardin, toisen Trezorin ja yhden Ledger:n kanssa. Tallennan tämän *Descriptor*:n myös PDF-tiedostona kolmelle USB-tikulle, joita kutakin säilytetään yhdessä laitteistosalkussa. Näin maksimoin mahdollisuuteni, etten koskaan hukkaa *Descriptor*:ia, ja olen varma, että minulla on kaksi kopiota (yksi fyysinen ja yksi digitaalinen) jokaisessa laitteessa.



Kun Multisig-salkkusi on luotu, Sparrow antaa sinulle automaattisesti tämän *Descriptorin*. Klikkaa "*Save PDF...*"-painiketta tallentaaksesi sen sekä tekstinä että QR-koodina.



![Image](assets/fr/22.webp)



Voit sitten tulostaa tämän PDF-tiedoston ja kopioida sen USB-tikkuun.



![Image](assets/fr/23.webp)



Rekisteröimme tämän *Descriptorin* myös Coldcardiin (jos käytät sellaista kokoonpanossasi). Tämän avulla Coldcard voi tarkistaa, että jokainen myöhemmin allekirjoitettu tapahtuma vastaa alkuperäistä Wallet:ää: oikeat xpubs, oikea Address-muoto, oikea johdannaispolku.... Ilman tätä tuotua *Descriptoria* Coldcard ei voi vahvistaa, että Exchange-osoitteita ei ole kaapattu tai että PSBT:tä ei ole peukaloitu.



Tämä tekee Coldcardista niin mielenkiintoisen Multisig:ssa: se tarjoaa lisätarkistuksia tiettyjä kehittyneitä hyökkäyksiä vastaan, joita muut laitteistolompakot eivät salli (edellyttäen tietysti, että käytät sitä allekirjoittamiseen).



Siirry Sparrow'ssa "*Asetukset*"-valikkoon ja napsauta sitten "*Vie...*".



![Image](assets/fr/24.webp)



Napsauta "*Coldcard Multisig*" -vaihtoehdon vieressä "*Export File...*" ja tallenna tekstitiedosto Micro SD-kortille.



![Image](assets/fr/25.webp)



Aseta sitten kortti Coldcardiin. Mene "*Settings*"-valikkoon, sitten "*Multisig Wallets*" ja valitse "*Import from SD*".



![Image](assets/fr/26.webp)



Valitse sopiva tiedosto ja vahvista tuonti.



![Image](assets/fr/27.webp)



Napsauta juuri tuodun Multisig:n nimeä.



![Image](assets/fr/28.webp)



Tarkista Multisig:n konfigurointiparametrit ja vahvista rekisteröinti.



![Image](assets/fr/29.webp)



Multisig on nyt tallennettu oikein Coldcardiin. Jos sinulla on useita Coldcard-kortteja samassa Multisig:ssä, toista tämä toimenpide jokaisen kortin kohdalla.



*Descriptor*:n tallentamisen lisäksi älä unohda kiinnittää erityistä huomiota Mnemonic-lausekkeiden tallentamiseen kutakin allekirjoituslaitettasi varten. Jos olet vasta aloittamassa, suosittelen lämpimästi tutustumaan tähän toiseen opetusohjelmaan, jotta opit, miten niitä tallennetaan ja hallitaan oikein:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ennen kuin saat ensimmäiset bitcoinit Multisig:lläsi, **suositan sinua tekemään tyhjän palautustestin**. Merkitse muistiin joitakin viitetietoja, kuten ensimmäinen vastaanottava Address, ja nollaa sitten laitteistosi lompakot, kun Wallet on vielä tyhjä. Kokeile seuraavaksi palauttaa Multisig Wallet laitteistokukkaroihin käyttämällä Mnemonic-lauseen paperitallennuksia ja sitten Sparrow'ssa *Descriptor*:n avulla. Tarkista, että palautuksen jälkeen luotu ensimmäinen Address vastaa alun perin kirjoittamaasi. Jos se täsmää, voit olla varma, että paperiset varmuuskopiot ovat luotettavia.



Jos haluat lisätietoja palautustestin suorittamisesta, suosittelen, että tutustut tähän toiseen opetusohjelmaan:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Vastaanota bitcoineja Multisig:lla



Wallet on nyt valmis vastaanottamaan bitcoineja. Napsauta Sparrow'ssa välilehteä "*Vastaanottaa*".



![Image](assets/fr/30.webp)



Ennen kuin käytät Sparrow Wallet:n tuottamaa Address:tä, ota aikaa tarkistaa se suoraan laitteiston lompakoiden näytöltä. Näin varmistat, että Address:tä ei ole muutettu ja että laitteissasi on yksityiset avaimet, joita tarvitaan siihen liittyvien varojen käyttämiseen. Tämä auttaa suojautumaan useilta hyökkäysvektoreilta.



Napsauta tätä varten "*Näytä Address*" näyttääksesi Address:n Trezorissa tai Ledger:ssa, kun se on kytketty kaapelilla.



![Image](assets/fr/31.webp)



Coldcardin avulla tämä todentaminen voidaan suorittaa ilman minkäänlaista vuorovaikutusta Sparrow'n kanssa. Avaa vain "*Address Explorer*"-valikko ja valitse sitten Multisig aivan alareunasta.



![Image](assets/fr/32.webp)



Tämän jälkeen näet Multisig:n luomat vastaanotto-osoitteet.



![Image](assets/fr/33.webp)



Tarkista, että kussakin Hardware Wallet:ssa näkyvä Address vastaa täsmälleen Sparrow Wallet:ssä olevaa Address:a. Tämä on suositeltavaa tehdä juuri ennen Address:n jakamista maksajan kanssa, jotta voidaan olla varmoja sen eheydestä.



Tämän jälkeen voit määrittää Address:lle "*Label*", jolla osoitat vastaanotettujen bitcoinien alkuperän. Tämä on hyvä tapa organisoida UTXO:iden hallinta.



![Image](assets/fr/34.webp)



Kun tämä on vahvistettu, voit käyttää Address:ta bitcoinien vastaanottamiseen.



![Image](assets/fr/35.webp)



## Bitcoinien lähettäminen Multisig:lläsi



Nyt kun olet saanut ensimmäiset Satssit Multisig Wallet -laitteellasi, voit myös käyttää ne! Mene Sparrow'ssa "*lähettää*"-välilehdelle luodaksesi uuden tapahtuman.



![Image](assets/fr/36.webp)



Jos haluat käyttää *Coin Control*:a eli valita manuaalisesti UTXO:t, jotka haluat käyttää, siirry välilehdelle "*UTXO:t*". Valitse UTXO:t, jotka haluat käyttää, ja napsauta sitten "*Send Selected*". Sinut ohjataan automaattisesti välilehdelle "*Lähettää*", jossa UTXO:t on jo valmiiksi täytetty.



![Image](assets/fr/37.webp)



Syötä määränpää Address. Useita osoitteita voidaan lisätä napsauttamalla "*+ Lisää*".



![Image](assets/fr/38.webp)



Lisää "*Label*" kuvaamaan tämän kulun tarkoitusta, jotta tapahtumia on helpompi seurata.



![Image](assets/fr/39.webp)



Syötä valitulle Address:lle lähetettävä summa.



![Image](assets/fr/40.webp)



Säädä latausnopeus nykyisten verkko-olosuhteiden mukaan. Katso esimerkiksi [Mempool.space] (https://Mempool.space/) sopivan lataustason valitsemiseksi.



Kun olet tarkistanut kaikki tapahtumaparametrit, napsauta "*Create Transaction*".



![Image](assets/fr/41.webp)



Jos olet tyytyväinen kaikkeen, napsauta "*Viimeistele tapahtuma allekirjoittamista varten*".



![Image](assets/fr/42.webp)



Näytön alareunassa näet, että Sparrow odottaa kahta allekirjoitusta. Tämä on normaalia: tässä käytetty Wallet on Multisig 2-de-3.



![Image](assets/fr/43.webp)



Aloitan allekirjoittamisen Coldcardilla. Tätä varten asetan Micro SD-kortin tietokoneeseen ja napsautan sitten "*Tallenna tapahtuma*".



![Image](assets/fr/44.webp)



Voit lähettää allekirjoitettavan tapahtuman Hardware Wallet:een kolmella eri tavalla ja hakea sen sitten Sparrow'sta. Ensimmäinen on käyttää Micro SD-korttia, kuten tässä Coldcardin tapauksessa. Toinen on kaapeliyhteys, jota käytämme toisen allekirjoituksen yhteydessä (Ledger ja Trezor). Lopuksi on mahdollista käyttää QR-koodin välittämistä kameralla varustetuissa laitteissa, kuten Coldcard Q, Jade Plus tai Passport V2.



Kun PSBT (*Partially Signed Bitcoin Transaction*) on tallennettu Micro SD -muistitikulle, asetan sen Coldcard MK3 -korttiin ja valitsen "*Ready to Sign*" -valikon.



![Image](assets/fr/45.webp)



Tarkista Hardware Wallet-näytöltä huolellisesti tapahtuman parametrit: vastaanottajan Address, lähetetty summa ja maksut. Kun maksutapahtuma on vahvistettu, vahvista ja siirry allekirjoitukseen.



![Image](assets/fr/46.webp)



Palauta sitten Micro SD -kortti tietokoneeseen ja napsauta Sparrow'ssa "*Load Transaction*". Valitse tiedostoistasi Coldcardin allekirjoittama PSBT.



![Image](assets/fr/47.webp)



Näet, että Coldcardin allekirjoitus on lisätty. Käytän nyt toista laitetta, tässä tapauksessa Ledger:ta, suorittamaan toisen vaaditun allekirjoituksen. Yhdistän sen, avaan lukituksen ja napsautan sitten Sparrow'ssa "*Sign*".



![Image](assets/fr/48.webp)



Napsauta Hardware Wallet:n nimen vieressä olevaa "*Sign*"-painiketta.



![Image](assets/fr/49.webp)



Kun käytät Ledger:tä ensimmäistä kertaa tämän Multisig:n kanssa, Sparrow pyytää sinua vahvistamaan allekirjoittajien laajennetut julkiset avaimet (xpubs). Kuten Coldcardin kohdalla, tämä vaihe estää sinua allekirjoittamasta sokeasti myöhemmin. Varmistaaksesi nämä tiedot vertaa Ledger:n näytöllä näkyviä xpubeja suoraan muiden laitteistojen lompakoiden antamiin xpubeihin.



![Image](assets/fr/50.webp)



Tarkista vastaanottajan Address, siirretty summa ja transaktiomaksu ja allekirjoita transaktio.



![Image](assets/fr/51.webp)



Allekirjoita painamalla näyttöä.



![Image](assets/fr/52.webp)



Sparrow'lla on nyt kaksi allekirjoitusta, jotka tarvitaan varojen vapauttamiseksi Multisig-salkusta. Tarkista tapahtuma vielä kerran, ja jos kaikki sujuu hyvin, klikkaa "*Broadcast Transaction*" lähettääksesi sen verkon kautta.



![Image](assets/fr/53.webp)



Löydät tämän tapahtuman Sparrow Wallet:n "*Transaktiot*"-välilehdeltä.



![Image](assets/fr/54.webp)



Onneksi olkoon, tiedät nyt, miten moniääninen Wallet voidaan asentaa ja käyttää Sparrow'ssa. Jos pidit tätä ohjetta hyödyllisenä, olisin kiitollinen, jos jättäisit Green-peukalon alle. Voit vapaasti jakaa tätä artikkelia sosiaalisissa verkostoissa. Kiitos jakamisesta!



Jos haluat mennä pidemmälle, suosittelen, että tutustut tähän oppaaseen, jossa käsitellään toista menetelmää Bitcoin Wallet:n turvallisuuden lisäämiseksi, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7