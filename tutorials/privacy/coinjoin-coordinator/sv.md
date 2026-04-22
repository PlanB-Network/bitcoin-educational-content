---
name: Coinjoin-samordnare - WabiSabi
description: Hur man ställer in och kör en coinjoin-koordinator enligt WabiSabi-protokollet (används i Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Introduktion 👋


I den här expertguiden hjälper vi dig att konfigurera en coinjoin-koordinator, i huvudsak en server som sammanför människor som vill spara på transaktionsavgifter eller öka sin integritet i kedjan i samarbetstransaktioner. Eftersom det inte längre finns någon företagsdriven koordinator som levereras med Wasabi Wallet måste användarna hitta och välja sin egen föredragna koordinatorserver. Endast ett fåtal samordnare har dykt upp och bett om en samordningsavgift på 0%, så utvecklarna av Wasabi Wallet har arbetat hårt för att göra det så enkelt som möjligt att börja driva din egen samhällskoordinator (på hårdvara så liten som en Raspberry Pi5!). De för närvarande aktiva samordnarna som begär 0% samordningsavgift kan hittas på [LiquiSabi](https://liquisabi.com) och ännu viktigare på [nostr](https://github.com/Kukks/WasabiNostr).


## Krav 🫴



- VPS (hostad nod) eller dator/server (självhostad nod)
- Beskuren/full Bitcoin kärnnod (testad med v29.0)


Valfritt:


- (Sub)Domain som vidarebefordrar trafik till noden (t.ex. coinjoin.[yourdomain].io)


Vi rekommenderar att du har viss erfarenhet av kommandoradsuppmaningar och bash, eftersom alla steg inte kan automatiseras.


Hårdvarumässigt är det lämpligt att ha ett system med:


- 4 kärnor
- 16 GB RAM-MINNE
- 2 TB SSD eller NVMe (för en full nod) / 128 GB SSD (för en pruned-nod)


Sådana krav kan tillgodoses av en Raspberry Pi 5 för bara 120 $, exklusive lagring som kostar cirka 100 $ för en 2TB NVMe-sticka.


Billiga VPS kommer vanligtvis med endast 1 kärna och 4 GB RAM, vilket jag har funnit är för lite för att synkronisera och verifiera hela bitcoin blockchain på blockhöjd 911817.


Lagringsmässigt kommer en full nod att kräva minst 2 TB disklagring, helst SSD eller NVMe-typ. När blockchain beskärs kan en mycket mindre lagringsenhet accepteras (t.ex. en 128 GB SSD).


Om du tänker köra en koordinator för stora (300+ input) coinjoins rekommenderas att du väljer ett system med snabbare/nyare kärnor med högre prestanda för alla signaturverifieringar.


## Installation 🛠️


På noden vill vi ladda ner och installera den senast släppta versionen av Wasabi Wallet, som innehåller en backend och koordinator som fristående körbara filer bredvid wallet.


Hitta den senaste versionen: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) och verifiera PGP-signaturen för utgåvan med nycklarna: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Driftsättningsdetaljerna varierar beroende på maskinvara (CPU-arkitektur) och OS-val, nedan ges de olika detaljerna för en Raspberry Pi (ARM-64) med Debian-baserade RaspiBlitz som utgångspunkt. Hoppa vidare för (X86-64) Ubuntu OS-distribution med hjälp av Nix.


Installationsanvisningarna hittar du här: [Wasabi Docs] (https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian utplacering


För RaspiBlitz (testad med v1.11) noder kan en deployment script som bygger från källkod användas: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Enkel driftsättning


För en minimal utrullning behöver du bara extrahera de körbara programmen för din plattform i en mapp.

Exempel på kommandoradskoder för Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Detta bör resultera i följande giltiga signaturmeddelande:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Och du kan fortsätta att installera det nedladdade paketet:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfiguration 🧾


Innan du kör koordinatorn måste du redigera filen Config.json med din:


- Bitcoin RPC referenser
- Parametrar för önskad runda
- Coordinator Extended Public Key (skapa en ny SegWit wallet för att ta emot insamlat damm)

**Varning**: Taproot wallet kommer att resultera i outnyttjade UTXO! Använd en Native Segwit wallet här.


- Tillåtna typer av in- och utmatningsadresser
- Announcer-konfiguration för publicering över nostr (namn, beskrivning, Uri, minsta ingångar, nostr-relä, nostr-privat nyckel)


Du kan köra koordinatorn som endast är tillgänglig via .onion-adressen, eller använda din egen clearnet-domän.


Hitta eller skapa konfigurationsfilen på den här sökvägen:


`~/.walletwasabi/coordinator/Config.json`


Redigera den med kommandot:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Se detta exempel Config.json:


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

### Tor-konfiguration 🧅


För att fylla i din OnionServicePrivateKey måste du troligen generera en först.


Wasabi Wallet kommer att generera en privat nyckel åt dig om du kör den första gången med ```"PublishAsOnionService": true,``` inställd i filen Config.json.


Kör koordinatorn en gång med kommando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


För att se din Onion hidden service-adress kan du antingen kontrollera koordinatorloggarna med:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


och du kommer att hitta något liknande:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Den långa URL:en som slutar på .onion är din dolda serviceadress eller CoordinatorUri.


Eller kontrollera din koordinators konfigurationsfil igen med:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Vilket automatiskt ska fyllas i nu.


## Löpning ⚡


När alla konfigurationsparametrar har ställts in kan du köra koordinatortjänsten och börja annonsera din första omgång 🕶️


Starta helt enkelt koordinatorn med kommandot:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Du kan övervaka den aktuella omgången och antalet registrerade UTXO:or/mynt genom att kontrollera (i Tor-webbläsaren för .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Valfritt: felsökning av koordinatorserver


Du kan övervaka eventuella problem eller fel i loggfilen på ```~/.walletwasabi/backend/Logs.txt````


Typiska problem inkluderar RPC-anslutningsproblem, detta måste aktiveras i ```~/.bitcoin/bitcoin.conf```` med:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Valfritt: Köra backend-servern


Tillsammans med koordinatorn kan du också tillhandahålla en backend-server för användare som inte har sin egen bitcoin-nod att ansluta till för avgiftsberäkningar och blockfilter.


Starta denna tjänst med kommando:


```
wbackend
```


## Bjuda in Wasabi-användare till din koordinator 🫂


För att andra användare ska hitta din tjänst kan du förlita dig på nostr-annonsören, eller dela en magisk länk med din domän (clearnet) eller dolda tjänst (.onion-länk) och runda parametrar så här:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


När en användare kopierar den magiska länken och öppnar sin Wasabi Wallet, kommer programvaran automatiskt att visa koordinatordialogen med din domän och dina parametrar.


![detected](assets/en/02.webp)


💚🍣 Grattis till decentralisering av bitcoin-sekretess 🕶️


Kom ihåg din träning [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet är endast för försvar 🛡️