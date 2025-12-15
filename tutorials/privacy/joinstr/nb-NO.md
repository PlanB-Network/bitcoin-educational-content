---
name: Joinstr
description: Desentraliserte CoinJoins via Nostr-nettverket for suveren Bitcoin-konfidensialitet
---

![cover](assets/cover.webp)



Bitcoin-blokkjedens gjennomsiktighet gjør det mulig å spore transaksjonshistorikken. CoinJoins bryter disse koblingene ved å blande flere samtidige transaksjoner, noe som gjenoppretter et konfidensialitetsnivå som kan sammenlignes med kontanter.



Tradisjonelle løsninger er imidlertid avhengige av en sentral koordinator som et eneste feilpunkt. Wasabi og Samourai innstilte driften i 2024 etter press fra myndighetene.



**Joinstr** eliminerer denne svakheten ved å bruke det desentraliserte Nostr-nettverket for koordinering. Denne applikasjonen med åpen kildekode muliggjør virkelig suverene CoinJoins, der ingen sentral myndighet kan sensurere, overvåke eller avbryte tjenesten.



## Hva er Joinstr?



Joinstr er et åpen kildekode-verktøy som revolusjonerer CoinJoins-tilnærmingen ved å utnytte Nostr-protokollen som koordineringsinfrastruktur. I motsetning til sentraliserte løsninger som krever en dedikert server, baserer Joinstr seg på et distribuert nettverk av Nostr-reléer for å gjøre det mulig for deltakerne å koordinere direkte mellom jevnaldrende.



**Desentralisert arkitektur** : Nostr-nettverket erstatter den sentrale koordinatoren. Deltakerne oppretter eller blir med i "bassenger" ved å legge ut krypterte kunngjøringer via Nostr-reléene. Denne informasjonen (beløp, deltakere, adresser) forblir uforståelig for reléene, noe som sikrer at ingen sentral enhet kan overvåke, sensurere eller filtrere CoinJoins.



**SIGHASH_ALL|ANYONECANPAY-mekanisme**: Joinstr utnytter dette Bitcoin-signaturflagget, slik at hver deltaker bare kan signere sin egen input, mens alle outputs valideres. Hver bruker genererer sin PSBT lokalt, og distribuerer den deretter via Nostr. Hver bruker genererer sin PSBT lokalt, signerer den og distribuerer den deretter via Nostr. Bitcoinsene dine forblir under din eksklusive kontroll frem til den endelige signeringen.



**Filosofi**: Joinstr følger Bitcoin-cypherpunk-etoset, med tre mål: **motstand mot sensur** (ingen myndighet kan stoppe tjenesten), **total ikke-fengsling** (du beholder dine private nøkler), og **likestilling** (ingen UTXO kan diskrimineres).



### Hovedfunksjoner



**Fleksible puljer**: I motsetning til faste valører kan alle brukere opprette en pool med nøyaktig ønsket beløp og antall deltakere, noe som optimaliserer bruken av UTXO uten kunstig splitting.



**Transparente gebyrer**: Ingen koordineringsgebyrer. Kun Bitcoin-transaksjonsgebyrer deles likt mellom deltakerne (noen få tusen satoshier per person).



**Efemeralitet**: Ingen brukerdata beholdes. Informasjon overføres via krypterte, kortvarige Nostr-meldinger, som glemmes umiddelbart etter transaksjonen.



### Tilgjengelige plattformer



Denne veiledningen fokuserer på **Android-applikasjonen**, som er den eneste stabile og anbefalte løsningen for øyeblikket. Det finnes en Electrum-plugin, men den har kompatibilitetsproblemer som gjør den ustabil. Et webgrensesnitt er under utvikling.



## Bitcoin Kjernekonfigurasjon



Joinstr Android krever en tilkobling til en Bitcoin-node via RPC. Du må først konfigurere Bitcoin Core på datamaskinen for å godta tilkoblinger fra telefonen.



**Merknad**: For mer informasjon om den komplette konfigurasjonen av Bitcoin Core, se våre dedikerte veiledninger :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Krav til nettverk



#### Finn din lokale IP-adresse



Android-telefonen din må kunne nå Bitcoin-noden i det lokale nettverket. Finn IP-adressen til datamaskinen din:



**På macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Enkelt alternativ:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**På Linux** :



```bash
hostname -I | awk '{print $1}'
```



**På Windows** :



```cmd
ipconfig
```



Finn IPv4-adressen (format `192.168.x.x` eller `10.0.x.x`)



