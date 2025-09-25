---
name: Jade Plus - Sparrow
description: Jade Plusi täiustatud konfiguratsioon koos Sparrow Walletiga
---
![cover](assets/cover.webp)

Jade Plus on ainult Bitcoini riistvara rahakott, mille on kujundanud Blockstream. See on klassikalise Jade'i järeltulija, millel on tarkvara täiustused, rohkem võimalusi ja ümberkujundatud ergonoomika intuitiivsemaks kasutamiseks. See uus versioon on uhke suurepärase 1,9-tollise LCD-ekraaniga, millel on laiem värvigamma kui selle eelkäijal. Optimeeritud on ka nupud ja menüü navigeerimine.

Jade Plus'i saab kasutada mitmel viisil: juhtmega USB-C ühenduse kaudu, "*Air-Gap*" režiimis koos micro SD-kaardiga (vajalik adapter), Bluetoothi kaudu või isegi QR-koodide vahetamise teel tänu integreeritud kaamerale. See riistvaraline rahakott on akutoitega.

See on saadaval alates 149,99 dollarist musta baasversioonina ning "*Genesis Grey*" või "*Lunar Silver*" versioonide hind võib tõusta kuni 20 dollariga. Jade Plus on seega huvitav valik, mille täiustatud funktsioonid on võrreldavad kõrgekvaliteediliste riistvaraliste rahakottide, nagu Coldcard Q või Passport V2, omadega, kuid üsna madala hinnaga, mis on lähedane keskklassi mudelitele.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

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

Selles õpetuses seadistame Jade Plusi täiustatud konfiguratsiooni koos töölauaprogrammi Sparrow Wallet tarkvara QR-koodide režiimiga. See konfiguratsioon sobib ideaalselt edasijõudnutele või kogenud kasutajatele. Kui otsite lihtsamat lähenemist algajatele, siis soovitan vaadata seda õpetust, kus kasutame Jade Plus'i koos Green Walletiga Bluetooth-ühenduse kaudu:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Jade Plus ohutusmudel

Jade Plus kasutab turvamudelit, mis põhineb "virtuaalsel turvalisel elemendil", mille materialiseerib "pime oraakel". Konkreetselt öeldes ühendab see mehhanism kasutaja valitud PIN-koodi, Jade'is hoitava saladuse ja oraakli (Blockstream'i hallatav server) saladuse, et luua kahe üksuse vahel jaotatud AES-256 võti. Algatamise ajal kindlustab ECDH-vahetus side oraakliga ja krüpteerib taastamislause riistvara rahakotis. Praktiliselt öeldes, kui soovite juurdepääsu seemnele tehingute allkirjastamiseks, vajate juurdepääsu :


- Jade Plus seade ise;
- PIN-koodi seadme avamiseks ;
- Ja oraakli saladuse juurde.

Selle lähenemisviisi peamine eelis on see, et riistvara tasandil puudub üks vigastuspunkt, sest kui ründaja peaks kunagi Jade'ile ligi pääsema, on võtmete väljavõtmiseks vaja samaaegselt ohustada nii Jade'i kui ka oraaklit. See mudel tähendab ka seda, et Jade Plus on täielikult avatud lähtekoodiga, vältides piiranguid, mis on seotud tõeliste füüsiliste turvaliste elementide kasutamisega, nagu näiteks Ledgeri puhul.

Selle süsteemi puuduseks on see, et Jade Plusi kasutamine sõltub Blockstream'i poolt hallatavast oraaklist. Kui see oraakel muutub kättesaamatuks, ei ole enam võimalik riistvaralist rahakotti otse PIN-koodiga kasutada. See ei tähenda siiski, et teie bitcoinid on kadunud, sest neid saab endiselt taastada, kasutades oma taastamislauset, mille saate sisestada Jade Plus'is režiimis "*stateless*". Selle sõltuvuse vältimiseks saate ka oma oraakliserveri konfigureerida ja hallata.

Teine võimalus oma seemne haldamiseks on lihtsalt mitte registreerida seda Jade Plus'is. Sellisel juhul muutub Jade ainult allkirjastamise seadmeks. Initsialiseerimise ajal salvestate lisaks tavapärasele taastamislause salvestamisele sõnade kujul ka käsitsi genereeritud QR-koodina. Nii saate iga kord, kui kasutate rahakotti, importida seemne Jade'i kaamera abil. See võib olla edasijõudnud kasutajatele huvitav võimalus, sõltuvalt teie turvastrateegiast, kuid te peate olema ettevaatlik nii seemne salvestamisel kui ka selle kaitsmisel, sest isegi QR-koodina võimaldaks see kellelgi teie raha varastada. Vaatame seda võimalust selles õpetuses, kuid see ei ole kohustuslik.

