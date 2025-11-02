---
name: LNbits server
description: Installatie en configuratie van een self-hosted LNbits server op Ubuntu VPS met PHOENIXD of op Umbrel
---

![cover](assets/cover.webp)



LNbits is een open source Interface webapplicatie die elke Lightning backend (LND, Core Lightning, PHOENIXD) transformeert in een compleet serviceplatform. Met deze self-hosted oplossing kun je meerdere Lightning-portefeuilles geïsoleerd beheren, verkooppunten implementeren, donatiesystemen of factureringsservices maken, terwijl je de volledige controle over je fondsen behoudt.



Deze tutorial behandelt twee installatiemethoden: **VPS Ubuntu met PHOENIXD** (lichtgewicht oplossing zonder een volledig Bitcoin knooppunt) en **Umbrel** (integratie met uw bestaande LND knooppunt). In tegenstelling tot de algemene LNbits tutorial van Plan B Network, die concepten en uitbreidingen behandelt, richt deze gids zich op stap-voor-stap technische installatieprocedures.



## Wat is LNbits?



LNbits is een Lightning-boekhoudsysteem ontwikkeld in Python (FastAPI) dat verbinding maakt met een bestaande backend (LND, Core Lightning, PHOENIXD). In tegenstelling tot traditionele Lightning nodes, biedt LNbits een toegankelijke Interface, waarmee je verschillende geïsoleerde portefeuilles kunt beheren met hun eigen API sleutels. U kunt subaccounts aanmaken voor uw familie, werknemers of projecten, zonder dat ze toegang krijgen tot al uw fondsen.



De ontkoppelde architectuur slaat informatie op in SQLite (standaard) of PostgreSQL (productie), terwijl fondsen beheerd blijven door je Lightning backend. Deze scheiding garandeert draagbaarheid: u kunt migreren van PHOENIXD naar LND zonder uw gebruikersgegevens te verliezen.



## Belangrijkste kenmerken



LNbits biedt een veelzijdig **uitbreidingssysteem**: TPoS (verkooppunt), Paywall (geld verdienen met content), Events (ticketing), LndHub (server voor BlueWallet), Bolt Cards (NFC-betalingen), Split Payments (automatische distributie) en User Manager (gebruikersbeheer met authenticatie).



Het **dashboard** toont realtime saldi, transactiegeschiedenis en factureringstools. Elke Wallet heeft een unieke URL die zijn API sleutels bevat, waardoor toegang mogelijk is zonder traditionele login. Het drietraps API sleutelsysteem** (admin, Invoice, alleen-lezen) biedt granulaire controle over machtigingen voor veilige integraties.



LNbits implementeert **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) en ondersteunt **Lightning Address**, waardoor compatibiliteit met moderne Lightning wallets wordt gegarandeerd en de inzet van professionele diensten wordt vergemakkelijkt.



## Ondersteunde platforms



**Ubuntu VPS**: Lichtgewicht oplossing zonder volledige Bitcoin node. Vereisten: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + domeinnaam vereist voor publieke blootstelling (LNURL-diensten).



**Umbrel**: Eenvoudige installatie vanuit de App Store. Vereiste: functioneel Umbrel knooppunt met gesynchroniseerde LND en open kanalen. Automatische configuratie.



Hieronder staan links naar onze Umbrel en Umbrel LND tutorials:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installeren op Ubuntu VPS met PHOENIXD



### Stap 1: De VPS server beveiligen



**Voordat u gaat installeren**, moet u uw Ubuntu VPS server beveiligen volgens de regels van de kunst. Deze stap is **kritiek** om uw infrastructuur en uw Lightning fondsen te beschermen.



