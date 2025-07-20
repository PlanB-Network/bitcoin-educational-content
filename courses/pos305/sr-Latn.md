---
name: Bitcoin i BTC Pay Server
goal: Instalirajte BTC Pay Server za vaše poslovanje
objectives: 

  - Razumeti šta je btcpayserver.
  - Samostalno hostujte i konfigurišite BTC Pay Server.
  - Koristite btcpayserver u svom svakodnevnom poslovanju.

---

# Bitcoin i BTCPay Server


Ovo je uvodni kurs o BTCPay Server Operatoru koji su napisali Alekos i Bas, a koji su u Plan ₿ format kursa prilagodili melontwist i asi0.


NEZAVRŠENA PRIČA


"Ovo su laži, moje poverenje u tebe je slomljeno, učiniću te zastarelim."


Proizvedeno od strane BTCPay Server Foundation


+++

# Uvod


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Pregled kursa


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Dobrodošli na kurs POS 305 o BTCPay Serveru!


Cilj ove obuke je da vas nauči kako da instalirate, konfigurišete i koristite BTCPay Server u okviru vašeg poslovanja ili organizacije. BTCPay Server je open-source rešenje koje vam omogućava da obrađujete Bitcoin uplate autonomno, sigurno i isplativo. Ovaj kurs je prvenstveno namenjen naprednim korisnicima koji žele da ovladaju samostalnim hostovanjem BTCPay Server-a za potpunu integraciju u svoje svakodnevne operacije.


**Sekcija 1: Uvod u BTCPay Server**

Počećemo sa opštom prezentacijom BTCPay Server-a, uključujući ekran za prijavu, upravljanje korisničkim nalozima i kreiranje nove prodavnice. Ovaj uvod će vam pomoći da razumete BTCPay Server Interface i shvatite osnovne funkcije potrebne za početak korišćenja ovog alata.


**Sekcija 2: Uvod u Obezbeđivanje Bitcoin Ključeva**

Bezbednost vaših Bitcoin sredstava je veoma važna. U ovom odeljku ćemo istražiti generisanje kriptografskih ključeva, korišćenje hardverskih novčanika za zaštitu ovih ključeva, i kako da komunicirate sa vašim ključevima putem BTCPay Server-a. Takođe ćete naučiti kako da konfigurišete BTCPay Server Lightning Wallet kako biste optimizovali vaše transakcije.


**Sekcija 3: BTCPay Server Interface**

Ovaj deo će vas voditi kroz korisnički Interface BTCPay Server-a. Naučićete kako da se krećete kroz kontrolnu tablu, konfigurišete podešavanja prodavnice i servera, upravljate plaćanjima i iskoristite integrisane dodatke. Cilj je da vas upozna sa alatima potrebnim za prilagođavanje vaše instalacije prema vašim potrebama.


**Sekcija 4: Konfigurisanje BTCPay Servera**

Konačno, fokusiraćemo se na praktičnu instalaciju BTCPay Server-a u različitim okruženjima. Bilo da koristite LunaNode, Voltage ili Umbrel čvor, naučićete osnovne korake za implementaciju i konfiguraciju vašeg BTCPay Server-a, uzimajući u obzir specifičnosti svakog okruženja.


Spremni da savladate BTCPay Server i unapredite svoje poslovanje? Krenimo!


## Kritičke pohvale za Autorov Bitcoin i BTCPay Server


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Hajde da počnemo sa tim šta je BTCPay Server i odakle potiče. Cenimo transparentnost i određene standarde kako bismo formirali poverenje u Bitcoin prostoru.

Projekat u svemiru je narušio ove vrednosti. Glavni programer BTCPay Server-a, Nicolas Dorier, shvatio je ovo lično i obećao da će ih učiniti zastarelim. Evo nas mnogo godina kasnije, svakodnevno radimo ka ovoj budućnosti, potpuno otvorenog koda.


> Ovo su laži, moje poverenje u tebe je slomljeno, učiniću te zastarelim.
> Nicolas Dorier

Nakon reči koje je izgovorio Nicolas, bilo je vreme da se počne sa izgradnjom. Mnogo rada je uloženo u ono što danas zovemo BTCPay Server. Više ljudi je želelo da pomogne u ovom poduhvatu. Najprepoznatljiviji su r0ckstardev, MrKukks, Pavlenex, i prvi trgovac koji je koristio softver, astupidmoose.


Šta znači open source i šta je potrebno za takav projekat?


FOSS označava Free & Open-Source Software. Prvi deo se odnosi na uslove koji omogućavaju svakome da kopira, modifikuje i čak distribuira verzije (čak i za profit) softvera. Drugi deo se odnosi na otvoreno deljenje izvornog koda, podstičući javnost da doprinese i poboljša ga.

Ovo privlači iskusne korisnike koji su entuzijastični u vezi sa doprinosom softveru koji već koriste i od kojeg imaju koristi, što se vremenom pokazuje kao uspešnije u usvajanju u odnosu na vlasnički softver. To je u skladu sa etosom Bitcoin da „informacije žele biti slobodne.“ Okuplja strastvene ljude koji formiraju zajednicu i jednostavno je zabavnije. Kao i Bitcoin, FOSS je neizbežan.


### Pre nego što počnemo


Ovaj kurs se sastoji od više delova. Mnoge će obraditi vaš učitelj u učionici, Demo okruženja kojima dobijate pristup, server koji je hostovan za vas, i moguće ime domena. Ako završavate ovaj kurs samostalno, imajte na umu da okruženja označena kao DEMO neće biti dostupna za vas.

NB. Ako pratite ovaj kurs u učionici, imena servera mogu se razlikovati u zavisnosti od postavke vaše učionice. Varijable u imenima servera mogu biti različite zbog toga.


### Struktura Kursa


Svako poglavlje ima ciljeve i procene znanja. U ovom kursu, pokrićemo svaki od njih i imati rezime ključnih karakteristika na svakom bloku lekcije (tj. poglavlju). Ilustracije su prikazane kako bi pružile vizuelne povratne informacije i ojačale ključne koncepte u vizuelnom aspektu. Ciljevi su postavljeni na početku svakog bloka lekcije. Ovi ciljevi prevazilaze kontrolnu listu. Oni vam pružaju vodič ka novom skupu veština. Procene znanja postaju progresivno izazovnije postavljanje vašeg BTCPay Server-a.


### Šta studenti dobijaju uz kurs?


Sa kursom BTCPay Server, student može razumeti osnovne principe, tehničke i netehničke, Bitcoin. Opsežna obuka u korišćenju Bitcoin putem BTCPay Server-a omogućiće studentima da upravljaju sopstvenom Bitcoin infrastrukturom.


### Važne Web adrese ili Mogućnosti kontakta


Fondacija BTCPay Server, koja je omogućila Alekosu i Basu da napišu ovaj kurs, nalazi se u Tokiju, Japan. Fondacija BTCPay Server može se kontaktirati putem navedene veb stranice;



- https://foundation.btcpayserver.org
- pridružite se zvaničnim kanalima za ćaskanje: https://chat.btcpayserver.org


## Uvod u Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Razumevanje Bitcoin putem vežbe u učionici


Ovo je vežba u učionici, tako da ako sami pohađate ovaj kurs, ne možete je izvesti, ali i dalje možete proći kroz ovu vežbu. Da biste završili ovaj zadatak, minimalan broj ljudi je između 9 i 11.


Vežba počinje nakon gledanja uvoda „Kako Bitcoin i Blockchain rade“ od strane BBC-a.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Ova vežba zahteva učešće najmanje devet osoba. Ova vežba ima za cilj da fizički pruži ideju o tome kako Bitcoin funkcioniše. Igrajući svaku ulogu u mreži, imaćete interaktivan i zabavan način učenja. Ova vežba ne uključuje Lightning Network.


### Primer; Zahteva 9 / 11 osoba


Uloge su :



- 1 Kupac
- 1 Trgovac
- 7 do 9 Bitcoin čvorova


**Postavka je sledeća:**


Kupci kupuju proizvod iz prodavnice sa Bitcoin.


**Scenario 1 - Tradicionalni bankarski sistem**