## Jade Plus'i lahtipakkimine

Kui saate oma Jade Plusi, kontrollige, et pakend ja pitser oleksid heas korras, et veenduda, et pakki ei ole avatud.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Karbist leiate :


- Le Jade Plus;
- USB-C kaabel;
- Kaardid, et salvestada oma mälulause sõnade või "*CompactSeedQR*" kujul;
- Mõned kasutusjuhised ;
- Nöör;
- Mõned kleebised.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Seadmel on 4 navigatsiooninuppu:


- Nupp paremal allosas lülitab Jade sisse;
- Seadme esiküljel olevat suurt nuppu kasutatakse elemendi valimiseks;
- Kaks väikest nuppu üleval võimaldavad navigeerida vasakule ja paremale;
- Võite valida elemendi ka seadme ülaosas asuvatel kahel nupul üheaegselt klõpsates.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Uue Bitcoini rahakoti loomine

Klõpsake nupul start.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Klõpsake nuppu "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Valige "Täiustatud seadistus".

![Image](assets/fr/07.webp)

Seejärel klõpsake "*Loo uus rahakott*", et luua uus seemne. Saate valida 12- või 24-sõnalise mälulause vahel. Teie rahakoti turvalisus jääb mõlema valiku puhul võrdseks, seega võib olla mugavam valida kõige lihtsam variant salvestamiseks, st 12 sõna.

![Image](assets/fr/08.webp)

Vajutage nupule "*Jätka*", et kuvada oma uus taastamisfraas.

![Image](assets/fr/09.webp)

Teie Jade Plus kuvab teie 12-sõnalist mnemoonilist lauset. **See mnemonüüm annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda fraasi valdab, võib teie raha varastada, isegi kui tal puudub füüsiline juurdepääs teie Jade Plus'ile. 12-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie Jade kaob, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.**

Võite kirjutada selle karbis olevale papile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.

![Image](assets/fr/10.webp)

Lisateavet selle kohta, kuidas oma mnemofraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

loomulikult ei tohi te neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidisportfelli kasutatakse ainult Testnetis ja see kustutatakse õpetuse lõpus.

Klõpsake ekraani paremas servas oleval noolega, et kuvada järgmised sõnad.

![Image](assets/fr/11.webp)

Kui olete oma lause salvestanud, palub Jade Plus teil seda kinnitada. Valige õige sõna vastavalt järjekorrale seadme ülaosas asuvate nuppude abil ja klõpsake keskmist nuppu, et liikuda edasi järgmise sõna juurde.

![Image](assets/fr/12.webp)

Seejärel on teil 2 võimalust. Nagu sissejuhatuses selgitatud, saate valida, kas salvestada oma seemne otse seadmesse ja kasutada Blockstream'i "*Virtual Secure Element*" kaitsesüsteemi, et pääseda ligi oma rahakotile (variant 1) või salvestada oma seemne QR-koodina ja skaneerida seda iga kord, kui seda kasutate (variant 2).

Valiku 1 puhul valige "*Ei*" ja valiku 2 puhul "*Ja*".

![Image](assets/fr/13.webp)

### Võimalus 1: QR PIN-lukustuse avamine

Kui olete valinud valiku 1 (CompactSeedQR: "*No*"), viiakse teid otse ühendusmeetodi valiku juurde. Selles õpetuses soovime kasutada seadet Air-Gap-režiimis QR-koodi vahetamise kaudu, seega valige "*QR*".

![Image](assets/fr/27.webp)

Klõpsake nuppu "*Jätka*".

![Image](assets/fr/28.webp)

PIN-koodi kasutatakse teie Jade'i avamiseks ja see pakub kaitset volitamata füüsilise juurdepääsu eest. See PIN-kood ei ole seotud teie rahakoti krüptograafiliste võtmete tuletamisega. Seega, isegi kui teil puudub juurdepääs sellele PIN-koodile, võimaldab teie 12-sõnalise mnemoonilise fraasi omamine taastada juurdepääsu oma bitcoinidele. Soovitame valida võimalikult juhusliku PIN-koodi. Samuti veenduge, et salvestate selle koodi eraldi kohta, kus teie Jade on salvestatud, näiteks paroolihaldurisse.

