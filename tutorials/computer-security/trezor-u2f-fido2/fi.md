---
name: Trezor U2F & FIDO2
description: Vahvista verkkoturvallisuuttasi Trezorin avulla
---
![cover](assets/cover.webp)



Trezor-laitteet ovat laitteistolompakoita, jotka on alun perin suunniteltu turvaamaan Bitcoin Wallet, mutta niissä on myös kehittyneitä vaihtoehtoja vahvaa todennusta varten verkossa. Koska ne ovat yhteensopivia **U2F**- ja **FIDO2**-protokollien kanssa, voit turvata pääsyn verkkotileillesi turvautumatta pelkästään salasanoihin.



Google ja Yubico esittelivät U2F-protokollan (*Universal 2nd Factor*) vuonna 2014, minkä jälkeen FIDO Alliance standardoi sen. Se mahdollistaa toisen fyysisen todentamistekijän (2FA) lisäämisen kirjautumisen yhteydessä. Kun se on aktivoitu, käyttäjien on klassisen salasanan lisäksi hyväksyttävä jokainen yritys muodostaa yhteys tiliinsä painamalla Trezorissa olevaa painiketta. Tässä yhteydessä Trezor toimii samalla tavalla kuin Yubikey.



Menetelmä perustuu epäsymmetriseen salaukseen: salaisia tietoja ei välitetä, joten phishing- tai salakuunteluhyökkäykset ovat tehottomia. Monet verkkopalvelut tukevat nyt U2F:ää.



Kaksitekijätodennuksen mahdollistavan U2F:n lisäksi Trezorit tukevat myös FIDO2:ta (*Fast IDentity Online 2.0*), joka on U2F:n kehitysversio. Kyseessä on vuonna 2018 standardoitu todennusprotokolla, joka laajentaa U2F:n logiikkaa ja jonka tavoitteena on korvata salasanat kokonaan. Se perustuu kahteen komponenttiin: *WebAuthn* (selainpuoli) ja *CTAP2* (fyysisen avaimen puoli). FIDO2 mahdollistaa "salasanattoman" todennuksen: käyttäjät tunnistautuvat ainoastaan Trezor-laitteensa avulla, joka toimii ainutlaatuisena kryptografisena tunnisteena, ilman ylimääräistä salasanaa. Tämä protokolla on nyt yhteensopiva useiden verkkopalvelujen kanssa, erityisesti yrityksille suunnattujen palvelujen kanssa.



Salasanattoman* toiminnallisuuden lisäksi FIDO2 mahdollistaa myös kaksitekijätodennuksen samalla tavalla kuin U2F.



FIDO2:ssa otetaan käyttöön myös käsite "resident credentials" eli suoraan Trezoriin tallennetut tunnistetiedot, jotka sisältävät sekä yhteyden mahdollistavan yksityisen avaimen että käyttäjän tunnistetiedot. Tämä mekanismi mahdollistaa aidosti salasanattoman todennuksen: kytke Trezor yksinkertaisesti laitteeseen ja vahvista pääsy ilman tunnuksen tai salasanan syöttämistä. Sitä vastoin perinteisemmät ei-paikalliset tunnukset tallentavat laitteeseen vain yksityisen avaimen; käyttäjätunnus on tallennettu palvelimen puolelle, joten se on syötettävä jokaisen yhteyden muodostamisen yhteydessä. Katsomme myöhemmin, miten ne tallennetaan Trezorilla.



Tässä oppaassa selvitämme, miten U2F tai FIDO2 aktivoidaan kaksitekijätodennusta varten ja miten FIDO2 määritetään, jotta voit käyttää tilejäsi ilman salasanaa suoraan Trezorilla.



**Huomaa:** U2F on yhteensopiva kaikkien Trezor-mallien kanssa, mutta FIDO2 on tuettu vain Safe 3:ssa, Safe 5:ssä ja Model T:ssä, ei Model One -mallissa.



## U2F/FIDO2:n käyttäminen 2FA:ta varten Trezorissa



Ennen kuin aloitat, varmista, että olet asettanut Bitcoin Wallet:n Trezoriin. On tärkeää tallentaa Mnemonic oikein, sillä U2F- ja FIDO2-avaimet, joita käytetään U2F- ja FIDO2-todennuksessa kaksitekijätodennuksessa, johdetaan tästä Mnemonic:sta. Jos Trezor-laitteesi katoaa tai vahingoittuu, voit saada avaimesi takaisin syöttämällä Mnemonic-lauseesi toiseen Trezor-laitteeseen (huomaa, että FIDO2-tunnistautumiseen "*salasanattomassa*" tilassa seed ei yksinään riitä, kuten näemme seuraavissa kappaleissa).



Liitä Trezor tietokoneeseen ja avaa sen lukitus.



![Image](assets/fr/01.webp)



Pääset tilille, jonka haluat suojata kaksitekijätodennuksella. Käytän esimerkiksi Bitwarden-tiliä. Löydät 2FA-vaihtoehdon yleensä palvelun asetuksista, välilehdiltä "*autentikointi*", "*turvallisuus*", "*kirjautuminen*" tai "*salasana*".



