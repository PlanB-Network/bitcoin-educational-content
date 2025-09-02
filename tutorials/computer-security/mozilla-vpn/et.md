---
name: Mozilla VPN
description: Kaitske oma seadmeid ja interneti sirvimise andmeid.
---
![cover](assets/cover.webp)



Digitaalsel andmekogumise ajastul on privaatsus internetis muutunud meie, internetikasutajate, jaoks oluliseks küsimuseks. Reklaami jälgimise, avalike võrkude kaudu toimuva häkkimise ohu ja geograafiliste piirangute vahel pöördub üha rohkem kasutajaid VPNide (*Virtuaalsed privaatvõrgud*) poole, et oma sirvimist kaitsta. Pakutavate võimaluste hulgast paistab silma Mozilla sihtasutuse teenus, mis on tuntud oma Commitment vaba ja eetilise interneti eest. Selles õpetuses vaatame Mozilla VPN-i, et võtta oma interneti privaatsus kontrolli alla.



## Mis on Mozilla VPN?



***Virtuaalne privaatvõrk*** (VPN) on süsteem, mille abil saab luua otsese ühenduse eri kohtvõrkudega ühendatud kaugarvutite vahel. Teisisõnu on see süsteem, mis isoleerib ja krüpteerib teie andmevahetuse ülejäänud internetiliiklusest. Kui soovite rohkem teada saada VPN-idest, nende kasutusvõimalustest ja kasutamisest tulenevatest eelistest, vaadake kursust SCU 101:



https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47

