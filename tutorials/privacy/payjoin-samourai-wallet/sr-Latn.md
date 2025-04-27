---
name: PayJoin - Samourai Wallet
description: Kako izvršiti PayJoin transakciju na Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)


***PAŽNJA:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, Payjoins Stowaway na Samourai Wallet funkcioniše samo ručnom razmenom PSBT između uključenih strana, pod uslovom da su oba korisnika povezana na svoj Dojo. Što se tiče Sparrow-a, Payjoins putem BIP78 i dalje rade. Međutim, moguće je da će ovi alati biti ponovo pokrenuti u narednim nedeljama. U međuvremenu, možete pročitati ovaj članak da biste razumeli teorijsko funkcionisanje Stowaway.*


_Ako planirate da ručno izvršite Stowaway, procedura je veoma slična onoj opisanoj u ovom vodiču. Glavna razlika je u izboru tipa Stowaway transakcije: umesto da izaberete `Online`, kliknite na `In Person / Manual`. Zatim ćete morati ručno da Exchange PSBT-ove kako biste konstruisali Stowaway transakciju. Ako ste fizički blizu svog saradnika, možete skenirati QR kodove uzastopno. Ako ste na udaljenosti, JSON fajlovi se mogu razmeniti putem sigurnog komunikacionog kanala. Ostatak vodiča ostaje nepromenjen._


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije postanu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Naterajte špijune Blockchain da preispitaju sve što misle da znaju.*

PayJoin je specifična struktura transakcije Bitcoin koja poboljšava privatnost korisnika tokom trošenja kroz saradnju sa primaocem plaćanja. Postoji nekoliko implementacija koje olakšavaju postavljanje i automatizaciju PayJoin. Među tim implementacijama, najpoznatija je Stowaway, koju su razvili timovi u Samourai Wallet. Ovaj vodič objašnjava kako izvršiti Stowaway PayJoin transakciju koristeći Samourai Wallet aplikaciju.


## Kako funkcioniše Stowaway?


Kao što je ranije pomenuto, Samourai Wallet nudi alat PayJoin pod nazivom "Stowaway." Dostupan je putem softvera Sparrow Wallet na PC-ju ili aplikacije Samourai Wallet na Androidu. Da bi se izvršio PayJoin, primalac, koji takođe deluje kao saradnik, mora koristiti softver kompatibilan sa Stowaway, naime Sparrow ili Samourai. Ova dva softvera su interoperabilna, omogućavajući Stowaway transakciju između Sparrow Wallet i Samourai Wallet, i obrnuto.


Stowaway se oslanja na kategoriju transakcija koju Samourai naziva "Cahoots." Cahoot je u suštini kolaborativna transakcija između više korisnika, koja zahteva off-chain informacije Exchange. Do danas, Samourai nudi dva Cahoots alata: Stowaway (Payjoins) i StonewallX2 (koji ćemo istražiti u budućem članku).


Transakcije u dosluhu uključuju razmene delimično potpisanih transakcija između korisnika. Ovaj proces može biti dugotrajan i nezgrapan, posebno kada se obavlja na daljinu. Međutim, i dalje se može ručno izvesti sa drugim korisnikom, što može biti zgodno ako su saradnici fizički blizu. U praksi, ovo uključuje ručnu razmenu pet QR kodova koji se sukcesivno skeniraju.


Kada se radi na daljinu, ovaj proces postaje previše složen. Da bi se rešio ovaj problem, Samourai je razvio šifrovani komunikacioni protokol zasnovan na Tor-u, nazvan "Soroban." Sa Soroban-om, razmene neophodne za PayJoin su automatizovane iza korisnički prijatnog Interface. Ovo je druga metoda koju ćemo proučiti u ovom članku.


Ove šifrovane razmene zahtevaju uspostavljanje veze i autentifikaciju između učesnika Cahoots-a. Soroban komunikacije su stoga zasnovane na Paynym-ima korisnika. Ako niste upoznati sa Paynym-ima, pozivam vas da pogledate ovaj članak za više detalja: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



