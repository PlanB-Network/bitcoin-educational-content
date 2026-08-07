---
name: Aggiornare BTCPay Server
description: Applica un aggiornamento di sicurezza alla tua istanza BTCPay Server e ruota le credenziali che contano
---

![cover](assets/cover.webp)

Gestire il proprio processore di pagamenti significa essere anche il proprio team di sicurezza. Quando i manutentori di BTCPay Server pubblicano una release di sicurezza, nessuno applicherà la patch alla tua istanza al posto tuo: l'aggiornamento, la verifica e la rotazione delle credenziali che ne seguono spettano a te.

Questo tutorial illustra l'intera procedura, qualunque sia il modo in cui hai distribuito BTCPay Server: controllare la versione in esecuzione, applicare l'aggiornamento in base al tipo di distribuzione, verificare che sia effettivamente andato a buon fine e ruotare i segreti che un attaccante potrebbe aver catturato mentre la tua istanza era vulnerabile.

Se non hai ancora distribuito BTCPay Server, inizia dalla guida di installazione:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## La vulnerabilità critica di agosto 2026

⚠️ **Allerta di sicurezza critica (7 agosto 2026):** una vulnerabilità critica che colpisce BTCPay Server viene sfruttata attivamente e può portare alla perdita di fondi. Aggiorna la tua istanza alla **versione 2.4.2** immediatamente tramite `Admin Dashboard > Server > Maintenance > Update`, poi controlla che il footer mostri `2.4.2`. Se non puoi aggiornare subito, spegni il tuo BTCPay Server. Una volta aggiornato, devi anche rinnovare completamente i tuoi macaroon e il tuo `macaroons.db`, rinnovare completamente le stringhe di autenticazione di qualsiasi altro backend Lightning e, se hai generato un hot wallet on-chain all'interno di BTCPay Server, spostare quei fondi e ricreare il wallet. Gli integratori dovrebbero anche aggiornare NBXplorer alla versione 2.6.10. Fonte: [note di rilascio di BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

La versione 2.4.2 è stata pubblicata il 7 agosto 2026. Le note di rilascio dichiarano che risolve una vulnerabilità critica già sfruttata attivamente, segnalata da `brunoerg` e `benthecarman` tramite lo sforzo del Bitcoin Red Team. La stessa release risolve anche un bypass dell'autenticazione a due fattori TOTP tramite l'autenticazione Basic di Greenfield, e disattiva l'autenticazione Basic di Greenfield per impostazione predefinita cinque minuti dopo la creazione dell'account.

Da "sfruttata attivamente" derivano due conseguenze:

- **L'aggiornamento non è opzionale e non è qualcosa da pianificare per la settimana prossima.** Un'istanza non aggiornata e raggiungibile da internet deve essere aggiornata oppure spenta.
- **L'aggiornamento da solo non basta.** Se la tua istanza è stata compromessa prima che tu applicassi la patch, l'attaccante potrebbe già possedere copie delle tue credenziali Lightning e di qualsiasi materiale di chiavi di hot wallet generato per te da BTCPay Server. Questi segreti restano validi dopo l'aggiornamento finché non li ruoti. La sezione sulla rotazione qui sotto è la parte che le persone saltano, ed è la parte che protegge davvero i tuoi fondi.

## Passo 1 — Scopri quale versione stai eseguendo

Accedi al tuo BTCPay Server e guarda il **footer di qualsiasi pagina**: lì viene mostrata la stringa della versione. Puoi anche aprire `Admin Dashboard > Server > Maintenance`, che mostra la versione attuale e i controlli di aggiornamento.

Se la tua istanza espone la Greenfield API, `GET /api/v1/server/info` restituisce anch'essa la versione.

Qualsiasi versione inferiore a `2.4.2` è vulnerabile.

## Passo 2 — Aggiorna

### Distribuzione Docker self-hosted (l'installazione standard)

Questo copre la distribuzione Docker ufficiale, quella che ottieni dalla documentazione di BTCPay Server, dal launcher one-click di LunaNode e dalla maggior parte delle installazioni su VPS.

Il percorso più semplice è l'interfaccia web:

1. Vai su `Admin Dashboard > Server > Maintenance`.
2. Clicca su **Update**.
3. Attendi che i container vengano scaricati e riavviati. L'interfaccia sarà indisponibile per alcuni minuti.

Se l'interfaccia web non è raggiungibile, o preferisci vedere i log, procedi via SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

In un'installazione predefinita `$BTCPAY_BASE_DIRECTORY` è `/root`, quindi la directory è `/root/btcpayserver-docker`. Lo script scarica le immagini più recenti, ricrea i container e stampa le versioni risultanti.

La distribuzione Docker include NBXplorer insieme a BTCPay Server, quindi un aggiornamento standard porta anche NBXplorer alla versione raccomandata `2.6.10`. Se esegui NBXplorer separatamente — tipico per gli integratori e per gli stack personalizzati — aggiornalo esplicitamente.

### Umbrel

Apri la dashboard di Umbrel, vai su **App Store**, trova BTCPay Server e applica l'aggiornamento se disponibile.

