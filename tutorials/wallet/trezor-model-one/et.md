---
name: Trezor Model One
description: Hardware Wallet Model One seadistamine ja kasutamine
---
![cover](assets/cover.webp)



*Pildi krediit: [Trezor.io](https://trezor.io/)*



Trezor Model One on esimene Hardware Wallet, mille SatoshiLabs 2014. aastal välja andis. Pärast enam kui kümneaastast olemasolu on see endiselt huvitav valik, eriti kasutajate jaoks, kes otsivad nii tehniliselt kui ka eelarve poolest kättesaadavat Hardware Wallet. Tegelikult on selle hind ametlikul Trezori veebilehel 49 eurot. See on üks ainsatest riistvaralistest rahakottidest selles hinnaklassis. See jääb keskele umbes 20-eurose algtaseme seadmete, nagu Tapsigner, millel sageli puudub ekraan, ja umbes 80-eurose keskklassi seadmete, nagu Ledger Nano S Plus või Trezor Safe 3, vahele.



Model One'il on 0,96-tolline monokroomne OLED-ekraan ja kaks füüsilist nuppu. See töötab ilma patareita, kasutades ainult mikro-USB-ühendust toite- ja andmeside Exchange jaoks.



![Image](assets/fr/01.webp)



Model One'i peamine puudus on turvalise elemendi puudumine, mis muudab selle haavatavaks mitmesuguste füüsiliste rünnakute suhtes, millest mõnda on suhteliselt lihtne teostada. Need rünnakud võivad hõlmata lisakanalite analüüsi, et määrata seadme PIN-kood, või keerukamaid tehnikaid, et eraldada krüpteeritud seed, et seda hiljem brute-force'i abil murda. Pange tähele, et need rünnakud nõuavad füüsilist juurdepääsu seadmele. Seda haavatavust saab siiski oluliselt vähendada, kui kasutada kindlat passphrase BIP39. Kui valite selle Hardware Wallet, soovitan tungivalt konfigureerida passphrase.



Model One pakub kahte olulist eelist:




- See põhineb täielikult avatud lähtekoodiga arhitektuuril. Erinevalt uuematest Secure Elementi mudelitest on kõik Model One'i riist- ja tarkvarakomponendid auditeeritavad;
- See on varustatud ekraaniga. Minu teada on see ainus Hardware Wallet, mis on turul selles hinnaklassis ekraaniga. See on väga oluline omadus, sest see võimaldab kontrollida allkirjastatud teavet ja vastuvõtuaadressi, mis takistab paljusid digitaalseid rünnakuid.



Trezor Model One võib seega olla mõistlik valik piiratud eelarvega algajatele ja edasijõudnutele. Siiski on oluline olla teadlik selle füüsilise kaitse piirangutest, mis tulenevad Secure Elementi puudumisest. Kui teie eelarve on piiratud, on see hea valik, kuid kui te saate endale lubada paremat mudelit, näiteks Trezor Safe 3, mille hind on 79 eurot, on see eelistatavam, kuna see sisaldab Secure Elementi.



## Trezor Model One'i lahtipakkimine



Kui saate oma Model One'i kätte, veenduge, et karp ja Seal on terved, et kinnitada, et pakendit ei ole avatud. Seadme autentsuse ja terviklikkuse tarkvaraline kontroll toimub ka seadme hilisemal seadistamisel.



Karbi sisu sisaldab:




- Trezor Model One;
- Kaardimaterjal Mnemonic fraasi, kleebiste ja juhiste salvestamiseks;
- USB-A mikro-USB-kaabel.



![Image](assets/fr/02.webp)



Seadmes navigeerimine on väga lihtne:




- Kinnitamiseks tehke paremklõps ja jätkake järgmiste sammudega;
- Tagasi minekuks kasutage vasakut nuppu.



## Eeltingimused



Selles õpetuses näitan teile, kuidas kasutada Trezor Model One'i koos [Sparrow Wallet portfellihaldustarkvaraga](https://sparrowwallet.com/download/). Kui te ei ole seda tarkvara veel paigaldanud, siis palun tehke seda kohe. Kui vajate abi, on meil ka üksikasjalik õpetus Sparrow Wallet seadistamise kohta :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Model One'i seadistamiseks, selle autentsuse kontrollimiseks ja püsivara installimiseks on vaja ka Trezor Suite'i tarkvara. Kasutame seda tarkvara ainult selleks ja pärast seda on seda vaja ainult püsivara uuendamiseks. Wallet igapäevaseks haldamiseks kasutame eranditult Sparrow Wallet, kuna see on optimeeritud Bitcoin jaoks ja seda on lihtne kasutada isegi algajatele (Sparrow toetab ainult Bitcoin, mitte altcoine).



[Lae Trezor Suite alla ametlikust veebisaidist](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Nende mõlema programmi puhul soovitan tungivalt kontrollida nii nende autentsust (GnuPG abil) kui ka terviklikkust (Hash abil) enne nende paigaldamist oma masinasse. Kui te ei tea, kuidas seda teha, võite jälgida seda teist õpetust :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Model One käivitamine



Ühendage Model One arvutiga, kuhu on juba paigaldatud Trezor Suite ja Sparrow Wallet.



![Image](assets/fr/04.webp)



Avage Trezor Suite, seejärel klõpsake nupule "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Valige "*Bitcoin-only firmware*", seejärel klõpsake "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite installib seejärel püsivara teie Model One'ile. Palun oodake installimise ajal.



![Image](assets/fr/07.webp)



Klõpsake nuppu "*Jätka*".



![Image](assets/fr/08.webp)



## Bitcoin portfelli loomine



Klõpsake Trezor Suite'is nupule "*Loo uus Wallet*".



![Image](assets/fr/09.webp)



Nõustuge Hardware Wallet kasutustingimustega.



![Image](assets/fr/10.webp)



Trezor Suite'is klõpsake nuppu "*Vajuta varundamist*".



![Image](assets/fr/11.webp)



Tarkvara annab juhiseid, kuidas hallata oma Mnemonic fraasi.



See Mnemonic annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda lauset valdab, võib teie raha varastada, isegi ilma füüsilise juurdepääsuta teie Trezor Model One'ile.



24-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie Hardware Wallet kaob, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.



Võite kirjutada selle karbis olevale papile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.



Kinnitage juhised, seejärel klõpsake nupule "*Loo Wallet varukoopia*".



![Image](assets/fr/12.webp)



Model One loob teie Mnemonic fraasi juhusliku numbrigeneraatori abil. Veenduge, et teid ei jälgita selle toimingu ajal. Kirjutage ekraanil esitatud sõnad enda valitud füüsilisele andmekandjale. Sõltuvalt teie turvastrateegiast võite kaaluda fraasi mitmete täielike füüsiliste koopiate tegemist (kuid eelkõige ärge jagage seda). Oluline on hoida sõnad nummerdatud ja järjestikku.



***Es on selge, et te ei tohi neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidist Wallet kasutatakse ainult Testnet-l ja see kustutatakse õpetuse lõpus



Lisateavet selle kohta, kuidas oma Mnemonic fraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Järgmiste sõnade juurde liikumiseks tehke paremklõps. Kui olete kõik sõnad üles kirjutanud, klõpsake uuesti paremale nupule, et liikuda edasi järgmise sammu juurde.



![Image](assets/fr/13.webp)



Teie Hardware Wallet näitab taas kõik teie sõnad. Kontrollige, et olete need kõik üles kirjutanud.



![Image](assets/fr/14.webp)



## PIN-koodi seadistamine



Järgneb PIN-koodi samm. PIN-kood avab teie Trezori lukustuse. Seega pakub see kaitset volitamata füüsilise juurdepääsu eest. See PIN-kood ei ole seotud teie Wallet krüptograafiliste võtmete tuletamisega. Seega isegi ilma PIN-koodile juurdepääsuta võimaldab teie 12-sõnalise Mnemonic fraasi omamine taastada juurdepääsu oma bitcoinidele.



Trezor Suite'is klõpsake nupule "*Jätka PIN-koodi*", seejärel nupule "*Set PIN*".



![Image](assets/fr/15.webp)



Kinnitage Model One'i kohta.



![Image](assets/fr/16.webp)



Soovitame valida võimalikult juhusliku PIN-koodi. Salvesta see kood kindlasti sellesse kohta, mis ei ole sinu Trezori salvestamise koht (nt paroolihaldurisse). PIN-koodi saate määrata 8 kuni 50-kohalise PIN-koodi. Turvalisuse suurendamiseks soovitan valida võimalikult pikk PIN-kood.



PIN-kood tuleb sisestada Trezor Suite'is arvutis, klõpsates numbritele vastavatele punktidele vastavalt Trezor Model One'i klaviatuuri konfiguratsioonile.



See konkreetne PIN-koodi sisestamise meetod on vajalik iga kord, kui te oma Trezor Model One'i lahti lukustate, kas Trezor Suite'i või Sparrow Wallet kaudu.



![Image](assets/fr/17.webp)



Kui olete lõpetanud, klõpsake nupule "*Enter PIN*".



![Image](assets/fr/18.webp)



Kinnitamiseks kirjutage PIN-kood uuesti üles.



![Image](assets/fr/19.webp)



Klõpsake Trezor Suite'is nupule "*Complete setup*".



![Image](assets/fr/20.webp)



Teie Model One'i konfigureerimine on nüüd lõpule viidud. Soovi korral saate muuta oma Hardware Wallet nime ja kodulehte.



![Image](assets/fr/21.webp)



Me ei vaja enam Trezor Suite'i tarkvara, välja arvatud selleks, et teha oma Hardware Wallet-le korrapäraselt püsivara uuendusi või kui soovite teha taastamistesti. Nüüd hakkame portfelli haldamiseks kasutama Sparrow'd, sest see tarkvara sobib suurepäraselt ainult Bitcoin kasutamiseks.



## Portfelli seadistamine Sparrow Wallet-l



Alustage Sparrow Wallet allalaadimisest ja installimisest [ametlikust veebisaidist](https://sparrowwallet.com/) oma arvutisse, kui te seda veel teinud ei ole.



Kui olete avanud Sparrow Wallet, veenduge, et tarkvara on ühendatud Bitcoin sõlmpunktiga, mida näitab Interface paremas alumises nurgas olev märkeruut. Kui teil on probleeme Sparrow ühendamisega, soovitan teil tutvuda selle õpetuse algusega:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klõpsake vahekaardil "*Fail*" ja seejärel "*Uus Wallet*".



![Image](assets/fr/22.webp)



Andke oma portfellile nimi ja klõpsake seejärel nupule "*Loo Wallet*".



![Image](assets/fr/23.webp)



Valige rippmenüüst "*Skripti tüüp*" skripti tüüp, mida kasutatakse teie bitcoinide kaitsmiseks. Soovitan "*Taproot*" või selle puudumisel "*Native SegWit*".



![Image](assets/fr/24.webp)



Klõpsake nupule "*Connected Hardware Wallet*". Teie Model One peab muidugi olema arvutiga ühendatud.



![Image](assets/fr/25.webp)



Vajutage nupule "*Scan*". Teie Model One peaks ilmuma.



Kui ühendate Model One'i arvutiga, kus on avatud Sparrow Wallet, siis palutakse teil sisestada Sparrow's passphrase BIP39. Seda täiustatud võimalust käsitletakse ühes tulevases õpetuses. Praegu võite lihtsalt valida "*Toggle passphrase Off*", et Trezor ei nõuaks iga kord käivitamisel passphrase sisestamist.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klõpsake nupule "*Import Keystore*".



![Image](assets/fr/27.webp)



Nüüd näete oma Wallet üksikasju, sealhulgas oma esimese konto laiendatud avalikku võtit. Wallet loomise lõpuleviimiseks klõpsake nuppu "*Kandida*".



![Image](assets/fr/28.webp)



Valige tugev parool, et tagada juurdepääs Sparrow Wallet-le. See parool tagab turvalise juurdepääsu teie Sparrow Wallet andmetele, kaitstes teie avalikke võtmeid, aadresse, silte ja tehingulugu volitamata juurdepääsu eest.



Soovitan teil salvestada see parool paroolihaldurisse, et te seda ei unustaks.



![Image](assets/fr/29.webp)



Ja nüüd on teie portfell imporditud Sparrow Wallet-sse!



![Image](assets/fr/30.webp)



Enne kui saate oma esimesed bitcoinid oma Wallet-sse, ** soovitan teil tungivalt teha tühja taastamistesti**. Kirjutage üles mõned võrdlusandmed, näiteks oma xpub, ja seejärel lähtestage oma Trezor Model One, kui Wallet on veel tühi. Seejärel proovige taastada oma Wallet Trezoril, kasutades oma paberkandjal varukoopiaid. Kontrollige, kas pärast taastamist loodud xpub vastab sellele, mille te algselt üles kirjutasite. Kui see vastab, võite olla kindel, et teie paberkandjal varukoopiad on usaldusväärsed.



Kui soovite rohkem teada saada, kuidas teha taastamistesti, soovitan teil tutvuda selle teise õpetusega:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kuidas saada bitcoine Trezor Model One'iga?



Klõpsake Sparrow's vahekaardil "*Vastuvõtmine*".



![Image](assets/fr/31.webp)



Enne Sparrow Wallet pakutud Address kasutamist kontrollige seda oma Trezori ekraanil. See tava võimaldab teil kinnitada, et Sparrow'l kuvatav Address ei ole pettus ja et Hardware Wallet on tõepoolest selle Address abil tagatud bitcoinide hilisemaks kulutamiseks vajaliku privaatvõtme omanikuks. See aitab teil vältida mitut liiki rünnakuid.



Selle kontrolli teostamiseks klõpsake nuppu "*Kuvada Address*".



![Image](assets/fr/32.webp)



Kontrollige, et teie Trezoril kuvatav Address vastab Sparrow Wallet-le. Samuti on soovitatav teha see kontroll vahetult enne oma Address edastamist saatjale, et olla kindel selle kehtivuses. Kinnitamiseks võite vajutada parempoolset nuppu.



![Image](assets/fr/33.webp)



Võite lisada ka "*Label*", et kirjeldada bitcoinide allikat, mida selle Address abil kaitstakse. See on hea tava, mis võimaldab teil oma UTXOsid paremini hallata.



![Image](assets/fr/34.webp)



Seejärel saate seda Address kasutada bitcoinide vastuvõtmiseks.



![Image](assets/fr/35.webp)



## Kuidas saata bitcoine Trezor Model One'iga?



Nüüd, kui olete saanud oma esimese Satsi oma Model One'i kindlustatud Wallet-s, võite neid ka kulutada! Ühendage oma Trezor arvutiga, käivitage Sparrow Wallet, seejärel minge vahekaardile "*Send*", et luua uus tehing.



![Image](assets/fr/36.webp)



Kui soovite *Mündikontrolli*, st valida konkreetselt, milliseid UTXOsid tehingus tarbida, minge vahekaardile "*UTXOd*". Valige UTXO-d, mida soovite kulutada, ja klõpsake seejärel nupule "*Send Selected*". Teid suunatakse tagasi samale ekraanile vahekaardile "*Send*", kuid teie UTXO-d on juba valitud tehingu jaoks.



![Image](assets/fr/37.webp)



Sisestage sihtkoht Address. Võite sisestada ka mitu aadressi, klõpsates nupule "*+ Add*".



![Image](assets/fr/38.webp)



Kirjutage "*Silt*", et meeles pidada selle kulu eesmärki.



![Image](assets/fr/39.webp)



Valige sellele Address-le saadetav summa.



![Image](assets/fr/40.webp)



Kohandage oma tehingu tasumäär vastavalt praegusele turule. Näiteks võite kasutada [Mempool.space](https://Mempool.space/), et valida sobiv tasumäär.



Veenduge, et kõik tehingu parameetrid on õiged, seejärel klõpsake "*Loo tehing*".



![Image](assets/fr/41.webp)



Kui olete kõigega rahul, klõpsake nuppu "*Tehingu allkirjastamiseks lõpuleviimine*".



![Image](assets/fr/42.webp)



Klõpsake nuppu "*Sign*".



![Image](assets/fr/43.webp)



Klõpsake oma Trezor Model One'i kõrval nupule "*Sign*".



![Image](assets/fr/44.webp)



Kontrollige oma Hardware Wallet ekraanil tehingu parameetreid, sealhulgas vastuvõtva Address vastuvõtja, saadetud summa ja tasu. Kui tehing on Trezoril kontrollitud, tehke allakirjutamiseks paremklõps.



![Image](assets/fr/45.webp)



Teie tehing on nüüd allkirjastatud. Kontrollige veelkord, et kõik on korras, seejärel klõpsake "*Tehingu edastamine*", et edastada see Bitcoin võrgus.



![Image](assets/fr/46.webp)



Leiad selle Sparrow Wallet vahekaardilt "*Tehingud*".



![Image](assets/fr/47.webp)



Palju õnne, te olete nüüd kursis Trezor Model One'i ja Sparrow Wallet põhikasutusega! Et minna sammu võrra kaugemale, soovitan seda põhjalikku õpetust Hardware Wallet Trezori kasutamise kohta passphrase BIP39-ga, et tugevdada teie ohutust :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite allpool Green pöidla. Jagage seda artiklit julgelt oma suhtlusvõrgustikes. Tänan teid väga!