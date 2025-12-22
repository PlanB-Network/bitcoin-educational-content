---
name: Joinstr
description: Gedecentraliseerde CoinJoins via het Nostr netwerk voor soevereine Bitcoin vertrouwelijkheid
---

![cover](assets/cover.webp)



De transparantie van de Bitcoin blockchain maakt het mogelijk om de transactiegeschiedenis te traceren. CoinJoins verbreken deze banden door meerdere gelijktijdige transacties te mengen, waardoor een niveau van vertrouwelijkheid wordt hersteld dat vergelijkbaar is met contant geld.



Traditionele oplossingen vertrouwen echter op een centrale coördinator als een centraal storingspunt. Wasabi en Samourai staakten hun activiteiten in 2024 onder druk van de regelgeving.



**Joinstr** elimineert deze zwakte door gebruik te maken van het gedecentraliseerde Nostr netwerk voor coördinatie. Deze open source applicatie maakt echt soevereine CoinJoins mogelijk, waarbij geen enkele centrale autoriteit de dienst kan censureren, controleren of onderbreken.



## Wat is Joinstr?



Joinstr is een open source tool die een revolutie teweegbrengt in de CoinJoins aanpak door gebruik te maken van het Nostr protocol als coördinatie-infrastructuur. In tegenstelling tot gecentraliseerde oplossingen die een toegewijde server vereisen, vertrouwt Joinstr op een gedistribueerd netwerk van Nostr relais om deelnemers in staat te stellen rechtstreeks te coördineren tussen peers.



**Gedecentraliseerde architectuur** : Het Nostr-netwerk vervangt de centrale coördinator. Deelnemers creëren of sluiten zich aan bij "pools" door gecodeerde aankondigingen te posten via de Nostr relais. Deze informatie (bedragen, deelnemers, adressen) blijft onbegrijpelijk voor de relais, zodat geen enkele centrale entiteit CoinJoins kan controleren, censureren of filteren.



**SIGHASH_ALL|ANYONECANPAY mechanisme**: Joinstr maakt gebruik van deze Bitcoin handtekeningvlag, waardoor elke deelnemer alleen zijn of haar invoer kan ondertekenen terwijl alle uitvoer wordt gevalideerd. Elke gebruiker genereert zijn of haar PSBT lokaal en verdeelt deze via Nostr. Elke gebruiker genereert zijn PSBT lokaal, ondertekent het en verspreidt het dan via Nostr. Uw bitcoins blijven onder uw exclusieve controle tot de uiteindelijke ondertekening.



**Filosofie**: Joinstr volgt het Bitcoin cypherpunk ethos en streeft drie doelen na: **weerstand tegen censuur** (geen enkele autoriteit kan de dienst stoppen), **totale niet-custodialiteit** (je behoudt je privésleutels) en **gelijke behandeling** (geen enkele UTXO mag gediscrimineerd worden).



### Belangrijkste kenmerken



**Flexibele pools**: In tegenstelling tot vaste coupures kan elke gebruiker een pool aanmaken met het exacte gewenste bedrag en het beoogde aantal deelnemers, waardoor het gebruik van UTXO wordt geoptimaliseerd zonder kunstmatige splitsing.



**Transparante kosten**: Geen coördinatiekosten. Alleen Bitcoin transactiekosten worden gelijk verdeeld onder de deelnemers (een paar duizend satoshis per persoon).



**Ephemerality**: Er worden geen gebruikersgegevens bewaard. Informatie wordt verzonden via versleutelde efemere Nostr-berichten, die na de transactie onmiddellijk worden vergeten.



### Beschikbare platforms



Deze tutorial richt zich op de **Android applicatie**, de enige momenteel stabiele en aanbevolen oplossing. Er bestaat een Electrum plugin, maar die heeft compatibiliteitsproblemen waardoor hij onstabiel is. Een webinterface is in ontwikkeling.



## Bitcoin Kernconfiguratie



Joinstr Android vereist een verbinding met een Bitcoin knooppunt via RPC. Je moet eerst Bitcoin Core op je computer configureren om verbindingen van je telefoon te accepteren.



**Noot**: Voor meer details over de volledige configuratie van Bitcoin Core, zie onze speciale tutorials:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Netwerkvereisten



#### Lokaliseer uw lokale IP-adres



Je Android-telefoon moet het Bitcoin knooppunt op het lokale netwerk kunnen bereiken. Zoek het IP-adres van je computer:



**Op macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Eenvoudig alternatief:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Op Linux** :



```bash
hostname -I | awk '{print $1}'
```



**Op Windows** :



```cmd
ipconfig
```



Zoek het IPv4-adres (formaat `192.168.x.x` of `10.0.x.x`)



