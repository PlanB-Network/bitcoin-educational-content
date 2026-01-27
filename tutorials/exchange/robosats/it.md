---
name: Robosats
description: Come utilizzare Robosats
---

![cover](assets/cover.webp)

RoboSats (https://learn.robosats.com/) è un modo semplice per scambiare Bitcoin in modo privato con valute nazionali. Semplifica l'esperienza peer-to-peer e utilizza invoice lightning hold per ridurre al minimo i requisiti di custodia e fiducia.

![video](https://youtu.be/XW_wzRz_BDI)

## Guida

Questa guida è di Bitcoin Q&A (https://bitcoiner.guide/robosats/). Tutto il merito va a lui, supportalo lì (https://bitcoiner.guide/contribute); BitcoinQ&A è anche un mentore di Bitcoin. Contattalo per il mentoring!

![image](assets/0.webp)

RoboSats - Uno scambio P2P semplice e privato basato su Lightning

## Prima di iniziare

### Cose che devi sapere

| Gergo        | Definizione                                                                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | La tua identità di scambio privata generata automaticamente. Non riutilizzare lo stesso robot più di una volta poiché potrebbe compromettere la tua privacy.                                                                                      |
| Token        | Una stringa di caratteri casuali utilizzata per generare il tuo robot unico.                                                                                                                                                                      |
| Maker        | Un utente che crea un'offerta per comprare o vendere Bitcoin.                                                                                                                                                                                     |
| Taker        | Un utente che accetta l'offerta di un altro utente per comprare o vendere Bitcoin.                                                                                                                                                                |
| Bond         | Una quantità di Bitcoin bloccata da entrambi i partecipanti come garanzia per agire correttamente e completare la propria parte dello scambio. I bond sono di solito il 3% dell'importo totale dello scambio e sono supportati da invoice Hodl. |
| Trade Escrow | Utilizzato dal venditore come metodo per trattenere l'importo dello scambio di Bitcoin, utilizzando nuovamente invoice Hodl.                                                                                                                      |
| Commissioni  | RoboSats addebita lo 0,2% dell'importo dello scambio, che viene diviso tra il maker e il taker. Il taker paga lo 0,175% e il maker paga lo 0,025%.                                                                                                |

## Cose che devi avere

### Un wallet Lightning

RoboSats è nativo di Lightning, quindi avrai bisogno di un wallet Lightning per finanziare il bond e ricevere i sats acquistati come acquirente. Fai attenzione nella scelta del wallet, perché non tutti sono compatibili con la tecnologia utilizzata da RoboSats.

Se gestisci un nodo, Zeus è la scelta migliore. Se invece non hai un tuo nodo, ti consiglio vivamente Phoenix, un wallet mobile multipiattaforma con configurazione semplice e accesso a Lightning. Phoenix è stato utilizzato per la realizzazione di questa guida.

### Un po' di Bitcoin

Acquirenti e venditori devono finanziare un bond prima che avvenga qualsiasi scambio. Di solito si tratta di una quantità molto piccola (~3% dell'importo), ma resta comunque un requisito indispensabile.

Stai usando RoboSats per acquistare i tuoi primi sats? Puoi chiedere in prestito la piccola quantità necessaria a un amico. Se non hai questa possibilità, ci sono diverse altre opzioni per ottenere sats senza KYC e iniziare.

### Accesso a RoboSats

Ovviamente ti serve accedere a RoboSats! Ci sono quattro modi principali:

1. Tramite Tor Browser (consigliato!)
2. Tramite un browser web normale (non consigliato!)
3. Tramite l'APK Android
4. Con il tuo client personale

Se sei nuovo a Tor Browser, scopri di più e scaricalo [qui](https://www.torproject.org/download/).  
Nota per utenti iOS: 'Onion Browser' non è Tor Browser. Usa invece Orbot + Safari oppure Orbot + DuckDuckGo.

## Acquisto di Bitcoin

I seguenti passaggi sono stati eseguiti nel maggio 2023 utilizzando la versione 0.5.0, accessibile tramite Tor Browser. Dovrebbero essere identici anche per chi usa RoboSats tramite l'APK Android.

Al momento della stesura, RoboSats è ancora in fase di sviluppo attivo, quindi l'interfaccia potrebbe cambiare, ma i passaggi di base per completare una transazione resteranno per lo più invariati.

> Quando carichi per la prima volta RoboSats, ti troverai davanti a questa pagina iniziale. Clicca su Start.

![image](assets/2.webp)

Genera il tuo token e conservalo in un luogo sicuro, come un'app di appunti crittografata o un gestore di password. Questo token serve per recuperare il tuo ID Robot temporaneo nel caso in cui il browser o l'app si chiudano a metà di una transazione.

![image](assets/3.webp)

Incontra la tua nuova identità di Robot, poi clicca su Continua.

![image](assets/4.webp)

Clicca su Offerte per sfogliare il libro degli ordini. In cima alla pagina puoi filtrare le tue preferenze. Prendi nota delle percentuali di bond e del premio rispetto al tasso di cambio medio.

- Scegli Acquista
- Scegli la tua valuta
- Scegli il tuo metodo di pagamento

![image](assets/5.webp)

> Clicca sull'offerta che vuoi accettare. Inserisci l'importo (nella valuta fiat scelta) che vuoi acquistare dal venditore, controlla i dettagli e clicca su Prendi Ordine.

Se il venditore non è online (indicatore rosso sull’immagine del profilo), vedrai un avviso che ti informa del fatto che la transazione potrebbe richiedere più tempo. Se procedi e il venditore non conferma in tempo, riceverai un rimborso del 50% dell'importo del bond per il tempo perso.

![image](assets/6.webp)

Ora devi bloccare la tua bond pagando la invoice sullo schermo. È una invoice di blocco che rimane congelata nel tuo wallet e viene addebitata solo se non completi la tua parte della transazione.

![image](assets/7.webp)

Nel tuo wallet Lightning scannerizza il codice QR e paga la invoice.

![image](assets/8.webp)

Poi, nel tuo wallet Lightning genera una invoice per l'importo mostrato e incollala nello spazio indicato.

![image](assets/9.webp)

Attendi che il venditore blocchi l'importo della sua transazione. Quando lo fa, RoboSats va al passaggio successivo e si apre la finestra di chat. Saluta e chiedi al venditore i dati per il pagamento in valuta fiat. Una volta inviato il pagamento con il metodo scelto, confermalo in RoboSats. La chat è crittografata con PGP, quindi solo tu e il tuo partner di transazione potete leggerla.

![image](assets/10.webp)

Quando il venditore conferma di aver ricevuto il pagamento, RoboSats rilascia automaticamente i tuoi sats tramite la invoice che hai fornito.

![image](assets/11.webp)

Quando la invoice è saldata, la transazione è completata e il bond viene sbloccato. Vedrai un riepilogo della transazione.

![image](assets/12.webp)

Controlla il tuo wallet Lightning per verificare che i sats siano arrivati.

![image](assets/13.webp)

## Funzionalità aggiuntive

Oltre all'acquisto e alla vendita di Bitcoin, RoboSats ha altre funzionalità utili.

### Garage dei Robot

Vuoi avere più scambi contemporaneamente senza condividere la stessa identità? Nessun problema. Clicca sulla scheda Robot, genera un nuovo Robot e crea o prendi un altro ordine.

![image](assets/14.webp)

### Creazione di ordini

Oltre ad accettare l’offerta di un altro utente, puoi crearne una tua e aspettare che venga accettata.

- Apri la pagina di creazione.
- Scegli se l'ordine è per comprare o vendere Bitcoin.
- Inserisci importo e valuta.
- Inserisci il metodo di pagamento che sei disposto a usare.
- Inserisci la percentuale di "Premium sul mercato" che sei disposto ad accettare (può essere anche negativa per offrire uno sconto rispetto al prezzo attuale).
- Clicca su Crea ordine.
- Paga la invoice Lightning per bloccare il tuo Maker Bond.
- Il tuo ordine è ora attivo. Aspetta che qualcuno lo accetti.

![image](assets/15.webp)

### Pagamenti on-chain

RoboSats è centrato su Lightning, ma puoi ricevere i sats anche su un indirizzo Bitcoin on-chain. Dopo aver bloccato il bond, puoi selezionare questa opzione. Verrà mostrata una panoramica delle commissioni. Quelle extra includono:

- Una commissione di scambio raccolta da RoboSats (dinamica e variabile a seconda del traffico della rete).
- Una commissione di mining per la transazione on-chain (configurabile da te).

![image](assets/16.webp)

### Scambi P2P

RoboSats ti consente di scambiare sats dentro o fuori dal tuo Lightning Wallet. Clicca sul pulsante di scambio in alto nella pagina delle offerte per vedere quelle attive.

Come acquirente di un'offerta "Scambio in", invii Bitcoin on-chain e ricevi sats su Lightning (meno commissioni e premi).  
Come acquirente di un'offerta "Scambio out", invii sats via Lightning e ricevi Bitcoin on-chain (meno commissioni e premi).  
Se usi Samourai o Sparrow Wallet puoi sfruttare anche la funzione Stowaway.

Alcune offerte possono includere alternative ancorate a Bitcoin come RBTC, LBTC e WBTC. Fai molta attenzione: il Bitcoin ancorato non è Bitcoin.

![image](assets/17.webp)

### Esegui il tuo client RoboSats

Se usi Umbrel, Citadel o Start9 puoi installare il tuo client RoboSats direttamente sul nodo. I vantaggi:

- Caricamento molto più veloce.
- Maggiore sicurezza: scegli tu quale app client eseguire.
- Accesso sicuro a RoboSats da qualsiasi browser o dispositivo. Non serve Tor se sei nella rete locale o usi una VPN: il tuo nodo gestisce l'anonimità con Tor.
- Puoi scegliere a quale coordinatore P2P connetterti (di default: robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion).

![image](assets/18.webp)

## FAQ

### Posso essere truffato?

Se come acquirente invii il pagamento fiat ma il venditore non ti rilascia i sats, puoi aprire una controversia. Se dimostri agli arbitri di RoboSats di aver inviato il pagamento, riceverai i fondi in escrow del venditore e il suo bond.

### Come posso annullare una transazione?

Puoi annullarla dopo aver pubblicato il bond cliccando su Collaborative Cancel. Se il tuo partner accetta, non ci sono commissioni. Se invece il partner vuole completare lo scambio e tu annulli lo stesso, perdi il bond.

### RoboSats funziona con il metodo di pagamento 'X'?

Sì, non ci sono restrizioni. Se non vedi offerte con il metodo che vuoi, creane una tu.

![image](assets/19.webp)

### Cosa apprende RoboSats su di me?

Se lo usi tramite Tor o l’app Android, nulla.  
Tor protegge la tua connessione, PGP protegge la chat, e ogni Robot è monouso.  

Eccezione: Lightning non è del tutto privato lato ricezione. Se ricevi sul tuo nodo Lightning, il tuo ID nodo appare nelle invoice e può essere collegato alla tua attività on-chain. Lo stesso vale se scegli di ricevere on-chain.

Per ridurre i rischi puoi usare un Proxy Wallet per Lightning o Coinjoin per on-chain.

### Federazione

Oggi esiste un solo coordinatore, gestito dal team di RoboSats. Questo è un punto di centralizzazione e quindi vulnerabile a regolamentazioni.  
Essendo open source, chiunque può creare un proprio coordinatore. Questo aumenta la decentralizzazione ma frammenta la liquidità.  

Il team sta lavorando a un modello federato. Per te, utente finale, non cambia molto: avrai solo schermate extra per aggiungere o rimuovere coordinatori.

FINE della guida  
https://bitcoiner.guide/robosats/

