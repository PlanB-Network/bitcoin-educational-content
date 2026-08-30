---
name: Sparrow Wallet - Multisig
description: Looge Sparrow's mitme allkirjaga rahakott
---
![cover](assets/cover.webp)


Mitme allkirjaga rahakott (sageli nimetatud "*Multisig*") on Bitcoini rahakoti struktuur, mis nõuab kulutamise autoriseerimiseks mitut krüptograafilist allkirja erinevatelt võtmetelt. Erinevalt tavalisest ("*singlesig*") rahakotist, kus UTXO avamiseks piisab ühest privaatvõtmest, põhineb Multisig **m/n** mudelil: rahakotiga seotud _n_ võtmest peab _m_ iga tehingut tingimata kaasallkirjastama.


See mehhanism võimaldab rahakoti kontrolli jagada mitme üksuse või seadme vahel. Näiteks 2/3 konfiguratsioonis genereeritakse kolm sõltumatut võtmekomplekti, kuid vahendite vabastamiseks on vaja ainult kahte. Selline arhitektuur vähendab drastiliselt võtme kompromiteerimise või kaotamisega seotud riske: varas, kellel on juurdepääs ainult ühele võtmele, ei saa rahakotti tühjendada, ja kasutaja, kes ühe kaotab, pääseb ülejäänud kahega ikkagi oma vahenditele ligi.


![Image](assets/fr/01.webp)


Suurem turvalisus toob siiski kaasa suurema keerukuse. Multisig-rahakoti seadistamine nõuab mitme mnemoonilise fraasi (üks iga allkirjateguri kohta) ja laiendatud avalike võtmete ("*xpub*") turvamist. Kui kasutate Multisig 2/3 rahakotti, peavad rahakoti taastamiseks olema kas kõik kolm mnemoonilist fraasi või vähemalt kaks fraasi kolmest. Kui teil on aga ainult kaks fraasi kolmest, vajate ka juurdepääsu kolmele *xpub*-ile, ilma milleta on võimatu taastada avalikke võtmeid, mida on vaja nende kaitstavatele bitcoinidele juurdepääsuks.


Kokkuvõttes peate Multisig-rahakoti taastamiseks :


- Kas pääsema ligi kõikidele mnemoonilistele fraasidele, mis on seotud iga allkirjateguriga;
- Või omama allkirjastamiseks lävendi poolt nõutavat minimaalset arvu mnemoonilisi fraase ning lisaks juurdepääsu kõikide tegurite xpub-idele, et taastada vajalikud avalikud võtmed.


![Image](assets/fr/02.webp)


Multisig-rahakoti varukoopiate haldamist hõlbustavad *Output Script Descriptors*, mis koondavad kokku kõik vahenditele juurdepääsuks vajalikud avalikud andmed. Seda funktsiooni ei ole siiski veel rakendatud kõikides rahakotihaldustarkvarades.


Multisig sobib eriti hästi bitcoineridele, kes otsivad tugevdatud turvalisust või vahendite kollektiivset haldamist: ettevõtted, ühendused, pered või üksikkasutajad, kes hoiavad märkimisväärset kogust bitcoine. Sellega saab luua detsentraliseeritud haldusskeeme, näiteks jagada allkirjastamisõigust mitme juhi või meeskonnaliikme vahel.


Selles õpetuses õpime, kuidas luua ja kasutada klassikalist mitme allkirjaga rahakotti **Sparrow Walletiga**. Kui soovite luua kohandatud mitme allkirjaga rahakotti ajalukkudega (*timelock*), soovitan selle asemel kasutada Lianat:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Eeltingimused


Selles õpetuses näitan teile, kuidas teha Multisig [Sparrow Walleti rahakotihaldustarkvaraga](https://sparrowwallet.com/download/). Kui te ei ole seda tarkvara veel paigaldanud, tehke seda kohe. Kui vajate abi, on meil olemas ka üksikasjalik õpetus Sparrow Walleti seadistamise kohta :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Mitme allkirjaga rahakoti seadistamiseks vajate erinevaid riistvaralisi rahakotte. Näiteks Multisig 2/3 puhul võiksite kasutada :


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Image](assets/fr/03.webp)