Jednostavno rečeno, Paynym je jedinstveni identifikator povezan sa vašim Wallet koji omogućava razne funkcionalnosti, uključujući šifrovanu razmenu poruka. Paynym je predstavljen u obliku identifikatora i ilustracije koja predstavlja robota. Evo primera mog na Testnet: ![paynym samourai Wallet](assets/en/1.webp)


**Ukratko:**


- _Payjoin_ = Specifična struktura kolaborativnih transakcija;
- _Stowaway_ = PayJoin implementacija dostupna na Samourai i Sparrow Wallet;
- _Cahoots_ = Ime koje je Samourai dao svim njihovim vrstama kolaborativnih transakcija, uključujući PayJoin Stowaway;
- _Soroban_ = Šifrovani komunikacioni protokol uspostavljen na Toru, omogućavajući saradnju sa drugim korisnicima u kontekstu Cahoots transakcije;
- _Paynym_ = Jedinstveni identifikator Wallet koji omogućava komunikaciju sa drugim korisnikom na Sorobanu, kako bi se izvršila Cahoots transakcija.


[**-> Saznajte više o PayJoin transakcijama i njihovoj korisnosti**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Kako uspostaviti vezu između Paynyms?


Da biste izvršili udaljenu Cahoots transakciju, posebno PayJoin (Stowaway) putem Samourai, potrebno je "Pratiti" korisnika s kojim nameravate da sarađujete, koristeći njihov Paynym. U slučaju Stowaway, to znači pratiti osobu kojoj želite poslati bitkoine.


**Evo postupka za uspostavljanje ove veze:**


Da biste započeli, potrebno je da dobijete kod za plaćanje primaoca Paynym-a za PayJoin. U Samourai Wallet aplikaciji, primalac mora da dodirne ikonicu svog Paynym-a (mali robot) koja se nalazi u gornjem levom uglu ekrana, a zatim klikne na svoj Paynym nadimak, koji počinje sa `+...`. Na primer, moj je `+namelessmode0aF`. Ako vaš saradnik koristi Sparrow Wallet, pozivam vas da pogledate naš posvećeni vodič klikom ovde.


![connexion paynym samourai](assets/notext/2.webp)


Vaš saradnik će zatim biti preusmeren na svoju Paynym stranicu. Odatle, mogu podeliti svoje Paynym podatke sa vama ili podeliti svoj QR kod koji možete skenirati. Da bi to uradili, moraju kliknuti na malu ikonu "podeli" koja se nalazi u gornjem desnom uglu njihovog ekrana.

![partager paynym samourai](assets/en/1.webp)


Na vašoj strani, pokrenite vašu Samourai Wallet aplikaciju i pristupite meniju "PayNyms" na isti način. Ako prvi put koristite vaš Paynym, biće potrebno da dobijete identifikator.


![demander un paynym](assets/notext/3.webp)


Zatim kliknite na plavi "+" u donjem desnom uglu ekrana.

![ajouter paynym collaborateur](assets/notext/4.webp)

Zatim možete nalepiti kod plaćanja vašeg saradnika odabirom `COLLER LE CODE PAIEMENT`, ili otvoriti kameru da skenirate njihov QR kod pritiskom na `SCANNEZ LE CODE QR`.![paste paynym identifier](assets/notext/5.webp)


Kliknite na dugme `SUIVRE`.

![follow paynym](assets/notext/6.webp)

Potvrdite klikom na `YES`.

![confirm follow paynym](assets/notext/7.webp)

Softver će vam zatim ponuditi dugme `SE CONNECTER`. Nije potrebno kliknuti na ovo dugme za naš vodič. Ovaj korak je potreban samo ako planirate da izvršite plaćanja drugom Paynym-u kao deo BIP47, što nije povezano sa našim vodičem.

![connect paynym](assets/notext/8.webp)

Jednom kada primalaćev Paynym prati vaš Paynym, ponovite ovu operaciju u suprotnom smeru tako da vas primalac takođe prati. Zatim možete izvršiti PayJoin.


## Kako uraditi PayJoin na Samourai Wallet?


Ako ste završili ove preliminarne korake, konačno ste spremni da izvršite PayJoin transakciju! Da biste to uradili, pratite naš video tutorijal:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**Spoljni resursi:**


- https://docs.samourai.io/en/spend-tools#stowaway.