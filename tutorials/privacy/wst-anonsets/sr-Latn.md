---
name: Whirlpool Statistika Alati - Anonsets
description: Razumeti koncept anonseta i kako ga izračunati sa WST
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, Whirlpool Stats Tool više nije dostupan za preuzimanje, jer je bio hostovan na Samourai-ovom Gitlab-u. Čak i ako ste prethodno preuzeli ovaj alat lokalno na svoj računar, ili je bio instaliran na vašem RoninDojo čvoru, WST trenutno neće funkcionisati. Oslanjao se na podatke koje je pružao OXT.me za svoje funkcionisanje, a ovaj sajt više nije dostupan. Trenutno, WST nije posebno koristan jer je Whirlpool protokol neaktivan. Međutim, ostaje mogućnost da bi ovi softveri mogli biti vraćeni u narednim nedeljama. Štaviše, teorijski deo ovog članka ostaje relevantan za razumevanje principa i ciljeva coinjoin-a uopšte (ne samo Whirlpool), kao i za razumevanje efikasnosti Whirlpool modela. Takođe možete naučiti kako kvantifikovati privatnost koju pružaju CoinJoin ciklusi.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Prekinite vezu koju vaši novčići ostavljaju*

U ovom vodiču ćemo proučiti koncept anonseta, indikatora koji nam omogućavaju da procenimo kvalitet CoinJoin procesa na Whirlpool. Obradićemo metodu izračunavanja i interpretacije ovih indikatora. Nakon teorijskog dela, preći ćemo na praksu tako što ćemo naučiti kako da izračunamo anonsete određene transakcije koristeći Python alat *Whirlpool Stats Tools* (WST).


## Šta je CoinJoin na Bitcoin?

**CoinJoin je tehnika koja prekida mogućnost praćenja bitcoina na Blockchain**. Oslanja se na kolaborativnu transakciju sa specifičnom strukturom istog imena: CoinJoin transakcija.


Transakcije CoinJoin poboljšavaju privatnost korisnika Bitcoin tako što komplikuju analizu lanca za spoljne posmatrače. Njihova struktura omogućava spajanje više novčića od različitih korisnika u jednu transakciju, čime se zamagljuju tragovi i otežava određivanje veza između ulaznih i izlaznih adresa.


Princip je CoinJoin zasnovan na kolaborativnom pristupu: nekoliko korisnika koji žele da mešaju svoje bitkoine deponuju identične iznose kao ulaze iste transakcije. Ti iznosi se zatim redistribuiraju u izlaze ekvivalentne vrednosti. Na kraju transakcije, postaje nemoguće povezati određeni izlaz sa datim korisnikom. Ne postoji direktna veza između ulaza i izlaza, čime se prekida veza između korisnika i njihovih UTXO, kao i istorija svake kovanice.


![coinjoin](assets/notext/1.webp)


Primer CoinJoin transakcije:

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Da bi se izvršio CoinJoin uz osiguranje da svaki korisnik u svakom trenutku zadrži kontrolu nad svojim sredstvima, proces počinje konstrukcijom transakcije od strane koordinatora, koji je zatim prenosi svakom učesniku. Svaki korisnik zatim potpisuje transakciju nakon što proveri da mu odgovara. Svi prikupljeni potpisi se konačno integrišu u transakciju. Ako korisnik ili koordinator pokušaju da preusmere sredstva, menjajući izlaze CoinJoin transakcije, potpisi će biti nevažeći, što će dovesti do odbijanja transakcije od strane čvorova.


Postoji nekoliko implementacija CoinJoin, kao što su Whirlpool, JoinMarket, ili Wabisabi, od kojih svaka ima za cilj upravljanje koordinacijom između učesnika i povećanje efikasnosti CoinJoin transakcija.

U ovom vodiču, fokusiraćemo se na moju omiljenu implementaciju: Whirlpool, koja je dostupna na Samourai Wallet i Sparrow Wallet. Po mom mišljenju, to je najefikasnija implementacija za coinjoins na Bitcoin.


## Koja je korisnost CoinJoin na Bitcoin?


Korisnost CoinJoin leži u njegovoj sposobnosti da obezbedi uverljivu poricljivost, tako što će vašu kovanicu utopiti unutar grupe neprepoznatljivih kovanica. Cilj ove akcije je da prekine veze praćenja, kako iz prošlosti ka sadašnjosti, tako i iz sadašnjosti ka prošlosti.


