---
name: Lightning Network Daemon (Linux)
description: Lightning Network Daemon installeren en draaien op Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



De Lightning Network is een tweede Layer van Bitcoin, waardoor het bliksemafmetingen kan aannemen, vooral dankzij de snelheid en lage kosten van de transacties die het biedt.



In deze tutorial installeren we de Lightning Network Daemon implementatie op onze Linux machine (Ubuntu 24.04 distributie).



## Wat is Lightning Network Daemon?



Lightning Network Daemon is een volledige Go-implementatie van de Lightning Network. Het is gemaakt door Lightning Labs en laat je een volledige instantie van een Lightning node op je machine draaien.


Met andere woorden, met deze implementatie kun je :





- Interactie met de Lightning Network**: Je kunt commandoregels gebruiken om Lightning wallets aan te maken, betaalkanalen en routes te beheren, en nog veel meer, direct vanaf je machineterminal.
- Een extern Bitcoin knooppunt of je eigen Bitcoin core instantie koppelen**: Met LND kun je een Bitcoin instantie koppelen en als backend gebruiken. Om deze implementatie te gebruiken, hoef je geen Bitcoin core instantie op je machine te draaien.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Waarom een eigen Lightning-knooppunt?


Lightning is een Bitcoin overlay die het overdrachtsproces optimaliseert en de transactiekosten verlaagt.



Door je Lightning-node te roteren, krijg je soevereiniteit en autonomie. Je hebt controle over je fondsen, dus houd er rekening mee:



"Niet je sleutels, niet je bitcoins."



In die zin verhoogt het draaien van een Lightning-node de veiligheid en integriteit van je gegevens op de volgende manieren:





- Totale controle**: Beheer je eigen betaalkanalen, word je eigen bank en ben de baas over je bezittingen.
- Vertrouwelijkheid**: Transactie zonder vertrouwen op derden om je privacy te beschermen.
- Leren en autonomie**: Dankzij de `lncli` commando's kun je de onderliggende processen van Lightning beter begrijpen door jezelf toe te passen vanaf je terminal.
- Decentralisatie**: Speel een actieve rol in het versterken en decentraliseren van de Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Er zijn twee opties om een instantie van de LND implementatie op onze machine te draaien. We kunnen de omgeving opzetten op onze eigen machine om lokaal te draaien, of LND installeren vanuit een Docker container. We concentreren ons hier op de eerste optie en zullen in een latere tutorial bekijken hoe we Docker kunnen gebruiken.


## LND installeren vanaf broncode



### Vereisten


Aangezien LND geschreven is in Go, moet je ervoor zorgen dat je de GoLang omgeving en de nodige afhankelijkheden op je Linux machine hebt.





- Hardwarevereisten:**


Voor een soepele, naadloze ervaring moet je machine de benodigde capaciteit hebben om je LND Lightning node te draaien.



Je hebt nodig :


1. **8 GB RAM** voor optimale vloeiendheid,


2. **Een multi-core processor (quad-core of meer)** om de acties van je node efficiënt te beheren,


3. **Ten minste 5 GB schijfruimte** voor de pruned node-modus en 1 TB om Bitcoin core te draaien (optioneel als u een extern knooppunt gebruikt)





- Nuttige afhankelijkheden installeren:**


Met het onderstaande commando kun je op je machine de gereedschappen installeren die je nodig hebt om LND te draaien. Je moet onder andere `Git` installeren, een versiebeheerprogramma, en `make`, dat de LND implementatie kan uitvoeren en bouwen vanaf de broncode.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Installeer GoLang op uw Linux-machine**



Op de datum van deze tutorial vereist LND versie 1.23.6 van Go*** voor installatie.



Als je al een vorige versie had geïnstalleerd, verwijder deze dan voor de nieuwe Go-installatie.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go** omgeving configureren


In je `~/.bashrc` bestand, initialiseer de volgende omgevingsvariabelen om Go toe te voegen aan je Linux systeem.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- De installatie controleren** (in het Frans)


```bash
go version
```



![go-version](assets/fr/03.webp)


### De LND GitHub repository klonen



Gebruik git om een kopie van de LND broncode lokaal op je machine te krijgen


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Bouwen en installeren



Met de eerder geïnstalleerde `make` tool kun je een executable bouwen van de LND broncode en verder gaan met je installatie.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



