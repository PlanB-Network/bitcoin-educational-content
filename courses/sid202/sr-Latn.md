---
name: Zgrada sa Elements i Liquid Network
goal: Naučite koristiti i razvijati se uz Elements open-source Blockchain platformu i njene ključne funkcije
objectives: 

  - Razumite osnovne pojmove platforme Elements Blockchain i Liquid bočnih lanaca.
  - Naučite kako postaviti i pokrenuti Elements čvorove za samostalne i Sidechain konfiguracije.
  - Steknite praktično iskustvo sa federisanim block signing i Federated 2-Way Peg.
  - Postavite i upravljajte sigurnim, efikasnim Blockchain okruženjima za stvarne slučajeve upotrebe.

---

# Izgraditi na Liquid i Elements


Otkrijte napredne funkcije i mogućnosti Liquid i Elements, i naučite kako efikasno koristiti ove alate za unapređenje vaših razvojnih projekata. Ova obuka pruža potpunu teorijsku i praktičnu osnovu, omogućavajući vam da savladate funkcije kao što su Confidential Transactions, Issued Assets i Federated block signing.


Liquid, baziran na okviru Elements, dizajniran je za poboljšanje privatnosti, skalabilnosti i funkcionalnosti za finansijska i tehnička rešenja. U ovom kursu, steći ćete praktično iskustvo sa izdavanjem i upravljanjem sredstvima, Federated 2-Way Peg, i korišćenjem alata kao što su elementsd i elements-cli, osnažujući vas da kreirate inovativna rešenja prilagođena vašim potrebama.


Ovaj kurs je prilagođen programerima svih nivoa iskustva. Početnici i korisnici srednjeg nivoa će pronaći pristupačna objašnjenja i praktične primere, dok napredni korisnici mogu dublje istražiti tehničke detalje i manje poznate funkcije Liquid i Elements.


Pridružite nam se kako biste unapredili svoje veštine, otključali puni potencijal Liquid i Elements, i kreirali uticajne alate za budućnost inovacija Liquid.

+++

# Uvod


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## Pregled kursa


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


Dobrodošli na kurs SID202!


Cilj *Elements Academy* je da predstavi i objasni ključne koncepte *Elements*, platforme otvorenog koda na kojoj je izgrađen Liquid Sidechain. Do kraja ovog kursa, trebalo bi da imate solidno razumevanje glavnih karakteristika Elements, kao što su Confidential Transactions i Issued Assets, kao i procesa uključenih u rad sa Elements Core. Svaki deo kursa uključuje lekcije sa objašnjavajućim tekstovima i video zapisima, nakon čega sledi kviz.


Ova obuka ima za cilj da vas nauči kako da koristite i razvijate sa open-source platformom Elements, sa fokusom na Liquid Network. Otkrićete kako ove tehnologije mogu poboljšati privatnost, skalabilnost i funkcionalnost vaših razvojnih projekata. Bilo da ste početnik ili iskusni programer, ovaj kurs će vam pružiti snažnu osnovu za savladavanje osnovnih koncepata Elements i Liquid, kao i njihovih praktičnih primena.


**Sekcija 1: Uvod**

Počećemo sa sveobuhvatnim pregledom koncepata Elements. Naučićete kako je ova platforma dizajnirana da pruži modularnu i fleksibilnu osnovu za kreiranje bočnih lanaca kao što je Liquid. Cilj je razumeti strukturu Elements pre nego što se upustimo u njene praktične primene.


**Sekcija 2: Elements**

Ovaj deo će se fokusirati na to kako Elements funkcioniše. Naučićete kako da konfigurišete Elements čvor, upravljate njime u samostalnom režimu, ili ga koristite kao Sidechain.


**Sekcija 3: Korišćenje Elements – Praktične Upotrebe**

Kada se savladaju teorijske osnove, pokrićemo praktične primene Elements. Naučićete kako da izvršite Confidential Transactions, izdate sredstva i upravljate ponovnim izdavanjem sredstava.


**Sekcija 4: Elements Federacija**

Ovde ćemo istražiti napredne mehanizme, uključujući federisani block signing, korišćenje Elements kao Sidechain, i kreiranje nezavisnih blokčejnova. Ovaj deo će vam pomoći da razumete kako da osigurate bezbednost, integritet i interoperabilnost blokčejnova zasnovanih na Elements.


Spremni da istražite potencijal Elements i Liquid Sidechain? Hajde da počnemo!



## Pregled Elements


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements je open source, Sidechain-sposobna Blockchain platforma, koja omogućava pristup moćnim funkcijama razvijenim od strane članova zajednice, kao što su Confidential Transactions i Issued Assets.


Elements je, u svojoj suštini, protokol koji omogućava postizanje konsenzusa oko istorije transakcija i pravila koja upravljaju prenosom i kreiranjem sredstava pohranjenih u distribuiranom Blockchain Ledger.


