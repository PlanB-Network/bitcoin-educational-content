---
name: Seedkeeper x SeedSigner
description: Kuidas kasutada Seedkeeperit koos SeedSigneriga?
---

![cover](assets/cover.webp)



*Tänu [Satochip](https://satochip.io/) meeskonnale, kes on nõus [nende videote](https://www.youtube.com/@satochip/videod) taaskasutamisega selles õpetuses. Tänud ka [Crypto Guide](https://www.youtube.com/@CryptoGuide/) firmware fork eest, mis võimaldas toetada kiipkaarte



---

SeedSigner on wallet riistvara, mille panete ise kokku standardvarustusest, tavaliselt Raspberry Pi Zero ümber. Seda wallet nimetatakse "*stateless*": erinevalt enamikust teistest turul olevatest mudelitest (Coldcard, Trezor, Ledger jne.) ei salvesta ta mingeid andmeid püsimällu, vaid töötab ainult otse RAMist. Selle tulemusena ei salvestata teie portfelli seed kunagi SeedSignerisse. Iga kord, kui te taaskäivitate, peate selle täitma, et seade saaks teie tehinguid allkirjastada. Kõige tavalisem meetod on salvestada oma seed QR-koodina, mida te siis iga kord skaneerite (*SeedQR*).



Selline lähenemisviis kujutab endast siiski märkimisväärset ohtu: seed peab jääma ligipääsetavaks selge tekstina, et seda oleks võimalik skaneerida. Varguse või sissetungi korral võib ründaja selle hõlpsasti kätte saada ja teie bitcoinid varastada.



Selle nõrkuse ületamiseks saab SeedSignerit kombineerida [**Seedkeeperiga**](https://satochip.io/product/seedkeeper/), mis on Satochipi poolt välja töötatud kiipkaart. See võimaldab mnemoonilisi fraase (või muid saladusi) salvestada secure element-sse, mis on kaitstud PIN-koodiga. Seedkeeper-rakendus on avatud lähtekoodiga ja selle secure element-l on EAL6+ sertifikaat. Koos SeedSigneriga kasutatuna pakub see väga huvitavat turvaelementi: teie võtmeid hallatakse täielikult off-line, te allkirjastate oma tehinguid usaldusväärsel ekraanil ja seed on füüsiliselt kaitstud füüsilise rünnaku suhtes vastupidavas kiipkaardis.



Paigaldamise lõpuleviimiseks on vaja vaid järgmisi esemeid:




- Klassikalise SeedSigneri jaoks on vaja tavalist varustust: Raspberry Pi Zero, Waveshare 1,3-tolline ekraan, ühilduv kaamera ja microSD-kaart (täpsemalt leiad SeedSigneri õpetusest allpool);
- SeedSigneri laienduskomplekt, mis on saadaval [Satochipi ametlikus poes](https://satochip.io/product/seedsigner-extension-kit/), mis võimaldab teil lugeda ja kirjutada kiipkaardile otse teie SeedSignerist. Teine võimalus on kasutada välist kiipkaardilugejat, mille saab kaabli abil ühendada Raspberry Pi Micro-USB-porti. Ma ei ole seda lahendust siiski ise katsetanud;
- Seedkeeper või alternatiivina tühi kiipkaart, millele saab paigaldada Seedkeeper-rakenduse (Satochipi poolt müüdav laienduskomplekt sisaldab juba tühja kiipkaarti).



![Image](assets/fr/01.webp)



See õpetus hõlmab kahte stsenaariumi:




- Kui teil on juba Bitcoin portfell, mida hallatakse SeedSigneri kaudu, installige lihtsalt uus püsivara. Seejärel saate jätkata oma olemasoleva wallet kasutamist, kasutades seekord Seedkeeper'i, et tagada suurem turvalisus.
- Kui teil ei ole veel Bitcoin wallet seotud oma SeedSigneriga, peate järgima allpool nimetatud õpetuse samme **5** ja **6**. Nendes punktides selgitatakse, kuidas generate mnemofraasi SeedSigneriga ühendada, salvestada see *SeedQR* kaudu ja seejärel ühendada see wallet Sparrow Wallet-ga, et seda hallata. Ma ei hakka neid protseduure siin kirjeldama ja **eeldan, et teil on juba toimiv Bitcoin wallet, mis on konfigureeritud Sparrow ja teie SeedSigneriga**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Paigaldage püsivara



SeedSigneri kasutamiseks koos Seedkeeperiga tuleb paigaldada alternatiivne firmware, mis erineb algsest SeedSignerist, et toetada kiipkaartide lugemist. Selleks [soovitan kasutada fork alates "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Laadige alla [pildi uusim versioon](https://github.com/3rdIteration/seedsigner/releases) (`.zip`), mis vastab teie kasutatavale Raspberry Pi mudelile.



![Image](assets/fr/02.webp)



Kui teil seda veel ei ole, laadige alla tarkvara [Balena Etcher](https://etcher.balena.io/), seejärel toimige järgmiselt:




- Sisestage microSD-kaart arvutisse;
- Launch Etcher ;
- Valige just alla laaditud .zip-fail;
- Valige sihtmärgiks microSD-kaart;
- Klõpsake nuppu "Flash!`.



![Image](assets/fr/03.webp)



Oodake, kuni protsess on lõppenud: teie microSD on nüüd kasutusvalmis. Nüüd võite minna edasi oma seadme kokkupaneku juurde.



Lisateavet püsivara paigaldamise ja tarkvara kontrollimise kohta (samm, mida ma soovitan tungivalt teha) leiate järgmisest juhendmaterjalist:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Nutikaardilugeja kokkupanek



![video](https://youtu.be/jqE8HDMCImA)



Alustage kaamera paigaldamisega Raspberry Pi Zero'le, sisestades selle ettevaatlikult kaameratihvtisse ja lukustades selle musta keelega. Seejärel asetage Pi korpuse põhja, jälgides, et pordid oleksid vastavuses vastavate avadega.



![Image](assets/fr/04.webp)



Seejärel ühendage kiipkaardilugeja Raspberry Pi Zero GPIO-pinide külge.



![Image](assets/fr/05.webp)



Libistage plastkate üle kiipkaardilugeja, kuni see on õigesti paigutatud.



![Image](assets/fr/06.webp)



Seejärel lisage ekraan laienduse GPIO-pinidele.



![Image](assets/fr/07.webp)



Lõpuks sisestage microSD-kaart, mis sisaldab püsivara, Raspberry Pi Zero külgporti.



![Image](assets/fr/08.webp)



Nüüd saate SeedSigneri ühendada kas Raspberry Pi Zero Micro-USB-pordi või laienduse USB-C-pordi kaudu. Mõlemad võimalused toimivad. Oodake paar sekundit käivitumist, seejärel peaks ilmuma tervitusekraan.



![Image](assets/fr/09.webp)



SeedSigneri esialgse seadistamise kohta lisateavet leiate järgmisest juhendmaterjalist:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Nutikaardi väljalülitamine Seedkeeper'i rakendusega (valikuline)



![video](https://youtu.be/NF4HemyEcOY)



Kui teil on juba Seedkeeper, võite selle sammu vahele jätta ja minna otse sammu 4 juurde. Selles jaotises vaatame, kuidas paigaldada Seedkeeper'i rakendus tühjale kiipkaardile (DIY-meetod).



Alustamiseks avage oma SeedSigneri menüü "Tööriistad > Smartcard Tools".



![Image](assets/fr/10.webp)



Seejärel valige `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Sisestage oma kiipkaart SeedSigner'i lugejasse, kiip allapoole, ja valige seejärel rakendus "SeedKeeper".



![Image](assets/fr/12.webp)



Palun olge paigaldamise ajal kannatlik: protsess võib võtta mitu kümme sekundit.



![Image](assets/fr/13.webp)



Kui applet on edukalt paigaldatud, saate jätkata sammuga 4.



![Image](assets/fr/14.webp)



## 4. Olemasoleva SeedQRi salvestamine Seedkeeperil



![video](https://youtu.be/X-vmFHU9Ec8)



Nüüd, kui teie Seedkeeper on töökorras, saate salvestada oma Bitcoin wallet mnemonüümi kiipkaardile. Alustamiseks lülitage oma SeedSigner sisse nagu tavaliselt, seejärel skannige oma wallet *SeedQR*, et laadida see seadmesse. Kui seed on imporditud, valige lihtsalt `Done`.



![Image](assets/fr/15.webp)



Kui seed on laaditud, avage menüü "Varukoopia seemne".



![Image](assets/fr/16.webp)



Seejärel sisestage oma SeedKeeper SeedSigner-kettasse ja valige valik `To SeedKeeper`.



![Image](assets/fr/17.webp)



SeedSigner palub teil seejärel sisestada oma Seedkeeper'i PIN-kood. Kuna tegemist on tühja kaardiga, ei ole koodi veel määratud. Selle sammu vahelejätmiseks sisestage ükskõik milline kood ja kinnitage seejärel.



![Image](assets/fr/18.webp)



SeedSigner tuvastab, et Seedkeeper ei ole veel initsialiseeritud (st parooli pole määratud). Jätkamiseks klõpsake nuppu `I Understanding`.



![Image](assets/fr/19.webp)



Nüüd valige oma seemnepidaja uus PIN-kood, mis võib olla vahemikus 4-16 märki. Lisaturvalisuse tagamiseks valige pikk ja juhuslik kood: see on ainus tõkkepuu, mis kaitseb füüsilist juurdepääsu teie mnemofraasile.



Ärge unustage, et salvestate selle PIN-koodi kohe pärast selle loomist kas usaldusväärsesse paroolihaldurisse või eraldi füüsilisele andmekandjale, sõltuvalt teie strateegiast. Viimasel juhul ärge kunagi hoidke PIN-koodi sisaldavat andmekandjat samas kohas kui teie Seedkeeper, vastasel juhul muutub kaitse ebaefektiivseks. Oluline on varukoopia olemasolu: **Kui see PIN-kood puudub teil juurdepääs oma seed-le ja teie bitcoinid on kadunud**.



![Image](assets/fr/20.webp)



Seejärel saate määratleda oma mnemoonilise fraasiga seotud "sildi". See silt on kasulik, kui te salvestate Seedkeeperisse mitu saladust, et saaksite need hõlpsasti tuvastada.



![Image](assets/fr/21.webp)



Teie mälulause on nüüd nutikaardile salvestatud.



![Image](assets/fr/22.webp)



Turvastrateegia osas on võimalik kasutada mitmeid lähenemisviise, sõltuvalt teie vajadustest ja riskipositsiooni tasemest. Isiklikult soovitan teil hoida vähemalt 2 koopiat oma seed-st:




- See on esmakordne kiipkaartide puhul, mida saate hoida hõlpsasti kättesaadavana igapäevaste toimingute jaoks, näiteks aadresside kontrollimiseks või tehingute allkirjastamiseks. See meetod on praktiline (nagu näeme 5. osas) ja jääb tänu PIN-koodi pakutavale kaitsele turvaliseks, nii et saate seda hoida ilma suurema riskita;
- Teine koopia teie krüpteerimata mnemofraasist, mis on teie portfelli lõplikuks varukoopiaks, mida kasutatakse ainult Seedkeeper'i kadumise või varguse korral. Kuna see versioon on krüpteerimata, tuleb seda hoida eraldi, turvalisemas kohas, et vältida kahe varukoopia samaaegset kahjustamist.



Sõltuvalt teie kaitsestrateegiast ja riskiprofiilist võite ka dubleerida seed mitmel erineval Seedkeeper'il või luua mitu füüsilist koopiat mnemoonikust. Kui soovite nende tavade kohta rohkem teada saada, vaadake järgmist juhendmaterjali:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. seed laadimine Seedkeeperist



![video](https://youtu.be/ms0Iq_IyaoE)



Nüüd saate kasutada oma Seedkeeperit, et laadida oma mnemooniline fraas SeedSignerisse käivitamisel ja seega allkirjastada oma Bitcoin tehingud. Alustamiseks lülitage oma SeedSigner sisse, ühendades selle, seejärel avage menüü `Seeds`.



![Image](assets/fr/23.webp)



Seejärel valige valik "From SeedKeeper".



![Image](assets/fr/24.webp)



Sisestage oma Seedkeeper kiipkaardi lugejasse ja sisestage PIN-kood, et avada see. Kinnitage oma sisestus, vajutades parempoolset alumist kinnitusnuppu `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper võib sisaldada mitmeid saladusi, nii et SeedSigner palub teil seejärel valida, millist soovite laadida. Kuvatud silt vastab sammus 4 määratud nimele. Kui, nagu minu puhul, olete registreerinud ainult ühe seed, on saadaval ainult üks valik.



![Image](assets/fr/26.webp)



Teie seed on nüüd laetud. Kontrollige, et tegemist on õige wallet-ga, võrreldes ekraanil kuvatavat sõrmejälge Sparrow Wallet seadetes määratud sõrmejäljega. See sõrmejälg esitati ka wallet esmakordsel loomisel.



Kui kasutate passphrase, võite seda selles etapis kasutada (vt selle õpetuse 6. osa). Vastasel juhul klõpsake lihtsalt nuppu "Valmis".



![Image](assets/fr/27.webp)



Seejärel saate oma wallet kasutada tavapäraselt: kontrollida oma tarneaadresse ja allkirjastada tehinguid, nagu klassikalise SeedSigneriga. Lisateavet selle kasutamise kohta leiate spetsiaalsest juhendmaterjalist :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Seedkeeper'i kasutamine koos passphrase BIP39-ga



Kas te kasutate passphrase portfelli kaitsmiseks Bitcoin portfelli? Saate selle ka oma Seedkeeperis registreerida, koos oma seed-ga. See lahendus võimaldab teil kiiresti laadida oma wallet SeedSignerisse, ilma et peaksite passphrase iga kord käsitsi väikesele klahvistikule sisestama.



Minu arvates on see meetod eriti huvitav, sest see võimaldab teil kasutada passphrase turvaeeliseid, kõrvaldades samal ajal selle igapäevase kasutamisega seotud piirangud. Siin on näide konfiguratsioonist, mida ma soovitaksin:




- Hoidke oma seed ja passphrase Seedkeeperis, mis on kaitstud tugeva PIN-koodiga (see on oluline). See varukoopia võimaldab teil oma wallet hõlpsasti igapäevaselt kasutada. Soovi korral võite selle teabe dubleerida teisel Seedkeeperil;
- Hoidke ka selge koopia oma mälumärkidest ja passphrase, paberil või metallist. See on teie viimase abinõuna kasutatav varukoopia, kui kaotate oma Seedkeeper'i või selle PIN-koodi. Hoidke neid koopiaid kindlasti eraldi kohtades, et neid ei saaks samaaegselt ohustada.



Sellise konfiguratsiooni korral, kui keegi saab kätte ainult teie lihtsa teksti mnemoonika, ei saa ta midagi varastada ilma passphrase tundmata (eeldusel muidugi, et see on piisavalt tugev, et vastu seista brute-force rünnakule). Kui aga keegi avastab teie passphrase lihtsa tekstina, jääb see ilma vastava mnemoonilise fraasita kasutuskõlbmatuks.



Lõpuks, kui kellelgi õnnestub saada füüsiline ligipääs teie Seedkeeperile, mis sisaldab seed ja passphrase, ei saa ta midagi välja võtta, kui ta ei tea PIN-koodi. Erinevalt passphrase-st ei saa seda koodi lõhkuda, sest nutikaart lukustab end automaatselt pärast 5 ebaõiget katset.



Selle konfiguratsiooni ohutus põhineb seega kahel olulisel punktil:




- **passphrase tugev**: see peab olema pikk, juhuslik ja sisaldama mitmesuguseid tähemärke. Selle keerukus ei ole teie jaoks probleemiks, sest te peate selle sisestama ainult üks kord klaviatuuril initsialiseerimise ajal; pärast seda edastab selle Seedkeeper ;
- **Tugev PIN-kood** Seedkeeperile: samuti juhuslik ja koosneb 16 tähemärgist.



Selle seadistuse seadistamiseks alustage oma passphrase laadimisega SeedSignerisse tavalisel viisil. Võite järgida selles juhendis kirjeldatud menetlust:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Kui teie passphrase portfell on nõuetekohaselt SeedSignerisse laaditud, avage menüü "Seedid" ja valige sellele portfellile vastav jalajälg. Pange tähele, et see jalajälg erineb passphrase-ta portfelli omast.



![Image](assets/fr/28.webp)



Seejärel klõpsake nupule `Backup Seed`, sisestage Seedkeeper kettale ja valige `To SeedKeeper`.



![Image](assets/fr/29.webp)



Sisestage PIN-kood, et avada Seedkeeper, seejärel määrake sellele saladusele silt. Te võite jätta sõrmejälje sildiks, et säilitada mingisugune usutav eitatavus, või märkida selgesõnaliselt näiteks `Passphrase Wallet`.



![Image](assets/fr/30.webp)



Teie passphrase portfell on nüüd registreeritud Seedkeeperis.



![Image](assets/fr/31.webp)



Järgmisel käivitamisel sisestage lihtsalt Seedkeeper kettasse ja seejärel navigeerige menüüsse `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Sisestage PIN-kood, et avada kiipkaart, seejärel valige wallet, mis vastab teie passphrase-le.



![Image](assets/fr/33.webp)



Kontrollige passphrase ja teie wallet jäljendit, seejärel kinnitage.



![Image](assets/fr/34.webp)



Nüüd saate passphrase abil oma portfellile ligi ja allkirjastada oma tehinguid nagu tavaliselt SeedSigneriga.



## 7. Lisavõimalused



Menüüst "Tööriistad > Nutikaardi tööriistad" leiate mitu võimalust oma Seedkeeper'i haldamiseks:





- Menüüs "Üldised tööriistad" saate :
 - Kontrollige kaardi autentsust;
 - PIN-koodi muutmine ;
 - Muuda oma saladustega seotud sildid ;
 - Lülita NFC-funktsioon välja (soovitatav, kui kasutad ainult kiibilugejat) ;
 - Tehke tehasepärane lähtestamine.





- Menüüs `SeedKeeper Functions` saate :
 - Vaadake registreeritud saladuste nimekirja ;
 - Salvesta uus saladus ;
 - Olemasoleva saladuse kustutamine ;
 - Salvestage või laadige oma kirjeldused (kasulik funktsioon multi-sig portfellide jaoks).





- Menüüs `DIY Tools` saate :
 - Seedkeeper-rakenduse koostamine ;
 - Paigaldage applet tühjale kaardile ;
 - Kustutage Seedkeeper-rakendust, et see uuesti tühjaks teha.



Nüüd tead, kuidas kasutada Seedkeeperit oma portfelli turvaliseks varundamiseks koos SeedSigneriga.



Kui see ülesehitus on teid veennud, siis ärge kõhkle toetamast projekte, mis seda võimaldavad:




- Ostes oma seadmed otse [Satochipi veebisaidilt](https://satochip.io/shop/);
- Tehes [annetuse projektile SeedSigner](https://seedsigner.com/donate/);
- Tellides [Crypto Guide'i YouTube'i kanali](https://www.youtube.com/@CryptoGuide/), mida haldab isik, kes haldab GitHubi repositooriumi, kus asub muudetud püsivara.