LND installeren op uw machine



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Uw installatie controleren** (in het Frans)



Om er zeker van te zijn dat alles goed is gegaan, zou het uitvoeren van dit commando je de versie van LND moeten geven die je momenteel draait.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Onderhoud en upgrades



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **BELANGRIJK**: LND updates kunnen recentere versies van Go vereisen, dus zorg ervoor dat u uw systeem bijwerkt om afhankelijkheidsproblemen tijdens de installatie te voorkomen.


### Lightning Network Daemon configureren



De configuratie van een Lightning LND knooppunt is vergelijkbaar met die van Bitcoin, en wordt uitgevoerd in een configuratiebestand dat alle parameters van je knooppunt bevat. Om dit te doen, kun je in de root van je machine een verborgen map `.LND` aanmaken en vervolgens je configuratiebestand `LND.conf` in deze map maken.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





In het configuratiebestand kunt u uw LND knooppunt instellen.



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



## Uw configuratie begrijpen



Het is belangrijk dat u begrijpt welke configuratie u minimaal nodig heeft voor een correcte en volledige installatie van uw LND node.



Gebaseerd op de inhoud van het `~/.LND/LND.conf` bestand, zijn hier de details van de velden:





- noseedbackup**: Hiermee kun je kiezen of je wilt dat LND automatische back-ups van je portemonnees maakt.  Als je deze eigenschap op `0` zet, kun je handmatig herstelinformatie opslaan op een zelf gekozen veilige locatie.





- debuglevel**: Hiermee kun je het detailniveau van fouten en logs definiëren als er fouten optreden tijdens een actie.





- Bitcoin.active**: Instrueert LND om te functioneren als een Bitcoin knooppunt en te communiceren met het Bitcoin netwerk.





- Bitcoin.Mainnet**: Geeft LND op om verbinding te maken met Bitcoin's hoofdnetwerk (Mainnet), je kunt de waarden `bitcoind.signet` en `bitcoind.regtest` respectievelijk instellen voor de Bitcoin Signet en Bitcoin Regtest netwerken





- Bitcoin.node**: Specificeert het type Bitcoin knooppunt waarmee LND verbinding moet maken.





- Bitcoin.rpcuser** en **Bitcoin.rpcpassword** : Vertegenwoordigen.


respectievelijk de logins (gebruiker, wachtwoord) om verbinding te maken met uw Bitcoin knooppunt





- bitcoind.zmqpubrawblock** en **bitcoind.zmqpubrawtx**: definiëren respectievelijk ZeroMQ eindpunten om meldingen over nieuwe blokken en transacties op het Bitcoin netwerk te ontvangen.




## Uw installatie controleren met LND



Je zult er waarschijnlijk zeker van willen zijn dat het proces geslaagd is en dat je synchroniseert met de Lightning Network om je knooppuntinformatie up-to-date te houden.



Om de LND implementatie te starten en informatie over je knooppunt te verkrijgen, typ je simpelweg het commando :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Acties uitvoeren op LND



Zodra de installatie is voltooid en gecontroleerd, kun je deze gaan gebruiken.


Hier zijn de essentiële commando's om je op weg te helpen.



### Een Wallet maken


Uw Lightning Wallet is de eerste stap in elke actie om uw fondsen te beheren.



⚠️ **BELANGRIJK**: Noteer zorgvuldig uw 24-woord **seed zin**. U hebt deze nodig om uw geld terug te krijgen in geval van problemen.



Bewaar ook je Wallet wachtwoord, zodat je het kunt ontgrendelen met het `lncli unlock` commando wanneer je het LND knooppunt herstart.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Controleer je saldo



Raadpleeg je rekeningen rechtstreeks vanaf je terminal:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informatie over je knooppunt



Gebruik het onderstaande commando om erachter te komen welke kanalen actief zijn op jouw knooppunt.



```bash
lncli listchannels
```



Je kunt ook een lijst opvragen van de knooppunten waarmee je verbonden bent.



```bash
lncli listpeers
```



### Kanaalbeheer



Met een Lightning-kanaal heb je een **directe, paar-per-paar verbinding met een andere node op de Lightning Network**. In dit kanaal kun je vrij Exchange Satoshi's gebruiken tot de capaciteit van het kanaal.



### Verbinding maken met een knooppunt



Verbinding maken met andere Lightning-knooppunten is een fundamentele actie als je actief wilt deelnemen en wilt profiteren van de kracht van Lightning.



Om verbinding te maken met een peer (Lightning-knooppunt), heb je drie stukjes informatie nodig:




- De publieke sleutel van het knooppunt**: Dit is de unieke identificatiecode van het knooppunt in het Bitcoin netwerk;
- IP** : Het IP van de machine waarop het knooppunt is geïnstalleerd;
- PORT** :  De open poort op de machine die communicatie met dit knooppunt mogelijk maakt.



Je kunt knooppunten vinden om mee te verbinden op [amboss](https://amboss.space/), een platform dat informatie over Lightning knooppunten weergeeft.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Zorg ervoor dat je verbinding maakt met **betrouwbare knooppunten** om de integriteit van je eigen systeem te behouden. Hier zijn enkele aanbevelingen voor het kiezen van de juiste verbindingen.





- Geografische diversificatie**: Maak verbinding met knooppunten in verschillende regio's.





- Reputatie**: Kies knooppunten met een goede beschikbaarheid.





- Capaciteit**: Kies knopen met een goede liquiditeit.





- Kosten**: Kosten voor het doorsturen van cheques.


### Een betalingskanaal openen


Om een betaalkanaal te openen, zorg je ervoor dat je **verbonden** bent met het peer-knooppunt en definieer je de **capaciteit** (de hoeveelheid satoshi's) die je wilt blokkeren in dit kanaal.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Maak een Lightning Invoice



Een Lightning Invoice vertegenwoordigt een tekenreeks die je wens uitdrukt om satoshis te ontvangen in je Lightning Wallet.


Als je Lightning-facturen maakt met je eigen node, kun je je gegevens (geografisch en persoonlijk) beschermen en heb je 100% autonomie over het beheer van je fondsen.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Een bliksemschicht betalen Invoice



```bash
lncli payinvoice <FACTURE>
```


### Een kanaal sluiten



Er zijn twee manieren om een actief kanaal op je huidige knooppunt te sluiten.





- Coöperatieve afsluiting**: Hiermee geef je aan dat je knooppunt zich wil terugtrekken uit het betalingskanaal, waarbij je ervoor zorgt dat lopende taken worden voltooid en dat er een back-up van gegevens wordt gemaakt om verlies van fondsen te voorkomen.


```
lncli closechannel <ID_CANAL>
```




- Gedwongen sluiting**: ⚠️ Te vermijden indien mogelijk, deze actie onderbreekt lopende processen in je betalingskanaal en verhoogt het risico op het verliezen van fondsen.


```
lncli closechannel --force <ID_CANAL>
```


## Beste praktijken en veiligheid voor uw LND knooppunt.


Veiligheid is van het grootste belang bij het gebruik van een Bitcoin/ Lightning node. Hier volgen enkele punten om de veiligheid van uw installatie te verbeteren:





- Bewaar uw `seed zin` op een veilige, offline locatie.





- Maak regelmatig backups van het `~/.LND/kanaal.backup` bestand: Dit bestand slaat je kanaaltoestanden op iedere keer dat er een nieuwe kanaal wordt geopend (of een oude kanaal wordt gesloten) op je knooppunt.


⚠️ Stelt je in staat kanalen te herstellen en in betalingskanalen geblokkeerde fondsen terug te krijgen in geval van gegevensverlies of een knooppuntstoring



U kunt uw fondsen herstellen met de onderstaande opdracht door het back-uppad van dit bestand op te geven:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Zorg ervoor dat je de herstelwoorden en het wachtwoord van je Lightning Wallet hebt opgeslagen.
- Houd je systeem up-to-date.



## Huidige probleemoplossing


### Veelvoorkomende problemen




- bitcoind verbindingsfout** : Controleer uw RPC inloggegevens
- Synchronisatie geblokkeerd** : Controleer uw internetverbinding
- Toestemmingsfout**: Controleer de rechten van de map `~/.LND`




Je bent aan het einde gekomen van deze tutorial. Als je meer wilt leren over Lightning, bieden we deze inleidende cursus aan om je een beter inzicht te geven in de concepten en werkwijzen achter de Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb