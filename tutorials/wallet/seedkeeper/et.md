---
name: Seedkeeper
description: Kuidas varundada oma wallet Bitcoin Seedkeeper nutikaardiga?
---

![cover](assets/cover.webp)



Seedkeeper on nutikaart, mille on välja töötanud Belgia ettevõte Satochip, mis on spetsialiseerunud digitaalsaladuste haldamiseks ja kaitsmiseks mõeldud riistvaralahendustele. Satochip on tuntud oma Bitcoin ökosüsteemi jaoks mõeldud kiipkaartide valiku poolest ja kavandas Seedkeeper'i alternatiivina traditsioonilistele mälusõnade salvestamise meetoditele.



Konkreetselt on Seedkeeper multifunktsionaalne EAL6-sertifikaadiga kiipkaart, millel on turvaline protsessor ja võltsimiskindel mälu (nn turvaline element). Nagu nimigi ütleb, on selle ülesanne salvestada Bitcoin wallet märke ja paroole krüpteeritud ja kaitstud viisil. Seedkeeperiga saate generate importida, organiseerida ja salvestada oma saladusi otse kaardi turvalisse ossa.



Minu arvates on Seedkeeperil kaks peamist kasutusvõimalust, mida uurime 2 eraldi õpetuses:




- Bitcoin** Mälusõnade salvestamine: selle asemel, et kirjutada oma 12 või 24 sõna paberile, saate need sisestada nutikaardile ja kaitsta neid PIN-koodiga.
- Paroolide haldamine**: saate generate tugevat parooli rakenduses Seedkeeper ja salvestada need otse kiipkaardile, mis annab teile mugava ja hõlpsasti kasutatava võrguühenduseta paroolihalduri.