Multisig-konfiguratsioonis on hea mõte kasutada erinevate tootjate riistvaralisi rahakotte. Nii tagate, et kui mõnel konkreetsel mudelil tekib tõsine probleem, ei mõjuta see teie Multisigi üldist turvalisust. Lisaks võimaldab see kasutada iga seadme eripäraseid eeliseid. Näiteks minu konfiguratsioonis :



- Trezor Model One on täielikult avatud lähtekoodiga, mis võimaldab kontrollida seedi genereerimist. Kuna sellel ei ole Secure Elementi, jääb see aga füüsiliste rünnakute suhtes haavatavaks;



- Ledger Flexil seevastu on kontrollimatu suletud lähtekoodiga püsivara, kuid see sisaldab Secure Elementi, mis pakub suurepärast füüsilist kaitset;



- Passport Core ühendab täielikult avatud lähtekoodiga püsivara, Secure Elementi ja *air-gapped* QR-koodivahetuse. See on sõltumatu kolmas allkirjastaja, mis suudab kontrollida aadresse ja allkirjastada PSBT-sid ilma USB-andmesidet kasutamata.


Enne Multisig-rahakoti seadistamist veenduge, et iga riistvaraline rahakott on õigesti seadistatud (mnemoonilise fraasi genereerimine ja salvestamine, PIN-koodi määramine). Üksikasjalike juhiste saamiseks võite tutvuda meie õpetustega iga riistvaralise rahakoti kohta, näiteks :


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Nagu näeme selles õpetuses hiljem, on Multisig-konfiguratsiooni võimalik lisada ka tegur, mis ei ole seotud riistvaralise rahakotiga, vaid mille privaatvõtmed on salvestatud teie arvutisse. See meetod on ilmselgelt vähem turvaline kui ainult riistvaraliste rahakottide kasutamine, kuid teatud juhtudel võib see olla asjakohane. Näiteks Multisig 2/3 puhul võiksite valida kaks riistvaralist rahakotti ja ühe tarkvaralise rahakoti.

> ⚠️ **Coldcard MK3 turvateade:** ärge looge uut seedi MK3-l, mille püsivara on vanem kui 4.2.0. Varasema püsivaraga genereeritud seedid tuleb asendada ja vahendid mujale viia. Seepärast kasutab see õpetus *air-gapped* võrdlusallkirjastajana Passport Core'i.


## Multisig-rahakoti loomine


Avage Sparrow Wallet, klõpsake vahekaardil "*File*" ja valige seejärel "*New Wallet*".


![Image](assets/fr/04.webp)


Andke oma mitme allkirjaga rahakotile nimi ja klõpsake kinnitamiseks "*Create Wallet*".


![Image](assets/fr/05.webp)


Valige rippmenüüst "*Policy Type*" valik "*Multi Signature*".


![Image](assets/fr/06.webp)


Paremas ülanurgas saate nüüd määrata oma Multisigi võtmete koguarvu ning kaasallkirjastajate arvu, mida on vaja kulutamise autoriseerimiseks. Minu näites on tegemist 2/3 skeemiga.


![Image](assets/fr/07.webp)


Akna allosas kuvab Sparrow Wallet kolm "*Keystore*"-i. Igaüks neist esindab ühte võtmekomplekti. Siin kasutan kolme riistvaralist rahakotti, seega vastab iga "*Keystore*" ühele neist. Nüüd seadistame need.


Alustan Passport Core'ist. Vahekaardil "*Keystore 1*" valin valiku "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Avage Passportis konto, mida soovite kasutada, ja valige seejärel "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport kuvab animeeritud QR-koodi, mis sisaldab tema avaliku võtme teavet.

Valige Sparrow's "*Passport*" kõrval "*Scan...*" ja skannige see animeeritud QR-kood oma arvuti veebikaameraga. Võrrelge Sparrow's kuvatavat peavõtme sõrmejälge Passportis kuvatavaga ja importige seejärel keystore.

