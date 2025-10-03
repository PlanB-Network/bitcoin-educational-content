---
name: Minibits Wallet
description: Vodič za Minibits Wallet
---

![cover](assets/cover.webp)


U ovom vodiču, provesti ću vas kroz postavljanje Minibits Wallet za korišćenje ecash-a. Moćna tehnologija plaćanja fokusirana na privatnost koja radi zajedno sa Bitcoin. Minibits je ecash i Lightning Wallet koji omogućava trenutne, jeftine i privatne prenose vrednosti, što ga čini idealnim za svakodnevne transakcije gde je privatnost važna.


Pre nego što zaronimo u Minibits, hajde da uspostavimo jasno razumevanje šta ecash jeste, a šta nije. Mnogi ljudi mešaju ecash sa Bitcoin ili Blockchain tehnologijom, ali to su suštinski različiti koncepti.


Ecash NIJE Bitcoin. Ne zamenjuje vaš samostalni Bitcoin Wallet već ga dopunjuje. Ecash NIJE Blockchain i NE postoji na bilo kom javnom Ledger. Zanimljivo je da ecash NIJE nova tehnologija—zapravo prethodi svetskoj mreži, sa konceptima razvijenim 1980-ih i 1990-ih.


Šta je ekesh: neverovatno privatan (transakcije ne ostavljaju tragove), peer-to-peer (direktni transferi bez posrednika) i funkcioniše kao digitalni instrument na donosioca (ako ga posedujete, vi ga kontrolišete). Ključna prednost je što se ekesh MOŽE koristiti van mreže—ili pošiljalac ili primalac mogu biti isključeni sa interneta tokom transakcija. Ekesh MOŽE biti kovan od strane jedne strane ili od strane federacije pouzdanih entiteta, i to JE savršena komplementarna tehnologija za Bitcoin, koja obrađuje male, česte transakcije dok Bitcoin služi kao poravnanje Layer.


Imajte na umu da ova Minibits postavka predstavlja `skrbničko rešenje`, što znači da verujete operateru Mint-a da upravlja vašim sredstvima. Ovo uvodi određene rizike koje morate razumeti pre nego što nastavite.


Projekat prikazuje ovo važno odricanje odgovornosti:


- Ovaj Wallet treba koristiti samo u istraživačke svrhe.
- Wallet je beta verzija sa nepotpunom funkcionalnošću i poznatim i nepoznatim greškama.
- Ne koristite ga sa velikim količinama ekesh-a.
- Ecash uskladišten u Wallet izdaje kovnica
- verujete da će kovnica podržati to sa Bitcoin dok ne prenesete svoja sredstva na drugi Bitcoin lightning Wallet.
- Kešu protokol koji Wallet implementira još uvek nije prošao opsežnu reviziju ili testiranje.


Tretirajte Minibits kao svakodnevni Wallet, a ne kao štedni račun, i nikada ne čuvajte značajnu vrednost ovde.


## 1️⃣ Postavljanje vašeg Wallet


Da biste započeli, posetite [Minibits Website](https://www.minibits.cash/) gde ćete pronaći opcije za preuzimanje za sve glavne platforme. iOS korisnici mogu preuzeti sa [App Store](https://testflight.apple.com/join/defJQgTD), dok korisnici iOS-a u EU imaju dodatnu opciju instaliranja sa [Freedom Store](https://freedomstore.io/). Android korisnici mogu preuzeti aplikaciju sa [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) ili preuzeti APK datoteku direktno sa [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) stranice.


Kada instalirate Minibits, videćete uvodne ekrane koji objašnjavaju osnovne pojmove—možete ih pročitati ili preskočiti ako ste već upoznati sa tehnologijom. Kada završite ove početne korake, bićete upitani da izaberete između:


- `Razumem, vodi me do Wallet` za nove korisnike ili
- `Povrati izgubljeni Wallet` ako vraćaš sa rezervne kopije.


![image](assets/en/01.webp)

Nakon završetka početnog podešavanja, doći ćete na Početni ekran, koji ima nekoliko važnih Elements za napomenuti. ① Ikona profila u gornjem uglu vodi vas na vašu stranicu profila gde možete pristupiti vašim Minibits Wallet Address i odabrati opcije `batch receive`. ② U sredini ekrana, videćete Mintove koje možete koristiti, sa Minibits mintom izabranim po defaultu. ③ Red akcija ispod pruža opcije za slanje ecash ili lightning uplata, skeniranje QR koda i primanje uplata. ④ Na kraju, donja navigaciona traka sadrži prečice do Početnog ekrana, Istorije transakcija, Kontakata i Podešavanja.


![image](assets/en/02.webp)


## 2️⃣ Upravljaj mentama


Podrazumevano, Minibits kovnica je omogućena kada pokrenete aplikaciju. Međutim, jedna od prednosti ecash-a je mogućnost korišćenja više kovnica za povećanu decentralizaciju i sigurnost. Da biste dodali drugu kovnicu, idite na `Settings`, zatim izaberite `Manage mints`, i na kraju dodirnite `Add mint`.


[Bitcoinmints.com](Bitcoinmints.com) pruža sveobuhvatan spisak dostupnih menjačnica sa ocenama korisnika kako bi vam pomogao da izaberete pouzdane opcije. Korišćenje više menjačnica smanjuje vaš rizik. Ako jedna menjačnica ima problema, vaša sredstva na drugim menjačnicama ostaju dostupna.


![image](assets/en/04.webp)


## 3️⃣ Kreiranje rezervne kopije


Bekap je verovatno najkritičniji korak u celom procesu postavljanja. Da biste pristupili opcijama Bekapa, idite na `Podešavanja`-> `Bekap` Ovde ćete pronaći dve ključne opcije:

1. `Vaša seed fraza` koja sadrži `12 reči` omogućava vam da povratite svoj ecash saldo u slučaju gubitka uređaja. Ova seed fraza je vaš glavni ključ za sav ecash preko svih menjačnica koje ste dodali. Zapišite je na fizički medijum (papir ili metal) i čuvajte je na sigurnom na više lokacija. Nikada ne čuvajte svoju seed frazu digitalno gde bi mogla biti ugrožena. Razmislite o poseti ovom [uputstvu](https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) za najbolje prakse za zaštitu vaše Wallet.

2. `Wallet backup` koji sadrži dugačak niz za rezervnu kopiju.


**Pažnja**: I dalje će vam biti potrebna vaša seed fraza kada koristite ovu rezervnu kopiju za oporavak vašeg Wallet.


![image](assets/en/05.webp)


## 4️⃣ Kreiraj Minibits Wallet Address


Zatim idite na `Contacts` na dnu i prilagodite svoj posvećeni `Minibits Wallet Address` dodirom na `Change` -> `Change Wallet Address`. Unesite svoj preferirani Address i proverite dostupnost.


![image](assets/en/07.webp)


Nakon što postavite svoj Address, bićete upitani za malu `Donaciju` kako biste podržali projekat. Iako je ovo opcionalno, toplo preporučujem da razmislite o tome ako planirate redovno koristiti uslugu. Projekti otvorenog koda poput Minibits-a oslanjaju se na podršku zajednice za nastavak razvoja i održavanja. Čak i mali doprinos pomaže u osiguravanju dugovečnosti projekta.


![image](assets/en/08.webp)


## 5️⃣ Nostr Setup


Ako želite da nagradite ljude koje pratite na Nostr-u, možete `Dodati svoj npub ključ` tako što ćete odabrati `Kontakti` a zatim `Javno`. Ovo povezuje vaš Minibits Wallet sa Nostr društvenom mrežom, omogućavajući jednostavno nagrađivanje.


Takođe imate opciju da `Koristite svoj profil` tako što ćete otići na `Podešavanja`, a zatim `Privatnost` da uvezete svoj Nostr Address i ključ. Međutim, budite svesni da će ovo zaustaviti vaš Wallet od komunikacije sa minibits.cash Nostr i LNURL Address serverima, što onemogućava Address funkcije za primanje zaps i uplata.


![image](assets/en/09.webp)


## 6️⃣ Primi sredstva


Da biste inicijalno primili sredstva, potrebno je da dopunite svoj Wallet putem lightning Invoice. Ovaj proces je jednostavan: dodirnite `Topup`, unesite `Amount` koji želite dodati, opcionalno dodajte `Memo`, a zatim dodirnite `Create Invoice`. Potrebno je da platite ovaj Invoice koristeći drugi Lightning Wallet, ovo konvertuje Bitcoin Lightning uplate u ecash tokene unutar vašeg Minibits Wallet.


![image](assets/en/10.webp)


## 7️⃣ Pošalji sredstva


Sada kada ste finansirali svoj Wallet, možete slati sredstva na dva različita načina.


### Pošalji ecash


Prva opcija je da pošaljete ecash direktno. Dodirnite `Send`, zatim izaberite `Send ecash`, unesite `Amount`, i dodirnite `Create token.` Ovo će generate QR kod koji možete podeliti sa primaocem ili ga oni mogu skenirati direktno svojim uređajem. Primalac će videti tokene kako se pojavljuju u njihovom Wallet skoro trenutno, bez Blockchain naknada ili kašnjenja u potvrdi.


![image](assets/en/11.webp)


### Plati sa Lightning


Druga opcija je plaćanje putem Lightning-a. Dodirnite `Send`, zatim izaberite `Pay with Lightning`. Možete izabrati iz svojih Nostr `contacts` (ako ste povezali svoj npub), ili uneti/nalepiti Lightning Address, Invoice, ili LNURL kod za plaćanje koristeći opciju `Paste` ili `scan`. Nakon `Confirming` primaoca, bićete upitani da unesete `Amount to Pay`, opcionalno dodate belešku, a zatim dodirnite `Confirm` praćeno sa `Pay now` da biste završili Lightning transakciju.


![image](assets/en/12.webp)


## 8️⃣ Kreiraj NWC vezu


Još jedna moćna funkcija Minibits-a je mogućnost kreiranja `Nostr Wallet Connect (NWC)` konekcija, koje omogućavaju drugim aplikacijama da zatraže plaćanja sa vašeg Wallet bez izlaganja vaših privatnih ključeva.


Da biste ovo postavili, idite na `Settings`, zatim izaberite `Nostr Wallet Connect`, i dodirnite `Add connection`. Imenujte vašu konekciju nečim opisnim kako biste identifikovali i aplikaciju i povezani korisnički nalog. Postavite razuman maksimalni dnevni limit kako biste kontrolisali koliko se može potrošiti putem ove konekcije, zatim dodirnite `Save` da završite postavljanje.


Ova funkcija je posebno korisna za usluge kao što su Nostr klijenti gde želite omogućiti automatsko davanje napojnica bez ručnog odobravanja svake transakcije.


![image](assets/en/12.webp)


## 🎯 Zaključak


Minibits pruža pristupačnu ulaznu tačku u svet ecash-a, nudeći plaćanja fokusirana na privatnost koja dopunjuju vaša Bitcoin sredstva. Zapamtite da uvek održavate odgovarajuće rezervne kopije, razmislite o korišćenju više menjačnica za redundanciju i čuvajte samo odgovarajuće iznose u ovom skrbničkom rešenju.


Za dodatne resurse, pogledajte Minibits GitHub repozitorijum, zvaničnu veb stranicu i njihov Telegram kanal gde zajednica aktivno diskutuje o razvoju i rešava probleme.


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Website](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ekosistem ekesh-a se još uvek razvija, ali alati poput Minibits-a čine ovu moćnu tehnologiju privatnosti sve dostupnijom svakodnevnim korisnicima.