---
name: Blockstream Green - 2FA
description: Postavljanje 2/2 Multisig na Green Wallet
---
![cover](assets/cover.webp)

___

***Napomena:** Od maja 2025. godine neće biti moguće aktivirati nove naloge zaštićene dvofaktorskom autentifikacijom (2FA). Ova funkcija je dostupna samo korisnicima koji su prethodno aktivirali ovu vrstu naloga.*

___

Software Wallet je aplikacija instalirana na računaru, pametnom telefonu ili drugom uređaju povezanom na Internet, koja vam omogućava upravljanje i zaštitu vaših Bitcoin Wallet ključeva. Za razliku od hardverskih novčanika, koji izoluju privatne ključeve, "Hot" novčanici stoga rade u okruženju potencijalno izloženom sajber napadima, povećavajući rizik od piraterije i krađe.

Softverski novčanici treba da se koriste za upravljanje razumnim količinama bitkoina, posebno za svakodnevne transakcije. Oni takođe mogu biti zanimljiva opcija za ljude sa ograničenim Bitcoin sredstvima, za koje ulaganje u Hardware Wallet može delovati nesrazmerno. Međutim, njihova stalna izloženost internetu čini ih manje sigurnim za čuvanje dugoročnih ušteđevina ili velikih fondova. Za ovo drugo, najbolje je odlučiti se za sigurnija rešenja, kao što su hardverski novčanici.

U ovom vodiču, pokazaću vam kako da poboljšate sigurnost Hot Wallet koristeći opciju "*2FA*" na Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Predstavljamo Blockstream Green


Blockstream Green je Software Wallet dostupan na mobilnim uređajima i desktopu. Ranije poznat kao *Green Address*, ovaj Wallet je postao Blockstream projekat nakon akvizicije 2016. godine.


Green je posebno jednostavna aplikacija za korišćenje, što je čini zanimljivom za početnike. Nudi sve osnovne funkcije dobrog Bitcoin Wallet, uključujući RBF (*Replace-by-fee*), opciju povezivanja sa Tor mrežom, mogućnost povezivanja sopstvenog čvora, SPV (*Simple Payment Verification*), označavanje i kontrolu novčića.


Blockstream Green takođe podržava Liquid Network, Bitcoin Sidechain razvijen od strane Blockstream-a za brzo, Confidential Transactions izvan glavnog Blockchain. U ovom vodiču, fokusiramo se isključivo na Bitcoin, ali sam takođe napravio još jedan vodič da naučite kako koristiti Liquid na Green :


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig opcija (2FA)


Na Green, možete kreirati klasični "*singlesig*" Hot Wallet. Ali takođe imate opciju "*2FA Multisig*", koja poboljšava sigurnost vašeg Hot Wallet bez prekomplikovanja njegovog svakodnevnog upravljanja.


Dakle, postavićete 2/2 Multisig Wallet, što znači da će svaka transakcija zahtevati potpisivanje sa dva ključa. Prvi ključ, izveden iz vaše 12- ili 24-reči Mnemonic fraze, je lokalno zaštićen PIN kodom na vašem telefonu. Imate potpunu kontrolu nad ovim ključem. Drugi ključ drže Blockstream serveri i za njegovo korišćenje u potpisivanju je potrebna autentifikacija, koja se može postići putem koda primljenog putem emaila, SMS-a, telefonskog poziva, ili, kao što ćemo videti u ovom vodiču, putem aplikacije za autentifikaciju (Authy, Google Authenticator, itd.).


Da biste osigurali svoju autonomiju u slučaju neuspeha Blockstream-a (na primer, u slučaju bankrota kompanije ili uništenja servera koji drže drugi ključ), na vaš Multisig se primenjuje mehanizam vremenskog zaključavanja. Ovaj mehanizam transformiše 2/2 Multisig u 1/2 Multisig nakon otprilike godinu dana (ili tačno 51,840 blokova, ali ova vrednost je promenljiva), nakon čega će vašem Wallet biti potreban samo vaš lokalni ključ za trošenje bitkoina. Dakle, ako izgubite pristup Blockstream serverima ili 2FA autentifikaciji, samo treba da sačekate najviše godinu dana da biste mogli slobodno koristiti svoje bitkoine sa svojom aplikacijom, bez zavisnosti od Blockstream-a.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Ovaj metod značajno povećava sigurnost vašeg Hot Wallet, dok vam ostavlja kontrolu nad vašim bitcoinima i olakšava njihovu svakodnevnu upotrebu. Međutim, zahteva redovno osvežavanje vremenskog zaključavanja kako bi se održala sigurnost 2FA. Odbrojavanje od 360 dana, tokom kojeg su vaša sredstva zaštićena 2FA, počinje čim primite bitcoine. Ako, 360 dana nakon ovog prijema, niste izvršili transakciju trošenja ovih sredstava, vaši bitcoini će biti zaštićeni samo vašim lokalnim ključem, bez 2FA.


