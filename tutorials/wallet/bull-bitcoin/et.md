---
name: Bull Bitcoin Wallet
description: Uurige, kuidas kasutada Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*BTC Sessionsi videoõpetus tutvustab teile Bull Bitcoin Wallet!* seadistamise ja kasutamise protsessi


Selles juhendis tutvustatakse Bull Bitcoin Wallet paigaldamist, konfigureerimist ja kasutamist. Saate teada, kuidas saata ja vastu võtta raha Bitcoin On-Chain, Liquid ja Lightning võrkudes ning kuidas Bitcoin võrkude vahel liikuda. wallet ulatuslikud funktsioonid teevad sellest võimsa, kõik-ühes-vahendi Bitcoin haldamiseks. Alustame.


## Sissejuhatus


Bull Bitcoin Wallet, mille on välja töötanud [Bull Bitcoin](https://www.bullbitcoin.com/), on **iseseisev** Bitcoin wallet, mis tähendab, et teil on täielik kontroll oma privaatvõtmete ja seega ka oma rahaliste vahendite üle, sõltumata kolmandast isikust. Avatud lähtekoodiga ja Cypherpunk filosoofiast lähtuv Wallet ühendab endas lihtsuse, konfidentsiaalsuse ja täiustatud funktsioonid, nagu võrkudevahelised vahetused ja PayJoini tugi. See võimaldab teil hallata oma bitcoine kolmes võrgus: **Bitcoin onchain**, **Liquid** ja **Lightning**, millest igaüks on kohandatud konkreetsetele kasutusviisidele. [BullBitcoin GitHubis](https://github.com/orgs/SatoshiPortal/projects/49) saate tutvuda praeguste teemade ja eelseisvate arengutega. Kuna projekt on 100% avatud lähtekoodiga ja "avalikult ehitatud", võite saata ka oma ettepanekuid ja kõiki vigu, millega te kokku puutute. Kuigi mõned rahakotid toetavad nüüd mitut võrku, paistab Bull Bitcoin Wallet silma selle poolest, et ta integreerib sügavuti privaatsusfunktsioone kõikides võrkudes, mis teeb sellest võimsa vahendi oma Bitcoin haldamiseks kõigis suuremates võrkudes


## 1️⃣ Eeldused


Enne **Bull Bitcoin Wallet** kasutamise alustamist veenduge, et teil on olemas järgmised esemed:



- Ühilduv nutitelefon**: **iOS** (iPhone või iPad) või **Android** seade
- Interneti-ühendus
- Turvaline varunduskandja**: Kirjutage oma **tagasivõtmislause** (12 sõna) paberile või metallile ja hoidke seda turvalises kohas.
- Põhiteadmised**: Bitcoin mõistete (aadressid, tehingud, tasud) minimaalne mõistmine on kasulik, kuigi see õpetus selgitab iga sammu algajatele.


## 2️⃣ Paigaldamine


Rakenduse saab paigaldada läbi:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(iOS-seadmetele)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (Android-seadmetele)


Androidi kasutajatel on ka alternatiivseid võimalusi:



- Lae APK otse [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) lehelt või
- Paigaldage läbi Nostr-ga ühilduva [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Pärast rakenduse installimist jälgige tervitusekraanil oma konto konfigureerimist.


## 3️⃣ Esialgne konfiguratsioon


Avamisel kuvatakse järgmised valikud:



- `Loo uus Wallet`
- `Recover Wallet` ja
- "Täiustatud valikud


Alustame valiku "Täiendavad valikud" koputamisest.


Siin saame enne wallet loomist või taastamist konfigureerida täiustatud seaded:


1. Lülita sisse `Tor proxy`, et suunata liiklust üle Tor võrgu.

1. [Orbot app](https://orbot.app/en/) peab olema paigaldatud ja töötab enne aktiveerimist

2. Tor Proxy kehtib ainult Bitcoin (mitte Liquid) suhtes ja võib põhjustada aeglasema ühenduse.

2. Seadistage `Custom Electrum Server` või

3. Reguleerige seaded `Recover Bull`. Lisateavet [Recover Bull](https://recoverbull.com/) kohta saame hiljem.


Kui olete teinud kõik valikulised kohandused, puudutage valikut "Valmis". Kui soovite olemasolevat Wallet uuesti kasutada, klõpsake nuppu `Recover Wallet` ja täitke oma taastamislause 12 sõna.


Vastasel juhul klõpsake nuppu "Loo uus Wallet".


![image](assets/en/01.webp)


## 4️⃣ Avakuva


Enne kui me sügavamale sukeldume, heidame orienteerumiseks pilgu "Avakuvale":



- tehingute ülevaade ja seadete menüü asuvad üleval.
- Saldo "Kättesaadav" on privaatsuse valik, mida saab sisse või välja lülitada.
- Juurdepääs "Bitcoin Bull Exchange", et "osta, müüa või maksta" (see sõltub jurisdiktsioonist ja võib nõuda KYC-i).
- raha ülekandmine rahakottide vahel
- "Turvaline Bitcoin" võrdub "Onchain Bitcoin Wallet"
- "Pikamaksed" Lightning- / Liquid Network kaudu *(Märkus: Bull Bitcoin Wallet võimaldab makseid teha ja vastu võtta Lightning'i kaudu. Lightning'i kaudu saadud raha salvestatakse [*Liquid võrku](https://liquid.net/) (Wallet Pikamaksed) tänu automaatsele vahetusele [*Boltz vahetuse](https://boltz.exchange/) kaudu. See annab teile võimaluse suhelda Lightninguga, ilma et peaksite likviidsuskanaleid haldama, jäädes samal ajal isehoidjaks)*)
- vahendite saatmine ja vastuvõtmine


![image](assets/en/02.webp)


Esmalt teeme mõned olulised seadistused ja alustame `Backup`iga.


## 5️⃣ Varukoopia


Varundamise alustamiseks koputage rakenduse paremas ülemises nurgas asuvat "hammasratta ikooni (⚙)" ja valige "Wallet varundamine". Teile kuvatakse kaks meetodit oma wallet kindlustamiseks: `Encrypted Vault` ja `Physical Backup`. Uurime mõlemat.


![image](assets/en/03.webp)


### Füüsiline varundamine


Puudutage valikut "Füüsiline varundus", et näha loetelu 12 sõnast, mis esindavad teie taastamise või seed fraasi. Palun arvestage järgmist:



- Kirjutage oma "taastumislause" üles ülima hoolikusega. Kirjutage see paberile või metallile ja hoidke seda turvalises kohas (seif, offline-koht). See fraas on teie ainus vahend, mille abil saate oma bitcoinidele ligi, kui seade kaob või rakendus kustutatakse.
- Samuti on oluline märkida, et igaüks, kes seda lauset kasutab, võib kõik teie bitcoinid varastada. Ärge kunagi salvestage seda digitaalselt:
- Puudub ekraanipilt
- Pilve, e-posti või sõnumite varukoopiaid ei ole
- Ei ole kopeerimist/liitmist (oht, et salvestatakse lõikelauale)


![image](assets/en/25.webp)


Järgmisel ekraanil peate panema sõna õiges järjekorras, et veenduda, et seed lause on õige. Saate kinnituse, kui test on tehtud ja see on edukas.


! **See punkt on kriitiline**. Täiendava abi saamiseks :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Krüpteeritud hoidla


Samuti on võimalik teha krüpteeritud, anonüümne varukoopia pilves. Aga kas me ei maininud eelmises lõigus, et pilves varundamine on riskantne ja seda tuleks vältida? Bull Bitcoin meeskond on aga välja töötanud nutika viisi, kuidas muuta protsess turvaliseks. See toimib järgmiselt:


`Recoverbull` on varundusprotokoll, mis lihtsustab teie Bitcoin wallet turvamist, jagades varundamise kaheks osaks. Esiteks krüpteeritakse teie wallet varundusfail teie seadmes, kasutades tugevat krüpteerimisvõtit. Selle krüpteeritud faili saate salvestada kuhu iganes te soovite, näiteks Google Drive'ile või oma seadmesse. Teiseks, faili avamiseks vajalik krüpteerimisvõti on salvestatud Recoverbull Key Serveris. wallet taastamiseks on teil vaja nii krüpteeritud varundatud faili kui ka võtit, millele pääsete ligi oma PIN-koodi või parooliga. See disain tagab, et teie pilvevarukoopia üksi on kasutu ja et võtmeserver üksi on kasutu ilma teie konkreetse varukoopiafailita. See hoiab teie vahendid turvaliselt isegi siis, kui üks osa on ohus.


Mõelge sellest nagu seifist. Krüpteeritud varundatud fail on *karp*, mida saate hoida ükskõik kus (näiteks Google Drive'is). Teie taastamise PIN-kood on *võti*, mida salvestatakse eraldi Recoverbull Key Serveris. Varas peaks selle avamiseks saama nii teie konkreetse kasti kui ka teie konkreetse võtme. See disain tagab, et isegi kui keegi saab teie varukoopiafaili, on see kasutu ilma serveri võtmeta ja serveri võti on kasutu ilma teie unikaalse varukoopiafailita.


Lisateave `Recoverbull` wallet varundusprotokolli kohta [siin](https://recoverbull.com/).


Koputage valikut "Krüpteeritud võlv" ja seejärel "Jätka", et kinnitada vaikimisi serveri kasutamine. Ühendus suunatakse läbi `Tor` võrgu, et tagada privaatsus ja anonüümsus.


**PIN-koodide mõistmine**



- "Rakenduse avamise PIN-kood "**:** Valikuline PIN-kood, mis on määratud menüüs "Seaded > Turvalisuse PIN-kood", et lukustada telefonis olev rakendus.
- "Taastamis PIN "**:** Kohustuslik PIN-kood, mis on loodud "Salastatud Vault" varundamise käigus ja mida kasutatakse varundatud faili dekrüpteerimiseks taastamise ajal.


Need on kaks eraldi PIN-koodi. Ärge unustage oma taastamise PIN-koodi, sest see on teie wallet taastamiseks hädavajalik."


**Recovery PIN seadistamine:**



- Te peate looma PIN-koodi või salasõna, et taastada juurdepääs oma wallet-le.
- PIN-kood / parool peab olema vähemalt 6-kohaline (nt vältige lihtsaid jadasid nagu 123456, mida ei aktsepteerita).
- Ilma selle PIN-koodita on wallet taastamine võimatu.


Järgmisena valige võlvkambrite pakkuja:



- "Google Drive" või
- "kohandatud asukoht" (nt teie seade)


![image](assets/en/04.webp)


Nüüd salvestage `backup fail`. Seejärel koputage valikut `Test Recovery`, valige oma salvestatud varukoopiafail või võlv ja seejärel koputage valikut `Decrypt Vault`. Sisestage oma `PIN` või `Password`. Kui kõik töötas, ilmub ekraan `Testimine edukalt lõpetatud`.


### Impordi / ekspordi etiketid


Nüüd, kui me oleme loonud oma varukoopia, siis vaatame `Labels`.  Bull Bitcoin wallet parandab privaatsust ja korraldust, võimaldades kasutajatel luua oma vastuvõtuaadresside ja tehingute jaoks kohandatud sildid. Need sildid aitavad teil oma vahendeid kategoriseerida, sest sildiga varustatud aadressile saadetud tehingud pärivad selle sildi, samuti saate sildistada väljaminevad tehingud, et jälgida nende muutumist. wallet toetab täielikult standardit [BIP-329](https://bip329.org/), mis tähendab, et saate kõik oma sildid eksportida faili ja importida neid teise wallet-sse. See funktsioon tagab, et saate sujuvalt varundada oma tehinguajalugu ja kategoriseeringuid või migreerida neid wallet eri instantside vahel, ilma et kaotaksite oma isiklikku korraldust.


![image](assets/en/05.webp)


## 6️⃣ Seadistused


Kui teie esmane varukoopia on kindlustatud, uurime teisi seadetes saadaval olevaid funktsioone.


### A - Juurdepääsu tagamine


Rakenduse kaitsmiseks navigeerige menüüsse `Settings` ja valige `Security PIN`, et valida PIN-kood. Looge tugev PIN-kood, et lukustada juurdepääs oma wallet-le. Kuigi see samm on vabatahtlik, on see väga soovitatav, et vältida volitamata juurdepääsu, kui keegi teine kasutab teie telefoni.


![image](assets/en/06.webp)


### B - ühendus isikliku sõlme (valikuline)


Wallet BullBitcoin ühendub vaikimisi Electrum serveritega: esimene, mida haldab Bull Bitcoin ja teine Blockstream'i server, mis mõlemad ei pea logisid, vähendades jälgimise riski.


Suurema konfidentsiaalsuse tagamiseks saate rakenduse ühendada oma Bitcoin sõlme Electrum serveri kaudu. Selleks koputage valikut "Seaded" > "Bitcoin seaded" > "Electrum Server seaded", seejärel koputage valikut "+ Lisa kohandatud server", et sisestada oma serveri aadress ja volitused.


![image](assets/en/07.webp)


### C - Valuuta


Saldo kuvatakse põhiekraanil nii sats kui ka USA dollarites. Selle muutmiseks navigeerige menüüsse `Settings` > `Currency`. Seal saate vahetada `sats/BTC` vahel ja valida oma vaikimisi fiat-valuuta.


![image](assets/en/08.webp)


### D - Bitcoin seaded


Menüü "Bitcoin seaded", mis pakub põhjalikku juurdepääsu teie wallet põhikonfiguratsioonidele ja andmetele. Siin saate kontrollida oma `Secure Bitcoin` ja `Instant payments wallets` põhilisi üksikasju, andes teile täieliku läbipaistvuse ja kontrolli. Selle menüü põhifunktsioonid on järgmised:



- Wallet üksikasjad:** Konkreetse teabe vaatamiseks navigeerige oma turvalise Bitcoin või välkmaksete wallet juurde.
- Wallet sõrmejälg:** Teie wallet unikaalne identifikaator.
- Avalik võti (Pubkey):** Võti, mida kasutatakse teie generate vastuvõtuaadresside Bitcoin vastuvõtmiseks.
- Descriptor:** Tehniline kokkuvõte teie wallet struktuurist.
- Tuletamise tee:** Konkreetne tee, mida kasutatakse generate kõigi aadresside tuletamiseks teie peamise privaatvõtme alusel.
- Address View:** Juurdepääs oma kasutamata vastuvõtuaadresside nimekirjale ja aadresside muutmine (varsti saadaval)


Lisaks on teil võimalus:



- "Aktiveeri automaatne ülekanne" seaded, et määrata maksimaalne kohene wallet saldo, mis kantakse seejärel automaatselt üle turvalisse bitcoin wallet-sse.
- Importida üldisi rahakotte `Mnemonic` fraasi kaudu või importida `watch-only`
- Connect `Hardvarakomplektid`: praegu toetatud seadmed on ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade ja Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Otse wallet-st on teil juurdepääs [Bull Bitcoin vahetusele] (https://www.bullbitcoin.com/), mis võimaldab teil osta, müüa ja maksta Bitcoin ilma rakendusest lahkumata. See integratsioon pakub mugavat lahendust oma Bitcoin vajaduste haldamiseks. Pange tähele, et juurdepääs börsile ja selle teenustele võib olla teie jurisdiktsioonist lähtuvalt piiratud ning regulatiivsete standardite järgimiseks ja platvormi kõigi funktsioonide kasutamiseks võib olla vajalik kliendiandmete kontrollimine (KYC).


Alustamiseks koputage paremas alumises nurgas "Exchange", seejärel "Registreeru" või "Logi sisse" oma kontole.


Börsil on järgmised [funktsioonid](https://www.bullbitcoin.com/):



- Ostke Bitcoin oma pangakontolt iseteenindusega
- Mittekaitstavad isikud
- Üksikisikud või ettevõtted
- Kohene väljavõtmine
- Ei mingeid varjatud tasusid
- Lightning Network saadaval
- Tehingupiirangud puuduvad
- Korduvad ostuvõimalused


![image](assets/en/09.webp)


Lisateabe saamiseks külastage seda õpetust:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Raha saamine


Raha vastuvõtmine **Bull Bitcoin Wallet** abil on lihtne ja paindlik, toetades kolme erinevat võrku, mis on kohandatud erinevatele kasutusviisidele:



- Bitcoin (onchain)-võrk turvaliseks ja pikaajaliseks säilitamiseks.
- "Liquid" võrk kiireks ja konfidentsiaalsemaks tehinguks.
- "Lightning" võrgustik kiireks ja odavaks maksmiseks.


Rakendus genereerib automaatselt sobiva aadressi või arve vastavalt valitud võrgule. Järgnevalt on kirjeldatud, kuidas iga võrgu puhul toimida.


### Vastuvõtmine Onchaini kaudu (Bitcoin võrk)


on-chain vahendite vastuvõtmiseks võite kas valida Avakuval "Turvaline Bitcoin Wallet" ja koputada nuppu "Vastuvõtmine" või koputada põhinuppu "Vastuvõtmine" ja seejärel valida "Bitcoin võrk".


Vastuvõtuaadressi genereerimiseks on kaks peamist režiimi:


**Vaikimisi režiim (URI koos täiendavate sisendparameetritega)


Vaikimisi genereerib wallet [BIP21 URI] (https://bips.dev/21/). See on standarditud vorming, mis pakendab rohkem teavet kui lihtne aadress, sealhulgas summa, isikliku märkuse ja PayJoini parameetrid, et suurendada privaatsust. See terviklik URI kodeeritakse QR-koodiks ja tehakse kopeerimiseks kättesaadavaks. Formaat näeb välja selline: `bitcoin:<aadress>?<parameeter1>=<väärtus1>&<parameeter2>=<väärtus2>`.



- Täiendavad sisendparameetrid:**
    - Summa:** Määrake soovitud summa BTC, sats või fiat-valuutas.
    - Sõnum:** Lisage isiklik märkus, mis on saatjale nähtav.
    - PayJoin:** Võta see valik kasutusele, et parandada privaatsust, ühendades tehingus nii saatja kui ka vastuvõtja sisendid.


Näide URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Tähtis märkus: Palun ärge saatke rahalisi vahendeid selles õpetuses toodud aadressidele, wallet kustutatakse.*


![image](assets/en/10.webp)


**Kopeeri või skaneeri ainult Address valik on lubatud


Kui valik "Ainult Address kopeerimine või skaneerimine" on lubatud, genereerib rakendus lihtsa Bitcoin aadressi SegWit (bech32) formaadis.


Näide:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Isegi kui sisestate summa või märkuse, ei lisata neid QR-koodi ega kopeeritud aadressi.


![image](assets/en/11.webp)


### Vastuvõtmine Liquid Network kaudu


Võite saada makse Liquid Network kohta. Kui olete ekraanil "Vastuvõtmine", on teil samad kaks võimalust maksetaotluse koostamiseks:


**1. Lihtne Address:** Kopeerige standardne Liquid aadress. See on teie wallet unikaalne identifikaator Liquid võrgus ja ei sisalda mingit konkreetset summat ega sõnumit.


Näide Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Üksikasjalik maksetaotlus (URI):** Struktureerituma taotluse puhul saate määrata summa ja isikliku märkuse. See teave kodeeritakse automaatselt jagatavaks URI-ks ja vastavaks QR-koodiks.



- Summa:** Saate määrata summa Bitcoin (BTC), Satoshis (Sats) või fiat-valuutas.
- Märkus:** Lisage isiklik sõnum tehingu identifitseerimiseks.


**Näide URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Tehingu lõpuleviimiseks esitage saatjale "aadress" või "URI". Võite seda teha, kopeerides selle oma lõikelauale või lasta neil skannida QR-koodi otse oma ekraanilt.


![image](assets/en/12.webp)


### Vastuvõtmine välklambi kaudu



Bull Bitcoin Wallet võimaldab teil saata ja vastu võtta makseid ka Lightning Network kaudu. Oluline omadus on, et Lightning'i kaudu saadud raha vahetatakse automaatselt Liquid Network-sse ja salvestatakse Wallet-sse "Instant Payments". See teenus töötab `Boltz` abil. Selline disain võimaldab teil kasutada Lightning'i kiirust ja madalat hinda ilma likviidsuskanalite haldamise keerukuseta, säilitades samal ajal oma vahendite täieliku iseseisva haldamise. Kuigi see hübriidne lähenemisviis on isehaldatav ja väldib kanalite haldamise keerukust, toob see kaasa kolmanda osapoole teenuse (Boltz), väikese vahetustasu ja sõltuvuse Liquid Network funktsionääride föderatsioonist kui võtmeomanikest, mis erineb traditsioonilisest, mittehaldatavast Lightning wallet-st, kus te ise haldate oma kanaleid. Lisateavet Liquid ja selle haldusmudeli kohta saate siit:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Piirangud:**
    - Minimaalne summa:** Nõutav on minimaalne arve summa. Palun kontrollige rakendusest kehtivat piirmäära
    - Tasud:** Teie, vastuvõtja, vastutate väikese vahetustasu eest. See tasu arvatakse maha saatja poolt ülekantavast summast ja see võib muutuda
- Eelised:**
    - Iseteenindus:** Teie rahalised vahendid on alati teie kontrolli all, kindlustatud Liquid võrgus.
    - Vältige kõrgeid On-Chain tasusid:** Kasutades Lightningit ja salvestades Liquid-s, saate vältida on-chain tasusid, mis on seotud traditsioonilise Lightning-kanali avamisega. Te võite hiljem, kui kogunenud summa õigustab kulutusi, valida vahendite ülekandmise on-chain kanalisse.
    - Vihje:** Kõige kuluefektiivsema tehingu tegemiseks kahe Bull Bitcoin kasutaja vahel kasutage otse **Liquid võrku**, et vältida täielikult välkkiirte vahetustasu.


Makse saamiseks peate esitama generate "Välkarve":


1. "Sisestage summa "**:** Määrake summa, mida soovite saada Bitcoin (BTC), Satoshis (Sats) või fiat-valuutas.

2. "Lisa märkus" **(valikuline):** Lisage märkus või märkus. See lisatakse arvele ja kuvatakse teie tehinguajaloos, kui makse on sooritatud, et seda oleks lihtsam tuvastada.

3. "Invoice kehtivus "**:** Välkarve on ajaliselt piiratud ja kaotab kehtivuse **12 tunni** pärast. Kui seda ei ole selle aja jooksul tasutud, muutub see kehtetuks ja te peate generate uue arve koostama.


Andke saatjale arve, kopeerides selle oma lõikelauale või lastes neil skaneerida ekraanil kuvatavat QR-koodi.


![image](assets/en/13.webp)


## 9️⃣ Raha saatmine


Saate saatmisekraanile pääseda otse avalehelt või mis tahes rahakotist. Bull Bitcoin Wallet lihtsustab protsessi, tuvastades automaatselt sihtvõrgu - "Bitcoin", "Liquid" või "Lightning" - sisestatud aadressi või arve alusel, olenemata sellest, kas see on kleebitud või skannitud QR-koodi abil.


### On-Chain edastamine Bitcoin võrgu kaudu


Raha saatmine on-chain tähendab, et teie tehing salvestatakse otse Bitcoin plokiahelas. See meetod on parim suuremate ülekannete või mittetundlike ülekannete puhul. Alustamiseks võite vajutada nuppu "Saada" all paremal ja skaneerida või sisestada "standard Bitcoin aadressi".


Kui teie esitatud aadress ei sisalda konkreetset summat, palutakse teil üksikasjad sisestada saatmise ekraanil. Võite määrata summa oma eelistatud ühikus, näiteks BTC, satoshis või fiat-ühikus. Teil on ka võimalus lisada isiklik märkus, mis on isiklik märkus teie enda jaoks, et aidata teil hiljem tehingut tuvastada. Seda märkust ei edastata saajale.


Seevastu kui skannitud või kleebitud maksetaotlus sisaldab juba kõiki vajalikke üksikasju, näiteks BIP21 URI-d koos eelnevalt määratud summaga, siis wallet möödub andmete sisestamise ekraanist ja viib teid otse makse kinnitamise ekraanile, et autoriseerida makse.


![image](assets/en/14.webp)


Enne tehingu edastamist kuvatakse teile kinnitusekraan. On väga oluline, et te võtaksite aega ja vaataksite hoolikalt läbi kõik parameetrid, pöörates suurt tähelepanu saaja aadressile, saadetava summa suurusele ja võrgutasudele. See ekraan pakub ka võimsaid vahendeid oma tehingu kohandamiseks.


Tasusid saab kontrollida peamiselt kahel viisil. Esimene meetod on valida soovitud tehingukiirus, näiteks madal, keskmine või kõrge, ning wallet arvutab teile automaatselt sobiva tasu. Teine meetod võimaldab täpsemat kontrolli, võimaldades teil määrata konkreetse tasu, kas absoluutse kogusumma satoshi või suhtelise määra baidi kohta, mis annab seejärel hinnangulise kinnitamisaja.


Edasijõudnud kasutajatele pakub wallet mitmeid seadistusi tehingu peenhäälestamiseks. vaikimisi on sisse lülitatud `Replace-by-Fee` (RBF), mis on väärtuslik funktsioon, mis võimaldab teil kiirendada tehingut, kui see jääb mempoolis kinni, edastades selle uuesti kõrgema tasuga. Saate ka käsitsi valida, millistest `Unspent Transaction Outputs` (UTXOs) kulutada. See on võimas vahend UTXO konsolideerimiseks, strateegia, mille puhul ühendate mitu väikest sisendit üheks suuremaks. Kuigi see võib praeguse tehingu puhul maksta rohkem tasusid, võib see oluliselt vähendada tulevaste tehingute tasusid, eriti kui võrgutasud peaksid eeldatavasti tõusma.


![image](assets/en/15.webp)


PayJoin käivitub automaatselt, kui skannite saaja maksetaotluse (BIP21 URI), mis sisaldab parameetrit `pj=`. Kui te lihtsalt kleebite tavalise aadressi ilma lisaparameetriteta, siis see funktsioon ei aktiveeru. See koostöömeetod parandab privaatsust, kombineerides nii saatja kui ka vastuvõtja sisendeid, murdes ühise sisendi-omandi heuristikat ja võimaldades mõnes olukorras ka paremat skaleerimist ja tasude kokkuhoidu.


### Saatmine Liquid Network-le


Liquid Network on mõeldud kiireks, konfidentsiaalseks tehinguks minimaalsete tasudega. Kui saadate raha Liquid kaudu, võetakse see välja teie `Instant Payments Wallet`st. Protsess on lihtne: te lihtsalt sisestate või skaneerite saaja `Liquid aadressi`.


Kui aadressil ei ole summat määratud, palutakse teil see esitada saatmise ekraanil. Võite sisestada summa BTC-des, satoshides või fiatites. Liquid peamine eelis on selle madal miinimumkünnis. Nagu on-chain tehingute puhul, saate lisada vabatahtliku isikliku märkuse enda jaoks. Kui maksetaotlus sisaldab juba summat, liigub wallet otse kinnituse ekraanile.


Liquid tehingu kinnitusekraanil vaatate läbi üksikasjad. Tasud on märkimisväärselt madalad ja need arvutatakse vastavalt tehingu keerukusele. Need on tavaliselt umbes 0,1 sat/vB, mis lihtsa tehingu puhul on vaid 20-40 satoshit (näiteks 26 satoshit seisuga 21. detsember 2025).


![image](assets/en/16.webp)


### Saatmine Lightning Network-le


Saate kas skaneerida välk Address (nt "runningbitcoin@rizful.com"), mis võimaldab teil määrata summa ja vabatahtliku märkuse saaja jaoks, või skaneerida eelnevalt määratud summaga arve, mis viib teid otse kinnitusekraanile.


*Pange tähele, et kehtivad miinimumsummad ja tasud.*


Bull Bitcoin Wallet saadab välkmakseid, võttes raha välja teie "Instant Payments Wallet" (Liquid-l) ja vahetades seda "Boltz" kaudu. See hübriidlähenemine on täielikult isemajandav ja väldib spetsiaalse Lightning-kanali haldamisega seotud kõrgeid on-chain tasusid, kuid see nõuab `vahetustasude` maksmist. Madalaima hinna saamiseks saatke otse saaja Liquid aadressile, kui ta kasutab ka Bull Bitcoin wallet.


## 🔟 Raha ülekandmine rahakottide vahel


Bull Bitcoin võimaldab teil oma Bitcoin-i liigutada oma "turvalise Bitcoin" wallet ja oma Liquid Network-i või "välise Wallet" Wallet-i vahel. Ülekande tegemiseks navigeerige lihtsalt jaotisesse `Transfer`, valige lähte- ja sihtrahakott, sisestage summa, mida soovite üle kanda, ja kinnitage tehing.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Teie Bull Bitcoin Wallet taastamine


Selles jaotises selgitatakse, kuidas taastada juurdepääs oma Bull Bitcoin Wallet rahalistele vahenditele, kui kaotate oma seadme, eemaldate rakenduse või peate lihtsalt vahetama uue seadme vastu. Nagu juba selgitatud, on taastamiseks kaks peamist meetodit: kasutades unikaalset `Recoverbull` meetodit ja kasutades standardset `BIP39 seed fraasi`.


### Meetod 1: Recoverbull


Kokkuvõte: Wallet varukoopiaid krüpteeritakse lokaalselt. Krüpteeritud faili saab salvestada pilvesalvestusse või mõnda teise seadmesse. Krüpteerimisvõti salvestatakse Recoverbull Key Serveris. Mõlemat hoitakse eraldi ja wallet taastamiseks tuleb neid kombineerida.


Alustuseks kustutan Wallet koos kõigi fondidega ja paigaldan uuesti wallet. Maandume taas `Tervitusekraanile`. Seekord valige valik `Recover Wallet`. Seejärel navigeerige meetodile `Encrypted Vault`, kinnitage, et kasutate `Default Key server`, ja valige asukoht või `Vault provider`, kuhu te salvestasite varundatud faili.


![image](assets/en/18.webp)


See näitab, et võlv on edukalt imporditud. Koputage nuppu `Decrypt Vault` ja sisestage `PIN`. Järgmisel ekraanil kuvatakse teie "saldod" ja "tehingute arv", mis taastati.


![image](assets/en/19.webp)


### Meetod 2: seemnefraas


See meetod kasutab teie wallet peamist taastamislauset, mis on standardne 12 sõnaline nimekiri, mis on teie vahendite lõplikuks varunduseks. See on kõige universaalsem viis Bitcoin wallet taastamiseks, kuna see ei ole seotud ühegi konkreetse teenuse või serveriga. Kui teil on see fraas olemas, saate taastada oma wallet mis tahes ühilduvas seadmes, isegi ilma juurdepääsuta Bull Bitcoin võtmeserverile.


Valige tervitusekraanilt "Wallet taastamine". Seekord valige meetod `Füüsiline varundamine`. Rakendus esitab sõnade ruudustiku. Valige hoolikalt iga sõna oma 12 -sõnalise seed fraasi õiges järjekorras. Olge täpne, sest ühegi vea korral on wallet vale.


## 1️⃣2️⃣ Hardware Wallet ühendamine


Kõrgeima turvalisuse tagamiseks otsustavad paljud Bitcoin kasutajad hoida oma raha "külmhoidlas". See tähendab, et teie Bitcoin-d kontrollivaid "privaatvõtmeid" hoitakse seadmes, mis ei ole kunagi ühendatud internetti. wallet (või signimisseade) on spetsiaalne füüsiline seade, mis on loodud just selleks otstarbeks. See toimib nagu teie võtmete digitaalne hoidla, mis tagab, et need ei ole kunagi avatud võimalikele ohtudele, mis võivad tekkida internetiarvutis või nutitelefonis.


Ühendades riistvaralise wallet Bull Bitcoin rakendusega, saate mõlemast maailmast parima: oma isiklike võtmete kompromissitu turvalisuse külmhoidla koos Bull Bitcoin wallet võimsate funktsioonide ja kasutajasõbraliku kasutajaliidesega saldode vaatamiseks ja tehingute haldamiseks. Selles viimases peatükis näitame teile, kuidas ühendada riistvaraline wallet, näiteks [Coldcard Q] (https://coldcard.com/q), teie Bull Bitcoin wallet-ga. Selles õpetuses ei käsitleta põhjalikult Coldcard Q seadistamist; selle kohta saate teavet siin:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Wallet importimine


![image](assets/en/26.webp)


Kõigepealt valige Coldcard Q peamenüüst "Wallet eksport" ja seejärel "Bull Wallet". Teie Coldcard generateQR-koodi.


![image](assets/en/20.webp)


Avage Bull Bitcoin Wallet ja navigeerige menüüsse `Settings` > `Bitcoin Settings` > `Import wallet` ja valige oma telefonis `Coldcard Q` ja koputage `Open the camera`, et skannida seda QR-koodi, et importida oma riistvara wallet avalikud võtmed.


![image](assets/en/21.webp)


### Vastuvõtmine Coldcardiga Q


Bitcoin vastuvõtmiseks ühendatud Coldcard Q abil ei ole vaja, et seade oleks füüsiliselt teie telefoniga ühendatud. Bull Bitcoin Wallet on juba importinud vajalikud avalikud võtmed, mis võimaldab tal ise generate-aadressi importida.


1. Puudutage oma imporditud Coldcard Q allkirjastamise seadet ja valige "Vastuvõtmine".

2. Rakendus kuvab automaatselt värske Bitcoin aadressi teie Coldcard wallet-st.

3. Kasutage seda aadressi vahendite saamiseks. Bitcoin kinnitatakse otse riistvara wallet võtmetele, kuigi seade oli protsessi ajal võrguühenduseta.


![image](assets/en/22.webp)


### Coldcardiga saatmine Q


Bitcoin saatmine koos Coldcard Q-ga nõuab teie füüsilist kinnitust, et autoriseerida mis tahes tehing. Kuigi Bull Wallet rakendust kasutatakse tehingu koostamiseks, saab lõpliku allkirja luua ainult riistvaral wallet ise.


Alustamiseks avage oma "Kuldkaart Q" wallet ja koputage nuppu "Saada". Seejärel avage kaamera, et skannida vastuvõtva aadressi QR-koodi. Pärast skaneerimist sisestage `summa`, mida soovite saata, ja reguleerige vastavalt vajadusele `tasu prioriteeti`.


Rohkem valikuid saate vaadata jaotisest Täpsemad seaded. Siit leiate valiku `Kõrvaldamine tasu alusel` (RBF), mis on vaikimisi aktiveeritud ja võimaldab teil hiljem kiirendada kinni jäänud tehingut. Samuti on teil valik `Coin Control`, mis võimaldab teil käsitsi valida konkreetsed UTXO-d, mida soovite kulutada.


Kui olete kõik üksikasjad läbi vaadanud, koputage tehingu ettevalmistamiseks nuppu "Näita PSBT".


![image](assets/en/23.webp)


Puudutage Coldcard Q nuppu "Skaneerimine" ja skannige telefonis kuvatavat QR-koodi selle kaamera abil. Seejärel kuvatakse Coldcardi ekraanil kõik tehingu üksikasjad. Kontrollige hoolikalt summat, saaja aadressi ja oma muutmisaadressi. Kui kõik on õige, vajutage tehingu allkirjastamiseks Coldcard Q-l nuppu "Enter". Seejärel ilmub ekraanile allkirjastatud tehingu QR-kood.


![image](assets/en/24.webp)


Puudutage Bull wallet ekraanil valikut "Olen valmis", seejärel puudutage nuppu "Kaamera", et skaneerida allkirjastatud tehingu QR-kood oma Coldcard Q-lt. Bull Wallet kuvab nüüd allkirjastatud tehingu kokkuvõtte. Vaadake see veel kord üle ja seejärel koputage valikut `Broadcast` Transaction. See lõpetab protsessi, saates tehingu Bitcoin võrku ja teie raha on teel.


## 🎯 Kokkuvõte


Te olete nüüd oma teekonna läbi Bull Bitcoin Wallet lõpetanud. Rakendus asetab võimsad privaatsus- ja turvavahendid otse teie käeulatuses, muutes täiustatud funktsioonide kasutamise lihtsaks. See aitab teil jääda privaatseks selliste funktsioonidega nagu `PayJoin`, mis peidab teie tehingud plokiahelas, ja `Tor-integratsioon`, mis varjab teie võrguaktiivsuse uudishimulike silmade eest. Nende jaoks, kes soovivad täielikku kontrolli, saate ühendada oma isikliku Bitcoin-sõlme, et mitte enam loota kolmandate osapoolte serveritele, ja kasutada wallet-ga, et hoida oma privaatvõtmeid täiesti offline ja turvaliselt. Nutikate varundusvõimalustega ja Bitcoin, Liquid ja Lightningi sujuvaga on Bull Bitcoin Wallet tugev, kõik-ühes-valik kõigile, kes soovivad oma rahaliste vahendite privaatsust, turvalisust ja täielikku kontrolli all hoidmist.


## 📚 Bull Wallet ressursid


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Koduleht ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)