![Image](assets/fr/02.webp)



Valitse kaksitekijätodennusta koskevassa osiossa "*Passkey*"-vaihtoehto (termi voi vaihdella käyttämästäsi sivustosta riippuen).



![Image](assets/fr/03.webp)



Sinua pyydetään usein vahvistamaan nykyinen salasanasi.



![Image](assets/fr/04.webp)



Anna suojausavaimelle nimi, jotta se on helppo tunnistaa, ja napsauta sitten "*Lue avain*".



![Image](assets/fr/05.webp)



Tilitietosi näkyvät Trezorin näytöllä. Vahvista koskettamalla näyttöä tai painamalla -painiketta. Sinua pyydetään myös vahvistamaan PIN-koodisi.



![Image](assets/fr/06.webp)



Rekisteröi tämä suojausavain.



![Image](assets/fr/07.webp)



Tästä lähtien, kun haluat muodostaa yhteyden tiliisi, sinua pyydetään tavallisen salasanasi lisäksi yhdistämään Trezorisi.



![Image](assets/fr/08.webp)



Voit sitten painaa Trezorin näyttöä vahvistaaksesi todennuksen.



![Image](assets/fr/09.webp)



Hardware Wallet Trezorin käyttämisen etuna kaksitekijätodennuksessa on se, että voit helposti palauttaa avaimesi Mnemonic-lauseen ansiosta. Tämän perusvarmuuskopion lisäksi voit käyttää myös hätäkoodia, jonka tarjoaa jokainen palvelu, jossa olet aktivoinut 2FA:n. Tämän hätäkoodin avulla voit muodostaa yhteyden tiliisi, jos hukkaat turvaavaimesi. Se korvaa siis 2FA:n yhteyden muodostamiseksi tarvittaessa.



Esimerkiksi Bitwardenissa saat tämän koodin näkyviin napsauttamalla "*View recovery code*".



![Image](assets/fr/10.webp)



Suosittelen, että säilytät tätä koodia eri paikassa kuin pääsalasanaasi, jotta niitä ei varasteta yhdessä. Jos esimerkiksi salasanasi on tallennettu salasanahallintaan, säilytä 2FA-hätäkoodia paperilla, erikseen.



Tämä lähestymistapa tarjoaa kaksi varmuuskopiotasoa, jos Trezor 2FA-todennuksen menetyksen sattuessa: ensimmäinen varmuuskopio, jossa käytetään Mnemonic-lausetta kaikille tileillesi, ja toinen varmuuskopio, jossa käytetään hätäkoodeja kullekin tilille. On kuitenkin tärkeää, että **ei sekoiteta Mnemonic:n ja hätäkoodin roolia**:




- 12- tai 24-sanaisen Mnemonic-lauseen avulla pääset käsiksi 2FA-avaimiin kaikilla tileilläsi, mutta myös Trezorilla suojattuihin bitcoineihisi;
- Hätäkoodin avulla voit ohittaa 2FA-pyynnön väliaikaisesti vain kyseisellä tilillä (tässä esimerkissä vain Bitwardenissa).



## FIDO2:n käyttäminen Trezorissa



Kaksitekijätodennuksen lisäksi FIDO2 mahdollistaa myös "salasanattoman" todentamisen eli sen, ettei sivustolle kirjauduttaessa tarvitse syöttää salasanaa. Liitä Trezor yksinkertaisesti tietokoneeseen, jotta voit käyttää suojattua tiliäsi tällä tavoin. Tässä kerrotaan, miten tämä ominaisuus määritetään.



Ennen kuin aloitat, varmista, että olet asettanut Bitcoin Wallet:n Trezoriin. Mnemonic:n tallentaminen on tärkeää, sillä FIDO2 "*salasanattomat*" tunnukset on salattu seed:lla (seuraavassa osassa kerrotaan, miten tunnukset tallennetaan oikein).



Liitä Trezor tietokoneeseen ja avaa sen lukitus.



![Image](assets/fr/01.webp)



Pääset tilille, jonka haluat suojata "*salasanattomassa*" tilassa. Käytän esimerkkinä Bitwarden-tiliä. Tämä vaihtoehto löytyy yleensä palvelun asetuksista, usein "*autentikointi*", "*turvallisuus*" tai "*salasana*" -välilehdeltä.



Esimerkiksi Bitwardenissa tämä vaihtoehto löytyy "*Haastesalasana*"-välilehdeltä. Klikkaa "*Turn on*" aktivoidaksesi todennuksen FIDO2:n kautta.



![Image](assets/fr/11.webp)



Sinua pyydetään usein vahvistamaan salasanasi.



![Image](assets/fr/12.webp)



Tilitietosi näkyvät Trezorin näytöllä. Vahvista koskettamalla näyttöä tai painamalla -painiketta. Sinun on myös vahvistettava PIN-koodisi.



![Image](assets/fr/13.webp)



