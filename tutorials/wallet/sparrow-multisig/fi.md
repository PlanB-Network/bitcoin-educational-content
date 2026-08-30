---
name: Sparrow Wallet - Multisig
description: Luo usean allekirjoituksen lompakko Sparrow'ssa
---
![cover](assets/cover.webp)


Usean allekirjoituksen lompakko (josta käytetään usein nimitystä "*Multisig*") on Bitcoin-lompakon rakenne, joka vaatii useita kryptografisia allekirjoituksia eri avaimilta varojen käytön valtuuttamiseksi. Toisin kuin tavallisessa ("*singlesig*") lompakossa, jossa yksi yksityinen avain riittää UTXO:n lukituksen avaamiseen, Multisig perustuu **m-of-n**-malliin: lompakkoon liitetyistä _n_ avaimesta _m_ avaimen on ehdottomasti allekirjoitettava jokainen transaktio.


Tämän mekanismin avulla lompakon hallinta voidaan jakaa useiden osapuolten tai laitteiden kesken. Esimerkiksi 2-of-3-kokoonpanossa luodaan kolme itsenäistä avainjoukkoa, mutta varojen vapauttamiseen tarvitaan vain kaksi. Tämä arkkitehtuuri pienentää huomattavasti avaimen vaarantumiseen tai katoamiseen liittyviä riskejä: varas, jolla on pääsy vain yhteen avaimeen, ei voi tyhjentää lompakkoa, ja käyttäjä, joka menettää yhden avaimen, pääsee edelleen varoihinsa kahdella jäljellä olevalla.


![Image](assets/fr/01.webp)


Tämä parempi turvallisuus tuo kuitenkin mukanaan enemmän monimutkaisuutta. Multisig-lompakon pystyttäminen edellyttää useiden muistilauseiden (yksi kutakin allekirjoitustekijää kohti) ja laajennettujen julkisten avainten ("*xpub*") turvaamista. Jos käytät 2-of-3-Multisig-lompakkoa, sen palauttamiseen tarvitset joko kaikki kolme muistilausetta tai vähintään kaksi kolmesta lauseesta. Mutta jos sinulla on vain kaksi kolmesta lauseesta, tarvitset lisäksi pääsyn kaikkiin kolmeen *xpub*-avaimeen, joita ilman on mahdotonta palauttaa julkiset avaimet, joita tarvitaan niiden suojaamiin bitcoineihin pääsemiseksi.


Yhteenvetona: Multisig-lompakon palauttamiseksi sinulla on oltava:


- Joko pääsy kaikkiin kunkin allekirjoitustekijän muistilauseisiin;
- Tai kynnyksen edellyttämä vähimmäismäärä muistilauseita allekirjoittamista varten, sekä pääsy kaikkien tekijöiden xpub-avaimiin tarvittavien julkisten avainten palauttamiseksi.


![Image](assets/fr/02.webp)


Multisig-lompakon varmuuskopioiden hallintaa helpottavat *Output Script Descriptor* -kuvaajat, jotka kokoavat yhteen kaikki varoihin pääsyyn tarvittavat julkiset tiedot. Tätä toiminnallisuutta ei kuitenkaan ole vielä toteutettu kaikissa lompakonhallintaohjelmistoissa.


Multisig sopii erityisen hyvin bitcoinereille, jotka etsivät parempaa turvallisuutta tai varojen yhteishallintaa: yrityksille, yhdistyksille, perheille tai yksittäisille käyttäjille, joilla on merkittävä määrä bitcoineja. Sen avulla voi rakentaa hajautettuja hallintomalleja, esimerkiksi jakaa allekirjoitusvaltaa useiden johtajien tai tiimin jäsenten kesken.


Tässä oppaassa opettelemme luomaan ja käyttämään klassista usean allekirjoituksen lompakkoa **Sparrow Walletilla**. Jos haluat luoda räätälöidyn usean allekirjoituksen lompakon aikalukoilla, suosittelen sen sijaan Lianaa:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Edellytykset


Tässä oppaassa näytän sinulle, miten teet Multisigin [Sparrow Wallet -lompakonhallintaohjelmistolla](https://sparrowwallet.com/download/). Jos et ole vielä asentanut tätä ohjelmistoa, tee se nyt. Jos tarvitset apua, meillä on myös yksityiskohtainen opas Sparrow Walletin määrittämiseen:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Usean allekirjoituksen lompakon pystyttämiseen tarvitset useita eri laitteistolompakoita. Esimerkiksi 2-of-3-Multisigiin voisit käyttää:


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Image](assets/fr/03.webp)


