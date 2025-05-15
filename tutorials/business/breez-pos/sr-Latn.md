---
name: Breez point of sales

description: Vodič za početak prihvatanja Bitcoin koristeći Breez POS
---

![cover](assets/cover.webp)

_Ovaj tekst dolazi sa Breez dokumentacionog sajta: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_


## Šta je Breez POS?


**Breez** je aplikacija za Lightning sa punom uslugom, bez starateljstva. Hajde da to razložimo:



- Lightning** je Bitcoin platna mreža koja smanjuje vreme transakcije sa minuta na milisekunde i naknade za transakcije sa nekoliko dolara na nekoliko centi ili manje. Lightning pretvara Bitcoin iz digitalnog zlata u digitalnu valutu, zadržavajući sve prednosti koje čine Bitcoin odličnim.
- Nekustodijalno** znači da Breez ne preuzima vlasništvo nad novcem korisnika. Mnoge Lightning aplikacije preuzimaju vlasništvo nad novcem svojih korisnika. One su u suštini Bitcoin banke. Sa nekustodijalnom aplikacijom kao što je Breez, svi korisnici su svoje sopstvene banke.
- Full-service** znači da Breez automatski i u pozadini brine o gotovo svim tehničkim operacijama. Stvari poput kreiranja kanala, dolazne likvidnosti i rutiranja ostaju ispod haube. (Ali Breez je takođe otvorenog koda, tako da su svi zainteresovani za reviziju tehnologije dobrodošli da to učine!)


**Breez POS** je skraćenica za naš režim prodajnog mesta. Drugim rečima, Breez funkcioniše kao digitalna kasa za preduzeća i trgovce koji žele da prihvate Lightning uplate (pored svog "standardnog" režima, koji je kao digitalna verzija kožnog Wallet za Bitcoin, i plejera za podkaste sledeće generacije). Sada ćemo pogledati kako da postavite Breez kao Lightning kasu za vaše poslovanje.


## Kako započeti sa Breez?


1. Prvi korak je preuzimanje aplikacije. Dostupna je za Android i iOS (instalirajte TestFlight i kliknite na link sa svog uređaja).

2. Breez može automatski da se bekapuje na Google Drive, iCloud, ili bilo koji WebDav server.

**Napomena:** svaki uređaj pokreće svoj Lightning čvor. Možete pokrenuti POS režim na koliko god uređaja želite, ali stanja će ostati odvojena.

3. Sa otvorenom aplikacijom, kliknite na ikonu u gornjem levom uglu da pronađete režim Prodajnog mesta.


## Postavljanje POS-a


Da biste postavili POS, kliknite na ikonu u gornjem levom uglu, zatim kliknite na Point of Sale > POS Settings.


### Lozinka Menadžera


U podešavanjima POS-a, imate opciju da kreirate lozinku menadžera. Lozinka menadžera onemogućava slanje odlaznih uplata iz Breez aplikacije bez autorizacije. Prodajno osoblje će moći samo da prima uplate sa uređaja. Imajte na umu da ako koristite ovu opciju, možda ćete želeti da sprečite pristup Breez-ovoj rezervnoj kopiji, pa se preporučuje korišćenje eksternog WebDav naloga (npr. Nextcloud) za ovu svrhu.


### Lista stavki


Lista artikala je katalog artikala za prodaju i njihovih cena. Postoje dva načina za dodavanje artikala na listu:



- Da biste uneli stavke jednu po jednu, kliknite na Stavke blizu vrha glavnog prikaza POS-a, a zatim na znak "+" u donjem desnom uglu. Ovde možete uneti naziv jedne vrste stavke, cenu (prikazanu u valuti po vašem izboru) i SKU (jedinstveni interni identifikator za tu vrstu stavke; opcionalno je).
- Da biste uneli više stavki odjednom, kliknite na ikonu kalkulatora u gornjem levom uglu, zatim Point of Sale > Preferences > POS Settings, i zatim kliknite na tri tačke desno od Items List, a zatim na Import from CSV. Ovo će vam omogućiti da uvezete CSV fajl koji ste unapred pripremili i koji sadrži nazive vaših stavki, cene i SKU-ove.


### Fiat Display


