---
name: Pravljenje novih rešenja sa Elements i Liquid mrežom
goal: Naučite kako koristiti i praviti aplikacije na Elements blokčejn platformi otvorenog koda i njene ključne funkcije
objectives: 

  - Razumevanje osnovnih pojmova Elements blokčejn platforme i Liquid bočnog lanca (eng. sidechain).
  - Naučite kako postaviti i pokrenuti Elements čvorove kao samostalne konfiguracije i kao konfiguracije bočnog lanca.
  - Steknite praktično iskustvo sa potpisivanjem blokova od strane federacije i sa Federated 2-Way Peg-om.
  - Postavite i upravljajte sigurnim, efikasnim blokčejn okruženjima za praktične primene u stvarnom svetu.

---

# Pravljenje rešenja na Liquid-u i Elements-u


Otkrijte napredne funkcije i mogućnosti Liquid-a i Elements-a, i naučite kako efikasno koristiti ove alate za unapređenje vaših razvojnih projekata. Ova obuka pruža potpunu teorijsku i praktičnu osnovu, omogućavajući vam da savladate funkcije kao što su poverljive transakcije (eng. Confidential Transactions), emitovani aseti (eng. Issued Assets) i potpisivanje blokova od strane federacije (eng. Federated block signing).


Liquid, baziran na Elements platformi, dizajniran je za poboljšanje privatnosti, skalabilnosti i funkcionalnosti za finansijska i tehnička rešenja. U ovom kursu, steći ćete praktično iskustvo sa izdavanjem i upravljanjem sredstvima, Federated 2-Way Peg, i korišćenjem alata kao što su elementsd i elements-cli, osnažujući vas da kreirate inovativna rešenja prilagođena vašim potrebama.


Ovaj kurs je prilagođen programerima svih nivoa iskustva. Početnici i korisnici srednjeg nivoa će pronaći pristupačna objašnjenja i praktične primere, dok napredni korisnici mogu detaljnije istražiti tehničke detalje i manje poznate funkcije Liquid-a i Elements-a.


Pridružite nam se kako biste unapredili svoje veštine, otključali puni potencijal Liquid-a i Elements-a, i razvijali alate od značaja za budućnost inovacija zasnovanih na Liquid mreži.

+++

# Uvod


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## Pregled kursa


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


Dobrodošli na kurs SID202!


Cilj *Elements Akademije* je da predstavi i objasni ključne koncepte *Elements-a*, platforme otvorenog koda na kojoj je izgrađen Liquid Sidechain. Do kraja ovog kursa, trebalo bi da imate solidno razumevanje glavnih karakteristika Elements-a, kao što su poverljive transakcije i emitovana sredstva, kao i procesa povezanih sa radom Elements Core-a. Svaki deo kursa uključuje lekcije sa objašnjavajućim tekstovima i video zapisima, nakon čega sledi kviz.


Ova obuka ima za cilj da vas nauči kako da koristite i razvijate sa open-source platformom Elements, sa fokusom na Liquid mrežu. Otkrićete kako ove tehnologije mogu poboljšati privatnost, skalabilnost i funkcionalnost vaših razvojnih projekata. Bilo da ste početnik ili iskusni programer, ovaj kurs će vam pružiti snažnu osnovu za savladavanje osnovnih koncepata Elements-a i Liquid-a, kao i njihovih praktičnih primena.


**Sekcija 1: Uvod**

Počećemo sa sveobuhvatnim pregledom Elements koncepata. Naučićete kako je ova platforma dizajnirana da pruži modularnu i fleksibilnu osnovu za kreiranje bočnih lanaca kao što je Liquid. Cilj je razumeti strukturu Elements-a pre nego što se upustimo u njegove praktične primene.


**Sekcija 2: Elements**

Ovaj deo će se fokusirati na to kako Elements funkcioniše. Naučićete kako da konfigurišete Elements čvor, koristite ga u samostalnom režimu ili kao bočni lanac (sidechain).


**Sekcija 3: Korišćenje Elements-a – Praktične upotrebe**

Kada se savladaju teorijske osnove, pokrićemo praktične primene Elements-a. Naučićete kako da izvršite poverljive transakcije, izdate sredstva i upravljate ponovnim izdavanjem sredstava.


**Sekcija 4: Elements federacija**

Ovde ćemo istražiti napredne mehanizme, uključujući federisano potpisivanje blokova, korišćenje Elements-a kao bočnog lanca, i kreiranje nezavisnih blokčejnova. Ovaj deo će vam pomoći da razumete kako da osigurate bezbednost, integritet i interoperabilnost blokčejnova zasnovanih na Elements-u.


Spremni da istražite potencijal Elements-a i Liquid Sidechain-a? Hajde da počnemo!



## Pregled Elements-a


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements je platforma otvorenog koda za blokčejn koja podržava rad sa bočnim lancima, i koja omogućava pristup moćnim funkcijama razvijenim od strane članova zajednice, kao što su poverljive transakcije i izdavanje digitalnih resursa.


Elements je, u svojoj suštini, protokol koji omogućava postizanje konsenzusa oko istorije transakcija i pravila koja upravljaju prenosom i kreiranjem digitalnih sredstava sačuvanih u distribuiranom blokčejn digitalnom dnevniku (eng. Ledger).