Multisig-kokoonpanossa on hyvä käyttää eri valmistajien laitteistolompakoita. Näin varmistat, että jos jossakin tietyssä mallissa ilmenee vakava ongelma, se ei vaaranna Multisigisi kokonaisturvallisuutta. Lisäksi näin hyödyt kunkin laitteen omista vahvuuksista. Esimerkiksi minun kokoonpanossani:



- Trezor Model One on täysin avoimen lähdekoodin laite, mikä tekee seedin luonnin todentamisen mahdolliseksi. Koska siinä ei kuitenkaan ole Secure Element -sirua, se on edelleen altis fyysisille hyökkäyksille;



- Ledger Flexissä on puolestaan suljettu, ei-todennettavissa oleva laiteohjelmisto, mutta siihen on integroitu Secure Element, joka tarjoaa erinomaisen fyysisen suojan;



- Passport Core yhdistää täysin avoimen lähdekoodin laiteohjelmiston, Secure Element -sirun ja Air-Gap-tilassa tapahtuvan QR-koodinvaihdon. Se on itsenäinen kolmas allekirjoittaja, joka voi varmistaa osoitteita ja allekirjoittaa PSBT:itä ilman USB-datayhteyttä.


Ennen kuin määrität Multisig-lompakkosi, varmista, että jokainen laitteistolompakko on oikein konfiguroitu (muistilauseen luonti ja tallennus, PIN-koodin määritys). Yksityiskohtaiset ohjeet löydät kutakin laitteistolompakkoa koskevista oppaistamme, esimerkiksi:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Kuten näemme myöhemmin tässä oppaassa, Multisig-kokoonpanoosi on myös mahdollista sisällyttää tekijä, jota ei ole liitetty laitteistolompakkoon vaan jonka yksityiset avaimet on tallennettu tietokoneellesi. Tämä menetelmä on tietenkin vähemmän turvallinen kuin pelkkien laitteistolompakoiden käyttö, mutta se voi olla perusteltua joissakin tapauksissa. Esimerkiksi 2-of-3-Multisigissa voisit valita kaksi laitteistolompakkoa ja yhden ohjelmistolompakon.

> ⚠️ **Coldcard MK3 -turvallisuusilmoitus:** älä luo uutta seediä MK3:lla, jossa on vanhempi laiteohjelmisto kuin 4.2.0. Vanhemmalla laiteohjelmistolla luodut seedit on vaihdettava ja varat siirrettävä. Siksi tässä oppaassa käytetään Air-Gap-viiteallekirjoittajana Passport Corea.


## Multisig-lompakon luominen


Avaa Sparrow Wallet, napsauta välilehteä "*File*" ja valitse sitten "*New Wallet*".


![Image](assets/fr/04.webp)


Anna usean allekirjoituksen lompakollesi nimi ja vahvista napsauttamalla "*Create Wallet*".


![Image](assets/fr/05.webp)


Valitse pudotusvalikosta "*Policy Type*" vaihtoehto "*Multi Signature*".


![Image](assets/fr/06.webp)


Oikeassa yläkulmassa voit nyt määrittää Multisigisi avainten kokonaismäärän sekä sen, montako yhteisallekirjoittajaa varojen käytön valtuuttamiseen tarvitaan. Esimerkissäni kyseessä on 2-of-3-malli.


![Image](assets/fr/07.webp)


Ikkunan alaosassa Sparrow Wallet näyttää kolme "*Keystore*"-kohtaa. Kukin niistä edustaa yhtä avainjoukkoa. Käytän tässä kolmea laitteistolompakkoa, joten kukin "*Keystore*" vastaa yhtä niistä. Määritämme ne nyt.


Aloitan Passport Coresta. Valitsen välilehdessä "*Keystore 1*" vaihtoehdon "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Avaa Passportissa tili, jota haluat käyttää, ja valitse sitten "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport näyttää animoidun QR-koodin, joka sisältää sen julkisen avaimen tiedot.

Valitse Sparrow'ssa "*Scan...*" kohdan "*Passport*" vierestä ja lue tuo animoitu QR-koodi tietokoneesi web-kameralla. Vertaa Sparrow'n näyttämää pääavaimen sormenjälkeä Passportin näyttämään sormenjälkeen ja tuo sitten keystore.

