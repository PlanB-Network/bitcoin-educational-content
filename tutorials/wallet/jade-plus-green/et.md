---
name: Jade Plus - roheline
description: Jade Plus'i lihtne konfigureerimine koos rohelise
---
![cover](assets/cover.webp)

Jade Plus on ainult Bitcoini riistvara rahakott, mille on kujundanud Blockstream. See on klassikalise Jade'i järeltulija, mille tarkvara on täiustatud, millel on rohkem võimalusi ja mille ergonoomika on ümber kujundatud, et seda oleks intuitiivsem kasutada. See uus versioon on uhke suurepärase 1,9-tollise LCD-ekraaniga, millel on laiem värvigamma kui selle eelkäijal. Optimeeritud on ka nupud ja menüü navigeerimine.

Jade Plus'i saab kasutada mitmel viisil: juhtmega USB-C ühenduse kaudu, "*Air-Gap*" režiimis koos micro SD-kaardiga (vajalik adapter), Bluetoothi kaudu või isegi QR-koodide vahetamise teel tänu integreeritud kaamerale. See riistvaraline rahakott on akutoitega.

See on saadaval alates 149,99 dollarist musta baasversioonina ning "*Genesis Grey*" või "*Lunar Silver*" versioonide hind võib tõusta kuni 20 dollariga. Jade Plus on seega huvitav valik, mille täiustatud funktsioonid on võrreldavad kõrgekvaliteediliste riistvaraliste rahakottide, nagu Coldcard Q või Passport V2, omadega, kuid üsna madala hinnaga, mis on lähedane keskklassi mudelitele.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus ühildub enamiku portfellihaldustarkvaraga. Siin on kokkuvõte ühilduvusest kirjutamise ajal (jaanuar 2025):

| Lauaplaat | Mobiil | USB | Bluetooth | QR | JadeLink | Haldustarkvara

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 | 🟢 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |

| Hoidja | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |

Selles õpetuses seadistame ja kasutame Jade Plus'i koos Blockstream'i mobiilirakendusega Green Wallet Bluetooth-ühenduse kaudu. See seadistus sobib ideaalselt algajatele. Kui otsite edasijõudnute lähenemist, soovitan vaadata seda õpetust, kus kasutame Jade Plus'i koos Sparrow Walletiga QR-koodide režiimis:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Jade Plus ohutusmudel

Jade Plus kasutab turvamudelit, mis põhineb "virtuaalsel turvalisel elemendil", mille materialiseerib "pime oraakel". Konkreetselt öeldes ühendab see mehhanism kasutaja valitud PIN-koodi, Jade'is hoitava saladuse ja oraakli (Blockstream'i hallatav server) saladuse, et luua kahe üksuse vahel jaotatud AES-256 võti. Algatamise ajal kindlustab ECDH-vahetus side oraakliga ja krüpteerib taastamislause riistvara rahakotis. Praktiliselt öeldes, kui soovite juurdepääsu seemnele tehingute allkirjastamiseks, vajate juurdepääsu :


- Jade Plus seadme enda juurde;
- PIN-koodi seadme avamiseks ;
- Ja oraakli saladuse juurde.

Selle lähenemisviisi peamine eelis on see, et riistvara tasandil puudub üks vigastuspunkt, sest kui ründaja peaks kunagi Jade'ile ligi pääsema, on võtmete väljavõtmiseks vaja samaaegselt ohustada nii Jade'i kui ka oraaklit. See mudel tähendab ka seda, et Jade Plus on täielikult avatud lähtekoodiga, vältides piiranguid, mis on seotud tõeliste füüsiliste turvaliste elementide kasutamisega, nagu näiteks Ledgeri puhul.

Selle süsteemi puuduseks on see, et Jade Plusi kasutamine sõltub Blockstream'i poolt hallatavast oraaklist. Kui see oraakel muutub kättesaamatuks, ei ole enam võimalik riistvaralist rahakotti otse PIN-koodiga kasutada. See ei tähenda siiski, et teie bitcoinid on kadunud, sest neid saab endiselt taastada, kasutades oma taastamislauset, mille saate sisestada Jade Plus'is režiimis "*stateless*". Selle sõltuvuse vältimiseks saate ka oma oraakliserveri konfigureerida ja hallata.

## Jade Plus'i lahtipakkimine

Kui saate oma Jade Plusi, kontrollige, et pakend ja pitser oleksid heas korras, et veenduda, et pakki ei ole avatud.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Karbist leiate :


- Le Jade Plus;
- USB-C kaabel;
- Kaardid, et salvestada oma mälulause sõnade või "*CompactSeedQR*" kujul;
- Mõned kasutusjuhised ;
- Nöör;
- Mõned kleebised.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Seadmel on 4 navigatsiooninuppu:


