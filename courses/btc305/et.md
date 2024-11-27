---
name: Bitcoin ja BTCPay Server
goal: Paigalda oma ettevõttele BTCPay Server
objectives:
  - Mõista, mis on btcpayserver.
  - Paigalda ja seadista ise BTCPay Server.
  - Kasuta btcpayserverit oma igapäevases äritegevuses.
---

# Bitcoin ja BTCPay Server

See on sissejuhatav kursus BTCPay Serveri operaatoritele, mille on kirjutanud Alekos ja Bas ning mis on kohandatud Plan ₿ kursuse formaati melontwisti ja asi0 poolt.

POOLELI OLEV LUGU

"See on vale, minu usaldus teie vastu on murtud, ma teen teid iganenuks."

Tootnud BTCPay Serveri Sihtasutus

+++

# Sissejuhatus

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Kriitiline tunnustus autori Bitcoinile ja BTCPay Serverile

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Alustame sellest, mis on BTCPay Server ja kust see pärineb. Me väärtustame läbipaistvust ja teatud standardeid, et kujundada usaldust Bitcoini ruumis.
Üks projekt selles valdkonnas murdis neid väärtusi. BTCPay Serveri peaarhitekt, Nicolas Dorier, võttis seda isiklikult ja lubas neid iganenuks muuta. Siin me oleme aastaid hiljem ja töötame selle tuleviku nimel, täielikult avatud lähtekoodiga, iga päev.

> See on vale, minu usaldus teie vastu on murtud, ma teen teid iganenuks.
> Nicolas Dorier

Pärast Nicolase öeldud sõnu oli aeg hakata ehitama. Palju tööd läks sellesse, mida me nüüd nimetame BTCPay Serveriks. Rohkem inimesi tahtis sellele tõukele kaasa aidata. Kõige äratuntavamad on r0ckstardev, MrKukks, Pavlenex ja esimene kaupmees, kes tarkvara kasutas, astupidmoose.

Mida tähendab avatud lähtekood ja mis käib sellise projekti juurde?

FOSS tähistab vaba ja avatud lähtekoodiga tarkvara. Esimene viitab tingimustele, mis lubavad kellelgi tarkvara kopeerida, muuta ja isegi levitada versioone (isegi kasumit teenides). Viimane viitab lähtekoodi avalikule jagamisele, julgustades avalikkust kaasa aitama ja seda parandama.
See toob kaasa kogenud kasutajad, kes on entusiastlikud kaasa aitama tarkvarale, mida nad juba kasutavad ja millest väärtust saavad, tõestades aja jooksul, et see võidab omaksvõtu osas litsentsitud tarkvara üle. See on kooskõlas Bitcoini eetosega, et "informatsioon igatseb olla vaba". See toob kokku kirglikud inimesed, kes moodustavad kogukonna ja on lihtsalt lõbusam. Nagu Bitcoin, on FOSS paratamatu.

### Enne kui alustame

See kursus koosneb mitmest osast. Paljude eest hoolitseb teie klassiruumi õpetaja, juurdepääsuga demo keskkondadele, teile hostitud server ja võimalik, et domeeninimi. Kui läbite selle kursuse iseseisvalt, olge teadlikud, et DEMO-ga märgistatud keskkonnad ei pruugi teile kättesaadavad olla.
NB. Kui järgite seda kursust klassiruumis, võivad serverinimed erineda sõltuvalt teie klassiruumi seadistusest. Serverinimedes võivad olla erinevused selle tõttu.

### Kursuse struktuur

Igal peatükil on eesmärgid ja teadmiste hindamised. Selles kursuses käsitleme igaüht neist ja igal õppetüki blokil (st peatükil) on kokkuvõte võtmefunktsioonidest. Illustratsioonid on esitatud visuaalse tagasiside andmiseks ja peamiste kontseptsioonide visuaalseks tugevdamiseks. Eesmärgid on iga õppetüki bloki alguses paika pandud. Need eesmärgid lähevad kaugemale kontrollnimekirjast. Need annavad teile juhendi uue oskuste komplekti juurde. Teadmiste hindamised muutuvad järk-järgult keerukamaks teie BTCPay Serveri seadistamisel.

### Mida õpilased kursusega saavad?

BTCPay Serveri kursusega saab õpilane mõista Bitcoin'i põhiprintsiipe, nii tehnilisi kui ka mitte-tehnilisi. Põhjalik koolitus Bitcoin'i kasutamise kohta läbi BTCPay Serveri võimaldab õpilastel hallata oma Bitcoin'i infrastruktuuri.

### Olulised veebiaadressid või kontaktivõimalused

BTCPay Serveri Sihtasutus, mis võimaldas Alekosel ja Bas'il selle kursuse kirjutada, asub Tokyo's, Jaapanis. BTCPay Serveri sihtasutusega saab ühendust võtta järgneval veebilehel;

- https://foundation.btcpayserver.org
- liitu ametlike vestluskanalitega: https://chat.btcpayserver.org

## Sissejuhatus Bitcoin'i

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Bitcoin'i mõistmine klassiruumi harjutuse kaudu

See on klassiruumi harjutus, nii et kui võtate seda kursust ise, ei saa te seda harjutust teha, kuid võite siiski sellest harjutusest läbi minna. Selle ülesande täitmiseks on vajalik inimeste arv vahemikus 9 kuni 11.

Harjutus algab pärast BBC tutvustuse "Kuidas Bitcoin ja plokiahel töötavad" vaatamist.

