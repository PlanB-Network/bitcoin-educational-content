---
name: Boltz
description: Vahetage erinevate Bitcoin kihtide vahel, säilitades samal ajal kontrolli.
---


![cover](assets/cover.webp)



Alates selle kasutuselevõtust 2009. aastal on Bitcoin vastastikune elektrooniline sularahasüsteem eksponentsiaalselt kasvanud, andes elu lahendustele, mis võimaldavad tänapäeval olla süsteem, mida me saame koheselt kasutada oma igapäevastes toimingutes, eelkõige Lightning Network kaudu.



Bitcoin protokolli kihtide vahel jäi siiski üks suur probleem: sujuv koostalitlusvõime. Bitcoin potentsiaali täielikuks ärakasutamiseks oli hädavajalik leida lahendus, mis võimaldaks tehinguid protokolli eri kihtide vahel. Selle vajaduse tõttu loodi 2019. aastal Boltz, sild, mis ühendab mitu Bitcoin kihti.



## Mis on Boltz?



[Boltz] (https://boltz.Exchange) on mittekaitstav platvorm, mis on ideaalne kõigile, kes soovivad teha tehinguid Bitcoin protokolli eri kihtide vahel:




- on chain**: Bitcoin peamine kett, kus tehinguid kinnitatakse keskmiselt iga 10 minuti järel, tehingutasud on sageli kõrged, mis ei pruugi vastata kasutajate vajadustele ;
- Lightning Network**: Bitcoin pealekandmine madala tasu eest tehtavateks välkmakseteks, mis võimaldab Bitcoin kasutada igapäevasteks makseteks;
- Liquid Network**: Blockstream'i loodud Bitcoin kattekiht, mis võimaldab kiire, Confidential Transactions ja muude Bitcoin-põhiste finantsinstrumentide kasutamist;
- RootStock**: Bitcoin protokollil põhinev lahendus arukate lepingute arendamiseks.



![layers](assets/fr/01.webp)



Koostalitlusvõime nende eri kihtide vahel on väga oluline, sest see annab kasutajatele vajaliku paindlikkuse, et nad saaksid täielikult ära kasutada kõike, mida Bitcoin ökosüsteemil on pakkuda.



Boltz kasutab aatomivahetusi. See tehnoloogia võimaldab bitcoinide vahetamist 2 kihi vahel (nt BTC onchain Exchange-s BTC vastu Lightningis) otse kahe osapoole vahel, ilma usalduse ja vahendaja vajaduseta. Neid vahetusi nimetatakse "aatomiks", sest need võivad anda ainult kaks tulemust:




- Kas Exchange on edukas ja kaks osalejat on tegelikult vahetanud oma BTC-d;
- Kas Exchange ebaõnnestub ja mõlemad osalejad lahkuvad oma algse BTC-ga.



Sel viisil säilitate oma bitcoinide alalise isevalitsuse ja Exchange ei põhine usaldusel vastaspoole vastu: kas Exchange õnnestub või ebaõnnestub, kuid kumbki osapool ei saa teise osapoole raha varastada.



Aatomiline Exchange töötab nutikate lepingutega [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). Seda tüüpi Contract puhul "lukustatakse" summa kahesuunalises kanalis ja kehtestatakse ajaline piirang, nii et kui tehing ei ole teatud aja jooksul lõpule viidud, läheb saldo hoiustajale tagasi. Sellist mehhanismi kasutab Boltzi platvorm.



## Teie esimesed vahetused Boltziga



Boltz on mittedepositoorne veebiplatvorm, mis ei nõua sinult isiklikke andmeid. Boltzil on minimalistlik, sujuv Interface, mis võimaldab teil alustada kauplemist vähem kui minutiga.



![boltz](assets/fr/02.webp)



Kui olete platvormil, saate luua aatomivahetusi Bitcoin ökosüsteemi eri kihtide vahel.



![home](assets/fr/03.webp)



Näete minimaalset ja maksimaalset arvu satoshisid (väikseim Bitcoin ühik), millega saate Boltzi kaudu kaubelda, sealhulgas võrgutasud ja Boltzi poolt kehtestatud protsent vahemikus 0,1% kuni 0,5%.



![fees](assets/fr/04.webp)



Seejärel valige Layer, millest soovite teha aatomi Exchange, ja valige Layer, millele soovite bitcoine saada.



![couches](assets/fr/05.webp)



Selles õpetuses keskendume aatomi Exchange peast Layer kuni Lightning Network.



Saate konfigureerida baasüksuse oma vahetuste jaoks, valides järgmiste valikute vahel :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Kui olete oma põhikonfiguratsioonid lõpetanud, sisestage oma aatomi Exchange summa, seejärel looge Lightning Invoice samaväärse summa jaoks või sisestage lihtsalt oma LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Kindluse mõttes kontrollige oma aatomi Exchange parameetreid, et eksportida oma Exchange-ga seotud varuklahvid.



Laadige **Settings** ikoonil alla varukoopia võti ja salvestage fail nõuetekohaselt.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



See fail sisaldab teie aatomivahetusega seotud portfelli 12 märksõna.



Seejärel klõpsake nupule **Loo aatomi Exchange** ja jätkake märgitud summa maksmist.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Kui teie makse on tehtud ja kinnitatud, saate automaatselt vastavat summat oma Lightning Wallet-le.



Leidke menüüst **Tagastamine** oma aatomi Exchange ajalugu, et tuvastada Exchange, mille eest soovite raha tagasi saada. Samuti saate importida teises seadmes tehtud vahetuste ajalugu, kasutades näiteks nende vahetustega seotud varukoopia võtmefaili.



![refund](assets/fr/11.webp)



Menüüs **History** saate laadida alla oma päästevõtmega seotud vahetuste üksikasjalikuma ajaloo, klõpsates nupule **Backup**.



![backup](assets/fr/12.webp)



⚠️ Palun ärge avaldage ka seda faili, sest see sisaldab kogu teie tehingutega seotud teavet ja nende tehingutega seotud varundusvõtit.



Boltz pakub teile kõrgetasemelist konfidentsiaalsust tänu juurdepääsule Tor-võrgustiku "onion" lingi kaudu. Tehke aatomivahetused täiesti anonüümseks, valides **Onion** menüü, pärast Tori sirvimise aktiveerimist teie brauseris.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nüüdseks olete juba tuttav Boltziga, ainulaadse Exchange platvormiga, mis võimaldab Bitcoin ökosüsteemi erinevate kihtide koostalitlusvõimet.