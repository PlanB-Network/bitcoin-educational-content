---
name: Bull Bitcoin Wallet
description: Saznajte kako koristiti Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Ovaj video tutorijal od BTC Sessions vodi vas kroz proces postavljanja i korišćenja Bull Bitcoin Wallet!*


Ovaj vodič vas vodi kroz instalaciju, konfiguraciju i korišćenje Bull Bitcoin Wallet. Naučićete kako da šaljete i primate sredstva na Bitcoin On-Chain, Liquid i Lightning mrežama, kao i kako da premestite Bitcoin između njih. Opsežne funkcije wallet čine ga moćnim, sve-u-jednom alatom za upravljanje vašim Bitcoin. Hajde da počnemo.


## Uvod


Bull Bitcoin Wallet, developed by [Bull Bitcoin](https://www.bullbitcoin.com/), je **self-custodial** Bitcoin wallet, što znači da imate potpunu kontrolu nad svojim privatnim ključevima i stoga svojim sredstvima, bez oslanjanja na treću stranu. Otvorenog koda i ukorenjen u Cypherpunk filozofiji, ovaj Wallet kombinuje jednostavnost, poverljivost i napredne funkcije kao što su zamene između mreža i podrška za PayJoin. Omogućava vam upravljanje vašim bitcoinima na tri mreže: **Bitcoin onchain**, **Liquid** i **Lightning**, svaka prilagođena specifičnim upotrebama. Na [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), možete pogledati trenutne teme i nadolazeće razvojne projekte. Kako je projekat 100% otvorenog koda i "izgrađen javno", možete takođe poslati svoje predloge i sve greške na koje naiđete. Dok neki novčanici sada podržavaju više mreža, Bull Bitcoin Wallet se ističe dubokom integracijom funkcija privatnosti na svim njima, čineći ga moćnim alatom za upravljanje vašim Bitcoin na svim glavnim mrežama.


## 1️⃣ Preduslovi


Pre nego što počnete koristiti **Bull Bitcoin Wallet**, uverite se da imate sledeće stavke:



- Compatible Smartphone**: A **iOS** (iPhone ili iPad) ili **Android** uređaj
- Internet konekcija
- Sigurnosna kopija medija**: Zapišite svoju **frazu za oporavak** (12 reči) na papir ili metal i čuvajte je na sigurnom mestu.
- Osnovno znanje**: Minimalno razumevanje Bitcoin koncepta (adrese, transakcije, naknade) je korisno, iako ovaj vodič objašnjava svaki korak za početnike.


## 2️⃣ Instalacija


Aplikaciju možete instalirati putem:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(for iOS devices)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (za Android uređaje)


Korisnici Androida takođe imaju alternativne opcije:



- Preuzmite APK direktno sa stranice [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) ili
- Instalirajte putem Nostr-kompatibilnog [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Nakon instalacije aplikacije, pratite uputstva na ekranu dobrodošlice kako biste konfigurisali svoj nalog.


## 3️⃣ Inicijalna konfiguracija


Pri otvaranju, prikazuju vam se sledeće opcije:



- `Kreiraj Novi Wallet`
- `Oporavi Wallet` and
- `Napredne opcije`


Hajde da počnemo tako što ćemo dodirnuti `Advanced Options`.


Ovde možemo konfigurisati napredna podešavanja pre kreiranja ili oporavka wallet:


1. Omogući `Tor proxy` za usmeravanje saobraćaja preko Tor mreže.

1. [Orbot app](https://orbot.app/en/) treba biti instalirana i pokrenuta pre nego što omogućite

2. Tor Proxy se primenjuje samo na Bitcoin (ne na Liquid) i može rezultirati sporijom vezom.

2. Postavite `Custom Electrum Server`, ili

3. Podesite postavke `Recover Bull`. Više ćemo naučiti o [Recover Bull](https://recoverbull.com/) kasnije.


Nakon što izvršite sve opcionalne prilagodbe, dodirnite `Done`. Ako želite ponovo koristiti postojeći Wallet, kliknite na `Recover Wallet` i unesite 12 reči vaše fraze za oporavak.


Inače, kliknite na `Create a New Wallet`.


![image](assets/en/01.webp)


## 4️⃣ Početni ekran


Pre nego što zaronimo dublje, hajde da pogledamo `Početni ekran` kako bismo se orijentisali:



- `transaction overview` i `settings menu` se nalaze na vrhu.
- `Dostupno stanje` ima opciju privatnosti koja može biti `uključena ili isključena`.
- Pristupite `Bitcoin Bull Exchange` da biste `Kupili, Prodali ili Platili` (ovo zavisi od jurisdikcije i može zahtevati KYC).
- `Transfer` sredstava između novčanika
- `Secure Bitcoin` jednako Onchain Bitcoin Wallet
- `Instant payments` putem Lightning- / Liquid Network *(Napomena: Bull Bitcoin Wallet omogućava plaćanja putem Lightning-a. Sredstva primljena putem Lightning-a se čuvaju na [*Liquid mreži](https://liquid.net/) (u Wallet Instant Payments) zahvaljujući automatskoj zameni putem [*Boltz razmene](https://boltz.exchange/). Ovo vam omogućava interakciju sa Lightning-om bez potrebe za upravljanjem kanalima likvidnosti, dok ostajete u samostalnom staranju.)*
- `Slanje` i `Primanje` sredstava


![image](assets/en/02.webp)


Prvo, hajde da napravimo neke važne konfiguracije i počnemo sa `Backup`.


## 5️⃣ Bekap


Da biste započeli proces bekapa, dodirnite `ikonu zupčanika (⚙)` u gornjem desnom uglu aplikacije i izaberite `Wallet Backup`. Biće vam predstavljene dve metode za osiguranje vašeg wallet: `Šifrovani Trezor` i `Fizički Bekap`. Hajde da istražimo svaku od njih.


![image](assets/en/03.webp)


### Fizička rezervna kopija


Dodirnite `Physical Backup` da biste videli listu od 12 reči koje predstavljaju vašu frazu za oporavak ili seed. Molimo vas da razmotrite sledeće:



- Zapišite svoju `frazu za oporavak` sa najvećom pažnjom. Zapišite je na papir ili metal i čuvajte na sigurnom mestu (sef, vanmrežna lokacija). Ova fraza je vaš jedini način pristupa vašim bitcoinima u slučaju gubitka uređaja ili brisanja aplikacije.
- Takođe je važno napomenuti da svako ko ima ovu frazu može ukrasti sve vaše bitkoine. Nikada je ne čuvajte digitalno:
- Nema snimka ekrana
- Nema rezervnih kopija oblaka, e-pošte ili poruka
- Bez kopiranja/lepljenja (rizik od čuvanja u međumemoriji)


![image](assets/en/25.webp)


Sledeći ekran će vas navesti da stavite reč u pravilan redosled kako biste se uverili da ste ispravno dobili seed frazu. Dobićete potvrdu kada je test završen i uspešan.


! **Ova tačka je kritična**. Za dalju pomoć :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Šifrovani trezor


Postoji i opcija šifrovane, anonimne rezervne kopije u oblaku. Ali zar nismo pomenuli u poslednjem pasusu da su rezervne kopije u oblaku rizične i da ih treba izbegavati? Međutim, tim Bull Bitcoin je razvio pametan način da proces učini bezbednim. Evo kako to funkcioniše:


`Recoverbull` je protokol za pravljenje rezervnih kopija koji pojednostavljuje osiguranje vašeg Bitcoin wallet tako što deli rezervnu kopiju na dva dela. Prvo, rezervna kopija vašeg wallet se šifrira na vašem uređaju koristeći jak ključ za šifrovanje. Ovu šifrovanu datoteku možete sačuvati gde god želite, kao što su Google Drive ili vaš uređaj. Drugo, ključ za šifrovanje potreban za otključavanje datoteke čuva Recoverbull Key Server. Da biste povratili vaš wallet, potrebni su vam i šifrovana rezervna kopija i ključ, kojem pristupate pomoću vašeg PIN-a ili lozinke. Ovaj dizajn osigurava da vaša rezervna kopija u oblaku sama po sebi nije korisna i da server ključeva sam po sebi nije koristan bez vaše specifične rezervne kopije. Ovo čuva vaša sredstva sigurnim čak i ako je jedan deo kompromitovan.


Zamislite to kao sef. Šifrovana rezervna datoteka je *kutija*, koju možete čuvati bilo gde (kao što je Google Drive). Vaš PIN za oporavak je *ključ*, koji je odvojeno uskladišten od strane Recoverbull Key Server-a. Lopov bi morao da dobije i vašu specifičnu kutiju i vaš specifični ključ da bi je otvorio. Ovaj dizajn osigurava da čak i ako neko dobije vašu rezervnu datoteku, ona je beskorisna bez ključa sa servera, a ključ sa servera je beskoristan bez vaše jedinstvene rezervne datoteke.


Saznajte više o `Recoverbull` wallet protokolu za bekap [ovde](https://recoverbull.com/).


Dodirnite `Encrypted vault`, a zatim `Continue` da potvrdite korišćenje Podrazumevanog Servera. Veza će biti usmerena kroz `Tor` Mrežu kako bi se osigurala privatnost i anonimnost.


**Razumevanje Vaših PIN-ova**



- `PIN za otključavanje aplikacije`**:** Opcioni PIN postavljen u `Podešavanja > Sigurnosni PIN` za zaključavanje aplikacije na vašem telefonu.
- `Recovery PIN`**:** Obavezni PIN kreiran tokom procesa bekapa `Encrypted Vault`, koristi se za dešifrovanje vaše bekap datoteke tokom oporavka.


Ovo su dva odvojena PIN-a. Ne zaboravite svoj PIN za oporavak, jer je neophodan za vraćanje vašeg wallet."


**Podešavanje PIN-a za oporavak:**



- Morate kreirati PIN ili lozinku za povratak pristupa vašem wallet.
- PIN / Lozinka mora imati najmanje 6 cifara (npr., izbegavajte jednostavne sekvence poput 123456, koje nisu prihvaćene).
- Bez ovog PIN-a, oporavak wallet je nemoguć.


Zatim, izaberite provajdera trezora:



- `Google Drive` ili
- a `custom location` (npr. vaš uređaj)


![image](assets/en/04.webp)


Sada, sačuvaj `backup file`. Zatim, dodirni `Test Recovery`, izaberi svoj sačuvani backup fajl ili trezor, a potom dodirni `Decrypt Vault`. Unesi svoj `PIN` ili `Password`. Ako je sve uspelo, pojaviće se ekran `Test completed successfully`.


### Uvoz / Izvoz Oznaka


Sada kada smo kreirali našu rezervnu kopiju, pogledajmo `Labels`. Bull Bitcoin wallet poboljšava privatnost i organizaciju omogućavajući korisnicima da kreiraju prilagođene oznake za svoje adrese za primanje i transakcije. Ove oznake pomažu vam da kategorizujete svoja sredstva, jer će transakcije poslate na adresu sa oznakom naslediti tu oznaku, a možete takođe označiti odlazne transakcije kako biste pratili njihovu promenu. wallet u potpunosti podržava standard [BIP-329](https://bip329.org/), što znači da možete izvesti sve svoje oznake u datoteku i uvesti ih u drugi wallet. Ova funkcija osigurava da možete besprekorno napraviti rezervnu kopiju svoje istorije transakcija i kategorizacija, ili ih migrirati između različitih instanci wallet, bez gubitka vaše personalizovane organizacije.


![image](assets/en/05.webp)


## 6️⃣ Postavke


Sa vašom primarnom rezervnom kopijom osiguranom, hajde da istražimo ostale funkcije dostupne u podešavanjima.


### A - Obezbeđivanje pristupa


Da biste osigurali aplikaciju, idite na `Settings` i izaberite `Security PIN` da biste odabrali PIN kod. Kreirajte jak PIN da zaključate pristup vašem wallet. Iako je ovaj korak opcionalan, toplo se preporučuje da sprečite neovlašćen pristup ako neko drugi koristi vaš telefon.


![image](assets/en/06.webp)


### B - Povezivanje sa ličnim čvorom (opciono)


Wallet BullBitcoin se po podrazumevanoj vrednosti povezuje sa Electrum serverima: prvi kojim upravlja Bull Bitcoin i sekundarni server od Blockstream-a, za koje se smatra da ne vode evidenciju, čime se smanjuje rizik od praćenja.


Za veću poverljivost, možete povezati aplikaciju sa sopstvenim Bitcoin čvorom preko Electrum servera. Da biste to uradili, dodirnite `Settings` > `Bitcoin Settings` > `Electrum Server Settings`, zatim dodirnite `+ Add Custom Server` da unesete adresu i akreditive vašeg servera.


![image](assets/en/07.webp)


### C - Valuta


Dostupno stanje je prikazano na glavnom ekranu u oba oblika `sats` i `USD`. Da biste to promenili, idite na `Settings` > `Currency`. Tamo možete menjati između `sats/BTC` i odabrati vašu `podrazumevanu fiat valutu`.


![image](assets/en/08.webp)


### D - Bitcoin Postavke


Meni `Bitcoin Settings` nudi dubok pristup osnovnim konfiguracijama i podacima vašeg wallet. Ovde možete pregledati osnovne detalje vašeg `Secure Bitcoin` i `Instant payments wallets`, pružajući vam potpunu transparentnost i kontrolu. Ključne funkcije unutar ovog menija uključuju:



- Wallet Detalji:** Navigirajte do vašeg Secure Bitcoin ili Instant payments wallet da biste videli specifične informacije.
- Wallet Fingerprint:** Jedinstveni identifikator za vaš wallet.
- Javni ključ (Pubkey):** Ključ koji se koristi za generate vaše Bitcoin adrese za primanje.
- Descriptor:** Tehnički rezime strukture vašeg wallet.
- Putanja derivacije:** Specifična putanja korišćena za generate sve adrese iz vašeg glavnog privatnog ključa.
- Address Pregled:** Pristupite listi vaših neiskorišćenih adresa za primanje i promena adresa (uskoro)


Štaviše, imate opciju da:



- Postavke `Enable Auto Transfer` za postavljanje maksimalnog trenutnog wallet salda, koji će zatim biti automatski prebačen na sigurni bitcoin wallet.
- Uvezi Generic novčanike putem `Mnemonic` Fraze ili uvezi `samo za gledanje`
- Poveži `Hardware wallets`: trenutno podržani uređaji su ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade i Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Direktno sa wallet, imate pristup [Bull Bitcoin berzi](https://www.bullbitcoin.com/), što vam omogućava da kupujete, prodajete i plaćate Bitcoin bez napuštanja aplikacije. Ova integracija pruža praktično rešenje za upravljanje vašim Bitcoin potrebama. Imajte na umu da pristup berzi i njenim uslugama može biti ograničen u zavisnosti od vaše jurisdikcije, a završetak verifikacije "Upoznaj svog kupca" (KYC) može biti potreban kako bi se ispunili regulatorni standardi i koristile sve funkcije platforme.


Da biste započeli, dodirnite `Exchange` u donjem desnom uglu, zatim `Sign up` ili `Login` na vaš nalog.


Razmena nudi sledeće [karakteristike](https://www.bullbitcoin.com/):



- Kupite Bitcoin sa samostalnim čuvanjem sa vašeg bankovnog računa
- Nekustodijalni
- Pojedinci ili korporacije
- Trenutno povlačenje
- Nema skrivenih naknada
- Lightning Network dostupno
- Bez ograničenja transakcija
- Opcije ponovljene kupovine


![image](assets/en/09.webp)


Da biste saznali više, posetite ovaj vodič:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Primanje sredstava


Primanje sredstava putem **Bull Bitcoin Wallet** je jednostavno i fleksibilno, podržavajući tri različite mreže prilagođene za različite slučajeve upotrebe:



- Mreža `Bitcoin (onchain)` za sigurno, dugoročno skladištenje.
- Mreža `Liquid` za brze, poverljivije transakcije.
- Mreža `Lightning` za trenutna plaćanja niske cene.


Aplikacija automatski generiše odgovarajuću adresu ili fakturu na osnovu odabrane mreže. Evo kako da nastavite za svaku mrežu.


### Primanje putem Onchain (Bitcoin mreža)


Da biste primili on-chain sredstva, možete ili odabrati `Secure Bitcoin Wallet` sa početnog ekrana i dodirnuti `Receive`, ili dodirnuti glavni `Receive` dugme i zatim izabrati `Bitcoin network`.


Imate dva osnovna načina za generisanje adrese za primanje:


**Podrazumevani režim (URI sa dodatnim ulaznim parametrima)


Podrazumevano, wallet generiše [BIP21 URI](https://bips.dev/21/). Ovo je standardizovani format koji sadrži više informacija od jednostavne adrese, uključujući iznos, ličnu belešku i PayJoin parametre za poboljšanje privatnosti. Ovaj sveobuhvatni URI je kodiran u QR kod i dostupan za kopiranje. Format izgleda ovako: `bitcoin:<address>?<parameter1>=<value1>&<parameter2>=<value2>`.



- Dodatni ulazni parametri:**
    - Iznos:** Navedite traženi iznos u BTC, sats ili fiat valuti.
    - Poruka:** Dodajte ličnu belešku koja će biti vidljiva pošiljaocu.
    - PayJoin:** Omogućite ovu opciju da poboljšate privatnost kombinovanjem ulaza od oba učesnika u transakciji.


Primer URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Važna napomena: Molimo vas da ne šaljete sredstva na adrese u ovom uputstvu, wallet će biti obrisan.*


![image](assets/en/10.webp)


**Kopiraj ili skeniraj Address samo opcija omogućena


Sa omogućenim `Copy or scan Address only option`, aplikacija generiše jednostavnu Bitcoin adresu u SegWit (bech32) formatu.


Primer:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Čak i ako unesete iznos ili belešku, oni neće biti uključeni u QR kod ili kopiranu adresu.


![image](assets/en/11.webp)


### Prijem putem Liquid Network


Možete primiti uplatu na Liquid Network. Kada ste na ekranu `Receive`, imate iste dve opcije za generisanje zahteva za uplatu:


**1. Simple Address:** Kopirajte standardnu `Liquid adresu`. Ovo je jedinstveni identifikator za vaš wallet na Liquid mreži i ne uključuje bilo koji specifičan iznos ili poruku.


Primer Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Detaljan zahtev za plaćanje (URI):** Za strukturiraniji zahtev, možete navesti iznos i ličnu belešku. Ove informacije se automatski kodiraju u deljivi URI i odgovarajući QR kod.



- Amount:** Možete postaviti iznos u Bitcoin (BTC), Satoshis (Sats), ili u fiat valuti.
- Napomena:** Dodajte ličnu poruku da identifikujete transakciju.


**Primer URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Da biste završili transakciju, pošaljite `adresu` ili `URI` pošiljaocu. To možete učiniti kopiranjem u vaš clipboard ili tako što će oni skenirati QR kod direktno sa vašeg ekrana.


![image](assets/en/12.webp)


### Primanje putem Lightninga



Bull Bitcoin Wallet takođe vam omogućava slanje i primanje uplata putem Lightning Network. Ključna karakteristika je da se sredstva primljena putem Lightning-a automatski menjaju i čuvaju na `Liquid Network` unutar vašeg `Instant Payments Wallet`. Ovu uslugu pokreće `Boltz`. Ovaj dizajn vam omogućava da uživate u brzini i niskim troškovima Lightning-a bez složenosti upravljanja kanalima likvidnosti, a sve to uz potpuno samostalno čuvanje vaših sredstava. Iako je ovaj hibridni pristup samostalno čuvanje i izbegava složenost upravljanja kanalima, uvodi uslugu treće strane (Boltz), malu naknadu za zamenu i oslanjanje na federaciju funkcionera Liquid Network kao ključnih čuvara, što je drugačije od tradicionalnog, nekustodijalnog Lightning wallet gde sami upravljate svojim kanalima. Više o Liquid i njihovom modelu upravljanja možete saznati ovde:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Ograničenja:**
    - Minimalni iznos:** Potreban je minimalni iznos fakture. Molimo proverite aplikaciju za trenutni limit.
    - Naknade:** Vi, primalac, odgovorni ste za malu naknadu za zamenu. Ova naknada se oduzima od iznosa koji pošiljalac prenosi i podložna je promenama.
- Prednosti:**
    - Self-Custodial:** Vaša sredstva su uvek pod vašom kontrolom, osigurana na Liquid mreži.
    - Izbegnite visoke On-Chain naknade:** Korišćenjem Lightning-a i skladištenjem na Liquid, zaobilazite on-chain naknade povezane sa otvaranjem tradicionalnog Lightning kanala. Možete odlučiti da prebacite sredstva na on-chain kanal kasnije, kada akumulirani iznos opravdava trošak.
    - Savjet:** Za najisplativiju transakciju između dva Bull Bitcoin korisnika, koristite **Liquid mrežu direktno** kako biste u potpunosti izbjegli Lightning naknade za zamjenu.


Da biste primili uplatu, morate generate `Lightning fakturu`:


1. `Unesite iznos`**:** Navedite iznos koji želite da primite u Bitcoin (BTC), Satošijima (Sats) ili fiat valuti.

2. `Dodaj belešku` **(Opcionalno):** Uključite belešku ili napomenu. Ovo će biti ugrađeno u fakturu i prikazano u vašoj istoriji transakcija kada uplata bude završena, što će olakšati identifikaciju.

3. `Invoice Validity`**:** Lightning faktura je vremenski osetljiva i ističe nakon **12 sati**. Ako nije plaćena u tom periodu, postaje nevažeća i biće potrebno da generate novu.


Pošaljite pošiljaocu fakturu kopiranjem u vaš clipboard ili im dozvolite da skeniraju QR kod prikazan na vašem ekranu.


![image](assets/en/13.webp)


## 9️⃣ Slanje sredstava


Možete pristupiti ekranu za slanje direktno sa početne stranice ili iz bilo kog od vaših novčanika. Bull Bitcoin Wallet pojednostavljuje proces automatskim detektovanjem odredišne mreže—`Bitcoin`, `Liquid` ili `Lightning`—na osnovu adrese ili fakture koju unesete, bilo da je nalepite ili skenirate putem QR koda.


### On-Chain Prenos putem Bitcoin Mreže


Slanje sredstava on-chain znači da je vaša transakcija direktno zabeležena na Bitcoin blockchain-u. Ova metoda je najbolja za veće transfere ili transfere koji nisu vremenski osetljivi. Da biste započeli, možete dodirnuti `Send Button` dole desno, i skenirati ili uneti `standard Bitcoin address`.


Ako adresa koju navedete ne uključuje određeni iznos, bićete upitani da popunite detalje na ekranu za slanje. Možete navesti iznos u svojoj preferiranoj jedinici, kao što su BTC, satoshi ili fiat ekvivalent. Takođe imate opciju da dodate ličnu belešku, koja je privatna napomena za vašu sopstvenu referencu kako biste kasnije lakše identifikovali transakciju. Ova beleška se ne deli sa primaocem.


Suprotno tome, ako zahtev za plaćanje koji skenirate ili nalepite već sadrži sve potrebne detalje, kao što je BIP21 URI sa unapred definisanim iznosom, wallet će zaobići ekran za unos podataka i odvesti vas direktno na ekran za potvrdu kako biste autorizovali plaćanje.


![image](assets/en/14.webp)


Pre nego što vaša transakcija bude emitovana, biće vam prikazan ekran za potvrdu. Ključno je da odvojite trenutak i pažljivo pregledate svaki parametar, obraćajući posebnu pažnju na adresu primaoca, iznos koji se šalje i mrežne naknade. Ovaj ekran takođe pruža moćne alate za prilagođavanje vaše transakcije.


Naknade možete kontrolisati na dva osnovna načina. Prvi metod je da izaberete željenu brzinu transakcije, kao što su niska, srednja ili visoka, i wallet će automatski izračunati odgovarajuću naknadu za vas. Drugi metod omogućava precizniju kontrolu tako što vam dozvoljava da postavite specifičnu naknadu, bilo kao apsolutni iznos u satoshijima ili kao relativnu stopu po bajtu, što zatim pruža procenjeno vreme potvrde.


Za napredne korisnike, wallet nudi nekoliko podešavanja za fino podešavanje transakcije. `Replace-by-Fee` (RBF) je podrazumevano omogućen, što je vredna funkcija koja vam omogućava da ubrzate transakciju ako se zaglavi u mempool-u tako što ćete je ponovo emitovati sa većom naknadom. Takođe možete ručno odabrati koje `Unspent Transaction Outputs` (UTXO-e) želite da potrošite. Ovo je moćan alat za konsolidaciju UTXO, strategiju gde kombinujete više malih ulaza u jedan veći. Iako ovo može koštati više u naknadama za trenutnu transakciju, može značajno smanjiti naknade za buduće transakcije, posebno ako se očekuje rast mrežnih naknada.


![image](assets/en/15.webp)


PayJoin se automatski pokušava kada skenirate zahtev za plaćanje primaoca (BIP21 URI) koji uključuje parametar `pj=`. Ako jednostavno nalepite običnu adresu bez dodatnih parametara, ova funkcija neće biti aktivirana. Ova kolaborativna metoda poboljšava privatnost kombinovanjem ulaza od strane pošiljaoca i primaoca, razbijajući heuristiku zajedničkog vlasništva ulaza i omogućavajući bolje skaliranje i uštedu na naknadama u nekim okolnostima.


### Slanje na Liquid Network


`Liquid Network` je dizajniran za brze, poverljive transakcije sa minimalnim naknadama. Kada šaljete sredstva putem Liquid, ona se povlače sa vašeg `Instant Payments Wallet`. Proces je jednostavan: jednostavno unesete ili skenirate primaočevu `Liquid adresu`.


Ako adresa ne navodi iznos, bićete zamoljeni da ga unesete na ekranu za slanje. Možete uneti iznos u BTC, satoshijima ili fiat valuti. Ključna prednost Liquid je njegov nizak minimalni prag. Kao i kod on-chain transakcija, možete dodati opcionalnu ličnu belešku za sopstvene evidencije. Ako zahtev za plaćanje već uključuje iznos, wallet će direktno preći na ekran za potvrdu.


Na ekranu za potvrdu transakcije Liquid, pregledaćete detalje. Naknade su primetno niske i izračunavaju se na osnovu složenosti transakcije. Obično su oko 0.1 sat/vB, što za jednostavnu transakciju iznosi samo 20-40 satoshija (na primer, 26 satoshija od 21. decembra 2025).


![image](assets/en/16.webp)


### Slanje na Lightning Network


Možete ili skenirati Lightning Address (npr. `runningbitcoin@rizful.com`) što vam omogućava da postavite iznos i opcionalnu belešku za primaoca, ili skenirati fakturu sa unapred definisanim iznosom, što vas vodi direktno na ekran za potvrdu.


*Imajte na umu da se primenjuju minimalni iznosi i naknade.*


Bull Bitcoin Wallet šalje Lightning uplate povlačenjem sredstava sa vašeg `Instant Payments Wallet` (na Liquid) i zamenom putem `Boltz`. Ovaj hibridni pristup je potpuno samostalno skrbnički i izbegava visoke on-chain naknade za upravljanje posvećenim Lightning kanalom, ali zahteva plaćanje `swap fee`. Za najniže troškove, šaljite direktno na Liquid adresu primaoca ako i oni koriste Bull Bitcoin wallet.


## 🔟 Prenos sredstava između vaših novčanika


Bull Bitcoin vam omogućava da premestite svoj Bitcoin između vašeg `Secure Bitcoin` wallet i vašeg `Instant Payments Wallet` na Liquid Network ili na `external Wallet`. Da biste izvršili transfer, jednostavno idite na odeljak `Transfer`, izaberite izvorni i odredišni novčanik, unesite iznos koji želite da premestite i potvrdite transakciju.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Oporavak vašeg Bull Bitcoin Wallet


Ovaj odeljak objašnjava kako da povratite pristup svojim Bull Bitcoin Wallet sredstvima ako izgubite uređaj, deinstalirate aplikaciju ili jednostavno treba da pređete na novi uređaj. Kao što je već objašnjeno, postoje dva osnovna metoda za oporavak: korišćenjem jedinstvenog `Recoverbull` metoda i korišćenjem standardne `BIP39 seed fraze`.


### Metod 1: Recoverbull


Sažetak: Wallet rezervne kopije su šifrovane lokalno. Šifrovana datoteka može biti sačuvana u cloud skladištu ili na drugom uređaju. Ključ za šifrovanje čuva Recoverbull Key Server. Obe komponente su odvojene i moraju biti kombinovane da bi se povratio wallet.


Da počnem, izbrisaću Wallet sa svim sredstvima na njemu i ponovo instalirati wallet. Ponovo ćemo se naći na `Welcome screen`. Ovog puta, izaberite opciju `Recover Wallet`. Zatim, idite na metod `Encrypted Vault`, potvrdite korišćenjem `Default Key server`, i izaberite lokaciju ili `Vault provider` gde ste sačuvali rezervnu kopiju.


![image](assets/en/18.webp)


Navodi se da je trezor uspešno uvezen. Dodirnite dugme `Decrypt Vault` i unesite `PIN`. Sledeći ekran će prikazati vaše `stanje` i `broj transakcija` koje su oporavljene.


![image](assets/en/19.webp)


### Metod 2: Seed Phrase


Ova metoda koristi glavnu frazu za oporavak vašeg wallet, standardnu listu od 12 reči koja služi kao krajnja sigurnosna kopija za vaša sredstva. To je najuniverzalniji način za oporavak Bitcoin wallet, jer nije vezan ni za jednu specifičnu uslugu ili server. Sve dok imate ovu frazu, možete obnoviti vaš wallet na bilo kom kompatibilnom uređaju, čak i bez pristupa Bull Bitcoin Key Server-u.


Sa ekrana dobrodošlice, izaberite `Recover Wallet`. Ovog puta, izaberite metod `Physical backup`. Aplikacija će prikazati mrežu reči. Pažljivo izaberite svaku reč vaše 12-reči seed fraze u tačnom redosledu. Budite precizni, jer jedna greška će rezultirati netačnim wallet.


## 1️⃣2️⃣ Povezivanje Hardware Wallet


Za najviši nivo sigurnosti, mnogi korisnici Bitcoin odlučuju da čuvaju svoja sredstva u `cold storage`. To znači da `privatni ključevi` koji kontrolišu vaš Bitcoin budu na uređaju koji nikada nije povezan na internet. `Hardware wallet` (ili uređaj za potpisivanje) je specijalizovani fizički uređaj dizajniran upravo za ovu svrhu. On funkcioniše kao digitalni sef za vaše ključeve, osiguravajući da nikada nisu izloženi potencijalnim pretnjama online računara ili pametnog telefona.


Povezivanjem hardvera wallet sa aplikacijom Bull Bitcoin, dobijate najbolje iz oba sveta: beskompromisnu sigurnost hladnog skladišta za vaše privatne ključeve, u kombinaciji sa moćnim funkcijama i korisnički prijatnim interfejsom Bull Bitcoin wallet za pregled stanja i upravljanje transakcijama. U ovom poslednjem poglavlju, pokazaćemo vam kako da povežete hardver wallet, kao što je [Coldcard Q](https://coldcard.com/q), sa vašim Bull Bitcoin wallet. Ovaj vodič neće pokrivati detaljno postavljanje Coldcard Q; o tome možete saznati ovde:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Uvoz Wallet


![image](assets/en/26.webp)


Prvo, iz glavnog menija na vašem Coldcard Q, izaberite `Export Wallet`, zatim odaberite `Bull Wallet`. Vaš Coldcard će generate QR kod.


![image](assets/en/20.webp)


Otvorite Bull Bitcoin Wallet i idite na `Settings` > `Bitcoin Settings` > `Import wallet` i izaberite `Coldcard Q` na vašem telefonu i dodirnite `Open the camera` da skenirate ovaj QR kod za uvoz javnih ključeva vašeg hardverskog wallet.


![image](assets/en/21.webp)


### Primanje sa Coldcard Q


Da biste primili Bitcoin koristeći povezani Coldcard Q, nije potrebno da uređaj bude fizički povezan sa vašim telefonom. Bull Bitcoin Wallet je već uvezao potrebne javne ključeve, omogućavajući mu da samostalno generate adrese.


1. Dodirnite vaš uvezeni Coldcard Q uređaj za potpisivanje i izaberite `Receive`.

2. Aplikacija će automatski prikazati novu Bitcoin adresu sa vašeg Coldcard-ovog wallet.

3. Koristite ovu adresu za primanje sredstava. Bitcoin će biti direktno osiguran na ključeve hardvera wallet, iako je uređaj bio van mreže tokom procesa.


![image](assets/en/22.webp)


### Slanje sa Coldcard Q


Slanje Bitcoin sa vašim Coldcard Q zahteva vašu fizičku potvrdu za autorizaciju bilo koje transakcije. Dok se Bull Wallet aplikacija koristi za kreiranje transakcije, konačni potpis može biti kreiran samo na samom hardveru wallet.


Da biste započeli, otvorite svoj `Coldcard Q` wallet i dodirnite `Pošalji`. Zatim, `otvorite kameru` da skenirate QR kod za adresu primaoca. Nakon skeniranja, unesite `iznos` koji želite poslati i prilagodite `prioritet naknade` po potrebi.


Za više opcija, možete pogledati pod Napredna Podešavanja. Ovde ćete pronaći opciju `Replace by Fee` (RBF), koja je podrazumevano aktivirana i omogućava vam da kasnije ubrzate zaglavljenu transakciju. Takođe imate opciju `Coin Control`, koja vam omogućava da ručno izaberete specifične UTXO-e koje želite da potrošite.


Kada pregledate sve detalje, dodirnite `Show PSBT` da pripremite transakciju.


![image](assets/en/23.webp)


Dodirnite dugme `Scan` na vašem Coldcard Q i koristite njegovu kameru da skenirate QR kod prikazan na vašem telefonu. Ekran Coldcard-a će vam zatim prikazati sve detalje transakcije. Pažljivo proverite iznos, adresu primaoca i vašu adresu za kusur. Ako je sve tačno, pritisnite dugme `Enter` na Coldcard Q da potpišete transakciju. Zatim će se na ekranu pojaviti QR kod potpisane transakcije.


![image](assets/en/24.webp)


Na Bull wallet, dodirnite `I'm done`, zatim dodirnite dugme `Camera` da skenirate QR kod `signed transaction` sa vašeg Coldcard Q. Bull Wallet će sada prikazati ekran sažetka potpisane transakcije. Pregledajte ga još jednom, zatim dodirnite `Broadcast` Transaction. Ovo finalizuje proces slanjem transakcije na Bitcoin mrežu, i vaša sredstva će biti na putu.


## 🎯 Zaključak


Sada ste završili svoje putovanje kroz Bull Bitcoin Wallet. Aplikacija stavlja moćne alate za privatnost i sigurnost na dohvat ruke, čineći napredne funkcije jednostavnim za korišćenje. Pomaže vam da ostanete privatni sa funkcijama kao što su `PayJoin`, koji skriva vaše transakcije na blockchain-u, i `Tor integracija`, koja maskira vašu mrežnu aktivnost od znatiželjnih očiju. Za one koji žele ultimativnu kontrolu, možete se povezati na svoj `lični Bitcoin čvor` kako biste prestali da se oslanjate na servere trećih strana, i koristiti `Hardware wallet` da biste svoje privatne ključeve držali potpuno van mreže i bezbednim. Sa pametnim opcijama za backup i besprekornom podrškom za Bitcoin, Liquid i Lightning, Bull Bitcoin Wallet je snažan, sve-u-jednom izbor za svakoga ko ozbiljno želi da zadrži svoja sredstva privatnim, sigurnim i potpuno pod svojom kontrolom.


## 📚 Bull Wallet Resursi


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)