![how bitcoin and the blockchain works](https://youtu.be/mhE_vvwAiRc)

Selles harjutuses on vaja vähemalt üheksa inimese osalemist. Harjutuse eesmärk on füüsiliselt saada ettekujutus sellest, kuidas Bitcoin töötab. Iga võrgus osaleja rolli mängides saate interaktiivse ja lõbusa õppimiskogemuse. See harjutus ei hõlma Lightning Network'i.

### Näide; Nõuab 9 / 11 inimest

Rollid on järgmised:

- 1 Klient
- 1 Kaupmees
- 7 kuni 9 Bitcoin'i sõlme

**Seadistus on järgmine:**

Klient ostab kauplusest toote Bitcoin'iga.

**Stsenaarium 1 - Traditsiooniline pangasüsteem**

- Seadistus:
  - Vaadake diagramme/selgitajat lisatud Figjamis - [Tegevuse skeem](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Saage kolm õpilasvabatahtlikku mängima Kliendi (Alice), Kaupmehe (Bob) ja Panga rolle.
- Toimingu jada:
  - Klient - sirvib veebipoodi ja leiab 25 dollari eest eseme, mida nad soovivad, ning teatab Kaupmehele, et soovib seda osta
  - Kaupmees - küsib makset.
  - Klient - saadab kaarditeabe Kaupmehele
  - Kaupmees - edastab teabe Pangale (identifitseerides nii enda kui ka kliendi identiteedi/teabe) paludes makset
  - Pank kogub teavet Kliendi ja Kaupmehe (Alice ja Bob) kohta ning kontrollib, kas kliendi kontol on piisavalt vahendeid.
  - Võtab Alice'i kontolt maha 25 dollarit, lisab Bob'i kontole 24 dollarit, võtab 1 dollari teenustasu
  - Kaupmees saab Pangalt rohelise tule ja saadab kliendile kauba.
- Kommentaarid:
  - Bobil ja Alicel peab olema pangaarve.
  - Pank kogub identifitseerivat teavet nii Bobi kui ka Alice kohta.
  - Pank võtab lõivu.
  - Pangale peab olema usaldatud iga osaleja raha hoidmine kogu aeg.

**Stsenaarium 2 - Bitcoin'i süsteem**

- Seadistus:
  - Vaadake diagramme/selgitajat lisatud Figjamis - [Tegevuse skeem](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Asenda Pank üheksa õpilasega, kes mängivad Arvuti (Bitcoin Node'id/Miner'id) rolli võrgus, et asendada Pank.
- Igal 9 Arvutil on täielik ajalooline ülevaade kõigist kunagi tehtud tehingutest (seega täpsed saldod ilma võltsinguteta), samuti reeglite kogum:
  - Kontrolli, kas tehing on korrektselt allkirjastatud (võti sobib lukku)
  - Edasta ja võta vastu kehtivaid tehinguid võrgu eakaaslastelt, viska välja kehtetud (kaasa arvatud need, mis üritavad samu vahendeid kaks korda kulutada)
- Uuenda/lisa perioodiliselt kirjeid uute tehingutega, mis on saadud "juhuslikult" arvutilt, tingimusel, et kõik sisud on kehtivad (märkus: me jätame praegu lihtsuse huvides tähelepanuta Proof of Work komponendi), vastasel juhul lükka need tagasi ja jätka nagu varem, kuni järgmine "juhuslik" arvuti saadab uuenduse
  - Kui sisu oli kehtiv, premeeriti õiget summat.
- Mängi läbi sündmuste jada:
  - Klient - sirvib poodi internetis ja leiab eseme hinnaga $25, mida nad soovivad, ning teavitab Kaupmeest, et nad sooviksid osta
  - Kaupmees - küsib makset, saates kliendile arve/aadressi oma rahakotist.
  - Klient - koostab tehingu (saates $25 väärtuses BTC-d Kaupmehele antud aadressile) ja edastab selle Bitcoin võrku.
- Arvutid - võtavad tehingu vastu ja kontrollivad:
  - Saatmisel olevas aadressis on vähemalt $25 BTC-d
  - Tehing on korrektselt allkirjastatud (“avatud” kliendi poolt)
  - Kui see pole nii, siis tehingut võrku ei levitata, kui aga on, siis see levib ja ootab.
  - Kaupmehed saavad kontrollida, et tehing on ootel ja ootab.
- Üks arvuti valitakse "juhuslikult" välja, et pakkuda välja tehingu lõplikku vormistamist, edastades "bloki", mis seda sisaldab; kui see vastab nõuetele, saavad nad BTC preemia.
  - VALIKULINE/EDASIJÕUDNUTELE - arvuti juhusliku valimise asemel simuleerige kaevandamist, lastes Arvutitel täringut veeretada, kuni mingi ettemääratud tulemus saabub (nt esimene, kes veeretab kaks kuut, valitakse)
  - Samuti saab läbi mängida, mis juhtuks, kui kaks Arvutit võidavad peaaegu samaaegselt, põhjustades ahela lõhenemise.
  - Arvutid kontrollivad kehtivust, uuendavad/lisavad kirjeid oma pearaamatusse, kui reeglid on täidetud, ja edastavad bloki eakaaslastele.
  - Juhuslikult valitud arvuti saab preemia kehtiva bloki pakkumise eest.
  - Kaupmees kontrollib, et tehing oli lõplikult vormistatud; seega vahendid laekusid ja ese saadeti kliendile.
- Kommentaarid:
  - Pane tähele, et eelnev pangasuhte olemasolu polnud vajalik.
  - Kolmandat osapoolt ei ole vaja kaasata; asendatud koodi/stiimulitega.
  - Andmeid ei koguta kellegi poolt väljaspool otsest vahetust ja osalejate vahel tuleb vahetada ainult vajalik kogus (nt saatmisaadress).
  - Inimeste vahel ei nõuta usaldust (välja arvatud Kaupmees, kes saadab eseme), paljuski nagu sularahaost.
  - Raha kuulub otse inimestele.
  - Bitcoin'i pearaamat on lihtsuse huvides kujutatud dollarites, kuid tegelikkuses on see BTC.
  - Simuleerime ühe tehingu edastamist, kuid tegelikkuses on võrgus ootel mitu tehingut ja blokid sisaldavad korraga tuhandeid tehinguid. Node'id kontrollivad ka, et võrgus poleks topeltkulutamise tehinguid ootel (kui oleks, siis viskaksin kõik peale ühe välja).
- Pettuse stsenaariumid:
  - Mis siis, kui kliendil ei oleks $25 BTC-d?
    - Nad ei saaks tehingut luua, sest “avamine” ja “omand” on sama asi ning arvutid kontrollivad, kas tehing on korrektselt allkirjastatud; vastasel juhul lükatakse see tagasi.
- Mis juhtub, kui juhuslikult valitud arvuti üritab "muuta pearaamatut"?
  - Plokk lükatakse tagasi, kuna iga teine arvuti omab täielikku ajalugu ja märkaks muudatust, rikkudes ühte nende reeglitest.
  - Juhuslik arvuti ei saaks preemiat ja ükski nende plokist pärit tehing ei saaks lõplikult kinnitatud.

## Teadmiste hindamine

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### KA Klassiarutelu

Arutage mõningaid lihtsustusi, mis tehti klassiülesandes teise stsenaariumi all, ja kirjeldage, mida tegelik Bitcoin süsteem teeb üksikasjalikumalt.

### KA Sõnavara ülevaade

Defineerige järgmised võtmetähtsusega terminid, mis tutvustati eelmises jaotises:

- Sõlm (Node)
- Mempool
- Raskustase (Difficulty Target)
- Plokk (Block)

**Arutage grupina mõningate lisaterminite tähendust:**

Blockchain, Tehing (Transaction), Topeltkulutamine (Double-Spend), Bütsantsi kindralite probleem (Byzantine Generals’ Problem), Kaevandamine (Mining), Töötõend (Proof of Work, PoW), Hash-funktsioon, Ploki preemia (Block Reward), Blockchain, Pikim kett (Longest Chain), 51% rünnak, Väljund (Output), Väljundi lukk (Output Lock), Muutus (Change), Satoshi'd, Avalik/Privaat võti, Aadress, Avaliku võtme krüptograafia, Digitaalallkiri, Rahakott (Wallet)

# BTCPay Serveri tutvustus

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## BTCPay Serveri sisselogimisekraani mõistmine

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Töötamine BTCPay Serveriga

Selle kursuse ploki eesmärk on saada üldine arusaam BTCPay Serveri tarkvarast. Jagatud keskkonnas on soovitatav järgida õpetaja demonstreerimist ja jälgida koos BTCPay Serveri õpikuga õpetajat. Õpid looma rahakotti mitmel viisil. Näited hõlmavad kuumade rahakottide seadistamist ja riistvara rahakotte, mis on ühendatud läbi BTCPay Serveri Vaulti. Need eesmärgid toimuvad demo keskkonnas, millele annab juurdepääsu teie kursuse õpetaja.

Kui järgite seda kursust iseseisvalt, leiate kolmandate osapoolte hostide nimekirja demo eesmärkidel aadressil https://directory.btcpayserver.org/filter/hosts. Me ei soovita kasutada neid kolmandate osapoolte võimalusi tootmiskeskkondades, kuid need teenivad õigeid eesmärke Bitcoin'i ja BTCPay Serveri kasutuselevõtu tutvustamiseks.

BTCPay Serveri rockstar praktikandina võib teil olla eelnev kogemus Bitcoin'i sõlme seadistamisel. See kursus räägib spetsiaalselt BTCPay Serveri tarkvarapaketi kohta.

Paljud BTCPay Serveri võimalused eksisteerivad mingil kujul ka teistes Bitcoin'i rahakottidega seotud tarkvarades.

### BTCPay Serveri sisselogimisekraan

Demo keskkonda sisenemisel palutakse teil 'Logi sisse' või 'Loo oma konto'. Serveri administraatorid võivad turvalisuse kaalutlustel uute kontode loomise funktsiooni välja lülitada. BTCPay Serveri logosid ja nupuvärve saab muuta, kuna BTCPay Server on avatud lähtekoodiga tarkvara. Kolmas osapool võib tarkvara White-label'ida ja muuta kogu välimust.

![image](assets/en/0.webp)

### Konto loomise aken

Kontode loomine BTCPay Serveris nõuab kehtivaid e-posti aadressi stringe; näiteks example@email.com oleks kehtiv string e-posti jaoks.

Parool peab olema vähemalt 8 tähemärki pikk, sealhulgas tähed, numbrid ja sümbolid. Pärast parooli seadmist üks kord, peate sisestatud parooli kinnitama, et veenduda, et see on õige, võrreldes esimeses parooliväljas sisestatuga.
Kui nii e-posti kui ka parooli väljad on korrektselt täidetud, klõpsake nupul ‘Create Account’. See salvestab e-posti ja parooli õpetaja BTCPay Serveri eksemplaris.
![image](assets/en/1.webp)

**!Märkus!**

Kui järgite seda kursust iseseisvalt, võiks sellise konto loomine toimuda kolmanda osapoole hostis; seetõttu mainime taas, et neid ei tohiks kasutada tootmiskeskkondades, vaid ainult koolitusotstarbel.

### Konto loomine BTCPay Serveri administraatori poolt

BTCPay Serveri eksemplari administraator saab samuti luua kontosid BTCPay Serveris. BTCPay Serveri eksemplari administraator saab klõpsata ‘Server Settings’ (1), seejärel ‘Users’ vahekaardil (2) ja üleval paremal ‘Users’ vahekaardil nupul “+ Add User” (3). Eesmärgis (4.3) saate rohkem teada administraatori kontrolli kontode üle.

![image](assets/en/2.webp)

Administraatorina on vaja kasutaja e-posti aadressi ja määrata standardne parool. Soovitatav on administraatoril teavitada kasutajat, et turvalisuse huvides peaksid nad enne konto kasutamist seda parooli muutma. Kui administraator ei sea parooli ja SMTP on serveris seadistatud, saab kasutaja e-kirja kutse lingiga, et luua oma konto ja seada ise parool.

### Näide

Kui järgite kursust õpetaja juhendamisel, järgige õpetaja antud linki ja looge oma konto pakutavas demo keskkonnas. Veenduge, et teie e-posti aadress ja parool oleksid turvaliselt salvestatud; neid sisselogimisandmeid on vaja kursuse ülejäänud demo eesmärkide jaoks.

Teie õpetaja võis olla eelnevalt kogunud e-posti aadressi ja saatnud kutse lingi enne seda harjutust. Kui on antud juhised, kontrollige oma e-posti.

Kui võtate kursust ilma õpetajata, looge oma konto kasutades BTCPay Serveri demo keskkonda; minge aadressile

https://mainnet.demo.btcpayserver.org/login.

Seda kontot tuleks kasutada ainult demonstratsiooni/koolituse eesmärgil ja mitte kunagi äriks.

### Oskuste kokkuvõte

Selles jaotises õppisite järgmist:

- Kuidas luua kontot majutatud serveris läbi liidese.
- Kuidas serveri administraator saab käsitsi lisada kasutajaid serveri seadetes.

### Teadmiste hindamine

#### KA Kontseptuaalne Ülevaade

Andke põhjuseid, miks Demo Serveri kasutamine tootmise eesmärgil on halb mõte.

## Kasutajakonto(de) haldamine

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Konto haldamine BTCPay Serveris

Pärast konto loomist saab poe omanik seda hallata BTCPay Serveri UI vasakus alanurgas. Konto nupu all on mitu kõrgema taseme seadistust.

- Tume/Hele režiim.
- Peida tundlik info lüliti.
- Halda kontot.

![image](assets/en/3.webp)

### Tume ja Hele režiim

BTCPay Serveri kasutajad saavad valida UI Tume või Hele režiimi vahel. Kliendiga suhtlevad lehed ei muutu. Nad kasutavad kliendi eelistatud seadeid tumeda või heleda režiimi osas.

### Peida tundlik info lüliti

Peida tundlik info nupp toob kiire ja lihtsa turvakihi. Kui peate oma BTCPay Serverit kasutama, kuid avalikus kohas võib keegi teie õlale piiluda, lülitage sisse Peida Tundlik Info ja kõik väärtused BTCPay Serveris peidetakse. Keegi võib teie õlale piiluda, kuid ei näe enam tegeletavaid väärtusi.

### Konto haldamine

Kui kasutajakonto on loodud, siis siin saab hallata paroole, 2fa-d või API võtmeid.

### Konto Haldamine - Konto

Valikuliselt uuendage oma kontot erineva e-posti aadressiga. Selleks, et tagada teie e-posti aadressi õigsus, võimaldab BTCPay Server saata kinnituseks kontroll-e-kirja. Kui kasutaja määrab uue e-posti aadressi ja kinnitab, et kinnituskiri töötas, klõpsake salvestamiseks. Kasutajanimi jääb samaks mis eelmine e-post.

Kasutaja võib otsustada kustutada oma konto tervikuna. Seda saab teha, klõpsates konto vahelehel kustutamise nuppu.

![image](assets/en/4.webp)

**!Märkus!**

Pärast e-posti muutmist, konto kasutajanimi ei muutu. Eelnevalt antud e-posti aadress jääb sisselogimisnimeks.

### Konto Haldamine - Parool

Üliõpilane võib soovida oma parooli muuta. Ta saab seda teha, minnes parooli vahelehele. Siin on tal vaja sisestada oma vana parool ja saab selle muuta uueks.

![image](assets/en/5.webp)

### Kahefaktoriline Autentimine (2fa)

Et piirata varastatud parooli tagajärgi, võite kasutada kahefaktorilist autentimist (2fa), mis on suhteliselt uus turvameetod. Kahefaktorilise autentimise saate aktiveerida konto haldamise kaudu ja kahefaktorilise autentimise vahelehe kaudu. Pärast kasutajanime ja parooliga sisselogimist peate tegema teise sammu.

BTCPay Server võimaldab 2FA-d lubada kahel viisil, rakenduspõhine 2FA (Authy, Google, Microsoft autentikatsioonirakendused) või turvaseadmete kaudu (FIDO2 või LNURL Auth).

### Kahefaktoriline Autentimine - Rakenduspõhine

Sõltuvalt teie mobiiltelefoni operatsioonisüsteemist (Android või iOS), saavad kasutajad valida järgmiste rakenduste vahel;

1. Laadige alla kahefaktoriline autentikatsioonirakendus;
   - Authy [Android](https://play.google.com/store/apps/details?id=com.authy.authy) või [iOS](https://apps.apple.com/us/app/authy/id494168017) jaoks
   - Microsoft Authenticator [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) või [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) jaoks
   - Google Authenticator [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) või [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605) jaoks
2. Pärast autentikatsioonirakenduse allalaadimist ja installimist.
   - Skaneerige BTCPay Serveri poolt pakutud QR-kood
   - Või sisestage BTCPay Serveri poolt genereeritud võti käsitsi oma autentikatsioonirakendusse.
3. Autentikatsioonirakendus annab teile unikaalse koodi. Sisestage unikaalne kood BTCPay Serverisse, et kinnitada seadistus, ja klõpsake protsessi lõpuleviimiseks kinnita.

![image](assets/en/6.webp)

### Oskuste Kokkuvõte

Selles jaotises õppisite järgmist:

- Konto haldamise võimalused ja erinevad viisid konto haldamiseks BTCPay Serveri instantsis.
- Kuidas seadistada rakenduspõhist 2FA-d.

### Teadmiste Hindamine

#### KA Kontseptuaalne Ülevaade

Kirjeldage, kuidas rakenduspõhine 2FA aitab teie kontot turvata

## Uue poe loomine

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Loo oma poodi viisard

Kui uus kasutaja logib sisse BTCPay Serverisse, on keskkond tühi ja vajab esimest poodi. BTCPay Serveri tutvustav võlur annab kasutajale võimaluse „Loo oma pood“ (1). Poodi võib vaadelda kui kodu teie Bitcoin'i vajadustele. Uus BTCPay Serveri sõlm alustab Bitcoin'i plokiahela sünkroniseerimisega (2). Sõltuvalt sellest, millist infrastruktuuri te BTCPay Serveri jaoks kasutate, võib see võtta mõnest tunnist mõne päevani. Instantsi praegune versioon kuvatakse teie BTCPay Serveri kasutajaliidese paremas alanurgas. See on kasulik viide, kui tegelete tõrkeotsinguga.
![image](assets/en/7.webp)

### Loo oma pood võlur

Selle kursuse järgimine algab veidi erineva ekraaniga kui eelmine leht. Kuna teie juhendaja on Demo keskkonna ette valmistanud, on Bitcoin'i plokiahel eelnevalt sünkroniseeritud ja seetõttu te ei näe sõlmede sünkroonimise olekut.

Kasutaja võib otsustada kustutada kogu oma konto. Seda saab teha, klõpsates kustutamisnuppu kontovahekaardil.

![image](assets/en/8.webp)

**!Märkus!**

BTCPay Serveri kontod võivad luua piiramatu arvu poode. Iga pood on rahakott või „kodu“.

### Näide

Alustage klõpsates "Loo oma pood".

![image](assets/en/9.webp)

See loob teie esimese kodu ja armatuurlaua BTCPay serveri kasutamiseks.

(1) Pärast "Loo oma pood" klõpsamist nõuab BTCPay Server, et te nimetate poe; see võib olla teile mis tahes kasulik nimi.

![image](assets/en/10.webp)

(2) Järgmiseks tuleb määrata vaikimisi poe valuuta, kas fiat valuuta või denomineeritud Bitcoin / Sats standardis. Demo keskkonnas seame selle USD-le.

![image](assets/en/11.webp)

(3) Poe seadistuse viimase parameetrina nõuab BTCPay Server, et määrate "Eelistatud hinnaallika", et võrrelda Bitcoin'i hinda praeguse fiat hinnaga, nii et teie pood kuvab õige vahetuskursi Bitcoin'i ja poe määratud fiat valuuta vahel. Me jääme Demo näites vaikimisi juurde ja seame selle Krakeni börsile. BTCPay Server kasutab vahetuskursside kontrollimiseks Krakeni API-d.

![image](assets/en/12.webp)

(4) Nüüd, kui need poe parameetrid on määratud, klõpsake nupul Loo ja BTCPay Server loob teie esimese poe armatuurlaua, kus võlur jätkub.

![image](assets/en/13.webp)

Palju õnne, olete loonud oma esimese poe ja see lõpetab selle harjutuse.

![image](assets/en/14.webp)

### Oskuste kokkuvõte

Selles jaotises õppisite:

- Poe loomine ja vaikimisi valuuta seadistamine koos hinnaallika eelistustega.
- Iga "Pood" on uus kodu, eraldatud teistest poodidest sellel BTCPay Serveri paigaldusel.

# Sissejuhatus Bitcoin'i võtmete turvamisse

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Bitcoin'i võtmete genereerimise mõistmine

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Mis on seotud bitcoin'i võtmete genereerimisega?

Bitcoin'i rahakotte luues luuakse nn "seemne". Viimases eesmärgis lõite "seemne", Enne genereeritud sõnade seeriaid tuntakse ka kui mnemoonilisi fraase. Seemet kasutatakse individuaalsete Bitcoin'i võtmete tuletamiseks ja Bitcoin'i saatmiseks või vastuvõtmiseks. Seemnefraase ei tohiks kunagi jagada kolmandate osapoolte või usaldamatute eakaaslastega.
Seemne genereerimine toimub tööstusstandardi alusel, mida tuntakse kui "Hierarhiliselt Deterministlikku" (HD) raamistikku.
![image](assets/en/15.webp)

### Aadressid

BTCPay Server on loodud uue Aadressi genereerimiseks. See leevendab avaliku võtme või Aadressi korduvkasutamise probleemi. Sama avaliku võtme kasutamine muudab teie kogu makseajaloo jälgimise väga lihtsaks. Võtmete mõtlemine ühekordseks kasutamiseks mõeldud kupongidena parandaks oluliselt teie privaatsust. Kasutame ka Bitcoin Aadresse, ärge ajage neid segamini avalike võtmetega.

Aadress tuletatakse avalikust võtmest läbi "hashimisalgoritmi". Enamik rahakotte ja tehinguid kuvab siiski Aadresseid, mitte neid avalikke võtmeid. Aadressid on üldiselt lühemad kui avalikud võtmed ja algavad tavaliselt `1`, `3` või `bc1`, samas kui avalikud võtmed algavad `02`, `03` või `04`.

- Aadressid, mis algavad `1.....`, on endiselt väga levinud aadressid. Nagu peatükis Uue poe loomine mainitud, on need pärandaadressid. See aadressitüüp on mõeldud P2PKH tehingute jaoks. P2Pkh kasutab Base58 kodeeringut, mis muudab aadressi tõstutundlikuks. Selle struktuur põhineb avalikul võtmel koos lisatud ühe tähega identifikaatorina.

- Aadressid, mis algavad `bc1...`, liiguvad aeglaselt väga levinud aadresside hulka. Neid tuntakse kui (native) SegWit Aadresseid. Need pakuvad paremat tasustruktuuri kui teised mainitud Aadressid. Native SegWit Aadressid kasutavad Bech32 kodeeringut ja lubavad ainult väiketähti.

- Aadressid, mis algavad `3...`, on endiselt levinud börsidel sissemakseaadressidena. Neid aadresse mainitakse peatükis Uue poe loomine, mähitud või pesastatud SegWit aadressidena. Siiski võivad need toimida ka "Multisig Aadressina". Kui neid kasutatakse SegWit aadressina, on tehingutasud jällegi väiksemad, kuid mitte nii väikesed kui Native SegWit puhul. P2SH Aadressid kasutavad Base58 kodeeringut. See muudab need tõstutundlikuks, nagu pärandaadress.

- Aadressid, mis algavad `2...`, on Testnet aadressid. Need on mõeldud testnet bitcoinide (tBTC) vastuvõtmiseks. Te ei tohiks seda kunagi segi ajada ja saata Bitcoine nendele aadressidele. Arenduseesmärkidel võite genereerida testnet rahakoti. Veebis on mitmeid kraane, kust saada testnet Bitcoine. Ärge kunagi ostke Testnet Bitcoine. Testnet Bitcoine kaevandatakse. See võib olla põhjus, miks arendaja võib eelistada Regtesti. See on arendajatele mõeldud mänguväljakukeskkond, kust puuduvad teatud võrgukomponendid. Siiski on Bitcoin arenduseesmärkidel väga kasulik.

### Avalikud Võtmed

Avalikke võtmeid kasutatakse tänapäeval praktikas vähem. Aja jooksul on bitcoinide kasutajad asendanud need Aadressidega. Siiski eksisteerivad need endiselt ja kasutatakse aeg-ajalt. Avalikud võtmed on üldiselt palju pikemad stringid kui aadressid. Nagu aadresside puhul, algavad need spetsiifilise identifikaatoriga.

- Esiteks, `02...` ja `03...` on väga standardsete avalike võtmete identifikaatorid, kodeeritud SEC formaadis. Neid saab töödelda ja muuta aadressideks vastuvõtmiseks, kasutada mitme allkirjaga aadresside loomiseks või allkirja kontrollimiseks. Varajased Bitcoin tehingud kasutasid avalikke võtmeid osana P2PK tehingutest.

- HD rahakotid kasutavad siiski erinevat struktuuri. `xpub...`, `ypub...` või `zpub...` on nn laiendatud avalikud võtmed, mida nimetatakse xpubideks. Neid võtmeid kasutatakse paljude avalike võtmete tuletamiseks, kuna see on osa HD rahakotist. Kuna teie xpub hoiab teie kogu ajaloo, st mineviku ja tuleviku tehingute, kirjeid, ärge jagage neid usaldamatute osapooltega.

### Oskuste Kokkuvõte

Selles jaotises õppisite järgmist:

- Aadresside ja avaliku võtme andmetüüpide erinevused ning aadresside kasutamise eelised avalike võtmete üle.

### Teadmiste hindamine

Kirjeldage iga tehingu jaoks uute aadresside kasutamise eelist võrreldes aadresside taaskasutamise või avaliku võtme meetoditega

## Võtmete turvamine riistvara rahakotiga

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Bitcoini võtmete hoiustamine

Pärast seemnefraasi genereerimist nõuab selles raamatus genereeritud 12 - 24 sõna nimekiri korralikku varundamist ja turvalisust, kuna need sõnad on ainus viis rahakotile juurdepääsu taastamiseks. HD rahakottide struktuur ja kuidas see ühe seemne abil aadresse deterministlikult genereerib, tagatakse kõik teie loodud aadressid varundamisega kasutades seda ühte mnemooniliste sõnade nimekirja, mis esindab teie seemet või taastefraasi.

Hoidke oma taastefraas turvaliselt. Kui keegi, eriti pahatahtliku kavatsusega, sellele juurde pääseb, võivad nad teie vahendid liigutada. Seemne turvaliselt ja turvatult hoidmine, aga ka selle meeles pidamine on teineteisele vastastikune. Bitcoini privaatvõtmete hoiustamiseks on mitmeid meetodeid, igaühel oma eelised ja puudused, kas turvalisuse, privaatsuse, mugavuse või füüsiliste vahendite osas. Privaatvõtmete tähtsuse tõttu kipuvad bitcoini kasutajad neid võtmeid "isehoidmises" säilitama, mitte kasutama "hoiustamisteenuseid" nagu pangad. Sõltuvalt kasutajast peab ta kasutama kas külma hoiustamise lahendust või kuuma rahakotti.

### Kuuma ja külma hoiustamise meetodid bitcoini võtmetele

Tavaliselt jaotatakse bitcoini rahakotid kuuma rahakoti või külma rahakoti kategooriatesse. Enamik kompromisse seisneb mugavuses, kasutuslihtsuses ja turvariskides. Igaüht neist meetoditest võib samuti näha hoiustamislahenduses. Siiski on kompromissid siin enamasti turvalisuse ja privaatsusega seotud ning ulatuvad selle kursuse raamidest välja.

### Kuum rahakott

Kuumad rahakotid on kõige mugavam viis Bitcoini kasutamiseks mobiili, veebi või lauaarvuti tarkvara kaudu. Rahakott on alati ühendatud internetiga, võimaldades kasutajatel Bitcoini saata või vastu võtta. See on aga ka selle nõrkus, kuna rahakott on alati võrgus, on see nüüd rohkem avatud rünnakutele häkkerite või teie seadmes oleva pahavara poolt. BTCPay Serveris hoiustatakse privaatvõtmeid instantsis. Kui keegi pääseb teie BTCPay Serveri poodi, võivad nad sellelt aadressilt vahendid varastada, kui nad on pahatahtlikud. Kui BTCPay Server töötab majutatud keskkonnas, peaksite seda alati oma turvaprofiilis arvestama ja eelistatavalt sellisel juhul mitte kasutama kuuma rahakotti. Kui BTCPay Server on paigaldatud teie enda riistvarale, mida te turvate ja usaldate, väheneb riskiprofiil märkimisväärselt, kuid see ei kao kunagi!

### Külm rahakott

Inimesed liigutavad oma Bitcoini külma rahakotti, kuna see suudab privaatvõtmed internetist eraldada. Internetiühenduse võrrandist eemaldamine vähendab pahavara, nuhkvara ja SIM-vahetuste riski. Usutakse, et külma hoiustamine on turvalisuse ja autonoomia osas parem kui kuum hoiustamine, niikaua kui võetakse asjakohaseid ettevaatusabinõusid, et vältida Bitcoini privaatvõtmete kaotamist. Külm hoiustamine sobib kõige paremini suurtele Bitcoini kogustele, mida ei ole kavas tihti kulutada rahakoti seadistuse keerukuse tõttu.

On mitmeid meetodeid, kuidas hoiustada Bitcoini võtmeid külmas hoiustamises, alates paber rahakottidest kuni ajurahakottideni, riistvara rahakottideni või algusest peale rahakoti failini. Enamik rahakotte kasutab seemnefraasi genereerimiseks BIP 39. Siiski ei ole Bitcoini põhitarkvaras veel jõutud konsensusele selle kasutamise osas. Bitcoini põhitarkvara genereerib endiselt Wallet.dat faili, mille peate hoiustama turvalises võrguühenduseta asukohas.

### Oskuste kokkuvõte

Selles jaotises saite teada:

- Kuuma ja külma rahakoti erinevused funktsionaalsuse ja nende kompromisside osas.
- Mis on rahakott?
- Mis vahe on kuumadel ja külmadel rahakottidel?

- Kirjeldage, mida tähendab "rahakoti genereerimine"?

## Kasutades oma Bitcoin võtmeid

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### BTCPay Serveri Rahakott

BTCPay Server koosneb järgmistest standardsetest rahakoti funktsioonidest:

- Tehingud
- Saada
- Vasta võtta
- Uuesti skaneerida
- Tõmbemaksed
- Väljamaksed
- PSBT
- Üldseaded

### Tehingud

Administraatorid näevad konkreetsele poele ühendatud ahelarahakoti sisse- ja väljaminevaid tehinguid tehingute vaates. Igal tehingul on eristus vastu võetud ja saadetud vahel. Vastu võetud tehingud on rohelised ja väljaminevad tehingud punased. BTCPay Serveri tehingute vaates näevad administraatorid ka standardsete siltide komplekti.

| Tehingu Tüüp    | Kirjeldus                                     |
| --------------- | --------------------------------------------- |
| App             | Makse saadi läbi rakenduse loodud arve        |
| invoice         | Makse saadi läbi arve                         |
| payjoin         | Maksmata, arve taimer ei ole veel aegunud     |
| payjoin-exposed | UTXO paljastati läbi arve payjoin ettepaneku  |
| payment-request | Makse saadi läbi makse taotluse               |
| payout          | Makse saadeti läbi väljamakse või tagasimakse |

### Kuidas Saata

BTCPay serveri saatefunktsioon saadab tehinguid teie BTCPay Serveri ahelarahakotist. BTCPay Server võimaldab mitmel viisil allkirjastada oma tehinguid fondide kulutamiseks. Tehingut saab allkirjastada;

- Riistvara Rahakott
- Rahakotid, mis toetavad PSBT-d
- HD privaatvõti või taastamisseemned.
- Kuum Rahakott

#### Riistvara rahakott

BTCPay Serveril on sisseehitatud riistvara rahakoti tugi, mis võimaldab teil kasutada oma riistvara rahakotti BTCPay Vaultiga, ilma et see lekitaks teavet kolmandate osapoolte rakendustele või serveritele. Riistvara rahakoti integreerimine BTCPay Serveris võimaldab teil importida oma riistvara rahakoti ja kulutada sissetulevaid vahendeid lihtsa kinnitusega oma seadmes. Teie privaatvõtmed ei lahku seadmest ja kõik vahendid valideeritakse teie täisnoodi vastu, nii et andmeleket ei toimu.

#### Allkirjastamine rahakotiga, mis toetab PSBT-d

PSBT (osaliselt allkirjastatud Bitcoin tehingud) on Bitcoin tehingute vahetusformaadiks, mis vajavad veel täielikku allkirjastamist. PSBT-d toetatakse BTCPay Serveris ja seda saab allkirjastada ühilduvate riist- ja tarkvararahakottidega.

Täielikult allkirjastatud Bitcoin tehingu loomine toimub järgmiste sammude kaudu:

- PSBT koostatakse spetsiifiliste sisendite ja väljunditega, kuid ilma allkirjadeta
- Eksporditud PSBT-d saab importida rahakott, mis toetab seda formaati
- Tehingu andmeid saab uurida ja allkirjastada kasutades rahakotti
- Allkirjastatud PSBT fail eksporditakse rahakotist ja imporditakse BTCPay Serverisse
- BTCPay Server toodab lõpliku Bitcoin tehingu
- Kontrollite tulemust ja edastate selle võrku

#### Allkirjastamine HD privaatvõtmega või mnemoonilise seemnega

Kui olete varem loonud rahakoti kasutades BTCPay Serverit, saate vahendeid kulutada sisestades oma privaatvõtme sobivasse välja. Määrake korrektne "AccountKeyPath" rahakoti seadetes; vastasel juhul ei saa kulutada.

#### Allkirjastamine kuuma rahakotiga

Kui lõite uue rahakoti oma poe seadistamisel ja lubasite selle kui kuuma rahakoti, kasutab see automaatselt serveril salvestatud seemet allkirjastamiseks.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) on Bitcoin protokolli funktsioon, mis võimaldab teil asendada varem edastatud tehingu (kui see veel ei ole kinnitatud). See võimaldab juhuslikult muuta teie rahakoti tehingu jälge või asendada see kõrgema tasumääraga, et tõsta tehing kinnitamise järjekorras (kaevandamises) kõrgemale prioriteedile. See asendab efektiivselt algse tehingu, kuna kõrgem tasumäär saab prioriteedi ja kui see on kinnitatud, muudab algse tehingu kehtetuks (ei toimu topeltkulutust).
Vajutage "Täpsemad seaded" nuppu, et vaadata RBF valikuid;

![image](assets/en/16.webp)

- Juhuslikustamine suurema privaatsuse jaoks, võimaldab tehingut automaatselt asendada tehingu jälje juhuslikustamiseks.
- Jah, Märgista tehing RBF-iks ja see asendatakse selgelt (vaikimisi ei asendata, ainult sisendi abil)
- Ei, Ära luba tehingu asendamist.

### Mündi Valik

Mündi valik on edasijõudnud privaatsust tõstev funktsioon, mis võimaldab teil valida mündid, mida soovite tehingu tegemisel kulutada. Näiteks maksmine müntidega, mis on värskelt segatud konjoini segust.

Mündi valik töötab loomulikult koos rahakoti siltide funktsiooniga. See võimaldab teil sissetulevaid vahendeid sildistada sujuvamaks UTXO haldamiseks ja kulutamiseks.

BTCpay Server toetab ka BIP-329 siltide haldamiseks. BIP-329 võimaldab siltide lisamist; kui teete ülekande rahakotist, mis toetab seda konkreetset BIP-i ja seadistate sildid, tunnistab BTCPay Server neid ja impordib need. Serverite migreerimisel saab seda teavet samuti eksportida ja uude keskkonda importida.

### Kuidas Vastu Võtta

BTCPay Serveris vastuvõtu nupule vajutades genereeritakse kasutamata aadress, mida saab maksete vastuvõtmiseks kasutada. Administraatorid võivad samuti genereerida uue aadressi, luues uue "Arve".

BTCPay Server palub alati genereerida järgmise saadaoleva aadressi, et vältida aadressi taaskasutust. Pärast "Genereeri järgmine saadaolev BTC aadress" nupule vajutamist genereeris BTCPay Server uue aadressi ja QR-koodi. See võimaldab teil otse seada aadressile Sildi paremaks aadresside haldamiseks.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Uuesti skaneerimine

Uuesti skaneerimise funktsioon toetub Bitcoin Core 0.17.0 "Scantxoutset" funktsioonile, et skaneerida blockchaini praegust seisundit (nimetatakse UTXO Set) mündide jaoks, mis kuuluvad seadistatud tuletusskeemi. Rahakoti uuesti skaneerimine lahendab kaks probleemi, mida BTCPay Serveri kasutajad kogevad.

1. Vahe limiidi probleem - Enamik kolmanda osapoole rahakotte on kerged rahakotid, mis jagavad sõlme paljude kasutajate vahel. Kerged ja täis sõlmele toetuvad rahakotid piiravad jälgitavate tasakaaluta aadresside hulka (tavaliselt 20) blockchainis, et vältida jõudlusprobleeme. BTCPay Server genereerib iga arve jaoks uue aadressi. Arvestades eelnevat, pärast BTCPay Serveri 20 järjestikuse tasumata arve genereerimist, lõpetab väline rahakott tehingute jälgimise, eeldades, et uusi tehinguid ei toimunud. Teie väline rahakott ei näita neid, kui arved on makstud 21., 22. jne korral. Teisest küljest jälgib BTCPay Serveri rahakott sisemiselt kõiki genereeritud aadresse koos palju suurema vahe limiidiga. See ei sõltu kolmandast osapoolest ja saab alati näidata õiget saldo.
2. Lahendus vahepiirangu probleemile - Kui teie [väline/olemasolev rahakott](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) võimaldab vahepiirangu konfiguratsiooni, siis lihtne lahendus on selle suurendamine. Siiski, enamik rahakotte seda ei võimalda. Ainsad rahakotid, mida me teame, mis lubavad vahepiirangu seadistamist, on Electrum, Wasabi ja Sparrow Wallet. Kahjuks võite paljude teiste rahakottidega kokku puutuda probleemiga. Parima kasutajakogemuse ja privaatsuse tagamiseks kaaluge väliste rahakottide kasutamisest loobumist ja BTCPay Serveri sisemise rahakoti kasutamist.

#### BTCPay Server kasutab “mempoolfullrbf=1”

BTCPay Server kasutab “mempoolfullrbf=1”; oleme lisanud selle vaikimisi teie BTCPay Serveri seadistusse. Siiski oleme teinud sellest ka fragmendi, mille saate ise välja lülitada. Ilma “mempoolfullrbf=1”-ta, kui klient topeltkulutab makse tehinguga, mis ei signaliseeri RBF-i, saaks kaupmees sellest teada alles pärast kinnitust.

Administraator võib soovida sellest seadistusest loobuda. Järgneva stringi abil saate muuta vaikeseadistust.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### BTCPay Serveri rahakoti seaded

BTCPay Serveri rahakoti seaded annavad selge ja kiire ülevaate teie rahakoti üldistest seadetest. Kõik need seaded on eeltäidetud, kui rahakott loodi BTCPay Serveriga.

![image](assets/en/19.webp)

BTCPay Serveri rahakoti seaded annavad selge ja kiire ülevaate teie rahakoti üldistest seadetest. Kõik need seaded on eeltäidetud, kui rahakott loodi BTCPay Serveriga. BTCPay Serveri rahakoti seadete juures algab kõik rahakoti staatusest. Kas see on ainult-vaatamise või kuum rahakott? Rahakoti tüübist sõltuvalt võivad tegevused varieeruda puuduvate tehingute rahakotis uuesti skaneerimisest, vanade tehingute ajaloost kärpimisest, rahakoti registreerimisest makselinkide jaoks või praeguse rahakoti asendamisest ja kustutamisest poega seotud. BTCPay Serveri rahakoti seadetes võib administraator määrata rahakotile sildi paremaks rahakoti haldamiseks. Siin saab administraator näha ka Derivatsiooni skeemi, konto võtit (xpub), sõrmejälge ja võtmepathi. Maksete seaded rahakotis on ainult 2 peamist seadet. Makse on kehtetu, kui tehing ei kinnitu (määratud minutites) pärast arve aegumist. Arvestage arve kinnitatuks, kui maksetehingul on X arv kinnitusi. Administraatorid saavad seada ka lüliti, et näidata maksetel soovitatud tasusid või määrata käsitsi kinnituse sihtmärk plokkide arvus.

![image](assets/en/20.webp)

**!Märkus!**

Kui järgite seda kursust iseseisvalt, võiks sellise konto loomine toimuda kolmanda osapoole hostis, seega mainime taas, et neid ei tohiks kasutada tootmiskeskkondades, vaid ainult koolitusotstarbel.

### Näide

#### Seadista Bitcoin Rahakott BTCPay Serveris

BTCPay Server võimaldab rahakoti seadistamist kahel viisil. Üks viis on juba olemasoleva Bitcoin rahakoti importimine. Importimine saab toimuda riistvara rahakoti ühendamise, rahakoti faili importimise, laiendatud avaliku võtme sisestamise, rahakoti QR-koodi skaneerimise või vähem soovitatava, käsitsi loodud rahakoti taastamisseemne sisestamise teel. BTCPay Serveris on võimalik ka uus rahakott luua. BTCPay Serveri uue rahakoti genereerimisel on kaks võimalikku seadistusviisi.
BTCPay Serveri kuum rahakoti valik võimaldab funktsioone nagu 'Payjoin' või 'Liquid'. Siiski on sellel puudus: selle rahakoti jaoks genereeritud taastamisseem salvestatakse serverisse, kus igaühel, kellel on administraatori õigused, on võimalik taastamisseemet hankida. Kuna teie privaatvõti on tuletatud teie taastamisseemnest, võib pahatahtlik tegelane saada juurdepääsu teie praegustele ja tulevastele vahenditele!
Selle riski leevendamiseks BTCPay Serveris saab administraator seadistada Serveri Seaded > Poliitikad > "Luba mitte-administraatoritel luua oma poodidele kuumi rahakotte" ei, nagu see vaikimisi on. Nende kuumade rahakottide turvalisuse suurendamiseks peaks serveri administraator lubama kontodel, millel on lubatud kuumad rahakotid, 2FA autentimise. Privaatvõtmete hoidmine avalikul serveril on ohtlik ja sellega kaasnevad riskid. Mõned neist on sarnased Lightning Network'i riskidega (vt järgmist peatükki Lightning Network'i riskide kohta).

Teine võimalus, mida BTCPay Server pakub uue rahakoti loomiseks, on luua Vaatlus-Ainult rahakott. BTCPay Server genereerib teie privaatvõtmed ühe korra. Pärast kasutaja kinnitust, et nad on oma Seemnefraasi üles kirjutanud, kustutab BTCPay Server privaatvõtmed serverist. Selle tulemusena on teie poel nüüd ühendatud Vaatlus-Ainult rahakott. Saadud vahendite kulutamiseks oma vaatlus-ainult rahakotist vaadake peatükki Kuidas Saata, kasutades kas BTCPay Server Vaulti, PSBT-d (osaliselt allkirjastatud bitcoin tehing) või, vähem soovitatavalt, oma seemnefraasi käsitsi esitades.

Te lõite eelmises osas uue 'Poe'. Paigaldusviisard jätkab küsimisega, kas seadistada "rahakott" või "Lightning node". Selles näites järgite "Seadista rahakott" viisardi protsessi (1).

![image](assets/en/21.webp)

Pärast "Seadista rahakott" valimist jätkab viisard küsimisega, kuidas soovite jätkata; BTCPay Server pakub nüüd võimalust ühendada olemasolev Bitcoin rahakott teie uue poega. Kui teil pole rahakotti, pakub BTCPay Server uue loomist. See näide järgib samm-sammult "loo uus rahakott" (2). Järgige samme, et õppida, kuidas "Ühenda olemasolev rahakott (1).

![image](assets/en/22.webp)

**!Märkus!**

Kui võtate seda kursust klassiruumis, on praegune näide ja genereeritud seeme ainult hariduslikel eesmärkidel. Nendel aadressidel ei tohiks kunagi olla suuremat summat kui harjutuste jaoks vajalik.

(1) Jätkake “Uus rahakott” viisardit, klõpsates nupul "Loo uus rahakott".

![image](assets/en/23.webp)

(2) Pärast “Loo uus rahakott” valimist annab järgmine aken viisardis võimalused “Kuum rahakott” ja “Vaatlus-ainult rahakott”. Kui järgite juhendajaga koos, on teie keskkond ühine Demo ja saate luua ainult Vaatlus-ainult rahakoti. Märgake allpool toodud joonistel mõlema vahelist erinevust. Kuna olete Demo keskkonnas koos juhendajaga, looge "Vaatlus-ainult rahakott" ja jätkake "Uus Rahakott" viisardiga.

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) Uue rahakoti viisardi jätkamisel olete nüüd BTC vaatlus-ainult rahakoti loomise jaotises. Siin saame määrata rahakoti "Aadressi tüübi". BTCPay Server võimaldab teil valida eelistatud Aadressi tüübi; selle kursuse kirjutamise ajal on endiselt soovitatav kasutada bech32 aadresse. Õppige esimeses peatükis rohkem aadresside kohta.

- Segwit (bech32)
- Native SegWit aadressid algavad `bc1q`. - Näide: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Legacy aadressid algavad numbriga `1`.
  - Näide: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Edasijõudnutele)
  - Taproot aadressid algavad `bc1p`.
  - Näide: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Segwit wrapped aadressid algavad `3`.
  - Näide: `37BBXXXXXXXXXXXXXXX`

Valige segwit (soovitatud) kui eelistatud rahakoti aadressi tüüp.

![image](assets/en/26.webp)

(4) Rahakoti parameetri seadistamisel lubab BTCPay Server kasutajatel seada valikulise paroolilause läbi BIP39, olge kindlad, et kinnitate oma parooli.

![image](assets/en/27.webp)

(5) Pärast rahakoti aadressi tüübi seadistamist ja võimalike edasijõudnute valikute seadmist, klõpsake Loo, ja BTCPay Server genereerib teie uue rahakoti. Pange tähele, et see on viimane samm enne teie seemnefraasi genereerimist. Veenduge, et teete seda keskkonnas, kus keegi ei saa teie seemnefraasi ekraanilt varastada.

![image](assets/en/28.webp)

(6) Järgnevas võluri ekraanil näitab BTCPay Server teile teie äsja genereeritud rahakoti taastamise seemnefraasi; need on võtmed teie rahakoti taastamiseks ja tehingute allkirjastamiseks. BTCPay Server genereerib 12-sõnalise seemnefraasi. Need sõnad kustutatakse serverist pärast seda seadistusekraani. See rahakott on spetsiifiliselt ainult-vaatamise rahakott. On soovitatav mitte salvestada seda seemnefraasi digitaalselt või fotopildina. Kasutajad võivad võluris edasi minna ainult siis, kui nad aktiivselt kinnitavad, et nad on oma seemnefraasi üles kirjutanud.

![image](assets/en/29.webp)

(7) Pärast Valmis klõpsamist ja äsja genereeritud Bitcoin'i seemnefraasi turvamist, uuendab BTCPay Server teie poodi uue rahakotiga ja on valmis makseid vastu võtma. Kasutajaliideses, vasakul navigeerimismenüüs, pange tähele, kuidas Bitcoin on nüüd esile tõstetud ja aktiveeritud rahakoti all.

![image](assets/en/30.webp)

### Näide: Seemnefraasi üleskirjutamine

See on väga eriline ja turvaline hetk Bitcoin'i kasutamiseks. Nagu varem mainitud, peaks ainult teie ise omama juurdepääsu või teadmisi oma seemnefraasi kohta. Järgides juhendajat ja klassiruumi, peaks genereeritud seeme olema kasutusel ainult sellel kursusel. Liiga paljud faktorid, nagu klassikaaslaste uudishimulikud pilgud, turvamata süsteemid ja paljud teised, muudavad need võtmed ainult hariduslikuks ja mitteusaldusväärseks. Siiski tuleks kursuse näidete jaoks genereeritud võtmed siiski säilitada.

Esimene meetod, mida me praeguses olukorras kasutame, samuti kõige vähem turvaline, on seemnefraasi õiges järjekorras üleskirjutamine. Seemnefraasi kaart on kursuse materjalides, mida antakse õpilasele või leitakse BTCPay Server GitHub'ist. Me kasutame seda kaarti sõnade üleskirjutamiseks eelmises etapis genereeritud sõnadest. Veenduge, et kirjutate need õiges järjekorras üles. Pärast üleskirjutamist kontrollige seda, mida tarkvara andis, et veenduda, et kirjutasite need õiges järjekorras üles. Kui olete need üles kirjutanud, klõpsake märkeruutu, mis kinnitab, et olete oma seemnefraasi korrektselt üles kirjutanud.

