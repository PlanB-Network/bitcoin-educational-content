---
name: ThunderHub
description: Interface Web di gestione del nodo luminoso LND
---
![cover](assets/cover.webp)



## Introduzione



ThunderHub è un **gestore open-source per i nodi Lightning (LND)**, che offre un Interface intuitivo accessibile da qualsiasi dispositivo o browser.



**Caratteristiche principali:**




- **Monitoraggio**: Visione globale di saldi, canali, transazioni, statistiche di routing
- **Gestione**: Apertura/chiusura canali, pagamenti in entrata/uscita, bilanciamento canali
- **Integrazioni**: Supporto LNURL, scambi via Boltz, backup Amboss
- **Interface responsive**: Compatibile con dispositivi mobili, tablet e desktop con temi scuri o chiari



ThunderHub si integra facilmente con **Umbrel**, **Voltage**, **RaspiBlitz** e **MyNode**, semplificando la gestione quotidiana del nodo.



**ThunderHub è particolarmente adatto agli operatori che cercano un interface ergonomico per gestire i propri canali, controllare la liquidità (ribilanciamento), monitorare le transazioni e integrare servizi di terze parti come Amboss. La sicurezza è garantita da una connessione locale o Tor.**



Se non avete ancora un nodo Lightning, vi consigliamo di seguire la nostra esercitazione su LND Umbrel:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installazione



ThunderHub può essere installato in diversi modi, a seconda dell'ambiente di hosting del nodo Lightning. Sia che si utilizzi una soluzione "chiavi in mano" (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, ecc.) o un'installazione manuale, ThunderHub è spesso disponibile senza grandi sforzi. Di seguito descriviamo due approcci comuni: tramite l'App Store di Umbrel e tramite l'installazione manuale (applicabile a un server o a una distribuzione self-hosted).



### Installazione tramite Umbrel



Umbrel integra ThunderHub nel suo **App Store**, rendendo l'installazione estremamente semplice. Non c'è bisogno di una riga di comando o di una configurazione manuale: tutto avviene tramite Interface Umbrel. Basta seguire questi passaggi:





- Aprire la dashboard di **Umbrel**: Connettersi al web Interface del proprio nodo Umbrel (ad esempio `http://umbrel.local` sulla rete locale, o tramite il suo `.onion` Address se si utilizza Tor).
- **Accedere all'App Store**: Nel menu principale di Umbrel, cliccate su "App Store" (o "App"). Cercare **ThunderHub** nell'elenco delle applicazioni disponibili.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Installare ThunderHub**: Fare clic sull'applicazione ThunderHub, quindi sul pulsante di installazione. Confermare se necessario. Umbrel scaricherà e distribuirà automaticamente ThunderHub sul vostro nodo.





- **Avviare l'applicazione**: Una volta completata l'installazione (qualche decina di secondi), ThunderHub appare nella pagina iniziale. Fare clic sull'icona per aprirla. ThunderHub si avvia nel browser.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Importante:** Quando ThunderHub viene aperto per la prima volta, visualizza automaticamente la **password predefinita** necessaria per accedere. L'opzione "Non mostrarla più" consente di nascondere questa visualizzazione per le connessioni future. **Consigliamo vivamente di**




- Salvate immediatamente questa **password** nel vostro gestore di password
- **Copiatelo** per utilizzarlo nella fase successiva
- Una volta salvata la password, selezionare "Non mostrare più questo"



![Page de connexion de ThunderHub](assets/fr/03.webp)



Verrà quindi visualizzata la pagina di accesso, in cui è necessario inserire la password copiata nel passaggio precedente per sbloccare il Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel si occupa di fornire a ThunderHub le informazioni sulla connessione LND (certificato TLS, macaron di amministrazione, ecc.) in background, quindi non è necessario effettuare alcuna configurazione aggiuntiva. In pochi clic, ThunderHub sarà attivo e funzionante sul vostro nodo Umbrel.



### Installazione manuale (self-hosted, escluso Umbrel)



