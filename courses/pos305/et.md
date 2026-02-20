---
name: BTC Pay Serveri valdamine
goal: Kohaliku ettevõtte jaoks BTC Pay Server instantsi seadistamine
objectives:
- Mõista BTCPay Serveri rolli põhitõdesid maksete töötlemisel
- Omandada BTCPay Serveri konfigureerimisprotsessi sisemine toimimine
- Juurutada BTCPay Server pilve- ja sõlmpõhistes keskkondades
- Saada BTC Pay Serveri operaatoriks
---
# Teekond finantsilise suveräänsuse poole

Usaldus on habras, eriti kui tegemist on rahaga. See sissejuhatav kursus juhendab teid läbi BTCPay Serveri, võimsa tööriista, mis võimaldab teil vastu võtta Bitcoin'i makseid ilma kolmandatest osapooltest sõltumata. Õpite BTCPay Serveri operaatoriks saamise põhitõdesid

Alekose ja Basi loodud ning melontwisti ja asi0 kohandatud kursus paljastab, kuidas üksikisikud ja ettevõtted loovad alternatiive traditsioonilistele maksesüsteemidele. Olenemata sellest, kas olete Bitcoin'ist uudishimulik või valmis haldama ettevõtete maksetaristuid, avastate praktilisi oskusi, mis seaavad kahtluse alla olemasoleva olukorra. Valmis uurima, milline finantsiline sõltumatus tegelikult välja näeb?
+++
# Sissejuhatus


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Kursuse ülevaade


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Tere tulemast POS 305 kursusele BTCPay Serveril!


Selle koolituse eesmärk on õpetada teile, kuidas paigaldada, konfigureerida ja kasutada BTCPay Serverit oma ettevõttes või organisatsioonis. BTCPay Server on avatud lähtekoodiga lahendus, mis võimaldab teil töödelda Bitcoin makseid iseseisvalt, turvaliselt ja kulutõhusalt. See kursus on suunatud eelkõige edasijõudnud kasutajatele, kes soovivad omandada BTCPay Serveri isehostimise täieliku integreerimise oma igapäevastesse toimingutesse.


**Lõik 1: BTCPay serveri tutvustus**

Alustame BTCPay Serveri üldise tutvustamisega, sealhulgas sisselogimisekraaniga, kasutajakontode haldamisega ja uue poe loomisega. See sissejuhatus aitab teil mõista BTCPay Serveri Interface ja mõista selle tööriista kasutamise alustamiseks vajalikke põhifunktsioone.


** 2. jagu: Sissejuhatus Bitcoin võtmete kaitsmisse**

Teie Bitcoin vahendite turvalisus on väga oluline. Selles jaotises uurime krüptograafiliste võtmete genereerimist, riistvaraliste rahakottide kasutamist nende võtmete kaitsmiseks ja seda, kuidas suhelda oma võtmetega BTCPay Serveri kaudu. Samuti saate teada, kuidas konfigureerida BTCPay Server Lightning Wallet, et optimeerida oma tehinguid.


**Jagu 3: BTCPay Server Interface**

See osa juhatab teid läbi BTCPay Serveri kasutaja Interface. Saate teada, kuidas navigeerida armatuurlaual, konfigureerida kaupluse ja serveri seadeid, hallata makseid ja kasutada integreeritud pistikprogramme. Eesmärgiks on anda teile vajalikud vahendid, et kohandada oma paigaldust vastavalt teie konkreetsetele vajadustele.


**Jagu 4: BTCPay serveri konfigureerimine**

Lõpuks keskendume BTCPay Serveri praktilisele paigaldamisele erinevates keskkondades. Kas kasutate LunaNode'i, Voltage'i või Umbrel-sõlme, saate teada olulised sammud BTCPay Serveri paigaldamiseks ja konfigureerimiseks, võttes arvesse iga keskkonna eripära.


Kas olete valmis BTCPay Serverit omandama ja oma äri kasvatama? Alustame!


## Autorite Bitcoin ja BTCPay Server'i kriitiline tunnustamine


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Alustame sellest, mis on BTCPay Server ja selle päritolu. Me väärtustame läbipaistvust ja teatud standardeid, et kujundada usaldust Bitcoin ruumis.

Projekt ruumis rikkus neid väärtusi. BTCPay Serveri juhtiv arendaja Nicolas Dorier võttis seda isiklikult ja andis lubaduse need iganenuks muuta. Siin me nüüd, mitu aastat hiljem, oleme ja töötame selle tuleviku nimel, täielikult avatud lähtekoodiga, iga päev.


> See on vale, minu usaldus teie vastu on murtud, ma teen teid iganenuks.
> Nicolas Dorier

Pärast Nicolas'i sõnu oli aeg hakata ehitama. Märkimisväärne hulk tööd kulus sellele, mida me nüüd nimetame BTCPay Serveriks. Rohkem inimesi soovis sellesse jõupingutusse panustada. Kõige tuntumad on r0ckstardev, MrKukks, Pavlenex ja esimene kaupmees, kes tarkvara kasutas, astupidmoose.


Mida tähendab avatud lähtekood ja mida tähendab selline projekt?


