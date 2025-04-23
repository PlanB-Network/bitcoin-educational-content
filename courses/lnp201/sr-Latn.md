---
name: Teorijsko Uvodjenje u Lightning Network
goal: Otkrijte Lightning Network iz tehničke perspektive
objectives: 

  - Razumeti rad kanala mreže.
  - Upoznajte se sa terminima HTLC, LNURL i UTXO.
  - Asimilirati upravljanje likvidnošću i naknade LNN-a.
  - Prepoznajte Lightning Network kao mrežu.
  - Razumeti teorijske upotrebe Lightning Network.

---

# Putovanje do Bitcoin-ovog Drugog Layer


Zaronite u srž Lightning Network, esencijalnog sistema za budućnost Bitcoin transakcija. LNP201 je teorijski kurs o tehničkom funkcionisanju Lightning-a. Otkriva osnove i mehanizme ove druge Layer mreže, dizajnirane da učini Bitcoin plaćanja brzim, ekonomičnim i skalabilnim.


Zahvaljujući svojoj mreži platnih kanala, Lightning omogućava brze i sigurne transakcije bez beleženja svakog Exchange na Bitcoin Blockchain. Kroz poglavlja ćete naučiti kako funkcioniše otvaranje, upravljanje i zatvaranje kanala, kako se plaćanja sigurno usmeravaju kroz posredničke čvorove uz minimiziranje potrebe za poverenjem, i kako upravljati likvidnošću. Otkrićete šta su Commitment transakcije, HTLC-ovi, ključevi opoziva, mehanizmi kažnjavanja, lukovi usmeravanja i fakture.


Bilo da ste početnik sa Bitcoin ili iskusniji korisnik, ovaj kurs će pružiti dragocene informacije za razumevanje i korišćenje Lightning Network. Iako ćemo pokriti neke osnove rada Bitcoin u prvim delovima, važno je savladati osnove izuma Satoshi pre nego što se upustite u LNP201.


Uživaj u svom otkriću!


+++

# Uvod

<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>


## Pregled kursa

<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>


Dobrodošli na kurs LNP201!


Ova obuka ima za cilj da vam pruži detaljno tehničko razumevanje Lightning Network, mreže koja je dizajnirana da olakša brze i često niskotarifne Bitcoin transakcije. Postepeno ćete otkrivati osnovne pojmove koji upravljaju ovim sistemom, od otvaranja platnih kanala do tehnika rutiranja i upravljanja likvidnošću.


**Sekcija 1: Osnove**

Počećemo sa opštim uvodom u Lightning Network, uspostavljajući osnovne temelje o Bitcoin, njegovim adresama, UTXO-ima i načinu na koji transakcije funkcionišu. Ovaj osnovni pregled je neophodan da bismo razumeli kako Lightning Network oslanja na osnovne mehanizme Blockchain za sigurno funkcionisanje.


**Sekcija 2: Otvaranje i Zatvaranje Kanala**

U ovom odeljku ćemo istražiti proces otvaranja kanala, koji je kamen temeljac Lightning Network. Naučićete kako se kreiraju Commitment transakcije, ulogu ključeva za opoziv za bezbednost, i kako se kanali mogu zatvoriti bilo kolaborativno ili jednostrano. Svaki korak će biti precizno i tehnički objašnjen kako biste razumeli sve suptilnosti.


**Section 3: Mreža Likvidnosti**

Lightning Network nije ograničen na pojedinačne kanale; to je prava mreža plaćanja. Videćemo kako transakcije mogu biti usmerene kroz posredničke čvorove koristeći HTLC-ove. Ovaj deo će vas takođe upoznati sa izazovima dolazne i odlazne likvidnosti.


**Sekcija 4: Lightning Network Alati**

Ovaj odeljak predstavlja praktične alate Lightning Network, kao što su *Invoices*, *LNURL* i *Keysend*. Takođe ćete naučiti kako da upravljate likvidnošću svojih kanala, što je ključni aspekt za osiguranje nesmetanih plaćanja i maksimiziranje efikasnosti vaših transakcija na Lightning-u.


**Sekcija 5: Dalje istraživanje**

Na kraju, završićemo obuku ponavljanjem obrađenih pojmova i otvaranjem puta ka naprednijim temama za one koji žele da prodube svoje znanje o Lightning Network.


Spremni da otkrijete tehničke mehanizme Lightning Network? Hajde da zaronimo!


# Osnovi


<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>


## Razumevanje Lightning Network


<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::



Lightning Network je mreža platnih kanala izgrađena na vrhu Bitcoin protokola, sa ciljem omogućavanja brzih i niskotarifnih transakcija. Omogućava kreiranje platnih kanala između učesnika, unutar kojih se transakcije mogu obavljati gotovo trenutno i uz minimalne naknade, bez potrebe za pojedinačnim beleženjem svake transakcije na Blockchain. Tako, Lightning Network nastoji poboljšati skalabilnost Bitcoin i učiniti ga upotrebljivim za plaćanja male vrednosti.


Pre nego što istražimo aspekt "mreže", važno je razumeti koncept **kanala plaćanja** na Lightning-u, kako funkcioniše i njegove specifičnosti. Ovo je tema prvog poglavlja.


### Koncept platnog kanala


Kanal plaćanja omogućava dvema stranama, ovde **Alice** i **Bob**, da Exchange sredstva preko Lightning Network. Svaki protagonist ima čvor, simbolizovan krugom, a kanal između njih je predstavljen linijskim segmentom.


![LNP201](assets/en/01.webp)


U našem primeru, Alis ima 100.000 satoshija na svojoj strani kanala, a Bob ima 30.000, što ukupno čini 130.000 satoshija, što predstavlja **kapacitet kanala**.


**Ali šta je Satoshi?**


**Satoshi** (ili "sat") je obračunska jedinica na Bitcoin. Slično kao cent za evro, Satoshi je jednostavno frakcija Bitcoin. Jedan Satoshi je jednak **0.00000001 Bitcoin**, ili jedna stomilionitina Bitcoin. Korišćenje Satoshi postaje sve praktičnije kako vrednost Bitcoin raste.


### Alokacija sredstava u kanalu


Hajde da se vratimo na kanal plaćanja. Ključni koncept ovde je "**strana kanala**". Svaki učesnik ima sredstva na svojoj strani kanala: Alis 100.000 satoshija i Bob 30.000. Kao što smo videli, zbir ovih sredstava predstavlja ukupni kapacitet kanala, cifra koja se postavlja kada se otvori.


![LNP201](assets/en/02.webp)


Hajde da uzmemo primer Lightning transakcije. Ako Alisa želi da pošalje 40.000 satoshija Bobu, to je moguće jer ima dovoljno sredstava (100.000 satoshija). Nakon ove transakcije, Alisa će imati 60.000 satoshija na svojoj strani, a Bob 70.000.


![LNP201](assets/en/03.webp)


**Kapacitet kanala**, na 130.000 satoshija, ostaje konstantan. Ono što se menja je raspodela sredstava. Ovaj sistem ne dozvoljava slanje više sredstava nego što neko poseduje. Na primer, ako Bob želi da pošalje nazad 80.000 satoshija Alisi, ne bi mogao, jer ima samo 70.000.


Još jedan način da zamislite raspodelu sredstava je da zamislite **klizač** koji pokazuje gde se sredstva nalaze u kanalu. U početku, sa 100.000 satoshija za Alisu i 30.000 za Boba, klizač je logično na Alisinoj strani. Nakon transakcije od 40.000 satoshija, klizač će se pomeriti blago ka Bobovoj strani, koji sada ima 70.000 satoshija.


![LNP201](assets/en/04.webp)


Ova reprezentacija može biti korisna za zamišljanje ravnoteže sredstava u kanalu.


### Osnovna pravila platnog kanala


Prva stvar koju treba zapamtiti je da je **kapacitet kanala** fiksiran. To je donekle kao prečnik cevi: određuje maksimalnu količinu sredstava koja se mogu poslati kroz kanal odjednom.

Hajde da uzmemo primer: ako Alisa ima 130.000 satoshija na svojoj strani, može poslati maksimalno 130.000 satoshija Bobu u jednoj transakciji. Međutim, Bob može zatim poslati ta sredstva nazad Alisi, bilo delimično ili u celosti.


Važno je razumeti da fiksni kapacitet kanala ograničava maksimalni iznos jedne transakcije, ali ne i ukupan broj mogućih transakcija, niti ukupni obim sredstava razmenjenih unutar kanala.


**Šta bi trebalo da izvučete iz ovog poglavlja?**



- Kapacitet kanala je fiksiran i određuje maksimalnu količinu koja se može poslati u jednoj transakciji.
- Sredstva u kanalu su raspodeljena između dva učesnika, i svaki može poslati drugom samo sredstva koja poseduju na svojoj strani.
- Lightning Network na taj način omogućava brzo i efikasno Exchange sredstava, uz poštovanje ograničenja nametnutih kapacitetom kanala.


Ovo je kraj prvog poglavlja, gde smo postavili osnove za Lightning Network. U narednim poglavljima ćemo videti kako otvoriti kanal i dublje istražiti ovde diskutovane koncepte.


## Bitcoin, Adrese, UTXO, i Transakcije


<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>


:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::


Ovo poglavlje je pomalo posebno jer neće biti direktno posvećeno Lightning-u, već Bitcoin. Naime, Lightning Network je Layer na vrhu Bitcoin. Stoga je neophodno razumeti određene fundamentalne koncepte Bitcoin kako bi se pravilno shvatilo funkcionisanje Lightning-a u narednim poglavljima. U ovom poglavlju ćemo pregledati osnove Bitcoin adresa za primanje, UTXO-e, kao i funkcionisanje Bitcoin transakcija.


### Bitcoin Adrese, Privatni Ključevi, i Javni Ključevi


Bitcoin Address je niz karaktera izveden iz **javnog ključa**, koji se sam izračunava iz **privatnog ključa**. Kao što sigurno znate, koristi se za zaključavanje bitkoina, što je ekvivalentno njihovom primanju u naš Wallet.


Privatni ključ je tajni element koji **nikada ne treba deliti**, dok se javni ključ i Address mogu deliti bez rizika po bezbednost (njihovo otkrivanje predstavlja rizik samo za vašu privatnost). Ovde je uobičajena reprezentacija koju ćemo usvojiti tokom ove obuke:



- **Privatni ključevi** će biti predstavljeni **vertikalno**.
- **Javni ključevi** će biti predstavljeni **horizontalno**.
- Njihova boja označava ko ih poseduje (Alisa u narandžastom i Bob u crnom...).


### Transakcije Bitcoin: Slanje sredstava i skripti


Na Bitcoin, transakcija uključuje slanje sredstava sa jednog Address na drugi. Uzmimo primer gde Alisa šalje 0.002 Bitcoin Bobu. Alisa koristi privatni ključ povezan sa njenim Address da **potpiše** transakciju, čime dokazuje da zaista može da potroši ta sredstva. Ali šta se tačno dešava iza ove transakcije? Sredstva na Bitcoin Address su zaključana **skriptom**, vrstom mini-programa koji nameće određene uslove za trošenje sredstava.


