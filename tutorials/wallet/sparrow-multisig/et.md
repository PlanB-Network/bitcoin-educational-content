---
name: Varblane Wallet - Multisig
description: Looge Sparrow's mitme allkirjaga portfoolio
---
![cover](assets/cover.webp)



Mitme allkirjaga Wallet (sageli nimetatakse "*Multisig*") on Bitcoin Wallet struktuur, mis nõuab kulutuse lubamiseks mitut krüptograafilist allkirja erinevatest võtmetest. Erinevalt tavalisest ("*singlesig*") Wallet-st, kus UTXO avamiseks piisab ühest privaatvõtmest, põhineb Multisig mudelil **m-of-n**: Wallet-ga seotud _n_ võtmetest peab iga tehingu _m_ tingimata kaasallkirjastama.



See mehhanism võimaldab portfelli kontrolli jagada mitme üksuse või seadme vahel. Näiteks 2-kolmese konfiguratsiooni puhul genereeritakse kolm sõltumatut võtmekomplekti, kuid vahendite vabastamiseks on vaja ainult kahte. Selline arhitektuur vähendab oluliselt võtme kompromiteerimise või kaotamisega seotud riske: varas, kellel on juurdepääs vaid ühele võtmele, ei saa Wallet tühjaks teha ja kasutaja, kes kaotab ühe võtme, saab ülejäänud kahe võtmega ikkagi juurdepääsu oma rahalistele vahenditele.



![Image](assets/fr/01.webp)



Suurema turvalisusega kaasneb aga ka suurem keerukus. Multisig Wallet seadistamine nõuab mitme Mnemonic fraasi (üks iga allkirjafaktori kohta) ja laiendatud avalike võtmete ("*xpub*") kindlustamist. Tõepoolest, kui kasutate Multisig 2-of-3 Wallet, siis Wallet saamiseks peavad teil olema kas kõik kolm Mnemonic fraasi või vähemalt kaks neist kolmest fraasist. Kui teil on aga ainult kaks kolmest fraasist, siis on teil vaja ka juurdepääsu kolmele *xpub*, ilma milleta on võimatu saada välja avalikke võtmeid, mida on vaja nende poolt kaitstud bitcoinide kättesaamiseks.



Kokkuvõtvalt võib öelda, et Multisig portfelli taastamiseks peate :




- Või pääsete juurde kõigile Mnemonic fraasidele, mis on seotud iga allkirjafaktoriga;
- Kas omab minimaalset arvu Mnemonic fraase, mis on künnise järgi allkirjastamiseks vajalik, ja omab ka juurdepääsu kõigi tegurite xpubidele, et saada vajalikke avalikke võtmeid.



![Image](assets/fr/02.webp)



Seda Multisig portfelli varunduste haldamist hõlbustavad *Output Script Descriptors*, mis koondavad kõik fondidele juurdepääsuks vajalikud avalikud andmed. See funktsioon ei ole siiski veel kõikides portfellihaldustarkvarades rakendatud.



Multisig sobib eriti hästi bitcoini kasutajatele, kes soovivad suuremat turvalisust või rahaliste vahendite kollektiivset haldamist: ettevõtted, ühendused, perekonnad või üksikkasutajad, kes omavad märkimisväärset hulka bitcoine. Seda saab kasutada detsentraliseeritud juhtimisskeemide loomiseks, näiteks allkirjastamisõiguse jagamiseks mitme juhi või meeskonnaliikme vahel.



Selles õpetuses õpime, kuidas luua ja kasutada klassikalist mitme allkirjaga Wallet koos **Sparrow Walletga**. Kui soovite luua kohandatud multisignatuurportfelli koos ajamärkidega, soovitan kasutada hoopis Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Eeltingimused



