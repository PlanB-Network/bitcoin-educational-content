---
name: Pears
description: Come si installano e si utilizzano le applicazioni su Pears?
---

![cover](assets/cover.webp)

In questo tutorial impareremo a eseguire applicazioni su **Pears**, una tecnologia peer-to-peer (P2P) sviluppata da **Holepunch** e supportata da **Tether**. L'obiettivo è semplice: rendere possibile la distribuzione e l'utilizzo di applicazioni web senza fare affidamento su alcuna infrastruttura centralizzata (nessun server, nessun host, nessun intermediario). In altre parole, anche se un provider cloud chiude o un paese blocca un dominio, l'applicazione continua a vivere tra i peer della rete.


## 1. Cos'è Pears?

Pears è un ambiente runtime, uno strumento di sviluppo e una piattaforma di distribuzione per applicazioni peer-to-peer. Questo strumento open-source permette di costruire, condividere ed eseguire software senza server o infrastrutture, direttamente tra utenti. In concreto, ciò significa che invece di ospitare un'applicazione su un server centrale, ogni utente diventa un nodo della rete, condividendo parte dell'applicazione e dei dati con altri peer. L'intero sistema forma una rete distribuita, con ogni istanza che coopera per mantenere il servizio accessibile.

![Image](assets/fr/01.webp)

Questo approccio si basa su una serie di componenti software modulari sviluppati da Holepunch:
- **Hypercore**: un registro distribuito che garantisce la coerenza e la sicurezza dei dati senza un database centrale.
- **Hyperbee**: un indicizzatore in cima a Hypercore, per un'organizzazione e una navigazione efficiente dei dati.
- **Hyperdrive**: un file system distribuito utilizzato per archiviare e sincronizzare i file delle applicazioni tra peer.
- **Hyperswarm** e **HyperDHT**: livelli di rete che consentono la scoperta e la connessione tra peer in tutto il mondo, senza un server centrale.
- **Secretstream**: un protocollo di crittografia E2E per proteggere gli scambi tra due peer.

Combinando questi componenti, Pears consente di creare applicazioni autonome, crittografate e distribuite, in cui ogni utente partecipa attivamente alla rete. Questa architettura decentralizzata elimina i costi di infrastruttura, i rischi di censura e gli SPOF (*Single Point of Failure*).


## 2. Origine e filosofia del progetto

Pears è sviluppato da Holepunch, una società fondata da Mathias Buus e Paolo Ardoino (CEO di Tether e CTO di Bitfinex), con la missione di estendere la logica peer-to-peer oltre a Bitcoin. La loro ambizione è quella di costruire il "Peer-to-Peer Internet", dove ogni applicazione può essere eseguita senza autorizzazione, senza server e senza intermediari. Holepunch è già alla base di **Keet**, un'applicazione di videoconferenza e messaggistica completamente P2P.

*Questa guida all'installazione di Pears è suddivisa in diverse sezioni a seconda del sistema operativo in uso. Passate direttamente alla sezione corrispondente al vostro ambiente per seguire le istruzioni appropriate*:
- **Linux (Debian)** → Parte **3**
- **Windows** → Parte **4**
- **macOS** → Parte **5**


## 3. Come installare Pears su Linux (Debian)

L'installazione di Pears su un sistema Debian è relativamente semplice, ma richiede alcuni prerequisiti che verranno illustrati in dettaglio in questa sezione.

### 3.1. Aggiorna il sistema

Innanzitutto, è importante assicurarsi che il sistema sia aggiornato.

```bash
sudo apt update && sudo apt upgrade -y
```

![Image](assets/fr/02.webp)

### 3.2. Installa le dipendenze

Pears si basa su alcune librerie di sistema, in particolare `libatomic1`, utilizzata dal runtime Bare JavaScript. Installala con il seguente comando:

```bash
sudo apt install -y libatomic1 curl git
```

![Image](assets/fr/03.webp)

### 3.3. Installa Node.js e npm tramite NVM

Pears è distribuito tramite *npm*, il gestore di pacchetti di *Node.js*. Sebbene Pears non dipenda direttamente da *Node.js* per funzionare, è necessario per l'installazione. Il metodo consigliato per l'installazione di *Node.js* su Linux è *NVM* (*Node Version Manager*), che consente di gestire diverse versioni di Node in parallelo.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