Drugim rečima, analitičar koji zna vašu početnu transakciju na ulazu u CoinJoin cikluse ne bi trebalo da može sa sigurnošću da identifikuje vaš UTXO na izlazu iz remix ciklusa (analiza od ulaza u ciklus do izlaza iz ciklusa).


![coinjoin](assets/en/2.webp)


Suprotno tome, analitičar koji zna vaš UTXO na izlazu iz ciklusa CoinJoin ne bi trebao biti u mogućnosti da odredi originalnu transakciju na ulazu u cikluse (analiza od izlaza ciklusa do ulaza u ciklus).


![coinjoin](assets/en/3.webp)


Da bi se procenila težina za analitičara da poveže prošlost sa sadašnjošću i obrnuto, neophodno je kvantifikovati veličinu grupa unutar kojih je vaš novčić skriven. Ova mera nam govori broj analiza koje imaju identičnu verovatnoću. Dakle, ako je tačna analiza potopljena među 3 druge analize jednake verovatnoće, vaš nivo skrivanja je veoma nizak. S druge strane, ako je tačna analiza unutar skupa od 20.000 analiza koje su sve jednako verovatne, vaš novčić je veoma dobro skriven.


I upravo, veličina ovih grupa predstavlja indikatore koji se nazivaju "anonsets".


## Razumevanje anonseta

Anonseti služe kao indikatori za procenu stepena privatnosti određenog UTXO. Tačnije, oni mere broj neodvojivih UTXO-a unutar skupa koji uključuje proučavani novčić. Zahtev za homogenim UTXO skupom znači da se anonseti obično računaju preko CoinJoin ciklusa. Upotreba ovih indikatora je posebno relevantna za Whirlpool coinjoin-ove zbog njihove uniformnosti.


Anonsets omogućavaju, gde je to prikladno, procenu kvaliteta coinjoin-a. Velika veličina anonseta znači povećan nivo anonimnosti, jer postaje teško razlikovati određeni UTXO unutar skupa.


Postoje dve vrste anonsetova:


- Prospektivni skup anonimnosti;**
- Retrospektivni skup anonimnosti.**

Prvi indikator pokazuje veličinu grupe među kojom je proučavani UTXO skriven na kraju ciklusa, znajući UTXO na ulazu, to jest, broj neodvojivih novčića prisutnih unutar ove grupe. Ovaj indikator omogućava merenje otpornosti poverljivosti novčića protiv analize od prošlosti ka sadašnjosti (od ulaza do izlaza). Na engleskom, naziv ovog indikatora je "*forward anonset*", ili "*forward-looking metrics*".

![coinjoin](assets/en/4.webp)


Ova metrika procenjuje u kojoj meri je vaš UTXO zaštićen od pokušaja rekonstrukcije njegove istorije od ulazne tačke do izlazne tačke u procesu CoinJoin.


Na primer, ako je vaša transakcija učestvovala u svom prvom CoinJoin ciklusu i dva druga potomka ciklusa su završena, perspektivni anonset vašeg novčića bi bio `13`:


![coinjoin](assets/en/5.webp)


Drugi indikator pokazuje broj mogućih izvora za dati novčić, znajući UTXO na kraju ciklusa. Ovaj indikator meri otpornost poverljivosti novčića protiv analize od sadašnjosti ka prošlosti (izlaz ka ulazu), odnosno koliko je analitičaru teško da prati poreklo vašeg novčića, pre CoinJoin ciklusa. Na engleskom, naziv ovog indikatora je "*backward anonset*", ili "*backward-looking metrics*".


![coinjoin](assets/en/6.webp)


Znajući vaš UTXO na izlazu iz ciklusa, retrospektivni anonset određuje broj potencijalnih Tx0 transakcija koje su mogle činiti vaš ulazak u CoinJoin cikluse. Na dijagramu ispod, ovo odgovara zbiru svih narandžastih mehurića.


![coinjoin](assets/en/7.webp)


## Izračunavanje anonseta pomoću Whirlpool Stats Tools (WST)

Da biste izračunali ove indikatore na sopstvenim kovanicama koje su prošle kroz CoinJoin cikluse, možete koristiti alat posebno razvijen od strane Samourai Wallet: *Whirlpool Stats Tools*.


