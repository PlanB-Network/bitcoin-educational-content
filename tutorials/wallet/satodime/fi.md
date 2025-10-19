---
name: Satodime
description: Selvitä, miten Satodimea käytetään mobiilisovelluksen avulla
---
![cover](assets/cover.webp)



Tässä oppaassa käydään läpi Satodime-mobiilisovelluksen asennus, konfigurointi ja käyttö. Opit, miten saat korttisi haltuun, luot kassakaappeja, lisäät varoja, purat kortin ja palautat yksityiset avaimesi. Liitteissä on resursseja, parhaita käytäntöjä ja teknisiä selityksiä.



## Johdanto



***[Satochipin](https://satochip.io/fr/)** kehittämä *Satodime** on suojattu haltijakortti Bitcoin:n tallentamiseen konkreettisella ja yksinkertaisella tavalla. Se toimii Hardware Wallet:n itsesäilyttäjänä, jossa sinulla on täysi hallintaoikeus yksityisiin avaimiisi ilman riippuvuutta kolmannesta osapuolesta. Se on avoimen lähdekoodin ja EAL6+-sertifioitu ja tukee jopa kolmea itsenäistä tallelokeroa.



### Tuotteen tausta



Satodime, **carte au porteur, kuuluu sille, joka sen fyysisesti omistaa**, eikä sitä tarvitse rekisteröidä tai tunnistaa etukäteen. Se vastaa turvallisen, kannettavan Bitcoin-säilytyksen tarpeeseen, sillä kuka tahansa, jolla on kortti, voi käyttää sitä tai siirtää bitcoineja skannaamalla sen mobiilisovelluksen avulla haltuunottoon tai kassakaappien avaamiseen. Toisin kuin paperilaskussa, kortti käyttää Seal yksityisten avainten tallentamiseen suojattua sirua, joka paljastuu vasta sulkemisen jälkeen, jolloin kortti muistuttaa käteistä rahaa, jonka Ownership määräytyy fyysisen hallussapidon perusteella. Kortti sopii erinomaisesti bitcoinien lahjoittamiseen, sillä se helpottaa bitcoinien turvallista siirtämistä kädestä käteen, ja mobiilisovellus hyödyntää NFC:tä älypuhelimen vuorovaikutuksen mahdollistamiseksi.





- Turvallisuus**: Yksityiset avaimet luodaan ja tallennetaan väärentämisen estävään siruun; näkyvä tila (suljettu, suljettu, suljettu, tyhjä).
- Ominaisuudet**: Osta bitcoineja suoraan sovelluksen kautta (Paybis-kumppani); hallinnoi Mainnet ja Testnet.
- Avoin lähdekoodi**: AGPLv3-lisenssin alainen koodi, todennettavissa GitHubissa.



### Jatkuva kehitys



Sovellus kehittyy säännöllisesti. Tarkista päivitykset Satochipin verkkosivuilta tai kaupoista. Esimerkiksi uusia lohkoketjuja tai ostotoimintoja voidaan lisätä. Tarkista [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) jatkuvasta kehityksestä.



## 1. Edellytykset



Ennen kuin aloitat **Satodime**:n käytön, varmista, että sinulla on seuraavat tavarat:





- Yhteensopiva älypuhelin**: NFC-toiminnolla varustettu Android- tai iOS-laite.
- Satodime**-kortti: Uusi tai alustamaton.
- Internet-yhteys**: Lataa sovellus.
- Perustiedot**: Ymmärrys yksityisistä/julkisista avaimista ja niiden menettämisen riskeistä (peruuttamaton).
- Turvallinen väline**: Turvallinen paikka, johon yksityiset avaimet voidaan tallentaa, kun ne on purettu (paperi, metalli, ei koskaan digitaalinen).



## 2. Asennus





- Lataa hakemus** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Tarkista kehittäjä (Satochip) petosten välttämiseksi.
 - Satodime on **avoin lähdekoodi**. Lähdekoodi : [Satochipin GitHub](https://github.com/Toporin/Satodime-Applet).





- Asenna ja käynnistä sovellus**: Aktivoi puhelimen NFC tarvittaessa.



![image](assets/fr/01.webp)



## 3. Alkuperäinen konfigurointi



### 3.1 Käynnistä sovellus ja skannaa



Avaa sovellus ja seuraa ohjattua toimintoa. Aseta Satodime-kortti puhelimesi NFC-lukijaan (yleensä takana). Pidä sitä alhaalla koko toiminnon ajan, jotta yhteys on vakaa.





- Jos NFC ei toimi, tarkista puhelimen asetukset.
- Malja vahvistaa menestyksen: "Onnistunut lukeminen".



![image](assets/fr/02.webp)



Pääsääntöisesti **kaikki seuraavat toiminnot edellyttävät vahvistusta Satodime-kortin skannauksella**



### 3.2 Kortin haltuunotto (*Ownership*)



Ensimmäistä käyttökertaa varten tulee kortin omistajaksi, jotta kortti voidaan turvata:





- Napsauta sovelluksessa "*Take Ownership*".
- Vahvista toiminto: tämä luo yksilöllisen omistajan avaimen.
- Skannaa kartta uudelleen, jotta muutokset tulevat voimaan.
- Varoitus**: Tämä vaihe on peruuttamaton. Katso [artikkeli *Ownership*] (https://satochip.io/satodime-Ownership-explained/).



![image](assets/fr/03.webp)




## 4. Luo turvallinen



Satodime tukee enintään 3 kassakaappia. Luo yksi tallentamaan Bitcoin :





- Valitse tyhjä kassakaappi (esim. Kassakaappi 01).
- Valitse Blockchain (Bitcoin).
- Napsauta "*Create & Seal*".
- Skannaa kortti generate:lle ja Seal:lle yksityinen avain (joka on tuntematon, kunnes se on avattu).
- Onnittelut**: Kassakaappisi on nyt sinetöity ja valmis vastaanottamaan varoja.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Lisää varoja



Kun se on suljettu, lataa kassakaappiin bitcoineja:





- Valitse kassakaappi.
- Napsauta "*Lisää varoja*".
- Kopioi julkinen Address tai skannaa QR-koodi.
- Lähetä varoja toisesta Wallet:stä.
- Tarkista saldo Blockchain:n vahvistuksen jälkeen.
- Ostovaihtoehto: Klikkaa "*Osta*" ostaaksesi suoraan Paybis-palvelun kautta (Visa, Mastercard jne.). Sovellettavat maksut.



![image](assets/fr/06.webp)



## 6. Kassakaapin sinetöinnin avaaminen



Jos haluat päästä käsiksi yksityiseen avaimeen ja siirtää varat muualle, avaa kassakaappi:





- Valitse suljettu kassakaappi.
- Napsauta "Unseal".
- Vahvista varoitus: Tämä toimenpide on peruuttamaton.
- Skannaa kortti avataksesi sen.
- Kassakaapin tilaksi on asetettu "*Ensuljettu*"; yksityinen avain voidaan nyt tarkastella/viettää.
- Varoitus**: Kun salaus on avattu, yksityinen avain on käytettävissä. Jos joku ottaa älypuhelimesi haltuunsa, hän voi päästä käsiksi tähän avaimeen ja siten saada kassakaapissasi olevat varat takaisin (peruuttamattomasti).



![image](assets/fr/07.webp)



## 7. Palauta yksityinen avain



Kun olet poistanut sinetöinnin, vie avain käytettäväksi toisessa Wallet -laitteessa:





- Varmista, että olet turvallisessa ympäristössä.
- Napsauta "*Näytä yksityinen avain*".
- Valitse muoto: Legacy, SegWit, WIF jne.
- Kopioi avain tai skannaa QR-koodi.
- Turvallisuus**: Turvallisuus: Älä koskaan jaa yksityistä avaintasi. Säilytä se offline-tilassa.
- Tuo se Wallet-ohjelmistoon, joka on yhteensopiva rahastojen hallinnoinnin kanssa (esim. Sparrow wallet tai Electrum).



![image](assets/fr/08.webp)





## 8. Nollaa runko



Kassakaapin nollaaminen poistaa siihen liittyvän yksityisen avaimen peruuttamattomasti. Toisin sanoen, jos et ole varmistanut kopiota yksityisestä avaimestasi tai tuonut sitä toiseen Wallet:ään, kassakaapin nollaaminen aiheuttaa kassakaapissa olevien varojen peruuttamattoman menetyksen.



![image](assets/fr/09.webp)



Rungon nollaaminen tyhjentää korttipaikan ja tekee sen valmiiksi uutta runkoa varten.



## 9. Siirto Ownership



Jos haluat esimerkiksi tarjota bitcoineja Satodimen kautta, sinun on :




- Ota Ownership kortista,
- Luo Bitcoin-turvakaappi,
- Siirrä Satss sinne,
- Siirrä kortti Ownership: kortin omistajaksi tulee henkilö, joka skannaa kortin seuraavaksi,
- Anna Satodime-kortti haluamallesi henkilölle ja pyydä häntä lataamaan sovellus ja skannaamaan kortti, jotta hän voi ottaa Ownership-kortin - ja näin päästä käsiksi kortille "tallennettuihin" bitcoineihin.



![image](assets/fr/10.webp)




## LIITTEET



### A1. Parhaat käytännöt



Käyttääksesi **Satodimea** turvallisesti :





- Varmista kortti**: Käsittele sitä kuin käteistä; katoaminen = menetetyt varat, jos ei omistaja.
- Tärkein varmuuskopio**: Tallenna yksityiset avaimet sinetöinnin purkamisen jälkeen turvalliselle fyysiselle tietovälineelle. Ei koskaan digitaalisesti.
- Tarkista tila**: Tarkista aina kortti Ownership ja kassakaappien sinetöity tai sinetöimätön tila skannaamalla.
- Luottamuksellisuus**: Käytä uusia osoitteita; vältä keskitettyjä vaihtoja siirtoja varten.
- Päivitykset**: Pidä sovellus ajan tasalla kauppojen kautta.
- Toipuminen**: Jos kortti on kadonnut, mutta se on omistuksessa, varat ovat Blockchain:ssä; käytä yksityistä avainta, jos se on sinetöity.



### A2. Lisäresurssit



Erityisesti Satodime :




- [Satodime-tuote](https://satochip.io/fr/product/satodime/)
- [Mobiiliopas](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Network](https://planb.network/), jossa on oppaita itsesäilytyksestä, yksityisistä avaimista jne.



**Tallenna palautuslauseesi** :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Ohjearvio Satochipistä (tuotemerkin ensimmäinen tuote) :**



https://planb.network/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Siementenhoitajan opetusohjelmat:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Tietoja Satochipistä



**Viralliset linkit** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Tuki: info@satochip.io



**Satochip** on belgialainen yritys, joka kehittää laitteisto- ja ohjelmistoratkaisuja bitcoinien ja muiden kryptovaluuttojen hallintaan ja säilytykseen. Sen lippulaivatuote, Satochip Hardware Wallet, on NFC-kortti, joka on varustettu EAL6+-sertifioidulla secure element:llä. Seedkeeper, Mnemonic-lauseen ja salaisuuden hallitsija, ja Satodime, haltijakortti, täydentävät Satochipin kattavan valikoiman, joka on räätälöity käyttäjien tarpeisiin. Avoimen lähdekoodin ohjelmistolla toimivien laitteiden tavoitteena on demokratisoida Bitcoin:n tietoturva.