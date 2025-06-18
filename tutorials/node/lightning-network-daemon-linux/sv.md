---
name: Lightning Network Daemon (Linux)
description: Installera och köra Lightning Network Daemon på Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network är en andra Layer av Bitcoin, vilket gör att den kan anta blixtsnabba dimensioner, särskilt tack vare snabbheten och den låga kostnaden för de transaktioner som den erbjuder.



I den här handledningen installerar vi Lightning Network Daemon-implementeringen på vår Linux-maskin (Ubuntu 24.04-distribution).



## Vad är Lightning Network Daemon?



Lightning Network Daemon är en komplett Go-implementering av Lightning Network. Den skapades av Lightning Labs och låter dig köra en fullständig instans av en Lightning-nod på din maskin.


Med andra ord, med denna implementering kan du :





- Interagera med Lightning Network**: Du kan använda kommandorader för att skapa Lightning-portföljer, hantera betalningskanaler och -vägar och mycket mer, direkt från din maskinterminal.
- Länka en avlägsen Bitcoin-nod eller din egen Bitcoin Core-instans**: Med LND kan du länka en Bitcoin-instans och använda den som din backend. För att använda den här implementeringen behöver du inte köra en Bitcoin Core-instans på din maskin.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Varför ha en egen Lightning-nod?


Lightning är ett Bitcoin-överlägg som optimerar överföringsprocessen och minskar transaktionskostnaderna.



Genom att rotera din Lightning-nod får du suveränitet och autonomi. Du har kontroll över dina medel, så kom ihåg:



"Inte dina nycklar, inte dina bitcoins."



På så sätt ökar säkerheten och integriteten för dina data när du kör en Lightning-nod på följande sätt:





- Total kontroll**: Hantera dina egna betalningskanaler, bli din egen bank och var herre över dina tillgångar.
- Konfidentialitet**: Transaktioner utan att förlita dig på att tredje part skyddar din integritet.
- Lärande och självständighet**: Tack vare kommandona `lncli` kan du bättre förstå Lightnings underliggande processer genom att själv tillämpa dem från din terminal.
- Decentralisering**: Spela en aktiv roll i att stärka och decentralisera Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Du har två alternativ för att köra en instans av LND-implementeringen på vår maskin. Vi kan antingen ställa in miljön på vår egen maskin för att köra lokalt, eller installera LND från en Docker-container. Här kommer vi att koncentrera oss på det första alternativet och se hur vi går vidare med Docker i en senare handledning.


## Installera LND från källkod



### Förkunskapskrav


Eftersom LND är skriven i Go måste du se till att du har GoLang-miljön och de nödvändiga beroendena på din Linux-maskin.





- Krav på hårdvara:**


För en smidig och sömlös upplevelse måste din maskin ha den kapacitet som krävs för att köra din LND Lightning-nod.



Du kommer att behöva :


1. **8 GB RAM** för optimal flytbarhet,


2. **En flerkärnig processor (fyrkärnig eller mer)** för att effektivt hantera din nods åtgärder,


3. **Minst 5 GB diskutrymme** för beskuret nodläge och 1 TB för att köra Bitcoin Core (valfritt om du använder en fjärrnod)





- Installera användbara beroenden:**


Med kommandot nedan kan du installera de verktyg du behöver för att köra LND på din maskin. Du behöver bland annat installera `Git`, ett versionshanteringsverktyg, och `make`, som kan exekvera och bygga LND-implementationen från källkod.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Installera GoLang på din Linux-maskin**



Från och med datumet för denna handledning kräver LND version 1.23.6 av Go*** för installation.



Om du redan hade en tidigare version installerad tar du bort den för den nya Go-installationen.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfiguration av Go**-miljön


I filen `~/.bashrc` initialiserar du följande miljövariabler för att lägga till Go i ditt Linux-system.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Kontroll av installationen** (på franska)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Klona LND GitHub-förvaret



Använd git för att få en kopia av LND:s källkod lokalt på din dator


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Bygga och installera



Med det tidigare installerade verktyget `make` kan du bygga en körbar fil från LND:s källkod och fortsätta med installationen.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Installera LND på din maskin



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Kontrollera din installation** (på franska)



För att se till att allt gick smidigt kan du köra det här kommandot för att få reda på vilken version av LND du kör för närvarande.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Underhåll och uppgraderingar



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **VIKTIGT**: LND-uppdateringar kan kräva nyare versioner av Go, så se till att uppdatera ditt system för att undvika beroendeproblem under installationen.


### Konfigurera Lightning Network Daemon



Konfigurationen av en Lightning LND-nod liknar den för Bitcoin och utförs i en konfigurationsfil som innehåller alla parametrar för din nod. För att göra detta kan du skapa en dold mapp `.LND` i roten på din maskin och sedan skapa din konfigurationsfil `LND.conf` i denna mapp.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





I konfigurationsfilen kan du ställa in din LND-nod.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Förstå din konfiguration



Det är viktigt att du förstår vilken minimikonfiguration du behöver för en korrekt och fullständig installation av din LND-nod.



Baserat på innehållet i filen `~/.LND/LND.conf`, här är detaljerna för fälten:





- noseedbackup**: Gör det möjligt för dig att välja om du vill att LND ska utföra automatiska säkerhetskopior av dina portföljer.  Om du ställer in den här egenskapen på "0" kan du manuellt spara återställningsinformation på en personligt vald säker plats.





- felsökningsnivå**: Ger dig möjlighet att definiera detaljnivån för fel och loggar i händelse av fel som uppstår under en åtgärd.





- Bitcoin.aktiv**: Instruerar LND att fungera som en Bitcoin-nod och interagera med Bitcoin-nätverket.