Teie Passporti xpub on nüüd imporditud. Korrake Ledger Flexi ja Trezor Model One'i puhul vastavat protseduuri.


Ledger Flexi jaoks valin "*Keystore 2*" ja klõpsan seejärel "*Connected Hardware Wallet*". Veenduge, et Ledger on arvutiga ühendatud, lukust lahti ja et Bitcoini rakendus on avatud.


![Image](assets/fr/15.webp)


Seejärel klõpsake nuppu "*Scan...*".


![Image](assets/fr/16.webp)


Klõpsake oma riistvaralise rahakoti nime kõrval "*Import Keystore*".


![Image](assets/fr/17.webp)


Teine allkirjastaja on nüüd Sparrow Walletis õigesti registreeritud.


![Image](assets/fr/18.webp)


Kordan täpselt sama protseduuri Trezor One'iga, et Multisigi konfiguratsioon lõpule viia.


![Image](assets/fr/19.webp)


Minu konfiguratsioonis me seda juhtumit ei käsitle, kuid kui soovite lisada oma Multisigi allkirja Sparrow's oleva tarkvaralise rahakoti kaudu (kuum rahakott), klõpsake lihtsalt nuppu "*New or Imported Software Wallet*".


Nüüd, kui kõik teie allkirjastamisseadmed on Sparrow Walletisse imporditud, saate Multisigi loomise lõpule viia, klõpsates "*Apply*".


![Image](assets/fr/20.webp)


Valige tugev parool, et kaitsta juurdepääsu oma Sparrow Walleti rahakotile. See parool kaitseb teie avalikke võtmeid, aadresse, silte ja tehinguajalugu volitamata juurdepääsu eest.


Ärge unustage seda parooli turvalises kohas, näiteks paroolihalduris, salvestada, et te seda ei kaotaks.


![Image](assets/fr/21.webp)


## Multisig-rahakoti varundamine


Nüüd salvestame *Output Script Descriptori* sõltumatule andmekandjale ja hoiame sellest mitut koopiat.


*Deskriptor* sisaldab kõiki teie Multisig-rahakoti xpub-e ning võtmete genereerimiseks kasutatud tuletusradasid. Pidage meeles, mida nägime 1. osas: Multisig-rahakoti taastamiseks peavad teil olema kas **kõik** mnemoonilised fraasid või ainult minimaalne arv, mida on vaja allkirjastamise lävendi saavutamiseks. Viimasel juhul on aga hädavajalik omada ka puuduvate allkirjastajate **xpub-e**. *Deskriptor* sisaldab kõiki teie Multisigi xpub-e.


Kui see ei ole selge, pidage meeles lihtsalt seda: Multisigi taastamiseks vajate sõltuvalt lävendist minimaalset arvu mnemoonilisi fraase iga kasutatud riistvaralise rahakoti kohta (minu puhul: 2 fraasi) ning lisaks *deskriptorit*.


See *deskriptor* ei sisalda privaatvõtmeid, ainult avalikke. See tähendab, et see ei anna juurdepääsu vahenditele. Seega ei ole see nii kriitiline kui mnemoonilised fraasid, mis annavad teie bitcoinidele täieliku juurdepääsu. *Deskriptoriga* seotud risk puudutab ainult konfidentsiaalsust: kompromiteerimise korral võiks kolmas osapool jälgida kõiki teie tehinguid, kuid ei saaks teie vahendeid kulutada.


Soovitan tungivalt teha sellest *deskriptorist* mitu koopiat ja hoida neid koos iga oma Multisigi allkirjastamisseadmega. Näiteks minu puhul prindin *deskriptori* paberile ja hoian ühte koopiat koos Passportiga, teist koos Trezoriga ja kolmandat koos Ledgeriga. Salvestan selle *deskriptori* ka PDF-failina kolmele USB-mälupulgale, millest igaüht hoitakse koos ühe riistvaralise rahakotiga. Nii maksimeerin oma võimalusi seda *deskriptorit* kunagi mitte kaotada ja olen kindel, et mul on iga seadme juures kaks koopiat (üks füüsiline ja üks digitaalne).


Kui teie Multisig-rahakott on loodud, annab Sparrow selle *deskriptori* teile automaatselt. Klõpsake nuppu "*Save PDF...*", et salvestada see nii tekstina kui ka QR-koodina.


![Image](assets/fr/22.webp)


Seejärel saate selle PDF-i välja printida ja kopeerida oma USB-mälupulkadele.


![Image](assets/fr/23.webp)


Passport kasutab Sparrow poolt imporditud multisig-konfiguratsiooni, et QR-koodiga sidumise ja allkirjastamise käigus kuvada ja kontrollida asjakohast võtmeteavet. Hoidke *deskriptorit* eraldi: see jääb hädavajalikuks rahakoti taastamiseks, kui üks allkirjastaja ei ole kättesaadav.


Lisaks *deskriptori* salvestamisele ärge unustage pöörata erilist tähelepanu iga allkirjastamisseadme mnemooniliste fraaside salvestamisele. Kui te alles alustate, soovitan tungivalt tutvuda selle teise õpetusega, et õppida neid õigesti salvestama ja haldama:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Enne esimeste bitcoinide vastuvõtmist oma Multisigile **soovitan tungivalt teha tühja rahakotiga taastamistesti**. Märkige üles mõned võrdlusandmed, näiteks esimene vastuvõtuaadress, ja lähtestage seejärel oma riistvaralised rahakotid, kuni rahakott on veel tühi. Seejärel proovige taastada oma Multisig-rahakott riistvaralistel rahakottidel, kasutades mnemooniliste fraaside paberkoopiaid, ja pärast seda Sparrow's, kasutades *deskriptorit*. Kontrollige, et pärast taastamist genereeritud esimene aadress vastab sellele, mille algselt üles kirjutasite. Kui see nii on, võite olla kindel, et teie paberkoopiad on usaldusväärsed.


Et rohkem teada saada, kuidas taastamistesti teha, soovitan tutvuda selle teise õpetusega:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoinide vastuvõtmine oma Multisigile


Teie rahakott on nüüd valmis bitcoine vastu võtma. Klõpsake Sparrow's vahekaardil "*Receive*".


![Image](assets/fr/30.webp)


Enne Sparrow Walleti genereeritud aadressi kasutamist võtke aega ja kontrollige seda otse oma riistvaraliste rahakottide ekraanil. Nii tagate, et aadressi ei ole muudetud ja et teie seadmetel on privaatvõtmed, mida on vaja seotud vahendite kulutamiseks. See aitab teid kaitsta mitmete rünnakuvektorite eest.


Selleks klõpsake "*Display Address*", et kuvada aadress oma Trezoril või Ledgeril, kui need on kaabliga ühendatud.


![Image](assets/fr/31.webp)


Passporti puhul valige multisig-konto ja seejärel "*Verify Address*". Skannige Sparrow's kuvatud vastuvõtuaadressi QR-kood. Passport kinnitab oma ekraanil, kas aadress kuulub multisig-rahakotile.


Kontrollige, et igal riistvaralisel rahakotil kuvatav aadress vastab täpselt Sparrow Walletis olevale. Soovitatav on seda teha vahetult enne aadressi jagamist maksjaga, et olla kindel selle terviklikkuses.


Seejärel saate sellele aadressile määrata "*Label*"-i, et märkida vastu võetud bitcoinide päritolu. See on hea viis oma UTXO-de haldamise korraldamiseks.


![Image](assets/fr/34.webp)


Kui see on kontrollitud, võite aadressi kasutada bitcoinide vastuvõtmiseks.


![Image](assets/fr/35.webp)


## Bitcoinide saatmine oma Multisigiga


Nüüd, kui olete oma Multisig-rahakotile esimesed satoshid vastu võtnud, saate neid ka kulutada! Uue tehingu koostamiseks minge Sparrow's vahekaardile "*Send*".


![Image](assets/fr/36.webp)


Kui soovite kasutada *Coin Controli*, st valida käsitsi UTXO-d, mida soovite kulutada, minge vahekaardile "*UTXOs*". Valige UTXO-d, mida soovite kulutada, ja klõpsake seejärel "*Send Selected*". Teid suunatakse automaatselt vahekaardile "*Send*", kus UTXO-d on juba eeltäidetud.


