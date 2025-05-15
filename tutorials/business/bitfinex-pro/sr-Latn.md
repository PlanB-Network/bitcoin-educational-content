---
name: Bitfinex - Kompanija
description: Kreiranje i upravljanje nalogom kompanije na Bitfinex-u
---
![cover](assets/cover.webp)


Osnovan 2012. godine, Bitfinex je jedna od prvih Bitcoin i Altcoin Exchange platformi. U početku fokusiran na P2P Bitcoin razmene, platforma je brzo proširila svoje usluge kako bi uključila margin trgovanje, P2P finansiranje, trgovanje derivatima i OTC ("*over-the-counter*") tržište za transakcije velikog obima.


Danas je Bitfinex kompletna platforma, koja omogućava kako jednostavne kupovine bitkoina, tako i korišćenje naprednih funkcionalnosti trgovanja (tradicionalno trgovanje, derivati, OTC, pozajmljivanje, itd.) sa alatima za upravljanje rizikom. Dostupna je u veb verziji, a za jednostavne transakcije dostupna je i laka za korišćenje mobilna aplikacija.


U ovom vodiču pokrićemo proces kreiranja poslovnog naloga na Bitfinex-u, kupovinu i prodaju bitcoina, upravljanje transakcijama za računovodstvene svrhe, kao i deponovanje i povlačenje evra i bitcoina. Cilj je da vam pružimo osnovno znanje, bilo da planirate integrisati Bitcoin u vaš novčani tok ili prihvatiti Bitcoin kao sredstvo plaćanja.


Ako ste zainteresovani za temu integracije Bitcoin u vaše poslovanje, preporučio bih vam da otkrijete naš kompletan teorijski kurs obuke na tu temu:


https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a

## 1 - Kreiranje Bitfinex naloga


