---
name: Seedkeeper - Paroolihaldur
description: Kuidas salvestada oma paroole Seedkeeper nutikaardiga?
---

![cover](assets/cover.webp)



Seedkeeper on nutikaart, mille on välja töötanud Belgia ettevõte Satochip, mis on spetsialiseerunud digitaalsaladuste haldamiseks ja kaitsmiseks mõeldud riistvaralahendustele. Satochip on tuntud oma Bitcoin ökosüsteemi jaoks mõeldud kiipkaartide valiku poolest ja kavandas Seedkeeper'i alternatiivina traditsioonilistele mnemofraaside ja muude digitaalsaladuste säilitamise meetoditele.



Konkreetselt on Seedkeeper multifunktsionaalne EAL6-sertifikaadiga kiipkaart, millel on turvaline protsessor ja võltsimiskindel mälu (nn turvaline element). Nagu nimigi ütleb, on selle ülesanne salvestada Bitcoin portfoolio mnemonikaid ja paroole krüpteeritud ja kaitstud viisil. Seedkeeperiga saate generate, importida, korrastada ja salvestada oma saladusi otse kaardi turvalisse ossa.



Minu arvates on Seedkeeperil kaks peamist kasutusvõimalust, mida uurime 2 eraldi õpetuses:




- Bitcoin** Mälusõnade salvestamine: selle asemel, et kirjutada oma 12 või 24 sõna paberile, saate need sisestada kiipkaardile ja kaitsta neid PIN-koodiga.
- Paroolide haldamine**: saate generate tugevaid paroole rakenduse Seedkeeper kaudu ja salvestada need otse nutikaardile, mis annab teile mugava ja hõlpsasti kasutatava võrguühenduseta paroolihalduri.



