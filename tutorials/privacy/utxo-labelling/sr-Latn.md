---
name: Označavanje UTXO
description: Kako pravilno označiti svoj UTXO?
---
![cover](assets/cover.webp)


U ovom vodiču ćete otkriti sve što treba da znate o označavanju UTXO-a u vašem Bitcoin Wallet i o kontroli novčića. Počinjemo sa teorijskim delom kako bismo u potpunosti razumeli ove pojmove, pre nego što pređemo na praktični deo gde istražujemo kako konkretno koristiti oznake u glavnom Bitcoin Wallet softveru.


## Šta je UTXO označavanje?

"Labelling" je tehnika koja uključuje povezivanje anotacije ili oznake sa specifičnim UTXO unutar Bitcoin Wallet. Ove anotacije se čuvaju lokalno od strane Wallet softvera i nikada se ne prenose preko Bitcoin mreže. Labelling je stoga alat za lično upravljanje.


Na primer, ako primim UTXO iz P2P transakcije putem Bisq-a sa Charlesom, mogao bih joj dodeliti oznaku `Bisq P2P Purchase Charles`.


Označavanje omogućava da se zapamti poreklo ili predviđena destinacija UTXO, što pojednostavljuje upravljanje fondovima i optimizuje privatnost korisnika. Označavanje postaje još relevantnije kada se kombinuje sa funkcionalnošću "kontrole novčića". Kontrola novčića je opcija dostupna u dobrim Bitcoin novčanicima, koja korisniku daje mogućnost da ručno izabere koje će se specifične UTXO koristiti kao ulazi prilikom kreiranja transakcije.


Korišćenje Wallet sa kontrolom novčića, u kombinaciji sa UTXO označavanjem, omogućava korisnicima da precizno razlikuju i biraju UTXO-e za svoje transakcije, čime se izbegava spajanje UTXO-a iz različitih izvora. Ova praksa smanjuje rizike povezane sa Heuristikom Zajedničkog Ulaza Ownership (CIOH), koja sugeriše zajednički Ownership ulaza transakcije, što može ugroziti privatnost korisnika.


Hajde da se vratimo na primer mog no-KYC UTXO sa Bisq-a; želim da izbegnem kombinovanje sa UTXO koji dolazi, recimo, sa regulisane Exchange platforme koja zna moj identitet. Postavljanjem posebne oznake na moj no-KYC UTXO i na moj KYC UTXO, moći ću lako da identifikujem koji UTXO da koristim kao ulaz za ispunjavanje troška, koristeći funkcionalnost kontrole novčića.


## Kako pravilno označiti svoj UTXO?

Ne postoji univerzalna metoda za označavanje UTXO-a koja odgovara svima. Na vama je da definišete sistem označavanja kako biste se lako snašli u svom Wallet.

Ključni kriterijum u označavanju je izvor UTXO. Trebalo bi jednostavno naznačiti kako je ovaj novčić stigao u vaš Wallet. Da li je sa Exchange platforme? Namirenje računa od strane klijenta? Peer-to-peer Exchange? Ili predstavlja kusur od kupovine? Tako biste mogli navesti:


- `Povlačenje Exchange.com`;
- `Plaćanje Klijent David`;
- `P2P Kupovina Charles`;
- `Povraćaj od kupovine sofe`.

![labelling](assets/en/1.webp)

Da biste poboljšali upravljanje UTXO i pridržavali se strategija segregacije fondova unutar vašeg Wallet, možete obogatiti svoje oznake dodatnim indikatorom koji odražava ove razdvajanja. Ako vaš Wallet sadrži dve kategorije UTXO-a koje ne želite da mešate, možete integrisati marker u svoje oznake kako biste jasno razlikovali ove grupe.


Ovi markeri razdvajanja će zavisiti od vaših sopstvenih kriterijuma, kao što je razlika između KYC UTXO (poznavanje vašeg identiteta) i no-KYC (anonimno), ili između profesionalnih i ličnih sredstava. Uzimajući prethodno pomenute primere oznaka, ovo bi se moglo prevesti kao:


- `KYC - Povlačenje Exchange.com`;
- `KYC - Klijent za Plaćanje David`;
- `NO KYC - P2P Kupovina Charles`;
- `BEZ KYC - Promena od kupovine sofe`.

![labelling](assets/en/2.webp)

U svakom slučaju, imajte na umu da je dobro označavanje ono koje ćete moći razumeti kada vam bude potrebno. Ako je vaš Bitcoin Wallet prvenstveno namenjen za štednju, može se desiti da će vam oznake biti korisne tek za nekoliko decenija. Stoga, pobrinite se da budu jasne, precizne i sveobuhvatne.


Takođe je preporučljivo da se obeležavanje novčića održava tokom transakcija. Na primer, tokom UTXO konsolidacije bez KYC, obavezno označite rezultat kao `konsolidacija bez KYC`, a ne samo kao `konsolidacija`, kako biste održali jasan trag porekla novčića.


Konačno, nije obavezno staviti datum na etiketu. Većina Wallet softvera već prikazuje datum transakcije, i uvek je moguće preuzeti ovu informaciju na Block explorer koristeći njegov txid.