Idite na [zvaničnu Bitfinex veb stranicu](https://www.bitfinex.com/). Na početnoj stranici pronađite i kliknite na opciju "*Sign Up*" da biste započeli kreiranje svog naloga. Prvo ćete kreirati standardni nalog za pojedince, opcija "*Corporate*" će biti izabrana kasnije tokom procesa verifikacije.


![BITFINEX](assets/fr/01.webp)


Popunite potrebne informacije: unesite svoju poslovnu email adresu Address i zemlju u kojoj je vaša kompanija registrovana. Izaberite sigurno korisničko ime i lozinku, zatim kliknite na "*Sign up*" da potvrdite registraciju.


![BITFINEX](assets/fr/02.webp)


Za savete o korišćenju i zaštiti jakih, jedinstvenih lozinki, pogledajte i ovaj vodič :


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Sada ćemo konfigurisati 2FA da osiguramo nalog. Koristite aplikaciju za autentifikaciju na svom pametnom telefonu, kao što su Google Authenticator ili Authy na primer. Pronaći ćete vodič za ovaj alat ovde :


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Skenirajte QR kod pomoću svoje aplikacije i unesite 6 cifara koje su date.


![BITFINEX](assets/fr/03.webp)


Registracija je završena.


![BITFINEX](assets/fr/04.webp)


Proverite svoj poštanski sandučić i kliknite na link koji je poslao Bitfinex da potvrdite svoju registraciju.


![BITFINEX](assets/fr/05.webp)


Vaš nalog je sada kreiran. Kliknite na "*Prijavi se*" da pristupite platformi.


![BITFINEX](assets/fr/06.webp)


## 2 - Verifikacija naloga kompanije


Bitfinex primenjuje proces verifikacije (KYC) koji je u skladu sa važećim propisima. U "Osnovnom" režimu, nije moguće vršiti depozite, što čini neophodnim dobijanje barem "Srednjeg" nivoa verifikacije, ili čak "Potpunog" ako je potrebno.


Kada vaš nalog bude kreiran, trebalo bi da se pojavi iskačući prozor koji predlaže da verifikujete svoj nalog. Kliknite na "*Verifikuj*".


![BITFINEX](assets/fr/07.webp)


Ako se ovaj prozor ne pojavi, idite na svoj profil u gornjem desnom uglu Interface, zatim kliknite na "*Verification*".


![BITFINEX](assets/fr/08.webp)


Pod "*Account Type*", izaberite "*Corporate*". U mom slučaju, unapređujem na "*Intermediate*", tako da biram "*Upgrade to Intermediate*".


![BITFINEX](assets/fr/09.webp)


Dovršite korake pružanjem:




- Informacije o kompaniji (naziv kompanije, kontakt podaci, poslovni sektor, itd.);
- Pravni dokumenti (osnivački akt, izvod iz Kbis-a, spisak direktora i akcionara);
- KYC informacije za svakog stvarnog vlasnika ili direktora (identifikacioni dokumenti, dokaz o Address, itd.).


Kada vaša prijava bude završena i poslata, može proći nekoliko dana da platforma izvrši validaciju za poslovnu verifikaciju. Tokom ovog perioda, depoziti će biti privremeno blokirani.


![BITFINEX](assets/fr/10.webp)


## 3 - Brzi uvod u Bitfinex Interface


Kada se prijavite, videćete navigacionu traku na vrhu Interface sa: "*Trading*", "*Derivatives*", "*Funding*", "*OTC*", "*P2P*", "*Wallet*", itd. Bitfinex nudi širok spektar funkcionalnosti, uključujući :




- Trgovanje**: "*klasično*" tržište gde možete postavljati naloge za kupovinu i prodaju kriptovaluta (uključujući Bitcoin) ;
- OTC**: Over-The-Counter usluga za trgovanje velikim količinama direktno sa drugim igračem, van javnih knjiga naloga;
- Finansiranje**: Oblast posvećena pozajmljivanju i maržinskom finansiranju;
- Derivatives**: Sekcija za derivate (fjučersi, itd.), namenjena iskusnim trgovcima;
- P2P**: Omogućava vam kupovinu ili prodaju kriptovaluta od drugih korisnika na peer-to-peer osnovi.


Za standardnu upotrebu (kupovina/prodaja bitkoina, depoziti/isplate i upravljanje gotovinom), uglavnom ćete koristiti karticu "*Trading*", kao i odeljke "*Wallet*", "*Deposit*" i "*Withdraw*".


![BITFINEX](assets/fr/11.webp)


Još jedna prednost korporativne formule je mogućnost kreiranja podračuna. To znači da možete omogućiti pristup ovim podračunima za više korisnika, svaki sa specifičnim pravima (samo za čitanje, trgovanje, samo za depozit, itd.).


## 4 - Depozit i povlačenje evra (fiat)


Da biste položili eure na svoj Bitfinex korporativni račun, pristupite podmeniju "*Deposit*" koji se nalazi u meniju "*Wallet*" na vrhu Interface.


![BITFINEX](assets/fr/12.webp)


Odaberite "*Bank transfer*" ili "*Credit/Debit Card*" za uplatu u evrima (ili bilo kojoj drugoj fiat valuti).


![BITFINEX](assets/fr/13.webp)


Izaberite fiat valutu za slanje, npr. euro. Ako koristite samo osnovne funkcije "*Trading*", kliknite na "*Exchange*". Takođe navedite iznos koji želite da položite i zemlju banke vašeg poslovnog računa.


![BITFINEX](assets/fr/14.webp)


Izvršite transfer sa vašeg poslovnog bankovnog računa na bankovni račun koji je naznačio Bitfinex.


Da biste povukli sredstva, procedura je slična: idite na podmeni "*Withdraw*".


![BITFINEX](assets/fr/15.webp)


Kliknite na "*Bankovni transfer*".


![BITFINEX](assets/fr/16.webp)


Odaberite fiat valutu koju želite povući, račun koji će biti terećen na Bitfinex-u ("*Exchange*" ako koristite samo osnovne funkcije) i iznos koji želite povući.


![BITFINEX](assets/fr/17.webp)


Bitfinex može zahtevati validaciju vašeg bankovnog računa pre nego što prihvati transfer, iz razloga usklađenosti.


![BITFINEX](assets/fr/18.webp)


Jednom kada je procedura pokrenuta, Bitfinex će prebaciti sredstva na vaš bankovni račun.


## 5 - Polaganje i povlačenje bitkoina


Da biste deponovali Bitcoin na Bitfinex, pristupite podmeniju "*Deposit*".


![BITFINEX](assets/fr/19.webp)


Kliknite na "*Cryptocurrency*".


![BITFINEX](assets/fr/13.webp)


Odaberite "*BTC*". Pojaviće se prijemni Address. Kopirajte ovaj Address i koristite ga sa svog samostalnog čuvanja Wallet ili druge platforme za slanje vašeg BTC.


![BITFINEX](assets/fr/20.webp)


Da biste povukli Bitcoin, idite na podmeni "*Withdraw*".


![BITFINEX](assets/fr/21.webp)


Kliknite na "*Cryptocurrency*".


![BITFINEX](assets/fr/22.webp)


Odaberite "*BTC*". Izaberite Bitfinex nalog koji će biti terećen za vašu isplatu ("*Exchange*" za osnovne funkcije). Unesite iznos i odredište Address za bitkoine. Obavezno proverite isplatu Address kako biste sprečili bilo kakve greške.


![BITFINEX](assets/fr/23.webp)


Nakon vaše potvrde, vaši bitkoini će biti prebačeni. Imajte na umu da naknade i kašnjenja mogu varirati u zavisnosti od zagušenja Mempool.


Bitfinex takođe nudi opcije depozita i povlačenja putem Lightning Network, omogućavajući brže i jeftinije transakcije.


![BITFINEX](assets/fr/24.webp)


Ako ste zainteresovani za Lightning Network, imamo i kompletan kurs obuke koji će vam pomoći da razumete kako funkcioniše:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

## 6 - Kupovina i prodaja bitkoina na Bitfinex-u


Bitfinex nudi različite režime trgovanja. Za jednostavnost korišćenja, izaberite klasično spot tržište, poznato i kao "*Trading*" ili "*Exchange*". Ovde možete postaviti naloge za kupovinu ili prodaju po tržišnoj ceni, ili postaviti limitiranu cenu.


U gornjem meniju kliknite na "*Trading*".


![BITFINEX](assets/fr/25.webp)


Odaberite par "*BTC/EUR*" ako želite kupiti ili prodati BTC u Exchange za evre, na primer.


![BITFINEX](assets/fr/26.webp)


Interface prikazuje grafikon cena u centru, knjigu naloga na dnu i modul za unos naloga sa leve strane. U sekciji za unos naloga, možete birati između "*Market*" naloga (izvršava se odmah po najboljoj dostupnoj ceni) ili "*Limit*" naloga (vi definišete cenu). Naznačite količinu BTC za kupovinu ili prodaju, ili izaberite procenat vašeg balansa. Zatim kliknite na "*Buy*" za kupovinu ili "*Sell*" za prodaju.


![BITFINEX](assets/fr/27.webp)


Istoriju izvršenih naloga možete pogledati u donjem delu Interface.


![BITFINEX](assets/fr/28.webp)


## 7 - Izvoz istorije transakcija i računovodstvo


Za potrebe računovodstva, trebaće da izvezete detalje vaših transakcija (kupovine, prodaje, depoziti, isplate). Bitfinex nudi sveobuhvatan alat za izveštavanje. Kliknite na ikonu vašeg profila u gornjem desnom uglu Interface, zatim na meni "*Reports*".


![BITFINEX](assets/fr/29.webp)


Sa leve strane možete izabrati tip podataka za izvoz. Na primer, izborom "*Trades*" dobićete pristup svim vašim trgovinama.


![BITFINEX](assets/fr/30.webp)


Definišite željeni period u polju "*Date*" i, ako je potrebno, ograničite pretragu na jedan ili više specifičnih parova putem polja "*Symbol*".


![BITFINEX](assets/fr/31.webp)


Da biste izvezli ove podatke, kliknite na dugme "*Export*".


![BITFINEX](assets/fr/32.webp)


Proverite parametre, zatim potvrdite izvoz.


![BITFINEX](assets/fr/33.webp)


Izveštaj će biti poslat na email Address povezan sa vašim Bitfinex nalogom, kao CSV fajl.


![BITFINEX](assets/fr/34.webp)


Kada je datoteka izvezena, možete je integrisati u vaš računovodstveni softver ili poslati vašem ovlašćenom računovođi.


## 9 - Upotreba slučajeva za kompaniju


U zavisnosti od ciljeva i strukture vaše kompanije, korišćenje Bitfinex-a može varirati.


### Kupovina bitkoina za gotovinu


**Cilj:** Diversifikovati tok gotovine kompanije ulaganjem u Bitcoin.


**Koraci koje treba pratiti:**




- Depozitujte eure na Bitfinex sa bankovnog računa kompanije;
- Iskoristi ove eure da kupiš Bitcoin;
- Čuvajte bitkoine na platformi ili ih povucite kako biste ih osigurali u samostalnom čuvanju ;
- Izvezite istorije transakcija po potrebi.


### Prihvatanje Bitcoin kao sredstva plaćanja


**Cilj:** Ponudite svojoj kompaniji mogućnost prihvatanja Bitcoin kao sredstva plaćanja za vaše proizvode ili usluge.


**Koraci koje treba pratiti:**




- Integrirajte Bitcoin sistem plaćanja. Za mala preduzeća, jednostavan Wallet softver može biti dovoljan, ili možete odabrati specijalizovana rešenja kao što su Swiss Bitcoin Pay ili BTCPay Server da integrišete Bitcoin kao opciju plaćanja na vašem sajtu ili na prodajnom mestu;
- Prenosi uplate primljene u bitkoinima na vaš Bitfinex nalog;
- U zavisnosti od vaše finansijske strategije, prodate bitkoine primljene za eure, zadržite ih za potencijalno buduće povećanje vrednosti, ili se odlučite za kombinaciju oba;
- Čuvajte bitkoine na platformi ili ih povucite za samostalno čuvanje. Takođe možete povući eure na svoj bankovni račun;
- Izvezite istorije transakcija po potrebi.


Za detaljniji uvid u ovu temu, preporučujem ovaj sveobuhvatni kurs obuke o integraciji Bitcoin u poslovanje, koji detaljno pokriva dodavanje u tok gotovine, prihvatanje Bitcoin uplata i računovodstvo :


https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a