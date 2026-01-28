---
name: Cake Wallet
description: Uputstvo o Cake Wallet i Silent Payments
---

![cover](assets/cover.webp)


Ovaj vodič istražuje [**Cake Wallet**](https://cakewallet.com/): open-source, ne-kustodijalni, na privatnost fokusirani multi-valutni wallet dostupan za Android, iOS, macOS, Linux i Windows. Uronićemo u njegove Bitcoin-specifične funkcije privatnosti, proći kroz slanje/primanje Bitcoin putem **Silent Payments** (poboljšan on-chain protokol privatnosti) i pogledaćemo implementaciju PayJoin v2 za asinhrone transakcije.


## 🎉 Ključne karakteristike



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) poboljšavaju prethodne [BIP 47 kodove plaćanja](https://silentpayments.xyz/docs/comparing-proposals/bip47/) takođe nazvane "PayNyms" sa ponovo upotrebljivim stealth adresama. Kada pošiljalac koristi vašu Silent Payment adresu, njihov wallet generiše jedinstvenu jednokratnu adresu koristeći različite ključeve koji će biti kombinovani u jedinstvenu jednokratnu Taproot adresu. Zapisi na blockchain-u pokazuju nepovezane transakcije, sprečavajući povezivanje dolaznih uplata. Silent Payments nude niz prednosti, uključujući:
    - Ponovno upotrebljive adrese: Nema potrebe za generate novom adresom za svaku transakciju, što pruža bolje korisničko iskustvo i povećanu privatnost
    - Nema povećanja troškova: Tihi Plaćanja ne povećavaju veličinu ili trošak transakcija.
    - Poboljšana anonimnost: Spoljni posmatrači ne mogu povezati transakcije sa adresom za Tihu Uplatu.
    - Nije potrebna interakcija pošiljaoca i primaoca: Transakcije se mogu obaviti bez ikakve komunikacije između strana.
    - Jedinstvene adrese za svaku uplatu: Eliminisanje rizika od slučajnog ponovnog korišćenja adrese.
    - Nije potreban server: Tihi Plaćanja se mogu izvršiti bez potrebe za posvećenim serverom.
- PayJoin v2** ublažava analizu transakcijskih grafova spajanjem ulaza pošiljalaca i primalaca u jednu transakciju. Cake Wallet implementira dva ključna napretka:
    - Asinhrone Transakcije**: Pošiljalac i primalac više ne moraju biti istovremeno online da bi završili privatnu transakciju.
    - Komunikacija bez servera**: Nijedna strana ne mora da pokreće Payjoin server, čime se uklanja velika tehnička prepreka.
- Coin Control** omogućava ručni izbor UTXO tokom transakcija. Ovo sprečava slučajno povezivanje adresa prilikom trošenja više UTXO-a sa različitim poreklima.
- TOR** podrška, omogućavajući korisnicima da usmere svoj mrežni saobraćaj kroz Tor mrežu
- RBF** (Replace-By.Fee) vam omogućava da prilagodite naknadu nakon slanja transakcije.


## 1️⃣ Postavljanje vašeg Wallet


Cake Wallet nudi širok spektar podrške za platforme. Možete birati između `Android`, `iOS / macOS`, `Linux` i `Windows`. Da biste započeli, posetite https://docs.cakewallet.com/get-started/ i izaberite vaš operativni sistem.


![image](assets/en/01.webp)


Nakon instalacije, postavite `PIN` (4 ili 6 cifara). Zatim ćete videti:


1. `Kreiraj novi Wallet` (za nove korisnike)

2. `Restore Wallet` (za postojeće novčanike)


![image](assets/en/02.webp)


Na sledećem ekranu možete birati iz širokog spektra kriptovaluta. Izaberite `Bitcoin` i dodirnite `Next`, zatim unesite `Wallet name` kako biste identifikovali wallet. Dodirivanjem `Advanced Settings` pojavljuje se niz `Privacy Stettings`. Napravite sledeće izmene:



- Fiat API:** odaberite `Tor Only` (usmerava zahteve za cene kroz Tor)
- Zameni:** izaberi `Samo Tor` (anonimizuje saobraćaj razmene)


BIP-39 seed tip se generiše podrazumevano, sa opcijom da se promeni na Electrum seed tip. Putanje derivacije su sledeće:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Ako želite dodati dodatni sloj sigurnosti, možete postaviti `passphrase`. Glavna svrha passphrase je pružiti dodatnu zaštitu od fizičkih napada. Čak i ako napadač pronađe seed frazu, ne može pristupiti vašem wallet bez ispravnog passphrase. Drugim rečima, seed fraza sama predstavlja jedan wallet, dok seed fraza plus passphrase stvara potpuno drugačiji wallet bez veze s originalom. Ova funkcija takođe omogućava `tajne novčanike` zaštićene passphrase i pruža vam mogućnost uverljivog poricanja. U prisilnoj situaciji, mogli biste otkriti seed frazu dok veće imovine ostaju sigurne u passphrase-zaštićenom wallet.


Ako već pokrećete svoj čvor, uključite `Add New Custom Node` i unesite svoj `Node Address` da biste validirali transakcije i blokove unutar svoje infrastrukture. Kada završite, dodirnite `Continue` i `Next` da biste kreirali svoj wallet.


![image](assets/en/03.webp)


Na sledećem ekranu, dobijate odricanje odgovornosti:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Da biste naučili najbolje prakse za čuvanje vaše mnemoničke fraze, molimo vas da pogledate ovaj vodič:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Dodirnite `Razumem. Pokaži mi moj seed` i sačuvajte ove reči na sigurnom mestu! Zatim dodirnite `Verifikuj seed` i nakon verifikacije `Otvori Wallet`.


## 2️⃣ Postavke


Pre nego što zaronimo dublje, hajde da pogledamo `Home Screen` i `Settings`.


Na početnom ekranu možemo videti različite prikazane stavke:



- `Hamburger meni` nas vodi do `podešavanja`
- Dostupno stanje
- Kartica za Tihе Uplаtе za početak skeniranja transakcija poslatih na vašu adresu za Tihе Uplаtе
- Omogući Payjoin kao funkciju koja čuva privatnost i štedi na naknadama
- na dnu su Prečice do `Wallet Pregled`, `Primi`, `Zameni` između Bitcoin i drugih valuta, `Pošalji` i `Kupi`


![image](assets/en/11.webp)


Dodirivanje ikone `Hamburger meni` otvara meni sa podešavanjima. Hajde da pregledamo opcije.


![image](assets/en/05.webp)


### A - Povezivanje i sinhronizacija 🔗


Ovde možemo ponovo povezati wallet, upravljati čvorovima i povezati se sa sopstvenim čvorom (preporučeno). `Silent Payments Scanning` nam omogućava prilagođavanje skeniranja specificiranjem ili `Scan from block height` ili `Scan from date`.


![image](assets/en/06.webp)


Kao `Alpha` funkcija postoji i opcija da se `Omogući ugrađeni Tor` za usmeravanje saobraćaja kroz Tor mrežu.


### B - Postavke za tiha plaćanja 🔈


Možemo uključiti karticu Silent Payments na početnom ekranu da bismo prikazali ovu funkciju. Omogućavanje `Always scanning` omogućava wallet da kontinuirano prati blockchain za dolazne Silent Payments. Možemo odrediti parametre skeniranja kako bismo prilagodili proces skeniranja našim potrebama kao što je opisano gore.


![image](assets/en/07.webp)


### C - Sigurnost i bekap 🗝️


Da bismo osigurali naš wallet, možemo kreirati rezervnu kopiju prateći uputstva u aplikaciji. Ovo će osigurati da imamo sigurnu kopiju naših privatnih ključeva, omogućavajući nam da povratimo naš wallet ako bude izgubljen ili ukraden. Pored toga, možemo pregledati našu seed frazu i privatne ključeve, promeniti naš PIN, omogućiti biometrijsku autentifikaciju, potpisati / verifikovati i postaviti 2FA za dodatni sloj zaštite.


![image](assets/en/08.webp)


**Napomena**: Od septembra 2025. godine, biometrijska autentifikacija otiskom prsta na Android uređajima mora funkcionisati sa najmanje biometrijskom implementacijom Klase 2, za više detalja pogledajte [ovde](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Međutim, ovaj zahtev se može promeniti u budućnosti.


### D - Postavke privatnosti 🔒


Takođe možemo poboljšati sigurnost našeg wallet korišćenjem Tor-a za šifrovanje naše internet konekcije i zaštitu naše privatnosti prilikom pristupa spoljnim izvorima. Pored toga, možemo sprečiti pravljenje snimaka ekrana kako bismo zadržali poverljivost informacija našeg wallet, omogućiti automatski generisane adrese za kreiranje novih za svaku transakciju, i onemogućiti kupovinu/prodaju kako bismo sprečili neovlašćene transakcije. Nadalje, možemo `Omogućiti PayJoin`, što je još jedna funkcija privatnosti koju ćemo kasnije pregledati.


![image](assets/en/09.webp)


### E - Ostala podešavanja 🔧


Ostala podešavanja omogućavaju nam da upravljamo prioritetom naknade i postavimo podrazumevani nivo naknade za naše transakcije. Ovo nam omogućava da kontrolišemo naknade za transakcije povezane sa našim Silent Payments, uzimajući u obzir trenutnu iskorišćenost mreže.


![image](assets/en/10.webp)


## 3️⃣ Primanje ₿itcoina koristeći Silent Payments


Postoji nekoliko opcija i tipova adresa dostupnih za primanje Bitcoin. `Segwit (P2WPKH)` *(počinje sa bc1q....)* je podrazumevana opcija. Hajde da izaberemo `Silent Payments` u ovom primeru.


Da biste primili Tihu Uplatu, prvo dodirnite ikonu `Receive` u Cake Wallet. Zatim unesite iznos koji očekujete da primite. Da biste odredili tip adrese, ponovo dodirnite `Receive` na vrhu ekrana, a zatim izaberite `Silent Payments` iz opcija.


Na glavnom ekranu će biti prikazan vaš višekratni QR kod za Tiho Plaćanje i adresa. Kao što se očekuje, adresa je prilično dugačka:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Sada, koristite BIP-352 kompatibilan wallet (kao što je Plavi Wallet) da skenirate ovaj QR kod i pošaljete uplatu. Videćete da wallet izvodi jedinstvenu adresu destinacije iz vaše tihe adrese.


![image](assets/en/13.webp)


## 4️⃣ Slanje ₿itcoina koristeći Silent Payments


Pošto Blue Wallet može samo da `šalje` tihe uplate, koristićemo drugi BIP 352 kompatibilan wallet kao primaoca. Ovaj proces je identičan kao kod regularne Bitcoin transakcije.



- Dodirnite `Pošalji` na početnom ekranu
- ili lepljenjem naše višekratne `sp1qq...` adrese ili skeniranjem QR koda direktno unutar aplikacije.
- Odaberite koliko želite potrošiti sa svog dostupnog salda
- Dodirnite `Pošalji` na dnu ekrana da potvrdite transakciju


Jednom kada unesemo adresu `sp1qq...`, wallet automatski izvodi odgovarajuću `bc1p...` Taproot adresu (P2TR) u pozadini, koja će se koristiti za Tiho Plaćanje.


Opcionalno možemo napisati internu belešku za svaku transakciju, prilagoditi postavke naknade ili odabrati određene UTXO-e za transakciju koristeći funkciju `Coin Control`.


![image](assets/en/14.webp)


`Prevucite` udesno da potvrdite transakciju.


Kada pošaljete transakciju, bićete upitani da li želite da dodate ovaj kontakt u vaš adresar.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Hajde da pregledamo šta je PayJoin [o tome](https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 je funkcija očuvanja privatnosti i uštede na naknadama u Bitcoin koja omogućava pošiljaocu i primaocu transakcije da zajedno kreiraju jednu transakciju. Ova transakcija ima ulaze od *oba* pošiljaoca i primaoca, razbijajući najčešće tehnike nadzora protiv Bitcoin i omogućavajući bolje skaliranje i uštede na naknadama u nekim okolnostima._


Da biste saznali više o PayJoin, možete posetiti sledeći vodič.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Da bi koristili PayJoin, obe strane zahtevaju PayJoin kompatibilan wallet, a primalac treba da ima bar jedan novčić ili izlaz u svom wallet. Da biste započeli, molimo vas da pratite ove korake:


1. Dodirnite `Hamburger Menu` i dodirnite dugme `Privacy`.

2. Uključi opciju `Use Payjoin`

3.  Dodirnite `Receive` na početnom ekranu i biće vam prikazan PayJoin QR kod i dugme za kopiranje (kada je izabran Segwit)


![image](assets/en/16.webp)


## 6️⃣ Ostale funkcije


Postoji nekoliko drugih funkcija kao što su `Swaps` za više valuta, opcije `Buy and Sell` sa različitim povezivanjima sa prodavcima i specifični programi za Cake kao što je `Cake Pay`, koji vam omogućava kupovinu prepaid kartica ili poklon kartica.


![image](assets/en/17.webp)


## 🎯 Zaključak


Ovo je naša recenzija Cake Wallet, koji nudi praktičnu Bitcoin privatnost zahvaljujući funkcijama kao što su Silent Payments (BIP-352) i Payjoin v2.


Tihi Plaćanja zamenjuju jednokratne adrese sa višekratnim stealth adresama kako bi sprečili on-chain povezivanje dolaznih transakcija. Iako su problemi sa sinhronizacijom prethodnih verzija značajno poboljšani, postoje povećani zahtevi za računarstvom za skeniranje i detekciju Tihih Plaćanja, što zahteva više resursa i propusnog opsega.


Payjoin v2 ometa analizu lanca spajanjem ulaza pošiljaoca i primaoca u jedinstvene transakcije bez dodatnih naknada ili centralne koordinacije. Ovo narušava uobičajenu heuristiku vlasništva ulaza, što je značajna prednost jer znači da ne možete pretpostaviti da svi ulazi pripadaju pošiljaocu.


Za korisnike koji daju prioritet finansijskoj anonimnosti, Cake Wallet je održiva opcija. Uključuje protokole privatnosti direktno u svoju osnovnu funkcionalnost, čineći ih dostupnim bez tehničke složenosti. Kako nadzor nad javnim blokčejnovima raste, alati poput ovog pomažu u održavanju privatnosti transakcija tamo gde je to najvažnije. Šira primena ovih standarda unutar wallet okruženja bila bi dobrodošao razvoj.


## 📚 Resursi


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/