![Image](assets/fr/04.webp)

Quindi ricarica il terminale per attivare *NVM* :

```bash
source ~/.bashrc
```

![Image](assets/fr/05.webp)

Verifica che *NVM* sia installato:

```bash
nvm --version
```

![Image](assets/fr/06.webp)

Quindi installa una versione stabile di *Node.js* (ad esempio l'attuale LTS):

```bash
nvm install --lts
```

![Image](assets/fr/07.webp)

Controlla le installazioni di *Node.js* e *npm*:

```bash
node -v
npm -v
```

![Image](assets/fr/08.webp)

### 3.4 Installa Pears con npm

Una volta che *npm* è disponibile, è possibile installare Pears CLI a livello globale sul proprio sistema. Questo ti permetterà di eseguire il comando `pear` da qualsiasi directory.

```bash
npm install -g pear
```

![Image](assets/fr/09.webp)

### 3.5. Inizializza Pears

Dopo l'installazione, è sufficiente eseguire il seguente comando nel terminale:

```bash
pear
```

Al primo avvio, Pears si connette alla rete peer-to-peer per scaricare i componenti necessari. Questo processo non richiede un server centrale: i file vengono ottenuti direttamente da altri peer.

![Image](assets/fr/10.webp)

Una volta completato il download, esegui nuovamente il comando per verificare che tutto funzioni:

```bash
pear
```

![Image](assets/fr/11.webp)

Se tutto è stato installato correttamente, verrà visualizzata la Guida di Pears con un elenco dei comandi disponibili.

### 3.6. Prova Pears con Keet

Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.

```bash
pear run pear://keet
```

Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza passare per un server centrale. Se Keet viene lanciato correttamente, l'installazione di Pears è perfettamente funzionante.

![Image](assets/fr/12.webp)

Il vostro sistema Linux è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.


## 4. Come installare Pears su Windows

L'installazione di Pears su Windows è altrettanto facile che su Linux, ma richiede alcuni strumenti speciali.

*Se utilizzi Linux, puoi saltare al **passo 6**.*

### 4.1. Apri PowerShell in modalità amministratore

Prima di tutto, esegui PowerShell con i diritti di amministratore:
- Fai clic sul menu Start;
- Digita PowerShell;
- Clicca con il tasto destro del mouse su "_Windows PowerShell_";
- Seleziona "_Esegui come amministratore_".

![Image](assets/fr/15.webp)

### 4.2. Scarica NVS

Pears viene installato tramite *npm*, il gestore di pacchetti *Node.js*. Su Windows, il metodo raccomandato da Holepunch è di usare *NVS* (*Node Version Switcher*), che è più stabile di *NVM* su questo sistema.

In PowerShell, esegui il seguente comando per installare l'ultima versione di *NVS* :

```PowerShell
winget install jasongin.nvs
```

![Image](assets/fr/16.webp)

### 4.3. Installa Node.js

Dopo l'installazione, riavvia PowerShell e immetti il seguente comando:

```powershell
nvs
```

Si dovrebbe vedere un elenco delle versioni di *Node.js* disponibili. Seleziona la prima premendo il tasto `a` sulla tastiera.

![Image](assets/fr/17.webp)

*Node.js* è installato.

![Image](assets/fr/18.webp)

### 4.4. Controlla le installazioni

Assicurati che *Node.js* e *npm* siano accessibili:

```powershell
node -v
npm -v
```

Entrambi i comandi devono restituire un numero di versione.

![Image](assets/fr/19.webp)

### 4.5. Installazione di Pears con npm

Una volta che *Node.js* e *npm* sono disponibili, installa **Pears CLI** a livello globale sul sistema:

```powershell
npm install -g pear
```

Questo installerà il binario `pear` nella cartella globale *npm*.

![Image](assets/fr/20.webp)

### 4.6. Controlla e inizializza Pears

Una volta completata l'installazione, esegui:

```powershell
pear
```

Al primo avvio, Pears scaricherà automaticamente i componenti necessari dalla rete peer-to-peer. Questo processo può richiedere alcuni istanti.

![Image](assets/fr/21.webp)

Se tutto è andato bene, dovrebbe apparire la schermata di aiuto di CLI Pears con un elenco dei sottocomandi disponibili (run, seed, info...).

### 4.7. Prova Pears con Keet

Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.

```bash
pear run pear://keet
```

Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza passare per un server centrale. Se Keet viene lanciato correttamente, l'installazione di Pears è perfettamente funzionante.

![Image](assets/fr/22.webp)

Il vostro sistema Windows è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.


## 5. Come si installa Pears su macOS?

L'installazione di Pears su macOS è simile a quella su Linux, ma richiede alcune modifiche specifiche per l'ambiente Apple. Scopriamo insieme questi passaggi.

*Se utilizzi Linux o Windows e hai già installato Pears, procedi direttamente al **passo 6**.*

### 5.1. Verifica i requisiti di sistema

Prima dell'installazione, assicurati che *Xcode Command Line Tools* sia presente nel sistema. Questo pacchetto fornisce gli strumenti di compilazione necessari per _Node.js_ e le sue dipendenze.

Per farlo, apri un terminale con la scorciatoia da tastiera `Cmd + Barra spaziatrice`, quindi digita `Terminal` e premere il tasto `Invio`. È quindi possibile inserire questo comando nel terminale per avviare l'installazione:

```bash
xcode-select --install
```

Se gli strumenti sono già installati sul sistema, macOS ti informerà.

### 5.2. installare la NVM

Pears è distribuito tramite *npm*, il gestore di pacchetti *Node.js*. Sebbene Pears non dipenda direttamente da *Node.js* per funzionare, è necessario per l'installazione. Il metodo consigliato per l'installazione di *Node.js* su macOS è *NVM* (*Node Version Manager*), che consente di gestire diverse versioni di Node in parallelo.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

Quindi ricarica il terminale per attivare *NVM* :

```bash
source ~/.zshrc
```

Se si usa *bash* piuttosto che *zsh*, eseguire :

```bash
source ~/.bashrc
```

Quindi verifica che *NVM* sia installato:

```bash
nvm --version
```

Il terminale dovrebbe restituire la versione di *NVM* installata nel sistema.

### 5.3. Installa Node.js e npm

Quindi installa una versione stabile di *Node.js* (ad esempio l'attuale LTS):

```bash
nvm install --lts
```

Una volta completata l'installazione, verifica le versioni installate:

```bash
node -v
npm -v
```

Entrambi i comandi devono restituire un numero di versione.

### 5.4 Installa Pears con npm

Una volta che *npm* è disponibile, puoi installare Pears CLI a livello globale sul tuo sistema. Questo ti permetterà di eseguire il comando `pear` da qualsiasi directory.

```bash
npm install -g pear
```

### 5.5. Inizializza Pears

Dopo l'installazione, è sufficiente eseguire il seguente comando nel terminale:

```bash
pear
```

Al primo avvio, Pears si connette alla rete peer-to-peer per scaricare i componenti necessari. Questo processo non richiede un server centrale: i file vengono ottenuti direttamente da altri peer.

Una volta completato il download, esegui nuovamente il comando per verificare che tutto funzioni:

```bash
pear
```

Se tutto è stato installato correttamente, verrà visualizzata la Guida di Pears con un elenco dei comandi disponibili.

### 5.6. Prova Pears con Keet

Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.

```bash
pear run pear://keet
```

Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza passare per un server centrale. Se Keet viene lanciato correttamente, l'installazione di Pears è perfettamente funzionante.

Il sistema macOS è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.


## 6. Come si utilizza un'applicazione su Pears?

Una volta che Pears è attivo e funzionante, puoi eseguire l'applicazione di tua scelta direttamente con il seguente comando:

```bash
pear run pear://[KEY]
```

È sufficiente sostituire `[KEY]` con la chiave dell'applicazione che si desidera utilizzare.

![Image](assets/fr/13.webp)

Per sapere come far funzionare la nostra piattaforma Plan ₿ Academy su Pears, consultate questo tutorial completo:

https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Per scoprire come utilizzare l'applicazione di messaggistica Keet appena lanciata su Pears, consultate questo tutorial:

https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b