- Nupp paremal allosas lülitab Jade sisse;
- Seadme esiküljel olevat suurt nuppu kasutatakse elemendi valimiseks;
- Kaks väikest nuppu üleval võimaldavad navigeerida vasakule ja paremale;
- Võite valida elemendi ka seadme ülaosas asuvatel kahel nupul üheaegselt klõpsates.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Uue Bitcoini rahakoti loomine

Klõpsake nupul start.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Klõpsake nuppu "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Valige "Alusta seadistamist". Valik "*Advanced Setup*" teeb sama asja, kuid võimaldab juurdepääsu täiustatud seadetele.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Seejärel klõpsake "*Loo uus rahakott*", et luua uus seemne.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Vajutage nupule "*Jätka*", et kuvada oma uus taastamisfraas.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Teie Jade Plus kuvab teie 12-sõnalist mnemoonilist lauset. **See mnemonüüm annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda fraasi valdab, võib teie raha varastada, isegi kui tal puudub füüsiline juurdepääs teie Jade Plus'ile. 12-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie Jade kaob, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.

Võite kirjutada selle karbis olevale papile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Lisateavet selle kohta, kuidas oma mnemofraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Es on selge, et te ei tohi neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidisportfelli kasutatakse ainult Testnetis ja see kustutatakse õpetuse lõpus

Klõpsake ekraani paremas servas oleval noolega, et kuvada järgmised sõnad.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Kui olete oma lause salvestanud, palub Jade Plus teil seda kinnitada. Valige õige sõna vastavalt järjekorrale seadme ülaosas asuvate nuppude abil ja klõpsake keskmist nuppu, et liikuda edasi järgmise sõna juurde.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Jade Plusi ühendamine rohelise rahakotiga

Selles õpetuses kasutame Jade Plus'is asuva rahakoti haldamiseks rakendust Green Wallet. See meetod sobib eriti hästi algajatele. Kui soovite oma Bitcoini rahakotti üksikasjalikumalt hallata, võite kasutada ka Sparrow Wallet'i, mida käsitleme eraldi õpetuses:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Blockstream Green'i rakenduse paigaldamise ja seadistamise juhiseid leiate selle teise õpetuse esimesest osast:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

Kui olete Blockstream Green'i rakenduses, klõpsake nupule "*Uue portfelli konfigureerimine*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Valige "*Hardvarakontol*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktiveerige oma nutitelefonis Bluetooth, seejärel klõpsake nuppu "*Connect your Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Lubage rohelisele rakendusele juurdepääs Bluetooth-ühendustele.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Rakendus otsib teie Jade Plus'i.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Klõpsake Jade Plus'is menüüs "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Valige oma seade rohelises rakenduses.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Kinnitage oma Jade Plus'i paarituskood.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green pakub teile testi, et veenduda, et teie Jade on tõeline. Klõpsake selleks nupule.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Kinnitage Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Roheline kinnitab, et teie seade on ehtne.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## PIN-koodi seadistamine

Klõpsake nupule "*Jätka*", et valida oma Jade'i PIN-kood.

![JADE-PLUS-GREEN](assets/fr/24.webp)

PIN-kood avab teie Jade'i lukustuse. Seega on see kaitse volitamata füüsilise juurdepääsu eest. See PIN-kood ei ole seotud teie rahakoti krüptograafiliste võtmete tuletamisega. Seega, isegi kui teil puudub juurdepääs sellele PIN-koodile, võimaldab teie 12-sõnalise mnemoonilise fraasi omamine taastada juurdepääsu oma bitcoinidele. Soovitame valida võimalikult juhusliku PIN-koodi. Ja salvestage see kood kindlasti eraldi kohta, kus teie Jade on salvestatud (nt paroolihaldurisse).

Valige oma Jade'i 6-kohaline PIN-kood, kasutades numbrite sirvimiseks parempoolset ja vasakpoolset nuppu ning numbri sisestamise kinnitamiseks keskmist nuppu.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Kinnitage oma PIN-kood teist korda.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Teie bitcoini rahakott on loodud.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Bitcoini konto loomine

Nüüd peate looma konto oma portfellis. Vajutage nupule "*Loo konto*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Valige "*Standard*", kui soovite luua klassikalise ühe sümboliga portfelli.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Lisateavet "*2FA*" valiku kohta saate sellest juhendmaterjalist:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Teie konto on loodud.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Kui soovite oma rohelist portfelli isikupärastada, klõpsake kolmel väikesel punktil üleval paremal.

![JADE-PLUS-GREEN](assets/fr/31.webp)

