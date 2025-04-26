---
name: Bitcoin Čvorovi
description: Kako da pokrenem čvor sa alternativnim klijentom Bitcoin Knots?
---
![cover](assets/cover.webp)


Bitcoin Knots je alternativna implementacija Bitcoin protokola, izvedena iz Bitcoin Core. Dizajnirao i održava Luke Dashjr, nudi neke dodatne funkcije i prilagođavanja pravila iz Mempool, dok ostaje kompatibilan sa drugim čvorovima na mreži. Bitcoin Knots integriše Bitcoin Wallet, ali se takođe može koristiti kao jednostavan Bitcoin čvor uz drugi Wallet softver.


## Zašto koristiti Knots umesto Core?


Trenutno je Core većinska implementacija Bitcoin protokola na mreži. Bitcoin protokol je samo skup pravila. Potreban je softver da bi se ona primenila. Mašina koja pokreće softver koji implementira Bitcoin protokol naziva se čvor, i svi ti čvorovi zajedno čine Bitcoin mrežu.


Kroz istoriju Bitcoin, pojavili su se brojni klijenti proizašli iz početnog softvera koji je razvio Satoshi Nakamoto. Danas (mart 2025), Bitcoin Core čini ogromnu većinu, sa skoro 98% čvorova na Bitcoin mreži koji koriste ovog klijenta.


Međutim, alternativni softver je takođe dostupan. To nisu čvorovi povezani sa Altcoin kao što je Bitcoin Cash, već alternativni klijenti kompatibilni sa pravom Bitcoin mrežom. Od ovih, Bitcoin Knots je najpoznatiji. Trenutno predstavlja oko 1,4% mreže. Ostali alternativni klijenti su i dalje u velikoj manjini.


![Image](assets/fr/01.webp)


Postoje dva glavna razloga za korišćenje alternativnog klijenta kao što je Knots umesto Core:




- Tehnički**: Ovi klijenti često nude različite opcije u odnosu na Core, posebno u smislu upravljanja Mempool, određujući koje transakcije prihvata i emituje vaš čvor.
- Policy**: Neki ljudi preferiraju korišćenje alternativnih klijenata kao što je Knots iz netehničkih razloga, posebno da bi podržali alternativu Core-u i tako smanjili njegov monopol. Ako bi Core ikada bio kompromitovan, bilo bi korisno ne samo imati solidne, dobro održavane alternativne klijente, već i znati kako ih koristiti. Drugi koriste Knots iz protesta, jer su izgubili poverenje u Core-ove programere ili ne odobravaju upravljanje većinskim klijentom.


## Kako da instaliram Bitcoin Knots?


