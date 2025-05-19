---
name: Lightning Network Daemon (Linux)
description: Installazione ed esecuzione di Lightning Network Daemon su Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Il Lightning Network è un secondo Layer del Bitcoin, che gli consente di assumere dimensioni fulminee, grazie soprattutto alla velocità e al basso costo delle transazioni che offre.



In questa guida, installeremo l'implementazione Lightning Network Daemon sulla nostra macchina Linux (distribuzione Ubuntu 24.04).



## Che cos'è il Lightning Network Daemon?



Lightning Network Daemon è un'implementazione completa in Go di Lightning Network. È stata creata da Lightning Labs e consente di eseguire un'istanza completa di un nodo Lightning sulla propria macchina.


In altre parole, con questa implementazione è possibile :





- Interagire con il Lightning Network**: È possibile utilizzare le linee di comando per creare portafogli Lightning, gestire canali e percorsi di pagamento e molto altro ancora, direttamente dal terminale della macchina.
- Collegamento di un nodo Bitcoin remoto o della propria istanza Bitcoin Core**: LND consente di collegare un'istanza Bitcoin e di utilizzarla come backend. Per utilizzare questa implementazione, non è necessario eseguire un'istanza Bitcoin Core sul proprio computer.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Perché avere un proprio nodo Lightning?


Lightning è un overlay Bitcoin che ottimizza il processo di trasferimento e riduce i costi delle transazioni.



Ruotando il vostro nodo Lightning, guadagnate sovranità e autonomia. Avete il controllo dei vostri fondi, quindi tenetelo a mente:



"Non le vostre chiavi, non i vostri bitcoin"



In questo senso, l'esecuzione di un nodo Lightning aumenta la sicurezza e l'integrità dei dati nei seguenti modi:





- Controllo totale**: Gestite i vostri canali di pagamento, diventate la vostra banca personale e siate padroni dei vostri beni.
- Riservatezza**: Operare senza affidarsi a terzi per proteggere la propria privacy.
- Apprendimento e autonomia**: Grazie ai comandi `lncli`, è possibile comprendere meglio i processi sottostanti a Lightning applicandosi dal proprio terminale.
- Decentramento**: Partecipare attivamente al rafforzamento e al decentramento del Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Per eseguire un'istanza dell'implementazione di LND sul nostro computer abbiamo due possibilità. Possiamo configurare l'ambiente sulla nostra macchina per eseguirlo localmente, oppure installare LND da un contenitore Docker. In questa sede ci concentreremo sulla prima opzione e vedremo come procedere con Docker in un'esercitazione successiva.


## Installare LND dal codice sorgente



### Prerequisiti


Poiché LND è scritto in Go, è necessario assicurarsi di avere l'ambiente GoLang e le dipendenze necessarie sulla propria macchina Linux.





- Requisiti hardware:**


Per un'esperienza fluida e senza interruzioni, la macchina deve avere la capacità necessaria per eseguire il nodo LND Lightning.



Avrete bisogno di :


1. **8 GB di RAM** per una fluidità ottimale,


2. **Un processore multi-core (quad-core o più)** per gestire in modo efficiente le azioni del nodo,


3. **Almeno 5 GB di spazio su disco** per la modalità nodo potato e 1 TB per eseguire Bitcoin Core (opzionale se si utilizza un nodo remoto)





- Installare le dipendenze utili:**


Il comando qui sotto vi permetterà di installare sul vostro computer gli strumenti necessari per eseguire LND. Tra le altre cose, dovrete installare `Git`, uno strumento di versionamento, e `make`, che può eseguire e compilare l'implementazione di LND dal codice sorgente.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Installare GoLang sulla macchina Linux**



Alla data di questa esercitazione, LND richiede la versione 1.23.6 di Go*** per l'installazione.



Se era già installata una versione precedente, rimuoverla per la nuova installazione di Go.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Configurazione dell'ambiente Go**


