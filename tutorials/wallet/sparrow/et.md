---
name: Varblane Wallet
description: Sparrow Wallet paigaldamine, konfigureerimine ja kasutamine
---
![cover](assets/cover.webp)

Sparrow Wallet on Craig Raw poolt välja töötatud isehaldatav Bitcoin portfellihaldustarkvara. Seda avatud lähtekoodiga tarkvara hindavad bitcoin'id oma paljude funktsioonide ja intuitiivse Interface eest.

Sparrow'd saab kasutada kahel viisil:


- Nagu Hot Wallet, kus teie isiklikud võtmed on salvestatud teie arvutisse.
- Cold Wallet haldurina, kus privaatvõtmeid hoitakse Hardware Wallet-l. Selles režiimis manipuleerib Sparrow ainult avalikku Wallet teavet, jälgib vahendeid, genereerib aadresse ja koostab tehinguid, kuid Hardware Wallet allkiri on vajalik, et need tehingud oleksid kehtivad. Seega võib see asendada selliseid rakendusi nagu Ledger Live või Trezor Suite.

Sparrow toetab ühe ja mitme allkirjaga rahakotte ning võimaldab mitme rahakoti sujuvat haldamist. Näiteks saate samaaegselt juhtida ühte Wallet, mis on ühendatud Ledger-ga, teist Trezoriga, ning samuti Hot Wallet.

Tarkvara pakub ka täiustatud mündikontrollifunktsioone, mis võimaldavad teil täpselt valida, milliseid UTXOsid teie tehingutes kasutada, et optimeerida oma konfidentsiaalsust.

Mis puutub ühendusse, siis Sparrow võimaldab teil ühendada oma Bitcoin sõlme kas eemalt Electrumi serveri kaudu või Bitcoin Core'i abil. Samuti on võimalik kasutada avalikku sõlme, kui teil ei ole veel oma sõlme. Kaugühendused toimuvad Tori kaudu.

## Paigaldage Sparrow Wallet