![Image](assets/fr/37.webp)


Sisestage sihtaadress. Mitu aadressi saab lisada, klõpsates "*+ Add*".


![Image](assets/fr/38.webp)


Lisage "*Label*", mis kirjeldab selle kulutuse eesmärki, et oma tehinguid oleks lihtsam jälgida.


![Image](assets/fr/39.webp)


Sisestage summa, mis tuleb valitud aadressile saata.


![Image](assets/fr/40.webp)


Kohandage tasumäära vastavalt praegustele võrgutingimustele. Sobiva tasutaseme valimiseks vaadake näiteks [Mempool.space](https://Mempool.space/).


Kui olete kõik tehingu parameetrid üle kontrollinud, klõpsake "*Create Transaction*".


![Image](assets/fr/41.webp)


Kui kõik on teie meelt mööda, klõpsake "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Ekraani allosas näete, et Sparrow ootab 2 allkirja. See on normaalne: siin kasutatav rahakott on Multisig 2/3.


![Image](assets/fr/43.webp)


Alustan allkirjastamist oma Passportiga. Klõpsake Sparrow's "*Show QR*", et kuvada PSBT (*Partially Signed Bitcoin Transaction*) animeeritud QR-koodidena. Valige Passportis multisig-konto ja seejärel "*Sign with QR Code*" ning skannige Sparrow's kuvatud QR-kood.


Kontrollige oma riistvaralise rahakoti ekraanil hoolikalt tehingu parameetreid: saaja aadressi, saadetavat summat ja tasusid. Kui tehing on üle vaadatud, kinnitage see, et allkirjastamisega edasi minna.


Pärast tehingu heakskiitmist kuvab Passport allkirjastatud PSBT animeeritud QR-koodidena. Klõpsake Sparrow's "*Scan QR*" ja skannige need koodid oma veebikaameraga. Seejärel lisatakse Passporti allkiri. Nüüd kasutan teise nõutava allkirja jaoks Ledgerit: ühendan selle ja avan luku ning klõpsan Sparrow's "*Sign*".


![Image](assets/fr/48.webp)


Klõpsake oma riistvaralise rahakoti nime kõrval "*Sign*".


![Image](assets/fr/49.webp)


Kui kasutate oma Ledgerit selle Multisigiga esimest korda, palub Sparrow teil kontrollida kaasallkirjastajate laiendatud avalikke võtmeid (xpub-e). Nagu Passporti puhul, hoiab see samm ära hilisema pimesi allkirjastamise. Selle teabe kinnitamiseks võrrelge Ledgeri ekraanil kuvatavat xpub-i nendega, mille annavad otse teie teised riistvaralised rahakotid.


![Image](assets/fr/50.webp)


Kontrollige saaja aadressi, ülekantavat summat ja tehingutasu ning allkirjastage seejärel tehing.


![Image](assets/fr/51.webp)


Allkirjastamiseks vajutage ekraanile.


![Image](assets/fr/52.webp)


Sparrow'l on nüüd kaks allkirja, mida on vaja vahendite vabastamiseks Multisig-rahakotist. Kontrollige tehingut viimast korda ja kui kõik on korras, klõpsake "*Broadcast Transaction*", et see võrku edastada.


![Image](assets/fr/53.webp)


Selle tehingu leiate Sparrow Walleti vahekaardilt "*Transactions*".


![Image](assets/fr/54.webp)


Palju õnne, nüüd te teate, kuidas Sparrow's mitme allkirjaga rahakotti seadistada ja kasutada. Kui see õpetus oli teile kasulik, oleksin tänulik, kui jätaksite allpool rohelise pöidla. Jagage seda artiklit julgelt oma sotsiaalvõrgustikes. Aitäh jagamise eest!


Et kaugemale minna, soovitan tutvuda selle õpetusega teise meetodi kohta oma Bitcoini rahakoti turvalisuse suurendamiseks – BIP39 paroolifraas :


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7