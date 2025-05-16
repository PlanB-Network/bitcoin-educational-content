---
name: Ledger U2F & FIDO2
description: Paranna verkkoturvallisuuttasi Ledger:n avulla
---
![cover](assets/cover.webp)



Ledger-laitteet ovat laitteistolompakoita, jotka on alun perin suunniteltu turvaamaan Bitcoin Wallet, mutta niissä on myös kehittyneitä vaihtoehtoja vahvaa todennusta varten verkossa. Koska ne ovat yhteensopivia **U2F**- ja **FIDO2**-protokollien kanssa, voit turvata verkkotilien käytön asettamalla toisen todentamistekijän.



Google ja Yubico esittivät U2F-protokollan (Universal 2nd Factor) vuonna 2014, minkä jälkeen FIDO Alliance standardoi sen. Se mahdollistaa toisen fyysisen todentamistekijän (2FA) lisäämisen kirjautumisen yhteydessä. Kun se on aktivoitu, käyttäjien on klassisen salasanan lisäksi hyväksyttävä jokainen yritys muodostaa yhteys tiliinsä painamalla painiketta Ledger:ssä. Tässä yhteydessä Ledger toimii samalla tavalla kuin Yubikey. U2F on itse asiassa FIDO2-standardin alakomponentti, joka kattaa sen ja tuo samalla merkittäviä parannuksia, kuten natiivin tuen nykyaikaisille selaimille ja suuremman joustavuuden todentamisavainten hallinnassa.



Nämä menetelmät perustuvat epäsymmetriseen salaukseen: salaisia tietoja ei välitetä, joten phishing- tai salakuunteluhyökkäykset ovat tehottomia. Monet verkkopalvelut tukevat nyt U2F- ja FIDO2-tunnuksia.



Tässä ohjeessa näytämme, miten U2F ja FIDO2 aktivoidaan kaksitekijätodennusta varten Ledger:ssa.



**Huomaa:** U2F ja FIDO2 ovat tuettuja kaikissa Ledger-laitteissa, joissa on uusin laiteohjelmisto: Nano X ja Nano S classic -laitteissa versiosta 2.1.0 alkaen ja Nano S Plus -laitteissa versiosta 1.1.0 alkaen. Stax- ja Flex-mallit ovat täysin yhteensopivia.



## Asenna Ledger Security Key -sovellus



Jos käytät Ledger-laitetta, tiedät luultavasti, että laiteohjelmisto ei yksinään sisällä kaikkia kryptolompakoiden hallintaan tarvittavia ominaisuuksia. Jos haluat käyttää esimerkiksi Bitcoin Wallet -laitetta, sinun on asennettava "*Bitcoin*"-sovellus. Vastaavasti MFA-avainten hallitsemiseksi sinun on asennettava "*Security Key*"-sovellus.



Ennen kuin aloitat, varmista, että olet asentanut Bitcoin Wallet:n Ledger:ään. On tärkeää tallentaa Mnemonic oikein, sillä 2FA:ssa käytettävät avaimet johdetaan tästä Mnemonic:sta. Jos Ledger-laitteesi katoaa tai vahingoittuu, voit saada avaimesi takaisin syöttämällä Mnemonic-lausekkeesi toiseen Ledger-laitteeseen (tällä hetkellä FIDO2-tunnisteita "*salasanattomassa*" tilassa ei vielä tueta Ledgersissä, joten käytössä ei ole vakituisia tunnisteita).



Liitä Ledger tietokoneeseen ja avaa sen lukitus.



![Image](assets/fr/01.webp)



