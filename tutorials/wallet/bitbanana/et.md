---
name: BitBanana
description: Lightning-sõlme mobiilihaldur
---

![cover](assets/cover.webp)



Selles õpetuses saate teada, kuidas paigaldada ja konfigureerida BitBanana Androidis, et juhtida oma Lightning-sõlme nutitelefonist. Näeme, kuidas ühendada rakendus oma olemasoleva infrastruktuuriga (Umbrel, RaspiBlitz, myNode või mõni LND/Core Lightning-sõlm), teha Lightning-makseid, hallata oma kanaleid eemalt, vaadata oma marsruuttulu ja varundada oma konfiguratsioone. Samuti saate teada, millised on parimad turvameetodid teie sõlme juurdepääsu kaitsmiseks ja kuidas seda võrrelda populaarse alternatiiviga Zeus.



## BitBanana tutvustamine



BitBanana on avatud lähtekoodiga Android-mobiilirakendus, mis muudab teie nutitelefoni Lightning-sõlme kaugjuhtimiseks täielikuks armatuurlauaks. Erinevalt Lightningi rahakottidest, mis integreerivad telefoni kohaliku sõlme, võtab BitBanana vastu 100% kaugjuhtimise filosoofia: rakendus ei hoia satoshi ja ühendab ainult teie olemasoleva infrastruktuuriga.



Michael Wünschi poolt MIT-litsentsi alusel välja töötatud rakendus tagab täieliku läbipaistvuse, mille puhul ei koguta isikuandmeid ja mille koostamine on kontrollitud ja reprodutseeritav. BitBanana toetab algselt LND ja Core Lightning standard-URIde kaudu (`lndconnect://` ja `clngrpc://`), mis lihtsustab oluliselt algset seadistamist. Rakendus tunneb ka LndHubi ja Nostr Wallet Connecti kasutajate jaoks, kellel puudub isiklik sõlmpunkt, kuigi need režiimid toimivad piiratud funktsionaalsusega custodial.



Kasutajaliides pakub täielikku juurdepääsu kõigile teie sõlme kriitilistele funktsioonidele: maksete saatmine ja vastuvõtmine (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), Lightning-kanalite haldamine (avamine, sulgemine, tasude korrigeerimine, tasakaalustamine), täiustatud mündikontroll ja valvekaartide haldamine. BitBanana rakendab ka mitu tugevat turvakihti: biomeetriline lukustus, varjatud režiim, hädaolukorra PIN-kood ja algupärane Tor-tugi ühenduste anonüümseks muutmiseks.



## Toetatud platvormid ja paigaldus



### Paigaldamine



BitBanana on saadaval ainult Android 8.0 või uuema versiooni jaoks. Rakendust ei ole olemas iOS-i jaoks ja ühtegi versiooni ei ole kavas. Seda piirangut selgitab projekti ajalugu: BitBanana on otsene järeltulija Zap Androidile, mida algselt arendas Michael Wünsch, kes otsustas jätkata oma tööd oma kaubamärgi all. Zap oli perekond eraldi rakendusi (Zap Android, Zap iOS, Zap Desktop), mida arendasid eri toetajad eraldi koodibaasidega. BitBanana jätkab ainult Androidi haru.



Lisaks sellele on iOSi ökosüsteemil märkimisväärseid regulatiivseid ja tehnilisi piiranguid mitteametlike Lightning-rakenduste jaoks. 2023. aastal lükkas Apple Zeuse uuenduse tagasi "litsentsi rikkumiste" tõttu ja 2024. aastal lahkus Phoenix Wallet USA App Store'ist, kuna Lightning-teenuse pakkujate suhtes valitses regulatiivne ebakindlus. Need takistused seletavad, miks paljud Lightningi arendajad eelistavad Androidi, mis pakub avatud poliitikat mittekaitstavate rakenduste jaoks.



Androidi jaoks on saadaval kolm paigaldusmeetodit: F-Droid (reprodutseeritavad buildid, lähtekoodi kontrollimine) või käsitsi APK GitHubist.



![BitBanana](assets/fr/01.webp)



Ametlik bitbanana.appi veebisait (vasakul) kiidab "100% Self-Custodial with ZERO data collection". Keskmisel ekraanil on kolm allalaadimisvõimalust: F-Droid (soovitatav), Google Play ja APK. Parempoolne ekraan näitab maksehoiatuste teavituste luba.



