---
name: Nodo fulmine RGB
description: Come si lancia un nodo Lightning compatibile con RGB con RLN?
---
![cover](assets/cover.webp)

In questo tutorial passo passo, imparerete a configurare un nodo Lightning RGB in un ambiente Regtest. Vedremo come creare i token RGB e farli circolare nei canali.

## Il progetto RLN

Il team RGB di Bitfinex lavora dal 2022 per arricchire l'ecosistema RGB sviluppando uno stack tecnologico completo. Piuttosto che puntare a un singolo prodotto commerciale, i suoi sforzi si concentrano sulla messa a disposizione di mattoni software open-source, sul contributo alle specifiche del protocollo RGB e sulla creazione di riferimenti di implementazione.

Tra i contributi notevoli di Bitfinex all'ecosistema RGB c'è [la libreria *RGBlib*](https://github.com/RGB-Tools/rgb-lib), scritta in Rust e accessibile tramite binding in Kotlin e Python, che semplifica notevolmente lo sviluppo di applicazioni RGB incapsulando complessi meccanismi di convalida e coinvolgimento.

Il team di Bitfinex ha anche progettato un portafoglio mobile RGB, chiamato "[*Iris Wallet*](https://iriswallet.com/)", disponibile su Android. Questo portafoglio integra l'uso di un server proxy RGB per gestire facilmente gli scambi di dati fuori catena (*conferimenti*) per la *convalida lato cliente* su RGB.

Bitfinex ha anche sviluppato il progetto `rgb-lightning-node` (RLN). Si tratta di un demone Rust basato su un fork di `rust-lightning` (LDK), modificato per tenere conto dell'esistenza di asset RGB in un canale. Quando viene aperto un canale, è possibile specificare la presenza di token RGB e ogni volta che lo stato del canale viene aggiornato, viene creata una transizione di stato che riflette la distribuzione dei token nelle uscite di Lightning. Questo permette di :


- Aprire canali Lightning in USDT, ad esempio;
- Instradare questi gettoni attraverso la rete, a condizione che i percorsi di instradamento abbiano una liquidità sufficiente;
- Sfruttare la logica di punizione e di timelock di Lightning senza modifiche: basta ancorare la transizione RGB in un'uscita aggiuntiva della transazione di impegno.

Il codice RLN è ancora in fase alfa: si consiglia di utilizzarlo solo in **regtest** o su **testnet**.

## Promemoria protocollo RGB

RGB è un protocollo che gira sopra Bitcoin ed emula le funzionalità dei contratti intelligenti e la gestione degli asset digitali, senza sovraccaricare la blockchain su cui si basa. A differenza degli smart contract on-chain convenzionali (come ad esempio su Ethereum), RGB si basa su un sistema di "*convalida lato cliente*": la maggior parte dei dati e delle cronologie di stato sono scambiati e memorizzati esclusivamente dai partecipanti coinvolti, mentre la blockchain Bitcoin ospita solo piccoli impegni crittografici (tramite meccanismi come *Tapret* o *Opret*). Nel protocollo RGB, la blockchain Bitcoin funge quindi solo da server di marcatura temporale e da sistema di protezione contro le doppie spese.

Un contratto RGB è strutturato come una macchina a stati evolutiva. Inizia con una Genesi che definisce lo stato iniziale (descrivendo, ad esempio, l'offerta, il ticker o altri metadati) secondo uno Schema rigorosamente tipizzato e compilato. Le transizioni di stato e, se necessario, le estensioni di stato vengono quindi applicate per modificare o estendere questo stato. Ogni operazione, sia che trasferisca beni fungibili (RGB20) sia che crei beni unici (RGB21), comporta *Sigilli a uso singolo*. Questi collegano gli UTXO Bitcoin agli stati fuori catena e impediscono la doppia spesa, garantendo al contempo riservatezza e scalabilità.

Per saperne di più sul funzionamento del protocollo RGB, vi consiglio di seguire questo corso di formazione completo:

https://planb.network/courses/csv402
## Installazione del nodo Lightning compatibile con RGB

Per compilare e installare il binario `rgb-lightning-node', si inizia clonando il repository e i suoi sottomoduli, quindi si esegue il comando :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- L'opzione `--recurse-submodules` clona anche i sottodispositivi necessari (compresa la versione modificata di `rust-lightning`);
- L'opzione `--shallow-submodules` limita la profondità del clone per accelerare il download, fornendo comunque l'accesso ai commit essenziali.

Dalla root del progetto, eseguire il seguente comando per compilare e installare il binario :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` assicura che la versione delle dipendenze sia rispettata;
- `--debug` non è obbligatorio, ma può aiutare a concentrarsi (si può usare `--release` se si preferisce);
- `-percorso .` indica a `cargo install` di installare dalla directory corrente.

Al termine di questo comando, un eseguibile `rgb-lightning-node' sarà disponibile nella cartella `$CARGO_HOME/bin/`. Assicurarsi che questo percorso sia presente in `$PATH`, in modo da poter invocare il comando da qualsiasi directory.

## Prerequisiti

Per funzionare, il demone `rgb-lightning-node` ha bisogno della presenza e della configurazione di :


- Un nodo `bitcoind`**

Ogni istanza RLN dovrà comunicare con `bitcoind` per trasmettere e monitorare le proprie transazioni sulla catena. Al demone dovranno essere forniti l'autenticazione (login/password) e l'URL (host/porta).


- Un indicizzatore** (Electrum o Esplora)

Il demone deve essere in grado di elencare ed esplorare le transazioni sulla catena, in particolare di trovare l'UTXO su cui è stata ancorata una risorsa. È necessario specificare l'URL del server Electrum o di Esplora.


- Un proxy RGB**

Il server proxy è un componente (opzionale, ma altamente raccomandato) per semplificare lo scambio di *conferme RGB* tra i peer Lightning. Anche in questo caso, è necessario specificare un URL.

Gli ID e gli URL vengono inseriti quando il demone viene *sbloccato* tramite l'API.

## Lancio di Regtest

Per un uso semplice, c'è uno script `regtest.sh` che avvia automaticamente, tramite Docker, un insieme di servizi: `bitcoind`, `electrs` (indicizzatore), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Consente di avviare un ambiente locale, isolato e preconfigurato. Crea e distrugge i contenitori e le directory di dati a ogni riavvio. Inizieremo avviando il file :

```bash
./regtest.sh start
```

Questo script :


- Creare una cartella `docker/` per memorizzare i file ;
- Eseguire `bitcoind` in regtest, così come l'indicizzatore `electrs` e il `rgb-proxy-server`;
- Aspettare che tutto sia pronto per l'uso.

![RLN](assets/fr/04.webp)

Successivamente, lanceremo diversi nodi RLN. In shell separate, eseguire ad esempio (per lanciare 3 nodi RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- Il parametro `--rete regtest` indica l'uso della configurazione regtest;
- `--daemon-listening-port` indica su quale porta REST il nodo Lightning ascolterà le chiamate API (JSON);
- `--ldk-peer-listening-port` specifica la porta Lightning p2p da ascoltare;
- `dataldk0/`, `dataldk1/` sono i percorsi delle directory di archiviazione (ogni nodo memorizza le proprie informazioni separatamente).

È ora possibile eseguire comandi sui nodi RLN dal browser, grazie all'API. In particolare, è possibile *sbloccare* i demoni. È sufficiente aprire un browser sullo stesso computer dei nodi e inserire l'URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Perché un nodo possa aprire un canale, deve prima disporre di bitcoin su un indirizzo generato con il seguente comando (per il nodo n°1, ad esempio):

```bash
curl -X POST http://localhost:3001/address
```

La risposta vi fornirà un indirizzo.

![RLN](assets/fr/06.webp)

Nel Regtest `bitcoind`, stiamo per estrarre alcuni bitcoin. Eseguire :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Inviare i fondi all'indirizzo del nodo generato sopra:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Quindi, estrarre un blocco per confermare la transazione:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Lancio di Testnet (senza Docker)

Se volete testare uno scenario più realistico, potete lanciare i nodi RLN sulla Testnet anziché in Regtest, puntando a servizi pubblici o controllati da voi:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Per impostazione predefinita, se non viene trovata alcuna configurazione, il demone cercherà di utilizzare il file :


- `bitcoind_rpc_host`: `electrum.iriswallet.com
- `bitcoind_rpc_port`: `18332
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Con il login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

È possibile personalizzare questi elementi anche tramite l'API `init`/`unlock`.

## Emissione di un token RGB

Per emettere un token, inizieremo creando degli UTXO "colorabili":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

Naturalmente è possibile adattare l'ordine. Per confermare la transazione, viene emesso un :

```bash
./regtest.sh mine 1
```

Ora possiamo creare una risorsa RGB. Il comando dipende dal tipo di risorsa che si desidera creare e dai suoi parametri. Qui sto creando un token NIA (*Non Inflatable Asset*) chiamato "PBN" con una dotazione di 1000 unità. La `precisione` consente di definire la divisibilità delle unità.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

La risposta include l'ID della risorsa appena creata. Ricordarsi di annotare questo identificatore. Nel mio caso, è :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

È quindi possibile trasferirlo sulla catena o allocarlo in un canale Lightning. Questo è esattamente ciò che faremo nella prossima sezione.

## Apertura di un canale e trasferimento di un asset RGB

È necessario prima collegare il proprio nodo a un peer sulla rete Lightning utilizzando il comando `/connectpeer`. Nel mio esempio, controllo entrambi i nodi. Quindi recupererò la chiave pubblica del mio secondo nodo Lightning con questo comando:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Il comando restituisce la chiave pubblica del mio nodo n°2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Successivamente, apriremo il canale specificando la risorsa pertinente (`PBN`). Il comando `/openchannel` consente di definire la dimensione del canale in satoshi e di scegliere di includere l'asset RGB. Dipende da cosa si vuole creare, ma nel mio caso il comando è :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Per saperne di più, cliccate qui:


- `peer_pubkey_e_opt_addr`: Identificatore del peer a cui ci si vuole connettere (la chiave pubblica trovata in precedenza);
- `capacità_sat`: Capacità totale del canale in satoshi ;
- `push_msat`: Importo in millisatoshi inizialmente trasferito al peer quando il canale viene aperto (qui trasferisco immediatamente 10.000 sats in modo che possa fare un trasferimento RGB più tardi) ;
- `asset_amount`: Quantità di risorse RGB da impegnare nel canale ;
- `asset_id` : identificatore univoco dell'asset RGB impegnato nel canale;
- `pubblico`: Indica se il canale deve essere reso pubblico per l'instradamento sulla rete.

![RLN](assets/fr/14.webp)

Per confermare la transazione, vengono estratti 6 blocchi:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Il canale Lightning è ora aperto e contiene anche 500 gettoni `PBN` dal lato del nodo n°1. Se il nodo n°2 desidera ricevere i token `PBN`, deve generare una fattura. Ecco come fare:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Con :


- `amt_msat`: Importo della fattura in millisatoshi (minimo 3000 sats) ;
- `scadenza_sec` : tempo di scadenza della fattura in secondi ;
- `asset_id` : identificativo dell'asset RGB associato alla fattura ;
- importo_patrimonio": Importo del bene RGB da trasferire con questa fattura.

In risposta, si otterrà una fattura RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Ora pagheremo questa fattura dal primo nodo, che detiene il denaro necessario con il token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Il pagamento è stato effettuato. Questo può essere verificato eseguendo il comando :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Ecco come distribuire un nodo Lightning modificato per trasportare risorse RGB. Questa dimostrazione si basa su :


- Un ambiente regtest (tramite `./regtest.sh`) o testnet ;
- Un nodo Lightning (`rgb-lightning-node`) basato su un `bitcoind`, un indicizzatore e un `rgb-proxy-server`;
- Una serie di API REST JSON per l'apertura/chiusura di canali, l'emissione di token, il trasferimento di attività tramite Lightning, ecc.

Grazie a questo processo :


- Le transazioni con impegno lightning includono un'uscita aggiuntiva (OP_RETURN o Taproot) con l'ancoraggio di una transizione RGB;
- I trasferimenti vengono effettuati esattamente come i tradizionali pagamenti Lightning, ma con l'aggiunta di un token RGB;
- Più nodi RLN possono essere collegati per instradare e sperimentare pagamenti attraverso più nodi, a condizione che ci sia sufficiente liquidità sia in bitcoin che in asset RGB sul percorso.

Se avete trovato utile questo tutorial, vi sarei molto grato se metteste un pollice verde qui sotto. Non esitate a condividere questo articolo sui vostri social network. Grazie mille!

Raccomando anche quest'altro tutorial in cui spiego come utilizzare lo strumento RGB CLI sviluppato dall'associazione LNP/BP per creare un contratto RGB:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4