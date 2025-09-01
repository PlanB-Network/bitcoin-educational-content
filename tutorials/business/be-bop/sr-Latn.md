---
name: be-BOP
description: Praktični vodič za monetizaciju vašeg poslovanja sa be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** je platforma za e-trgovinu dizajnirana za preduzetnike koji žele da prodaju online i offline, u potpunoj autonomiji, dok prihvataju uplate u Bitcoin, putem bankovnog računa i u gotovini. Rešenje je takođe korisno za bilo koju vrstu organizacije koja želi da prikuplja donacije ili monetizuje svoje različite aktivnosti.



Rešenje je jednostavno, lagano i autonomno. Omogućava kreiranje online prodavnice, čak i u okruženju gde su tradicionalne finansijske usluge ograničene ili odsutne. Zaista, **be-BOP** je dizajniran da funkcioniše efikasno sa ili bez pristupa bankama, koristeći Bitcoin kao platnu infrastrukturu.



U ovom vodiču, provest ćemo vas korak po korak kroz:





- Kreirajte svoju prvu online prodavnicu sa **be-BOP**
- Personalizujte svoju izložbu i svoje proizvode
- Konfiguriši dostupne metode plaćanja
- Razumite najbolje prakse za efikasnu prodaju na mreži sa **be-BOP**



Ovaj vodič ne zahteva napredne tehničke veštine. Namenjen je programerima, kao i zanatlijama, trgovcima, zadrugama ili preduzetnicima koji žele da se upuste u digitalnu trgovinu na suveren i otporan način.



## Preduslovi za instalaciju be-BOP-a na sopstvenom serveru



Pre nego što počnete sa instalacijom be-BOP, uverite se da imate sledeću tehničku infrastrukturu. Ovi Elements su neophodni za pravilno funkcionisanje platforme:



### skladište kompatibilno sa S3



be-BOP koristi sistem skladištenja za upravljanje fajlovima (kao što su slike proizvoda). Ovo zahteva pristup S3 servisu, kao što je:





- [MinIO](https://min.io/) samostalno hostovano
- Amazon S3 (AWS)
- Scaleway Object Storage



Moraćete da konfigurišete bucket i obezbedite sledeće informacije:





- S3_BUCKET**: ime korpe
- S3_ENDPOINT_URL**: pristupni link za vašu S3 uslugu
- S3_KEY_ID** i S3_KEY_SECRET: vaši pristupni kodovi
- S3_REGION**: region vaše S3 usluge



### MongoDB baza podataka u ReplicaSet režimu



be-BOP koristi MongoDB za čuvanje podataka o prodavnici, korisnicima, proizvodima i drugih podataka.



Imate dve opcije:





- Instalirajte MongoDB lokalno sa **omogućenim ReplicaSet režimom**
- Koristite onlajn servis kao što je **MongoDB Atlas**



Trebaće vam sledeće promenljive:





- MONGODB_URL**: veza sa bazom podataka Address
- MONGODB_DB**: ime baze podataka



## Node.js okruženje



be-BOP radi sa Node.js. Uverite se da imate **Node.js** verziju 18 ili višu i da je **Corepack** omogućen (potreban za upravljanje paket menadžerima kao što je pnpm). Komanda za pokretanje je `corepack enable`



### Git LFS instaliran



Neki resursi (kao što su velike slike) se upravljaju putem Git LFS (Large File Storage). Uverite se da imate instaliran Git LFS na vašem računaru pomoću komande `git lfs install`. Kada su ovi preduslovi ispunjeni, spremni ste da pređete na sledeći korak: preuzimanje i konfigurisanje be-BOP.



**Napomena:** Tehnički vodič za implementaciju softvera dostupan je u posebnom uputstvu.



## Kreiranje Super-Admin naloga



Prvi put kada se be-BOP pokrene, kreira se nalog **Super Admin**. Ovaj nalog ima sva ovlašćenja potrebna za upravljanje funkcijama pozadinske kancelarije. Da biste kreirali nalog, pratite ove korake:





- Idite na `yourresiteweb/admin/login`
- Kreiraj super-admin nalog sa sigurnim prijavljivanjem i lozinkom



Ovaj nalog će vam omogućiti pristup svim funkcijama pozadinskog sistema. Kada ga kreirate, možete se prijaviti unosom korisničkog imena i lozinke.



![login](assets/fr/001.webp)



## Konfiguracija i bezbednost pozadinskog sistema



Pre nego što konfigurišete vašu Interface back-office vezu, potrebno je da kreirate jedinstveni Hash. Ovo pruža zaštitu protiv zlonamernih aktera koji pokušavaju da ukradu vezu ka vašem Interface adminu.



Da biste kreirali Hash, idite na `/admin/Settings`. U odeljku posvećenom bezbednosti (npr. "Admin Hash"), definišite jedinstveni string (Hash). Kada se registruje, URL za back-office će biti izmenjen (npr. `/admin-yourhash/login`) kako bi se ograničio pristup neovlašćenim osobama.



![hash-login](assets/fr/002.webp)



2.2. Aktivirajte režim održavanja (ako je potrebno)



Još uvek u /admin/Settings, (Settings > General preko Interface grafike) označite opciju "enable maintenance mode" na dnu stranice.



![maintenance-mode](assets/fr/003.webp)



Ako je potrebno, možete navesti listu autorizovanih IPv4 adresa (odvojenih zarezima) kako biste omogućili pristup prednjem uredu tokom održavanja. Zadnji ured ostaje dostupan administratorima.



![ip-bebop](assets/fr/004.webp)



## Postavljanje komunikacija



Da bi omogućili da be-BOP šalje obaveštenja (npr. za narudžbine, registracije ili sistemske poruke), potrebno je da konfigurišete bar jedan metod komunikacije. Dostupne su dve opcije: e-mail (SMTP) ili Nostr.



### SMTP konfiguracija (e-mail)



be-BOP može slati e-mailove putem SMTP servera. Trebaće vam važeći SMTP akreditivi, koje često obezbeđuje e-mail servis (npr. Mailgun, Gmail, itd.).



Evo šta treba da znate:



SMTP_HOST: SMTP server Address (npr. smtp.mailgun.org)



SMTP_PORT: port koji se koristi (često 587 ili 465)



SMTP_USER: vaše korisničko ime (obično e-mail Address)



SMTP_PASSWORD: vaša lozinka ili API ključ



SMTP_FROM: e-mail Address koji će se pojaviti kao pošiljalac




### Nostr konfiguracija



be-BOP vam omogućava slanje obaveštenja putem Nostr protokola, decentralizovane infrastrukture za razmenu poruka. Da biste to uradili, potrebno je da generate ili Supply Nostr privatni ključ (NSEC). Možete generate ovaj ključ direktno putem be-BOP-ovog Interface, u delu posvećenom Nostr-u. Kada su ovi Elements pravilno konfigurisani, be-BOP će moći automatski da šalje poruke i upozorenja vašim korisnicima.



## Kompatibilne metode plaćanja



be-BOP je kompatibilan sa nekoliko rešenja za plaćanje, omogućavajući vam da ponudite vašim kupcima veću fleksibilnost. Evo šta vam je potrebno da postavite metod plaćanja koji vam najviše odgovara.



### Bitcoin Onchain



be-BOP vam omogućava da prihvatite Bitcoin uplate direktno na Blockchain (On-Chain), jednostavno i sigurno.



**Koraci konfiguracije:**





- Idite na meni **Postavke plaćanja**
- Kliknite na **Bitcoin Nodeless** da pristupite parametrima plaćanja On-Chain.
- Popunite sledeća polja:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Savet:** Da biste dobili svoj prošireni javni ključ (Zpub), možete pogledati napredna podešavanja vašeg Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, itd.). Uverite se da vaš Wallet **nije samo za čitanje** ako nameravate da koristite istoriju transakcija.



