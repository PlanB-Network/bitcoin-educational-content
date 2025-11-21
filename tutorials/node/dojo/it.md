---
name: Dojo
description: Un nodo Bitcoin open-source per la privacy e l'autonomia
---

![cover](assets/cover.webp)



*Questo tutorial è basato sulla [documentazione ufficiale di Ashigaru](https://ashigaru.rs/docs/), che ho ripreso e ampliato. Ho riscritto tutte le sezioni per migliorarne la chiarezza, ho aggiunto ulteriori spiegazioni dettagliate e illustrazioni per i principianti, per rendere l'installazione e l'uso più facili da capire.*



---

Dojo è un programma open source progettato per fungere da server backend per alcuni portafogli Bitcoin orientati alla privacy, basati su un nodo Bitcoin core. Storicamente, è stato sviluppato per lavorare con Samourai Wallet, un Wallet mobile che offriva funzioni avanzate di privacy come Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet è stato chiuso in seguito all'arresto dei suoi sviluppatori, ma il suo successore comunitario, **Ashigaru Wallet**, ha preso il sopravvento e continua a fare affidamento su Dojo per offrire un'esperienza completa agli utenti che desiderano mantenere il controllo dei propri dati quando utilizzano Bitcoin.



![Image](assets/fr/01.webp)



In pratica, Dojo agisce come un gateway tra il Wallet e la rete Bitcoin. Senza Dojo, un Wallet mobile leggero dovrebbe interrogare server di terze parti per ottenere lo stato dei vostri UTXO e la vostra cronologia, o per trasmettere le vostre transazioni. Ciò implica la dipendenza e la fuga di dati sensibili verso un server di terze parti (indirizzi utilizzati, importi, frequenza di pagamento, ecc.). Con Dojo, questo server è ospitato da voi stessi, direttamente collegato al vostro nodo Bitcoin. In questo modo, tutte le vostre richieste di portafoglio vengono gestite da un server di terze parti. In questo modo, tutte le richieste di portafoglio passano attraverso un'infrastruttura che voi controllate, senza intermediari, rafforzando la vostra riservatezza e sovranità.



## Requisiti per la creazione di un Dojo



La creazione di un server Dojo non richiede una macchina ultra potente. Chiunque abbia un computer di base, una connessione Internet stabile e la possibilità di lasciarlo acceso ininterrottamente (24 ore su 24, 7 giorni su 7) può creare un Dojo funzionante.



### Scegliere il tipo di macchina



È possibile utilizzare :




- un computer portatile ;
- un computer desktop ;
- un mini-PC (ad esempio Intel NUC, Lenovo Thincentre Tiny...).



Ogni opzione presenta vantaggi e svantaggi:




- Prezzo: un mini-PC o un desktop ricondizionato è spesso più economico di un laptop nuovo.
- Ingombro: un Mini-PC occupa meno spazio.
- Supply: un computer portatile ha il vantaggio di avere una batteria, il che significa che non si spegnerà in caso di interruzione di corrente, a differenza di un mini-PC.
- Aggiornabilità: in genere i barboni consentono di aggiungere memoria o di sostituire facilmente un disco Hard.



Per maggiori informazioni sulla scelta dell'attrezzatura, vi consiglio di seguire questo corso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Attrezzatura consigliata



Non è necessario acquistare una macchina nuova. Un computer ricondizionato con le specifiche riportate di seguito offrirà prestazioni molto migliori rispetto all'elettronica su scheda singola (come il Raspberry Pi).



**Specifiche minime:**




- Architettura X86-64 (processore a 64 bit).
- processore dual-core da 2 GHz o più veloce.
- 8 GB di RAM minimo.
- 2 TB o più di SSD NVMe (per memorizzare Blockchain di Bitcoin e gli indici necessari).



**Sistema operativo consigliato: **




- Una distribuzione basata su Debian, come Ubuntu 24.04 LTS.



**Attrezzatura consigliata:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- ecc.



È perfettamente possibile eseguire un server Dojo su altre configurazioni hardware. Tuttavia, per ottenere le migliori prestazioni e limitare i problemi, si consiglia di seguire le raccomandazioni di cui sopra.



In questa esercitazione utilizzerò un vecchio ThinkCentre Tiny con processore Intel Pentium Dual-Core G4400T, 8 GB di RAM e un'unità SSD da 2 TB.



## 1 - Installazione di Ubuntu



*Se si desidera installare Dojo su un dispositivo già configurato, è possibile saltare questo passaggio e passare direttamente al punto 2.*



Dopo aver preparato l'hardware scelto, è il momento di installare un sistema operativo. È possibile utilizzare praticamente qualsiasi distribuzione Debian, ma vi consiglio di optare per una versione LTS di Ubuntu, poiché è perfettamente adatta ai nostri scopi. Ecco i passi da seguire:



### 1.1. creare una chiave USB avviabile



Da un computer già funzionante (la vostra macchina abituale), scaricate l'immagine ISO di Ubuntu LTS [dal sito ufficiale](https://ubuntu.com/download/desktop) (`24.04` al momento in cui scriviamo, ma prendete la più recente se ne è disponibile un'altra).



