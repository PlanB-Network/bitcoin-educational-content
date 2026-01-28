---
name: ArkadeOS
description: Kompletan vodič za Arkade portfolio i Ark protokol
---

![cover](assets/cover.webp)



Mreža Bitcoin suočava se sa velikim izazovom: skalabilnost. Dok glavni sloj (sloj 1) nudi neprevaziđenu sigurnost i decentralizaciju, može obraditi samo ograničen broj transakcija po sekundi. Lightning Network se pojavio kao obećavajuće rešenje drugog sloja (sloj 2), omogućavajući brza plaćanja po niskoj ceni. Međutim, Lightning nameće sopstvena ograničenja: upravljanje kanalima, potrebu za dolaznom likvidnošću i tehničku složenost koja može odvratiti nove korisnike.



Ovo je pozadina za **Ark**, novi layer 2 protokol dizajniran da ponudi pojednostavljeno korisničko iskustvo bez žrtvovanja suvereniteta. **ArkadeOS** (ili Arkade) je prva velika implementacija ovog protokola, nudeći Bitcoin portfolio sledeće generacije.



Ovaj vodič će vas provesti kroz svet Arkade. Istražićemo kako funkcioniše Ark protokol, kako instalirati i konfigurisati Arkade wallet, i kako ga koristiti za slanje i primanje bitkoina trenutno, poverljivo i bez uobičajenih Lightning Network frikcija.



## Razumevanje Ark protokola



Pre nego što se upustite u korišćenje Arkade, neophodno je razumeti ključne pojmove Ark protokola koji ga pokreće. Ark nije zaseban blokčejn, već inteligentan mehanizam koordinacije na vrhu Bitcoin.



### Koncept VTXO


U srcu Arka je **VTXO** (Virtual UTXO). VTXO je UTXO koji još nije objavljen na Bitcoin blokčejnu: postoji van glavnog lanca (off-chain) ali je podržan transakcijama unapred potpisanim na blokčejnu.



Za razliku od stanja na centralizovanoj berzi, VTXO zaista pripada vama. Vi posedujete kriptografski dokaz koji vam omogućava da u bilo kom trenutku zatražite odgovarajuće stvarne bitkoine na blokčejnu, čak i ako Ark server nestane. VTXO-i vam omogućavaju da trenutno prenesete vrednost između korisnika bez čekanja na potvrde blokova.



### Uloga ASP-a (Ark Service Provider)


Protokol Ark radi na modelu klijent-server. Server se zove **ASP** (Ark Service Provider). ASP igra ulogu dirigenta:




- Pruža neophodnu likvidnost za mrežu.
- Koordinira transakcije između korisnika.
- Organizuje "runde" poravnanja na blockchainu.



Važno je napomenuti da je ASP **ne-kustodijalan**. Nikada ne drži vaše privatne ključeve, niti može ukrasti vaša sredstva. Njegova uloga je isključivo tehnička i logistička. Ako ASP cenzuriše vaše transakcije ili prestane sa radom, uvek možete povratiti svoja sredstva putem jednostranog izlaznog postupka.



### Runde i privatnost


Transakcije na Arku se finalizuju u grupama koje se zovu **Runde**. Periodično (npr. svakih nekoliko sekundi), ASP prikuplja sve čekajuće transakcije i sidri ih na Bitcoin blokčejn u jednoj optimizovanoj transakciji.


Ovaj mehanizam nudi dve glavne prednosti:




- Skalabilnost**: Jedna on-chain transakcija može validirati hiljade off-chain uplata, drastično smanjujući troškove za korisnike.
- Poverljivost**: Svaka runda deluje kao **CoinJoin**. Sredstva svih učesnika se mešaju u zajednički fond pre nego što se ponovo raspodele u obliku novih VTXO-a. Ovo prekida vezu između pošiljaoca i primaoca, čineći izuzetno teškim, ako ne i nemogućim, za spoljnog posmatrača da prati uplate.



## Prezentacija ArkadeOS-a



ArkadeOS je konkretna aplikacija koja čini Ark protokol dostupnim široj javnosti. Razvijen od strane Ark Labs, to je kompletan ekosistem koji obuhvata portfelj (Wallet), server (Operator) i alate za razvoj.



Za krajnjeg korisnika, Arkade ima oblik elegantne, intuitivne web wallet (PWA - Progressive Web App). Ona skriva kriptografsku složenost VTXO-a i rundi iza poznatog interfejsa. Sa Arkade, imate adresu za primanje, dugme za slanje i istoriju transakcija, baš kao klasični wallet, ali sa snagom Arkove trenutnosti i poverljivosti.



