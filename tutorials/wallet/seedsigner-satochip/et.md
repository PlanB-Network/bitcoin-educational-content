---
name: Satochip x SeedSigner
description: Kuidas kasutada Satochipi koos SeedSigneriga?
---

![cover](assets/cover.webp)



*Tänu [Crypto Guide](https://www.youtube.com/@CryptoGuide/) oma fork SeedSigner firmware'ile nutikaardi toe eest, mida me kasutame selles õpetuses



---

Satochip on wallet kiipkaardiformaadis riistvara, millel on EAL6+ sertifitseeritud turvaelement, mis on üks kõrgemaid turvastandardeid. Selle on projekteerinud ja tootnud samanimeline Belgia ettevõte Satochip.



Umbes 25-eurose hinnaga Satochip eristub konkurentide hulgast oma suurepärase hinna ja kvaliteedi suhtega. Tänu turvalisele kiibile pakub see vastupidavust füüsilistele rünnakutele. Lisaks sellele on selle rakenduse lähtekood täielikult avatud lähtekoodiga, mis on litsentsitud *AGPLv3* alusel.



Teisest küljest seab selle formaat teatavad funktsionaalsed piirangud. Satochip'i peamine puudus on integreeritud ekraani puudumine: kasutajad peavad seega allkirjastama tehinguid pimesi, tuginedes ainult arvuti ekraanile.



Selle nõrkuse ületamiseks on eriti huvitav konfiguratsioon kasutada seda koos SeedSigneriga. Selles seadistuses ei toimu suhtlus enam otse arvuti ja Satochipi vahel, vaid QR-koodide vahetamise kaudu arvuti ja SeedSigner vahel. SeedSigner toimib siis usaldusekraanina: ta kuvab allkirjastatavat teavet, samal ajal kui allkirjastamine toimub Satochipi poolt. Erinevalt tavapärasest SeedSigneri kasutamisest (või isegi kasutamisest koos Seedkeeperiga) ei laadita seed kunagi SeedSignerisse. SeedSigner muutub seega Satochipi ekraaniks, kõrvaldades pimesi allkirjastamisega seotud riskid.



Kui me vaatame probleemi teistpidi, täidab SeedSigner koos Satochipiga SeedSigneri suure lünga: võime salvestada ja kasutada seed-i secure element-siseselt.



Minu arvates pakub selline konfiguratsioon mitmeid eeliseid tavapäraste riistvaraliste rahakottide ees:




- Satochip maksab umbes 25 eurot ja kuna rakendus on avatud lähtekoodiga, saate selle ise tühjale kiipkaardile paigaldada. Seejärel tuleb lisada SeedSigneri komponentide ja kiipkaartide lugemiseks vajaliku laienduse maksumus: sõltuvalt sellest, kust te selle riistvara ostate, peaks summa olema 70-100 eurot.
- Kogu seadistusega seotud tarkvara on avatud lähtekoodiga: SeedSigner firmware ja Satochip applet.
- Saate kasu sertifitseeritud turvaelemendist.
- Konfigureerimist saab teostada täiesti iseseisvalt, kasutamata otseselt Bitcoin kasutamiseks mõeldud riistvara, mis võib pakkuda teatud välistele ohtudele (sealhulgas sõltuvalt riigist ka riigi survele) teatud liiki usutavat eitamist ja vastupanu. See on huvitav lahendus ka siis, kui teie piirkonnas on juurdepääs kaubanduslikule riistvarale piiratud või võimatu.




## 1. Vajalikud materjalid



Selle seadistuse tegemiseks vajate järgmisi esemeid:




- Klassikalise SeedSigner'ile vajalik tavapärane varustus :
 - raspberry Pi Zero koos GPIO-pinidega,
 - 1.3" Waveshare ekraan,
 - ühilduv kaamera,
 - microSD-kaart.



![Image](assets/fr/01.webp)





- SeedSigneri laienduskomplekt, mis on saadaval [ametlikus Satochip poes](https://satochip.io/product/seedsigner-extension-kit/), mis võimaldab teil lugeda ja kirjutada kiipkaardile otse teie SeedSignerist. Teine võimalus on kasutada [välist kiipkaardilugejat](https://satochip.io/product/chip-card-reader/), mida saab kaabli abil ühendada Raspberry Pi Micro-USB-porti. Ma ei ole seda lahendust siiski ise katsetanud;
- [A Satochip](https://satochip.io/product/satochip/) või alternatiivina [tühi kiipkaart](https://satochip.io/product/card-for-diy-project/), millele saab paigaldada Satochip-rakenduse (Satochipi poolt müüdav laienduskomplekt sisaldab juba tühja kiipkaarti). Satochipi laienduskomplekt toetab ka [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/) formaati. Seega võite soovi korral valida selle formaadi.



![Image](assets/fr/02.webp)



Täpsemat teavet SeedSigneri kokkupanekuks vajalike seadmete kohta leiate selle teise õpetuse 1. osast:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Paigaldage püsivara



Et kasutada oma SeedSignerit koos Satochipiga, peate installima alternatiivse firmware, mis erineb algsest SeedSignerist, et toetada kiipkaardi lugemist. Selleks [soovitan kasutada fork alates "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Laadige alla [image'i uusim versioon](https://github.com/3rdIteration/seedsigner/releases) (`.zip`), mis vastab teie kasutatavale Raspberry Pi mudelile.



![Image](assets/fr/03.webp)



Kui teil seda veel ei ole, laadige alla tarkvara [Balena Etcher](https://etcher.balena.io/), seejärel toimige järgmiselt:




- Sisestage microSD-kaart arvutisse;
- Launch Etcher ;
- Valige just alla laaditud .zip-fail;
- Valige sihtmärgiks microSD-kaart;
- Klõpsake nuppu "Flash!`.



![Image](assets/fr/04.webp)



Oodake, kuni protsess on lõppenud: teie microSD on nüüd kasutusvalmis. Nüüd võite minna edasi oma seadme kokkupaneku juurde.



Lisateavet püsivara paigaldamise ja tarkvara kontrollimise kohta (samm, mida ma soovitan tungivalt teha) leiate järgmisest juhendmaterjalist:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Nutikaardilugeja kokkupanek



Alustage kaamera paigaldamisega Raspberry Pi Zero'le, sisestades selle ettevaatlikult kaameratihvtisse ja lukustades selle musta keelega. Seejärel asetage Pi korpuse põhja, jälgides, et pordid oleksid vastavuses vastavate avadega.



![Image](assets/fr/05.webp)



Seejärel ühendage kiipkaardilugeja Raspberry Pi Zero GPIO-pinide külge.



![Image](assets/fr/06.webp)



Libistage plastkate üle kiipkaardilugeja, kuni see on õigesti paigutatud.



![Image](assets/fr/07.webp)



Seejärel lisage ekraan laienduse GPIO-pinidele.



![Image](assets/fr/08.webp)



Lõpuks sisestage microSD-kaart, mis sisaldab püsivara, Raspberry Pi Zero külgporti.



![Image](assets/fr/09.webp)



Nüüd saate SeedSigneri ühendada kas Raspberry Pi Zero Micro-USB-pordi või laienduse USB-C-pordi kaudu. Mõlemad võimalused toimivad. Oodake paar sekundit käivitumist, seejärel peaks ilmuma tervitusekraan.



![Image](assets/fr/10.webp)



SeedSigneri esialgse seadistamise kohta lisateabe saamiseks soovitan teil tutvuda järgneva õpetuse 4. osaga:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Nutikaardi väljalülitamine Satochip rakenduse abil (valikuline)



Kui teil on juba Satochip, võite selle sammu vahele jätta ja minna otse sammu 4 juurde. Selles jaotises vaatame, kuidas paigaldada Satochip-rakendust tühjale kiipkaardile (DIY-meetod). Applet on lihtsalt väike programm, mis töötab nutikaardil ja võimaldab meil hallata konkreetseid funktsioone.



Alustamiseks avage oma SeedSigneri menüü "Tööriistad > Smartcard Tools".



![Image](assets/fr/11.webp)



Seejärel valige `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Sisestage oma kiipkaart SeedSigneri lugejasse, kiip allapoole suunatud, ja valige rakendus `Satochip`.



![Image](assets/fr/13.webp)



Palun olge paigaldamise ajal kannatlik: protsess võib võtta mitu kümme sekundit.



![Image](assets/fr/14.webp)



Kui applet on edukalt paigaldatud, saate jätkata sammuga 4.



![Image](assets/fr/15.webp)




## 5. seed loomine ja salvestamine



### 5.1. seed genereerimine



Nüüd, kui teil on kõik riist- ja tarkvara korralikult tööle pandud, võite jätkata Bitcoin portfelli loomisega. Selleks ühendage oma SeedSigner, seejärel generate oma seed nagu tavalise SeedSigneriga, kas täringut veeretades või fotot tehes:




- Mine menüüsse `Tööriistad > Kaamera / Nopavisked`;
- Seejärel järgige entroopia loomise protsessi vastavalt valitud meetodile;
- Lõpuks varundage seed füüsilisele andmekandjale ja kontrollige varukoopiaid hoolikalt.



![Image](assets/fr/16.webp)



Kui soovite näha selle protseduuri üksikasju, järgige selle õpetuse 5. osa:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. seed salvestamine Seedkeeperile



Kui seed on genereeritud, on see ainus aeg, mil see jääb SeedSigneri RAM-i. Minu puhul tahan ma selle salvestada [Seedkeeper](https://satochip.io/product/seedkeeper/), mis on teine Satochipi toode, mis on mõeldud saladuste säilitamiseks. Kasutan seda seadet viimase abinõuna, juhul kui mu Satochip peaks kaduma.



Siin valitud varundusstrateegia sõltub teie eelistustest, kuid kindlasti peab olema vähemalt üks koopia teie mnemofraasist, kas füüsilisel andmekandjal (paber või metall) või, nagu siin, Seedkeeperis. Te võite ka varukoopiate arvu korrutada vastavalt vajadusele. Lisateabe saamiseks portfelli varundusstrateegiate kohta soovitan lugeda seda õpetust :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Oma seed varundamiseks Seedkeeperil minge otse menüüsse `Backup Seed` (Seedide varundamine).



![Image](assets/fr/17.webp)



Seejärel sisestage oma Seedkeeper kiipkaardilugejasse ja valige "SeedKeeperile".



![Image](assets/fr/18.webp)



Sisestage PIN-kood, et avada see.



![Image](assets/fr/19.webp)



Valige `Silt`, et hõlpsasti identifitseerida oma erinevaid Seedkeeperisse salvestatud saladusi. Võite näiteks lihtsalt säilitada wallet jäljendi või märkida selgesõnaliselt `Seed`. Valik sõltub teie eelistustest ja riskist.



![Image](assets/fr/20.webp)



Kui teie varundusstrateegia tugineb ainult sellele Seedkeeperile, siis soovitan tungivalt käivitada nüüd tühja taastamistesti ja seejärel võrrelda sõrmejälgi, et kontrollida, kas varundamine toimib.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Seedkeeper PIN-kood peaks olema võimalikult pikk ja juhuslik, et vältida toorest jõudu, kui kaart on füüsiliselt ohustatud. Samuti peaksite säilitama selle PIN-koodi varukoopiat, mida hoitakse Seedkeeperist eraldi. Ilma selle PIN-koodita ei pääse te Seedkeeperisse salvestatud müntidele ligi ja teie bitcoinid lähevad lõplikult kaduma.



### 5.3. Säästa seed Satochipil



Nüüd, kui teie portfell on loodud, salvestatud ja kontrollitud, kanname selle üle Satochipile. Selleks veenduge, et seed on laaditud SeedSigneri RAM-i. Seejärel minge menüüsse `Tööriistad > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Sisestage oma Satochip kiipkaardilugejasse ja valige "Initsialiseeri seemnega".



![Image](assets/fr/22.webp)



Seade palub teil sisestada Satochip PIN-koodi; kuna kaart on uus ja mitteinitsialiseeritud, ei ole PIN-koodi veel olemas. Selle sammu vahelejätmiseks sisestage ükskõik milline kood (see ei ole blokeeriv).



![Image](assets/fr/23.webp)



SeedSigner tuvastab, et teie Satochip ei ole initsialiseeritud. Kinnitamiseks klõpsake `I Understanding`.



![Image](assets/fr/24.webp)



Seejärel saate määrata Satochip PIN-koodi, mis võib olla 4 kuni 16 tähemärki. wallet turvalisuse tugevdamiseks valige pikk ja juhuslik kood: see on ainus kaitse füüsilise juurdepääsu vastu teie mnemofraasile.



Ärge unustage, et salvestate selle PIN-koodi kohe pärast selle loomist kas turvalisse paroolihaldurisse või füüsilisele andmekandjale, sõltuvalt teie isiklikust strateegiast. Viimasel juhul ärge kunagi hoidke PIN-koodi sisaldavat kandjat samas kohas kui teie Satochip, vastasel juhul muutub kaitse kasutuks. Oluline on varukoopia olemasolu: **Kui see PIN-kood puudub teil juurdepääs oma seed-le ja teie bitcoinid on igaveseks kadunud**.



![Image](assets/fr/25.webp)



SeedSigner küsib seejärel, millist seed soovite Satochipisse importida. Valige see, mille sõrmejälg vastab äsja loodud portfellile.



![Image](assets/fr/26.webp)



Teie seed on nüüd imporditud Satochippi.



![Image](assets/fr/27.webp)



Nüüd saate oma SeedSigneri välja lülitada.



Kui soovite kasutada passphrase BIP39-i, et suurendada oma wallet turvalisust, vaadake selle õpetuse 6. osa:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Importida wallet Sparrow-sse



Nüüd, kui teie portfell on loodud ja töötab, impordime selle avaliku teabe (*keystore*) Sparrow Wallet või mõnda teise portfellihaldustarkvarasse. Seda tarkvara kasutatakse teie tehingute loomiseks, levitamiseks ja jälgimiseks. Siiski ei saa see neid allkirjastada, kuna ainult Satochip (ja kõik varukoopiad) hoiavad selleks toiminguks vajalikke privaatvõtmeid.



### 6.1 SeedSigneri ja Satochipi ettevalmistamine



Sisestage operatsioonisüsteemi sisaldav microSD-kaart, seejärel lülitage SeedSigner sisse. Hetkel ei saa ta midagi teha, sest ta ei tunne veel teie seed. Te peate alustuseks sisestama Satochipi kiipkaardilugejasse, sest see on see, mis hoiab teie seed-i.



Avakuval avage menüü "Tööriistad > Nutikaardi tööriistad > Satochipi funktsioonid".



![Image](assets/fr/28.webp)



Seejärel klõpsake nuppu `Export Xpub`.



![Image](assets/fr/29.webp)



Valige portfelli tüüp. Meie puhul on tegemist ühe portfelliga: valige `Single Sig`.



![Image](assets/fr/30.webp)



Järgmisena tuleb valida skriptimisstandard. Valige viimane: `Native SegWit`.



![Image](assets/fr/31.webp)



Lõpuks valige "Koordinaator", st portfellihaldustarkvara, mida soovite kasutada. Siinkohal kasutame Sparrow Wallet.



![Image](assets/fr/32.webp)



Ilmub hoiatusteade: see on täiesti normaalne. Laiendatud avalik võti (`xpub`) võimaldab teil vaadata kõiki teie seed (esimesel kontol) saadud aadresse. See ei anna aga juurdepääsu teie rahalistele vahenditele: selle avalikustamine ohustaks teie privaatsust, kuid mitte teie bitcoinide turvalisust. Teisisõnu, see võimaldab teil jälgida oma saldot, kuid mitte kulutada neid.



Klõpsake nuppu "Ma saan aru".



![Image](assets/fr/33.webp)



Seejärel sisestage oma Satochipi PIN-kood, et avada see. See on kood, mille määrasite ja salvestasite punktis 5.



![Image](assets/fr/34.webp)



Lõpuks klõpsake nuppu `Export Xpub`, kui olete kuvatud teabega rahul.



![Image](assets/fr/35.webp)



SeedSigner genereerib seejärel teie xpubi dünaamilise QR-koodi kujul, mis sisaldab kõiki andmeid, mida vajate oma portfelli haldamiseks Sparrow Wallet-s. QR-koodi skaneerimise lihtsustamiseks saate joysticki abil reguleerida ekraani heledust.



### 6.2 Uue portfelli importimine Sparrow Wallet-sse



Veenduge, et tarkvara Sparrow Wallet on teie arvutisse paigaldatud. Kui te ei tea, kuidas seda alla laadida, selle autentsust kontrollida ja õigesti paigaldada, vaadake meie täielikku õpetust sel teemal :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Avage oma arvutis Sparrow Wallet, seejärel klõpsake menüüribal nuppu `Fail → Import Wallet`.



![Image](assets/fr/36.webp)



Liikuge alla "SeedSigner" juurde, seejärel valige "Scan...". Teie veebikaamera aktiveeritakse: skannige SeedSigneri ekraanil kuvatavat dünaamilist QR-koodi.



![Image](assets/fr/37.webp)



Määrake oma portfellile nimi, seejärel klõpsake nuppu "Loo Wallet". Seejärel palub Sparrow teil määrata parool, et lukustada kohalik juurdepääs sellele wallet-le. Valige tugev parool: see kaitseb teie andmeid Sparrow-s (avalikud võtmed, aadressid, sildid ja tehingute ajalugu). Seda parooli ei ole siiski vaja wallet taastamiseks tulevikus: seda on vaja ainult teie mnemooniline fraas (ja võimalik, et ka passphrase).



Soovitan selle parooli salvestada paroolihaldurisse, et vältida selle kaotamist.



![Image](assets/fr/38.webp)



Teie võtmesalvestus on edukalt imporditud.



![Image](assets/fr/39.webp)



Nüüd kontrollige, et Sparrow Wallet-s kuvatav "Master fingerprint" vastab teie SeedSigneril eelnevalt leitud sõrmejäljele.



SeedSigner palub teil seejärel impordi kehtivuse kinnitamiseks skaneerida suvaline vastuvõtuaadress teie Sparrow wallet-st.



![Image](assets/fr/40.webp)



Teie Satochip (SeedSigneri kaudu) ja Sparrow Wallet on nüüd turvaliselt ühendatud. Sparrow toimib täieliku haldusliidesena, samal ajal kui Satochip jääb ainsaks seadmeks, mis on võimeline teie tehinguid allkirjastama. Nüüd olete valmis bitcoinide vastuvõtmiseks ja saatmiseks täiesti õhukindlas konfiguratsioonis.



![Image](assets/fr/41.webp)



## 7. Bitcoinide vastuvõtmine ja saatmine



Teie Satochip ja Sparrow Wallet on nüüd konfigureeritud koos töötama. Selles jaotises selgitame samm-sammult, kuidas selles režiimis bitcoine vastu võtta ja saata.



### 7.1 Bitcoinide vastuvõtmine



#### 7.1.1 Vastuvõtuaadressi genereerimine



Avage oma arvutis Sparrow Wallet ja avage oma `Satochip-SeedSigner` wallet, kasutades oma parooli. Kontrollige, et tarkvara on ühendatud serveriga (indikaator paremal all). Seejärel klõpsake külgribal nupule `Vastuvõtmine`.



![Image](assets/fr/42.webp)



Ilmub uus Bitcoin aadress. Te leiate :




- Aadress tekstiformaadis (alustades `bc1q...`, kui kasutate P2WPKH, nagu selles näites) ;
- Sellega seotud QR-kood ;
- Väli "Label", mis on kasulik tehingute jälgimiseks.



Soovitan tungivalt lisada sildi igale bitcoini kviitungile oma wallet-s. See aitab teil hõlpsasti tuvastada iga UTXO päritolu ja paremini hallata oma privaatsust. Kui soovite selle olulise teema kohta rohkem teada saada, vaadake spetsiaalset koolitust Plan ₿ Akadeemias :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Sildi lisamiseks sisestage lihtsalt nimi väljale "Silt" ja kinnitage.



Näiteks:



```txt
Label : Sale of the Raspberry Pi Zero
```



Teie aadress on nüüd seotud selle märgisega kõigis Sparrow sektsioonides.



![Image](assets/fr/43.webp)



#### 7.1.2 Address kontroll SeedSigneril



Enne vastuvõtuaadressi edastamist maksjale on oluline kontrollida, et see kuuluks teie seed-le. See samm tagab, et teie Satochip saab seejärel allkirjastada selle aadressiga seotud tehinguid. Samuti takistab see võimalikke rünnakuid, mille puhul Sparrow kuvab võltsitud aadressi. Pidage meeles, et Sparrow töötab ebaturvalises keskkonnas (teie arvutis), mille ründepind on palju suurem kui teie Satochipil, mis on täielikult isoleeritud. Seepärast ei tohiks te kunagi pimesi usaldada Sparrow-s kuvatavaid aadresse enne nende kontrollimist wallet riistvaras.



Sparrow-s klõpsake aadressi QR-koodil, et seda suurendada: see kuvatakse siis täisekraanil.



![Image](assets/fr/44.webp)



Sisestage Satochip oma SeedSignerisse, seejärel valige peamenüüst "Skaneerimine". Skaneerige arvutis kuvatavat QR-koodi, seejärel valige `Kasutage Satochip-kaarti`.



![Image](assets/fr/45.webp)



Seejärel kinnitage kasutatava skripti tüüp (antud juhul `Native SegWit`), sisestage selle avamiseks Satochip PIN-kood ja kinnitage `xpub` teave.



![Image](assets/fr/46.webp)



Kui skaneeritud aadress vastab teie seed-st saadud aadressile, kuvab SeedSigner teate: "Address kontrollitud".



![Image](assets/fr/47.webp)



Siis saate olla kindel, et aadress kuulub teie portfelli.



#### 7.1.3 Raha laekumine



Nüüd saate selle aadressi edastada tekstina või QR-koodi kaudu isikule või osakonnale, kes peab teile saatma satss. Kui tehing on võrgus edastatud, ilmub see Sparrow Wallet vahekaardile "Tehingud".



![Image](assets/fr/48.webp)



### 7.2 Saada bitcoine



Bitcoinide saatmine Satochip-SeedSigner-konfiguratsiooniga hõlmab 3 sammu:




- Tehingu loomine Sparrow ;
- Selle tehingu allkirjastamine Satochipil, SeedSigner'i kaudu ;
- Lõpuks edastatakse tehing Sparrow-st üle võrgu.



Kõik andmevahetused kahe seadme vahel toimuvad ainult QR-koodide kaudu.



#### 7.2.1 Tehingu loomine Sparrows



Sparrow Wallet saate luua tehingu, klõpsates vasakpoolsel külgribal vahekaardil "Saada". Ma eelistan siiski kasutada vahekaarti `UTXOs`, mis võimaldab teil praktiseerida *Coin Control*. See meetod pakub täpset kontrolli kulutatud UTXOde üle, et piirata tehingute käigus ilmnevat teavet.



Valige vahekaardil `UTXOs` mündid, mida soovite kulutada, ja seejärel klõpsake nuppu `Sendage valitud`.



![Image](assets/fr/49.webp)



Seejärel täitke tehingu väljad:




- Sisestage jaotises "Maksa aadressile" saaja aadress või skannige tema QR-kood kaamera ikooni abil;
- Lisage lahtrisse "Silt" selle kulu jälgimiseks silt;
- Sisestage lahtrisse "Summa" saadetav summa;
- Lõpuks valige laadimismäär vastavalt praegustele võrgutingimustele (hinnangud on kättesaadavad aadressil [mempool.space](https://mempool.space/)).



Kui olete kõik väljad täitnud, vaadake teave hoolikalt läbi ja klõpsake seejärel nupule "Tehingu loomine >>".



![Image](assets/fr/50.webp)



Kontrollige veel kord tehingu üksikasju, et need oleksid täpsed, seejärel klõpsake "Tehingu allkirjastamiseks lõpuleviimine".



![Image](assets/fr/51.webp)



Tehing on nüüdseks valmis, kuid seda ei ole veel allkirjastatud. [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) kuvamiseks QR-koodina klõpsake nuppu `Show QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Tehingu allkirjastamine Satochipiga



Lülitage oma SeedSigner sisse ja sisestage Satochip nagu tavaliselt. Valige avaekraanilt "Skaneerimine" ja skannige seejärel Sparrow-l kuvatavat QR-koodi.



![Image](assets/fr/53.webp)



Valige valik "Kasuta Satochip-kaarti".



![Image](assets/fr/54.webp)



Sisestage PIN-kood, et avada kiipkaart.



![Image](assets/fr/55.webp)



SeedSigner tuvastab, et tegemist on PSBT-ga, ja kuvab tehingu kokkuvõtte:




   - Saadetud summa,
   - Sihtkoha aadressid,
   - Sellega seotud tehingukulud.



Klõpsake nupule "Vaata üksikasju" ja uurige kogu teavet otse SeedSigneri ekraanil. Kõige olulisemad punktid, mida kontrollida, on saadetud summad, sihtaadressid ja tehingutasud.



![Image](assets/fr/56.webp)



Kui kõik on korras, valige "Kinnita PSBT", et allkirjastada tehing Satochipiga.



![Image](assets/fr/57.webp)



Kui allkirjastamine on lõpule viidud, genereerib SeedSigner uue QR-koodi, mis sisaldab allkirjastatud tehingut ja on valmis Sparrow-ga skaneerimiseks.



#### 7.2.3 Tehingu edastamine Sparrow-st



Nüüd, kui tehing on allkirjastatud ja valideeritud, on vaja seda vaid Bitcoin võrgus edastada, et kaevandaja saaks selle plokki lisada. Sparrows klõpsake nuppu `Scan QR`.



![Image](assets/fr/58.webp)



Esitage veebikaamerale oma SeedSigneril kuvatav QR-kood (see, mis sisaldab allkirjastatud tehingut). Seejärel kuvab Sparrow kõik tehingu üksikasjad. Kontrollige, et kõik andmed oleksid õiged, ja seejärel klõpsake "Broadcast Transaction", et edastada tehing Bitcoin võrgus.



![Image](assets/fr/59.webp)



Teie tehing on nüüd võrku edastatud. Selle kinnitust saate jälgida Sparrow Wallet vahekaardil "Tehingud".



![Image](assets/fr/60.webp)



## 8. Saage oma wallet tagasi



Nagu me eelmistes punktides nägime, on sõltuvalt teie turvastrateegiast lisaks Satochip'ile mitmeid võimalusi oma taastamislausete varundamiseks:




- Kasutades klassikalist *SeedQR* koos SeedSigneriga ;
- Mälusõna füüsilisel andmekandjal salvestamise teel;
- Või salvestades selle seemnehoidjale, nagu on selgitatud punktis 5.2.



Igal juhul on 2 peamist olukorda, mille puhul on vaja sekkuda: Satochipi kadumine või SeedSigneri kadumine. Vaatleme, kuidas reageerida mõlemas nimetatud stsenaariumis.



### 8.1. wallet kättesaamine Satochipiga



Kui teie Satochip on endiselt olemas, kuid teie SeedSigner on katki või kadunud, on olukorda üsna lihtne hallata, sest teie wallet on endiselt Satochipis.



Parim võimalus on soovitada vajalikke komponente ja ehitada uus SeedSigner nullist üles. Kuna tegemist on "olekuta" seadmega, ei ole oluline, kas kasutate sama või teist SeedSignerit: seni, kuni saate oma Satochipi sisestada, töötab kõik normaalselt.



Kui te ei soovi seda ümber ehitada, võite kasutada oma Satochipi ka klassikalisel viisil, st otse arvutist, ilma SeedSigneri kaudu käimata. See meetod töötab suurepäraselt, kuid vähendab oluliselt teie Bitcoin wallet turvalisust: te kaotate "*õhkhaardistatud*" isolatsiooni ja peate nüüd pimesi allkirjastama, kuna SeedSigner toimis usaldusväärse ekraanina. See võib siiski olla ajutine lahendus hädaolukorras või kui te ei saa SeedSignerit ümber ehitada.



Selleks on vaja USB-kiipkaardi või NFC-lugejat. Avage wallet, mida soovite taastada, Sparrow-s, seejärel minge vahekaardile "Seaded" ja klõpsake nuppu "Asendamine".



![Image](assets/fr/61.webp)



Sisestage oma Satochip arvutiga ühendatud kiipkaardilugejasse, seejärel klõpsake "Impordi" kõrval "Satochip".



![Image](assets/fr/62.webp)



Lõpuks sisestage oma kiipkaardi PIN-kood, et avada see. Seejärel saate juurdepääsu oma wallet-le, luua tehinguid ja allkirjastada neid otse ühendatud Satochipi abil.



### 8.2. Saage oma portfell SeedSigneriga kätte



Teine, tundlikum stsenaarium on see, kui kaotate juurdepääsu oma Satochipile, mis sisaldab seed: kas see on katki, kadunud, varastatud või olete unustanud selle PIN-koodi. Kui teie Satochip on varastatud või kadunud, soovitame tungivalt, et kui juurdepääs teie rahalistele vahenditele on taastunud, kannate oma bitcoinid kohe üle täiesti uuele wallet-le, mis on loodud teise seed-ga. See tagab, et võimalik ründaja ei saa kunagi juurdepääsu teie satssidele.



Oma portfellile juurdepääsu taastamiseks ja vahendite liigutamiseks laadige lihtsalt oma seed SeedSignerisse. Sõltuvalt kasutatavast varunduskandjast on teil mitu võimalust:





- Sisestage oma mnemooniline fraas käsitsi menüüs `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Skaneerige oma *SeedQR*, klõpsates avalehel nupule "Skaneerimine".



![Image](assets/fr/64.webp)





- Või laadige oma seed Seedkeeperist menüüst `Seeds > From SeedKeeper` (seda meetodit kasutan ma selles õpetuses). Teil tuleb lihtsalt sisestada Seedkeeper PIN-kood ja valida saladus, mida kasutatakse seed-na SeedSigneril.



![Image](assets/fr/65.webp)



Kui seed on laaditud SeedSignerisse, saate olenemata sellest, millist meetodit kasutate, allkirjastada ühe või mitu skaneerimistehingut, et viia oma bitcoinid uude, kompromiteerimata wallet-i. Kuidas seda teha, leiate järgmise õpetuse osast 7.2:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Nüüd te teate, kuidas kasutada Satochip'i oma Bitcoin portfelli turvaliseks haldamiseks koos SeedSigneriga.



Kui see ülesehitus on teid veennud, siis ärge kõhkle toetamast projekte, mis seda võimaldavad:




- Ostes oma seadmed otse [Satochipi veebisaidilt](https://satochip.io/shop/);
- Tehes [annetuse projektile SeedSigner](https://seedsigner.com/donate/);
- Tellides [Crypto Guide'i YouTube'i kanali](https://www.youtube.com/@CryptoGuide/), mida haldab isik, kes haldab GitHubi repositooriumi, kus asub modifitseeritud püsivara, mida me kasutasime selles õpetuses.