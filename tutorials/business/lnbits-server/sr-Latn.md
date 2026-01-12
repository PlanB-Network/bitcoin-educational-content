---
name: LNbits Server
description: Instalacija i konfiguracija samostalno hostovanog LNbits servera na Ubuntu VPS sa Phoenixd ili na Umbrel
---

![cover](assets/cover.webp)



LNbits je open source web interfejs koji transformiše bilo koji Lightning backend (LND, Core Lightning, Phoenixd) u kompletnu servisnu platformu. Ovo rešenje koje sami hostujete omogućava vam da upravljate višestrukim Lightning portfolijima u izolaciji, postavljate prodajna mesta, kreirate sisteme za donacije ili usluge naplate, dok zadržavate potpunu kontrolu nad vašim sredstvima.



Ovaj vodič pokriva dva pristupa instalaciji: **VPS Ubuntu sa Phoenixd** (lagano rešenje bez punog Bitcoin čvora) i **Umbrel** (integracija sa vašim postojećim LND čvorom). Za razliku od opšteg LNbits vodiča Plan ₿ Akademije, koji pokriva koncepte i ekstenzije, ovaj vodič se fokusira na tehničke procedure instalacije korak po korak.



## Šta je LNbits?



LNbits je sistem za knjigovodstvo na Lightning mreži razvijen u Pythonu (FastAPI) koji se povezuje sa postojećim backendom (LND, Core Lightning, Phoenixd). Za razliku od tradicionalnih Lightning čvorova, LNbits nudi pristupačan interfejs za upravljanje nekoliko izolovanih portfolija sa sopstvenim API ključevima. Možete kreirati podračune za svoju porodicu, zaposlene ili projekte, bez davanja pristupa svim vašim sredstvima.



Decoupled arhitektura skladišti informacije u SQLite (podrazumevano) ili PostgreSQL (produkcija), dok sredstva ostaju upravljana od strane vašeg Lightning backend-a. Ovo razdvajanje garantuje prenosivost: možete migrirati sa Phoenixd na LND bez gubitka korisničkih podataka.



## Ključne karakteristike



LNbits nudi svestran **sistem ekstenzija**: TPoS (prodajno mesto), Paywall (monetizacija sadržaja), Events (prodaja karata), LndHub (server za BlueWallet), Bolt Cards (NFC plaćanja), Split Payments (automatska distribucija), i User Manager (upravljanje korisnicima sa autentifikacijom).



**Dashboard** prikazuje stanje u realnom vremenu, istoriju transakcija i alate za naplatu. Svaki wallet ima jedinstveni URL koji sadrži njegove API ključeve, omogućavajući pristup bez tradicionalnog prijavljivanja. Troslojni API sistem ključeva** (admin, faktura, samo za čitanje) nudi detaljnu kontrolu dozvola za sigurne integracije.



LNbits nativno implementira **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) i podržava **Lightning Address**, garantujući kompatibilnost sa modernim Lightning novčanicima i olakšavajući implementaciju profesionalnih usluga.



## Podržane platforme



**Ubuntu VPS**: Laganija rešenja bez punog Bitcoin čvora. Preduslovi: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + naziv domena potreban za javnu izloženost (LNURL usluge).



**Umbrel**: Laka instalacija iz App Store-a. Preduslov: funkcionalan Umbrel čvor sa sinhronizovanim LND i otvorenim kanalima. Automatska konfiguracija.



Ispod su linkovi ka našim tutorijalima za Umbrel i Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalacija na Ubuntu VPS sa Phoenixd



### Korak 1: Obezbeđivanje VPS servera



**Pre nego što bilo šta instalirate**, potrebno je da obezbedite vaš Ubuntu VPS server prema pravilima struke. Ovaj korak je **kritičan** za zaštitu vaše infrastrukture i vaših Lightning sredstava.



Evo detaljnog vodiča koji će vam pomoći da započnete: **[Početna konfiguracija Ubuntu servera - Vodič korak po korak](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** autora Daniel P. Costas.



Ovaj vodič pokriva korisničku konfiguraciju, siguran SSH, firewall (UFW), fail2ban, automatska ažuriranja i dobre prakse sigurnosti sistema.



### Korak 2: Instaliranje Phoenixd



Kada je vaš server siguran, potrebno je instalirati i konfigurisati Phoenixd. Plan ₿ Academy nudi sveobuhvatan posvećen vodič koji pokriva instalaciju, seed generaciju i konfiguraciju systemd servisa :



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Kada Phoenixd bude pokrenut (proverite sa `./phoenix-cli getinfo`), zabeležite **HTTP lozinku** u `~/.phoenix/phoenix.conf` - biće vam potrebna da povežete LNbits sa Phoenixd.



### LNbits implementacija



Instaliraj UV i kloniraj LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurišite Phoenixd backend:


```bash
cp .env.example .env && nano .env
```



Dodaj u `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Testiraj sa `uv run lnbits --host 0.0.0.0 --port 5000` zatim kreiraj systemd servis sa `Wants=phoenixd.service`.



## Početno podešavanje i prva upotreba



### SuperUser aktivacija



Aktivirajte administratorski interfejs u `.env` :


```
LNBITS_ADMIN_UI=true
```



Ponovo pokrenite LNbits (`sudo systemctl restart lnbits`) i preuzmite SuperUser ID:


```bash
cat ~/lnbits/data/.super_user
```



Idite na `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` za administrativni panel. Meni "Server" vam omogućava da konfigurišete izvore finansiranja, ekstenzije i korisničke naloge.



### Sigurno kreiranje naloga



**Važno za javno izlaganje**: Ako izlažete svoju LNbits instancu na javnom domenu dostupnom s Interneta, **kritično** je onemogućiti besplatno kreiranje korisničkih naloga.



Sa SuperUser administrativnog interfejsa, idite na "Settings" i zatim na odeljak "User Management". Tamo ćete pronaći opciju "Allow creation of new users".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Za javnu izložbu sa domenom** :




- Morate onemogućiti** opciju "Dozvoli kreiranje novih korisnika"
- Bez ove zaštite, bilo ko na Internetu može kreirati nalog na vašoj instanci.
- Napadač bi mogao kreirati naloge i koristiti likvidnost vašeg Lightning čvora bez vašeg znanja.
- Moraćete ručno da kreirate korisničke naloge iz SuperUser interfejsa.



**Samo za lokalnu upotrebu** :




- Ova opcija je manje kritična ako je vaša instanca dostupna samo lokalno (http://localhost:5000)
- Međutim, onemogućavanje ove opcije je dobra opšta bezbednosna praksa



Jednom kada se konfiguriše, samo SuperUser administrator može kreirati nove korisničke naloge putem interfejsa "Korisnici". Ovaj pristup garantuje potpunu kontrolu nad tim ko može pristupiti vašoj Lightning infrastrukturi i koristiti vaša sredstva.



### Otvaranje prvog kanala



Phoenixd automatski upravlja kanalima putem auto-likvidnosti. Generišite Lightning fakturu od ~30,000 sats iz LNbits i platite je sa drugog wallet. Phoenixd automatski otvara kanal ka ACINQ. Naknada za otvaranje (~20-23k sats) se odbija, preostali balans (~7-10k sats) se pojavljuje nakon on-chain potvrde.



Proveri status pomoću `./phoenix-cli getinfo`. Zatim razmotri onemogućavanje automatske likvidnosti (`auto-liquidity=off` u `phoenix.conf`) kako bi kontrolisao otvaranje kanala.



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


Aktiviraj: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Dodajte u `.env`: `FORWARDED_ALLOW_IPS=*`



## Instalacija Umbrel



### Postavljanje sa App Store-a



Idite u Umbrel App Store, potražite "LNbits" i kliknite na "Install".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel automatski proverava potrebne zavisnosti. LNbits zahteva Lightning Node (LND) da bi radio. Ako je vaš Lightning čvor već operativan, kliknite na "Install LNbits" da potvrdite.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel preuzima Docker sliku, automatski konfiguriše veze sa LND i pokreće kontejner (2-5 minuta). Instalacija se odvija u potpunosti u pozadini.



### Početna konfiguracija SuperUser-a



Prilikom prvog pokretanja, LNbits vas poziva da kreirate SuperUser administratorski nalog. Unesite korisničko ime i sigurnu lozinku kako biste zaštitili pristup administrativnom interfejsu.



![Configuration SuperUser](assets/fr/03.webp)



**Važno**: Ovaj SuperUser nalog ima potpune privilegije na vašem LNbits instance-u. Izaberite jaku lozinku i čuvajte je na sigurnom.



Jednom kada kreirate nalog, automatski ćete biti preusmereni na glavni administrativni interfejs. Umbrel je već postavio LND kao vaš izvor finansiranja - sva Lightning plaćanja će ići kroz vaše postojeće kanale.



### Pristup administratorskom interfejsu



U levom meniju kliknite na "Settings" da biste pristupili celom administrativnom panelu.



![Interface Settings](assets/fr/04.webp)



Odsek "Upravljanje novčanicima" prikazuje ključne informacije o vašoj konfiguraciji:




- Izvor finansiranja** : LndBtcRestWallet (direktna veza sa vašim LND Umbrel čvorom)
- Ravnoteža čvora** : Ukupna likvidnost dostupna u vašim Lightning kanalima
- LNbits Balance**: Sredstva dodeljena LNbits sistemu (u početku 0 sats)



Sada možete direktno iskoristiti likvidnost vašeg Umbrel čvora za sve LNbits novčanike koje kreirate. Nije potrebna dodatna konfiguracija - LNbits je spreman za rad.



### Upravljanje korisnicima



Jedna od najmoćnijih karakteristika LNbits-a je njegova sposobnost da kreira više nezavisnih korisnika, svaki sa autentifikacijom lozinkom i izolovanim novčanicima. Ova arhitektura omogućava iskorišćavanje likvidnosti vašeg Umbrel čvora dok nudi potpuno izolovane podračune za različite namene: posao, porodicu, zaposlene, projekte, itd.



U bočnom meniju kliknite na "Korisnici" da biste pristupili upravljanju korisnicima. Kliknite na "KREIRAJ NALOG" da biste dodali novog korisnika.



![Gestion des utilisateurs](assets/fr/05.webp)



Popunite obrazac za kreiranje korisnika:




- Korisničko ime**: Korisničko ime za prijavu (primer: "satoshi")
- Postavi lozinku**: Aktivirajte ovu opciju da postavite lozinku za autentifikaciju
- Lozinka** i **Ponovi lozinku**: Postavite lozinku za ovog korisnika



![Création utilisateur satoshi](assets/fr/06.webp)



Opciona polja (Nostr javni ključ, Email, Ime, Prezime) mogu ostati prazna za minimalnu konfiguraciju. Kliknite na "CREATE ACCOUNT" da potvrdite.



![Confirmation utilisateur créé](assets/fr/07.webp)



Vaš novi korisnik se sada pojavljuje na listi korisnika sa svojim jedinstvenim identifikatorom i korisničkim imenom.



![Liste des utilisateurs](assets/fr/08.webp)



**Važna tačka**: Svaki korisnik može se prijaviti potpuno nezavisno sa svojom lozinkom. SuperUser administrator zadržava punu kontrolu putem administrativnog interfejsa.



### Upravljanje korisnikom wallet



Sada kada je korisnik "satoshi" kreiran, potrebno je dodeliti mu wallet Lightning. Kliknite na ikonu wallet (druga ikona) za dotičnog korisnika, zatim na "CREATE NEW WALLET".



![Gestion des wallets](assets/fr/09.webp)



Dijalog okvir vas poziva da imenujete wallet. Unesite opisni naziv (npr. "Wallet Od Satoshi") i izaberite valutu prikaza (CUC, USD, EUR, itd.).



![Création wallet](assets/fr/10.webp)



Kliknite na "CREATE". LNbits trenutno generiše radni wallet Lightning za ovog korisnika.



![Confirmation wallet créé](assets/fr/11.webp)



Sada vidite dva postojeća novčanika: podrazumevani wallet "LNbits wallet" kreiran automatski, i novi "Wallet Of Satoshi". Da biste pojednostavili korisničko iskustvo, možete obrisati podrazumevani wallet klikom na ikonu za brisanje (crvena kanta za smeće).



![Wallet final unique](assets/fr/12.webp)



Korisnik "satoshi" sada ima jedan, jasno identifikovan wallet. Svaki korisnik wallet funkcioniše potpuno autonomno dok koristi likvidnost vašeg osnovnog LND čvora.



**Ključni koncept**: Svi ovi novčanici dele globalnu likvidnost vašeg Umbrel čvora. Ne kreirate nove Lightning kanale za svaki wallet - LNbits deluje kao inteligentni računovodstveni sloj koji upravlja raspodelom sredstava unutar vaše postojeće Lightning infrastrukture. To je moć LNbits-ovog multi-wallet sistema.



### Prijava korisnika



Odjavite se sa SuperUser naloga (ikona u gornjem desnom uglu) i vratite se na LNbits stranicu za prijavu. Sada se možete prijaviti sa podacima novog korisnika.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Unesite korisničko ime ("satoshi") i prethodno definisanu lozinku, zatim kliknite na "LOGIN". Korisnik dobija direktan pristup svom ličnom wallet, potpuno izolovanom od administrativnog interfejsa.



### Interface od korisnika wallet



Kada se prijavi, korisnik pristupa svom kompletnom wallet Lightning interfejsu.



![Interface wallet utilisateur](assets/fr/14.webp)



Interfejs sadrži:




- Trenutno stanje**: Prikazano u sats i u odabranoj valuti (CUC u ovom primeru)
- Glavne radnje**: ZALJEPI ZAHTJEV, KREIRAJ FAKTURU, QR ikona (brzo skeniranje)
- Istorija transakcija** : Kompletna lista svih uplata i isplata
- Desna strana panela**: Opcije konfiguracije i pristupa



### Mobilni pristup wallet



Desna bočna tabla nudi posebno praktičnu funkciju: mobilni pristup wallet. Otvorite odeljak "Mobilni Pristup" da biste otkrili dostupne opcije.



![Mobile Access](assets/fr/15.webp)



LNbits nudi nekoliko načina za korišćenje ovog wallet na pametnom telefonu:



**Opcija 1: Kompatibilne mobilne aplikacije




- Preuzmite **Zeus** ili **BlueWallet** sa App Store-a ili Google Play-a
- Aktiviraj ekstenziju **LndHub** u LNbits za ovaj wallet
- Skenirajte LndHub QR kod mobilnom aplikacijom da povežete wallet



**Opcija 2: Direktan pristup putem mobilnog pregledača**




- QR kod prikazan u "Izvoz na telefon sa QR kodom" sadrži punu URL adresu wallet sa integrisanom autentifikacijom
- Skenirajte ovaj QR kod sa svog pametnog telefona da biste otvorili wallet direktno u svom mobilnom pregledaču.
- Dodaj stranicu na početni ekran za brz pristup



**Važna bezbednost**: Ovaj URL sadrži API ključeve za potpuni pristup wallet. Nikada ga ne delite javno. Tretirajte ovaj QR kod kao svoje Bitcoin privatne ključeve - svako ko skenira ovaj QR kod dobija potpuni pristup wallet.



Ova mobilna funkcija pretvara vašu LNbits Umbrel instancu u pravi Lightning wallet server za vas i vaše prijatelje, dok zadržavate potpunu suverenost nad vašim sredstvima zahvaljujući vašem samostalno hostovanom čvoru.



### Deljenje korisničkog pristupa



Glavna upotreba za ovu konfiguraciju sa više korisnika je **deljenje novčanika sa vašom porodicom ili bliskim krugom**. Kada kreirate korisnika sa posvećenim wallet (kao što je "satoshi" u našem primeru), možete podeliti ove pristupne podatke sa pouzdanim članovima vašeg domaćinstva.



**Pristup sigurnosti na Umbrelu**: Pristup vašoj LNbits instanci na Umbrelu je prirodno zaštićen, jer mu se može pristupiti samo:




- Na vašoj lokalnoj mreži** : Članovi vašeg domaćinstva povezani na istu WiFi/Ethernet mrežu mogu pristupiti instanci
- Putem VPN-a**: Ako koristite VPN kao što je Tailscale konfigurisan na vašem Umbrel serveru, ovlašćeni korisnici mogu dobiti siguran daljinski pristup



Ovaj dvostruki sloj zaštite (pristup mreži + autentifikacija korisnika) čini opciju "Dozvoli kreiranje novih korisnika" manje kritičnom na Umbrel-u. Samo osobe koje već imaju pristup vašoj mreži ili VPN-u mogu doći do interfejsa za prijavu.



**Tipičan scenario**: Kreirate nalog za "tatu", nalog za "mamu", nalog za "posao" i tako dalje. Svaki član porodice ima svoj izolovani wallet Lightning, dok koristi zajedničku likvidnost vašeg Umbrel čvora. Jednostavno podelite korisničko ime i lozinku - korisnik se zatim može povezati sa bilo kog uređaja na vašoj lokalnoj mreži ili putem vašeg Tailscale VPN-a. Molimo vas da pogledate naš posvećeni Tailscale vodič za više informacija:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Istraži dostupna proširenja



Vratite se na SuperUser interfejs i pristupite meniju "Extensions" u levom bočnom panelu da biste otkrili kompletan LNbits ekosistem ekstenzija.



![Extensions disponibles](assets/fr/16.webp)



LNbits nudi bogat katalog ekstenzija koje vašu instancu pretvaraju u pravi platformu za Lightning usluge:





- Jukebox**: sats-pokretan jukebox sistem (Spotify plaćanja)
- Podrška Ulaznice**: Plaćeni sistem podrške (primajte satss za odgovaranje na pitanja)
- TPoS**: Siguran, mobilni terminal za prodajna mesta za trgovce
- User Manager**: napredno upravljanje korisnicima i wallet (koje smo upravo koristili)
- Događaji**: Prodaja i validacija ulaznica za događaje
- LNURLDevices**: Upravljanje prodajnim mestima, bankomati, povezani prekidači
- SMTP**: Omogućite korisnicima slanje e-pošte i zaradite satss
- Boltcards**: Programiranje NFC kartica za Lightning tap-to-pay plaćanja
- NostrNip5**: Kreirajte NIP5 adrese za vaše domene
- Splitpayments**: Automatska distribucija uplata između više novčanika



Svako proširenje se aktivira jednim klikom iz ovog interfejsa. Proširenja označena kao "BESPLATNO" su bez naknade, dok su neka dostupna kao "PLAĆENE" verzije. Istražite katalog kako biste identifikovali ona koja odgovaraju vašim potrebama - bilo za poslovanje, porodično upravljanje ili eksperimentisanje sa mogućnostima Lightning Network.



## Prednosti i ograničenja



**Prednosti**: Finansijski suverenitet (potpuna kontrola nad sredstvima/ključevima/podacima), arhitektonska fleksibilnost (migracija bez gubitaka VPS→full node), profesionalni sistem proširenja, intuitivan interfejs.



**Ograničenja** : Softver u beta verziji (oprez kod iznosa), sigurnost pod odgovornošću administratora, URL-ovi koji sadrže osetljive API ključeve (HTTPS obavezan), upravljanje više korisnika podrazumeva starateljsku odgovornost.



## Najbolje prakse



**Backups**: Phoenixd Seed/LND akreditivi, LNbits baza podataka, .env fajlovi. Automatizovati dnevno, čuvati van produkcionog servera, enkriptovano. Redovno testirati povratke.



**Održavanje**: Redovno proveravajte ažuriranja (LNbits, Lightning backend, operativni sistem). Uvek proverite beleške o izdanju pre većih ažuriranja.





- Na Umbrel**: App Store automatski obaveštava o novim verzijama. Sinhronizujte ekstenzije putem "Manage Extensions" > "Update All". Proverite uključivanje SQLite baze podataka u automatske rezervne kopije Umbrel-a.
- Na VPS**: Ažurirajte ručno sa `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Pratite sistemske logove: `sudo journalctl -u lnbits -f`.



## Zaključak



LNbits samohosting nudi konkretan put ka finansijskom suverenitetu uz Lightning. VPS+Phoenixd nudi lagano rešenje za brze usluge, Umbrel punu integraciju sa postojećim Bitcoin čvorom. Skalabilna arhitektura omogućava evoluciju od jednostavnog multi-korisničkog wallet do sofisticiranih poslovnih slučajeva.



Samostalno hostovanje podrazumeva odgovornost: napravite rezervne kopije seed-ova, zaštitite pristup, počnite sa skromnim iznosima. Uz ove mere predostrožnosti, LNbits postaje robusno rešenje za Lightning ekonomiju, uz očuvanje decentralizacije i autonomije.



## Resursi



### Zvanična dokumentacija




- [LNbits Dokumentacija](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Službeni vodič za instalaciju](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Vodiči zajednice




- [Početna konfiguracija Ubuntu servera](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) autora Daniel P. Costas (korak-po-korak sigurnost VPS-a)
- [Instalacija LNbits + Phoenixd na Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) autor: Daniel P. Costas (kompletan vodič)
- [LNbits Server na Clearnet-u](https://ereignishorizont.xyz/lnbits-server/en/) od Axela
- [LNbits na VPS-u](https://github.com/TrezorHannes/vps-lnbits) od strane Hannesa