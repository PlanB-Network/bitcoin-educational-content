---
name: Misty Breez
description: Keulaton Lightning Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez on Breezin kehittämä Lightning itsekantava Wallet, joka perustuu Breezin ohjelmistokehityssarjaan ja BlockStreamin kehittämään **Liquid**-verkkoon.


Se tarjoaa täysin uudenlaisen lähestymistavan toimintaan ilman Lightning-solmua: mahdollinen **PELINMUUTTAJA** Bitcoin-verkkojen välisissä siirroissa.


Tässä opetusohjelmassa kuvaamme, miten tämä salkku toimii, ja annamme sinulle täydellisen yleiskatsauksen.



## Miten Misty Breez toimii?



Misty Breez on toteutus, jossa ei ole Lightning-solmua backendinä. Se on kehitetty Breez SDK:n ja Liquid:n pohjalta.



Liquid on Bitcoin-verkon rinnakkainen Layer-verkko, joka tarjoaa merkittäviä parannuksia nopeuteen ja transaktiokustannuksiin. Tämän Layer:n ansiosta Misty Breez voi luopua Lightning-solmusta ja käyttää sen sijaan kolmannen osapuolen Exchange-palveluja, kuten **Boltzia**, varmistaakseen yhteentoimivuuden Liquid Network:n ja Lightning Network:n välillä. Älä kiirehdi, palaamme vielä tähän.



Aloitetaan seikkailumme nyt Misty Breez Wallet:llä.



## Aloittaminen Misty Breezin kanssa