Najčešći skript zahteva potpis sa privatnim ključem povezanim sa Address. Kada Alisa potpiše transakciju svojim privatnim ključem, ona **otključava skript** koji blokira sredstva, i tada se ona mogu preneti. Prenos sredstava uključuje dodavanje novog skripta tim sredstvima, koji propisuje da će za njihovo trošenje ovog puta biti potreban potpis privatnog ključa **Boba**.


![LNP201](assets/en/05.webp)


### UTXOs: Neutrošeni Izlazi Transakcija


Na Bitcoin, ono što mi zapravo Exchange nisu direktno bitcoini, već **UTXO-i** (_Unspent Transaction Outputs_), što znači "nepotrošeni izlazi transakcija".


UTXO je deo Bitcoin koji može imati bilo koju vrednost, na primer, **2,000 bitcoina**, **8 bitcoina**, ili čak **8,000 Sats**. Svaki UTXO je zaključan skriptom, i da bi se potrošio, mora se ispuniti uslov skripta, što je često potpis sa privatnim ključem koji odgovara datom primajućem Address.


UTXO-i se ne mogu deliti. Svaki put kada se koriste za trošenje iznosa u bitcoinima koji predstavljaju, to mora biti učinjeno u celosti. To je pomalo kao novčanica: ako imate novčanicu od €10 i dugujete pekaru €5, ne možete jednostavno preseći novčanicu na pola. Morate mu dati novčanicu od €10, a on će vam vratiti €5 kusura. Ovo je tačno isti princip za UTXO-e na Bitcoin! Na primer, kada Alisa otključa skriptu svojim privatnim ključem, ona otključava celu UTXO. Ako želi da pošalje samo deo sredstava predstavljenih ovom UTXO Bobu, može je "fragmentirati" na nekoliko manjih. Zatim će poslati 0.0015 BTC Bobu i poslati ostatak, 0.0005 BTC, na **kusur Address**.


Evo primera transakcije sa 2 izlaza:



- UTXO od 0.0015 BTC za Boba, zaključan skriptom koji zahteva Bobov potpis privatnim ključem.
- UTXO od 0.0005 BTC za Alisu, zaključan skriptom koji zahteva njen sopstveni potpis.


![LNP201](assets/en/06.webp)


### Višepotpisne Adrese


Pored jednostavnih adresa generisanih iz jednog javnog ključa, moguće je kreirati **adrese sa više potpisa** iz više javnih ključeva. Posebno zanimljiv slučaj za Lightning Network je **2/2 adresa sa više potpisa Address**, generisana iz dva javna ključa:


![LNP201](assets/en/07.webp)


Da biste potrošili sredstva zaključana sa ovom 2/2 multi-potpisnom Address, potrebno je potpisati sa dva privatna ključa povezana sa javnim ključevima.


![LNP201](assets/en/08.webp)


Ovaj tip Address je upravo reprezentacija na Bitcoin Blockchain kanala plaćanja na Lightning Network.


**Šta bi trebalo da izvučete iz ovog poglavlja?**



- **Bitcoin Address** je izveden iz javnog ključa, koji je sam izveden iz privatnog ključa.
- Sredstva na Bitcoin su zaključana pomoću **skripti**, i da bi se ta sredstva potrošila, potrebno je zadovoljiti skriptu, što obično podrazumeva davanje potpisa sa odgovarajućim privatnim ključem.
- UTXO-i** su delovi bitkoina zaključani skriptama, i svaka transakcija na Bitcoin se sastoji od otključavanja UTXO i zatim kreiranja jednog ili više novih u zamenu.
- 2/2 multi-signature adrese** zahtevaju potpis dva privatna ključa za trošenje sredstava. Ove specifične adrese se koriste u kontekstu Lightning-a za kreiranje platnih kanala.


Ovo poglavlje o Bitcoin omogućilo nam je da pregledamo neke osnovne pojmove za ono što sledi. U sledećem poglavlju ćemo posebno otkriti kako funkcioniše otvaranje kanala na Lightning Network.


# Otvaranje i zatvaranje kanala


<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>


## Otvaranje kanala


<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>


:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::


U ovom poglavlju ćemo preciznije videti kako otvoriti platni kanal na Lightning Network i razumeti vezu između ove operacije i osnovnog Bitcoin sistema.


### Kanali munja


Kao što smo videli u prvom poglavlju, **kanal plaćanja** na Lightning mreži može se uporediti sa "cevi" za razmenu sredstava između dva učesnika (**Alice** i **Bob** u našim primerima). Kapacitet ovog kanala odgovara zbiru dostupnih sredstava na svakoj strani. U našem primeru, Alice ima **100.000 satoshija** i Bob ima **30.000 satoshija**, što daje **ukupni kapacitet** od **130.000 satoshija**.


![LNP201](assets/en/09.webp)


### Nivoi informacija Exchange


Ključno je jasno razlikovati različite nivoe Exchange na Lightning Network:



- Komunikacija od tačke do tačke (Lightning protokol)**: Ovo su poruke koje Lightning čvorovi šalju jedni drugima radi komunikacije. Ove poruke ćemo predstavljati isprekidanim crnim linijama u našim dijagramima.
- Kanali plaćanja (Lightning protokol)**: Ovo su putevi za razmenu sredstava na Lightning-u, koje ćemo predstaviti punim crnim linijama.
- Transakcije Bitcoin (protokol Bitcoin)**: Ovo su transakcije napravljene na lancu, koje ćemo predstaviti narandžastim linijama.


![LNP201](assets/en/10.webp)


Vredi napomenuti da Lightning čvor može komunicirati putem P2P protokola bez otvaranja kanala, ali za Exchange sredstva, kanal je neophodan.


### Koraci za otvaranje Lightning kanala



- Poruka Exchange**: Alisa želi da otvori kanal sa Bobom. Ona mu šalje poruku koja sadrži iznos koji želi da deponuje u kanalu (130,000 Sats) i njen javni ključ. Bob odgovara deljenjem svog javnog ključa.


![LNP201](assets/en/11.webp)



- Kreiranje multisignature Address**: Sa ova dva javna ključa, Alisa kreira **2/2 multisignature Address**, što znači da će sredstva koja će kasnije biti deponovana na ovaj Address zahtevati oba potpisa (Alise i Boba) da bi bila potrošena.


![LNP201](assets/en/12.webp)



- Transakcija depozita**: Alisa priprema Bitcoin transakciju za deponovanje sredstava na ovaj multisignature Address. Na primer, može odlučiti da pošalje **130.000 satoshija** na ovaj multisignature Address. Ova transakcija je **konstruisana, ali još nije objavljena** na Blockchain.


![LNP201](assets/en/13.webp)



- Transakcija povlačenja**: Pre nego što objavi transakciju depozita, Alisa konstruira transakciju povlačenja kako bi mogla povratiti svoja sredstva u slučaju problema sa Bobom. Naime, kada Alisa objavi transakciju depozita, njen Sats će biti zaključan na 2/2 multisignature Address koji zahteva i njen i Bobov potpis za otključavanje. Alisa se štiti od ovog rizika gubitka konstruisanjem transakcije povlačenja koja joj omogućava da povrati svoja sredstva.


![LNP201](assets/en/14.webp)



- Bobov potpis**: Alisa šalje transakciju depozita Bobu kao dokaz i traži od njega da potpiše transakciju povlačenja. Kada se dobije Bobov potpis na transakciji povlačenja, Alisa je sigurna da može povratiti svoja sredstva u bilo kom trenutku, jer je sada potreban samo njen potpis da bi se otključao višestruki potpis.


![LNP201](assets/en/15.webp)



- Objavljivanje transakcije depozita**: Kada se Bobov potpis dobije, Alisa može objaviti transakciju depozita na Bitcoin Blockchain, čime se zvanično otvara Lightning kanal između dva korisnika.


![LNP201](assets/en/16.webp)


### Kada je kanal otvoren?


Kanal se smatra otvorenim kada je transakcija depozita uključena u Bitcoin blok i dostigne određenu dubinu potvrda (broj sledećih blokova).


**Šta treba da zapamtiš iz ovog poglavlja?**



- Otvaranje kanala počinje sa Exchange **poruka** između dve strane (Exchange iznosa i javnih ključeva).
- Kanal se formira kreiranjem **2/2 multisignature Address** i deponovanjem sredstava u njega putem Bitcoin transakcije.
- Osoba koja otvara kanal osigurava da može **povratiti svoja sredstva** putem transakcije povlačenja potpisane od strane druge strane pre objavljivanja transakcije depozita.


U narednom poglavlju, istražićemo tehnički rad Lightning transakcije unutar kanala.


## Commitment Transaction


<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>


:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::


U ovom poglavlju ćemo otkriti tehničko funkcionisanje transakcije unutar kanala na Lightning Network, to jest, kada se sredstva premeštaju sa jedne strane kanala na drugu.


### Podsetnik o životnom ciklusu kanala


Kao što je ranije viđeno, Lightning kanal počinje sa **otvaranjem** putem Bitcoin transakcije. Kanal se može **zatvoriti** u bilo kom trenutku, takođe putem Bitcoin transakcije. Između ova dva trenutka, unutar kanala se može izvršiti gotovo beskonačan broj transakcija, bez prolaska kroz Bitcoin Blockchain. Pogledajmo šta se dešava tokom transakcije u kanalu.


![LNP201](assets/en/17.webp)


### Početno stanje kanala


U trenutku otvaranja kanala, Alisa je deponovala **130.000 satoshija** na multisignature Address kanala. Dakle, u početnom stanju, sva sredstva su na Alisinoj strani. Pre otvaranja kanala, Alisa je takođe tražila od Boba da potpiše **transakciju povlačenja**, koja bi joj omogućila da povrati svoja sredstva ako želi da zatvori kanal.


![LNP201](assets/en/18.webp)


### Neobjavljene transakcije: Commitment transakcije


Kada Alisa izvrši transakciju u kanalu da pošalje sredstva Bobu, kreira se nova Bitcoin transakcija kako bi se odrazila ova promena u raspodeli sredstava. Ova transakcija, nazvana **Commitment Transaction**, nije objavljena na Blockchain, ali predstavlja novo stanje kanala nakon Lightning transakcije.


Hajde da uzmemo primer gde Alisa šalje 30.000 satoshija Bobu:



- Inicialno**: Alisa ima 130.000 satoshija.
- Nakon transakcije**: Alisa ima 100.000 satoshija, a Bob 30.000 satoshija.

Da bi potvrdili ovaj transfer, Alice i Bob kreiraju novu **neobjavljenu Bitcoin transakciju** koja bi poslala **100.000 satoshija Alice** i **30.000 satoshija Bobu** iz multisignature Address. Obe strane konstruiraju ovu transakciju nezavisno, ali sa istim podacima (iznosima i adresama). Kada je konstruisana, svaka potpisuje transakciju i razmenjuje svoj potpis sa drugom stranom. Ovo omogućava bilo kojoj strani da objavi transakciju u bilo kom trenutku ako je potrebno da povrate svoj deo kanala na glavnom Bitcoin Blockchain.

![LNP201](assets/en/19.webp)


### Proces prenosa: Invoice