Hier is een gedetailleerde handleiding om je op weg te helpen: **[Initial Ubuntu server configuration - Step-by-step guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** door Daniel P. Costas.



Deze handleiding behandelt gebruikersconfiguratie, veilige SSH, firewall (UFW), fail2ban, automatische updates en goede systeembeveiligingspraktijken.



### Stap 2: PHOENIXD installeren



Zodra je server veilig is, moet je PHOENIXD installeren en configureren. Plan B Network biedt een complete tutorial over de installatie, het genereren van seed en de configuratie van de systemd service:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Als PHOENIXD eenmaal draait (controleer met `./Phoenix-CLI getinfo`), noteer dan het **HTTP wachtwoord** in `~/.Phoenix/Phoenix.conf` - dat heb je nodig om LNbits met PHOENIXD te verbinden.



### LNbits inzet



UV installeren en LNbits klonen :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Configureer de PHOENIXD backend:


```bash
cp .env.example .env && nano .env
```



Toevoegen aan `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Test met `uv run lnbits --host 0.0.0.0 --port 5000` maak dan een systemd service aan met `Wants=PHOENIXD.service`.



## Eerste installatie en eerste gebruik



### Supergebruiker activering



Activeer de Interface beheerder in `.env` :


```
LNBITS_ADMIN_UI=true
```



Start LNbits opnieuw op (`sudo systemctl restart lnbits`) en vraag de SuperUser ID op:


```bash
cat ~/lnbits/data/.super_user
```



Ga naar `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` voor het administratiepaneel. In het menu "Server" kunt u financieringsbronnen, extensies en gebruikersaccounts configureren.



### Veilig een account aanmaken



**Belangrijk voor publieke blootstelling**: Als je je LNbits instantie blootstelt aan een publieke domeinnaam die toegankelijk is vanaf het internet, is het **kritisch** om het vrij aanmaken van gebruikersaccounts uit te schakelen.



Ga vanuit het SuperUser beheer Interface naar "Instellingen" en dan naar de sectie "Gebruikersbeheer". Hier vind je de optie "Nieuwe gebruikers aanmaken toestaan".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Voor een openbare tentoonstelling met domeinnaam** :




- U moet de optie "Nieuwe gebruikers aanmaken toestaan" uitschakelen**
- Zonder deze bescherming kan iedereen op het internet een account aanmaken op jouw instantie
- Een aanvaller kan accounts aanmaken en de liquiditeit van uw LIGHTNING NODE gebruiken zonder dat u het weet
- U moet handmatig gebruikersaccounts aanmaken vanuit de Interface SuperUser



**Alleen voor lokaal gebruik** :




- Deze optie is minder kritisch als je instantie alleen lokaal toegankelijk is (http://localhost:5000)
- Het uitschakelen van deze optie is echter een goede algemene veiligheidspraktijk



Eenmaal geconfigureerd, kan alleen de SuperUser-beheerder nieuwe gebruikersaccounts aanmaken via Interface "Gebruikers". Deze aanpak garandeert totale controle over wie toegang heeft tot uw Lightning-infrastructuur en wie uw fondsen kan gebruiken.



### Het eerste kanaal openen



PHOENIXD beheert kanalen automatisch via auto-liquiditeit. generate een Lightning Invoice van ~30.000 Sats van LNbits en betaal het van een andere Wallet. PHOENIXD opent automatisch een kanaal naar ACINQ. De openingskosten (~20-23k Sats) worden afgetrokken, het resterende saldo (~7-10k Sats) verschijnt na On-Chain bevestiging.



Controleer de status met `./Phoenix-CLI getinfo`. Overweeg dan om auto-liquidity uit te schakelen (`auto-liquidity=off` in `Phoenix.conf`) om kanaalopeningen te controleren.



### Openbare weergave en HTTPS



**Belangrijk**: HTTPS verplicht voor openbare weergave (API sleutel beveiliging + LNURL compatibiliteit). Sla deze stap over voor lokaal gebruik.



**Caddy (aanbevolen)**: automatische SSL. `sudo apt install -y caddy`, bewerk `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Herstart: `sudo systemctl restart caddy`.



**Nginx** : Meer controle. Installeer `nginx certbot python3-certbot-nginx`, maak `/etc/nginx/sites-available/lnbits` aan:


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


Activeer: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Toevoegen aan `.env`: `FORWARDED_ALLOW_IPS=*`



## Installatie paraplu



### Implementatie vanuit de App Store



Ga naar de Umbrel App Store, zoek naar "LNbits" en klik op "Installeren".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel controleert automatisch op vereiste afhankelijkheden. LNbits heeft LIGHTNING NODE (LND) nodig om te kunnen draaien. Als uw LIGHTNING NODE al operationeel is, klik dan op "Installeer LNbits" om te bevestigen.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel downloadt het Docker image, configureert automatisch de verbindingen met LND en start de container (2-5 minuten). De installatie vindt volledig op de achtergrond plaats.



### Initiële SuperUser-configuratie



Bij de eerste start vraagt LNbits u om de SuperUser administratoraccount aan te maken. Voer een gebruikersnaam in en stel een veilig wachtwoord in om de toegang tot het Interface administratiesysteem te beveiligen.



![Configuration SuperUser](assets/fr/03.webp)



**Belangrijk**: Dit SuperUser account heeft volledige rechten op je LNbits instantie. Kies een sterk wachtwoord en bewaar het veilig.



Zodra u een account hebt aangemaakt, gaat u automatisch naar het hoofdadministratiegedeelte van Interface. Umbrel heeft LND al ingesteld als uw financieringsbron - alle Lightning-betalingen gaan via uw bestaande kanalen.



### Toegang tot Interface beheerder



Klik in het menu aan de linkerkant op "Instellingen" om het volledige beheerpaneel te openen.



![Interface Settings](assets/fr/04.webp)



In het gedeelte "Portemonneebeheer" wordt belangrijke informatie over je configuratie weergegeven:




- Financieringsbron** : LndBtcRestWallet (directe verbinding met uw LND Umbrel knooppunt)
- Node Saldo** : Totale beschikbare liquiditeit in uw Lightning-kanalen
- LNbits-saldo**: Fondsen toegewezen aan het LNbits-systeem (aanvankelijk 0 Sats)



Je kunt nu direct de liquiditeit van je Umbrel-node benutten voor alle LNbits wallets die je aanmaakt. Er is geen extra configuratie nodig - LNbits is up and running.



### Gebruikersbeheer



Een van de krachtigste functies van LNbits is de mogelijkheid om meerdere onafhankelijke gebruikers aan te maken, elk met wachtwoordverificatie en geïsoleerde portemonnees. Deze architectuur maakt het mogelijk om te profiteren van de liquiditeit van uw Umbrel-node en tegelijkertijd volledig geïsoleerde sub-accounts aan te bieden voor verschillende doeleinden: bedrijf, familie, werknemers, projecten, enz.



Klik in het zijmenu op "Gebruikers" om naar het gebruikersbeheer te gaan. Klik op "ACCOUNT CREËREN" om een nieuwe gebruiker toe te voegen.



![Gestion des utilisateurs](assets/fr/05.webp)



Vul het formulier in om een gebruiker aan te maken:




- Gebruikersnaam**: Inlog gebruikersnaam (voorbeeld: "Satoshi")
- Wachtwoord instellen**: Activeer deze optie om een verificatiewachtwoord in te stellen
- Wachtwoord** en **Wachtwoord herhalen**: Stel het wachtwoord voor deze gebruiker in



![Création utilisateur satoshi](assets/fr/06.webp)



Optionele velden (Nostr Public Key, E-mail, Voornaam, Achternaam) kunnen leeg gelaten worden voor een minimale configuratie. Klik op "ACCOUNT CREËREN" om te bevestigen.



![Confirmation utilisateur créé](assets/fr/07.webp)



Je nieuwe gebruiker verschijnt nu in de lijst van gebruikers met zijn of haar unieke identifier en gebruikersnaam.



![Liste des utilisateurs](assets/fr/08.webp)



**Belangrijk punt**: Elke gebruiker kan volledig onafhankelijk inloggen met zijn of haar eigen wachtwoord. De SuperUser beheerder behoudt de volledige controle via de Interface administratietool.



### Beheer gebruiker Wallet



Nu de "Satoshi" gebruiker is aangemaakt, moet u hem een Wallet Lightning toewijzen. Klik op het Wallet icoon (tweede icoon) voor de betreffende gebruiker en vervolgens op "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



Een dialoogvenster vraagt je om de Wallet een naam te geven. Voer een beschrijvende naam in (bijv. "Wallet Of Satoshi") en selecteer de weergavemunteenheid (CUC, USD, EUR, enz.).



![Création wallet](assets/fr/10.webp)



Klik op "CREËREN". LNbits genereert direct een werkende Wallet Lightning voor deze gebruiker.



![Confirmation wallet créé](assets/fr/11.webp)



Je ziet nu de twee bestaande wallets: de standaard Wallet "LNbits Wallet" die automatisch is aangemaakt, en de nieuwe "Wallet Of Satoshi". Om de gebruikerservaring te vereenvoudigen, kun je de standaard Wallet verwijderen door op het verwijder icoon (rode prullenbak) te klikken.



![Wallet final unique](assets/fr/12.webp)



De "Satoshi" gebruiker heeft nu een enkele, duidelijk geïdentificeerde Wallet. Elke gebruiker Wallet werkt volledig autonoom, terwijl hij gebruik maakt van de liquiditeit van het onderliggende LND knooppunt.



**Key concept**: Al deze wallets delen de globale liquiditeit van uw Umbrel-node. U maakt geen nieuwe Lightning-kanalen aan voor elke Wallet - LNbits fungeert als een intelligente boekhoudkundige Layer die de toewijzing van fondsen beheert binnen uw bestaande Lightning-infrastructuur. Dat is de kracht van het multi-Wallet systeem van LNbits.



### Inloggen gebruiker



Log uit uit het SuperUser-account (pictogram rechtsboven) en ga terug naar de inlogpagina van LNbits. Je kunt nu inloggen met de gegevens van de nieuwe gebruiker.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Voer de eerder gedefinieerde gebruikersnaam ("Satoshi") en het wachtwoord in en klik dan op "LOGIN". De gebruiker krijgt direct toegang tot zijn persoonlijke Wallet, volledig geïsoleerd van de administratie Interface.



### Interface van Wallet gebruiker



Eenmaal verbonden heeft de gebruiker toegang tot zijn Interface vanaf de Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



De Interface heeft :




- Huidig saldo**: Weergegeven in Sats en in de gekozen valuta (CUC in dit voorbeeld)
- Belangrijkste acties**: "PASTE REQUEST" (een rekening plakken om te betalen), "CREATE Invoice" (generate een ontvangstbewijs), QR-pictogram (snel scannen)
- Transactiegeschiedenis** : Volledige lijst van alle betalingen en ontvangsten
- Zijpaneel rechts**: Configuratie en toegangsopties



### Wallet mobiele toegang



Het rechter zijpaneel biedt een bijzonder praktische functie: mobiele toegang tot de Wallet. Vouw het gedeelte "Mobiele toegang" open om de beschikbare opties te ontdekken.



![Mobile Access](assets/fr/15.webp)



LNbits biedt verschillende manieren om deze Wallet op een smartphone te gebruiken:



**Optie 1: Compatibele mobiele toepassingen




- Download **Zeus** of **BlueWallet** van App Store of Google Play
- Activeer de **LndHub** extensie in LNbits voor deze Wallet
- Scan de LndHub QR-code met de mobiele app om de Wallet aan te sluiten



**Optie 2: Directe toegang via mobiele browser**




- De QR code weergegeven in "Exporteer naar telefoon met QR Code" bevat de volledige URL van de Wallet met geïntegreerde verificatie
- Scan deze QR-code vanaf uw smartphone om Wallet direct in uw mobiele browser te openen
- Pagina toevoegen aan beginscherm voor snelle toegang



**Belangrijke beveiliging**: Deze URL bevat de API sleutels voor volledige toegang tot Wallet. Deel deze nooit publiekelijk. Behandel deze QR-code zoals je je Bitcoin privé-sleutels zou behandelen - iedereen die deze QR-code scant, krijgt volledige toegang tot Wallet.



Deze mobiele functie verandert je LNbits Umbrel instance in een echte Lightning Wallet server voor jou en je vrienden, terwijl je volledige soevereiniteit over je fondsen behoudt dankzij je zelf gehoste node.



### Gedeelde gebruikerstoegang



Het belangrijkste gebruik voor deze multi-user configuratie is **portefeuilles delen met je familie of naaste omgeving**. Zodra je een gebruiker hebt aangemaakt met een specifiek Wallet (zoals "Satoshi" in ons voorbeeld), kun je deze inloggegevens delen met vertrouwde leden van je gezin.



**Toegangsbeveiliging op Umbrel**: De toegang tot uw LNbits-instantie op Umbrel is natuurlijk beveiligd, omdat deze alleen toegankelijk is :




- Op je lokale netwerk** : Leden van je huishouden die op hetzelfde WiFi- of Ethernet-netwerk zijn aangesloten, hebben toegang tot de instantie
- Via VPN**: Als u gebruik maakt van een VPN zoals Tailscale geconfigureerd op uw Umbrel server, kunnen bevoegde gebruikers beveiligde toegang op afstand krijgen



Deze dubbele Layer bescherming (netwerktoegang + gebruikersauthenticatie) maakt de optie "Nieuwe gebruikers toestaan" minder kritisch op Umbrel. Alleen mensen die al toegang hebben tot uw netwerk of VPN kunnen de Interface login bereiken.



**Typisch scenario**: U maakt een 'vader'-account aan, een 'moeder'-account, een 'bedrijfs'-account enzovoort. Elk lid van de familie heeft zijn eigen geïsoleerde Wallet Lightning, terwijl hij profiteert van de gedeelde liquiditeit van uw Umbrel-knooppunt. Deel gewoon de gebruikersnaam en het wachtwoord - de gebruiker kan vervolgens verbinding maken vanaf elk apparaat op uw lokale netwerk of via uw Tailscale VPN. Bekijk onze speciale Tailscale handleiding voor meer informatie:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Beschikbare extensies verkennen



Ga terug naar de Interface SuperUser en ga naar het menu "Extensies" in het linker zijpaneel om het complete LNbits extensie ecosysteem te ontdekken.



![Extensions disponibles](assets/fr/16.webp)



LNbits biedt een uitgebreide catalogus met extensies die je instantie omtoveren tot een echt Lightning-servicesplatform:





- Jukebox**: Jukeboxsysteem op Sats (Spotify-betalingen)
- Support Tickets**: Betaald ondersteuningssysteem (ontvang Satss om vragen te beantwoorden)
- TPoS**: Veilige, mobiele betaalterminal voor retailers
- User Manager**: geavanceerd beheer van gebruikers en Wallet (die we net hebben gebruikt)
- Evenementen**: Verkoop en validatie van tickets voor evenementen
- LNURLDevices**: Beheer van verkooppunten, geldautomaten, aangesloten schakelaars
- SMTP**: Stel gebruikers in staat om e-mails te versturen en Satss te verdienen
- Boltcards**: NFC-kaarten programmeren voor Lightning tap-to-pay betalingen
- NostrNip5**: NIP5-adressen maken voor uw domeinen
- Gesplitste betalingen**: Automatische verdeling van betalingen tussen meerdere wallets



Elke extensie wordt met één klik geactiveerd vanaf deze Interface. Extensies met de markering "FREE" zijn gratis, terwijl sommige beschikbaar zijn als "PAID" versie. Verken de catalogus om de extensies te vinden die aan uw behoeften voldoen - of het nu gaat om zaken doen, familiebeheer of experimenteren met de mogelijkheden van Lightning Network.



## Voordelen en beperkingen



**Voordelen**: Financiële soevereiniteit (volledige controle over fondsen/sleutels/gegevens), architecturale flexibiliteit (verliesloze VPS→Full node migratie), professioneel uitbreidingssysteem, intuïtieve Interface.



**Beperkingen** : Software in bèta (voorzichtig met hoeveelheden), beveiliging onder verantwoordelijkheid van beheerder, URL's die gevoelige API sleutels bevatten (HTTPS verplicht), beheer door meerdere gebruikers impliceert beheerdersverantwoordelijkheid.



## Beste praktijken



**Backups**: seed PHOENIXD/credentials LND, LNbits database, `.env` bestanden. Dagelijks automatiseren, buiten productieserver houden, versleuteld. Test herstel regelmatig.



**Onderhoud**: Controleer regelmatig op updates (LNbits, Lightning backend, besturingssysteem). Controleer altijd release notes voor grote updates.





- Op Umbrel**: App Store word je automatisch op de hoogte gebracht van nieuwe versies. Synchroniseer extensies via "Extensies beheren" > "Alles bijwerken". Controleer of SQLite-database is opgenomen in automatische back-ups van Umbrel.
- Op VPS**: Update handmatig met `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Controleer systeem logs: `sudo journalctl -u lnbits -f`.



## Conclusie



LNbits self-hosting biedt een concreet pad naar Lightning financiële soevereiniteit. VPS+PHOENIXD biedt een lichtgewicht oplossing voor snelle diensten, Umbrel volledige integratie met bestaande Bitcoin node. De schaalbare architectuur maakt evolutie mogelijk van eenvoudig multi-user Wallet tot geavanceerde zakelijke use cases.



Zelf hosten brengt verantwoordelijkheid met zich mee: maak een back-up van zaden, bescherm de toegang, begin met bescheiden hoeveelheden. Met deze voorzorgsmaatregelen wordt LNbits een robuuste oplossing voor de Lightning-economie, met behoud van decentralisatie en autonomie.



## Bronnen



### Officiële documentatie




- [LNbits documentatie](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Officiële installatiegids](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Communautaire gidsen




- [Eerste configuratie Ubuntu-server](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) door Daniel P. Costas (stapsgewijze VPS-beveiliging)
- [LNbits + PHOENIXD installatie op Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) door Daniel P. Costas (volledige handleiding)
- [LNbits Server op Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) door Axel
- [LNbits op VPS](https://github.com/TrezorHannes/vps-lnbits) door Hannes