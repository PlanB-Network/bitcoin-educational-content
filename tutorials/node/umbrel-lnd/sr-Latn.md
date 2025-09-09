---
name: Umbrel LND
description: Napredni vodič za instalaciju i konfiguraciju Lightning Network Daemon (LND) na Umbrel-u
---
![cover](assets/cover.webp)




## Uvod



Ovaj napredni vodič vas vodi korak-po-korak kroz instalaciju, konfiguraciju i korišćenje aplikacije Lightning Node (LND) na vašem Umbrel čvoru. Naučićete kako da otvorite kanale, upravljate svojom likvidnošću i sinhronizujete svoj čvor sa mobilnom aplikacijom.



## 1. Preduslov: funkcionalan Bitcoin Umbrel čvor



Pre nego što implementirate Lightning, potrebno je da imate potpuno operativan Bitcoin čvor na Umbrel-u. Ovo uključuje instalaciju Umbrel-a (na Raspberry Pi, NAS ili drugoj mašini) i potpunu sinhronizaciju Bitcoin Blockchain-a .



Da biste instalirali Umbrel i konfigurisali svoj Bitcoin čvor, preporučujemo da pratite naš posvećeni vodič :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Proverite da je vaš Bitcoin čvor ažuriran i ispravno radi, jer Lightning Network zavisi od njega za sve off-chain transakcije.



## 2. Uvod u Lightning mrežu



Lightning mreža je protokol drugog sloja, osmišljen da ubrza i smanji troškove Bitcoin transakcija tako što ih obavlja van glavnog blokčejna.



U konkretnim terminima, Lightning koristi mrežu platnih kanala između čvorova: dva korisnika otvaraju kanal blokiranjem on-chain BTC-a (inicijalna transakcija), zatim mogu trenutno razmenjivati plaćanja unutar ovog kanala. Ove off-chain transakcije nisu zabeležene na Blockchain-u, otuda njihova brzina i praktično nulti trošak.



Plaćanja se mogu usmeravati kroz više kanala (zahvaljujući posredničkim čvorovima) kako bi stigla do bilo kog primaoca na mreži, omogućavajući gotovo neograničen broj trenutnih transakcija. Lightning tako nudi veoma brze, niskotarifne transakcije, idealne za svakodnevna plaćanja ili mikro-transakcije, dok smanjuje opterećenje na Bitcoin Blockchain-u.



Da bi radio, Lightning čvor mora biti stalno povezan na mrežu i komunicirati sa drugim Lightning čvorovima. Postoje razne softverske implementacije (LND, Core Lightning, Eclair, itd.), koje su sve međusobno kompatibilne. Umbrel koristi LND (Lightning Network Daemon) kao deo svoje zvanične Lightning Node aplikacije. Ovaj vodič se fokusira na LND.



Za potpuni teorijski uvod u Lightning mrežu, preporučujemo da pohađate naš posvećeni kurs :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Ovaj kurs će vam pružiti temeljno razumevanje osnovnih pojmova Lightning mreže, a zatim će vas voditi ka praktičnom radu sa vašim LND čvorom.



## 3. Zašto samostalno hostovati LND?



Rukovanje sopstvenim Lightning čvorom (LND) na Umbrel-u vam daje potpunu suverenost nad vašim sredstvima i kanalima, u poređenju sa čuvanjem sredstava kod treće strane ili polu-povereničkim rešenjima.



### Poređenje Lightning rešenja :



**Rešenja za čuvanje (npr: Wallet of Satoshi)**:




- Vaši Lightning bitcoini su upravljani od strane pouzdane treće strane
- Lako za korišćenje, bez tehničke složenosti
- Operater drži vaša sredstva i može pratiti vaše transakcije
- Žrtvujete kontrolu i poverljivost



**Prilagođeni novčanici  (npr. Phoenix, Breez)** :




- Korisnici zadržavaju svoje privatne ključeve i time vlasništvo nad svojim BTC-om
- Nema potpunog upravljanja čvorovima - aplikacija upravlja kanalima u pozadini
- Kompromis između jednostavnosti i suvereniteta
- Zavisnost od infrastrukture dobavljača za likvidnost
- Tehnička ograničenja (jedan pametni telefon ne može usmeravati plaćanja za druge)



