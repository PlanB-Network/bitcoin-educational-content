---
name: Ashigaru - Whirlpool Coinjoin
description: Come faccio a fare coinjoin sull'applicazione Ashigaru?
---

![cover](assets/cover.webp)



"Un bitcoin wallet per le strade"



In questo tutorial imparerete cos'è una coinjoin e come realizzarne una con l'applicazione Ashigaru Terminal e l'implementazione del Whirlpool, un protocollo di coinjoin ereditato dal Samourai Wallet.



## Come funzionano i coinjoint Whirlpool



In questo tutorial non riprenderò la nozione di coinjoin, la sua utilità o il funzionamento teorico della Whirlpool, poiché questi argomenti sono già stati spiegati in dettaglio nella parte 5 del corso di formazione BTC 204 della Plan ₿ Academy. Se non avete ancora imparato il funzionamento del Whirlpool o il principio di una coinjoin, vi consiglio vivamente di consultare questa parte 5 prima di continuare:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Tuttavia, ecco alcuni dati e fatti rapidi che possono essere utili.



I portafogli compatibili Whirlpool utilizzano 4 conti separati per soddisfare le esigenze del processo di coinjoin:




- Il conto **Deposit**, identificato dall'indice `0'` ;
- Il conto della **Bad Bank** (o *scambio di diossine*), identificato dall'indice `2.147.483.644'` ;
- Il conto **Premix**, identificato dall'indice `2 147 483 645'` ;
- Il conto **Postmix**, identificato dall'indice `2 147 483 646'`.



Su Ashigaru, nel novembre 2025, sono disponibili due denominazioni di piscine (questo elenco probabilmente si evolverà nei prossimi mesi: ricordatevi quindi di controllare i valori mentre leggete):




