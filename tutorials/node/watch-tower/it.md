---
name: Lightning Watchtower
description: Comprensione e utilizzo di un Watchtower sul nodo Lightning
---
![cover](assets/cover.webp)



## Come funzionano le torri di guardia?



Parte essenziale dell'ecosistema Lightning Network, le _Watchtowers_ forniscono un ulteriore livello di protezione per i canali Lightning degli utenti. Il loro ruolo principale è quello di monitorare lo stato del canale e di intervenire se una parte del canale cerca di frodare l'altra.



Come può un Watchtower determinare se un canale è stato compromesso? Riceve dal cliente (una delle parti del canale) le informazioni necessarie per identificare e gestire correttamente qualsiasi violazione. Queste informazioni includono i dettagli della transazione più recente, lo stato attuale del canale e il Elements necessario per creare transazioni penali. Prima di trasmettere questi dati al Watchtower, il cliente può crittografarli per preservarne la riservatezza. In questo modo, anche se il Watchtower riceve i dati, non sarà in grado di decifrarli fino a quando non si sarà verificata una violazione. Questo meccanismo di crittografia protegge la privacy del cliente e impedisce al Watchtower di accedere in modo non autorizzato a informazioni sensibili.



In questa esercitazione, vedremo 3 modi per utilizzare un **Watchtower** :




- prima di tutto, il classico metodo grezzo tramite LND,
- poi un altro approccio con Eye of Satoshi,
- e infine, la configurazione semplificata di un Watchtower sul vostro nodo Lightning ospitato con Umbrel.



## 1 - Configurazione di un Watchtower o di un client tramite LND