Više informacija o Elements-u možete lako pronaći na vebsajtu Elements projekta (https://elementsproject.org/), zvaničnom Liquid blogu (https://blog.Liquid.net/) i portalu za programere (https://Liquid.net/devs).


### Elements


Pokrenut 2015. godine, Elements smanjuje troškove interne izrade i istraživanja i koristi najnoviju blokčejn tehnologiju, otvarajući mogućnosti za brojne nove primene. Blokčejn zasnovan na Elements-u može raditi ili kao samostalni blokčejn ili biti povezan s drugim i raditi kao bočni lanac blokova. Pokretanje Elements-a kao Sidechain-a omogućava da se sredstva verifikovano prenose između različitih blokčejnova.


Zasnovano na Bitcoin kodnoj bazi i proširen dodatnim funkcionalnostima, Elements omogućava programerima koji su upoznati sa bitcoind API-jem da brzo i ekonomično kreiraju funkcionalne blokčejnove i rade na projektima koji služe kao dokaz izvodljivosti ideje (eng. proof-of-concepts projects). Budući da je izgrađen na kodnoj bazi Bitcoin-a, Elements takođe može služiti kao testna platforma za promene u samom Bitcoin protokolu.


Neke od glavnih karakteristika Elements-a navedene su u nastavku.


#### Poverljive transakcije


Podrazumevano, sve adrese unutar Elements-a su skrivene koristeći poverljive transakcije. Skrivanje je proces u kojem se iznos i vrsta imovine koja se prenosi kriptografski sakrivaju od svih, osim učesnika i onih kojima odluče da otkriju ključ za skrivanje (eng. blinding key).


#### Izdavanje digitalnih resursa


Izdavanje digitalnih resursa na Elements platformi omogućava izdavanje i prenos više tipova sredstava između učesnika mreže. Izdata imovina takođe koristi poverljive transakcije i može biti ponovo izdata ili uništena od strane bilo koga ko drži relevantni token za ponovno izdavanje. (eng. reissuance token).


#### Federated 2-Way Peg


Elements je platforma opšte blokčejn namene koja se takođe može "vezati" za postojeći blokčejn (kao što je Bitcoin) kako bi se omogućio dvosmerni prenos sredstava sa jednog lanca na drugi. Implementacija Elements-a kao Sidechain-a omogućava vam da zaobiđete neka od inherentnih svojstava glavnog lanca, dok zadržavate dobar stepen sigurnosti koju pružaju sredstva osigurana na glavnom lancu.


#### Potpisivanje blokova


Elements koristi jaku federaciju (eng. Strong Federation) potpisnika, nazvanih Blok potpisnici, koji potpisuju i kreiraju blokove na pouzdan i pravovremen način. Ovo uklanja kašnjenje transakcija koje postoji u PoW procesu rudarenja, koji je podložan velikim varijacijama u vremenu potvrđivanja bloka zbog svoje nasumične Poisson distribucije. Federisani proces potpisivanja blokova postiže pouzdano kreiranje blokova bez uvođenja potrebe za poverenjem treće strane ili računarskim `algoritmom` zasnovanim na rudarenju.


Elements dodaje sve ove funkcije na Bitcoin Core kodnu bazu, proširujući mogućnosti glavnog protokola i omogućavajući nove poslovne slučajeve kada se implementira kao Sidechain ili kao samostalno blokčejn rešenje.


# Elements


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Kako Elements Radi


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements pruža tehničko rešenje za probleme sa kojima se korisnici blokčejna suočavaju svakodnevno; čekanje na potrvđivanje transakcija, nedostatak privatnosti i rizik po zamenjivost (eng. fungability).


Elements prevazilazi ove probleme kroz korišćenje federacije za potpisivanje blokova i korišćenjem poverljivih transakcija.


Za razliku od Bitcoin mreže, proces potpisivanja blokova unutar Elements-a ne oslanja se na višestranačke potpise sa dinamičkim članstvom (eng. Dynamic Membership Multiparty Signatures - DMMS) i Proof of Work (PoW). Umesto toga, Elements koristi Strong Federation potpisnika, nazvanih Blok Potpisnici, koji mogu potpisivati i kreirati blokove na pouzdan i pravovremen način. Ovo uklanja potrebu za čekanjem potvrde transakcija kao što je u PoW procesu rudarenja, koji je podložan velikoj varijabilnosti dužine čekanja na potvrdu bloka zbog svoje slučajne Poisson distribucije. Federisani proces potpisivanja blokova postiže pouzdano kreiranje blokova bez uvođenja potrebe za poverenjem treće strane.


Elements može raditi kao Sidechain za drugi blokčejn, kao što je Bitcoin, ili kao samostalni blokčejn bez zavisnosti od drugih mreža.


Kada se koristi kao Sidechain, Strong Federation takođe sadrži članove koji omogućavaju siguran i kontrolisan prenos sredstava između glavnog lanca i Elements Sidechain-a. Kontrolisani prenos sredstava naziva se Federated 2-Way Peg, a članovi koji obavljaju ulogu prenosa sredstava nazivaju se Čuvarima (eng. Watchmen).


Procesi uključeni u vođenje Elements mreže kao i uloge učesnika u mreži su važni za razumevanje kako Elements funkcioniše.


Bilo da je implementiran kao Sidechain ili samostalni blokčejn, Elements koristi Strong Federaciju potpisnika blokova za potvrđivanje blokova.


### Strong federations


Elements koristi konsenzus model koji je prvi predložio Blockstream, nazvan Strong Federations. Strong Federation ne koristi Proof of Work (PoW) i umesto toga se oslanja na kolektivne akcije grupe međusobno-nepoverljivih učesnika, nazvanih funkcionerima (eng.Functionaries).


Uloge koje Funkcioner može ispuniti unutar Strong Federation su: potpisnici blokova i čuvari. Potpisnici blokova su potrebni ako pokrećete Elements bilo kao Sidechain ili u samostalnom blokčejn režimu, dok su čuvari potrebni samo u Sidechain konfiguraciji.


Radnje koje član Strong Federation može da izvrši podeljene su između dve različite uloge kako bi se poboljšala sigurnost i ograničila šteta koju napadač može da prouzrokuje.


Kombinovanjem uloga ovih učesnika, Elements omogućava brzo kreiranje blokova (bržu i konačnu potvrdu transakcija) i sigurna, prenosiva sredstva (povezana sredstva koja se direktno mogu povezati sa drugim blokčejnom).


Možete pročitati dokument o Strong Federation konsenzusu ovde: https://blockstream.com/strong-federations.pdf


### Potpisnici blokova


Blokčejn poput Bitcoin-a se produžava kada bilo ko ko je deo dinamičke grupe potpisnika blokova pokaže dokaz potrošenog rada. Dinamička priroda ove grupe uvodi problem čekanja svojstvene takvim sistemima.


Korišćenjem fiksnog skupa potpisnika, federativni model zamenjuje dinamički skup sa poznatim setom potpisnika i višepotpisnim sistemom. Smanjenje broja učesnika potrebnih za produženje blokčejna povećava brzinu i skalabilnost sistema, dok validacija od strane svih strana osigurava integritet istorije transakcija.


Potpisivanje blokova od strane federacije se sastoji od nekoliko faza:



- Korak 1 - Blok potpisnici predlažu kandidatske blokove naizmenično svim ostalim učesnicima.



- Korak 2 - Svaki potpisnik bloka signalizira svoju nameru unapred obavezujući se da će potpisati dati blok koji je kandidat.



- Korak 3 - Ako je zadati prag broja potvrda (eng. pre-commitment) ispunjen, svaki blok potpisnik potpisuje blok.



- Korak 4 - Ako je prag potpisa (koji može biti različit od onog u koraku 3) ispunjen, blok se prihvata i šalje mreži. Strong Federation je postigla konsenzus o najnovijem bloku transakcija.



- Korak 5 - Sledeći blok zatim predlaže sledeći potpisnik po round-robin mehanizmu i proces se ponavlja.


Zato što generisanje blokova kod Strong Federation nije probabilističko i zasniva se na fiksnom skupu potpisnika, nikada neće biti podložno reorganizacijama sa više blokova. Ovo omogućava značajno smanjenje vremena čekanja povezanog sa potvrđivanjem transakcija. Takođe uklanja podsticaj za rudarenje radi profita (tj. nagrade za blokove) i zamenjuje ga podsticajem za produktivno učešće u mreži gde svi učesnici imaju isti zajednički cilj; osiguranje da mreža nastavi da funkcioniše na način koji je koristan za sve. Ovo se postiže bez uvođenja jedinstvene tačke kvara ili većih zahteva za poverenjem.


### Elements kao Sidechain - Watchmen i Federated 2-Way Peg


Kada se pokreće kao Sidechain, neki članovi Strong Federation imaju dodatnu ulogu da ispune, ulogu Watchmen-a. Watchmen-i su odgovorni za transfer sredstava u i iz Elements Sidechain-a, procesi poznati kao `Peg-In` i `Peg-Out`.


Da bi Sidechain radio na pouzdan način, mora omogućiti učesnicima da verifikuju da je ponuda sredstava kontrolisana i proverljiva. Elements Sidechain koristi dvosmerni federativni peg koji omogućava dvosmeran transfera sredstava u i iz Elements blokčejna. Ovo zadovoljava zahteve dokazivog izdavanja sredstava ili tokena i transfera između lanaca blokova.


Funkcija Federated 2-Way Peg-a omogućava da digitalna sredstva na jednom blokčejnu bude interoperabilna sa drugim blokčejnovima i da predstavlja drugi izvorni resurs blokčejna. Povezivanjem vašeg blokčejna sa drugim, možete proširiti mogućnosti glavnog i prevazići neka od njegovih inherentnih ograničenja.


Na visokom nivou, transferi u Sidechain-u se dešavaju kada neko pošalje sredstva na glavnom blokčejnu na adresu kontrolisanu od strane višepotpisnog novčanika Watchmen-a. Ovo efektivno zamrzava sredstva na glavnom blokčejnu. Watchmen zatim validiraju transakciju i oslobađaju istu količinu povezanog sredstva unutar Sidechain-a. Oslobođena sredstva se šalju na Sidechain novčanik koji može dokazati pravo na originalna sredstva na glavnom blokčejnu. Ovaj proces efektivno premešta sredstva sa matičnog lanca na Sidechain.


Kako bi prebacila sredstva nazad na glavni lanac, korisnik pravi specijalnu peg-out transakciju na Sidechain-u. Ovu transakciju proveravaju Watchmen-i koji zatim potpisuju transakciju trošenja sa više-potpisnog novčanika koji kontrolišu na glavnom blokčejnu. Određeni broj učesnika u federaciji mora potpisati pre nego što transakcija na glavnom blokčejnu postane važeća. Kada Watchmen-i pošalju sredstvo nazad na glavni blokčejn, oni takođe uništavaju odgovarajući iznos na Sidechain-u, efektivno prenoseći sredstva između blokčejnova.


## Postavljanje i pokretanje Elements platforme


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Kako je Elements zasnovan na kodnoj bazi Bitcoin-a, komponente koje čine funkcionalnu mrežu su veoma slične.


Sam softver Elements čvora se zove `elementsd` i radi kao daemon na korisnikovom računaru. daemon (ili servis u Windows-u) je program koji radi kao pozadinski servis bez potrebe za direktnom kontrolom prijavljenog korisnika.


Napomena: Kroz ovaj dokument, uvek ćemo se pozivati na elementsd kao na daemon verziju, ali sve bi moglo biti urađeno sa Elements-qt, pod uslovom da je opcija servera omogućena.


Elements daemon se povezuje sa drugim čvorovima na mreži kako bi mogao razmenjivati transakcije i podatke o blokovima, validirajući i proširujući svoju lokalnu kopiju mrežnog blokčejna.


Elements softver takođe se sastoji od klijentskog programa nazvanog `elements-cli` koji vam omogućava da šaljete Remote Procedure Call (RPC) komande ka elementsd sa komandne linije. Ovo se može koristiti, na primer, za upit bilansa novčanika, pregled podataka o transakcijama ili blokovima ili emitovanje transakcije. Ova postavka bi trebalo da bude poznata svima koji su koristili Bitcoin ekvivalente; bitcoind i bitcoin-cli.


Čvor Elements može se konfigurisati prosleđivanjem parametara prilikom pokretanja ili putem konfiguracione datoteke, što omogućava pokretanje više instanci na istom računaru. Ovo je korisno za testiranje i razvojne svrhe jer možete postaviti sopstvenu lokalnu mrežu na jednom računaru, pri čemu svaki Elements čvor ima svoju kopiju blokčejn podataka, upravlja sopstvenim skupom nepotvrđenih validnih transakcija i sluša RPC zahteve na različitim portovima.


### Repozitorijum Elements koda i zajednica


Elements je projekat otvorenog koda i njegov izvorni kod se može pronaći u Elements GitHub repozitorijumu na https://github.com/ElementsProject/Elements. Repozitorijum sadrži izvorni kod za elementsd i elements-cli programe zajedno sa alatima za instalaciju i izgradnju, skup testova i neku instruktivnu dokumentaciju.


Da bi upotpunio repozitorijum koda, tu je i vebsajt https://elementsproject.org, resurs fokusiran na zajednicu koji sadrži objašnjenja šta je Elements, kako funkcioniše i sveobuhvatan odeljak sa tutorijalima. Tutorijal se fokusira na učenje o Elements-u prateći primere komandne linije i pokazuje vam kako da izgradite jednostavne desktop i veb aplikacije na njemu. Sajt takođe navodi popularne Elements forume za diskusiju unutar zajednice i sam je hostovan na GitHub-u, omogućavajući doprinos zajednice sadržaju sajta.


Da biste pokrenuli Elements na vašem računaru, prvo ćete morati klonirati (preuzeti kopiju) izvornog koda, instalirati sve zavisnosti koje kod ima i na kraju izbilodovati izvršne datoteke daemona i klijenta. Softver Elements je tada spreman za konfiguraciju i pokretanje.


## Konfigurisanje čvorova i umrežavanje


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


Postavke konfiguracije mogu se proslediti Elements čvoru prilikom pokretanja kako bi se promenio način na koji radi, validira podatke, povezuje se sa drugim čvorovima i inicijalizuje svoje blokčejn podatke.


Postavke se ili učitavaju iz određenog `Elements.conf` fajla ili se prosleđuju kao parametri putem komandne linije.


Neke stvari se mogu promeniti korišćenjem ovih parametara:



- Naziv podrazumevanog asseta korišćen u samostalnim blokčejn implementacijama.
- Broj početne imovine koja je stvorena.
- Imovina koja će se koristiti prilikom plaćanja transakcijskih naknada na mreži.
- Lokacija skladištenja blokčejn datoteka.
- RPC akreditivi korišćeni za povezivanje sa Bitcoin čvorom.
- `n od m` prag koji treba ispuniti i važeći javni ključevi koji mogu potpisivati blokove.
- Skripta koja treba biti zadovoljena kako bi se izvršio prenos sredstava u i iz Sidechain-a.
- Da li se povezati na Bitcoin čvor kao Sidechain ili ne.


Mnogi od njih čine deo pravila konsenzusa mreže, tako da je važno da se primenjuju na svim čvorovima prilikom pokretanja. Neki se mogu promeniti nakon što je lanac inicijalizovan, ali neki moraju biti fiksirani nakon što su korišćeni za inicijalizaciju lanca.


Upotreba parametara biće obuhvaćena kasnije u kursu, kako budu relevantni za svaku sekciju.


### Osnovne operacije korišćenjem komandne linije


Ovaj kurs će prikazati primere kod kojih se koristi program `elements-cli` za upućivanje RPC poziva ka jednom ili više Elements čvorova. Ovo se radi iz terminal sesije i da bi komande bile kraće koristiće se `alias`. Prema ovoj konvenciji kada vidite nešto poput sledećih komandi:


```bash
e1-dae

e1-cli getnewaddress
```


`e1-dae` i `e1-CLI` su zapravo tipografske skraćenice koje koriste funkciju `alias` terminala. `e1-dae` i `e1-CLI` će zapravo biti zamenjeni kada se komanda izvrši i komanda koja će se pokrenuti biće slična ovoj:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


Ono što vidimo iznad je poziv za pokretanje Elements daemona i poziv za elements-cli program smeštene u direktorijumu `$HOME/Elements/src` i vrednost za `datadir` parametar. Parametar `datadir` nam omogućava da kažemo daemon i klijentskoj instanci gde da pronađu njihove konfiguracione fajlove i, u slučaju daemon, gde da sačuvaju svoju kopiju blokčejna. Kako dele konfiguracioni fajl, klijent će biti u mogućnosti da izvrši RPC pozive ka daemon-u.


Pokretanjem gornje komande ponovo, ali sa drugačijom vrednošću `datadir`, možemo pokrenuti više od jedne instance Elements-a, svaka sa svojom zasebnom kopijom blokčejna i konfiguracionim podešavanjima. Po ovom konvencionalnom pravilu koristićemo alias `e2-dae` i `e2-CLI` u toku kursa da se referišemo na drugačiji datadir direktorijum od e1. Tako bi gornji primer za našu drugu `e2` instancu bio:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


Ovo će nam omogućiti da izvršimo sve vrste operacija kao što su transakcije sredstava između čvorova, izdavanje sredstava i proveru upotrebe zaslepljivanja u poverljivim transakcijama između različitih čvorova na istoj mreži.


# Praktična primena korišćenje Elements-a


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Poverljive transakcije


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


U ovom odeljku ćete naučiti kako da koristite funkcionalnost poverljivih transakcija na Elements platformi.

Sve adrese u Elements-u su, po defaultu, sakrivene koristeći poverljive transakcije, što čini da količina i tip prenetih sredstava budu vidljivi samo učesnicima u transakciji (i onima kojima odluče da otkriju ključ za maskiranje), dok se i dalje kriptografski garantuje da se ne može potrošiti više novčića nego što je dostupno.


### Poverljive adrese i poverljive transakcije


Podrazumevano, kada kreirate novu adresu u Elements-u koristeći komandu `getnewaddress`, ona se kreira kao poverljiva adresa.


Kako bismo demonstrirali poverljive transakcije, demonstriraćemp da e2 sam sebi pošalje neka sredstva, a zatim ćemo pokušati da pregledamo transakciju sa e1. Ovo će pokazati poverljivu prirodu transakcija u Elements-u.


Svaki nova adresa generisna od strane Elements čvora je poverljiva po defaultu. Možemo to demonstrirati tako što ćemo koristeći e2 da generišemo novu adresu.


```
e2-cli getnewaddress
```


Imajte na umu da adrese počinje sa e1. Ovo je identifikuje kao poverljivu adresu. Detaljnije ispitivanje adrese pomoću komande getaddressinfo prikazuje više detalja o adresi.


```
e2-cli getaddressinfo <address>
```


Možete videti da postoji poverljivi_ključ (eng. confidential_key) parametar koje nam govori da je to poverljiva adresa.


Confidential_key je javni ključ za maskiranje, koji se dodaje samoj poverljivoj adresi. Ovo je razlog zašto je poverljiva adresa tako duga.


Takođe ima pridruženu neprikrivenu adresu. Ako želite da koristite redovne, neprikrivene transakcije unutar Elements-a, sredstva treba poslati na ovu adresu umesto na onu sa prefiksom lq1.


Sada možemo omogućiti da e2 pošalje neka sredstva na adresu koja je generisana. Kasnije čemo pokazati da e1, pošto nije jedna od strana u transakciji, neće moći da vidi detalje ove transakcije.


```
e2-cli sendtoaddress <address>
```


Zabeleži transaction ID. Potvrdi transakciju.


```
e2-cli -generate 101
```


Gledajući transakciju gde je e2 poslao neka sredstva samom sebi iz perspektive samog e2.


```
e2-cli gettransaction <txid>
```


Pomicanjem naviše kroz detalje transakcije, možete videti da e2 može pregledati poslate i primljene iznose, kao i imovinu koja je transaktovana. Takođe možete videti amountblinder i assetblinder parametre, koja se koriste za sakrivanje detalja od drugih čvorova koji nisu uključeni u transakciju.


Da bismo proverili detalje iste transakcije koristeći e1, prvo moramo dobiti detalje transakcije u neobrađenom obliku.


```
e1-cli getrawtransaction <txid>
```


To vraća sirove detalje transakcije. Ako pogledate unutar vout sekcije, možete videti da postoje tri instance. Prve dve instance su iznosi primanja i kusura, a treća je naknada za transakciju. Od ova tri iznosa, naknada je jedina kojoj možete videti vrednost, jer je sama naknada uvek ne sakrivena unutar Elements-a.


### Ključevi za maskiranje (eng. Blinding Keys)


Ono što prva dva odeljka vout prikazuju su "zamaskirani opsezi" iznosa vrednosti i obavezujući podaci koji služe kao dokaz stvarnog iznosa i tipa prenete imovine.


Čak i ako bismo uvezli privatni ključ e2 u novčanik e1, i dalje ne bi mogli videti iznose i tip transakcije imovine jer još uvek nemamo saznanja o ključu za zaslepljivanje koji koristi e2. Dokazaćemo ovo uvozom privatnog ključa koji koristi e2-ov novčanik u e1-ov. Prvo moramo izvesti ključ iz e2.


```
e2-cli dumpprivkey <address>
```


Zatim ga uvesti u e1.


```
e1-cli importprivkey <privkey>
```


Sada možemo dokazati da e1 i dalje ne može videti vrednosti.


```
e1-cli gettransaction <txid>
```


Zaista, prikazuje 0 kao iznos tx kada je zapravo bio 1.


Da bismo mogli videti stvarnu, nezamaskiranu vrednost, potrebna nam je ključ za maskiranje. Da bismo to uradili, prvo izvozimo maskirajuću ključ iz e2.


```
e2-cli dumpblindingkey <address>
```


Zatim ga uvezi u e1.


```
e1-cli importblindingkey <address> <blinding key>
```


Sada kada dobijemo detalje transakcije od e1.


```
e1-cli gettransaction <txid>
```


Pokazuje da sa uvezenim ključem za maskiranje, sada možemo videti stvarnu vrednost 1 unutar transakcije.


U ovom odeljku smo videli da upotreba ključa za maskiranje skriva iznos i tip sredstava u transakciji, i da uvozom pravog maskirajućeg ključa možemo otkriti te vrednosti. U praktičnoj upotrebi, ključ za zaslepljivanje može, na primer, biti dat revizoru, ukoliko postoji potreba da se verifikuju iznosi i tipovi sredstava koje poseduje neka strana. Funkcija poverljivih transakcija unutar Elements-a takođe omogućava izvođenje "dokaza opsega". Dokazi opsega mogu dokazati da je iznos sredstva unutar datog opsega, bez potrebe da se otkrije stvarni iznos.


Takođe smo videli da su poverljive transakije opcioni, ali su podrazumevano omogućene kada se generišu nove adrese.


To je to za ovu lekciju; srećno na kvizu i vidimo se u sledećoj!


## Emitovani aseti (eng. Issued Assets)


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


U ovom odeljku ćete naučiti kako koristiti funkciju Issued Assets unutar Elements.


Issued Assets omogućava izdavanje i prenos više vrsta sredstava između učesnika Elements mreže. Bilo koji čvor na mreži može izdati sopstvena sredstva. Izdavanja mogu predstavljati zamenjivo vlasništvo bilo kog sredstva uključujući vaučere, kupone, valute, depozite, obveznice, akcije, itd. Issued Assets otvaraju vrata za berzi bez potrebe za poverenjem u centralni entitet, opcija i drugih naprednih pametnih ugovora koja uključuju samostalni Issued Assets.


Izdati resurs takođe ima koristi i od poverljivih transakcija i može ga ponovo izdati bilo ko ko drži povezani token.


Prvi korak je da ćemo trebati imati pristup dva Elements čvora, koje ćemo nazvati e1 i e2. Čvorovima su resetovani blokčejnovi i default asset je podeljen između njih.


Dva čvora su na istoj lokalnoj mreži i povezana su međusobno, te stoga dele iste transakcije u svojim Mempool-ovima i identične blokčejnove. Iako rade na istoj mašini, važno je napomenuti da ne dele iste stvarne blokčejn fajlove. Svaki čvor upravlja svojom lokalnom kopijom blokčejna, koja sadrži istu istoriju transakcija jer su u konsenzusu i pridržavaju se istih pravila protokola kao i drugi.


Hajde da počnemo proverom pogleda svakog čvora na postojeća izdata sredstava na mreži.


Ovo se radi pomoću komande listissuances.


```
e1-cli listissuances

e2-cli listissuances
```


Kao što možete videti, oba čvora prikazuju istu istoriju izdavanja. Oba prikazuju jedan aset, inicijalno izdavanje od 21 milion Bitcoin-a koje je kreirano inicijalizacijom glavnog lanca. Možete videti heksadecimalni ID aseta u rezultatima pokretanjem gore navedene komande, kao i oznaku dodeljenu asetu, koja je 'Bitcoin'.


Važno je napomenuti da defaultni asset uvek dobija oznaku kada se lanac inicijalizuje. Kada izdajete sopstvene asete, možete sami postaviti oznake za njih, što ćemo uskoro i uraditi. Pre nego što to možemo da uradimo, potrebno je da izdamo sopstveni aset.


Izdavanje novog sredstva će obaviti e1. Ovo se radi pomoću komande issueasset.


```
e1-cli issueasset 100 1 false
```


`issueasset` prihvata 3 parametra.


Količina novog sredstva za izdavanje, koristili smo 100. Količina tokena za kreiranje (tokeni se koriste za ponovno izdavanje količina neke imovine), od kojih smo odabrali 1. Poslednji parametar govori Elements-u da li da kreira izdavanje sredstva kao zamaskirane (eng. blinded) ili nezamaskirane (eng. unblinded). Koristićemo unblinded jer želimo da vidimo izdate količine iz e2 čvora vrlo brzo, pa ćemo uneti false.


Pokretanje komande vraća podatke o izdavanju. Ovo uključuje transaction ID, od kojeg možete uzeti kopiju za kasniju upotrebu, jedinstvenu heksadecimalnu vrednost sredstva i jedinstvenu heksadecimalnu vrednost tokena sredstva.


Generišite blok za potvrdu transakcije izdavanja.


```
e1-cli -generate 1
```


Pokreni komandu `listissuances` unutar e1 ponovo.


```
e1-cli listissuances
```


To nam pokazuje da je e1 čvor sada svestan izdavanja urađenih od strane čvora e2, početnog izdavanja Bitcoina i našeg novoizdatog sredstva, od kojeg možemo videti 100. Obratite pažnju na heksadecimalnu vrednost novog sredstva i da nema pridružene oznake sredstva, kao što postoji za izdavanje Bitcoin-a.


Proveri ponovo e2-ovu listu poznatih izdavanja.


```
e2-cli listissuances
```


To nam pokazuje da e2 nije svestan izdavanja sredstava koje je izvršio e1. Može videti samo početno izdavanje Bitcoina koje je već mogao videti.


Ovo je zato što e2 nije svestan i ne prati adrese na koju je nova imovina poslata kada ju je izdao e1.


Važno je napomenuti da čak iako e2 ne može videti samo izdavanje, e1 bi i dalje mogao poslati e2 čvoru deo imovine. Nova imovina bi se zatim pojavila kao raspoloživo stanje u e2-ovom novčaniku, iako e2 nije svesan originalnog izdavanja.


Da bi omogućili e2 da vidi stvarno izdavanje (i samim tim izdat iznos), potrebno je dodati adresu u e2 kao praćenu adresu.


Da bismo to uradili, moramo saznati adresu na koji je sredstvo poslato. Za ovo ćemo koristiti transaction ID koji smo ranije kopirali i zatražiti od e1 da preuzme detalje te transakcije kako bismo pronašli tačnu adresu koju ćemo dodati u listu praćenja e2 novčanika.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


Pomicanjem naviše pored heksa podataka transakcije videćete adresu na kojoj se nalazi 100 naših novih sredstava, identifikovanih po njihovoj heks vrednosti.


Uzmite adresu i kopirajte je kako bismo je mogli uvesti u e2.


Sada treba da uvezemo tu adresu u e2. Da bismo to uradili koristimo komandu importaddress.


```
e2-cli importaddress <the-issued-to-address>
```


Ako sada proverimo listu izdavanaja čvora e2.


```
e2-cli listissuances
```


Možete videti da je naš novoizdati aset sada uključen na listu. Čvor e2 je takođe u mogućnosti da odredi količinu aseta koja je izdata, zajedno sa količinom povezanog tokena, jer je izdavanje bilo unblinded izdavanje. Da biste omogućili korišćenje mapiranja ID-a aseta u ime unutar Elements-a, prvo zaustavite Elements.


```
e1-cli stop
```


Zatim ga ponovo pokrenite sa dodatnim parametrom koji mapira heksadecimalnu vrednost sredstva na ponuđenu oznaku. Ovo omogućava čvoru da prikaže podatke o sredstvu u formatu koji je čitljiviji ljudima. Možete dodati ovo na kraj Elements.conf ako želite, tada ne morate dodavati argument za daemon svaki put kada ga pokrenete. Na primer:


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


Ali ćemo ovde koristiti metodu argumentacije.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


Ponovno šaljem upit čvoru za listu izdavanja.


```
e1-cli listissuances
```


To nam pokazuje da mapiranje heksadecimalne vrednosti sredstva na njegovu oznaku funkcioniše. Ponovo proveravamo listu izdavanja na e2 čvoru.


```
e2-cli listissuances
```


Možete videti da čvor e2 nema pristup ovoj oznaci, jer su oznake dostupne samo čvoru koji ih je postavio. Zaista, možemo dodeliti drugačiju oznaku istom heksu resursa na e2 nego što smo to uradili na e1. Prvo zaustavite čvor e2.


```
e2-cli stop
```


Ponovno pokretanje uz dodeljivanje drugačije oznake heksadecimalnoj vrednosti našeg novog sredstva.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


Listing izdavanja iz e2.


```
e2-cli listissuances
```


Oznake sredstava su lokalne za svaki čvor, samo heksadecimalni oblik sredstva prepoznaju drugi čvorovi na mreži.


Mapiranje oznake na heksadecimalnu vrednost sredstva je korisno prilikom izvršavanja radnji kao što su transakcije i upiti stanja unutar novčanika, jer omogućava skraćeni način referisanja na sredstvo. Na primer, ako želimo da pošaljemo deo našeg novog sredstva (u iznosu od 10) sa e1 na e2 bez korišćenja oznake.


Prvo treba da nabavimo adresu na koju ćemo poslati sredstvo.


```
e2-cli getnewaddress
```


Zatim upotrebite komandu sendtoaddress.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```


Potvrdite transakciju generisanjem bloka.


```
generate 1
```


Provera da li je sredstvo primljeno na e2.


```
e2-cli getwalletinfo
```


Možemo videti da je sredstvo zaista primljeno.


Imajte na umu da e2 mapira heksadecimalnu vrednost primljenog sredstva i prikazuje je koristeći sopstvenu oznaku. Lakši način da se uradi ista stvar bio bi korišćenje oznake sredstva unutar e1 prilikom slanja.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


Iza kulisa, Elements mapira lokalne oznake u heksadecimalne vrednosti kako bi pomogao u pojednostavljivanju korišćenja funkcionalnosti Issued Assets.


U ovom odeljku smo videli kako izdati i označiti sredstva. U sledećem odeljku ćemo pogledati ponovno izdavanje i uništavanje količina izdatog sredstva.


## Ponovno izdavanje sredstva


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


U ovom odeljku ćete naučiti kako da izdate više već izdatog sredstva, kao i kako da uništite određenu količinu izdatog sredstva.


Potrebno je ponovo izdati (stvoriti više) imovine ili uništiti određenu količinu imovine kada imovina predstavlja nešto što nema fiksnu ponudu. Ovo bi moglo da se odnosi na imovinu koja predstavlja zlato čuvano u trezoru, na primer; kako jedinice zlata ulaze i izlaze iz trezora, imovina koja predstavlja ponudu trezora mora biti prilagođena naviše ili naniže u skladu s tim.


Ponovno izdavanje iznosa sredstva zahteva vlasništvo nad povezanim tokenom koji je kreiran zajedno sa sredstvom kada je sredstvo prvobitno izdato.


Kada kreirate više od jednog sredstva, nije važno koji čvor je prvobitno izdao sredstvo, sve dok čvor koji ponovo izdaje određenu količinu sredstva poseduje ono što se obično naziva reissuance token sredstva. Pogledaćemo kako inicijalno kreirati reissuance token, kako ga koristiti za ponovno izdavanje nekog iznosa sredstva i takođe kako preneti reissuance token na druge čvorove, kako bi i oni imali dozvolu da ponovo izdaju sredstvo.


Trebaće nam pristup dvema Elements čvorovima, koje ćemo nazvati e1 i e2. Čvorovima su resetovani blokčejnovi i defaultni asset je podeljen između njih.


Izdaćemo e1 količinu od 100 novog sredstva i kreirati 1 reissuance token za to isto sredstvo. Kreiraćemo izdavanje kao neskriveno (eng. unblinded) kako bismo pojednostavili primer. Dakle, hajde da izdamo sredstvo i njegov povezani reissuance token.


```
e1-cli issueasset 100 1 false
```


Zabeleži ID sredstva i takođe ID tokena za ponovno izdavanje.


Pošto ćemo kasnije ponovo izdavati više jedinica sredstva sa e2, biće potrebno da zabeležimo ID transakcije u kojoj je sredstvo izdato i da ga iskoristimo za uvoz adrese na koju je sredstvo poslato.


Potvrdite transakciju.


```
e1-cli -generate 1
```


Sada ćemo proveriti detalje transakcije koristeći komandu gettransaction:


```
e1-cli gettransaction <txid>
```


Pomicanjem naviše pored heksa podataka transakcije videćete da je u transakciji čvor e1 primio 1 reissuance token i 100 izdatog sredstva.


Napravite kopiju adrese kako bismo je mogli uvesti u e2.


A sada uvoz adrese u e2-ov novčanik.


```
e2-cli importaddress <address>
```


Sada možemo videti da su i e1 i e2 svesni izdavanja imovine.


```
e1-cli listissuances

e2-cli listissuances
```


Trenutno e1 drži svu količinu imovine i 1 reissuance token, ali e2 ne.


```
e1-cli getwalletinfo
```


Takođe imajte na umu da e1 ima manje defaultnog asseta nego ranije jer je platio mali iznos za pokrivanje transakcijskih naknada. Ovaj iznos treba da bude prikupljen od strane e1 kada blok koji je kreiran bude imao preko 100 blokova konfirmacija.


```
e2-cli getwalletinfo
```


Kako e1 drži token za izdavanje, može ponovo izdati više sredstava. Ovo se radi korišćenjem komande reissueasset. Hajde da e1 ponovo izda još 100 te imovine.


```
e1-cli reissueasset <asset-id> 100
```


Provera ponovnog izdavanja je uspela.


```
e1-cli getwalletinfo
```


Možete videti da e1 sada drži 200 jedinica imovine, kao što se i očekivalo.


Kako e2 ne poseduje količinu tokena za ponovno izdavanje, dobiće grešku ako pokuša ponovo izdati sredstvo.


```
e2-cli reissueasset <asset-id> 100
```


Zabeleži poruku o grešci.


Detalje ponovnog izdavanja možemo pregledati iz e1 koristeći komandu listissuances.


```
e1-cli listissuances
```


Zabeleži oznaku `is_reissuance`.


Ako sada pošaljemo čvoru e2 određenu količinu reissuance tokena, oni će moći sami da ponovo izdaju količinu tog sredstva. Prvo nam je potrebna adresa da bismo ih poslali. Vredi napomenuti da se reissuance token tretira isto kao i bilo koje drugo sredstvo unutar Elements-a prilikom slanja i prikazivanja stanja i da se takođe može razložiti na manje apoene kao i bilo koje drugo sredstvo, tako da ne moramo poslati 1 reissuance token e2 da bi mogao ponovo izdati sredstvo. Bilo koji apoen će biti dovoljan. Generisanje adrese za e2 da primi reissuance token.


```
e2-cli getnewaddress
```


Zatim pošaljite deo RIT-a sa e1 na e2.


```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potvrdite transakciju.


```
e1-cli -generate 1
```


Sada možemo videti da e2 ima u svom vlasništvu 0.1 koji je poslat.


```
e2-cli getwalletinfo
```


To znači da e2 sada može ponovo izdati više sredstava povezanih sa RIT-om koji drži u svom novčaniku. Ponovo ćemo izdati 500 sredstava sa e2.


```
e2-cli reissueasset <asset-id> 500
```


Proverite rezultat ponovnog izdavanja.


```
e2-cli getwalletinfo
```


Možete videti da e2 sada drži iznos ponovo izdatih asseta u svom saldu novčanika i da sam RIT nije potrošen u procesu ponovnog izdavanja imovine.


Uništavanje količine imovine je nešto što svako ko poseduje bar količinu koja se uništava može da uradi, to nije regulisano od strane reissuance tokena.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


U ovom odeljku smo videli kako izdati sredstvo, zajedno sa načinom korišćenja tokena za ponovno izdavanje koji se opcionalno kreira kao deo izdavanja sredstva. Takođe smo videli kako je prenos reissuance tokena jednostavan kao i prenos bilo kog drugog sredstva, i da posedovanje bilo koje količine reissuance token daje vlasniku pravo da izda više povezanog sredstva. Stoga je veoma važno kontrolisati ko ima pristup tokenima za ponovno izdavanje u vašoj mreži. Takođe smo videli kako uništiti količinu sredstva i da ovaj proces nije kontrolisan posedovanjem reissuance tokena.


# Elements federacija


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## potpisivanje blokova


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements podržava federativni model potpisivanja koji vam omogućava da odredite broj Strong Federation članova koji moraju potpisati predloženi blok kako bi se proizveo važeći blok.


Ranije, i radi lakšeg primera, kreirali smo blokove koristeći komandu `generate`, koja nije morala da zadovolji zahtev za višestrukim potpisom kako bi blokovi kreirani bili prihvaćeni od strane mreže kao validni.


Postavićemo naše čvorove da zahtevaju 2-od-2 potpisa za kreiranje blokova. Ovo će biti postavljeno korišćenjem signblockscript parametra, koji može biti dodat u konfiguracioni fajl ili prosleđen čvoru prilikom pokretanja. Da bismo inicijalizovali lanac sa ovim parametrom, prvo moramo izgraditi skriptu od koje je sastavljen.


Uradićemo ovo koristeći neke postojeće čvorove, sačuvati podatke koje oni generišu, a zatim obrisati lanac kako bismo ga mogli ponovo pokrenuti koristeći naš signblockscript parametar. Ovo je neophodno jer skripta čini deo konsenzusnih pravila mreže i biće potrebno postaviti je pre on chain inicijalizacije. Ne može se dodati kasnije na već postojeći lanac.


Trebaće nam pristup dvema Elements čvorovima, koje ćemo nazvati e1 i e2. Čvorovima su resetovani blokčejnovi i defaultni asset je podeljen između njih.


Osigurajte da je parametar con_max_block_sig_size postavljen na visoku vrednost u vašoj Elements.conf datoteci, inače će potpisivanje blokova kasnije u ovom odeljku zakazati. Za ovaj vodič smo postavili con_max_block_sig_size=2000.


Kako ćemo resetovati naš blokčejn i obrisati novčanike povezane sa e1 i e2, biće nam potrebno da napravimo kopiju adresa, javnih ključeva i privatnih ključeva koje koristimo za generisanje skripte potpisivanje blokova, kako bismo ih mogli koristiti kasnije.


Prvo, potrebno je da za svaki od onih čvorova koji će biti potpisnici blokova da generišemo novu adresu, od kojih treba da uzmete kopiju.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Zatim treba da izdvojimo javne ključeve iz adresa i zabeležimo ih za kasniju upotrebu.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Zatim izdvojite privatne ključeve, koje ćemo ponovo uvesti kasnije kako bi čvorovi mogli potpisivati blokove nakon što ponovo inicijalizujemo naše blokčejnove i podatke novčanika.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Sada treba da generišemo skriptu za preuzimanje sredstava (otkupna skripta eng.redeem script) sa zahtevom za višepotpis 2 od 2. To radimo koristeći komandu createmultisig i prosleđujući 2 kao prvi parametar, a zatim obezbeđujući dva javna ključa. To su ključevi čije vlasništvo treba da se dokaže kasnije kada se blok kreira.


Bilo koji čvor, e1 ili e2, može generisati Multisig.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


To nam daje naš redeemscript, koji možete kopirati za kasniju upotrebu.


Sada moramo obrisati postojeće podatke blokčejna i novčanika kako bismo mogli ponovo početi sa novim signblockscript kao deo pravila konsenzusa blokčejna. Zato smo ranije morali napraviti kopiju nekih podataka, kao što su privatni ključevi koji će se koristiti u novom lancu za potpisivanje blokova. Ovo morate uraditi pre nego što nastavite.


Sa našim postojećim novčanikom i obrisanim podacima lanca, sada možemo pokrenuti naše čvorove i inicijalizovati novi lanac koristeći signblockscript parametar. Prosledićemo -evbparams=dynafed:0::: da onemogućimo dynafed aktivaciju, jer nam ta napredna funkcija nije potrebna za ovaj primer.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


Sada treba da uvezemo privatne ključeve koje smo ranije sačuvali kako bi naši čvorovi mogli da potpisuju i pomognu u kompletiranju bilo kojih predloženih blokova.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


Korišćenje komande generate sada bi trebalo da prijavi grešku jer ne ispunjava potrebna pravila za potpisivanje blokova koja sada sprovode naši čvorovi.


```
e1-cli -generate 1
```


Da bi predložio novi blok, bilo koji čvor može pozvati getnewblockhex komandu. Ovo vraća heksadecimalni zapis novog bloka koji će biti potrebno potpisati pre nego što ga prihvate bilo koji čvorovi na našoj mreži.


```
e1-cli getnewblockhex
```


Zapamtite da komanda samo kreira predloženi blok, ne generiše jedan.


Da bismo to potvrdili, možemo videti da trenutno nema blokova u našem blokčejnu.


```
e1-cli getblockcount
```


Ako pokušamo poslati heksadecimalni blok bez prethodnog potpisivanja.


```
e1-cli submitblock <block-hex>
```


Dobijamo poruku koja nam govori da je dokaz o bloku nevažeći. To je zato što još uvek nije potpisan od 2 strane od potrebne 2 strane.


Dakle, hajde da e1 potpiše predloženi blok.


```
e1-cli signblock <block-hex>
```


Neka e2 potpiše hex.


```
e2-cli signblock <block-hex>
```


Primetite da e2 ne potpisuje izlaz kreiran potpisivanjem predloženog bloka od strane e1. Oboje potpisuju heksadecimalni oblik predloženog bloka nezavisno od rezultata onog drugog.


Sada treba da kombinujemo potpise blokova e1 i e2. Bilo koji čvor to može da uradi, sve što im je potrebno je potpisani blok heks od drugog čvora.


```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```


Možete videti da combineblocksigs komanda ispisuje heksadecimalni zapis potpisanog bloka, kao i status "complete", što nam govori da je heksadecimalni zapis bloka spreman za podnošenje.


Sada bilo koji čvor može poslati završeni blok hex. Neka to uradi e1.


```
e1-cli submitblock <combined-signed-hex>
```


Provera da li je podnošenje bilo važeće.


```
e1-cli getblockcount

e2-cli getblockcount
```


Možete videti da su i e1 i e2 prihvatili blok kao važeći i dodali ga na vrh svojih lokalnih kopija blokčejna.


Da rezimiramo proces. U ovom odeljku imamo:


- Predloženi blok.
- Svaki čvor potpisuje blok.
- Kombinovanje potpisa.
- Provere da su potpisi važeći i da ispunjavaju prag za redeemscript definisan u blokčejnu.
- Podnošenje bloka.


Svaki čvor na mreži je validirao blok i dodao ga svojoj lokalnoj kopiji blokčejna.


### Potpisivanje bloka


Iako proces u početku deluje složeno, redosled potpisivanje bloka u Elements-u je uvek isti i početno podešavanje treba izvršiti samo jednom:


1. Inicijalno podešavanje (izvodi se jednom)

2. Kreiranje višepotpisne adrese pod nazivom `signblockscript` koristeći javne ključeve potpisivača bloka federacije (eng. Federated Block Signers).

3. Redeem skripta iz ove adrese se koristi za pokretanje novog blokčejna.

4. Proizvodnja blokova (u toku)

5. Predloženi blokovi se generišu i razmenjuju radi potpisivanja.


Kada potreban prag broja potpisnika potpiše predloženi blok, potpisi se kombinuje i šalju mreži. Ako ispunjava kriterijume `signblockscript` lanca, čvorovi ga prihvataju kao važeći blok.


## Elements kao bočni lanac


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements je blokčejn platforma opšte namene otvorenog koda koja se takođe može `vezati` za postojeći blokčejn, kao što je Bitcoin. Kada je vezana za drugi blokčejn, za Elements se kaže da radi kao `Sidechain`. Bočni lanci omogućavaju dvosmerni prenos sredstava sa jednog lanca na drugi. Implementacija Elements kao Sidechain-a omogućava vam da zaobiđete neka od inherentnih ograničenja glavnog lanca (eng. mainchain), dok zadržavate dobar stepen sigurnosti koju pružaju sredstva osigurana na glavnom lancu.


Iako je Sidechain svestan mainchain-a i njegove istorije transakcija, mainchain nema svest o Sidechain-u i nije potrebna za njegovo funkcionisanje. Ovo omogućava sporednim lancima da inoviraju bez ograničenja ili kašnjenja povezanih sa predlozima za poboljšanje mainchain protokola. Umesto da se pokušava direktno promeniti, proširenje glavnog protokola unutar Sidechain-a omogućava da mainchain ostane siguran i specijalizovan, podržavajući nesmetano funkcionisanje Sidechain-a.


Proširivanjem funkcionalnosti Bitcoin-a i korišćenjem njegove osnovne sigurnosti, Sidechain bazirani na Elements platformi je u mogućnosti da pruži novu funkcionalnost koja prethodno nije bila dostupna korisnicima mainchain-a. Primer bočnog lanca baziranog na Elements-u u proizvodnoj upotrebi je Liquid Network.


Da bismo inicijalizovali Elements blokčejn kao Sidechain, potrebno je da koristimo federated peg script parametar. Ovaj parametar može biti postavljen u konfiguracionom fajlu čvora ili prosleđen prilikom pokretanja.


Federated peg script definiše koji članovi Strong Federation-a mogu da obavljaju funkcije peg-in i peg-out. Ovi funkcioneri se nazivaju `watchmen` jer nadgledaju mainchain i Sidechain za validne peg-in i peg-out transakcije i izvršavaju ih ako su validne. `Peg-out` znači premestiti povezanu imovinu iz Sidechain-a u mainchain, dok `peg-in` znači premestiti povezanu imovinu u Sidechain iz mainchain-a. Kada kažemo `premestiti u Sidechain`, zapravo mislimo da se sredstva zaključavaju multi-potpisnom adresom na mainchain-u i odgovarajući iznos imovine se kreira na Elements Sidechain-u. Kada kažemo `premestiti iz Sidechain-a`, mislimo da se imovina uništava na Elements Sidechain-u i odgovarajući iznos se oslobađa iz zaključanih sredstava na mainchain-u. Dozvola za obavljanje funkcija peg-in i peg-out zahteva da funkcioneri dokažu vlasništvo nad javnim ključevima korišćenih u federated peg script-i. Ovo se postiže korišćenjem odgovarajućih privatnih ključeva.


Da bismo kreirali federated peg script, prvo moramo da obezbedimo da svaki od naših čvorova generiše javni ključ. Takođe moramo da sačuvamo povezane privatne ključeve za kasniju upotrebu jer ćemo morati da obrišemo sve postojeće podatke lanca i inicijalizujemo novi lanac koristeći federated peg script. Ovo je zato što federated peg script čini deo konsenzus pravila Sidechain-a, i ne može se primeniti na postojeći, nepovezani, blokčejn kasnije.


Dakle, hajde da generišemo adrese za svaki od naših čvorova, sačuvamo relevantne podatke za kasniju upotrebu i generišemo federated peg script koju ćemo koristiti za inicijalizaciju našeg Sidechain-a kasnije.


Prvo nam je potrebno da svaki od naših čvorova, koji će delovati kao watchmen u našoj mreži, da generiše novu adresu.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Zatim validiramo adrese da bismo dobili javne ključeve.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


A zatim preuzmite privatne ključeve povezane sa svakom adresom.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Sačuvajte privatne i javne ključeve za kasniju upotrebu.


Sada moramo obrisati postojeće podatke blokčejna i novčanika jer ćemo inicijalizovati novi lanac koristeći federated peg script. Možete to učiniti sada. Ne zaboravite pokrenuti Bitcoin daemon, koji ćemo morati povezati.


Sada možemo inicijalizovati novi lanac sa federated peg script kreiranim korišćenjem javnih ključeva koje smo ranije sačuvali. Brojevi koje unosimo i koji okružuju naše javne ključeve u komandi definišu i ograničavaju broj korišćenih ključeva, kao i broj ključeva nad čijim vlasništvo mora biti dokazan kako bi se izvršilo peg-in i peg-out iz našeg Sidechain-a.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


Sada ćemo uvesti privatne ključeve koje smo ranije sačuvali, kako bi naši čvorovi kasnije mogli da potpišu i završe prenos sredstava između lanaca i ispune zahteve federated peg script-e.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


Sada treba da potvrdimo neke blokove na oba lanca. Potvrđivanje blokova je neophodan zahtev ovog procesa povezivanja lanaca jer štiti od reorganizacije blokova na mainchain-u što vodi ka inflaciji ponude vezane imovine unutar Sidechain-a.


Da bismo ovu sekciju fokusirali na federisani peg, generisaćemo blokove bez korišćenja modela potpisivanje blokova koji smo razmatrali u prethodnoj sekciji, i vratićemo se korišćenju komande 'generate' za kreiranje novih blokova.


```
b-cli generate 101

e1-cli generate 1
```


Ne moramo nužno da generišemo blokove odmah za Elements. Ali, hajde da generišemo jedan ipak. To je dobra praksa da se izbegnu potencijalne nedoslednosti.


Sada je naš lanac spreman za peg-in. Da bismo izvršili peg-in, potrebno je da generišemp posebnu vrstu adrese koristeći komandu getpeginaddress. Imajte na umu da vremenski period između generisanja peg-in adrese sa getpeginaddress i njenog preuzimanja sa claimpegin treba da bude što kraće. Peg-in adrese nisu dugoročno izdržljive i ne bi trebalo da se ponovo koriste.


```
e1-cli getpeginaddress
```


Možete videti da komanda kreira novu mainchain adresu, kao i novi skript koji će biti potrebno zadovoljiti kako bi se preuzela peg-in sredstva. Mainchain adresa je `pay to script Hash` adresa koju će koristiti funkcioneri koji obavljaju Watchmen ulogu unutar Elements mreže.


Kao i getnewaddress, getpeginaddress dodaje novu tajnu novčaniku pozivnog čvora , tako da je važno da uključite rezervnu kopiju datoteke novčanika u vaš proces upravljanja čvorovima.


Sada ćemo poslati neki Bitcoin iz mainchain-a u Sidechain. Naš mainchain regresioni test novčanik već drži neka sredstva.


```
b-cli getwalletinfo
```


Možemo videti da novčanik sadrži 50 Bitcoin-a. Poslaćemo jedan Bitcoin sa mainchain-a na Sidechain. Moramo poslati sredstva na mainchain adresu koji je naš čvor generisao ranije.


```
b-cli sendtoaddress <e1-pegin-address>
```


Moramo sačuvati ID ove transakcije jer će nam kasnije trebati kao dokaz o finansiranju.


Sada možemo videti da je bilans mainchain novčanika smanjen za iznos koji smo poslali, plus dodatni mali iznos za pokrivanje troškova transakcija.


```
b-cli getwalletinfo
```


Moramo ponovo da prihvatimo transakciju potvrđivanjem bloka.


```
b-cli generate 101
```


Da bi naš Elements čvor preuzeo peg-in sredstva, potrebno je da pribavimo `dokaz` da je peg-in transakcija izvršena. Kriptografski dokaz koristi ID finansirajuće transakcije za izračunavanje Merkle putanje koja dokazuje da je transakcija prisutna u potvrđenom bloku.


```
b-cli gettxoutproof '["<tx-id>"]'
```


Takođe nam trebaju neobrađenim podaci o transakcijama.


```
b-cli getrawtransaction <tx-id>
```


Sa dokazom i neobrađenim podacima za peg-in transakciju, naš Elements čvor sada može zatražiti peg-in koristeći neobrađenu transakciju i dokaz transakcije.


```
e1-cli claimpegin <raw> <proof>
```


Imajte na umu da postoji opcioni treći argument koji smo mogli da obezbedimo za claimpegin. Ovaj treći parametar može se koristiti za specificiranje Sidechain adrese na koju će se poslati potraživana sredstva. Ovo nije bilo potrebno u našem primeru jer smo pozivali komandu sa istog čvora koji poseduje adresu na koji će potraživana sredstva biti poslata.


Provera stanja e1.


```
e1-cli getwalletinfo
```


Generisanje bloka za potvrdu zahteva.


```
e1-cli generate 1
```


Provera stanja e1.


```
e1-cli getwalletinfo
```


Možemo videti da je peg-in uspešno preuzet.


Da biste izvršili peg-out, proces je sličan. U tom smislu se generiše adresa, sredstva se šalju na nju i sredstva se oslobađaju ako je transakcija validna. Nećemo pokrivati ceo proces peg-out-a jer uključuje rad na mainchain-u što je van okvira ovog kursa. Koraci u vezi sa događajima u Elements mreži su da se adresa generiše na glavnoj mreži.


```
b-cli getnewaddress
```


Sredstva se šalju na mainchain adresu sa Elements čvora koristeći sendtomainchain komandu.


```
e1-cli sendtomainchain <new-address> 1
```


Generisanje bloka za potvrdu transakcije.


```
e1-cli generate 1
```


Proveri saldo nočanika čvora.


```
e1-cli getwalletinfo
```


I videti da se saldo smanjio.


U ovom odeljku smo videli kako da:


- Generišemo federated peg script.
- Inicijalizujemo novi lanac koji koristi skriptu kao pravilo konsenzusa mreže.
- Pošaljemo sredstva sa mainchain-a na Sidechain.
- Zatražimo sredstva unutar Elements Sidechain-a.
- Razumemo kako se započinje slanje sredstava nazad na mainchain.


### FederatedPegScript



Da bi Elements radio kao Sidechain, Genesis blok u njegovom blokčejnu mora biti kreiran sa `fedpegscript`. Ovo se postiže prosleđivanjem `fedpegscript` parametra prilikom pokretanja čvora. Skripta će tada postati deo konsenzus pravila Elements blokčejna i omogućiti validaciju i izvršavanje peg-in i peg-out zahteva.


`fedpegscript` se sastoji od javnih ključeva koje kontrolišu oni koji su ovlašćeni za izvršavanje peg akcija. Sledeći primer prikazuje format 2-od-2 multisignature fedpegscript-a:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


Napomena: Karakteri izvan javnih ključeva su graničnici koji označavaju javni ključ i `n od m` zahteve. Na primer, šablon za 1-of-1 fedpegscript bi bio '5121<javni ključ 1>51ae'.


### Peg-in


Pre nego što peg-in može biti prihvaćen od strane Elements Sidechain-a, mora imati dovoljno potvrda na mainchain-u. Ovo je neophodno kako bi se izbegla inflacija ponude povezanog (eng. pegged) asseta na Elements Sidechain-u koja bi mogla biti uzrokovana reorganizacijom mainchain-a.


Kratke reorganizacije vrha Bitcoin blokčejna očekuju se kao deo normalnog rada Proof of Work (PoW) konsenzusnog mehanizma. Kao takav, Elements prihvata peg-in kao važeći samo kada ima dovoljan broj potvrda unutar Bitcoin blokčejna. Ovo služi da se spreči da Elements prihvati isti peg-in više puta.


### Peg-Out


Peg-out se dešava kada Elements čvor pozove komandu `sendtomainchain`, koja kao ulaz uzima mainchain adresu (odredište peg-out-a) kao i iznos povezanog asseta koji treba da bude `povučen`. Ovo kreira peg-out transakciju na Sidechain. Kada funkcioneri koji deluju kao watchmen-i otkriju da je peg-out transakcija potvrđena na Sidechain-u, oni se pobrinu da zapravo oslobode sredstvo na mainchain-u na peg-out-a adresu, kao što smo naučili u ranijim delovima kursa.


## Elements kao samostalni blokčejn


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


Do sada smo videli kako pokrenuti Elements kao Sidechain. Međutim, Elements može takođe funkcionisati kao samostalno blokčejn rešenje sa sopstvenim podrazumevanim izvornim sredstvom. U ovoj postavci Elements blokčejn i dalje zadržava sve karakteristike Sidechain implementacije, kao što su Confidential Transactions i Issued Assets, ali nije potrebno izvršiti peg-in ili peg-out da bi se osnovna sredstva dodala ili uklonila iz opticaja.

U ovom odeljku ćemo:


Inicijalizovati novi Elements blokčejn sa defaultnim assetom nazvanim `newasset`.


Navesti 1,000,000 `newasset` koji će biti kreirani zajedno sa 2 tokena za ponovno izdavanje.


Zatražiti sve anyone-can-spend `newasset` kovanice.


Zatražiti sve anyone-can-spend tokene za ponovno izdavanje 'newasset-a'.


Poslati sredstvo i njegov reissuance token na novčanik drugog čvora.


Ponovo izdati više 'newasset-a' sa oba čvora.


Da bi se inicijalizovala Elements mreža da radi kao samostalni blokčejn, svaki čvor treba da se pokrene sa nekim osnovnim parametrima. Oni se koriste da bi se čvoru reklo da ne pokušava da validira peg-ins sa drugog blokčejna, ime default asseta mreže kao i količinu defaultnog asseta i pridruženog reissuance tokena koji treba kreirati.


Počećemo sada novi lanac koristeći ove parametre na naša dva povezana Elements čvora. Nazvaćemo default asset `newasset` i izdaćemo milion njih i dva `newasset` tokena za ponovno izdavanje.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


Imajte na umu da su iznosi korišćeni ovde u najmanjoj denominaciji koju mreža može prihvatiti, tako da dvesta miliona tokena za ponovno izdavanje zapravo odgovaraju dvema celim tokenima. Isto važi i za denominaciju početnih besplatnih novčića.


Proverite trenutni bilans novčanika našeg čvora.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Možemo videti da se inicijalizacija završila ispravno.


Kako su početna izdavanja sredstava kreirana kao `bilo ko može potrošiti`, e1 će ih sve preuzeti kako bismo mogli ukloniti pristup e2.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


Imajte na umu da ne moramo navesti 'newasset' kao sredstvo za slanje jer je to već default asset. I samim tim je i defaultni asset korišćen za plaćanje mrežnih naknada.


U okviru Elements-a, možete poslati više tipova sredstava na istu adresu, tako da možemo ponovo koristiti adresu koji smo upravo generisali za primanje defaultnog asseta, i koristiti ga kao odredišnu adresu za ponovno izdavanje tokena.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potvrdite transakcije.


```
e1-cli generate 101
```


Proverićemo da je e1 sada jedini vlasnik sredstava i tokena za ponovno izdavanje tih sredstava.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Što možemo videti da je zaista i slučaj.


Sada ćemo poslati deo 'newasset' korisniku e2, koji trenutno ima saldo nula.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


Imajte na umu da nismo morali da navedemo tip sredstva koje treba poslati, jer je `newasset` kreiran kao mrežni podrazumevani asset.


Hajde da pošaljemo i neke od tokena za ponovno izdavanje `newasset-a` čvoru e2.


```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potvrdite transakcije.


```
e1-cli generate 101
```


Možemo proveriti da li su novčanici ažurirani u skladu s tim.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Sada ćemo ponovo izdati nešto od defaultnog asseta iz e1. Imajte na umu da je mogućnost da se ovo uradi omogućena početnim parametrom initialreissuancetokens. Koji, ako se izostavi ili postavi na nulu, će rezultirati defaultnim assetom koji ne može biti ponovo izdat kasnije.


```
e1-cli reissueasset newasset 100
```


Mogli smo koristiti oznaku `newasset` umesto da moramo obezbediti hex id vrednost jer Elements lanac uvek označava svoj defaultni asset.


Provera da li je ponovno izdavanje defaultnog asseta uspelo:


```
e1-cli generate 101

e1-cli getwalletinfo
```


Dokazaćemo sada da, pošto e2 drži neke tokene ponovnog izdavanja `newasset`, može takođe ponovo izdati defaultni asset.


```
e2-cli reissueasset newasset 100
```


Provera da li je ponovno izdavanje defaultnog asseta od strane e2 uspelo.


```
e2-cli generate 101

e2-cli getwalletinfo
```


U ovom odeljku smo postavili Elements kao samostalni blokčejn i proverili da osnovna funkcionalnost radi kako očekujemo.


Koristili smo startne parametre za:


Inicijalizaciju novog Elements blokčejna sa defaultnim assetom nazvanim 'newasset'.


Naveli količinu defaultnog asseta za kreiranje on chain inicijalizacije.


Kreirali neke tokene za ponovno izdavanje defaultnog asseta i ponovo izdali više defaultnog asseta sa oba čvora.


Na našoj samostalnoj blokčejn Elements mreži, sve druge transakcione operacije će funkcionisati na isti način kao primeri pokriveni u glavnim delovima kursa, ali će koristiti 'newasset' umesto `Bitcoin` kao podrazumevano sredstvo i sredstvo za naknadu.


### Parametri pokretanja čvora i inicijalizacije blokčejna


Da bi se Elements čvor postavio da radi kao samostalni blokčejn, potrebno je koristiti nekoliko parametara zajedno. Sada ćemo pogledati svaki od njih i saznati šta rade.


#### `validatepegin=0`

Kao samostalni blokčejn nije potrebno da validira bilo koje peg-in ili peg-out transakcije, potrebno je da onemogućimo te provere. Sa ovom postavkom, ne morate da pokrećete Bitcoin klijentski softver ili čuvate kopiju Bitcoin blokčejna, jer će Elements mreža raditi nezavisno.


#### `defaultpeggedassetname`

Ovo vam omogućava da navedete ime defaultnog asseta kreiranog prilikom inicijalizacije blokčejna.


#### `initialfreecoins`

Broj (ekvivalentno jedinici bitkojn satošija) defaultnog asseta za kreiranje.


#### `initialreissuancetokens`

Broj (ekvivalentno jedinici bitkojn satošija) tokena za ponovno izdavanje za kreiranje podrazumevanog sredstva. Bez ovoga bi bilo nemoguće kreirati više defaultnog asseta. Ako ne želite da bude moguće kreirati više osnovne imovine, ovo može biti postavljeno na nulu ili izostavljeno.


Koristeći ove parametre, uobičajeni način za pokretanje čvora bi izgledao ovako:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### Osnovne operacije


Parametar `defaultpeggedassetname` primenjuje oznaku na osnovnu imovinu. Bez ovog podešavanja, osnovna imovina će automatski biti nazvan `Bitcoin`. U prethodnim odeljcima, kada smo slali sredstva koja smo sami izdali na drugi čvor, morali smo da navedemo ili heksadecimalnu vrednost sredstva ili lokalno primenjenu oznaku sredstva kako bismo rekli Elements platformi koje sredstvo šaljemo. Pošto se `defaultpeggedassetname` primenjuje na sve čvorove, ne moramo ga imenovati kada ga šaljemo, čak iako njegovo ime nije `Bitcoin`. Svaka funkcija koja bi pre podrazumevano slala `Bitcoin` sada će poslati šta god ste odlučili da označite kao podrazumevanu imovinu.


Dakle, slanje 10 novih defaultnih asseta na adresu je jednostavno kao:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


Ako ste takođe obezbedili čvoru vrednost za `initialreissuancetokens` veću od nule, onda ćete takođe moći da ponovo izdate više defaultnog asseta, što nije moguće ako pokrenete Elements kao Sidechain.


Da bi se to uradilo, bilo koji čvor koji drži neku količinu tokena povezanog sa defaultnim assetom samo treba da izda komandu u obliku:


```
e1-cli reissueasset <default asset name> <amount>
```


Korišćenjem gore navedenih parametara možete upravljati Elements-om kao samostalnim blokčejnom sa sopstvenom osnovnom imovinom, odvojenom od Bitcoin-a i drugih blokčejnova.


## Zaključak


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


Na ovom kursu smo naučili da je Elements mrežni protokol otvorenog koda koji se može implementirati kao bočni lanac na drugi blokčejn, ili kao samostalno blokčejn rešenje.


Videli smo da su izvorni kod i vebsajt za Elements (https://github.com/ElementsProject/Elements) hostovani na GitHub-u i da postoje forumi za diskusiju u zajednici, kao što su Build On L2 (https://community.Liquid.net/c/developers/), ili Liquid Developers Telegram (https://t.me/liquid_devel), koji se mogu koristiti za više informacija o implementaciji i razvoju aplikacija na Elements-u i Liquid-u. Ključne funkcije kao što su Confidential Transactions i Issued Assets su pokrivene, zajedno sa time kako članovi Strong Federation omogućavaju federisani potpis blokova i mehanizam 2-Way Peg.


Sledeći korak je da se izazoveš sveobuhvatnim kvizom koji pokriva sve prethodne sekcije, a zatim da započneš svoje Elements putovanje…srećno!


# Završni deo


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## Recenzije i ocene


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Zaključak


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>
