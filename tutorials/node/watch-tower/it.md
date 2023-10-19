---
name: Watch Tower
description: Comprendere e utilizzare una torre di guardia
---

> Crediti a: https://blog.summerofbitcoin.org/bitcoin-lightning-and-the-eye-of-satoshi-watchtower-revolutionizing-transactions-and-security//

## Come funzionano le torri di guardia?

Parte essenziale dell'ecosistema della Lightning Network, le torri di guardia offrono un grado extra di protezione ai canali di lightning degli utenti. La loro principale responsabilità è monitorare la salute dei canali e intervenire se una delle parti del canale cerca di truffare l'altra.

Ma come può una torre di guardia determinare se un canale è stato compromesso? La torre di guardia riceve le informazioni necessarie dal client, una delle parti del canale, per identificare correttamente e rispondere a eventuali violazioni. Le informazioni più recenti sulla transazione, la condizione attuale del canale e le informazioni necessarie per creare transazioni di penalità sono spesso incluse in queste informazioni. Prima di trasmettere i dati alla torre di guardia, il client potrebbe crittografarli per proteggere la privacy e il segreto. Ciò impedisce alla torre di guardia di decrittare i dati crittografati a meno che non si sia verificata effettivamente una violazione, anche se ottiene i dati. La privacy del client è protetta da questo sistema di crittografia, che impedisce anche alla torre di guardia di accedere a dati privati senza autorizzazione.

## Come configurare il proprio Eye of Satoshi e iniziare a contribuire

L'Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) è una torre di guardia non custodiale per Lightning conforme a [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Ha due componenti principali:

1. teos: che include una CLI e la funzionalità principale lato server della torre. Quando viene compilato, verranno prodotti due binari: teosd e teos-cli.

2. teos-common: che include funzionalità condivise lato server e lato client (utile per creare un client).

Per eseguire correttamente la torre, è necessario avere bitcoind in esecuzione prima di eseguire la torre con il comando teosd. Prima di eseguire entrambi questi comandi, è necessario configurare il file bitcoin.conf. Ecco i passaggi su come farlo:

1. Installa Bitcoin Core dalla sorgente o scaricalo. Dopo il download, posiziona il file bitcoin.conf nella directory utente di Bitcoin Core. Controlla questo link per ulteriori informazioni su dove posizionare il file, poiché dipende dal sistema operativo che stai utilizzando.

2. Dopo aver identificato il luogo in cui deve essere creato il file, aggiungi queste opzioni:

```
#RPC
server=1
rpcuser=<tuo-utente>
rpcpassword=<tua-password>

#chain
regtest=1
```

- server: per le richieste RPC
- rpcuser e rpcpassword: i client RPC possono autenticarsi con il server
- regtest: non richiesto, ma utile se stai pianificando lo sviluppo.

rpcuser e rpcpassword devono essere scelti da te. Devono essere scritti senza virgolette. Ad esempio:

```
rpcuser=aniketh
rpcpassword=strongpassword
```

Ora, se esegui bitcoind, dovrebbe avviarsi il nodo.

1. Per la parte della torre, prima devi installare teos dalla sorgente. Segui le istruzioni fornite in questo link.
2. Dopo aver installato con successo teos nel tuo sistema e aver eseguito i test, puoi procedere con l'ultimo passaggio che consiste nel configurare il file teos.toml nella directory utente di teos. Il file deve essere posizionato in una cartella chiamata .teos (presta attenzione al punto) nella tua cartella home. Ad esempio, /home/<tuo-nome-utente>/.teos per Linux. Una volta trovato il posto, crea un file teos.toml e imposta queste opzioni corrispondenti alle cose che abbiamo modificato su bitcoind.

```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <tuo-utente>
btc_rpc_password = <tua-password>
```

Nota che qui il nome utente e la password devono essere scritti tra virgolette, ad esempio:

```
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```

Una volta fatto ciò, dovresti essere pronto per eseguire la torre. Dato che stiamo utilizzando regtest, è probabile che non ci siano blocchi estratti nella nostra rete di test bitcoin la prima volta che la torre si connette ad essa (se ci sono, qualcosa non va sicuramente). La torre costruisce una cache interna degli ultimi 100 blocchi da bitcoind, quindi quando viene eseguita per la prima volta potremmo ottenere il seguente errore:

> ERRORE [teosd] Non ci sono abbastanza blocchi per avviare la torre (richiesti: 100). Estrai almeno altri 100 blocchi

Dato che stiamo utilizzando regtest, possiamo estrarre blocchi emettendo un comando RPC, senza dover aspettare i 10 minuti di tempo mediano che di solito vediamo in altre reti (come mainnet o testnet). Controlla l'aiuto di bitcoin-cli e cerca come estrarre blocchi. Se hai bisogno di aiuto, puoi consultare questo articolo.

![image](assets\2.png)

Ecco fatto, hai eseguito con successo la torre. Congratulazioni. 🎉

https://blog.summerofbitcoin.org/bitcoin-lightning-and-the-eye-of-satoshi-watchtower-revolutionizing-transactions-and-security//