## Instalacija i konfiguracija



Kako je Arkade progresivna veb aplikacija, posebno je lako instalirati je i ne uključuje nužno tradicionalne prodavnice aplikacija.



### Pristup i instalacija


Arkade možete pristupiti direktno iz bilo kog modernog web pregledača (Chrome, Safari, Brave) na računaru ili mobilnom uređaju.





- Posetite zvaničnu veb stranicu aplikacije: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Dočekaće vas niz uvodnih ekrana koji vas upoznaju sa ključnim konceptima Arkade: novi ekosistem za Bitcoin, važnost samostalnog čuvanja i prednosti grupnih transakcija.



![arkade onboarding](assets/fr/02.webp)





- Na Androidu (Chrome/Brave)** : Pritisnite meni pretraživača (tri tačke) i izaberite "Instaliraj aplikaciju" ili "Dodaj na početni ekran".
- Na iOS-u (Safari)**: Pritisnite dugme za deljenje (kvadrat sa strelicom nagore) i izaberite "Na početni ekran".



Jednom instaliran, Arkade se pokreće kao izvorna aplikacija, preko celog ekrana i bez adresne trake.



### Kreiranje portfolija


Prilikom prvog pokretanja, od vas će biti zatraženo da konfigurišete svoj portfolio.





- Kliknite na **"Create New Wallet"**.



![create wallet](assets/fr/03.webp)





- wallet se kreira trenutno. Za razliku od tradicionalnih Bitcoin novčanika, **Arkade ne koristi frazu za oporavak od 12 ili 24 reči**. Umesto toga, Arkade automatski generiše **privatni ključ** u Nostr (nsec) formatu, koji će se koristiti za bekap i vraćanje vašeg wallet. Zapamtite da odmah sačuvate ovaj ključ (pogledajte sledeći odeljak).





- Videćete ekran "Vaš novi wallet je aktivan!", što potvrđuje da je vaš wallet spreman za korišćenje. Kliknite na **"IDI NA NOVČANIK"** da pristupite glavnom interfejsu.



Jednom kada ste u vašem wallet, bićete prebačeni na Arkade-ov glavni interfejs. Ovde ćete pronaći vaš saldo, dugmad za slanje i primanje sredstava, i karticu "Aplikacije" koja omogućava pristup integrisanim aplikacijama kao što su Boltz (Lightning razmena), LendaSat i LendaSwap (usluge pozajmljivanja), i Fuji Money (sintetička sredstva).



![wallet interface](assets/fr/04.webp)



### Veza sa ASP


Podrazumevano, portfolio je automatski konfigurisan da se poveže sa zvaničnim Arkade Labs ASP. Možete proveriti na koji server ste povezani tako što ćete otići na **Settings** > **About** gde ćete videti adresu servera (trenutno `https://arkade.computer`).



U trenutnoj verziji Arkade (Beta), nije moguće ručno modifikovati ASP server. Aplikacija se automatski povezuje na zvanični Arkade Labs ASP. U budućnosti, korisnici će možda moći da biraju između različitih ASP-ova prema svojim preferencijama, ali ova funkcija još uvek nije dostupna.



### Pravljenje rezervne kopije vašeg privatnog ključa


**Arkade koristi privatni ključ u Nostr (nsec) formatu kao metodu za rezervnu kopiju i oporavak. Da biste napravili rezervnu kopiju svog privatnog ključa :





- Idite na **Podešavanja** sa glavnog ekrana.
- Odaberite **"Backup and privacy "**.
- Videćete vaš **privatni ključ** prikazan u formatu `nsec...`. Ovaj dugačak niz karaktera je vaše jedino sredstvo za vraćanje vašeg wallet.
- Pritisnite **"COPY NSEC TO CLIPBOARD "** da kopirate vaš privatni ključ.
- Čuvajte ovaj ključ na sigurnom mestu**: zapišite ga na papir, sačuvajte u sigurnom menadžeru lozinki ili koristite bilo koji drugi metod bekapa koji vam odgovara.
- Arkade takođe nudi opciju **"Omogući Nostr rezervne kopije"**. Ova funkcija koristi Nostr protokol (decentralizovana mreža) za automatsko pravljenje rezervnih kopija određenih podataka sa vašeg wallet u šifrovanom obliku na Nostr releje. Ovo olakšava sinhronizaciju između više uređaja i nudi jednostavniji oporavak statusa vašeg wallet.



