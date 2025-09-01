---
name: Graylog
description: Centralizzare e analizzare facilmente i registri
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## Distribuzione di Graylog su Debian 12



### I. Presentazione



Graylog è una soluzione open source di "log sink" progettata per centralizzare, archiviare e analizzare i log delle macchine e dei dispositivi di rete in tempo reale. In questo tutorial impareremo a installare la versione gratuita di Graylog su una macchina Debian 12!



All'interno di un sistema informatico, ogni **server**, sia esso in esecuzione **Linux** o **Windows**, e ogni **dispositivo di rete** (switch, router, firewall, ecc.) **genera i propri log**, memorizzati localmente. Con i registri memorizzati localmente su ogni macchina, l'analisi e la correlazione degli eventi è molto difficile... È qui che entra in gioco **Graylog**. Agisce come un **sensore di log**, il che significa che **tutti i computer gli invieranno i loro log** (ad esempio tramite syslog). Graylog **archivia e indicizza questi registri**, consentendo di eseguire ricerche globali e di creare avvisi.



Graylog è uno strumento di analisi e monitoraggio che facilita l'identificazione di comportamenti sospetti e di vari problemi (stabilità, prestazioni, ecc.).




![Image](assets/fr/034.webp)



**Nota: la versione gratuita, **Graylog Open**, non è un SIEM come Wazuh, soprattutto perché manca di vere funzioni di rilevamento delle intrusioni.



### II. Prerequisiti



Lo **stack Graylog** si basa su **diversi componenti** che dovremo installare e configurare. Qui installeremo tutti i componenti sullo stesso server, ma è possibile creare cluster basati su diversi nodi e distribuire i ruoli su più server. Ai fini di questa esercitazione, installeremo **Graylog 6.1**, la versione più recente.





- MongoDB 7**, la versione correntemente raccomandata per Graylog (minimo 5.0.7, massimo 7.x)
- OpenSearch**, un Fork open source di Elasticsearch creato da Amazon (minimo 1.1.x, massimo 2.15.x)
- OpenJDK 17**