Kada Bob želi da primi sredstva, on šalje Alisi **_fakturu_** za 30.000 satoshija. Alisa zatim nastavlja sa plaćanjem ovog Invoice započinjanjem transfera unutar kanala. Kao što smo videli, ovaj proces se oslanja na kreiranje i potpisivanje novog **Commitment Transaction**.


Svaki Commitment Transaction predstavlja novu raspodelu sredstava u kanalu nakon transfera. U ovom primeru, nakon transakcije, Bob ima 30,000 satoshija, a Alice ima 100,000 satoshija. Ako bilo koji od dva učesnika odluči da objavi ovaj Commitment Transaction na Blockchain, to bi rezultiralo zatvaranjem kanala i sredstva bi bila raspodeljena prema ovoj poslednjoj raspodeli.


![LNP201](assets/en/20.webp)


### Nova država nakon druge transakcije


Hajde da uzmemo drugi primer: nakon prve transakcije gde je Alisa poslala 30.000 satoshija Bobu, Bob odlučuje da pošalje **10.000 satoshija nazad Alisi**. Ovo stvara novo stanje kanala. Novi **Commitment Transaction** će predstavljati ovu ažuriranu distribuciju:



- Alice** sada ima **110.000 satoshija**.
- Bob** ima **20.000 satoshija**.


![LNP201](assets/en/21.webp)


Ponovo, ova transakcija nije objavljena na Blockchain, ali može biti u bilo kom trenutku u slučaju da je kanal zatvoren.


Ukratko, kada se sredstva prenose unutar Lightning kanala:



- Alice i Bob kreiraju novi **Commitment Transaction**, koji odražava novu raspodelu sredstava.
- Ova transakcija Bitcoin je **potpisana** od strane obe strane, ali **nije objavljena** na Bitcoin Blockchain sve dok kanal ostaje otvoren.
- Transakcije Commitment osiguravaju da svaki učesnik može povratiti svoja sredstva u bilo kom trenutku na Bitcoin Blockchain objavljivanjem poslednje potpisane transakcije.


Međutim, ovaj sistem ima potencijalnu manu, koju ćemo Address u sledećem poglavlju. Videćemo kako svaki učesnik može zaštititi sebe od pokušaja prevare od strane druge strane.


## Ključ za opoziv


<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

U ovom poglavlju ćemo detaljnije istražiti kako transakcije funkcionišu na Lightning Network tako što ćemo diskutovati o mehanizmima koji su postavljeni da zaštite od varanja, osiguravajući da svaka strana poštuje pravila unutar kanala.


### Podsetnik: Commitment Transakcije


Kao što je ranije viđeno, transakcije na Lightning mreži oslanjaju se na neobjavljene **Commitment transakcije**. Ove transakcije odražavaju trenutnu raspodelu sredstava u kanalu. Kada se izvrši nova Lightning transakcija, kreira se novi Commitment Transaction i potpisuje od strane obe strane kako bi odražavao novo stanje kanala.


Hajde da uzmemo jednostavan primer:



- Početno stanje**: Alisa ima **100.000 satoshija**, Bob **30.000 satoshija**.
- Nakon transakcije u kojoj Alice šalje **40.000 satoshija** Bobu, novi Commitment Transaction raspoređuje sredstva na sledeći način:
  - Alice: **60.000 satoshija**
  - Bob: **70.000 satoshija**


![LNP201](assets/en/22.webp)


U bilo kom trenutku, obe strane mogu objaviti **najnoviji Commitment Transaction** potpisan za zatvaranje kanala i povrat svojih sredstava.


### Greška: Varanje objavljivanjem stare transakcije


Potencijalni problem nastaje ako jedna od strana odluči da **prevari** objavljivanjem starog Commitment Transaction. Na primer, Alisa bi mogla da objavi stariji Commitment Transaction gde je imala **100.000 satoshija**, iako sada u stvarnosti ima samo **60.000**. To bi joj omogućilo da ukrade **40.000 satoshija** od Boba.


![LNP201](assets/en/23.webp)


Čak i gore, Alisa bi mogla objaviti prvu transakciju povlačenja, onu pre nego što je kanal otvoren, gde je imala **130,000 satoshija**, i tako ukrasti sredstva celog kanala.


![LNP201](assets/en/24.webp)


### Rešenje: Ključ za opoziv i vremenska brava


Da bi se sprečila ovakva vrsta varanja od strane Alise, na Lightning Network, **sigurnosni mehanizmi** su dodati transakcijama Commitment:



- Vremenska brava**: Svaki Commitment Transaction uključuje vremensku bravu za Alicina sredstva. Vremenska brava je Smart contract primitiv koji postavlja vremenski uslov koji mora biti ispunjen da bi transakcija bila dodata u blok. To znači da Alice ne može povratiti svoja sredstva dok ne prođe određeni broj blokova ako objavi jednu od Commitment transakcija. Ova vremenska brava počinje da se primenjuje od potvrde Commitment Transaction. Njeno trajanje je uglavnom proporcionalno veličini kanala, ali se može i ručno konfigurisati.
- Revocation Key**: Alisina sredstva takođe može odmah potrošiti Bob ako poseduje **ključ opoziva**. Ovaj ključ se sastoji od tajne koju drži Alisa i tajne koju drži Bob. Imajte na umu da je ova tajna različita za svaki Commitment Transaction.

Zahvaljujući ova 2 kombinovana mehanizma, Bob ima vremena da otkrije Alisin pokušaj prevare i da je kazni povlačenjem svog izlaza pomoću ključa za opoziv, što za Boba znači povratak svih sredstava kanala. Naš novi Commitment Transaction će sada izgledati ovako:


![LNP201](assets/en/25.webp)


Hajde da zajedno detaljno opišemo funkcionisanje ovog mehanizma.


### Proces ažuriranja transakcije


Kada Alisa i Bob ažuriraju stanje kanala novom Lightning transakcijom, oni unapred Exchange svoje odgovarajuće **tajne** za prethodni Commitment Transaction (onaj koji će postati zastareo i mogao bi omogućiti jednom od njih da vara). To znači da, u novom stanju kanala:



- Alice i Bob imaju novi Commitment Transaction koji predstavlja trenutnu raspodelu sredstava nakon Lightning transakcije.
- Svaki ima tajnu onog drugog za prethodnu transakciju, što im omogućava da koriste ključ za opoziv samo ako jedan od njih pokuša da prevari objavljivanjem transakcije sa starim stanjem u mempoolovima čvorova Bitcoin. Zaista, da bi se kaznila druga strana, neophodno je imati obe tajne i Commitment Transaction onog drugog, koji uključuje potpisani ulaz. Bez ove transakcije, ključ za opoziv je beskoristan. Jedini način da se dobije ova transakcija je da se preuzme iz mempoolova (u transakcijama koje čekaju potvrdu) ili u potvrđenim transakcijama na Blockchain tokom vremenskog zaključavanja, što dokazuje da druga strana pokušava da prevari, bilo namerno ili ne.


Hajde da uzmemo primer kako bismo dobro razumeli ovaj proces:



- Početno stanje**: Alisa ima **100.000 satoshija**, Bob **30.000 satoshija**.


![LNP201](assets/en/26.webp)



- Bob želi da primi 40.000 satoshija od Alise putem njihovog Lightning kanala. Da bi to uradio:
   - On joj šalje Invoice zajedno sa svojom tajnom za opozivni ključ njegovog prethodnog Commitment Transaction.
   - Kao odgovor, Alisa pruža svoj potpis za Bobov novi Commitment Transaction, kao i svoju tajnu za opozivni ključ svoje prethodne transakcije.
   - Konačno, Bob šalje svoj potpis za Alisin novi Commitment Transaction.
   - Ove razmene omogućavaju Alisi da pošalje **40,000 satoshija** Bobu preko Lightning mreže putem njihovog kanala, a nove Commitment transakcije sada odražavaju ovu novu raspodelu sredstava.


![LNP201](assets/en/27.webp)



- Ako Alisa pokuša da objavi stari Commitment Transaction gde je još uvek posedovala **100,000 satoshija**, Bob, koji je pribavio ključ za opoziv, može odmah povratiti sredstva koristeći taj ključ, dok je Alisa blokirana vremenskim zaključavanjem.


![LNP201](assets/en/28.webp)


Čak i ako, u ovom slučaju, Bob nema ekonomski interes da pokuša da prevari, ako to ipak učini, Alis takođe ima koristi od simetrične zaštite koja joj nudi iste garancije.


**Šta bi trebalo da izvučete iz ovog poglavlja?**


**Transakcije Commitment** na Lightning Network uključuju sigurnosne mehanizme koji smanjuju i rizik od varanja i podsticaje za isto. Pre potpisivanja novog Commitment Transaction, Alice i Bob Exchange svoje odgovarajuće **tajne** za prethodne transakcije Commitment. Ako Alice pokuša da objavi stari Commitment Transaction, Bob može koristiti **ključ za opoziv** da povrati sva sredstva pre nego što Alice to može (jer je blokirana vremenskim zaključavanjem), što je kažnjava za pokušaj varanja.


Ovaj sigurnosni sistem osigurava da učesnici poštuju pravila Lightning Network, i ne mogu profitirati od objavljivanja starih Commitment transakcija.


U ovom trenutku obuke, sada znate kako se otvaraju Lightning kanali i kako funkcionišu transakcije unutar ovih kanala. U sledećem poglavlju, otkrićemo različite načine za zatvaranje kanala i povratak vaših bitkoina na glavnom Blockchain.


## Zatvaranje kanala


<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>


:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::


U ovom poglavlju ćemo diskutovati o **zatvaranju kanala** na Lightning Network, što se obavlja putem Bitcoin transakcije, baš kao i otvaranje kanala. Nakon što smo videli kako transakcije unutar kanala funkcionišu, sada je vreme da vidimo kako zatvoriti kanal i povratiti sredstva na Bitcoin Blockchain.


### Podsetnik o životnom ciklusu kanala


**Životni ciklus kanala** počinje njegovim **otvaranjem**, putem Bitcoin transakcije, zatim se unutar njega obavljaju Lightning transakcije, i na kraju, kada strane žele da povrate svoja sredstva, kanal se **zatvara** kroz drugu Bitcoin transakciju. Srednje transakcije obavljene na Lightning-u predstavljene su neobjavljenim **Commitment transakcijama**.


![LNP201](assets/en/29.webp)


### Tri vrste zatvaranja kanala


Postoje tri glavna načina da se zatvori ovaj kanal, koji se mogu nazvati **dobar, grub i neposlušan** (inspirisano Andreasom Antonopoulosom u _Mastering the Lightning Network_):



- The Good**: the **cooperative closure**, where Alice i Bob se dogovore da zatvore kanal.
- Loše**: **prisilno zatvaranje**, gde jedna od strana odluči da zatvori kanal pošteno, ali bez saglasnosti druge strane.
- The Ugly**: the **zatvaranje sa varanjem**, gde jedna od strana pokušava da ukrade sredstva objavljivanjem starog Commitment Transaction (bilo kojeg osim poslednjeg, koji odražava stvarnu i fer raspodelu sredstava).


Hajde da uzmemo primer:



- Alisa poseduje **100.000 satoshija**, a Bob **30.000 satoshija**.
- Ova distribucija se odražava u **2 Commitment transakcije** (jedna po korisniku) koje nisu objavljene, ali bi mogle biti u slučaju zatvaranja kanala.


![LNP201](assets/en/30.webp)


### Dobro: kooperativno zatvaranje


U **kooperativnom zatvaranju**, Alisa i Bob se dogovaraju da zatvore kanal. Evo kako to ide:



- Alice šalje poruku Bobu putem Lightning komunikacionog protokola da predloži zatvaranje kanala.
- Bob se slaže, i dve strane ne prave dalje transakcije u kanalu.


![LNP201](assets/en/31.webp)



- Alice i Bob zajedno pregovaraju o naknadama za **završnu transakciju**. Ove naknade se obično izračunavaju na osnovu Bitcoin tržišta naknada u trenutku zatvaranja. Važno je napomenuti da **uvek osoba koja je otvorila kanal** (Alice u našem primeru) plaća naknade za zatvaranje.
- Oni konstruiraju novu **završnu transakciju**. Ova transakcija podseća na Commitment Transaction, ali bez vremenskih zaključavanja ili mehanizama opoziva, jer obe strane sarađuju i nema rizika od varanja. Ova kooperativna završna transakcija je stoga drugačija od Commitment transakcija.


Na primer, ako Alisa poseduje **100.000 satoshija** a Bob **30.000 satoshija**, završna transakcija će poslati **100.000 satoshija** na Alisin Address i **30.000 satoshija** na Bobov Address, bez vremenskih ograničenja. Kada obe strane potpišu ovu transakciju, Alisa je objavljuje. Kada transakcija bude potvrđena na Bitcoin Blockchain, Lightning kanal će biti zvanično zatvoren.


![LNP201](assets/en/32.webp)


**Kooperativno zatvaranje** je preferirani metod zatvaranja jer je brzo (nema vremenskog zaključavanja) i naknade za transakcije su prilagođene prema trenutnim uslovima tržišta Bitcoin. Ovo izbegava plaćanje premalo, što bi moglo rizikovati blokiranje transakcije u mempool-ovima, ili preplaćivanje nepotrebno, što dovodi do nepotrebnog finansijskog gubitka za učesnike.


### Loše: prisilno zatvaranje


Kada Alisin čvor pošalje poruku Bobovom sa zahtevom za kooperativno zatvaranje, ako on ne odgovori (na primer, zbog prekida interneta ili tehničkog problema), Alisa može nastaviti sa **prisilnim zatvaranjem** objavljivanjem **poslednjeg potpisanog Commitment Transaction**.

U ovom slučaju, Alice će jednostavno objaviti poslednji Commitment Transaction, koji odražava stanje kanala u trenutku kada je poslednja Lightning transakcija obavljena sa pravilnom raspodelom sredstava.


![LNP201](assets/en/33.webp)


Ova transakcija uključuje **timelock** za Alisina sredstva, što usporava zatvaranje.


![LNP201](assets/en/34.webp)


Takođe, naknade za Commitment Transaction mogu biti nepogodne u trenutku zatvaranja, jer su postavljene kada je transakcija kreirana, ponekad nekoliko meseci ranije. Generalno, Lightning klijenti precenjuju naknade kako bi izbegli buduće probleme, ali to može dovesti do prekomernih naknada, ili obrnuto, previše niskih.


Ukratko, **prisilno zatvaranje** je opcija poslednjeg izbora kada vršnjak više ne odgovara. To je sporije i manje ekonomično od kooperativnog zatvaranja. Stoga ga treba izbegavati koliko god je to moguće.


### Prevara: varanje


Konačno, zatvaranje sa **varanjem** se dešava kada jedna od strana pokuša da objavi stari Commitment Transaction, često gde su držali više sredstava nego što bi trebalo. Na primer, Alisa bi mogla da objavi staru transakciju gde je posedovala **120.000 satoshija**, dok sada zapravo poseduje samo **100.000**.


![LNP201](assets/en/35.webp)


Bob, to prevent this cheating, monitors the Bitcoin Blockchain and its Mempool to ensure Alice does not publish an old transaction. If Bob detects a cheating attempt, he can use the **revocation key** to recover Alice's funds and punish her by taking the entire funds of the channel. Since Alice is blocked by the timelock on her output, Bob has time to spend it without a timelock on his side to recover the whole sum on an Address he owns.


![LNP201](assets/en/36.webp)


Očigledno, varanje može potencijalno uspeti ako Bob ne deluje u okviru vremena koje nameće vremenska brava na Alisinom izlazu. U tom slučaju, Alisin izlaz se otključava, omogućavajući joj da ga iskoristi za kreiranje novog izlaza na Address koji ona kontroliše.


**Šta bi trebalo da izvučete iz ovog poglavlja?**


Postoje tri načina za zatvaranje kanala:



- Kooperativno Zatvaranje**: Brzo i manje skupo, gde se obe strane slažu da zatvore kanal i objave prilagođenu transakciju zatvaranja.
- Prinudno Zatvaranje**: Manje poželjno, jer se oslanja na objavljivanje Commitment Transaction, sa potencijalno nepovoljnim naknadama i vremenskim zaključavanjem, što usporava zatvaranje.
- Varanje**: Ako jedna od strana pokuša da ukrade sredstva objavljivanjem stare transakcije, druga strana može koristiti ključ za opoziv da kazni ovo varanje.


U narednim poglavljima, istražićemo Lightning Network iz šire perspektive, fokusirajući se na to kako njegova mreža funkcioniše.


# Mreža Likvidnosti


<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>


## Lightning Network


<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::


U ovom poglavlju ćemo istražiti kako uplate na Lightning Network mogu stići do primaoca čak i ako nisu direktno povezani platnim kanalom. Lightning je, zapravo, **mreža platnih kanala**, koja omogućava slanje sredstava do udaljenog čvora kroz kanale drugih učesnika. Otkrićemo kako se uplate usmeravaju kroz mrežu, kako se likvidnost kreće između kanala i kako se obračunavaju transakcione naknade.


### Mreža kanala plaćanja


Na Lightning Network, transakcija odgovara transferu sredstava između dva čvora. Kao što je viđeno u prethodnim poglavljima, neophodno je otvoriti kanal sa nekim da bi se izvršile Lightning transakcije. Ovaj kanal omogućava skoro beskonačan broj off-chain transakcija pre nego što se zatvori kako bi se povratila On-Chain ravnoteža. Međutim, ova metoda ima nedostatak jer zahteva direktan kanal sa drugom osobom za primanje ili slanje sredstava, što podrazumeva otvaranje i zatvaranje transakcije za svaki kanal. Ako planiram da izvršim veliki broj plaćanja sa ovom osobom, otvaranje i zatvaranje kanala postaje isplativo. Suprotno tome, ako mi je potrebno da izvršim samo nekoliko Lightning transakcija, otvaranje direktnog kanala nije povoljno, jer bi me koštalo 2 On-Chain transakcije za ograničen broj off-chain transakcija. Ovaj slučaj bi se mogao desiti, na primer, kada želim da platim Lightning-om kod trgovca bez planiranja povratka.


Da bi rešio ovaj problem, Lightning Network omogućava usmeravanje plaćanja kroz nekoliko kanala i posredničkih čvorova, čime se omogućava transakcija bez direktnog kanala sa drugom osobom.


Na primer, zamislite da:



- Alice** (u narandžastom) ima kanal sa **Suzie** (u sivom) sa **100.000 satoshija** na njenoj strani i **30.000 satoshija** na Suzieinoj strani.
- Suzie** ima kanal sa **Bobom** u kojem ona poseduje **250.000 satoshija**, dok Bob nema satoshije.


![LNP201](assets/en/37.webp)


Ako Alice želi da pošalje sredstva Bobu bez otvaranja direktnog kanala sa njim, moraće da prođe kroz Suzie, i svaki kanal će morati da prilagodi likvidnost na svakoj strani. **Poslati satoshi ostaju unutar svojih odgovarajućih kanala**; oni zapravo ne "prelaze" kanale, već se transfer vrši putem prilagođavanja interne likvidnosti u svakom kanalu.


Pretpostavimo da Alisa želi da pošalje **50.000 satoshija** Bobu:



- Alice** šalje 50.000 satoshija **Suzie** u njihovom zajedničkom kanalu.
- Suzie** replicira ovaj transfer slanjem 50.000 satoshija **Bobu** u njihovom kanalu.


![LNP201](assets/en/38.webp)


Dakle, uplata se usmerava Bobu putem kretanja likvidnosti u svakom kanalu. Na kraju operacije, Alis završava sa 50,000 Sats. Ona je zaista prenela 50,000 Sats jer je na početku imala 100,000. Bob, sa svoje strane, završava sa dodatnih 50,000 Sats. Za Suzi (posrednički čvor), ova operacija je neutralna: na početku je imala 30,000 Sats u svom kanalu sa Alis i 250,000 Sats u svom kanalu sa Bobom, ukupno 280,000 Sats. Nakon operacije, ona drži 80,000 Sats u svom kanalu sa Alis i 200,000 Sats u svom kanalu sa Bobom, što je ista suma kao na početku.


Ovaj transfer je stoga ograničen **dostupnom likvidnošću** u pravcu transfera.


### Izračunavanje rute i limita likvidnosti


Hajde da uzmemo teoretski primer druge mreže sa:



- 130,000 satoshis** na Aliceinoj strani (u narandžastom) u njenom kanalu sa **Suzie** (u sivom).
- 90,000 satoshis** na **Suzienoj** strani i **200,000 satoshis** na **Karolinoj** strani (u roze boji).
- 150.000 satoshija** na **Karolinoj** strani i **100.000 satoshija** na **Bobovoj** strani.


![LNP201](assets/en/39.webp)


Maksimum koji Alisa može poslati Bobu u ovoj konfiguraciji je **90.000 satoshija**, jer je ograničena najmanjom dostupnom likvidnošću u kanalu od **Suzie do Carol**. U suprotnom smeru (od Boba do Alise), plaćanje nije moguće jer **Suziena** strana u kanalu sa **Alisom** ne sadrži satoshije. Stoga, ne postoji **nikakva ruta** koja bi se mogla koristiti za transfer u ovom smeru.

Alisa šalje **40.000 satoshija** Bobu kroz kanale:



- Alice prenosi 40.000 satoshija na svoj kanal sa Suzie.
- Suzie prenosi 40.000 satoshija Carol u njihovom zajedničkom kanalu.
- Carol konačno prenosi 40.000 satoshija Bobu.


![LNP201](assets/en/40.webp)


**Satošiji poslati** u svakom kanalu **ostaju u kanalu**, tako da satošiji koje je Karol poslala Bobu nisu isti kao oni koje je Alis poslala Suzi. Prenos se vrši samo podešavanjem likvidnosti unutar svakog kanala. Štaviše, ukupni kapacitet kanala ostaje nepromenjen.


![LNP201](assets/en/41.webp)


Kao u prethodnom primeru, nakon transakcije, izvorni čvor (Alice) ima 40.000 satoshija manje. Međuprostorni čvorovi (Suzie i Carol) zadržavaju isti ukupan iznos, čineći operaciju neutralnom za njih. Na kraju, odredišni čvor (Bob) prima dodatnih 40.000 satoshija.


