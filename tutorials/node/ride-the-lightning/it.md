---
name: Ride The Lightning (RTL)
description: Utilizzare Ride The Lightning (RTL) per gestire il proprio nodo Lightning
---
![cover](assets/cover.webp)


## 1. Introduzione



**Ride The Lightning (RTL)** è un'applicazione web completa Interface per la gestione di un nodo Lightning Network. Questa applicazione web self-hosted offre un **cockpit Lightning** accessibile dal browser. RTL funziona con tutte le principali implementazioni di Lightning (LND, Core Lightning/CLN ed Eclair) e offre un controllo totale sul nodo e sui canali. Open-source (licenza MIT) e gratuito, RTL è integrato di default in molte soluzioni di nodi chiavi in mano (RaspiBlitz, MyNode, Umbrel, ecc.).



**Senza un interface grafico, i nodi Lightning possono essere gestiti solo tramite comandi CLI di facile utilizzo. RTL semplifica queste operazioni con un interface ergonomico. Ecco le principali applicazioni:**





- **Visualizzazione dei canali e dei nodi** - La dashboard visualizza il saldo On-Chain, la liquidità di Lightning (locale/remoto), lo stato di sincronizzazione, l'alias del nodo e altro ancora. È possibile visualizzare l'elenco dei canali, la capacità, la distribuzione locale/remota e lo stato. RTL offre dashboard sensibili al contesto per analizzare l'attività da diversi punti di vista.





- **Gestione fulminea dei canali** - Aprite/chiudete i canali con pochi clic. RTL consente di connettersi a un peer e di aprire un canale senza alcun comando. È possibile regolare le commissioni di routing, visualizzare il punteggio del saldo o avviare un ribilanciamento circolare per riequilibrare i fondi tra i canali.





- **Tracciamento e pagamenti** - RTL gestisce le transazioni Lightning: invio di pagamenti tramite fatture, fatture generate da ricevere, tracciamento delle transazioni (pagamenti, instradamento) con cronologia dettagliata. Interface analizza anche l'instradamento per vedere quali pagamenti passano attraverso il vostro nodo.





- **Gestione e backup Wallet On-Chain** - La scheda On-Chain consente di gestire gli indirizzi generate e di inviare transazioni. RTL semplifica il salvataggio dei canali esportando il file SCB per il LND, con aggiornamento automatico per ogni modifica del canale.



In breve, RTL è un **potente cruscotto per il Lightning Network**, che offre un Interface educativo per pilotare il vostro nodo su base quotidiana. Questo tutorial vi guiderà attraverso la sua installazione e il suo utilizzo per gestire i canali e i pagamenti.



## 2. Funzionamento tecnico dell'RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Prima di entrare nel vivo, è utile capire brevemente **come RTL interagisce con il nodo Lightning** a livello tecnico.



**Architettura generale:** RTL è un'applicazione web costruita con Node.js (backend) e Angular (frontend). In concreto, RTL viene eseguito come un piccolo server web locale (sulla porta 3000 per impostazione predefinita) che dialoga con l'implementazione di Lightning tramite le sue API. A seconda del tipo di API :





- Con **LND**, RTL utilizza l'API REST di LND (porta 8080) per eseguire i comandi di Lightning. La connessione è protetta da TLS e richiede il file **admin macaroon** di LND per l'autenticazione.





- Con **Core Lightning (CLN)**, RTL utilizza l'API REST fornita da *c-lightning-REST*, oppure una **runa di accesso** tramite il plugin `commando`. Soluzioni come Umbrel configurano automaticamente queste Elements.





- Con **Eclair**, RTL si connette all'API REST di Eclair utilizzando la password di autenticazione configurata.



**Configurazione e sicurezza:** RTL è configurato tramite un file JSON (`RTL-Config.json`) in cui si definiscono la porta web, la password di accesso e le informazioni di connessione al nodo. Il web Interface è protetto da una login/password (la `password` predefinita può essere modificata) e supporta il 2FA. Per impostazione predefinita, RTL funziona come HTTP locale (`http://localhost:3000`), ma per l'accesso remoto, utilizzare sempre una connessione sicura (HTTPS tramite reverse-proxy, Tor o VPN).