### RPC configuratie



#### bitcoin.conf bewerken



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Zoek je `bitcoin.conf` bestand:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: ~/Library/Toepassingsondersteuning/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Open het bestand met je favoriete teksteditor en voeg deze configuratie toe om de RPC server te activeren.



**Aanbevolen configuratie om aan de slag te gaan (bladwijzer)** :



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



**mainnet** configuratie (voor productiegebruik) :



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



**Belangrijk** :




- Signet wordt sterk aanbevolen** voor je eerste tests: de applicatie is nog in ontwikkeling (bèta) en er kunnen nog bugs in zitten. Met Signet kun je gratis testen, zonder echt geld te riskeren
- Vervang `192.168.1.0/24` door het subnet van je netwerk (als je IP bijvoorbeeld `192.168.68.57` is, gebruik dan `192.168.68.0/24`)



**Veiligheid**: Genereer een sterk wachtwoord :



```bash
openssl rand -base64 32
```



### Initialisatie



#### Opnieuw opstarten en controleren



1. Bitcoin Core volledig afsluiten


2. Start het programma opnieuw op om de configuratie toe te passen




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Wanneer Bitcoin Core voor de eerste keer opstart, zal het de bookmark blockchain downloaden en synchroniseren. Deze operatie is veel sneller dan op mainnet (slechts enkele minuten). Wacht tot de synchronisatie voltooid is voordat je verder gaat.



![CRÉATION DE WALLET](assets/fr/04.webp)



Eenmaal gesynchroniseerd, maak je een nieuwe portefeuille aan door te klikken op "Maak een nieuwe wallet". Geef het een expliciete naam zoals `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Je wallet is nu aangemaakt en klaar om gebookmarkte bitcoins te ontvangen om te testen.



#### Bitcoins met bladwijzers krijgen (test)



Om Joinstr op bookmark te testen, heb je gratis testbitcoins nodig:



![SIGNET FAUCET](assets/fr/06.webp)



Gebruik een openbare bladwijzer zoals :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



In Bitcoin Core, generate een nieuw ontvangstadres ("Ontvangst" tab), kopieer het en plak het in het kraanformulier. Los indien nodig de captcha op. Je ontvangt binnen enkele seconden gratis Bitcoins.



## Android-toepassing



### Installatie



![APPLICATION ANDROID](assets/fr/07.webp)



Ga naar [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) om de laatste APK versie te downloaden. Download het bestand in je Android browser en open het om de installatie te starten. Indien nodig moet je installatie van onbekende bronnen toestaan in de beveiligingsinstellingen van je telefoon.



### Toepassingsconfiguratie



![PERMISSIONS VPN](assets/fr/08.webp)



Bij de eerste start vraagt de Joinstr-toepassing om toestemming om de ingebouwde VPN te bedienen. Accepteer beide verzoeken om toestemming: OpenVPN controle en VPN verbinding. Deze toestemmingen zijn nodig voor VPN-integratie, die je netwerkprivacy beschermt.



![INTERFACE APPLICATION](assets/fr/09.webp)



De Joinstr-toepassing is onderverdeeld in drie hoofdtabbladen:




- Home**: Beginscherm
- Pools**: CoinJoin pools aanmaken en beheren
- Instellingen**: Toepassingsconfiguratie



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Configureer de instellingen op het tabblad "Instellingen":



**1. Nostr-relais**: Nostr relay-adres voor poolcoördinatie




- Voorbeeld: `wss://relay.damus.io`
- Andere aanbevolen relais: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Belangrijk**: Alle deelnemers moeten dezelfde Nostr relay** gebruiken om dezelfde pools te zien en zich bij dezelfde pools aan te sluiten. Als u een andere relay gebruikt, ziet u geen pools die op andere relays zijn aangemaakt



**2. Node URL**: IP-adres van uw Bitcoin knooppunt (zonder poort)




- Formaat: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC Gebruikersnaam** : De gebruikersnaam geconfigureerd in `rpcuser=` op uw bitcoin.conf