Il **server Graylog** gira su **Debian 12**, ma l'installazione è possibile su altre distribuzioni, anche tramite Docker. La macchina virtuale è dotata di **8 GB di RAM** e **256 GB di spazio su disco**, in modo da avere risorse sufficienti per tutti i componenti (altrimenti questo può avere un impatto significativo sulle prestazioni). Tuttavia, questo dato è indicativo, poiché **il dimensionamento dell'architettura di Graylog dipende dalla quantità di informazioni da elaborare**. Graylog può elaborare 30 MB o 300 MB di dati al giorno, così come 300 GB di dati al giorno... È una soluzione **scalabile** in grado di gestire **terabyte di registri** (vedere [questa pagina](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Fonte: Graylog



Prima di iniziare la configurazione, assegnare un IP statico Address alla macchina Graylog e installare gli ultimi aggiornamenti. Assicurarsi di impostare il fuso orario della macchina locale e di definire un server NTP per la sincronizzazione di data e ora. Ecco il comando da eseguire:



```
sudo timedatectl set-timezone Europe/Paris
```



**Nota: l'installazione di **OpenSearch è facoltativa** se si utilizza invece **Graylog Data Node**.



### III Installazione passo-passo di Graylog



Iniziamo aggiornando la cache dei pacchetti e installando gli strumenti necessari per il futuro.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Installazione di MongoDB



Una volta fatto questo, inizieremo a installare MongoDB. Scaricare la chiave GPG corrispondente al repository MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Aggiungere quindi il repository di MongoDB 6 alla macchina Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Successivamente, aggiorneremo la cache dei pacchetti e cercheremo di installare MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB non può essere installato perché manca una dipendenza: **libssl1.1**. Dovremo installare questo pacchetto manualmente prima di poter procedere, perché Debian 12 non lo ha nei suoi repository.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Scaricheremo il pacchetto DEB denominato "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (ultima versione) con il comando **wget**, quindi lo installeremo con il comando **dpkg**. Questo produce i due comandi seguenti:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Riavviare l'installazione di MongoDB:



```
sudo apt-get install -y mongodb-org
```



Quindi riavviare il servizio MongoDB e abilitarlo all'avvio automatico quando viene lanciato il server Debian.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Con MongoDB installato, possiamo passare all'installazione del componente successivo.



#### B. Installazione di OpenSearch



Passiamo all'installazione di OpenSearch sul server. Il comando seguente aggiunge la chiave di firma per i pacchetti OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Aggiungiamo quindi il repository OpenSearch, in modo da poter scaricare il pacchetto con **apt** in seguito:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Aggiornare la cache dei pacchetti:



```
sudo apt-get update
```



Quindi **installare OpenSearch**, facendo attenzione a **definire la password predefinita per l'account Admin** dell'istanza. Qui la password è "**IT-Connect2024!**", ma sostituite questo valore con una password forte. **Evitate password deboli** come "**P@ssword123**" e usate almeno **8 caratteri** con almeno un carattere di ogni tipo (minuscolo, maiuscolo, numero e carattere speciale), altrimenti si verificherà un errore alla fine dell'installazione. **Questo è un prerequisito da OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Si prega di essere pazienti durante l'installazione...



Una volta terminato, prendetevi un momento per eseguire la configurazione minima. Aprire il file di configurazione in formato YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Quando il file è aperto, impostare le seguenti opzioni:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Questa configurazione di OpenSearch è stata progettata per configurare un singolo nodo. Ecco alcune spiegazioni dei diversi parametri utilizzati:





- cluster.name: graylog**: questo parametro nomina il cluster OpenSearch con il nome "**graylog**".
- node.name: ${HOSTNAME}**: il nome del nodo viene impostato dinamicamente per corrispondere a quello della macchina Linux locale. Anche se abbiamo un solo nodo, è importante assegnargli un nome corretto.
- path.data: /var/lib/opensearch**: questo percorso specifica dove OpenSearch memorizza i suoi dati sulla macchina locale, in questo caso in "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: questo percorso definisce dove vengono memorizzati i file di log di OpenSearch, qui in "**/var/log/opensearch**".
- discovery.type: single-node**: questo parametro configura OpenSearch per lavorare con un singolo nodo, da cui la scelta dell'opzione "**single-node**".
- network.host: 127.0.0.1**: questa configurazione assicura che OpenSearch ascolti solo il suo anello locale Interface, che è sufficiente dato che si trova sullo stesso server di Graylog.
- action.auto_create_index: false**: disabilitando la creazione automatica dell'indice, OpenSearch non creerà automaticamente un indice quando un documento viene inviato senza un indice esistente.
- plugins.security.disabled: true**: questa opzione disattiva il plugin di sicurezza OpenSearch, il che significa che non ci saranno autenticazione, gestione degli accessi o crittografia delle comunicazioni. Questa impostazione fa risparmiare tempo durante la configurazione di Graylog, ma dovrebbe essere evitata in produzione (vedere [questa pagina](https://opensearch.org/docs/1.0/security-plugin/index/)).



Alcune opzioni sono già presenti, quindi è sufficiente rimuovere il "#" per attivarle, quindi indicare il proprio valore. Se non si riesce a trovare un'opzione, è possibile dichiararla direttamente alla fine del file.



![Image](assets/fr/023.webp)



Salvare e chiudere il file.



#### C. Configurare Java (JVM)



È necessario configurare la macchina virtuale Java utilizzata da OpenSearch per regolare la quantità di memoria che il servizio può utilizzare. Modificare il seguente file di configurazione:



```
sudo nano /etc/opensearch/jvm.options
```



Con la configurazione qui implementata, **OpenSearch inizierà con 4 GB di memoria allocata e potrà crescere fino a 4 GB**, quindi non ci saranno variazioni di memoria durante il funzionamento. Qui la configurazione tiene conto del fatto che la macchina virtuale ha un totale di **8 GB di RAM**. Entrambi i parametri devono avere lo stesso valore. Ciò significa sostituire le righe:



```
-Xms1g
-Xmx1g
```



Con queste righe:



```
-Xms4g
-Xmx4g
```



Ecco un'immagine della modifica da apportare:



![Image](assets/fr/022.webp)



Chiudere il file dopo averlo salvato.



Inoltre, dobbiamo controllare la configurazione del parametro "**max_map_count**" nel kernel Linux. Esso definisce il limite di aree di memoria mappate per processo, al fine di soddisfare le esigenze della nostra applicazione. **OpenSearch**, come Elasticsearch**, raccomanda di impostare questo valore a "262144" per evitare errori di gestione della memoria.



In linea di principio, su una macchina Debian 12 appena installata, il valore è già corretto. Ma controlliamo. Eseguire questo comando:



```
cat /proc/sys/vm/max_map_count
```



Se si ottiene un valore diverso da "**262144**", eseguire il comando seguente, altrimenti non è necessario.



```
sudo sysctl -w vm.max_map_count=262144
```



Infine, abilitate l'avvio automatico di OpenSearch e lanciate il servizio associato.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Se si visualizza lo stato del sistema, si dovrebbe vedere un processo Java con 4 GB di RAM.



```
top
```



![Image](assets/fr/029.webp)



Il prossimo passo: la tanto attesa installazione di Graylog!



#### D. Installazione di Graylog



Per **installare Graylog 6.1** nella sua ultima versione, eseguire i seguenti 4 comandi per **scaricare e installare Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Una volta fatto questo, è necessario apportare alcune modifiche alla configurazione di Graylog prima di provare a lanciarlo.



Cominciamo a configurare queste due opzioni:





- password_secret**: questo parametro serve a definire una chiave utilizzata da Graylog per proteggere la memorizzazione delle password degli utenti (nello spirito di una chiave di salatura). Questa chiave deve essere **unica** e **casuale**.
- root_password_sha2**: questo parametro corrisponde alla password di amministratore predefinita in Graylog. È memorizzata come Hash SHA-256.



Inizieremo generando una chiave di 96 caratteri per il parametro **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Copiare il valore restituito, quindi aprire il file di configurazione di Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Incollare la chiave nel parametro **password_secret**, in questo modo:



![Image](assets/fr/027.webp)



Salvare e chiudere il file.



Successivamente, è necessario impostare la password per l'account "**admin**" creato di default. Nel file di configurazione deve essere memorizzato il Hash della password, il che significa che deve essere calcolato. L'esempio seguente fornisce il Hash della password "**LogsWells@**": adattare il valore alla propria password.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Copiare il valore ottenuto come output (senza il trattino alla fine della riga).



Aprire nuovamente il file di configurazione di Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Incollare il valore nell'opzione **root_password_sha2** in questo modo:



![Image](assets/fr/026.webp)



Nel file di configurazione, impostare l'opzione "**http_bind_address**". Specificare "**0.0.0.0:9000**" in modo che il web Interface di Graylog sia accessibile sulla porta **9000**, attraverso qualsiasi server IP Address.



![Image](assets/fr/024.webp)



Quindi impostare l'opzione "**elasticsearch_hosts**" su `http://127.0.0.1:9200` per dichiarare la nostra istanza OpenSearch locale. Questo è necessario, perché non stiamo usando un **Graylog Data Node**. Senza questa opzione, non sarà possibile andare avanti...



![Image](assets/fr/025.webp)



Salvare e chiudere il file.



Questo comando attiva Graylog in modo che si avvii automaticamente al successivo avvio e lancia immediatamente il server Graylog.



```
sudo systemctl enable --now graylog-server
```



Una volta fatto questo, provare a connettersi a Graylog da un browser. Immettere l'IP Address (o il nome) del server e la porta 9000.



**Per vostra informazione



Non molto tempo fa, al primo accesso a Graylog appariva una finestra di autenticazione simile a quella qui sotto. Si doveva inserire il login "**admin**" e la password. E poi si rimaneva spiacevolmente sorpresi nello scoprire che la connessione non funzionava.



![Image](assets/fr/031.webp)



È stato necessario tornare alla riga di comando del server Graylog e consultare i log. Si è potuto così vedere che **per la prima connessione**, è necessario **utilizzare una password temporanea**, specificata nei log.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



È stato quindi necessario riprovare la connessione con l'utente "**admin**" e la password temporanea, che ha permesso di effettuare il login!



**Questo non è più il caso. Tutto ciò che dovete fare è accedere con il vostro account di amministratore e la password configurata alla riga di comando



![Image](assets/fr/033.webp)



**Benvenuti al Interface di Graylog!



![Image](assets/fr/019.webp)



#### E. Graylog: creare un nuovo account amministratore



Invece di utilizzare l'account amministratore creato in modo nativo da Graylog, è possibile creare il proprio account amministratore personale. Fare clic sul menu "**Sistema**", quindi su "**Utenti e team**" e cliccare sul pulsante "**Crea utente**". Compilare quindi il modulo e assegnare il ruolo di amministratore al proprio account.



![Image](assets/fr/020.webp)



Un account personalizzato può contenere informazioni aggiuntive, come nome e cognome ed e-mail Address, a differenza di un account amministratore nativo. Inoltre, questo garantisce una migliore tracciabilità quando ogni persona lavora con un account nominato.



## Inviare i log a Graylog con rsyslog



### I. Presentazione



In questa seconda parte, impareremo a configurare una macchina Linux per inviare i suoi log a un server Graylog. Per farlo, installeremo e configureremo Rsyslog sul sistema.



### II. Configurazione di Graylog per ricevere i log di Linux



Inizieremo configurando Graylog. Ci sono tre passaggi da completare:





- La creazione di un **Input** per creare un punto di ingresso che permetta alle macchine Linux di **inviare log Syslog via UDP**.
- La creazione di un nuovo **indice** per memorizzare e **indicizzare tutti i registri Linux**.
- Creazione di uno **Stream** per **indirizzare** i log ricevuti da Graylog al nuovo indice Linux.



#### A. Creare un ingresso per Syslog



Accedere a Graylog Interface, fare clic su "**Sistema**" nel menu e poi su "**Ingressi**". Nell'elenco a discesa, selezionare "**Syslog UDP**" e fare clic sul pulsante "**Lancia nuovo ingresso**". È anche possibile creare un ingresso Syslog TCP, ma questo richiede l'uso di un certificato TLS: un vantaggio per la sicurezza, ma non è trattato in questo articolo.



![Image](assets/fr/001.webp)



Sullo schermo apparirà una procedura guidata. Iniziare dando un nome a questo input, ad esempio "**Graylog_UDP_Rsyslog_Linux**" e scegliere una porta. Per impostazione predefinita, la porta è "**514**", ma è possibile personalizzarla. Qui è stata selezionata la porta "**12514**".



![Image](assets/fr/016.webp)



È anche possibile selezionare l'opzione "**Store full message**" per memorizzare l'intero messaggio di log in Graylog. Fare clic su "**Lancio dell'input**".



![Image](assets/fr/017.webp)



Il nuovo ingresso è stato creato ed è ora attivo. Graylog può ora ricevere i log Syslog sulla porta 12514/UDP, ma non abbiamo ancora finito di configurare l'applicazione.



![Image](assets/fr/018.webp)


**Nota: un singolo ingresso può essere usato per memorizzare i registri di diverse macchine Linux.



#### B. Creare un nuovo indice Linux



È necessario creare un indice in Graylog per memorizzare i log dalle macchine Linux. Un **indice** in Graylog è una struttura di archiviazione che contiene i log ricevuti, cioè i messaggi ricevuti. Graylog utilizza OpenSearch come motore di archiviazione e i messaggi sono indicizzati per consentire ricerche rapide ed efficienti.



Da Graylog, fare clic su "**Sistema**" nel menu, quindi su "**Indici**". Nella nuova pagina visualizzata, fare clic su "**Create index set**".



![Image](assets/fr/005.webp)



Nominare questo indice, ad esempio "**Indice Linux**", aggiungere una descrizione e un prefisso, prima di confermare. In questo caso, **magazzineremo tutti i registri di Linux in questo indice**. È anche possibile creare indici specifici per memorizzare solo determinati registri (solo registri [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), registri di servizi Web, ecc.)



![Image](assets/fr/006.webp)



Ora dobbiamo creare un nuovo flusso per indirizzare i messaggi a questo indice.



#### C. Creare un flusso



Per creare un nuovo flusso, fare clic su "**Flussi**" nel menu principale di Graylog. Quindi fare clic sul pulsante "**Create stream**" a destra. Nella finestra che appare, dare un nome al flusso, ad esempio "**Flusso Linux**" e scegliere l'indice "**Indice Linux**" per il campo "**Index Set**". Confermare la scelta.



**Nota: i messaggi corrispondenti a questo flusso saranno inclusi anche nel "**Flusso predefinito**", a meno che non si selezioni l'opzione "**Rimuovi le corrispondenze dal 'flusso predefinito'**".



![Image](assets/fr/002.webp)



Quindi, nelle impostazioni di Steam, fare clic sul pulsante "**Aggiungi regola flusso**" per aggiungere una nuova regola di instradamento dei messaggi. Se non riuscite a trovare questa finestra, cliccate su "**Streams**" nel menu, quindi sulla riga corrispondente al vostro stream, cliccate su "**More**" e poi su "**Manage Rules**".



Scegliere il tipo "**match input**" e selezionare l'input **Rsyslog in UDP** creato in precedenza. Confermare con il pulsante "**Crea regola**". Tutti i messaggi inviati al nuovo ingresso saranno ora inviati all'Indice per Linux.



![Image](assets/fr/003.webp)



Il nuovo stream dovrebbe apparire nell'elenco e dovrebbe essere nello stato "**Running**". La larghezza di banda dei messaggi mostra "**0 msg/s**", poiché al momento non viene inviato alcun log all'ingresso UDP di Rsyslog. Per visualizzare i registri di un flusso, è sufficiente fare clic sul suo nome.



![Image](assets/fr/004.webp)



**Tutto è pronto sul lato Graylog**. Il passo successivo è la configurazione della macchina Linux.



### III. Installazione e configurazione di Rsyslog su Linux



Accedere alla macchina Linux, in locale o in remoto, e utilizzare un account utente con i permessi di elevare i suoi privilegi (tramite sudo). Altrimenti, utilizzare direttamente l'account "root".



#### A. Installazione del pacchetto Rsyslog



Iniziate aggiornando la cache dei pacchetti e installando il pacchetto denominato "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Quindi controllare lo stato del servizio. Nella maggior parte dei casi, è già in funzione.



```
sudo systemctl status rsyslog
```



#### B. Configurazione di Rsyslog



Rsyslog ha un file di configurazione principale che si trova qui:



```
/etc/rsyslog.conf
```



Inoltre, la directory "**/etc/rsyslog.d/**" è usata per memorizzare altri file di configurazione per Rsyslog. Nel file di configurazione principale è presente una direttiva Include per importare tutti i file "**.conf**" presenti in questa directory. In questo modo è possibile avere file aggiuntivi per la configurazione di Rsyslog senza modificare il file principale.



In questa directory è necessario utilizzare dei numeri per definire l'ordine di caricamento, poiché i file vengono caricati in ordine alfabetico. L'aggiunta di un prefisso numerico consente di gestire la priorità tra più file di configurazione. In questo caso, abbiamo solo un file aggiuntivo, quindi non è un problema.



In questa directory verrà creato un file chiamato "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



In questo file, inserire questa riga:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Ecco come interpretare questa linea:





- `*.*`: significa inviare tutti i log Syslog dalla macchina Linux a Graylog.
- `@`: indica che il trasporto viene eseguito in UDP. È necessario specificare "**@@**" per passare a TCP.
- `192.168.10.220:12514`: indica il Address del server Graylog e la porta su cui vengono inviati i log (corrispondente all'Input).
- `RSYSLOG_SyslogProtocol23Format`: corrisponde al formato dei messaggi da inviare a Graylog.



Al termine, salvare il file e riavviare Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Dopo questa azione, i primi messaggi dovrebbero arrivare sul server Graylog!



### IV. Visualizzazione dei log di Linux in Graylog



Da Graylog, è possibile fare clic su "**Streams**" e selezionare il nuovo stream per visualizzare i messaggi correlati. In alternativa, fare clic su "**Ricerca**", selezionare il proprio Steam e avviare una ricerca.



Ecco alcune caratteristiche principali del Interface:



**1** - Selezionare il periodo per il quale visualizzare i messaggi. Per impostazione predefinita, vengono visualizzati i messaggi degli ultimi 5 minuti.



**2** - Selezionare il flusso o i flussi da visualizzare.



**3** - Attivare l'aggiornamento automatico dell'elenco dei messaggi (ad esempio, ogni 5 secondi). Altrimenti, l'elenco sarà statico e si dovrà aggiornarlo manualmente.



**4** - Fare clic sulla lente di ingrandimento per avviare la ricerca dopo aver modificato il periodo, il flusso o il filtro.



**5** - Barra di immissione per specificare i filtri di ricerca. In questo caso, ho specificato "**source:srv\-docker**" per visualizzare solo i log della nuova macchina su cui ho appena configurato Rsyslog.



I log vengono inviati dalla macchina Linux:



![Image](assets/fr/015.webp)



### V. Identificazione di un errore di connessione SSH



Il punto di forza di Graylog è la capacità di indicizzare i log e di effettuare ricerche in base a vari criteri: macchina di origine, Timestamp, contenuto del messaggio, ecc... Potremmo cercare di identificare le connessioni SSH fallite.



Da una macchina remota (il server Graylog, per esempio), provare a connettersi al server Linux su cui è stato appena configurato Rsyslog. Ad esempio:



```
ssh [email protected]
```



Quindi inserire deliberatamente un **nome utente** e una **password** errati, al fine di ottenere **errori di connessione generate**. Nel file "**/var/log/auth.log**", questo farà sì che generate registri messaggi simili ai seguenti:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Dovreste trovare questi messaggi su Graylog.



Su Graylog, utilizzare il seguente filtro di ricerca per visualizzare solo i messaggi corrispondenti:



```
message:Failed password AND application_name:sshd
```



Se si dispone di più server e si desidera analizzare i registri di un server specifico, specificare il suo nome in aggiunta a:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Ecco una panoramica del risultato su una macchina in cui ho generato diversi errori di connessione, in momenti diversi della giornata:



![Image](assets/fr/009.webp)



I tentativi di connessione non riusciti vengono effettuati dalla macchina con IP Address "**192.168.10.199**". Per saperne di più sull'attività di questo host, è possibile **ricercare questo IP Address**. Graylog produrrà tutti i log in cui si fa riferimento a questo IP Address, su tutti gli host (per i quali è configurato l'invio di log).



In questo caso, il filtro da utilizzare può essere:



```
message:"192.168.10.199"
```



Otteniamo altri risultati (non sorprendenti, dato che non filtriamo l'applicazione SSH):



![Image](assets/fr/008.webp)



### VI. Conclusione



Seguendo questa guida, dovreste essere in grado di configurare una macchina Linux per inviare i suoi log a un server Graylog. In questo modo, sarete in grado di centralizzare i log dei vostri host Linux nel vostro log sink!



Per andare oltre, considerate la possibilità di creare dashboard e avvisi per ricevere notifiche quando viene rilevata un'anomalia.



![Image](assets/fr/007.webp)