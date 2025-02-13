---
name: Bisq 2
description: Täielik juhend Bisq 2 kasutamise ja bitcoinide P2P vahetamise kohta
---
![cover](assets/cover.webp)

## Sissejuhatus

KYC-vabad peer-to-peer (P2P) börsid on kasutajate konfidentsiaalsuse ja finantsautonoomia säilitamiseks hädavajalikud. Need võimaldavad otsetehinguid üksikisikute vahel ilma isikusamasuse kontrollimise vajaduseta, mis on oluline nende jaoks, kes hindavad privaatsust. Teoreetiliste mõistete põhjalikumaks mõistmiseks vaadake kursust BTC204:

https://planb.network/courses/btc204
### Mis on Bisq 2?

Bisq 2 on 2024. aastal käivitatud populaarse detsentraliseeritud Bisq-vahetuse uus versioon. Erinevalt oma eelkäijast on Bisq 2 välja töötatud nii, et see toetab mitut vahetusprotokolli, pakkudes kasutajatele suuremat paindlikkust.

**Vaimne uus funktsioon:**


- Mitme privaatsusvõrgustiku (Tor, I2P) tugi
- Mitu identiteeti suurema konfidentsiaalsuse tagamiseks
- REST API kauplemisrobotite jaoks
- Mitme portfooliotüübi tugi
- Kohustusliku deposiidiga rollisüsteem BSQ-s

Käesolev juhend keskendub ainult Bisq Easy'le, mis on praegu ainus olemasolev protokoll. Bisq Easy on mõeldud spetsiaalselt uutele Bitcoini kasutajatele. See protokoll võimaldab kasutajatel osta ja müüa Bitcoine fiat-valuutade vastu detsentraliseeritud peer-to-peer platvormil. Tehingud on piiratud 600 USA dollari ekvivalendiga (minimaalselt 6 USA dollariga) ja vahetusturve sõltub BTC-müüjate mainest. Bisq Easy'l ei ole kauplemistasusid ega tagatise nõudeid. Bisq Easy peaks asendama Bisq 1 alla 600 USD (või samaväärse summa) sularahavahetuse puhul.

** Peamised omadused:**