### Lightning Network



be-BOP može takođe prihvatiti instant Bitcoin uplate zahvaljujući Lightning Network. Dve opcije konfiguracije su trenutno dostupne:



**Feniksd**



Idite na meni `Payment Settings`, kliknite na `Phoenixd`



![phoenixd](assets/fr/006.webp)



Zatim ćete morati uneti **lozinku ili token autentifikaciju** koja vas povezuje sa vašom Phoenixd instancom, backend-om koji je razvio Acinq i koji vam omogućava upravljanje Lightning plaćanjima sa vašim sopstvenim čvorom, ali bez složenosti upravljanja kanalima plaćanja.



**Swiss Bitcoin Pay**



Ako ne želite sami da upravljate Lightning čvorom, **Swiss Bitcoin Pay** je spremno rešenje koje je lako za konfiguraciju i idealno za početak prihvatanja Lightning plaćanja bez složene infrastrukture.



Koraci konfiguracije:





- U meniju "Payment Settings" kliknite na `Swiss Bitcoin Pay`
- Prijavite se na svoj Swiss Bitcoin Pay nalog (ili kreirajte jedan ako ga već nemate).
- Unesite API ključ koji je dostavio Swiss Bitcoin Pay, zatim kliknite na "Sačuvaj"



Jednom kada se postavi, be-BOP će automatski generate Lightning fakture za vaše klijente, a vi ćete primati uplate direktno na vaš švajcarski Bitcoin Pay račun. Ovo rešenje je idealno za korisnike koji žele da izbegnu tehničku složenost ličnog čvora dok prihvataju brze, niskotarifne uplate.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Pored Bitcoin, be-BOP vam takođe omogućava da prihvatite gotovinske uplate putem PayPal-a, poznatog i široko korišćenog međunarodnog rešenja.



Koraci konfiguracije:





- Idite na meni `Payment Settings`
- Kliknite na `PayPal
- U vašem Paypal nalogu (sekcija za programere), unesite `Client ID` i `Secret`
- Odaberite valutu po vašem izboru (npr. **USD**, **EUR**, **XOF**, itd.)
- Kliknite na `save



![paypal](assets/fr/008.webp)



