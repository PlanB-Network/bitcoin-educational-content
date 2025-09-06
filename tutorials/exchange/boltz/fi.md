---
name: Boltz
description: Vaihda eri Bitcoin-kerrosten välillä säilyttäen samalla hallinta.
---


![cover](assets/cover.webp)



Vuonna 2009 tapahtuneen käyttöönoton jälkeen Bitcoin:n vertaisverkkoon perustuva sähköinen käteisrahajärjestelmä on kasvanut räjähdysmäisesti, ja se on kehittänyt ratkaisuja, joiden ansiosta se on nykyään järjestelmä, jota voimme käyttää välittömästi jokapäiväisissä toimissamme, erityisesti Lightning Network:n kautta.



Bitcoin:n protokollakerrosten välillä oli kuitenkin edelleen suuri ongelma: nestemäinen yhteentoimivuus. Bitcoin:n täyden potentiaalin hyödyntämiseksi oli välttämätöntä löytää ratkaisu, joka mahdollistaisi transaktiot protokollan eri kerrosten välillä. Tämä tarve johti vuonna 2019 Boltziin, joka on silta, joka yhdistää useita Bitcoin-kerroksia.



## Mikä on Boltz?



[Boltz] (https://boltz.Exchange) on ei-hallinnollinen alusta, joka sopii kaikille, jotka haluavat käydä kauppaa Bitcoin-protokollan eri kerrosten välillä:




- on chain**: Bitcoin:n pääketju, jossa transaktiot vahvistetaan keskimäärin 10 minuutin välein, transaktiomaksut ovat usein korkeita, mikä ei välttämättä vastaa käyttäjien tarpeita ;
- Lightning Network**: Bitcoin:n päällekkäiskäyttö mahdollistaa pikamaksut alhaisilla maksuilla, jolloin Bitcoin:ää voidaan käyttää päivittäisiin maksuihin;
- Liquid Network**: Blockstreamin luoma Bitcoin:n päällys, joka mahdollistaa nopean, Confidential Transactions:n ja muiden Bitcoin-pohjaisten rahoitusvälineiden käytön;
- RootStock**: Bitcoin-protokollaan perustuvien älykkäiden sopimusten kehittämiseen tarkoitettu ratkaisu.



![layers](assets/fr/01.webp)



Näiden eri kerrosten välinen yhteentoimivuus on erittäin tärkeää, sillä se antaa käyttäjille joustavuutta, jota he tarvitsevat voidakseen hyödyntää kaikkea, mitä Bitcoin-ekosysteemillä on tarjota.



Boltz käyttää atomivaihtoja. Tämän tekniikan avulla bitcoineja voidaan vaihtaa kahden kerroksen välillä (esim. BTC onchain Exchange:ssä BTC:hen Lightningissa) suoraan kahden osapuolen välillä ilman luottamusta ja ilman välittäjää. Näitä vaihtoja kutsutaan "atomisiksi", koska ne voivat tuottaa vain kaksi tulosta:




- Joko Exchange onnistuu ja kaksi osallistujaa on tosiasiallisesti vaihtanut BTC:nsä;
- Joko Exchange epäonnistuu, ja molemmat osallistujat lähtevät alkuperäiset BTC:t mukanaan.



Tällä tavoin säilytät bitcoinisi pysyvästi itse, eikä Exchange perustu luottamukseen vastapuolta kohtaan: Exchange joko onnistuu tai epäonnistuu, mutta kumpikaan osapuoli ei voi varastaa toisen osapuolen varoja.



Atominen Exchange toimii älykkäiden sopimusten [HTLC](https://planb.network/resources/glossary/htlc) kanssa (*Hashed Timelock Contract*). Tämäntyyppisessä Contract:ssä summa "lukitaan" kaksisuuntaiseen kanavaan ja otetaan käyttöön aikarajoitus, jolloin jos transaktiota ei saada päätökseen tietyn ajan kuluessa, saldo palautuu tallettajalle. Tätä mekanismia käytetään Boltz-alustalla.



## Ensimmäiset keskustelut Boltzin kanssa



Boltz on tallentamaton verkkoalusta, joka ei vaadi sinulta henkilökohtaisia tietoja. Boltzilla on minimalistinen, sujuva Interface, jonka avulla voit aloittaa kaupankäynnin alle minuutissa.



![boltz](assets/fr/02.webp)



Kun olet päässyt alustalle, voit luoda atomisia vaihtoja Bitcoin-ekosysteemin eri kerrosten välillä.



![home](assets/fr/03.webp)



Näet vähimmäis- ja enimmäismäärän satosheja (pienin Bitcoin:n yksikkö), joilla voit käydä kauppaa Boltzin kautta, mukaan lukien verkkomaksut ja Boltzin perimä prosenttiosuus, joka on 0,1-0,5 %.



![fees](assets/fr/04.webp)



Valitse sitten Layer, josta haluat tehdä atomisen Exchange:n, ja valitse Layer, josta haluat vastaanottaa bitcoinit.



![couches](assets/fr/05.webp)



Tässä opetusohjelmassa keskitymme atomaattiseen Exchange:aan pääkohdasta Layer:stä Lightning Network:ään.



Voit määrittää tukiaseman vaihtoja varten valitsemalla vaihtoehdoista :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Kun olet saanut peruskonfiguraatiot valmiiksi, lisää atomisen Exchange:n määrä ja luo sitten Lightning Invoice vastaavalle määrälle tai yksinkertaisesti lisää LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Tarkista varmuuden vuoksi atomisen Exchange:n parametrit, jotta voit viedä Exchange:een liitetyt varmuuskopioavaimet.



Lataa varmuuskopioavain **asetukset** -kuvakkeesta ja tallenna tiedosto asianmukaisesti.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Tämä tiedosto sisältää atomipörssiisi liittyvän salkun 12 avainsanaa.



Napsauta sitten **Luo atomic Exchange** -painiketta ja jatka ilmoitetun summan maksamista.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Kun maksusi on suoritettu ja vahvistettu, saat automaattisesti vastaavan summan Lightning Wallet:een.



Etsi **Palautus**-valikosta atomisesta Exchange-historiastasi se Exchange, josta haluat saada palautuksen. Voit myös tuoda toiseen laitteeseen tekemiesi vaihtojen historian esimerkiksi näihin vaihtoihin liittyvän varmuuskopioavaintiedoston avulla.



![refund](assets/fr/11.webp)



Valikossa **Historia** voit ladata tarkemman historian pelastusavaimeen liittyvistä vaihdoista napsauttamalla **Tallennus**-painiketta.



![backup](assets/fr/12.webp)



⚠️ Älä myöskään paljasta tätä tiedostoa, sillä se sisältää kaikki tapahtumiin liittyvät tiedot ja näihin tapahtumiin liittyvän varmuuskopioavaimen.



Boltz tarjoaa sinulle korkean tason luottamuksellisuutta, koska se on saatavilla Tor-verkon .onion-linkin kautta. Tee atomivaihdoista täysin anonyymejä valitsemalla **Onion**-valikko, kun olet aktivoinut Tor-selauksen selaimessasi.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nyt tunnet jo Boltzin, ainutlaatuisen Exchange-alustan, joka mahdollistaa yhteentoimivuuden Bitcoin-ekosysteemin eri kerrosten välillä.