Breez šalje i prima samo Bitcoin, a za većinu transakcija na Lightning mreži, koje su obično za manje iznose, suma je obično prikazana u Satošijima, tj. Sats (1 BTC = 100,000,000 Sats). Međutim, mnogi trgovci smatraju praktičnim da mogu videti (i reći kupcima) vrednost kupovine prikazanu u lokalnoj fiat valuti.


U glavnom prikazu POS-a, valuta koja se trenutno prikazuje vidljiva je na desnoj strani (podrazumevano je SAT). Tu je i padajuća lista drugih dostupnih valuta za prikaz. Da biste dodali ili uklonili valute iz ove padajuće liste, kliknite na Point of Sale > Preferences > Fiat Currencies. Zatim jednostavno označite valute koje želite da imate u svom padajućem meniju i poništite one koje želite da izostavite.


Prikazane vrednosti su sa yadio, uglednog izvora za Exchange-kurs podatke, i ažuriraju se gotovo u realnom vremenu. Ali zapamtite: koja god vrednost valute trenutno bila prikazana, sama uplata je u Bitcoin.


### Punjenje narudžbine


Da sastavite porudžbinu, dodajte stavke sa liste artikala ili jednostavno unesite iznos na tastaturi. Zatim kliknite na Naplati na vrhu glavnog pregleda POS-a. Tada ćete videti QR kod koji kupac može skenirati svojim Lightning aplikacijom, koji možete direktno podeliti iz druge aplikacije na vašem uređaju, ili koji možete kopirati i nalepiti gde je potrebno.


Na skeniranju tog koda ili klikom na podeljeni/nalepeni Invoice, kupac će videti Invoice u svojoj Lightning aplikaciji i imati opciju da ga plati i odmah završi transakciju.


Jednom kada vidite animaciju Payment approved! u aplikaciji Breez na uređaju trgovca, možete kliknuti na ikonu štampača da generate štampate račun za kupca. Da biste koristili štampač računa na Androidu, pokušajte koristiti ovaj drajver. Imajte na umu da možete štampati i prethodne transakcije putem ekrana Transakcije.


### Izveštaj o prodaji


Da biste videli dnevni, nedeljni i/ili mesečni izveštaj o vašoj prodaji (za računovodstvene svrhe ili druge), kliknite na ikonu u gornjem levom uglu, a zatim kliknite na Transakcije. Kliknite na ikonu Izveštaj da biste prikazali izveštaj i na ikonu Kalendar da biste promenili izabrani vremenski period.


### Izvoz transakcija


Da biste videli listu primljenih uplata u Breez-u, kliknite na ikonu u gornjem levom uglu, a zatim kliknite na Transakcije. Kliknite na tri tačke u gornjem desnom uglu, zatim na Izvoz da biste izvezli listu dolaznih uplata u CSV formatu. Da biste ograničili listu na određeni vremenski period, kliknite na ikonu kalendara da postavite vremenski raspon.


### Štampanje Računa


Da biste odštampali račun o prodaji, kliknite na ikonu štampanja u gornjem desnom uglu dijaloga za potvrdu plaćanja. Alternativno, kliknite na ikonu u gornjem levom uglu, a zatim kliknite na Transakcije. Pronađite prodaju za štampanje, otvorite je i kliknite na ikonu štampanja u gornjem desnom uglu.


**Napomena:** koristite ovaj drajver za štampanje na prenosivom 58mm/80mm Bluetooth/USB termalnom štampaču.


## Želim da naučim više



- Za više informacija o Lightning i Breez, pogledajte naš [blog](https://breez.technology/blog).
- Za više tehničkih saveta o tome kako da maksimalno iskoristite aplikaciju i izvršite uobičajene operacije, pogledajte našu [dokumentaciju](https://breez.technology/documentation).
- Ako zapnete i ne možete pronaći odgovor u bilo kojoj našoj pomoći, možete nas pronaći na [Telegramu](https://t.me/breez_labs) ili nam poslati [email](mailto:support@breez.technology).
- Ako želite da pogledate neke demonstracione video snimke Breez POS moda u akciji koje su napravili naši fanovi i korisnici, [ovde](https://www.youtube.com/watch?v=xxxx) je jedan odličan kratak, a [ovde](https://www.youtube.com/watch?v=xxxx) je duži, detaljniji.