- Postavljanje:
  - Pogledajte dijagrame/objašnjenja u priloženom Figjam-u - [Šematski prikaz aktivnosti](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Dobijte tri studenta volontera da igraju uloge Kupca (Alice), Trgovca (Bob) i Banke.
- Izvedi redosled događaja:
  - Kupac - pretražuje prodavnicu online i pronalazi artikal za $25 koji želi, i obaveštava Prodavca da bi želeo da ga kupi.
  - Trgovac- traži uplatu.
  - Kupac- šalje informacije o kartici Trgovcu
  - Trgovac - prosleđuje informacije Banci (identifikujući i svoj i identitet/informacije) zahtevajući plaćanje od
  - Banka prikuplja informacije o Kupcu i Trgovcu (Alice i Bob) i proverava da li je stanje na računu kupca dovoljno.
  - Oduzima $25 sa Alisinog računa, dodaje $24 na Bobov račun, uzima $1 za uslugu
  - Trgovac dobija odobrenje od Banke i šalje proizvod kupcu.
- Komentari:
  - Bob i Alice moraju imati odnos sa bankom.
  - Banka prikuplja identifikacione informacije o Bobu i Alisi.
  - Banka uzima deo.
  - Banka mora biti poverena za čuvanje novca svakog učesnika sve vreme.


**Scenario 2 - Bitcoin Sistem**



- Postavljanje:
  - Pogledajte dijagrame/objašnjenje u priloženom Figjam - [Šema Aktivnosti](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Zamenite Bank sa devet studenata koji će igrati ulogu Računara (Bitcoin Čvorovi/Rudari) u mreži kako bi zamenili Banku.
- Svaki od 9 računara ima potpun istorijski zapis svih prošlih transakcija ikada napravljenih (tako tačni saldi bez falsifikata), kao i skup pravila:
  - Potvrdite da je transakcija ispravno potpisana (thekeyfitsthelock)
  - Emitujte i primajte validne transakcije ka vršnjacima u mreži, odbacite nevalidne (uključujući one koje pokušavaju da potroše ista sredstva dvaput)
- Periodično ažurirajte/dodajte zapise sa novim transakcijama primljenim od “nasumičnog” računara pod uslovom da su svi sadržaji validni (napomena: za sada zanemarujemo komponentu Proof of Work radi jednostavnosti), u suprotnom ih odbacite i nastavite kao i pre dok sledeći “nasumični” računar ne pošalje ažuriranje.
  - Odgovarajući iznos je nagrađen ako je sadržaj bio važeći.
- Izvedi redosled događaja:
  - Kupac - pretražuje prodavnicu online i pronalazi artikal za $25 koji želi, i obaveštava trgovca da bi želeo da ga kupi.
  - Trgovac- traži uplatu slanjem kupcu Invoice/Address sa njihovog Wallet.
  - Kupac - konstruira transakciju (šalje $25 vrednosti BTC na Address koji je obezbedio Trgovac) i emituje je na Bitcoin Mrežu.
- Računari- primaju transakciju i verifikuju:
  - U Address se šalje najmanje $25 BTC-a iz
  - Transakcija je ispravno potpisana („otključana“ od strane kupca)
  - Ako nije slučaj, transakcija neće biti propagirana kroz mrežu, a ako jeste, onda se propagira i drži na čekanju.
  - Trgovci mogu proveriti da je transakcija na čekanju i u procesu čekanja.
- Jedan računar je „nasumično“ izabran da predloži finalizaciju predložene transakcije emitovanjem „bloka“ koji je sadrži; ako je ispravan, dobiće BTC nagradu.
  - OPCIONALNO/NAPREDNO - umesto nasumičnog odabira računara, simulirajte Mining tako što će računari bacati kockice dok se ne dogodi neki unapred određeni ishod (npr. prvi koji baci dve šestice zaredom je odabran)
  - Takođe može simulirati šta bi se desilo ako dva računara pobede približno istovremeno, što bi rezultiralo podelom lanca.
  - Računari proveravaju validnost, ažuriraju/dodaju zapise u svoje knjige ako su pravila ispunjena, i emituju blok ka vršnjacima.
  - Nasumično odabrani računar dobija nagradu za predlaganje važećeg bloka.
  - Trgovac proverava da li je transakcija završena; stoga su sredstva primljena, a predmet je poslat kupcu.
- Komentari:
  - Primetite da nije bilo potrebe za prethodnim bankarskim odnosom.
  - Nema potrebe za trećom stranom da posreduje; zamenjeno kodom/podsticajima.
  - Nema prikupljanja podataka od strane bilo koga van direktnog Exchange i samo neophodna količina mora biti razmenjena između učesnika (npr. slanje Address).
  - Nije potrebno poverenje između ljudi (osim što Trgovac šalje predmet), slično kao kupovina gotovinom na mnogo načina.
  - Novac je u vlasništvu pojedinaca.
  - Bitcoin Ledger je prikazan u dolarima radi jednostavnosti, ali u stvarnosti, to je BTC.
  - Simuliramo jednu transakciju koja se emituje, ali u stvarnosti, više transakcija čeka u mreži, a blokovi uključuju hiljade transakcija odjednom. Čvorovi takođe proveravaju da nema transakcija sa dvostrukim trošenjem na čekanju (odbacio bih sve osim jedne ako bi to bio slučaj).
- Scenariji varanja:
  - Šta ako kupac nije imao $25 BTC?
    - Ne bi mogli da kreiraju transakciju jer su „otključavanje“ i „Ownership“ ista stvar, a računari proveravaju da li je transakcija ispravno potpisana; u suprotnom, odbijaju je.
  - Šta ako nasumično odabrani računar pokuša da „promeni Ledger“?
    - Blok bi bio odbijen, jer svaki drugi računar ima kompletnu istoriju i primetio bi promenu, kršeći jedno od njihovih pravila.
    - Random Computer ne bi dobio nagradu, a nijedna transakcija iz njihovog bloka ne bi bila finalizovana.


## Procena znanja


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### Diskusija u učionici KA


Razgovarajte o nekim preteranim pojednostavljenjima napravljenim u vežbi u učionici pod drugim scenarijem i opišite šta stvarni Bitcoin sistem radi detaljnije.


### Pregled rečnika KA


Definišite sledeće ključne pojmove predstavljene u prethodnom delu:



- Čvor
- Mempool
- Ciljna Težina
- Blok


**Razgovarajte o značenju nekih dodatnih pojmova kao grupa:**


Blockchain, Transakcija, Dvostruko trošenje, Problem vizantijskih generala, Mining, Proof of Work (PoW), Hash Funkcija, Block reward, Blockchain, Najduži lanac, 51% Napad, Izlaz, Zaključavanje izlaza, Kusur, Satošiji, Javni/Privatni ključ, Address, Kriptografija javnog ključa, Digitalni potpis, Wallet


# Predstavljamo BTCPay Server


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Razumevanje ekrana za prijavu na BTCPay Server


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Rad sa BTCPay Serverom


Cilj ovog kursnog bloka biće sticanje opšteg razumevanja BTCPay Server softvera. U deljenom okruženju, preporučuje se da pratite demonstraciju instruktora i pratite BTCPay Server priručnik kako biste pratili predavača. Naučićete kako da kreirate Wallet kroz više metoda. Primeri uključuju Hot Wallet postavke i hardverske novčanike povezane putem BTCPay Server Vault-a. Ovi ciljevi se ostvaruju u Demo okruženju, koje prikazuje i omogućava pristup vaš instruktor kursa.


Ako pratite ovaj kurs sami, možete pronaći listu trećih strana domaćina za demo svrhe na https://directory.btcpayserver.org/filter/hosts. Snažno savetujemo protiv korišćenja ovih opcija trećih strana kao produkcionih okruženja, ali one služe pravoj svrsi za uvod u korišćenje Bitcoin i BTCPay Server-a.


Kao BTCPay Server rockstar pripravnik, možda imate prethodno iskustvo sa postavljanjem Bitcoin čvora. Ovaj kurs će govoriti specifično prilagođen BTCPay Server softverskom paketu.


Mnoge opcije u BTCPay Serveru postoje u nekom obliku ili drugom u drugom softveru povezanom sa Bitcoin Wallet.


### BTCPay Server Ekran za prijavu


Kada uđete u Demo okruženje, od vas se traži da se ‘Prijavite’ ili ‘Kreirate svoj nalog.’ Administratori servera mogu isključiti opciju kreiranja novih naloga iz bezbednosnih razloga. BTCPay Server logotipi i boje dugmadi mogu se promeniti jer je BTCPay Server softver otvorenog koda. Treća strana domaćin može da White-label-uje softver i promeni ceo izgled.


![image](assets/en/0.webp)


### Prozor Kreiraj Nalog


Kreiranje naloga na BTCPay Server-u zahteva validne Email Address stringove; example@email.com bi bio validan string za Email.


Lozinka mora imati najmanje 8 karaktera, uključujući slova, brojeve i specijalne karaktere. Nakon što postavite lozinku, moraćete da potvrdite unetu lozinku kako biste bili sigurni da je ista kao ona uneta u prvo polje za lozinku.


Kada su oba polja, Email i Lozinka, ispravno popunjena, kliknite na dugme 'Kreiraj nalog'. Ovo će sačuvati Email i lozinku na instanci BTCPay Server-a instruktora.


![image](assets/en/1.webp)


**!Note!**


Ako pratite ovaj kurs samostalno, kreiranje ovog naloga bi bilo nešto što biste mogli uraditi na hostu treće strane; stoga, ponovo napominjemo da ih nikada ne koristite kao produkciona okruženja, već samo u svrhe obuke.


### Kreiranje naloga od strane BTCPay Server administratora


Administrator instance BTCPay Servera takođe može kreirati naloge za BTCPay Server. Administrator instance BTCPay Servera može kliknuti na ‘Server Settings’ (1), kliknuti na karticu ‘Users’ (2), i kliknuti na dugme “+ Add User” (3) u gornjem desnom uglu kartice Users. U Cilju (4.3), naučićete više o administratorskoj kontroli Naloga.


![image](assets/en/2.webp)


Kao administrator, potrebno je da imate korisnikov Email Address i postavite standardnu lozinku. Preporučuje se da kao Administrator obavestite korisnika da bi trebalo da promene ovu lozinku pre nego što koriste nalog iz bezbednosnih razloga. Ako Administrator NE postavi lozinku i SMTP je podešen na serveru, korisnik će dobiti email sa pozivnim linkom da kreira svoj nalog i sam postavi lozinku.


### Primer


Kada pratite kurs od strane instruktora, pratite link koji je dao instruktor i kreirajte svoj nalog na obezbeđenom Demo okruženju. Osigurajte da su vaša email adresa Address i lozinka sačuvani na sigurnom mestu; biće vam potrebni ovi podaci za prijavu za ostale ciljeve demonstracije u ovom kursu.


Vaš instruktor je možda unapred prikupio email Address i poslao pozivni link pre ove vežbe. Ako vam je rečeno, proverite svoj Email.


Kada pohađate kurs bez instruktora, kreirajte svoj nalog koristeći BTCPay Server demo okruženje; idite na


https://Mainnet.demo.btcpayserver.org/login.


Ovaj nalog treba koristiti samo za demonstraciju/obuku i nikada za poslovanje.


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Kako kreirati nalog na hostovanom serveru putem Interface.
- Kako administrator servera može ručno dodati korisnike u postavkama servera.


### Procena znanja


#### KA Konceptualni Pregled


Navedite razloge zašto korišćenje Demo Servera nije dobra ideja za produkcijske svrhe.


## Upravljanje korisničkim nalogom/nalozima


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Upravljanje nalozima na BTCPay Serveru


Nakon što vlasnik prodavnice kreira svoj nalog, može ga upravljati u Donjem Levom delu BTCPay Server korisničkog interfejsa. Ispod dugmeta Nalog, postoje višestruka podešavanja višeg nivoa.



- Tamni/Svetli režim.
- Sakrij osetljive informacije.
- Upravljaj Nalogom.


![image](assets/en/3.webp)


### Tamni i Svetli režim


Korisnici BTCPay Server-a mogu birati između Light ili Dark moda verzije korisničkog interfejsa. Stranice okrenute ka korisnicima neće se menjati. One koriste postavke koje preferiraju korisnici u vezi sa tamnim ili svetlim modom.


### Sakrij osetljive informacije


Dugme za skrivanje osetljivih informacija donosi brz i jednostavan Layer nivo sigurnosti. Kad god treba da koristite svoj BTCPay Server, a postoji mogućnost da neko viri preko vašeg ramena u javnom prostoru, uključite Skrivanje osetljivih informacija, i sve vrednosti u BTCPay Server-u će biti skrivene. Neko može da pogleda preko vašeg ramena, ali više ne može da vidi vrednosti sa kojima radite.


### Upravljaj Nalogom


Kada je korisnički nalog kreiran, ovde možete upravljati lozinkama, 2fa ili API ključevima.


### Upravljanje nalogom - Nalog


Opcionalno ažurirajte svoj nalog sa drugačijim Email Address. Da biste osigurali da je vaš email Address tačan, BTCPay Server vam omogućava da pošaljete verifikacioni email. Kliknite na sačuvaj ako korisnik postavi novi email Address i potvrdi da je verifikacija uspela. Korisničko ime ostaje isto kao prethodni Email.


Korisnik može odlučiti da obriše ceo svoj nalog. Ovo se može uraditi klikom na dugme za brisanje na kartici Nalog.


![image](assets/en/4.webp)


**!Napomena!**


Nakon promene Email-a, korisničko ime za nalog neće se promeniti. Prethodno dat Email Address ostaće ime za prijavu.


### Upravljanje nalogom - Lozinka


Student može želeti da promeni svoju lozinku. To može učiniti odlaskom na karticu Lozinka. Ovde je potrebno da unese svoju staru lozinku i može je promeniti u novu.


![image](assets/en/5.webp)


### Dvofaktorska autentifikacija (2fa)


Da biste ograničili posledice ukradene lozinke, možete koristiti dvofaktorsku autentifikaciju (2fa), relativno novi metod zaštite. Možete aktivirati dvofaktorsku autentifikaciju putem Upravljanja nalogom i kartice za dvofaktorsku autentifikaciju. Morate završiti drugi korak nakon prijavljivanja sa svojim korisničkim imenom i lozinkom.


BTCPay Server omogućava dva načina aktiviranja 2FA, 2FA zasnovan na aplikaciji (Authy, Google, Microsoft autentifikatori) ili putem sigurnosnih uređaja (FIDO2 ili LNURL Auth).


### Dvofaktorska autentifikacija - zasnovana na aplikaciji


Na osnovu operativnog sistema vašeg mobilnog telefona (Android ili iOS), korisnici mogu birati između sledećih aplikacija;


1. Preuzmite autentifikator sa dva faktora;


   - Authy za [Android](https://play.google.com/store/apps/details?id=com.authy.authy) ili [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator za [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) ili [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator za [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) ili [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Nakon preuzimanja i instaliranja aplikacije Authenticator.


   - Skenirajte QR kod koji je obezbedio BTCPay Server
   - Ili ručno unesite generisani ključ od strane BTCPay Server-a u vašu aplikaciju Authenticator.

3. Aplikacija Authenticator će vam pružiti jedinstveni kod. Unesite jedinstveni kod u BTCPay Server da biste verifikovali postavku, i kliknite na verifikuj da biste završili proces.


![image](assets/en/6.webp)


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Opcije upravljanja nalogom i različiti načini upravljanja nalogom na instance BTCPay Server-a.
- Kako postaviti dvofaktorsku autentifikaciju zasnovanu na aplikaciji.


### Procena znanja


#### KA Konceptualni Pregled


Opišite kako aplikacija za dvofaktorsku autentifikaciju (2FA) pomaže u zaštiti vašeg naloga.


## Kreiranje nove prodavnice


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Kreiraj čarobnjaka za prodavnicu


Kada se novi korisnik prijavi na BTCPay Server, okruženje je prazno i potrebno je kreirati prvu prodavnicu. Uvodni čarobnjak BTCPay Server-a će korisniku dati opciju da ‘Kreirajte svoju prodavnicu’ (1). Prodavnica se može posmatrati kao Dom za vaše Bitcoin potrebe. Novi BTCPay Server čvor će započeti sa Sinhronizacijom Bitcoin Blockchain (2). U zavisnosti od infrastrukture na kojoj pokrećete BTCPay Server, ovo može trajati od nekoliko sati do nekoliko dana. Trenutna verzija instance prikazana je u donjem desnom uglu vašeg BTCPay Server korisničkog interfejsa. Ovo je korisno za referencu prilikom rešavanja problema.


![image](assets/en/7.webp)


### Kreiraj čarobnjaka za svoju prodavnicu


Praćenje ovog kursa će početi sa malo drugačijim ekranom nego prethodna stranica. Kako je vaš instruktor pripremio Demo okruženje, Bitcoin Blockchain je prethodno sinhronizovan, i stoga nećete videti status sinhronizacije čvorova.


Korisnik može odlučiti da obriše ceo svoj nalog. Ovo se može uraditi klikom na dugme za brisanje na kartici Nalog.


![image](assets/en/8.webp)


**!Napomena!**


BTCPay Server nalozi mogu napraviti neograničen broj prodavnica. Svaka prodavnica je Wallet ili „home“.


### Primer


Započnite klikom na "Kreiraj svoju prodavnicu".


![image](assets/en/9.webp)


Ovo će kreirati vaš prvi Početni ekran i kontrolnu tablu za korišćenje BTCPay servera.


(1) Nakon što kliknete na "Create your store", BTCPay Server će zahtevati da imenujete prodavnicu; ovo može biti bilo šta što vam je korisno.


![image](assets/en/10.webp)


(2) Podrazumevana valuta prodavnice mora biti postavljena sledeće, bilo fiat valuta ili denominovana u Bitcoin / Sats standardu. Za demo okruženje, postavićemo je na USD.


![image](assets/en/11.webp)


(3) Kao poslednji parametar u podešavanju prodavnice, BTCPay Server zahteva da postavite "Preferred price source" kako biste uporedili cenu Bitcoin sa trenutnom fiat cenom, tako da vaša prodavnica prikazuje tačnu Exchange stopu između Bitcoin i fiat valute postavljene u prodavnici. Ostaćemo pri podrazumevanom u Demo primeru i postaviti ovo na Kraken Exchange. BTCPay Server koristi Kraken API za proveru Exchange stopa.


![image](assets/en/12.webp)


(4) Sada kada su ovi parametri prodavnice postavljeni, kliknite na dugme Create, i BTCPay Server će kreirati kontrolnu tablu vaše prve prodavnice, gde će se čarobnjak nastaviti.


![image](assets/en/13.webp)


Čestitamo, kreirali ste svoju prvu prodavnicu, i ovo zaokružuje ovu vežbu.


![image](assets/en/14.webp)


### Sažetak veština


U ovom odeljku ste naučili:



- Kreiranje prodavnice i konfigurisanje podrazumevane valute u kombinaciji sa preferencijama izvora cena.
- Svaka "Prodavnica" je novi dom odvojen od drugih prodavnica na ovoj instalaciji BTCPay Server-a.


# Uvod u obezbeđivanje Bitcoin ključeva


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Razumevanje generisanja ključeva Bitcoin


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Šta je uključeno u generisanje Bitcoin ključeva?


Bitcoin novčanici, kada se kreiraju, kreiraju takozvani "seed". U poslednjem cilju, kreirali ste "seed". Niz reči generisanih ranije takođe je poznat kao Mnemonic fraze. seed se koristi za izvođenje pojedinačnih Bitcoin Ključeva i koristi se za slanje ili primanje Bitcoin. seed fraze nikada ne bi trebalo deliti sa trećim stranama ili nepouzdanim osobama.


seed generacija je urađena prema industrijskom standardu poznatom kao "Hijerarhijski Deterministički" (HD) okvir.


![image](assets/en/15.webp)


### Adrese


BTCPay Server izgrađen na generate novi Address. Ovo ublažava problem ponovne upotrebe javnog ključa ili Address. Korišćenje istog javnog ključa čini praćenje vaše celokupne istorije plaćanja veoma lakim. Razmišljanje o ključevima kao o vaučerima za jednokratnu upotrebu značajno bi poboljšalo vašu privatnost. Takođe koristimo Bitcoin adrese, nemojte ih mešati sa javnim ključevima.


Address se dobija iz javnog ključa putem „algoritma heširanja“. Većina novčanika i transakcija, međutim, prikazuje Adrese umesto tih javnih ključeva. Adrese su, uopšteno, kraće od javnih ključeva i obično počinju sa `1`, `3` ili `bc1`, dok javni ključevi počinju sa `02`, `03` ili `04`.



- Adrese koje počinju sa `1.....` su i dalje veoma uobičajene adrese. Kao što je pomenuto u poglavlju Kreiranje nove prodavnice, ovo su nasleđene adrese. Ovaj tip Address je namenjen za P2PKH transakcije. P2Pkh koristi Base58 kodiranje, što čini Address osetljivim na velika i mala slova. Njegova struktura se zasniva na javnom ključu sa dodatnom 1 cifrom kao identifikatorom.



- Adrese koje počinju sa `bc1...` polako postaju veoma uobičajene adrese. One su poznate kao (native) SegWit adrese. Ove adrese nude bolju strukturu naknada od drugih pomenutih adresa. Native SegWit adrese koriste Bech32 kodiranje i dozvoljavaju samo mala slova.



- Adrese koje počinju sa `3...` i dalje se često koriste od strane menjačnica za adrese depozita. Ove adrese su pomenute u poglavlju Kreiranje nove prodavnice, obavijene ili ugnježdene SegWit adrese. Međutim, one takođe mogu funkcionisati kao "Multisig Address". Kada se koriste kao SegWit Address, ponovo dolazi do uštede na troškovima transakcija, ali manje nego kod Native SegWit. P2SH Adrese koriste Base58 kodiranje. Ovo ih čini osetljivim na velika i mala slova, kao i nasleđene Address.



- Adrese koje počinju sa `2...` su Testnet adrese. One su namenjene za primanje Testnet Bitcoin (tBTC). Nikada ne bi trebalo da pomešate ovo i pošaljete Bitcoin na ove adrese. Za potrebe razvoja, možete generate Testnet Wallet. Postoji više slavina na mreži za dobijanje Testnet Bitcoin. Nikada ne kupujte Testnet Bitcoin. Testnet Bitcoin se rudari. Ovo može biti razlog da programer koristi Regtest umesto toga. Ovo je okruženje za igru za programere, koje nedostaje određenim mrežnim komponentama. Bitcoin je, međutim, za razvojne svrhe, veoma koristan.


### Javni ključevi


Javni ključevi se danas manje koriste u praksi. Vremenom su ih korisnici Bitcoin zamenjivali Adresama. Oni i dalje postoje i povremeno se koriste. Javni ključevi su, uopšteno, mnogo duži nizovi od adresa. Kao i kod adresa, počinju sa specifičnim identifikatorom.



- Prvo, `02...` i `03...` su veoma standardni identifikatori javnih ključeva kodirani u SEC formatu. Oni se mogu obraditi i pretvoriti u adrese za primanje, koristiti za kreiranje multi-sig adresa, ili za verifikaciju potpisa. Rane Bitcoin transakcije koristile su javne ključeve kao deo P2PK transakcija.



- HD novčanici, međutim, koriste drugačiju strukturu. `xpub...`, `ypub...` ili `zpub...` se nazivaju proširenim javnim ključevima, odnosno xpubs. Ovi ključevi se koriste za izvođenje mnogih javnih ključeva kao deo HD Wallet. Pošto vaš xpub sadrži zapise vaše celokupne istorije, što znači prošlih i budućih transakcija, nikada ih ne delite sa nepouzdanim stranama.


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Razlike između tipova podataka adresa i javnih ključeva i prednosti korišćenja adresa u odnosu na javne ključeve.


### Procena znanja


Opiši prednost korišćenja svežih adresa za svaku transakciju u poređenju sa ponovnom upotrebom Address ili metodama javnog ključa.


## Osiguravanje ključeva sa Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Čuvanje Bitcoin ključeva


Nakon generisanja seed fraze, lista od 12 - 24 reči generisanih u ovoj knjizi zahteva odgovarajuće bekapove i sigurnost, jer su ove reči jedini način za povratak pristupa Wallet. Struktura HD novčanika i kako generiše adrese deterministički koristeći taj jedan seed, sve vaše kreirane adrese će biti bekapovane koristeći ovu jednu listu Mnemonic reči koje predstavljaju vaš seed ili frazu za oporavak.


Čuvajte svoju frazu za oporavak na sigurnom mestu. Ako neko, posebno sa zlonamernim namerama, dođe do nje, može da premesti vaša sredstva. Čuvanje seed na sigurnom i bezbednom mestu, ali i pamćenje iste, međusobno su povezani. Postoji nekoliko metoda za čuvanje privatnih ključeva Bitcoin, od kojih svaka ima svoje prednosti i nedostatke, bilo u pogledu sigurnosti, privatnosti, praktičnosti ili fizičkih sredstava. Zbog važnosti privatnih ključeva, korisnici Bitcoin obično čuvaju i bezbedno drže te ključeve u "samostalnom staranju" umesto korišćenja "starateljskih" usluga poput banaka. U zavisnosti od korisnika, on mora koristiti ili Cold rešenje za skladištenje ili Hot Wallet.


### Hot i Cold skladištenje ključeva Bitcoin


Obično su Bitcoin novčanici denominovani u Hot Wallet ili Cold Wallet. Većina kompromisa leži u pogodnosti, jednostavnosti korišćenja i bezbednosnim rizicima. Svaka od ovih metoda može se videti i u rešenju sa skrbnikom. Međutim, kompromisi ovde su uglavnom zasnovani na bezbednosti i privatnosti i prevazilaze okvire ovog kursa.


### Hot Wallet


Hot novčanici su najprikladniji način za interakciju sa Bitcoin putem mobilnog, web ili desktop softvera. Wallet je uvek povezan na internet, omogućavajući korisnicima slanje ili primanje Bitcoin. Međutim, to je ujedno i njegova slabost, jer je Wallet, budući da je uvek online, sada podložniji napadima hakera ili zlonamernog softvera na vašem uređaju. U BTCPay Server-u, Hot novčanici čuvaju privatne ključeve na instanci. Svako ko pristupi vašoj BTCPay Server prodavnici mogao bi ukrasti sredstva iz ovog Address ako je zlonameran. Kada BTCPay Server radi u hostovanom okruženju, uvek bi trebalo da uzmete ovo u obzir u svom bezbednosnom profilu i po mogućstvu ne koristiti Hot-Wallet u takvom slučaju. Kada je BTCPay Server instaliran na sopstvenom hardveru, osiguranom i pouzdanom od strane vas, profil rizika se značajno smanjuje, ali nikada ne nestaje!


### Cold Wallet


Pojedinci prebacuju svoj Bitcoin u Cold Wallet jer može izolovati privatne ključeve od interneta. Uklanjanje internet konekcije iz jednačine smanjuje rizik od malvera, špijunskog softvera i zamene SIM kartica. Veruje se da je Cold skladištenje superiornije od Hot skladištenja u pogledu sigurnosti i autonomije, pod uslovom da se preduzmu adekvatne mere predostrožnosti kako bi se izbegao gubitak privatnih ključeva Bitcoin. Cold skladištenje je najpogodnije za velike količine Bitcoin, koje nisu namenjene za čestu potrošnju zbog složenosti Wallet postavke.


Postoji više metoda kako sačuvati Bitcoin ključeve u Cold skladištu, od papirnih novčanika do memorijskih novčanika, hardverskih novčanika, ili, od početka, Wallet datoteke. Većina novčanika koristi BIP 39 za generate seed frazu. Međutim, unutar Bitcoin osnovnog softvera, konsenzus još nije postignut o njegovom korišćenju. Bitcoin osnovni softver će i dalje generate Wallet.dat datoteku koju treba da čuvate na sigurnom offline mestu.


### Sažetak veština


U ovom odeljku, naučili ste:



- Razlike između novčanika Hot i Cold u pogledu funkcionalnosti i njihovih kompromisa.


### Provera znanja Konceptualni pregled



- Šta je Wallet?



- Koja je razlika između Hot i Cold novčanika?



- Opisati šta znači "generisati Wallet"?


## Korišćenje vaših Bitcoin ključeva


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay Server Wallet


BTCPay Server se sastoji od sledećih standardnih Wallet funkcija:



- Transakcije
- Pošalji
- Primiti
- Ponovno skeniraj
- Povuci Plaćanja
- Isplate
- PSBT
- Opšta podešavanja


### Transakcije


Administratori mogu videti dolazne i odlazne transakcije za On-Chain Wallet povezane sa ovom specifičnom prodavnicom u prikazu transakcija. Svaka transakcija ima razliku između primljenih i poslatih. Primljene će biti Green, a odlazne transakcije će biti crvene. U okviru prikaza transakcija na BTCPay Server-u, administratori će takođe videti skup standardnih oznaka.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Kako poslati


Funkcija slanja BTCPay servera šalje transakcije sa vašeg BTCPay Server On-Chain Wallet. BTCPay Server omogućava više načina potpisivanja vaših transakcija za trošenje sredstava. Transakcija može biti potpisana sa;



- Hardware Wallet
- Novčanici koji podržavaju PSBT
- HD privatni ključ ili fraze za oporavak.
- Hot Wallet


#### Hardware Wallet


BTCPay Server ima ugrađenu podršku za Hardware Wallet koja vam omogućava da koristite vaš Hardware Wallet sa BTCPay Vault-om bez curenja informacija ka aplikacijama ili serverima trećih strana. Integracija Hardware Wallet unutar BTCPay Server-a omogućava vam da uvezete vaš Hardware Wallet i trošite dolazna sredstva jednostavnom potvrdom na vašem uređaju. Vaši privatni ključevi nikada ne napuštaju uređaj, a sva sredstva se validiraju u odnosu na vaš Full node tako da nema curenja podataka.


#### Potpisivanje sa Wallet podržava PSBT


PSBT (Delimično potpisane Bitcoin transakcije) je format za razmenu Bitcoin transakcija koje još uvek nisu u potpunosti potpisane. PSBT je podržan u BTCPay Server-u i može se potpisati kompatibilnim hardverskim i softverskim novčanicima.


Izgradnja potpuno potpisane Bitcoin transakcije prolazi kroz sledeće korake:



- PSBT se konstruira sa specifičnim ulazima i izlazima, ali bez potpisa
- Izvezeni PSBT može biti uvezen od strane Wallet koji podržava ovaj format
- Podaci o transakciji mogu se pregledati i potpisati pomoću Wallet
- Potpisana datoteka PSBT se izvozi iz Wallet i uvozi sa BTCPay Server
- BTCPay Server proizvodi konačnu Bitcoin transakciju
- Verifikujete rezultat i emitujete ga na mrežu.


#### Potpisivanje sa HD privatnim ključem ili Mnemonic seed


Ako ste ranije kreirali Wallet koristeći BTCPay Server, možete potrošiti sredstva unosom vašeg privatnog ključa u odgovarajuće polje. Postavite odgovarajući "AccountKeyPath" u Wallet> Postavke; u suprotnom, ne možete potrošiti.


#### Potpisivanje sa Hot Wallet


Ako ste kreirali novi Wallet prilikom postavljanja vaše prodavnice i omogućili ga kao Hot Wallet, automatski će koristiti seed sačuvan na serveru za potpisivanje.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) je funkcija protokola Bitcoin koja vam omogućava da zamenite prethodno emitovanu transakciju (dok je još nepotvrđena). Ovo omogućava nasumično menjanje otiska transakcije vašeg Wallet ili njenu zamenu sa višom stopom naknade kako bi se transakcija pomerila više u redu prioriteta za potvrdu (Mining). Ovo će efikasno zameniti originalnu transakciju jer će viša stopa naknade biti prioritetizovana, i kada bude potvrđena, poništiće originalnu (nema dvostruke potrošnje).


Pritisnite dugme "Advanced Settings" da biste videli opcije RBF;


![image](assets/en/16.webp)



- Nasumično za veću privatnost, Omogućava da se transakcija automatski zameni za nasumično menjanje otiska prsta transakcije.
- Da, označi transakciju za RBF i zameni je eksplicitno (Ne zamenjuje se podrazumevano, samo unosom)
- Ne, ne dozvoli da transakcija bude zamenjena.


### Izbor novčića


Izbor novčića je napredna funkcija za poboljšanje privatnosti koja vam omogućava da izaberete novčiće koje želite da potrošite prilikom kreiranja transakcije. Na primer, plaćanje novčićima koji su sveže iz mešavine.


Izbor novčića radi prirodno sa funkcijom Wallet oznaka. Ovo vam omogućava da označite dolazna sredstva za lakše upravljanje i trošenje UTXO.


BTCpay Server takođe podržava BIP-329 za upravljanje etiketama. BIP-329 omogućava etikete na; ako prenesete sa Wallet koji podržava ovaj određeni BIP i postavite etikete, BTCPay Server će ih prepoznati i uvesti. Kada migrirate servere, ove informacije se takođe mogu izvesti i uvesti u novo okruženje.


### Kako primiti


Kada kliknete na dugme za primanje u BTCPay Server-u, generiše se neiskorišćeni Address koji se može koristiti za primanje uplata. Administratori takođe mogu generate novi Address generisanjem novog „Invoice.“


BTCPay Server će uvek tražiti da generate sledeći dostupni Address kako bi se izbegla ponovna upotreba Address. Nakon klika na “generate next available BTC Address,” BTCPay Server je generisao novi Address i QR. Takođe vam omogućava da direktno postavite Oznaku na Address za bolje upravljanje vašim adresama.


![image](assets/en/17.webp)


![image](assets/en/18.webp)


#### Ponovno skeniraj


Funkcija ponovnog skeniranja oslanja se na Bitcoin Core 0.17.0 “Scantxoutset” kako bi skenirala trenutno stanje Blockchain (nazvanog UTXO Set) za novčiće koji pripadaju konfigurisanom derivacionom šemu. Wallet ponovni sken rešava dva problema sa kojima se korisnici BTCPay Server-a suočavaju.


1. Problem sa ograničenjem praznina - Većina novčanika trećih strana su laki novčanici koji dele čvor između mnogih korisnika. Laki i Full node-zavisni novčanici ograničavaju broj (obično 20) adresa bez salda koje prate na Blockchain kako bi sprečili probleme sa performansama. BTCPay Server generiše novi Address za svaki Invoice. Imajući u vidu navedeno, nakon što BTCPay Server generiše 20 uzastopnih neplaćenih faktura, eksterni Wallet prestaje da preuzima transakcije, pretpostavljajući da nije bilo novih transakcija. Vaš eksterni Wallet ih neće prikazati kada fakture budu plaćene na 21., 22., itd. S druge strane, interno, BTCPay Server Wallet prati svaki Address koji generiše zajedno sa mnogo većim ograničenjem praznina. Ne oslanja se na treću stranu i uvek može prikazati tačan saldo.

2. Rešenje za gap limit - Ako vaš [eksterni/postojeći Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) omogućava konfiguraciju gap limita, jednostavno rešenje je da ga povećate. Međutim, većina novčanika to ne dozvoljava. Jedini novčanici za koje znamo da omogućavaju konfiguraciju gap limita su Electrum, Wasabi i Sparrow Wallet. Nažalost, verovatno ćete naići na problem sa mnogim drugim novčanicima. Za najbolje korisničko iskustvo i privatnost, razmislite o napuštanju eksternih novčanika i korišćenju internog BTCPay Server Wallet.


#### BTCPay Server koristi “mempoolfullrbf=1”


BTCPay Server koristi “mempoolfullrbf=1”; dodali smo ovo kao podrazumevanu opciju u vašu BTCPay Server postavku. Međutim, takođe smo napravili fragment koji možete sami onemogućiti. Bez “mempoolfullrbf=1,” ako kupac dvostruko potroši uplatu transakcijom koja ne signalizira RBF, Trgovac bi to saznao tek nakon potvrde.


Administrator može želeti da isključi ovu postavku. Pomoću sledećeg niza možete promeniti podrazumevanu postavku.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```


### Postavke BTCPay Server Wallet


Postavke Wallet unutar BTCPay Server-a pružaju jasan i brz pregled opštih postavki vašeg Wallet. Sve ove postavke su unapred popunjene ako je Wallet kreiran sa BTCPay Server-om.


![image](assets/en/19.webp)


Postavke Wallet unutar BTCPay Server-a pružaju jasan i brz pregled opštih postavki vašeg Wallet. Sve ove postavke su unapred popunjene ako je Wallet kreiran sa BTCPay Server-om. Postavke Wallet u BTCPay Server-u počinju sa statusom Wallet. Da li je to samo za gledanje ili Hot Wallet? U zavisnosti od tipa Wallet, akcije mogu varirati od ponovnog skeniranja Wallet za nedostajuće transakcije, obrezivanja starih transakcija iz istorije, registracije Wallet za platne linkove, ili zamene i brisanja trenutnog Wallet povezanog sa prodavnicom. U postavkama Wallet BTCPay Server-a, administratori mogu postaviti Oznaku za Wallet radi boljeg upravljanja Wallet. Ovde će Administrator takođe moći da vidi Šemu Derivacije, ključ naloga (xpub), Otisak prsta i Putanju ključa. Plaćanja u postavkama Wallet imaju samo 2 glavne postavke. Plaćanje je nevažeće ako transakcija ne uspe da se potvrdi u (postavljenim minutima) nakon isteka Invoice. Smatrajte Invoice potvrđenim kada transakcija plaćanja ima X broj potvrda. Administratori takođe mogu postaviti prekidač za prikaz preporučenih naknada pri plaćanjima ili postaviti ručni cilj potvrde u broju blokova.


![image](assets/en/20.webp)


**!Napomena!**


Ako pratite ovaj kurs samostalno, kreiranje ovog naloga bi moglo biti nešto što ćete uraditi na hostu treće strane, stoga ponovo napominjemo da ih nikada ne koristite kao produkciona okruženja, već samo za svrhe obuke.


### Primer


#### Postavljanje Bitcoin Wallet u BTCPay Server


BTCPay Server omogućava dva načina postavljanja Wallet. Jedan način je uvoz već postojećeg Bitcoin Wallet. Uvoz se može izvršiti povezivanjem Hardware Wallet, uvozom Wallet datoteke, unosom proširenog javnog ključa, skeniranjem QR koda Wallet, ili najmanje poželjno, ručnim unosom prethodno kreiranog Wallet oporavka seed. U BTCPay Server-u je takođe moguće kreirati novi Wallet. Postoje dva moguća načina konfiguracije BTCPay Server-a prilikom generisanja novog Wallet.


Opcija Hot Wallet u BTCPay Server-u omogućava funkcije poput 'PayJoin' ili 'Liquid'. Međutim, postoji nedostatak, recovery seed generisan za ovaj Wallet biće sačuvan na serveru, gde bilo ko ko ima Admin kontrolu može dohvatiti recovery seed. Kako je vaš privatni ključ izveden iz vašeg recovery seed, zlonamerni akter bi mogao dobiti pristup vašim trenutnim i budućim sredstvima!


Da bi se smanjio takav rizik u BTCPay Server-u, administrator može postaviti u Podešavanja servera > Politike > "Dozvoli ne-administratorima da kreiraju Hot novčanike za svoje prodavnice" na ne, što je podrazumevano. Da bi se poboljšala sigurnost tih Hot novčanika, administrator servera treba da omogući 2FA autentifikaciju na nalozima kojima je dozvoljeno da imaju Hot novčanike. Čuvanje privatnih ključeva na javnom serveru je opasno i nosi rizike. Neki su slični rizicima Lightning Network (pogledajte sledeće poglavlje za rizike Lightning Network).


Druga opcija koju BTCPay Server nudi za generisanje novog Wallet je kreiranjem Watch-only wallet. BTCPay Server će generate vaše privatne ključeve jednom. Nakon što korisnik potvrdi da je zapisao svoju seed frazu, BTCPay Server će obrisati privatne ključeve sa servera. Kao rezultat, vaša prodavnica sada ima Watch-only Wallet povezan sa njom. Da biste potrošili sredstva primljena na vašem Watch-only wallet, pogledajte poglavlje Kako poslati, bilo korišćenjem BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction), ili, najmanje preporučeno, ručnim unosom vaše seed fraze.


Kreirali ste novu 'Prodavnicu' u poslednjem delu. Čarobnjak za instalaciju će nastaviti tako što će vas pitati da "Postavite Wallet" ili "Postavite Lightning čvor". U ovom primeru, pratićete proces čarobnjaka "Postavite Wallet" (1).


![image](assets/en/21.webp)


Nakon što kliknete na "Set up a Wallet", čarobnjak će nastaviti tako što će vas pitati kako želite da nastavite; BTCPay Server sada nudi opciju povezivanja postojećeg Bitcoin Wallet sa vašom novom prodavnicom. Ako nemate Wallet, BTCPay Server predlaže kreiranje novog. Ovaj primer će pratiti korake za “create a new Wallet” (2). Pratite korake da naučite kako da "Connect an existing Wallet (1).


![image](assets/en/22.webp)


**!Napomena!**


Ako pohađate ovaj kurs u učionici, trenutni primer i seed koji smo generisali su samo u obrazovne svrhe. Nikada ne bi trebalo da postoji bilo koji značajan iznos osim onog koji je potreban tokom vežbi na ovim adresama.


(1) Nastavite čarobnjak „New Wallet“ klikom na dugme „Create a new Wallet“.


![image](assets/en/23.webp)


(2) Nakon što kliknete na “Kreiraj novi Wallet,” sledeći prozor u čarobnjaku će ponuditi opcije “Hot Wallet” i “Watch-only wallet.” Ako pratite zajedno sa instruktorom, vaše okruženje je deljeni Demo, i možete kreirati samo Watch-only wallet. Obratite pažnju na razliku između obe slike ispod. Kako ste u Demo okruženju i pratite zajedno sa instruktorom, kreirajte "Watch-only wallet" i nastavite sa čarobnjakom "Novi Wallet."


![image](assets/en/24.webp)


![image](assets/en/25.webp)


(3) Nastavljajući novi Wallet čarobnjak, sada ste u odeljku Kreiraj BTC Watch-only wallet. Ovde možemo postaviti Wallet "Address tip" BTCPay Server vam omogućava da izaberete svoj preferirani Address tip; od trenutka pisanja ovog kursa, i dalje se preporučuje korišćenje bech32 adresa. Saznajte više detalja o adresama u prvom poglavlju ovog dela.



- SegWit (bech32)
  - Native SegWit su adrese koje počinju sa `bc1q`.
  - Primer: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legat
  - Legacy adrese su adrese koje počinju brojem `1`.
  - Primer: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Za napredne korisnike)
  - Taproot adrese počinju sa `bc1p`.
  - Primer: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit umotan
  - SegWit wrapped su adrese koje počinju sa `3`.
  - Primer: `37BBXXXXXXXXXXXXXXX`


Izaberite SegWit (preporučeno) kao vaš preferirani Wallet Address tip.


![image](assets/en/26.webp)


(4) Kada postavljate parametar za Wallet, BTCPay Server omogućava korisnicima da postave opcionalni passphrase putem BIP39, obavezno potvrdite vašu lozinku.


![image](assets/en/27.webp)


(5) Nakon što postavite Wallet tipa Address i eventualno postavite neke napredne opcije, kliknite na Create, i BTCPay Server će generate vaš novi Wallet. Imajte na umu da je ovo poslednji korak pre generisanja vaše seed fraze. Uverite se da ovo radite samo u okruženju gde niko ne može ukrasti seed frazu gledajući u vaš ekran.


![image](assets/en/28.webp)


(6) Na sledećem ekranu čarobnjaka, BTCPay Server vam prikazuje Recovery seed frazu za vaš novo generisani Wallet; ovo su ključevi za oporavak vašeg Wallet i potpisivanje transakcija. BTCPay Server generiše seed frazu od 12 reči. Ove reči će biti izbrisane sa servera nakon ovog ekrana za podešavanje. Ovaj Wallet je specifično Watch-only wallet. Preporučuje se da se seed fraza ne čuva digitalno ili putem fotografske slike. Korisnici mogu nastaviti dalje u čarobnjaku samo ako aktivno potvrde da su zapisali svoju seed frazu.


![image](assets/en/29.webp)


(7) Nakon što kliknete na Done i osigurate novogenerisanu Bitcoin seed frazu, BTCPay Server će ažurirati vašu prodavnicu sa priloženim novim Wallet i spreman je za primanje uplata. U Korisničkom Interface, u levom navigacionom meniju, primetite kako je Bitcoin sada istaknut i aktiviran ispod Wallet.


![image](assets/en/30.webp)


### Primer: Pisanje seed fraze


Ovo je veoma poseban i siguran trenutak za korišćenje Bitcoin. Kao što je ranije pomenuto, samo vi treba da imate pristup ili znanje o vašoj seed frazi. Dok pratite instruktora i učionicu, seed generisana treba da se koristi samo u ovom kursu. Previše faktora, radoznali pogledi od strane kolega iz razreda, nesigurni sistemi i mnogi drugi čine ove ključeve samo edukativnim i nepouzdanim. Međutim, generisani ključevi i dalje treba da budu sačuvani za primere na kursu.


Prva metoda koju ćemo koristiti u trenutnoj situaciji, takođe najmanje sigurna, jeste zapisivanje seed fraze u ispravnom redosledu. Kartica sa seed frazom nalazi se u materijalu kursa koji je obezbeđen studentu ili se može pronaći na BTCPay Server GitHub-u. Koristićemo ovu karticu da zapišemo reči generisane u prethodnom koraku. Obavezno ih zapišite u tačnom redosledu. Nakon što ih zapišete, proverite ih u odnosu na ono što je dato od strane softvera kako biste bili sigurni da ste ih zapisali u ispravnom redosledu. Kada ih zapišete, označite polje za potvrdu koje navodi da ste pravilno zapisali svoju seed frazu.


### Primer: Skladištenje fraze seed na Hardware Wallet


U ovom kursu, dotičemo se čuvanja seed fraze na Hardware Wallet. Praćenje ovog kursa od strane instruktora možda neće uvek uključivati takav uređaj. U kursu, materijali za vođenje su napisali listu hardverskih novčanika koji bi odgovarali ovoj vežbi.


U ovom primeru ćemo koristiti BTCPay Server vault i Blockstream Jade Hardware Wallet.


Takođe možete pratiti putem video snimka kao referencu za povezivanje Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Preuzmite BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Obavezno preuzmite ispravne datoteke za vaš sistem. Korisnici Windows-a treba da preuzmu paket [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), korisnici Mac-a preuzimaju [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), a korisnici Linux-a treba da preuzmu [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Nakon instalacije BTCPay Server Vault-a, pokrenite softver klikom na ikonu na vašoj radnoj površini. Kada je BTCPay Server Vault pravilno instaliran i pokrenut po prvi put, zatražiće dozvolu za korišćenje sa Web aplikacijama. Zatražiće da odobrite pristup specifičnom BTCPay Server-u sa kojim radite. Prihvatite ove uslove. BTCPay Server Vault će sada tražiti Hardverski uređaj. Kada uređaj bude pronađen, BTCPay Server će prepoznati da Vault radi i da je preuzeo vaš uređaj.


**!Napomena!**


Ne dajte svoje SSH ključeve ili administratorski nalog servera nikome osim administratorima kada koristite Hot Wallet. Svako ko ima pristup ovim nalozima imaće pristup sredstvima u Hot Wallet.


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Transakcioni prikaz Bitcoin Wallet i njegove različite kategorizacije.
- Različite opcije su dostupne prilikom slanja sa Bitcoin Wallet, od hardvera do Hot novčanika.
- Problem limita praznine sa kojim se suočavaju većina novčanika, i kako to ispraviti.
- Kako generate novi Bitcoin Wallet unutar BTCPay Server-a, uključujući čuvanje ključeva u Hardware Wallet i pravljenje rezervne kopije fraze za oporavak.


U ovom cilju, naučili ste kako da generate novi Bitcoin Wallet unutar BTCPay Server-a. Još nismo prešli na to kako obezbediti ili koristiti te ključeve. U brzom pregledu ovog cilja, naučili ste kako da postavite prvu prodavnicu. Naučili ste kako da generate Bitcoin Recovery seed frazu.


### Praktični pregled procene znanja


Opiši metodu za generisanje ključeva i šemu za njihovo osiguranje, zajedno sa kompromisima/risicima šeme sigurnosti.


## BTCPay Server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Kada administrator servera obezbedi novu BTCPay Server instancu, može postaviti Lightning Network implementaciju, LND, Core Lightning, ili Eclair; pogledajte deo Konfigurisanje BTCPay Server-a za detaljnija uputstva za instalaciju.


Ako se prati u učionici, povezivanje Lightning čvora sa vašim BTCPay Serverom funkcioniše preko Custom čvora. Korisnik koji nije administrator servera na BTCPay Serveru neće moći da koristi interni Lightning čvor po defaultu. Ovo je da bi se zaštitio vlasnik servera od gubitka sredstava. Administratori servera mogu instalirati Plugin kako bi omogućili pristup svom Lightning čvoru preko LNBank; ovo je van okvira ove knjige; pročitajte više o LNBank na zvaničnoj stranici plugina.


### Poveži interni čvor (administrator servera)


Administrator servera može koristiti interni Lightning čvor BTCPay Server-a. Bez obzira na Lightning implementaciju, povezivanje sa internim Lightning čvorom je isto.


Goto a previous setup store, and click on the "Lightning" Wallet in the left menu. BTCPay Server gives two setup possibilities, Using the Internal node (Server admin only by default) or a custom node (external connection). Server administrators can click on the "Use internal node" option. There is no further configuration required. Click the "save" button and notice the notification stating, "BTC Lightning node updated". The store has now successfully got Lightning Network capabilities.


### Povežite eksterni čvor (server korisnik/vlasnik prodavnice)


Po podrazumevanoj vrednosti, vlasnicima prodavnica nije dozvoljeno da koriste Lightning Node server administratora. Potrebno je uspostaviti vezu sa eksternim čvorom, bilo sa čvorom koji je u vlasništvu vlasnika prodavnice pre postavljanja BTCPay Server-a, LNBank dodatkom ako ga obezbedi server administrator, ili sa kustodijalnim rešenjem kao što je Alby.


Idite u prethodno podešenu prodavnicu i kliknite na "Lightning" ispod novčanika u levom meniju. Pošto vlasnicima prodavnica nije dozvoljeno da koriste interni čvor po defaultu, ova opcija je zasivljena. Korišćenje prilagođenog čvora je jedina opcija koja je po defaultu dostupna vlasnicima prodavnica.


BTCPay Server treba informacije o povezivanju; prethodno napravljeno (ili rešenje sa skrbnikom) će dostaviti ove informacije specifične za implementaciju Lightning-a. Unutar BTCPay Server-a, vlasnici prodavnica mogu koristiti sledeće veze;



- C-lightning putem TCP ili Unix domen soket konekcije.
- Lightning Charge putem HTTPS-a
- Eclair putem HTTPS
- LND putem REST proxyja
- LNDhub putem REST API-ja


![image](assets/en/31.webp)


Kliknite "testiraj vezu" da biste osigurali da ste ispravno uneli detalje veze. Nakon što se potvrdi da je veza dobra, kliknite sačuvaj, i BTCPay Server će prikazati da je prodavnica ažurirana sa Lightning Node-om.


### Upravljanje internim Lightning čvorom LND (Administrator servera)


Nakon povezivanja internog Lightning čvora, administratori servera će primetiti nove pločice na Kontrolnoj tabli specifično za informacije o Lightning-u.



- Lightning Balance
- BTC u kanalima
  - BTC otvaranje kanala
  - BTC lokalni balans
  - BTC udaljena ravnoteža
  - BTC zatvaranje kanala
- BTC On-Chain
  - BTC potvrđeno
  - BTC nepotvrđeno
  - BTC rezervisano
- Lightning Services
  - Vozi munju (RTL).


Klikom na Ride the Lightning Logo u pločici "Lightning services" ili na "Lightning" ispod novčanika u levom meniju, administratori servera mogu pristupiti RTL-u za upravljanje Lightning čvorom.


**Napomena!**


Povezivanje sa internim Lightning čvorom nije uspelo - Ako interna veza ne uspe, potvrdite:


1. Bitcoin On-Chain čvor je potpuno sinhronizovan

2. Interni čvor za Lightning je "Omogućen" pod "Lightning" > "Postavke" > "BTC Lightning Postavke"


Ako ne možete da se povežete sa vašim Lightning čvorom, pokušajte da restartujete vaš server, ili pročitajte više detalja u zvaničnoj dokumentaciji BTCPay Server-a; https://docs.btcpayserver.org/Troubleshooting/ . Ne možete prihvatati lightning uplate u vašoj prodavnici dok se vaš Lightning čvor ne pojavi kao "Online". Pokušajte da testirate vašu Lightning konekciju klikom na link "Public Node Info"


### Lightning Wallet


U okviru opcije Lightning Wallet u levoj traci menija, administratori servera će pronaći lak pristup RTL-u, informacijama o njihovom javnom čvoru i podešavanjima Lightning-a specifičnim za njihovu BTCPay Server prodavnicu.


#### Informacije o internom čvoru


Administratori servera mogu kliknuti na informacije o internom čvoru i baciti pogled na status svog servera (Online/Offline) i string za povezivanje za Clearnet ili Tor.


![image](assets/en/32.webp)


#### Promeni vezu


Ako vlasnik prodavnice odluči da koristi promenjeno unutar Lightning Settings - Promeni vezu.

Pored prodavnice informacija o javnom čvoru, vlasnici mogu pronaći ovu opciju. Ona će vratiti početno podešavanje za povezivanje sa eksternim čvorom munje, popuniti nove informacije o čvoru munje, kliknuti na sačuvaj i ažurirati prodavnicu sa novim informacijama o čvoru.


![image](assets/en/33.webp)


#### Usluge


Ako administrator servera odluči da instalira više usluga za implementaciju Lightning-a, one će biti navedene ovde. Sa standardnom LND implementacijom, administratori će imati Ride The Lightning (RTL) kao standardni alat za upravljanje čvorovima.


#### BTC Lightning Wallet postavke


Nakon dodavanja Lightning čvora u prodavnicu u prethodnom koraku, unutar postavki Lightning Wallet, vlasnici prodavnica i dalje mogu da ga deaktiviraju za svoju prodavnicu koristeći prekidač na vrhu Lightning postavki.


![image](assets/en/34.webp)


#### Opcije Lightning plaćanja


Vlasnici prodavnica mogu postaviti parametre za sledeće kako bi poboljšali Lightning iskustvo za svoje kupce.



- Prikaži iznose Lightning plaćanja u Satoshijima.
- Dodajte hop hints za privatne kanale na Lightning Invoice.
- Objediniti On-Chain i Lightning URL/QR kodove za plaćanje pri naplati.
- Postavite šablon opisa za lightning fakture.


#### LNURL


Vlasnici prodavnica mogu da izaberu da li će koristiti ili ne koristiti LNURL. Lightning Network URL, ili LNURL, je predloženi standard za interakcije između Lightning platioca i primaoca. Ukratko, LNURL je bech32 kodiran URL sa prefiksom lnurl. Očekuje se da Lightning Wallet dekodira URL, kontaktira URL i sačeka JSON objekat sa daljim instrukcijama, najznačajnije tag koji definiše ponašanje knurl-a.



- Omogući LNURL
- LNURL Klasični Režim
  - Za kompatibilnost sa Wallet, Bech32 kodirano (klasično) naspram čistog URL-a (nadolazeće)
- Dozvoli primaocu da ostavi komentar.


### Primer 1


#### Povežite se sa Lightning-om pomoću internog čvora (Administrator)


Ova opcija je dostupna samo ako ste Administrator ove instance ili ako je Administrator promenio podrazumevana podešavanja gde korisnici mogu koristiti interni lightning čvor.


Kao administrator, kliknite na Lightning Wallet u levom meniju. BTCPay Server će tražiti da koristite jednu od dve opcije za povezivanje Lightning Node-a, Interni čvor ili prilagođeni eksterni čvor. Kliknite na Koristi interni čvor i kliknite na sačuvaj.


#### Upravljanje vašim Lightning čvorom (RTL)


Nakon povezivanja sa internim lightning čvorom, BTCPay Server će se ažurirati i prikazati obaveštenje "BTC Lightning čvor ažuriran", potvrđujući da ste sada povezali Lightning sa vašom prodavnicom.


Upravljanje čvorom munje je zadatak Administratora servera. Ovo uključuje.



- Upravljaj transakcijom
- Upravljanje likvidnošću
  - Dolazna likvidnost
  - Izlazna likvidnost
- Upravljanje vršnjacima i kanalima
  - Povezani vršnjaci
  - Naknade za kanal
  - Status kanala
- Pravljenje čestih rezervnih kopija stanja kanala.
- Provera izveštaja o rutiranju
- Alternativno, koristite usluge kao što je Loop.


Svo upravljanje čvorovima munje se standardno obavlja sa RTL (pod pretpostavkom da koristite LND implementaciju). Administratori mogu kliknuti na svoj Lightning Wallet u BTCPay Serveru i pronaći dugme za otvaranje RTL. Glavna kontrolna tabla BTCPay Servera je sada ažurirana sa Lightning Network pločicama, uključujući brz pristup RTL.


### Primer 2


#### Poveži se sa lightning-om pomoću Alby


Kada se povezujete sa skrbnikom kao što je Alby, vlasnici prodavnica prvo treba da kreiraju nalog, posetite: https://getalby.com/


![image](assets/en/35.webp)


Nakon kreiranja Alby naloga, idite u vašu BTCPay Server prodavnicu.


Korak 1: Kliknite na 'Set up a Lightning node' na kontrolnoj tabli ili 'Lightning' ispod novčanika.


![image](assets/en/36.webp)


Korak 2: Unesite svoje Wallet akreditive za povezivanje koje je obezbedio Alby. Na kontrolnoj tabli Alby, kliknite na Wallet. Ovde ćete pronaći "Wallet Akreditive za povezivanje". Kopirajte ove akreditive. Nalepite akreditive iz Alby u polje za konfiguraciju povezivanja u BTCPay Server.


![image](assets/en/37.webp)


Korak 3: Nakon što obezbedite BTCPay Server-u detalje za povezivanje, kliknite na dugme "Test Connection" da biste osigurali da veza radi ispravno. Obratite pažnju na poruku "Connection to lightning node successful" na vrhu ekrana. Ovo potvrđuje da sve funkcioniše kako treba.


![image](assets/en/38.webp)


Korak 4: Kliknite na sačuvaj, i vaša prodavnica je sada povezana sa lightning nodom od strane Alby.


![image](assets/en/39.webp)


**!Napomena!**


Nikada ne veruj rešenju za čuvanje Lightning mreže sa više vrednosti nego što si spreman da izgubiš.


### Sažetak veština


U ovom odeljku ste naučili:



- Kako povezati interni ili eksterni Lightning čvor
- Sadržaj i funkcija različitih pločica povezanih sa Lightning-om na Kontrolnoj tabli
- Kako konfigurisati Lightning Wallet koristeći Voltage Surge ili Alby


### Procena znanja Praktični pregled


Opišite neke od različitih opcija za povezivanje Lightning Wallet sa vašom prodavnicom.


# BTCPay Server Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Pregled kontrolne table


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server je modularni softverski paket. Međutim, postoje standardi koje će svaki BTCPay Server imati i sa kojima će Administrator/korisnici komunicirati. Počevši od Kontrolne table. Glavna ulazna tačka svakog BTCPay Server-a nakon prijavljivanja. Kontrolna tabla daje pregled kako vaša prodavnica posluje, trenutnog stanja Wallet i poslednjih tx-a u proteklih 7 dana. Kako je to modularni prikaz, dodaci mogu koristiti ovaj prikaz za svoju korist i kreirati svoje pločice na Kontrolnoj tabli. Za ovu knjigu kursa, govorićemo samo o standardnim dodacima/aplikacijama i njihovim odgovarajućim prikazima kroz BTCPay Server.


### Pločice Kontrolne Table


Unutar glavnog prikaza BTCPay Server kontrolne table dostupno je nekoliko standardnih pločica. Ove pločice su namenjene vlasniku prodavnice ili administratoru da brzo upravlja svojom prodavnicom u jednom pregledu.



- Wallet balans
- Aktivnost transakcije
- Lightning Balance (ako je Lightning omogućen u prodavnici)
- Lightning Services (ako je Lightning omogućen u prodavnici)
- Nedavne transakcije.
- Nedavne fakture
- Trenutno aktivni Crowdfund-ovi
- Performanse prodavnice / najprodavaniji artikli.


### Wallet saldo


Wallet Balance pločica pruža brz pregled sredstava i performansi vašeg Wallet. Može se prikazati u BTC ili Fiat valuti na nedeljnom, mesečnom ili godišnjem grafikonu.


![image](assets/en/40.webp)


### Aktivnost transakcije


Pored pločice Wallet Balance, BTCPay Server prikazuje brzi pregled čekajućih isplata, broj transakcija u poslednjih 7 dana i da li je vaša prodavnica izdala bilo kakve povrate. Klikom na dugme Upravljaj ulazite u upravljanje čekajućim isplatama (saznajte više o isplatama u BTCPay Server - Poglavlje o plaćanjima).


![image](assets/en/41.webp)


### Lightning Balance


Ovo je vidljivo samo kada je Lightning aktiviran.


Kada je Administrator omogućio pristup Lightning Network, BTCPay Server kontrolna tabla sada ima novu pločicu sa informacijama o vašem Lightning čvoru. Koliko BTC-a je u kanalima, kako je ovo balansirano lokalno ili udaljeno (prilivna ili odlazna likvidnost) ako se kanali zatvaraju ili otvaraju, i koliko Bitcoin drži On-Chain na lightning čvoru.


![image](assets/en/42.webp)


### Lightning Services


Ovo je vidljivo samo kada je munja aktivna.


Pored prikaza stanja vašeg Lightning računa na BTCPay Server kontrolnoj tabli, administratori će takođe videti pločicu za Lightning usluge. Ovde administratori mogu pronaći brze dugmiće za alate koje koriste za upravljanje svojim Lightning čvorom; na primer, Ride the Lightning je jedan od standardnih alata sa BTCPay Server-om za upravljanje Lightning čvorom.


![image](assets/en/43.webp)


### Nedavne transakcije


Pločica nedavnih transakcija će prikazati najnovije transakcije vaše prodavnice. Jednim klikom, Administrator instance BTCPay Server-a sada može videti najnoviju transakciju i proveriti da li je potrebna pažnja prema njoj.


![image](assets/en/44.webp)


### Nedavne fakture


Pločica sa nedavnim fakturama prikazuje 6 najnovijih faktura generisanih od strane vašeg BTCPay Server-a, uključujući Status i iznos Invoice. Pločica takođe uključuje dugme "Prikaži sve" za lak pristup kompletnom pregledu Invoice.


![image](assets/en/45.webp)


### Point Of Sale i Crowdfunds


Kako BTCPay Server isporučuje skup standardnih dodataka ili aplikacija, Point Of Sale i Crowdfund su dva glavna dodatka BTCPay Server-a. Sa svakom prodavnicom i Wallet, korisnik BTCPay Server-a može generate onoliko Point Of Sales ili Crowdfunds koliko smatra potrebnim. Svaki će kreirati novu pločicu na kontrolnoj tabli koja prikazuje performanse dodataka.


![image](assets/en/46.webp)


Primetite blagu razliku između pločice Point of Sale i Crowdfund. Administrator vidi najprodavanije artikle u pločici Point of Sales. U pločici Crowdfund, ovo postaje Top Perks. Obe pločice imaju brze dugmiće za upravljanje odgovarajućom aplikacijom i pregled nedavno kreiranih faktura prema najprodavanijim artiklima ili top pogodnostima.


![image](assets/en/47.webp)


**!?Napomena!?**


Grafikoni stanja i nedavne transakcije dostupni su samo za On-Chain način plaćanja. Informacije o Lightning Network stanjima i transakcijama su na listi zadataka. Od BTCPay Server verzije 1.6.0, osnovna Lightning Network stanja su dostupna.


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Osnovni raspored pločica na glavnoj odredišnoj stranici poznat je kao Kontrolna tabla.
- Osnovno razumevanje sadržaja svake pločice.


### Pregled procene znanja


Nabroj što više pločica sa kontrolne table koliko možeš iz memorije.


## BTCPay Server - Postavke prodavnice


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


U okviru softvera BTCPay Server, znamo za 2 tipa podešavanja. BTCPay Server podešavanja specifična za prodavnicu, dugme za podešavanja koje se nalazi u levom meniju ispod Kontrolne table, i BTCPay Server podešavanja, koja se nalaze na dnu menija odmah iznad Naloga. BTCPay Server podešavanja specifična za server mogu videti samo administratori servera.


Postavke prodavnice sastoje se od mnogih kartica za kategorizaciju svakog skupa postavki.



- General
- Stope
- Izgled naplate
- Pristupni tokeni
- Korisnici
- Uloge
- Webhooks
- Procesori Isplata
- E-pošta
- Forme


### General


U kartici Opšta podešavanja, vlasnici prodavnica postavljaju podrazumevane vrednosti za brendiranje i plaćanje. Prilikom početnog podešavanja prodavnice, dat je naziv prodavnice; ovo će biti prikazano u Opštim podešavanjima pod Naziv prodavnice. Ovde vlasnik prodavnice takođe može podesiti svoj veb-sajt da odgovara brendiranju i ID prodavnice koji Administrator može prepoznati u bazi podataka.


#### Brendiranje


Kako je BTCPay Server FOSS, vlasnik prodavnice može prilagoditi brendiranje kako bi odgovaralo njegovoj prodavnici. Postavite boju brenda, sačuvajte logotipe vašeg brenda i dodajte prilagođeni CSS za stranice koje su okrenute javnosti/klijentima (Fakture, Zahtevi za plaćanje, Povlačenje uplata).


#### Plaćanje


U postavkama plaćanja, vlasnici prodavnica mogu da postave podrazumevanu valutu svoje prodavnice (bilo u Bitcoin ili u bilo kojoj fiat valuti).


#### Dozvoli bilo kome da kreira fakture


Ovo podešavanje je namenjeno programerima ili graditeljima na BTCPay Server-u. Kada je ovo podešavanje uključeno za vašu prodavnicu, omogućava spoljašnjem svetu da kreira fakture na vašoj BTCPay Server instanci.


#### Dodajte dodatnu naknadu (mrežna naknada) na fakture.


Jedna funkcija unutar BTCPay-a za zaštitu trgovaca od Dust napada ili klijenata da kasnije izazovu visoke troškove naknada kada trgovac treba da premesti mnogo Bitcoin odjednom. Na primer, kupac je kreirao Invoice za 20$ i platio ga delimično, plaćajući 1$ 20 puta dok Invoice nije bio u potpunosti plaćen. Trgovac sada ima veću transakciju, povećavajući Mining trošak u slučaju da trgovac odluči da premesti ta sredstva kasnije. Podrazumevano, BTCPay primenjuje dodatni trošak mreže na ukupan iznos Invoice kako bi pokrio taj trošak za trgovca kada je Invoice plaćen u više transakcija. BTCPay nudi nekoliko opcija za prilagođavanje ove funkcije zaštite. Možete primeniti mrežnu naknadu:



- Samo ako kupac izvrši više od jedne uplate za Invoice (U gornjem primeru, ako je kupac kreirao Invoice za 20\$ i platio 1\$, ukupno dugovanje za Invoice je sada 19\$ + mrežna naknada. Mrežna naknada se primenjuje nakon prve uplate)
- Na svakoj uplati (uključujući prvu uplatu, u našem primeru, ukupno će biti 20\$ + mrežna naknada odmah, čak i na prvoj uplati)
- Nikada ne dodaj mrežnu naknadu (potpuno onemogućava mrežnu naknadu)


Iako štiti od Dust transakcija, takođe može negativno uticati na poslovanje ako nije pravilno komunicirano. Kupci mogu imati dodatna pitanja i misliti da im naplaćujete previše.


#### Invoice ističe ako ceo iznos nije plaćen nakon?


Invoice tajmer je po defaultu postavljen na 15 minuta. Tajmer je mehanizam zaštite protiv volatilnosti jer zaključava iznos Bitcoin prema Bitcoin u fiat kursu. Ako kupac ne plati Invoice u definisanom periodu, Invoice se smatra isteklim. Invoice se smatra "plaćenim" čim je transakcija vidljiva na Blockchain (0-potvrda), ali se smatra "završenim" kada dostigne broj potvrda koji je trgovac definisao (obično, 1-6). Tajmer je prilagodljiv po minutima.


#### Razmotrite Invoice plaćen čak i ako je plaćeni iznos X% manji od očekivanog?


Kada kupac koristi Exchange Wallet za direktno plaćanje Invoice, Exchange uzima malu naknadu. To znači da takav Invoice nije smatran potpuno završenim. Invoice dobija status "delimično plaćeno". Ovde možete postaviti procenat ako trgovac želi da prihvati nedovoljno plaćene fakture.


### Stope


U BTCPay Server-u, kada se generiše Invoice, uvek je potrebna najnovija i tačna Bitcoin cena u fiat valuti. Kada se kreira nova prodavnica u BTCPay Server-u, od administratora se traži da postave svoj preferirani izvor cena; nakon što je prodavnica postavljena, vlasnici prodavnica uvek mogu promeniti svoj izvor cena u ovoj kartici.


#### Napredno skriptovanje pravila za stopu


Uglavnom koriste napredni korisnici. Ako je uključen, vlasnici prodavnica mogu kreirati skripte oko ponašanja cena i načina naplate svojim kupcima.


#### Testiranje


Brzo mesto za testiranje vaših preferiranih valutnih parova. Ovo takođe uključuje funkciju za proveru podrazumevanih valutnih parova putem REST upita.


### Izgled naplate


Kartica Izgled naplate počinje sa postavkama specifičnim za Invoice i podrazumevanim načinom plaćanja i omogućava specifične načine plaćanja kada su ispunjeni postavljeni zahtevi.


#### Invoice postavke


Podrazumevani načini plaćanja. BTCPay Server u standardnoj konfiguraciji ima tri opcije.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)


Možemo postaviti parametre za našu prodavnicu, gde će kupac komunicirati sa Lightning-om samo kada je cena manja od X iznosa i obrnuto za On-Chain transakcije kada je X veći od Y uvek prikazati On-Chain opciju plaćanja.


![image](assets/en/48.webp)


#### Plaćanje


Od izdanja BTCPay Server 1.7, uveden je novi Checkout Interface, nazvan Checkout V2. Od izdanja 1.9 je standardizovan, administratori i vlasnici prodavnica i dalje mogu postaviti naplatu na prethodno izdanje. Korišćenjem prekidača "Koristi klasičnu naplatu", vlasnik prodavnice može vratiti prodavnicu na prethodno iskustvo naplate. BTCPay Server takođe ima odabrani set unapred podešenih opcija za online trgovinu ili iskustvo u prodavnici.


![image](assets/en/49.webp)


Kada kupac stupi u interakciju sa prodavnicom i generiše Invoice, postoji vreme isteka za Invoice. Podrazumevano, BTCPay Server postavlja ovo na 5 minuta, a Administrator može postaviti ovo na vreme koje smatra prikladnim. Stranica za naplatu može se dodatno prilagoditi proverom sledećih parametara:



- Proslavite uplatu prikazivanjem konfeta
- Prikaži zaglavlje prodavnice (Ime i logo)
- Prikaži dugme "Plati u Wallet"
- Ujedini URL/QR kodove za plaćanja On-Chain i off-chain
- Prikaži iznose Lightning plaćanja u Satoshijima
- Automatsko otkrivanje jezika pri naplati


![image](assets/en/50.webp)


Kada Auto-detect jezik nije postavljen, BTCPay Server će, po defaultu, prikazivati engleski. Vlasnik prodavnice može promeniti ovaj podrazumevani jezik na svoj preferirani jezik.


![image](assets/en/51.webp)


Kliknite na padajući meni i vlasnici prodavnica mogu postaviti prilagođeni HTML naslov koji će biti prikazan na stranici za naplatu.


![image](assets/en/52.webp)


Da bi se osiguralo da kupac zna svoj način plaćanja, vlasnik prodavnice može eksplicitno postaviti svoju naplatu da uvek zahteva od korisnika da izaberu svoj preferirani način plaćanja. Kada je Invoice plaćen, BTCPay Server omogućava kupcu da se vrati u webshop. Vlasnici prodavnica mogu postaviti ovo preusmeravanje nakon što je kupac automatski platio.


![image](assets/en/53.webp)


#### Javni račun


U okviru postavki javnog računa, vlasnik prodavnice može postaviti stranice računa na javno i prikazati listu plaćanja na stranici računa i QR kod računa kako bi ga kupac lako digitalno pristupio.


![image](assets/en/54.webp)


### Pristupni tokeni


Pristupni tokeni se koriste za uparivanje sa određenim e-commerce integracijama ili prilagođenim integracijama.


![image](assets/en/55.webp)


### Korisnici


Korisnici prodavnice su mesto gde vlasnik prodavnice može upravljati članovima svog osoblja, njihovim nalozima i pristupom prodavnici. Nakon što članovi osoblja kreiraju svoje naloge, vlasnik prodavnice može dodati određene korisnike u prodavnicu kao goste ili vlasnike. Da biste dodatno definisali ulogu člana osoblja, pogledajte sledeći odeljak o „BTCPay Server podešavanjima prodavnice - Uloge.“


![image](assets/en/56.webp)


### Uloge


Vlasnik prodavnice možda neće smatrati standardne uloge korisnika dovoljno značajnim. U postavkama prilagođenih uloga, vlasnik prodavnice može definisati tačne potrebe za svaku ulogu u svom poslovanju.


(1) Da biste kreirali novu ulogu, kliknite na dugme "+ Dodaj ulogu".


![image](assets/en/57.webp)


(2) Unesite naziv uloge, na primer, "Kasir".


![image](assets/en/58.webp)


(3) Konfigurišite pojedinačne dozvole za ulogu.



- Izmenite svoje prodavnice.
- Upravljajte Exchange nalozima povezanim sa vašim prodavnicama.
  - Prikaži Exchange naloge povezane sa vašim prodavnicama.
- Upravljajte svojim povlačenim plaćanjima.
- Kreiraj povlačna plaćanja.
  - Kreiraj neodobrene pull uplate.
- Izmeni fakture.
  - Pregledaj fakture.
  - Kreiraj Invoice.
  - Kreirajte fakture sa lightning čvorova povezanih sa vašim prodavnicama.
- Pogledajte vaše prodavnice.
  - Pregledaj fakture.
  - Pregledaj svoje zahteve za plaćanje.
  - Izmenite webhook-ove prodavnica.
- Izmenite svoje zahteve za plaćanje.
  - Pregledaj svoje zahteve za plaćanje.
- Koristite lightning čvorove povezane sa vašim prodavnicama.
  - Pregledajte lightning fakture povezane sa vašim prodavnicama.
  - Kreirajte fakture sa lightning čvorova povezanih sa vašim prodavnicama.
- Depozitujte sredstva na Exchange račune povezane sa vašim prodavnicama.
- Povucite sredstva sa Exchange računa u vašu prodavnicu.
- Trgujte sredstvima na Exchange računima vaše prodavnice.


Kada se uloga kreira, ime je fiksno i ne može se promeniti kasnije u režimu uređivanja.


![image](assets/en/59.webp)


### Webhooks


U okviru BTCPay Server-a, relativno je lako napraviti novi "Webhook". U postavkama BTCPay Server prodavnice - kartica Webhooks, vlasnik prodavnice može lako kreirati novi webhook klikom na "+ Create Webhook". Webhooks omogućavaju BTCPay Server-u da šalje HTTP događaje vezane za vašu prodavnicu drugim serverima ili e-commerce integracijama.


![image](assets/en/60.webp)


Sada ste u prikazu za kreiranje Webhook-a. Uverite se da znate svoj Payload URL i nalepite ga u svoj BTCPay Server. Dok ste nalepili payload URL, ispod se prikazuje tajna za webhook. Kopirajte tajnu za webhook i obezbedite je na krajnjoj tački. Kada je sve postavljeno, možete uključiti u BTCPay Server-u Automatsko ponovno slanje. Pokušaćemo ponovo da pošaljemo svaku neuspelu isporuku nakon 10 sekundi, 1 minuta, i do 6 puta nakon 10 minuta. Možete se prebacivati između svakog događaja ili specificirati događaje prema vašim potrebama. Obavezno omogućite webhook i pritisnite Dodaj webhook da biste ga sačuvali.


![image](assets/en/61.webp)


Webhooks nisu namenjeni da budu kompatibilni sa Bitpay API-jem. Postoje dva odvojena IPN-a (u terminima BitPay-a: "Instant Payment Notifications") u BTCPay Serveru.



- Webhookp
- Obaveštenja


Koristite URL za obaveštenja samo kada kreirate fakture putem Bitpay API-ja.


### Procesori Isplata


Procesori isplata rade zajedno sa konceptom Isplata u BTCPay Server-u. Agregator isplata za grupisanje više transakcija i njihovo slanje odjednom. Sa procesorima isplata, vlasnik prodavnice može automatizovati grupisane isplate. BTCPay Server pruža dve metode automatizovanih isplata, On-Chain i off-chain (LN).


Vlasnik prodavnice može kliknuti i konfigurisati oba procesora isplate zasebno. Vlasnik prodavnice možda želi da pokrene procesor On-Chain samo jednom svakih X sati, dok off-chain može ići svakih nekoliko minuta. Za On-Chain, možete takođe postaviti cilj za koji blok treba da bude uključen. Po default-u, ovo je postavljeno na 1 (ili sledeći dostupan blok). Primetite da postavljanje procesora isplate off-chain ima samo intervalni tajmer i nema cilj bloka. Lightning Network isplate su trenutne.


![image](assets/en/62.webp)

![image](assets/en/63.webp)


Vlasnici prodavnica mogu konfigurisati On-Chain procesor samo ako imaju Hot-Wallet povezan sa svojom prodavnicom.


![image](assets/en/64.webp)


Nakon postavljanja procesora za isplatu, možete ga brzo ukloniti ili izmeniti vraćanjem na karticu procesora za isplatu u postavkama BTCPay Server prodavnice.


**!?Napomena!?**


Procesor isplata On-Chain - Procesor isplata na lancu može raditi samo na prodavnici koja je konfigurisana sa povezanim Hot Wallet. Ako nema povezanog Hot Wallet, BTCPay Server ne drži ključeve za Wallet i neće moći automatski da obradi isplate.


### E-pošta


BTCPay Server može koristiti e-poštu za obaveštenja ili, kada je pravilno postavljeno, za oporavak naloga koji su napravljeni na instanci, jer standardni BTCPay Server ne šalje e-poštu kada je lozinka izgubljena, na primer.


![image](assets/en/65.webp)


Pre nego što vlasnik prodavnice može postaviti pravila za Email koja će se aktivirati na specifične događaje u njegovoj prodavnici, moramo postaviti osnovna podešavanja email-a. BTCPay Server zahteva ova podešavanja kako bi slao email-ove za događaje vezane za vašu prodavnicu ili za resetovanje lozinke.


BTCPay Server je olakšao popunjavanje ovih informacija korišćenjem opcije "Quick Fill":



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


Korišćenjem opcije brzog popunjavanja, BTCPay Server će unapred popuniti polja za SMTP server i port; sada vlasnik prodavnice treba samo da unese svoje akreditive u Email Address, Prijava (što je obično jednako vašem emailu Address), i vašu lozinku. Napredna opcija koju BTCPay Server nudi u podešavanjima emaila je Onemogućavanje provere sigurnosti TLS sertifikata; po podrazumevanim podešavanjima, ovo je Omogućeno.


![image](assets/en/66.webp)


Sa pravilima e-pošte, vlasnik prodavnice može postaviti specifične događaje koji će pokrenuti slanje e-poruka na određene e-mail adrese.



- Invoice Kreirano
- Invoice Primljena uplata
- Invoice Obrada
- Invoice Istekao
- Invoice Rešeno
- Invoice Nevažeće
- Invoice Plaćanje Izmireno


Ako je kupac dostavio Email Address, ovi okidači mogu takođe poslati informacije kupcu. Vlasnici prodavnica mogu unapred popuniti liniju Predmeta kako bi jasno naznačili zašto se ovaj Email dogodio i koji okidač ga je izazvao.


![image](assets/en/67.webp)


### Obrasci


Kako BTCPay Server ne prikuplja nikakve podatke, vlasnik prodavnice možda želi dodati prilagođeni obrazac u svoje iskustvo naplate; na ovaj način, vlasnik prodavnice može prikupiti dodatne informacije od svog kupca. BTCPay Server graditelj obrazaca sastoji se od dva dela, vizuelnog i naprednijeg prikaza koda obrazaca.


Kada kreirate novi obrazac, BTCPay Server otvara novi prozor koji traži osnovne informacije o tome šta želite da vaš novi obrazac zahteva. Na početku, vlasnik prodavnice treba da da jasno ime svom novom obrascu, ovo ime NE MOŽE biti promenjeno nakon što je postavljeno.


![image](assets/en/68.webp)


Nakon što vlasnik prodavnice da ime obrascu, možete takođe prebaciti prekidač za "Dozvoli javnu upotrebu obrasca" na UKLJUČENO, i on postaje Green. Ovo je kako bi se obrazac koristio na svakom mestu koje je okrenuto ka kupcima. Na primer, ako vlasnik prodavnice kreira 1 poseban Invoice ne preko svog prodajnog mesta, možda će i dalje želeti da prikupi informacije od kupca; ovo prebacivanje na UKLJUČENO omogućava prikupljanje tih informacija.


![image](assets/en/69.webp)


Svaki obrazac počinje sa najmanje 1 Novo polje obrasca. Vlasnik prodavnice može odabrati kakav tip polja treba da bude;



- Tekst
- Broj
- Lozinka
- E-pošta
- URL
- Telefonski brojevi
- Datum
- Skrivena polja
- Polje
- Oblast za unos otvorenih komentara.
- Selektor opcija


Svaka vrsta dolazi sa svojim parametrima za popunjavanje. Vlasnik prodavnice može ih postaviti po svom nahođenju. Ispod prvog kreiranog polja, vlasnici prodavnica mogu nastaviti dodavati nova polja u ovaj jedan obrazac.


![image](assets/en/70.webp)


#### Napredni prilagođeni obrasci


BTCPay Server takođe omogućava kreiranje Formi u kodu. Posebno u JSON formatu. Umesto da gledaju u editor, vlasnici prodavnica mogu kliknuti na dugme CODE odmah pored editora i ući u kod svojih Formi. U definiciji polja, mogu se postaviti samo sledeća polja; vrednosti polja se čuvaju u metapodacima Invoice:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Naziv polja predstavlja naziv JSON svojstva koje čuva vrednost koju je korisnik uneo u metapodacima Invoice. Neka dobro poznata imena mogu se interpretirati i modifikovati postavke Invoice.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Možete unapred popuniti polja Invoice automatski dodavanjem niza upita u URL obrasca, kao što je "?your_field=value".


Evo nekoliko slučajeva upotrebe za ovu funkciju:



- Pomoć korisničkom unosu: Unapred popunite polja poznatim informacijama o korisniku kako biste im olakšali popunjavanje obrasca. Na primer, ako već znate korisnikov email Address, možete unapred popuniti polje za email kako biste im uštedeli vreme.
- Personalizacija: Prilagodite obrazac na osnovu preferencija ili segmentacije kupaca. Na primer, ako imate različite nivoe kupaca, možete unapred popuniti obrazac relevantnim podacima, kao što su njihov nivo članstva ili specifične ponude.
- Praćenje: Pratite izvor poseta korisnika koristeći skrivena polja i unapred popunjene vrednosti. Na primer, možete kreirati linkove sa unapred popunjenim utm_media vrednostima za svaki marketinški kanal (npr. Twitter, Facebook, Email). Ovo vam pomaže da analizirate efikasnost vaših marketinških napora.
- A/B testiranje: Unapred popunite polja različitim vrednostima kako biste testirali različite verzije formulara, omogućavajući vam optimizaciju korisničkog iskustva i stope konverzije.


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Izgled i funkcije kartica u Podešavanjima prodavnice
- Mnoštvo opcija za fino podešavanje rukovanja osnovnim Exchange stopama, delimičnim plaćanjima, blagim nedovoljno plaćenim iznosima i još mnogo toga.
- Prilagodite izgled naplate, uključujući omogućavanje glavnog lanca u zavisnosti od cene naspram Lightning-a na fakturama.
- Upravljajte nivoima pristupa prodavnici i dozvolama za različite uloge.
- Konfigurišite automatske e-poruke i njihove okidače
- Kreirajte prilagođene obrasce za prikupljanje dodatnih informacija o kupcima prilikom naplate.


### Procene Znanja


#### KA Pregled


Koja je razlika između Podešavanja prodavnice i Podešavanja servera?


#### KA Hipotetički


Opišite neke opcije koje biste mogli odabrati u Checkout Appearance > Invoice Settings, i zašto.


## BTCPay Server - Postavke servera


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server se sastoji od dva različita prikaza podešavanja. Jedan je posvećen podešavanjima prodavnice, a drugi podešavanjima servera. Ovo drugo je dostupno samo ako ste administrator servera, a ne vlasnicima prodavnica. Administratori servera mogu dodavati korisnike, kreirati prilagođene uloge, konfigurisati email server, postavljati politike, izvršavati zadatke održavanja, proveravati sve usluge povezane sa BTCPay Server-om, otpremati fajlove na server ili proveravati dnevnike (Logs).


### Korisnici


Kao što je pomenuto u prethodnom delu, administratori servera mogu pozvati korisnike na svoj server dodavanjem u karticu Korisnici.


### Prilagođene uloge za ceo server


BTCPay Server poznaje dve vrste prilagođenih uloga, prilagođene uloge specifične za prodavnicu i prilagođene uloge na nivou servera u postavkama BTCPay Server-a. Obe imaju sličan skup dozvola; međutim, ako se postave kroz BTCpay Server Settings - Roles karticu, primenjena uloga će biti na nivou servera i primenjivaće se na više prodavnica. Obratite pažnju na oznaku "Server-wide" za prilagođene uloge u postavkama servera.


![image](assets/en/71.webp)


### Prilagođene uloge za ceo server


Dozvola za prilagođene uloge na nivou servera;



- Izmenite svoje prodavnice.
- Upravljajte Exchange nalozima povezanim sa vašim prodavnicama.
  - Prikaži Exchange naloge povezane sa vašim prodavnicama.
- Upravljajte svojim povlačenim plaćanjima.
- Kreiraj povlačna plaćanja.
  - Kreirajte neodobrene pull uplate.
- Izmeni fakture.
  - Pregledaj fakture.
  - Kreiraj Invoice.
  - Kreirajte fakture sa čvorova za plaćanje povezanim sa vašim prodavnicama.
- Pogledajte vaše prodavnice.
  - Pregledaj fakture.
  - Pregledajte vaše zahteve za plaćanje.
  - Izmeni webhookove prodavnica.
- Izmenite svoje zahteve za plaćanje.
  - Pregledaj svoje zahteve za plaćanje.
- Koristite čvorove munje povezane sa vašim prodavnicama.
  - Pregledajte lightning fakture povezane sa vašim prodavnicama.
  - Kreirajte fakture sa čvorova munje povezanih sa vašim prodavnicama.
- Depozitujte sredstva na Exchange račune povezane sa vašim prodavnicama.
- Povucite sredstva sa Exchange računa u vašu prodavnicu.
- Trgujte sredstvima na Exchange računima vaše prodavnice.


**!?Napomena!?**


Kada se uloga kreira, ime je fiksno i ne može se promeniti kasnije u režimu uređivanja.


### Email


Postavke e-pošte za ceo server izgledaju slično onima u postavkama e-pošte specifičnim za prodavnicu. Međutim, ova konfiguracija ne upravlja samo okidačima za prodavnice ili administratorima logova. Ova postavka e-pošte takođe omogućava oporavak lozinke na BTCPay Serveru pri prijavi. Radi slično kao postavke specifične za prodavnicu; administratori mogu brzo popuniti svoje parametre e-pošte i uneti svoje e-mail akreditive, i server sada može slati e-poštu.


![image](assets/en/72.webp)


### Politike


BTCPay Server administratori politika mogu postaviti neka podešavanja na teme kao što su Podešavanja postojećih korisnika, Podešavanja novih korisnika, Podešavanja obaveštenja i Podešavanja održavanja. Ova podešavanja su namenjena registraciji novih korisnika kao administratora ili običnih korisnika, ili čak sakrivanju BTCPay Server-a od pretraživača dodavanjem u zaglavlje vašeg servera.


![image](assets/en/73.webp)


#### Postojeća podešavanja korisnika


Opcije dostupne ovde su odvojene od prilagođenih uloga. Ove dodatne dozvole mogu učiniti prodavnicu ili vlasnika prodavnice ranjivim na napade. Politike koje se mogu dodati postojećim korisnicima:



- Dozvoli ne-administratorima da koriste interni Lightning čvor u svojim prodavnicama.
  - Ovo bi omogućilo vlasnicima prodavnica da koriste Administratorov Lightning čvor na serveru i, prema tome, njegova sredstva! Oprez, ovo nije rešenje za davanje pristupa Lightning-u.
- Dozvoli ne-administratorima da kreiraju Hot novčanike za svoje prodavnice.
  - Ovo bi omogućilo svakome ko ima nalog na vašoj BTCPay Server instanci da kreira Hot-novčanike i čuva njihov oporavak seed na serveru Administratora. Ovo bi moglo učiniti Administratora odgovornim za držanje sredstava treće strane!
- Dozvoli ne-administratorima da uvoze Hot novčanike za svoje prodavnice.
  - Slično prethodnoj temi kreiranja Hot novčanika, ova politika omogućava uvoz Hot Wallet, sa istim opasnostima pomenutim u odeljku o kreiranju Hot novčanika.


![image](assets/en/74.webp)


#### Nove postavke korisnika


Možemo postaviti neka važna podešavanja za upravljanje novim korisnicima koji dolaze na server. Možemo postaviti email za potvrdu novih registracija, onemogućiti kreiranje novih korisnika putem ekrana za prijavu i ograničiti pristup kreiranju korisnika preko API-ja za korisnike koji nisu administratori.



- Zahtevaj e-poruku za potvrdu registracije.
  - Administrator servera mora da postavi Email server!
- Onemogući registraciju novih korisnika na serveru
- Onemogući pristup API krajnjoj tački za kreiranje korisnika za korisnike koji nisu administratori.


Podrazumevano, BTCPay Server ima uključenu opciju Onemogući registraciju novih korisnika i isključen pristup API krajnjoj tački za kreiranje korisnika za ne-administratore. Ovo je iz bezbednosnih razloga kako nijedna nasumična osoba koja bi mogla pronaći BTCPay prijavu vašeg servera ne bi mogla početi sa kreiranjem naloga.


![image](assets/en/75.webp)


#### Postavke obaveštenja


![image](assets/en/76.webp)


#### Postavke održavanja


BTCPay Server je projekat otvorenog koda koji se nalazi na GitHub-u. Kad god BTCPay Server objavi novu verziju softvera, administratori mogu biti obavešteni da je dostupna nova verzija. Administratori takođe mogu želeti da obeshrabre pretraživače (google, yahoo, duckduckgo) od indeksiranja domena BTCPay Server-a. Kako je BTCPay Server FOSS, programeri širom sveta možda žele da kreiraju nove funkcije; BTCPay Server ima eksperimentalnu funkciju koja, kada je uključena, omogućava administratoru da koristi funkcije koje još nisu namenjene za produkciju, isključivo u svrhe testiranja.



- Proveri izdanja na GitHub-u i obavesti kada nova verzija BTCPay Server-a bude dostupna.
- Odvratite pretraživače od indeksiranja ove lokacije
- Omogući eksperimentalne funkcije.


![image](assets/en/77.webp)


#### Dodaci


BTCPay Server može dodati dodatke i proširiti svoj skup funkcija. Dodaci se, po defaultu, učitavaju iz BTCPay Server plugin-builder repozitorijuma. Administrator, međutim, može odabrati da vidi dodatke u Pre-release stanju, i ako to programer dodatka dozvoli, administrator servera sada može instalirati beta verzije dodataka.


![image](assets/en/78.webp)


##### Postavke prilagođavanja


Standardna BTCPay Server implementacija biće dostupna putem domena postavljenog prilikom instalacije. Međutim, administrator servera može premapirati osnovni domen i prikazati jednu od kreiranih aplikacija iz određene prodavnice. Administrator servera takođe može mapirati specifične domene na specifične aplikacije.



- Prikaži aplikaciju na root-u web sajta
  - Prikazuje listu mogućih aplikacija za prikaz na osnovnom domenu.


![image](assets/en/79.webp)



- Mapirajte specifične domene na specifične aplikacije.
  - Kada kliknete da postavite određeni domen za određene aplikacije, Administrator može postaviti onoliko domena usmerenih na određene aplikacije koliko je potrebno.


![image](assets/en/80.webp)


#### Blok istraživači


BTCPay Server, kao standard, dolazi sa Mempool.space kao svojim Block explorer za transakcije. Kada BTCPay Server generiše novi Invoice, i postoji transakcija vezana za njega, vlasnik prodavnice može kliknuti da otvori transakciju; BTCPay Server će standardno pokazivati prema Mempool.space kao Block explorer; administrator servera može ovo promeniti prema svojoj preferenciji.


![image](assets/en/81.webp)


### Usluge


Postavke BTCPay Servera: Kartica Usluge je pregled komponenti koje vaš BTCPay Server koristi. Usluge koje vaš BTCPay Server izlaže mogu se razlikovati u zavisnosti od metode implementacije.


Administrator BTCPay Servera može kliknuti na „Pogledaj informacije“ iza svake usluge da je otvori i postavi specifična podešavanja.


![image](assets/en/82.webp)


#### LND (gRPC)


BTCPay izlaže LND-ovu GRPC uslugu za spoljašnju potrošnju; informacije o povezivanju možete pronaći u ovom specifičnom meniju podešavanja; kompatibilni novčanici su navedeni ovde. BTCPay Server takođe daje QR kod za povezivanje koji možete skenirati i primeniti u mobilnom Wallet.


Administratori servera mogu otvoriti više detalja da vide;



- Detalji domaćina
- Korišćenje SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay izlaže REST uslugu LND za vanjsku potrošnju; informacije o povezivanju možete pronaći ovde; kompatibilni novčanici su navedeni ovde. Među kompatibilnim novčanicima su Joule, Alby i ZeusLN. BTCPay Server daje QR kod za povezivanje, skenirajte i primenite u kompatibilnom Wallet.



- REST Uri
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon


#### LND seed Rezerva


LND seed rezervna kopija je korisna za povrat sredstava sa vašeg LND Wallet u slučaju oštećenja vašeg Servera. Kako je Lightning čvor Hot-Wallet, poverljive seed informacije možete pronaći na ovoj stranici.


LND dokumentuje proces oporavka. Pogledajte https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md za dokumentaciju.


#### Vozi munju


Ride the Lightning je alat za upravljanje Lightning čvorovima izgrađen kao softver otvorenog koda. BTCPay Server koristi RTL kao komponentu za upravljanje Lightning čvorovima u svom sklopu. Administratori BTCPay Server-a mogu pristupiti RTL-u putem postavki Servera - kartica Usluge ili klikom na Lightning Wallet.


#### Full node P2P


Administratori servera možda žele da povežu svoj Bitcoin čvor sa mobilnim Wallet. Ova stranica pruža informacije za daljinsko povezivanje sa vašim Full node putem P2P protokola. U trenutku pisanja ove knjige, BTCPay Server navodi Blockstream Green i Wasabi Wallet kao kompatibilne novčanike. BTCPay Server daje QR kod za povezivanje, skenirajte i primenite u kompatibilnom Wallet.


#### Full node RPC


Ova stranica izlaže informacije za daljinsko povezivanje sa vašim Full node putem RPC protokola.


#### SSH


SSH se koristi za svrhe održavanja. BTCPay Server prikazuje početnu komandu za povezivanje sa vašim Serverom i SSH javne ključeve ovlašćene za povezivanje sa vašim Serverom. Administratori Servera možda žele da isključe izmene SSH-a putem korisničkog interfejsa BTCPay Servera.


#### Dinamički DNS


Dinamički DNS omogućava vam da imate stabilno DNS ime koje pokazuje na vaš Server, čak i ako se vaš IP Address redovno menja. Ovo se preporučuje ako hostujete BTCPay Server kod kuće i želite da imate clearnet domen za pristup vašem Serveru.


Imajte na umu da morate pravilno konfigurisati vašu NAT i BTCPay Server instalaciju da biste dobili HTTPS sertifikat.


### Tema


BTCPay Server, kao standard, dolazi sa dve teme: Svetli i Tamni režim. Ove se mogu promeniti klikom na Nalog u donjem levom uglu i prebacivanjem između Tamne ili Svetle teme. Administratori BTCPay Server-a mogu dodati svoju temu pružanjem prilagođene CSS teme.


Administratori mogu proširiti Svetlu/Tamnu temu dodavanjem sopstvenog prilagođenog CSS-a ili postavljanjem svoje prilagođene teme kao potpuno prilagođene.


![image](assets/en/83.webp)


#### Brendiranje servera


Administratori servera mogu promeniti brendiranje BTCPay Server-a postavljanjem brendiranja vaše kompanije na nivou celog servera. Kako je BTCPay Server FOSS, administratori servera mogu prilagoditi softver i promeniti izgled kako bi odgovarao njihovom poslovanju.


![image](assets/en/84.webp)


### Održavanje


Kao administrator servera, vaši korisnici očekuju da se dobro brinete o serveru. Unutar kartice Održavanje BTCPay Servera, administrator može obaviti osnovno održavanje. Postavite ime domena za instance BTCPay Servera, restartujte ili očistite server. Možda najvažnije, pokrenite ažuriranja.


BTCPay Server je projekat otvorenog koda i često se ažurira. Svako novo izdanje se najavljuje ili putem vaših BTCPay Server obaveštenja ili na zvaničnim kanalima putem kojih BTCPay Server komunicira.


![image](assets/en/85.webp)


#### Naziv domena


Nakon što je BTCPay Server postavljen, administrator možda želi da promeni originalni domen. Unutar kartice Održavanje, administrator može promeniti domen. Nakon što klikne na potvrdu i postavi odgovarajuće DNS zapise na domenu, BTCPay Server se ažurira i restartuje kako bi se vratio na novi domen.


![image](assets/en/86.webp)


#### Ponovo pokreni


Ponovo pokreni BTCPay Server i povezane usluge.


![image](assets/en/87.webp)


#### Čisto


BTCPay Server radi sa Docker komponentama; sa ažuriranjima, može doći do zaostalih Docker slika, privremenih fajlova, itd. Administratori servera mogu očistiti ovo i povratiti prostor u svom okruženju pokretanjem Clean skripte.


![image](assets/en/88.webp)


#### Ažuriranje


Moguće najvažnija opcija u kartici Održavanje. BTCPay Server je izgrađen od strane zajednice, i stoga su njegovi ciklusi ažuriranja češći nego kod većine softverskih proizvoda. Kada BTCPay Server ima novo izdanje, administratori će biti obavešteni u svom centru za obaveštenja. Klikom na dugme za ažuriranje, BTCPay Server će proveriti GitHub za najnovije izdanje, ažurirati Server i restartovati ga. Pre ažuriranja, administratorima servera se uvek savetuje da pročitaju beleške o izdanju koje se distribuiraju kroz zvanične kanale BTCPay Server-a.


![image](assets/en/89.webp)


### Zapisnici


Suočiti se s problemom nikada nije zabavno. Ovaj dokument objašnjava najčešći tok rada i korake kako efikasno identifikovati vaš problem i rešiti ga sami ili uz pomoć zajednice.


Identifikovanje problema je ključno.


#### Replikacija problema


Prvo i najvažnije, pokušajte da utvrdite kada se problem javlja. Pokušajte da reprodukujete problem. Pokušajte da ažurirate i restartujete vaš Server kako biste proverili da li možete da reprodukujete vaš problem. Ako bolje opisuje vaš problem, napravite snimak ekrana.


##### Ažuriranje servera


Proverite svoju verziju BTCPay Server-a ako je mnogo starija od [najnovije verzije](https://github.com/btcpayserver/btcpayserver/releases) BTCPay Server-a. Ažuriranje vašeg Servera može rešiti problem.


##### Ponovno pokretanje servera


Ponovno pokretanje vašeg Servera je jednostavan način za rešavanje mnogih uobičajenih problema sa BTCPay Serverom. Možda ćete morati da se povežete putem SSH na vaš Server da biste ga ponovo pokrenuli.


##### Ponovno pokretanje usluge


Možda će biti potrebno da ponovo pokrenete određenu uslugu u vašoj BTCPay Server implementaciji za neke probleme. Na primer, ponovo pokretanje lets encrypt kontejnera za obnavljanje SSL sertifikata.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Koristite docker ps da pronađete ime druge usluge koju želite ponovo pokrenuti.


#### Gledanje kroz dnevnike


Logovi mogu pružiti ključne informacije. U narednim pasusima, opisaćemo kako dobiti informacije iz logova za različite delove BTCPay-a.


##### BTCPay Dnevnici


Od verzije v1.0.3.8, možete lako pristupiti BTCPay Server logovima sa prednjeg kraja. Ako ste administrator servera, idite na Podešavanja Servera > Logovi i otvorite datoteku logova. Ako ne znate šta određena greška u logovima znači, pomenite je prilikom rešavanja problema.


Ako želite detaljnije logove i koristite Docker implementaciju, možete pregledati logove specifičnih Docker kontejnera koristeći komandnu liniju. Pogledajte ova [uputstva za ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) u instancu BTCPay koja radi na VPS-u.


Na sledećoj stranici, opšta lista imena kontejnera korišćenih za BTCPay Server.


Pokrenite naredbe ispod da biste prikazali logove po imenu kontejnera. Zamenite ime kontejnera da biste pregledali logove drugih kontejnera.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Postoji nekoliko načina za pristup vašim LND logovima kada koristite Docker. Prvo se prijavite kao root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Alternativno, možete brzo odštampati logove koristeći ID kontejnera (potrebni su samo prvi jedinstveni karakteri ID-a, kao što su dva krajnja leva karaktera):


```bash
docker logs 'add your container ID'
```


Ako iz bilo kog razloga trebate više logova


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Videćete nešto poput


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Da biste pristupili nesažetim zapisima tih zapisa, uradite `cat LND.log` ili ako želite drugi, koristite `cat LND.log.15`.


Da biste pristupili komprimovanim logovima u `.gzip` koristite `gzip -d LND.log.16.gz` (u ovom slučaju pristupamo `LND.log.16.gz`). Ovo bi trebalo da vam da novi fajl, gde možete koristiti `cat LND.log.16`. U slučaju da gore navedeno ne radi, možda ćete prvo morati da instalirate gzip sa `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


alternativno, koristi ovo


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Takođe možete dobiti informacije o logu sa c-lightning CLI komandom.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin Node Logs


Pored [pregleda logova](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) vašeg bitcoind kontejnera, možete koristiti i bilo koju od [bitcoin-cli komandi](https://developer.Bitcoin.org/reference/RPC/index.html)


[(otvara se novi prozor)](https://developer.Bitcoin.org/reference/RPC/index.html) da biste dobili informacije sa vašeg Bitcoin čvora. BTCPay uključuje skriptu koja vam omogućava da lako komunicirate sa vašim Bitcoin čvorom.


Unutar btcpayserver-docker fascikle, dobij informacije o Blockchain koristeći svoj čvor:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Datoteke


BTCPay Server ima lokalni fajl sistem i otprema Store (proizvodne) resurse, logotipe i brendiranje direktno na Server. Fajl sistem Servera je dostupan samo administratorima servera; vlasnici prodavnica mogu otpremati svoje logotipe/brendiranje na nivou prodavnice.


Kada je administrator servera na kartici Skladištenje datoteka, moguće je direktno otpremiti na vaš server ili promeniti provajdera skladištenja datoteka na lokalni sistem datoteka ili Azure Blob Storage.


![image](assets/en/90.webp)


![image](assets/en/91.webp)


### Sažetak veština


U ovom odeljku, naučili ste sledeće:



- Razlika između podešavanja Prodavnice i Servera, posebno u vezi sa Korisnicima, Ulogama i Emailovima
- Postavite pravila za ceo server za korišćenje i kreiranje Lightning ili Bitcoin Hot Wallet, registraciju novih korisnika i obaveštenja putem e-pošte.
- Kako dodati prilagođene teme (umesto jednostavnih opcija svetlo/tamno koje su dostupne) kao i kreirati prilagođene logotipe
- Izvršite jednostavne zadatke održavanja servera putem pruženog GUI-ja.
- Otklonite probleme, uključujući preuzimanje detalja za bilo koji od Docker kontejnera ili vašeg čvora.
- Upravljanje skladištenjem datoteka


### Procena znanja


#### KA Konceptualni Pregled


Koja je razlika u ulogama dodeljenim putem Servera u odnosu na Podešavanja prodavnice i šta opisuje potencijalnu upotrebu jedne u odnosu na drugu?


#### KA Practical Review


Opišite neke moguće slučajeve upotrebe omogućene na kartici Politike.


#### KA Practical Review


Opišite neke radnje koje administrator može rutinski obavljati na kartici Održavanje.


## BTCPay Server - Plaćanja


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice je dokument koji prodavac izdaje kupcu radi naplate.


U BTCPay Serveru, Invoice predstavlja dokument koji mora biti plaćen u definisanom vremenskom intervalu po fiksnoj Exchange stopi. Fakture imaju rok isteka jer zaključavaju Exchange stopu unutar određenog vremenskog okvira kako bi zaštitile primaoca od fluktuacija cena.


Jezgro BTCPay Server-a je sposobnost da deluje kao sistem za upravljanje Bitcoin Invoice. Invoice je esencijalni alat za praćenje i upravljanje primljenom uplatom.


Osim ako ne koristite ugrađeni [Wallet](https://docs.btcpayserver.org/Wallet/) za ručno primanje uplata, sve uplate unutar prodavnice će biti prikazane na stranici Fakture. Ova stranica kumulativno sortira uplate po datumu i predstavlja centralni deo za upravljanje Invoice i rešavanje problema sa uplatama.


![image](assets/en/92.webp)


### General


#### Invoice statusi


Tabela ispod navodi i opisuje standardne Invoice statuse u BTCPay-u i predlaže uobičajene akcije. Akcije su samo preporuke. Na korisnicima je da definišu najbolji tok akcije za njihov slučaj upotrebe i poslovanje.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled then contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from an processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice detalji


Stranica sa detaljima Invoice sadrži sve informacije vezane za Invoice.


Informacije o Invoice se automatski kreiraju na osnovu statusa Invoice, stope Exchange, itd. Informacije o proizvodu se automatski kreiraju ako je Invoice kreiran sa informacijama o proizvodu, kao što je u aplikaciji Point of Sale.


#### Invoice filtriranje


Fakture se mogu filtrirati putem brzih filtera koji se nalaze pored dugmeta za pretragu ili naprednih filtera, koji se mogu uključiti klikom na link (Pomoć) na vrhu. Korisnici mogu filtrirati fakture po prodavnici, ID-u narudžbine, ID-u artikla, statusu ili datumu.


#### Invoice izvoz


BTCPay Server fakture mogu se izvesti u CSV ili JSON formatu. Za više informacija o Invoice izvozu i računovodstvu.


#### Vraćanje Invoice


Ako, iz bilo kog razloga, želite da izvršite povraćaj novca, možete lako kreirati povraćaj iz pregleda Invoice.


#### Arhiviranje faktura


Kao rezultat funkcije bez ponovne upotrebe Address u BTCPay Server-u, uobičajeno je videti mnogo istečenih faktura na stranici Invoice vaše prodavnice. Da biste ih sakrili iz pregleda, izaberite ih na listi i označite kao arhivirane. Fakture koje su označene kao arhivirane nisu obrisane. Plaćanje na arhiviranu Invoice će i dalje biti detektovano od strane vašeg BTCPay Server-a (status paidLate). Možete pregledati arhivirane fakture prodavnice u bilo kom trenutku izborom arhiviranih faktura iz padajućeg menija filtera pretrage.


#### Podrazumevana valuta


Podrazumevana valuta prodavnice, ovo je postavljeno u čarobnjaku za kreiranje prodavnice


#### Dozvoli bilo kome da kreira Invoice


Trebalo bi da omogućite ovu opciju ako želite da dozvolite spoljnjem svetu da kreira fakture u vašoj prodavnici. Ova opcija je korisna samo ako koristite dugme za plaćanje ili ako izdajete fakture putem API-ja ili HTML veb-sajta treće strane. PoS aplikacija je unapred autorizovana i nije potrebno omogućiti ovo da bi slučajni posetilac otvorio vašu POS prodavnicu i kreirao Invoice.


#### Dodaj dodatnu naknadu (mrežnu naknadu) na Invoice



- Samo ako kupac izvrši više od jedne uplate za Invoice
- Na svakoj uplati
- Nikada ne dodaj mrežnu naknadu


#### Invoice ističe ako ceo iznos nije plaćen nakon .. minuta.


Invoice tajmer je po podrazumevanoj vrednosti podešen na 15 minuta. Tajmer je mehanizam zaštite protiv volatilnosti jer zaključava iznos kriptovalute prema kursevima kripto u fiat. Ako kupac ne plati Invoice u definisanom periodu, Invoice se smatra isteklim. Invoice se smatra "plaćenim" čim je transakcija vidljiva na Blockchain (o-potvrda), ali se smatra "završenim" kada dostigne broj potvrda koji je trgovac definisao (obično, 1-6). Tajmer je prilagodljiv.


#### Razmotrite da je Invoice plaćen čak i ako je plaćeni iznos ..% manji od očekivanog.


U situaciji kada kupac koristi Exchange Wallet za direktno plaćanje Invoice, Exchange uzima malu naknadu. To znači da takav Invoice nije smatran potpuno završenim. Invoice dobija status "delimično plaćeno." Ako trgovac želi da prihvati nedovoljno plaćene fakture, možete postaviti procenat ovde.


### Zahtevi


Zahtevi za plaćanje su funkcija koja omogućava vlasnicima BTCPay prodavnica da kreiraju dugotrajne fakture. Sredstva se plaćaju na zahtev za plaćanje koristeći Exchange kurs u trenutku plaćanja. Ovo omogućava korisnicima da izvrše plaćanja kada im odgovara, bez pregovaranja ili verifikacije Exchange kurseva sa vlasnikom prodavnice u trenutku plaćanja.


Korisnici mogu plaćati zahteve u delimičnim uplatama. Zahtev za uplatu će ostati važeći dok se ne plati u celosti ili ako vlasnik prodavnice zahteva vreme isteka. Adrese se nikada ne koriste ponovo. Novi Address se generiše svaki put kada korisnik klikne na plaćanje kako bi se kreirao Invoice za zahtev za uplatu.


Vlasnici prodavnica mogu štampati zahteve za plaćanje (ili izvesti Invoice podatke) za vođenje evidencije i računovodstvo. BTCPay automatski označava fakture kao Zahteve za plaćanje na Invoice listi vaše prodavnice.


#### Prilagodite svoje zahteve za plaćanje



- Invoice Iznos - Postavite traženi iznos plaćanja
- Denominacija - Prikaži traženi iznos u fiat valuti ili kriptovaluti
- Količina Plaćanja - Dozvoli samo pojedinačna plaćanja ili delimična plaćanja
- Vreme isteka - Dozvoli plaćanja do određenog datuma ili bez isteka
- Opis - Tekst Editor, Tabele Podataka, Ugradnja Fotografija i Video Zapisa
- Izgled - Boja i stil sa CSS temama


![image](assets/en/93.webp)


#### Kreiraj Zahtev za Plaćanje


U levom meniju idite na Zahtjev za plaćanje i kliknite "Kreiraj zahtjev za plaćanje".


![image](assets/en/94.webp)


Obezbedite Ime Zahteva, Iznos, Prikaz Valute, Povezanu Prodavnicu, Vreme Isteka i Opis (Opcionalno)


Izaberite opciju Dozvoli primaocu da kreira fakture u njihovoj valuti ako želite da omogućite delimična plaćanja.


Kliknite Sačuvaj i Pregledaj da biste pregledali vaš zahtev za plaćanje.


BTCPay kreira URL za zahtev za plaćanje. Podelite ovaj URL da biste videli svoj zahtev za plaćanje. Trebate više istih zahteva? Možete duplicirati zahteve za plaćanje koristeći opciju Kloniraj u glavnom meniju.


![image](assets/en/95.webp)


**UPOZORENJE**


Zahtevi za plaćanje zavise od prodavnice, što znači da je svaki zahtev za plaćanje povezan sa prodavnicom tokom kreiranja. Obavezno povežite Wallet sa svojom prodavnicom kojoj pripada zahtev za plaćanje.


#### Plaćeni zahtev


Platilac i podnosilac zahteva mogu videti status zahteva za plaćanje nakon slanja uplate. Status će se prikazati kao Izmireno ako je uplata primljena u celosti. Ako su izvršene samo delimične uplate, Iznos Duga će prikazati preostali dug.


![image](assets/en/96.webp)


#### Prilagodite Zahteve za Plaćanje


Opis sadržaja može se urediti pomoću uređivača teksta zahteva za plaćanje. Oba izbora su dostupna ako želite da koristite dodatne teme boja ili prilagođeni CSS stil.


Netehnički korisnici mogu koristiti [bootstrap temu](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Dalja prilagođavanja mogu se izvršiti dodavanjem dodatnog CSS koda, kao što je prikazano ispod.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Povuci plaćanja


Tradicionalno, primalac deli svoj Bitcoin Address kako bi izvršio Bitcoin uplatu, a pošiljalac kasnije šalje novac na taj Address. Takav sistem se naziva Push uplata, jer pošiljalac inicira uplatu dok primalac može biti nedostupan, gurajući uplatu ka primaocu.


Međutim, šta je sa obrtanjem uloga?


Šta ako, umesto da pošiljalac šalje uplatu, pošiljalac dozvoli primaocu da povuče uplatu u trenutku kada to primaocu odgovara? Ovo je koncept Pull uplate. Ovo omogućava nekoliko novih primena, kao što su:



- Pretplatnička usluga (gde pretplatnik dozvoljava usluzi da povlači novac svakih x vremenskih perioda)
- Povraćaji (gde trgovac dozvoljava kupcu da povuče novac od povraćaja na svoj Wallet kada smatraju da je to prikladno)
- Obračunavanje na osnovu vremena za frilensere (gde osoba koja angažuje dozvoljava frilenseru da povlači novac na njegov Wallet kako se vreme prijavljuje)
- Patronat (gde patron omogućava primaocu da povlači novac svakog meseca kako bi nastavio da podržava njihov rad)
- Automatska prodaja (gde bi korisnik Exchange dozvolio Exchange da povlači novac sa njihovog Wallet kako bi prodavao svakog meseca automatski)
- Sistem povlačenja stanja (gde usluga sa velikim obimom omogućava korisnicima da zatraže povlačenja sa svog stanja, usluga zatim može lako grupisati sve isplate mnogim korisnicima u fiksnim intervalima)


### Isplate


Funkcionalnost isplate je povezana sa [Pull Payments](https://docs.btcpayserver.org/PullPayments/). Ova funkcija vam omogućava da kreirate isplate unutar vašeg BTCPay. Ova funkcija vam omogućava da obradite pull payment (povraćaj novca, isplate plata ili povlačenja).


#### Primer 1: Povraćaj


Hajde da počnemo sa primerom povraćaja novca. Kupac je kupio artikal u vašoj prodavnici, ali nažalost mora da ga vrati. Oni žele povraćaj novca. Unutar BTCPay-a, možete kreirati [Refund](https://docs.btcpayserver.org/Refund/) i obezbediti kupcu link da preuzme svoja sredstva. Kada god kupac unese svoj Address i preuzme sredstva, to će biti prikazano u Isplatama.


Prvi status koji ima je Čeka odobrenje. Prodavci mogu proveriti da li više njih čeka, a nakon odabira koristite dugme Radnje.


Opcije na dugmetu za akciju



- Odobri izabrane isplate
- Odobri i pošalji izabrane isplate
- Otkaži izabrane isplate


Sledeći korak je da odobrite i pošaljete odabrane isplate jer želimo da refundiramo kupca. Proverite Address kupca, prikazuje iznos i da li želimo da naknade budu oduzete od refundacije ili ne. Kada završite provere, ostaje samo potpisivanje transakcije.


Kupac sada dobija ažuriranja na stranici za potraživanje. Može pratiti transakciju jer mu je obezbeđen link ka Block explorer i njegovoj transakciji. Kada transakcija bude potvrđena, status se menja u Završeno.


#### Primer 2: Plata


Sada ćemo preći na isplatu plata, jer se ovo pokreće iznutra iz prodavnice, a ne na zahtev kupca. Osnova je ista; koristi Pull payments. Ali umesto kreiranja povraćaja, napravićemo [Pull Payment](https://docs.btcpayserver.org/PullPayments/).


Idite na karticu Pull Payments u vašem BTCPay serveru. U gornjem desnom uglu, kliknite na dugme Create Pull Payment.


Sada smo u kreiranju Isplate, dajte joj ime i željeni iznos u željenoj valuti, popunite Opis, kako bi zaposleni znao o čemu se radi. Sledeći deo je sličan povraćajima. Zaposleni popunjava Odredište Address i iznos koji želi da potražuje iz ove Isplate. Može odlučiti da napravi 2 odvojena potraživanja, na različite adrese, ili čak delimično potražuje preko lightning-a.


Ako postoji više čekajućih Isplata, možete ih grupisati za potpisivanje i slanje. Kada budu potpisane, isplate prelaze na karticu U toku i prikazuju Transakciju. Kada ih mreža prihvati, isplata prelazi na karticu Završeno. Kartica završeno služi isključivo u istorijske svrhe. Sadrži obrađene Isplate i transakciju koja im pripada.


### Povuci plaćanja


#### Koncept


Kada pošiljalac konfiguriše Pull plaćanje, može konfigurisati brojna svojstva:



- Ime zahteva za povlačenje
- Ograničena količina
- Jedinica (kao što su BTC, SAT, USD)
- Metode Plaćanja
  - BTC On-Chain
  - BTC off-chain
- Opis
- Prilagođeni CSS
- Datum završetka (opciono za Lightning Network BOLT11)


Nakon toga, pošiljalac može podeliti pull uplatu koristeći link sa primaocem, omogućavajući primaocu da kreira isplatu. Primalac će izabrati svoju isplatu:



- Koji način plaćanja koristiti
- Gde poslati novac


Jednom kada se isplata kreira, ona će se računati prema ograničenju povlačenja za tekući period. Pošiljalac će zatim odobriti isplatu postavljanjem stope po kojoj će isplata biti poslata i nastaviti sa plaćanjem.


Za pošiljaoca, pružamo jednostavan način za grupisanje plaćanja nekoliko isplata iz [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server pruža potpuni API i pošiljaocu i primaocu koji je dokumentovan na stranici `/docs` vaše instance. (ili na vebsajtu sa dokumentacijom https://docs.btcpayserver.org)


Pošto naš API izlaže punu sposobnost povlačenja plaćanja, pošiljalac može automatizovati plaćanja prema svojim potrebama.


### Sažetak veština


U ovom odeljku ste naučili sledeće:



- Detaljno razumevanje BTCPay Server-ovih Invoice statusa kao i radnji koje se mogu izvršiti nad njima
- Prilagodite i upravljajte mehanizmima produženog veka Invoice poznatim kao Zahtevi.
- Dodatne fleksibilne mogućnosti plaćanja otvorene su jedinstvenom funkcijom Pull Payment na BTCPay Server-u, posebno kako rukovati povratima i isplatama plata.


### Procena znanja


#### KA Konceptualni Pregled


Koje su neke razlike između faktura i zahteva za plaćanje, i koji bi mogao biti dobar razlog za korišćenje potonjeg?


#### KA Konceptualni Pregled


Kako pull plaćanja proširuju ono što se obično može uraditi On-Chain? Opišite neke slučajeve upotrebe koje omogućavaju.


## Podrazumevani Dodaci za BTCPay Server


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Podrazumevani Pluginovi i Aplikacije


BTCPay server dolazi sa standardnim setom Pluginova (Aplikacija) koji mogu pretvoriti BTCPay Server u e-commerce platni prolaz. Sa dodatkom Point Of Sale, Crowdfund platforme i jednostavnog Pay dugmeta, BTCPay Server postaje lako rešenje za implementaciju.


### Point Of Sale


Jedan od standardnih dodataka BTCPay Server-a je Point of Sale (PoS). Sa PoS dodatkom, vlasnik prodavnice može kreirati Webshop direktno iz BTCPay Server-a, vlasniku prodavnice nisu potrebna rešenja trećih strana za e-trgovinu da bi vodio Webshop. Web-bazirana PoS aplikacija omogućava korisnicima sa fizičkim prodavnicama da lako prihvate Bitcoin, bez naknada ili treće strane, direktno na njihov Wallet. PoS se može lako prikazati na tabletima ili drugim uređajima koji podržavaju pretraživanje interneta. Korisnici mogu lako kreirati prečicu na početnom ekranu kako bi brzo pristupili web aplikaciji.


#### Kako kreirati novu prodajnu tačku


BTCPay Server omogućava vlasnicima prodavnica da brzo kreiraju prodajno mesto u više rasporeda. BTCPay Server prepoznaje da nije svaka prodavnica e-trgovina, i da nije svaka prodavnica bar ili restoran, te dolazi sa više standardnih podešavanja za vaš PoS.


Kada vlasnik prodavnice klikne na "Point of Sale" u svojoj levoj traci menija, BTCPay Server će sada tražiti ime; ovo ime će biti vidljivo u levoj traci menija. Kliknite Kreiraj da biste kreirali PoS.


![image](assets/en/97.webp)


#### Ažuriraj novo kreirani Point of Sale


Nakon kreiranja novog PoS-a, sledeći ekran će biti za ažuriranje vaše prodajne tačke i dodavanje artikala za vašu prodavnicu.


##### Ime aplikacije


Naziv koji ovde date vašem prodajnom mestu biće vidljiv u glavnom meniju BTCPay Servera.


##### Prikaži Naslov


Javnost će videti javni naslov ili ime kada poseti vašu prodavnicu. BTCPay Server standardno imenuje vašu prodavnicu „Tea shop“. Zamenite ovo imenom vaše prodavnice.


![image](assets/en/98.webp)


#### Izaberite stil prodajnog mesta


BTCPay Server je sposoban prikazati svoj Point Of Sale na više načina.



- Lista proizvoda
  - Prikaz prodavnice gde kupci mogu kupiti samo 1 proizvod odjednom.
- Lista proizvoda sa korpom.
  - Prikaz prodavnice gde kupci mogu kupiti više artikala odjednom i dobiti pregled korpe za kupovinu sa desne strane ekrana.
- Samo tastatura
  - Nema liste proizvoda, samo tastatura za direktno fakturisanje.
- Štampaj prikaz (Štampaj lista proizvoda sa QR)
  - Ako ne možete uvek prikazati svoju listu proizvoda digitalno, potrebna vam je "offline" rešenje za proizvode; BTCPay Server ima opciju štampanja za prikazivanje kao Offline prodavnica.


![image](assets/en/99.webp)


#### Stil prodajnog mesta - Lista proizvoda


![image](assets/en/100.webp)


#### Stil prodajnog mesta - Lista proizvoda + Korpa


![image](assets/en/101.webp)


#### Stil prodajnog mesta - Samo tastatura


![image](assets/en/102.webp)


#### Stil prodajnog mesta - Prikaz štampe


![image](assets/en/103.webp)


#### Valuta


Vlasnik prodavnice može postaviti drugačiju valutu za svoj Point of Sale od svoje ukupno postavljene podrazumevane valute. Podrazumevana valuta prodavnice će automatski popuniti ovo polje.


#### Opis


Recite svetu o svojoj prodavnici; šta prodajete i po kojoj ceni? Sve što objašnjava vašu prodavnicu ide ovde.


![image](assets/en/104.webp)


#### Proizvodi


Kada se kreira prodajno mesto, standardni BTCPay Server dodaje nekoliko stavki u prodavnicu za referencu. Kliknite na dugme Izmeni na bilo kojoj od standardnih stavki da biste bolje razumeli svaku moguću opciju za stavku.


Kreiranje novog proizvoda u vašoj prodavnici sastoji se od sledećih polja;



- Naslov
- Cena (fiksna, minimalna ili prilagođena)
- URL slike
- Opis
- Inventar
- ID
- Tekst Dugmeta za Kupovinu.
- Omogući/Onemogući


Kada vlasnik prodavnice popuni sva polja za nove proizvode, kliknite na sačuvaj, i primetićete da se sekcija Proizvodi u prodajnom mestu sada popunjava. Uvek se pobrinite da sačuvate u gornjem desnom uglu ekrana kako biste izbegli da vlasnici prodavnica izgube svoj napredak u dodavanju proizvoda.


Vlasnici prodavnica takođe mogu koristiti "Raw Editor" za konfigurisanje svojih proizvoda. Raw editor zahteva osnovno razumevanje JSON struktura.


![image](assets/en/105.webp)


#### Checkout


BTCPay Server omogućava malu prilagođenu naplatu specifičnu za PoS. Vlasnik prodavnice može postaviti tekst "Kupi za x" ili zatražiti specifične podatke o kupcu dodavanjem u obrasce.


#### Saveti


Samo nekim prodavnicama je potrebna opcija za napojnice na njihovim prodajama. Vlasnici prodavnica mogu uključiti ili isključiti ovu opciju prema potrebi svoje prodavnice. Ako prodavnica koristi uključene napojnice, vlasnik prodavnice može postaviti tekst u polju za napojnice koji želi. BTCPay Server napojnice funkcionišu na osnovu procentualnog iznosa. Vlasnici prodavnica mogu dodati više procenata sa razdvajanjem zarezima.


#### Popusti


Kao vlasnik prodavnice, možda ćete želeti da kupcu date prilagođeni popust na kasi; prekidač za Popuste postaje dostupan na kasi vaše prodavnice. Međutim, ovo se veoma ne preporučuje kod sistema za samoposlugu.


#### Prilagođena Plaćanja


Kada je opcija Prilagođena Plaćanja uključena, kupac može uneti svoju cenu koja je jednaka ili veća od originalne Invoice generisane od strane prodavnice.


#### Dodatne opcije


Nakon što postavite sve za vašu prodajnu tačku, ostaju neke dodatne opcije. Vlasnici prodavnica mogu lako ugraditi svoju prodajnu tačku putem Iframe-a ili ugraditi dugme za plaćanje koje vodi do određenog artikla u prodavnici. Da bi stilizovali upravo kreiranu prodavnicu, vlasnici mogu dodati prilagođeni CSS na dnu dodatnih opcija.


#### Izbriši ovu aplikaciju


Ako vlasnik prodavnice želi potpuno obrisati Point of Sale sa svog BTCPay Server-a, na dnu ažuriranja PoS-a, vlasnici prodavnica mogu kliknuti na dugme Delete this app kako bi potpuno uništili svoju PoS aplikaciju. Kada kliknu na "Delete this app", BTCPay Server će tražiti potvrdu unosom `DELETE` i potvrdom klikom na dugme Delete. Nakon brisanja, vlasnik prodavnice se vraća na BTCPay Server kontrolnu tablu.


### BTCPay Server - Crowdfund


Pored dodatka za prodajno mesto, BTCPay Server ima opciju za kreiranje crowdfund-a. Kao i na bilo kojoj drugoj platformi za crowdfund, vlasnici prodavnica mogu postaviti cilj, kreirati pogodnosti za doprinose i prilagoditi ga svojim potrebama.


#### Kako postaviti novi crowdfund


Kliknite na Crowdfund dodatak kroz glavni meni sa leve strane vašeg BTCPay Server-a, ispod sekcije Dodataka. BTCPay Server će sada zatražiti ime za Crowdfund; ovo ime će takođe biti prikazano u levoj traci menija.


![image](assets/en/106.webp)


#### Ažuriraj novo kreirani Point of Sale


Kada se Aplikaciji dodeli ime, njen sledeći ekran će biti ažuriranje Aplikacije kako bi imala kontekst.


#### Ime aplikacije


Ime koje date vašem Crowdfund-u biće vidljivo u glavnom meniju BTCPay Server-a.


#### Prikaži Naslov


Naslov je dat za Crowdfund za javnost.


#### Tagline


Dajte crowdfundu kratak opis koji prepoznaje svrhu prikupljanja sredstava.


![image](assets/en/107.webp)


#### Istaknuta URL adresa slike


Svaki crowdfund ima svoju glavnu sliku, onu baner sliku koju odmah prepoznajete. Ova slika može biti sačuvana na vašem serveru ako imate Administratorska prava, Admini mogu da otpremaju pod BTCPay Server Server podešavanjima - Fajlovi. Kada ste vlasnik Prodavnice, slika mora biti otpremljena na web putem treće strane hosta (na primer imgur).


#### Objavi Crowdfund


Ovaj prekidač čini vaš Crowdfund javnim i time vidljivim za spoljašnji svet. Za potrebe testiranja ili da biste videli da li je vaša tema ispravno primenjena, možda ćete želeti da ovo ostavite isključenim tokom perioda izrade crowdfund-a.


#### Opis


Recite svetu o svom Crowdfund-u, za šta prikupljate sredstva? Sve što objašnjava vaš crowdfund ide ovde.


![image](assets/en/108.webp)


#### Cilj grupnog finansiranja


Postavite ciljanu sumu koju bi prikupljanje sredstava trebalo da prikupi za projekat i u kojoj valuti bi cilj trebalo da bude izražen. Ukoliko su vaši ciljevi postavljeni između određenih datuma, uključite ove početne i krajnje datume ispod Ciljeva u crowdfund-u.


![image](assets/en/109.webp)


#### Pogodnosti


Pogodnosti mnogo pomažu vašem crowdfunding-u. Ovo je zato što pogodnosti ljudima daju način da učestvuju u vašoj kampanji. One se oslanjaju na sebične motive, kao i na dobronamerne motive. I omogućavaju vam pristup potrošnji vaših pristalica, ne samo njihovoj filantropskoj kesi -- možete pogoditi koja je značajnija.


Kreiranje nove pogodnosti sastoji se od sledećih polja ;



- Naslov
- Cena (fiksna, minimalna ili prilagođena)
- URL slike
- Opis
- Inventar
- ID
- Tekst Dugmeta za Kupovinu.
- Omogući/Onemogući


Kada vlasnik prodavnice popuni sva polja za novu pogodnost koju treba kreirati, kliknite na sačuvaj, i primetićete da se odeljak Pogodnosti u crowdfunds sada popunjava.


![image](assets/en/110.webp)


### BTCPay Server - Point Of Sale


#### Doprinosi


Vlasnici prodavnica mogu izabrati kako će prikazati pogodnosti, kako su sortirane ili čak rangirane u odnosu na druge pogodnosti. Međutim, kada se ciljevi Crowdfund-a postignu, vlasnici prodavnica možda žele da zaustave prilive donacija ka ovom prikupljanju sredstava. Stoga, on može uključiti opciju "Ne dozvoli dodatne doprinose nakon dostizanja cilja". Ovo će zaustaviti Crowdfund od prihvatanja donacija.


##### Ponašanje u crowdfundingu


Crowdfund-ov standard računa samo fakture kreirane putem Crowdfund-a prema cilju. Međutim, mogu postojati slučajevi kada vlasnik prodavnice želi da sve fakture napravljene u ovoj prodavnici budu uračunate u crowdfund.


#### Dodatne opcije za prilagođavanje


BTCpay Server nudi nekoliko dodatnih prilagođavanja. Dodajte zvukove, animacije ili čak diskusione niti u Crowdfund. Vlasnici prodavnica takođe mogu promeniti izgled i doživljaj Crowdfund-a unosom sopstvenog prilagođenog CSS-a.


#### Izbriši ovu aplikaciju


Ako vlasnik prodavnice želi potpuno obrisati Crowdfund sa svog BTCPay Server-a, na dnu ažuriranja Crowdfund-a vlasnici prodavnica mogu kliknuti na dugme „Delete this app“ kako bi potpuno uništili svoju Crowdfund aplikaciju. Kada kliknu na "Delete this app", BTCPay Server će tražiti potvrdu unosom `DELETE` i potvrdom klikom na dugme Delete. Nakon brisanja, vlasnik prodavnice se vraća na BTCPay Server kontrolnu tablu.


### BTCPay Server - Dugme za plaćanje


HTML koji se lako ugrađuje i visoko prilagodljivi dugmići za plaćanje omogućavaju vlasnicima prodavnica da primaju napojnice i donacije. U levom meniju BTCPay Server-a, ispod sekcije Plugins, vlasnici prodavnica mogu kliknuti na “Pay Button” i kliknuti na Enable kako bi kreirali dugme za plaćanje.


#### Opšta podešavanja


U okviru Opštih Postavki za Dugme za Plaćanje, vlasnici prodavnica mogu postaviti



- Standardna cena
- Podrazumevana valuta
- Podrazumevani način plaćanja
  - Koristi podrazumevane vrednosti prodavnice
  - BTC On-Chain
  - BTC off-chain (Lightning)
  - BTC off-chain (LNURL-pay)
- Opis naplate
- ID porudžbine


#### Prikaži opcije


BTCPay Server-ovo dugme za plaćanje može se konfigurisati da odgovara različitim stilovima. Dugmad mogu imati fiksni ili prilagođeni iznos, prikazan sa klizačem ili plus i minus prekidačima.


#### Koristi Modal


Kada kreiraju dugme za plaćanje, vlasnici prodavnica mogu izabrati njegovo ponašanje kada ga kupac klikne i prikazati ga u modalnom prozoru ili kao novu stranicu.


**!?Napomena!?**


Upozorenje: Dugme za plaćanje treba koristiti samo za napojnice i donacije


Korišćenje dugmeta za plaćanje za e-commerce integracije se ne preporučuje jer korisnik može izmeniti informacije relevantne za narudžbinu. Za e-commerce, trebalo bi da koristite naš Greenfield API. Ako ova prodavnica obrađuje komercijalne transakcije, savetujemo vam da kreirate zasebnu prodavnicu pre korišćenja dugmeta za plaćanje.


#### Prilagodi tekst dugmeta za plaćanje


Podrazumevano, BTCPay Server-ovo dugme za plaćanje navodi "Plati sa BTCPay". Vlasnici prodavnica mogu postaviti ovaj tekst po svojoj želji i promeniti BTCPay Server logo u svoj. Postavite tekst koristeći "Tekst Dugmeta za Plaćanje" i nalepite URL slike ispod "URL Slike Dugmeta za Plaćanje".


##### Veličina slike


Veličina slike na dugmetu može biti postavljena samo na tri podrazumevane vrednosti.



- 146x40px
- 168x46px
- 209x57px


#### Tipka Tip


BTCPay Server zna za tri stanja za dugme za plaćanje.



- Fiksni iznos
  - Prethodno postavljena cena nalazi se u opštim podešavanjima dugmeta.
- Prilagođeni iznos
  - BTCPay Server-ovo dugme za plaćanje ima + i - prekidače za postavljanje prilagođene cene.
  - Kada koristite prilagođeni iznos, BTCPay Server će zahtevati Min, Max i koliko postepeno treba da se poveća.
  - Dugmad mogu biti postavljena na „Koristi jednostavan stil unosa“. Ovo uklanja +/- prekidače.
  - Prilagodite dugme u liniji gde se dugme i prekidači pojavljuju u liniji.
- Klizač
  - Slično prilagođenom iznosu, međutim, vizuelno drugačije jer ima klizač umesto +/- prekidača.
  - Kada koristite klizač, BTCPay Server će zahtevati Min, Max i koliko postepeno treba da se povećava.


**!?Napomena!?**


Brisanje dugmeta za plaćanje može se izvršiti na vrhu u opisu upozorenja.


#### Obaveštenja o uplati


Server IPN (Instant Payment Notification) je namenjen za webhooks i može biti popunjen URL-om za post-purchase podatke.


#### Obaveštenja putem e-pošte


Kad god se izvrši plaćanje, BTCPay Server može obavestiti vlasnika prodavnice.


#### Preusmeravanje pregledača


Kada kupac završi kupovinu, biće preusmeren na ovaj link ako ga je postavio vlasnik prodavnice.


#### Opcije za unapred plaćanje


Navedite dodatne parametre niza upita koji bi trebalo da budu dodati na stranicu za naplatu kada se kreira Invoice. Na primer, `lang=da-DK` bi učitao stranicu za naplatu na danskom jeziku po defaultu.


#### Koristite aplikaciju kao krajnju tačku


Direktno povežite dugme za plaćanje sa stavkom u jednoj od PoS ili Crowdfund aplikacija od ranije.


Vlasnici prodavnica mogu kliknuti na padajući meni i odabrati željenu aplikaciju; kada je aplikacija odabrana, vlasnik prodavnice može dodati stavku koju treba povezati.


#### Generisani Kod


Kako je BTCPay Server-ovo dugme za plaćanje lako-ugradivi HTML, BTCPay Server prikazuje generisani kod za kopiranje na vebsajt na dnu nakon konfigurisanja dugmeta za plaćanje.


Vlasnici prodavnica mogu kopirati generisani kod na svoj vebsajt, i dugme za plaćanje sa BTCPay Server-a je direktno aktivno na njihovom vebsajtu.


#### Obaveštenja o uplati


IPN server (Instant Payment Notification) je namenjen za webhooks i može biti popunjen URL-om za postavljanje podataka o kupovini.


#### Obaveštenja putem e-pošte


Kad god se izvrši plaćanje, BTCPay Server može obavestiti vlasnika prodavnice.


#### Preusmeravanje pregledača


Kada kupac završi kupovinu, biće preusmeren na ovaj link ako ga je postavio vlasnik prodavnice.


#### Opcije za unapred plaćanje


Navedite dodatne parametre niza upita koji bi trebalo da budu dodati na stranicu za naplatu kada se Invoice kreira. Na primer, `lang=da-DK` bi učitao stranicu za naplatu na danskom jeziku po defaultu.


#### Koristite aplikaciju kao krajnju tačku


Direktno povežite dugme za plaćanje sa stavkom u jednoj od PoS ili Crowdfund aplikacija od ranije. Vlasnici prodavnica mogu kliknuti na padajući meni i izabrati željenu aplikaciju, kada je aplikacija izabrana, vlasnik prodavnice može dodati stavku koja treba da bude povezana.


#### Generisani kod


Kako je BTCPay Server-ovo dugme za plaćanje lako-ugradivi HTML, BTCPay Server prikazuje generisani kod za kopiranje na vebsajt na dnu nakon konfigurisanja dugmeta za plaćanje. Vlasnici prodavnica mogu kopirati generisani kod na svoj vebsajt i dugme za plaćanje sa BTCPay Server-a je direktno aktivno na njihovom vebsajtu.


### Sažetak veština


U ovom odeljku ste naučili:



- Kako koristiti integrisani PoS dodatak BTCPay Server-a za jednostavno kreiranje prilagođene prodavnice
- Kako koristiti integrisani Crowdfund dodatak BTCPay Server-a za jednostavno kreiranje prilagođene crowdfund aplikacije
- Generisanje koda za prilagođeno dugme za plaćanje koristeći Pay Button dodatak


### Procena znanja


#### KA Review


Koja su tri ugrađena dodatka koja dolaze standardno sa BTCPay Serverom? U nekoliko reči, opišite kako se svaki može koristiti.


# Konfigurisanje BTCPay Servera


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Osnovno razumevanje instalacije BTCPay Server-a na LunaNode okruženju


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Instaliranje BTCPay Servera na hostovanoj okolini (LunaNode)


Ovi koraci će obezbediti sve potrebne informacije za početak korišćenja BTCPay Server-a na LunaNode. Postoji mnogo opcija kako da se softver implementira.

Možete pronaći sve detalje o BTCPay Server-u na https://docs.btcpayserver.org.


#### Gde da počnemo?


U ovom delu, upoznaćete se sa LunaNode kao provajderom hostinga, naučiti o prvim koracima korišćenja vašeg BTCPay Server-a, i naučiti kako da radite sa Lightning Network. Nakon što prođemo kroz sve korake, možete pokrenuti veb prodavnicu ili platformu za crowdfunding koja prihvata Bitcoin!


Ovo je jedan od mnogih načina za implementaciju BTCPay Servera. Pročitajte našu dokumentaciju za više detalja,


https://docs.btcpayserver.org.


### BTCPay Server - LunaNode deployment


#### LunaNode implementacija


Prvo, idite na vebsajt LunaNode.com, gde ćemo kreirati novi nalog. Kliknite na Sign Up u gornjem desnom uglu ili koristite Get Started čarobnjak na njihovoj početnoj stranici.


![image](assets/en/111.webp)


Nakon što kreirate svoj novi nalog, LunaNode šalje verifikacioni email. Kada verifikujete nalog, u poređenju sa Voltage, odmah vam se prikazuje opcija da dopunite stanje na nalogu. Ovo stanje je potrebno za plaćanje prostora na serveru i troškova hostinga.


![image](assets/en/112.webp)


#### Dodajte kredit na svoj LunaNode nalog


Kada kliknete na "Deposit credit", možete da odredite koliko želite da dopunite svoj račun i kako želite da platite. LunaNode i BTCPay Server će koštati između 10$USD i 20$USD mesečno.

U poređenju sa Voltage.cloud, dobijate potpuni pristup svom Virtual Private Server-u (VPS od sada) i stoga imate veću kontrolu nad svojim serverom. Nakon što kreirate svoj novi nalog, LunaNode šalje verifikacioni email.

Jednom kada verifikujete nalog, u poređenju sa Voltage, sada vam se odmah nudi mogućnost da dopunite stanje na vašem nalogu. Ovo stanje je potrebno za plaćanje prostora na serveru i troškova hostinga.


#### Kako postaviti novi server?


U ovom vodiču ćemo proći kroz postavljanje kreiranjem skupa API ključeva i korišćenjem BTCPay Server pokretača koji je napravio LunaNode.


U vašem LunaNode kontrolnom panelu, kliknite na API u gornjem desnom uglu. Ovo će otvoriti novu stranicu. Potrebno je samo da postavite Ime za API ključ. Ostalo će biti rešeno od strane LunaNode i neće biti pokriveno u ovom vodiču. Kliknite na dugme Create API Credential.

Nakon kreiranja API akreditiva, dobićete dugačak niz slova i karaktera. Ovo je vaš API ključ.


![image](assets/en/113.webp)


#### Kako postaviti novi server?


Postoje 2 dela ovih akreditiva, API ključ i API ID; biće nam potrebna oba. Pre nego što pređemo na sledeći korak, hajde da otvorimo drugu karticu u pregledaču i odemo na https://launchbtcpay.lunanode.com/


Ovde će vam biti zatraženo da unesete svoj API ključ i API ID. Ovo je da bi se verifikovalo da ste vi taj koji obezbeđuje ovaj novi server. API ključ bi trebalo da bude otvoren u vašem prethodnom tabu; ako se pomerite naniže u tabeli ispod, pronaći ćete API ID.


Vratite se na stranicu sa Pokretačem, popunite polja sa vašim API ključem i ID-om, i kliknite na nastavi.


![image](assets/en/114.webp)


U sledećem koraku, možete obezbediti ime domena. Ako već posedujete domen i želite da ga koristite za BTCPay Server, obavezno dodajte i DNS zapis (nazvan `A` zapis) na vašem domenu. Ako ne posedujete domen, koristite domen koji obezbeđuje LunaNode (možete ga kasnije promeniti u BTCPay Server podešavanjima) i kliknite Nastavi.


Pročitajte više o postavljanju ili promeni DNS zapisa za BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Pokreni BTCPay Server na LunaNode


Nakon što preduzmemo prethodne korake, možemo postaviti sve opcije za naš novi server. Ovde ćemo izabrati Bitcoin (BTC) kao našu Podržanu valutu; možemo postaviti email za obaveštenja o enkripcijskim sertifikatima za potrebe obnove; ovo nije obavezno.


Ovaj vodič ima za cilj postavljanje Mainnet okruženja (stvarni svet Bitcoin); međutim, LunaNode takođe omogućava da ovo postavite na Testnet ili Regtest za potrebe razvoja. Ostavićemo ga na Mainnet opciji za ovaj vodič.


Izaberite svoju Lightning implementaciju. LunaNode nudi dve različite implementacije, LND i Core Lightning. Za ovaj vodič, uzećemo LND. Postoje male, ali stvarne razlike u obe implementacije; za više o tome, preporučujemo čitanje opsežne dokumentacije; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/115.webp)


LunaNode nudi više planova za virtuelne mašine (VM). Oni se razlikuju u cenovnim rangovima i specifikacijama servera. Za ovaj vodič, m2 plan će biti dovoljan; međutim, ako ste označili više od samo Bitcoin kao valutu, razmislite o korišćenju barem m4.


Ubrzajte početnu Blockchain sinhronizaciju; ovo je opcionalno i zavisi od vaših potreba. Postoje napredne opcije kao što su postavljanje Lightning Alias-a, usmeravanje na određeno GitHub izdanje ili postavljanje SSH ključeva; nijedna od ovih opcija neće biti obrađena u ovom vodiču.


Nakon što popunite obrazac, morate kliknuti na Launch VM, i Lunanode će početi sa kreiranjem vašeg novog VM-a, uključujući instaliran BTCPay Server na njemu. Ovaj proces traje nekoliko minuta; kada vaš server bude spreman, LunaNode će vam dati link do vašeg novog BTCPay Servera.


Nakon procesa kreiranja, kliknite na link ka vašem BTCPay Server-u; ovde će vam biti zatraženo da kreirate Administrator nalog.


![image](assets/en/116.webp)


### Sažetak veština


U ovom odeljku ste naučili:



- Kreiranje i finansiranje naloga na LunaNode
- Korišćenje BTCPay Server Launchera za kreiranje sopstvenog servera


### Procena znanja


#### KA Konceptualni Pregled


Opiši neke od razlika između pokretanja instance BTCPay Servera na VPS-u i kreiranja naloga na hostovanoj instanci.


## Instaliranje BTCPay Servera na Voltage okruženju


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Upoznaćete se sa Voltage.cloud kao provajderom hostinga, naučiti o prvim koracima korišćenja vašeg BTCPay Server-a, i naučiti kako da koristite Lightning Network. Nakon što prođemo kroz sve korake, možete pokrenuti veb prodavnicu ili platformu za crowdfunding koja prihvata Bitcoin!


Ovo je jedan od mnogih načina za implementaciju BTCPay Servera. Pročitajte našu dokumentaciju za više detalja,

https://docs.btcpayserver.org.


### BTCPay Server - Voltage.cloud deployment


Prvo, idite na vebsajt Voltage.cloud i registrujte se za novi nalog. Kada kreirate nalog, možete se prijaviti za besplatni probni period od 7 dana. Ili kliknite na "Sign Up" u gornjem desnom uglu ili koristite opciju "Try a free 7 day trial" na njihovoj početnoj stranici.


![image](assets/en/117.webp)


Nakon što ste napravili nalog, kliknite na dugme `NODES` na vašoj kontrolnoj tabli. Kada odaberemo Nodes i kreiramo novi čvor, biće nam prikazane moguće ponude napona čvora. Kako će ovaj vodič takođe pokriti LightningNetwork, na Voltage-u prvo moramo izabrati našu Lightning implementaciju pre nego što kreiramo BTCPay Server. Kliknite na LightningNode.


![image](assets/en/118.webp)


Ovde ćete morati da izaberete kakvu vrstu Lightning čvora želite. Voltage ima razne opcije za vašu rasvetu. Ovo je drugačije kada se koristi, na primer, LunaNode. Za svrhe ovog vodiča, Lite Node će biti dovoljan. Pročitajte više o razlikama na Voltage.cloud.


![image](assets/en/119.webp)


Dajte svom čvoru Ime, postavite lozinku i osigurajte ovu lozinku. Ako se ova lozinka izgubi, gubite pristup svojim rezervnim kopijama, a Voltage je ne može povratiti. Kreirajte čvor, a Voltage vam prikazuje napredak. Voltage je kreirao vaš Lightning čvor. Sada možemo kreirati BTCPay Server instancu i direktno pristupiti Lightning Network.


Kliknite na Nodes u gornjem levom uglu vaše kontrolne table. Ovde možete postaviti sledeći deo vaše BTCPay Server instance. Kliknite na "create new" kada ste u pregledu čvorova. Dobijate sličan ekran kao ranije. Sada umesto Lightning Node, biramo BTCPay Server.


Napon vam pokazuje geolokaciju vašeg BTCPay Server-a, napon hostuje u regionu zapadnog dela SAD-a. Ovde ćete takođe videti trošak hostovanja servera. Kliknite na Kreiraj i dajte svom BTCPay Server-u ime. Omogućite Lightning i napon vam pokazuje Lightning čvor kreiran u prethodnom koraku. Kliknite na Kreiraj, i napon će kreirati instance BTCPay Server-a.


![image](assets/en/120.webp)


Nakon što kliknete na kreiranje, Voltage vam prikazuje podrazumevano korisničko ime i lozinku. Oni su slični vašoj prethodnoj postavljenoj lozinci u Voltage. Kliknite na dugme Prijava na nalog da biste bili preusmereni na vaš BTCPay Server.


Dobrodošli u vašu novu BTCPay Server instance. Kako smo već postavili Lightning u procesu kreiranja, pokazuje vam da je Lightning već omogućen!


### Sažetak veština


U ovom poglavlju ste naučili:



- Kreiranje naloga na Voltage.cloud
- Koraci za pokretanje BTCPay Server-a zajedno sa Lightning čvorom na nalogu


### Procena znanja


#### KA Konceptualni Pregled


Koje su neke ključne razlike između Voltage i LunaNode postavki?


## Instaliranje BTCPay Servera na Umbrel čvor


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Na kraju ovih koraka, možete prihvatati lightning uplate u vašoj BTCPay prodavnici na vašoj lokalnoj mreži. Ovaj proces će se takođe primeniti ako pokrećete umbrel čvor u restoranu ili poslovanju. Ako želite da povežete ovu prodavnicu sa javnim veb-sajtom, pratite Naprednu vežbu da izložite vaš umbrel čvor javnosti.


https://umbrel.com/


![image](assets/en/121.webp)


### BTCPay Server - Umbrel deployment


Nakon što se vaš Umbrel čvor potpuno sinhronizuje sa Bitcoin Blockchain, idite u Umbrel App Store i potražite BTCPay Server ispod Aplikacija.


![image](assets/en/122.webp)


Kliknite na BTCPay Server da biste videli detalje aplikacije. Kada su detalji otvoreni za BTCPay Server, u donjem desnom uglu prikazuju se zahtevi za pravilno funkcionisanje aplikacije. Prikazuje da su potrebni Bitcoin i Lightning čvor. Ako niste instalirali Lightning čvor na vašem Umbrel-u, kliknite na Instaliraj. Ovaj proces može potrajati nekoliko minuta.


![image](assets/en/123.webp)


Nakon instalacije vašeg lightning čvora:


1. Kliknite na otvori u detaljima aplikacije ili na Aplikaciju na Umbrels kontrolnoj tabli.

2. Kliknite na postavljanje novog čvora; biće vam prikazane 24 reči za oporavak vašeg lightning čvora.

3. Zapiši ovo.


![image](assets/en/124.webp)


Umbrel će tražiti verifikaciju upravo napisanih reči. Nakon što je Lightning čvor postavljen, vratite se u Umbrel App Store i pronađite BTCPay Server. Kliknite na dugme za instalaciju, i Umbrel će prikazati da li su potrebne komponente instalirane i da BTCPay Server zahteva pristup tim komponentama. Nakon instalacije, kliknite na Otvori u gornjem desnom uglu detalja aplikacije ili otvorite BTCPay Server preko vašeg Umbrel kontrolnog panela.


Umbrel će tražiti verifikaciju za upravo napisane reči.


![image](assets/en/125.webp)


**!?Napomena!?**


Pobrinite se da ih skladištite na odgovarajućem mestu kao što ste ranije naučili sa skladištenjem ključeva.


Nakon što je Lightning čvor postavljen, vratite se u Umbrel App Store i pronađite BTCPay Server. Kliknite na dugme za instalaciju, i Umbrel će pokazati da li su potrebne komponente instalirane i da BTCPay Server zahteva pristup tim komponentama.


![image](assets/en/126.webp)


Nakon instalacije, kliknite na Open u gornjem desnom uglu detalja aplikacije ili otvorite BTCPay Server preko vaše Umbrels kontrolne table.


![image](assets/en/127.webp)


### Sažetak veština


U ovom odeljku ste naučili:



- Koraci za instalaciju BTCPay Server-a sa Lightning funkcionalnošću na Umbrel čvoru


### Procena znanja


#### KA Konceptualni Pregled


Kako se postavljanje na Umbrel razlikuje od prethodne dve hostovane opcije?


# Završni Deo


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Recenzije i ocene

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Zaključak kursa


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>