**Važno**: Nostr rezervne kopije su samo funkcija za **udobnost**. One ne zamenjuju rezervnu kopiju vašeg nsec ključa. Nostr releji ne garantuju trajno skladištenje podataka. Vaš nsec privatni ključ ostaje vaše jedino garantovano sredstvo za povratak vaših sredstava.



![backup private key](assets/fr/05.webp)




## Korišćenje Arkade



Jednom kada postavite svoj wallet, spremni ste da istražite mogućnosti Arkade-a. Interfejs je dizajniran da besprekorno ujedini različite tipove Bitcoin plaćanja (On-chain, Lightning, Ark).



### Primanje sredstava



Da biste finansirali svoj portfolio, pritisnite **"Receive "**. Arkade nudi tri metode prijema:





- Plaćanje Ark**: Ako pošiljalac takođe koristi Arkade, podelite svoju Ark adresu za trenutni, poverljivi i gotovo besplatni transfer.
- On-chain deposit (Boarding)**: Use the Bitcoin address (`bc1p...`) to receive from a classic wallet or an exchange. Allow for confirmation (~10 min) before funds are converted into VTXOs.
- Lightning swap**: Generiši Lightning fakturu i plati je sa eksternog wallet Lightning. Sredstva stižu trenutno putem automatskog zamene.



![receive amount](assets/fr/06.webp)



Ekran za prijem prikazuje sve dostupne opcije: QR kod, Ark adresa, Bitcoin (BIP21) adresa i Lightning faktura. Za Lightning uplate, držite aplikaciju otvorenom tokom transakcije.



![receive confirmation](assets/fr/07.webp)



### Slanje sredstava



Da biste poslali sredstva, pritisnite **"Pošalji "** i nalepite adresu primaoca ili skenirajte QR kod. Arkade automatski detektuje vrstu potrebnog plaćanja:





- Ark** plaćanje: Na Ark adresu, transfer je trenutan, privatan i praktično besplatan (0 SATS naknada). Primalac ne mora biti online.
- Lightning** plaćanje: Skenirajte Lightning fakturu (`lnbc...`) i Arkade automatski izvršava zamenu. ASP plaća fakturu za vas i zadužuje vaš Arkade saldo.
- On-chain payment**: Towards a classic Bitcoin address (`bc1q...` or `bc1p...`), Arkade initiates a "Collaborative Output" which will be included in the next on-chain round.



Proverite detalje na ekranu "Potpiši transakciju", zatim potvrdite sa **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Trenutno ograničenje (Beta)**: VTXO-ovi kreirani pre manje od 24 sata ne mogu se koristiti za on-chain izlaze. Ako naiđete na grešku, molimo sačekajte dok vaši VTXO-ovi ne "sazru".



