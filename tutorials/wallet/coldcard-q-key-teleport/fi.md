---
name: COLDCARD Q - Key Teleport
description: Mikä on Key Teleport ja miten sitä käytetään?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Mikä on **Key Teleport** -ominaisuus, jonka Coinkite tarjoaa lippulaivansa ColdCardQ-laitteen yhteydessä?



**Key Teleport**:n avulla voit siirtää luottamuksellisia tietoja turvallisesti 2 ColdCardQ:n välillä. Siirtokanavan ei tarvitse edes olla salattu, vaan se voi olla julkinen.



Tätä voidaan käyttää siirtämiseen:





- **gW-0-lauseet** (ColdCard Q:n seed-mestari tai ColdCardQ:n [seed Holviin](https://coldcard.com/docs/temporary-seeds/#seed-vault) tallennetut salaisuudet.
- **luottamukselliset muistiinpanot ja salasanat**: tämä voi olla mikä tahansa salaisuus tai koko ColdCardQ:n [Secure Notes & Passwords] -hakemisto (https://coldcard.com/docs/secure_notes/).
- **varmuuskopio koko ColdCardQ:sta**: varmuuskopion vastaanottavalla ColdCardQ:lla ei saa olla seed Masteria, jotta tämä toimisi.
- gW-3 (**osittain allekirjoitetut Bitcoin-transaktiot**) osana monialakirjoitusjärjestelmää.



Tämä edellyttää, että olet päivittänyt [laitteen laiteohjelmiston versioon v1.3.2Q](https://coldcard.com/docs/upgrade/) tai uudempaan.



## Miten käytän Key Teleportia?



### 1- Minkälaisten tietojen siirtäminen



Tässä tarkastelemme seed-lauseiden, muistiinpanojen, salasanojen tai koko ColdCardQ-varmuuskopion siirtoa. PSBT-siirtoja usean allekirjoituksen tapahtumia varten käsitellään myöhemmin.



#### Valmistele laite vastaanottamaan salaisuudet



Valitse ColdCardQ:n **"Advanced / Tools**"-valikosta **"Key Teleport (start) "**.


Seuraavassa näytössä ehdotetaan 8-numeroista salasanaa, tässä "20420219". Sinun on ilmoitettava tämä salasana lähettäjälle. Voit lähettää salasanan esimerkiksi tekstiviestillä, suosimallasi suojatulla viestijärjestelmällä tai jopa äänipuhelulla.



Siirry sitten seuraavaan vaiheeseen napsauttamalla ColdCardQ:n **"Enter**"-painiketta.




![CCQ-key-teleport](assets/fr/01.webp)




Näytölle luodaan QR-koodi. Jälleen kerran sinun on välitettävä tämä QR-koodi ColdCardQ:n "lähettäjälle". Helpoin tapa tehdä tämä on videopuhelu.



**ÄLÄ LÄHETÄ TÄTÄ QR-KOODIA SAMAA LÄHETYSKANAVAA PITKIN, JOTA KÄYTETTIIN EDELLISEN 8-NUMEROISEN SALASANAN LÄHETTÄMISEEN**.



![CCQ-key-teleport](assets/fr/02.webp)



*Niille, joita asia kiinnostaa, yritetään ymmärtää mekanismi, jonka avulla salaisuuksia voidaan siirtää suojaamattomien kanavien kautta*



*Mitä me itse asiassa teemme tässä, on salaisuuksien siirron aloittaminen Diffie-Hellman-menetelmällä, jota käsitellään BTC204-kurssilla, jonka olen sisällyttänyt alla olevaan*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Meillä on tällä hetkellä:*




- luodaan ephemeral-avainpari (julkinen/yksityinen Ka ja ka, Ka=G.ka, G on ECDH-generaattoripiste) ja 8-numeroinen salasana.
- käytti tätä salasanaa salatakseen julkisen avaimen (Ka) AES-256-CTR:llä ja lähetti sitten tämän salasanan viestintäkanavan A kautta "lähettävälle" **ColdCardQ:lle**
- lopuksi lähetimme salatun paketin lähettäjälle edellä mainitun QR-koodin kautta käyttäen toista viestintäkanavaa B, joka eroaa ensimmäisestä.



#### Valmistele laite, joka lähettää salaisuudet



Napsauta lähettävässä laitteessa **"QR "**-painiketta skannataksesi vastaanottavan laitteen lähettämän QR-koodin ja syötä sitten 8-numeroinen salasana, joka sinulle ilmoitettiin edellisessä vaiheessa erillisen kanavan kautta. Olemme nyt valmiita aloittamaan tietojen lähettämisen "lähettävästä" laitteesta.



**Älä kirjoita 8-numeroista salasanaa väärin, sillä virheilmoitusta ei näytetä ja prosessi jatkuu. Lopullinen tiedonsiirto kuitenkin epäonnistuu ja sinun on aloitettava alusta**.



![CCQ-key-teleport](assets/fr/03.webp)



*Uteliaimmille kerrotaan vielä kerran, mitä kryptografian ja salaisen tiedonsiirron alalla on meneillään:*




- tuomme salatut tiedot skannaamalla QR-koodin vastaanottavassa laitteessa.
- sitten purimme ne käyttämällä 8-numeroista salasanaa, joka lähetettiin meille toissijaisen kanavan kautta.
- meillä on siis hallussamme vastaanottajan alun perin luoma julkinen avain (Ka).
- Tämän jälkeen generate luo uuden ephemeral-avainparin (Kb/kb, jossa Kb=G.kb) lähettävään laitteeseen, jota käytetään ECDH:n soveltamiseen Ka:han. Suoritamme siis operaation kb.Ka=Ks , jossa Ks on nimeltään **"istuntoavain"**.




Sinua pyydetään nyt valitsemaan kahden ColdCardQ:n välillä siirrettävien salaisuuksien luonne (luottamukselliset muistiinpanot, salasana, täysi varmuuskopio, holvisi sisältämät siemenet, seed-laitteen master).



![CCQ-key-teleport](assets/fr/04.webp)



Tässä salaisuutemme on lyhyt viesti valitsemalla **"Pikatekstiviesti "**. Kirjoita viestisi (meille "PlanB Network rocks") ja paina sitten **"ENTER "**.


Tämän jälkeen laite luo uuden satunnaisen salasanan nimeltä **"Teleport Password "** , esimerkissä "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Paina **"ENTER "** ja sinulle näytetään uusi QR-koodi. Skannaa se vastaanottavalla laitteella. Ja lähetä eri viestintäkanavalla **"Teleportin salasana "** vastaanottajalle.



![CCQ-key-teleport](assets/fr/06.webp)



*Tässä taas uteliaille tiedoksi, että tässä vaiheessa:*




- kun siirrettävät salaisuudet on valittu, generate luo uuden satunnaisen salasanan nimeltä **"Teleport Password"**.
- salataan sitten salaisuudet AES-256-CTR:llä käyttäen edellisessä vaiheessa luotua **"istuntoavainta"**, "Ks".
- etuliitteenä pakettiin, joka on jo salattu **"Istuntoavaimella "**, lisätään julkinen avaimemme Kb ja sitten vielä Layer AES-256-CTR-salaus **"Teleportin salasanalla "**. Koko asia koodataan QR-koodiksi




#### Viimeistele salaisuuksien siirto vastaanottavalle laitteelle



Paina **"QR "**-painiketta skannataksesi lähettävän laitteen visio-kanavan kautta esittämän QR-koodin. Sinua pyydetään syöttämään **"Teleportin salasana "** meille "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Tämän jälkeen tiedot puretaan ja tehdään ymmärrettäviksi vastaanottavalle laitteelle. Vastaanotettu viesti on todellakin "PlanB Network rocks". Siinä kaikki.



![CCQ-key-teleport](assets/fr/08.webp)



*Mitä oikeastaan tapahtui tämän viimeisen vaiheen aikana :*?




- olemme purkaneet lähettäjän lähettämät tiedot käyttämällä **"Teleportin salasanaa"**.
- meillä on siis julkinen avain Kb ja salainen viestimme, joka on salattu **"istuntoavaimella "**, "Ks". Mutta miten voimme tehdä tämän, koska vastaanottajana emme tiedä Ks:ää, jonka lähettäjä on luonut?
- Meidän on sovellettava yksityistä avaintamme "ka" alkuvaiheesta **"Valmistele laite, joka vastaanottaa tiedot"** julkiseen avaimeen Kb.
- Itse asiassa laskemalla ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks saadaan Ks. Sitä käytetään lopulta salaisen viestin salaamiseen.



### 2- PSBT:n siirtäminen Multisig:ään (edistynyt)



Tämä edellyttää, että Wallet Multisig on jo luotu ja että ColdCardQ-laitteesi on jo esiasetettu siten, että se pystyy suorittamaan usean allekirjoituksen tapahtumia. Jos näin ei ole, selitykset ovat saatavilla [täällä](https://coldcard.com/docs/Multisig/) Coinkiten verkkosivustolla.



Nopea muistutus siitä, mikä on monikäyttöinen Wallet (Multisig).



Yleensä Wallet-varojesi käyttämiseen tarvitaan vain yksi yksityinen avain, jolla voit avata osoitteisiisi liittyvät UTXO:t.


Wallet Multisig:n tapauksessa varojen käyttämiseen voidaan tarvita jopa 15 yksityistä avainta ja siten 15 allekirjoitusta. Tämä tunnetaan nimellä "M out of N" -salkku, jossa N on välillä 1-15 ja M on varojen käyttämiseen tarvittavien allekirjoitusten määrä. Esimerkiksi Wallet Multisig 3:sta 5:stä edellyttää vähintään kolme allekirjoitusta viidestä mahdollisesta.



Haasteena on sitten koordinoida allekirjoittajien välinen koordinointi, jotta "PSBT" allekirjoittaisi vuorostaan "Partially Signed Bitcoin Transaction:n". Tässä yhteydessä voidaan käyttää **Key Teleport** -menetelmää PSBT:n välittämiseen allekirjoittajien välillä yksinkertaisella ja luottamuksellisella tavalla. Yksinkertainen videopuhelu allekirjoittajien välillä riittää.



Näin se tehdään Multisig 3 of 4 -mallissa.



**Allekirjoittaja 1:**



Allekirjoittaja 1 tuo PSBT:n maahan ja allekirjoittaa sen. Lopuksi hän napsauttaa **"T "** käyttääkseen **"Key Teleport "** siirtääkseen PSBT:n allekirjoittajalle 2.



![CCQ-key-teleport](assets/fr/09.webp)




Kun allekirjoittaja 2 on valittu napsauttamalla **"ENTER "**, annetaan "TELEPORTIN SALASANA" (tässä JJ YC AB 6A), joka on toimitettava allekirjoittajalle 2 toisen viestintäkanavan kautta. Esimerkiksi tekstiviestillä tai äänipuhelulla, mutta **ei** videopuhelulla.



Paina uudelleen **"ENTER "** ja näyttöön tulee QR-koodi, joka edustaa PSBT:ta, jonka on allekirjoittanut 1 ja joka on salattu "TELEPORT PASSWORD"-luvulla.



![CCQ-key-teleport](assets/fr/10.webp)



**Allekirjoittaja 2:**



Allekirjoittaja 2 skannaa allekirjoittajan 1 hänelle esittämän QR-koodin. Syöttää sitten toissijaisen viestintäkanavan kautta lähetetyn "TELEPORT PASSWORD" -luvun, jolla lähetetyt tiedot puretaan.



Allekirjoittaja 2 allekirjoittaa tapahtuman ja napsauttaa sitten **"T "** siirtääkseen PSBT:n allekirjoittajalle 3 "Key Teleportin" kautta.


On selvää, että 2 allekirjoitusta on jo käytetty. Enää puuttuu vain allekirjoittaja 3, jotta tapahtuma olisi pätevä. Valitse allekirjoittaja 3 klikkaamalla **"ENTER "**.



![CCQ-key-teleport](assets/fr/11.webp)



Sitten luodaan uusi "TELEPORTIN SALASANA", jota seuraa jälleen QR-koodi, joka koodaa PSBT:n, jonka ovat allekirjoittaneet 1 ja 2, ja joka on sitten salattu tällä uudella "TELEPORTIN SALASANALLA" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Allekirjoittaja 3:**



Toista sama vaihe kuin edellä.


Allekirjoittaja 3 skannaa allekirjoittajan 2 hänelle esittämän QR-koodin. Syöttää sitten toissijaisen viestintäkanavan välityksellä lähetetyn "TELEPORT PASSWORD" -lukusanan.



Allekirjoittaja 3 allekirjoittaa maksutapahtuman, ja koska tällä kertaa on käytetty kolmea neljästä allekirjoituksesta, maksutapahtuma merkitään viimeistellyksi ja se on valmis levitettäväksi eri välineillä (SD-kortti, NFC, QR jne.).



![CCQ-key-teleport](assets/fr/13.webp)



Jos ColdCardQ:n "Push Tx" -ominaisuus on aktivoitu, kiinnitä ColdCardQ minkä tahansa NFC-yhteydellä varustetun Internet-yhteydellä varustetun laitteen (älypuhelin/tabletti) takapuolelle ja lähetä tapahtuma Bitcoin-verkon kautta.



![CCQ-key-teleport](assets/fr/14.webp)



*PSBT:n siirroissa allekirjoittajalta toiselle käytetään yksinkertaisesti "Key Teleport" -menetelmää, jossa käytetään "Teleport Password" -salasanaa jokaisessa vaiheessa, jolloin PSBT salataan siirron aikana allekirjoittajalta toiselle. Koska siirrettyjä tietoja ei voida käyttää varojen varastamiseen, ei tarvita Diffie-Hellmania, kuten lähetettäessä erittäin luottamuksellisia salaisuuksia (seed, salasana jne...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Lähde: [ColdCardin virallinen verkkosivusto](https://coldcard.com/)*