---
name: Peach
description: Kompletan vodič za korišćenje Peach i trgovanje bitkoinima u P2P
---

![cover](assets/cover.webp)





## Uvod



Peer-to-peer razmene bez KYC (P2P) su ključne za očuvanje poverljivosti korisnika i finansijske autonomije. Omogućavaju direktne transakcije između pojedinaca bez potrebe za verifikacijom identiteta, što je od suštinskog značaja za one koji cene privatnost. Za dublje razumevanje teorijskih koncepata, pogledajte kurs BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Šta je Peach?



Peach je P2P platforma za razmenu koja omogućava korisnicima kupovinu i prodaju bitkoina bez KYC. Nudi intuitivan interfejs i napredne sigurnosne funkcije. U poređenju sa drugim rešenjima kao što su Bisq, HodlHodl i Robosat, Peach se ističe po lakoći korišćenja.


Sistem eskroua multisignature (2-2) garantuje sigurnost sredstava tokom transakcija. Peach podržava različite metode plaćanja i sadrži sistem reputacije koji vodi trgovce u njihovim akcijama. Kao i obično sa P2P platformama, stoga je važno održavati dobru reputaciju kako bi se održala kredibilnost kod drugih trgovaca.



### 2. Privatnost i prikupljeni podaci



**Koje informacije prikuplja Peach?



Peach nastoji da čuva apsolutni minimum podataka o svojim korisnicima. Ovde je pregled podataka koji se čuvaju na našim serverima:





- hash vašeg jedinstvenog identifikatora aplikacije (AdID)
- hash vaših podataka o plaćanju
- Vaši šifrovani razgovori
- Podaci o transakcijama kako bi se osiguralo da anonimni korisnici ne prekorače limit trgovanja (vrste korišćenih metoda plaćanja, iznosi kupovine i prodaje)
- Addresses korišćen za slanje i primanje sa escrow računa
- Podaci o korišćenju (Firebase i Google Analytics), samo uz vaš pristanak



Kao podsetnik, hash je podatak učinjen neprepoznatljivim, slično enkripciji. Isti podaci će uvek proizvesti isti hash, što omogućava detekciju duplikata bez poznavanja originalnih podataka.



*Za detaljnije objašnjenje hashing-a, pohađajte ovaj kurs:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Ko može videti moje podatke o plaćanju?





- Samo vaša suprotna strana može videti vaše podatke o plaćanju
- Podaci se prenose putem Peach servera, ali su potpuno šifrovani od kraja do kraja.
- U slučaju spora, vaši podaci o plaćanju i istorija razgovora biće vidljivi dodeljenom Peach posredniku.



## Instalacija i konfiguracija



### 1. Instalirajte aplikaciju Peach



![Installation de Peach](assets/fr/01.webp)





