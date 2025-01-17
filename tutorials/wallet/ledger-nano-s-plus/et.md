---
name: Ledger Nano S Plus
description: Ledger Nano S Plus seadistamine ja kasutamine
---
![cover](assets/cover.webp)

Riistvara rahakott on elektrooniline seade, mis on pühendatud Bitcoin'i rahakoti privaatvõtmete haldamisele ja turvamisele. Erinevalt tarkvaralistest rahakottidest (või kuumadest rahakottidest), mis on paigaldatud üldotstarbelistele masinatele, mis on sageli ühendatud Internetiga, võimaldavad riistvara rahakotid privaatvõtmete füüsilist isoleerimist, vähendades häkkimise ja varguse riske.

Riistvara rahakoti peamine eesmärk on seadme funktsionaalsuste minimeerimine nii palju kui võimalik, et vähendada selle rünnakupinda. Väiksem rünnakupind tähendab ka vähem potentsiaalseid rünnakutegevusi, st vähem süsteemi nõrkusi, mida ründajad võiksid ära kasutada bitcoini juurdepääsuks.

On soovitatav kasutada riistvara rahakotti oma bitcoinide turvamiseks, eriti kui omate olulisi summasid, kas absoluutväärtuses või kui osa teie koguvarast.

Riistvara rahakotte kasutatakse koos rahakoti haldamise tarkvaraga arvutis või nutitelefonis. See tarkvara haldab tehingute loomist, kuid tehingute kinnitamiseks vajalik krüptograafiline allkiri tehakse ainult riistvara rahakoti sees. See tähendab, et privaatvõtmed ei ole kunagi potentsiaalselt haavatavas keskkonnas paljastatud.

Riistvara rahakotid pakuvad kasutajale kahekordset kaitset: ühelt poolt kaitsevad nad teie bitcoine kaugrünnakute eest, hoides privaatvõtmeid võrguühenduseta, ja teiselt poolt pakuvad nad üldiselt paremat füüsilist vastupanu võtmete kättesaamise katsetele. Ja just nendel 2 turvakriteeriumil saab hinnata ja järjestada turul saadaolevaid erinevaid mudeleid.

Selles õpetuses pakun avastada ühte neist lahendustest: **Ledger Nano S Plus**.

![NANO S PLUS LEDGER](assets/notext/01.webp)

## Sissejuhatus Ledger Nano S Plus'sse

Ledger Nano S Plus on riistvara rahakott, mida toodab Prantsuse ettevõte Ledger, turuhinnaga 79 €.

![NANO S PLUS LEDGER](assets/notext/02.webp)

Nano S Plus on varustatud CC EAL6+ sertifitseeritud kiibiga ("*turvaelement*"), mis pakub teile täiustatud kaitset riistvara füüsiliste rünnakute vastu. Ekraani ja nuppe kontrollib otseselt see kiip. Sageli tõstatatud kriitikapunkt on see, et selle kiibi kood ei ole avatud lähtekoodiga, mis nõuab teatud usaldust selle komponendi terviklikkuse vastu. Siiski auditeerivad seda elementi sõltumatud eksperdid.

Kasutamise osas toimib Ledger Nano S Plus ainult juhtmega USB-C ühenduse kaudu.

Ledger eristub oma konkurentidest alati väga kiire uute Bitcoin'i funktsioonide, nagu näiteks Taproot või Miniscript, omaksvõtuga, mida hinnatakse kõrgelt.
Pärast selle testimist leian, et Ledger Nano S Plus on suurepärane sissejuhatav riistvara rahakott. See pakub kõrgetasemelist turvalisust mõistliku hinnaga. Selle peamine puudus võrreldes sama hinnaklassi teiste seadmetega on asjaolu, et püsivara kood ei ole avatud lähtekoodiga. Samuti on Nano S Plus ekraan suhteliselt väike võrreldes kallimate mudelitega, nagu Ledger Flex või Coldcard Q1. Siiski on selle liides väga hästi kujundatud: hoolimata selle kahest nupust ja väikesest ekraanist, on see lihtne kasutada, sealhulgas edasijõudnute funktsioonide jaoks, nagu BIP39 paroolilause. Ledger Nano S Plus'il ei ole akut, õhulõhe ühendust, kaamerat ega mikro SD porti, kuid see on selle hinnaklassi jaoks täiesti normaalne.
Minu arvates on Ledger Nano S Plus hea valik oma Bitcoin'i rahakoti turvamiseks ja sobib nii algajatele kui ka kesktaseme kasutajatele. Siiski, selles hinnaklassis eelistan ma isiklikult Trezor Safe 3-t, mis pakub umbes samu võimalusi. Trezori eelis, minu arvates, on selle turvaelemendi haldamises: mnemooniline fraas ja võtmed hallatakse ainult avatud lähtekoodiga, kuid saavad siiski kiibi kaitsest kasu. Trezori puuduseks on see, et nad on uute funktsioonide rakendamisel mõnikord väga aeglased, erinevalt Ledgerist.
## Kuidas osta Ledger Nano S Plus?

