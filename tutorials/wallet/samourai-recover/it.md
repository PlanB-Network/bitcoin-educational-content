---
name: Samourai Wallet - Recupero
description: Come recuperare i bitcoin bloccati su Samourai Wallet?
---
![cover](assets/cover.webp)

A seguito dell'arresto dei fondatori di Samourai Wallet e del sequestro dei loro server il 24 aprile, alcune funzionalità dell'applicazione sono ora inoperative, e gli utenti che non dispongono di un proprio Dojo non possono più trasmettere transazioni.

Dopo aver assistito diversi utenti nel recupero dei loro bitcoin negli ultimi giorni, credo di aver incontrato la maggior parte dei problemi che possono sorgere durante il ripristino di un Samourai Wallet. Pertanto, questo tutorial inizierà con un rapporto di situazione per identificare le funzionalità che rimangono operative e quelle che non sono più disponibili all'interno dell'ecosistema Samourai Wallet e del software interessato da questo incidente. Successivamente, procederemo passo dopo passo per recuperare un Samourai Wallet utilizzando il software Sparrow Wallet. Esamineremo tutti gli ostacoli potenziali incontrati durante questo processo e vedremo soluzioni per risolverli. Infine, nell'ultima parte, scoprirai i potenziali rischi per la tua privacy a seguito del sequestro dei server.

*Un grande ringraziamento a [@Louferlou](https://twitter.com/Louferlou), che ha assistito diversi utenti nel loro recupero e ha condiviso le sue esperienze con me, e che ha anche contribuito ai test per determinare cosa è ancora funzionale.*

## Samourai Wallet funziona ancora?

Sì, **l'app Samourai Wallet è ancora funzionante**, ma a certe condizioni.

Prima di tutto, è necessario che l'app fosse stata precedentemente installata sul tuo smartphone. Il Google Play Store ha rimosso l'app, e l'APK era ospitato sul sito web sequestrato. Pertanto, al momento è complicato installare Samourai. Potresti trovare APK online, ma sconsiglio di scaricarli a meno che tu non sia sicuro della fonte.

Dato che la pagina di Samourai Wallet non è più disponibile sul Google Play Store, non è possibile disabilitare gli aggiornamenti automatici. Se l'app tornasse sulle piattaforme di download, sarebbe saggio **disabilitare gli aggiornamenti automatici** fino a quando non saranno disponibili più informazioni riguardo lo sviluppo del caso.

Se Samourai Wallet è già installato sul tuo smartphone, dovresti comunque essere in grado di accedere all'app. Per utilizzare la funzionalità portafoglio di Samourai, è essenziale collegare un Dojo. In precedenza, gli utenti senza un Dojo personale dipendevano dai server di Samourai per accedere alle informazioni della blockchain Bitcoin e per trasmettere transazioni. Con il sequestro di questi server, l'app non può più accedere a questi dati.
Se non avevi un Dojo connesso prima ma ne hai uno ora, puoi configurarlo per utilizzare di nuovo la tua app Samourai. Questo comporta il controllo dei tuoi backup, l'eliminazione del portafoglio (il portafoglio, non l'applicazione) e il recupero del portafoglio collegando il tuo Dojo all'applicazione. Per maggiori dettagli su questi passaggi, puoi consultare [questo tutorial, nella sezione "_Preparare il tuo Samourai Wallet_" : COINJOIN - DOJO](https://planb.network/it/tutorials/privacy/coinjoin-dojo).
Se la tua app Samourai era già connessa al tuo Dojo personale, allora la parte del portafoglio funziona perfettamente per te. Puoi ancora vedere il tuo saldo e trasmettere transazioni. Nonostante tutto ciò che sta accadendo, penso che Samourai Wallet rimanga il miglior software di portafoglio mobile al momento. Personalmente, ho intenzione di continuare a usarlo.
Il problema principale che potresti incontrare è l'inaccessibilità degli account Whirlpool dall'app. Di solito, Samourai tenta di stabilire una connessione con il tuo Whirlpool CLI e avviare i cicli di coinjoin prima di darti accesso a questi account. Tuttavia, poiché questa connessione non è più possibile, l'app continua a cercare all'infinito senza mai darti accesso agli account Whirlpool. In questo caso, puoi recuperare questi account su un altro software di portafoglio mantenendo solo l'account di deposito su Samourai.
### Quali strumenti sono ancora disponibili su Samourai?

D'altra parte, alcuni strumenti sono stati colpiti dalla chiusura del server o sono completamente indisponibili.

Per quanto riguarda gli strumenti di spesa individuale, tutto funziona normalmente a patto, naturalmente, che tu abbia il tuo Dojo. Le transazioni Stonewall normali (e non Stonewall x2) funzionano senza alcun problema.

Commenti su Twitter hanno evidenziato che la privacy offerta da una transazione Stonewall potrebbe ora essere ridotta. Il valore aggiunto di una transazione Stonewall risiede nel fatto che è indistinguibile da una transazione Stonewall x2 in termini di struttura. Quando un analista incontra questo specifico schema, non può determinare se si tratta di uno Stonewall standard con un singolo utente o di uno Stonewall x2 che coinvolge due utenti. Tuttavia, come vedremo nei paragrafi seguenti, effettuare transazioni Stonewall x2 è diventato più complesso a causa della non disponibilità di Soroban. Alcuni pensano quindi che un analista potrebbe ora assumere che qualsiasi transazione con questa struttura sia uno Stonewall normale. Personalmente, non condivido questa ipotesi. Sebbene le transazioni Stonewall x2 possano essere meno frequenti (e penso che lo fossero già prima di questo incidente), il fatto che siano ancora possibili può invalidare un'intera analisi basata sull'assunzione che non lo siano.
**[-> Scopri di più sulle transazioni Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
Per quanto riguarda Ricochet, non sono stato in grado di verificare se il servizio sia ancora operativo, poiché non possiedo un Dojo sul Testnet, e preferisco non rischiare di spendere `100 000 sats` verso un portafoglio che potrebbe essere controllato dalle autorità. Se hai avuto l'opportunità di testare questo strumento di recente, ti invito a contattarmi così possiamo aggiornare questo articolo.

Se hai bisogno di usare Ricochet, sii consapevole che puoi sempre eseguire questa operazione manualmente con qualsiasi software di portafoglio. Per imparare come eseguire manualmente i vari salti correttamente, ti consiglio di consultare quest'altro articolo: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

Lo strumento JoinBot non è più operativo, poiché era completamente dipendente dalla partecipazione di un portafoglio gestito da Samourai.

Per quanto riguarda altri tipi di transazioni collaborative, spesso definite "cahoots", rimangono possibili, ma solo manualmente. Prima della chiusura del server, avevi due opzioni per eseguire transazioni Stonewall x2 o Stowaway (PayJoin):
- Usare la rete Soroban per scambiare automaticamente e a distanza i PSBT;
- O eseguire questi scambi manualmente scansionando più codici QR.

Dopo vari test, appare che Soroban non sia più funzionante. Per eseguire queste transazioni collaborative, lo scambio di dati deve quindi essere fatto manualmente. Ecco due opzioni per eseguire questo scambio:
- Se sei fisicamente vicino al tuo collaboratore, puoi scansionare i codici QR successivamente;
- Se sei distante dal tuo collaboratore, puoi scambiare i PSBT tramite un canale di comunicazione esterno all'applicazione. Tuttavia, fai attenzione, poiché i dati contenuti in questi PSBT sono sensibili in termini di privacy. Ti consiglio di utilizzare un servizio di messaggistica criptata per garantire la riservatezza dello scambio.
**[-> Scopri di più sulle transazioni Stonewall x2.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Scopri di più sulle transazioni Stowaway.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

Per quanto riguarda Whirlpool, il protocollo non sembra più funzionare, nemmeno per gli utenti che possiedono il proprio Dojo. Ho monitorato il mio RoninDojo negli ultimi giorni e ho tentato alcune manipolazioni di base, ma il CLI di Whirlpool non è stato in grado di connettersi da quando il server è stato chiuso.

Tuttavia, rimango speranzoso che questo protocollo possa essere riattivato o forse immaginato in modo diverso nelle prossime settimane, a seconda di come evolve la situazione. Questa pausa potrebbe essere un'opportunità per esplorare nuovi approcci o potenziali miglioramenti a questo sistema.
### Quali strumenti esterni sono ancora disponibili?
Per quanto riguarda altri strumenti legati all'ambiente Samourai, alcuni sono ancora disponibili mentre altri no.

Il sito web gratuito di analisi della catena OXT.me non è purtroppo più disponibile al momento.

Lo strumento Whirlpool Stats Tool non è più disponibile per il download, poiché era ospitato sul GitLab di Samourai. Anche se lo avevi precedentemente scaricato localmente sul tuo computer, o se era installato sul tuo nodo RoninDojo, WST non funzionerà per il momento. Infatti, dipendeva dai dati forniti da OXT.me per il suo funzionamento, e questo sito non è più accessibile. Attualmente, WST non è particolarmente utile poiché il protocollo Whirlpool è inattivo.

Il sito KYCP.org attualmente non è più accessibile.

Il GitLab che ospitava il codice per lo strumento Python Boltzmann Calculator è stato anche sequestrato. Al momento, quindi, non è più possibile scaricare questo strumento. Ma se hai un RoninDojo, puoi continuare a utilizzare Boltzmann Calculator nello stesso modo di prima.

Per quanto riguarda RoninDojo, questo software nodo-in-box continua a funzionare correttamente nonostante l'indisponibilità di alcuni strumenti specifici come Whirlpool CLI e WST. Può ancora essere utilizzato per altri software di portafoglio grazie a Fulcrum o Electrs. Se desideri ottenere maggiori informazioni su RoninDojo o se hai domande specifiche, ti incoraggio a unirti al [loro gruppo Telegram](https://t.me/RoninDojoNode).

Tuttavia, il codice sorgente per RoninDojo attualmente non è più accessibile, poiché era ospitato sul GitLab di Samourai. Pertanto, non è possibile installarlo manualmente su un Raspberry Pi al momento.

Per quanto riguarda il software di portafoglio watch-only Sentinel, la situazione è simile a quella dell'app Samourai. Se hai il tuo Dojo, puoi continuare a utilizzare Sentinel senza problemi. Tuttavia, se non hai un Dojo, non sarai più in grado di stabilire una connessione. A differenza di Samourai, il sito web di Sentinel è ancora accessibile online. Ma fai attenzione a questo sito e all'APK offerto lì, poiché non è chiaro chi controlli attualmente queste risorse.

### Sparrow Wallet è influenzato?
Sparrow Wallet continua a funzionare normalmente, ad eccezione degli strumenti Samourai che non sono più disponibili. Attualmente, non è più possibile eseguire coinjoins tramite Sparrow. Allo stesso modo, gli strumenti per la spesa collaborativa non sono più accessibili, poiché Sparrow non offre l'opzione di scambio manuale di PSBT, a differenza di Samourai. Per tutte le altre funzionalità, Sparrow opera senza problemi. È possibile utilizzare questo software anche per recuperare un portafoglio Samourai, se necessario.

## Come recuperare un portafoglio Samourai?
Come abbiamo visto nelle sezioni precedenti, se possiedi il tuo Dojo, non è necessariamente richiesto cambiare software. **Samourai rimane un'ottima scelta di hot wallet** per le tue spese quotidiane. Tuttavia, se non hai un Dojo o se preferisci optare per un altro software, ti spiegherò il processo completo di recupero, dettagliando eventuali ostacoli che potresti incontrare.

In ogni caso, è importante prendersi il proprio tempo e assicurarsi di non fare errori. Ricorda, non c'è fretta, poiché detieni le tue chiavi private, e il sequestro dei server di Samourai non influisce in alcun modo su questo. Qualunque cosa accada, ovviamente non possono accedere alle tue chiavi private.

### Verifica la passphrase

Per recuperare il tuo portafoglio, devi avere la tua passphrase, anche se opti per il recupero tramite il file di backup. Inizia verificando la validità di questa passphrase. Apri la tua app Samourai Wallet, clicca sull'icona Paynym in alto a sinistra, poi seleziona `Impostazioni`.

![samourai](assets/1.webp)

Successivamente, clicca su `Risoluzione dei problemi` e poi su `Test passphrase/backup`.

![samourai](assets/2.webp)

Inserisci la tua passphrase e clicca `Ok`. Se è corretta, Samourai lo confermerà. Hai anche l'opzione di verificare il file di backup se prevedi di utilizzarlo in seguito.

![samourai](assets/3.webp)

Questo passaggio è facoltativo ma consigliato. Conferma che la passphrase è corretta, eliminando una potenziale fonte di problemi in seguito. Se Samourai indica che la passphrase è incorretta in questa fase, il recupero non sarà possibile. Assicurati di aver inserito correttamente la passphrase e controllala di nuovo.

### Opzione 1: Recuperare il portafoglio su Sparrow con il file di backup

Dalla versione 1.8.6 di Sparrow Wallet, è possibile importare direttamente il tuo portafoglio Samourai utilizzando il file di testo di backup denominato `samourai.txt`, che la tua applicazione genera automaticamente. Questo file contiene tutte le informazioni necessarie per recuperare il tuo portafoglio ed è criptato con la tua passphrase per sicurezza.

Se scegli questa opzione, avrai bisogno del tuo file `samourai.txt` aggiornato e della tua passphrase. Per generare questo file su Samourai Wallet, clicca sui tre piccoli punti in alto a destra, poi seleziona `Esporta backup portafoglio`.

![samourai](assets/4.webp)
Successivamente, scegli `Esporta negli Appunti`. Dopo di che, dovrai trasferire questo file al tuo PC in modo sicuro. Poiché il file è criptato, ma la sola passphrase è sufficiente per decifrarlo, è importante prendere precauzioni durante la sua trasmissione. Se opti per un trasferimento diretto come testo semplice, dovrai creare un file `samourai.txt` sul tuo PC e incollare il contenuto degli appunti in esso. Un'alternativa sarebbe recuperare direttamente il file `samourai.txt` dai file memorizzati sul tuo telefono.
Una volta che hai accesso al file sul tuo PC, apri Sparrow Wallet, clicca sulla scheda `File` e seleziona `Importa Portafoglio` per iniziare l'importazione del tuo portafoglio.

![samourai](assets/5.webp)
Scorri verso il basso fino a `Samourai Backup`, clicca su `Importa File`, e poi seleziona il tuo file `samourai.txt`.
![samourai](assets/6.webp)

Sparrow ti chiederà quindi una password per decriptare il file. Questa password è in realtà la tua passphrase. Inseriscila nel campo corrispondente e clicca su `Importa`.

![samourai](assets/7.webp)

Se in questa fase il tuo portafoglio non appare, è possibile che tu abbia commesso un errore copiando il file `samourai.txt` o inserendo la passphrase. Puoi consultare la sezione di risoluzione dei problemi per ulteriore aiuto.

![samourai](assets/8.webp)

Per quanto riguarda il tipo di script, se non hai configurato altri script in Samourai, dovresti normalmente usare solo SegWit V0 (Native SegWit / P2WPKH). Mantieni questo script predefinito e clicca su `Importa`.

![samourai](assets/9.webp)

Dai un nome al tuo portafoglio, ad esempio, "Samourai Recovery", e poi clicca su `Crea Portafoglio`.

![samourai](assets/10.webp)

Sparrow ti chiederà quindi di scegliere una password. Questa password protegge solo l'accesso al tuo portafoglio su questo PC e non riguarda la derivazione delle chiavi del tuo portafoglio. Assicurati di scegliere una password forte, annotala per ricordarla, e clicca su `Imposta Password`.

![samourai](assets/11.webp)

Sparrow deriverà quindi le chiavi del tuo portafoglio e cercherà le transazioni corrispondenti.

![samourai](assets/12.webp)

Per ora, solo il tuo conto deposito è accessibile. Se stavi usando Samourai solo per questo conto, dovresti vedere tutti i tuoi fondi. Tuttavia, se stavi usando anche Whirlpool, dovrai derivare i conti `premix`, `postmix` e `badbank`. Su Sparrow, clicca semplicemente sulla scheda `Impostazioni`, poi su `Aggiungi Conti...`.

![samourai](assets/13.webp)
Nella finestra che si apre, seleziona `Conti Whirlpool` dal menu a tendina, poi clicca su `OK`.
![samourai](assets/14.webp)

Vedrai quindi apparire i tuoi vari conti Whirlpool, e Sparrow deriverà le chiavi necessarie per utilizzare i bitcoin associati.

![samourai](assets/15.webp)

Se stai usando un software diverso da Sparrow, come Electrum, per recuperare il tuo portafoglio Samourai, ecco gli indici dei conti Whirlpool per il recupero manuale:
- Deposito: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Ora hai accesso ai tuoi bitcoin su Sparrow. Se hai bisogno di aiuto nell'uso di Sparrow Wallet, puoi anche consultare [il nostro tutorial dedicato](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Raccomando inoltre di importare manualmente le etichette che avevi associato ai tuoi UTXO su Samourai. Questo ti permetterà di eseguire un controllo efficace delle monete su Sparrow successivamente.

### Opzione 2: Recupera il portafoglio su Sparrow con la frase mnemonica

Se non desideri eseguire il recupero con il file di backup, puoi optare per un metodo più tradizionale utilizzando semplicemente la tua frase di recupero di 12 parole e la tua passphrase. Questa seconda opzione è spesso più semplice.
Per iniziare, assicurati di avere a portata di mano la tua frase di recupero e la tua passphrase. Quindi, apri il software Sparrow Wallet, clicca sulla scheda `File` e seleziona `Importa Portafoglio` per iniziare l'importazione del tuo portafoglio.
![samourai](assets/16.webp)

Scegli `Parole Mnemoniche (BIP39)` e, nel menu a tendina, clicca su `Usa 12 Parole`.

![samourai](assets/17.webp)

Inserisci le 12 parole della tua frase di recupero nell'ordine corretto.

![samourai](assets/18.webp)

Se Sparrow mostra un messaggio di `Checksum Invalido`, ciò indica che il checksum della frase di recupero non è valido, il che probabilmente significa che hai commesso un errore nell'inserimento delle parole.

![samourai](assets/19.webp)

Se la tua frase è corretta, spunta la casella `Usare Passphrase?` e inserisci la tua passphrase nel campo dedicato. Infine, se tutto sembra corretto, clicca sul pulsante `Scopri Portafoglio`.

![samourai](assets/20.webp)

Nomina il tuo portafoglio, ad esempio, "Recupero Samourai", poi clicca su `Crea Portafoglio`.

![samourai](assets/21.webp)
Sparrow ti chiederà quindi di scegliere una password. Questa password protegge solo l'accesso al tuo portafoglio su questo PC e non è collegata alla derivazione delle chiavi del tuo portafoglio. Assicurati di scegliere una password forte, scrivila per ricordarla e clicca su `Imposta Password`.
![samourai](assets/22.webp)

Sparrow deriverà quindi le chiavi per il tuo portafoglio e cercherà le transazioni corrispondenti.

![samourai](assets/23.webp)

Se in questa fase il tuo portafoglio non appare, è possibile che tu abbia commesso un errore nell'inserimento della passphrase o della frase di recupero. Puoi consultare la sezione dedicata alla risoluzione dei problemi per ulteriore aiuto.

Per ora, solo il tuo conto deposito è accessibile. Se stavi usando Samourai solo per questo conto, dovresti vedere tutti i tuoi fondi. Tuttavia, se stavi utilizzando anche Whirlpool, dovrai derivare i conti `premix`, `postmix` e `badbank`. Su Sparrow, clicca semplicemente sulla scheda `Impostazioni`, poi su `Aggiungi Conti...`.

![samourai](assets/24.webp)

Nella finestra che si apre, seleziona `Conti Whirlpool` dall'elenco a tendina, poi clicca su `OK`.

![samourai](assets/25.webp)

Vedrai quindi apparire i tuoi vari conti Whirlpool, e Sparrow deriverà le chiavi necessarie per utilizzare i bitcoin associati.

![samourai](assets/26.webp)

Se stai utilizzando un altro software come Electrum per recuperare il tuo portafoglio Samourai, ecco gli indici dei conti Whirlpool per il recupero manuale:
- Deposito: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Ora hai accesso ai tuoi bitcoin su Sparrow. Se hai bisogno di aiuto nell'utilizzo di Sparrow Wallet, puoi anche consultare [il nostro tutorial dedicato](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Raccomando inoltre di importare manualmente le etichette che avevi associato ai tuoi UTXO su Samourai. Ciò ti permetterà di eseguire un controllo efficace delle monete su Sparrow successivamente.

### Quali sono i problemi comuni riscontrati?
Dopo aver assistito diverse persone negli ultimi giorni, credo di aver incontrato la maggior parte dei problemi che possono impedire il recupero del tuo portafoglio. Se non riesci ancora ad accedere al tuo portafoglio nonostante i tutorial precedenti, ecco alcune raccomandazioni aggiuntive. Prima di tutto, affinché il recupero funzioni, è assolutamente essenziale che la frase di recupero sia corretta. Se non riesci a trovare la tua frase di 12 parole, puoi utilizzare *opzione 1* per recuperare dal file di backup di Samourai. Puoi anche accedere alla tua frase di recupero direttamente in Samourai Wallet navigando in `Impostazioni`, poi `Portafoglio`, e infine selezionando `Mostra frase di recupero di 12 parole`.

Successivamente, un errore di battitura nella tua passphrase durante il recupero risulterà in chiavi derivate errate, che impediranno il recupero del tuo portafoglio su Sparrow. **La passphrase deve essere perfettamente accurata!**

Per risolvere questo problema, ti consiglio prima di tutto di verificare la validità della tua passphrase nell'applicazione Samourai come descritto nella sezione "_Verifica la passphrase_" di questo articolo:
1. **Validazione in Samourai:** Se Samourai conferma che la passphrase è corretta, prova nuovamente il recupero dall'inizio, assicurandoti di inserire accuratamente la passphrase in Sparrow senza errori;
2. **Errore Passphrase:** Se Samourai indica che la passphrase è errata, è inutile continuare i tentativi su Sparrow. Finché la passphrase corretta non viene trovata, il recupero del tuo portafoglio è impossibile. Se hai perso permanentemente la tua passphrase, mantieni al sicuro la tua applicazione Samourai. Tutto ciò che puoi fare è sperare che i server vengano riavviati in modo da poter effettuare spese direttamente dall'applicazione senza necessità di recupero. **Non tentare di connettere un Dojo in questo caso**, poiché ciò implicherebbe il reset del tuo portafoglio su Samourai, che richiede l'accesso alla passphrase.

Tra gli altri errori incontrati, molti sono relativi alla configurazione della rete su Sparrow.

Prima di tutto, assicurati che Sparrow sia correttamente configurato in modalità `mainnet` piuttosto che in modalità `testnet`. Infatti, se Sparrow cerca le tue transazioni sul Testnet, non troverà nulla, perché il tuo portafoglio è sul Mainnet. Il Testnet è una versione alternativa di Bitcoin, utilizzata esclusivamente per test e sviluppo, e opera su una rete separata dalla rete principale (Mainnet), con i propri blocchi e transazioni. Per verificare su quale rete ti trovi, clicca sulla scheda `Strumenti`, poi su `Riavvia in`. Se viene visualizzata l'opzione `Mainnet`, allora non sei sulla rete principale. Selezionala per riavviare Sparrow sul Mainnet e poi inizia di nuovo il tuo processo di recupero.

Alcuni hanno anche incontrato difficoltà nel connettere Sparrow al proprio nodo. In basso a destra di Sparrow, un interruttore colorato indica se il tuo software è correttamente connesso a un nodo Bitcoin. Per recuperare le tue transazioni Samourai, è essenziale che il software sia ben connesso. Controlla che l'interruttore sia attivato, come nella mia immagine qui sotto (giallo per un nodo pubblico, verde per Bitcoin Core e blu per un server Electrum).

Se l'interruttore non è attivato, clicca su di esso per riattivare la connessione.

Se il problema persiste, ecco alcune possibili soluzioni:
- Se stai cercando di connetterti al tuo server Electrum (blu) o al tuo Bitcoin Core (verde) e Sparrow non riesce a connettersi, controlla le informazioni di connessione in `File > Preferenze... > Server`.
- Se il problema di connessione persiste, potrebbe essere dovuto a una sincronizzazione incompleta del tuo nodo. Assicurati che il tuo nodo e il tuo indicizzatore siano sincronizzati al 100%. Se necessario, come ultima risorsa, disconnetti il tuo nodo da Sparrow e connettiti a un nodo pubblico; - Se eri già connesso a un nodo pubblico e la connessione fallisce, prova a cambiare nodo selezionandone un altro dall'elenco a discesa.

![samourai](assets/31.webp)

Se hai recuperato con successo il tuo portafoglio, ma sembra incompleto, potrebbe esserci un problema legato alla derivazione.

Un problema potrebbe verificarsi se hai usato il tuo conto deposito Samourai con un tipo di script diverso da `P2WPKH`. Per impostazione predefinita, Samourai utilizza questo tipo di script, ma se lo hai cambiato manualmente, devi anche regolarlo quando recuperi su Sparrow.

Per derivare rami per altri tipi di script, devi ripetere il processo di recupero per ogni tipo di script utilizzato. Per questo, vai su `File > Nuovo Portafoglio` su Sparrow, seleziona un altro tipo di script dall'elenco a discesa, clicca su `Nuovo o Importa Portafoglio Software`, e segui gli stessi passaggi come nel tutorial iniziale.

![samourai](assets/32.webp)

Un altro problema di derivazione che ho incontrato è relativo al valore del Gap Limit. Questo valore indica a Sparrow dopo quante indirizzi vuoti dovrebbe smettere di derivare nuovi indirizzi. Se dopo il recupero, noti che mancano alcune transazioni, questo potrebbe essere dovuto a un Gap Limit troppo basso. Per risolvere, vai sull'account che sta causando il problema, ad esempio, l'account postmix (se sono coinvolti diversi account, ripeti questa operazione per ciascuno).

![samourai](assets/33.webp)

Clicca sulla scheda `Impostazioni` e poi sul pulsante `Avanzate...`.
![samourai](assets/34.webp)
Aumenta gradualmente il valore del Gap Limit, ad esempio, qui l'ho impostato a `400`. Poi, clicca sul pulsante `Chiudi`.

![samourai](assets/35.webp)

Clicca su `Applica` per finalizzare. Sparrow deriverà quindi un numero maggiore di indirizzi e cercherà fondi su di essi, il che dovrebbe aiutare a recuperare tutte le tue transazioni.

![samourai](assets/36.webp)

Questo copre i vari problemi di recupero che ho incontrato negli ultimi giorni. Se, dopo aver provato tutte queste soluzioni, hai ancora problemi, ti invito a unirti a [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) per chiedere aiuto. Visito regolarmente questo Discord e sarei lieto di aiutare se ho la soluzione. Anche altri bitcoiner saranno in grado di condividere le loro esperienze e offrire assistenza. **In ogni caso, è essenziale mantenere confidenziale la tua frase di recupero, il tuo file di backup e la tua passphrase**. Non condividerli con nessuno, poiché ciò potrebbe permettere loro di rubare i tuoi bitcoin.

Una volta completato il recupero, ora hai accesso ai tuoi bitcoin. Questa è una buona cosa, ma potrebbe non essere sufficiente. Infatti, il sequestro dei server solleva nuovi potenziali rischi per la tua privacy. Nella sezione seguente, esamineremo questi rischi in dettaglio e delineeremo le precauzioni da prendere per proteggere la tua privacy.

## Quali sono le conseguenze per la privacy delle tue transazioni?

### Come utente Samourai senza Dojo

Se stavi usando Samourai Wallet senza aver collegato il tuo Dojo, i tuoi xpub dovevano essere comunicati ai server di Samourai affinché l'app funzionasse. Con il sequestro di questi server, è possibile che le autorità ora abbiano accesso a questi xpub.
Questo scenario rimane ipotetico. Non sappiamo se questi xpub siano stati registrati, se un'eventuale archiviazione sia stata distrutta, se le autorità li abbiano recuperati e se prevedano di utilizzarli per l'analisi della catena. Tuttavia, in una tale situazione, è prudente considerare lo scenario peggiore, in cui le autorità hanno gli xpub degli utenti che non hanno collegato il proprio Dojo. A titolo di riferimento, un xpub è una stringa di caratteri che contiene tutti gli elementi necessari per generare chiavi pubbliche figlie (chiave pubblica + codice catena). Viene utilizzato nei portafogli deterministici gerarchici per generare indirizzi di ricezione e osservare le transazioni di un account senza esporre le chiavi private associate. Questo consente, ad esempio, la creazione di un portafoglio "solo visualizzazione". Tuttavia, divulgare gli xpub può compromettere la privacy dell'utente, poiché permettono a terze parti di tracciare le transazioni e vedere i saldi degli account associati. Chiunque conosca i tuoi xpub può quindi vedere tutti gli indirizzi di ricezione del tuo portafoglio, quelli usati in passato e quelli che verranno generati in futuro.

Per gli utenti senza un Dojo, una potenziale fuga dei tuoi xpub ha due conseguenze principali:
- I coinjoin che potresti aver eseguito risultano inefficaci dal punto di vista della privacy per chiunque conosca i tuoi xpub, quindi le tue monete perdono tutto l'anonset;
- Questa persona può anche tracciare tutti gli indirizzi di ricezione del tuo Samourai Wallet.

È quindi importante considerare lo scenario peggiore e separarsi da questo portafoglio, potenzialmente compromesso in termini di privacy. Per fare ciò, crea un nuovo portafoglio da zero con un altro software, come Sparrow Wallet. Dopo aver verificato la validità dei tuoi backup, trasferisci tutti i tuoi fondi effettuando transazioni. Sebbene questa operazione non interrompa il collegamento di tracciabilità delle tue monete, impedirà alle autorità di conoscere con certezza gli indirizzi del tuo nuovo portafoglio.

Durante questa operazione di trasferimento, raccomando di evitare la consolidazione delle tue monete. Se assumiamo che i tuoi xpub siano compromessi, la consolidazione non avrà alcun impatto dal punto di vista della persona che ha accesso a questi xpub, poiché la tua privacy è già compromessa con essi. Tuttavia, ti consiglio di non consolidare troppo le tue monete principalmente per proteggere la tua privacy da altre persone. Nel peggiore dei casi, solo le autorità potrebbero avere accesso ai tuoi xpub, ma il resto del mondo non ne è a conoscenza. Quindi, dal punto di vista degli altri, consolidare le tue monete potrebbe danneggiare significativamente la tua privacy a causa dell'Euristica di Proprietà Comune dell'Input (CIOH).

Infine, per interrompere definitivamente il tracciamento, considera anche di eseguire coinjoin da questo nuovo portafoglio.
**Attenzione:** Semplicemente recuperare il tuo Samourai wallet su Sparrow Wallet non è sufficiente. È necessario creare un portafoglio completamente nuovo con una nuova frase di recupero se vuoi evitare di utilizzare xpub che potrebbero essere trapelati. Se importi il tuo seed esistente in Sparrow, stai solo cambiando il software di gestione del portafoglio, ma il portafoglio rimane lo stesso.

### Come utente di Sparrow o Samourai con Dojo

Se il tuo portafoglio è gestito solo su Sparrow Wallet, i tuoi xpub non potrebbero essere trapelati, sia che tu stia utilizzando un nodo pubblico o il tuo nodo Bitcoin. Allo stesso modo, se stai utilizzando l'app Samourai e hai sempre collegato questa app al tuo Dojo dall'creazione del tuo portafoglio, anche i tuoi xpub sono sicuri.
Tuttavia, se hai utilizzato lo stesso portafoglio in un periodo **senza il tuo Dojo** e poi con il tuo Dojo, è possibile che i server di Samourai potrebbero aver avuto accesso ai tuoi xpub, e quindi le autorità potrebbero conoscerli. Se ti trovi in questa situazione specifica, ti consiglio di seguire le raccomandazioni della sezione precedente e considerare i tuoi xpub come compromessi.
Per coloro che hanno sempre utilizzato Sparrow o Samourai con il proprio Dojo, il rischio principale è che gli anonset delle tue monete potrebbero potenzialmente essere ridotti. Supponiamo, nello scenario peggiore, che tutti gli utenti senza un Dojo abbiano i loro xpub nelle mani delle autorità, allora il percorso delle loro monete attraverso i cicli di coinjoin potrebbe essere tracciato da queste autorità.

Per illustrare questo, prendiamo un esempio concreto. Immagina di aver partecipato a un primo ciclo di coinjoin, seguito da due ulteriori cicli di coinjoin a valle. Se gli xpub degli utenti senza un Dojo non sono stati divulgati, allora l'anonset prospettico della tua moneta sarebbe 13.

![samourai](assets/37.webp)

Tuttavia, se consideriamo che gli xpub sono stati divulgati e che hai incontrato un utente senza dojo durante il coinjoin iniziale, e poi 2 durante il primo coinjoin a valle, allora il tuo anonset prospettico sarebbe solo 10 invece di 13 dal punto di vista dell'autorità.

![samourai](assets/38.webp)
Questa potenziale diminuzione dell'anonset è complessa da quantificare, poiché dipende da numerosi fattori, e ogni moneta è influenzata in modo diverso. Ad esempio, un utente senza Dojo incontrato nei cicli iniziali influisce sull'anonset prospettico molto più di uno incontrato nei cicli successivi. Per darti un'idea della situazione, che rimane ipotetica, le ultime statistiche fornite da Samourai indicavano che tra l'85% e il 90% delle monete coinvolte nei coinjoin proveniva da utenti con Dojo, Sparrow o Bitcoin Keeper, ovvero utenti che, anche nello scenario peggiore, non avrebbero visto i loro xpub divulgati.
Sebbene queste cifre siano difficili da verificare, mi sembrano coerenti per due motivi:
- Sparrow Wallet è ampiamente utilizzato;
- La maggior parte del software node-in-box offre implementazioni Dojo, e questi software mainstream come Umbrel sono molto popolari al giorno d'oggi.

Quindi, diversi aspetti devono essere considerati. Se la privacy delle tue monete nei confronti delle autorità è estremamente importante per te, sarebbe prudente prepararsi allo scenario peggiore, ed è difficile garantire al 100% che i tuoi cicli di coinjoin Whirlpool non possano essere tracciati a causa della potenziale divulgazione degli xpub degli utenti senza Dojo. Sebbene questa ipotesi sia altamente improbabile, non è impossibile.

D'altra parte, se la privacy delle tue monete nei confronti dell'autorità potenzialmente in possesso di questi xpub non è cruciale per te, allora la situazione può essere considerata diversamente.

Specifichiamo "nei confronti dell'autorità" perché è importante ricordare che solo l'autorità che ha sequestrato i server è potenzialmente a conoscenza di questi xpub. Se il tuo obiettivo nell'utilizzare coinjoin era impedire al tuo fornaio di poter seguire i tuoi fondi, allora lui non è meglio informato di prima del sequestro del server.
Infine, è essenziale considerare l'anonset iniziale della tua moneta, prima del sequestro del server. Prendiamo l'esempio di una moneta che aveva raggiunto un anonset prospettico di 40.000; la potenziale diminuzione di questo anonset è probabilmente trascurabile. Infatti, con un anonset di base già molto alto, è improbabile che la presenza di alcuni utenti senza Dojo possa cambiare radicalmente la situazione. Tuttavia, se la tua moneta aveva un anonset di 40, allora questa potenziale perdita potrebbe seriamente influenzare i tuoi anonset e potenzialmente permettere la tracciabilità. Con lo strumento WST ora fuori servizio a seguito della chiusura di OXT.me, puoi solo stimare questi anonset. Per l'anonset retrospettivo, non c'è troppo di cui preoccuparsi poiché il modello Whirlpool assicura che sia molto alto fin dal primo coinjoin, grazie all'eredità dei tuoi pari. L'unico caso in cui ciò potrebbe rappresentare un problema è se la tua moneta non è stata remixata per diversi anni ed è stata mixata all'inizio del lancio di una pool. Riguardo l'anonset prospettico, puoi esaminare la durata durante la quale la tua moneta è stata disponibile per i coinjoin. Se sono passati diversi mesi, allora probabilmente ha un anonset prospettico estremamente alto. Al contrario, se è stata aggiunta a una pool solo poche ore prima che i server venissero sequestrati, allora il suo anonset prospettico è probabilmente molto basso.
[**-> Scopri di più sugli anonset e il loro metodo di calcolo.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Un altro aspetto da considerare è l'impatto delle consolidazioni sugli anonset delle monete che sono state mixate. Dato che gli account Whirlpool non sono più accessibili tramite l'app Samourai, è probabile che molti utenti abbiano trasferito il loro portafoglio ad altri software e tentato di ritirare i loro fondi da Whirlpool. In particolare, lo scorso fine settimana, quando le commissioni sulle transazioni nella rete Bitcoin erano relativamente alte, c'era un forte incentivo tecnico ed economico a consolidare le monete post-mix. Ciò significa che è probabile che molti utenti abbiano effettuato significative consolidazioni.

Il problema con queste consolidazioni post-mix è che riducono sempre gli anonset, non solo per l'utente che le esegue, ma anche per gli utenti che ha incontrato durante i loro cicli di coinjoin. Anche se non sono stato in grado di verificare o quantificare con precisione questo fenomeno, gli incentivi economici legati alle commissioni sulle transazioni in quel momento possono portarci a supporre che gli anonset siano potenzialmente più bassi.

### Come Utente Sentinel

Il funzionamento della rete dell'applicazione di portafoglio watch-only Sentinel è simile a quello di Samourai. Per accedere alle informazioni del tuo portafoglio, l'applicazione deve trasmettere i xpubs, le chiavi pubbliche e gli indirizzi che hai fornito a un Dojo. Se hai sempre usato il tuo Dojo su Sentinel, non c'è problema e puoi continuare a usare l'applicazione senza preoccupazioni. Tuttavia, se eri dipendente dai server di Samourai per il tuo Sentinel, è possibile che i tuoi xpubs siano stati esposti. In questo caso, è consigliabile seguire lo stesso processo di cambio del portafoglio raccomandato per Samourai Wallet quando connesso ai server di Samourai.

Nell'improbabile evento in cui stessi usando il tuo Dojo con Samourai ma non con Sentinel, sarebbe più saggio considerare che i tuoi xpubs siano compromessi.

## Conclusione
Grazie per aver letto questo articolo fino alla fine. Se pensi che manchino informazioni o se hai suggerimenti, per favore non esitare a contattarmi per condividere i tuoi pensieri. Inoltre, se hai bisogno di ulteriore assistenza nel recuperare il tuo Samourai Wallet nonostante questa guida, ti invito a unirti al [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) per chiedere aiuto. Visito regolarmente questo Discord e sarei lieto di assisterti se ho la soluzione. Anche altri bitcoiner saranno in grado di condividere le loro esperienze e offrire il loro supporto. **In ogni caso, è essenziale mantenere confidenziale la tua frase di recupero, il tuo file di backup e la tua passphrase**. Non condividerli con nessuno, poiché ciò potrebbe permettere loro di rubare i tuoi bitcoin.