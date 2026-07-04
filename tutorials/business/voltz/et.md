---
name: Voltz
description: Kõik-ühes Lightning wallet teie ettevõtte jaoks.
---

![cover](assets/cover.webp)



Voltzi platvormi idee pärineb ühelt bitcoin'i kasutajarühmalt, kes soovis pakkuda oma bitcoin wallet teenust. Tulemuseks oli täielik infrastruktuur bitcoinide vastuvõtmiseks jaemüügis. Selles õpetuses võtame teid kaasa Voltz'i ja platvormi bitcoini integreerimise võimaluste tutvustamisel.



## Voltziga alustamine



Lisaks sellele, et Voltz on eestkostetav Lightning wallet, mis võimaldab teil iga päev saata, vastu võtta ja maksta, on Voltz täielik platvorm, mis pakub arvukaid laiendusi bitcoini integreerimiseks müügipunktina või turuplatsina teie ettevõttesse.



Mine [Voltz] platvormile (https://www.lnvoltz.xyz/en) ja loo konto, klõpsates nupule "Proovi nüüd".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Oluline on määrata tugev tähtnumbriline parool, et suurendada oma võimalusi brute-force rünnakute vastu, ja kontrollida, et olete tõepoolest Voltzi ametlikul veebisaidil, et täita oma sisselogimisandmed, et kaitsta end andmepüügi eest.



Voltzi kasutajaliides on väga sarnane LnBitsi platvormiga.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz on tegelikult ehitatud LnBits serverile; vaadake meie õpetust, et teada saada, kuidas oma LnBits serverid paigaldada ja oma lahendusi neile ehitada.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Platvorm võimaldab teil tõhusalt hallata mitut portfelli. Vaikimisi on teil registreerimisel automaatselt Lightning portfell. Siiski saate lisada ka teisi portfelle.



![wallets](assets/fr/03.webp)



### Kaasaskantavus



Voltz ei piirdu ainult veebiliidesega: jaotises **Mobile Access** saate ühendada oma aktiivse Voltz wallet rakendustega, nagu Zeus või Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Selleks tuleb platvormile paigaldada ja aktiveerida **LndHub** laiendus.



![lndhub](assets/fr/04.webp)



Valige oma aktiivne Voltzi portfell ja skaneerige vastav QR-kood, sõltuvalt sellest, milliseid õigusi soovite anda.




- Arve QR-kood võimaldab teil ainult lugeda oma portfelli ajalugu ja generate uusi arveid.
- Administraatori QR-kood võimaldab teil vaadata ajalugu, generate arveid ja ka tasuda välkarvete eest.



![qrs](assets/fr/05.webp)



Selles õpetuses ühendame meie Voltz wallet Blue Wallet rakendusega.



![connect](assets/fr/06.webp)



Kui meie portfell on ühendatud, sünkroonitakse kõik teostatud tegevused Blue Wallet ja Voltzi vahel. Näiteks, kui te generate arve Blue Wallet-s, siis on teil ka ajalugu Voltzis.



![sync](assets/fr/07.webp)



Jaotises **Portfelli konfiguratsioon** leiate minimaalsed parameetrid, nagu portfelli nime kohandamine ja valuuta, milles soovite makseid saada.



![config](assets/fr/08.webp)



### Laiendused



Voltzi platvormi üks eripära on selle modulaarsus, mis võimaldab teil aktiveerida vajalikud laiendused. Laienduste loetelu leiate menüüst **Laiendused**.



![extensions](assets/fr/09.webp)



Nende laienduste hulgas on TPoS, müügipunktiterminal, mida saate kasutada inventari pidamiseks ja klientide maksete kogumiseks.



![tpos](assets/fr/10.webp)



Müügipunkti terminalist saate :




- Hankige veebileht, mida saate jagada oma klientide ja partneritega;
- Haldage toodete varusid;
- Lightning-arvete koostamine;
- Sularahamaksed Bolt kaartide kaudu.



Laiendus on saadaval nii tasuta kui ka tasulise versioonina, mis pakub lisafunktsioone. Kassaterminali loomiseks klõpsake laienduse logo all oleval nupul **Avatakse** ja seejärel klõpsake nupul **Uue kassaterminal**.



![new_tpos](assets/fr/11.webp)



Määrake oma müügipunkti nimi, seejärel ühendage Voltz wallet oma terminaliga maksete kogumiseks. Võite aktiveerida jootraha, märgistades ruutu **Activate gratuities**. Aktiveerige ka arve printimise võimalus, kui soovite klientidele kviitungeid väljastada (see funktsioon on veel arendamisel, seega võib esineda tõrkeid).



Müügiterminal sisaldab ka maksude konfigureerimist, kui soovite kohaldada oma riigi makse otse oma toodetele.



![tpos](assets/fr/12.webp)



Kui teie kassaterminal on loodud, saate lisada eelkonfigureeritud tooteid ja teenuseid, et tagada sujuv makse- ja raamatupidamiskogemus teile ja teie klientidele.



![product](assets/fr/13.webp)



Looge oma tooted, määrates nende nime, lisades pildi ja määrates müügihinna.  Lihtsamaks jälgimiseks saate oma tooted kategoriseerida. Saate kohaldada makse otse konkreetsele tootele. Kui tootele ei ole maksu kohaldatud, kohaldatakse müügipunkti loomise etapis konfigureeritud maks automaatselt.



![products](assets/fr/14.webp)



Saate automaatselt importida oma tootenimekirja JSON-vormingust, klõpsates nupule **Import/Eksport**.



![exports](assets/fr/15.webp)



Juurdepääs kassaplatvormile toimub lingi kaudu, klõpsates ikoonil **Uus vahekaart**, või jagage oma kassaplatvormi QR-koodi kaudu oma klientidega, klõpsates ikoonil **QR-kood**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Teie kliendid saavad selle liidese kaudu tutvuda teie kataloogiga ja teha makseid.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



Kättesaadavate laienduste grupist leiate ka selliseid vahendeid nagu **Invoice** ja **Payment Link** laiendused, mis võimaldavad teil generate arveid koos konkreetsete toodetega koguda üksikuid makseid ilma POS-terminali kaudu käimata.



## Jälgige oma makseid



Menüüs **Maksed** annab Voltz teile ülevaate teie erinevatesse portfellidesse tehtud maksetest.


Saate jälgida oma makseid :




- Staatus.
- Märgistus: näiteks **TPOS** müügikoha maksete jaoks ja **lnhub** mobiilse ühenduse kaudu Zeuse ja Blue Wallet rahakottides.
- Kollektsiooni portfell.
- Sissetulevate ja väljaminevate maksete kogusumma.
- Täpselt määratletud ajavahemik.



![payments](assets/fr/22.webp)



## Rohkem võimalusi



Voltz on ka infrastruktuur, millele saab ehitada oma lahendusi. Jaotises **Laiendused** leiate juhendi, kuidas Voltzi ja LnBitsi ökosüsteemi raames oma laiendusi arendada.



![build](assets/fr/23.webp)



Juhul, kui soovite arendada lahendusi väljaspool ökosüsteemi, kuid siiski kasutada nende infrastruktuuri, leiate jaotisest **URL of node** API võtmed ja dokumentatsiooni teabe koos näitega, mida saate nende andmetega teha.



Võite luua Lightning-arveid oma rakendustest, kasutades oma Voltz wallet, tasuda Lightning-arveid, dekodeerida ja kontrollida arveid.



![keys](assets/fr/24.webp)



Nüüd on sul Voltzist hea ülevaade. Kui teile meeldis see õpetus, siis oleme kindlad, et saate meie kursuse abil rohkem teada parimatest meetoditest ja vahenditest, kuidas integreerida bitcoin oma äri: Bitcoin ettevõtetele.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a