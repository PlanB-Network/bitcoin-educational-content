---
name: Joinstr
description: Decentralizovani CoinJoin-ovi putem Nostr mreže za suverenu Bitcoin poverljivost
---

![cover](assets/cover.webp)



Transparentnost Bitcoin blockchain-a omogućava praćenje istorije transakcija. CoinJoins prekidaju ove veze mešanjem više istovremenih transakcija, vraćajući nivo poverljivosti uporediv sa gotovinom.



Međutim, tradicionalna rešenja se oslanjaju na centralnog koordinatora kao jedinstvenu tačku otkaza. Wasabi i Samourai su obustavili rad 2024. godine pod regulatornim pritiskom.



**Joinstr** eliminiše ovu slabost korišćenjem decentralizovane Nostr mreže za koordinaciju. Ova aplikacija otvorenog koda omogućava istinski suverene CoinJoin-e, gde nijedna centralna vlast ne može cenzurisati, nadgledati ili prekinuti uslugu.



## Šta je Joinstr?



Joinstr je alat otvorenog koda koji revolucionira pristup CoinJoins korišćenjem Nostr protokola kao koordinacione infrastrukture. Za razliku od centralizovanih rešenja koja zahtevaju posvećen server, Joinstr se oslanja na distribuiranu mrežu Nostr releja kako bi omogućio učesnicima da se direktno koordiniraju između vršnjaka.



**Decentralizovana arhitektura** : Nostr mreža zamenjuje centralnog koordinatora. Učesnici kreiraju ili se pridružuju "bazenima" postavljanjem šifrovanih najava putem Nostr releja. Ove informacije (iznosi, učesnici, adrese) ostaju nerazumljive za releje, osiguravajući da nijedan centralni entitet ne može nadgledati, cenzurisati ili filtrirati CoinJoins.



**SIGHASH_ALL|ANYONECANPAY mechanism**: Joinstr eksploatiše ovu Bitcoin zastavicu potpisa, omogućavajući svakom učesniku da potpiše samo svoj ulaz dok validira sve izlaze. Svaki korisnik generiše svoj PSBT lokalno, zatim ga distribuira putem Nostr-a. Svaki korisnik generiše svoj PSBT lokalno, potpisuje ga, zatim ga distribuira putem Nostr-a. Vaši bitkoini ostaju pod vašom isključivom kontrolom do konačnog potpisa.



**Filozofija**: Joinstr prati Bitcoin cypherpunk etos, sa ciljem postizanja tri cilja: **otpornost na cenzuru** (nema autoriteta koji može zaustaviti uslugu), **potpuna nekustodijalnost** (vi zadržavate svoje privatne ključeve), i **jednako tretiranje** (nema diskriminacije protiv UTXO).



### Glavne karakteristike



**Fleksibilni bazeni**: Za razliku od fiksnih denominacija, bilo koji korisnik može kreirati bazen sa tačno željenim iznosom i ciljnim brojem učesnika, optimizujući korišćenje UTXO bez veštačkog deljenja.



**Transparentne naknade**: Nema naknada za koordinaciju. Samo Bitcoin transakcione naknade se dele jednako između učesnika (nekoliko hiljada satoshija po osobi).



**Efemernost**: Nema zadržavanja korisničkih podataka. Informacije prolaze putem šifrovanih efemernih Nostr poruka, koje se odmah zaboravljaju nakon transakcije.



### Dostupne platforme



Ovaj vodič se fokusira na **Android aplikaciju**, jedino trenutno stabilno i preporučeno rešenje. Postoji Electrum dodatak, ali ima probleme sa kompatibilnošću koji ga čine nestabilnim. Web interfejs je u fazi razvoja.



## Bitcoin Core konfiguracija



Joinstr Android zahteva vezu sa Bitcoin čvorom preko RPC. Prvo morate konfigurisati Bitcoin Core na vašem računaru da prihvati veze sa vašeg telefona.



**Napomena**: Za više detalja o kompletnoj konfiguraciji Bitcoin Core, pogledajte naše posvećene tutorijale :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Zahtevi mreže



#### Pronađite svoju lokalnu IP adresu



Vaš Android telefon mora biti u mogućnosti da dosegne vaš Bitcoin čvor na lokalnoj mreži. Pronađite IP adresu vašeg računara:



**Na macOS-u** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Jednostavna alternativa:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Na Linuxu** :



```bash
hostname -I | awk '{print $1}'
```



**Na Windowsu** :



```cmd
ipconfig
```



Pronađi IPv4 adresu (format `192.168.x.x` ili `10.0.x.x`)



### RPC konfiguracija