Per gli utenti esterni a Umbrel (ad esempio su un server personale, su un Raspberry Pi con RaspiBlitz o su un'installazione *stand-alone*), l'installazione di ThunderHub richiede alcuni passaggi aggiuntivi. Di seguito descriviamo l'installazione dai sorgenti e la configurazione, secondo la [documentazione ufficiale di ThunderHub](https://docs.thunderhub.io).



#### Installazione



**Prequisiti:** Assicurarsi che il sistema soddisfi i requisiti minimi secondo [documentation setup](https://docs.thunderhub.io/setup):




- **Node.js** versione 18 o superiore
- **npm** installato
- Accesso ai file di autenticazione LND :
  - Certificato TLS LND (`tls.cert`)
  - Macaron di amministrazione LND (`admin.macaron`)
  - LND servizio gRPC Address (nome host:porta) (default `127.0.0.1:10009` a livello locale)



**1. Recuperare il codice ThunderHub:** Clonare il repository GitHub del progetto come descritto nella [documentazione di installazione](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. installare le dipendenze e creare l'applicazione:**



```bash
npm install
npm run build
```



Questi comandi installano tutti i moduli necessari e compilano l'applicazione (ThunderHub è scritto in TypeScript/React).



**3. Aggiornamento successivo:** ThunderHub offre diversi metodi per gli aggiornamenti futuri:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Configurazione (Setup)



**1. File di configurazione principale:** Creare un file `.env.local` nella radice della cartella ThunderHub per personalizzare la configurazione (questo impedirà che le impostazioni vengano sovrascritte durante gli aggiornamenti). Variabili principali come da [documentazione di setup](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Configurazione degli account del server:** Creare il file YAML specificato in `ACCOUNT_CONFIG_PATH`:



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Accesso remoto:** Per connettersi a un nodo LND remoto, aggiungere a `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Sicurezza:** Al primo avvio, ThunderHub **automaticamente** nasconde la `masterPassword` e tutte le password degli account nel file YAML, per evitare di avere password in chiaro sul server.



**5. Avviare ThunderHub:**



```bash
npm start
```



Per impostazione predefinita, il server è in ascolto sulla porta 3000. Accedere a `http://localhost:3000` (o `http://ip-serveur:3000` dalla rete locale).



**6. Alternativa Docker:** ThunderHub fornisce immagini Docker ufficiali:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Viene visualizzata la pagina di accesso a ThunderHub. Selezionare l'account configurato e inserire la password per accedere alla dashboard.



**Installazione su altre distribuzioni:** Le distribuzioni di nodi preconfezionate (RaspiBlitz, MyNode, Start9, ecc.) offrono generalmente il supporto nativo di ThunderHub attraverso le rispettive interfacce di amministrazione.



**Per ulteriori informazioni:** Consultare la documentazione ufficiale completa :




- **Installazione:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Configurazione:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Queste risorse illustrano in dettaglio opzioni avanzate come gli account SSO, i macaron crittografati, la configurazione di TOR e molto altro ancora.



Una volta che ThunderHub è installato e accessibile, si è pronti a sfruttarne tutte le funzionalità. Nella sezione seguente, daremo un'occhiata a ThunderHub Interface e alle sue varie schede, per guidarvi nel suo utilizzo.



## Presentazione del Interface



Interface ThunderHub è strutturato attorno a un menu principale (solitamente visualizzato nella colonna laterale sinistra) che comprende diverse sezioni chiave. Ognuna di esse corrisponde a un aspetto della gestione del nodo Lightning. Esaminiamole una per una:





- **Home** - Scheda Home con dashboard generale (panoramica del nodo e azioni rapide).
- **Dashboard** - Dashboard personalizzabile con widget e metriche avanzate.
- **Peers** - Gestione dei peer lightning (connessioni ad altri nodi).
- **Canali** - Gestione dettagliata dei canali Lightning.
- **Rebalance** - Strumento di bilanciamento dei canali (pagamenti circolari).
- **Transazioni** - Cronologia dei pagamenti Lightning (transazioni LN).
- **Inoltri** - Statistiche di instradamento (pagamenti inoltrati dal proprio nodo).
- **Catena** - Portafoglio On-Chain di Node (On-Chain BTC: UTXO, transazioni).
- **Amboss** - Integrazione con Amboss (monitoraggio dei nodi, backup, ecc.).
- **Strumenti** - Strumenti vari (backup, messaggi firmati, macaron, rapporti, ecc.).
- **Scambio** - Funzioni di scambio On-Chain/Lightning tramite Boltz.
- **Statistiche** - Statistiche avanzate e metriche delle prestazioni dei nodi.



*(Nota: a seconda della versione di ThunderHub, alcune sezioni possono avere titoli leggermente diversi o funzioni aggiuntive, ma i principi generali rimangono gli stessi)*



### Home (pannello di controllo generale)



La scheda **Home** di ThunderHub è la pagina iniziale che appare dopo l'accesso. Contiene il **Dashboard generale**, che offre una **globale panoramica** dello stato del nodo Lightning e suggerisce **azioni rapide** per le operazioni di routine. Ecco cosa troverete di solito:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Bilanci e capacità:** Nella parte superiore della pagina, ThunderHub visualizza i bilanci disponibili. In genere, qui viene visualizzato il saldo On-Chain (Bitcoin On-Chain nel Wallet del nodo, simboleggiato da un Anchor ⚓) e il saldo Lightning (le capacità dei canali, simboleggiate da un fulmine Bolt ⚡). Questo vi dà un'idea immediata dei fondi che avete nel On-Chain e nel Fulmine. Se avete diversi conti o canali, assicuratevi di essere su quello giusto (ad esempio, Mainnet vs Testnet).





- **Statistiche chiave:** Il cruscotto può mostrare alcune metriche globali per il nodo, ad esempio il numero di canali aperti, il numero di peer connessi, le tariffe di routing guadagnate (se applicabili), ecc. Si tratta di un riepilogo dell'attività recente e dello stato di salute del nodo.





- **Azioni rapide:** Il dashboard dispone di pulsanti per eseguire rapidamente le operazioni più comuni, senza dover navigare nei menu. Queste azioni rapide includono :





- **Fantasma**: Impostare un Lightning Address personalizzato tramite Amboss.
- **Donazione**: Effettuate una donazione tramite Lightning.
- **Accesso/Accesso**: Collegatevi al vostro account Amboss (Quick Connect) e andate direttamente su Amboss.space per visualizzare le informazioni sul vostro nodo.
- **Address**: Inserire un Lightning Address per effettuare un pagamento.
- **Apri**: Apre un nuovo canale Lightning. Facendo clic si apre un modulo per l'inserimento dell'URI del nodo remoto a cui aprire il canale, dell'importo e, se applicabile, della tariffa massima On-Chain da utilizzare.
- **Decodifica**: Decodificare un Lightning Invoice o LNURL per visualizzare i dettagli prima del pagamento.
- **LNURL**: Elabora gli LNURL per i pagamenti o i prelievi Lightning.
- **Accesso a LnMarkets**: Accedi a LnMarkets per fare trading.



Queste azioni rapide permettono di eseguire le operazioni più frequenti direttamente dalla pagina iniziale, senza dover navigare tra le varie schede del Interface.



In breve, la dashboard di ThunderHub offre una "rapida occhiata" al nodo e consente di eseguire le operazioni più frequenti (invio/ricezione, apertura di un canale) con un solo clic. È il punto di partenza ideale per l'amministrazione quotidiana.



### Cruscotto



La sezione **Dashboard** è separata dalla scheda Home e offre un dashboard più avanzato e personalizzabile. Questa sezione consente di creare una vista personalizzata con widget specifici in base alle proprie esigenze di operatore del nodo.





- **Widget personalizzabili:** A differenza della Home page, che ha un layout fisso, la Dashboard consente di scegliere esattamente quali Elements visualizzare e come organizzarli.



![Dashboard sans widgets activés](assets/fr/06.webp)



Se non ci sono widget abilitati, verrà visualizzato un messaggio "Nessun widget abilitato!" con un pulsante "Impostazioni" per accedere ai parametri di personalizzazione.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Nelle impostazioni è possibile scegliere tra un'ampia gamma di widget organizzati in categorie: "Lightning - Info", "Lightning - Tabella", "Lightning - Grafico" e così via. Ogni widget può essere attivato o disattivato individualmente con i pulsanti "Mostra/Nascondi".



![Bas de la page des paramètres](assets/fr/08.webp)



In fondo alle impostazioni, si trova il pulsante "Alla dashboard" per tornare alla dashboard e il pulsante "Reimposta widget" per reimpostare la visualizzazione predefinita.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Una volta configurata, la dashboard può visualizzare vari grafici e metriche: Grafici dei pagamenti lampo, numero di fatture emesse, statistiche sugli inoltri, saldi dettagliati, ecc.





- **Metriche avanzate:** Accesso a statistiche più dettagliate sulle prestazioni del nodo, con grafici e dati in tempo reale.





- **Panoramica configurabile:** Il display può essere adattato alle esigenze di un utente occasionale o di un operatore professionale che gestisce più canali di routing.





- **Interface modulare:** Aggiungete o rimuovete i widget a seconda delle necessità: grafici in avanti, metriche di liquidità, avvisi sullo stato di salute dei nodi, ecc.



Questa sezione è particolarmente utile per gli utenti avanzati che desiderano monitorare metriche specifiche o ottenere una panoramica più tecnica del proprio nodo Lightning. È complementare alla sezione Home, in quanto offre maggiore flessibilità e controllo sulla visualizzazione delle informazioni.



### Coetanei



La sezione **Peers** elenca tutti i nodi Lightning attualmente connessi al proprio come peer. Un **peer** è una connessione diretta da nodo a nodo sul Lightning Network. Il vostro nodo può essere connesso a peer anche senza un canale aperto (ad esempio, solo per ricevere informazioni di gossip sul Exchange), oppure, naturalmente, ogni canale aperto implica automaticamente un peer connesso.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Nella scheda Peers, si vedrà :





- **Colonne informative:** Il Interface visualizza dettagli utili come lo stato di sincronizzazione, il tipo di connessione (clearnet o Tor), il ping, i satoshis ricevuti/inviati e il volume dei dati scambiati.
- Aggiungere un peer: ThunderHub consente di connettersi manualmente a un nuovo peer tramite il pulsante **"Aggiungi"** nell'angolo in alto a destra. È necessario inserire l'URI del nodo (formato `<public_key>@<socket>`). Una volta convalidato, ThunderHub invia il comando corrispondente `lncli connect`. Se il nodo è online e accessibile, verrà aggiunto all'elenco dei peer.



### Canali



La scheda **Canali** è il cuore della gestione dei canali di Lightning. È probabilmente la sezione che consulterete più spesso. Presenta **tutti i canali Lightning** con i relativi dettagli e consente di eseguire azioni di gestione su questi canali.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Ecco cosa troverete nella pagina Canali:





- **Visualizzazione dell'elenco dei canali:** Ogni canale aperto (o che si apre/chiude) viene elencato, di solito con l'alias del nodo remoto, la capacità totale del canale e una barra colorata che illustra la distribuzione della liquidità locale rispetto a quella remota. ThunderHub utilizza un codice colore (spesso blu/Green) o una percentuale per indicare l'equilibrio del canale: ad esempio, blu per la quota locale, Green per la quota remota. Se un canale è perfettamente bilanciato (50/50), la barra sarà la metà di ciascun colore. In questo modo è possibile identificare a colpo d'occhio quali canali sono sbilanciati (tutti blu = quasi tutti locali, tutti Green = quasi tutti remoti).





- **Colonne informative:** Il Interface visualizza colonne dettagliate tra cui Stato, Azioni disponibili, Informazioni sul peer, ID canale, Capacità, Attività, Tariffe e Saldo con visualizzazione grafica della liquidità.





- **Configurazione del display:** Una rotella dentata nell'angolo in alto a destra consente di personalizzare la visualizzazione dei canali in base alle proprie preferenze.





- **Stato:** Vedrete anche degli indicatori di stato - ad esempio `Active` (il canale è aperto e operativo), `Offline` (il peer è disconnesso, quindi il canale è momentaneamente inutilizzabile), `Pending` (per aperture o chiusure in attesa di conferma da parte di On-Chain).





- **Azioni su un canale:** Per ogni canale, ThunderHub fornisce pulsanti di azione (spesso sotto forma di icone):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Modifica delle tariffe:** La funzione Interface "Aggiorna politica del canale" consente di regolare tutti i parametri del canale: Tariffa base, Tariffa (in ppm), Delta CLTV, HTLC massimo e HTLC minimo. In questo modo è possibile regolare le politiche tariffarie individualmente per ogni canale, con l'obiettivo di attirare (o scoraggiare) il traffico di routing. *(Nota: ThunderHub non sostituisce uno strumento di gestione automatica delle tariffe, ma per la regolazione manuale è molto efficace)*
- Canale di chiusura (**Chiusura**): Il "Canale di chiusura" del Interface consente di scegliere tra una chiusura **cooperativa** (predefinita) o una chiusura **forzata** (*Force Close*) definendo le spese (in Sats/vByte). **Importante:** preferire sempre la chiusura cooperativa, quando possibile, per evitare ritardi di regolamento On-Chain e commissioni più elevate. ThunderHub vi dirà se il peer è online (con possibilità di cooperazione) o meno. In caso di chiusura forzata, assicurarsi di confermare, poiché è irreversibile e innesca una transazione a tappeto con un blocco temporale (generalmente 144 blocchi o ~1 giorno su Bitcoin Mainnet).
- **Aprire un nuovo canale:** Per aprire un nuovo canale, fare clic sulla ruota dentata in alto a destra della pagina Canali, quindi selezionare "Apri". A questo punto è possibile avviare un canale verso un nuovo interlocutore o un interlocutore esistente. Il vantaggio di utilizzare questa pagina è quello di avere davanti a sé un elenco dei canali esistenti, che può aiutare a decidere dove aprire un nuovo canale.



In breve, la sezione Canali vi offre un **controllo preciso su ogni canale**. È qui che si gestisce l'allocazione della liquidità, si decide quali canali mantenere o chiudere e si impostano i parametri di instradamento per canale. ThunderHub offre un chiaro Interface per queste operazioni cruciali di gestione dei nodi.



### Riequilibrio



La scheda **Rebalance** è dedicata al **bilanciamento dei canali**. Il bilanciamento (o *ribilanciamento*) consiste nel riaggiustare la distribuzione dei fondi tra i vostri canali in uscita e in entrata, effettuando un **pagamento circolare** da uno dei vostri canali a un altro dei vostri canali, attraverso il Lightning Network. Questo vi permette, senza apportare nuovi fondi, di spostare la liquidità da un canale troppo pieno a uno troppo vuoto, rendendo i vostri canali più utili (un canale bilanciato può sia inviare che ricevere pagamenti).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub facilita notevolmente questa operazione, che altrimenti risulterebbe noiosa alla riga di comando. Ecco come utilizzare la sezione Riequilibrio:





- **Visualizzazione iniziale dei canali:** Entrando in Rebalance, ThunderHub visualizza un elenco dei canali, con un indicatore di bilanciamento per ciascuno di essi (simile a quello presente nella pagina Canali). È possibile vedere subito quali canali sono sbilanciati. ThunderHub può ordinare i canali in ordine crescente di bilanciamento, in modo che i canali più sbilanciati si trovino in cima all'elenco (0,0 significa interamente locale o remoto).





- **Selezione dei peer:** Il Interface consente di selezionare facilmente i peer in uscita e in entrata per il ribilanciamento.





- **Impostazioni dei parametri:** È possibile impostare :
  - La **tassa massima** (in Sats e ppm) che si è disposti a pagare
  - L'**importo da riequilibrare** con l'opzione "Fisso" o "Target"
- **Nodi da evitare** durante l'instradamento
- **Tempo massimo di prova** per la ricerca del percorso





- Selezionare il canale **fonte**: Selezionare innanzitutto il canale **in uscita (sorgente)**, ovvero il canale dal quale si ha troppa liquidità locale da spostare. In pratica, si tratta di un canale in cui la quota locale è elevata (> 50%). Immaginiamo un canale A con 1.000.000 di Satss, di cui 900.000 locali: un buon candidato per inviare Satss altrove. Facendo clic su questo canale A come "in uscita", ThunderHub lo contrassegna come sorgente.





- Scegliere **canale target**: Successivamente, scegliere il **canale in entrata (target)** che deve ricevere liquidità. In genere, si tratta di un canale in cui la situazione è opposta: la maggior parte dei fondi si trova sul lato opposto (ad esempio, solo 100.000 Satss locali su 1.000.000). ThunderHub, una volta selezionato il canale sorgente, ordinerà gli altri canali in ordine inverso (equilibrio decrescente) per aiutare a identificare i canali più complementari. Selezionate un canale B che abbia spazio sul lato locale. ThunderHub visualizzerà chiaramente i due canali selezionati (sorgente A e destinazione B).





- Impostare l'importo della tassa e la tolleranza: Un modulo consente di inserire :





  - La **quota** da riequilibrare (in Sats). Spesso si sceglie una quantità pari a quella che bilancerebbe entrambi i canali a \~50/50. ThunderHub può pre-compilare metà della capacità in eccesso del canale sorgente, ad esempio.
  - Il **compenso massimo** che si è disposti a pagare per questa operazione (opzionale). Questa tariffa è espressa in Sats (costo totale dell'instradamento circolare). Se si lascia vuoto, ThunderHub cercherà un percorso indipendentemente dal costo, cosa che in genere non è consigliabile (è meglio impostare un limite, ad esempio 10 Sats per un piccolo riequilibrio, o un massimo di ppm).





- **Trova percorso:** Fare clic sul pulsante per trovare un percorso. ThunderHub interroga il LND per calcolare un percorso dal canale di origine attraverso la rete al canale di destinazione. Se trova un percorso possibile che soddisfa i criteri di tariffazione, lo visualizza con i dettagli dei passaggi e il costo della tariffa. Ad esempio, potrebbe indicare che ha trovato un percorso a 3 hop con un totale di 2 Sats a pagamento.





- Avviare il ribilanciamento: Se si è soddisfatti del percorso proposto, fare clic su **Canale di ribilanciamento**. ThunderHub avvierà quindi il pagamento circolare tramite LND. Se il pagamento va a buon fine, verrà visualizzata una notifica di successo e i canali A e B vedranno modificati i loro saldi in tempo reale. ThunderHub aggiornerà l'indicatore di saldo di questi canali (idealmente sarà più verde di prima, a indicare un saldo migliore).





- **Regolazioni e iterazioni:** Se non viene trovato un percorso al primo tentativo (o se è troppo costoso), è possibile regolare i parametri :





  - Provate con una quantità minore (a volte un ribilanciamento parziale va a buon fine, mentre una quantità maggiore fallisce).
  - Aumentate gradualmente la tariffa massima, ma fate attenzione a non pagare più tasse di quanto valga.
  - Utilizzare il pulsante **Aggiungi un altro percorso**, se disponibile, per provare un'alternativa.
  - Provate un'altra coppia di canali se le cose si fanno davvero difficili.



ThunderHub rende il processo molto **intuitivo e visivo**. In soli 4 passaggi (selezionare il canale in uscita, selezionare il canale in entrata, importo, convalida), è possibile fare ciò che prima richiedeva complessi comandi manuali. Lo strumento è prezioso per mantenere un nodo ben bilanciato, migliorare le prestazioni e l'esperienza di routing (è più facile inviare e ricevere pagamenti su tutti i canali).



Infine, si noti che un ribilanciamento consuma i costi di instradamento (pagati ai nodi intermedi), quindi è un **investimento** per rendere il nodo più fluido. Utilizzatelo con saggezza, ad esempio per supportare un canale verso un servizio che utilizzate spesso (liquidità in entrata) o per bilanciare un canale di routing di grandi dimensioni. ThunderHub vi permette di farlo in modo **semplice ed efficiente**.



### Transazioni



La sezione **Transazioni** di ThunderHub corrisponde alla cronologia delle transazioni **Lightning** del vostro nodo, cioè ai pagamenti e alle fatture pagate o ricevute tramite i canali. Si tratta di una sorta di estratto conto per le operazioni LN.



![Historique des transactions Lightning](assets/fr/14.webp)



In questa scheda sono presenti :





- **Grafico Invoice:** Nell'angolo in alto a destra, un grafico mostra l'evoluzione delle fatture ricevute nel tempo, consentendo di visualizzare l'attività del nodo.





- Un elenco cronologico di tutte le transazioni Lightning effettuate *da* o *a* del vostro nodo. Ogni voce può mostrare :





  - Tipo di operazione: **invio di pagamento** (pagamento in uscita) o **ricezione di pagamento** (in entrata, tramite un Invoice pagato).
  - L'importo in Sats.
  - Data/ora.
  - ID pagamento (pre-immagine Hash o RHash) o commento (se si è aggiunto un promemoria al Invoice).
  - Stato: **completato**, o eventualmente **in corso**/*inadempiuto* (ad esempio un pagamento in attesa di risoluzione, ma in genere LND lo elabora rapidamente, quindi c'è poco "in sospeso" rispetto alle transazioni On-Chain).



In breve, la sezione Transazioni serve come registro delle attività del **LN**. È molto utile per verificare se un pagamento è andato a buon fine, quante commissioni è costato o per tracciare la storia dei vostri scambi Lightning. Insieme alla sezione Inoltri (descritta di seguito), avrete una visione completa del denaro che è passato attraverso il vostro nodo.



### Attaccanti



La scheda **Forwards** è dedicata all'attività di **routing** del vostro nodo, cioè ai pagamenti che **transitano** attraverso i vostri canali (quando agite come nodo intermediario sul Lightning Network). Se si opera come nodo di instradamento, questa è una sezione importante per monitorare le proprie prestazioni.



![Statistiques de routage Lightning](assets/fr/15.webp)



In Forward, ThunderHub presenta :





- **Filtri e opzioni di visualizzazione:** In alto a destra, i filtri consentono di ordinare i dati per giorno/settimana/mese/anno e di scegliere tra visualizzazione grafica o tabellare.





- **Messaggio di attività:** Se non è stato eseguito alcun instradamento durante il periodo selezionato, il Interface visualizza "Nessun inoltro per questo periodo", come mostrato in questo esempio.





- Una **tabella di inoltri recenti**: ogni voce corrisponde a un pagamento che è stato **inoltrato** attraverso il vostro nodo. Per ogni inoltro, in genere si vede :





  - Timestamp,
  - la quantità instradata (in Sats),
  - il **fee guadagnato** su questo inoltro (in Sats, è la differenza tra quanto ricevuto sul canale in entrata e inviato su quello in uscita),
  - i canali in entrata e in uscita utilizzati (spesso identificati dall'alias del peer o dall'ID del canale).
  - stato (normalmente *completato*, o fallimento se un inoltro è fallito durante il percorso).





- **Statistiche aggregate**: ThunderHub calcola e visualizza nella parte superiore della pagina i totali e le statistiche relative a un determinato periodo (ad esempio, le ultime 24 ore, o 7 giorni, ecc.)



In breve, la sezione Inoltri offre una **riepilogo in tempo reale dell'attività di instradamento del nodo Lightning**. Abbinata alle sezioni Canali e Riequilibrio, costituisce un pacchetto completo per l'ottimizzazione del nodo: Canali/Rebalance per la liquidità, Forwards per l'osservazione dei risultati (flussi e profitti).



### Catena



La sezione **Catena** corrisponde alla gestione del portafoglio Bitcoin On-Chain del vostro nodo LND. Questo Interface consente di visualizzare e gestire i fondi Bitcoin, che vengono utilizzati per aprire canali o ricevere fondi da canali chiusi.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Nella Catena, troverete :





- Saldo On-Chain: **Visualizza il saldo totale di BTC disponibile in Wallet LND.**





- **Elenco degli UTXO:** Visualizza tutte le uscite non spese (UTXO) con importo, conferme, Address e formato per ciascuna uscita.





- **Cronologia delle transazioni:** Tabella dettagliata di tutte le transazioni Bitcoin con tipo (entrata/uscita), data, importo, spese, conferme, blocco di inclusione, indirizzi e txid.



### Amboss



ThunderHub si integra con la piattaforma **Amboss** (amboss.space), che offre informazioni dettagliate sui nodi Lightning, un mercato della liquidità e utili funzioni come il backup dei canali criptati e il monitoraggio della disponibilità.



![Intégration Amboss avec ses options](assets/fr/17.webp)



In ThunderHub, la sezione Amboss consente di **collegare** il nodo al proprio account Amboss:





- **Ghost Address:** Impostare un **Lightning Address** personalizzato per il proprio nodo, per facilitare i pagamenti in entrata.





- Backup automatico dei canali:** Funzione di punta per i backup criptati dei canali** (file SCB) su Amboss. Attivate **Amboss Auto Backup = Yes** nelle impostazioni per inviare automaticamente gli aggiornamenti dei backup criptati ogni volta che cambiate canale. In caso di guasto, sarete in grado di recuperare i vostri fondi grazie a questo backup esterno.





- Controlli di salute: Attivare **Amboss Healthcheck = Yes** per far sì che il nodo invii regolarmente ping ad Amboss. Si riceveranno avvisi se il nodo sembra essere offline.





- **Altre caratteristiche:** Push automatico del saldo, integrazione **Magma/Hydro** (mercato della liquidità) e accesso a statistiche dettagliate sulle prestazioni.



L'integrazione di Amboss aggiunge una **sicurezza Layer** essenziale con il monitoraggio automatico del backup esterno e della disponibilità, accessibile direttamente da ThunderHub.



### Strumenti



La sezione **Strumenti** raggruppa vari strumenti avanzati per la gestione del nodo. Ecco i principali Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Backup:** Gestisci manualmente i backup dei tuoi canali (SCB). ThunderHub vi permette di **scaricare il file di backup** completo dei vostri canali (opzione "Backup di tutti i canali -> Download"). Conservate questo file `channel-all.bak` in un luogo sicuro: è essenziale per recuperare i vostri fondi in caso di crash. È anche possibile **importare** un file di backup quando si rialloca un nodo.





- **Contabilità:** Strumento di esportazione per i rapporti finanziari, compresi i compensi guadagnati/pagati e i volumi instradati in un determinato periodo.
- **Messaggi firmati:** Firmare o verificare i messaggi con il proprio nodo per dimostrare Ownership del proprio nodo Lightning tramite firma crittografica.
- Macaron (sezione Bakery):** Gestire i macaron LND** per creare accessi personalizzati. Il Interface "Bakery" consente di selezionare con precisione ogni permesso: "Aggiungere o rimuovere Peer", "Creare indirizzi di catena", "Creare fatture", "Creare macaron", "Derivare chiavi", "Ottenere chiavi di accesso", "Ottenere transazioni di catena", "Ottenere fatture", "Ottenere informazioni Wallet", "Ottenere pagamenti", "Ottenere Peer", "Pagare fatture", "Revocare ID di accesso", "Inviare a indirizzi di catena", "Firmare byte", "Firmare messaggi", "Fermare daemon", "Verificare firma byte", "Verificare messaggi" e così via. Ogni permesso può essere attivato singolarmente con i pulsanti "Sì/No" per creare un macaron su misura.
- **Informazioni di sistema:** Visualizzazione della versione di Wallet e degli RPC attivati.



In breve, la sezione Strumenti riunisce le funzioni di amministrazione avanzate - backup, contabilità, sicurezza e gestione degli accessi - in un Interface unificato.



### Scambio



La scheda **Swap** di ThunderHub consente di scambiare i satoshi Lightning con Bitcoin On-Chain tramite il servizio Boltz. Questa funzione è utile per "scaricare" la liquidità in eccesso di Lightning sul canale senza chiudere un canale.



![Interface de swap via Boltz](assets/fr/19.webp)



Il processo è semplice:





- **Importo**: Definire l'importo da scambiare
- **Address**: Immettere la ricezione Bitcoin Address
- **Esecuzione**: ThunderHub comunica con Boltz per elaborare automaticamente il Exchange



**Vantaggi:**




- Servizio non custodiale (senza custodia in contanti)
- Preservare i canali esistenti
- Interface integrato facile da usare



Boltz addebita una piccola commissione e l'utente paga la commissione di transazione standard Bitcoin. ThunderHub visualizza tutti i costi prima della conferma.



### Statistiche



La sezione **Stats** di ThunderHub offre **statistiche avanzate** sul nodo Lightning per analizzare le prestazioni e ottimizzare il routing.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Questa sezione è essenziale per ottimizzare i costi, identificare i canali di successo e pianificare l'espansione del nodo.



## Conclusione



**ThunderHub** si è affermato come lo strumento essenziale per una facile amministrazione di un nodo Lightning **LND**. Questo moderno Interface offre tutte le funzioni essenziali: gestione dei canali, pagamenti, monitoraggio, con caratteristiche avanzate come il ribilanciamento automatico e l'integrazione con Amboss.



**Benefici chiave:**




- Interface elegante e intuitivo
- Strumenti potenti (ribilanciamento, swap di Boltz, backup automatici)
- Compatibile con Umbrel, Voltage, RaspiBlitz e altre distribuzioni



ThunderHub democratizza la gestione avanzata dei nodi Lightning, rendendo accessibile ciò che prima richiedeva complessi comandi tecnici. Che siate principianti o operatori esperti, ThunderHub vi permette di gestire in modo efficiente il vostro nodo Lightning tramite un Interface moderno e completo.



## Risorse



**Link ufficiali:**




- **Sito ufficiale:** [thunderhub.io](https://thunderhub.io)
- **Documentazione:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Codice sorgente GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)