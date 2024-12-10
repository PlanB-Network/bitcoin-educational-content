---
name: Samourai Wallet - Taastamine
description: Kuidas taastada bitcoine, mis on kinni jäänud Samourai Wallet'is?
---
![kaas](assets/cover.webp)

Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil on mõned rakenduse funktsioonid nüüdseks mitteoperatiivsed ning kasutajad, kellel pole oma Dojo't, ei saa enam tehinguid edastada.

Viimastel päevadel mitmele kasutajale nende bitcoinide taastamisel abistades usun, et olen kohanud enamikku probleeme, mis võivad Samourai Wallet'i taastamisel tekkida. Seetõttu alustame olukorra ülevaatega, et tuvastada funktsioonid, mis on Samourai Wallet ökosüsteemis endiselt töökorras ja need, mis enam saadaval ei ole, ning tarkvara, mida see intsident mõjutas. Järgmisena jätkame samm-sammult Samourai Wallet'i taastamisega, kasutades Sparrow Wallet tarkvara. Vaatleme kõiki potentsiaalseid takistusi, mis selle protsessi käigus ette võivad tulla, ja näeme lahendusi nende lahendamiseks. Lõpuks, viimases osas, avastate potentsiaalsed riskid teie privaatsusele pärast serveri konfiskeerimist.

*Suur tänu [@Louferlou](https://twitter.com/Louferlou)'le, kes on aidanud mitmel kasutajal taastuda ja jaganud minuga oma kogemusi, ning kes on samuti aidanud testida, mis on endiselt funktsionaalne.*

## Kas Samourai Wallet töötab endiselt?

Jah, **Samourai Wallet rakendus töötab endiselt**, kuid teatud tingimustel.

Esiteks on vajalik, et rakendus oleks varem teie nutitelefonis installitud. Google Play Store on rakenduse eemaldanud ja APK oli majutatud konfiskeeritud veebilehel. Seetõttu on Samourai praegu paigaldamine keeruline. Võite leida APK-sid internetist, kuid ma ei soovita neid alla laadida, kui te pole allika suhtes kindel.

Kuna Samourai Wallet lehte ei ole enam Google Play poes saadaval, ei ole võimalik automaatseid uuendusi keelata. Kui rakendus naaseb allalaadimisplatvormidele, oleks tark **keelata automaatsed uuendused**, kuni juhtumi arengu kohta on rohkem teavet.

Kui Samourai Wallet on juba teie nutitelefonis installitud, peaksite siiski suutma rakendusele juurde pääseda. Samourai rahakoti funktsionaalsuse kasutamiseks on oluline ühendada Dojo. Varem sõltusid isikliku Dojota kasutajad Samourai serveritest, et pääseda juurde Bitcoin'i plokiahela teabele ja edastada tehinguid. Nende serverite konfiskeerimisega ei saa rakendus enam neile andmetele juurde pääseda.
Kui teil polnud enne ühendatud Dojot, kuid nüüd on, saate selle seadistada, et kasutada oma Samourai rakendust uuesti. See hõlmab teie varukoopiate kontrollimist, rahakoti kustutamist (rahakoti, mitte rakenduse) ja rahakoti taastamist, ühendades oma Dojo rakendusega. Nende sammude kohta leiate rohkem üksikasju [sellest õpetusest, jaotises "_Valmistage ette oma Samourai Wallet_" : COINJOIN - DOJO](https://planb.network/en/tutorials/privacy/coinjoin-dojo).
Kui teie Samourai rakendus oli juba ühendatud oma Dojoga, siis rahakoti osa töötab teie jaoks täiuslikult. Saate endiselt näha oma saldo ja edastada tehinguid. Hoolimata kõigest, mis toimub, arvan ma, et Samourai Wallet jääb praegu parimaks mobiilse rahakoti tarkvaraks. Isiklikult plaanin seda jätkuvalt kasutada.
Peamine probleem, millega võite kokku puutuda, on Whirlpooli kontodele rakendusest juurdepääsu puudumine. Tavaliselt üritab Samourai luua ühenduse teie Whirlpool CLI-ga ja alustada coinjoin tsükleid enne, kui annab teile juurdepääsu nendele kontodele. Kuna see ühendus pole enam võimalik, jätkab rakendus lõputult otsingut, andmata kunagi juurdepääsu Whirlpooli kontodele. Sellisel juhul saate need kontod taastada teises rahakotitarkvaras, hoides alles ainult deposiidikonto Samourais.
### Millised tööriistad on Samourais endiselt saadaval?

Teisest küljest on mõned tööriistad kas serveri sulgemise tõttu mõjutatud või täielikult kättesaamatud.

Individuaalsete kulutamise tööriistade osas töötab kõik tavaliselt, eeldusel, et teil on oma Dojo. Tavalised Stonewall tehingud (ja mitte Stonewall x2) töötavad probleemideta.

Twitteri kommentaarides on rõhutatud, et Stonewall tehingu pakutav privaatsus võib nüüd olla vähendatud. Stonewall tehingu lisaväärtus seisneb selles, et selle struktuur on eristamatu Stonewall x2 tehingust. Kui analüütik kohtab seda konkreetset mustrit, ei saa ta kindlaks teha, kas tegemist on standardse Stonewalliga ühe kasutajaga või Stonewall x2-ga, kus osaleb kaks kasutajat. Siiski, nagu järgmistes lõikudes näeme, on Sorobani kättesaamatus tõttu Stonewall x2 tehingute sooritamine muutunud keerulisemaks. Seetõttu arvavad mõned, et analüütik võib nüüd eeldada, et iga sellise struktuuriga tehing on tavaline Stonewall. Isiklikult ei jaga ma seda eeldust. Kuigi Stonewall x2 tehingud võivad olla vähem sagedased (ja ma arvan, et need olid juba enne seda intsidenti), võib asjaolu, et need on endiselt võimalikud, tühistada terve analüüsi, mis põhineb eeldusel, et neid ei ole.
**[-> Lugege lisaks Stonewall tehingute kohta.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
Ricocheti osas ei ole ma suutnud kontrollida, kas teenus on endiselt töös, kuna mul ei ole Testnetis Dojot, ja ma eelistan mitte riskida `100 000 sats` kulutamisega rahakotile, mida võivad kontrollida võimud. Kui teil on olnud võimalus hiljuti seda tööriista testida, kutsun teid üles minuga ühendust võtma, et saaksime seda artiklit uuendada.

Kui vajate Ricocheti kasutamist, pidage meeles, et saate seda toimingut alati käsitsi teostada mis tahes rahakotitarkvaraga. Selleks, et õppida, kuidas erinevaid hüppeid korrektselt käsitsi sooritada, soovitan konsulteerida selle teise artikliga: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

JoinBot tööriist ei ole enam töökorras, kuna see sõltus täielikult rahakoti osalemisest, mida haldas Samourai.

Teiste koostöötehingute tüüpide osas, mida sageli nimetatakse "kaasosalisteks", on need endiselt võimalikud, kuid ainult käsitsi. Enne serveri sulgemist oli teil kaks võimalust Stonewall x2 või Stowaway (PayJoin) tehingute sooritamiseks:
- Kasutage Sorobani võrku, et automaatselt ja kaugelt vahetada PSBT-sid;
- Või sooritage need vahetused käsitsi, skaneerides mitmeid QR-koode.

Pärast mitmeid katseid selgub, et Soroban ei toimi enam. Nende koostöötehingute sooritamiseks tuleb andmevahetus seega teha käsitsi. Siin on kaks võimalust selle vahetuse sooritamiseks:
- Kui olete füüsiliselt oma kaasosalise lähedal, saate järjestikku skaneerida QR-koode;
- Kui te olete oma koostööpartnerist kaugel, saate PSBT-sid vahetada välise suhtluskanali kaudu rakendusest väljaspool. Olge siiski ettevaatlikud, kuna nendes PSBT-des sisalduvad andmed on privaatsuse seisukohast tundlikud. Soovitan kasutada krüpteeritud sõnumside teenust, et tagada vahetuse konfidentsiaalsus.
**[-> Uuri lähemalt Stonewall x2 tehingute kohta.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Uuri lähemalt Stowaway tehingute kohta.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

Mis puutub Whirlpooli, siis tundub, et protokoll ei toimi enam, isegi kasutajatele, kellel on oma Dojo. Olen viimastel päevadel jälgitud oma RoninDojo't ja proovinud mõningaid lihtsaid manipulatsioone, kuid Whirlpool CLI pole serveri sulgemisest saadik suutnud ühendust luua.

Siiski jään lootma, et see protokoll saab taasaktiveeritud või ehk teisiti ettekujutatud lähinädalatel, olenevalt olukorra arengust. See paus võib olla võimalus uurida uusi lähenemisviise või potentsiaalseid täiustusi selles süsteemis.
### Millised välistööriistad on endiselt saadaval?
Seoses teiste Samourai keskkonnaga seotud tööriistadega, mõned on endiselt saadaval, samas kui teised mitte.

Tasuta ahela analüüsi veebileht OXT.me ei ole kahjuks hetkel saadaval.

Whirlpool Stats Tool ei ole enam allalaadimiseks saadaval, kuna see oli majutatud Samourai GitLabis. Isegi kui olete selle Pythoni tööriista varem oma masinasse lokaalselt alla laadinud või kui see oli installitud teie RoninDojo sõlmele, ei tööta WST hetkel. Tõepoolest, selle töö sõltus andmetest, mida pakkus OXT.me, ja see sait ei ole enam kättesaadav. Praegu ei ole WST eriti kasulik, kuna Whirlpooli protokoll on mitteaktiivne.

KYCP.org sait ei ole hetkel enam kättesaadav.

GitLab, mis majutas Boltzmanni kalkulaatori Pythoni tööriista koodi, on samuti hõivatud. Praegusel hetkel ei ole seega võimalik seda tööriista alla laadida. Kuid kui teil on RoninDojo, saate Boltzmanni kalkulaatorit kasutada samamoodi nagu varem.

Mis puutub RoninDojosse, siis see sõlme-kastis tarkvara jätkab korrektselt toimimist hoolimata teatud spetsiifiliste tööriistade, nagu Whirlpool CLI ja WST, kättesaamatusest. Seda saab endiselt kasutada teiste rahakottide tarkvara jaoks tänu Fulcrumile või Electrsele. Kui soovite saada rohkem teavet RoninDojo kohta või teil on konkreetseid küsimusi, julgustan teid liituma [nende Telegrami grupiga](https://t.me/RoninDojoNode).

Siiski ei ole RoninDojo lähtekood hetkel enam kättesaadav, kuna see oli majutatud Samourai GitLabis. Seetõttu ei ole võimalik seda hetkel Raspberry Pi-le käsitsi installida.

Mis puutub vaatlusrakenduse tarkvarasse Sentinel, siis olukord on sarnane Samourai rakendusega. Kui teil on oma Dojo, saate Sentinelit probleemideta jätkuvalt kasutada. Kui teil aga Dojot ei ole, ei saa te enam ühendust luua. Erinevalt Samouraist on Sentinel veebileht siiski endiselt võrgus kättesaadav. Kuid olge selle saidi ja seal pakutava APK suhtes ettevaatlik, kuna pole selge, kes hetkel neid ressursse kontrollib.

### Kas Sparrow Wallet on mõjutatud?
Sparrow Wallet jätkab tavapärast tööd, välja arvatud Samourai tööriistad, mis ei ole enam saadaval. Praegu ei ole võimalik Sparrow' kaudu teostada coinjoine. Samuti ei ole enam kättesaadavad koostööl põhinevad kulutamise tööriistad, kuna Sparrow ei paku PSBT-de käsitsi vahetamise võimalust, erinevalt Samouraist. Kõigi teiste funktsioonide osas töötab Sparrow ilma probleemideta. Samuti võite seda tarkvara kasutada Samourai rahakoti taastamiseks, kui see on vajalik.

## Kuidas taastada Samourai rahakotti?
Nagu eelmistes jaotistes nägime, kui teil on oma Dojo, ei ole tingimata vajalik tarkvara vahetada. **Samourai jääb suurepäraseks valikuks kuumaks rahakotiks** igapäevaseks kulutamiseks. Kuid, kui teil ei ole Dojot või kui eelistate valida mõne teise tarkvara, selgitan ma täielikku taastamisprotsessi, tuues välja võimalikud takistused, millega võite kokku puutuda.

Igal juhul on oluline võtta aega ja veenduda, et ei teeks vigu. Pea meeles, et kiiret ei ole, kuna sa hoiad oma privaatvõtmeid ja Samourai serverite hõivamine ei mõjuta seda mingil viisil. Mis iganes juhtub, ilmselgelt ei saa nad teie privaatvõtmetele ligi pääseda.

### Kontrollige paroolilauset

Oma rahakoti taastamiseks peab teil olema teie paroolilause, isegi kui valite taastamise varundusfaili kaudu. Alustage paroolilause kehtivuse kontrollimisega. Avage oma Samourai Wallet rakendus, klõpsake vasakus ülanurgas oma Paynym ikoonil, seejärel valige `Settings`.

![samourai](assets/1.webp)

Järgmisena klõpsake `Troubleshooting` ja seejärel `Passphrase/backup test`.

![samourai](assets/2.webp)

Sisestage oma paroolilause ja klõpsake `Ok`. Kui see on õige, kinnitab Samourai seda. Teil on ka võimalus kontrollida varundusfaili, kui plaanite seda hiljem kasutada.

![samourai](assets/3.webp)

See samm on valikuline, kuid soovitatav. See kinnitab, et paroolilause on õige, kõrvaldades potentsiaalse probleemi allika hiljem. Kui Samourai näitab selles etapis, et paroolilause on vale, ei ole taastamine võimalik. Veenduge, et olete paroolilause õigesti sisestanud ja kontrollige seda uuesti.

### Valik 1: Taastage rahakott Sparrow's varundusfaili abil

Alates Sparrow Wallet'i versioonist 1.8.6 on võimalik otse importida teie Samourai rahakott, kasutades varundustekstifaili nimega `samourai.txt`, mille teie rakendus automaatselt genereerib. See fail sisaldab kõiki vajalikke andmeid teie rahakoti taastamiseks ja see on krüpteeritud teie paroolilausega turvalisuse tagamiseks.

Kui valite selle võimaluse, vajate teie ajakohast `samourai.txt` faili ja teie paroolilauset. Selle faili genereerimiseks Samourai Wallet'is klõpsake kolmel väikesel punktil üleval paremal, seejärel valige `Export wallet backup`.

![samourai](assets/4.webp)
Seejärel valige `Export to Clipboard`. Pärast seda peate faili turvaliselt oma arvutisse üle kandma. Kuna fail on krüpteeritud, kuid paroolilause üksi on piisav selle dekrüpteerimiseks, on oluline võtta ettevaatusabinõusid selle edastamisel. Kui valite otseülekande lihttekstina, peate looma oma arvutis `samourai.txt` faili ja kleepima lõikelaua sisu sinna. Alternatiivina võiksite otse telefoni salvestatud failidest `samourai.txt` faili kätte saada.
Kui teil on fail arvutis kättesaadav, avage Sparrow Wallet, klõpsake vahekaardil `File` ja valige `Import Wallet`, et alustada oma rahakoti importimist.

![samourai](assets/5.webp)
Kerige alla `Samourai Backup`, klõpsake `Import File` ja seejärel valige oma `samourai.txt` fail.
![samourai](assets/6.webp)

Seejärel küsib Sparrow teilt parooli faili dekrüpteerimiseks. See parool on tegelikult teie paroolilause. Sisestage see vastavasse välja ja klõpsake `Import`.

![samourai](assets/7.webp)

Kui selles etapis teie rahakott ei ilmu, on võimalik, et tegite vea `samourai.txt` faili kopeerimisel või paroolilause sisestamisel. Lisabi saamiseks võite konsulteerida tõrkeotsingu jaotisega.

![samourai](assets/8.webp)

Skripti tüübi osas, kui te pole Samourais teisi skripte seadistanud, peaksite tavaliselt kasutama ainult SegWit V0 (Native SegWit / P2WPKH). Hoidke see vaikimisi skript ja klõpsake `Import`.

![samourai](assets/9.webp)

Nimetage oma rahakott, näiteks "Samourai Recovery", ja seejärel klõpsake `Create Wallet`.

![samourai](assets/10.webp)

Seejärel küsib Sparrow teilt parooli valimist. See parool kaitseb ainult juurdepääsu teie rahakotile sellel arvutil ja ei puuduta teie rahakoti võtmete tuletamist. Valige kindlasti tugev parool, tehke märge selle meeldejätmiseks ja klõpsake `Set Password`.

![samourai](assets/11.webp)

Seejärel tuletatakse Sparrow'is teie rahakoti võtmed ja otsitakse vastavaid tehinguid.

![samourai](assets/12.webp)

Praegu on juurdepääsetav ainult teie deposiidikonto. Kui kasutasite Samouraid ainult selle konto jaoks, peaksite nägema kõiki oma vahendeid. Kui kasutasite aga ka Whirlpooli, peate tuletama `premix`, `postmix` ja `badbank` kontod. Sparrow'is klõpsake lihtsalt `Settings` vahekaardil, seejärel `Add Accounts...`.

![samourai](assets/13.webp)
Avanevas aknas valige rippmenüüst `Whirlpool Accounts`, seejärel klõpsake `OK`.
![samourai](assets/14.webp)

Seejärel näete oma erinevaid Whirlpooli kontosid ja Sparrow tuletatakse vajalikud võtmed seotud bitcoinide kasutamiseks.

![samourai](assets/15.webp)

Kui kasutate Samourai rahakoti taastamiseks Sparrow'ist erinevat tarkvara, nagu Electrum, siis siin on Whirlpooli konto indeksid käsitsi taastamiseks:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Nüüd on teil juurdepääs oma bitcoinidele Sparrow's. Kui vajate abi Sparrow Wallet'i kasutamisel, võite vaadata ka [meie pühendatud õpetust](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Soovitan samuti käsitsi importida sildid, mille olite seostanud oma UTXO-dega Samourais. See võimaldab teil hiljem Sparrow's tõhusat mündikontrolli teostada.

### Valik 2: Taastage rahakott Sparrow's mnemoonilise fraasi abil

Kui te ei soovi taastamist varundusfaili abil teostada, võite valida traditsioonilisema meetodi, kasutades lihtsalt oma 12-sõnalist taastefraasi ja paroolilauset. See teine ​​võimalus on sageli lihtsam.
Alustuseks veenduge, et teil on käepärast teie taastefraas ja parool. Seejärel avage Sparrow Wallet tarkvara, klõpsake vahekaardil `File` ja valige `Import Wallet`, et alustada rahakoti importimist.
![samourai](assets/16.webp)

Valige `Mnemonic Words (BIP39)` ja rippmenüüst klõpsake `Use 12 Words`.

![samourai](assets/17.webp)

Sisestage oma taastefraasi 12 sõna õiges järjekorras.

![samourai](assets/18.webp)

Kui Sparrow kuvab teate `Invalid Checksum`, tähendab see, et taastefraasi kontrollsumma ei kehti, mis tõenäoliselt tähendab, et tegite sõnade sisestamisel vea.

![samourai](assets/19.webp)

Kui teie fraas on õige, märkige ruut `Use Passphrase?` ja sisestage oma parool vastavasse välja. Lõpuks, kui kõik tundub korrektne, klõpsake nupul `Discover Wallet`.

![samourai](assets/20.webp)

Nimetage oma rahakott, näiteks "Samourai Recovery", seejärel klõpsake `Create Wallet`.

![samourai](assets/21.webp)
Seejärel palub Sparrow teil valida parooli. See parool kaitseb ainult juurdepääsu teie rahakotile sellel arvutil ja ei ole seotud teie rahakoti võtmete tuletamisega. Valige kindlasti tugev parool, kirjutage see üles, et seda meeles pidada, ja klõpsake `Set Password`.
![samourai](assets/22.webp)

Seejärel tuletatakse Sparrow'ga teie rahakoti võtmed ja otsitakse vastavaid tehinguid.

![samourai](assets/23.webp)

Kui selles etapis teie rahakott ei ilmu, on võimalik, et tegite parooli või taastefraasi sisestamisel vea. Lisabi saamiseks võite konsulteerida pühendatud tõrkeotsingu jaotisega.

Praegu on juurdepääsetav ainult teie deposiidikonto. Kui kasutasite Samourai'd ainult selle konto jaoks, peaksid kõik teie vahendid olema nähtavad. Kui kasutasite aga ka Whirlpooli, peate tuletama `premix`, `postmix` ja `badbank` kontod. Sparrow'is klõpsake lihtsalt vahekaardil `Settings`, seejärel `Add Accounts...`.

![samourai](assets/24.webp)

Avanevas aknas valige rippmenüüst `Whirlpool Accounts`, seejärel klõpsake `OK`.

![samourai](assets/25.webp)

Seejärel näete oma erinevaid Whirlpooli kontosid ja Sparrow tuletatakse vajalikud võtmed seotud bitcoinide kasutamiseks.

![samourai](assets/26.webp)

Kui kasutate oma Samourai rahakoti taastamiseks mõnda muud tarkvara nagu Electrum, siis siin on Whirlpooli konto indeksid käsitsi taastamiseks:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Nüüd on teil juurdepääs oma bitcoinidele Sparrow's. Kui vajate Sparrow Walleti kasutamisel abi, võite konsulteerida ka [meie pühendatud õpetusega](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Soovitan samuti käsitsi importida sildid, mille olite seostanud oma UTXO-dega Samourai's. See võimaldab teil Sparrow's hiljem tõhusat müntide kontrolli teostada.

### Millised on levinumad probleemid?
Pärast viimastel päevadel mitme inimese abistamist usun, et olen kohanud enamikku probleeme, mis võivad takistada teie rahakoti taastamist. Kui te ikka ei pääse oma rahakotile ligi vaatamata eelnevatele õpetustele, siis siin on mõned lisasoovitused. Esiteks ja kõige tähtsam, taastamise õnnestumiseks on absoluutselt hädavajalik, et taastefraas oleks õige. Kui te ei leia oma 12-sõnalist fraasi, võite kasutada *valikut 1*, et taastada Samourai varukoopiast. Samuti võite oma taastefraasi Samourai Rahakotis otse kätte saada, navigeerides `Seaded` > `Rahakott` ja lõpuks valides `Näita 12-sõnalist taastefraasi`.

Järgmisena, trükivea tegemine oma paroolilauses taastamise ajal toob kaasa valesti tuletatud võtmed, mis takistavad teie rahakoti taastamist Sparrow's. **Paroolilause peab olema täiesti täpne!**

Selle lahendamiseks soovitan esmalt kontrollida oma paroolilause kehtivust Samourai rakenduses, nagu on kirjeldatud artikli "_Kontrolli paroolilauset_" jaotises:
1. **Kontroll Samourais:** Kui Samourai kinnitab, et paroolilause on õige, proovige taastamist algusest peale, veendudes, et sisestate paroolilause Sparrow'sse ilma veata;
2. **Paroolilause Viga:** Kui Samourai näitab, et paroolilause on vale, on mõttetu jätkata katseid Sparrow's. Niikaua kui õiget paroolilauset ei leita, on teie rahakoti taastamine võimatu. Kui olete oma paroolilause jäädavalt kaotanud, hoidke oma Samourai rakendust turvaliselt. Kõik, mida teha saate, on loota, et serverid taaskäivitatakse, nii et saate teha kulutusi otse rakendusest ilma taastamise vajaduseta. **Ärge ühendage sel juhul Dojot**, kuna see tähendaks teie rahakoti lähtestamist Samourais, mis nõuab paroolilausele juurdepääsu.

Teiste kohatud vigade seas on paljud seotud võrgu konfiguratsiooniga Sparrow's.

Esiteks, veenduge, et Sparrow on õigesti seadistatud `mainnet` režiimis, mitte `testnet` režiimis. Tõepoolest, kui Sparrow otsib teie tehinguid Testnetis, ei leia ta midagi, sest teie rahakott on Mainnetis. Testnet on Bitcoin'i alternatiivne versioon, mida kasutatakse ainult testimiseks ja arendamiseks ning mis töötab eraldi võrgus peavõrgust (Mainnet), omades oma plokke ja tehinguid. Selleks, et kontrollida, millises võrgus te olete, klõpsake vahekaardil `Tööriistad`, seejärel `Taaskäivita kui`. Kui kuvatakse `Mainnet` valik, siis te ei ole peavõrgus. Valige see, et taaskäivitada Sparrow Mainnetis ja seejärel alustage oma taastamisprotsessi uuesti.

![samourai](assets/27.webp)
Mõned on kohanud ka raskusi Sparrow ühendamisel oma sõlmega. Sparrow paremas alanurgas olev värviline lüliti näitab, kas teie tarkvara on õigesti ühendatud Bitcoin'i sõlmega. Teie Samourai tehingute taastamiseks on hädavajalik, et tarkvara oleks hästi ühendatud. Kontrollige, kas lüliti on aktiveeritud, nagu minu allpool olevas pildis (kollane avaliku sõlme jaoks, roheline Bitcoin Core'i jaoks ja sinine Electrum serveri jaoks).
![samourai](assets/28.webp)

Kui lüliti pole aktiveeritud, klõpsake sellel, et ühendus uuesti aktiveerida.

![samourai](assets/29.webp)

Kui probleem püsib, siis siin on mõned võimalikud lahendused:
- Kui proovite ühenduda oma enda Electrum serveriga (sinine) või oma Bitcoin Core'iga (roheline) ja Sparrow ei saa ühendust, kontrollige ühenduse teavet alates `Fail > Eelistused... > Server`;

![samourai](assets/30.webp)
- Kui ühendusprobleem püsib, võib see olla tingitud teie sõlme mittetäielikust sünkroniseerimisest. Veenduge, et teie sõlm ja indekseerija oleksid 100% sünkroniseeritud. Kui vajalik, viimase abinõuna, katkestage ühendus oma sõlmega Sparrow'st ja ühendage avaliku sõlmega; - Kui olite juba ühendatud avaliku sõlmega ja ühendus ebaõnnestub, proovige sõlme vahetada, valides teise nimekirjast.

![samourai](assets/31.webp)

Kui olete oma rahakoti edukalt taastanud, kuid see tundub puudulik, võib probleem olla seotud tuletamisega.

Probleem võib tekkida, kui kasutasite oma Samourai deposiidikontot erineva skripti tüübiga kui `P2WPKH`. Vaikimisi kasutab Samourai seda skripti tüüpi, kuid kui olete seda käsitsi muutnud, peate seda ka Sparrow's taastamisel kohandama.

Teiste skripti tüüpide harude tuletamiseks peate kordama taastamisprotsessi iga kasutatud skripti tüübi jaoks. Selleks minge Sparrow's `File > New Wallet`, valige rippmenüüst teine skripti tüüp, klõpsake `New or Imported Software Wallet` ja järgige samu samme nagu algõpetuses.

![samourai](assets/32.webp)

Teine tuletamisprobleem, millega olen kokku puutunud, on seotud Gap Limit väärtusega. See väärtus ütleb Sparrow'le, pärast mitut tühja aadressi peaks see lõpetama uute aadresside tuletamise. Kui pärast taastamist märkate, et mõned tehingud on puudu, võib see olla liiga madala Gap Limiti tõttu. Selle lahendamiseks minge probleemi põhjustavale kontole, näiteks postmix kontole (kui mitu kontot on mõjutatud, korrake seda toimingut igaühe jaoks).

![samourai](assets/33.webp)

Klõpsake vahekaardil `Settings` ja seejärel nupul `Advanced...`.
![samourai](assets/34.webp)
Suurendage järk-järgult Gap Limiti väärtust, näiteks siin ma seadsin selle `400` peale. Seejärel klõpsake nupul `Close`.

![samourai](assets/35.webp)

Klõpsake `Apply`, et lõpetada. Sparrow tuletaks seejärel suurema hulga aadresse ja otsiks nendelt vahendeid, mis peaks aitama taastada kõik teie tehingud.

![samourai](assets/36.webp)

See katab erinevad taastamisprobleemid, millega olen viimastel päevadel kokku puutunud. Kui pärast kõigi nende lahenduste proovimist on teil endiselt probleeme, kutsun teid liituma [Discover Bitcoin Discordiga](https://discord.gg/xKKm29XGBb), et küsida abi. Ma külastan seda Discordi regulaarselt ja oleksin rõõmus aidata, kui mul on lahendus. Teised bitcoinikasutajad saavad samuti jagada oma kogemusi ja pakkuda abi. **Igal juhul on oluline hoida oma taastefraas, varukoopiadokument ja parool saladuses**. Ärge jagage neid kellegagi, kuna see võib võimaldada neil varastada teie bitcoine.

Kui taastamine on lõpetatud, on teil nüüd juurdepääs oma bitcoinidele. See on hea asi, kuid see ei pruugi olla piisav. Tõepoolest, serverite konfiskeerimine toob kaasa uued potentsiaalsed riskid teie privaatsusele. Järgmises jaotises uurime neid riske üksikasjalikult ja kirjeldame ettevaatusabinõusid, mida tuleks võtta oma privaatsuse kaitsmiseks.

## Mis on tagajärjed teie tehingute privaatsusele?

### Samourai kasutajana ilma Dojota

Kui kasutasite Samourai rahakotti ilma oma Dojot ühendamata, pidid teie xpubid olema edastatud Samourai serveritele, et rakendus toimiks. Nende serverite konfiskeerimisega on võimalik, et võimudel on nüüd juurdepääs nendele xpubidele.
See stsenaarium jääb hüpoteetiliseks. Me ei tea, kas need xpub-id olid salvestatud, kas võimalik salvestuskoht hävitati, kas võimud on need taastanud ja kas nad kavatsevad neid kasutada ahelanalüüsiks. Siiski, sellises olukorras on mõistlik arvestada halvima stsenaariumiga, kus võimudel on kasutajate xpub-id, kes ei ühendanud omaenda Dojot. Viiteks, xpub on tähemärkide jada, mis sisaldab kõiki vajalikke elemente laste avalike võtmete genereerimiseks (avalik võti + ahelakood). Seda kasutatakse hierarhilistes deterministlikes rahakottides vastuvõtvate aadresside genereerimiseks ja konto tehingute jälgimiseks ilma seotud privaatvõtmeid paljastamata. See võimaldab näiteks luua "ainult-vaatamise" rahakoti. Siiski, xpub-ide avalikustamine võib ohustada kasutaja privaatsust, kuna need võimaldavad kolmandatel osapooltel jälgida tehinguid ja näha seotud kontode jääke.
Igaüks, kes teab teie xpub-e, võib seega näha kõiki teie rahakoti vastuvõtvaadresse, neid, mida on minevikus kasutatud, ja neid, mis luuakse tulevikus.

Kasutajatele, kellel ei ole Dojot, on teie xpub-ide võimalikul lekkimisel kaks peamist tagajärge:
- Teie poolt võib-olla teostatud coinjoinid muutuvad privaatsuse seisukohast ebaefektiivseks igaühe jaoks, kes teab teie xpub-e, seega teie mündid kaotavad kogu anonüümsuse;
- See isik saab samuti jälgida kõiki teie Samourai rahakoti vastuvõtvaadresse.

Seetõttu on oluline arvestada halvima stsenaariumiga ja loobuda sellest rahakotist, mis on potentsiaalselt kompromiteeritud privaatsuse osas. Selleks looge nullist uus rahakott teise tarkvaraga, nagu Sparrow Wallet. Pärast oma varukoopiate kehtivuse kontrollimist kandke kõik oma vahendid üle, tehes tehinguid. Kuigi see toiming ei katkesta teie müntide jälgitavuse linki, takistab see võimudel teie uue rahakoti aadresse kindlalt teadmast.

Selle ülekandetoimingu ajal soovitan vältida oma müntide konsolideerimist. Kui me eeldame, et teie xpub-id on kompromiteeritud, ei oma konsolideerimine isiku vaatepunktist, kellel on juurdepääs nendele xpub-idele, mingit mõju, kuna teie privaatsus on nendega juba kompromiteeritud. Siiski, soovitan teil mitte liiga palju oma münte konsolideerida peamiselt teiste inimeste eest privaatsuse kaitsmiseks. Halvimal juhul võivad ainult võimud omada juurdepääsu teie xpub-idele, kuid ülejäänud maailm ei tea neist. Seega, teiste vaatepunktist võib teie müntide konsolideerimine teie privaatsust oluliselt kahjustada Common Input Ownership Heuristic (CIOH) tõttu.

Lõpuks, et jälgimist lõplikult katkestada, kaaluge ka coinjoinide tegemist sellest uuest rahakotist.
**Hoiatus:** Lihtsalt oma Samourai rahakoti taastamine Sparrow Walletis ei ole piisav. On vajalik luua täiesti uus rahakott uue taastefraasiga, kui soovite vältida võimalikult lekkinud xpub-ide kasutamist. Kui impordite oma olemasoleva seemne Sparrow'sse, vahetate ainult rahakoti haldustarkvara, kuid rahakott jääb samaks.

### Sparrow või Samourai kasutajana koos Dojoga

Kui teie rahakotti hallatakse ainult Sparrow Walletis, ei oleks teie xpub-id saanud lekkida, olgu te kasutate avalikku sõlme või omaenda Bitcoin sõlme. Samamoodi, kui kasutate Samourai rakendust ja olete alati ühendanud selle rakenduse omaenda Dojoga alates rahakoti loomisest, on teie xpub-id samuti turvalised.
Siiski, kui olete kasutanud sama rahakotti perioodil **ilma omaenda Dojota** ja seejärel oma Dojoga, on võimalik, et Samourai serveritel võis olla juurdepääs teie xpubidele ja seetõttu võivad võimud neid teada. Kui olete selles konkreetses olukorras, soovitan teil järgida eelmise jaotise soovitusi ja pidada oma xpubid kompromiteerituks.
Neile, kes on alati kasutanud Sparrow'd või Samouraid oma Dojoga, on peamine risk see, et teie müntide anonüümsete komplektide suurus võib potentsiaalselt väheneda. Oletame, halvimal juhul, et kõik Dojota kasutajad on andnud oma xpubid võimude kätte, siis võiksid need võimud jälgida nende müntide teekonda läbi coinjoin tsüklite.

Selle illustreerimiseks võtame konkreetse näite. Kujutage ette, et osalesite esimeses coinjoin tsüklis, millele järgnes kaks täiendavat allavoolu coinjoin tsüklit. Kui Dojota kasutajate xpubid ei ole lekkinud, siis oleks teie mündi eeldatav anonüümsete komplektide suurus 13.

![samourai](assets/37.webp)

Siiski, kui me eeldame, et xpubid on lekkinud ja et kohtasite algse coinjoini ajal ühte Dojota kasutajat ja seejärel kahte esimese allavoolu coinjoini ajal, siis oleks teie eeldatav anonüümsete komplektide suurus võimude vaatepunktist ainult 10 asemel 13.

![samourai](assets/38.webp)
Selle potentsiaalse anonüümsete komplektide suuruse vähenemise kvantifitseerimine on keeruline, kuna see sõltub paljudest teguritest ja iga münt on erinevalt mõjutatud. Näiteks Dojota kasutaja, keda kohati varajastes tsüklites, mõjutab eeldatavat anonüümsete komplektide suurust palju rohkem kui hilisemates tsüklites kohatud kasutaja. Et anda teile ettekujutus olukorrast, mis jääb hüpoteetiliseks, näitasid Samourai viimased statistikad, et 85% kuni 90% coinjoinides osalenud müntidest pärines kasutajatelt, kellel oli Dojo, Sparrow või Bitcoin Keeper, st kasutajatelt, kes isegi halvimal juhul ei oleks näinud oma xpubide lekkimist.
Kuigi neid numbreid on raske kontrollida, tunduvad need mulle kahest põhjusest konsistentsetena:
- Sparrow Wallet on laialdaselt kasutusel;
- Enamik node-in-box tarkvarast pakub Dojo rakendusi ja need peavoolu tarkvarad nagu Umbrel on tänapäeval väga populaarsed.

Seega tuleb arvestada mitme aspektiga. Kui teie müntide privaatsus võimude ees on teile äärmiselt oluline, oleks mõistlik valmistuda halvimaks stsenaariumiks ja on raske garanteerida 100%, et teie Whirlpool coinjoin tsüklid ei oleks jälgitavad potentsiaalse xpubide lekke tõttu Dojota kasutajatelt. Kuigi see eeldus on väga ebatõenäoline, ei ole see võimatu.

Teisest küljest, kui teie müntide privaatsus võimude ees, kes võivad neid xpubisid omada, ei ole teie jaoks kriitiline, siis võib olukorda vaadata teisiti.

Ma täpsustan "võimude ees", sest on oluline meeles pidada, et ainult võimud, kes serverid hõivasid, on potentsiaalselt teadlikud neist xpubidest. Kui teie eesmärk coinjoini kasutamisel oli takistada teie pagaril teie vahendite jälgimist, siis ta ei ole paremini informeeritud kui enne serveri hõivamist.
Lõpetuseks on oluline arvestada oma mündi algset anonüümsuskomplekti (anonset) enne serveri hõivamist. Võtame näiteks mündi, mis oli saavutanud potentsiaalse anonseti 40 000; selle anonseti võimalik vähenemine on tõenäoliselt tühine. Tõepoolest, juba väga kõrge baasanonseti korral on ebatõenäoline, et mõne Dojota kasutaja olemasolu võiks olukorda radikaalselt muuta. Siiski, kui teie mündil oli anonset 40, siis võib see potentsiaalne leke teie anonsete olukorda tõsiselt mõjutada ja potentsiaalselt võimaldada jälgimist. Pärast OXT.me sulgemist WST tööriista enam kasutada ei saa, saate neid anonsete ainult hinnata. Retrospektiivse anonseti puhul pole liiga palju muretseda, kuna Whirlpooli mudel tagab, et see on esimesest coinjoinist alates väga kõrge, tänu teie eakaaslaste pärandile. Ainus juhtum, kus see võib probleemi tekitada, on siis, kui teie münti pole mitu aastat remixitud ja see segati basseini käivitamise alguses. Tuleviku anonseti osas saate uurida, kui kaua teie münt on olnud saadaval coinjoinide jaoks. Kui see on olnud mitu kuud, siis on sellel tõenäoliselt äärmiselt kõrge tuleviku anonset. Vastupidisel juhul, kui see lisati basseini vaid mõni tund enne serverite hõivamist, siis on selle tuleviku anonset tõenäoliselt väga madal.
[**-> Lugege lisaks anonsetide ja nende arvutusmeetodi kohta.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Teine aspekt, mida kaaluda, on konsolideerimiste mõju segatud müntide anonsetidele. Kuna Whirlpooli kontodele ei pääse enam ligi Samourai rakenduse kaudu, on tõenäoline, et paljud kasutajad on oma rahakoti teise tarkvarasse üle kandnud ja üritanud oma vahendeid Whirlpoolist välja võtta. Eriti eelmisel nädalavahetusel, kui Bitcoin võrgu tehingutasud olid suhteliselt kõrged, oli tugev tehniline ja majanduslik stiimul post-mix müntide konsolideerimiseks. See tähendab, et tõenäoliselt on paljud kasutajad teinud olulisi konsolideerimisi.

Probleem nende post-mix konsolideerimistega on see, et need alati vähendavad anonsete, mitte ainult kasutaja jaoks, kes neid teostab, vaid ka kasutajate jaoks, kellega nad oma coinjoin tsüklites kohtusid. Kuigi ma ei ole suutnud seda nähtust täpselt kontrollida ega kvantifitseerida, võivad sel ajal tehingutasudega seotud majanduslikud stiimulid meid eeldada, et anonsetid on potentsiaalselt madalamad.

### Kui olete Sentinel kasutaja

Watch-only rahakoti rakenduse Sentinel võrgutegevus on sarnane Samourai omaga. Oma rahakoti infole juurdepääsuks peab rakendus edastama teie poolt antud xpubid, avalikud võtmed ja aadressid Dojole. Kui olete alati kasutanud oma Dojot Sentinelis, siis probleemi pole ja võite rakendust muretult edasi kasutada. Kui aga olite sõltuv Samourai serveritest oma Sentineli jaoks, on võimalik, et teie xpubid on paljastatud. Sel juhul on soovitatav järgida sama rahakoti vahetamise protsessi, mida soovitatakse Samourai Walleti puhul, kui see on ühendatud Samourai serveritega.

Ebatõenäolisel juhul, kui kasutasite oma Dojot Samouraiga, kuid mitte Sentineliga, oleks targem eeldada, et teie xpubid on kompromiteeritud.

## Järeldus
Tänan, et lugesite seda artiklit lõpuni. Kui arvate, et informatsiooni on puudu või kui teil on ettepanekuid, palun ärge kõhelge minuga ühendust võtta, et jagada oma mõtteid. Lisaks, kui vajate edasist abi oma Samourai Wallet'i taastamisel hoolimata sellest juhendist, kutsun teid liituma [Discover Bitcoin Discordiga](https://discord.gg/xKKm29XGBb), et küsida abi. Külastan seda Discordi regulaarselt ja oleksin rõõmus teid aidata, kui mul on lahendus. Teised bitcoinikasutajad saavad samuti jagada oma kogemusi ja pakkuda oma tuge. **Igal juhul on oluline hoida oma taastefraasi, varukoopiat ja paroolilauset konfidentsiaalsena**. Ärge jagage neid kellegagi, kuna see võib võimaldada neil teie bitcoine varastada.