Passportin xpub on nyt tuotu. Toista vastaava menettely Ledger Flexille ja Trezor Model Onelle.


Ledger Flexin osalta valitsen "*Keystore 2*" ja napsautan sitten "*Connected Hardware Wallet*". Varmista, että Ledger on liitetty tietokoneeseen, sen lukitus on avattu ja Bitcoin-sovellus on auki.


![Image](assets/fr/15.webp)


Napsauta sitten painiketta "*Scan...*".


![Image](assets/fr/16.webp)


Napsauta laitteistolompakkosi nimen vierestä "*Import Keystore*".


![Image](assets/fr/17.webp)


Toinen allekirjoittaja on nyt rekisteröity oikein Sparrow Walletiin.


![Image](assets/fr/18.webp)


Toistan täsmälleen saman menettelyn Trezor Onella viimeistelläkseni Multisig-kokoonpanon.


![Image](assets/fr/19.webp)


Omassa kokoonpanossani en käsittele tätä tapausta, mutta jos haluat sisällyttää Multisigiisi Sparrow'n ohjelmistolompakolla (kuumalompakolla) tehtävän allekirjoituksen, napsauta vain painiketta "*New or Imported Software Wallet*".


Nyt kun kaikki allekirjoituslaitteesi on tuotu Sparrow Walletiin, voit viimeistellä Multisigin luomisen napsauttamalla "*Apply*".


![Image](assets/fr/20.webp)


Valitse vahva salasana suojaamaan pääsyä Sparrow Wallet -lompakkoosi. Tämä salasana suojaa julkiset avaimesi, osoitteesi, merkintäsi ja tapahtumahistoriasi luvattomalta käytöltä.


Muista tallentaa tämä salasana turvalliseen paikkaan, esimerkiksi salasanahallintaan, jotta et menetä sitä.


![Image](assets/fr/21.webp)


## Multisig-lompakon varmuuskopiointi


Tallennamme nyt *Output Script Descriptor* -kuvaajan erilliselle tietovälineelle ja säilytämme siitä useita kopioita.


*Descriptor* sisältää kaikki Multisig-lompakkosi xpub-avaimet sekä avainten luontiin käytetyt johdannaispolut. Muista, mitä näimme osassa 1: Multisig-lompakon palauttamiseksi sinulla on oltava joko **kaikki** muistilauseet tai vain allekirjoituskynnyksen saavuttamiseen vaadittava vähimmäismäärä. Jälkimmäisessä tapauksessa on kuitenkin välttämätöntä, että sinulla on myös puuttuvien allekirjoittajien **xpub-avaimet**. *Descriptor* sisältää kaikki Multisigisi xpub-avaimet.


Jos tämä ei ole selvää, muista vain tämä: Multisigin palauttamiseen tarvitset kynnyksen mukaisen vähimmäismäärän muistilauseita kullekin käytetylle laitteistolompakolle (minun tapauksessani: 2 lausetta) sekä *Descriptor*-kuvaajan.


Tämä *Descriptor* ei sisällä yksityisiä avaimia, vain julkisia. Se ei siis anna pääsyä varoihin. Se ei siksi ole yhtä kriittinen kuin muistilauseet, jotka antavat täyden pääsyn bitcoineihisi. *Descriptor*-kuvaajaan liittyvä riski koskee ainoastaan luottamuksellisuutta: jos se vaarantuu, kolmas osapuoli voisi tarkkailla kaikkia tapahtumiasi, mutta ei voisi käyttää varojasi.


Suosittelen vahvasti, että teet tästä *Descriptor*-kuvaajasta useita kopioita ja säilytät niitä Multisigisi jokaisen allekirjoituslaitteen yhteydessä. Esimerkiksi minä tulostan *Descriptor*-kuvaajan paperille ja säilytän yhden kopion Passportin, toisen Trezorin ja yhden Ledgerin kanssa. Tallennan tämän *Descriptor*-kuvaajan myös PDF-tiedostona kolmelle USB-muistitikulle, joista jokainen säilytetään yhden laitteistolompakon kanssa. Näin maksimoin mahdollisuuteni olla koskaan menettämättä tätä *Descriptor*-kuvaajaa, ja voin olla varma, että jokaisen laitteen kanssa on kaksi kopiota (yksi fyysinen ja yksi digitaalinen).


