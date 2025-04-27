---
name: Teorijsko Uvodjenje u Lajtning Mrežu
goal: Otkrijte Lajtning Mrežu iz tehničke perspektive
objectives: 

  - Razumeti rad kanala plaćanja unutar mreže.
  - Upoznati se sa terminima HTLC, LNURL i UTXO.
  - Usvojiti znanje o upravljanju likvidnošću i naknadama LNN-a.
  - Prepoznaj Lajtning mrežu kao mrežu.
  - Razumeti teorijske upotrebe Lajtning Mreže.

---
# Putovanje do drugog nivoa Bitkojna

Istražite suštinu Lajtning mreže, esencijalnog sistema za budućnost Bitkojn transakcija. LNP201 je teorijski kurs o tehničkom funkcionisanju Lajtninga. Otkriva osnove i mehanizme ovog drugog nivoa, dizajniranog da učini Bitkojn plaćanja brzim, ekonomičnim i skalabilnim.

Zahvaljujući svojoj mreži platnih kanala, Lajtning omogućava brze i sigurne transakcije bez beleženja svake transakcije na Bitkojn blokčejnu. Kroz poglavlja ćete naučiti kako funkcioniše otvaranje, upravljanje i zatvaranje kanala plaćanja, kako se plaćanja sigurno usmeravaju kroz posredničke čvorove uz minimiziranje potrebe za poverenjem, i kako upravljati likvidnošću. Otkrićete šta su Obavezujuće transakcije, HTLC-ovi, ključevi opoziva, mehanizmi kažnjavanja, rutiranja sa višestrukim šifrovanjem (onion routing) i fakture.

Bilo da ste Bitkojn početnik ili iskusniji korisnik, ovaj kurs će pružiti vredne informacije za razumevanje i korišćenje Lajtning mreže. Iako ćemo pokriti neke osnove rada Bitkojna u prvim delovima, neophodno je da savladate osnove Satošijevog izuma pre nego što se upustite u LNP201.

Uživaj u svom otkriću!

+++
Uvod
<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>

Pregled kursa
<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>

Dobrodošli na kurs LNP201!

Ova obuka ima za cilj da vam pruži duboko tehničko razumevanje Lightning Network-a, mreže koja je dizajnirana da olakša brze i često jeftine Bitcoin transakcije. Postepeno ćete otkrivati osnovne koncepte koji upravljaju ovim sistemom, od otvaranja platnih kanala do tehnika usmeravanja i upravljanja likvidnošću.

**Deo 1: Osnovni principi**

Počećemo sa opštim uvodom u Lightning Network, postavljajući osnovne temelje o Bitcoinu, njegovim adresama, UTXO-ima i načinu na koji transakcije funkcionišu. Ova osnovna analiza je neophodna da bismo razumeli kako Lightning Network oslanja na mehanizme osnovnog blockchain-a da bi sigurno funkcionisao.

**Deo 2: Otvaranje i zatvaranje kanala**

U ovom delu ćemo istražiti proces otvaranja kanala, koji je kamen temeljac Lightning Network-a. Naučićete kako se kreiraju transakcije obaveze, ulogu ključeva za opoziv u bezbednosti i kako se kanali mogu zatvoriti ili zajednički ili jednostrano. Svaki korak će biti precizno i tehnički objašnjen kako biste razumeli sve suptilnosti.

**Deo 3: Mreža likvidnosti**

Lightning Network nije ograničen na pojedinačne kanale; to je prava mreža plaćanja. Videćemo kako se transakcije mogu usmeravati kroz posredničke čvorove koristeći HTLC-ove. Ovaj deo će vas takođe upoznati sa izazovima ulazne i izlazne likvidnosti.

**Deo 4: Alati Lightning Network-a**

Ovaj deo predstavlja praktične alate Lightning Network-a, kao što su Fakture, LNURL i Keysend. Takođe ćete naučiti kako da upravljate likvidnošću svojih kanala, što je suštinski aspekt za obezbeđivanje nesmetanih plaćanja i maksimizaciju efikasnosti vaših transakcija na Lightning-u.

**Deo 5: Dalje**

Na kraju, zaključićemo obuku ponavljanjem pokrivenih koncepata i otvaranjem puta za naprednije teme za one koji žele da prodube svoje znanje o Lightning Network-u.

Spremni da otkrijete tehničke mehanizme Lightning Network-a? Hajde da zaronimo!