Valik "*Rename*" võimaldab teil kohandada oma portfelli nime, mis on eriti kasulik, kui haldate samas rakenduses mitut portfelli. Menüü "*Unit*" võimaldab teil muuta oma portfelli põhiüksust. Näiteks saate valida, kas see kuvatakse bitcoinide asemel satoshides. Lõpuks annab menüü "*Parameetrid*" teile juurdepääsu muudele valikutele. Siit leiate näiteks oma laiendatud avaliku võtme ja selle kirjelduse, mis on kasulik, kui kavatsete luua oma Jade'ist ainult kellade rahakoti.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Jade'iga uuesti ühendamiseks pärast selle väljalülitamist vajutage seadme allosas olevat sisse/välja nuppu. Valige rohelise rakenduse avalehel oma seade:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Seejärel sisestage oma Jade'i PIN-kood ja teil on taas ühendus olemas.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Teie Jade avatakse Blockstream'i "virtuaalse turvalise elemendi" kaudu (vt selle õpetuse esimest osa). Selleks on vaja Bluetooth-ühendust rakendusega Green. Kui teil tekib bluetooth-ühendusega avamise ajal raskusi, proovige kahe seadme lahutada ja uuesti ühendada. Kui probleem püsib, saate oma Jade'i siiski avada, valides võimaluse "*QR Scan*" ja järgides [Blockstream'i veebisaidil] (https://jadefw.blockstream.com/pinqr/index.html) olevaid juhiseid.

Enne esimeste bitcoinide saamist oma rahakotti, ** soovitan teil tungivalt teha tühja taastamistesti**. Pange kirja mõned võrdlusandmed, näiteks oma xpub või esimene vastuvõtuaadress, seejärel kustutage oma rahakott rohelises rakenduses ja Jade Plus'is, kui see on veel tühi (`Options -> Device -> Factory Reset`). Seejärel proovige taastada oma rahakott, kasutades oma paberkandjal varukoopiaid mnemofraasiga. Kontrollige, et pärast taastamist genereeritud küpsisteave vastaks sellele, mille te algselt kirja panite. Kui see vastab, võite olla kindel, et teie paberkandjal varukoopiad on usaldusväärsed. Lisateavet selle kohta, kuidas teha testtaastamine, leiate sellest teisest juhendmaterjalist :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoinide vastuvõtmine

Nüüd, kui teie Bitcoini rahakott on loodud, olete valmis saama oma esimesi sati! Lihtsalt klõpsake rohelise rakenduse nupule "*Vaata*".

![JADE-PLUS-GREEN](assets/fr/35.webp)

Roheline näitab vastuvõtu aadressi, kuid enne selle kasutamist on oluline kontrollida seda Jade'ile, et kinnitada, et see kuulub tõepoolest meie portfelli. Selleks klõpsake nupule "*Kontrollige seadmes*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Kontrollige Jade'ile, et aadress on sama, mis rohelisel, seejärel klõpsake kinnitamiseks nupule.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Nüüd saate jagada aadressi maksjaga, et saada bitcoine oma rahakotti. Kui tehing edastatakse võrgus, ilmub see teie rahakotis. Oodake, kuni olete saanud piisavalt kinnitusi, et pidada tehingut lõplikuks.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Bitcoinide saatmine

Kui teie rahakotis on bitcoine, saate nüüd ka bitcoine saata. Klõpsake nupule "*Sendama*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Järgmisel leheküljel sisestage saaja aadress. Selle saate sisestada käsitsi või skannida QR-koodi.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Valige maksesumma.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Ekraani allosas saate valida selle tehingu tasumäärad. Teil on võimalus valida, kas järgida rakenduse soovitusi või kohandada oma tasud. Mida kõrgem on tasu võrreldes teiste pooleliolevate tehingutega, seda kiiremini töödeldakse teie tehingut. Teavet tasuturu kohta leiate [Mempool.space](https://mempool.space/) jaotisest "*Tehingutasud*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Klõpsake "*Järgmine*", et pääseda tehingu kokkuvõtte ekraanile. Kontrollige, et aadress, summa ja tasud on õiged.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Kui kõik läheb hästi, libistage ekraani allosas olevat rohelist nuppu paremale, et allkirjastada ja edastada tehing Bitcoini võrgus.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Nüüd palutakse teil kinnitada tehing Jade'ile.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Veenduge, et saaja aadress on õige. Kinnitamiseks klõpsake kontrollmärgil.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Kontrollige, kas tasu summa on õige, seejärel kinnitage.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Teie tehing on allkirjastatud ja eetrisse saadetud roheliselt.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Palju õnne, te teate nüüd, kuidas seadistada ja kasutada Jade Plus'i koos Blockstream Green mobiilirakendusega Bluetooth-ühenduse kaudu. Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite alljärgnevalt rohelise pöidla. Jagage seda artiklit julgelt oma sotsiaalvõrgustikes. Täname jagamise eest!

Et minna sammu võrra kaugemale, soovitan seda Jade Plus'i õpetust, kus me seadistame selle koos Sparrow Wallet'i tarkvaraga QR-režiimis. Samuti saate teada, kuidas kasutada oma riistvaralise rahakoti täiustatud seadeid:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