Lisää sivustolla nimi, jolla muistat suojausavaimesi, ja napsauta sitten "*Kytke päälle*".



![Image](assets/fr/14.webp)



Tämän jälkeen sinua pyydetään tunnistamaan henkilöllisyytesi, jotta voidaan tarkistaa, että avain toimii oikein.



![Image](assets/fr/15.webp)



Tästä lähtien tilillesi kirjauduttaessa ei enää tarvitse syöttää sähköpostiosoitettasi Address tai käyttäjätunnusta. Napsauta vain painiketta tunnistaaksesi itsesi fyysisellä avaimella kirjautumislomakkeella.



![Image](assets/fr/16.webp)



Vahvista yhteys Trezoriin syöttämällä Hardware Wallet PIN-koodi.



![Image](assets/fr/17.webp)



Saat yhteyden tiliisi ilman, että sinun tarvitsee syöttää salasanaasi.



![Image](assets/fr/18.webp)



**Huomaa, että vaikka aktivoisit "*salasanattoman*" todennuksen FIDO2:n kautta Trezorissa, verkkotilisi pääsalasana on edelleen voimassa kirjautumista varten**



## Tallenna FIDO2-tunnukset (tunnukset asukkaat)



Jos käytät FIDO2:ta tai U2F:ää kaksitekijätodennukseen, eli kirjaudut tileille, jotka vaativat salasanan lisäksi 2FA-varmennuksen Trezorin kautta, Mnemonic-lauseella saat avaimesi käyttöösi. Jos kuitenkin käytät FIDO2:ta "*salasanattomassa*" tilassa, kuten edellisessä jaksossa kuvattiin, on tarpeen tehdä kopio FIDO-tunnisteistasi sen lisäksi, että varmuuskopioit Mnemonic-lauseen, joka salaa nämä tunnisteet.



Tätä varten tarvitset tietokoneen, johon on asennettu Python. Avaa terminaali ja suorita seuraava komento asentaaksesi tarvittavat Trezor-ohjelmistot:



```shell
pip3 install --upgrade trezor
```



Liitä Trezor tietokoneeseen USB:n kautta ja avaa sen lukitus PIN-koodilla.



![Image](assets/fr/01.webp)



Voit hakea Trezoriin tallennettujen FIDO2-tunnisteiden luettelon suorittamalla seuraavan komennon:



```shell
trezorctl fido credentials list
```



Vahvista vienti Trezorissa.



![Image](assets/fr/19.webp)



FIDO2-kirjautumistietosi näkyvät päätelaitteessasi. Esimerkiksi Bitwarden-tilini osalta sain nämä tiedot:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopioi ja tallenna kaikki nämä tiedot tekstitiedostoon. Tähän varmuuskopiointiin ei liity muita merkittäviä riskejä kuin sen paljastaminen, että käytät näitä palveluja FIDO2:n kanssa. "*Credential ID*" on salattu Wallet:n seed:lla, mikä tarkoittaa, että tämän varmuuskopion hankkinut hyökkääjä ei pystyisi muodostamaan yhteyttä tileihisi, vaan ainoastaan huomaamaan, että käytät näitä tilejä. Jotta voit purkaa näiden tunnusten salauksen, tarvitset Wallet:n seed:n.



Voit siis luoda useita kopioita tästä tekstitiedostosta ja tallentaa ne eri paikkoihin, esimerkiksi paikallisesti tietokoneellesi, tiedostojen isännöintipalveluun ja ulkoiselle tietovälineelle, kuten USB-tikulle. Muista kuitenkin, että tämä varmuuskopio ei päivity automaattisesti, joten sinun on uusittava se aina, kun muodostat uuden "*salasanattoman*" yhteyden Trezoriin.



Kuvitellaan nyt, että olet rikkonut Trezorisi. Saadaksesi FIDO2-tunnuksesi takaisin sinun on ensin palautettava Wallet-laitteesi Mnemonic-lauseen avulla uudella FIDO2-yhteensopivalla Trezor-laitteella.



Kun palautus on valmis, voit tuoda FIDO2-tunnukset uuteen laitteeseen suorittamalla terminaalissa seuraavan komennon:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Korvaa yksinkertaisesti `<CREDENTIAL_ID>` jollakin tunnuksellasi. Esimerkiksi minun tapauksessani tämä antaisi:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor pyytää sinua tuomaan FIDO2-tunnuksesi. Vahvista painamalla näytössä.



![Image](assets/fr/20.webp)



FIDO2-kirjautuminen on nyt käytössä Trezorissa. Toista tämä menettely jokaiselle tunnuksellesi.



Onneksi olkoon, olet nyt valmiina käyttämään Trezoria U2F:n ja FIDO2:n kanssa! Jos tämä opetusohjelma oli mielestäsi hyödyllinen, olisin hyvin kiitollinen, jos jättäisit Green-peukalon alle. Voit vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!



Suosittelen myös tätä toista opetusohjelmaa, jossa tarkastelemme toista ratkaisua U2F- ja FIDO2-todennukseen:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e