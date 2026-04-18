---
name: Coinjoin-coördinator - WabiSabi
description: Hoe een coinjoin-coördinator opzetten en uitvoeren volgens het WabiSabi-protocol (gebruikt in Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Inleiding


In deze expertgids zullen we je helpen bij het opzetten van een coinjoin coördinator, in wezen een server die mensen samenbrengt die willen besparen op transactiekosten of hun onchain privacy willen verhogen in gezamenlijke transacties. Omdat er geen bedrijfsgestuurde coördinator meer gebundeld is met Wasabi Wallet, moeten gebruikers hun eigen voorkeursserver vinden en selecteren. Er zijn maar een paar coördinatoren die 0% coördinatiekosten vragen, dus de ontwikkelaars van Wasabi Wallet hebben hard gewerkt om het zo makkelijk mogelijk te maken om je eigen community-coördinator te runnen (op hardware zo klein als een Raspberry Pi5!). De momenteel actieve coördinatoren die 0% coördinatiekosten vragen, zijn te vinden op [LiquiSabi](https://liquisabi.com) en nog belangrijker op [nostr](https://github.com/Kukks/WasabiNostr).


## Vereisten 🫴



- VPS (gehost knooppunt) of computer/server (zelf gehost knooppunt)
- Gesnoeid/Volledig Bitcoin kernknooppunt (getest met v29.0)


Optioneel:


- (Sub)domein dat verkeer doorstuurt naar het knooppunt (bijv. coinjoin.[uwdomein].io)


Het wordt aanbevolen om enige ervaring te hebben met commandoregelprompts en bash, omdat niet alle stappen geautomatiseerd kunnen worden.


Qua hardware is het aan te raden om een systeem te hebben met:


- 4 kernen
- 16 GB RAM
- 2 TB SSD of NVMe (voor een full-node) / 128 GB SSD (voor een pruned-node)


In dergelijke behoeften kan worden voorzien door een Raspberry Pi 5 voor slechts 120 $, exclusief de opslag die ongeveer 100 $ kost voor een 2TB NVMe-stick.


Goedkope VPS worden meestal geleverd met slechts 1 core en 4GB RAM, wat volgens mij te weinig is om de hele bitcoin blockchain te synchroniseren en te verifiëren op blockheight 911817.


Qua opslag heeft een full-node minimaal 2TB aan schijfruimte nodig, bij voorkeur SSD of NVMe type. Bij het snoeien van de blockchain is een veel kleinere opslagschijf acceptabel (bijvoorbeeld een 128GB SSD).


Als je van plan bent om een coördinator voor grote (300+ input) coinjoins te gebruiken, is het aan te raden om een systeem te kiezen met snellere/nieuwe cores met een hogere prestatie voor alle handtekeningverificaties.


## Installatie 🛠️


Op het knooppunt willen we de laatst uitgebrachte versie van Wasabi Wallet downloaden en installeren, die een backend en coördinator bevat als zelfstandige uitvoerbare bestanden naast wallet.


Zoek de nieuwste versie: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) en controleer de PGP-handtekening van de uitgave met de sleutels: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


De implementatiedetails verschillen afhankelijk van de hardware (CPU-architectuur) en OS keuze, hieronder worden de verschillende details gegeven voor een Raspberry Pi (ARM-64) met RaspiBlitz op basis van Debian als startpunt. Ga verder voor de implementatie van (X86-64) Ubuntu OS met Nix.


De installatie-instructies vind je hier: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Inzet RaspiBlitz/Debian


Voor RaspiBlitz (getest met v1.11) knooppunten kan een script uitrol worden gebruikt die vanaf de broncode is gebouwd: [home.admin/config.scripts/bonus.wasabi.sh] (https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Eenvoudige implementatie


Voor een minimale implementatie wil je gewoon de uitvoerbare bestanden voor je platform uitpakken in een map.

Voorbeeld commandoregelcodes voor Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Dit zou moeten resulteren in het volgende geldige handtekeningbericht:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


En je kunt doorgaan met het installeren van het gedownloade pakket:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Configuratie 🧾


Voordat u de coördinator uitvoert, moet u het bestand Config.json bewerken met uw:


- Bitcoin RPC referenties
- Voorkeursrondeparameters
- Coördinator uitgebreide openbare sleutel (maak een nieuwe SegWit wallet voor het ontvangen van verzameld stof)

**Waarschuwing**: Taproot wallet zal resulteren in onuitgeefbare UTXO's! Gebruik hier een Native Segwit wallet.


- Toegestane typen invoer- en uitvoeradressen
- Omroeperconfiguratie voor publiceren via nostr (naam, beschrijving, Uri, minimumingangen, nostr-relais, nostr-privésleutel)


U kunt de coördinator alleen toegankelijk maken via het .onion-adres of uw eigen clearnet-domein gebruiken.


Zoek of maak het config-bestand op dit pad:


`~/.walletwasabi/coordinator/Config.json`


Bewerk het met het commando:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Zie dit voorbeeld Config.json:


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

### Tor-configuratie 🧅


Om je OnionServicePrivateKey in te vullen moet je er waarschijnlijk eerst een genereren.


Wasabi Wallet genereert een privésleutel voor je als je het de eerste keer uitvoert met ```"PublishAsOnionService": true,``` ingesteld in het Config.json bestand.


Voer de coördinator eenmaal uit met het commando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Om het verborgen serviceadres van de Ui te zien, controleer je de coördinatorlogs met:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


en je zult iets vinden als:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


De lange URL die eindigt op .onion is je verborgen serviceadres of CoordinatorUri.


Of controleer opnieuw uw coördinatorconfiguratiebestand met:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Dit zou nu automatisch moeten worden ingevuld.


## Hardlopen ⚡


Zodra alle configuratieparameters zijn ingesteld, kun je de coördinatorservice starten en je eerste ronde 🕶️ aankondigen


Start de coördinator gewoon met het commando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Je kunt de huidige ronde en het aantal geregistreerde UTXO's/munten controleren (in Tor browser voor .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Optioneel: debugging coördinator server


Je kunt controleren op problemen of fouten in het logbestand op ``~/.walletwasabi/backend/Logs.txt``


Typische problemen zijn RPC verbindingsproblemen, dit moet ingeschakeld worden in ``~/.bitcoin/bitcoin.conf`` met:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Optioneel: De backendserver uitvoeren


Samen met de coördinator kun je ook een backend server aanbieden voor gebruikers die geen eigen bitcoin node hebben om verbinding mee te maken voor kostenramingen en blockfilters.


Start deze service met het commando:


```
wbackend
```


## Wasabi-gebruikers uitnodigen voor uw coördinator 🫂


Voor andere gebruikers om je service te vinden kun je vertrouwen op de nostr announcer, of een magische link delen met je domein (clearnet) of verborgen service (.onion link) en ronde parameters zoals deze:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Wanneer een gebruiker de magische link kopieert en zijn Wasabi Wallet opent, toont de software automatisch het coördinatordialoogvenster met jouw domein en parameters.


![detected](assets/en/02.webp)


gefeliciteerd met het decentraliseren van de privacy van bitcoin 🕶️


Denk aan je training [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet is alleen voor verdediging 🛡️