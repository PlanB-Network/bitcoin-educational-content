---
name: Seedkeeper
description: Miten varmuuskopioin wallet Bitcoin:n Seedkeeper-älykortilla?
---

![cover](assets/cover.webp)



Seedkeeper on älykortti, jonka on kehittänyt Satochip, belgialainen yritys, joka on erikoistunut digitaalisten salaisuuksien hallintaan ja suojaamiseen tarkoitettuihin laitteistoratkaisuihin. Satochip on tunnettu Bitcoin-ekosysteemiin tarkoitetuista älykorttivalikoimistaan, ja se suunnitteli Seedkeeper-kortin vaihtoehdoksi perinteisille muistilauseiden tallennusmenetelmille.



Konkreettisesti Siementarkkailija on EAL6-sertifioitu monikäyttöinen älykortti, jossa on turvallinen prosessori ja väärentämissuojattu muisti (niin sanottu "Secure Element"). Kuten nimestä voi päätellä, sen tehtävänä on tallentaa Bitcoin wallet-muistitietoja ja salasanoja salatulla ja suojatulla tavalla. Seedkeeperillä voit generate, tuoda, järjestää ja tallentaa salaisuutesi suoraan kortin turvalliseen komponenttiin.



Mielestäni Seedkeeperillä on kaksi pääasiallista käyttötarkoitusta, joita tarkastelemme kahdessa erillisessä opetusohjelmassa:




- Bitcoin**-muistilauseiden tallennus: sen sijaan, että kirjoittaisit 12 tai 24 sanaa paperille, voit tuoda ne älykorttiin ja suojata ne PIN-koodilla.
- Salasanojen hallinta**: Voit käyttää generate:ää vahvaa salasanaa Seedkeeper-sovelluksen kautta ja tallentaa ne suoraan älykorttiin, jolloin saat kätevän ja helppokäyttöisen offline-salasanojen hallinnan.