Valige 6-kohaline PIN-kood oma Jade'ile, kasutades numbrite sirvimiseks vasakut ja paremat nuppu ning iga numbri kinnitamiseks keskmist nuppu.

![Image](assets/fr/29.webp)

Kinnitage oma PIN-kood teist korda.

![Image](assets/fr/30.webp)

Nagu sissejuhatuses selgitatud, salvestatakse teie seemned Jade Plus'is krüpteeritult. Selle dekrüpteerimiseks peate andma :


- Kehtiv PIN-kood (mille me just seadistasime) ;
- Blockstream'i poolt hallatava oraakli saladus.

Selles edasijõudnute õpetuses kasutame Sparrow Wallet'i, et hallata oma Bitcoini rahakotti. Kuid erinevalt Blockstreami Green Wallet'i tarkvarast ei ole Sparrow'l juurdepääsu Blockstreami serverites asuvale oraaklile. Seetõttu kasutame Blockstream'i veebisaiti, et saada oraakli saladus iga kord, kui me Jade Plus'i lahti lukustame.

Külasta https://jadefw.blockstream.com/pinqr/index.html

Klõpsake nuppu "*Start QR Unlock*".

![Image](assets/fr/31.webp)

Klõpsake nuppu "*Tehtud*", kuna olete Jade Plus'i PIN-koodi juba valinud.

![Image](assets/fr/32.webp)

Kasutage oma arvuti kaamerat, et skaneerida Jade'i ekraanil kuvatavaid QR-koode.

![Image](assets/fr/33.webp)

Kinnitage oma Jade, et pääseda järgmisele ekraanile.

![Image](assets/fr/34.webp)

Skaneerige nüüd veebisaidil nähtav QR-kood, et saada kätte oraakli saladus.

![Image](assets/fr/35.webp)

Nüüd, kui teie portfell on loodud, võite jätkata järgmiste sammudega ja jätta vahele alajaotuse "*Võimalus 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Iga kord käivitamisel klõpsake "*QR Mode*".

![Image](assets/fr/37.webp)

Valige "*QR PIN-koodi avamine*".

![Image](assets/fr/38.webp)

Sisestage oma PIN-kood.

![Image](assets/fr/39.webp)