Ledger Nano S Plus on müügil [ametlikul veebilehel](https://shop.ledger.com/products/ledger-nano-s-plus). Füüsilises poes ostmiseks leiate [sertifitseeritud edasimüüjate nimekirja](https://www.ledger.com/reseller) Ledgeri veebisaidilt.

## Eeltingimused

Kui olete oma Ledger Nano kätte saanud, on esimene samm pakendi kontrollimine, et veenduda, et seda ei ole avatud. Kui see on kahjustatud, võib see viidata sellele, et riistvara rahakott on kompromiteeritud ja ei pruugi olla autentne.

Avamisel peaksite leidma karbist järgmised esemed:
- Ledger Nano S Plus;
- USB-C kuni USB-A kaabel;
- Kasutusjuhend;
- Kaardid oma mnemoonilise fraasi üles kirjutamiseks.

Selle õpetuse jaoks on vaja kahte tarkvararakendust: Ledger Live Ledgeri seadistamiseks ja Sparrow Wallet oma Bitcoin'i rahakoti haldamiseks. Laadige [Ledger Live](https://www.ledger.com/ledger-live) ja [Sparrow Wallet](https://sparrowwallet.com/download/) alla nende ametlikelt veebisaitidelt.

![NANO S PLUS LEDGER](assets/notext/03.webp)
Nende kahe tarkvaraprogrammi puhul soovitan tungivalt kontrollida nii nende autentsust (GnuPG abil) kui ka nende terviklikkust (hashi kaudu) enne nende installimist oma masinasse. Kui te ei ole kindel, kuidas seda teha, võite järgida seda teist õpetust:
https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Kuidas seadistada Ledger Nano?

Ühendage oma Nano arvutiga, kus on installitud Ledger Live ja Sparrow Wallet. Ledgeril navigeerimiseks kasutage vasakut nuppu vasakule liikumiseks ja paremat nuppu paremale liikumiseks. Valiku kinnitamiseks või valimiseks vajutage mõlemat nuppu korraga.

![NANO S PLUS LEDGER](assets/notext/04.webp)

Kerige läbi erinevate tutvustuslehtede ja seejärel alustamiseks klõpsake mõlemal nupul.

![NANO S PLUS LEDGER](assets/notext/05.webp)

Valige valik "*Seadista kui uus seade*".

![NANO S PLUS LEDGER](assets/notext/06.webp)

Valige PIN-kood, mida kasutatakse teie Ledgeri avamiseks. See on seega kaitse volitamata füüsilise juurdepääsu vastu. See PIN-kood ei mängi rolli teie rahakoti krüptograafiliste võtmete tuletamisel. Seega, isegi ilma sellele PIN-koodile juurdepääsuta, võimaldab teie 24-sõnaline mnemooniline fraas teil oma bitcoine uuesti kätte saada.

![NANO S PLUS LEDGER](assets/notext/07.webp)

Soovitatav on valida võimalikult juhuslik 8-kohaline PIN-kood. Samuti veenduge, et salvestate selle koodi erinevasse kohta, kus teie Ledger Nano S Plus asub (näiteks paroolihalduris).

Kasutage nuppudega numbrite kohal liikumiseks, seejärel valige iga number, klõpsates mõlemal nupul korraga.

![NANO S PLUS LEDGER](assets/notext/08.webp)

Sisestage oma PIN-kood teist korda selle kinnitamiseks.
Teie Nano annab juhiseid, kuidas hallata teie taastefraasi.

**See mnemooniline fraas annab täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele**. Igaüks, kes on selle fraasi valduses, võib teie vahendid varastada, isegi ilma füüsilise juurdepääsuta teie Ledgerile. 24-sõnaline fraas võimaldab teil taastada juurdepääsu oma bitcoinidele kaotuse, varguse või teie Ledger Nano S Plus kahjustumise korral. Seetõttu on väga oluline hoolikalt salvestada ja hoida seda turvalises kohas.

Võite selle üles kirjutada kaasasolevale papptükile, või suurema turvalisuse tagamiseks soovitan ma graveerida selle roostevabast terasest alusele, et kaitsta tulekahju, üleujutuste või kokkuvarisemise ohtude eest.

Võite neid juhiseid sirvida ja lehti vahele jätta, klõpsates paremat nuppu.

Ledger loob teie mnemoonilise fraasi kasutades oma juhusliku numbri generaatorit. Veenduge, et teid selle toimingu ajal ei jälgitaks. Kirjutage Ledgeri poolt antud sõnad üles füüsilisele meediumile, mille olete valinud. Oma turvastrateegiast lähtuvalt võiksite kaaluda fraasi mitme täieliku füüsilise koopia tegemist (kuid oluline on, et te seda ei jaotaks). On oluline hoida sõnad nummerdatuna ja järjestikuses järjekorras.
***Ilmselgelt ei tohiks te neid sõnu kunagi internetis jagada, vastupidiselt sellele, mida ma teen selles õpetuses. See näidisrahakott kasutatakse ainult Testnetis ja kustutatakse pärast õpetust.***

Järgmiste sõnade juurde liikumiseks klõpsake paremat nuppu.

Kui kõik sõnad on üles märgitud, klõpsake järgmise sammu juurde liikumiseks kahte nuppu.

Klõpsake kahtluse "*Kinnita oma taastefraas*", seejärel valige oma mnemoonilise fraasi sõnad nende järjekorras, et kinnitada, et olete need õigesti üles märkinud. Kasutage valikute vahel liikumiseks vasakut ja paremat nuppu, seejärel valige õige sõna, klõpsates kahte nuppu. Jätkake seda protseduuri kuni 24. sõnani.

Kui kinnitatav fraas vastab täpselt sellele, mille Ledger teile eelmises etapis andis, võite jätkata. Kui mitte, näitab see, et teie füüsiline varukoopia mnemoonilisest fraasist on vale ja peate protsessi uuesti alustama.

Ja nii ongi, teie seeme on teie Ledger Nano S Plus'is õigesti loodud. Enne uue Bitcoin'i rahakoti loomist sellest seemnest, uurigem koos seadme seadeid.

## Kuidas muuta oma Ledgeri seadeid?

Seadetele juurdepääsemiseks hoidke mõnda sekundit all kahte nuppu.

Klõpsake menüül "*Settings*".

Ja valige "*General*".

Menüüs "*Language*" saate muuta kuvakeelt.

Menüüs "*Brightness*" saate reguleerida ekraani heledust. Ülejäänud üldseaded meid praegu ei huvita.

Nüüd minge jaotisse "*Security*" seaded.
"*PIN-koodi muutmine*" võimaldab teil muuta oma PIN-koodi. ![NANO S PLUS LEDGER](assets/notext/22.webp)
"*Salasõna*" võimaldab teil seadistada BIP39 salasõna. Salasõna on valikuline parool, mis koos teie taastefraasiga pakub teie rahakotile lisakihti turvalisust.

![NANO S PLUS LEDGER](assets/notext/23.webp)

Praegu genereeritakse teie rahakott 24-sõnalise mnemoonilise fraasi põhjal. See taastefraas on väga oluline, kuna see võimaldab teil kaotuse korral taastada kõik oma rahakoti võtmed. Siiski kujutab see endast ühtset rikkepunkti (SPOF). Kui see on kompromiteeritud, on teie bitcoiinid ohus. Siin tulebki mängu salasõna. See on valikuline parool, mille võite suvaliselt valida, mis lisandub mnemoonilisele fraasile, et suurendada rahakoti turvalisust.

Salasõna ei tohiks segi ajada PIN-koodiga. See mängib rolli teie krüptograafiliste võtmete tuletamisel. See töötab koos mnemoonilise fraasiga, muutes seemet, millest võtmed genereeritakse. Seega, isegi kui keegi saab kätte teie 24-sõnalise fraasi, ilma salasõnata ei pääse nad teie vahenditele ligi. Salasõna kasutamine loob sisuliselt uue rahakoti eristuvate võtmetega. Salasõna muutmine (isegi veidi) genereerib erineva rahakoti.

Salasõna on väga võimas vahend oma bitcoiinide turvalisuse suurendamiseks. Siiski on väga oluline mõista, kuidas see töötab enne selle rakendamist, et vältida juurdepääsu kaotamist oma rahakotile. Seetõttu soovitan teil konsulteerida selle teise õpetusega, kui soovite oma Ledgeril salasõna seadistada:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

"*PIN-luku*" menüü võimaldab teil seadistada ja aktiveerida oma Ledgeri automaatse lukustamise pärast kindlaksmääratud tegevusetuse perioodi.

![NANO S PLUS LEDGER](assets/notext/24.webp)

"*Ekraanisäästja*" menüü võimaldab teil reguleerida oma Ledger Nano uinakurežiimi. Pange tähele, et ekraanisäästja ei nõua ärkamisel PIN-koodi sisestamist, välja arvatud juhul, kui "*PIN-luku*" valik on aktiveeritud vastavalt uinakurežiimile. See funktsioon on eriti kasulik Ledger Nano X seadmetele, mis on varustatud akuga, et vähendada nende energiatarbimist.

![NANO S PLUS LEDGER](assets/notext/25.webp)

Lõpuks võimaldab "*Seadme lähtestamine*" menüü teil teie Ledgeri lähtestada. Jätkake selle lähtestamisega ainult siis, kui olete kindel, et see ei sisalda ühtegi bitcoiinide turvamiseks vajalikku võtit, kuna võite jäädavalt kaotada juurdepääsu oma vahenditele. See valik võib olla kasulik tühja taastamise testi tegemiseks, kuid räägin sellest veidi hiljem rohkem.

![NANO S PLUS LEDGER](assets/notext/26.webp)
## Kuidas installida Bitcoin rakendust?

Alustage Ledger Live tarkvara käivitamisega oma arvutis, seejärel ühendage ja avage oma Ledger Nano. Ledger Live'is minge menüüsse "*Minu Ledger*". Teilt küsitakse juurdepääsu lubamist teie Nanole.

![NANO S PLUS LEDGER](assets/notext/27.webp)

Kinnitage juurdepääs oma Ledgeril, klõpsates kahe nupu peal.

![NANO S PLUS LEDGER](assets/notext/28.webp)

Esmalt veenduge Ledger Live'is, et kuvatakse "*Ehtsuskontroll*". See kinnitab, et teie seade on autentne.

![NANO S PLUS LEDGER](assets/notext/29.webp)

Kui teie Ledger Nano tarkvara ei ole ajakohane, pakub Ledger Live automaatselt selle uuendamist. Vajadusel klõpsake "*Uuenda tarkvara*", seejärel "*Paigalda uuendus*", et alustada paigaldamist. Oma Ledgeril kinnitage klõpsates kahe nupu peal, seejärel oodake paigaldamise ajal.
Lõpuks lisame Bitcoin rakenduse. Selleks klõpsake Ledger Live'is nupul "*Install*" kõrval "*Bitcoin (BTC)*".
![NANO S PLUS LEDGER](assets/notext/30.webp)

Rakendus installitakse teie Nano'le.

![NANO S PLUS LEDGER](assets/notext/31.webp)

Edaspidi ei ole teil Ledger Live tarkvara igapäevaseks rahakoti haldamiseks enam vaja. Võite aeg-ajalt sinna tagasi pöörduda, et uuendada püsivara, kui on saadaval uued versioonid. Kõige muu jaoks kasutame Sparrow Walletit, mis on palju terviklikum tööriist Bitcoin rahakoti efektiivseks haldamiseks.

![NANO S PLUS LEDGER](assets/notext/32.webp)

## Kuidas seadistada uut Bitcoin rahakotti Sparrow'ga?

Avage Sparrow Wallet ja jätke sissejuhatavad lehed vahele, et jõuda avalehele. Kontrollige, et olete õigesti ühendatud noodiga, jälgides ekraani paremas alanurgas asuvat lülitit.

![NANO S PLUS LEDGER](assets/notext/33.webp)

Soovitan tungivalt kasutada omaenda Bitcoin noodit. Selles õpetuses kasutan avalikku noodit (kollane), kuna olen testnetis, kuid tavakasutuseks on parem valida kohalik Bitcoin Core (roheline) või Electrum server, mis on ühendatud kaugnoodiga (sinine).

Klõpsake menüül "*File*" seejärel "*New Wallet*".

![NANO S PLUS LEDGER](assets/notext/34.webp)

Valige sellele rahakotile nimi, seejärel klõpsake nupul "*Create Wallet*".

![NANO S PLUS LEDGER](assets/notext/35.webp)

"*Script Type*" rippmenüüs valige skripti tüüp, mida kasutatakse teie bitcoinide turvamiseks. Soovitan valida "*Taproot*", või kui see pole saadaval, siis "*Native SegWit*".

![NANO S PLUS LEDGER](assets/notext/36.webp)
Klõpsake nupul "*Connected Hardware Wallet*".
![NANO S PLUS LEDGER](assets/notext/37.webp)

Kui te pole seda veel teinud, ühendage oma Ledger Nano S Plus arvutiga, avage see oma PIN-koodiga ja seejärel avage "*Bitcoin*" rakendus, klõpsates Bitcoin logo peal korra kahe nupuga.

*Selles õpetuses kasutan Bitcoin Testnet rakendust, kuid protseduur jääb samaks põhivõrgu jaoks.*

![NANO S PLUS LEDGER](assets/notext/38.webp)

Sparrow'is klõpsake nupul "*Scan*".

![NANO S PLUS LEDGER](assets/notext/39.webp)

Seejärel klõpsake nupul "*Import Keystore*".

![NANO S PLUS LEDGER](assets/notext/40.webp)

Nüüd näete oma rahakoti üksikasju, sealhulgas teie esimese konto laiendatud avalikku võtit. Klõpsake nupul "*Apply*", et lõpetada rahakoti loomine.

![NANO S PLUS LEDGER](assets/notext/41.webp)

Valige tugev parool, et kaitsta juurdepääsu Sparrow Walletile. See parool tagab juurdepääsu turvalisuse teie rahakoti andmetele Sparrow's, mis aitab kaitsta teie avalikke võtmeid, aadresse, silte ja tehingute ajalugu igasuguse volitamata juurdepääsu eest.

Soovitan teil see parool salvestada paroolihaldurisse, et te seda ei unustaks.

![NANO S PLUS LEDGER](assets/notext/42.webp)

Ja ongi kõik, teie rahakott on nüüd loodud!

![NANO S PLUS LEDGER](assets/notext/43.webp)
Enne kui saate oma rahakotti esimesed bitcoini, **soovitan tungivalt teha kuiva trenni taastamise testi**. Pane kirja viiteteave, näiteks sinu xpub, seejärel lähtesta oma Ledger Nano, kui rahakott on veel tühi. Pärast seda proovi oma rahakotti Ledgeris taastada, kasutades oma paberil varukoopiaid. Kontrolli, kas taastamise järel genereeritud xpub ühtib algsega, mille üles märkisid. Kui jah, võid olla kindel, et sinu paberil varukoopiad on usaldusväärsed.
Et rohkem teada saada, kuidas taastamise testi teha, soovitan konsulteerida selle teise õpetusega:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kuidas vastu võtta bitcoine Ledger Nano abil?

Klõpsa vahekaardil "*Receive*".

![NANO S PLUS LEDGER](assets/notext/44.webp)

Ühenda oma Ledger Nano S Plus arvutiga, ava see oma PIN-koodiga, seejärel ava "*Bitcoin*" rakendus.

![NANO S PLUS LEDGER](assets/notext/45.webp)
Enne Sparrow Wallet'is pakutud aadressi kasutamist, kontrolli seda oma Ledgeri ekraanil. See praktika võimaldab sul kinnitada, et Sparrow'is kuvatav aadress ei ole petlik ja et riistvara rahakott tõepoolest omab privaatvõtit, mis on vajalik hiljem selle aadressiga turvatud bitcoinide kulutamiseks. See aitab vältida mitut tüüpi rünnakuid.
Selle kontrollimiseks klõpsa nupul "*Display Address*".

![NANO S PLUS LEDGER](assets/notext/46.webp)

Veendu, et sinu Ledgeril kuvatav aadress ühtib Sparrow Wallet'is näidatuga. Soovitatav on seda kontrolli teha vahetult enne oma aadressi saatjale andmist, et olla selle kehtivuses kindel. Aadressi täielikuks vaatamiseks võid kasutada nuppe.

![NANO S PLUS LEDGER](assets/notext/47.webp)

Seejärel klõpsa "*Approve*", kui aadressid on tõepoolest identsed.

![NANO S PLUS LEDGER](assets/notext/48.webp)

Sa võid lisada "*Label*" selleks, et kirjeldada bitcoini allikat, mis selle aadressiga turvatakse. See on hea tava, mis aitab sul paremini hallata oma UTXO-sid.

![NANO S PLUS LEDGER](assets/notext/49.webp)

Lisateabe saamiseks sildistamise kohta soovitan samuti tutvuda selle teise õpetusega:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Seejärel võid kasutada seda aadressi bitcoinide vastuvõtmiseks.

![NANO S PLUS LEDGER](assets/notext/50.webp)

## Kuidas saata bitcoine Ledger Nano abil?

Nüüd, kui oled oma rahakotti turvatud Nano S Plus'iga saanud esimesed satid, võid neid ka kulutada! Ühenda oma Ledger arvutiga, ava see, käivita Sparrow Wallet ja seejärel mine vahekaardile "*Send*", et koostada uus tehing.

![NANO S PLUS LEDGER](assets/notext/51.webp)

Kui soovid teha "*coin control*", mis tähendab konkreetsete UTXO-de valimist tehingus kasutamiseks, mine vahekaardile "*UTXOs*". Vali UTXO-d, mida soovid kulutada, seejärel klõpsa "*Send Selected*". Sind suunatakse tagasi sama "*Send*" vahekaardi ekraanile, kuid sinu UTXO-d on juba tehingu jaoks valitud.

![NANO S PLUS LEDGER](assets/notext/52.webp)

Sisesta sihtkoha aadress. Mitme aadressi sisestamiseks võid klõpsata nupul "*+ Add*".

![NANO S PLUS LEDGER](assets/notext/53.webp)

Märgi "*Label*", et meeles pidada selle kulutuse eesmärki.

![NANO S PLUS LEDGER](assets/notext/54.webp)
Valige saadetava summa sellele aadressile.
![NANO S PLUS LEDGER](assets/notext/55.webp)

Kohandage tehingu tasu määra vastavalt praegusele turuolukorrale.

![NANO S PLUS LEDGER](assets/notext/56.webp)
Veenduge, et kõik teie tehingu seaded on õiged, seejärel klõpsake nupul "*Loo Tehing*".
![NANO S PLUS LEDGER](assets/notext/57.webp)

Kui kõik tundub teile korras, klõpsake nupul "*Finaliseeri Tehing Allkirjastamiseks*".

![NANO S PLUS LEDGER](assets/notext/58.webp)

Klõpsake nupul "*Allkirjasta*".

![NANO S PLUS LEDGER](assets/notext/59.webp)

Klõpsake nupul "*Allkirjasta*" oma Ledger Nano S Plus kõrval.

![NANO S PLUS LEDGER](assets/notext/60.webp)

Kontrollige oma Ledgeri ekraanil tehingu seadeid, sealhulgas saaja aadressi, saadetud summat ja tasu suurust.

![NANO S PLUS LEDGER](assets/notext/61.webp)

Kui kõik tundub teile korras, vajutage "*Allkirjasta tehing*" nupule, vajutades kahte nuppu.

![NANO S PLUS LEDGER](assets/notext/62.webp)

Teie tehing on nüüd allkirjastatud. Kontrollige kõik üle, et kõik tunduks korras, seejärel klõpsake nupul "*Edasta Tehing*", et see Bitcoin'i võrgus levitada.

![NANO S PLUS LEDGER](assets/notext/63.webp)

Leiate selle Sparrow Wallet'i "*Tehingud*" vahelehelt.

![NANO S PLUS LEDGER](assets/notext/64.webp)

Palju õnne, nüüd olete kursis Ledger Nano S Plus'i põhikasutusega Sparrow Wallet'iga! Tulevases õpetuses vaatame, kuidas kasutada Ledgerit koos Lianaga, et ära kasutada Miniscripti.

Kui leidsite selle õpetuse kasuliku, oleksin tänulik, kui jätaksite allapoole pöidla üles. Julgelt jagage seda artiklit oma sotsiaalvõrgustikes. Suur tänu!

Soovitan teil samuti tutvuda selle täieliku õpetusega Ledger Flex kohta:

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a