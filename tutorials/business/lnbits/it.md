---
name: LNbits
description: Piattaforma di contabilità commerciale
---
![presentation](assets/lnbits-intro.webp)

# Sistema di contabilità

LNbits è dotato di molti strumenti per controllare e incanalare i fondi in entrata e in uscita, collegare il vostro negozio web o anche dispositivi come un portafoglio hardware o un bancomat che avete costruito voi stessi. I tipi di utente includono:


- I proprietari di portafogli che desiderano utilizzare LNbits come interfaccia per la gestione dei propri fondi e per le sue funzioni extra.
- Commercianti o fornitori di servizi online e offline che vogliono accettare pagamenti Bitcoin onchain e Lightning Network.
- Sviluppatori che vogliono creare applicazioni per la rete Lightning.
- Operatori di nodi che desiderano integrare il proprio nodo con il sistema LNbits a fini contabili.
- Tutti hanno esigenze diverse. Costruiamo LNbits in modo modulare, in modo che ogni utente possa utilizzare le nostre funzioni nel modo più adatto a lui.

# Gestore del portafoglio

LNbits è un sistema di contabilità gratuito e open-source, non un gestore di nodi. La gestione dei canali è di competenza del nodo Lightning collegato a LNbits come fonte di finanziamento, come LND o c-lightning. Il superutente o l'utente amministratore del sistema LNbits sono responsabili della gestione dell'accessibilità complessiva e della configurazione delle funzioni di contabilità e delle estensioni interne.

LNbits funge da interfaccia tra l'utente e il nodo Lightning, fornendo un modo semplice e intuitivo per gestire e interagire con la rete di pagamento.

Pensate a LNbits come a un "framework modulare di Wordpress" per il vostro nodo. Una piattaforma facile da gestire, basata su estensioni che si possono combinare per numerosi casi d'uso.

Pensate a LNbits come al software di gestione finanziaria della vostra banca. Il vostro nodo offre canali di pagamento e LNbits estende il vostro nodo in modo da poter gestire più di un portafoglio lightning di cui il vostro nodo è dotato. Questi portafogli non devono necessariamente appartenere a voi stessi. Supponiamo che voi, in qualità di gestore del nodo LN, abbiate già abbastanza liquidità e fondi per i canali e che ora vogliate offrire alcuni servizi bancari in bitcoin ai vostri amici, alla vostra famiglia, al vostro negozio o ad altri commercianti abituali.

Offrirete loro un modo semplice per aprire un "conto bancario" sul vostro nodo senza avere accesso ad altri portafogli sul vostro nodo e a tutta la liquidità del nodo, ma solo alla loro parte. Il vostro nodo (la banca) agisce solo come fornitore di trasporto per i loro pagamenti (in entrata e in uscita).

NOTA: tutti i fondi che i vostri "clienti" depositano nei loro conti bancari LNbits sul vostro nodo, andranno direttamente nei canali LN del vostro nodo. Questo significa che TU sei il vero proprietario di quei fondi. Avrete una grande responsabilità per i loro fondi. Non siate malvagi e non scappate con i fondi, non siate malvagi e non applicate commissioni elevate. Vogliamo fottere i banchieri della fiat, non fottere gli altri (utenti bitcoin).

# Piattaforma demo

La demo si trova all'indirizzo [https://legend.lnbits.com](https://legend.lnbits.com). È completamente funzionante e può essere utilizzata per conoscere la rete Lightning e le caratteristiche di LNbits e LNURL in generale. Sebbene non possiamo impedirvi di utilizzarla, vi chiediamo di non usarla per la vostra configurazione di produzione. Non solo lavoriamo spesso sui server per testare nuove funzionalità, ma vorremmo anche incoraggiarvi a gestire il vostro nodo e LNbits in modo sovrano. Se pensate che gestire un nodo sia troppo impegnativo per il momento, potete collegare LNbits a un servizio di finanziamento custode nel cloud come Opennode, Luna o Votage o al Lightning Tipbot su Telegram, solo per citarne alcuni.

