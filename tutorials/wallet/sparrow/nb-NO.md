---
name: Spurv Wallet
description: Installere, konfigurere og bruke Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet er en selvforvaltende Bitcoin-programvare for porteføljeforvaltning utviklet av Craig Raw. Denne programvaren med åpen kildekode er verdsatt av bitcoinere for sine mange funksjoner og intuitive Interface.

Det er to måter å bruke Sparrow på:


- Som en Hot Wallet, der de private nøklene er lagret på PC-en.
- Som en Cold Wallet-administrator, der private nøkler oppbevares på en Hardware Wallet. I denne modusen manipulerer Sparrow bare offentlig Wallet-informasjon, sporer midler, genererer adresser og bygger transaksjoner, men Hardware Wallet-signaturen er nødvendig for å gjøre disse transaksjonene gyldige. Den kan derfor erstatte applikasjoner som Ledger Live eller Trezor Suite.

Sparrow støtter lommebøker med én signatur og flere signaturer, og gjør det mulig å administrere flere lommebøker på en smidig måte. Du kan for eksempel styre en Wallet koblet til en Ledger, en annen til en Trezor, og samtidig ha en Hot Wallet.

Programvaren tilbyr også avanserte funksjoner for myntkontroll, slik at du kan velge nøyaktig hvilke UTXO-er som skal brukes i transaksjonene dine for å optimalisere konfidensialiteten.

Når det gjelder tilkobling, lar Sparrow deg koble deg til din egen Bitcoin-node, enten eksternt via en Electrum Server eller med Bitcoin Core. Det er også mulig å bruke en offentlig node hvis du ennå ikke har din egen. Fjerntilkoblinger gjøres via Tor.

## Installer Sparrow Wallet

