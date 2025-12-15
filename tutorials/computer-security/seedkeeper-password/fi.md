---
name: Seedkeeper - Salasananhallinta
description: Miten tallennat salasanasi Seedkeeper-älykortilla?
---

![cover](assets/cover.webp)



Seedkeeper on älykortti, jonka on kehittänyt Satochip, belgialainen yritys, joka on erikoistunut digitaalisten salaisuuksien hallintaan ja suojaamiseen tarkoitettuihin laitteistoratkaisuihin. Seedkeeper on tunnettu Bitcoin-ekosysteemiin tarkoitetuista älykorttivalikoimistaan, ja Satochip suunnitteli sen vaihtoehdoksi perinteisille menetelmille, joilla tallennetaan muistisääntöjä ja muita digitaalisia salaisuuksia.



Konkreettisesti Siementarkkailija on EAL6-sertifioitu monikäyttöinen älykortti, jossa on turvallinen prosessori ja väärentämissuojattu muisti (niin sanottu "Secure Element"). Kuten nimestä voi päätellä, sen tehtävänä on tallentaa Bitcoin-salkun muistitietoja ja salasanoja salatulla ja suojatulla tavalla. Seedkeeperillä voit generate, tuoda, järjestää ja tallentaa salaisuutesi suoraan kortin turvalliseen komponenttiin.



Mielestäni Seedkeeperillä on kaksi pääasiallista käyttötarkoitusta, joita tarkastelemme kahdessa erillisessä opetusohjelmassa:




- Bitcoin**-muistilauseiden tallennus: sen sijaan, että kirjoittaisit 12 tai 24 sanaa paperille, voit tuoda ne älykorttiin ja suojata ne PIN-koodilla.
- Salasanojen hallinta**: voit käyttää generate:ää vahvoja salasanoja Seedkeeper-sovelluksen kautta ja tallentaa ne suoraan älykorttiin, jolloin saat kätevän ja helppokäyttöisen offline-salasanojen hallinnan.



Teknisesti ottaen Seedkeeperin kapasiteetti on 8192 tavua, joten se voi tallentaa vähintään 50 erillistä salaisuutta (tarkka määrä riippuu salaisuuksien koosta ja kuhunkin salaisuuteen liittyvistä metatiedoista). Seedkeeperiä voidaan käyttää joko [tietokoneeseen liitetyn älykortinlukijan](https://satochip.io/accessories/) kautta tai mobiilisovelluksen kautta NFC-yhteyden avulla. Koko järjestelmä toimii offline-tilassa ilman Internet-yhteyttä, mikä takaa rajoitetun hyökkäyspinnan.



![Image](assets/fr/001.webp)



Erityisen mielenkiintoinen ominaisuus on mahdollisuus kopioida yhden Seedkeeper-tallentimen sisältö toiseen tallentimeen varmuuskopion luomista varten. Tässä oppaassa näytämme, miten juuri tämä tehdään.



Tässä oppaassa käsittelemme vain SeedKeeperin käyttöä perinteisten salasanojen hallintaan salasanahallinnan tapaan. Jos haluat käyttää SeedKeeperiä Bitcoin wallet-muistilauseiden tallentamiseen, katso tämä toinen opetusohjelma:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Miten saan siemenvartijan?



Seedkeeper voidaan hankkia kahdella tavalla. Voit [ostaa sen suoraan Satochipin virallisesta kaupasta](https://satochip.io/product/seedkeeper/) tai valtuutetulta jälleenmyyjältä. Mutta koska [Seedkeeper-sovellus on avointa lähdekoodia](https://github.com/Toporin/Seedkeeper-Applet), voit myös asentaa sen itse [tyhjälle älykortille](https://satochip.io/product/blank-javacard-for-diy-project/).



Jos haluat käyttää Seedkeeperin varmuuskopiointitoimintoa, sinun on luonnollisesti ostettava kaksi älykorttia.



## 2. Seedkeeper-asiakasohjelman asentaminen



Ensimmäinen vaihe on asentaa ohjelmisto tietokoneeseen tai älypuhelimeen. Tietokoneella sinun on [ladattava Satochip-Utilsin uusin versio](https://github.com/Toporin/Satochip-Utils/releases). Mobiililaitteissa Seedkeeper-sovellus on saatavilla [Google Play Storesta](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) ja [Apple App Storesta](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Siemenenvartijan alustaminen



Käynnistä sovellus ja napsauta "*Click & Scan*"-painiketta.



![Image](assets/fr/003.webp)



Sinulta kysytään PIN-koodia siementarkkailijaa varten. Koska kyseessä on uusi kortti, PIN-koodia ei ole vielä määritelty. Syötä mikä tahansa koodi ohittaaksesi tämän vaiheen ja napsauta sitten "*Seuraava*".



![Image](assets/fr/004.webp)



Aseta kortti sitten älypuhelimen takaosaan. Sovellus havaitsee, että Seedkeeperiä ei ole vielä alustettu, ja pyytää sinua asettamaan älykortin PIN-koodin, jonka pituus on 4-16 merkkiä. Optimaalisen turvallisuuden takaamiseksi valitse vankka PIN-koodi, joka on mahdollisimman pitkä, satunnainen ja koostuu useista eri merkeistä. Tämä PIN-koodi on ainoa este salasanojesi fyysiselle käytölle.



**Muista myös tallentaa tämä PIN-koodi nyt** esimerkiksi salasanahallintaan tai erilliselle fyysiselle tietovälineelle. Jälkimmäisessä tapauksessa älä koskaan säilytä PIN-koodin sisältävää tietovälinettä samassa paikassa kuin Seedkeeperiäsi, sillä muuten tämä suojaus on hyödytön. Luotettava varmuuskopio on tärkeää: ilman PIN-koodia et voi palauttaa Seedkeeperiin tallennettuja salaisuuksia.



![Image](assets/fr/005.webp)



Vahvista PIN-koodi toisen kerran.



![Image](assets/fr/006.webp)



Seedkeeper on nyt alustettu. Voit avata sen lukituksen syöttämällä juuri asettamasi PIN-koodin.



![Image](assets/fr/007.webp)



Pääset nyt älykortin hallintasivulle.



![Image](assets/fr/008.webp)



## 4. Tallenna salasanat Seedkeeperiin



Kun siemenvartijasi on avattu, napsauta "*+*"-painiketta.



![Image](assets/fr/009.webp)



Valitse "Luo salaisuus*". "*Tuo salaisuus*" -vaihtoehdon avulla voit tallentaa olemassa olevan salaisuuden (esimerkiksi aiemmin luodun salasanan).



![Image](assets/fr/010.webp)



Meidän tapauksessamme haluamme tallentaa salasanan. Napsauta "*Salasana*".



![Image](assets/fr/011.webp)



Määritä tälle salaisuudelle "*Label*", jotta se voidaan helposti tunnistaa, jos tallennat useita tietoja Seedkeeperiin. Voit myös lisätä salasanaan liittyvän tunnisteen ja sivuston URL-osoitteen.



![Image](assets/fr/012.webp)



Valitse salasanasi pituus ja parametrit ja napsauta sitten "*Generate*" ja sitten "*Import*".



![Image](assets/fr/013.webp)



Aseta Seedkeeper älypuhelimen takaosaan.



![Image](assets/fr/014.webp)



Salasanasi on rekisteröity.



![Image](assets/fr/015.webp)



## 5. Pääset käsiksi Seedkeeper-salasanaasi



Jos haluat tarkistaa salasanasi, ota Seedkeeper ja napsauta "*Click & Scan*"-painiketta.



![Image](assets/fr/016.webp)



Syötä PIN-koodi ja paina sitten "*Seuraava*".



![Image](assets/fr/017.webp)



Aseta Seedkeeper älypuhelimen takaosaan.



![Image](assets/fr/018.webp)



Tämä vie sinut luetteloon kaikista rekisteröidyistä salaisuuksistasi. Tässä esimerkissä haluan näyttää Plan ₿ Academy -tilini salasanan, joten napsautan sitä.



![Image](assets/fr/019.webp)



Paina "*Paljasta*"-painiketta.



![Image](assets/fr/020.webp)



Skannaa Seedkeeper uudelleen.



![Image](assets/fr/021.webp)



Aiemmin tallennettu salasanasi näkyy nyt näytöllä. Voit kopioida sen ja käyttää sitä kyseisellä verkkosivustolla.



![Image](assets/fr/022.webp)



## 6. Varmuuskopiointi Seedkeeperistä



Teemme nyt varmuuskopion Seedkeeperistä toiselle Seedkeeperille, jotta meillä on kaksi kopiota. Tämä redundanssi voi olla osa strategiaa tärkeimpien salasanojesi suojaamiseksi: esimerkiksi säilyttämällä Seedkeepereitä kahdessa eri paikassa fyysisten riskien rajoittamiseksi tai antamalla kopion luotettavan sukulaisen haltuun.



Tätä varten ota mukaan toinen siementenvartija (muista tunnistaa jompikumpi merkillä sekaannusten välttämiseksi). Aloita sen alustaminen tämän ohjeen vaiheessa 3 kuvatulla tavalla. Valitse jälleen kerran vahva PIN-koodi. Strategiastasi riippuen voit valita eri PIN-koodin tai säilyttää saman.



![Image](assets/fr/023.webp)



Avaa sovellus, napsauta "*Click & Scan*", syötä Seedkeeper n°1 (lähde) PIN-koodi ja skannaa se.



![Image](assets/fr/024.webp)



Tämä vie sinut etusivulle, jossa on luettelo salaisuuksistasi. Napsauta kolmea pientä pistettä käyttöliittymän oikeassa yläkulmassa.



![Image](assets/fr/025.webp)



Valitse "*Tehdä varmuuskopio*" ja paina sitten "*Aloita*".



![Image](assets/fr/026.webp)



Syötä varmuuskopiokortin PIN-koodi (Seedkeeper nro 2).



![Image](assets/fr/027.webp)



Skannaa sitten kortti.



![Image](assets/fr/028.webp)



Tee sama pääkortille (Seedkeeper nro 1) ja napsauta sitten "*Tuo varmuuskopio*".



![Image](assets/fr/029.webp)



Seedkeeper nro 2 sisältää nyt kaikki Seedkeeper nro 1:een tallennetut salaisuudet.



![Image](assets/fr/030.webp)



Voit skannata Seedkeeper n°2:n tarkistaaksesi, että salaisuudet on kopioitu.



![Image](assets/fr/031.webp)



Siinä kaikki! Nyt tiedät, miten käyttää Seedkeeperiä salasanojesi tallentamiseen. Tulevassa opetusohjelmassa katsomme, miten Seedkeeperiä käytetään Bitcoin wallet:n varmuuskopiointiin. Kutsun sinut myös tutustumaan sen yhdistettyyn käyttöön SeedSignerin kanssa:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356