Kun Multisig-lompakkosi on luotu, Sparrow antaa tämän *Descriptor*-kuvaajan automaattisesti. Napsauta painiketta "*Save PDF...*" tallentaaksesi sen sekä tekstinä että QR-koodina.


![Image](assets/fr/22.webp)


Voit sitten tulostaa tämän PDF-tiedoston ja kopioida sen USB-muistitikuillesi.


![Image](assets/fr/23.webp)


Passport käyttää Sparrow'n tuomaa multisig-kokoonpanoa näyttääkseen ja varmistaakseen olennaiset avaintiedot QR-parituksen ja allekirjoituksen aikana. Säilytä *Descriptor* erikseen: se on edelleen välttämätön lompakon palauttamiseksi, jos yksi allekirjoittaja ei ole käytettävissä.


*Descriptor*-kuvaajan tallentamisen lisäksi muista kiinnittää erityistä huomiota kunkin allekirjoituslaitteen muistilauseen tallentamiseen. Jos olet vasta aloittelija, suosittelen lämpimästi tutustumaan tähän toiseen oppaaseen, jossa opit tallentamaan ja hallitsemaan niitä oikein:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ennen kuin vastaanotat ensimmäiset bitcoinisi Multisigiisi, **suosittelen vahvasti tekemään tyhjän palautustestin**. Merkitse muistiin joitakin viitetietoja, kuten ensimmäinen vastaanotto-osoite, ja palauta sitten laitteistolompakkosi tehdasasetuksiin lompakon ollessa vielä tyhjä. Yritä seuraavaksi palauttaa Multisig-lompakkosi laitteistolompakoihin muistilauseiden paperisista varmuuskopioista ja sen jälkeen Sparrow'hun *Descriptor*-kuvaajan avulla. Tarkista, että palautuksen jälkeen luotu ensimmäinen osoite vastaa sitä, jonka kirjasit alun perin muistiin. Jos se vastaa, voit olla rauhallisin mielin siitä, että paperiset varmuuskopiosi ovat luotettavia.


Jos haluat oppia lisää palautustestin tekemisestä, suosittelen tutustumaan tähän toiseen oppaaseen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoinien vastaanottaminen Multisigiin


Lompakkosi on nyt valmis vastaanottamaan bitcoineja. Napsauta Sparrow'ssa välilehteä "*Receive*".


![Image](assets/fr/30.webp)


Ennen kuin käytät Sparrow Walletin luomaa osoitetta, tarkista se rauhassa suoraan laitteistolompakoidesi näytöltä. Näin varmistat, ettei osoitetta ole muutettu ja että laitteesi hallitsevat yksityisiä avaimia, joita tarvitaan siihen liittyvien varojen käyttämiseen. Tämä auttaa suojaamaan sinua useilta hyökkäysvektoreilta.


Napsauta tätä varten "*Display Address*" näyttääksesi osoitteen Trezorissa tai Ledgerissä, kun se on liitetty kaapelilla.


![Image](assets/fr/31.webp)


Passportissa valitse multisig-tili ja valitse "*Verify Address*". Lue Sparrow'n näyttämän vastaanotto-osoitteen QR-koodi. Passport vahvistaa näytöllään, kuuluuko osoite multisig-lompakkoon.


Tarkista, että jokaisen laitteistolompakon näyttämä osoite vastaa täsmälleen Sparrow Walletissa olevaa osoitetta. Tämä on hyvä tehdä juuri ennen osoitteen jakamista maksajalle, jotta olet varma sen eheydestä.


Voit sitten antaa tälle osoitteelle "*Label*"-merkinnän, joka kertoo vastaanotettujen bitcoinien alkuperän. Tämä on hyvä tapa järjestää UTXO:idesi hallintaa.


![Image](assets/fr/34.webp)


Kun tämä on tarkistettu, voit käyttää osoitetta bitcoinien vastaanottamiseen.


![Image](assets/fr/35.webp)


## Bitcoinien lähettäminen Multisigilla


Nyt kun olet vastaanottanut ensimmäiset satsit Multisig-lompakkoosi, voit myös käyttää niitä! Siirry Sparrow'ssa välilehteen "*Send*" rakentaaksesi uuden transaktion.


![Image](assets/fr/36.webp)


Jos haluat käyttää *Coin Control* -toimintoa eli valita käytettävät UTXO:t käsin, siirry välilehteen "*UTXOs*". Valitse UTXO:t, jotka haluat käyttää, ja napsauta sitten "*Send Selected*". Sinut ohjataan automaattisesti välilehteen "*Send*", jossa UTXO:t on jo täytetty valmiiksi.