Gå til [den offisielle nedlastingssiden for Sparrow Wallet] (https://sparrowwallet.com/download/) og velg programvareversjonen som passer til operativsystemet ditt.

![Image](assets/fr/01.webp)

Det er viktig å kontrollere programvarens integritet og autentisitet før du installerer den. Hvis du ikke vet hvordan du gjør dette, finner du en fullstendig veiledning her :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Når Sparrow er installert, kan du hoppe over de innledende forklaringsskjermene og gå rett til skjermbildet for tilkoblingsadministrasjon.

![Image](assets/fr/02.webp)

## Koble til Bitcoin-nettverket

For å samhandle med Bitcoin-nettverket og kringkaste transaksjonene dine, må Sparrow være koblet til en Bitcoin-node. Det er tre hovedmåter å etablere denne forbindelsen på:


- 🟡 Bruke en offentlig node, dvs. koble til en tredjepartsnode som tillater slike tilkoblinger. Hvis du ikke har din egen Bitcoin-node, kan du komme raskt i gang med Sparrow med dette alternativet. Noden du kobler deg til, vil imidlertid se alle transaksjonene dine, noe som kan gå på bekostning av konfidensialiteten din. Det er viktig å ha kontroll over nøklene dine, men det er enda bedre å ha din egen node. Bruk derfor kun dette alternativet hvis du er nybegynner, og vær klar over risikoen for personvernet ditt.
- 🟢 Koble til en Bitcoin Core-node. Hvis du har din egen Bitcoin Core-node, kan du koble den til Sparrow Wallet, enten lokalt hvis Bitcoin Core er installert på samme maskin, eller eksternt.
- 🔵 Tilkobling via en Electrum-server. Hvis Bitcoin-noden din er utstyrt med Electrum, slik tilfellet er med node-in-a-box-løsninger som Umbrel eller Start9, kan du koble deg til den eksternt fra Sparrow.

**Det er å foretrekke å bruke en tilkobling via Electrs eller Bitcoin Core på din egen node for å redusere behovet for å stole på en tredjepart og optimalisere konfidensialiteten**

### Koble til en offentlig node 🟡

Det er veldig enkelt å koble seg til en offentlig node. Klikk på fanen "*Public Server*".

![Image](assets/fr/03.webp)

Velg en node fra nedtrekkslisten.

![Image](assets/fr/04.webp)

Klikk deretter på "*Test Connection*".

![Image](assets/fr/05.webp)

Når du er tilkoblet, vil Sparrow Wallet vise en gul hake nederst i høyre hjørne av Interface for å indikere at du er koblet til en offentlig node.

![Image](assets/fr/06.webp)

### Tilkobling til en Bitcoin-kjerne 🟢

Den andre metoden for å koble til en Bitcoin-node er å koble Sparrow til en Bitcoin Core. Hvis Bitcoin Core er installert på samme maskin, vil autentiseringen skje via cookie-filen. Hvis Bitcoin Core er på en ekstern maskin, må du bruke passordet som er definert i filen `Bitcoin.conf`.

Vær oppmerksom på at hvis du bruker en beskåret Bitcoin Core-node, vil du ikke kunne gjenopprette en Wallet som inneholder transaksjoner som er eldre enn de lokalt lagrede blokkene. For en ny Wallet opprettet på Sparrow vil dette imidlertid ikke være noe problem: De nye transaksjonene dine vil være synlige, selv med en beskåret node.

For å konfigurere en Bitcoin Core-node kan du se en av følgende veiledninger, avhengig av operativsystemet ditt:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Gå til fanen "*Bitcoin Core*" på Sparrow.

![Image](assets/fr/07.webp)

**Med Bitcoin Core local:**

Hvis Bitcoin Core er installert på datamaskinen din, finner du filen `Bitcoin.conf` blant programvarefilene. Hvis denne filen ikke finnes, kan du opprette den. Åpne den med et tekstredigeringsprogram, og sett inn følgende linje:

```ini
server=1
```

Lagre deretter endringene.

Du kan også gjøre dette via Bitcoin-QTs Interface-grafikk ved å navigere til "*Innstillinger*" > "*Options...*" og aktivere alternativet "*Enable RPC server*".

Ikke glem å starte programvaren på nytt etter at du har gjort disse endringene.

![Image](assets/fr/08.webp)

Gå deretter tilbake til Sparrow Wallet og skriv inn banen til cookie-filen din, som vanligvis ligger i samme mappe som `Bitcoin.conf`, avhengig av operativsystemet ditt:

| **macOS** | ~/Bibliotek/Applikasjonssupport/Bitcoin | ~

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin

| **Linux** | ~/.Bitcoin | ~/.Bitcoin

![Image](assets/fr/09.webp)

La de andre parameterne være standard, URL `127.0.0.1` og port `8332`, og klikk deretter på "*Test Connection*".

![Image](assets/fr/10.webp)

Tilkoblingen er opprettet. En Green-hake vises nederst i høyre hjørne for å indikere at du er koblet til en Bitcoin Core-node.

![Image](assets/fr/11.webp)

**Med Bitcoin Core-fjernkontroll:**

Hvis Bitcoin Core er installert på en annen maskin som er koblet til samme nettverk, må du først finne filen `Bitcoin.conf` blant programvarefilene. Hvis denne filen ikke finnes ennå, kan du opprette den. Åpne denne filen med et tekstredigeringsprogram, og legg til følgende linje:

```ini
server=1
```

Når du har redigert filen, må du sørge for å lagre den i riktig mappe for operativsystemet ditt:

| **macOS** | ~/Bibliotek/Applikasjonssupport/Bitcoin | | **macOS** | ~/Library/Application Support/Bitcoin

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin

| **Linux** | ~/.Bitcoin | ~/.Bitcoin

Denne operasjonen kan også utføres via den grafiske Interface Bitcoin-QT Interface. Gå til menyen "*Settings*", deretter "*Options...*", og aktiver alternativet "*Enable RPC server*" ved å krysse av i den tilhørende boksen. Hvis filen `Bitcoin.conf` ikke finnes, kan du opprette den direkte fra denne Interface ved å klikke på "*Open Configuration File*".

![Image](assets/fr/12.webp)

Finn IP Address til maskinen som er vert for Bitcoin Core i ditt lokale nettverk. For å gjøre dette kan du bruke et verktøy som [Angry IP Scanner] (https://angryip.org/). La oss for eksempel anta at IP Address på noden din er `192.168.1.18`.

I filen `Bitcoin.conf` legger du til følgende linjer, og setter `rpcbind=192.168.1.18` til å samsvare med IP Address på noden din.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

I filen `Bitcoin.conf` legger du til et brukernavn og passord for eksterne tilkoblinger. Sørg for å erstatte `loic` med ditt brukernavn og `my_password` med et sterkt passord:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Etter at du har endret og lagret filen, starter du Bitcoin-QT-programvaren på nytt.

Du kan nå gå tilbake til Sparrow Wallet. Gå til fanen "*User / Pass*". Skriv inn brukernavnet og passordet du konfigurerte i filen `Bitcoin.conf`. La de andre parameterne være standard, dvs. URL `127.0.0.1` og port `8332`. Klikk deretter på "*Test Connection*".

![Image](assets/fr/15.webp)

Tilkoblingen er opprettet. En Green-hake vises nederst i høyre hjørne for å indikere at du er koblet til en Bitcoin Core-node.

![Image](assets/fr/16.webp)

### Koble til en Electrum-server 🔵

Det siste alternativet for tilkobling er å bruke en ekstern Electrum-server. Denne metoden lar deg koble deg til noden din via Tor fra en annen enhet, og drar nytte av en indekserer for å bla gjennom porteføljene dine på Sparrow raskere. Det er spesielt egnet hvis du har en node-i-en-boks-løsning som Umbrel eller Start9, som lar deg installere Electrum med ett enkelt klikk.

For å gjøre dette må du hente Tor `.onion' Address fra Electrum-serveren din. Med Umbrel, for eksempel, finner du den i Electrs applikasjon.

![Image](assets/fr/17.webp)

Åpne fanen "*Private Electrum*" på Sparrow Wallet.

![Image](assets/fr/18.webp)

Skriv inn Tor Address i det angitte feltet. Andre innstillinger kan forbli standard. Klikk deretter på "*Test Connection*".

![Image](assets/fr/19.webp)

Tilkoblingen er bekreftet. Hvis du lukker dette vinduet, vises en blå hake nederst i høyre hjørne, noe som indikerer at du er koblet til en Electrum-server.

![Image](assets/fr/20.webp)

## Lag en varm portefølje

Nå som Sparrow Wallet er konfigurert til å kommunisere med Bitcoin-nettverket, er du klar til å opprette din første Wallet. Denne delen veileder deg gjennom opprettelsen av en Hot Wallet, dvs. en Wallet der de private nøklene er lagret på datamaskinen din. Siden datamaskinen din er en kompleks maskin som er koblet til Internett, utgjør den en svært stor angrepsflate. Derfor bør en Hot Wallet kun brukes til begrensede mengder bitcoins. Hvis du vil lagre større beløp, bør du velge en sikker Wallet med en Hardware Wallet. Hvis det er dette du er ute etter, kan du hoppe videre til neste avsnitt.

For å opprette en Hot Wallet klikker du på "*File*"-fanen og deretter på "*New Wallet*" på startskjermen til Sparrow Wallet.

![Image](assets/fr/21.webp)

Skriv inn et navn på porteføljen din, og klikk på "*Opprett Wallet*".

![Image](assets/fr/22.webp)

Øverst i Interface kan du velge om du vil opprette en "*Single Signature*"- eller "*Multi Signature*"-portefølje. Rett nedenfor velger du hvilken type skript som skal låse UTXOene dine. Jeg anbefaler at du bruker den nyeste standarden: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Klikk deretter på "*Nye eller importerte Software Wallet*".

![Image](assets/fr/24.webp)

Velg BIP39-standarden, siden den støttes av praktisk talt all programvare i Bitcoin-porteføljen. Deretter velger du lengden på gjenopprettingsfrasen. For øyeblikket er det tilstrekkelig med en 12-ordsfrase, ettersom begge gir samme sikkerhet, men 12-ordsfrasen er enklere å lagre.

![Image](assets/fr/25.webp)

Klikk på "*generate New*"-knappen for å generate din Wallets Mnemonic-frase. Denne frasen gir full, ubegrenset tilgang til alle bitcoinsene dine. Alle som har denne frasen kan stjele pengene dine, selv uten fysisk tilgang til datamaskinen din.

Frasen på 12 ord gjenoppretter tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller ødeleggelse av datamaskinen din. Det er derfor svært viktig å lagre den nøye og oppbevare den på et trygt sted.

Du kan gravere den på papir eller, for ekstra sikkerhet, gravere den på rustfritt stål for å beskytte den mot brann, oversvømmelse eller kollaps. Valget av medium for Mnemonic avhenger av sikkerhetsstrategien din, men hvis du bruker Sparrow som en varm Wallet som inneholder moderate mengder, bør papir være tilstrekkelig.

Hvis du vil ha mer informasjon om hvordan du lagrer og administrerer Mnemonic frasen din, anbefaler jeg på det sterkeste å følge denne andre veiledningen, spesielt hvis du er nybegynner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Du må selvsagt aldri dele disse ordene på Internett, slik jeg gjør i denne veiledningen. Dette eksemplet Wallet vil kun bli brukt på Testnet og vil bli slettet ved slutten av veiledningen.**

Du kan også velge å legge til en passphrase BIP39 ved å klikke på "*Bruk passphrase*"-boksen. Advarsel: Det kan være svært nyttig å bruke en passphrase, men hvis du ikke forstår hvordan den fungerer, kan det være svært risikabelt. Derfor anbefaler jeg deg på det sterkeste å lese denne korte teoretiske artikkelen om emnet:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Når du har lagret Mnemonic og eventuelle passphrase på et fysisk medium, klikker du på "*Bekreft sikkerhetskopiering*".

![Image](assets/fr/27.webp)

Skriv inn de 12 ordene på nytt for å bekrefte at de er lagret riktig, og klikk deretter på "*Create Keystore*".

![Image](assets/fr/28.webp)

Klikk deretter på "*Importer Keystore*" for å generate porteføljenøklene dine fra Mnemonic-frasen.

![Image](assets/fr/29.webp)

Klikk på "*Apply*" for å fullføre opprettelsen av porteføljen.

![Image](assets/fr/30.webp)

Angi et sterkt passord for å sikre tilgangen til Sparrow-porteføljen din. Det er lurt å oppbevare dette passordet i en passordbehandler, slik at du ikke glemmer det. Merk at dette passordet ikke spiller noen rolle i utledningen av nøklene dine. Det brukes kun for å få tilgang til Wallet via Sparrow Wallet. Så selv uten dette passordet vil Mnemonic-frasen din være tilstrekkelig for å få tilgang til bitcoinsene dine fra alle BIP39-kompatible programmer.

![Image](assets/fr/31.webp)

Din Hot Wallet er nå opprettet. Du kan hoppe til *Mottak av bitcoins*-delen av denne veiledningen hvis du ikke planlegger å bruke en Hardware Wallet med Sparrow.

## Forvaltning av en Cold-portefølje

Den andre måten å bruke Sparrow Wallet på er å sette den opp som en porteføljeforvalter med en Hardware Wallet. I denne konfigurasjonen forblir de private nøklene til Bitcoin Wallet utelukkende på Hardware Wallet, mens Sparrow kun har tilgang til den offentlige informasjonen. Denne tilnærmingen gir et høyere sikkerhetsnivå enn Hot-lommebøkene som er omtalt ovenfor, ettersom de private nøklene oppbevares på en spesialisert enhet, ofte med en sikker chip, som ikke er koblet til Internett og derfor utgjør en mye mindre angrepsflate enn en tradisjonell datamaskin.

Det finnes to hovedmåter å koble Hardware Wallet til Sparrow på:


- Med kabel, vanligvis brukt med innstegsmodeller som Trezor Safe 3 eller Ledger Nano S Plus ;
- I Air-Gap-modus, dvs. uten direkte kablet tilkobling, via et MicroSD-kort eller QR-kode Exchange.

Sparrow støtter alle disse kommunikasjonsmetodene og er kompatibel med de fleste maskinvarelommebøker på markedet.

I denne veiledningen bruker jeg en Ledger Nano S med kabel, men fremgangsmåten er den samme i Air-Gap-modus. Du finner detaljer som er spesifikke for din Hardware Wallet i den dedikerte veiledningen om Plan ₿ Network.

Før du starter, må du kontrollere at Wallet allerede er konfigurert på Hardware Wallet. Hvis du bruker en kablet tilkobling, kobler du den til datamaskinen via kabelen.

For å importere den såkalte "*Keystore*" (den offentlige informasjonen som trengs for å administrere porteføljen) til Sparrow Wallet, klikker du på "*File*"-fanen og deretter på "*Ny Wallet*".

![Image](assets/fr/32.webp)

Gi porteføljen din et navn og klikk på "*Opprett Wallet*". Jeg anbefaler deg å oppgi navnet på Hardware Wallet for å enkelt kunne identifisere den senere.

![Image](assets/fr/33.webp)

Øverst på Interface kan du velge mellom en "*Enkeltsignatur*"- eller "*Flere signaturer*"-portefølje. I vårt eksempel vil vi konfigurere en enkeltsignaturportefølje.

Rett nedenfor velger du typen skript for å låse UTXO-ene dine. Hvis Hardware Wallet støtter det, foreslår jeg at du velger "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Deretter er fremgangsmåten forskjellig avhengig av tilkoblingsmetoden. Hvis du bruker en Air-Gap-metode, velger du "*Airgapped Hardware Wallet*". Følg deretter instruksjonene som er spesifikke for din enhet.

![Image](assets/fr/35.webp)

Hvis du bruker en kabeltilkobling, som i mitt tilfelle, velger du "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Klikk på "*Scan*" for å få Sparrow til å oppdage enheten din. Sørg for at den er koblet til og ulåst. For noen modeller, for eksempel Ledger, må du åpne "*Bitcoin*"-programmet for å aktivere deteksjon.

![Image](assets/fr/37.webp)

Velg "*Importer nøkkellager*".

![Image](assets/fr/38.webp)

Klikk på "*Apply*" for å fullføre opprettelsen av porteføljen.

![Image](assets/fr/39.webp)

Angi et sterkt passord for å sikre tilgangen til Sparrow Wallet. Dette passordet vil beskytte dine offentlige nøkler, adresser og transaksjonshistorikk. Vi anbefaler at du lagrer det i en passordbehandler. Merk at dette passordet ikke spiller noen rolle i utledningen av nøklene dine. Selv uten dette passordet kan du få tilgang til bitcoinsene dine med din Mnemonic via hvilken som helst BIP39-kompatibel programvare.

![Image](assets/fr/40.webp)

Forvaltningsporteføljen din er nå konfigurert på Sparrow.

![Image](assets/fr/41.webp)

## Motta bitcoins

Nå som Wallet er satt opp på Sparrow, kan du motta bitcoins. Bare gå til "*Mottak*"-menyen.

![Image](assets/fr/42.webp)

Sparrow vil vise den første ubrukte Address i din Wallet. Du kan legge til en "*Label*" til denne Address for å minne deg på opprinnelsen til disse satoshiene i fremtiden.

![Image](assets/fr/43.webp)

Hvis du bruker en Hot Wallet, kan Address som vises, brukes umiddelbart, enten ved å kopiere den eller ved å skanne den tilhørende QR-koden.

Hvis du bruker en Hardware Wallet, er det svært viktig å sjekke Address på enhetsskjermen før du bruker den. For kablede enheter kobler du til og låser opp Hardware Wallet, og deretter klikker du på "*Vis Address*" i Sparrow. Kontroller at Address som vises på Hardware Wallet, stemmer overens med det som vises på Sparrow.

![Image](assets/fr/44.webp)

For Hardware Wallet Air-Gap-brukere varierer Address-verifiseringen avhengig av enhetsmodell. Se den dedikerte Plan ₿ Network-veiledningen for nøyaktige instruksjoner.

Når transaksjonen har blitt sendt av betaleren, vises den under fanen "*Transaksjoner*". Du kan klikke på den for å få mer informasjon, for eksempel txid.

![Image](assets/fr/45.webp)

Under fanen "*Adresser*" finner du en liste over alle innboksadressene dine. Du kan se om de allerede er brukt, og om det er lagt til en etikett. *"*Mottak*"-adressene er de Sparrow viser når du klikker på "*Mottak*", og de er beregnet på innkommende betalinger. "*Change*"-adressene brukes til Exchange i transaksjonene dine, dvs. for å få tilbake den ubrukte delen av UTXO-ene dine i inngående betalinger.

![Image](assets/fr/46.webp)

Fanen "*UTXOs*" viser alle UTXO-ene dine, dvs. de Bitcoin-fragmentene du har. Du kan se mengden av hver UTXO og den tilhørende etiketten.

![Image](assets/fr/47.webp)

## Send bitcoins

Nå som du har noen satoshier i Wallet, har du også muligheten til å sende noen. Selv om det finnes flere måter å gjøre dette på, anbefaler jeg at du bruker "*UTXOs*"-menyen for å få mer nøyaktig kontroll over myntene du bruker (*myntkontroll*), i stedet for å gå direkte til "*Send*"-menyen (selv om sistnevnte kan være tilstrekkelig hvis du er nybegynner).

![Image](assets/fr/48.webp)

Velg UTXO-ene du ønsker å bruke som inndata for denne transaksjonen, og klikk deretter på "*Send Selected*". På denne måten kan du velge de mest hensiktsmessige kildene blant UTXO-ene dine, i henhold til utgiftene dine og etikettene som brukes når de mottas, for å optimalisere konfidensialiteten til betalingene dine. Sørg for at summen av de valgte UTXO-ene er større enn beløpet du ønsker å sende.

![Image](assets/fr/49.webp)

Skriv inn mottakerens Address i feltet "*Betal til*". Du kan også skanne Address med webkameraet ditt ved å klikke på kameraikonet. Med "*+Legg til*"-knappen kan du betale flere adresser i én enkelt transaksjon.

![Image](assets/fr/50.webp)

Legg til en etikett på transaksjonen for å minne deg på formålet med den. Denne etiketten vil også bli knyttet til din eventuelle Exchange.

![Image](assets/fr/51.webp)

Angi beløpet som skal sendes til denne Address.

![Image](assets/fr/52.webp)

Juster gebyrsatsen i henhold til gjeldende markedsforhold. Du kan gjøre dette ved å angi en absolutt avgiftsverdi eller ved å justere avgiftssatsen med glidebryteren.

![Image](assets/fr/53.webp)

Nederst på Interface kan du velge mellom "*Efficiency*" og "*Privacy*". I mitt tilfelle er ikke "*Privacy*"-alternativet tilgjengelig, ettersom jeg bare har én UTXO i denne porteføljen. "*Efficiency*" tilsvarer en klassisk transaksjon, mens "*Privacy*" er en transaksjon av Stonewall-typen, en transaksjonsstruktur som forsterker konfidensialiteten ved å simulere en mini-CoinJoin, noe som gjør kjedeanalysen mer kompleks.

![Image](assets/fr/54.webp)

Sparrow viser et sammendragsdiagram som viser inndata, utdata og transaksjonsgebyrer (merk at gebyrer faktisk ikke er en utdata, i motsetning til hva dette diagrammet antyder). Hvis du er fornøyd med alt, klikker du på "*Opprett transaksjon*".

![Image](assets/fr/55.webp)

Dette tar deg til en side med detaljer om Elements for transaksjonen din. Kontroller at all informasjonen er korrekt, og klikk deretter på "*Finalize Transaction for Signing*".

![Image](assets/fr/56.webp)

Det er viktig å beholde standard Sighash. For å forstå hvorfor, kan du ta en titt på dette kurset, der jeg forklarer alt du trenger å vite om Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

På det neste skjermbildet varierer alternativene avhengig av hvilken type Wallet du bruker:


- For en Hardware Wallet Air-Gap klikker du på "*Vis QR*" for å vise en PSBT som du kan signere med enheten din, og deretter laster du den signerte PSBT inn i Sparrow ved hjelp av "*Scan QR*". Alternativet "*Save Transaction*" fungerer på samme måte, men med utvekslinger på et microSD-minne;
- For en Hot Wallet klikker du bare på "*Sign*" og skriver inn Wallet-passordet for å signere ;
- For en kablet Hardware Wallet klikker du også på "*Sign*" for å sende den usignerte transaksjonen til enheten din.

![Image](assets/fr/57.webp)

Kontroller mottakerens Address, det sendte beløpet og gebyrene på din Hardware Wallet. Hvis alt er riktig, kan du fortsette med signeringen.

Når transaksjonen er signert, vises den på nytt i Sparrow, klar til å sendes ut på Bitcoin-nettverket for senere inkludering i en blokk. Hvis alt er i orden, klikker du på "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Transaksjonen din er nå sendt og venter på bekreftelse.

![Image](assets/fr/59.webp)

## Administrere og konfigurere porteføljer på Sparrow

I fanen "*Innstillinger*" finner du detaljert informasjon om porteføljen din, for eksempel :


- Porteføljetype (enkeltsignatur eller multi-sig) ;
- Type skript som brukes ;
- Navnet du har tildelt porteføljen ;
- Hovednøkkelavtrykk;
- Omkjøringsveien ;
- Kontoens utvidede offentlige nøkkel.

![Image](assets/fr/60.webp)

Med "*Eksporter*"-knappen kan du eksportere porteføljeinformasjonen din slik at du kan bruke den i andre programmer, samtidig som du beholder informasjonen som er satt opp i Sparrow.

Med knappen "*Legg til konto*" kan du legge til en ekstra konto i porteføljen din. En konto tilsvarer et separat sett med innboksadresser. Denne funksjonen kan for eksempel være nyttig hvis du ønsker å skille mellom en personlig konto og en bedriftskonto, med én enkelt Mnemonic-frase.

Knappen "*Avansert*" gir tilgang til avanserte innstillinger, for eksempel tilpasning av Sparrows Address-søk og endring av porteføljepassordet.

![Image](assets/fr/61.webp)

Når du lukker Sparrow Wallet, låses Wallet automatisk. Neste gang du åpner programvaren, vil et vindu be deg om å låse opp Wallet med passordet.

![Image](assets/fr/62.webp)

Hvis dette vinduet ikke åpnes, eller hvis du ønsker å åpne en annen portefølje på Sparrow, klikker du på fanen "*File*" og velger "*Open Wallet*".

![Image](assets/fr/63.webp)

Dette vil åpne File Manager til mappen der Sparrow lagrer lommebøkene dine. Velg den Wallet du ønsker å åpne, og skriv inn passordet for å låse den opp.

![Image](assets/fr/64.webp)

I "*File*"-menyen under "*Settings*" finner du parametrene for Bitcoin-nettverkstilkoblingen, som du allerede har sett på i de foregående avsnittene. Du kan også justere ulike parametere, for eksempel hvilken enhet som skal brukes, fiat-valuta for omregning og informasjonskilder.

![Image](assets/fr/65.webp)

Fanen "*Vis*" tilbyr tilpasningsalternativer og tilgang til noen nyttige kommandoer, for eksempel "*Aktualiser Wallet*", som oppdaterer transaksjonssøket for porteføljen din.

![Image](assets/fr/66.webp)

Fanen "*Verktøy*" samler flere avanserte verktøy, blant annet :


- med "*Sign/Verify Message*" kan du bevise at du er i besittelse av en mottakende Address eller verifisere en signatur.
- "*Send To Many*" tilbyr en forenklet Interface for å utføre transaksjoner til flere mottakeradresser samtidig, noe som er praktisk for batchutgifter.
- "*Sweep Private Key*" lar deg hente bitcoins som er sikret med en enkel privat nøkkel og overføre dem til Sparrow Wallet. Dette kan være spesielt nyttig for de som har bitcoins fra tidlig på 2010-tallet, før HD-lommebøkenes tid.
- "Verify Download" verifiserer integriteten og autentisiteten til nedlastet programvare før du installerer den på enheten din.
- "*Restart In*" lar deg bytte til lommebøkene dine på Testnet- eller Signet-nettverk. Dette kan være nyttig hvis du ønsker å få tilgang til testnettverk med mynter uten reell verdi.

![Image](assets/fr/67.webp)

Du vet nå alt om Sparrow Wallet-programvaren, et utmerket verktøy for daglig forvaltning av Bitcoin-porteføljene dine.

Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del den gjerne på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også denne andre veiledningen, der jeg forklarer hvordan du konfigurerer Hardware Wallet COLDCARD Q med Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3