Rakendus taotleb õigusi: võrk (sõlmeühendus), kaamera (QR-koodid), NFC (LNURL), taustateenused (teavitused), biomeetria (turvalisus) ja WireGuard VPN. Ei mingeid jälgimisseadmeid, null andmete kogumine. Lubage parool või biomeetriline lukustus, et tagada juurdepääs.



## Esialgne konfiguratsioon



### LND sõlme ühendamine



BitBanana ühendamiseks oma LND sõlme (Umbrel, RaspiBlitz, myNode), saada `lndconnect` URI või QR-kood, mis sisaldab aadressi, TLS-sertifikaati ja autentimise makrooni.



Selles õpetuses kasutame LND sõlme, mis on ühendatud vihmavarju kaudu. Täpsema teabe saamiseks vaadake meie spetsiaalset õpetust :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Avage Lightning Node'i rakenduses üleval paremal asuv menüü ja valige "Connect wallet".



![BitBanana](assets/fr/04.webp)



Valige **gRPC (Tor)**, et luua ühendus Tori kaudu (soovitatav). Kuvatakse QR-kood ja üksikasjad (Host .onion, Port 10009, Macaroon).



![BitBanana](assets/fr/02.webp)



Vajutage BitBanana's "CONNECT NODE", skannige QR-koodi või kleepige URI. Lubage kaamerale juurdepääs, seejärel kontrollige enne kinnitamist kuvatavat .onion-aadressi.



**Core Lightning** ühendus



Kui kasutate LND asemel Core Lightning'i (CLN), jääb protsess identseks, kusjuures URI `clngrpc://` sisaldab vastastikuseid TLS-sertifikaate. Core Lightning toetab algselt BOLT12 (pakkumised), võimaldades taaskasutatavaid arveid ja korduvaid makseid, mis ei ole LNDs saadaval.



**ühendus ilma isikliku sõlmpunktita (LNbits/hosted)**



Kui teil ei ole Lightning-sõlme, saab BitBanana luua ühenduse majutatud teenustega LndHubi (BlueWallet ja LNbits kasutavad protokolli) või Nostr Wallet Connecti (NWC) kaudu. Pange tähele: need režiimid toimivad hoiustamisrežiimil (teenus majutab teie raha), mille funktsionaalsus on piiratud. Te ei saa hallata kanaleid ega konfigureerida marsruutimistasusid ning saate saata ja vastu võtta ainult Lightning-makseid.



Lisateavet LNbits'i või Nostr Wallet Connecti kohta leiate meie erinevatest juhendmaterjalidest:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Igapäevane kasutamine



### Interface peamine



Avakuval kuvatakse teie Lightning-saldo, vasakul üleval olev menüü annab juurdepääsu järgmistele jaotistele: Kanalid, marsruutimine, allkirjastamine/kinnitamine, sõlmed, kontaktid, seaded, varundamine. Kella ikoon (üleval paremal) avab tehinguajaloo. Nupud "Saada" ja "Saada" allosas võimaldavad teil saata ja vastu võtta oma satoshisid.



![BitBanana](assets/fr/05.webp)



### Välk ja on-chain maksed



![BitBanana](assets/fr/10.webp)



**Makse saatmine:** Vajutage avakuval nuppu "Saada". Makseekraan (vasakul) pakub aadressi või makseandmete sisestamist väljale "Address või makseandmed", paremal üleval on QR-skanner koodide skaneerimiseks. Samuti saate valida kontaktide sektsioonis salvestatud kontakti, et vältida iga kord skaneerimist.



BitBanana tunneb intelligentselt ära kõik makseformaadid: lightning Address (e-posti formaat, näiteks `utilisateur@domaine.com`), LNURL-maksekoodid dünaamiliste maksete jaoks, LNURL-väljavõtmine raha väljavõtmiseks ja isegi Keysend maksed otse Lightningi avalikule võtmele ilma eelneva arveta. Rakendus teeb vajalikud LNURL-eraldised automaatselt taustal.



Kui arve on laetud, kuvab BitBanana kõik üksikasjad: täpne summa, hinnangulised marsruutimistasud, makse kirjeldus (kui saaja on selle esitanud) ja arve kehtivusaeg. Pärast kinnitust suunatakse makse teie välklamblikanalite kaudu. Seejärel saate vaadata tehingu üksikasjadest hüppeliselt läbitud marsruuti ja tegelikult makstud tasusid.