Tehniliselt võttes on Seedkeeperi maht 8192 baiti, mis võimaldab salvestada vähemalt 50 eraldi saladust (täpne arv sõltub nende suurusest ja igaühega seotud metaandmetest). Seedkeeperile saab juurdepääsu kas [arvutiga ühendatud kiipkaardilugeja](https://satochip.io/accessories/) või NFC-ühendusega mobiilirakenduse kaudu. Kogu süsteem töötab võrguühenduseta režiimis, ilma internetiühenduseta, mis tagab piiratud ründepinna.



![Image](assets/fr/001.webp)



Eriti huvitav funktsioon on võimalus duplitseerida ühe Seedkeeper'i sisu teise Seedkeeper'i, et luua varukoopia. Selles õpetuses näitame teile, kuidas seda teha.



Selles õpetuses käsitleme ainult SeedKeeperi kasutamist traditsiooniliste paroolide jaoks paroolihalduri moodi. Kui soovite kasutada SeedKeeperit Bitcoin wallet mnemooniliste lausete salvestamiseks, vaadake seda teist õpetust:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Kuidas ma saan seemnepidaja?



Seedkeeper'i saamiseks on kaks peamist võimalust. Saate [osta selle otse Satochipi ametlikust poest](https://satochip.io/product/seedkeeper/) või volitatud edasimüüjalt. Kuid kuna [Seedkeeper on avatud lähtekoodiga](https://github.com/Toporin/Seedkeeper-Applet), on teil ka võimalus see ise [tühjale kiipkaardile](https://satochip.io/product/blank-javacard-for-diy-project/) paigaldada.



Kui soovite kasutada Seedkeeperi varundamisfunktsiooni, peate ilmselgelt ostma kaks kiipkaarti.



## 2. Seedkeeper-kliendi paigaldamine



Esimene samm on tarkvara installimine arvutisse või nutitelefoni. Arvutis peate [laadige alla Satochip-Utils'i uusim versioon](https://github.com/Toporin/Satochip-Utils/releases). Mobiiltelefonidel on Seedkeeper'i rakendus saadaval [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) ja [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Seedkeeper'i initsialiseerimine



Käivitage rakendus ja vajutage nupule "*Click & Scan*".



![Image](assets/fr/003.webp)



Teilt küsitakse PIN-koodi teie Seedkeeperile. Kuna tegemist on uue kaardiga, ei ole PIN-koodi veel kindlaks määratud. Selle sammu vahelejätmiseks sisestage ükskõik milline kood ja vajutage seejärel nuppu "*Järgmine*".



![Image](assets/fr/004.webp)



Seejärel asetage kaart nutitelefoni tagaküljele. Rakendus tuvastab, et Seedkeeper ei ole veel initsialiseeritud, ja palub teil määrata oma kiipkaardi PIN-koodi, mis on 4-16 tähemärki pikk. Optimaalse turvalisuse tagamiseks valige tugev PIN-kood, mis on võimalikult pikk, juhuslik ja koosneb paljudest erinevatest märkidest. See PIN-kood on ainus takistus teie salasõnadele füüsilise juurdepääsu vastu.



**Mäleta ka seda PIN-koodi nüüd salvestada**, näiteks paroolihalduris või eraldi füüsilisel andmekandjal. Viimasel juhul ärge kunagi hoidke PIN-koodi sisaldavat andmekandjat samas kohas kui teie Seedkeeper, sest muidu muutub see turvaelement kasutuks. On oluline, et teil oleks usaldusväärne varukoopia: ilma PIN-koodita ei ole teil võimalik taastada oma Seedkeeperisse salvestatud saladusi.



![Image](assets/fr/005.webp)



Kinnitage PIN-kood teist korda.



![Image](assets/fr/006.webp)



Teie Seedkeeper on nüüd initsialiseeritud. Saate selle avada, sisestades äsja määratud PIN-koodi.



![Image](assets/fr/007.webp)



Nüüd jõuate oma kiipkaardi haldamise lehele.



![Image](assets/fr/008.webp)



## 4. Salvesta paroolid Seedkeeperisse



Kui teie Seedkeeper on lukustamata, klõpsake nupule "*+*".



![Image](assets/fr/009.webp)



Valige "Genereeri saladus*". Valik "*Saladuse importimine*" võimaldab salvestada olemasoleva saladuse (näiteks varem loodud salasõna).



![Image](assets/fr/010.webp)



Meie puhul tahame salvestada parooli. Vajutage nupule "*Password*".



![Image](assets/fr/011.webp)



Määrake sellele saladusele "*Silt*", et seda oleks lihtne tuvastada, kui salvestate oma Seedkeeperisse mitu teavet. Samuti saate lisada parooliga seotud tunnuse ja saidi URL-i.



![Image](assets/fr/012.webp)



Valige oma parooli pikkus ja parameetrid, seejärel klõpsake "*Generate*" ja seejärel "*Import*".



![Image](assets/fr/013.webp)



Asetage oma Seedkeeper nutitelefoni tagaküljele.



![Image](assets/fr/014.webp)



Teie salasõna on registreeritud.



![Image](assets/fr/015.webp)



## 5. Juurdepääs oma Seedkeeper paroolile



Kui soovite oma salasõna kontrollida, võtke oma Seedkeeper ja klõpsake nupule "*Click & Scan*".



![Image](assets/fr/016.webp)



Sisestage oma PIN-kood ja vajutage "*Järgmine*".



![Image](assets/fr/017.webp)



Asetage oma Seedkeeper nutitelefoni tagaküljele.



![Image](assets/fr/018.webp)



See viib teid kõigi teie registreeritud saladuste nimekirja. Selles näites tahan ma kuvada oma Plan ₿ Academy konto parooli, seega klõpsan sellel.



![Image](assets/fr/019.webp)



Vajutage nuppu "*Reveal*".



![Image](assets/fr/020.webp)



Skaneerige oma Seedkeeper uuesti.



![Image](assets/fr/021.webp)



Ekraanile ilmub nüüd teie eelnevalt salvestatud parool. Võite selle kopeerida ja kasutada seda vastaval veebisaidil.



![Image](assets/fr/022.webp)



## 6. Seedkeeper'i varundamine



Nüüd teeme oma Seedkeeperist varukoopia teise Seedkeeperisse, nii et meil on kaks koopiat. See redundants võib olla osa strateegiast, et kindlustada oma kõige tähtsamaid paroole: näiteks hoida oma Seedkeeperit kahes erinevas kohas, et piirata füüsilisi riske, või usaldada koopia usaldusväärsele sugulasele.



Selleks võtke kaasa oma teine seemnepidaja (ärge unustage, et üks neist kahest oleks märgistatud, et vältida segadust). Alustage selle initsialiseerimisega, nagu on kirjeldatud selle õpetuse 3. sammus. Valige jällegi tugev PIN-kood. Sõltuvalt teie strateegiast võite valida erineva PIN-koodi või jätta sama.



![Image](assets/fr/023.webp)



Avage rakendus, klõpsake "*Click & Scan*", sisestage oma Seedkeeper nr 1 (allikas) PIN-kood, seejärel skannige see.



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



See on kõik, mis vaja! Nüüd teate, kuidas kasutada Seedkeeper'i oma paroolide salvestamiseks. Järgmises õpetuses vaatame, kuidas kasutada Seedkeeperit Bitcoin wallet varundamiseks. Samuti kutsun teid üles avastama selle kombineeritud kasutamist koos SeedSigneriga :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356