Selles õpetuses näitan teile, kuidas teha Multisig [Sparrow Wallet portfellihaldustarkvara](https://sparrowwallet.com/download/) abil. Kui te pole seda tarkvara veel paigaldanud, siis palun tehke seda kohe. Kui vajate abi, on meil ka üksikasjalik õpetus Sparrow Wallet seadistamise kohta :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Mitme allkirja Wallet loomiseks on vaja erinevaid riistvaralisi rahakotte. Näiteks Multisig 2-de-3 jaoks võiksite kasutada :




- Trezor Model One;
- Ledger Flex;
- Coldcard MK3.



![Image](assets/fr/03.webp)



Multisig konfiguratsioonis on hea mõte kasutada erinevaid Hardware Wallet marki. See tagab, et kui mõnel konkreetsel mudelil tekib tõsine probleem, ei mõjuta see teie Multisig üldist ohutust. Veelgi enam, see võimaldab teil kasutada iga seadme konkreetseid eeliseid. Näiteks minu konfiguratsioonis :





- Trezor Model One on täielikult avatud lähtekoodiga, mis võimaldab kontrollida seed põlvkonda. Kuna see ei ole varustatud turvalise elemendiga, jääb see siiski füüsiliste rünnakute suhtes haavatavaks;





- Ledger Flex kasutab seevastu kontrollimatut patenteeritud püsivara, kuid sisaldab turvalist elementi, mis pakub suurepärast füüsilist kaitset;





- Coldcard on varustatud turvalise elemendiga ja selle kood on otsitav. See on huvitav valik meie konfiguratsiooni jaoks, sest see pakub kontrollfunktsioone, mida teistel mudelitel ei ole.



Enne Multisig Wallet konfigureerimist veenduge, et iga Hardware Wallet on õigesti konfigureeritud (Mnemonic genereerimine ja salvestamine, PIN-koodi määratlemine). Üksikasjalikud juhised leiate meie iga Hardware Wallet kohta käivatest juhendmaterjalidest, näiteks :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Nagu me hiljem selles õpetuses näeme, on võimalik integreerida oma Multisig konfiguratsiooni ka faktor, mis ei ole seotud Hardware Wallet-ga, kuid mille privaatvõtmed on salvestatud teie arvutis. See meetod on ilmselgelt vähem turvaline kui ainuüksi riistvaraliste rahakottide kasutamine, kuid teatud juhtudel võib see olla asjakohane. Näiteks Multisig 2-de-3 puhul võiksite valida kaks riistvaralist rahakotti ja ühe Software Wallet.



## Multisig portfelli loomine



Avage Sparrow Wallet, klõpsake vahekaardil "*Fail*", seejärel valige "*Uue Wallet*".



![Image](assets/fr/04.webp)



Määrake oma mitme allkirjaga portfellile nimi, seejärel klõpsake kinnitamiseks "*Loo Wallet*".



![Image](assets/fr/05.webp)



Valige rippmenüüst "*Policy Type*" valik "*Multi Signature*".



![Image](assets/fr/06.webp)



Paremas ülemises nurgas saate nüüd määratleda oma Multisig võtmete koguarvu ning ka kulude kinnitamiseks vajalike kaasallkirjastajate arvu. Minu näites on tegemist 2-ast-3 skeemiga.



![Image](assets/fr/07.webp)



Akna allosas kuvab Sparrow Wallet kolm "*Keystore*". Igaüks neist tähistab võtmekomplekti. Siin kasutan ma kolme riistvara portfelli, seega vastab iga "*Keystore*" ühele neist. Nüüd konfigureerime neid.



Ma alustan Coldcardiga. Vahelehel "*Keystore 1*" valin valiku "*Airapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Kui seade on külmakaardil lahti lukustatud, lähen menüüsse "*Settings*" ja seejärel "*Multisig Wallets*".



![Image](assets/fr/09.webp)



Selles menüüs saate hallata Multisig portfelle, milles Coldcard osaleb. Ma tahan luua uue, seega valin "*Export XPUB*".



![Image](assets/fr/10.webp)



Kui te haldate ainult ühte kontot, võite lahtri "*Konto number*" tühjaks jätta ja kinnitada otse kinnitamisnupu vajutamisega.



![Image](assets/fr/11.webp)



Seejärel salvestab Coldcard generate faili, mis sisaldab teie xpubi, mis on salvestatud Micro SD-kaardile.



![Image](assets/fr/12.webp)



Sisestage see Micro SD mälupulk arvutisse. Klõpsake Sparrow Wallet-s nupul "*Import File...*" nupu "*Coldcard Multisig*" kõrval, seejärel valige Coldcardiga loodud fail kaardil.



![Image](assets/fr/13.webp)



Teie xpub on edukalt imporditud. Nüüd kordame protseduuri kahe teise riistvaralise rahakotiga.



![Image](assets/fr/14.webp)



Ledger Flexi puhul valin "*Keystore 2*", seejärel klõpsan "*Connected Hardware Wallet*". Veenduge, et Ledger on arvutiga ühendatud, lukustamata ja et rakendus Bitcoin on avatud.



![Image](assets/fr/15.webp)



Seejärel klõpsake nupule "*Scan...*".



![Image](assets/fr/16.webp)



Klõpsake oma riistvaraportfelli nime kõrval nuppu "*Import Keystore*".



![Image](assets/fr/17.webp)



Teine allakirjutanu on nüüd korrektselt registreeritud Sparrow Wallet-s.



![Image](assets/fr/18.webp)



Multisig konfiguratsiooni lõpuleviimiseks kordan täpselt sama protseduuri Trezor One'iga.



![Image](assets/fr/19.webp)



Minu konfiguratsioonis me seda juhtumit ei hõlma, kuid kui soovite lisada allkirja Software Wallet kaudu Sparrow's (Hot Wallet) oma Multisig-sse, klõpsake lihtsalt nupule "*Uus või imporditud Software Wallet*".



Nüüd, kui kõik teie allkirjastatud seadmed on imporditud Sparrow Wallet-sse, saate Multisig loomise lõpule viia, klõpsates "*Kandideeri*".



![Image](assets/fr/20.webp)



Valige tugev parool, et tagada juurdepääs oma Sparrow Wallet Wallet-le. See parool kaitseb teie avalikke võtmeid, aadresse, silte ja tehinguajalugu volitamata juurdepääsu eest.



Ära unusta seda parooli salvestada turvalisse kohta, näiteks paroolihaldurisse, et vältida selle kaotamist.



![Image](assets/fr/21.webp)



## Multisig portfelli varundamine



Nüüd salvestame oma *Output Script Descriptor* Coldcard'ile (see kehtib ainult nende kasutajate kohta, kelle Multisig-s on Coldcard) ja eelkõige hoiame sellest varukoopia sõltumatul andmekandjal.



*Descriptor* sisaldab kõiki teie Multisig portfellis olevaid xpubisid, samuti generate võtmete tuletamise teed. Pidage meeles, mida nägime 1. osas: Multisig portfelli taastamiseks peavad teil olema kas **kõik** Mnemonic fraasid või ainult minimaalne arv, mis on vajalik allkirja künnise saavutamiseks. Viimasel juhul on aga oluline omada ka **puuduvate allakirjutajate xpubisid**. *Descriptor* sisaldab kõiki teie Multisig xpubs.



Kui see ei ole selge, siis pidage meeles järgmist: Multisig saamiseks on vaja iga kasutatud Hardware Wallet kohta minimaalset arvu Mnemonic fraase, sõltuvalt künnisest (minu puhul: 2 fraasi), samuti *Descriptor*.



See *Descriptor* ei sisalda privaatseid võtmeid, vaid ainult avalikke. See tähendab, et see ei anna juurdepääsu rahalistele vahenditele. Seetõttu ei ole see nii kriitiline kui Mnemonic laused, mis annavad täieliku juurdepääsu teie bitcoinidele. *Descriptori* risk on seotud üksnes konfidentsiaalsusega: kompromissi korral võib kolmas isik jälgida kõiki teie tehinguid, kuid ei saa teie raha kulutada.



Soovitan tungivalt luua sellest *Descriptorist* mitu koopiat ja hoida neid iga Multisig allkirjastava seadme juures. Näiteks minu puhul trükin *Descriptor* paberile ja hoian ühte koopiat Coldcardiga, teist Trezoriga ja ühte Ledger-ga. Samuti salvestan selle *Descriptor* PDF-failina kolmele USB-pulgale, mida hoitakse koos ühe riistvara portfelliga. Sel viisil maksimeerin oma võimalusi, et *Descriptor* ei lähe kunagi kaduma, ja olen kindel, et mul on iga seadmega kaks koopiat (üks füüsiline ja üks digitaalne).



Kui teie Multisig portfell on loodud, annab Sparrow teile automaatselt selle *Descriptor*. Vajutage nupule "*Save PDF...*", et salvestada see nii tekstina kui ka QR-koodina.



![Image](assets/fr/22.webp)



Seejärel saate selle PDF-faili välja printida ja kopeerida USB-pulgale.



![Image](assets/fr/23.webp)



Me registreerime selle *Descriptori* ka Coldcardis (kui te kasutate seda oma konfiguratsioonis). See võimaldab Coldcardil kontrollida, et iga hiljem allkirjastatud tehing vastab algsele Wallet-le: õiged xpubid, õige Address formaat, õige tuletamise tee... Ilma selle imporditud *Descriptorita* ei saa Coldcard kinnitada, et Exchange aadresse ei ole kaaperdatud või et PSBT ei ole võltsitud.



Just see teeb Coldcard Multisig puhul nii huvitavaks: see pakub lisakontrolli teatud keeruliste rünnakute vastu, mida teised riistvaralised rahakotid ei võimalda (eeldusel muidugi, et kasutate seda allkirjastamiseks).



Sparrow's avage menüü "*Settings*", seejärel klõpsake "*Export...*".



![Image](assets/fr/24.webp)



Valiku "*Coldcard Multisig*" kõrval klõpsake "*Export File...*" ja salvestage tekstifail Micro SD-kaardile.



![Image](assets/fr/25.webp)



Seejärel sisestage kaart Coldcardisse. Minge menüüsse "*Settings*", seejärel "*Multisig Wallets*" ja valige "*Import from SD*".



![Image](assets/fr/26.webp)



Valige sobiv fail ja kinnitage import.



![Image](assets/fr/27.webp)



Klõpsake oma äsja imporditud Multisig nimel.



![Image](assets/fr/28.webp)



Kontrollige Multisig konfiguratsiooniparameetrid, seejärel kinnitage registreerimine.



![Image](assets/fr/29.webp)



Teie Multisig on nüüd õigesti salvestatud teie Coldcardile. Kui teil on mitu Coldcard'i samas Multisig-s, korrake seda protseduuri igaühele.



Lisaks *Descriptor* salvestamisele ärge unustage erilist tähelepanu pöörata Mnemonic fraaside salvestamisele iga teie allkirja seadme jaoks. Kui te alles alustate, siis soovitan tungivalt tutvuda selle teise õpetusega, et õppida, kuidas neid õigesti salvestada ja hallata:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Enne esimeste bitcoinide saamist oma Multisig-ga, **tunnen tungivalt, et teete tühja taastamistesti**. Pange kirja mõned võrdlusandmed, näiteks esimene vastuvõttev Address, seejärel lähtestage oma riistvara rahakotid, kui Wallet on veel tühi. Seejärel proovige taastada oma Multisig Wallet riistvara rahakottidel, kasutades oma Mnemonic fraasipaberi varukoopiaid, seejärel Sparrow's, kasutades *Descriptor*. Kontrollige, et esimene pärast taastamist genereeritud Address vastab sellele, mille te algselt üles kirjutasite. Kui see vastab, võite olla kindel, et teie paberil tehtud varukoopiad on usaldusväärsed.



Kui soovite rohkem teada saada, kuidas teha taastamistesti, soovitan teil tutvuda selle teise õpetusega:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Saate bitcoin'e oma Multisig-ga



Teie Wallet on nüüd valmis bitcoinide vastuvõtmiseks. Klõpsake Sparrow's vahekaardil "*Vastuvõtmine*".



![Image](assets/fr/30.webp)



Enne Sparrow Wallet poolt genereeritud Address kasutamist võtke aega, et kontrollida seda otse oma riistvaralise rahakoti ekraanil. See tagab, et Address ei ole muudetud ja et teie seadmetes on olemas seotud raha kulutamiseks vajalikud privaatvõtmed. See aitab kaitsta teid mitmete ründevektorite eest.



Selleks klõpsake "*Display Address*", et kuvada Address oma Trezoril või Ledger-l, kui see on ühendatud kaabliga.



![Image](assets/fr/31.webp)



Coldcardiga saab seda kontrolli teostada ilma Sparrow'ga suhtlemata. Avage lihtsalt menüü "*Address Explorer*", seejärel valige oma Multisig kõige allosas.



![Image](assets/fr/32.webp)



Seejärel näete Multisig poolt genereeritud vastuvõtuaadresse.



![Image](assets/fr/33.webp)



Kontrollige, et Address, mis kuvatakse igal Hardware Wallet-l, vastab täpselt sellele, mis on Sparrow Wallet-l. Soovitav on seda teha vahetult enne Address jagamist maksjaga, et olla kindel selle terviklikkuses.



Seejärel saate määrata sellele Address-le "*Label*", et näidata saadud bitcoinide päritolu. See on hea viis oma UTXOde haldamise korraldamiseks.



![Image](assets/fr/34.webp)



Kui see on kontrollitud, saate bitcoinide saamiseks kasutada Address.



![Image](assets/fr/35.webp)



## Bitcoinide saatmine oma Multisig-ga



Nüüd, kui olete saanud oma esimese Satsi oma Multisig Wallet kohta, võite neid ka kulutada! Sparrow's minge vahekaardile "*Send*", et luua uus tehing.



![Image](assets/fr/36.webp)



Kui soovite kasutada *Müntide kontrolli*, st valida käsitsi UTXO-d, mida soovite kulutada, minge vahekaardile "*UTXO-d*". Valige UTXOd, mida soovite kulutada, ja klõpsake seejärel nupule "*Send Selected*". Teid suunatakse automaatselt vahekaardile "*Send*", kus UTXO-d on juba eeltäidetud.



![Image](assets/fr/37.webp)



Sisestage sihtkoht Address. Mitut aadressi saab lisada, klõpsates "*+ Add*".



![Image](assets/fr/38.webp)



Lisage "*Etikett*", et kirjeldada selle kulu eesmärki, mis hõlbustab tehingute jälgimist.



![Image](assets/fr/39.webp)



Sisestage valitud Address-le saadetav summa.



![Image](assets/fr/40.webp)



Reguleerige laadimiskiirust vastavalt praegustele võrgutingimustele. Sobiva laadimistaseme valimiseks vaadake näiteks [Mempool.space] (https://Mempool.space/).



Pärast kõigi tehingu parameetrite kontrollimist klõpsake nuppu "*Loo tehing*".



![Image](assets/fr/41.webp)



Kui olete kõigega rahul, klõpsake nupule "*Tehingu allkirjastamiseks lõpuleviimine*".



![Image](assets/fr/42.webp)



Ekraani allosas näete, et Sparrow ootab 2 allkirja. See on normaalne: siin kasutatav Wallet on Multisig 2-de-3.



![Image](assets/fr/43.webp)



Alustan allkirjastamist oma Coldcardiga. Selleks sisestan Micro SD-kaardi arvutisse, seejärel klõpsan "*Save Transaction*".



![Image](assets/fr/44.webp)



Allkirjastatava tehingu edastamiseks Hardware Wallet-le ja seejärel selle kättesaamiseks Sparrow'st on 3 võimalust. Esimene on kasutada Micro SD-kaarti, nagu me siinkohal teeme Coldcard'i puhul. Teine võimalus on kasutada kaabliühendust, mida me kasutame teise allkirja puhul (Ledger ja Trezor). Lõpuks on võimalik kasutada QR-koodiga sidet, mis on mõeldud kaameraga varustatud seadmete jaoks, nagu Coldcard Q, Jade Plus või Passport V2.



Kui PSBT (*Partially Signed Bitcoin Transaction*) on salvestatud Micro SD-le, sisestan selle Coldcard MK3-sse, seejärel valin menüüst "*Ready to Sign*".



![Image](assets/fr/45.webp)



Kontrollige hoolikalt oma Hardware Wallet ekraanil tehingu parameetreid: saaja Address, saadetud summa ja tasud. Kui tehing on kinnitatud, kinnitage allkirjastamiseks.



![Image](assets/fr/46.webp)



Seejärel tagastage Micro SD mälupulk arvutisse ja klõpsake Sparrow's nupule "*Load Transaction*". Valige oma failidest Coldcardi poolt allkirjastatud PSBT.



![Image](assets/fr/47.webp)



Näete, et Coldcard'i allkiri on lisatud. Kasutan nüüd teist seadet, antud juhul Ledger, et täita teine nõutav allkiri. Ühendan selle, vabastan selle, seejärel klõpsan Sparrow'l "*Sign*".



![Image](assets/fr/48.webp)



Klõpsake Hardware Wallet nime kõrval nupule "*Sign*".



![Image](assets/fr/49.webp)



Kui kasutate oma Ledger esimest korda koos selle Multisig-ga, palub Sparrow teil kontrollida kaasallkirjastajate laiendatud avalikke võtmeid (xpubs). Nagu ka Coldcardiga, takistab see samm hilisemat pimedat allkirjastamist. Selle teabe kinnitamiseks võrrelge Ledger ekraanil kuvatud xpubi nende xpubidega, mis on esitatud otse teie teiste riistvaraliste rahakottide poolt.



![Image](assets/fr/50.webp)



Kontrollige saaja Address, ülekantavat summat ja tehingutasu ning allkirjastage seejärel tehing.



![Image](assets/fr/51.webp)



Vajutage allkirja andmiseks ekraanile.



![Image](assets/fr/52.webp)



Sparrow'l on nüüd kaks allkirja, mis on vajalikud vahendite vabastamiseks Multisig portfellist. Kontrollige tehingut veel viimast korda ja kui kõik on korras, klõpsake "*Broadcast Transaction*", et tehing üle võrgu edastada.



![Image](assets/fr/53.webp)



Selle tehingu leiate Sparrow Wallet vahekaardilt "*Tehingud*".



![Image](assets/fr/54.webp)



Palju õnne, te teate nüüd, kuidas seadistada ja kasutada mitme allkirjaga Wallet-i Sparrow's. Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite allpool Green pöidla. Palun jagage seda artiklit julgelt oma suhtlusvõrgustikes. Täname jagamise eest!



Kui soovite edasi minna, siis soovitan teil tutvuda selle õpetusega, mis käsitleb teist meetodit Bitcoin Wallet turvalisuse suurendamiseks, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7