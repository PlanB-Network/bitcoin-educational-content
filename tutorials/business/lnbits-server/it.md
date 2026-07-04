---
name: LNbits Server
description: Installazione e configurazione di un server LNbits self-hosted su Ubuntu VPS con Phoenixd o su Umbrel
---

![cover](assets/cover.webp)

LNbits è un'interfaccia web open source che trasforma qualsiasi backend Lightning (LND, Core Lightning, Phoenixd) in una piattaforma di servizi completa. Questa soluzione self-hosted consente di gestire più wallet Lightning in modo isolato, distribuire punti vendita, creare sistemi di donazione o servizi di fatturazione, mantenendo il controllo totale sui fondi.

Questo tutorial copre due approcci all'installazione: **VPS Ubuntu con Phoenixd** (soluzione leggera senza un nodo Bitcoin completo) e **Umbrel** (integrazione con il nodo LND esistente). A differenza del tutorial generale di Plan ₿ Academy su LNbits, che tratta i concetti e le estensioni, questa guida si concentra sulle procedure tecniche di installazione passo dopo passo.


## Che cos'è LNbits?

LNbits è un sistema di contabilità Lightning sviluppato in Python (FastAPI) che si collega a un backend esistente (LND, Core Lightning, Phoenixd). A differenza dei nodi Lightning tradizionali, LNbits offre un'interfaccia accessibile per la gestione di diversi portafogli isolati con le proprie chiavi API. È possibile creare sottoconti per la famiglia, i dipendenti o i progetti, senza dare loro accesso a tutti i fondi.

L'architettura disaccoppiata memorizza le informazioni in SQLite (default) o PostgreSQL (produzione), mentre i fondi rimangono gestiti dal backend Lightning. Questa separazione garantisce la portabilità: potete migrare da Phoenixd a LND senza perdere i dati degli utenti.


## Caratteristiche principali

LNbits offre un versatile **sistema di estensione**: TPoS (punto vendita), Paywall (monetizzazione dei contenuti), Eventi (biglietteria), LndHub (server per BlueWallet), Bolt Cards (pagamenti NFC), Split Payments (distribuzione automatica) e User Manager (gestione utenti con autenticazione).

La **dashboard** visualizza i saldi in tempo reale, lo storico delle transazioni e gli strumenti di fatturazione. Ogni wallet ha un URL unico che contiene le chiavi API, consentendo l'accesso senza un login tradizionale. **Il sistema di chiavi API a tre livelli** (amministratore, invoice, sola lettura) offre un controllo granulare delle autorizzazioni per integrazioni sicure.

LNbits implementa nativamente **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) e supporta **Lightning Address**, garantendo la compatibilità con i moderni wallet Lightning, facilitando la distribuzione di servizi professionali.


## Piattaforme supportate

**Ubuntu VPS**: soluzione leggera senza nodo Bitcoin completo. Prerequisiti: 1 vCPU, 1-2 GB di RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nome di dominio richiesto per l'esposizione pubblica (servizi LNURL).

**Umbrel**: Facile installazione dall'App Store. Prerequisito: nodo Umbrel funzionante con LND sincronizzato e canali aperti. Configurazione automatica.

Di seguito sono riportati i link alle nostre esercitazioni su Umbrel e Umbrel LND:

https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


## Installazione su Ubuntu VPS con Phoenixd

### Passo 1: Protezione del server VPS

**Prima di qualsiasi installazione**, è necessario proteggere il server VPS Ubuntu secondo le regole dell'arte. Questo passo è **critico** per proteggere la tua infrastruttura e i tuoi fondi Lightning.