**Samostalno hostovan LND čvor (Umbrel)** :




- Maksimalni suverenitet: vaši On-Chain i off-chain BTC-ovi su potpuno pod vašom kontrolom
- Nema trećih strana uključenih u otvaranje kanala ili upravljanje vašim plaćanjima
- Povećana poverljivost (vaši kanali i transakcije su poznati samo vama i vašim direktnim saradnicima)
- Sloboda korišćenja: povežite se sa sopstvenim uslugama i novčanicima
- Mogućnost usmeravanja transakcija za druge (naknada u vidu mikro-naknade)
- Povećane tehničke odgovornosti (održavanje, upravljanje likvidnošću, sigurnosne kopije)



Ukratko, samostalno hostovanje LND vam daje maksimalnu kontrolu, ali zahteva više tehničkih veština. To je kompromis između pogodnosti i suvereniteta.



## 4. Uputstvo korak po korak



### 4.1 Instaliranje i konfiguracija aplikacije Lightning Node na Umbrel



Jednom kada se vaš Umbrel čvor (Bitcoin) sinhronizuje, pratite ove korake :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Preuzmite i instalirajte aplikaciju Lightning čvora preko „App Store“ dela Umbrel interfejsa.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) će biti implementiran na vašem Umbrel-u kao aplikacija. Kada je prvi put otvorite, videćete poruku upozorenja koja vas informiše da je Lightning eksperimentalna tehnologija.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Možete birati između kreiranja novog čvora ili obnavljanja jednog iz sigurnosne kopije/seed. Za prvu instalaciju, izaberite kreiranje novog čvora. Aplikacija Lightning Node će generisati Mnemonic frazu sa 24 reči (vaš Lightning seed): zapišite je vrlo pažljivo (idealno offline, na papiru), jer će biti korišćena za obnavljanje vaših Lightning sredstava ako bude potrebno.



**Napomena: Kod novijih verzija Umbrela, prilikom instalacije Lightning aplikacije dobija se seed od 24 reči (dok sam Bitcoin Umbrel čvor to ne obezbeđuje).



![Interface principale de Lightning Node](assets/fr/04.webp)



Nakon inicijalizacije, pristupićeš glavnom interfejsu Lightning Node-a.



