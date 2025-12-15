---
name: Joinstr
description: Decentraliserade CoinJoins via Nostr-nätverket för suverän Bitcoin-konfidentialitet
---

![cover](assets/cover.webp)



Bitcoin-blockkedjans transparens gör det möjligt att spåra transaktionshistoriken. CoinJoins bryter dessa länkar genom att blanda flera samtidiga transaktioner, vilket återställer en sekretessnivå som kan jämföras med kontanter.



Traditionella lösningar förlitar sig dock på en central samordnare som utgör en enda felkälla. Wasabi och Samourai upphörde med sin verksamhet 2024 efter påtryckningar från myndigheterna.



**Joinstr** eliminerar denna svaghet genom att använda det decentraliserade Nostr-nätverket för samordning. Denna applikation med öppen källkod möjliggör verkligt suveräna CoinJoins, där ingen central myndighet kan censurera, övervaka eller avbryta tjänsten.



## Vad är Joinstr?



Joinstr är ett verktyg med öppen källkod som revolutionerar CoinJoins-metoden genom att utnyttja Nostr-protokollet som en samordningsinfrastruktur. Till skillnad från centraliserade lösningar som kräver en dedikerad server förlitar sig Joinstr på ett distribuerat nätverk av Nostr-reläer för att göra det möjligt för deltagare att samordna direkt mellan kamrater.



**Decentraliserad arkitektur** : Nostr-nätverket ersätter den centrala koordinatorn. Deltagare skapar eller ansluter sig till "pooler" genom att skicka krypterade meddelanden via Nostr-reläerna. Denna information (belopp, deltagare, adresser) förblir obegriplig för reläerna, vilket säkerställer att ingen central enhet kan övervaka, censurera eller filtrera CoinJoins.



**SIGHASH_ALL|ANYONECANPAY-mekanism**: Joinstr utnyttjar denna Bitcoin-signaturflagga, vilket gör att varje deltagare endast kan signera sina inmatningar samtidigt som alla utmatningar valideras. Varje användare genererar sin PSBT lokalt och distribuerar den sedan via Nostr. Varje användare genererar sin PSBT lokalt, signerar den och distribuerar den sedan via Nostr. Dina bitcoins förblir under din exklusiva kontroll fram till den slutliga signeringen.



**Filosofi**: Joinstr följer Bitcoin:s cypherpunk-etos och strävar efter tre mål: **motstånd mot censur** (ingen myndighet kan stoppa tjänsten), **total icke-frihetsberövande** (du behåller dina privata nycklar) och **jämlik behandling** (ingen UTXO kan diskrimineras).



### Huvudsakliga egenskaper



**Flexibla pooler**: Till skillnad från fasta valörer kan alla användare skapa en pool med exakt önskat belopp och målantal deltagare, vilket optimerar användningen av UTXO utan artificiell uppdelning.



**Transparenta avgifter**: Inga samordningsavgifter. Endast Bitcoin:s transaktionsavgifter delas lika mellan deltagarna (några tusen satoshis per person).



**Ephemerality**: Ingen användardata lagras. Information överförs via krypterade efemära Nostr-meddelanden, som glöms bort omedelbart efter transaktionen.



### Tillgängliga plattformar



Denna handledning fokuserar på **Android-applikationen**, den enda för närvarande stabila och rekommenderade lösningen. Det finns ett Electrum-plugin men det har kompatibilitetsproblem som gör det instabilt. Ett webbgränssnitt är under utveckling.



## Bitcoin Kärnkonfiguration



Joinstr Android kräver en anslutning till en Bitcoin-nod via RPC. Du måste först konfigurera Bitcoin Core på din dator för att acceptera anslutningar från din telefon.



**Notera**: För mer information om den fullständiga konfigurationen av Bitcoin Core, se våra dedikerade handledning :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Krav på nätverk



#### Leta reda på din lokala IP-adress



Din Android-telefon måste kunna nå din Bitcoin-nod i det lokala nätverket. Hitta IP-adressen till din dator:



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



Hitta IPv4-adressen (format `192.168.x.x` eller `10.0.x.x`)



### RPC-konfiguration



#### Redigera bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Leta reda på filen `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Bibliotek/Applikationsstöd/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Öppna filen med din favorittextredigerare och lägg till den här konfigurationen för att aktivera RPC-servern.



