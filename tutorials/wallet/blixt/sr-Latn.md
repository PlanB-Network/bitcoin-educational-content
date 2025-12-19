---
name: Blixt Wallet
description: Kako početi koristiti moćan LN čvor na svom mobilnom uređaju?
---
![cover](assets/cover.webp)


Ovaj vodič je posvećen svim novim korisnicima koji žele početi koristiti Bitcoin Lightning Network (LN) na BESPLATAN, OPEN SOURCE, POTPUNO NE-KUSTODIJALAN način.


Korišćenje [Blixt Wallet](https://blixtwallet.com/), punog LN čvora na vašem mobilnom uređaju, gde god da se nalazite.


Ako nikada niste koristili Bitcoin Lightning Network, pre nego što počnete, [molimo pročitajte ovo jednostavno objašnjenje analogije o Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## VAŽNI ASPEKTI:



- Blixt je privatni čvor, NE rutirajući čvor! Imajte to na umu: To znači da će svi LN kanali u Blixt-u biti neobjavljeni u LN grafu (tzv. privatni kanali). To znači, OVAJ ČVOR NEĆE RUTIRATI plaćanja drugih kroz Blixt čvor. Ovaj Blixt čvor NIJE za rutiranje, ponavljam. Uglavnom je da možete upravljati svojim LN kanalima i obavljati svoja LN plaćanja privatno, kad god vam zatreba. Ovaj Blixt čvor je potrebno da bude online i sinhronizovan SAMO PRE nego što ćete obaviti svoje transakcije. Zato ćete videti ikonu na vrhu koja pokazuje status sinhronizacije. Potrebno je samo nekoliko trenutaka, u zavisnosti od toga koliko dugo ste ga držali offline.



- Blixt koristi LND (aezeed) kao Wallet backend, tako da ne pokušavajte da uvezete druge tipove Bitcoin novčanika u njega. [Ovde su objašnjeni tipovi Wallet Mnemonic seedova](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). A ovde je [opsežnija lista svih tipova novčanika](https://walletsrecovery.org/). Dakle, ako ste ranije imali LND čvor, možete uvesti seed i backup.channels u Blixt, [kako je objašnjeno u ovom vodiču](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Na kraju ovog vodiča pronaći ćete poseban odeljak sa ["saveti i trikovi"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt važni linkovi - pogledajte ih na kraju ovog vodiča, molimo vas da ih dodate u obeleživače.


---

## Blixt - First Contact


Dakle… Darthova mama je odlučila da počne koristiti LN sa Blixtom. Odluka Hard, ali mudra. Blixt je samo za pametne ljude i one koji zaista žele da nauče više, duboko korišćenje LN.


![blixt](assets/en/01.webp)


Dart upozorava svoju mamu:


"*Mama, ako počneš koristiti Blixt LN Node, prvo ćeš morati znati šta je Lightning Network i kako funkcioniše, barem na osnovnom nivou. [Ovde sam sastavio jednostavnu listu resursa o Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Molim te, pročitaj ih prvo.*"


Darthova mama je pročitala resurse i napravila svoj prvi korak: instalirala je Blixt na svoj potpuno novi Android uređaj. Blixt je takođe dostupan za iOS i macOS (desktop). Ali ti nisu za Darthovu mamu... Ipak, preporučuje se korišćenje novije verzije Androida, barem 9 ili 10, za bolju kompatibilnost i iskustvo. Pokretanje punog LN čvora na mobilnom uređaju nije lak zadatak i može zauzeti dosta prostora (minimum 600MB) i memorije.


Kada otvorite Blixt, ekran „Dobrodošli“ će vam ponuditi neke opcije:


![blixt](assets/en/02.webp)


U gornjem desnom uglu videćete 3 tačke koje aktiviraju meni sa:



- „omogući Tor“ - korisnik može započeti sa Tor mrežom, posebno ako želi da obnovi stari LND čvor koji je radio samo sa Tor peer-ovima.
- „Postavi Bitcoin čvor“ - ako korisnik želi da se poveže direktno na svoj čvor, kako bi sinhronizovao blokove putem Neutrino-a, može to učiniti odmah sa početnog ekrana. Ova opcija je takođe dobra u slučaju da vaša internet konekcija ili Tor nisu dovoljno stabilni za povezivanje na podrazumevani Bitcoin čvor (node.blixtwallet.com).
- Uskoro će biti dodat jezik tamo, tako da korisnik može odmah početi sa jezikom koji mu je ugodan. Ako želite da doprinesete ovom projektu otvorenog koda prevodima na druge jezike, [molimo pridružite se ovde](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPCIJA A - Kreiraj novi Wallet


Ako odlučite da „kreirate novi Wallet“, bićete preusmereni direktno na glavni ekran Blixt Wallet.


Ovo je vaš „cockpit“ i takođe je „Main LN Wallet“, pa budite svesni, prikazivaće vam samo stanje vašeg LN Wallet. Onchain Wallet je prikazan zasebno (vidi C).


![blixt](assets/en/03.webp)


A - Blixt blokira ikonu indikatora sinhronizacije. Ovo je najvažnija stvar za LN čvor: da bude sinhronizovan sa mrežom. Ako ta ikona još uvek radi, znači da vaš čvor NIJE SPREMAN! Zato budite strpljivi, posebno za prvu inicijalnu sinhronizaciju. Može potrajati do 6-8 minuta, u zavisnosti od vašeg uređaja i internet konekcije.


Možete kliknuti na to i videti status sinhronizacije:


![blixt](assets/en/04.webp)


Takođe možete kliknuti na dugme „Prikaži LND log“ (A) ako želite da vidite i pročitate više tehničkih detalja LND loga, u realnom vremenu. Veoma je korisno za otklanjanje grešaka i učenje više o tome kako LN funkcioniše.


B - Ovde možete pristupiti svim Blixt postavkama, i ima ih mnogo! Blixt nudi mnoge bogate funkcije i opcije za upravljanje vašim LN čvorom kao profesionalac. Sve te opcije su detaljno objašnjene na “[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu”.


C - Ovde imate meni „Magic Drawer“, [detaljno objašnjen ovde](https://blixtwallet.github.io/features#blixt-drawer). Ovde je „Onchain Wallet“ (B), Lightning Kanali (C), Kontakti, Ikona statusa kanala (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Je meni za pomoć, sa linkovima ka FAQ / stranici sa vodičima, kontaktiranje programera, Github stranici i Telegram grupi za podršku.


E - Naznačite svoj prvi BTC Address, gde možete deponovati svoj prvi testni Sats. OVO JE OPCIONO! Ako deponujete direktno u taj Address, otvara se LN kanal prema Blixt Node. To znači da ćete videti vaš deponovani Sats, kako ide u drugu onchain transakciju (tx), za otvaranje tog LN kanala. To možete proveriti u Blixt onchain Wallet (pogledajte tačku C), klikom na gornji desni TX meni.


![blixt](assets/en/06.webp)


Kao što možete videti u Onchain Transaction Log, koraci su veoma detaljni i pokazuju gde Sats idu (depozit, otvaranje, zatvaranje kanala).


PREPORUKA:


Nakon testiranja nekoliko situacija, došli smo do zaključka da je mnogo bolje efikasno otvarati kanale između 1 i 5 M Sats. Manji kanali imaju tendenciju da se brzo iscrpe i plaćaju viši % naknada u poređenju sa većim kanalima.


F - Naznačite svoj glavni Lightning Wallet saldo. Ovo NIJE vaš ukupni Blixt Wallet saldo, već predstavlja samo Sats koji imate u Lightning kanalima, dostupan za slanje. Kao što je ranije naznačeno, Onchain Wallet je odvojen. Imajte na umu ovaj aspekt. Onchain Wallet je odvojen iz važnog razloga: koristi se uglavnom za otvaranje/zatvaranje LN kanala.


Ok, dakle sada je Darthova mama uplatila neki Sats u onchain Address prikazan na glavnom ekranu. Preporučuje se da kada to uradite, držite Blixt aplikaciju online i aktivnom neko vreme, dok BTC transakciju ne preuzmu rudari u prvi blok.


Nakon toga može potrajati do 20-30 minuta dok se potpuno ne potvrdi i kanal ne bude otvoren, a videćete ga u Magic Drawer - Lightning Channels kao aktivan. Takođe, mala obojena tačka na vrhu fioke, ako je Green, pokazaće da je vaš LN kanal online i spreman za korišćenje za slanje Sats preko LN.


Address i poruka dobrodošlice koja se prikazuje će nestati. Nema više potrebe za otvaranjem automatskog kanala sada. Takođe možete deaktivirati opciju u meniju Podešavanja.


Vreme je da krenemo dalje, testirajući druge funkcije i opcije za otvaranje LN kanala.


Sada, hajde da otvorimo još jedan kanal sa drugim čvorom. Blixt zajednica je sastavila [listu dobrih čvorova za početak korišćenja sa Blixtom](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Procedura za otvaranje LN kanala u Blixt**


Ovo je veoma jednostavno, potrebno je samo nekoliko koraka i malo strpljenja:



- Idite na [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033) listu partnera
- Odaberite čvor i kliknite na njegov naslovni link, otvoriće se njegova Amboss stranica.
- Kliknite da prikažete QR kod za URI čvora Address


![blixt](assets/en/07.webp)


Otvorite Blixt i idite do gornje fioke - Lightning Kanali i kliknite na dugme „+“


![blixt](assets/en/08.webp)


Sada kliknite na (A) kameru da skenirate QR kod sa Amboss stranice i detalji čvora će biti popunjeni. Dodajte iznos Sats za kanal koji želite, a zatim odaberite stopu naknade za tx. Možete ga ostaviti na auto (B) za bržu potvrdu ili ga ručno prilagoditi pomeranjem dugmeta. Takođe možete dugo pritisnuti broj i urediti ga kako želite.


Ne stavljajte manje od 1 sat/vbyte! Obično je bolje konsultovati [Mempool fees](https://Mempool.space/) pre otvaranja kanala i odabrati odgovarajuću naknadu.


Gotovo, sada samo kliknite na dugme „open channel“ i sačekajte 3 potvrde, što obično traje 30 min (1 blok otprilike svakih 10 min).


Jednom kada bude potvrđeno, videćete kanal aktivan u vašem odeljku „Lightning Channels“.


---

## Blixt - Drugi Kontakt


Ok, sada imamo LN kanal sa samo OUTBOUND likvidnošću. To znači da možemo samo SLATI, još uvek ne možemo PRIMATI Sats preko LN.


![blixt](assets/en/09.webp)


Zašto? Da li ste pročitali vodiče navedene na početku? Ne? Vratite se i pročitajte ih. Veoma je važno razumeti kako LN kanali funkcionišu.


![blixt](assets/en/10.webp)


Kao što možete videti u ovom primeru, kanal otvoren sa prvim depozitom nema previše PRILIVNE likvidnosti („Može primiti“), ali ima mnogo ODILIVNE likvidnosti („Može poslati“).


Dakle, koje opcije imate, ako želite da primite više Sats nego LN?



- Potrošite malo Sats iz postojećeg kanala. Da, LN je platna mreža Bitcoin, koja se uglavnom koristi za brže, jeftinije, privatno i jednostavno trošenje vašeg Sats. LN NIJE način za čuvanje, za to imate onchain Wallet.



- Zamenite neki Sats nazad u vaš onchain Wallet koristeći uslugu podmorskog swap-a. Na ovaj način ne trošite vaš Sats, već ga vraćate nazad u vaš onchain Wallet. Ovde možete videti detalje nekih metoda na [Blixt Guides Page](https://blixtwallet.github.io/guides).



- Otvorite INBOUND kanal od bilo kog LSP provajdera. Ovde je video demo o tome kako koristiti LNBig LSP za otvaranje inbound kanala. To znači da ćete platiti malu naknadu za PRAZAN kanal (sa vaše strane) i moći ćete da primate više Sats u taj kanal. Ako ste trgovac koji prima više nego što troši, to je dobra opcija. Takođe, ako kupujete Sats preko LN, koristeći Robosats ili bilo koji drugi LN Exchange.



- Otvorite Dunder kanal, sa Blixt čvorom ili bilo kojim drugim Dunder LSP provajderom. Dunder kanal je jednostavan način da dobijete neku PRILIVNU likvidnost, ali u isto vreme deponujete neki Sats u taj kanal. Takođe je dobro jer će otvoriti kanal sa [UTXO](https://en.Bitcoin.it/wiki/UTXO) koji nije iz vašeg Blixt Wallet. To dodaje malo privatnosti. Takođe je dobro jer, ako nemate Sats u onchain Wallet, da otvorite normalan LN kanal, ali ih imate u drugom LN Wallet, možete jednostavno platiti iz tog drugog Wallet kroz LN otvaranje i depozit (sa vaše strane) tog Dunder kanala. [Više detalja o tome kako Dunder funkcioniše i kako pokrenuti sopstveni server ovde](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Evo koraka za aktiviranje otvaranja Dunder kanala:



- Idite na Podešavanja, u odeljku „Eksperimenti“ aktivirajte polje za „Omogući Dunder LSP“.
- Jednom kada to uradite, vratite se na odeljak “Lightning Network” i videćete da se pojavila opcija “Set Dunder LSP Server”. Tamo je po defaultu postavljeno “https://dunder.blixtwallet.com” ali možete promeniti sa bilo kojim drugim Dunder LSP provajderom Address. [Ovde je lista Blixt zajednice](https://github.com/hsjoberg/blixt-Wallet/issues/1033) sa čvorovima koji mogu obezbediti Dudner LSP kanale za vaš Blixt.
- Sada možete otići na glavni ekran i kliknuti na dugme „Primi“. Zatim pratite ovu proceduru [objašnjenu u ovom vodiču](https://blixtwallet.github.io/guides#guide-lsp).


OK, tako da nakon što je Dunder kanal potvrđen (trajaće nekoliko minuta) završićete sa 2 LN kanala: jedan otvoren inicijalno sa autopilotom (kanal A) i jedan sa više dolazne likvidnosti, otvoren sa Dunderom (kanal B).


![blixt](assets/en/12.webp)


Dobro, sada ste spremni za slanje i primanje dovoljno Sats preko LN !


SREĆAN Bitcoin MUNJA!


---

## Blixt - Treći Kontakt


Zapamtite, u poglavlju jedan „Prvi kontakt“ bile su 2 opcije na ekranu dobrodošlice:


- [Opcija A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Kreiraj novi Wallet
- Opcija B - Vratiti Wallet


Dakle, sada hajde da razgovaramo o tome kako da obnovimo Blixt Wallet ili bilo koji drugi LND čvor koji je pao. Ovo je malo tehničkije, ali molim vas obratite pažnju. Nije to Hard.


### OPCIJA B - Vrati Wallet


U prošlosti sam napisao poseban vodič o [kako obnoviti srušeni Umbrel čvor](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), gde sam takođe spomenuo metodu korišćenja Blixt-a kao brzog procesa obnove, koristeći seed + channel.backup datoteku iz Umbrel-a.


Takođe sam napisao vodič kako da povratite vaš Blixt čvor ili migrirate vaš Blixt na drugi uređaj, [ovde](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Ali objasnimo ovaj proces u jednostavnim koracima. Kao što možete videti na slici iznad, postoje 2 stvari koje treba da uradite da biste vratili vaš prethodni Blixt/LND čvor:



- gornja kutija je mesto gde morate uneti svih 24 reči sa vašeg seed (stari / neaktivan čvor)
- na dnu su dve opcije dugmeta za umetanje / otpremanje channel.backup fajla, prethodno sačuvanog sa vašeg starog Blixt/LND čvora. Može biti iz lokalne datoteke (koju ste prethodno otpremili na svoj uređaj) ili može biti sa udaljene lokacije na Google drive / iCloud. Blixt ima ovu opciju da sačuva rezervnu kopiju vaših kanala direktno na Google / iCloud drive. Pogledajte više detalja na [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Ipak, ako ranije niste imali otvorene LN kanale, nema potrebe da otpremate bilo kakav channels.backup fajl. Jednostavno unesite 24 reči seed i pritisnite dugme za obnavljanje.


Ne zaboravite da aktivirate Tor, iz menija sa 3 tačke na vrhu, kao što smo objasnili u odeljku Opcija A. To je slučaj kada imate SAMO Tor peer-ove i ne možete biti kontaktirani preko clearnet-a (domen/IP). U suprotnom nije neophodno.


Još jedna korisna funkcija je postavljanje specifičnog Bitcoin čvora iz tog gornjeg menija. Podrazumevano sinhronizuje blokove sa node.blixtwallet.com (neutrino režim), ali možete postaviti bilo koji drugi Bitcoin čvor koji pruža neutrino sinhronizaciju.


Dakle, kada popunite te opcije i pritisnete dugme za vraćanje, Blixt će prvo početi da sinhronizuje blokove putem Neutrino-a, kao što smo objasnili u poglavlju Prvi Kontakt. Budite strpljivi i pratite proces vraćanja na glavnom ekranu, klikom na ikonu za sinhronizaciju.


![blixt](assets/en/14.webp)


Kao što možete videti u ovom primeru, pokazuje da su Bitcoin blokovi 100% sinhronizovani (A) i da je proces oporavka u toku (B). To znači da će LN kanali koje ste prethodno imali biti zatvoreni i sredstva vraćena u vaš Blixt onchain Wallet.


Ovaj proces zahteva vreme! Zato vas molimo da budete strpljivi i pokušajte da vaš Blixt bude aktivan i online. Početna sinhronizacija može trajati do 6-8 minuta, a zatvaranje kanala može trajati do 10-15 minuta. Zato je bolje da uređaj bude dobro napunjen.


Jednom kada ovaj proces započne, možete proveriti u Magic Drawer - Lightning Channels, status svakog od vaših prethodnih kanala, pokazujući da su u statusu "pending to close". Kada se svaki kanal zatvori, možete videti closing tx u onchain Wallet (pogledajte Magic Drawer - Onchain), i otvoriti tx meni log.


![blixt](assets/en/15.webp)


Takođe će biti dobro da proverite i dodate, ako već nisu tamo, vaše prethodne čvorove koje ste imali u vašem starom LN čvoru. Dakle, idite na meni Podešavanja, dole do “Lightning Network” i uđite u opciju “Prikaži Lightning čvorove”.


![blixt](assets/en/16.webp)


Unutar sekcije ćete videti vršnjake sa kojima ste povezani u tom trenutku i možete dodati još, bolje je dodati one sa kojima ste već imali kanale. Samo idite na [Amboss stranicu](https://amboss.space/), potražite alias vaših vršnjačkih čvorova ili nodeID i skenirajte njihov node URI.


![blixt](assets/en/17.webp)


Kao što možete videti na slici iznad, postoje 3 aspekta:


A - predstavlja clearnet čvor Address URI (domen/IP)


B - predstavlja Tor onion čvor Address URI (.onion)


C - je QR kod za skeniranje vašom Blixt kamerom ili dugme za kopiranje.


Ovaj čvor Address URI morate dodati na svoju listu partnera. Dakle, imajte na umu da nije dovoljno samo ime aliasa čvora ili nodeID.


Sada možete otići na Magic Drawer (meni u gornjem levom uglu) - Lightning Channels, i možete videti na kojoj visini bloka dospeća će sredstva biti vraćena u vaš onchain Address.


![blixt](assets/en/18.webp)


Taj blok broj 764272 je kada će sredstva biti dostupna u vašem Bitcoin onchain Address. I može potrajati do 144 bloka od 1. bloka potvrde dok ne budu oslobođena. [Zato proverite to u Mempool](https://Mempool.space/).


I to je to. Samo strpljivo čekajte dok svi kanali ne budu zatvoreni i sredstva vraćena u vaš onchain Wallet.


👉 **Tajna metoda vraćanja :**


Postoji još jedan metod za vraćanje vašeg Blixt LND čvora bez zatvaranja kanala. Ali je skriven od običnih početnika, jer je ovaj metod SAMO za one koji znaju šta rade.


U slučaju da trebate migrirati svoj postojeći (funkcionalni) Blixt čvor na drugi novi uređaj, bez zatvaranja postojećih LN kanala, moraćete da uradite sledeće korake:



- Pretpostavljamo da ste već sačuvali Blixt Wallet seed (24 words aezeed)
- Na starom uređaju idite na "Settings" - odeljak za debagovanje - "Compact LND database". Ovaj korak je opcionalan, ali se preporučuje ako želite manju veličinu channel.db fajla. Obično je prilično velik, u zavisnosti od aktivnosti vašeg čvora. Ovo će restartovati Blixt i smanjiti veličinu db fajla.
- Kada se ponovo pokrene, idite na "Settings" i promenite svoje uobičajeno alias ime u "Hampus". Ovo će aktivirati skrivene opcije, samo za napredne korisnike.
- Idite skroz dole do odeljka "Debug" i videćete novu opciju "Export channel.db file". UPOZORENJE! Kada izvršite ovaj izvoz, postojeći Blixt LN čvor će biti onemogućen na ovom starom uređaju i izvoziće celu bazu podataka čvora (channel.db) spremnu za uvoz na novi uređaj.
- Ova db datoteka će biti sačuvana u određeni folder na vašem starom uređaju (Documents ili Downloads) i odatle ćete je morati premestiti takvu kakva jeste na vaš novi uređaj. Možete koristiti na primer [LocalSend FOSS aplikaciju](https://github.com/localsend/localsend) da direktno prenesete datoteku između uređaja.
- U ovom trenutku vaš stari Blixt MORA ostati isključen. NEMOJTE GA PONOVO OTVARATI!
- Kada prenesete datoteku channel.db na novi uređaj, pokrenite novu instalaciju Blixt-a i izaberite "Restore Wallet" na prvom ekranu.
- Na dugme gde piše "Select SCB file" dugo pritisnite (NE jednostavan klik!) i tada ćete videti opciju da izaberete channel.db fajl gde ga sačuvate lokalno na novom uređaju. Ako samo jednostavno pritisnete to dugme, koristiće podrazumevano SCB fajl (sa zatvaranjem kanala), ne radi za punu rezervnu kopiju uživo kanala.
- Stavite 24 reči seed i zatim kliknite "Restore"
- Videćete da će Blixt početi da se sinhronizuje sa Neutrino. Možete i gledati logove sinhronizacije.
- IMAJTE NA UMU! Pokušajte da Blixt bude otvoren sve vreme u ovoj fazi! Nemojte dozvoliti da pređe u režim spavanja ili da zatvorite ekran aplikacije. To bi moglo prekinuti početnu sinhronizaciju i moraćete da je ponovo uradite. Strpljivo sačekajte, neće trajati više od nekoliko minuta.
- Kada se početna sinhronizacija blokova završi, brzo će skenirati vaše prethodne Wallet adrese i tada će vaši kanali ponovo biti online, živi i zdravi.
- Nažalost, prethodna istorija plaćanja i kontakti još uvek nije moguće vratiti. Ali to ionako nije toliko važno.


I GOTOVO! Sada imate potpuno obnovljen Blixt LN čvor. Takođe može raditi sa drugim LND rezervnim kopijama (Umbrel, Raspiblitz itd.) ako ste prethodno ispravno sačuvali channel.db datoteku. Dakle, Blixt može bukvalno spasiti bilo koji LND mrtav čvor.


---

## Blixt - Četvrti Kontakt


Ovo poglavlje se bavi prilagođavanjem i boljim upoznavanjem vašeg Blixt Node-a. Neću opisivati sve dostupne funkcije, ima ih previše i već su objašnjene na [Blixt Features Page](https://blixtwallet.github.io/features).


Ali ću ukazati na neke od onih koji su neophodni za napredovanje koristeći vaš Blixt i imati sjajno iskustvo.


### A - Ime (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) je standard za prenošenje "imena primaoca" u BOLT11 fakturama.


Ovo može biti bilo koje ime i može se promeniti u bilo kom trenutku.


Ova opcija je zaista korisna u raznim slučajevima, kada želite poslati ime zajedno sa opisom Invoice, tako da primalac može imati nagoveštaj od koga je primio te Sats. Ovo je potpuno opciono i takođe na ekranu za plaćanje, korisnik mora označiti polje koje ukazuje na slanje alias imena.


Evo kako bi izgledalo kada koristite [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Ovo je još jedan primer slanja na drugu Wallet aplikaciju koja podržava NameDesc:


![blixt](assets/en/21.webp)


### B - Lightning Box


Počevši od nove verzije v0.6.9-420 [nedavno najavljene](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt je uveo novu moćnu funkciju za Lightning Address u Blixt.


Ova nova funkcija je opcionalna i nije uključena po defaultu!


Za sada podrazumevani LN Box pokreće Blixt server i nudi @blixtwallet.com LN Address. Ali BILO KO sa LND javnim čvorom može pokrenuti Lightning Box server i ponuditi LN Address za svoju sopstvenu domenu, samostalno čuvanje.


Trenutno, Blixt server samo prosleđuje uplate poslate na LN adrese @blixtwallet.com Blixt korisnicima koji su postavili svoj LN Address. Korisnici moraju staviti svoj Blixt čvor Wallet u "persistent mode" kako bi primili ove uplate na svoje @blixtwallet.com LN adrese.


Pogledajte u napomenama o izdanju video demo o tome kako postaviti vaš LN Address u Blixt.


Ovaj LN Address implementiran u Blixt Wallet aplikaciju, je kao chat preko LN, instantan i zabavan, takođe podržava [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (dodavanje alias imena plaćanju). Možete dodati u listu kontakata sve vaše redovne LN adrese koje često koristite i imati ih pri ruci za ćaskanje. Sada se Blixt može smatrati punom LN chat aplikacijom 😂😂.


Još jedna korisna funkcija je puna podrška za LUD-18 (koju takođe [Stacker.News](https://stacker.news/r/DarthCoin) i drugi podržavaju).


![blixt](assets/en/22.webp)


Kao što možete videti na gornjem snimku ekrana, prilikom slanja sa Stacker News naloga, lepo se prikazuje logo + LN Address + poruka. Na isti način funkcioniše slanje sa Blixt-a, možete priložiti vaš Blixt LN Address ili jednostavno dodati ime aliasa (prethodno postavljeno u Blixt podešavanjima) ili čak oba.


Ova opcija iz LUD-18 mogla bi biti korisna i za pretplatničke usluge, gde korisnik može poslati specifičan alias (NIJE vaš čvor alias ili vaše pravo ime!) i na osnovu toga možete biti registrovani ili primiti specifičnu poruku ili bilo šta drugo. Dodavanje imena aliasa ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ komentar ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) na LN uplatu može imati više namena!


Evo koda za [Lightning Box](https://github.com/hsjoberg/lightning-box) ako ga pokrećete za sebe, svoju porodicu i prijatelje, na svom čvoru.


Ovde takođe možete pokrenuti [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) za Blixt mobilne čvorove i ponuditi likvidnost za Blixt korisnike ako imate dobar javni LN čvor (radi samo sa LND).


### C - Backup LN Kanali i seed reči


Ovo je veoma važna funkcija !


Nakon otvaranja ili zatvaranja LN kanala treba da napravite rezervnu kopiju. To se može uraditi ručno čuvanjem male datoteke na lokalnom uređaju (obično u folderu za preuzimanje) ili korišćenjem Google Drive ili iCloud naloga.


![blixt](assets/en/23.webp)


Idite na Blixt Settings - Wallet sekciju. Tamo imate opcije za čuvanje svih važnih podataka za vaš Blixt Wallet:



- "Prikaži Mnemonic" - prikazaće 24 reči seed da ih zapišete
- „Ukloni Mnemonic sa uređaja“ - ovo je opcionalno i koristite ga samo ako zaista želite da uklonite seed reči sa svog uređaja. Ovo NEĆE obrisati vaš Wallet, samo seed. Ali budite oprezni! Nema načina da ih povratite ako ih prvo niste zapisali.
- „Izvezi rezervnu kopiju kanala“ - ova opcija će sačuvati malu datoteku na vašem lokalnom uređaju, obično u folder „preuzimanja“, odakle je možete uzeti i premestiti van vašeg uređaja, radi sigurnog čuvanja.
- „Verify channel backup“ - ovo je dobra opcija ako koristite Google Drive ili iCloud da proverite integritet bekapa urađenog na daljinu.
- „Google drive channel backup“ - će sačuvati rezervnu kopiju u vašem ličnom Google drive-u. Datoteka je šifrovana i čuva se u posebnom skladištu odvojeno od vaših uobičajenih google datoteka. Dakle, nema brige da je neko može pročitati. U svakom slučaju, ta datoteka je potpuno beskorisna bez seed reči, tako da niko ne može uzeti vaša sredstva samo iz te datoteke.


Preporučio bih za ovaj deo sledeće:



- koristite menadžer lozinki za sigurno čuvanje vašeg seed i rezervne datoteke. KeePass ili Bitwarden su veoma dobri za to i mogu se koristiti na više platformi i samostalno hostovati ili offline.
- URADI BEKAP SVAKI PUT kada otvoriš ili zatvoriš kanal. Taj fajl se ažurira sa informacijama o kanalima. Nema potrebe da to radiš nakon svake transakcije koju si obavio na LN. Bekap kanala ne čuva te informacije, već samo status kanala.


![blixt](assets/en/24.webp)


---

## Blixt - Saveti i trikovi


### SLUČAJ 1 - PROBLEMI SA SINHRONIZACIJOM


"_Moj Blixt se ne sinhronizuje... Moj Blixt ne prikazuje saldo... Moj Blixt ne može da otvori kanale... Pokušao sam da ga obnovim na drugom uređaju... itd_"


Svi ovi problemi počinju zato što VAŠ UREĐAJ NE SINHRONIZUJE ISPRAVNO. Molimo vas da razumete ovaj važan aspekt: Blixt je mobilni LND čvor, koji koristi Neutrino za sinhronizaciju / čitanje blokova.



- Evo manje tehničkog objašnjenja iz [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Evo još tehničkih resursa od [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Evo kako možete aktivirati Neutrino na svom kućnom čvoru i služiti filtere blokova za vaš mobilni čvor, sa [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


PODSETNIK: Korišćenje Neutrino preko clearnet-a je potpuno bezbedno, vaš IP ili xpub nisu otkriveni. Samo čitate blokove sa udaljenog čvora pomoću neutrino. To je sve. Sve ostalo se obavlja na vašem lokalnom uređaju.


Dakle, NEMA POTREBE da ga koristite sa Tor-om. Tor će dodati veliku latenciju vašem procesu sinhronizacije i učiniti vaš Blixt veoma nestabilnim. Ako zaista želite da koristite preko Tor-a, budite sigurni šta radite i imajte dobru vezu i strpljenje. Isti slučaj važi za korišćenje VPN-a. Budite pažljivi kakvu latenciju vam daje taj VPN.


Možete testirati latenciju neutrino servera jednostavnim pingovanjem, sa računara ili sa mobilnog telefona.


![blixt](assets/en/25.webp)


Ovo je uobičajen ping ka neutrino serveru europe.blixtwallet.com, što pokazuje da je veza veoma dobra sa prosečnim vremenom odziva od 50ms i TTL od 51. Vreme odziva može varirati, ali ne previše. TTL mora biti stabilan.


Ako su ove vrednosti veće od 100-150ms, vaš proces sinhronizacije će zastareti ili još gore, može izazvati zatvaranje kanala od strane vršnjaka! Nemojte ignorisati ovaj aspekt.


Bez odgovarajuće sinhronizacije, takođe ne možete videti tačan balans ili vaši LN kanali neće biti online i operativni. Bez obzira koliko giga ultra terra mbps imate brzina preuzimanja NIJE BITNA. Bitno je vreme odziva i TTL (time to live).


Ovo je kao opšti slučaj za LATAM korisnike. Ne znam šta se dešava tamo dole, ali vi imate užasnu konekciju sa pingovima preko 200ms što može poremetiti bilo kakvu sinhronizaciju.


Pa šta je rešenje za ove očajne korisnike?



- prestani koristiti Blixt sa Torom. Potpuno je beskorisno
- možete koristiti VPN, ali ga pažljivo odaberite i stalno pratite ping. Koristite onaj koji je bliži vašoj geografskoj lokaciji. Udaljenost znači više ms vremena odziva, zapamtite.
- odaberite pažljivo svoje neutrino kolege, ovde je lista poznatih javnih neutrino servera:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Još jedan način je da odaberete jedan sa ove liste čvorova koji najavljuju "kompaktne filtere" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Izaberite onaj koji je bliži vašoj geografskoj lokaciji.


Još jedan način (najbolji način) je da se povežete sa lokalnim čvorom zajednice, koji vodi prijatelj ili grupa koju poznajete, i koji nudi neutrino konekciju. [Evo uputstava kako to uraditi.](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Njihov čvor neće biti pogođen ni na koji način, samo im je potrebna stabilna i javna konekcija.


Postoji potreba za više neutrino servera u LATAM regionu, za bolje i brže sinhronizovanje. Zato se organizujte sa vašom lokalnom Bitcoin zajednicom i odlučite ko i gde će pokrenuti Bitcoin Core + Neutrino za vašu sopstvenu upotrebu. Dovoljna je samo javna IP adresa. Ako nemate pristup javnoj IP adresi, možete koristiti VPS IP i napraviti wireguard tunel do vašeg kućnog čvora. Na taj način preusmeravate sav saobraćaj na vašu lokalnu VPS IP adresu, bez otkrivanja bilo kakvih privatnih informacija o vašem kućnom čvoru.


### SLUČAJ 2 - NIKADA NE ZAVRŠAVA SINHRONIZACIJU


"_Moj Blixt ima dobru vezu sa neutrino serverom ali je zaglavljen u sinhronizaciji._"


#### Vremenski server


Ponekad ljudi koriste razne stare uređaje ili nisu pravilno povezani sa vremenskim serverom. Neutrino se sinhronizuje u redu dok ne dostigne stvarne blokove koji ne odgovaraju stvarnom lokalnom vremenu. Videćete u Blixt LND logovima grešku koja kaže da je "vremenska oznaka bloka daleko u budućnosti" ili nešto vezano za "zaglavlje ne prolazi proveru ispravnosti".


Brzo rešenje: postavite tačno vreme i datum za svoj uređaj i ponovo pokrenite Blixt.


#### Nizak prostor na uređaju


Ponekad korišćenje starog uređaja, sa malo prostora, može dostići granični limit i zaglaviti se. Zaista, što više koristite ovaj mobilni LND čvor, neutrino fajlovi postaju veći, kao i channel.db fajl.


Brzo rešenje: Idite na Blixt Opcije - Debug sekcija - Izaberite "stop LND i obriši neutrino fajlove". Ovo će restartovati aplikaciju i započeti novo sveže sinhronizovanje. Ponekad ovo brzo rešenje može popraviti i oštećene podatke. Imajte na umu da će biti potrebno neko vreme, između 1 i 3 minuta, da se potpuno resinkronizuje. NE briše postojeća sredstva ili kanale, ali da, nakon resinkronizacije može pokrenuti ponovno skeniranje vaših Bitcoin adresa i to može potrajati više vremena.


Sledeći korak je da proverite koliko je podataka još uvek zauzeto. To možete videti u Android App info - podaci. Ako je i dalje veće od 400-500MB, možete kompaktovati LND fajlove. Dakle, idite na Blixt Opcije - Debug sekcija - Izaberite "Compact DB LND". Ponovo pokrenite Blixt aplikaciju ako se ne uradi automatski. Kompaktovanje se odvija pri pokretanju i samo jednom. Sada ćete videti da su Blixt podaci manje zauzeti.


#### Uporan režim


Ponekad ljudi ne otvore Blixt dugo vremena, pa je sinhronizacija previše stara. Ali očekuju da će biti sinhronizovani odmah kada ga otvore.


Molim vas da budete strpljivi i pogledate na vrh točka koji se okreće. Opcionalno možete otići na Opcije - Pogledaj Informacije o Čvoru i proveriti da li je sinhronizovan sa lancem i grafom označenim kao "true". Bez te oznake "true" ne možete pravilno koristiti Blixt, ne možete ispravno videti stanje, ne možete videti LN kanale online, ne možete vršiti plaćanja.


Brzo rešenje: Postoji moćna opcija da "održite u životu" vaš Blixt čvor. Idite na Opcije - Eksperimenti - Izaberite "Aktiviraj Persistentni Režim". To će restartovati vaš Blixt i staviti LND servis u persistentni režim, tj. uvek će biti aktivan i održavati vašu sinhronizaciju online, čak i ako pređete na drugu aplikaciju ili jednostavno zatvorite Blixt (ne forsirano zatvaranje ili ubijanje zadatka). Možete ga tako držati ceo dan ako ste na stabilnoj vezi i trebate koristiti Blixt više puta. Neće trošiti previše baterije.


### SLUČAJ 3 - ŽELIM DA PREĐEM NA DRUGI UREĐAJ


U redu o ovom scenariju napisao sam opsežan vodič na [stranici FAQ](https://blixtwallet.github.io/faq#blixt-restore): sa 2 opcije, brza (kooperativno zatvaranje kanala pre migracije) i spora (prisilno zatvaranje kanala jer je stari uređaj mrtav).


Ali želim da ponovim ovde neke važne aspekte i dodam novu "tajnu" proceduru.


PODSETNIK:



- Uvek napravite rezervnu kopiju statusa vaših kanala (SCB) NAKON svakog otvaranja ili zatvaranja kanala. Potrebno je samo nekoliko sekundi da to uradite.
- Ne čuvajte stare SCB fajlove, da ne biste bili zbunjeni i vratili ih. Potpuno su beskorisni i mogli bi pokrenuti kaznenu proceduru ako ih koristite. Uvek koristite poslednju verziju SCB fajla ako nastavite sa vraćanjem.
- Sačuvajte SCB datoteku (to je šifrovani tekst sa ekstenzijom .bin) van vašeg uređaja, na sigurnom mestu. Možete koristiti [LocalSend](https://github.com/localsend/localsend) za prebacivanje ove datoteke na PC ili drugi uređaj.
- Sačuvaj takođe seed svog Blixt Wallet na sigurnom mestu, na primer u offline menadžeru lozinki / enkriptovanom USB-u.


Tajna metoda: Kako migrirati Blixt čvor bez zatvaranja postojećih kanala. Za ovo ćete morati pažljivo pročitati prethodni odeljak "Treći kontakt" u ovom vodiču o "Obnavljanju Wallet".


Ovaj postupak NIJE ZA POČETNIKE, namenjen je samo naprednim korisnicima! Zato nije široko dostupan i preporučujem da ga radite samo uz asistenciju Blixt developera ili moju podršku. Molim vas da ne ignorišete ovaj savet.


### SLUČAJ 4 - KOJE PEER-OVE KORISTITI ZA OTVARANJE KANALA?


Kao što sam napisao na [Blixt vodič stranici](https://blixtwallet.github.io/guides) postoji mnogo načina za otvaranje kanala sa ovom mobilnom LND čvorom. Ali neki važni aspekti koje bih želeo da vas podsetim ovde:



- otvorite sa dobro poznatim LSP čvorovima i sa čvorovima koje je zajednica potvrdila. [Pogledajte ovde listu](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- ne otvarajte sa slučajnim Tor čvorovima. Oni su bezvredni i imaćete samo probleme sa nemogućnošću plaćanja. Bez obzira koliko je vaš prijatelj "pokretač čvora" dobar sa lošim Tor čvorom u džungli, nikada vam neće dati najbolje rute za mobilni privatni čvor. Ne otvarate kanale sa nekim zato što vam je prijatelj. Ovo nije Facebook! Otvarate kanal zbog: dobrih ruta, malih naknada, dostupnosti.
- nema potrebe otvarati gomilu malih kanala, 2-3 ili maksimalno 4, ali sa dobrom količinom Sats. Ne otvarajte male kanale, potpuno su beskorisni. Manji od 200k za mobilni nemaju mnogo koristi.
- imajte na umu LSP-ove koji nude dolazne kanale i JIT (just in time) kanale. Oni su veoma korisni jer ne morate koristiti nijedan od svojih UTXO-a, možete platiti otvaranje kanala sredstvima koja već imate u drugim LN novčanicima, slažući ih i pripremajući za otvaranje većeg kanala. Trebalo bi da koristite ove JIT kanale u svoju korist. [Objasnio sam u ovom vodiču](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) više opcija za peer-ove za privatne čvorove kao što je Blixt. Takođe [ovde u ovom vodiču objavljenom na SN](https://stacker.news/items/679242/r/DarthCoin) objasnio sam kako upravljati likvidnošću privatnih mobilnih čvorova.


---

## Zaključak


OK, postoje mnoge druge neverovatne funkcije koje Blixt nudi, prepustiću tebi da ih otkrivaš jednu po jednu i zabaviš se.


Ova aplikacija je zaista potcenjena, uglavnom zato što nije podržana od strane bilo kakvog VC finansiranja, vođena je zajednicom, izgrađena sa ljubavlju i strašću za Bitcoin i Lightning Network.


Ovaj mobilni LN čvor, Blixt je veoma moćan alat u rukama mnogih korisnika, ako znaju kako da ga dobro koriste. Samo zamislite, šetate svetom sa LN čvorom u sopstvenom džepu i niko to neće znati.


I ne govorimo o svim drugim bogatim funkcijama koje dolaze uz to, koje vrlo malo ili nijedna druga Wallet aplikacija ne može ponuditi.


U međuvremenu, ovde su svi linkovi o ovom neverovatnom Bitcoin Lightning Node:



- [Blixt Official Webpage](https://blixtwallet.com/)
- [Blixt Github page](https://github.com/hsjoberg/blixt-Wallet/)
- [Stranica sa funkcijama Blixt](https://blixtwallet.github.io/features) - objašnjava jednu po jednu svaku funkciju i funkcionalnost.
- [Blixt FAQ stranica](https://blixtwallet.github.io/faq) - Lista pitanja i odgovora i rešavanje problema za Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demonstracije, video tutorijali, dodatni vodiči i slučajevi upotrebe za Blixt
- Preuzmi: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [Direktno preuzimanje APK](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegram grupa za direktnu podršku](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Stranica za crowdfunding na Geyseru](https://geyser.fund/project/blixt) - donirajte Sats kako želite da podržite projekat
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonimni LN chat
- [Blixt prezentacija - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - promo video (you can test your 1st use of LN)
- [Štampaj A4 flajer sa prvim koracima korišćenja Blixt-a, na različitim jezicima](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt takođe nudi potpuno funkcionalan demo](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) direktno na svojoj veb stranici ili na posvećenoj verziji veba, kako biste imali potpuno iskustvo testiranja pre nego što počnete da ga koristite u stvarnom svetu.


---
**ODRICANJE ODGOVORNOSTI:**


*Ja nisam plaćen niti podržan na bilo koji način od strane developera ove aplikacije. Napisao sam ovaj vodič jer sam primetio da interesovanje za ovu Wallet aplikaciju raste i novi korisnici još uvek ne razumeju kako da počnu sa njom. Takođe, da pomognem Hampus-u (glavnom developeru) sa dokumentacijom o korišćenju ovog čvora Wallet.*


*Nemam nikakav drugi interes u promovisanju ove LN aplikacije, osim da podstaknem usvajanje Bitcoin i LN. Ovo je jedini način!*


---