---
name: Plan ₿ Academy - Pears App
description: Come installare e utilizzare l'applicazione Plan ₿ Academy su Pears?
---

![cover](assets/cover.webp)


Probabilmente sapete già che Plan ₿ Academy è il più grande database educativo dedicato a Bitcoin, che riunisce corsi, tutorial e migliaia di risorse open-source. In origine, Plan ₿ Academy era un sito web. Ma cosa succederebbe se non fosse più possibile accedervi normalmente, ad esempio in caso di censura?


In questo tutorial impareremo a gestire la piattaforma **Plan ₿ Academy** in modo veramente resistente alla censura utilizzando **Pears**, una tecnologia peer-to-peer (P2P) sviluppata da **Holepunch** e supportata da **Tether**.


Pears è il software che ci permette di gestire la piattaforma Plan ₿ Academy senza affidarci a un sito web centralizzato. In questo tutorial, installeremo Pears sul vostro computer per accedere a Plan ₿ Academy attraverso Pears.


L'obiettivo di Pears è semplice: rendere possibile la distribuzione e l'utilizzo di applicazioni web senza dipendere da alcuna infrastruttura centralizzata (nessun server, nessun host, nessun intermediario). In altre parole, anche se un cloud provider chiude o un paese blocca un dominio, l'applicazione continua a vivere tra i peer della rete. Questo approccio permette alla nostra piattaforma educativa, Plan ₿ Academy, di rimanere accessibile in tutto il mondo, senza un singolo punto di guasto.


---

**TL;DR:**



- Installare le pere;



- Eseguire il seguente comando per avviare l'applicazione Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Cosa sono le pere?


Pears è allo stesso tempo un ambiente di runtime, uno strumento di sviluppo e una piattaforma di distribuzione per applicazioni peer-to-peer. Questo strumento open-source consente di costruire, condividere ed eseguire software senza server o infrastrutture, direttamente tra utenti. In termini pratici, ciò significa che invece di ospitare un'applicazione su un server centrale, ogni utente diventa un nodo della rete: condivide parte dell'applicazione e dei dati con altri peer. L'intero sistema forma una rete distribuita in cui ogni istanza collabora per mantenere il servizio accessibile.


![Image](assets/fr/01.webp)


Questo approccio si basa su una serie di componenti software modulari sviluppati da Holepunch:



- Hypercore**: un registro distribuito che garantisce la coerenza e la sicurezza dei dati senza un database centrale.
- Hyperbee**: un indice costruito in cima a Hypercore che permette di organizzare e interrogare i dati in modo efficiente.
- Hyperdrive**: un file system distribuito utilizzato per archiviare e sincronizzare i file delle applicazioni tra pari.
- Hyperswarm** e **HyperDHT**: livelli di rete che consentono la scoperta di peer e connessioni in tutto il mondo senza un server centrale.
- Secretstream**: un protocollo di crittografia end-to-end che protegge la comunicazione tra peer.


Combinando questi componenti, Pears consente di creare applicazioni autonome, crittografate e distribuite, in cui ogni utente partecipa attivamente alla rete. Questa architettura decentralizzata elimina i costi di infrastruttura, i rischi di censura e gli SPOF (*Single Points of Failure*).


Pears è sviluppato da Holepunch, una società fondata da Mathias Buus e Paolo Ardoino (CEO di Tether e CTO di Bitfinex), con la missione di estendere la logica peer-to-peer oltre il Bitcoin. La loro ambizione è costruire "*Internet dei peer*", dove ogni applicazione può operare senza permessi, senza server e senza intermediari. La loro ambizione è quella di costruire la "*Internet dei pari*", dove ogni applicazione possa operare senza permessi, senza server e senza intermediari. Holepunch è già alla base di **Keet**, un'applicazione di videoconferenza e messaggistica completamente P2P.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Questa guida all'installazione di Pears è suddivisa in più sezioni a seconda del sistema operativo in uso. Andate direttamente alla sezione corrispondente al vostro ambiente per seguire le istruzioni appropriate:*



- Linux (Debian)** → Sezione **2**
- Windows** → Sezione **3**
- macOS** → Sezione **4**


## 2. Come installare Pears su Linux (Debian)?


L'installazione di Pears su Debian è relativamente semplice, ma richiede alcuni prerequisiti che verranno illustrati in dettaglio in questa sezione.


### 2.1. Aggiornare il sistema


Prima di ogni altra cosa, è importante assicurarsi che il sistema sia aggiornato.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Installare le dipendenze


Pears si basa su alcune librerie di sistema, tra cui `libatomic1`, utilizzata dal motore di runtime Bare JavaScript. Installatelo con il seguente comando:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Installare Node.js e npm tramite NVM


Pears è distribuito attraverso *npm*, il gestore di pacchetti *Node.js*. Sebbene Pears non dipenda direttamente da *Node.js* per funzionare, è necessario per l'installazione. Il modo consigliato per installare *Node.js* su Linux è attraverso *NVM* (*Node Version Manager*), che consente di gestire più versioni di Node una accanto all'altra.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Quindi, ricaricare il terminale per attivare *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Verificare che la *NVM* sia installata correttamente:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Successivamente, installare una versione stabile di *Node.js* (ad esempio, la versione LTS corrente):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Verificare che *Node.js* e *npm* siano installati correttamente:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Installare Pears con npm


Una volta che *npm* è disponibile, è possibile installare globalmente Pears CLI sul proprio sistema. Ciò consente di eseguire il comando `pear` da qualsiasi directory.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inizializzare le pere


Dopo l'installazione, è sufficiente eseguire il seguente comando nel terminale:


```bash
pear
```


Al primo avvio, Pears si connette alla rete peer-to-peer per scaricare i componenti necessari. Questo processo non si basa su alcun server centrale: i file vengono recuperati direttamente da altri peer.


![Image](assets/fr/10.webp)


Una volta completato il download, eseguire nuovamente il comando per confermare che tutto funziona:


```bash
pear
```


![Image](assets/fr/11.webp)


Se tutto è stato installato correttamente, apparirà il menu di aiuto di Pears con un elenco dei comandi disponibili.


### 2.6. Test delle pere con Keet


Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P esistente e disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source sviluppato da Holepunch.


```bash
pear run pear://keet
```


Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza utilizzare un server centrale. Se Keet si avvia correttamente, significa che l'installazione di Pears è perfettamente funzionante.


![Image](assets/fr/12.webp)


Il vostro sistema Linux è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.


## 3. Come installare Pears su Windows


L'installazione di Pears su Windows è altrettanto semplice che su Linux, ma richiede alcuni strumenti specifici.


*Se si utilizza Linux e si è già installato Pears, si può passare direttamente al **fase 5**


### 3.1. Aprire PowerShell come amministratore


Innanzitutto, avviate PowerShell con i privilegi di amministratore:



- Fare clic sul menu Start;
- Digitare "PowerShell";
- Fate clic con il tasto destro del mouse su "*Windows PowerShell*";
- Selezionare "*Esegui come amministratore*".


![Image](assets/fr/15.webp)


### 3.2. Scaricare NVS


Pears viene installato tramite *npm*, il gestore di pacchetti *Node.js*. Su Windows, il metodo raccomandato da Holepunch è di usare *NVS* (*Node Version Switcher*), che è più stabile di *NVM* su questo sistema.


In PowerShell, eseguire il seguente comando per installare l'ultima versione di *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Installare Node.js


Dopo l'installazione, riavviare PowerShell, quindi immettere il seguente comando:


```powershell
nvs
```


Si dovrebbe vedere un elenco delle versioni di *Node.js* disponibili. Selezionare la prima premendo il tasto `a` sulla tastiera.


![Image](assets/fr/17.webp)


*Node.js* è ora installato.


![Image](assets/fr/18.webp)


### 3.4. Verifica delle installazioni


Assicurarsi che *Node.js* e *npm* siano accessibili:


```powershell
node -v
npm -v
```


Entrambi i comandi dovrebbero restituire un numero di versione.


![Image](assets/fr/19.webp)


### 3.5. Installare Pears con npm


Una volta che *Node.js* e *npm* sono disponibili, installare **Pears CLI** a livello globale sul sistema:


```powershell
npm install -g pear
```


Questo installa il binario `pear` nella cartella globale *npm*.


![Image](assets/fr/20.webp)


### 3.6. Verifica e inizializzazione di Pears


Una volta completata l'installazione, eseguire:


```powershell
pear
```


Al primo avvio, Pears scaricherà automaticamente i componenti necessari dalla rete peer-to-peer. Questo processo può richiedere alcuni istanti.


![Image](assets/fr/21.webp)


Se tutto è andato bene, si dovrebbe vedere il menu di aiuto di Pears CLI con l'elenco dei sottocomandi disponibili (run, seed, info...).


### 3.7. Prova pere con Keet


Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile in rete, come Keet, il software di messaggistica e videoconferenza open-source sviluppato da Holepunch.


```bash
pear run pear://keet
```


Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza utilizzare alcun server centrale. Se Keet viene lanciato con successo, significa che l'installazione di Pears è perfettamente funzionante.


![Image](assets/fr/22.webp)


Il vostro sistema Windows è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.


## 4. Come installare Pears su macOS


L'installazione di Pears su macOS è simile a quella di Linux, ma richiede alcuni aggiustamenti specifici per l'ambiente Apple. Esaminiamo insieme questi passaggi.


*Se si utilizza Linux o Windows e si è già installato Pears, si può passare direttamente al **fase 5**


### 4.1. Controllare i prerequisiti del sistema


Prima dell'installazione, assicurarsi che *Xcode Command Line Tools* sia installato sul sistema. Questo pacchetto fornisce gli strumenti di compilazione necessari per *Node.js* e le sue dipendenze.


Per farlo, aprire un terminale usando la scorciatoia `Cmd + Barra spaziatrice`, digitare `Terminal` e premere `Invio`. Quindi, eseguire il seguente comando nel terminale per installarlo:


```bash
xcode-select --install
```


Se gli strumenti sono già installati sul sistema, macOS ne darà notifica.


### 4.2. Installare la NVM


Pears è distribuito tramite *npm*, il gestore di pacchetti *Node.js*. Sebbene Pears non dipenda direttamente da *Node.js* per funzionare, è necessario per l'installazione. Il metodo consigliato per l'installazione di *Node.js* su macOS è *NVM* (*Node Version Manager*), che consente di gestire più versioni di Node contemporaneamente.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Quindi ricaricare il terminale per attivare *NVM*:


```bash
source ~/.zshrc
```


Se si usa *bash* invece di *zsh*, eseguire:


```bash
source ~/.bashrc
```


Successivamente, verificare che *NVM* sia installato correttamente:


```bash
nvm --version
```


Il terminale dovrebbe visualizzare la versione di *NVM* installata.


### 4.3. Installare Node.js e npm


Quindi, installare una versione stabile di *Node.js* (ad esempio, la versione LTS attuale):


```bash
nvm install --lts
```


Una volta completata l'installazione, verificare le versioni installate:


```bash
node -v
npm -v
```


Entrambi i comandi dovrebbero restituire un numero di versione.


### 4.4. Installare Pears con npm


Una volta che *npm* è disponibile, è possibile installare globalmente Pears CLI sul proprio sistema. Questo permetterà di eseguire il comando `pear` da qualsiasi directory.


```bash
npm install -g pear
```


### 4.5. Inizializzare le pere


Dopo l'installazione, è sufficiente eseguire il seguente comando nel terminale:


```bash
pear
```


Al primo avvio, Pears si connette alla rete peer-to-peer per scaricare i componenti necessari. Questo processo non richiede alcun server centrale: i file vengono recuperati direttamente dagli altri peer.


Una volta completato il download, rieseguire il comando per verificare che tutto funzioni:


```bash
pear
```


Se tutto è stato installato correttamente, apparirà il menu di aiuto di Pears con l'elenco dei comandi disponibili.


### 4.6. Test delle pere con Keet


Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.


```bash
pear run pear://keet
```


Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza utilizzare un server centrale. Se Keet viene lanciato con successo, significa che l'installazione di Pears è perfettamente funzionante.


Il sistema macOS è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.


## 5. Come utilizzare l'Accademia Plan ₿ sulle pere


Una volta che Pears è installato e funzionante, è possibile lanciare direttamente la piattaforma **Plan ₿ Academy** attraverso la rete P2P. È sufficiente eseguire il seguente comando nel terminale (lo stesso comando funziona su Linux, Windows e macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Una volta completato il caricamento, Plan ₿ Academy si aprirà all'interno del vostro ambiente Pears, pronto per essere utilizzato proprio come il sito web originale, ma senza dipendere da un server centrale.


![Image](assets/fr/14.webp)


## 6. Come seminare la pianta ₿ Accademia delle pere


Nella rete Pears, *seed* un'applicazione significa ridistribuirla ad altri peer dal proprio computer. In pratica, quando si seed Plan ₿ Academy, il proprio computer diventa una fonte di dati che permette agli altri utenti di scaricare l'applicazione senza fare affidamento su un server centrale.


Questo meccanismo rafforza la resilienza e la resistenza alla censura della nostra applicazione sulla rete Pears. Più peer seed un'applicazione, più diventa disponibile e decentralizzata, anche se alcuni nodi originali vanno offline.


Per contribuire alla distribuzione di Plan ₿ Academy, è sufficiente eseguire il seguente comando:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Finché questo comando rimane attivo, il dispositivo partecipa alla distribuzione dei file dell'applicazione. Se si chiude il terminale, il processo di condivisione si interrompe.


Per continuare la semina dopo un riavvio, è possibile eseguire il comando in background o creare un servizio di sistema, ad esempio un servizio systemd su Linux, un LaunchAgent su macOS o un'attività pianificata su Windows. Questi metodi garantiscono che l'applicazione Plan ₿ Academy riprenda automaticamente la semina all'avvio del sistema.


Grazie per aver contribuito alla distribuzione decentralizzata di Plan ₿ Academy su Pears e per aver contribuito a rendere l'istruzione Bitcoin davvero resistente alla censura!