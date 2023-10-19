---
name: Blixt

description: Portafoglio LN multifunzione
---

![presentazione](assets/1.jpeg)

## Un potente nodo BTC/Lightning nel tuo taschino, ovunque tu sia

Vorrei presentarvi un nuovo nodo e portafoglio mobile BTC/LN interessante e potente - Blixt. Il nome deriva dallo svedese e significa "fulmine".

## Come ho scoperto questa piccola gemma?

Ho un nodo Umbrel LND e volevo avere un piano di backup per ripristinare rapidamente il mio nodo in caso di emergenza1. Ho quindi trovato questo portafoglio mobile che consente di ripristinare tutti i fondi del nodo dalle copie di backup SCB. Successivamente, ho iniziato a testarlo in modo più approfondito e ho scoperto che È UN NODO COMPLETO NEL TUO TASCHINO.

Ricordatevelo perché è molto importante!

> Alla fine di questo articolo troverete alcuni tutorial semplici e veloci su come utilizzarlo e come connettersi ad altri nodi.

Si tratta di un'applicazione sorprendente su Android e iOS che consente di eseguire un nodo BTC-LND nel tuo taschino. Incredibile, vero? Sul tuo telefono puoi avere un nodo BTC LN pronto in meno di 10 minuti, con funzionalità avanzate per gli utenti esperti, ma anche per i nuovi utenti o per coloro che non sono così esperti di tecnologia, poiché l'uso è semplice e intuitivo.

Blixt Wallet è un progetto open-source con licenza MIT e si concentra su una nicchia di utenti che vogliono iniziare con BTC/LN ma non hanno le risorse per far funzionare una macchina completa o semplicemente vogliono eseguire un nodo mobile.
Link

Ecco alcuni link relativi a questa nuova applicazione di nodo/portafoglio:

> Sito ufficiale - con anche una deliziosa demo interattiva
>
> Repository GitHub: verifica lo stato di sviluppo e/o scarica le sorgenti
>
> Gruppo di supporto Telegram - dove puoi fare domande direttamente allo sviluppatore e alla comunità
>
> Download dell'applicazione Android Blixt
> Download dell'applicazione Testflight per iOS
> Feed Twitter con demo

![immagine principale](assets/2.JPEG)

# Principali funzionalità disponibili

## Nodo Neutrino

Blixt si connette per impostazione predefinita al server di Blixt per sincronizzare i blocchi e l'indice con Neutrino (modalità SPV per la verifica semplificata dei pagamenti), ma l'utente può anche connettersi al proprio nodo. È sorprendente constatare che la sincronizzazione di un nodo SPV richiede meno di 5 minuti, nel mio caso su Android 11, per essere pronto all'uso del portafoglio del nodo completo (on-chain e LN).

\*\*Nodo completo non custodiale

Gli utenti possono gestire i propri canali con un'interfaccia semplice e con informazioni sufficienti per avere una buona esperienza. Nel menu del cassetto in alto a sinistra, è possibile andare ai canali Lightning per iniziare ad aprire con altri nodi, come si desidera. Non dimenticate di attivare Tor nelle impostazioni. È molto meglio per la privacy e anche perché, come nodo mobile, se cambiate spesso la vostra connessione a Internet / l'IP di Clearnet, i vostri peer possono confondersi. Con l'URI del nodo Tor, si avrà sempre lo stesso ID privato indipendentemente dalla propria posizione/IP.

## Backup/Ripristino di un nodo LND

Una funzione potente, facile da gestire e utile è il ripristino di altri nodi LND morti, con la sola lista dei semi di 24 parole e il file channels.backup.

> Ecco una guida su come ripristinare i nodi Umbrel morti in Blixt in caso di SHTF.

Gli utenti hanno anche la possibilità di salvare il backup dei canali Blixt su Google drive e/o sulla memoria locale del proprio cellulare (per spostarlo successivamente in un luogo sicuro, lontano dal telefono).

La procedura di ripristino è abbastanza semplice: si inserisce il seme di 24 parole, si aggiunge il file di backup (precedentemente copiato nella memoria del cellulare) e si clicca su ripristina. Ci vorrà un po' di tempo per sincronizzare e scansionare tutti i blocchi per i tx passati. I canali verranno automaticamente chiusi e i fondi torneranno nel vostro portafoglio onchain (vedere il menu del cassetto in alto a sinistra - onchain).

