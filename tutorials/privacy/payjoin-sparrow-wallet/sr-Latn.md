---
name: PayJoin - Sparrow novčanik
description: Kako napraviti PayJoin transakciju sa Sparrow novčanikom?
---

![tutorial cover image sparrow payjoin](assets/cover.webp)


_**UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, Payjoins Stowaway na Samourai novčaniku sada funkcioniše samo ručnom razmenom PSBT između uključenih strana, pod uslovom da su oba korisnika povezana na svoj Dojo. Što se tiče Sparrow-a, Payjoins putem BIP78 i dalje funkcioniše. Međutim, ovi alati mogu biti ponovo pokrenuti u narednim nedeljama. U međuvremenu, uvek možete pročitati ovaj članak da biste razumeli teorijsko funkcionisanje payjoins-a._


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Naterajte špijune Blockchain-a da preispitaju sve što misle da znaju.*

PayJoin je specifična struktura Bitcoin transakcije koja poboljšava privatnost korisnika tokom trošenja saradnjom sa primaocem plaćanja. Postoji nekoliko implementacija koje olakšavaju postavljanje i automatizaciju PayJoin-a. Među tim implementacijama, najpoznatija je Stowaway koju je razvio tim Samourai novčanika. Ovaj vodič ima za cilj da vas provede kroz proces pravljenja Stowaway PayJoin transakcije koristeći Sparrow softverski novčanik.


## Kako funkcioniše Stowaway?


Kao što je ranije pomenuto, Samourai novčanik nudi alat PayJoin pod nazivom "Stowaway." Dostupan je putem softverskog novčanika Sparrow na PC-ju ili aplikacije Samourai novčanik na Androidu. Da bi se izvršio PayJoin, primalac, koji takođe deluje kao saradnik, mora koristiti softver kompatibilan sa Stowaway, naime Sparrow ili Samourai novčanik. Ova dva softvera su interoperabilna, omogućavajući Stowaway transakcije između Sparrow novčanika i Samourai novčanika, i obrnuto.


Stowaway se oslanja na kategoriju transakcija koju Samourai naziva "Cahoots." Cahoot je u suštini kolaborativna (saradnička) transakcija između više korisnika, koja zahteva razmenu informacija van lanca (off-chain). Trenutno, Samourai nudi dva Cahoots alata: Stowaway (Payjoins) i StonewallX2 (koji ćemo istražiti u budućem članku).


Transakcije u dosluhu uključuju razmenu delimično potpisanih transakcija između korisnika. Ovaj proces može biti dugotrajan i zamoran, posebno kada se obavlja na daljinu. Međutim, i dalje se može obaviti ručno sa drugim korisnikom, što može biti zgodno ako su saradnici fizički blizu. U praksi, ovo uključuje ručnu razmenu pet QR kodova koji se sukcesivno skeniraju.


Kada se radi na daljinu, ovaj proces postaje previše složen. Da bi se rešio ovaj problem, Samourai je razvio šifrovani komunikacioni protokol zasnovan na Tor-u, nazvan "Soroban." Sa Soroban-om, neophodne razmene za PayJoin su automatizovane iza korisnički prijatnog interfejsa. Ovo je druga metoda koju ćemo istražiti u ovom članku.


Ove šifrovane razmene zahtevaju uspostavljanje veze i autentifikaciju između Cahoots učesnika. Soroban koristi Paynyme korisnika kao osnovu za uspostavljanje komunikacije. Ako niste upoznati sa Paynyms, pozivam vas da pogledate ovaj članak za više detalja: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

Jednostavno rečeno, Paynym je jedinstveni identifikator povezan sa vašim novčanikom koji omogućava razne funkcionalnosti, uključujući šifrovanu razmenu poruka. Paynym je predstavljen u obliku identifikatora i ilustracije koja predstavlja robota. Evo primera mog na Testnet-u: ![Paynym Sparrow](assets/en/1.webp)


**Ukratko:**



- _Payjoin_ = Specifična struktura kolaborativne transakcije;
- _Stowaway_ = PayJoin implementacija dostupna na Samourai i Sparrow novčanicima;
- _Cahoots_ = Ime koje je Samourai dao svim njihovim vrstama kolaborativnih transakcija, uključujući PayJoin Stowaway;
- _Soroban_ = Šifrovani komunikacioni protokol uspostavljen na Toru, omogućavajući saradnju sa drugim korisnicima u kontekstu Cahoots transakcije.
- _Paynym_ = Jedinstveni identifikator novčanika koji omogućava komunikaciju sa drugim korisnikom putem Soroban mreže, radi realizacije Cahoots transakcije.


[**-> Saznajte više o PayJoin transakcijama i njihovoj korisnosti**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Kako uspostaviti vezu između Paynyms?


Da biste izvršili udaljenu Cahoots transakciju, posebno PayJoin (Stowaway) koristeći Samourai ili Sparrow, potrebno je "Pratiti", eng. "Follow",  korisnika s kojim nameravate da sarađujete, koristeći njihov Paynym. U slučaju Stowaway-a, to znači pratiti osobu kojoj želite poslati bitkoine.


**Evo postupka za uspostavljanje ove veze:**


Prvo, treba da pribavite Paynym identifikator primaoca. Ovo se može uraditi korišćenjem njihovog nadimka ili koda za plaćanje. Da biste to uradili, iz primaočevog Sparrow novčanika, izaberite karticu `Tools`, zatim kliknite na `Show PayNym`.

![Show Paynym](assets/notext/2.webp)

![Paynym Sparrow](assets/en/1.webp)

Na vašoj strani, otvorite vaš Sparrow novčanik i pristupite istom meniju `Show PayNym`. Ako koristite vaš PayNym prvi put, biće potrebno da dobijete identifikator klikom na `Retrieve PayNym`.

![Retrieve paynym](assets/notext/3.webp)

Dalje, unesite Paynym identifikator vašeg saradnika (bilo njihov nadimak `+...` ili njihov platni kod `PM...`) u polje `Find Contact`, zatim kliknite na dugme `Add Contact`.

![add contact](assets/notext/4.webp)

Softver će vam zatim ponuditi dugme `Link Contact`. Nije potrebno kliknuti na ovo dugme za naš vodič. Ovaj korak je potreban samo ako planirate da izvršite uplate Paynym-u navedenom u kontekstu BIP47, što nije povezano sa našim vodičem.


Kada primalčev Paynym počne da prati vaš Paynym, ponovite isti postupak u suprotnom smeru, kako bi i primalac zapratio vas. Nakon toga možete izvršiti Payjoin.


## Kako izvesti PayJoin na Sparrow novčaniku?


Ako ste završili ovih nekoliko preliminarnih koraka, konačno ste spremni da izvršite PayJoin transakciju! Da biste to uradili, pratite naš video tutorijal:

![Payjoin tutorial - Sparrow novčanik](https://youtu.be/ZQxKod3e0Mg)


**Spoljni resursi:**



- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.
