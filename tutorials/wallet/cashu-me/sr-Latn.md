---
name: Cashu.me
description: Cashu.me vodič za korišćenje ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Evo video tutorijal od BTC Sessions, video vodič koji vas vodi kroz postavljanje i korišćenje Cashu.me Bitcoin Wallet, koji vam omogućava pristup jednostavnim, jeftinim i privatnim Bitcoin transakcijama - bez potrebe za prodavnicom aplikacija!*


U ovom vodiču istražićemo Cashu.me, Wallet zasnovan na pretraživaču za privatna Bitcoin plaćanja koristeći Chaumian ecash. Pre nego što zaronimo, hajde da imamo kratak uvod u ecash i kako funkcioniše.


## Uvod u ecash


Zamislite da imate digitalni novac koji funkcioniše tačno kao fizičke novčanice u vašem džepu - privatan, trenutni i upotrebljiv od osobe do osobe bez posrednika. To je ono što omogućava ecash: digitalni način plaćanja koji vraća privatnost fizičkog novca u digitalni svet. Za razliku od onchain-Bitcoin, koji beleži svaku transakciju na javnom Ledger vidljivom svakome, ecash stvara privatne tokene koji predstavljaju pravu Bitcoin vrednost dok čuvaju vaše potrošačke navike poverljivim.


Zamislite ekesh kao digitalne nosioce instrumenata koji su uskladišteni na vašem uređaju - ako ih posedujete, vi ih i posedujete, baš kao i fizički novac. Ovi tokeni su izdati od strane pouzdanih servisa nazvanih `Mints` koji drže osnovne Bitcoin rezerve. Kada koristite ekesh, ne emitujete svoje transakcije celokupnoj mreži. Umesto toga, razmenjujete privatne tokene direktno sa drugima, stvarajući iskustvo plaćanja koje više liči na davanje nekome gotovine nego na tradicionalno digitalno plaćanje.


Cashu je besplatan i otvoren Chaumian ecash protokol izgrađen za Bitcoin. Tehnologija se oslanja na pionirska kriptografska istraživanja Davida Chauma iz 1980-ih, koristeći `slepe potpise` za osiguranje privatnosti. Kada primite ecash tokene, kovnica ih potpisuje bez saznanja gde će biti potrošeni sledeći put - ključna karakteristika koja sprečava praćenje transakcija. Važno je napomenuti da ecash ne zamenjuje Bitcoin; on ga dopunjuje rešavanjem nekih kritičnih problema koji dolaze sa zahtevima Bitcoin arhitekture. Pruža privatnost koju nudi fizički novac (koju transparentni Ledger Bitcoin nema) i omogućava trenutne mikrotransakcije bez Blockchain naknada ili kašnjenja u potvrdi.


Ecash se besprekorno integriše sa Lightning Network. Koristite Lightning za deponovanje Bitcoin u kovnicu (konvertujući vašu Bitcoin vrednost u ecash tokene) i za kasnije povlačenje (konvertujući tokene nazad u potrošljiv Lightning balans). Zajedno, oni čine moćnu kombinaciju: Bitcoin obezbeđuje sigurno poravnanje Layer, Lightning omogućava brze transakcije i interoperabilnost mreže, a ecash dodaje privatnost Layer koja čini da digitalna plaćanja ponovo deluju zaista privatno.


## Cashu.me


Cashu.me je `Progressive Web App (PWA)` koja implementira Cashu protokol - specifičnu implementaciju Chaumian ecash dizajniranu za Bitcoin. Kao PWA, radi direktno u vašem pregledaču bez potrebe za instalacijom iz prodavnica aplikacija, iako je možete `instalirati` na vaš uređaj radi lakšeg pristupa. Ovaj pristup zasnovan na vebu osigurava široku kompatibilnost između operativnih sistema, dok održava sigurnost putem kriptografskih protokola umesto ograničenja platforme.


## 🎉 Ključne Funkcije


Hajde da zaronimo u funkcije i istražimo šta Cashu.me nudi:



- Chaumian ecash na Lightning**: Koristi slepe potpise tako da kovnice ne mogu pratiti korisničke bilanse ili istorije transakcija
- Samostalno čuvanje tokena**: Kontrolišete ecash tokene lokalno sa vašom seed frazom
- seed rezervne fraze**: 12-rečenička fraza za oporavak Wallet
- Mint independence**: Radi sa više nezavisnih kovnica—niste vezani za jednog provajdera
- Instantne, besplatne transakcije**: Unutar iste kovnice, plaćanja se završavaju za nekoliko sekundi bez naknada
- Arhitektura koja čuva privatnost**: Mints ne mogu videti ko sa kim obavlja transakcije
- Offline ecash**: Šaljite/primajte tokene putem lokalnog protokola prenosa, kao što su NFC, QR kod, Bluetooth, itd. bez internet konekcije
- Otkrijte ecash mints putem Nostr**: Pronađite i verifikujte pouzdane mints kroz Nostr protokol
- Razmenite ecash između mintova**: Svi mintovi koriste Lightning, što znači da možete prenositi vrednost između njih.
- Daljinski upravljajte svojim Wallet pomoću Nostr Wallet Connect (NWC)**: Povežite se sa drugim aplikacijama kao što je Nostr Client i započnite zapping putem NWC


Ključna kompromisna tačka je `povjerenje`: dok vi kontrolišete same tokene, morate vjerovati kovnicama da čuvaju osnovne Bitcoin rezerve. Kao što navodi Cashuova dokumentacija:


> ...kovnica upravlja Lightning infrastrukturom i čuva satoshije za korisnike kovničkog ecash-a. Korisnici moraju verovati kovnici da će Redeem njihov ecash kada žele da ga zamene za Lightning.

— Cashu Dokumentacija, [Opšta pitanja o bezbednosti i privatnosti](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Ovo čini ecash skrbničkim rešenjem za sam Bitcoin, iako zadržavate punu kontrolu nad tokenima.


## 1️⃣ Početno podešavanje


① Počnite tako što ćete posetiti [Wallet.cashu.me](https://Wallet.cashu.me) u vašem pregledaču. Pošto je Cashu.me `PWA`, ne morate ga preuzimati iz prodavnica aplikacija, jednostavno otvorite sajt direktno u vašem pregledaču. Za lakši pristup, možete ga opcionalno instalirati na početni ekran vašeg uređaja.


② Da biste instalirali PWA, dodirnite dugme ⋮ menija u vašem pregledaču i izaberite `Dodaj na početni ekran`. Kada se instalira, zatvorite karticu pregledača i pokrenite Cashu.me sa početnog ekrana vašeg uređaja. Na ekranu dobrodošlice, dodirnite `Dalje` da nastavite.


③ Sigurnost je ključna. Čuvajte svoju seed frazu sigurno u menadžeru lozinki ili, još bolje, zapišite je na papir. Ova fraza za oporavak od 12 reči je vaš jedini način da povratite sredstva ako izgubite pristup ovom uređaju. Dodirnite ikonu 👁️ da otkrijete svoju seed frazu, pažljivo zapišite svih 12 reči redom, zatim označite polje `Zapisao/la sam`. Dodirnite `Dalje` da nastavite, i označite polje da potvrdite da prihvatate `uslove` na sledećem ekranu.


![image](assets/en/01.webp)


Nakon završetka postavljanja, potrebno je povezati se sa `Mint`. Dodirnite `ADD MINT`, a zatim `DISCOVER MINTS` da biste videli mintove koje preporučuje Nostr zajednica. Za dodatnu verifikaciju, možete pregledati ocene mintova na [bitcoinmints.com](bitcoinmints.com).


Zatim dodirnite `Click to browse mints` da biste videli celu listu. Izaberite mint kopiranjem njegovog URL-a, lepljenjem u polje za URL i davanjem prepoznatljivog imena. Za ovaj primer, koristićemo:


URL: `https://mint.minibits.cash/Bitcoin`

Ime: `Minibits`


![image](assets/en/02.webp)


Dodirnite `ADD MINT` da biste završili proces. Na ekranu za potvrdu, proverite da li verujete operateru ove kovnice, zatim ponovo dodirnite `ADD MINT`. Minibits kovnica će se sada pojaviti na vašem početnom ekranu. Kada vaš Wallet bude postavljen, moraćete da ga finansirate pre nego što obavite transakcije.


![image](assets/en/03.webp)


## 2️⃣ Finansiranje vašeg Wallet


Cashu.me nudi dva različita načina za finansiranje vašeg Wallet. Kada dodirnete `Receive` na početnom ekranu, videćete opcije za primanje sredstava putem `ECASH` ili putem `LIGHTNING.` Hajde da istražimo obe opcije.


![image](assets/en/04.webp)


### Finansiranje putem LIGHTNING


Prva opcija je da finansirate Wallet putem Lightning Invoice. `Select a mint` ako ste dodali različite kovnice i definišite `amount (Sats)` koji želite da primite. Zatim dodirnite `CREATE Invoice.` Sada će vam biti prikazan QR-kod koji možete skenirati sa drugim lightning Wallet ili jednostavno možete `Copy` Invoice i nalepiti u drugi Wallet da platite i finansirate vaš cashu.me Wallet.


![image](assets/en/05.webp)


### Primanje ekesh-a


Metoda ecash vam omogućava da primate tokene direktno od drugog ecash Wallet. Počnite tako što ćete dodirnuti dugme `Receive` i odabrati opciju `ECASH`. Moći ćete da `Paste` ili `Scan` ili koristite `NFC` da pošaljete Cashu token sa drugog Wallet. Ako izaberete da nalepite, unesite token string koji ste kopirali sa drugog Wallet, `Amount` i `Mint` će se automatski prikazati. Dodirnite `RECEIVE` da završite transakciju, i Sats će se pojaviti u vašem Wallet. Primetite da je vaš balans sada raspoređen preko više mintova. Na primer, možete imati 1,000 Sats u vašem Minibits `Mint` i dodatnih 1,000 Sats u Coinos `Mint`. Ova separacija preko različitih mintova je važan aspekt Cashu arhitekture.


![image](assets/en/06.webp)


### Prebacivanje između mintova


Ako više ne verujete određenoj kovnici koju ste dodali, cashu.me nudi opciju `Swap` za prebacivanje sredstava sa jedne kovnice na drugu. Idite na karticu kovnica i skrolujte dole dok ne vidite `Multimint Swaps`. Izaberite kovnicu `FROM` i `TO` iz padajućih menija i unesite iznos koji želite da prenesete. Dodirnite `SWAP` da biste premestili tokene između kovnica. Ovo će biti izvršeno putem Lightning transakcije, tako da treba da ostavite prostora za potencijalne Lightning naknade. U mom primeru, 1 sat je bio dovoljan.


![image](assets/en/07.webp)


## 3️⃣ Slanje sredstava


Da biste poslali Sats, Cashu.me nudi dve opcije. Za slanje putem `ecash` ili putem `lightning`. Pogledajmo obe opcije.


### Slanje putem Lightning-a


Da biste poslali putem Lightning-a, pratite ove korake:


1. Dodirnite `SEND` na početnom ekranu i odaberite `Lightning`

2. Aplikacija će vas podstaći da unesete `Lightning Invoice` ili `-Address`. Možete direktno nalepiti Invoice/Address, ili koristiti opciju skeniranja QR koda da ga vizuelno uhvatite, zatim potvrdite sa `ENTER`.

3. Izaberite Mint sa kojeg želite da platite koristeći padajući meni i dodirnite `PAY` da potvrdite. **Napomena**: postoji i opcija da koristite `Multinut` pod `Settings` -> `Experimental` koja vam omogućava da platite fakture sa više mintova odjednom.

4. Nakon uspešnog završetka, videćete potvrdu o uplati i iznos koji je odbijen sa vašeg stanja.


![image](assets/en/08.webp)


### Slanje putem ecash-a


Slanje e-novca je podjednako jednostavno.


1. Dodirnite `SEND` i ovog puta izaberite opciju `ECASH`.

2. `Odaberite kovnicu` i unesite `Iznos` koji želite poslati u Sats i dodirnite `POŠALJI` za potvrdu

3. Ovo kreira `Animirani QR Kod` koji možete prilagoditi podešavanjem parametara Brzine i Veličine. Svako može skenirati ovaj QR Kod da bi odmah Redeem na Sats, ili možete dodirnuti KOPIRAJ da biste poslali token string nekome drugom putem alternativnih kanala kao što su Bluetooth, NFC, ili standardne poruke.

4. Otvaram još jedan Wallet. Nalepi iz međumemorije i izaberi `Primi ecash` u drugom Wallet.


![image](assets/en/09.webp)


## 4️⃣ Dodatne Funkcije


Pored osnovne funkcionalnosti slanja i primanja, Cashu.me nudi moćne dodatne funkcije koje poboljšavaju vaše Bitcoin iskustvo unutar Nostr ekosistema.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) transformiše način na koji komunicirate sa Nostr aplikacijama stvarajući besprekornu vezu između vašeg Wallet i društvenih aplikacija. Ovaj protokol omogućava aplikacijama kao što su [Damus](https://damus.io/) ili [Primal](https://primal.net/home) da zahtevaju plaćanja direktno putem Nostr releja bez potrebe da napuštate aplikaciju.


Da biste postavili `NWC` u Cashu.me:


1. Idite na `Settings` u gornjem levom Hamburger meniju

2. Skroluj do odeljka `NOSTR Wallet CONNECT` i dodirni dugme `Enable`.

3. Zatim ćete postaviti dozvolu da biste utvrdili maksimalni iznos koji aplikacije mogu potrošiti sa vašeg Wallet.

4. Once configured, you can copy the connection string and paste it into any Nostr client that supports `NWC`, enabling instant zapping and tipping functionality.


![image](assets/en/10.webp)


### Lightning Address preko npub.cash


Cashu.me se integriše sa [npub.cash](https://npub.cash/) kako bi vam pružio Lightning Address koji besprekorno radi sa Nostr protokolom. Ovde se možete prijaviti i preuzeti svoje korisničko ime tako što ćete obezbediti svoj Nostr `nsec`, što košta 5.000 Sats i podržava npub.cash projekat, ili možete koristiti bilo koji Nostr javni ključ (`npub`) bez registracije.


Prvo idite na `Settings` i dodirnite `Enable` Lightning Address sa npub.cash. Ovo će generate npub.cash Address koristeći `npub` string izveden iz vaše Wallet seed fraze po defaultu.


Alternativno, posetite [ovu veb stranicu](https://npub.cash/username) da biste preuzeli prilagođeno korisničko ime koristeći svoj sopstveni Nostr `nsec`, što vam omogućava personalizovano Lightning Address korisničko ime poput username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Zaključak


Cashu.me isporučuje privatna Bitcoin plaćanja koja funkcionišu kao fizički novac — trenutno i peer-to-peer bez izlaganja vaše istorije transakcija. Lično cenim njegovu PWA arhitekturu jer radi bez ograničenja prodavnica aplikacija. Kombinovanjem sigurnosti Bitcoin, brzine Lightning-a i privatnosti ecash-a, Wallet nudi slučajeve upotrebe koji bi mogli poboljšati svakodnevno usvajanje Bitcoin.


Iako imate potpunu kontrolu nad svojim ecash tokenima kroz samostalno čuvanje, zapamtite da menjačnice deluju kao pouzdane treće strane koje drže osnovne Bitcoin rezerve. Mogućnost korišćenja više menjačnica i zamene između njih pruža fleksibilnost uz očuvanje privatnosti.


Zahvaljujući funkcijama kao što su NWC i npub.cash adrese, Cashu.me je privlačna Wallet opcija za društvene klijente koji cene privatnost i suverenitet nad ograničenjima politike velikih tehnoloških kompanija.


## 📚 Resursi


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)