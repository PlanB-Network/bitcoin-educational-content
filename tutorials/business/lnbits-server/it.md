---
name: Server LNbits
description: Installazione e configurazione di un server LNbits self-hosted su Ubuntu VPS con PHOENIXD o su Umbrel
---

![cover](assets/cover.webp)



LNbits è un'applicazione web open source Interface che trasforma qualsiasi backend Lightning (LND, Core Lightning, PHOENIXD) in una piattaforma di servizi completa. Questa soluzione self-hosted consente di gestire più portafogli Lightning in modo isolato, distribuire punti vendita, creare sistemi di donazione o servizi di fatturazione, mantenendo il controllo totale sui fondi.



Questo tutorial copre due approcci all'installazione: **VPS Ubuntu con PHOENIXD** (soluzione leggera senza un nodo Bitcoin completo) e **Umbrel** (integrazione con il nodo LND esistente). A differenza del tutorial generale di Plan B Network su LNbits, che tratta i concetti e le estensioni, questa guida si concentra sulle procedure tecniche di installazione passo dopo passo.



## Che cos'è LNbits?



LNbits è un sistema di contabilità Lightning sviluppato in Python (FastAPI) che si collega a un backend esistente (LND, Core Lightning, PHOENIXD). A differenza dei nodi Lightning tradizionali, LNbits offre un Interface accessibile, che consente di gestire diversi portafogli isolati con chiavi API proprie. È possibile creare sottoconti per la famiglia, i dipendenti o i progetti, senza dare loro accesso a tutti i fondi.



L'architettura disaccoppiata memorizza le informazioni in SQLite (default) o PostgreSQL (produzione), mentre i fondi rimangono gestiti dal backend Lightning. Questa separazione garantisce la portabilità: è possibile migrare da PHOENIXD a LND senza perdere i dati degli utenti.



## Caratteristiche principali



LNbits offre un versatile **sistema di estensione**: TPoS (punto vendita), Paywall (monetizzazione dei contenuti), Eventi (biglietteria), LndHub (server per BlueWallet), Bolt Cards (pagamenti NFC), Split Payments (distribuzione automatica) e User Manager (gestione utenti con autenticazione).



Il **dashboard** visualizza i saldi in tempo reale, lo storico delle transazioni e gli strumenti di fatturazione. Ogni Wallet ha un URL unico che contiene le chiavi API, consentendo l'accesso senza un login tradizionale. Il sistema di chiavi API a tre livelli** (amministratore, Invoice, sola lettura) offre un controllo granulare delle autorizzazioni per integrazioni sicure.



LNbits implementa nativamente **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) e supporta **Lightning Address**, garantendo la compatibilità con i moderni portafogli Lightning e facilitando la distribuzione di servizi professionali.



## Piattaforme supportate



**Ubuntu VPS**: Soluzione leggera senza nodo Bitcoin completo. Prerequisiti: 1 vCPU, 1-2 GB di RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nome di dominio richiesto per l'esposizione pubblica (servizi LNURL).



**Umbro**: Facile installazione dall'App Store. Prerequisito: nodo Umbrel funzionante con LND sincronizzato e canali aperti. Configurazione automatica.



Di seguito sono riportati i link alle nostre esercitazioni su Umbrel e Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installazione su Ubuntu VPS con PHOENIXD



### Passo 1: Protezione del server VPS



**Prima di qualsiasi installazione**, è necessario proteggere il server VPS Ubuntu secondo le regole dell'arte. Questo passo è **critico** per proteggere la vostra infrastruttura e i vostri fondi Lightning.