Nel file `~/.bashrc`, inizializzate le seguenti variabili d'ambiente per aggiungere Go al vostro sistema Linux.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Verifica dell'installazione** (in francese)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Clonare il repository LND su GitHub



Usare git per ottenere una copia del codice sorgente di LND in locale sulla propria macchina


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Costruire e installare



Lo strumento `make', precedentemente installato, vi permetterà di costruire un eseguibile dal codice sorgente di LND e di procedere con l'installazione.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Installare LND sulla macchina



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Verifica dell'installazione** (in francese)



Per assicurarsi che tutto sia andato bene, eseguire questo comando dovrebbe fornire la versione di LND attualmente in uso.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Manutenzione e aggiornamenti



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **IMPORTANTE**: Gli aggiornamenti di LND possono richiedere versioni più recenti di Go, quindi assicuratevi di aggiornare il vostro sistema per evitare problemi di dipendenza durante l'installazione.


### Configurazione del Lightning Network Daemon



La configurazione di un nodo Lightning LND è simile a quella del Bitcoin e viene eseguita in un file di configurazione contenente tutti i parametri del nodo. A tale scopo, nella radice della macchina è possibile creare una cartella nascosta `.LND` e quindi creare il file di configurazione `LND.conf` in questa cartella.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Nel file di configurazione, è possibile impostare il nodo LND.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Comprendere la configurazione



È importante capire la configurazione minima necessaria per un'installazione corretta e completa del nodo LND.



In base al contenuto del file `~/.LND/LND.conf', ecco i dettagli dei campi:





- noseedbackup**: Consente di scegliere se si desidera che LND esegua un backup automatico dei portafogli.  Impostando questa proprietà a `0` è possibile salvare manualmente le informazioni di ripristino in un luogo sicuro scelto personalmente.





- debuglevel**: Permette di definire il livello di dettaglio degli errori e dei log in caso di errori durante un'azione.





- Bitcoin.active**: Indica al LND di operare come un nodo Bitcoin e di interagire con la rete Bitcoin.





- Bitcoin.Mainnet**: Specifica che LND si connette alla rete principale di Bitcoin (Mainnet), è possibile impostare i valori `bitcoind.signet` e `bitcoind.regtest` rispettivamente per le reti Bitcoin Signet e Bitcoin Regtest





- Bitcoin.node**: Specifica il tipo di nodo Bitcoin a cui il LND deve collegarsi.





- Bitcoin.rpcuser** e **Bitcoin.rpcpassword** : Rappresentare.


rispettivamente i login (utente, password) per connettersi al proprio nodo Bitcoin





- bitcoind.zmqpubrawblock** e **bitcoind.zmqpubrawtx**: definiscono rispettivamente gli endpoint ZeroMQ per ricevere notifiche su nuovi blocchi e transazioni sulla rete Bitcoin.




## Verifica dell'installazione con LND



Probabilmente si vorrà verificare che il processo sia andato a buon fine e che si stia sincronizzando con il Lightning Network per mantenere aggiornate le informazioni sui nodi.



Per avviare l'implementazione di LND e ottenere informazioni sul proprio nodo, è sufficiente digitare il comando :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Esecuzione di azioni su LND



Una volta completata e verificata l'installazione, è possibile iniziare a utilizzarla.


Ecco i comandi essenziali per iniziare.



### Creare un portafoglio


Il vostro portafoglio Lightning è il primo passo di qualsiasi azione di gestione dei vostri fondi.



⚠️ **IMPORTANTE**: Prendete nota della vostra frase di 24 parole **seed**. Vi servirà per recuperare i fondi in caso di problemi.



Salvare anche la password del Wallet in modo da poterlo sbloccare con il comando `lncli unlock` quando si riavvia il nodo LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Controllare il saldo



Consultate i vostri conti direttamente dal vostro terminale:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informazioni sul nodo



Utilizzate il comando seguente per scoprire quali canali sono attivi sul vostro nodo.



```bash
lncli listchannels
```



È inoltre possibile ottenere un elenco dei nodi a cui si è connessi.



