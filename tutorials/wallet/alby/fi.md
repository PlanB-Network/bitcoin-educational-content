---
name: Alby

description: Selainlaajennus Bitcoin:lle ja Lightning Network:lle
---

![cover](assets/cover.webp)




Maksujen tekeminen yhä helpommaksi bitcoinilla on haaste, jonka monet alan yritykset kohtaavat. Alby erottuu joukosta Alby wallet-laajennuksellaan selaimille. Tämän laajennuksen tarkoituksena on luoda joustava kehys, joka tunnistaa osoitteet automaattisesti ja mahdollistaa kitkattomien bitcoin-maksujen tekemisen. Tässä opetusohjelmassa tutustumme Alby-laajennukseen ja testaamme, miten se helpottaa maksamista selaimesta.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby-laajennus



Alby-laajennus on työkalu, jonka avulla verkkoselaimesi voi toimia helposti ja turvallisesti Bitcoin-verkon ja sen Lightning Network-kerroksen kanssa. Sille on ominaista kolme näkökohtaa:




- Lightning Network wallet: Yhdistä Alby-solmusi tai -tilisi lähettääksesi ja vastaanottaaksesi bitcoineja nopeasti ja edullisesti Lightning Network-kerroksen kautta.
- Sujuvat maksut verkon kautta: Se poistaa tarpeen skannata QR-koodeja tai siirtyä sovellusten välillä Bitcoin-maksuja varten Lightningia tukevilla verkkosivustoilla. Se mahdollistaa sujuvat maksutapahtumat yhdellä napsautuksella tai ilman vahvistusta, jos olet asettanut budjetin.
- Nostr:n johtaja: Laajennus hallinnoi Nostr-avaimiasi, mikä helpottaa yhteyden muodostamista ja vuorovaikutusta Nostr-sovellusten kanssa ja toimii turvallisena allekirjoittajana paljastamatta yksityistä avaintasi jokaiselle alustalle.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Yhdistä laajennukseen



Tässä ohjeessa käytämme Alby-laajennusta Firefox-selaimessa Ubuntu-käyttöjärjestelmässä. Se on kuitenkin saatavilla myös Windowsissa ja Chrome-selaimen kaltaisissa selaimissa.



Voit lisätä Alby-laajennuksen selaimeesi [Firefox]-laajennuskaupasta (https://addons.mozilla.org/fr/firefox/addon/alby/) tai [Chrome]-laajennuskaupasta (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ On tärkeää tarkistaa, että laajennuksen tekijä on todellakin virallinen Alby-tili, jotta vältytään kaikenlaiselta piratismilta tai bitcoinien varastamiselta.



Lisää laajennus selaimeesi napsauttamalla oikealla olevaa painiketta.


Myönnä tarvittavat oikeudet laajennuksen asentamiseen ja käyttämiseen ja kiinnitä laajennus sitten työkaluriville, jotta se on helppo hakea.



![pin](assets/fr/03.webp)



Sinun on myös määritettävä lukituksen avauskoodi (erittäin tärkeä), joka takaa turvallisen pääsyn Lightning wallet:een selaimesta. Suosittelemme, että asetat vahvan aakkosnumeerisen salasanan.



ℹ️ Tallenna salasana turvalliseen paikkaan, jotta voit käyttää sitä, jos unohdat sen, sillä sitä voidaan muuttaa, mutta sitä ei voi palauttaa.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby osoittaa sopeutumiskykynsä tarjoamalla sinulle kaksi vaihtoehtoa:




- Jatka Alby-tilillä, jos haluat nauttia sovelluksista ja pitää bitcoinisi hallinnassa.
- Kytke oma wallet- tai Lightning-solmusi, jos sinulla on jo laajennuksen tukema solmu.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Tässä oppaassa päätämme jatkaa Alby-tilillä, jotta voimme hyödyntää Alby-ekosysteemin ominaisuuksia.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Kirjaudu Alby-tilillesi tai luo tili, jos sinulla ei vielä ole sellaista.



![signup](assets/fr/05.webp)



## Ensimmäisten maksujen suorittaminen



Kun olet kirjautunut sisään, voit napsauttaa Alby-laajennusta työkalupalkissa päästäksesi salkkuusi.



![buzzin](assets/fr/06.webp)



Kun olet luonut Alby-tilisi, sinun on yhdistettävä se wallet-tiliin, jotta voit käyttää satosheja. Jotta voit yhdistää bitcoin wallet:n Alby-tiliisi, suosittelemme käyttämään Alby Hub-solmua, jonka voit joko perustaa tietokoneellesi tai tilata Alby:n tarjoaman suunnitelman.



![hubplan](assets/fr/13.webp)




Tässä ohjeessa Alby-tiliä tukee koneemme paikallinen asennus.


Jos haluat rakentaa oman Alby-solmun, suosittelemme Alby Hub-opastusta.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Tämän solmun avulla voit luoda itseohjautuvia Lightning-salkkuja ja hallita tehokkaasti Lightning-kanavia, joiden avulla voit lähettää ja vastaanottaa satosheja.



![channels](assets/fr/14.webp)



Avaa vastaanottokanavat, jotka määrittelevät vastaanotettavien satelliittien kokonaismäärän.



![receivechanal](assets/fr/15.webp)



Avaa lähetyskanavat estämällä satoshit bitcoin onchain -osoitteessa. Blokkaamasi satoshit määrittelevät kokonaissatoshien määrän, jonka voit käyttää.



![spend](assets/fr/16.webp)



Voit nyt lähettää ja vastaanottaa satosheja Alby-laajennuksen kautta.



![exchange](assets/fr/08.webp)



Tästä eteenpäin Alby-laajennus pystyy havaitsemaan Lightning-osoitteet ja -laskut, jotka ovat saatavilla vierailemillasi verkkosivuilla, ja ehdottaa, että maksat ne bitcoinilla tai Lightningilla suoraan laajennuksestasi.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Palautusavaimien suojaaminen pääavaimella



Alby-laajennuksen tarjoama pääavain toimii suojaavana päällysnäytönä, jonka avulla voit kommunikoida turvallisesti Bitcoin:n pääverkkokerroksen (Onchain) ja Nostr-järjestelmän kanssa ja aktivoida Lightning-yhteyden Nostr-sovellusten kanssa.



![masterKey](assets/fr/11.webp)



Tämä pääavain on 12 sanaa, jotka ovat samankaltaisia kuin palautuslausekkeesi. Siksi suosittelemme, että säilytät sen turvallisesti, jotta varmistat, että se on käytettävissä milloin tahansa.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Voit nyt kokea kitkattomia Bitcoin- ja Lightning-maksuja Alby-laajennuksen avulla. Jos pidit tästä opetusohjelmasta, suosittelemme Alby Hub-opetusohjelmaamme, jonka avulla voit perustaa oman Alby-solmun ja hallita kaikkia Alby-lompakoitasi sujuvasta ja tehokkaasta käyttöliittymästä.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a