**on-chain izlazna poverljivost**: Primer ispod prikazuje [Ark izlaznu transakciju na mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Primećujemo raspodeljeni ulaz na 4 različita izlaza, slično kao kod CoinJoin. Za spoljnog posmatrača, nemoguće je odrediti koji iznos pripada kojem korisniku.



![transaction ark mempool](assets/fr/11.webp)



## Napredne funkcije



### upravljanje istekom VTXO


Tehnička karakteristika Ark protokola je da VTXO-i imaju **ograničen vek trajanja**. Ovo vremensko ograničenje je inherentno dizajnu protokola. Vreme isteka je podesivo od strane svakog ASP servera; na zvaničnom Arkade Labs ASP-u, ovaj period je oko **4 nedelje (≈30 dana)**.



**Ovo ograničenje omogućava Ark serveru da efikasno upravlja likvidnošću i očisti VTXO-e od neaktivnih korisnika. Nakon isteka, Ark server tehnički može preuzeti preostala sredstva u VTXO stablu.



**Da biste održali svoje VTXO-ove aktivnim, potrebno ih je "osvežiti" pre nego što isteknu. Osvežavanje se sastoji od učešća u novoj "rundi" gde se vaši VTXO-ovi blizu isteka zamenjuju za nove VTXO-ove sa novim punim periodom važenja (≈30 dana na Arkade Labs ASP).



Arkade portfolio automatski upravlja ovim procesom: aplikacija konstantno prati status vaših VTXO-a i automatski ih osvežava nekoliko dana pre nego što isteknu. Sve dok redovno otvarate svoju aplikaciju (barem jednom nedeljno), vaši VTXO-i će automatski ostati aktivni.



**Ako ne otvorite svoj portfolio duže od 4 nedelje, vaši VTXO-i će isteći. Međutim, ne gubite svoja sredstva: zadržavate opciju njihovog povraćaja putem **jednostranog izlaza** (pogledajte sledeći odeljak). Ovaj postupak je skuplji i sporiji, ali osigurava da vaša sredstva ostanu povratljiva.



Potreba za redovnim otvaranjem aplikacije čini Arkade **"Hot Wallet"** dizajniranim za svakodnevnu potrošnju, a ne kao sef za dugoročne uštede. Za čuvanje bitkoina bez korišćenja tokom dužih perioda, preferirajte hladni wallet hardver.



**Proverite status svojih VTXO-ova**: Možete pratiti status svojih VTXO-ova u **Podešavanja** > **Napredno**. Pogledajte "Sledeće Obnavljanje" da vidite kada će se desiti sledeće automatsko obnavljanje, i "Virtuelni Novčići" da vidite detaljnu listu svih vaših VTXO-ova sa datumom isteka.



![vtxo management](assets/fr/09.webp)



### Jednostrani Izlaz (Unilateral Exit)



Jednostrani izlaz je **osnovna kriptografska garancija** Ark protokola koja osigurava da dobijete svoja sredstva nazad, čak i ako ASP nestane, cenzuriše vaše transakcije ili odbije saradnju. Tehnički, vaši VTXO-i su **pre-potpisane Bitcoin transakcije** koje posedujete. U apsolutnoj hitnosti, možete emitovati ove transakcije na Bitcoin blokčejnu kako biste povratili svoja sredstva bez ičijeg odobrenja.



**Kako to funkcioniše? Proces se odvija u dve faze. Prvo, **Razmotavanje**: sekvencijalno emitujete unapred potpisane transakcije koje čine vaše VTXO-e u stablu transakcija. Zatim **Finalizacija**: kada vremenska zaključavanja isteknu (obično 24 sata), preuzimate svoje bitkoine sa standardne adrese.**



**Trenutni status u Arkade**: U Beta verziji još uvek ne postoji dugme ili jednostavan korisnički interfejs za jednostrani izlaz. Ova funkcionalnost trenutno zahteva korišćenje Arkade SDK-a i tehničko znanje TypeScript programiranja.



**Even if the procedure isn't accessible at the touch of a button, the cryptographic guarantee is there. Your VTXOs contain pre-signed transactions that legitimately belong to you. It's this technical guarantee that makes Ark a **non-custodial** protocol: even in the worst-case scenario, your funds remain technically recoverable. A simplified interface will probably be added in future versions of Arkade.



## Prednosti i ograničenja



Da bismo Arkade postavili u pravi kontekst, hajde da rezimiramo njegove trenutne snage i slabosti.



### Istaknuto




- Korisničko iskustvo (UX)**: Nema upravljanja kanalima, dolaznog kapaciteta ili složenih rezervnih kopija kanala kao kod Lightning-a. Samo instalirajte i koristite.
- Privatnost** : Podrazumevana arhitektura CoinJoin nudi mnogo viši nivo anonimnosti nego standardne on-chain ili Lightning transakcije.
- Interoperabilnost**: Platite bilo koji Bitcoin QR kod (On-chain ili Lightning) sa jednog interfejsa.



### Ograničenja




- Young protocol**: Ark je veoma nova tehnologija. Mogu postojati greške. Preporučljivo je ne koristiti Ark za čuvanje iznosa čiji bi gubitak bio kritičan.
- ASP zavisnost**: Iako nije skrbnički, sistem se oslanja na dostupnost ASP-a za fluidnost. Ako je ASP van mreže, više ne možete obavljati transakcije trenutno (samo povući svoja on-chain sredstva).
- Hot Wallet only** : Potreba za redovnim otvaranjem aplikacije radi osvežavanja VTXO-a nije pogodna za hladno skladištenje (Cold Storage).



## Poređenje: Arkade vs Lightning vs Cashu



Da bismo bolje razumeli pozicioniranje Arkade-a, hajde da ga uporedimo sa druga dva glavna rešenja za skalabilnost.




| Kriterijum | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Model** | Zajednički UTXO koordinisan od strane servera (ASP) | P2P mreža platnih kanala | Slepi tokeni izdati od strane banke (Mint) |
| **Starateljstvo** | **Nesitodijalno** (vi imate ključeve) | **Nesitodijalno** (vi imate ključeve) | **Kustodijalno** (Mint drži sredstva) |
| **Privatnost** | **Visoka** (izvorni CoinJoin, slepo za javnost) | **Srednja** (Onion rutiranje, ali kanali vidljivi) | **Veoma Visoka** (slepo čak i za Mint) |
| **Skalabilnost** | Odlična (masovni batching on-chain) | Odlična (beskonačne transakcije off-chain) | Odlična (jednostavni potpisi servera) |
| **Iskustvo** | Jednostavno (blizu on-chain novčanika) | Kompleksno (upravljanje kanalima, likvidnost) | Veoma jednostavno (kao digitalni keš) |
| **Glavni rizik** | Dostupnost ASP-a i isteknuće | Upravljanje kanalima i rezervne kopije | Poverenje u Mint (rizik od krađe) |

**Arkade** je idealan kompromis: jednostavnost i poverljivost Cashu-a, ali sa suverenitetom (bez starateljstva) Lightning-a.



## Podrška i pomoć



Ako naiđete na bilo kakve probleme ili imate pitanja dok koristite Arkade, aplikacija nudi nekoliko opcija podrške:





- Idite na **Settings** > **Support**.
- Naći ćete nekoliko opcija:
  - Korisnička podrška**: Dobijte pomoć sa svojim portfoliom, prijavite greške ili postavite pitanja.
  - Secure Chat**: Vaši razgovori su sigurni i privatni, sa istorijom koja se čuva između sesija.
  - Izveštaji o greškama**: Prijavite sve probleme na koje naiđete, uključujući korake za njihovo reprodukovanje.
  - Pratite Napredak**: Uvek pratite svoje tikete podrške i razgovore.



![support](assets/fr/10.webp)



Tim Arkade je takođe aktivan na Telegramu putem kanala @arkade_os za podršku i mogućnosti integracije.



## Važna napomena: Aplikacija u Beta verziji



**⚠️ Arkade je trenutno u javnoj beta verziji na mainnet Bitcoin**. Iako je aplikacija funkcionalna sa pravim bitkoinima, važno je preduzeti određene mere predostrožnosti.



### Preporuke za upotrebu




- Koristite male iznose**: Izbegavajte čuvanje velikih suma na Arkade. Koristite ovaj wallet za vaše svakodnevne troškove i čuvajte vašu ušteđevinu na hladnom wallet hardveru.
- Mogući bagovi i ograničenja**: Kao i kod svake aplikacije koja je u aktivnom razvoju, Arkade može pokazivati bagove ili neočekivano ponašanje. Prijavite sve probleme putem integrisane podrške.
- Brza evolucija** : Aplikacija i protokol se konstantno unapređuju. Neke funkcije mogu biti promenjene ili dodate u budućim verzijama.



### Trenutna poznata ograničenja




- 24-časovno kašnjenje na VTXOs** : Novo kreirani VTXOs ne mogu se odmah koristiti za on-chain izlaze.
- ASP jedinstven**: Još uvek nije moguće promeniti ASP server u aplikaciji.
- Tehnički jednostrani izlaz**: Još nema pojednostavljenog interfejsa za jednostrani izlaz (zahteva SDK).



Tim Arkade Labs aktivno radi na ublažavanju ovih ograničenja u budućim verzijama.



## Zaključak



ArkadeOS predstavlja značajan proboj u ekosistemu Bitcoin. Implementacijom Ark protokola, dokazuje da je moguće pomiriti jednostavnost korišćenja sa fundamentalnim principima Bitcoin: ne veruj, proveri.



Iako je još uvek u povoju, Arkade nudi fascinantan uvid u to kako bi budućnost Bitcoin plaćanja mogla izgledati: trenutna, privatna i dostupna svima bez tehničkih preduslova. To je savršen alat za vaše dnevne troškove, dopunjujući vaše sigurno rešenje za štednju (Cold Wallet).



Podstičemo vas da testirate Arkade sa malim iznosima kako biste sami otkrili ovaj novi protokol. Ekosistem se brzo razvija, a Arkade je na čelu ove inovacije.



## Resursi



Da biste saznali više, konsultujte zvanične resurse:





- Arkade** website: [arkadeos.com](https://arkadeos.com)
- Dokumentacija**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark** protokol: [ark-protocol.org](https://ark-protocol.org)
- Izvorni Kod** : [GitHub Arkade](https://github.com/arkade-os)