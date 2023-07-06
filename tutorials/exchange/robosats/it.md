---
name: Robosats

description: Come utilizzare Robosats
---

![cover](assets/cover.jpeg)

# Robosats

RoboSats (https://learn.robosats.com/) è un modo semplice per scambiare Bitcoin in modo privato con valute nazionali. Semplifica l'esperienza peer-to-peer e utilizza fatture lightning hold per ridurre al minimo i requisiti di custodia e fiducia.

![video](https://youtu.be/XW_wzRz_BDI)

## Guida

> Questa guida è di Bitocin Q&A (https://bitcoiner.guide/robosats/). Tutto il merito va a lui, supportatelo lì (https://bitcoiner.guide/contribute); BitcoinQ&A è anche un mentore di Bitcoin. Contattatelo per il mentoring!

![image](assets/0.png)

RoboSats - Uno scambio P2P semplice e privato basato su Lightning

## Prima di iniziare

### Cose che devi sapere

| Gergo        | Definizione                                                                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | La tua identità di scambio privata generata automaticamente. Non riutilizzare lo stesso robot più di una volta poiché potrebbe compromettere la tua privacy.                                                                                      |
| Token        | Una stringa di caratteri casuali utilizzata per generare il tuo robot unico.                                                                                                                                                                      |
| Maker        | Un utente che crea un'offerta per comprare o vendere Bitcoin.                                                                                                                                                                                     |
| Taker        | Un utente che accetta l'offerta di un altro utente per comprare o vendere Bitcoin.                                                                                                                                                                |
| Bond         | Una quantità di Bitcoin bloccata da entrambi i partecipanti come garanzia per giocare correttamente e completare la propria parte dello scambio. I bond sono di solito il 3% dell'importo totale dello scambio e sono supportati da fatture Hodl. |
| Trade Escrow | Utilizzato dal venditore come metodo per trattenere l'importo dello scambio di Bitcoin, utilizzando nuovamente fatture Hodl.                                                                                                                      |
| Commissioni  | RoboSats addebita lo 0,2% dell'importo dello scambio, che viene diviso tra il maker e il taker. Il taker paga lo 0,175% e il maker paga lo 0,025%.                                                                                                |

## Cose che devi avere

### Un portafoglio Lightning

RoboSats è nativo di Lightning, quindi avrai bisogno di un portafoglio Lightning per finanziare il bond e ricevere i sats acquistati come acquirente. Dovresti fare attenzione nella scelta del tuo portafoglio, poiché non tutti sono compatibili con la tecnologia utilizzata da RoboSats.

Se sei un gestore di nodi, Zeus è di gran lunga la migliore opzione. Se non hai il tuo nodo, ti consiglio vivamente Phoenix, un portafoglio mobile multi-piattaforma con una configurazione semplice e accesso a Lightning. Phoenix è stato utilizzato nella produzione di questa guida.

### Un po' di Bitcoin

I compratori e i venditori devono finanziare un bond prima che possa avvenire qualsiasi scambio. Di solito si tratta di una quantità molto piccola (~3% dell'importo dello scambio), ma è comunque un requisito indispensabile.

Stai utilizzando RoboSats per acquistare i tuoi primi sats? Perché non farti prestare la piccola quantità necessaria per iniziare da un amico!? Se sei da solo, ecco alcune altre ottime opzioni per ottenere alcuni sats senza KYC per iniziare.

### Accesso a RoboSats

Ovviamente avrai bisogno di accedere a RoboSats! Ci sono quattro modi principali per farlo:

1. Tramite Tor Browser (Consigliato!)
2. Tramite un browser web normale (Non consigliato!)
3. Tramite l'APK Android
4. Il tuo client personale

Se sei nuovo al browser Tor, scopri di più e scaricalo [qui](https://www.torproject.org/download/).
Una breve nota per gli utenti iOS che desiderano accedere a RoboSats tramite Tor dai loro telefoni. 'Onion Browser' non è Tor Browser. Invece, utilizzare Orbot + Safari e Orbot + DuckDuckGo.

## Acquisto di Bitcoin

I seguenti passaggi sono stati eseguiti nel maggio 2023 utilizzando la versione 0.5.0, accessibile tramite il browser Tor. I passaggi dovrebbero essere identici per gli utenti che accedono a RoboSats tramite l'APK Android.

Al momento della stesura, RoboSats è ancora in fase di sviluppo attivo, quindi l'interfaccia potrebbe cambiare leggermente in futuro, ma i passaggi di base necessari per completare la transazione dovrebbero rimanere in gran parte invariati.

> Quando carichi per la prima volta RoboSats, verrai accolto da questa pagina iniziale. Fai clic su Start.

![image](assets/2.png)

Genera il tuo token e conservalo in un luogo sicuro, come un'app di appunti crittografata o un gestore di password. Questo token può essere utilizzato per recuperare il tuo ID Robot temporaneo nel caso in cui il tuo browser o app si chiuda a metà strada durante una transazione.

![image](assets/3.png)

Incontra la tua nuova identità di Robot, quindi fai clic su Continua.

![image](assets/4.png)

Fai clic su Offerte per sfogliare il libro degli ordini. In cima alla pagina puoi filtrare le tue preferenze. Assicurati di prendere nota delle percentuali di garanzia e del premio rispetto al tasso di cambio medio.

- Scegli Acquista
- Scegli la tua valuta
- Scegli il tuo metodo di pagamento

![image](assets/5.png)

> Fai clic sull'offerta che desideri accettare. Inserisci l'importo (nella tua valuta fiat scelta) che desideri acquistare dal venditore, quindi controlla nuovamente i dettagli e fai clic su Prendi Ordine.

Se il venditore non è online (individuabile da un punto rosso sulla sua immagine del profilo), vedrai un avviso che la transazione potrebbe richiedere più tempo del solito. Se continui e il venditore non procede in tempo, verrai compensato del 50% dell'importo della garanzia per il tempo perso.

![image](assets/6.png)

Successivamente, devi bloccare la tua garanzia di transazione pagando la fattura sullo schermo. Si tratta di una fattura di blocco che viene congelata nel tuo portafoglio. Verrà addebitata solo se non riesci a completare il tuo lato della transazione.

![image](assets/7.png)

Nel tuo portafoglio Lightning, scannerizza il codice QR e paga la fattura.

![image](assets/8.png)

Successivamente, nel tuo portafoglio Lightning genera una fattura per l'importo mostrato e incollala nello spazio fornito.

![image](assets/9.png)

Attendi che il venditore blocchi l'importo della sua transazione. Quando ciò avviene, RoboSats passerà automaticamente al passaggio successivo in cui si aprirà la finestra di chat. Saluta e chiedi al venditore le informazioni di pagamento in valuta fiat. Una volta fornite, invia il pagamento tramite il metodo scelto, quindi confermalo in RoboSats. Tutta la chat in RoboSats è crittografata con PGP, il che significa che solo tu e il tuo partner di transazione potete leggere i messaggi.

![image](assets/10.png)

Una volta che il venditore conferma di aver ricevuto il pagamento, RoboSats rilascia automaticamente il pagamento utilizzando la fattura fornita in precedenza.

![image](assets/11.png)

Quando la fattura viene pagata, la transazione è completata e la tua garanzia viene sbloccata. Vedrai quindi un riepilogo della transazione.

![image](assets/12.png)

Controlla il tuo portafoglio Lightning per confermare che i satoshi siano arrivati.

![image](assets/13.png)

## Funzionalità aggiuntive

Oltre all'ovvio acquisto e vendita di Bitcoin, RoboSats ha alcune altre funzionalità che dovresti conoscere.
Garage dei Robot
Vuoi avere più scambi contemporaneamente, ma non vuoi condividere la stessa identità tra di loro? Nessun problema! Clicca sulla scheda Robot, genera un Robot aggiuntivo e crea o prendi il tuo prossimo ordine.
![image](assets/14.png)

### Creazione di ordini

Oltre a prendere l'offerta di qualcun altro, puoi crearne una tua e aspettare che un altro Robot venga da te.

- Apri la pagina di creazione.
- Scegli se il tuo ordine è per comprare o vendere Bitcoin.
- Inserisci l'importo e la valuta con cui vuoi comprare/vendere.
- Inserisci il metodo di pagamento che sei disposto a utilizzare.
- Inserisci la percentuale di "Premium sul mercato" che sei disposto ad accettare. Nota che questa può essere una cifra negativa per fare un'offerta a un prezzo scontato rispetto al prezzo di mercato attuale.
- Clicca su Crea ordine.
- Paga la fattura Lightning per bloccare il tuo Maker Bond.
- Il tuo ordine è ora attivo. Siediti e aspetta che qualcuno lo accetti.

![image](assets/15.png)

### Pagamenti on-chain

RoboSats è incentrato su Lightning, ma gli acquirenti hanno la possibilità di ricevere i loro sats su un indirizzo Bitcoin on-chain. Gli acquirenti possono selezionare questa opzione dopo aver bloccato il loro bond. Dopo aver selezionato on-chain, l'acquirente vedrà una panoramica delle commissioni. Le commissioni aggiuntive per questo servizio includono:

- Una commissione di scambio raccolta da RoboSats - Questa commissione è dinamica e varia a seconda di quanto è occupata la rete Bitcoin.
- Una commissione di mining per la transazione di pagamento - Questa è configurabile dall'acquirente.

![image](assets/16.png)

### Scambi P2P

RoboSats consente agli utenti di scambiare sats dentro o fuori dal loro Lightning Wallet. Basta cliccare sul pulsante di scambio in cima alla pagina delle offerte per visualizzare le offerte di scambio attuali.

Come acquirente di un'offerta di "Scambio in", invii Bitcoin on-chain al peer e ricevi sats indietro, al netto delle commissioni e/o dei premi pubblicizzati, nel tuo Lightning Wallet. Come acquirente di un'offerta di "Scambio out", invii sats tramite Lightning e ricevi Bitcoin, al netto di eventuali commissioni e/o premi, nel tuo indirizzo on-chain. Gli utenti di Samourai o Sparrow Wallet possono anche sfruttare la funzione Stowaway per completare uno scambio.

Le offerte di scambio di RoboSats possono anche includere alternative ancorate a Bitcoin come RBTC, LBTC e WBTC. Dovresti fare molta attenzione se interagisci con questi token poiché tutti presentano vari compromessi. Il Bitcoin ancorato non è Bitcoin!

![image](assets/17.png)

### Esegui il tuo client RoboSats

Gli utenti di Umbrel, Citadel e Start9 possono installare il proprio client RoboSats direttamente sul loro nodo. I vantaggi di farlo sono elencati come segue:

- Tempi di caricamento drasticamente più veloci.
- Più sicuro: controlli quale app client RoboSats esegui.
- Accesso sicuro a RoboSats da qualsiasi browser/dispositivo. Non è necessario utilizzare TOR se ti trovi nella tua rete locale o stai usando una VPN: il backend del tuo nodo gestisce la torificazione necessaria per l'anonimizzazione.
- Consente di controllare a quale coordinatore di mercato P2P ti connetti (impostato su robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion per impostazione predefinita)

![image](assets/18.png)

## FAQ

### Posso essere truffato?

Come acquirente, se hai inviato la valuta fiat richiesta per il tuo lato della transazione, ma il venditore non ti rilascia i satoshi, puoi aprire una controversia. Se durante questo processo di controversia riesci a dimostrare agli arbitri di RoboSats di aver inviato la valuta fiat, i fondi in escrow del venditore e il suo trade bond ti saranno rilasciati. Come posso annullare una transazione?

Puoi annullare una transazione dopo aver pubblicato il tuo trade bond cliccando sul pulsante Collaborative Cancel nel menu della transazione. Se il tuo partner di transazione è d'accordo ad annullare, non incorrerai in alcuna commissione. Ma se il tuo partner di transazione desidera completare la transazione e tu decidi comunque di annullare, perderai il tuo trade bond.

### RoboSats funziona con il metodo di pagamento 'X'?

Non ci sono restrizioni sui metodi di pagamento in RoboSats. Se non vedi offerte nel tuo metodo desiderato, crea la tua offerta utilizzandolo!

![image](assets/19.png)

### Cosa apprende RoboSats su di me quando lo uso?

Se utilizzi RoboSats tramite Tor o l'app Android, assolutamente nulla! Scopri di più qui.

- Tor protegge la privacy della tua rete.
- La crittografia PGP mantiene privata la chat di trading.
- L'assenza di account significa un Robot per ogni transazione. Ciò significa che RoboSats non può correlare più transazioni a un'unica entità.

Tuttavia, ci sono alcune eccezioni! Lightning è abbastanza privato come mittente, ma non come destinatario. Se ricevi sul tuo nodo Lightning, il tuo ID del nodo viene condiviso nelle tue fatture. Questo ID del nodo fornisce a chiunque lo conosca un punto di partenza per cercare di collegare la tua attività on-chain. Questo è vero anche se un utente sceglie di ricevere la propria transazione tramite un pagamento on-chain.

Per mitigare questo rischio, gli utenti possono optare per l'utilizzo di una soluzione come un Proxy Wallet per Lightning o Coinjoin per on-chain.

### Federazione

Al momento c'è un unico coordinatore di RoboSats gestito dal team di sviluppatori di RoboSats. Nel Bitcoin, qualsiasi forma di centralizzazione rende più facile il bersaglio per i governi o i regolatori che potrebbero non guardare con favore un servizio specifico.

Essendo RoboSats un progetto Open Source, chiunque potrebbe prendere il codice e iniziare a gestire il proprio coordinatore. Sebbene ciò decentralizzi in parte il rischio da un singolo bersaglio, frammenta anche un mercato di liquidità già esiguo.

Il team di RoboSats è consapevole di ciò e ha iniziato a lavorare su un modello federato. Come utente finale, questo non dovrebbe cambiare molto il flusso di trading sopra descritto, ma ci saranno viste o schermate extra per aggiungere o rimuovere diversi coordinatori che emergono.

FINE della guida
https://bitcoiner.guide/robosats/
