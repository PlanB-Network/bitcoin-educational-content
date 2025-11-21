---
name: LNbits

description: Platforma za računovodstvo trgovaca
---

![presentation](assets/lnbits-intro.webp)

# Računovodstveni sistem


LNbits je prepun mnogih alata za kontrolu i usmeravanje vaših dolaznih i odlaznih sredstava, povezivanje vaše veb prodavnice ili čak uređaja kao što su Hardware Wallet ili bankomat koji ste sami izgradili. Tipovi korisnika uključuju:


- Vlasnici Wallet koji žele da koriste LNbits kao Interface za upravljanje svojim sredstvima, kao i za dodatne funkcije.
- Online i offline trgovci ili pružaoci usluga koji žele da prihvate Bitcoin onchain i Lightning Network uplate.
- Programeri koji žele da razvijaju Lightning Network aplikacije.
- Operateri čvorova koji žele da integrišu svoj čvor sa LNbits sistemom za računovodstvene svrhe.
- Svi oni imaju različite potrebe. Gradimo LNbits na modularan način tako da svaki korisnik može koristiti naše funkcije na način koji vam najbolje odgovara.


# Wallet menadžer


LNbits je besplatan i otvoren sistem za računovodstvo - nije menadžer čvorova. Upravljanje kanalima je domen Lightning čvora koji je povezan sa LNbits kao izvor finansiranja, kao što su LND ili c-lightning. Superkorisnik ili Administratorski korisnici u sistemu LNbits su odgovorni za upravljanje ukupnom pristupačnošću i konfiguracijom računovodstvenih funkcija i internih ekstenzija.


LNbits deluje kao Interface između korisnika i Lightning čvora, pružajući jednostavan, korisnički prijatan način za upravljanje i interakciju sa mrežom plaćanja.


Zamislite LNbits kao „wordpress modularni okvir“ za vaš čvor. Lako upravljiva platforma, zasnovana na ekstenzijama koje možete kombinovati za brojne slučajeve upotrebe.


Zamislite LNbits kao vaš sopstveni softver za upravljanje finansijama banke. Vaš čvor nudi kanale za plaćanje, a LNbits proširuje vaš čvor kako bi mogao da upravlja sa više od jednog lightning Wallet koji dolazi sa vašim čvorom. Ovi novčanici ne moraju nužno pripadati vama. Recimo da vi, kao LN operater čvora, već imate dovoljno likvidnosti kanala i sredstava i sada želite da ponudite neke Bitcoin bankarske usluge svojim prijateljima, porodici, sopstvenoj prodavnici ili drugim redovnim trgovcima.


Ponudićete im jednostavan način da otvore „bankovni račun“ na vašem čvoru bez pristupa drugim novčanicima na vašem čvoru i svoj likvidnosti vašeg čvora, već samo njihovom delu. Vaš čvor (banka) deluje samo kao pružalac transporta za njihove uplate (ulazne/izlazne).


NAPOMENA: sva sredstva koja vaši „kupci“ polože na svoje LNbits bankovne račune na vašem čvoru, ići će direktno u kanale vašeg čvora LN. To znači da ste VI zapravo pravi vlasnik tih sredstava. Imaćete veliku odgovornost za njihova sredstva. Nemojte biti zli i pobeći sa sredstvima, nemojte biti zli i naplaćivati visoke naknade. Želimo da zeznemo fiat bankare, ne da zeznemo jedni druge (korisnike Bitcoin).


# Demo platforma