### RPC-konfigurasjon



#### Rediger bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Finn filen `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Åpne filen med din foretrukne tekstredigerer, og legg til denne konfigurasjonen for å aktivere RPC-serveren.



**Anbefalt konfigurasjon for å komme i gang (bokmerke)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet**-konfigurasjon (for produksjonsbruk) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Viktig** :




- Signet anbefales på det sterkeste** for dine første tester: applikasjonen er fortsatt under utvikling (beta), og det kan fortsatt finnes feil. Med Signet kan du teste gratis, uten å risikere ekte penger
- Erstatt `192.168.1.0/24` med nettverkets undernett (f.eks. hvis IP-en din er `192.168.68.57`, bruker du `192.168.68.0/24`)



**Sikkerhet**: Generer et sterkt passord :



```bash
openssl rand -base64 32
```



### Initialisering



#### Start på nytt og sjekk



1. Slå av Bitcoin Core helt


2. Start den på nytt for å bruke konfigurasjonen




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Når Bitcoin Core starter opp for første gang, vil den laste ned og synkronisere bokmerkeblokkjeden. Denne operasjonen er mye raskere enn på mainnet (bare noen få minutter). Vent til synkroniseringen er fullført før du fortsetter.



![CRÉATION DE WALLET](assets/fr/04.webp)



Når du har synkronisert, oppretter du en ny portefølje ved å klikke på "Create a new wallet". Gi den et eksplisitt navn, for eksempel `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Din wallet er nå opprettet og klar til å motta bokmerkede bitcoins for testing.



#### Få bokmerkede bitcoins (test)



For å teste Joinstr på bokmerke, trenger du gratis test bitcoins :



![SIGNET FAUCET](assets/fr/06.webp)



Bruk et offentlig bokmerke som :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bokmerke257.bublina.eu.org](https://signet257.bublina.eu.org)



I Bitcoin Core, generate en ny mottaksadresse (fanen "Receive"), kopier den og lim den inn i kranskjemaet. Løs captcha om nødvendig. Du vil motta gratis bokmerkede bitcoins i løpet av sekunder.



## Android-applikasjon



### Installasjon



![APPLICATION ANDROID](assets/fr/07.webp)



Gå til [gitlab.com/invincible-privacy/invincible-privacy/joinstr-kmp/-/releases] (https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) for å laste ned den nyeste APK-versjonen. Last ned filen i Android-nettleseren din, og åpne den for å starte installasjonen. Du må eventuelt tillate installasjon fra ukjente kilder i telefonens sikkerhetsinnstillinger.



### Applikasjonskonfigurasjon



![PERMISSIONS VPN](assets/fr/08.webp)



Ved første oppstart vil Joinstr-applikasjonen be om tillatelser til å kontrollere det innebygde VPN-et. Godta begge tillatelsesforespørslene: OpenVPN-kontroll og VPN-tilkobling. Disse tillatelsene er nødvendige for VPN-integrering, noe som beskytter personvernet ditt i nettverket.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr-applikasjonen er organisert i tre hovedfaner:




- Hjem**: Startskjerm
- Pooler**: Opprette og administrere CoinJoin-bassenger
- Innstillinger**: Applikasjonskonfigurasjon



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigurer innstillinger i fanen "Innstillinger":



**1. Nostr Relay**: Nostr relay-adresse for koordinering av bassenget




- Eksempel: `wss://relay.damus.io`
- Andre anbefalte reléer: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Viktig**: Alle deltakere må bruke **samme Nostr-relé** for å se og bli med i de samme puljene. Hvis du bruker et annet relé, vil du ikke se bassenger som er opprettet på andre reléer



**2. Node-URL**: IP-adressen til Bitcoin-noden (uten port)




- Format: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC Brukernavn** : Brukernavnet som er konfigurert i `rpcuser=` på din bitcoin.conf




- Eksempel: `satoshi



**4. RPC Passord** : Passordet som er angitt i `rpcpassword=` på din bitcoin.conf



**5. RPC-port** : RPC-port avhengig av nettverk




- Mainnet** : `8332`
- Bokmerke**: `38332`



**6. Wallet**: Velg Bitcoin-kjerneporteføljen som inneholder UTXO-ene som skal blandes




- Eksempel: `tuto_joinstr_signet`



**7. VPN-gateway**: Velg en Riseup VPN-server




- Eksempel: `(Paris) vpn07-par.riseup.net`
- Andre tilgjengelige: Amsterdam, Seattle, etc.
- ⚠️ **Viktig**: Alle deltakere i samme pulje må bruke **samme VPN-gateway** for å delta i CoinJoin. Under mikserunden må alle deltakerne vises med samme exit-IP-adresse for å forhindre at nettverksanalyser korrelerer deltakerne



Joinstr-applikasjonen **integrerer** Riseup VPN, noe som forenkler koordineringen mellom deltakerne.



**Viktig** :




- Kontroller at telefonen og datamaskinen er på samme lokale WiFi-nettverk
- VPN-tilkoblingen aktiveres automatisk når du deltar i en pool
- Klikk på **"Lagre"** når du har stilt inn alle parametrene



## Praktisk bruk



### Opprett eller bli med i en pool



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Du har to alternativer for å delta i en CoinJoin:



**Alternativ 1: Opprett et nytt basseng**



Klikk på "Opprett ny pool" i fanen "Pools". Spesifiser pålydende i BTC (f.eks. 0,002 BTC) og ønsket antall deltakere (minimum 2, anbefalt 3-5 for større anonymitet). Programmet venter deretter på at andre brukere skal bli med i bassenget ditt. Når det nødvendige antallet er nådd, begynner utgangsregistreringsprosessen automatisk, og du må velge din UTXO for å blande og klikke på "Registrer".



**⏱️ Viktig**: Puljer utløper etter **10 minutter** uten aktivitet. Hvis det nødvendige antallet deltakere ikke er nådd, blir bassenget automatisk stengt.



**Alternativ 2: Bli med i en eksisterende pool**



I fanen "Vis andre bassenger" kan du bla gjennom de tilgjengelige bassengene som er opprettet av andre brukere. Velg en gruppe som tilsvarer beløpet ditt, og bli med i den. Sørg for at du har konfigurert det samme Nostr-reléet og den samme VPN-gatewayen som de andre deltakerne (se avsnittet Konfigurasjon).



**Regel for valg av UTXO**: Din UTXO må være litt høyere enn puljens pålydende (mellom +500 og +5000 sats overskudd).



**Eksempel**: For en pool på 0,002 BTC (200 000 sats) bruker du en UTXO mellom 200 500 og 205 000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Prosessen er deretter **helt automatisk**: Når inndataene dine er registrert, venter programmet på at alle deltakerne skal registrere sine inndata. Når alle innspillene er registrert, opprettes PSBT, signeres automatisk med dine nøkler og kombineres deretter med signaturene til de andre deltakerne. Til slutt sendes hele transaksjonen ut på Bitcoin-nettverket. Du mottar TXID (transaksjonsidentifikatoren) når kringkastingen er fullført. Ingen manuell manipulering av PSBT er nødvendig på Android.



### on-chain-verifisering



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Når transaksjonen har blitt sendt, vil du motta TXID (transaksjonsidentifikator). Se den på [mempool.space](https://mempool.space) eller i din favorittnettleser. Hvis du vil teste på et bokmerke, bruker du [mempool.space/signet](https://mempool.space/signet).



Du kan observere :





- N oppføringer**: Én per deltaker (i vårt eksempel 2 bidrag)
- N identiske utganger**: nøyaktig beløp av valøren (her, 2 utganger på 0,00199800 BTC hver)
- Flytdiagram**: mempool.space viser visuelt blandingen av innganger og utganger
- Funksjoner** : Transaksjonen kan identifiseres som SegWit, Taproot, RBF osv.



Ettersom alle hovedutganger har samme mengde, er det **umulig å avgjøre hvem som tilhører hvem**. Dette er det grunnleggende prinsippet i CoinJoin: at det ikke er mulig å skille mellom utgangene.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Vær oppmerksom på dette**: Hvis UTXO-ene dine var større enn poolens denominasjon, vil du ha valutautganger (overskudd). Disse UTXOene kan fortsatt spores og må håndteres separat fra de anonymiserte utbetalingene. Kombiner dem aldri med de blandede utgangene dine.



## CoinJoin kvalitets- og anonymitetspakker



Effektiviteten til en CoinJoin måles ved hjelp av dens **anonset**: antall utganger med identisk verdi som produseres av transaksjonen. Jo høyere dette tallet er, desto vanskeligere er det å finne ut hvilken input som tilsvarer hvilken output.



Joinstr genererer for øyeblikket puljer med **2 til 5 deltakere** i gjennomsnitt. Disse tallene er lavere enn tradisjonelle sentraliserte koordinatorer som Wasabi (50-100 deltakere) eller Whirlpool (5-10 deltakere), men det er prisen for desentralisering.



💡 **For å forstå anonymitetssett og beregningen av dem i detalj**, se hele kurset vårt: [Anonymitetssett] (https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. andre CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Andre aktive CoinJoin-løsninger** :




- Ashigaru**: Åpen kildekode-implementering av Whirlpool-protokollen med sentralisert koordinator, men kan distribueres på en desentralisert måte. Fortsetter å operere etter overtakelsen av Samourai Wallet i 2024.
- JoinMarket**: Desentralisert P2P-løsning uten sentral koordinator, basert på en maker/taker-forretningsmodell der "makers" tilfører likviditet og får betalt av "takers".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Det grunnleggende kompromisset**: Joinstr og JoinMarket er de eneste to løsningene uten en sentral koordinator. JoinMarket bruker en P2P-forretningsmodell med økonomiske insentiver, mens Joinstr bruker Nostr for kostnadsfri koordinering. Joinstr ofrer umiddelbar anonymitet i stor skala til fordel for enkelhet (ingen maker/taker-administrasjon) og totalt fravær av koordineringsavgifter.



**Praktisk anbefaling**: For å kompensere for mindre puljer kan du kjøre flere påfølgende runder med CoinJoin med forskjellige deltakere. Fordel rundene og bytt Nostr-stafetter mellom hver runde for å maksimere konfidensialiteten.



Se gjerne vårt komplette kurs om bitcoin-personvern for mer informasjon om dette emnet:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Fordeler og begrensninger



### Høydepunkter



**Forbedret personvern**: Kombinasjonen av Nostr-kommunikasjonskryptering, delt VPN mellom deltakerne og den anbefalte bruken av Tor skaper beskyttelse i flere lag som er vanskelig å omgå.



**Transparente, minimale kostnader**: Ingen koordineringskostnader, kun mining-kostnader deles rettferdig mellom deltakerne. Ingen prosentandel kreves inn av noen operatør.



### Begrensninger å ta hensyn til





- Variabel likviditet**: Mindre puljer, kan vente på at deltakerne kommer sammen
- Prosjekt under utvikling**: Applikasjon i beta, feil mulig. Test først med små mengder på bokmerke
- Sybil-angrep**: Mulighet for at én motstander kontrollerer flere deltakere i puljen



## Beste praksis



**UTXO isolasjon**: Kombiner aldri en blandet UTXO med en ublandet. Bruk en separat portefølje for de anonymiserte resultatene.



**Flere runder er avgjørende**: Utfør minst tre påfølgende runder med forskjellige deltakere. Varier mengder og tidspunkt for å unngå mønstre. Gjennomfør rundene med flere timers mellomrom.



**Nettverksbeskyttelse**: Bruk Tor systematisk i tillegg til det innebygde VPN-et. Generer kortvarige Nostr-nøkler for hver viktige økt.



**Forsiktig fremgang**: Begynn å bokmerke med små mengder.



## Konklusjon



Joinstr representerer en virkelig desentralisert Bitcoin personvernløsning. Ved å bruke Nostr til koordinering elimineres avhengigheten av sentrale koordinatorer, samtidig som brukernes suverenitet bevares.



**For brukere som verdsetter motstand mot sensur og er forberedt på å utføre flere runder med CoinJoin for å kompensere for mindre bassenger.



På bakgrunn av den økende økonomiske kontrollen blir desentraliserte verktøy for å beskytte personvernet stadig viktigere.



## Ressurser



### Offisiell dokumentasjon




- [Joinstrs offisielle nettside](https://joinstr.xyz)
- [Brukerdokumentasjon] (https://docs.joinstr.xyz/users/using-joinstr)
- [Teknisk dokumentasjon] (https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab kildekode](https://gitlab.com/invincible-privacy/joinstr)
- [Android-applikasjon] (https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Veiledninger




- [Electrum plugin tutorial] (https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Komplett guide av Uncensored Tech



### Fellesskap og støtte




- [Telegram Joinstr Group] (https://t.me/joinstr) - Fellesskapsstøtte og bokmerkehjørner
- [Teknisk diskusjon på DelvingBitcoin] (https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Ytterligere verktøy




- [Bokmerke Faucet](https://signetfaucet.com) - Gratis test Bitcoins
- [Alt Signet Faucet] (https://alt.signetfaucet.com) - Faucet alternativ
- [Mempool.space](https://mempool.space) - Block explorer med personvernanalyse