Uloga posrednih čvorova je stoga veoma važna u funkcionisanju Lightning Network. Oni olakšavaju transfere nudeći više puteva za plaćanja. Da bi se ovi čvorovi podstakli da obezbede svoju likvidnost i učestvuju u usmeravanju plaćanja, plaćaju im se **naknade za usmeravanje**.


### Naknade za usmeravanje


Međupostojni čvorovi primenjuju naknade kako bi omogućili prolazak uplata kroz njihove kanale. Ove naknade postavlja **svaki čvor za svaki kanal**. Naknade se sastoje od 2 Elements:



- "**Osnovna naknada**": fiksni iznos po kanalu, često **1 sat** po defaultu, ali prilagodljiv.
- "**Varijabilna naknada**": procenat prenetog iznosa, izračunat u **delovima po milionu (ppm)**. Po defaultu, iznosi **1 ppm** (1 sat po milionu prenetih satoshija), ali se može i prilagoditi.


Naknade se takođe razlikuju u zavisnosti od smera transfera. Na primer, za transfer od Alise do Suzi, primenjuju se Alisine naknade. Suprotno tome, od Suzi do Alise, koriste se Suziine naknade.


Na primer, za kanal između Alice i Suzie, mogli bismo imati:



- Alice**: osnovna naknada od 1 sat i 1 ppm za promenljive naknade.
- Suzie**: osnovna naknada od 0.5 sat i 10 ppm za promenljive naknade.


![LNP201](assets/en/42.webp)


Da bismo bolje razumeli kako funkcionišu naknade, proučićemo isti Lightning Network kao ranije, ali sada sa sledećim naknadama za rutiranje:



- Kanal **Alice - Suzie**: osnovna naknada od 1 Satoshi i 1 ppm za Alice.
- Kanal **Suzie - Carol**: osnovna naknada od 0 Satoshi i 200 ppm za Suzie.
- Carol - Bob** Kanal: osnovna naknada od 1 Satoshi i 1 ppm za Suzie 2.

![LNP201](assets/en/43.webp)


Za istu uplatu od **40,000 satoshija** Bobu, Alis će morati poslati malo više, jer će svaki posrednički čvor odbiti svoje naknade:



- Carol** oduzima 1.04 satošija na kanalu sa Bobom:

$$ f*{\text{Carol-Bob}} = \text{osnovna naknada} + \left(\frac{\text{ppm} \times \text{iznos}}{10^6}\right) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ Sats} $$



- Suzie** odbija 8 satoshija kao naknade na kanalu sa Carol:

$$ f*{\text{Suzie-Carol}} = \text{osnovna naknada} + \left(\frac{\text{ppm} \times \text{iznos}}{10^6}\right) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$


Ukupne naknade za ovu uplatu na ovom putu su stoga **9.04 satoshija**. Dakle, Alisa mora poslati **40,009.04 satoshija** da bi Bob primio tačno **40,000 satoshija**.


![LNP201](assets/en/44.webp)


Likvidnost je stoga ažurirana:


![LNP201](assets/en/45.webp)


### Onion Routing


Da bi usmerio uplatu od pošiljaoca do primaoca, Lightning Network koristi metodu zvanu "**onion routing**". Za razliku od rutiranja klasičnih podataka, gde svaki ruter odlučuje o smeru podataka na osnovu njihove destinacije, onion routing funkcioniše drugačije:



- Čvor koji šalje izračunava celu rutu**: Na primer, Alisa određuje da njena uplata mora proći kroz Suzi i Karol pre nego što stigne do Boba.
- Svaki posrednički čvor zna samo svog neposrednog suseda**: Suzie zna samo da je primila sredstva od Alice i da ih mora preneti Carol. Međutim, Suzie ne zna da li je Alice izvorni čvor ili posrednički čvor, a takođe ne zna da li je Carol čvor primaoca ili samo još jedan posrednički čvor. Ovo pravilo važi i za Carol i sve druge čvorove na putu. Onion rutiranje tako čuva poverljivost transakcija maskiranjem identiteta pošiljaoca i krajnjeg primaoca.

Da bi se osiguralo da čvor koji prenosi može izračunati kompletnu rutu do primaoca u onion rutiranju, mora održavati **mrežni graf** kako bi znao njegovu topologiju i odredio moguće rute.

**Šta bi trebalo da izvučete iz ovog poglavlja?**



- Na Lightning mreži, plaćanja se mogu usmeravati između čvorova koji su indirektno povezani preko posredničkih kanala. Svaki od ovih posredničkih čvorova olakšava prenos likvidnosti.
- Posrednički čvorovi primaju proviziju za svoju uslugu, koja se sastoji od fiksnih i varijabilnih naknada.
- Onion routing omogućava čvoru koji prenosi podatke da izračuna kompletnu rutu bez da posrednički čvorovi znaju izvor ili konačno odredište.


U ovom poglavlju istražili smo usmeravanje plaćanja na Lightning Network. Ali postavlja se pitanje: šta sprečava posredničke čvorove da prihvate dolazno plaćanje bez prosleđivanja na sledeću destinaciju, sa ciljem presretanja transakcije? Upravo je to uloga HTLC-ova koje ćemo proučiti u narednom poglavlju.


## HTLC – Hashed Time Locked Contract


<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>


:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::


U ovom poglavlju ćemo otkriti kako Lightning omogućava plaćanjima da prolaze kroz posredničke čvorove bez potrebe za poverenjem u njih, zahvaljujući **HTLC** (_Hashed Time-Locked Contracts_). Ovi pametni ugovori osiguravaju da će svaki posrednički čvor primiti sredstva iz svog kanala samo ako prosledi uplatu krajnjem primaocu, u suprotnom, uplata neće biti validirana.


Problem koji se javlja kod usmeravanja plaćanja je stoga neophodno poverenje u posredničke čvorove, kao i među samim posredničkim čvorovima. Da bismo to ilustrovali, vratimo se našem pojednostavljenom primeru Lightning Network sa 3 čvora i 2 kanala:



- Alice ima kanal sa Suzie.
- Suzie ima kanal sa Bobom.


Alice želi da pošalje 40,000 Sats Bobu, ali nema direktan kanal sa njim i ne želi da otvori jedan. Ona traži rutu i odlučuje da ide preko Suzijinog čvora.


![LNP201](assets/en/46.webp)


Ako Alice naivno pošalje 40.000 satoshija Suzi u nadi da će Suzi preneti taj iznos Bobu, Suzi bi mogla zadržati sredstva za sebe i ne preneti ništa Bobu.


![LNP201](assets/en/47.webp)

Da bismo izbegli ovu situaciju, na Lightning mreži koristimo HTLC-ove (Hashed Time-Locked Contracts), koji čine plaćanje posredničkom čvoru uslovnim, što znači da Suzie mora ispuniti određene uslove da bi pristupila Aliceinim sredstvima i prenela ih Bobu.


### Kako HTLC-ovi Rade


An HTLC je poseban Contract zasnovan na dva principa:



- Uslov pristupa**: Primalac mora otkriti tajnu kako bi otključao uplatu koja mu pripada.
- Isticanje**: Ako uplata nije u potpunosti izvršena u definisanom periodu, ona se otkazuje, a sredstva se vraćaju pošiljaocu.


Evo kako ovaj proces funkcioniše u našem primeru sa Alisom, Suzi i Bobom:


![LNP201](assets/en/48.webp)


**Kreiranje tajne**: Bob generiše nasumičnu tajnu označenu kao _s_ (preimage), i izračunava njen Hash označen kao _r_ sa Hash funkcijom označenom kao _h_. Imamo:


$$
r = h(s)
$$


Korišćenje funkcije Hash onemogućava pronalaženje _s_ samo sa _h(s)_, ali ako je _s_ obezbeđeno, lako je verifikovati da odgovara _h(s)_.


![LNP201](assets/en/49.webp)


**Slanje zahteva za plaćanje**: Bob šalje **Invoice** Alisi tražeći uplatu. Ovaj Invoice posebno uključuje Hash _r_.


![LNP201](assets/en/50.webp)


**Slanje uslovnog plaćanja**: Alice šalje HTLC od 40.000 satoshija Suziju. Uslov da Suzie primi ova sredstva je da dostavi Alice tajnu _s'_ koja zadovoljava sledeću jednačinu:


$$
h(s') = r
$$


![LNP201](assets/en/51.webp)


**Prenos HTLC krajnjem primaocu**: Suzie, da bi dobila 40,000 satoshija od Alice, mora preneti sličan HTLC od 40,000 satoshija Bobu, koji ima isti uslov, naime da mora obezbediti Suzie tajnu _s'_ koja zadovoljava jednačinu:


$$
h(s') = r
$$


![LNP201](assets/en/52.webp)


**Validacija tajnom _s_**: Bob pruža _s_ Suziju da primi obećanih 40,000 satoshija u HTLC. Sa ovom tajnom, Suzi može otključati Alisin HTLC i dobiti 40,000 satoshija od Alise. Plaćanje je tada ispravno usmereno Bobu.


![LNP201](assets/en/53.webp)

Ovaj proces sprečava Suzie da zadrži Aliceina sredstva bez završetka prenosa Bobu, jer mora poslati uplatu Bobu kako bi dobila tajnu _s_ i tako otključala Alicein HTLC. Operacija ostaje ista čak i ako ruta uključuje nekoliko posredničkih čvorova: jednostavno je pitanje ponavljanja Suzinih koraka za svaki posrednički čvor. Svaki čvor je zaštićen uslovima HTLC-ova, jer otključavanje poslednjeg HTLC od strane primaoca automatski pokreće otključavanje svih ostalih HTLC-ova u kaskadi.


### Istek i upravljanje HTLC-ovima u slučaju problema


Ako tokom procesa plaćanja, jedan od posredničkih čvorova, ili čvor primaoca, prestane da odgovara, posebno u slučaju prekida interneta ili struje, tada se plaćanje ne može završiti, jer tajna potrebna za otključavanje HTLC-ova nije prenesena. Uzimajući naš primer sa Alisom, Suzi i Bobom, ovaj problem se javlja, na primer, ako Bob ne prenese tajnu _s_ Suzi. U tom slučaju, svi HTLC-ovi uzvodno od puta su blokirani, kao i sredstva koja oni osiguravaju.


![LNP201](assets/en/54.webp)


Da bi se to izbeglo, HTLC-ovi na Lightning-u imaju isteka koji omogućava uklanjanje HTLC ako nije završen nakon određenog vremena. Istek prati specifičan redosled jer počinje prvo sa HTLC najbližim primaocu, a zatim se progresivno pomera ka izdavaocu transakcije. U našem primeru, ako Bob nikada ne da tajnu _s_ Suzie, to bi prvo izazvalo da Suzie-in HTLC prema Bobu istekne.


![LNP201](assets/en/55.webp)


Zatim HTLC od Alice do Suzie.


![LNP201](assets/en/56.webp)


Ako bi redosled isteka bio obrnut, Alisa bi mogla da povrati svoju uplatu pre nego što Suzi može da se zaštiti od potencijalne prevare. Zaista, ako se Bob vrati da preuzme svoj HTLC dok je Alisa već uklonila svoj, Suzi bi bila u nepovoljnom položaju. Ovaj kaskadni redosled isteka HTLC stoga osigurava da nijedan posrednički čvor ne trpi nepravedne gubitke.


### Reprezentacija HTLC-ova u Commitment transakcijama


Commitment transakcije predstavljaju HTLC-ove na takav način da se uslovi koje nameću na Lightning mogu preneti na Bitcoin u slučaju prinudnog zatvaranja kanala tokom trajanja HTLC. Kao podsetnik, Commitment transakcije predstavljaju trenutno stanje kanala između dva korisnika i omogućavaju jednostrano prinudno zatvaranje u slučaju problema. Sa svakim novim stanjem kanala, kreiraju se 2 Commitment transakcije: po jedna za svaku stranu. Hajde da ponovo razmotrimo naš primer sa Alisom, Suzi i Bobom, ali da detaljnije pogledamo šta se dešava na nivou kanala između Alise i Suzi kada se kreira HTLC.

![LNP201](assets/en/57.webp)


Pre početka plaćanja od 40,000 Sats između Alise i Boba, Alisa ima 100,000 Sats u svom kanalu sa Suzi, dok Suzi drži 30,000. Njihove Commitment transakcije su sledeće:


![LNP201](assets/en/58.webp)


Alice je upravo primila Bobov Invoice, koji značajno sadrži _r_, Hash tajne. Tako može konstruisati HTLC od 40,000 satoshija sa Suzie. Ovaj HTLC je predstavljen u najnovijim Commitment transakcijama kao izlaz pod nazivom "**_HTLC Out_**" na Aliceinoj strani, jer sredstva izlaze, i "**_HTLC In_**" na Suziejinoj strani, jer sredstva ulaze.


![LNP201](assets/en/59.webp)


Ovi izlazi povezani sa HTLC dele potpuno iste uslove, naime:



- Ako Suzie može da obezbedi tajnu _s_, može odmah da otključa ovaj izlaz i prenese ga na Address koji kontroliše.
- Ako Suzie ne poseduje tajnu _s_, ona ne može otključati ovaj izlaz, a Alice će moći da ga otključa nakon vremenskog zaključavanja kako bi ga poslala na Address koji ona kontroliše. Vremensko zaključavanje tako daje Suzie period da reaguje ako dobije _s_.


Ovi uslovi se primenjuju samo ako je kanal zatvoren (tj. Commitment Transaction je objavljen On-Chain) dok je HTLC još uvek aktivan na Lightning-u, što znači da plaćanje između Alice i Boba još nije finalizovano, i HTLC-ovi još nisu istekli. Zahvaljujući ovim uslovima, Suzie može povratiti 40,000 satoshija HTLC koji joj se duguju pružanjem _s_. U suprotnom, Alice povraća sredstva nakon isteka vremenskog zaključavanja, jer ako Suzie ne zna _s_, to znači da nije prenela 40,000 satoshija Bobu, i stoga, Alice-ina sredstva joj se ne duguju.


Štaviše, ako je kanal zatvoren dok je nekoliko HTLC-ova na čekanju, biće onoliko dodatnih izlaza koliko ima tekućih HTLC-ova.

Ako kanal nije zatvoren, onda se nakon isteka ili uspeha Lightning uplate kreiraju nove Commitment transakcije kako bi odrazile novo, sada stabilno stanje kanala, to jest, bez ikakvih čekajućih HTLC-ova. Izlazi povezani sa HTLC-ovima mogu stoga biti uklonjeni iz Commitment transakcija.

![LNP201](assets/en/60.webp)


Konačno, u slučaju kooperativnog zatvaranja kanala dok je HTLC aktivan, Alisa i Suzi prestaju da prihvataju nove uplate i čekaju na rešavanje ili isteknuće tekućih HTLC-ova. Ovo im omogućava da objave lakšu završnu transakciju, bez izlaza vezanih za HTLC-ove, čime se smanjuju naknade i izbegava čekanje na mogući vremenski zaključavanje.


**Šta bi trebalo da izvučete iz ovog poglavlja?**


HTLC-ovi omogućavaju usmeravanje Lightning uplata kroz više čvorova bez potrebe za poverenjem u njih. Evo ključnih tačaka koje treba zapamtiti:



- HTLC-ovi osiguravaju bezbednost plaćanja putem tajne (preimage) i vremena isteka.
- Rešavanje ili isteknuće HTLC-ova prati specifičan redosled: zatim od odredišta ka izvoru, kako bi se zaštitio svaki čvor.
- Sve dok HTLC nije ni rešen ni istekao, održava se kao izlaz u najnovijim Commitment transakcijama.


U sledećem poglavlju, otkrićemo kako čvor koji izdaje Lightning transakciju pronalazi i bira rute kako bi njegova uplata stigla do čvora primaoca.


## Pronalaženje Puta


<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>


:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::


U prethodnim poglavljima, videli smo kako koristiti kanale drugih čvorova za usmeravanje plaćanja i dostizanje čvora bez direktnog povezivanja putem kanala. Takođe smo diskutovali o tome kako osigurati bezbednost transfera bez poverenja u posredničke čvorove. U ovom poglavlju, fokusiraćemo se na pronalaženje najbolje moguće rute za dostizanje ciljnog čvora.


### Problem rutiranja u Lightning mreži


Kao što smo videli, u Lightning-u, čvor koji šalje uplatu mora izračunati kompletnu rutu do primaoca, jer koristimo sistem onion rutiranja. Posrednički čvorovi ne znaju ni tačku porekla ni konačnu destinaciju. Oni znaju samo odakle uplata dolazi i kojem čvoru je moraju proslediti dalje. To znači da čvor koji šalje mora održavati dinamičku lokalnu topologiju mreže, sa postojećim Lightning čvorovima i kanalima između svakog, uzimajući u obzir otvaranja, zatvaranja i ažuriranja stanja.


![LNP201](assets/en/61.webp)

Čak i sa ovom topologijom Lightning Network, postoji suštinska informacija za rutiranje koja ostaje nedostupna čvoru koji šalje, a to je tačna distribucija likvidnosti u kanalima u bilo kom trenutku. Naime, svaki kanal prikazuje samo svoj **ukupni kapacitet**, ali unutrašnja distribucija sredstava je poznata samo dvema učesničkim čvorovima. Ovo predstavlja izazove za efikasno rutiranje, jer uspeh plaćanja zavisi posebno od toga da li je njegov iznos manji od najniže likvidnosti na odabranoj ruti. Međutim, likvidnosti nisu sve vidljive čvoru koji šalje.

![LNP201](assets/en/62.webp)


### Ažuriranje Mape Mreže


Da bi održali svoju mrežnu mapu ažurnom, čvorovi redovno šalju Exchange poruke kroz algoritam nazvan "**_gossip_**". Ovo je distribuirani algoritam koji se koristi za širenje informacija na epidemijski način svim čvorovima u mreži, što omogućava Exchange i sinhronizaciju Global State kanala u nekoliko komunikacionih ciklusa. Svaki čvor propagira informacije jednom ili više nasumično izabranih suseda ili ne, a oni, zauzvrat, propagiraju informacije drugim susedima i tako dalje dok se ne postigne globalno sinhronizovano stanje.


2 glavne poruke razmenjene između Lightning čvorova su sledeće:



- "**Najave kanala**": poruke koje signaliziraju otvaranje novog kanala.
- "**Ažuriranja Kanala**": ažurirajte poruke o stanju kanala, posebno o evoluciji naknada (ali ne o distribuciji likvidnosti).


Lightning čvorovi takođe prate Bitcoin Blockchain kako bi detektovali transakcije zatvaranja kanala. Zatvoreni kanal se zatim uklanja sa mape jer se više ne može koristiti za usmeravanje naših plaćanja.


### Usmeravanje Plaćanja


Hajde da uzmemo primer malog Lightning Network sa 7 čvorova: Alice, Bob, 1, 2, 3, 4 i 5. Zamislite da Alice želi da pošalje uplatu Bobu, ali mora proći kroz posredničke čvorove.


![LNP201](assets/en/63.webp)


Evo stvarna raspodela sredstava u ovim kanalima:



- Kanal između Alice i 1**: 250.000 Sats na Aliceinoj strani, 80.000 na strani 1 (ukupni kapacitet od 330.000 Sats).
- Kanal između 1 i 2**: 300.000 Sats na strani 1, 200.000 na strani 2 (ukupni kapacitet od 500.000 Sats).
- Kanal između 2 i 3**: 50,000 Sats na strani 2, 60,000 na strani 3 (ukupni kapacitet od 110,000 Sats).
- Kanal između 2 i 5**: 90.000 Sats na strani 2, 160.000 na strani 5 (ukupni kapacitet od 250.000 Sats).
- Kanal između 2 i 4**: 180.000 Sats na strani 2, 110.000 na strani 4 (ukupni kapacitet od 290.000 Sats).
- Kanal između 4 i 5**: 200.000 Sats na strani 4, 10.000 na strani 5 (ukupni kapacitet od 210.000 Sats).
- Kanal između 3 i Bob**: 50.000 Sats na strani 3, 250.000 na strani Bob (ukupni kapacitet od 300.000 Sats).
- Kanal između 5 i Bob**: 260.000 Sats na strani 5, 100.000 na strani Bob (ukupni kapacitet od 360.000 Sats).


![LNP201](assets/en/64.webp)


Da bi izvršila uplatu od 100.000 Sats od Alice do Boba, opcije rutiranja su ograničene dostupnom likvidnošću u svakom kanalu. Optimalna ruta za Alice, na osnovu poznatih distribucija likvidnosti, mogla bi biti sekvenca `Alice → 1 → 2 → 4 → 5 → Bob`:


![LNP201](assets/en/65.webp)


Ali, pošto ne zna tačnu raspodelu sredstava u svakom kanalu, mora da proceni optimalnu rutu probabilistički, uzimajući u obzir sledeće kriterijume:



- Verovatnoća uspeha**: kanal sa većim ukupnim kapacitetom verovatnije će sadržati dovoljnu likvidnost. Na primer, kanal između čvora 2 i čvora 3 ima ukupan kapacitet od 110,000 Sats, tako da je malo verovatno da će se naći 100,000 Sats ili više na strani čvora 2, iako ostaje moguće.
- Naknade za transakcije**: pri odabiru najbolje rute, čvor koji šalje takođe uzima u obzir naknade koje primenjuje svaki posrednički čvor i nastoji da minimizira ukupne troškove rutiranja.
- Isticanje HTLC-ova**: da bi se izbegla blokirana plaćanja, vreme isticanja HTLC-ova je takođe parametar koji treba uzeti u obzir.
- Broj posredničkih čvorova**: konačno, šire gledano, čvor koji šalje će nastojati da pronađe rutu sa što manje mogućih čvorova kako bi smanjio rizik od greške i ograničio naknade za Lightning transakcije.


Analizom ovih kriterijuma, čvor koji šalje može testirati najverovatnije rute i pokušati da ih optimizuje. U našem primeru, Alisa bi mogla rangirati najbolje rute na sledeći način:



- `Alice → 1 → 2 → 5 → Bob`, jer je to najkraća ruta sa najvećim kapacitetom.
- `Alice → 1 → 2 → 4 → 5 → Bob`, jer ova ruta nudi dobre kapacitete, iako je duža od prve.
- `Alice → 1 → 2 → 3 → Bob`, jer ova ruta uključuje kanal `2 → 3`, koji ima vrlo ograničen kapacitet, ali ostaje potencijalno upotrebljiv.


### Izvršenje Plaćanja


Alice odlučuje da testira svoju prvu rutu (`Alice → 1 → 2 → 5 → Bob`). Stoga šalje HTLC od 100,000 Sats ka čvoru 1. Ovaj čvor proverava da li ima dovoljno likvidnosti sa čvorom 2 i nastavlja prenos. Čvor 2 zatim prima HTLC od čvora 1, ali shvata da nema dovoljno likvidnosti u svom kanalu sa čvorom 5 da usmeri uplatu od 100,000 Sats. Tada šalje poruku o grešci nazad ka čvoru 1, koji je prenosi do Alice. Ova ruta nije uspela.


![LNP201](assets/en/66.webp)


Alice zatim pokušava da usmeri svoju uplatu koristeći svoju drugu rutu (`Alice → 1 → 2 → 4 → 5 → Bob`). Ona šalje HTLC od 100,000 Sats čvoru 1, koji ga prenosi čvoru 2, zatim čvoru 4, čvoru 5, i konačno Bobu. Ovog puta, likvidnost je dovoljna i ruta je funkcionalna. Svaki čvor otključava svoj HTLC u kaskadi koristeći preimage koji je obezbedio Bob (tajna _s_), što omogućava da Aliceina uplata Bobu bude uspešno finalizovana.


![LNP201](assets/en/67.webp)


Pretraga rute se sprovodi na sledeći način: čvor koji šalje započinje identifikovanjem najboljih mogućih ruta, zatim pokušava plaćanja sukcesivno dok se ne pronađe funkcionalna ruta.


Vredi napomenuti da Bob može obezbediti Alisi informacije u **Invoice** kako bi olakšao rutiranje. Na primer, može naznačiti obližnje kanale sa dovoljno likvidnosti ili otkriti postojanje privatnih kanala. Ove indikacije omogućavaju Alisi da izbegne rute sa malom šansom za uspeh i da prvo pokuša puteve koje preporučuje Bob.


**Šta bi trebalo da izvučete iz ovog poglavlja?**



- Čvorovi održavaju mapu topologije mreže putem najava i praćenjem zatvaranja kanala na Bitcoin Blockchain.
- Pretraga optimalne rute za plaćanje ostaje probabilistička i zavisi od mnogih kriterijuma.
- Bob može pružiti indikacije u **Invoice** kako bi usmerio Alisin put i spasio je od testiranja malo verovatnih ruta.


U narednom poglavlju, posebno ćemo proučiti funkcionisanje faktura, pored nekih drugih alata koji se koriste na Lightning Network.


# Alati Lightning Network


<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>


## Invoice, LNURL, and Keysend


<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::


U ovom poglavlju, detaljnije ćemo razmotriti rad **faktura** u Lightning mreži, odnosno zahteva za plaćanje koje čvor primalac šalje čvoru pošiljaocu. Cilj je razumeti kako izvršiti i primiti plaćanja na Lightning mreži. Takođe ćemo diskutovati o 2 alternative klasičnim fakturama: LNURL i Keysend.


![LNP201](assets/en/68.webp)


### Struktura Lightning faktura


Kao što je objašnjeno u poglavlju o HTLC-ovima, svaka uplata počinje generisanjem **Invoice** od strane primaoca. Ovaj Invoice se zatim prenosi platiocu (putem QR koda ili kopiranjem) kako bi se inicirala uplata. Invoice se sastoji od dva glavna dela:



- Deo čitljiv ljudima**: ovaj deo sadrži jasno vidljive metapodatke za poboljšanje korisničkog iskustva.
- The Payload**: ova sekcija uključuje informacije namenjene mašinama za obradu plaćanja.


Tipična struktura Invoice počinje sa identifikatorom `LN` za "Lightning", zatim `bc` za Bitcoin, pa količina Invoice. Separator `1` razdvaja deo čitljiv ljudima od dela podataka (korisni teret).


Hajde da uzmemo sledeći Invoice kao primer:


```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Već možemo da ga podelimo na 2 dela. Prvo, tu je deo čitljiv ljudima:


```invoice
lnbc100u
```


Zatim deo namenjen za teret:


```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Dva dela su odvojena sa `1`. Ovaj separator je izabran umesto specijalnog karaktera kako bi omogućio lako kopiranje celog Invoice dvostrukim klikom.


U prvom delu, možemo videti da:



- `LN` označava da je to Lightning transakcija.
- `bc` ukazuje da je Lightning Network na Bitcoin Blockchain (a ne na Testnet ili na Litecoin).
- `100u` označava količinu Invoice, izraženu u **mikrobitkoinima** (`u` znači "mikro"), što ovde iznosi 10.000 Sats.


Da biste odredili iznos plaćanja, on je izražen u podjedinicama Bitcoin. Ovde su korišćene jedinice:



- Milibitkoin (označen `m`):** Predstavlja jednu hiljaditinu Bitcoin.


$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$



- Mikrobitkoin (označen kao `u`):** Takođe ponekad nazvan "bit", predstavlja jedan milioniti deo Bitcoin.


$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$



- Nanobitcoin (označeno `n`):** Predstavlja jednu milijarditu deo Bitcoin.


$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$



- Picobitcoin (označeno `p`):** Predstavlja jednu trilionitu deo Bitcoin.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$


### Nosiivost Invoice


Nosač podataka Invoice uključuje nekoliko informacija neophodnih za obradu plaćanja:



- Timestamp:** Trenutak stvaranja Invoice, izražen u Unix Timestamp (broj sekundi koji su protekli od 1. januara 1970).
- Hashing the Secret**: Kao što smo videli u odeljku o HTLC-ovima, čvor koji prima mora obezbediti čvoru koji šalje Hash preimage-a. Ovo se koristi u HTLC-ovima za obezbeđivanje transakcije. Nazvali smo ga "_r_".
- Tajna Plaćanja**: Još jedna tajna se generiše od strane primaoca, ali se ovaj put prenosi čvoru koji šalje. Koristi se u onion rutiranju kako bi se sprečilo da međučvorovi pogode da li je sledeći čvor konačni primalac ili ne. Ovo na taj način održava oblik poverljivosti za primaoca u odnosu na poslednji međučvor na ruti.
- Javni ključ primaoca**: Ukazuje platiocu na identifikator osobe kojoj treba platiti.
- Trajanje isteka**: Maksimalno vreme za plaćanje Invoice (1 sat po podrazumevanim postavkama).
- Routing Hints**: Dodatne informacije koje pruža primalac kako bi pomogao pošiljaocu da optimizuje putanju plaćanja.
- Potpis**: Garantuje integritet Invoice autentifikacijom svih informacija.


Fakture se zatim kodiraju u **bech32**, istom formatu kao za Bitcoin SegWit adrese (format koji počinje sa `bc1`).


### LNURL Povlačenje


U tradicionalnoj transakciji, kao što je kupovina u prodavnici, Invoice se generiše za ukupan iznos koji treba platiti. Kada se Invoice predstavi (u obliku QR koda ili niza karaktera), kupac ga može skenirati i završiti transakciju. Plaćanje zatim prati tradicionalni proces koji smo proučavali u prethodnom odeljku. Međutim, ovaj proces ponekad može biti veoma nezgodan za korisničko iskustvo, jer zahteva da primalac pošalje informacije pošiljaocu putem Invoice.


Za određene situacije, kao što je povlačenje bitkoina sa online servisa, tradicionalni proces je previše složen. U takvim slučajevima, **LNURL** rešenje za povlačenje pojednostavljuje ovaj proces prikazivanjem QR koda koji primalac Wallet skenira kako bi automatski kreirao Invoice. Servis zatim plaća Invoice, a korisnik jednostavno vidi trenutno povlačenje.


![LNP201](assets/en/69.webp)


LNURL je komunikacioni protokol koji specificira skup funkcionalnosti dizajniranih da pojednostave interakcije između Lightning čvorova i klijenata, kao i aplikacija trećih strana. LNURL povlačenje, kao što smo upravo videli, je samo jedan primer među ostalim funkcionalnostima.

Ovaj protokol se zasniva na HTTP-u i omogućava kreiranje linkova za razne operacije, kao što su zahtev za plaćanje, zahtev za povlačenje ili druge funkcionalnosti koje poboljšavaju korisničko iskustvo. Svaki LNURL je bech32 kodiran URL sa lnurl prefiksom, koji, kada se skenira, pokreće niz automatskih akcija na Lightning Wallet.

Na primer, funkcija LNURL-withdraw (LUD-03) omogućava povlačenje sredstava sa usluge skeniranjem QR koda, bez potrebe za ručnim generate i Invoice. Slično, LNURL-auth (LUD-04) omogućava prijavljivanje na online usluge korišćenjem privatnog ključa na nečijem Lightning Wallet umesto lozinke.


### Slanje Lightning uplate bez Invoice: Keysend


Još jedan zanimljiv slučaj je transfer sredstava bez prethodnog primanja Invoice, poznat kao "**Keysend**". Ovaj protokol omogućava slanje sredstava dodavanjem preimage-a u šifrovane podatke o plaćanju, dostupne samo primaocu. Ovaj preimage omogućava primaocu da otključa HTLC, čime se sredstva preuzimaju bez prethodnog generisanja Invoice.


Da pojednostavimo, u ovom protokolu, pošiljalac je taj koji generiše tajnu korišćenu u HTLC-ovima, umesto primalac. Praktično, ovo omogućava pošiljaocu da izvrši uplatu bez prethodne interakcije sa primaocem.


![LNP201](assets/en/70.webp)


**Šta bi trebalo da izvučete iz ovog poglavlja?**



- **Lightning Invoice** je zahtev za plaćanje koji se sastoji od dela čitljivog za ljude i dela sa podacima za mašinu.
- Invoice je kodiran u **bech32**, sa separatorom `1` radi lakšeg kopiranja i delom podataka koji sadrži sve informacije potrebne za obradu plaćanja.
- Drugi procesi plaćanja postoje na Lightning-u, posebno **LNURL-Withdraw** za olakšavanje povlačenja, i **Keysend** za direktne transfere bez Invoice.


U narednom poglavlju, videćemo kako operater čvora može upravljati likvidnošću u svojim kanalima, da nikada ne bude blokiran i uvek može slati i primati uplate na Lightning Network.


## Upravljanje vašom likvidnošću


<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>


:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::


U ovom poglavlju ćemo istražiti strategije za efikasno upravljanje likvidnošću na Lightning Network. Upravljanje likvidnošću varira u zavisnosti od tipa korisnika i konteksta. Pogledaćemo glavne principe i postojeće tehnike kako bismo bolje razumeli kako optimizovati ovo upravljanje.


### Potrebe za likvidnošću


Postoje tri glavna korisnička profila na Lightning-u, svaki sa specifičnim potrebama za likvidnošću:



- Platilac**: Ovo je onaj koji vrši plaćanja. Potrebna im je odlazna likvidnost kako bi mogli preneti sredstva drugim korisnicima. Na primer, to može biti potrošač.
- Prodavac (ili Primaoc)**: Ovo je onaj koji prima uplate. Oni trebaju dolaznu likvidnost kako bi mogli prihvatiti uplate na svoj čvor. Na primer, to može biti preduzeće ili online prodavnica.
- The Router**: Međučvor, često specijalizovan za usmeravanje plaćanja, koji mora optimizovati svoju likvidnost u svakom kanalu kako bi usmerio što više plaćanja i zaradio naknade.


Ovi profili očigledno nisu fiksni; korisnik može prelaziti između platioca i primaoca u zavisnosti od transakcija. Na primer, Bob može primiti svoju platu preko Lightning-a od svog poslodavca, što ga stavlja u poziciju "prodavca" koji zahteva dolaznu likvidnost. Nakon toga, ako želi da iskoristi svoju platu za kupovinu hrane, postaje "platioc" i tada mora imati odlaznu likvidnost.


Da bismo bolje razumeli, uzmimo primer jednostavne mreže sastavljene od tri čvora: kupca (Alice), rutera (Suzie) i prodavca (Bob).


![LNP201](assets/en/71.webp)


Zamislite da kupac želi poslati 30.000 Sats prodavcu i da uplata ide kroz čvor rutera. Svaka strana tada mora imati minimalnu količinu likvidnosti u pravcu uplate:



- Platilac mora imati najmanje 30.000 satoshija na svojoj strani kanala sa ruterom.
- Prodavac mora imati kanal gde je 30.000 satoshija na suprotnoj strani da bi mogao da ih primi.
- Ruter mora imati 30.000 satoshija na strani platioca u njihovom kanalu, i takođe 30.000 satoshija na njihovoj strani u kanalu sa prodavcem, da bi mogao da usmeri plaćanje.


![LNP201](assets/en/72.webp)


### Strategije upravljanja likvidnošću


Platioci moraju osigurati održavanje dovoljne likvidnosti na svojoj strani kanala kako bi garantovali odlaznu likvidnost. Ovo se pokazuje kao relativno jednostavno, jer je dovoljno otvoriti nove Lightning kanale da bi se imala ova likvidnost. Naime, početna sredstva zaključana u Multisig On-Chain su u potpunosti na strani platioca u Lightning kanalu na početku. Kapacitet plaćanja je stoga osiguran sve dok su kanali otvoreni sa dovoljno sredstava. Kada je odlazna likvidnost iscrpljena, dovoljno je otvoriti nove kanale.

S druge strane, za prodavca je zadatak složeniji. Da bi mogli da primaju uplate, moraju imati likvidnost na suprotnoj strani svojih kanala. Dakle, otvaranje kanala nije dovoljno: moraju takođe izvršiti uplatu u ovom kanalu kako bi premestili likvidnost na drugu stranu pre nego što sami mogu primati uplate. Za određene profile korisnika Lightning mreže, kao što su trgovci, postoji jasna nesrazmera između onoga što njihov čvor šalje i onoga što prima, s obzirom na to da je cilj poslovanja prvenstveno da prikupi više nego što troši, kako bi ostvarilo profit. Srećom, za ove korisnike sa specifičnim potrebama za dolaznom likvidnošću, postoji nekoliko rešenja:



- Privlačenje kanala**: Trgovac ima prednost zbog obima očekivanih dolaznih uplata na njihovom čvoru. Uzimajući to u obzir, mogu pokušati privući rutirajuće čvorove koji traže prihod od naknada za transakcije i koji bi mogli otvoriti kanale prema njima, nadajući se da će usmeravati njihove uplate i prikupiti povezane naknade.



- Kretanje likvidnosti**: Prodavac takođe može otvoriti kanal i preneti deo sredstava na suprotnu stranu vršenjem fiktivnih uplata drugom čvoru, koji će novac vratiti na drugi način. U sledećem delu ćemo videti kako izvesti ovu operaciju.



- Trokutasto otvaranje**: Platforme postoje za čvorove koji žele zajednički otvarati kanale, omogućavajući svakom da ima koristi od trenutne dolazne i odlazne likvidnosti. Na primer, [LightningNetwork+](https://lightningnetwork.plus/) nudi ovu uslugu. Ako Alice, Bob i Suzie žele otvoriti kanal sa 100,000 Sats, mogu se dogovoriti na ovoj platformi da Alice otvori kanal prema Bobu, Bob prema Suzie, a Suzie prema Alice. Na ovaj način, svaki ima 100,000 Sats odlazne likvidnosti i 100,000 Sats dolazne likvidnosti, dok su zaključali samo 100,000 Sats.


![LNP201](assets/en/73.webp)



- Kupovina kanala**: Postoje usluge za iznajmljivanje Lightning kanala kako bi se dobila dolazna likvidnost, kao što su [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) ili [Lightning Labs Pool](https://lightning.engineering/pool/). Na primer, Alisa može kupiti kanal od milion satoshija prema svom čvoru kako bi mogla primati uplate.


![LNP201](assets/en/74.webp)


Konačno, za rutere, čiji je cilj da maksimiziraju broj obrađenih uplata i prikupljenih naknada, oni moraju:



- Otvorite dobro finansirane kanale sa strateškim čvorovima.
- Redovno prilagođavajte distribuciju sredstava u kanalima prema potrebama mreže.


### Loop Out Service


Usluga [Loop Out](https://lightning.engineering/loop/), koju nudi Lightning Labs, omogućava premeštanje likvidnosti na suprotnu stranu kanala dok se sredstva vraćaju na Bitcoin Blockchain. Na primer, Alisa šalje 1 milion satoshija putem Lightning-a ka loop čvoru, koji joj zatim vraća ta sredstva u On-Chain bitkoinima. Ovo balansira njen kanal sa 1 milion satoshija na svakoj strani, optimizujući njen kapacitet za primanje uplata.


![LNP201](assets/en/75.webp)


Stoga, ova usluga omogućava dolaznu likvidnost dok povraća nečije bitkoine On-Chain, što pomaže u ograničavanju imobilizacije gotovine potrebne za prihvatanje plaćanja sa Lightning-om.


**Šta treba da ponesete iz ovog poglavlja?**



- Da biste slali uplate na Lightning mreži, morate imati dovoljno likvidnosti na vašoj strani u vašim kanalima. Da biste povećali ovaj kapacitet slanja, jednostavno otvorite nove kanale.
- Da biste primali uplate, potrebno je da imate likvidnost na suprotnoj strani u vašim kanalima. Povećanje ovog kapaciteta za primanje je složenije, jer zahteva da drugi otvore kanale prema vama, ili da izvrše (fiktivne ili stvarne) uplate kako bi premestili likvidnost na drugu stranu.
- Održavanje likvidnosti na željenom nivou može biti još izazovnije u zavisnosti od korišćenja kanala. Zato postoje alati i usluge koji pomažu da se kanali balansiraju prema željama.


U sledećem poglavlju, predlažem da pregledamo najvažnije koncepte ove obuke.


# Idi dalje


<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>


## Rezime kursa



<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>


:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::


U ovom završnom poglavlju koje označava kraj obuke LNP201, predlažem da ponovo pregledamo važne koncepte koje smo zajedno obradili.


Cilj ove obuke bio je da vam pruži sveobuhvatno i tehničko razumevanje Lightning Network. Otkrili smo kako se Lightning Network oslanja na Bitcoin Blockchain za obavljanje off-chain transakcija, zadržavajući osnovne karakteristike Bitcoin, posebno odsustvo potrebe za poverenjem u druge čvorove.


### Kanali Plaćanja


U početnim poglavljima, istražili smo kako dve strane, otvaranjem platnog kanala, mogu obavljati transakcije van Bitcoin Blockchain. Evo koraka koji su obuhvaćeni:



- Otvaranje Kanala**: Kreiranje kanala se vrši putem Bitcoin transakcije koja zaključava sredstva u 2/2 multisignature Address. Ovaj depozit predstavlja Lightning kanal na Blockchain.


![LNP201](assets/en/76.webp) 2. **Transactions in the Channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new state of the channel reflected in a commitment transaction.

![LNP201](assets/en/77.webp)



- Osiguranje i Zatvaranje**: Učesnici se obavezuju na novo stanje kanala razmenom ključeva za opoziv kako bi osigurali sredstva i sprečili bilo kakvu prevaru. Oba učesnika mogu zatvoriti kanal kooperativno pravljenjem nove transakcije na Bitcoin Blockchain, ili kao poslednja opcija kroz prisilno zatvaranje. Ova poslednja opcija, iako manje efikasna jer je duža i ponekad loše procenjena u smislu naknada, i dalje omogućava povraćaj sredstava. U slučaju prevare, žrtva može kazniti prevaranta povraćajem svih sredstava iz kanala na Blockchain.


![LNP201](assets/en/78.webp)


### Mreža kanala


Nakon proučavanja izolovanih kanala, proširili smo našu analizu na mrežu kanala:



- Ruting**: Kada dve strane nisu direktno povezane kanalom, mreža omogućava rutiranje kroz posredničke čvorove. Plaćanja tada prolaze sa jednog čvora na drugi.


![LNP201](assets/en/79.webp)



- HTLCs**: Plaćanja koja prolaze kroz posredničke čvorove osigurana su "_Hash Time-Locked Contracts_" (HTLC), koji omogućavaju da sredstva budu zaključana dok se plaćanje ne završi od početka do kraja.


![LNP201](assets/en/80.webp)



- Onion Routing**: Da bi se osigurala poverljivost plaćanja, onion routing maskira krajnju destinaciju za posredničke čvorove. Čvor koji šalje mora stoga izračunati celu rutu, ali u nedostatku potpunih informacija o likvidnosti kanala, nastavlja kroz sukcesivne pokušaje da usmeri plaćanje.


![LNP201](assets/en/81.webp)


### Upravljanje Likvidnošću


Videli smo da je upravljanje likvidnošću izazov na Lightning mreži kako bi se osigurao nesmetan protok plaćanja. Slanje plaćanja je relativno jednostavno: zahteva samo otvaranje kanala. Međutim, primanje plaćanja zahteva da se ima likvidnost na suprotnoj strani nečijih kanala. Evo nekih strategija koje su diskutovane:



- Privlačenje kanala**: Podsticanjem drugih čvorova da otvore kanale prema sebi, korisnik dobija dolaznu likvidnost.



- Premještanje Likvidnosti**: Slanjem uplata na druge kanale, likvidnost se pomera na suprotnu stranu.


![LNP201](assets/en/82.webp)



- Korišćenje usluga kao što su Loop i Pool**: Ove usluge omogućavaju rebalansiranje ili kupovinu kanala sa likvidnošću na suprotnoj strani.

![LNP201](assets/en/83.webp)


- Kolaborativna Otvaranja**: Dostupne su i platforme za povezivanje radi izvođenja trostrukih otvaranja i za obezbeđivanje dolazne likvidnosti.


![LNP201](assets/en/84.webp)


# Završni deo


<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>


## Recenzije i Ocene


<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Završni ispit


<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>

## Zaključak


<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>