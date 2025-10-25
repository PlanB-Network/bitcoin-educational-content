---
name: Umbrel
description: Oppdag og installer Umbrel - din Bitcoin-node og hjemmeserver
---

![cover](assets/cover.webp)



## Innledning



### Hva er en Bitcoin-node?



En Bitcoin-node er en datamaskin som deltar i Bitcoin-nettverket ved å kjøre Bitcoin Core-programvaren eller en alternativ klient. Dens rolle er avgjørende for driften og sikkerheten i nettverket:





- **Blockchain-lagring**: Opprettholder en komplett, oppdatert kopi av Blockchain Bitcoin
- **Transaksjonsverifisering**: validerer hver transaksjon og blokk i henhold til protokollreglene
- **Formidling av informasjon**: Deler nye transaksjoner og blokker med andre noder
- **Skaper konsensus**: Bidrar til anvendelsen av nettverksregler



Å drive din egen Bitcoin-node er et avgjørende skritt mot økonomisk suverenitet, og gir deg flere viktige fordeler:





- **Konfidensialitet**: Del transaksjonene dine uten å avsløre informasjonen din til tredjeparter
- **Motstand mot sensur**: Ingen kan hindre deg i å bruke Bitcoin
- **Uavhengig verifisering**: Du trenger ikke å stole på andres noder for å verifisere transaksjonene dine
- **Bygge konsensus**: Bidra til anvendelsen av Bitcoin-nettverksreglene
- **Nettverksstøtte**: Bli en aktiv deltaker i nettverksdistribusjon og desentralisering



### Umbrel: En enkel løsning for drift av en Bitcoin-node



Umbrel er et operativsystem med åpen kildekode som forenkler installasjon og administrasjon av en Bitcoin-node. Det forvandler også datamaskinen din til en personlig og privat hjemmeserver, noe som gjør det enkelt å være vert for :





- En komplett Bitcoin-node
- Bitcoin viktige bruksområder (Electrs, Mempool.space)
- Andre personlige tjenester (skylagring, strømming, VPN osv.)



Med sin elegante og intuitive Interface-bruker Interface gjør Umbrel selvhusholdte tjenester tilgjengelige for alle, samtidig som du beholder full kontroll over dataene dine.



## Alternativer for montering av paraply