Ecco una guida dettagliata per aiutarvi a iniziare: **[Configurazione iniziale del server Ubuntu - Guida passo-passo](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** di Daniel P. Costas.

Questa guida tratta la configurazione degli utenti, l'SSH sicuro, il firewall (UFW), fail2ban, gli aggiornamenti automatici e le buone pratiche di sicurezza del sistema.

### Passo 2: Installazione di Phoenixd

Una volta che il server è sicuro, è necessario installare e configurare Phoenixd. Plan ₿ Academy offre un tutorial completo che copre l'installazione, la generazione di seed e la configurazione del servizio systemd:

https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Una volta che Phoenixd è attivo e funzionante (verifica con `./phoenix-cli getinfo`), prendi nota della **password HTTP** in `~/.phoenix/phoenix.conf`: ti servirà per collegare LNbits a Phoenixd.

### Distribuzione di LNbits

Installa UV e clona LNbits :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```

Configura il backend Phoenixd:

```bash
cp .env.example .env && nano .env
```

Aggiungi a `.env` :

```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```

Esegui il test con `uv run lnbits --host 0.0.0.0 --port 5000` e crea un servizio systemd con `Wants=phoenixd.service`.


## Configurazione iniziale e primo utilizzo

### Attivazione del SuperUser

Attiva l'interfaccia amministratore in `.env`:

```
LNBITS_ADMIN_UI=true
```

Riavvia LNbits (`sudo systemctl restart lnbits`) e recupera l'ID SuperUser:

```bash
cat ~/lnbits/data/.super_user
```

Vai a `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` per il pannello di amministrazione. Il menu "Server" consente di configurare le fonti di finanziamento, le estensioni e gli account utente.

### Creazione sicura dell'account

**Importante per l'esposizione pubblica**: se stai esponendo la tua istanza LNbits su un dominio pubblico accessibile da Internet, è **critico** disabilitare la creazione gratuita di account utente.

Dall'interfaccia di amministrazione di SuperUser, vai su "Impostazioni" e poi sulla sezione "Gestione utenti". Lì troverai l'opzione "Consenti la creazione di nuovi utenti".

![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)

**Per un'esposizione pubblica con nome di dominio**:
- **È necessario disabilitare** l'opzione "Consenti la creazione di nuovi utenti".
- Senza questa protezione, chiunque su Internet può creare un account sulla tua istanza.
- Un utente malintenzionato potrebbe creare account e utilizzare la liquidità del tuo nodo Lightning a tua insaputa.
- È necessario creare manualmente gli account utente dall'interfaccia SuperUser.

**Solo per uso locale**:
- Questa opzione è meno critica se l'istanza è accessibile solo localmente (http://localhost:5000).
- Tuttavia, disabilitare questa opzione è una buona pratica di sicurezza generale.

Una volta configurato, solo l'amministratore SuperUser può creare nuovi account utente tramite l'interfaccia "Utenti". Questo approccio garantisce un controllo totale su chi può accedere alla tua infrastruttura Lightning e utilizzare i tuoi fondi.

### Apertura del primo canale

Phoenixd gestisce automaticamente i canali tramite l'autoliquidazione. Genera un'invoice Lightning di ~30.000 sats da LNbits e pagala da un altro wallet. Phoenixd apre automaticamente un canale verso ACINQ. La commissione di apertura (~20-23k sats) viene detratta, il saldo restante (~7-10k sats) appare dopo la conferma on-chain.

Controlla lo stato con `./phoenix-cli getinfo`. Considera poi la possibilità di disabilitare l'autoliquidità (`auto-liquidity=off` in `phoenix.conf`) per controllare le aperture dei canali.

### Visualizzazione pubblica e HTTPS

**Importante**: HTTPS obbligatorio per la visualizzazione pubblica (sicurezza della chiave API + compatibilità con LNURL). Salta questo passaggio solo per l'uso locale.

**Caddy (consigliato)**: SSL automatico. `sudo apt install -y caddy`, modificare `/etc/caddy/Caddyfile` :

```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```

Riavvia: `sudo systemctl restart caddy`.

**Nginx**: Più controllo. Installa `nginx certbot python3-certbot-nginx`, crea `/etc/nginx/sites-available/lnbits` :

```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```

Attiva: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`

Aggiungi a `.env`: `FORWARDED_ALLOW_IPS=*`


## Installazione su Umbrel

### Distribuzione da App Store

Vai sull'App Store Umbrel, cerca "LNbits" e fa clic su "Installa".

![Installation LNbits Umbrel](assets/fr/01.webp)

Umbrel controlla automaticamente le dipendenze necessarie. Per funzionare, LNbits richiede Lightning Node (LND). Se il tuo nodo Lightning è già operativo, fai clic su "Installa LNbits" per confermare.

![Dépendances LNbits](assets/fr/02.webp)

Umbrel scarica l'immagine Docker, configura automaticamente le connessioni con LND e avvia il contenitore (2-5 minuti). L'installazione avviene interamente in background.

### Configurazione iniziale del SuperUser

Al primo avvio, LNbits chiede di creare l'account amministratore SuperUser. Immetti un nome utente e una password sicura per proteggere l'accesso all'interfaccia di amministrazione.

![Configuration SuperUser](assets/fr/03.webp)

**Importante**: questo account SuperUser ha pieni privilegi sulla tua istanza LNbits. Scegli una password forte e tienila al sicuro.

Una volta creato un account, accedi automaticamente all'interfaccia di amministrazione principale. Umbrel ha già impostato LND come fonte di finanziamento: tutti i pagamenti di Lightning passeranno attraverso i canali esistenti.

### Accesso all'interfaccia amministratore

Nel menu a sinistra, fai clic su "Impostazioni" per accedere al pannello di amministrazione completo.

![Interface Settings](assets/fr/04.webp)

La sezione "Gestione dei wallet" visualizza le informazioni principali sulla configurazione:
- **Fonte di finanziamento** : LndBtcRestWallet (connessione diretta al proprio nodo LND Umbrel).
- **Saldo del nodo** : liquidità totale disponibile nei canali Lightning.
- Saldo LNbits**: fondi assegnati al sistema LNbits (inizialmente 0 sats).

Ora puoi sfruttare direttamente la liquidità del tuo nodo Umbrel per tutti i wallet LNbits che crei. Non è necessaria alcuna configurazione aggiuntiva: LNbits è già operativo.

### Gestione degli utenti

Una delle caratteristiche più potenti di LNbits è la possibilità di creare più utenti indipendenti, ciascuno con autenticazione tramite password e wallet isolati. Questa architettura consente di sfruttare la liquidità del nodo Umbrel, offrendo al contempo sottoconti totalmente isolati per usi diversi: affari, famiglia, dipendenti, progetti, ecc.

Nel menu laterale, clicca su "Utenti" per accedere alla gestione degli utenti. Cliccare su "CREA ACCOUNT" per aggiungere un nuovo utente.

![Gestion des utilisateurs](assets/fr/05.webp)

Compila il modulo di creazione dell'utente:
- **Nome utente**: nome utente (esempio: "satoshi").
- **Imposta password**: attiva questa opzione per impostare una password di autenticazione.
- **Password** e **Password repeat**: imposta la password per questo utente.

![Création utilisateur satoshi](assets/fr/06.webp)

I campi opzionali (chiave pubblica Nostr, e-mail, nome e cognome) possono essere lasciati vuoti per una configurazione minima. Fai clic su "CREA ACCOUNT" per confermare.

![Confirmation utilisateur créé](assets/fr/07.webp)

Il nuovo utente appare ora nell'elenco degli utenti con il suo identificativo unico e il suo nome utente.

![Liste des utilisateurs](assets/fr/08.webp)

**Nota bene**: ogni utente può accedere in modo completamente indipendente con la propria password. L'amministratore SuperUser mantiene il pieno controllo attraverso l'interfaccia di amministrazione.

### Gestione wallet dell'utente

Ora che l'utente "satoshi" è stato creato, è necessario assegnargli un wallet Lightning. Fai clic sull'icona wallet (seconda icona) dell'utente in questione, quindi su "CREA NUOVO PORTAFOGLIO".

![Gestion des wallets](assets/fr/09.webp)

Una finestra di dialogo chiede di assegnare un nome al wallet. Inserisci un nome descrittivo (ad esempio "Wallet di Satoshi") e selezionare la valuta di visualizzazione (CUC, USD, EUR, ecc.).

![Création wallet](assets/fr/10.webp)

Fai clic su "CREA". LNbits genera immediatamente un wallet Lightning funzionante per questo utente.

![Confirmation wallet créé](assets/fr/11.webp)

Ora si vedono i due wallet esistenti: il wallet predefinito "LNbits wallet" creato automaticamente e il nuovo "Wallet Of Satoshi". Per semplificare l'esperienza dell'utente, è possibile eliminare il wallet predefinito facendo clic sull'icona di eliminazione (cestino rosso).

![Wallet final unique](assets/fr/12.webp)

L'utente "satoshi" ha ora un unico wallet chiaramente identificato. Ogni utente wallet opera in modo completamente autonomo, pur utilizzando la liquidità del nodo LND sottostante.

**Concetto chiave**: tutti questi wallet condividono la liquidità globale del tuo nodo Umbrel. Non si creano nuovi canali Lightning per ogni wallet: LNbits agisce come un livello di contabilità intelligente che gestisce l'allocazione dei fondi all'interno della tua infrastruttura Lightning esistente. Questa è la potenza del sistema multi-wallet di LNbits.

### Accesso utente

Esci dall'account SuperUser (icona in alto a destra) e tornare alla pagina di login di LNbits. Ora è possibile accedere con le credenziali del nuovo utente.

![Connexion utilisateur satoshi](assets/fr/13.webp)

Inserisci il nome utente ("satoshi") e la password precedentemente definiti, quindi fai clic su "LOGIN". L'utente accede direttamente al suo wallet personale, totalmente isolato dall'interfaccia di amministrazione.

### Interfaccia dall'utente wallet

Una volta effettuato il login, l'utente accede all'interfaccia completa di wallet Lightning.

![Interface wallet utilisateur](assets/fr/14.webp)

Le caratteristiche dell'interfaccia:
- **Saldo corrente**: visualizzato in sats e nella valuta scelta (CUC in questo esempio).
- **Azioni principali**: INCOLLA RICHIESTA, CREA INVOICE, icona QR (scansione rapida).
- **Cronologia delle transazioni** : elenco completo di tutti i pagamenti e le ricevute.
- **Pannello laterale destro**: opzioni di configurazione e accesso.

### Accesso mobile al wallet

Il pannello laterale destro offre una funzione particolarmente pratica: l'accesso mobile al wallet. Aprite la sezione "Accesso mobile" per scoprire le opzioni disponibili.

![Mobile Access](assets/fr/15.webp)

LNbits offre diversi modi per utilizzare questo wallet su uno smartphone:

**Opzione 1: applicazioni mobili compatibili**

- Scarica **Zeus** o **BlueWallet** dall'App Store o da Google Play.
- Attiva l'estensione **LndHub** in LNbits per questo wallet.
- Scansiona il codice QR LndHub con l'applicazione mobile per collegare il wallet.

**Opzione 2: accesso diretto tramite browser mobile**

- Il codice QR visualizzato in "Esportazione su telefono con codice QR" contiene l'URL completo del wallet con autenticazione integrata
- Scansionate questo codice QR dal vostro smartphone per aprire il wallet direttamente nel vostro browser mobile
- Aggiungere una pagina alla schermata iniziale per un accesso rapido

**Importante per la sicurezza**: questo URL contiene le chiavi del API per l'accesso completo al wallet. Non condividetelo mai pubblicamente. Tratta questo codice QR come le tue chiavi private Bitcoin: chiunque esegua la scansione di questo codice QR otterrà l'accesso completo al wallet.

Questa funzione mobile trasforma la tua istanza LNbits Umbrel in un vero e proprio server Lightning wallet per te e i tuoi amici, mantenendo la completa sovranità sui tuoi fondi grazie al tuo nodo self-hosted.

### Condivisione dell'accesso degli utenti

Il caso d'uso principale di questa configurazione multiutente è la **condivisione dei wallet con la famiglia o la cerchia ristretta**. Una volta creato un utente con un wallet dedicato (come "satoshi" nel nostro esempio), è possibile condividere le credenziali di accesso con i membri fidati della famiglia.

**Sicurezza dell'accesso su Umbrel**: l'accesso alla tua istanza LNbits su Umbrel è naturalmente protetto, in quanto si può accedere in maniera univoca:
- **Sulla rete locale** : i membri del tuo nucleo familiare collegati alla stessa rete WiFi/Ethernet possono accedere all'istanza.
- **Tramite VPN**: se si utilizza una VPN come Tailscale configurata sul server Umbrel, gli utenti autorizzati possono ottenere un accesso remoto sicuro.

Questo doppio livello di protezione (accesso alla rete + autenticazione dell'utente) rende l'opzione "Consenti la creazione di nuovi utenti" meno critica su Umbrel. Solo le persone che hanno già accesso alla rete o alla VPN possono accedere all'interfaccia di login.

**Scenario tipico**: si crea un conto "papà", un conto "mamma", un conto "azienda" e così via. Ogni membro della famiglia ha il proprio Lightning wallet isolato, pur beneficiando della liquidità condivisa del tuo nodo Umbrel. È sufficiente condividere il nome utente e la password: l'utente può connettersi da qualsiasi dispositivo della rete locale o tramite la VPN Tailscale. Per ulteriori informazioni, consultare il nostro tutorial dedicato a Tailscale:

https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Esplora le estensioni disponibili

Torna all'interfaccia SuperUser e accedi al menu "Estensioni" nel pannello laterale sinistro per scoprire l'intero ecosistema di estensioni LNbits.

![Extensions disponibles](assets/fr/16.webp)

LNbits offre un ricco catalogo di estensioni che trasformano la tua istanza in una vera e propria piattaforma di servizi Lightning:
- **Jukebox**: sistema jukebox alimentato da sats (pagamenti Spotify).
- **Biglietti di supporto**: sistema di supporto a pagamento (ricevere sats per rispondere alle domande).
- **TPoS**: terminale mobile e sicuro per i punti vendita al dettaglio.
- **User Manager**: gestione avanzata di utenti e wallet (che abbiamo appena utilizzato).
- **Eventi**: vendita e convalida di biglietti per eventi.
- **Dispositivi LNURLD**: gestione dei punti vendita, ATM, switch collegati.
- **SMTP**: consente agli utenti di inviare email e guadagnare sats.
- **Boltcards**: programmazione di carte NFC per pagamenti Lightning tap-to-pay.
- **NostrNip5**: crea indirizzi NIP5 per i tuoi domini.
- **Pagamenti frazionati**: distribuzione automatica dei pagamenti tra più wallet.

Ogni estensione si attiva con un solo clic da questa interfaccia. Le estensioni contrassegnate con "FREE" sono gratuite, mentre alcune sono disponibili in versione "PAID". Esplora il catalogo per individua quelle che rispondono alle tue esigenze, che si tratti di affari, gestione familiare o sperimentazione delle capacità del Lightning Network.


## Vantaggi e limiti

**Vantaggi**: sovranità finanziaria (controllo totale di fondi/chiavi/dati), flessibilità architettonica (migrazione VPS → full node senza perdite), sistema di estensione professionale, interfaccia intuitiva.

**Limitazioni**: software in versione beta (attenzione alle quantità), sicurezza sotto la responsabilità dell'amministratore, URL contenenti chiavi API sensibili (HTTPS obbligatorio), la gestione multiutente implica una responsabilità di custodia.


## Le migliori pratiche

**Backup**: Phoenixd Seed/LND credenziali, database LNbits, file .env. Automatizza quotidianamente, tieni fuori dal server di produzione, crittografato. Testa regolarmente i ripristini.

**Manutenzione**: controlla regolarmente gli aggiornamenti (LNbits, backend Lightning, sistema operativo). Controlla sempre le note di rilascio prima degli aggiornamenti principali.

- **Su Umbrel**: App Store notifica automaticamente le nuove versioni. Sincronizza le estensioni tramite "Gestione estensioni" > "Aggiorna tutto". Controlla l'inclusione del database SQLite nei backup automatici di Umbrel.
- **Sul VPS**: aggiorna manualmente con `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Monitora i log di sistema: `sudo journalctl -u lnbits -f`.


## Conclusione

LNbits self-hosting offre un percorso concreto verso la sovranità finanziaria di Lightning. VPS+Phoenixd offre una soluzione leggera per servizi veloci, Umbrel piena integrazione con il nodo Bitcoin esistente. L'architettura scalabile consente di passare da semplici wallet multiutente a sofisticati casi d'uso aziendali.

Il self-hosting implica responsabilità: backup dei seed, protezione dell'accesso, inizio con importi modesti. Con queste precauzioni, LNbits diventa una soluzione robusta per l'economia Lightning, preservando al contempo la decentralizzazione e l'autonomia.


## Risorse

### Documentazione ufficiale

- [Documentazione LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Guida ufficiale all'installazione](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)

### Guide della comunità

- [Configurazione iniziale del server Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) di Daniel P. Costas (sicurezza VPS passo dopo passo)
- [Installazione di LNbits + Phoenixd su Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) di Daniel P. Costas (guida completa)
- [Server LNbits su Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) di Axel
- [LNbits su VPS](https://github.com/TrezorHannes/vps-lnbits) di Hannes
