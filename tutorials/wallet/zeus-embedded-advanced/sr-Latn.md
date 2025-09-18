---
name: Zeus Embedded - Napredni
description: Više-čvorni samostalno-kustodijalni Lightning novčanik
---

![Zeus](assets/cover.webp)


## Uvod u ZEUS Wallet


ZEUS je mobilna aplikacija za upravljanje Bitcoin Wallet i čvorovima sa punim funkcionalnostima Bitcoin lightning Wallet koja čini Bitcoin plaćanja jednostavnim, daje korisnicima potpunu kontrolu nad njihovim finansijama i omogućava naprednijim korisnicima da upravljaju svojim Lightning čvorovima iz dlana svoje ruke.


### Ko je ZEUS namenjen?

Trenutno je ZEUS namenjen ljudima koji pokreću sopstvene kućne / poslovne čvorove [Lightning Network Daemon (LND)](https://lightning.engineering/) ili [Core Lightning (CLN)](https://blockstream.com/lightning/) i upravljaju njima daljinski putem Zeusa.


Trgovci koji koriste [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) ili [Alby](https://getalby.com/) (ili bilo koji drugi LNDhub nalog) takođe mogu povezati, koristiti i upravljati svojim čvorovima / nalozima putem ZEUS-a.


[Počevši od verzije v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS će početi da zadovoljava prosečne korisnike koji žele jednostavan način da izvrše brza i jeftina bitcoin plaćanja sa svog mobilnog uređaja, koristeći [ugrađeni mobilni Lightning čvor](https://docs.zeusln.app/category/embedded-node) sa integrisanim [Lightning provajderom usluga (LSP)](https://docs.zeusln.app/lsp/intro).


### Važni Zeus resursi:


- Zvanična stranica Zeusa - [https://zeusln.app/](https://zeusln.app/)
- Zeus Dokumentacija - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github repozitorijum](https://github.com/ZeusLN/zeus)
- [Zeus Telegram grupa za podršku](https://t.me/ZeusLN)
- [Zeus na NOSTR-u](https://iris.to/zeus@zeusln.app)
- [Najave na Zeus Blogu](https://blog.zeusln.com)


### Zeus Features

#### Opšte karakteristike:


- Samostalno čuvanje, Bitcoin i samo Lightning Wallet
- Bez naknada za obradu, Bez KYC
- Potpuno otvorenog koda (APGLv3)
- Više čvorova / naloga podržano (možete upravljati svojim kućnim čvorom/čvorovima, pokrenuti ugrađeni LND čvor, povezati se sa više LNDhub naloga)
- Lako za korišćenje meni aktivnosti
- PIN ili passphrase enkripcija, Privatni režim - sakrijte svoje osetljive podatke
- Knjiga kontakata, više tema, više jezika


#### Tehničke karakteristike


- Poveži se preko Tor-a
- Puna podrška za LNURL (plaćanje, povlačenje, autentifikacija, kanal), Slanje na Lightning adrese
- Detaljno upravljanje Lighting kanalom, podrška za MPP/AMP, Keysend, upravljanje naknadama za rutiranje
- Replace-by-fee (RBF) i Child-pays-for-parent (CPFP) podrška
- NFC plaćanja i zahtevi, Potpiši i verifikuj poruke
- SegWit i Taproot podrška
- Jednostavni Taproot Kanali
- Self-custodial lightning addresses (@zeuspay.com)
- Point of Sale by Square (uskoro open PoS)


### Vodiči i video tutorijali

Da biste mogli koristiti Zeus i upravljati Lightning kanalima, likvidnošću, naknadama itd., bolje je prvo pročitati neke važne vodiče o Lightning Network.


#### Vodiči:


- [LND - Dokumentacija za Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Dokumentacija za Core Lightning](https://lightning.readthedocs.io/index.html)
- [Vodič za početnike o Lightningu](https://bitcoiner.guide/lightning/) – od Bitcoin Q&A
- [Upravljanje Lightning čvorom](https://www.lightningnode.info/) – od openoms
- [Lightning mreža i analogija sa aerodromom](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Upravljanje likvidnošću Lightning čvora](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Održavanje Lightning čvora](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video tutorijal od BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Vodič korak-po-korak kako započeti korišćenje Zeus LN ugrađenog čvora na vašem mobilnom uređaju


![Image](assets/en/01.webp)


Posvećujem ovaj vodič svim novim korisnicima Lightning Network (LN) koji žele započeti novo suvereno putovanje koristeći Wallet čvor za samostalno čuvanje na svojim mobilnim uređajima.


Hajde da pretpostavimo da ste već prošli kroz svu tu plejadu kustodijalnih LN novčanika, ali još niste spremni da počnete sa radom na JAVNOM rutiranju LN čvora, već samo želite da gomilate više Sats preko LN na više samokustodijalan način i obavljate svoje redovne uplate preko LN.


Evo Zeusa, počevši od [verzije v0.8.0 objavljene na njihovom blogu](https://blog.zeusln.com/new-release-zeus-v0-8-0/), sada nudi ugrađeni LND čvor u aplikaciji. Do sada je Zeus bio aplikacija za upravljanje udaljenim čvorovima + LNDhub nalozima. Ali sada… čvor je u telefonu!


![Image](assets/en/02.webp)


### Brzi pregled glavnih karakteristika za Zeus Node:



- **Privatni LND čvor** - To znači da ovaj čvor NEĆE obavljati javno usmeravanje plaćanja drugih kroz vaš čvor. Čvor i kanali su neobjavljeni (privatni, nisu vidljivi na javnom LN grafu). Primanje i obavljanje plaćanja će se vršiti preko vaših povezanih LSP partnera. **ZAPAMTITE: Zeus Embedded Node NEĆE obavljati javno usmeravanje!**
- **Uporna LND usluga** - korisnik može aktivirati ovu funkciju i održavati LND uslugu aktivnom neprekidno kao bilo koji regularni LN čvor. Aplikacija ne mora biti otvorena, uporna usluga će održavati svu komunikaciju online.
-   **Neutrino blok filteri** - sinhronizacija blokova se radi koristeći [blok filtere i Neutrino protokol](https://bitcoinops.org/en/topics/compact-block-filters/) (bez davanja informacija o on-chain sredstvima naših korisnika). Podsetnik: za veze sa velikom latencijom / sporim internetom, ova Neutrino zasnovana sinhronizacija blokova ponekad može da ne uspe. Pokušaj prelaska na obližnji Neutrino server može pomoći u vraćanju sinhronizacije. Bez ove sinhronizacije vaš LND čvor ne može da se pokrene!
- **Jednostavni Taproot Kanali** - Kada zatvaraju ove kanale, korisnici imaju manje naknade i dobijaju veću privatnost jer izgledaju kao bilo koja druga Taproot potrošnja kada se ispituje njihov On-Chain otisak.
- **Integrated LSP** - Olympus je novi LSP čvor za Zeus. Korisnici mogu odmah primiti Sats preko LN, bez prethodnog postavljanja LN kanala. Jednostavno će morati kreirati LN Invoice i platiti sa bilo kojeg drugog LN Wallet, uz Zeus 0-conf kanal uslugu. Pročitajte više o Zeus LSP ovde. LSP takođe pruža dodatnu privatnost našim korisnicima tako što im obezbeđuje umotane fakture koje skrivaju javne ključeve njihovih čvorova od platioca.
- **Knjiga kontakata** - možete ručno sačuvati kontakte ili uvesti iz NOSTR-a, za lako slanje uplata vašim redovnim destinacijama.
- **Puna podrška za LNURL, LN Address slanje i primanje** - sada možete postaviti svoj sopstveni self-custodial LN Address sa @zeuspay.com. Podsetnik: Takođe možete koristiti Zeus za LN-auth na sajtovima gde se možete prijaviti sa LN autentifikacijom. Veoma je praktično.
- **Point of Sale** - Sada korisnici trgovci mogu postaviti svoje proizvode i prodavati direktno iz Zeusa, sa integrisanim PoS. Za sada sadrži osnovne potrebe, ali će u budućnosti sadržati proširene funkcije.
- **LND dnevnici** - korisnik može čitati LND servisne dnevnike u realnom vremenu i koristiti ih za otklanjanje mogućih problema (uglavnom za loše veze)
- **Automated Backups** - the LN node channels are automatically back up on the Olympus server. This automated backup is encrypted with your node Wallet seed (without the seed is totally useless). User also can export manually a SCB (static channels backup) for a disaster recovery.


### Kako se pridružiti Zeus LN čvoru (ugrađen LND)


U ovom vodiču govoriću samo o ugrađenom LND čvoru, a ne o drugim načinima korišćenja ove sjajne aplikacije (upravljanje udaljenim čvorovima i LNDhub nalozi). Za ostale tipove konekcija, molim vas pogledajte [stranicu Zeus dokumentacije](https://docs.zeusln.app/category/getting-started), koja je veoma dobro objašnjena i nema potrebe za pisanjem posebnog vodiča.


#### KORAK 1 - POČETNO PODEŠAVANJE


Zbog činjenice da je Zeus pun LND čvor, imaću nekoliko početnih preporuka:



- Ne koristite stari uređaj, to bi moglo uticati na korišćenje ove moćne aplikacije. Posebno u periodu sinhronizacije aplikacija može intenzivno koristiti CPU i RAM. Nedostatak ovih resursa može čak onemogućiti korišćenje Zeus aplikacije.
- Koristite najmanje Android 11 kao mobilni OS i ažurirajte koliko god je moguće. Za iOS isto, pokušajte koristiti mnogo višu verziju OS-a.
- Trebaće vam najmanje 1GB prostora na disku za skladištenje podataka. Vremenom može rasti, ali postoji funkcionalnost za kompresiju baze podataka na nivo MB-a.
- Nema potrebe koristiti Zeus sa Tor ili Orbot servisom. Molim vas, nemojte komplikovati stvari više nego što je potrebno. Tor u ovom slučaju neće vam ponuditi više privatnosti, već će samo pogoršati stvari za inicijalnu sinhronizaciju. Takođe, budite pažljivi sa VPN-ovima koje koristite i proverite latenciju konekcije prema neutrino serverima. Imajte na umu, Neutrino blok filteri ne otkrivaju niti prate identitet vašeg uređaja, već samo služe blokovima. LN saobraćaj je takođe iza LSP-a sa privatnim kanalima, tako da je vrlo malo informacija izloženo, nema razloga za brigu o privatnosti.
-   Budite strpljivi za početnu sinhronizaciju, može potrajati nekoliko minuta. Pokušajte da budete povezani na širokopojasni internet sa dobrom latencijom. Ako pokrećete svoj Bitcoin čvor, [možete aktivirati neutrino servis](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) i povezati svoj Zeus sa sopstvenim čvorom, čak i koristeći internu LAN mrežu, tako da ćete imati maksimalnu brzinu.


Kada postavite tip veze „Embedded node“, aplikacija će se neko vreme sinhronizovati. Strpljivo sačekajte da taj deo završi, a zatim uđite na glavnu stranicu Postavke.


![Image](assets/en/03.webp)


Ukratko, hajde da zaronimo u svaki odeljeni deo Podešavanja i razumemo neke od glavnih funkcija, pre nego što počnete koristiti Zeus:


**A - POSTAVKE**


Ovo je odeljak sa opštim podešavanjima za celu aplikaciju


**1 - Lightning Service Provider (LSP)**


Ovde su predstavljene dve LSP usluge:



- _Kanali u pravo vreme_ - kada nemate otvoren kanal ili dostupnu dolaznu likvidnost, ako je usluga aktivirana, otvoriće kanal u hodu za vas. Ova opcija može biti onemogućena ako ne želite da otvarate više kanala ovog tipa.
- _Zahtevajte kanale unapred_ - možete kupiti dolazne kanale od Olympus LSP direktno u aplikaciji sa više opcija i iznosa (za dolazne i odlazne).


LSP pomaže korisnicima da se povežu na Lightning mrežu otvaranjem platnih kanala ka njihovim čvorovima. [Pročitajte više o LSP ovde](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS ima novi integrisani LSP nazvan [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), koji je dostupan svim korisnicima koji koriste novi ugrađeni čvor.


U ovom odeljku, podrazumevano je Olympus LSP (https://0conf.lnolymp.us), ali uskoro možete postaviti i drugi 0conf LSP koji podržava ovaj protokol.


_Imaj na umu:_

_kada otvorite kanal sa Olympus LSP koristeći umotane LN fakture, takođe dobijate 100k ulazne likvidnosti! Ovo je zaista dobra opcija u slučaju da odmah trebate primiti više Sats._

_Primer: deponuješ 400k Sats da otvoriš LSP kanal, zatim LSP otvara kanal kapaciteta 500k Sats prema tvom Zeus čvoru i prebacuje 400k Sats koje si deponovao na tvoju stranu._

_"Inbound liquidity" = više “prostora” u vašem kanalu za primanje._


U budućnosti se nadamo da ćemo imati mnogo drugih LSP-ova koji bi mogli biti integrisani u Zeus i koristiti se alternativno svaki od njih. Samo je pitanje vremena kada će novi LSP-ovi usvojiti otvoreni standard za ove vrste 0conf kanala.


Ako ne želite da otvarate nove kanale „u hodu“, možete onemogućiti ovu opciju.


U ovom istom odeljku, imate i opciju da izaberete "request Simple Taproot Channels" kada LSP otvori kanal prema vašem Zeus čvoru. Ovi Simple Taproot Kanali nude bolju On-Chain privatnost i niže naknade pri zatvaranju kanala. Postoje samo dva razloga zbog kojih ih ne biste želeli koristiti:



- Oni su novi, i još uvek može biti grešaka u LND kada ih koristite.
- Vaš kontrapartner ih ne podržava. Čak i LND čvorovi moraju eksplicitno da se opredele za njih, za sada.


**2 - Postavke plaćanja**


Ova funkcija će vam omogućiti da postavite sopstvene preferirane naknade za plaćanja, preko LN ili na lancu. Takođe pruža opciju za povećanje ili smanjenje vremena isteka za vaše fakture.


Ako neki od vaših LN plaćanja ne uspeju, možete povećati naknadu kako biste pronašli bolju rutu. Takođe, ako radite onchain transakcije, možete postaviti specifičnu naknadu kako vaša transakcija ne bi ostala zaglavljena u Mempool duže vreme, u slučaju perioda visokih naknada.


**3 - Postavke faktura**


U ovom odeljku su neke opcije za generate fakture:



- Postavite standardni dopis da se prikazuje u Invoice vi generate
- Vreme isteka u sekundama, u slučaju da želite određeno vreme, duže ili kraće, za plaćanje vašeg Invoice
- Uključite naznake rute - pružite informacije za pronalaženje neoglašenih ili privatnih kanala. Ovo omogućava usmeravanje plaćanja ka čvorovima koji nisu javno vidljivi na mreži. Naznaka rute pruža delimičnu rutu između primaočevog privatnog čvora i javnog čvora. Ova naznaka rute se zatim uključuje u Invoice koji generiše primalac i pruža platiocu. Predlažem da bude omogućeno po defaultu, inače dolazna plaćanja mogu propasti (nije pronađena ruta).
- AMP Invoice - Atomska višekanalna plaćanja su nova vrsta Lightning plaćanja implementirana od strane LND koja omogućavaju primanje Sats bez specifičnog Invoice, koristeći [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Praktično je statički kod za plaćanje. [Pročitajte više ovde](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Prikaži prilagođeno preimage polje - koristite ovu opciju samo u vrlo specifičnim slučajevima kada zaista želite koristiti prilagođena polja u preimage. [Pročitajte više ovde](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Još jedna opcija u ovom odeljku je kako postaviti tip onchain Address koji želite da koristite: SegWit nested, SegWit, Taproot.


![Image](assets/en/04.webp)


Kliknite na dugme sa točkićem na vrhu i pojaviće se iskačući ekran za izbor željenog tipa Address. Kada to postavite, sledeći put kada pritisnete dugme za prijem za onchain, generate će izabrati tip Address. Možete ga promeniti u bilo kom trenutku.


**4 - Postavke kanala**


U ovom odeljku unapred postavljate neke karakteristike otvaranja kanala kao:



- broj potvrda
- Najavi kanal (podrazumevano je isključeno), što znači da će biti nenajavljeni kanali.
- Jednostavni Taproot Kanali
- Prikaži dugme za kupovinu kanala


**5 - Postavke privatnosti**


Ovde ćete pronaći osnovna podešavanja za dodavanje više privatnosti koristeći Zeus aplikaciju:



- Block explorer za otvaranje detalja tx (Mempool.space, blockstream.info ili prilagođeni lični)
- Pročitajte međuspremnik - uključivanje/isključivanje ako želite da Zeus čita međuspremnik vašeg uređaja
- Lurker mode - on/off prekidač ako želite sakriti određene osjetljive informacije iz svoje Zeus aplikacije. Dobra je opcija kada pravite demonstracije ili snimke ekrana.
- Mempool predlog naknade - aktivirajte ovu opciju ako želite koristiti preporučene nivoe naknada sa [Mempool.space](https://Mempool.space/)


**6 - Bezbednost**


Ovaj odeljak ima samo dve opcije za obezbeđivanje aplikacije pri otvaranju: postavite lozinku ili PIN.


Kada postavite PIN za otvaranje aplikacije, takođe ćete moći da postavite "PIN za prisilu". Ovaj tajni dodatni PIN će se koristiti SAMO u slučaju situacije prisile, ako ste ugroženi. Ako unesete ovaj PIN, sva konfiguracija će biti OBRISANA. Zato je bolje da redovno ažurirate svoje rezervne kopije. Automatske rezervne kopije su UKLJUČENE po defaultu, ali je dobro imati i svoje rezervne kopije, van uređaja.


**7 - Valuta**


Omogući ili onemogući opciju za prikaz konverzije fiat valuta u korišćenju Zeus aplikacije. Trenutno podržava preko 30 fiat valuta širom sveta.


**8 - Jezik**


Možete se prebacivati između više jezika za prevođenje, pregledanih od strane Zeus zajednice sa izvornim govornicima.


**9 - Prikaz**


U ovom odeljku možete personalizovati svoj Zeus ekran, birajući različite teme boja, podrazumevani ekran (tastatura ili balans), prikazivanje vašeg aliasa čvora, aktiviranje velikih tastera tastature, prikazivanje više decimalnih mesta.


**10 - Prodajno mesto**


Ovo je posebna funkcija za omogućavanje / onemogućavanje integrisanog PoS sistema u Zeus. Možete koristiti samostalni PoS ili povezan sa Square PoS sistemom. Trenutno podržava osnovne funkcionalnosti kao PoS, ali dovoljno za dobar početak i može pomoći malim trgovcima (barovi/restorani, prodavnice) da počnu prihvatati BTC na prirodan način.


Unutar ovih postavki, pronaći ćete razne opcije za postavljanje vašeg PoS-a:



- Potvrda tipa plaćanja: LN samo, 0-potvrda, 1-potvrda
- Omogući / onemogući napojnice za zaposlenog koji upravlja PoS-om
- Prikaži / sakrij tastaturu
- Procenat poreza koji se primenjuje na kartu
- Kreirajte proizvode i kategorije proizvoda
- Jednostavan popis svih prodaja


Ovde je video demonstracija uživo kako koristiti Zeus PoS:


**B - Backup Wallet**


Ugrađeni čvor u ZEUS-u zasnovan je na LND i koristi [aezeed seed format](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Ovo je drugačije od tipičnog [BIP39 formata](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) koji vidite u većini Bitcoin novčanika, iako može izgledati slično. Aezeed uključuje dodatne podatke uključujući datum rođenja Wallet koji će pomoći da se ponovna skeniranja tokom oporavka odvijaju efikasnije.


Format ključa aezeed treba da bude kompatibilan sa sledećim mobilnim novčanicima: Blixt, BlueWallet i Breez. Imajte na umu da sam seed neće biti dovoljan za povraćaj svih vaših stanja ako imate otvorene ili kanale u procesu zatvaranja!


Saznajte više o procesu pravljenja rezervnih kopija i vraćanja na [Zeus Docs stranici](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


SAVET ZA NAPAJANJE: Kada sačuvate vaš seed, molimo vas da sačuvate i node pubkey! Ponekad je dobro imati ga pri ruci, zajedno sa vašim seed i SCB (Staticka Rezerva Kanala) u slučaju da trebate verifikovati oporavak.


SCB je neophodan samo ako imate otvorene LN kanale. U slučaju da imate samo onchain sredstva, nije neophodan.


Ako vidite da se nakon dužeg vremena i dalje ne prikazuje stara istorija transakcija, idite na Embedded node - Peers i onemogućite opciju korišćenja liste izabranih peer-ova (podrazumevano je btcd.lnolymp.us). To će pokrenuti restart i povezaće se sa prvim dostupnim neutrino čvorom sa boljim odzivom. Ili koristite druge dobro poznate neutrino peer-ove navedene ispod.


Ako želite videti više opcija oporavka za LND čvor, [molimo pročitajte moj prethodni vodič](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), gde možete pronaći korake kako da uvezete aezeed seed u Sparrow Wallet ili druge metode.


**C - Ugrađeni Čvor**


U ovom odeljku ćemo pronaći neke osnovne alate za upravljanje integrisanim čvorom:



- _Disaster Recovery_ - Automatske i ručne sigurnosne kopije za LN kanale. Molimo pročitajte više o tome kako koristiti ovu funkciju na Zeus Docs stranici.
- _Express Graph Sync_ - Zeus aplikacija će preuzeti LN gossip data grafikon sa posvećenog servera, za bržu i bolju sinhronizaciju, nudeći najbolje putanje plaćanja. Možete takođe izabrati da obrišete prethodne podatke grafikona pri pokretanju.
- _Peers_ - sekcija za upravljanje neutrino peer-ovima i 0-conf peer-ovima. Ako imate problema sa inicijalnom sinhronizacijom, kanali se ne povezuju, to je zato što vaš uređaj ima visoku latenciju sa konfigurisanim neutrino peer-om. Pokušajte promeniti listu preferiranih peer-ova ili dodajte vaš specifični peer za koji znate da ima bolju latenciju za sinhronizaciju. Dobro poznati neutrino serveri su:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - za region US
 - sg.lnolymp.us - za region Azije
 - btcd-Mainnet.lightning.computer - za region SAD
 - uswest.blixtwallet.com (Seattle) - za US region
 - europe.blixtwallet.com (Nemačka) - za EU region
 - asia.blixtwallet.com - za region Azije
 - node.eldamar.icu - za region US
 - noad.sathoarder.com - za region SAD
 - bb1.breez.technology | bb2.breez.technology - za region SAD
 - neutrino.shock.network - US region



- _LND logovi_ - veoma koristan alat za otklanjanje problema sa vašim LN čvorom i detaljnu kontrolu onoga što se dešava na tehničkom nivou.
- _Advanced settings_ - više alata za kontrolu korišćenja vašeg LND čvora:



 - _Režim pronalaženja puta_ - bimodalni ili apriori, načini za pronalaženje bolje rute za vaše LN uplate i takođe resetovanje prethodnih informacija o rutiranju. Molimo vas da pročitate ove veoma dobre vodiče o pronalaženju puta: [Pronalaženje puta](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - od strane Docs Lightning Engineering i [LN Pronalaženje puta za uplate](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - od strane Voltage.
 - _Persistent LND_ - aktivirajte ovaj režim ako želite da LND servis radi kontinuirano u pozadini i održava vaš čvor online 24/7. Ovo je veoma korisno ako koristite Zeus kao PoS u maloj prodavnici ili primate mnogo LN napojnica preko LN Address.
 - _Rescan wallet_ - ova opcija će pokrenuti pri restartovanju kompletno skeniranje svih onchain transakcija vašeg Wallet. Aktivirajte je samo u slučaju da vam nedostaju neke transakcije u vašem Wallet. Zadatak reskeniranja će potrajati, nekoliko minuta, pa budite strpljivi i uvek proverite logove da biste videli više detalja o napretku.
 - _Compact Database_ - ova opcija je veoma korisna ako vaša Zeus aplikacija zauzima mnogo prostora na uređaju (pogledajte detalje aplikacije u podešavanjima uređaja). Ako imate mnogo aktivnosti koristeći Zeus, preporučujem da češće radite ovu kompakciju. Kada vidite da imate više od 1-1.5GB podataka za Zeus aplikaciju, uradite kompakciju. Aplikacija će se restartovati i potrajaće neko vreme, pa budite strpljivi.
 - _Obriši Neutrino fajlove_ - ova opcija za brisanje neutrino fajlova (sa restartom) će značajno smanjiti upotrebu skladišnog prostora. Smanjenje upotrebe podataka takođe ima veliki uticaj na potrošnju baterije, smanjujući potrošnju baterije, posebno ako koristite Zeus u režimu stalnog rada.


**D - Informacije o čvoru**


U ovom odeljku ćete pronaći više detalja o statusu vašeg Zeus čvora kao:



- Alias - kratki ID čvora
- Javni ključ - puni javni ključ za vaš čvor potreban drugim čvorovima da pronađu put do vašeg čvora. Zapamtite da ovaj javni ključ NIJE vidljiv na regularnim LN Explorerima (Mempool, Amboss, 1ML itd.). Ovaj javni ključ je dostupan SAMO preko vaših povezanih LN partnera i kanala.
- LN implementacija verzija
- verzija aplikacije Zeus
- Sinhronizovano sa lancem i Sinhronizovano sa grafom status - veoma važni, pokazuju tačan status vašeg čvora. Ako ova dva ne prikazuju “true” to znači da se vaš čvor još uvek sinhronizuje ili ima problema sa sinhronizacijom. Preporučuje se da pogledate u vaše LND logove ili sačekate malo duže.
- Visina bloka i Hash - prikazuje poslednji blok i Hash koji je vaš čvor video i sinhronizovao.


**E - Informacije o mreži**


Ovaj odeljak prikazuje više detalja o opštem statusu za Lightning Network, izvučenih iz vaših podataka sinhronizacije grafika: broj dostupnih javnih kanala, broj čvorova, broj zombi kanala (van mreže ili mrtvih), prečnik grafa, prosečan i maksimalan izlazni stepen za graf.


Ovi podaci mogu biti korisni za otklanjanje grešaka ili jednostavno za statistiku.


**F - Lightning Address**


U ovom odeljku korisnik može postaviti sopstveno samostalno čuvanje LN Address @zeuspay.com.


ZEUS PAY koristi heševe preimaga generisane od strane korisnika, HODL fakture i Zaplocker Nostr šemu atestacije kako bi omogućio korisnicima koji možda nisu online 24/7 da primaju uplate na statički lightning Address. Korisnici samo treba da se prijave u svoje ZEUS novčanike u roku od 24 sata da bi preuzeli uplate, inače će biti vraćene pošiljaocu.


Ako aktivirate „persistent mode“ svi plaćanja na vaš LN Address će biti odmah primljeni.


Saznajte kako funkcionišu [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) plaćanja i više o [ZeusPay naknadama ovde](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain Adrese**


U ovom odeljku možete konsultovati vaše generisane onchain adrese za bolju kontrolu novčića.


**H - Kontakti**


U Zeus v 0.8.0 uvedena je nova knjiga kontakata koju možete koristiti za brzo slanje uplata svojim prijateljima i porodici, takođe sa mogućnošću uvoza kontakata iz Nostr-a.


Jednostavno unesite svoj Nostr npub ili čitljiv NIP-05 Address, i ZEUS će pretražiti Nostr za sve vaše kontakte. Odavde možete brzo poslati uplatu kontaktu ili uvesti sve ili odabrane kontakte u vašu lokalnu knjigu kontakata./<


Evo kratkog videa kako da konfigurišete i koristite svoje Zeus kontakte:


**I - Alati**


Ovde imamo različite podsekcije sa više alata:



- _Nalozi_ - ovde možete uvesti spoljne naloge / novčanike, Cold novčanike, Hot novčanike, da biste ih kontrolisali ili koristili kao izvor spoljnog finansiranja za kanale vašeg Zeus čvora. Ova funkcija je još uvek eksperimentalna.
- _Ubrzaj transakciju_ - Ova funkcija može biti korisna kada imate zaglavljenu tx u Mempool i želite da povećate naknadu. Moraćete da obezbedite izlaz tx iz detalja tx i izaberete željenu novu naknadu koju želite da koristite. Mora biti viša od prethodne i zahteva da imate više sredstava dostupnih u vašem onchain Wallet.


![Image](assets/en/05.webp)


Morate otići na vašu čekajuću tx i kopirati txid outpoint. Zatim dođite u ovaj deo i nalepite ga, zatim izaberite novu naknadu koju želite da koristite za povećanje. Pojaviće se novi ekran sa preporučenim naknadama u tom trenutku, ili možete postaviti prilagođenu. Zapamtite, MORA biti viša od prethodne.


Uvek je bolje držati UTXO sa maksimalnih 100k Sats u vašem Zeus onchain Wallet, kako biste mogli da ga koristite za povećanje naknada kada je to potrebno.



- _Potpiši ili verifikuj_ - Sa ovom funkcijom možete potpisati određenu poruku sa vašim Wallet ključevima. Takođe se može koristiti za verifikaciju poruke kako bi se dokazalo da dolazi od specifičnih Wallet ključeva.
- _Konvertor valuta_ - jednostavan alat za izračunavanje konverzije kursa između BTC i drugih fiat valuta.


**J - Merch i Podrška**


Ovde ćete pronaći više informacija i linkova o Zeusu, online prodavnici, sponzorima, društvenim mrežama.


**K - Pomoć**


U ovom poslednjem odeljku ćete pronaći linkove ka Zeus dokumentacionoj stranici, Github problemima (ako želite da prijavite grešku ili zahtev direktno programerima aplikacije), email podršku.



### KORAK 2 - POČNITE KORISTITI ZEUS NODE



Zapamti, Zeus se uglavnom koristi kao LN Wallet, za jednostavna i brza plaćanja preko LN. Naravno, sadrži i onchain Wallet, ali taj bi se trebao koristiti isključivo za otvaranje/zatvaranje LN kanala, a ne za redovna plaćanja kafe.


Molim vas pročitajte moj drugi vodič o [kako biti sopstvena banka koristeći 3 nivoa Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


U ovom trenutku korisnik ima 2 načina da počne koristiti Zeus:



- Odmah preko LN, koristeći 0-conf kanal sa Olympus LSP
- Prvo deponujte u onchain Wallet, a zatim otvorite normalan LN kanal sa željenim peer-om.


#### Metoda A - Korišćenje Olympus LSP


Ovo je veoma jednostavan i direktan način za uvođenje novog korisnika LN sa Zeusom. To može biti potpuno novi korisnik Bitcoin koji nema nikakav Sats, uveden od strane prijatelja, ili novi trgovac koji počinje sa svojom prvom LN uplatom.


Podrazumevano, Zeus će koristiti svoj sopstveni LSP, Olympus. Ali kasnije možete preći i na druge LSP-ove koji podržavaju ovaj 0-conf protokol za otvaranje kanala.


Jednostavnim kreiranjem Invoice na vašem Zeus-u (unesite iznos i kliknite dugme „request“), moći ćete odmah primiti te Sats.


Invoice koji generate će biti [umotan](https://docs.zeusln.app/lsp/wrapped-invoices) i biće vam predstavljene naknade povezane sa uslugom ako su plaćene. Ovaj umotani Invoice sadrži naznake ruta ka vašem Zeus čvoru, tako da LSP može pronaći vaš novi čvor i otvoriti kanal sa novim sredstvima koja deponujete.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Da biste dobili LN kanal od LSP-a sa sredstvima koja želite da primite prvi put, ovaj Invoice mora biti plaćen sa drugog LN Wallet i sačekajte nekoliko trenutaka dok LSP otvara kanal prema vašem Zeus čvoru, odbija naknadu i prebacuje preostali iznos uplate na vašu stranu kanala.


Sve što treba da uradite je da platite Invoice generisan za vas u ZEUS-u sa još jednim lightning Wallet, i vaš kanal će se otvoriti odmah. [Molimo vas da pogledate Zeus LSP naknade](https://docs.zeusln.app/lsp/fees).


Još jedna prednost plaćanja za kanal je rutiranje bez naknade. To znači da prilikom rutiranja uplata, prvi skok kroz OLYMPUS by ZEUS ne podrazumeva naknade za rutiranje. Imajte na umu da će vam skokovi nakon OLYMPUS by ZEUS i dalje naplaćivati.


Kada je kanal spreman, kliknite na desno dugme na dnu ekrana, koje prikazuje Zeus kanale.


![Image](assets/en/08.webp)


I videćete kanal poput ovog, koji prikazuje vašu stranu bilansa kanala:


![Image](assets/en/09.webp)


Što više budete trošili sa ovog kanala, imaćete više dolazne likvidnosti. Što više Sats budete primali u ovaj kanal, imaćete manje prostora za dolaznu likvidnost.


Evo jednostavne vizuelne demonstracije (autor Rene Pickhardt) o tome kako funkcionišu LN kanali:


U ovom trenutku, razmatrajući demo ekran za kanale, kliknite na ime kanala i videćete više detalja o njemu.


Imate jedan kanal sa Olympusom, ukupnog kapaciteta 490 000 Sats, sa saldom od 378k Sats na vašoj strani i 88k Sats na strani Olympusa. To znači da možete primiti maksimalno još 88k Sats u istom kanalu.


Ako treba da primite više od 88k Sats (dostupna ulazna likvidnost u ovom slučaju), recimo još 500k Sats, jednostavnim kreiranjem novog LN Invoice sa tim iznosom, pokrenuće se zahtev za novi kanal ka Olympus LSP. Tako ćete dobiti 2. kanal.


Zato se preporučuje da se, kako biste izbegli plaćanje većih naknada za otvaranje više kanala, prvi put otvori veći kanal, recimo 1-2M Sats. Kada je otvoren, možete zameniti deo tih Sats na lancu, recimo 50%, koristeći bilo koju eksternu uslugu zamene opisanu u ovom vodiču.


Jednom kada zamenite sa tog kanala recimo 50% i vratite Sats u svoj Zeus onchain Wallet, spremni ste da pređete na sledeći metod otvaranja novog kanala - iz onchain balansa.


#### Metod B - Korišćenje vašeg onchain salda


Ovim metodom možete otvoriti kanale prema bilo kojem drugom LN čvoru, uključujući isti Olympus LSP. Ali ako već imate kanal sa Olympusom, preporučuje se da imate i sa drugim čvorom, radi veće pouzdanosti i takođe možete koristiti MPP (multi-part payment).


![Image](assets/en/10.webp)


Iznad je primer plaćanja LN Invoice koristeći MPP. Kao što možete videti na dnu ekrana imate "podešavanja" i otvara se padajuća stranica sa više detalja o uplati koju ćete izvršiti. Na tom ekranu, ako imate otvorena najmanje 2 kanala, MPP funkcija će biti UKLJUČENA po defaultu. Takođe možete aktivirati AMP (atomski multi-put) i postaviti specifične delove koje želite. Ovo je moćna funkcija!


Za privatni čvor kao što je Zeus, preporučio bih da imate 2-3 dobra kanala (maksimalno 4-5), sa dobrim LSP-ovima i dobrom likvidnošću kako biste pokrili sve vaše potrebe za plaćanje ili primanje Sats preko LN. [Pogledajte više saveta o likvidnosti LN čvorova u ovom vodiču](/nodes/managing-lightning-node-liquidity-en.html). Takođe, ovde je još jedan [opšti vodič o LN likvidnosti](https://Bitcoin.design/guide/how-it-works/liquidity/) od Bitcoin Design tima.


Odabir pravih vršnjaka, znam, nije lak zadatak, čak ni za iskusne korisnike. [Zato ću vam dati neke opcije za početak](https://github.com/ZeusLN/zeus/discussions/2265), ovo su čvorovi vršnjaka koje sam lično testirao koristeći Zeus (pokušao sam da se povežem samo na LND čvorove kako bih izbegao probleme sa nekompatibilnošću)


Evo i lista proverenih čvorova za Zeus. Ako znate dobre, slobodno ih dodajte na tu listu.


Možete otvoriti kanal u Zeus-u tako što ćete otići na prikaz Kanali klikom na ikonu kanala u donjem desnom uglu glavnog prikaza, a zatim pritisnuti ikonu + u gornjem desnom uglu.


![Image](assets/en/11.webp)


Ako želite da otvorite kanal sa određenim čvorom, kliknite na (A) gornji ugao da skenirate QR nodeID čvora (na Mempool, Amboss, 1ML možete dobiti taj QR) i svi detalji o peer-u će biti popunjeni.


PODSETNIK:


- Zeus embedded node do not use Tor service ! So please do not try to open channels with nodes that are under Tor! You are doing more damage to yourself than adding more privacy. Tor for LN it doesn’t offer more privacy but adding more trouble.
- pažljivo birajte svoje vršnjake, bolje da budu dobri LSP-ovi, dobri rutirajući čvorovi, a ne nasumični pleb čvorovi koji bi mogli zatvoriti vaše kanale i ne bi mogli ponuditi dobru likvidnost. [Ovde sam napisao posvećen vodič](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) o likvidnosti i primerima čvorova.


Ako direktno kliknete na dugme „Open Channel to Olympus“ popunićete potrebna polja za otvaranje kanala ka [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Za razliku od plaćenih LSP kanala, vaš kanal će zahtevati On-Chain potvrdu, koristeći vaša onchain sredstva (možete izabrati iz vaših UTXO-a u prikazu otvorenog kanala); neće se otvoriti odmah. Molimo vas da prvo proverite stvarne Mempool naknade i prilagodite ih u skladu s tim, u zavisnosti od toga koliko brzo želite da otvorite taj kanal.


Pre nego što pritisnete dugme za otvaranje kanala, spustite napredne opcije:


![Image](assets/en/12.webp)


Takođe ćete morati da se uverite da je kanal neobjavljen (privatan). Podrazumevano je opcija isključena za objavljene kanale. Ova opcija se ne preporučuje da bude aktivirana za Zeus ugrađeni čvor, korisna je samo kada koristite Zeus sa vašim udaljenim čvorom, kao javni rutirajući čvor.


Za razliku od plaćenih LSP kanala, nećete imati koristi od rutiranja bez naknade otvaranjem kanala ovom metodom.


I gotovo, samo kliknite na dugme „Open Channel“, sačekajte da rudari potvrde tx. Kada je kanal otvoren, možete transaktovati po želji sa Sats iz vaših kanala.


Imajte na umu da će ovi kanali imati sav balans na VAŠOJ strani, tako da nećete imati dolaznu likvidnost. Kao što sam već rekao, zamenite ili potrošite nešto Sats kupujući stvari preko LN kako biste "napravili više prostora" za primanje.


Zamislite svoje LN kanale kao čašu vode. Sipate malo vode (Sats) u praznu čašu (vaš kanal) dok je ne napunite. Ne možete sipati više vode dok ne popijete malo (trošenje / zamena). Kada je čaša skoro prazna, sipajte više vode (Sats) u nju koristeći zamenu. [Pročitajte više o eksternim uslugama zamene ovde](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Postoje i druge LSP usluge kao što je prodaja ulaznih kanala: LNBig ili Bitrefill. Mislim da postoji još ovakvih usluga, ali ih trenutno ne mogu se setiti.


Dakle, ako vam je potreban praktično prazan LN kanal (saldo je 100% na strani peer-a od početka), za primanje više uplata nego što možete da obradite na vašim postojećim popunjenim kanalima, ovo bi mogla biti veoma dobra opcija. Platićete određenu naknadu za otvaranje ovih kanala i dobićete dosta prostora za dolazne transakcije.



## SAVETI I TRIKOVI


### Ograničenja dolaznih rezervi


Trenutno, zbog nekih ograničenja koda LN nije moguće primiti tačno koliko je prikazano u “Inbound”. Uvek imajte na umu da bi trebalo da pravite fakture sa nešto manjim iznosom, odnosno iznosom “Channel Local Reserve”.


![Image](assets/en/13.webp)


Kao što možete videti na gornjoj slici, "inbound" prikazuje da još uvek mogu primiti 5101 Sats, ali u stvari u ovom trenutku je nemoguće primiti više. I možete primetiti da je to ista količina kao "Lokalna rezerva".


Dakle, imajte na umu, kada pravite fakture za primanje, takođe pogledajte likvidnost vaših kanala i oduzmite lokalnu rezervu od tog iznosa, ako želite da maksimalno povećate iznos koji se može primiti.


### Brzi saveti za nove korisnike koji počinju sa Zeus čvorom:



- Iskoristite pravilno svoje nove kanale.


Na primer, ako znate da ćete za nedelju dana primiti recimo 1M Sats, otvorite 2M Sats kanal i zamenite u onchain Wallet ili u drugi (privremeni) kustodijalni LN nalog 50-60% vaše izlazne likvidnosti. Uvek budite spremni sa više likvidnosti. Kada vam bude potrebno više likvidnosti nazad u vašim Zeus kanalima, možete je vratiti iz kustodijalnih naloga.


Ako znaš da ćeš slati recimo 500k Sats/nedeljno, onda otvori kanal od 1M Sats. Na taj način ćeš i dalje imati rezervu dok ga ponovo ne napuniš.



- Ako ste trgovac i uvek ćete primati više nego što redovno trošite, kupite namenski ulazni kanal. To je najjeftiniji način. Plaćate minimalnu naknadu i dobijate "prazan" kanal.



- Ne otvarajte male besmislene kanale od 50-100-300-500k Sats. Napunićete ih za nekoliko dana, čak i ako ih koristite samo za zaps. Otvorite veće i različite, NE samo jedan kanal.


Kada otvorite veći kanal, uvek možete koristiti eksterne podmorske zamene da premestite Sats u vaše onchain novčanike (uključujući povratak na Zeus onchain). Održavanje ravnoteže između ulazne i izlazne likvidnosti je dobro, a takođe možete „ponovo koristiti“ te Sats za otvaranje više kanala ako želite.


### Wrapped Invoice


Ako želite dodati više privatnosti kada primate, možete koristiti metodu “wrapped Invoice”. Podsetnik: da biste to mogli da uradite, potreban vam je kanal sa Olympus LSP. Omotane fakture će “sakriti” konačnu destinaciju (vaš Zeus čvor) i prikazati vaš LSP čvor kao destinaciju platiocu.


Da biste dobili umotani Invoice, idite na glavni ekran tastature, unesite iznos i pritisnite zahtev. Prikazaće se normalan QR kod za vaš Invoice. Sada, kliknite na dugme "X" u gornjem desnom uglu i bićete preusmereni na više opcija za Invoice.


![Image](assets/en/14.webp)


Sada ćete morati da aktivirate tu opciju na vrhu „Enable LSP“ i pritisnete dugme „Create Invoice“. Ta opcija će kreirati umotani Invoice i zapamtite, naplatiće malu naknadu.


### Fakture sa naznakama rute


Ovo je veoma korisna funkcija ako želite da upravljate likvidnošću više dolaznih kanala. Praktično, možete naznačiti na koji dolazni kanal želite da primite Sats sa Invoice.


Ova funkcija se može koristiti i za kružno rebalansiranje, kada želite premestiti likvidnost iz jednog popunjenog kanala u drugi iscrpljeni.


Kako kreirati Invoice sa smernicama za rutu?



- Na glavnom ekranu, prevucite udesno fioku LN i kliknite na "Receive"
- U Invoice podešavanju idite do donjeg dela i aktivirajte dugme "Insert route hints", zatim izaberite karticu "Custom". Otvoriće se ekran sa svim dostupnim kanalima. Izaberite onaj koji želite da primite.
- Popunite sve ostale Invoice detalje, iznos, belešku itd. i kliknite na "kreiraj Invoice".
- Plaćanje tog Invoice će dovesti Sats u naznačeni kanal.


Ako želite da platite sebi taj Invoice (cirkularno balansiranje), kada ga plaćate sa svog istog Zeus čvora, na ekranu za plaćanje, izaberite izlazni kanal (onaj sa više likvidnosti) koji želite da bude korišćen za slanje plaćanja.


### Plati sa Keysend


Keysend je veoma potcenjena funkcija LN i korisnici bi je trebali češće koristiti.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) omogućava korisnicima u Lightning Network da šalju uplate drugima, direktno na njihov javni ključ, sve dok njihov čvor ima javne kanale i ima omogućen keysend. Keysend ne zahteva od primaoca da izda Invoice.


Pa kako to možeš uraditi sa Zeusom?


Jednostavno skenirajte ili kopirajte odredišni nodeID (ili koristite Zeus kontakte da sačuvate vaše redovne odredišne čvorove kao kontakte) i zatim sa glavnog Zeus ekrana, kliknite na dugme „Pošalji“. Na tom ekranu zatim nalepite nodeID ili izaberite iz vaših kontakata.


Stavite iznos Sats, poruku ako je potrebno (da, možete je koristiti i kao tajni chat preko LN) i kliknite na dugme „Pošalji“. Gotovo!


![Image](assets/en/15.webp)


Ako imate direktan kanal sa odredišnim peer-om, neće biti uključenih naknada.


Ako nemate direktan kanal sa odredišnim peer-om, onda će keysend uplata platiti naknade kao normalna LN Invoice uplata, usmerena na regularan put kao i svaka druga uplata. Samo, zapamtite, neće ostati nikakav trag kao LN Invoice.


## Zaključak


Preporučujem da pročitate prateći vodič [Napredna upotreba Zeusa](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) sa dodatnim uputstvima i slučajevima upotrebe.


I... to je to! Od sada jednostavno koristite Zeus Node kao regularni BTC/LN Wallet na svom mobilnom uređaju. Korisnički interfejs je prilično jednostavan i lak za korišćenje, intuitivan za bilo koju vrstu korisnika, mislim da ne moram ulaziti u više detalja o tome kako izvršiti i primati uplate.


U zaključku, ovde je tabela poređenja privatnosti :


![Image](assets/en/16.webp)