> Se in precedenza i canali erano aperti con il vecchio nodo dietro Tor, è necessario attivare l'opzione Tor (e riavviare l'applicazione) dal menu delle impostazioni. In questo modo, il processo di chiusura non fallirà e/o l'opzione di chiusura forzata non verrà utilizzata.

Non dimenticate di fare un backup dei vostri canali LN dopo averli aperti e/o chiusi. Bastano pochi secondi per essere al sicuro. In seguito, potrete spostare il file di backup in un luogo sicuro lontano dal vostro cellulare.

Per testare il seme in uno scenario di ripristino, prima di aggiungere fondi, è sufficiente utilizzare lo stesso seme di 24 parole (aezeed) in BlueWallet. Se l'indirizzo BTC generato è lo stesso in Blixt, il gioco è fatto. Non c'è bisogno di usare BlueWallet in seguito, si può semplicemente cancellare il portafoglio testato per il ripristino.

### Tor intégré

Une volta attivata, l'applicazione si riavvierà dietro la rete Tor. Da questo momento, puoi vedere nelle impostazioni del menu il tuo ID del nodo con un indirizzo onion, in modo che altri nodi possano aprire canali verso il tuo piccolo nodo mobile Blixt. Oppure diciamo che hai il tuo nodo a casa e vuoi avere piccoli canali con il tuo nodo mobile Blixt. Una combinazione perfetta.

## Dunder LSP - Liquidity Service Provider o Fornitore di Servizi di Liquidità

Una funzionalità semplice e fantastica che offre ai nuovi utenti la possibilità di iniziare ad accettare BTC sulla Lightning Network immediatamente, senza dover depositare fondi sul portafoglio on-chain per poi aprire canali LN.

Per i nuovi utenti, questa è una grande notizia, perché si suppone che possano iniziare da zero, direttamente su LN. Per fare ciò, è sufficiente creare una fattura (o invoice) LN dalla schermata principale sul pulsante "ricevi", inserire l'importo, la descrizione, ecc. e pagare da un altro portafoglio. Blixt aprirà un canale di massimo 500k sats per transazione ricevuta. Puoi aprirne più di uno, se necessario.

Un caso interessante e utile è il seguente: diciamo che il tuo primo importo ricevuto è di 200k. Blixt aprirà un canale di 500k sats e avrai già 200k (meno le spese di apertura) dal tuo lato, ma poiché hai ancora 300k di "spazio" disponibile, puoi riceverne di più. Quindi il prossimo pagamento, diciamo, di 100k arriverà direttamente tramite questo canale, senza ulteriori spese, e avrai ancora 200k di spazio per riceverne di più.

Ma se scegli di ricevere il terzo pagamento, diciamo, di 300k, verrà creato un altro nuovo canale da 500k e verranno spinti dal tuo lato questi 300k.

Se ci sono troppe richieste, il nodo di Blixt può modificare la capacità del canale durante l'apertura.

## Apertura automatica del canale

Nelle impostazioni, l'utente può attivare questa opzione e avere un servizio automatizzato che apre canali con i migliori nodi e percorsi a partire dal saldo disponibile nel portafoglio onchain dell'applicazione Blixt. È una funzione vantaggiosa per i nuovi utenti che non sanno bene con quale nodo aprire un canale e/o come aprire un canale LN. È come un pilota automatico per LN.

> Ricorda: questa opzione viene utilizzata solo una volta, quando crei il tuo nuovo portafoglio Blixt, ed è attivata per impostazione predefinita. Quindi, se il nuovo utente scannerizza il codice QR on-chain sulla schermata principale e deposita i suoi primi sats a quell'indirizzo, Blixt aprirà automaticamente un canale con quei sats, con il nodo pubblico Blixt.

## Servizi di liquidità in entrata

**Funzionalità dedicata ai commercianti che hanno bisogno di più liquidità IN ENTRATA, facile da usare. Per fare ciò, è sufficiente selezionare uno dei fornitori di liquidità nell'elenco, pagare l'importo desiderato per il canale e fornire l'ID del tuo nodo e da lì si aprirà un canale verso il tuo nodo Blixt.**