Teknisesti ottaen Seedkeeperin kapasiteetti on 8192 tavua, joten se voi tallentaa vähintään 50 erillistä salaisuutta (tarkka määrä riippuu salaisuuksien koosta ja kuhunkin salaisuuteen liittyvistä metatiedoista). Seedkeeperiä voidaan käyttää joko [tietokoneeseen liitetyn älykortinlukijan](https://satochip.io/accessories/) kautta tai mobiilisovelluksen kautta NFC-yhteyden avulla. Koko järjestelmä toimii offline-tilassa ilman Internet-yhteyttä, mikä takaa rajoitetun hyökkäyspinnan.



![Image](assets/fr/001.webp)



Erityisen mielenkiintoinen ominaisuus on mahdollisuus kopioida yhden Seedkeeper-tallentimen sisältö toiseen tallentimeen varmuuskopion luomista varten. Tässä oppaassa näytämme, miten juuri tämä tehdään.



Seedkeeper on myös erittäin mielenkiintoinen yhdistettynä wallet:n tilattomaan laitteistoon, kuten SeedSigneriin tai Specter DIY:hen. Tällöin ei tarvitse käyttää Satochipin asiakasta tietokoneella tai matkapuhelimessa. Seedkeeper pitää seed:n secure element:ssaan, ja sitä voidaan käyttää suoraan allekirjoituslaitteen kanssa, jolloin paperista QR-koodia ei tarvita. En kehitä tätä tiettyä käyttötapausta tässä opetusohjelmassa, sillä sitä käsitellään toisessa erillisessä opetusohjelmassa :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Mihin käyttötarkoitukseen Seedkeeperiä käytetään?



Tässä oppaassa käsittelen vain Bitcoin:een liittyviä käyttötapauksia, sillä siitä tässä oppaassa on kyse. Emme käsittele salasanojen hallintatoimintoja, jotka ovat toisen opetusohjelman aiheena.



Seedkeeperillä on useita etuja verrattuna pelkkään muistilauseen varmuuskopiointiin paperilla:





- Varkauden kestävä:** wallet:n seed:een ei pääse käsiksi selväkielisenä tekstinä. Sen poimiminen edellyttää siemenenvartijan PIN-koodin tuntemista. Varas, joka saa laitteen haltuunsa, ei voi tehdä sillä mitään ilman tätä koodia.





- Riskin jakaminen kahteen tekijään:** Voit jakaa turvallisuuden digitaaliseen ja fyysiseen tekijään. Jos esimerkiksi tallennat Seedkeeper PIN-koodin salasanahallintaasi, tarvitset sekä pääsyn tähän hallintaan että älykortin fyysisen hallussapidon saadaksesi seed:n (hyökkäyksen todennäköisyys on huomattavasti pienempi).





- Keskitetty hallinta:** Seedkeeper helpottaa useiden eri salkkujen siementen hallintaa.





- Helppo varmuuskopiointi:** yksinkertaisesti kopioi salatut varmuuskopiot muille SeedKeeperille.



seed:stä on kuitenkin useita haittoja verrattuna yksinkertaiseen paperiseen varmuuskopiointiin:





- Hinta:** Vaikka hinta on vaatimaton (noin 25 euroa), se on silti korkeampi kuin paperiarkin hinta.





- Riippuvuus yleiskäyttöisestä laskentalaitteesta:** seed:n syöttäminen ja hallinta edellyttää tietokonetta tai älypuhelinta, mikä tarkoittaa, että muistikuvasi kulkee koneen läpi, jolla on paljon laajempi hyökkäyspinta kuin wallet-laitteistolla. Tämä voi olla riski, jos kone on vaarassa. Tämän vuoksi en suosittele Seedkeeperin käyttöä wallet-laitteiston seed:n tallentamiseen (paitsi tilattomassa käytössä ilman tietokonetta, kuten SeedSignerin kanssa). wallet-laitteiston tehtävänä on nimenomaan tallentaa seed minimaalisessa, erittäin turvallisessa ympäristössä. Kun seed syötetään manuaalisesti tavallisella tietokoneella, se ei enää rajoitu wallet-laitteistoon: se päätyy myös yleiskäyttöiseen koneeseen, joka on alttiina monille hyökkäysvektoreille. On siis parempi käyttää Seedkeeperiä mieluummin kuumassa kuin kylmässä wallet:ssa (paitsi SeedSigner / tilaton wallet-laitteisto).





- PIN-koodiin liittyvä katoamisriski:** seed:n suora saavuttamattomuus, toisin kuin paperilla oleva varmuuskopio, suojaa todellakin fyysiseltä varkaudelta. Mutta kuten aina, turvallisuus on tasapainoilua varkaus- ja häviämisriskin välillä. Jos varmuuskopiosi vaatii PIN-koodin, tämän koodin menettäminen tekee muistilauseen palauttamisen ja siten bitcoinien käytön mahdottomaksi.



Näiden etujen ja haittojen valossa katson, että Seedkeeperiä voidaan käyttää parhaiten (sen salasanojen hallintatoiminnon lisäksi) toisaalta **ohjelmistosalkkujen** siementen tallentamiseen, koska ne ovat jo puhelimessasi tai tietokoneessasi, tai näytöttömien wallet-laitteistojen, kuten Satochipin, siementen tallentamiseen, ja toisaalta sen käyttämiseen yhdessä tilattomien wallet-laitteistojen, kuten SeedSignerin, kanssa, jolloin se todella pääsee oikeuksiinsa.



Toinen erityisen kiinnostava käyttötapaus Seedkeeperille on mahdollisuus varmuuskopioida salkkujen *Descriptorit* turvallisesti ja luotettavasti.



## 2. Miten saan siemenvartijan?



Seedkeeper voidaan hankkia kahdella tavalla. Voit [ostaa sen suoraan Satochipin virallisesta kaupasta](https://satochip.io/product/seedkeeper/) tai valtuutetulta jälleenmyyjältä. Mutta koska [Seedkeeper-sovellus on avointa lähdekoodia](https://github.com/Toporin/Seedkeeper-Applet), voit myös asentaa sen itse [tyhjälle älykortille](https://satochip.io/product/blank-javacard-for-diy-project/).



Jos haluat käyttää Seedkeeperin varmuuskopiointitoimintoa, sinun on luonnollisesti ostettava kaksi älykorttia.



## 3. Seedkeeper-asiakasohjelman asentaminen



Tässä ohjeessa varmuuskopioimme seed-salkkumme Seedkeeperiin. Ensimmäinen vaihe on asentaa ohjelmisto tietokoneeseen tai älypuhelimeen. Tietokoneessa sinun on [ladattava Satochip-Utilsin uusin versio](https://github.com/Toporin/Satochip-Utils/releases). Mobiililaitteissa Seedkeeper-sovellus on saatavilla [Google Play Storesta](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) sekä [Apple App Storesta](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Siemenenvartijan alustaminen



Käynnistä sovellus ja napsauta "*Click & Scan*"-painiketta.



![Image](assets/fr/003.webp)



Sinulta kysytään PIN-koodia siementarkkailijaa varten. Koska kyseessä on uusi kortti, PIN-koodia ei ole vielä määritelty. Syötä mikä tahansa koodi ohittaaksesi tämän vaiheen ja napsauta sitten "*Seuraava*".



![Image](assets/fr/004.webp)



Aseta kortti sitten älypuhelimen takaosaan. Sovellus havaitsee, että Seedkeeperiä ei ole vielä alustettu, ja pyytää sinua asettamaan älykortin PIN-koodin, jonka pituus on 4-16 merkkiä. Optimaalisen turvallisuuden takaamiseksi valitse vahva salasana, joka on mahdollisimman pitkä, satunnainen ja koostuu useista eri merkeistä. Tämä PIN-koodi on ainoa este palautuslauseen fyysiselle käytölle.



**Muista myös tallentaa tämä PIN-koodi nyt** esimerkiksi salasanahallintaan tai erilliselle fyysiselle tietovälineelle. Jälkimmäisessä tapauksessa älä koskaan säilytä PIN-koodin sisältävää tietovälinettä samassa paikassa kuin Seedkeeperiäsi, sillä muuten tämä suojaus on hyödytön. Luotettava varmuuskopio on tärkeää: ilman PIN-koodia et voi palauttaa Seedkeeperiin tallennettuja salaisuuksia.



![Image](assets/fr/005.webp)



Vahvista PIN-koodi toisen kerran.



![Image](assets/fr/006.webp)



Seedkeeper on nyt alustettu. Voit avata sen lukituksen syöttämällä juuri asettamasi PIN-koodin.



![Image](assets/fr/007.webp)



Pääset nyt älykortin hallintasivulle.



![Image](assets/fr/008.webp)



## 5. Rekisteröi seed Seedkeeperiin



Kun siemenvartijasi on avattu, napsauta "*+*"-painiketta.



![Image](assets/fr/009.webp)



Valitse "Tuo salaisuus*". "*Luo salaisuus*" -vaihtoehdon avulla voit luoda uuden muistisäännön suoraan sovelluksesta.



![Image](assets/fr/010.webp)



Meidän tapauksessamme haluamme tallentaa seed:n salkkuun. Napsauta "*Mnemonic*".



![Image](assets/fr/011.webp)



Määritä tälle salaisuudelle "*Label*", jotta se voidaan helposti tunnistaa, jos tallennat useita tietoja Seedkeeperiin.



![Image](assets/fr/012.webp)



Kirjoita sitten palautuslausekkeesi sille varattuun kenttään. Voit halutessasi lisätä myös passphrase BIP39:n tai *Descriptors*. Napsauta sitten "Tuo*".



![Image](assets/fr/013.webp)



*Tässä kuvassa näkyvä muistilista on kuvitteellinen eikä se kuulu kenellekään. Se on vain esimerkki. Älä koskaan paljasta omaa muistisääntöäsi kenellekään, tai bitcoinisi varastetaan



Aseta Seedkeeper älypuhelimen takaosaan.



![Image](assets/fr/014.webp)



seed on rekisteröity.



![Image](assets/fr/015.webp)



## 6. Pääset seed:een Seedkeeperissä



Jos haluat tarkistaa muistisääntösi, ota Seedkeeper ja napsauta "*Click & Scan*"-painiketta.



![Image](assets/fr/016.webp)



Syötä PIN-koodi ja paina sitten "*Seuraava*".



![Image](assets/fr/017.webp)



Aseta Seedkeeper älypuhelimen takaosaan.



![Image](assets/fr/018.webp)



Tämä vie sinut luetteloon kaikista rekisteröidyistä salaisuuksistasi. Tässä esimerkissä haluan näyttää salkkuni "*Blockstream App*" seed:n, joten napsautan sitä.



![Image](assets/fr/019.webp)



Paina "*Paljasta*"-painiketta.



![Image](assets/fr/020.webp)



Skannaa Seedkeeper uudelleen.



![Image](assets/fr/021.webp)



Aiemmin tallentamasi muistilause näkyy nyt näytöllä.



![Image](assets/fr/022.webp)



## 7. Varmuuskopiointi Seedkeeperistä



Teemme nyt varmuuskopion Seedkeeperistä toiselle Seedkeeperille, jotta meillä on kaksi kopiota. Tämä redundanssi voi olla osa bitcoinien turvaamiseen tähtäävää strategiaa: esimerkiksi varastoimalla fraasi kahdessa eri paikassa fyysisten riskien rajoittamiseksi tai antamalla kopion luotettavan sukulaisen haltuun osana perintösuunnitelmaa.



Tätä varten ota mukaan toinen siementenvartija (muista tunnistaa jompikumpi merkillä sekaannusten välttämiseksi). Aloita sen alustaminen tämän ohjeen vaiheessa 4 kuvatulla tavalla. Valitse jälleen kerran vahva salasana. Strategiastasi riippuen voit valita eri salasanan tai säilyttää saman.



![Image](assets/fr/023.webp)



Avaa sovellus, napsauta "*Click & Scan*", syötä Seedkeeper n°1 (lähde) salasana ja skannaa se sitten.



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



Siinä kaikki! Nyt tiedät, miten Seedkeeperiä voidaan käyttää Bitcoin wallet:n muistilausekkeen tallentamiseen. Tulevassa opetusohjelmassa tarkastelemme, miten Seedkeeperiä voi käyttää salasanojen tallentamiseen. Kutsun sinut myös tutustumaan sen yhdistettyyn käyttöön SeedSignerin kanssa:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Tässä oppaassa olemme maininneet Bitcoin-salkun ***Descriptors*** useaan otteeseen. Etkö tiedä, mitä ne ovat? Siinä tapauksessa suosittelen, että osallistut ilmaiselle CYP 201 -koulutuskurssillemme, jossa käsitellään perusteellisesti kaikkia HD-salkkujen toimintaan liittyviä mekanismeja!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f