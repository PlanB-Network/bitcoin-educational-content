---
name: RoninDojo

description: Instaliranje i korišćenje vašeg RoninDojo Bitcoin čvora.
---
***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, određene funkcije RoninDojo-a, kao što je Whirlpool, više nisu operativne. Međutim, moguće je da bi ovi alati mogli biti ponovo uspostavljeni ili pokrenuti na drugačiji način u narednim nedeljama. Takođe, pošto je RoninDojo kod bio hostovan na Samourai-ovom GitLab-u, koji je takođe zaplenjen, nije moguće preuzeti kod sa interneta. Timovi RoninDojo-a verovatno rade na ponovnom objavljivanju koda.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je namenjen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti podstičemo upotrebu ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


_Ovaj vodič je posvećen instalaciji RoninDojo v1. Da biste iskoristili najnovija poboljšanja i funkcije, toplo preporučujem da pogledate naš vodič posvećen direktnoj instalaciji RoninDojo v2 na vaš Raspberry Pi:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Pokretanje i korišćenje sopstvenog čvora je ključno za istinsko učešće u Bitcoin mreži.Iako vođenje Bitcoin čvora ne donosi korisniku finansijsku korist, ali sa druge strane omogućava da sačuva svoju privatnost, deluje nezavisno i ima kontrolu nad poverenjem u mrežu.



U ovom članku, detaljno ćemo razmotriti RoninDojo, odlično rešenje za pokretanje sopstvenog Bitcoin čvora.


### Sadržaj:



- Šta je RoninDojo?
- Koji hardver odabrati?
- Kako instalirati RoninDojo?
- Kako koristiti RoninDojo?
- Zaključak


Ako niste upoznati sa načinom rada Bitcoin čvora i njegovom ulogom, preporučujem da počnete čitanjem ovog članka: The Bitcoin Node - Part 1/2: Technical Concepts.


![Samourai](assets/1.webp)


## Šta je RoninDojo?


Dojo je potpuni Bitcoin čvor server razvijen od strane Samourai Wallet tima. Možete ga slobodno instalirati na bilo koji uređaj.


RoninDojo je asistent za instalaciju i alat za administraciju Dojo-a i raznih drugih alata. RoninDojo preuzima originalnu implementaciju Dojo-a i dodaje mnoge druge alate, dok istovremeno olakšava instalaciju i upravljanje.


Oni takođe nude "plug-and-play" hardver, RoninDojo Tanto, sa unapred instaliranim RoninDojo na mašini koju je sastavio njihov tim. Tanto je plaćeno rešenje, pogodno za one koji ne žele da se upuštaju u tehničke detalje.


Kod za RoninDojo je otvorenog koda, tako da je moguće instalirati ovo rešenje na sopstvenom hardveru. Ova opcija je isplativa, ali zahteva malo više manipulacije, što ćemo uraditi u ovom članku.


RoninDojo je Dojo, tako da omogućava laku integraciju Whirlpool CLI u vaš Bitcoin čvor kako biste imali najbolje moguće CoinJoin iskustvo. Sa Whirlpool CLI, ne samo da možete dozvoliti vašim bitcoinima da se remixuju 24/7 bez potrebe da držite vaš lični računar uključenim, već možete i značajno poboljšati vašu privatnost.