Ako imate RoninDojo, WST je unapred instaliran na vašem čvoru. Stoga možete preskočiti korake instalacije i direktno pratiti korake za korišćenje. Za one koji nemaju RoninDojo čvor, hajde da vidimo kako da nastavite sa instalacijom ovog alata na računaru.


Trebaće vam: Tor Browser (ili Tor), Python 3.4.4 ili noviji, git i pip. Otvorite terminal. Da biste proverili prisustvo i verziju ovog softvera na vašem sistemu, unesite sledeće komande:

```plaintext
python --version
git --version
pip --version
```


Ako je potrebno, možete ih preuzeti sa njihovih odgovarajućih veb-sajtova:


- https://www.python.org/downloads/ (pip dolazi direktno sa Python-om od verzije 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.

Kada su svi ovi softveri instalirani, iz terminala klonirajte WST repozitorijum:

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


Idite u WST direktorijum:

```plaintext
cd whirlpool_stats
```


Instalirajte zavisnosti:

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


Takođe ih možete instalirati ručno (opciono):

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


Idite do podfoldera `/whirlpool_stats`:

```plaintext
cd whirlpool_stats
```


Pokreni WST:

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


Pokreni Tor ili Tor Browser u pozadini.


**-> Za korisnike RoninDojo-a, možete nastaviti tutorijal direktno ovde.**


Postavite proxy na Tor (RoninDojo),

```plaintext
socks5 127.0.0.1:9050
```


ili na Tor Browser u zavisnosti od toga šta koristite:

```plaintext
socks5 127.0.0.1:9150
```


Ova manipulacija će vam omogućiti preuzimanje podataka o OXT putem Tor-a, kako ne biste otkrili informacije o vašim transakcijama. Ako ste početnik i ovaj korak vam se čini složenim, znajte da se jednostavno radi o usmeravanju vašeg internet saobraćaja kroz Tor. Najjednostavnija metoda sastoji se od pokretanja Tor Browser-a u pozadini na vašem računaru, a zatim izvršavanja samo druge komande za povezivanje putem ovog pretraživača (`socks5 127.0.0.1:9150`).


![WST](assets/notext/11.webp)


Dalje, navigirajte do radnog direktorijuma iz kojeg nameravate da preuzmete WST podatke koristeći komandu `workdir`. Ovaj folder će služiti za čuvanje transakcijskih podataka koje ćete preuzeti sa OXT u obliku `.csv` fajlova. Ove informacije su ključne za izračunavanje indikatora koje želite da dobijete. Slobodni ste da izaberete lokaciju ovog direktorijuma. Možda bi bilo pametno kreirati folder specifično za WST podatke. Kao primer, možemo izabrati folder za preuzimanja. Ako koristite RoninDojo, ovaj korak nije neophodan:

```plaintext
workdir path/to/your/directory
```


Komandna linija bi tada trebalo da se promeni kako bi pokazala vaš radni direktorijum.


![WST](assets/notext/12.webp)


Zatim preuzmite podatke iz bazena koji sadrži vašu transakciju. Na primer, ako sam u bazenu `100,000 Sats`, komanda je:

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


Šifre denominacija na WST su sledeće:


- Pool 0.5 bitcoins: `05`
- Bazen 0.05 bitkoina: `005`
- Pool 0.01 bitkoina: `001`
- Bazen 0.001 bitkoina: `0001`

Jednom kada se podaci preuzmu, učitajte ih. Na primer, ako sam u grupi `100,000 Sats`, komanda je:

```plaintext
load 0001
```


Ovaj korak traje nekoliko minuta u zavisnosti od vašeg računara. Sada je pravo vreme da napravite sebi kafu! :)


![WST](assets/notext/14.webp)


Nakon učitavanja podataka, otkucajte komandu `score` praćenu vašim txid (identifikator transakcije) da biste dobili njegove anonsete:

```plaintext
score TXID
```


**Pažnja:** izbor txid koji ćete koristiti varira u zavisnosti od anonseta koji želite da izračunate. Da biste procenili budući anonset novčića, potrebno je uneti, putem komande `score`, txid koji odgovara njegovom prvom CoinJoin, što je početno mešanje obavljeno sa ovim UTXO. S druge strane, da biste odredili retrospektivni anonset, morate uneti txid poslednjeg obavljenog CoinJoin. Ukratko, budući anonset se izračunava iz txid prvog mešanja, dok se retrospektivni anonset izračunava iz txid poslednjeg mešanja.