*Questa esercitazione è tratta da [la documentazione ufficiale del LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Potrebbero essere state apportate alcune modifiche alla versione originale



Dalla versione 0.7.0, `LND` supporta l'esecuzione di un Watchtower altruistico privato come sottosistema completamente integrato in `LND`. Le torri di guardia forniscono una seconda linea di difesa contro scenari di violazione dolosa o accidentale quando il nodo del cliente è offline o non è in grado di rispondere al momento della violazione, offrendo un maggior grado di sicurezza per i fondi del canale.



A differenza delle torri di guardia _ricompensa_, che richiedono una parte dei fondi del canale in cambio del loro servizio, una torre di guardia _altruista_ restituisce tutti i fondi della vittima (meno le spese del On-Chain) senza richiedere una commissione. Le torri di guardia ricompensa saranno attivate in una versione successiva; sono ancora in fase di test e miglioramento.



Inoltre, il `LND` può ora essere configurato per funzionare come un _client di torre di guardia_, salvando le transazioni criptate di riparazione della violazione (le cosiddette "transazioni di giustizia") da altre torri di guardia altruiste. Il Watchtower memorizza blob crittografati di dimensioni fisse e può decifrare e pubblicare la transazione di giustizia solo dopo che la parte offesa ha trasmesso uno stato Commitment revocato. Le comunicazioni cliente ↔ Watchtower sono crittografate e autenticate utilizzando coppie di chiavi effimere, il che limita la capacità del Watchtower di rintracciare i propri clienti tramite credenziali a lungo termine.



Si noti che abbiamo scelto di distribuire in questa versione un insieme limitato di funzionalità che forniscono già una sicurezza significativa per gli utenti di `LND`. Molte altre funzionalità legate al Watchtower sono prossime al completamento o in fase avanzata; continueremo a distribuirle man mano che le testiamo e non appena saranno ritenute sicure.



nota: per il momento, le torri di guardia salvano solo l'output `to_local` e `to_remote` degli impegni revocati; il salvataggio dell'output HTLC sarà implementato in una versione futura, poiché il protocollo può essere esteso per includere ulteriori dati di firma in blob criptati._



### Configurazione di un Watchtower



Per configurare un Watchtower, gli utenti della riga di comando devono compilare il sotto-server opzionale `watchtowerrpc`, che consente l'interazione con il Watchtower tramite gRPC o `lncli`. I binari pubblicati includono il sotto-server `watchtowerrpc` per impostazione predefinita.



La configurazione minima per attivare il Watchtower è `Watchtower.active=1`.



È possibile recuperare le informazioni sulla configurazione del Watchtower con `lncli tower info`:



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



L'insieme completo delle opzioni di configurazione del Watchtower è disponibile tramite `LND -h`:



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Interfacce di ascolto



Per impostazione predefinita, il Watchtower ascolta su `:9911`, che corrisponde alla porta `9911` su tutte le interfacce disponibili. Gli utenti possono definire le proprie interfacce di ascolto tramite l'opzione `--Watchtower.listen=`. È possibile verificare la configurazione nel campo `"listeners"` di `lncli tower info`. Se si riscontrano problemi di connessione al Watchtower, verificare che la `<porta>` sia aperta o che il proxy sia configurato correttamente su un Interface attivo.



#### Indirizzi IP esterni



Gli utenti possono anche specificare l'IP esterno del Watchtower con `Watchtower.externalip=`, che espone l'URI completo del Watchtower (pubkey@host:port) tramite RPC o `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Gli URI Watchtower possono essere comunicati ai clienti per la connessione e l'utilizzo con il seguente comando:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Se i clienti di Watchtower devono accedervi da remoto, assicurarsi di :




- Aprire la porta 9911 (o una porta definita tramite `Watchtower.listen`).
- Utilizzare un proxy per reindirizzare il traffico da una porta aperta al Watchtower in ascolto.



#### Servizi nascosti Tor



Watchtowers supporta i servizi nascosti di Tor e può automaticamente generate all'avvio con le seguenti opzioni:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Il .onion Address appare quindi nel campo `"uris"` durante una query `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



nota: la chiave pubblica del Watchtower è diversa dalla chiave pubblica del nodo `LND'. Per il momento, funge da "whitelist del Soft", in quanto i clienti devono conoscere la chiave pubblica del Watchtower per usarlo come backup, in attesa di meccanismi di whitelist più avanzati. Si consiglia di NON divulgare apertamente questa chiave pubblica, a meno che non si sia disposti a esporre il proprio Watchtower all'intera Internet._



#### Directory del database Watchtower



Il database Watchtower può essere spostato utilizzando l'opzione `Watchtower.towerdir=`. Si noti che un suffisso `/Bitcoin/Mainnet/Watchtower.db` verrà aggiunto al percorso scelto per isolare i database per stringa. Pertanto, impostando `Watchtower.towerdir=/path/to/towerdir` si otterrà un database a `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



In Linux, ad esempio, il database predefinito del Watchtower si trova all'indirizzo :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Configurazione di un client Watchtower



Per configurare un client Watchtower, sono necessari due elementi:





- Attivare il client Watchtower con l'opzione `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- L'URI di un Watchtower attivo.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



È possibile configurare più torri di guardia in questo modo.



#### Tariffe per le transazioni legali



Gli utenti possono impostare facoltativamente la tariffa per le transazioni di giustizia tramite l'opzione `wtclient.sweep-fee-rate`, che accetta valori in sat/byte. Il valore predefinito è 10 sat/byte, ma è possibile puntare a tassi più alti per ottenere una maggiore priorità durante i picchi di spesa. La modifica di `sweep-fee-rate` si applica a tutti i nuovi aggiornamenti dopo il riavvio di daemon.



#### Supervisione



Con il comando `lncli wtclient`, gli utenti possono ora interagire direttamente con il client Watchtower per ottenere o modificare le informazioni su tutte le torri di guardia registrate.



Ad esempio, con `lncli wtclient tower`, è possibile conoscere il numero di sessioni attualmente negoziate con il Watchtower aggiunto in precedenza e determinare se viene utilizzato per i backup grazie al campo `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Per ottenere informazioni sulle sessioni Watchtower, utilizzare l'opzione `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Tutte le opzioni di configurazione del client Watchtower sono disponibili tramite `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Installazione del proprio occhio di Satoshi



*Questo tutorial è parzialmente estratto da un articolo del [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). Sono state apportate modifiche alla versione originale*



L'Occhio del Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) è un fulmine Watchtower non depositario, conforme a [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). È costituito da due componenti principali:





- teos**: include un Interface a riga di comando (CLI) e le funzioni server essenziali di Watchtower. Due binari - **teosd** e **teos-CLI** - vengono prodotti quando questo _crate_ viene compilato.





- teos-common**: include funzionalità condivise lato server e lato client (utile per creare un client).



Per eseguire correttamente Watchtower, è necessario eseguire **bitcoind** prima di lanciare Watchtower con il comando **teosd**. Prima di eseguire questi due comandi, è necessario configurare il file **Bitcoin.conf**. Ecco come fare:





- Installare Bitcoin core dai sorgenti o scaricarlo. Dopo il download, collocare il file **Bitcoin.conf** nella cartella utente di Bitcoin core. Consultare questo link per ulteriori informazioni sulla posizione del file, che dipende dal sistema operativo utilizzato.





- Una volta identificata la posizione, aggiungere le seguenti opzioni:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: per le richieste RPC





- rpcuser** e **rpcpassword**: autenticazione dei client RPC al server





- regtest**: non è richiesto, ma è utile se si sta pianificando lo sviluppo.



I valori di **rpcuser** e **rpcpassword** devono essere scelti dall'utente. Devono essere scritti senza virgolette. Ad esempio:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Ora, se si esegue **bitcoind**, il nodo dovrebbe avviarsi.





- Per la parte Watchtower, è necessario prima installare **teos** dai sorgenti. Seguire le istruzioni fornite in questo link.





- Dopo aver installato **teos** sul sistema ed eseguito i test, si può passare alla fase finale: impostare il file **teos.toml** nella directory utente di teos. Il file deve essere collocato in una cartella denominata **.teos** (notare il punto) sotto la propria home directory. Ad esempio, **/home//.teos** in Linux. Una volta individuata la posizione, creare un file **teos.toml** e impostare queste opzioni in linea con le modifiche apportate al **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Si noti che il nome utente e la password devono essere scritti **tra virgolette**. Utilizzando l'esempio precedente :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Una volta fatto ciò, dovreste essere pronti ad avviare il Watchtower. Poiché stiamo eseguendo **regtest**, è probabile che alla prima connessione del Watchtower non siano stati estratti blocchi sulla rete di test Bitcoin (se lo sono stati, c'è qualcosa che non va). Watchtower crea una cache interna degli ultimi 100 blocchi di **bitcoind**; quindi, al primo avvio, si potrebbe ottenere il seguente errore:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Dal momento che stiamo usando **regtest**, possiamo bloccare Miner emettendo un comando RPC, senza dover aspettare il ritardo medio di 10 minuti che si osserva su altre reti (come Mainnet o Testnet). Vedere la guida di **bitcoin-cli** per i dettagli su come effettuare i blocchi Miner.



![Image](assets/fr/01.webp)



Questo è tutto: avete eseguito con successo il Watchtower. Congratulazioni. 🎉




## 3 - Configurazione di un Watchtower su Umbrel



Su Umbrel, connettersi a un Watchtower per proteggere il proprio nodo Lightning è estremamente semplice, poiché tutto si svolge tramite il Interface grafico. Dopo la connessione remota al nodo, aprire l'applicazione "**Nodo Lightning**".



![Image](assets/fr/02.webp)



Fare clic sui tre puntini in alto a destra del Interface, quindi selezionare "**Impostazioni avanzate**".



![Image](assets/fr/03.webp)



Nel menu "**Watchtower**" sono disponibili due opzioni:





- Servizio Watchtower**: questa opzione consente di gestire un Watchtower, ossia un servizio che monitora i canali di altri nodi per individuare eventuali tentativi di frode. In caso di violazione, il vostro Watchtower pubblica una transazione sul Blockchain, consentendo agli utenti di recuperare i fondi bloccati. Una volta attivato, l'URI del vostro Watchtower appare e può essere comunicato ad altri nodi affinché lo aggiungano al proprio client Watchtower;





- Client Watchtower**: questa opzione consente di collegarsi a torri di guardia esterne per proteggere i propri canali. Una volta attivata, potete aggiungere servizi Watchtower ai quali il vostro nodo trasmetterà le informazioni necessarie sui suoi canali. Queste torri di controllo monitoreranno il loro stato e interverranno in caso di tentativi di frode.



La priorità per voi è ovviamente quella di attivare il *Client Watchtower* per proteggere il vostro nodo, ma vi consiglio anche di attivare il *Servizio Watchtower* per contribuire in cambio alla sicurezza degli altri utenti.



![Image](assets/fr/04.webp)



Quindi fare clic sul pulsante "**Save and Restart Node**" del Green. Il LND si riavvia.



Nello stesso menu, troverete anche l'URI del vostro servizio Watchtower, se lo avete attivato. È anche possibile aggiungere l'URI di un Watchtower esterno per proteggere i propri canali. Fare clic su "**ADD**" per confermare.



![Image](assets/fr/05.webp)



Ci sono diverse torri di guardia disponibili online. Ad esempio, [LN+ e Voltage offrono un Watchtower altruista](https://lightningnetwork.plus/Watchtower) a cui è possibile collegarsi:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Un'altra opzione è quella di Exchange il vostro URI Watchtower con i vostri compagni di bitcoiners, in modo che ognuno protegga il nodo dell'altro.



Raccomando inoltre di creare diverse torri di guardia per ridurre i rischi nel caso in cui una di esse non sia disponibile.



Infine, è possibile regolare il parametro "**Watchtower Client Sweep Fee Rate**". Questo parametro definisce la tariffa massima che siete disposti a pagare per includere in un blocco una transazione di punizione Watchtower broadcast. Assicuratevi di impostare un valore sufficientemente alto, adeguato agli importi bloccati nei vostri canali.