Idite na [zvaničnu Bitcoin Knots veb stranicu](https://bitcoinknots.org/#download) da preuzmete verziju za vaš operativni sistem. Ne zaboravite da preuzmete otisak prsta i potpise kako biste verifikovali softver. Ovi fajlovi su takođe dostupni [na Bitcoin Knots GitHub repozitorijumu](https://github.com/bitcoinknots/Bitcoin).


![Image](assets/fr/02.webp)


Pre nego što instalirate softver na svoj uređaj, preporučujemo da proverite njegovu autentičnost i integritet. Ako ne znate kako, pogledajte ovaj drugi vodič:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Kada je softver verifikovan, instalirajte ga prateći korake navedene u instalacionom panelu.


![Image](assets/fr/03.webp)


## Pokreni IBD


Prvi put kada pokrenete Bitcoin Knots, moći ćete da izaberete lokalni direktorijum gde će vaši podaci čvora (uključujući Blockchain, UTXO set i parametre) biti sačuvani.


![Image](assets/fr/04.webp)


Takođe možete odabrati da obrežete Blockchain podatke kako biste zadržali samo najnovije blokove. Ova opcija omogućava vašem čvoru da proveri svaki blok u celosti unutar postavljenog ograničenja skladištenja, čime se postepeno uklanjaju najstariji blokovi. Ako imate dovoljno prostora na disku (trenutno oko 650 GB, ali ovaj broj raste), ostavite ovu opciju neoznačenu. Ako vam je prostor na disku ograničen, aktivirajte obrezivanje i navedite maksimalni dozvoljeni kapacitet.


Imajte na umu: Ako je vaš čvor orezan i koristite ga za sinhronizaciju obnovljenog Wallet, nećete moći da povratite transakcije pre najstarijeg lokalno sačuvanog bloka.


![Image](assets/fr/05.webp)


Druga dostupna opcija je "*Assume Valid*". Ona ubrzava početnu sinhronizaciju preskakanjem verifikacije potpisa za transakcije uključene u blokove pre određenog bloka.


Cilj "*Pretpostavi Validno*" je da ubrza prvu sinhronizaciju čvora bez značajnog smanjenja sigurnosti, pretpostavljajući da su te transakcije već masovno validirane od strane mreže unapred. Jedini važan kompromis je da vaš čvor neće otkriti bilo kakve prethodne Bitcoin krađe, ali će i dalje garantovati tačnost ukupnog broja izdatih bitkoina. Vaš čvor će verifikovati sve potpise transakcija nakon specificiranog bloka. Ovaj pristup se zasniva na pretpostavci da je transakcija koja je dugo prihvaćena od strane mreže bez izazova najverovatnije validna.


Na primer, ovde, "*Assume Valid*" je postavljen na blok br. 855 000 `00000000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, objavljen 1. avgusta 2024. Tokom IBD, moj čvor će stoga započeti potpunu verifikaciju potpisa tek od ovog bloka.


![Image](assets/fr/06.webp)


Zatim kliknite na dugme "*OK*" da pokrenete *Initial Block Download*. Morate biti strpljivi tokom početne sinhronizacije čvora. Ako želite da nastavite sinhronizaciju kasnije, jednostavno zatvorite softver i isključite računar. Sinhronizacija će se nastaviti bez problema sledeći put kada otvorite program.


![Image](assets/fr/07.webp)


## Postavljanje vašeg Bitcoin Knot


Kliknite na karticu "*Settings*", zatim izaberite "*Options*".


![Image](assets/fr/08.webp)


U kartici "*Main*", pristupate glavnim parametrima čvora:




- "*Start...*" automatski pokreće čvor kada se vaš računar pokrene kako bi odmah započeo sinhronizaciju;
- "*Prune...*" podešava ograničenje skladišta ako ste odlučili da obrežete Blockchain ;
- "*Keš baze podataka...*" postavlja maksimalnu količinu RAM-a dozvoljenu vašem čvoru;
- Konačno, aktivirajte "*Omogući RPC server*" ako želite da povežete vaš Bitcoin Knots čvor sa drugim Wallet softverom, kao što su Sparrow Wallet ili Liana na primer.


![Image](assets/fr/09.webp)


Na kartici "*Wallet*" pronaći ćete postavke za integrisani Wallet koji možete kasnije kreirati na Knots. Preporučujem da aktivirate RBF i kontrolu novčića. Takođe možete definisati tip skripte koja će se koristiti.


![Image](assets/fr/10.webp)


Kartica "*Network*" sadrži mrežne parametre koje možete prilagoditi svojim specifičnim potrebama.


![Image](assets/fr/11.webp)


Kartica "*Mempool*" omogućava vam da konfigurišete *Memory Pool*, tj. upravljanje nepotvrđenim transakcijama koje su uskladištene u memoriji, i maksimalnu veličinu dodeljenu ovoj funkcionalnosti (300 MB po podrazumevanoj vrednosti).


![Image](assets/fr/12.webp)


Kartica "Filtriranje spama" je funkcija Bitcoin Knots. Ovde ćete pronaći niz podešavanja koja vam omogućavaju da izaberete koje transakcije ćete prihvatiti ili odbiti da emitujete. Glavni cilj je ograničiti određene marginalne upotrebe Bitcoin, posebno meta-protokole, kako bi se borili protiv ovih praksi dok izbegavate preopterećenje vašeg čvora. To je politički izbor, u zavisnosti od vaše lične vizije Bitcoin.


Takođe ćete pronaći klasične parametre kao što je definicija praga "*Dust*".


Međutim, ovi parametri utiču samo na pravila standardizacije. Vaš čvor će nastaviti da prihvata nepotvrđene transakcije samo kada su uključene u blok, kako bi ostao kompatibilan sa ostatkom Bitcoin mreže. Ova podešavanja samo menjaju način na koji vaš čvor obrađuje i distribuira nepotvrđene transakcije svojim vršnjacima. U praksi, pošto je Knots u manjini, pravila koja su podrazumevano uspostavljena na Bitcoin Core definišu standardizaciju na mreži.


![Image](assets/fr/13.webp)


Kartica "*Mining*" omogućava vam da konfigurišete moguće učešće vašeg čvora u Mining, ako želite da aktivirate ovu funkciju.


![Image](assets/fr/14.webp)


Konačno, kartica "*Display*" odnosi se na parametre koji se tiču Interface grafike, uključujući jezik softvera.


![Image](assets/fr/15.webp)


## Kreiranje Bitcoin Wallet


Kada je početna sinhronizacija završena, vaš Bitcoin Knots čvor je potpuno funkcionalan. Sada imate opciju povezivanja ovog čvora sa drugim Wallet softverom, ili korišćenja ugrađenog Hot Wallet direktno. Da biste to uradili, kliknite na dugme "*Create a new Wallet*".


![Image](assets/fr/16.webp)


Dajte svom Wallet ime. Takođe ga možete zaštititi sa passphrase BIP39 klikom na "*Encrypt Wallet*". Kada budete spremni, kliknite na dugme "*Create*".


![Image](assets/fr/17.webp)


passphrase BIP39 je opcionalna lozinka koju možete slobodno izabrati, pored vaše Mnemonic fraze, kako biste povećali sigurnost vašeg Wallet. Pre nego što konfigurišete ovu funkciju, snažno vam savetujemo da pročitate sledeći članak, koji detaljno objašnjava kako passphrase funkcioniše u teoriji, i kako izbeći greške koje bi mogle dovesti do trajnog gubitka vaših bitkoina:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Ako ste aktivirali opciju passphrase, izaberite robusnu i pažljivo je sačuvajte na jednom ili više sigurnih fizičkih medija.


![Image](assets/fr/18.webp)


Vaš Bitcoin Wallet je sada kreiran.


![Image](assets/fr/19.webp)


## Pravljenje rezervne kopije vašeg Bitcoin Wallet


Čak i pre nego što primite svoje prve bitkoine, važno je da napravite rezervnu kopiju vašeg Bitcoin Wallet kako biste mogli da povratite svoja sredstva u slučaju gubitka ili kvara računara. Da biste to uradili, kliknite na karticu "*File*" a zatim na "*Backup Wallet*".


![Image](assets/fr/20.webp)


Ova operacija generiše jednu datoteku koja se može koristiti za vraćanje svih vaših bitkoina. Zato budite veoma pažljivi i sačuvajte je na sigurnom spoljašnjem medijumu.


## Primite bitkoine


Da biste primili bitkoine direktno na vaš Knots Wallet, kliknite na dugme "*Receive*".


![Image](assets/fr/21.webp)


Dodelite "*Label*" svom Address kako biste lako identifikovali njegovu svrhu i olakšali buduću upotrebu *Coin Control*-a. Takođe možete unapred definisati tačan iznos koji će biti primljen na ovom Address, ili dodati poruku za platioca. Kada postavite parametre, kliknite na "*Request payment*".


![Image](assets/fr/22.webp)


Bitcoin Čvorovi zatim prikazuju prijemni Address, koji možete kopirati ili skenirati i poslati platiocu.


![Image](assets/fr/23.webp)


Jednom kada je transakcija emitovana, možete pratiti njen status direktno u meniju "*Transakcije*".


![Image](assets/fr/24.webp)


## Pošalji bitkoine


Sada kada imate bitkoine u vašem Knots Wallet, možete ih poslati. Da biste to uradili, kliknite na dugme "*Send*".


![Image](assets/fr/25.webp)


Kliknite na dugme "*Inputs...*" da biste odabrali tačan UTXO koji želite da potrošite na ovu transakciju.


![Image](assets/fr/26.webp)


Unesite primaoca Bitcoin Address.


![Image](assets/fr/27.webp)


Dodajte oznaku da biste zapamtili svrhu ove transakcije.


![Image](assets/fr/28.webp)


Unesite iznos koji želite poslati na ovaj Address.


![Image](assets/fr/29.webp)


Kliknite na dugme "*Choose...*" da biste izabrali odgovarajuću stopu naknade za vašu transakciju, na osnovu trenutnog statusa mreže.


![Image](assets/fr/30.webp)


Ako je sve po vašem zadovoljstvu, kliknite na dugme "*Pošalji*". Ako koristite passphrase, bićete zamoljeni da ga popunite u ovoj fazi.


![Image](assets/fr/31.webp)


Proverite parametre transakcije još jednom, a zatim, ako je sve ispravno, kliknite na dugme "*Pošalji*" ponovo da potpišete i distribuirate vašu transakciju.


![Image](assets/fr/32.webp)


Vaša transakcija koja čeka potvrdu sada se pojavljuje na kartici "*Transakcije*".


![Image](assets/fr/33.webp)


## Povezivanje vašeg čvora sa drugim programom


Bitcoin Knots' integrisani Interface za upravljanje vašim Bitcoin Wallet nije nužno najintuitivniji, a njegova funkcionalnost ostaje relativno ograničena. Međutim, možete povezati vaš Bitcoin Knots čvor sa specijalizovanim Wallet softverom za upravljanje kako biste lako pristupili Blockchain Bitcoin podacima i emitovali vaše transakcije.


Procedura će zavisiti od korišćenog softvera, ali postoje dva glavna scenarija: ili je Bitcoin Knots instaliran na istom računaru kao vaš Wallet softver, ili radi na zasebnoj mašini.


### Sa lokalnim Bitcoin Čvorovima :


Ako je Bitcoin Knots instaliran na vašem računaru, pronađite datoteku `Bitcoin.conf` među softverskim datotekama. Ako ova datoteka ne postoji, možete je kreirati. Otvorite je pomoću uređivača teksta i umetnite sledeći red:


```ini
server=1
```


Zatim sačuvaj svoje izmene.


Takođe možete to uraditi putem Bitcoin-QT-ove Interface grafike tako što ćete otići na "*Settings*" > "*Options...*" i omogućiti opciju "*Enable RPC server*".


Ne zaboravite da restartujete softver nakon što napravite ove promene.


![Image](assets/fr/34.webp)


Zatim idite na svoj Wallet softver za upravljanje (npr. Sparrow Wallet ili Liana) i unesite putanju do vaše cookie datoteke, koja se obično nalazi u istom folderu kao i `Bitcoin.conf`, u zavisnosti od vašeg operativnog sistema:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


Ostavite ostale parametre kao podrazumevane, URL `127.0.0.1` i port `8332`, zatim kliknite na "*Test Connection*".


![Image](assets/fr/36.webp)


### Sa daljinskim Bitcoin Čvorovi :


Ako je Bitcoin Knots instaliran na drugoj mašini povezanoj na istu mrežu, prvo pronađite datoteku `Bitcoin.conf` među softverskim datotekama. Ako ova datoteka još ne postoji, možete je kreirati. Otvorite ovu datoteku pomoću uređivača teksta i dodajte sledeći red:


```ini
server=1
```


Nakon uređivanja datoteke, obavezno je sačuvajte u odgovarajućem folderu za vaš operativni sistem:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

Ova operacija se takođe može izvesti putem Bitcoin-QT-ove Interface grafike. Idite na meni "*Settings*", zatim "*Options...*", i aktivirajte opciju "*Enable RPC server*" označavanjem odgovarajućeg polja. Ako `Bitcoin.conf` datoteka ne postoji, možete je kreirati direktno iz ovog Interface klikom na "*Open Configuration File*".


![Image](assets/fr/37.webp)


Pronađite IP Address mašine koja hostuje Bitcoin Knots na vašoj lokalnoj mreži. Da biste to uradili, možete koristiti alat kao što je [Angry IP Scanner](https://angryip.org/). Pretpostavimo, radi argumentacije, da je IP Address vašeg čvora `192.168.1.18`.


U datoteku `Bitcoin.conf` dodajte sledeće linije, postavljajući `rpcbind=192.168.1.18` da odgovara IP adresi Address vašeg čvora.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


Takođe dodajte korisničko ime i lozinku za daljinske veze u `Bitcoin.conf` datoteku. Obavezno zamenite `loic` sa vašim korisničkim imenom i `my_password` sa jakom lozinkom:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


Nakon izmene i čuvanja datoteke, ponovo pokrenite Bitcoin Knots.


Sada možete otići na vaš Wallet softver za upravljanje (npr. Sparrow Wallet ili Liana). Na Sparrow-u, idite na karticu "*User / Pass*". Unesite korisničko ime i lozinku koje ste konfigurisali u `Bitcoin.conf` fajlu. Ostavite ostale parametre kao podrazumevane, tj. URL `127.0.0.1` i port `8332`. Zatim kliknite na "*Test Connection*".


![Image](assets/fr/40.webp)


Veza je uspostavljena.


Sada znate sve o alternativnoj implementaciji Bitcoin Knots.


Ako ste našli ovaj vodič korisnim, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno ga podelite na vašim društvenim mrežama. Hvala vam puno!


Takođe preporučujem ovaj drugi vodič u kojem objašnjavam kako da postavite svoj sopstveni Lightning čvor:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a