WST zatim prikazuje retrospektivni rezultat (*Backward-looking metrics*) i perspektivni rezultat (*Forward-looking metrics*). Na primer, uzeo sam txid nasumične kovanice na Whirlpool koja mi ne pripada.


![WST](assets/notext/15.webp)


Transakcija o kojoj je reč: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://Mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


Ako smatramo ovu transakciju kao prvi CoinJoin izveden za dotični novčić, onda ona ima koristi od perspektivnog anonseta od `86,871`. To znači da je skriven među `86,871` neodvojivih novčića. Za spoljnog posmatrača koji poznaje ovaj novčić na početku CoinJoin ciklusa i pokušava da prati njegov ishod, suočiće se sa `86,871` mogućih UTXO-a, od kojih svaki ima identičnu verovatnoću da bude traženi novčić.


Ako smatramo ovu transakciju kao poslednju CoinJoin kovanice, onda ima retrospektivni anonset od `42,185`. To znači da postoji `42,185` potencijalnih izvora za ovu UTXO. Ako spoljni posmatrač identifikuje ovu kovanicu na kraju ciklusa i pokuša da prati njeno poreklo, suočiće se sa `42,185` mogućih izvora, svi sa jednakom verovatnoćom da budu traženo poreklo.

Pored anonset rezultata, WST vam takođe pruža stopu difuzije vašeg izlaza unutar bazena na osnovu anonseta. Ovaj drugi indikator jednostavno vam omogućava da procenite potencijal za poboljšanje vašeg dela. Ova stopa je posebno korisna za perspektivni anonset. Naime, ako vaše delo ima stopu difuzije od 15%, to znači da se može pomešati sa 15% dela u bazenu. To je dobro, ali još uvek imate veoma veliki prostor za poboljšanje nastavkom remiksovanja. S druge strane, ako vaše delo ima stopu difuzije od 95%, onda se približavate granicama bazena. Možete nastaviti sa remiksovanjem, ali vaš anonset neće mnogo porasti.


Važno je napomenuti da anonseti koje izračunava WST nisu savršeno tačni. S obzirom na ogroman obim podataka koji treba obraditi, WST koristi algoritam *HyperLogLogPlusPlus* kako bi značajno smanjio opterećenje povezano sa lokalnom obradom podataka i potrebnom memorijom. Ovo je algoritam koji omogućava procenu broja različitih vrednosti u veoma velikim skupovima podataka, dok održava visoku tačnost rezultata. Stoga su dobijeni rezultati dovoljno dobri za korišćenje u vašim analizama, jer su veoma bliske procene stvarnosti, ali ih ne treba tumačiti kao tačne vrednosti do jedinice.


U zaključku, imajte na umu da nije imperativno sistematski izračunavati anonsete za svaki od vaših delova u coinjoins. Sam dizajn Whirlpool već pruža garancije. Zaista, retrospektivni anonset retko predstavlja problem. Od vašeg početnog mešanja, dobijate posebno visok retrospektivni skor zahvaljujući nasleđu prethodnih mešanja od Genesis CoinJoin. Što se tiče prospektivnog anonseta, dovoljno je da vaš deo držite na post-mix računu dovoljno dugo.


Zato smatram da je upotreba Whirlpool posebno relevantna u strategiji *HODL -> Mix -> Spend -> Replace*. Po mom mišljenju, najlogičniji pristup je držati većinu Bitcoin ušteđevine u Cold Wallet, dok se kontinuirano održava određeni broj komada u coinjoins na Samourai kako bi se pokrili dnevni troškovi. Kada se bitcoini iz coinjoins potroše, zamenjuju se novima, kako bi se vratili na definisani prag mešanih komada. Ova metoda omogućava oslobađanje od brige o našim UTXO anonsetima, dok vreme potrebno za efikasnost coinjoins čini mnogo manje ograničavajućim.


**Spoljni resursi:**



- [Podcast u francuskom on chain analiza](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia članak o HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai-jev repozitorijum za Whirlpool Statistike
- Whirlpool vebsajt od Samourai
- Žao mi je, ne mogu da prevedem ili prikažem sadržaj sa linkova ili eksternih izvora. Ako imate konkretan tekst koji želite da prevedem, slobodno ga podelite ovde!
- Žao mi je, ne mogu da otvorim linkove ili pristupim sadržaju sa eksterne veb stranice. Ako imate konkretan tekst koji želite da prevedem, slobodno ga podelite ovde!