Više informacija o Elements možete lako pronaći na vebsajtu Elements projekta (https://elementsproject.org/), zvaničnom blogu Liquid (https://blog.Liquid.net/) i portalu za programere (https://Liquid.net/devs).


### Elements


Pokrenut 2015. godine, Elements smanjuje troškove interne izrade i istraživanja i koristi najnoviju Blockchain tehnologiju, otvarajući mnoge nove slučajeve upotrebe za implementaciju. Blockchain zasnovan na Elements može raditi ili kao samostalni Blockchain ili biti povezan s drugim i raditi kao Sidechain. Pokretanje Elements kao Sidechain omogućava da se sredstva verifikovano prenose između različitih blokčejnova.


Izgrađen na kodnoj bazi Bitcoin i proširujući je, omogućava programerima koji su upoznati sa bitcoind API-jem da brzo i ekonomično kreiraju funkcionalne blokčejnove i testiraju projekte dokazivanja koncepta. Budući da je izgrađen na kodnoj bazi Bitcoin, Elements takođe može služiti kao testna platforma za promene u samom Bitcoin protokolu.


Neke od glavnih karakteristika Elements navedene su u nastavku.


#### Confidential Transactions


Podrazumevano, sve adrese u Elements su blinded koristeći Confidential Transactions. Zaslepljivanje je proces kojim se količina i tip sredstva koje se prenosi kriptografski skrivaju od svih, osim učesnika i onih kojima odluče da otkriju ključ za zaslepljivanje.


#### Issued Assets


Issued Assets na Elements omogućava izdavanje i prenos više tipova sredstava između učesnika mreže. Izdato sredstvo takođe ima koristi od Confidential Transactions i može biti ponovo izdano ili uništeno od strane bilo koga ko poseduje relevantni reissuance token.


#### Federated 2-Way Peg


Elements je platforma opšte namene Blockchain koja se takođe može "vezati" za postojeći Blockchain (kao što je Bitcoin) kako bi se omogućio dvosmerni prenos sredstava sa jednog lanca na drugi. Implementacija Elements kao Sidechain omogućava vam da zaobiđete neka od inherentnih svojstava glavnog lanca, dok zadržavate dobar stepen sigurnosti koju pružaju sredstva osigurana na glavnom lancu.


#### Potpisani Blokovi


Elements koristi Strong Federation potpisnika, nazvanih Blok Potpisnici, koji potpisuju i kreiraju blokove na pouzdan i pravovremen način. Ovo uklanja kašnjenje transakcija u PoW Mining procesu, koji je podložan velikim varijacijama vremena bloka zbog svoje nasumične poisson distribucije. Federisani block signing proces postiže pouzdano kreiranje blokova bez uvođenja potrebe za poverenjem treće strane ili računarskim `algoritmom` zasnovanim na Mining.


Elements dodaje sve ove funkcije na Bitcoin Core kodnu bazu, proširujući mogućnosti mainchain protokola i omogućavajući nove poslovne slučajeve kada se implementira kao Sidechain ili kao samostalno Blockchain rešenje.


# Element


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Kako Elements Radi


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements pruža tehničko rešenje za probleme sa kojima se korisnici Blockchain suočavaju svakodnevno; kašnjenje transakcija, nedostatak privatnosti i rizik za fungibilnost.


Elements prevazilazi ove probleme kroz korišćenje Federated block signing i Confidential Transactions.


Za razliku od mreže Bitcoin, proces block signing unutar Elements ne oslanja se na Dinamičke Članstvo Multiparty Potpise (DMMS) i Proof of Work (PoW). Umesto toga, Elements koristi Strong Federation potpisnika, nazvanih Blok Potpisnici, koji mogu potpisivati i kreirati blokove na pouzdan i pravovremen način. Ovo uklanja kašnjenje transakcija u PoW Mining procesu, koji je podložan velikoj varijabilnosti vremena bloka zbog svoje slučajne poisson distribucije. Federisani block signing proces postiže pouzdano kreiranje blokova bez uvođenja potrebe za poverenjem treće strane.


Elements može raditi kao Sidechain za drugi Blockchain, kao što je Bitcoin, ili kao samostalni Blockchain bez zavisnosti od drugih mreža.


Kada se koristi kao Sidechain, Strong Federation takođe sadrži članove koji omogućavaju siguran i kontrolisan prenos sredstava između glavnog lanca i Elements Sidechain. Kontrolisani prenos sredstava naziva se Federated 2-Way Peg, a članovi koji obavljaju ulogu prenosa sredstava nazivaju se watchmen.


Procesi uključeni u vođenje Elements mreže i uloge učesnika u mreži su važni za razumevanje kako Elements funkcioniše.


Bilo da je implementiran kao Sidechain ili samostalni Blockchain, Elements koristi Jake Federacije Potpisnika Blokova za proizvodnju blokova.


### Snažne Federacije


Elements koristi konsenzus model koji je prvi predložio Blockstream, nazvan Strong Federations. Strong Federation ne treba Proof of Work (PoW) i umesto toga se oslanja na kolektivne akcije grupe međusobno-nepoverljivih učesnika, nazvanih Functionaries.


Uloge koje Funkcioner može ispuniti unutar Strong Federation su: Potpisnici Blokova i watchmen. Potpisnici Blokova su potrebni ako pokrećete Elements bilo u Sidechain ili u samostalnom Blockchain režimu, dok su watchmen potrebni samo u Sidechain postavci.


Radnje koje član Strong Federation može da izvrši podeljene su između dve različite uloge kako bi se poboljšala sigurnost i ograničila šteta koju napadač može da prouzrokuje.


Kada se kombinuju, uloge ovih učesnika omogućavaju Elements da obezbedi i brzo kreiranje blokova (brže i konačno potvrđivanje transakcija) i osigurane, prenosive asete (aseti vezani direktno za drugi Blockchain).


Možete pročitati dokument o Strong Federations ovde: https://blockstream.com/strong-federations.pdf


### Blokiraj Potpisnike


Blockchain poput Bitcoin se produžava kada bilo ko ko je deo dinamičke grupe potpisnika blokova produži lanac demonstrirajući da je Proof of Work potrošen. Dinamička priroda skupa uvodi probleme latencije svojstvene takvim sistemima.


Korišćenjem fiksnog skupa potpisnika, federativni model zamenjuje dinamički skup poznatim skupom, šemom sa više potpisa. Smanjenje broja učesnika potrebnih za proširenje Blockchain povećava brzinu i skalabilnost sistema, dok validacija od strane svih strana osigurava integritet istorije transakcija.


Federated block signing se sastoji od nekoliko faza:



- Korak 1 - Blok Potpisnici predlažu kandidatske blokove naizmenično svim ostalim učesnicima Blok Potpisnicima.



- Korak 2 - Svaki block signer signalizira svoju nameru unapred se obavezujući da će potpisati dati kandidat blok.



- Korak 3 - Ako je zadati prag za pre-Commitment ispunjen, svaki block signer potpisuje blok.



- Korak 4 - Ako je prag potpisa (koji može biti različit od onog u koraku 3) ispunjen, blok se prihvata i šalje mreži. Strong Federation je postigao konsenzus o najnovijem bloku transakcija.



- Korak 5 - Sledeći blok zatim predlaže sledeći block signer u round-robin i proces se ponavlja.


Zato što generisanje blokova kod Strong Federation nije probabilističko i zasniva se na fiksnom skupu potpisnika, nikada neće biti podložno reorganizacijama sa više blokova. Ovo omogućava značajno smanjenje vremena čekanja povezanog sa potvrđivanjem transakcija. Takođe uklanja podsticaj za rudarenje radi profita (tj. nagrade za blokove) i zamenjuje ga podsticajem za produktivno učešće u mreži gde svi učesnici imaju isti zajednički cilj; osiguranje da mreža nastavi da funkcioniše na način koji je koristan za sve. Ovo postiže bez uvođenja jedne tačke kvara ili većih zahteva za poverenjem.


### Elements kao Sidechain - watchmen i Federated 2-Way Peg


Kada se pokreće kao Sidechain, neki članovi Strong Federation imaju dodatnu ulogu da ispune, onu watchmen. watchmen su odgovorni za transfer sredstava u i iz Elements Sidechain, procesi poznati kao `Peg-In` i `Peg-Out`.


Da bi Sidechain radio na pouzdan način, mora omogućiti učesnicima da verifikuju da je Supply sredstava kontrolisan i proverljiv. Elements Sidechain koristi dvosmerni federativni peg za omogućavanje dvosmernog transfera sredstava u i iz Elements Blockchain. Ovo zadovoljava zahteve dokazivog izdavanja i međulančanih transfera.


Funkcija Federated 2-Way Peg omogućava da jedan aset bude interoperabilan sa drugim blokčejnovima i da predstavlja drugi izvorni aset Blockchain. Povezivanjem vašeg Blockchain sa drugim, možete proširiti mogućnosti mainchain i prevazići neka od njegovih inherentnih ograničenja.


Na visokom nivou, transferi u Sidechain se dešavaju kada neko pošalje mainchain sredstva na Address kontrolisan od strane multi-potpisnog watchmen Wallet. Ovo efektivno zamrzava sredstva na mainchain. watchmen zatim validira transakciju i oslobađa istu količinu povezanog sredstva unutar Sidechain. Oslobođena sredstva se šalju na Sidechain Wallet koji može dokazati pravo na originalna mainchain sredstva. Ovaj proces efektivno premešta sredstva sa matičnog lanca na Sidechain.


Kako bi prebacio sredstva nazad na mainchain, korisnik pravi specijalnu peg-out transakciju na Sidechain. Ovu transakciju proverava watchmen koji zatim potpisuju transakciju trošenja sa multi-potpisnog Wallet koji kontrolišu na mainchain. Prag broja učesnika u federaciji mora potpisati pre nego što transakcija na mainchain postane važeća. Kada watchmen pošalju sredstvo nazad na mainchain, oni takođe uništavaju odgovarajući iznos na Sidechain, efektivno prenoseći sredstva između blokčejnova.


## Postavljanje i Pokretanje Elements


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Kako je Elements zasnovan na kodnoj bazi Bitcoin, komponente koje čine funkcionalnu mrežu su veoma slične.


Sama Elements čvor softver se zove `elementsd` i radi kao daemon na korisnikovom računaru. daemon (ili servis u Windows-u) je program koji radi kao pozadinski servis bez potrebe za direktnom kontrolom prijavljenog korisnika.


Napomena: Kroz ovaj dokument, uvek ćemo se pozivati na elementsd kao na verziju daemon, ali sve bi moglo biti urađeno sa Elements-qt, pod uslovom da je opcija servera omogućena.


Elements daemon se povezuje sa drugim čvorovima na mreži kako bi mogao Exchange transakcije i podatke o blokovima, validirajući i proširujući svoju lokalnu kopiju mrežnog Blockchain.


Elements softver takođe se sastoji od klijentskog programa nazvanog `elements-cli` koji vam omogućava da šaljete Remote Procedure Call (RPC) komande ka elementsd sa komandne linije. Ovo se može koristiti za upit Wallet balansa, pregled podataka o transakcijama ili blokovima ili emitovanje transakcije, na primer. Ova postavka bi trebalo da bude poznata svima koji su koristili Bitcoin ekvivalente; bitcoind i bitcoin-cli.


Čvor Elements može se konfigurisati prosleđivanjem parametara prilikom pokretanja ili putem konfiguracione datoteke, što omogućava pokretanje više instanci na istom računaru. Ovo je korisno za testiranje i razvojne svrhe jer možete postaviti sopstvenu lokalnu mrežu na jednom računaru, pri čemu svaki Elements čvor ima svoju kopiju Blockchain podataka, upravlja sopstvenim skupom nepotvrđenih validnih transakcija i sluša RPC zahteve na različitim portovima.


### Elements Code Repository i Zajednica


Elements je projekat otvorenog koda i njegov izvorni kod se može pronaći u Elements GitHub repozitorijumu na https://github.com/ElementsProject/Elements. Repozitorijum sadrži izvorni kod za elementsd i elements-cli programe zajedno sa alatima za instalaciju i izgradnju, skup testova i neku instruktivnu dokumentaciju.


Da bi upotpunio repozitorijum koda, tu je i vebsajt https://elementsproject.org, resurs fokusiran na zajednicu koji sadrži objašnjenja šta je Elements, kako funkcioniše i sveobuhvatan odeljak sa tutorijalima. Tutorijal se fokusira na učenje o Elements prateći primere komandne linije i pokazuje vam kako da izgradite jednostavne desktop i veb aplikacije na njemu. Sajt takođe navodi popularne Elements forume za diskusiju u zajednici i sam je hostovan na GitHub-u, omogućavajući doprinos zajednice sadržaju sajta.


Da biste pokrenuli Elements na vašem računaru, prvo ćete morati klonirati (preuzeti kopiju) izvorni kod, instalirati sve zavisnosti koje kod ima i na kraju izgraditi izvršne datoteke daemon i klijenta. Softver Elements je tada spreman za konfiguraciju i pokretanje.


## Konfigurisanje čvorova i umrežavanje


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


Postavke konfiguracije mogu se proslediti čvoru Elements prilikom pokretanja kako bi se promenio način na koji radi, validira podatke, povezuje se sa drugim čvorovima i inicijalizuje svoje Blockchain podatke.


Postavke se ili učitavaju iz određenog `Elements.conf` fajla ili se prosleđuju kao parametri putem komandne linije.


Neke stvari se mogu promeniti korišćenjem ovih parametara:



- Naziv default asset korišćen u samostalnim implementacijama Blockchain.
- Broj početne imovine koja je stvorena.
- Imovina koja će se koristiti prilikom plaćanja transakcijskih naknada na mreži.
- Lokacija skladištenja Blockchain datoteka.
- RPC akreditivi korišćeni za povezivanje sa Bitcoin čvorom.
- Prag `n od m` prag koji treba ispuniti i važeći javni ključevi koji mogu potpisivati blokove.
- Skripta koja treba biti zadovoljena kako bi se izvršio prenos sredstava u i iz Sidechain.
- Da li se povezati na Bitcoin čvor kao Sidechain ili ne.


Mnogi od njih čine deo pravila konsenzusa mreže, tako da je važno da se primenjuju na svim čvorovima prilikom pokretanja. Neki se mogu promeniti nakon što je lanac inicijalizovan, ali neki moraju biti fiksirani nakon što se koriste za inicijalizaciju lanca.


Korišćenje parametara biće obrađeno kasnije u kursu, kako i kada budu povezani sa svakim delom.


### Osnovne operacije korišćenjem komandne linije


Ovaj kurs će prikazati primere koji koriste program `elements-cli` za upućivanje poziva RPC ka jednom ili više čvorova Elements. Ovo se radi iz terminal sesije i da bi komande bile kraće koristiće se `alias`. Prema ovoj konvenciji kada vidite nešto poput sledećih komandi:


```bash
e1-dae

e1-cli getnewaddress
```


`e1-dae` i `e1-CLI` su zapravo tipografske prečice koje koriste funkciju `alias` terminala. `e1-dae` i `e1-CLI` će zapravo biti zamenjeni kada se komanda izvrši i komanda koja će se pokrenuti biće slična:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


Ono što vidimo iznad je poziv za pokretanje Elements daemon i poziv za elements-cli programe smeštene u direktorijumu `$HOME/Elements/src` i vrednost za `datadir` parametar. Parametar `datadir` nam omogućava da kažemo daemon i klijent instance gde da pronađu njihove konfiguracione fajlove i, u slučaju daemon, gde da sačuvaju svoju kopiju Blockchain. Kako dele konfiguracioni fajl, klijent će biti u mogućnosti da izvrši RPC pozive ka daemon.


Pokretanjem gornje komande ponovo, ali sa drugačijom vrednošću `datadir`, možemo pokrenuti više od jedne instance Elements, svaka sa svojom zasebnom kopijom Blockchain i podešavanjima konfiguracije. Po ovom konvencionalnom pravilu koristićemo alias `e2-dae` i `e2-CLI` u toku kursa da se referišemo na drugačiji datadir direktorijum od e1. Tako bi gornji primer za našu drugu `e2` instancu bio:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


Ovo će nam omogućiti da izvršimo sve vrste operacija kao što su transakcije sredstava između čvorova, izdavanje sredstava i proveru upotrebe zaslepljivanja u Confidential Transactions između različitih čvorova na istoj mreži.


# Korišćenje Elementa Praktična primena


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Confidential Transactions


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


U ovom odeljku ćete naučiti kako da koristite funkciju Confidential Transactions uređaja Elements.


Sve adrese u Elements su, po defaultu, blinded koristeći Confidential Transactions, što čini da količina i tip prenetih sredstava budu vidljivi samo učesnicima u transakciji (i onima kojima odluče da otkriju ključ za zaslepljivanje), dok se i dalje kriptografski garantuje da se ne može potrošiti više novčića nego što je dostupno.


### Poverljive Adrese i Confidential Transactions


Podrazumevano, kada kreirate novi Address u Elements koristeći komandu `getnewaddress`, on se kreira kao poverljivi Address.


Kako bismo demonstrirali Confidential Transactions, poslaćemo e2 da sam sebi pošalje neka sredstva, a zatim ćemo pokušati da pregledamo transakciju sa e1. Ovo će pokazati poverljivu prirodu transakcija u Elements.


Svaki novi Address generisan od strane Elements čvora je poverljiv po defaultu. Možemo to demonstrirati tako što ćemo dobiti e2 da generate novi Address.


```
e2-cli getnewaddress
```


Imajte na umu da Address počinje sa e1. Ovo ga identifikuje kao Pov. Address. Detaljnije ispitivanje Address pomoću komande getaddressinfo prikazuje više detalja o Address.


```
e2-cli getaddressinfo <address>
```


Možete videti da postoji svojstvo confidential_key koje nam govori da je to poverljivo Address.


Poverljivi_ključ je javni ključ za zaslepljivanje, koji se dodaje samom poverljivom Address. Ovo je razlog zašto je poverljivi Address tako dug.


Takođe ima pridruženi nekonfidencijalni Address. Ako želite da koristite redovne, nekonfidencijalne transakcije unutar Elements, sredstva treba poslati na ovaj Address umesto na onaj sa prefiksom lq1.


Sada možemo omogućiti da e2 pošalje neka sredstva na Address koji je generisao. Ovo će kasnije pokazati da e1, pošto nije jedna od strana u transakciji, neće moći da vidi detalje transakcije.


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


Pomicanjem naviše kroz detalje transakcije, možete videti da e2 može pregledati iznose poslate i primljene, kao i imovinu koja je transaktovana. Takođe možete videti amountblinder i assetblinder svojstva, koja se koriste za sakrivanje detalja od drugih čvorova koji nisu uključeni u transakciju.


Da bismo proverili detalje iste transakcije iz e1, prvo moramo dobiti sirove detalje transakcije.


```
e1-cli getrawtransaction <txid>
```


To vraća sirove detalje transakcije. Ako pogledate unutar vout sekcije, možete videti da postoje tri instance. Prve dve instance su iznosi primanja i kusura, a treća je naknada za transakciju. Od ova tri iznosa, naknada je jedina u kojoj možete videti vrednost, jer je sama naknada uvek unblinded unutar Elements.


### Blinding Keys


Ono što prva dva odeljka vout prikazuju su "blinded opsezi" iznosa vrednosti i Commitment podaci koji služe kao dokaz stvarnog iznosa i tipa prenete imovine.


Čak i ako bismo uvezli privatni ključ e2 u e1-ov Wallet, i dalje ne bi mogao videti iznose i tip transakcije imovine jer još uvek nema saznanja o ključu za zaslepljivanje koji koristi e2. Dokazaćemo ovo uvozom privatnog ključa koji koristi e2-ov Wallet u e1-ov. Prvo moramo izvesti ključ iz e2.


```
e2-cli dumpprivkey <address>
```


Zatim ga uvezi u e1.


```
e1-cli importprivkey <privkey>
```


Sada možemo dokazati da e1 i dalje ne može videti vrednosti.


```
e1-cli gettransaction <txid>
```


Zaista, prikazuje 0 kao iznos tx kada je zapravo bio 1.


Da bismo mogli videti stvarnu, nezamaskiranu vrednost, potrebna nam je maskirajuća ključ. Da bismo to uradili, prvo izvozimo maskirajuću ključ iz e2.


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


Pokazuje da sa uvezenim ključem za zaslepljivanje, sada možemo videti stvarnu vrednost 1 unutar transakcije.


U ovom odeljku smo videli da upotreba ključa za zaslepljivanje skriva iznos i tip sredstava u transakciji, i da uvozom pravog ključa za zaslepljivanje možemo otkriti te vrednosti. U praktičnoj upotrebi, ključ za zaslepljivanje može, na primer, biti dat revizoru, ukoliko postoji potreba da se verifikuju iznosi i tipovi sredstava koje poseduje neka strana. Funkcija Confidential Transactions iz Elements takođe omogućava izvođenje "dokaza opsega". Dokazi opsega mogu dokazati da je iznos sredstva unutar datog opsega, bez potrebe da se otkrije stvarni iznos.


Takođe smo videli da su Confidential Transactions opcioni, ali su podrazumevano omogućeni kada se generiše novi Address.


To je to za ovu lekciju; srećno na kvizu i vidimo se u sledećoj!


## Issued Assets


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


U ovom odeljku ćete naučiti kako koristiti funkciju Issued Assets uređaja Elements.


Issued Assets omogućava izdavanje i prenos više vrsta sredstava između učesnika Elements mreže. Bilo koji čvor na mreži može izdati sopstvena sredstva. Izdavanja mogu predstavljati fungibilne Ownership bilo kog sredstva uključujući vaučere, kupone, valute, depozite, obveznice, akcije, itd. Issued Assets otvara vrata za izgradnju Trustless berzi, opcija i drugih naprednih pametnih ugovora koji uključuju samostalni Issued Assets.


Izdati resurs takođe ima koristi od Confidential Transactions i može ga ponovo izdati bilo ko ko drži povezani token.


Prvi korak je da ćemo trebati pristup dvema Elements čvorovima, koje ćemo nazvati e1 i e2. Čvorovima su resetovani blokčeinovi i default asset je podeljen između njih.


Dva čvora su na istoj lokalnoj mreži i povezana su međusobno, te stoga dele iste transakcije u svojim transakcijama Mempool i identične blokčejnove. Iako rade na istoj mašini, važno je napomenuti da ne dele iste stvarne Blockchain fajlove. Svaki čvor upravlja svojom lokalnom kopijom Blockchain, koja sadrži istu istoriju transakcija jer su u konsenzusu i pridržavaju se istih pravila protokola kao i drugi.


Hajde da počnemo proverom pogleda svakog čvora na postojeća izdavanja sredstava na mreži.


Ovo se radi pomoću komande listissuances.


```
e1-cli listissuances

e2-cli listissuances
```


Kao što možete videti, oba čvora prikazuju istu istoriju izdavanja. Obe prikazuju jedan aset, inicijalno izdavanje od 21 milion Bitcoin koje je kreirano on chain inicijalizacijom. Možete videti heksadecimalni ID aseta u rezultatima pokretanja gore navedene komande, kao i oznaku dodeljenu asetu, koja je 'Bitcoin'.


Važno je napomenuti da default asset uvek dobija oznaku kada se lanac inicijalizuje. Kada izdajete sopstvene asete, možete sami postaviti oznake za njih, što ćemo uskoro i uraditi. Pre nego što to možemo da uradimo, potrebno je da izdamo sopstveni aset.


Izdavanje novog sredstva će obaviti e1. Ovo se radi pomoću komande issueasset.


```
e1-cli issueasset 100 1 false
```


`issueasset` prihvata 3 parametra.


Količina novog sredstva za izdavanje, koristili smo 100. Količina tokena za kreiranje (tokeni se koriste za ponovno izdavanje količina sredstva), od kojih smo odabrali 1. Konačni parametar govori Elements da ili kreira izdavanje sredstva kao blinded ili unblinded. Koristićemo unblinded jer želimo da vidimo količine izdavanja iz e2 za minut, pa ćemo uneti false.


Pokretanje komande vraća podatke o izdavanju. Ovo uključuje transaction ID, od kojeg možete uzeti kopiju za kasniju upotrebu, jedinstvenu heksadecimalnu vrednost sredstva i jedinstvenu heksadecimalnu vrednost tokena sredstva.


generate blok za potvrdu transakcije izdavanja.


```
e1-cli -generate 1
```


Pokreni komandu `listissuances` protiv e1 ponovo.


```
e1-cli listissuances
```


To nam pokazuje da je e1 sada svestan 2 izdavanja, početnog izdavanja Bitcoin i našeg novoizdatog sredstva, od kojeg možemo videti 100. Obratite pažnju na heksadecimalnu vrednost novog sredstva i da nema pridružene oznake sredstva, kao što postoji za izdavanje Bitcoin.


Proveri ponovo e2-ovu listu poznatih izdanja.


```
e2-cli listissuances
```


To nam pokazuje da e2 nije svestan izdavanja sredstava koje je izvršio e1. Može videti samo početno izdavanje Bitcoin koje je već mogao videti.


Ovo je zato što e2 nije svestan i ne prati Address na koji je nova imovina poslata kada ju je izdao e1.


Važno je napomenuti da čak iako e2 ne može videti samo izdavanje, e1 bi i dalje mogao poslati e2 deo imovine. Nova imovina bi se zatim pojavila kao raspoloživo stanje u e2-ovom Wallet, iako nije svesna originalnog izdavanja.


Da bi omogućili e2 da vidi stvarno izdavanje (i samim tim iznos izdat), potrebno je dodati Address u e2 kao praćeni Address.


Da bismo to uradili, moramo saznati Address na koji je sredstvo poslato. Za ovo ćemo koristiti transaction ID koji smo ranije kopirali i zatražiti od e1 da preuzme detalje te transakcije kako bismo pronašli tačan Address koji ćemo dodati na Wallet listu praćenja e2.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


Pomicanjem naviše pored heksa podataka transakcije videćete Address koji je primio 100 naših novih sredstava, identifikovanih po njihovoj heks vrednosti.


Uzmite Address i kopirajte ga kako bismo ga mogli uvesti u e2.


Sada da uvezemo taj Address u e2. Da bismo to uradili koristimo komandu importaddress.


```
e2-cli importaddress <the-issued-to-address>
```


Ako sada proverimo listu izdanja e2.


```
e2-cli listissuances
```


Možete videti da je naš novoizdati aset sada uključen na listu. Čvor e2 je takođe u mogućnosti da odredi količinu aseta koja je izdata, zajedno sa količinom povezanog tokena, jer je izdavanje bilo unblinded izdavanje. Da biste omogućili korišćenje mapiranja ID-a aseta u ime unutar Elements, prvo zaustavite Elements.


```
e1-cli stop
```


Zatim ga ponovo pokrenite sa dodatnim parametrom koji mapira heksadecimalnu vrednost sredstva na obezbeđenu oznaku. Ovo omogućava čvoru da prikaže podatke o sredstvu u formatu koji je čitljiviji ljudima. Možete dodati ovo na kraj Elements.conf ako želite, tada ne morate dodavati argument za daemon svaki put kada ga pokrenete. Na primer:


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


Ali ćemo ovde koristiti metodu argumentacije.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


Ponovno upitujem čvor za listu izdanja.


```
e1-cli listissuances
```


To nam pokazuje da mapiranje heksadecimalne vrednosti sredstva na njegovu oznaku funkcioniše. Ponovo proveravamo listu izdanja na e2 čvoru.


```
e2-cli listissuances
```


Možete videti da čvor e2 nema pristup ovoj oznaci, jer su oznake dostupne samo čvoru koji ih je postavio. Zaista, možemo dodeliti drugačiju oznaku istom heksu resursa na e2 nego što smo to uradili na e1. Prvo zaustavite čvor e2.


```
e2-cli stop
```


Ponovno pokretanje sa drugačijom oznakom dodeljenom heksu našeg novog sredstva.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


Listing izdanja iz e2.


```
e2-cli listissuances
```


Oznake sredstava su lokalne za svaki čvor, samo heksadecimalni oblik sredstva prepoznaju drugi čvorovi na mreži.


Mapiranje oznake na heksadecimalnu vrednost sredstva je korisno prilikom izvršavanja radnji kao što su transakcije i Wallet upiti stanja, jer omogućava skraćeni način referisanja na sredstvo. Na primer, ako želimo da pošaljemo deo našeg novog sredstva (u iznosu od 10) sa e1 na e2 bez korišćenja oznake.


Prvo treba da nabavimo Address na koji ćemo poslati sredstvo.


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


Imajte na umu da e2 mapira heksadecimalnu vrednost primljenog sredstva i prikazuje je koristeći sopstvenu oznaku. Lakši način da se uradi ista stvar bio bi korišćenje oznake sredstva e1 prilikom slanja.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


Iza kulisa, Elements mapira lokalne oznake u heksadecimalne vrednosti kako bi pomogao u pojednostavljivanju korišćenja Issued Assets.


U ovom odeljku smo videli kako izdati i označiti sredstva. U sledećem odeljku ćemo pogledati ponovno izdavanje i uništavanje količina izdatog sredstva.


## Ponovno izdavanje sredstava


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


U ovom odeljku ćete naučiti kako da izdate više već izdatog sredstva, kao i kako da uništite određenu količinu izdatog sredstva.


Potrebno je ponovo izdati (stvoriti više) imovine ili uništiti određenu količinu imovine kada imovina predstavlja nešto što nema fiksni Supply. Ovo bi moglo da se odnosi na imovinu koja predstavlja zlato čuvano u trezoru, na primer; kako jedinice zlata ulaze i izlaze iz trezora, imovina koja predstavlja Supply trezora mora biti prilagođena naviše ili naniže u skladu s tim.


Ponovno izdavanje iznosa sredstva zahteva Ownership povezanog tokena koji je kreiran zajedno sa sredstvom kada je prvobitno izdato.


Kada kreirate više od jednog sredstva, nije važno koji čvor je prvobitno izdao sredstvo, sve dok čvor koji ponovo izdaje količinu sredstva poseduje ono što se obično naziva reissuance token sredstva. Pogledaćemo kako inicijalno kreirati reissuance token, kako ga koristiti za ponovno izdavanje količine sredstva i takođe kako preneti reissuance token na druge čvorove, kako bi i oni imali dozvolu da ponovo izdaju sredstvo.


Trebaće nam pristup dvema Elements čvorovima, koje ćemo nazvati e1 i e2. Čvorovima su resetovani blokčeinovi i default asset je podeljen između njih.


Izdaćemo e1 količinu od 100 novog sredstva i kreirati 1 reissuance token za to isto sredstvo. Kreiraćemo izdavanje kao unblinded kako bismo pojednostavili primer. Dakle, hajde da izdamo sredstvo i njegov povezani reissuance token.


```
e1-cli issueasset 100 1 false
```


Zabeleži ID sredstva i takođe ID (ponovnog izdavanja) tokena.


Kako ćemo kasnije ponovo izdavati više sredstava iz e2, potrebno je da zabeležimo transaction ID u kojem je sredstvo izdano i iskoristimo to za uvoz Address u koji je sredstvo poslato.


Potvrdite transakciju.


```
e1-cli -generate 1
```


Sada ćemo proveriti detalje transakcije koristeći komandu gettransaction:


```
e1-cli gettransaction <txid>
```


Pomicanjem naviše pored heksa podataka transakcije videćete da je u transakciji e1 primio 1 reissuance token i 100 povezanog sredstva.


Napravite kopiju Address kako bismo je mogli uvesti u e2.


A sada uvoz Address u e2-ov Wallet.


```
e2-cli importaddress <address>
```


Sada možemo videti da su i e1 i e2 svesni izdavanja imovine.


```
e1-cli listissuances

e2-cli listissuances
```


Trenutno e1 drži količinu imovine i 1 reissuance token, ali e2 ne.


```
e1-cli getwalletinfo
```


Takođe imajte na umu da e1 ima manje default asset nego ranije jer je platio mali iznos za pokrivanje transakcijskih naknada. Ovaj iznos treba da bude prikupljen od strane e1 kada blok koji je kreiran sazri preko 100 blokova duboko.


```
e2-cli getwalletinfo
```


Kako e1 drži reissuance token, može ponovo izdati više toga. Ovo se radi korišćenjem komande reissueasset. Hajde da e1 ponovo izda još 100 te imovine.


```
e1-cli reissueasset <asset-id> 100
```


Provera ponovnog izdavanja je uspela.


```
e1-cli getwalletinfo
```


Možete videti da e1 sada drži 200 jedinica imovine, kao što se očekivalo.


Kako e2 ne drži količinu reissuance token, dobiće grešku ako pokušaju ponovo izdati sredstvo.


```
e2-cli reissueasset <asset-id> 100
```


Zabeleži poruku o grešci.


Detalje ponovnog izdavanja možemo pregledati iz e1 koristeći komandu listissuances.


```
e1-cli listissuances
```


Zabeleži zastavicu `is_reissuance`.


Ako sada pošaljemo e2 određenu količinu reissuance token, oni će moći sami da ponovo izdaju količinu tog sredstva. Prvo nam je potreban Address da bismo ga poslali. Vredi napomenuti da se reissuance token tretira isto kao i bilo koje drugo sredstvo unutar Elements prilikom slanja i prikazivanja stanja i da se takođe može razložiti na manje apoene kao i bilo koje drugo sredstvo, tako da ne moramo poslati 1 reissuance token e2 da bi mogao ponovo izdati sredstvo. Bilo koji apoen će biti dovoljan. Generisanje Address za e2 da primi reissuance token.


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


Sada možemo videti da e2 drži 0.1 koji je poslat.


```
e2-cli getwalletinfo
```


To znači da e2 sada može ponovo izdati više sredstava povezanih sa RIT-om koji drži u svom Wallet. Ponovo ćemo izdati 500 sredstava za e2.


```
e2-cli reissueasset <asset-id> 500
```


Proverite rezultat ponovnog izdavanja.


```
e2-cli getwalletinfo
```


Možete videti da e2 sada drži iznos ponovo izdat u svom Wallet saldu i da sam RIT nije potrošen u procesu ponovnog izdavanja imovine.


Uništavanje količine imovine je nešto što svako ko poseduje bar količinu koja se uništava može da uradi, to nije regulisano od strane reissuance token.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


U ovom odeljku smo videli kako izdati sredstvo, zajedno sa načinom korišćenja reissuance token koji se opcionalno kreira kao deo izdavanja sredstva. Takođe smo videli kako je prenos reissuance token jednostavan kao i prenos bilo kog drugog sredstva, i da posedovanje bilo koje količine reissuance token daje vlasniku pravo da izda više povezanog sredstva. Stoga je veoma važno kontrolisati ko ima pristup tokenima za ponovno izdavanje u vašoj mreži. Takođe smo videli kako uništiti količinu sredstva i da ovaj proces nije kontrolisan posedovanjem reissuance token.


# Element Federacija


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## block signing


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements podržava federativni model potpisivanja koji vam omogućava da odredite broj Strong Federation članova koji moraju potpisati predloženi blok kako bi se proizveo važeći blok.


Ranije, i radi lakšeg primera, kreirali smo blokove koristeći komandu `generate`, koja nije morala da zadovolji zahtev za višestrukim potpisom kako bi blokovi kreirani bili prihvaćeni od strane mreže kao validni.


Postavićemo naše čvorove da zahtevaju 2-od-2 Multisig kreiranje blokova. Ovo će biti postavljeno korišćenjem signblockscript parametra, koji može biti dodat u konfiguracioni fajl ili prosleđen čvoru prilikom pokretanja. Da bismo inicijalizovali lanac sa ovim parametrom, prvo moramo izgraditi skriptu od koje je sastavljen.


Uradićemo ovo koristeći neke postojeće čvorove, sačuvati podatke koje oni generišu, a zatim obrisati lanac kako bismo ga mogli ponovo pokrenuti koristeći naš signblockscript parametar. Ovo je neophodno jer skripta čini deo konsenzusnih pravila mreže i biće potrebno postaviti je pri on chain inicijalizaciji. Ne može se dodati kasnije na već postojeći lanac.


Trebaće nam pristup dvema Elements čvorovima, koje ćemo nazvati e1 i e2. Čvorovima su resetovani blokčeinovi i default asset je podeljen između njih.


Osigurajte da je parametar con_max_block_sig_size postavljen na visoku vrednost u vašoj Elements.conf datoteci, inače će block signing kasnije u ovom odeljku zakazati. Za ovaj vodič smo postavili con_max_block_sig_size=2000.


Kako ćemo resetovati naš Blockchain i obrisati novčanike povezane sa e1 i e2, biće nam potrebno da napravimo kopiju adresa, javnih ključeva i privatnih ključeva koje koristimo za generate skriptu block signing kako bismo ih mogli koristiti kasnije.


Prvo, potrebno je da svaki od onih koji će biti block signing čvorovi do generate novi Address, od kojih treba da uzmete kopiju.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Zatim treba da izdvojimo javne ključeve iz adresa i zabeležimo ih za kasniju upotrebu.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Zatim izdvojite privatne ključeve, koje ćemo ponovo uvesti kasnije kako bi čvorovi mogli potpisivati blokove nakon što ponovo inicijalizujemo naše Blockchain i Wallet podatke.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Sada treba da generate skriptu Redeem sa zahtevima za višestruki potpis 2 od 2. To radimo koristeći komandu createmultisig i prosleđujući prvi parametar kao 2, a zatim obezbeđujući dva javna ključa. To su ključevi koje Ownership treba da dokaže kasnije kada se blok kreira.


Ili čvor, e1 ili e2, mogao bi generate Multisig.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


To nam daje naš redeemscript, koji možete kopirati za kasniju upotrebu.


Sada moramo obrisati postojeće podatke Blockchain i Wallet kako bismo mogli ponovo početi sa novim signblockscript kao delom pravila konsenzusa lanca. Zato smo ranije morali napraviti kopiju nekih podataka, kao što su privatni ključevi koji će se koristiti u novom lancu za potpisivanje blokova. Ovo morate uraditi pre nego što nastavite.


Sa našim postojećim Wallet i podacima lanca obrisanim, sada možemo pokrenuti naše čvorove i inicijalizovati novi lanac koristeći signblockscript parametar. Prosledićemo -evbparams=dynafed:0::: da onemogućimo dynafed aktivaciju, jer nam ta napredna funkcija nije potrebna za ovaj primer.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


Sada treba da uvezemo privatne ključeve koje smo ranije sačuvali kako bi naši čvorovi mogli da potpisuju i pomognu u kompletiranju bilo kojih predloženih blokova.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


Korišćenje komande generate sada bi trebalo da prijavi grešku jer ne ispunjava potrebna pravila block signing koja sada sprovode naši čvorovi.


```
e1-cli -generate 1
```


Da bi predložio novi blok, bilo koji čvor može pozvati getnewblockhex komandu. Ovo vraća heksadecimalni zapis novog bloka koji će biti potrebno potpisati pre nego što ga prihvate bilo koji čvorovi na našoj mreži.


```
e1-cli getnewblockhex
```


Zapamtite da komanda samo kreira predloženi blok, ne generate jedan.


Da bismo to potvrdili, možemo videti da trenutno nema blokova u našem Blockchain.


```
e1-cli getblockcount
```


Ako pokušamo poslati heksadecimalni blok bez prethodnog potpisivanja.


```
e1-cli submitblock <block-hex>
```


Dobijamo poruku koja nam govori da je dokaz o bloku nevažeći. To je zato što još uvek nije potpisan od strane 2 od potrebne 2 strane.


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


Provera da li je podnesak bio važeći.


```
e1-cli getblockcount

e2-cli getblockcount
```


Možete videti da su i e1 i e2 prihvatili blok kao važeći i dodali ga na vrh svojih lokalnih kopija Blockchain.


Da rezimiramo proces. U ovom odeljku imamo:


- Predložio blok.
- Neka svaki čvor to potpiše.
- Kombinovane potpise.
- Provereno da su potpisi važeći i da ispunjavaju prag lanca redeemscript.
- Podnet je podnet.


Svaki čvor na mreži je validirao blok i dodao ga svojoj lokalnoj kopiji Blockchain.


### block signing


Iako proces u početku deluje složeno, redosled block signing u Elements je uvek isti i početno podešavanje treba izvršiti samo jednom:


1. Inicijalno podešavanje (izvodi se jednom)

2. Kreiran je multisignature Address pod nazivom `signblockscript` koristeći javne ključeve Federated Block Signers.

3. Skripta Redeem iz ovoga se koristi za pokretanje novog Blockchain.

4. Proizvodnja blokova (u toku)

5. Predloženi blokovi se generišu i razmenjuju radi potpisivanja.


Kada prag broja potpisnika potpiše predloženi blok, on se kombinuje i šalje mreži. Ako ispunjava kriterijume lanca `signblockscript`, čvorovi ga prihvataju kao važeći blok.


## Element kao bočni lanac


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements je platforma opšte namene otvorenog koda Blockchain koja se takođe može `vezati` za postojeću Blockchain, kao što je Bitcoin. Kada je vezan za drugu Blockchain, za Elements se kaže da radi kao `Sidechain`. Bočni lanci omogućavaju dvosmerni prenos sredstava sa jednog lanca na drugi. Implementacija Elements kao Sidechain omogućava vam da zaobiđete neka od inherentnih ograničenja mainchain, dok zadržavate dobar stepen sigurnosti koju pružaju sredstva osigurana na mainchain.


Iako je Sidechain svestan mainchain i njegove istorije transakcija, mainchain nema svest o Sidechain i nije potrebna za njegovo funkcionisanje. Ovo omogućava sporednim lancima da inoviraju bez ograničenja ili kašnjenja povezanih sa predlozima za poboljšanje mainchain protokola. Umesto da se pokušava direktno promeniti, proširenje glavnog protokola omogućava da mainchain ostane siguran i specijalizovan, podržavajući nesmetano funkcionisanje Sidechain.


Proširivanjem funkcionalnosti Bitcoin i korišćenjem njegove osnovne sigurnosti, Elements-bazirani Sidechain je u mogućnosti da pruži novu funkcionalnost koja prethodno nije bila dostupna korisnicima mainchain. Primer Elements-baziranog Sidechain u proizvodnoj upotrebi je Liquid Network.


Da bismo inicijalizovali Elements Blockchain kao Sidechain, potrebno je da koristimo federated peg script parametar. Ovaj parametar može biti postavljen u konfiguracionom fajlu čvora ili prosleđen prilikom pokretanja.


federated peg script definiše koji članovi Strong Federation mogu da obavljaju funkcije peg-in i peg-out. Ovi funkcioneri se nazivaju `watchmen` jer nadgledaju mainchain i Sidechain za validne peg-in i peg-out transakcije i izvršavaju ih ako su validne. `Peg-out` znači premestiti povezanu imovinu iz Sidechain u mainchain, dok `peg-in` znači premestiti povezanu imovinu u Sidechain iz mainchain. Kada kažemo `premestiti u Sidechain`, zapravo mislimo da se sredstva zaključavaju u multi-potpisnom Address na mainchain i odgovarajući iznos imovine se kreira na Elements Sidechain. Kada kažemo `premestiti iz Sidechain`, mislimo da se imovina uništava na Elements Sidechain i odgovarajući iznos se oslobađa iz zaključanih sredstava na mainchain. Dozvola za obavljanje funkcija peg-in i peg-out zahteva da funkcioneri dokažu Ownership javnih ključeva korišćenih u federated peg script. Ovo se postiže korišćenjem odgovarajućih privatnih ključeva.


Da bismo kreirali federated peg script, prvo moramo da obezbedimo da svaki od naših čvorova generate ima javni ključ. Takođe moramo da sačuvamo povezane privatne ključeve za kasniju upotrebu jer ćemo morati da obrišemo sve postojeće podatke lanca i inicijalizujemo novi lanac koristeći federated peg script. Ovo je zato što federated peg script čini deo konsenzus pravila Sidechain, i ne može se primeniti na postojeći, nepovezani, Blockchain kasnije.


Dakle, generate i Address sa svakim od naših čvorova, sačuvaj relevantne podatke za kasniju upotrebu i generate federated peg script koji ćemo koristiti za inicijalizaciju našeg Sidechain kasnije.


Prvo nam je potreban svaki od naših čvorova, koji će delovati kao watchmen u našoj mreži, da generate novi Address.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Zatim validiramo Address da bismo dobili javne ključeve.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


A zatim preuzmite privatne ključeve povezane sa svakim Address.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Sačuvaj privatne i javne ključeve za kasniju upotrebu.


Sada moramo obrisati postojeće podatke Blockchain i Wallet jer ćemo inicijalizovati novi lanac koristeći federated peg script. Možete to učiniti sada. Ne zaboravite pokrenuti Bitcoin daemon, koji ćemo morati povezati.


Sada možemo inicijalizovati novi lanac sa federated peg script kreiranim korišćenjem javnih ključeva koje smo ranije sačuvali. Brojevi koje unosimo i koji okružuju naše javne ključeve definišu i ograničavaju broj korišćenih ključeva, i ključ Ownership koji mora biti dokazan kako bi se izvršilo peg-in i peg-out iz našeg Sidechain.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


Sada ćemo uvesti privatne ključeve koje smo ranije sačuvali, kako bi naši čvorovi kasnije mogli da potpišu i završe prenos sredstava između lanaca i ispune zahteve federated peg script.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


Sada treba da sazrimo neke blokove na oba lanca. Sazrevanje blokova je zahtev procesa povezivanja jer štiti od reorganizacije blokova na mainchain što vodi ka inflaciji pegged asset Supply unutar Sidechain.


Da bismo ovu sekciju fokusirali na federisani peg, generisaćemo blokove bez korišćenja modela block signing koji smo razmatrali u prethodnoj sekciji, i vratićemo se korišćenju komande 'generate' za kreiranje novih blokova.


```
b-cli generate 101

e1-cli generate 1
```


Ne moramo nužno da generate blokove odmah za Elements. Ali, hajde da generate jedan ipak. To je dobra praksa da se izbegnu potencijalne nedoslednosti.


Sada je naš lanac spreman za peg-in. Da bismo izvršili peg-in, potrebno je da generate posebnu vrstu Address koristeći komandu getpeginaddress. Imajte na umu da trajanje između generisanja peg-in Address sa getpeginaddress i njegovog preuzimanja sa claimpegin treba da bude što kraće. peg-in adrese nisu dugoročno izdržljive i ne bi trebalo da se ponovo koriste.


```
e1-cli getpeginaddress
```


Možete videti da komanda kreira novi mainchain Address, kao i novi skript koji će biti potrebno zadovoljiti kako bi se preuzela peg-in sredstva. mainchain Address je `pay to script Hash` Address koji će koristiti funkcioneri koji obavljaju watchmen ulogu unutar Elements mreže.


Kao i getnewaddress, getpeginaddress dodaje novu tajnu pozivnom čvoru Wallet, tako da je važno uključiti rezervnu kopiju Wallet datoteke u vaš proces upravljanja čvorovima.


Sada ćemo poslati neki Bitcoin iz mainchain u Sidechain. Naš mainchain regresioni test Wallet već drži neka sredstva.


```
b-cli getwalletinfo
```


Možemo videti da Wallet drži 50 Bitcoin. Poslaćemo jedan Bitcoin sa mainchain na Sidechain. Moramo poslati sredstva na mainchain Address koji je naš čvor generisao ranije.


```
b-cli sendtoaddress <e1-pegin-address>
```


Moramo sačuvati ID ove transakcije jer će nam kasnije trebati kao dokaz o finansiranju.


Sada možemo videti da je saldo mainchain Wallet smanjen za iznos koji smo poslali, plus dodatni mali iznos za pokrivanje troškova transakcija.


```
b-cli getwalletinfo
```


Moramo ponovo da obradimo transakciju.


```
b-cli generate 101
```


Da bi naš Elements čvor preuzeo peg-in sredstva, potrebno je da pribavimo `dokaz` da je peg-in transakcija izvršena. Kriptografski dokaz koristi finansiranje transaction ID za izračunavanje merkel puta i dokazuje da je transakcija prisutna u potvrđenom bloku.


```
b-cli gettxoutproof '["<tx-id>"]'
```


Takođe nam trebaju sirovi podaci o transakcijama.


```
b-cli getrawtransaction <tx-id>
```


Sa dokazom i neobrađenim podacima za peg-in transakciju, naš Elements čvor sada može zatražiti peg-in koristeći neobrađenu transakciju i dokaz transakcije.


```
e1-cli claimpegin <raw> <proof>
```


Imajte na umu da postoji opcioni treći argument koji smo mogli da obezbedimo za claimpegin. Ovaj treći parametar može se koristiti za specificiranje Sidechain Address na koji će se poslati potraživana sredstva. Ovo nije bilo potrebno u našem primeru jer smo pozivali komandu sa istog čvora koji poseduje Address na koji će potraživana sredstva biti poslata.


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


Da biste izvršili peg-out, proces je sličan. U tom smislu se generiše Address, sredstva se šalju na njega i sredstva se oslobađaju ako je transakcija validna. Nećemo pokrivati ceo proces peg-out-a jer uključuje rad na mainchain što je van okvira ovog kursa. Koraci u smislu Elements događaja su da se Address generiše na mainchain.


```
b-cli getnewaddress
```


Sredstva se šalju na mainchain Address sa Elements čvora koristeći sendtomainchain komandu.


```
e1-cli sendtomainchain <new-address> 1
```


Generisanje bloka za potvrdu transakcije.


```
e1-cli generate 1
```


Proveri saldo čvora Wallet.


```
e1-cli getwalletinfo
```


I videti da se saldo smanjio.


U ovom odeljku smo videli kako da:


- generate a federated peg script.
- Inicijalizuj novi lanac koji koristi skriptu kao pravilo konsenzusa mreže.
- Pošalji sredstva sa mainchain na Sidechain.
- Zatražite sredstva unutar Elements Sidechain.
- Razumeti kako se započinje slanje sredstava nazad na mainchain.


### FederatedPegScript



Da bi Elements radio kao Sidechain, blok Genesis u njegovom Blockchain mora biti kreiran sa `fedpegscript` na mestu. Ovo se postiže prosleđivanjem `fedpegscript` parametra prilikom pokretanja čvora. Skripta će tada postati deo konsenzus pravila Elements Blockchain i omogućiti validaciju i izvršavanje peg-in i peg-out zahteva.


`fedpegscript` se sastoji od javnih ključeva koje kontrolišu oni koji su ovlašćeni za izvršavanje peg akcija. Sledeći primer prikazuje format 2-od-2 multisignature fedpegscript-a:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


Napomena: Karakteri izvan javnih ključeva su graničnici koji označavaju javni ključ i `n od m` zahteve. Na primer, šablon za 1-of-1 fedpegscript bi bio '5121<javni ključ 1>51ae'.


### Peg-in


Pre nego što peg-in može biti prihvaćen od strane Elements Sidechain, mora imati dovoljno potvrda na mainchain. Ovo je neophodno kako bi se izbegla inflacija u Supply od pegged asset na Elements Sidechain koja bi mogla biti uzrokovana reorganizacijom mainchain.


Kratke reorganizacije vrha Bitcoin Blockchain očekuju se kao deo normalnog rada Proof of Work (PoW) konsenzusnog mehanizma. Kao takav, Elements prihvata peg-in kao važeći samo kada ima dovoljnu dubinu unutar Bitcoin Blockchain. Ovo služi da se spreči da Elements prihvati isti peg-in više puta.


### Peg-Out


Peg-out se dešava kada čvor Elements pozove komandu `sendtomainchain`, koja kao ulaz uzima mainchain Address (odredište peg-out-a) kao i iznos pegged asset koji treba da bude `povučen`. Ovo kreira peg-out transakciju na Sidechain. Kada Funkcioneri koji deluju kao watchmen otkriju da je peg-out transakcija potvrđena na Sidechain, oni se pobrinu da zapravo oslobode sredstvo na mainchain do odredišta peg-out-a, kao što smo naučili u ranijim delovima kursa.


## Elements kao samostalni Blockchain


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


Do sada smo pogledali kako pokrenuti Elements kao Sidechain. Međutim, može takođe funkcionisati kao samostalno Blockchain rešenje sa sopstvenim podrazumevanim izvornim sredstvom. U ovoj postavci Elements Blockchain i dalje zadržava sve karakteristike Sidechain implementacije, kao što su Confidential Transactions i Issued Assets, ali nije potrebno peg-in ili peg-out za dodavanje ili uklanjanje default asset iznosa iz opticaja.


U ovom odeljku ćemo:


Inicijalizuj novi Elements Blockchain sa default asset nazvanim `newasset`.


Navedite 1,000,000 `newasset` koji će biti kreiran zajedno sa 2 tokena za ponovno izdavanje za njega.


Zatraži sve anyone-can-spend `newasset` kovanice.


Zatraži sve anyone-can-spend tokene za ponovno izdavanje za 'newasset'.


Pošalji sredstvo i njegov reissuance token na Wallet drugog čvora.


Ponovo izdajte više 'newasset' sa oba čvora.


Da bi se inicijalizovala Elements mreža da radi kao samostalna Blockchain, svaki čvor treba da se pokrene sa nekim osnovnim parametrima. Oni se koriste da bi se čvoru reklo da ne pokušava da validira peg-ins sa druge Blockchain, ime mreže default asset i količina default asset i pridruženog reissuance token koji treba kreirati.


Počećemo novi lanac koristeći ove parametre na naša dva povezana Elements čvora sada. Nazvaćemo default asset `newasset` i izdaćemo milion njih i dva `newasset` tokena za ponovno izdavanje.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


Imajte na umu da su iznosi korišćeni ovde u najmanjoj denominaciji koju mreža može prihvatiti, tako da dvesta miliona tokena za ponovnu izdaju zapravo odgovaraju dvema celim tokenima. Isto važi i za denominaciju početnih besplatnih novčića.


Proverite trenutne Wallet bilanse našeg čvora.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Možemo videti da je inicijalizacija radila ispravno.


Kako su početna izdavanja sredstava kreirana kao `bilo ko može potrošiti`, e1 će ih sve preuzeti kako bismo mogli ukloniti pristup e2.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


Imajte na umu da ne moramo navesti 'newasset' kao sredstvo za slanje jer je to već default asset. i stoga je i default asset korišćen za plaćanje mrežnih naknada.


U okviru Elements, možete poslati više tipova sredstava na isti Address, tako da možemo ponovo koristiti Address koji smo upravo generisali za primanje default asset, i koristiti ga kao odredišni Address za ponovnu izdavanje tokena.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potvrdite transakcije.


```
e1-cli generate 101
```


Proverićemo da je e1 jedini nosilac sredstva i njegov reissuance token sada.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Što možemo videti da je zaista slučaj.


Sada ćemo poslati deo 'newasset' korisniku e2, koji trenutno ima saldo nula.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


Imajte na umu da nismo morali da navedemo tip sredstva koje treba poslati, jer je `newasset` kreiran kao mrežni default asset


Hajde da pošaljemo i neke od tokena za ponovno izdavanje za `newasset` na e2.


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


Sada ćemo ponovo izdati neke od default asset iz e1. Imajte na umu da je mogućnost da se ovo uradi omogućena početnim parametrom initialreissuancetokens. Koji, ako se izostavi ili postavi na nulu, će rezultirati default asset koji ne može biti ponovo izdat kasnije.


```
e1-cli reissueasset newasset 100
```


Mogli smo koristiti oznaku `newasset` umesto da moramo obezbediti hex id vrednost jer Elements lanac uvek označava svoj default asset.


Provera da li je ponovno izdavanje default asset uspelo:


```
e1-cli generate 101

e1-cli getwalletinfo
```


Dokazaćemo sada da, pošto e2 drži neke tokene ponovnog izdavanja `newasset`, može takođe ponovo izdati default asset.


```
e2-cli reissueasset newasset 100
```


Provera da li je ponovno izdavanje default asset od strane e2 uspelo.


```
e2-cli generate 101

e2-cli getwalletinfo
```


U ovom odeljku smo postavili Elements kao samostalni Blockchain i proverili da osnovna funkcionalnost radi kako očekujemo.


Koristili smo startne parametre za:


Inicijalizuj novi Elements Blockchain sa default asset nazvanim 'newasset'.


Navedite količinu default asset za kreiranje inicijalizacije on chain.


Kreirajte neke tokene za ponovnu izdavanje za default asset i ponovo izdajte više default asset sa oba čvora.


Na našoj samostalnoj Blockchain Elements mreži, sve druge transakcione operacije će funkcionisati na isti način kao primeri pokriveni u glavnim delovima kursa, ali će koristiti 'newasset' umesto `Bitcoin` kao podrazumevani i naknadni aset.


### Parametri pokretanja čvora i inicijalizacije lanca


Da bi se Elements čvor postavio da radi kao samostalni Blockchain, potrebno je koristiti nekoliko parametara zajedno. Sada ćemo pogledati svaki od njih i saznati šta rade.


#### `validatepegin=0`

Kao samostalni Blockchain ne treba da validira bilo koje peg-in ili peg-out transakcije, potrebno je da onemogućimo te provere. Sa ovom postavkom, ne morate da pokrećete Bitcoin klijentski softver ili čuvate kopiju Bitcoin Blockchain, jer će Elements mreža raditi nezavisno.


#### `defaultpeggedassetname`

Ovo vam omogućava da navedete ime default asset kreiranog prilikom inicijalizacije Blockchain.


#### `initialfreecoins`

Broj (u ekvivalentu jedinice Bitcoin's Satoshi) default asset za kreiranje.


#### `initialreissuancetokens`

Broj (u ekvivalentu jedinice Bitcoin Satoshi) tokena za ponovno izdavanje za kreiranje default asset. Bez ovoga bi bilo nemoguće kreirati više default asset. Ako ne želite da bude moguće kreirati više default asset, ovo može biti postavljeno na nulu ili izostavljeno.


Koristeći ove parametre, uobičajeni način za pokretanje čvora bi izgledao ovako:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### Osnovne operacije


Parametar `defaultpeggedassetname` primenjuje oznaku na default asset. Bez ovog podešavanja, default asset će automatski biti nazvan `Bitcoin`. U prethodnim odeljcima, kada smo slali sredstva koja smo sami izdali na drugi čvor, morali smo da navedemo ili heksadecimalnu vrednost sredstva ili lokalno primenjenu oznaku sredstva kako bismo rekli Elements koje sredstvo šaljemo. Pošto se `defaultpeggedassetname` primenjuje na sve čvorove, ne moramo ga imenovati kada ga šaljemo, čak iako njegovo ime nije `Bitcoin`. Svaka funkcija koja bi pre podrazumevano slala `Bitcoin` sada će poslati šta god ste odlučili da označite kao default asset.


Dakle, slanje 10 novih default asset na Address je jednostavno kao:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


Ako ste takođe obezbedili čvoru vrednost za `initialreissuancetokens` veću od nule, onda ćete takođe moći da ponovo izdate više default asset, što nije moguće ako pokrenete Elements kao Sidechain.


Da bi to uradio, bilo koji čvor koji drži količinu tokena povezanog sa default asset samo treba da izda komandu u obliku:


```
e1-cli reissueasset <default asset name> <amount>
```


Korišćenjem gore navedenih parametara možete upravljati Elements kao samostalnim Blockchain sa sopstvenim default asset, odvojenim od Bitcoin i drugih blokčejnova.


## Zaključak


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


Na ovom kursu smo naučili da je Elements open-source mrežni protokol koji se može implementirati kao Sidechain na drugi Blockchain, ili kao samostalno Blockchain rešenje.


Videli smo da su izvorni kod i vebsajt za Elements (https://github.com/ElementsProject/Elements) hostovani na GitHub-u i da postoje forumi za diskusiju u zajednici, kao što su Build On L2 (https://community.Liquid.net/c/developers/), ili Liquid Developers Telegram (https://t.me/liquid_devel), koji se mogu koristiti za više informacija o implementaciji i razvoju aplikacija na Elements i Liquid. Ključne funkcije kao što su Confidential Transactions i Issued Assets su pokrivene, zajedno sa time kako članovi Strong Federation omogućavaju federisani block signing i mehanizam 2-Way Peg.


Sledeći korak je da se izazoveš kumulativnim kvizom koji pokriva sve prethodne sekcije, a zatim da započneš svoje Elements putovanje…srećno!


# Završni deo


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## Recenzije i ocene


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Zaključak


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>