## Uputstvo: Obeležavanje na Specter Desktop


Povežite i otvorite svoj Wallet na Specter Desktop, zatim izaberite karticu `Addresses`.


![labelling](assets/notext/3.webp)

Ovde ćete videti listu svih vaših adresa, kao i sve bitkoine koji su na njima zaključani. Podrazumevano, adrese su identifikovane po svom indeksu u koloni `Label`. Da biste promenili oznaku, jednostavno kliknite na nju, unesite željenu oznaku, a zatim potvrdite klikom na plavi ikonu.

![labelling](assets/notext/4.webp)


Vaša oznaka će se zatim pojaviti na listi vaših adresa.


![labelling](assets/notext/5.webp)


Takođe možete unapred dodeliti oznaku kada delite svoj prijemni Address sa pošiljaocem. Da biste to uradili, pristupom kartici `Receive`, zabeležite svoju oznaku u predviđenom polju.


![labelling](assets/notext/6.webp)


## Uputstvo: Obeležavanje na Electrum


Na Electrum Wallet, nakon prijavljivanja na vaš Wallet, kliknite na transakciju kojoj želite dodeliti oznaku iz kartice `History`.


![labelling](assets/notext/7.webp)


Otvara se novi prozor. Kliknite na polje `Description` i unesite svoju oznaku.


![labelling](assets/notext/8.webp)


Kada se etiketa unese, možete zatvoriti ovaj prozor.


![labelling](assets/notext/9.webp)


Vaša oznaka je uspešno sačuvana. Možete je pronaći pod karticom `Opis`.


![labelling](assets/notext/10.webp)


Na kartici `Coins`, sa koje možete vršiti kontrolu novčića, vaša oznaka se nalazi u koloni `Label`.


![labelling](assets/notext/11.webp)


## Uputstvo: Obeležavanje na Green Wallet


U aplikaciji Green Wallet, pristupite svom Wallet i odaberite transakciju koju želite označiti. Zatim kliknite na malu ikonu olovke da zabeležite svoju oznaku.


![labelling](assets/notext/12.webp)


Unesite svoju oznaku, a zatim kliknite na dugme `Save` Green.


![labelling](assets/notext/13.webp)


Moći ćete pronaći svoju oznaku kako u detaljima vaše transakcije, tako i na kontrolnoj tabli vašeg Wallet.


![labelling](assets/notext/14.webp)


## Uputstvo: Obeležavanje na Samourai Wallet


U Samourai Wallet, postoje različite metode koje vam omogućavaju da dodelite oznaku transakciji. Za prvu, počnite otvaranjem vašeg Wallet i odaberite transakciju kojoj želite da dodate oznaku. Zatim pritisnite dugme `Add`, koje se nalazi pored polja `Notes`.


![labelling](assets/notext/15.webp)


Unesite svoju oznaku i potvrdite klikom na plavo dugme `Dodaj`.


![labelling](assets/notext/16.webp)


Naći ćete svoju oznaku u detaljima vaše transakcije, ali i na kontrolnoj tabli vašeg Wallet.


![labelling](assets/notext/17.webp)

Za drugi metod, kliknite na tri male tačke u gornjem desnom uglu ekrana, zatim na meni `Prikaži neiskorišćene izlaze transakcija`.

![labelling](assets/notext/18.webp)


Ovde ćete pronaći sveobuhvatnu listu svih UTXO-a prisutnih u vašem Wallet. Prikazana lista se odnosi na moj depozitni račun, međutim, ova operacija se može ponoviti za Whirlpool račune navigacijom iz posebnog menija.


Zatim kliknite na UTXO koji želite označiti, a zatim na dugme `Add`.


![labelling](assets/notext/19.webp)


Unesite svoju oznaku i potvrdite klikom na plavo dugme `Dodaj`. Zatim ćete pronaći svoju oznaku kako u detaljima vaše transakcije, tako i na kontrolnoj tabli vašeg Wallet.


![labelling](assets/notext/20.webp)


## Uputstvo: Obeležavanje na Sparrow Wallet


Sa softverom Sparrow Wallet, moguće je dodeliti oznake na više načina. Najjednostavniji metod je dodavanje oznake unapred, kada se prima Address komunicira pošiljaocu. Da biste to uradili, u meniju `Receive`, kliknite na polje `Label` i unesite oznaku po vašem izboru. Ovo će biti sačuvano i dostupno kroz softver čim bitkoini budu primljeni na Address.


![labelling](assets/notext/21.webp)


Ako ste zaboravili da označite svoj Address po prijemu, i dalje je moguće dodati oznaku kasnije putem menija `Transactions`. Jednostavno kliknite na svoju transakciju unutar kolone `Label`, zatim unesite željenu oznaku.


![labelling](assets/notext/22.webp)


Takođe imate opciju da dodate ili izmenite svoje oznake iz menija `Adrese`.


![labelling](assets/notext/23.webp)


Konačno, možete pregledati svoje oznake u meniju `UTXOs`. Sparrow Wallet automatski dodaje u zagrade iza vaše oznake prirodu izlaza, što pomaže u razlikovanju UTXO-a koji su rezultat kusura od onih primljenih direktno.


![labelling](assets/notext/24.webp)