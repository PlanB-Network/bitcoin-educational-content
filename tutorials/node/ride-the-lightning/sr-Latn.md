---
name: Ride The Lightning (RTL)
description: Koristite Ride The Lightning (RTL) za upravljanje vašim Lightning čvorom
---
![cover](assets/cover.webp)


## 1. Uvod



**Ride The Lightning (RTL)** je kompletna veb aplikacija za upravljanje čvorom Lightning mreže . Ova samostalno hostovana veb aplikacija nudi Lightning** "kokpit" dostupan iz vašeg pregledača. RTL radi sa svim glavnim Lightning implementacijama (LND, Core Lightning/CLN i Eclair) i pruža vam potpunu kontrolu nad vašim čvorom i kanalima. Kao open-source (MIT licenca) i besplatna, RTL aplikacija je integrisan po defaultu u mnogim rešenjima za čvorove spremnim za upotrebu (RaspiBlitz, MyNode, Umbrel, itd.).



**Bez grafičkog interfejsa, Lightning čvorovima se može upravljati samo putem jednostavnih CLI komandi prilagođenih korisniku. RTL pojednostavljuje ove operacije ergonomskim interfejsom. Ovde su **glavne aplikacije**:





- **Pregledajte svoje kanale i čvor** - Kontrolna tabla prikazuje On-Chain saldo, Lightning likvidnost (lokalna/udaljena), status sinhronizacije, alias čvora i više. Možete pregledati listu svojih kanala, kapacitet, lokalnu/udaljenu distribuciju i status. RTL nudi kontekstualno osetljive kontrolne table za analizu aktivnosti iz različitih uglova.





- **Upravljanje Lightning kanalima** - Otvorite/zatvorite kanale uz nekoliko klikova. RTL vam omogućava da se povežete sa peer-om i otvorite kanal bez komande. Možete prilagoditi naknade za rutiranje, pregledati balansni skor ili pokrenuti kružno rebalansiranje kako biste rebalansirali sredstva između kanala.





- **Pratite i izvršavajte uplate** - RTL upravlja Lightning transakcijama: šaljite uplate putem faktura, generišite fakture za primanje, pratite transakcije (uplate, rutiranje) sa detaljnom istorijom. Interfejs takođe analizira rutiranje kako bi video koje uplate prolaze kroz vaš čvor.





- **Upravljanje i rezervna kopija On-Chain novčanika** - Kartica On-Chain omogućava vam da generišete adrese i šaljete transakcije. RTL olakšava čuvanje kanala izvozom SCB datoteke za LND, sa automatskim ažuriranjem za svaku izmenu kanala.



Ukratko, RTL je **moćna kontrolna tabla za Lightning mrežu**, koja nudi edukativni korisnički interfejs za svakodnevno upravljanje vašim čvorom. Ovaj vodič će vas provesti kroz instalaciju i korišćenje za upravljanje vašim kanalima i plaćanjima.



## 2. Tehnički rad RTL-a



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Pre nego što pređemo na suštinu, korisno je ukratko razumeti **kako RTL komunicira sa vašim Lightning čvorom** na tehničkom nivou.



**Opšta arhitektura:** RTL je veb aplikacija izgrađena sa Node.js (backend) i Angular (frontend). Konkretno, RTL radi kao mali lokalni veb server (na portu 3000 po podrazumevanju) koji komunicira sa vašom Lightning implementacijom putem svojih API-ja. U zavisnosti od tipa :





- Sa **LND**, RTL koristi REST API LND (port 8080) za izvršavanje Lightning komandi. Veza je obezbeđena TLS-om i zahteva **admin macaroon** fajl iz LND-a za autentifikaciju.





- Sa **Core Lightning (CLN)**, RTL koristi ili REST API koji pruža *c-lightning-REST*, ili **access rune** putem `commando` dodatka. Rešenja kao što je Umbrel automatski konfigurišu ove elemente.





- Sa **Eclair**, RTL se povezuje na Eclair REST API koristeći konfigurisanu lozinku za autentifikaciju.



**Konfiguracija i sigurnost:** RTL se konfiguriše putem JSON fajla (`RTL-Config.json`) gde definišete web port, pristupnu lozinku i informacije o povezivanju sa vašim čvorom. Web interfejs je zaštićen prijavom/lozinkom (podrazumevana `password` treba da se promeni) i podržava 2FA. Podrazumevano, RTL radi kao lokalni HTTP (`http://localhost:3000`), ali za daljinski pristup uvek koristite sigurnu vezu (HTTPS putem reverse-proxy, Tor, ili VPN).



Ukratko, RTL je dodatna komponenta koja se povezuje sa vašim čvorom preko sigurnih API-ja, zahteva odgovarajuće pristupne tokene i nudi sopstveni sigurnosni sloj. Ova modularna arhitektura čak omogućava upravljanje **nekolicinom Lightning čvorova sa jednom RTL instancom**.



## 3. RTL instalacija



Kako je RTL distribuiran kao softver otvorenog koda, postoji nekoliko načina da ga instalirate na svoj sistem. U ovom odeljku ćemo pokriti dva glavna pristupa: ručna instalacija i instalacija putem Umbrel-a.



### Ručno metoda



Ručno instaliranje je pogodno ako želite da zadržite detaljnu kontrolu ili ako integrišete RTL u prilagođenu konfiguraciju. Koraci navedeni u nastavku odnose se na LND čvor koji radi na Linux operativnom sistemu (npr. Raspberry Pi ili VPS sa Ubuntu/Debian), ali su slični za CLN/Eclair.



**Preduslov:** uverite se da imate **sinhronizovan** Bitcoin čvor i funkcionalan Lightning čvor (LND, CLN ili Eclair) na mašini. RTL ne sadrži Lightning čvor per se, već se povezuje na postojeći čvor. Takođe vam je potreban instaliran **Node.js** (preporučena verzija 14+). Možete proveriti sa `node -v` ili instalirati Node sa zvaničnog sajta (https://nodejs.org/en/download/) ili putem vašeg menadžera paketa.



Glavne faze instalacije su:



**Preuzmi RTL kod**: Kloniraj zvanični RTL GitHub repozitorijum u direktorijum po vašem izboru. Na primer:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Instaliraj zavisnosti**: RTL je Node.js aplikacija, tako da je potrebno instalirati potrebne module. U RTL folderu, pokreni :



```bash
npm install --omit=dev --legacy-peer-deps
```



Ova komanda instalira potrebne NPM pakete (ignorišući razvojne zavisnosti). Opcija `--legacy-peer-deps` se preporučuje kako bi se izbegli mogući konflikti zavisnosti u Node-u.



**RTL-Config**: Kada su zavisnosti postavljene, pripremite konfiguracioni fajl. Kopirajte/preimenujte fajl `Sample-RTL-Config.json` u korenu projekta u `RTL-Config.json`. Otvorite ga :





   - **UI password**: izaberite sigurnu lozinku i unesite je u `multiPass` (umesto podrazumevane `"password"`).
   - **Port**: podrazumevano `3000`. Možete ga promeniti ako je ovaj port već zauzet na vašem računaru.
   - **Node**: u odeljku `nodes[0]`, prilagodite parametre za vaš čvor:
     - `lnNode`: opisni naziv za vaš čvor (npr. `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (or `"CLN"`/`"ECL"` as appropriate).
     - Pod `authentication`:
       - macaroonPath`: navedite punu putanju do fascikle koja sadrži LND-ov macaroon admin.
       - `configPath`: putanja do konfiguracione datoteke čvora (`LND.conf` za LND).
     - Pod `settings`:
       - `fiatConversion`: postavite na `true` ako želite konverziju fiat valuta.
       - `unannouncedChannels`: postavite na `true` da biste videli nenajavljene kanale.
       - `themeColor` i `themeMode`: prilagođavanje interfejsa.
       - `channelBackupPath`: putanja za LND rezervne kopije kanala.
       - `lnServerUrl`: URL vašeg Lightning čvora (npr. `https://127.0.0.1:8080`).



**Pokreni RTL server**: U RTL fascikli, pokreni :



```bash
node rtl
```



Aplikacija se pokreće i može se pristupiti na `http://localhost:3000`.



**(Opcionalno) Pokreni RTL kao servis**: Za automatsko pokretanje, kreiraj systemd:



Da uradite ovo:




- Otvorite terminal na vašem računaru.
- Kreirajte novi servis fajl pomoću sledeće komande. (zamenite `nano` vašim omiljenim uređivačem):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopirajte i nalepite sadržaj ispod u ovaj fajl:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Zamenite `/path/to/RTL/rtl` sa stvarnom putanjom do `rtl` fajla na vašem računaru, i `<your_user>` sa vašim korisničkim imenom na Linuxu.
- Sačuvaj i zatvori datoteku.
- Ponovo učitajte systemd konfiguraciju:


```bash
sudo systemctl daemon-reload
```




- Aktivirajte i pokrenite RTL uslugu:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL će sada automatski početi svaki put kada se mašina ponovo pokrene. Njegov status možete proveriti sa:


```bash
sudo systemctl status RTL
```



### Instalacija putem Umbrel-a



Ako koristite [Umbrel](https://getumbrel.com), instalacija RTL-a je mnogo jednostavnija:





- Pristupite Umbrel interfejsu (obično putem `http://umbrel.local`)
- Idi na **App Store**
- Pretraži "Ride The Lightning"



**Važna napomena: postoje dve odvojene RTL aplikacije u Umbrel App Store-u:**




- **Ride The Lightning** (za LND): za korišćenje sa Umbrel-ovim podrazumevanim Lightning čvorom (LND).
- **Ride The Lightning (Core Lightning)**: koristite samo ako ste instalirali aplikaciju *Core Lightning* na Umbrel-u i želite upravljati ovim čvorom pomoću RTL.



*Svaka RTL verzija je unapred konfigurisana za dijalog sa odgovarajućom implementacijom (LND ili Core Lightning). Ako niste promenili vaš Lightning čvor, jednostavno izaberite klasičnu LND verziju*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Kliknite na **Instaliraj**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Važno:** Nakon instalacije, RTL prikazuje ekran sa podrazumevanom lozinkom. **Kopirajte i sačuvajte ovu lozinku** - biće vam potrebna za prijavljivanje na RTL korisnički interfejs. Ova lozinka će biti prikazana svaki put kada se RTL pokrene dok ne označite opciju "Ne prikazuj ponovo", engleski "Don't show it again".



Umbrel automatski brine o:




- Preuzimanju i konfiguraciji RTL-a
- Konfigurisanju pristupa Lightning čvoru
- Upravljanju ažuriranjima
- Osiguravanju pristupa interfejsu



Kada se instalira, aplikacija se pojavljuje u vašem meniju *Aplikacije* na Umbrel-u. Kliknite na **Ride The Lightning** da je pokrenete.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Na ekranu za prijavu unesite lozinku koju ste ranije kopirali. Kada se prijavite, RTL web interfejs će biti direktno dostupan sa Umbrel kontrolne table, bez dodatne konfiguracije!



## 4. Uvod i upotreba RTL interfejsa



Sada kada je RTL pokrenut, hajde da istražimo njegov web interfejs i njene ključne karakteristike. Proći ćemo kroz različite sekcije aplikacije kako bismo vam dali potpuni pregled.



### Glavna kontrolna tabla



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Čim se prijavite, pristupate **glavnoj kontrolnoj tabli**, koja vam pruža pregled vašeg Lightning čvora. Ova stranica centralizuje osnovne informacije:




- Vaš ukupni Lightning saldo
- On-Chain raspoloživi saldo
- Raspodela vaše likvidnosti (prilivi/odlivi)
- Brz pristup za slanje i primanje satošija putem vašeg Lightning čvora



### Upravljanje On-Chain fondom 



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Kartica **On-Chain** omogućava vam upravljanje vašim bitcoinima direktno na glavnom lancu:




- Prikaz stanja u različitim jedinicama (Sats, BTC, USD)
- Kompletna lista transakcija
- Generisanje Taproot (P2TR), P2SH (NP2WKH) ili Bech32 (P2WKH) adresa
- UTXO upravljanje, primanje i slanje bitkoina



### Lightning: detaljna prezentacija podmenija



RTL interfejs ima bočni meni posvećen Lightning mreži, okupljajući sve ključne funkcije za upravljanje vašim čvorom. Evo detalja za svaki podmeni, redosledom iz snimka ekrana:



#### 1. Peers/Channels (povezani čvoroni i kanali)



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Ovaj podmeni vam omogućava da:




- Pogledajte listu vaših povezanih čvorova i Lightning kanala koji su otvoreni ili na čekanju.
- Dodajte novog peer-a (povežite se sa drugim Lightning čvorom).
- Otvorite, zatvorite ili upravljajte postojećim kanalima.
- Prikaži detalje svakog kanala: kapacitet, lokalni/udaljeni balans, status, istorija trgovanja, skor balansa, itd.



#### 2. Transakcije



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



U ovom podmeniju, možete :




- Poslati Lightning uplate (preko fakture).
- Generisati i upravljati fakturama za primanje uplata.
- Pregledati kompletnu istoriju poslatih i primljenih uplata, sa detaljima (iznos, datum, status, naknade, broj preskakanja, itd.).



#### 3. Rutiranje



Ovaj podmeni prikazuje:




- Plaćanja usmerena putem vašeg čvora za druge Lightning mreže korisnika.
- Statistika rutiranja: broj prenetih transakcija, zarađene naknade, naiđene greške.
- Izvoziva istorija za naprednu analizu.



#### 4. Odlaganja (eng. Deferrals)



Ovaj podmeni nudi:




- Detaljni izveštaji o aktivnosti vašeg Lightning čvora.
- Grafikoni i tabele o kanalima, plaćanjima, naknadama, kapacitetu, itd.
- Alati za bolje razumevanje performansi vašeg čvora.



#### 5. Grafička pretrga



Ovaj podmeni vam omogućava da:




- Istražite topologiju Lightning mreže.
- Pretraži specifične čvorove ili kanale.
- Dobijte informacije o povezivanju i ukupnom kapacitetu mreže.



#### 6. Potpiši/Verifikuj



Ovaj podmeni nudi:




- Sposobnost potpisivanja poruke ključem vašeg čvora (dokaz o vlasništvu).
- Verifikacija potpisa za autentifikaciju poruka od drugih čvorova.



#### 7. Rezervna kopija (eng. Backup)



Ovaj podmeni je posvećen bekapu:




- Izvozu rezervne datoteke kanala (SCB za LND).
- Vraćanju konfiguraciju ili kanale ako je potrebno.
- Savetima za zaštitu vaših rezervnih kopija.



#### 8. Čvor/Mreža



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



U ovom podmeniju ćete pronaći:




- Potpuni rezime statusa vašeg Lightning čvora: alias, verzija, boja, status sinhronizacije.
- Statistika o kanalima (aktivni, na čekanju, zatvoreni), ukupni kapacitet, povezanost.
- Informacije o globalnoj Lightning mreži i poziciji vašeg čvora u njemu.



### Usluge: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz je privatnosti naklonjena, ne-kustodijalna menjačnica koja konvertuje bitkoine između Lightning mreže i Blockchain Bitcoin-a (On-Chain). Nudi dve vrste operacija: Reverse Submarine Swap (**Swap Out**) i Submarine Swap (**Swap In**).



#### Swap Out (Reverse Submarine Swap)



Swap Out konvertuje satošija dostupne na Lightning mreži u On-Chain bitkoine. Ovaj mehanizam je koristan kada čvor ostane bez dolaznog kapaciteta, ili kada želite da povratite sredstva sa On-Chain adrese. Proces funkcioniše na sledeći način:




- Korisnik bira iznos za razmenu
- Čvor šalje Lightning uplatu Boltz-u
- Zauzvrat, Boltz blokira ekvivalentan iznos u On-Chain bitcoinima.
- Kada je transakcija potvrđena, korisnik može preuzeti sredstva otkrivanjem tajne korišćene u zameni.



Ovaj proces je ne-kustodijalan, pri čemu Boltz nikada ne drži sredstva korisnika.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Submarine Swap)



S druge strane, Swap In omogućava da se sredstva On-Chain ponovo ubrizgaju u Lightning mrežu. Ovo je posebno korisno za obnavljanje izlaznog kapaciteta na vašim kanalima. Postupak je sledeći:




- Korisnik šalje bitkoine na određenu adresu generisanu od strane Boltz-a
- Ova sredstva može osloboditi samo Boltz ako plati Lightning fakturu generisanu od strane korisničkog čvora.
- Jednom kada je faktura plaćena, sredstva su dostupna na Lightning kanalu, povećavajući izlazni kapacitet čvora.



![Configuration d'un swap-in](assets/fr/12.webp)



Ova dva mehanizma omogućavaju efikasno upravljanje likvidnošću Lightning kanala, uz očuvanje korisnikovog suvereniteta nad njegovim sredstvima.



### Konfiguracija i prilagođavanje



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Kartica **Node Config** vam omogućava prilagođavanje vašeg iskustva:




- Aktivacija nenajavljenih kanala
- Prilagodite prikaz rasprodaje
- Block explorer konfiguracija
- Podešavanje interfejsa



### Dokumentacija i pomoć



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Konačno, odeljak **Pomoć** nudi sveobuhvatnu dokumentaciju o:




- Početnon konfiguraciji
- Upravljanju povezanim čvorovima i kanalima
- Plaćanjima i transakcijama
- Rezervnim kopijama i vraćanjima
- Izveštajima i statistikama
- Potpisima i verifikaciji
- Parametrima čvora i aplikacije



Ovaj sveobuhvatni interfejs omogućava vam da efikasno upravljate svojim Lightning čvorom, od osnovnih operacija do naprednih funkcija, sve u intuitivnom, dobro organizovanom interfejsu.



## 5. Napredni slučajevi upotrebe i bezbednost



U ovom odeljku, evo šta treba da znate kako biste nastavili sa RTL-om i osigurali svoj Lightning čvor:



### Praćenje i rešavanje problema



Da biste nadgledali svoj čvor, možete izvesti RTL podatke (logove, CSV) i pregledati ih u alatima kao što je Grafana. U slučaju problema (blokirana uplata, neaktivan kanal), konsultujte LND/CLN logove i koristite dijagnostičke komande (`lncli listchannels`, `lncli pendingchannels`, itd.). RTL takođe nudi logove interfejsa za praćenje događaja rutiranja.



### Siguran daljinski pristup



Nikada ne izlažite RTL direktno na internetu. Dajte prednost:




- **VPN-u** (npr. Tailscale) za privatni, šifrovani pristup
- **Tor-u** za siguran, anoniman pristup
- **Reverse proxy HTTPS** (Nginx/Caddy) samo ako znate kako da ga konfigurišete



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Dobre bezbednosne prakse





- **Zaštitite svoj pristup**: nikada ne delite admin.macaroon ili vašu RTL lozinku. Ograničite dozvole na osetljivim fajlovima.
- **Redovni bekapovi**: eksportujte fajl bekapa kanala (SCB) nakon svake izmene i čuvajte ga van čvora.
- **Ažuriranja**: održavajte RTL, vaš čvor i Umbrel ažurnim sa najnovijim sigurnosnim ispravkama.
- **Poverljivost**: anonimizujte dnevnike i snimke ekrana pre nego što ih podelite. Nikada javno ne delite svoje bilanse ili liste partnera.
- **Jedinstveni pristup**: RTL nije za više korisnika. Ne delite administratorski pristup. U slučaju da je potreban pristup samo za čitanje, koristite odgovarajući macaroon.



Primenom ovih principa, u velikoj meri ograničavate rizike i zadržavate kontrolu nad svojim Lightning čvorom.



## 7. Zaključak



**Ride The Lightning** je esencijalni alat za efikasno upravljanje Bitcoin/Lightning čvorom, bilo da ste početnik ili napredni korisnik. Pruža jasan korisnički interfejs za kontrolu vaših kanala, plaćanja i zdravlja čvora, dok produbljuje vaše razumevanje Lightning mreže.



RTL se izdvaja po svojoj kompatibilnosti sa više implementacija, naprednim funkcijama (rebalansiranje, zamene, izveštaji) i pedagoškom pristupu. Za jednostavne potrebe, Umbrel interfejs ili mobilni novčanik će biti dovoljni, ali RTL ima savršenog smisla za aktivno, optimizovano upravljanje čvorovima.



Da saznate više :




- Zvanična RTL veb stranica: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Tehničke diskusije, najave projekata, povratne informacije i obrazovni resursi
- Umbrel Community Forum: [community.getumbrel.com](https://community.getumbrel.com) - Zvanični forum sa posvećenim Bitcoin/Lightning odeljkom, vodičima i rešenjima za uobičajene probleme
- Lightning Network Developers: [github.com/lightning](https://github.com/lightning) - Zvanični GitHub repozitorijum za praćenje razvoja i doprinos izvornom kodu
- Stack Exchange Bitcoin: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Tehnička pitanja i odgovori sa programerima i naprednim korisnicima



Ukratko, RTL vam daje potpunu kontrolu nad vašim Lightning čvorom, u modernom, potpuno opremljenom interfejsu.



**Izvori:** RTL zvanična veb stranica; RTL GitHub; Umbrel App Store; Umbrel zajednica; Plan B Network resursi.



Da biste produbili svoje razumevanje o tome kako Lightning mreža funkcioniše, takođe vam preporučujem da pohađate ovaj besplatni kurs:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
