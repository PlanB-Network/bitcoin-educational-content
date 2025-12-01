---
name: Makadaamia Wallet
description: Cashu mobiilne wallet anonüümsete ja kiirete BTC maksete tegemiseks
---

![cover](assets/cover.webp)



Macadamia Wallet on iOS-i mobiilne wallet, mis rakendab Cashu protokolli, Chaumian ecash-süsteemi, mis võimaldab täiesti anonüümseid Bitcoin makseid. Tänu pimedatele allkirjadele ei saa ükski vaatleja teie sissemakseid teie kulutustega siduda, pakkudes füüsilise sularahaga sarnast konfidentsiaalsust.



Selles õpetuses vaatame, kuidas paigaldada ja konfigureerida Macadamia, teha oma esimesed Cashu tehingud (Mint, Send, Receive, Melt) ja hallata mitut minti, et kindlustada oma raha.



## Mis on Macadamia Wallet?



### Cashu protokoll



Cashu kasutab David Chaumi leiutatud pimedat allkirjastamist: te hoiustate bitcoin'id "mündi" serveris, mis väljastab samaväärseid märke satoshis. Rahapaja allkirjastab need märgid ilma nende sisu nägemata, mistõttu on võimatu siduda token kasutajaga. Vahetused on off-chain, peer-to-peer ja täiesti läbipaistmatu - isegi rahapaja ei saa jälgida, kes kellele maksab.



Macadamia on avatud lähtekoodiga wallet iOS, mis on arendatud Swift/SwiftUI-s. See töötab ilma konto või KYC-ta, teie märgid on salvestatud lokaalselt ja kaitstud seed fraasiga. Kood on auditeeritav GitHubis ja märgid on koostalitlusvõimelised teiste Cashu rahakottidega (Minibits, Cashu.me).



### Hooldusmudel ja kompromiss



**Tähtis**: Cashu tegutseb hooldusmudelil. Märgid on makselubadused (IOU), mille tagatis on rahapaja Bitcoin reservid. Kui rahapaja kaob, kaotavad teie žetoonid oma väärtuse. See on kompromiss maksimaalse konfidentsiaalsuse tagamiseks.



Kasutage makadaamiat kui füüsilist wallet: ainult väikestes kogustes. Hajutage oma vahendid mitme mündi peale, et lahjendada riski.



## Peamised omadused



Macadamia rakendab Cashu protokolli neli põhilist operatsiooni. **Mint** konverteerib teie satoshid Lightning-arve kaudu žetoonideks. **Send** võimaldab teil saata märgid tasuta QR-koodi või lingi kaudu, täiesti off-chain. **Vastuvõtmine** võimaldab teil saada žetoneid või generate Lightning-arve. **Sulatus** maksab Lightning-arve, hävitades teie märgid.



wallet toetab mitme kaevanduse samaaegset haldamist. Te saate Lightning'i kaudu vahetada žetoonide vahel.



## Toetatud platvormid



Macadamia on saadaval ainult iOS 17 või uuemal versioonil iPhone'ile ja iPadile. Native Swift/SwiftUI rakendus pakub optimaalset integratsiooni Apple'i ökosüsteemiga.



Cashu protokoll tagab rahakottide koostalitlusvõime. Saate taastada oma seed fraasi teistes rakendustes, näiteks Minibits Androidis või Nutstashis töölaual.



Praegust versiooni levitatakse TestFlight'i kaudu. Kasutage selle beetaversiooniga ainult väikestes kogustes.



## Paigaldamine



Macadamia on praegu saadaval TestFlight'i, Apple'i beetatestimise programmi kaudu. Siin on, kuidas seda paigaldada:



### Paigaldamine TestFlight'i kaudu



**Samm 1: Lae alla TestFlight**



Kui teil ei ole veel TestFlight'i rakendust oma seadmes, otsige App Store'is üles "TestFlight" ja installige see. TestFlight on Apple'i ametlik rakendus iOS-rakenduste beetaversioonide testimiseks.



**Samm 2: Liitu Macadamia beetaprogrammiga** (prantsuse keeles)



Kui TestFlight on paigaldatud, järgige seda kutselinki oma iPhone'ist või iPadist: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Link avab automaatselt TestFlight ja pakub teile Macadamia Wallet installimist. Puudutage "Accept" ja seejärel "Install", et alustada allalaadimist. Rakendus kaalub umbes kümme megabaiti ja selle paigaldamine võtab vaid mõned sekundid.