- Bitcoin.Mainnet**: Anger att LND ska ansluta till Bitcoin:s huvudnätverk (Mainnet), du kan ange värdena `bitcoind.signet` och `bitcoind.regtest` för nätverken Bitcoin Signet respektive Bitcoin Regtest





- Bitcoin.nod**: Anger vilken typ av Bitcoin-nod som LND ska ansluta till.





- Bitcoin.rpcuser** och **Bitcoin.rpcpassword** : Representera.


respektive inloggningarna (användare, lösenord) för att ansluta till din Bitcoin-nod





- bitcoind.zmqpubrawblock** och **bitcoind.zmqpubrawtx**: definierar ZeroMQ-slutpunkter för att ta emot meddelanden om nya block och transaktioner i Bitcoin-nätverket.




## Kontrollera din installation med LND



Du kommer förmodligen att vilja se till att processen har lyckats och att du synkroniserar med Lightning Network för att hålla din nodinformation uppdaterad.



För att starta LND-implementeringen och få information om din nod skriver du bara kommandot :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Utföra åtgärder på LND



När installationen har slutförts och kontrollerats kan du börja använda den.


Här är de viktigaste kommandona för att du ska komma igång.



### Skapa en portfölj


Din Lightning-portfölj är det första steget i alla åtgärder för att förvalta dina pengar.



⚠️ **VIKTIGT**: Notera noga din 24 ord långa **seed-fras**. Du behöver den för att få tillbaka dina pengar om det skulle uppstå problem.



Spara också ditt Wallet-lösenord så att du kan låsa upp det med kommandot `lncli unlock` när du startar om din LND-nod.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Kontrollera ditt saldo



Konsultera dina konton direkt från din terminal:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Information om din nod



Använd kommandot nedan för att ta reda på vilka kanaler som är aktiva på din nod.



```bash
lncli listchannels
```



Du kan också få en lista över de noder som du är ansluten till.



```bash
lncli listpeers
```



### Hantering av kanaler



En Lightning-kanal ger dig möjlighet att ha en **direkt, parvis anslutning med en annan nod på Lightning Network**. I den här kanalen kan du fritt använda Exchange Satoshis upp till kanalens kapacitet.



### Anslut till en nod



Att ansluta till andra Lightning-noder är en grundläggande åtgärd om du vill delta aktivt och dra nytta av kraften i Lightning.



För att ansluta till en peer (Lightning-nod) behöver du tre uppgifter:




- Nodens publika nyckel**: Detta är nodens unika identifierare i Bitcoin-nätverket;
- IP** : IP-adressen för den maskin som noden är installerad på;
- PORT** :  Den port som är öppen på den maskin som tillåter kommunikation med denna nod.



Du kan hitta noder att ansluta till på [amboss] (https://amboss.space/), en plattform som listar information om Lightning-noder.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Se till att du ansluter till **tillförlitliga noder** för att bevara integriteten i ditt eget system. Här är några rekommendationer för att välja rätt anslutningar.





- Geografisk diversifiering**: Anslut till noder i olika regioner.





- Rykte**: Välj noder med god tillgänglighet.





- Kapacitet**: Välj knutar med god likviditet.





- Avgifter**: Checkroutingavgifter.


### Öppna en betalningskanal


För att öppna en betalningskanal ska du se till att du är **ansluten** till peer-noden och sedan ange den **kapacitet** (det belopp i satoshis) som du vill blockera i den här kanalen.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Skapa en blixt Invoice



En Lightning Invoice representerar en teckensträng som uttrycker din önskan att få satoshis i din Lightning Wallet.


Genom att skapa Lightning-fakturor med din egen nod kan du skydda dina uppgifter (geografiska och personliga) och ger dig 100% autonomi över hanteringen av dina medel.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Betalning av en blixt Invoice



```bash
lncli payinvoice <FACTURE>
```


### Stäng en kanal



Det finns två sätt att stänga en aktiv kanal på din aktuella nod.





- Stängning av kooperativ**: Detta signalerar att din nod vill dra sig ur betalningskanalen, vilket säkerställer att pågående uppgifter slutförs och att data säkerhetskopieras för att undvika förlust av medel.


```
lncli closechannel <ID_CANAL>
```




- Tvingad stängning**: ⚠️ Bör undvikas om möjligt, eftersom denna åtgärd avbryter pågående processer i din betalningskanal och ökar risken för att du förlorar pengar.


```
lncli closechannel --force <ID_CANAL>
```


## Bästa praxis och säkerhet för din LND-nod.


Säkerhet är av yttersta vikt när du använder en Bitcoin/Blixtnod. Här följer några punkter för att stärka säkerheten i din installation:





- Förvara din `seed-fras` på en säker plats utanför nätet.





- Gör regelbundna säkerhetskopior av filen `~/.LND/channel.backup`: Den här filen sparar dina kanaltillstånd varje gång en ny kanal öppnas (eller en gammal kanal stängs) på din nod.


⚠️ Gör det möjligt att återställa kanaler och återvinna medel som blockerats i betalningskanaler i händelse av dataförlust eller nodfel



Du kan återställa dina pengar med kommandot nedan genom att ange sökvägen för säkerhetskopian av den här filen:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Se till att du har sparat din Lightning Wallet:s återställningsord och lösenord.
- Håll ditt system uppdaterat.



## Aktuell felsökning


### Frekventa problem




- bitcoind anslutningsfel** : Kontrollera dina inloggningsuppgifter för RPC
- Synkronisering blockerad** : Kontrollera din Internet-anslutning
- Fel i behörigheten**: Kontrollera rättigheterna för mappen `~/.LND`




Så du har kommit till slutet av denna handledning. Om du vill lära dig mer om Lightning erbjuder vi den här introduktionskursen för att ge dig en bättre förståelse för begreppen och metoderna bakom Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb