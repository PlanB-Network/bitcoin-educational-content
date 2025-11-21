---
name: COLDCARD - Yhteiskirjoitus
description: Tutustu rinnakkaisallekirjoitusominaisuuteen ja käytä sitä COLDCARD-kortissasi
---

![cover](assets/cover.webp)


*HUOM: Tämä opetusohjelma on suunnattu henkilöille, joilla on jo jonkin verran kokemusta usean allekirjoituksen lompakoista, Coinkite-laitteista ja ohjelmistoista, kuten Sparrow wallet:sta tai Nunchukista.*



![video](https://youtu.be/MjMPDUWWegw)




**Miksi ColdCard Co-Sign?



Tämän ominaisuuden avulla voit lisätä ColdCard-laitteeseesi (Q tai Mk4) **kulutusehtoja** laitteiston turvamoduulin (HSM) tapaan, jotta voit suojata varojasi ja säilyttää samalla huomattavan joustavuuden ja hallinnan niiden suhteen.



Kulutusehtoja voivat olla esimerkiksi:





- Suuruusrajat**: rajoittaa bitcoinien määrän, jonka voit käyttää yhdessä transaktiossa.
- Nopeusrajoitukset:** Määritä, kuinka monta transaktiota voit suorittaa aikayksikössä (tunnissa, päivässä, viikossa jne.) ja kuinka monta lohkoa niiden välillä on oltava vähintään.
- Ennalta hyväksytyt osoitteet:** Salli bitcoinien lähettäminen vain ennalta hyväksyttyihin osoitteisiin.
- Kaksitekijätodennus:** Vaatii vahvistuksen kolmannen osapuolen 2FA-mobiilisovelluksesta (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) NFC-yhteydellä varustetulla älypuhelimella/tabletilla, jossa on internetyhteys.



**Miten se toimii



Lisäämällä ColdCard Mk4- tai Q-laitteeseen toinen seed, jota kutsutaan "Spending Policy Key" -avaimeksi ja johon viitataan tässä oppaassa nimellä "C Key".


Tämän ylimääräisen seed:n lisäksi sinua pyydetään Supply:een vähintään yksi ylimääräinen avain (XPUB), jota kutsumme "vara-avaimeksi", jotta voit luoda Wallet Multisig 2-on-N.



Lyhyesti sanottuna luomme Wallet Multisig:n, ja ColdCard-laitteesi sisältää kaksi varojen käyttämiseen tarvittavaa yksityistä avainta, laitteen seed-pääavaimen ja "Spending Policy Key" -avaimen.



Aina kun C-avainta pyydetään allekirjoittamaan, sovelletaan määriteltyjä käyttöehtoja, ja ColdCard allekirjoittaa vain, jos maksutapahtuma on niiden mukainen.



Jos haluat luopua näistä käyttöehdoista, voit tehdä niin:




- allekirjoittamalla yhdellä vara-avaimella ja seed-kädellä tai kahdella vara-avaimella Multisig:n koosta riippuen.
- syöttämällä "Spending Policy Key" tai "C Key" "Co-Sign" -valikossa. **Viimeistä ei voi käyttää suoraan laitteessa, koska muuten kuka tahansa voisi peruuttaa määritetyt kulutusehdot.**




## ColdCard Co-Signin määrittäminen



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktivoi toiminto



Varmista ensin, että laitteessasi on vähintään uusin laiteohjelmistoversio:




- Mk4: v5.4.2
- Q: v1.3.2Q




Valitse Mk4- tai ColdCardQ-järjestelmässäsi *Lisätyökalut > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*Seuraavassa ohjeessa kuvakaappaukset on otettu ColdCardQ:lla, mutta vaiheet ja valikot ovat samat Mk4:n ja Q:n välillä*



Näyttöön tulee yhteenveto toiminnoista.


Avainten nimeämiseen käytetty terminologia, jota käytämme jälleen 2-on-3 multi-signature Wallet:ssä, jonka olemme luomassa, on seuraava:



Näppäin A = Coldcard master seed


Näppäin B = vara-avain


Näppäin C = Menopoliittinen avain



Napsauta **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



Seuraavaksi on päätettävä, mikä yksityinen avain toimii "Kulutuskäytännön avaimena" tai "Avaimena C".



Näemme, että meillä on useita vaihtoehtoja:





- Tai paina **"ENTER "** luodaksesi generate uuden seed-lauseen, jossa on 12 sanaa.





- Napsauta joko **"(1) "**, jos haluat tuoda olemassa olevan 12 sanan seed:n, tai valitse **"(2) "**, jos haluat tuoda olemassa olevan 24 sanan seed:n.





- Tai paina **"(6) "** tuodaksesi seed laitteen holvista.



Tätä ohjetta varten päätimme tuoda olemassa olevan 12-sanaisen seed:n painamalla **"(1) "**. Tämä voi olla mikä tahansa seed BIP39, jonka jo omistat ja josta sinulla on luonnollisesti varmuuskopio.



Kirjoita seed:n 12 sanaa näppäimistöllä. Tässä esimerkissä valitsemme seed:n kelvollisen lauseen beef x 12. Paina sitten **"ENTER "**.


*HUOMAUTUS: jos sinulla ei ole varmuuskopiota tästä seed:stä, et voi enää muuttaa laitteesi "Co-Sign"-asetuksia muuttaaksesi käyttöehtojasi*



Laitteessa on nyt aktivoitu "Co-Sign"-ominaisuus. Seuraavaksi meidän on valittava menoehdot ja viimeisteltävä sitten usean allekirjoituksen Wallet:n luominen.



![Co-Sign](assets/fr/03.webp)



### 2- Valitse menoehdot tai "*menopolitiikka*"



Tässä määritetään kulutusta koskevat ehdot, joiden on täytyttävä, kun **"C-avain "** tai **"Kulutuskäytäntöavain**" allekirjoittaa tapahtuman.



Napsauta valikossa **"Yhteinen allekirjoitus "** kohtaa **"Kulutuskäytäntö**".



Tämän jälkeen voit valita enimmäissumman, eli kuinka monta satoshia voit käyttää yhdessä maksutapahtumassa.



Tässä esimerkissä valitsemme suurimmaksi magnitudiksi **21212** satoshi. Vahvista valinta napsauttamalla **"ENTER "**.




![Co-Sign](assets/fr/04.webp)



Tämän jälkeen asetetaan enimmäisnopeus eli transaktioiden määrä, jonka laite pystyy allekirjoittamaan aikayksikössä. Tässä opetusohjelmassa valitsemme rajoittamattoman nopeuden, eli transaktioiden lukumäärää ei ole rajoitettu.




![Co-Sign](assets/fr/05.webp)



### 3- Luo Wallet Multisig 2-on-N



Meidän on vielä valittava kolmas avain Wallet Multisig:lle, eli **"Backup Key "** (avain B), laitteen **master seed** (avain A) ja **"Spending Policy Key "** (avain C) lisäksi.



B-avaimemme on tuotava joko SD-kortin kautta tai QR-koodin kautta ColdCardQ:n tapauksessa.


Tätä varten tarvitsemme toisen ColdCard Mk4- tai Q-laitteen, jossa Key B -näppäintä käytetään.



Tässä toisessa laitteessa, joka sisältää **"Backup Key "**, esimerkiksi ColdCard Mk4 tässä esimerkissä, siirry päävalikosta kohtaan **"Asetukset "**, sitten **"Multisig Wallet"** ja lopuksi **"Export Xpub "**.


(Jos toinen laitteesi on ColdCardQ, voit tietysti viedä Xpubin QR-koodin avulla).





![Co-Sign](assets/fr/06.webp)





Aseta seuraavassa näytössä SD-kortti ja napsauta oikeassa alakulmassa olevaa **"validoi "**-painiketta. Klikkaa sitten **"(1) "** tallentaaksesi tiedoston SD-kortille.



Tiedoston nimessä on julkisen avaimen sormenjälki (*fingerprint*), ja sen muoto on `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Aseta sitten SD-kortti "alkuperäiseen" ColdCardQ:een ja tuo "varmuuskopioavain" (avain B).


Valitse "ColdCard Co-Signing" -valikosta "Build 2-of-N" ja napsauta seuraavassa näytössä **"ENTER "** ja sitten uudelleen **"ENTER "** tuodaksesi "Backup Key" SD-kortilta.



![Co-Sign](assets/fr/08.webp)



Jätä seuraavassa näytössä "Tilinumero" tyhjäksi (ellet tiedä tarkalleen, mitä olet tekemässä) ja napsauta uudelleen **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Vihdoinkin olemme valmiita käyttämään uutta Wallet Multisig 2-sur-3:a, joka koostuu seuraavasti:



Näppäin A= kylmäkortti Q master seed


Avain B= Vara-avain (juuri tuotu toisesta Coldcard-laitteesta)


Avain C= Kulutuskäytäntöjen avain (jos sitä käytetään allekirjoittamiseen, se asettaa ennalta määritellyt kulutusta koskevat ehdot)



## Allekirjoitus Sparrow wallet:n kanssa



Tutustu tarvittaessa alla oleviin ohjeisiin tutustuaksesi Sparrow wallet-ohjelmistoon:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Vienti Wallet Multisig 2-sur-3 Sparrow wallet:een



Meidän on nyt vietävä Wallet Multisig Sparrow:ään, jotta voimme sijoittaa sinne ensimmäiset satelliittimme.



Valitse ColdCardQ:n päävalikosta **"Asetukset "** ja sitten **"Multisig Lompakot "**.


Nyt näytetään ColdCard-korttisi tiedossa olevat Multisig-lompakot, ja näppäinten lukumäärä on "2/3" (2-sur3). Valitse juuri luomamme Multisig **"ColdCard Co-Sign "** ja napsauta sitten **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Valitse lopuksi menetelmä, jolla voit viedä Wallet:n Sparrow:een. Meidän tapauksessamme valitsemme SD-kortin, joten napsauta **"(1) "** sen jälkeen, kun olet asettanut SD-kortin laitteen korttipaikkaan A.



![Co-Sign](assets/fr/11.webp)



Valitse sitten Sparrow wallet:ssa "Tuo Wallet".



![Co-Sign](assets/fr/12.webp)



Napsauta sitten **"Tuo tiedosto "**. Valitse sitten tiedosto **"export-Coldcard_Co-sign.txt "** SD-kortillasi.



![Co-Sign](assets/fr/13.webp)



Anna Wallet:lle nimi, joka näkyy Sparrow:ssä, ja valitse salasana Wallet:n salausta varten (tai ei).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Olemme nyt valmiita vastaanottamaan ensimmäiset satoshiimme ja testaamaan Wallet:ään soveltamiamme käyttöehtoja.



![Co-Sign](assets/fr/16.webp)



### 2- Ennalta määritettyjen menopolitiikkojen testaaminen



Muistutuksena mainittakoon, että olimme päättäneet Wallet Multisig:n suurimmaksi magnitudiksi 21212 satoshia. Tämä tarkoitti sitä, että aina kun Kulutuspolitiikan avain (avain C) allekirjoitti tapahtuman, se oli voimassa vain, jos käytetty summa oli enintään 21212 satoshia.



Testataan sitä.


Napsautetaan ensin Sparrow:n "Receive"-välilehteä ja pudotetaan muutama Satss Wallet:een, jota käytämme koko tämän ohjeen ajan.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Yritetään sitten käyttää enemmän kuin 21212 sallittua satoshia simuloimalla 50 000 Sats-tapahtumaa.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Kun olemme skannanneet *allekirjoittamatonta* tapahtumaa edustavan QR-koodin ColdCardQ:lla tapahtuman tuomiseksi, näytöllä näkyy tämä. Varoitusviesti kertoo meille, että käyttöehtoja ei ole täytetty. Jos allekirjoitamme tapahtuman kuitenkin, vain toinen kahdesta avaimesta (laitteessa oleva seed master, mutta ei "Key C") allekirjoittaa.




![Co-Sign](assets/fr/23.webp)



Kun tapahtumamme on tuotu Sparrow:een, näemme, että vain yksi allekirjoituksista on sovellettu tapahtumaan.



![Co-Sign](assets/fr/24.webp)




Toistetaan nyt koe, mutta 21 000 satoshin transaktiolle, eli pienemmälle kuin Wallet:lle asettamamme maksimimagnitudi (21212 Sats).




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Yritetään allekirjoittaa tämä tapahtuma ColdCardQ:lla.



Tällä kertaa ei ole ongelmia, varoitusviestiä ei tule näkyviin, ja kun tuomme allekirjoitetun tapahtuman Sparrow wallet:ään, tällä kertaa kaksi allekirjoitusta on käytetty, joten tapahtuma on voimassa ja valmis jakeluun.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Yhteiskirjoitus Nunchukin kanssa



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & valkoiset osoitteet



Tässä kappaleessa käytämme Wallet Multisig Co-Signia Nunchukin kanssa ja käytämme tilaisuutta uusien käyttöehtojen soveltamiseen, jotta näemme, miten se sujuu.



Siirry kohtaan *Avanced Tools > ColdCard Co-Signing*.


Meitä pyydetään syöttämään "Spending Policy Key", jotta pääsemme valikkoon, jonka avulla voimme muuttaa käyttöehtoja. Meidän tapauksessamme kirjoitamme 12 x "beef".



Olemme päättäneet pitää suuruusluokan 21212 Sats ja enimmäisnopeuden "Limit Velocity" tähän opetusohjelmaan liittyvistä käytännön syistä. Toisaalta aiomme käyttää **"Whitelist Addresses "** -valikkoa määräämään osoitteet, joihin varojamme voidaan käyttää.




![Co-Sign](assets/fr/31.webp)




Skannaa QR-koodit, jotka liittyvät osoitteisiin (valitsemme 2), jotka haluat lisätä valkoiseen listaan, ja napsauta sitten **"ENTER "**. Kun olet vahvistanut osoitteet painamalla peräkkäin **"ENTER "**, näemme, että Magnitude- ja edunsaajaosoitteita koskevat rajoitukset on otettu käyttöön.



![Co-Sign](assets/fr/32.webp)



Lopuksi, jotta saat täydellisen kuvan "Co-Sign" -palvelun tarjoamista mahdollisuuksista, aktivoidaan "Web 2FA" -vaihtoehto.


Tämän ominaisuuden avulla voit käyttää TOTP RFC-6238 -yhteensopivaa sovellusta, kuten Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / tai Aegis Authenticator, lisätäksesi ylimääräisen Layer-turvan.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Konkreettisesti sanottuna ennen maksutapahtuman allekirjoittamista sinun on tuotava NFC-yhteensopiva, internet-yhteydellä varustettu laitteesi lähelle Coldcard-korttiasi. Tämä vie sinut automaattisesti coldcard.com-verkkosivulle, jossa sinua pyydetään syöttämään hakemuksesi 6-numeroinen koodi. Jos syötät oikean koodin, verkkosivu näyttää joko QR-koodin, jonka voit skannata ColdCardQ:ta varten, tai 8-numeroisen koodin, jonka voit syöttää Mk4-laitteellasi, jotta laitteesi saa luvan allekirjoittaa.





![Co-Sign](assets/fr/33.webp)



Kun olet skannannut kaksoistodennussovelluksessa näkyvän QR-koodin ja lisännyt ColdCard Co-Sign (CCC) -tilisi, sinua pyydetään varmistamaan, että kaikki on kunnossa, syöttämällä 2FA-koodisi.



Kirjoita ColdCard-korttisi NFC-laitteen takaosaan.



![Co-Sign](assets/fr/34.webp)



Kirjoita avautuvalle verkkosivulle suosikkisovelluksesi 2FA-koodi. Skannaa sitten ColdCardQ:n kanssa näkyvä QR-koodi (tai syötä Mk4:ssä näkyvä 8-numeroinen koodi).



![Co-Sign](assets/fr/35.webp)




Olemme nyt asettaneet rajoituksen suuruudelle (21212 Sats), kohdeosoitteille ja kaksinkertaiselle todennukselle.



![Co-Sign](assets/fr/36.webp)



### 2- Vie Wallet Multisig 2 vs. 3 Nunchukiin



Viedään Wallet Multisig 2-on-3 Nunchukiin tällä kertaa, kuten teimme aiemmin Sparrow:n kanssa.


Siirry kohtaan *Asetukset > Multisig Lompakot > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Valitse tällä kertaa NFC-vaihtoehto vientiä varten napsauttamalla ColdcardQ:n samannimistä painiketta **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Jos avaat sovelluksen Nunchukissa ensimmäistä kertaa, valitse **"Recover existing Wallet"**.



![Co-Sign](assets/fr/38.webp)



Jos sinulla on jo Wallet sovelluksessa, napsauta oikeassa yläkulmassa olevaa **"+"** ja sitten **"Recover existing Wallet"**.



![Co-Sign](assets/fr/39.webp)




Valitse sitten **"Recover Wallet from COLDCARD "** ja sitten **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Napauta lopuksi älypuhelimen takaosaa ColdCardQ-laitteen näyttöön, jotta voit tuoda Wallet:n NFC:n kautta.



![Co-Sign](assets/fr/41.webp)



Tilimme ja aiemmin Sparrow wallet:n kautta talletetut satoshit ovat palanneet.



![Co-Sign](assets/fr/42.webp)



### 3- Testaa ennalta määritettyjä menokäytäntöjä



Yritetään nyt tehdä transaktio, joka rikkoo asettamiamme kahta kulutusehtoa. **Yritetään käyttää yli 21212 Sats Address:lle, jota ei ole hyväksytty.** Yritetään lähettää 22 222 Sats Address:lle satunnaiselle Address:lle.



![Co-Sign](assets/fr/43.webp)



Kun tapahtuma on luotu, voit viedä sen ColdCard-korttiisi klikkaamalla kolmea pientä pistettä oikeassa yläkulmassa.



![Co-Sign](assets/fr/44.webp)



Valitse sitten **"Vie BBQR:n kautta "** ja skannaa ColdCardQ:n kanssa näkyvä QR-koodi.



![Co-Sign](assets/fr/45.webp)



ColdcardQ näyttää tämän jälkeen varoituksen, jossa näytön alareunaan vierittäessäsi selvitetään, että maksutapahtuma on odotetusti käyttöehtojen vastainen.



**Huomaa, että laite ei kerro meille, mitä menoehtoja siihen liittyy, jotta mahdollinen hyökkääjä ei yrittäisi kiertää rajoituksia.** **Huomaa, että laite ei kerro meille, mitä menoehtoja siihen liittyy, jotta mahdollinen hyökkääjä ei yrittäisi kiertää rajoituksia




![Co-Sign](assets/fr/46.webp)



Jos vielä vahvistat painamalla **"ENTER "**, allekirjoitettua tapahtumaa edustava QR-koodi tulee näkyviin. Jos tuot sen Nunchukilla, näet, että on käytetty vain yhtä allekirjoitusta.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Suoritetaan täsmälleen sama operaatio, mutta tällä kertaa transaktiolla, joka kunnioittaa suuruusrajaa (21212 Sats) ja lähettää satoshit yhteen kahdesta ennalta määritetystä osoitteesta.



Lähetämme Nunchuk 12121 Sats:n yhteen kahdesta osoitteestamme. Sitten viemme tapahtuman ColdCardiin, kuten aiemmin on tehty.



![Co-Sign](assets/fr/49.webp)




Kun olet tuonut allekirjoittamattoman tapahtuman ColdCardQ:een, katsotaan, mitä meille näytetään tällä kertaa.



Varoitus on aina läsnä, mutta tällä kertaa näytön alareunaan vierittämällä näemme, että maksutapahtuma on validoitava 2FA:n avulla. Laite pyytää meitä tuomaan ColdcardQ:n lähelle Internetiin yhdistettyä NFC-päätelaitetta (älypuhelin tai tabletti), minkä teemme.



![Co-Sign](assets/fr/50.webp)



Älypuhelimessamme avautuu verkkosivu, jossa meitä pyydetään syöttämään 2FA-koodimme, minkä teemme Proton Authenticatorin ansiosta.



![Co-Sign](assets/fr/51.webp)





Skannaa sitten verkkosivulla näkyvä QR-koodi ja valtuuta ColdCardisi allekirjoittamaan maksutapahtuma.


Tapahtuma on nyt allekirjoitettu kahdella avaimella, joten se on voimassa.



Jos ColdCardQ-laitteesi Push Tx on käytössä, voit lähettää tapahtuman suoraan verkkoon napauttamalla älypuhelimen takapuolta.



![Co-Sign](assets/fr/52.webp)




Jos "Push tx" ei ole aktivoitu, paina ColdCardQ:n "QR"-painiketta näyttääksesi allekirjoitetun tapahtuman QR-koodina ja tuo se Nunchukiin samalla tavalla kuin edellisessä esimerkissä.



![Co-Sign](assets/fr/53.webp)



Tällä kertaa huomaamme, että kaksi allekirjoitusta on käytetty, joten tapahtuma on valmis lähetettäväksi Bitcoin-verkkoon.



![Co-Sign](assets/fr/54.webp)




Olemme päässeet tämän opetusohjelman loppuun, joka antaa sinulle yleiskatsauksen Coinkiten ColdCardQ- ja Mk4-laitteisiin integroidun Co-Sign-toiminnon tarjoamista mahdollisuuksista sekä sen käytöstä lompakoiden, kuten Sparrow:n ja Nunchukin, kautta.