![Paramètres de l'application](assets/fr/05.webp)



U postavkama aplikacije pronaći ćete niz važnih opcija:




   - Konsultujte svoj ID čvora (jedinstveni identifikator vašeg čvora)
   - Povezivanje spoljnog novčanika (Connect Wallet)
   - Prikaži tajne reči
   - Pristupite naprednim postavkama
   - Oporavi kanale
   - Preuzmi rezervnu kopiju datoteke kanala
   - Omogući automatske rezervne kopije
   - Konfigurišite rezervnu kopiju putem Tor-a (Backup over Tor)



Ove opcije su ključne za sigurnost i upravljanje vašim Lightning čvorom. Obavezno aktivirajte automatske rezervne kopije i čuvajte vaše tajne reči na sigurnom.



**Korisni resursi:**




- [Umbrel Community](https://community.umbrel.com) - Forum za diskusiju gde korisnici mogu deliti probleme i rešenja u vezi sa Umbrelom i njegovim ekosistemom


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Opis funkcija aplikacije Lightning Node na Umbrel-u
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Zvanična LND dokumentacija

### 4.2 Otvaranje Lightning kanala



Kada LND bude pokrenut, možete otvoriti svoj prvi Lightning kanal. Da biste pronašli kvalitetne čvorove za povezivanje:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) je istraživač za pronalaženje pouzdanih čvorova za otvaranje kanala.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Na primer, [ACINQ čvor](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) je prepoznat čvor sa odličnim statistikama dostupnosti i likvidnosti.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Za ovaj vodič, otvorićemo kanal sa [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Informacije potrebne za povezivanje (pubkey@ip:port) su date na njihovoj Amboss stranici.



Da biste otvorili kanal :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Na početnoj stranici Lightning Node-a, kliknite na dugme "+ OPEN CHANNEL"



![Configuration du canal](assets/fr/10.webp)



Na stranici za konfiguraciju kanala:




   - Nalepite ID čvora kopiran iz Amboss-a (format: pubkey@ip:port)
   - Definiši količinu kapaciteta kanala (neki čvorovi kao što je ACINQ imaju minimume, npr. 400k Sats)
   - Prilagodite naknade za otvaranje transakcija ako je potrebno



![Canal en cours d'ouverture](assets/fr/11.webp)



Nakon što je transakcija poslata, kanal će se na početnoj stranici prikazati kao „u procesu otvaranja“ (eng. opening). Sačekajte potvrdu On-Chain transakcije.



![Détails du canal](assets/fr/12.webp)



Kliknite na kanal da biste videli njegove detalje:




   - Trenutni status
   - Ukupni kapacitet
   - Raspodela likvidnosti (prilivi/odlivi)
   - Javni ključ udaljenog čvora
   - I druge tehničke informacije



### Korišćenje Lightning Network+ za dobijanje dolazne likvidnosti



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ je dostupan u Umbrel App Store-u kako bi olakšao primanje novca.



![Interface principale de LN+](assets/fr/14.webp)



Glavni interfejs nudi tri važne opcije:




- "Likvidnosne zamene" (eng. Liquidity swaps): istražite dostupne ponude zamene
- "Open For Me": filtriraj zamene za koje ispunjavaš uslove
- "To Docs": pristup dokumentaciji



![Message d'erreur LN+](assets/fr/15.webp)



Napomena: Ako još nemate otvoren kanal, videćete ovu poruku o grešci kada kliknete na "Open for me".



![Liste des swaps disponibles](assets/fr/16.webp)



Stranica "Liquidity Swaps" prikazuje sve dostupne ponude zamena na mreži.



![Swaps éligibles](assets/fr/17.webp)



"Open For Me" filtrira samo one zamene za koje vaš čvor ispunjava potrebne uslove.



![Détails d'un swap](assets/fr/18.webp)



Primer detalja zamene:




- Pentagon konfiguracija (5 učesnika)
- Kapacitet od 300k Sats po kanalu
- Preduslov: minimum 10 otvorenih kanala sa ukupnim kapacitetom od 1M Sats
- Dostupna mesta: 4/5



### 4.3 Sinhronizacija sa mobilnom aplikacijom (Zeus)



Da biste daljinski kontrolisali vaš Lightning čvor (pametni telefon), možete koristiti Zeus (aplikacija otvorenog koda dostupna na iOS/Android).



**Konfiguracija Zeusa za Umbrel:**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Uverite se da je vaš Umbrel čvor dostupan (podrazumevano putem Tor-a).


U Umbrelu interfejsu, otvorite aplikaciju Lightning Node, zatim kliknite na dugme "Connect Wallet" kako je naznačeno strelicom.



![Page de connexion avec QR code](assets/fr/20.webp)



Pojavljuje se QR kod koji sadrži vaše LND pristupne podatke u lndconnect formatu. Ovaj QR kod je posebno gust sa informacijama, pa ga slobodno uvećajte radi lakšeg čitanja.



![Configuration initiale de Zeus](assets/fr/21.webp)



Na vašem telefonu :




   - Otvorite Zeus
   - Na početnoj stranici kliknite na "Advanced setup" da povežete svoj Lightning čvor.
   - U parametrima, izaberite "Create or connect a Wallet" ili u prevodu "Kreiraj ili poveži novčanik"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



U Zeusu:




   - Izaberite "LND (REST)" kao tip konekcije
   - Možete ili skenirati QR kod (preporučeni metod) ili uneti informacije ručno. (Ne ustručavajte se da zumirate Umbrel QR kod, jer je veoma gust)
   - Važno: aktivirajte opciju "Use Tor" ako je vaš Umbrel dostupan samo putem Tor-a (podrazumevano)
   - Sačuvaj konfiguraciju



Vaš Zeus je sada povezan sa vašim Umbrel čvorom i omogućava vam da vršite Lightning uplate, pregledate vaše kanale, stanja, itd., dok ostajete potpuno samostalni.



**Napredne opcije povezivanja:**



Podrazumevano, veza Zeus ↔ Umbrel je putem Tor-a. Za bržu vezu, postoje dve alternative:



**Lightning Node Connect (LNC)**:




   - Mehanizam šifrovane veze Lightning Labs
   - Instalirajte aplikaciju Lightning Terminal na Umbrel (uključuje pristup LNC-u)
   - generišite QR kod za povezivanje u Lightning Terminalu (Connect → Connect Zeus via LNC)
   - Skeniraj to u Zeus aplikaciji (izaberi "LNC" kao tip konekcije)



**VPN Tailscale**:




   - Lako konfigurisani mesh VPN
   - Instalirajte Tailscale na Umbrel (App Store) i na vašem mobilnom telefonu
   - Poveži Zeusa putem Tailscale privatne IP adrese umesto Tor Address



Ove opcije nisu obavezne, a Tor + Zeus rešenje dobro funkcioniše u većini slučajeva.



> **Korisni resursi:**
> - [Zeus Dokumentacija - Umbrel Povezivanje](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Zvanični vodič za povezivanje Zeusa sa Umbrelom
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus open-source projekat
> - [Umbrel Zajednica - Povezivanje Zeusa putem Tailscale-a](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Vodič za povezivanje Zeusa sa Umbrelom koristeći Tailscale

## 5. Bezbednost i najbolje prakse



Upravljanje samostalno hostovanim Lightning čvorom zahteva posebnu pažnju prema bezbednosti.



### Rezervna kopija i sigurnost za vaš čvor



**Osnovne vrste rezervnih kopija**



Vašem Lightning Umbrel čvoru su potrebne dve vrste rezervnih kopija:



**Seed fraza (24 reči)**




- Obnavlja On-Chain sredstva
- Neophodna za ponovno kreiranje vašeg Lightning novčanika
- Za ultra-sigurno skladištenje (offline, na papiru)



**Fajl statičnog bekapa kanala (SCB)** 




- Sadrži informacije o Lightning kanalu
- Omogućava prisilno zatvaranje kanala u slučaju pada sistema
- **Važno:** Nikada ručno ne čuvajte datoteku `channel.db` (rizik od kaznenih penala)



**Ručna procedura za pravljenje rezervne kopije**



Da biste ručno sačuvali svoje kanale :


1. Pristupite meniju Lightning Node (tri tačke "⋮" pored "+ Open Channel")


2. Preuzmi rezervnu kopiju kanala


3. Izvezite novi SCB nakon svake izmene kanala


4. Bezbedno skladištite SCB (šifrovani mediji, kopija van lokacije)



**Umbrel** automatski sistem za pravljenje rezervnih kopija



Umbrel ima sofisticirani automatski sistem za pravljenje rezervnih kopija koji osigurava :



*Zaštitu podataka:*




- Šifrovanje na strani klijenta pre prenosa
- Slanje putem Tor mreže
- Podaci dopunjeni nasumičnim popunjavanjem
- Jedinstven ključ za šifrovanje za vaš uređaj



*Poboljšana sigurnost:*




- Trenutne sigurnosne kopije pri promenama statusa
- "Lažni" rezervni podaci u nasumičnim intervalima
- Sakrij promene veličine rezervne kopije
- Zaštita protiv vremenske analize



*Proces restauracije:*




- Identifikator i ključ izvedeni iz vašeg Umbrel seed-a
- Potpuna restauracija moguća samo sa Mnemonic frazom 
- Automatski oporavak najnovijih rezervnih kopija
- Vratite postavke kanala i podatke



### Obnova nakon pada



Ako je vaš čvor izgubljen (kvar hardvera, oštećena SD kartica) :




- Ponovo instaliraj Umbrel
- Unesite vašs seed od 24-reči u Lightning aplikaciju 
- Uvezite SCB datoteku tokom restauracije



LND će kontaktirati svakog partnera vaših starih kanala kako bi ih zatvorio i povratio vaš deo On-Chain sredstava. Kanali će biti trajno zatvoreni (da bi se ponovo otvorili ako bude potrebno).



### Dostupnost i zaštita od prevara



Idealno, ostavite svoj čvor online što je češće moguće. U slučaju dužeg odsustva:




- Zlonamerni čvor mogao bi pokušati emitovati staro stanje kanala
- Lightning omogućava „period žalbe“ (oko 2 nedelje na LND-u).
- Ako ćete biti odsutni duže vreme, postavite Watchtower



**Watchtower konfiguracija:**




- U naprednim LND postavkama, dodajte URL pouzdanog Watchtower servera
- Možete koristiti javnu uslugu ili instalirati svoj vlastiti Watchtower




Da biste saznali više o konfigurisanju i korišćenju osmatračnica, preporučujemo da pogledate naš posvećeni vodič :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Druge najbolje prakse





- **Ažuriranja softvera:** Održavajte Umbrel i LND ažurnim (bezbednosne ispravke)
- **Zaštita hardvera:** Koristite stabilan sistem (Raspberry Pi sa SSD-om, mini-PC) i UPS
- **Mreža sigurnost:** Zadrži podrazumevanu Tor konfiguraciju, promeni Umbrel administratorsku lozinku (podrazumevano: "moneyprintergobrrr")
- **Šifrovanje:** Omogućite šifrovanje diska ako je moguće



## 6. Dodatni alati



Umbrelova aplikacija Lightning Node pruža osnovne funkcije za upravljanje vašim kanalima, ali alati trećih strana nude naprednu funkcionalnost.



### ThunderHub



Moderni web interfejs za upravljanje Lightning čvorom, koji se može instalirati putem Umbrel App Store-a.



**Funkcije:**




- Vizualizacija kanala u realnom vremenu (kapaciteti, stanja)
- Integrisani alati za rebalansiranje
- Podrška za naplatu putem više puteva (MPP)
- Generisanje QR koda LNURL
- Upravljanje On-Chain transakcijama 



ThunderHub je idealan za praćenje aktivnog čvora za rutiranje i obavljanje jednostavnog balansiranja kanala.



### Ride The Lightning (RTL)



Web kompatibilan interfejs sa nekoliko Lightning implementacija (LND, Core Lightning, Eclair).



**Istaknuto:**




- Upravljanje sa više čvorova
- Kontrolne table osetljive na kontekst
- Podrška za submarine swaps putem Lightning Loop-a
- dvofaktorska autentifikacija
- Izvoz/uvoz rezervnih kopija kanala



RTL je kompletan "švajcarski nož" za administriranje Lightning čvora sa pristupom koji je više usmeren ka stručnjacima.



### Drugi korisni alati





- **Lightning Shell**: Komandna linija (lncli) putem pregledača
- **BTC RPC Explorer & Mempool** : Monitoring Blockchain-a
- **LNmetrics & Torq**: Analiza performansi rutiranja
- **Amboss & 1ML**: Upravljanje čvorom sa socijalnim funkcijama (aliasi, kontakti, analiza mreže)



Ovi alati se mogu instalirati u samo nekoliko klikova putem Umbrel App Store-a, bez ikakve složene konfiguracije.



**Dodatni resursi alata:**




- [ThunderHub.io - Funkcije](https://thunderhub.io) - Pregled funkcija ThunderHub-a
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL dokumentacija
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - Praktični vodič za rebalansiranje
- [Vodič "Upravljanje Lightning čvorovima"](https://github.com/openoms/lightning-node-management) - Napredna dokumentacija za napredne korisnike



## Zaključak



Pokretanje sopstvenog LND čvora na Umbrelu je važan korak ka finansijskoj suverenosti. Iako zahteva više tehničkog angažovanja nego skrbničko rešenje, prednosti u smislu kontrole, poverljivosti i aktivnog učešća u Lightning Network su značajne.



Prateći ovaj vodič, sada biste trebali biti u mogućnosti da instalirate LND, otvorite kanale, upravljate svojom likvidnošću i pristupite svom čvoru na daljinu. Slobodno postepeno istražujte napredne funkcije i dodatne alate kako postajete sve upoznatiji sa ekosistemom.



Zapamtite da sigurnost vaših sredstava zavisi od vaših zaštitnih mera i praksi. Odvojite vreme da razumete svaki aspekt pre nego što se obavežete na velike iznose.