Ovo ograničenje čini opciju 2FA pogodnijom za potrošnju Wallet, gde redovne transakcije automatski obnavljaju vremenske brave. Za dugoročne uštede Wallet, ovo može biti problematično, jer ćete morati razmišljati o tome da svake godine izvršite transakciju na svoj račun pre nego što vremenska brava istekne.


Još jedan nedostatak ove sigurnosne metode je što ćete morati koristiti manjinske skripte. To znači da, sa stanovišta poverljivosti, stvari postaju složenije: vrlo malo ljudi koristi isti tip skripte kao vi, što olakšava spoljnjem posmatraču da identifikuje vaš Wallet otisak. Štaviše, ove skripte će prouzrokovati veće troškove transakcija zbog njihove veće veličine.


Ako ne želite da koristite opciju 2FA i jednostavno želite da postavite "*singlesig*" Wallet na Green, pozivam vas da pogledate ovaj drugi vodič:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Instaliranje i konfiguracija Blockstream Green softvera


Prvi korak je naravno preuzimanje aplikacije Green. Idite u svoju prodavnicu aplikacija:



- [Za Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Za Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


Za korisnike Androida, aplikaciju možete instalirati i putem `.apk` fajla [dostupnog na Blockstream-ovom GitHub-u](https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Pokrenite aplikaciju, a zatim označite polje "Prihvatam uslove...*".


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Kada prvi put otvorite Green, početni ekran se pojavljuje bez konfigurisanog Wallet. Kasnije, ako kreirate ili uvezete novčanike, oni će se pojaviti u ovom Interface. Pre nego što pređete na kreiranje Wallet, savetujem vam da prilagodite postavke aplikacije prema vašim potrebama. Kliknite na "Postavke aplikacije".


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Opcija "*Poboljšana privatnost*", dostupna samo na Androidu, poboljšava privatnost onemogućavanjem snimaka ekrana i skrivanjem pregleda aplikacija. Takođe automatski zaključava pristup aplikaciji čim je vaš telefon zaključan, čineći vaše podatke težim za izlaganje.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


Za one koji žele poboljšati svoju privatnost, aplikacija nudi opciju preusmeravanja vašeg saobraćaja putem Tor-a, mreže koja šifrira sve vaše veze i otežava praćenje vaših aktivnosti. Iako ova opcija može malo usporiti rad aplikacije, toplo se preporučuje za zaštitu vaše privatnosti, posebno ako ne koristite svoj sopstveni kompletan čvor.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Za korisnike koji imaju svoj sopstveni kompletan čvor, Green Wallet nudi mogućnost povezivanja putem Electrum servera, garantujući potpunu kontrolu nad informacijama Bitcoin mreže i distribucijom transakcija.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


Još jedna alternativna funkcija je opcija "*SPV Verification*", koja vam omogućava da direktno verifikujete određene Blockchain podatke i tako smanjite potrebu za poverenjem u podrazumevani čvor Blockstream-a, iako ova metoda ne pruža sve garancije Full node.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


Kada prilagodite ova podešavanja svojim potrebama, kliknite na dugme "*Save*" i ponovo pokrenite aplikaciju.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Kreiraj Bitcoin Wallet na Blockstream Green


Sada ste spremni da kreirate Bitcoin Wallet. Kliknite na dugme "*Get Started*".


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Možete birati između kreiranja lokalnog Software Wallet ili upravljanja Cold Wallet putem Hardware Wallet. Za ovaj vodič, fokusiraćemo se na kreiranje Hot Wallet, tako da ćete morati odabrati opciju "*On This Device*".


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Zatim možete izabrati da obnovite postojeći Bitcoin Wallet ili da kreirate novi. Za potrebe ovog tutorijala, kreiraćemo novi Wallet. Međutim, ako treba da regenerišete postojeći Bitcoin Wallet iz njegove Mnemonic fraze, na primer nakon gubitka starog telefona, moraćete da izaberete drugu opciju.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Zatim možete izabrati između 12-reči ili 24-reči Mnemonic fraze. Ova fraza će vam omogućiti da povratite pristup vašem Wallet sa bilo kog kompatibilnog softvera u slučaju problema sa vašim telefonom. Trenutno, izbor 24-reči fraze ne nudi više sigurnosti od 12-reči fraze. Stoga preporučujem da izaberete 12-reči Mnemonic frazu.


Green će vam zatim pružiti vašu Mnemonic frazu. Pre nego što nastavite, uverite se da vas niko ne posmatra. Kliknite na "*Prikaži frazu za oporavak*" da biste je prikazali na ekranu.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima**. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem telefonu (podložno isteklom vremenskom zaključavanju ili 2FA u slučaju 2/2 Wallet na Green).


Omogućava vam da povratite pristup vašim lokalnim ključevima u slučaju gubitka, krađe ili loma vašeg telefona. Zato je veoma važno da ih pažljivo napravite rezervnu kopiju **na fizičkom mediju (ne digitalnom)** i čuvate je na sigurnom mestu. Možete ih zapisati na parče papira, ili za dodatnu sigurnost, ako je u pitanju veliki Wallet, preporučujem graviranje na nosač od nerđajućeg čelika kako biste ga zaštitili od rizika od požara, poplave ili urušavanja (za Hot Wallet dizajniran da osigura malu količinu bitkoina, jednostavna papirna kopija verovatno je dovoljna).


*Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom vodiču. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Kada pravilno zabeležite svoju Mnemonic frazu na fizički medij, kliknite na "*Nastavi*". Green Wallet će vas zatim zamoliti da potvrdite neke od reči u vašoj Mnemonic frazi kako bi se osiguralo da ste ih ispravno zabeležili. Popunite praznine nedostajućim rečima.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Izaberite PIN kod svog uređaja, koji će se koristiti za otključavanje vašeg Green Wallet. Ovo je vaša zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše Mnemonic fraze od 12 ili 24 reči omogućiće vam da povratite pristup vašim lokalnim ključevima.


Preporučujemo da izaberete 6-cifreni PIN kod koji je što je moguće nasumičniji. Obavezno sačuvajte ovaj kod kako ga ne biste zaboravili, inače ćete biti primorani da preuzmete svoj Wallet sa Mnemonic. Zatim možete dodati opciju biometrijske blokade kako ne biste morali unositi PIN svaki put kada ga koristite. Generalno govoreći, biometrija je daleko manje sigurna od samog PIN-a. Dakle, po defaultu, savetujem vam da ne postavljate ovu opciju otključavanja.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Unesite svoj PIN drugi put da ga potvrdite.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Sačekajte da vaš Wallet bude kreiran, zatim kliknite na dugme "*Create an account*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Zatim možete birati između standardnog Wallet sa jednim potpisom ili Wallet zaštićenog dvofaktorskom autentifikacijom (2FA). U ovom uputstvu, izabraćemo drugu opciju.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Vaš Bitcoin Multisig Wallet je sada kreiran korišćenjem Green aplikacije!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## Podešavanje 2FA


Kliknite na svoj nalog.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


Kliknite na dugme Green "*Povećajte sigurnost svog naloga dodavanjem 2FA*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Zatim ćete moći da izaberete metod autentifikacije za pristup drugom ključu vašeg 2/2 Multisig. Za ovaj vodič, koristićemo aplikaciju za autentifikaciju. Ako niste upoznati sa ovom vrstom aplikacije, preporučujem da pogledate naš vodič o Authy:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Odaberite "*Authenticator Application*".


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green će zatim prikazati QR kod i ključ za oporavak. Ovaj ključ vam omogućava da povratite pristup vašem 2FA u slučaju gubitka vaše Authy aplikacije. Preporučljivo je napraviti sigurnosnu kopiju ovog ključa, iako i dalje možete povratiti pristup vašim bitcoinima nakon što istekne vremenska brava, kao što je objašnjeno gore.


U vašoj aplikaciji za autentifikaciju, dodajte novi kod, a zatim skenirajte QR kod koji je obezbedio Green.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Očigledno, nikada ne smete deliti ovaj ključ i QR kod na Internetu, kao što ja radim u ovom vodiču. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.*


Kliknite na dugme "*Continue*".


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Unesite 6-cifreni dinamički kod prisutan u vašoj aplikaciji za autentifikaciju.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


Dvofaktorska autentifikacija je sada omogućena.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Pregledom ovog menija možete takođe postaviti trajanje vremenske brave. Odbrojavanje počinje čim bitkoini budu primljeni, a kada vremenska brava istekne, vaša sredstva mogu biti potrošena samo sa vašim lokalnim ključem, bez potrebe za 2FA. Podrazumevano trajanje je postavljeno na 12 meseci, ali za štednju Wallet, može imati smisla izabrati 15 meseci kako bi se smanjila učestalost obnove vremenske brave. Suprotno tome, za potrošnju Wallet, vremenska brava od 6 meseci može biti poželjnija, jer će se često obnavljati sa vašim dnevnim transakcijama, a kraća vremenska brava smanjuje čekanje u slučaju problema sa 2FA. Na vama je da odredite trajanje vremenske brave koje vam najviše odgovara.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


Sada možete izaći iz ovog menija. Vaš Multisig Wallet je spreman!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Postavljanje vašeg Wallet na Blockstream Green


Ako želite da personalizujete svoj Wallet, kliknite na tri male tačke u gornjem desnom uglu.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


Opcija "*Rename*" vam omogućava da prilagodite ime vašeg Wallet, što je posebno korisno ako upravljate sa nekoliko novčanika na istoj aplikaciji.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


Meni "*Unit*" vam omogućava da promenite osnovnu jedinicu vašeg Wallet. Na primer, možete odabrati da je prikažete u satoshijima umesto u bitkoinima.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


Meni "*Settings*" omogućava pristup raznim opcijama vašeg Bitcoin Wallet.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Ovde ćete, na primer, pronaći vaš prošireni javni ključ i njegov *deskriptor*, korisno ako planirate da postavite Wallet u režimu samo za gledanje sa ovog Wallet.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Takođe možete promeniti svoj Wallet PIN i aktivirati biometrijsku vezu.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Korišćenje Blockstream Green


Sada kada je vaš Bitcoin Wallet postavljen, spremni ste da primite svoj prvi Sats! Jednostavno kliknite na dugme "*Receive*".


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green će zatim prikazati prvi prazan prijem Address u vašem Wallet. Možete ili skenirati povezani QR kod, ili direktno kopirati Address da biste poslali bitkoine. Ovaj tip Address ne specificira iznos koji treba poslati od strane platioca. Međutim, možete generate Address koji zahteva određeni iznos, klikom na tri male tačke u gornjem desnom uglu, zatim na "*Zahtevaj iznos*", i unosom željenog iznosa.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


Kada se transakcija emituje na mreži, pojaviće se u vašem Wallet.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


Sačekajte dok ne dobijete dovoljno potvrda da smatrate transakciju konačnom.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Sa bitcoinima u vašem Wallet, sada možete i slati bitcoine. Kliknite na "*Pošalji*".


![GREEN 2FA MULTISIG](assets/fr/42.webp)


Na sledećoj stranici unesite primaočev Address. Možete ga uneti ručno ili skenirati QR kod.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Izaberite iznos plaćanja.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


Na dnu ekrana, možete odabrati stopu naknade za ovu transakciju. Imate izbor da pratite preporuke aplikacije ili da prilagodite svoje naknade. Što je naknada viša u odnosu na druge transakcije na čekanju, vaša transakcija će biti brže obrađena. Za informacije o tržištu naknada, molimo posetite [Mempool.space](https://Mempool.space/) u sekciji "*Transaction Fees*".


![GREEN 2FA MULTISIG](assets/fr/45.webp)


Kliknite na "*Next*" da biste pristupili ekranu sažetka transakcije. Proverite da li su Address, iznos i naknade tačni.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Ako sve bude u redu, pomerite dugme Green na dnu ekrana udesno da potpišete i emitujete transakciju na mreži Bitcoin.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


Ovo je trenutak kada treba da unesete svoj autentifikacioni kod da biste otključali drugi Multisig ključ koji drži Blockstream. Unesite 6-cifreni kod prikazan u vašoj autentifikacionoj aplikaciji.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


Vaša transakcija će se sada pojaviti na vašoj Bitcoin Wallet kontrolnoj tabli, čekajući potvrdu.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Sada znate kako lako postaviti 2/2 Multisig Wallet koristeći Blockstream Green-ovu 2FA opciju!


Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj drugi sveobuhvatni vodič o mobilnoj aplikaciji Blockstream Green za postavljanje Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a