![Installation TestFlight](assets/fr/01.webp)



### Oluline teave beetaversioonide kohta



Macadamia on endiselt aktiivses arendusfaasis. TestFlight'i versioone uuendatakse sageli ja need võivad lisada uusi funktsioone või parandada vigu. Siiski, nagu iga beetaversiooni puhul, võivad esineda tõrkeid. ** Soovitame tungivalt kasutada ainult väikeseid koguseid**, mida te nõustute, et tehniliste probleemide korral võivad need kaduma minna.



Macadamia ei kogu kasutajate andmeid vastavalt esitatud privaatsuspoliitikale. Kontrollige installimisel kindlasti, et arendaja on cypherbase UG.



## Esialgne konfiguratsioon



Esimesel käivitamisel genereerib Macadamia 12 sõnast koosneva BIP-39 lause. Kirjutage need turvalisse kohta - mitte kunagi ekraanipildina. Need sõnad võimaldavad teil uuesti luua oma wallet ja kulutada oma žetoonid.



![Configuration initiale](assets/fr/02.webp)



Järgige nelja sammu: tervitus, tingimuste aktsepteerimine, seed lause salvestamine ja lõplik kinnitus.



![Interface principale](assets/fr/03.webp)



Kui seadistamine on lõpetatud, esitab Macadamia kolm peamist vahekaarti. **Wallet** näitab teie saldot ja tehinguajalugu. **Mints** võimaldab teil hallata oma Cashu servereid. **Settings** annab juurdepääsu seadetele ja teie seed fraasile.



