---
name: LNbits
description: Piattaforma di contabilità aziendale
---
![presentation](assets/cover.webp)


## Sistema di contabilità

LNbits è dotato di molti strumenti per controllare e incanalare i fondi in entrata e in uscita, collegare il tuo negozio web o anche dispositivi come un wallet hardware o un ATM che hai costruito tu stesso. I tipi di utente includono:
- I proprietari di wallet che desiderano utilizzare LNbits come interfaccia per la gestione dei propri fondi e per le sue funzioni extra.
- Commercianti o fornitori di servizi online e offline che vogliono accettare pagamenti Bitcoin onchain e Lightning Network.
- Sviluppatori che vogliono creare applicazioni per la rete Lightning.
- Operatori di nodi che desiderano integrare il proprio nodo con il sistema LNbits a fini contabili.
- Tutti hanno esigenze diverse. Costruiamo LNbits in modo modulare, in modo che ogni utente possa utilizzare le nostre funzioni nel modo più adatto a lui.


## Gestore del wallet

LNbits è un sistema di contabilità gratuito e open-source, non un gestore di nodi. La gestione dei canali è di competenza del nodo Lightning collegato a LNbits come fonte di finanziamento, come LND o c-lightning. Il superutente o l'utente amministratore del sistema LNbits sono responsabili della gestione dell'accessibilità complessiva e della configurazione delle funzioni di contabilità e delle estensioni interne.

LNbits funge da interfaccia tra l'utente e il nodo Lightning, fornendo un modo semplice e intuitivo per gestire e interagire con la rete di pagamento.

Pensa a LNbits come a un "framework modulare di Wordpress" per il tuo nodo. Una piattaforma facile da gestire, basata su estensioni che si possono combinare per numerosi casi d'uso.

Pensate a LNbits come al software di gestione finanziaria della tua banca. Il tuo nodo offre canali di pagamento e LNbits estende il tuo nodo in modo da poter gestire più di un wallet Lightning di cui il tuo nodo è dotato. Questi wallet non devono necessariamente appartenere a te stesso. Supponiamo che tu, in qualità di gestore del nodo LN, abbia già abbastanza liquidità e fondi per i canali e che ora voglia offrire alcuni servizi bancari in bitcoin ai tuoi amici, alla tua famiglia, al tuo negozio o ad altri commercianti abituali.

Offri loro un modo semplice per aprire un "conto bancario" sul tuo nodo senza avere accesso ad altri wallet sul tuo nodo e a tutta la liquidità del nodo, ma solo alla loro parte. Il tuo nodo (la banca) agisce solo come fornitore di trasporto per i loro pagamenti (in entrata e in uscita).

NOTA: tutti i fondi che i tuoi "clienti" depositano nei loro conti bancari LNbits sul tuo nodo, andranno direttamente nei canali LN del tuo nodo. Questo significa che TU sei il vero proprietario di quei fondi. Avrai una grande responsabilità per i loro fondi. Non essere malvagio e non scappare con i fondi, non essere malvagio e non applicare commissioni elevate. Vogliamo fottere i banchieri delle fiat, non fottere gli altri (utenti Bitcoin).


## Piattaforma demo

La demo si trova all'indirizzo [https://legend.lnbits.com](https://legend.lnbits.com). È completamente funzionante e può essere utilizzata per conoscere la rete Lightning e le caratteristiche di LNbits e LNURL in generale. Sebbene non possiamo impedirti di utilizzarla, ti chiediamo di non usarla per la tua configurazione di produzione. Non solo lavoriamo spesso sui server per testare nuove funzionalità, ma vorremmo anche incoraggiarti a gestire il tuo nodo e LNbits in modo sovrano. Se pensi che gestire un nodo sia troppo impegnativo per il momento, puoi collegare LNbits a un servizio di finanziamento custodial nel cloud come Opennode, Luna o Votage o al Lightning Tipbot su Telegram, solo per citarne alcuni.


