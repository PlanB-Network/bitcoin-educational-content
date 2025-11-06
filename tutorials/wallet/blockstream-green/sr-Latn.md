---
name: Blockstream Green - Mobilni
description: Postavljanje mobilnog Software Wallet
---
![cover](assets/cover.webp)


Software Wallet je aplikacija instalirana na računaru, pametnom telefonu ili drugom uređaju povezanom na Internet, omogućavajući vam upravljanje i zaštitu vaših Bitcoin Wallet ključeva. Za razliku od hardverskih novčanika, koji izoluju privatne ključeve, "Hot" novčanici stoga rade u okruženju potencijalno izloženom sajber napadima, povećavajući rizik od piraterije i krađe.


Softverski novčanici treba da se koriste za upravljanje razumnim količinama bitkoina, posebno za svakodnevne transakcije. Oni takođe mogu biti zanimljiva opcija za ljude sa ograničenim Bitcoin sredstvima, za koje ulaganje u Hardware Wallet može izgledati nesrazmerno. Međutim, njihova stalna izloženost internetu čini ih manje sigurnim za čuvanje vaših dugoročnih ušteđevina ili velikih sredstava. Za ovo poslednje, najbolje je odlučiti se za sigurnija rešenja, kao što su hardverski novčanici.


U ovom vodiču, želeo bih da vas upoznam sa jednim od najboljih mobilnih Software Wallet rešenja: **Blockstream Green**.


![GREEN](assets/fr/01.webp)


Ako želite da saznate kako da koristite Blockstream Green na svom računaru, pogledajte ovaj drugi vodič:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

## Predstavljamo Blockstream Green


Blockstream Green je Software Wallet dostupan na mobilnim uređajima i desktopu. Ranije poznat kao *Green Address*, ovaj Wallet je postao Blockstream projekat nakon njegove akvizicije 2016. godine.


Green je posebno jednostavna aplikacija za korišćenje, što je čini zanimljivom za početnike. Nudi sve osnovne funkcije dobrog Bitcoin Wallet, uključujući RBF (*Replace-by-fee*), opciju povezivanja sa Tor-om, mogućnost povezivanja sopstvenog čvora, SPV (*Simple Payment Verification*), označavanje i kontrolu novčića.


Blockstream Green takođe podržava Liquid Network, Bitcoin Sidechain razvijen od strane Blockstream-a za brzo, Confidential Transactions izvan glavnog Blockchain. Ovaj vodič se fokusira isključivo na Bitcoin, ali kasniji će pokriti upotrebu Liquid.


## Instaliranje i konfiguracija aplikacije Blockstream Green


Prvi korak je naravno preuzimanje aplikacije Green. Idite u svoju prodavnicu aplikacija:



- [Za Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Za Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN](assets/fr/02.webp)


Za korisnike Androida, možete takođe instalirati aplikaciju putem `.apk` fajla [dostupnog na Blockstream-ovom GitHub-u](https://github.com/Blockstream/green_android/releases).


![GREEN](assets/fr/03.webp)


Pokrenite aplikaciju, a zatim označite polje "Prihvatam uslove...*".


![GREEN](assets/fr/04.webp)


Kada prvi put otvorite Green, početni ekran se pojavljuje bez konfigurisanog Wallet. Kasnije, ako kreirate ili uvezete novčanike, oni će se pojaviti u ovom Interface. Pre nego što pređete na kreiranje Wallet, savetujem vam da prilagodite postavke aplikacije prema vašim potrebama. Kliknite na "Postavke aplikacije".


![GREEN](assets/fr/05.webp)


Opcija "*Poboljšana privatnost*", dostupna samo na Androidu, poboljšava privatnost onemogućavanjem snimaka ekrana i skrivanjem pregleda aplikacija. Takođe automatski zaključava pristup aplikaciji čim se vaš telefon zaključa, čineći vaše podatke težim za izlaganje.


![GREEN](assets/fr/06.webp)


Za one koji žele poboljšati svoju privatnost, aplikacija nudi opciju usmeravanja vašeg saobraćaja putem Tor-a, mreže koja šifrira sve vaše veze i otežava praćenje vaših aktivnosti. Iako ova opcija može malo usporiti rad aplikacije, toplo se preporučuje za zaštitu vaše privatnosti, posebno ako ne koristite svoj kompletan čvor.


![GREEN](assets/fr/07.webp)


Za korisnike koji imaju svoj sopstveni kompletan čvor, Green Wallet nudi mogućnost povezivanja putem Electrum servera, garantujući potpunu kontrolu nad informacijama Bitcoin mreže i distribucijom transakcija.


![GREEN](assets/fr/08.webp)


Još jedna alternativna funkcija je opcija "*SPV Verification*", koja vam omogućava da direktno verifikujete određene Blockchain podatke i tako smanjite potrebu za poverenjem u podrazumevani čvor Blockstream-a, iako ova metoda ne pruža sve garancije Full node.


![GREEN](assets/fr/09.webp)


Kada prilagodite ova podešavanja svojim potrebama, kliknite na dugme "*Save*" i ponovo pokrenite aplikaciju.


![GREEN](assets/fr/10.webp)


## Kreiraj Bitcoin Wallet na Blockstream Green


Sada ste spremni da kreirate Bitcoin Wallet. Kliknite na dugme "*Get Started*".


![GREEN](assets/fr/11.webp)


Možete birati između kreiranja lokalnog Software Wallet ili upravljanja Cold Wallet putem Hardware Wallet. Za ovaj vodič, koncentrisaćemo se na kreiranje Hot Wallet, tako da ćete morati odabrati opciju "*Na ovom uređaju*". U budućem vodiču, pokazaću vam kako da koristite drugu opciju.


Opcija "*Watch-only*", u međuvremenu, omogućava vam da uvezete prošireni javni ključ (`xpub`) kako biste videli transakcije Wallet bez mogućnosti trošenja povezanih sredstava, što je korisno za praćenje Wallet na Hardware Wallet, na primer.


![GREEN](assets/fr/12.webp)


Zatim možete izabrati da obnovite postojeći Bitcoin Wallet ili da kreirate novi. Za potrebe ovog tutorijala, kreiraćemo novi Wallet. Međutim, ako treba da regenerišete postojeći Bitcoin Wallet iz njegove Mnemonic fraze, na primer nakon gubitka vašeg Hardware Wallet, moraćete da izaberete drugu opciju.


![GREEN](assets/fr/13.webp)


Zatim možete izabrati između 12-reči ili 24-reči Mnemonic fraze. Ova fraza će vam omogućiti da povratite pristup vašem Wallet sa bilo kog kompatibilnog softvera u slučaju problema sa vašim telefonom. Trenutno, izbor 24-reči fraze ne nudi više sigurnosti od 12-reči fraze. Stoga preporučujem da izaberete 12-reči Mnemonic frazu.


Green će vam zatim pružiti vašu Mnemonic frazu. Pre nego što nastavite, uverite se da vas niko ne posmatra. Kliknite na "*Prikaži frazu za oporavak*" da biste je prikazali na ekranu.


![GREEN](assets/fr/14.webp)


**Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima** Svako ko poseduje ovaj Mnemonic može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem telefonu.


Vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vašeg telefona. Zato je veoma važno da ga pažljivo napravite rezervnu kopiju **na fizičkom mediju (ne digitalnom)** i čuvate je na sigurnom mestu. Možete ga zapisati na komad papira, ili za dodatnu sigurnost, ako je ovo veliki Wallet, preporučujem graviranje na nosač od nerđajućeg čelika kako biste ga zaštitili od rizika od požara, poplave ili urušavanja (za Hot Wallet dizajniran da osigura malu količinu bitcoina, jednostavna papirna kopija je verovatno dovoljna).


*Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom uputstvu. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva.*


![GREEN](assets/fr/15.webp)


Jednom kada pravilno zabeležite svoju Mnemonic frazu na fizičkom mediju, kliknite na "*Nastavi*". Green Wallet će vas zatim zamoliti da potvrdite neke od reči u vašoj Mnemonic frazi kako biste bili sigurni da ste ih pravilno zabeležili. Popunite praznine nedostajućim rečima.


![GREEN](assets/fr/16.webp)


Izaberite PIN kod svog uređaja, koji će se koristiti za otključavanje vašeg Green Wallet. Ovo je vaša zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše 12- ili 24-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.


Preporučujemo da izaberete 6-cifreni PIN kod koji je što je moguće nasumičniji. Obavezno sačuvajte ovaj kod kako ga ne biste zaboravili, inače ćete biti primorani da preuzmete svoj Wallet sa Mnemonic. Zatim možete dodati opciju biometrijske blokade kako ne biste morali unositi PIN svaki put kada ga koristite. Generalno govoreći, biometrija je daleko manje sigurna od samog PIN-a. Dakle, po defaultu, savetujem vam da ne postavljate ovu opciju otključavanja.


![GREEN](assets/fr/17.webp)


Unesite svoj PIN drugi put da ga potvrdite.


![GREEN](assets/fr/18.webp)


Sačekajte da vaš Wallet bude kreiran, zatim kliknite na dugme "*Kreiraj nalog*".


![GREEN](assets/fr/19.webp)


Možete zatim izabrati između standardnog Wallet sa jednim potpisom, koji ćemo koristiti u ovom uputstvu, ili Wallet zaštićenog dvofaktorskom autentifikacijom (2FA).


![GREEN](assets/fr/20.webp)


Opcija 2FA na Green kreira 2/2 multisignature Wallet, sa jednim ključem koji drži Blockstream. To znači da su za obavljanje transakcije potrebna oba ključa: lokalni ključ zaštićen vašim PIN kodom na telefonu i udaljeni ključ osiguran 2FA na Blockstream-ovim serverima. U slučaju gubitka pristupa 2FA ili nedostupnosti Blockstream-ovih usluga, mehanizmi oporavka zasnovani na time-lock skriptama osiguravaju da se vaša sredstva mogu autonomno povratiti. Iako ova konfiguracija značajno smanjuje rizik od krađe vaših bitcoina, složenija je za upravljanje i delimično zavisi od Blockstream-a. Za ovaj vodič, odlučićemo se za klasični single-signature Wallet, sa ključevima koji su lokalno pohranjeni na telefonu.


Vaš Bitcoin Wallet je sada kreiran korišćenjem aplikacije Green!


![GREEN](assets/fr/21.webp)


Pre nego što primite svoje prve bitkoine u svoj Wallet, **toplo vam savetujem da izvršite test praznog oporavka**. Zapišite neke referentne informacije, kao što su vaš xpub ili prvi prijemni Address, zatim obrišite svoj Wallet u aplikaciji Green dok je još uvek prazan. Zatim pokušajte da obnovite svoj Wallet na Green koristeći svoje papirne rezervne kopije. Proverite da li informacije o kolačićima generisane nakon obnove odgovaraju onima koje ste prvobitno zapisali. Ako odgovaraju, možete biti sigurni da su vaše papirne rezervne kopije pouzdane. Da biste saznali više o tome kako izvršiti test oporavka, molimo vas da pogledate ovaj drugi vodič:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Postavljanje vašeg Wallet na Blockstream Green


Ako želite da personalizujete svoj Wallet, kliknite na tri male tačke u gornjem desnom uglu.


![GREEN](assets/fr/22.webp)


Opcija "*Preimenuj*" vam omogućava da prilagodite ime vašeg Wallet, što je posebno korisno ako upravljate sa nekoliko novčanika na istoj aplikaciji.


![GREEN](assets/fr/23.webp)


Meni "*Unit*" vam omogućava da promenite osnovnu jedinicu vašeg Wallet. Na primer, možete odabrati da je prikažete u satoshijima umesto u bitkoinima.


![GREEN](assets/fr/24.webp)


Meni "*Settings*" omogućava pristup raznim opcijama vašeg Bitcoin Wallet.


![GREEN](assets/fr/25.webp)


Ovde, na primer, pronaći ćete svoj prošireni javni ključ i njegov *deskriptor*, korisno ako planirate da postavite Wallet u režimu samo za gledanje sa ovog Wallet.


![GREEN](assets/fr/26.webp)


Takođe možete promeniti svoj Wallet PIN i aktivirati biometrijsku vezu.


![GREEN](assets/fr/27.webp)


## Korišćenje Blockstream Green


Sada kada je vaš Bitcoin Wallet postavljen, spremni ste da primite svoj prvi Sats! Jednostavno kliknite na dugme "*Receive*".


![GREEN](assets/fr/28.webp)


Green će zatim prikazati prvi prazan prijem Address u vašem Wallet. Možete ili skenirati povezani QR kod, ili direktno kopirati Address za slanje bitkoina. Ovaj tip Address ne specificira iznos koji treba poslati od strane platioca. Međutim, možete generate Address koji zahteva određeni iznos, klikom na tri male tačke u gornjem desnom uglu, zatim na "*Zahtevaj iznos*", i unosom željenog iznosa.


Pošto koristite SegWit v0 nalog (BIP84), vaš Address će počinjati sa `bc1q...`. U mom primeru, koristim Testnet Wallet, tako da je prefiks malo drugačiji.


![GREEN](assets/fr/29.webp)


Kada se transakcija emituje na mreži, pojaviće se u vašem Wallet.


![GREEN](assets/fr/30.webp)


Sačekajte dok ne dobijete dovoljno potvrda da biste transakciju smatrali konačnom.


![GREEN](assets/fr/31.webp)


Sa bitcoinima u vašem Wallet, sada možete i slati bitcoine. Kliknite na "*Pošalji*".


![GREEN](assets/fr/32.webp)


Na sledećoj stranici unesite primalacov Address. Možete ga uneti ručno ili skenirati QR kod.


![GREEN](assets/fr/33.webp)


Izaberite iznos plaćanja.


![GREEN](assets/fr/34.webp)


Na dnu ekrana, možete odabrati stopu naknade za ovu transakciju. Imate izbor da pratite preporuke aplikacije ili da prilagodite svoje naknade. Što je naknada viša u odnosu na druge transakcije na čekanju, vaša transakcija će biti brže obrađena. Za informacije o tržištu naknada, molimo posetite [Mempool.space](https://Mempool.space/) u sekciji "*Transaction Fees*".


![GREEN](assets/fr/35.webp)


Kliknite na "*Next*" da biste pristupili ekranu sažetka transakcije. Proverite da li su Address, iznos i naknade tačni.


![GREEN](assets/fr/36.webp)


Ako sve bude u redu, pomerite dugme Green na dnu ekrana udesno da potpišete i emitujete transakciju na mreži Bitcoin.


![GREEN](assets/fr/37.webp)


Vaša transakcija će se sada pojaviti na vašoj Bitcoin Wallet kontrolnoj tabli, čekajući potvrdu.


![GREEN](assets/fr/38.webp)


*Ovaj vodič je zasnovan na [originalnoj verziji koja pripada Bitstack-u](https://www.bitstack-app.com/blog/installer-portefeuille-Bitcoin-Green-Wallet) koju je napisao Loïc Morel. Bitstack je francuska Bitcoin neo-banka koja nudi mogućnost štednje u bitkoinima, bilo putem DCA (Dollar Cost Averaging), ili putem automatskog sistema zaokruživanja za dnevne troškove.* Bitstack je francuska Bitcoin neo-banka koja nudi mogućnost štednje u bitkoinima, bilo putem DCA (Dollar Cost Averaging), ili putem automatskog sistema zaokruživanja za dnevne troškove.