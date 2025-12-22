---
name: Dojo
description: En Bitcoin-node med åpen kildekode for personvern og autonomi
---

![cover](assets/cover.webp)



*Denne veiledningen er basert på [den offisielle Ashigaru-dokumentasjonen](https://ashigaru.rs/docs/), som jeg har overtatt og utvidet. Jeg har omskrevet alle avsnitt for å gjøre dem mer oversiktlige, lagt til mer detaljerte forklaringer og illustrasjoner for nybegynnere, slik at installasjonen og bruken blir enklere å forstå



---

Dojo er et åpen kildekode-program designet for å fungere som en backend-server for visse personvernorienterte Bitcoin-lommebøker, basert på en Bitcoin core-node. Historisk sett ble det utviklet for å fungere med Samourai Wallet, en mobil Wallet som tilbød avanserte personvernfunksjoner som Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet er nå lagt ned etter at utviklerne ble arrestert, men etterfølgeren, **Ashigaru Wallet**, har tatt over og fortsetter å stole på Dojo for å tilby en komplett opplevelse for brukere som ønsker å ha kontroll over dataene sine når de bruker Bitcoin.



![Image](assets/fr/01.webp)



I praksis fungerer Dojo som en gateway mellom Wallet og Bitcoin-nettverket. Uten Dojo ville en lett mobil Wallet måtte spørre tredjepartsservere for å få status på UTXO-ene og historikken din, eller for å kringkaste transaksjonene dine. Dette innebærer avhengighet og lekkasje av sensitive data til en tredjepartsserver (brukte adresser, beløp, betalingsfrekvens osv.). Med Dojo hoster du denne serveren selv, direkte koblet til din egen Bitcoin-node. På denne måten går alle dine porteføljeforespørsler gjennom en infrastruktur som du kontrollerer, uten mellomledd, noe som styrker din konfidensialitet og suverenitet.



## Krav for å sette opp en dojo



Å sette opp en Dojo-server krever ikke en ultrakraftig maskin. Alle som har en enkel datamaskin, en stabil Internett-tilkobling og muligheten til å la den stå på kontinuerlig (24/7), kan sette opp en fungerende Dojo.



### Velg maskintype



Du kan bruke :




- en bærbar datamaskin ;
- en stasjonær datamaskin ;
- en mini-PC (f.eks. Intel NUC, Lenovo Thincentre Tiny ...).



Hvert alternativ har sine fordeler og ulemper:




- Pris: En renovert mini-PC eller stasjonær PC vil ofte være billigere enn en ny bærbar PC.
- Fotavtrykk: En Mini-PC tar mindre plass.
- Strøm Supply: En bærbar PC har fordelen av å ha et batteri, noe som betyr at den ikke vil slå seg av i tilfelle strømbrudd, i motsetning til en mini-PC.
- Oppgraderingsmuligheter: Med barbones kan du som regel legge til minne eller enkelt bytte ut en Hard-disk.



Hvis du vil ha mer informasjon om valg av utstyr, anbefaler jeg at du tar dette kurset:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Anbefalt utstyr



Det er ikke nødvendig å kjøpe en ny maskin. En renovert datamaskin med spesifikasjonene nedenfor vil gi mye bedre ytelse enn enkeltkort-elektronikk (som Raspberry Pi).



**Minimumsspesifikasjoner:**




- X86-64-arkitektur (64-biters prosessor).
- 2 GHz dobbeltkjerneprosessor eller raskere.
- minimum 8 GB RAM.
- 2 TB eller mer NVMe SSD (for å lagre Blockchain eller Bitcoin og de nødvendige indeksene).



**Anbefalt operativsystem: **




- En Debian-basert distribusjon, for eksempel Ubuntu 24.04 LTS.



**Anbefalt utstyr:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- osv.



Det er fullt mulig å kjøre en Dojo-server på andre maskinvarekonfigurasjoner. For å få best mulig ytelse og begrense problemer anbefaler vi imidlertid at du følger anbefalingene ovenfor.



I denne veiledningen bruker jeg en gammel ThinkCentre Tiny med en Intel Pentium Dual-Core G4400T-prosessor, 8 GB RAM og en 2 TB SSD.



## 1 - Installere Ubuntu



*Hvis du ønsker å installere Dojo på en enhet som allerede er konfigurert, kan du hoppe over dette trinnet og gå direkte til trinn 2.*



Når du har klargjort den valgte maskinvaren, er det på tide å installere et operativsystem. Du kan bruke nesten hvilken som helst Debian-distribusjon, men jeg anbefaler at du velger en LTS-versjon av Ubuntu, da den passer perfekt til våre formål. Her er trinnene du skal følge:



### 1.1. Opprett en oppstartbar USB-nøkkel



Fra en datamaskin som allerede fungerer (din vanlige maskin), laster du ned Ubuntu LTS ISO-image [fra det offisielle nettstedet](https://ubuntu.com/download/desktop) (`24.04` i skrivende stund, men ta den nyeste hvis en annen er tilgjengelig).



![Image](assets/fr/02.webp)



Sett inn en USB-nøkkel på minst 8 GB i denne datamaskinen, og opprett deretter en oppstartbar nøkkel ved hjelp av programvare som [Balena Etcher](https://etcher.balena.io/). Velg Ubuntu ISO-bildet du nettopp har lastet ned, velg USB-nøkkelen som målenhet, og start deretter opprettelsesprosessen (vær tålmodig, det kan ta flere minutter).



![Image](assets/fr/03.webp)



Sett den oppstartbare USB-nøkkelen inn i den avslåtte datamaskinen (den du vil kjøre Dojo på). Start maskinen, og trykk umiddelbart på **F12** eller **F10** på tastaturet (avhengig av modell) for å få tilgang til oppstartsmenyen. Velg deretter USB-nøkkelen som den prioriterte enheten i datamaskinens oppstartsrekkefølge.



![Image](assets/fr/04.webp)



### 1.2. Installer operativsystemet



Startskjermen til Ubuntu vises. Velg "Prøv eller installer Ubuntu*".



![Image](assets/fr/05.webp)



Følg deretter den klassiske Ubuntu-installasjonsprosessen:




- Velg språk.
- Velg tastaturtype.
- Hvis du er tilkoblet via RJ45-kabel, er det ikke nødvendig å konfigurere Wi-Fi.
- Klikk på "*Install Ubuntu*" og kryss av for alternativet for å installere tredjepartsprogramvare (Wi-Fi-drivere, multimediekodeker osv.).
- Når veiviseren spør etter type installasjon, velger du "*Slett disk og installer Ubuntu*". **Advarsel**: Denne operasjonen vil slette innholdet på disken fullstendig. Kontroller nøye at disken du har valgt, tilsvarer NVMe SSD-enheten som er beregnet for Dojo.
- Opprett et enkelt brukernavn (f.eks. "*loic*").
- Gi maskinen et navn (f.eks. "*dojo-node*").
- Angi et sterkt passord og oppbevar det trygt.
- Aktiver alternativet "*Begj om passord for å logge inn*" for å styrke sikkerheten.
- Angi tidssonen din, og klikk deretter på "*Install*".
- Vent til installasjonen er fullført. Når installasjonen er fullført, starter systemet automatisk på nytt.
- Fjern USB-installasjonsnøkkelen når du starter datamaskinen på nytt.



For mer informasjon om Ubuntu-installasjonsprosessen, se vår egen veiledning :



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. Systemoppdatering



Etter første oppstart åpner du en terminal ved hjelp av tastekombinasjonen ***Ctrl + Alt + T*** og kjører følgende kommandoer for å oppdatere systemet:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Installasjon av uthus



For at Dojo skal fungere skikkelig, må visse programvarebrikker være til stede på systemet ditt. Disse brukes til å administrere programvarelagre, kommunikasjon, dekomprimering av arkiver og kjøring av Dojo i Docker-containere. Alle disse operasjonene utføres i terminalen.



### 2.1. Forberedelse



Følgende kommando sender deg tilbake til din personlige mappe. Dette er en god fremgangsmåte før du kjører en rekke installasjoner.



```bash
cd ~/
```



Før du installerer programvare, må du forsikre deg om at databasen med programvare som er tilgjengelig på maskinen din, er oppdatert. Slik unngår du å installere foreldede versjoner.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. Installer verktøy



Flere verktøy må legges til i systemet:




- `apt-transport-https`: gjør det mulig å laste ned pakker på en sikker måte via HTTPS
- `ca-certificates`: håndterer sertifikatene som kreves for krypterte tilkoblinger
- `curl`: for å hente filer fra Internett
- `gnupg-agent`: for GPG-nøkkelhåndtering
- software-properties-common`: inneholder verktøy for manipulering av APT-repositorier
- `unzip`: pakker ut filer i ZIP-format



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Under installasjonen kan det hende at systemet ber deg om bekreftelse. Trykk på tasten "*y*", og trykk deretter på "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. Installer Torsocks



Torsocks gjør det mulig å utføre visse kommandoer via Tor-nettverket, noe som forbedrer konfidensialiteten i kommunikasjonen.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Installer Docker og Docker Compose



Dojo kjører i Docker-containere. Dette betyr at hver tjeneste er isolert i et uavhengig miljø, noe som forenkler vedlikehold og sikkerhet. For å gjøre dette må du installere Docker og Docker Compose-verktøyet, som gjør at du kan administrere flere containere samtidig.



#### Legg til Docker-signeringsnøkkel



Docker tilbyr sin egen digitale signaturnøkkel. Ved å legge den til, verifiseres ektheten til nedlastede pakker.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Offisielt Docker-depot lagt til



Deretter må du fortelle systemet hvor de offisielle Docker-pakkene finnes. Denne kommandoen legger til et nytt depot i konfigurasjonen av pakkebehandleren.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Installere Docker og Docker Compose



De viktigste Docker-komponentene kan nå installeres.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Brukerautorisasjon



Som standard er det bare kommandoer som utføres med administratorrettigheter som kan starte Docker. For å gjøre det enklere anbefaler jeg at du legger til din nåværende bruker i gruppen "*docker*". Da kan du bruke Docker uten å måtte skrive `sudo` hver gang.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Opprettelse av enkeltbrukere (valgfritt)



Hvis du ønsker å forbedre sikkerheten i systemet ditt, anbefaler jeg at du oppretter en egen bruker som kun kjører Dojo. Denne separasjonen begrenser risikoen: Hvis det oppstår et sikkerhetsproblem i Dojo, vil det ikke gå direkte ut over hovedkontoen din.



### 3.1. Opprettelse av brukerkonto



Følgende kommando oppretter en ny bruker med navnet "*dojo*". Denne brukeren vil ha en hjemmekatalog `/home/dojo` og tilgang til bash-terminalen. Den vil også bli lagt til i sudo-gruppen for å gjøre det mulig å utføre administratorkommandoer.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Angi et passord



Det er viktig å tildele et sterkt passord til denne kontoen. Ideelt sett bør du bruke en passordbehandler som Bitwarden for å generate en lang, Hard vanskelig å gjette kombinasjon.



```bash
sudo passwd dojo
```



Systemet ber deg deretter om å skrive inn passordet du har valgt, og deretter bekrefte det en gang til.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autoriser brukeren til å bruke Docker



For at brukeren "*dojo*" skal kunne starte containerne som trengs for å kjøre Dojo, må han legges til i Docker-gruppen. På denne måten unngår du å måtte innlede hver kommando med `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Omstart av systemet



For at gruppeendringene skal tre i kraft, må maskinen startes på nytt.



```bash
sudo reboot
```



### 3.5. Logg inn med ny bruker



Når systemet starter på nytt, logger du inn med ***dojo***-påloggingen og passordet du definerte tidligere. Alle påfølgende trinn må utføres fra denne dedikerte kontoen.



## 4. Last ned og sjekk Dojo



Før du installerer Dojo, er det viktig å forsikre deg om at filene kommer fra den offisielle utvikleren og at de ikke har blitt endret. Dette trinnet baserer seg på bruk av PGP og hasher for å verifisere filenes autentisitet og integritet.



### 4.1. Importer utviklerens PGP-nøkkel



Last ned utviklerens offentlige nøkkel via Tor, og importer den til din lokale nøkkelring. Denne nøkkelen vil bli brukt til å verifisere signaturene som er knyttet til Dojo-filer.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. Last ned den nyeste versjonen av Dojo



Hent det komprimerte arkivet som inneholder Dojo-kildekoden. I dette eksemplet er den nyeste versjonen `1.27.0`: modifiser kommandoen i henhold til [den nyeste versjonen her på det offisielle GitHub-arkivet](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Last ned fingeravtrykk og signatur



Utviklerne publiserer en fil som viser de digitale fingeravtrykkene til arkivene, samt en fil som er signert med PGP-nøkkelen deres. Last ned dem for å sammenligne filene dine lokalt.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Kontroller PGP-signaturen



Kontroller at fingeravtrykksfilen er signert med den importerte nøkkelen.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Et korrekt resultat viser en gyldig signatur med nøkkelen `E53AD419B242822F19E23C6D3033D463D6E544F6` og den tilhørende Address `dojocoder@pm.me`. Det kan vises en advarsel om at nøkkelen ikke er sertifisert: Du kan ignorere den.



Hvis signaturen derimot er ugyldig, må du umiddelbart stoppe installasjonsprosessen og starte på nytt fra begynnelsen.



![Image](assets/fr/17.webp)



### 4.5. Kontroller arkivets integritet



Beregn SHA256-fingeravtrykket til den nedlastede filen, og åpne deretter fingeravtrykksfilen for å sammenligne de to verdiene.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Hvis de to fingeravtrykkene er identiske, kan du være sikker på at arkivet ikke har blitt endret. Hvis de er forskjellige, må du ikke gå lenger og slette filene.



![Image](assets/fr/18.webp)



### 4.6. Pakk ut og organiser filer



Når verifiseringen er fullført, kan du pakke ut arkivet og opprette en mappe som er dedikert til Dojo-installasjonen.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Rydd opp i unødvendige filer



Slett midlertidige filer og arkiver som ikke lenger er nødvendige for å holde miljøet rent.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Dojo-konfigurasjon



Dojo er en backend-server som samler flere tjenester for å samhandle med porteføljen din og administrere Bitcoin-noden din. Konfigurasjonen kan være kompleks, men prosjektet tilbyr en forenklet metode som automatisk installerer og konfigurerer følgende komponenter:




- Dojo (hoved-API)
- Bitcoin core (komplett Bitcoin-node)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indexer (rask indeksering av blokker og transaksjoner)
- Fulcrum Electrum Server tilgjengelig på Tor-nettverket
- Fulcrum Electrum Server tilgjengelig på det lokale nettverket
- Legitimasjon for administrasjon



### 5.1. Administrasjonslegitimasjon



For å sikre tilgangen til de ulike tjenestene må du generate flere unike identifikatorer:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSORD`
- `MYSQL_ROOT_PASSORD`
- mYSQL_USER
- `MYSQL_PASSORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Disse identifikatorene **må være unike** (dette er svært viktig: du må ikke bruke det samme passordet for flere tjenester), bestå utelukkende av tall, store bokstaver og små bokstaver (alfanumeriske) og være på rundt 40 tegn for å garantere et høyt sikkerhetsnivå. Nok en gang anbefaler jeg på det sterkeste å bruke en passordadministrator.



### 5.2. Få tilgang til konfigurasjonsfiler



Dojo-konfigurasjonsfilene ligger i mappen `conf/`. Flytt til denne katalogen:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core-konfigurasjon



Åpne Bitcoin core-konfigurasjonsfilen med tekstredigeringsprogrammet nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



I denne filen legger du inn de genererte identifikatorene:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Erstatt `din-ID-her` og `ditt-passord-her` med dine egne innlogginger (med et sterkt passord).***



Du kan også justere størrelsen på hurtigminnet som Bitcoin core bruker for å forbedre ytelsen (du kan til og med bruke mer hvis du har mye RAM tilgjengelig):



```
BITCOIND_DB_CACHE=2048
```



Slik lagrer du endringene og lukker redigeringsprogrammet :




- trykk `Ctrl + X
- type `y`
- trykk deretter på "*Enter*"



### 5.4. MySQL-konfigurasjon



Åpne deretter MySQL-databasekonfigurasjonen:



```bash
nano docker-mysql.conf.tpl
```



Vennligst skriv inn innloggingsopplysningene dine:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Erstatt `din-ID-her` og `ditt-passord-her` med dine egne innlogginger (med sterke, unike passord).***



Lagre på samme måte (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Konfigurasjon av Fulcrum-indekser



Åpne følgende fil:



```bash
nano docker-indexer.conf.tpl
```



Legg til parametrene for å aktivere Fulcrum og integrere det riktig i Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Deretter er det to muligheter, avhengig av konfigurasjonen din. Hvis Dojo er installert på en maskin som er atskilt fra din vanlige datamaskin (på en dedikert maskin, en server ...), skriver du inn dens IP Address i ditt lokale nettverk, for eksempel :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



For å finne ut den lokale IP Address på maskinen din, åpner du en annen terminal og skriver inn følgende kommando:



```bash
hostname -I
```



Den andre muligheten: Hvis Dojo kjøres direkte på din vanlige datamaskin, beholder du standardverdien som allerede finnes i konfigurasjonsfilen :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Lagre og avslutt redigeringsprogrammet (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Konfigurasjon av knutepunkttjenester



Til slutt åpner du konfigurasjonen av Dojo-hovedtjenesten:



```bash
nano docker-node.conf.tpl
```



Vennligst skriv inn innloggingsopplysningene dine:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Erstatt `ditt-passord-her` med din egen legitimasjon (med sterke, unike passord).***



![Image](assets/fr/26.webp)



Aktiver deretter den lokale indekseren:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Lagre og avslutt redigeringsprogrammet (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Innloggingsadministrasjon



Når konfigurasjonen er fullført, er det ikke nødvendig å lagre alle identifikatorene som genereres. Den eneste som absolutt må lagres, er :



```
NODE_ADMIN_KEY
```



Denne påloggingen gjør det mulig for deg å logge inn i Dojo-vedlikeholdsverktøyet senere. Alle andre pålogginger kan fjernes fra passordbehandleren eller håndskrevne notater. De forblir tilgjengelige fra Dojo-konfigurasjonsfilene hvis du skulle få behov for å hente dem frem i fremtiden.



## 6. Dojo-installasjon



På dette stadiet vil Dojo bli installert og startet på maskinen din. Operasjonen vil starte flere tjenester (Bitcoin core, Fulcrum-indeksereren, Dojo-backend osv.) og starte full synkronisering av Blockchain Bitcoin. Dette kan ta flere dager, avhengig av maskinvaren og Internett-tilkoblingen din.



### 6.1. Sjekk at Docker fungerer som den skal



Før du starter installasjonen, må du sørge for at Docker er i drift. Kjør følgende kommando:



```bash
docker run hello-world
```



Denne kommandoen laster ned og starter en liten testcontainer. Hvis alt fungerer som det skal, bør du se en melding som ligner på :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Hvis denne meldingen ikke vises, starter du med å starte maskinen på nytt med :



```bash
sudo reboot
```



Logg deretter inn på **dojo**-kontoen din igjen og kjør testkommandoen på nytt. Hvis feilen vedvarer, har ikke Docker blitt installert riktig. I så fall må du gå tilbake til trinn 2.4 om installering av Docker og sjekke hver kommando nøye.



### 6.2. Gå til Dojo-installasjonskatalogen



Skriptene som kreves for installasjonen, ligger i mappen `my-dojo`. Flytt til denne katalogen:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Bruk kommandoen `ls` for å kontrollere at filen `dojo.sh` finnes. Dette er hovedskriptet som automatiserer installasjonen av Dojo og oppstarten av alle tjenestene.



![Image](assets/fr/29.webp)



### 6.3. Start installasjonen



Start installasjonen ved å kjøre :



```bash
./dojo.sh install
```



Bekreft installasjonen ved å trykke på `y` og deretter "*Enter*".



![Image](assets/fr/30.webp)



Dette skriptet vil :




- laste ned og starte de nødvendige Docker-containerne,
- initialiserer Bitcoin core og starter synkroniseringen av Blockchain,
- starte Fulcrum-indekseren for å spore transaksjoner og adresser,
- aktivere Dojo-backenden og dens API-er.



Du vil se en jevn strøm av logger som ruller forbi, med fargerike referanser som `bitcoind`, `soroban`, `nodejs` eller `fulcrum`. Denne rullingen indikerer at Dojo er oppe og kjører og begynner å utføre de ulike tjenestene.



![Image](assets/fr/31.webp)



### 6.4. Avslutt loggvisning



Logger vises i sanntid i terminalen. Hvis du vil gå tilbake til ledeteksten mens Dojo kjører i bakgrunnen, skriver du :



```
Ctrl + C
```



Ikke bekymre deg: Å stoppe loggvisningen stopper ikke tjenestene. Docker fortsetter å kjøre Dojo i bakgrunnen (du trenger selvsagt ikke å stoppe datamaskinen hvis du vil at IBD skal fortsette).



### 6.5. Forståelse av *Initial Block Download* (IBD)



Ved oppstart må Bitcoin core laste ned og verifisere hele Blockchain siden 2009. Dette trinnet kalles ***Initial Block Download* (IBD)**. Det er viktig, ettersom det gjør det mulig for Dojo-noden å verifisere hver Bitcoin-blokk og -transaksjon uavhengig av hverandre.



Varigheten av denne synkroniseringen avhenger av flere faktorer:




- prosessorkraften og mengden RAM-minne som er tilgjengelig,
- hastigheten på disken din,
- antall og kvalitet på peers noden din kobler seg til,
- hastigheten på Internett-tilkoblingen din.



I praksis tar denne operasjonen vanligvis mellom **2 og 7 dager**. I løpet av denne perioden kan du la maskinen være i kontinuerlig drift. Jo lenger maskinen er på, desto raskere vil synkroniseringen bli fullført. Jeg anbefaler at du sjekker synkroniseringsstatusen regelmessig ved å se i Bitcoin core-loggene, eller ved å bruke Dojo-vedlikeholdsverktøyet når det er installert (se neste avsnitt).



For å få mer kunnskap om IBD og, mer generelt, om hvordan Bitcoin-noden fungerer og hvilken rolle den spiller, anbefaler jeg at du tar en titt på dette kurset:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Overvåking av synkronisering



Når du installerer Dojo for første gang, må du vente på at to hovedoperasjoner er fullført: fullstendig nedlasting av Blockchain Bitcoin (*IBD*) og indeksering av denne Blockchain av Fulcrum. Avhengig av tilkoblingen din og maskinens strøm, kan dette ta flere dager. I løpet av denne tiden kan du overvåke fremdriften i prosessen for å forsikre deg om at alt går som det skal.



Det finnes to måter å overvåke synkroniseringsstatusen på:




- bruk av Dojo Maintenance Tool (eller DMT), som er enkelt, men gir få detaljer under IBD;
- direkte konsultasjon av Dojo-logger på maskinen din, mer teknisk, men mye mer presist.



### 7.1. Sjekk via Dojo Maintenance Tool (DMT)



Dojo Maintenance Tool er et sikkert, nettbasert Interface som lar deg overvåke anleggets status og utføre visse operasjoner. Det er den enkleste og mest tilgjengelige måten å overvåke IBD-anleggets fremdrift på. I den innledende synkroniseringsfasen kan informasjonen som vises, være begrenset. DMT viser for eksempel ikke den detaljerte fremdriften i Fulcrum-indekseringen. Når synkroniseringen er fullført, vil DMT derimot vise :




- alle lys på Green;
- den siste validerte blokken for hver tjeneste (Node, Indexer, Dojo DB).



For å få tilgang til den, må du vite URL-en til DMT-en din og koble deg til den [via Tor-nettleseren](https://www.torproject.org/download/). For å gjøre dette åpner du en terminal og går til katalogen `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Kjør deretter følgende kommando:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Du får da tilgang til all informasjon om tilkoblinger til Dojo via Tor. Den vi er interessert i her, er følgende URL:



```
Dojo API and Maintenance Tool =
```



For å få tilgang til DMT fra en hvilken som helst maskin på et hvilket som helst nettverk (også eksternt), åpner du Tor Browser og skriver inn denne URL-en etterfulgt av `/admin`. Hvis URL-en din for eksempel er `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, må du skrive inn i [Tor Browser](https://www.torproject.org/download/) -feltet:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Vær vennlig å behandle denne Address strengt konfidensielt



Du blir deretter omdirigert til en autentiseringsside. DMT er logget inn med passordet `NODE_ADMIN_KEY` som du genererte tidligere.



![Image](assets/fr/33.webp)



Når du er logget inn, kan du få tilgang til *Dojo Maintenance Tool*! Under IBD kan du se "*Latest Block*"-informasjonen i "*Full node*"-menyen, som gir deg informasjon om den nåværende statusen til Bitcoin-noden.



![Image](assets/fr/34.webp)



Husk å bokmerke denne Address i Tor Browser for enkel gjenfinning senere.



Når Dojo er fullstendig synkronisert, bør du se Green-sjekken ✅ på alle indikatorene på DMT-startsiden.



### 7.2. Verifisering via Dojo-logger



Den andre måten å spore utviklingen av IBD på, er å se direkte i maskinloggene. Denne tilnærmingen gir mye mer presis overvåking i sanntid. Du kan se hvordan Bitcoin core går frem i nedlastingen av blokker, og hvordan Fulcrum indekserer dem.



Koble til maskinen som er vert for Dojo, og åpne en terminal. Alle kommandoer skal utføres fra katalogen `my-dojo`. Plasser deg i denne mappen:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core-logger



Se Bitcoin core-logger for å spore IBD-fremdriften:



```bash
./dojo.sh logs bitcoind
```



I begynnelsen vil du se en førsynkroniseringsfase av blokkoverskriftene:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Når dette tallet når 100 %, vil Bitcoin core starte den fullstendige nedlastingen av Blockchain. Du vil se IBD-fremdriften. For å finne ut den nåværende blokkhøyden, se på verdien som er angitt med `height=`. Du kan også følge tasten `progress=`, som angir prosentandelen av IBD-fremdriften.



![Image](assets/fr/36.webp)



For å lukke loggene og gå tilbake til ledeteksten bruker du som alltid kombinasjonen `Ctrl + C`.



#### Fulcrum-logger



Når Bitcoin core har fullført forsynkroniseringen av overskriften, begynner Fulcrum å indeksere Blockchain etter hvert som den kjører. Se loggene med :



```bash
./dojo.sh logs fulcrum
```



Du vil da se høyden på den sist indekserte blokken, angitt etter `height:`, samt indekseringsprosenten.



![Image](assets/fr/37.webp)



### 7.3. Korrupsjon i Fulcrum-databasen



Fulcrum er en særdeles kraftig indekserer, men installasjonen kan være komplisert, ikke minst på grunn av den delikate databasehåndteringen. Ved strømbrudd eller plutselig nedstengning av maskinen under den første synkroniseringen kan indeksererens database bli ødelagt. Dette kan du for eksempel se hvis du har følgende logger:



```bash
fulcrum | The database has been corrupted etc...
```



**Denne typen feil bør være rettet i den kommende utgivelsen av Fulcrum 2.0.



Hvis dette skjer med deg, har det ingen innvirkning på bitcoind (din Bitcoin-node): dens IBD vil fortsette å utvikle seg uavhengig av Fulcrum. Du vil imidlertid ikke kunne bruke Fulcrum før du har slettet de ødelagte dataene og startet synkroniseringen på nytt fra begynnelsen. Slik fungerer det:



Stopp Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Slett bare Fulcrum-beholderen og -volumet:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalt er navnet `my-dojo_data-fulcrum`, men hvis dette ikke er tilfelle for deg, kan du tilpasse navnet som ble returnert av forrige kommando.



Deretter relanserer du Dojo og gjenoppbygger Fulcrum fra bunnen av:



```bash
./dojo.sh upgrade
```



Deretter kan du sjekke at Fulcrum fungerer som det skal ved å se i loggene:



```bash
docker logs -f fulcrum
```




## 8. Bruke Dojo-vedlikeholdsverktøyet



Når Bitcoin-knuten er synkronisert til varphodet med den mest Proof of Work, og Blockchain er 100 % indeksert av Fulcrum, kan du begynne å bruke Dojo.



Dojo tilbyr et bredt spekter av funksjoner, som regelmessig forbedres med hver nye versjon. Etter min mening er de to viktigste :




- muligheten til å koble til Ashigaru Wallet for å bruke din egen node til å konsultere Blockchain-data og kringkaste transaksjonene dine,
- og Block explorer, som gir deg tilgang til informasjon om Blockchain Bitcoin uten å eksponere dataene dine for en ekstern instans du ikke kontrollerer.



La oss finne ut hvordan du bruker dem.


### 8.1. Koble Ashigaru til dojoen din



Det er veldig enkelt å koble Ashigaru Wallet til Dojo: Når du er på DMT-en, åpner du "*Pairing*"-menyen. En QR-kode vises, som du kan skanne direkte med Ashigaru-applikasjonen.



![Image](assets/fr/38.webp)



Første gang du starter Ashigaru-applikasjonen etter at du har opprettet eller gjenopprettet Wallet, blir du omdirigert til siden "*Konfigurer Dojo-serveren*". Trykk på "*Scan QR*", og skann deretter QR-koden som vises på DMT-en din.



![Image](assets/fr/39.webp)



Klikk deretter på knappen "*Fortsett*".



![Image](assets/fr/40.webp)



Du er nå koblet til dojoen din.



![Image](assets/fr/41.webp)



### 8.2. Bruk av Block explorer



Dojo installerer automatisk en Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), som trekker direkte på data fra din egen Bitcoin-node. En utforsker gir deg tilgang til rå informasjon fra Blockchain og din Mempool gjennom en lettfattelig Interface-web. Du kan for eksempel enkelt sjekke statusen til en ventende transaksjon, se saldoen til en Address eller undersøke sammensetningen av en blokk.



For å få tilgang til den, må du bare hente Tor Address fra nettleseren din. Dette gjør du ved å kjøre den samme kommandoen som du brukte for å hente Address for DMT-en din:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Du får tilgang til all informasjon om Dojo-tilkoblingen din via Tor. Den vi er interessert i her, er følgende URL:



```
Block Explorer =
```



Hvis du allerede er koblet til DMT-enheten, kan du også finne denne Address i "*Pairing*"-menyen, inne i JSON-tilkoblingen:



![Image](assets/fr/43.webp)



For å få tilgang til nettleseren din fra en hvilken som helst maskin på et hvilket som helst nettverk (også eksternt), åpner du [Tor Browser](https://www.torproject.org/download/) og skriver inn URL-en du nettopp har hentet.



⚠️ **Vær vennlig å behandle denne Address strengt konfidensielt



Da får du tilgang til din egen Block explorer.



![Image](assets/fr/44.webp)



*Bildekreditt: https://ashigaru.rs/.*



For å spore en transaksjon skriver du bare inn txid i søkefeltet øverst til høyre.



![Image](assets/fr/45.webp)



*Bildekreditt: https://ashigaru.rs/.*



Hvis du vil sjekke bevegelsene som er knyttet til en Address, går du frem på samme måte ved å skrive inn Address i søkefeltet.



![Image](assets/fr/46.webp)



*Bildekreditt: https://ashigaru.rs/.*



Du kan også skrive inn Hash eller høyden på en blokk i søkefeltet for å vise detaljer.



![Image](assets/fr/47.webp)



*Bildekreditt: https://ashigaru.rs/.*



## 9. Vedlikehold av dojo



### 9.1 Stopp din Dojo



Du må aldri brått slå av strømmen til Dojo, da dette kan ødelegge visse databaser, spesielt Fulcrum-indekseren. Hvis du må slå den av, må du alltid utføre en ren nedstengning av Dojo, og når alle prosedyrer er fullført, må du også slå av maskinen:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Oppdater din Dojo



Dojo utvikles jevnlig, og nye versjoner utgis for å fikse feil, forbedre stabiliteten og legge til nye funksjoner. Det er derfor viktig [å se etter oppdateringer regelmessig](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) og å oppdatere Dojo. Prosessen er lik den første installasjonen, men krever at du erstatter visse filer med den nyeste tilgjengelige versjonen, samtidig som du beholder konfigurasjonen. Her er de detaljerte trinnene du må følge for en ren og sikker oppdatering:



For å finne ut hvilken versjon av Dojo du har, kjører du kommandoen :



```bash
./dojo.sh version
```



Selv om dette trinnet er valgfritt, anbefaler jeg at du starter med å oppdatere operativsystemet ditt. Dette reduserer risikoen for inkompatibilitet og sikrer at avhengighetene som brukes av Dojo, er oppdaterte:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Gå til Dojo-katalogen og stopp de aktuelle tjenestene:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Start deretter systemet på nytt for å begynne på nytt:



```bash
sudo reboot
```



Dojo leveres med digitalt signerte filer. Disse PGP-signaturene sikrer at filene stammer fra utvikleren og ikke har blitt endret på noen måte. Det er viktig å sjekke dem hver gang du oppdaterer Dojo, akkurat som du gjorde da du installerte det første gang. Start med å laste ned utviklerens offentlige nøkkel via Tor, og importer den deretter :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Gå tilbake til din personlige katalog:



```bash
cd ~/
```



Last ned den nyeste versjonen av Dojo fra GitHub via Tor. I dette eksemplet er det versjon `1.28.0` (som ennå ikke eksisterer i skrivende stund: dette er bare for å gi et eksempel). Husk å erstatte filen og lenken [med den versjonen du ønsker å installere](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Last også ned filen som inneholder PGP-fingeravtrykkene og signaturen (husk igjen å justere versjonen i kommandoen):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Kontroller at den nedlastede fingeravtrykksfilen er signert med utviklerens nøkkel:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Et korrekt resultat skal vises :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Det kan vises en advarsel om at nøkkelen ikke er sertifisert, men det har ingen betydning. Hvis signaturen derimot er ugyldig eller tilsvarer en annen nøkkel, må du ikke gå lenger, men begynne på nytt og sjekke koblingene.



Deretter beregner du SHA256-fingeravtrykket til arkivet og sammenligner det med den offisielle fingeravtrykksfilen :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Hvis de to fingeravtrykkene stemmer perfekt overens, er arkivet ekte og intakt. Hvis de er forskjellige, må du slette filene umiddelbart og ikke fortsette.



Dekomprimer arkivet i hjemmekatalogen din:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Kopier deretter innholdet til Dojo-katalogen, og overskriv den gamle :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Denne operasjonen beholder konfigurasjonsfilene som ligger i `~/dojo-app/docker/my-dojo/conf`, men erstatter alle andre filer med de oppdaterte versjonene.



For å holde miljøet rent, sletter du unødvendige filer :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Gå tilbake til Dojo-skriptkatalogen, og kjør kommandoen update:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Denne kommandoen instruerer Docker om å gjenoppbygge avbildningene med de nye filene, og deretter automatisk starte alle tjenestene på nytt. På slutten av prosessen kan du sjekke loggene for å forsikre deg om at Bitcoin core, Fulcrum og Dojo fungerer som de skal:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Hvis tjenestene starter uten feil og loggene viser at blokker blir behandlet, er Dojo nå oppdatert og i drift.