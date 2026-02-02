---
name: Ashigaru
description: Samourai fork Wallet, et kindlustada, hallata ja segada oma bitcoin'e
---

![cover](assets/cover.webp)



Ashigaru on Bitcoin mobiilne wallet rakendus, mis on jätkuks Samourai Wallet projektile, kuid uuel kujul. See tarkvara sündis erilises kontekstis: 2024. aasta aprillis arreteerisid Ameerika ametivõimud Samourai Wallet asutajad ja nende serverid konfiskeeriti. Kuigi Samurai rakendus ise jäi kasutatavaks, ei hooldata seda praegu enam. Ashigaru on Samurai Wallet tasuta fork versioon, mida hooldab anonüümne meeskond, et tagada Samurai funktsionaalsuse järjepidevus ja kaitsta selle algset filosoofiat: kaitsta Bitcoin kasutajate privaatsust ja suveräänsust.



Ashigaru võtab paljuski üle Samourai DNA: sarnane kasutajaliides, ilmselgelt isemajandav lähenemine, avatud lähtekood ja keskendumine privaatsusele. Koodi levitatakse GNU GPLv3 litsentsi alusel, mis tagab, et igaüks võib tarkvara kontrollida, muuta või levitada.



Ashigaru rakendus integreerib hulga täiustatud vahendeid teie UTXOde konfidentsiaalsuse ja haldamise jaoks:




- Whirlpool**, Zerolinkil põhinev coinjoin-protokoll, mis võimaldab teil katkestada deterministlikud seosed tehingu sisenemiste ja väljumiste vahel, kaotamata seejuures suveräänsust oma vahendite üle.
- PayNym**, mis rakendab korduvkasutatavaid maksekoode (BIP47), mis on nüüd esindatud "*Pepehash*" avatar-süsteemi kaudu.
- Ricochet**, funktsioon, mis lisab tehingutele vahepealseid hüppeid, et neid oleks raskem jälgida.
- Ja muidugi ***Coin Control***, et valida, külmutada ja märgistada oma UTXO-d täpselt.
- Partiiväljastamine***, et vähendada kulusid, koondades mitu makset üheks tehinguks.
- **Stealth Mode**, mis peidab rakenduse teie mobiiltelefonis mannekeeni käivitaja taha, et telefoni füüsilisel kontrollimisel jääks see märkamatuks.
- Täiustatud kulutamisvahendid oma konfidentsiaalsuse optimeerimiseks (payjoin, stonewall...).
- Optimeeritud taastamissüsteem, mis kasutab Passphrase BIP39.
- Süsteem tehingutasude valiku automaatseks optimeerimiseks.



![Image](assets/fr/01.webp)



Ashigaru on seega suunatud kasutajatele, kes on teadlikud Bitcoin tehingu jälgitavusega seotud probleemidest. Olenemata sellest, kas olete eraelu puutumatust arvestav kasutaja, kogenud bitcoiner, kes on pühendunud enesekontrollile, või üksikisik, kes puutub kokku suurenenud jälgimise riskidega, annab see wallet rakendus teile vahendid, mida vajate, et taastada kontroll oma tegevuse üle Bitcoin-s.



Ashigaru on saadaval mobiiliversioonina rakenduse kaudu, mida uurime selles õpetuses. Kuid seda saab kasutada ka arvutis ***Ashigaru Terminal*** abil, mida tutvustame tulevases õpetuses.



![Image](assets/fr/02.webp)



Selles õpetuses tutvustan teile Ashigaru põhilist kasutamist: paigaldamine, ühendamine Dojoga, varundamine, bitcoinide vastuvõtmine ja saatmine. Täiustatud vahendeid tutvustatakse teistes spetsiaalsetes õpetustes.



## 1. Ashigaru eeldused



Rakendus vajab korralikuks toimimiseks mõningaid eeldusi. Esiteks ei ole see rakendus saadaval klassikalistes poodides, nagu Google Play Store või App Store. See installeeritakse telefoni käsitsi ainult selle `.apk` failist, mida saab alla laadida Tor-võrgu kaudu. Nii et kui kasutate iPhone'i, siis see meetod ei tööta: teil on vaja Android-seadet.