Mine [ametlikule Sparrow Wallet allalaadimislehele](https://sparrowwallet.com/download/) ja vali oma operatsioonisüsteemile vastav tarkvaraversioon.

![Image](assets/fr/01.webp)

Oluline on kontrollida tarkvara terviklikkust ja autentsust enne selle paigaldamist. Kui te ei tea, kuidas seda teha, leiate täieliku õpetuse siit :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kui Sparrow on paigaldatud, võite jätta esialgsed selgitavad ekraanid vahele ja minna otse ühenduse haldamise ekraanile.

![Image](assets/fr/02.webp)

## Ühendamine Bitcoin võrguga

Bitcoin võrguga suhtlemiseks ja oma tehingute edastamiseks peab Sparrow olema ühendatud Bitcoin sõlme. Selle ühenduse loomiseks on kolm peamist võimalust:


- 🟡 Kasutades avalikku sõlme, st ühendudes kolmanda osapoole sõlme, mis lubab selliseid ühendusi. Kui sul ei ole oma Bitcoin sõlme, võimaldab see võimalus Sparrow'ga kiiresti alustada. Kuid sõlme, millega te ühendute, näeb kõiki teie tehinguid, mis võib ohustada teie konfidentsiaalsust. Kontroll oma võtmete üle on oluline, kuid oma sõlme omamine on veelgi parem. Seega kasutage seda võimalust ainult siis, kui te alles alustate, olles samas teadlik oma privaatsust ohustavatest riskidest.
- 🟢 Ühendamine Bitcoin tuumasõlmega. Kui teil on oma Bitcoin Core'i sõlmpunkt, saate selle ühendada Sparrow Wallet-ga kas lokaalselt, kui Bitcoin Core on paigaldatud samasse masinasse, või eemalt.
- 🔵 Ühendus Electrumi serveri kaudu. Kui teie Bitcoin-sõlm on varustatud Electrumiga, nagu näiteks node-in-a-box-lahenduste puhul, nagu Umbrel või Start9, siis saate sellega Sparrow'st eemalt ühendust luua.

**Võimalik on kasutada ühendust Electrs või Bitcoin Core'i kaudu oma sõlmes, et vähendada vajadust usaldada kolmandat osapoolt ja optimeerida oma konfidentsiaalsust**

### Ühenda avaliku sõlme 🟡

Avaliku sõlme ühendamine on väga lihtne. Klõpsake vahekaardil "*Public Server*".

![Image](assets/fr/03.webp)

Valige rippmenüüst sõlme.

![Image](assets/fr/04.webp)

Seejärel klõpsake nuppu "*Testiühendus*".

![Image](assets/fr/05.webp)

Pärast ühendamist kuvab Sparrow Wallet Interface paremas alumises nurgas kollase märkeruudu, mis näitab, et olete ühendatud avaliku sõlmpunktiga.

![Image](assets/fr/06.webp)

### Bitcoin tuumaga ühendamine 🟢

Teine meetod Bitcoin sõlme ühendamiseks on Sparrow'i ühendamine Bitcoin tuumaga. Kui Bitcoin Core on paigaldatud samasse masinasse, toimub autentimine küpsiste faili kaudu. Kui Bitcoin Core asub kaugemas masinas, tuleb kasutada parooli, mis on määratud failis `Bitcoin.conf`.

Pange tähele, et kui te kasutate kärbitud Bitcoin tuumasõlme, ei saa te taastada Wallet, mis sisaldab tehinguid, mis eelnevad lokaalselt salvestatud plokkidele. Sparrow'l loodud uue Wallet puhul ei ole see aga probleem: teie uued tehingud on nähtavad, isegi kui sõlme on kärbitud.

Bitcoin Core-sõlme konfigureerimiseks saate sõltuvalt teie operatsioonisüsteemist tutvuda ühega järgmistest juhendmaterjalidest:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Mine Sparrow's vahekaardile "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**With Bitcoin Core local:**

Kui teie arvutisse on paigaldatud Bitcoin Core, otsige tarkvara failide hulgast üles fail "Bitcoin.conf". Kui seda faili ei ole olemas, saate selle luua. Avage see tekstiredaktoriga ja sisestage järgmine rida:

```ini
server=1
```

Seejärel salvestage oma muudatused.

Seda saate teha ka Bitcoin-QT Interface graafiku kaudu, kui navigeerite "*Settings*" juurde > "*Options...*" ja aktiveerige valik "*Enable RPC server*".

Ärge unustage pärast nende muudatuste tegemist tarkvara taaskäivitamist.

![Image](assets/fr/08.webp)

Seejärel naaske Sparrow Wallet-sse ja sisestage oma küpsiste faili tee, mis tavaliselt asub samas kaustas nagu `Bitcoin.conf`, sõltuvalt teie operatsioonisüsteemist:

| **macOS** | ~/Library/Application Support/Bitcoin | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Jäta muud parameetrid vaikimisi, URL `127.0.0.1` ja port `8332`, seejärel klõpsa "*Testiühendus*".

![Image](assets/fr/10.webp)

Ühendus on loodud. Parempoolsesse alumisse nurka ilmub Green märkeruut, mis näitab, et olete ühendatud Bitcoin Core-sõlmega.

![Image](assets/fr/11.webp)

**Bitcoin Core kaugjuhtimispuldiga:**

Kui Bitcoin Core on paigaldatud teise masinasse, mis on ühendatud samasse võrku, otsige kõigepealt tarkvara failide hulgast üles fail "Bitcoin.conf". Kui seda faili veel ei ole, võite selle luua. Avage see fail tekstiredaktoriga ja lisage järgmine rida:

```ini
server=1
```

Pärast faili redigeerimist salvestage see kindlasti oma operatsioonisüsteemi jaoks sobivasse kausta:

| **macOS** | ~/Library/Application Support/Bitcoin | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin | ~/.Bitcoin |

Seda toimingut saab teha ka graafilise Bitcoin-QT Interface kaudu. Avage menüü "*Settings*", seejärel "*Options...*" ja aktiveerige valik "*Enable RPC server*", märgistades vastava kasti. Kui faili `Bitcoin.conf` ei ole olemas, saate selle luua otse sellest Interface-st, klõpsates "*Open Configuration File*".

![Image](assets/fr/12.webp)

Leidke Bitcoin Core'i majutava masina IP-aadress Address teie kohalikus võrgus. Selleks võite kasutada sellist tööriista nagu [Angry IP Scanner](https://angryip.org/). Oletame, et teie sõlme IP Address on `192.168.1.18`.

Lisage faili `Bitcoin.conf` järgmised read, seades `rpcbind=192.168.1.18`, et see vastaks teie sõlme IP Address-le.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Lisage faili `Bitcoin.conf` kasutajanimi ja parool kaugühenduste jaoks. Asendage `loic` kindlasti oma kasutajanimega ja `my_password` tugeva parooliga:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Pärast faili muutmist ja salvestamist käivitage Bitcoin-QT tarkvara uuesti.

Nüüd võite naasta Sparrow Wallet juurde. Minge vahekaardile "*Kasutaja / Pass*". Sisestage kasutajanimi ja parool, mille seadistasite failis `Bitcoin.conf`. Jäta muud parameetrid vaikimisi, st URL `127.0.0.1` ja port `8332`. Seejärel klõpsake nuppu "*Test Connection*".

![Image](assets/fr/15.webp)

Ühendus on loodud. Paremasse alumisse nurka ilmub Green märkeruut, mis näitab, et olete ühendatud Bitcoin Core-sõlmega.

![Image](assets/fr/16.webp)

### Ühendamine Electrumi serveriga 🔵

Viimane võimalus ühendamiseks on kasutada Electrumi kaugserverit. See meetod võimaldab teil oma sõlmpunktiga Tor'i kaudu teisest seadmest ühendust luua ja kasutada indekseerija eeliseid, et sirvida oma portfelle Sparrow's kiiremini. See sobib eriti hästi, kui teil on node-in-a-box lahendus nagu Umbrel või Start9, mis võimaldab Electrumi paigaldada ühe klõpsuga.

Selleks hankige oma Electrumi serveri Tor `.onion' Address. Umbreliga leiate selle näiteks Electrs rakendusest.

![Image](assets/fr/17.webp)

Sparrow Wallet-s avage vahekaart "*Privaatne Electrum*".

![Image](assets/fr/18.webp)

Sisestage oma Tor Address ettenähtud kohta. Muud seaded võivad jääda vaikimisi. Seejärel klõpsake "*Testiühendus*".

![Image](assets/fr/19.webp)

Ühendus on kinnitatud. Kui sulgete selle akna, ilmub paremasse alumisse nurka sinine märkeruut, mis näitab, et olete ühendatud Electrumi serveriga.

![Image](assets/fr/20.webp)

## Loo soe portfell

Nüüd, kui Sparrow Wallet on konfigureeritud Bitcoin võrguga suhtlemiseks, olete valmis looma oma esimese Wallet. See lõik juhendab teid Hot Wallet, st Wallet, mille privaatvõtmed on salvestatud teie arvutisse, loomisel. Kuna teie arvuti on keeruline masin, mis on ühendatud internetti, kujutab see endast väga suurt ründepinda. Järelikult tuleks Hot Wallet kasutada ainult piiratud koguses bitcoinide jaoks. Suuremate summade hoidmiseks valige turvaline Wallet koos Hardware Wallet-ga. Kui see on see, mida te otsite, võite edasi minna järgmisesse jaotisse.

Hot Wallet loomiseks klõpsake Sparrow Wallet avakuval vahekaardil "*Fail*" ja seejärel "*Uue Wallet*".

![Image](assets/fr/21.webp)

Sisestage oma portfelli nimi ja klõpsake "*Loo Wallet*".

![Image](assets/fr/22.webp)

Interface ülaosas saate valida, kas soovite luua portfelli "*Ühene allkiri*" või "*Multiallkiri*". Vahetult allpool valige UTXOde lukustamiseks skripti tüüp. Soovitan kasutada viimast standardit: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Seejärel klõpsake nupule "*Uus või imporditud Software Wallet*".

![Image](assets/fr/24.webp)

Valige BIP39 standard, kuna seda toetab praktiliselt kogu Bitcoin portfelli tarkvara. Seejärel valige oma taastamislause pikkus. Praegu piisab 12-sõnalisest fraasist, kuna mõlemad pakuvad sarnast turvalisust, kuid 12-sõnalist fraasi on lihtsam salvestada.

![Image](assets/fr/25.webp)

Klõpsake nupule "*generate New*", et generate oma Wallet Mnemonic fraasi generate. See fraas annab täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda fraasi valdab, võib teie raha varastada, isegi ilma füüsilise juurdepääsuta teie arvutile.

12-sõnaline lause taastab juurdepääsu teie bitcoinidele arvuti kadumise, varguse või purunemise korral. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.

Võite selle graveerida paberile või täiendava turvalisuse tagamiseks graveerida selle roostevabast terasest, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest. Mnemonic kandja valik sõltub teie turvastrateegiast, kuid kui te kasutate Sparrow'd kui mõõdukaid koguseid sisaldavat Wallet sooja kulutust, peaks paberist piisama.

Lisateabe saamiseks selle kohta, kuidas oma Mnemonic fraasi õigesti salvestada ja hallata, soovitan tungivalt jälgida seda teist õpetust, eriti kui olete algaja:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Es on selge, et te ei tohi neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidist Wallet kasutatakse ainult Testnet-l ja see kustutatakse õpetuse lõpus.**

Võite valida ka passphrase BIP39 lisamise, klõpsates kastil "*Kasutage passphrase*". Hoiatus: passphrase kasutamine võib olla väga kasulik, kuid kui te ei mõista, kuidas see töötab, võib see olla väga riskantne. Seepärast soovitan tungivalt lugeda seda lühikest teoreetilist artiklit sel teemal:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kui olete salvestanud oma Mnemonic ja kõik passphrase füüsilisele andmekandjale, klõpsake "*Kinnitage varukoopia*".

![Image](assets/fr/27.webp)

Sisestage uuesti oma 12 sõna, et kinnitada, et need on õigesti salvestatud, seejärel klõpsake "*Loo võtmesalvestus*".

![Image](assets/fr/28.webp)

Seejärel klõpsake "*Import Keystore*", et generate oma portfelli võtmed Mnemonic fraasist.

![Image](assets/fr/29.webp)

Portfelli loomise lõpetamiseks klõpsake nuppu "*Kandideeri*".

![Image](assets/fr/30.webp)

Määrake tugev parool, et tagada juurdepääs oma Sparrow portfellile. Seda parooli on hea mõte hoida paroolihalduris, et te seda ei unustaks. Pange tähele, et see parool ei mängi teie võtmete tuletamisel mingit rolli. Seda kasutatakse ainult juurdepääsuks teie Wallet-le Sparrow Wallet kaudu. Seega piisab teie Mnemonic fraasist ka ilma selle paroolita, et pääseda bitcoinidele ligi mis tahes BIP39-ga ühilduvast rakendusest.

![Image](assets/fr/31.webp)

Teie Hot Wallet on nüüd loodud. Kui te ei kavatse kasutada Hardware Wallet-d koos Sparrow'ga, siis võite selle õpetuse *Bitcoinide vastuvõtmine* osa vahele jätta, kui te ei kavatse kasutada Hardware Wallet-d koos Sparrow'ga.

## Cold portfelli haldamine

Teine viis Sparrow Wallet kasutamiseks on selle seadistamine portfellihaldurina koos Hardware Wallet-ga. Sellise konfiguratsiooni puhul jäävad teie Bitcoin Wallet privaatvõtmed ainult Hardware Wallet-le, samal ajal kui Sparrow pääseb ligi ainult avalikule teabele. See lähenemisviis pakub kõrgemat turvataset kui eespool käsitletud Hot rahakotid, kuna privaatvõtmeid hoitakse spetsiaalses seadmes, mis on sageli turvalise kiibiga, mis ei ole ühendatud internetti ja kujutab endast seetõttu palju väiksemat rünnakupinda kui traditsiooniline arvuti.

Hardware Wallet ühendamiseks Sparrow'ga on kaks peamist võimalust:


- Kaabli abil, mida tavaliselt kasutatakse algtasemel mudelitega nagu Trezor Safe 3 või Ledger Nano S Plus ;
- Air-Gap-režiimis, st ilma otsese traadiga ühenduseta, MicroSD-kaardi või QR-koodi Exchange kaudu.

Sparrow toetab kõiki neid kommunikatsioonimeetodeid ja ühildub enamiku turul olevate riistvaraliste rahakottidega.

Selles õpetuses kasutan ma Ledger Nano S-i koos kaabliga, kuid protseduur on sarnane Air-Gap režiimis. Hardware Wallet jaoks spetsiifilised üksikasjad leiate Plan ₿ Network-le pühendatud õpetusest.

Enne alustamist veenduge, et Wallet on juba konfigureeritud Hardware Wallet-s. Kui kasutate juhtmega ühendust, ühendage see kaabli kaudu arvutiga.

Nn "*Keystore*" (portfelli haldamiseks vajalik avalik teave) importimiseks Sparrow Wallet-sse klõpsake vahekaardil "*Fail*" ja seejärel "*New Wallet*".

![Image](assets/fr/32.webp)

Nimetage oma portfell ja klõpsake "*Loo Wallet*". Soovitan teil sisestada oma Hardware Wallet nime, et seda hiljem hõlpsasti identifitseerida.

![Image](assets/fr/33.webp)

Interface ülaosas saate valida portfelli "*Single Signature*" või "*Multi Signature*" vahel. Meie näite jaoks konfigureerime ühe allkirjaga portfelli.

Vahetult allpool valige UTXOde lukustamiseks skripti tüüp. Kui teie Hardware Wallet toetab seda, soovitan valida "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Järgnevalt erineb menetlus vastavalt teie ühendusmeetodile. Kui kasutate Air-Gap meetodit, valige "*Airapped Hardware Wallet*". Seejärel järgige oma seadmele omaseid juhiseid.

![Image](assets/fr/35.webp)

Kui te kasutate kaabliühendust, nagu minu puhul, valige "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Klõpsake "*Scan*", et Sparrow tuvastaks teie seadme. Veenduge, et see on ühendatud ja lukustamata. Mõne mudeli, näiteks Ledger puhul peate avama rakenduse "*Bitcoin*", et võimaldada tuvastamist.

![Image](assets/fr/37.webp)

Valige "*Import Keystore*".

![Image](assets/fr/38.webp)

Portfelli loomise lõpetamiseks klõpsake nuppu "*Kandideeri*".

![Image](assets/fr/39.webp)

Seadistage tugev parool, et tagada juurdepääs teie Sparrow Wallet-le. See parool kaitseb teie avalikke võtmeid, aadresse ja tehinguajalugu. Soovitame selle salvestada paroolihaldurisse. Pange tähele, et see parool ei mängi teie võtmete tuletamisel mingit rolli. Isegi ilma selleta saate oma Mnemonic abil taastada juurdepääsu oma bitcoinidele mis tahes BIP39-ga ühilduva tarkvara abil.

![Image](assets/fr/40.webp)

Teie haldusportfell on nüüd Sparrow's konfigureeritud.

![Image](assets/fr/41.webp)

## Bitcoinide vastuvõtmine

Nüüd, kui teie Wallet on Sparrow's seadistatud, saate bitcoin'e vastu võtta. Avage lihtsalt menüü "*Vaata*".

![Image](assets/fr/42.webp)

Sparrow kuvab teie Wallet esimese kasutamata Address. Sellele Address-le saate lisada "*Label*", et teile tulevikus nende satoshide päritolu meelde tuletada.

![Image](assets/fr/43.webp)

Kui kasutate Hot Wallet, saab kuvatud Address kohe kasutada kas selle kopeerimise või sellega seotud QR-koodi skaneerimise teel.

Kui kasutate Hardware Wallet, on väga oluline enne seadme kasutamist kontrollida seadme ekraanil Address. Juhtmega seadmete puhul ühendage Hardware Wallet ja vabastage see, seejärel klõpsake Sparrow's "*Display Address*". Veenduge, et teie Hardware Wallet-l kuvatav Address vastab Sparrow's näidatud Address-le.

![Image](assets/fr/44.webp)

Hardware Wallet Air-Gap kasutajate puhul on Address verifitseerimine sõltuvalt seadme mudelist erinev. Täpseid juhiseid leiate spetsiaalsest Plan ₿ Network juhendmaterjalist.

Kui maksja on tehingu edastanud, näete seda vahekaardil "*Tehingud*". Te saate sellel klõpsata, et saada lisateavet, näiteks txid.

![Image](assets/fr/45.webp)

Vahekaardil "*Aadressid*" leiate nimekirja kõigist oma postkasti aadressidest. Näete, kas neid on juba kasutatud ja kas silt on lisatud. *Vastuvõtu*" aadressid on need, mida Sparrow näitab, kui klõpsate "*Võta*" ja mis on mõeldud sissetulevate maksete jaoks. Aadressid "*Vaheta*" on mõeldud Exchange jaoks teie tehingutes, st selleks, et saada tagasi teie UTXOde kasutamata osa sisendist.

![Image](assets/fr/46.webp)

Vahekaardil "*UTXOd*" näete kõiki oma UTXOsid, st teie valduses olevaid Bitcoin fragmente. Näete iga UTXO kogust ja sellega seotud märgistust.

![Image](assets/fr/47.webp)

## Bitcoinide saatmine

Nüüd, kui teil on oma Wallet-s mõned satoshid, on teil ka võimalus neid saata. Kuigi selleks on mitu võimalust, soovitan kasutada menüüd "*UTXOs*", et täpsemalt kontrollida kulutatud münte (*coin control*), mitte minna otse menüüsse "*Send*" (kuigi viimasest võib piisata, kui oled algaja).

![Image](assets/fr/48.webp)

Valige UTXOd, mida soovite selle tehingu sisendina kasutada, seejärel klõpsake nuppu "*Sendage valitud*". See lähenemisviis võimaldab teil valida oma UTXOde hulgast kõige sobivamad allikad vastavalt teie kuludele ja nende laekumisel kohaldatavatele siltidele, et optimeerida maksete konfidentsiaalsust. Veenduge, et valitud UTXOde summa on suurem kui summa, mida soovite saata.

![Image](assets/fr/49.webp)

Sisestage saaja Address väljale "*Pay to*". Address saate skaneerida ka oma veebikaameraga, klõpsates kaamera ikoonil. Nupu "*+Add*" abil saate maksta mitme aadressi eest ühe tehinguga.

![Image](assets/fr/50.webp)

Lisage oma tehingule silt, mis tuletab teile meelde selle eesmärki. See silt seostatakse ka teie võimaliku Exchange-ga.

![Image](assets/fr/51.webp)

Sisestage sellele Address-le saadetav summa.

![Image](assets/fr/52.webp)

Kohandage tasumäär vastavalt praegustele turutingimustele. Seda saate teha, sisestades absoluutse tasu väärtuse või kohandades tasu määra liuguriga.

![Image](assets/fr/53.webp)

Interface allosas saate valida "*Tõhusus*" ja "*Privaatsus*" vahel. Minu puhul ei ole valik "*Privaatsus*" saadaval, kuna mul on selles portfellis ainult üks UTXO. "*Efektiivsus*" vastab klassikalisele tehingule, samas kui "*Privaatsus*" on Stonewall-tüüpi tehing, tehingustruktuur, mis tugevdab teie konfidentsiaalsust, simuleerides mini-CoinJoin, mis muudab ahela analüüsi keerulisemaks.

![Image](assets/fr/54.webp)

Sparrow kuvab kokkuvõtliku diagrammi, mis näitab teie sisendeid, väljundeid ja tehingutasusid (pange tähele, et tasud ei ole tegelikult väljund, vastupidiselt sellele, mida see diagramm näitab). Kui olete kõigega rahul, klõpsake nuppu "*Loo tehing*".

![Image](assets/fr/55.webp)

See viib teid lehele, kus on üksikasjalikult kirjeldatud teie tehingu Elements. Kontrollige, et kõik andmed oleksid õiged, seejärel klõpsake "*Tehingu allkirjastamiseks lõpuleviimine*".

![Image](assets/fr/56.webp)

Oluline on säilitada vaikimisi Sighash. Et mõista, miks, vaadake seda koolituskursust, kus ma selgitan teile kõike, mida te peate Sighashist teadma:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Järgmisel ekraanil varieeruvad valikud sõltuvalt kasutatava Wallet tüübist:


- Hardware Wallet Air-Gapi puhul klõpsake "*Näita QR*", et kuvada PSBT, mille saate oma seadmega allkirjastada, seejärel laadige allkirjastatud PSBT Sparrow'sse, kasutades "*Scan QR*". Valik "*Save Transaction*" töötab sarnaselt, kuid vahetustega microSD kaardil ;
- Hot Wallet puhul klõpsake lihtsalt "*Sign*" ja sisestage allkirjastamiseks Wallet parool ;
- Juhtmega Hardware Wallet puhul klõpsake ka "*Sign*", et saata allkirjastamata tehing oma seadmesse.

![Image](assets/fr/57.webp)

Kontrollige oma Hardware Wallet-lt saaja Address, saadetud summat ja tasusid. Kui kõik on õige, jätkake allkirjastamist.

Kui tehing on allkirjastatud, ilmub see uuesti Sparrow'sse ja on valmis Bitcoin võrgus edastamiseks, et seda hiljem blokki lisada. Kui kõik on korras, klõpsake nuppu "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Teie tehing on nüüd eetrisse saadetud ja ootab kinnitust.

![Image](assets/fr/59.webp)

## Portfellide haldamine ja konfigureerimine Sparrow's

Vahekaardil "*Settings*" leiate üksikasjalikku teavet oma portfelli kohta, näiteks :


- Portfelli tüüp (ühe signeeringuga või multi-sig) ;
- Kasutatud skripti tüüp ;
- Portfellile määratud nimi ;
- Peavõti jäljend;
- Ümbersõidutee ;
- Konto laiendatud avalik võti.

![Image](assets/fr/60.webp)

Nupp "*Eksport*" võimaldab teil eksportida oma portfelli teavet, et saaksite seda kasutada teistes tarkvarades, säilitades samal ajal Sparrow's seadistatud teabe.

Nupu "*Add Account*" abil saate lisada oma portfellile täiendava konto. Konto vastab eraldi postkasti aadresside kogumile. See funktsioon võib olla kasulik näiteks siis, kui soovite eristada isiklikku ja ärikontot ühe Mnemonic fraasiga.

Nupp "*Advanced*" annab juurdepääsu täiustatud seadetele, näiteks Sparrow' Address otsingu kohandamine ja portfelli parooli muutmine.

![Image](assets/fr/61.webp)

Kui sulgete Sparrow Wallet, lukustub Wallet automaatselt. Kui avate tarkvara järgmine kord, kuvatakse aken, milles palutakse teil Wallet lukustus parooliga avada.

![Image](assets/fr/62.webp)

Kui see aken ei avane või kui soovite avada mõne teise portfelli Sparrow's, klõpsake vahekaardil "*Fail*" ja valige "*Open Wallet*".

![Image](assets/fr/63.webp)

See avab teie failihalduri kausta, kus Sparrow salvestab teie rahakotte. Lihtsalt valige Wallet, mida soovite avada, ja sisestage selle avamiseks parool.

![Image](assets/fr/64.webp)

Menüüst "*Fail*" jaotises "*Settings*" leiate Bitcoin võrguühenduse parameetrid, mida on juba eelmistes jaotistes uuritud. Samuti saate reguleerida erinevaid parameetreid, nagu kasutatav ühik, konverteerimiseks kasutatav fiat-valuuta ja teabeallikad.

![Image](assets/fr/65.webp)

Vahekaart "*View*" pakub kohandamisvõimalusi ja juurdepääsu mõnele kasulikule käsule, näiteks "*Refresh Wallet*", mis värskendab teie portfelli tehinguotsingut.

![Image](assets/fr/66.webp)

Vahekaart "*Tööriistad*" koondab mitmeid täiustatud tööriistu, sealhulgas :


- "*Sign/Verify Message*" võimaldab teil tõestada vastuvõtva Address omamist või kontrollida allkirja.
- "*Send mitmele*" pakub lihtsustatud Interface tehingu sooritamiseks mitmele vastuvõtuaadressile korraga, mis on mugav partii kulutuste tegemiseks.
- "*Sweep Private Key*" võimaldab teil saada bitcoin'e, mis on kaitstud lihtsa privaatvõtmega, ja kanda need oma Sparrow Wallet-le. See võib olla eriti kasulik neile, kelle bitcoinid pärinevad 2010. aastate algusest, enne HD-rahakottide ajastut.
- "Kontrollida allalaadimist" kontrollib allalaaditud tarkvara terviklikkust ja autentsust enne selle paigaldamist teie seadmesse.
- "*Restart In*" võimaldab teil lülituda oma rahakottidesse Testnet või Signet võrkudes. See võib olla kasulik, kui soovite kasutada testvõrke, mille mündid ei oma tegelikku väärtust.

![Image](assets/fr/67.webp)

Te teate nüüd kõike Sparrow Wallet tarkvarast, mis on suurepärane vahend Bitcoin portfellide igapäevaseks haldamiseks.

Kui leidsite selle õpetuse kasulikuks, oleksin väga tänulik, kui jätaksite allpool Green pöidla. Võite seda vabalt jagada oma sotsiaalsetes võrgustikes. Tänan teid väga!

Soovitan ka seda teist õpetust, kus ma selgitan, kuidas konfigureerida Hardware Wallet COLDCARD Q koos Sparrow Wallet-ga:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3