![Image](assets/fr/37.webp)


Syötä kohdeosoite. Useita osoitteita voi lisätä napsauttamalla "*+ Add*".


![Image](assets/fr/38.webp)


Lisää "*Label*"-merkintä, joka kuvaa tämän rahansiirron tarkoitusta, jotta transaktioidesi seuraaminen on helpompaa.


![Image](assets/fr/39.webp)


Syötä valittuun osoitteeseen lähetettävä summa.


![Image](assets/fr/40.webp)


Säädä siirtomaksutasoa verkon senhetkisen tilanteen mukaan. Voit esimerkiksi tarkistaa sopivan maksutason osoitteesta [Mempool.space](https://Mempool.space/).


Kun olet tarkistanut kaikki transaktion parametrit, napsauta "*Create Transaction*".


![Image](assets/fr/41.webp)


Jos kaikki on kunnossa, napsauta "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Näytön alaosassa näet, että Sparrow odottaa 2 allekirjoitusta. Tämä on normaalia: tässä käytetty lompakko on 2-of-3-Multisig.


![Image](assets/fr/43.webp)


Aloitan allekirjoittamisen Passportilla. Napsauta Sparrow'ssa "*Show QR*" näyttääksesi PSBT:n (*Partially Signed Bitcoin Transaction*) animoituina QR-koodeina. Valitse Passportissa multisig-tili ja valitse "*Sign with QR Code*", ja lue sitten Sparrow'n näyttämä QR-koodi.


Tarkista laitteistolompakkosi näytöltä huolellisesti transaktion parametrit: vastaanottajan osoite, lähetetty summa ja siirtomaksut. Kun olet vahvistanut transaktion, hyväksy se siirtyäksesi allekirjoitukseen.


Kun olet hyväksynyt transaktion, Passport näyttää allekirjoitetun PSBT:n animoituina QR-koodeina. Napsauta Sparrow'ssa "*Scan QR*" ja lue nämä koodit web-kameralla. Passportin allekirjoitus lisätään tämän jälkeen. Käytän nyt Ledgeriä toiseen vaadittuun allekirjoitukseen: liitän sen ja avaan lukituksen, ja napsautan sitten Sparrow'ssa "*Sign*".


![Image](assets/fr/48.webp)


Napsauta "*Sign*" laitteistolompakkosi nimen vierestä.


![Image](assets/fr/49.webp)


Kun käytät Ledgeriä tässä Multisigissa ensimmäisen kerran, Sparrow pyytää sinua varmistamaan yhteisallekirjoittajien laajennetut julkiset avaimet (xpub). Kuten Passportin kohdalla, tämä vaihe estää sinua allekirjoittamasta myöhemmin sokkona. Vahvista nämä tiedot vertaamalla Ledgerin näytöllä näkyvää xpub-avainta niihin, jotka muut laitteistolompakkosi antavat suoraan.


![Image](assets/fr/50.webp)


Tarkista vastaanottajan osoite, siirretty summa ja transaktion siirtomaksu, ja allekirjoita sitten transaktio.


![Image](assets/fr/51.webp)


Paina näyttöä allekirjoittaaksesi.


![Image](assets/fr/52.webp)


Sparrow'lla on nyt kaksi allekirjoitusta, jotka tarvitaan varojen vapauttamiseen Multisig-lompakosta. Tarkista transaktio viimeisen kerran, ja jos kaikki on kunnossa, napsauta "*Broadcast Transaction*" lähettääksesi sen verkkoon.


![Image](assets/fr/53.webp)


Löydät tämän transaktion Sparrow Walletin välilehdestä "*Transactions*".


![Image](assets/fr/54.webp)


Onnittelut, osaat nyt pystyttää ja käyttää usean allekirjoituksen lompakkoa Sparrow'ssa. Jos tämä opas oli sinulle hyödyllinen, olisin kiitollinen, jos jättäisit alle vihreän peukun. Jaa artikkeli vapaasti sosiaalisessa mediassa. Kiitos jakamisesta!


Jos haluat mennä pidemmälle, suosittelen tutustumaan tähän oppaaseen, joka käsittelee toista tapaa parantaa Bitcoin-lompakkosi turvallisuutta, BIP39-salalausetta:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