![Ajout d'un mint](assets/fr/04.webp)



Nüüd peate konfigureerima mündi, st Cashu serveri, mis väljastab teie märgid. Minge vahekaardile "Mints", koputage valikut "Add new Mint URL" ja sisestage valitud mündi aadress (nt mint.cubabitcoin.org). Vaadake bitcoinmints.com või cashu.space mainekate avalike rahapajade kohta. Kinnitage ainult need rahapaigad, mille mainet olete kontrollinud, sest nemad hoiavad teie satoshisid.



## Igapäevane kasutamine



### Uute žetoonide loomine (Mint)



Selleks, et toita oma wallet Macadamiat ecashiga, peate tegema operatsiooni "Mint" (et luua žetoonid). Puudutage valikut "Receive", seejärel valige valik "Lightning". Sisestage soovitud summa (nt 1000 sats), valige kasutatav mündi, seejärel generate Lightning-arve.



![Opération Mint](assets/fr/05.webp)



Makske Lightning arve, mis on koostatud teie tavapärase wallet (Phoenix, Zeus, BlueWallet) abil.



![Confirmation Mint](assets/fr/06.webp)



Cashu märgid ilmuvad pärast maksmist koheselt teie saldole.



### Märgiste saatmine



Cashu-märkide saatmiseks teisele kasutajale puudutage põhiekraanil nuppu "Saada" ja seejärel valige "Ecash". Sisestage saadetav summa (nt 50 sats) ja lisage vajaduse korral kirjeldav märkus.



![Envoi Ecash](assets/fr/07.webp)



Jagage QR-koodi või genereeritud teksti iMessage'i, Signaali või Telegrami kaudu. Saaja nõuab raha koheselt ja tasuta.



### Võtke vastu žetoonid



Teise kasutaja saadetud Cashu-märkide vastuvõtmiseks puudutage valikut "Vastuvõtmine" ja seejärel valige "Ecash". Skaneerige token QR-koodi või kleepige saadud token link.



![Réception Ecash](assets/fr/08.webp)



Puudutage "Redeem", et taotleda token.



### Välkmaksed (sulatamine)



Lightning-arve tasumiseks Cashu-märkidega puudutage valikut "Saada" ja seejärel valige "Lightning". Sisestage BOLT11 arve, mille eest soovite tasuda.



![Paiement Lightning](assets/fr/11.webp)



Rahapaja hävitab teie žetoonid ja teostab välkmakse. Seega saate maksta mis tahes Lightning-teenuse eest, säilitades samal ajal oma anonüümsuse.



### Vahetage mündi vahel



Kui saate žetoonid rahapajast, mida te ei ole konfigureerinud, pakub Macadamia teile nende žetoonide haldamiseks mitmeid võimalusi.



![Swap inter-mints](assets/fr/09.webp)



Lisage uus rahapaja või vahetage žetoonid olemasoleva rahapaja vastu. Vahetus kasutab Lightningi kui silda, et kanda oma raha anonüümselt üle.



### Täiustatud mitme mündi haldamine



Macadamia pakub keerulisi vahendeid mitme mündi samaaegseks haldamiseks ja vahendite strateegiliseks jaotamiseks.



![Gestion multi-mints](assets/fr/10.webp)



"Raha jaotamine" jaotab automaatselt teie saldo vastavalt protsentidele (nt 50/50). "Ülekanne" võimaldab käsitsi ülekandeid rahapaikade vahel, et hajutada oma riske.



## Eelised ja piirangud



**Kõrgpunktid** :





- Maksimaalne konfidentsiaalsus**: Jälgimatuid tehinguid, isegi rahapaja poolt. Puuduvad plokiahela metaandmed, jälgimisvõimaluseta peer-to-peer-vahetused.
- Kiire ja tasuta**: Tasuta kohesed ülekanded mündi piires, ideaalsed mikromaksete tegemiseks.
- Koostalitlusvõime**: standardiseeritud Cashu-tokenid kasutamiseks teiste ühilduvate rahakottidega (Minibits, Nutstash).
- Lihtsus**: Interface iOS native on algajatele kättesaadav, jäädes samas kontrollitavaks (avatud lähtekood).



**Piirangud** :





- Hooldusmudel**: nõutav on mündi usaldus. Kui rahapaja kaob, kaotavad teie žetoonid oma väärtuse.
- ainult iOS**: Android/desktop versioon puudub. Cashu koostalitlusvõime võimaldab juurdepääsu teiste rahakottide kaudu, kuid optimaalne kogemus jääb iOS-i.
- Mündisõltuvus**: Mint offline = ei saa teostada tema sekkumist nõudvaid tehinguid (Mint, Melt).
- Arenev tehnoloogia** : Aktiivne areng, võimalikud vead, arenevad standardid.



## Parimad tavad





- Mitmekesistage oma münte**: Hajutage oma žetoonid mitme maineka mündi vahel, et lahjendada riski.
- Piirsummad**: Kasutage Macadamia't füüsilise wallet igapäevaste maksete tegemiseks, mitte seifina.
- Kindlustage oma seed**: Hoidke oma 12-sõnalist lauset paberil turvalises kohas. Testige aeg-ajalt taastamist.
- Kontrollige minte**: Cashu.space ja kogukonna foorumid enne mündi lisamist. Valige need, millel on hea kasutusaeg ja hea maine.
- VPN või Tor**: Peida oma IP-aadress VPN/Toriga, et maksimeerida võrgu privaatsust.
- Liitu kogukonnaga**: Telegram/Discord Cashu rühmadesse uuenduste, mündi soovituste ja parimate tavade saamiseks.



## Kokkuvõte



Macadamia Wallet toob füüsilise sularaha omadused digitaalsesse Bitcoin. Kombineerides Chaumi ja Lightning pimedad allkirjad, pakub see elegantset lahendust tehingute konfidentsiaalsuse tagamiseks. Selle emakeelne iOS-liides teeb keerulise krüptotehnoloogia kättesaadavaks, jäädes samas avatud lähtekoodiga ja koostalitlusvõimeliseks Cashu ökosüsteemiga.



Hooldusmudel nõuab valvsust ja häid turvatavasid. Õigesti kasutatuna saab Macadamiast hindamatu väärtusega vahend anonüümsust nõudvate igapäevaste maksete tegemiseks, mis täiendab säästmiseks kasutatavaid mittehoiustatavaid rahakotte.



## Ressursid



### Ametlikud dokumendid




- Ametlik veebileht: [macadamia.cash](https://macadamia.cash)
- Makadaamia KKK: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHubi lähtekood: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashu dokumentatsioon




- Tehniline dokumentatsioon: [docs.cashu.space](https://docs.cashu.space)
- Avalike rahapajade nimekiri: [bitcoinmints.com](https://bitcoinmints.com)
- Protokolli ametlik veebileht: [cashu.space](https://cashu.space)



### Ühendus




- Telegram Cashu grupp: [t.me/cashu_ecash](https://t.me/cashu_ecash)