**Makse vastuvõtmine:** Vajutage nuppu "Vastuvõtmine". Valikuklahv (paremal ekraanil) võimaldab valida Lightning (kohene makse teie kanalite kaudu) ja On-Chain vahel. Lightning-kviitungi puhul sisestage soovitud summa satoshides (või jätke 0, et luua arve, millel puudub kindel summa, mida maksja peab täitma), ja lisage vabatahtlik kirjeldus, mis ilmub arvel. BitBanana genereerib koheselt Lightning-arve koos QR-koodiga skaneerimiseks. Samuti saate arve kopeerida tekstina ja saata selle e-kirjaga. Niipea, kui makse on laekunud, saadetakse teile push-teade ja tehing ilmub kohe ajalukku koos kõigi üksikasjadega.



### Kanalid ja marsruutimine



![BitBanana](assets/fr/06.webp)



Jaotises "Kanalid" kuvatakse teie saatmis- ja vastuvõtuvõimalused ning loetletakse teie kanalid koos unikaalsete avataridega. Iga kanal näitab oma likviidsuse jagunemist kohaliku ja kaughäälestuse vahel. Puudutage kanalit, et saada täielikud üksikasjad ja toimingud (sulgemine, marsruutimistasude muutmine). Kolm punkti üleval paremal annavad juurdepääsu valikule "Rebalance", et tasakaalustada oma kanalite likviidsust. Nupp "+" avab uue kanali.



Marsruudi jaotises (keskne ekraan) kuvatakse edastamise tulud perioodide kaupa (1D, 1W, 1M, 3M, 6M, 1Y) koos üksikasjaliku edastamise ajalooga, et optimeerida oma strateegiat.



Sign/Verify (parempoolne ekraan) võimaldab krüptograafiliselt allkirjastada/verifitseerida sõnumeid, et tõestada sõlme kontrolli.



### Mitmesõlmed ja parameetrid



![BitBanana](assets/fr/07.webp)



**Sõlmede haldamine**: loetleb teie sõlmede nimekirja, kus on nupud käsitsi lisamiseks, QR-koodi skannimiseks või sõlmede vahel vahetamiseks. Eelkõige saate luua eri tüüpi ühendusi ühe ja sama sõlme juurde: LAN, VPN või Tor.



**Kontaktide haldamine**: salvestab teie Lightning-kontaktid kiirete maksete tegemiseks.



**Settings**: kohandada valuuta, keel, avatarid. Turvalisuse ja privaatsuse sektsioon: App Lock (PIN/biomeetria), Hide balance (salajane režiim), Tor (IP anonüümseks muutmine). Hinnaoraaklite, plokkide uurijate, kohandatud tasu hindajate konfigureerimine.



## Eelised ja piirangud



**Kõrgpunktid:**




- Täielik mobiilsus: kontrollige oma Lightning-sõlme ükskõik kust
- Täielik funktsionaalsus: maksed (LNURL, Lightning Address, BOLT 12), kanalite haldamine, mündi kontroll, vaatetornid, mitme sõlme haldamine
- Turvalisus: PIN/biomeetria, varjatud režiim, hädaolukorra PIN-kood, algupärane Tor, ekraanipildi blokeerimine
- Tasuta, avatud lähtekoodiga (MIT), null komisjonitasu, null andmete kogumine



**Piirangud:**