Sellele põhimõttele tuginedes on [Mozilla VPN] (https://www.mozilla.org/fr/products/vpn/download/) avatud lähtekoodiga VPN-teenus, mille Mozilla Foundation arendas 2020. aastal. See on saadaval aadressil:





- Android,
- iOS,
- Mac,
- Linux,
- Windows,
- ja ka Mozilla Firefoxi brauseri laiendusena.



![download](assets/fr/01.webp)



See on saadaval enam kui 30 riigis ja sellel on üle 500 serveri, mis vastutavad teie IP Address maskeerimise eest, et teid ümber paigutada, tagades samal ajal teie suhtluse konfidentsiaalsuse Internetis. Mozilla VPN-i eristab:





- Kasutamise lihtsus: lihtsustatud, minimalistlik Interface graafika, mis näitab teile põhilisi servereid ja riike, mille hulgast saate valida.





- WireGuard-tehnoloogia: sideprotokoll ja avatud lähtekoodiga tarkvara, mis kasutab krüptograafia tipptasemel krüpteeritud tunnelite loomiseks, pakkudes kerget ja lihtsamini kasutatavat alternatiivi, millel on väiksem koodibaas ning mille puhul on rõhuasetus kiirusel ja turvalisusel.





- Läbipaistev hinnakujundus: umbes 10 eurot kuutasu ja 5 eurot kuus aastatellimuse eest.





- Mitu ühendatud seadet: Ühendage kuni 5 seadet samaaegselt oma Mozilla VPN-kontoga.



## Mozilla VPN-i kasutamise alustamine



Saate alla laadida [Mozilla VPN](https://www.mozilla.org/fr/products/vpn/download/) sõltuvalt teie operatsioonisüsteemist. Selles õpetuses vaatame Mozilla VPN-i Windows operatsioonisüsteemi all.



⚠️ Kuna Mozilla VPN ei ole mõnes riigis saadaval, võib see teade ilmuda, kui laadite Mozilla VPN-i rakenduse alla Google Play Store'ist.



![playstore](assets/fr/02.webp)



Pärast edukat paigaldamist klõpsake uue konto loomiseks nupule **Registreeri**.



![inscription](assets/fr/03.webp)



Sisestage oma salasõna ja kinnitage oma konto, täites oma e-posti aadressile Address saadetud OTP-koodi. Kuna Mozilla VPN on Mozilla Foundationi tasuline teenus, on Mozilla VPNi täielikuks kasutamiseks vaja tellimust. Klõpsake "Telli nüüd", et suunata teid Mozilla VPN-i hinnakujunduslehele.



![tarifs](assets/fr/04.webp)



Seejärel valige endale sobiv tellimusleping.



![plans](assets/fr/05.webp)



Seejärel jätkake maksmist PayPali või krediitkaardiga.



![paiement](assets/fr/06.webp)



Kui olete oma tellimuse aktiveerinud, avage Mozilla VPN-i tarkvara ja lubage Mozilla VPN-il teie soovil koguda tehnilisi andmeid teie sirvimise kohta või mitte.



![collecte](assets/fr/07.webp)



Saate aktiveerida ka reklaamivastase võitluse, brauseri jälgimise ja pahavara blokeerimise võimalused.



![privacy](assets/fr/08.webp)



Kui konfiguratsiooniprotsess on lõpetatud, näeb Mozilla VPN Interface välja nii:



![home](assets/fr/09.webp)



VPN-i saate aktiveerida, klõpsates alloleval raadionupul, mis paigutab teie arvuti IP Address ümber teie valitud asukoha IP-aadresside vahemikku. Samuti saate vaadata oma Mozilla VPN-kontoga ühendatud seadmete nimekirja otse avalehelt.



![activate](assets/fr/10.webp)



Mozilla VPN võimaldab teil valida oma asukoha kahes formaadis:





- Single-Hop: mis paigutab teie arvuti IP Address ümber ja krüpteerib andmed konkreetses valitud piirkonnas asuvasse serverisse, meie näites Sofiasse Valgevenes.





- Multi-Hop: loob teie arvutist krüpteeritud ühenduse kahe kaugserveriga. Tegemist on kahekordse krüpteerimisega: teie andmed krüpteeritakse serveri A kaudu, seejärel krüpteeritakse andmed serverist A uuesti serverisse B.



![hops](assets/fr/11.webp)



Klõpsates ikoonil **Settings**, saate juurdepääsu erinevatele Mozilla VPNi kohandamisvõimalustele. Menüüs **Võrgusätted** saate seadistada Mozilla VPN-i kõigi oma rakenduste jaoks või valida rakendused, millega te ei soovi Mozilla VPN-i kasutada. See valik on üks uuendusi, mis eristab Mozilla VPN-i enamusest teistest VPN-dest: tunneli jagamine.



![permissions](assets/fr/12.webp)



Jagatud tunneldamine on mugav funktsioon, mis võimaldab teil suunata osa oma internetiliiklusest VPN-i kaudu ja osa ilma VPN-ita sama sessiooni ajal. See võib olla kasulik internetipanganduse või muu internetiliikluse puhul, mis ei tööta VPNiga korralikult.



⚠️Mozilla VPN pakub jagatud tunneldamist kõigis toodetes, välja arvatud MacOs ja iOS-is. Vabandust, Apple'i kasutajad, te ei saa seda funktsiooni kasutada. Tõenäoliselt küll, sest nad lubasid seda funktsiooni ainult oma Androidi rakenduse kaudu ja nüüd laieneb see ka teistele operatsioonisüsteemidele.



Selleks, et tagada kasutajatele suurem konfidentsiaalsus, on Mozilla VPN-l **Kill Switch** süsteem, mis võimaldab katkestada teie internetiühenduse, kui VPN mingil põhjusel katkeb. See kaitseb teie IP Address ja muud isiklikku teavet.



Nüüd olete valmis turvaliselt ja konfidentsiaalselt internetis surfama. Kui sulle meeldis see õpetus, anna sellele Green pöidlaid. Oleme ka kindlad, et teile meeldib meie õpetus MULLVAD VPN-i kohta, mis on teine VPN-lahendus, mis ei nõua oma kasutajatelt mingeid isikuandmeid ja võimaldab teil maksta oma tellimise eest bitcoin'idega (mis on konfidentsiaalsem variant kui krediitkaardid):



https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8