Asenna sovellus avaamalla [Ledger Live] -ohjelmisto (https://www.Ledger.com/Ledger-live) ja siirtymällä sitten "*My Ledger*" -välilehdelle. Etsi "*Security Key*" -sovellus ja asenna se laitteeseesi.



![Image](assets/fr/02.webp)



"*Turva-avain*"-sovelluksen pitäisi nyt näkyä muiden Ledger:een asennettujen sovellusten rinnalla.



![Image](assets/fr/03.webp)



Napsauta sovellusta jättäessäsi sen auki ohjeen seuraavia vaiheita varten.



![Image](assets/fr/04.webp)



## Käytä U2F/FIDO2:ta 2FA:ta varten Ledger:n kanssa



Pääset tilille, jonka haluat suojata kaksitekijätodennuksella. Käytän esimerkiksi Bitwarden-tiliä. Löydät 2FA-vaihtoehdon yleensä palvelun asetuksista, välilehdiltä "*autentikointi*", "*turvallisuus*", "*kirjautuminen*" tai "*salasana*".



![Image](assets/fr/05.webp)



Valitse kaksitekijätodennusta koskevassa osiossa "*Passkey*"-vaihtoehto (termi voi vaihdella käyttämästäsi sivustosta riippuen).



![Image](assets/fr/06.webp)



Sinua pyydetään usein vahvistamaan nykyinen salasanasi.



![Image](assets/fr/07.webp)



Anna suojausavaimelle nimi, jotta se on helppo tunnistaa, ja napsauta sitten "*Lue avain*".



![Image](assets/fr/08.webp)



Tilisi tiedot näkyvät Ledger-näytössä. Vahvista painamalla "*Register*"-painiketta (tai molempia painikkeita samanaikaisesti käyttämästäsi mallista riippuen).



![Image](assets/fr/09.webp)



Avain on rekisteröity onnistuneesti.



![Image](assets/fr/10.webp)



Rekisteröi tämä suojausavain.



![Image](assets/fr/11.webp)



Kun kirjaudut sisään tilillesi, sinua pyydetään tästä lähtien tavallisen salasanasi lisäksi yhdistämään Ledger.



![Image](assets/fr/12.webp)



Tämän jälkeen voit vahvistaa todennuksen painamalla Ledger:n näytön "*Log in*"-painiketta (tai molempia painikkeita samanaikaisesti käyttämästäsi mallista riippuen).



![Image](assets/fr/13.webp)



Hardware Wallet Ledger:n käyttämisen etuna kaksitekijätodennuksessa on se, että voit helposti palauttaa avaimesi Mnemonic-lauseen ansiosta. Tämän perusvarmistuksen lisäksi voit käyttää myös hätäkoodia, jonka jokainen palvelu, jossa olet aktivoinut 2FA:n, toimittaa. Tämän hätäkoodin avulla voit muodostaa yhteyden tiliisi, jos hukkaat turvaavaimesi. Se korvaa siis 2FA:n yhteyden muodostamiseksi tarvittaessa.



Esimerkiksi Bitwardenissa saat tämän koodin näkyviin napsauttamalla "*View recovery code*".



![Image](assets/fr/14.webp)



Suosittelen, että säilytät tätä koodia eri paikassa kuin pääsalasanaasi, jotta niitä ei varasteta yhdessä. Jos esimerkiksi salasanasi on tallennettu salasanahallintaan, säilytä 2FA-hätäkoodia paperilla, erikseen.



Tämä lähestymistapa tarjoaa kaksi varmuuskopiointitasoa, jos Ledger 2FA-todennuksen menetys tapahtuu: ensimmäinen varmuuskopio, jossa käytetään Mnemonic-lause kaikkien tilien osalta, ja toinen tilikohtainen varmuuskopio, jossa käytetään hätäkoodeja. On kuitenkin tärkeää, että **ei sekoiteta Mnemonic:n roolia hätäkoodin rooliin** :




- 12- tai 24-sanaisen Mnemonic-lauseen avulla pääset käsiksi 2FA-avaimiin kaikilla tileilläsi, mutta myös Ledger:llä suojattuihin bitcoineihisi;
- Hätäkoodin avulla voit ohittaa 2FA-pyynnön väliaikaisesti vain kyseisellä tilillä (tässä esimerkissä vain Bitwardenissa).



Onneksi olkoon, olet nyt ajan tasalla Ledger:n käyttämisestä makrotaloudellista rahoitusapua varten! Jos pidit tätä ohjetta hyödyllisenä, olisin hyvin kiitollinen, jos jättäisit Green-peukalon alle. Voit vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!



Suosittelen myös tätä toista opetusohjelmaa, jossa tarkastelemme toista ratkaisua U2F- ja FIDO2-todennukseen:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e