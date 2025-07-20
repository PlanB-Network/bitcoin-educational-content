---
name: Umbrel Nostr
description: Konfigurisanje i korišćenje Nostr aplikacija na Umbrel
---

![cover](assets/cover.webp)



## Preduslovi: Instalacija Umbrel-a



Umbrel je platforma otvorenog koda koja vam omogućava da lako hostujete Bitcoin aplikacije i druge usluge na sopstvenom ličnom serveru. To je sve-u-jednom rešenje koje uveliko pojednostavljuje samostalno hostovanje Bitcoin čvorova i decentralizovanih aplikacija.



Uverite se da ste instalirali Umbrel prateći naš vodič za instalaciju:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Uvod u Nostr



**Nostr** je otvoreni, decentralizovani mrežni protokol dizajniran za društveno umrežavanje. Njegovo ime znači _"Beleške i druge stvari prenesene putem releja"_. Omogućava svakome da objavljuje poruke (beleške), upravljane kao JSON događaji, i da ih širi putem relej servera umesto centralizovane platforme. Svaki korisnik poseduje par kriptografskih ključeva (privatni/javni) koji služe kao identifikator: javni ključ (npub) identifikuje korisnika, a privatni ključ (nsec) omogućava potpisivanje poruka. Zahvaljujući ovoj distribuiranoj arhitekturi, **Nostr nudi otpornost na cenzuru** i veliku fleksibilnost: možete koristiti nekoliko klijenata i povezati se na onoliko releja koliko želite, bez zavisnosti od jednog servera.



Ukratko, Nostr je decentralizovani komunikacioni protokol gde **klijenti** (korisničke aplikacije) šalju i primaju događaje putem **relaya** (servera). Ovaj protokol je posebno popularan u zajednici Bitcoin od 2023. godine, zbog svojih vrednosti decentralizacije i suvereniteta podataka.



**Napomena:** Da biste koristili Nostr, biće vam potreban vaš privatni ključ (generisan od strane Nostr klijenta ili putem posebnog dodatka). **Nikada ne delite svoj privatni ključ**, jer bi to omogućilo bilo kome da se predstavlja kao vi. Čuvajte ga na sigurnom mestu i koristite alate za sigurno upravljanje ključevima (pogledajte Savet ispod).



## Umbrel aplikacije za Nostr



Umbrel nudi ekosistem integrisanih aplikacija kako biste u potpunosti iskoristili Nostr na svom ličnom čvoru. Detaljno ćemo opisati upotrebu glavnih aplikacija povezanih sa Nostr-om: **Nostr Relay**, **noStrudel**, **Snort** i **Nostr Wallet Connect**. Svaka od njih zadovoljava specifičnu potrebu: _Nostr Relay_ je **privatni relej server**, _noStrudel_ i _Snort_ su **Nostr klijenti** (interfejsi za čitanje/objavljivanje beleški), dok je _Nostr Wallet Connect_ alat za povezivanje vašeg **Lightning portfolija** sa Nostr-om.



### Nostr Relay - Vaš privatni relej na Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** je Umbrelova zvanična aplikacija za pokretanje **sopstvenog Nostr releja** na vašem čvoru. Glavni cilj je imati **privatan** i pouzdan relej za **bekapovanje svih vaših Nostr** aktivnosti u realnom vremenu. Drugim rečima, korišćenjem ovog ličnog releja uz javne releje, osiguravate da su sve vaše beleške, poruke i reakcije kopirane kod kuće, zaštićene od cenzure ili gubitka podataka.



**Instalacija:** Iz Umbrel prodavnice aplikacija (kategorija _Social_), instalirajte _Nostr Relay_. Kada se pokrene, aplikacija radi u pozadini (docker servis).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Videćete njegovu Interface mrežu putem Umbrel-a: pruža osnovne informacije i, pre svega, URL vašeg releja (gore desno), koji ćete morati kopirati za dalju upotrebu. Dostupan je i dugme za sinhronizaciju (ikona globusa).



**Da biste iskoristili svoj Umbrel relej :



**Dodajte relej u vaš Nostr klijent:** U vašoj klijentskoj aplikaciji (npr. Damus na iOS-u, Amethyst na Androidu, Snort ili noStrudel na Umbrel-u, itd.), dodajte URL vašeg privatnog releja koji ste ranije kopirali. Podrazumevano, Umbrel relej sluša na portu **4848**. Ako mu pristupate na lokalnoj mreži, to daje URL kao: `ws://umbrel.local:4848` (ili koristite lokalnu IP adresu Umbrel-a).



Ako koristite Tailscale (pogledajte ispod), možete čak koristiti MagicDNS DNS alias (obično `umbrel` ili automatski generisano ime) da mu pristupite sa bilo kog mesta, uvek na portu 4848.



Ako više voliš Tor, preuzmi Umbrelov .onion Address i koristi ga sa portom 4848 putem pretraživača ili klijenta kompatibilnog sa Tor-om (pogledaj odeljak o Tor-u)



Once the URL has been added to your Nostr client's Relay configuration, connect to this relay. You should see in your client that the Umbrel relay is connected (usually indicated by a Green dot or similar).



**Synchronizujte istoriju (opciono)**: U Interface mreži _Nostr Relay_ na Umbrel-u, kliknite na **globus** 🌐 ikonu (na vrhu stranice). Ova akcija će naterati vaš Umbrel relej da se poveže sa vašim drugim relejima (onima koji su konfigurisani u vašem klijentu) kako bi **uvezao vaše stare javne** aktivnosti. To znači da će beleške koje ste ranije objavili ili pročitali putem javnih releja takođe biti preuzete i sačuvane na vašem privatnom releju. Molimo sačekajte da se sinhronizacija završi.



**Koristite Nostr kao i obično:** Od sada, svaka nova aktivnost (objavljene beleške, reakcije, šifrovane privatne poruke, itd.) koju obavljate na Nostr-u biće prosleđena kao i obično javnim relejima **i paralelno vašem Umbrel releju**. Ako je vaš Nostr klijent pravilno konfigurisan, slat će svaki događaj svim relejima (uključujući vaš). Vaš privatni relej će delovati kao rezervna kopija u realnom vremenu. Čak i u slučaju privremene diskonekcije, vaši korisnici će moći kasnije da resinhronizuju nedostajuće podatke zahvaljujući ovom releju. ovo vam daje potpunu kontrolu nad vašim Nostr podacima.



U pozadini, Umbrelov _Nostr Relay_ zasnovan je na projektu otvorenog koda **nostr-rs-relay** (implementacija Rust protokola). Podržava ceo Nostr protokol i brojne standardne NIP-ove (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, itd.), garantujući maksimalnu kompatibilnost sa klijentima.



### noStrudel - Nostr klijent za istraživače



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** je Nostr veb klijent namenjen naprednim korisnicima, idealan za razumevanje i detaljno istraživanje Nostr mreže. To je neka vrsta sandbox-a za ispitivanje događaja i releja, kao i za eksperimentisanje sa naprednim funkcijama protokola. Interface je na engleskom jeziku i relativno tehnički, što ga čini idealnim za iskusne korisnike koji su radoznali o unutrašnjem funkcionisanju Nostr-a.



**Instalacija:** Instalirajte _noStrudel_ iz Umbrel prodavnice aplikacija (kategorija _Social_). Kada se pokrene, može se pristupiti putem vašeg pregledača na vašem Umbrel Address (npr. `http://umbrel.local` ili putem njegovog .onion/Tailscale, pogledajte odeljak za eksterni pristup).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Konfiguriši releje:** Kada otvoriš noStrudel, videćeš dugme "Setup Relays" u gornjem desnom uglu. Klikni na njega da konfigurišeš svoje releje.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Na ovu stranicu nalepite URL vaše Umbrel releja koji ste ranije kopirali. Takođe možete dodati i druge releje koje aplikacija predlaže po defaultu. Kada konfigurišete svoje releje, kliknite na "Sign in" u donjem levom uglu da nastavite.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Connection:** noStrudel vam nudi nekoliko opcija povezivanja. U našem slučaju, izabraćemo "Private Key" i nalepiti vaš prethodno generisani Nostr privatni ključ. Ako još nemate ključ, možete instalirati [Nostr Connect] ekstenziju (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) da kreirate i/ili sačuvate vaše Nostr ključeve i tako komunicirate sigurnije sa raznim Nostr aplikacijama.



![Interface principale de noStrudel](assets/fr/07.webp)



Jednom povezan, možete koristiti noStrudel za deljenje beležaka putem Nostr-a. Interface vam omogućava pristup:





- Kompletna Nostr kontrolna tabla sa vremenskom linijom beleški, obaveštenjima, porukama, pretragom profila
- Upravljanje relejem i status veze
- Napredni alati za ispitivanje događaja i njihovog JSON sadržaja
- Opcije konfiguracije za filtere vremenske linije i PIN-ove



**Savjet:** Na _noStrudel_ možete postaviti _filtere vremenske linije_ ili testirati različite _NIP-ove (Nostr Implementation Possibilities)_. Na primer, proverite podršku za NIP-05 (decentralizovani identifikatori) ili novije funkcije. Ovo čini _noStrudel_ odličnim alatom za eksperimentisanje u kontrolisanom okruženju.



### Snort - Moderni Nostr klijent na Umbrelu



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** je još jedan Nostr veb klijent dostupan na Umbrel-u, koji nudi moderan, brz i pregledan **Interface** za interakciju sa decentralizovanom društvenom mrežom. Za razliku od noStrudel-a, koji je namenjen naprednim korisnicima, _Snort_ teži jednostavnosti upotrebe bez žrtvovanja funkcionalnosti. Izgrađen je u React-u i nudi uredan UX koji podseća na klasične društvene mreže, što ga čini pogodnim za svakodnevnu upotrebu.



**Instalacija:** Instalirajte _Snort_ iz Umbrel App Store-a (kategorija _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Kada otvorite Snort, videćete dugme "Register" u donjem levom uglu.



![Options de connexion dans Snort](assets/fr/10.webp)



Možete izabrati da se registrujete ili povežete sa postojećim nalogom (što ćemo uraditi za ovaj vodič).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort nudi nekoliko metoda povezivanja. Možete koristiti prethodno instaliranu Nostr Connect ekstenziju ili druge dostupne metode. Kada se povežete, moći ćete koristiti aplikaciju u potpunosti.



Interface iz _Snort_-a nudi :





- Prikaz **Objave/Razgovori/Globalno** za navigaciju između vaših beleški, razgovora u nitima ili globalnog feeda
- Kartice za **Obaveštenja**, **Poruke** (DM), **Pretraga**, **Profil**, itd.
- Dugme **+** ili _Write_ za objavljivanje nove beleške
- Upravljanje **pretplatama (praćenje)** i **listama**
- Meni za upravljanje relejima za dodavanje/uklanjanje releja i praćenje njihove dostupnosti



**Preporučena konfiguracija releja:** Da biste dodali svoj Umbrel relej, idite na Podešavanja - Releji. Unesite URL vašeg releja (`ws://umbrel:4848` ili drugi URL u zavisnosti od vaše konfiguracije) u Snortovu listu releja. Na ovaj način, Snort će objavljivati vaše beleške na vašem privatnom releju pored javnih.



### Nostr Wallet Connect - Povežite vaš Lightning Wallet sa Nostr



**Nostr Wallet Connect (NWC)** je aplikacija koja **povezuje vaš Umbrel (Lightning)** čvor sa kompatibilnim Nostr aplikacijama kako bi omogućila Lightning plaćanja (na primer, slanje _zaps_, tih mikro-plaćanja za "lajkovanje" sadržaja). U ovom vodiču ćemo pogledati kako povezati noStrudel sa vašim Lightning čvorom kako biste vršili plaćanja direktno sa Interface.



**Instalacija i konfiguracija:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Instaliraj _Nostr Wallet Connect_ iz Alby prodavnice na Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



U noStrudel-u, kliknite na svoj profil u gornjem desnom uglu, zatim na dugme "manage".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Kliknite na "Lightning" zatim "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Među dostupnim opcijama povezivanja, izaberite "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Kliknite na "Connect" da biste bili automatski preusmereni na vašu Umbrel Nostr Wallet Connect sesiju.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Na stranici Nostr Wallet Connect, možete:




   - Definišite svoj maksimalni budžet
   - Potvrdite autorizacije
   - Postavite vreme isteka za vezu


Kliknite na "connect" da završite.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Preusmeren si na noStrudel sa porukom o potvrdi: sada možeš zapovati ceo svet sa svog Wallet/LND čvora!



Zahvaljujući NWC, vaša **Lightning plaćanja putem Nostr-a** (zaps za nagrađivanje postova, _Value for Value_ plaćanja, itd.) počinju sa **vašeg sopstvenog čvora**. Više ne morate da usmeravate svoje transakcije preko eksternih servisa ili da skenirate QR kod sa telefona svaki put. Korisničko iskustvo je znatno poboljšano, dok ostaje _ne-kustodijalno_ i prijateljsko prema privatnosti.



Ako želite da saznate kako da postavite svoj Lightning čvor na Umbrel-u, preporučujem da pogledate ovaj drugi sveobuhvatni vodič:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Napredna konfiguracija i bezbednost



Korišćenje Umbrel-a i Nostr-a zajedno na naprednom nivou zahteva posebnu pažnju na **bezbednost** i **povezivanje**. Evo nekoliko saveta kako da zaštitite vašu konfiguraciju i pristupite joj optimalno, gde god da se nalazite.



### Siguran spoljašnji pristup: Tor i Tailscale



Iz bezbednosnih razloga, vaš Umbrel je po podrazumevanim postavkama dostupan samo na vašoj lokalnoj mreži (i putem Tor-a). Da biste komunicirali sa Nostr-om van kuće, imate dva preferirana rešenja: **Tor** (anonimni pristup putem onion mreže) i **Tailscale** (privatna VPN mreža).





- Pristup putem Tor-a:** Umbrel automatski konfiguriše **Tor servis (.onion)** za svoj Interface web i aplikacije. To znači da možete pristupiti Interface Umbrel (uključujući _noStrudel_ ili _Snort_) sa bilo kog mesta, koristeći Tor pretraživač, bez izlaganja vaše javne IP adrese. _Tor se koristi za pristup vašim Umbrel servisima izvan vaše lokalne mreže, bez izlaganja vašeg uređaja Internetu ([Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ Da biste koristili ovu opciju, idite na Umbrel podešavanja i preuzmite vaš Umbrel .onion URL (ili skenirajte priloženi QR kod). Na Tor pretraživaču, pristupite ovom .onion Address: dobićete isti Interface kao lokalno. Tada možete koristiti vaše Nostr aplikacije kao kod kuće.


**Nostr relay putem Tor-a:** Ako želite da vaš Nostr relej bude dostupan putem Tor-a vašim korisnicima (ili ovlašćenim prijateljima), to je moguće. Umbrel ne pruža direktno .onion Address releja, ali pošto radi na portu 4848, možete ili:





    - Koristite UI Umbrel-ov .onion Address i konfigurišite vaš klijent da se poveže preko ovog Interface (nepraktično za WebSocket),





    - Ili** izložite port 4848 kao zasebnu onion uslugu. Ovo zahteva podešavanje Tor konfiguracije na Umbrel-u (rezervisano za napredne korisnike koji su vešti sa SSH-om). Alternativno, razmislite o **Tor tunelu** na drugom serveru koji preusmerava na Umbrel: međutim, za ličnu upotrebu, najlakše je koristiti Tailscale.





- Pristup putem Tailscale-a:** [Tailscale](https://tailscale.com/) je mesh VPN rešenje koje stvara virtuelnu privatnu mrežu između vaših uređaja i Umbrel-a. Prednost: radi kao da ste na LAN-u, ali preko Interneta, šifrovano i bez složene konfiguracije. **Tailscale dodeljuje vašem Umbrel-u fiksnu IP adresu i privatno ime domena, bez obzira na njegovu mrežnu lokaciju ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. U praksi, kada instalirate Tailscale na Umbrel (iz Umbrel App Store-a, kategorija _Networking_) **i** na vaše uređaje (mobilni, PC...), moći ćete da pristupite Umbrel-u putem Address kao što je `100.x.y.z` (Tailscale IP) ili imenom kao što je `umbrel.tailnet123.ts.net`.


za Nostr_, Tailscale je izuzetno koristan: vaš mobilni uređaj, ako ima aktiviran Tailscale, moći će da se poveže na `ws://umbrel:4848` (zahvaljujući MagicDNS) ili direktno na Tailscale IP i port 4848 da koristi relej. Klijenti kao što su Damus ili Amethyst će videti vaš Umbrel kao da je na istoj lokalnoj mreži. **Savet:** Omogućite opciju **MagicDNS** u Tailscale da koristite hostname `umbrel` umesto da pamtite IP. Ovo osigurava glatku vezu sa vašim relejom čak i kada ste u pokretu ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Štaviše, Tailscale vam omogućava pristup Interface Umbrel (a samim tim i _noStrudel/Snort_ web klijentima) putem jednostavnog pregledača, koristeći privatnu IP adresu ili dodeljeno ime domena. Nema potrebe za Tor pregledačem, a brzine prenosa podataka su generalno bolje nego putem Tor mreže.




**Napomena: Tor i Tailscale nisu međusobno isključivi. Možete zadržati Tor aktivnim za anonimizovani pristup ili specifične usluge, a koristiti Tailscale svakodnevno zbog njegove jednostavnosti. U oba slučaja, ne morate otvarati port na vašem ruteru, što pojačava sigurnost.



### Osiguravanje vašeg Nostr releja (preporučene prakse)



Ako hostujete Nostr relej na Umbrelu, posebno u naprednom kontekstu, obavezno primenite nekoliko dobrih praksi:





- Privatni ili ograničeni relej:** Po defaultu, vaš Umbrel relej je privatan (nije javno objavljen) i, ako mu pristupate samo putem Tailscale-a ili vašeg LAN-a, ostaće nedostupan strancima. **Čuvajte link poverljivim ** Ne objavljujte ga na javnim Nostr mrežama osim ako ne želite dobrovoljno da hostujete druge korisnike, što je potpuno drugačije pitanje (moderacija, protok, itd.). Za ličnu upotrebu, preporučujemo da ograničite pristup na sebe i, ako je potrebno, na nekoliko pouzdanih prijatelja i porodicu.





- Whitelist / Auth**: Implementacija nostr-rs-relay podržava mehanizam autentifikacije **NIP-42** kao i _whitelists_ javnih ključeva. Omogućavanjem ovih opcija, možete ograničiti svoj relej tako da **prihvata samo događaje potpisane određenim ključevima (vašim)**, ili da klijenti moraju da se autentifikuju kako bi objavili. podešavanje ovoga zahteva uređivanje `config.toml` konfiguracionog fajla releja u Umbrel-u (putem SSH u Docker kontejneru)._ To je napredna manipulacija, ali na primer možete navesti oglase koji su dozvoljeni (`pubkey_whitelist`). Na ovaj način, čak i ako neko otkrije vaš relej, neće moći da objavi ništa tamo ako nije na listi.





- Ažuriranja i održavanje:** Održavajte svoj Umbrel i aplikaciju _Nostr Relay_ ažurnim. Ažuriranja mogu uključivati poboljšanja performansi (npr. bolje rukovanje neželjenom poštom) i sigurnosne popravke. Na Umbrelu redovno proveravajte App Store za ažuriranja _Nostr Relay_ i primenjujte ih po potrebi.





- Praćenje i ograničenja:** Pratite kako se koristi vaš relej. Ako ga otvorite za druge, pratite opterećenje (CPU/RAM skladište) na vašem Umbrel-u, jer relej može brzo akumulirati mnogo podataka. nostr-rs-relay nudi podesiva **ograničenja brzine i skladištenja** (`limits` u konfiguraciji, npr. broj događaja po sekundi, maksimalna veličina događaja, brisanje starih događaja...). Za privatnu upotrebu verovatno nećete morati da dirate ovo, ali budite svesni da ovi parametri postoje ako vam zatrebaju ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Osiguranje Nostr ključeva:** Ova tačka je već pomenuta, ali je ključna: nikada ne unosite svoje Nostr privatne ključeve u Interface kojem ne verujete u potpunosti. Umesto toga, koristite ekstenzije za pregledač ili spoljne uređaje (kao što su Nostr _signers_ na odvojenim telefonima) za potpisivanje osetljivih akcija. Na Umbrel-u, vaši web klijenti kao što su _Snort_ i _noStrudel_ mogu raditi bez poznavanja vašeg tajnog ključa, putem NIP-07. Iskoristite ovu priliku da kombinujete udobnost i sigurnost.




Prateći ove savete, vaša integracija Umbrel čvora sa Nostr-om biće i moćna **i** sigurna. Imaćete kompletno okruženje: Bitcoin čvor za Lightning plaćanja, privatni Nostr relej za suverenitet podataka i visokoperformantne Nostr veb klijente za navigaciju ovom novom decentralizovanom društvenom mrežom. Uživajte u istraživanju Nostr-a sa Umbrel-om!