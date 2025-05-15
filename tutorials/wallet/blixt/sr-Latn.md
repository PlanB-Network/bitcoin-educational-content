---
name: Blixt

description: Mobilni LN Čvor Wallet
---

![presentation](assets/blixt_intro_en.webp)


## Snažan BTC/Lightning čvor u vašem džepu, gde god da ste


Želeo bih da vas upoznam sa zanimljivim i moćnim novim BTC/LN mobilnim čvorom i Wallet – Blixt. Ime dolazi iz švedskog i znači "munja".

Ako nikada niste koristili Bitcoin Lightning Network, pre nego što počnete, molimo vas da pročitate [ovo jednostavno objašnjenje analogije o Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).


## VAŽNI ASPEKTI:


### 1. Blixt je privatni čvor, NIJE čvor za rutiranje! Imajte to na umu.


To znači da svi LN kanali u Blixtu neće biti najavljeni na LN grafu (tzv. privatni kanali). To znači, OVAJ ČVOR NEĆE RADITI RUTIRANJE plaćanja drugih kroz Blixt čvor. [Pročitajte više o privatnim i javnim kanalima ovde](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).


Blixt mobilni čvor NIJE za rutiranje, ponavljam. Služi prvenstveno za upravljanje sopstvenim LN kanalima i obavljanje LN plaćanja privatno, kad god vam zatreba.


Blixt mobilni čvor, potrebno je da bude online i sinhronizovan SAMO PRE nego što ćete obaviti svoje transakcije. Zato ćete videti ikonu na vrhu koja pokazuje status sinhronizacije. Potrebno je samo nekoliko trenutaka, u zavisnosti od toga koliko dugo ste ga držali offline i ponovo sinhronizovali LN grafikon.


### 2. Blixt koristi LND (aezeed) kao pozadinu za Wallet, tako da ne pokušavajte da uvozite druge tipove Bitcoin novčanika u njega.


[Ovde ste objasnili tipove novčanika](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Dakle, ako ste ranije imali LND čvor, možete importovati seed i backup.channels u Blixt, [kao što je objašnjeno u ovom vodiču](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).


### 3. Blixt važni linkovi (molimo vas da ih dodate u obeleživače):



- [Blixt Github repository](https://github.com/hsjoberg/blixt-Wallet) | [Github Releases](https://github.com/hsjoberg/blixt-Wallet/releases) (preuzmite apk datoteku direktno)
- [Blixt Features page](https://blixtwallet.github.io/features) - objašnjavajući jednu po jednu svaku funkciju i funkcionalnost.
- [Blixt FAQ stranica](https://blixtwallet.github.io/faq) - Lista pitanja i odgovora i rešavanje problema za Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demonstracije, video tutorijali, dodatni vodiči i slučajevi upotrebe za Blixt
- [Štampaj A4 flajer](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) sa prvim koracima korišćenja Blixt-a, na različitim jezicima.
- Blixt takođe nudi potpuno funkcionalan demo direktno na [svojoj veb stranici](https://blixtwallet.com) ili na posebnoj [veb verziji](https://blixt-Wallet-git-master-hsjoberg.vercel.app/), kako biste imali potpuno iskustvo testiranja pre nego što počnete koristiti Blixt u stvarnom svetu.
- [Stranica za crowdfunding na Geyseru](https://geyser.fund/project/blixt) - donirajte Sats kako želite da podržite projekat
- [Telegram support group](https://t.me/blixtwallet)


# Ključne funkcije dostupne


## Neutrino Node


Blixt se po defaultu povezuje na Blixt-ov server kako bi sinhronizovao blokove i indeksirao sa Neutrino (SPV mod za pojednostavljenu verifikaciju plaćanja), ali korisnik takođe može da se poveže na svoj čvor. Iznenađujuće je videti da sinhronizacija SPV čvora traje manje od 5 minuta, u mom slučaju na Android 11, da bi bio spreman za korišćenje Full node Wallet (On-Chain i LN).


## Kompletan nekustodijalni čvor


Korisnik može upravljati sopstvenim kanalima uz jednostavan za korišćenje Interface i sa dovoljno prikazanih informacija za dobro iskustvo. U meniju gornje leve fioke, možete otići do Lightning kanala da započnete otvaranje sa drugim čvorovima, po želji. Ne zaboravite da omogućite Tor u podešavanjima. Mnogo je bolje za privatnost, a takođe i zato što kao mobilni čvor, ako često menjate internet konekciju / clearnet IP, vaši partneri mogu biti ometeni. Sa Tor čvor URI, uvek ćete imati isti privatni identifikator bez obzira na vašu lokaciju / IP.


## Backup/Restore an LND Node


Snažna, jednostavna za upravljanje i korisna funkcija je obnavljanje drugih mrtvih LND čvorova, samo uz 24-rečnu seed listu i channels.backup fajl. [Ovde je vodič o tome kako obnoviti mrtve Umbrel čvorove u Blixt u slučaju SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)


Korisnik takođe ima opciju da sačuva rezervnu kopiju Blixt kanala na Google Drive i/ili lokalnu memoriju na sopstvenom mobilnom uređaju (da bi je kasnije premestio na sigurno mesto, dalje od telefona).


Proces restauracije je prilično jednostavan: ubacite 24 reči seed, dodajte rezervnu kopiju (prethodno kopiranu u memoriju mobilnog uređaja), i kliknite na restauraciju. Biće potrebno neko vreme da se sinhronizuju i skeniraju svi blokovi za vaše prethodne transakcije. Kanali će biti automatski zatvoreni i sredstva vraćena na vaš On-Chain Wallet (pogledajte meni u gornjem levom fioci - On-Chain).


**Napomena** Ako ste prethodno imali otvorene kanale sa vašim starim čvorom iza Tor-a, prvo morate omogućiti Tor opciju (i restartovati aplikaciju) iz menija podešavanja. Na ovaj način, procedura zatvaranja neće propasti i/ili opcija prisilnog zatvaranja neće biti korišćena.


Ne zaboravite da napravite rezervnu kopiju vaših LN kanala nakon otvaranja i/ili zatvaranja kanala. Potrebno je samo nekoliko sekundi da budete sigurni. Kasnije, možete premestiti rezervnu kopiju na sigurno mesto dalje od vašeg mobilnog uređaja.

Da biste testirali vaš seed u scenariju obnove, pre dodavanja sredstava, jednostavno koristite istih 24 reči seed (aezeed) u BlueWallet. Ako je generisani BTC Address isti u Blixt, spremni ste. Nema potrebe da koristite BlueWallet nakon toga, možete jednostavno obrisati testirani Wallet za obnovu.


## Ugrađeni Tor


Jednom kada ga aktivirate, aplikacija će se ponovo pokrenuti iza Tor mreže. Od ovog trenutka, možete videti u postavkama menija vaš ID čvora sa onion Address, tako da drugi čvorovi mogu otvoriti kanale ka vašem malom Blixt mobilnom čvoru. Ili recimo da imate svoj čvor kod kuće i želite da imate male kanale sa vašim Blixt mobilnim čvorom. Savršena kombinacija.


## Dunder LSP - Pružalac usluga likvidnosti


Jednostavna i fantastična funkcija koja novim korisnicima nudi mogućnost da odmah počnu prihvatati BTC na Lightning Network, bez potrebe za deponovanjem sredstava On-Chain i zatim otvaranjem LN kanala.


Za nove korisnike, ovo su sjajne vesti jer bi trebalo da mogu da počnu od nule, direktno na LN. Da biste to uradili, jednostavno kreirajte LN Invoice sa glavnog ekrana na dugmetu "primi", unesite iznos, opis, itd., i platite sa drugog Wallet. Blixt će otvoriti kanal do 400k Sats po primljenoj transakciji. Možete otvoriti više kanala ako je potrebno.


Zanimljiv i koristan slučaj je sledeći: recimo da je vaš prvi primljeni iznos 200k. Blixt će otvoriti 400k Sats kanal sa već 200k (minus naknade za otvaranje) na vašoj strani, ali pošto još uvek imate 200k "prostora" dostupnog, možete primiti više. Tako će sledeća uplata, recimo 100k, stići direktno kroz ovaj kanal, bez dodatnih naknada, i još uvek imate 100k prostora za primanje više.


Ali ako odlučiš da primiš, recimo, 300k za treću uplatu, to će kreirati još jedan novi kanal od 400k i prebaciti tih 300k na tvoju stranu.


Ako ima previše zahteva, Blixt čvor može prilagoditi kapacitet kanala tokom otvaranja.


## Automatsko Otvaranje Kanala


U postavkama, korisnik može aktivirati ovu opciju i imati automatizovanu uslugu koja otvara kanale sa najboljim čvorovima i rutama na osnovu dostupnog balansa u On-Chain Wallet aplikacije Blixt. Ovo je korisna funkcija za nove korisnike koji nisu sigurni sa kojim čvorom da otvore kanal i/ili kako da otvore LN kanal. To je kao autopilot za LN.


**Zapamtite:** ova opcija se koristi samo jednom, kada kreirate svoj novi Blixt Wallet, i podrazumevano je omogućena. Dakle, ako novi korisnik skenira On-Chain QR kod na glavnom ekranu i deponuje svoj prvi Sats na taj Address, Blixt će automatski otvoriti kanal sa tim Sats, sa Blixt javnim čvorom.


## Dolazeće Usluge Likvidnosti


Funkcija posvećena trgovcima kojima je potrebna veća DOLAZNA likvidnost, laka za korišćenje. Da biste to uradili, jednostavno izaberite jednog od pružalaca likvidnosti sa liste, platite iznos koji želite za kanal, i navedite svoj ID čvora, i odatle će se otvoriti kanal ka vašem Blixt čvoru.


## Liste kontakata


Korisna funkcija ako želite da imate trajnu listu primalaca sa kojima najčešće trgujete. Ova lista može sadržati LNURL-ove, Lightning adrese ili buduće statične informacije o plaćanju/fakture. Za sada, ova lista ne može biti sačuvana van aplikacije, ali postoje planovi da se doda opcija za njen izvoz.


## LNURL i Lightning Address


Puna podrška za LNURL. Možete platiti na LNURL, LN-auth, LN-chan zahtev sa LNURL.

Možete poslati na bilo koji LN Address i takođe ga dodati u svoju listu kontakata.

Takođe počevši od verz. 0.6.9 dostupno je primanje na vaš sopstveni LN Address _@blixtwallet.com_ tip, putem [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box) funkcije.


## Keysend


Veoma moćna funkcija koju ima malo mobilnih novčanika. Možete poslati/gurnuti sredstva direktno kroz kanal ili usmeriti ka drugom čvoru, dodajući poruku ako je potrebno. To je kao tajni chat preko LN. Ova funkcija je veoma korisna za prikazivanje poruka na Amboss.space bilbordu ([ovde je vodič za ovaj Amboss bilbord](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).


## Potpisivanje poruka


Veoma koristan alat za potpisivanje poruka privatnim ključem vašeg Blixt čvora, autentifikaciju poruka i slično. Veoma malo mobilnih novčanika ima ovu funkciju, gotovo nijedan.


## Višekanalna Plaćanja - Višesmjerna Plaćanja (MPP)


Korisna funkcija za LN plaćanja, koja vam omogućava da podelite LN plaćanje na više delova, preko više kanala. To je dobar način da se balansira likvidnost na mreži i poboljša privatnost.


## Lightning Browser


Niz usluga trećih strana sa LN, organizovanih unutar jednostavnog, pristupačnog i korisnički prijateljskog pregledača. Takođe je dobar način za promociju preduzeća koja prihvataju BTC na LN. Ovo je funkcija koja će se dalje razvijati u budućnosti. Za sada, ne radi iza Tor-a, tako da će pregledanje ovih aplikacija biti u otvorenoj mreži (clearnet).


## Istraživači Dnevnika


Ovo je moćan alat za proveru LND logova i statusa vašeg čvora uopšte. Postoji opcija za čuvanje log fajla. Veoma je korisno imati ove logove pri ruci u slučaju da vam je potrebna pomoć programera u identifikaciji određenih problema.


## Bezbednost


Možete postaviti u postavkama aplikacije, za veću sigurnost vašeg Wallet/čvora, mogućnost pokretanja aplikacije pomoću PIN koda i/ili otiska prsta.


## On-Chain Wallet


Ova funkcija je malo skrivena, u meniju fioke u gornjem levom uglu. Pošto je retko koristi korisnik LN, nije vidljiva na glavnom ekranu. Ali to je u redu, možete je imati na posebnom Wallet gde možete upravljati adresama i pregledati dnevnik transakcija, uvozom vašeg seed na Sparrow na primer. Možda će u budućnosti, Blixt Wallet takođe uključivati funkciju za upravljanje UTxO-ima. Ali za sada, KORISTITE samo ovaj On-Chain Wallet za otvaranje ili zatvaranje kanala na LN.


## Posebne karakteristike



- Sa verzijom 0.6.9 uveden je "persistent mode" koji omogućava korisniku da pokreće Blixt kao uvek online LN čvor, održavajući LND usluge aktivnim i LN Wallet spremnim za primanje/slanje u bilo koje vreme.
- Jednostavni Taproot Kanali - omogućavaju otvaranje Taproot kanala za veću privatnost i napredne funkcije
- Kanali bez potvrde sa Blixt Dunder LSP
- Speedloader ("LN channel sync") - Ovo znači da će svi kanali biti brzo sinhronizovani pri pokretanju, za bolje pronalaženje puta. Iako je pomalo iritantno što morate videti ekran za sinhronizaciju na početku, to će osigurati da Wallet zna za sve kanale i da će plaćanja biti brža i pouzdanija.
- Prevedeno na 25+ jezika!


## "Easter Eggs"


Da, u aplikaciji Blixt postoje neke skrivene funkcije, sitnice koje čine aplikaciju šarmantnom, aktivirajući zabavne/zanimljive akcije i odgovore.

Savjet: pokušaj dvaput kliknuti na Blixt logo u ladici 🙂 Ostatak ću ti prepustiti da otkriješ.


# Blixt Početni Vodič Korak-po-Korak


**Savjet:** kao novi korisnik LN, ako počnete koristiti Blixt LN Node, prvo ćete morati znati šta je Lightning Network i kako funkcioniše, barem na osnovnom nivou. [Ovde smo sastavili jednostavnu listu resursa o Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Molimo vas da ih prvo pročitate.


Pokretanje punog LN čvora na mobilnom uređaju nije lak zadatak i može zauzeti nešto prostora (min 600MB) i memorije. Preporučujemo da imate dobar mobilni uređaj, ažuriran i da koristite barem Android 11 kao operativni sistem.


Kada otvorite Blixt, ekran „Dobrodošli“ će vam ponuditi nekoliko opcija:


![Demo Blixt 01](assets/blixt_t01.webp)


U gornjem desnom uglu videćete 3 tačke koje aktiviraju meni sa:



- „omogući Tor“ - korisnik može započeti sa Tor mrežom, posebno ako želi da obnovi stari LND čvor koji je radio samo sa Tor peer-ovima.
- „Postavi Bitcoin čvor“ - ako korisnik želi da se poveže direktno na svoj čvor, kako bi sinhronizovao blokove putem Neutrino-a, može to učiniti odmah sa početnog ekrana. Ova opcija je takođe dobra u slučaju da vaša internet konekcija ili Tor nisu dovoljno stabilni za povezivanje na podrazumevani Bitcoin čvor (node.blixtwallet.com).


## Prvi korak - Kreiraj novi Wallet


Ako odlučite da „kreirate novi Wallet“, bićete preusmereni direktno na glavni ekran Blixt Wallet.


Ovo je vaš “cockpit” i takođe je “Main LN Wallet”, pa imajte na umu da će vam prikazati samo stanje vašeg LN Wallet. Onchain Wallet je prikazan odvojeno (pogledajte C).


![Demo Blixt 02](assets/blixt_t02.webp)


A - Blixt blokira ikonu indikatora sinhronizacije. Ovo je najvažnija stvar za LN čvor: da bude sinhronizovan sa mrežom. Ako je ta ikona i dalje prisutna i radi, to znači da vaš čvor NIJE SPREMAN! Zato budite strpljivi, posebno za prvu inicijalnu sinhronizaciju. Može potrajati do 6-8 minuta, u zavisnosti od vašeg uređaja i internet veze.


Možete kliknuti na to i videti status sinhronizacije:


![Demo Blixt 03](assets/blixt_t03.webp)


Takođe možete kliknuti na dugme „Prikaži LND Log“ (A) ako želite da vidite i pročitate više tehničkih detalja LND loga, u realnom vremenu. Veoma je korisno za debagovanje i učenje više o tome kako LN funkcioniše.


B - Ovde možete pristupiti svim Blixt postavkama, i ima ih mnogo! Blixt nudi mnogo bogatih funkcija i opcija za upravljanje vašim LN čvorom kao profesionalac. Sve te opcije su detaljno objašnjene na [„Blixt Features Page - Options Menu“](https://blixtwallet.github.io/features#blixt-options).


C - Ovde imate meni „Magic Drawer“, takođe detaljno objašnjen ovde. Ovde je „Onchain Wallet“ (B), Lightning kanali (C), Kontakti, Ikona statusa kanala (A), Keysend (D).


![Demo Blixt 04](assets/blixt_t04.webp)


D - Je meni za pomoć, sa linkovima ka FAQ / Stranici sa vodičima, kontaktiranje programera, Github stranici i Telegram grupi za podršku.


E - Naznačite svoj prvi BTC Address, gde možete deponovati svoj prvi testni Sats. OVO JE OPCIONO! Ako deponujete direktno u taj Address, otvara se LN kanal prema Blixt Node. To znači da ćete videti svoj deponovani Sats, kako ide u drugu onchain transakciju (tx), za otvaranje tog LN kanala. To možete proveriti u Blixt onchain Wallet (pogledajte tačku C), klikom na gornji desni TX meni.


![Demo Blixt 05](assets/blixt_t05.webp)


Kao što možete videti u Onchain Transaction Log, koraci su veoma detaljni i pokazuju gde Sats idu (depozit, otvaranje, zatvaranje kanala)


**Preporuka:** nakon testiranja nekoliko situacija, došli smo do zaključka da je mnogo efikasnije otvarati kanale između 1 i 5 M Sats. Manji kanali imaju tendenciju da se brzo iscrpe i plaćaju veći % naknada u poređenju sa većim kanalima.


F - Naznačite svoj glavni Lightning Wallet saldo. Ovo NIJE vaš ukupni Blixt Wallet saldo, već predstavlja samo Sats koji imate u Lightning kanalima, dostupan za slanje. Kao što je ranije navedeno, Onchain Wallet je odvojen. Imajte na umu ovaj aspekt. Onchain Wallet je odvojen iz važnog razloga: koristi se uglavnom za otvaranje/zatvaranje LN kanala.


U redu, sada ste deponovali neki Sats u taj onchain Address prikazan na glavnom ekranu. Preporučuje se da kada to uradite, držite vašu Blixt aplikaciju online i aktivnom neko vreme, dok BTC tx ne bude uzet od strane rudara u prvi blok.


Nakon toga može potrajati do 20-30 minuta dok se potpuno ne potvrdi i kanal ne bude otvoren, a videćete ga u Magic Drawer - Lightning Channels kao aktivan. Takođe, mala obojena tačka na vrhu fioke, ako je Green, će ukazivati da je vaš LN kanal online i spreman za korišćenje za slanje Sats preko LN.


Address i poruka dobrodošlice koja se prikazuje će nestati. Nema više potrebe za otvaranjem automatskog kanala sada. Takođe možete deaktivirati opciju u meniju Podešavanja.


Vreme je da se krene dalje, testirajući druge funkcije i opcije za otvaranje LN kanala.


Sada, hajde da otvorimo još jedan kanal sa drugim čvorom. Blixt zajednica je sastavila [listu dobrih čvorova za početak korišćenja sa Blixt.](https://github.com/hsjoberg/blixt-Wallet/issues/1033)


### Postupak za otvaranje normalnog nenajavljenog (privatnog) LN kanala u vašem Blixt mobilnom čvoru


Ovo je vrlo jednostavno, potrebno je samo nekoliko koraka i malo strpljenja:



- Idite na [Blixt Community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) dobrih partnera
- Odaberite čvor i kliknite na vezu naslova njegovog imena, otvoriće se njegova Amboss stranica.
- Kliknite da prikažete QR kod za URI čvora Address


![Demo Blixt 06](assets/blixt_t06.webp)


Sada, otvori Blixt i idi do gornje fioke - Lightning Channels i klikni na dugme „+”


![Demo Blixt 07](assets/blixt_t07.webp)


Sada kliknite na (A) kameru da skenirate QR kod sa Amboss stranice i detalji čvora će biti popunjeni. Dodajte iznos Sats za kanal koji želite, a zatim odaberite stopu naknade za tx. Možete ostaviti automatski (B) za bržu potvrdu ili ga ručno prilagoditi pomeranjem dugmeta. Takođe možete dugo pritisnuti broj i urediti ga kako želite.


Ne stavljajte manje od 1 sat/vbyte! Obično je bolje [konsultovati Mempool naknade](https://Mempool.space/) pre otvaranja kanala i odabrati odgovarajuću naknadu.


Gotovo, sada samo kliknite na dugme „open channel“ i sačekajte 3 potvrde, što obično traje 30 min (1 blok otprilike svakih 10 min).


Jednom kada bude potvrđeno, videćete kanal aktivan u vašem odeljku „Lightning Channels“.


## Drugi korak - Dobijte više dolazne likvidnosti


Ok, sada imamo LN kanal sa samo IZLAZNOM likvidnošću. To znači da možemo samo SLATI, još uvek ne možemo PRIMATI Sats preko LN. Zašto? Da li ste pročitali vodiče navedene na početku? Ne? Vratite se i pročitajte ih. Veoma je važno razumeti kako LN kanali funkcionišu.


![Demo Blixt 08](assets/blixt_t08.webp)


Kao što možete videti u ovom primeru, kanal otvoren sa prvim depozitom nema previše PRILIVNE likvidnosti („Može primiti“), ali ima mnogo ODLAZNE likvidnosti („Može poslati“).


Dakle, koje opcije imate, ako želite da primite više Sats nego LN?



- Potrošite nešto Sats iz postojećeg kanala. Da, LN je platna mreža Bitcoin, koja se uglavnom koristi za brže, jeftinije, privatno i lako trošenje vašeg Sats. LN NIJE način za čuvanje, za to imate onchain Wallet.
- Zamenite neke Sats nazad u vaš onchain Wallet koristeći uslugu submarine swap. Na ovaj način ne trošite vaše Sats, već ih vraćate nazad na vaš onchain Wallet. Ovde možete videti detalje nekih metoda, na [Blixt Guides Page](https://blixtwallet.github.io/guides).
- Otvorite INBOUND kanal od bilo kog LSP provajdera. Ovde je video demo o [kako koristiti LNBig LSP za otvaranje inbound kanala](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). To znači da ćete platiti malu naknadu za PRAZAN kanal (na vašoj strani) i moći ćete da primate više Sats u taj kanal. Ako ste trgovac koji prima više nego što troši, to je dobra opcija. Takođe, ako kupujete Sats preko LN, koristeći Robosats ili bilo koji drugi LN Exchange.
- Otvorite Dunder kanal, sa Blixt čvorom ili bilo kojim drugim Dunder LSP provajderom. Dunder kanal je jednostavan način da dobijete nešto PRILIVNE likvidnosti, ali u isto vreme deponujete nešto Sats u taj kanal. Takođe je dobro jer će otvoriti kanal sa [UTXO](https://en.Bitcoin.it/wiki/UTXO) koji nije iz vašeg Blixt Wallet. To dodaje malo privatnosti.

Je takođe dobro jer, ako nemate Sats u onchain Wallet, da otvorite normalan LN kanal, ali ih imate u drugom LN Wallet, možete jednostavno platiti iz tog drugog Wallet kroz LN otvaranje i depozit (sa vaše strane) tog Dunder kanala. [Više detalja o tome kako Dunder funkcioniše i kako pokrenuti sopstveni server ovde.](https://github.com/hsjoberg/dunder-lsp)


![Demo Blixt 09](assets/blixt_t09.webp)


Evo koraka kako aktivirati otvaranje Dunder kanala:



- Idite na Podešavanja, u odeljku „Eksperimenti“ aktivirajte polje za „Omogući Dunder LSP“.
- Jednom kada to uradite, vratite se na odeljak “Lightning Network” i videćete da se pojavila opcija “Set Dunder LSP Server”. Tamo je po defaultu postavljeno “https://dunder.blixtwallet.com” ali možete ga promeniti sa bilo kojim drugim Dunder LSP provajderom Address. [Ovde je lista Blixt zajednice](https://github.com/hsjoberg/blixt-Wallet/issues/1033) sa čvorovima koji mogu obezbediti Dudner LSP kanale za vaš Blixt.
- Sada možete otići na glavni ekran i kliknuti na dugme „Primi“. Zatim sledite ovu proceduru objašnjenu [u ovom vodiču](https://blixtwallet.github.io/guides#guide-lsp).


Ok, tako da nakon što je Dunder kanal potvrđen (trajaće nekoliko minuta) završićeš sa 2 LN kanala: jedan otvoren inicijalno sa autopilotom (kanal A) i jedan sa više dolazne likvidnosti, otvoren sa Dunderom (kanal B).


![Demo Blixt 10](assets/blixt_t10.webp)


Dobro, sada ste spremni za slanje i primanje dovoljno Sats preko LN !


## Treći korak - Procedura za vraćanje čvora


Dakle, sada hajde da razgovaramo o tome kako da obnovimo Blixt Wallet ili bilo koji drugi LND čvor koji je pao. Ovo je malo tehničkije, ali molim vas obratite pažnju. Nije to Hard.


**Podsetnik:** ranije sam napisao poseban vodič sa više opcija [kako obnoviti srušeni LND čvor](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), gde sam takođe spomenuo metodu korišćenja Blixt kao brzog procesa obnove, koristeći seed + channel.backup fajl sa vašeg mrtvog LND čvora. Takođe sam napisao vodič kako obnoviti vaš Blixt čvor ili migrirati vaš Blixt na drugi uređaj, [ovde](https://blixtwallet.github.io/faq#blixt-restore).


![Demo Blixt 11](assets/blixt_t11.webp)


Ali objasnimo ovaj proces u jednostavnim koracima. Kao što možete videti na slici iznad, postoje 2 stvari koje treba da uradite da biste vratili vaš prethodni Blixt/LND čvor:



- gornja kutija je mesto gde morate uneti svih 24 reči sa vašeg seed (stari / mrtvi čvor)
- dno su dve opcije dugmeta za umetanje / otpremanje channel.backup datoteke, prethodno sačuvane sa vašeg starog Blixt/LND čvora. Može biti iz lokalne datoteke (prethodno je otpremite na svoj uređaj) ili može biti sa udaljene lokacije na Google drive / iCloud. Blixt ima ovu opciju da sačuva rezervnu kopiju vaših kanala direktno na Google / iCloud drive. Pogledajte više detalja na [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Ipak, ako ranije niste imali otvorene LN kanale, nema potrebe da otpremate bilo kakav channels.backup fajl. Jednostavno unesite 24 reči seed i pritisnite dugme za vraćanje.


Ne zaboravite da aktivirate Tor, iz menija sa 3 tačke na vrhu, kao što smo objasnili u poglavlju "Prvi korak" ovog vodiča. To je slučaj kada imate SAMO Tor peer-ove i ne možete biti kontaktirani preko clearnet-a (domena/IP). U suprotnom nije potrebno.


Još jedna korisna funkcija je postavljanje specifičnog Bitcoin čvora iz tog gornjeg menija. Po defaultu sinhronizuje blokove sa node.blixtwallet.com (neutrino mod), ali možete postaviti bilo koji drugi Bitcoin čvor koji pruža neutrino sinhronizaciju.


Dakle, kada popunite te opcije i pritisnete dugme za vraćanje, Blixt će prvo početi da sinhronizuje blokove putem Neutrino-a, kao što smo objasnili u poglavlju "Prvi korak" ovog vodiča. Budite strpljivi i pratite proces vraćanja na glavnom ekranu, klikom na ikonu za sinhronizaciju.


![Demo Blixt 12](assets/blixt_t12.webp)


Kao što možete videti u ovom primeru, pokazuje da su Bitcoin blokovi 100% sinhronizovani (A) i da je proces oporavka u toku (B). To znači da će LN kanali koje ste ranije imali biti zatvoreni i sredstva vraćena u vaš Blixt onchain Wallet.


Ovaj proces zahteva vreme! Zato vas molimo da budete strpljivi i pokušate da održite vaš Blixt aktivnim i online. Početna sinhronizacija može potrajati do 6-8 minuta, a zatvaranje kanala može potrajati do 10-15 minuta. Zato je bolje da uređaj bude dobro napunjen.


Jednom kada ovaj proces započne, možete proveriti u Magic Drawer - Lightning Channels, status svakog od vaših prethodnih kanala, pokazujući da su u statusu "pending to close". Kada se svaki kanal zatvori, možete videti closing tx u onchain Wallet (pogledajte Magic Drawer - Onchain), i otvoriti tx menu log.


![Demo Blixt 13](assets/blixt_t13.webp)


Takođe će biti dobro da proverite i dodate, ako već nisu tamo, vaše prethodne peer-ove koje ste imali na vašem starom LN čvoru. Dakle, idite na meni Podešavanja, dole do “Lightning Network” i uđite u opciju “Prikaži Lightning Peers”.


![Demo Blixt 14](assets/blixt_t14.webp)


Unutar sekcije videćete čvorove na koje ste trenutno povezani i možete dodati još, bolje je dodati one sa kojima ste već imali kanale. Samo idite na Amboss stranicu, potražite alias ili nodeID vaših čvorova i skenirajte njihov node URI.


![Demo Blixt 15](assets/blixt_t15.webp)


Kao što možete videti na slici iznad, postoje 3 aspekta:


A - predstavlja clearnet čvor Address URI (domen/IP)


B - predstavlja Tor onion čvor Address URI (.onion)


C - je QR kod za skeniranje vašom Blixt kamerom ili dugme za kopiranje.


Ovaj čvor Address URI morate dodati na svoju listu partnera. Dakle, imajte na umu da nije dovoljno samo ime aliasa čvora ili nodeID.


Sada možete otići na Magic Drawer (gornji levi meni) - Lightning Channels, i možete videti na kojoj visini bloka dospeća će sredstva biti vraćena na vaš onchain Address.


![Demo Blixt 16](assets/blixt_t16.webp)


Taj blok broj 764272 je kada će sredstva biti upotrebljiva u vašem Bitcoin onchain Address. I može potrajati do 144 bloka od 1. bloka potvrde dok ne budu oslobođena. Zato proverite to u [the Mempool](https://Mempool.space/).


I to je to. Samo strpljivo čekajte dok svi kanali ne budu zatvoreni i sredstva se vrate u vaš onchain Wallet.


## Četvrti korak - Prilagođavanje


Ovo poglavlje se bavi prilagođavanjem i boljim upoznavanjem vašeg Blixt Node-a. Neću opisivati sve dostupne funkcije, ima ih previše i već su objašnjene na [Blixt Features Page](https://blixtwallet.github.io/features).


Ali ću istaći neke od onih koji su neophodni za napredovanje koristeći vaš Blixt i imati sjajno iskustvo.


### A - Ime (NameDesc)


![Demo Blixt 17](assets/blixt_t17.webp)


[The NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) je standard za prenošenje "imena primaoca" u BOLT11 fakturama.


Ovo može biti bilo koje ime i može se promeniti u bilo kom trenutku.


Ova opcija je zaista korisna u raznim slučajevima, kada želite poslati ime zajedno sa opisom Invoice, tako da primalac može imati nagoveštaj od koga je primio te Sats. Ovo je potpuno opciono i takođe na ekranu za plaćanje, korisnik mora označiti polje koje ukazuje na slanje alias imena.


Evo kako bi izgledalo kada koristite [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![Demo Blixt 18](assets/blixt_t18.webp)


Ovo je još jedan primer slanja na drugu Wallet aplikaciju koja podržava NameDesc:


![Demo Blixt 19](assets/blixt_t19.webp)


### B - Backup LN Kanali i seed reči


Ovo je veoma važna funkcija!


Nakon otvaranja ili zatvaranja LN kanala treba da napravite rezervnu kopiju. To se može uraditi ručno čuvanjem male datoteke na lokalnom uređaju (obično u folderu za preuzimanje) ili korišćenjem Google Drive ili iCloud naloga.


![Demo Blixt 20](assets/blixt_t20.webp)


Idite na Blixt Settings - Wallet sekciju. Tamo imate opcije za čuvanje svih važnih podataka za vaš Blixt Wallet:



- „Show Mnemonic“ - će prikazati 24 reči seed da ih zapišete
- „Ukloni Mnemonic sa uređaja“ - ovo je opcionalno i koristite ga samo ako zaista želite da uklonite seed reči sa svog uređaja. Ovo NEĆE obrisati vaš Wallet, samo seed. Ali budite oprezni! Ne postoji način da ih povratite ako ih prvo niste zapisali.
- „Izvezi rezervnu kopiju kanala“ - ova opcija će sačuvati malu datoteku na vašem lokalnom uređaju, obično u folder „preuzimanja“, odakle je možete uzeti i premestiti van vašeg uređaja, radi sigurnog čuvanja.
- „Verify channel backup“ - ovo je dobra opcija ako koristite Google drive ili iCloud da proverite integritet bekapa urađenog na daljinu.
- „Google drive channel backup“ - će sačuvati rezervnu kopiju u vašem ličnom Google drive-u. Datoteka je šifrovana i čuva se u posebnom skladištu odvojeno od vaših uobičajenih google datoteka. Dakle, nema brige da je neko može pročitati. U svakom slučaju, ta datoteka je potpuno beskorisna bez seed reči, tako da niko ne može uzeti vaša sredstva samo iz te datoteke.


Preporučio bih za ovaj deo sledeće:



- koristite menadžer lozinki da bezbedno sačuvate vaš seed i rezervnu kopiju fajla. [KeePass](https://keepass.info/) ili Bitwarden su veoma dobri za to i mogu se koristiti na više platformi i samostalno hostovati ili offline.
- URADITE BEKAP SVAKI PUT kada otvorite ili zatvorite kanal. Taj fajl se ažurira sa informacijama o kanalima. Nema potrebe da to radite nakon svake transakcije koju ste obavili na LN. Bekap kanala ne čuva te informacije, već samo status kanala.


![Demo Blixt 21](assets/blixt_t21.webp)


## Zaključak


Ok, postoje mnoge druge neverovatne funkcije koje Blixt nudi, prepustiću tebi da ih otkrivaš jednu po jednu i zabaviš se.


Ova aplikacija je zaista potcenjena, uglavnom zato što nije podržana od strane bilo kakvog VC finansiranja, vođena je zajednicom, izgrađena s ljubavlju i strašću za Bitcoin i Lightning Network.


Ovaj mobilni LN čvor, Blixt je veoma moćan alat u rukama mnogih korisnika, ako znaju kako da ga dobro koriste. Samo zamislite, šetate svetom sa LN čvorom u svom džepu i niko to neće znati.


I ne govorimo o svim drugim bogatim funkcijama koje dolaze uz to, koje vrlo malo ili nijedna druga Wallet aplikacija ne može ponuditi.


Nadam se da uživaš u korišćenju. Lično, obožavam ga i veoma mi je koristan (pogledaj ovde primer upotrebe gde je ovaj Wallet sjajan alat).


SREĆAN Bitcoin MUNJA!


Neka ₿ITCOIN bude s tobom!


**Odricanje od odgovornosti:** Nisam plaćen niti podržan na bilo koji način od strane programera ove aplikacije. Napisao sam ovaj vodič jer sam primetio da interesovanje za ovu Wallet aplikaciju raste, a novi korisnici i dalje ne razumeju kako da počnu sa njom. Takođe, da pomognem Hampus-u (glavnom programeru) sa dokumentacijom o korišćenju ovog čvora Wallet. Nemam nikakav drugi interes u promovisanju ove LN aplikacije, osim da podržim usvajanje Bitcoin i LN. Ovo je jedini način!