### Näide: Seemnefraasi hoidmine riistvaralises rahakotis

Sellel kursusel puudutame seemnefraasi hoidmist riistvaralises rahakotis. Juhendaja poolt antud kursuse järgimine ei pruugi alati sellist seadet hõlmata. Kursuse juhendmaterjalides on kirjas nimekiri riistvaralistest rahakottidest, mis sobiksid selle harjutuse jaoks.
Selles näites kasutame BTCPay Serveri hoidlat ja Blockstream Jade riistvaralist rahakotti.
Samuti võite jälgida videojuhendit riistvaralise rahakoti ühendamise kohta.
![BTCPay Server - Kuidas ühendada oma riistvaralist rahakotti BTCPay hoidlaga.](https://youtu.be/s4qbGxef43A)

Laadige alla BTCPay Serveri hoidla: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Veenduge, et laadite alla oma süsteemile õiged failid. Windowsi kasutajad peaksid allalaadima [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) paketi, Maci kasutajad [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) ja Linuxi kasutajad [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Pärast BTCPay Serveri hoidla installimist käivitage tarkvara, klõpsates töölaual ikoonil. Kui BTCPay Serveri hoidla on korrektselt installitud ja käivitatud esimest korda, küsib see luba kasutamiseks veebirakendustega. See palub anda juurdepääsu konkreetsele BTCPay Serverile, millega te töötate. Nõustuge nende tingimustega. BTCPay Serveri hoidla hakkab nüüd otsima riistvaralist seadet. Kui seade on leitud, tuvastab BTCPay Server, et hoidla töötab ja on teie seadme tuvastanud.

**!Märkus!**

Ärge andke oma SSH võtmeid või serveri administraatori kontot kellelegi teisele peale administraatorite, kui kasutate kuumat rahakotti. Igaühel, kellel on juurdepääs nendele kontodele, on juurdepääs kuumas rahakotis olevatele vahenditele.

### Oskuste Kokkuvõte

Selles jaotises õppisite järgmist:

- Bitcoini rahakoti tehingute vaade ja selle erinevad kategoriseerimised.
- Erinevad võimalused Bitcoini rahakotist saatmisel, alates riistvaralistest kuni kuumade rahakottideni.
- Lõhe limiidi probleem, millega enamik rahakotte silmitsi seisab, ja kuidas seda parandada.
- Kuidas genereerida uus Bitcoini rahakott BTCPay Serveris, sealhulgas võtmete salvestamine riistvaralisse rahakotti ja taastefraasi varundamine.

Selles eesmärgis olete õppinud, kuidas genereerida uus Bitcoini rahakott BTCPay Serveris. Me ei ole veel käsitlenud, kuidas neid võtmeid turvata või kasutada. Selle eesmärgi kiire ülevaate käigus olete õppinud, kuidas seadistada esimene pood. Olete õppinud, kuidas genereerida Bitcoini taastefraas.

### Praktilise Hindamise Teadmiste Ülevaade

Kirjeldage meetodit võtmete genereerimiseks ja skeemi nende turvamiseks, koos turvaskeemi kaubanduslike kompromisside/riskidega.

## BTCPay Serveri Lightning Rahakott

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Kui serveri administraator seadistab uue BTCPay Serveri instantsi, saab ta seadistada Lightning võrgu implementatsiooni, LND, Core Lightning või Eclair; vaadake osa BTCPay Serveri seadistamiseks täpsemate paigaldusjuhiste jaoks.
Kui järgite klassiruumi juhiseid, siis Lightning node ühendamine teie BTCPay Serveriga toimub läbi Custom node. Kasutaja, kes ei ole BTCPay Serveri serveri administraator, ei saa vaikimisi kasutada sisemist Lightning node'i. See on selleks, et kaitsta serveri omanikku oma vahendite kaotamise eest. Serveri administraatorid võivad paigaldada Plugin'i, et anda juurdepääs oma Lightning node'ile läbi LNBank; see on selle raamatu ulatusest väljas; lugege LNBank kohta rohkem ametlikul plugin'i lehel.

### Ühenda sisemine node (serveri administraator)

Serveri Administraator saab kasutada BTCPay Serveri sisemist Lightning Node'i. Sõltumata Lightning'i rakendusest, on sisemise Lightning node'iga ühendamine sama.

Mine tagasi eelnevalt seadistatud poodi ja klõpsa vasakus menüüs "Lightning" rahakotil. BTCPay Server pakub kahte seadistamise võimalust, kasutades Sisemist node'i (vaikimisi ainult Serveri administraator) või kohandatud node'i (väline ühendus). Serveri administraatorid saavad klõpsata "Kasuta sisemist node'i" valikul. Edasine seadistamine pole vajalik. Klõpsa "salvesta" nuppu ja pane tähele teadet, mis ütleb, "BTC Lightning node uuendatud". Pood on nüüd edukalt saanud Lightning võrgu võimekuse.

### Ühenda väline node (serveri kasutaja/poe omanik)

Kuna poe omanikele ei ole vaikimisi lubatud kasutada serveri administraatori Lightning Node'i. Ühendus tuleb luua välise node'iga, kas node'iga, mis kuulus poe omanikule enne BTCPay Serveri seadistamist, LNBank plugin'iga, kui see on serveri administraatori poolt kättesaadavaks tehtud, või hoiustajalahendusega nagu Alby.

Mine tagasi eelnevalt seadistatud poodi ja klõpsa vasakus menüüs rahakottide all "Lightning". Kuna poe omanikele ei ole vaikimisi lubatud kasutada sisemist node'i, on see valik tuhmunud. Kohandatud node on ainus vaikimisi saadaolev valik poe omanikele.

BTCPay Server vajab ühenduse teavet; eelnevalt loodud (või hoiustajalahendus) annab selle teabe, mis on spetsiifiline Lightning'i rakendusele. BTCPay Serveris saavad poe omanikud kasutada järgmisi ühendusi;

- C-lightning TCP või Unix domain socket ühenduse kaudu.
- Lightning Charge HTTPS kaudu
- Eclair HTTPS kaudu
- LND REST proxy kaudu
- LNDhub REST API kaudu

![image](assets/en/31.webp)

Klõpsa "testi ühendust", et veenduda, et sisestasid ühenduse andmed õigesti. Pärast ühenduse kinnitamist klõpsa salvesta ja BTCPay Server näitab, et pood on uuendatud Lightning Node'iga.

### Sisemise Lightning node LND haldamine (Serveri administraator)

Pärast sisemise Lightning Node'iga ühendamist märkavad serveri administraatorid uusi plaate armatuurlaual, mis on spetsiifiliselt Lightning'i teabe jaoks.

- Lightning Balance
- BTC kanalites
  - BTC avatud kanalid
  - BTC kohalik saldo
  - BTC kaugsaldo
  - BTC sulgevad kanalid
- BTC On-chain
  - BTC kinnitatud
  - BTC kinnitamata
  - BTC reserveeritud
- Lightning Teenused
  - Ride the Lightning (RTL).

Klõpsates kas "Ride the Lightning" logol "Lightning teenuste" plaadil või "Lightning" all rahakottides vasakus menüüs, saavad serveri administraatorid jõuda RTL-i Lightning node haldamiseks.

**Märkus!**

Kui sisemise Lightning Node'iga ühendamine ebaõnnestub - Kui sisemine ühendus ebaõnnestub, kinnita:

1. Et Bitcoin on-chain node on täielikult sünkroniseeritud
2. Et Sisemine lightning node on "Lubatud" all "Lightning" > "Seaded" > "BTC Lightning Seaded"
   Kui te ei saa ühendust oma Lightning sõlmega, proovige oma serverit taaskäivitada või lugege lisateavet BTCPay Serveri ametlikust dokumentatsioonist; https://docs.btcpayserver.org/Troubleshooting/ . Te ei saa oma poes Lightning makseid vastu võtta enne, kui teie Lightning sõlm kuvatakse olekus "Online". Proovige testida oma Lightning ühendust, klõpsates lingil "Public Node Info".

### Lightning rahakott

Vasakul menüüribal asuvas Lightning rahakoti valikus leiavad serveri administraatorid lihtsa juurdepääsu RTL-ile, nende avalikule sõlme infole ja Lightning seadetele, mis on spetsiifilised nende BTCPay Serveri poele.

#### Sisemine sõlme info

Serveri administraatorid saavad klõpsata sisemise sõlme info peal ja heita pilgu oma serveri olekule (Online/ Offline) ning ühenduse stringile Clearneti või Tori jaoks.

![image](assets/en/32.webp)

#### Ühenduse muutmine

Kui poe omanik otsustab kasutada muudatusi Lightning seadetes - Ühenduse muutmine.
Avaliku sõlme info kõrval leiavad poe omanikud selle valiku. See toob tagasi algse seadistuse väliste Lightning sõlme ühenduste jaoks, täitke uue Lightning sõlme info, klõpsake salvesta ja uuendage poodi uue sõlme infoga.

![image](assets/en/33.webp)

#### Teenused

Kui serveri administraator otsustab paigaldada mitu teenust Lightning rakendamiseks, kuvatakse need siin. Standardse LND rakendamisega on administraatoritel Ride The Lightning (RTL) standardtööriistana sõlme haldamiseks.

#### BTC Lightning rahakoti seaded

Pärast Lightning sõlme lisamist poodi eelmises etapis, saavad poe omanikud Lightning rahakoti seadetes siiski valida, kas deaktiveerida see oma poe jaoks, kasutades Lightning seadete ülaosas lülitit.

![image](assets/en/34.webp)

#### Lightning maksevalikud

Poe omanikud saavad seada parameetreid järgmiseks, et parandada Lightning kogemust oma klientidele.

- Kuvage Lightning maksesummad Satoshi'des.
- Lisage privaatkanalitele hüppeviited Lightning arvele.
- Ühtlustage on-chain ja Lightning makse URL/QR koodid kassas.
- Seadke kirjelduse mall Lightning arvetele.

#### LNURL

Poe omanikud saavad valida, kas kasutada LNURL-i või mitte. Lightning Network URL ehk LNURL on ettepanek interaktsioonide standardiks Lightning makse tegija ja saaja vahel. Lühidalt, LNURL on bech32 kodeeritud url, millele eelneb lnurl. Lightning rahakott peaks dekodeerima URL-i, võtma ühendust URL-iga ja ootama JSON objekti edasiste juhistega, eelkõige sildiga, mis määratleb knurl'i käitumise.

- Luba LNURL
- LNURL klassikaline režiim
  - Rahakoti ühilduvuse jaoks, Bech32 kodeeritud (klassikaline) vs selgetekstiline URL (tulevane)
- Luba saajal edastada kommentaar.

### Näide 1

#### Ühendu Lightninguga sisemise sõlme kaudu (Administraator)

See valik on saadaval ainult siis, kui olete selle eksemplari administraator või kui administraator on muutnud vaikeseadeid, kus kasutajad saavad kasutada sisemist lightning sõlme.

Administraatorina klõpsake vasakul menüüribal Lightning Rahakotil. BTCPay Server palub valida kahe võimaluse vahel Lightning Sõlme ühendamiseks, kasutada sisemist sõlme või kohandatud välist sõlme. Klõpsake kasutage sisemist sõlme ja seejärel salvestage.

#### Oma Lightning sõlme haldamine (RTL)

Pärast sisemise lightning sõlme ühendamist uuendab BTCPay Server ja kuvab teate "BTC Lightning sõlm uuendatud", kinnitades, et olete nüüd ühendanud Lightningi oma poega.

Lightning sõlme haldamine on serveri administraatori ülesanne. See hõlmab.

- Tehingute haldamine
- Likviidsuse haldamine
  - Sissetulev likviidsus
  - Väljaminev likviidsus
- Eakaaslaste ja kanalite haldamine
  - Ühendatud eakaaslased
  - Kanalitasud
  - Kanali olek
- Kanaliseisundite sagedane varundamine.
- Marsruutimisaruannete kontrollimine.
- Alternatiivina kasutage teenuseid nagu Loop.

Kõik välgu sõlme haldamise toimingud tehakse standardina RTL-i abil (eeldades, et kasutate LND-implementatsiooni). Administraatorid saavad BTCPay Serveris klõpsata oma Lightning Wallet'il ja leida nupu RTL-i avamiseks. BTCPay Serveri peamine armatuurlaud on nüüd uuendatud Lightning Networki plaatidega, sealhulgas kiire juurdepääs RTL-ile.

### Näide 2

#### Ühendamine välguvõrguga Alby kaudu

Kui ühendate hoidlaga nagu Alby, peaksid poe omanikud esmalt looma konto, külastage: https://getalby.com/

![pilt](assets/en/35.webp)

Pärast Alby konto loomist minge oma BTCPay Serveri poodi.

1. samm: Klõpsake armatuurlaual 'Seadista Lightning sõlm' või 'Lightning' rahakottide all.

![pilt](assets/en/36.webp)

2. samm: Sisestage oma rahakoti ühenduse mandaadid, mille Alby on teile andnud. Alby armatuurlaual klõpsake Wallet. Siit leiate "Wallet Connection Credentials". Kopeerige need mandaadid. Kleepige Alby mandaadid BTCPay Serveri ühenduse konfiguratsiooni väljale.

![pilt](assets/en/37.webp)

3. samm: Pärast BTCPay Serverile ühenduse üksikasjade andmist klõpsake nuppu "Test Connection", et veenduda ühenduse nõuetekohases toimimises. Ekraani ülaosas märkate teadet "Connection to lightning node successful". See kinnitab, et kõik toimib korras.

![pilt](assets/en/38.webp)

4. samm: Klõpsake salvesta ja teie pood on nüüd ühendatud välgu sõlmega Alby kaudu.

![pilt](assets/en/39.webp)

**!Märkus!**

Ärge usaldage hoidla Lightning lahendust rohkem väärtusele, kui olete valmis kaotama.

### Oskuste kokkuvõte

Selles jaotises õppisite:

- Kuidas ühendada sisemine või väline Lightning sõlm
- Erinevate Lightninguga seotud plaatide sisu ja funktsioon armatuurlaual
- Kuidas seadistada Lightning rahakotti kasutades Voltage Surge'i või Alby't

### Teadmiste hindamine Praktiline Ülevaade

Kirjeldage mõningaid erinevaid võimalusi Lightning rahakoti oma poega ühendamiseks.

# BTCPay Serveri liides

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Armatuurlaua ülevaade

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server on modulaarne tarkvarapakett. Siiski on olemas standardid, mida iga BTCPay Serveril on ja mida administraatorid/kasutajad kasutavad. Alustades armatuurlauast. Iga BTCPay Serveri peamine sisenemispunkt pärast sisselogimist. Armatuurlaud annab ülevaate sellest, kuidas teie pood esineb, rahakoti praegune saldo ja viimased tehingud viimase 7 päeva jooksul. Kuna see on modulaarne vaade, võivad pistikprogrammid kasutada seda vaadet oma kasuks ja luua oma plaadid armatuurlauale. Selle kursuse raamatus räägime ainult standardsetest pistikprogrammidest/rakendustest ja nende vastavatest vaadetest läbi BTCPay Serveri.

### Armatuurlaua plaadid

BTCPay Serveri armatuurlaua peamises vaates on saadaval mõned standardplaadid. Need plaadid on mõeldud poe omanikule või administraatorile, et ta saaks oma poodi kiiresti ühes ülevaates hallata.

- Rahakoti saldo
- Tehingu tegevus
- Lightning saldo (kui Lightning on poes lubatud)
- Lightning teenused (kui Lightning on poes lubatud)
- Hiljutised tehingud.
- Hiljutised arved
- Praegused aktiivsed rahakogumiskampaaniad
- Poe esitus / enim müüdud esemed.

### Rahakoti saldo

Rahakoti Saldo plaat annab kiire ülevaate teie rahakoti vahenditest ja toimivusest. Seda saab vaadata kas BTC või Fiat valuutas nädala, kuu või aasta graafikul.
![image](assets/en/40.webp)

### Tehingute aktiivsus

Rahakoti Saldo plaadi kõrval kuvab BTCPay Server kiire ülevaate ootel olevatest väljamaksetest, viimase 7 päeva tehingute arvust ja kas teie pood on teinud mingeid tagasimakseid. Hallatavate ootel väljamaksete haldamiseks klõpsake nupul Halda (lisateavet väljamaksete kohta BTCPay Serveris - Maksete peatükis).

![image](assets/en/41.webp)

### Lightning Saldo

See on nähtav ainult siis, kui Lightning on aktiveeritud.

Kui administraator on lubanud Lightning võrgu juurdepääsu, on BTCPay Serveri armatuurlaual nüüd uus plaat teie Lightning sõlme teabega. Kui palju BTC-d on kanalites, kuidas see on tasakaalustatud kohalikult või kaugelt (sisse- või väljaminev likviidsus), kas kanalid on sulgemisel või avamisel ja kui palju bitcoini hoitakse on-chain Lightning sõlmel.

![image](assets/en/42.webp)

### Lightning Teenused

See on nähtav ainult siis, kui lightning on aktiivne.

Lisaks oma Lightning saldo nägemisele BTCPay Serveri armatuurlaual, näevad administraatorid ka Lightning Teenuste plaati. Siin saavad administraatorid leida kiirnuppe tööriistadele, mida nad kasutavad oma Lightning sõlme haldamiseks; näiteks Ride the Lightning on üks standardtööriistadest BTCPay Serveris Lightning sõlme haldamiseks.

![image](assets/en/43.webp)

### Hiljutised Tehingud

Hiljutiste tehingute plaat näitab teie poe kõige hiljutisemaid tehinguid. Ühe klõpsuga saab BTCPay Serveri instantsi administraator nüüd näha viimast tehingut ja kontrollida, kas see vajab tähelepanu.

![image](assets/en/44.webp)

### Hiljutised arved

Hiljutiste arvete plaat näitab teie BTCPay Serveri poolt genereeritud 6 viimast arvet, sealhulgas staatus ja arve summa. Plaadil on ka "Vaata kõiki" nupp, et hõlpsasti pääseda ligi täielikule arvete ülevaatele.

![image](assets/en/45.webp)

### Müügikohad ja Kogumisfondid

Kuna BTCPay Server pakub standardsete pluginate või rakenduste komplekti, on Müügikoht ja Kogumisfond BTCPay Serveri kaks peamist pluginat. Iga poe ja rahakotiga võib BTCPay Serveri kasutaja genereerida nii palju Müügikohti või Kogumisfonde, kui ta sobivaks peab. Igaüks loob uue armatuurlaua plaadi, näidates pluginate toimivust.

![image](assets/en/46.webp)

Pange tähele väikest erinevust Müügikoha ja Kogumisfondi plaadi vahel. Administraator näeb Müügikoha plaadil enim müüdud esemeid. Kogumisfondi plaadil muutub see Parimateks Perkideks. Mõlemal plaadil on kiirnupud vastava rakenduse haldamiseks ja hiljuti loodud arvete vaatamiseks enim müüdud esemete või parimate perkide järgi.

![image](assets/en/47.webp)

**!?Pane tähele!?**

Saldo graafikud ja hiljutised tehingud on saadaval ainult on-chain maksemeetodi jaoks. Teave Lightning Võrgu saldode ja tehingute kohta on töös. Alates BTCPay Serveri versioonist 1.6.0 on saadaval põhilised Lightning Võrgu saldod.

### Oskuste Kokkuvõte

Selles jaotises õppisite järgmist:

- Peamine maandumislehe paigutus, mida tuntakse kui Armatuurlaud.
- Põhiline arusaam iga plaadi sisust.

### Teadmiste Hindamise Ülevaade

Loetlege mälu järgi nii palju plaate, kui saate, Armatuurlauast.

## BTCPay Server - Poe seaded

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
BTCPay Server tarkvaras teame kahte tüüpi seadeid. BTCPay Serveri poe-spetsiifilised seaded, seadete nupp, mis asub vasakul menüüribal armatuurlaua all, ja BTCPay Serveri seaded, mis asuvad menüüriba allosas kohe konto kohal. BTCPay Serveri serveri-spetsiifilisi seadeid saavad vaadata ainult serveri administraatorid.
Poe seaded koosnevad mitmest vahekaardist, et kategoriseerida iga seadete kogum.

- Üldine
- Hinnad
- Kassa välimus
- Juurdepääsutõendid
- Kasutajad
- Rollid
- Veebikonksud
- Maksete töötlejad
- E-postid
- Vormid

### Üldine

Üldiste seadete vahekaardil seavad poe omanikud oma brändingu ja maksete vaikeväärtused. Poe esmasel seadistamisel anti poele nimi; see kajastub üldistes seadetes poe nime all. Siin saab poe omanik seada ka oma veebisaidi vastavusse brändinguga ja poe ID, et administraator saaks selle andmebaasis ära tunda.

#### Bränding

Kuna BTCPay Server on FOSS, saab poe omanik teha kohandatud brändingu, et see vastaks tema poele. Määra brändi värv, salvesta oma brändi logod ja lisa kohandatud CSS avalike/klientidele suunatud lehtedele (Arved, Maksepäringud, Tõmbemaksed)

#### Makse

Maksete seadetes saavad poe omanikud määrata oma poe vaikevaluuta (kas Bitcoinis või mis tahes fiat valuutas).

#### Luba kellelgi luua arveid

See seade on mõeldud arendajatele või ehitajatele BTCPay Serveri peal. Kui see seade on teie poe jaoks sisse lülitatud, võimaldab see välismaailmal luua arveid teie BTCPay Serveri instantsis.

#### Lisa lisatasu (võrgutasu) arvetele

BTCPay funktsioon kaupmeeste kaitsmiseks tolmurünnakute eest või klientide eest, kes võivad hiljem tekitada suuri tasusid, kui kaupmees peab korraga liigutama palju bitcoine. Näiteks lõi klient 20$ suuruse arve ja maksis selle osaliselt, makstes 1$ 20 korda, kuni arve oli täielikult makstud. Nüüd on kaupmehel suurem tehing, suurendades kaevandamiskulu, kui kaupmees otsustab hiljem neid vahendeid liigutada. Vaikimisi rakendab BTCPay arve kogusummale lisavõrgukulu, et katta see kaupmehe kulu, kui arve makstakse mitme tehinguga. BTCPay pakub mitmeid võimalusi selle kaitsefunktsiooni kohandamiseks. Võite rakendada võrgutasu:

- Ainult juhul, kui klient teeb arve eest rohkem kui ühe makse (Eelnevas näites, kui klient lõi 20\$ suuruse arve ja maksis 1\$, on arve kogusumma nüüd 19\$ + võrgutasu. Võrgutasu rakendatakse pärast esimest makset)
- Iga makse puhul (kaasa arvatud esimene makse, meie näites oleks kogusumma kohe 20\$ + võrgutasu, isegi esimese makse puhul)
- Ära kunagi lisa võrgutasu (keelab võrgutasu täielikult)

Kuigi see kaitseb tolmutehingute eest, võib see ka negatiivselt kajastuda ettevõtetes, kui seda korralikult ei suhelda. Kliendid võivad esitada lisaküsimusi ja arvata, et te neid üle laete.

#### Arve aegub, kui täielikku summat ei ole makstud pärast?

Arve taimer on vaikimisi seatud 15 minutiks. Taimer on kaitsemehhanism volatiilsuse vastu, kuna see lukustab Bitcoin'i summa vastavalt Bitcoin'i ja fiat'i kurssidele. Kui klient ei maksa arvet määratud perioodi jooksul, loetakse arve aegunuks. Arve loetakse "makstuks" kohe, kui tehing on blockchainis nähtav (0-kinnitust), kuid "lõpetatuks" siis, kui see jõuab kaupmehe määratud kinnituste arvuni (tavaliselt 1-6). Taimerit saab minutite kaupa kohandada.

#### Pea arve makstuks isegi kui makstud summa on X% väiksem kui oodatud?

Kui klient kasutab arve otse tasumiseks vahetuse rahakotti, võtab vahetus väikese tasu. See tähendab, et sellist arvet ei peeta täielikult lõpetatuks. Arve saab oleku "osaliselt tasutud". Siin saate määrata protsendimäära, kui kaupmees soovib aktsepteerida alamakstud arveid.

### Määrad

BTCPay Serveris, kui arve genereeritakse, on alati vaja kõige uuemat ja täpsemat Bitcoini ja fiat valuuta kurssi. Uue poe loomisel BTCPay Serveris palutakse administraatoritel seada eelistatud hinnallikas; pärast poe seadistamist saavad poe omanikud alati muuta oma hinnallikat selles vahekaardil.

#### Täiustatud hinnareegli skriptimine

Peamiselt kasutavad seda võimsad kasutajad. Kui see on sisse lülitatud, saavad poe omanikud luua skripte hinna käitumise ja selle üle, kuidas oma klientidelt tasu võtta.

#### Testimine

Kiire testimiskoht teie eelistatud valuutapaaridele. See hõlmab ka funktsiooni vaikimisi valuutapaaride kontrollimiseks REST päringu kaudu.

### Kassa välimus

Kassa välimuse vahekaart algab arve-spetsiifiliste seadetega ja vaikimisi maksemeetodiga ning võimaldab kindlate nõuete täitmisel spetsiifilisi maksemeetodeid.

#### Arve seaded

Vaikimisi maksemeetodid. BTCPay Server standardkonfiguratsioonis on kolm valikut.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Me saame seada parameetrid oma poele, kus klient suhtleb ainult Lightninguga, kui hind on väiksem kui X summa ja vastupidi On-chain tehingutele, kui X on suurem kui Y, esitatakse alati On-chain maksevõimalus.

![image](assets/en/48.webp)

#### Kassa

Alates BTCPay Serveri versioonist 1.7 tutvustati uut kassa liidest, Checkout V2, nagu seda nimetatakse. Kuna versioon 1.9 standardiseeriti, saavad administraatorid ja poe omanikud siiski seada kassa eelmisele väljalaskele. Kasutades lülitit "Kasuta klassikalist kassat", saab poe omanik seada poe tagasi eelmisele kassa kogemusele. BTCPay Serveril on ka valik eelseadeid veebikaubanduse või poesiseseks kogemuseks.

![image](assets/en/49.webp)

Kui klient suhtleb poega ja genereerib arve, on arvel aegumistähtaeg. Vaikimisi seab BTCPay Server selle 5 minutiks ja administraator saab selle seada mis tahes sobivaks ajaks. Kassa lehte saab veelgi kohandada, kontrollides järgmisi parameetreid:

- Tähistage makset konfetiga
- Näita poe päist (nimi ja logo)
- Näita nuppu "Maksa rahakotis"
- Ühtlusta on-chain ja off-chain maksete URL-id/QR-koodid
- Kuvage Lightning maksete summad Satoshi'des
- Automaatne keele tuvastamine kassas

![image](assets/en/50.webp)

Kui automaatne keele tuvastamine pole seatud, kuvab BTCPay Server vaikimisi inglise keelt. Poe omanik saab muuta seda vaikimisi oma eelistatud keeleks.

![image](assets/en/51.webp)

Klõpsake rippmenüül ja poe omanikud saavad seada kohandatud HTML pealkirja, mida kuvatakse kassa lehel.

![image](assets/en/52.webp)

Selleks, et klient teaks oma makseviisi, saab poe omanik alati nõuda, et kasutajad valiksid oma eelistatud maksemeetodi. Kui arve on tasutud, võimaldab BTCPay Server kliendil naasta veebipoodi. Poe omanikud saavad seada selle ümbersuunamise pärast kliendi makset automaatselt.

![image](assets/en/53.webp)

#### Avalik kviitung

Avaliku kviitungi seadetes saab poe omanik seada kviitungi lehed avalikuks ja näidata maksete loendit kviitungi lehel ning kviitungi QR-koodi, et klient saaks seda digitaalselt hõlpsasti kasutada.
![pilt](assets/en/54.webp)

### Juurdepääsutõendid

Juurdepääsutõendid on kasutusel teatud e-kaubanduse integratsioonide või kohandatud integratsioonide paaristamiseks.

![pilt](assets/en/55.webp)

### Kasutajad

Poe kasutajad on need, kus poe omanik saab hallata oma töötajate kontosid ja nende juurdepääsu poele. Pärast töötajate kontode loomist saab poe omanik lisada teatud kasutajad poele külaliskasutajate või omanikena. Töötaja rolli täpsemaks määratlemiseks vaadake järgmist jaotist „BTCPay Serveri poe seaded - Rollid“.

![pilt](assets/en/56.webp)

### Rollid

Poe omanik võib leida, et kasutaja standardrollid ei ole piisavalt olulised. Kohandatud rollide seadetes saab poe omanik määratleda iga rolli täpsed vajadused oma äris.

(1) Uue rolli loomiseks klõpsake nuppu "+ Lisa roll".

![pilt](assets/en/57.webp)

(2) Sisestage rolli nimi, näiteks "Kassapidaja".

![pilt](assets/en/58.webp)

(3) Seadistage rolli individuaalsed õigused.

- Muuda oma poode.
- Halda oma poodidega seotud vahetuskontosid.
  - Vaata oma poodidega seotud vahetuskontosid.
- Halda oma tõmbemakseid.
- Loo tõmbemakseid.
  - Loo kinnitamata tõmbemakseid.
- Muuda arveid.
  - Vaata arveid.
  - Loo arve.
  - Loo arveid oma poodidega seotud välgu sõlmedest.
- Vaata oma poode.
  - Vaata arveid.
  - Vaata oma maksepäringuid.
  - Muuda poodide veebikonkse.
- Muuda oma maksepäringuid.
  - Vaata oma maksepäringuid.
- Kasuta oma poodidega seotud välgu sõlmi.
  - Vaata oma poodidega seotud välgu arveid.
  - Loo arveid oma poodidega seotud välgu sõlmedest.
- Deponeeri vahendeid oma poodidega seotud vahetuskontodele.
- Võta vahendeid oma poodide vahetuskontodelt välja.
- Kauple oma poe vahetuskontodel olevate vahenditega.

Kui roll on loodud, on nimi fikseeritud ja seda ei saa muutmise režiimis muuta.

![pilt](assets/en/59.webp)

### Veebikonksud

BTCPay Serveris on uue "Veebikonksu" loomine üsna lihtne. BTCPay Serveri poe seadete - Veebikonksude vahekaardil saab poe omanik hõlpsasti luua uue veebikonksu, klõpsates nupul "+ Loo Veebikonks". Veebikonksud võimaldavad BTCPay Serveril saata HTTP-sündmusi, mis on seotud teie poega, teistele serveritele või e-kaubanduse integratsioonidele.

![pilt](assets/en/60.webp)

Nüüd olete veebikonksu loomise vaates. Veenduge, et teate oma Payload URL-i ja kleepige see oma BTCPay Serverisse. Kui olete Payload URL-i kleepinud, kuvatakse selle all veebikonksu saladus. Kopeerige veebikonksu saladus ja esitage see lõpp-punktis. Kui kõik on seadistatud, saate BTCPay Serveris lubada automaatse uuesti saatmise. Me üritame ebaõnnestunud saatmist uuesti teha pärast 10 sekundit, 1 minutit ja kuni 6 korda pärast 10 minutit. Saate vahetada iga sündmuse vahel või määrata oma vajadustele vastavad sündmused. Veenduge, et veebikonks on lubatud ja vajutage selle salvestamiseks nuppu Lisa veebikonks.

![pilt](assets/en/61.webp)

Veebikonksud ei ole mõeldud ühilduma Bitpay API-ga. BTCPay Serveris on kaks eraldi IPN-i (BitPay terminites: "Kohene Makseteavitused").

- Webhookp
- Teavitused

Kasutage teavituste URL-i ainult siis, kui loote arveid Bitpay API kaudu.

### Maksete Töötlejad

Maksetöötlejad töötavad koos maksete töötlemise kontseptsiooniga BTCPay Serveris. Maksete koondaja võimaldab mitu tehingut korraga saata. Maksetöötlejate abil saab poe omanik automatiseerida koondatud makseid. BTCPay Server pakub kahte meetodit automatiseeritud maksete jaoks, On-chain ja Off-chain (LN).
Poe omanik saab klõpsata ja seadistada mõlemad maksetöötlejad eraldi. Poe omanik võib soovida käivitada On-chain töötleja iga X tunni järel, samas kui Off-chain võib minna iga paari minuti tagant. On-chain puhul võite seada ka sihtmärgi, millisesse plokki see peaks lisatama. Vaikimisi on see seatud 1-le (või järgmisele saadaolevale plokile). Pane tähele, et Off-chain maksetöötleja seadistamisel on ainult intervalli taimer ja ploki sihtmärki pole. Lightning Networki maksed on kohesed.

![image](assets/en/62.webp)
![image](assets/en/63.webp)

Poe omanikud saavad seadistada On-chain töötleja ainult siis, kui nende poele on ühendatud Hot-wallet.

![image](assets/en/64.webp)

Pärast maksetöötleja seadistamist saate selle kiiresti eemaldada või muuta, naastes BTCPay Serveri poe seadistuste juurde maksetöötleja vahekaardile.

**!?Märkus!?**

Maksetöötleja On-chain - Onchain maksete töötleja saab töötada ainult poes, mis on seadistatud ühendusega Hot wallet'iga. Kui Hot wallet pole ühendatud, ei oma BTCPay Server rahakoti võtmeid ja ei saa makseid automaatselt töödelda.

### E-kirjad

BTCPay Server saab kasutada e-kirju teavituste jaoks või, kui see on õigesti seadistatud, kaotatud paroolidega kontode taastamiseks, kuna standardina BTCPay Server ei saada e-kirja, kui parool on kadunud, näiteks.

![image](assets/en/65.webp)

Enne kui poe omanik saab seadistada e-kirja reegleid, mis käivituvad tema poe kindlatel sündmustel, peame seadistama mõned põhilised e-kirja seaded. BTCPay Server vajab neid seadeid, et saata e-kirju sündmuste kohta, mis põhinevad teie poel või parooli lähtestamiseks.

BTCPay Server tegi selle teabe sisestamise lihtsamaks, kasutades "Kiirtäitmise" valikut:

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Kiirtäitmise valiku kasutamisel täidab BTCPay Server SMTP serveri ja pordi väljad eelnevalt; nüüd peab poe omanik täitma ainult oma volitused e-posti aadressi, sisselogimise (mis on tavaliselt võrdne teie e-posti aadressiga) ja parooli väljadel. BTCPay Serveri e-kirja seadetes pakutav edasijõudnute valik on TLS-sertifikaadi turvakontrollide keelamine; vaikimisi on see lubatud.

![image](assets/en/66.webp)

E-kirja reeglitega saab poe omanik seada kindlad sündmused, mis käivitavad e-kirju kindlatele e-posti aadressidele.

- Arve Loodud
- Arve Sai Makse
- Arve Töötlemisel
- Arve Aegunud
- Arve Lahendatud
- Arve Kehtetu
- Arve Makse Lahendatud

Kui klient on andnud e-posti aadressi, saavad need käivitajad saata teavet ka kliendile. Poe omanikud saavad eelnevalt täita Teema rea, et selgitada, miks see e-kiri saadeti ja mis käivitaja selle põhjustas.

![image](assets/en/67.webp)

### Vormid

Kuna BTCPay Server ei kogu andmeid, võib poe omanik soovida lisada oma kassakogemusele kohandatud vormi; nii saab poe omanik koguda lisateavet oma kliendilt. BTCPay Serveri vormiehitaja koosneb kahest osast, visuaalsest ja keerukamast koodivaatest vormidele.
Uue vormi loomisel avab BTCPay Server uue akna, paludes põhiinfot selle kohta, mida soovite oma uue vormiga küsida. Alguses peab poe omanik andma oma uuele vormile selge nime, seda nime EI saa pärast määramist muuta.
![image](assets/en/68.webp)

Pärast seda, kui poe omanik on vormile nime andnud, võib ta samuti lülitada "Luba vorm avalikuks kasutamiseks" sisse, ja see muutub roheliseks. See on selleks, et vormi saaks kasutada igas kliendile suunatud kohas. Näiteks, kui poe omanik loob 1 eraldi arve, mitte läbi oma Müügikoha, võib ta siiski soovida koguda infot kliendilt; see lüliti sisselülitamine võimaldab seda infot koguda.

![image](assets/en/69.webp)

Iga vorm algab vähemalt 1 uue vormiväljaga. Poe omanik saab valida, milline välja tüüp peaks olema;

- Tekst
- Number
- Parool
- E-post
- URL
- Telefoninumbrid
- Kuupäev
- Peidetud väljad
- Väljade grupp
- Tekstiala avatud kommentaaride jaoks.
- Valiku valija

Iga tüüp tuleb koos oma parameetritega, mida täita. Poe omanik saab seda oma soovi järgi seadistada. Esimese loodud välja all saavad poe omanikud lisada sellele ühele vormile uusi välju.

![image](assets/en/70.webp)

#### Edasijõudnud kohandatud vormid

BTCPay Server võimaldab teil ka vorme koodis ehitada. Eelkõige JSON. Toimetaja vaatamise asemel saavad poe omanikud klõpsata koodi nupul kohe toimetaja kõrval ja siseneda oma vormide koodi. Välja definitsioonis saab määrata ainult järgmised väljad; väljade väärtused salvestatakse arve metaandmetesse:

| Väli                  | Kirjeldus                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | Kui tõene, peab .value olema määratud vormi definitsioonis ja kasutaja ei saa välja väärtust muuta. (näide: vormi definitsiooni versioon)                                                                                                                                                                                                                                                                                      |
| .fields.type          | HTML sisendi tüüp tekst, raadio, märkeruut, parool, peidetud, nupp, värv, kuupäev, datetime-local, kuu, nädal, aeg, e-post, number, vahemik, otsing, url, valik, tel                                                                                                                                                                                                                                                           |
| .fields.options       | Kui .fields.type on valik, valitavate väärtuste loend                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.options.text  | Selle valiku jaoks kuvatav tekst                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.options.value | Välja väärtus, kui see valik on valitud                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.type=fieldset | Loob HTML väljade grupi ümber laste .fields.fields (vt allpool)                                                                                                                                                                                                                                                                                                                                                                |
| .fields.name          | Välja JSON omaduse nimi, nagu see ilmub arve metaandmetes                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.value         | Välja vaikimisi väärtus                                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.required      | kui tõene, on väli nõutav                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.label         | Välja silt                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.helpText      | Lisatekst välja selgitamiseks.                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.fields        | Võite oma väljad korraldada hierarhias, lubades alamväljadel olla arve metaandmete sees pesastatud. See struktuur aitab teil paremini korraldada ja hallata kogutud teavet, muutes selle kättesaadavamaks ja tõlgendatavamaks. Näiteks, kui teil on vorm, mis kogub kliendi teavet, võite grupeerida väljad ülemvälja alla, mida nimetatakse kliendiks. Selle ülemvälja all võite omada alamvälju nagu nimi, Email ja aadress. |

Välja nimi esindab JSON-i omaduse nime, mis salvestab kasutaja poolt pakutud väärtuse arve metaandmetes. Mõned tuntud nimed võivad tõlgendada ja muuta arve seadeid.

| Välja nimi       | Kirjeldus    |
| ---------------- | ------------ |
| invoice_amount   | Arve summa   |
| invoice_currency | Arve valuuta |

Võite arve välju automaatselt eeltäita, lisades vormi URL-ile päringustringid, nagu "?your_field=value".

Siin on mõned kasutusjuhud selle funktsiooni jaoks:

- Kasutaja sisendi abistamine: Eeltäitke väljad teadaoleva kliendi teabega, et muuta neil vormi täitmine lihtsamaks. Näiteks, kui te juba teate kliendi e-posti aadressi, võite eeltäita e-posti välja, et säästa nende aega.
- Personaliseerimine: Kohandage vormi kliendi eelistuste või segmentatsiooni põhjal. Näiteks, kui teil on erinevad klienditasemed, võite vormi eeltäita asjakohaste andmetega, nagu nende liikmetase või konkreetsed pakkumised.
- Jälgimine: Jälgige kliendi külastuste allikat kasutades peidetud välju ja eeltäidetud väärtusi. Näiteks, võite luua linke eeltäidetud utm_media väärtustega iga turunduskanali jaoks (nt Twitter, Facebook, Email). See aitab analüüsida teie turundustegevuste efektiivsust.
- A/B testimine: Eeltäitke väljad erinevate väärtustega, et testida erinevaid vormi versioone, võimaldades optimeerida kasutajakogemust ja konversioonimäärasid.

### Oskuste Kokkuvõte

Selles jaotises õppisite järgmist:

- Vahelehtede paigutus ja funktsioonid Poe Seadistustes
- Mitmekesised valikud aluseks olevate vahetuskursside, osaliste maksete, väikeste alamaksete ja muu peenhäälestamiseks.
- Kohandage kassas välimust, sealhulgas hinna-sõltuv peamise ahela vs. Lightning lubamine arvetel.
- Halda poe juurdepääsu tasemeid ja õigusi erinevate rollide vahel.
- Seadista automaatseid e-maile ja nende käivitajaid
- Looge kohandatud vorme, et koguda kassas lisakliendi teavet.

### Teadmiste Hindamine

#### KA Ülevaade

Mis vahe on Poe Seadistustel ja Serveri Seadistustel?

#### KA Hüpoteetiline

Kirjeldage mõningaid valikuid, mida võiksite valida Kassa Välimus > Arve Seaded all, ja miks.

## BTCPay Server - Serveri seaded

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server koosneb kahest erinevast seadete vaatest. Üks on pühendatud Poe seadistustele ja teine Serveri seadistustele. Viimane on saadaval ainult kui olete Serveri administraator ja mitte poe omanikele. Serveri administraatorid saavad lisada kasutajaid, luua kohandatud rolle, seadistada e-posti serverit, määrata poliitikaid, teostada hooldustoiminguid, kontrollida BTCPay Serveriga seotud kõiki teenuseid, üles laadida faile serverisse või kontrollida Logisid.

### Kasutajad

Nagu eelnevas osas mainitud, saavad Serveri Administraatorid kutsuda kasutajaid oma serverisse, lisades nad Kasutajate vahelehele.

### Serveri laiused kohandatud Rollid

BTCPay Server tunneb kahte sorti kohandatud rolle, poe-spetsiifilised kohandatud rollid ja serveri-laiused Kohandatud rollid BTCPay Serveri seadetes. Mõlemad hoiavad sarnast õiguste komplekti; siiski, kui seadistatud läbi BTCpay Serveri Seaded - Rollide vahelehe, rakendub määratud roll serveri-laiuselt ja kehtib mitmele poele. Märkige "Serveri-laiune" silt kohandatud rollidele Serveri seadetes.

### Serveriülesed kohandatud rollid

Serveriüleste kohandatud rollide õiguste komplekt:

- Muuda oma poode.
- Halda oma poodidega seotud vahetuskontosid.
  - Vaata oma poodidega seotud vahetuskontosid.
- Halda oma tõmbemakseid.
  - Loo tõmbemakseid.
  - Loo kinnitamata tõmbemakseid.
- Muuda arveid.
  - Vaata arveid.
  - Loo arve.
  - Loo arveid oma poodidega seotud välgu sõlmedest.
- Vaata oma poode.
  - Vaata arveid.
  - Vaata oma maksepäringuid.
  - Muuda poodide veebikonkse.
- Muuda oma maksepäringuid.
  - Vaata oma maksepäringuid.
- Kasuta oma poodidega seotud välgu sõlmi.
  - Vaata oma poodidega seotud välgu arveid.
  - Loo arveid oma poodidega seotud välgu sõlmedest.
- Deponeeri vahendeid oma poodidega seotud vahetuskontodele.
- Võta vahendeid oma poodide vahetuskontodelt välja.
- Kauple vahenditega oma poodide vahetuskontodel.

**!?Pane tähele!?**

Kui roll on loodud, on nimi fikseeritud ja seda ei saa muuta redigeerimisrežiimis.

### E-post

Serveriüleste e-posti seaded näevad välja sarnased poodidele spetsiifiliste e-posti seadetega. Siiski, see seadistus hõlmab mitte ainult poodide või administraatori logide jaoks mõeldud käivitajaid. See e-posti seadistus võimaldab ka parooli taastamist BTCPay Serveris sisselogimisel. See töötab sarnaselt poodidele spetsiifiliste seadetega; administraatorid saavad kiiresti sisestada oma e-posti parameetrid ja sisestada oma e-posti volitused ning server saab nüüd e-kirju saata.

### Poliitikad

BTCPay Serveri poliitika administraatorid saavad seada mõningaid sätteid teemadel nagu Olemasolevate Kasutajate seaded, Uute Kasutajate Seaded, Teavituste seaded ja Hoolduse seaded. Need on mõeldud uute kasutajate registreerimiseks administraatorina või tavaliste kasutajatena või isegi BTCPay Serveri peitmine otsingumootoritest, lisades need oma serveri päisesse.

#### Olemasolevate kasutajate seaded

Siin saadaolevad valikud on eraldi kohandatud rollidest. Need lisavolitused võivad muuta poe või poe omaniku rünnakutele haavatavaks. Poliitikad, mis võivad olemasolevatele kasutajatele lisada:

- Lubada mitte-administraatoritel kasutada oma poodides sisemist välgu sõlme.
  - See võimaldaks poe omanikel kasutada serveri administraatori välgu sõlme ja seega tema vahendeid! Olge ettevaatlik, see ei ole lahendus välgu juurdepääsu andmiseks.
- Lubada mitte-administraatoritel luua oma poodidele kuumi rahakotte.
  - See võimaldaks kõigil teie BTCPay Serveri eksemplari kontoga isikutel luua kuumi rahakotte ja salvestada nende taastamise seemet administraatori serveris. See võib muuta administraatori vastutavaks kolmandate osapoolte vahendite hoidmise eest!
- Lubada mitte-administraatoritel importida oma poodidele kuumi rahakotte.
  - Sarnaselt eelmise teemaga kuumade rahakottide loomisest, lubab see poliitika importida kuuma rahakoti, samade ohtudega, mis mainitud kuumade rahakottide loomise jaotises.

#### Uute kasutajate seaded

Me saame seada mõned olulised sätted uute kasutajate serverisse tuleku haldamiseks. Me saame seada kinnituse e-kirja uute registreerimiste jaoks, keelata uute kasutajate loomise sisselogimisekraanil ja piirata mitte-administraatorite juurdepääsu kasutajate loomisele API kaudu.

- Nõuda registreerimisel kinnituse e-kirja.
  - Serveri administraator peab olema seadistanud e-posti serveri!
- Keelata uute kasutajate registreerimine serveris
- Keelata mitte-administraatoritel juurdepääs kasutajate loomise API lõpp-punktile.

Vaikimisi on BTCPay Server keelanud uute kasutajate registreerimise ja lülitanud välja mitte-administraatorite juurdepääsu kasutajate loomise API lõpp-punktile. See on turvalisuse aspektist, kus ükskõik milline juhuslik isik, kes võib leida teie serveri BTCPay sisselogimise, ei saa hakata kontosid looma.

#### Teavituste Seaded

![image](assets/en/76.webp)

#### Hooldusseaded

BTCPay Server on avatud lähtekoodiga projekt, mis asub GitHubis. Iga kord, kui BTCPay Server avaldab tarkvara uue versiooni, saavad administraatorid teate, et uus versioon on saadaval. Administraatorid võivad soovida ka takistada otsingumootoritel (google, yahoo, duckduckgo) BTCPay Serveri domeeni indekseerimast. Kuna BTCPay Server on FOSS, võivad arendajad üle maailma soovida luua uusi funktsioone; BTCPay Serveril on eksperimentaalne funktsioon, mille sisselülitamisel saab administraator kasutada tootmiseks veel mitte mõeldud funktsioone, puhtalt testimise eesmärgil.

- Kontrollige GitHubis väljalaskeid ja teavitage, kui uus BTCPay Serveri versioon on saadaval.
- Takistage otsingumootoritel selle saidi indekseerimist
- Luba eksperimentaalsed funktsioonid.

![image](assets/en/77.webp)

#### Pluginad

BTCPay Server võib lisada pluginaid ja laiendada oma funktsioonide komplekti. Pluginad laaditakse vaikimisi BTCPay Serveri plugin-builder repositooriumist. Administraator võib siiski soovida näha pluginaid eelväljalaske olekus ja kui plugina arendaja seda lubab, saab serveri administraator nüüd installida pluginate beetaversioone.

![image](assets/en/78.webp)

##### Kohandamise Seaded

Standardne BTCPay Serveri paigaldus on kättesaadav domeeni kaudu, mis on selle jaoks seadistatud installimisel. Serveri administraator saab siiski muuta juurdomeeni ja kuvada ühte loodud rakendustest kindlast poest. Serveri administraator saab ka kaardistada kindlad domeenid kindlatele rakendustele.

- Kuvage rakendus veebisaidi juurtes
  - Kuvab võimalike rakenduste loendi, mida näidata juurdomeenis.

![image](assets/en/79.webp)

- Kaardista kindlad domeenid kindlatele rakendustele.
  - Kui klõpsate kindla domeeni seadistamiseks kindlatele rakendustele, saab administraator seadistada nii palju domeene, kui vaja, suunatuna kindlatele rakendustele.

![image](assets/en/80.webp)

#### Blokiahelauurijad

BTCPay Server tuleb standardina mempool.space'iga kui oma tehingute blokiahelauurijaga. Kui BTCPay Server genereerib uue arve ja sellele on seotud tehing, saab poe omanik klõpsata, et avada tehing; BTCPay Server suunab standardina mempool.space'i kui blokiahelauurija; serveri administraator võib selle muuta oma eelistuse järgi.

![image](assets/en/81.webp)

### Teenused

BTCPay Serveri seadete: Teenuste vaheleht on ülevaade komponentidest, mida teie BTCPay Server kasutab. Teie BTCPay Serveri poolt pakutavad teenused võivad sõltuda paigaldusmeetodist.

BTCPay Serveri administraator saab klõpsata "Vaata teavet" iga teenuse taga, et see avada ja seadistada kindlaid sätteid.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay teeb LND gRPC teenuse väliseks kasutamiseks kättesaadavaks; siit leiate ühenduse teabe selle konkreetse seadete menüüs; siin on loetletud ühilduvad rahakotid. BTCPay Server annab ka QR-koodi ühenduse loomiseks, mida saab skannida ja rakendada mobiilirahakotis.

Serveri administraatorid saavad avada rohkem detaile, et näha;

- Hosti üksikasjad
- SSL kasutamine
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay teeb LND REST teenuse väliseks kasutamiseks kättesaadavaks; siit leiate ühenduse teabe; siin on loetletud ühilduvad rahakotid. Ühilduvate rahakottide hulka kuuluvad Joule, Alby ja ZeusLN. BTCPay Server annab QR-koodi ühenduse loomiseks, mida saab skannida ja rakendada ühilduvas rahakotis.

- REST Uri
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### LND Seemne Varundamine

LND seemne varundamine on kasulik, et taastada vahendid teie LND rahakotist, juhul kui teie Server korrumpub. Kuna Lightning node on Hot-wallet, leiate konfidentsiaalse seemne informatsiooni sellelt lehelt.

LND dokumenteerib taastamisprotsessi. Vaadake dokumentatsiooni aadressil https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md.

#### Ride The Lightning

Ride the Lightning on Lightning node haldamise tööriist, mis on loodud avatud lähtekoodiga tarkvarana. BTCPay Server kasutab RTL-i kui Lightning node haldamise komponenti oma tarkvarapakis. BTCPay Serveri administraatorid pääsevad RTL-ile ligi Serveri seadete - Teenuste vahelehe kaudu või klõpsates Lightning rahakotil.

#### Täisnode P2P

Serveri administraatorid võivad soovida ühendada oma Bitcoin node mobiilse rahakotiga. See leht avalikustab informatsiooni, kuidas ühenduda kaugelt teie täisnode'iga P2P protokolli kaudu. Selle raamatu kirjutamise hetkel loetleb BTCPay Server Blockstream Greeni ja Wasabi rahakoti ühilduvate rahakottidena. BTCPay Server annab ühenduse jaoks QR-koodi, skannige ja rakendage ühilduvas rahakotis.

#### Täisnode RPC

See leht avalikustab informatsiooni, kuidas ühenduda kaugelt teie täisnode'iga RPC protokolli kaudu.

#### SSH

SSH-d kasutatakse hoolduse eesmärgil. BTCPay Server näitab esialgset ühenduskäsku, et jõuda teie Serverini ja SSH avalikke võtmeid, mis on volitatud ühenduma teie Serveriga. Serveri administraatorid võivad soovida välja lülitada SSH muudatused läbi BTCPay Serveri UI.

#### Dünaamiline DNS

Dünaamiline DNS võimaldab teil omada stabiilset DNS-i nime, mis osutab teie Serverile, isegi kui teie IP-aadress regulaarselt muutub. See on soovitatav, kui hostite BTCPay Serverit kodus ja soovite oma Serverile juurdepääsuks selge nime domeeni.

Pange tähele, et peate korrektselt seadistama oma NAT-i ja BTCPay Serveri paigalduse, et saada HTTPS sertifikaat.

### Teema

BTCPay Server tuleb standardina kahe teemaga: Hele ja Tume režiimid. Neid saab vahetada, klõpsates vasakus alanurgas Kontol ja lülitades Tume teema või Hele teema vahel. BTCPay Serveri administraatorid võivad lisada oma teema, pakkudes kohandatud CSS-teemat.

Administraatorid saavad laiendada Hele/Tume teemat, lisades oma kohandatud CSS-i või seades oma kohandatud teema täielikuks kohanduseks.

![pilt](assets/en/83.webp)

#### Serveri Bränding

Serveri administraatorid saavad muuta BTCPay Serveri brändingut, seadistades oma ettevõtte Serveri-ülese brändingu. Kuna BTCPay Server on FOSS, saavad serveri administraatorid tarkvara valge sildiga märgistada ja muuta välimust, et see sobiks nende äriga.

![pilt](assets/en/84.webp)

### Hooldus

Serveri administraatorina ootavad teie kasutajad, et hoolitsete Serveri eest hästi. BTCPay Serveri Hoolduse vahelehel saab admin teha mõningaid olulisi hooldustoiminguid. Seadistage domeeninimi BTCPay Serveri instantsile, Taaskäivitage või puhastage Server. Võib-olla kõige tähtsam, käivitage uuendused.

BTCPay Server on avatud lähtekoodiga projekt ja uuendab tihti. Iga uus väljalase teatatakse kas teie BTCPay Serveri teavituste kaudu või ametlikel kanalitel, mille kaudu BTCPay Server suhtleb.

![pilt](assets/en/85.webp)

#### Domeeninimi

Pärast BTCPay Serveri seadistamist võib administraator soovida muuta oma algset Domeeni. Hoolduse vahelehel saab administraator Domeeni muuta. Pärast kinnitamise klõpsamist ja sobivate DNS-kirjete seadistamist Domeenil, uuendab ja taaskäivitab BTCPay Server, et naasta uuele Domeenile.

![pilt](assets/en/86.webp)

#### Taaskäivitus

Taaskäivitage BTCPay Server ja sellega seotud teenused.

![pilt](assets/en/87.webp)

#### Puhastus

BTCPay Server töötab Dockeri komponentidega; uuendustega võib jääda üle Dockeri pilte, ajutisi faile jne. Serveri administraatorid saavad seda koristada ja oma keskkonnas ruumi tagasi võita, käivitades puhastusskripti.
![image](assets/en/88.webp)

#### Uuendamine

Võib-olla kõige olulisem valik Hoolduse vahekaardil. BTCPay Server on ehitatud kogukonna poolt ja seetõttu on selle uuendustsüklid sagedasemad kui enamikul tarkvaratoodetel. Kui BTCPay Serveril on uus väljalase, teavitatakse administraatoreid nende teavituste keskuses. Uuendamise nupule vajutades kontrollib BTCPay Server GitHubist viimast väljalaset, uuendab Serverit ja taaskäivitab selle. Enne uuendamist soovitatakse serveri administraatoritel alati lugeda läbi väljalaske märkmed, mis on jaotatud läbi BTCPay Serveri ametlike kanalite.

![image](assets/en/89.webp)

### Logid

Probleemiga silmitsi seismine pole kunagi lõbus. See dokument selgitab kõige tavalisemat töövoogu ja samme, et tõhusalt tuvastada oma probleem ja lahendada see ise või kogukonna abiga.

Probleemi tuvastamine on kriitilise tähtsusega.

#### Probleemi kordamine

Esmalt ja kõige tähtsamalt, proovige kindlaks teha, millal probleem esineb. Proovige probleemi korrata. Proovige oma Serverit uuendada ja taaskäivitada, et kontrollida, kas suudate oma probleemi taasesitada. Kui see kirjeldab teie probleemi paremini, tehke ekraanipilt.

##### Serveri uuendamine

Kontrollige oma BTCPay Serveri versiooni, kui see on palju vanem kui BTCPay Serveri [viimane versioon](https://github.com/btcpayserver/btcpayserver/releases). Serveri uuendamine võib probleemi lahendada.

##### Serveri taaskäivitamine

Serveri taaskäivitamine on lihtne viis paljude kõige levinumate BTCPay Serveri probleemide lahendamiseks. Võib olla vajalik SSH kaudu oma Serverisse sisse logida, et seda taaskäivitada.

##### Teenuse taaskäivitamine

Mõnede probleemide puhul võib olla vajalik taaskäivitada ainult teatud teenus teie BTCPay Serveri paigutuses. Näiteks lets encrypt konteineri taaskäivitamine SSL-sertifikaadi uuendamiseks.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Kasutage docker ps, et leida mõne teise teenuse nimi, mida soovite taaskäivitada.

#### Logide läbivaatamine

Logid võivad pakkuda olulist teavet. Järgnevates lõikudes kirjeldame, kuidas saada logi teavet BTCPay erinevate osade kohta.

##### BTCPay logid

Alates v1.0.3.8 saate hõlpsasti juurdepääsu BTCPay Serveri logidele esiküljelt. Kui olete serveri administraator, minge Serveri seaded > Logid ja avage logifail. Kui te ei tea, mida konkreetne viga logides tähendab, mainige seda tõrkeotsingu käigus.

Kui soovite üksikasjalikumaid logisid ja kasutate Dockeri paigutust, saate vaadata konkreetsete Dockeri konteinerite logisid kasutades käsurida. Vaadake neid [juhiseid ssh kasutamiseks](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) BTCPay instantsi sisse logimiseks, mis töötab VPS-is.

Järgmisel lehel on üldine nimekiri konteinerite nimedest, mida kasutatakse BTCPay Serveris.

Käivitage allpool toodud käsud, et printida logid konteineri nime järgi. Asendage konteineri nimi, et vaadata teiste konteinerite logisid.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Logid        | Konteineri nimi                   |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker

LND logidele juurdepääsemiseks Dockeri kasutamisel on mitu võimalust. Esiteks logige sisse kui root:

```bash
sudo su -
Liikuge õigesse kausta:
cd btcpayserver-docker
# Leia konteineri name:
<partId>6f124f36-b51c-5e53-a734-08fb1f20db25</partId>
docker ps
Prindi logid konteineri nime järgi:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Alternatiivina võite logid kiiresti printida kasutades konteineri ID-d (vajalik on ainult esimesed unikaalsed ID tähemärgid, nagu kaks kõige vasakpoolsemat tähemärki):

```bash
docker logs 'lisa oma konteineri ID'
```

Kui mingil põhjusel on vaja rohkem logisid

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Näete midagi sellist

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Pakitud logidele juurdepääsemiseks kasutage `cat lnd.log` või kui soovite mõnda teist, kasutage `cat lnd.log.15`.

Kompressitud logidele `.gzip` formaadis juurdepääsemiseks kasutage `gzip -d lnd.log.16.gz` (sel juhul pääseme ligi `lnd.log.16.gz`). See peaks andma teile uue faili, kus saate teha `cat lnd.log.16`. Kui eelnev ei tööta, võib teil olla vaja esmalt installida gzip, kasutades `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Leia c-lightning konteineri ID.
<partId>8f12e767-13df-5bc4-85e4-00e227091300</partId>
docker logs 'lisa oma konteineri ID siia'
```

alternatiivina kasutage seda

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Logi informatsiooni saate ka c-lightning cli käsu abil.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Bitcoin Node Logid

Lisaks oma Bitcoind konteineri [logide vaatamisele](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) saate kasutada ka ükskõik millist [bitcoin-cli käsku](https://developer.bitcoin.org/reference/rpc/index.html)

[(avaneb uues aknas)](https://developer.bitcoin.org/reference/rpc/index.html), et saada teavet oma bitcoin node'ist. BTCPay sisaldab skripti, mis võimaldab teil oma Bitcoin node'iga hõlpsalt suhelda.

btcpayserver-docker kaustas, saate oma node'i kasutades blockchaini teavet:

```bash
bitcoin-cli.sh getblockchaininfo
```

### Failid

BTCPay Server kasutab kohalikku failisüsteemi ja võimaldab kaupluse (toote) varade, logode ja brändingute otsest üleslaadimist serverisse. Serveri failisüsteem on kättesaadav ainult serveri administraatoritele; kaupluse omanikud saavad oma logosid/brändinguid kaupluse tasandil üles laadida.
Kui serveri administraator on Failihoidla vahekaardil, on võimalik faile otse oma serverisse üles laadida või muuta failihoidla pakkujat kohalikuks failisüsteemiks või Azure Blob Storage'iks.

![image](assets/en/90.webp)

![image](assets/en/91.webp)

### Oskuste Kokkuvõte

Selles jaotises õppisite järgmist:

- Erinevus kaupluse ja serveri seadistuste vahel, eriti seoses kasutajate, rollide ja e-kirjadega
- Seada serveriülesed poliitikad Lightning või Bitcoin kuumade rahakottide kasutamiseks ja loomiseks, uute kasutajate registreerimiseks ja e-posti teavitusteks.
- Kuidas lisada kohandatud teemasid (võrreldes lihtsate heledate/tumedate valikutega, mida pakutakse) samuti luua kohandatud logosid
- Lihtsate serveri hooldusülesannete täitmine GUI kaudu
- Probleemide lahendamine, sealhulgas Dockeri konteinerite või teie sõlme üksikasjade hankimine
- Failihoidla haldamine

### Teadmiste Hindamine

#### KA Kontseptuaalne Ülevaade

Mis on rollide erinevus, mis on määratud läbi Serveri vs Kaupluse Seaded, ja kirjeldage potentsiaalset kasutust ühe eelistamiseks teise üle?

#### KA Praktiline Ülevaade

Kirjeldage mõningaid võimalikke kasutusjuhtumeid, mida Poliitikate vahekaart võimaldab.

#### KA Praktiline Ülevaade

Kirjeldage mõningaid toiminguid, mida administraator võib rutiinselt Hoolduse vahekaardil teha.

## BTCPay Server - Maksed

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Arve on dokument, mille müüja väljastab ostjale makse kogumiseks.

BTCPay Serveris esindab arve dokumenti, mis tuleb määratud ajavahemiku jooksul fikseeritud vahetuskursiga tasuda. Arvetel on aegumistähtaeg, kuna need lukustavad vahetuskursi kindlaks ajaks, et kaitsta saajat hinnakõikumiste eest.

BTCPay Serveri tuum on võime toimida Bitcoin arvete haldussüsteemina. Arve on oluline vahend saadud makse jälgimiseks ja haldamiseks.

Kui te ei kasuta sisseehitatud [Rahakotti](https://docs.btcpayserver.org/Wallet/) maksete käsitsi vastuvõtmiseks, kuvatakse kõik poe maksete kohta arvete lehel. See leht sorteerib makseid kumulatiivselt kuupäeva järgi ja on keskne osa arvete haldamiseks ja maksete tõrkeotsinguks.

![image](assets/en/92.webp)

### Üldine

#### Arvete olekud

Allpool olev tabel loetleb ja kirjeldab BTCPay's standardseid arvete olekuid ning pakub tavalisi toiminguid. Toimingud on ainult soovitused. Kasutajad määravad parima tegevuskäigu oma kasutusjuhtumi ja äri jaoks.

| Arve Olek                        | Kirjeldus                                                                                                            | Tegevus                                                                                                                                                                 |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uus                              | Tasumata, arve taimer ei ole veel aegunud                                                                            | Puudub                                                                                                                                                                  |
| Uus (osaliselt makstud)          | Makstud, mitte täies ulatuses, arve taimer ei ole veel aegunud                                                       | Puudub                                                                                                                                                                  |
| Aegunud                          | Tasumata, arve taimer on aegunud                                                                                     | Puudub                                                                                                                                                                  |
| Aegunud (osaliselt makstud) \*\* | Makstud, mitte täies summas, ja aegunud                                                                              | Võtke ühendust ostjaga, et korraldada tagasimakse või paluda neil tasuda oma võlg. Valikuliselt märkige arve lahendatuks või kehtetuks                                  |
| Aegunud (hilinenud makse)        | Makstud, täies summas, pärast arve taimeri aegumist                                                                  | Võtke ühendust ostjaga, et korraldada tagasimakse või töödelge tellimus, kui hilinenud kinnitused on aktsepteeritavad.                                                  |
| Tasutud (makstudÜle)             | Makstud rohkem kui arve summa, tasutud, saadud piisav hulk kinnitusi                                                 | Võtke ühendust ostjaga, et korraldada üle makstud summa tagastamine, või valikuliselt oodake, kuni ostja teiega ühendust võtab                                          |
| Töötlemisel                      | Makstud täies ulatuses, kuid ei ole saanud piisavat hulka kinnitusi, nagu on määratud poe seadetes                   | Võtke ühendust ostjaga, et korraldada üle makstud summa tagastamine, või valikuliselt oodake, kuni ostja teiega ühendust võtab                                          |
| Töötlemisel (makstudÜle)         | Makstud rohkem kui arve summa, ei ole saadud piisavat hulka kinnitusi                                                | Oodake, kuni tehing on tasutud, seejärel võtke ühendust ostjaga, et korraldada üle makstud summa tagastamine, või valikuliselt oodake, kuni ostja teiega ühendust võtab |
| Tasutud                          | Makstud täies ulatuses, saadud piisav hulk kinnitusi poes                                                            | Täitke tellimus                                                                                                                                                         |
| Tasutud (märgitud)               | Staatus manuaalselt muudetud tasutuks töötlemisel või kehtetu staatuselt                                             | Poe administraator on märkinud makse tasutuks                                                                                                                           |
| Kehtetu\*                        | Makstud, kuid ei ole saadud piisavat hulka kinnitusi määratud ajavahemiku jooksul poe seadetes                       | Kontrollige tehingut blockchain uurijas, kui see on saanud piisavalt kinnitusi, märkige tasutuks                                                                        |
| Kehtetu (märgitud)               | Staatus manuaalselt muudetud kehtetuks tasutud või aegunud staatuselt                                                | Poe administraator on märkinud makse kehtetuks                                                                                                                          |
| Kehtetu (makstudÜle)             | Makstud rohkem kui arve summa, kuid ei ole saadud piisavat hulka kinnitusi määratud ajavahemiku jooksul poe seadetes | Kontrollige tehingut blockchain uurijas, kui see on saanud piisavalt kinnitusi, märkige tasutuks                                                                        |

#### Arve üksikasjad

Arve üksikasjade leht sisaldab kogu informatsiooni seoses arvega.

Arve informatsioon luuakse automaatselt põhinedes arve staatusel, vahetuskursil jne. Toote informatsioon luuakse automaatselt, kui arve loodi toote informatsiooniga, nagu näiteks Point of Sale rakenduses.

#### Arvete filtreerimine

Arveid saab filtreerida kiirfiltreid kasutades, mis asuvad otsingunupu kõrval või kasutades täpsemaid filtreid, mida saab aktiveerida klõpsates (Abi) lingil lehe ülaosas. Kasutajad saavad filtreerida arveid poe, tellimuse ID, eseme ID, staatuse või kuupäeva järgi.

#### Arvete eksportimine

BTCPay Serveri arveid saab eksportida CSV või JSON formaadis. Lisainformatsiooni arvete eksportimise ja raamatupidamise kohta.

#### Arve tagastamine

Kui mingil põhjusel soovite väljastada tagastuse, saate hõlpsalt luua tagastuse arve vaatest.

#### Arvete arhiveerimine

BTCPay Serveri mitte-aadressi taaskasutamise funktsiooni tõttu on tavaline näha palju aegunud arveid teie poe arve lehel. Et neid oma vaatest peita, valige need nimekirjast ja märkige arhiveerituks. Arhiveeritud arved ei kustutata. Arhiveeritud arvele tehtud makse tuvastatakse teie BTCPay Serveris (makstudHilja staatus). Saate igal ajal vaadata poe arhiveeritud arveid, valides otsingufiltrist arhiveeritud arved.

#### Vaikimisi valuuta

Poe vaikimisi valuuta, see seati poe loomise viisardis

#### Lubage kellelgi luua arve

Peaksite selle võimaluse lubama, kui soovite lubada välismaailmal luua arveid teie poes. See võimalus on kasulik ainult siis, kui kasutate maksenuppu või kui väljastate arveid API või kolmanda osapoole HTML veebisaidi kaudu. PoS rakendus on eelautoriseeritud ja ei vaja seda võimalust lubada juhuslikul külastajal avada teie PoS pood ja luua arve.

#### Lisa lisatasu (võrgutasu) arvele

- Ainult juhul, kui klient teeb rohkem kui ühe makse arve eest
- Iga makse puhul
- Ärge kunagi lisage võrgutasu

#### Arve aegub, kui täissummat ei ole makstud pärast .. minutit.

Arve taimer on vaikimisi seadistatud 15 minutile. Taimer on kaitsemehhanism volatiilsuse vastu, kuna see lukustab krüptoraha summa vastavalt krüpto ja fiat valuutade kurssidele. Kui klient ei maksa arvet määratud ajavahemiku jooksul, loetakse arve aegunuks. Arvet peetakse "makstuks" kohe, kui tehing on blockchainis nähtav (0-kinnitustega), kuid "lõpetatuks" peetakse seda siis, kui see on saavutanud kaupmehe määratud kinnituste arvu (tavaliselt 1-6). Taimerit on võimalik kohandada.

#### Pea arvet makstuks isegi, kui makstud summa on ..% väiksem kui oodatud.

Olukorras, kus klient kasutab arve otse maksmiseks vahetuse rahakotti, võtab vahetus väikese tasu. See tähendab, et sellist arvet ei peeta täielikult lõpetatuks. Arve saab oleku "osaliselt makstud". Kui kaupmees soovib aktsepteerida alamakstud arveid, saate siin määrata protsendimäära.

### Päringud

Maksepäringud on funktsioon, mis võimaldab BTCPay poe omanikel luua pikaajalisi arveid. Vahendid makstakse maksepäringule vastavalt makse hetkel kehtivale vahetuskursile. See võimaldab kasutajatel teha makseid oma mugavuse järgi ilma kaupmehega makse hetkel vahetuskursse läbi rääkimata või kinnitamata.

Kasutajad saavad maksepäringuid tasuda osamaksetena. Maksepäring jääb kehtivaks kuni see on täielikult tasutud või kui poe omanik nõuab aegumistähtaega. Aadresse ei kasutata kunagi uuesti. Iga kord, kui kasutaja klõpsab maksmiseks, genereeritakse uus aadress, et luua maksepäringule arve.

Poe omanikud saavad printida maksepäringuid (või eksportida arve andmeid) arvestuse ja raamatupidamise jaoks. BTCPay märgib automaatselt arved maksepäringutena teie poe arveloendis.

#### Kohanda oma maksepäringuid

- Arve Summa - Määra Nõutav Maksesumma
- Denominatsioon - Näita Nõutavat Summat Fiat või Krüptorahas
- Maksete Kogus - Lubab ainult ühekordseid makseid või osamakseid
- Aegumise Aeg - Lubab makseid kuni kindla kuupäevani või ilma aegumistähtajata
- Kirjeldus - Tekstiredaktor, Andmetabelid, Fotode & Videote Lisamine
- Välimus - Värv ja Stiil CSS Teemade abil

![image](assets/en/93.webp)

#### Loo Maksepäring

Vasakus menüüs mine Maksepäring ja klõpsa "Loo Maksepäring".

![image](assets/en/94.webp)

Sisesta Päringu Nimi, Summa, Kuvatav Denominatsioon, Seotud Pood, Aegumise Aeg & Kirjeldus (Valikuline)

Vali võimalus Lubada maksjal luua arveid oma denominatsioonis, kui soovid lubada osamakseid.

Klõpsa Salvesta & Vaata, et üle vaadata oma maksepäring.

BTCPay loob maksepäringule URL-i. Jaga seda URL-i, et vaadata oma maksepäringut. Vajad mitut sama päringut? Saad kloonida maksepäringuid kasutades Kloonimise võimalust põhimenüüs.

![image](assets/en/95.webp)

**HOIATUS**

Maksepäringud on poe-põhised, mis tähendab, et iga maksepäring on loomisel seotud poega. Veendu, et sinu poega, millele maksepäring kuulub, on ühendatud rahakott.

#### Makstud Päring

Maksja ja päringu esitaja saavad vaadata maksepäringu staatust pärast makse saatmist. Staatuseks kuvatakse "Lahendatud", kui makse on täielikult laekunud. Kui makstud on ainult osaliselt, kuvatakse Tasumata Summa jääk.

![image](assets/en/96.webp)

#### Kohanda Maksepäringuid

Kirjelduse sisu saab redigeerida maksepäringu tekstiredaktori abil. Mõlemad võimalused on saadaval, kui soovid kasutada täiendavaid värviteemasid või kohandatud CSS stiilimist.
Mitte-tehnilised kasutajad saavad kasutada [bootstrap teemat](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Edasist kohandamist saab teha, lisades täiendavat CSS koodi, nagu allpool näidatud.

```css
:root {
  --btcpay-font-family-base: "Source Sans Pro", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --btcpay-primary: #7d4698;
  --btcpay-primary-accent: #59316b;
  --btcpay-body-text: #333a41;
  --btcpay-body-bg: #fff;
  --btcpay-bg-tile: #f8f9fa;
}

#mainNav {
  color: white;
  background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
  color: white;
}
```

### Pull maksete

Traditsiooniliselt jagab saaja oma Bitcoin aadressi, et teha Bitcoin makse, ja saatja saadab hiljem raha sellele aadressile. Sellist süsteemi nimetatakse Push makseks, kuna saatja algatab makse, samal ajal kui saaja võib olla kättesaamatu, surudes makse saajale.

Aga mis siis, kui rollid vahetuvad?

Mis siis, kui saatja asemel, kes surub makse, lubab saatja saajal tõmmata makse endale sobival ajal? See on Pull makse kontseptsioon. See võimaldab mitmeid uusi rakendusi, nagu:

- Tellimusteenus (kus tellija lubab teenusel tõmmata raha iga x aja tagant)
- Tagasimaksed (kus kaupmees lubab kliendil tõmmata tagasimakse raha oma rahakotti, kui nad seda sobivaks peavad)
- Aja põhine arveldamine vabakutselistele (kus töö tellija lubab vabakutselisel tõmmata raha oma rahakotti, kui aega on aruandlusel märgitud)
- Patroonlus (kus patroon lubab saajal tõmmata raha iga kuu, et jätkata nende töö toetamist)
- Automaatne müük (kus börsi klient lubab börsil tõmmata raha oma rahakotist, et müüa automaatselt iga kuu)
- Saldo väljavõtmise süsteem (kus suure mahuga teenus lubab kasutajatel taotleda väljamakseid oma saldost, teenus saab seejärel hõlpsalt kõik väljamaksed paljudele kasutajatele fikseeritud intervallidega teha)

### Väljamaksed

Väljamakse funktsionaalsus on seotud [Pull Maksetega](https://docs.btcpayserver.org/PullPayments/). See funktsioon võimaldab teil luua väljamakseid oma BTCPay's. See funktsioon võimaldab teil töödelda pull makseid (tagasimaksed, palga väljamaksed või väljavõtmised).

#### Näide 1: Tagasimakse

Alustame tagasimakse näitega. Klient on teie poest ostnud eseme, kuid kahjuks peab selle tagastama. Nad soovivad tagasimakset. BTCPay's saate luua [Tagasimakse](https://docs.btcpayserver.org/Refund/) ja anda kliendile lingi oma vahendite nõudmiseks. Kui klient on oma aadressi esitanud ja vahendid nõudnud, kuvatakse see Väljamaksetes.

Esimene staatus on Ootel Heakskiitmist. Poe töötajad saavad kontrollida, kas mitu ootab, ja pärast valiku tegemist kasutate Toimingute nuppu.

Toimingute nupu valikud

- Kinnita valitud väljamaksed
- Kinnita ja saada valitud väljamaksed
- Tühista valitud väljamaksed

Järgmine samm on Kinnita ja saada valitud väljamaksed, kuna soovime kliendile tagasimakset teha. Kontrollige kliendi aadressi, näidake summat ja kas soovite, et tasud lahutataks tagasimaksest või mitte. Kui olete kontrollid teinud, jääb üle ainult tehingu allkirjastamine.
Klient saab nüüd värskendusi Nõude esitamise lehel. Ta saab tehingut jälgida, kuna talle on antud link plokiahelavaatlejale ja tema tehingule. Kui tehing on kinnitatud ja staatus muutub Lõpetatuks.

#### Näide 2: Palk

Nüüd vaatame palga väljamakset, kuna see toimub poe seest ja mitte Kliendi taotlusel. Alus on sama; kasutatakse Tõmbemakseid. Kuid selle asemel, et luua tagasimakse, teeme me [Tõmbemakse](https://docs.btcpayserver.org/PullPayments/).

Mine oma BTCPay serveris Tõmbemaksete vahekaardile. Üleval paremal klõpsa Loo Tõmbemakse nuppu.

Nüüd oleme Väljamakse loomisel, anna sellele nimi ja soovitud summa soovitud valuutas, täida Kirjeldus, et töötaja teaks, millega on tegu. Järgmine osa on sarnane tagasimaksetega. Töötaja täidab Sihtkoha aadressi ja summa, mida ta soovib sellest Väljamaksest nõuda. Ta võib otsustada teha selle 2 eraldi nõudena, erinevatele aadressidele, või isegi osaliselt nõuda läbi välgu.

Kui ootab mitu Väljamakset, saate need partiidena allkirjastada ja välja saata. Kui allkirjastatud, liiguvad väljamaksed In progress vahekaardile ja näitavad Tehingut. Kui võrk on selle aktsepteerinud, liigub väljamakse Completed vahekaardile. Completed vahekaart on puhtalt ajaloolistel eesmärkidel. See hoiab töödeldud Väljamakseid ja tehingut, mis sellele kuulub.

### Tõmbemaksed

#### Kontseptsioon

Kui saatja seadistab Tõmbemakse, saab ta konfigureerida mitmeid omadusi:

- Tõmbenõude Nimi
- Limiidi summa
- Ühik (nagu BTC, SAT, USD)
- Maksemeetodid
  - BTC On-chain
  - BTC Off-chain
- Kirjeldus
- Kohandatud CSS
- Lõppkuupäev (valikuline Lightning Network BOLT11 jaoks)

Pärast seda saab saatja jagada tõmbemakset lingi abil saajaga, võimaldades saajal luua väljamakse. Saaja valib oma väljamakse:

- Millist maksemeetodit kasutada
- Kuhu raha saata

Kui väljamakse on loodud, arvestatakse see tõmbemakse praeguse perioodi limiidi hulka. Saatja kiidab seejärel väljamakse heaks, määrates määra, millega väljamakse saadetakse, ja jätkab maksmisega.

Saatjale pakume lihtsat viisi mitme väljamakse maksmiseks [BTCPay Sisemisest Rahakotist](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

BTCPay Server pakub täielikku API-d nii saatjale kui ka saajale, mis on dokumenteeritud teie eksemplari `/docs` lehel. (või dokumentatsiooni veebisaidil https://docs.btcpayserver.org)

Kuna meie API paljastab tõmbemaksete täieliku võimekuse, saab saatja makseid oma vajadustele vastavalt automatiseerida.

### Oskuste kokkuvõte

Selles jaotises õppisite järgmist:

- Sügav mõistmine BTCPay Serveri arvete staatustest ning nendega tehtavatest toimingutest
- Kohandage ja hallake pikendatud elueaga arvete mehhanisme, mida tuntakse kui Taotlusi.
- Lisavõimalused paindlike maksete jaoks, mida BTCPay Serveri unikaalne Tõmbemakse funktsioon avab, eriti kuidas käsitleda tagasimakseid ja palgamakseid.

### Teadmiste hindamine

#### KA Kontseptuaalne Ülevaade

Mis on mõned erinevused arvete ja maksetaotluste vahel ning mis võiks olla hea põhjus viimase kasutamiseks?

#### KA Kontseptuaalne Ülevaade

Kuidas tõmbemaksed laiendavad seda, mida tavaliselt saab teha on-chain? Kirjeldage mõningaid kasutusjuhtumeid, mida need võimaldavad.

## BTCPay Serveri Vaikimisi Pluginad

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Vaikimisi Pluginad ja Rakendused

BTCPay serveriga kaasneb standardne komplekt Pluginasid (Rakendusi), mis muudavad BTCPay Serveri e-kaubanduse makseväravaks. Lisades Point Of Sale'i, Crowdfund platvormi ja lihtsa Pay nupu, muutub BTCPay Server lihtsalt kasutusele võetavaks lahenduseks.

### Müügikoht

Üks BTCPay Serveri standardsetest Pluginatest on Müügikoht (PoS). PoS plugina abil saab poe omanik luua veebipoe otse BTCPay Serverist, poe omanik ei vaja kolmanda osapoole e-kaubanduse lahendusi veebipoe pidamiseks. Veebipõhine PoS rakendus võimaldab kasutajatel, kellel on füüsilised poed, hõlpsalt vastu võtta Bitcoini, ilma tasudeta või kolmanda osapoole sekkumiseta, otse oma rahakotti. PoSi saab kergesti kuvada tahvelarvutites või muudes veebibrauserit toetavates seadmetes. Kasutajad saavad hõlpsalt luua avakuva otsetee, et kiiresti veebirakendusele juurde pääseda.

#### Kuidas luua uut Müügikohta

BTCPay Server võimaldab poe omanikel kiiresti luua Müügikohta mitmes paigutuses. BTCPay Server mõistab, et mitte iga pood ei ole e-kaubandus, ja mitte iga pood ei ole baar või restoran, ning see tuleb mitme standardse seadistusega teie PoSi jaoks.

Kui poe omanik klõpsab vasakul menüüribal "Müügikoht", küsib BTCPay Server nüüd nime; see nimi on nähtav vasakul menüüribal. Klõpsake PoSi loomiseks nuppu Loo.

![image](assets/en/97.webp)

#### Uuendage äsja loodud Müügikohta

Pärast uue PoSi loomist on järgmine ekraan teie Müügikoha uuendamiseks ja oma poe jaoks esemete lisamiseks.

##### Rakenduse nimi

Siin teie Müügikohale antud nimi on nähtav BTCPay Serveri peamenüüs.

##### Kuvatav pealkiri

Avalikkus näeb külastades teie poodi avalikku pealkirja või nime. BTCPay Server nimetab vaikimisi teie poe "Teepoeks". Asendage see oma poe nimega.

![image](assets/en/98.webp)

#### Valige Müügikoha Stiil

BTCPay Server on võimeline kuvama oma Müügikohta mitmel viisil.

- Toodete nimekiri
  - Poevaade, kus kliendid saavad korraga osta ainult ühe toote.
- Toodete nimekiri koos ostukorviga.
  - Poevaade, kus kliendid saavad korraga osta mitu eset ja saada ostukorvi ülevaate oma ekraani paremal küljel.
- Ainult numbriklaviatuur
  - Toodete nimekirja pole, ainult numbriklaviatuur otsearvelduseks.
- Prinditav vaade (Prinditav toodete nimekiri QR-koodiga)
  - Kui te ei saa alati oma toodete nimekirja digitaalselt kuvada, vajate toodete jaoks "offline" lahendust; BTCPay Serveril on prinditav vaade, mis toimib Offline poena.

![image](assets/en/99.webp)

#### Müügikoha Stiil - Toodete nimekiri

![image](assets/en/100.webp)

#### Müügikoha Stiil - Toodete nimekiri + Ostukorv

![image](assets/en/101.webp)

#### Müügikoha Stiil - Ainult numbriklaviatuur

![image](assets/en/102.webp)

#### Müügikoha Stiil - Prinditav vaade

![image](assets/en/103.webp)

#### Valuuta

Poe omanik võib seada oma Müügikohale erineva valuuta kui tema üldine vaikimisi määratud valuuta. Poe vaikimisi valuuta täidab selle välja automaatselt.

#### Kirjeldus

Rääkige maailmale oma poest; mida te müüte ja kui palju? Kõik, mis selgitab teie poodi, läheb siia.

#### Tooted

Kui Müügipunkt on loodud, lisab standardne BTCPay Server poodi mõned esemed viitena. Iga standardse eseme muutmiseks klõpsake nuppu Muuda, et paremini mõista iga võimalikku valikut eseme jaoks.

Uue toote loomine teie poes koosneb järgmistest väljadest;

- Pealkiri
- Hind (fikseeritud, minimaalne või kohandatud)
- Pildi URL
- Kirjeldus
- Laoseis
- ID
- Osta Nupu Tekst
- Luba/Keela

Kui poe omanik on kõik uue toote väljad täitnud, klõpsake salvestamiseks ja märkate, et Müügipunkti Toodete sektsioon hakkab täituma. Veenduge alati, et salvestate ekraani paremas ülanurgas, et vältida olukorda, kus poe omanikud võivad kaotada oma edusamme toodete lisamisel.

Poe omanikud võivad kasutada ka "Toorredaktorit" oma toodete seadistamiseks. Toorredaktor nõuab JSON struktuuride põhiteadmisi.

#### Kassa

BTCPay Server võimaldab väikest Müügipunkti-spetsiifilist kassa kohandamist. Poe omanik saab seadistada teksti "Osta x eest" või küsida konkreetseid kliendiandmeid, lisades vorme.

#### Jootraha

Mitte kõik poed ei vaja oma müügil jootraha võimalust. Poe omanikud võivad selle oma poe jaoks sisse või välja lülitada, nagu nad sobivaks peavad. Kui pood kasutab jootraha võimalust, saab poe omanik määrata jootraha väljale meelepärase teksti. BTCPay Serveri jootraha töötab protsendimäära alusel. Poe omanikud saavad lisada mitu protsenti komadega eraldatult.

#### Allahindlused

Poe omanikuna võiksite kliendile kassas kohandatud allahindlust pakkuda; allahindluste lüliti muutub teie poe kassas saadaval olevaks. Siiski, see ei ole soovitatav iseteenindussüsteemide puhul.

#### Kohandatud Maksed

Kui Kohandatud Maksed on sisse lülitatud, saab klient sisestada oma määratud hinna, mis on võrdne või suurem kui poe poolt genereeritud algne arve.

#### Lisavõimalused

Pärast kõige seadistamist oma Müügipunkti jaoks, on mõned lisavõimalused alles. Poe omanikud saavad hõlpsasti oma Müügipunkti Iframe'i kaudu manustada või lisada maksenupu, mis viitab konkreetsele poe esemele. Just loodud Müügipunkti poe stiilimiseks võivad omanikud lisada kohandatud CSS-i lisavõimaluste allosas.

#### Kustuta see rakendus

Kui poe omanik soovib oma BTCPay Serverist Müügipunkti täielikult kustutada, saavad poe omanikud Müügipunkti uuendamise allosas klõpsata nupul Kustuta see rakendus, et oma Müügipunkti rakendus täielikult hävitada. Kui klõpsate "Kustuta see rakendus", küsib BTCPay Server kinnitust, paludes sisestada `DELETE` ja kinnitada klõpsates Kustuta nuppu. Pärast kustutamist naaseb poe omanik BTCPay Serveri armatuurlauale.

### BTCPay Server - Hooandja

Müügipunkti pistikprogrammi kõrval on BTCPay Serveril võimalus luua hooandja. Nagu iga teinegi Hooandja platvorm, saavad poe omanikud seada eesmärgi, luua panustele hüvesid ja seda oma vajaduste järgi kohandada.

#### Kuidas seadistada uut hooandjat

Klõpsake BTCPay Serveri vasakul menüül Hooandja pistikprogrammil, Plugin sektsiooni all. BTCPay Server nõuab nüüd Hooandjale nime; see nimi kuvatakse ka vasakul menüüribal.

#### Uuendage äsja loodud Müügipunkti

Kui rakendusele on nimi antud, on järgmine ekraan rakenduse konteksti uuendamine.

#### Rakenduse Nimi

Teie Hooandjale antud nimi kuvatakse BTCPay Serveri peamenüüs.

#### Kuvapealkiri

Pealkiri on antud avalikkusele korjanduse jaoks.

#### Slogan

Anna korjandusele üherealine tutvustus, et mõista, mille jaoks raha kogutakse.

![pilt](assets/en/107.webp)

#### Esiletõstetud Pildi URL

Igal korjandusel on oma peamine pilt, see üks banner, mida kohe ära tunned. Seda pilti saab hoida oma serveris, kui sul on Administratiivsed õigused, Administraatorid saavad üles laadida BTCPay Serveri seadete all - Failid. Kui oled Poe omanik, peab pilt olema üles laaditud veebi kolmanda osapoole hosti kaudu (näiteks imgur).

#### Tee Korjandus Avalikuks

See lüliti teeb sinu Korjanduse avalikuks ja seega nähtavaks välismaailmale. Testimise eesmärgil või kui soovid näha, kas sinu teema on õigesti rakendatud, võiksid selle ajaks, kui korjandust koostad, hoida selle seadistuse VÄLJAS.

#### Kirjeldus

Räägi maailmale oma Korjandusest, mille jaoks raha kogud? Kõik, mis selgitab sinu korjandust, läheb siia.

![pilt](assets/en/108.webp)

#### Korjanduse Eesmärk

Sea sihtmärk, kui palju peaks korjandus projekti jaoks teenima ja millises valuutas eesmärk peaks olema määratletud. Veendu, et kui sinu eesmärgid on seatud kuupäevade vahel, lisa need siht- ja lõppkuupäevad Korjanduse eesmärkide alla.

![pilt](assets/en/109.webp)

#### Hüved

Hüved aitavad sinu korjandusel palju. See on seetõttu, et hüved annavad inimestele võimaluse sinu kampaanias osaleda. Nad puudutavad nii isekaid motiive kui ka heategevuslikke motiive. Ja need võimaldavad sul pääseda ligi toetajate kulutustele, mitte ainult nende heategevuslikule rahakotile -- võid arvata, kumb on olulisem.

Uue hüve loomine koosneb järgmistest väljadest;

- Pealkiri
- Hind (fikseeritud, minimaalne või kohandatud)
- Pildi URL
- Kirjeldus
- Inventuur
- ID
- Osta Nupu Tekst
- Luba/Keela

Kui poe omanik on kõik uue loodava hüve väljad täitnud, klõpsa salvesta ja märkad, et Korjanduste jaotises on hüved nüüd nähtavad.

![pilt](assets/en/110.webp)

### BTCPay Server - Müügikoht

#### Panused

Poe omanikud saavad valida, kuidas Hüvesid kuvada, kuidas neid sorteerida või isegi teiste hüvedega võrrelda. Kuid, kui Korjanduse eesmärgid on saavutatud, võib poe omanik soovida peatada annetuste voolu sellele korjandusele. Seetõttu võib ta lülitada sisse "Ära luba täiendavaid panuseid pärast sihtmärgi saavutamist". See peatab Korjanduse annetuste vastuvõtmise.

##### Korjanduse käitumine

Korjanduse standard arvestab eesmärgi suunas ainult neid arveid, mis on loodud Korjandusega. Siiski võib olla juhtumeid, kus Poe omanik soovib, et kõik selles poes loodud arved läheksid korjanduse arvestusse.

#### Lisavõimalused kohandamiseks

BTCpay Server pakub mõningaid lisakohandamisi. Lisa helisid, animatsioone või isegi arutelulõime Korjandusele. Poe omanikud võivad samuti muuta Korjanduse välimust ja tundet, sisestades oma kohandatud CSS-i.

#### Kustuta see rakendus

Kui poe omanik soovib oma Korjanduse BTCPay Serverist täielikult kustutada, saab Korjanduse uuendamise lehe allosas klõpsata nupul “Kustuta see rakendus”, et oma Korjanduse rakendus täielikult hävitada. Kui klõpsad "Kustuta see rakendus", küsib BTCPay Server kinnitust, paludes trükkida `DELETE` ja kinnitada klõpsates Kustuta nuppu. Pärast kustutamist naaseb poe omanik BTCPay Serveri armatuurlauale.

### BTCPay Server - Maksenupp

Lihtsalt integreeritavad HTML-i ja kõrgelt kohandatavad maksenupud võimaldavad poeomanikel saada jootraha ja annetusi. BTCPay Serveri vasakus menüüribas, Plugins sektsiooni all, saavad poeomanikud klõpsata "Pay Button" ja seejärel klõpsata Enable, et luua maksenupp.

#### Üldised Seaded

Maksenupu Üldistes Seadetes saavad poeomanikud määrata

- Standardhind
- Vaikimisi Valuuta
- Vaikimisi Makseviis
  - Kasuta poe vaikimisi
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Kassa kirjeldus
- Tellimuse ID

#### Kuvamise valikud

BTCPay Serveri maksenuppu saab seadistada erinevate stiilide jaoks. Nuppudel võib olla fikseeritud või kohandatud summa, mida näidatakse kas liuguriga või pluss- ja miinuslülititega.

#### Kasuta Modaali

Maksenupu loomisel saavad poeomanikud valida selle käitumise, kui klient seda klõpsab, ja näidata seda modaalis või uuel lehel.

**!?Märkus!?**

Hoiatus: Maksenuppu tuleks kasutada ainult jootraha ja annetuste jaoks

Maksenupu kasutamine e-kaubanduse integratsioonides ei ole soovitatav, kuna kasutaja saab muuta tellimusega seotud teavet. E-kaubanduse jaoks peaksite kasutama meie Greenfield API-d. Kui see pood töötleb kommertstehinguid, soovitame enne maksenupu kasutamist luua eraldi poe.

#### Kohanda Maksenupu Teksti

Vaikimisi ütleb BTCPay Serveri maksenupp "Maksa BTCPay'ga". Poeomanikud saavad seda teksti oma soovi järgi seada ja muuta BTCPay Serveri logo oma logoks. Teksti seadmiseks kasutage "Pay Button Text" ja kleepige pildi URL "Pay Button Image URL" alla.

##### Pildi suurus

Nupus oleva pildi suurus saab olla ainult kolmes vaikimisi suuruses.

- 146x40px
- 168x46px
- 209x57px

#### Nupu Tüüp

BTCPay Server teab kolme olekut maksenupu jaoks.

- Fikseeritud Summa
  - Eelnevalt määratud hind on nupu üldistes seadetes.
- Kohandatud Summa
  - BTCPay Serveri maksenupul on + ja - lülitid kohandatud hinna seadmiseks.
  - Kohandatud summa kasutamisel palub BTCPay Server määrata Min, Max ja kui järk-järgult see peaks suurenema.
  - Nuppudele võib seada "Kasuta lihtsat sisestusstiili". See eemaldab +/- lülitid.
  - Sobita nupp joonele, kus nupp ja lülitid ilmuvad jooneliselt.
- Liugur
  - Sarnane kohandatud summaga, kuid visuaalselt erinev, kuna sellel on liugur +/- lülitite asemel.
  - Liuguri kasutamisel palub BTCPay Server määrata Min, Max ja kui järk-järgult see peaks suurenema.

**!?Märkus!?**

Maksenupu kustutamine saab teha ülaosas hoiatuse kirjelduses.

#### Makseteavitused

Serveri IPN (Instant Payment Notification) on mõeldud veebikonksude jaoks ja seda saab täita URL-iga, et postitada ostujärgseid andmeid.

#### E-posti Teavitused

Iga kord, kui makse toimub, võib BTCPay Server teavitada poeomanikku.

#### Brauseri ümbersuunamine

Kui klient on ostu lõpetanud, suunatakse ta sellele lingile, kui poeomanik on selle seadnud.

#### Täiustatud Maksenupu Valikud

Määrake täiendavad päringustringi parameetrid, mis tuleks lisada kassalehele, kui arve on loodud. Näiteks `lang=da-DK` laadiks kassalehe vaikimisi taani keeles.

#### Kasuta Rakendust Kui Lõpp-punkti

Linkige maksenupp otse ühele PoS või Crowdfund rakenduses olevale esemele enne.
Poeomanikud saavad rippmenüüst valida soovitud rakenduse; kui rakendus on valitud, saab poeomanik lisada ühendamist vajava eseme.

#### Genereeritud Kood

Kuna BTCPay Serveri maksenupp on hõlpsasti manustatav HTML, näitab BTCPay Server pärast maksenupu seadistamist allpool genereeritud koodi, mida saab kopeerida veebisaidile.

Poeomanikud saavad genereeritud koodi kopeerida oma veebisaidile ja BTCPay Serveri maksenupp on otse nende veebisaidil aktiivne.

#### Makseteated

Serveri IPN (Instant Payment Notification) on mõeldud veebihaakide jaoks ja seda saab täita URL-iga, et postitada ostuandmed.

#### E-posti Teated

Iga kord, kui makse on toimunud, saab BTCPay Server teavitada poeomanikku.

#### Brauseri ümbersuunamine

Kui klient on ostu sooritanud, suunatakse ta sellele lingile, kui poeomanik on selle seadistanud.

#### Täiustatud Maksenupu Valikud

Määrake täiendavad päringustringi parameetrid, mis tuleks lisada kassalehele pärast arve loomist. Näiteks `lang=da-DK` laadiks vaikimisi kassalehe taani keeles.

#### Kasuta Rakendust Kui Lõpp-punkti

Linkige maksenupp otse ühele esemele PoS või Crowdfund rakendustes. Poeomanikud saavad rippmenüüst valida soovitud rakenduse, kui rakendus on valitud, saab poeomanik lisada ühendamist vajava eseme.

#### Genereeritud Kood

Kuna BTCPay Serveri maksenupp on hõlpsasti manustatav HTML, näitab BTCPay Server pärast maksenupu seadistamist allpool genereeritud koodi, mida saab kopeerida veebisaidile. Poeomanikud saavad genereeritud koodi kopeerida oma veebisaidile ja BTCPay Serveri maksenupp on otse nende veebisaidil aktiivne.

### Oskuste Kokkuvõte

Selles jaotises õppisite:

- Kuidas kasutada BTCPay Serveri integreeritud PoS pistikprogrammi, et hõlpsasti luua kohandatud pood
- Kuidas kasutada BTCPay Serveri integreeritud Crowdfund pistikprogrammi, et hõlpsasti luua kohandatud crowdfund rakendus
- Kohandatud maksenupu koodi genereerimine, kasutades Pay Button pistikprogrammi

### Teadmiste Hindamine

#### KA Ülevaade

Millised on kolm sisseehitatud pistikprogrammi, mis tulevad standardina koos BTCPay Serveriga? Kirjeldage lühidalt, kuidas igaüht saab kasutada.

# BTCPay Serveri Seadistamine

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Põhiline arusaam BTCPay Serveri paigaldamisest LunaNode keskkonnas

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### BTCPay Serveri paigaldamine Hostitud Keskk. (LunaNode)

Need sammud annavad kogu vajaliku teabe BTCPay Serveri kasutamise alustamiseks LunaNodel. Tarkvara juurutamiseks on palju võimalusi.
Kõiki BTCPay Serveri üksikasju leiate aadressilt https://docs.btcpayserver.org.

#### Kust alustame?

Selles osas tutvute LunaNode kui majutusteenuse pakkujaga, õpite tundma oma BTCPay Serveri esimesi samme ja saate teada, kuidas toimida Lightning Networkiga. Pärast kõigi sammude läbimist saate käitada veebipoodi või crowdfund platvormi, mis aktsepteerib Bitcoini!

See on üks paljudest viisidest BTCPay Serveri juurutamiseks. Lugege meie dokumentatsiooni rohkemate üksikasjade saamiseks,

https://docs.btcpayserver.org.

### BTCPay Server - LunaNode juurutamine

#### LunaNode juurutamine

Esmalt minge veebilehele LunaNode.com, kus loome uue konto. Klõpsake paremas ülanurgas nuppu "Sign Up" või kasutage nende avalehel olevat "Get Started" viisardit.
![image](assets/en/111.webp)

Pärast uue konto loomist saadab LunaNode teile kinnituseks e-kirja. Kui olete konto kinnitanud, erinevalt Voltage'st, esitatakse teile kohe võimalus teie konto jääki suurendada. See saldo on vajalik serveriruumi ja majutuskulude tasumiseks.

![image](assets/en/112.webp)

#### Lisa krediiti oma LunaNode kontole

Kui olete klõpsanud "Deposit credit", saate määrata, kui palju soovite oma kontot täiendada ja kuidas soovite selle eest maksta. LunaNode ja BTCPay Server maksavad 10$USD kuni 20$USD kuus.
Võrreldes Voltage.cloud'iga, saate täieliku juurdepääsu oma Virtuaalsele Privaatserverile (VPS edaspidi) ja seega rohkem kontrolli oma serveri üle. Pärast uue konto loomist saadab LunaNode teile kinnituseks e-kirja.
Kui olete konto kinnitanud, erinevalt Voltage'st, esitatakse teile kohe võimalus teie konto jääki suurendada. See saldo on vajalik serveriruumi ja majutuskulude tasumiseks.

#### Kuidas paigaldada uut serverit?

Selles juhendis läbime seadistuse, luues API võtmete komplekti ja kasutades LunaNode'i poolt loodud BTCPay Serveri käivitajat.

Oma LunaNode'i armatuurlaual klõpsake paremas ülanurgas API. See avab uue lehe. Meil on vaja määrata ainult API võtme nimi. Ülejäänuga tegeleb LunaNode ja seda ei käsitleta selles juhendis. Klõpsake nuppu "Create API Credential".
Pärast API volituste loomist saate pika tähtede ja märkide jada. See on teie API võti.

![image](assets/en/113.webp)

#### Kuidas paigaldada uut serverit?

Nendel volitustel on 2 osa, API võti ja API ID; meil on mõlemat vaja. Enne järgmise sammu juurde liikumist avame brauseris teise vahelehe ja läheme aadressile https://launchbtcpay.lunanode.com/

Siin palutakse teil esitada oma API võti ja API ID. See on selleks, et kinnitada, et just teie seadistate seda uut serverit. API võti peaks olema endiselt avatud teie eelmises vahelehes; kui kerite tabelis allapoole, leiate API ID.

Minge tagasi lehele Launcheriga, täitke väljad oma API võtme ja ID-ga ning klõpsake jätkamiseks.

![image](assets/en/114.webp)

Järgmises etapis saate esitada domeeninime. Kui teil on juba domeen ja soovite seda kasutada BTCPay Serveri jaoks, veenduge, et lisate ka oma domeenile DNS-i kirje (nimetatakse `A` kirjeks). Kui teil pole domeeni, kasutage selle asemel LunaNode'i pakutavat domeeni (saate seda hiljem BTCPay Serveri seadetes muuta) ja klõpsake Jätka.

Lugege lisaks, kuidas seadistada või muuta BTCPay Serveri jaoks DNS-i kirjet; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Käivita BTCPay Server LunaNodel

Pärast eelnevate sammude sooritamist saame määrata kõik valikud meie uuele serverile. Siin valime toetatud valuutaks Bitcoin (BTC); saame määrata e-posti, et saada teavitusi krüpteerimissertifikaatide uuendamise kohta; see ei ole kohustuslik.
See juhend on suunatud Mainnet keskkonna (reaalmaailma Bitcoin) seadistamisele; siiski võimaldab LunaNode teil seda seadistada ka Testneti või Regtesti jaoks arenduseesmärkidel. Juhendi jaoks jätame valikuks Mainneti.

Valige oma Lightningi rakendus. LunaNode pakub kahte erinevat rakendust, LND ja Core Lightning. Selle juhendi jaoks valime LND. Mõlemas rakenduses on väikesed, kuid olulised erinevused; rohkem selle kohta soovitame lugeda põhjalikku dokumentatsiooni; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![image](assets/en/115.webp)

LunaNode pakub mitmeid Virtuaalmasina (VM) plaane. Need erinevad hinnavahemike ja serveri spetsifikatsioonide poolest. Selle juhendi jaoks piisab m2 plaanist; siiski, kui olete valinud rohkem kui ainult Bitcoini valuutaks, kaaluge vähemalt m4 kasutamist.

Kiirendage algset plokiahela sünkroniseerimist; see on valikuline ja sõltub teie vajadustest. On olemas täiustatud valikud nagu Lightningi hüüdnime seadistamine, kindla GitHubi väljalaske osutamine või SSH võtmete seadistamine; ükski neist ei ole selles juhendis käsitletud.

Pärast vormi täitmist peate klõpsama nupul Launch VM, ja LunaNode hakkab looma teie uut VM-i, millele on paigaldatud BTCPay Server. See protsess võtab paar minutit; kui teie server on valmis, annab LunaNode teile lingi teie uuele BTCPay Serverile.

Pärast loomisprotsessi klõpsake lingil oma BTCPay Serverile; siin palutakse teil luua administraatori konto.

![image](assets/en/116.webp)

### Oskuste kokkuvõte

Selles jaotises õppisite:

- Konto loomine ja rahastamine LunaNodel
- BTCPay Serveri käivitaja kasutamine oma serveri loomiseks

### Teadmiste hindamine

#### KA Kontseptuaalne Ülevaade

Kirjeldage mõningaid erinevusi BTCPay Serveri instantsi käitamisel VPS-is võrreldes konto loomisega majutatud instantsil.

## BTCPay Serveri paigaldamine Voltage keskkonda

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Tutvute hostingupakkujaga Voltage.cloud, õpite tundma esimesi samme oma BTCPay Serveri kasutamisel ja saate teada, kuidas toimida Lightning Networkiga. Pärast kõigi sammude läbimist saate käitada veebipoodi või rahastamisplatvormi, mis aktsepteerib Bitcoini!

See on üks paljudest viisidest BTCPay Serveri paigaldamiseks. Lugege lisateavet meie dokumentatsioonist,
https://docs.btcpayserver.org.

### BTCPay Server - Voltage.cloud paigaldamine

Esmalt minge veebilehele Voltage.cloud ja registreeruge uueks kontoks. Konto loomisel saate registreeruda 7-päevasele tasuta prooviperioodile. Klõpsake kas üleval paremal asuval nupul Sign Up või kasutage nende avalehel olevat valikut "Try a free 7 day trial".

![image](assets/en/117.webp)

Pärast konto loomist klõpsake oma armatuurlaual nuppu `NODES`. Kui oleme valinud Nodes ja loonud uue node, tutvustatakse meile võimalikke node'sid, mida Voltage pakub. Kuna see juhend käsitleb ka LightningNetworki, peame Voltage'is esmalt valima oma Lightningi rakenduse, enne kui loome BTCPay Serveri. Klõpsake LightningNode.

![image](assets/en/118.webp)
Siin peate valima, millist tüüpi Lightning sõlme soovite. Voltage pakub mitmeid võimalusi teie valgustusseadistuse jaoks. See erineb näiteks LunaNode'iga seadistamisel. Selle juhendi eesmärgil piisab Lite Node'ist. Lugege Voltage.cloud'is erinevuste kohta lähemalt.
![image](assets/en/119.webp)

Andke oma sõlmele nimi, seadistage parool ja hoidke seda parooli turvaliselt. Kui see parool kaob, kaotate juurdepääsu oma varukoopiatele ja Voltage ei saa seda taastada. Looge sõlm ja Voltage näitab teile edenemist. Voltage on loonud teie Lightning sõlme. Nüüd saame luua BTCPay Serveri instantsi ja pääseda otse juurde Lightning võrgule.

Klõpsake oma armatuurlaua ülaosas nuppu Nodes (Sõlmed). Siin saate seadistada järgmise osa oma BTCPay Serveri instantsist. Klõpsake "create new" (loo uus), kui olete sõlmede ülevaates. Saate sarnase ekraani nagu varem. Nüüd, Lightning Node'i asemel, valime BTCPay Serveri.

Voltage näitab teile teie BTCPay Serveri geolokatsiooni, Voltage hostib seda USA lääneosas. Siin näete ka serveri hostimise kulu. Klõpsake Loo ja andke oma BTCPay Serverile nimi. Luba Lightning ja Voltage näitab teile eelmises etapis loodud Lightning sõlme. Klõpsake Loo ja Voltage loob BTCPay Serveri instantsi.

![image](assets/en/120.webp)

Pärast loomisele vajutamist esitleb Voltage teile vaikimisi kasutajanime ja parooli. Need on sarnased teie eelmises Voltage'is seadistatud parooliga. Klõpsake nuppu Logi sisse kontole, et suunata teid oma BTCPay Serverisse.

Tere tulemast oma uude BTCPay Serveri instantsi. Kuna oleme juba loomisprotsessis Lightning'i seadistanud, näitab see teile, et Lightning on juba lubatud!

### Oskuste kokkuvõte

Selles peatükis õppisite:

- Konto loomine Voltage.cloud'is
- Sammud BTCPay Serveri käivitamiseks koos Lightning sõlmega kontol

### Teadmiste hindamine

#### KA Kontseptuaalne Ülevaade

Mis on mõned peamised erinevused Voltage'i ja LunaNode'i seadistuste vahel?

## BTCPay Serveri paigaldamine Umbreli sõlmele

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Nende sammude lõpuks saate oma kohalikus võrgus BTCPay poes vastu võtta lightning makseid. See protsess kehtib ka siis, kui käitate umbreli sõlme restoranis või ettevõttes. Kui soovite selle poe ühendada avaliku veebisaidiga, järgige edasijõudnute harjutust, et avalikustada oma umbreli sõlm avalikkusele.

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay Server - Umbreli paigaldus

Pärast seda, kui teie Umbreli sõlm on täielikult sünkroniseeritud Bitcoin'i plokiahelaga, minge Umbreli rakenduste poodi ja otsige BTCPay Serverit rakenduste alt.

![image](assets/en/122.webp)

Klõpsake BTCPay Serveril, et näha rakenduse üksikasju. Kui BTCPay Serveri üksikasjad on avatud, näitab alumine parem pool rakenduse nõuetekohaseks töötamiseks vajalikke nõudeid. Näidatakse, et see nõuab Bitcoin'i ja Lightning sõlme. Kui te pole oma Umbrelis Lightning sõlme veel installinud, klõpsake Install (Paigalda). See protsess võib võtta paar minutit.

![image](assets/en/123.webp)

Pärast oma Lightning sõlme paigaldamist:

1. Klõpsake rakenduse üksikasjades või Umbreli armatuurlaual rakendusel avatud.
2. Klõpsake seadista uus sõlm; teile kuvatakse 24 sõna teie Lightning sõlme taastamiseks.
3. Kirjutage need üles.

![image](assets/en/124.webp)
Umbrel küsib kirja pandud sõnade kinnitust. Pärast Lightning node'i seadistamist, naaske Umbreli rakenduste poodi ja otsige üles BTCPay Server. Klõpsake paigaldusnupul ja Umbrel näitab, kas nõutavad komponendid on paigaldatud ning et BTCPay Server vajab nende komponentide juurdepääsu. Paigaldamise järel klõpsake rakenduse detailide paremas ülanurgas nupul Ava või avage BTCPay Server läbi oma Umbreli armatuurlaua.
Umbrel küsib kirja pandud sõnade kinnitust.

![image](assets/en/125.webp)

**!?Pane tähele!?**

Veenduge, et hoiate neid õiges kohas, nagu varem võtmete hoidmisel õpitud.

Pärast Lightning node'i seadistamist, naaske Umbreli rakenduste poodi ja otsige üles BTCPay Server. Klõpsake paigaldusnupul ja Umbrel näitab, kas nõutavad komponendid on paigaldatud ning et BTCPay Server vajab nende komponentide juurdepääsu.

![image](assets/en/126.webp)

Paigaldamise järel klõpsake rakenduse detailide paremas ülanurgas nupul Ava või avage BTCPay Server läbi oma Umbreli armatuurlaua.

![image](assets/en/127.webp)

### Oskuste Kokkuvõte

Selles jaotises õppisite:

- Samme BTCPay Serveri paigaldamiseks Lightning funktsionaalsusega Umbreli noodil

### Teadmiste hindamine

#### KA Kontseptuaalne Ülevaade

Kuidas erineb seadistamine Umbrelil võrreldes kahe eelneva majutatud võimalusega?

# Järeldus

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Hinnake kursust
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Kursuse Järeldus

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![image](assets/en/128.webp)

Teil peaks nüüd olema üldine arusaam sellest, mis on Bitcoin, kuidas see toimib ja kuidas see saab skaleeruda teise kihi lahendustega nagu Lightning Network. Selles kursuses käsitlesime põhjalikult, kuidas igaüks saab kasutada BTCPay Serverit, alates esmasest paigaldusest kuni poe loomise ja keerulise arvete haldamiseni, et saada finantsiliselt suveräänseks isikuks või kauplejaks.

Õnnitleme kursuse lõpetamise puhul. Loodame, et teile meeldis sisu ja jätkate BTCPay Serveri kasutamist ja uurimist ning olete sama põnevil Bitcoin'i ja kasvava ehitajate ning osalejate kogukonna lubavast tulevikust nagu meiegi.

> **FOSS on paratamatu.**

### Sõnastik

| Termin                                         | Definitsioon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 51% Rünnak                                     | Teadlikult uue pikima plokkide ahela loomine, et asendada plokid plokiahelas. See võimaldab teil asendada tehinguid, mis on kaevandatud plokiahelasse. Sellist rünnakut on kõige lihtsam teostada, kui teil on enamus kaevandamisvõimsusest, mistõttu seda nimetatakse ka "Enamusrünnakuks" või "51% Rünnakuks".                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| AccountKey                                     | Konto võti ümberbaasimiseks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AccountKeyPath                                 | Tee juurest konto võtmeni, mida eelneb peamise avaliku võtme sõrmejälje eesliide.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Aadress                                        | Bitcoin'i aadressid kodeerivad kompaktselt vajaliku teabe makse saajale tasumiseks. Kaasaegne aadress koosneb tähtede ja numbrite jadast, mis algab bc1-ga ja näeb välja nagu bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Aadress on lühend saaja lukustusskriptist, mida saatja saab kasutada vahendite saajale üleandmiseks. Enamik aadresse esindab kas saaja avalikku võtit või mingit skripti, mis määratleb keerukamaid kulutamistingimusi. Eelnev näide on bech32 aadress, mis kodeerib tunnistajaprogrammi, lukustades vahendid avaliku võtme räsi (Vaata Pay-to-Witness-Public-Key-Hash). On ka vanemaid aadressiformaate, mis algavad 1 või 3-ga ja kasutavad Base58Check aadressikodeeringut avaliku võtme räside või skripti räside esindamiseks.        |
| Aadressi Tüüp                                  | Aadress võib esindada mitmeid erinevaid skripte. Aadressid kodeeritakse ja eeldatakse, et edastada nende skripti tüüp. Pärandaadressid kasutavad Base58 ja kui pärandaadress on avaliku võtme räsi, siis nimetatakse seda P2PKH aadressiks, mis algab ‘1’-ga. Harvemini on pärandaadress skripti räsi, sel juhul algab see ‘3’-ga. Praegu kodeeritakse kõik SegWit aadressid Bech32-s ja algavad eesliitega ‘bc1’.                                                                                                                                                                                                                                                                                                                                                   |
| Rakendus                                       | BTCPay Serveril on pistikprogrammid, mis võivad toimida iseseisva rakendusena.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BIP 329                                        | Rahakoti siltide eksport/import                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BIP49                                          | Määratleb HD rahakottide tuletamisskeemi, kasutades P2WPKH-nested-in-P2SH (BIP 141) serialiseerimisvormingut eraldatud tunnistajate tehingute jaoks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Bitcoin Aadress                                | Tähtnumbriline jada, kuhu saadate oma bitcoini, nii et see "elab" nüüd seal. On identifikaator, mis koosneb umbes 33 tähest ja numbrist. Praeguses protokolli versioonis algab aadress 1, 3 või b-ga. Saaja aadressi omamine on bitcoini tehingu alustamiseks vajalik osa. Bitcoin'i aadresse genereeritakse avalikest võtmetest ja ühest võtmekomplektist saab genereerida mitu aadressi, et parandada privaatsust. Bitcoin'i aadressid toimivad nagu e-posti aadressid, kui soovite saata sõnumi, peate teadma, kuhu see läheb, sama on bitcoini puhul. Enne bitcoini tehingu saatmist peate veenduma, et saaja aadress on täpne, kuna bitcoini tehingud on pöördumatud ja võite saata bitcoini aadressile, mis ei kuulu saajale.                                  |
| bitcoin versus Bitcoin                         | Bitcoin on rahaline võrgustik ja bitcoin (väiketähtedega) on rahaline üksus Bitcoin'i võrgustikus. Kasutate bitcoini valuutat või žetooni tehingute tegemiseks Bitcoin'i võrgustikus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Plokk                                          | Plokk on Bitcoin'i plokiahelas andmestruktuur, mis koosneb päisest ja Bitcoin'i tehingute kehast. Plokile on märgitud ajatempel ja see kinnitab konkreetset eelkäijat (vanemplokki). Kui plokki päist räsida, annab see töötõendi, mis muudab plokiahela tõenäoliselt muutumatuks. Plokid peavad järgima võrgukonsensuse poolt kehtestatud reegleid, et laiendada plokiahelat. Kui plokk lisatakse plokiahelasse, peetakse kaasatud tehinguid esimeseks kinnituseks.                                                                                                                                                                                                                                                                                                 |
| Plokiuurija                                    | Veebipõhine tööriist, mis võimaldab otsida reaalajas ja ajaloolist teavet plokiahela kohta, sealhulgas andmeid plokkide, tehingute, aadresside ja muu kohta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ploki Hash                                     | Ploki hash on ploki andmete SHA-256 räsi ja seda esitatakse tavaliselt kuueteistkümnendsüsteemis. Ploki hash'i võib tõlgendada väga suure arvuna. Selleks, et rahuldada Proof-of-Work nõuet, peab ploki hash olema teatud lävendist madalam. Seega algavad kõik ploki hash'id nullide seeriaga, millele järgneb tähtnumbriline jada. Mõnedel plokkidel võib olla kuni kakskümmend juhtivat nulli, samas kui varasematel plokkidel võib olla nii vähe kui kaheksa. Nullide nõutav arv näitab ligikaudselt kaevandamise raskust ploki avaldamise ajal.                                                                                                                                                                                                                 |
| Ploki Kõrgus                                   | Iga plokk on nummerdatud kasvavas järjekorras, alustades nullist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Ploki Autasu                                   | Koosneb ploki toetusest (uusloomatud bitcoin) ja kõikide plokis sisalduvate tehingute tehingutasude summast.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ploki Suurus                                   | Igal plokil on piiratud hulk andmeid, mida see mahutada saab. Andmed, mis ei mahtunud teatud plokki, salvestatakse ühes järgnevatest plokkidest. Bitcoin'i plokkidel oli varem ploki suurus 1mb, kuid pärast pehmet haru saab ploki suurus tehniliselt mahutada kuni 4mb andmeid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Ploki Toetus                                   | Iga plokis loodud uus bitcoin. Iga toodetud ja plokiahelasse lisatud plokk võimaldab ploki loojal luua teatud hulga uut bitcoini. Toetus algas 50 BTC-ga ploki kohta ja väheneb iga 210 000 ploki ehk umbes iga nelja aasta järel poole võrra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Plokiahel                                      | Jaotatud logi ehk andmebaas kõigist Bitcoin'i tehingutest. Tehingud on grupeeritud eraldi uuendusteks, mida nimetatakse plokkideks, piiratud kuni 4 miljoni kaaluühikuga. Plokke toodetakse ligikaudu iga 10 minuti järel stohhastilise protsessi, mida nimetatakse kaevandamiseks, kaudu. Iga plokk sisaldab arvutuslikult intensiivset "töötõendit". Töötõendi nõue on kasutusel plokkide intervallide reguleerimiseks ja plokiahela kaitsmiseks ajaloo ümberkirjutamise rünnakute eest: ründaja peaks olemasolevat töötõendit ületama, et asendada juba avaldatud plokke, muutes iga ploki tõenäoliselt muutumatuks, kuna see on maetud järgnevate plokkide alla.                                                                                                 |
| BTCPAY Serveri Seif                            | Optimaalse tasakaalu saavutamiseks kasutusmugavuse, turvalisuse ja privaatsuse vahel on soovitatav kasutada BTCPay Serveri rahakotti koos riistvaralise rahakotiga. BTCPay Seif on loodud selleks, et sillutada tee riistvaralise rahakoti ja BTCPay Serveri vahel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Bütsantsi Kindralite Probleem                  | Mänguteooria probleem, mis kirjeldab detsentraliseeritud osapoolte raskusi konsensusele jõudmisel ilma usaldusväärse keskse osapoole toeta. Nimi pärineb stsenaariumist, kus mitu kindralit piiravad Bütsantsi. Nad on linna ümber piiranud, kuid peavad kollektiivselt otsustama, millal rünnata. Kui kõik kindralid ründavad samal ajal, võidavad nad, kuid kui nad ründavad erinevatel aegadel, kaotavad nad. Kindralitel puuduvad omavahel turvalised suhtluskanalid, kuna kõik saadetud või vastuvõetud sõnumid võivad olla Bütsantsi kaitsjate poolt pealt kuulatud või petlikult saadetud. Kuidas saavad kindralid korraldada rünnaku samal ajal?                                                                                                             |
| Tsensuur                                       | Kontroll selle üle, millist teavet saab massidele edastada. Bitcoin'i puhul on tsensuur kolmandate osapoolte võime peatada tehing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Vahetus                                        | UTXO-de osa, mis tagastatakse saatja rahakotti, tavaliselt erineva aadressi kaudu. Võrdub sisendite summaga miinus kulutatud summa ja tehingutasu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Child Pays For Parent (CPFP)                   | Tehnika, kus kasutaja kulutab madala tasumääraga kinnitamata tehingust väljundi lapse tehingus, mille tasumäär on kõrge, et julgustada kaevureid mõlemat tehingut plokki lisama.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Coinbase Transaction                           | Iga ploki esimene tehing, mis jagab ploki tasu ja tehingutasud selle kaevandanud isikule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Coincidence of Wants                           | Majandusnähtus, kus kaks osapoolt omavad eset, mida teine soovib, nii et nad vahetavad neid esemeid otse ilma rahalise vahendita.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Cold Storage                                   | Andmete haldamise viis ilma internetiühenduseta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Cold Wallet                                    | Bitcoin'i rahakoti tüüp, mis hoiab teie privaatvõtmeid turvaliselt võrguühenduseta, tavaliselt füüsilisel seadmel. Tuntud ka kui riistvararahakott, ja see kaitseb teie digitaalset bitcoini veebihäkkerite eest, kasutades välkmäluseadet, mis ei ole internetiga ühendatud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Command Line Interface (CLI)                   | Seadmega või arvutiprogrammiga suhtlemine kasutaja või kliendi käskude ja seadme või programmi vastuste kaudu tekstiridade kujul.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Commitment Transaction                         | Kohustustehing on Bitcoin'i tehing, mille mõlemad kanalipartnerid on allkirjastanud, ja mis kodeerib kanali viimase saldo. Iga kord, kui kanali kaudu tehakse või edastatakse uus makse, uuendatakse kanali saldot ja mõlemad osapooled allkirjastavad uue kohustustehingu. Oluliselt, kanalis Alice'i ja Bob'i vahel, hoiab nii Alice kui ka Bob oma kohustustehingu versiooni, mille on allkirjastanud ka teine pool. Kanali saab igal hetkel sulgeda kas Alice või Bob, kui nad esitavad oma kohustustehingu Bitcoin'i plokiahelale. Vanema (ajast aru saanud) kohustustehingu esitamist peetakse pettuseks (st protokolli rikkumiseks) Lightning Network'is ja seda võib karistada teine pool, nõudes kanalis olevad kõik vahendid endale, läbi karistustehingu. |
| Confirmation                                   | Kui tehing on plokki lisatud, on sellel üks kinnitus. Niipea, kui plokiahelas kaevandatakse veel üks plokk, on tehingul kaks kinnitust ja nii edasi. Kuus või enam kinnitust peetakse piisavaks tõendiks, et tehingut ei saa tagasi pöörata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Crowdfund (CF)                                 | BTCPay Serveri vaikimisi plugin, mis võimaldab poe omanikul hõlpsasti luua tüüpilise rahastamiskampaania veebilehe. Nad saavad hõlpsasti seada eesmärgi, luua panustamise eeliseid ja seda oma vajadustele kohandada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Cryptography                                   | Eri süsteem, kus algne sõnum muudetakse nii, et seda saavad vastu võtta ainult ettenähtud saajad                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Dashboard                                      | BTCPay Serveri keskne maandumisleht. See annab ülevaate kõigist poe tegevustest, kuvatuna mitmel kokkuvõtlikul plaadil.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Demo                                           | Viitab virtuaalsele keskkonnale, kus tarkvara demod toimuvad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Deployment                                     | Tarkvara kasutuselevõtt hõlmab kõiki tegevusi, mis muudavad tarkvarasüsteemi kasutamiseks valmis. Üldine kasutuselevõtu protsess koosneb mitmest omavahel seotud tegevusest võimalike üleminekutega nende vahel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Tuletus Tee                                    | Andmepala, mis ütleb Hierarhilise Deterministliku (HD) rahakoti, kuidas tuletada konkreetne võti võtmete puus. Tuletus teed kasutatakse Bitcoin'i standardina ja need tutvustati HD rahakottidega osana BIP 32-st.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Raskusastme Korrigeerimine                     | Raskusastme sihtmärgi kohandamine iga 2016 ploki järel (umbes kaks nädalat), et proovida tagada, et plokid kaevandataks keskmiselt iga 10 minuti järel. See loob seega plokkide vahel järjepideva aja ja võrgustikku uute bitcoinide järjepideva väljastamise (läbi ploki preemia).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Raskusastme Sihtmärk                           | Kaevandamisel kasutatav number, millest ploki räsi peab olema madalam, et plokk lisataks plokiahelale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Digitaalne Allkiri                             | Digitaalne allkiri on matemaatiline skeem digitaalsete sõnumite või dokumentide autentsuse ja terviklikkuse kontrollimiseks. Seda võib vaadelda krüptograafilise kohustusena, milles sõnum ei ole peidetud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Jagatav                                        | Kauba omadus, mida saab jagada väiksemateks osadeks ilma väärtust kaotamata. Kuna majandustehingud toimuvad sageli erinevates summas, peab valuuta olema jagatav, et seda saaks majanduses laialdaselt kasutada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Docker                                         | Tarkvara, mis pakendab tarkvara standardiseeritud üksusteks, mida nimetatakse konteineriteks, mis sisaldavad kõike, mida tarkvara vajab töötamiseks, sealhulgas teegid, süsteemitööriistad, kood ja tööaeg.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Topeltkulutamine                               | Olukord, kus õnnestub kulutada mingit summat rohkem kui üks kord. Bitcoin kaitseb topeltkulutamise eest, kontrollides, et iga plokiahelale lisatud tehing järgib konsensuse reegleid; see tähendab kontrollimist, et tehingu sisendid pole varem kulutatud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vastupidav                                     | Raha omadus, mille korral valuuta suudab säilitada oma algse oleku aja jooksul ja taluda korduvat kasutamist. Vastupidav valuuta peab suutma taluda võimalikku kahjustust.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Electrum                                       | Electrum on üks populaarsemaid Bitcoin'i rahakotte, loodud 2011. aastal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Laiendatud avalik võti (Xpub)                  | Laiendatud avalik võti, tuntud ka kui Xpub, on avalik võti, mis toimib HD rahakoti tuletatud võtmete vanemana. See Xpub on standard, mis tutvustati BIP 32-s. Rahakotid kasutavad seda kulisside taga avalike võtmete tuletamiseks. Xpub'i jagamine ei ole soovitatav vastu, teie vahendid ei ole otseselt liikumise ohus, xpub ei saa tuletada privaatvõtmeid. Xpub'i jagamise eelis võib olla näiteks BTCPay Serveris rahakogumise eesmärgil. Xpub jagatakse online vahenditega, samal ajal kui privaatvõtmed jäävad offline'is HWW-sse.                                                                                                                                                                                                                           |
| F.U.D.                                         | Lühend sõnadest Hirm, ebakindlus ja kahtlus; Tavaliselt esile kutsutud tahtlikult, et seada konkurent ebasoodsasse olukorda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Tasu                                           | Lightning Network'i kontekstis võtavad sõlmed teiste kasutajate maksete edastamise eest marsruutimistasusid. Iga sõlm saab määrata oma tasupoliitika, mis arvutatakse fikseeritud baastasu ja maksesumma sõltuva tasumäära summana. Bitcoin'i kontekstis maksab tehingu saatja kaevuritele tehingu plokki lisamise eest tehingutasu. Bitcoin'i tehingutasud ei sisalda baastasu ja sõltuvad lineaarselt tehingu kaalust, kuid mitte summast.                                                                                                                                                                                                                                                                                                                         |
| Fiat                                           | Valitsuse väljastatud valuuta, mida ei toeta kaup nagu kuld.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Finite                                         | Viitab Bitcoini piiratud pakkumisele.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Fork                                           | Protokolli või koodijupi muudatus. Forkid on tavaliselt projekti uuendamiseks tutvustatud. Avatud lähtekoodiga kogukonnas eksisteerivad forkid, kuna paljud isikud otsustavad alla laadida ja käitada sama tarkvara erinevatel aegadel ning ei uuenda alati. Kui kaks kasutajat laadivad alla ja käitavad tarkvara versiooni 1 ning ainult üks kasutaja uuendab, kui väljastatakse versioon 2, siis uuendanud kasutaja käitab versiooni 1 fork'i.                                                                                                                                                                                                                                                                                                                    |
| Funding Transaction                            | Tehing, mida kasutatakse maksekanali avamiseks. Rahastamistehingu väärtus (bitcoini vääringus) on täpselt maksekanali mahutavus. Rahastamistehingu väljund on 2-st-2 multisignatuuri skript (multisig), kus iga kanalipartner kontrollib üht võtit. Oma multisigi olemuse tõttu saab seda kulutada ainult kanalipartnerite vastastikusel nõusolekul. Lõpuks kulutatakse see ühe kohustusliku tehingu või sulgemistehingu poolt.                                                                                                                                                                                                                                                                                                                                      |
| Fungible                                       | Olemine midagi (nagu raha või kaup) sellist laadi, et üht osa või kogust võib asendada teise võrdse osa või kogusega võla tasumisel või arvelduskonto sulgemisel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Gap Limit                                      | Viitab standardsele avalike aadresside arvule, mida kontrollitakse tehingute jaoks plokiahelas, et arvutada konto jääki. Aadressil, mis ületab aadressi lõhe limiiti, saadud tehinguid ei tuvastata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Genesis Block                                  | Esimene plokk Bitcoin'i plokiahelas. Satoshi Nakamoto, Bitcoin'i looja, kaevandas Genesis ploki 3. jaanuaril 2009 ja lisas sel päeval Financial Times'i pealkirja “Chancellor on brink of second bailout for banks.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Github                                         | Platvorm ja pilvepõhine teenus tarkvaraarenduseks ja versioonikontrolliks kasutades Giti, mis võimaldab arendajatel oma koodi salvestada ja hallata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Gossip Protocol                                | LN sõlmed saadavad ja saavad teavet Lightning Network'i topoloogia kohta läbi kuulujutu sõnumite, mis vahetatakse oma eakaaslastega. Kuulujutu protokoll on peamiselt määratletud BOLT #7-s ja määratleb sõlme_teadaande, kanali_teadaande ja kanali_uuenduse sõnumite formaadi. Rämpsposti vältimiseks edastatakse sõlme teadaande sõnumeid ainult juhul, kui sõlmel on juba kanal, ja kanali teadaande sõnumeid edastatakse ainult juhul, kui kanali rahastamistehing on Bitcoin'i võrgu poolt kinnitatud. Tavaliselt ühenduvad Lightning sõlmed oma kanalipartneritega, kuid on täiesti sobiv ühenduda mis tahes muu Lightning sõlmega, et töödelda kuulujutu sõnumeid.                                                                                           |
| Gresham's Law                                  | Seadus, mis väidab, et “halb raha tõrjub välja hea”. Teisisõnu, majanduses, kus kasutusel on kaks valuutat, kulutavad inimesed halba raha, mis pidevalt devalveerub, ja hoiavad head raha, mis säilitab oma väärtuse. Seega domineerib halb raha ringluses ja igapäevastes tehingutes, samal ajal kui hea raha domineerib säästudes ja pikaajalistes investeeringutes.                                                                                                                                                                                                                                                                                                                                                                                               |
| Halving                                        | Sündmus, mis vähendab bitcoin'i väljaandmise määra poole võrra iga 210 000 ploki järel (umbes iga nelja aasta tagant).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Hard Fork                                      | Konsensuse muutus, mis ei ole tagasiühilduv. Tagasiühildumatus tekib siis, kui varem kehtetuks peetud käitumine muutub kehtivaks. Kõvade hargnemiste (hard fork) korral peavad kõik sõlmed uuendama, et säilitada konsensus. Vastasel juhul lükkavad vanad sõlmed tehingud või plokid vanade reeglite alusel tagasi kui kehtetud, samal ajal kui uuendatud sõlmed aktsepteerivad neid kui kehtivaid. Sel põhjusel välditakse Bitcoinis kõvasid hargnemisi igal võimalusel.                                                                                                                                                                                                                                                                                           |
| Hardware Wallet (HWW)                          | Eriline tüüp Bitcoin'i rahakott, mis salvestab kasutaja privaatvõtmed turvalises riistvaraseadmes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Hash Function                                  | Krüptograafiline räsifunktsioon on matemaatiline algoritm, mis kaardistab suvalise suurusega andmed kindla suurusega bitijadaks (räsi) ja on kavandatud ühesuunaliseks funktsiooniks, st funktsiooniks, mida on praktiliselt võimatu tagurpidi lahendada. Ainus viis ideaalse krüptograafilise räsifunktsiooni väljundi põhjal sisendandmeid taasluua on proovida brute-force otsingut võimalike sisenditega, et näha, kas need annavad sobiva tulemuse.                                                                                                                                                                                                                                                                                                             |
| Hash Rate                                      | Mõõdik, mis näitab, mitu räsi kaevurid Bitcoin'i võrgus sekundi jooksul kumulatiivselt toodavad. Üksik räsi on katse luua plokile Proof-of-Work.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Hot Wallet                                     | Seade, millel on välised ühendused, eriti internetiga. Hot wallet on Bitcoin'i rahakott, mis ühendub internetiga. Need rahakotid on igapäevaseks kulutamiseks mugavamad, kuid ei ole nii turvalised kui külmhoiustamise võimalused, kuna nad suhtlevad internetiga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Initial Block Download (IBD)                   | Protsess, mille käigus ehitatakse Bitcoin'i plokiahel nullist üles. Kui uus sõlm seadistatakse ja ühendub võrguga, ühendub see teiste sõlmedega ja küsib neilt plokke. Uus sõlm töötleb neid plokke ja ehitab plokiahela, kuni on jõudnud järele ja on võrguga sünkroonis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Invoice                                        | Kaubandusdokument, mille müüja väljastab ostjale seoses müügitehinguga ja mis näitab tooteid, koguseid ja toodete või teenuste eest kokkulepitud hindu, mida müüja on ostjale pakkunud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Know Your Customer (KYC)                       | Seadused, mille eesmärk on vältida finantsasutuste kasutamist ebaseaduslike rahasiirte jaoks, nõudes, et kõik finantskontod oleksid isikute või organisatsioonidega tuvastatavad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Layer 2                                        | Võrk, mis on ehitatud plokiahela peale, näiteks Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Legacy Address                                 | Legacy aadressid kasutavad Base58 ja kui legacy aadress on avaliku võtme räsi, nn P2PKH aadress, algab see ‘1’-ga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Lightning Network                              | Protokoll Bitcoin'i peal. See loob maksekanalite võrgustiku, mis võimaldab usaldusväärsete maksete edastamist võrgus HTLC-de ja sibulmarsruutimise abil. Lightning Network'i teised komponendid on kuulujutuprotokoll, transpordikiht ja maksepäringud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Liquidity                                      | Mitme omaduse mõõdik konkreetse vara tellimusraamatus antud turul. Likviidsus on näitaja, kui palju mõjutab suur tellimus vara hinda turul. Likviidsemal varal on sügavam tellimusraamatu sügavus. See tähendab, et see suudab absorbeerida rohkem tellimusi väiksemate hinnaliikumistega.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pikim Ahel                                     | Ahel plokkidest, mille ehitamiseks kulus kõige rohkem vaeva. Nimetatud nii, kuna intuitiivselt võttes on blockchain, milles on rohkem plokke, nõudnud rohkem energiat ehitamiseks kui ahel, milles on vähem plokke, kuid täpsemalt on see ahel, mille tootmiseks oli vaja rohkem tööd, seega parem nimetus oleks võinud olla "raskem ahel".                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Peamine Ahel                                   | Lightning Network'i kontekstis viitab see Bitcoin'i võrgustikule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Vahetusvahend                                  | Hea tüüp, mis hõlbustab teiste kaupade ja teenuste vahetamist majanduses. Ajalooliselt kasutati vahetusvahendina esemeid nagu kestad, helmed ja kuld.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Mempool                                        | Lühend "mälu basseinist", see on ajutine ladustamiskoht sõlme poolt vastu võetud tehingutele.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Kaevur                                         | Sõlm, mis tegeleb blockchaini ehitamisega, lisades uusi plokke läbi hashimise protsessi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Kaevandamine                                   | Protsess, mille käigus konstrueeritakse plokk hiljutistest Bitcoin'i tehingutest ja seejärel lahendatakse arvutuslik probleem, mis on vajalik töötõendina. See on protsess, mille kaudu uuendatakse jagatud bitcoin'i pearaamatut (st Bitcoin'i blockchaini) ja mille kaudu lisatakse pearaamatusse uued tehingud. Samuti on see protsess, mille kaudu emiteeritakse uus bitcoin. Iga kord, kui luuakse uus plokk, saab kaevandav sõlm uue bitcoin'i, mis on loodud selle ploki coinbase tehingus.                                                                                                                                                                                                                                                                   |
| Mitmeallkirjastamine (multisig)                | Skript, mis nõuab kulutamise autoriseerimiseks rohkem kui ühte allkirja. Maksekanalid kodeeritakse alati multisig aadressidena, mis nõuavad ühte allkirja iga maksekanali partneri poolt. Kahepoolse maksekanali standardjuhul kasutatakse 2-st-2 multisig aadressi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Sõlm                                           | Arvuti, mis osaleb võrgus. Eelkõige Bitcoin'i või Lightning võrgustikus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Väljund                                        | Bitcoinides loodud pakett bitcoin'i tehingus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Väljundi Lukk                                  | Nõuete kogum, mis on asetatud väljundile. Neid nõudeid tuleb täita, et saaks väljundit tehingus kasutada. Kõige tavalisem näide on lihtne nõue omada privaatvõtit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| P2SH Aadress                                   | P2SH aadressid on Base58Check kodeeringud 20-baidise skripti hash'ist. P2SH aadressid algavad "3"-ga. P2SH aadressid peidavad kogu keerukuse, nii et makse saatja ei näe skripti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P2WPKH Aadress                                 | "Native SegWit v0" aadressiformaat, P2WPKH aadressid on bech32-kodeeritud ja algavad "bc1q"-ga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| P2WSH Aadress                                  | "Native SegWit v0" skripti aadressiformaat, P2WSH aadressid on bech32-kodeeritud ja algavad "bc1q"-ga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Osaliselt Allkirjastatud Bitcoin Tehing (PSBT) | Bitcoin'i standard, mis hõlbustab allkirjastamata tehingute portatiivsust, mis võimaldab mitmel osapoolel lihtsalt allkirjastada sama tehingu. See on kõige kasulikum, kui mitu osapoolt soovivad lisada samale tehingule sisendeid. PSBT tutvustati BIP 174-ga ja võimaldab kasutajatel tehinguid külmladustusseadmes lihtsamalt allkirjastada ja seejärel allkirjastatud tehingu internetiühendusega seadmest edastada.                                                                                                                                                                                                                                                                                                                                            |
| Marsruudi leidmine                             | Protsess maksetee leidmiseks lähtepunktist sihtpunkti Lightning Network'is.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Makse avaliku võtme räsi (P2PKH)               | P2PKH on väljundi tüüp, mis lukustab bitcoini avaliku võtme räsi. Väljundi, mille lukustab P2PKH skript, saab avada (kulutada), esitades räsi ja digitaalse allkirja vastava era võtmega.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Makse skripti räsi (P2SH)                      | P2SH on mitmekülgne väljundi tüüp, mis võimaldab keerukate Bitcoin'i skriptide kasutamist. P2SH puhul keerukat skripti, mis täpsustab väljundi kulutamise tingimused (lunastamise skript), ei esitata lukustusskriptis. Selle asemel lukustatakse väärtus skripti räsi, mis tuleb esitada ja täita väljundi kulutamiseks.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Makse Taproot'ile (P2TR)                       | Aktiveeritud novembris 2021, Taproot on uus väljundi tüüp, mis lukustab bitcoini puu kulutamistingimustele või ühele juurtingimusele.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Makse tunnistaja avaliku võtme räsi (P2WPKH)   | P2WPKH on P2PKH SegWit'i ekvivalent, kasutades eraldatud tunnistajat. Allkiri P2WPKH väljundi kulutamiseks asetatakse tunnistaja puusse, mitte ScriptSig väljale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Makse tunnistaja skripti räsi (P2WSH)          | P2WSH on P2SH SegWit'i ekvivalent, kasutades eraldatud tunnistajat. Allkiri ja skript P2WSH väljundi kulutamiseks asetatakse tunnistaja puusse, mitte ScriptSig väljale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Payjoin                                        | Eriline Bitcoin'i tehingu tüüp, kus nii saatja kui ka saaja panustavad sisendeid, et murda ühise sisendi omandi heuristika, eeldus, mida kasutatakse bitcoin'i kasutajate privaatsuse kõrvaldamiseks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Maksekanal                                     | Finantssuhe kahe sõlme vahel Lightning Network'is, luues bitcoin'i tehingu, mis maksab multisignatuuri aadressile. Kanalipartnerid saavad kanalit kasutada bitcoin'i saatmiseks üksteisele ilma kõiki tehinguid Bitcoin'i plokiahelasse lisamata. Tüüpilises maksekanalis lisatakse plokiahelasse ainult kaks tehingut: rahastamistehing ja kohustuse tehing. Kanali kaudu saadetud makseid ei registreerita plokiahelas ja öeldakse, et need toimuvad "väljaspool ahelat".                                                                                                                                                                                                                                                                                          |
| Makse taotlus                                  | Funktsioon, mis võimaldab BTCPay poe omanikel luua pikaajalisi arveid. Makse taotlusele makstud vahendid kasutavad makse hetkel kehtivat vahetuskurssi. See võimaldab kasutajatel teha makseid oma mugavuse järgi, ilma et peaksid poe omanikuga makse hetkel vahetuskursse läbi rääkima või kinnitama.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Väljamakse                                     | Funktsionaalsus on seotud tõmbemaksetega. See funktsioon võimaldab teil töödelda tõmbemakseid (tagasimaksed, palgamaksed või väljamaksed).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Plugin                                         | Tarkvara lisand, mis on paigaldatud programmi, suurendades selle võimekust.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Müügikoha (PoS)                                | BTCPay Serveri vaikimisi plugin, mis võimaldab poe omanikul luua veebipoe otse BTCPay Serverist. Poe omanik ei vaja veebipoe käitamiseks kolmanda osapoole e-kaubanduse lahendusi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Portable                                       | Kauba võime olla hõlpsasti ruumis transporditav. Portatiivsus on heliraha oluline omadus; selleks, et raha laialdaselt omaks võetaks ja seega kasutatav oleks, peab see suutma suhtelise kergusega liikuda üle piiride, inimeste vahel ja pikkade vahemaade taha.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Proof Of Work (PoW)                            | Andmed, mille leidmine nõuab olulist arvutustööd ja mida igaüks saab hõlpsasti kontrollida, et tõestada töö hulka, mis oli selle tootmiseks vajalik. Bitcoinis peavad kaevurid leidma numbrilise lahenduse SHA-256 algoritmile, mis vastab võrguülesele sihtmärgile, mida nimetatakse raskusastme sihtmärgiks.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Pseudonym                                      | Võltsnimi, mida isikud kasutavad oma identiteedi kaitsmiseks või maine loomiseks eraldi oma tegelikust identiteedist. Avalikke võtmeid kasutatakse selleks, et Bitcoin'i kasutajad saaksid bitcoine vastu võtta, jäädes samal ajal plokiahela suhtes pseudonüümseks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Public-Key Cryptography                        | Hõlmab võtmepaari, mida tuntakse avaliku võtme ja privaatvõtmena, mis on seotud isikuga, kes peab elektrooniliselt autentima oma identiteeti või allkirjastama või krüpteerima andmeid. Avalik võti avaldatakse ja vastav privaatvõti hoitakse saladuses. Avaliku võtmega krüpteeritud andmeid saab dekrüpteerida ainult vastava privaatvõtmega.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Public/Private Key                             | Võtmepaar, mida kasutatakse avaliku võtme krüptograafias. Avalik võti jagatakse teistega avalikult ja seda võib mõelda kui kontonumbrit, samal ajal kui privaatvõti hoitakse saladuses ja seda võib mõelda kui parooli.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Pull Payment                                   | Traditsiooniliselt, et teha Bitcoin'i makse, jagab saaja oma bitcoin'i aadressi ja saatja saadab hiljem raha sellele aadressile. Sellist süsteemi nimetatakse tõukemakseks, kuna saatja algatab makse, samal ajal kui saaja võib olla kättesaamatu, surudes sisuliselt makse saajale. Tüüpilise stsenaariumi asemel, kus saatja "surub" makse, lubab saatja saajal tõmmata makse ajal, mida saaja peab sobivaks.                                                                                                                                                                                                                                                                                                                                                     |
| Rabbit Hole                                    | Viide "Alice Imedemaal", kus kangelane asub seiklusele sisenedes küülikuauku. Bitcoin'i kontekstis viitab see näiliselt lõpututele teemadele, mida üks uurib ja näeb uues valguses, kui nad on hakanud Bitcoin'i mõistma.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Receive                                        | Protsess, kus bitcoine saadetakse antud aadressile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Register                                       | Konto loomise või teenusele registreerumise protsess, mida tehakse tavaliselt kasutajanime ja parooli valimisega.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Replace By Fee (RBF)                           | Bitcoin'i tehingut saab määrata RBF-na, et võimaldada saatjal asendada see tehing teise sarnase tehinguga, mis maksab kõrgemat tasu. See mehhanism eksisteerib selleks, et kasutajad saaksid reageerida, kui võrk muutub ülekoormatuks ja tasud tõusevad ootamatult.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Repository                                     | Versioonikontrollisüsteemides on hoidla andmestruktuur, mis salvestab metaandmeid failide komplekti või kataloogistruktuuri kohta. Olenevalt sellest, kas kasutusel olev versioonikontrollisüsteem on hajutatud, nagu Git või Mercurial, või tsentraliseeritud, nagu Subversion, CVS või Perforce, võib kogu teave hoidlas olla dubleeritud iga kasutaja süsteemis või hoitakse seda ühel serveril. Mõned metaandmed, mida hoidla sisaldab, hõlmavad muu hulgas hoidla muudatuste ajaloolist arvestust, kogumit commit-objekte ja viidete kogumit commit-objektidele, mida nimetatakse peadeks.                                                                                                                                                                      |
| Rescan                                         | Protsess, mille käigus skaneeritakse praegust UTXO (Unspent Transaction Output) komplekti kuuluvate müntide olemasolu, mis kuuluvad varem konfigureeritud tuletusskeemi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Revokation Key                                 | Iga tagasivõetava järjestuse küpsuslepingu (RSMC) sisaldab kahte tühistamisvõtit. Iga kanalipartner teab ühte tühistamisvõtit. Mõlemat tühistamisvõtit teades saab RSMC väljundi kulutada etteantud ajalukus. Uue kanaliseisundi läbirääkimisel jagatakse vanad tühistamisvõtmed, sellega "tühistades" vana seisundi. Tühistamisvõtmeid kasutatakse selleks, et takistada kanalipartneritel vana kanaliseisundi levitamist.                                                                                                                                                                                                                                                                                                                                          |
| Routing                                        | Makse sooritamise protsess, kasutades Lightning Network'i teed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Routing Fees                                   | Lightning Network'is teiste kasutajate maksete edastamise eest võetavad tasud. Igal sõlmpunktil võib olla oma tasupoliitika, mis arvutatakse fikseeritud baastasu ja maksesumma sõltuva tasumäära summana.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Salability                                     | Kauba turul müümise lihtsus igal ajal, kui selle omanik soovib, minimaalse hinnakaotusega.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Satoshi (sat)                                  | Satoshi on bitcoin'i väikseim ühik (nimetus), mida saab blockchain'is registreerida. Üks satoshi on 1/100 miljondik (0.00000001) bitcoin'ist ja on nimetatud Bitcoin'i looja Satoshi Nakamoto järgi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Satoshi Nakamoto                               | Nimi, mida kasutas isik või inimeste rühm, kes kavandas Bitcoin'i ja lõi selle algse viiteimplementatsiooni. Implementatsiooni osana töötasid nad välja ka esimese blockchain'i andmebaasi. Protsessis lahendasid nad esimesena digitaalse valuuta topeltkulutamise probleemi. Nende tegelik identiteet on endiselt teadmata.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Satoshi Per Byte                               | Tehingu prioriteedi mõõtmise ühik, määratletud kui tehingu tasu satoshi'ides jagatuna tehingu suurusega baitides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Satoshi Per Verabyte                           | Sarnane mõiste nagu Satoshi Per Byte, kuid uute aadresside jaoks, mis kasutavad Segwit'i. Võrdne tehingu suurusega kaaluühikutes jagatuna 4-ga. Kaaluühikud arvutatakse, võttes tehingu suuruse (ilma tunnistajata) korrutatuna kolmega, lisades sellele tehingu suuruse koos tunnistajaga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Scarcity                                       | Kauba omadus, mida ei saa kulutusteta kopeerida. Nappus ei sõltu olemasolevate kaubaühikute arvust, vaid pigem rohkemate ühikute tootmise kulukusest.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Script                                         | Bitcoin kasutab tehingute jaoks skriptimissüsteemi nimega Bitcoin Script. See sarnaneb Forth programmeerimiskeelele, on lihtne, põhineb virnal ja töödeldakse vasakult paremale. See on tahtlikult Turingi mittetäielik, ilma tsüklite või rekursioonita.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Seed Phrase                                    | Sõnade loetelu, mis salvestab kogu vajaliku teabe Bitcoin'i vahendite taastamiseks ahelas. Rahakotitarkvara genereerib tavaliselt seemnefraasi ja juhendab kasutajat seda paberile kirjutama. Kui kasutaja arvuti läheb katki või nende kõvaketas muutub rikutuks, saavad nad sama rahakotitarkvara uuesti alla laadida ja kasutada paberist varukoopiat, et oma bitcoin'id tagasi saada.                                                                                                                                                                                                                                                                                                                                                                            |
| Segregated Witness (SegWit)                    | Segregated Witness (SegWit) on 2017. aastal Bitcoin'i protokolli tehtud uuendus, mis lisab uue tunnistaja allkirjadele ja muudele tehingu autoriseerimise tõenditele. See uus tunnistaja väli on tehingu ID arvutusest välja jäetud, mis lahendab enamiku kolmandate osapoolte tehingute muudetavuse probleeme. Segregated Witness rakendati pehme uuendusena ja on muudatus, mis tehniliselt muudab Bitcoin'i protokolli reegleid rangemaks.                                                                                                                                                                                                                                                                                                                        |
| Self-Sovereignty                               | Mudel digitaalsete identiteetide haldamiseks, milles üksikisikutel või ettevõtetel on ainuõigus oma kontode ja isikuandmete üle kontrolli omada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Send                                           | Bitcoini saatmise protsess aadressile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity Mode                               | Lülitatav poe seadetest, aktiveerimine muudab numbrilised väärtused (nt bitcoini kogus) kõigis vaadetes varjatuks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Server Settings                                | BTCPay Serveri seaded, mis kehtivad serveri laiuses (võrreldes poe seadetega, mis on piiratud ühe poe ulatuses).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SHA-256                                        | Krüptograafiline räsifunktsioon. Kuulub turvaliste räsifunktsioonide (SHA) perekonda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Shopify                                        | Kanada rahvusvaheline e-kaubanduse ettevõte, mille peakontor asub Ottawas, Ontarios. Shopify on selle ettevõtte omanduses olev e-kaubanduse platvormi nimi veebipoodidele ja jaemüügi kassasüsteemidele.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SMTP                                           | Simple Mail Transfer Protocol on internetistandardi suhtlusprotokoll elektroonilise posti edastamiseks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Soft Fork                                      | Protokolli uuendus, mis on nii edasi- kui tagasiühilduv, võimaldades nii vanadel kui uutel sõlmedel jätkata sama ahela kasutamist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Software Stack                                 | Arvutustehnikas on lahenduste kogum või tarkvarapakett tarkvaraalamsüsteemide või komponentide kogum, mis on vajalik täieliku platvormi loomiseks nii, et rakenduste toetamiseks ei ole vaja täiendavat tarkvara.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Store                                          | BTCPay Serveri pood võib olla vaadeldav kui "kodu" konkreetsele bitcoin'i rahakotile, laiendatuna kõigi BTCPay Serveri funktsioonidega.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Store Settings                                 | BTCPay Serveri poe spetsiifilised seaded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Taproot                                        | Bitcoin'i uuendus, mis tutvustaks mitmeid uusi funktsioone. Uuendus on kirjeldatud BIP-des 340, 341 ja 342 ning tutvustab Schnorr'i allkirjastamise skeemi, Taproot'i ja Tapscript'i. Koos tutvustavad need uuendused uusi, tõhusamaid, paindlikumaid ja privaatsemaid viise bitcoini ülekandmiseks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Thier's Law                                    | Seadus, mis väidab, et hea raha tõrjub välja halva raha.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Third-Party Host                               | Kui üksikisiku või ettevõtte veebisait töötab teise ettevõtte omanduses ja hallatavatel serveritel. Alternatiiviks on oma veebisaidi majutamine oma serverites oma andmekeskuses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Timelock                                       | Timelock on tüüpi piirang, mis piirab mõne bitcoini kulutamist kuni määratud tulevikuaja või ploki kõrguseni. Timelockid on olulised paljudes Bitcoin'i lepingutes, sealhulgas maksekanalites ja HTLC-des.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Topoloogia                                     | Lightning Network'i topoloogia kirjeldab Lightning Network'i kuju matemaatilise graafina. Graafi sõlmed on Lightning sõlmed (võrgu osalejad/peers). Graafi servad on maksekanalid. Lightning Network'i topoloogia on avalikult edastatud gossip protokolli abil, välja arvatud teatamata kanalid. See tähendab, et Lightning Network võib olla märkimisväärselt suurem kui teatatud kanalite ja sõlmede arv. Topoloogia tundmine on eriti huvipakkuv maksete allikapõhises marsruutimisprotsessis, kus saatja avastab marsruudi.                                                                                                                                                                                                                                     |
| Tehing                                         | Tehingud on andmestruktuurid, mida Bitcoin kasutab bitcoini ülekandmiseks ühelt aadressilt teisele. Mitu tuhat tehingut on koondatud plokki, mis seejärel salvestatakse (kaevandatakse) plokiahelasse. Iga ploki esimene tehing, mida nimetatakse coinbase tehinguks, genereerib uut bitcoini.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Tehingu ID                                     | Tähtede ja numbrite jada, mis identifitseerib plokiahelas konkreetse tehingu. Jada on lihtsalt tehingu topelt SHA-256 räsi. Seda räsi saab kasutada tehingu otsimiseks sõlmest või plokiuurijast.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Kahefaktoriline autentimine (2FA)              | Identiteedi ja juurdepääsu haldamise turvameetod, mis nõuab ressurssidele ja andmetele juurdepääsuks kahte autentimisvormi, sageli lisaks standardsele sisselogimisparoolile ka sekundaarset seadet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Tsenseerimatu                                  | Omadus, et ükski üksus ei saa bitcoini tehingut tagasi pöörata või rahakotti või aadressi musta nimekirja panna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Konfiskeerimatu                                | Omadus, et ükski üksus ei saa bitcoini võtta üksuselt vastu nende tahte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Kulutamata Tehingu Väljundid (UTXO)            | Väljundid, mida ei ole veel kulutatud, seega on need uutes tehingutes kulutamiseks saadaval.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Kasutajakogemus (UX)                           | Kuidas kasutaja suhtleb ja kogeb toodet, süsteemi või teenust. See hõlmab inimese tajusid kasulikkusest, kasutusmugavusest ja efektiivsusest.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Kasutajaliides (UI)                            | Inimese ja arvuti suhtlus- ja kommunikatsioonipunkt seadmes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verifitseeritav                                | Hea omadus, mida on lihtne eristada võltsingutest ja jäljenditest.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Virtuaalne                                     | Olek arvutis või arvutivõrgus simuleeritud või emuleeritud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Virtuaalne masin (VM)                          | Arvutustehnikas on virtuaalne masin arvutisüsteemi virtualiseerimine või emuleerimine. Virtuaalsed masinad põhinevad arvuti arhitektuuridel ja pakuvad füüsilise arvuti funktsionaalsust. Nende rakendused võivad hõlmata spetsiaalset riistvara, tarkvara või mõlema kombinatsiooni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Virtuaalne Privaatserver                       | Virtuaalne privaatserver on virtuaalne masin, mida müüakse teenusena Interneti majutusteenuse poolt. Terminil "virtuaalne pühendatud server" on sarnane tähendus. Virtuaalne privaatserver jookseb oma operatsioonisüsteemi koopiaga ja klientidel võib olla superkasutaja taseme juurdepääs sellele operatsioonisüsteemi instantsile, nii et nad saavad installida peaaegu igasuguse tarkvara, mis sellel OS-il töötab.                                                                                                                                                                                                                                                                                                                                             |
| Volatiilsus                                    | Mõõdik, mis näitab vara hinna muutuste ulatust ajas. Varad, mis kogevad regulaarselt suuri hinnamuutusi, on volatiilsemad, samas kui varad, millel on stabiilsem hind, on vähem volatiilsed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Rahakott                                       | Bitcoin'i rahakotid hoiavad kasutaja võtmeid, võimaldades kasutajatel vastu võtta bitcoine, allkirjastada tehinguid ja kontrollida oma kontoseisu. Bitcoin'i rahakotis hoitavad privaatsed ja avalikud võtmed täidavad kahte erinevat funktsiooni, kuid on loomisel omavahel seotud. Bitcoin'i rahakotid sisaldavad kasutaja võtmeid, mitte nende tegelikke bitcoine. Kontseptuaalselt on rahakott nagu võtmehoidja selles mõttes, et see hoiab paljusid privaatsete ja avalike võtmete paare. Neid võtmeid kasutatakse tehingute allkirjastamiseks, võimaldades kasutajal tõestada, et nad omavad tehingu väljundeid plokiahelas, st. nende bitcoine. Kõik bitcoinid on plokiahelas salvestatud tehingu väljundite kujul.                                           |
| Wasabi Rahakott                                | Avatud lähtekoodiga, mittehoiustav, privaatsusele keskendunud Bitcoin'i rahakott lauaarvutitele, mis rakendab usalduseta CoinJoin'i.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Ainult-Vaatamise Rahakott                      | Bitcoin'i rahakotid, mis võimaldavad teil jälgida oma bitcoine külmas hoiustamises, samal ajal keelates vahendite kulutamise võimaluse. See on seetõttu, et ainult-vaatamise rahakotid ei salvesta ega kasuta privaatvõtmeid ja seetõttu ei saa volitada ühtegi kulutust kasutaja nimel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Vaal                                           | Bitcoin'i kontekstis on vaal keegi, kes omab suurt hulka bitcoine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Valge Silt                                     | Valge sildi toode on toode või teenus, mille üks ettevõte toodab ja mida teised ettevõtted kaubamärgistavad nii, et see näib, nagu oleksid nad selle valmistanud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Valge Raamat                                   | Tutvustab uut ideed või aruteluteemat. Bitcoin'i valge raamat tutvustas Bitcoin'i kui "Eakaaslastevahelist elektroonilist sularahasüsteemi", mis "ei vajanud usaldusväärseid kolmandaid osapooli". Satoshi Nakamoto avaldas valge raamatu 31. oktoobril 2008 e-posti nimekirjas krüptograafidele ja küberpunkidele.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Pakitud Segwit                                 | Disaini rakendus, mis sisaldus SegWit'i uuenduses, mille eesmärk oli võimaldada rahakottidel ja muul Bitcoin'i tarkvaral SegWit'i lihtsamini toetada. Selle saavutamiseks kasutatakse kahte põhilist SegWit'i skripti, P2WPKH ja P2WSH, kui P2SH tehingu "lunastusskripti", andes tulemuseks pakitud SegWit'i skriptitüübid P2SH-P2WPKH ja P2SH-P2WSH vastavalt.                                                                                                                                                                                                                                                                                                                                                                                                     |

![pilt](assets/en/129.webp)