Demo se može pronaći na [https://legend.lnbits.com](https://legend.lnbits.com). Potpuno je funkcionalan i može se koristiti za učenje o Lightning Network i funkcijama LNbits i LNURL uopšte. Iako vas ne možemo sprečiti, zamolili bismo vas da ga ne koristite za vašu produkcijsku postavku. Ne samo da često radimo na serverima kako bismo testirali nove funkcije, već bismo vas želeli ohrabriti da pokrenete svoj sopstveni čvor i LNbits na suveren način. Ako mislite da je pokretanje čvora previše za sada, možete povezati LNbits sa uslugom čuvara u oblaku kao što su Opennode, Luna ili Votage ili sa Lightning Tipbot-om na Telegramu, da navedemo neke.


# LNbits flajer


Želite da predate osnovne informacije trgovcu ili prijatelju koji se bavi građevinom? Veoma smo srećni da objavimo naš prvi flajer koji svi mogu koristiti. Veličina je globalno tipičan format flajera sa 6 stranica (2 preklopa) i širinom od 3508 i visinom od 2480px.


LNbits za trgovce: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits za graditelje: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# Neke Osnove


LNbits radi na osnovu LNURL protokola što znači da su zahtevi validni u dva oblika: ili kao https:// clearnet link (samopotpisani sertifikati nisu dozvoljeni) ili kao http:// v2/v3 onion link. Da biste ponudili LNbits usluge kao što su LNURLp/w QR kodovi ili NFC kartice, koje se mogu koristiti na terenu, potrebno je da otvorite LNbits prema clearnet-u (https).


Pre nego što instalirate LNbits, obavezno pročitajte i razumite sledeće opšte vodiče o tome šta je LNbits i koje mogućnosti vam otvara.



- [LND Vodič](https://docs.lightning.engineering/) | Instaliranje LND
- [LND Config Primer](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND Postavke
- [Vodič za CLN](https://docs.corelightning.org/docs/installation) | Instalacija CLN-a
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Pokreni Watchtower](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Veoma važno!


Detaljniji vodiči za korišćenje LNbits-a u specifičnim scenarijima upotrebe ovde:



- [Početak sa LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack vodič
- [ToDos za vašu sigurnost sa LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Private Banks on Lightning Network](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Substack vodič
- [Pokrenite skrbničke novčanike za svoje prijatelje i porodicu](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack vodič
- [LNbits za mali restoran / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack vodič
- [Korišćenje LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack vodič
- [Pokrenite svoj NOSTR Market sa LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack vodič
- [Korišćenje LNbits za školske projekte ili festivalske događaje](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools)  Substack vodič



# Instaliraj LNbits


## Osnovni vodič za instalaciju


LNbits se može instalirati na bilo koju Linux OS mašinu. Ne zahteva moćnu mašinu ili server, već samo dovoljno RAM memorije i malo prostora na disku za bazu podataka. Može se pokretati odvojeno od BTC/LN čvora (lokalni PC ili udaljeni VPS) ili zajedno na istoj mašini sa čvorom ili već instaliranom u mašini sa softverom za čvor u paketu.


Možete birati između najčešćih upravitelja paketa kao što su poetry i nix. Po defaultu, LNbits će koristiti SQLite kao svoju bazu podataka. Takođe možete koristiti PostgreSQL koji se preporučuje za aplikacije sa velikim opterećenjem. [Ovde je vodič za osnovnu instalaciju koristeći poetry ili nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


Za sve koji su novi u ovome, naći ćete detaljnije vodiče korak po korak za pokretanje vašeg LNbits-a u specifičnim okruženjima:


- [LNbits na clearnet-u](https://ereignishorizont.xyz/lnbits-server/en/) od Axela
- [LNbits na VPS-u](https://github.com/TrezorHannes/vps-lnbits) od strane Hannesa
- [LNbits na cloudflare](https://www.nodeacademy.org/lnbits) od Lea


Možete pronaći i video o [dockerizovanom podešavanju na VPS-u sa PostgreSQ, LightningTipBot kao izvorom finansiranja koristeći nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).


[Više scenarija instalacije ovde](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


Za čvorove softverskih paketa, molimo vas da pogledate njihovu specifičnu dokumentaciju o LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


Kada niste zainteresovani za tehničke stvari i ne želite da hostujete svoj izvor finansiranja niti svoj lnbits, postoji [LNbits SaaS verzija](https://saas.lnbits.com) (Softver-kao-usluga) koju možete koristiti. To je u osnovi kao LNbits u oblaku, ali možete sami definisati izvor finansiranja (npr. vaš Node, LNbits Wallet, LNtipbot, fakewallet itd.) i promenljive okruženja - što uglavnom nije slučaj kod drugih cloud-rešenja.


[Evo detaljnog vodiča kako koristiti LNbits SaaS za specifične slučajeve upotrebe](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## Izvori finansiranja


LNbits nije softver za upravljanje čvorovima već računovodstveni sistem fokusiran na LN na vrhu LND ili CLN izvora finansiranja. Nakon prve instalacije možete posetiti vaš LNbits na http://localhost:5000/.


Da biste izmenili izvor finansiranja, idite na svoj super-user-URL i izaberite izvor finansiranja unutar "Manage Server" ili uredite .env fajl tako što ćete izmeniti `LNBITS_BACKEND_WALLET_CLASS` na željeni izvor ako ste postavili `adminUI=TRUE` u `.env`.


Pronaći ćete .env datoteku unutar vaše lnbits/ ili lnbits/apps/data fascikle proširivanjem komande za listanje datoteka u vašem direktorijumu pomoću `ls -a`.


Možda ćete takođe morati da instalirate dodatne pakete ili izvršite dodatne korake podešavanja, birajući željeni izvor finansiranja. Nakon ponovnog pokretanja, vaša nova podešavanja će biti aktivna.


Koje izvore finansiranja mogu koristiti za LNbits?


LNbits može raditi na mnogim izvorima finansiranja lightning-mreže. Trenutno postoji podrška za CoreLightning, LND, LNbits, LNPay, OpenNode, a redovno se dodaju novi.

Važno je odabrati izvor koji ima dobru likvidnost i dobre povezane partnere. Ako koristite LNbits za javne usluge, plaćanja vaših korisnika mogu tek tada teći srećno u oba smera.


Backend Wallet (izvor finansiranja) može se konfigurisati korišćenjem sledećih LNbits promenljivih okruženja u `.env` fajlu ili unutar vašeg superkorisničkog naloga u odeljku Upravljanje-serverom.

Ako želite da koristite .env verziju, parametre možete pronaći ovde:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-RPC
- Spark (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon or Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_adresa
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon or Bech64/Hex

Takođe možete koristiti macaroon šifrovan AES-om (više informacija) umesto toga koristeći


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Da biste šifrovali svoj macaroon, pokrenite `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.


### LNbits (još jedna LNbits instanca)



- LNbits instanca hostovana na cloud serveru ili vašem sopstvenom kućnom serveru
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! Ne KORISTITE ovaj za proizvodne / komercijalne svrhe, samo za testiranje !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot


Da povežete svoj [Lightning Tipbot](https://t.me/LightningTipBot) sa Telegramom, potrebno je da postavite sledeći parametar:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: Da biste dobili ključ, potrebno je da jednom pokrenete /api u privatnom četu sa LightningTipbot-om na Telegramu.


Takođe pogledajte ovaj vodič kako instalirati [LNbits sa LightningTipBot preko vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### IBEX HUB


Registrujte se [ovde](https://ibexpay.ibexmercado.com/onboard) zatim preuzmite svoje ključeve/token-e odatle, krajnja tačka je https://ibexpay-api.ibexmercado.com.

Više informacija pogledajte [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


### LNPay

Da bi Invoice listener radio, morate imati javno dostupnu URL adresu u vašem LNbits i postaviti [LNPay webhook](https://dashboard.lnpay.co/webhook/) koji pokazuje na `<your LNbits host>/Wallet/webhook` sa događajem "Wallet Receive" i bez datog tajnog ključa. Postavka `https://mylnbits/Wallet/webhook` će biti krajnja URL adresa koja će biti obaveštena o svakoj uplati.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Da bi Invoice radio, potrebno je da imate javno dostupnu URL adresu u vašem LNbits. Podešavanje webhook-a je opcionalno.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby je ekstenzija za pregledač sa funkcionalnostima LN Wallet i LNDHUB nalogom koji se može koristiti kao izvor finansiranja za LNbits. [Više detalja ovde](https://getalby.com/).


Da bi Invoice radio, morate imati javno dostupnu URL adresu u vašem LNbits. Ručno postavljanje webhook-a nije potrebno. Možete generate Alby pristupni token ovde: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## Dodatni / Vodiči za rešavanje problema


Evo nekoliko dodatnih uputstava u slučaju da su vam potrebna. Kliknite na strelicu da biste proširili opis.


### The Killswitch 🚨


U poslednje vreme bilo je mnogo opasnih grešaka ne samo u celom prostoru već i u LNbits, pa smo odlučili da nešto preduzmemo po tom pitanju. Sada možete da se prijavite za upozorenja i/ili da preduzmete direktne mere kada se ponovo pojavi ranjivost ili greška koja bi mogla dovesti do gubitka sredstava.


![killswitchn](assets/lnbits-killswitch.webp)


Ako se prebaci na void-Wallet, svi tipovi korisnika na instanci će videti žuti baner tamo gde biste inače našli obaveštenje "LNbits je u Beta fazi" pored oblasti za temu/jezik gore desno - i to je najočigledniji nagoveštaj da se nešto dogodilo. Pogledajte vaš novi server-tab istaknut u Green u levom delu prozora.


Kako to funkcioniše? Kada je killswitch omogućen, tajni GitHub repozitorijum dostupan samo LNbits core timu će biti proveravan u intervalu od X minuta (koji može biti specificiran). Ako je ranjivi bug objavljen u ovom repozitorijumu, to služi kao signal koji aktivira killswitch na svim instalacijama koje su pretplaćene i prelazi vašu lnbits instancu na korišćenje void Wallet. Ako su se oblaci razišli i instalirali ste sigurnosnu nadogradnju, možete ponovo postaviti vaš izvor finansiranja na vaš čvor, Wallet ili šta god da koristite, takođe putem sekcije Manage Server. Ovaj wiki ima sekciju o promeni izvora finansiranja ako ne znate šta da konfigurišete.



### Razlika između admina i superusera


LNbits Admin UI vam omogućava da promenite LNbits postavke putem LNbits frontend-a. Podrazumevano je onemogućeno i prvi put kada postavite promenljivu okruženja `LNBITS_ADMIN_UI=true` u `.env` fajlu, postavke se inicijalizuju i biće korišćene. Od tog trenutka se koriste odgovarajuće postavke iz baze podataka umesto onih iz .env fajla.


### Super User


Sa Admin UI smo uveli super korisnika koji ima pristup serveru tako da može menjati postavke koje mogu srušiti server ili učiniti ga neodgovarajućim putem frontend-a i API-ja, kao npr. menjanje izvora finansiranja. Super korisnik je smešten samo unutar tabele postavki baze podataka. Nakon što se postavke "resetuju na podrazumevane" i ponovo pokrenu, kreira se novi super korisnik. Takođe smo dodali dekorator za API rute da proveri postojanje super korisnika. Njegov ID se nikada ne šalje preko API-ja i frontend-a i samo prima bool (da/ne) da li ste super korisnik ili ne.


Samo super korisnik sme da brrrr satoshije na različite novčanike putem odeljka "Top Up".


Možete takođe poslati super korisnika putem webhoka na drugu uslugu kada je kreiran. Više informacija ovde https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


Na frontend-u ćete takođe pronaći mogućnost promene slike prodavnice koja se prikazuje na stranici "create Wallet" otvaranjem sekcije Manage Server i izborom Theme -> Custom Logo.


### Admin Users


Enviroment varijabla: `LNBITS_ADMIN_USERS`, lista ID-ova korisnika odvojena zarezima. Admin korisnici mogu menjati podešavanja u admin ui - sa izuzetkom podešavanja izvora finansiranja, jer bi to zahtevalo restart servera i potencijalno moglo učiniti server nedostupnim. Takođe, imaju pristup svim ekstenzijama posvećenim njima u `LNBITS_ADMIN_EXTENSIONS`.


### Dozvoljeni korisnici


Promenljiva okruženja: `LNBITS_ALLOWED_USERS`, lista ID-ova korisnika odvojena zarezima. Definisanjem ovih korisnika LNbits više neće biti dostupan javnosti. Samo definisani korisnici i administratori mogu tada pristupiti LNbits interfejsu.




#### Ažuriraj LNbits

Normalno ažuriranje vaše lokalne instance LNbits jednostavno je kopiranjem i lepljenjem sledećih CLI komandi:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Ako koristite Raspiblitz ili MyNode, možda će vam dodatno trebati

```
sudo systemctl restart lnbits
```

na kraju, jer pokreće LNbits kao uslugu.


Na Umbrel/Citadel komande bi bile

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### Migracija sa SQLite na PostgreSQL


Ako već imate instaliran i pokrenut LNbits na SQLite bazi podataka, toplo preporučujemo migraciju na postgres ako planirate da pokrećete LNbits u većem obimu.


Uključen je skript koji može lako izvršiti migraciju. Potrebno je da već imate instaliran Postgres i da postoji lozinka za korisnika (pogledajte vodič za instalaciju Postgres iznad). Pored toga, vaša LNbits instanca treba da se pokrene jednom na postgresu kako bi implementirala bazu podataka Schema pre nego što migracija može da funkcioniše:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Nadam se da sada sve radi i da je migrirano... Ponovo pokreni LNbits i proveri da li sve funkcioniše ispravno.



#### Bekap i obnova baze podataka


Molimo pogledajte [ovaj veoma detaljan vodič o procesu pravljenja rezervnih kopija i vraćanja podataka](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).



#### Finansiranje mog LNbits Wallet sa mog čvora ne radi


Ako želite poslati Sats sa istog čvora koji je izvor finansiranja vašeg LNbits, potrebno je da uredite LND.conf datoteku.


Parametri koji treba da budu uključeni su: `allow-circular-route=1`


Molim vas, uradite to u odeljku Application options vašeg LND.conf. Na nekim čvorovima snopa pokretanje LND bi moglo da ne uspe inače.


NAPOMENA: Preporučuje se da umesto toga koristite novu adminUI ekstenziju sa opcijom "TopUp" za dodavanje sredstava na LNbits nalog.


#### Greška 426

Dobio sam grešku: "lnurl treba da bude isporučen preko javno dostupnog https domena ili tor. 426 upgrade required"


Ova greška obično se javlja jer vaš LNbits iza ngnix tunela ne prosleđuje ispravno LNURL Address. Zaustavite vaš LNbits i uredite .env datoteku dodajući ovu liniju:

`FORWARDED_ALLOW_IPS=*`


Takođe, ako koristite ngnix podešavanje, budite sigurni da imate ove zaglavlja u ngnix konfiguraciji:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### Greška mreže

Dobio sam "https error", "network error" ili druge greške prilikom skeniranja QR koda</summary>


Loše vesti, ovo je greška u rutiranju koja može imati dosta razloga. Prvo proverite QR-ov LNURL sa [Lightning Decoder](https://lightningdecoder.com/) da li možete pronaći nešto čudno tamo. Hajde da pokušamo nekoliko najverovatnijih problema i njihovih rešenja.


LNbits radi samo putem Tor-a, ne možete ga otvoriti na javnoj domeni kao što je lnbits.yourdomain.com



- S obzirom na to da želite da vaš setup ostane ovakav, otvorite vaš LNbits Wallet koristeći .onion URI i kreirajte ga ponovo. Na ovaj način QR kod je generisan da bude dostupan putem ovog .onion URI, dakle samo putem tor-a. Nemojte generate taj QR sa .local URI, jer neće biti dostupan putem interneta - samo unutar vašeg kućnog LAN-a.
- Otvorite svoju LN Wallet aplikaciju koju ste koristili za skeniranje tog QR koda i ovog puta koristite tor (pogledajte postavke Wallet aplikacije). Ako aplikacija ne nudi tor, možete koristiti Orbot (Android) kao alternativu. Pogledajte odeljak za instalaciju za detaljna uputstva o tome kako otvoriti svoj LNbits za clearnet/https.



#### Sprečite druge da generišu novčanike na mom LNbits-u


Kada pokrećete svoj LNbits na clearnet-u, u suštini svako može generate na Wallet na njemu. Pošto su sredstva vašeg čvora vezana za ove novčanike, možda ćete želeti da to sprečite. Postoje dva načina da to uradite:


Konfigurišite dozvoljene korisnike i ekstenzije u `.env` fajlu ([pogledajte primer env ovde](https://github.com/lnbits/lnbits/blob/main/.env.example)). Ovo funkcioniše samo ako koristite podešavanje `adminUI=FALSE` u .env, u suprotnom to morate uraditi u odeljku Upravljanje Serverom -> Korisnici -> Dozvoljeni Korisnici. Svi ostali neće biti dozvoljeni nakon toga.




#### Prilagodite vremenski okvir isteka Invoice


Sada možete generate fakture sa prilagođenim istekom. Kompatibilno sa backend-ovima: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet za sada!


Možete postaviti `LIGHTNING_INVOICE_EXPIRY` u vašoj .env datoteci ili koristiti AdminUI da promenite podrazumevanu vrednost za sve fakture. Takođe postoji novo polje u /api/v1/payments endpointu gde možete postaviti isteknuće u JSON podacima.




## Wallet-URL izbrisano


### Wallet na demo serveru legend.lnbits


Uvek sačuvajte kopiju vašeg Wallet-URL, Export2phone-QR ili LNDhub za vaše sopstvene novčanike na sigurnom mestu. LNbits NE MOŽE da vam pomogne da ih povratite kada se izgube.


### Wallet na vašem sopstvenom izvoru finansiranja/čvoru

Uvek sačuvajte kopiju vašeg Wallet-URL, Export2phone-QR ili LNDhub za vaše sopstvene novčanike na sigurnom mestu. Sve LNbits korisnike i Wallet-ID možete pronaći u vašem LNbits menadžeru korisnika ili u vašoj sqlite bazi podataka. Da biste uredili ili pročitali LNbits bazu podataka, idite u LNbits /data folder i potražite fajl pod nazivom sqlite.db. Možete ga otvoriti i urediti pomoću excela ili sa posvećenim SQL-Editorom kao što je [SQLite browser](https://sqlitebrowser.org/).


Takođe možete preuzeti novčanike putem CLI i pregledati svaki Wallet unutar vaše baze podataka.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


Izlaz će izgledati otprilike ovako


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

i želite da stavite ove vrednosti u URL kao ovo


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Gde zamenjujete f8a43fc363ea428db5c53b3559935f1f sa vrednošću koja dolazi pre imena (u našem primeru f8a43fc363ea428db5c53b3559935f1f) i 1280ff5910a9c485a782a2376f338b6c je vaš korisnik i treba da postane vrednost prikazana posle imena. Da biste izašli iz sqlite3 unesite


```
.quit
```

#### LNURL za lightning-Address obrnuto


Pokušajte ovaj [enkoder](https://lnurl-codec.netlify.app/) od fiatjaf ili [ovaj](https://lightningdecoder.com/). Za plaćanje ili proveru LNURLp možete takođe koristiti [LNurlpay](https://wwww.lnurlpay.com/). Trebalo bi da bude HTTPS, a ne HTTP.



#### Podesite komentar koji će ljudi videti kada plaćaju putem mog LNURLp QR-a.

Kada kreirate LNURL-p, po defaultu polje za komentar nije popunjeno. To znači da komentari nisu dozvoljeni da budu priloženi uz uplate.


Da biste omogućili komentare, dodajte dužinu karaktera okvira, od 1 do 250. Kada unesete broj, okvir za komentare će biti prikazan u procesu plaćanja. Takođe možete urediti već kreirani LNURL-p i dodati taj broj.


![lnbits comments](assets/lnbits-comments.webp)


#### Depozitujte onchain BTC na LNbits

Postoje dva načina za Exchange Sats sa onchain BTC na LN BTC (odnosno na LNbits).


##### Putem spoljnog servisa za zamenu.


Drugi korisnici koji nemaju pristup vašem LNb mogu koristiti uslugu zamene kao što su [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) ili [ZigZag](https://zigzag.io/). Ovo je korisno ako pružate samo LNURL/LN fakture iz vaše LNbits instance, ali platiša ima samo onchain Sats pa će morati prvo da zamene te Sats na svojoj strani. Procedura je jednostavna: korisnik šalje onchain btc usluzi zamene i pruža LNURL / LN Invoice iz LNbits kao odredište zamene.


##### Korišćenje Onchain i Boltz LNbits ekstenzije.


Imajte na umu da je ovo zaseban Wallet, a ne LN btc koji je predstavljen od strane LNbits kao "vaš Wallet" na vašem LN izvoru finansiranja. Ovaj onchain Wallet se takođe može koristiti za zamenu LN btc u (npr. vaš hardverski novčanik) korišćenjem LNbits Boltz ili Deezy ekstenzije. Ako vodite veb prodavnicu koja je povezana sa vašim LNbits za LN uplate, veoma je korisno redovno prebacivati sve Sats sa LN u onchain. Ovo vodi ka više prostora u vašim LN kanalima kako biste mogli primati nove sveže Sats.


Procedura za one bez Bitcoin Hardware Wallet:



- Koristite Electrum ili Sparrow Wallet da kreirate novi onchain Wallet i sačuvajte rezervnu kopiju seed na sigurnom mestu.
- Idite na Wallet informacije i kopirajte xpub.
- Idite na LNbits - Onchain ekstenziju i kreirajte novi Watch-only wallet sa tim xpub.
- Idite na LNbits - Tipjar ekstenziju i kreirajte novi Tipjar. Izaberite i onchain opciju pored LN Wallet.
- Opcionalno - Idite na LNbits - SatsPay ekstenziju i kreirajte novu naplatu za onchain btc. Možete izabrati između onchain i LN ili oba. Tada će kreirati Invoice koji se može deliti.
- Opcionalno - Ako koristite svoj LNbits povezan sa Wordpress + Woocommerce stranicom, kada kreirate/povežete Watch-only wallet sa vašom LN btc prodavnicom Wallet, kupac će imati obe opcije za plaćanje na istom ekranu.


Kada primite uplatu u LNbits, dnevnik transakcija će prikazati samo sažeti tip transakcije.


![lnbits payment details](assets/lnbits-payment-details.webp)


U pregledu transakcija pronaći ćete malu strelicu Green za primljena sredstva i crvenu strelicu za sredstva koja su poslana.


Ako kliknete na te strelice, iskačući prozor sa detaljima prikazuje priložene poruke kao i ime pošiljaoca, ako je dato.


Da biste konfigurisali ime koje će se pojaviti unutar plaćanja, u LNbits trenutno nije moguće to učiniti - ali da biste primili. Ovo je moguće samo ako pošiljalac LN Wallet podržava [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) kao [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).


Videćete zatim alias/pseudonim u odeljku sa detaljima vaših LNbits transakcija (kliknite na strelice). Imajte na umu da tamo možete dati bilo koje ime i da ono možda neće biti povezano sa pravim imenom pošiljaoca ako takvo primite.


![lnbits namedesc](assets/lnbits-namedesc.webp)


Da biste uvezli svoj LNbits nalog u Wallet aplikaciju, otvorite svoj LNbits sa nalogom / Wallet koji želite da koristite, idite na "upravljanje ekstenzijama" i aktivirajte LNDHUB ekstenziju. Otvorite LNDHUB ekstenziju, izaberite Wallet koji želite da koristite i skenirajte ili "admin" ili "samo Invoice" QR, u zavisnosti od nivoa sigurnosti koji želite za taj Wallet.


Možete koristiti [Zeus](https://zeusln.app/) ili [Bluewallet](https://bluewallet.io/) kao Wallet aplikacije za lndhub nalog pri čemu BW podržava više od jednog takvog Wallet.


Kada to radite, preporučujemo da takođe postavite URI mreže LN na onaj vašeg sopstvenog čvora. Ako je vaša LNbits instanca samo na Toru, takođe morate koristiti te aplikacije sa aktiviranim Torom. Takođe, u ovom slučaju morate otvoriti LNbits stranicu preko vašeg Tor .onion Address.


Ako imate grešku "unsupported Hash type" kada koristite ypub u On-Chain ekstenziji, proverite da li vaša LNbits instanca koristi python 3.10 jer bi mogla biti pogođena [ovim problemom](https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Izmenite openssl.cnf kao što je opisano u stackoverflow odgovoru i restartujte vaš LNbits.



## Alati i izgradnja sa LNbits


LNbits ima sve vrste [otvorenih API-ja](https://legend.lnbits.com/docs) i alata za programiranje i povezivanje sa mnogo različitih uređaja za bezbroj slučajeva upotrebe.


Kada ste novi u izgradnji, počnite sa ovim [MakerBits prezentacijama](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) od Ben Arc-a o izgradnji gedžeta baziranih na LNbits.


### VAŽNO:


- LNbits radi na osnovu LNURL protokola čiji su zahtevi validni u dva oblika: ili kao https:// clearnet link (nisu dozvoljeni samopotpisani sertifikati) ili kao http:// v2/v3 onion link. Da biste ponudili LNbits usluge kao što su LNURLp/w QR kodovi ili NFC kartice, koje mogu biti korišćene na terenu, potrebno je da otvorite LNbits za clearnet (https).
- Koristite samo DATA-kablove za napajanje vašeg esp32. Nisu svi kablovi podržavaju prenos podataka pored napajanja esp-a. Ne biste bili prvi ako je kabl koji ste dobili uz esp samo za napajanje.
- Obavezno nemojte koristiti USB-Hub sa drugim priključenim uređajima. Ovo može dovesti do čudnih efekata koji su Hard za otklanjanje grešaka (npr. ne pokretanje ili zaustavljanje).
- Da biste realizovali esp projekte sa MacOS-om, biće vam potreban UART Bridge Driver. Ako imate problema sa drajverom na Mac ili Linux sistemima, možete ih pronaći ovde ili, ako je uključen TTGO Display, ovaj ovde. Ako ste na Windows-u i imate problema sa povezivanjem, obavezno preuzmite STARU verziju 11.1.0 jer novija ne radi! Takođe možete pronaći serijski terminal ovde da proverite vašu konekciju - postavite na baudrate 115200.
- Iako je mnogo udobnije koristiti Platform.io (npr. zavisnosti se instaliraju automatski), preporučujemo korišćenje Arduina za sve koji su novi u izradi.
- TT-Go Display S3: Boja jezička zaštitne folije ekrana govori vam koji kontroler tačno (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) je korišćen za izradu. Sačuvajte ga kako biste mogli da otklonite greške ako sami programirate, a ekran ne prikazuje grafiku ispravno, npr. pogrešne boje, zrcaljene slike ili raspršene piksele na ivicama. Ako ikada budete morali to da uradite, postoji epski vodič za prilagođavanje različitim ekranima.
- Uvek koristi lowercase lnurl239xx umesto LNURLl239xx
- Dodavanje lightning:lnurl1234xyz će kreirati QR koji zahteva otvaranje korisničkog Wallet za ovaj Invoice pri skeniranju (poslednja instalirana lightning aplikacija na iOS-u, podešavanje na Androidu)
- Ako flešujete esp32 putem veba, to će raditi samo sa ovim pregledačima (TL:DR Chrome, Edge & Opera).
- Imajte na umu ovu referencu PIN-OUT za esp
- Kada koristite FOSSoftware ili FOSGuides, molimo vas da uvek navedete autora. Svi vole da gledaju kako njihova "beba" raste, a to takođe pokreće lanac izgradnje koji je prilično sjajan za gledanje:)


Dođite u [Makerbits Telegram Grupu](https://t.me/makerbits) ako vam treba pomoć sa projektom - tu smo za vas!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


Evo nekoliko kategorija projekata koje možete izgraditi sa LNbits:



- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [Aparat za prodaju](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora i Mesh umrežavanje](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [POMOĆNICI I RESURSI](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Više primera projekata "Powered by LNbits" ovde](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Upotreba za LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)