Tori kaudu apk-faili allalaadimiseks on vaja brauserit, mis võimaldab juurdepääsu .onion-saitidele. Kõige lihtsam viis on paigaldada oma telefoni rakendus Tor Browser, mis on saadaval [Google Play poest](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) või otse [selle `.apk` kaudu](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Enamik uuemaid nutitelefone blokeerib vaikimisi tundmatutest allikatest pärinevate rakenduste paigaldamise. Sa pead selle valiku ajutiselt aktiveerima oma seadme seadetes Tor Browser'i jaoks, et lubada installimist. Kui rakendus on paigaldatud, ärge unustage selle funktsiooni deaktiveerida, et tugevdada telefoni turvalisust.



Teine oluline eeldus Ashigaru kasutamiseks on Bitcoin Dojo sõlme olemasolu. Turvalisuse ja suveräänsuse huvides ei halda Ashigaru meeskond teie rakenduse ühendamiseks keskset serverit. Seega peate käivitama omaenda Dojo instantsi või ühendama selle usaldusväärse instantsiga.



Dojo võimaldab teie Ashigaru rakendusel konsulteerida plokiahela teabega, vaadata oma aadresside saldosid ja edastada oma tehinguid Bitcoin võrgus.



Et rohkem teada saada Dojo kohta ja õppida, kuidas seda paigaldada, kutsun teid üles jälgima seda spetsiaalset õpetust :



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Kui te tõesti ei saa endale lubada oma Dojo't, võite leida inimesi, kes on valmis oma instantsi tasuta jagama aadressil [dojobay.pw](https://www.dojobay.pw/mainnet/). See võib olla ajutine lahendus, kuid pikemas perspektiivis soovitan kasutada oma Dojo-d, et tagada oma suveräänsus ja konfidentsiaalsus.



## 2. Kontrollida ja paigaldada Ashigaru rakendus



### 2.1. Lae alla Ashigaru rakendus



Avage oma telefonis Tor Browser ja minge [Ashigaru ametlikule veebisaidile](https://ashigaru.rs/download/), jaotis `Download`. Seejärel klõpsake paigaldusfaili allalaadimiseks nupule `Download for Android`.



![Image](assets/fr/04.webp)



Enne rakenduse paigaldamist teie seadmesse kontrollime selle autentsust ja terviklikkust. See on väga oluline samm, eriti kui paigaldate rakenduse otse `.apk' failist.



### 2.2. Kontrolli Ashigaru taotlust



Mine tagasi [Ashigaru ametlikule veebisaidile](https://ashigaru.rs/download/) jaotisesse `Download`, seejärel kopeeri pealkirja `SHA-256 Hash APK-faili` all kuvatav sõnum. Kopeerige kogu plokk alates `BEGIN PGP SIGNED MESSAGE` kuni `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Avage endiselt telefonis uus vahekaart Tor Browseris ja minge [Keybase'i verifitseerimisvahendisse](https://keybase.io/verify). Sisestage äsja kopeeritud sõnum etteantud väljale ja vajutage seejärel nupule `Verify`.



![Image](assets/fr/06.webp)



Kui allkiri on ehtne, kuvab Keybase teate, mis kinnitab, et fail on allkirjastatud Ashigaru arendajate poolt. Samuti võite klõpsata Keybase'i poolt näidatud `ashigarudev` profiilil ja kontrollida, et nende võtme sõrmejälg vastab täpselt : `A138 06B1 FA2A 676B`.



Kui aga selles etapis ilmneb viga, tähendab see, et allkiri on kehtetu. Sellisel juhul **ei tohi APK-d installida**. Alustage uuesti algusest või küsige enne jätkamist abi kogukonnalt.



![Image](assets/fr/07.webp)



Keybase on andnud teile rakenduse hashi. Nüüd kontrollime, et allalaetud `.apk` faili hash vastab Keybase'is kontrollitud failile. Selleks minge [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Klõpsake nupul `BROWSE...` ja valige sammus 2.1 alla laetud `.apk` fail.


Seejärel valige hash-funktsioon `SHA-256` ja klõpsake `CALCULATE HASH`, et arvutada teie faili hash.



![Image](assets/fr/09.webp)



Sait kuvab teie .apk-faili hashi. Võrrelge seda Keybase.io's kontrollitud hashiga. Kui kaks hashi on identsed, on autentsuse ja terviklikkuse kontroll olnud edukas. Nüüd võite jätkata rakenduse installimist.



![Image](assets/fr/10.webp)



### 2.3. installige Ashigaru rakendus



Rakenduse installimiseks avage oma telefoni failihaldur ja minge allalaadimiste kausta. Seejärel klõpsake äsja kontrollitud .apk-failil ja kinnitage paigaldamine, kui seda küsitakse.



![Image](assets/fr/11.webp)



Ashigaru on nüüd teie telefoni paigaldatud.



## 3. Rakenduse initsialiseerimine ja Bitcoin portfelli loomine



Rakenduse esmakordsel käivitamisel valige `MAINNET`.



![Image](assets/fr/12.webp)



Seejärel klõpsake nupule "Alusta".



![Image](assets/fr/13.webp)



Nüüd loome uue Bitcoin portfelli. Vajutage nuppu "Loo uus wallet".



![Image](assets/fr/14.webp)



### 3.1. luua Bitcoin portfell



Ashigaru vajab passphrase BIP39. Valige oma passphrase ja sisestage see vastavatesse väljadesse. See peab olema võimalikult pikk ja juhuslik, et vastu seista brute-force rünnakule.



Tehke sellest passphrase-st kohe füüsiline varukoopia. See on väga oluline samm: kui te kaotate oma telefoni, **kui teil ei ole enam seda passphrase, ei saa te enam juurdepääsu oma Ashigaru wallet-s salvestatud bitcoinidele**. Sama passphrase kasutatakse ka wallet taastamisfaili krüpteerimiseks.



Kui te ei tea, mis on passphrase või ei mõista täielikult, kuidas see töötab, siis soovitan teil tungivalt lugeda seda täiendavat õpetust. See on oluline, sest passphrase on teie turvalisuse kriitiline element: selle kasutamise vääritimõistmine võib põhjustada teie rahaliste vahendite lõpliku kaotuse.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kui olete sisestanud oma passphrase, klõpsake nuppu "NEXT".



![Image](assets/fr/15.webp)



Seejärel valige PIN-kood. Seda koodi kasutatakse teie Ashigaru wallet lukustuse avamiseks, kaitstes seda volitamata füüsilise juurdepääsu eest. See ei ole seotud teie wallet võtmete krüptograafilise tuletamisega. See tähendab, et isegi PIN-koodi teadmata saab igaüks, kellel on teie mnemooniline fraas ja passphrase, taastada juurdepääsu teie bitcoinidele.



Valige pikk, juhuslik PIN-kood. Ärge unustage hoida varukoopiat telefonist eraldi, et vältida nende samaaegset kahjustamist.



![Image](assets/fr/16.webp)



Kui PIN-kood on loodud, kuvab Ashigaru teie wallet mälulause. Hoiatus: see fraas annab koos teie passphrase-ga täieliku juurdepääsu teie bitcoinidele. Igaüks, kes seda hoiab, võib teie raha enda valdusesse võtta, isegi kui tal puudub juurdepääs teie telefonile. Seda 12-sõnalist jada saab kasutada oma wallet taastamiseks telefoni kadumise, varguse või purunemise korral. Seetõttu on oluline salvestada see võimalikult hoolikalt füüsilisel andmekandjal (paber või metall).



Ärge kunagi salvestage seda lauset digitaalsel kujul, sest muidu riskite oma raha varguse ohtu seadmisega. Sõltuvalt teie turvastrateegiast võite luua mitu füüsilist koopiat, kuid ärge kunagi jagage seda. Hoidke sõnad täpselt oma järjekorras ja veenduge, et need on nummerdatud.



Lõpuks, ärge kunagi hoidke mnemoonikat ja passphrase samas kohas. Kui mõlemad on korraga ohustatud, võib ründaja saada juurdepääsu teie wallet-le.



![Image](assets/fr/17.webp)



Kui soovite rohkem teada saada, kuidas kindlustada oma mnemofraasi, vaadake seda täiendavat õpetust :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Seejärel palub Ashigaru teil oma passphrase uuesti kinnitada. Kasutage seda võimalust, et kontrollida, kas teie füüsiline varukoopia on õige.



![Image](assets/fr/18.webp)



### 3.2. ühendage dojo



Järgmisena tuleb samm, mis ühendab teie Dojoga. Nagu sissejuhatuses selgitatud, peab Ashigaru olema ühendatud Dojoga, et suhelda Bitcoin võrguga.



Logige sisse oma Dojo "Hooldusvahendisse" ja avage menüü "KASUTAMINE".



![Image](assets/fr/19.webp)



Vajutage Ashigarul nuppu `Scan QR` ja skannige seejärel DMT poolt kuvatavat ühenduse QR-koodi. Seejärel vajutage kinnitamiseks nuppu `Continue`.



![Image](assets/fr/20.webp)



wallet avamiseks sisestage PIN-kood. See viib teid sünkroonimislehele. On tavaline, et selles etapis ilmnevad *PayNym* vead, kuna wallet on uus. Lihtsalt klõpsake nuppu `Continue` (Jätka).



![Image](assets/fr/21.webp)



Seejärel jõuate oma portfelli avalehele.



![Image](assets/fr/22.webp)



Enne edasist tegutsemist soovitan teil teha proovi taastamine, kui wallet ei sisalda veel bitcoine. See võimaldab teil kontrollida, et teie paberil tehtud varukoopiad töötavad korralikult. Kuidas seda teha, saate teada sellest juhendmaterjalist:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Ashigaru rakenduse seadistamine



Rakenduse seadetele juurdepääsemiseks klõpsake oma *PayNym* pildil vasakus ülanurgas, seejärel valige "Seaded".



![Image](assets/fr/23.webp)



Siit leiate mitmeid võimalusi Ashigaru töö kohandamiseks teie vajadustele. Soovitan siiski tungivalt, et aktiveeriksite kohe alguses 2 olulist parameetrit.



Alustage menüüst `Turvalisus > Varjatud režiim`, seejärel aktiveerige see funktsioon, kui seda vajate. See peidab Ashigaru rakenduse telefoni paigaldatud tavalise rakenduse nime, logo ja kasutajaliidese taha. Selle eesmärk on takistada kellelgi Ashigaru tuvastamist teie telefoni füüsilise kontrollimisel.



![Image](assets/fr/24.webp)



Igal pakutaval võltsrakendusel on konkreetne meetod, kuidas avada tõeline Ashigaru kasutajaliides. Näiteks kui valite kalkulaatori, kaob Ashigaru rakendus teie avakuvalt ja asendatakse võltskalkulaatoriga. Kui avate selle, näete klassikalist töötavat kalkulaatori kasutajaliidest, kuid Ashigarule pääsemiseks peate vaid viis korda kiiresti koputama sümbolit `=`.



Teine oluline parameeter, mida tuleb aktiveerida, on [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). See valik võimaldab teil suurendada tehingu maksumust, kui see jääb mempool'isse kinni, sest selle maksumus on liiga madal. Selle saate aktiveerida menüüst `Transactions > Spend using RBF`.



![Image](assets/fr/25.webp)



Vihje: Saate muuta oma portfelli näitamise ühikut `BTC`lt `sat`le, klõpsates lihtsalt avalehel kuvataval kogusaldol.



## 5. Saada bitcoins kohta Ashigaru



Nüüd, kui teie portfell on töökorras, võite saada satss. Selleks vajutage kasutajaliidese paremas allosas asuvat nuppu "+" ja seejärel rohelist nuppu "Vastuvõtmine".



![Image](assets/fr/26.webp)



Ashigaru näitab teile seejärel esimest kasutamata vastuvõtuaadressi teie wallet-s, et vältida aadressi korduvkasutamist (aadressi korduvkasutamine on teie privaatsuse seisukohast väga halb tava). Seejärel saate selle aadressi edastada isikule või teenusele, kes peab teile bitcoine saatma.



![Image](assets/fr/27.webp)



Kui tehing on võrgus edastatud, ilmub see automaatselt rakenduse avalehele.



![Image](assets/fr/28.webp)



## 6. Saada bitcoine koos Ashigaru'ga



Nüüd, kui teil on bitcoinid Ashigaru wallet-s, saate neid ka saata. Selleks vajutage paremal allosas olevat nuppu "+" ja valige seejärel punane nupp "Saada".



![Image](assets/fr/29.webp)



Seejärel valige konto, millelt soovite kulutusi teha. Hetkel ei ole me veel käsitlenud kontot `Postmix`, mis on reserveeritud coinjoinide jaoks, mida me vaatame hilisemas õpetuses. Seega saadame raha põhihoiuse kontolt.



![Image](assets/fr/30.webp)



Sisestage oma tehingu andmed: saadetav summa ja saaja Bitcoin aadress.



![Image](assets/fr/31.webp)



Kui klõpsate kolmel väikesel punktil üleval paremas nurgas ja seejärel "Näita kasutamata väljundeid", saate ka täpselt valida, milliseid UTXOsid soovite kulutada, et suurendada oma privaatsust.



![Image](assets/fr/32.webp)



Kui olete kõik andmed sisestanud, klõpsake kasutajaliidese allosas olevale valgele noolele, et jätkata.



Seejärel avaneb kokkuvõtte lehekülg, kus on esitatud kõik tehingu üksikasjad. Kuvatakse mitu olulist elementi:




- Kontrollige veelkord plokis "Sihtkoht", et saaja aadress ja saadetud summa oleksid õiged;
- Plokis "Tasud" saate vaadata Ashigaru poolt automaatselt valitud tasumäärasid ja vajadusel neid muuta, klõpsates nupul "HALDAMINE" ;
- Blokk "Tehing" näitab tehingu tüüpi, mida te kavatsete teha. Siinkohal räägime lihtsast tehingust, kuid Ashigaru toetab ka muud tüüpi privaatsust optimeeritud tehinguid, mida käsitleme üksikasjalikult ühes tulevases õpetuses;
- Punane plokk "Tehingu hoiatus" hoiatab teid, kui teie tehing näitab mustreid, mida ahela analüüsi tööriistad suudavad tuvastada ja mis võivad teie privaatsust ohustada. Sellele klõpsates saate vaadata üksikasju. Näiteks minu puhul ütleb Ashigaru mulle, et saadetud summa on ümmargune (`3000 sats`), mis võimaldab mul järeldada, milline väljund vastab kulule ja milline vahetusele. Et rohkem teada saada nende ahelanalüüsi heuristikate kohta, kutsun teid üles jälgima minu BTC 204 koolitust Plan ₿ Academy ;
- Lõpuks saate lisada oma tehingule sildi, et hoida selle eesmärki.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kui olete kõik andmed kontrollinud, kasutage bitcoinide saatmiseks rohelist noolt. Hoidke nool all ja lohistage seda üleslaadimise kinnitamiseks paremale.



![Image](assets/fr/33.webp)



Teie tehing on edastatud Bitcoin võrgus.



![Image](assets/fr/34.webp)



## 7. Ashigaru wallet taastamine



Ashigaru wallet taastamine erineb pisut klassikalise Bitcoin wallet taastamisest, kuna selle puhul kasutatakse samu meetodeid, mis Samurai Wallet puhul. Kui te kaotate juurdepääsu oma wallet-le (kas PIN-koodi unustamisel, selle desinstalleerimisel või telefoni kaotamisel), on bitcoinide taastamiseks mitu võimalust.



Kui teil on endiselt juurdepääs telefonile või kui te olete teinud sellest failist varukoopia, on kõige lihtsam meetod kasutada varukoopiafaili `ashigaru.txt`. See fail sisaldab kogu teavet, mida vajate oma portfelli taastamiseks uuel Ashigaru instantsil (või Sparrow Wallet), kuid see on krüpteeritud passphrase-ga, mille määrasite selle õpetuse sammus 3.1. Seetõttu peab teil selle meetodi kasutamiseks olema nii fail `ashigaru.txt` kui ka teie passphrase.



Nende kahe elemendi abil saate näiteks taastada oma portfelli Sparrow Wallet.



![Image](assets/fr/35.webp)



Kui teil ei ole juurdepääsu failile `ashigaru.txt`, saate oma rahalistele vahenditele uuesti juurdepääsu, kasutades oma passphrase mnemoonilist fraasi, nagu te seda teeksite iga teise Bitcoin portfelli puhul. Soovitan seda taastamist teostada kas uues Ashigaru-instantsis või otse Sparrow Wallet-s, et hõlpsasti taastada Whirlpool möödapääsuteed, kui te seda kasutasite. Teise võimalusena saate selle teabe importida mis tahes teise BIP39-ga ühilduvasse tarkvarasse, sisestades tuletamise teed käsitsi.



Lisateavet selle protsessi kohta leiate täielikust juhendmaterjalist, mille olen kirjutanud Wallet Samurai wallet taastamise kohta. Kuna Ashigaru on fork, on protseduur identne:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Nagu näete, on passphrase hädavajalik, millist taastamismeetodit te ka ei kasutaks. Seega tagage see kindlasti hoolikalt. Samuti võite teha mitu koopiat, sõltuvalt teie turvastrateegiast.



## 8. Taotluse ajakohastamine



Et uuendada Ashigaru rakendust, kuna sa installeerisid selle `.apk` failist, mitte Play Store'i kaudu nagu tavalise rakenduse, pead sa alla laadima uue `.apk` faili, mis vastab uuendatud versioonile, ja seejärel paigaldama selle käsitsi.



Korrake käesoleva õpetuse punktis 2 kirjeldatud samme, kuid kui klõpsate installimise käivitamiseks .apk-failile, peaks **Android-telefon pakkuma teile võimalust `Update`, mitte `Install`**.



![Image](assets/fr/41.webp)



See on väga oluline punkt: kui Android kuvab `Install` asemel `Update`, siis installite tõenäoliselt võltsitud versiooni. Sellisel juhul katkestage paigaldusprotseduur kohe.



Nagu ka esimese paigalduse puhul, kontrollige enne uuendamise jätkamist faili .apk autentsust ja terviklikkust.



Et teada saada, millal uus versioon on saadaval, vaadake aeg-ajalt Ashigaru ametlikul veebisaidil. Võite olla kindel, et Ashigaru on stabiilne ja küps rakendus, mis on päritud Samourai Wallet-lt, ning uuendusi tehakse noorema tarkvaraga võrreldes suhteliselt harva.



## 9. Annetada Ashigaru projektile



Ashigaru on avatud lähtekoodiga projekt. Kui soovite selle arendamist toetada, võite teha annetuse otse rakendusest PayNymi kaudu.



Selleks klõpsake oma PayNym'ile liideses üleval paremal ja valige seejärel oma maksekood, mis algab tähega `PM...`.



![Image](assets/fr/36.webp)



Seejärel vajutage ekraani paremas allservas nuppu "+".



![Image](assets/fr/37.webp)



Valige saajaks `Ashigaru Open Source Project`.



![Image](assets/fr/38.webp)



Klõpsake nupule `CONNECT`, et luua BIP47 sidekanal (rohkem selle protokolli kohta allpool olevas õpetuses).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Kui teavitustehing on kinnitatud, saate oma annetused projektile saata, klõpsates liideses paremas ülemises nurgas oleval väikesel valgel noolega.



![Image](assets/fr/40.webp)



Te teate nüüd, kuidas kasutada rakenduse Ashigaru põhifunktsioone. Edasistes õpetustes vaatleme, kuidas kasutada täiustatud kulutamistehinguid, samuti Whirlpool, Samurai Wallet-st päritud mündiühenduste rakendamist.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