⚠️ **Importante:** i pacchetti dell'app store sono ripacchettizzati dal team Umbrel e possono essere in ritardo rispetto a monte di ore o giorni. Controlla la versione nel footer di BTCPay Server dopo l'aggiornamento. Se è ancora inferiore a `2.4.2`, **ferma l'app** dalla dashboard di Umbrel e attendi la release pacchettizzata invece di lasciare in esecuzione un'istanza vulnerabile.

La guida dedicata a Umbrel copre l'app stessa:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Stessa logica: aggiorna BTCPay Server dal marketplace di StartOS, poi verifica la versione nel footer. Se la versione pacchettizzata non è ancora `2.4.2`, ferma il servizio finché non lo è.

### Hosting gestito e di terze parti

Se qualcun altro gestisce la tua istanza (un provider di hosting, un'associazione, il server di un amico), hai comunque bisogno della conferma. Chiedi all'operatore la stringa di versione mostrata nel footer, e chiedi esplicitamente se la rotazione delle credenziali post-aggiornamento descritta di seguito è stata eseguita. "Abbiamo aggiornato" non è la stessa risposta di "abbiamo ruotato i tuoi macaroon".

## Passo 3 — Verifica che l'aggiornamento sia effettivamente andato a buon fine

Ricarica l'interfaccia di BTCPay Server e leggi la versione nel footer. Deve mostrare `2.4.2` o superiore.

Non fidarti del fatto che il comando di aggiornamento termini senza errori: su macchine con risorse limitate uno scaricamento di immagine può fallire silenziosamente e lasciare in esecuzione il container precedente. Leggi la versione, ogni volta.

## Passo 4 — Ruota le tue credenziali

Questo è il passo che trasforma "patchato" in "sicuro". Poiché la vulnerabilità veniva sfruttata prima che la correzione fosse rilasciata, considera ogni segreto detenuto dalla tua istanza come potenzialmente noto a un attaccante.

### Lightning: LND

Rigenera i macaroon **e** il file `macaroons.db`. Eliminare solo i file macaroon non basta — LND deriva i macaroon dalla chiave radice memorizzata in `macaroons.db`, quindi un attaccante in possesso di una copia di un vecchio macaroon mantiene l'accesso finché quel database non viene ricreato.

La procedura è: ferma LND, rimuovi `macaroons.db` e i file `*.macaroon` dalla directory di rete (per mainnet, `data/chain/bitcoin/mainnet/` all'interno della directory dati di LND), poi riavvia e sblocca LND, che li ricrea. Esegui prima un backup della directory, e ricollega ogni applicazione che usava i vecchi macaroon — BTCPay Server stesso, Zeus, Thunderhub, RTL, Alby e qualsiasi script tu abbia scritto.

Se esponi anche LND su internet, rivedi contemporaneamente il suo certificato TLS e qualsiasi credenziale in `lnd.conf`.

### Lightning: altri backend

Qualsiasi cosa che si autentica al tuo nodo con una stringa deve ottenere una nuova stringa:

- **Core Lightning**: rigenera la rune o le credenziali di accesso usate dalla connessione.
- **Phoenixd**: ruota la password HTTP.
- **LNbits e simili**: revoca e riemetti le chiavi admin e invoice.
- **Stringhe di connessione al nodo remoto** memorizzate nelle impostazioni del negozio di BTCPay Server: riscrivile con i nuovi segreti.

### Hot wallet on-chain generato all'interno di BTCPay Server

Se hai lasciato che BTCPay Server generasse un wallet on-chain per te — anziché collegare un hardware wallet o importare un xpub le cui chiavi non hanno mai toccato il server — quel seed ha vissuto sulla macchina.

Consideralo bruciato:

1. Crea un nuovo wallet, idealmente con un hardware wallet in modo che le chiavi non risiedano mai più sul server.
2. Sposta i fondi dal vecchio wallet al nuovo.
3. Sostituisci lo schema di derivazione nelle impostazioni del negozio con il nuovo wallet.
4. Non riutilizzare mai il vecchio seed.

Le configurazioni watch-only (xpub o hardware wallet) non necessitano di questo: le chiavi private non sono mai state sul server. Questo è esattamente il motivo per cui la guida di installazione le raccomanda.

### Account BTCPay Server e chiavi API

Già che ci sei:

- Cambia le password di ogni account utente sull'istanza.
- Revoca e riemetti tutte le **chiavi API** Greenfield.
- Re-iscrivi l'autenticazione a due fattori, dato che la 2.4.2 risolve un bypass del 2FA.
- Apri `Admin Dashboard > Server > Users` e controlla che non esista alcun account inatteso.
- Rivedi i recenti **payout**, **pull payment** e **rimborsi** alla ricerca di voci che non hai creato tu.
- Rivedi i tuoi webhook e i loro segreti.

## Passo 5 — Resta informato per la prossima volta

Le release di sicurezza aiutano solo gli operatori che ne vengono a conoscenza:

- Segui le [release di BTCPay Server su GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub può inviarti un'email a ogni nuova release di un repository.
- Segui i canali di annuncio del progetto e il [blog ufficiale](https://blog.btcpayserver.org/).
- Mantieni la tua istanza su una versione che puoi aggiornare rapidamente: più sei indietro, più diventa doloroso un aggiornamento di emergenza.

Il self-hosting ti dà sovranità sui tuoi pagamenti. Il costo di quella sovranità è esattamente questo: leggere le note di rilascio ed essere tu a fare l'aggiornamento.