- Nõuab aktiivset Lightning-sõlme (või LNbits'i hoolduse režiimis)
- IOS versiooni ei ole plaanis
- Telefonile juurdepääsu tagamine on kriitiline (makaronide administraator = täielik juurdepääs sõlme)



## Parimad tavad



**Turvalisus:**




- PIN-koodi/biomeetrilise lukustuse aktiveerimine (takistab volitamata juurdepääsu sõlmpunktile)
- Seadistage hädaolukorra PIN-kood (kustutab delikaatsed andmed sundolukorra korral)
- Ärge kunagi jagage oma sisselogimise URI-d või makrooni
- Varjatud režiim vaenulikus keskkonnas



**Login:**




- VPN-võrk (Tailscale, ZeroTier): parim kompromiss kiiruse ja turvalisuse vahel
- Tor: maksimaalne konfidentsiaalsus, suurem latentsus
- Clearnet: vältida, kui see ei ole vajalik (IP-ühendus, avatud pordid)



### Varundamine ja taastamine



Lõpuks on olemas menüü "Varukoopia", mis võimaldab teil salvestada oma konfiguratsioone telefoni migreerimiseks või uuesti paigaldamiseks.



![BitBanana](assets/fr/08.webp)



**Tähtis:** Varukoopia EI sisalda seed või kanali varukoopiaid (tuleb teha sõlmes). See sisaldab: sõlme konfiguratsioone (aadressid, sertifikaadid, makaronid), sildid, kontaktid, parameetrid. Restore nupp võimaldab importida olemasoleva varukoopia. Enne salvestamist on vaja kinnitust.



![BitBanana](assets/fr/09.webp)



Sisestage krüpteerimisparool (paremal ekraanil). Süsteem avab failivaliku (vasakpoolne ekraan), et salvestada `BitBananaBackup_2025-XX-XX-XX.dat`. Kinnitus "Backup created".



**Turvalisus:** Salvesta varukoopia krüpteeritult (isiklik pilv, USB, NAS). Ärge kunagi jagage faile või paroole. Testige taastamist regulaarselt. Varukoopia taastab ühendused, mitte vahendid.



## BitBanana vs Zeus: Mis vahe on?



Kui uurite mobiilirakendusi Lightning-sõlme haldamiseks, siis tõenäoliselt puutute kokku Zeusega, mis on populaarne alternatiiv BitBanana'le. Erinevalt BitBanana'st, mis keskendub ainult olemasoleva sõlme kaugjuhtimisele, on Zeusil terviklikum lähenemine, pakkudes kahte töörežiimi: otse rakendusse integreeritud Lightning-sõlme (integreeritud režiim koos integreeritud LND-ga) ja kaugühendus välise sõlmega, nagu BitBanana.



See kahesugune funktsionaalsus teeb Zeuse eriti atraktiivseks algajatele, kes soovivad Lightninguga eksperimenteerida ilma eelneva infrastruktuurita. Sisseehitatud režiim võimaldab koheselt käivitada täieliku mobiilse sõlme, samas kui edasijõudnud kasutajad saavad pärast isikliku sõlme konfigureerimist üle minna kaugühendusele. Zeus toetab ka LND ja Core Lightning kaugühenduse jaoks, näiteks BitBanana.



Zeuse teine suur eelis on selle platvormideülene kättesaadavus (iOS ja Android), samas kui BitBanana jääb ainult Androidi-põhiseks. Zeus sisaldab ka Olympus LSP infrastruktuuri, et hõlbustada Lightning-maksete vastuvõtmist just-in-time-kanalite kaudu, müügipunktisüsteemi kaupmeeste jaoks ja integreeritud swap-funktsioone likviidsuse haldamiseks.



Siiski on BitBanana säilitanud oma konkreetsed tugevused: lihtsam ja sujuvam kasutajaliides, parem kasutajakogemus (UX) tänu eranditult kaugjuhtimisele keskendumisele ja hariv lähenemine koos kontekstipõhiste selgitustega. Zeus pakub rohkem funktsionaalsust, kuid keerulisema kasutajaliidese arvelt. Rakendus on endiselt eriti sobiv kasutajatele, kes soovivad juhtida sõlme ainult eemalt, ilma hoolduse funktsioonideta.



Kui soovite Zeuse kohta rohkem teada saada, vaadake järgmisi õpetusi:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Kokkuvõte



BitBanana muudab teie Androidi nutitelefoni täielikuks Lightning armatuurlauaks, pakkudes sõlmeoperaatoritele enneolematut liikuvust. Rakendus katab kõik funktsioonid: maksed (kõik vormingud), kanalite haldamine, mündi kontroll, vaatetornid, mitme sõlme, täiustatud turvalisus (PIN/biomeetria, Tor, Emergency PIN).



Täiesti suveräänne BitBanana ei kogu mingeid andmeid ja ei ohusta teie raha konfidentsiaalsust ega kontrolli. Avatud lähtekood (MIT) tagab läbipaistvuse.



## Ressursid



### Ametlikud dokumendid




- [BitBanana veebileht](https://bitbanana.app)
- [Täielik dokumentatsioon](https://docs.bitbanana.app)
- [GitHubi lähtekood](https://github.com/michaelWuensch/BitBanana)



### Paigaldamine




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)