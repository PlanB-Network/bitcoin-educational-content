---
name: Coordinatore Coinjoin - WabiSabi
description: Come impostare ed eseguire un coordinatore di coinjoin seguendo il protocollo WabiSabi (utilizzato in Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Introduzione 👋


In questa guida per esperti vi aiuteremo a configurare un coordinatore coinjoin, essenzialmente un server che riunisce le persone che vogliono risparmiare sulle commissioni di transazione o aumentare la loro privacy onchain nelle transazioni collaborative. Poiché non esiste più un coordinatore gestito da un'azienda in bundle con il Wasabi Wallet, gli utenti devono trovare e selezionare il proprio server coordinatore preferito. Solo pochi coordinatori si sono presentati chiedendo una tassa di coordinamento dello 0%, quindi gli sviluppatori di Wasabi Wallet hanno lavorato duramente per rendere il più semplice possibile iniziare a gestire il proprio coordinatore di comunità (su un hardware piccolo come un Raspberry Pi5!). I coordinatori attualmente attivi che chiedono lo 0% di spese di coordinamento possono essere trovati su [LiquiSabi](https://liquisabi.com) e soprattutto su [nostr](https://github.com/Kukks/WasabiNostr).


## Requisiti 🫴



- VPS (nodo ospitato) o computer/server (nodo auto-ospitato)
- Nodo Bitcoin Core potato/pieno (testato con v29.0)


Opzionale:


- (sotto)dominio che inoltra il traffico al nodo (ad es. coinjoin.[yourdomain].io)


Si consiglia di avere una certa esperienza con i prompt della riga di comando e con bash, poiché non tutti i passaggi possono essere automatizzati.


Dal punto di vista hardware è consigliabile avere un sistema con:


- 4 core
- 16 GB DI RAM
- 2 TB SSD o NVMe (per un nodo completo) / 128 GB SSD (per un nodo pruned)


Tali requisiti possono essere soddisfatti da un Raspberry Pi 5 per soli 120 dollari, escluso lo storage che costa circa 100 dollari per una chiavetta NVMe da 2 TB.


I VPS economici sono in genere dotati di un solo core e 4 GB di RAM, che ho scoperto essere troppo pochi per sincronizzare e verificare l'intero blockchain di bitcoin alla blockheight 911817.


Dal punto di vista dello storage, un nodo completo richiede almeno 2 TB di memoria su disco, preferibilmente di tipo SSD o NVMe. Quando si riduce il blockchain, è accettabile un'unità di archiviazione molto più piccola (ad esempio, un SSD da 128 GB).


Se si intende eseguire un coordinatore per coinjoin di grandi dimensioni (oltre 300 input), si consiglia di scegliere un sistema con core più veloci/nuovi con prestazioni più elevate per tutte le verifiche delle firme.


## Installazione 🛠️


Sul nodo vogliamo scaricare e installare l'ultima versione rilasciata di Wasabi Wallet, che include un backend e un coordinatore come eseguibili standalone accanto a wallet.


Trovare l'ultima versione: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) e verificare la firma PGP della release con le chiavi: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


I dettagli dell'implementazione variano a seconda dell'hardware (architettura della CPU) e della scelta del sistema operativo; di seguito vengono forniti i diversi dettagli per un Raspberry Pi (ARM-64) con Debian basato su RaspiBlitz come punto di partenza. Andare avanti per l'implementazione del sistema operativo Ubuntu (X86-64) utilizzando Nix.


Le istruzioni per l'installazione sono disponibili qui: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Distribuzione RaspiBlitz/Debian


Per i nodi RaspiBlitz (testati con la v1.11) è possibile utilizzare un deployment script costruito dal codice sorgente: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Facile da usare


Per una distribuzione minima, è sufficiente estrarre gli eseguibili per la propria piattaforma in una cartella.

Esempi di codici da riga di comando per Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Il risultato dovrebbe essere il seguente messaggio di firma valido:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


E si può procedere all'installazione del pacchetto scaricato:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Configurazione 🧾


Prima di eseguire il coordinatore è necessario modificare il file Config.json con il proprio:


- Bitcoin RPC credenziali
- Parametri di rotazione preferiti
- Coordinator Extended Public Key (creare un nuovo SegWit wallet per ricevere la polvere raccolta)

**Attenzione**: I Taproot wallet daranno luogo a UTXO non spendibili! Utilizzare un wallet Segwit nativo.


- Tipi di indirizzi di ingresso e di uscita consentiti
- Configurazione dell'annunciatore per la pubblicazione su nostr (nome, descrizione, Uri, ingressi minimi, relè nostr, chiave privata nostr)


È possibile gestire il coordinatore accessibile solo tramite l'indirizzo .onion, oppure utilizzare il proprio dominio clearnet personalizzato.


Trova o crea il file di configurazione in questo percorso:


`~/.walletwasabi/coordinator/Config.json`


Modificare con il comando:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Vedere questo esempio Config.json:


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

### Configurazione Tor 🧅


Per inserire la propria OnionServicePrivateKey è probabilmente necessario generarne una prima.


Wasabi Wallet genererà una chiave privata per voi se lo eseguite la prima volta con ```"PublishAsOnionService": true,`` impostato nel file Config.json.


Eseguire il coordinatore una volta con il comando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Per vedere l'indirizzo del servizio nascosto Onion, controllare i log del coordinatore con:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


e troverete qualcosa di simile:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


L'URL lungo che termina con .onion è il vostro indirizzo di servizio nascosto o CoordinatorUri.


Oppure ricontrollare il file di configurazione del coordinatore con:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Che ora dovrebbe essere compilato automaticamente.


## Esecuzione ⚡


Una volta impostati tutti i parametri di configurazione, è possibile eseguire il servizio di coordinamento e iniziare ad annunciare il primo round 🕶️


È sufficiente avviare il coordinatore con il comando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


È possibile monitorare il round corrente e il numero di UTXO/coin registrati controllando (nel browser Tor per .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Opzionale: debug del server coordinatore


È possibile monitorare eventuali problemi o errori nel file di log in ```~/.walletwasabi/backend/Logs.txt```


I problemi tipici includono problemi di connessione con RPC, che deve essere abilitato in ``~/.bitcoin/bitcoin.conf`` con:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Opzionale: Esecuzione del server backend


Insieme al coordinatore potete anche fornire un server di backend per gli utenti che non hanno un proprio nodo bitcoin a cui connettersi per le stime delle tariffe e i filtri di blocco.


Avviare il servizio con il comando:


```
wbackend
```


## Invitare gli utenti Wasabi al proprio coordinatore 🫂


Per far sì che gli altri utenti trovino il vostro servizio, potete affidarvi all'annunciatore nostr, oppure condividere un link magico con il vostro dominio (clearnet) o servizio nascosto (link .onion) e parametri circolari come questo:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Quando un utente copia il link magico e apre il suo Wasabi Wallet, il software mostrerà automaticamente la finestra di dialogo del coordinatore con il vostro dominio e i vostri parametri.


![detected](assets/en/02.webp)


💚🍣 Congratulazioni per la decentralizzazione della privacy in bitcoin 🕶️


Ricorda il tuo allenamento [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), il Wasabi Wallet è solo per la difesa 🛡️