- Voorbeeld: `satoshi



**4. RPC wachtwoord** : Het wachtwoord ingesteld in `rpcpassword=` op uw bitcoin.conf



**5. RPC poort** : RPC poort afhankelijk van netwerk




- Mainnet** : `8332`
- Bladwijzer**: `38332`



**6. Wallet**: Selecteer het Bitcoin kernportfolio met de UTXO's die gemengd moeten worden




- Voorbeeld: `tuto_joinstr_signet`



**7. VPN-gateway**: Selecteer een Riseup VPN-server




- Voorbeeld: `(Paris) vpn07-par.riseup.net`
- Andere beschikbaar: Amsterdam, Seattle, enz.
- ⚠️ **Belangrijk**: Alle deelnemers in dezelfde pool moeten dezelfde **VPN Gateway** gebruiken om deel te nemen aan CoinJoin. Tijdens de mixronde moeten alle deelnemers verschijnen met hetzelfde exit IP-adres om te voorkomen dat netwerkanalyses deelnemers met elkaar in verband brengen



De Joinstr-applicatie **integreert** de Riseup VPN, wat de coördinatie tussen de deelnemers vereenvoudigt.



**Belangrijk** :




- Zorg ervoor dat je telefoon en computer zich op hetzelfde lokale WiFi-netwerk bevinden
- De VPN-verbinding wordt automatisch geactiveerd als u deelneemt aan een pool
- Klik op **"Opslaan"** als je alle parameters hebt ingesteld



## Praktisch gebruik



### Een pool maken of lid worden



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Je hebt twee opties om deel te nemen aan een CoinJoin:



**Optie 1: Maak een nieuwe pool**



Klik op "Nieuwe pool aanmaken" in de tab "Pools". Specificeer de denominatie in BTC (bijv. 0,002 BTC) en het gewenste aantal deelnemers (minimaal 2, aanbevolen 3-5 voor meer anonimiteit). De applicatie wacht dan op andere gebruikers om zich bij je pool aan te sluiten. Zodra het vereiste aantal is bereikt, begint het registratieproces voor de uitvoer automatisch en moet je je UTXO selecteren om te mengen en op "Registreren" klikken.



**⏱️ Belangrijk**: Pools vervallen na **10 minuten** inactiviteit. Als het vereiste aantal deelnemers niet wordt bereikt, wordt de pool automatisch gesloten.



**Optie 2: Sluit je aan bij een bestaande pool**



Blader op het tabblad "Andere pools bekijken" door de beschikbare pools die door andere gebruikers zijn aangemaakt. Selecteer een pool die overeenkomt met uw hoeveelheid en sluit u hierbij aan. Zorg ervoor dat je dezelfde Nostr relay en VPN Gateway hebt geconfigureerd als de andere deelnemers (zie sectie Configuratie).



**UTXO selectieregel**: Jouw UTXO moet iets hoger zijn dan de waarde van de pool (tussen +500 en +5000 sats overschot).



**Voorbeeld**: Voor een pool van 0,002 BTC (200.000 sats), gebruik een UTXO tussen 200.500 en 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Het proces verloopt dan **volautomatisch**: zodra jouw input is geregistreerd, wacht de applicatie tot alle deelnemers hun input hebben geregistreerd. Zodra alle inputs zijn geregistreerd, wordt de PSBT aangemaakt, automatisch ondertekend met uw sleutels en vervolgens gecombineerd met de handtekeningen van de andere deelnemers. Ten slotte wordt de volledige transactie op het Bitcoin netwerk uitgezonden. U ontvangt de TXID (transactie-identificatie) zodra de broadcast is voltooid. Op Android is geen handmatige manipulatie van PSBT vereist.



### on-chain verificatie



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Zodra de transactie is uitgezonden, ontvang je de TXID (transaction identifier). Bekijk het op [mempool.space](https://mempool.space) of je favoriete browser. Om te testen op een bladwijzer, gebruik je [mempool.space/signet](https://mempool.space/signet).



U kunt observeren:





- N inzendingen**: Eén per deelnemer (in ons voorbeeld, 2 vermeldingen)
- N identieke uitgangen**: exact bedrag van de denominatie (hier 2 uitgangen van elk 0,00199800 BTC)
- Stroomdiagram**: mempool.space toont visueel de mix van inputs en outputs
- Kenmerken** : De transactie kan worden geïdentificeerd als SegWit, Taproot, RBF, enz.



Omdat alle hoofduitgangen dezelfde hoeveelheid hebben, is het **onmogelijk om te bepalen welke bij wie hoort**. Dit is het fundamentele principe van CoinJoin: de ononderscheidbaarheid van uitgangen.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Let op**: Als je UTXO's groter waren dan de denominatie van de pool, heb je deviezenuitvoer (overschotten). Deze UTXO's blijven traceerbaar en moeten apart van je geanonimiseerde outputs worden beheerd. Combineer ze nooit met je gemengde outputs.



## CoinJoin kwaliteit en anonimiteitspakketten



De efficiëntie van een CoinJoin wordt gemeten aan de hand van de **anonset**: het aantal outputs van identieke waarde die door de transactie worden geproduceerd. Hoe hoger dit getal, hoe moeilijker het is om te bepalen welke input overeenkomt met welke output.



Joinstr genereert momenteel pools van gemiddeld **2 tot 5 deelnemers**. Deze cijfers zijn lager dan traditionele gecentraliseerde coördinatoren zoals Wasabi (50-100 deelnemers) of Whirlpool (5-10 deelnemers), maar dat is de prijs van decentralisatie.



💡 **Om anonimiteitensets en hun berekening in detail te begrijpen**, zie onze volledige cursus: [Anonimiteitensets](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. andere CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Andere actieve CoinJoin oplossingen** :




- Ashigaru**: Open-source implementatie van het Whirlpool protocol met gecentraliseerde coördinator, maar decentraal inzetbaar. Blijft werken na de inbeslagname van Samourai Wallet in 2024.
- JoinMarket**: Gedecentraliseerde P2P oplossing zonder centrale coördinator, gebaseerd op een maker/nemer bedrijfsmodel waarbij "makers" liquiditeit verschaffen en worden beloond door "nemers".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**De fundamentele afweging**: Joinstr en JoinMarket zijn de enige twee oplossingen zonder centrale coördinator. JoinMarket gebruikt een P2P bedrijfsmodel met financiële prikkels, terwijl Joinstr Nostr gebruikt voor kostenloze coördinatie. Joinstr offert onmiddellijke anonimiteit op grote schaal op ten voordele van eenvoud (geen maker/nemer beheer) en de totale afwezigheid van coördinatiekosten.



**Praktische aanbeveling**: Om kleinere groepen te compenseren, kun je verschillende opeenvolgende CoinJoin rondes doen met verschillende deelnemers. Verdeel je rondes en wissel tussen elke ronde van Nostr-relais om de vertrouwelijkheid te maximaliseren.



Raadpleeg gerust onze volledige cursus over bitcoin privacy voor meer informatie over dit onderwerp:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Voordelen en beperkingen



### Hoogtepunten



**Verbeterde privacy**: De combinatie van Nostr communicatie-encryptie, gedeelde VPN tussen deelnemers en het aanbevolen gebruik van Tor creëert meerlaagse bescherming die moeilijk te omzeilen is.



**Transparant, minimale kosten**: Geen coördinatiekosten, alleen mining kosten worden eerlijk verdeeld tussen de deelnemers. Geen percentage geheven door een operator.



### Te overwegen beperkingen





- Variabele liquiditeit**: Kleinere pools, kan wachten tot deelnemers samenkomen
- Project in uitvoering**: Toepassing in bèta, bugs mogelijk. Test eerst met kleine hoeveelheden op bladwijzer
- Sybil-aanvallen**: Mogelijkheid dat één tegenstander meerdere pooldeelnemers controleert



## Beste praktijken



**UTXO isolatie**: Combineer nooit een gemengde UTXO met een ongemengde. Gebruik een aparte portfolio voor je geanonimiseerde uitvoer.



**Meerdere rondes zijn essentieel**: Voer minimaal 3 opeenvolgende rondes uit met verschillende deelnemers. Varieer in hoeveelheden en timing om patronen te voorkomen. Spreid rondes enkele uren uit elkaar.



**Netwerkbeveiliging**: Gebruik systematisch Tor naast de ingebouwde VPN. Genereer kortstondige Nostr-sleutels voor elke belangrijke sessie.



**Voorzichtige vooruitgang**: Begin met kleine hoeveelheden.



## Conclusie



Joinstr vertegenwoordigt een echt gedecentraliseerde Bitcoin privacyoplossing. Door Nostr te gebruiken voor de coördinatie elimineert het de afhankelijkheid van centrale coördinatoren terwijl de soevereiniteit van de gebruiker behouden blijft.



**Voor gebruikers die waarde hechten aan weerstand tegen censuur en bereid zijn meerdere rondes CoinJoin uit te voeren om kleinere pools te compenseren.



Tegen een achtergrond van toenemende financiële controle worden gedecentraliseerde tools om privacy te beschermen essentieel.



## Bronnen



### Officiële documentatie




- [Officiële website van Joinstr](https://joinstr.xyz)
- [Gebruikersdocumentatie](https://docs.joinstr.xyz/users/using-joinstr)
- [Technische documentatie](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab broncode](https://gitlab.com/invincible-privacy/joinstr)
- [Android-toepassing](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Lesmateriaal




- [Electrum plugin tutorial](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Complete handleiding door Uncensored Tech



### Gemeenschap en ondersteuning




- [Telegram Joinstr Group](https://t.me/joinstr) - Gemeenschapsondersteuning en bladwijzerhoeken
- [Technische discussie over DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Extra hulpmiddelen




- [Bladwijzer Faucet](https://signetfaucet.com) - Gratis test Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternatief
- [Mempool.space](https://mempool.space) - Block explorer met privacy analyse