- 0.25 BTC`, con una tassa di iscrizione di `0,0125 BTC`;
- 0.025 BTC, con una quota di iscrizione di 0,00125 BTC.



Ogni ciclo di miscelazione può coinvolgere da 5 a 10 UTXO in ingresso e in uscita.



![Image](assets/fr/01.webp)



## Requisiti del software



Per realizzare coinjoin con Whirlpool, sono necessari tre programmi distinti:





- Ashigaru Terminal**, che consente di gestire le coinjoin direttamente dal computer;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, l'applicazione sul tuo smartphone con cui puoi spendere i tuoi bitcoin in *postmix* da qualsiasi luogo;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, un'implementazione del nodo Bitcoin che garantisce una connessione sovrana alla rete, senza dipendere da un server di terze parti.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Installate ciascuno di questi strumenti seguendo le rispettive esercitazioni, quindi potete iniziare a creare le vostre prime coinjoin.



## Ricevere bitcoin



Dopo aver creato il vostro portafoglio, inizierete con un singolo conto, identificato dall'indice `0'. Questo è il conto `Deposit`. È a questo conto che invierete i bitcoin destinati ai coinjoin. È possibile riceverli sia tramite l'applicazione Ashigaru (si veda la parte 5 del tutorial dedicato), sia tramite Ashigaru Terminal (anch'esso dettagliato nella parte 5 del tutorial dedicato).



Una volta che il conto di deposito contiene almeno l'importo necessario per partecipare al pool più piccolo (più le spese di servizio e il minimo richiesto per coprire i costi del mining), sarete pronti a iniziare le vostre prime coinjoin.



![Image](assets/fr/02.webp)



## Rendere il Tx0



Una volta che i fondi sono arrivati sul conto di deposito e la transazione è stata confermata, è possibile avviare il processo di coinjoin. Per fare ciò, sul Terminale Ashigaru, aprire il menu "Portafogli" e selezionare il proprio wallet. Se il proprio wallet è bloccato, il software richiederà la password e il passphrase. Se il tuo wallet è bloccato, il software ti chiederà la password e il passphrase.



![Image](assets/fr/03.webp)



Selezionare quindi il conto "Deposito".



![Image](assets/fr/04.webp)



Andare al menu `UTXOs`.



![Image](assets/fr/05.webp)



Qui verrà visualizzato un elenco di tutti gli UTXO presenti nel conto di deposito. Selezionare quelli che si desidera inviare nei cicli coinjoin.



Per una maggiore riservatezza e per evitare la *Common Input Ownership Heuristic (CIOH)*, si raccomanda di utilizzare un solo UTXO per ogni ingresso in Whirlpool (una spiegazione dettagliata di questo principio si trova in BTC 204).



Premere il tasto `INVIO' sulla tastiera per selezionare un UTXO: un asterisco `(*)` apparirà accanto ad esso per indicare che è stato selezionato.



![Image](assets/fr/06.webp)



Quindi fare clic sul pulsante `Mix Selected`.



![Image](assets/fr/07.webp)



Se si dispone di un UTXO sufficientemente grande per partecipare a uno dei due pool disponibili, è possibile selezionare il pool di destinazione utilizzando le frecce. In questa pagina vengono visualizzati i dettagli del proprio Tx0 :




- il numero di UTXO che entreranno nel pool;
- le varie commissioni applicate (commissioni di servizio e commissioni mining) ;
- l'entità del *cambiamento tossico*.



Controllare attentamente le informazioni, quindi fare clic su `Broadcast` per trasmettere il Tx0.



![Image](assets/fr/08.webp)



Ashigaru visualizzerà quindi il TXID del vostro Tx0, confermando che la transazione è stata trasmessa in rete.



![Image](assets/fr/09.webp)



## Creazione di coinjoin



Una volta che il Tx0 è stato trasmesso, tornate alla pagina iniziale del vostro conto di deposito, quindi fate clic su "Conti" e selezionate il conto "Premix".



![Image](assets/fr/10.webp)



Nel menu `UTXOs`, si vedranno le varie parti equalizzate, pronte per entrare nei cicli di coinjoin. Non appena Tx0 viene confermato, il terminale Ashigaru inizierà automaticamente il primo ciclo di miscelazione.



![Image](assets/fr/11.webp)



Una volta confermato il Tx0, la prima transazione coinjoin verrà creata e trasmessa automaticamente dal terminale Ashigaru. Andando su "Conti > Postmix > UTXO", è possibile visualizzare gli UTXO equalizzati, in attesa della conferma del loro primo ciclo.



![Image](assets/fr/12.webp)



Ora è possibile lasciare Ashigaru Terminal in esecuzione in background: continuerà a mixare e remixare i brani automaticamente.



## Rifinitura delle giunzioni a moneta



Ora potete lasciare che le vostre monete si rimescolino automaticamente. Il modello Whirlpool significa che non ci sono costi aggiuntivi per il rimescolamento: niente commissioni di servizio, niente commissioni mining. Quindi, lasciare che le vostre monete partecipino a un maggior numero di cicli di miscelazione non può che giovare alla vostra riservatezza.



Per una migliore comprensione di questo meccanismo e di quanti cicli vale la pena aspettare, vi consiglio di leggere questo articolo:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Per visualizzare il numero di remix eseguiti da ciascuno dei vostri brani, aprite il menu `UTXOs` nell'account `Postmix`.



![Image](assets/fr/13.webp)



Per spendere le monete miste, accedere all'applicazione Ashigaru, che utilizza lo stesso wallet del software Ashigaru Terminal. Il wallet visualizzato all'apertura corrisponde al conto `Deposit`. Per accedere al conto `Postmix`, che contiene le UTXO miste, cliccare sul simbolo Whirlpool nell'angolo in alto a destra.



![Image](assets/fr/14.webp)



In questo conto, vedrete tutte le vostre monete attualmente mescolate. Per spenderle, premere il simbolo `+` in basso a destra dello schermo, quindi selezionare `Invio`.



![Image](assets/fr/15.webp)



Inserite i dettagli della vostra transazione: l'indirizzo del destinatario, l'importo da inviare e, se lo desiderate, scegliete una struttura di transazione specifica per aumentare ulteriormente la vostra riservatezza (consultate i tutorial corrispondenti).



![Image](assets/fr/16.webp)



Controllare attentamente i dettagli della transazione, quindi trascinare la freccia in fondo allo schermo per confermare la spedizione.



![Image](assets/fr/17.webp)



La vostra transazione è stata firmata e trasmessa sulla rete Bitcoin.



![Image](assets/fr/18.webp)



## Spendete il cambiamento doxxico



Ricordate: Il modello del Whirlpool si basa sull'equalizzazione dei pezzi a Tx0, prima che entrino nei pool. È questo meccanismo che interrompe il tracciamento degli UTXO. A mio parere, questo è il modello di coinjoin più efficiente, ma ha uno svantaggio: genera un *cambio* che non passa attraverso il processo di coinjoin.



Questa modifica corrisponde a un UTXO creato per ogni Tx0. È isolata in un conto specifico denominato `Cambio tossico` o `Bad Bank`, a seconda del software, per evitare di utilizzarla con gli altri UTXO. Questo è molto importante, perché questi UTXO non sono stati mescolati: i loro collegamenti di tracciabilità rimangono intatti e possono compromettere la vostra riservatezza stabilendo una connessione tra voi e la vostra attività di coinjoin. Maneggiateli quindi con cura e **non usateli mai con altri UTXO**, che siano mescolati o meno. La combinazione di un UTXO tossico con un UTXO misto annullerà tutti i vantaggi in termini di privacy ottenuti con le coinjoin.



Per il momento, Ashigaru non offre un accesso diretto a questo account `Doxxic Change` (almeno, io non l'ho trovato). Questa funzione sarà probabilmente aggiunta in un aggiornamento futuro. Nel frattempo, l'unico modo per recuperare questi fondi è importare il tuo seed nel Sparrow Wallet. Quest'ultimo normalmente rileverà automaticamente che il tuo seed è un conto di denaro. Quest'ultimo normalmente rileverà automaticamente che si tratta di un wallet usato con il Whirlpool e vi darà accesso a tutti e quattro i conti, compreso il conto `Doxxic Change`. Potete quindi spendere questi UTXO come normali bitcoin dal Sparrow.



Ecco alcune possibili strategie per gestire le UTXO in valuta estera da coinjoin senza compromettere la propria privacy:





- Se il vostro UTXO tossico è abbastanza grande da unirsi a un pool più piccolo, questa è generalmente l'opzione migliore. Fate attenzione, però, a non unire mai più UTXO tossici per ottenere questo risultato, perché in questo modo si creerà un legame tra le varie voci del Whirlpool.





- Contrassegnarli come non spendibili: ** Un altro approccio prudente è quello di tenerli semplicemente così come sono nel loro conto separato e lasciarli inalterati. In questo modo si eviterà di spenderli accidentalmente. Se il valore dei bitcoin aumenta, potrebbero essere aperti nuovi pool adeguati alle loro dimensioni.





- Effettuare donazioni:** È possibile scegliere di trasformare questi UTXO tossici in donazioni a sviluppatori Bitcoin, progetti open-source o associazioni che accettano BTC. Questo vi permette di smaltirli in modo utile e di sostenere l'ecosistema.





- Acquistare carte regalo prepagate o carte Visa:** Piattaforme come [Bitrefill] (https://www.bitrefill.com/) consentono di scambiare i bitcoin con carte regalo o carte Visa ricaricabili che possono essere utilizzate nei negozi. Questo può essere un modo semplice e discreto per spendere gli UTXO tossici.





- Scambiarli con Monero:** Samourai Wallet offriva un servizio di scambio atomico BTC/XMR, ora scomparso. Se esiste un servizio simile (personalmente non ne conosco), è un'ottima soluzione per isolare questi UTXO, convertirli in Monero e poi eventualmente rispedirli a Bitcoin. Tuttavia, questo metodo era costoso e dipendeva dalla liquidità disponibile. Tuttavia, questo metodo è costoso e dipende dalla liquidità disponibile.





- Trasferirli al Lightning Network:** Trasferire questi UTXO al Lightning Network per beneficiare di commissioni di transazione ridotte è un'opzione potenzialmente interessante. Tuttavia, questo metodo può rivelare alcune informazioni a seconda dell'uso che si fa di Lightning e deve quindi essere usato con cautela.



## Come posso conoscere la qualità dei nostri cicli di coinjoin?



Per essere veramente efficace, una coinjoin deve presentare un elevato grado di uniformità tra gli importi in entrata e in uscita. Questa uniformità aumenta il numero di possibili interpretazioni per un osservatore esterno, che a sua volta aumenta l'incertezza sulla transazione. Per misurare questa incertezza, utilizziamo il concetto di entropia applicato alla transazione. Il modello Whirlpool è riconosciuto come uno dei più efficaci in questo senso, in quanto garantisce un'eccellente omogeneità tra i partecipanti. Per un approfondimento di questo principio, vi consiglio di consultare l'ultimo capitolo della Parte 5 del corso di formazione BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Le prestazioni di diversi cicli coinjoin si misurano in base alla dimensione degli insiemi in cui è nascosta una moneta. Questi insiemi definiscono i cosiddetti *anonset*. Ne esistono due tipi: il primo misura la riservatezza di fronte all'analisi retrospettiva (dal presente al passato), mentre il secondo misura la resistenza all'analisi prospettica (dal passato al presente). Per una spiegazione completa di questi due indicatori, leggete il seguente tutorial (o, ancora una volta, il corso di formazione BTC 204):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Come gestire il postmix?



Dopo aver eseguito diversi cicli di coinjoin, la strategia migliore è quella di mantenere gli UTXO nel conto `Postmix`, lasciandoli rimescolare indefinitamente fino a quando non si ha realmente bisogno di spenderli.



Alcuni utenti preferiscono trasferire i loro bitcoin misti in un hardware wallet protetto. Questa opzione è possibile, ma richiede un certo rigore per garantire che la riservatezza acquisita con coinjoin non venga compromessa.



La fusione degli UTXO è l'errore più frequente. È importante non combinare mai UTXO misti con UTXO non misti nella stessa transazione, altrimenti si rischia di attivare il *Common Input Ownership Heuristic (CIOH)*. Ciò implica una gestione rigorosa degli UTXO, in particolare attraverso un'etichettatura chiara e precisa. In generale, la fusione degli UTXO è una pratica scorretta che, se mal gestita, porta spesso a una perdita di riservatezza.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Occorre inoltre essere cauti nel consolidare UTXO miste. Si possono prendere in considerazione consolidamenti limitati se gli UTXO hanno anonset significativi, ma riducono inevitabilmente il livello di riservatezza. Evitate consolidamenti massicci o affrettati, effettuati prima di un numero sufficiente di remix, perché potrebbero stabilire collegamenti inferenziali tra i vostri pezzi pre- e post-mix. In caso di dubbio, è meglio non consolidare gli UTXO postmix e trasferirli uno per uno sull'hardware wallet, generando ogni volta un nuovo indirizzo di ricezione vuoto. Non dimenticate di etichettare ogni UTXO trasferito.



Sconsigliamo vivamente di spostare le UTXO postmix in portafogli che utilizzano script di minoranza. Ad esempio, se avete partecipato alla Whirlpool da un portafoglio multi-sig in `P2WSH`, sarete in pochi a condividere questo tipo di script. Inviando i vostri UTXO postmix a questo stesso tipo di script, riducete notevolmente il vostro anonimato. Oltre al tipo di script, altre impronte digitali specifiche di wallet possono compromettere la vostra riservatezza, quindi la cosa migliore da fare è spenderle dall'applicazione Ashigaru.



Infine, come per tutte le transazioni Bitcoin, non riutilizzate mai un indirizzo di ricezione. Ogni pagamento deve essere inviato a un nuovo, unico indirizzo vuoto.



Il metodo più semplice e sicuro è lasciare che gli UTXO misti riposino nel loro conto `Postmix`, lasciarli rimescolare naturalmente e spenderli solo quando necessario da Ashigaru.



I portafogli Ashigaru e Sparrow incorporano ulteriori salvaguardie contro gli errori più comuni associati all'analisi della blockchain, aiutandovi a preservare la riservatezza delle vostre transazioni.