RoninDojo integriše mnoge druge alate koji se oslanjaju na vaš Dojo, kao što je Boltzmann kalkulator, koji određuje nivo privatnosti transakcije, Electrum server za povezivanje vaših različitih Bitcoin novčanika sa vašim čvorom, ili [Mempool](https://planb.network/resources/glossary/mempool) server za privatno praćenje vaših transakcija.

U poređenju sa drugim rešenjem za node kao što je Umbrel, koje sam vam predstavio u ovom članku, RoninDojo je duboko fokusiran na "on chain" rešenja i alate koji optimizuju privatnost korisnika. Stoga, RoninDojo ne dozvoljava interakciju sa Lightning mrežom.

RoninDojo nudi manje alata u poređenju sa Umbrelom, ali nekoliko osnovnih funkcija za Bitkoinere prisutnih na Roninu su izuzetno stabilne.


Dakle, ako vam nisu potrebne sve funkcije Umbrel servera i želite samo jednostavan i stabilan čvor sa nekoliko osnovnih alata kao što su Whirlpool ili Mempool, onda je RoninDojo verovatno dobro rešenje za vas.


Po mom mišljenju, razvojni fokus Umbrela je snažno usmeren na Lightning mrežu i svestrane alate. I dalje je Bitcoin čvor, ali cilj je da postane multitasking mini-server. Nasuprot tome, razvojni fokus RoninDojo-a je više usklađen sa timovima u Samourai Wallet-u i fokusira se na osnovne alate za bitkojnere, omogućavajući potpunu nezavisnost i optimizovano upravljanje privatnošću na Bitcoin-u.


Imajte na umu da je postavljanje RoninDojo čvora nešto složenije od Umbrel čvora.


Sada kada smo uspeli da naslikamo sliku RoninDojo-a, hajde da vidimo kako da zajedno postavimo ovaj čvor.


## Koji hardver odabrati?


Da biste izabrali mašinu koja hostuje i pokreće RoninDojo, imate nekoliko opcija.


Kao što je ranije objašnjeno, najjednostavniji izbor je naručiti Tanto, plug-and-play mašinu dizajniranu specifično za ovu svrhu. Da naručite svoju, idite ovde: [link](https://shop.ronindojo.io/product-category/nodes/).


Pošto timovi RoninDojo proizvode open-source kod, moguće je implementirati RoninDojo i na drugim mašinama. Najnovije verzije instalacionog čarobnjaka možete pronaći na ovoj stranici: [link](https://ronindojo.io/en/downloads.html), a najnovije verzije koda na ovoj stranici: [link](https://code.samourai.io/ronindojo/RoninDojo).


Lično, instalirao sam ga na Raspberry Pi 4 8GB i sve radi savršeno.


Međutim, imajte na umu da timovi RoninDojo ukazuju na to da često postoje problemi sa kućištem i SSD adapterom. Stoga se ne preporučuje korišćenje kućišta sa kablom za SSD vašeg uređaja. Umesto toga, preporučuje se korišćenje kartice za proširenje skladišta koja je posebno dizajnirana za vašu matičnu ploču, kao što je ova: Raspberry Pi 4 Storage Expansion Card.


Evo kako da postavite svoj RoninDojo čvor:



- Raspberry Pi 4.
- Kućište sa ventilatorom.
- Kompatibilna kartica za proširenje skladišta.
- Kabl za napajanje.
- Industrijska micro SD kartica od 16GB ili više.
- SSD od 1TB ili veći.
- RJ45 Ethernet kabl, preporučuje se kategorija 8.


## Kako instalirati RoninDojo?


### Korak 1: Pripremite butabilnu micro SD karticu.


Kada sastavite svoju mašinu, možete započeti instalaciju RoninDojo-a. Da biste to uradili, počnite tako što ćete kreirati butabilnu micro SD karticu snimanjem odgovarajuće slike diska na nju.


Umetnite svoju micro SD karticu u lični računar, zatim idite na zvaničnu RoninDojo veb stranicu da preuzmete RoninOS disk image: https://ronindojo.io/en/downloads.html.


Preuzmite sliku diska koja odgovara vašem hardveru. U mom slučaju, preuzeo sam "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" sliku:


![Download RoninOS disk image](assets/2.webp)


Kada se slika preuzme, proverite njen integritet koristeći odgovarajući .SHA256 fajl. Detaljno ću opisati kako to uraditi u ovom članku: Kako proveriti integritet Bitcoin softvera na Windows-u?


Specifična uputstva za proveru integriteta RoninOS-a su takođe dostupna na ovoj stranici: https://wiki.ronindojo.io/en/extras/verify.


Da biste snimili ovu sliku na vašu micro SD karticu, možete koristiti softver kao što je Balena Etcher, koji možete preuzeti ovde: https://www.balena.io/etcher/.


Da biste to uradili, izaberite sliku u Etcher-u i flešujte je na micro SD karticu:


![Burn disk image with Etcher](assets/3.webp)


Kada je operacija završena, možete umetnuti bootabilnu micro SD karticu u Raspberry Pi i uključiti uređaj.


### Korak 2: Konfigurišite RoninOS.


RoninOS je operativni sistem vašeg RoninDojo čvora. To je modifikovana verzija Manjaro-a, Linux distribucije. Nakon pokretanja vašeg uređaja i čekanja nekoliko minuta, možete započeti njegovu konfiguraciju.


Da biste se povezali na daljinu, potrebno je da pronađete IP adresu vaše RoninDojo mašine. Da biste to uradili, možete, na primer, da se povežete na administrativni panel vašeg internet rutera, ili možete preuzeti softver kao što je https://angryip.org/ da skenirate vašu lokalnu mrežu i pronađete IP adresu mašine.


Kada pronađete IP, možete preuzeti kontrolu nad vašom mašinom sa drugog računara povezanog na istu lokalnu mrežu koristeći SSH.


Sa računara koji koristi macOS ili Linux, jednostavno otvorite terminal. Sa računara koji koristi Windows, možete koristiti specijalizovani alat kao što je Putty ili direktno koristiti Windows PowerShell.


Kada se terminal otvori, unesite sledeću komandu:

```
ssh root@192.168.?.?
```


Jednostavno zamenite dva znaka pitanja sa IP adresom vašeg prethodno pronađenog RoninDojo.

Savet: U Shell-u, desnim klikom nalepite stavku.


Dalje, stići ćete do kontrolne table Manjaro. Izaberite odgovarajući raspored tastature koristeći strelice za promenu cilja u padajućoj listi.


![Manjaro Keyboard Configuration](assets/4.webp)


Izaberite korisničko ime i lozinku za vašu sesiju. Koristite jaku lozinku i napravite sigurnu rezervnu kopiju. Opcionalno možete koristiti slabu lozinku tokom instalacije, a kasnije je lako promeniti "kopiranjem i lepljenjem" u RoninUI. Ovo će vam omogućiti da koristite veoma jaku lozinku bez trošenja previše vremena na ručno kucanje tokom podešavanja Manjaro-a.


![Manjaro Username Configuration](assets/5.webp)


Dalje, od vas će se tražiti da izaberete root lozinku. Za root lozinku, unesite jaku lozinku direktno. Nećete moći da je promenite iz RoninUI. Takođe, zapamtite da sigurno napravite rezervnu kopiju ove root lozinke.


Zatim unesite svoju lokaciju i vremensku zonu.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Zatim, izaberite ime hosta.


![Manjaro Hostname Configuration](assets/8.webp)


Konačno, proverite informacije o Manjaro konfiguraciji i potvrdite.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### Korak 3: Preuzmite RoninDojo.


Početna konfiguracija RoninOS-a će biti završena. Kada bude završeno, kao što je prikazano na gornjem snimku ekrana, mašina će se ponovo pokrenuti. Sačekajte nekoliko trenutaka, a zatim unesite sledeću komandu da se ponovo povežete sa vašom RoninDojo mašinom:

```
ssh username@192.168.?.?
```


Jednostavno zamenite "username" sa korisničkim imenom koje ste prethodno odabrali, i zamenite znakove pitanja sa IP adresom vašeg RoninDojo-a.


Zatim unesite lozinku korisnika.


U terminalu, izgledaće ovako:


![SSH Connection to RoninOS](assets/10.webp)


Sada ste povezani sa svojom mašinom, koja trenutno ima samo RoninOS. Sada treba da instalirate RoninDojo na nju.


Preuzmite najnoviju verziju RoninDojo unosom sledeće komande:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


Preuzimanje će biti brzo. U terminalu ćete videti ovo:


![Cloning RoninDojo](assets/11.webp)


Sačekajte da se preuzimanje završi, zatim instalirajte i pristupite RoninDojo korisničkom interfejsu koristeći sledeću komandu:

```
~/RoninDojo/ronin
```


Bićete zamoljeni da unesete svoju korisničku lozinku:


![Bitcoin Node Password Verification](assets/12.webp)


Ova komanda je potrebna samo prvi put kada pristupate svom RoninDojo. Nakon toga, da biste pristupili RoninCLI putem SSH, jednostavno ćete morati uneti komandu [SSH username@192.168.?.?] zamenjujući "username" sa vašim korisničkim imenom i unoseći IP adresu vašeg čvora. Bićete upitani za vašu korisničku lozinku.


Sledeće, videćete ovu veličanstvenu animaciju:


![RoninCLI launch animation](assets/13.webp)


Zatim ćete konačno stići na RoninDojo CLI korisnički interfejs.


### Korak 4: Instalirajte RoninDojo.


Sa glavnog menija, koristite strelice na tastaturi da pređete na meni "Sistem". Pritisnite taster enter da potvrdite svoj izbor.


![RoninCLI navigation menu to System](assets/14.webp)


Zatim idite na meni "System Setup & Install".


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Konačno, proverite "System Setup" i "Install RoninDojo" koristeći razmak, zatim izaberite "Accept" da započnete instalaciju.


![RoninDojo installation confirmation](assets/16.webp)


Neka instalacija teče tiho. U mom slučaju, trajalo je oko 2 sata. Držite terminal otvoren tokom procesa.


Povremeno proveravajte svoj terminal, jer će vam biti zatraženo da pritisnete taster u određenim fazama instalacije, kao što je ovde na primer:


![RoninDojo installation in progress](assets/17.webp)


Na kraju instalacije, videćete pokretanje različitih kontejnera:


![Node container startup](assets/18.webp)


Zatim će se vaš čvor ponovo pokrenuti. Ponovo se povežite sa RoninCLI za sledeći korak.


![Bitcoin node restart](assets/19.webp)


### Korak 5: Preuzmite Proof-of-Work lanac i pristupite RoninUI.


Kada je instalacija završena, vaš čvor će početi preuzimanje Bitcoin Proof-of-Work lanca. Ovo se naziva Početno Preuzimanje Blokova (IBD). Obično traje između 2 i 14 dana u zavisnosti od vaše internet konekcije i uređaja.


Možete pratiti napredak preuzimanja lanca pristupanjem RoninUI web interfejsu.


Da biste mu pristupili sa lokalne mreže, upišite sledeće u adresnu traku vašeg pregledača:



- Ili direktno unesite IP adresu vaše mašine (192.168.?.?)
- Ili unesite: ronindojo.local


Zapamti da isključiš svoj VPN ako ga koristiš.


### Mogući preokret


Ako niste u mogućnosti da se povežete sa RoninUI iz vašeg pregledača, proverite ispravnost rada aplikacije iz vašeg Terminala povezanog na vaš čvor putem SSH. Povežite se sa glavnim menijem prateći prethodne korake:



- Ukucaj: SSH username@192.168.?.? zamenjujući sa svojim akreditivima.



- Unesite lozinku korisnika.


Jednom na glavnom meniju, idite na: **RoninUI > Restart**


Ako se aplikacija ispravno restartuje, problem je sa vezom iz vašeg pregledača. Proverite da li ne koristite VPN i uverite se da ste povezani na istu mrežu kao i vaš čvor.


Ako ponovno pokretanje izazove grešku, pokušajte ažurirati operativni sistem, a zatim ponovo instalirati RoninUI. Da biste ažurirali OS: **System > Software Updates > Update Operating System**


Kada se ažuriranje i ponovno pokretanje završe, ponovo se povežite sa svojim čvorom putem SSH i ponovo instalirajte RoninUI: **RoninUI > Ponovna instalacija**


Nakon što ponovo preuzmete RoninUI, pokušajte se povezati sa RoninUI putem vašeg pregledača.


**Savet:** Ako slučajno izađete iz RoninCLI i nađete se na Manjaro terminalu, jednostavno unesite komandu "ronin" da biste se direktno vratili na glavni meni RoninCLI.


### Prijava na veb


Možete se prijaviti na RoninUI web interfejs sa bilo koje mreže koristeći Tor. Da biste to uradili, preuzmite Tor adresu vašeg RoninUI sa RoninCLI: **Credentials > Ronin UI**


Preuzmi Tor adresu koji završava sa .onion i zatim se prijavi na Ronin UI unosom ove adrese u svoj Tor pretraživač. Pazi da ne otkriješ svoje različite akreditive, jer su to osetljive informacije.


![RoninUI web login interface](assets/20.webp)


Kada se prijavite, bićete upitani za vašu korisničku lozinku. To je ista lozinka koju koristite za prijavu putem SSH.


![RoninUI web interface management panel](assets/21.webp)


Možemo videti napredak IBD-a (Initial Block Download) ovde. Budite strpljivi, preuzimate sve transakcije napravljene na Bitcoin-u od 3. januara 2009.


Nakon preuzimanja celog Blockchain-a, indeksator će kompaktovati bazu podataka. Ova operacija traje oko 12 sati. Takođe možete pratiti njen napredak pod "Indexer" na RoninUI.


Vaš RoninDojo čvor će biti potpuno funkcionalan nakon ovoga:


![Indexer synchronized at 100% functional node](assets/22.webp)


Ako želite promeniti korisničku lozinku u jaču, to možete učiniti sada iz kartice "Settings". Na RoninDojo-u ne postoji dodatni sloj bezbednosti, zato preporučujem da izaberete zaista jaku lozinku i vodite računa o njenoj rezervnoj kopiji.


## Kako koristiti RoninDojo?


Kada se lanac preuzme i kompaktira, možete početi uživati u uslugama koje nudi vaš novi RoninDojo čvor. Hajde da vidimo kako ih koristiti.


### Povezivanje softverskog novčanika sa electrs.


Prva korisnost vašeg novoinstaliranog i sinhronizovanog čvora biće emitovanje vaših transakcija na Bitcoin mrežu. Zato ćete verovatno želeti da povežete različite softvere za upravljanje novčanikom sa njim.


Možete to uraditi koristeći Electrum Rust Server (electrs). Aplikacija je obično unapred instalirana na vašem RoninDojo čvoru. Ako nije, možete je ručno instalirati sa RoninCLI.


Jednostavno idite na: **Applications > Manage Applications > Install Electrum Server**


Da biste dobili Tor adresu vašeg Electrum Servera, iz RoninCLI menija idite na:

**Credentials > Electrs**


Samo treba da unesete .onion link u vaš softver novčanika. Na primer, u Sparrow novčaniku, idite na karticu:

**File > Preferences > Server**


U tipu servera izaberite `Private Electrum`, zatim unesite Tor adresu vašeg Electrum Servera u odgovarajuće polje. Na kraju, kliknite na "Test Connection" da testirate i sačuvate vašu konekciju.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Povezivanje softvera novčanika sa Samourai Dojo.


Umesto korišćenja Electrs, možete takođe koristiti Samourai Dojo za povezivanje vašeg kompatibilnog softverskog novčanika sa vašim RoninDojo čvorom. Na primer, Samourai novčanik nudi ovu opciju.


Da biste to uradili, jednostavno skenirajte QR kod za povezivanje vašeg Dojo-a. Da biste mu pristupili iz RoninUI, kliknite na karticu "Dashboard", a zatim na dugme "Manage" u okviru vašeg Dojo-a. Tada ćete moći da vidite QR kodove za povezivanje vašeg Dojo-a i BTC-RPC Explorer-a. Da biste ih prikazali, kliknite na "Display values".


![Retrieving the connection QR code to Dojo](assets/24.webp)


Da biste povezali svoj Samourai novčanik sa svojim Dojo-om, potrebno je da skenirate ovaj QR kod tokom instalacije aplikacije:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Korišćenje sopstvenog Mempool Explorer-a.


Osnovni alat za Bitcoinere, explorer vam omogućava da proverite razne informacije o Bitcoin lancu. Sa Mempool, na primer, možete u realnom vremenu proveriti naknade koje primenjuju drugi korisnici kako biste u skladu s tim prilagodili svoje. Takođe možete proveriti status potvrde jedne od vaših transakcija ili videti stanje adrese.


Ovi alati za istraživanje mogu vas izložiti rizicima po privatnost i zahtevaju da verujete bazi podataka treće strane. Kada koristite ovaj onlajn alat bez prolaska kroz sopstveni čvor:



- Rizikujete curenje informacija o vašem novčaniku.



- Verujete menadžeru vebsajta za Proof-of-Work lanac koji hostuju.


Da biste izbegli ove rizike, možete koristiti sopstvenu Mempool instancu na svom čvoru putem Tor mreže. Sa ovim rešenjem, ne samo da čuvate svoju privatnost prilikom korišćenja usluge, već više ne morate da verujete provajderu jer pretražujete sopstvenu bazu podataka.


Da biste to uradili, počnite instaliranjem Mempool Space Visualizer iz RoninCLI:


**Applications > Manage Applications > Install Mempool Space Visualizer**


Jednom instaliran, preuzmite link do vašeg Mempool-a. Tor adresa će vam omogućiti pristup sa bilo koje mreže. Slično tome, preuzimamo ovaj link putem RoninCLI:


**Credentials > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Jednostavno unesite svoj Mempool Tor adresu u Tor pretraživač da biste uživali u svojoj Mempool instanci, zasnovanoj na vašim podacima. Preporučujem da dodate ovu Tor adresu u svoje omiljene za brži pristup. Takođe možete kreirati prečicu na vašoj radnoj površini.


![Mempool Space interface](assets/27.webp)


Ako još uvek nemate Tor pregledač, možete ga preuzeti ovde: https://www.torproject.org/download/


Takođe možete pristupiti sa svog pametnog telefona instaliranjem Tor Browser-a i unosom iste adrese. Sa bilo kog mesta, možete pregledati stanje Bitcoin lanca koristeći svoj čvor.


### Korišćenje Whirlpool CLI.


Vaš RoninDojo čvor takođe uključuje WhirlpoolCLI – komandno-linijski interfejs koji omogućava automatizaciju Whirlpool mešanja sa drugog uređaja.


Kada izvodite CoinJoin sa Whirlpool implementacijom, aplikacija koju koristite mora ostati otvorena kako bi se izvršili miksevi i remiksevi. Ovaj proces može biti zamoran za korisnike koji žele imati visoke anon setove, jer uređaj koji hostuje aplikaciju sa Whirlpool-om mora stalno ostati uključen. U praktičnom smislu, to znači da ako želite uključiti svoje UTXO-e u 24/7 remikseve, moraćete držati svoj lični računar ili telefon stalno uključen sa otvorenom aplikacijom.


Jedno rešenje za ovo ograničenje je korišćenje WhirlpoolCLI na mašini koja je namenjena da bude stalno uključena, kao što je Bitcoin čvor. Na ovaj način, naši UTXO-ovi mogu biti remixovani 24/7 bez potrebe da držimo drugu mašinu osim našeg Bitcoin čvora uključenom.

WhirlpoolCLI se koristi sa WhirlpoolGUI, grafičkim interfejsom koji se instalira na lični računar za jednostavno upravljanje Coinjoins. Detaljno ću objasniti kako postaviti Whirlpool CLI sa sopstvenim dojom u ovom članku: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


Da biste saznali više o CoinJoin uopšte, sve objašnjavam u ovom članku: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Korišćenje Whirlpool Stat Alata.


Nakon što izvršite CoinJoins sa Whirlpool, možda ćete želeti da znate stvarni nivo privatnosti vaših mešanih UTXO-a. Whirlpool Stat Tool vam omogućava da to lako uradite. Pomoću ovog alata možete izračunati perspektivni skor i retrospektivni skor vaših mešanih UTXO-a. Da biste saznali više o izračunavanju ovih Anon Setova i kako funkcionišu, preporučujem da pročitate ovaj odeljak: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


Alat je unapred instaliran na vašem RoninDojo. Za sada je dostupan samo iz RoninCLI. Da biste ga pokrenuli iz glavnog menija, idite na:

**Samourai Toolkit > Whirlpool Stat Tool**


Uputstva za upotrebu će se pojaviti. Kada završite, pritisnite bilo koji taster da pristupite komandnim linijama:


![Whirlpool Stats Tool software home](assets/28.webp)


Terminal će prikazati:

**wst#/tmp>**


Da biste izašli iz ovog interfejsa i vratili se u RoninCLI meni, jednostavno unesite komandu:

```
quit
```


Da bismo počeli, postavićemo proxy na Tor-u kako bismo izvukli OXT podatke uz potpunu privatnost. Unesite komandu:

```
socks5 127.0.0.1:9050
```


Zatim preuzmite podatke iz bazena koji sadrži vašu transakciju:

```
download 0001
```


**Napomena:** zamenite `0001` sa kodom oznake bazena koji vas interesuje.


Šifre denominacija su sledeće na WST:



- Bazen 0.5 bitkoina: 05
- Bazen 0.05 bitkoina: 005
- Bazen 0.01 bitkoina: 001
- Bazen 0.001 bitkoina: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


Kada se podaci preuzmu, učitajte ih komandom:

```
load 0001
```


**Napomena:** zameni `0001` sa kodom oznake bazena koji te interesuje.


![Loading data from pool 0001](assets/30.webp)

Neka se proces učitavanja odvija, može potrajati nekoliko minuta. Nakon učitavanja podataka, unesite komandu score praćenu vašim txid (identifikator transakcije) da biste dobili njegove Anon Setove:

```
score TXID
```


**Napomena:** zamenite `txid` sa identifikatorom vaše transakcije.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST će zatim prikazati retrospektivni skor (metrike usmerene unazad) praćen prospektivnim skorom (metrike usmerene unapred). Pored Anon Set skorova, WST vam takođe pruža stopu difuzije vašeg izlaza u bazenu na osnovu anon seta.


Imajte na umu da se očekivani rezultat vašeg UTXO izračunava na osnovu txid vaše početne mešavine, a ne vaše poslednje mešavine. Suprotno tome, retrospektivni rezultat UTXO se izračunava na osnovu txid poslednjeg ciklusa.


Još jednom, ako ne razumete ove pojmove Anon Sets, preporučujem da pročitate ovaj deo mog članka o CoinJoin-u gde sve objašnjavam detaljno sa dijagramima: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### Korišćenje Boltzmann kalkulatora.


Boltzmann kalkulator je alat koji vam omogućava da lako izračunate različite napredne metrike na Bitcoin transakciji, uključujući njen nivo entropije. Svi ovi podaci će vam omogućiti da kvantifikujete nivo privatnosti transakcije i otkrijete bilo kakve potencijalne greške. Ovaj alat je unapred instaliran na vašem RoninDojo čvoru.


Da biste mu pristupili iz RoninCLI, povežite se putem SSH-a, a zatim idite na meni:

**Samourai Toolkit > Boltzmann Calculator**


Pre nego što objasnim kako se koristi na RoninDojo, objasniću šta ove metrike predstavljaju, kako se izračunavaju i za šta se koriste.


Ovi indikatori mogu se koristiti za bilo koju Bitcoin transakciju, ali su posebno zanimljivi za proučavanje kvaliteta CoinJoin transakcije.


1. Prvi indikator koji izračunava ovaj softver je broj mogućih kombinacija. Na kalkulatoru je označen kao "nb combinations". S obzirom na vrednosti UTXO-a, ovaj indikator predstavlja broj mogućih mapiranja od ulaza ka izlazima.


**napomena:** ako niste upoznati sa terminom `UTXO`, preporučujem da pročitate ovaj kratki članak:


> Mehanizam Bitcoin transakcije: UTXO, ulazi i izlazi.

Drugim rečima, ovaj indikator predstavlja broj mogućih interpretacija za određenu transakciju. Na primer, struktura Whirlpool 5x5 CoinJoin će imati broj mogućih kombinacija jednak 1496:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Kredit: KYCP


2. Drugi izračunati indikator je entropija transakcije. Pošto broj mogućih kombinacija može biti veoma visok za transakciju, može se odlučiti da se umesto toga koristi entropija. Entropija predstavlja binarni logaritam broja mogućih kombinacija. Njena formula je sledeća:



- E: entropija transakcije.
- C: broj mogućih kombinacija za transakciju.


**E = log2(C)**


U matematici, binarni logaritam (osnova 2) je inverzna funkcija funkcije stepena broja 2. Drugim rečima, binarni logaritam od x je stepen na koji broj 2 mora biti podignut da bi se dobila vrednost x.


Tako:


**E = log2(C)**


**C = 2^E**


Ovaj indikator je izražen u bitovima. Na primer, ovde je izračunata entropija transakcije Whirlpool 5x5 CoinJoin, sa prethodno pomenutim brojem mogućih kombinacija jednakim 1496:


**C = 1496**


**E = log2(1496)**


**E = 10.5469 bita**


Dakle, ova transakcija CoinJoin ima entropiju od 10.5469 bita, što je veoma dobro.


Što je ovaj indikator viši, to postoji više različitih interpretacija transakcije, i stoga je transakcija poverljivija.


Hajde da uzmemo još jedan primer. Evo "klasične" transakcije koja ima jedan ulaz i dva izlaza:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Kredit: OXT


Ova transakcija ima samo jedno moguće tumačenje:


**[(inp 0) > (Outp 0 ; Outp 1)]**


Dakle, njegova entropija će biti jednaka 0:


**C = 1**,

**E = log2(C)**,

**E = 0**


3. Treći indikator koji vraća Boltzmann kalkulator je efikasnost Tx nazvana "Wallet Efficiency". Ovaj indikator jednostavno omogućava poređenje ulazne transakcije sa najboljom mogućom transakcijom u istoj konfiguraciji.


Sada ćemo uvesti koncept maksimalne entropije, koja predstavlja najvišu dostižnu entropiju za datu strukturu transakcije. Na primer, struktura Whirlpool 5x5 CoinJoin će imati maksimalnu entropiju od 10.5469. Indikator efikasnosti upoređuje ovu maksimalnu entropiju sa stvarnom entropijom ulazne transakcije. Njegova formula je sledeća:



- ER: Stvarna entropija izražena u bitovima.
- EM: Maksimalna entropija sa istom strukturom izražena u bitovima.
- Ef: Efikasnost izražena u bitovima.


**Ef = ER - EM**


**Ef = 10.5469 - 10.5469**


**Ef = 0 bita**


Ovaj indikator se takođe izražava kao procenat, pa formula postaje:



- CR: Stvarni broj mogućih kombinacija.
- CM: Maksimalan broj mogućih kombinacija sa istom strukturom.
- Ef: Efikasnost izražena kao procenat.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


Efikasnost od 100% znači da ova transakcija ima najviši mogući nivo privatnosti u odnosu na svoju strukturu.


4. Četvrti izračunati indikator je gustina entropije. Omogućava nam da povežemo entropiju sa svakim ulazom ili izlazom. Ovaj indikator se može koristiti za poređenje efikasnosti između transakcija različitih veličina.


Njegova kalkulacija je veoma jednostavna: delimo entropiju transakcije brojem prisutnih ulaza i izlaza. Na primer, za Whirlpool 5x5 CoinJoin, imali bismo:


ED: Gustina entropije izražena u bitovima.

E: Entropija transakcije izražena u bitovima.

T: Ukupan broj ulaza i izlaza u transakciji.


T = 5 + 5 = 10

ED = E / T

ED = 10.5469 / 10

ED = 1.054 bita


Peti podatak koji pruža Boltzmann kalkulator je tabela verovatnoće veza između ulaza i izlaza. Ova tabela jednostavno daje verovatnoću (Boltzmann skor) da određeni ulaz odgovara određenom izlazu.


Ako uzmemo naš primer sa Whirlpool CoinJoin, tabela verovatnoće bi bila:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Ovde možemo videti da svaki ulaz ima jednaku verovatnoću da bude povezan sa svakim izlazom.


Međutim, ako uzmemo primer transakcije sa jednim ulazom i dva izlaza, izgledalo bi ovako:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

U ovom primeru, možemo videti da je verovatnoća svakog izlaza koji dolazi iz ulaza 0 100%.


Što je niža ova verovatnoća, to je viši nivo poverljivosti.


6. Šesti podatak koji se izračunava je broj determinističkih veza. Takođe će biti obezbeđen odnos determinističkih veza. Ovaj indikator ističe broj veza između ulaza i izlaza date transakcije koje imaju verovatnoću od 100%, što znači da su neosporne.


Odnos ukazuje na broj determinističkih veza u transakciji u poređenju sa ukupnim brojem veza.


Na primer, transakcija CoinJoin Whirlpool nema determinističke veze između ulaza i izlaza. Pokazatelj će biti nula, a odnos će takođe biti 0%.


Međutim, za drugu proučavanu transakciju (1 ulaz i 2 izlaza), indikator je 2, a odnos je 100%.


Dakle, ako je ovaj indikator nula, to ukazuje na dobru poverljivost.


Sada kada smo proučili indikatore, hajde da vidimo kako da ih izračunamo koristeći ovaj softver. Iz RoninCLI, idite na meni:

**Samourai Toolkit > Boltzmann Calculator**


![Boltzmann Calculator software homepage](assets/35.webp)


Jednom kada je softver pokrenut, unesite transaction ID koji želite da proučite. Možete uneti više transakcija odjednom tako što ćete ih odvojiti zarezom, a zatim pritisnite enter:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


Kalkulator će zatim vratiti sve indikatore koje smo ranije videli:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Ukucajte komandu "Quit" da izađete iz softvera i vratite se u RoninCLI meni.


Da biste saznali više o Boltzmann kalkulatoru, preporučujem čitanje ovih članaka:



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Povezivanje Bisq-a.


Bisq je peer-to-peer platforma za razmenu koja vam omogućava kupovinu i prodaju bitcoina. Koristi se sa desktop softverom koji radi na Toru i omogućava vam da razmenite bitcoine bez potrebe da otkrijete svoj identitet.

Bisq osigurava peer-to-peer razmene putem 2/2 sistema sa više potpisa. Možete koristiti ovaj softver sa svojim RoninDojo čvorom kako biste optimizovali privatnost svojih razmena i verovali Blockchain podacima sa vašeg čvora.


Da biste preuzeli Bisq softver, idite na njihovu zvaničnu veb stranicu: https://bisq.network/


Da biste započeli sa softverom, preporučujem da pročitate ovu stranicu: https://bisq.network/getting-started/


Da biste preuzeli vezu za povezivanje sa vašeg RoninDojo, potrebno je da se povežete sa RoninCLI putem SSH. Zatim idite na meni:

**Applications > Manage Applications**


Unesite svoju lozinku, zatim označite polje razmakom:

**[ ] Enable Bisq Connection**


Potvrdite svoj izbor. Neka se vaš čvor instalira, a zatim preuzmite Tor V3 adresu sa:

**Credentials > Bitcoind**


Kopiraj adresu ispod "Bitcoin daemon".


Takođe možete preuzeti svoj bitcoind Tor V3 adresu iz RoninUI interfejsa jednostavnim klikom na "Manage" u okviru "Bitcoin Core" na "Dashboard":


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Da povežete svoj čvor iz Bisq-a, idite na meni:

**Settings > Network Info**


![Access the node connection interface from the Bisq software](assets/39.webp)


Kliknite na balon "Use custom Bitcoin Core nodes". Zatim unesite vaš Bitcoin TorV3 adresu u predviđeno polje, sa ".onion" ali bez "http://".


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Ponovo pokrenite Bisq softver. Vaš čvor je sada povezan sa vašim Bisq.


### Druge funkcije.


Vaš RoninDojo čvor takođe uključuje i druge osnovne funkcije. Imate mogućnost skeniranja specifičnih informacija kako biste osigurali da se one uzmu u obzir.


Na primer, ponekad je moguće da vaš novčanik povezan sa vašim RoninDojo ne pronađe bitkoine koji vam pripadaju. Stanje je 0 iako ste sigurni da imate Bitcoin u ovom novčaniku. Postoji mnogo mogućih uzroka koje treba razmotriti, uključujući grešku u putanjama derivacije, a među njima je takođe moguće da vaš čvor ne posmatra vaše adrese.


Da biste to popravili, možete proveriti da vaš čvor prati vaš xpub pomoću "xpub alata". Da biste mu pristupili iz RoninUI, idite na meni:

**Maintenance > XPUB Tool**


Unesite problematični xpub i kliknite "Check" da biste verifikovali ove informacije.


![XPUB Tool from RoninUI](assets/41.webp)


Ako vaš xpub prati čvor, videćete da se ovo pojavljuje:


![XPUB Tool result showing successful analysis](assets/42.webp)


Proverite da su sve transakcije ispravno prikazane. Takođe, proverite da li tip derivacije odgovara onom na vašem novćaniku. Ovde možemo videti da čvor interpretira ovaj xpub kao BIP44 derivaciju. Ako ovaj tip derivacije ne odgovara onom na vašem novčaniku, kliknite na dugme "Retype", zatim izaberite BIP44/BIP49/BIP84 prema vašem izboru:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Ako vaš xpub nije praćen od strane vašeg čvora, videćete ovaj ekran koji vas poziva da ga uvezete:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Takođe možete koristiti druge alate za održavanje:



- Alat za transakcije: Omogućava vam da posmatrate detalje određene transakcije.
- Alat za adrese: Omogućava vam da proverite da li određenu adresu prati vaš Dojo.
- Ponovno skeniraj blokove: Prisiljava vaš čvor da ponovo skenira odabrani raspon blokova.


Takođe ćete pronaći alat "Push Tx" na RoninUI. Omogućava vam da emitujete potpisanu transakciju na Bitcoin mrežu. Mora biti uneta u heksadecimalnom formatu:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Zaključak.


Videli smo kako instalirati i započeti sa ovim divnim alatom koji je RoninDojo. To je odličan izbor za pokretanje sopstvenog Bitcoin čvora. To je stabilno rešenje koje integriše i održava ažuriranim sve esencijalne alate za Bitkoinera.


Ako vas korišćenje terminala ne plaši i ako vam nisu potrebni alati povezani sa Lightning mrežom, onda bi vam RoninDojo mogao biti privlačan.


Ako možete, razmislite o doniranju programerima koji besplatno proizvode ovaj open-source softver za vas: https://donate.ronindojo.io/


Da biste saznali više o RoninDojo-u, preporučujem da pogledate linkove u mojim spoljnim resursima ispod.


### Dalje čitanje:



- Razumevanje i korišćenje CoinJoin-a na Bitcoin-u.
- Hash funkcije - izvod iz e-knjige Bitcoin Démocratisé 1.
- Sve što treba da znate o Bitcoin passphrase.


### Spoljni resursi:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