# Volantino LNbits

Volete consegnare alcune informazioni di base a un commerciante o a un vostro amico costruttore? Siamo lieti di annunciare il nostro primo volantino a disposizione di tutti. Il formato è quello tipico di un volantino di 6 pagine (2 pieghe) con una larghezza di 3508 e un'altezza di 2480px.

LNbits per i commercianti: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits per i costruttori: [EN](/assets/lnbits-builders-it.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Alcune nozioni di base

LNbits funziona sulla base del protocollo LNURL, il che significa che le richieste sono valide in due forme: o come link https:// clearnet (non sono ammessi certificati autofirmati) o come link http:// v2/v3 onion. Per offrire servizi LNbits come i codici QR LNURLp/w o le carte NFC, che possono essere utilizzati in libertà, è necessario aprire LNbits a clearnet (https).

Prima di installare LNbits, assicuratevi di aver letto e compreso le seguenti guide generali su cosa è LNbits e quali possibilità vi offre.


- [Guida LND](https://docs.lightning.engineering/) | Installazione di LND
- [Esempio di configurazione LND](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Impostazioni LND
- [Guida CLN](https://docs.corelightning.org/docs/installation) | Installazione di CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Gestire una torre di guardia](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Molto importante!

Guide più dettagliate sull'utilizzo di LNbit in scenari d'uso specifici qui:


- [Guida introduttiva a LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Guida alla sottostazione
- [ToDos per la vostra sicurezza con LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Banche private sulla rete dei fulmini](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Guida alla sottostima
- [Esegui i portafogli dei custodi per i tuoi amici e parenti] (https://darthcoin.substack.com/p/the-bank-of-lnbits) | Guida alla sottostima
- [LNbits per un piccolo ristorante/albergo](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Guida Substack
- [Utilizzo del copilota LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Guida di Substack
- [Avvia il tuo mercato NOSTR con LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Guida alla sottostazione
- [Utilizzo di LNbits per progetti scolastici o per eventi di festival](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Guida all'utilizzo di Substack

# Installare LNbits

## Guida all'installazione di base

LNbits può essere installato su qualsiasi macchina con sistema operativo Linux. Non richiede una macchina o un server potente, ma solo sufficiente memoria RAM e spazio su disco per il database. Può essere eseguito separatamente da un nodo BTC/LN (PC locale o VPS remoto) o insieme sulla stessa macchina con il nodo o già installato in una macchina software del nodo.

È possibile scegliere tra i gestori di pacchetti più comuni, come poetry e nix. Per impostazione predefinita, LNbits utilizza SQLite come database. È possibile utilizzare anche PostgreSQL, consigliato per le applicazioni con un carico elevato. [Ecco una guida per l'installazione di base usando poetry o nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Per tutti coloro che sono alle prime armi, troverete guide dettagliate passo-passo per far funzionare i vostri LNbit in ambienti specifici:


- [LNbits su clearnet](https://ereignishorizont.xyz/lnbits-server/en/) di Axel
- [LNbits su un VPS](https://github.com/TrezorHannes/vps-lnbits) di Hannes
- [LNbits su cloudflare](https://www.nodeacademy.org/lnbits) di Leo

È anche possibile trovare un video su [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Altri scenari di installazione qui](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Per i nodi software bundle, fare riferimento alla loro documentazione specifica su LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Se non siete interessati alle questioni tecniche e non volete ospitare la vostra fonte di finanziamento o il vostro LNbits, potete utilizzare [LNbits SaaS version](https://saas.lnbits.com) (Software-as-a-service). È fondamentalmente come LNbits in un cloud, ma potete definire voi stessi la fonte di finanziamento (ad esempio il vostro Nodo, un portafoglio LNbits, il LNtipbot, il fakewallet, ecc.) e le variabili di ambiente - cosa che per lo più non avviene in altre soluzioni cloud.

[Ecco una guida dettagliata su come utilizzare LNbits SaaS per casi d'uso specifici](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Fonti di finanziamento

LNbits non è un software per la gestione dei nodi, ma un sistema di contabilità focalizzato sugli LN in aggiunta a una fonte di finanziamento LND o CLN. Dopo la prima installazione è possibile visitare il proprio LNbits all'indirizzo http://localhost:5000/.

Per modificare la fonte di finanziamento, accedere all'URL del super-utente e selezionare una fonte di finanziamento all'interno di "Manage Server" o modificare il file .env modificando `LNBITS_BACKEND_WALLET_CLASS` con la fonte desiderata se si imposta `adminUI=TRUE` nel `.env`.

Il file .env si trova all'interno della cartella lnbits/ o lnbits/apps/data estendendo il comando per elencare i file nella propria directory con `ls -a`.

Potrebbe essere necessario installare altri pacchetti o eseguire ulteriori passaggi di configurazione, selezionando la fonte di finanziamento desiderata. Dopo un riavvio, la nuova configurazione sarà attiva.

Quali fonti di finanziamento posso utilizzare per LNbits?

LNbits può funzionare su molte fonti di finanziamento delle reti di luce. Attualmente sono supportati CoreLightning, LND, LNbits, LNPay, OpenNode e altri vengono aggiunti regolarmente.

È importante scegliere una fonte che abbia una buona liquidità e una buona connessione tra pari. Se si utilizza LNbits per i servizi pubblici, i pagamenti degli utenti possono fluire felicemente in entrambe le direzioni.

Un portafoglio backend (fonte di finanziamento) può essere configurato utilizzando le seguenti variabili d'ambiente LNbits nel file `.env` o all'interno del proprio account superuser nella sezione Manage-Server.

Se si desidera utilizzare la versione .env, è possibile trovare i parametri qui:

### Fulmine di nucleo


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/percorso/lightning-rpc
- Scintilla (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - sPARK_TOKEN`: chiave_di_accesso_segreta

### Demone della rete Lightning


- LND (RIPOSO)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon o Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: porta
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon o Bech64/Hex

Si può anche usare un amaretto crittografato con AES (maggiori informazioni) usando


  - lND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Per criptare il macaroon, eseguire `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (un'altra istanza di LNbits)


- Istanza LNbits ospitata su un server cloud o sul proprio server domestico
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (! NON utilizzare questo server per scopi produttivi/commerciali, ma solo per i test!!!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Fulmine TipBot

Per collegare il [Lightning Tipbot](https://t.me/LightningTipBot) da Telegram è necessario impostare i seguenti parametri:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Per ottenere la chiave è necessario eseguire /api in una chat privata con LightningTipbot su Telegram una volta.

Si veda anche questo tutorial su come installare [LNbits con LightningTipBot via vps] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### HUB IBEX

Registratevi [qui] (https://ibexpay.ibexmercado.com/onboard) e poi prendete le vostre chiavi/token da lì, il punto finale è https://ibexpay-api.ibexmercado.com.

Per maggiori informazioni, vedere [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Affinché l'ascoltatore di fatture funzioni, è necessario disporre di un URL accessibile pubblicamente nel proprio LNbits e impostare un [LNPay webhook](https://dashboard.lnpay.co/webhook/) che punti a `<l'host di LNbits>/wallet/webhook` con l'evento "Wallet Receive" e nessun segreto. L'impostazione `https://mylnbits/wallet/webhook` sarà l'url dell'endpoint che riceverà la notifica di ogni pagamento.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### Nodo aperto

Affinché la fattura funzioni, è necessario avere un URL accessibile pubblicamente nel proprio LNbits. L'impostazione del webhook è facoltativa.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby è un'estensione del browser con funzionalità di portafoglio LN e conto LNDHUB che può essere utilizzato come fonte di finanziamento per gli LNbit. [Maggiori dettagli qui](https://getalby.com/).

Affinché la fattura funzioni, è necessario disporre di un URL accessibile pubblicamente nel proprio LNbits. Non è necessaria alcuna impostazione manuale del webhook. È possibile generare un token di accesso Alby qui: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Guide aggiuntive / Risoluzione dei problemi

Ecco alcune istruzioni aggiuntive nel caso in cui ne aveste bisogno. Fate clic sulla freccia per espandere la descrizione.

### I Killswitch 🚨

Ultimamente si sono verificati così tanti bug pericolosi non solo nell'intero settore, ma anche in LNbits, che abbiamo deciso di fare qualcosa al riguardo. Ora è possibile ricevere avvisi e/o intraprendere azioni dirette, quando si ripresenta una vulnerabilità o un bug che potrebbe portare alla perdita di fondi.

![killswitchn](assets/lnbits-killswitch.webp)

Se si passa al void-wallet, tutti gli utenti dell'istanza vedranno un banner giallo dove normalmente si trova l'avviso "LNbits è in Beta" accanto all'area del tema/lingua sulla destra - ed è l'indizio più ovvio che qualcosa è successo. Date un'occhiata alla vostra nuova scheda server evidenziata in verde nella parte sinistra della finestra.

Come funziona? Quando il killswitch è abilitato, un repository github segreto, disponibile solo al team di LNbits, viene controllato a un intervallo di X minuti (che può essere specificato). Se in questo repository viene pubblicato un bug vulnerabile, questo segnale fa scattare il killswitch su tutte le installazioni che si sono iscritte e fa passare la vostra istanza lnbits all'uso del portafoglio vuoto. Se le nubi si sono diradate e avete installato l'aggiornamento di sicurezza, potete impostare nuovamente la fonte di finanziamento sul vostro nodo, sul vostro portafoglio o su qualsiasi altra cosa stiate usando, anche attraverso la sezione Manage Server. Questo wiki contiene una sezione su come cambiare fonte di finanziamento se non si sa cosa configurare.

### Differenza tra admin e superuser

L'interfaccia amministrativa di LNbits consente di modificare le impostazioni di LNbits tramite il frontend di LNbits. È disattivata per impostazione predefinita e la prima volta che si imposta la variabile di ambiente `LNBITS_ADMIN_UI=true` nel file `.env`, le impostazioni vengono inizializzate e saranno utilizzate. Da quel momento in poi verranno utilizzate le impostazioni del database al posto di quelle del file .env.

### Super utente

Con l'interfaccia utente dell'amministratore abbiamo introdotto il superutente, che ha accesso al server e può quindi modificare le impostazioni che potrebbero mandare in crash il server o renderlo poco reattivo tramite il frontend e le API, come ad esempio la modifica della fonte di finanziamento. Il superutente è memorizzato solo nella tabella delle impostazioni del database. Dopo che le impostazioni sono state "riportate ai valori predefiniti" e riavviate, viene creato un nuovo superutente. Abbiamo anche aggiunto un decoratore per le rotte API per verificare l'esistenza di un superutente. Il suo ID non viene mai inviato tramite l'API e il frontend e riceve solo un bool (sì/no) se si è superutente o meno.

Solo il superutente può trasferire i satoshis a diversi portafogli tramite la sezione "Ricarica".

Si può anche inviare il superutente tramite webhook a un altro servizio quando viene creato. Maggiori informazioni qui https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Nel frontend troverete anche la possibilità di cambiare l'immagine del negozio che viene mostrata nella pagina "crea portafoglio" aprendo la sezione Gestisci server e scegliendo Tema -> Logo personalizzato.

### Utenti amministratori

Variabile di ambiente: `LNBITS_ADMIN_USERS`, elenco virgola-seperato di ID utente. Gli utenti amministratori possono modificare le impostazioni nell'interfaccia utente dell'amministrazione, a eccezione delle impostazioni della fonte di finanziamento, perché ciò richiederebbe il riavvio del server e potrebbe rendere il server inaccessibile. Inoltre hanno accesso a tutte le estensioni a loro dedicate in `LNBITS_ADMIN_EXTENSIONS`.

### Utenti ammessi

Variabile di ambiente: `LNBITS_ALLOWED_USERS`, elenco virgolettato di ID utente. Definendo questi utenti, LNbits non sarà più utilizzabile dal pubblico. Solo gli utenti e gli amministratori definiti possono accedere al frontend di LNbits.

#### Aggiornare LNbits

Per aggiornare normalmente l'istanza locale di LNbits è sufficiente copiare e incollare i seguenti comandi CLI:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Se si esegue Raspiblitz o MyNode, si potrebbe avere bisogno di un'ulteriore opzione

```
sudo systemctl restart lnbits
```

alla fine, perché esegue LNbits come servizio.

Su Umbrel/Citadel i comandi saranno

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### Migrazione da SQLite a PostgreSQL

Se avete già LNbits installato e funzionante su un database SQLite, vi consigliamo vivamente di migrare a postgres se avete intenzione di far funzionare LNbits su scala.

È stato incluso uno script che può eseguire la migrazione in modo semplice. È necessario che Postgres sia già installato e che ci sia una password per l'utente (vedere la guida all'installazione di Postgres sopra). Inoltre, l'istanza di LNbits deve essere eseguita una volta su Postgres per implementare lo schema del database prima che la migrazione possa funzionare:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Si spera che ora tutto funzioni e venga migrato... Avviare nuovamente LNbits e verificare che tutto funzioni correttamente.

#### Backup e ripristino del database

Consultare [questa guida molto dettagliata sul processo di backup e ripristino] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Finanziare il mio portafoglio LNbits dal mio nodo non funziona

Se si desidera inviare saturazioni dallo stesso nodo che è la fonte di finanziamento dei propri LNbit, è necessario modificare il file lnd.conf.

I parametri da includere sono: `allow-circular-route=1`

Lo si faccia nella sezione Application options del proprio lnd.conf. Su alcuni nodi bundle l'avvio di LND potrebbe altrimenti fallire.

NOTA: Si consiglia di utilizzare la nuova estensione adminUI con l'opzione "TopUp" per aggiungere fondi a un conto LNbits.

#### Errore 426

Ho ricevuto l'errore: "lnurl deve essere consegnato su un dominio https pubblicamente accessibile o su tor. richiesto l'aggiornamento 426"</summary>

Questo errore di solito è dovuto al fatto che LNbits dietro un tunnel ngnix non inoltra correttamente l'indirizzo LNURL. Fermare LNbits e modificare il file .env aggiungendo questa riga:

`FORWARDED_ALLOW_IPS=*`

Inoltre, se si usa una configurazione ngnix, assicurarsi di avere questi header nella configurazione ngnix:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Errore di rete

Ho ottenuto "errore https", errore di rete" o altri durante la scansione di un QR</summary>

Brutte notizie, si tratta di un errore di routing che potrebbe avere molte ragioni. Per prima cosa controllate l'LNURL del QR con il [Lightning Decoder](https://lightningdecoder.com/) se trovate qualcosa di strano. Proviamo alcuni dei possibili problemi e le loro soluzioni.

LNbits funziona solo via Tor, non è possibile aprirlo su un dominio pubblico come lnbits.yourdomain.com


- Dato che volete che la vostra configurazione rimanga così, aprite il vostro portafoglio LNbits utilizzando l'URI .onion e createlo di nuovo. In questo modo il QR viene generato per essere accessibile tramite questo URI .onion, quindi solo via tor. Non generare il QR da un URI .local, perché non sarà raggiungibile via internet, ma solo dalla propria home-LAN.
- Aprire l'applicazione del portafoglio LN utilizzata per la scansione del QR e questa volta utilizzare tor (vedere le impostazioni dell'applicazione del portafoglio). Se l'app non offre tor, è possibile utilizzare Orbot (Android). Per istruzioni dettagliate su come aprire i vostri LNbit per clearnet/https, consultate la sezione Installazione.

#### Impedire ad altri di generare portafogli con i miei LNbit

Quando si gestisce il nodo LNbits in clearnet, tutti possono generare un portafoglio su di esso. Dal momento che i fondi del vostro nodo sono legati a questi portafogli, potreste volerlo impedire. Ci sono due modi per farlo:

Configurare gli utenti e le estensioni consentite nel file `.env` ([vedere l'esempio di env qui](https://github.com/lnbits/lnbits/blob/main/.env.example)). Questo funziona solo se si usa l'impostazione `adminUI=FALSE` nel file .env, altrimenti è necessario farlo nella sezione Gestione del server -> Utenti -> Utenti consentiti. Tutti gli altri non saranno poi autorizzati.

#### Personalizzare il periodo di scadenza della fattura

Ora è possibile generare fatture con una scadenza personalizzata. Compatibile con i backend: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet finora!

È possibile impostare `LIGHTNING_INVOICE_EXPIRY` nel file .env o utilizzare l'AdminUI per modificare il valore predefinito per tutte le fatture. C'è anche un nuovo campo nell'endpoint /api/v1/payments in cui è possibile impostare la scadenza nei dati JSON.

## Portafoglio-URL cancellato

### Portafoglio sul server demo legend.lnbits

Salvate sempre una copia del vostro wallet-URL, Export2phone-QR o LNDhub per i vostri portafogli in un luogo sicuro. LNbits non può aiutarvi a recuperarli in caso di smarrimento.

### Portafoglio sulla propria fonte/nodo di finanziamento

Salvate sempre una copia del vostro wallet-URL, Export2phone-QR o LNDhub per i vostri portafogli in un luogo sicuro. È possibile trovare tutti gli utenti LNbits e gli ID dei portafogli nell'estensione LNbits User Manager o nel database sqlite. Per modificare o leggere il database di LNbits, andate nella cartella LNbits /data e cercate il file sqlite.db. È possibile aprirlo e modificarlo con excel o con un editor SQL dedicato come [SQLite browser] (https://sqlitebrowser.org/).

Inoltre è possibile scaricare i portafogli tramite cli e visualizzare ogni portafoglio all'interno del database.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

L'output sarà simile a questo

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

e si desidera inserire questi valori in un url come questo

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

In questo modo si sostituisce f8a43fc363ea428db5c53b3559935f1f con il valore che precede il nome (nel nostro esempio f8a43fc363ea428db5c53b3559935f1f) e 1280ff5910a9c485a782a2376f338b6c è il vostro utente e dovrebbe diventare il valore mostrato dopo il nome. Per uscire da sqlite3 inserire

```
.quit
```

#### LNURL per un indirizzo di posta elettronica viceversa

Provate questo [encoder](https://lnurl-codec.netlify.app/) di fiatjaf o [questo](https://lightningdecoder.com/). Per pagare o controllare un LNURLp si può anche usare [LNurlpay](https://wwww.lnurlpay.com/). Dovrebbe essere indicato HTTPS e non HTTP.

#### Configurare un commento che le persone vedono quando pagano al mio LNURLp QR

Quando si crea un LNURL-p, per impostazione predefinita la casella dei commenti non è riempita. Ciò significa che i commenti non possono essere allegati ai pagamenti.

Per consentire i commenti, aggiungere la lunghezza dei caratteri della casella, da 1 a 250. Una volta inserito un numero, la casella dei commenti verrà visualizzata nel processo di pagamento. È anche possibile modificare un LNURL-p già creato e aggiungere quel numero.

![lnbits comments](assets/lnbits-comments.webp)

#### Depositare BTC onchain su LNbits

Esistono due modi per scambiare saturazioni da BTC onchain a LN BTC (rispettivamente a LNbits).

##### Tramite un servizio di swap esterno.

Altri utenti che non hanno accesso al vostro LNb possono usare un servizio di scambio come [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) o [ZigZag](https://zigzag.io/). Questo è utile se si forniscono solo fatture LNURL/LN dalla propria istanza LNbits, ma un pagatore dispone solo di saturazioni onchain, per cui dovrà prima scambiarle dalla propria parte. La procedura è semplice: l'utente invia btc onchain al servizio di swap e fornisce la fattura LNURL / LN di LNbits come destinazione dello swap.

##### Utilizzo dell'estensione LNbits di Onchain e Boltz.

Tenete presente che si tratta di un portafoglio separato, non quello di LN btc che è rappresentato da LNbits come "il vostro portafoglio" sulla vostra fonte di finanziamento LN. Questo portafoglio onchain può essere utilizzato anche per scambiare LN btc con (ad esempio, il vostro hardwarewallet) utilizzando l'estensione LNbits Boltz o Deezy. Se gestite un negozio web che è collegato al vostro LNbits per i pagamenti in LN, è molto utile scaricare regolarmente tutte le sature da LN a onchain. In questo modo si ottiene più spazio nei canali LN per poter ricevere nuova saturazione.

Procedura per chi non ha un portafoglio hardware bitcoin:


- Utilizzare Electrum o Sparrow per creare un nuovo portafoglio onchain e salvare il seed di backup in un luogo sicuro.
- Andare alle informazioni sul portafoglio e copiare il file xpub.
- Andate su LNbits - Estensione Onchain e create un nuovo portafoglio per soli orologi con questo xpub.
- Andare su LNbits - estensione Tipjar e creare un nuovo Tipjar. Selezionare anche l'opzione onchain oltre al portafoglio LN.
- Opzionale - Andare su LNbits - estensione SatsPay e creare un nuovo addebito per onchain btc. È possibile scegliere tra onchain e LN o entrambi. Verrà quindi creata una fattura che potrà essere condivisa.
- Opzionale - Se si utilizza LNbits collegato a una pagina Wordpress + Woocommerce, una volta creato/collegato un portafoglio per soli orologi al portafoglio del negozio LN btc, il cliente avrà entrambe le opzioni di pagamento nella stessa schermata.

Quando si riceve un pagamento in LNbits, nel registro delle transazioni viene visualizzato solo il tipo di transazione ripresa.

![lnbits payment details](assets/lnbits-payment-details.webp)

Nella panoramica delle transazioni troverete una piccola freccia verde per i fondi ricevuti e una freccia rossa per i fondi inviati.

Se si fa clic su queste frecce, un popup di dettagli mostra i messaggi allegati e il nome del mittente, se indicato.

Per configurare un nome da far apparire nei pagamenti, in LNbits non è attualmente possibile farlo - ma riceverlo. Questo è possibile solo se il portafoglio LN del mittente supporta [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) come [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Vedrete quindi un alias/pseudonimo nella sezione dei dettagli delle vostre transazioni LNbits (cliccate sulle frecce). Si noti che è possibile indicare qualsiasi nome e che potrebbe non essere correlato al nome del vero mittente, se lo si riceve.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Per importare il vostro conto LNbits in un'app portafoglio, aprite il vostro LNbits con l'account/il portafoglio che volete utilizzare, andate su "gestione estensioni" e attivate l'estensione LNDHUB. Aprire l'estensione LNDHUB, scegliere il portafoglio che si desidera utilizzare e scansionare il QR "admin" o "invoice only", a seconda del livello di sicurezza desiderato per quel portafoglio.

È possibile utilizzare [Zeus](https://zeusln.app/) o [Bluewallet](https://bluewallet.io/) come applicazioni portafoglio per un account lndhub, dove BW supporta più di un portafoglio.

Quando si esegue questa operazione, si consiglia di impostare anche l'URI della rete LN su quello del proprio nodo. Se l'istanza di LNbits è solo Tor, è necessario utilizzare queste applicazioni con Tor attivato. Anche in questo caso è necessario aprire la pagina di LNbits attraverso il proprio indirizzo Tor .onion.

Se si verifica l'errore "tipo di hash non supportato" quando si utilizza un ypub nell'estensione On-chain, verificare se l'istanza di LNbits utilizza python 3.10, potrebbe essere affetta da [questo problema] (https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Modificare il file openssl.cnf come descritto nella risposta di stackoverflow e riavviare LNbits.

## Attrezzi e costruzione con LNbits

LNbits dispone di ogni sorta di [API aperte] (https://legend.lnbits.com/docs) e di strumenti per programmare e connettersi a molti dispositivi diversi per una miriade di casi d'uso.

Se siete alle prime armi con la costruzione, iniziate con questa [MakerBits presentations](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) di Ben Arc sulla costruzione di gadget basati su LNbits.

### IMPORTANTE:


- LNbits funziona sulla base del protocollo LNURL, le cui richieste sono valide in due forme: o come link https:// clearnet (non sono ammessi certificati autofirmati) o come link http:// v2/v3 onion. Per offrire servizi LNbits come i codici QR LNURLp/w o le carte NFC, che possono essere utilizzati in libertà, è necessario aprire LNbits a clearnet (https).
- Per alimentare l'esp32 utilizzare solo cavi dati. Non tutti i cavi supportano i dati oltre all'alimentazione dell'esp. Non saresti il primo se il cavo fornito con l'esp fosse di sola alimentazione
- Assicurarsi di non utilizzare un hub USB con altri dispositivi collegati. Questo può portare a strani effetti difficili da debuggare (ad esempio, il mancato avvio o l'arresto).
- Per realizzare i progetti esp con MacOS è necessario un driver UART Bridge. Se avete problemi con il driver su sistemi Mac o Linux, potete trovarli qui o, se si tratta di un display TTGO, qui. Se avete problemi di connessione con Windows, assicuratevi di scaricare la VECCHIA versione 11.1.0 perché quella più recente non funziona! Per verificare la connessione, qui si può trovare anche un terminale seriale, impostato su un baudrate di 115200.
- Anche se è molto più comodo usare Platform.io (ad esempio, le dipendenze vengono installate automaticamente), raccomandiamo l'uso di Arduino per tutti coloro che sono alle prime armi con la costruzione.
- TT-Go Display S3: Il colore della linguetta della pellicola protettiva dello schermo indica esattamente quale controller (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...) è stato utilizzato per costruirlo. Conservatelo per poter eseguire il debug se vi programmate e lo schermo non visualizza correttamente la grafica, ad esempio colori sbagliati, immagini speculari o pixel vaganti ai bordi. Se mai dovessi avere bisogno di farlo, c'è una guida epica sulla regolazione per i diversi schermi
- Usare sempre lnurl239xx minuscolo invece di LNURLl239xx
- L'aggiunta di lightning:lnurl1234xyz creerà un QR che richiede l'apertura del portafoglio dell'utente per questa fattura alla scansione (ultima app lightning installata su iOS, impostazione in Android)
- Se state flashando un esp32 via web funzionerà solo con questi browser (TL:DR Chrome, Edge e Opera).
- Tenere presente il riferimento PIN-OUT per l'esp
- Quando utilizzate FOSSoftware o FOSGuide, linkate sempre l'autore. Tutti amano veder crescere il proprio bambino e questo dà inizio a una catena di costruzione che è davvero impressionante da vedere :)

Vieni nel [Gruppo Telegram di Makerbits](https://t.me/makerbits) se hai bisogno di aiuto per un progetto - ci siamo noi!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Ecco alcune categorie di progetti che potete realizzare con LNbits:


- [Dispositivo di firma Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Lampada Nostr Zap](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Piggy fulminato](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Portafoglio hardware](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Distributore automatico](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora e la rete mesh](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [AIUTANTI E RISORSE](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Altri esempi di progetti "Powered by LNbits" qui](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Casi d'uso per LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)