Ecco una guida dettagliata per aiutarvi a iniziare: **[Configurazione iniziale del server Ubuntu - Guida passo-passo](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** di Daniel P. Costas.



Questa guida tratta la configurazione degli utenti, l'SSH sicuro, il firewall (UFW), fail2ban, gli aggiornamenti automatici e le buone pratiche di sicurezza del sistema.



### Passo 2: Installazione del PHOENIXD



Una volta che il server è protetto, è necessario installare e configurare il PHOENIXD. Plan B Network offre un tutorial completo dedicato all'installazione, alla generazione del seed e alla configurazione del servizio systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Una volta che il PHOENIXD è attivo e funzionante (verificare con `./Phoenix-CLI getinfo`), prendere nota della **Password HTTP** in `~/.Phoenix/Phoenix.conf` - ne avrete bisogno per connettere LNbits al PHOENIXD.



### Distribuzione di LNbits



Installare UV e clonare LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Configurare il backend PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Aggiungere a `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Eseguire il test con `uv run lnbits --host 0.0.0.0 --port 5000` e creare un servizio systemd con `Wants=PHOENIXD.service`.



## Configurazione iniziale e primo utilizzo



### Attivazione del SuperUser



Attivare l'amministratore di Interface in `.env`:


```
LNBITS_ADMIN_UI=true
```



Riavviare LNbits (`sudo systemctl restart lnbits`) e recuperare l'ID SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Andare a `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` per il pannello di amministrazione. Il menu "Server" consente di configurare le fonti di finanziamento, le estensioni e gli account utente.



### Creazione sicura dell'account



**Importante per l'esposizione pubblica**: Se state esponendo la vostra istanza LNbits su un dominio pubblico accessibile da Internet, è **critico** disabilitare la creazione gratuita di account utente.



Dall'amministrazione di SuperUser Interface, andate su "Impostazioni" e poi sulla sezione "Gestione utenti". Troverete l'opzione "Consenti la creazione di nuovi utenti".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Per un'esposizione pubblica con nome di dominio** :




- È necessario disabilitare** l'opzione "Consenti la creazione di nuovi utenti"
- Senza questa protezione, chiunque su Internet può creare un account sulla vostra istanza
- Un utente malintenzionato potrebbe creare account e utilizzare la liquidità del vostro LIGHTNING NODE a vostra insaputa
- È necessario creare manualmente gli account utente dal SuperUser Interface



**Solo per uso locale** :




- Questa opzione è meno critica se l'istanza è accessibile solo localmente (http://localhost:5000)
- Tuttavia, disabilitare questa opzione è una buona pratica di sicurezza generale



Una volta configurato, solo l'amministratore SuperUser può creare nuovi account utente tramite il menu Interface "Utenti". Questo approccio garantisce un controllo totale su chi può accedere alla vostra infrastruttura Lightning e utilizzare i vostri fondi.



### Apertura del primo canale



PHOENIXD gestisce automaticamente i canali tramite l'autoliquidazione. generate un Lightning Invoice di ~30.000 Sats da LNbits e lo paga da un altro Wallet. Il PHOENIXD apre automaticamente un canale verso ACINQ. La commissione di apertura (~20-23k Sats) viene detratta, il saldo rimanente (~7-10k Sats) appare dopo la conferma del On-Chain.



Controllare lo stato con `./Phoenix-CLI getinfo`. Considerare quindi la possibilità di disabilitare l'autoliquidità (`auto-liquidity=off` in `Phoenix.conf`) per controllare le aperture dei canali.



### Visualizzazione pubblica e HTTPS



**Importante**: HTTPS obbligatorio per la visualizzazione pubblica (sicurezza della chiave API + compatibilità con LNURL). Saltare questo passaggio solo per l'uso locale.



**Caddy (consigliato)**: SSL automatico. `sudo apt install -y caddy`, modificare `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Riavviare: `sudo systemctl restart caddy`.



**Nginx** : Più controllo. Installare `nginx certbot python3-certbot-nginx`, creare `/etc/nginx/sites-available/lnbits` :


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


Attivare: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Aggiungere a `.env': `FORWARDED_ALLOW_IPS=*`



## Installazione dell'ombrello



### Distribuzione da App Store



Andate sull'App Store Umbrel, cercate "LNbits" e fate clic su "Installa".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel controlla automaticamente le dipendenze necessarie. Per funzionare, LNbits richiede il LIGHTNING NODE (LND). Se il vostro LIGHTNING NODE è già operativo, fate clic su "Installa LNbits" per confermare.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel scarica l'immagine Docker, configura automaticamente le connessioni con LND e avvia il contenitore (2-5 minuti). L'installazione avviene interamente in background.



### Configurazione iniziale del SuperUser



Al primo avvio, LNbits chiede di creare l'account amministratore SuperUser. Immettere un nome utente e impostare una password sicura per proteggere l'accesso al sistema di amministrazione Interface.



![Configuration SuperUser](assets/fr/03.webp)



**Importante**: Questo account SuperUser ha pieni privilegi sulla vostra istanza LNbits. Scegliete una password forte e tenetela al sicuro.



Una volta creato l'account, si accede automaticamente all'area amministrativa principale del Interface. Umbrel ha già impostato il LND come fonte di finanziamento: tutti i pagamenti Lightning passeranno attraverso i canali esistenti.



### Accesso all'amministratore del Interface



Nel menu a sinistra, fare clic su "Impostazioni" per accedere al pannello di amministrazione completo.



![Interface Settings](assets/fr/04.webp)



La sezione "Gestione dei portafogli" visualizza le informazioni principali sulla configurazione:




- Fonte di finanziamento** : LndBtcRestWallet (connessione diretta al vostro nodo LND Umbrel)
- Saldo del nodo** : Liquidità totale disponibile nei canali Lightning
- Saldo LNbits**: Fondi assegnati al sistema LNbits (inizialmente 0 Sats)



Ora potete sfruttare direttamente la liquidità del vostro nodo Umbrel per tutti i portafogli LNbits che create. Non è necessaria alcuna configurazione aggiuntiva: LNbits è già operativo.



### Gestione degli utenti



Una delle caratteristiche più potenti di LNbits è la possibilità di creare più utenti indipendenti, ciascuno con autenticazione tramite password e portafogli isolati. Questa architettura consente di sfruttare la liquidità del nodo Umbrel, offrendo al contempo sottoconti totalmente isolati per usi diversi: affari, famiglia, dipendenti, progetti, ecc.



Nel menu laterale, cliccare su "Utenti" per accedere alla gestione degli utenti. Cliccare su "CREA ACCOUNT" per aggiungere un nuovo utente.



![Gestion des utilisateurs](assets/fr/05.webp)



Compilare il modulo di creazione dell'utente:




- Nome utente**: Nome utente (esempio: "Satoshi")
- Imposta password**: Attivare questa opzione per impostare una password di autenticazione
- Password** e **Password repeat**: Imposta la password per questo utente



![Création utilisateur satoshi](assets/fr/06.webp)



I campi opzionali (chiave pubblica Nostr, e-mail, nome e cognome) possono essere lasciati vuoti per una configurazione minima. Fare clic su "CREA ACCOUNT" per confermare.



![Confirmation utilisateur créé](assets/fr/07.webp)



Il nuovo utente appare ora nell'elenco degli utenti con il suo identificativo unico e il suo nome utente.



![Liste des utilisateurs](assets/fr/08.webp)



**Punto importante**: Ogni utente può accedere in modo completamente indipendente con la propria password. L'amministratore SuperUser mantiene il pieno controllo attraverso lo strumento di amministrazione del Interface.



### Gestione utente Wallet



Ora che l'utente "Satoshi" è stato creato, è necessario assegnargli un Wallet Lightning. Fare clic sull'icona Wallet (seconda icona) dell'utente in questione, quindi su "CREA NUOVO Wallet".



![Gestion des wallets](assets/fr/09.webp)



Una finestra di dialogo chiede di dare un nome al Wallet. Inserire un nome descrittivo (ad esempio "Wallet Of Satoshi") e selezionare la valuta di visualizzazione (CUC, USD, EUR, ecc.).



![Création wallet](assets/fr/10.webp)



Fare clic su "CREA". LNbits genera immediatamente un Wallet Lightning funzionante per questo utente.



![Confirmation wallet créé](assets/fr/11.webp)



Ora si vedono i due portafogli esistenti: il Wallet predefinito "LNbits Wallet" creato automaticamente e il nuovo "Wallet Of Satoshi". Per semplificare l'esperienza dell'utente, è possibile eliminare il Wallet predefinito facendo clic sull'icona di eliminazione (cestino rosso).



![Wallet final unique](assets/fr/12.webp)



L'utente "Satoshi" dispone ora di un singolo Wallet chiaramente identificato. Ogni utente Wallet opera in modo completamente autonomo, pur utilizzando la liquidità del nodo LND sottostante.



**Concetto chiave**: Tutti questi portafogli condividono la liquidità globale del vostro nodo Umbrel. Non si creano nuovi canali Lightning per ogni Wallet: LNbits agisce come un Layer contabile intelligente che gestisce l'allocazione dei fondi all'interno della vostra infrastruttura Lightning esistente. Questa è la potenza del sistema multi-Wallet di LNbits.



### Accesso utente



Uscire dall'account SuperUser (icona in alto a destra) e tornare alla pagina di login di LNbits. Ora è possibile accedere con le credenziali del nuovo utente.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Inserire il nome utente ("Satoshi") e la password precedentemente definiti, quindi fare clic su "LOGIN". L'utente accede direttamente al suo Wallet personale, totalmente isolato dal Interface di amministrazione.



### Interface dall'utente Wallet



Una volta collegato, l'utente accede al suo Interface dal Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Il Interface è dotato di :




- Saldo corrente**: Visualizzato in Sats e nella valuta scelta (CUC in questo esempio)
- Azioni principali**: "PASTE REQUEST" (incolla una fattura da pagare), "CREATE Invoice" (generate una ricevuta), icona QR (scansione rapida)
- Cronologia delle transazioni** : Elenco completo di tutti i pagamenti e le ricevute
- Pannello laterale destro**: Opzioni di configurazione e accesso



### Accesso mobile Wallet



Il pannello laterale destro offre una funzione particolarmente pratica: l'accesso mobile al Wallet. Aprite la sezione "Accesso mobile" per scoprire le opzioni disponibili.



![Mobile Access](assets/fr/15.webp)



LNbits offre diversi modi per utilizzare il Wallet su uno smartphone:



**Opzione 1: applicazioni mobili compatibili




- Scaricate **Zeus** o **BlueWallet** dall'App Store o da Google Play
- Attivare l'estensione **LndHub** in LNbits per questo Wallet
- Scansionare il codice QR LndHub con l'applicazione mobile per collegare il Wallet



**Opzione 2: accesso diretto tramite browser mobile**




- Il codice QR visualizzato in "Esportazione su telefono con codice QR" contiene l'URL completo del Wallet con autenticazione integrata
- Scansionate questo codice QR dal vostro smartphone per aprire Wallet direttamente nel vostro browser mobile
- Aggiungere una pagina alla schermata iniziale per un accesso rapido



**Importante per la sicurezza**: Questo URL contiene le chiavi API per l'accesso completo al Wallet. Non condividetelo mai pubblicamente. Non condividetelo mai pubblicamente. Trattate questo codice QR come le vostre chiavi private del Bitcoin: chiunque esegua la scansione di questo codice QR ottiene l'accesso completo al Wallet.



Questa funzione mobile trasforma la vostra istanza LNbits Umbrel in un vero e proprio server Lightning Wallet per voi e i vostri amici, mantenendo la completa sovranità sui vostri fondi grazie al vostro nodo self-hosted.



### Condivisione dell'accesso degli utenti



Il caso d'uso principale di questa configurazione multiutente è la **condivisione dei portafogli con la famiglia o la cerchia ristretta**. Una volta creato un utente con un Wallet dedicato (come "Satoshi" nel nostro esempio), è possibile condividere le credenziali di accesso con i membri fidati della famiglia.



**Sicurezza dell'accesso su Umbrel**: L'accesso alla vostra istanza LNbits su Umbrel è naturalmente protetto, in quanto si può accedere solo a :




- Sulla rete locale** : I membri del vostro nucleo familiare collegati alla stessa rete WiFi/Ethernet possono accedere all'istanza
- Tramite VPN**: Se si utilizza una VPN come Tailscale configurata sul server Umbrel, gli utenti autorizzati possono ottenere un accesso remoto sicuro



Questa doppia protezione Layer (accesso alla rete + autenticazione dell'utente) rende l'opzione "Consenti la creazione di nuovi utenti" meno critica su Umbrel. Solo chi ha già accesso alla rete o alla VPN può raggiungere il login Interface.



**Scenario tipico**: Si crea un conto "papà", un conto "mamma", un conto "azienda" e così via. Ogni membro della famiglia ha il proprio Wallet Lightning isolato, pur beneficiando della liquidità condivisa del vostro nodo Umbrel. È sufficiente condividere il nome utente e la password: l'utente può connettersi da qualsiasi dispositivo della rete locale o tramite la VPN Tailscale. Per ulteriori informazioni, consultare il nostro tutorial dedicato a Tailscale:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Esplora le estensioni disponibili



Tornate al SuperUser Interface e accedete al menu "Estensioni" nel pannello laterale sinistro per scoprire l'intero ecosistema di estensioni LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits offre un ricco catalogo di estensioni che trasformano la vostra istanza in una vera e propria piattaforma di servizi Lightning:





- Jukebox**: Sistema jukebox alimentato da Sats (pagamenti Spotify)
- Biglietti di supporto**: Sistema di supporto a pagamento (ricevere Satss per rispondere alle domande)
- TPoS**: Terminale mobile e sicuro per i punti vendita al dettaglio
- User Manager**: gestione avanzata di utenti e Wallet (che abbiamo appena utilizzato)
- Eventi**: Vendita e convalida di biglietti per eventi
- Dispositivi LNURLD**: Gestione dei punti vendita, ATM, switch collegati
- SMTP**: Consente agli utenti di inviare e-mail e guadagnare Satss
- Boltcards**: Programmazione di carte NFC per pagamenti Lightning tap-to-pay
- NostrNip5**: Crea indirizzi NIP5 per i tuoi domini
- Pagamenti frazionati**: Distribuzione automatica dei pagamenti tra più portafogli



Ogni estensione si attiva con un solo clic da questo Interface. Le estensioni contrassegnate con "FREE" sono gratuite, mentre alcune sono disponibili in versione "PAID". Esplorate il catalogo per individuare quelle che corrispondono alle vostre esigenze, sia per gli affari, sia per la gestione della famiglia, sia per sperimentare le capacità del Lightning Network.



## Vantaggi e limiti



**Vantaggi**: Sovranità finanziaria (pieno controllo su fondi/chiavi/dati), flessibilità architettonica (migrazione VPS→Full node senza perdite), sistema di estensione professionale, Interface intuitivo.



**Limitazioni** : Software in versione beta (attenzione alle quantità), sicurezza sotto la responsabilità dell'amministratore, URL contenenti chiavi API sensibili (HTTPS obbligatorio), la gestione multiutente implica una responsabilità di custodia.



## Le migliori pratiche



**Backup**: seed PHOENIXD/credenziali LND, database LNbits, file `.env`. Automatizzare quotidianamente, tenere fuori dal server di produzione, crittografato. Testare regolarmente i ripristini.



**Manutenzione**: Controllare regolarmente gli aggiornamenti (LNbits, backend Lightning, sistema operativo). Controllare sempre le note di rilascio prima degli aggiornamenti principali.





- Su Umbrel**: App Store notifica automaticamente le nuove versioni. Sincronizzare le estensioni tramite "Gestione estensioni" > "Aggiorna tutto". Controllare l'inclusione del database SQLite nei backup automatici di Umbrel.
- Su VPS**: Aggiornare manualmente con `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Monitorare i log di sistema: `sudo journalctl -u lnbits -f`.



## Conclusione



LNbits self-hosting offre un percorso concreto verso la sovranità finanziaria di Lightning. VPS+PHOENIXD offre una soluzione leggera per servizi veloci, con una piena integrazione con il nodo Bitcoin esistente. L'architettura scalabile consente di passare da semplici Wallet multiutente a sofisticati casi d'uso aziendali.



Il self-hosting implica responsabilità: backup dei semi, protezione dell'accesso, inizio con importi modesti. Con queste precauzioni, LNbits diventa una soluzione robusta per l'economia Lightning, preservando al contempo la decentralizzazione e l'autonomia.



## Risorse



### Documentazione ufficiale




- [Documentazione LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Guida ufficiale all'installazione](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Guide della comunità




- [Configurazione iniziale del server Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) di Daniel P. Costas (sicurezza VPS passo dopo passo)
- [Installazione di LNbits + PHOENIXD su Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) di Daniel P. Costas (guida completa)
- [Server LNbits su Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) di Axel
- [LNbits su VPS](https://github.com/TrezorHannes/vps-lnbits) di Hannes