In breve, RTL è un componente aggiuntivo che si connette al vostro nodo tramite API sicure, richiede token di accesso appropriati e offre il proprio Layer di sicurezza. Questa architettura modulare consente persino di gestire **diversi nodi Lightning con una singola istanza RTL**.



## 3. Installazione RTL



Poiché RTL è distribuito come software open-source, esistono diversi modi per installarlo sul sistema. In questa sezione tratteremo due approcci principali: l'installazione manuale e l'installazione tramite Umbrel.



### Metodo manuale



L'installazione manuale è adatta se si desidera mantenere un controllo a grana fine o se si sta integrando RTL in una configurazione personalizzata. I passaggi riportati di seguito si riferiscono a un nodo LND con sistema operativo Linux (ad esempio Raspberry Pi o VPS con Ubuntu/Debian), ma sono simili per CLN/Eclair.



**Prerequisito:** assicurarsi di avere un nodo Bitcoin **sincronizzato** e un nodo Lightning funzionante (LND, CLN o Eclair) sulla macchina. RTL non contiene un nodo Lightning di per sé, ma si collega a un nodo esistente. È inoltre necessario che **Node.js** sia installato (si consiglia la versione 14+). È possibile verificare con `node -v` o installare Node dal sito ufficiale (https://nodejs.org/en/download/) o dal proprio gestore di pacchetti.



Le principali fasi di installazione sono :



**Scaricare il codice RTL**: Clonare il repository ufficiale RTL su GitHub nella directory di propria scelta. Ad esempio:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Installare le dipendenze**: RTL è un'applicazione Node.js, quindi è necessario installare i moduli necessari. Nella cartella di RTL, eseguire :



```bash
npm install --omit=dev --legacy-peer-deps
```



Questo comando installa i pacchetti NPM necessari (ignorando le dipendenze di sviluppo). L'opzione `--legacy-peer-deps` è consigliata per evitare possibili conflitti di dipendenza da Node.



**RTL-Config**: Una volta che le dipendenze sono a posto, preparare il file di configurazione. Copiare/rinominare il file `Sample-RTL-Config.json` nella root del progetto in `RTL-Config.json`. Aprirlo nel file :





- **Password UI**: scegliere una password sicura e inserirla in `multiPass` (invece della `"password"` predefinita).
- **Porta**: predefinita `3000`. È possibile cambiarla se la porta è già occupata sul computer.
- **Nodo**: nella sezione `nodi[0]`, regolare i parametri per il proprio nodo:
     - `lnNode`: un nome descrittivo per il nodo (ad esempio, `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (o `"CLN"`/`"ECL"` a seconda dei casi).
     - Sotto `autenticazione`:
       - macaroonPath`: specificare il percorso completo della cartella contenente l'admin di LND.
       - `configPath`: percorso del file di configurazione del nodo (`LND.conf` per il LND).
     - In `Impostazioni`:
       - `fiatConversion`: impostare `true` se si desidera la conversione della valuta fiat.
       - `unannouncedChannels`: impostare su `true` per vedere i canali non annunciati.
       - themeColor` e `themeMode`: Personalizzazione Interface.
       - channelBackupPath`: percorso per i backup dei canali LND.
       - `lnServerUrl`: URL del nodo Lightning (ad esempio, `https://127.0.0.1:8080`).



**Avviare il server RTL**: Nella cartella RTL, eseguire :



```bash
node rtl
```



L'applicazione si avvia e si può accedere a `http://localhost:3000`.



**(Opzionale) Eseguire RTL come servizio**: Per l'avvio automatico, creare un file systemd :



Per farlo:




- Aprite un terminale sul vostro computer.
- Creare un nuovo file di servizio con il seguente comando (sostituire `nano` con il proprio editor preferito):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Copiate e incollate il contenuto sottostante in questo file:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Sostituire `/path/to/RTL/rtl` con il percorso effettivo del file `rtl` sulla propria macchina e `<vostro_utente>` con il proprio nome utente Linux.
- Salvare e chiudere il file.
- Ricaricare la configurazione di systemd:


```bash
sudo systemctl daemon-reload
```




- Attivare e avviare il servizio RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL si avvia automaticamente a ogni riavvio della macchina. È possibile controllare il suo stato con :


```bash
sudo systemctl status RTL
```



### Installazione tramite Umbrel



Se si usa [Umbrel](https://getumbrel.com), l'installazione RTL è molto più semplice:





- Accesso a Interface Umbrel (di solito tramite `http://umbrel.local`)
- Andare su **App Store**
- Ricerca di "Ride The Lightning"



**Nota importante: ci sono due applicazioni RTL separate nell'App Store di Umbrel:**




- **Ride The Lightning** (per LND): da utilizzare con il nodo Lightning predefinito di Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: utilizzare solo se si è installata l'applicazione *Core Lightning* su Umbrel e si desidera gestire questo nodo con RTL.



*Ogni versione RTL è preconfigurata per dialogare con l'implementazione corrispondente (LND o Core Lightning). Se non avete cambiato il vostro nodo Lightning, scegliete semplicemente la versione classica LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Fare clic su **Installazione**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Importante:** Dopo l'installazione, RTL visualizza una schermata con la password predefinita. **Copiate e salvate questa password**: vi servirà per accedere al Interface RTL. Questa password verrà visualizzata a ogni avvio di RTL finché non si seleziona l'opzione "Non mostrarla più".



Umbrel si occupa automaticamente di :




- Scaricare e configurare RTL
- Configurazione dell'accesso al nodo Lightning
- Gestire gli aggiornamenti
- Protezione dell'accesso al Interface



Una volta installata, l'applicazione appare nel menu *Apps* di Umbrel. Fare clic su **Ride The Lightning** per avviarla.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Nella schermata di accesso, inserire la password copiata in precedenza. Una volta effettuato l'accesso, l'RTL web Interface sarà accessibile direttamente dalla dashboard di Umbrel, senza bisogno di ulteriori configurazioni!



## 4. Introduzione e utilizzo di Interface RTL



Ora che RTL è attivo e funzionante, esploriamo il web Interface e le sue caratteristiche principali. Passeremo in rassegna le diverse sezioni dell'applicazione per darvi una panoramica completa.



### Il pannello di controllo principale



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Non appena si effettua il login, si accede alla **dashboard principale**, che offre una panoramica del proprio nodo Lightning. Questa pagina centralizza le informazioni essenziali:




- Il saldo totale di Lightning
- Saldo On-Chain disponibile
- La ripartizione della vostra liquidità (in entrata/uscita)
- Accesso rapido all'invio e alla ricezione di Satss tramite il vostro nodo Lightning



### Gestione dei fondi On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



La scheda **On-Chain** consente di gestire i bitcoin direttamente sulla catena principale:




- Visualizzazione del saldo in diverse unità (Sats, BTC, USD)
- Elenco completo delle transazioni
- Generazione Address Taproot (P2TR), P2SH (NP2WKH) o Bech32 (P2WKH)
- Gestione UTXO, ricezione e invio di bitcoin



### Lightning: presentazione dettagliata dei sottomenu



Interface RTL presenta un menu laterale dedicato a Lightning Network, che riunisce tutte le funzioni essenziali per la gestione del nodo. Ecco i dettagli di ciascun sottomenu, nell'ordine della schermata:



#### 1. Pari/Canali



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Questo sottomenu consente di :




- Visualizza l'elenco dei peer connessi e dei canali Lightning aperti o in attesa.
- Aggiungere un nuovo peer (connettersi a un altro nodo Lightning).
- Aprire, chiudere o gestire i canali esistenti.
- Visualizzare i dettagli di ogni canale: capacità, saldi locali/remoti, stato, storia del trading, punteggio del saldo, ecc.



#### 2. Transazioni



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



In questo sottomenu è possibile :




- Inviare i pagamenti Lightning (tramite Invoice).
- generate e gestire le fatture per ricevere i pagamenti.
- Visualizzare lo storico completo dei pagamenti inviati e ricevuti, con i relativi dettagli (importo, data, stato, spese, numero di salti, ecc.).



#### 3. Instradamento



Questo sottomenu visualizza :




- Pagamenti instradati dal vostro nodo per altri utenti Lightning Network.
- Statistiche di instradamento: numero di transazioni trasmesse, commissioni percepite, errori riscontrati.
- Cronologia esportabile per analisi avanzate.



#### 4. Rinvii



Questo sottomenu offre :




- Rapporti dettagliati sull'attività del nodo Lightning.
- Grafici e tabelle su canali, pagamenti, tariffe, capacità, ecc.
- Strumenti per comprendere meglio le prestazioni del nodo.



#### 5. Ricerca del grafico



Questo sottomenu consente di :




- Esplorare la topologia del Lightning Network.
- Ricerca di nodi o canali specifici.
- Ottenere informazioni sulla connettività e sulla capacità complessiva della rete.



#### 6. Firma/Verifica



Questo sottomenu offre :




- La capacità di firmare un messaggio con la chiave del proprio nodo (prova di Ownership).
- Verifica della firma per autenticare i messaggi provenienti da altri nodi.



#### 7. Backup



Questo sottomenu è dedicato al backup:




- Esportazione del file di backup del canale (SCB per LND).
- Se necessario, ripristinare la configurazione o i canali.
- Suggerimenti per proteggere i backup.



#### 8. Nodo/Rete



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



In questo sottomenu si trova :




- Un riepilogo completo dello stato del nodo Lightning: alias, versione, colore, stato di sincronizzazione.
- Statistiche sui canali (attivi, in attesa, chiusi), capacità totale, connettività.
- Informazioni sul Lightning Network globale e sulla posizione del nodo in esso.



### Servizi: Scambi Boltz



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz è un servizio di privacy-friendly, non custodiale Exchange che converte i bitcoin tra Lightning Network e Blockchain Bitcoin (On-Chain). Offre due tipi di operazioni: Reverse Submarine Swap (**Swap Out**) e Submarine Swap (**Swap In**).



#### Swap Out (Scambio sottomarino inverso)



Swap Out converte i Satss disponibili sul Lightning Network in bitcoin del On-Chain. Questo meccanismo è utile quando un nodo esaurisce la capacità in entrata, o quando si desidera recuperare fondi da un On-Chain Address. Il processo funziona come segue:




- L'utente seleziona un importo da scambiare
- Il nodo invia un pagamento Lightning a Boltz
- Nel Exchange, Boltz blocca un importo equivalente in bitcoin del On-Chain
- Una volta confermata la transazione, l'utente può reclamare i fondi rivelando un segreto utilizzato nello scambio



Questo processo non è di tipo detentivo: Boltz non trattiene mai i fondi dell'utente.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Scambio di sottomarini)



Swap In, invece, permette di reimmettere i fondi del On-Chain nel Lightning Network. Ciò è particolarmente utile per ripristinare la capacità di uscita dei canali. La procedura è la seguente:




- L'utente invia bitcoin a uno specifico Address generato da Boltz
- Questi fondi possono essere sbloccati da Boltz solo se paga un Lightning Invoice generato dal nodo dell'utente
- Una volta pagato il Invoice, i fondi sono disponibili sul canale Lightning, aumentando la capacità di produzione del nodo



![Configuration d'un swap-in](assets/fr/12.webp)



Questi due meccanismi consentono di gestire in modo efficiente la liquidità del canale Lightning, mantenendo la sovranità dell'utente sui propri fondi.



### Configurazione e personalizzazione



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



La scheda **Configurazione del nodo** consente di personalizzare l'esperienza:




- Attivazione di canali non annunciati
- Personalizzare la visualizzazione delle vendite
- Configurazione Block explorer
- Regolazione del Interface



### Documentazione e assistenza



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Infine, la sezione **Help** offre una documentazione completa su :




- Configurazione iniziale
- Gestione dei pari e dei canali
- Pagamenti e transazioni
- Backup e ripristini
- Rapporti e statistiche
- Firme e verifiche
- Parametri del nodo e dell'applicazione



Questo Interface completo consente di gestire il nodo Lightning in modo efficiente, dalle operazioni di base alle funzioni avanzate, il tutto in un Interface intuitivo e ben organizzato.



## 5. Casi d'uso avanzati e sicurezza



In questa sezione, ecco ciò che occorre sapere per andare avanti con l'RTL e proteggere il nodo Lightning:



### Monitoraggio e risoluzione dei problemi



Per monitorare il nodo, è possibile esportare i dati RTL (log, CSV) e visualizzarli in strumenti come Grafana. In caso di problemi (pagamento bloccato, canale inattivo), consultate i log LND/CLN e utilizzate i comandi di diagnostica (`lncli listchannels`, `lncli pendingchannels`, ecc.). RTL offre anche i log del Interface per monitorare gli eventi di routing.



### Accesso remoto sicuro



Non esporre mai la RTL direttamente su Internet. Dare la preferenza a :




- **VPN** (ad es. Tailscale) per un accesso privato e crittografato
- **Tor** per un accesso sicuro e anonimo
- Reverse proxy **HTTPS** (Nginx/Caddy) solo se si sa come configurarlo



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Buone pratiche di sicurezza





- **Proteggete il vostro accesso**: non condividete mai admin.macaroon o la vostra password RTL. Limitare i permessi sui file sensibili.
- **Backup regolari**: esportare il file di backup del canale (SCB) dopo ogni modifica e conservarlo al di fuori del nodo.
- **Aggiornamenti**: mantenete RTL, il vostro nodo e Umbrel aggiornati con le ultime correzioni di sicurezza.
- **Riservatezza**: anonimizzare i log e le schermate prima di condividerli. Non condividere mai pubblicamente i saldi o gli elenchi di pari.
- **Accesso singolo**: RTL non è multiutente. Non condividere l'accesso all'amministrazione. Per l'accesso in sola lettura, utilizzare un macaron dedicato, se necessario.



Applicando questi principi, si limitano notevolmente i rischi e si mantiene il controllo sul nodo Lightning.



## 7. Conclusione



**Ride The Lightning** è uno strumento essenziale per gestire efficacemente un nodo Bitcoin/Lightning, sia che siate principianti o utenti avanzati. Fornisce un Interface chiaro per il controllo dei canali, dei pagamenti e dello stato di salute del nodo, approfondendo al contempo la comprensione del Lightning Network.



RTL si distingue per la sua compatibilità multi-implementazione, le sue funzioni avanzate (ribilanciamento, swap, report) e il suo approccio pedagogico. Per esigenze semplici, il Interface Umbrel o il Wallet mobile sono sufficienti, ma l'RTL è perfetto per una gestione attiva e ottimizzata dei nodi.



Per saperne di più :




- Sito ufficiale di RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Discussioni tecniche, annunci di progetti, feedback e risorse didattiche
- **Forum della comunità Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Forum ufficiale con sezione dedicata a Bitcoin/Lightning, guide e soluzioni ai problemi più comuni
- **Sviluppatori Lightning Network**: [github.com/lightning](https://github.com/lightning) - Repository GitHub ufficiale per seguire lo sviluppo e contribuire al codice sorgente
- **Pila Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Domande e risposte tecniche con sviluppatori e utenti avanzati



In breve, RTL vi offre un controllo totale sul vostro nodo Lightning, in un Interface moderno e completo.



**Fonti :** Sito ufficiale RTL; RTL GitHub; Umbrel App Store; Umbrel Community; Risorse della rete Plan B.



Per approfondire la comprensione del funzionamento del Lightning Network, vi consiglio di seguire questo corso gratuito:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb