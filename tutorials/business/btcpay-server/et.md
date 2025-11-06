---
name: BTCPay server
description: BTC maksete vastuvõtmine ilma vahendajateta
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server on Nicolas Dorier' loodud tasuta, avatud lähtekoodiga tarkvarapakett, mis võimaldab bitcoin-makseid vastu võtta ilma vahendajateta. See on loodud selleks, et pakkuda autonoomiat ja finantssõltumatust, paigaldatakse oma serverisse ja see pakub täielikku tehinguhaldust, alates arvete esitamisest kuni on-chain või Lightning Network maksete valideerimiseni ja raamatupidamiseni. See integreerub hõlpsasti e-kaubanduse saitidega (WooComerce, Shopify jne) või seda saab kasutada füüsiliste kaupluste (*POS*) makseterminalina.



BTCPay Server on kahtlemata kõige arenenum lahendus kaupmeestele, kes soovivad bitcoini vastu võtta. See on turvalisuse, suveräänsuse ja konfidentsiaalsuse mõttes kõige põhjalikum ja töökindlam tarkvara. Teisalt on see ka kõige keerulisem paigaldada ja hooldada. On olemas ka lihtsamaid alternatiive: mõned on täielikult hoiustatud, nagu OpenNode, samas kui teised pakuvad huvitavat kompromissi kasutusmugavuse ja suveräänsuse vahel, nagu Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Selle õpetuse eesmärk on juhtida teid samm-sammult läbi BTCPay Serveri paigaldamise, konfigureerimise ja kasutamise, et saaksite kasutusele võtta turvalise, sõltumatu makseinfrastruktuuri kooskõlas Bitcoin eetikaga.



## BTCPay serveri omadused



Tsentraliseeritud Bitcoin müügipunkti lahendused, nagu näiteks *OpenNode*, pakuvad kasutusmugavust, kuid sõltuvad kolmanda osapoole ettevõttest, kuna neid ei saa ise hallata ja need on enamasti patenteeritud. Kuigi need lihtsustavad maksete seadistamist, hõlmavad nad komisjonitasusid ja seavad oma kasutajad rohkem riskidele kui BTCPay Server'i sarnane lahendus, nii rahaliste vahendite hoidmise kui ka konfidentsiaalsuse osas.



BTCPay Server on suunatud veebipõhistele või füüsilistele kaupmeestele, ühendustele ja mittetulundusühingutele, kes soovivad saada annetusi bitcoinides. Samuti on see ideaalne lahendus projektide omanikele ja arendajatele, kes soovivad otsest toetust oma kogukonnalt.



BTCPay Serveri eripära on järgmised:




- selle **täielik autonoomia**,
- **KYC** menetluse puudumine,
- täielik kontroll rahaliste vahendite üle**,
- **Platvormitasude kaotamine**.



Muutudes oma maksetöötlejaks, kaotate igasuguse sõltuvuse tsentraliseeritud kolmandast osapoolest teie ja teie klientide vahel. Saate võtta makseid vastu otse bitcoinides ja generate maksearveid. See tagab, et ei teid ega teie ettevõtet ei saa keegi teine keelata. Te mängite nii panga kui ka maksetöötleja rolli, ilma et peaksite iga tehingu eest vahendajale vahendustasu maksma.



**on-chain** tehingutasud jäävad, kuid neid saab vähendada, kui kasutada **Liquid** või **Lightning** võrku.



Lisaks :




- Täielikult kohandatav kasutajaliides ja arved;
- Native **Tor** tugi täiustatud konfidentsiaalsuse tagamiseks;
- Toetus **rahastamise**, **POS** ja **maksunuppude** jaoks;
- Ühildub paljude valuutadega ;
- Bitcoin otsetoetused ja vastastikused maksed ;
- Täielik kontroll oma isiklike võtmete üle;
- Täiustatud privaatsus ;
- Tõhustatud turvalisus ;
- Isehostitav tarkvara ;
- Toetus **SegWit** ja **Valgusvõrgu** jaoks;
- Sisene, sõlmpõhine portfell koos riistvaraportfellide integreerimisega.



## BTCPay serveri paigaldamine ja seadistamine



### Hosting-režiimi valimine



BTCPay Serverit saab paigaldada mitmel erineval viisil. Sõltuvalt teie vajadustest ja ressurssidest on kolm peamist võimalust:




- BTCPay server, mida haldab kolmas osapool**: kasutate platvormi, mis haldab teenust teie eest. See on lihtne, kuid tavaliselt mitte tasuta.
- BTCPay Server, mis on ise majutatud pilveserveris** (nt [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) või mõne muu teenusepakkuja kaudu). See on soovitatav lahendus enamikule algajatele kaupmeestele.
- BTCPay Server on paigaldatud teie enda riistvarale (lokaalselt)** : arvutile, mini-PC-le või Umbrelile. See meetod on tehnilisem, kuid pakub täielikku sõltumatust.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Alustava kaupmehe jaoks on **kasutamine pilveserveris** parim kompromiss autonoomia, lihtsuse ja turvalisuse vahel, ilma et oleks vaja hallata kogu tehnilist infrastruktuuri.



BTCPay Serveri saab kiiresti kasutusele võtta mitmete veebimajutuse pakkujate kaudu. Nende seas paistab **Voltage** silma kui võrdluslahendus kasutajatele, kes vajavad **lugevat**, **professionaalset** ja **sovernalist** infrastruktuuri.



### Loo BTCPay serveri instants Voltage'ile



**Voltage** on Bitcoin ja Lightning hostinguplatvorm, mis võimaldab teil koheselt kasutusele võtta oma BTCPay server, ilma keerulise seadistamise või serveri hooldamiseta.



