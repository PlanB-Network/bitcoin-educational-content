---
name: LNbits server
description: Installation och konfiguration av en egen LNbits-server på Ubuntu VPS med PHOENIXD eller på Umbrel
---

![cover](assets/cover.webp)



LNbits är en Interface-webbapplikation med öppen källkod som omvandlar alla Lightning-backend (LND, Core Lightning, PHOENIXD) till en komplett serviceplattform. Med den här självhostande lösningen kan du hantera flera Lightning-portföljer isolerat, distribuera försäljningsställen, skapa donationssystem eller faktureringstjänster, samtidigt som du behåller total kontroll över dina medel.



Denna handledning omfattar två installationsmetoder: **VPS Ubuntu med PHOENIXD** (lättviktslösning utan en fullständig Bitcoin-nod) och **Umbrel** (integration med din befintliga LND-nod). Till skillnad från Plan B Networks allmänna LNbits-handledning, som täcker koncept och tillägg, fokuserar den här guiden på steg-för-steg tekniska installationsprocedurer.



## Vad är LNbits?



LNbits är ett Lightning-redovisningssystem utvecklat i Python (FastAPI) som ansluter till en befintlig backend (LND, Core Lightning, PHOENIXD). Till skillnad från traditionella Lightning-noder erbjuder LNbits en tillgänglig Interface, så att du kan hantera flera isolerade portföljer med sina egna API-nycklar. Du kan skapa underkonton för din familj, anställda eller projekt, utan att ge dem tillgång till alla dina medel.



Den frikopplade arkitekturen lagrar information i SQLite (standard) eller PostgreSQL (produktion), medan medel förblir hanterade av din Lightning-backend. Denna separation garanterar portabilitet: du kan migrera från PHOENIXD till LND utan att förlora dina användardata.



## Viktiga funktioner



LNbits erbjuder ett mångsidigt **utvidgningssystem**: TPoS (försäljningsställe), Paywall (monetarisering av innehåll), Events (biljettförsäljning), LndHub (server för BlueWallet), Bolt Cards (NFC-betalningar), Split Payments (automatisk distribution) och User Manager (användarhantering med autentisering).



På **dashboard** visas saldon i realtid, transaktionshistorik och faktureringsverktyg. Varje Wallet har en unik URL som innehåller dess API-nycklar, vilket ger åtkomst utan traditionell inloggning. API-nyckelsystemet** med tre nivåer (admin, Invoice, skrivskyddad) erbjuder detaljerad kontroll av behörigheter för säkra integrationer.



LNbits implementerar naturligt **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) och stöder **Lightning Address**, vilket garanterar kompatibilitet med moderna Lightning-plånböcker och underlättar distributionen av professionella tjänster.



## Plattformar som stöds



**Ubuntu VPS**: Lättviktslösning utan full Bitcoin-nod. Förutsättningar: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + domännamn krävs för offentlig exponering (LNURL-tjänster).



**Umbrytande**: Enkel installation från App Store. Förutsättning: funktionell Umbrel-nod med synkroniserad LND och öppna kanaler. Automatisk konfiguration.



Nedan finns länkar till våra handledningar för Umbrel och Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installation på Ubuntu VPS med PHOENIXD



### Steg 1: Säkra VPS-servern



**Innan någon installation** måste du säkra din Ubuntu VPS-server enligt konstens alla regler. Detta steg är **kritiskt** för att skydda din infrastruktur och dina Lightning-medel.