Umbrel tilbyr to hovedmåter å bruke løsningen på: et nøkkelferdig alternativ (Umbrel Home) og en gratis versjon med åpen kildekode (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Den nøkkelferdige løsningen



Umbrel Home er en forhåndskonfigurert hjemmeserver, spesialdesignet for en optimal opplevelse. Denne alt-i-ett-maskinvareløsningen inkluderer:



**Hardware-funksjoner**




- Prosessor med høy ytelse optimalisert for selvhosting
- Forhåndsinstallert SSD-lagring med høy hastighet
- Stillegående kjølesystem
- Kompakt, elegant design
- Integrerte USB- og Ethernet-porter



**Eksklusive fordeler**




- Plug-and-play-installasjon: plugg inn og sett i gang
- Premium support med dedikert assistanse
- Garanterte automatiske oppdateringer
- Integrert migreringsveiviser
- Full maskinvaregaranti
- Full støtte for alle funksjoner



**Pris**: €399 (prisen kan variere avhengig av sesong)



### UmbrelOS: Versjonen med åpen kildekode



UmbrelOS er den gratis, åpen kildekode-versjonen av Umbrel-operativsystemet. Med denne fleksible løsningen kan du bruke din egen maskinvare samtidig som du drar nytte av Umbrels viktige funksjoner.



**Fordeler**




- Helt gratis
- Åpen, verifiserbar kildekode
- Frihet til å velge
- Avanserte tilpasningsmuligheter



**Støttede plattformer**




- Raspberry Pi 5: En populær og rimelig løsning
- X86-systemer: For standard PC-er eller servere
- Virtuell maskin: For testing eller bruk på eksisterende infrastruktur



**Begrensninger**




- Kun støtte fra fellesskapet
- Noen avanserte funksjoner er forbeholdt Umbrel Home
- Mer teknisk innledende konfigurasjon
- Ytelsen avhenger av valgt maskinvare



Denne versjonen er ideell for :




- Tekniske brukere
- De som allerede eier kompatibelt utstyr
- Folk som ønsker å lære og eksperimentere
- Utviklere som ønsker å bidra til prosjektet



Offisielle installasjonslenker :




- [Installasjon på Raspberry Pi 5] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installasjon på x86-systemer (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Installasjon av virtuell maskin] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



I denne veiledningen konsentrerer vi oss om å installere UmbrelOS på en Raspberry Pi 5, men de grunnleggende prinsippene er de samme for andre plattformer.



## Installere Umbrel OS på Raspberry Pi 5



### Nødvendige komponenter



For denne installasjonen trenger du :





- Raspberry Pi 5 (4 GB eller 8 GB RAM)
- En offisiell Raspberry Pi-strøm Supply (avgjørende for stabilitet!)
- MicroSD-kort (minimum 32 GB)
- En microSD-kortleser
- En ekstern SSD for datalagring
- Ethernet-kabel
- En USB-kabel for å koble til SSD-enheten



### Installasjonstrinn



**Last ned UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Besøk [offisiell nettside] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Last ned den nyeste versjonen av UmbrelOS for Raspberry Pi 5



**Balena Etcher** installasjon



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Last ned og installer [Balena Etcher] (https://www.balena.io/etcher/) på datamaskinen din



**Klargjøring av microSD**-kortet



![Insertion carte microSD](assets/fr/03.webp)




- Sett microSD-kortet inn i datamaskinens kortleser



**Bildet blinker**



![Flashage UmbrelOS](assets/fr/04.webp)




- Lansering av Balena Etcher
- Velg det nedlastede UmbrelOS-bildet
- Velg microSD-kortet ditt som destinasjon
- Klikk på "Flash!" og vent til prosessen er ferdig
- Ta ut kortet på en sikker måte



**Installasjon av microSD-kort**



![Installation microSD](assets/fr/05.webp)




- Sett inn microSD-kortet i Raspberry Pi 5



**Perifer tilkobling**



![Connexion périphériques](assets/fr/06.webp)




- Koble den eksterne SSD-enheten til en tilgjengelig USB-port
- Koble Ethernet-kabelen mellom Pi og ruteren din



**Slå på**



![Démarrage du Pi](assets/fr/07.webp)




- Koble til den offisielle Raspberry Pi-strømforsyningen Supply
- Vent noen minutter på at systemet skal starte opp



**Første tilgang**



![Accès interface web](assets/fr/08.webp)




- Åpne nettleseren på en enhet som er koblet til samme nettverk
- Få tilgang til Umbrels Interface-nettsted på `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Hvis `umbrel.local` ikke fungerer, må du finne IP Address til din Raspberry Pi på ditt lokale nettverk. Du kan :




- Rådfør deg med ruterens Interface
- Bruke en nettverksskanner som nmap
- Bruk kommandoen `arp -a` i terminalen på datamaskinen din



## Første skritt på Umbrel



Når Umbrel er startet og tilgjengelig via nettleseren, følger du disse trinnene for å komme i gang:



### Opprinnelig konfigurasjon



**Opprett kontoen din**



![Création compte](assets/fr/10.webp)




- Velg et brukernavn
- Angi et sikkert passord
- Du trenger disse opplysningene for å få tilgang til Umbrel



**Kontobekreftelse**



![Confirmation compte](assets/fr/11.webp)




- Klikk på "Neste" for å få tilgang til dashbordet ditt



**Oppdagelsen av Interface**



![Interface Umbrel](assets/fr/12.webp)




- Få tilgang til Umbrel App Store
- Oppdag de mange tilgjengelige applikasjonene
- La oss begynne med å installere de viktigste programmene for Bitcoin



### Installere Bitcoin-applikasjoner



**Bitcoin Node**



![Bitcoin Node](assets/fr/13.webp)




- Første program som skal installeres
- Last ned og sjekk hele Blockchain Bitcoin



**Electrs**



![Installation Electrs](assets/fr/14.webp)




- Electrum-server for tilkobling av Bitcoin-lommebøker
- Synkroniserer med Bitcoin-noden din



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interface-skjerm for Blockchain
- Sporer transaksjoner og blokkeringer i sanntid



## Sporing av en transaksjon med Mempool.space



Mempool.space er en Blockchain-utforsker med åpen kildekode som gir sanntidsvisualisering av Bitcoin-nettverket. Den lar deg spore transaksjonene dine og forstå hvordan transaksjoner forplanter seg i nettverket.



### Forståelse av Mempool og bekreftelser



"Mempool" (minnebassenget) er som et virtuelt venterom der alle ubekreftede Bitcoin-transaksjoner lagres før de inkluderes i en blokk. Slik behandles en transaksjon:



1. **Broadcast**: Når du sender en transaksjon, blir den først kringkastet i Bitcoin-nettverket


2. **Venter i Mempool**: Venter på å bli valgt av en Miner på grunnlag av kostnader


3. **Første bekreftelse**: En mindreårig inkluderer den i en blokk (1. konfirmasjon)


4. **Ytterligere bekreftelser**: Hver nye blokk som utvinnes etter den som inneholder transaksjonen din, legger til en bekreftelse



Det anbefalte antallet bekreftelser avhenger av mengden :




- For små beløp: 1-2 bekreftelser kan være tilstrekkelig
- For store beløp: 6 bekreftelser anses generelt som svært sikre



### Utforsk Interface fra Mempool.space



1. **Startsiden** gir deg en oversikt over Bitcoin-nettverket:




   - Nylig utvunnede blokker
   - Kostnadsoverslag for ulike prioriteringer
   - Den nåværende tilstanden til Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Søk etter en transaksjon**: For å spore en spesifikk transaksjon, lim inn dens identifikator (txid) i søkefeltet øverst på siden.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analyser transaksjonsdetaljer



Når transaksjonen din er funnet, gir Mempool.space deg en fullstendig analyse:



1. **Vesentlig informasjon** :




   - Status (bekreftet eller ikke)
   - Betalte utgifter (i Sats/vB)
   - Estimert bekreftelsestid



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Transaksjonsstruktur** :




   - Visuell fremstilling av innganger og utganger
   - Detaljert liste over involverte adresser
   - Overførte beløp



3. **Tekniske data** :




   - Transaksjonsvekt
   - Virtuell størrelse
   - Format og versjon som brukes
   - Andre spesifikke metadata



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Fordeler med å bruke Mempool.space på Umbrel



1. **Konfidensialitet**: Dine forespørsler går gjennom din egen node


2. **Uavhengighet**: Ingen behov for å være avhengig av en tredjepartstjeneste


3. **Pålitelighet**: Tilgang til data selv når offentlige nettlesere er nede



Med denne applikasjonen kan du effektivt overvåke transaksjonene dine, forstå hvordan gebyrer påvirker bekreftelseshastigheten og få en bedre forståelse av hvordan Bitcoin-nettverket fungerer.



## Koble til en Wallet Bitcoin til noden din



### Electrs konfigurasjon



**Lokal tilkobling**



![Connexion locale](assets/fr/18.webp)




- For bruk i ditt lokale nettverk
- Raskere og enklere å sette opp



**Remote-tilkobling via Tor**



![Connexion Tor](assets/fr/19.webp)




- Slik får du tilgang til noden din fra hvor som helst
- Sikrere og mer privat



### Tilkobling med Sparrow Wallet



**Tilgang til parametere**



![Paramètres Sparrow](assets/fr/20.webp)




- Åpen spurv Wallet
- Gå til Innstillinger > Server
- Klikk på "Endre eksisterende tilkobling"



**Valg av tilkoblingstype**



Sparrow tilbyr tre tilkoblingsmodi:



***Public Server***




- Tilkobling til offentlige servere (f.eks. blockstream.info, Mempool.space)
- Enkelt, men mindre privat



***Bitcoin Core***




- Direkte tilkobling til en Bitcoin-node
- Privat, men langsommere



***Privat Electrum***




- Koble til Electrs-serveren din
- Kombinerer konfidensialitet og ytelse



**Electrs**-konfigurasjon



Velg tilkoblingstype ved hjelp av informasjonen som vises i Electrs-programmet vi så tidligere:



I begge tilfeller må du la alternativene "Bruk SSL" og "Bruk proxy" være avmerket.



**Lokal tilkobling**


Vert: umbrel.local


Portnummer: 50001



**Fjerntilkobling (Tor)**


Vert : [din-Address-onion]


Portnummer: 50001



Tor-tilkoblingen er nødvendig hvis du vil ha tilgang til noden utenfor det lokale nettverket.



![Configuration connexion](assets/fr/21.webp)


Hvis du vil ha mer informasjon om Sparrow Wallet-programvaren, har vi en omfattende veiledning :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Konklusjon



Umbrel er nå klar til bruk. Du deltar aktivt i Bitcoin-nettverket samtidig som du beholder full kontroll over dataene dine. Utforsk gjerne de mange andre applikasjonene som er tilgjengelige i Umbrel App Store for å utvide mulighetene til hjemmeserveren din.



## Nyttige ressurser



### Offisiell dokumentasjon




- [Offisielt Umbrel-nettsted](https://umbrel.com)
- [Umbrel-dokumentasjon] (https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel] (https://apps.umbrel.com)



### Bitcoin-applikasjoner




- [Bitcoin Core] (https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Fellesskapet




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel] (https://github.com/getumbrel)
- [Twitter Umbrel] (https://twitter.com/umbrel)