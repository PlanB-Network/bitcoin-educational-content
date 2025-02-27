---
name: Bitfinex - ettevõte
description: Ettevõtte konto loomine ja haldamine Bitfinexis
---
![cover](assets/cover.webp)

2012. aastal asutatud Bitfinex on üks esimesi bitcoinide ja altcoinide vahetusplatvorme. Algselt keskenduti P2P-bitcoinide vahetamisele, kuid platvorm laiendas kiiresti oma teenuseid, et hõlmata marginaalkaubandust, P2P-rahastamist, tuletisinstrumentidega kauplemist ja börsivälist turgu ("*over-the-counter*") suure mahuga tehingute jaoks.

Täna on Bitfinex täielik platvorm, mis võimaldab nii bitcoinide lihtsat ostmist kui ka täiustatud kauplemisfunktsioonide kasutamist (traditsiooniline kauplemine, tuletisinstrumendid, börsiväline kauplemine, laenamine jne) koos riskijuhtimisvahenditega. See on saadaval veebiversioonina ja lihtsate tehingute jaoks on saadaval ka hõlpsasti kasutatav mobiilirakendus.

Selles õpetuses käsitleme Bitfinexis ärikonto loomise protsessi, bitcoinide ostmist ja müümist, tehingute haldamist raamatupidamise eesmärgil ning eurode ja bitcoinide hoiustamist ja väljavõtmist. Eesmärk on anda teile põhiteadmised, olenemata sellest, kas plaanite bitcoini oma rahavoogudesse integreerida või bitcoini maksevahendina vastu võtta.

Kui olete huvitatud bitcoini integreerimisest oma ettevõttesse, siis soovitan ka meie täielikku teoreetilist koolituskursust sel teemal:

https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a
## 1 - Bitfinexi konto loomine

Mine [ametlikule Bitfinexi veebisaidile](https://www.bitfinex.com/). Leidke kodulehelt ja klõpsake "*Sign Up*", et alustada konto loomist. Kõigepealt loote standardkonto nagu eraisikutele, "*Corporate*" valik valitakse hiljem kinnitamisprotsessi käigus.

![BITFINEX](assets/fr/01.webp)

Täitke nõutavad andmed: sisestage oma ettevõtte e-posti aadress ja teie ettevõtte asukohariik. Valige turvaline kasutajanimi ja salasõna, seejärel klõpsake registreerimise kinnitamiseks nupule "*Sign up*".

![BITFINEX](assets/fr/02.webp)

Näpunäiteid tugevate ja unikaalsete paroolide kasutamise ja kaitsmise kohta leiate ka sellest juhendmaterjalist :

https://planb.network/tutorials/others/general/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9
Nüüd konfigureerime 2FA, et kaitsta kontot. Kasutage oma nutitelefonis autentimisrakendust, näiteks Google Authenticator või Authy. Selle tööriista õpetuse leiad siit :

https://planb.network/tutorials/others/general/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7
Skaneeri QR-kood oma rakendusega ja sisesta 6 ettenähtud numbrit.

![BITFINEX](assets/fr/03.webp)

Registreerimine on lõpetatud.

![BITFINEX](assets/fr/04.webp)

Kontrollige oma postkasti ja klõpsake Bitfinexi saadetud lingile, et kinnitada oma registreerimist.

![BITFINEX](assets/fr/05.webp)

Teie konto on nüüd loodud. Vajutage platvormile juurdepääsuks nupule "*Logi sisse*".

![BITFINEX](assets/fr/06.webp)

## 2 - Ettevõtte konto kontrollimine

Bitfinex rakendab kehtivatele eeskirjadele vastavat kontrolliprotsessi (KYC). "Basic" režiimis on võimatu teha hoiuseid, mistõttu on oluline saada vähemalt "Intermediate" või vajadusel isegi "Full" verifikatsioonitase.

Kui teie konto on loodud, peaks hüpikaknas ilmuma soovitus, et te kinnitaksite oma konto. Klõpsake nupule "*Verify*".

![BITFINEX](assets/fr/07.webp)

Kui see aken ei ilmu, minge oma profiili ülevalt paremale, seejärel klõpsake "*Verification*".

![BITFINEX](assets/fr/08.webp)

Valige "*Konto tüüp*" all "*Corporate*". Minu puhul uuendan ma "*Keskmise*", seega valin "*Upgrade to Intermediate*".

![BITFINEX](assets/fr/09.webp)

Täitke sammud, andes :


- Ettevõtte andmed (ettevõtte nimi, kontaktandmed, tegevusvaldkond jne) ;
- Juriidilised dokumendid (põhikiri, Kbis väljavõte, juhatuse liikmete ja aktsionäride nimekiri);
- KYC-teave iga tegeliku tulusaaja või juhi kohta (isikut tõendavad dokumendid, aadressi tõendamine jne).

Kui teie taotlus on täidetud ja esitatud, võib platvormil kuluda mitu päeva, enne kui see kinnitatakse ettevõtte kinnitamiseks. Selle aja jooksul on hoiused ajutiselt blokeeritud.

![BITFINEX](assets/fr/10.webp)

## 3 - Bitfinexi liidese kiire tutvustus

Kui olete sisse loginud, näete kasutajaliidese ülaosas navigatsiooniriba, millel on: "*Trading*", "*Derivatiivid*", "*Funding*", "*OTC*", "*P2P*", "*Wallet*" jne. Bitfinex pakub mitmesuguseid funktsioone, sealhulgas :


- Kauplemine**: "*klassiline*" turg, kus saab esitada tellimusi krüptovaluutade (sh bitcoin) ostmiseks ja müümiseks;
- OTC**: Over-The-Counter teenus, mis on mõeldud suurte mahtudega kauplemiseks otse teise mängijaga, väljaspool avalikke tellimusraamatuid;
- Rahastamine**: Laenude ja marginaalfinantseerimise valdkond;
- Tuletisinstrumendid**: Tuletisinstrumentide (futuurid jne) sektsioon, mis on mõeldud kogenud kauplejatele;
- P2P**: Võimaldab teil osta või müüa krüptosid teistelt kasutajatelt peer-to-peer põhimõttel.

Tavapäraseks kasutamiseks (bitcoinide ostmine/müümine, sissemaksed/väljavõtmised ja sularaha haldamine) kasutate peamiselt vahekaarti "*Trading*", samuti jaotisi "*Wallet*", "*Deposit*" ja "*Withdraw*".

![BITFINEX](assets/fr/11.webp)

Teine ettevõtte valemi eelis on võimalus luua allkontosid. See tähendab, et saate anda nendele allkontodele juurdepääsu mitmele kasutajale, kellel on konkreetsed õigused (ainult lugemiseks, kauplemiseks, ainult hoiustamiseks jne).

## 4 - eurode (fiat) hoiustamine ja väljavõtmine

Eurode hoiustamiseks oma Bitfinex Corporate kontole avage "*Deposit*" alammenüü, mis asub kasutajaliidese ülaosas asuvas menüüs "*Wallet*".

![BITFINEX](assets/fr/12.webp)

Valige "*Pangaülekanne*" või "*Krediit/ Deebetkaart*", et teha sissemakseid eurodes (või mõnes muus vääringus).

![BITFINEX](assets/fr/13.webp)

Valige saadetav fiat-valuuta, nt euro. Kui kasutate ainult põhifunktsioone "*Trading*", klõpsake "*Exchange*". Märkige ka summa, mida soovite hoiustada, ja oma ärikonto panga riik.

![BITFINEX](assets/fr/14.webp)

Tehke ülekanne oma ettevõtte pangakontolt Bitfinexi osutatud pangakontole.

Raha väljavõtmiseks on menetlus sarnane: minge allmenüüsse "*Väljavõtmine*".

![BITFINEX](assets/fr/15.webp)

Klõpsake nupule "*Pangaülekanne*".

![BITFINEX](assets/fr/16.webp)

Valige fiat-valuuta, mida soovite välja võtta, konto, mida soovite Bitfinexis debiteerida ("*Vahetus*", kui kasutate ainult põhifunktsioone), ja summa, mida soovite välja võtta.

![BITFINEX](assets/fr/17.webp)

Bitfinex võib nõuda teie pangakonto kinnitamist enne ülekande aktsepteerimist, et tagada vastavus nõuetele.

![BITFINEX](assets/fr/18.webp)

Kui protseduur on algatatud, kannab Bitfinex raha teie pangakontole.

## 5 - bitcoinide hoiustamine ja väljavõtmine

Bitcoini hoiustamiseks Bitfinexis avage alammenüü "*Deposit*".

![BITFINEX](assets/fr/19.webp)

Klõpsake nupule "*Krüptoraha*".

![BITFINEX](assets/fr/13.webp)

Valige "*BTC*". Ilmub vastuvõtuaadress. Kopeerige see aadress ja kasutage seda omaenda rahakotist või mõnelt teiselt platvormilt BTC saatmiseks.

![BITFINEX](assets/fr/20.webp)

Bitcoinide väljavõtmiseks minge alammenüüsse "*Väljavõtmine*".

![BITFINEX](assets/fr/21.webp)

Klõpsake nupule "*Krüptoraha*".

![BITFINEX](assets/fr/22.webp)

Valige "*BTC*". Valige Bitfinexi konto, millelt soovite raha välja võtta ("*Vahetus*" põhifunktsioonide puhul). Sisestage summa ja bitcoinide sihtaadress. Kontrollige kindlasti väljavõtteaadressi, et vältida vigu.

![BITFINEX](assets/fr/23.webp)

Pärast kinnitust kantakse teie bitcoinid üle. Pange tähele, et tasud ja viivitused võivad erineda sõltuvalt mempool'i ülekoormusest.

Bitfinex pakub ka Lightning Networki kaudu sisse- ja väljamaksevõimalusi, mis võimaldab kiiremaid ja odavamaid tehinguid.

![BITFINEX](assets/fr/24.webp)

Kui olete Lightning Networkist huvitatud, on meil ka täielik koolituskursus, mis aitab teil mõista, kuidas see toimib:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
## 6 - Bitcoinide ostmine ja müümine Bitfinexis

Bitfinex pakub erinevaid kauplemisrežiime. Kasutamise lihtsustamiseks valige klassikaline hetketurg, mida tuntakse ka kui "*Trading*" või "*Exchange*". Siin saate esitada ostu- või müügikorraldusi turuhinnaga või määrata piirhinna.

Klõpsake ülemises menüüs nupule "*Trading*".

![BITFINEX](assets/fr/25.webp)

Valige paar "*BTC/EUR*", kui soovite osta või müüa BTC-d näiteks eurode vastu.

![BITFINEX](assets/fr/26.webp)

Kasutajaliideses kuvatakse keskel hinnagraafik, allosas on tellimusraamat ja vasakul on tellimuste sisestamise moodul. Korralduse sisestamise sektsioonis saate valida "*Market*" korralduse (täidetakse kohe parima võimaliku hinnaga) või "*Limit*" korralduse (määrate hinna ise) vahel. Märkige ostetava või müüdava BTC kogus või valige protsent oma saldost. Seejärel klõpsake ostmiseks "*Buy*" või müügiks "*Sell*".

![BITFINEX](assets/fr/27.webp)

Kasutajaliidese alumises osas saate vaadata oma täidetud korralduste ajalugu.

![BITFINEX](assets/fr/28.webp)

## 7 - Tehinguajaloo eksport ja raamatupidamine

Raamatupidamise eesmärgil peate eksportima oma tehingute (ostud, müük, sissemaksed, väljamaksed) üksikasjad. Bitfinex pakub põhjalikku aruandlusvahendit. Klõpsake oma profiili ikoonil kasutajaliidese paremas ülaosas ja seejärel menüüs "*Raportid*".

![BITFINEX](assets/fr/29.webp)

Vasakul saate valida eksporditavate andmete tüübi. Näiteks valides "*Trades*" saate juurdepääsu kõikidele oma tehingutele.

![BITFINEX](assets/fr/30.webp)

Määrake soovitud ajavahemik lahtris "*Date*" ja vajaduse korral piirake otsingut ühe või mitme konkreetse paariga väljal "*Symbol*".

![BITFINEX](assets/fr/31.webp)

Andmete eksportimiseks klõpsake nupule "*Eksport*".

![BITFINEX](assets/fr/32.webp)

Kontrollige parameetrid ja kinnitage eksport.

![BITFINEX](assets/fr/33.webp)

Aruanne saadetakse CSV-failina teie Bitfinexi kontoga seotud aadressile.

![BITFINEX](assets/fr/34.webp)

Kui fail on eksporditud, saate selle integreerida oma raamatupidamistarkvarasse või saata selle oma vannutatud raamatupidajale.

## 9 - Ettevõtte kasutusjuhtumid

Sõltuvalt teie ettevõtte eesmärkidest ja struktuurist võib Bitfinexi kasutamine olla erinev.

### Bitcoinide ostmine sularaha eest

**eesmärk:** Mitmekesistada ettevõtte rahavooge, investeerides bitcoinidesse.

**Sammud, mida tuleb järgida:**


- Hoiustage eurosid Bitfinexile ettevõtte pangakontolt;
- Kasutage neid eurosid bitcoini ostmiseks;
- Hoidke bitcoine platvormil või võtke need välja, et kindlustada need ise;
- Eksportida tehingulugu vastavalt vajadusele.

### Bitcoini aktsepteerimine maksevahendina

**eesmärk:** Pakkuda oma ettevõttele võimalust võtta bitcoin'i kui maksevahendit oma toodete või teenuste eest.

**Sammud, mida tuleb järgida:**


- Integreerige Bitcoini maksesüsteem. Väikeettevõtete jaoks võib piisata lihtsast rahakoti tarkvarast või võite valida spetsiaalsed lahendused nagu Swiss Bitcoin Pay või BTCPay Server, et integreerida bitcoin maksevahendina oma veebisaidil või müügikohas;
- Kandke bitcoinides saadud maksed oma Bitfinexi kontole;
- Sõltuvalt teie finantsstrateegiast, müüge saadud bitcoinid eurode eest, hoidke neid võimaliku tulevase väärtuse tõusu jaoks või valige mõlema kombinatsioon;
- Hoidke bitcoine platvormil või võtke need välja enda hoiustamiseks. Võite ka eurosid oma pangakontole välja võtta;
- Eksportida tehingulugu vastavalt vajadusele.

Sest põhjalikumalt vaadelda seda teemat, Soovitan seda põhjalikku koolituse integreerimise Bitcoin arvesse ettevõtete, mis hõlmab üksikasjalikult lisades rahavoogude, vastuvõtva Bitcoin maksete, ja raamatupidamine :

https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a