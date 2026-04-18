---
name: Coinjoin-koordinator - WabiSabi
description: Slik setter du opp og kjører en coinjoin-koordinator i henhold til WabiSabi-protokollen (brukt i Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Innledning 👋


I denne ekspertveiledningen hjelper vi deg med å sette opp en coinjoin-koordinator, i hovedsak en server som samler folk som ønsker å spare transaksjonsgebyrer eller øke personvernet i kjeden i samarbeidstransaksjoner. Siden det ikke lenger følger med en koordinator drevet av et selskap med Wasabi Wallet, må brukerne finne og velge sin egen foretrukne koordinatorserver. Bare noen få koordinatorer har dukket opp og krever 0 % koordineringsavgift, så utviklerne av Wasabi Wallet har jobbet hardt for å gjøre det så enkelt som mulig å begynne å drive sin egen samfunnskoordinator (på maskinvare så liten som en Raspberry Pi5!). De for tiden aktive koordinatorene som krever 0 % koordineringsavgift finner du på [LiquiSabi] (https://liquisabi.com) og, enda viktigere, på [nostr] (https://github.com/Kukks/WasabiNostr).


## Krav 🫴



- VPS (hostet node) eller datamaskin/server (selvhostet node)
- Beskåret/full Bitcoin Core-node (testet med v29.0)


Valgfritt:


- (under)domene som videresender trafikk til noden (f.eks. coinjoin.[yourdomain].io)


Det anbefales at du har litt erfaring med kommandolinjeprompter og bash, ettersom ikke alle trinn kan automatiseres.


Maskinvaremessig anbefales det å ha et system med:


- 4 kjerner
- 16 GB RAM
- 2 TB SSD eller NVMe (for en full node) / 128 GB SSD (for en pruned-node)


Slike krav kan leveres av en Raspberry Pi 5 for bare 120 $, unntatt lagringsplassen som koster rundt 100 $ for en 2 TB NVMe-pinne.


Billige VPS-er har vanligvis bare én kjerne og 4 GB RAM, noe som er for lite til å synkronisere og verifisere hele bitcoin blockchain på blokkhøyde 911817.


Lagringsmessig vil en full node kreve minst 2 TB disklagring, helst av SSD- eller NVMe-type. Ved beskjæring av blockchain kan en mye mindre lagringsenhet aksepteres (f.eks. en 128 GB SSD).


Hvis du har tenkt å kjøre en koordinator for store (300+ input) coinjoins, anbefales det å velge et system med raskere/nyere kjerner med høyere ytelse for alle signaturverifiseringene.


## Installasjon 🛠️


På noden ønsker vi å laste ned og installere den siste utgitte versjonen av Wasabi Wallet, som inkluderer en backend og koordinator som frittstående kjørbare filer ved siden av wallet.


Finn den nyeste versjonen: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) og verifiser PGP-signaturen til utgivelsen med nøklene: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Distribusjonsdetaljene varierer avhengig av maskinvare (CPU-arkitektur) og OS-valg, nedenfor er de forskjellige detaljene gitt for en Raspberry Pi (ARM-64) med Debian-basert RaspiBlitz som utgangspunkt. Hopp videre for (X86-64) Ubuntu OS-distribusjon ved hjelp av Nix.


Du finner installasjonsinstruksjonene her: [Wasabi Docs] (https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Utplassering av RaspiBlitz/Debian


For RaspiBlitz-noder (testet med v1.11) kan en distribusjons-script som bygger fra kildekoden, brukes: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Enkel distribusjon


For en minimal distribusjon vil du bare pakke ut de kjørbare filene for plattformen din i en mappe.

Eksempel på kommandolinjekoder for Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Dette skal resultere i følgende gyldige signaturmelding:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Og du kan fortsette å installere den nedlastede pakken:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfigurasjon 🧾


Før du kjører koordinatoren, må du redigere Config.json-filen med din:


- Bitcoin RPC Legitimasjon
- Foretrukne rundeparametere
- Coordinator Extended Public Key (opprett en ny SegWit wallet for mottak av innsamlet støv)

**Advarsel**: Taproot wallet vil resultere i ubrukelige UTXO-er! Bruk en innfødt Segwit wallet her.


- Tillatte inngangs- og utgangsadressetyper
- Announcer-konfigurasjon for publisering over nostr (navn, beskrivelse, Uri, minimum innganger, nostr-relé, nostr-privatnøkkel)


Du kan kjøre koordinatoren som bare er tilgjengelig via .onion-adressen, eller bruke ditt eget clearnet-domene.


Finn eller opprett konfigurasjonsfilen på denne banen:


`~/.walletwasabi/coordinator/Config.json`


Rediger den med kommandoen:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Se dette eksempelet Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Tor-konfigurasjon 🧅


For å fylle inn OnionServicePrivateKey må du sannsynligvis generere en først.


Wasabi Wallet genererer en privat nøkkel for deg hvis du kjører den første gang med ```"PublishAsOnionService": true,``` angitt i Config.json-filen.


Kjør koordinatoren én gang med kommandoen:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Hvis du vil se adressen til den skjulte Onion-tjenesten, kan du enten sjekke koordinatorloggene med :


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


og du vil finne noe slikt:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Den lange URL-adressen som slutter på .onion, er din skjulte tjenesteadresse eller CoordinatorUri.


Eller sjekk konfigurasjonsfilen for koordinatoren på nytt med :


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Som automatisk skal fylles ut nå.


## Løping ⚡


Når alle konfigurasjonsparametrene er angitt, kan du kjøre koordinatortjenesten og begynne å kunngjøre den første runden 🕶️


Start koordinatoren med kommandoen:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Du kan følge med på den nåværende runden og antall registrerte UTXO-er/mynter ved å sjekke (i Tor-nettleseren for .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Valgfritt: feilsøking av koordinatorserver


Du kan se etter eventuelle problemer eller feil i loggfilen på ```~/.walletwasabi/backend/Logs.txt````


Typiske problemer inkluderer RPC-tilkoblingsproblemer, dette må aktiveres i ```~/.bitcoin/bitcoin.conf``` med:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Valgfritt: Kjører backend-serveren


Sammen med koordinatoren kan du også tilby en backend-server som brukere som ikke har sin egen bitcoin-node, kan koble seg til for å få avgiftsestimater og blokkfiltre.


Start denne tjenesten med kommandoen:


```
wbackend
```


## Invitere Wasabi-brukere til koordinatoren din 🫂


For at andre brukere skal finne tjenesten din, kan du stole på nostr-annonsøren, eller dele en magisk lenke med domenet ditt (clearnet) eller skjult tjeneste (.onion-lenke) og runde parametere som dette:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Når en bruker kopierer den magiske lenken og åpner Wasabi Wallet, vil programvaren automatisk vise koordinatordialogen med domenet og parameterne dine.


![detected](assets/en/02.webp)


💚🍣 Gratulerer med desentraliseringen av bitcoin-personvernet 🕶️


Husk treningen din [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet er kun til forsvar 🛡️