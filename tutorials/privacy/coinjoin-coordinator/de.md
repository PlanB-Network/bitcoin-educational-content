---
name: Coinjoin Koordinator - WabiSabi
description: Einrichtung und Betrieb eines Coinjoin-Koordinators nach dem WabiSabi-Protokoll (verwendet in Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Einleitung 👋


In diesem Expertenleitfaden helfen wir Ihnen bei der Einrichtung eines Coinjoin-Koordinators, d.h. eines Servers, der Menschen zusammenbringt, die bei gemeinsamen Transaktionen Transaktionsgebühren sparen oder ihre Onchain-Privatsphäre erhöhen möchten. Da es keinen von einem Unternehmen betriebenen Koordinator mehr gibt, der mit Wasabi Wallet gebündelt ist, müssen die Nutzer ihren eigenen bevorzugten Koordinatorenserver finden und auswählen. Es sind nur wenige Koordinatoren aufgetaucht, die eine 0%ige Koordinationsgebühr verlangen, also haben die Entwickler von Wasabi Wallet hart daran gearbeitet, es so einfach wie möglich zu machen, einen eigenen Community-Koordinator zu betreiben (auf so kleiner Hardware wie einem Raspberry Pi5!). Die derzeit aktiven Koordinatoren, die 0% Koordinationsgebühr verlangen, finden Sie auf [LiquiSabi] (https://liquisabi.com) und vor allem auf [nostr] (https://github.com/Kukks/WasabiNostr).


## Anforderungen 🫴



- VPS (gehosteter Knoten) oder Computer/Server (selbst gehosteter Knoten)
- Abgeschnittener/vollständiger Bitcoin-Kernknoten (getestet mit v29.0)


Optional:


- (Sub-)Domain, die den Verkehr an den Knoten weiterleitet (z. B. coinjoin.[yourdomain].io)


Es wird empfohlen, einige Erfahrung mit Befehlszeilenaufforderungen und Bash zu haben, da nicht alle Schritte automatisiert werden können.


Hardwaremäßig ist es ratsam, ein System mit zu haben:


- 4 Kerne
- 16 GB RAM
- 2 TB SSD oder NVMe (für einen Full-Node) / 128 GB SSD (für einen pruned-Node)


Diese Anforderungen können von einem Raspberry Pi 5 für nur 120 $ erfüllt werden, ohne den Speicher, der für einen 2 TB NVMe-Stick rund 100 $ kostet.


Billige VPS haben in der Regel nur einen Kern und 4 GB RAM, was meiner Meinung nach zu wenig ist, um den gesamten Bitcoin blockchain mit der Blockhöhe 911817 zu synchronisieren und zu verifizieren.


Was den Speicherplatz betrifft, so benötigt ein vollständiger Knoten mindestens 2 TB Festplattenspeicher, vorzugsweise vom Typ SSD oder NVMe. Beim Beschneiden des blockchain ist ein viel kleineres Speicherlaufwerk akzeptabel (z. B. eine 128-GB-SSD).


Wenn Sie beabsichtigen, einen Koordinator für große (300+ Eingaben) Coinjoins einzusetzen, empfiehlt es sich, ein System mit schnelleren/neueren Kernen zu wählen, das eine höhere Leistung für alle Signaturüberprüfungen bietet.


## Einrichtung 🛠️


Auf dem Node wollen wir die letzte freigegebene Version von Wasabi Wallet herunterladen und installieren, die neben wallet auch ein Backend und einen Koordinator als eigenständige ausführbare Dateien enthält.


Suchen Sie die neueste Version: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) und überprüfen Sie die PGP-Signatur der Version mit den Schlüsseln: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Die Details der Implementierung hängen von der Hardware (CPU-Architektur) und der Wahl des Betriebssystems ab. Im Folgenden werden die verschiedenen Details für einen Raspberry Pi (ARM-64) mit Debian-basiertem RaspiBlitz als Ausgangspunkt angegeben. Fahren Sie fort mit dem Einsatz des Ubuntu-Betriebssystems (X86-64) unter Verwendung von Nix.


Die Installationsanweisungen finden Sie hier: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian-Einsatz


Für RaspiBlitz (getestet mit v1.11) Knoten kann ein aus dem Quellcode gebauter script verwendet werden: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Einfacher Einsatz


Für einen minimalen Einsatz müssen Sie nur die ausführbaren Dateien für Ihre Plattform in einen Ordner extrahieren.

Beispiel für Befehlszeilencodes für Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Das Ergebnis sollte die folgende gültige Signaturmeldung sein:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Dann können Sie das heruntergeladene Paket installieren:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfiguration 🧾


Bevor Sie den Koordinator starten, müssen Sie die Datei Config.json mit Ihrem:


- Bitcoin RPC Berechtigungsnachweise
- Bevorzugte Rundenparameter
- Erweiterter öffentlicher Schlüssel des Koordinators (Erstellen eines neuen SegWit wallet für den Empfang von gesammeltem Staub)

**Warnung**: Taproot wallet führen zu nicht auszahlbaren UTXO's! Verwenden Sie hier einen Native Segwit wallet.


- Erlaubte Eingangs- und Ausgangsadresstypen
- Konfiguration des Ansagers für die Veröffentlichung über nostr (Name, Beschreibung, Uri, Mindesteingaben, nostr-Relais, nostr-Privatschlüssel)


Sie können den Koordinator nur über die .onion-Adresse erreichen oder Ihre eigene Clearnet-Domain verwenden.


Suchen oder erstellen Sie die Konfigurationsdatei unter diesem Pfad:


`~/.walletwasabi/Koordinator/Config.json`


Bearbeiten Sie es mit dem Befehl:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Siehe dieses Beispiel Config.json:


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

### Tor-Konfiguration 🧅


Um Ihren OnionServicePrivateKey einzugeben, müssen Sie wahrscheinlich zuerst einen generieren.


Wasabi Wallet generiert einen privaten Schlüssel für Sie, wenn Sie es das erste Mal mit der Einstellung ```"PublishAsOnionService": true,``` in der Datei Config.json ausführen.


Führen Sie den Koordinator einmal mit dem Befehl aus:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Um die Adresse Ihres versteckten Onion-Dienstes zu sehen, überprüfen Sie entweder die Koordinatorprotokolle mit:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


und Sie werden etwas finden wie:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Die lange URL mit der Endung .onion ist Ihre versteckte Dienstadresse oder CoordinatorUri.


Oder überprüfen Sie noch einmal Ihre Koordinator-Konfigurationsdatei mit:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Diese sollte jetzt automatisch ausgefüllt werden.


## Laufend ⚡


Sobald alle Konfigurationsparameter eingestellt sind, können Sie den Koordinatordienst starten und mit der Ankündigung Ihrer ersten Runde beginnen 🕶️


Starten Sie den Koordinator einfach mit dem Befehl:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Du kannst die aktuelle Runde und die Anzahl der registrierten UTXO/Münzen überwachen, indem du (im Tor-Browser für .onion) nachschaust:


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Optional: Fehlersuche im Koordinatorenserver


Sie können alle Probleme und Fehler in der Logdatei unter ```~/.walletwasabi/backend/Logs.txt`` überwachen


Typische Probleme sind RPC Verbindungsprobleme, dies muss in ```~/.bitcoin/bitcoin.conf``` mit aktiviert werden:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Optional: Ausführen des Backend-Servers


Zusammen mit dem Koordinator können Sie auch einen Backend-Server für Benutzer bereitstellen, die keinen eigenen Bitcoin-Knoten haben, mit dem sie sich für Gebührenschätzungen und Blockfilter verbinden können.


Starten Sie diesen Dienst mit dem Befehl:


```
wbackend
```


## Einladen von Wasabi-Nutzern zu Ihrem Koordinator 🫂


Damit andere Nutzer Ihren Dienst finden, können Sie sich auf den nostr-Anzeiger verlassen oder einen magischen Link mit Ihrer Domain (clearnet) oder einem versteckten Dienst (.onion-Link) und runden Parametern wie diesem teilen:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Wenn ein Benutzer den magischen Link kopiert und seinen Wasabi Wallet öffnet, zeigt die Software automatisch den Koordinator-Dialog mit Ihrer Domain und Ihren Parametern an.


![detected](assets/en/02.webp)


💚🍣 Glückwunsch zur Dezentralisierung der Bitcoin-Privatsphäre 🕶️


Denken Sie an Ihre Ausbildung [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet ist nur zur Verteidigung gedacht 🛡️