![Image](assets/fr/02.webp)



Inserire una chiave USB di almeno 8 GB nel computer, quindi creare una chiave avviabile utilizzando un software come [Balena Etcher](https://etcher.balena.io/). Selezionate l'immagine ISO di Ubuntu appena scaricata, scegliete la chiave USB come dispositivo di destinazione e avviate il processo di creazione (siate pazienti, potrebbe richiedere diversi minuti).



![Image](assets/fr/03.webp)



Inserire la chiave USB avviabile nel computer spento (quello su cui si vuole eseguire Dojo). Avviare il computer e premere immediatamente **F12** o **F10** sulla tastiera (a seconda del modello) per accedere al menu di avvio. Scegliere quindi la chiave USB come dispositivo prioritario nell'ordine di avvio del computer.



![Image](assets/fr/04.webp)



### 1.2. installare il sistema operativo



Appare la schermata iniziale di Ubuntu. Selezionate "Prova o installa Ubuntu*".



![Image](assets/fr/05.webp)



Seguite quindi il classico processo di installazione di Ubuntu:




- Selezionare la lingua.
- Selezionare il tipo di tastiera.
- Se la connessione avviene tramite cavo RJ45, non è necessario configurare il Wi-Fi.
- Fate clic su "*Installa Ubuntu*" e selezionate l'opzione per installare software di terze parti (driver Wi-Fi, codec multimediali, ecc.).
- Quando la procedura guidata chiede il tipo di installazione, selezionate "*Cancella il disco e installa Ubuntu*". **Attenzione**: questa operazione cancellerà completamente il contenuto del disco. Controllare attentamente che il disco scelto corrisponda all'unità SSD NVMe destinata a Dojo.
- Creare un nome utente semplice (ad esempio "*loic*").
- Assegnare un nome alla macchina (ad esempio "*dojo-node*").
- Impostate una password forte e tenetela al sicuro.
- Attivare l'opzione "*Richiedere la mia password per accedere*" per rafforzare la sicurezza.
- Indicate il vostro fuso orario, quindi fate clic su "*Installa*".
- Attendere il completamento dell'installazione. Al termine, il sistema si riavvia automaticamente.
- Rimuovere la chiave di installazione USB al riavvio del computer.



Per maggiori dettagli sul processo di installazione di Ubuntu, consultate il nostro tutorial dedicato:



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. aggiornamento del sistema



Dopo il primo avvio, aprire un terminale utilizzando la combinazione di tasti ***Ctrl + Alt + T*** ed eseguire i seguenti comandi per aggiornare il sistema:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Installazione di un edificio esterno



Affinché Dojo funzioni correttamente, sul sistema devono essere presenti alcuni mattoni software. Questi sono utilizzati per gestire i repository software, la comunicazione, la decompressione degli archivi e l'esecuzione di Dojo all'interno dei contenitori Docker. Tutte queste operazioni vengono eseguite nel terminale.



### 2.1. Preparazione



Il comando seguente riporta alla cartella personale. Questa è una buona pratica prima di eseguire una serie di installazioni.



```bash
cd ~/
```



Prima di installare qualsiasi software, accertatevi che il database dei software disponibili sul vostro computer sia aggiornato. In questo modo si evita di installare versioni obsolete.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. installare le utility



È necessario aggiungere diversi strumenti al sistema:




- `apt-transport-https`: consente di scaricare pacchetti in modo sicuro tramite HTTPS
- `ca-certificates`: gestisce i certificati necessari per le connessioni criptate
- `curl`: per recuperare i file da Internet
- `gnupg-agent`: per la gestione delle chiavi GPG
- software-properties-common`: fornisce utilità per la manipolazione dei repository APT
- `unzip`: decomprime i file in formato ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Durante l'installazione, il sistema potrebbe chiedere una conferma. Premere il tasto "*y*", quindi premere "*Invio*".



![Image](assets/fr/08.webp)



### 2.3. installare Torsocks



Torsocks consente di eseguire alcuni comandi attraverso la rete Tor, migliorando la riservatezza delle comunicazioni.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. installare Docker e Docker Compose



Dojo viene eseguito all'interno di container Docker. Ciò significa che ogni servizio è isolato in un ambiente indipendente, semplificando la manutenzione e la sicurezza. A tal fine, è necessario installare Docker e lo strumento Docker Compose, che consente di gestire più contenitori contemporaneamente.



#### Aggiungere la chiave di firma Docker



Docker fornisce la propria chiave di firma digitale. Aggiungendola si verifica l'autenticità dei pacchetti scaricati.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Aggiunto il repository Docker ufficiale



Successivamente, è necessario indicare al sistema dove trovare i pacchetti Docker ufficiali. Questo comando aggiunge un nuovo repository alla configurazione del gestore di pacchetti.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Installazione di Docker e Docker Compose



A questo punto è possibile installare i componenti principali di Docker.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Autorizzazione dell'utente



Per impostazione predefinita, solo i comandi eseguiti con i diritti di amministratore possono lanciare Docker. Per maggiore comodità, consiglio di aggiungere l'utente corrente al gruppo "*docker*". Questo permette di usare Docker senza dover digitare ogni volta `sudo`.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Creazione di un singolo utente (opzionale)



Se volete migliorare la sicurezza del vostro sistema, vi consiglio di creare un utente separato esclusivamente per l'esecuzione di Dojo. Questa separazione limita i rischi: se un problema di sicurezza si verifica in Dojo, non comprometterà direttamente il vostro account principale.



### 3.1. creazione dell'account utente



Il comando seguente crea un nuovo utente chiamato "*dojo*". Questo utente avrà una home directory `/home/dojo` e l'accesso al terminale bash. Sarà anche aggiunto al gruppo sudo per consentire l'esecuzione di comandi di amministrazione.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Impostazione di una password



È importante assegnare una password forte a questo account. L'ideale sarebbe utilizzare un gestore di password come Bitwarden per generate una combinazione lunga e difficile da indovinare.



```bash
sudo passwd dojo
```



Il sistema chiederà quindi di inserire la password scelta e di confermarla una seconda volta.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autorizzare l'utente a usare Docker



Per consentire all'utente "*dojo*" di lanciare i contenitori necessari all'esecuzione di Dojo, è necessario aggiungerlo al gruppo Docker. Questo evita di dover far precedere ogni comando da `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Riavvio del sistema



Affinché le modifiche al gruppo abbiano effetto, è necessario riavviare la macchina.



```bash
sudo reboot
```



### 3.5. Accesso con il nuovo utente



Al riavvio del sistema, accedere con il login ***dojo*** e la password definita in precedenza. Tutti i passaggi successivi devono essere eseguiti da questo account dedicato.



## 4. Scaricare e controllare Dojo



Prima di installare Dojo, è essenziale assicurarsi che i file provengano dallo sviluppatore ufficiale e che non siano stati modificati. Questo passaggio si basa sull'uso di PGP e hash per verificare l'autenticità e l'integrità dei file.



### 4.1. importare la chiave PGP dello sviluppatore



Scaricare la chiave pubblica dello sviluppatore tramite Tor e importarla nel proprio portachiavi locale. Questa chiave verrà utilizzata per verificare le firme associate ai file Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. scaricare l'ultima versione di Dojo



Recuperare l'archivio compresso contenente il codice sorgente di Dojo. In questo esempio, la versione più recente è la `1.27.0`: modificare il comando secondo [l'ultima versione qui sul repository ufficiale di GitHub] (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Scaricare le impronte digitali e la firma



Gli sviluppatori pubblicano un file che elenca le impronte digitali degli archivi e un file firmato dalla loro chiave PGP. Scaricateli per confrontare i vostri file in locale.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Controllare la firma PGP



Verificare che il file delle impronte digitali sia stato firmato dalla chiave importata.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Un risultato corretto mostra una firma valida con la chiave `E53AD419B242822F19E23C6D3033D463D6E544F6` e il Address associato `dojocoder@pm.me`. Potrebbe apparire un avviso che indica che la chiave non è certificata: è possibile ignorarlo.



Se invece la firma non è valida, interrompere immediatamente il processo di installazione e ricominciare dall'inizio.



![Image](assets/fr/17.webp)



### 4.5. Controllare l'integrità dell'archivio



Calcolare l'impronta digitale SHA256 del file scaricato, quindi aprire il file dell'impronta digitale per confrontare i due valori.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Se le due impronte digitali sono identiche, si può essere certi che l'archivio non è stato modificato. Se invece sono diverse, non si deve andare oltre ed eliminare i file.



![Image](assets/fr/18.webp)



### 4.6. Estrarre e organizzare i file



Una volta completata la verifica, è possibile decomprimere l'archivio e preparare una cartella dedicata all'installazione di Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Pulire i file non necessari



Eliminare i file temporanei e gli archivi non più necessari per mantenere pulito l'ambiente.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Configurazione di Dojo



Dojo è un server di backend che riunisce diversi servizi per interagire con il portafoglio e gestire il nodo Bitcoin. La sua configurazione può essere complessa, ma il progetto offre un metodo semplificato che installa e configura automaticamente i seguenti componenti: il nodo Bitcoin. La sua configurazione può essere complessa, ma il progetto offre un metodo semplificato che installa e configura automaticamente i seguenti componenti:




- Dojo (API principale)
- Bitcoin core (nodo completo Bitcoin)
- Esploratore BTC-RPC (web Block explorer)
- Fulcrum Indexer (indicizzazione rapida di blocchi e transazioni)
- Server Fulcrum Electrum disponibile sulla rete Tor
- Fulcrum Electrum Server disponibile sulla rete locale
- Credenziali di amministrazione



### 5.1. credenziali di amministrazione



Per garantire l'accesso ai vari servizi, è necessario che il generate fornisca diversi identificatori unici:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- cHIAVE_NODO_ADMIN
- `NODO_JWT_SECRET`



Questi identificativi **devono essere unici** (questo è molto importante: non si deve usare la stessa password per più servizi), composti esclusivamente da numeri, lettere maiuscole e minuscole (alfanumerici) e lunghi circa 40 caratteri per garantire un alto livello di sicurezza. Ancora una volta, consiglio vivamente di utilizzare un gestore di password.



### 5.2. Accesso ai file di configurazione



I file di configurazione di Dojo si trovano nella cartella `conf/`. Spostarsi in questa cartella:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Configurazione del Bitcoin core



Aprire il file di configurazione di Bitcoin core con l'editor di testo nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



In questo file, inserire gli identificatori generati:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Sostituite `il vostro ID-qui` e `la vostra password-qui` con i vostri login (con una password forte).***



Si può anche regolare la dimensione della memoria cache usata da Bitcoin core per migliorare le prestazioni (se si dispone di molta RAM, se ne può usare di più):



```
BITCOIND_DB_CACHE=2048
```



Per salvare le modifiche e chiudere l'editor :




- premere `Ctrl + X
- tipo `y`
- quindi premere "*Invio*"



### 5.4. Configurazione di MySQL



Quindi aprire la configurazione del database MySQL:



```bash
nano docker-mysql.conf.tpl
```



Inserire i dati di accesso:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Sostituite `il vostro ID-qui` e `la vostra password-qui` con i vostri login (con password forti e uniche).***



Salvare allo stesso modo (`Ctrl + X`, `y`, "*Invio*").



![Image](assets/fr/23.webp)



### 5.5. Configurazione dell'indicizzatore Fulcrum



Aprire il seguente file:



```bash
nano docker-indexer.conf.tpl
```



Aggiungere i parametri per attivare Fulcrum e integrarlo correttamente in Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Ci sono poi due possibilità, a seconda della configurazione. Se Dojo è installato su una macchina separata dal computer di tutti i giorni (su una macchina dedicata, un server...), inserire il suo IP Address nella rete locale, ad esempio :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Per conoscere l'IP Address locale della macchina, aprire un altro terminale e inserire il seguente comando:



```bash
hostname -I
```



Seconda possibilità: se Dojo viene eseguito direttamente sul computer di tutti i giorni, mantenere il valore predefinito già presente nel file di configurazione :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Salvare e uscire dall'editor (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Configurazione del servizio del nodo



Infine, aprire la configurazione del servizio Dojo principale:



```bash
nano docker-node.conf.tpl
```



Inserire i dati di accesso:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Sostituire la `tua-password-qui` con le proprie credenziali (con password forti e uniche).***



![Image](assets/fr/26.webp)



Quindi attivare l'indicizzatore locale:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Salvare e uscire dall'editor (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Gestione degli accessi



Una volta completata la configurazione, non è necessario salvare tutti gli identificatori generati. L'unico che deve essere assolutamente salvato è :



```
NODE_ADMIN_KEY
```



Questo login vi consentirà di accedere successivamente allo strumento di manutenzione Dojo. Tutti gli altri login possono essere rimossi dal proprio gestore di password o da appunti scritti a mano. Rimangono accessibili dai file di configurazione di Dojo, nel caso in cui sia necessario recuperarli in futuro.



## 6. Installazione del Dojo



In questa fase, Dojo verrà installato e avviato sul vostro computer. L'operazione avvierà diversi servizi (Bitcoin core, l'indicizzatore Fulcrum, il backend Dojo, ecc.) e inizierà la sincronizzazione completa del Blockchain Bitcoin. L'operazione può richiedere diversi giorni, a seconda dell'hardware e della connessione Internet. Questa operazione può richiedere diversi giorni, a seconda dell'hardware e della connessione a Internet.



### 6.1. Verificare che Docker funzioni correttamente



Prima di iniziare l'installazione, assicurarsi che Docker sia operativo. Eseguire il seguente comando:



```bash
docker run hello-world
```



Questo comando scarica e lancia un piccolo contenitore di prova. Se tutto funziona correttamente, si dovrebbe vedere un messaggio simile a :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Se questo messaggio non viene visualizzato, riavviare il computer con :



```bash
sudo reboot
```



Quindi accedere nuovamente al proprio account **dojo** ed eseguire nuovamente il comando di prova. Se l'errore persiste, Docker non è stato installato correttamente. In questo caso, tornare al passo `2.4.` sull'installazione di Docker e controllare attentamente ogni comando.



### 6.2. Andare alla directory di installazione di Dojo



Gli script necessari per l'installazione si trovano nella cartella `my-dojo`. Spostarsi in questa cartella:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Usare il comando `ls` per verificare che il file `dojo.sh` sia presente. Questo è lo script principale che automatizza l'installazione di Dojo e l'avvio di tutti i suoi servizi.



![Image](assets/fr/29.webp)



### 6.3. Avviare l'installazione



Avviare l'installazione eseguendo il comando :



```bash
./dojo.sh install
```



Confermare l'installazione premendo `y` e poi "*Invio*".



![Image](assets/fr/30.webp)



Questo script :




- scaricare e lanciare i contenitori Docker necessari,
- inizializzare il Bitcoin core e avviare la sincronizzazione del Blockchain,
- avviare l'indicizzatore Fulcrum per tracciare transazioni e indirizzi,
- attivare il backend Dojo e le sue API.



Vedrete scorrere un flusso costante di log, con riferimenti colorati come `bitcoind`, `soroban`, `nodejs` o `fulcrum`. Questo scorrimento indica che Dojo è attivo e funzionante e sta iniziando a eseguire i vari servizi.



![Image](assets/fr/31.webp)



### 6.4. Uscita dalla visualizzazione del registro



I log appaiono in tempo reale nel terminale. Per tornare al prompt dei comandi mentre Dojo è in esecuzione in background, digitare :



```
Ctrl + C
```



Non preoccupatevi: l'interruzione della visualizzazione dei log non interrompe i servizi. Docker continua a eseguire Dojo in background (ovviamente non è necessario fermare il computer se si vuole che IBD continui).



### 6.5. Comprendere lo *Scarico iniziale del blocco* (IBD)



All'avvio, il Bitcoin core deve scaricare e verificare l'intero Blockchain dal 2009. Questa fase è chiamata ***Initial Block Download* (IBD)**. È essenziale, in quanto consente al nodo Dojo di verificare ogni blocco e transazione Bitcoin in modo indipendente.



La durata di questa sincronizzazione dipende da diversi fattori:




- la potenza del processore e la quantità di memoria RAM disponibile,
- la velocità del disco,
- il numero e la qualità dei peer a cui il nodo si connette,
- la velocità della connessione a Internet.



In pratica, questa operazione richiede generalmente da **2 a 7 giorni**. Durante questo periodo, è possibile lasciare la macchina sempre accesa. Più a lungo la macchina è accesa, più velocemente verrà completata la sincronizzazione. Si consiglia di controllare regolarmente lo stato di sincronizzazione consultando i registri di Bitcoin core o utilizzando lo strumento di manutenzione Dojo una volta installato (vedere la sezione successiva).



Per approfondire la conoscenza dell'IBD e, più in generale, del funzionamento e del ruolo del nodo Bitcoin, vi consiglio di seguire questo corso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Monitoraggio della sincronizzazione



Quando si installa Dojo per la prima volta, è necessario attendere il completamento di due operazioni principali: il download completo del Blockchain Bitcoin (*IBD*) e l'indicizzazione di questo Blockchain da parte di Fulcrum. A seconda della connessione e della potenza della macchina, potrebbero essere necessari alcuni giorni. Durante questo periodo, è possibile monitorare l'avanzamento del processo per assicurarsi che tutto proceda senza intoppi.



Esistono due modi per monitorare lo stato della sincronizzazione:




- l'uso del Dojo Maintenance Tool (o DMT), che è semplice ma fornisce pochi dettagli durante l'IBD;
- consultazione diretta dei log di Dojo sulla vostra macchina, più tecnica ma molto più precisa.



### 7.1. Controllo tramite lo strumento di manutenzione Dojo (DMT)



Lo strumento di manutenzione Dojo è un Interface sicuro, basato sul web, che consente di monitorare lo stato dell'impianto e di eseguire alcune operazioni. È il modo più semplice e accessibile per monitorare i progressi dell'IBD. Durante la fase iniziale di sincronizzazione, le informazioni visualizzate possono essere limitate. Ad esempio, il DMT non mostra il progresso dettagliato dell'indicizzazione Fulcrum. Al contrario, una volta completata la sincronizzazione, il DMT visualizzerà chiaramente :




- tutte le luci del Green;
- l'ultimo blocco convalidato per ogni servizio (Nodo, Indexer, Dojo DB).



Per accedervi, è necessario conoscere l'URL del proprio DMT e connettersi ad esso [tramite il browser Tor] (https://www.torproject.org/download/). Per farlo, aprire un terminale e andare nella cartella `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Eseguite quindi il seguente comando:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Avrete quindi accesso a tutte le informazioni relative alle connessioni al vostro Dojo tramite Tor. Quello che ci interessa qui è il seguente URL:



```
Dojo API and Maintenance Tool =
```



Per accedere al DMT da qualsiasi macchina su qualsiasi rete (anche da remoto), aprire Tor Browser e inserire questo URL seguito da `/admin`. Ad esempio, se il vostro URL è `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, dovrete inserire nella barra [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Si prega di mantenere questo Address strettamente confidenziale



Si verrà quindi reindirizzati a una pagina di autenticazione. Il DMT è connesso utilizzando la password `NODE_ADMIN_KEY` generata in precedenza.



![Image](assets/fr/33.webp)



Una volta effettuato il login, è possibile accedere allo *Strumento di manutenzione Dojo*! Durante l'IBD, è possibile visualizzare le informazioni "*Latest Block*" nel menu "*Full node*", che consente di conoscere lo stato attuale del nodo Bitcoin.



![Image](assets/fr/34.webp)



Ricordate di inserire questo Address nei preferiti di Tor Browser per poterlo recuperare facilmente in seguito.



Una volta che il Dojo è completamente sincronizzato, si dovrebbe vedere il controllo Green ✅ su tutti gli indicatori della pagina iniziale del DMT.



### 7.2. Verifica tramite i log di Dojo



Il secondo modo per seguire l'andamento dell'IBD è quello di consultare direttamente i registri della macchina. Questo approccio offre un monitoraggio molto più preciso e in tempo reale. È possibile vedere come Bitcoin core sta procedendo nel download dei blocchi e come Fulcrum li sta indicizzando.



Collegarsi alla macchina che ospita Dojo e aprire un terminale. Tutti i comandi devono essere eseguiti dalla cartella `my-dojo`. Posizionarsi in questa cartella:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Registri Bitcoin core



Visualizzare i registri Bitcoin core per monitorare i progressi dell'IBD:



```bash
./dojo.sh logs bitcoind
```



All'inizio, si vedrà una fase di pre-sincronizzazione delle intestazioni dei blocchi:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Quando questa cifra raggiunge il 100%, Bitcoin core inizia il download completo di Blockchain. Si vedrà l'avanzamento dell'IBD. Per conoscere l'altezza attuale del blocco, si può guardare il valore indicato da `height=`. Si può anche seguire il tasto `progress=`, che indica la percentuale di avanzamento dell'IBD.



![Image](assets/fr/36.webp)



Come sempre, per chiudere i registri e tornare al prompt dei comandi, utilizzare la combinazione `Ctrl + C`.



#### Tronchi Fulcrum



Una volta che Bitcoin core ha completato la pre-sincronizzazione dell'intestazione, Fulcrum inizia a indicizzare Blockchain man mano che procede. Visualizzare i suoi registri con :



```bash
./dojo.sh logs fulcrum
```



Si vedrà quindi l'altezza dell'ultimo blocco indicizzato, indicata dopo `height:`, e la percentuale di avanzamento dell'indicizzazione.



![Image](assets/fr/37.webp)



### 7.3. Corruzione del database Fulcrum



Fulcrum è un indicizzatore particolarmente potente, ma la sua installazione può essere complessa, anche a causa della delicata gestione del database. In caso di interruzione di corrente o di arresto improvviso della macchina durante la sincronizzazione iniziale, il database dell'indicizzatore può essere danneggiato. È possibile constatarlo, ad esempio, se si dispone dei seguenti log:



```bash
fulcrum | The database has been corrupted etc...
```



**Nota: ** Questo tipo di errore dovrebbe essere corretto con l'imminente rilascio di Fulcrum 2.0.



Se vi succede, non c'è alcun impatto su bitcoind (il vostro nodo Bitcoin): il suo IBD continuerà a progredire indipendentemente da Fulcrum. Tuttavia, non sarete in grado di utilizzare Fulcrum finché non avrete cancellato i dati corrotti e riavviato la sincronizzazione dall'inizio. Ecco come funziona:



Fermare il Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Eliminare solo il contenitore e il volume Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalmente il nome è `my-dojo_data-fulcrum`, se questo non è il vostro caso, adattate il nome restituito dal comando precedente.



Poi rilanciare Dojo e ricostruire Fulcrum da zero:



```bash
./dojo.sh upgrade
```



Si può quindi verificare che Fulcrum funzioni correttamente consultando i log:



```bash
docker logs -f fulcrum
```




## 8. Utilizzo dello strumento di manutenzione Dojo



Una volta che il nodo Bitcoin è sincronizzato con la testa dell'ordito con la maggior parte del Proof of Work e il Blockchain è indicizzato al 100% da Fulcrum, si può iniziare a usare il Dojo.



Il vostro Dojo offre una vasta gamma di funzionalità, regolarmente migliorate ad ogni nuova versione. A mio parere, le due più importanti sono :




- la possibilità di collegare il proprio Ashigaru Wallet per utilizzare il proprio nodo per consultare i dati del Blockchain e trasmettere le proprie transazioni,
- e il Block explorer, che consente di accedere alle informazioni sul Blockchain Bitcoin senza esporre i dati a un'istanza esterna non controllata dall'utente.



Scopriamo come utilizzarli.


### 8.1. Collegare Ashigaru al Dojo



Collegare l'Ashigaru Wallet al Dojo è molto semplice: una volta sul DMT, aprire il menu "*Pairing*". Appare un codice QR, che si può scansionare direttamente con l'applicazione Ashigaru.



![Image](assets/fr/38.webp)



Nell'applicazione Ashigaru, la prima volta che la si avvia dopo aver creato o ripristinato il Wallet, si verrà reindirizzati alla pagina "*Configura il server Dojo*". Premere "*Scansione QR*", quindi scansionare il codice QR visualizzato sul DMT.



![Image](assets/fr/39.webp)



Quindi fare clic sul pulsante "*Continua*".



![Image](assets/fr/40.webp)



Ora siete collegati al vostro Dojo.



![Image](assets/fr/41.webp)



### 8.2. Utilizzo del Block explorer



Dojo installa automaticamente un Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), che attinge direttamente ai dati del vostro nodo Bitcoin. L'explorer consente di accedere alle informazioni grezze del Blockchain e del proprio Mempool attraverso un web Interface di facile comprensione. È quindi possibile, ad esempio, controllare lo stato di una transazione in corso, visualizzare il saldo di un Address o esaminare la composizione di un blocco con facilità.



Per accedervi, è sufficiente recuperare il Tor Address dal browser. A tal fine, eseguire lo stesso comando utilizzato per ottenere il Address del DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Avrete accesso a tutte le informazioni sulla vostra connessione a Dojo tramite Tor. Quello che ci interessa qui è il seguente URL:



```
Block Explorer =
```



Se siete già connessi al DMT, potete trovare questo Address anche nel menu "*Pairing*", all'interno del JSON di connessione:



![Image](assets/fr/43.webp)



Per accedere al browser da qualsiasi macchina su qualsiasi rete (anche da remoto), aprire [Tor Browser](https://www.torproject.org/download/) e inserire l'URL appena recuperato.



⚠️ **Si prega di mantenere strettamente riservato questo Address



Avrete quindi accesso al vostro Block explorer.



![Image](assets/fr/44.webp)



*Credito d'immagine: https://ashigaru.rs/.*



Per rintracciare una transazione, è sufficiente inserire il suo txid nella barra di ricerca in alto a destra.



![Image](assets/fr/45.webp)



*Credito d'immagine: https://ashigaru.rs/.*



Per verificare i movimenti associati a un Address, procedere allo stesso modo inserendo il Address nella barra di ricerca.



![Image](assets/fr/46.webp)



*Credito d'immagine: https://ashigaru.rs/.*



È inoltre possibile inserire il Hash o l'altezza di un blocco nella barra di ricerca per visualizzarne i dettagli.



![Image](assets/fr/47.webp)



*Credito d'immagine: https://ashigaru.rs/.*



## 9. Manutenzione del dojo



### 9.1 Fermate il vostro Dojo



Non interrompere mai bruscamente l'alimentazione di Dojo, perché ciò potrebbe danneggiare alcuni database, in particolare l'indicizzatore Fulcrum. Se dovete spegnerlo, eseguite sempre uno spegnimento pulito di Dojo e, una volta completate tutte le procedure, spegnete anche la macchina:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Aggiornare il Dojo



Dojo si evolve regolarmente e vengono rilasciate nuove versioni per correggere bug, migliorare la stabilità e aggiungere funzionalità. È quindi importante [controllare regolarmente gli aggiornamenti](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) e aggiornare Dojo. Il processo è simile a quello dell'installazione iniziale, ma richiede la sostituzione di alcuni file con l'ultima versione disponibile, mantenendo la propria configurazione. Ecco i passi dettagliati da seguire per un aggiornamento pulito e sicuro:



Per conoscere la versione attuale di Dojo, eseguire il comando :



```bash
./dojo.sh version
```



Anche se questo passaggio è facoltativo, vi consiglio di iniziare aggiornando il vostro sistema operativo. Questo riduce il rischio di incompatibilità e garantisce che le dipendenze utilizzate da Dojo siano aggiornate:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Andare nella directory Dojo e arrestare i servizi correnti:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Quindi riavviare il sistema per fare tabula rasa:



```bash
sudo reboot
```



Dojo viene fornito con file firmati digitalmente. Queste firme PGP garantiscono che i file provengono dallo sviluppatore e non sono stati alterati in alcun modo. È importante controllarle ogni volta che si aggiorna Dojo, proprio come si è fatto alla prima installazione. Iniziare scaricando la chiave pubblica dello sviluppatore tramite Tor, quindi importarla:



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Tornare alla rubrica personale:



```bash
cd ~/
```



Scaricare l'ultima versione di Dojo da GitHub via Tor. In questo esempio, si tratta della versione `1.28.0` (che non esiste ancora al momento in cui scriviamo: è solo per dare un esempio). Ricordarsi di sostituire il file e il link [con la versione che si desidera installare](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Scaricate anche il file contenente le impronte digitali e la firma PGP (ancora una volta, ricordatevi di regolare la versione nel comando):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Verificare che il file di impronte digitali scaricato sia stato firmato dalla chiave dello sviluppatore:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Un risultato corretto dovrebbe visualizzare :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Potrebbe apparire un avviso che la chiave non è certificata, ma non è importante. Se invece la firma non è valida o corrisponde a un'altra chiave, non bisogna andare oltre e ricominciare da capo, controllando i collegamenti.



Calcolare quindi l'impronta digitale SHA256 dell'archivio e confrontarla con il file dell'impronta digitale ufficiale:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Se le due impronte digitali corrispondono perfettamente, l'archivio è autentico e intatto. Se differiscono, eliminare immediatamente i file e non continuare.



Decomprimere l'archivio nella propria home directory:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Quindi copiate il contenuto nella cartella Dojo, sovrascrivendo il vecchio file :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Questa operazione mantiene i file di configurazione che si trovano in `~/dojo-app/docker/my-dojo/conf`, ma sostituisce tutti gli altri file con le versioni aggiornate.



Per mantenere pulito l'ambiente, eliminare i file non necessari:



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Tornare alla cartella degli script di Dojo ed eseguire il comando update:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Questo comando indica a Docker di ricostruire le immagini con i nuovi file e di riavviare automaticamente tutti i servizi. Alla fine del processo, controllare i log per verificare che Bitcoin core, Fulcrum e Dojo funzionino correttamente:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Se i servizi si avviano senza errori e i log mostrano l'elaborazione di blocchi, il vostro Dojo è ora aggiornato e operativo.