Tehniliselt võttes on Seedkeeperi maht 8192 baiti, mis võimaldab salvestada vähemalt 50 eraldi saladust (täpne arv sõltub nende suurusest ja igaühega seotud metaandmetest). Seedkeeperile saab juurdepääsu kas [arvutiga ühendatud kiipkaardilugeja](https://satochip.io/accessories/) või NFC-ühendusega mobiilirakenduse kaudu. Kogu süsteem töötab võrguühenduseta režiimis, ilma internetiühenduseta, mis tagab piiratud ründepinna.



![Image](assets/fr/001.webp)



Eriti huvitav funktsioon on võimalus duplitseerida ühe Seedkeeper'i sisu teise Seedkeeper'i, et luua varukoopia. Selles õpetuses näitame teile, kuidas seda teha.



Seedkeeper on väga huvitav ka siis, kui seda kombineerida wallet staatusteta riistvaraga, nagu SeedSigner või Specter DIY. Sellisel juhul ei ole vaja kasutada Satochipi klienti arvutis või mobiiltelefonis. Seedkeeper hoiab seed oma secure element ja seda saab kasutada otse allkirjastamisseadmega, kaotades vajaduse paberkandjal QR-koodi järele. Ma ei hakka seda konkreetset kasutusjuhtumit selles õpetuses arendama, kuna see on teise spetsiaalse õpetuse teema :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Milline on Seedkeeper'i kasutusjuhtum?



Selles õpetuses käsitlen ma ainult Bitcoin-ga seotud kasutusjuhtumeid, kuna see ongi see, mida see õpetus käsitleb. Me ei käsitle paroolide haldamise funktsionaalsust, mis on teise õpetuse teema.



Võrreldes lihtsa mälulause paberkandjal varundamisega on Seedkeeper'i kasutamisel mitu eelist:





- Vargusvastane:** seed teie wallet-s ei ole selge tekstiga kättesaadav. Selle väljavõtmiseks peate teadma seemnepidaja PIN-koodi. Varas, kes seadme kätte saab, ei saa ilma selle koodita sellega midagi teha.





- Riski jaotamine kahe teguri vahel:** võite jagada turvalisuse digitaalse ja füüsilise teguri vahel. Näiteks kui salvestate Seedkeeper PIN-koodi oma paroolihalduris, on teil vaja seed saamiseks nii juurdepääsu sellele haldurile kui ka kiipkaardi füüsilist valdust (oluliselt väiksem rünnaku tõenäosus).





- Tsentraliseeritud haldamine:** Seedkeeper hõlbustab erinevate portfellide mitme seemne haldamist.





- Lihtsad varukoopiad:** lihtsalt dubleerige krüpteeritud varukoopiaid teistele SeedKeeperitele.



Kuid võrreldes teie seed lihtsa paberkandjal varundamisega on ka mitmeid puudusi:





- Hind:** on küll tagasihoidlik (umbes 25 eurot), kuid siiski kõrgem kui paberilehe hind.





- Sõltuvus üldotstarbelisest arvutiseadmest:** seed sisestamiseks ja haldamiseks on vaja arvutit või nutitelefoni, mis tähendab, et teie mnemo läbib masinat, millel on palju laiem ründepind kui wallet riistvaral. See võib kujutada endast ohtu, kui masin on ohustatud. Seepärast ei soovita ma kasutada Seedkeeperit seed riistvara wallet salvestamiseks (välja arvatud staatita kasutamisel ilma arvutita, nagu SeedSigneriga). wallet riistvara roll on just seed salvestamine minimalistlikus, väga turvalises keskkonnas. Kui seed sisestatakse käsitsi oma tavalisse arvutisse, ei ole see enam piiratud wallet riistvaraga: see satub ka üldotstarbelisse masinasse, mis on avatud mitmetele ründevektoritele. Seega on parem kasutada Seedkeeperit pigem kuuma kui külma wallet jaoks (v.a SeedSigner / olematu wallet riistvara).





- PIN-koodiga seotud kadumisrisk:** seed otsene kättesaamatus, erinevalt paberkandjal varundusest, pakub tõepoolest kaitset füüsilise varguse vastu. Kuid nagu alati, on turvalisus tasakaalustatav varguse ja kadumise riski vahel. Kui teie varukoopia nõuab PIN-koodi, muudab selle koodi kadumine võimatuks teie mälulause taastamise ja seega juurdepääsu teie bitcoinidele.



Neid eeliseid ja puudusi arvestades leian, et Seedkeeperi parimad kasutusalad (peale selle paroolihalduri funktsiooni) on ühelt poolt seemnete salvestamine teie **tarkvara portfellist**, kuna need asuvad juba teie telefonis või arvutis, või teie ekraanita wallet riistvarast nagu Satochip, ja teiselt poolt selle kasutamine koos staatita wallet riistvaraga nagu SeedSigner, kus ta tõeliselt esile tuleb.



Teine eriti huvitav kasutusjuhtum Seedkeeperile on võimalus turvaliselt ja usaldusväärselt varundada oma portfellide *Descriptors*.



## 2. Kuidas ma saan seemnepidaja?



Seedkeeper'i saamiseks on kaks peamist võimalust. Saate [osta selle otse Satochipi ametlikust poest](https://satochip.io/product/seedkeeper/) või volitatud edasimüüjalt. Kuid kuna [Seedkeeper on avatud lähtekoodiga](https://github.com/Toporin/Seedkeeper-Applet), on teil ka võimalus see ise [tühjale kiipkaardile](https://satochip.io/product/blank-javacard-for-diy-project/) paigaldada.



Kui soovite kasutada Seedkeeperi varundamisfunktsiooni, peate ilmselt ostma kaks kiipkaarti.



## 3. Seedkeeper-kliendi paigaldamine



Selles õpetuses varundame oma seed portfelli meie Seedkeeperil. Esimene samm on tarkvara installimine arvutisse või nutitelefoni. Arvutis peate [laadige alla Satochip-Utils'i uusim versioon](https://github.com/Toporin/Satochip-Utils/releases). Mobiiltelefonil on Seedkeeper'i rakendus saadaval nii [Google Play Store'is](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) kui ka [Apple App Store'is](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Seedkeeper'i initsialiseerimine



Käivitage rakendus ja vajutage nupule "*Click & Scan*".



![Image](assets/fr/003.webp)



Teilt küsitakse PIN-koodi teie Seedkeeperile. Kuna tegemist on uue kaardiga, ei ole PIN-koodi veel kindlaks määratud. Selle sammu vahelejätmiseks sisestage ükskõik milline kood ja vajutage seejärel nuppu "*Järgmine*".



![Image](assets/fr/004.webp)



Seejärel asetage kaart nutitelefoni tagaküljele. Rakendus tuvastab, et Seedkeeper ei ole veel initsialiseeritud, ja palub teil määrata oma kiipkaardi PIN-koodi, mis on 4-16 tähemärki pikk. Optimaalse turvalisuse tagamiseks valige tugev parool, mis on võimalikult pikk, juhuslik ja koosneb paljudest erinevatest märkidest. See PIN-kood on ainus takistus füüsilise juurdepääsu vastu teie taastamislausele.



**Mäleta ka seda PIN-koodi nüüd salvestada**, näiteks paroolihalduris või eraldi füüsilisel andmekandjal. Viimasel juhul ärge kunagi hoidke PIN-koodi sisaldavat andmekandjat samas kohas kui teie Seedkeeper, sest muidu muutub see turvaelement kasutuks. On oluline, et teil oleks usaldusväärne varukoopia: ilma PIN-koodita ei ole teil võimalik taastada oma Seedkeeperisse salvestatud saladusi.



![Image](assets/fr/005.webp)



Kinnitage PIN-kood teist korda.



![Image](assets/fr/006.webp)



Teie Seedkeeper on nüüd initsialiseeritud. Saate selle avada, sisestades äsja määratud PIN-koodi.



![Image](assets/fr/007.webp)



Nüüd jõuate oma kiipkaardi haldamise lehele.



![Image](assets/fr/008.webp)



## 5. seed registreerimine Seedkeeperil



Kui teie Seedkeeper on lukustamata, klõpsake nupule "*+*".



![Image](assets/fr/009.webp)



Valige "Impordi saladus*". Valik "*Lisenda saladus*" võimaldab teil luua uue mnemoonilise fraasi otse rakendusest.



![Image](assets/fr/010.webp)



Meie puhul tahame salvestada seed portfelli. Klõpsake nupule "*Mnemonic*".



![Image](assets/fr/011.webp)



Määrake sellele saladusele "*Silt*", et seda oleks lihtne tuvastada, kui salvestate oma Seedkeeperisse mitu teavet.



![Image](assets/fr/012.webp)



Seejärel sisestage oma taastamise fraas ettenähtud väljale. Soovi korral võite lisada ka passphrase BIP39 või oma *Descriptors*. Seejärel klõpsake nuppu "Import*".



![Image](assets/fr/013.webp)



*Sellel pildil kujutatud mnemoonika on väljamõeldud ja ei kuulu kellelegi. See on ainult näide. Ärge kunagi avaldage kellelegi oma mnemoonikat, sest muidu varastatakse teie bitcoinid



Asetage oma Seedkeeper nutitelefoni tagaküljele.



![Image](assets/fr/014.webp)



Teie seed on registreeritud.



![Image](assets/fr/015.webp)



## 6. Juurdepääs oma seed-le Seedkeeperil



Kui soovite oma mnemofraasi kontrollida, võtke oma Seedkeeper ja vajutage nupule "*Click & Scan*".



![Image](assets/fr/016.webp)



Sisestage oma PIN-kood ja vajutage "*Järgmine*".



![Image](assets/fr/017.webp)



Asetage oma Seedkeeper nutitelefoni tagaküljele.



![Image](assets/fr/018.webp)



See viib teid kõigi teie registreeritud saladuste nimekirja. Selles näites tahan kuvada oma "*Blockstream App*" portfelli seed, seega klõpsan sellel.



![Image](assets/fr/019.webp)



Vajutage nuppu "*Reveal*".



![Image](assets/fr/020.webp)



Skaneerige oma Seedkeeper uuesti.



![Image](assets/fr/021.webp)



Ekraanile kuvatakse nüüd teie eelnevalt salvestatud mälulause.



![Image](assets/fr/022.webp)



## 7. Seedkeeper'i varundamine



Me teeme nüüd oma Seedkeeperist varukoopia teise Seedkeeperisse, et meil oleks kaks koopiat. See redundants võib olla osa strateegiast, et kindlustada oma bitcoinid: näiteks hoiustada oma fraasi kahes erinevas kohas, et piirata füüsilisi riske, või usaldada koopia usaldusväärsele sugulasele osana pärimisplaanist.



Selleks võtke kaasa oma teine seemnepidaja (ärge unustage, et üks neist kahest oleks märgistatud, et vältida segadust). Alustage selle initsialiseerimisega, nagu on kirjeldatud selle õpetuse 4. sammus. Valige jällegi tugev parool. Sõltuvalt teie strateegiast võite valida teise parooli või jätta sama parooli.



![Image](assets/fr/023.webp)



Avage rakendus, klõpsake "*Click & Scan*", sisestage oma Seedkeeper nr 1 (allikas) parool ja seejärel skannige see.



![Image](assets/fr/024.webp)



See viib teid avalehele, kus on teie saladuste nimekiri. Klõpsake kolmele väikesele punktile kasutajaliidese paremas ülaosas.



![Image](assets/fr/025.webp)



Valige "*Taasta varukoopia*", seejärel vajutage "*Start*".



![Image](assets/fr/026.webp)



Sisestage oma varukaardi PIN-kood (Seedkeeper nr 2).



![Image](assets/fr/027.webp)



Seejärel skaneerige kaart.



![Image](assets/fr/028.webp)



Tehke sama ka põhikaardiga (Seedkeeper nr 1), seejärel klõpsake nuppu "*Make a backup*".



![Image](assets/fr/029.webp)



Teie Seedkeeper nr 2 sisaldab nüüd kõiki Seedkeeper nr 1 salvestatud saladusi.



![Image](assets/fr/030.webp)



Saate oma Seedkeeper n°2 skaneerida, et kontrollida, kas saladused on kopeeritud.



![Image](assets/fr/031.webp)



See on kõik, mis vaja! Nüüd te teate, kuidas kasutada Seedkeeper'i, et salvestada Bitcoin wallet mnemofraasi. Järgmises õpetuses vaatame, kuidas kasutada Seedkeeperit paroolide salvestamiseks. Samuti kutsun teid üles avastama selle kombineeritud kasutamist koos SeedSigneriga :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Selles õpetuses oleme maininud mitu korda ***Descriptors*** teie Bitcoin portfellis. Te ei tea, mis need on? Sellisel juhul soovitan teil läbida meie tasuta CYP 201 koolituskursus, kus käsitletakse põhjalikult kõiki HD portfellide toimimisega seotud mehhanisme!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f