Här är en detaljerad guide som hjälper dig att komma igång: **[Initial Ubuntu-serverkonfiguration - Steg-för-steg-guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** av Daniel P. Costas.



Den här guiden omfattar användarkonfiguration, säker SSH, brandvägg (UFW), fail2ban, automatiska uppdateringar och god praxis för systemsäkerhet.



### Steg 2: Installera PHOENIXD



När din server är säker måste du installera och konfigurera PHOENIXD. Plan B Network erbjuder en komplett dedikerad handledning som täcker installation, seed-generering och systemd-tjänstekonfiguration:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

När PHOENIXD är igång (kontrollera med `./Phoenix-CLI getinfo`), notera **HTTP-lösenordet** i `~/.Phoenix/Phoenix.conf` - du behöver det för att ansluta LNbits till PHOENIXD.



### LNbits utplacering



Installera UV och klona LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurera PHOENIXD-backend:


```bash
cp .env.example .env && nano .env
```



Lägg till i `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Testa med `uv run lnbits --host 0.0.0.0 --port 5000` och skapa sedan en systemd-tjänst med `Wants=PHOENIXD.service`.



## Inledande installation och första användning



### Aktivering av SuperUser



Aktivera Interface-administratören i `.env` :


```
LNBITS_ADMIN_UI=true
```



Starta om LNbits (`sudo systemctl restart lnbits`) och hämta SuperUser-ID:t:


```bash
cat ~/lnbits/data/.super_user
```



Gå till `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` för att komma till administrationspanelen. I menyn "Server" kan du konfigurera finansieringskällor, anknytningar och användarkonton.



### Säkert skapande av konto



**Viktigt för offentlig exponering**: Om du exponerar din LNbits-instans på ett offentligt domännamn som är tillgängligt från Internet, är det **kritiskt** att inaktivera det fria skapandet av användarkonton.



Från SuperUser-administrationen Interface går du till "Inställningar" och sedan till avsnittet "Användarhantering". Där hittar du alternativet "Tillåt skapande av nya användare".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**För en offentlig utställning med domännamn** :




- Du måste avaktivera** alternativet "Tillåt skapande av nya användare"
- Utan detta skydd kan vem som helst på Internet skapa ett konto på din instans
- En angripare kan skapa konton och använda likviditeten i din LIGHTNING NODE utan din vetskap
- Du måste skapa användarkonton manuellt från Interface SuperUser



**Endast för lokalt bruk** :




- Det här alternativet är mindre viktigt om din instans endast är tillgänglig lokalt (http://localhost:5000)
- Att avaktivera detta alternativ är dock en god allmän säkerhetspraxis



När konfigurationen är klar är det bara SuperUser-administratören som kan skapa nya användarkonton via Interface "Users". Detta tillvägagångssätt garanterar total kontroll över vem som kan komma åt din Lightning-infrastruktur och använda dina pengar.



### Öppning av den första kanalen



PHOENIXD hanterar automatiskt kanaler via auto-likviditet. generate en Lightning Invoice på ~30 000 Sats från LNbits och betala den från en annan Wallet. PHOENIXD öppnar automatiskt en kanal till ACINQ. Öppningsavgiften (~20-23k Sats) dras av, det återstående saldot (~7-10k Sats) visas efter On-Chain bekräftelse.



Kontrollera status med `./Phoenix-CLI getinfo`. Överväg sedan att inaktivera auto-liquidity (`auto-liquidity=off` i `Phoenix.conf`) för att kontrollera kanalöppningar.



### Offentlig visning och HTTPS



**Viktigt**: HTTPS är obligatoriskt för offentlig visning (API-nyckelsäkerhet + LNURL-kompatibilitet). Hoppa över detta steg endast för lokal användning.



**Caddy (rekommenderas)**: automatisk SSL. `sudo apt install -y caddy`, redigera `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Starta om: `sudo systemctl restart caddy`.



**Nginx** : Mer kontroll. Installera `nginx certbot python3-certbot-nginx`, skapa `/etc/nginx/sites-available/lnbits` :


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


Aktivera: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Lägg till i `.env`: `FORWARDED_ALLOW_IPS=*`



## Paraplyinstallation



### Driftsättning från App Store



Gå till Umbrel App Store, sök efter "LNbits" och klicka på "Installera".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel kontrollerar automatiskt om det finns nödvändiga beroenden. LNbits kräver LIGHTNING NODE (LND) för att köras. Om din LIGHTNING NODE redan är i drift, klicka på "Installera LNbits" för att bekräfta.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel laddar ner Docker-imagen, konfigurerar automatiskt anslutningar med LND och startar containern (2-5 minuter). Installationen sker helt i bakgrunden.



### Initial konfiguration av SuperUser



Vid första lanseringen uppmanar LNbits dig att skapa SuperUser-administratörskontot. Ange ett användarnamn och ställ in ett säkert lösenord för att skydda åtkomsten till Interface:s administrationssystem.



![Configuration SuperUser](assets/fr/03.webp)



**Viktigt**: Detta SuperUser-konto har fullständiga privilegier på din LNbits-instans. Välj ett starkt lösenord och förvara det på ett säkert sätt.



När du har skapat ett konto kommer du automatiskt till Interface:s huvudadministrationsområde. Umbrel har redan satt upp LND som din finansieringskälla - alla Lightning-betalningar kommer att gå via dina befintliga kanaler.



### Åtkomst till Interface-administratör



Klicka på "Inställningar" i menyn till vänster för att komma till den fullständiga administrationspanelen.



![Interface Settings](assets/fr/04.webp)



I avsnittet "Wallets Management" visas viktig information om din konfiguration:




- Finansieringskälla** : LndBtcRestWallet (direktanslutning till din LND Umbrel-nod)
- Nodbalans** : Total likviditet tillgänglig i dina Lightning-kanaler
- LNbits-saldo**: Medel som tilldelats LNbits-systemet (ursprungligen 0 Sats)



Du kan nu direkt utnyttja likviditeten i din Umbrel-nod för alla LNbits-plånböcker som du skapar. Ingen ytterligare konfiguration krävs - LNbits är igång.



### Hantering av användare



En av LNbits mest kraftfulla funktioner är dess förmåga att skapa flera oberoende användare, var och en med lösenordsautentisering och isolerade plånböcker. Denna arkitektur gör det möjligt att dra nytta av likviditeten i din Umbrel-nod samtidigt som du erbjuder helt isolerade underkonton för olika användningsområden: företag, familj, anställda, projekt etc.



Klicka på "Users" i sidomenyn för att komma till användarhanteringen. Klicka på "CREATE ACCOUNT" för att lägga till en ny användare.



![Gestion des utilisateurs](assets/fr/05.webp)



Fyll i formuläret för att skapa en användare:




- Användarnamn**: Användarnamn för inloggning (exempel: "Satoshi")
- Ange lösenord**: Aktivera detta alternativ för att ange ett lösenord för autentisering
- Lösenord** och **Lösenordsupprepning**: Ange lösenordet för den här användaren



![Création utilisateur satoshi](assets/fr/06.webp)



Valfria fält (Nostr Public Key, E-post, Förnamn, Efternamn) kan lämnas tomma för minimal konfiguration. Klicka på "CREATE ACCOUNT" för att bekräfta.



![Confirmation utilisateur créé](assets/fr/07.webp)



Din nya användare visas nu i listan över användare med sin unika identifierare och sitt användarnamn.



![Liste des utilisateurs](assets/fr/08.webp)



**Viktig punkt**: Varje användare kan logga in helt självständigt med sitt eget lösenord. SuperUser-administratören behåller full kontroll via Interface:s administrationsverktyg.



### Användare Wallet-hantering



Nu när "Satoshi"-användaren har skapats måste du tilldela honom en Wallet Lightning. Klicka på Wallet-ikonen (andra ikonen) för den berörda användaren och sedan på "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



En dialogruta uppmanar dig att namnge Wallet. Ange ett beskrivande namn (t.ex. "Wallet Of Satoshi") och välj visningsvaluta (CUC, USD, EUR, etc.).



![Création wallet](assets/fr/10.webp)



Klicka på "CREATE" (Skapa). LNbits genererar omedelbart en fungerande Wallet Lightning för den här användaren.



![Confirmation wallet créé](assets/fr/11.webp)



Du ser nu de två befintliga plånböckerna: standard Wallet "LNbits Wallet" som skapades automatiskt, och den nya "Wallet Of Satoshi". För att förenkla användarupplevelsen kan du radera standard Wallet genom att klicka på raderingsikonen (röd papperskorg).



![Wallet final unique](assets/fr/12.webp)



"Satoshi"-användaren har nu en enda, tydligt identifierad Wallet. Varje Wallet-användare arbetar helt självständigt, samtidigt som den använder likviditeten i din underliggande LND-nod.



** Nyckelkoncept **: Alla dessa plånböcker delar den globala likviditeten i din Umbrel-nod. Du skapar inte nya Lightning-kanaler för varje Wallet - LNbits fungerar som en intelligent redovisande Layer som hanterar fördelningen av medel inom din befintliga Lightning-infrastruktur. Det är kraften i LNbits multi-Wallet-system.



### Användarinloggning



Logga ut från SuperUser-kontot (ikonen längst upp till höger) och återgå till LNbits inloggningssida. Du kan nu logga in med den nya användarens autentiseringsuppgifter.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Ange det användarnamn ("Satoshi") och lösenord som tidigare definierats och klicka sedan på "LOGIN". Användaren får direkt tillgång till sin personliga Wallet, helt isolerad från administrationen Interface.



### Interface från Wallet användare



När användaren är ansluten får han åtkomst till sin Interface från Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Interface har följande egenskaper :




- Aktuellt saldo**: Visas i Sats och i vald valuta (CUC i detta exempel)
- Huvudsakliga åtgärder**: "PASTE REQUEST" (klistra in en räkning att betala), "CREATE Invoice" (generate ett kvitto), QR-ikon (snabbskanning)
- Transaktionshistorik** : Komplett lista över alla betalningar och kvitton
- Panel på höger sida**: Konfigurations- och åtkomstmöjligheter



### Wallet mobil åtkomst



Den högra sidopanelen erbjuder en särskilt praktisk funktion: mobil åtkomst till Wallet. Fäll ut avsnittet "Mobil åtkomst" för att upptäcka de tillgängliga alternativen.



![Mobile Access](assets/fr/15.webp)



LNbits erbjuder flera sätt att använda denna Wallet på en smartphone:



**Alternativ 1: Kompatibla mobila applikationer




- Ladda ner **Zeus** eller **BlueWallet** från App Store eller Google Play
- Aktivera tillägget **LndHub** i LNbits för denna Wallet
- Skanna LndHub QR-koden med mobilappen för att ansluta Wallet



**Alternativ 2: Direktåtkomst via mobil webbläsare**




- QR-koden som visas i "Exportera till telefon med QR-kod" innehåller den fullständiga webbadressen till Wallet med integrerad autentisering
- Skanna denna QR-kod från din smartphone för att öppna Wallet direkt i din mobila webbläsare
- Lägg till sidan på startskärmen för snabb åtkomst



**Viktig säkerhetsinformation**: Den här URL:en innehåller API-nycklarna för full åtkomst till Wallet. Dela den aldrig offentligt. Behandla denna QR-kod som du skulle behandla dina privata Bitcoin-nycklar - alla som skannar denna QR-kod får full tillgång till Wallet.



Den här mobila funktionen förvandlar din LNbits Umbrel-instans till en riktig Lightning Wallet-server för dig och dina vänner, samtidigt som du behåller fullständig suveränitet över dina pengar tack vare din självhostade nod.



### Delning av användaråtkomst



Det huvudsakliga användningsområdet för denna fleranvändarkonfiguration är **dela plånböcker med din familj eller nära krets**. När du har skapat en användare med en dedikerad Wallet (t.ex. "Satoshi" i vårt exempel) kan du dela dessa inloggningsuppgifter med betrodda medlemmar i ditt hushåll.



**Åtkomstsäkerhet på Umbrel**: Åtkomst till din LNbits-instans på Umbrel är naturligt skyddad, eftersom den endast kan nås :




- I ditt lokala nätverk** : Medlemmar i ditt hushåll som är anslutna till samma WiFi-/Ethernet-nätverk kan komma åt instansen
- Via VPN**: Om du använder ett VPN som Tailscale som är konfigurerat på din Umbrel-server kan auktoriserade användare få säker fjärråtkomst



Detta dubbla Layer-skydd (nätverksåtkomst + användarautentisering) gör alternativet "Tillåt skapande av nya användare" mindre kritiskt på Umbrel. Endast personer som redan har tillgång till ditt nätverk eller VPN kan nå Interface-inloggningen.



**Typiskt scenario**: Du skapar ett "pappa"-konto, ett "mamma"-konto, ett "företag"-konto och så vidare. Varje familjemedlem har sin egen isolerade Wallet Lightning, samtidigt som de drar nytta av den delade likviditeten i din Umbrel-nod. Dela helt enkelt användarnamn och lösenord - användaren kan sedan ansluta från vilken enhet som helst i ditt lokala nätverk eller via ditt Tailscale VPN. Se vår dedikerade Tailscale-handledning för mer information:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Utforska tillgängliga tillägg



Gå tillbaka till Interface SuperUser och öppna menyn "Extensions" i den vänstra sidopanelen för att upptäcka hela LNbits ekosystem för tillägg.



![Extensions disponibles](assets/fr/16.webp)



LNbits erbjuder en rik katalog med tillägg som omvandlar din instans till en verklig plattform för Lightning-tjänster:





- Jukebox**: Sats-drivet jukeboxsystem (Spotify-betalningar)
- Supportbiljetter**: Avgiftsbelagt supportsystem (få Satss för att svara på frågor)
- TPoS**: Säker, mobil kassaterminal för återförsäljare
- User Manager**: avancerad användar- och Wallet-hantering (som vi just har använt)
- Evenemang**: Försäljning och validering av evenemangsbiljetter
- LNURLDevices**: Hantering av försäljningsställen, bankomater, anslutna switchar
- SMTP**: Gör det möjligt för användare att skicka e-post och tjäna Satss
- Boltcards**: Programmering av NFC-kort för Lightning tap-to-pay-betalningar
- NostrNip5**: Skapa NIP5-adresser för dina domäner
- Delade betalningar**: Automatisk fördelning av betalningar mellan flera plånböcker



Varje tillägg aktiveras med ett enda klick från denna Interface. Tillägg markerade med "FREE" är kostnadsfria, medan vissa är tillgängliga som "PAID"-versioner. Utforska katalogen för att identifiera de som matchar dina behov - oavsett om det gäller affärer, familjehantering eller experimenterande med Lightning Network:s funktioner.



## Fördelar och begränsningar



**Fördelar**: Finansiell suveränitet (full kontroll över medel/nycklar/data), arkitektonisk flexibilitet (förlustfri VPS→Full node-migrering), professionellt förlängningssystem, intuitiv Interface.



**Begränsningar** : Programvara i betaversion (försiktighet med belopp), säkerhet under administratörens ansvar, webbadresser som innehåller känsliga API-nycklar (HTTPS obligatoriskt), hantering av flera användare innebär vårdnadshavaransvar.



## Bästa praxis



**Backups**: seed PHOENIXD/legitimationer LND, LNbits-databas, `.env`-filer. Automatisera dagligen, förvara utanför produktionsservern, krypterad. Testa återställningar regelbundet.



**Underhåll**: Kontrollera regelbundet om det finns uppdateringar (LNbits, Lightning backend, operativsystem). Kontrollera alltid release notes före större uppdateringar.





- På Umbrel**: App Store meddelar dig automatiskt om nya versioner. Synkronisera tillägg via "Hantera tillägg" > "Uppdatera alla". Kontrollera att SQLite-databasen ingår i Umbrels automatiska säkerhetskopior.
- På VPS**: Uppdatera manuellt med `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Övervaka systemloggar: `sudo journalctl -u lnbits -f`.



## Slutsats



LNbits självhosting erbjuder en konkret väg till Lightning finansiell suveränitet. VPS+PHOENIXD erbjuder en lättviktslösning för snabba tjänster, Umbrel full integration med befintlig Bitcoin-nod. Den skalbara arkitekturen möjliggör utveckling från enkla Wallet med flera användare till sofistikerade affärsanvändningsfall.



Självhosting innebär ansvar: säkerhetskopiera frön, skydda åtkomst, börja med blygsamma belopp. Med dessa försiktighetsåtgärder blir LNbits en robust lösning för Lightning-ekonomin, samtidigt som decentralisering och autonomi bevaras.



## Resurser



### Officiell dokumentation




- [LNbits-dokumentation](https://docs.lnbits.org)
- [LNbits GitHub] (https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub] (https://github.com/ACINQ/PHOENIXD)
- [Officiell installationsguide](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Gemenskapens guider




- [Initial Ubuntu-serverkonfiguration] (https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) av Daniel P. Costas (steg-för-steg VPS-säkerhet)
- [LNbits + PHOENIXD-installation på Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) av Daniel P. Costas (fullständig guide)
- [LNbits Server på Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) av Axel
- [LNbits på VPS](https://github.com/TrezorHannes/vps-lnbits) av Hannes