[FOSS](https://planb.academy/resources/glossary/foss) tähendab vaba ja avatud lähtekoodiga tarkvara. Esimene viitab tingimustele, mis lubavad igaühel kopeerida, muuta ja isegi levitada tarkvara versioone (isegi kasumi saamise eesmärgil). Viimane viitab lähtekoodi avalikule jagamisele, julgustades avalikkust panustama ja täiustama.

See tõmbab ligi kogenud kasutajaid, kes on entusiastlikud panustama tarkvarasse, mida nad juba kasutavad ja millest nad saavad kasu, mis osutub lõppkokkuvõttes edukamaks vastuvõtmiseks kui patenteeritud tarkvara. See on kooskõlas Bitcoin eetosega, et "teave ihkab olla vaba" See toob kokku kirglikud inimesed, kes moodustavad kogukonna ja on lihtsalt lõbusam. Nagu Bitcoin, on ka FOSS paratamatu.


### Enne kui me alustame


See kursus koosneb mitmest osast. Paljude eest hoolitseb teie klassiõpetaja, demokeskkonnad, millele te saate juurdepääsu, hostitud server enda jaoks ja võimalik, et ka domeeninimi. Kui te läbite selle kursuse iseseisvalt, siis arvestage, et DEMO-ga tähistatud keskkonnad ei ole teile kättesaadavad.

NB. Kui te jälgite seda kursust klassiruumis, võivad serverite nimed erineda sõltuvalt teie klassiruumi ülesehitusest. Selle tõttu võivad muutujad serverite nimedes olla erinevad.


### Kursuse struktuur


Igal peatükil on eesmärgid ja teadmiste hindamine. Selles kursuses käsitleme kõiki neid ja esitame iga õppetööploki (st peatüki) lõpus kokkuvõtte põhijoontest. Illustratsioonid on esitatud visuaalse tagasiside andmiseks ja võtmemõistete tugevdamiseks visuaalses aspektis. Eesmärgid on seatud iga õppetööploki alguses. Need eesmärgid lähevad kaugemale kontrollnimekirjast. Need annavad teile juhised uute oskuste omandamiseks. Teadmiste hindamine on järk-järgult keerulisem, kui teie BTCPay serveri seadistamine on lõpule viidud.


### Mida saavad õpilased koos kursusega?


BTCPay Serveri kursuse abil saab õpilane aru Bitcoin tehnilistest ja mittetehnilistest põhiprintsiipidest. BTCPay Server'i kaudu toimuv ulatuslik koolitus Bitcoin kasutamise kohta võimaldab õpilastel kasutada oma Bitcoin infrastruktuuri.


### Olulised veebiaadressid või kontaktvõimalused


BTCPay Server Foundation, mis võimaldas Alekosel ja Basil selle kursuse kirjutada, asub Tokyos, Jaapanis. BTCPay Server Foundationiga saab ühendust loetletud veebisaidi kaudu.



- https://foundation.btcpayserver.org
- Liituge ametlike vestluskanalitega: https://chat.btcpayserver.org


## Sissejuhatus Bitcoin-sse


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Bitcoin mõistmine klassiharjutuse kaudu


See on klassiruumi harjutus, nii et kui te ise selle kursuse läbite, ei saa te seda sooritada, kuid saate selle harjutuse siiski läbi teha. Selle ülesande täitmiseks on vaja vähemalt 9-11 inimest.


Harjutus algab pärast BBC sissejuhatuse "Kuidas Bitcoin ja [Blockchain](https://planb.academy/resources/glossary/blockchain) töötab" vaatamist.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Selleks on vaja vähemalt üheksa osalejat. Selle harjutuse eesmärk on anda füüsiline arusaam Bitcoin toimimisest. Mängides iga rolli võrgus, saate interaktiivse ja mängulise õppimisviisi. See harjutus ei hõlma [Lightning Network](https://planb.academy/resources/glossary/lightning-network).


### Näide: Vajab 9 / 11 inimest


Rollid on järgmised:



- 1 klient
- 1 kaupmees
- 7 kuni 9 Bitcoin [sõlme](https://planb.academy/resources/glossary/node)


**Setup on järgmine:**


Kliendid ostavad poest toote Bitcoin-ga.


**Stsenaarium 1 - traditsiooniline pangandussüsteem**



- Asetage üles:
  - Vaata skeeme/selgitusi lisatud joonisel Figjam - [Tegevusskeem](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Hankige kolm vabatahtlikku õpilast, kes mängivad kliendi (Alice), kaupmehe (Bob) ja panga rolli.
- Mängige sündmuste jada läbi:
  - Klient - sirvib veebis kauplust ja leiab 25 dollari eest toote, mida ta soovib, ning teatab kaupmehele, et soovib seda osta
  - Kaupmees- küsib tasu.
  - Klient- saadab kaardiinfo kaupmehele
  - Kaupmees- edastab pangale teabe (nii enda kui ka isiku/andmete tuvastamine), taotledes makseid
  - Pank kogub teavet kliendi ja kaupmehe kohta (Alice ja Bob) ning kontrollib, kas kliendi saldo on piisav.
  - Alice kontolt arvatakse maha 25 \$, Bob kontole lisatakse 24 \$, teenuse eest võetakse 1 \$
  - Kaupmees saab pangalt heakskiidu ja saadab kauba kliendile.
- Kommentaarid:
  - Bob ja Alice peavad olema seotud pangaga.
  - Pank kogub identifitseerimisandmeid nii Bob kui ka Alice kohta.
  - Pank võtab osa.
  - Pangale tuleb usaldada, et see hoiab kogu aeg iga osaleja raha.


**Stsenaarium 2 - Bitcoin süsteem**



- Asetage üles:
  - Vaata skeeme/selgitusi lisatud joonisel Figjam - [Tegevusskeem](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Asendage pank üheksa õpilasega, kes mängivad arvutite (Bitcoin sõlmede/miinerite) rolli võrgus, et asendada pank.
- Igal 9 arvutil on täielik ajalooline arvestus kõigi kunagi tehtud tehingute kohta (seega täpsed saldod ilma võltsinguteta), samuti reeglistik:
  - Kontrollida, kas tehing on korralikult allkirjastatud (thekeyfitsthelock)
  - Edastab ja võtab vastu kehtivaid tehinguid võrgus olevatele eakaaslastele, viskab välja kehtetud tehingud (sealhulgas need, mis üritavad kulutada sama raha kaks korda)
- Uuenda/täienda kirjeid perioodiliselt "juhuslikust" arvutist saadud uute tehingutega, tingimusel, et kogu sisu on kehtiv (märkus: praegu ignoreerime lihtsuse huvides Proof of Work komponenti), vastasel juhul lükkame need tagasi ja jätkame nagu varem, kuni järgmine "juhuslik" arvuti saadab uuenduse
  - Kui sisu oli kehtiv, siis premeeriti õiget summat.
- Mängige sündmuste jada läbi:
  - Klient - sirvib veebis kauplust ja leiab 25 dollari eest toote, mida ta soovib, ning teatab kaupmehele, et soovib seda osta
  - Kaupmees - küsib maksmist, saates kliendile Invoice/Address oma Wallet-st.
  - Klient koostab tehingu (saadab 25 dollari väärtuses BTC-d kaupmehe poolt antud Address-le) ja edastab selle Bitcoin-võrku.
- Arvutid - võtavad tehingu vastu ja kontrollivad:
  - Address-s on vähemalt 25 dollarit BTC-d, mis saadetakse Address-st
  - Tehing on nõuetekohaselt allkirjastatud ("lahti lukustatud" kliendi poolt)
  - Kui see ei ole nii, siis tehing ei levi läbi võrgu, ja kui see on nii, siis see levib ja jääb ootele.
  - Kaupmehed saavad kontrollida, et tehing on pooleli ja ootab.
- Üks arvuti valitakse "juhuslikult" välja, et teha ettepanek kavandatava tehingu lõpuleviimiseks, edastades seda sisaldava "ploki"; kui see kontrollitakse, saavad nad BTC tasu.
  - VÕIMALIK/ARENDATUD - arvuti juhusliku valimise asemel võib simuleerida Mining, lastes arvutitel visata täringut, kuni tekib mingi etteantud tulemus (nt valitakse esimene, kes viskab kaks kuutist)
  - Samuti saab läbi mängida, mis juhtuks, kui kaks arvutit võidaksid ligikaudu üheaegselt, mille tulemuseks oleks ahelate jagunemine.
  - Arvutid kontrollivad kehtivust, ajakohastavad/lisavad kirjeid oma pearaamatusse, kui reeglid on täidetud, ja edastavad tehingubloki kolleegidele.
  - Juhuslikult valitud arvuti saab tasu kehtiva ploki esitamise eest.
  - Kaupmehe kontrolltehing viidi lõpule, seega raha laekus ja kaup saadeti kliendile.
- Kommentaarid:
  - Pange tähele, et eelnev pangasuhe ei olnud vajalik.
  - Kolmandat osapoolt ei ole vaja hõlbustamiseks; asendatakse koodide/stiimulite abil.
  - Andmete kogumist ei tohi teostada keegi väljaspool otsest Exchange ja osalejate vahel tuleb vahetada ainult vajalik kogus (nt saatmine Address).
  - Inimeste vahel ei ole vaja usaldust (peale kaupmehe, kes saadab kauba), nagu sularaha ostu puhul mitmel moel.
  - Raha kuulub otse üksikisikutele.
  - Bitcoin Ledger on lihtsuse huvides kujutatud dollarites, kuid tegelikkuses on see BTC.
  - Me simuleerime ühe tehingu edastamist, kuid tegelikkuses on võrgus mitu tehingut pooleli ja plokid sisaldavad korraga tuhandeid tehinguid. Samuti kontrollivad sõlmed, et ei ole pooleli ühtegi topeltkulutustega tehingut (mina viskaksin antud juhul kõik peale ühe ära).
- Pettuse stsenaariumid:
  - Mis siis, kui kliendil ei oleks 25 BTC dollarit?
    - Nad ei saaks tehingut luua, sest "avamine" ja "Ownership" on üks ja sama asi ning arvutid kontrollivad, et tehing oleks nõuetekohaselt allkirjastatud; vastasel juhul lükkavad nad selle tagasi
  - Mis siis, kui juhuslikult valitud arvuti üritab "Ledger muuta"?
    - Blokeering lükatakse tagasi, kuna igal teisel arvutil on täielik ajalugu ja ta märkab muutust, mis rikub üht nende reeglit.
    - Juhuslik Arvuti ei saaks tasu ja nende ploki tehinguid ei lõpetataks.


## Teadmiste hindamine


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Klassiruumi arutelu


Arutlege mõningate liigsete lihtsustuste üle, mis tehti klassiharjutuses teise stsenaariumi raames, ja kirjeldage üksikasjalikumalt, mida tegelik Bitcoin süsteem teeb.


### KA sõnavara ülevaade


Määratlege järgmised eelnevas punktis tutvustatud põhiterminid:



- Sõlme
- [Mempool](https://planb.academy/resources/glossary/mempool)
- [Raskusaste](https://planb.academy/resources/glossary/difficulty) Eesmärk
- Plokk


**Rühmana arutleda mõnede täiendavate terminite tähenduse üle:**


Blockchain, tehing, topeltkulu, Bütsantsi kindlusprobleem, Mining, Proof of Work (PoW), Hash funktsioon, Block reward, Blockchain, pikim ahel, 51% rünnak, väljund, väljundlukk, muudatus, [Satoshis](https://planb.academy/resources/glossary/satoshi-sat), avalik/privaatvõti, Address, avaliku võtme [krüptograafia](https://planb.academy/resources/glossary/cryptography), digitaalne allkiri, Wallet


# BTCPay serveri tutvustamine


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## BTCPay serveri sisselogimisekraani mõistmine


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Töötamine BTCPay Serveriga


Selle kursusebloki eesmärk on saada üldine arusaam BTCPay Serveri tarkvarast. Ühiskeskkonnas on soovitatav jälgida õpetaja demonstratsiooni ja vaadata BTCPay Server kursuseraamatut, et koos õpetajaga kaasa elada. Te saate teada, kuidas luua Wallet mitme meetodi abil. Näidetena võib tuua Hot Wallet seadistused ja BTCPay Server Vault'i kaudu ühendatud riistvaralised rahakotid. Need eesmärgid toimuvad demokeskkonnas, mida kuvab ja millele annab juurdepääsu teie kursuse juhendaja.


Kui te järgite seda kursust ise, leiate nimekirja kolmandate osapoolte hostidest demo eesmärgil aadressil https://directory.btcpayserver.org/filter/hosts. Soovitame tungivalt mitte kasutada neid kolmanda osapoole võimalusi tootmiskeskkondadena; need täidavad siiski õiget eesmärki Bitcoin ja BTCPay Serveri kasutamise tutvustamiseks.


BTCPay Server rockstar'i praktikandina võib teil olla eelnev kogemus Bitcoin sõlme seadistamisel. See kursus on spetsiaalselt kohandatud BTCPay Serveri tarkvarapaketi jaoks.


Paljud BTCPay Serveri võimalused on ühel või teisel kujul olemas ka teistes Bitcoin Wallet-ga seotud tarkvarades.


### BTCPay serveri sisselogimise ekraan


Kui teid tervitatakse demo keskkonda, palutakse teil "Logi sisse" või "Loo oma konto" Serveri administraatorid võivad turvalisuse kaalutlustel uute kontode loomise funktsiooni keelata. BTCPay Serveri logosid ja nupuvärve võib muuta, sest BTCPay Server on avatud lähtekoodiga tarkvara. Kolmanda osapoole host võib tarkvara valges märgistusse panna ja kogu väljanägemist muuta.


![image](assets/en/001.webp)


### Konto loomise aken


Kontode loomine BTCPay serveris nõuab kehtivat e-posti Address stringi; example@email.com oleks sobiv string e-posti jaoks.


Parool peab olema vähemalt 8 tähemärki pikk, sisaldades tähti, numbreid ja sümboleid. Pärast ühekordset parooli määramist peate kontrollima, et parool oleks sama, mis on sisestatud esimesse paroolivälja.


Kui nii e-posti kui ka salasõna väljad on nõuetekohaselt täidetud, klõpsake nupule "Create Account" (konto loomine). See salvestab e-posti aadressi ja salasõna juhendaja BTCPay serveri instantsi.


![image](assets/en/002.webp)


**!Märkus!**


Kui te järgite seda kursust iseseisvalt, siis selle konto loomine toimub tõenäoliselt kolmanda osapoole hostil; seetõttu rõhutame veel kord, et neid ei tohiks kasutada tootmiskeskkondadena, vaid ainult koolituse eesmärgil.


### Konto loomine BTCPay serveri administraatori poolt


BTCPay serveri instantsi administraator saab ka BTCPay serveri jaoks kontosid luua. BTCPay serveri administraator saab klõpsata nupule "Serveri seaded" (1), klõpsata vahekaardil "Kasutajad" (2) ja klõpsata nupul "+ Lisa kasutaja" (3), mis asub vahekaardi "Kasutajad" paremas ülaosas. Eesmärgis (4.3) saate lisateavet kontode administraatori kontrolli kohta.


![image](assets/en/003.webp)


Administraatorina vajate kasutaja e-posti aadressi Address ja kehtestate standardse parooli. Turvalisuse huvides on soovitatav, et administraator teavitaks kasutajat selle salasõna muutmisest enne konto kasutamist. Kui administraator ei määra salasõna ja serveris on konfigureeritud SMTP, saab kasutaja e-kirja koos kutselinkiga, et ta saaks ise oma konto luua ja salasõna määrata.


### Näide


Kui jälgite kursust koos juhendajaga, järgige juhendaja antud linki ja looge oma konto demokeskkonnas. Veenduge, et teie e-posti Address ja parool on turvaliselt salvestatud; neid sisselogimise andmeid vajate selle kursuse ülejäänud demo eesmärkide jaoks.


Teie juhendaja võib olla eelnevalt kogunud e-posti Address ja saatnud kutselinki enne seda harjutust. Kui juhendatud, kontrollige oma e-posti aadressi.


Kui võtate kursuse ilma juhendajata, looge oma konto, kasutades BTCPay Serveri demokeskkonda; minge aadressile


https://Mainnet.demo.btcpayserver.org/login.


Seda kontot tuleks kasutada ainult tutvustamise/koolituse eesmärgil ja mitte kunagi ärilistel eesmärkidel.


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Kuidas luua konto hostitud serveris Interface kaudu.
- Kuidas serveri administraator saab kasutajaid käsitsi lisada serveri seadetes.


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Põhjendage, miks demo-serveri kasutamine on halb mõte tootmise jaoks.


## Kasutajakonto(de) haldamine


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Konto haldamine BTCPay serveris


Kui poeomanik on oma konto loonud, saab ta seda hallata BTCPay serveri kasutajaliidese vasakus allosas. Konto nupu all on mitu kõrgema taseme seadistust.



- Pimedas/valgusrežiim.
- Tundliku teabe peidamise lüliti.
- Konto haldamine.


![image](assets/en/004.webp)


### Tume ja hele režiim


BTCPay Serveri kasutajad saavad valida kasutajaliidese heleda või tumeda versiooni vahel. Kliendile suunatud leheküljed ei muutu. Need kasutavad kliendi soovitud seadeid seoses tumeda või heleda režiimiga.


### Tundliku info varjamine Toggle


Nupp Hide Sensitive Info (Peida tundlikud andmed) pakub kiiret ja lihtsat Layer turvalisust. Kui teil on vaja oma BTCPay Serveriga töötada, kuid avalikus ruumis võivad inimesed teie õla taga varitseda, lülitage sisse Hide Sensitive Info ja kõik BTCPay Serveris olevad väärtused on peidetud. Keegi võib küll üle õla vaadata, kuid ei näe enam väärtusi, millega te tegelete.


### Konto haldamine


Kui kasutajakonto on loodud, saab siin hallata paroole, 2FA-d või API-võtmeid.


### Konto haldamine - Konto


Valikuliselt ajakohastage oma kontot teise e-posti Address abil. Selleks, et tagada, et teie e-posti Address on õige, võimaldab BTCPay Server teil saata kontrollsõnumi. Klõpsake salvesta, kui kasutaja määrab uue e-posti Address ja kinnitab, et kontroll toimis. Kasutajanimi jääb samaks kui eelmine E-post.


Kasutaja võib otsustada kustutada kogu oma konto. Seda saab teha, klõpsates konto vahekaardil nupule kustutamine.


![image](assets/en/005.webp)


**!Märkus!**


Pärast e-posti aadressi muutmist ei muutu konto kasutajanimi. Varem antud Email Address jääb sisselogimise nimeks.


### Konto haldamine - Parool


Õpilane võib soovida muuta oma salasõna. Ta saab seda teha, minnes vahekaardile Parool. Siin peab ta sisestama oma vana salasõna ja saab selle uue vastu vahetada.


![image](assets/en/006.webp)


### Kahefaktoriline autentimine (2fa)


Varastatud salasõna tagajärgede piiramiseks võite kasutada kahefaktorilist autentimist (2FA), mis on suhteliselt uus turvameetod. Kahefaktorilise autentimise saate aktiveerida kontohalduse ja vahekaardi Kahefaktorilise autentimise kaudu. Pärast kasutajanime ja parooliga sisselogimist peate täitma teise sammu.


BTCPay Server toetab kahte meetodit 2FA võimaldamiseks: rakenduspõhine 2FA (Authy, Google, Microsoft Authenticators) või turvaseadmete kaudu (FIDO2 või LNURL Auth).


### Kahefaktoriline autentimine - rakenduspõhine


Sõltuvalt mobiiltelefoni operatsioonisüsteemist (Android või iOS) saavad kasutajad valida järgmiste rakenduste vahel;


1. Laadige alla kahefaktoriline autentifikaator.


   - Authy for [Android](https://play.google.com/store/apps/details?id=com.authy.authy) või [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) või [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator for [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) või [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Pärast Authenticator Appi allalaadimist ja installimist.


   - Skaneeri BTCPay serveri pakutud QR-koodi
   - Või sisestage BTCPay serveri poolt genereeritud võti käsitsi oma Authenticator rakendusse.

3. Authenticatori rakendus annab teile unikaalse koodi. Sisestage unikaalne kood BTCPay Serverisse, et kontrollida seadistamist, ja klõpsake protsessi lõpetamiseks nuppu verify (kinnita).


![image](assets/en/007.webp)


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Konto haldamise võimalused ja erinevad võimalused konto haldamiseks BTCPay Serveri instantsil.
- Kuidas seadistada rakenduspõhine 2FA.


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Kirjeldage, kuidas rakenduspõhine 2FA aitab teie kontot kaitsta.


## Uue poe loomine


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Loo oma poe võlur


Kui uus kasutaja logib sisse BTCPay Serverisse, on keskkond tühi ja vajab esimest salvestust. BTCPay Serveri sissejuhatus annab kasutajale võimaluse "Luua oma pood" (1). Kauplust võib vaadelda kui Bitcoin vajaduste kodu. Uus BTCPay Server Node alustab Bitcoin Blockchain sünkroniseerimisega (2). Sõltuvalt sellest, millisel infrastruktuuril te BTCPay Serveri käivitate, võib see kesta mõnest tunnist kuni mõne päevani. Instantsi praegune versioon kuvatakse BTCPay Serveri kasutajaliidese alumises paremas nurgas. See on abiks veaotsingul.


![image](assets/en/008.webp)


### Loo oma poe võlur


Pärast seda kursust algab eelmisest leheküljest veidi erinev ekraan. Kuna teie juhendaja on ettevalmistanud demokeskkonna, on Bitcoin Blockchain eelnevalt sünkroonitud ja seetõttu ei näe te sõlmede sünkroonimisolekut.


Kasutaja võib otsustada kustutada kogu oma konto. Seda saab teha, klõpsates konto vahekaardil nupule kustutamine.


![image](assets/en/009.webp)


**!Märkus!**


BTCPay Serveri kontod võivad luua piiramatu arvu kauplusi. Iga pood on Wallet või "kodu".


### Näide


Alustage, klõpsates nupul "Loo oma pood".


![image](assets/en/010.webp)


See loob teie esimese Kodu ja armatuurlaua BTCPay Serveri kasutamiseks.


(1) Pärast klõpsamist "Loo oma pood", BTCPay Server nõuab, et annaksite poele nime; see võib olla mis iganes teile kasulik.


![image](assets/en/011.webp)


(2) Järgmisena tuleb määrata vaikimisi kaupluse valuuta, kas fiatvaluuta või Bitcoin või Sats vääringuga valuuta. Demokeskkonna jaoks seame selle väärtuseks USD.


![image](assets/en/012.webp)


(3) Viimase parameetrina kaupluse seadistamisel nõuab BTCPay Server, et te määraksite "Eelistatud hinnaallika", et võrrelda Bitcoin hinda praeguse fiat-hinnaga, nii et teie kaupluses kuvatakse õige Exchange kurss Bitcoin ja kaupluse poolt määratud fiat-valuuta vahel. Me jääme demo näites vaikimisi ja seame selle Kraken Exchange-ks. BTCPay Server kasutab Exchange kursi kontrollimiseks Kraken API-d.


![image](assets/en/013.webp)


(4) Nüüd, kui need poe parameetrid on määratud, klõpsake nupule Create ja BTCPay Server loob teie esimese poe armatuurlaua, kus nõustaja jätkab.


![image](assets/en/014.webp)


Palju õnne, te olete loonud oma esimese poe ja sellega on see harjutus lõppenud.


![image](assets/en/015.webp)


### Oskuste kokkuvõte


Selles osas õppisite:



- Kaupluse loomine ja vaikimisi valuuta seadistamine koos hinnaallikate eelistustega.
- Iga "Kauplus" on uus kodu, mis on eraldatud teistest kauplustest selles BTCPay Serveri paigalduses.


# Bitcoin võtmete turvamise sissejuhatus


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Bitcoin võtmete genereerimise mõistmine


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Mis on seotud Bitcoin võtmete genereerimisega?


Bitcoin rahakotide loomisel luuakse nn "[seed](https://planb.academy/resources/glossary/seed)". Viimases eesmärgis lõid sa "seed", Enne loodud sõnade rida on tuntud ka kui Mnemonic fraasid. seed kasutatakse individuaalsete Bitcoin võtmete tuletamiseks ja Bitcoin saatmiseks või vastuvõtmiseks. seed fraase ei tohi kunagi jagada kolmandate isikute või usaldamata partneritega.


seed genereerimine toimub vastavalt tööstusstandardile, mida tuntakse kui "hierarhilist deterministlikku" (HD) raamistikku.


![image](assets/en/016.webp)


### Aadressid


BTCPay Server on ehitatud generate uus Address. See leevendab avaliku võtme või Address korduvkasutamise probleemi. Sama avaliku võtme kasutamine muudab kogu teie makseajaloo jälgimise väga lihtsaks. Võtmete mõtlemine ühekordse kasutusega vautšeritena parandaks oluliselt teie privaatsust. Me kasutame ka Bitcoin Aadresse, ärge ajage neid segi avalike võtmetega.


Address saadakse avalikust võtmest "hashing-algoritmi" abil Enamik rahakotte ja tehinguid kuvab aga pigem Aadresse kui neid avalikke võtmeid. Aadressid on üldiselt lühemad kui avalikud võtmed ja algavad tavaliselt `1`, `3` või `bc1`ga, samas kui avalikud võtmed algavad `02`, `03` või `04`ga.



- Aadressid, mis algavad numbriga `1.....`, on endiselt väga levinud aadressid. Nagu peatükis "Uue poe loomine" mainitud, on need vanad aadressid. See Address tüüp on mõeldud P2PKH tehingute jaoks. P2Pkh kasutab Base58 kodeeringut, mis muudab Address suur- ja väiketähenduslikuks. Selle struktuur põhineb avalikul võtmel koos täiendava numbriga identifikaatorina.



- Aadressid algusega `bc1...` liiguvad aeglaselt väga levinud aadresside hulka. Neid tuntakse kui (algupäraseid) [SegWit](https://planb.academy/resources/glossary/segwit)-aadresse. Need pakuvad paremat tasustruktuuri kui teised mainitud aadressid. Natiivsed SegWit aadressid kasutavad Bech32 kodeeringut ja lubavad ainult väikseid tähti.



- Aadressid, mis algavad numbritega `3...`, on börsidel ikka veel levinud hoiuseaadressid. Need aadressid on mainitud peatükis "Uue poe loomine", pakitud või nested SegWit aadressid. Need võivad aga toimida ka kui "Multisig Address". Kui neid kasutatakse SegWit Address-aadressidena, on [tehingutasude](https://planb.academy/resources/glossary/transaction-fees) osas mõningane kokkuhoid, jällegi vähem kui natiivse SegWit puhul. P2SH aadressid kasutavad Base58 kodeeringut. See muudab selle juhtumitundlikuks, nagu vanad Address.



- Aadressid, mis algavad sõnadega `2...`, on Testnet aadressid. Need on mõeldud Testnet Bitcoin (tBTC) vastuvõtmiseks. Te ei tohiks seda kunagi segi ajada ja saata Bitcoin nendele aadressidele. Arenduse eesmärgil võite generate Testnet Wallet. Internetis on mitmeid kraanid, et saada Testnet Bitcoin. Ärge kunagi ostke Testnet Bitcoin. Testnet Bitcoin on kaevandatud. See võib olla põhjus, miks arendaja võiks kasutada hoopis Regtest. See on arendajate mängukeskkond, millest puuduvad teatud võrgukomponendid. Bitcoin on aga väga kasulik arenduseesmärkidel.


### Avalikud võtmed


Avalikke võtmeid kasutatakse tänapäeval praktikas harvemini. Aja jooksul on Bitcoin kasutajad asendanud need aadressidega. Need on siiski veel olemas ja neid kasutatakse aeg-ajalt. Avalikud võtmed on üldiselt palju pikemad stringid kui aadressid. Nii nagu aadressidki, algavad nad konkreetse identifikaatoriga.



- Esiteks, `02...` ja `03...` on väga standardsed SEC-vormingus kodeeritud avaliku võtme tunnused. Neid saab töödelda ja muuta aadressideks vastuvõtmiseks, kasutada multi-sig aadresside loomiseks või allkirja kontrollimiseks. Bitcoin algusaegsed tehingud kasutasid avalikke võtmeid P2PK-tehingute osana.



- HD rahakotid kasutavad aga teistsugust struktuuri. `xpub...`, `ypub...` või `zpub...` nimetatakse laiendatud avalikeks võtmeteks ehk xpubideks. Neid võtmeid kasutatakse paljude avalike võtmete tuletamiseks HD Wallet osana. Kuna teie [xpub](https://planb.academy/resources/glossary/xpub) sisaldab andmeid kogu teie ajaloo kohta, st varasemate ja tulevaste tehingute kohta, ärge kunagi jagage neid usaldamatutele osapooltele.


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Erinevused aadresside ja avalike võtmete andmetüüpide vahel ning aadresside kasutamise eelised võrreldes avalike võtmetega.


### Teadmiste hindamine


Kirjeldage iga tehingu puhul uute aadresside kasutamise eeliseid võrreldes Address korduvkasutamise või avaliku võtme meetoditega.


## Võtmete kindlustamine Hardware Wallet abil


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Bitcoin võtmete säilitamine


Pärast seed fraasi genereerimist nõuab selles raamatus genereeritud 12-24 sõnast koosnev nimekiri nõuetekohast varundamist ja turvamist, kuna need sõnad on ainus viis Wallet juurdepääsu taastamiseks. HD rahakoti struktuur ja see, kuidas see genereerib aadressid deterministlikult ühe seed abil, tähendab, et kõik teie loodud aadressid varundatakse selle ühe Mnemonic sõnade loendi abil, mis kujutab teie seed või taastamisfraasi.


Hoidke oma taastumislause turvaliselt. Kui keegi pääseb ligi, eriti pahatahtlikult, võib ta teie raha liigutada. Hoidke seed turvaliselt ja turvaliselt, pidades samas meeles, et see on vastastikune nende vahel. Bitcoin privaatvõtmete säilitamiseks on mitu meetodit, millest igaühel on oma eelised ja puudused turvalisuse, privaatsuse, mugavuse ja füüsilise säilitamise osas. Privaatvõtmete olulisuse tõttu kalduvad Bitcoin kasutajad hoidma ja turvaliselt hoidma neid võtmeid pigem "enda hoiul" kui kasutama "hoiuteenuseid", nagu pangad. Sõltuvalt kasutajast peavad nad kasutama kas Cold säilitamislahendust või Hot Wallet.


### Hot ja Cold Bitcoin võtmete säilitamine


Tavaliselt on Bitcoin rahakotid Hot Wallet või Cold Wallet. Enamik kompromisse seisneb mugavuses, kasutusmugavuses ja turvariskides. Kõiki neid meetodeid võib vaadelda ka hoidja lahenduses. Kuid kompromissid on siin enamasti turvalisuse ja privaatsusega seotud ning väljuvad käesoleva kursuse raamidest.


### Hot Wallet


Hot rahakotid on kõige mugavam viis Bitcoin-ga suhtlemiseks mobiil-, veebi- või lauaarvutitarkvara kaudu. Wallet on alati ühendatud internetti, mis võimaldab kasutajatel saata või vastu võtta Bitcoin. See on aga ka selle nõrkus; kuna Wallet on alati võrgus, on see nüüd haavatavam häkkerite või pahavara rünnakute suhtes teie seadmes. BTCPay Serveris hoiavad Hot rahakotid privaatvõtmeid instantsil. Igaüks, kes pääseb teie BTCPay Serveri salvestusse, võib potentsiaalselt varastada raha sellest Address-st, kui ta on pahatahtlik. Kui BTCPay Server töötab hostitud keskkonnas, peaksite seda alati oma turvaprofiilis arvesse võtma ja sellisel juhul eelistatavalt mitte kasutama Hot Wallet. Kui BTCPay Server on paigaldatud riistvarale, mis on teie omanduses ja kaitstud, väheneb riskiprofiil märkimisväärselt, kuid see ei kao kunagi täielikult.


### Cold Wallet


Üksikisikud viivad oma Bitcoin Cold Wallet-sse, sest see suudab eralisi võtmeid internetist isoleerida, kaitstes neid seega võimalike veebiohtude eest. Internetiühenduse eemaldamine vähendab pahavara, nuhkvara ja SIM-kaardi vahetamise ohtu. Usutakse, et Cold mälu on turvalisuse ja sõltumatuse poolest parem kui Hot mälu, tingimusel et võetakse piisavaid ettevaatusabinõusid, et vältida Bitcoin privaatvõtmete kaotamist. Cold säilitamine on kõige sobivam suurte Bitcoin koguste jaoks, mida ei kavatseta Wallet seadistuse keerukuse tõttu sageli kulutada.


Bitcoin võtmete Cold salvestamiseks on erinevaid meetodeid, alates paberist rahakotidest kuni ajukotideni, riistvara rahakottideni või algusest peale Wallet failini. Enamik rahakotte kasutab [BIP](https://planb.academy/resources/glossary/bip) 39 generate fraasi seed jaoks. Bitcoin core tarkvaras ei ole aga veel saavutatud üksmeelt selle kasutamise osas. Bitcoin core tarkvara generate ikkagi Wallet.dat faili, mida peate salvestama turvalisse offline-kohta.


### Oskuste kokkuvõte


Selles osas õppisite:



- Hot ja Cold rahakottide erinevused funktsionaalsuse ja nende kompromisside osas.


### Teadmiste hindamine Kontseptuaalne ülevaade



- Mis on Wallet?



- Mis vahe on Hot ja Cold rahakottidel?



- Kirjeldage, mida tähendab "Wallet genereerimine"?


## Bitcoin võtmete kasutamine


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay server Wallet


BTCPay Server koosneb järgmistest standardsetest Wallet funktsioonidest:



- Tehingud
- Saada
- Saate
- Rescan
- Tõmba makseid
- Väljamaksed
- [PSBT](https://planb.academy/resources/glossary/psbt)
- Üldised seaded


### Tehingud


Administraatorid saavad näha selle konkreetse kauplusega ühendatud On-Chain Wallet sissetulevaid ja väljaminevaid tehinguid tehingute vaates. Iga tehingu puhul eristatakse saadud ja saadetud summad. Saadud on Green ja väljaminevad tehingud on punased. BTCPay Serveri tehingute vaates näevad administraatorid ka standardseid [silte](https://planb.academy/resources/glossary/label).



| Tehingu tüüp | Kirjeldus                                          |
| ------------- | -------------------------------------------------- |
| Rakendus      | Makse saadi rakenduse loodud arve kaudu            |
| Arve          | Makse saadi arve kaudu                             |
| [Payjoin](https://planb.academy/resources/glossary/payjoin)       | Pole makstud, arve taimer ei ole veel aegunud      |
| Payjoin-paljastatud | [UTXO](https://planb.academy/resources/glossary/utxo) paljastati arve payjoin-ettepaneku kaudu |
| Maksepäring   | Makse saadi maksepäringu kaudu                     |
| Väljamakse    | Makse saadeti väljamakse või tagasimakse kaudu     |

### Kuidas saata


BTCPay serveri saatmisfunktsioon saadab tehinguid teie BTCPay serverist On-Chain Wallet. BTCPay Server võimaldab mitmel viisil allkirjastada oma tehinguid raha kulutamiseks. Tehingu saab allkirjastada;



- Hardware Wallet
- Rahakotid, mis toetavad PSBT
- HD privaatne võti või taastamise seemned.
- Hot Wallet


#### Hardware Wallet


BTCPay Serveril on sisseehitatud Hardware Wallet tugi, mis võimaldab teil kasutada oma Hardware Wallet-d koos BTCPay Vault'iga, ilma et teave lekiks kolmandatele rakendustele või serveritele. Hardware Wallet integratsioon BTCPay Serveris võimaldab teil importida oma Hardware Wallet ja kulutada sissetulevaid vahendeid lihtsa kinnitusega oma seadmes. Teie isiklikud võtmed ei lahku kunagi seadmest ja kõik vahendid valideeritakse teie Full node vastu, mis tagab, et andmed ei leki.


#### Allkirjastamine Wallet toetava PSBT-ga


PSBT (osaliselt allkirjastatud Bitcoin-tehingud) on andmevahetusformaat Bitcoin-tehingute jaoks, mis tuleb veel täielikult allkirjastada. PSBT on BTCPay Serveris toetatud ja seda saab allkirjastada ühilduvate riist- ja tarkvaraliste rahakottidega.


Täielikult allkirjastatud Bitcoin tehingu koostamine toimub järgmiste etappide kaudu:



- PSBT konstrueeritakse konkreetsete sisendite ja väljunditega, kuid signatuurid puuduvad
- Eksporditud PSBT saab importida seda formaati toetava Wallet abil
- Tehinguandmeid saab kontrollida ja allkirjastada Wallet abil
- Allkirjastatud PSBT fail eksporditakse Wallet-st ja imporditakse BTCPay Serveriga
- BTCPay Server toodab lõpliku Bitcoin tehingu
- Kontrollida tulemust ja edastada see võrku


#### Allkirjastamine HD privaatvõtme või Mnemonic seed abil


Kui olete enne BTCPay Serveri kasutamist loonud Wallet, saate raha kulutada, sisestades oma isikliku võtme vastavasse lahtrisse. Seadistage Wallet> Seaded õige "AccountKeyPath"; vastasel juhul ei saa te kulutada.


#### Allkirjastamine Hot Wallet-ga


Kui olete poe seadistamisel loonud uue Wallet ja aktiveerinud selle Hot Wallet-na, kasutab see automaatselt allkirjastamiseks serveris salvestatud seed.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) on Bitcoin protokolli funktsioon, mis võimaldab asendada eelnevalt edastatud tehingu (kui see on veel kinnitamata). See võimaldab juhuslikult muuta oma Wallet tehingu sõrmejälge või asendada see kõrgema tasumääraga, et liigutada tehing kinnituse (Mining) prioriteetsuse järjekorras kõrgemale. See asendab tegelikult algse tehingu, kuna kõrgema tasumääraga tehing saab prioriteedi, ja kui see on kinnitatud, muudab see algse tehingu kehtetuks (topeltkulutusi ei toimu).


Vajutage nuppu "Täpsemad seaded", et vaadata RBF valikuid.


![image](assets/en/017.webp)



- Randomize for higher privacy, võimaldab tehingu sõrmejälje juhuslikuks muutmiseks automaatselt asendada tehingu sõrmejälgi.
- Jah, RBF tehingu märkimine ja selgesõnaline asendamine (ei asendata vaikimisi, ainult sisendiga)
- Ei, ärge lubage tehingut asendada.


### Coin Valik


Coin valik on täiustatud privaatsust suurendav funktsioon, mis võimaldab teil valida münte, mida soovite tehingu tegemisel kulutada. Näiteks maksmine müntidega, mis on värskelt ühildatud.


Coin valik töötab koos Wallet siltide funktsiooniga. See võimaldab teil märgistada sissetulevaid vahendeid sujuvamaks UTXO haldamiseks ja kulutamiseks.


BTCPay Server toetab BIP-329 etikettide haldamiseks. Kui te kannate üle Wallet-st, mis toetab BIP-329 ja millel on määratud sildid, siis BTCPay Server tunneb need ära ja impordib need automaatselt. Serverite migreerimisel saab seda teavet ka eksportida ja uude keskkonda importida.


### Kuidas saada


Kui klõpsate BTCPay Serveris nupule receive, genereerib see kasutamata Address, mida saab kasutada maksete vastuvõtmiseks. Administraatorid võivad luua ka generate uue Address, luues uue "Invoice"


BTCPay Server palub teil alati generate järgmist olemasolevat Address, et vältida Address korduvkasutamist. Pärast klõpsamist "generate järgmine olemasolev BTC Address" genereerib BTCPay Server uue Address ja QR. Samuti võimaldab see teil määrata Address-le otse sildi, et paremini hallata oma aadresse.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Uuesti skaneerimine


Funktsioon "Rescan" tugineb Bitcoin core 0.17.0 "Scantxoutset" funktsioonile, et otsida Blockchain (nn UTXO Set) hetkeseisundist münte, mis kuuluvad konfigureeritud tuletusskeemi. Wallet rescan lahendab kaks levinud probleemi, millega BTCPay Serveri kasutajad sageli kokku puutuvad.


1. Lünga piiramise probleem - Enamik kolmanda osapoole rahakotte on kerged rahakotid, mis jagavad sõlme paljude kasutajate vahel. Kerge ja Full node-le tuginevad rahakotid piiravad Blockchain-l jälgitavate saldota aadresside arvu (tavaliselt 20), et vältida jõudlusprobleeme. BTCPay Server genereerib iga Invoice jaoks uue Address. Eespool öeldut silmas pidades, kui BTCPay Server genereerib 20 järjestikust tasumata arvet, lõpetab väline Wallet tehingute hankimise, eeldades, et uusi tehinguid ei ole toimunud. Teie väline Wallet ei näita neid, kui arved on makstud 21., 22. jne. päeval. Teisest küljest jälgib BTCPay Server Wallet sisemiselt kõiki tema poolt genereeritud Address koos oluliselt kõrgema vahepiiriga. See ei sõltu kolmandast isikust ja võib alati näidata õiget saldot.

2. Lahendus lõhepiir - Kui teie [väline/olemasolev Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) võimaldab lõhepiiri konfigureerimist, on lihtne lahendus selle suurendamine. Enamik rahakotte seda siiski ei võimalda. Ainukesed rahakotid, mis toetavad praegu teadaolevalt gap-limiidi konfigureerimist, on Electrum, Wasabi ja Sparrow wallet. Kahjuks tekib teil tõenäoliselt probleem paljude teiste rahakottidega. Parima kasutajakogemuse ja privaatsuse tagamiseks kaaluge välise rahakoti asemel BTCPay serveri sisemise Wallet kasutamist.


#### BTCPay Server kasutab "mempoolfullrbf=1"


BTCPay Server kasutab "mempoolfullrbf=1"; me oleme lisanud selle vaikimisi teie BTCPay Serveri seadistusse. Siiski oleme teinud selle ka funktsiooniks, mille saate ise välja lülitada. Ilma "mempoolfullrbf=1", kui klient teeb topeltmakse tehinguga, mis ei signaliseeri RBF, saaks kaupmees sellest teada alles pärast kinnitust.


Administraator võib soovida seda seadistust mitte kasutada. Järgmise stringi abil saate vaikimisi seadistust muuta.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay serveri Wallet seaded


Wallet seaded BTCPay Serveris annavad selge ja ülevaatliku ülevaate teie Wallet üldistest seadetest. Kõik need seaded on eeltäidetud, kui Wallet on loodud BTCPay Serveriga.


![image](assets/en/020.webp)


Wallet seaded BTCPay Serveris annavad selge ja ülevaatliku ülevaate teie Wallet üldistest seadetest. Kõik need seaded on eeltäidetud, kui Wallet on loodud BTCPay Serveriga. BTCPay Serveri Wallet seaded algavad Wallet olekust. Kas tegemist on ainult jälgiva või ainult Hot Wallet-ga? Sõltuvalt Wallet tüübist võivad toimingud olla erinevad, sealhulgas Wallet uuesti skaneerimine puuduvate tehingute jaoks, vanade tehingute kärpimine ajaloost, Wallet registreerimine makselinkide jaoks või praeguse kauplusega seotud Wallet asendamine ja kustutamine. BTCPay Serveri Wallet seadetes võivad administraatorid Wallet parema haldamise eesmärgil määrata Wallet jaoks etiketi. Siin saab administraator näha ka tuletusskeemi, kontovõtit (xpub), sõrmejälge ja võtmepaati. Wallet seadete maksete puhul on ainult kaks peamist seadistust. Makse on kehtetu, kui tehingut ei kinnitata (määratud minuti jooksul) pärast Invoice kehtivusaja lõppu. Invoice loetakse kinnitatuks, kui maksetehing on kinnitanud X arvu kinnitusi. Administraatorid saavad ka lülitada soovitatud tasude kuvamise makseekraanil või määrata käsitsi kinnituse eesmärgi plokkide arvu.


![image](assets/en/021.webp)


**!Märkus!**


Kui te järgite seda kursust iseseisvalt, siis selle konto loomine toimub tõenäoliselt kolmanda osapoole serveris. Seetõttu soovitame veel kord, et neid ei tohiks kasutada tootmiskeskkondadena, vaid pigem ainult koolituse eesmärgil.


### Näide


#### Bitcoin Wallet seadistamine BTCPay serveris


BTCPay Server pakub Wallet seadistamiseks kaks meetodit. Üks võimalus on importida olemasolev Bitcoin Wallet. Impordiks võib ühendada Hardware Wallet, importida Wallet faili, sisestada laiendatud avaliku võtme, skaneerida Wallet QR-koodi või, mis on kõige ebasoodsam, sisestada käsitsi eelnevalt loodud Wallet taastamise seed. BTCPay Serveris on võimalik luua ka uus Wallet. Uue Wallet genereerimisel on BTCPay Serveril kaks võimalikku seadistamisviisi.


BTCPay Serveri valik Hot Wallet võimaldab selliseid funktsioone nagu "PayJoin" või "Liquid". Sellel on siiski üks puudus: selle Wallet jaoks loodud taastamise seed salvestatakse serveris, kust igaüks, kellel on administraatori kontroll, võib selle välja võtta. Kuna teie privaatne võti on tuletatud teie taastamis seed-st, võib pahatahtlik isik saada juurdepääsu teie praegustele ja tulevastele rahalistele vahenditele!


Selle riski vähendamiseks BTCPay Serveris võib administraator seadistada väärtuseks "Server Settings > Policies > Allow non-admins to create Hot wallets for their stores" ("Luba mitteadmins to create Hot wallets for their stores") "no" ("ei"), kuna see on vaikimisi väärtus. Nende Hot rahakottide turvalisuse suurendamiseks peaks serveri administraator lubama 2FA autentimist kontodel, millel on lubatud Hot rahakotid. Privaatsete võtmete salvestamine avalikus serveris on ohtlik praktika ja sellega kaasnevad märkimisväärsed riskid. Mõned neist on sarnased Lightning Network riskidega (vt järgmist peatükki Lightning Network riskide kohta).


Teine võimalus, mida BTCPay Server pakub uue Wallet genereerimiseks, on Watch-only wallet loomine. BTCPay Server generate teie isiklikud võtmed üks kord. Pärast seda, kui kasutaja kinnitab, et on oma seed fraasi üles kirjutanud, kustutab BTCPay Server privaatvõtmed serverist. Selle tulemusena on teie kauplus nüüd ühendatud Watch-only wallet. Watch-only wallet-le saadud raha kulutamiseks vt peatükki Kuidas saata, kasutades kas BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction) või, mis on kõige vähem soovitatav, esitades käsitsi oma seed fraasi.


Sa lõid viimases osas uue "poe". Installeerimisviisard jätkab, küsides "Set up a Wallet" või "Set up a Lightning node". Selles näites järgite "Set up a Wallet" (1) viisardiprotsessi.


![image](assets/en/022.webp)


Pärast klõpsamist "Seadistage Wallet" jätkab viisard, küsides, kuidas soovite jätkata; BTCPay Server pakub nüüd võimalust ühendada olemasolev Bitcoin Wallet teie uue kauplusega. Kui teil ei ole Wallet, soovitab BTCPay Server luua uus. Selles näites järgitakse samme "uue Wallet loomiseks" (2). Järgige samme, et õppida, kuidas "ühendada olemasolev Wallet (1).


![image](assets/en/023.webp)


**!Märkus!**


Kui te läbite selle kursuse klassiruumis, siis võtke arvesse, et praegune näide ja meie loodud seed on mõeldud ainult õppeotstarbeks. Nendel aadressidel ei tohiks kunagi olla mingit olulist muud kui nõutud kogu harjutuste ajal.


(1) Jätkake nõustaja "Uus Wallet", klõpsates nupul "Create a new Wallet".


![image](assets/en/024.webp)


(2) Pärast klõpsamist "Create a new Wallet" (Loo uus Wallet), annab järgmine aken viisardis valikuid "Hot Wallet" ja "Watch-only wallet" Kui te jälgite koos juhendajaga, on teie keskkond jagatud demo ja te saate luua ainult Watch-only wallet. Pange tähele erinevust kahe alltoodud joonise vahel. Kuna olete Demo keskkonnas, jälgides koos juhendajaga, looge "Watch-only wallet" ja jätkake "New Wallet" viisardiga.


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Jätkates uue Wallet juhi tööd, olete nüüd jaotises Create BTC Watch-only wallet. Siin saame määrata Wallet "Address tüübi" BTCPay Server võimaldab teil valida oma eelistatud Address tüübi; selle kursuse kirjutamise ajal on endiselt soovitatav kasutada bech32-aadresse. Täpsemalt saate aadresside kohta teada selle osa esimeses peatükis.



- SegWit (bech32)
  - Native SegWit aadressid algavad sõnaga "bc1q".
  - Näide: `bc1qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Vanad aadressid on aadressid, mis algavad numbriga `1`.
  - Näide: `15e15hXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Taproot (edasijõudnutele)
  - Taproot aadressid algavad sõnaga "bc1p".
  - Näide: `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit pakitud
  - SegWit-ga ümbritsetud aadressid algavad numbriga "3".
  - Näide: "37BBXXXXXXXXXXXXXXXXXXXXXXX"


Valige eelistatud Wallet Address tüübiks SegWit (soovitatav).


![image](assets/en/027.webp)


(4) Wallet parameetri seadistamisel võimaldab BTCPay Server kasutajatel seadistada valikuline passphrase läbi BIP39; kinnitage kindlasti oma parool.


![image](assets/en/028.webp)


(5) Pärast Wallet tüübi Address ja võimalike edasiste valikute seadistamist klõpsake nuppu Create ja BTCPay Server generate teie uut Wallet. Pange tähele, et see on viimane samm enne seed fraasi genereerimist. Veenduge, et teete seda ainult keskkonnas, kus keegi ei saa teie ekraani vaadates seed fraasi varastada.


![image](assets/en/029.webp)


(6) BTCPay Server kuvab järgmisel ekraanil teie äsja loodud Wallet jaoks taastamise seed fraasi; need on võtmed teie Wallet taastamiseks ja tehingute allkirjastamiseks. BTCPay Server genereerib 12 sõnast koosneva seed fraasi. Need sõnad kustutatakse serverist pärast seda häälestusekraani. See Wallet on konkreetselt Watch-only wallet. Seda seed fraasi ei soovitata salvestada digitaalselt või fotokujutisena. Kasutajad võivad viisardis edasi minna ainult siis, kui nad tunnistavad aktiivselt, et nad on oma seed fraasi üles kirjutanud.


![image](assets/en/030.webp)


(7) Pärast klõpsamist Valmis ja äsja loodud Bitcoin seed fraasi kinnitamist uuendab BTCPay Server teie poe lisatud uue Wallet ja on valmis makseid vastu võtma. Märkige kasutaja Interface vasakpoolses navigatsioonimenüüs, kuidas Bitcoin on nüüd esile tõstetud ja aktiveeritud Wallet all.


![image](assets/en/031.webp)


### Näide: seed fraasi üleskirjutamine


See on eriti turvaline hetk Bitcoin kasutamiseks. Nagu eespool mainitud, peaks ainult teil olema juurdepääs teie seed fraasile või teadmised selle kohta. Kuna te jälgite koos õpetaja ja klassiruumi, tuleks genereeritud seed kasutada ainult sellel kursusel. Liiga paljud tegurid, sealhulgas klassikaaslaste uudishimulikud silmad, ebaturvalised süsteemid ja muud, muudavad need võtmed ainult õppeotstarbelisteks ja ebausaldusväärseteks. Siiski tuleks genereeritud võtmed siiski säilitada kursuse näidete jaoks.


Esimene meetod, mida me selles olukorras kasutame, mis on ka kõige vähem turvaline, on seed lause üleskirjutamine õiges järjekorras. seed fraasikaart on lisatud õpilasele antud õppematerjalidesse või on leitav BTCPay serveri GitHubist. Kasutame seda kaarti eelnevas etapis genereeritud sõnade üleskirjutamiseks. Kirjutage need kindlasti õiges järjekorras. Kui olete need üles kirjutanud, kontrollige neid tarkvara poolt antud sõnade suhtes, et veenduda, et olete need õiges järjekorras üles kirjutanud. Kui olete need üles kirjutanud, klõpsake märkeruutu, et olete seed lause õigesti üles kirjutanud.


### Näide: seed fraasi salvestamine Hardware Wallet-sse


Selles kursuses käsitleme seed fraasi salvestamist Hardware Wallet-le. Selle kursuse jälgimine koos juhendajaga võib mõnikord sisaldada sellist seadet. Kursuse juhendmaterjalides on koostatud loetelu riistvaralistest rahakottidest, mis sobiksid selle harjutuse jaoks.


Selles näites kasutame BTCPay Server vault ja Blockstream Jade Hardware Wallet.


Võite jälgida ka videojuhendit Hardware Wallet ühendamise kohta.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Lae alla BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Veenduge, et laadite alla õiged failid oma konkreetse süsteemi jaoks. Windowsi kasutajad peaksid alla laadima paketi [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), Maci kasutajad [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) ja Linuxi kasutajad [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Pärast BTCPay Server Vault'i installimist käivitage tarkvara, klõpsates selle ikoonil töölaual. Kui BTCPay Server Vault on korralikult paigaldatud ja esimest korda käivitatud, küsib see luba veebirakenduste kasutamiseks. See küsib juurdepääsu konkreetsele BTCPay Serverile, millega te töötate. Nõustuge nende tingimustega. BTCPay Server Vault otsib nüüd riistvara seadet. Kui seade on leitud, tuvastab BTCPay Server, et Vault töötab ja on teie seadme välja otsinud.


**!Märkus!**


Hot Wallet kasutamisel ärge andke oma SSH-võtmeid või serveri administraatori kontot kellelegi teisele peale administraatorite. Kõigil, kellel on juurdepääs nendele kontodele, on juurdepääs Hot Wallet vahenditele.


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Bitcoin Wallet tehingu vaade ja selle erinevad kategoriseeringud.
- Bitcoin Wallet saatmisel on saadaval erinevaid võimalusi, alates riistvarast kuni Hot rahakottideni.
- Enamiku rahakottide kasutamisel esinev lõhe probleemi ja kuidas seda parandada.
- Kuidas luua BTCPay Serveris uus generate Bitcoin Wallet, sealhulgas salvestada võtmed Hardware Wallet ja varundada taastamisfraas.


Selles eesmärgis õppisite, kuidas luua BTCPay Serveris uus generate Bitcoin Wallet. Me ei ole veel käsitlenud, kuidas neid võtmeid kindlustada või kasutada. Selle eesmärgi lühiülevaates olete õppinud, kuidas luua esimene kauplus. Te olete õppinud, kuidas generate Bitcoin taastamise seed fraasi.


### Teadmiste hindamine Praktiline ülevaade


Kirjeldage võtmete genereerimise meetodit ja nende kaitsmise skeemi koos turvaskeemi kompromisside/riskidega.


## BTCPay Server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Kui serveriadministraator loob uue BTCPay Serveri instantsi, võib ta seadistada Lightning Network rakendamise, näiteks LND, Core Lightning või Eclair; üksikasjalikumaid paigaldusjuhiseid leiate osast BTCPay Serveri konfigureerimine.


Kui järgneb klassiruum, töötab Lightning-sõlme ühendamine teie BTCPay serveriga läbi Custom-sõlme. Kasutaja, kes ei ole BTCPay Serveri serveri administraator, ei saa vaikimisi kasutada sisemist Lightning-sõlme. Selle eesmärk on kaitsta serveri omanikku oma raha kaotamise eest. Serveriadministraatorid võivad paigaldada lisaseadme, et anda juurdepääs oma Lightning-sõlmele LNBanki kaudu; see ei kuulu käesoleva raamatu reguleerimisalasse. Lisateavet LNBanki kohta leiate ametlikul pluginate lehel.


### Ühenda sisesõlme (serveri administraator)


Serveriadministraator saab kasutada BTCPay Serveri sisemist Lightning Node'i. Sõltumata Lightningi rakendusest on Lightningi sisemise sõlme ühendamine sama.


Minge eelmisse seadistuspoodi ja klõpsake vasakpoolses menüüs "Lightning" Wallet. BTCPay Server annab kaks seadistamisvõimalust: kasutades sisemist sõlme (vaikimisi ainult serveri administraator) või kohandatud sõlme (väline ühendus). Serveri administraatorid saavad klõpsata valikut "Kasuta sisemist sõlme". Rohkem seadistusi ei ole vaja teha. Vajutage nupule "save" ja märkige teade "BTC Lightning node updated". Kauplus on nüüd edukalt saanud Lightning Network võimekuse.


### Ühenda väline sõlme (serveri kasutaja/kaupluse omanik)


Vaikimisi ei ole poeomanikel lubatud kasutada serveri administraatori Lightning Node'i. Ühendus tuleb luua välise sõlme, kas poe omanikule kuuluva sõlme enne BTCPay serveri seadistamist, LNBanki pluginaga, kui see on serveri administraatori poolt kättesaadavaks tehtud, või hoiulahendusega nagu Alby.


Mine eelmisse seadistuspoodi ja klõpsa vasakpoolses menüüs rahakottide all nupule "Lightning". Kuna poeomanikud ei tohi vaikimisi kasutada sisemist sõlme, on see valik hallis. Kohandatud sõlme kasutamine on poeomanikele vaikimisi ainus võimalus.


BTCPay Server nõuab ühendusandmeid; eeltäidetud (või hoiustatud lahendus) edastab selle teabe spetsiaalselt Lightningi rakendusele kohandatud kujul. BTCPay Serveris saavad poeomanikud kasutada järgmisi ühendusi;



- C-valgustus TCP või Unixdomeenide kauduocketconnection.
- Lightning Charge HTTPS-i kaudu
- Eclair HTTPS-i kaudu
- LND REST-proxy kaudu
- LNDhub REST API kaudu


![image](assets/en/032.webp)


Klõpsake nuppu "testühendus", et veenduda, et olete ühenduse andmed õigesti sisestanud. Kui ühendus on kinnitanud, et see on hea, klõpsake nuppu "Salvesta" ja BTCPay Server näitab, et kauplus on uuendatud Lightning Node'iga.


### Lightning-sisese sõlme LND haldamine (serveri administraator)


Pärast sisemise Lightning-sõlme ühendamist märkavad serveri administraatorid juhtpaneelil uusi plaate spetsiaalselt Lightning-teabe jaoks.



- Lightning Balance
- BTC kanalites
  - BTC kanalite avamine
  - BTC kohalik Saldo
  - BTC kaugbilanss
  - BTC kanalite sulgemine
- BTC On-Chain
  - BTC kinnitas
  - BTC kinnitamata
  - BTC reserveeritud
- Välguteenused
  - Ride the Lightning (RTL).


Klõpsates vasakpoolses menüüs "Lightning-teenuste" plaadi Ride the Lightning Logo või "Lightning" all rahakottide all, pääsevad serveriadministraatorid Lightning-sõlme haldamiseks RTL-i.


**Märkus!**


Lightning Node'i sisemise sõlme ühendamine ebaõnnestub - Kui sisemine ühendus ebaõnnestub, kinnitage:


1. Bitcoin On-Chain sõlm on täielikult sünkroniseeritud

2. Sisene välgussõlm on "Aktiveeritud" jaotises "Välk" > "Seaded" > "BTC välguseaded"


Kui te ei saa oma Lightning-sõlmega ühendust, võite proovida oma serveri taaskäivitamist või lugeda lisateavet BTCPay Serveri ametlikust dokumentatsioonist; https://docs.btcpayserver.org/Troubleshooting/. Te ei saa oma poes Lightning-makseid vastu võtta enne, kui teie Lightning-sõlm ilmub "Online". Proovige testida oma Lightning-ühendust, klõpsates lingil "Public Node Info".


### Välk Wallet


Vasakpoolse menüüriba valikust Lightning Wallet leiavad serveri administraatorid hõlpsasti ligipääsu RTLile, oma avaliku sõlme infole ja Lightningi seadetele, mis on seotud nende BTCPay serveri kauplusega.


#### Sisene sõlme info


Serveri administraatorid saavad klõpsata sisemise sõlme infolehel, et vaadata oma serveri olekut (Online/Offline) ja Clearneti või [Tori](https://planb.academy/resources/glossary/tor) ühendusstringi.


![image](assets/en/033.webp)


#### Muuda ühendust


Välise Lightning-sõlme muutmiseks minge jaotisse "Lightning Settings" ja klõpsake "Change connection" (jaotise "Public Node info" kõrval). See nullib olemasoleva seadistuse. Sisestage uued sõlme andmed, klõpsake nuppu Save (Salvesta) ja pood ajakohastub vastavalt.


![image](assets/en/034.webp)


#### Teenused


Kui serveri administraator otsustab paigaldada Lightningi rakendamiseks mitu teenust, loetletakse need siin. LND standardse rakendamise puhul on administraatoritel Ride The Lightning (RTL) standardne vahend sõlmede haldamiseks.


#### BTC Lightning Wallet seaded


Pärast Lightning-sõlme lisamist poodi eelmises etapis, saavad poeomanikud selle siiski oma poe jaoks deaktiveerida, kasutades Lightning-seadete ülaosas asuvat lülitusklahvi.


![image](assets/en/035.webp)


#### Lightning Maksevõimalused


Poeomanikud saavad oma klientide Lightning-kogemuse parandamiseks määrata järgmised parameetrid.



- Välkmaksete summade kuvamine Satoshis.
- Lisage Lightning Invoice-le privaatsete kanalite hüppevihjed.
- Ühtlustage On-Chain ja Lightning makse URL/QR-koodid kassas.
- Määrake välkarvete kirjelduse mall.


#### LNURL


Poeomanikud saavad valida, kas kasutada või mitte kasutada LNURLi. Lightning Network URL ehk LNURL on Lightning Payeri ja makse saaja vahelise suhtluse kavandatav standard. LNURL on lühidalt öeldes bech32-kodeeritud URL, mille eesliide on LNURL. Lightning Wallet peaks URL-i dekodeerima, võtma sellega ühendust ja ootama JSON-objekti edasiste juhistega, eelkõige LNURL-i käitumist määratleva sildiga.



- LNURL-i lubamine
- LNURL klassikaline režiim
  - Wallet ühilduvus, Bech32 kodeeritud (klassikaline) vs selge tekstiga URL (tulemas)
- Lubage makse saajal edastada märkus.


### Näide 1


#### Ühendage Lightning sisesõlme (administraator) abil Lightningiga


See valik on saadaval ainult siis, kui te olete selle instantsi administraator või kui administraator on muutnud vaikimisi seadeid nii, et kasutajad saavad kasutada sisemist välgussõlme.


Administraatorina klõpsake vasakul menüüribal Lightning Wallet. BTCPay Server palub teil valida üks kahest Lightning Node'i ühendamise võimalusest: sisesõlm või kohandatud väline sõlm. Klõpsake valikut "Kasuta sisemist sõlme" ja seejärel klõpsake "Salvesta"


#### Lightning-sõlme haldamine (RTL)


Pärast sisemise Lightning-sõlme ühendamist uuendab BTCPay Server ja kuvab teate "BTC Lightning-sõlm uuendatud", mis kinnitab, et olete nüüd Lightning'i oma kauplusega ühendanud.


Välgussõlme haldamine on serveri administraatori ülesanne. See hõlmab järgmist:


- Tehingu haldamine
- Likviidsuse haldamine
  - Sissetulev likviidsus
  - Väljaminev likviidsus
- Kolleegide ja kanalite haldamine
  - Ühendatud eakaaslased
  - Kanalitasud
  - Kanali staatus
- Teha sagedased varukoopiad kanali seisunditest.
- Marsruudiaruannete kontrollimine
- Teise võimalusena võite kasutada selliseid teenuseid nagu Loop.


Kõik välgumihaarete haldamine toimub standardselt RTL-i abil (eeldusel, et kasutate LND rakendust). Administraatorid saavad BTCPay Serveris klõpsata oma Lightning Wallet-l ja leida nupu RTL-i avamiseks. BTCPay Serveri peamine armatuurlaud on nüüd uuendatud Lightning Network plaatidega, sealhulgas kiire juurdepääs RTLile.


### Näide 2


#### Ühendage välk koos Albyga


Alby-suguse hooldajaga ühendamisel peaksid poeomanikud esmalt looma konto ja külastama veebilehte https://getalby.com/


![image](assets/en/036.webp)


Pärast Alby konto loomist minge oma BTCPay Serveri kauplusesse.


1. samm: klõpsake juhtpaneelil või rahakottide all "Lightning" nupule "Set up a Lightning node".


![image](assets/en/037.webp)


2. samm: Sisestage oma Wallet ühendusandmed, mille Alby on andnud. Klõpsake Alby juhtpaneelil Wallet. Siit leiate "Wallet Connection Credentials". Kopeerige need volitused. Sisestage Alby poolt saadud volitused BTCPay Serveri ühenduse konfiguratsiooniväljale.


![image](assets/en/038.webp)


3. samm: Pärast BTCPay Serverile ühenduse üksikasjade esitamist klõpsake nupule "Testühendus", et tagada ühenduse nõuetekohane toimimine. Märkige ekraani ülaosas olevat teadet "Ühendus välgumihkliinikuga edukas". See kinnitab, et kõik töötab ootuspäraselt.


![image](assets/en/039.webp)


4. samm: Klõpsake nuppu "Salvesta" ja teie pood on nüüd Alby poolt Lightning-sõlmega ühendatud.


![image](assets/en/040.webp)


**!Märkus!**


Ärge kunagi usaldage hoidjale Lightning lahendus rohkem väärtust, kui olete valmis kaotama.


### Oskuste kokkuvõte


Selles osas õppisite:



- Kuidas ühendada sisemine või väline Lightning-sõlm
- Erinevate välguga seotud plaatide sisu ja funktsioonid armatuurlaual
- Kuidas konfigureerida Lightning Wallet, kasutades Voltage Surge või Alby funktsiooni


### Teadmiste hindamine Praktiline ülevaade


Kirjeldage mõningaid erinevaid võimalusi Lightning Wallet ühendamiseks teie kauplusega.


# BTCPay server Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Ülevaade armatuurlauast


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server on modulaarne tarkvarapakett. Siiski on olemas standardid, mida iga BTCPay Server peab järgima ning need standardid reguleerivad administraatori ja kasutajate vahelist suhtlust. Alustades armatuurlauast. Iga BTCPay Serveri peamine sisenemispunkt pärast sisselogimist. Dashboard annab ülevaate teie poe tulemuslikkusest, Wallet praegusest saldost ja viimase 7 päeva tehingutest. Kuna tegemist on modulaarse vaatega, võivad pluginad seda vaadet enda kasuks kasutada ja luua oma plaadid Dashboardile. Sellel kursusel arutame kogu BTCPay Serveris ainult standardseid pluginaid ja rakendusi koos nende vastavate vaadetega.


### Armatuurlaua plaadid


BTCPay serveri armatuurlaua põhivaates on saadaval paar standardset plaati. Need plaadid on mõeldud poe omanikule või administraatorile, et ta saaks oma poodi kiiresti hallata ühes ülevaates.



- Wallet tasakaal
- Tehingu aktiivsus
- Lightning Balance (kui Lightning on poes lubatud)
- Lightning Teenused (kui Lightning on poes lubatud)
- Hiljutised tehingud.
- Hiljutised arved
- Praegused aktiivsed ühisrahastused
- Kaupluse tulemuslikkus / enimmüüdud kaubad.


### Wallet tasakaal


Wallet saldoplaat annab kiire ülevaate teie Wallet rahalistest vahenditest ja tulemuslikkusest. Seda saab vaadata kas BTC- või Fiat-valuutas nädala-, kuu- või aastagraafikuna.


![image](assets/en/041.webp)


### Tehingu aktiivsus


Wallet saldoplaadi kõrval näitab BTCPay Server kiirülevaadet väljamaksetest, tehingutest viimase 7 päeva jooksul ja sellest, kas teie pood on väljastanud tagasimakseid. Vajutades nupule Manage (Halda), jõuate pooleliolevate väljamaksete haldamisse (rohkem teavet väljamaksete kohta leiate peatükist BTCPay Server - Payments (Maksed)).


![image](assets/en/042.webp)


### Lightning Balance


See on nähtav ainult siis, kui välk on aktiveeritud.


Kui administraator on lubanud Lightning Network juurdepääsu, on BTCPay serveri armatuurlaual nüüd uus plaat teie Lightning-sõlme teabega. Kui palju BTC-d on kanalites, kuidas see on tasakaalustatud lokaalselt või eemalt (sissetulev või väljaminev likviidsus), kas kanalid on sulgemas või avanemas ja kui palju Bitcoin hoiab On-Chain välgussõlmes.


![image](assets/en/043.webp)


### Välguteenused


See on nähtav ainult siis, kui välk on aktiivne.


BTCPay serveri armatuurlaual näevad administraatorid lisaks oma Lightning-saldole ka Lightning-teenuste plaati. Siit leiavad administraatorid Lightning-sõlme haldamiseks kasutatavate tööriistade kiirnupud; näiteks Ride the Lightning on üks BTCPay Serveri standardsetest tööriistadest Lightning-sõlme haldamiseks.


![image](assets/en/044.webp)


### Hiljutised tehingud


Paanil Viimased tehingud kuvatakse teie poe kõige hiljutisemad tehingud. BTCPay serveri administraator saab nüüd ühe klõpsuga näha viimast tehingut ja näha, kas sellele on vaja tähelepanu pöörata.


![image](assets/en/045.webp)


### Hiljutised arved


Paanil Viimased arved kuvatakse 6 viimast BTCPay serveri poolt genereeritud arvet, sealhulgas staatus ja Invoice summa. Paani juurde kuulub ka nupp "Vaata kõiki", et pääseda hõlpsasti Invoice ülevaatele.


![image](assets/en/046.webp)


### Müügipunktid ja ühisrahastused


Kuna BTCPay Server pakub komplekti standardseid pluginaid või rakendusi, on BTCPay Serveri kaks peamist pluginat Point Of Sale ja Crowdfund. Iga poe ja Wallet puhul võib BTCPay Serveri kasutaja generate nii palju Point Of Sales'i või Crowdfund'i kasutada, kui ta seda vajalikuks peab. Iga neist loob uue armatuurlaua plaadi, mis näitab pluginate jõudlust.


![image](assets/en/047.webp)


Pane tähele väikest erinevust müügipunkti ja ühisrahastuse plaadi vahel. Administraator näeb müügipunkti plaadil kõige rohkem müüdud esemeid. Crowdfund'i plaadil muutub see Top Perks'iks. Mõlemal plaadil on kiirnupud vastava rakenduse haldamiseks ja viimaste arvete vaatamiseks, mis on loodud tippartiklite või tipphüvitiste järgi.


![image](assets/en/048.webp)


**!?Märkus!?**


Saldograafid ja hiljutised tehingud on saadaval ainult On-Chain makseviiside puhul. Teave Lightning Network saldode ja tehingute kohta on tööplaanis. Alates BTCPay serveri versioonist 1.6.0 on saadaval põhilised Lightning Network saldod.


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Peamise maandumislehe plaatide põhiline paigutus on tuntud kui armatuurlaud.
- Põhiline arusaam iga plaadi sisust.


### Teadmiste hindamise läbivaatamine


Loetlege armatuurlaual nii palju plaate mälust kui võimalik.


## BTCPay Server - poe seaded


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


BTCPay Serveri tarkvaras on teada kahte tüüpi seadeid. BTCPay Serveri poespetsiifilised seaded, seadete nupp, mis asub vasakul menüüriba all Dashboardi all, ja BTCPay Serveri seaded, mis asub menüüriba allosas, otse konto kohal. BTCPay Serveri serveri spetsiifilisi seadeid saavad vaadata ainult serveri administraatorid.


Poe seaded koosnevad paljudest vahekaartidest, et kategoriseerida iga seadete komplekti.



- Üldine
- Hinnad
- Kassa välimus
- Juurdepääsutunnused
- Kasutajad
- Rollid
- Veebikonksud
- Väljamaksete töötlejad
- E-kirjad
- Vormid


### Üldine


Üldiste seadete vahekaardil määravad poeomanikud oma brändi ja makse vaikimisi. Poe esmasel seadistamisel anti poe nimi; see kajastub üldiste seadete jaotises poe nimi. Siin saab poeomanik määrata ka oma veebilehe brändingu ja poe ID, et administraator saaks selle andmebaasis ära tunda.


#### Branding


Kuna BTCPay Server on FOSS, saab poeomanik teha oma poele sobiva brändi. Määrake brändi värvi, salvestage oma brändi logod ja lisage kohandatud CSS avalike/kliendile suunatud lehekülgede jaoks (arved, maksetaotlused, maksete tõmbamine)


#### Maksmine


Maksete seadetes saavad poeomanikud määrata oma poe vaikimisi valuuta (kas Bitcoin või mis tahes fiat-valuuta).


#### Võimaldab igaühel arveid koostada


See seade on mõeldud arendajatele või ehitajatele BTCPay Serveri peal. Kui see seade on teie poe jaoks lubatud, võimaldab see välismaailmale luua arveid teie BTCPay Serveri instantsil.


#### Lisage arvetele lisatasu (võrgutasu)


BTCPay funktsioon, mis kaitseb kaupmehi Dust rünnakute eest või kliente hiljem suurte tasude tekkimise eest, kui kaupmees peab korraga liigutama suure summa Bitcoin. Näiteks lõi klient 20$ eest Invoice ja maksis selle osaliselt, makstes 1$ 20 korda, kuni Invoice oli täielikult tasutud. Kaupmehel on nüüd suurem tehing, mis suurendab Mining kulusid, kui kaupmees otsustab neid vahendeid hiljem liigutada. Vaikimisi kohaldab BTCPay Invoice kogusummale täiendavat võrgukulu, et katta see kulu kaupmehe jaoks, kui Invoice makstakse mitme tehinguga. BTCPay pakub mitmeid võimalusi selle kaitsefunktsiooni kohandamiseks. Saate kohaldada võrgutasu:



- Ainult juhul, kui klient teeb Invoice eest rohkem kui ühe makse (ülaltoodud näites, kui klient lõi Invoice 20\$ eest ja maksis 1\$, on Invoice kogusumma nüüd 19\$ + võrgutasu. Võrgutasu rakendatakse pärast esimest makset)
- Iga makse puhul (sealhulgas esimene makse, meie näites on kogusumma 20\$ + võrgutasu kohe, isegi esimesel maksel)
- Mitte kunagi võrgutasu lisamine (lülitab võrgutasu täielikult välja)


Kuigi see kaitseb Dust tehingute eest, võib see ka negatiivselt mõjutada ettevõtteid, kui sellest ei teavitata nõuetekohaselt. Klientidel võivad tekkida lisaküsimused ja nad võivad arvata, et te küsite neilt liiga palju.


#### Invoice aegub, kui kogu summa ei ole makstud pärast?


Invoice taimeri on vaikimisi seadistatud 15 minutile. Taimer toimib kaitsemehhanismina volatiilsuse vastu, kuna see lukustab Bitcoin summa vastavalt Bitcoin ja Exchange vahekordadele. Kui klient ei maksa Invoice kindlaksmääratud aja jooksul, loetakse Invoice aegunuks. Invoice loetakse "makstud" kohe, kui tehing on Blockchain-l nähtav (null kinnitust), ja "lõpetatud", kui see jõuab kaupmehe määratud kinnituste arvuni (tavaliselt 1-6). Taimer on kohandatav minutite kaupa.


#### Kas Invoice on makstud isegi siis, kui makstud summa on X% väiksem kui oodatud?


Kui klient kasutab Exchange Wallet otse Invoice eest tasumiseks, võtab Exchange väikese tasu. See tähendab, et sellist Invoice ei loeta täielikult lõpetatuks. Invoice on märgitud kui "osaliselt tasutud". Siin saate määrata protsendi, kui kaupmees soovib aktsepteerida alatasa makstud arveid.


### Hinnad


Kui BTCPay serveris genereeritakse Invoice, vajab see alati kõige ajakohasemat ja täpsemat Bitcoin-to-fiat hinda. Uue poe loomisel BTCPay Serveris palutakse administraatoritel määrata oma eelistatud hinnaallikas. Pärast poe loomist saavad poeomanikud igal ajal sellel vahekaardil oma hinnaallikat muuta.


#### Täiustatud määrareeglite skriptimine


Kasutavad peamiselt võimsad kasutajad. Kui see on sisse lülitatud, saavad poeomanikud luua skripte, mis käsitlevad hinnakäitumist ja seda, kuidas klientidelt tasu küsida.


#### Testimine


Teie eelistatud valuutapaaride kiire testimise koht. See funktsioon sisaldab ka võimalust kontrollida vaikimisi valuutapaare REST päringu kaudu.


### Kassa välimus


Väljaku "Kassaväljund" vahekaart algab Invoice-spetsiifiliste seadistustega ja vaikimisi makseviisiga ning võimaldab konkreetsed makseviisid, kui seatud nõuded on täidetud.


#### Invoice seaded


Vaikimisi makseviisid. BTCPay Server pakub oma standardkonfiguratsioonis kolme võimalust.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain ja Lightning)


Me saame määrata oma poe jaoks parameetrid, mille kohaselt klient suhtleb Lightningiga ainult siis, kui hind on väiksem kui X summa, ja vastupidi On-Chain tehingute puhul, kui X on suurem kui Y, esitatakse alati On-Chain maksevõimalus.


![image](assets/en/049.webp)


#### Kassa


Alates BTCPay Serveri versioonist 1.7 võeti kasutusele uus Checkout Interface, Checkout V2. Kuna versioon 1.9 standardiseeriti, saavad administraatorid ja poeomanikud endiselt määrata kassat eelmisele versioonile. Kasutades lülitit "Kasuta klassikalist kassat", saab poeomanik taastada poe eelmise kassakorralduse. BTCPay Serveril on ka valitud eelseadistused veebikaubanduse või kaupluses toimuva väljamakse kogemuse jaoks.


![image](assets/en/050.webp)


Kui klient suhtleb kauplusega ja genereerib Invoice, on Invoice-le määratud kehtivusaeg. BTCPay Server seab selle vaikimisi 5 minutiks ja administraatorid saavad seda kohandada vastavalt oma eelistustele. Kassalehte saab veelgi kohandada, kontrollides järgmisi parameetreid:



- Tähistage maksmist konfettide näitamisega
- Näita poe pealkirja (nimi ja logo)
- Näita nuppu "Maksa Wallet"
- On-Chain ja off-chain maksete ühtlustamine URL/QRid
- Välkmaksete summade kuvamine Satoshis
- Automaatne keele tuvastamine kassas


![image](assets/en/051.webp)


Kui automaatne keele tuvastamine ei ole määratud, kuvab BTCPay Server vaikimisi inglise keelt. Poeomanik saab seda vaikimisi keelt muuta oma eelistatud keeleks.


![image](assets/en/052.webp)


Klõpsake rippmenüüd ja poeomanikud saavad määrata kassalehel kuvatava kohandatud HTML-pealkirja.


![image](assets/en/053.webp)


Selleks, et kliendid teaksid oma makseviisi, võib poeomanik sõnaselgelt määrata oma kassas alati nõudma, et kasutajad valiksid oma eelistatud makseviisi. Kui Invoice on makstud, lubab BTCPay Server kliendil veebipoodi tagasi pöörduda. Poeomanikud võivad selle ümbersuunamise seadistada nii, et seda rakendatakse automaatselt pärast seda, kui klient on maksnud.


![image](assets/en/054.webp)


#### Avalik kättesaamine


Poeomanik saab avaliku kviitungi seadete raames määrata kviitungi leheküljed avalikuks, kuvades kviitungi lehel maksete nimekirja ja QR-koodi, et klient saaks sellele hõlpsasti ligi pääseda.


![image](assets/en/055.webp)


### Juurdepääsutunnused


Juurdepääsutunnuseid kasutatakse teatavate e-kaubanduse integratsioonide või kohandatud integratsioonidega sidumiseks.


![image](assets/en/056.webp)


### Kasutajad


Poe kasutajad on koht, kus poe omanik saab hallata oma töötajaid, nende kontosid ja juurdepääsu poele. Pärast töötajate kontode loomist saab poeomanik lisada poele konkreetseid kasutajaid külaliskasutajatena või omanikena. Töötajate rollide täpsemaks määratlemiseks vaadake järgmist jaotist "BTCPay serveri poe seaded - rollid"


![image](assets/en/057.webp)


### Rollid


Poeomanik ei pruugi leida, et kasutaja standardrollid on piisavalt olulised. Kohandatud rollide seadetes saab poeomanik määratleda iga rolli täpsed vajadused oma äris.


(1) Uue rolli loomiseks klõpsake nuppu "+ Lisa roll".


![image](assets/en/058.webp)


(2) Sisestage rolli nimi, näiteks "Kassapidaja".


![image](assets/en/059.webp)


(3) Konfigureerige rolli individuaalsed õigused.



- Muutke oma kauplusi.
- Haldage oma kauplustega seotud Exchange kontosid.
  - Vaadake oma kauplustega seotud Exchange kontosid.
- Halda oma tõmmatud makseid.
- Loo pull-maksed.
  - Looge heakskiitmata pull-makseid.
- Muuda arveid.
  - Vaata arveid.
  - Looge Invoice.
  - Looge arveid oma kauplustega seotud välgumissõlmedest.
- Vaadake oma kauplusi.
  - Vaata arveid.
  - Vaadake oma maksetaotlusi.
  - Muuda kaupluste veebikonksud.
- Muuta oma maksetaotlusi.
  - Vaadake oma maksetaotlusi.
- Kasutage oma kauplustega seotud välgumihklusi.
  - Vaadake oma kauplustega seotud välkarveid.
  - Looge arveid oma kauplustega seotud välgumissõlmedest.
- Hoiustage raha oma kauplustega seotud Exchange kontodele.
- Exchange kontodelt raha väljavõtmine oma kauplusesse.
- Kauple raha oma poe Exchange kontodel.


Kui roll luuakse, on nimi fikseeritud ja seda ei saa muuta pärast seda, kui see on redigeerimisrežiimis.


![image](assets/en/060.webp)


### Veebikonksud


BTCPay Serveris on uue "Webhooki" loomine üsna lihtne. BTCPay Serveri poe seadetes - vahekaardil "Webhooks" saab poe omanik hõlpsasti luua uue veebikonksu, klõpsates "+ Create Webhook". Veebikonksud võimaldavad BTCPay Serveril saata teie kauplusega seotud HTTP-sündmusi teistele serveritele või e-kaubanduse integratsioonidele.


![image](assets/en/061.webp)


Nüüd olete veebikonksu loomise vaates. Veenduge, et te teate oma Payload URL-i ja kleebige see BTCPay serverisse. Kuigi te kleebisite Payload URL-i, näitab see all veebikonksu saladus. Kopeerige webhooki saladus ja esitage see lõpp-punktis. Kui kõik on seadistatud, saate BTCPay Serveris lülitada sisse "Automaatne uuesti edastamine" BTCPay Server üritab iga ebaõnnestunud saatmist uuesti toimetada 10 sekundi pärast, 1 minuti pärast ja kuni 6 korda 10 minuti pärast. Võite lülitada iga sündmuse vahel või määrata sündmused oma vajaduste järgi. Veenduge, et lubate veebikonksu ja vajutage salvestamiseks nuppu "Add webhook".


![image](assets/en/062.webp)


Veebikonksud ei ole mõeldud Bitpay APIga ühilduvaks. BTCPay Serveris on kaks eraldi IPN-i (BitPay terminites: "Instant Payment Notifications").



- Webhookp
- Teated


Kasutage teavitamise URL-i ainult siis, kui loote arveid Bitpay API kaudu.


### Väljamaksete töötlejad


Väljamaksete töötlejad töötavad koos BTCPay Serveri väljamaksete kontseptsiooniga. Väljamaksete agregaator, et koondada mitu tehingut ja saata need korraga. Väljamaksete töötlejate abil saab poeomanik automatiseerida pakettmakseid. BTCPay Server pakub kahte automatiseeritud väljamaksete meetodit: On-Chain ja off-chain (LN).


Poe omanik saab klõpsata ja konfigureerida mõlemad väljamakseprotsessorid eraldi. Poeomanik võib soovida käivitada On-Chain protsessorit ainult üks kord iga X tunni järel, samas kui off-chain protsessor võib töötada iga paari minuti tagant. On-Chain puhul võite määrata ka eesmärgi, millise ploki puhul see peaks olema kaasatud. Vaikimisi on selleks määratud 1 (või järgmine olemasolev plokk). Pange tähele, et off-chain väljamaksete protsessori seadistamisel on ainult intervallitimeri ja mitte mingi plokkide sihtmärk. Lightning Network maksed on kohesed.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Poeomanikud saavad On-Chain protsessorit konfigureerida ainult siis, kui nende poega on ühendatud Hot Wallet.


![image](assets/en/065.webp)


Pärast väljamakseprotsessori seadistamist saate selle kiiresti eemaldada või muuta, kui naasete BTCPay Server Store'i seadete vahelehele "Väljamaksete protsessor".


**Märkus**


Väljamaksete protsessor On-Chain - Väljamaksete protsessor On-Chain saab töötada ainult kaupluses, mis on konfigureeritud ühendatud Hot Wallet. Kui Hot Wallet ei ole ühendatud, ei ole BTCPay serveril Wallet võtmeid ja ta ei saa väljamakseid automaatselt töödelda.


### E-kirjad


BTCPay Server võib kasutada e-kirju teavituste jaoks või, kui see on õigesti seadistatud, et taastada instantsil loodud kontod. Standardselt ei saada BTCPay Server näiteks salasõna kaotamise korral e-kirja.


![image](assets/en/066.webp)


Enne kui poeomanik saab määrata e-posti reegleid, et käivitada oma poes konkreetseid sündmusi, peab ta kõigepealt seadistama mõned põhilised e-posti seaded. BTCPay Server vajab neid seadeid, et saata e-kirju teie kauplusega seotud sündmuste või paroolide lähtestamise korral.


BTCPay Server lihtsustas selle teabe täitmist, kasutades võimalust "Quick Fill":



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


Kiirtäitmise võimalust kasutades täidab BTCPay Server eelnevalt SMTP-serveri ja pordi väljad. Nüüd peab poeomanik ainult täitma oma andmed, sealhulgas e-posti Address, sisselogimise (mis on tavaliselt võrdne teie e-posti Address-ga) ja oma parooli. BTCPay serveri e-posti seadetes on täiustatud valikuks TLS-sertifikaadi turvakontrolli väljalülitamine; vaikimisi on see sisse lülitatud.


![image](assets/en/067.webp)


E-kirjade reeglite abil saab poe omanik määrata konkreetsed sündmused, mis käivitavad e-kirjade saatmise konkreetsetele e-posti aadressidele.



- Invoice Loodud
- Invoice Saadud makse
- Invoice töötlemine
- Invoice aegunud
- Invoice Arveldatud
- Invoice Invaliidne
- Invoice Maksmine arveldatud


Kui klient on andnud e-posti Address, võivad need käivitajad saata teavet ka kliendile. Poeomanikud saavad eeltäita teemarida, et teha selgeks, miks see e-kiri toimus ja mis selle vallandas.


![image](assets/en/068.webp)


### Vormid


Kuna BTCPay Server ei kogu mingeid andmeid, võib poeomanik soovida lisada oma kassakogemusele kohandatud vormi; sel viisil saab poeomanik koguda kliendilt lisateavet. BTCPay Server Form builder koosneb kahest osast: vormide visuaalne ja täiustatud koodivaade.


Uue vormi loomisel avab BTCPay Server uue akna, milles küsitakse põhiteavet selle kohta, mida soovite, et teie uus vorm küsiks. Kõigepealt peab poe omanik andma oma uuele vormile selge nime; seda nime ei saa pärast selle määramist enam muuta.


![image](assets/en/069.webp)


Pärast seda, kui poeomanik on andnud vormile nime, võite lülitada ka lüliti "Allow form for public use" asendisse ON ja see lülitub Green. See tagab, et vormi kasutatakse igas kliendiga kokkupuutuvas kohas. Näiteks kui poeomanik loob eraldi Invoice mitte oma müügipunkti kaudu, võib ta ikkagi soovida kliendilt teavet koguda. See lülitus võimaldab seda teavet koguda.


![image](assets/en/070.webp)


Iga vorm algab vähemalt 1 uue vormiväljaga. Poe omanik saab valida, mis tüüpi väli see peaks olema.



- Tekst
- Number
- Parool
- E-post
- URL
- Telefoninumbrid
- Kuupäev
- Varjatud väljad
- Fieldset
- Tekstiala avatud kommentaaride jaoks.
- Valikuvõimaluse valija


Igal tüübil on oma parameetrid, mida täita. Poe omanik saab selle seadistada oma maitse järgi. Esimese loodud välja all saavad poeomanikud lisada sellele vormile uusi välju.


![image](assets/en/071.webp)


#### Täiustatud kohandatud vormid


BTCPay Server võimaldab teil ka vormide koostamist koodis. JSON, eriti. Selle asemel, et vaadata redaktorit, saavad poeomanikud klõpsata nupule CODE otse redaktori kõrval ja pääseda oma Vormide koodi sisse. Välja määratluses saab määrata ainult järgmisi välju; väljade väärtused on salvestatud Invoice metaandmetesse:



| Väli | Kirjeldus |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant | Kui on true, peab .value olema määratud vormi definitsioonis ja kasutaja ei saa välja väärtust muuta. (näide: vormi definitsiooni versioon) |
| .fields.type | HTML sisenditüüp: text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel |
| .fields.options | Kui .fields.type on select, siis valitavate väärtuste loend |
| .fields.options.text | Selle valiku puhul kuvatav tekst |
| .fields.options.value | Välja väärtus, kui see valik on märgitud |
| .fields.type=fieldset | Loob HTML fieldset-i alamväljade .fields.fields ümber (vt allpool) |
| .fields.name | Välja JSON-omaduse nimi, nagu see ilmub arve metaandmetes |
| .fields.value | Välja vaikeväärtus |
| .fields.required | kui on true, on väli kohustuslik |
| .fields.label | Välja silt |
| .fields.helpText | Täiendav tekst välja selgitamiseks. |
| .fields.fields | Saate oma välju organiseerida hierarhiliselt, võimaldades alamväljade pesastamist arve metaandmetesse. See struktuur aitab teil kogutud teavet paremini organiseerida ja hallata, muutes sellele juurdepääsu ja tõlgendamise lihtsamaks. Näiteks kui teil on vorm, mis kogub klienditeavet, saate rühmitada väljad ülemvälja customer alla. Selle ülemvälja sees võivad olla alamväljad nagu name, Email ja address. |

Välja nimi kujutab endast JSON-omaduse nime, mis salvestab kasutaja poolt antud väärtuse Invoice metaandmetes. Mõningaid tuntud nimesid saab tõlgendada ja muuta, et kohandada Invoice seadeid.



| Välja nimi       | Kirjeldus             |
| ---------------- | ---------------------- |
| invoice_amount   | Arve summa            |
| invoice_currency | Arve valuuta          |

Invoice väljad saab automaatselt eeltäita, lisades vormi URL-ile päringustringid, näiteks "?your_field=value".


Siin on mõned selle funktsiooni kasutusjuhud:



- Kasutaja sisestamise abistamine: Väljade eeltäitmine teadaolevate kliendiinformatsioonidega, et hõlbustada vormi täitmist. Näiteks kui te teate juba kliendi e-posti aadressi Address, saate eeltäita e-posti väli, et säästa nende aega.
- Isikupärastamine: Kohandage vorm kliendi eelistuste või segmenteerimise alusel. Näiteks kui teil on erinevad kliendiklassid, saate vormi eelnevalt täita asjakohaste andmetega, näiteks nende liikmelisuse taseme või konkreetsete pakkumistega.
- Jälgimine: Jälgige klientide külastuste allikat, kasutades varjatud välju ja eeltäidetud väärtusi. Näiteks saate luua lingid eeltäidetud utm_media väärtustega iga turunduskanali jaoks (nt Twitter, Facebook, e-post). See aitab teil analüüsida oma turundustegevuse tõhusust.
- A/B testimine: Täitke väljad eelnevalt erinevate väärtustega, et testida erinevaid vormiversioone, mis võimaldab teil optimeerida kasutajakogemust ja konversioonimäära.


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Poe seadete vahekaartide paigutus ja funktsioonid
- Palju võimalusi Exchange aluseks olevate määrade, osaliste maksete, väikeste alamaksete ja muu sellise käsitlemise peenhäälestamiseks.
- Kohandage kassaväljundit, sealhulgas hinnast sõltuvat põhiketti vs. Lightningi võimaldamist arvetel.
- Haldage kaupluste juurdepääsu ja õiguste tasemeid rollide lõikes.
- Automaatsete e-kirjade ja nende käivitajate konfigureerimine
- Loo kohandatud vormid kliendi lisateabe kogumiseks kassas.


### Teadmiste hindamine


#### KA läbivaatamine


Mis vahe on poe seadete ja serveri seadete vahel?


#### KA Hüpoteetiline


Kirjeldage mõningaid valikuid, mida võiksite valida jaotises Kassade välimus > Invoice seaded, ja miks.


## BTCPay Server - Serveri seaded


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server koosneb kahest erinevast seadistuse vaatest. Üks on pühendatud poe seadetele ja teine serveri seadetele. Viimane on kättesaadav ainult serveri administraatoritele, mitte poe omanikele. Serveri administraatorid saavad lisada kasutajaid, luua kohandatud rolle, konfigureerida e-posti serverit, määrata poliitikaid, käivitada hooldusülesandeid, kontrollida kõiki BTCPay Serveriga seotud teenuseid, laadida serverisse faile või kontrollida logisid.


### Kasutajad


Nagu eelmises osas mainitud, saavad serveriadministraatorid kutsuda kasutajaid oma serverisse, lisades neid vahekaardile Kasutajad.


### Kogu serverit hõlmavad kohandatud rollid


BTCPay Serveril on kahte tüüpi kohandatud rollid: kaupluse-spetsiifilised kohandatud rollid ja kogu serverit hõlmavad kohandatud rollid BTCPay Serveri seadetes. Mõlemad sisaldavad sarnaseid õigusi, kuid kui need on määratud BTCpay Serveri seadete - Rollid vahekaardil, on rakendatud roll kogu serverit hõlmav ja kehtib mitme kaupluse kohta. Pange tähele, et Serveri seadetes on kohandatud rollidele lisatud silt "Server-wide" (kogu serverit hõlmav).


![image](assets/en/072.webp)


### Kogu serverit hõlmavad kohandatud rollid


Kogu serverit hõlmav kohandatud rollide õiguste kogum;



- Muutke oma kauplusi.
- Haldage oma kauplustega seotud Exchange kontosid.
  - Vaadake oma kauplustega seotud Exchange kontosid.
- Halda oma tõmmatud makseid.
- Loo pull-maksed.
  - Looge heakskiitmata pull-makseid.
- Muuda arveid.
  - Vaata arveid.
  - Looge Invoice.
  - Looge arveid oma kauplustega seotud välgumissõlmedest.
- Vaadake oma kauplusi.
  - Vaata arveid.
  - Vaadake oma maksetaotlusi.
  - Muuda kaupluste veebikonksud.
- Muuta oma maksetaotlusi.
  - Vaadake oma maksetaotlusi.
- Kasutage oma kauplustega seotud välgumihklusi.
  - Vaadake oma kauplustega seotud välkarveid.
  - Looge arveid oma kauplustega seotud välgumissõlmedest.
- Hoiustage raha oma kauplustega seotud Exchange kontodele.
- Exchange kontodelt raha väljavõtmine oma kauplusesse.
- Kauple raha oma poe Exchange kontodel.


**!?Märkus!?**


Kui roll luuakse, on nimi fikseeritud ja seda ei saa muuta pärast seda, kui see on redigeerimisrežiimis.


### E-post


Kogu serverit hõlmavad e-posti seaded näevad välja sarnaselt kauplusekohaste e-posti seadetega. See seadistus ei käsitse siiski mitte ainult kaupluste või administraatori logide, vaid ka muude sündmuste vallandamisi. See e-posti seadistus teeb ka parooli taastamise BTCPay serveris sisselogimise ajal kättesaadavaks. See toimib sarnaselt poespetsiifiliste seadistustega; administraatorid saavad kiiresti täita oma e-posti parameetrid ja sisestada oma e-posti volitused, mis võimaldab serveril saata e-kirju.


![image](assets/en/073.webp)


### Poliitikad


BTCPay Serveri poliitikaadministraatorid saavad määrata erinevaid seadistusi sellistes teemades nagu Olemasoleva kasutaja seaded, Uue kasutaja seaded, Teavituse seaded ja Hoolduse seaded. Need on mõeldud uute kasutajate registreerimiseks administraatorite või tavakasutajatena või BTCPay Serveri varjamiseks otsingumootorite eest, lisades selle oma serveri päisesse.


![image](assets/en/074.webp)


#### Olemasoleva kasutaja seaded


Siin saadaval olevad valikud on kohandatud rollidest eraldi. Need täiendavad õigused võivad muuta poe või selle omaniku rünnakute suhtes haavatavaks. Poliitikad, mida võib lisada olemasolevatele kasutajatele:



- Lubage mitteadminidel kasutada oma kauplustes sisemist Lightning-sõlme.
  - See võimaldaks poeomanikel kasutada serveri administraatori Lightning-sõlme ja seega ka tema raha! Ettevaatust, see ei ole lahendus Lightningile juurdepääsu andmiseks.
- Lubage mitte-adminidel luua oma kaupluste jaoks Hot rahakotte.
  - See võimaldaks kõigil, kellel on konto teie BTCPay serveri instantsil, luua Hot-pangakotte ja salvestada nende taastamise seed administraatori serveris. See võib muuta administraatori vastutavaks kolmandate isikute raha hoidmise eest!
- Luba mitte-adminidel importida Hot rahakotte oma kauplustesse.
  - Sarnaselt eelmisele Hot rahakottide loomise teemale võimaldab see poliitika importida Hot Wallet, kusjuures samad ohud, mida mainiti Hot rahakottide loomise osas.


![image](assets/en/075.webp)


#### Uued kasutaja seaded


Saame määrata mõned olulised seaded, et hallata uusi kasutajaid, kes tulevad serverisse. Saame määrata uute registreerimiste kinnituse e-posti, keelata uute kasutajate loomise sisselogimisekraani kaudu ja piirata mitte-adminide juurdepääsu kasutajate loomisele API kaudu.



- Nõuab registreerimise kinnituse e-posti aadressi.
  - Serveri administraator peab olema seadistanud e-posti serveri.
- Uute kasutajate registreerimise keelamine serveris
- Keelake mitteadminite juurdepääs kasutaja loomise API-punktile.


Vaikimisi on BTCPay Server lülitatud välja "Lülita uute kasutajate registreerimine serveris välja" ja lülitanud välja mitteadminite juurdepääsu kasutaja loomise API-punktile. See on turvalisuse huvides, et suvalised inimesed, kes satuvad teie BTCPay sisselogimise peale, ei saaks kontosid luua.


![image](assets/en/076.webp)


#### Teavituse seaded


![image](assets/en/077.webp)


#### Hoolduse seaded


BTCPay Server on avatud lähtekoodiga projekt, mis elab GitHubis. Kui BTCPay Server annab välja uue versiooni, saavad administraatorid teada, et uus versioon on saadaval. Samuti võivad administraatorid soovida vältida, et otsingumootorid (nagu Google, Yahoo ja DuckDuckGo) ei indekseeriks BTCPay Serveri domeeni. Kuna BTCPay Server on FOSS, võivad arendajad kogu maailmas soovida luua uusi funktsioone. BTCPay Serveril on eksperimentaalne funktsioon, mille sisselülitamine võimaldab administraatoritel kasutada funktsioone, mis ei ole mõeldud tootmises kasutamiseks, vaid pigem testimiseks.



- Kontrollige väljaandeid GitHubis ja teavitage, kui uus BTCPay Serveri versioon on saadaval.
- Hoidke otsingumootoreid selle saidi indekseerimisest kõrvale
- Lubage eksperimentaalsed funktsioonid.


![image](assets/en/078.webp)


#### Plugins


BTCPay Server saab lisada pluginad ja laiendada oma funktsioonikomplekti. Vaikimisi laaditakse pluginad BTCPay Serveri pluginate looja repositooriumist. Administraator võib siiski valida, kas pluginad on eelversioonis, ja kui pluginate arendaja seda lubab, saab serveri administraator nüüd paigaldada pluginate beetaversioone.


![image](assets/en/079.webp)


##### Kohandamise seaded


BTCPay serveri standardne kasutuselevõtt on ligipääsetav paigaldamise ajal loodud domeeni kaudu. Serveri administraator võib siiski root-domeeni ümber määrata ja kuvada ühe loodud rakenduse konkreetsest poest. Serveriadministraator saab ka kaardistada konkreetsed domeenid konkreetsetele rakendustele.



- Näidata rakendust veebisaidi juurest
  - Kuvab nimekirja võimalikest rakendustest, mida saab kuvada juurdomeenil.


![image](assets/en/080.webp)



- Kaardistage konkreetsed domeenid konkreetsetele rakendustele.
  - Kui klõpsate konkreetse domeeni seadistamiseks konkreetsete rakenduste jaoks, saab administraator määrata nii palju domeene, mis on suunatud konkreetsetele rakendustele, kui vaja.


![image](assets/en/081.webp)


#### Plokkide uurijad


BTCPay Server on standardselt varustatud Mempool.space'iga, mis on tehinguteks mõeldud Block explorer-ga. Kui BTCPay Server genereerib uue Invoice ja sellega on seotud tehing, saab poe omanik tehingu avamiseks klõpsata. BTCPay Server osutab vaikimisi Mempool.space'ile kui Block explorer-le, kuid serveri administraator võib seda muuta oma eelistatud valikuks.


![image](assets/en/082.webp)


### Teenused


"BTCPay serveri seaded: Teenused" on ülevaade komponentidest, mida teie BTCPay Server kasutab. Teenused, mida teie BTCPay Server pakub, võivad sõltuvalt kasutuselevõtumeetodist erineda.


BTCPay serveri administraator saab klõpsata iga teenuse taga olevale "Vaata teavet", et avada see ja määrata konkreetsed seaded.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay avab LND GRPC-teenuse väljastpoolt tarbimiseks; ühendusandmed leiate sellest konkreetsest seadete menüüst; ühilduvad rahakotid on loetletud siin. BTCPay Server pakub ühendamiseks ka QR-koodi, mida saab skaneerida ja rakendada mobiilis Wallet.


Serveriadministraatorid saavad avada rohkem üksikasju, et näha.



- Peremehe andmed
- SSL-i kasutamine
- Makroonid
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL-salakirjakomplekt (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay avaldab LND REST-teenuse väljastpoolt tarbimiseks; ühendusandmed leiate [siit](https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay); ühilduvad rahakotid on loetletud [siin](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server). Ühilduvate rahakottide hulgas on Joule, Alby ja ZeusLN. BTCPay Server pakub ühenduse loomiseks QR-koodi, mida saab skannida ja rakendada ühilduvas Wallet-s.



- REST URI
- Makroonid
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon


#### LND seed Varukoopia


LND seed varukoopia on kasulik, et taastada vahendid teie LND Wallet-st, kui server on kahjustatud. Kuna Lightning-sõlm on Hot-Wallet, leiate konfidentsiaalset seed teavet sellelt leheküljelt.


LND dokumenteerib taastamisprotsessi. Dokumentatsiooni vt https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md.


#### Ride The Lightning


Ride the Lightning on avatud lähtekoodiga tarkvarana loodud Lightning-sõlme haldusvahend. BTCPay Server kasutab RTL-i kui Lightning-sõlmede halduskomponenti oma virna. BTCPay Serveri administraatorid pääsevad RTLi juurde serveri seadete - teenuste vahekaardil või Lightning Wallet klõpsates.


#### Full node P2P


Serveriadministraatorid võivad soovida ühendada oma Bitcoin sõlme mobiilse Wallet-ga. Sellel leheküljel on teave selle kohta, kuidas Full node-ga kaugühendust luua P2P protokolli kaudu. Selle kursuse kirjutamise ajal on BTCPay Server loetleb Blockstream Green ja Wasabi rahakotid ühilduvate rahakottidena. BTCPay Server pakub ühenduse loomiseks QR-koodi, mida saab skannida ja rakendada ühilduvas Wallet-s.


#### Full node RPC


Sellel lehel on teave Full node-ga kaugühenduse loomiseks RPC protokolli kaudu.


#### SSH


SSH-d kasutatakse hoolduse eesmärgil. BTCPay Server näitab algset ühenduskäsku teie serverisse jõudmiseks ja SSH avalikke võtmeid, mis on lubatud teie serveriga ühendumiseks. Serveri administraatorid võivad soovida SSH-ümberkorraldused BTCPay Serveri kasutajaliidese kaudu keelata.


#### Dünaamiline DNS


Dünaamiline DNS võimaldab teil kasutada stabiilset DNS-nime, mis osutab teie serverile, isegi kui teie IP Address muutub regulaarselt. See on soovitatav, kui te majutate BTCPay Serverit kodus ja soovite, et teie Serverile oleks juurdepääsuks selge domeen.


Pange tähele, et HTTPS-sertifikaadi saamiseks peate oma NAT-i ja BTCPay Serveri paigaldamise korralikult konfigureerima.


### Teema


BTCPay Server on standardselt varustatud kahe teemaga: Hele ja tume režiim. Neid saab vahetada, klõpsates vasakus allosas oleval kontol ja vahetades tumedate ja heledate teemade vahel. BTCPay Serveri administraatorid saavad lisada omaenda teema, pakkudes kohandatud CSS-teemat.


Administraatorid saavad laiendada Light/Dark teemat, lisades oma kohandatud CSS-i või seadistades oma kohandatud teema täielikult kohandatud teemaks.


![image](assets/en/084.webp)


#### Server Branding


Serveriadministraatorid saavad muuta BTCPay serveri brändingut, määrates kogu serverit hõlmava ettevõtte brändingu. Kuna BTCPay Server on FOSS, saavad serveriadministraatorid tarkvara valget värvi märgistada ja selle välimust oma ettevõttele sobivaks kohandada.


![image](assets/en/085.webp)


### Hooldus


Serveri administraatorina ootavad kasutajad, et te hoolitseksite serveri eest. BTCPay Serveri hoolduse vahekaardil saab administraator teha mõningaid olulisi hooldustöid. Määrake BTCPay Serveri instantsi domeeninimi, taaskäivitage või puhastage Server. Võimalik, et kõige tähtsam, käivitada uuendusi.


BTCPay Server on avatud lähtekoodiga projekt ja seda uuendatakse sageli. Igast uuest versioonist antakse teada kas teie BTCPay Serveri teated või BTCPay Serveri ametlikes kanalites, mille kaudu BTCPay Server suhtleb.


![image](assets/en/086.webp)


#### Domeeninimi


Pärast BTCPay Serveri seadistamist võib administraator soovida oma algsest domeenist loobuda. Hoolduse vahekaardil saab administraator domeeni muuta. Pärast kinnituse klõpsamist ja domeeni õigete DNS-kirjete seadistamist uuendab ja taaskäivitab BTCPay Server uue domeeni juurde naasmiseks.


![image](assets/en/087.webp)


#### Restart


Käivitage BTCPay Server ja sellega seotud teenused uuesti.


![image](assets/en/088.webp)


#### Puhas


BTCPay Server töötab koos Docker-komponentidega; uuendustega võivad jääda Docker-kujutiste jäägid, ajutised failid jne. Serveri administraatorid saavad ruumi vabastada, käivitades skripti Clean.


![image](assets/en/089.webp)


#### Ajakohastamine


See on kõige olulisem valik vahekaardil Hooldus. BTCPay Server on loodud kogukonna poolt ja seetõttu on selle uuendustsüklid sagedasemad kui enamiku tarkvaratoodete puhul. Kui BTCPay Serverile ilmub uus versioon, saavad administraatorid sellest teate oma teavituskeskuses. Vajutades nupule update, kontrollib BTCPay Server GitHubi uusimat väljaannet, uuendab serverit ja taaskäivitab selle. Enne uuendamist soovitatakse serveri administraatoritel alati lugeda BTCPay Serveri ametlike kanalite kaudu levitatavaid väljaande märkusi.


![image](assets/en/090.webp)


### Logid


Probleemiga silmitsi seismine ei ole kunagi lõbus. Selles dokumendis kirjeldatakse kõige tavalisemat töökorraldust ja samme, kuidas probleemi tõhusalt tuvastada ja lahendada, kas iseseisvalt või kogukonna abiga.


Probleemi kindlakstegemine on ülioluline.


#### Probleemi kordamine


Kõigepealt püüdke kindlaks teha, millal probleem tekib. Proovige probleemi korrata. Proovige uuendada ja taaskäivitada oma Server, et kontrollida, kas saate probleemi reprodutseerida. Kui see kirjeldab teie probleemi paremini, tehke ekraanipilt.


##### Serveri uuendamine


Kontrollige oma BTCPay Serveri versiooni, kui see on palju vanem kui BTCPay Serveri [uusim versioon](https://github.com/btcpayserver/btcpayserver/releases). Serveri uuendamine võib probleemi lahendada.


##### Serveri taaskäivitamine


Serveri taaskäivitamine on lihtne viis paljude kõige tavalisemate BTCPay serveri probleemide lahendamiseks. Võimalik, et teil on vaja SSH-ühendust oma serverisse, et saaksite selle taaskäivitada.


##### Teenuse taaskäivitamine


Teil võib olla vaja taaskäivitada ainult teatud teenust teie BTCPay Serveri juurutamisel, näiteks letsencrypt-konteineri taaskäivitamine SSL-sertifikaadi uuendamiseks.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Kasutage docker ps, et leida teise teenuse nimi, mida soovite taaskäivitada.


#### Logide läbivaatamine


Logid võivad anda olulist teavet. Järgnevalt kirjeldame, kuidas saada BTCPay erinevate osade kohta logiteavet.


##### BTCPay logid


Alates versioonist v1.0.3.8 saad hõlpsasti juurdepääsu BTCPay serveri logidele otsepaketi kaudu. Kui olete serveri administraator, minge serverisseaded > Logid ja avage logifail. Kui te ei tea, mida konkreetne viga logides tähendab, mainige seda veaotsingu ajal.


Kui soovite üksikasjalikumaid logisid ja kasutate Dockeri kasutuselevõttu, saate vaadata konkreetsete Dockeri konteinerite logisid käsurea abil. Vaadake neid [ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) juhiseid VPS-i peal töötava BTCPay instantsi sisenemiseks.


Järgmisel leheküljel on BTCPay Serveri jaoks kasutatavate konteinerite nimede üldine loetelu.


Käivitage alljärgnevad käsud, et printida logid konteineri nime järgi. Asendage konteineri nimi, et vaadata teisi konteineri logisid.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```



| Logid         | Konteineri nimi                    |
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


Dockeri kasutamisel on mitu võimalust pääseda ligi oma LND logidele. Esiteks logige sisse root'ina:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Teise võimalusena saate kiirelt printida logisid, kasutades konteineri ID-d (vaja on ainult esimesi unikaalseid ID-märke, näiteks kaks kõige vasakpoolsemat märki):


```bash
docker logs 'add your container ID'
```


Kui teil on mingil põhjusel vaja rohkem palke


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Sa näed midagi sellist


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Nende logide pakkimata logidele juurdepääsuks tehke `cat LND.log` või kui soovite teist, siis kasutage `cat LND.log.15`.


Selleks, et pääseda ligi tihendatud logidele `.gzip`, kasutage `gzip -d LND.log.16.gz` (antud juhul pääseme ligi `LND.log.16.gz`). See peaks andma teile uue faili, kus saate teha `cat LND.log.16`. Juhul, kui ülaltoodu ei toimi, võib olla vaja esmalt paigaldada gzip, kasutades `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Teise võimalusena kasutage seda:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Te saate logiteavet ka käsuga c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin sõlme logid


Lisaks oma bitcoind konteineri [logide vaatamisele](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) saate kasutada ka mõnda [bitcoin-cli käsku](https://developer.Bitcoin.org/reference/RPC/index.html)


[(avaneb uus aken)](https://developer.Bitcoin.org/reference/RPC/index.html), et saada teavet oma Bitcoin sõlme kohta. BTCPay sisaldab skripti, mis võimaldab teil oma Bitcoin sõlmpunktiga hõlpsasti suhelda.


Btcpayserver-docker kausta sees, saada Blockchain teave oma sõlme abil:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Failid


BTCPay Serveril on kohalik failisüsteem, mis võimaldab laadida kaupluse (toote) varasid, logosid ja kaubamärke otse serverisse. Serveri failisüsteemile pääsevad ligi ainult serveri administraatorid; poeomanikud saavad oma logod või brändingu üles laadida poe tasandil.


Kui serveri administraator on vahekaardil Faili salvestusruum, on võimalik otse oma serverisse üles laadida või muuta faili salvestusruumi teenusepakkuja kohalikuks failisüsteemiks või Azure Blob Storage'iks.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- Poe ja serveri seadete erinevus, eelkõige seoses kasutajate, rollide ja e-kirjadega
- Määrake kogu serverit hõlmavad eeskirjad Lightning või Bitcoin Hot Wallet kasutamiseks ja loomiseks, uute kasutajate registreerimiseks ja e-posti teavitamiseks.
- Kuidas lisada kohandatud teemasid (lihtsate heledate/tumedate valikute asemel) ning luua kohandatud logosid
- Lihtsate serveri hooldustööde teostamine ettenähtud graafilise kasutajaliidese kaudu
- Probleemide lahendamine, sealhulgas mis tahes Dockeri konteinerite või teie sõlme üksikasjade otsimine
- Failide salvestamise haldamine


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Milline on erinevus serveri ja poe seadete kaudu määratud rollide vahel ja mis kirjeldab ühe võimalikku kasutust teise asemel?


#### KA praktiline ülevaade


Kirjeldage mõningaid võimalikke kasutusjuhtumeid, mis on lubatud vahekaardil Poliitikad.


#### KA praktiline ülevaade


Kirjeldage mõningaid tegevusi, mida administraator võib tavapäraselt teha vahekaardil Hooldus.


## BTCPay Server - Maksed


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice on dokument, mille müüja väljastab ostjale makse kogumiseks.


BTCPay Serveris tähistab Invoice dokumenti, mis tuleb tasuda kindlaksmääratud aja jooksul kindla Exchange määraga. Arvetel on aegumiskuupäevad, sest need lukustavad Exchange kursi kindlaksmääratud ajavahemiku jooksul, kaitstes vastuvõtjat hinnakõikumiste eest.


BTCPay Serveri tuum on võime tegutseda Bitcoin Invoice juhtimissüsteemina. Invoice on oluline vahend saadud maksete jälgimiseks ja haldamiseks.


Kui te ei kasuta maksete käsitsi vastuvõtmiseks sisseehitatud [Wallet](https://docs.btcpayserver.org/Wallet/), kuvatakse kõik poe sisesed maksed arvete lehel. See leht sorteerib maksed kumulatiivselt kuupäeva järgi ja on keskne ressurss Invoice haldamiseks ja maksete tõrkeotsinguks.


![image](assets/en/093.webp)


### Üldine


#### Invoice olekud


Alljärgnevas tabelis on loetletud ja kirjeldatud Invoice standardseisundid BTCPays koos soovitatud üldiste tegevustega. Tegevused on vaid soovitused. Kasutajad peavad ise määrama oma kasutusjuhtumi ja ettevõtte jaoks parima tegutsemisviisi.



| Arve olek | Kirjeldus | Tegevus |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New | Tasumata, arve taimer pole veel aegunud | Puudub |
| New (paidPartial) | Tasutud osaliselt, arve taimer pole veel aegunud | Puudub |
| Expired | Tasumata, arve taimer on aegunud | Puudub |
| Expired (paidPartial) ** | Tasutud osaliselt ja aegunud | Võtke ostjaga ühendust tagasimakseks või paluge tasuda võlgnevus. Valikuliselt märkige arve settled või invalid |
| Expired (paidLate) | Tasutud täies mahus pärast arve taimeri aegumist | Võtke ostjaga ühendust tagasimakseks või töötlege tellimus, kui hilised kinnitused on aktsepteeritavad. |
| Settled (paidOver) | Tasutud arvel olevast summast rohkem, laekunud piisav arv kinnitusi | Võtke ostjaga ühendust enamtasutud summa tagastamiseks või oodake, kuni ostja teiega ühendust võtab |
| Processing | Tasutud täies mahus, kuid pole laekunud piisavalt kinnitusi (vastavalt poe seadetele) | Võtke ostjaga ühendust enamtasutud summa tagastamiseks või oodake, kuni ostja teiega ühendust võtab |
| Processing (paidOver) | Tasutud arvel olevast summast rohkem, pole laekunud piisavalt kinnitusi | Oodake olekut settled, seejärel võtke ostjaga ühendust tagasimakseks või oodake ostja kontakti |
| Settled | Tasutud täies mahus, poes on laekunud piisav arv kinnitusi | Täitke tellimus |
| Settled (marked) | Olek muudeti käsitsi processing või invalid olekust settled olekusse | Poe administraator märkis makse olekuks settled |
| Invalid* | Tasutud, kuid määratud aja jooksul ei laekunud piisavalt kinnitusi | Kontrollige tehingut plokiahela sirvijas; kui kinnitusi on piisavalt, märkige settled |
| Invalid (marked) | Olek muudeti käsitsi settled või expired olekust invalid olekusse | Poe administraator märkis makse olekuks invalid |
| Invalid (paidOver) | Tasutud arvest rohkem, kuid määratud aja jooksul ei laekunud piisavalt kinnitusi | Kontrollige tehingut plokiahela sirvijas; kui kinnitusi on piisavalt, märkige settled |

#### Invoice üksikasjad


Leht Invoice üksikasjad sisaldab kogu Invoicega seotud teavet.


Invoice teave luuakse automaatselt Invoice staatuse, Exchange määra jne alusel. Tooteinfo luuakse automaatselt, kui Invoice on loodud koos tooteinfoga, näiteks müügipunkti rakenduses.


#### Invoice filtreerimine


Arveid saab filtreerida otsingunupu kõrval asuvate kiirfiltrite või täiustatud filtrite abil, mida saab muuta, klõpsates üleval asuvat linki (Abi). Kasutajad saavad arveid filtreerida kaupluse, tellimuse ID, artikli ID, staatuse või kuupäeva järgi.


#### Invoice eksport


BTCPay serveri arveid saab eksportida CSV- või JSON-formaadis. Lisateave Invoice ekspordi ja raamatupidamise kohta.


#### Invoice tagasimaksmine


Kui soovite mingil põhjusel tagastust väljastada, saate hõlpsasti luua tagastuse vaates Invoice.


#### Arvete arhiveerimine


BTCPay Serveri Address korduvkasutamise puudumise tõttu on tavaline, et teie poe Invoice lehel on palju aegunud arveid. Nende varjamiseks valige need nimekirjast välja ja märgistage need arhiveerituks. Arhiveerituks märgitud arveid ei kustutata. Arhiveeritud Invoice-le tehtud makse tuvastab teie BTCPay server endiselt (staatus paidLate). Saate poe arhiveeritud arveid igal ajal vaadata, valides otsingufiltri rippmenüüst arhiveeritud arved.


#### Vaikimisi valuuta


Poe vaikimisi valuuta, mis määrati poe loomise viisardis.


#### Võimaldab igaühel luua Invoice


Te peaksite selle valiku lubama, kui soovite, et teie poes saaks arved luua ka väljastpoolt. See valik on kasulik ainult siis, kui kasutate maksmise nuppu või kui väljastate arveid API või kolmanda osapoole HTML-veebisaidi kaudu. PoS-rakendus on eellubatud ja ei nõua selle seadistuse lubamist, et suvaline külastaja saaks avada teie POS-poe ja luua Invoice.


#### Lisamaksu (võrgutasu) lisamine Invoice-le



- Ainult juhul, kui klient teeb Invoice eest rohkem kui ühe makse
- Iga makse puhul
- Ärge kunagi lisage võrgutasu


#### Invoice aegub, kui kogu summa ei ole makstud pärast ... protokolli.


Invoice taimeri on vaikimisi seatud 15 minutile. Taimer toimib kaitsemehhanismina volatiilsuse vastu, kuna see lukustab krüptoraha summa krüpto ja fatiidi kursi alusel. Kui klient ei maksa Invoice kindlaksmääratud aja jooksul, loetakse Invoice aegunuks. Invoice loetakse "makstud" kohe, kui tehing on Blockchain-l nähtav (null kinnitust), ja loetakse "lõpetatuks", kui see jõuab kaupmehe poolt määratud kinnituste arvuni (tavaliselt 1-6). Taimer on kohandatav.


#### Arvestage Invoice makstud summaga isegi siis, kui makstud summa on ..% väiksem kui oodatud.


Olukorras, kus klient kasutab Exchange Wallet otse Invoice eest tasumiseks, võtab Exchange väikese tasu. See tähendab, et sellist Invoice ei loeta täielikult lõpetatuks. Invoice märgitakse kui "osaliselt tasutud" Kui kaupmees soovib aktsepteerida alakasutatud arveid, saate siin määrata protsendimäära


### Taotlused


Maksetaotlused on funktsioon, mis võimaldab BTCPay poeomanikel luua pikaajalisi arveid. Raha makstakse vastavalt maksetaotlusele, kasutades maksmise ajal kehtivat Exchange kurssi. See võimaldab kasutajatel sooritada makseid endale sobival ajal, ilma et nad peaksid maksmise ajal kaupluse omanikuga Exchange kurssi läbi rääkima või kontrollima.


Kasutajad saavad taotluste eest tasuda osamaksetena. Maksetaotlus jääb kehtima kuni selle täieliku tasumiseni või kui poe omanik nõuab aegumistähtaega. Aadresse ei kasutata kunagi uuesti. Iga kord, kui kasutaja klõpsab maksetaotluse jaoks Invoice loomiseks Address, luuakse uus Address.


Kaupluse omanikud saavad printida maksetaotlusi (või eksportida Invoice andmeid) arvestuse pidamiseks ja raamatupidamiseks. BTCPay märgistab arved automaatselt maksetaotlusteks teie poe Invoice nimekirjas.


#### Kohandage oma maksetaotlusi



- Invoice Summa - Määrake taotletav maksesumma
- Denomination - Näita taotletud summat fiat- või krüptoraha kujul
- Makse kogus - lubab ainult ühekordseid makseid või osalisi makseid
- Kehtivusaeg - lubab makseid kuni teatud kuupäevani või ilma kehtivusaja lõppemiseta
- Kirjeldus - Tekstiredaktor, andmetabelid, fotode ja videote sisseehitamine
- Välimus - värv ja stiil CSS-teemadega


![image](assets/en/094.webp)


#### Loo maksetaotlus


Mine vasakpoolses menüüs jaotisele Maksetaotlus ja klõpsa "Loo maksetaotlus".


![image](assets/en/095.webp)


Sisestage taotluse nimi, summa, nimiväärtus, seotud kauplus, kehtivusaeg ja kirjeldus (valikuline)


Valige valik Luba makse saajal koostada arveid oma nimiväärtuses, kui soovite lubada osamakseid.


Klõpsake maksetaotluse läbivaatamiseks nuppu Save & View (Salvesta ja vaata).


BTCPay loob maksetaotluse URL-i. Jagage seda URL-i oma maksetaotluse vaatamiseks. Kas vajate mitu sama taotlust? Te saate maksetaotlusi dubleerida, kasutades peamenüüst kloonimise valikut.


![image](assets/en/096.webp)


**HOIATUS**


Maksetaotlused on kauplusest sõltuvad, mis tähendab, et iga maksetaotlus on loomise ajal seotud kauplusega. Veenduge, et Wallet on ühendatud teie kauplusega, millele maksetaotlus kuulub.


#### Tasuline taotlus


Pärast makse saatmist saavad makse saaja ja maksetaotleja vaadata maksetaotluse staatust. Kui makse on täies ulatuses laekunud, siis kuvatakse staatusena "Arveldatud". Kui on tehtud ainult osaline makse, siis näitab Amount Due (tasumisele kuuluv summa) järelejäänud summat.


![image](assets/en/097.webp)


#### Kohandage maksetaotlusi


Kirjelduse sisu saab muuta maksetaotluse tekstiredaktoriga. Mõlemad valikud on saadaval, kui soovite kasutada täiendavaid värvitemaatikaid või kohandatud CSS-stiilimist.


Mittetehnilised kasutajad saavad kasutada [bootstrap-teemat](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Täiendavat kohandamist saab teha täiendava CSS-koodiga, nagu allpool näidatud.


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


### Tõmmata makseid


Traditsiooniliselt jagab vastuvõtja Bitcoin Address, et teha Bitcoin makse, ja saatja saadab hiljem raha sellele Address-le. Sellist süsteemi nimetatakse Push-makseks, sest saatja algatab makse, kui vastuvõtja ei pruugi olla kättesaadav, lükates makse vastuvõtjale.


Aga kuidas oleks, kui rolli ümber pöörata?


Mis siis, kui selle asemel, et saatja lükkab makse, lubab saatja vastuvõtjal tõmmata makse ajal, mil vastuvõtja seda vajalikuks peab? See ongi Pull-makse kontseptsioon. See võimaldab mitmeid uusi rakendusi, näiteks:



- Tellimusteenus (kus tellija lubab teenusel iga x aja tagant raha tõmmata)
- Tagasimaksed (kus kaupmees lubab kliendil tõmmata tagasimakstud raha oma Wallet-le, kui ta seda vajalikuks peab)
- Ajapõhine arveldamine vabakutseliste jaoks (kus töövõtja lubab vabakutselisel tõmmata raha oma Wallet-sse, kui aeg saab aru)
- Patronaaž (kus patroon lubab abivajajal igal kuul raha tõmmata, et jätkata oma töö toetamist)
- Automaatne müük (kus Exchange klient lubab Exchange-l automaatselt iga kuu Wallet-lt raha välja võtta, et seda müüa)
- Saldo väljavõtmise süsteem (kus suure mahuga teenus võimaldab kasutajatel taotleda väljamakseid oma saldost, teenus saab seejärel hõlpsasti koondada kõik väljamaksed paljudele kasutajatele kindlaksmääratud ajavahemike järel)


### Väljamaksed


Väljamaksefunktsioon on seotud funktsiooniga [Pull Payments](https://docs.btcpayserver.org/PullPayments/). See funktsioon võimaldab teil luua väljamakseid oma BTCPay raames. See funktsioon võimaldab teil töödelda pull-makseid (tagasimaksed, palga väljamaksed või väljamaksed).


#### Näide 1: Tagasimakse


Alustame tagasimaksmise näitest. Klient on ostnud teie poest toote, kuid kahjuks peab ta selle tagastama. Ta soovib raha tagasi saada. BTCPays saate luua [Tagasimakse](https://docs.btcpayserver.org/Refund/) ja anda kliendile lingi, et ta saaks oma raha tagasi nõuda. Kui klient on esitanud oma Address ja nõudnud raha, kuvatakse see väljamaksete jaotises.


Esimene staatus on "Ootab heakskiitu". Kaupluse müüjad saavad kontrollida, kas mitu ootab, ja pärast valiku tegemist kasutate nuppu Tegevused.


Tegevusnupu valikud



- Heakskiita valitud väljamaksed
- Kinnitada ja saata valitud väljamakseid
- Tühista valitud väljamaksed


Järgmine samm on valitud väljamaksete kinnitamine ja saatmine, sest me tahame kliendile raha tagasi maksta. Kontrollige kliendi Address, kus on märgitud summa ja see, kas soovime, et tasud lahutatakse tagasimaksest või mitte. Pärast kontrollide täitmist on tehingu allkirjastamine ainus järelejäänud samm.


Klient saab nüüd nõude esitamise lehel ajakohastatud. Ta saab jälgida tehingut, sest talle antakse link Block explorer ja tema tehingu kohta. Kui tehing on kinnitatud, muutub selle staatus "Lõpetatud".


#### Näide 2: Palk


Nüüd vaatleme palga väljamaksmist, sest seda juhitakse poe seest, mitte kliendi soovil. Alusidee on sama; see kasutab pull-makseid. Kuid selle asemel, et luua tagasimakse, teeme [Pull Payment](https://docs.btcpayserver.org/PullPayments/).


Mine oma BTCPay serveris vahekaardile Pull Payments. Klõpsake üleval paremal pool nupul Create Pull Payment.


Nüüd oleme väljamakse loomisel, anna sellele nimi ja soovitud summa valitud valuutas. Täitke kirjeldus, et töötaja teaks, millega on tegemist. Järgmine osa on sarnane tagasimaksetele. Töötaja täidab sihtkoha Address ja summa, mida ta soovib sellest väljamaksest taotleda. Ta võib otsustada teha 2 eraldi nõuet, erinevatele aadressidele või isegi osaliselt nõuda üle välkkiirte.


Kui ootab mitu väljamakseid, saate need allkirjastada ja välja saata partiidena. Pärast allkirjastamist viiakse väljamaksed vahekaardile Jooksev ja kuvatakse Tehing. Kui võrk on selle heaks kiitnud, liigub väljamakse vahekaardile Lõpetatud. Väljastatud vahekaart on puhtalt ajaloolistel eesmärkidel. See sisaldab töödeldud väljamakseid ja sinna kuuluvaid tehinguid


### Tõmmata makseid


#### Kontseptsioon


Kui saatja konfigureerib Pull-makse, saab ta konfigureerida mitmeid omadusi:



- Tõmbetaotlus Nimi
- Piirsumma
- Ühik (näiteks BTC, SAT, USD)
- Makseviisid
  - BTC On-Chain
  - BTC off-chain
- Kirjeldus
- Kohandatud CSS
- Lõppkuupäev (Lightning Network BOLT11 puhul vabatahtlik)


Pärast seda saab saatja jagada pull-makset lingi abil vastuvõtjaga, mis võimaldab vastuvõtjal luua väljamakse. Vastuvõtja valib oma väljamakse:



- Millist makseviisi kasutada
- Kuhu raha saata


Kui väljamakse on loodud, arvestatakse see jooksva perioodi pull-makse limiidi hulka. Seejärel kiidab saatja väljamakse heaks, määrates määra, millega väljamakse saadetakse, ja jätkab maksmist.


Pakume saatjale lihtsat meetodit mitme väljamakse kogumiseks [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server pakub täielikku API-d nii saatjale kui ka vastuvõtjale, mis on dokumenteeritud teie instantsi leheküljel `/docs`. (või dokumentatsiooni veebilehel https://docs.btcpayserver.org)


Kuna meie API pakub kõiki pull-maksete võimalusi, saab saatja automatiseerida makseid vastavalt oma vajadustele.


### Oskuste kokkuvõte


Selles osas õppisid sa järgmist:



- BTCPay Serveri Invoice olekute ja nendega tehtavate toimingute põhjalik tundmine
- Kohandada ja hallata Invoice pikendatud elueaga mehhanisme, mida tuntakse kui taotlusi.
- BTCPay Serveri ainulaadse Pull Payment funktsiooniga avanevad täiendavad paindlikud maksevõimalused, eriti tagasimaksete ja palgamaksete käsitlemisel.


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Millised on mõned erinevused arvete ja maksetaotluste vahel ning mis võib olla hea põhjus viimaste kasutamiseks?


#### KA kontseptuaalne ülevaade


Kuidas laiendavad tõmbemaksed seda, mida tavaliselt saab teha On-Chain? Kirjeldage mõningaid kasutusjuhtumeid, mida nad võimaldavad.


## BTCPay serveri vaikimisi pluginad


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Vaikimisi pistikprogrammid ja rakendused


BTCPay serveriga on kaasas standardne hulk lisaseadmeid (rakendusi), mis võivad muuta BTCPay serveri e-kaubanduse makseväravaks. Müügipunkti, ühisrahastusplatvormi ja lihtsa maksmise nupu lisamisega muutub BTCPay Server kergesti kasutatavaks lahenduseks.


### Müügipunkt


Üks BTCPay Serveri standardsetest pluginatest on müügipunkt (Point of Sale - PoS). PoS-pluginiga saab poeomanik luua veebipoe otse BTCPay Serverist; poeomanik ei vaja veebipoe käitamiseks kolmanda osapoole e-kaubanduse lahendusi. Veebipõhine PoS-rakendus võimaldab kasutajatel, kellel on telliskivipoed, hõlpsasti ja ilma tasudeta või kolmanda osapoole abita vastu võtta Bitcoin otse oma Wallet-sse. PoS-i saab hõlpsasti kuvada tahvelarvutites või muudes seadmetes, mis toetavad veebi sirvimist. Kasutajad saavad hõlpsasti luua koduekraani otsetee, et veebirakendusele kiiresti juurde pääseda.


#### Kuidas luua uus müügipunkt


BTCPay Server võimaldab poeomanikel kiiresti luua müügipunkti mitmes kujunduses. BTCPay Server tunnistab, et mitte iga pood ei ole e-kaubandus ja mitte iga pood ei ole baar või restoran, ning see on varustatud mitme standardse seadistusega PoSi jaoks.


Kui poeomanik klõpsab vasakul menüüribal nupule "Müügipunkt", küsib BTCPay Server nüüd nime; see nimi on nähtav vasakul menüüribal. PoSi loomiseks klõpsake nuppu Create.


![image](assets/en/098.webp)


#### Värskelt loodud müügipunkti ajakohastamine


Pärast uue müügipunkti loomist saate järgmisel ekraanil uuendada oma müügipunkti ja lisada kaupluse kaupu.


##### Rakenduse nimi


Teie müügipunktile antud nimi on nähtav BTCPay serveri peamenüüs.


##### Näita pealkiri


Avalikkus näeb külastades teie poe pealkirja või nime. BTCPay Server nimetab teie poe vaikimisi "Teepood" Asendage see oma poe nimega.


![image](assets/en/099.webp)


#### Vali müügipunkti stiil


BTCPay Server on võimeline kuvama oma müügikohta mitmel viisil.



- Toote nimekiri
  - Poe vaade, kus kliendid saavad korraga osta ainult 1 toodet.
- Toote nimekiri koos ostukorviga.
  - Poe vaade, kus kliendid saavad osta korraga mitu toodet ja saada ostukorvi ülevaate ekraani paremale poole.
- Ainult klaviatuur
  - Ei mingit tootenimekirja, vaid ainult klaviatuur otsearveldamiseks.
- Print display (trükitav tootenimekiri koos QR-ga)
  - Kui te ei saa oma tootenimekirja alati digitaalselt kuvada, vajate toodete jaoks "offline-lahendust"; BTCPay Serveril on printimisnäidik, mis toimib offline-poena.


![image](assets/en/100.webp)


#### Point Of Sale Style - Toote nimekiri


![image](assets/en/101.webp)


#### Müügipunkti stiil - Toote nimekiri + ostukorv


![image](assets/en/102.webp)


#### Müügipunkti stiil - ainult klaviatuur


![image](assets/en/103.webp)


#### Müügipunkti stiil - Prindi väljapanek


![image](assets/en/104.webp)


#### Valuuta


Poe omanik võib määrata oma müügipunkti jaoks erineva valuuta kui tema üldine vaikimisi seatud valuuta. Poe vaikevaluuta täidab selle välja automaatselt.


#### Kirjeldus


Rääkige oma poest; mida ja kui palju te müüte? Kõik, mis selgitab teie poodi, läheb siia.


![image](assets/en/105.webp)


#### Tooted


Kui müügipunkt luuakse, lisab standardne BTCPay Server kauplusesse paar toodet, millele saab viidata. Vajutage nupule Edit (Muuda) mis tahes standardse eseme juures, et paremini mõista iga võimalikku valikut eseme jaoks.


Uue toote loomine poes koosneb järgmistest väljadest;



- Pealkiri
- Hind (fikseeritud, minimaalne või kohandatud)
- Pildi URL
- Kirjeldus
- Inventuur
- ID
- Osta nupu tekst.
- Lubamine/väljalülitamine


Kui poe omanik on täitnud kõik uued tooteväljad, klõpsake nuppu salvesta ja märkate, et müügipunkti jaotis Tooted on nüüd täidetud. Salvestage alati ekraani paremas ülanurgas, et vältida võimalust, et poeomanikud võivad toodete lisamisel oma edusammud kaotada.


Poeomanikud võivad oma toodete konfigureerimiseks kasutada ka "Raw Editorit". Toores redaktor nõuab põhiteadmisi JSON-struktuuridest.


![image](assets/en/106.webp)


#### Kassa


BTCPay Server võimaldab väikest PoS-spetsiifilist kassade kohandamist. Poeomanik saab määrata "Osta x eest" teksti või küsida konkreetseid kliendiandmeid, lisades need vormidele.


#### Näpunäited


Ainult mõned kauplused vajavad võimalust Tips oma müügi kohta. Poeomanikud võivad selle sisse või välja lülitada, nagu nad oma poe jaoks vajalikuks peavad. Kui kauplus kasutab sisse lülitatud näpunäiteid, saab kaupluse omanik määrata väljal soovitud näpunäidete teksti. BTCPay Serveri jootraha töötab protsendi alusel. Poeomanikud saavad lisada mitu protsenti, mis on eraldatud komadega.


#### Allahindlused


Poe omanikuna võid soovida anda kliendile kassas kohandatud allahindlust; allahindluste lüliti muutub kättesaadavaks sinu poe kassas. Seda soovitatakse aga tungivalt mitte kasutada isekassasüsteemide puhul.


#### Kohandatud maksed


Kui valik Custom Payments on sisse lülitatud, saab klient sisestada määratud hinna, mis on võrdne või suurem kui poe poolt genereeritud algne Invoice.


#### Lisavõimalused


Pärast seda, kui olete kõik oma müügipunkti jaoks seadistanud, on jäänud mõned lisavõimalused. Poeomanikud saavad oma PoSi hõlpsasti integreerida Iframe'i kaudu või integreerida maksenupu, mis viitab konkreetsele poeartiklile. Äsja loodud PoS-poe stiliseerimiseks võivad omanikud lisada lisavõimaluste allosas kohandatud CSS-i.


#### Kustuta see rakendus


Kui poeomanik soovib müügikoha täielikult kustutada oma BTCPay serverist, siis poeomanikud saavad poe uuendamise lõpus klõpsata nupule Kustuta see rakendus, et oma müügikoha rakendus täielikult hävitada. Kui klõpsate nupule "Kustuta see rakendus", küsib BTCPay Server kinnitust, sisestades `DELETE` ja kinnitades selle nupule Delete. Pärast kustutamist naaseb poe omanik BTCPay Serveri armatuurlauale.


### BTCPay Server - ühisrahastamine


Lisaks müügipunkti pluginale on BTCPay Serveril võimalus luua ühisrahastust. Nii nagu iga teine Crowdfund-platvorm, saavad poeomanikud seada eesmärgi, luua soodustusi sissemaksete eest ja kohandada seda oma vajaduste järgi.


#### Kuidas luua uus ühisrahastu


Klõpsake BTCPay serveri vasakpoolses peamenüüs, pluginate jaotise Plugin all, Crowdfund pluginale. BTCPay Server küsib nüüd Crowdfundile nime; see nimi kuvatakse ka vasakul menüüribal.


![image](assets/en/107.webp)


#### Värskelt loodud müügipunkti ajakohastamine


Kui rakendusele on antud nimi, tuleb järgmisel ekraanil uuendada rakendust, et sellel oleks kontekst.


#### Rakenduse nimi


Teie ühisrahastusele antud nimi on nähtav BTCPay Serveri peamenüüs.


#### Näita pealkiri


Pealkiri on antud ühisrahastusele avalikkuse jaoks.


#### Tagline


Andke ühisrahastusele üks liitsõna, et tunnustada, millega rahakogumisüritus tegeleb.


![image](assets/en/108.webp)


#### Esile tõstetud pildi URL


Igal ühisrahastusel on oma põhipilt, üks bänner, mille te kohe ära tunnete. Seda pilti saab salvestada teie serverisse, kui teil on haldusõigused. Administraatorid saavad pilti üles laadida BTCPay serveri seadete all - Failid. Kui olete poe omanik, tuleb pilt laadida üles veebi kolmanda osapoole veebihalduri (näiteks Imgur) kaudu.


#### Teha ühisrahastuse avalikuks


See lüliti muudab teie ühisrahastuse avalikuks ja seega välismaailmale nähtavaks. Testimise eesmärgil või selleks, et näha, kas teie teema on õigesti rakendatud, jätke see ühisrahastuse loomise ajaks väljalülitatud (OFF).


#### Kirjeldus


Rääkige maailmale oma ühisrahastusest. Milleks te kogute? Kõik, mis selgitab teie ühisrahastust, läheb siia.


![image](assets/en/109.webp)


#### Ühisrahastuse eesmärk


Seadke eesmärk, mida annetuskampaania peaks projekti jaoks teenima ja millises vääringus see eesmärk peaks olema väljendatud. Veenduge, et kui teie eesmärgid on seatud kuupäevade vahel, lisage need siht- ja lõppkuupäevad ühisrahastuse eesmärkide alla.


![image](assets/en/110.webp)


#### Eelised


Soodustused võivad teie ühisrahastamist oluliselt tõhustada. Seda seetõttu, et lisatasud annavad inimestele võimaluse teie kampaanias osaleda. Nad kasutavad nii isekat kui ka heatahtlikku motivatsiooni. Ja nad võimaldavad teil juurdepääsu oma toetajate kulutustele, mitte ainult nende heategevuslikule rahakotile -- võite arvata, kumb on olulisem.


Uue eelisfunktsiooni loomine koosneb järgmistest väljadest.



- Pealkiri
- Hind (fikseeritud, minimaalne või kohandatud)
- Pildi URL
- Kirjeldus
- Inventuur
- ID
- Osta nupu tekst.
- Lubamine/väljalülitamine


Kui poeomanik on täitnud kõik uue soodustuse väljad, klõpsake nupule Salvesta ja te märkate, et Crowdfunds'i soodustuste sektsioon on nüüd täidetud.


![image](assets/en/111.webp)


### BTCPay Server - müügipunkt


#### Panused


Poeomanikud saavad valida, kuidas soodustusi kuvada, kuidas neid sorteerida või neid isegi teiste soodustuste vastu seada. Kui aga Crowdfunds'i eesmärgid on saavutatud, võivad poeomanikud soovida lõpetada selle rahakogumise suunas tehtavate annetuste voogamise. Seetõttu saab ta lülitada sisse "Ära luba täiendavaid annetusi pärast eesmärgi saavutamist". See takistab Crowdfund'ile annetuste vastuvõtmist.


##### Ühisrahastuse käitumine


Crowdfundi standard arvestab eesmärgi hulka ainult Crowdfundiga loodud arveid. Siiski võib esineda juhtumeid, kus poe omanik soovib, et kõik selles poes tehtud arved läheksid arvesse Crowdfundi puhul.


#### Lisavõimalused kohandamiseks


BTCpay Server pakub paar täiendavat kohandamist. Lisage helisid, animatsioone või isegi aruteluteemasid ühisrahastusele. Poeomanikud võivad muuta ka Crowdfundi välimust ja tunnetust, sisestades oma kohandatud CSS-i.


#### Kustuta see rakendus


Kui poeomanik soovib oma BTCPay serverist ühisrahastuse täielikult kustutada, saab ta ühisrahastuse uuendamise lõpus klõpsata nupule "Kustuta see rakendus", et oma ühisrahastuse rakendus täielikult eemaldada. Kui klõpsate nupule "Kustuta see rakendus", küsib BTCPay Server kinnitust, kirjutades `DELETE` ja kinnitades seda nupule Delete vajutades. Pärast kustutamist naaseb poe omanik BTCPay Serveri armatuurlauale.


### BTCPay Server - Makse nupp


Lihtsalt sisseehitatav HTML ja väga hästi kohandatavad maksenupud võimaldavad poeomanikel võtta vastu näpunäiteid ja annetusi. BTCPay Serveri vasakul menüüribal, Plugins jaotise all, saavad poeomanikud klõpsata "Pay Button" ja klõpsata "Enable", et luua maksenupp.


#### Üldised seaded


Makse nupu üldiste seadete raames saavad poeomanikud määrata



- Standardhind
- Vaikimisi valuuta
- Vaikimisi makseviis
  - Kasutage poe vaikimisi
  - BTC On-Chain
  - BTC off-chain (välk)
  - BTC off-chain (LNURL-pay)
- Kassa kirjeldus
- Tellimuse ID


#### Kuvamisvõimalused


BTCPay Serveri makse nuppu saab konfigureerida erinevatele stiilidele sobivaks. Nupud võivad olla fikseeritud või kohandatud summaga, mida kuvatakse kas liuguri või pluss- ja miinusklahvidega.


#### Kasutage Modal


Maksenupu loomisel saavad poeomanikud valida selle käitumise, kui klient sellele klõpsab, ja näidata seda modaalina või uue lehega.


**!?Märkus!?**


Hoiatus: Maksmise nuppu tuleks kasutada ainult näpunäidete ja annetuste jaoks


Maksenupu kasutamine e-kaubanduse integratsioonide puhul ei ole soovitatav, kuna kasutaja saab muuta tellimusega seotud teavet. E-kaubanduse jaoks peaksite kasutama meie Greenfield API-d. Kui see pood töötleb äritehinguid, soovitame enne maksenupu kasutamist luua eraldi pood.


#### Kohandada Pay nupu tekst


Vaikimisi on BTCPay serveri maksenupu märgitud "Pay With BTCPay". Poeomanikud saavad selle teksti oma soovide järgi seadistada ja BTCPay Serveri logo enda omale sobivaks muuta. Määrake tekst, kasutades "Pay Button Text" ja kleepige pildi URL alla "Pay Button Image URL".


##### Pildi suurus


Nupu pildi suurust saab määrata ainult kolmele vaikimisi väärtusele.



- 146x40px
- 168x46px
- 209x57px


#### Nupu tüüp


BTCPay Server tunneb kolm maksenupu olekut.



- Fikseeritud summa
  - Eelmine määratud hind on nupu üldistes seadetes.
- Kohandatud summa
  - BTCPay Serveri maksmise nupul on + ja - lülitid kohandatud hinna määramiseks.
  - Kui kasutate kohandatud summat, küsib BTCPay Server Min, Max ja seda, kui järk-järgult see peaks suurenema.
  - Nupud võib seadistada "Kasuta lihtsat sisestusstiili ".See võtab ära +/- lülitid.
  - Paigalda nuppu reas, kus nupp ja lülitid ilmuvad reas.
- Liugur
  - Sarnaselt kohandatud summale on see siiski visuaalselt erinev, kuna sellel on +/- lülitite asemel liugur.
  - Liuguri kasutamisel küsib BTCPay Server Min, Max ja seda, kui järk-järgult see peaks suurenema.


**!?Märkus!?**


Makse nuppu saab hoiatuse kirjelduse ülaosas kustutada.


#### Makseteated


Server IPN (Instant Payment Notification) on mõeldud veebikonksude jaoks ja seda saab konfigureerida ostujärgsete andmete URL-iga.


#### E-posti teated


Kui makse on tehtud, saab BTCPay Server teavitada poe omanikku.


#### Brauseri ümbersuunamine


Kui klient ostu sooritab, suunatakse ta sellele lingile, kui poe omanik on selle seadnud.


#### Täiustatud makse nupu valikud


Määrake täiendavad päringustringi parameetrid, mis tuleks lisada kassaleheküljele, kui Invoice on loodud. Näiteks `lang=da-DK` laadib kassalehe vaikimisi taani keeles.


#### Rakenduse kasutamine lõpp-punktina


Võite siduda maksenupu otse mõne varem kasutatud PoS- või Crowdfund-rakenduse objektiga.


Poeomanikud saavad klõpsata rippmenüüs ja valida soovitud rakenduse; kui rakendus on valitud, saab poeomanik lisada toote, mis tuleb siduda.


#### Genereeritud kood


Kuna BTCPay Serveri maksenupp on hõlpsasti integreeritav HTML, näitab BTCPay Server pärast maksenupu seadistamist allosas genereeritud koodi, mida saab veebisaidile kopeerida.


Poeomanikud saavad genereeritud koodi oma veebisaidile kopeerida ja BTCPay serveri maksenupp on otse nende veebisaidil aktiivne.


#### Makseteated


Server IPN (Instant Payment Notification) on mõeldud veebikonksude jaoks ja seda saab konfigureerida ostuandmete postitamiseks URL-iga.


#### E-posti teated


Iga kord, kui makse tehakse, saab BTCPay Server teavitada poe omanikku.


#### Brauseri ümbersuunamine


Kui klient ostu sooritab, suunatakse ta sellele lingile, kui poe omanik on selle seadnud.


#### Täiustatud makse nupu valikud


Määrake täiendavad päringustringi parameetrid, mis tuleks lisada kassaleheküljele, kui Invoice on loodud. Näiteks `lang=da-DK` laadib kassalehe vaikimisi taani keeles.


#### Rakenduse kasutamine lõpp-punktina


Võite siduda maksenupu otse mõne varem kasutatud PoS- või Crowdfund-rakenduse objektiga. Poeomanikud saavad klõpsata rippmenüüs ja valida soovitud rakenduse. Kui rakendus on valitud, saab poeomanik lisada sidumist vajava eseme.


#### Genereeritud kood


Kuna BTCPay Serveri maksenupp on hõlpsasti integreeritav HTML, näitab BTCPay Server pärast maksenupu seadistamist allosas genereeritud koodi, mida saab veebisaidile kopeerida. Poeomanikud saavad genereeritud koodi oma veebisaidile kopeerida ja BTCPay Serveri maksenupp on nende veebisaidil otse aktiivne.


### Oskuste kokkuvõte


Selles osas õppisite:



- Kuidas kasutada BTCPay Serveri integreeritud PoS pluginat, et luua kohandatud pood lihtsalt
- Kuidas kasutada BTCPay Serveri integreeritud Crowdfund pluginat, et luua hõlpsasti kohandatud ühisrahastuse rakendus
- Makse nupu koodi genereerimine kohandatud maksunupu jaoks, kasutades Pay Button pluginat


### Teadmiste hindamine


#### KA läbivaatamine


Millised on kolm sisseehitatud pluginat, mis kuuluvad BTCPay Serveri standardvarustusse? Kirjeldage paari sõnaga, kuidas igaühte saab kasutada.


# BTCPay serveri konfigureerimine


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## BTCPay Serveri paigaldamise põhitõed LunaNode'i keskkonnas


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### BTCPay serveri paigaldamine hostitud keskkonda (LunaNode)


Need sammud annavad kogu vajaliku teabe, et alustada BTCPay Serveri kasutamist LunaNode'is. Tarkvara kasutuselevõtuks on palju võimalusi.

Kõik andmed BTCPay serveri kohta leiate aadressilt https://docs.btcpayserver.org.


#### Kust me alustame?


Selles osas tutvute LunaNode'iga kui hostinguteenuse pakkujaga, tutvute BTCPay serveri kasutamise esimeste sammudega ja saate teada, kuidas kasutada Lightning Network-ga. Kui oleme kõik sammud läbi käinud, saate käivitada Bitcoin-i vastuvõtva veebipoe või ühisrahastusplatvormi!


See on üks paljudest võimalustest BTCPay Serveri kasutuselevõtuks. Lisateavet leiate meie dokumentatsioonist.


https://docs.btcpayserver.org.


### BTCPay Server - LunaNode kasutuselevõtmine


#### LunaNode kasutuselevõtmine


Kõigepealt minge LunaNode.com veebilehele, kus loome uue konto. Klõpsake paremal üleval Sign Up või kasutage nende kodulehel olevat Get Started wizard'i.


![image](assets/en/112.webp)


Pärast uue konto loomist saadab LunaNode teile kinnitava e-kirja. Kui olete konto kinnitanud, võrreldes Voltage'iga, kuvatakse teile kohe võimalus oma kontojääkide täiendamiseks. See saldo on vajalik serveriruumi ja hostingukulude katmiseks.


![image](assets/en/113.webp)


#### Lisa krediiti oma LunaNode'i kontole


Kui olete klõpsanud nuppu "Krediidi hoiustamine", saate määrata, kui palju soovite oma kontot täiendada ja kuidas soovite selle eest maksta. LunaNode ja BTCPay Server maksavad 10 ja 20 dollarit kuus.

Võrreldes Voltage.cloudiga saate täieliku juurdepääsu oma virtuaalsele privaatserverile (VPS), mis võimaldab teil oma serveri üle suuremat kontrolli. Pärast uue konto loomist saadab LunaNode teile kinnitava e-kirja.

Kui olete kontot kinnitanud, võrreldes Voltage'iga, pakutakse teile kohe võimalust oma kontojääki täiendada. See saldo on vajalik serveriruumi ja hostingukulude katmiseks.


#### Kuidas võtta kasutusele uus server?


Selles juhendis tutvustame teile seadistamisprotsessi, luues API võtmete komplekti ja kasutades LunaNode'i poolt välja töötatud BTCPay Serveri käivitajat.


Klõpsake oma LunaNode'i armatuurlaual üleval paremal API-l. See avab uue lehekülje. Meil tuleb määrata ainult API võtme nimi. Ülejäänu eest hoolitseb LunaNode ja seda käesolevas juhendis ei käsitleta. Vajutage nupule Create API Credential.

Pärast API volituste loomist saate pika tähe- ja tähemärkide jada. See on teie API võti.


![image](assets/en/114.webp)


#### Kuidas võtta kasutusele uus server?


Nendes volitustes on kaks osa, API võti ja API ID; me vajame mõlemat. Enne kui läheme järgmise sammu juurde, avame brauseris teise vahekaardi ja läheme aadressile https://launchbtcpay.lunanode.com/


Siin palutakse teil esitada oma API võti ja API ID. See on selleks, et teaksite, et just teie olete see, kes selle uue serveri esitas. API võti peaks olema endiselt avatud teie eelmises vahekaardis; kui kerite allolevas tabelis alla, leiate API ID.


Saate minna tagasi lehele, kus on Launcher, täita väljad oma API võtme ja ID-ga ning klõpsata nupule Jätka.


![image](assets/en/115.webp)


Järgmises etapis saate anda domeeninime. Kui teil on juba oma domeen ja soovite seda BTCPay Server'i jaoks kasutada, veenduge, et lisate ka DNS-kirje (nn A-kirje) oma domeenile. Kui teil ei ole domeeni, kasutage selle asemel LunaNode'i pakutavat domeeni (seda saate hiljem BTCPay Serveri seadetes muuta) ja klõpsake nuppu Continue (Jätka).


Lisateave BTCPay Serveri DNS kirje seadmise või muutmise kohta; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### BTCPay serveri käivitamine LunaNode'is


Pärast eelnevate sammude tegemist saame määrata kõik meie uue serveri valikud. Siin valime Bitcoin (BTC) kui meie toetatud valuuta. Samuti saame määrata e-posti, et saada teateid krüpteerimissertifikaatide uuendamise kohta, mis on valikuline.


Selle juhendi eesmärk on seadistada Mainnet keskkond (tegelik Bitcoin), kuid LunaNode võimaldab arenduse eesmärgil seadistada ka Testnet või Regtest. Me jätame selle juhendi jaoks Mainnet valikule.


Saate valida oma Lightning rakendamise. LunaNode pakub kahte erinevat rakendust, LND ja Core Lightning. Selles juhendis võtame LND. Mõlemal implementatsioonil on vähe, kuid tõelisi erinevusi; selle kohta soovitame lugeda põhjalikku dokumentatsiooni: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode pakub mitut virtuaalmasina (VM) paketti. Need erinevad hinnaklassi ja serveri spetsifikatsioonide poolest. Selle juhendi jaoks piisab m2-plaanist; kui olete aga valinud valuutaks rohkem kui Bitcoin, kaaluge vähemalt m4-plaani kasutamist.


Kiirendada Blockchain esialgset sünkroniseerimist; see on vabatahtlik ja sõltub teie vajadustest. On olemas täiustatud võimalusi, näiteks Lightning Alias'i määramine, konkreetsele GitHubi väljaandele viitamine või SSH-võtmete määramine; ühtegi neist ei käsitleta selles juhendis.


Pärast vormi täitmist peate klõpsama nupule Launch VM ja Lunanode hakkab looma teie uut VM-i, sealhulgas sellele paigaldatud BTCPay Server'i. See protsess võtab paar minutit; kui teie server on valmis, annab LunaNode teile lingi teie uuele BTCPay Serverile.


Pärast loomise protsessi klõpsake BTCPay serveri lingil; siin palutakse teil luua administraatori konto.


![image](assets/en/117.webp)


### Oskuste kokkuvõte


Selles osas õppisite:



- LunaNode'i konto loomine ja rahastamine
- BTCPay Server Launcher'i kasutamine oma serveri loomiseks


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Kirjeldage mõningaid erinevusi BTCPay Serveri instantsi käitamise vahel VPS-is ja konto loomise vahel hostitud instantsis.


## BTCPay Serveri paigaldamine Voltage keskkonda


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Sa tutvud Voltage.cloud'iga kui hostinguteenuse pakkujaga, tutvud BTCPay serveri kasutamise esimeste sammudega ja õpid kasutama Lightning Network. Kui oleme kõik sammud läbi käinud, saate käivitada Bitcoin vastuvõtva veebipoe või ühisrahastusplatvormi!


See on üks paljudest võimalustest BTCPay Serveri kasutuselevõtuks. Lisateavet leiate meie dokumentatsioonist.

https://docs.btcpayserver.org.


### BTCPay Server - Voltage.cloud kasutuselevõtt


Kõigepealt minge veebisaidile Voltage.cloud ja registreerige uus konto. Konto loomisel saate registreerida 7-päevase tasuta prooviperioodi. Klõpsake kas üleval paremal asuvale registreerimisele või kasutage nende avalehel olevat valikut "Proovige tasuta 7-päevast prooviperioodi".


![image](assets/en/118.webp)


Pärast konto loomist klõpsake oma armatuurlaual nupule "NODES". Kui oleme valinud Nodes ja loonud uue sõlme, kuvatakse meile võimalikud sõlme Voltage pakkumised. Kuna selles juhendis käsitletakse ka Lightning Network, siis Voltage'is peame enne BTCPay serveri loomist esmalt valima oma Lightning rakendamise. Klõpsake LightningNode.


![image](assets/en/119.webp)


Siin peate valima, millist Lightning-sõlme soovite. Voltage on erinevaid võimalusi teie valgustuse seadistamiseks. See on erinev näiteks LunaNode'i kasutuselevõtmisel. Selle juhendi eesmärkidel piisab Lite Node'ist. Loe erinevuste kohta lähemalt Voltage.cloudist.


![image](assets/en/120.webp)


Andke oma sõlmpunktile nimi, määrake parool ja kindlustage see parool. Kui see parool läheb kaduma, kaotate juurdepääsu oma varukoopiatele ja Voltage ei saa seda taastada. Looge sõlme ja Voltage näitab teile edusamme. Voltage on loonud teie Lightning Node'i. Nüüd saame luua BTCPay serveri instantsi ja pääseda otse Lightning Network-le ligi.


Klõpsake oma armatuurlaua vasakus ülaosas nupule Nodes. Siin saate seadistada oma BTCPay serveri järgmise osa. Kui olete sõlmede ülevaates, klõpsake "create new" (loo uus). Saate sarnase ekraani nagu enne. Nüüd valime Lightning Node'i asemel BTCPay Server.


Voltage näitab teie BTCPay serveri geograafilist asukohta, mis asub USA läänepoolses piirkonnas. Siin näete ka serveri majutuskulu. Klõpsake nuppu Create ja andke oma BTCPay serverile nimi. Lubage Lightning ja Voltage näitab teile eelmises etapis loodud Lightning-sõlme. Klõpsake Create ja Voltage loob BTCPay Serveri instantsi.


![image](assets/en/121.webp)


Pärast seda, kui vajutate nuppu create, esitab Voltage teile vaikimisi kasutajanime ja parooli. Need on sarnased teie eelnevalt Voltage'is määratud parooliga. Klõpsake nupule Logi kontole, et suunata teid BTCPay serverisse.


Tere tulemast oma uude BTCPay serverisse. Kuna me oleme Lightning'i juba loomisprotsessis seadistanud, näitab see, et Lightning on juba sisse lülitatud!


### Oskuste kokkuvõte


Selles peatükis õppisite:



- Konto loomine Voltage.cloud'is
- Sammud BTCPay Serveri käivitamiseks koos Lightning node'iga kontol


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Millised on peamised erinevused Voltage'i ja LunaNode'i seadistuste vahel?


## BTCPay serveri paigaldamine Umbreli sõlme


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Nende sammude lõpus saate oma BTCPay poes välkmakseid vastu võtta oma kohalikus võrgus. See protsess kehtib ka siis, kui te haldate vihmavarju sõlme restoranis või ettevõttes. Kui soovite selle poe ühendada avaliku veebisaidiga, järgige edasijõudnute harjutust, et oma umbrel-sõlme avalikkusele eksponeerida.


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay Server - Umbreli kasutuselevõtt


Kui teie Umbrel-sõlm on täielikult sünkroonitud Bitcoin Blockchain-ga, minge Umbrel App Store'i ja otsige rakenduste alt BTCPay Server.


![image](assets/en/123.webp)


Rakenduse üksikasjade vaatamiseks klõpsake BTCPay Serveril. Kui BTCPay Serveri andmed on avatud, kuvatakse all paremas nurgas nõuded rakenduse nõuetekohaseks toimimiseks. See näitab, et selleks on vaja Bitcoin ja Lightning node. Kui te ei ole Lightning Node'i oma Umbrelile paigaldanud, klõpsake nuppu Install. See protsess võib võtta paar minutit.


![image](assets/en/124.webp)


Pärast välgussõlme paigaldamist:


1. Klõpsake rakenduse üksikasjades või Umbrels armatuurlaual oleval rakendusel Avatud.

2. Klõpsake uue sõlme seadistamine; teile kuvatakse 24 sõna teie välgussõlme taastamiseks.

3. Kirjutage need üles.


![image](assets/en/125.webp)


Umbrel küsib äsja kirja pandud sõnade kinnitamist. Pärast Lightning-sõlme seadistamist pöörduge tagasi Umbrel App Store'i ja leidke BTCPay Server. Klõpsake nupule install ja Umbrel näitab, kas vajalikud komponendid on paigaldatud ja kas BTCPay Server nõuab juurdepääsu nendele komponentidele. Pärast installimist klõpsake rakenduse üksikasjade paremas ülaosas nupule Open (Avatud) või avage BTCPay Server oma Umbreli armatuurlaua kaudu.


Umbrel küsib äsja kirja pandud sõnade kinnitamist.


![image](assets/en/126.webp)


**!?Märkus!?**


Veenduge, et hoiustate neid turvalises kohas, nagu eelnevalt võtmete hoiustamisel õpitud.


Pärast Lightning-sõlme seadistamist pöörduge tagasi Umbrel App Store'i ja otsige üles BTCPay Server. Klõpsake nupule install ja Umbrel näitab, kas vajalikud komponendid on paigaldatud ja kas BTCPay Server nõuab juurdepääsu nendele komponentidele.


![image](assets/en/127.webp)


Pärast installimist klõpsake rakenduse üksikasjade paremas ülaosas nupule Avatud või avage BTCPay Server oma Umbreli armatuurlaua kaudu.


![image](assets/en/128.webp)


### Oskuste kokkuvõte


Selles osas õppisite:



- Sammud BTCPay Serveri paigaldamiseks koos Lightning-funktsiooniga Umbrel-sõlmele


### Teadmiste hindamine


#### KA kontseptuaalne ülevaade


Mille poolest erineb Umbreli seadistus kahest eelmisest hostitud valikust?


# Lõplik osa


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Arvamused ja hinnangud

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Kursuse kokkuvõte


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>