Seejärel minge [Blockstream'i veebisaidile](https://jadefw.blockstream.com/pinqr/qrpin.html), et vahetada QR-koode oraakliga.

![Image](assets/fr/40.webp)

Teie Jade on nüüd vabastatud.

![Image](assets/fr/41.webp)

### Valik 2: CompactSeedQR

Kui olete valinud võimaluse 2 (CompactSeedQR: "*Ja*"), klõpsake uuesti "*Ja*".

![Image](assets/fr/14.webp)

Klõpsake nuppu "*Start*".

![Image](assets/fr/15.webp)

Võite kasutada Jade Plus'i karbis kaasasolevat QR-koodi baasi. Valige sobiv kast sõltuvalt sellest, kas olete valinud 12- või 24-sõnalise lause. Võite ka [printida malli Blockstream'i veebisaidilt](https://help.blockstream.com/hc/article_attachments/41928319071769).

Teie Jade Plus kuvab iga QR-koodi tsooni.

![Image](assets/fr/16.webp)

Kasutage pliiatsit, et värvida ruute ja paljundada oma seemne QR-koodina. Olge täpne, et Jade Plus'i kaamera saaks seda hiljem skaneerida. Kasutage noolt, et liikuda edasi järgmisele alale.

![Image](assets/fr/17.webp)

Kui olete lõpetanud, klõpsake nuppu "*Tehtud*".

![Image](assets/fr/18.webp)

Skaneeri oma käsitsi valmistatud QR-koodi Jade Plus'iga, et kontrollida selle kehtivust.

![Image](assets/fr/19.webp)

Kui teie paberi varukoopia on õige, klõpsake nuppu "*Jätka*".

![Image](assets/fr/20.webp)

Selles õpetuses kasutame ainult QR-koodi skaneerimisel põhinevat ühendusrežiimi, seega valige "*QR*".

![Image](assets/fr/21.webp)

Lisaks CompactSeedQR-i varukoopiale saate lisada ka PIN-koodi, nagu valikus 1. See pakub kaks võimalust oma rahakotile juurdepääsuks: kas PIN-koodi ja Blockstream'i "Virtual Secure Element" süsteemi kaudu või CompactSeedQRi kaudu.

Kui valite topelt PIN-koodi valiku, valige "*PIN*" ja järgige PIN-koodi määramiseks samu samu samu samme nagu 1. valiku puhul.

Kui soovite jätkata ainult CompactSeedQRiga, valige "*SeedQR*".

![Image](assets/fr/22.webp)

Nüüd, kui teie portfell on loodud, võite liikuda edasi järgmiste sammude juurde.

![Image](assets/fr/23.webp)

Iga kord käivitamisel klõpsake nuppu "*QR Mode*" ja seejärel "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Kasutage seadme kaamerat, et skannida oma salvestatud seemet QR-koodina.

![Image](assets/fr/25.webp)

Teie Jade on nüüd vabastatud.

![Image](assets/fr/26.webp)

## BIP39 parooli lisamine

BIP39 parool on vabatahtlik salasõna, mille saate vabalt valida ja mis lisatakse teie mnemofraasile, et tugevdada rahakoti turvalisust. Kui see funktsioon on aktiveeritud, on teie Bitcoini rahakotile juurdepääsuks vaja nii mnemoonilist kui ka paroollauset. Ilma kummata oleks rahakoti taastamine võimatu.

Enne selle suvandi seadistamist oma Jade Plus'is on tungivalt soovitatav lugeda seda artiklit, et mõista täielikult salasõna teoreetilist toimimist ja vältida vigu, mis võivad viia teie bitcoinide kaotamiseni:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kui teie Jade on endiselt lukustatud (paroollauset saab sisestada ainult siis, kui seade ei ole lukustamata), avage menüü "*Options*".

![Image](assets/fr/42.webp)

Valige "*BIP39 salasõna*".

![Image](assets/fr/43.webp)

Valikus "*Sagedus*" saate valida, kas Jade Plus palub teil iga kord käivitamisel sisestada oma salasõna:


- "*Disabled*" keelab salasõna kasutamise;
- "*Ne Järgmine sisselogimine ainult*" nõuab, et te pöörduksite sellesse menüüsse tagasi, et aktiveerida järgmise käivitamise korral teie paroolfraasi päring. See valik võimaldab teil selle kasutamist mitte avaldada;
- "*Always Ask*" paneb Jade'i süstemaatiliselt küsima teie salasõna iga kord, kui see käivitub, paljastades seega, et teie rahakott on kaitstud salasõnaga.

Valige valik vastavalt oma turvastrateegiale. Mina isiklikult valin näiteks "*Always Ask*".

![Image](assets/fr/44.webp)

Seejärel saate valida kahe meetodi vahel, mille abil saate sisestada oma salasõna:


- "*Manuaal*: Virtuaalne klaviatuur võimaldab sisestada tähed (suured ja väikesed tähed), numbrid ja sümbolid tähemärkide kaupa. See on kõigi riistvaraliste rahakottide standardmeetod;
- "*Sõnaloend*": Mis kiirendab paroolide sisestamist ja suurendab selle entroopiat. Sisestamise ajal pakub süsteem välja sõnu BIP39 nimekirjast, mis lihtsustab lukustuse avamist. See meetod genereerib automaatselt lause, ühendades valitud sõnad, mis on eraldatud tühikutega (näide: `abandon ability able`).

Mina isiklikult soovitan kasutada esimest meetodit, sest see on standard, mida leiad kõikidel teistel portfooliotugedel.

![Image](assets/fr/45.webp)

Seejärel saate naasta avakuvale ja avada oma rahakoti tavapäraselt, kasutades kas PIN-koodi või CompactSeedQR-i (nagu eespool näha). Seejärel palutakse teil sisestada oma salasõna.

![Image](assets/fr/46.webp)

Sisestage see Jade klaviatuuril ja tehke kindlasti üks või mitu varukoopiat füüsilisel andmekandjal (paber või metall). Näites kasutan ma väga nõrka salasõna, kuid te peate valima tugeva, juhusliku salasõna, mis sisaldab igat tüüpi sümboleid ja on piisavalt pikk (nagu tugev parool).

![Image](assets/fr/47.webp)

Kui teie salasõna on kehtiv, kinnitage.

![Image](assets/fr/48.webp)

Pange tähele, et BIP39 paroolifraasid on sõltuvad suur- ja kirjavigastusest. Kui sisestate algselt seadistatud salasõnast veidi erineva salasõna, ei anna Jade veateadet, vaid tuletab teise krüptograafiliste võtmete komplekti, mis ei ole teie esialgses portfellis olevad võtmed.

Seetõttu on oluline, et seadistamisel märkige üles oma põhivõtme sõrmejälg, mille leiate ekraani paremast alumisest nurgast. Näiteks minu parooliga `PBN` on minu peavõti sõrmejälg `3AD1AE65`.

![Image](assets/fr/49.webp)

Iga kord, kui avate oma Jade'i oma parooliga, kontrollige, et sõrmejälg oleks sama, mis konfigureerimise ajal sisestatud sõrmejälg. Kui see on nii, siis on teie tunnussõna õige ja pääsete ligi õigele Bitcoini rahakotile. Kui see ei ole nii, siis olete vales rahakotis ja peate uuesti proovima, jälgides, et te ei teeks sisestusvigu.

Enne esimeste bitcoinide saamist oma rahakotti, ** soovitan teil tungivalt teha tühja taastamistesti**. Pange kirja mõned võrdlusandmed, näiteks oma xpub või esimene vastuvõtuaadress, seejärel kustutage oma rahakott Jade Plus'is, kui see on veel tühi (`Options -> Device -> Factory Reset`). Seejärel proovige taastada oma rahakott, kasutades oma paberkandjal varukoopiaid mälulause ja mis tahes salasõna. Kontrollige, et pärast taastamist genereeritud küpsisteave vastaks sellele, mille algselt kirja panite. Kui see vastab, võite olla kindel, et teie paberkandjal varukoopiad on usaldusväärsed. Kui soovite rohkem teada saada, kuidas teha proovitaastamist, vaadake seda teist õpetust:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Rahakoti konfigureerimine Sparrow Wallet'is

Selles õpetuses tutvustan Jade Plusi täiustatud kasutamist Sparrow Wallet'i abil. See riistvaraline rahakott ühildub aga paljude teiste programmidega, näiteks Liana, Nunchuk, Specter, Green ja Keeper. Need ühilduvused erinevad ühenduste osas: USB, Bluetooth või QR-kood (vt täpsemalt tabelit sissejuhatuses).

Alustage Sparrow Walleti allalaadimisest ja installimisest [ametlikul veebisaidil](https://sparrowwallet.com/) oma arvutisse, kui te seda veel teinud ei ole.

![Image](assets/fr/50.webp)

Enne paigaldamist kontrollige kindlasti tarkvara autentsust ja terviklikkust. Kui te ei tea, kuidas seda teha, vaadake seda õpetust:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kui Sparrow Wallet on avatud, klõpsake vahekaardil "*Fail*" ja seejärel "*Uus rahakott*".

![Image](assets/fr/51.webp)

Anna oma rahakotile nimi, seejärel klõpsa "*Loo rahakott*".

![Image](assets/fr/52.webp)

Valige "*Airapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Klõpsake "*Scan...*" valiku "*Jade*" kõrval.

![Image](assets/fr/54.webp)

Avage oma Jade Plus ja kui kasutate Jade Plus'i, sisestage oma paroolfraas. Seejärel minge menüüsse "*Options*", valige "*Wallet*" ja klõpsake "*Export Xpub*".

![Image](assets/fr/55.webp)

Teie Jade kuvab teie Keystore'i mitmete QR-koodide kaudu. Skaneerige neid oma masina abil Sparrow.

![Image](assets/fr/56.webp)

Nüüd peaksite nägema oma xpubi ja üldvõtme sõrmejälge, mis peaks vastama teie Jade Plus'is olevale sõrmejäljele. Klõpsake nupule "*Kanna*".

![Image](assets/fr/57.webp)

Määrake tugev parool, et tagada juurdepääs oma Sparrow rahakotile. See parool kaitseb teie avalikke võtmeid, aadresse, silte ja tehinguajalugu volitamata juurdepääsu eest. See parool on hea mõte salvestada paroolihaldurisse, et te seda ei unustaks.

![Image](assets/fr/58.webp)

Teie portfell on nüüd Sparrow's õigesti konfigureeritud.

![Image](assets/fr/59.webp)

## Bitcoinide vastuvõtmine

Nüüd, kui teie Jade Plus on konfigureeritud, olete valmis saama oma esimesed satsid oma uude Bitcoini rahakotti. Selleks klõpsake Sparrow's menüüs "*Võta*".

![Image](assets/fr/60.webp)

Sparrow kuvab teie portfellis esimese tühja vastuvõtu aadressi.

![Image](assets/fr/61.webp)

Enne selle kasutamist kontrollime seda Jade Plusi ekraanil, et veenduda, et see kuulub meie Bitcoini rahakoti juurde. Klõpsake Jade'is "*Scan QR*", seejärel skannige Sparrow'l kuvatava aadressi QR-koodi.

![Image](assets/fr/62.webp)

Kontrollige, et teie Jade'i ekraanil kuvatav aadress vastab Sparrow Wallet'i ekraanil kuvatavale aadressile. Kui see vastab, klõpsake jätkamiseks kontrollmärgile.

![Image](assets/fr/63.webp)

Teie riistvaraline rahakott kinnitab seejärel, et see aadress on osa teie rahakotist ja et sellega seotud privaatne võti asub seal.

![Image](assets/fr/64.webp)

Kui teie Jade on aadressi kinnitanud, saate seda nüüd bitcoinide saamiseks kasutada. Kui tehing edastatakse võrgus, ilmub see ka Sparrow's. Oodake, kuni olete saanud piisavalt kinnitusi, et pidada tehingut lõplikuks.

![Image](assets/fr/65.webp)

## Bitcoinide saatmine

Nüüd, kui teil on mõned satsid rahakotis, võite ka mõned saata. Selleks klõpsake menüüs "*UTXOs*".

![Image](assets/fr/66.webp)

Valige UTXOd, mida soovite selle tehingu sisendina kasutada, seejärel klõpsake nuppu "*Sendage valitud*".

![Image](assets/fr/67.webp)

Sisestage saaja aadress, silt, mis tuletab teile meelde tehingu eesmärki, ja summa, mille soovite sellele aadressile saata.

![Image](assets/fr/68.webp)

Kohandage tasumäär vastavalt praegustele turutingimustele ja seejärel klõpsake nuppu "*Loo tehing*".

![Image](assets/fr/69.webp)

Kontrollige, et kõik tehingu parameetrid on õiged, seejärel klõpsake "*Tehingu allkirjastamiseks lõpuleviimine*".

![Image](assets/fr/70.webp)

Klõpsake "*Näita QR*", et kuvada PSBT (*Partially Signed Bitcoin Transaction*). Sparrow on tehingu koostanud, kuid sellel puuduvad veel allkirjad, et avada sisendis kasutatud bitcoinid. Neid allkirju saab teha ainult Jade Plus, mis võõrustab teie seemne, andes juurdepääsu tehingu allkirjastamiseks vajalikele privaatvõtmetele.

![Image](assets/fr/71.webp)

Klõpsake oma Jade Plus'is "*Scan QR*", et skaneerida Sparrow'l kuvatavat PSBT-d.

![Image](assets/fr/72.webp)

Kinnitage, et tarneaadress ja saadetud summa on õiged, seejärel klõpsake kinnitamiseks noolt.

![Image](assets/fr/73.webp)

Veenduge, et tasu suurus on teie valitud, seejärel klõpsake tehingu allkirjastamiseks liideses vasakus ülanurgas oleval kriipsu ikoonil.

![Image](assets/fr/74.webp)

Klõpsake Sparrow Wallet'is "*Scan QR*" ja skaneerige oma Jade'ile kuvatavat QR-koodi.

![Image](assets/fr/75.webp)

Teie allkirjastatud tehing on nüüd valmis Bitcoini võrgus edastamiseks ja kaevandaja poolt plokki lisamiseks. Kui kõik on õige, klõpsake nuppu "*Tehingu edastamine*".

![Image](assets/fr/76.webp)

Teie tehing on edastatud ja ootab kinnitust.

![Image](assets/fr/77.webp)

Palju õnne, te teate nüüd, kuidas seadistada ja kasutada Jade Plus'i QR-režiimis. Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite alla rohelise pöidla. Jaga seda artiklit julgelt oma suhtlusvõrgustikes. Täname jagamise eest!

Kui soovite edasi minna, siis soovitan seda teist Jade Plus'i õpetust, kus me konfigureerime seda Bluetoothi kaudu koos rohelise mobiilirakendusega:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0