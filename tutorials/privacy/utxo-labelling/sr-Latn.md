---
name: Označavanje UTXO-a
description: Kako pravilno označiti svoj UTXO?
---
![cover](assets/cover.webp)


U ovom vodiču ćete otkriti sve što treba da znate o označavanju UTXO-a u vašem Bitcoin novčaniku i o kontroli novčića. Počinjemo sa teorijskim delom kako bismo u potpunosti razumeli ove pojmove, pre nego što pređemo na praktični deo gde istražujemo kako konkretno koristiti oznake u glavnom Bitcoin Wallet softveru.


## Šta je UTXO označavanje?

[Označavanje, engl. "labelling"](https://planb.network/resources/glossary/labeling), je tehnika koja uključuje povezivanje anotacije ili oznake sa specifičnim UTXO-om unutar Bitcoin novčanika. Ove anotacije se čuvaju lokalno od strane softvera novčanika i nikada se ne prenose preko Bitcoin mreže. Označavanje je stoga alat za lično upravljanje.


Na primer, ako primim UTXO iz P2P transakcije putem Bisq-a sa Charlesom, mogao bih UTXO-u dodeliti oznaku `Bisq P2P Purchase Charles`.


Označavanje omogućava da se zapamti poreklo ili predviđena destinacija UTXO-a, što pojednostavljuje upravljanje fondovima i optimizuje privatnost korisnika. Označavanje postaje još relevantnije kada se kombinuje sa funkcionalnošću ["kontrole novčića"](https://planb.network/resources/glossary/coin-control). Kontrola novčića je opcija dostupna u dobrim Bitcoin novčanicima, koja korisniku daje mogućnost da ručno izabere koje će specifične UTXO koristiti kao ulazi prilikom kreiranja transakcije.


Korišćenje novčanika sa kontrolom novčića, u kombinaciji sa UTXO označavanjem, omogućava korisnicima da precizno razlikuju i biraju UTXO-e za svoje transakcije, čime se izbegava spajanje UTXO-a iz različitih izvora. Ova praksa smanjuje rizike povezane sa heuristikom zajedničkog vlasništva nad ulazima (CIOH), koja pretpostavlja da svi ulazi u jednoj transakciji pripadaju istoj osobi, što može ugroziti privatnost korisnika.


Hajde da se vratimo na primer mog no-KYC UTXO-a sa Bisq-a; želim da izbegnem kombinovanje sa UTXO-om koji dolazi, recimo, sa regulisane platforme za trgovinu koja zna moj identitet. Postavljanjem posebne oznake na moj no-KYC UTXO i na moj KYC UTXO, moći ću lako da identifikujem koji UTXO da koristim kao ulaz za plaćanje troška, koristeći funkcionalnost kontrole novčića.


## Kako pravilno označiti svoj UTXO?

Ne postoji univerzalna metoda za označavanje UTXO-a koja odgovara svima. Na vama je da definišete sistem označavanja kako biste se lako snašli u svom novčaniku.

Ključni kriterijum u označavanju je izvor UTXO-a. Trebalo bi jednostavno naznačiti kako je ovaj novčić stigao u vaš novačnik. Da li je sa platforme za trgovinu? Namirenje računa od strane klijenta? Peer-to-peer razmena? Ili predstavlja kusur od kupovine? Tako biste mogli navesti:


- `Povlačenje Exchange.com`;
- `Plaćanje klijenta David`;
- `P2P kupovina Charles`;
- `Povraćaj od kupovine sofe`.

![labelling](assets/en/1.webp)

Da biste poboljšali upravljanje UTXO-om i pridržavali se strategija segregacije fondova unutar vašeg novčanika, možete obogatiti svoje oznake dodatnim indikatorom koji odražava ove razdvajanje. Ako vaš novčanik sadrži dve kategorije UTXO-a koje ne želite da mešate, možete integrisati marker u svoje oznake kako biste jasno razlikovali ove grupe.


Ovi markeri razdvajanja će zavisiti od vaših sopstvenih kriterijuma, kao što je razlika između KYC UTXO (poznavanje vašeg identiteta) i no-KYC (anonimno), ili između profesionalnih i ličnih sredstava. Uzimajući prethodno pomenute primere oznaka, ovo bi se moglo prevesti kao:


- `KYC - Povlačenje Exchange.com`;
- `KYC - Klijent za plaćanje David`;
- `NO KYC - P2P kupovina Charles`;
- `BEZ KYC - Promena od kupovine sofe`.

![labelling](assets/en/2.webp)

U svakom slučaju, imajte na umu da je dobro označavanje ono koje ćete moći razumeti kada vam bude potrebno. Ako je vaš Bitcoin novčanik prvenstveno namenjen za štednju, može se desiti da će vam oznake biti korisne tek za nekoliko decenija. Stoga, pobrinite se da budu jasne, precizne i sveobuhvatne.


Takođe je preporučljivo da se obeležavanje novčića održava tokom transakcija. Na primer, tokom UTXO konsolidacije bez KYC, obavezno označite rezultat kao `konsolidacija bez KYC`, a ne samo kao `konsolidacija`, kako biste održali jasan trag porekla novčića.


Na kraju, nije obavezno dodavati datum u oznaku (labelu). Većina softvera za novčanike već prikazuje datum transakcije, a tu informaciju je uvek moguće pronaći i putem blockchain explorera, koristeći TXID (identifikator transakcije).


## Uputstvo: Obeležavanje na Specter Desktop-u


Povežite i otvorite svoj novčanik na Specter Desktop, zatim izaberite karticu `Addresses`.


![labelling](assets/notext/3.webp)

Ovde ćete videti listu svih vaših adresa, kao i sve bitkoine koji su na njima zaključani. Podrazumevano, adrese su identifikovane po svom indeksu u koloni `Label`. Da biste promenili oznaku, jednostavno kliknite na nju, unesite željenu oznaku, a zatim potvrdite klikom na plavu ikonu.

![labelling](assets/notext/4.webp)


Vaša oznaka će se zatim pojaviti na listi vaših adresa.


![labelling](assets/notext/5.webp)


Takođe možete unapred dodeliti oznaku kada delite svoju prijemnu adresu sa pošiljaocem. Da biste to uradili, pristupom kartici `Receive`, zabeležite svoju oznaku u predviđenom polju.


![labelling](assets/notext/6.webp)


## Uputstvo: Obeležavanje na Electrum-u


Na Electrum novčaniku, nakon prijavljivanja na vaš novčanik, kliknite na transakciju kojoj želite dodeliti oznaku iz kartice `History`.


![labelling](assets/notext/7.webp)


Otvara se novi prozor. Kliknite na polje `Description` i unesite svoju oznaku.


![labelling](assets/notext/8.webp)


Kada se etiketa unese, možete zatvoriti ovaj prozor.


![labelling](assets/notext/9.webp)


Vaša oznaka je uspešno sačuvana. Možete je pronaći pod karticom `Description`, u prevodu `Opis`.


![labelling](assets/notext/10.webp)


Na kartici `Coins`, sa koje možete vršiti kontrolu novčića, vaša oznaka se nalazi u koloni `Label`.


![labelling](assets/notext/11.webp)


## Uputstvo: Obeležavanje na Green novčaniku


U aplikaciji Green Wallet, pristupite svom novčaniku i odaberite transakciju koju želite označiti. Zatim kliknite na malu ikonu olovke da zabeležite svoju oznaku.


![labelling](assets/notext/12.webp)


Unesite svoju oznaku, a zatim kliknite na zeleno dugme `Save`.


![labelling](assets/notext/13.webp)


Moći ćete pronaći svoju oznaku kako u detaljima vaše transakcije, tako i na kontrolnoj tabli vašeg novčanika.


![labelling](assets/notext/14.webp)


## Uputstvo: Obeležavanje na Samourai novčaniku


U Samourai novčaniku, postoje različite metode koje vam omogućavaju da dodelite oznaku transakciji. Za prvu, počnite otvaranjem vašeg novčaniku i odaberite transakciju kojoj želite da dodate oznaku. Zatim pritisnite dugme `Add`, koje se nalazi pored polja `Notes`.


![labelling](assets/notext/15.webp)


Unesite svoju oznaku i potvrdite klikom na plavo dugme `Add`, u prevodu `Dodaj`.


![labelling](assets/notext/16.webp)


Naći ćete svoju oznaku u detaljima vaše transakcije, ali i na kontrolnoj tabli vašeg novčanika.


![labelling](assets/notext/17.webp)

Za drugi metod, kliknite na tri male tačke u gornjem desnom uglu ekrana, zatim na meni `Show Unspent Transaction Outputs`, u prevodu `Prikaži neiskorišćene izlaze transakcija`.

![labelling](assets/notext/18.webp)


Ovde ćete pronaći sveobuhvatnu listu svih UTXO-a prisutnih u vašem novčaniku. Prikazana lista se odnosi na moj depozitni račun, međutim, ova operacija se može ponoviti za Whirlpool račune navigacijom iz posebnog menija.


Zatim kliknite na UTXO koji želite označiti, a zatim na dugme `Add`.


![labelling](assets/notext/19.webp)


Unesite svoju oznaku i potvrdite klikom na plavo dugme `Add`, u prevodu `Dodaj`. Zatim ćete pronaći svoju oznaku kako u detaljima vaše transakcije, tako i na kontrolnoj tabli vašeg novčanika.


![labelling](assets/notext/20.webp)


## Uputstvo: Obeležavanje na Sparrow novčaniku


Sa softverom Sparrow novčanik, moguće je dodeliti oznake na više načina. Najjednostavniji metod je dodavanje oznake unapred, kada se primajuća adresa komunicira pošiljaocu. Da biste to uradili, u meniju `Receive`, kliknite na polje `Label` i unesite oznaku po vašem izboru. Ovo će biti sačuvano i dostupno kroz softver čim bitkoini budu primljeni na adresu.


![labelling](assets/notext/21.webp)


Ako ste zaboravili da označite svoju adresu po prijemu, i dalje je moguće dodati oznaku kasnije putem menija `Transactions`. Jednostavno kliknite na svoju transakciju unutar kolone `Label`, zatim unesite željenu oznaku.


![labelling](assets/notext/22.webp)


Takođe imate opciju da dodate ili izmenite svoje oznake iz menija `Addresses`, u prevodu `Adrese`.


![labelling](assets/notext/23.webp)


Konačno, možete pregledati svoje oznake u meniju `UTXOs`. Sparrow novčanik automatski dodaje u zagrade iza vaše oznake prirodu izlaza, što pomaže u razlikovanju UTXO-a koji su rezultat kusura od onih primljenih direktno.


![labelling](assets/notext/24.webp)
