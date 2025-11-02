---
name: LNbits Server
description: Instalacija i konfiguracija samostalno hostovanog LNbits servera na Ubuntu VPS sa PHOENIXD ili na Umbrel
---

![cover](assets/cover.webp)



LNbits je open source Interface web aplikacija koja transformiše bilo koji Lightning backend (LND, Core Lightning, PHOENIXD) u kompletnu servisnu platformu. Ovo rešenje koje sami hostujete omogućava vam da upravljate višestrukim Lightning portfolijima u izolaciji, postavljate prodajna mesta, kreirate sisteme za donacije ili usluge naplate, dok zadržavate potpunu kontrolu nad vašim sredstvima.



Ovaj vodič pokriva dva pristupa instalaciji: **VPS Ubuntu sa PHOENIXD** (lagano rešenje bez pune Bitcoin nod) i **Umbrel** (integracija sa vašim postojećim LND nodom). Za razliku od opšteg LNbits vodiča Plan B Network-a, koji pokriva pojmove i ekstenzije, ovaj vodič se fokusira na tehničke procedure instalacije korak po korak.



## Šta je LNbits?



LNbits je Lightning računovodstveni sistem razvijen u Pythonu (FastAPI) koji se povezuje sa postojećim backendom (LND, Core Lightning, PHOENIXD). Za razliku od tradicionalnih Lightning čvorova, LNbits nudi pristupačan Interface, omogućavajući vam upravljanje sa nekoliko izolovanih portfolija sa sopstvenim API ključevima. Možete kreirati podračune za svoju porodicu, zaposlene ili projekte, bez davanja pristupa svim vašim sredstvima.



Decoupled arhitektura čuva informacije u SQLite (podrazumevano) ili PostgreSQL (produkcija), dok sredstva ostaju upravljana od strane vašeg Lightning backend-a. Ovo razdvajanje garantuje prenosivost: možete migrirati sa PHOENIXD na LND bez gubitka korisničkih podataka.



## Ključne karakteristike



LNbits nudi svestran **sistem ekstenzija**: TPoS (prodajno mesto), Paywall (monetizacija sadržaja), Events (prodaja karata), LndHub (server za BlueWallet), Bolt Cards (NFC plaćanja), Split Payments (automatska distribucija), i User Manager (upravljanje korisnicima sa autentifikacijom).



**Dashboard** prikazuje stanja u realnom vremenu, istoriju transakcija i alate za naplatu. Svaki Wallet ima jedinstveni URL koji sadrži njegove API ključeve, omogućavajući pristup bez tradicionalnog prijavljivanja. Troslojni API sistem ključeva** (admin, Invoice, samo za čitanje) nudi detaljnu kontrolu dozvola za sigurne integracije.



LNbits nativno implementira **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) i podržava **Lightning Address**, garantujući kompatibilnost sa modernim Lightning novčanicima i olakšavajući implementaciju profesionalnih usluga.



## Podržane platforme



**Ubuntu VPS**: Lako rešenje bez pune Bitcoin čvorne tačke. Preduslovi: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + naziv domena potreban za javnu izloženost (LNURL usluge).



**Umbrel**: Laka instalacija iz App Store-a. Preduslov: funkcionalan Umbrel čvor sa sinhronizovanim LND i otvorenim kanalima. Automatska konfiguracija.



Ispod su linkovi ka našim tutorijalima za Umbrel i Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalacija na Ubuntu VPS sa PHOENIXD



### Korak 1: Obezbeđivanje VPS servera



**Pre nego što bilo šta instalirate**, potrebno je da obezbedite vaš Ubuntu VPS server u skladu sa pravilima struke. Ovaj korak je **kritičan** za zaštitu vaše infrastrukture i vaših Lightning sredstava.