**Rekommenderad konfiguration för att komma igång (bokmärke)** :



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



*konfiguration *mainnet** (för produktionsbruk) :



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



**Viktigt** :




- Signet rekommenderas starkt** för dina första tester: applikationen är fortfarande under utveckling (beta) och det kan fortfarande finnas buggar. Signet låter dig testa gratis, utan att riskera riktiga pengar
- Ersätt `192.168.1.0/24` med ditt nätverks subnät (t.ex. om din IP är `192.168.68.57`, använd `192.168.68.0/24`)



**Säkerhet**: Skapa ett starkt lösenord :



```bash
openssl rand -base64 32
```



### Initialisering



#### Starta om och kontrollera



1. Stäng av Bitcoin Core helt och hållet


2. Starta om den för att tillämpa konfigurationen




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



När Bitcoin Core startas upp för första gången kommer den att ladda ner och synkronisera bokmärkesblockkedjan. Denna operation är mycket snabbare än på mainnet (bara några minuter). Vänta tills synkroniseringen är klar innan du fortsätter.



![CRÉATION DE WALLET](assets/fr/04.webp)



När du har synkroniserat skapar du en ny portfölj genom att klicka på "Skapa en ny wallet". Ge den ett tydligt namn, t.ex. "tuto_joinstr_signet".



![WALLET CRÉÉ](assets/fr/05.webp)



Din wallet är nu skapad och redo att ta emot bokmärkta bitcoins för testning.



#### Få bokmärke bitcoins (test)



För att testa Joinstr på bokmärke behöver du gratis testbitcoins :



![SIGNET FAUCET](assets/fr/06.webp)



