---
name: Bitchat
description: Decentralizovano, internet-free slanje poruka za slobodnu komunikaciju
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Ovaj video tutorijal od BTC Sessions vodi vas kroz proces postavljanja i korišćenja Bitchat-a!*


Bitchat je nastao iz napora brzog prototipiranja gde je [@jack](https://primal.net/jack) razvio početni koncept tokom vikend kodiranja. [@calle](https://primal.net/calle) se pridružio projektu ubrzo nakon toga kako bi zajedno razvijali Android implementaciju. Jack trenutno vodi razvoj iOS verzije, dok calle nadgleda Android verziju uz podršku mnogih drugih saradnika.


## Uvod: Razgovarajte slobodno, bez mreže


Zamislite slanje poruka kada internet ne radi, tokom prirodne katastrofe ili na mestima gde je komunikacija ograničena. Bitchat to omogućava. To je decentralizovana, peer-to-peer aplikacija za razmenu poruka koja preskače centralne servere, omogućavajući uređajima da direktno komuniciraju jedni s drugima, potpuno offline koristeći Bluetooth i mesh umrežavanje. Dizajniran sa privatnošću i otpornošću na umu, Bitchat je idealan za korišćenje u oblastima gde je tradicionalna povezanost nepouzdana ili nedostupna—kao što su scenariji katastrofa, udaljene lokacije ili za one koji žele da izbegnu nadzor. U svojoj srži, Bitchat koristi kriptografiju kako bi osigurao da je svaka poruka end-to-end enkriptovana, verifikovana i otporna na manipulaciju.


U ovom vodiču pokazaćemo kako Bitchat funkcioniše i kako ga možete koristiti za zaista privatnu, offline-spremnu komunikaciju.


## 🚀 Ključne funkcije


Bitchat omogućava slanje poruka van mreže putem ovih [funkcija](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Kompatibilno na više platformi**: Potpuna protokolska kompatibilnost između iOS-a i Androida.
- Decentralizovana Mesh Mreža**: Automatsko otkrivanje vršnjaka i višestruko prosleđivanje poruka preko Bluetooth Low Energy (BLE)
- End-to-End Enkripcija**: X25519 razmena ključeva + AES-256-GCM za privatne poruke
- Razgovori zasnovani na kanalima**: Grupno dopisivanje po temama sa opcionalnom zaštitom lozinkom
- Store & Forward**: Poruke keširane za vanmrežne čvorove i isporučene kada se ponovo povežu
- Privatnost na prvom mestu**: Nema naloga, nema brojeva telefona, nema trajnih identifikatora
- IRC-Stil Komande: Poznati interfejs sa komandama `/join, /msg, /who`.
- Zadržavanje Poruka**: Opcionalno čuvanje poruka na nivou kanala koje kontrolišu vlasnici kanala
- Hitna Brisanja**: Trostruko dodirnite logo da odmah obrišete sve podatke
- Moderni Android UI**: Jetpack Compose sa Material Design 3
- Tamne/Svetle Teme**: Estetika inspirisana terminalom koja odgovara iOS verziji
- Optimizacija Baterije**: Adaptivno skeniranje i upravljanje energijom


## 1️⃣ Kako Bitchat Radi - jednostavno


Bitchat vam omogućava da šaljete poruke direktno na obližnje telefone putem Bluetooth-a (`BLE` kako sledi), bez potrebe za internetom ili mobilnim signalom. Kada započnete razgovor, telefoni obavljaju sigurno rukovanje kako bi kreirali jedinstveni, privremeni enkripcioni ključ za vašu konverzaciju. Svaka poruka je zaštićena end-to-end enkripcijom, a za svaku se koristi novi ključ kako bi se osiguralo da prethodne poruke ostanu bezbedne čak i ako vaš telefon kasnije bude kompromitovan. Na kraju, aplikacija deli poruke na male delove i meša ih sa slučajnim lažnim podacima kako bi sakrila vašu aktivnost slanja poruka. Za direktne razgovore uređaj-na-uređaj, radi samo u dometu do ~100m. To je kao da razmenjujete šifrovane poruke u prepunoj sobi—uređaji šapuću direktno jedan drugom, uništavajući ključeve nakon svake poruke.


Bitchat takođe omogućava da se pridružite čet sobama zasnovanim na lokaciji koristeći Nostr protokol i `#geohashes`. Geohash je kratak kod, kao `#u33d`, koji predstavlja određeno geografsko područje, od jedne četvrti, do čitavog grada ili regiona. Možete se `teleportovati` u bilo koju geohash čet sobu širom sveta jednostavnim unosom njenog taga. Vaše poruke se šalju kroz decentralizovanu mrežu releja, što štiti vašu tačnu lokaciju. Štaviše, svaki put kada se pridružite geohash sobi, dobijate novi, privremeni identitet, dodajući dodatni sloj privatnosti vašim razgovorima zasnovanim na lokaciji.


Za tačnije tehničke detalje, molimo vas da pogledate [zvanični Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Instalacija i podešavanje


### Gde nabaviti Bitchat


Možete instalirati Bitchat putem:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (za iOS uređaje)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (za Android uređaje)


Korisnici Androida takođe imaju alternativne opcije:



- Preuzmite APK direktno sa stranice [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) ili
- Instalirajte putem Nostr-kompatibilnog [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Napomena**: _Ovaj vodič se prvenstveno fokusira na implementaciju za Android. Verzija za iOS može se razlikovati._


### Proces postavljanja


Nakon instalacije, otvorite Bitchat da biste videli ovaj početni ekran sa dozvolama. Evo šta treba da uradite:


1. **Dodeli ove potrebne dozvole:**


   - Bluetooth pristup** (za otkrivanje obližnjih Bitchat korisnika)
   - Precizna lokacija** (Android zahteva ovo za Bluetooth funkcionalnost)
   - Obaveštenja** (za primanje obaveštenja o privatnim porukama)

2. **Onemogući optimizaciju baterije**:


   - Ovo omogućava Bitchat-u da radi u pozadini
   - Kontinuirano održava veze u mreži sa mešom


Dodirnite `Grant Permissions`, pratite `prompts` i `Disable Battery Optimization` da biste prešli na sledeći ekran.


![image](assets/en/02.webp)


Dobrodošli na glavnu stranicu Bitchat-a. Hajde da se upoznamo:


### Postavke


Prvo i najvažnije. Meni sa podešavanjima može se otvoriti dodirom na `Bitchat logo`. Dostupne su sledeće opcije:



- Podesi `appearance` (system/light/dark).
- omogući `Proof of work` za geohash za odvraćanje spama (opciono)
- Uključite `Tor` da poboljšate privatnost.


![image](assets/en/16.webp)


### Postavite svoj identitet


Dodirnite polje `bitchat/anonXXXX` na vrhu da biste izabrali svoje korisničko ime. Ovako će vas drugi videti u Bluetooth i internet režimima. Na primer, možete promeniti "anon2022" u korisničko ime po vašem izboru.


![image](assets/en/03.webp)


### Izaberite Mrežne Kanale


Koristite meni `#location channels` (desno od korisničkog imena) da biste prešli između tipova konekcija:



- BLE Mesh***: Podrazumevani Bluetooth režim (bez interneta, domet od 10 do 50 metara)
- #geohashes**: Internet-enabled geographic communities using [Nostr protocol](https://nostr.com/)


Kada odaberete režim `#geohashes`, Bitchat se integriše sa Nostr protokolom kako bi omogućio geografske zajednice. Vaše poruke se objavljuju na `decentralizovanim Nostr relejima` umesto na Bitchat-ovoj peer-to-peer mreži, omogućavajući šire, ali lokacijski filtrirane razgovore. Ključno je da vaši Bitchat identifikacioni ključevi kriptografski potpisuju sve Nostr događaje kako bi se održala autentifikacija, dok geohash oznake (kao što je `#u4pruyd` za komšiluk) filtriraju poruke na izabrani nivo preciznosti. To znači da možete učestvovati u lokalnim diskusijama bez otkrivanja tačnih koordinata, iako je potreban pristup internetu.


![image](assets/en/04.webp)


### Nadzirati vršnjake

licenca: CC-BY-SA-V4

Brojač vršnjaka prikazuje korisnike:



- U blizini (BLE Mesh) ili
- U vašoj geohash zoni (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Globalni Čet & Privatne Poruke


Bitchat pruža dva različita načina komunikacije kako bi zadovoljio različite potrebe:



- Javni kanali:** Za otvorene razgovore sa drugima. Možete se povezati ili putem lokalne BLE mesh mreže za korisnike u blizini ili putem globalnog #geohash-a za internet-omogućene, lokacione zajednice.
- Privatne poruke:** Za sigurne, jedan-na-jedan razgovore. One uspostavljaju direktnu, šifrovanu vezu kako bi vaša komunikacija ostala poverljiva.


Razumevanje oba režima pomoći će vam da se snađete u svojim razgovorima.


### Javni Kanali: Centar Zajednice


Meni `#location channels` (gore-desno) kontroliše vašu javnu vidljivost. Odabirom `mesh` povezujete se sa svim obližnjim korisnicima putem BLE mreže, obično uređajima unutar 10-50 metara. Ovo stvara otvoreni forum gde se poruke emituju svima u dometu, idealno za najave događaja ili lokalna upozorenja.


Za šire geografsko pokrivanje, izaberite bilo koju `#geohash` oznaku da se pridružite internetom podržanim zajednicama filtriranim po lokaciji. Ovi kanali koriste Nostr protokole za prenos, omogućavajući komunikaciju između gradova ili regiona uz održavanje relevantnosti zasnovane na lokaciji. Vaše poruke se pojavljuju uživo drugim korisnicima u istom kanalu, a novi učesnici automatski vide nedavnu istoriju poruka prilikom pridruživanja.


![image](assets/en/06.webp)


### Privatni razgovori: Sigurni i šifrovani


Da biste započeli privatni razgovor, jednostavno dodirnite bilo koje `korisničko ime` prikazano u `Pregledu vršnjaka.` Takođe možete dodirnuti `ikonu zvezde` da označite ovog korisnika kao omiljenog, što će ga zadržati vidljivim na vašoj listi kontakata čak i kada je van mreže.


![image](assets/en/07.webp)


Bitchat automatski pokreće svoj `sigurnosni handshake` kada započnete privatni razgovor. Uređaji razmenjuju efemerne ključeve kako bi kreirali enkriptovani tunel specifično za vaš razgovor. Ovaj proces osigurava da sve vaše poruke i deljeni fajlovi ostanu poverljivi zahvaljujući kontinuiranoj end-to-end enkripciji. Privatne poruke podržavaju deljenje teksta i fajlova.


![image](assets/en/08.webp)


## 4️⃣ Dodatne funkcije


Možete odmah pristupiti panelu akcija tako što ćete otkucati `/` bilo gde u Bitchat-u. Ovo otkriva meni komandi za brze akcije.



- Upravljaj vezama**: `Blokiraj korisnike` ili `Odblokiraj saradnike`
- Kontrole kanala**: `Prikaži kanale` ili `Pridruži se/kreiraj kanal`
- Društvene interakcije**: `Pošalji topli zagrljaj`  ili `udari pastrmkom` 🎣
- Održavanje ćaskanja**: `Obriši poruke ćaskanja`
- Alati za privatnost**: `Vidi ko je online` ili `Pošalji privatnu poruku`


Komande se izvršavaju odmah - kao `/block Satoshi` da utišate kritičare ili `/hug Hal` da širite pozitivnost 🫂.


![image](assets/en/09.webp)


## 5️⃣ Kreiranje kanala


Kanali u Bitchat-u omogućavaju organizovanu komunikaciju oko tema, lokacija ili zajednica. Da biste kreirali svoj, pratite ovaj tok rada:


### Korak 1: Kreirajte kanal


Da biste kreirali kanal, otkucajte `/j` ili `/join` praćeno `imenom kanala` u bilo kom četu (npr. `/j <imekanala>`). Nakon kreiranja, pojavljuje se nova `ikona ⧉` koja označava novi kanal. Drugi korisnici mogu se pridružiti otkucavanjem iste komande (npr. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Korak 2: Konfigurišite postavke


Pored podrazumevanih komandi, sledeća podešavanja su dostupna unutar kanala:



- `/save` za čuvanje poruka lokalno
- `/transfer` za prenos vlasništva kanala i
- `/pass` za promenu lozinke kanala.


Za privatne zajednice, ova komanda omogućava zaštitu lozinkom, zahtevajući od odobrenih članova da unesu prilagođenu lozinku pre nego što se pridruže.


## 6️⃣ Panic Mode


Sada, hajde da razgovaramo o tom `panic mode`: trostrukim pritiskom na `Bitchat logo` pokreće se potpuno brisanje svih lokalnih poruka i podataka unutar aplikacije. Ovo je vaša ultimativna zaštita privatnosti, savršena za situacije koje zahtevaju trenutnu diskreciju.


**Važno podsećanje:** _Panic mod je trajan. Jednom aktiviran, podaci se ne mogu povratiti. Koristite sa oprezom._


![image](assets/en/11.webp)


## 7️⃣  Geohashes


Geohash kanali omogućavaju ciljane razgovore zasnovane na `geografskim lokacijama` umesto tradicionalnih mrežnih veza. Ova funkcija pretvara bitchat u alat za komunikaciju svestan lokacije, idealan za lokalnu koordinaciju, izgradnju zajednice i diskusije specifične za lokaciju.


### Kako `#geohashes` funkcionišu


Sistem deli svet na mrežne kvadrate koristeći [Geohash sistem](https://en.wikipedia.org/wiki/Geohash), gde svaki karakter u hešu predstavlja veću preciznost:



- Nivo 4** (npr., `u33d`): Pokriva približno 25km × 25km - idealno za diskusije na nivou grada
- Nivo 6** (npr., `u33d8z`): Pokriva oko 1,2 km × 1,2 km - preciznost na nivou komšiluka
- Nivo 8** (npr., `u33d8z1k`): Pokriva otprilike 150 m × 150 m - tačnost na nivou ulice


Precizna selekcija balansira privatnost sa korisnošću: viši nivoi stvaraju ekskluzivnije zone, ali preciznije otkrivaju vašu lokaciju.


### Pridruživanje kanalima `#geohash`


1. Pristupite meniju `#location channels`.

2. Izaberite željeni nivo preciznosti i unesite `#geohash` (npr. #u33d)

3. Dodirnite dugme `Teleport` da biste se pridružili `#location channel`.


![image](assets/en/12.webp)


Alternativno, možete dodirnuti `map icon` da biste koristili prikaz mape za određivanje nivoa preciznosti i dodirnuti `select` da biste se pridružili `#location channel`.


![image](assets/en/13.webp)


**Važno podsećanje**: _#geohash funkcionalnost zahteva aktivnu internet konekciju - za razliku od BLE mesh-a koji funkcioniše offline putem Bluetooth-a._


## 8️⃣ Toplotne mape


Toplotne mape su kul način da otkrijete Bitchat događaje i kanale širom sveta. [Bitmap](https://bitmap.lat/) vizualizuje i prati anonimne, lokacijski zasnovane poruke preko Nostr mreže, prikazujući efemerne Nostr događaje. Pogledajte i pridružite se kanalima i četovima specifičnim za lokaciju.


![image](assets/en/15.webp)


## 🎯 Zaključak


Bitchat omogućava sigurnu, decentralizovanu komunikaciju za scenarije gde tradicionalno slanje poruka ne uspeva. Može da funkcioniše bez internet infrastrukture koristeći BLE mesh umrežavanje, što ga čini pogodnim za proteste, zone katastrofa i udaljena područja gde je povezanost ograničena ili cenzurisana. Aplikacija osigurava privatnost kroz efemernu enkripciju ključeva, kanale lokacija zasnovane na geohash-u i režim panike za brisanje podataka.


Aplikacija je još uvek u ranoj fazi razvoja, ali već pokazuje potencijal. Korisnici bi trebalo da očekuju povremene greške i prijave probleme putem [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Planirana su poboljšanja, uključujući integraciju `ecash` za privatne transakcije unutar aplikacije koristeći Cashu protokol.


![image](assets/en/14.webp)


## 📚 Bitchat Resursi


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)