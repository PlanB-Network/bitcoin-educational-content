---
name: Bisq 2
description: Potpuni vodič za korišćenje Bisq 2 i razmenu bitkoina P2P
---
![cover](assets/cover.webp)


## Uvod


Peer-to-peer razmene bez KYC (P2P) su ključne za očuvanje poverljivosti korisnika i finansijske autonomije. Omogućavaju direktne transakcije između pojedinaca bez potrebe za verifikacijom identiteta, što je od suštinskog značaja za one koji cene privatnost. Za dublje razumevanje teorijskih koncepata, pogledajte kurs BTC204:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Šta je Bisq 2?


Bisq 2 je nova verzija popularnog decentralizovanog Bisq Exchange, lansirana 2024. Za razliku od svog prethodnika, Bisq 2 je razvijen da podržava više Exchange protokola, nudeći korisnicima veću fleksibilnost.


**Ključne nove funkcije:**




- Podrška za više mreža privatnosti (Tor, I2P)
- Višestruki identiteti za veću poverljivost
- REST API za trgovačke botove
- Podrška za više tipova Wallet
- Sistem uloga sa obaveznim depozitom u BSQ


Ovaj vodič se fokusira isključivo na "Bisq Easy", jedini trenutno dostupni protokol. Bisq Easy je dizajniran posebno za nove korisnike Bitcoin. Ovaj protokol omogućava korisnicima da kupuju i prodaju Bitcoine u zamenu za fiat valute na decentralizovanoj peer-to-peer platformi. Transakcije su ograničene na ekvivalent od 600 USD (sa minimumom od 6 USD), a sigurnost Exchange se oslanja na reputaciju prodavaca BTC-a. Bisq Easy nema naknade za trgovanje niti zahteve za sigurnosni depozit. Očekuje se da će Bisq Easy zameniti Bisq 1 za gotovinske razmene ispod 600 USD (ili ekvivalent).


**Glavne karakteristike:**




- Desktop aplikacija za više platformi
- Nekoliko Exchange protokola dostupno
- Decentralizovana P2P mreža
- Fokus na poverljivost (bez KYC, korišćenje Tor-a)
- Nekustodijalni (zadržavate kontrolu nad svojim sredstvima)
- Otvoreni kod (AGPL)


### Razlike sa Bisq 1


**Za kupce:**




- Nije potreban sigurnosni depozit
- Bez naknada za trgovanje
- Nema Mining naknada
- Bezbednost zasnovana na reputaciji dobavljača
- Niži limiti trgovanja (ekvivalentno 600 USD)


**Za prodavce:**




- Nije potreban sigurnosni depozit
- Izgradnja reputacije
- Mogućnost spaljivanja BSQ ili kreiranja BSQ obveznica
- Potencijalno veća prodajna premija (10-15% iznad tržišta)


**Važna napomena:** Kada se Bisq Multisig protokol implementira u Bisq 2, stara verzija Bisq-a može biti ukinuta. Međutim, Bisq 1 će se i dalje koristiti kao alat za upravljanje Bisq CAD-om i za BSQ-BTC razmene.


### Exchange proces




- Kreator ponude definiše uslove Exchange
- Jednom kada se trgovci dogovore o uslovima (način plaćanja i cena), Exchange počinje
- Prodavac šalje svoje bankovne podatke kupcu, a kupac šalje svoj Bitcoin Address prodavcu.
- Kupac vrši uplatu u gotovini i obaveštava prodavca
- Jednom kada uplata bude primljena, prodavac šalje bitkoine kupcu na Address
- Exchange je završen kada kupac primi bitkoine


### Važne pravila




- Pre nego što razmenite podatke o plaćanju, Exchange može biti otkazan bez opravdanja
- Nakon što su detalji razmenjeni, neispunjavanje obaveza može rezultirati proterivanjem.
- Za bankovne transfere, **nikada ne koristite termine "Bisq" ili "Bitcoin"** u razlogu plaćanja (ovo može dovesti do zamrzavanja sredstava ili čak do blokiranja bankovnog računa primaoca ili platioca)
- Trgovci moraju da se prijave bar jednom dnevno kako bi pratili proces
- U slučaju problema, trgovci mogu pozvati usluge medijatora.