## Volantino di LNbits

Vuoi consegnare alcune informazioni di base a un commerciante o a un tuo amico costruttori? Siamo lieti di annunciare il nostro primo volantino a disposizione di tutti. Il formato è quello tipico di un volantino di 6 pagine (2 pieghe) con una larghezza di 3508px e un'altezza di 2480px.

LNbits per i commercianti: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits per i costruttori: [EN](/assets/lnbits-builders-it.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


## Alcune nozioni di base

LNbits funziona sulla base del protocollo LNURL, il che significa che le richieste sono valide in due forme: o come link https://clearnet (non sono ammessi certificati autofirmati) o come link http://v2/v3 onion. Per offrire servizi LNbits come i codici QR LNURLp/w o le carte NFC, che possono essere utilizzati in libertà, è necessario aprire LNbits a clearnet (https).

Prima di installare LNbits, assicurati di aver letto e compreso le seguenti guide generali su cosa è LNbits e quali possibilità ti offre.

- [Guida LND](https://docs.lightning.engineering/) | Installazione di LND.
- [Esempio di configurazione LND](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Impostazioni LND.
- [Guida CLN](https://docs.corelightning.org/docs/installation) | Installazione di CLN.
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec.
- [Gestire una watchtower](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Molto importante!

Guide più dettagliate sull'utilizzo di LNbit in scenari d'uso specifici qui:
- [Guida introduttiva a LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Guida alla sottostazione.
- [ToDos per la vostra sicurezza con LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video.
- [Banche private su Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Guida alla sottostima.
- [Esegui i wallet dei custodial per i tuoi amici e parenti](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Guida alla sottostima.
- [LNbits per un piccolo ristorante/albergo](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Guida Substack.
- [Utilizzo del copilota LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Guida di Substack.
- [Avvia il tuo mercato NOSTR con LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Guida alla sottostazione.
- [Utilizzo di LNbits per progetti scolastici o per eventi di festival](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Guida all'utilizzo di Substack.


## Installare LNbits

### Guida all'installazione di base

LNbits può essere installato su qualsiasi macchina con sistema operativo Linux. Non richiede una macchina o un server potente, ma solo sufficiente memoria RAM e spazio su disco per il database. Può essere eseguito separatamente da un nodo BTC/LN (PC locale o VPS remoto) o insieme sulla stessa macchina con il nodo o già installato in una macchina software del nodo.

È possibile scegliere tra i gestori di pacchetti più comuni, come poetry e nix. Per impostazione predefinita, LNbits utilizza SQLite come database. È possibile utilizzare anche PostgreSQL, consigliato per le applicazioni con un carico elevato. [Ecco una guida per l'installazione di base usando poetry o nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Per tutti coloro che sono alle prime armi, troverai guide dettagliate passo-passo per far funzionare i tuoi LNbit in ambienti specifici:
- [LNbits su clearnet](https://ereignishorizont.xyz/lnbits-server/en/) di Axel.
- [LNbits su un VPS](https://github.com/TrezorHannes/vps-lnbits) di Hannes.
- [LNbits su cloudflare](https://www.nodeacademy.org/lnbits) di Leo.

È anche possibile trovare un video su [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Altri scenari di installazione qui](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Per i nodi software bundle, fare riferimento alla loro documentazione specifica su LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

### LNbits SaaS

Se non sei interessato alle questioni tecniche e non vuoi ospitare la tua fonte di finanziamento o il tuo LNbits, puoi utilizzare [LNbits SaaS version](https://saas.lnbits.com) (Software-as-a-service). È fondamentalmente come LNbits in un cloud, ma puoi definire tu stesso la fonte di finanziamento (ad esempio il tuo Nodo, un wallet LNbits, il LNtipbot, il fakewallet, ecc.) e le variabili di ambiente - cosa che per lo più non avviene in altre soluzioni cloud.

[Ecco una guida dettagliata su come utilizzare LNbits SaaS per casi d'uso specifici](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

### Fonti di finanziamento

LNbits non è un software per la gestione dei nodi, ma un sistema di contabilità focalizzato sugli LN in aggiunta a una fonte di finanziamento LND o CLN. Dopo la prima installazione è possibile visitare il tuo LNbits all'indirizzo http://localhost:5000/.

Per modificare la fonte di finanziamento, accedi all'URL del super-utente e selezionare una fonte di finanziamento all'interno di "Manage Server" o modificare il file .env modificando `LNBITS_BACKEND_WALLET_CLASS` con la fonte desiderata se si imposta `adminUI=TRUE` nel `.env`.

Il file .env si trova all'interno della cartella lnbits/ o lnbits/apps/data estendendo il comando per elencare i file nella propria directory con `ls -a`.

Potrebbe essere necessario installare altri pacchetti o eseguire ulteriori passaggi di configurazione, selezionando la fonte di finanziamento desiderata. Dopo un riavvio, la nuova configurazione sarà attiva.

Quali fonti di finanziamento posso utilizzare per LNbits?

LNbits può funzionare su molte fonti di finanziamento di Ligthning Network. Attualmente sono supportati CoreLightning, LND, LNbits, LNPay, OpenNode e altri vengono aggiunti regolarmente.

È importante scegliere una fonte che abbia una buona liquidità e una buona connessione tra peer. Se si utilizza LNbits per i servizi pubblici, i pagamenti degli utenti possono fluire felicemente in entrambe le direzioni.

Un wallet backend (fonte di finanziamento) può essere configurato utilizzando le seguenti variabili d'ambiente LNbits nel file `.env` o all'interno del tuo account superuser nella sezione Manage-Server.

Se si desidera utilizzare la versione .env, è possibile trovare i parametri qui:

#### CoreLightning

- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/percorso/lightning-rpc
- Spark (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - sPARK_TOKEN`: chiave_di_accesso_segreta

#### Lightning Network Daemon

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
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon o Bech64/Hex. Si può anche usare un macaroon crittografato con AES (maggiori informazioni)
  - `lND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Per criptare il macaroon, esegui `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

#### LNbits (un'altra istanza di LNbits)

- Istanza LNbits ospitata su un server cloud o sul proprio server domestico
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!NON utilizzare questo server per scopi produttivi/commerciali, ma solo per i test!!!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

#### Lightning TipBot

Per collegare il [Lightning Tipbot](https://t.me/LightningTipBot) da Telegram è necessario impostare i seguenti parametri:

  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Per ottenere la chiave è necessario eseguire /api in una chat privata con LightningTipbot su Telegram una volta.

Vedi anche questo tutorial su come installare [LNbits con LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

#### IBEX HUB

Registrati [qui](https://ibexpay.ibexmercado.com/onboard) e poi prendi le tue chiavi/token da lì, il punto finale è https://ibexpay-api.ibexmercado.com.

Per maggiori informazioni, vedi [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

#### LNPay

Affinché l'invoice listener funzioni, è necessario disporre di un URL accessibile pubblicamente nel tuo LNbits e impostare un [LNPay webhook](https://dashboard.lnpay.co/webhook/) che punti a `<l'host di LNbits>/wallet/webhook` con l'evento "Wallet Receive" e nessun segreto. L'impostazione `https://mylnbits/wallet/webhook` sarà l'url dell'endpoint che riceverà la notifica di ogni pagamento.

  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

#### Open Node

Affinché l'invoice funzioni, è necessario avere un URL accessibile pubblicamente nel tuo LNbits. L'impostazione del webhook è facoltativa.

  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

#### Alby

Alby è un'estensione del browser con funzionalità di wallet LN e conto LNDHUB che può essere utilizzato come fonte di finanziamento per gli LNbit. [Maggiori dettagli qui](https://getalby.com/).

Affinché l'invoice funzioni, è necessario disporre di un URL accessibile pubblicamente nel proprio LNbits. Non è necessaria alcuna impostazione manuale del webhook. È possibile generare un token di accesso Alby qui: https://getalby.com/developer/access_tokens/new

- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

### Guide aggiuntive / Risoluzione dei problemi

Ecco alcune istruzioni aggiuntive nel caso in cui ne avessi bisogno. Fai clic sulla freccia per espandere la descrizione.

#### I Killswitch 🚨

Ultimamente si sono verificati così tanti bug pericolosi non solo nell'intero settore, ma anche in LNbits, che abbiamo deciso di fare qualcosa al riguardo. Ora è possibile ricevere avvisi e/o intraprendere azioni dirette, quando si ripresenta una vulnerabilità o un bug che potrebbe portare alla perdita di fondi.

![killswitchn](assets/lnbits-killswitch.webp)

Se si passa al void-wallet, tutti gli utenti dell'istanza vedranno un banner giallo dove normalmente si trova l'avviso "LNbits è in Beta" accanto all'area del tema/lingua sulla destra - ed è l'indizio più ovvio che qualcosa è successo. Dai un'occhiata alla tua nuova scheda server evidenziata in verde nella parte sinistra della finestra.

Come funziona? Quando il killswitch è abilitato, un repository github segreto, disponibile solo al team di LNbits, viene controllato a un intervallo di X minuti (che può essere specificato). Se in questo repository viene pubblicato un bug vulnerabile, questo segnale fa scattare il killswitch su tutte le installazioni che si sono iscritte e fa passare la tua istanza lnbits all'uso del portafoglio vuoto. Se le nubi si sono diradate e hai installato l'aggiornamento di sicurezza, puoi impostare nuovamente la fonte di finanziamento sul tuo nodo, sul tuo wallet o su qualsiasi altra cosa stiate usando, anche attraverso la sezione Manage Server. Questo wiki contiene una sezione su come cambiare fonte di finanziamento se non si sa cosa configurare.

#### Differenza tra admin e superuser

L'interfaccia amministrativa di LNbits consente di modificare le impostazioni di LNbits tramite il frontend di LNbits. È disattivata per impostazione predefinita e la prima volta che si imposta la variabile di ambiente `LNBITS_ADMIN_UI=true` nel file `.env`, le impostazioni vengono inizializzate e saranno utilizzate. Da quel momento in poi verranno utilizzate le impostazioni del database al posto di quelle del file .env.

#### Super utente

Con l'interfaccia utente dell'amministratore abbiamo introdotto il superutente, che ha accesso al server e può quindi modificare le impostazioni che potrebbero mandare in crash il server o renderlo poco reattivo tramite il frontend e le API, come ad esempio la modifica della fonte di finanziamento. Il superutente è memorizzato solo nella tabella delle impostazioni del database. Dopo che le impostazioni sono state "riportate ai valori predefiniti" e riavviate, viene creato un nuovo superutente. Abbiamo anche aggiunto un decoratore per le rotte API per verificare l'esistenza di un superutente. Il suo ID non viene mai inviato tramite l'API e il frontend e riceve solo una riposta booleana (sì/no) se si è superutente o meno.

Solo il superutente può trasferire i satoshi a diversi wallet tramite la sezione "Ricarica".

Puoi anche inviare il superutente tramite webhook a un altro servizio quando viene creato. Maggiori informazioni qui https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Nel frontend troverai anche la possibilità di cambiare l'immagine del negozio che viene mostrata nella pagina "crea wallet" aprendo la sezione Gestisci server e scegliendo Tema -> Logo personalizzato.

#### Utenti amministratori

Variabile di ambiente: `LNBITS_ADMIN_USERS`, elenco virgola-seperato dell'ID utente. Gli utenti amministratori possono modificare le impostazioni nell'interfaccia utente dell'amministrazione, a eccezione delle impostazioni della fonte di finanziamento, perché ciò richiederebbe il riavvio del server e potrebbe rendere il server inaccessibile. Inoltre hanno accesso a tutte le estensioni a loro dedicate in `LNBITS_ADMIN_EXTENSIONS`.

#### Utenti ammessi

Variabile di ambiente: `LNBITS_ALLOWED_USERS`, elenco virgolettato dell'ID utente. Definendo questi utenti, LNbits non sarà più utilizzabile dal pubblico. Solo gli utenti e gli amministratori definiti possono accedere al frontend di LNbits.

##### Aggiornare LNbits

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

Se esegui Raspiblitz o MyNode, potresti avere bisogno di un'ulteriore opzione:

```
sudo systemctl restart lnbits
```

alla fine, perché esegue LNbits come servizio.

Su Umbrel/Citadel i comandi saranno:

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

##### Migrazione da SQLite a PostgreSQL

Se hai già installato LNbits e questo funziona su un database SQLite, ti consiglio vivamente di migrare a PostgreSQL se hai intenzione di far funzionare LNbits su grande scala.

È stato incluso uno script che può eseguire la migrazione in modo semplice. È necessario che PostgreSQL sia già installato e che ci sia una password per l'utente (vedi la guida all'installazione di PostgreSQL più sopra). Inoltre, l'istanza di LNbits deve essere eseguita una volta su PostgreSQL per implementare lo schema del database prima che la migrazione possa funzionare:

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

Spera che ora tutto funzioni e venga migrato... Avvia nuovamente LNbits e verificare che tutto funzioni correttamente.

##### Backup e ripristino del database

Consulta [questa guida molto dettagliata sul processo di backup e ripristino](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

##### Finanziare il mio wallet LNbits dal mio nodo non funziona

Se desideri inviare sats dallo stesso nodo che è la fonte di finanziamento dei tuoi LNbit, è necessario modificare il file lnd.conf.

I parametri da includere sono: `allow-circular-route=1`

Fallo nella sezione Application options del proprio lnd.conf. Su alcuni nodi bundle l'avvio di LND potrebbe altrimenti fallire.

NOTA: Ti consiglio di utilizzare la nuova estensione adminUI con l'opzione "TopUp" per aggiungere fondi a un conto LNbits.

##### Errore 426

Ho ricevuto l'errore: "lnurl deve essere inviato sopra un dominio https pubblicamente accessibile o su tor.426 aggiornamento richiesto".

Questo errore di solito è dovuto al fatto che LNbits dietro un tunnel ngnix non inoltra correttamente l'indirizzo LNURL. Ferma LNbits e modifica il file .env aggiungendo questa riga:

`FORWARDED_ALLOW_IPS=*`

Inoltre, se usi una configurazione ngnix, assicurati di avere questi header nella configurazione ngnix:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

##### Errore di rete

Ho ottenuto "errore https", "errore di rete" o altri durante la scansione di un QR.

Brutte notizie, si tratta di un errore di routing che potrebbe avere molte ragioni. Per prima cosa controlla l'LNURL del QR con il [Lightning Decoder](https://lightningdecoder.com/) se trovi qualcosa di strano. Proviamo alcuni dei possibili problemi e le loro soluzioni.

LNbits funziona solo via Tor, non è possibile aprirlo su un dominio pubblico come lnbits.yourdomain.com

- Dato che vuoi che la tua configurazione rimanga così, apri il tuo wallet LNbits utilizzando l'URI .onion e crealo di nuovo. In questo modo il QR viene generato per essere accessibile tramite questo URI .onion, quindi solo via Tor. Non generare il QR da un URI .local, perché non sarà raggiungibile via internet, ma solo dalla propria home-LAN.
- Apri l'applicazione del wallet LN utilizzata per la scansione del QR e questa volta utilizza Tor (vedi le impostazioni dell'applicazione del wallet). Se l'app non offre Tor, è possibile utilizzare Orbot (Android). Per istruzioni dettagliate su come aprire i tuoi LNbit per clearnet/https, consulta la sezione Installazione.

##### Impedire ad altri di generare wallet con i miei LNbit

Quando si gestisce il nodo LNbits in clearnet, tutti possono generare su di esso un wallet. Dal momento che i fondi del tuo nodo sono legati a questi wallet, potresti volerlo impedire. Ci sono due modi per farlo:

Configura gli utenti e le estensioni consentite nel file `.env` ([vedi l'esempio del file env qui](https://github.com/lnbits/lnbits/blob/main/.env.example)). Questo funziona solo se usi l'impostazione `adminUI=FALSE` nel file .env, altrimenti è necessario farlo nella sezione Gestione del server -> Utenti -> Utenti consentiti. Tutti gli altri non saranno poi autorizzati.

##### Personalizzare il periodo di scadenza dell'invoice

Ora è possibile generare invoice con una scadenza personalizzata. Compatibile con i backend: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet finora!

Puoi impostare `LIGHTNING_INVOICE_EXPIRY` nel file .env o utilizzare l'AdminUI per modificare il valore predefinito per tutte le invoice. C'è anche un nuovo campo nell'endpoint /api/v1/payments in cui è possibile impostare la scadenza nei dati JSON.

### Wallet-URL cancellato

#### Wallet sul server demo legend.lnbits

Salva sempre una copia del tuo wallet-URL, Export2phone-QR o LNDhub, in un luogo sicuro, per i tuoi wallet. LNbits non può aiutarti a recuperarli in caso di smarrimento.

#### Wallet sulla propria fonte/nodo di finanziamento

Salva sempre una copia del tuo wallet-URL, Export2phone-QR o LNDhub, in un luogo sicuro, per i tuoi wallet. Puoi trovare tutti gli utenti LNbits e gli ID dei wallet nell'estensione LNbits User Manager o nel database sqlite. Per modificare o leggere il database di LNbits, andate nella cartella LNbits /data e cercate il file sqlite.db. È possibile aprirlo e modificarlo con excel o con un editor SQL dedicato come [SQLite browser](https://sqlitebrowser.org/).

Inoltre puoi scaricare i wallet tramite cli e visualizzare ogni wallet all'interno del database.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

L'output sarà simile a questo

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

e se desideri inserire questi valori in un url come questo

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

In questo modo sostituisci "f8a43fc363ea428db5c53b3559935f1f" con il valore che precede il nome (nel nostro esempio f8a43fc363ea428db5c53b3559935f1f) e "1280ff5910a9c485a782a2376f338b6c" è il tuo utente e dovrebbe diventare il valore mostrato dopo il nome. Per uscire da sqlite3 inserisci

```
.quit
```

##### LNURL per un indirizzo di posta elettronica viceversa

Provate questo [encoder](https://lnurl-codec.netlify.app/) di fiatjaf o [questo](https://lightningdecoder.com/). Per pagare o controllare un LNURLp si può anche usare [LNurlpay](https://wwww.lnurlpay.com/). Dovrebbe essere indicato HTTPS e non HTTP.

##### Configurare un commento che le persone vedono quando pagano al mio LNURLp QR

Quando si crea un LNURL-p, per impostazione predefinita la casella dei commenti non è riempita. Ciò significa che i commenti non possono essere allegati ai pagamenti.

Per consentire i commenti, aggiungi la lunghezza dei caratteri della casella, da 1 a 250. Una volta inserito un numero, la casella dei commenti verrà visualizzata nel processo di pagamento. Puoi anche modificare un LNURL-p già creato e aggiungere quel numero.

![lnbits comments](assets/lnbits-comments.webp)

##### Depositare BTC onchain su LNbits

Esistono due modi per scambiare sats da BTC onchain a LN BTC (rispettivamente a LNbits).

###### Tramite un servizio di swap esterno.

Altri utenti che non hanno accesso al tuo LNbits possono usare un servizio di swap come [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) o [ZigZag](https://zigzag.io/). Questo è utile se fornisci solo invoice LNURL/LN dalla tua istanza LNbits, ma se un cliente dispone solo di sats onchain, dovrà  quindi prima scambiarli dalla propria parte. La procedura è semplice: l'utente invia btc onchain al servizio di swap e fornisce l'invoice LNURL/LN di LNbits come destinazione dello swap.

###### Utilizzo Onchain dell'estensione Boltz LNbits.

Tieni presente che si tratta di un wallet separato, non quello di LN BTC che è rappresentato da LNbits come "il tuo portafoglio" sulla tua fonte di finanziamento LN. Questo wallet onchain può essere utilizzato anche per scambiare LN BTC con (ad esempio, il tuo hardwarewallet) utilizzando l'estensione LNbits Boltz o Deezy. Se gestisci un negozio web che è collegato al tuo LNbits per i pagamenti in LN, è molto utile scaricare regolarmente tutti i sats da LN a onchain. In questo modo si ottiene più spazio nei canali LN per poter ricevere nuovi sats.

Procedura per chi non ha un hardware wallet Bitcoin:
- Utilizza Electrum o Sparrow per creare un nuovo wallet onchain e salva il seed di backup in un luogo sicuro.
- Vai alle informazioni sul wallet e copia il file xpub.
- Vai su LNbits - Estensione Onchain e crea un nuovo wallet watch-only con questo xpub.
- Vai su LNbits - estensione Tipjar e creare un nuovo Tipjar. Seleziona anche l'opzione onchain oltre al wallet LN.
- Opzionale - Vai su LNbits - estensione SatsPay e crea un nuovo addebito per onchain btc. Puoi scegliere tra onchain e LN o entrambi. Verrà quindi creata un'invoice che potrà essere condivisa.
- Opzionale - Se si utilizza LNbits collegato a una pagina Wordpress + Woocommerce, una volta creato/collegato un wallet watch-only al wallet del negozio LN BTC, il cliente avrà entrambe le opzioni di pagamento nella stessa schermata.

Quando si riceve un pagamento in LNbits, nel registro delle transazioni viene visualizzato solo il tipo di transazione ripresa.

![lnbits payment details](assets/lnbits-payment-details.webp)

Nella panoramica delle transazioni troverete una piccola freccia verde per i fondi ricevuti e una freccia rossa per i fondi inviati.

Se fai clic su queste frecce, un popup di dettagli mostra i messaggi allegati e il nome del mittente, se indicato.

Per configurare un nome da far apparire nei pagamenti, in LNbits non è attualmente possibile farlo - ma riceverlo. Questo è possibile solo se il wallet LN del mittente supporta [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) come [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Vedrai quindi un alias/pseudonimo nella sezione dei dettagli delle tue transazioni LNbits (clicca sulle frecce). Nota che è possibile indicare qualsiasi nome e che potrebbe non essere correlato al nome del vero mittente, se lo si riceve.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Per importare il tuo conto LNbits in un'app wallet, apri il tuo LNbits con l'account/il wallet che vuoi utilizzare, vai su "gestione estensioni" e attiva l'estensione LNDHUB. Apri l'estensione LNDHUB, sceglie il wallet che si desideri utilizzare e scansiona il QR "admin" o "invoice only", a seconda del livello di sicurezza desiderato per quel wallet.

È possibile utilizzare [Zeus](https://zeusln.app/) o [Bluewallet](https://bluewallet.io/) come applicazioni wallet per un account lndhub, dove BW supporta più di un portafoglio.

Quando esegui questa operazione, consiglio di impostare anche l'URI della rete LN su quello del tuo nodo. Se l'istanza di LNbits è solo su Tor, è necessario utilizzare queste applicazioni con Tor attivato. Anche in questo caso è necessario aprire la pagina di LNbits attraverso il tuo indirizzo Tor .onion.

Se verifichi l'errore "tipo di hash non supportato" quando utilizzi un ypub nell'estensione On-chain, verifica se l'istanza di LNbits utilizza python 3.10, potrebbe essere affetta da [questo problema](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Modifica il file openssl.cnf come descritto nella risposta di stackoverflow e riavvia LNbits.

### Attrezzi e utensili da costruzione con LNbits

LNbits dispone di ogni sorta di [API aperte](https://legend.lnbits.com/docs) e di strumenti per programmare e connettersi a molti dispositivi diversi per una miriade di casi d'uso.

Se sei alle prime armi con la creazione di gadget, iniziate con questa [MakerBits presentations](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) di Ben Arc sulla costruzione di gadget basati su LNbits.

#### IMPORTANTE:
- LNbits funziona sulla base del protocollo LNURL, le cui richieste sono valide in due forme: o come link https://clearnet (non sono ammessi certificati autofirmati) o come link http://v2/v3 onion. Per offrire servizi LNbits come i codici QR LNURLp/w o le carte NFC, che possono essere utilizzati nella libertà, è necessario aprire LNbits in clearnet (https).
- Per alimentare l'esp32 utilizza solo cavi dati. Non tutti i cavi supportano i dati oltre all'alimentazione dell'esp. Non saresti il primo se il cavo fornito con l'esp fosse di sola alimentazione.
- Assicurati di non utilizzare un hub USB con altri dispositivi collegati. Questo può portare a strani effetti difficili da debuggare (ad esempio, il mancato avvio o l'arresto).
- Per realizzare i progetti esp con MacOS è necessario un driver UART Bridge. Se hai problemi con il driver su sistemi Mac o Linux, puoi trovarli qui o, se si tratta di un display TTGO, qui. Se hai problemi di connessione con Windows, assicurati di scaricare la VECCHIA versione 11.1.0 perché quella più recente non funziona! Per verificare la connessione, qui si può trovare anche un terminale seriale, impostato su un baudrate di 115200.
- Anche se è molto più comodo usare Platform.io (ad esempio, le dipendenze vengono installate automaticamente), raccomandiamo l'uso di Arduino per tutti coloro che sono alle prime armi con la costruzione.
- TT-Go Display S3: Il colore della linguetta della pellicola protettiva dello schermo indica esattamente quale controller (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...) è stato utilizzato per costruirlo. Conservalo per poter eseguire il debug se programmi e lo schermo non visualizza correttamente la grafica, ad esempio colori sbagliati, immagini speculari o pixel vaganti ai bordi. Se mai dovessi avere bisogno di farlo, c'è una guida epica sulla regolazione per i diversi schermi.
- Usa sempre lnurl239xx minuscolo invece di LNURLl239xx.
- L'aggiunta di lightning:lnurl1234xyz creerà un QR che richiede l'apertura del wallet dell'utente per questa invoice alla scansione (ultima app lightning installata su iOS, impostazione in Android).
- Se stai flashando un esp32 via web funzionerà solo con questi browser (TL:DR Chrome, Edge e Opera).
- Tieni presente il riferimento PIN-OUT per l'esp.
- Quando utilizzi FOSSoftware o FOSGuide, linkate sempre l'autore. Tutti amano veder crescere il proprio bambino e questo dà inizio a una catena di costruzione che è davvero impressionante da vedere :).

Vieni nel [Gruppo Telegram di Makerbits](https://t.me/makerbits) se hai bisogno di aiuto per un progetto - ci siamo noi!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Ecco alcune categorie di progetti che puoi realizzare con LNbits:
- [Dispositivo di firma Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Lampada Nostr Zap](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
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