- Preuzmite aplikaciju sa [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). Na iOS-u, prvo ćete morati instalirati [testflight](https://apps.apple.com/us/app/testflight/id899247664) aplikaciju.
- Pratite uputstva za instalaciju na vašem uređaju.
- Tokom instalacije, bićete upitani da izaberete da li želite da delite određene podatke kako biste poboljšali Peach aplikaciju. (slika 1)
- Na sledećem ekranu (slika 2), imate dve opcije:
 - Ako ste novi korisnik, kliknite na "Novi korisnik" da biste kreirali novi profil.
 - Ako već imate nalog, koristite "Restore" da vratite svoj postojeći profil
- Ako imate referalni kod, možete ga uneti ovde.
- Da biste vratili postojeći nalog (slika 3), biće vam potrebno :
 - Vaša rezervna datoteka
 - Lozinka za dešifrovanje ove datoteke



### 2. Pregled glavnih ekrana



Aplikacija Peach je organizovana oko četiri glavna ekrana dostupna iz donje navigacione trake:



![Navigation dans l'application](assets/fr/02.webp)





- Početna (4)** : Glavni ekran sa kojeg možete izabrati da kupite ili prodate, kreirate nove transakcije i pristupite dostupnim ponudama:
 - kreiraj ponude pomoću dva dugmeta ispod (kreiraj kupovinu / kreiraj prodaju)
 - iskoristite postojeće ponude koje su kreirali drugi korisnici, koristeći dva dugmeta ispod ("Kupi"/"Prodaj").





- Wallet (5)** : Vaš integrisani bitcoin wallet koji vam omogućava da :
 - Proverite stanje vašeg računa
 - Primite bitkoine
 - Envoyer bitcoini (sa kontrolom novčića)
 - Pogledajte istoriju transakcija
 - Finansiranje vaše prodaje





- Trgovine (6)**: vaši trenutni i prošli ugovori, pod tri kartice:
 - Kupovine u toku
 - Prodaja u toku
 - Istorija vaših razmena





- Postavke (7)** : Čvorište za konfiguraciju
 - Pogledaj svoj profil (reputacija, bedževi, ograničenja, itd.)
 - Upravljanje sigurnošću (backup, pin)
 - Upravljajte svojim metodama plaćanja
 - Kontaktirajte podršku
 - Promeni jezik
 - itd.



### 3. Konfigurišite svoje metode plaćanja



![Accès aux paramètres de paiement](assets/fr/03.webp)



Možete upravljati svojim metodama plaćanja u postavkama (slika 8)



Peach nudi online plaćanja i plaćanja licem u lice (samo na registrovanim okupljanjima).



**Online plaćanja



**Važno:**


da zaštiti korisnike, Peach zahteva da izvor sredstava odgovara onom koji je oglašen. Na trgovcima je da osiguraju da je to slučaj, radi sopstvene zaštite.



![Configuration des paiements en ligne](assets/fr/04.webp)



Da dodate metodu :




- U kartici "online" kliknite na "dodaj valutu/metod"
- Izaberite svoju valutu
- Odaberite željeni način plaćanja



*Vrste dostupnih metoda plaćanja:*



***Za bankovne transfere: ***




- SEPA (standardna ili instant)
- Unesite podatke o svom SEPA bankovnom računu.



***Online wallets prihvaćeni :***




- Nekoliko opcija dostupno u zavisnosti od vaše zemlje (Revolut, Paypal, Wise, Strike, itd.)
- Pratite uputstva da dodate svoje podatke za prijavu



*gift kartica upotrebljiva:*** Gift kartica upotrebljiva:*** Gift kartica upotrebljiva:*** Gift kartica upotrebljiva:*** Gift kartica upotrebljiva:*** Gift kartica upotrebljiva:***




- Amazon, Steam, itd.
- Unesite zemlju izdavanja kartice i druge potrebne informacije



***Nacionalne opcije plaćanja:***


Sistemi plaćanja specifični za zemlju :




- Satispay (Italija)
- MB Way (Portugal)
- Bizum (Španija)
- Brže uplate (Ujedinjeno Kraljevstvo)
- itd.



***Za plaćanja licem u lice: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Odaberite "Meetup" (slika 12)
- Zatim izaberite svoj meetup sa liste (slika 13)



### Uputstva za upotrebu





- Možete dodati nekoliko metoda plaćanja
- Što više metoda dodate, širi će biti raspon ponuda kojima ćete imati pristup.
- Proverite tačnost vaših informacija pre nego što se registrujete
- Možete promeniti ili izbrisati svoje metode plaćanja u bilo kom trenutku.



**Beleška o bezbednosti**: Vaše informacije o plaćanju su šifrovane i dele se samo sa vašim partnerom u razmeni tokom transakcije, osim u slučaju spora kada će i Peach medijator imati pristup.



### 4. Kako osigurati svoj portfolio



**Razumevanje vašeg Peach naloga



Peach nalog nema korisničko ime i lozinku. To je datoteka koja je lokalno uskladištena na vašem telefonu, što znači da Peach ne treba da čuva vaše podatke ili zna vaš identitet: vi imate kontrolu. Ova datoteka sadrži sve vaše podatke: uključujući 12 reči za oporavak bitcoina, PGP ključeve, detalje o plaćanju i tako dalje. Zato je ključno sačuvati ovu datoteku i zaštititi je __robustnom__ lozinkom.



Ovaj pristup garantuje određeni stepen poverljivosti i ostavlja odgovornost za upravljanje podacima i rezervnim kopijama u rukama korisnika. Gubljenje telefona bez rezervne kopije znači gubitak pristupa vašem Peach nalogu i sredstvima.



**Kreirajte svoje rezervne kopije**






- Pristupite postavkama sa kartice u donjem desnom uglu početnog ekrana
- Izaberite opciju "backups" u meniju podešavanja



![Processus de sauvegarde](assets/fr/06.webp)



Dve vrste rezervne kopije su dostupne:



**Sačuvaj datoteku naloga (slika 14)**




- Kliknite na "Kreiraj novu rezervnu kopiju"
- Kreirajte **jaku** lozinku za šifrovanje vaše rezervne datoteke
- Pošaljite ovu datoteku na lokaciju koja će osigurati njenu redundanciju u slučaju gubitka telefona.



Rezerva datoteke vraća vaš kompletan Peach nalog, uključujući :




- Vaš portfolio
- Vaši načini plaćanja
- Podaci o plaćanju
- Istorija transakcija sa detaljima o suprotnim stranama i razgovorima sa njima



**Čuvanje fraze za oporavak (slika 15)**




- Pratite uputstva da prikažete svoju frazu za oporavak
- Pažljivo napišite reči tačnim redosledom.
- Čuvajte ovu rezervnu kopiju na sigurnom mestu, idealno različitom od datoteke naloga.



Fraza za oporavak vam omogućava da povratite :




- Vaša reputacija, vaša trgovina
- Vaša bitcoin sredstva



Ali **NE** sledeće:




- Vaši trenutni i prošli razgovori
- Podaci o plaćanju
- Informacije o drugoj strani u istoriji transakcija




## Kupovina i prodaja bitkoina



### 1.a Kako kupiti bitkoine: Prihvatite ponudu za prodaju



Prvi refleks kupca treba da bude da pogleda ponude za prodaju koje su već finansirane bitcoin-om.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Na početnom ekranu, kliknite na dugme "Kupi" (slika 16)
- Zatim možete pregledati listu bitkoina koji su postavljeni u escrow sistem i spremni su za prodaju (slika 17). Možete videti količinu, cenu (u % u odnosu na KYC tržište), metode plaćanja i prihvaćene valute.
- Koristite filtere za sortiranje i redosled ponuda (slika 18).
- Napomena: dugme na dnu stranice sa filterima omogućava vam da primite obaveštenje kada je objavljena ponuda koja odgovara vašim filterima; i dugme "resetuj", koje jednostavno briše sve filtere (slika 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Pogledajte ponudu koja vam odgovara i pošaljite zahtev za zamenu (slika 19)
- Možete podneti nekoliko zahteva za zamenu, a prva pozitivna ponuda će poništiti vaše ostale zahteve.
- Izvršite uplatu dogovorenim načinom.


**Podsetnik:** izvor sredstava mora odgovarati onom koji ste naveli prilikom dodavanja načina plaćanja.




- Potvrdite uplatu u aplikaciji čim bude završena**.
- Sačekajte da prodavac primi uplatu i to potvrdi (slika 20)
- I na kraju, ocenite svoje iskustvo sa prodavcem (slika 21)



![Réception des bitcoins](assets/fr/09.webp)





- Pratite status vaše transakcije
- Proverite potvrdu o prijemu bitkoina
- Sredstva će biti dostupna u vašem Peach portfoliju (slika 22 i 23)



### 1.b Kako kupiti bitkoine: Kreirajte ponudu



Ako ne možete pronaći odgovarajuću ponudu za prodaju, možete kreirati ponudu za kupovinu. Pošto ovo ne obavezuje bilo koji bitcoin u ovoj fazi, imaćete manje šanse da pronađete partnera za razmenu, posebno ako je vaš dosadašnji učinak i reputacija loša ili nepostojeća. Da biste to ispravili, važno je, prilikom kreiranja ponude, *napraviti ponudu sa visokim premijama* kako biste motivisali prodavce da izaberu vašu ponudu. Nastavimo:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Na početnom ekranu kliknite na dugme "Kreiraj ponudu za kupovinu" (slika 24)
- Dodajte način plaćanja, ako to već niste učinili, i unesite svoje preferencije (količina, premium itd.) (slika 25).


Opcija "instant" vam omogućava da automatski prihvatite zahtev za trgovinu.




 - Ponovo kliknite na "create a bid" da nastavite
- Jednom kada je kreiran, na red dolaze prodavci da vam se obrate sa zahtevom za razmenu. Možete zatvoriti i izaći iz aplikacije bez brige.
- Premiju možete promeniti ako ne dobijete nikakve zahteve. Zapamtite: viša premija će motivisati prodavce da potraže vašu ponudu (slika 26).
- Ponudu ćete pronaći na kartici "Buy", koja se nalazi u prozoru "Exchange" (slika 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Kada primite zahtev za kupovinu (slika 28) (i ako niste deaktivirali instant trgovinu na slici 25), prihvatite trgovinu nakon provere reputacije prodavca. Ako je instant trgovina omogućena, pređite direktno na sliku 29.
- Prodavac tada mora da postavi bitcoin u sistem eskroua, („finansira sef“). (slika 29)
- Zatim platite prodavcu na odredištu prikazanom na Slici 30, putem vašeg ličnog bankarskog sistema. Nemojte povlačiti kursor "Izvršio sam uplatu" dok to ne učinite!
- Možete komunicirati sa prodavcem putem sistema za razmenu poruka (P2P šifrovano). U slučaju problema, možete otvoriti spor klikom na ikonu u gornjem desnom uglu (slika 31). Tada će Peach medijator ući u diskusiju.



![Offre de vente completée](assets/fr/12.webp)





- Jednom kada prodavac primi novac, prijaviće to i sistem eskrowa će osloboditi bitkoin, koji će biti na putu ka vašem wallet (podrazumevano putem GroupHug, Peach sistema grupisanja transakcija, koji se pokreće jednom dnevno),
- Ocenite svoje iskustvo sa prodavcem



To je to!



**Napomena za nove kupce:** prodavci zasnivaju svoje trgovine na reputaciji kupaca i obično izbegavaju ponude od kupaca bez završenih trgovina. Lakše je, u prvom slučaju, izgraditi reputaciju prihvatanjem postojećih ponuda za prodaju.




### 2.a Kako prodati bitkoine: Kreirajte prodaju



Najbrži i najlakši način za prodaju na Peach je **kreirati ponudu za prodaju**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Sa početne stranice kliknite na "Kreiraj prodajnu ponudu" (slika 32)
- Postavite svoju ponudu, obavezno unesite način plaćanja i ispravne parametre.


možete takođe :




  - napraviti nekoliko identičnih ponuda
  - aktivirajte "instant exchange" tako da prvi kupac koji naiđe može preuzeti ugovor (bez vaše potvrde) i nastaviti s plaćanjem.
  - izaberite adresu za povraćaj novca
  - finansirajte prtljažnik sa vašeg wallet Peach
- Finansirajte transakciju slanjem bitkoina na navedenu adresu (slika 34)
- Sačekajte potvrdu transakcije. Kada bude završeno, vaša ponuda će biti vidljiva na tržištu.



![Attente du paiement](assets/fr/14.webp)





- Sačekajte da kupac prihvati vašu ponudu. Razmislite o povećanju premije (%) ako želite da ubrzate stvari (slika 36)
- Kada primite zahtev za razmenu, proverite reputaciju kupca. Sami procenite da li vam profil odgovara i kliknite na "prihvati" ako jeste. (37)
- Sada je red na kupca da izvrši uplatu sa svoje banke na vašu. On će zatim proslediti uplatu vama. Ne oklevajte da kontaktirate kupca u četu.
- nakon što proverite da su sredstva primljena od strane vaše banke*, oslobodite sredstva klikom na dugme "primio sam uplatu" (slika 38). Nikada ne potvrđujte prijem uplate pre nego što proverite da je primljena na vaš račun.
- Proceni transakciju
- Bitcoins se automatski puštaju kupcu,



Tu imaš!



**Napomena o bezbednosti i saveti za uspešnu transakciju:**




 - Posmatrajte podatke o kupcu i proverite da li poreklo sredstava odgovara onom opisanom na Peach. Ako poreklo sredstava ne odgovara najavljenom, idite na Čet i otvorite argument (slika 39), i vratite sredstva na njihovo poreklo.
 - Pratite uputstva u žutoj mački.
 - Brzo odgovarajte na poruke od vašeg sagovornika
 - budite oprezni prema stavu kupca, posebno kada imate posla sa profilom sa malo iskustva
 - Ne oklevajte da koristite uslugu medijacije ako imate problem.



### 2.b Kako prodati bitkoine: prihvatite ponudu



Takođe je moguće pregledati i odabrati ponude za kupovinu. Moraćete biti posebno oprezni, jer se ovde nalazi najviše prevaranata.



![Prendre une offre d'achat](assets/fr/15.webp)





- Sa početne stranice, kliknite na "Prodaja" (slika 40)
- Koristite filtere da pregledate i odaberete najatraktivnije ponude (slika 41)



![vérification de la réputation](assets/fr/16.webp)





- pre nego što zatražite trgovinu, preporučujemo da procenite podobnost profila kupca. Možete kliknuti na ponudu, zatim na ID korisnika da biste videli njegov profil. Na primer, ponuda na slici 42 mogla bi se smatrati "rizičnom" (novi korisnik, relativno visok iznos). "Rizik" koji preuzimate prihvatanjem ove ponude je jednostavno gubljenje vremena, sve dok ne napravite grešku oslobađanja bitkoina bez primljenog novca. I dalje možete deponovati bitkoine u sef.


Ona na slici 43, s druge strane, dolazi od iskusnog trgovca (slika 44), bez sporova u svojoj istoriji. Stoga je to manje rizična ponuda.



![Match avec vendeur](assets/fr/17.webp)





- Kada je ponuda zatražena, ako kupac prihvati vaš zahtev, aplikacija će vas odvesti na sliku 34, gde možete nastaviti trgovinu kako je opisano u nastavku.




## Prednosti i nedostaci



### Peach pogodnosti





- Nije potreban KYC**: Čuva poverljivost korisnika.
- Nema pristupa bankovnim podacima**: Peach nema pristup vašim bankovnim podacima ili vašem identitetu.
- Interface intuitivan**: Lako za korišćenje za korisnike srednjeg nivoa.
- Otvoreni kod** : Izvorni kod je javan i proverljiv od strane zajednice.



### Peach nedostaci





- Ograničena Liquidnost**: Manji obim trgovanja u poređenju sa etabliranim platformama.
- Regulatorni rizik** : Aplikaciju upravlja švajcarska kompanija. Stoga podleže švajcarskim propisima, koji bi mogli evoluirati i potencijalno cenzurisati aplikaciju.



## Korisni resursi





- Francuski objašnjavajući video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Brzi vodič: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (čuvajte se prevaranata, administratori vam nikada neće prvi pisati privatnu poruku)