Misty Breez -mobiilisovellus on saatavilla virallisilla latausalustoilla, kuten Google Play Storessa (Androidissa) ja Apple Storessa (iOS:ssä). Voit myös ohjautua oikeaan sovellukseen viralliselta [Misty Breez] verkkosivustolta (https://breez.technology/misty/).



⚠️ Varmista, ettet sekoita Misty Breeziä Breez Wallet:een.



⚠️ **TÄRKEÄÄ**: On tärkeää ladata sovellus virallisilta alustoilta sen aitouden varmistamiseksi, jotta bitcoinit ovat turvassa.



![download-misty-breez](assets/fr/01.webp)



Tässä ohjeessa aloitamme Android-laitteesta. Tästä huolimatta kaikki tässä osiossa kuvatut vaiheet ja erityispiirteet soveltuvat myös iOS-laitteeseen.



Asennuksen jälkeen Misty Breez antaa sinulle mahdollisuuden luoda uuden Wallet:n tai palauttaa vanhan Lightning Wallet:n, jonka palautussanat sinulla on.


Tässä ohjeessa päätämme luoda uuden portfolion.



⚠️Misty Breez on tällä hetkellä kehitysvaiheessa, joten suosittelemme aloittamaan kohtuullisilla määrillä.



![create-wallet](assets/fr/02.webp)


### Tallenna toipumissanat :


Yksi ensimmäisistä asioista, jotka sinun pitäisi tehdä uutta portfoliota luodessasi, on varmuuskopioida 12 palautussanaa.


Seuraavassa on muutamia vinkkejä varmuuskopiointilauseen varmuuskopiointiin.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Jos haluat varmuuskopioida lauseita, valitse **Edellytykset > Suojaus** -valikko ja sitten **Tarkista varmuuskopiointilauseesi** -vaihtoehto.



![backup](assets/fr/03.webp)


Lisäturvaksi voit myös **luoda PIN-koodin**, jolla voit todentaa Wallet:n käytön.




Löydä paikallinen valuuttasi Misty Breezin hyväksymien valuuttojen joukosta. Määritä valuutta **Edellytykset > Fiat-valuutat** -valikosta ja valitse sitten haluamasi valuutta tai valuutat.



![devises](assets/fr/04.webp)



### Ensimmäisten liiketoimien tekeminen


Jos olet jo tutustunut Breezin valikoimaan, Misty Breezin intuitiivinen Interface ei lainkaan lannista sinua.



Napsauta Interface:n **Tase**-valikossa **Vastaanotto**-vaihtoehtoa luodaksesi laskuja, joilla saat bitcoinit Wallet:ään.



⚠️ Misty Breez pyytää sinua aktivoimaan sovelluksen ilmoitukset puhelimesi asetuksissa, jotta saat oikeuden Lightning Address:een.



Misty Breezin avulla voit :




- Vastaanota bitcoineja Lightning Network:llä **100 satoshista** aina **25 000 000 satoshiin** asti.
- Vastaanota bitcoineja Bitcoin-pääverkossa **25 000 satoshista**.



![transactions](assets/fr/05.webp)



Tästä alkaa Misty Breezin taika.


Toisin kuin Breez Wallet, joka tarjoaa sinulle Lightning-solmun ja pyytää sinua kattamaan maksukanavien avaamisesta ja sulkemisesta aiheutuvat kustannukset itse, Misty Breez ei pyydä sinua tekemään mitään. Kuten aiemmin mainittiin, Misty Breez ei edes toimi Lightning-solmun perusteella.



Katsotaanpa tarkemmin kulissien taakse.



Todellisuudessa omistat Liquid-salkun, joka liittyy Misty Breez -salkkuun. Loogisesti käsittelet L-BTC:tä (Liquid Bitcoin) kiinteillä kursseilla, jotka liittyvät kolmannen osapuolen submarine satoshis -konversiopalveluihin, jotka mahdollistavat yhteistoiminnan Lightning Network:n kanssa.



Kun vastaanotat maksun Misty Breez Wallet -järjestelmään, lähettäjä lähettää sinulle satosheja, jotka kulkevat Boltzin kaltaisen muuntopalvelun kautta (jota Misty Breez tällä hetkellä käyttää), jotta lähetetyt satosheet voidaan muuntaa L-BTC:ksi, joka vastaanotetaan Misty Breez Wallet -järjestelmään (siihen liittyvä Liquid Wallet).


Seuraavassa on yksinkertaistettu kaavio kulissien takana tapahtuvasta prosessista.



![lnswap-in](assets/fr/06.webp)



Napsauta Interface **Tase**-valikossa, napsauta **Lähettää**-vaihtoehtoa maksaaksesi Lightning Invoice.


Aseta Lightning Invoice, vastaanottajan Lightning Address tai skannaa yksinkertaisesti Invoice:ssä oleva QR-koodi maksaaksesi.



![send-bitcoins](assets/fr/07.webp)



Kulissien takana annat Misty Breez Wallet:een liitetyn Liquid Wallet:n muuntaa L-BTC:tä vastaavan summan Satoshiksi Boltzin kautta ja siirrät nämä Satoshit vastaanottajan Lightning Wallet:een (joka on Lightning Network:ssä).



![send-bitcoin-bts](assets/fr/08.webp)



Tämän Misty Breezin infrastruktuurin ominaisuuden ansiosta käyttäjät voivat suorittaa maksutapahtumia silloinkin, kun Misty Breez on offline-tilassa.



Kokeneemmille on myös valikko **Edellytykset > Kehittäjät**, josta saat hieman yksityiskohtaisempaa tietoa :




- Breez Software Development Kitin versio.
- Misty Breez Wallet:n julkinen avain.
- Lainanottaja, ensisijaisesta julkisesta avaimesta johdettu yksilöllinen tunniste.
- Salkun saldo.
- Vihje Liquid, pienten L-BTC-määrien lähettämiseen.
- Bitcoin-kärki pienten Bitcoin-määrien lähettämiseen.



Voit myös suorittaa tiettyjä toimintoja, kuten synkronoida Liquid Network:n kanssa, varmuuskopioida avaimet, jakaa toimintalokin ja valita Liquid Network:n uudelleenkuvauksen.



![dev-mode](assets/fr/09.webp)


Onnittelut! Sinulla on nyt hyvä käsitys Misty Breez -portfoliosta ja sen osuudesta Bitcoin-verkon välisiin liiketoimiin. Jos tämä opetusohjelma oli mielestäsi hyödyllinen, anna meille Green-peukalo. Olisimme iloisia kuullessamme sinusta.



Jos haluat mennä pidemmälle, suosittelen, että tutustut myös Aqua Wallet -oppaaseemme, joka toimii samalla tavalla kuin Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125