- Platvormiülene töölauarakendus
- Saadaval on mitu vahetusprotokolli
- Detsentraliseeritud P2P-võrk
- Keskendumine konfidentsiaalsusele (KYC-i puudumine, Tor'i kasutamine)
- Mittehooldusõiguslik (teil säilib kontroll oma rahaliste vahendite üle)
- Avatud lähtekood (AGPL)

### Erinevused võrreldes Bisq 1-ga

**Ostjatele:**


- Tagatisraha ei nõuta
- Kauplemistasud puuduvad
- Kaevandamistasud puuduvad
- Müüja mainel põhinev turvalisus
- Madalamad kauplemislimiidid (võrdub 600 USA dollariga)

**Müüjatele:**


- Tagatisraha ei nõuta
- Maine loomine
- BSQ põletamise või BSQ sidemete loomise võimalus
- Potentsiaalselt suurem müügipreemia (10-15% üle turuosa)

**Tähtis märkus:** Kui Bisq Multisig protokoll on rakendatud Bisq 2-s, saab Bisqi vana versiooni järk-järgult kaotada. Bisq 1 kasutatakse siiski jätkuvalt Bisq CADi ja BSQ-BTC vahetuste haldusvahendina.

### Vahetuse protsess


- Pakkumise tegija määratleb vahetuse tingimused
- Kui kauplejad on tingimustes (makseviis ja hind) kokku leppinud, algab vahetus
- Müüja saadab ostjale oma pangaandmed ja ostja saadab müüjale oma Bitcoini aadressi
- Ostja teeb makse sularahas ja teatab sellest müüjale
- Kui makse on laekunud, saadab müüja bitcoinid ostja aadressile
- Vahetamine on lõpule viidud, kui ostja saab bitcoinid kätte

### Olulised eeskirjad


- Enne makseandmete vahetamist võib vahetuse tühistada ilma põhjendusteta
- Pärast üksikasjade vahetamist võib kohustuste täitmata jätmine kaasa tuua väljasaatmise
- Pangaülekannete puhul **ei tohi kunagi kasutada makse põhjenduses väljendeid "Bisq" või "Bitcoin "** (see võib põhjustada raha külmutamise või isegi saaja või maksja pangakonto blokeerimise)
- Ettevõtjad peavad protsessi jälgimiseks vähemalt kord päevas sisse logima
- Probleemide korral võivad ettevõtjad kasutada vahendaja teenuseid

## Paigaldamine ja konfigureerimine

### 1. Laadige alla ja kontrollige Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Mine [bisq.network](https://bisq.network/downloads/)
- Laadige alla teie operatsioonisüsteemile vastav Bisq 2 versioon (kerige lehekülge allapoole)
- Kontrollige allalaaditud faili autentsust (tungivalt soovitatav). Allkirjade kontrollimise üksikasjalik juhend on esitatud järgmises õpetuses:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Paigaldamine vastavalt teie süsteemile

Palun järgige oma operatsioonisüsteemile vastavaid paigaldussamme. Kui teil tekib paigaldamisel raskusi, võite tutvuda [ametliku Bisq wiki](https://bisq.wiki/Downloading_and_installing) üksikasjaliku juhendiga.

### 3. Esimene käivitamine


- Käivitage Bisq 2 ja nõustuge kasutustingimustega

![Conditions d'utilisation](assets/fr/01.webp)


- Loo uus profiil, valides nime ja avatari

![Création du profil](assets/fr/02.webp)


- Seejärel viiakse teid rakenduse peamisele armatuurlauale, kus saate käivitada Bisq Easy, et osta või müüa oma esimesi bitcoin'e

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Makseviiside seadistamine


- Juurdepääs maksekontode sektsioonile peamenüüst

![Liste des comptes de paiement](assets/fr/04.webp)


- Lisage uus makseviis, täites nõutud andmed

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Makseviiside eelkonfigureerimine on vabatahtlik, kuid soovitatav, et säästa aega kauplemisel. Te saate oma makseviise konfigureerida ka otse kauplemise ajal, võttes ühendust oma vahetuspartneriga.

### 5. Konto turvalisus

** Andmete varundamine:**

Erinevalt Bisq 1-st ei integreeri Bisq 2 praegu Bitcoini rahakotti: tehingud toimuvad seega teie enda väliste rahakottide kaudu. Sellegipoolest soovitame regulaarselt varundada oma Bisq 2 andmekausta. Oma andmekausta leidmiseks vaadake [ametlikku Bisq wiki](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Identiteedi haldamine:**

Bisq 2 võimaldab teil luua mitu identiteeti. Iga identiteeti saab kasutada erinevat tüüpi tehinguteks. Teie identiteedid salvestatakse andmekaustas.

## Bitcoinide ostmine ja müümine

### Kuidas osta Bitcoine

**Võimalus 1: Kasuta olemasolevat pakkumist**


- Valige põhiekraanil "Bisq Easy", vahekaart "Alustamine", seejärel klõpsake "Start trade wizard"

![Lancer trade wizard](assets/fr/06.webp)


- Valige "Osta Bitcoin" ja valige oma valuuta

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Seadistage oma eelistatud makseviisid (SEPA, Revolut jne)

![Configuration méthodes de paiement](assets/fr/09.webp)


- Sel hetkel on teil kas nimekiri pakkumistest, mis vastavad teie eelnevatele kriteeriumidele, või peate minema "Pakkumiste raamatusse"

![Liste des offres](assets/fr/10.webp)


- Teisel juhul saate pakkumisi kuvada ja filtreerida kasutajaliidese paremas ülaosas asuvate nuppude abil

![Filtres des offres](assets/fr/11.webp)


- Kui olete oma pakkumise valinud, peate vaid valima oma makseviisi ja seejärel kinnitama kauplemise kokkuvõtte

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Võimalus 2: Loo oma pakkumine**


- Valige "Bisq Easy" ja seejärel "Pakkumiste raamat"
- Valige oma kauplemispaar (nt BTC/EUR)
- Klõpsake nuppu "Loo pakkumine
- Järgige pakkumise loomise nõustaja: Määrake summa (fikseeritud või vahemik)

![Configuration du montant](assets/fr/20.webp)


- Valige aktsepteeritud makseviisid

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Kontrollige kokkuvõtet ja avaldage pakkumine

![Récapitulatif et publication](assets/fr/22.webp)

Kui vahetus on algatatud :


- Saada oma Bitcoini aadress või Lightning arve müüjale

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Saada müüja pangaandmed

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Tehke makse (mainimata "Bisq" või "Bitcoin")
- Teavitage müüjat oma maksest

![Notification paiement](assets/fr/18.webp)


- Oodake bitcoinide saabumist

![Attente réception](assets/fr/19.webp)

### Kuidas müüa Bitcoine?

Müügiprotsess Bisq 2-s järgib sarnast loogikat nagu ostmisel, samade põhietappidega, kuid vastupidises järjekorras. Võite luua oma müügipakkumise või vastata olemasolevale ostupakkumisele. Järgnevalt on esitatud protsessi eri võimaluste ja etappide jaotus:

**Võimalus 1: Müügipakkumise koostamine**


- Valige "Bisq Easy" ja seejärel "Pakkumiste raamat"
- Klõpsake "Loo pakkumine" ja valige "Müü Bitcoin"
- Konfigureerige oma pakkumine :
 - Valige valuuta (EUR, USD jne.)
 - Valige aktsepteeritud makseviisid
 - Määrake summa (vahemikus 6-600 USD)
 - Määrake oma hind (fikseeritud või % turuhinnast)
- Kontrollige üksikasju ja avaldage pakkumine

**Võimalus 2: Võtke vastu olemasolev pakkumine**


- Sirvi pakkumisi vahekaardil "Pakkumiste raamat"
- Filtreeri valuuta ja makseviisi järgi
- Valige endale sobiv pakkumine
- Kontrollige üksikasju ja võtke pakkumine vastu

**Müügiprotsess:**

Kui vahetus on algatatud :


   - Saatke oma pangaandmed ostjale
   - Oodake ostja Bitcoini aadressi
   - Kontrollida, et aadress on kehtiv

Pärast makse teatamist :


   - Kontrollida, et makse on teie kontole laekunud
   - Kinnitage, et summa ja üksikasjad vastavad
   - Saatke bitcoinid esitatud aadressile
   - Märgista tehing lõpetatuks

Lõpetamine :


   - Oodake ostja kinnitust
   - Jäta tagasiside tehingu kohta
   - Ehitage oma maine tulevase müügi jaoks

**Tähtis märkus:** Müüjana peate olema eriti tähelepanelik tagasimaksete riski suhtes. Eelistage turvalisi makseviise ja kontrollige alati enne bitcoinide saatmist, et makse on laekunud.

## Head tavad ja ohutus

### Ohutusnõuanded

**Ostjatele:**


- Alustage väikeste kogustega
- Kontrollida müüjate mainet (minimaalne skoor 30,000)
- Kasutage ainult soovitatud makseviise
- Enne makse saatmist kontrollige, et müüja on aktiivne
- Kasutage ainult vahetusvestluses esitatud pangaandmeid
- Mitte kunagi ei tohi suhelda väljaspool Bisq 2 platvormi
- Hoidke maksetõendit
- Ärge kunagi saatke tundlikku teavet

**Müüjatele:**


- Olge uute kontodega ettevaatlik
- Vältige tagasimaksete suhtes tundlikke makseviise (PayPal, Venmo)
- Kontrollida, et konto andmed vastavad ostjale
- Piirake suhtlust vestlusega Bisq 2
- Kahtluse korral avatud vahendamine

### Maine loomine (müügiinimestele)

Selleks, et suurendada oma müüja mainet Bisqis, tehke regulaarselt tehinguid ja suhtle ostjatega professionaalselt. Vastake kiiresti ostjate päringutele, et tagada positiivne kogemus. Võite luua ka BSQ võlakirja, et näidata oma pühendumust platvormile. Need tegevused suurendavad usaldust ja meelitavad rohkem ostjaid.

### Vaidluste lahendamine


- Võtke oma vastaspoolega ühendust chat'i kaudu
- Vajaduse korral avage vaidlus
- Esitage kõik nõutavad tõendid
- Järgige vahendaja juhiseid

### Privaatsuspoliitika :


- Ei nõuta registreerimist ega tsentraliseeritud isikusamasuse kontrollimist
- Kõik ühendused lähevad läbi Tor-võrgu (ja varsti ka I2P)
- Puudub keskne server andmete säilitamiseks
- Tehingu üksikasjad on loetavad ainult asjaosalistele

### Kaitse tsensuuri vastu :


- Täielikult jaotatud P2P-võrk
- Tor-võrgu (ja varsti ka I2P) kasutamine tsensuuri vastu võitlemiseks
- Avatud lähtekoodiga projekt, mida juhib DAO, ilma tsentraliseeritud juriidilise isikuta

## Eelised ja puudused

### Bisq 2 eelised


- Maksimaalne konfidentsiaalsus**: KYC puudub, Tori kasutamine
- Detsentraliseerimine**: Ei mingit keskset serverit
- Turvalisus**: Avatud lähtekoodiga, mittekaitstav kood
- Intuitiivne kasutajaliides**: lihtsam kui Bisq 1
- Paindlikkus**: Mitu vahetusprotokolli

### Bisq 2 puudused


- Piiratud likviidsus** (hetkel) :
 - Uus protokoll käivitamisetapis
 - Vähesed müügipakkumised saadaval
 - Võimalik pikk ooteaeg ostja leidmiseks
- Kauplemislimiidid**: Maksimaalselt 600 USD tehingu kohta (koos Bisq easy'ga)
- Ainult lauaarvuti**: Mobiilirakendus puudub

## Tulevased protokollid

Kuigi Bisq Easy on praegu ainus olemasolev protokoll, on Bisq 2 jaoks väljatöötamisel mitu muud protokolli:


- Bisq Lightning**: Lightning-võrgus mitmepoolset arvutuskrüptograafiat kasutaval deponeerimissüsteemil põhinev vahetusprotokoll.
- Bisq MuSig**: Põhiprotokolli migratsioon Bisq 1-st Bisq 2-sse, kasutades 2-on-2 multisig'i koos tagatisrahaga.
- BSQ vahetus**: Kohene aatomivahetus BSQ ja BTC vahel.
- Likviidsed vahetustehingud**: Varade vahetamine Liquid-võrgus (USDT, BTC-L) aatomiliste vahetustehingute kaudu.
- Monero Swaps**: Aatomivahetused Bitcoini ja Monero vahel.
- Vedelik MuSig**: Multisig-protokolli versioon, mis kasutab L-BTC-d madalamate kulude ja suurema konfidentsiaalsuse tagamiseks.
- Allveelaeva vahetused**: Vahetused Bitcoini vahel Lightning-võrgus ja Bitcoini ahelas.
- Stablecoin Swaps**: Aatomivahetused Bitcoini ja USD stabiilse mündi vahel.
- Multisig Valikud**: P2P müügi- ja ostuoptsioonide loomine koos BTC blokeerimisega ahelasiseses multisig-tehingus.
- Multisig avatud lepingud**: Võimaldab luua kohandatud tingimuslikke lepinguid, kasutades 2-on-3 multisig süsteemi koos arbitraažiga.

Need protokollid on praegu väljatöötamisel ja neid integreeritakse järk-järgult Bisq 2-sse, pakkudes kasutajatele suuremat paindlikkust vastavalt nende erivajadustele.

## Kasulikud ressursid


- Ametlik veebileht: [bisq.network](https://bisq.network)
- Dokumentatsioon: [Bisq Wiki](https://bisq.wiki)
- Toetus: [Forum Bisq](https://bisq.community)
- Allikakood : [GitHub](https://github.com/bisq-network)