**Napomena:** Morate imati PayPal poslovni račun da biste generate ove identifikatore. Možete ih dobiti putem [developer] portala (https://developer.paypal.com)



### SumUp



Softver sada integriše **SumUp** rešenje za plaćanje, omogućavajući vam da prihvatate plaćanja kreditnim karticama jednostavno, sigurno i efikasno. Da biste iskoristili ovu funkcionalnost, potrebna je početna konfiguracija. Ovde su koraci koje treba pratiti, numerisani za jasno i progresivno sprovođenje:





- Počnite unosom svog **API ključa**, poverljivog ključa koji vam je dostavio SumUp kada ste kreirali svoj developerski nalog. On uspostavlja sigurnu vezu između vašeg SumUp naloga i softvera.
- Popunite polje `Merchant Code` jedinstvenim kodom koji identifikuje vašu firmu unutar SumUp platforme. Ovaj kod je ključan za povezivanje transakcija sa vašim poslovanjem.
- U polju `Currency` izaberite glavnu valutu koju koristite za svoje transakcije (npr. **EUR**, **USD**, **CDF**, itd.).
- Kada su sva polja ispravno popunjena, kliknite na dugme `Save` da biste sačuvali svoja podešavanja. Sistem će tada uspostaviti vezu sa vašim SumUp nalogom i vaš softver će biti spreman za prihvatanje uplata.



![payment-sumup](assets/fr/009.webp)



Nakon ove konfiguracije, integracija sa **SumUp** biće aktivna i operativna, omogućavajući vam brzo podizanje novca i praćenje vaših transakcija direktno iz softvera.



### Stripe



be-BOP takođe nudi potpunu integraciju sa **Stripe**, jednom od najpopularnijih platformi za online plaćanje. Stripe vam omogućava da prihvatite online plaćanja putem kreditne kartice, digitalnog Wallet i nekoliko drugih metoda plaćanja. Evo kako da ga aktivirate:





- Unesite **tajni ključ** koji se nalazi na Stripe kontrolnoj tabli.
- Popunite polje **Javni ključ**, koje takođe obezbeđuje Stripe.
- Odaberite **glavnu valutu**.
- Sačuvaj konfiguraciju, zatim klikni na `Save`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Imajte na umu:** Neophodno je znati režim PDV-a koji se primenjuje na vašu delatnost (npr.: prodaja pod PDV-om u zemlji prodavca, izuzeće uz opravdanje ili prodaja po stopi PDV-a zemlje kupca) kako biste pravilno konfigurisali opcije fakturisanja u **be-BOP**.



## Konfiguracija valute



**be-BOP** nudi napredno upravljanje valutama i prilagođen je za okruženja sa više valuta i specifične računovodstvene zahteve. Da bi se osigurala doslednost u finansijskim operacijama i izveštavanju, neophodno je pravilno konfigurisati različite valute koje se koriste u sistemu. Evo koraka koje treba pratiti za ovu konfiguraciju:





- Odaberite **glavnu valutu** (`Main currency`)
- Odaberite `Sekundarnu valutu
- Definiši **referentnu valutu** (`Valuta za referencu cene`)
- Označi `Računovodstvena valuta



Kada su sve valute ispravno konfigurisane, softver obezbeđuje automatsku i tačnu konverziju transakcija u više valuta, uz održavanje rigorozne računovodstvene doslednosti.



![settings-currencies](assets/fr/011.webp)



## Konfiguracija pristupa za oporavak putem e-pošte ili Nostr



Još uvek u `/admin/settings`, putem modula **ARM**, uverite se da super-admin nalog uključuje **email Address** ili **recovery pub**, čime se olakšava procedura u slučaju da zaboravite lozinku.



![settings-users](assets/fr/012.webp)



## Postavke jezika



Softver nudi mogućnost više jezika kako bi se prilagodio međunarodnoj publici i poboljšao korisnički doživljaj. Da biste aktivirali funkcionalnost više jezika, važno je konfigurisati dostupne jezike i definisati **podrazumevani jezik**.



![settings-languages](assets/fr/13.webp)



## Interface i konfiguracija identiteta u be-BOP



**be-BOP** pruža dizajnerima sve alate potrebne za dizajniranje veb-sajta. Prvi korak je otvaranje odeljka `/Admin > Merch > Layout` u podešavanjima. Počnite sa konfigurisanje **Top Bar**, **Navbar** i **Footer**.



### Le Top Bar



Konfiguracija **Top Bar** omogućava personalizaciju vizuelnog identiteta vašeg softvera prikazivanjem ključnih informacija odmah od prve linije Interface. Ovo pojačava prepoznavanje brenda i pruža jasan kontekst za korisnike.



#### Koraci konfiguracije:





- U polje `Brand name` unesite ime vaše kompanije, organizacije ili proizvoda. Ovo ime će se pojaviti na vrhu Interface i predstavljaće vaš glavni vizuelni identitet.
- Naznačite naslov veb-sajta**: izabrani naslov treba da sažme svrhu platforme. Ovaj naslov može se pojaviti u zaglavlju ili na kartici pregledača.
- Dodajte opis veb-sajta**: ovde unesite kratak opis vaše inicijative. Ovaj opis pomaže u kontekstualizaciji alata za korisnike i može se koristiti i za SEO svrhe.



Kada se unesu ovi podaci, **Gornja Traka** će prikazati jasnu, profesionalnu i koherentnu prezentaciju vašeg rešenja.



#### Linkovi u gornjoj traci



Odjeljak `Linkovi` u Gornjoj traci omogućava vam dodavanje prečica do važnih stranica u vašoj aplikaciji ili na vanjskim sajtovima. Ovi linkovi se prikazuju direktno u Gornjoj traci, nudeći vašim korisnicima brz, strukturiran pristup.



#### Koraci konfiguracije:





- Unesite naziv linka (Tekst)**: u polje `Tekst` unesite naziv ili oznaku linka kako će se prikazivati (npr. Početna, Kontakt, Pomoć...).
- Naznačite link Address (Url)**: u polje `Url` unesite puni Address ciljne stranice (interna ili eksterna).
- Dodajte druge linkove ako je potrebno**: svaki red konfiguracije omogućava dodavanje dodatnog linka koristeći polja `Text` i `Url`.
- Sačuvaj linkove**: kada su svi linkovi uneti, kliknite na dugme "Dodaj link u gornju traku" da ih sačuvate.



Ova konfiguracija vam omogućava da ponudite jasnu, fluidnu i pristupačnu navigaciju kroz različite sekcije vaše veb stranice ili do komplementarnih resursa.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



**Navbar** sekcija vam omogućava da konfigurišete glavni navigacioni meni vašeg be-BOP-a, koji se obično nalazi sa strane ili na vrhu Interface. Ovaj meni vodi korisnike do različitih stranica i funkcija aplikacije. Konfiguracija linkova je jednostavna i intuitivna. Evo kako funkcioniše:





- Unesite naziv linka (`Text`)**: na liniji konfiguracije, počnite popunjavanjem polja `Text`. Ovo odgovara nazivu linka prikazanom u navigacionoj traci (primeri: *Dashboard*, *Users*, *Settings*...).
- Unesite link Address (`Url`)**: pored polja `Text`, pronaći ćete polje `Url`. U ovo polje unesite Address stranice na koju bi link trebalo da preusmeri. Ovo može biti interna ruta ili link ka eksternoj stranici.
- Dodajte više veza ako je potrebno**: ispod prvog reda, dostupna su nova polja `Text` i `Url` za dodavanje onoliko veza koliko je potrebno. Svaka linija predstavlja dodatnu navigacionu vezu.
- Sačuvaj linkove**: kada unesete sve Elements, kliknite na dugme `Dodaj link u navigacioni bar` da sačuvate i prikažete rezultate u navigacionom baru.



Ova konfiguracija omogućava efikasno strukturiranje pristupa različitim delovima softvera, poboljšavajući ergonomiju i korisničko iskustvo.



![navbar](assets/fr/015.webp)



### Futer



Deo **Footer** omogućava vam da prilagodite podnožje vašeg softvera, dodajući korisne informacije ili linkove. Pre nego što konfigurišete linkove, počnite aktiviranjem određene opcije:





- Omogući prikaz oznake "Powered by be-BOP"**: aktiviraj dugme `Display Powered by be-BOP` da bi prikazao ovu oznaku u podnožju.
- Unesite naziv linka (`Text`)**: popunite polje `Text`, koje odgovara tekstu linka u podnožju (primeri: *Uslovi*, *Privatnost*, *Kontakt*...).
- Navedite link Address (`Url`)**: u polje `Url` unesite Address ciljne stranice (interna ili eksterna).
- Dodajte više linkova ako je potrebno**: koristite dodatne linije da kreirate onoliko linkova koliko želite.
- Sačuvaj linkove**: kliknite na dugme "Dodaj link u podnožje" da sačuvate linkove.



![footer](assets/fr/016.webp)



### Vizuelna personalizacija



**⚠️ Ne zaboravite da postavite logotipe za svetlu i tamnu temu, kao i favicon, putem** `Admin > Merch > Pictures`.



Evo kako da prilagodite izgled i osećaj vaše stranice:



#### Idite na odeljak Slike



Meni `Admin` > `Merch` > `Pictures`.



#### Dodaj novu sliku



Kliknite na `New Picture`.



#### Izaberite lokalnu datoteku



Kliknite na `Choose Files`, zatim izaberite sliku sa vašeg Hard diska.



#### Izaberite datoteku za uvoz



Dvaput kliknite na sliku koju želite da uvezete (svetli logo, tamni logo ili favicon).



#### Imenovanje slike



Popunite polje `Name of the picture`.



#### Dodaj sliku



Kliknite `Dodaj` da biste završili uvoz.



![pictures](assets/fr/017.webp)



### Podešavanje identiteta prodavca



#### Postavke identiteta



Dostupno putem `Admin > Identity` (ili `Settings > Identity`), ovaj odeljak vam omogućava da konfigurišete administrativne i pravne informacije vaše kompanije.



#### Pravne informacije





- Naziv preduzeća**: zvanični naziv kompanije.
- Business ID**: pravni identifikator ili registarski broj (RCCM, SIRET...).



#### Posao Address





- Ulica**: poštanski Address (ulica, broj...).
- Country**: zemlja.
- Država**: pokrajina ili region.
- Grad**: city.
- Poštanski broj**: postal code.



#### Kontakt informacije





- Email**: profesionalni email Address.
- Telefon**: broj telefona kompanije.



#### Bankovni račun





- Ime vlasnika računa**: ime vlasnika računa.
- Vlasnik računa Address**: vlasnik Address.
- IBAN**: Međunarodni broj bankovnog računa.
- BIC**: SWIFT/BIC kod.



![bank-account](assets/fr/019.webp)



#### Fakturisanje





- Kliknite na `Popuni sa glavnim informacijama prodavnice` da unapred popunite podatke.
- Informacije o izdavaocu u gornjem desnom uglu**: polje za pravne/porezne informacije vidljivo na fakturama.
- Kliknite `Update` da sačuvate izmene.



**Napomena:** možete uneti dodatne informacije koje će biti prikazane na Invoice, prema vašim potrebama.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fizička prodavnica Address



Za one koji imaju fizičku prodavnicu, dodajte specifičan puni Address u `Admin > Settings > Identity` ili u posebnom odeljku. Ovo će omogućiti da se prikazuje na zvaničnim dokumentima i u podnožju ako je potrebno.



![seller-id](assets/fr/021.webp)



## Upravljanje proizvodom



### Kreiranje novog proizvoda



Idite na `Admin > Merch > Products` da biste dodali ili izmenili proizvod. Popunite sledeća polja:



#### Osnovne informacije





- Naziv proizvoda**: naziv proizvoda (npr. *BOP majica ograničeno izdanje*).
- Slug**: URL identifikator bez razmaka (npr. `tshirt-bop-edition-limitee`).
- Alias** *(opciono)*: korisno za brzo dodavanje u korpu putem posebnog polja.



![product-config](assets/fr/028.webp)



#### Cene





- Cena Iznos**: cena proizvoda (npr. `25.00`).
- Cena Valuta**: valuta (EUR, USD, BTC, itd.).
- Specijalni proizvodi**:
  - ovo je besplatan proizvod.
  - ovo je proizvod plati-koliko-želiš.



#### Opcije proizvoda





- Jedan proizvod (`standalone`)**: samo jedno dodavanje moguće po narudžbini (npr. donacija, ulaznica).
- Proizvod sa varijacijama**:
  - Nemoj proveravati `Standalone`.
  - Proveri `Proizvod ima male varijacije (nema razlike u zalihama)`.
  - Dodaj:
    - Ime** (npr. *Veličina*),
    - Vrednosti** (npr.: S, M, L, XL),
    - Razlike u ceni** ako je primenljivo (npr.: `+2 USD` za XL).



![product-details](assets/fr/029.webp)



## Upravljanje zalihama



### Napredne opcije prilikom kreiranja proizvoda (Zalihe, Dostava, Ulaznice, itd.)



#### Proizvod sa ograničenim zalihama



Ako vaš proizvod nije dostupan u neograničenim količinama, označite `Proizvod ima ograničene zalihe`. Ovo aktivira automatsko praćenje preostalih količina. Kada je ovaj okvir označen, pojavljuje se polje za označavanje **dostupnih zaliha**.



Sistem upravlja:





- Rezervisane zalihe** → proizvodi u korpama koji još nisu plaćeni
- Zalihe prodate** → proizvodi već kupljeni



**Vreme rezervacije korpe**: Kada kupac doda proizvod u svoju korpu, on je "rezervisan" na ograničeno vreme. Možete izmeniti ovo vreme u: `Admin > Config > Cart reservation` (vrednost u minutima)



#### Proizvod za isporuku?



Proveri `Proizvod ima fizičku komponentu koja će biti poslata kupcu na Address`. Ovo je korisno za sve proizvode koji se šalju fizički (knjige, majice, itd.)



#### Druge opcije





- Karta**: označite ako je proizvod karta za događaj
- Rezervacija**: proverite da li je ovo termin za rezervaciju (npr.: sesija, sastanak)



![product-options](assets/fr/030.webp)



### Postavke akcije (dno)



Ovaj odeljak određuje **gde** i **kako** se proizvod može pregledati i kupiti:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Označite samo kanale koje želite koristiti.



## Kreiranje i prilagođavanje CMS stranica i vidžeta



### Obavezne CMS stranice



Idite na `Admin > Merch > CMS`. Videćete listu postojećih stranica i možete dodati nove pomoću **Add CMS page**.



CMS stranice su važne za:





- Obavestite svoje posetioce (npr. uslovi korišćenja)
- Poštujte zakon (npr. politiku privatnosti)
- Objasnite određene karakteristike prodavnice (npr. prikupljanje IP adresa, 0% PDV)



Možete dodati druge stranice po potrebi:





- O nama / Ko smo mi
- Podržite nas / Donacije
- ČPP
- Kontakt
- itd.



**Savjet: Kliknite na svaki link ili ikonu da biste izmenili **sadržaj**, **naslov** ili **seo vidljivost** svake stranice.**



### Raspored i grafika Elements



Idite na: `Admin > Merch > Layout`. Možete prilagoditi vizuelni Elements vaše lokacije:



![product-options](assets/fr/032.webp)



#### Top Bar





- Izmeni ili izbriši linkove (npr. POČETNA, O NAMA,...)
- Navigacija između ključnih sekcija sajta



#### Navigacioni meni (glavni navigacioni meni)





- Prisutno u sivom području ispod gornje trake
- Sadrži brz pristup: `Config`, `Payment Settings`, `Transaction`, `Node Management`, `Widgets`, itd.
- Samo direktori



#### Futer





- Može se uređivati iz `Admin > Merch > Layout`
- Sadrži: kontakt informacije, korisne linkove, pravne napomene..



#### Prilagodite vizuale



Idite na: `Admin > Merch > Pictures`



Možete:





- Promenite **glavni logo**
- Izmeni ili dodaj raspored **slika**



#### Opis lokacije



Takođe se može menjati u `Slike`, omogućava vam da prikažete **rezime ili slogan** u zaglavlju ili podnožju, u zavisnosti od teme.



**Napomena:** ovo vam omogućava da prilagodite izgled vašem identitetu brenda (obrazovni, komercijalni ili zajednički).



### Integrisanje widgeta u CMS stranice



Vidžeti** obogaćuju vaše CMS stranice dinamičkim ili vizuelnim Elements.



#### Kreiranje widgeta



Idi na: `Admin > Widgets`



Primeri dostupnih widgeta:





- Izazovi**: izazovi ili misije
- Tagovi**: kategorije ili ključne reči
- Slajderi**: karuseli sa slikama
- Specifikacije**: Tabele specifikacija
- Forms**: forme (kontakt, povratne informacije, itd.)
- Odbrojavanja**: tajmeri
- Galerije**: galerije slika
- Leaderboards**: rangiranje korisnika



![widgets](assets/fr/033.webp)



#### Integracija u CMS stranice



Koristite **shortcodes** u sadržaju vaših CMS stranica:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Trenutni parametri**:





- `slug`: jedinstveni identifikator widgeta
- `display=img-1`: slika specifična za proizvod
- `width`, `height`, `fit`: dimenzije slike i stil
- autoplay=3000`: vreme u ms između dve slajda



**Prednosti**:





- Lako za umetanje (kopiraj i nalepi)
- Dinamički: svaka izmena na vidžetu se automatski odražava
- Nije potreban programer



## Upravljanje narudžbama i izveštavanje



### Praćenje narudžbine



Da biste pregledali i upravljali prošlim narudžbinama, idite na: `Admin > Transakcija > Narudžbine`



Ovde ćete pronaći **kompletnu listu narudžbina** postavljenih na vašem sajtu.



![orders](assets/fr/034.webp)



#### Vizualizacija i pretraga



Interface vam omogućava pretragu i filtriranje narudžbina prema nekoliko kriterijuma:





- broj narudžbe: broj narudžbe
- alias proizvoda: identifikator ili naziv proizvoda
- payment Mean": način plaćanja koji se koristi (kartica, kripto, itd.)
- `Email`: email kupca



Ovi filteri olakšavaju brze pretrage i ciljani menadžment.



#### Detalji svake narudžbine



Klikom na narudžbinu možete pristupiti kompletnom fajlu koji sadrži:





- Proizvodi naručeni
- Informacije o kupcu
- Isporuka Address (ako je primenljivo)
- Bilo kakve beleške povezane sa narudžbinom



#### Moguće radnje na narudžbini



Možete:





- Potvrdite narudžbinu (ako je na čekanju)
- Otkaži narudžbinu (u slučaju problema ili na zahtev kupca)
- Dodaj **oznake** (za internu organizaciju)
- Konsultujte / dodajte **internu belešku**



**Napomena:** ovaj deo je ključan za dobru logistiku i odnose sa kupcima.



### Izveštavanje i izvoz



Da pristupite statistikama prodaje i plaćanja:


administrator > Settings > Reporting



![reporting](assets/fr/035.webp)



Ovde ćete pronaći pregled vašeg poslovanja, u obliku **mesečnih i godišnjih izveštaja**.



#### Sadržaj izveštaja



Izveštaji su podeljeni u odeljke:





- Detalji narudžbine**: broj narudžbina, status (potvrđeno, otkazano, na čekanju), evolucija
- Detalji proizvoda**: prodati proizvodi, količine, popularni proizvodi
- Detalji Plaćanja**: iznosi prikupljeni, razvrstani po načinu plaćanja



#### Izvoz podataka



Svaki odeljak uključuje dugme **Izvezi CSV**, koje vam omogućava da:





- Preuzmi podatke u CSV formatu
- Otvorite ih u Excel-u, Google Sheets, itd.
- Arhiviranje za administrativnu ili računovodstvenu upotrebu
- Koristite ih za interne izveštaje



**Napomena:** idealno za praćenje performansi, računovodstvo i prezentacije.



## Konfiguracija Nostr poruka (opcionalno)



![nostr-config](assets/fr/036.webp)



Platforma podržava protokol **Nostr** za određene napredne funkcije:





- Decentralizovana obaveštenja
- Prijava bez lozinke
- Interface lagana administracija



### Generisanje i dodavanje Nostr privatnog ključa



Idi na:


admin > Upravljanje čvorovima > Nostr





- Kliknite na **Create nsec** ako ga nemate.
- Sistem može generate to automatski.
- Alternativno, možete koristiti postojeći ključ (npr. iz Damus ili Amethyst).



Sledeće:





- Kopiraj `nsec` ključ
- Dodajte to u vašu `.env.local` (ili `.env`) datoteku: ```env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Funkcije aktivirane sa Nostr



Kada se konfiguriše, dostupno je nekoliko funkcija:



**Obaveštenja putem Nostr-a**





- Šalji upozorenja za narudžbine, uplate ili sistemske događaje
- Za administratore ili korisnike



**Interface lagana administracija**





- Dostupno putem Nostr klijenta
- Omogućava brzo, mobilno-prijateljsko upravljanje



**Povezivanje bez lozinke**





- Prijava putem sigurne veze (poslato preko Nostr)
- Veća sigurnost korisnika i fluidnost



## Dizajn i prilagođavanje teme



Da biste prilagodili izgled vaše prodavnice vašoj grafičkoj povelji, idite na: `Admin > Merch > Theme`



Ovde ćete pronaći sve opcije za **kreiranje** i **konfigurisanje** prilagođene teme.



### Kreiranje teme



![theme](assets/fr/037.webp)



Kada kreirate ili modifikujete temu, možete definisati:





- Boje**: za dugmad, pozadine, tekst, linkove, itd.
- Fontovi**: izbor tipova pisma za naslove, paragrafe, menije
- Grafički stilovi**: ivice, margine, razmaci, oblici blokova



### Prilagodljivi odeljci



Svaki deo sajta može se podešavati nezavisno:





- Zaglavlje**: gornja navigaciona traka
- Body**: glavni sadržaj
- Futer**: dno stranice



**Napomena:** ova granularnost osigurava doslednost između vizuala sajta i identiteta vašeg brenda.



### Aktivacija teme



Kada je tema konfigurisana:





- Kliknite na **Sačuvaj**
- Aktiviraj to kao prodavnicinu **glavnu temu**



**Napomena:** aktivna tema je ona koja će biti vidljiva posetiocima.



## Konfigurisanje šablona e-pošte



Platforma vam omogućava da personalizujete e-poštu koja se automatski šalje korisnicima. Idite na: `Admin > Settings > Templates`



![emails-templates](assets/fr/038.webp)



### Kreiranje / uređivanje šablona



Svaki email (potvrda narudžbine, zaboravljena lozinka, itd.) ima:





- Subject**: predmet e-pošte (npr. "Vaša narudžbina je potvrđena")
- HTML Telo**: HTML sadržaj prikazan u e-pošti



**Napomena:** možete umetnuti tekst, slike, linkove, itd., po potrebi.



### Korišćenje dinamičkih varijabli



Da bi mejlovi bili dinamični, ubacite promenljive kao što su:





- `{orderNumber}}`: zamenjeno stvarnim brojem narudžbine
- `{invoiceLink}}`: link ka Invoice
- `{websiteLink}}`: URL vaše veb stranice



**Napomena:** ove oznake se automatski zamenjuju kada se pošalju.



### Napredni saveti





- Kreirajte e-poštu koja je **responzivna** za lako čitanje na mobilnim uređajima
- Dodajte **dugmad za akciju** (plati, preuzmi, prati narudžbinu)
- Testirajte svoje e-poruke tako što ćete ih poslati sebi pre objavljivanja.



## Konfigurisanje specifičnih oznaka i vidžeta



### Upravljanje oznakama



Oznake se mogu koristiti za strukturiranje i obogaćivanje vašeg sadržaja. Da biste im pristupili: `Admin > Widgets > Tag`



![tags-config](assets/fr/039.webp)



### Kreiranje oznake



Popunite sledeća polja:





- Ime Oznake**: prikazano ime oznake
- Slug**: jedinstveni_identifikator (bez razmaka ili akcenata)
- Oznaka Porodica**: grupiše oznake po kategoriji



![targsconfig](assets/fr/040.webp)



#### Dostupne porodice:





- stvaraoci`: autori ili producenti
- trgovci: prodavci ili prodajna mesta
- `Temporal`: periodi ili datumi
- događaji: povezani događaji



### Opciona polja



Ova polja se mogu koristiti za obogaćivanje oznake kao da je stranica sa sadržajem:





- Naslov
- Podnaslov
- Kratak** sadržaj
- Pun sadržaj** (na francuskom)
- CTAs** (dugmad za akciju)



### Korišćenje oznaka



Oznake mogu biti:





- Alocirano proizvodima
- Integrisano u CMS stranice sa oznakom: [Tag=slug?display=var-1]



## Konfiguracija datoteka za preuzimanje



Da biste ponudili dokumente za preuzimanje svojim kupcima: `Admin > Merch > Files`



### Dodavanje datoteke



1. Kliknite na **New file**


2. Informi:




   - Ime datoteke** (npr. *Vodič za instalaciju*)
   - Datoteka za otpremanje** (PDF, slika, Word...)



**Napomena:** kada se doda, platforma automatski generiše **stalni link**.



### Korišćenje linka



Ovaj link se zatim može umetnuti u:





- CMS** stranica (kao tekstualni link ili dugme)
- **e-mail klijent** (putem šablona)
- **list proizvoda** (npr. preuzimanje priručnika)



Idealan je za pružanje *korisničkih priručnika, tehničkih vodiča, listova proizvoda...* bez potrebe za eksternim hostingom.



## Nostr-bot



Platforma nudi naprednu integraciju sa **Nostr** protokolom, putem automatizovanog bota.



Idite na: node Management > Nostr



### Glavne karakteristike



#### Upravljanje relejima





- Dodajte ili uklonite **relaye** koje koristi bot
- Optimizujte **doseg** i **pouzdanost** poslatih poruka



#### Automatska uvodna poruka





- Aktivirajte automatsku poruku pri **prvoj interakciji korisnika**
- Idealno za:
  - Predstavljanje vaše usluge
  - Pošaljite koristan link (npr. FAQ, kontakt, narudžba)



#### Sertifikacija vašeg `npub





- Dodajte **logo** i **javno ime**
- Veza ka **verifikovanoj veb domeni**
- Povećava kredibilitet i prepoznatljivost vašeg Nostr identiteta



### Nostr-bot slučajevi upotrebe





- Slanje **potvrda narudžbine** vama
- Automatski odgovor na **događaje (npr. nova narudžbina)**
- Kreiranje **decentralizovane interakcije sa korisnicima**



## Preopterećenje prevodnih oznaka



be-BOP je višejezičan (FR, EN, ES...), ali možete prilagoditi prevode svojim potrebama.



Da biste to uradili, idite na: `Settings > Language`



### Učitavanje i uređivanje



Datoteke za prevod su u JSON formatu. Možete:





- Preuzmi** jezičke datoteke
- Izmeni** postojeće tekstove
- Dodajte** svoje prevode



Link ka originalnim fajlovima:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Primer:** zamenite `Add to cart` sa `Dodaj u korpu` ili `Kupi`.



## Tim za saradnju & Point of Sale (POS)



### Upravljanje korisnicima i pravima pristupa



#### Kreiranje uloga



Idite na: `Admin > Settings > ARM`



Kliknite na **Create a role** da kreirate ulogu (npr. `Super Admin`, `POS`, `Ticket checker`).



Svaka uloga sadrži:





- write access**: write access
- read access**: read access
- zabranjen pristup**: zabranjeni odeljci



#### Kreiranje korisnika



U istom meniju `Admin > Settings > ARM`, dodajte korisnika sa:





- prijava
- alias
- oporavak e-pošte
- (opcionalno) `recovery npub` za povezivanje putem Nostr



Dodeli prethodno definisanu ulogu.



![pos-users](assets/fr/045.webp)



Korisnici sa **samo za čitanje** će videti menije u *kurzivu* i neće moći da menjaju sadržaj.



## Konfiguracija prodajnog mesta (POS)



### Dodeljivanje POS uloge



Da biste korisniku dali pristup POS-u, dodelite ulogu `Point of Sale (POS)` u: `Admin > Config > ARM`



Može se povezati putem sigurne URL adrese: `/pos` ili `/pos/touch`



### POS-specifične funkcije



Be-BOP nudi Interface posvećen fizičkoj prodaji (prodavnica, događaj, itd.).



#### Brzo dodavanje putem alias-a



U `/cart`, polje vam omogućava da dodate proizvod:





- Skeniranjem **bar koda** (ISBN, EAN13)
- Unošenjem **alias-a proizvoda** ručno



**Napomena:** proizvod se automatski dodaje u korpu.



#### Sredstva plaćanja



POS podržava:





- Vrste
- Kreditna kartica
- Lightning Network (kripto)
- Drugi prema konfiguraciji



Dve napredne opcije su dostupne:





- Izuzimanje od PDV-a**: primenljivo uz opravdanje (NVO, stranci...)
- Poklon popust**: izuzetan popust uz obavezan komentar



#### Prikaz na strani klijenta



URL `/pos/session` je namenjen za **sekundarni ekran** (HDMI, tablet...):



Poster:





- Proizvodi u toku
- Ukupan iznos
- Metod plaćanja
- Popusti primenjeni



**Napomena:** kupac prati narudžbinu uživo, dok je prodavac beleži na `/pos`.



### rezime POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Hvala što ste pažljivo pratili ovaj vodič.