## Instalacija i konfiguracija


### 1. Preuzmi i Verifikuj Bisq 2


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Idi na [bisq.network](https://bisq.network/downloads/)
- Preuzmite Bisq 2 verziju koja odgovara vašem operativnom sistemu (pomaknite se niz stranicu)
- Proverite autentičnost preuzete datoteke (preporučuje se). Za detaljan vodič o verifikaciji potpisa, pogledajte sledeći tutorijal:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Instalacija prema vašem sistemu


Molimo vas da pratite korake instalacije odgovarajuće za vaš operativni sistem. Ako naiđete na bilo kakve poteškoće tokom instalacije, možete se posavetovati sa detaljnim vodičem na [zvaničnoj Bisq wiki stranici](https://bisq.wiki/Downloading_and_installing).


### 3. Prvo pokretanje




- Pokreni Bisq 2 i prihvati uslove korišćenja


![Conditions d'utilisation](assets/fr/01.webp)




- Kreirajte novi profil odabirom imena i avatara


![Création du profil](assets/fr/02.webp)




- Zatim ćete biti prebačeni na glavnu kontrolnu tablu aplikacije, gde možete pokrenuti Bisq Easy za kupovinu ili prodaju svojih prvih bitkoina.


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. Postavljanje metoda plaćanja




- Pristupite odeljku za platne račune iz glavnog menija


![Liste des comptes de paiement](assets/fr/04.webp)




- Dodajte novi način plaćanja popunjavanjem potrebnih informacija


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


Pre-konfigurisanje metoda plaćanja je opcionalno, ali se preporučuje kako bi se uštedelo vreme prilikom trgovanja. Takođe možete konfigurisati svoje metode plaćanja direktno tokom trgovine kontaktiranjem vašeg Exchange partnera.


### 5. Bezbednost naloga


**Bekap podataka:**


Za razliku od Bisq 1, Bisq 2 trenutno ne integriše Bitcoin Wallet: transakcije se stoga obavljaju putem vaših sopstvenih eksternih novčanika. Ipak, preporučujemo da redovno pravite rezervne kopije vašeg Bisq 2 direktorijuma sa podacima. Da biste pronašli vaš direktorijum sa podacima, pogledajte [zvaničnu Bisq wiki stranicu](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).


**Upravljanje identitetom:**


Bisq 2 vam omogućava kreiranje više identiteta. Svaki identitet se može koristiti za različite tipove transakcija. Vaši identiteti su sačuvani u fascikli sa podacima.


## Kupovina i prodaja Bitcoina


### Kako kupiti Bitkoine


**Opcija 1: Iskoristite postojeću ponudu**




- Na glavnom ekranu, izaberite "Bisq Easy", karticu "Getting started", zatim kliknite na "Start trade wizard"


![Lancer trade wizard](assets/fr/06.webp)




- Izaberite "Kupi Bitcoin" i odaberite svoju valutu


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- Postavite svoje preferirane metode plaćanja (SEPA, Revolut, itd.)


![Configuration méthodes de paiement](assets/fr/09.webp)




- U ovom trenutku, ili imate listu ponuda koja odgovara vašim prethodnim kriterijumima, ili treba da odete na "Offerbook"


![Liste des offres](assets/fr/10.webp)




- U drugom slučaju, možete prikazati i filtrirati ponude koristeći dugmad u gornjem desnom uglu Interface.


![Filtres des offres](assets/fr/11.webp)




- Jednom kada odaberete svoju ponudu, sve što treba da uradite je da izaberete način plaćanja, a zatim potvrdite rezime trgovine.


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**Opcija 2: Kreiraj svoju ponudu**




- Odaberite "Bisq Easy" zatim "Offerbook"
- Izaberite svoj trgovački par (npr. BTC/EUR)
- Kliknite na "Create offer
- Pratite čarobnjaka za kreiranje ponude: Definišite iznos (fiksni ili raspon)


![Configuration du montant](assets/fr/20.webp)




- Odaberite prihvaćene metode plaćanja


![Sélection méthodes de paiement](assets/fr/21.webp)




  - Proverite rezime i objavite ponudu


![Récapitulatif et publication](assets/fr/22.webp)


Jednom kada je Exchange pokrenut :




- Pošaljite svoj Bitcoin Address ili Lightning Invoice prodavcu


![Envoi adresse Bitcoin](assets/fr/15.webp)




- Primite podatke o banci prodavca


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- Izvršite uplatu (bez pominjanja "Bisq" ili "Bitcoin")
- Obavesti prodavca o tvojoj uplati


![Notification paiement](assets/fr/18.webp)




- Sačekajte da bitkoini stignu


![Attente réception](assets/fr/19.webp)


### Kako prodati Bitkoine?


Proces prodaje na Bisq 2 prati sličnu logiku kao i kupovina, sa istim glavnim koracima, ali obrnutim redosledom. Možete ili kreirati svoju ponudu za prodaju, ili odgovoriti na postojeću ponudu za kupovinu. Evo pregleda različitih opcija i faza u procesu:


**Opcija 1: Kreiraj ponudu za prodaju**




- Odaberite "Bisq Easy" zatim "Offerbook"
- Kliknite na "Create offer" i izaberite "Sell Bitcoin"
- Konfigurišite svoju ponudu :
 - Odaberite valutu (EUR, USD, itd.)
 - Izaberite prihvaćene metode plaćanja
 - Postavite iznos (između 6 i 600 USD ekvivalenta)
 - Postavite svoju cenu (fiksnu ili % od tržišta)
- Proverite detalje i objavite ponudu


**Opcija 2: Prihvatite postojeću ponudu**




- Pregledajte ponude u kartici "Offerbook"
- Filtriraj po valuti i načinu plaćanja
- Odaberite ponudu koja vam odgovara
- Proverite detalje i prihvatite ponudu


**Proces prodaje:**


Jednom kada je Exchange pokrenut :




   - Pošaljite svoje bankovne podatke kupcu
   - Sačekajte Bitcoin Address kupca
   - Proveri da li je Address važeći


Nakon obaveštenja o uplati :




   - Proverite da li je uplata primljena na vaš račun
   - Potvrdite da se iznos i detalji podudaraju
   - Pošalji bitkoine na dati Address
   - Označi transakciju kao završenu


Finalizacija :




   - Sačekajte potvrdu od kupca
   - Ostavite povratne informacije o transakciji
   - Izgradite svoj ugled za buduću prodaju


**Važna napomena:** Kao prodavac, morate biti posebno oprezni zbog rizika od povraćaja sredstava. Dajte prednost sigurnim metodama plaćanja i uvek proverite da li je uplata primljena pre nego što pošaljete bitkoine.


## Dobre prakse i bezbednost


### Saveti za bezbednost


**Za kupce:**




- Počnite sa malim količinama
- Proverite reputaciju prodavaca (minimalni skor od 30.000)
- Koristite samo predložene metode plaćanja
- Proverite da li je prodavac aktivan pre nego što pošaljete uplatu
- Koristite samo bankovne podatke navedene u Exchange ćaskanju.
- Nikada ne komunicirajte van platforme Bisq 2
- Sačuvajte dokaz o uplati
- Nikada ne šaljite osetljive informacije


**Za prodavce:**




- Budite oprezni sa novim nalozima
- Izbegavajte metode plaćanja osetljive na povraćaj sredstava (PayPal, Venmo)
- Proverite da li podaci o računu odgovaraju kupcu
- Ograniči komunikaciju na chat Bisq 2
- Otvorite medijaciju u slučaju sumnje


### Izgradnja reputacije (za prodavce)


Da biste poboljšali svoju reputaciju na Bisq-u kao prodavac, redovno obavljajte transakcije i održavajte profesionalnu komunikaciju sa kupcima. Brzo odgovarajte na zahteve kupaca kako biste osigurali pozitivno iskustvo. Takođe možete kreirati BSQ obveznicu da pokažete svoj Commitment platformi. Ove akcije će izgraditi poverenje i privući više kupaca.


### Rešavanje sporova




- Kontaktirajte svog kolegu putem četa
- Ako je potrebno, otvorite spor
- Obezbedite sve tražene dokaze
- Pratite instrukcije medijatora


### Politika privatnosti :




- Nije potrebna registracija ili centralizovana verifikacija identiteta
- Sve veze idu kroz Tor mrežu (a uskoro i I2P)
- Nema centralnog servera za čuvanje podataka
- Detalji transakcije su čitljivi samo za uključene strane


### Zaštita od cenzure :




- Potpuno distribuirana P2P mreža
- Korišćenje Tor mreže (a uskoro i I2P) za otpor cenzuri
- Open source projekat kojim upravlja DAO, bez centralizovane pravne entiteta


## Prednosti i nedostaci


### Prednosti Bisq 2




- Maksimalna poverljivost**: Nema KYC, korišćenje Tor-a
- Decentralizacija**: Nema centralnog servera
- Sigurnost**: Otvoreni kod, nekustodijalni kod
- Intuitivni Interface**: jednostavniji od Bisq 1
- Fleksibilnost**: Više Exchange protokola


### Bisq 2 nedostaci




- Ograničena likvidnost** (za sada) :
 - Novi protokol u fazi pokretanja
 - Nekoliko prodajnih ponuda dostupno
 - Potencijalno dugo čekanje na pronalaženje kupca
- Ograničenja trgovanja**: Maksimalno 600 USD po transakciji (sa Bisq easy)
- Samo za desktop**: Nema mobilne aplikacije


## Budući Protokoli


Iako je Bisq Easy trenutno jedini dostupni protokol, nekoliko drugih protokola je u razvoju za Bisq 2 :




- Bisq Lightning**: Exchange protokol zasnovan na escrow sistemu koristeći kriptografiju višestranačke računarske obrade na Lightning Network.
- Bisq MuSig**: Migracija glavnog protokola sa Bisq 1 na Bisq 2, koristeći 2-na-2 Multisig sa sigurnosnim depozitima.
- BSQ Swaps**: Instantni atomski svopovi između BSQ i BTC.
- Liquid Swaps**: Exchange od sredstava na Liquid Network (USDT, BTC-L) putem atomskih zamena.
- Monero Swaps**: Atomske razmene između Bitcoin i Monera.
- Liquid MuSig**: Verzija Multisig protokola koja koristi L-BTC za niže troškove i veću poverljivost.
- Zamene podmornica**: Razmene između Bitcoin na Lightning Network i Bitcoin On-Chain.
- Stablecoin Swaps**: Atomske razmene između Bitcoin i USD stablecoina.
- Multisig Opcije**: Kreiranje P2P put i call opcija sa BTC blokiranjem u On-Chain Multisig transakciji.
- Multisig Open Contracts**: Omogućava kreiranje prilagođenih uslovnih ugovora koristeći 2-na-3 Multisig sistem sa arbitražom.


Ovi protokoli su trenutno u fazi razvoja i biće postepeno integrisani u Bisq 2, nudeći veću fleksibilnost korisnicima u skladu sa njihovim specifičnim potrebama.


## Korisni resursi




- Zvanična veb stranica: [bisq.network](https://bisq.network)
- Dokumentacija: [Bisq Wiki](https://bisq.wiki)
- Podrška: [Forum Bisq](https://bisq.community)
- Izvorni kod : [GitHub](https://github.com/bisq-network)