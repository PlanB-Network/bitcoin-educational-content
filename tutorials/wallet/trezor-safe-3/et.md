---
name: Trezor Safe 3
description: Hardware Wallet Safe 3 konfigureerimine ja kasutamine
---
![cover](assets/cover.webp)



*Pildi krediit: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 on SatoshiLabs'i loodud Hardware Wallet, mis loodi 2023. aastal. See on väga kompaktne ja kerge mudel (14 grammi), mis on mõeldud nii algajatele kui ka edasijõudnutele. See on kuulsa Model One'i järeltulija, millel on olulisi täiendusi, säilitades samas brändi avatud lähtekoodiga lähenemisviisi, mis eristab seda tema peamisest konkurendist Ledger. Safe 3 hind on 79 eurot. Seega on see paigutatud Hardware Wallet keskklassi segmenti, konkureerides otseselt Ledger Nano S Plusiga.



Safe 3 ei oma akut ja töötab ainult USB-C-ühenduse kaudu, mida kasutatakse nii toite- kui ka sidepidamiseks. Sellel on väike 0,96-tolline monokroomne OLED-ekraan ja kaks füüsilist nuppu.



![Image](assets/fr/01.webp)



Safe 3 pakub kõiki olulisi funktsioone, mida ühelt healt Hardware Wallet-lt oodatakse, sealhulgas suurepärast passphrase BIP39 integreerimist. Siiski ei toeta see veel Miniscripti.



See mudel sobib eriti hästi algajatele ja võib-olla on see isegi Hardware Wallet, mida ma uuele kasutajale soovitaksin. See sobib hästi ka edasijõudnutele. Teisest küljest ei pruugi see vastata kõigile edasijõudnud kasutajate ootustele, kes otsivad spetsiifilisemaid funktsioone, mis on saadaval sellistes seadmetes nagu Coldcard. Siiski, kui te ei vaja neid täiustatud võimalusi, võib Trezor Safe 3 olla suurepärane valik.



## Trezor Safe 3 ohutusmudel



Trezor Safe 3 on nüüd varustatud EAL6+ sertifikaadiga **Secure Element**, mis on märkimisväärne edasiminek võrreldes eelmiste mudelitega, nagu Model One ja Model T. See on OPTIGA Trust M V3 kiip, mis ei salvesta otseselt seed, vaid toimib krüptograafilise komponendina, et tagada juurdepääs sellele. Turvaline element säilitab saladuse, millele saab juurdepääsu ainult siis, kui kasutaja on PIN-koodi õigesti sisestanud. Seda saladust kasutatakse seejärel seed dekrüpteerimiseks, mis on salvestatud seadme põhimällu krüpteeritult.



See hübriidne turvasüsteem pakub paremat füüsilist kaitset, eelkõige väljavõtete või invasiivse analüüsi vastu, mille suhtes Model One oli vastuvõtlik, eriti PIN-koodi haldamisel. Need nõrgad kohad on nüüd tänu turvalise elemendi kasutamisele kõrvaldatud. Selle mudeli puhul säilitatakse ka avatud lähtekoodiga tarkvaraarhitektuur: kood, mis haldab isiklike võtmete genereerimist ja kasutamist, jääb täielikult kättesaadavaks ja kontrollitavaks. OPTIGA kiip haldab ainult PIN-koodi, mis on Bitcoin Wallet võtmehalduse väline element. See annab välja ainult saladuse, mida saab kasutada seed dekrüpteerimiseks. Samuti on OPTIGA Trust M V3 kiibil suhteliselt vaba litsents, mis lubab SatoshiLabsil vabalt avaldada võimalikke haavatavusi.



See turvamudel on minu arvates üks parimaid kompromisse, mis on täna turul saadaval. See ühendab turvalise elemendi eelised avatud lähtekoodiga tarkvarahaldusega. Varem pidid kasutajad valima kiibiga tugevdatud füüsilise turvalisuse ja avatud lähtekoodiga läbipaistvuse vahel; Trezor Safe 3 puhul on võimalik saada kasu mõlemast.