Külastage [ametlik Voltage'i veebisait](https://voltage.cloud).



![capture](assets/fr/03.webp)



Looge **kasutajakonto** kehtiva e-posti aadressi ja tugeva parooliga.



![capture](assets/fr/04.webp)



Voltage pakub **vaba 7-päevast prooviperioodi**. Pange tähele, et pärast 7-päevast tasuta prooviperioodi kutsutakse teid üles sõlmima fikseeritud tellimuslepingut hinnaga **25 $ kuus**, et jätkata **sõlmede aktiivsena hoidmist**.



Kui olete loonud Voltage'i konto ja esimest korda sisse loginud, suunatakse teid edasi kodulehele, millel on kaks peamist jaotist:




- **Infrastruktuuri** sektsioon Lightning-sõlmede, Bitcoin Core'i, BTCPay Serveri ja muude Bitcoin teenuste haldamiseks pilves;
- ja **Maksed** sektsioon, mis võimaldab teil kasutada Voltage'i API Lightning'i, et integreerida Bitcoin makseid kohandatud rakendustesse.



**BTCPay Server** instantsi kasutuselevõtmiseks klõpsake nupul **juurdepääsu infrastruktuur**. Siin saate luua, hallata ja jälgida kõiki oma teenuseid, sealhulgas Bitcoin sõlme ja BTCPay Server'i.



#### Loo grupp



Enne teenuse kasutuselevõttu palub platvorm teil **looda grupp**. **Rühm** (tööruum) on tööruum, mis koondab kõik teie Bitcoin- ja Lightning-teenused (nt sõlme, BTCPay Server, ekspluateerija jne). See on natuke nagu kaust, mis sisaldab teie erinevaid projekte.



![capture](assets/fr/05.webp)



Selle õpetuse jaoks on meie loodud grupi nimi **Genesis**. Soovi korral võite lisada profiilipildi. Kui see on tehtud, vajutage nupule **Loo**. Võite kutsuda teisi kasutajaid grupiga liituma ja soovi korral isegi grupi nime muuta.



Rühma avalehel kuvatakse mitu valikut:




- Lightning Nodes** : täieliku Lightning-sõlme (LND) kasutuselevõtmiseks ;
- Bitcoin tuumasõlmed** : täieliku Bitcoin sõlme käivitamiseks ;
- BTCPay Server** : BTCPay kasutusvalmis instantsi majutamiseks;
- Nostr Accounts**: Nostr identiteetide haldamiseks.



Aktiveerige **kaksikautentimine (2FA)**, et kaitsta oma kontot ja teenuseid (kui nupp on deaktiveeritud, on see punane).



![capture](assets/fr/06.webp)



Klõpsake valikute hulgas **BTCPay Server** ja seejärel **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Seejärel palub Voltage teil **luua ja konfigureerida oma BTCPay serveri instants**, valides **teenuse nime** (1) ja lubades Lightning-maksed (2).



Kui otsustate Lightning-makseid vastu võtta, vajate Lightning-sõlme.



Kui teil ei ole veel Bitcoin või Lightning sõlme, soovitab Voltage teil selle automaatselt luua.



Klõpsake nuppu **Loo välgussõlm** (3) .



![capture](assets/fr/08.webp)



Kui olete sõlme loomise liideses, palutakse teil valida **standardse** ja **professionaalse** kujunduse vahel.



Saate luua reaalse sõlme (**Mainnet**) või testsõlme (**Testnet**). Seejärel klõpsake nuppu **Jätka**.



![capture](assets/fr/09.webp)



Kasutame selle õpetuse jaoks standardplaani. Sisestage **sõlme nimi**, **parool** ja vajutage nuppu **Loo**.



![capture](assets/fr/10.webp)



Mõne hetke pärast on teie sõlmpunkt töökorras ja te saate avada vaba kanali, mille vastuvõtuvõimsus on 500 000 sats.



![capture](assets/fr/11.webp)



Veidi allapoole paremal leiate kogu vajaliku teabe oma sõlme kohta!



![capture](assets/fr/12.webp)



Nüüd, kui meie Lightning-sõlm on käivitatud ja töötab, pöördume tagasi BTCPay-serveri paigaldamise juurde. Nüüd saate klõpsata nupule **Create BTCPay**.



![capture](assets/fr/13.webp)



Avaneb lehekülg, kus on teie vaikimisi sisselogimise andmed ja teade, milles palutakse teil muuta oma esialgset parooli. Kui olete selle teinud, klõpsake kasutajaliidesele juurdepääsuks nupule **Login Now**.



![capture](assets/fr/14.webp)



See on kõik! Teie BTCPay server on kasutusvalmis. Teid suunatakse otse teie BTCPay serveri sisselogimislehele.



![capture](assets/fr/15.webp)



Kui olete sisse loginud, konfigureerige oma esimene **pood**:





- Anna sellele **nimi**.





- Valige **eelvaluuta** (EUR, USD, CFA jne).





- Valige **Vahetuskursi teenusepakkuja** (nt CoinGecko).



![capture](assets/fr/16.webp)



Seejärel suunatakse teid ümber oma poe armatuurlauale. Armatuurlaual märkate, et nupp **Loo oma pood** on märgitud rohelisega, kuna see samm on juba tehtud.



![capture](assets/fr/17.webp)



Veidi allpool on nupud **Configure wallet** ja **Configure Lightning node**. Meie puhul oleme juba ühendanud Lightning-sõlme, mis töötab pingel. Seega ei pea me seda siin tegema.



Liigume edasi portfelli konfigureerimise juurde. Vajutage nupule **Portfelli konfigureerimine**.



Kuna me alles alustame BTCPay Serveriga, ühendame olemasoleva wallet. Seega vajutage **Ühendage olemasolev portfell**.



![capture](assets/fr/18.webp)



Seejärel peate valima oma **impordimeetodi**. Valikuvõimaluste hulgast valige **Esita laiendatud avalik võti**.



![capture](assets/fr/19.webp)



Ühendades olemasoleva wallet, saate oma makseid **direktselt sellele välisele wallet-le**, ilma et BTCPay serveril oleks juurdepääs teie isiklikule võtmele. Seega, isegi kui server häkitakse või avalik võti (`xpub`) on ohustatud, saaks ründaja vaadata teie tehinguajalugu, kuid oleks **võimatu pääseda ligi teie rahalistele vahenditele**.



Kui klõpsate nupule **Kirjuta laiendatud avalik võti**, siis **juhitakse teid **leheküljele**, kus peate selle võtme esitama.



Nüüd otsime välja **laiendatud avaliku võtme**.



### Bitcoin wallet ühendamine



Maksete vastuvõtmiseks peate oma kauplusega ühendama Bitcoin wallet. Selleks on teil mitu võimalust:





- Riistvaraportfell** (Ledger, Trezor, Coldcard ...) ;





- Tarkvaraportfell** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** sisemine wallet (ei ole soovitatav, kuna see on vähem turvaline ja paljastab teie raha rohkem, kui serverisse häkitakse).



Selles õpetuses kasutame **tarkvaraportfelli**, mis on algse konfiguratsiooni jaoks paremini kättesaadav. Saate valida mitmete ühilduvate rakenduste vahel: **Electrum**, **Phoenix**, **Zeus**, **Muun** jne.



Demonstratsiooniks kasutame **Electrum**. Avage **Electrum**, klõpsake **Portfoolio** ja seejärel **Informatsioon** :



![capture](assets/fr/20.webp)



Seejärel kopeerige **peamise avalik võti (xpub)**.



![capture](assets/fr/21.webp)



Kui olete avaliku põhivõtme kopeerinud, kleepige see BTCPay serveri lehel olevasse väljale.



![capture](assets/fr/22.webp)



Pärast kinnitamist suunatakse teid ümber oma poe armatuurlauale.



![capture](assets/fr/23.webp)



### Müügipunkti (PoS) loomine



Kui olete oma poe ja portfelli seadistanud, saate nüüd luua **Müügipunkti (PoS)**, et hakata Bitcoin makseid otse oma klientidelt vastu võtma.



See **BTCPay Serveri** integreeritud funktsioon on ideaalne **kaupmeestele, käsitöölistele, restoranipidajatele või teenusepakkujatele**, kes soovivad võtta vastu Bitcoin ** ilma veebisaidi** või tehniliste eriteadmisteta.



### Mis on müügipunkt?



**PoS** on **ühendatud POS-liides**, mis toimib **Bitcoin makseterminalina**.


See võimaldab teil :




- Looge **toodete või teenuste menüü** fikseeritud hindadega.
- Looge **pikarekvisiitarve koos QR-koodiga**, mida saab skaneerida.
- Jagage **Makse URL**, millele on võimalik ligi pääseda nutitelefoni, tahvelarvuti või arvuti kaudu.



Teisisõnu, PoS muudab teie BTCPay serveri **direktseks müügiliideseks**, kus iga makse laekub **sellele Bitcoin wallet**, ilma vahendajateta.



### PoSi konfigureerimine



BTCPay armatuurlaual klõpsake **PLUGINS**, seejärel **Müügipunkt**.



Seejärel klõpsake nupule **Loo uus PoS-rakendus**. See tegevus lisab **Uue rakenduse** teie BTCPay kauplusesse, justkui paigaldaksite sisemüügi minisaidi.



Avaneb lehekülg oma rakenduse loomiseks. Määrake **rakenduse nimi**: see on sisemine nimi, mis on nähtav ainult teie armatuurlaualt (nt _Shoe Shop_).



Kinnitamiseks klõpsake **Loo**.



![capture](assets/fr/24.webp)



Pärast loomist suunatakse teid ümber müügipunkti **Detailne konfiguratsioonilehekülg**.



### Müügiliidese kohandamine



Sellel lehel saate määrata oma PoSi olulised elemendid:





- Rakenduse nimi** (sisemine haldusnimi, mida võib igal ajal muuta).





- Näidata pealkiri** (mida teie kliendid näevad lehe ülaosas).





- Müügipunkti stiil** (režiim **Kirjeldus** sobib teenuste, näiteks juuksuriteenuste või toitlustamise jaoks, samas kui režiim **Tootekataloog** on ideaalne kaupluste jaoks, mis pakuvad mitmeid kaupu).





- Näita valuuta** (vali **XOF**, **EUR** või **USD** vastavalt sinu tavapärastele hindadele).





- Toote nimekiri** (lisage siia oma tooted, kirjeldused ja hinnad).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Salvestage ja testige oma PoSi



Kui olete seadistamise lõpetanud, klõpsake **Save**, et salvestada oma seaded, seejärel **View**, et vaadata oma PoSi eelvaadet.



Näete oma tooteid tutvustavat lehekülge, kus iga nupp vastab ühele tootele või teenusele.



Niipea, kui klient valib toote :



1. BTCPay genereerib automaatselt Bitcoin või Lightning** arve.



2. Ekraanile ilmub **QR-kood**.



3. Kliendid saavad **skaneerida ja maksta otse** oma Bitcoin walletga.




![capture](assets/fr/27.webp)



### Lõpptulemus



Nüüd on teil täielik **Bitcoin müügipunkt**, mida saate :





- Avage nutitelefonist või tahvelarvutist oma poes ;





- Kuvatakse ekraanil, et klient saaks skaneerida ;





- Või jagada avaliku **URL** kaudu, näiteks lihtsustatud tellimislehe kaudu.



Iga makse puhul kantakse summa automaatselt **sellele BTCPay wallet**, ilma vahendajate või kolmandate osapoolte tasudeta.


See muudab teie PoSi **siseseisvaks Bitcoin makseterminaliks**.




## Igapäevane kasutamine



Enne reaalsete maksete väljamaksmist soovitame teha **testi**, et kontrollida, kas kõik toimib korralikult.



### Testi makse





- Looge arve** oma PoS-liidesest (näiteks 1 satoshi toode või väike summa).





- Skaneerige ekraanil olev QR-kood**, kasutades Bitcoin või Lightning wallet (näiteks **Phoenix**, **Muun** või **Wallet või Satoshi**).




![capture](assets/fr/28.webp)





- Kinnitage makse** oma wallet-s: tehing saadetakse koheselt.





- Tagasi BTCPay serverisse**: arve kuvatakse nimekirjas kui **Maksetud**.



![capture](assets/fr/29.webp)



Palju õnne! Teie müügipunkt on nüüd **funktsionaalne**. Saate hakata oma klientidelt Bitcoin makseid vastu võtma, lihtsalt, kiiresti ja ilma vahendajateta.



### Loo kliendile arve



Klõpsake menüüs **Arveid** valikut **Uue arve**.



![capture](assets/fr/30.webp)



Sisestage **summa** ja **kohaliku valuuta** (BTCPay arvutab automaatselt BTC-ga võrdväärse summa), samuti muud tootega seotud andmed.



![capture](assets/fr/31.webp)



Jagage kliendile **QR-kood** või **URL**.



![capture](assets/fr/32.webp)



### Jälgi saadud makseid



Menüüs **Arveid** näete endiselt kõigi oma tehingute nimekirja.


Võimalikud staatused on :





- Ootel**: makse ei ole veel kinnitatud.





- Makstud**: makse kinnitatud.





- Aegunud**: arve, mida ei ole tähtajaks tasutud.



### Kliendi raha tagasimaksmine



Valige menüüst **Arved** hüvitatav arve.



![capture](assets/fr/33.webp)



Klõpsake nupule **Refund** ja sisestage kliendi antud Bitcoin aadress.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Aruanded ja andmete eksport



BTCPay Server võimaldab teil **eksportida oma tehinguid** (CSV või Exceli formaadis). See on väga praktiline teie raamatupidamis- ja kassaseire jaoks.



![capture](assets/fr/36.webp)



Klõpsake menüüs **Raport** valikut **Eksport**: kõik teie tehingud salvestatakse CSV-faili, mida saate seejärel kohapeal vaadata.



## Ohutus ja parimad tavad



BTCPay Serveri poolt antud autonoomia (täielik suveräänsus teie vahendite üle) on tõeline tugevus. Kuid selle vabadusega kaasneb ka suurem vastutus turvalisuse osas. Haldades oma makseid ise, võtad sa endale oma panga rolli. Seepärast on hädavajalik võtta kasutusele parimad tavad, et kaitsta oma raha, andmeid ja infrastruktuuri. Siin on peamised punktid, mida tuleks arvesse võtta.



### Turvaline juurdepääs serverile





- Kasutage tugevat salasõna: kombineerige suur- ja väiketähti, numbreid ja erimärke. Vältige olemasoleva parooli korduvkasutamist.
- Aktiveerige kahefaktoriline autentimine (2FA), et pääseda ligi oma BTCPay liidesele.
- Uuendage regulaarselt oma operatsioonisüsteemi, BTCPay Serveri instantsi ja sõltuvusi (Docker, Bitcoin node, Lightning node...). Uuendused parandavad sageli turvaauke.



### Privaatsete võtmete haldamine ja varundamine





- Salvestage oma isiklikud võtmed ja seemnefraasid võrguühenduseta füüsilisel andmekandjal (paber või metall).
- Eelistatavalt kasutage wallet riistvara wallet.
- Hoidke oma varukoopiaid mitmes koopias eraldi, kaitstud füüsilises kohas.



### Turvalised maksed ja konfidentsiaalsus





- Kasutage Tor-võrku või VPN-i, et varjata oma serveri IP-aadressi ja kaitsta oma privaatsust.
- Lülita serveris välja mittevajalikud pordid ja piira SSH-ühendusi ainult usaldusväärsetele aadressidele.
- Aktiveerige HTTPS (SSL-sertifikaat) kõigi BTCPay veebiliidese ühenduste jaoks.
- Ärge kunagi jagage oma haldusliidest personaliga, kes ei ole koolitatud Bitcoin portfelli haldamiseks.



### Lightning-võrgu parimate tavade rakendamine



Teie kauplus on ühendatud Voltage'is** asuva **Lightning-sõlme külge, mis lihtsustab oluliselt võrgu tehnilist haldamist. Sellegipoolest on endiselt oluline võtta kasutusele **häid jälgimis- ja turvameetmed**:





- Salvestage oma Voltage-sõlme API** sisselogimis- ja juurdepääsuklahvid (mis võimaldavad BTCPayga ühendust luua).
- Kaitske oma Voltage'i kontot** kahefaktorilise autentimise ja tugeva parooliga.
- Jälgige oma Voltage'i armatuurlaualt sõlme ja kanalite olekut**: see aitab teil avastada anomaaliaid või desünkroniseerimist.
- Vältige oma API** kasutajatunnuste jagamist või nende avalikustamist (nt saidi koodis).
- Migratsiooni korral tuleb lihtsalt **ümberkonfigureerida BTCPay ja Voltage vaheline ühendus**: kanalit ei ole vaja käsitsi sulgeda.



Voltage'i abil saate kasu **turvalisest, kõrgelt kättesaadavast** ja **automaatselt varundatud** infrastruktuurist, säilitades samal ajal **täieliku suveräänsuse oma Lightning-maksete üle**.



### Korraldada ja struktureerida sisemisi protseduure





- Määrake selge juurdepääsupoliitika: kes võib luua arveid, vaadata makseid, pääseda sõlme jne.
- Dokumenteerige oma varundus- ja taastamisprotseduurid, et saaksite intsidendi korral kiiresti reageerida.
- Testige regulaarselt oma varukoopiate taastamist, et veenduda, et need toimivad korralikult.
- Koolitage oma töötajaid või kaastöötajaid põhilistes operatiivturbe küsimustes: valvsus andmepüügi vastu, turvaliste paroolide kasutamine, konfidentsiaalsuse austamine.



### Järelevalvet teostada ja kehtestada pidev hooldus





- Jälgige pidevalt oma serveri tegevust, kasutades logimis- või jälgimisvahendeid.
- Planeerige perioodiline turvalisuse ülevaatus: kontrollige uuendusi, juurdepääsu, varukoopiaid ja tehingute järjepidevust.



Palju õnne! Olete jõudnud selle õpetuse lõpuni. Nüüd saate BTCPay Serveriga iseseisvalt hakkama, mis muudab teie poe haldamise lihtsamaks.



Et rohkem teada saada, soovitan teil läbida meie täielik koolituskursus Bitcoin integreerimise kohta teie ettevõttesse:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a