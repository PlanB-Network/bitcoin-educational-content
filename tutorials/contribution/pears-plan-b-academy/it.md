---
name: Mappa ₿ Accademia - Pears App
description: Come si installa e si utilizza l'applicazione Plan ₿ Academy su Pears?
---

![cover](assets/cover.webp)



Come probabilmente saprete, Plan ₿ Academy è il più grande database didattico dedicato a Bitcoin, che riunisce corsi, tutorial e migliaia di risorse pubblicate sotto licenza aperta. Originariamente, Plan ₿ Academy era un sito web. Ma cosa succederebbe se non fosse più possibile accedervi normalmente, ad esempio in caso di censura?



In questo tutorial, impareremo a far funzionare la piattaforma **Plan ₿ Academy** in modo davvero incensurabile grazie a **Pears**, una tecnologia peer-to-peer (P2P) sviluppata da **Holepunch** e supportata da **Tether**.



Pears è il software che ci permetterà di gestire la piattaforma Plan ₿ Academy senza affidarci a un sito web centralizzato. In questo tutorial, installeremo Pears sul vostro computer per accedere a Plan ₿ Academy tramite Pears.



L'obiettivo di Pears è semplice: rendere possibile la distribuzione e l'utilizzo di applicazioni web senza fare affidamento su alcuna infrastruttura centralizzata (nessun server, nessun host, nessun intermediario). In altre parole, anche se un cloud provider chiude o un Paese blocca un dominio, l'applicazione continua a vivere tra i peer della rete. È questo approccio che consente alla nostra piattaforma educativa Plan ₿ Academy di rimanere accessibile ovunque nel mondo, senza un singolo punto di guasto.



---

**TL;DR :**





- Installare le pere ;





- Eseguire il seguente comando per avviare l'applicazione Plan ₿ Academy:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Installare le pere



### 1.1 Che cos'è la pera?



Pears è un ambiente runtime, uno strumento di sviluppo e una piattaforma di distribuzione per applicazioni peer-to-peer. Questo strumento open-source permette di costruire, condividere ed eseguire software senza server o infrastrutture, direttamente tra utenti. In concreto, ciò significa che invece di ospitare un'applicazione su un server centrale, ogni utente diventa un nodo della rete, condividendo parte dell'applicazione e dei dati con altri peer. L'intero sistema forma una rete distribuita, con ogni istanza che coopera per mantenere il servizio accessibile.



![Image](assets/fr/01.webp)



Questo approccio si basa su una serie di mattoni software modulari sviluppati da Holepunch:




- Hypercore**: un registro distribuito che garantisce la coerenza e la sicurezza dei dati senza un database centrale.
- Hyperbee**: un indicizzatore in cima a Hypercore, per un'organizzazione e una navigazione efficiente dei dati.
- Hyperdrive**: un file system distribuito utilizzato per archiviare e sincronizzare i file delle applicazioni tra peer.
- Hyperswarm** e **HyperDHT**: livelli di rete che consentono la scoperta e la connessione tra peer in tutto il mondo, senza un server centrale.
- Secretstream**: un protocollo di crittografia E2E per proteggere gli scambi tra due peer.



Combinando questi componenti, Pears consente di creare applicazioni autonome, crittografate e distribuite, in cui ogni utente partecipa attivamente alla rete. Questa architettura decentralizzata elimina i costi di infrastruttura, i rischi di censura e gli SPOF (*Single Point of Failure*).



Pears è sviluppato da Holepunch, una società fondata da Mathias Buus e Paolo Ardoino (CEO di Tether e CTO di Bitfinex), con la missione di estendere la logica peer-to-peer oltre il Bitcoin. La loro ambizione è quella di costruire il "Peer-to-Peer Internet", dove ogni applicazione può essere eseguita senza autorizzazione, senza server e senza intermediari. La loro ambizione è quella di costruire il "Peer-to-Peer Internet", dove ogni applicazione può essere eseguita senza autorizzazione, senza server e senza intermediari. Holepunch è già alla base di **Keet**, un'applicazione di videoconferenza e messaggistica completamente P2P.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Questa guida all'installazione di Pears è suddivisa in diverse sezioni a seconda del sistema operativo in uso. Passate direttamente alla sezione corrispondente al vostro ambiente per seguire le istruzioni appropriate :*




- Linux (Debian)** → Parte **1.2.**
- Windows** → Parte **1.3.**
- macOS** → Parte **1.4.**




### 1.2 - Come si installa Pears su Linux (Debian)?



L'installazione di Pears su un sistema Debian è relativamente semplice, ma richiede alcuni prerequisiti, che spiegheremo in dettaglio in questa sezione.



#### 1.2.1. Aggiornamento del sistema



Innanzitutto, è importante assicurarsi che il sistema sia aggiornato.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Installazione delle dipendenze



Pears si basa su alcune librerie di sistema, tra cui `libatomic1`, utilizzata dal runtime Bare JavaScript. Installatela con il seguente comando:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Installazione di Node.js e npm tramite NVM



Pears è distribuito tramite *npm*, il gestore di pacchetti *Node.js*. Sebbene Pears non dipenda direttamente da *Node.js* per funzionare, è necessario per l'installazione. Il metodo consigliato per l'installazione di *Node.js* su Linux è *NVM* (*Node Version Manager*), che consente di gestire diverse versioni di Node in parallelo.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Quindi ricaricare il terminale per attivare *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Verificare che *NVM* sia installato:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Quindi installare una versione stabile di *Node.js* (ad esempio l'attuale LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Controllare le installazioni di *Node.js* e *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Installare Pears con npm



Una volta che *npm* è disponibile, è possibile installare Pears CLI a livello globale sul proprio sistema. Questo vi permetterà di eseguire il comando `pear` da qualsiasi directory.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Inizializzare le pere



Dopo l'installazione, è sufficiente eseguire il seguente comando nel terminale:



```bash
pear
```



Al primo avvio, Pears si connette alla rete peer-to-peer per scaricare i componenti necessari. Questo processo non richiede un server centrale: i file vengono ottenuti direttamente da altri peer.



![Image](assets/fr/10.webp)



Una volta completato il download, eseguire nuovamente il comando per verificare che tutto funzioni:



```bash
pear
```



![Image](assets/fr/11.webp)



Se tutto è stato installato correttamente, verrà visualizzata la Guida di Pears con un elenco dei comandi disponibili.



#### 1.2.6. Test sulle pere con Keet



Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.



```bash
pear run pear://keet
```



Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza passare per un server centrale. Se Keet viene lanciato correttamente, l'installazione di Pears è perfettamente funzionante.



![Image](assets/fr/12.webp)



Il vostro sistema Linux è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.



### 1.3 - Come si installa Pears su Windows?



L'installazione di Pears su Windows è altrettanto facile che su Linux, ma richiede alcuni strumenti speciali.



*Se si utilizza Linux e si è già installato Pears, si può passare direttamente al punto 2



#### 1.3.1. Aprire PowerShell in modalità amministratore



Prima di tutto, eseguire PowerShell con i diritti di amministratore:




- Fare clic sul menu Start;
- Digitare PowerShell ;
- Cliccate con il tasto destro del mouse su "*Windows PowerShell*" ;
- Selezionare "*Esegui come amministratore*".



![Image](assets/fr/15.webp)



#### 1.3.2. Scarica NVS



Pears viene installato tramite *npm*, il gestore di pacchetti *Node.js*. Su Windows, il metodo raccomandato da Holepunch è di usare *NVS* (*Node Version Switcher*), che è più stabile di *NVM* su questo sistema.



In PowerShell, eseguire il seguente comando per installare l'ultima versione di *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Installazione di Node.js



Dopo l'installazione, riavviare PowerShell e immettere il seguente comando:



```powershell
nvs
```



Si dovrebbe vedere un elenco delle versioni di *Node.js* disponibili. Selezionare la prima premendo il tasto `a` sulla tastiera.



![Image](assets/fr/17.webp)



*Node.js* è installato.



![Image](assets/fr/18.webp)



#### 1.3.4. Verifica delle installazioni



Assicurarsi che *Node.js* e *npm* siano accessibili:



```powershell
node -v
npm -v
```



Entrambi i comandi devono restituire un numero di versione.



![Image](assets/fr/19.webp)



#### 1.3.5. Installare Pears con npm



Una volta che *Node.js* e *npm* sono disponibili, installare **Pears CLI** a livello globale sul sistema:



```powershell
npm install -g pear
```



Questo installerà il binario `pear` nella cartella globale *npm*.



![Image](assets/fr/20.webp)



#### 1.3.6. Controllo e inizializzazione di Pears



Una volta completata l'installazione, eseguire :



```powershell
pear
```



Al primo avvio, Pears scaricherà automaticamente i componenti necessari dalla rete peer-to-peer. Questo processo può richiedere alcuni istanti.



![Image](assets/fr/21.webp)



Se tutto è andato bene, dovrebbe apparire la schermata di aiuto di CLI Pears con un elenco dei sottocomandi disponibili (run, seed, info...).



#### 1.3.7. Test sulle pere con Keet



Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.



```bash
pear run pear://keet
```



Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza passare per un server centrale. Se Keet viene lanciato correttamente, l'installazione di Pears è perfettamente funzionante.



![Image](assets/fr/22.webp)



Il vostro sistema Windows è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.



### 1.4. Come installare Pears su macOS?



L'installazione di Pears su macOS è simile a quella su Linux, ma richiede alcune modifiche specifiche per l'ambiente Apple. Scopriamo insieme questi passaggi.



*Se si utilizza Linux o Windows e si è già installato Pears, si può passare direttamente al punto 2



#### 1.4.1. Verifica dei requisiti di sistema



Prima dell'installazione, assicurarsi che *Xcode Command Line Tools* sia presente sul sistema. Questo pacchetto fornisce gli strumenti di compilazione necessari per _Node.js_ e le sue dipendenze.



Per farlo, aprire un terminale con la scorciatoia da tastiera `Cmd + Barra spaziatrice`, quindi digitare `Terminal` e premere il tasto `Invio`. È quindi possibile inserire questo comando nel terminale per avviare l'installazione:



```bash
xcode-select --install
```



Se gli strumenti sono già installati sul sistema, macOS vi informerà.



#### 1.4.2. Installazione della NVM



Pears è distribuito tramite *npm*, il gestore di pacchetti *Node.js*. Sebbene Pears non dipenda direttamente da *Node.js* per funzionare, è necessario per l'installazione. Il metodo consigliato per l'installazione di *Node.js* su macOS è *NVM* (*Node Version Manager*), che consente di gestire diverse versioni di Node in parallelo.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Quindi ricaricare il terminale per attivare *NVM* :



```bash
source ~/.zshrc
```



Se si usa *bash* piuttosto che *zsh*, eseguire :



```bash
source ~/.bashrc
```



Quindi verificare che *NVM* sia installato:



```bash
nvm --version
```



Il terminale dovrebbe restituire la versione di *NVM* installata sul sistema.



#### 1.4.3 Installazione di Node.js e npm



Quindi installare una versione stabile di *Node.js* (ad esempio l'attuale LTS):



```bash
nvm install --lts
```



Una volta completata l'installazione, verificare le versioni installate:



```bash
node -v
npm -v
```



Entrambi i comandi devono restituire un numero di versione.



#### 1.4.4 Installazione di Pears con npm



Una volta che *npm* è disponibile, è possibile installare Pears CLI a livello globale sul proprio sistema. Questo vi permetterà di eseguire il comando `pear` da qualsiasi directory.



```bash
npm install -g pear
```



#### 1.4.5. Inizializzare le pere



Dopo l'installazione, è sufficiente eseguire il seguente comando nel terminale:



```bash
pear
```



Al primo avvio, Pears si connette alla rete peer-to-peer per scaricare i componenti necessari. Questo processo non richiede un server centrale: i file vengono ottenuti direttamente da altri peer.



Una volta completato il download, eseguire nuovamente il comando per verificare che tutto funzioni:



```bash
pear
```



Se tutto è stato installato correttamente, verrà visualizzata la Guida di Pears con un elenco dei comandi disponibili.



#### 1.4.6. Test sulle pere con Keet



Per verificare che Pears sia pienamente operativo, è possibile lanciare un'applicazione P2P già disponibile sulla rete, come Keet, il software di messaggistica e videoconferenza open-source di Holepunch.



```bash
pear run pear://keet
```



Questo comando carica l'applicazione Keet direttamente dalla rete Pears, senza passare per un server centrale. Se Keet viene lanciato correttamente, l'installazione di Pears è perfettamente funzionante.



Il sistema macOS è ora pronto per eseguire e ospitare applicazioni peer-to-peer con Pears.



## 2. Come si usa Plan ₿ Academy sulle pere?



Una volta che Pears è installato e funzionante, è possibile eseguire direttamente la piattaforma **Plan ₿ Academy** tramite la rete P2P. È sufficiente eseguire il seguente comando nel terminale (è lo stesso comando per Linux, Windows e macOS):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Una volta caricato, Plan ₿ Academy si aprirà nel vostro ambiente Pears, pronto per essere utilizzato come sul sito web originale, ma senza dipendere da un server centrale.



![Image](assets/fr/14.webp)