Evo detaljnog vodiča koji će vam pomoći da započnete: **[Početna konfiguracija Ubuntu servera - Vodič korak po korak](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** autora Daniel P. Costas.



Ovaj vodič pokriva korisničku konfiguraciju, siguran SSH, firewall (UFW), fail2ban, automatska ažuriranja i dobre prakse sigurnosti sistema.



### Korak 2: Instaliranje PHOENIXD



Kada je vaš server siguran, potrebno je instalirati i konfigurisati PHOENIXD. Plan B Network nudi kompletan posvećen vodič koji pokriva instalaciju, generisanje seed i konfiguraciju systemd servisa:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Once PHOENIXD is up and running (check with `./Phoenix-CLI getinfo`), note the **HTTP password** in `~/.Phoenix/Phoenix.conf` - you'll need it to connect LNbits to PHOENIXD.



### LNbits implementacija



Instaliraj UV i kloniraj LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurišite pozadinski sistem PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Dodaj u `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Testiraj sa `uv run lnbits --host 0.0.0.0 --port 5000` zatim kreiraj systemd servis sa `Wants=PHOENIXD.service`.



## Početno podešavanje i prva upotreba



### SuperUser aktivacija



Aktivirajte Interface administratora u `.env` :


```
LNBITS_ADMIN_UI=true
```



Ponovo pokrenite LNbits (`sudo systemctl restart lnbits`) i preuzmite SuperUser ID:


```bash
cat ~/lnbits/data/.super_user
```



Idite na `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` za administratorski panel. Meni "Server" vam omogućava da konfigurišete izvore finansiranja, ekstenzije i korisničke naloge.



### Sigurno kreiranje naloga



**Važno za javno izlaganje**: Ako izlažete vašu LNbits instancu na javnom domenskom imenu dostupnom sa Interneta, **kritično** je da onemogućite besplatno kreiranje korisničkih naloga.



Iz administracije SuperUser Interface, idite na "Podešavanja" a zatim na odeljak "Upravljanje korisnicima". Pronaći ćete opciju "Dozvoli kreiranje novih korisnika".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Za javnu izložbu sa domenom** :




- Morate onemogućiti** opciju "Dozvoli kreiranje novih korisnika"
- Bez ove zaštite, bilo ko na Internetu može kreirati nalog na vašoj instanci.
- Napadač bi mogao kreirati naloge i koristiti likvidnost vašeg LIGHTNING NODE bez vašeg znanja.
- Moraćete ručno da kreirate korisničke naloge sa Interface SuperUser



**Za lokalnu upotrebu samo** :




- Ova opcija je manje kritična ako je vaša instanca dostupna samo lokalno (http://localhost:5000)
- Međutim, onemogućavanje ove opcije je dobra opšta bezbednosna praksa



Jednom kada se konfiguriše, samo SuperUser administrator može kreirati nove korisničke naloge putem Interface "Korisnici". Ovaj pristup garantuje potpunu kontrolu nad tim ko može pristupiti vašoj Lightning infrastrukturi i koristiti vaša sredstva.



### Otvaranje prvog kanala



PHOENIXD automatski upravlja kanalima putem auto-likvidnosti. generate a Lightning Invoice od ~30,000 Sats iz LNbits i plati ga sa drugog Wallet. PHOENIXD automatski otvara kanal ka ACINQ. Naknada za otvaranje (~20-23k Sats) se odbija, preostali saldo (~7-10k Sats) se pojavljuje nakon On-Chain potvrde.



Proveri status pomoću `./Phoenix-CLI getinfo`. Zatim razmotri onemogućavanje automatske likvidnosti (`auto-liquidity=off` u `Phoenix.conf`) kako bi kontrolisao otvaranje kanala.



### Javni prikaz i HTTPS



**Važno**: HTTPS obavezan za javno prikazivanje (API sigurnost ključa + LNURL kompatibilnost). Preskočite ovaj korak samo za lokalnu upotrebu.



**Caddy (preporučeno)**: automatski SSL. `sudo apt install -y caddy`, izmenite `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Ponovno pokretanje: `sudo systemctl restart caddy`.



**Nginx** : Više kontrole. Instalirajte `nginx certbot python3-certbot-nginx`, kreirajte `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktiviraj: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Dodajte u `.env`: `FORWARDED_ALLOW_IPS=*`



## Instalacija Umbrel



### Distribucija sa App Store-a



Idite u Umbrel App Store, potražite "LNbits" i kliknite na "Install".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel automatski proverava potrebne zavisnosti. LNbits zahteva LIGHTNING NODE (LND) za rad. Ako je vaš LIGHTNING NODE već operativan, kliknite na "Install LNbits" da potvrdite.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel preuzima Docker sliku, automatski konfiguriše veze sa LND i pokreće kontejner (2-5 minuta). Instalacija se odvija u potpunosti u pozadini.



### Početna konfiguracija SuperUser-a



Prilikom prvog pokretanja, LNbits vas poziva da kreirate SuperUser administratorski nalog. Unesite korisničko ime i postavite sigurnu lozinku kako biste zaštitili pristup Interface administrativnom sistemu.



![Configuration SuperUser](assets/fr/03.webp)



**Važno**: Ovaj SuperUser nalog ima potpune privilegije na vašoj LNbits instanci. Izaberite jaku lozinku i čuvajte je na sigurnom.



Kada kreirate nalog, automatski ćete biti preusmereni na glavnu administrativnu oblast Interface. Umbrel je već postavio LND kao vaš izvor finansiranja - sva Lightning plaćanja će ići kroz vaše postojeće kanale.



### Pristup administratoru Interface



U levom meniju kliknite na "Settings" da biste pristupili celom administrativnom panelu.



![Interface Settings](assets/fr/04.webp)



Odsek "Wallets Management" prikazuje ključne informacije o vašoj konfiguraciji:




- Funding Source** : LndBtcRestWallet (direct connection to your LND Umbrel node)
- Ravnoteža Čvora** : Ukupna likvidnost dostupna u vašim Lightning kanalima
- Stanje LNbits**: Sredstva dodeljena LNbits sistemu (u početku 0 Sats)



Sada možete direktno iskoristiti likvidnost vašeg Umbrel čvora za sve LNbits novčanike koje kreirate. Nije potrebna dodatna konfiguracija - LNbits je pokrenut i radi.



### Upravljanje korisnicima



Jedna od najmoćnijih karakteristika LNbits-a je njegova sposobnost da kreira više nezavisnih korisnika, svaki sa autentifikacijom lozinkom i izolovanim novčanicima. Ova arhitektura omogućava iskorišćavanje likvidnosti vašeg Umbrel čvora dok nudi potpuno izolovane podračune za različite namene: posao, porodica, zaposleni, projekti, itd.



U bočnom meniju kliknite na "Korisnici" da biste pristupili upravljanju korisnicima. Kliknite na "KREIRAJ NALOG" da biste dodali novog korisnika.



![Gestion des utilisateurs](assets/fr/05.webp)



Popunite obrazac za kreiranje korisnika:




- Korisničko ime**: Korisničko ime za prijavu (primer: "Satoshi")
- Postavi lozinku**: Aktivirajte ovu opciju da postavite lozinku za autentifikaciju
- Lozinka** i **Ponovi lozinku**: Postavite lozinku za ovog korisnika



![Création utilisateur satoshi](assets/fr/06.webp)



Opciona polja (Nostr javni ključ, Email, Ime, Prezime) mogu ostati prazna za minimalnu konfiguraciju. Kliknite na "CREATE ACCOUNT" da potvrdite.



![Confirmation utilisateur créé](assets/fr/07.webp)



Vaš novi korisnik se sada pojavljuje na listi korisnika sa svojim jedinstvenim identifikatorom i korisničkim imenom.



![Liste des utilisateurs](assets/fr/08.webp)



**Važna tačka**: Svaki korisnik može da se prijavi potpuno nezavisno sa sopstvenom lozinkom. SuperUser administrator zadržava punu kontrolu putem Interface administrativnog alata.



### Upravljanje korisnikom Wallet



Sada kada je korisnik "Satoshi" kreiran, potrebno je dodeliti mu Wallet Lightning. Kliknite na ikonu Wallet (druga ikona) za dotičnog korisnika, zatim na "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



Dijalog okvir vas poziva da imenujete Wallet. Unesite opisni naziv (npr. "Wallet Od Satoshi") i izaberite valutu prikaza (CUC, USD, EUR, itd.).



![Création wallet](assets/fr/10.webp)



Kliknite na "CREATE". LNbits trenutno generiše radni Wallet Lightning za ovog korisnika.



![Confirmation wallet créé](assets/fr/11.webp)



Sada vidite dva postojeća novčanika: podrazumevani Wallet "LNbits Wallet" kreiran automatski, i novi "Wallet Of Satoshi". Da biste pojednostavili korisničko iskustvo, možete obrisati podrazumevani Wallet klikom na ikonu za brisanje (crvena kanta za smeće).



![Wallet final unique](assets/fr/12.webp)



Korisnik "Satoshi" sada ima jedan, jasno identifikovan Wallet. Svaki korisnik Wallet radi potpuno autonomno, dok koristi likvidnost vašeg osnovnog LND čvora.



**Ključni koncept**: Svi ovi novčanici dele globalnu likvidnost vašeg Umbrel čvora. Ne kreirate nove Lightning kanale za svaki Wallet - LNbits deluje kao inteligentni računovodstveni Layer koji upravlja raspodelom sredstava unutar vaše postojeće Lightning infrastrukture. To je moć LNbits-ovog multi-Wallet sistema.



### Prijava korisnika



Odjavite se sa SuperUser naloga (ikona gore desno) i vratite se na LNbits stranicu za prijavu. Sada se možete prijaviti sa podacima novog korisnika.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Unesite korisničko ime ("Satoshi") i prethodno definisanu lozinku, zatim kliknite na "LOGIN". Korisnik dobija direktan pristup svom ličnom Wallet, potpuno izolovanom od administracije Interface.



### Interface od Wallet korisnik



Kada se poveže, korisnik pristupa svom Interface sa Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Interface karakteristike :




- Trenutno stanje**: Prikazano u Sats i u odabranoj valuti (CUC u ovom primeru)
- Glavne akcije**: "ZALEPI ZAHTEV" (zalepi račun za plaćanje), "KREIRAJ Invoice" (generate priznanica), QR ikona (brzo skeniranje)
- Istorija transakcija** : Kompletna lista svih uplata i isplata
- Desna strana panela**: Opcije konfiguracije i pristupa



### Wallet mobilni pristup



Desna bočna tabla nudi posebno praktičnu funkciju: mobilni pristup Wallet. Otvorite odeljak "Mobilni Pristup" da biste otkrili dostupne opcije.



![Mobile Access](assets/fr/15.webp)



LNbits nudi nekoliko načina za korišćenje ovog Wallet na pametnom telefonu:



**Opcija 1: Kompatibilne mobilne aplikacije




- Preuzmite **Zeus** ili **BlueWallet** sa App Store-a ili Google Play-a
- Aktiviraj ekstenziju **LndHub** u LNbits za ovaj Wallet
- Skenirajte LndHub QR kod pomoću mobilne aplikacije da povežete Wallet



**Opcija 2: Direktan pristup putem mobilnog pregledača**




- QR kod prikazan u "Izvoz na telefon sa QR kodom" sadrži pun URL Wallet sa integrisanom autentifikacijom
- Skenirajte ovaj QR kod sa svog pametnog telefona da biste otvorili Wallet direktno u svom mobilnom pregledaču.
- Dodaj stranicu na početni ekran za brz pristup



**Važna sigurnost**: Ovaj URL sadrži API ključeve za potpuni pristup Wallet. Nikada ga ne delite javno. Tretirajte ovaj QR kod kao što biste tretirali svoje Bitcoin privatne ključeve - svako ko skenira ovaj QR kod dobija potpuni pristup Wallet.



Ova mobilna funkcija pretvara vašu LNbits Umbrel instancu u pravi Lightning Wallet server za vas i vaše prijatelje, dok zadržavate potpunu suverenost nad vašim sredstvima zahvaljujući vašem samostalno hostovanom čvoru.



### Deljenje pristupa korisnika



Glavna upotreba za ovu konfiguraciju sa više korisnika je **deljenje novčanika sa vašom porodicom ili bliskim krugom**. Kada kreirate korisnika sa posvećenim Wallet (kao što je "Satoshi" u našem primeru), možete podeliti ove pristupne podatke sa pouzdanim članovima vašeg domaćinstva.



**Pristup sigurnosti na Umbrelu**: Pristup vašoj LNbits instanci na Umbrelu je prirodno zaštićen, jer se može pristupiti samo :




- Na vašoj lokalnoj mreži** : Članovi vašeg domaćinstva povezani na istu WiFi/Ethernet mrežu mogu pristupiti instanci
- Putem VPN-a**: Ako koristite VPN kao što je Tailscale konfigurisan na vašem Umbrel serveru, ovlašćeni korisnici mogu dobiti siguran daljinski pristup



Ova dupla zaštita Layer (pristup mreži + autentifikacija korisnika) čini opciju "Dozvoli kreiranje novih korisnika" manje kritičnom na Umbrel-u. Samo osobe koje već imaju pristup vašoj mreži ili VPN-u mogu doći do Interface prijave.



**Tipičan scenario**: Kreirate nalog za "tatu", nalog za "mamu", nalog za "posao" i tako dalje. Svaki član porodice ima svoj izolovani Wallet Lightning, dok koristi zajedničku likvidnost vašeg Umbrel čvora. Jednostavno podelite korisničko ime i lozinku - korisnik se zatim može povezati sa bilo kog uređaja na vašoj lokalnoj mreži ili putem vašeg Tailscale VPN-a. Molimo vas da pogledate naš posvećeni Tailscale vodič za više informacija:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Istraži dostupna proširenja



Vratite se na Interface SuperUser i pristupite meniju "Extensions" u levom bočnom panelu da biste otkrili kompletan LNbits ekosistem ekstenzija.



![Extensions disponibles](assets/fr/16.webp)



LNbits nudi bogat katalog ekstenzija koje vašu instancu pretvaraju u pravi platformu za Lightning usluge:





- Jukebox**: Sats-pokretani jukebox sistem (Spotify plaćanja)
- Podrška Tiketi**: Plaćeni sistem podrške (primajte Satss za odgovaranje na pitanja)
- TPoS**: Siguran, mobilni terminal za prodajna mesta za trgovce
- User Manager**: napredno upravljanje korisnicima i Wallet (koji smo upravo koristili)
- Događaji**: Prodaja i validacija ulaznica za događaje
- LNURLDevices**: Upravljanje prodajnim mestima, bankomati, povezani prekidači
- SMTP**: Omogućite korisnicima slanje e-pošte i zaradu Sats
- Boltcards**: Programiranje NFC kartica za Lightning tap-to-pay plaćanja
- NostrNip5**: Kreirajte NIP5 adrese za vaše domene
- Splitpayments**: Automatska distribucija uplata između više novčanika



Svako proširenje se aktivira jednim klikom sa ovog Interface. Proširenja označena sa "BESPLATNO" su bez naknade, dok su neka dostupna kao "PLAĆENE" verzije. Istražite katalog kako biste identifikovali ona koja odgovaraju vašim potrebama - bilo za poslovanje, porodično upravljanje ili eksperimentisanje sa mogućnostima Lightning Network.



## Prednosti i ograničenja



**Prednosti**: Finansijski suverenitet (potpuna kontrola nad sredstvima/ključevima/podacima), arhitektonska fleksibilnost (migracija bez gubitaka VPS→Full node), profesionalni sistem proširenja, intuitivni Interface.



**Ograničenja** : Softver u beta verziji (oprez kod iznosa), sigurnost pod odgovornošću administratora, URL-ovi koji sadrže osetljive API ključeve (HTTPS obavezan), upravljanje više korisnika podrazumeva starateljsku odgovornost.



## Najbolje prakse



**Backups**: seed PHOENIXD/credentials LND, LNbits baza podataka, `.env` fajlovi. Automatizovati dnevno, čuvati van produkcionog servera, enkriptovano. Redovno testirati povratke.



**Održavanje**: Redovno proveravajte ažuriranja (LNbits, Lightning pozadinski sistem, operativni sistem). Uvek proverite beleške o izdanju pre većih ažuriranja.





- Na Umbrel**: Prodavnica aplikacija automatski vas obaveštava o novim verzijama. Sinhronizujte ekstenzije putem "Upravljanje ekstenzijama" > "Ažuriraj sve". Proverite uključivanje SQLite baze podataka u automatske rezervne kopije Umbrel-a.
- Na VPS**: Ažurirajte ručno sa `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Pratite sistemske logove: `sudo journalctl -u lnbits -f`.



## Zaključak



LNbits samohostovanje nudi konkretan put ka finansijskom suverenitetu uz Lightning. VPS+PHOENIXD nudi lagano rešenje za brze usluge, Umbrel punu integraciju sa postojećim Bitcoin čvorom. Skalabilna arhitektura omogućava evoluciju od jednostavnog multi-korisničkog Wallet do sofisticiranih poslovnih slučajeva.



Samostalno hostovanje podrazumeva odgovornost: napravite rezervne kopije seed-ova, zaštitite pristup, počnite sa skromnim iznosima. Uz ove mere predostrožnosti, LNbits postaje robusno rešenje za Lightning ekonomiju, dok očuvava decentralizaciju i autonomiju.



## Resursi



### Službena dokumentacija




- [LNbits Dokumentacija](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Službeni vodič za instalaciju](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Vodiči zajednice




- [Početna konfiguracija Ubuntu servera](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) autora Daniel P. Costas (korak-po-korak sigurnost VPS-a)
- [LNbits + PHOENIXD instalacija na Ubuntu VPS-u](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) autor Daniel P. Costas (kompletan vodič)
- [LNbits Server na Clearnet-u](https://ereignishorizont.xyz/lnbits-server/en/) od Axela
- [LNbits na VPS-u](https://github.com/TrezorHannes/vps-lnbits) od Hannes