Selles õpetuses näitame teile, kuidas Trezor Safe 3 turvaliselt seadistada ja kasutada.



## Trezor Safe 3 lahtipakkimine



Kui saate oma Safe 3 kätte, veenduge, et pakend ja Seal on terved, et kinnitada, et pakendit ei ole avatud. Seadme autentsuse ja terviklikkuse tarkvaraline kontroll toimub ka seadme hilisemal seadistamisel.



Karbi sisu sisaldab:




- Trezor Safe 3;
- Kott, mis sisaldab kaardimaterjali oma Mnemonic fraasi, kleebiste ja juhiste salvestamiseks;
- USB-C USB-C kaablile.



![Image](assets/fr/02.webp)



Avamisel peaks teie Trezor Safe 3 olema kaitstud kaitsekilega ja USB-C port peaks olema kaitstud hologrammiga Seal. Veenduge, et see on olemas.



![Image](assets/fr/03.webp)



Seadmes navigeerimine on lihtne: paremale kerimiseks kasutage parempoolset nuppu ja vasakule kerimiseks vasakut nuppu. Tegevuse kinnitamiseks vajutage mõlemat nuppu korraga.



![Image](assets/fr/04.webp)



## Eeltingimused



Selles õpetuses näitan teile, kuidas kasutada Trezor Safe 3 koos [Sparrow Wallet portfellihaldustarkvaraga](https://sparrowwallet.com/download/). Kui te ei ole seda tarkvara veel paigaldanud, siis palun tehke seda kohe. Kui vajate abi, on meil ka üksikasjalik õpetus Sparrow Wallet seadistamise kohta :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Samuti on vaja Trezor Suite'i tarkvara, et konfigureerida Safe 3, kontrollida selle autentsust ja paigaldada püsivara. Kasutame seda tarkvara ainult selleks ja pärast seda on seda vaja ainult püsivara uuendamiseks. Wallet igapäevaseks haldamiseks kasutame eranditult Sparrow Wallet, kuna see on optimeeritud Bitcoin jaoks ja seda on lihtne kasutada isegi algajatele (Sparrow toetab ainult Bitcoin, mitte altcoine).



[Lae Trezor Suite alla ametlikust veebisaidist](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Nende mõlema programmi puhul soovitan tungivalt kontrollida nii nende autentsust (GnuPG abil) kui ka terviklikkust (Hash abil) enne nende paigaldamist oma masinasse. Kui te ei tea, kuidas seda teha, võite jälgida seda teist õpetust :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 3 käivitamine



Ühendage oma Safe 3 arvutiga, kuhu on juba paigaldatud Trezor Suite ja Sparrow Wallet.



![Image](assets/fr/06.webp)



Avage Trezor Suite, seejärel klõpsake nupule "*Set up my Trezor*".



![Image](assets/fr/07.webp)



Valige "*Bitcoin-only firmware*", seejärel klõpsake "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



Trezor Suite installib seejärel püsivara teie seadmesse Safe 3. Palun oodake installimise ajal.



![Image](assets/fr/09.webp)



Klõpsake nuppu "*Jätka*".



![Image](assets/fr/10.webp)



Seejärel jätkake autentsuse kontrollimist, et veenduda, et teie Hardware Wallet ei ole võltsitud või kompromiteeritud.



![Image](assets/fr/11.webp)



Kinnitamiseks vajutage oma Safe 3 seadmel parempoolset nuppu.



![Image](assets/fr/12.webp)



Kui teie Trezor on ehtne, ilmub Trezor Suite'is kinnitussõnum.



![Image](assets/fr/13.webp)



Seejärel võite vahele jätta aknad põhiliste kasutusjuhenditega.



![Image](assets/fr/14.webp)



## Bitcoin portfelli loomine



Klõpsake Trezor Suite'is nupule "*Loo uus Wallet*".



![Image](assets/fr/15.webp)



Standardportfelli puhul saate valida vaikimisi varundustüübi. See loob klassikalise ühe sümboliga portfelli, millel on 12-sõnaline Mnemonic fraas. Klõpsake nuppu "*Loo Wallet*".



Kui soovite rohkem teada saada teiste Trezori pakutavate varundusvõimaluste, sealhulgas *Multi-share Backup* kohta, siis soovitan teil tutvuda ka selle õpetusega :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Nõustuge Hardware Wallet kasutustingimustega.



![Image](assets/fr/17.webp)



Uue portfelli loomiseks vajutage uuesti parempoolset nuppu.



![Image](assets/fr/18.webp)



Trezor Suite'is klõpsake nuppu "*Vajuta varundamist*".



![Image](assets/fr/19.webp)



Tarkvara annab juhiseid Mnemonic fraasi haldamiseks.



See Mnemonic annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda lauset valdab, võib teie raha varastada, isegi ilma füüsilise juurdepääsuta teie Trezor Safe 3-le.



12-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie Hardware Wallet kaob, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.



Võite kirjutada selle karbis olevale papile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.



Kinnitage juhised, seejärel klõpsake nupule "*Loo Wallet varukoopia*".



![Image](assets/fr/20.webp)



Safe 3 loob teie Mnemonic fraasi, kasutades oma juhusliku numbrigeneraatorit. Veenduge, et teid ei jälgita selle toimingu ajal. Kirjutage ekraanil esitatud sõnad enda valitud füüsilisele andmekandjale. Sõltuvalt teie turvastrateegiast võite kaaluda fraasi mitmete täielike füüsiliste koopiate tegemist (kuid eelkõige ärge jagage seda). Oluline on hoida sõnad nummerdatud ja järjestikku.



***Es on selge, et te ei tohi neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidist Wallet kasutatakse ainult Testnet peal ja see kustutatakse õpetuse lõpus



Lisateavet selle kohta, kuidas oma Mnemonic fraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Järgmiste sõnade juurde liikumiseks tehke paremklõps. Tagasi saate minna, klõpsates vasakule nupule. Kui olete kõik sõnad üles kirjutanud, hoidke all parempoolset nuppu, et liikuda järgmise sammu juurde.



![Image](assets/fr/22.webp)



Valige oma Mnemonic lause sõnad vastavalt nende järjekorrale, et veenduda, et olete need õigesti üles kirjutanud. Kasutage ettepanekute vahel navigeerimiseks vasakut ja paremat nuppu, seejärel valige õige sõna, klõpsates kahel nupul samaaegselt.



![Image](assets/fr/23.webp)



Kui see kontrollimise protseduur on lõpule viidud, klõpsake paremal asuval nupul.



![Image](assets/fr/24.webp)



## PIN-koodi seadistamine



Järgneb PIN-koodi samm. PIN-kood avab teie Trezori lukustuse. Seega pakub see kaitset volitamata füüsilise juurdepääsu eest. See PIN-kood ei ole seotud teie Wallet krüptograafiliste võtmete tuletamisega. Seega isegi ilma PIN-koodile juurdepääsuta võimaldab teie 12-sõnalise Mnemonic fraasi omamine taastada juurdepääsu oma bitcoinidele.



Trezor Suite'is klõpsake nupule "*Jätka PIN-koodi*", seejärel nupule "*Set PIN*".



![Image](assets/fr/25.webp)



Kinnitage Safe 3.



![Image](assets/fr/26.webp)



Soovitame valida võimalikult juhusliku PIN-koodi. Salvesta see kood kindlasti sellesse kohta, mis ei ole sinu Trezori salvestamise koht (nt paroolihaldurisse). PIN-koodi saate määrata 8 kuni 50-kohalise PIN-koodi. Turvalisuse suurendamiseks soovitan valida võimalikult pikk PIN-kood.



Kasutage iga numbri valimiseks vasakut ja paremat nuppu. Valiku kinnitamiseks ja järgmise numbri juurde liikumiseks vajutage mõlemat nuppu korraga.



![Image](assets/fr/27.webp)



Kui olete lõpetanud, klõpsake numbrite alguses olevale "*ENTER*" märkele ja kinnitage PIN-kood teist korda.



![Image](assets/fr/28.webp)



Teie PIN-kood on registreeritud.



![Image](assets/fr/29.webp)



Klõpsake Trezor Suite'is nupule "*Complete setup*".



![Image](assets/fr/30.webp)



Teie Safe 3 seadistamine on nüüd lõpule viidud. Soovi korral saate muuta oma Hardware Wallet nime ja kodulehte.



![Image](assets/fr/31.webp)



Me ei vaja enam Trezor Suite'i tarkvara, v.a. selleks, et teha oma Hardware Wallet-le regulaarselt püsivara uuendusi või kui soovite teha taastamistesti. Nüüd hakkame portfelli haldamiseks kasutama Sparrow'd, sest see tarkvara sobib suurepäraselt ainult Bitcoin kasutamiseks.



## Portfelli seadistamine Sparrow Wallet-süsteemis



Alustage Sparrow Wallet allalaadimisest ja installimisest [ametlikust veebisaidist](https://sparrowwallet.com/) oma arvutisse, kui te seda veel teinud ei ole.



Kui olete avanud Sparrow Wallet, veenduge, et tarkvara on ühendatud Bitcoin sõlmpunktiga, mida näitab Interface paremas alumises nurgas olev märkeruut. Kui teil on probleeme Sparrow'ga ühendamisega, soovitan teil lugeda selle õpetuse algust:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klõpsake vahekaardil "*Fail*" ja seejärel "*Uus Wallet*".



![Image](assets/fr/32.webp)



Andke oma portfellile nimi ja klõpsake seejärel nupule "*Loo Wallet*".



![Image](assets/fr/33.webp)



Valige rippmenüüst "*Skripti tüüp*" skripti tüüp, mida kasutatakse teie bitcoinide kaitsmiseks. Soovitan "*Taproot*" või selle puudumisel "*Native SegWit*".



![Image](assets/fr/34.webp)



Klõpsake nupule "*Connected Hardware Wallet*". Teie Safe 3 peab muidugi olema arvutiga ühendatud ja lukustamata.



![Image](assets/fr/35.webp)



Vajutage nupule "*Scan*". Teie Safe 3 peaks ilmuma. Klõpsake nupule "*Import Keystore*".



![Image](assets/fr/36.webp)



Nüüd näete oma Wallet üksikasju, sealhulgas oma esimese konto laiendatud avalikku võtit. Wallet loomise lõpuleviimiseks klõpsake nuppu "*Kandideeri*".



![Image](assets/fr/37.webp)



Valige tugev parool, et tagada juurdepääs Sparrow Wallet-le. See parool tagab turvalise juurdepääsu teie Sparrow Wallet andmetele, kaitstes teie avalikke võtmeid, aadresse, silte ja tehingulugu volitamata juurdepääsu eest.



Soovitan teil salvestada see parool paroolihaldurisse, et te seda ei unustaks.



![Image](assets/fr/38.webp)



Ja nüüd on teie portfell imporditud Sparrow Wallet-sse!



![Image](assets/fr/39.webp)



Enne kui saate oma esimesed bitcoinid Wallet-sse, **soovitan teil tungivalt teha tühja taastamistesti**. Kirjutage üles mõned võrdlusandmed, näiteks oma xpub, ja seejärel lähtestage oma Trezor Safe 3, kui Wallet on veel tühi. Seejärel proovige taastada oma Wallet Trezoril, kasutades oma paberkandjal varukoopiaid. Kontrollige, kas pärast taastamist loodud xpub vastab sellele, mille te algselt üles kirjutasite. Kui see vastab, võite olla kindel, et teie paberkandjal varukoopiad on usaldusväärsed.



Kui soovite rohkem teada saada, kuidas teha taastamistesti, soovitan teil tutvuda selle teise õpetusega:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kuidas ma saan Trezor Safe 3 abil bitcoin'e vastu võtta?



Klõpsake Sparrow's vahekaardil "*Vastuvõtmine*".



![Image](assets/fr/40.webp)



Enne Sparrow Wallet pakutud Address kasutamist kontrollige seda oma Trezori ekraanil. See praktika võimaldab teil kinnitada, et Sparrow'l kuvatav Address ei ole pettus ja et Hardware Wallet on tõepoolest selle Address abil tagatud bitcoinide hilisemaks kulutamiseks vajaliku privaatvõtme omanikuks. See aitab teil vältida mitut liiki rünnakuid.



Selle kontrolli teostamiseks klõpsake nupul "*Ekraan Address*".



![Image](assets/fr/41.webp)



Kontrollige, et teie Trezoril kuvatav Address vastab Sparrow Wallet-le. Samuti on soovitatav teha see kontroll vahetult enne oma Address edastamist saatjale, et olla kindel selle kehtivuses. Kinnitamiseks võite kasutada nuppe.



![Image](assets/fr/42.webp)



Seejärel saate lisada "*Label*", et kirjeldada bitcoinide allikat, mida selle Address-ga kaitstakse. See on hea tava, mis võimaldab teil oma UTXOsid paremini hallata.



![Image](assets/fr/43.webp)



Seejärel saate seda Address kasutada bitcoinide saamiseks.



![Image](assets/fr/44.webp)



## Kuidas saata bitcoine Trezor Safe 3 abil?



Nüüd, kui olete saanud oma esimese Satsi oma Safe 3-ga tagatud Wallet-le, võite neid ka kulutada! Ühendage oma Trezor arvutiga, avage see PIN-koodi abil, käivitage Sparrow Wallet, seejärel minge uue tehingu koostamiseks vahekaardile "*Send*".



![Image](assets/fr/45.webp)



Kui soovite *Mündikontrolli*, st valida konkreetselt, milliseid UTXOsid tehingus tarbida, minge vahekaardile "*UTXOd*". Valige UTXO-d, mida soovite kulutada, ja klõpsake seejärel nupule "*Send Selected*". Teid suunatakse tagasi samale ekraanile vahekaardile "*Send*", kuid teie UTXO-d on juba valitud tehingu jaoks.



![Image](assets/fr/46.webp)



Sisestage sihtkoht Address. Võite sisestada ka mitu aadressi, klõpsates nupule "*+ Add*".



![Image](assets/fr/47.webp)



Kirjutage "*Silt*", et meeles pidada selle kulu eesmärki.



![Image](assets/fr/48.webp)



Valige sellele Address-le saadetav summa.



![Image](assets/fr/49.webp)



Kohandage oma tehingu tasumäär vastavalt praegusele turule. Näiteks võite kasutada [Mempool.space](https://Mempool.space/), et valida sobiv tasumäär.



Veenduge, et kõik tehingu parameetrid on õiged, seejärel klõpsake "*Loo tehing*".



![Image](assets/fr/50.webp)



Kui olete kõigega rahul, klõpsake nuppu "*Tehingu allkirjastamiseks lõpuleviimine*".



![Image](assets/fr/51.webp)



Klõpsake nuppu "*Sign*".



![Image](assets/fr/52.webp)



Klõpsake Trezor Safe 3 kõrval nupule "*Sign*".



![Image](assets/fr/53.webp)



Kontrollige oma Hardware Wallet ekraanil tehingu parameetrid, sealhulgas vastuvõtva Address vastuvõtja, saadetud summa ja tasu. Kui tehing on Trezoril kontrollitud, vajutage allakirjutamiseks mõlemale nupule korraga.



![Image](assets/fr/54.webp)



Teie tehing on nüüd allkirjastatud. Kontrollige veelkord, et kõik on korras, seejärel klõpsake "*Broadcast Transaction*", et edastada see Bitcoin võrgus.



![Image](assets/fr/55.webp)



Selle leiate Sparrow Wallet vahekaardilt "*Tehingud*".



![Image](assets/fr/56.webp)



Palju õnne, te olete nüüd kursis Trezor Safe 3 ja Sparrow Wallet põhikasutusega! Et minna sammu võrra kaugemale, soovitan seda põhjalikku õpetust Hardware Wallet Trezori ja passphrase BIP39 kasutamise kohta, et suurendada teie ohutust:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite allpool Green pöidla. Jagage seda artiklit julgelt oma suhtlusvõrgustikes. Tänan teid väga!