## Elenco dei contatti

Funzionalità utile se si desidera avere un elenco duraturo di destinatari con cui si commercia la maggior parte del tempo. Questo elenco può essere costituito da LNURL, indirizzi Lightning o future informazioni di pagamento statiche/fatture. Al momento, questo elenco non può essere salvato al di fuori dell'applicazione, ma è prevista un'opzione per esportarlo.

## Invia a un indirizzo Lightning

Puoi inviare a qualsiasi indirizzo LN se non è presente nella tua lista dei contatti. Presto forse ci sarà un'opzione per avere il proprio indirizzo LN di tipo @blixtwallet.com.

Supporto LNURL

Puoi scannerizzare/pagare/collegarti con LNURL, ma al momento ciò non funziona se LNURL è dietro Tor.

## Keysend

Una funzionalità molto potente che pochi portafogli mobili hanno. Puoi inviare/spingere fondi direttamente attraverso un canale o puntato verso un altro nodo, aggiungendo un messaggio se necessario. Questa funzionalità è molto utile per visualizzare messaggi sulla bacheca Amboss.space (qui c'è una guida su questa bacheca Amboss).

## Firma dei messaggi

Strumento molto utile per firmare messaggi con la tua chiave privata del nodo Blixt, messaggi di autenticazione di accesso e così via. Molti portafogli mobili dispongono di questa funzionalità, praticamente nessuno.

## Pagamenti multi-canale - Multi-Path Payments (MPP)

Funzionalità utile per i pagamenti LN, che consente di suddividere un pagamento LN in più parti, attraverso più canali. È un ottimo modo per bilanciare la liquidità sulla rete e migliorare la privacy.

## Browser Lightning

Una serie di servizi di terze parti con LN, organizzati in un browser semplice, accessibile e a portata di mano per l'utente. È anche un ottimo modo per promuovere le aziende che accettano BTC su LN. Questa è una funzionalità che sarà ulteriormente sviluppata in futuro. Al momento, non funziona dietro Tor, quindi la navigazione su queste applicazioni avviene in chiaro (clearnet).

## Esploratori di Log

È uno strumento potente per verificare i log LND e lo stato del tuo nodo in generale. C'è un'opzione per salvare il file dei log. È molto utile avere questi log a portata di mano nel caso in cui tu abbia bisogno dell'aiuto dello sviluppatore per identificare alcuni problemi.

## Sicurezza

Vous pouvez impostare nelle impostazioni dell'applicazione, per una maggiore sicurezza del tuo portafoglio/nodo, la possibilità di avviare l'applicazione con un codice PIN e/o l'impronta digitale.

## Portafoglio On-chain

Questa funzionalità è un po' nascosta, nel menu a scomparsa in alto a sinistra. Poiché non viene spesso utilizzata da un utente di LN, non è visibile nella schermata principale. Ma non importa, puoi averla su un portafoglio separato dove puoi gestire gli indirizzi e visualizzare il registro delle transazioni, importando ad esempio il tuo seed su Sparrow. Forse in futuro, Blixt wallet includerà anche una funzionalità per gestire gli UTxO. Ma per ora, utilizza SOLO questo portafoglio on-chain per aprire o chiudere canali su LN.

"Easter Eggs"

Eh sì, nell'applicazione Blixt ci sono alcune funzionalità nascoste, piccole cose che rendono l'applicazione affascinante, attivando azioni e risposte divertenti/interessanti.
Suggerimento: prova a fare doppio clic sul logo Blixt nel menu a scomparsa 🙂 Ti lascio scoprire il resto.

# Mini guida per casi d'uso tipici con Blixt

A. Apertura dei canali verso il tuo mini-nodo Blixt dal tuo nodo umbrel

## Per gli utenti Android:

1. Vai nelle impostazioni di Blixt - attiva Tor - riavvia l'applicazione (chiudila forzatamente se non si riavvia automaticamente).

2. Attendi che Blixt si apra dietro Tor e sincronizzi gli ultimi blocchi.

3. Vai nelle impostazioni - clicca su "Mostra servizio onion Tor", copialo, è l'URI del tuo nodo Blixt.

4a. Vai nella tua applicazione Umbrel RideTheLightning o ThunderHub (preferisco quest'ultimo) - aggiungi un peer e incolla l'indirizzo onion, l'URI Blixt.

4b. Vai alla dashboard del tuo nodo Umbrel o RTL/TH - apri un canale e seleziona un peer noto dalla lista cercando il tuo ID del nodo Blixt.

5. Imposta la quantità di sats per il canale, clicca su apri.

6. Attendi 3 conferme per avere un nuovo canale con il tuo "mini nodo" Blixt.

## Per gli utenti iOS:

1. Vai nelle impostazioni di Blixt - attiva Tor - riavvia l'applicazione.

2. Attendi che Blixt si apra dietro Tor e sincronizzi gli ultimi blocchi.

3. Vai al tuo nodo Umbrel, copia l'URI Tor o mostra il codice QR.

4. Su Blixt Wallet, vai nelle Impostazioni - Mostra Peer Lightning - Aggiungi peer e scannerizza o incolla l'URI del tuo nodo Umbrel. Sarà aggiunto come peer noto.
5. Torna all'applicazione Thunderhub di Umbrel, apri il menu dei canali e seleziona un peer dalla lista a discesa dei peer esistenti.
6. Inserisci tutti gli altri dettagli per aprire il canale, clicca su Apri.

7. Aspetta 3 conferme per aprire questo canale e voilà, ora hai più liquidità in entrata nel tuo lato Blixt.

## B. Apertura di canali verso un nodo Umbrel

Questa volta apriremo un canale DAL tuo nodo Blixt, verso il tuo stesso nodo Umbrel (ad esempio), per testare la connessione e l'uso di Tor. Successivamente, una volta aperto, puoi bilanciare questo canale spingendo metà o l'importo desiderato verso il lato Umbrel. Può anche essere utilizzato come una "valvola di scarico" quando il tuo nodo principale Umbrel ha bisogno di più liquidità.

1. Vai al tuo nodo Umbrel e copia l'URI del tuo nodo, o mostra semplicemente il codice QR per l'URI dell'indirizzo onion.

2. Vai su Blixt - Impostazioni - Peer Lightning - Aggiungi nuovo peer.

3. Scannerizza il codice QR del tuo nodo Umbrel o incolla l'URI onion e il tuo nodo Umbrel verrà aggiunto come peer.

4. Torna alla schermata principale - cassetto in alto a sinistra - canali Lightning.

5. Clicca sul segno "+" per aprire un nuovo canale e incolla l'URI o scannerizza il codice QR del tuo nodo Umbrel. Aggiungi il numero di sats per il canale, le spese e clicca su apri.

6. Fatto! Il canale richiederà 3 conferme per essere aperto e... Buon Lightning con il tuo nodo Umbrel personale.

C. Ricevi fondi direttamente nel portafoglio LN

È un'esperienza semplice e piacevole ricevere fondi direttamente nel tuo appena aperto portafoglio di nodi Blixt, senza dover depositare fondi in anticipo e aprire manualmente canali con nodi specifici.

1. Una volta creato il portafoglio e salvato il seed, vai nelle impostazioni e attiva la funzionalità Dunder LSP.

2. Torna alla schermata principale - clicca su ricevi, inserisci l'importo, ho testato con 200k sats.

3. Verrà creata una fattura LN da pagare da un altro portafoglio LN.

4. Il servizio LSP Dunder creerà un canale di massimo 500k sats e spingerà i fondi che hai inviato (200k nel nostro caso) sul lato del tuo canale. In questo modo avrai un bel canale pronto per inviare e ricevere.
5. Se vuoi ricevere di più, i prossimi pagamenti verranno ricevuti nello stesso canale, fino a raggiungere il massimo di 500k. Se non c'è più "spazio" per ricevere nello stesso canale, Dunder LSP creerà un nuovo canale, seguendo la stessa procedura.
6. Fai un backup dei tuoi nuovi canali aperti. Da fare sempre dopo aver aperto o chiuso un nuovo canale. È molto facile e veloce e può evitarti molti problemi.

Questo è un caso d'uso perfetto per i nuovi piccoli commercianti che vogliono iniziare ad accettare BTC.

Note importanti

> Prima di iniziare a utilizzare i tuoi canali dietro Tor e se l'applicazione Blixt è rimasta chiusa a lungo/non sincronizzata, aspetta che l'icona di sincronizzazione in alto dello schermo scompaia e verifica che tutti i tuoi canali siano attivi. Se è tutto a posto, procedi con le tue transazioni.
>
> Se i canali non sono ancora attivi, aggiungi nuovamente la chiave pubblica (l'URI) dei tuoi peer, nelle opzioni di Blixt - Mostra peer. Puoi anche provare a aggiornare questa lista, se il gossip sotto Tor trova i tuoi peer, i canali saranno nuovamente attivi. Se no, aggiungili di nuovo, ciò spingerà il gossip a comunicare.
>
> Ma ricorda: non effettuare ciecamente una tx immediatamente dopo aver aperto l'applicazione Blixt. Ci vuole qualche istante per verificare se i tuoi canali sono attivi e per avvisarti in caso di errore nel percorso di pagamento o mancanza di liquidità sul percorso.
>
> Aprire canali LN con Blixt ha un costo, come qualsiasi altro nodo LN che apre canali. Questo ha un nome: "commit_fees" (o tasse di impegno) che sono come una riserva per chiudere i canali, per essere in grado di pagare le commissioni dei minatori. Quindi sii consapevole che quando depositi nel tuo portafoglio on-chain Blixt e apri canali (indipendentemente dall'utilizzo di LSP Dunder, l'apertura automatica dei canali o manualmente) l'importo disponibile sarà leggermente inferiore all'importo totale con cui hai aperto il canale. Ecco perché NON È RACCOMANDATO aprire canali molto piccoli come 20-50-100k sats.
>
> Inoltre, ogni transazione LN ha piccole commissioni per la rete. Non sono commissioni per Blixt, sono un costo che rende le tue transazioni sicure e protette dalla rete. Ma sono molto piccole, talvolta anche in milli-sats, spesso meno dello 0,5% dell'importo della tua transazione.
> Essendo un nodo LN, è fortemente sconsigliato utilizzare lo stesso seed su due dispositivi diversi. Questa procedura può essere fatta SOLO nel caso in cui tu sia in una procedura di recupero. Quando il portafoglio on-chain genera dal seed, inizierà a sincronizzare le transazioni precedenti e i saldi. Se non hai il LN.backup dei tuoi canali, questo non inizierà la procedura di ripristino completa. Quindi sì, vedrai lo stesso portafoglio on-chain su entrambi i dispositivi ma NON il saldo LN. E soprattutto NON PROVARE a ripristinare sugli stessi dispositivi gli stessi canali LN, altrimenti perderesti tutti i tuoi fondi LN!

Tieni presente che la chiusura dei canali richiede tempo, fino a quando i fondi non vengono liberati. Questo è come funziona LN (per saperne di più vai qui). Quindi, in generale, se hai una chiusura cooperativa (normale), ci vorranno almeno 40 blocchi prima che i fondi vengano liberati nel tuo portafoglio on-chain. Per i canali chiusi forzatamente, questa chiusura è di 144 blocchi o anche di più a volte. Quindi sii paziente e non preoccuparti, i fondi sono al sicuro.

## Conclusioni

Bene, queste sono alcune delle principali funzionalità (per un portafoglio mobile, è molto, vero?) tra molte altre e presto ce ne saranno ancora di più.

L'esperienza con questa applicazione di portafoglio/nodo LN è molto piacevole e facile da usare, un'applicazione molto reattiva, senza problemi significativi, solo piccole cose che devono essere aggiunte (ma non così importanti). È ancora un'applicazione giovane e ha bisogno di molti test in condizioni reali. Quindi non esitate a provarla e a segnalare al sviluppatore eventuali problemi che possono essere corretti o migliorati.

Non dimentichiamo che si tratta anche di un progetto open source e che la sua manutenzione è curata da un singolo sviluppatore, che fa tutto il lavoro! Quindi, per favore, aiutatelo con test e feedback e, cosa più importante, siate pazienti e segnalategli con molti dettagli se trovate problemi o se l'applicazione ha bisogno di ulteriori miglioramenti.

Spero che apprezzerai il suo utilizzo. Personalmente, lo adoro ed è molto utile per me (vedi qui un caso d'uso in cui questo portafoglio è uno strumento fantastico).

Che ₿ITCOIN SIA CON TE!
