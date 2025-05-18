---
name: Lightning Network Daemon (Linux)
description: Installere og kjøre Lightning Network Daemon på Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network er en ny Layer av Bitcoin, noe som gjør at den kan anta lyndimensjoner, særlig takket være hastigheten og de lave kostnadene ved transaksjonene den tilbyr.



I denne veiledningen skal vi installere Lightning Network Daemon-implementeringen på Linux-maskinen vår (Ubuntu 24.04-distribusjonen).



## Hva er Lightning Network Daemon?



Lightning Network Daemon er en komplett Go-implementering av Lightning Network. Den ble laget av Lightning Labs og lar deg kjøre en full instans av en Lightning-node på maskinen din.


Med andre ord, med denne implementeringen kan du :





- Samhandle med Lightning Network**: Du kan bruke kommandolinjer til å opprette Lightning-porteføljer, administrere betalingskanaler og -ruter og mye mer, direkte fra maskinterminalen din.
- Koble til en ekstern Bitcoin-node eller din egen Bitcoin Core-forekomst**: Med LND kan du koble til en Bitcoin-forekomst og bruke den som backend. For å bruke denne implementasjonen trenger du ikke å kjøre en Bitcoin Core-forekomst på maskinen din.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Hvorfor ha din egen Lightning-node?


Lightning er et Bitcoin-overlegg som optimaliserer overføringsprosessen og reduserer transaksjonskostnadene.



Ved å rotere Lightning-noden får du suverenitet og selvstendighet. Du har kontroll over midlene dine, så husk på det:



"Ikke nøklene dine, ikke bitcoinsene dine."



På denne måten øker sikkerheten og integriteten til dataene dine ved å kjøre en Lightning-node på følgende måter





- Total kontroll**: Administrer dine egne betalingskanaler, bli din egen bank og vær herre over eiendelene dine.
- Konfidensialitet**: Transaksjoner uten å måtte stole på at tredjeparter beskytter personvernet ditt.
- Læring og selvstendighet**: Takket være `lncli`-kommandoer kan du bedre forstå Lightnings underliggende prosesser ved å bruke dem selv fra terminalen din.
- Desentralisering**: Ta en aktiv rolle i å styrke og desentralisere Bitcoin/Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Du har to alternativer for å kjøre en instans av LND-implementeringen på maskinen vår. Vi kan enten sette opp miljøet på vår egen maskin for å kjøre lokalt, eller installere LND fra en Docker-container. Her konsentrerer vi oss om det første alternativet, og ser hvordan vi går frem med Docker i en senere veiledning.


## Installer LND fra kildekoden



### Forutsetninger


Siden LND er skrevet i Go, må du sørge for at du har GoLang-miljøet og de nødvendige avhengighetene på Linux-maskinen din.





- Krav til maskinvare:**


For å få en smidig og sømløs opplevelse må maskinen din ha den nødvendige kapasiteten til å kjøre LND Lightning-noden.



Du trenger :


1. **8 GB RAM** for optimal flyt,


2. **En flerkjerneprosessor (firekjerners eller mer)** for å administrere nodens handlinger på en effektiv måte,


3. **Minst 5 GB diskplass** for beskjæring av nodemodus og 1 TB for å kjøre Bitcoin Core (valgfritt hvis du bruker en ekstern node)





- Installer nyttige avhengigheter:**


Kommandoen nedenfor lar deg installere verktøyene du trenger for å kjøre LND på maskinen din. Du må blant annet installere `Git`, et versjonsverktøy, og `make`, som kan kjøre og bygge LND-implementasjonen fra kildekoden.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Installer GoLang på Linux-maskinen din**



Per datoen for denne veiledningen krever LND versjon 1.23.6 av Go*** for installasjon.



Hvis du allerede hadde en tidligere versjon installert, må du fjerne den for den nye Go-installasjonen.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfigurasjon av Go**-miljøet


I filen `~/.bashrc` initialiserer du følgende miljøvariabler for å legge til Go i Linux-systemet ditt.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Kontroll av installasjonen** (på fransk)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Klone LND GitHub-depotet



Bruk git for å få en kopi av LND-kildekoden lokalt på maskinen din


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Bygg og installer



Verktøyet `make`, som tidligere er installert, vil gjøre det mulig å bygge en kjørbar fil fra LND-kildekoden og fortsette med installasjonen.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Installer LND på maskinen din



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Kontroll av installasjonen** (på fransk)



For å forsikre deg om at alt gikk som det skulle, kan du kjøre denne kommandoen for å få vite hvilken versjon av LND du kjører for øyeblikket.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Vedlikehold og oppgraderinger



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **VIKTIG**: LND-oppdateringer kan kreve nyere versjoner av Go, så sørg for å oppdatere systemet ditt for å unngå avhengighetsproblemer under installasjonen.


### Konfigurere Lightning Network Daemon



Konfigurasjonen av en Lightning LND-node er lik den for Bitcoin, og utføres i en konfigurasjonsfil som inneholder alle parametrene for noden. For å gjøre dette kan du opprette en skjult mappe `.LND` ved roten av maskinen, og deretter opprette konfigurasjonsfilen `LND.conf` i denne mappen.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





I konfigurasjonsfilen kan du konfigurere LND-noden.



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



## Forstå konfigurasjonen din



Det er viktig at du forstår minimumskonfigurasjonen du trenger for en korrekt og fullstendig installasjon av LND-noden.



Basert på innholdet i filen `~/.LND/LND.conf`, her er detaljene i feltene:





- noseedbackup**: Lar deg velge om du vil at LND skal utføre automatiske sikkerhetskopier av porteføljene dine.  Hvis du setter denne egenskapen til `0`, kan du lagre gjenopprettingsinformasjon manuelt på et personlig valgt sikkert sted.





- feilsøkingsnivå**: Her kan du definere detaljnivået for feil og logger i tilfelle det oppstår feil under en handling.





- Bitcoin.aktiv**: Instruerer LND til å fungere som en Bitcoin-node og samhandle med Bitcoin-nettverket.





- Bitcoin.Mainnet**: Angir at LND skal koble seg til Bitcoins hovednettverk (Mainnet), og du kan angi verdiene `bitcoind.signet` og `bitcoind.regtest` for henholdsvis Bitcoin Signet- og Bitcoin Regtest-nettverkene





- Bitcoin.node**: Angir hvilken type Bitcoin-node LND skal koble seg til.





- Bitcoin.rpcuser** og **Bitcoin.rpcpassword** : Representerer.


henholdsvis påloggingsinformasjon (bruker, passord) for å koble til Bitcoin-noden





- bitcoind.zmqpubrawblock** og **bitcoind.zmqpubrawtx**: definerer henholdsvis ZeroMQ-endepunkter for å motta varsler om nye blokker og transaksjoner på Bitcoin-nettverket.




## Kontrollere installasjonen med LND



Du vil sannsynligvis forsikre deg om at prosessen har vært vellykket, og at du synkroniserer med Lightning Network for å holde nodeinformasjonen oppdatert.



For å starte LND-implementeringen og få informasjon om noden din, skriver du ganske enkelt inn kommandoen :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Utføre handlinger på LND



Når installasjonen er fullført og kontrollert, kan du begynne å bruke den.


Her er de viktigste kommandoene for å komme i gang.



### Opprett en portefølje


Lynporteføljen din er det første steget i enhver form for kapitalforvaltning.



⚠️ **VIKTIG**: Skriv nøye ned den 24 ord lange **seed-frasen**. Du trenger den for å få tilbake pengene dine i tilfelle problemer.



Lagre også Wallet-passordet ditt, slik at du kan låse det opp med kommandoen `lncli unlock` når du starter LND-noden på nytt.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Sjekk saldoen din



Se kontoene dine direkte fra terminalen din:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informasjon om noden din



Bruk kommandoen nedenfor for å finne ut hvilke kanaler som er aktive på noden din.



```bash
lncli listchannels
```



Du kan også få en liste over nodene du er koblet til.



```bash
lncli listpeers
```



### Kanaladministrasjon



En Lightning-kanal gir deg mulighet til å ha en **direkte, parvis forbindelse med en annen node på Lightning Network**. I denne kanalen kan du fritt bruke Exchange Satoshis opp til kanalens kapasitet.



### Koble til en node



Å koble seg til andre Lightning-noder er en grunnleggende handling hvis du ønsker å delta aktivt og dra nytte av kraften i Lightning.



For å koble deg til en motpart (Lightning-node) trenger du tre opplysninger:




- Nodens offentlige nøkkel**: Dette er nodens unike identifikator i Bitcoin-nettverket;
- IP** : IP-en til maskinen som noden er installert på;
- PORT** :  Porten som er åpen på maskinen som tillater kommunikasjon med denne noden.



Du kan finne noder du kan koble deg til på [amboss] (https://amboss.space/), en plattform som viser informasjon om Lightning-noder.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Sørg for at du kobler deg til **pålitelige noder** for å bevare integriteten til ditt eget system. Her er noen anbefalinger for valg av riktige tilkoblinger.





- Geografisk diversifisering**: Koble deg til noder i ulike regioner.





- Omdømme**: Velg noder med god tilgjengelighet.





- Kapasitet**: Velg knuter med god likviditet.





- Gebyrer**: Gebyrer for ruting av sjekker.


### Åpne en betalingskanal


For å åpne en betalingskanal må du sørge for at du er **tilkoblet** til motpartsnoden, og deretter definere **kapasiteten** (mengden satoshier) du ønsker å blokkere i denne kanalen.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Opprett en Lightning Invoice



En Lightning Invoice representerer en streng med tegn som uttrykker ditt ønske om å motta satoshier i din Lightning Wallet.


Ved å opprette Lightning-fakturaer med din egen node kan du beskytte dataene dine (geografiske og personlige) og gir deg 100 % autonomi over forvaltningen av midlene dine.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Betaler en Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Steng en kanal



Det finnes to måter å lukke en aktiv kanal på den aktuelle noden på.





- Nedleggelse av samarbeid**: Dette signaliserer at noden din ønsker å trekke seg ut av betalingskanalen, og sikrer at pågående oppgaver fullføres og at data sikkerhetskopieres for å unngå tap av midler.


```
lncli closechannel <ID_CANAL>
```




- Tvungen stenging**: ⚠️ Bør unngås hvis mulig, da denne handlingen avbryter pågående prosesser i betalingskanalen din og øker risikoen for å miste penger.


```
lncli closechannel --force <ID_CANAL>
```


## Beste praksis og sikkerhet for LND-noden din.


Sikkerhet er avgjørende når du bruker en Bitcoin/ Lightning-node. Her er noen punkter for å styrke sikkerheten ved installasjonen:





- Oppbevar `seed-frasen` på et sikkert sted utenfor nettet.





- Ta regelmessig sikkerhetskopier av filen `~/.LND/channel.backup`: Denne filen lagrer kanalstatusene dine hver gang en ny kanal åpnes (eller en gammel kanal lukkes) på noden din.


⚠️ Gjør det mulig å gjenopprette kanaler og gjenopprette midler som er blokkert i betalingskanaler i tilfelle tap av data eller nodefeil



Du kan gjenopprette pengene dine med kommandoen nedenfor ved å angi sikkerhetskopibanen til denne filen:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Sørg for at du har lagret gjenopprettingsordene og passordet til Lightning Wallet.
- Hold systemet ditt oppdatert.



## Aktuell feilsøking


### Hyppige problemer




- bitcoind-tilkoblingsfeil** : Sjekk innloggingsdetaljene dine for RPC
- Synkronisering blokkert** : Sjekk Internett-tilkoblingen din
- Tillatelsesfeil**: Sjekk rettighetene til mappen `~/.LND`




Så du har kommet til slutten av denne veiledningen. Hvis du ønsker å lære mer om Lightning, tilbyr vi dette introduksjonskurset for å gi deg en bedre forståelse av konseptene og praksisene bak Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb