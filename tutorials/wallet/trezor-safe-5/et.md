---
name: Trezor Safe 5
description: Hardware Wallet Safe 5 konfigureerimine ja kasutamine
---
![cover](assets/cover.webp)



*Pildi krediit: [Trezor.io](https://trezor.io/)*



Trezor Safe 5 on SatoshiLabs'i loodud ja 2024. aastal turule toodud viimase põlvkonna Hardware Wallet. See on positsioneeritud kui Safe 3 kõrgekvaliteediline versioon, mille puhul on keskendutud ergonoomikale ja vastupidavusele. See kasutab samu ohutusalaseid eeliseid, mis tema eelkäija Safe 3, võrreldes Model One ja Model T.



Safe 5, mille hind on 169 eurot, on paigutatud kõrgekvaliteedilise Hardware Wallet kategooriasse, konkureerides selliste mudelitega nagu Coldcard, Ledger Nano X ja Flex, Jade Plus, Passport ja Bitbox.



Safe 5 paistab silma 1,54-tollise värvilise puuteekraaniga, mida kaitseb *Gorilla Glass 3*, mis on vastupidav löökidele ja kriimustustele. Samuti on see varustatud *Trezor Touch* haptilise mootoriga, mis tekitab puudutamisel väikeseid vibratsioone. Nagu ka Safe 3, sisaldab see turvalist elementi ja töötab USB-C ühenduse kaudu, millele on lisatud Micro SD port.



Peamine erinevus Safe 3 ja Safe 5 vahel seisneb lisaks ohutusaspektidele ka seadme kvaliteedis. See parandab oluliselt kasutajakogemust, kuna töö on sujuvam ja ekraan on mugavam. Ohutuse poolest on see samaväärne.



![Image](assets/fr/01.webp)



Safe 5-l on kõik olulised funktsioonid, mida te ootate healt Hardware Wallet-lt, sealhulgas suurepärane integreerimine passphrase BIP39-ga. Siiski ei toeta see veel Miniscripti.



See mudel sobib eriti hästi algajatele ja edasijõudnutele. Teisest küljest ei pruugi see vastata kõigi nende edasijõudnud kasutajate ootustele, kes otsivad rohkem spetsiifilisi funktsioone, mis on saadaval sellistes seadmetes nagu Coldcard. Siiski, kui te ei vaja neid täiustatud võimalusi, võib Trezor Safe 5 olla suurepärane valik.



## Trezor Safe 5 ohutusmudel



Nagu ka Safe 3, on Trezor Safe 5 varustatud EAL6+ sertifikaadiga **Secure Element**, mis on märkimisväärne edusamm võrreldes varasemate mudelitega, nagu Model One ja Model T. See on OPTIGA Trust M V3 kiip, mis ei salvesta otseselt seed, vaid toimib krüptograafilise komponendina, et tagada juurdepääs sellele. Turvaline element säilitab saladuse, millele saab juurdepääsu ainult siis, kui kasutaja on PIN-koodi õigesti sisestanud. Seda saladust kasutatakse seejärel seed dekrüpteerimiseks, mis on salvestatud seadme põhimällu krüpteerituna.



See hübriidne turvasüsteem pakub paremat füüsilist kaitset, eelkõige väljavõtete või invasiivse analüüsi vastu, mille suhtes Model One oli vastuvõtlik, eriti PIN-koodi haldamisel. Need nõrgad kohad on nüüd tänu turvalise elemendi kasutamisele kõrvaldatud. Selle mudeli puhul säilitatakse ka avatud lähtekoodiga tarkvaraarhitektuur: kood, mis haldab isiklike võtmete genereerimist ja kasutamist, jääb täielikult kättesaadavaks ja kontrollitavaks. OPTIGA kiip haldab ainult PIN-koodi, mis on Bitcoin Wallet võtmehalduse väline element. See piirdub saladuse avaldamisega, mida saab kasutada seed dekrüpteerimiseks. Samuti on OPTIGA Trust M V3 kiibil suhteliselt vaba litsents, mis lubab SatoshiLabsil vabalt avaldada võimalikke haavatavusi (NDA-Free).



See turvamudel on minu arvates üks parimaid kompromisse, mis on täna turul saadaval. See ühendab turvalise elemendi eelised avatud lähtekoodiga tarkvarahaldusega. Varem pidid kasutajad valima kiibiga tugevdatud füüsilise turvalisuse ja avatud lähtekoodiga läbipaistvuse vahel; Trezor Safe'i puhul on võimalik saada kasu mõlemast.



Selles õpetuses saate teada, kuidas Trezor Safe 5 turvaliselt konfigureerida ja kasutada.



## Trezor Safe 5 lahtipakkimine



Kui saate oma Safe 5 kätte, veenduge, et pakend ja Seal on terved, et kinnitada, et pakendit ei ole avatud. Seadme autentsuse ja terviklikkuse tarkvaraline kontroll toimub ka seadme hilisemal seadistamisel.



Karbi sisu sisaldab:




- Trezor Safe 5;
- Kott, mis sisaldab kaardimaterjali oma Mnemonic fraasi, kleebiste ja juhiste salvestamiseks;
- USB-C USB-C kaablile.



Avamisel peaks teie Trezor Safe 5 olema kaitstud kaitsekilega ja USB-C port peaks olema kaitstud hologrammiga Seal. Veenduge, et see on olemas.



![Image](assets/fr/02.webp)



Seadme navigeerimine on üsna intuitiivne:




- Edasi liikumiseks puudutage ekraani alumist poolt;
- Libistage alla, et minna tagasi ;
- Vajutage ja hoidke ekraani all, et kinnitada toiming.



## Eeltingimused



Selles õpetuses näitan teile, kuidas kasutada Trezor Safe 5 koos [Sparrow Wallet portfellihaldustarkvaraga](https://sparrowwallet.com/download/). Kui te ei ole seda tarkvara veel paigaldanud, siis palun tehke seda kohe. Kui vajate abi, on meil ka üksikasjalik õpetus Sparrow Wallet seadistamise kohta :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Samuti on vaja Trezor Suite'i tarkvara, et konfigureerida Safe 5, kontrollida selle autentsust ja paigaldada püsivara. Kasutame seda tarkvara ainult selleks ja pärast seda on seda vaja ainult püsivara uuendamiseks. Wallet igapäevaseks haldamiseks kasutame eranditult Sparrow Wallet, kuna see on optimeeritud Bitcoin jaoks ja seda on lihtne kasutada isegi algajatele (Sparrow toetab ainult Bitcoin, mitte altcoine).



[Lae Trezor Suite alla ametlikust veebisaidist](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Nende mõlema programmi puhul soovitan tungivalt kontrollida nii nende autentsust (GnuPG abil) kui ka terviklikkust (Hash abil) enne nende paigaldamist oma masinasse. Kui te ei tea, kuidas seda teha, võite jälgida seda teist õpetust :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 5 käivitamine



Ühendage oma Safe 5 arvutiga, kuhu on juba paigaldatud Trezor Suite ja Sparrow Wallet.



![Image](assets/fr/04.webp)



Avage Trezor Suite, seejärel klõpsake nupule "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Valige "*Bitcoin-only firmware*", seejärel klõpsake "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite installib seejärel püsivara teie seadmesse Safe 5. Palun oodake installimise ajal.



![Image](assets/fr/07.webp)



Klõpsake nuppu "*Jätka*".



![Image](assets/fr/08.webp)



Seejärel jätkake autentsuse kontrollimist, et veenduda, et teie Hardware Wallet ei ole võltsitud või kompromiteeritud.



![Image](assets/fr/09.webp)



Kinnitamiseks vajutage oma Safe 5 ekraanile.



![Image](assets/fr/10.webp)



Kui teie Trezor on ehtne, ilmub Trezor Suite'is kinnitussõnum.



![Image](assets/fr/11.webp)



Seejärel võite vahele jätta aknad põhiliste kasutusjuhenditega.



![Image](assets/fr/12.webp)



## Bitcoin portfelli loomine



Klõpsake Trezor Suite'is nupule "*Loo uus Wallet*".



![Image](assets/fr/13.webp)



Standardse BIP39 Wallet loomiseks valige kõigepealt rippmenüüst "*Legacy Wallet backup types*", seejärel valige 12- või 24-sõnaline Mnemonic fraas (praegu soovitatakse 12 sõna). See võimaldab teil luua klassikalise ühe signeeringuga portfelli. Soovitan teil siin valida BIP39-ga kooskõlas olevad parameetrid, et hõlbustada otsingut ja vältida piiranguid konkreetsele keskkonnale. Lõpetamiseks klõpsake nupule "*Loo Wallet*".



Kui soovite rohkem teada saada teiste Trezori pakutavate varundusvõimaluste, sealhulgas *Multi-share Backup* kohta, siis soovitan teil tutvuda ka selle õpetusega :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Nõustuge Hardware Wallet kasutustingimustega.



![Image](assets/fr/15.webp)



Uue portfelli loomiseks vajutage ja hoidke ekraani all.



![Image](assets/fr/16.webp)



Trezor Suite'is klõpsake nuppu "*Vajuta varundamist*".



![Image](assets/fr/17.webp)



Tarkvara annab juhiseid Mnemonic fraasi haldamiseks.



See Mnemonic annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda lauset valdab, võib teie raha varastada, isegi ilma füüsilise juurdepääsuta teie Trezor Safe 5-le.



12-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie Hardware Wallet kaob, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.



Võite kirjutada selle karbis olevale papile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.



Kinnitage juhised, seejärel klõpsake nupule "*Loo Wallet varukoopia*".



![Image](assets/fr/18.webp)



Safe 5 loob teie Mnemonic fraasi, kasutades oma juhusliku numbrigeneraatorit. Veenduge, et teid ei jälgita selle toimingu ajal. Kirjutage ekraanil esitatud sõnad enda valitud füüsilisele andmekandjale. Sõltuvalt teie turvastrateegiast võite kaaluda fraasi mitmete täielike füüsiliste koopiate tegemist (kuid eelkõige ärge jagage seda). Oluline on hoida sõnad nummerdatud ja järjestikku.



***Es on selge, et te ei tohi neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidist Wallet kasutatakse ainult Testnet peal ja see kustutatakse õpetuse lõpus



Lisateavet selle kohta, kuidas oma Mnemonic fraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Järgmiste sõnade juurde liikumiseks klõpsake ekraani allosas. Tagasi saate minna, libistades allapoole. Kui olete kõik sõnad üles kirjutanud, hoidke sõrme ekraanil, et liikuda edasi järgmise sammu juurde.



![Image](assets/fr/20.webp)



Valige oma Mnemonic lause sõnad vastavalt nende järjekorrale, et veenduda, et olete need õigesti üles kirjutanud.



![Image](assets/fr/21.webp)



Kui see kontrollimisprotseduur on lõpetatud, klõpsake ekraanil, et jätkata.



![Image](assets/fr/22.webp)



## PIN-koodi seadistamine



Järgneb PIN-koodi samm. PIN-kood avab teie Trezori lukustuse. Seega pakub see kaitset volitamata füüsilise juurdepääsu eest. See PIN-kood ei ole seotud teie Wallet krüptograafiliste võtmete tuletamisega. Seega isegi ilma PIN-koodile juurdepääsuta võimaldab teie 12-sõnalise Mnemonic fraasi omamine taastada juurdepääsu oma bitcoinidele.



Trezor Suite'is klõpsake nupule "*Jätka PIN-koodi*", seejärel nupule "*Set PIN*".



![Image](assets/fr/23.webp)



Kinnitage Safe 5.



![Image](assets/fr/24.webp)



Soovitame valida võimalikult juhusliku PIN-koodi. Salvesta see kood kindlasti sellesse kohta, mis ei ole sinu Trezori salvestamise koht (nt paroolihaldurisse). PIN-koodi saate määrata 8 kuni 50-kohalise PIN-koodi. Turvalisuse suurendamiseks soovitan valida võimalikult pikk PIN-kood.



PIN-koodi sisestamiseks kasutage puuteplaati.



![Image](assets/fr/25.webp)



Kui olete lõpetanud, klõpsake paremal allosas Green märkeribal, seejärel kinnitage PIN-kood teist korda.



![Image](assets/fr/26.webp)



Teie PIN-kood on registreeritud.



![Image](assets/fr/27.webp)



Klõpsake Trezor Suite'is nupule "*Complete setup*".



![Image](assets/fr/28.webp)



Teie Safe 5 seadistamine on nüüd lõpule viidud. Soovi korral saate muuta oma Hardware Wallet nime ja avalehte.



![Image](assets/fr/29.webp)



Me ei vaja enam Trezor Suite'i tarkvara, v.a. selleks, et teha oma Hardware Wallet-le korrapäraseid püsivara uuendusi või kui soovite teha taastamistesti. Nüüd hakkame portfelli haldamiseks kasutama Sparrow'd, sest see tarkvara sobib suurepäraselt ainult Bitcoin kasutamiseks.



## Sparrow Wallet portfelli seadistamine



Alustage Sparrow Wallet allalaadimisest ja installimisest [ametlikust veebisaidist](https://sparrowwallet.com/) oma arvutisse, kui te seda veel ei ole teinud.



Kui olete avanud Sparrow Wallet, veenduge, et tarkvara on ühendatud Bitcoin sõlmpunktiga, mida näitab Interface paremas alumises nurgas olev märkeruut. Kui teil on probleeme Sparrow ühendamisega, soovitan teil tutvuda selle õpetuse algusega:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klõpsake vahekaardil "*Fail*" ja seejärel "*Uus Wallet*".



![Image](assets/fr/30.webp)



Andke oma portfellile nimi ja klõpsake seejärel nupule "*Loo Wallet*".



![Image](assets/fr/31.webp)



Valige rippmenüüst "*Skripti tüüp*" skripti tüüp, mida kasutatakse teie bitcoinide kaitsmiseks. Soovitan "*Taproot*" või selle puudumisel "*Native SegWit*".



![Image](assets/fr/32.webp)



Klõpsake nupule "*Connected Hardware Wallet*". Teie Safe 5 peab muidugi olema arvutiga ühendatud ja lukustamata.



Kui ühendate oma Safe 5 arvutiga, kus on avatud Sparrow Wallet, palutakse teil Hardware Wallet ekraanil sisestada passphrase BIP39. Seda täiustatud võimalust käsitletakse ühes tulevases õppematerjalis. Praegu võite lihtsalt klõpsata parempoolses ülemises nurgas olevale Green märkele, et kinnitada, et soovite kasutada tühja passphrase (st ilma passphrase-ta). Selleks, et Trezor ei küsiks iga kord käivitamisel passphrase sisestamist, minge Trezor Suite'i, sisenege seadistustesse ja muutke valikut "*Device*" > "*Wallet vaikimisi*" "*Standard*" asemel "*passphrase*".



![Image](assets/fr/33.webp)



Vajutage nupule "*Scan*". Teie Safe 5 peaks ilmuma. Klõpsake nupule "*Import Keystore*".



![Image](assets/fr/34.webp)



Nüüd näete oma Wallet üksikasju, sealhulgas oma esimese konto laiendatud avalikku võtit. Wallet loomise lõpuleviimiseks klõpsake nuppu "*Kandideeri*".



![Image](assets/fr/35.webp)



Valige tugev parool, et tagada juurdepääs Sparrow Wallet-le. See parool tagab turvalise juurdepääsu teie Sparrow Wallet andmetele, kaitstes teie avalikke võtmeid, aadresse, silte ja tehingulugu volitamata juurdepääsu eest.



Soovitan teil salvestada see parool paroolihaldurisse, et te seda ei unustaks.



![Image](assets/fr/36.webp)



Ja nüüd on teie portfell imporditud Sparrow Wallet-i!



![Image](assets/fr/37.webp)



Enne esimeste bitcoinide saamist Wallet-sse, ** soovitan teil tungivalt teha tühja taastamise test**. Kirjutage üles mõned võrdlusandmed, näiteks oma xpub, ja seejärel lähtestage oma Trezor Safe 5, kui Wallet on veel tühi. Seejärel proovige taastada oma Wallet Trezoril, kasutades oma paberkandjal varukoopiaid. Kontrollige, kas pärast taastamist loodud xpub vastab sellele, mille te algselt üles kirjutasite. Kui see vastab, võite olla kindel, et teie paberkandjal varukoopiad on usaldusväärsed.



Kui soovite rohkem teada saada, kuidas teha taastamistesti, soovitan teil tutvuda selle teise õpetusega:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kuidas ma saan Trezor Safe 5 abil bitcoin'e vastu võtta?



Klõpsake Sparrow's vahekaardil "*Vastuvõtmine*".



![Image](assets/fr/38.webp)



Enne Sparrow Wallet pakutud Address kasutamist kontrollige seda oma Trezori ekraanil. See praktika võimaldab teil kinnitada, et Sparrow'l kuvatav Address ei ole pettus ja et Hardware Wallet on tõepoolest selle Address abil tagatud bitcoinide hilisemaks kulutamiseks vajaliku privaatvõtme omanikuks. See aitab teil vältida mitut liiki rünnakuid.



Selle kontrolli teostamiseks klõpsake nuppu "*Kuvada Address*".



![Image](assets/fr/39.webp)



Kontrollige, et teie Trezoril kuvatav Address vastab Sparrow Wallet-le. Samuti on soovitatav teha see kontroll vahetult enne oma Address saatjale edastamist, et olla kindel selle kehtivuses. Kinnitamiseks võite vajutada ekraanile.



![Image](assets/fr/40.webp)



Seejärel saate lisada "*Label*", et kirjeldada bitcoinide allikat, mida selle Address abil kaitstakse. See on hea tava, mis võimaldab teil oma UTXOsid paremini hallata.



![Image](assets/fr/41.webp)



Seejärel saate seda Address kasutada bitcoinide saamiseks.



![Image](assets/fr/42.webp)



## Kuidas saata bitcoine Trezor Safe 5 abil?



Nüüd, kui olete saanud oma esimese Satsi oma Safe 5-ga tagatud Wallet-ga, võite neid ka kulutada! Ühendage oma Trezor arvutiga, avage see PIN-koodiga, käivitage Sparrow Wallet, seejärel minge vahekaardile "*Send*", et luua uus tehing.



![Image](assets/fr/43.webp)



Kui soovite *Mündikontrolli*, st valida konkreetselt, milliseid UTXOsid tehingus tarbida, minge vahekaardile "*UTXOd*". Valige UTXO-d, mida soovite kulutada, ja klõpsake seejärel nupule "*Send Selected*". Teid suunatakse tagasi samale ekraanile vahekaardile "*Send*", kuid teie UTXO-d on juba valitud tehingu jaoks.



![Image](assets/fr/44.webp)



Sisestage sihtkoht Address. Võite sisestada ka mitu aadressi, klõpsates nupule "*+ Add*".



![Image](assets/fr/45.webp)



Kirjutage "*Silt*", et meeles pidada selle kulu eesmärki.



![Image](assets/fr/46.webp)



Valige sellele Address-le saadetav summa.



![Image](assets/fr/47.webp)



Kohandage oma tehingu tasumäär vastavalt praegusele turule. Näiteks võite kasutada [Mempool.space](https://Mempool.space/), et valida sobiv tasumäär.



Veenduge, et kõik tehingu parameetrid on õiged, seejärel klõpsake "*Loo tehing*".



![Image](assets/fr/48.webp)



Kui olete kõigega rahul, klõpsake nuppu "*Tehingu allkirjastamiseks lõpuleviimine*".



![Image](assets/fr/49.webp)



Klõpsake nuppu "*Sign*".



![Image](assets/fr/50.webp)



Klõpsake Trezor Safe 5 kõrval nupule "*Sign*".



![Image](assets/fr/51.webp)



Kontrollige oma Hardware Wallet ekraanil tehingu parameetreid, sealhulgas vastuvõtva Address vastuvõtja, saadetud summa ja tasu. Kui tehing on Trezoril kontrollitud, vajutage ja hoidke ekraanil allkirja.



![Image](assets/fr/52.webp)



Teie tehing on nüüd allkirjastatud. Kontrollige veelkord, et kõik on korras, seejärel klõpsake "*Tehingu edastamine*", et edastada see Bitcoin võrgus.



![Image](assets/fr/53.webp)



Selle leiate Sparrow Wallet vahekaardilt "*Tehingud*".



![Image](assets/fr/54.webp)



Palju õnne, te olete nüüd kursis Trezor Safe 5 ja Sparrow Wallet põhikasutusega! Et minna sammu võrra kaugemale, soovitan seda põhjalikku õpetust Trezor Hardware Wallet kasutamise kohta koos passphrase BIP39-ga, et suurendada oma ohutust:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite allpool Green pöidla. Jagage seda artiklit julgelt oma suhtlusvõrgustikes. Tänan teid väga!