Använd ett offentligt bokmärke som :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com] (https://alt.signetfaucet.com)
- [bokmärke257.bublina.eu.org](https://signet257.bublina.eu.org)



I Bitcoin Core, generate en ny mottagningsadress (fliken "Receive"), kopiera den och klistra in den i kranformuläret. Lös captcha om det behövs. Du kommer att få gratis bokmärkta bitcoins inom några sekunder.



## Android-applikation



### Installation



![APPLICATION ANDROID](assets/fr/07.webp)



Gå till [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) för att ladda ner den senaste APK-versionen. Ladda ner filen i din Android-webbläsare och öppna den sedan för att starta installationen. Du måste tillåta installation från okända källor i telefonens säkerhetsinställningar om det behövs.



### Konfiguration av applikation



![PERMISSIONS VPN](assets/fr/08.webp)



Vid första lanseringen kommer Joinstr-programmet att be om behörighet att styra det inbyggda VPN:et. Acceptera båda behörighetsförfrågningarna: OpenVPN-kontroll och VPN-anslutning. Dessa behörigheter krävs för VPN-integration, vilket skyddar din nätverksintegritet.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr-applikationen är organiserad i tre huvudflikar:




- Hem**: Startskärm
- Pooler**: Skapa och hantera CoinJoin-pooler
- Inställningar**: Konfiguration av applikation



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigurera inställningar på fliken "Inställningar":



**1. Nostr relä**: Nostr reläadress för samordning av pool




- Exempel: `wss://relay.damus.io`
- Andra rekommenderade reläer: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Viktigt**: Alla deltagare måste använda **samma Nostr-relä** för att se och gå med i samma pooler. Om du använder ett annat relä kommer du inte att se pooler som skapats på andra reläer



**2. Nodens URL**: IP-adress för din Bitcoin-nod (utan port)




- Format: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC Användarnamn** : Det användarnamn som konfigurerats i `rpcuser=` på din bitcoin.conf




- Exempel: `satoshi



**4. RPC Lösenord** : Det lösenord som anges i `rpcpassword=` på din bitcoin.conf



**5. RPC-port** : RPC-port beroende på nätverk




- Mainnet** : `8332`
- Bokmärke**: `38332`



**6. Wallet**: Välj Bitcoin Core-portföljen som innehåller UTXO:erna som ska blandas




- Exempel: `tuto_joinstr_signet`



**7. VPN-gateway**: Välj en Riseup VPN-server




- Exempel: `(Paris) vpn07-par.riseup.net`
- Andra tillgängliga: Amsterdam, Seattle, etc.
- ⚠️ **Viktigt**: Alla deltagare i samma pool måste använda **samma VPN Gateway** för att delta i CoinJoin. Under mixningsrundan måste alla deltagare uppträda med samma exit-IP-adress för att förhindra att nätverksanalys korrelerar deltagare



Joinstr-applikationen **integreras nativt** i Riseup VPN, vilket förenklar samordningen mellan deltagarna.



**Viktigt** :




- Kontrollera att din telefon och dator är anslutna till samma lokala WiFi-nätverk
- VPN-anslutningen aktiveras automatiskt när du deltar i en pool
- Klicka på **"Spara"** när du har ställt in alla parametrar



## Praktisk användning



### Skapa eller gå med i en pool



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Du har två alternativ för att delta i en CoinJoin:



**Alternativ 1: Skapa en ny pool**



Klicka på "Skapa ny pool" på fliken "Pooler". Ange valören i BTC (t.ex. 0,002 BTC) och önskat antal deltagare (minst 2, rekommenderas 3-5 för större anonymitet). Applikationen väntar sedan på att andra användare ska ansluta sig till din pool. När det önskade antalet har uppnåtts börjar registreringsprocessen automatiskt, och du måste välja din UTXO för att blanda och klicka på "Registrera".



**⏱️ Viktigt**: Pooler upphör att gälla efter **10 minuter** av inaktivitet. Om det erforderliga antalet deltagare inte uppnås kommer poolen att stängas automatiskt.



**Alternativ 2: Gå med i en befintlig pool**



På fliken "Visa andra pooler" kan du bläddra bland de tillgängliga pooler som skapats av andra användare. Välj en pool som motsvarar ditt belopp och gå med i den. Kontrollera att du har konfigurerat samma Nostr-relä och VPN-gateway som de andra deltagarna (se avsnittet Konfiguration).



**UTXO urvalsregel**: Din UTXO måste vara något högre än poolens valör (mellan +500 och +5000 sats överskott).



**Exempel**: För en pool på 0,002 BTC (200 000 sats), använd en UTXO mellan 200 500 och 205 000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Processen är sedan **helt automatisk**: när din inmatning har registrerats väntar programmet på att alla deltagare ska registrera sina inmatningar. När alla inmatningar har registrerats skapas PSBT, signeras automatiskt med dina nycklar och kombineras sedan med de andra deltagarnas signaturer. Slutligen sänds den fullständiga transaktionen ut i Bitcoin-nätverket. Du får TXID (transaktionsidentifieraren) när sändningen är klar. Ingen manuell hantering av PSBT krävs på Android.



### on-chain verifiering



![TRANSACTION MEMPOOL](assets/fr/12.webp)



När transaktionen har sänts kommer du att få TXID (transaktionsidentifieraren). Visa den på [mempool.space](https://mempool.space) eller din favoritwebbläsare. För att testa på ett bokmärke, använd [mempool.space/signet](https://mempool.space/signet).



Du kan observera :





- N poster**: En per deltagare (i vårt exempel 2 bidrag)
- N identiska utgångar**: exakt belopp för valören (här, 2 utgångar på 0,00199800 BTC vardera)
- Flödesschema**: mempool.space visar visuellt mixen av inmatningar och utmatningar
- Egenskaper** : Transaktionen kan identifieras som SegWit, Taproot, RBF, etc.



Eftersom alla huvudutgångar har samma belopp är det **omöjligt att avgöra vilken som tillhör vem**. Detta är den grundläggande principen i CoinJoin: att utdata inte kan särskiljas.



**Exempel på transaktionssignum** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Observera**: Om dina UTXO:er var större än poolens denominering kommer du att ha valutautflöden (överskott). Dessa UTXO:er är spårbara och måste hanteras separat från dina anonymiserade utflöden. Kombinera dem aldrig med dina blandade utflöden.



## CoinJoin kvalitets- och anonymitetspaket



Effektiviteten hos en CoinJoin mäts genom dess **anonset**: antalet outputs av identiskt värde som produceras av transaktionen. Ju högre detta antal är, desto svårare är det att avgöra vilken input som motsvarar vilken output.



Joinstr genererar för närvarande pooler med **2 till 5 deltagare** i genomsnitt. Dessa siffror är lägre än traditionella centraliserade samordnare som Wasabi (50-100 deltagare) eller Whirlpool (5-10 deltagare), men det är priset för decentralisering.



💡 **För att förstå anonymitetsuppsättningar och deras beräkning i detalj**, se vår fullständiga kurs: [Anonymitetsuppsättningar] (https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr jämfört med andra CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Andra aktiva CoinJoin-lösningar** :




- Ashigaru**: Open source-implementering av Whirlpool-protokollet med centraliserad koordinator men som kan distribueras på ett decentraliserat sätt. Fortsätter att fungera efter att Samourai Wallet har tagits i besittning 2024.
- JoinMarket**: Decentraliserad P2P-lösning utan central koordinator, baserad på en maker/taker-affärsmodell där "makers" tillhandahåller likviditet och ersätts av "takers".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Den grundläggande avvägningen**: Joinstr och JoinMarket är de enda två lösningarna utan en central koordinator. JoinMarket använder en P2P-affärsmodell med ekonomiska incitament, medan Joinstr använder Nostr för kostnadsfri samordning. Joinstr offrar omedelbar anonymitet i stor skala till förmån för enkelhet (ingen hantering av maker/taker) och total avsaknad av samordningsavgifter.



**Praktisk rekommendation**: För att kompensera för mindre pooler, kör flera på varandra följande omgångar av CoinJoin med olika deltagare. Sprid ut dina omgångar och byt Nostr-reläer mellan varje omgång för att maximera din konfidentialitet.



Läs gärna vår kompletta kurs om bitcoin privacy för mer information om detta ämne:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Fördelar och begränsningar



### Höjdpunkter



**Förbättrad integritet**: Kombinationen av Nostr-kommunikationskryptering, delad VPN mellan deltagarna och den rekommenderade användningen av Tor skapar ett flerskiktat skydd som är svårt att kringgå.



**Transparenta, minimala kostnader**: Inga samordningskostnader, endast mining-kostnader delas rättvist mellan deltagarna. Ingen procentsats tas ut av någon operatör.



### Begränsningar att ta hänsyn till





- Variabel likviditet**: Mindre pooler, kan vänta på att deltagare ska gå samman
- Projekt pågår**: Applikation i beta, buggar möjliga. Testa först med små mängder på bokmärke
- Sybil-attacker**: Möjlighet för en motståndare att kontrollera flera pooldeltagare



## Bästa praxis



**UTXO isolering**: Kombinera aldrig en blandad UTXO med en oblandad. Använd en separat portfölj för dina anonymiserade utdata.



**Flera rundor är nödvändiga**: Utför minst 3 på varandra följande rundor med olika deltagare. Variera mängder och tidpunkter för att undvika mönster. Placera omgångarna med flera timmars mellanrum.



**Nätverksskydd**: Använd Tor systematiskt utöver det inbyggda VPN:et. Generera efemära Nostr-nycklar för varje viktig session.



**Försiktiga framsteg**: Börja med små mängder bokmärken.



## Slutsats



Joinstr representerar en verkligt decentraliserad Bitcoin-sekretesslösning. Genom att använda Nostr för samordning elimineras beroendet av centrala samordnare samtidigt som användarnas suveränitet bevaras.



** För användare som värdesätter motstånd mot censur och är beredda att utföra flera omgångar CoinJoin för att kompensera för mindre pooler.



Mot bakgrund av den ökande finansiella granskningen blir decentraliserade verktyg för att skydda den personliga integriteten allt viktigare.



## Resurser



### Officiell dokumentation




- [Joinstr officiella webbplats](https://joinstr.xyz)
- [Användardokumentation] (https://docs.joinstr.xyz/users/using-joinstr)
- [Teknisk dokumentation] (https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab källkod](https://gitlab.com/invincible-privacy/joinstr)
- [Android-applikation] (https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Handledning




- [Electrum plugin-handledning] (https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Komplett guide av Uncensored Tech



### Gemenskap och stöd




- [Telegram Joinstr Group] (https://t.me/joinstr) - Gemenskapsstöd och bokmärkeshörn
- [Teknisk diskussion om DelvingBitcoin] (https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Ytterligare verktyg




- [Bokmärke Faucet](https://signetfaucet.com) - Gratis test Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternativ
- [Mempool.space](https://mempool.space) - Block explorer med integritetsanalys