# Osnove

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Razumevanje Lajtning Mreže

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![video en](https://youtu.be/QDQ8NG0l3hk)

Dobrodošli na kurs LNP201, koji ima za cilj da objasni tehničko funkcionisanje Lajtning mreže.

Lajtning mreža je mreža platnih kanala izgrađena na Bitkojn protokolu, s ciljem omogućavanja brzih transakcija sa niskim naknada. Omogućava kreiranje platnih kanala između učesnika, unutar kojih se transakcije mogu obavljati gotovo trenutno i uz minimalne naknade, bez potrebe za pojedinačnim beleženjem svake transakcije na blokčejnu. Tako, Lajtning mreža nastoji poboljšati skalabilnost Bitkojna i učiniti ga upotrebljivim za plaćanja male vrednosti.

Pre nego što istražimo aspekt "mreže", važno je razumeti koncept **kanala plaćanja** na Lajtningu, kako funkcioniše i njegove specifičnosti. Ovo je tema prvog poglavlja.

### Koncept platnog kanala

Kanal plaćanja omogućava dvema stranama, ovde **Alisa** i **Bob**, da razmene sredstva preko Lajtning mreže. Svaki protagonist ima čvor, simbolizovan krugom, a kanal između njih je predstavljen linijom.

![LNP201](assets/en/01.webp)

U našem primeru, Alisa ima 100.000 satošija na svojoj strani kanala, a Bob ima 30.000, što ukupno čini 130.000 satošija, što predstavlja **kapacitet kanala**.

**Ali šta je Satoši?**

**Satoši** (ili "sat") je obračunska jedinica na Bitkojnu. Slično kao cent za euro, Satoši je jednostavno deo Bitkojna. Jedan Satoši je jednak **0.00000001 Bitkojna**, ili jedna stotina milionitog dela Bitkojna. Korišćenje Satošija postaje sve praktičnije kako vrednost Bitkojna raste.

### Alokacija sredstava u kanalu

Hajde da se vratimo na kanal plaćanja. Ključni koncept ovde je "**strana kanala**". Svaki učesnik ima sredstva na svojoj strani kanala: Alisa 100.000 satošija i Bob 30.000. Kao što smo videli, zbir ovih sredstava predstavlja ukupni kapacitet kanala, broj koji se postavlja kada se otvori kanal.

![LNP201](assets/en/02.webp)

Hajde da uzmemo primer Lajtning transakcije. Ako Alisa želi da pošalje 40.000 satošija Bobu, to je moguće jer ima dovoljno sredstava (100.000 satošija). Nakon ove transakcije, Alisa će imati 60.000 satošija na svojoj strani, a Bob 70.000.

![LNP201](assets/en/03.webp)

**Kapacitet kanala**, na 130.000 satošija, ostaje konstantan. Ono što se menja je raspodela sredstava. Ovaj sistem ne dozvoljava slanje više sredstava nego što neko poseduje. Na primer, ako Bob želi da pošalje nazad 80.000 satošija Alisi, ne bi mogao, jer ima samo 70.000.

Još jedan način da zamislite raspodelu sredstava je da zamislite **klizač** koji pokazuje gde se sredstva nalaze u kanalu. U početku, sa 100.000 satošija za Alisu i 30.000 za Boba, klizač je logično na Alisinoj strani. Nakon transakcije od 40.000 satošija, klizač će se pomeriti blago ka Bobovoj strani, koji sada ima 70.000 satošija.

![LNP201](assets/en/04.webp)

Ova reprezentacija može biti korisna za zamišljanje bilansa sredstava u kanalu.

### Osnovna pravila platnog kanala

Prva stvar koju treba zapamtiti je da je **kapacitet kanala** fiksiran. To je donekle kao prečnik cevi: određuje maksimalnu količinu sredstava koja se mogu poslati kroz kanal odjednom.

Hajde da uzmemo primer: ako Alisa ima 130.000 satošija na svojoj strani, može poslati maksimalno 130.000 satošija Bobu u jednoj transakciji. Međutim, Bob može zatim poslati ta sredstva nazad Alisi, bilo delimično ili u celosti.

Važno je razumeti da fiksni kapacitet kanala ograničava maksimalni iznos jedne transakcije, ali ne i ukupan broj mogućih transakcija, niti ukupni obim sredstava razmenjenih unutar kanala.

**Šta bi trebalo da izvučete iz ovog poglavlja?**


- Kapacitet kanala je fiksiran i određuje maksimalnu količinu koja se može poslati u jednoj transakciji.
- Sredstva u kanalu su raspodeljena između dva učesnika, i svaki može poslati drugome samo sredstva koja poseduju na svojoj strani.
- Lajtning mreža na taj način omogućava brzu i efikasnu razmenu sredstava, uz poštovanje ograničenja nametnutih kapacitetom kanala.

Ovo je kraj prvog poglavlja, gde smo postavili temelje za Lajtning mrežu. U narednim poglavljima ćemo videti kako otvoriti kanal i dublje istražiti ovde diskutovane koncepte.

## Bitkojn, Adrese, UTXO, i Transakcije

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![video en](https://youtu.be/U9l5IVriCss)

Ovo poglavlje je pomalo posebno jer neće biti direktno posvećeno Lajtningu, već Bitkojnu. Naime, Lajtning mreža je sloj iznad Bitkojna. Stoga je neophodno razumeti određene fundamentalne koncepte Bitkojna kako bi se pravilno shvatilo funkcionisanje Lajtninga u narednim poglavljima. U ovom poglavlju ćemo pregledati osnove Bitkojn adresa za primanje, UTXO, kao i funkcionisanje Bitkojn transakcija.

### Bitkojn Adrese, Privatni Ključevi i Javni Ključevi

Bitkon adresa je niz karaktera izvedenih iz **javnog ključa**, koji se sam izračunava iz **privatnog ključa**. Kao što sigurno znate, koristi se za zaključavanje bitkojna, što je ekvivalentno primanju bitkojna u naš novčanik.

Privatni ključ je tajni element koji **nikada ne trebate deliti**, dok se javni ključ i adresa mogu deliti bez rizika po bezbednost (njihovo otkrivanje predstavlja rizik samo za vašu privatnost). Ovde je uobičajena reprezentacija koju ćemo usvojiti tokom ove obuke:


- **Privatni ključevi** će biti predstavljeni **vertikalno**.
- **Javni ključevi** će biti predstavljeni **horizontalno**.
- Njihova boja označava ko ih poseduje (Alisa u narandžastom i Bob u crnom...).

### Bitkojn Transakcije: Slanje Sredstava i Skripte

Na Bitkojnu, transakcija uključuje slanje sredstava sa jedne adrese na drugu. Uzmimo primer gde Alisa šalje 0.002 Bitkojna Bobu. Alisa koristi privatni ključ povezan sa njenom adresom da **potpiše** transakciju, čime dokazuje da zaista može da potroši ta sredstva. Ali šta se tačno dešava tokom ove transakcije? Sredstva na Bitkojn adresi su zaključana **skriptom**, vrstom mini-programa koja određuje uslove za trošenje sredstava.

Najčešće skripta zahteva potpis sa privatnim ključem povezanim sa adresom. Kada Alisa potpiše transakciju svojim privatnim ključem, ona **otključava skriptu** koja blokira sredstva, i tada se ona mogu preneti. Prenos sredstava uključuje dodavanje nove skripte ovim sredstvima, koja propisuje da će za njihovo trošenje ovog puta biti potreban potpis privatnog ključa **Boba**.

![LNP201](assets/en/05.webp)

### UTXOs: Neutrošeni Izlazi Transakcija

Na Bitkojnu, ono što mi zapravo razmenjujemo nisu direktno bitkojni, već **UTXO** (_Unspent Transaction Outputs_), što znači "nepotrošeni izlazi transakcije".

UTXO je deo bitkojna koji može imati bilo koju vrednost, na primer, **2,000 bitkojna**, **8 bitkojna**, ili čak **8,000 satsa**. Svaki UTXO je zaključan skriptom, i da bi se potrošio, mora se ispuniti uslov skripte, što je često potpis sa privatnim ključem koji je povezan sa primajućom adresom.

UTXO-ovi ne mogu biti podeljeni. Svaki put kada se koriste za trošenje iznosa u bitckojnima koji predstavljaju, to mora biti učinjeno u celosti. To je pomalo kao novčanica: ako imate novčanicu od €10 i dugujete pekaru €5, ne možete jednostavno preseći novčanicu na pola. Morate mu dati novčanicu od €10, a on će vam vratiti €5 kusura. Ovo je tačno isti princip za UTXO-em na Bitkojnu! Na primer, kada Alisa otključa skriptu svojim privatnim ključem, ona otključava ceo UTXO. Ako želi da pošalje samo deo sredstava predstavljenih ovim UTXO Bobu, može ga "fragmentirati" na nekoliko manjih. Tada će poslati 0.0015 BTC Bobu i poslati ostatak, 0.0005 BTC, na svoju **kusur adresu**.

Evo primera transakcije sa 2 izlaza:


- UTXO od 0.0015 BTC za Boba, zaključan skriptom koji zahteva potpis Bobovog privatnog ključa.
- UTXO od 0.0005 BTC za Alisu, zaključan skriptom koji zahteva njen sopstveni potpis.

![LNP201](assets/en/06.webp)

### Višepotpisne Adrese

Pored jednostavnih adresa generisanih iz jednog javnog ključa, moguće je kreirati **adrese sa više potpisa** iz više javnih ključeva. Posebno zanimljiv slučaj za Lajtning mrežu je **2/2 adresa sa više potpisa**, generisana iz dva javna ključa:

![LNP201](assets/en/07.webp)

Da biste potrošili sredstva zaključana sa ovom 2/2 više-potpisnom adresom, neophodno je potpisati sa dva privatna ključa koja su povezana sa dva javna ključa.

![LNP201](assets/en/08.webp)

Ovaj tip adresa je upravo reprezentacija na Bitkojn blokčejnu kanala plaćanja na Lajtning mreži.

**Šta treba da ponesete iz ovog poglavlja?**


- **Bitkojn adresa** je izveden iz javnog ključa, koji je sam izveden iz privatnog ključa.
- Sredstva na Bitkojnu su zaključana pomoću **skripti**, i da bi se ta sredstva potrošila, potrebno je isppuniti uslove iz skripte, što obično podrazumeva davanje potpisa sa odgovarajućim privatnim ključem.
-**UTXO-ovi ** su delovi bitkojna zaključani skriptama, i svaka transakcija na Bitkojnu se sastoji od otključavanja UTXO i zatim kreiranja jednog ili više novih zauzvrat.
- **2/2 više-potpisne adrese** zahtevaju potpis dva privatna ključa za trošenje sredstava. Ove specifične adrese se koriste u kontekstu Lajtninga za kreiranje platnih kanala.

Ovo poglavlje o Bitkojnu omogućilo nam je da pregledamo neke osnovne pojmove za ono što sledi. U sledećem poglavlju, posebno ćemo otkriti kako funkcioniše otvaranje kanala na Lajtning mreži.

# Otvaranje i zatvaranje kanala

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Otvaranje kanala

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![video en](https://youtu.be/Ty80WuN5X-g)

U ovom poglavlju ćemo preciznije videti kako otvoriti platni kanal na Lajtning mreži i razumeti vezu između ove operacije i osnovnog Bitkojn sistema.

### Lajtning kanali

Kao što smo videli u prvom poglavlju, **kanal plaćanja** na Lightning mreži može se uporediti sa "cevkom" za razmenu sredstava između dva učesnika (**Alise** i **Boba** u našim primerima). Kapacitet ovog kanala odgovara zbiru dostupnih sredstava na svakoj strani. U našem primeru, Alisa ima **100,000 satošija** a Bob ima **30,000 satošija**, što daje **ukupni kapacitet** od **130,000 satošija**.

![LNP201](assets/en/09.webp)

### Nivoi razmene informacija

Važno je jasno razlikovati različite nivoe razmene na Lajtnign mreži:


- **Komunikacija od tačke do tačke (Lajtning protokol)**: Ovo su poruke koje Lajtning čvorovi šalju jedni drugima radi komunikacije. Ove poruke ćemo predstavljati isprekidanim crnim linijama u našim dijagramima.
- **Kanali plaćanja (Lajtning protokol)**: Ovo su putevi za razmenu sredstava na Lajtning mreži, koje ćemo predstaviti punim crnim linijama.
- **Bitkojn transakcije (Bitkojn protokol)**: Ovo su transakcije izvršene na blokčejnu, koje ćemo predstaviti narandžastim linijama.

![LNP201](assets/en/10.webp)

Vredi napomenuti da Lajtning čvor može komunicirati putem P2P protokola bez otvaranja kanala, ali za razmenu sredstva, kanal je neophodan.

### Koraci za otvaranje Lajtning kanala


- **Razmena poruke**: Alisa želi da otvori kanal sa Bobom. Ona mu šalje poruku koja sadrži iznos koji želi da deponuje u kanalu (130,000 Sats) i njen javni ključ. Bob odgovara deljenjem svog javnog ključa.

![LNP201](assets/en/11.webp)


- **Kreiranje višepotpisne adrese**: Sa ova dva javna ključa, Alisa kreira **2/2 višepotpisnu adresu**, što znači da će sredstva koja će kasnije biti deponovana na ovaj adresi zahtevati oba potpisa (Alise i Boba) da bi bila potrošena.

![LNP201](assets/en/12.webp)


- **Depozitna transakcija**: Alice priprema Bitkojn transakciju za deponovanje sredstava na ovoj višepotpisnoj adresi. Na primer, može odlučiti da pošalje **130,000 satošija** na ovu višepotpisnu adresu. Ova transakcija je **kreirana, ali još nije objavljena** na blokčejnu.

![LNP201](assets/en/13.webp)


- **Transakcija povlačenja**: Pre objavljivanja transakcije depozita, Alisa kreira transakciju povlačenja kako bi mogla povratiti svoja sredstva u slučaju problema sa Bobom. Naime, kada Alisa objavi transakciju depozita, njen Sats će biti zaključan na 2/2 višepotpisnoj adresi koja zahteva i njen i Bobov potpis za otključavanje. Alisa se štiti od ovog rizika gubitka kreiranjem transakcije povlačenja koja joj omogućava da povrati svoja sredstva.

![LNP201](assets/en/14.webp)


- **Bobov potpis**: Alice šalje transakciju depozita Bobu kao dokaz i traži od njega da potpiše transakciju povlačenja. Kada dobije Bobov potpis na transakciji povlačenja, Alice je sigurna da može povratiti svoja sredstva u bilo kom trenutku, jer je sada potreban samo njen potpis da bi se otključala višepotpisna transakcija.

![LNP201](assets/en/15.webp)


- **Objavljivanje transakcije depozita**: Kada se dobije Bobov potpis, Alis može objaviti transakciju depozita na Bitkojn blokčejnu, čime se zvanično otvara Lajtning kanal između dva korisnika.

![LNP201](assets/en/16.webp)

### Kada je kanal otvoren?

Kanal se smatra otvorenim kada je transakcija depozita uključena u Bitkojn blok i dostigne određeni broj potvrda (broj sledećih blokova).

**Šta treba da zapamtite iz ovog poglavlja?**


- Otvaranje kanala počinje sa razmenom **poruka** između dve strane (razmenom iznosa i javnih ključeva).
- Kanal se formira kreiranjem **2/2 višepotpisne adrese** i deponovanjem sredstava na tu adresu putem Bitkojn transakcije.
- Osoba koja otvara kanal osigurava da može **povratiti svoja sredstva** putem transakcije povlačenja koju je potpisala druga strana pre objavljivanja transakcije depozita.

U narednom poglavlju, bavićemo se tehničkim funkcionisanjem Lajtning transakcije unutar kanala.

## Obavezujuće transakcije

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![video en](https://youtu.be/dzPMGiR_JSE)

U ovom poglavlju ćemo otkriti tehničko funkcionisanje transakcije u okviru kanala na Lajtning mreži, odnosno kada se sredstva premeštaju s jedne strane kanala na drugu.

### Podsetnik o životnom ciklusu kanala

Kao što je prethodno prikazano, Lajtning kanal počinje sa **otvaranjem** putem Bitkojn transakcije. Kanal se može **zatvoriti** u bilo kom trenutku, takođe putem Bitkojn transakcije. Između ova dva trenutka, unutar kanala se može izvršiti skoro beskonačan broj transakcija, bez prolaska kroz Bitkojn blokčejn. Hajde da vidimo šta se dešava tokom transakcije u kanalu.

![LNP201](assets/en/17.webp)

### Početno stanje kanala

U trenutku otvaranja kanala, Alisa je deponovala **130,000 satošija** na višepotpisnu adresu kanala. Dakle, u početnom stanju, sva sredstva su na Alisinoj strani. Pre otvaranja kanala, Alisa je takođe tražila od Boba da potpiše **transakciju povlačenja**, koja bi joj omogućila da povrati svoja sredstva ako želi da zatvori kanal.

![LNP201](assets/en/18.webp)

### Neobjavljene transakcije: Obavezujuće transakcije

Kada Alisa izvrši transakciju u kanalu da pošalje sredstva Bobu, kreira se nova Bitkojn transakcija kako bi se odrazila ova promena u raspodeli sredstava. Ova transakcija, nazvana **Obavezujuća transakcija**, nije objavljena na blokčejnu, ali predstavlja novo stanje kanala nakon Lightning transakcije.

Hajde da uzmemo primer gde Alisa šalje 30.000 satošija Bobu:


-**U početku**: Alice ima 130.000 satošija.
-**Nakon transakcije**: Alice ima 100.000 satošija, a Bob 30.000 satošija.

Da bi potvrdili ovaj transfer, Alisa i Bob kreiraju novu **neobjavljenu Bitkojn transakciju** koja bi poslala **100.000 satošija Alisi** i **30.000 satošija Bobu** iz višepotpisne adrese. Obe strane kreiraju ovu transakciju nezavisno, ali sa istim podacima (iznosi i adrese). Kada je kreirana, svaka strana potpisuje transakciju i razmenjuje svoj potpis sa drugom stranom. Ovo omogućava bilo kojoj strani da objavi transakciju u bilo kom trenutku ako je potrebno da povrate svoj deo kanala na glavnom Bitkojn blokčejnu.

![LNP201](assets/en/19.webp)

### Proces prenosa: Fakture

Kada Bob želi da primi sredstva, šalje Alisi **_fakturu_** na 30.000 satošija. Alisa zatim nastavlja da plati ovu fakturu pokretanjem transfera unutar kanala. Kao što smo videli, ovaj proces se oslanja na kreiranje i potpisivanje nove **Obavezujuće transakcije**.

Svaka Obavezujuća transakcija predstavlja novu raspodelu sredstava u kanalu nakon transfera. U ovom primeru, nakon transakcije, Bob ima 30,000 satošija, a Alisa ima 100,000 satošija. Ako bilo koji od ova dva učesnika odluči da objavi Obavezujuću transakciju na blokčejnu, to bi rezultiralo zatvaranjem kanala i sredstva bi bila raspodeljena prema ovoj poslednjoj raspodeli.

![LNP201](assets/en/20.webp)

### Novo stanje nakon druge transakcije

Hajde da uzmemo drugi primer: nakon prve transakcije gde je Alisa poslala 30.000 satošija Bobu, Bob odlučuje da pošalje **10.000 satošija nazad Alisi**. Ovo stvara novo stanje kanala. Nova **Obavezujuća transakcija** će predstavljati ovu ažuriranu distribuciju:


- **Alisa** sada ima **110,000 satošija**.
- **Bob** ima **20,000 satošija**.

![LNP201](assets/en/21.webp)

Ponovo, ova transakcija nije objavljena na blokčejnu, ali može biti u bilo kom trenutku u slučaju da je kanal zatvoren.

Ukratko, kada se sredstva prenose unutar Lajtning kanala:


- Alisa i Bob kreiraju novu **Obavezujuću transakciju**, koja odražava novu raspodelu sredstava.
- Ova Bitkojn transakcija je **potpisana** od strane obe strane, ali **nije objavljena** na Bitkojn blokčejnu sve dok kanal ostaje otvoren.
- Obavezujuće transakcije osiguravaju da svaki učesnik može povratiti svoja sredstva u bilo kom trenutku na Bitkojn blokčejnu objavljivanjem poslednje potpisane transakcije.

Međutim, ovaj sistem ima potencijalnu manu, koju ćemo adresirati u narednom poglavlju. Videćemo kako svaki učesnik može zaštititi sebe od pokušaja prevare od strane druge strane.

## Ključ opoziva

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

![video en](https://youtu.be/veCs39uVFUk)

U ovom poglavlju, detaljnije ćemo istražiti kako transakcije funkcionišu na Lajtning mreži tako što ćemo diskutovati o mehanizmima koji su postavljeni da se zaštite od varanja, osiguravajući da svaka strana poštuje pravila unutar kanala.

### Podsetnik: Obavezujuće Transakcije

Kao što je ranije viđeno, transakcije na Lajtning mreži se oslanjaju na neobjavljene **Obavezujuće transakcije**. Ove transakcije odražavaju trenutnu raspodelu sredstava u kanalu. Kada se izvrši nova Lajtning transakcija, kreira se nova Obavezujuća transakcija i potpisuje se od strane obe strane kako bi se odrazilo novo stanje kanala.

Hajde da uzmemo jednostavan primer:


- **Početno stanje**: Alisa ima **100.000 satošija**, Bob **30.000 satošija**.
- Nakon transakcije u kojoj Alisa šalje **40.000 satošija** Bobu, nova Obavezujuća transakcija raspoređuje sredstva na sledeći način:
  - Alisa: **60,000 satošija**
  - Bob: **70,000 satošija**

![LNP201](assets/en/22.webp)

U bilo kom trenutku, obe strane mogu objaviti potpisanu **najnoviju Obavezujuću transakciju** kako bi zatvorili kanal i povratili svoja sredstava.

### Mana: Varanje objavljivanjem stare transakcije

Potencijalni problem nastaje ako jedna od strana odluči da **prevari** objavljivanjem stare Obavezujuće transakcije. Na primer, Alisa bi mogla da objavi stariju Obavezujuću transakciju gde je imala **100.000 satošija**, iako sada u stvarnosti ima samo **60.000**. Ovo bi joj omogućilo da ukrade **40.000 satošija** od Boba.

![LNP201](assets/en/23.webp)

Još gore, Alisa bi mogla objaviti prvu transakciju povlačenja, onu pre nego što je kanal otvoren, gde je imala **130,000 satošija**, i tako ukrasti celokupna sredstva kanala.

![LNP201](assets/en/24.webp)

### Rešenje: Ključ za opoziv i vremenska zabrana trošenja

Da bi se sprečila ovakva vrsta varanja od strane Alise, na Lajtning mreži, **sigurnosni mehanizmi** su dodati obavezujućim transakcijama:


- **Vremenska zabrana trošenja**: Svaka Obavezujuća transakcija uključuje vremensku zabranu trošenja za Alisina sredstva. Vremenska zabrana trošenja je primitiv Pametnih ugovora koji postavlja vremenski uslov koji mora biti ispunjen da bi transakcija bila dodata u blok. To znači da Alisa ne može povratiti svoja sredstva dok ne prođe određeni broj blokova ako objavi jednu od Obavezujućih transakcija. Ova vremenska zabrana trošenja počinje da se primenjuje od potvrde Obavezujuće transakcije na blokčejnu. Njeno trajanje je generalno proporcionalno veličini kanala, ali se može i ručno konfigurisati.
- **Ključ za opoziv**: Sredstva Alise takođe može odmah potrošiti Bob ako poseduje **ključ za opoziv**. Ovaj ključ se sastoji od tajne koju drži Alisa i tajne koju drži Bob. Imajte na umu da je ova tajna različita za svaku Obavezujuću transakciju.

Zahvaljujući ova 2 kombinovana mehanizma, Bob ima vremena da otkrije Alisin pokušaj prevare i da je kazni povlačenjem svog izlaza pomoću ključa za opoziv, što za Boba znači povratak svih sredstava kanala. Naša nova Obavezujuća transakcija će sada izgledati ovako:

![LNP201](assets/en/25.webp)

Hajde da zajedno detaljno opišemo funkcionisanje ovog mehanizma.

### Proces ažuriranja transakcije

Kada Alisa i Bob ažuriraju stanje kanala novom Lajtning transakcijom, oni unapred razmene svoje odgovarajuće **tajne** za prethodnu Obavezujuću transakciju (onaj koja će postati zastarela i koja bi omogućila jednom od njih da vara). To znači da, u novom stanju kanala:


- Alisa i Bob imaju novu Obavezujuću transakciju koja predstavlja trenutnu raspodelu sredstava nakon Lajtning transakcije.
- Svako ima tajnu onog drugog za prethodnu transakciju, što im omogućava da koriste ključ za opoziv samo ako jedan od njih pokuša da prevari objavljivanjem u mempoolovima Bitkojn čvorova one transakcije sa starim stanjem. Zaista, da bi se kaznila druga strana, neophodno je imati obe tajne i drugu Obavezujuću transakciju, koja uključuje potpisani ulaz. Bez ove transakcije, ključ za opoziv je beskoristan. Jedini način da se dobije ova transakcija je da se preuzme iz mempoolova (u transakcijama koje čekaju potvrdu) ili u potvrđenim transakcijama na Blokčejnu tokom perioda vremenskog zaključavanja, što dokazuje da druga strana pokušava da prevari, bilo namerno ili ne.

Hajde da uzmemo primer kako bismo dobro razumeli ovaj proces:


- **Početno stanje**: Alice ima **100.000 satošija**, Bob **30.000 satošija**.

![LNP201](assets/en/26.webp)


- Bob želi da primi 40.000 satošija od Alise putem njihovog Lajtning kanala. Da bi to uradio:
   - On joj šalje fakturu zajedno sa svojom tajnom za ključ opoziva njegove prethodne Obavezujuće transakcije.
   - Kao odgovor, Alisa pruža svoj potpis za Bobovu novu Obavezujuću transakciju, kao i svoju tajnu za ključ opoziva svoje prethodne transakcije.
   - Konačno, Bob šalje svoj potpis za Alisinu novu Obavezujuću transakciju.
   - Ove razmene omogućavaju Alisi da pošalje **40.000 satošija** Bobu preko Lajtning mreže putem njihovog kanala, a nove Obavezujuće transakcije sada odražavaju ovu novu raspodelu sredstava.

![LNP201](assets/en/27.webp)


- Ako Alisa pokuša da objavi staru Obavezujuću transakciju gde je još uvek posedovala **100,000 satošija**, Bob, koji je dobio ključ za opoziv, može odmah povratiti sredstva koristeći ovaj ključ, dok je Alice blokirana vremenskim zaključavanjem.

![LNP201](assets/en/28.webp)

Čak i ako, u ovom slučaju, Bob nema ekonomski interes da pokuša da prevari, ali ako to ipak učini, Alisa takođe ima koristi od simetrične zaštite koja joj nudi iste garancije.

**Šta bi trebalo da izvučete iz ovog poglavlja?**

**Obavezujuće transakcije** na Lajtning mreži uključuju sigurnosne mehanizme koji smanjuju i rizik od varanja i podsticaje za isto. Pre nego što potpišu novu Obavezujuću transakciju, Alisa i Bob razmenjuju svoje odgovarajuće **tajne** za prethodne Obavezujuće transakcije. Ako Alisa pokuša da objavi staru Obavezujuću transakciju, Bob može koristiti **ključ za opoziv** da povrati sva sredstva pre nego što Alisa to može (jer je blokirana vremenskim zaključavanjem), što je kažnjava za pokušaj varanja.

Ovaj sigurnosni sistem osigurava da učesnici poštuju pravila Lajtning mreže, i ne mogu profitirati od objavljivanja starih Obavezujućih transakcija.

U ovom trenutku obuke, sada znate kako se otvaraju Lajtning kanali i kako funkcionišu transakcije unutar ovih kanala. U sledećem poglavlju, otkrićemo različite načine za zatvaranje kanala i povratak vaših bitcoina na osnovni nivo blokčejna.

## Zatvaranje kanala

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![video en](https://youtu.be/zmAa2fj_V7w)

U ovom poglavlju ćemo diskutovati o **zatvaranju kanala** na Lajtning mreži, što se obavlja putem Bitkojn transakcije, baš kao i otvaranje kanala. Nakon što smo videli kako funkcionišu transakcije unutar kanala, sada je vreme da vidimo kako zatvoriti kanal i povratiti sredstva na Bitkojn blokčejn.

### Podsetnik o životnom ciklusu kanala

**Životni ciklus kanala** počinje njegovim **otvaranjem**, putem Bitkojn transakcije, zatim se unutar njega obavljaju Lajtning transakcije, i na kraju, kada strane žele da povrate svoja sredstva, kanal se **zatvara** kroz drugu Bitkojn transakciju. Srednje transakcije obavljene na Lajtningu su predstavljene neobjavljenim **Obavezujućim transakcijama**.

![LNP201](assets/en/29.webp)

### Tri vrste zatvaranja kanala

Postoje tri glavna načina da se zatvori ovaj kanal, koji se mogu nazvati **dobar, grub i izostajući** (inspirisano Andreasom Antonopoulosom u _Mastering the Lightning Network_):


- **Dobro**: **kooperativno zatvaranje**, gde se i Alisa i Bob slažu da zatvore kanal.
- **Loše**: **prisilno zatvaranje**, gde jedna od strana odluči da zatvori kanal pošteno, ali bez saglasnosti druge strane.
- **Ružno**: **zatvaranje sa varanjem**, gde jedna od strana pokušava da ukrade sredstva objavljivanjem stare Obavezujuće transakcije (bilo koje osim poslednje, koja odražava stvarnu i poštenu raspodelu sredstava).

Hajde da uzmemo primer:


- Alisa poseduje **100,000 satošija** a Bob **30,000 satošija**.
- Ova distribucija se odražava u **2 Obavezujuće transakcije** (jedna po korisniku) koje nisu objavljene, ali bi mogle biti u slučaju zatvaranja kanala.

![LNP201](assets/en/30.webp)

### Dobro: kooperativno zatvaranje

U **kooperativnom zatvaranju**, Alisa i Bob se dogovaraju da zatvore kanal. Evo kako to ide:


- Alisa šalje poruku Bobu putem Lajtning komunikacionog protokola kojom predlože zatvaranje kanala.
- Bob se slaže, i dve strane ne obavljaju dalje transakcije u kanalu.

![LNP201](assets/en/31.webp)


- Alisa i Bob zajedno pregovaraju o naknadama za **završnu transakciju**. Ove naknade se obično izračunavaju na osnovu Bitkon naknada na tržištu u trenutku zatvaranja. Važno je napomenuti da **uvek osoba koja je otvorila kanal** (Alisa u našem primeru) plaća naknade za zatvaranje.
- Oni kreiraju novu **završnu transakciju**. Ova transakcija podseća na Obavezujuću transakciju, ali bez vremenskih zaključavanja ili mehanizama opoziva, jer obe strane sarađuju i nema rizika od varanja. Ova kooperativna završna transakcija je stoga različita od Obavezujuće transakcije.

Na primer, ako Alisa poseduje **100.000 satošija** a Bob **30.000 satošija**, završna transakcija će poslati **100.000 satošija** na Alisinu adresu i **30.000 satošija** na Bobovu adresu, bez vremenskih ograničenja. Kada obe strane potpišu ovu transakciju, Alisa je objavljuje. Kada transakcija bude potvrđena na Bitkojn blokčejnu, Lajtning kanal će biti zvanično zatvoren.

![LNP201](assets/en/32.webp)

**Kooperativno zatvaranje** je preferirani metod zatvaranja jer je brzo (nema vremenskog zaključavanja) i naknade za transakcije su prilagođene trenutnim Bitkojn tržišnim uslovima. Ovim se izbegava postavljanje premale naknade, što bi moglo rizikovati blokiranjem transakcije u mempool-ovima, ili nepotrebno preplaćivanje , što dovodi do nepotrebnog finansijskog gubitka za učesnike.

### Loše: prisilno zatvaranje

Kada Alisin čvor pošalje poruku Bobovom sa zahtevom za kooperativno zatvaranje, ako on ne odgovori (na primer, zbog prekida interneta ili tehničkog problema), Alisa može nastaviti sa **prisilnim zatvaranjem** objavljivanjem **poslednje potpisane Obavezujuće transakcije**.

U ovom slučaju, Alice će jednostavno objaviti poslednju Obavezujuću transakciju, koja odražava stanje kanala u trenutku kada je poslednja Lajtning transakcija obavljena sa pravilnom raspodelom sredstava.

![LNP201](assets/en/33.webp)

Ova transakcija uključuje **vremensko zaključavanje** Alisinih sredstva, što usporava zatvaranje.

![LNP201](assets/en/34.webp)

Takođe, naknade za Obavezujuću transakciju mogu biti nepogodne u trenutku zatvaranja, jer su postavljene kada je transakcija kreirana, ponekad i nekoliko meseci ranije. Generalno, Lajtning klijenti precenjuju naknade kako bi izbegli buduće probleme, ali to može dovesti do prekomernih naknada, ili obrnuto, do preniskih.

Ukratko, **prisilno zatvaranje** je opcija poslednjeg izbora kada druga strana više ne odgovara. Ono je sporije i manje ekonomično od kooperativnog zatvaranja. Stoga, treba ga izbegavati koliko god je to moguće.

### Prevara: varanje

Na kraju, zatvaranje sa **varanjem** se dešava kada jedna od strana pokuša da objavi staru Obavezujuću transakciju, često gde su držali više sredstava nego što bi trebalo. Na primer, Alisa bi mogla da objavi staru transakciju gde je posedovala **120,000 satošija**, dok zapravo sada poseduje samo **100,000**.

![LNP201](assets/en/35.webp)

Bob, da bi sprečio ovu prevaru, nadgleda Bitkojn blokčejn i njegov Mempool kako bi osigurao da Alisa ne objavi staru transakciju. Ako Bob otkrije pokušaj prevare, može koristiti **ključ za opoziv** da uzme Alisina sredstva i kazni je tako što će uzeti celokupna sredstva kanala. Pošto je Alisa blokirana vremenskim zaključavanjem na svom izlazu, Bob ima vremena da ih potroši bez vremenskog zaključavanja sa svoje strane kako bi prebacio celokupan iznos na adresu koju poseduje.

![LNP201](assets/en/36.webp)

Očigledno, varanje može potencijalno uspeti ako Bob ne deluje u okviru vremena koliko traje zaključavanje na Alisinom izlazu. U tom slučaju, Alisin izlaz se otključava, omogućavajući joj da ga iskoristi za kreiranje novog izlaza na adresi koju ona kontroliše.

**Šta bi trebalo da izvučete iz ovog poglavlja?**

Postoje tri načina za zatvaranje kanala:


- **Kooperativno zatvaranje**: Brzo i manje skupo, gde se obe strane slažu da zatvore kanal i objave prilagođenu transakciju zatvaranja.
- **Prinudno zatvaranje**: Manje poželjno, jer se oslanja na objavljivanje Obavezujuće transakcije, sa potencijalno nepovoljnim naknadama i vremenskim zaključavanjem, što usporava zatvaranje.
- **Varanje**: Ako jedna od strana pokuša da ukrade sredstva objavljivanjem stare Obavezujuće transakcije, druga strana može koristiti ključ za opoziv da kazni ovo varanje.

U narednim poglavljima, istražićemo Lajtning mrežu iz šire perspektive, fokusirajući se na to kako mreža funkcioniše.

# Mreža Likvidnosti

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lajtning mreža

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![video en](https://youtu.be/44oBdNdXtEQ)

U ovom poglavlju ćemo istražiti kako uplate na Lajtning mrežu mogu stići do primaoca čak i ako nisu direktno povezani platnim kanalom. Lajtning je, zapravo, **mreža platnih kanala**, koja omogućava slanje sredstava udaljenom čvoru kroz kanale drugih učesnika. Otkrićemo kako se uplate usmeravaju kroz mrežu, kako se likvidnost kreće između kanala i kako se obračunavaju transakcione naknade.

### Mreža kanala plaćanja

Na Lajtning mreži, transakcija odgovara transferu sredstava između dva čvora. Kao što je viđeno u prethodnim poglavljima, neophodno je otvoriti kanal sa nekim da bi se izvršile Lajtning transakcije. Ovaj kanal omogućava skoro beskonačan broj transakcija izvan baznog blokčejna pre nego što se zatvori kako bi se povratila sredstva na bazni blokčejn nivo. Međutim, ova metoda ima nedostatak jer zahteva direktan kanal sa drugom osobom za primanje ili slanje sredstava, što podrazumeva otvaranje transakcije i zatvaranje transakcije za svaki kanal. Ako planiram da izvršim veliki broj plaćanja sa ovom osobom, otvaranje i zatvaranje kanala postaje isplativo. Suprotno tome, ako mi je potrebno da izvršim samo nekoliko Lajtning transakcija, otvaranje direktnog kanala nije povoljno, jer bi me koštalo 2 bazne transakcije za ograničen broj transakcija izvan baznog blokčejna. Ovaj slučaj se može desiti, na primer, kada želim da platim Lajtningom kod trgovca bez planiranja povratka.

Da bi rešio ovaj problem, Lajtning mreža omogućava usmeravanje plaćanja kroz nekoliko kanala i posredničkih čvorova, čime se omogućava transakcija bez direktnog kanala sa drugom osobom.

Na primer, zamislite da:


- **Alisa** (u narandžastom) ima kanal sa **Suzi** (u sivom) sa **100.000 satošija** na njenoj strani i **30.000 satošija** na Suzinoj strani.
- **Suzi** ima kanal sa **Bobom** u kojem ona poseduje **250.000 satošija**, dok Bob nema nijedan satoši.

![LNP201](assets/en/37.webp)

Ako Alisa želi da pošalje sredstva Bobu bez otvaranja direktnog kanala sa njim, moraće da prođe kroz Suzi, i svaki kanal će morati da prilagodi likvidnost na svakoj strani. **Poslati satošiji ostaju unutar svojih odgovarajućih kanala**; oni zapravo ne "prelaze" kanale, već se transfer vrši putem prilagođavanja interne likvidnosti u svakom kanalu.

Pretpostavimo da Alisa želi da pošalje **50.000 satošija** Bobu:


- **Alisa** šalje 50.000 satošija **Suzi** u njihovom zajedničkom kanalu.
- **Suzi** replicira ovaj transfer slanjem 50.000 satošija **Bobu** u njihovom kanalu.

![LNP201](assets/en/38.webp)

Dakle, uplata se usmerava Bobu putem kretanja likvidnosti u svakom kanalu. Na kraju operacije, Alisa završava sa 50,000 Sats. Ona je zaista prenela 50,000 Sats jer je na početku imala 100,000. Bob, sa svoje strane, završava sa dodatnih 50,000 Sats. Za Suzi (posrednički čvor), ova operacija je neutralna: na početku je imala 30,000 Sats u svom kanalu sa Alis i 250,000 Sats u svom kanalu sa Bobom, ukupno 280,000 Sats. Nakon operacije, ona drži 80,000 Sats u svom kanalu sa Alis i 200,000 Sats u svom kanalu sa Bobom, što je isti zbir kao na početku.

Ovaj transfer je stoga ograničen **dostupnom likvidnošću** u pravcu transfera.

### Izračunavanje rute i limiti likvidnosti

Hajde da uzmemo teoretski primer druge mreže sa:


- **130,000 satošija** na Alisinoj strani (u narandžastom) u njenom kanalu sa **Suzi** (u sivom).
- **90,000 satošija** na **Suzinoj** strani i **200,000 satošija** na **Karolinoj** strani (u roze boji).
- **150,000 satošija** na strani **Karol** i **100,000 satošija** na strani **Bob**.

![LNP201](assets/en/39.webp)

Maksimum koji Alisa može poslati Bobu u ovoj konfiguraciji je **90.000 satošija**, jer je ograničena najmanjom dostupnom likvidnošću u kanalu od **Suzi do Karol**. U suprotnom smeru (od Boba do Alise), plaćanje nije moguće jer **Suzina** strana u kanalu sa **Alisom** ne sadrži satošija. Stoga, **nema rute** koja se može koristiti za transfer u ovom smeru.

Alisa šalje **40,000 satošija** Bobu kroz kanale:


- Alisa prenosi 40,000 satošija na svoj kanal sa Suzi.
- Suzi prenosi 40,000 satošija Karol u njihovom zajedničkom kanalu.
- Karol konačno prenosi 40.000 satošija Bobu.

![LNP201](assets/en/40.webp)

**Satošiji poslati** u svakom kanalu **ostaju u kanalu**, tako da satošiji koje je Karol poslala Bobu nisu isti kao oni koje je Alis poslala Suzi. Prenos se vrši samo podešavanjem likvidnosti unutar svakog kanala. Štaviše, ukupni kapacitet kanala ostaje nepromenjen.

![LNP201](assets/en/41.webp)

Kao u prethodnom primeru, nakon transakcije, izvorni čvor (Alisa) ima 40.000 satošija manje. Međuprostorni čvorovi (Suzi i Karol) zadržavaju isti ukupan iznos, što operaciju čini neutralnom za njih. Na kraju, odredišni čvor (Bob) prima dodatnih 40.000 satošija.

Uloga posrednih čvorova je stoga veoma važna u funkcionisanju Lajtning mreže. Oni olakšavaju transfere nudeći više puteva za plaćanja. Da bi se ovi čvorovi podstakli da obezbede svoju likvidnost i učestvuju u usmeravanju plaćanja, plaćaju im se **naknade za usmeravanje**.

### Naknade za usmeravanje

Posrednički čvorovi naplaćuju naknade kako bi omogućili prolazak uplata kroz njihove kanale. Ove naknade postavlja **svaki čvor za svaki kanal**. Naknade se sastoje od 2 elementa:


- "**Osnovna naknada**": fiksni iznos po kanalu, često **1 sat** po defaultu, ali je konfigurabilan.
- "**Varijabilna naknada**": procenat prenetog iznosa, izračunat u **delovima po milionu (ppm)**. Podrazumevano je **1 ppm** (1 sat po milionu prenetih satošija), ali se može i prilagoditi.

Naknade se takođe razlikuju u zavisnosti od smera transfera. Na primer, za transfer od Alise do Suzi, primenjuju se Alisine naknade. Suprotno tome, od Suzi do Alise, koriste se Suzine naknade.

Na primer, za kanal između Alise i Suzi, mogli bismo imati:


- **Alisa**: osnovna naknada od 1 sat i 1 ppm za promenljive naknade.
- **Suzi**: osnovna naknada od 0.5 sat i 10 ppm za promenljive naknade.

![LNP201](assets/en/42.webp)

Da bismo bolje razumeli kako funkcionišu naknade, proučićemo istu Lajtning mrežu kao i ranije, ali sada sa sledećim naknadama za rutiranje:


- Kanal **Alisa - Suzi**: osnovna naknada od 1 Satošija i 1 ppm za Alisu.
- Kanal **Suzi - Karol**: osnovna naknada od 0 Satošija i 200 ppm za Suzi.
- Kanal **Karol - Bob** : osnovna naknada od 1 Satošija i 1 ppm za Suzi 2.

![LNP201](assets/en/43.webp)

Za istu uplatu od **40,000 Satošija** Bobu, Alisa će morati poslati malo više, jer će svaki posrednički čvor odbiti svoje naknade:


- **Karol** oduzima 1.04 Satošija na kanalu sa Bobom:

$$ f*{\text{Carol-Bob}} = \text{osnovna naknada} + \left(\frac{\text{ppm} \times \text{iznos}}{10^6}\right) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ Sats} $$


- **Suzi** odbija 8 Satošija kao naknade na kanalu sa Carol:

$$ f*{\text{Suzie-Carol}} = \text{osnovna naknada} + \left(\frac{\text{ppm} \times \text{iznos}}{10^6}\right) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$

Ukupne naknade za ovu uplatu na ovom putu su stoga **9.04 Satošija**. Dakle, Alisa mora poslati **40,009.04 Satošija** da bi Bob primio tačno **40,000 Satošija**.

![LNP201](assets/en/44.webp)

Likvidnost se stoga ažurira:

![LNP201](assets/en/45.webp)

### Onion Routing (usmeravanje)

Da bi usmerio uplatu od pošiljaoca do primaoca, Lajtning koristi metodu zvanu "**onion routing (usmeravanje)**". Za razliku od rutiranja klasičnih podataka, gde svaki ruter odlučuje o smeru podataka na osnovu njihove destinacije, onion usmeravanje funkcioniše drugačije:


- **Čvor koji šalje izračunava celu rutu**: Na primer, Alisa određuje da njena uplata mora proći kroz Suzi i Karol pre nego što stigne do Boba.
- **Svaki posrednički čvor zna samo svog neposrednog suseda**: Suzi zna samo da je primila sredstva od Alise i da ih mora preneti Karol. Međutim, Suzi ne zna da li je Alisa izvorni čvor ili posrednički čvor, i takođe ne zna da li je Karol čvor primaoca ili samo još jedan posrednički čvor. Ovo pravilo se takođe primenjuje na Karol i sve druge čvorove na putu. Onion usmeravanje tako čuva poverljivost transakcija maskiranjem identiteta pošiljaoca i krajnjeg primaoca.

Da bi se osiguralo da čvor koji prenosi može izračunati kompletnu rutu do primaoca u onion rutiranju, mora održavati **mrežni graf (grafikon veza izmedju čvorova)** kako bi znao svoju topologiju i odredio moguće rute.

**Šta treba da ponesete iz ovog poglavlja?**


- Na Lightning mreži, plaćanja se mogu usmeravati između čvorova koji su indirektno povezani preko posredničkih kanala. Svaki od ovih posredničkih čvorova olakšava prenos likvidnosti.
- Posrednički čvorovi primaju proviziju za svoju uslugu, koja se sastoji od fiksnih i varijabilnih naknada.
- Onion usmeravanje omogućava čvoru koji prenosi podatke da izračuna kompletnu rutu bez da posrednički čvorovi znaju izvor ili konačno odredište.

U ovom poglavlju smo istražili usmeravanje plaćanja na Lajtning mreži. Ali postavlja se pitanje: šta sprečava posredničke čvorove da prihvate dolazno plaćanje bez prosleđivanja na sledeću destinaciju, sa ciljem presretanja transakcije? Upravo je to uloga HTLC-ova koje ćemo proučiti u narednom poglavlju.

## HTLC – Hashed Time Locked Contract (hešovan vremenski zaključan ugovor)

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![video en](https://youtu.be/jI4nM297aHA)

U ovom poglavlju ćemo otkriti kako Lajtning omogućava plaćanja da prolaze kroz posredničke čvorove bez potrebe za poverenjem u njih, zahvaljujući **HTLC** (_Hashed Time-Locked Contracts_). Ovi pametni ugovori osiguravaju da će svaki posrednički čvor primiti sredstva iz svog kanala samo ako prosledi uplatu krajnjem primaocu, u suprotnom, uplata neće biti validirana.

Problem koji se javlja kod usmeravanja plaćanja je neophodno poverenje u posredničke čvorove, kao i među samim posredničkim čvorovima. Da bismo to ilustrovali, hajde da ponovo razmotrimo naš pojednostavljeni primer Lajtning mreže sa 3 čvora i 2 kanala:


- Alisa ima kanal sa Suzi.
- Suzi ima kanal sa Bobom.

Alisa želi da pošalje 40,000 Sats Bobu, ali nema direktan kanal sa njim i ne želi da otvori jedan. Ona traži rutu i odlučuje da ide preko Suzijinog čvora.

![LNP201](assets/en/46.webp)

Ako Alisa naivno pošalje 40.000 satošja Suzi u nadi da će Suzi preneti taj iznos Bobu, Suzi bi mogla zadržati sredstva za sebe i ne preneti ništa Bobu.

![LNP201](assets/en/47.webp)

Da bismo izbegli ovu situaciju, na Lajtning mreži koristimo HTLC-ove (Hashed Time-Locked Contracts), koji čine plaćanje posredničkom čvoru uslovnim, što znači da Suzi mora ispuniti određene uslove da bi pristupila Alisinim sredstvima i prenela ih Bobu.

### Kako HTLC-ovi Rade

HTLC je poseban ugovor zasnovan na dva principa:


- **Uslov pristupa**: Primalac mora otkriti tajnu kako bi otključao uplatu koja mu pripada.
- **Isticanje**: Ako uplata nije u potpunosti izvršena u definisanom periodu, ona se otkazuje, a sredstva se vraćaju pošiljaocu.

Evo kako ovaj proces funkcioniše u našem primeru sa Alisom, Suzi i Bobom:

![LNP201](assets/en/48.webp)

**Kreiranje tajne**: Bob generiše nasumičnu tajnu označenu kao _s_ (preimage), i izračunava njen Heš označen kao _r_ sa Heš funkcijom označenom kao _h_. Imamo:

$$
r = h(s)
$$

Korišćenje heš funkcije onemogućava pronalaženje _s_ samo sa _h(s)_, ali ako je _s_ obezbeđeno, lako je proveriti da li odgovara _h(s)_.

![LNP201](assets/en/49.webp)

**Slanje zahteva za plaćanjem**: Bob šalje **fakturu** Alisi tražeći uplatu. Ova faktura posebno uključuje Hash _r_.

![LNP201](assets/en/50.webp)

**Slanje uslovnog plaćanja**: Alice šalje HTLC od 40,000 satošija Suzi. Uslov da Suzi primi ova sredstva je da dostavi Alisi tajnu _s'_ koja zadovoljava sledeću jednačinu:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Prenos HTLC krajnjem primaocu**: Suzi, da bi dobila 40,000 satošija od Alise, mora preneti sličan HTLC od 40,000 satošija Bobu, koji ima isti uslov, naime da mora obezbediti Suzi tajnu _s'_ koja zadovoljava jednačinu:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Validacija tajnom _s_**: Bob pruža _s_ Suzi da bi primio obećanih 40,000 satošija u HTLC. Sa ovom tajnom, Suzi može otključati Alisin HTLC i dobiti 40,000 satošija od Alise. Plaćanje je tada ispravno usmereno Bobu.

![LNP201](assets/en/53.webp)

Ovaj proces sprečava Suzi da zadrži Alisina sredstva bez završetka prenosa Bobu, jer mora poslati uplatu Bobu kako bi dobila tajnu _s_ i tako otključala Alisin HTLC. Operacija ostaje ista čak i ako ruta uključuje nekoliko posredničkih čvorova: to je jednostavno ponavljanja Suzinih koraka za svaki posrednički čvor. Svaki čvor je zaštićen uslovima HTLC-ova, jer otključavanje poslednjeg HTLC-a od strane primaoca automatski pokreće otključavanje svih ostalih HTLC-ova u kaskadi.

### Isticanje i upravljanje HTLC-ovima u slučaju problema

Ako tokom procesa plaćanja, jedan od posredničkih čvorova, ili čvor primaoca, prestane da odgovara, posebno u slučaju prekida interneta ili struje, tada se plaćanje ne može završiti, jer tajna potrebna za otključavanje HTLC-ova nije preneta. Uzimajući naš primer sa Alisom, Suzi i Bobom, ovaj problem se javlja, na primer, ako Bob ne prenese tajnu _s_ Suzi. U tom slučaju, svi HTLC-ovi uzvodno od puta su blokirani, kao i sredstva koja oni obezbeđuju.

![LNP201](assets/en/54.webp)

Da bi se to izbeglo, HTLC-ovi na Lajtninu imaju vremenski rok koji omogućava uklanjanje HTLC ako nije završen nakon određenog vremena. Istek sledi specifičan redosled jer počinje prvo sa HTLC najbližim primaocu, a zatim se progresivno pomera ka izdavaocu transakcije. U našem primeru, ako Bob nikada ne da tajnu _s_ Suzi, to bi prvo izazvalo da Suzin HTLC prema Bobu istekne.

![LNP201](assets/en/55.webp)

Zatim HTLC od Alice do Suzi.

![LNP201](assets/en/56.webp)

Ako bi redosled isteka bio obrnut, Alisa bi mogla da povrati svoju uplatu pre nego što Suzi može da se zaštiti od potencijalne prevare. Zaista, ako se Bob vrati da preuzme svoj HTLC dok je Alisa već uklonila svoj, Suzi bi bila u nepovoljnom položaju. Ovaj kaskadni redosled isteka HTLC stoga osigurava da nijedan posrednički čvor ne trpi nepravedne gubitke.

### Reprezentacija HTLC-ova u Obavezujućim transakcijama

Obavezujuće transakcije predstavljaju HTLC-ove na takav način da se uslovi koje nameću na Lajtningu mogu preneti na Bitcoin u slučaju prinudnog zatvaranja kanala tokom trajanja HTLC. Kao podsetnik, Obavezujuće transakcije predstavljaju trenutno stanje kanala između dva korisnika i omogućavaju jednostrano prinudno zatvaranje u slučaju problema. Sa svakim novim stanjem kanala, kreiraju se dve Obavezujuće transakcije: po jedna za svaku stranu. Hajde da ponovo razmotrimo naš primer sa Alisom, Suzi i Bobom, ali da detaljnije pogledamo šta se dešava na nivou kanala između Alise i Suzi kada se kreira HTLC.

![LNP201](assets/en/57.webp)

Pre početka plaćanja od 40,000 Sats između Alise i Boba, Alisa ima 100,000 Sats u svom kanalu sa Suzi, dok Suzi drži 30,000. Njihove Obavezujuće transakcije su sledeće:

![LNP201](assets/en/58.webp)

Alisa je upravo primila Bobovu fakturu, koja sadrži _r_, heš tajne. Tako može konstruisati HTLC od 40,000 satošija sa Suzi. Ovaj HTLC je predstavljen u najnovijim Obavezujućim transakcijama kao izlaz pod nazivom "**_HTLC Out_**" na Alisinoj strani, jer sredstva izlaze, i "**_HTLC In_**" na Suzinog strani, jer sredstva ulaze.

![LNP201](assets/en/59.webp)

Ovi rezultati povezani sa HTLC dele potpuno iste uslove, naime:


- Ako Suzi može da obezbedi tajnu _s_, može odmah da otključa ovaj izlaz i prenese ga na adresu koju kontroliše.
- Ako Suzi ne poseduje tajnu _s_, neće moći da otključa ovaj izlaz, a Alisa će moći da ga otključa nakon vremenskog zaključavanja kako bi ga poslala na adresu koju ona kontroliše. Vremensko zaključavanje tako daje Suzi period da reaguje ako dobije _s_.

Ovi uslovi važe samo ako je kanal zatvoren (tj. Obavezujuća transakcija je objavljena na baznom blockčejnu) dok je HTLC još uvek aktivan na Lajtningu, što znači da plaćanje između Alise i Boba još nije finalizovano, i HTLC-ovi još nisu istekli. Zahvaljujući ovim uslovima, Suzi može povratiti 40,000 satošija od HTLC koji joj duguju pružanjem _s_. U suprotnom, Alisa povraća sredstva nakon isteka vremenskog zaključavanja, jer ako Suzi ne zna _s_, to znači da nije prenela 40,000 satošija Bobu, i stoga, Alisina sredstva joj nisu dugovana.

Štaviše, ako je kanal zatvoren dok je nekoliko HTLC-ova na čekanju, biće onoliko dodatnih izlaza koliko ima tekućih HTLC-ova.

Ako kanal nije zatvoren, nakon isteka ili uspeha Lajtning uplate, kreiraju se nove Obavezujuće transakcije kako bi odrazile novo, sada stabilno stanje kanala, to jest, bez ikakvih čekajućih HTLC-ova. Izlazi povezani sa HTLC-ovima stoga mogu biti uklonjeni iz Obavezujućih transakcija.

![LNP201](assets/en/60.webp)

Konačno, u slučaju kooperativnog zatvaranja kanala dok je HTLC aktivan, Alisa i Suzi prestaju prihvatati nove uplate i čekaju na rešavanje ili okončanje tekućih HTLC-ova. Ovo im omogućava da objave lakšu završnu transakciju, bez izlaza vezanih za HTLC-ove, čime se smanjuju naknade i izbegava čekanje na moguće vremenske zaključavanje.

**Šta bi trebalo da izvučete iz ovog poglavlja?**

HTLC-ovi omogućavaju usmeravanje Lajtning plaćanja kroz više čvorova bez potrebe za poverenjem u njih. Evo ključnih tačaka koje treba zapamtiti:


- HTLC-ovi osiguravaju bezbednost plaćanja putem tajne (ulazna vrednsot heš funkcije) i vremena isteka.
- Rešavanje ili istek HTLC-ova prati specifičan redosled: od odredišta ka izvoru, kako bi se zaštitio svaki čvor.
- Sve dok HTLC nije ni rešen ni istekao, predstavljen je kao izlaz u najnovijim Obavezujućim transakcijama

U narednom poglavlju, otkrićemo kako čvor koji kreira Lajtning transakciju pronalazi i bira rute kako bi njegova uplata stigla do čvora primaoca.

## Pronalaženje Vašeg Puta

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![video en](https://youtu.be/CqetCElRjUQ)

U prethodnim poglavljima, videli smo kako koristiti kanale drugih čvorova za usmeravanje plaćanja i dostizanje čvora bez direktnog povezivanja putem kanala. Takođe smo diskutovali o tome kako osigurati bezbednost transfera bez poverenja u posredničke čvorove. U ovom poglavlju, fokusiraćemo se na pronalaženje najbolje moguće rute za dostizanje odredišnog čvora.

### Problem rutiranja u Lajtning mreži

Kao što smo videli, u Lajtningu, čvor koji šalje uplatu mora izračunati kompletnu rutu do primaoca, jer koristimo sistem onion rutiranja. Posrednički čvorovi ne znaju ni tačku porekla ni krajnje odredište. Oni znaju samo odakle uplata dolazi i kojem čvoru je moraju dalje preneti. To znači da čvor koji šalje mora održavati dinamičku lokalnu topologiju mreže, sa postojećim Lajtning čvorovima i kanalima između svakog, uzimajući u obzir otvaranja, zatvaranja i ažuriranja stanja.

![LNP201](assets/en/61.webp)

Čak i sa ovom topologijom Lajtning mreže, postoji suštinska informacija za rutiranje koja ostaje nedostupna čvoru koji šalje, a to je tačna distribucija likvidnosti u kanalima u bilo kom trenutku. Naime, svaki kanal prikazuje samo svoj **ukupni kapacitet**, ali unutrašnja distribucija sredstava je poznata samo dvema učesničkim čvorovima. Ovo predstavlja izazove za efikasno rutiranje, jer uspeh plaćanja zavisi posebno od toga da li je njegov iznos manji od najniže likvidnosti na odabranoj ruti. Međutim, sve likvidnosti nisu vidljive čvoru koji šalje.

![LNP201](assets/en/62.webp)

### Ažuriranje Mrežne mape

Da bi održali svoju mrežnu mapu ažurnom, čvorovi redovno razmenjuju poruke putem algoritma nazvanog "**_gossip_ (ogovaranje)**". Ovo je distribuirani algoritam koji se koristi za širenje informacija na epidemijski način do svih čvorova u mreži, što omogućava razmenu i sinhronizaciju globalnog stanja kanala u nekoliko komunikacionih ciklusa. Svaki čvor propagira informacije jednom ili više povezanih čvorova izabranih nasumično ili ne, a oni, zauzvrat, propagiraju informacije drugim susedima i tako dalje dok se ne postigne globalno sinhronizovano stanje.

Dve glavne poruke razmenjene između Lajtning čvorova su sledeće:


- "**Najave Kanala**": poruke koje signaliziraju otvaranje novog kanala.
- "**Ažuriranja kanala**": poruke o novom stanju kanala, posebno o evoluciji naknada (ali ne o distribuciji likvidnosti).

Lajtning čvorovi takođe prate Bitkojn blokčejn kako bi detektovali transakcije zatvaranja kanala. Zatvoreni kanal se zatim uklanja sa mape jer se više ne može koristiti za usmeravanje plaćanja.

### Usmeravanje Plaćanja

Hajde da uzmemo primer male Lajtning mreže sa 7 čvorova: Alisa, Bob, 1, 2, 3, 4 i 5. Zamislite da Alisa želi da pošalje uplatu Bobu, ali mora proći kroz posredničke čvorove.

![LNP201](assets/en/63.webp)

Evo stvarne raspodele sredstava u ovim kanalima:


- **Kanal između Alice i 1**: 250,000 Sats na Alisinog strani, 80,000 na strani 1 (ukupni kapacitet od 330,000 Sats).
- **Kanal između 1 i 2**: 300.000 Sats na strani 1, 200.000 na strani 2 (ukupni kapacitet od 500.000 Sats).
- **Kanal između 2 i 3**: 50,000 Sats na strani 2, 60,000 na strani 3 (ukupni kapacitet od 110,000 Sats).
- **Kanal između 2 i 5**: 90.000 Sats na strani 2, 160.000 na strani 5 (ukupni kapacitet od 250.000 Sats).
- **Kanal između 2 i 4**: 180,000 Sats na strani 2, 110,000 na strani 4 (ukupni kapacitet od 290,000 Sats).
- **Kanal između 4 i 5**: 200.000 Sats na strani 4, 10.000 na strani 5 (ukupni kapacitet od 210.000 Sats).
- **Kanal između 3 i Bob**: 50,000 Sats na strani 3, 250,000 na strani Bob (ukupni kapacitet od 300,000 Sats).
- **Kanal između 5 i Bob**: 260.000 Sats na strani 5, 100.000 na strani Bob (ukupni kapacitet od 360.000 Sats).

![LNP201](assets/en/64.webp)

Kako bi se izvršila uplata od 100,000 Sats od Alise do Boba, opcije rutiranja su ograničene dostupnom likvidnošću u svakom kanalu. Optimalna ruta za Alisu, na osnovu poznatih distribucija likvidnosti, mogla bi biti sekvenca `Alisa → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Ali pošto Alisa ne zna tačnu raspodelu sredstava u svakom kanalu, ona mora da proceni optimalnu rutu probabilistički, uzimajući u obzir sledeće kriterijume:


- **Verovatnoća uspeha**: kanal sa većim ukupnim kapacitetom verovatnije će sadržati dovoljnu likvidnost. Na primer, kanal između čvora 2 i čvora 3 ima ukupan kapacitet od 110,000 Sats, tako da je malo verovatno da će se naći 100,000 Sats ili više na strani čvora 2, iako ostaje moguće.
- **Naknade za transakcije**: pri odabiru najbolje rute, čvor koji šalje takođe uzima u obzir naknade koje primenjuje svaki posrednički čvor i nastoji da minimizira ukupne troškove rutiranja.
- **Isticanje HTLC-ova**: da bi se izbegle blokirane uplate, vreme isticanja HTLC-ova je takođe parametar koji treba uzeti u obzir.
- **Broj posredničkih čvorova**: konačno, šire gledano, čvor koji šalje će nastojati da pronađe rutu sa što manje mogućih čvorova kako bi smanjio rizik od neuspeha i ograničio naknade za Lajtning transakciju.

Analizirajući ove kriterijume, čvor koji šalje može testirati najverovatnije rute i pokušati da ih optimizuje. U našem primeru, Alisa bi mogla rangirati najbolje rute na sledeći način:


- `Alice → 1 → 2 → 5 → Bob`, jer je to najkraća ruta sa najvećim kapacitetom.
- `Alice → 1 → 2 → 4 → 5 → Bob`, jer ova ruta nudi dobre kapacitete, iako je duža od prve.
- `Alice → 1 → 2 → 3 → Bob`, jer ova ruta uključuje kanal `2 → 3`, koji ima vrlo ograničen kapacitet, ali ostaje potencijalno upotrebljiv.

### Izvršenje Plaćanja

Alisa odlučuje da testira svoju prvu rutu (`Alice → 1 → 2 → 5 → Bob`). Stoga šalje HTLC od 100,000 Sats ka čvoru 1. Ovaj čvor proverava da li ima dovoljno likvidnosti sa čvorom 2 i nastavlja prenos. Čvor 2 zatim prima HTLC od čvora 1, ali shvata da nema dovoljno likvidnosti u svom kanalu sa čvorom 5 da usmeri uplatu od 100,000 Sats. Zatim šalje poruku o grešci nazad čvoru 1, koji je prenosi Alisi. Ova ruta nije uspela.

![LNP201](assets/en/66.webp)

Alisa zatim pokušava da usmeri svoju uplatu koristeći svoju drugu rutu (`Alice → 1 → 2 → 4 → 5 → Bob`). Ona šalje HTLC od 100,000 Sats čvoru 1, koji ga prenosi čvoru 2, zatim čvoru 4, čvoru 5, i konačno Bobu. Ovog puta, likvidnost je dovoljna i ruta je funkcionalna. Svaki čvor otključava svoj HTLC u kaskadi koristeći preimage koji je obezbedio Bob (tajna _s_), što omogućava da Alisina uplata Bobu bude uspešno finalizovana.

![LNP201](assets/en/67.webp)

Pretraga za rutom se sprovodi na sledeći način: čvor koji šalje započinje identifikovanjem najboljih mogućih ruta, zatim pokušava plaćanja sukcesivno dok se ne pronađe funkcionalna ruta.

Vredi napomenuti da Bob može obezbediti Alisi informacije u **fakturi** kako bi olakšao rutiranje. Na primer, može naznačiti obližnje kanale sa dovoljnom likvidnošću ili otkriti postojanje privatnih kanala. Ove indikacije omogućavaju Alisi da izbegne rute sa malom šansom za uspeh i da prvo pokuša puteve koje preporučuje Bob.

**Šta bi trebalo da izvučete iz ovog poglavlja?**


- Čvorovi održavaju mapu topologije mreže putem najava i praćenjem zatvaranja kanala na Bitkojn blokčejnu.
- Pretraga optimalne rute za plaćanje ostaje probabilistička i zavisi od mnogih kriterijuma.
- Bob može pružiti indikacije u **fakturi** kako bi usmerio Alice i spasio je od testiranja slabo mogućih ruta.

U narednom poglavlju, posebno ćemo proučiti funkcionisanje faktura, pored nekih drugih alata koji se koriste na Lajtning mreži.

# Alati Lajtning mreže

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Faktura, LNURL, and Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![video en](https://youtu.be/XANzf1Qqp9I)

U ovom poglavlju ćemo detaljnije razmotriti rad **faktura** u Lajtning mreži, odnosno zahteva za plaćanje koje čvor primalac šalje čvoru pošiljaocu. Cilj je razumeti kako izvršiti i primiti plaćanja na Lajtning mreži. Takođe ćemo diskutovati o dve alternative klasičnim fakturama: LNURL i Keysend.

![LNP201](assets/en/68.webp)

### Struktura Lajtning faktura

Kao što je objašnjeno u poglavlju o HTLC-ovima, svaka uplata počinje generisanjem **fakture** od strane primaoca. Ova faktura se zatim prenosi platiocu (putem QR koda ili kopiranjem) kako bi se inicirala uplata. Faktura se sastoji od dva glavna dela:


- **Deo razumljiv ljudima**: ovaj deo sadrži jasno vidljive metapodatke za poboljšanje korisničkog iskustva.
- **Payload (sadržaj)**: ova sekcija uključuje informacije namenjene mašinama za obradu plaćanja.

Tipična struktura fakture počinje sa identifikatorom `LN` za "Lightning", zatim `bc` za Bitcoin, pa iznos fakture. Separator `1` razdvaja deo čitljiv ljudima od dela podataka (payload).

Hajde da uzmemo sledeću fakturur kao primer:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Već možemo da ga podelimo na dva dela. Prvo, tu je deo čitljiv ljudima:

```invoice
lnbc100u
```

Zatim deo namenjen za kompjuter:

```invoice
p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Dva dela su odvojena sa `1`. Ovaj separator je izabran umesto specijalnog karaktera kako bi se omogućilo lako kopiranje cele fakture dvostrukim klikom.

U prvom delu, možemo videti da:


- `LN` označava da je to Lightning transakcija.
- `bc` ukazuje da je Lajtning mreža na Bitkojn blokčejnu (a ne na Testnet-u ili na Litecoin-u).
- `100u` označava iznos faktrue, izraženu u **mikrobitkoinima** (`u` znači "mikro"), što ovde iznosi 10.000 Sats.

Da biste odredili iznos plaćanja, on se izražava u podjedinicama Bitkojna. Ovde su korišćene jedinice:


- **Milibitkoin (označen `m`):** Predstavlja hiljaditi deo jednog Bitkojna.

$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$


- **Mikrobitkoin (označen kao `u`):** Takođe ponekad nazvan "bit", predstavlja milioniti deo Bitkojna.

$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$


- **Nanobitcoin (označeno `n`):** Predstavlja milijariditi deo Bitkojna.

$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$


- **Picobitcoin (označeno `p`):** Predstavlja trilioniti deo Bitkojna.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$

### Sadržaj Fakture

Sadržaj fakture uključuje nekoliko informacija neophodnih za obradu plaćanja:


- **Vremenska oznaka:** Trenutak kreiranja fakture, izražen u Unix Timestamp (broj sekundi koji su protekli od 1. januara 1970).
- **Heširanje tajne**: Kao što smo videli u delu o HTLC-ovima, čvor koji prima mora obezbediti čvoru koji šalje vrednost heša ulazne vrednosti tajne. Ovo se koristi u HTLC-ovima za obezbeđivanje transakcije. Nazvali smo ga "_r_".
- **Tajna Plaćanja**: Još jedna tajna se generiše od strane primaoca, ali se ovaj put prenosi čvoru koji šalje. Koristi se u onion rutiranju kako bi se sprečilo da međučvorovi pogode da li je sledeći čvor konačni primalac ili ne. Ovo na taj način obezbeđuje oblik poverljivosti za primaoca prema poslednjem međučvoru na ruti.
- **Javni ključ primaoca**: Ukazuje platiocu na identifikator osobe kojoj treba platiti.
- **Trajanje isteka**: Maksimalno vreme za plaćanje fakture (1 sat po defaultu).
- **Routing Hints**: Dodatne informacije koje pruža primalac kako bi pomogao pošiljaocu da optimizuje putanju plaćanja.
- **Potpis**: Garantuje integritet fakture autentifikacijom svih informacija.

Fakture se zatim kodiraju u **bech32**, istom formatu kao za Bitcoin SegWit adrese (format koji počinje sa `bc1`).

### LNURL Povlačenje

U tradicionalnoj transakciji, kao što je kupovina u prodavnici, faktura se generiše za ukupan iznos koji treba platiti. Kada se faktura predstavi (u obliku QR koda ili niza karaktera), kupac je može skenirati i završiti transakciju. Plaćanje zatim prati tradicionalni proces koji smo proučavali u prethodnom odeljku. Međutim, ovaj proces ponekad može biti veoma nezgodan za korisničko iskustvo, jer zahteva da primalac pošalje informacije pošiljaocu putem fakture.

Za određene situacije, kao što je povlačenje bitkojna sa online servisa, tradicionalni proces je previše zamoran. U takvim slučajevima, rešenje za povlačenje **LNURL** pojednostavljuje ovaj proces prikazivanjem QR koda koji onda novčanik primaoca skenira kako bi automatski kreirao fakture. Servis zatim plaća fakturu, a korisnik jednostavno vidi trenutno povlačenje.

![LNP201](assets/en/69.webp)

LNURL je komunikacioni protokol koji precizira skup funkcionalnosti dizajniranih da pojednostave interakcije između Lajtning čvorova i klijenata, kao i aplikacija trećih strana. LNURL povlačenje, kao što smo upravo videli, je stoga samo jedan primer među ostalim funkcionalnostima.

Ovaj protokol se zasniva na HTTP-u i omogućava kreiranje linkova za razne operacije, kao što su zahtev za plaćanje, zahtev za povlačenje ili druge funkcionalnosti koje poboljšavaju korisničko iskustvo. Svaki LNURL je bech32 kodiran URL sa lnurl prefiksom, koji, kada se skenira, pokreće niz automatskih akcija na Lajtning novčaniku.

Na primer, funkcija LNURL-withdraw (LUD-03) omogućava povlačenje sredstava sa online servisa skeniranjem QR koda, bez potrebe za ručnim generisanjem fakture. Slično, LNURL-auth (LUD-04) omogućava prijavljivanje na online usluge korišćenjem privatnog ključa na nečijem Lajtning novčaniku umesto lozinke.

### Slanje Lajtning uplate bez fakture: Keysend

Još jedan zanimljiv slučaj je transfer sredstava bez prethodnog primanja fakture, poznat kao "**Keysend**". Ovaj protokol omogućava slanje sredstava dodavanjem ulazne vrednosti heša u šifrovane podatke o plaćanju, dostupne samo primaocu. Ova ulazna vrednost omogućava primaocu da otključa HTLC, čime se sredstva preuzimaju bez prethodnog generisanja fakture.

Da pojednostavimo, u ovom protokolu, pošiljalac je taj koji generiše tajnu korišćenu u HTLC-ovima, umesto primalac. Praktično, ovo omogućava pošiljaocu da izvrši uplatu bez prethodne interakcije sa primaocem.

![LNP201](assets/en/70.webp)

**Šta bi trebalo da ponesete iz ovog poglavlja?**


- **Lajtning faktura** je zahtev za plaćanje koji se sastoji od dela čitljivog za ljude i dela sa podacima za mašinu.
- Faktura je kodirana u **bech32**, sa separatorom `1` radi lakšeg kopiranja i sastoji se od podataka koji sadrže sve informacije potrebne za obradu plaćanja.
- Drugi procesi plaćanja postoje na Lajtning mreži, posebno **LNURL-Withdraw** za olakšavanje povlačenja, i **Keysend** za direktne transfere bez fakture.

U sledećem poglavlju, videćemo kako operater čvora može upravljati likvidnošću u svojim kanalima, kako nikada ne bi bio blokiran i uvek mogao slati i primati uplate na Lajtning mrežu.

## Upravljanje Vašom Likvidnošću

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![video en](https://youtu.be/MIbej28La7Y)

U ovom poglavlju ćemo istražiti strategije za efikasno upravljanje likvidnošću na Lajtning mreži. Upravljanje likvidnošću varira u zavisnosti od tipa korisnika i konteksta. Pogledaćemo glavne principe i postojeće tehnike kako bismo bolje razumeli kako optimizovati ovo upravljanje.

### Potrebe za likvidnošću

Postoje tri glavna korisnička profila na Lajtningu, svaki sa specifičnim potrebama za likvidnošću:


- **Platilac**: Ovo je onaj koji vrši plaćanja. Oni trebaju odlaznu likvidnost kako bi mogli preneti sredstva drugim korisnicima. Na primer, to može biti potrošač.
- **Prodavac (ili Primilac uplata)**: Ovo je onaj koji prima uplate. Oni trebaju dolaznu likvidnost kako bi mogli prihvatiti uplate na svoj čvor. Na primer, ovo može biti preduzeće ili online prodavnica.
- **Usmeravač**: Međučvor, često specijalizovan za usmeravanje plaćanja, koji mora optimizovati svoju likvidnost u svakom kanalu kako bi usmerio što više plaćanja i zaradio naknade.

Ovi profili očigledno nisu fiksni; korisnik može prelaziti između platioca i primaoca u zavisnosti od transakcija. Na primer, Bob može primiti svoju platu putem Lajtninga od svog poslodavca, što ga stavlja u poziciju "prodavca" koji zahteva dolaznu likvidnost. Nakon toga, ako želi da koristi svoju platu za kupovinu hrane, postaje "platioc" i tada mora imati odlaznu likvidnost.

Da bismo bolje razumeli, uzmimo primer jednostavne mreže sastavljene od tri čvora: kupca (Alise), usmerivača (Suzi) i prodavca (Bob).

![LNP201](assets/en/71.webp)

Zamislite da kupac želi poslati 30.000 Sats prodavcu i da uplata ide kroz čvor usmerivača. Svaka strana tada mora imati minimalnu količinu likvidnosti u pravcu uplate:


- Platilac mora imati najmanje 30.000 satošija na svojoj strani kanala sa usmerivačem.
- Prodavac mora imati kanal gde je 30,000 satošija na suprotnoj strani da bi mogao da ih primi.
- Usmerivač mora imati 30.000 satošija na strani platioca u njihovom kanalu, i takođe 30.000 satošija na njihovoj strani u kanalu sa prodavcem, da bi mogao da usmeri uplatu.

![LNP201](assets/en/72.webp)

### Strategije upravljanja likvidnošću

Platioci moraju osigurati održavanje dovoljne likvidnosti na svojoj strani kanala kako bi garantovali odlaznu likvidnost. Ovo se pokazuje kao relativno jednostavno, jer je dovoljno otvoriti nove Lajtning kanale da bi se imala ova likvidnost. Naime, početna sredstva zaključana u višepotpisnoj baznoj transakciji su u potpunosti na strani platioca u Lightning kanalu na početku. Kapacitet plaćanja je stoga osiguran sve dok su kanali otvoreni sa dovoljno sredstava. Kada se odlazna likvidnost iscrpi, dovoljno je otvoriti nove kanale.

S druge strane, za prodavca, zadatak je složeniji. Da bi mogli da primaju uplate, moraju imati likvidnost na suprotnoj strani svojih kanala. Dakle, otvaranje kanala nije dovoljno: moraju takođe izvršiti uplatu u ovom kanalu kako bi premestili likvidnost na drugu stranu pre nego što sami mogu primati uplate. Za određene profile korisnika Lajtning mreže, kao što su trgovci, postoji jasna nesrazmera između onoga što njihov čvor šalje i onoga što prima, s obzirom na to da je cilj poslovanja prvenstveno da prikupi više nego što troši, kako bi ostvarili profit. Srećom, za ove korisnike sa specifičnim potrebama za dolaznom likvidnošću, postoji nekoliko rešenja:


- **Privlačenje kanala**: Trgovac ima prednost zbog obima očekivanih dolaznih uplata na svom čvoru. Uzimajući to u obzir, mogu pokušati privući posredničke čvorove koji traže prihod od naknada za transakcije i koji bi mogli otvoriti kanale prema njima, nadajući se da će usmeravati njihove uplate i prikupiti povezane naknade.
- **Kretanje likvidnosti**: Prodavac takođe može otvoriti kanal i preneti deo sredstava na suprotnu stranu tako što će izvršiti fiktivna plaćanja drugom čvoru, koji će vratiti novac na drugi način. U sledećem delu ćemo videti kako da izvedemo ovu operaciju.
- **Trokutasto otvaranje**: Platforme postoje za čvorove koji žele zajednički otvarati kanale, omogućavajući svakom da ima trenutnu dolaznu i odlaznu likvidnost. Na primer, [LightningNetwork+](https://lightningnetwork.plus/) nudi ovu uslugu. Ako Alisa, Bob i Suzi žele otvoriti kanal sa 100,000 Sats, mogu se dogovoriti na ovoj platformi da Alisa otvori kanal prema Bobu, Bob prema Suzi, a Suzi prema Alisi. Na ovaj način, svaki ima 100,000 Sats odlazne likvidnosti i 100,000 Sats dolazne likvidnosti, dok su zaključali samo 100,000 Sats.

![LNP201](assets/en/73.webp)


- **Kupovina kanala**: Postoje usluge za iznajmljivanje Lajtning kanala kako bi se dobila dolazna likvidnost, kao što su [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) ili [Lightning Labs Pool](https://lightning.engineering/pool/). Na primer, Alisa može kupiti kanal od milion satošija prema svom čvoru kako bi mogla primati uplate.

![LNP201](assets/en/74.webp)

Konačno, za usmerivače, čiji je cilj da maksimiziraju broj obrađenih uplata i prikupljenih naknada, oni moraju:


- Otvorite dobro finansirane kanale sa strateškim čvorovima.
- Redovno prilagođavaju raspodelu sredstava u kanalima prema potrebama mreže.

### Loop Out Usluga

Usluga [Loop Out](https://lightning.engineering/loop/), koju nudi Lightning Labs, omogućava premeštanje likvidnosti na suprotnu stranu kanala dok se sredstva vraćaju na Bitkojn blokčejn. Na primer, Alisa šalje 1 milion satošija putem Lajtninga ka loop čvoru, koji joj zatim vraća ta sredstva u baznim bitkoinima. Ovo balansira njen kanal sa 1 milion satošija na svakoj strani, optimizujući njen kapacitet za primanje uplata.

![LNP201](assets/en/75.webp)

Stoga, ova usluga omogućava dolaznu likvidnost dok vraća nečije bitkojne na bazni blokčejn, što pomaže u smanjivanju imobilizacije gotovine neophodne za prihvatanje plaćanja putem Lajtninga.

**Šta treba da ponesete iz ovog poglavlja?**


- Da biste slali uplate na Lajtning mreži, morate imati dovoljno likvidnosti na vašoj strani u vašim kanalima. Da biste povećali ovaj kapacitet slanja, jednostavno otvorite nove kanale.
- Da biste primali uplate, potrebno je da imate likvidnost na suprotnoj strani u vašim kanalima. Uvećanje ovog kapaciteta za primanje je složenije, jer zahteva da drugi otvore kanale prema vama, ili da izvrše (fiktivne ili stvarne) uplate kako bi premestili likvidnost na drugu stranu.
- Održavanje likvidnosti tamo gde je to potrebno može biti još izazovnije u zavisnosti od korišćenja kanala. Zato postoje alati i usluge koji pomažu da se kanali balansiraju prema želji.

U narednom poglavlju, predlažem da pregledamo najvažnije koncepte ove obuke.

# Idi Dalje

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Zaključak obuke

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![video en](https://youtu.be/coaskEGRjiU)

U ovom završnom poglavlju koje označava kraj obuke LNP201, predlažem da ponovo pregledamo važne koncepte koje smo zajedno obradili.

Cilj ove obuke bio je da vam pruži sveobuhvatno i tehničko razumevanje Lajtning mreže. Otkrili smo kako se Lajtning mreža oslanja na Bitkojn blokčejn za obavljanje off-chain transakcija, van Bitkojn blokčejna, dok zadržava osnovne karakteristike Bitkojna, posebno odsustvo potrebe za poverenjem u druge čvorove.

### Kanali Plaćanja

U početnim poglavljima, istražili smo kako dve strane, otvaranjem platnog kanala, mogu obavljati transakcije van Bitkojn blokčejna. Evo koraka koji su obuhvaćeni:


- **Otvaranje Kanala**: Kreiranje kanala se vrši putem Bitkojn transakcije koja zaključava sredstva u 2/2 višepotpisnoj adresi. Ovaj depozit predstavlja Lajtning kanal na Bitkojn blokčejnu.

![LNP201](assets/en/76.webp) 
2.**Transakcije unutar kanala**: Unutar ovih platnih kanala, onda je moguće izvršiti bezbroj transakcija bez potrebe da se transakcije objavljuju na baznom blokčejnu. Svaka Lajtning transakcija kreira novo stanje kanala koje se reflektuje u Obavezujućoj transakciji. 
![LNP201](assets/en/77.webp)


- **Osiguranje i Zatvaranje**: Učesnici se obavezuju na novo stanje kanala razmenom ključeva za opoziv kako bi osigurali sredstva i sprečili bilo kakvu prevaru. Oba učesnika mogu zatvoriti kanal kooperativno pravljenjem nove transakcije na Bitkojn blokčejnu, ili kao poslednja opcija kroz prisilno zatvaranje. Ova poslednja opcija, iako manje efikasna jer je duža i ponekad loše ocenjena u smislu naknada, ipak omogućava povraćaj sredstava. U slučaju prevare, žrtva može kazniti prevaranta povraćajem svih sredstava iz kanala na Blokčejn.

![LNP201](assets/en/78.webp)

### Mreža kanala

Nakon proučavanja izolovanih kanala, proširili smo našu analizu na mrežu kanala:


- **Usemeravanje**: Kada dve strane nisu direktno povezane kanalom, mreža omogućava rutiranje kroz posredničke čvorove. Plaćanja tada prolaze sa jednog čvora na drugi.

![LNP201](assets/en/79.webp)


- **HTLC**: Plaćanja koja prolaze kroz posredničke čvorove su osigurana "_Hash Time-Locked Contracts_" (HTLC), što omogućava da sredstva budu zaključana dok se plaćanje ne završi od početka do kraja.

![LNP201](assets/en/80.webp)


- **Onion usemeravanje**: Da bi se osigurala poverljivost plaćanja, onion usmeravanje maskira krajnju destinaciju za posredničke čvorove. Čvor koji šalje mora stoga izračunati celu rutu, ali u nedostatku potpunih informacija o likvidnosti kanala, nastavlja kroz sukcesivne pokušaje da usmeri plaćanje.

![LNP201](assets/en/81.webp)

### Upravljanje Likvidnošću

Videli smo da je upravljanje likvidnošću izazov na Lajtning mreži kako bi se osigurao nesmetan tok plaćanja. Slanje plaćanja je relativno jednostavno: zahteva samo otvaranje kanala. Međutim, primanje plaćanja zahteva da se ima likvidnost na suprotnoj strani nečijih kanala. Evo nekih strategija koje su diskutovane:


- **Privlačenje kanala**: Kada korisnik podsticanjem drugih čvorova da otvore kanale prema njemu, time obezbeđuje dolaznu likvidnost.
- **Premeštanje likvidnosti**: Slanjem uplata na druge kanale, likvidnost se pomera na suprotnu stranu.

![LNP201](assets/en/82.webp)


- **Korišćenje usluga kao što su Loop i Pool**: Ove usluge omogućavaju rebalansiranje ili kupovinu kanala sa likvidnošću na suprotnoj strani.

![LNP201](assets/en/83.webp)


- **Kolaborativna Otvaranja**: Dostupne su i platforme za povezivanje radi izvođenja trostranih otvaranja i za obezbeđivanje dolazne likvidnosti.

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