#### Izmeni bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Pronađite svoju datoteku `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Otvorite datoteku sa vašim omiljenim uređivačem teksta i dodajte ovu konfiguraciju da aktivirate RPC server.



**Preporučena konfiguracija za početak (označi kao oznaku)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet** konfiguracija (za proizvodnu upotrebu) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Važno** :




- Signet je visoko preporučen** za vaše prve testove: aplikacija je još uvek u razvoju (beta), i greške mogu još uvek postojati. Signet vam omogućava testiranje bez naplate, bez rizikovanja stvarnih sredstava.
- Zamenite `192.168.1.0/24` sa vašom mrežnom podmrežom (npr. ako je vaš IP `192.168.68.57`, koristite `192.168.68.0/24`)



**Bezbednost**: Generiši jaku lozinku :



```bash
openssl rand -base64 32
```



### Inicijalizacija



#### Ponovo pokreni i proveri



1. Potpuno isključite Bitcoin Core


2. Ponovo pokrenite da biste primenili konfiguraciju




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Kada se Bitcoin Core pokrene po prvi put, preuzeće i sinhronizovati blokčejn sa obeleživačima. Ova operacija je mnogo brža nego na mainnet (samo nekoliko minuta). Molimo sačekajte da se sinhronizacija završi pre nego što nastavite.



![CRÉATION DE WALLET](assets/fr/04.webp)



Jednom kada se sinhronizuje, kreirajte novi portfelj klikom na "Create a new wallet". Dajte mu eksplicitno ime kao što je `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Vaš wallet je sada kreiran i spreman za primanje obeleženih bitkoina za testiranje.



#### Dobij obeležene bitkoine (test)



Da biste testirali Joinstr na obeleživaču, potrebni su vam besplatni test bitkoini :



![SIGNET FAUCET](assets/fr/06.webp)



Koristite javnu oznaku kao :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



U Bitcoin Core, generate nova adresa za primanje ("Receive" kartica), kopirajte je i nalepite u formu za faucet. Rešite captcha ako je potrebno. Dobijate besplatne obeležene bitkoine u roku od nekoliko sekundi.



## Android aplikacija



### Instalacija



![APPLICATION ANDROID](assets/fr/07.webp)



Idite na [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) da preuzmete najnoviju verziju APK-a. Na vašem Android pregledaču, preuzmite datoteku, zatim je otvorite da pokrenete instalaciju. Moraćete da omogućite instalaciju iz nepoznatih izvora u sigurnosnim podešavanjima vašeg telefona ako je potrebno.



### Konfiguracija aplikacije



![PERMISSIONS VPN](assets/fr/08.webp)



Prilikom prvog pokretanja, aplikacija Joinstr će tražiti dozvole za kontrolu ugrađenog VPN-a. Prihvatite oba zahteva za dozvolu: kontrolu OpenVPN-a i VPN konekciju. Ove dozvole su potrebne za integraciju VPN-a, koja štiti privatnost vaše mreže.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr aplikacija je organizovana u tri glavne kartice:




- Početna**: Početni ekran
- Pools**: Kreiranje i upravljanje CoinJoin bazenima
- Postavke**: Konfiguracija aplikacije



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigurišite postavke u kartici "Settings":



**1. Nostr Relay**: Nostr relay adresa za koordinaciju bazena




- Primer: `wss://relay.damus.io`
- Ostale preporučene releje: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Važno**: Svi učesnici moraju koristiti **isti Nostr relej** da bi videli i pridružili se istim bazenima. Ako koristite drugi relej, nećete videti bazene kreirane na drugim relejima.



**2. Node URL**: IP adresa vašeg Bitcoin čvora (bez porta)




- Format: `http://VOTRE_IP_LOCALE`
- Primer: `http://192.168.68.57`



**3. RPC Username** : Korisničko ime konfigurisano u `rpcuser=` na vašem bitcoin.conf




- Primer: `satoshi



**4. RPC Password** : Lozinka postavljena u `rpcpassword=` na vašem bitcoin.conf



**5. RPC Port** : RPC port zavisi od mreže




- Mainnet** : `8332`
- Obeleživač**: `38332`



**6. Wallet**: Izaberite Bitcoin Core portfelj koji sadrži UTXO-ove za mešanje




- Primer: `tuto_joinstr_signet`



**7. VPN Gateway**: Odaberite Riseup VPN server




- (Paris) vpn07-par.riseup.net
- Drugi dostupni: Amsterdam, Sijetl, itd.
- ⚠️ **Važno**: Svi učesnici u istom bazenu moraju koristiti **isti VPN Gateway** da bi učestvovali u CoinJoin. Tokom runde mešanja, svi učesnici moraju se pojaviti sa istom izlaznom IP adresom kako bi se sprečila mrežna analiza koja povezuje učesnike.



Aplikacija Joinstr **nativno integriše** Riseup VPN, pojednostavljujući koordinaciju između učesnika.



**Važno** :




- Uverite se da su vaš telefon i računar na istoj lokalnoj WiFi mreži.
- VPN veza će biti automatski aktivirana kada učestvujete u bazenu
- Kliknite na **"Sačuvaj "** kada postavite sve parametre



## Praktična upotreba



### Kreiraj ili pridruži se bazenu



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Imate dve opcije za učešće u CoinJoin:



**Opcija 1: Kreiraj novi bazen**



Kliknite na "Create New Pool" u kartici "Pools". Navedite denominaciju u BTC (npr. 0.002 BTC) i željeni broj učesnika (minimum 2, preporučeno 3-5 za veću anonimnost). Aplikacija zatim čeka da se drugi korisnici pridruže vašem pool-u. Kada se dostigne potreban broj, proces registracije izlaza počinje automatski, i treba da izaberete vaš UTXO za mešanje i kliknete na "Register".



**⏱️ Važno**: Bazeni ističu nakon **10 minuta** neaktivnosti. Ako se ne postigne potreban broj učesnika, bazen će biti automatski zatvoren.



**Opcija 2: Pridružite se postojećem bazenu**



U kartici "View Other Pools", pregledajte dostupne bazene koje su kreirali drugi korisnici. Izaberite bazen koji odgovara vašem iznosu i pridružite mu se. Uverite se da ste konfigurisali isti Nostr relej i VPN Gateway kao i ostali učesnici (pogledajte odeljak Konfiguracija).



**UTXO pravilo selekcije**: Vaš UTXO mora biti nešto viši od denominacije bazena (između +500 i +5000 sats viška).



**Primer**: Za bazen od 0.002 BTC (200,000 sats), koristite UTXO između 200,500 i 205,000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Proces je tada **potpuno automatski**: kada vaš unos bude registrovan, aplikacija čeka da svi učesnici registruju svoje unose. Kada svi unosi budu registrovani, PSBT se kreira, automatski potpisuje vašim ključevima, a zatim kombinuje sa potpisima drugih učesnika. Na kraju, kompletna transakcija se emituje na Bitcoin mreži. Dobijate TXID (identifikator transakcije) kada emitovanje bude završeno. Nije potrebna ručna manipulacija PSBT na Androidu.



### on-chain verifikacija



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Kada transakcija bude emitovana, dobićete TXID (identifikator transakcije). Pogledajte ga na [mempool.space](https://mempool.space) ili u vašem omiljenom pregledaču. Da biste testirali na obeleživaču, koristite [mempool.space/signet](https://mempool.space/signet).



Možete posmatrati :





- N unosa**: Jedan po učesniku (u našem primeru, 2 unosa)
- N identični izlazi**: tačan iznos denominacije (ovde, 2 izlaza od po 0.00199800 BTC)
- Dijagram toka**: mempool.space vizuelno prikazuje mešavinu ulaza i izlaza
- Funkcije** : Transakcija se može identifikovati kao SegWit, Taproot, RBF, itd.



Kako svi glavni izlazi imaju istu količinu, **nemoguće je odrediti koji pripada kome**. Ovo je fundamentalni princip CoinJoin: neodvojivost izlaza.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Imajte na umu**: Ako su vaši UTXO-ovi bili veći od denominacije bazena, imaćete devizne izlaze (viškove). Ovi devizni UTXO-ovi ostaju uočljivi i moraju se upravljati odvojeno od vaših anonimizovanih izlaza. Nikada ih ne kombinujte sa vašim mešanim izlazima.



## CoinJoin paketi kvaliteta i anonimnosti



Efikasnost CoinJoin meri se njegovim **anonset**: brojem izlaza identične vrednosti proizvedenih transakcijom. Što je ovaj broj veći, teže je odrediti koji ulaz odgovara kojem izlazu.



Joinstr trenutno generiše grupe od **2 do 5 učesnika** u proseku. Ove brojke su niže od tradicionalnih centralizovanih koordinatora kao što su Wasabi (50-100 učesnika) ili Whirlpool (5-10 učesnika), ali to je cena decentralizacije.



💡 **Da biste detaljno razumeli skupove anonimnosti i njihovo izračunavanje**, pogledajte naš kompletan kurs: [Skupovi anonimnosti](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. other CoinJoins




| Aspekt | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Učesnici po basu** | 50-100 | 5-10 | Promenljiv (P2P) | **2-5** |
| **Koordinator** | Centralizovan (zatvoren 2024) | Centralizovan (aktivan) | P2P maker/taker | **Nije (Nostr)** |
| **Otpornost na cenzuru** | Slaba | Srednja | Veoma visoka | **Veoma visoka** |
| **Naknade za koordinaciju** | Procenat | Ulazna naknada | Plaćeno tvorcima | **Nije** |
| **UTXO diskriminacija** | Da (crne liste) | Ne | Ne | **Ne** |

💡 **Ostala aktivna CoinJoin rešenja** :




- Ashigaru**: Implementacija otvorenog koda Whirlpool protokola sa centralizovanim koordinatorom, ali primenljiva na decentralizovan način. Nastavlja sa radom nakon zaplene Samourai Wallet u 2024.
- JoinMarket**: Decentralizovano P2P rešenje bez centralnog koordinatora, zasnovano na poslovnom modelu proizvođač/potrošač gde "proizvođači" obezbeđuju likvidnost i bivaju nagrađeni od strane "potrošača".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Osnovna kompromis**: Joinstr i JoinMarket su jedina dva rešenja bez centralnog koordinatora. JoinMarket koristi P2P poslovni model sa finansijskim podsticajima, dok Joinstr koristi Nostr za besplatnu koordinaciju. Joinstr žrtvuje trenutnu anonimnost velikih razmera u korist jednostavnosti (bez upravljanja maker/taker) i potpunog odsustva koordinacionih naknada.



**Praktična preporuka**: Da biste nadoknadili manje grupe, sprovedite nekoliko uzastopnih rundi CoinJoin sa različitim učesnicima. Razmaknite svoje runde i promenite Nostr releje između svake runde kako biste maksimizirali svoju poverljivost.



Slobodno se posavetujte sa našim kompletnim kursom o privatnosti bitcoina za više informacija o ovoj temi:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prednosti i ograničenja



### Istaknuto



**Poboljšana privatnost**: Kombinacija Nostr enkripcije komunikacija, deljenog VPN-a između učesnika i preporučene upotrebe Tor-a stvara višeslojnu zaštitu koju je teško zaobići.



**Transparentni, minimalni troškovi**: Nema troškova koordinacije, samo mining troškovi se pravedno dele između učesnika. Nema procenta koji naplaćuje bilo koji operater.



### Ograničenja koja treba razmotriti





- Promenljiva likvidnost**: Manji bazeni, može čekati da se učesnici okupe
- Projekat u toku**: Aplikacija u beta verziji, mogući su bagovi. Prvo testirajte sa malim iznosima na obeleživaču.
- Sybil napadi**: Mogućnost da jedan protivnik kontroliše nekoliko učesnika u bazenu



## Najbolje prakse



**UTXO izolacija**: Nikada ne kombinujte mešani UTXO sa nemješanim. Koristite poseban portfelj za vaše anonimizirane izlaze.



**Više rundi je neophodno**: Izvedite najmanje 3 uzastopne runde sa različitim učesnicima. Varirajte iznose i vremena kako biste izbegli obrasce. Razmaknite runde nekoliko sati.



**Zaštita mreže**: Sistematski koristite Tor uz ugrađeni VPN. Generišite efemerne Nostr ključeve za svaku važnu sesiju.



**Oprezan napredak**: Počnite sa obeležavanjem malih količina.



## Zaključak



Joinstr predstavlja zaista decentralizovano Bitcoin rešenje za privatnost. Korišćenjem Nostr-a za koordinaciju, eliminiše zavisnost od centralnih koordinatora, dok očuvava suverenitet korisnika.



**Za korisnike koji cene otpornost na cenzuru i spremni su da izvedu nekoliko rundi CoinJoin kako bi nadoknadili manje bazene.



U pozadini sve većeg finansijskog nadzora, decentralizovani alati za zaštitu privatnosti postaju neophodni.



## Resursi



### Zvanična dokumentacija




- [Joinstr official website](https://joinstr.xyz)
- [Korisnička dokumentacija](https://docs.joinstr.xyz/users/using-joinstr)
- [Tehnička dokumentacija](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab izvorni kod](https://gitlab.com/invincible-privacy/joinstr)
- [Android aplikacija](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Tutorijali




- [Electrum plugin tutorial](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Kompletan vodič od Uncensored Tech



### Zajednica i podrška




- [Telegram Joinstr Group](https://t.me/joinstr) - Podrška zajednice i kutak za obeleživače
- [Tehnička diskusija o DelvingBitcoin-u](https://delvingbitcoin.org/t/ko-ce-upravljati-coinjoin-koordinatorima/934)



### Dodatni alati




- [Bookmark Faucet](https://signetfaucet.com) - Besplatni testni Bitcoini
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternativa
- [Mempool.space](https://mempool.space) - Block explorer sa analizom privatnosti