```bash
lncli listpeers
```



### Gestione dei canali



Un canale Lightning consente di avere una **connessione diretta, coppia per coppia, con un altro nodo del Lightning Network**. In questo canale è possibile utilizzare liberamente i satelliti Exchange fino alla capacità del canale.



### Collegarsi a un nodo



Connettersi ad altri nodi Lightning è un'azione fondamentale se si vuole partecipare attivamente e beneficiare della potenza di Lightning.



Per connettersi a un peer (nodo Lightning), sono necessarie tre informazioni:




- La chiave pubblica del nodo**: È l'identificatore unico del nodo nella rete Bitcoin;
- IP** : L'IP della macchina su cui è installato il nodo;
- PORT** :  La porta aperta sulla macchina che consente la comunicazione con questo nodo.



È possibile trovare i nodi a cui collegarsi su [amboss](https://amboss.space/), una piattaforma che elenca informazioni sui nodi Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Assicuratevi di collegarvi a **nodi affidabili** per preservare l'integrità del vostro sistema. Ecco alcuni consigli per scegliere le connessioni giuste.





- Diversificazione geografica**: Collegarsi a nodi in regioni diverse.





- Reputazione**: Scegliere nodi con una buona disponibilità.





- Capacità**: Scegliere nodi con una buona liquidità.





- Spese**: Spese di instradamento degli assegni.


### Aprire un canale di pagamento


Per aprire un canale di pagamento, assicurarsi di essere **connessi** al nodo peer, quindi definire la **capacità** (la quantità di satoshis) che si desidera bloccare in questo canale.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Creare un fulmine Invoice



Un Lightning Invoice rappresenta una stringa di caratteri che esprime il desiderio di ricevere satoshi nel proprio Lightning Wallet.


La creazione di fatture Lightning con il proprio nodo vi permette di proteggere i vostri dati (geografici e personali) e vi dà il 100% di autonomia sulla gestione dei vostri fondi.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Pagare un fulmine Invoice



```bash
lncli payinvoice <FACTURE>
```


### Chiudere un canale



Esistono due modi per chiudere un canale attivo sul nodo corrente.





- Chiusura cooperativa**: Segnala la volontà del nodo di ritirarsi dal canale di pagamento, garantendo il completamento delle attività in corso e il backup dei dati per evitare perdite di fondi.


```
lncli closechannel <ID_CANAL>
```




- Chiusura forzata**: ⚠️ Da evitare se possibile, questa azione interrompe i processi in corso nel vostro canale di pagamento e aumenta il rischio di perdita di fondi.


```
lncli closechannel --force <ID_CANAL>
```


## Pratiche ottimali e sicurezza per il nodo LND.


La sicurezza è fondamentale quando si utilizza un nodo Bitcoin/ Lightning. Ecco alcuni punti per rafforzare la sicurezza dell'installazione:





- Conservare la "frase seed" in un luogo sicuro e non in linea.





- Eseguire backup regolari del file `~/.LND/channel.backup`: Questo file salva gli stati dei canali ogni volta che un nuovo canale viene aperto (o un vecchio canale viene chiuso) sul vostro nodo.


⚠️ Consente di ripristinare i canali e recuperare i fondi bloccati nei canali di pagamento in caso di perdita di dati o guasto del nodo



È possibile ripristinare i fondi con il comando seguente, specificando il percorso di backup di questo file:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Accertarsi di aver salvato le parole di ripristino e la password di Lightning Wallet.
- Mantenete il vostro sistema aggiornato.



## Risoluzione dei problemi attuali


### Problemi frequenti




- Errore di connessione bitcoind** : Controllare i dati di accesso al RPC
- Sincronizzazione bloccata** : Controllare la connessione a Internet
- Errore di autorizzazione**: Controllare i diritti della cartella `~/.LND`




Siete arrivati alla fine di questo tutorial. Se volete saperne di più su Lightning, vi offriamo questo corso introduttivo per farvi capire meglio i concetti e le pratiche che stanno dietro al Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb