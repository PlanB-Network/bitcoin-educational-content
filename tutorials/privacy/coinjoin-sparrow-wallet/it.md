---
name: Coinjoin - Sparrow Wallet
description: Come eseguire un coinjoin su Sparrow Wallet?
---
![cover](assets/cover.webp)

***ATTENZIONE:** In seguito all'arresto dei fondatori di Samourai Wallet e al sequestro dei loro server il 24 aprile, lo strumento Whirlpool non funziona più, anche per coloro che dispongono del proprio Dojo o utilizzano Sparrow Wallet. Tuttavia, rimane possibile che questo strumento possa essere rimesso in servizio nelle prossime settimane o rilanciato in modo diverso. Inoltre, la parte teorica di questo articolo rimane pertinente per comprendere i principi e gli obiettivi dei coinjoins in generale (non solo Whirlpool), oltre a comprendere l'efficacia del modello Whirlpool.*

_Stiamo seguendo da vicino l'evoluzione di questo caso così come gli sviluppi relativi agli strumenti associati. Siate certi che aggiorneremo questo tutorial non appena saranno disponibili nuove informazioni._

_Questo tutorial è fornito solo a scopo educativo e informativo. Non approviamo né incoraggiamo l'uso di questi strumenti per scopi criminali. È responsabilità di ogni utente rispettare le leggi vigenti nella propria giurisdizione._

---

In questo tutorial, imparerai cos'è un coinjoin e come eseguirne uno utilizzando il software Sparrow Wallet e l'implementazione Whirlpool.

## Cos'è un coinjoin su Bitcoin?

**Un coinjoin è una tecnica che interrompe la tracciabilità dei bitcoin sulla blockchain**. Si basa su una transazione collaborativa con una struttura specifica dello stesso nome: la transazione coinjoin.

I coinjoin migliorano la privacy degli utenti Bitcoin complicando l'analisi della blockchain per gli osservatori esterni. La loro struttura consente di unire più input da diversi utenti in una singola transazione, offuscando così le tracce e rendendo difficile determinare i collegamenti tra gli indirizzi di input e output.

Il principio del coinjoin si basa su un approccio collaborativo: diversi utenti che desiderano mixare i loro bitcoin depositano importi identici come input della stessa transazione. Questi importi vengono poi ridistribuiti come output di pari valore a ciascun utente. Al termine della transazione, diventa impossibile associare un output specifico a un utente conosciuto in input. Non esiste un collegamento diretto tra gli input e gli output, il che rompe l'associazione tra gli utenti e i loro UTXO, così come la storia di ogni moneta.
![coinjoin](assets/notext/1.webp)

Esempio di una transazione coinjoin (non mia): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/it/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Per eseguire un coinjoin garantendo che ogni utente mantenga il controllo sui propri fondi in ogni momento, il processo inizia con la costruzione della transazione da parte di un coordinatore, che poi la trasmette ai partecipanti. Ogni utente firma quindi la transazione dopo aver verificato che sia di suo gradimento. Tutte le firme raccolte vengono infine integrate nella transazione. Se un utente o il coordinatore tenta di dirottare fondi, modificando gli output della transazione coinjoin, le firme risulteranno invalide, portando al rifiuto della transazione da parte dei nodi.

Esistono diverse implementazioni di coinjoin, come Whirlpool, JoinMarket o Wabisabi, ognuna con l'obiettivo di gestire il coordinamento tra i partecipanti e aumentare l'efficienza delle transazioni coinjoin.
In questo tutorial, ci addentreremo nell'implementazione di **Whirlpool**, che considero essere la soluzione più efficiente per eseguire coinjoin su Bitcoin. Sebbene disponibile su diversi portafogli, in questo tutorial, esploreremo esclusivamente il suo utilizzo con l'applicazione mobile Samourai Wallet, senza Dojo.

## Perché eseguire coinjoin su Bitcoin?

Uno dei problemi iniziali con qualsiasi sistema di pagamento peer-to-peer è il doppio pagamento: come impedire a individui malintenzionati di spendere le stesse unità monetarie più volte senza ricorrere ad un'autorità centrale per arbitrare?

Satoshi Nakamoto ha fornito una soluzione a questo dilemma attraverso il protocollo Bitcoin, un sistema di pagamento elettronico peer-to-peer che opera indipendentemente da qualsiasi autorità centrale. Nel suo white paper, sottolinea che l'unico modo per certificare l'assenza di doppio pagamento è garantire la visibilità di tutte le transazioni all'interno del sistema di pagamento.
Per garantire che ogni partecipante sia a conoscenza delle transazioni, queste devono essere divulgate pubblicamente. Pertanto, il funzionamento di Bitcoin si basa su un'infrastruttura trasparente e distribuita, che consente a qualsiasi operatore di nodo di verificare l'intera catena delle firme elettroniche e la storia di ogni moneta, dalla sua creazione da parte di un miner.

La natura trasparente e distribuita della blockchain di Bitcoin implica che qualsiasi utente della rete può seguire ed analizzare le transazioni di tutti gli altri partecipanti. Di conseguenza, l'anonimato a livello di transazione è impossibile. Tuttavia, l'anonimato è preservato a livello di identificazione individuale. A differenza del sistema bancario tradizionale dove ogni conto è collegato a un'identità personale, su Bitcoin i fondi sono associati a coppie di chiavi crittografiche, offrendo così agli utenti una forma di pseudonimato dietro identificatori crittografici.

Pertanto, la riservatezza su Bitcoin è compromessa quando osservatori esterni riescono ad associare specifici UTXO ad utenti identificati. Una volta stabilita questa associazione, diventa possibile tracciare le loro transazioni ed analizzare la storia dei loro bitcoin. Coinjoin è precisamente una tecnica sviluppata per rompere la tracciabilità degli UTXO, offrendo così un certo livello di riservatezza agli utenti di Bitcoin a livello di transazione.

## Come funziona Whirlpool?

Whirlpool si distingue dagli altri metodi coinjoin utilizzando transazioni "_ZeroLink_", che garantiscono che non ci sia tecnicamente alcun collegamento possibile tra tutti gli input e tutti gli output. Questo perfetto mescolamento è ottenuto attraverso una struttura in cui ogni partecipante contribuisce con un importo identico in input (ad eccezione delle commissioni di mining), generando così output di importi perfettamente uguali.
Questo approccio restrittivo agli input conferisce alle transazioni coinjoin di Whirlpool una caratteristica unica: l'assenza completa di collegamenti deterministici tra gli input e gli output. In altre parole, ogni output ha una probabilità uguale di essere attribuito a qualsiasi partecipante, rispetto a tutti gli altri output nella transazione.
Inizialmente, il numero di partecipanti in ogni coinjoin Whirlpool era limitato a 5, con 2 nuovi entranti e 3 remixers (spiegheremo questi concetti più avanti). Tuttavia, l'aumento delle commissioni per le transazioni on-chain osservato nel 2023 ha spinto i team di Samourai a ripensare il loro modello per migliorare la privacy riducendo i costi. Pertanto, tenendo conto della situazione del costo delle commissioni e del numero di partecipanti, il coordinatore può ora organizzare coinjoin che includono 6, 7 o 8 partecipanti. Queste sessioni potenziate sono denominate "_Cicli di Surge_". È importante notare che, indipendentemente dalla configurazione, ci sono sempre solo 2 nuovi entranti (per ogni round - mix) nei coinjoin di Whirlpool.

Pertanto, le transazioni Whirlpool sono caratterizzate da un numero identico di input ed output, che possono essere:

- 5 input e 5 output;
  ![coinjoin](assets/notext/2.webp)
- 6 input e 6 output;
  ![coinjoin](assets/notext/3.webp)
- 7 input e 7 output;
  ![coinjoin](assets/notext/4.webp)
- 8 input e 8 output.
  ![coinjoin](assets/notext/5.webp)
  Il modello proposto da Whirlpool si basa quindi su piccole transazioni coinjoin. A differenza di Wasabi e JoinMarket, dove la robustezza degli anonset si basa sul volume dei partecipanti in un singolo ciclo, Whirlpool scommette sulla catena di più cicli di piccole dimensioni.

In questo modello, l'utente paga le commissioni solo al suo ingresso iniziale in un pool, consentendogli di partecipare ad una moltitudine di remix senza commissioni aggiuntive. Sono i nuovi entranti a coprire le commissioni di mining per i remixers.
Con ogni coinjoin aggiuntivo a cui un UTXO partecipa, insieme ai suoi peer incontrati in passato, gli anonset cresceranno esponenzialmente. L'obiettivo è quindi sfruttare questi remix gratuiti che, ad ogni occorrenza - mix, contribuiscono ad aumentare la densità degli anonset associati a ciascun UTXO remixato.
Whirlpool è stato progettato tenendo conto di due requisiti importanti:

- L'accessibilità dell'implementazione su dispositivi mobili, dato che Samourai Wallet è principalmente un'applicazione per smartphone;
- La velocità dei cicli di remixing per promuovere un significativo aumento degli anonset.
  Questi imperativi hanno guidato le scelte degli sviluppatori di Samourai Wallet nella progettazione di Whirlpool, portandoli a limitare il numero di partecipanti per ciclo. Troppo pochi partecipanti avrebbero compromesso l'efficienza del coinjoin, riducendo drasticamente gli anonset generati ogni ciclo, mentre troppi partecipanti avrebbero posto problemi di gestione sulle applicazioni mobili e avrebbero ostacolato il flusso dei cicli.
  **In definitiva, non è necessario avere un alto numero di partecipanti per coinjoin su Whirlpool poiché gli anonset si ottengono attraverso l'accumulo di diversi cicli di coinjoin.**

[-> Scopri di più sugli anonset di Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Pool di Coinjoin e commissioni
Affinché questi cicli multipli aumentino efficacemente l'anonset, deve essere stabilito un certo quadro per limitare le quantità di UTXO utilizzati. Whirlpool definisce quindi diversi pool, o gruppi.

Una pool rappresenta un gruppo di utenti, che concordano sulla quantità di UTXO da utilizzare per ottimizzare il processo di coinjoin. Ogni pool specifica un importo fisso per l'UTXO a cui l'utente deve attenersi per partecipare. Quindi, per eseguire coinjoin con Whirlpool, è necessario selezionare una specifico pool tra le seguenti:
- 0,5 bitcoin;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100.000 sats).
- 
Unendoti ad una pool con i tuoi bitcoin, questi verranno divisi per generare UTXO che sono perfettamente omogenei con quelli degli altri partecipanti. Ogni pool ha un limite massimo; quindi, per importi che superano questo limite, sarai costretto o a fare due ingressi separati all'interno della stessa pool o a passare ad un'altra pool con un importo maggiore:

| Pool (bitcoin) | Importo massimo per ingresso (bitcoin) |
|-------------------|----------------------------------------|
| 0,5               | 35                                     |
| 0,05              | 3,5                                    |
| 0,01              | 0,7                                    |
| 0,001             | 0,025                                  |

Come accennato in precedenza, un UTXO è considerato appartenente ad una pool quando è pronto per essere integrato in un coinjoin. Tuttavia, ciò non significa che l'utente perda il possesso di esso. **Attraverso i diversi cicli di mix, mantieni il pieno controllo delle tue chiavi e, di conseguenza, dei tuoi bitcoin.** Questo è ciò che differenzia la tecnica del coinjoin da altre tecniche di mix centralizzate.

Per entrare in una pool di coinjoin, devono essere pagate le commissioni di servizio così come le commissioni di mining. Le commissioni di servizio sono fisse per ogni pool e sono destinate a compensare i team responsabili dello sviluppo e della manutenzione di Whirlpool.
Le commissioni di servizio per l'utilizzo di Whirlpool devono essere pagate solo una volta all'ingresso nella pool. Dopo questo passaggio, hai l'opportunità di partecipare ad un numero illimitato di remix senza alcuna commissione aggiuntiva. Ecco le attuali commissioni fisse per ogni pool:

| Pool (bitcoin) | Commissione di ingresso (bitcoin) |
| -------------- | --------------------------------- |
| 0,5            | 0,0175                            |
| 0,05           | 0,00175                           |
| 0,01           | 0,0005 (50 000 sats)              |
| 0,001          | 0,00005 (5 000 sats)              |


Queste commissioni funzionano essenzialmente come un biglietto d'ingresso per la pool scelta, indipendentemente dall'importo che inserisci in coinjoin. Pertanto, sia che tu partecipi al pool da 0,01 con esattamente 0,01 BTC o vi entri con 0,5 BTC, le commissioni rimarranno le stesse in valore assoluto.

Prima di procedere ai coinjoin, l'utente ha quindi la scelta tra 2 strategie:

- Optare per una pool più piccola per minimizzare le commissioni di servizio, sapendo che ricerà in cambio diversi piccoli UTXO;
- Preferire una pool più grande, accettando di pagare commissioni più elevate, ottenendo meno UTXO ma di importo maggiore.

Generalmente si sconsiglia di unire diversi UTXO mixati dopo i cicli di coinjoin, poiché ciò potrebbe compromettere la riservatezza acquisita (dimunendo anche la riservatezza di tutti i partecipanti che avevano partecipato ai coinjoin), soprattutto a causa dell'Euristica di Proprietà Comune dell'Input (CIOH). Pertanto, potrebbe essere saggio scegliere una pool più grande, anche se ciò significa pagare di più, per evitare di avere troppi UTXO di piccolo valore in uscita. L'utente deve valutare questi compromessi per scegliere la pool che preferisce.

Oltre alle commissioni di servizio, devono essere considerate anche le commissioni di mining inerenti a qualsiasi transazione Bitcoin. Come utente di Whirlpool, sarai tenuto a pagare le commissioni di mining per la transazione di preparazione (`Tx0`) così come quelle per il primo coinjoin. Tutti i remix successivi saranno gratuiti, grazie al modello di Whirlpool che si basa sul pagamento dei nuovi partecipanti.

Infatti, in ogni coinjoin di Whirlpool, due utenti tra tutti gli input sono nuovi partecipanti. Gli altri input provengono dai remixer. Di conseguenza, le commissioni di mining per tutti i partecipanti alla transazione sono coperte da questi due nuovi partecipanti, che beneficeranno poi anche di remix gratuiti:
![coinjoin](assets/it/6.webp)
Grazie a questo sistema di commissioni, Whirlpool si differenzia veramente da altri servizi di coinjoin poiché gli anonset degli UTXO non sono proporzionali al prezzo pagato dall'utente. Così, è possibile raggiungere livelli di anonimato considerevolmente alti pagando solo la commissione di ingresso nella pool e le commissioni di mining per due transazioni (la `Tx0` e il mix iniziale).
È importante notare che l'utente dovrà anche coprire le commissioni di mining per prelevare i propri UTXO dalla pool dopo aver completato i cicli di coinjoin, a meno che non abbiano selezionato l'opzione `mix to`, di cui parleremo nel tutorial qui sotto.

### Gli account del portafoglio HD utilizzati da Whirlpool
Per eseguire un coinjoin tramite Whirlpool, il portafoglio deve generare diversi account distinti. Un account, nel contesto di un portafoglio HD (Hierarchical Deterministic), costituisce una sezione completamente isolata dalle altre, questa separazione avviene al terzo livello di profondità della gerarchia del portafoglio, ovvero a livello dell'`xpub`.
Un portafoglio HD può teoricamente derivare fino a `2^(32/2)` account diversi. L'account iniziale, utilizzato di default su tutti i portafogli Bitcoin, corrisponde all'indice `0'`.

Per i portafogli adattati a Whirlpool, come Samourai o Sparrow, vengono utilizzati 4 account per soddisfare le esigenze del processo di coinjoin:
- L'account **deposito**, identificato dall'indice `0'`;
- L'account **bad bank** (o cambio tossico), identificato dall'indice `2 147 483 644'`;
- L'account **premix**, identificato dall'indice `2 147 483 645'`;
- L'account **postmix**, identificato dall'indice `2 147 483 646'`.

Ciascuno di questi account svolge una funzione specifica all'interno del coinjoin.
Tutti questi account sono collegati a un unico seed, che consente all'utente di recuperare l'accesso a tutti i suoi bitcoin utilizzando la propria frase di recupero e, se applicabile, la propria passphrase. Tuttavia, è necessario specificare al software, durante questa operazione di recupero, i diversi indici degli account che sono stati utilizzati.
Ora esaminiamo le diverse fasi di un coinjoin Whirlpool all'interno di questi account.

### Le diverse fasi dei coinjoin su Whirlpool
**Fase 1: La Tx0**
Il punto di partenza di qualsiasi coinjoin Whirlpool è l'account **deposito**. Questo account è quello che utilizzi automaticamente quando crei un nuovo portafoglio Bitcoin. Questo account deve essere accreditato con i bitcoin che si desidera mixare.
La `Tx0` rappresenta il primo passo nel processo di mixing di Whirlpool. Ha lo scopo di preparare ed omogeneizzare l'UTXO per il coinjoin, dividendo questi ultimi in unità corrispondenti all'importo della pool selezionata, per garantire l'omogeneità del mixing. Gli UTXO omogeneizzati vengono quindi inviati all'account **premix**. Per quanto riguarda la differenza che non può entrare nella pool, viene separata in un account specifico: il **bad bank** (o "cambio tossico").
Questa transazione iniziale `Tx0` serve anche per le commissioni di servizio dovute al coordinatore del mix. A differenza dei passaggi successivi, questa transazione non è collaborativa; l'utente deve quindi sostenere tutte le commissioni di mining:
![coinjoin](assets/it/7.webp)

In questo esempio di transazione `Tx0`, un input di `372,000 sats` dal nostro account **deposito** viene diviso in diversi UTXO di output, che sono distribuiti come segue:

- Un importo di `5,000 sats` destinato al coordinatore per le commissioni di servizio, corrispondente all'ingresso nella pool di `100,000 sats`;
- Tre UTXO preparati per il mixing, reindirizzati al nostro account **premix** e registrati presso il coordinatore. Questi UTXO sono omogeneizzati a `108,000 sats` ciascuno, per coprire le commissioni di mining per il loro futuro mix iniziale;
- L'eccedenza che non può entrare nella pool, essendo troppo piccola, è considerata cambio tossico. Viene inviata al suo account specifico. Qui, questo cambio ammonta a `40,000 sats`;
- Infine, ci sono `3,000 sats` che non costituiscono un output, ma sono le commissioni di mining necessarie per confermare la `Tx0`.

Ad esempio, ecco un vero Whirlpool Tx0 (non mio): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/it/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Fase 2: Il cambio tossico**
L'eccedenza che non può essere integrata nel pool, qui equivalente a `40.000 sats`, viene reindirizzata al conto **bad bank**, anche definito "cambio tossico", per garantire una stretta separazione dagli altri UTXO nel portafoglio.
Questo UTXO è pericoloso per la privacy dell'utente perché non solo è ancora legato al suo passato, e quindi possibilmente all'identità del suo proprietario, ma inoltre risulta chiaro per un osservatore esterne come appartenente ad un utente che ha eseguito un coinjoin.
Se questo UTXO viene unito con output mixati, questi perderanno tutta la riservatezza ottenuta durante i cicli di coinjoin, in particolare a causa della Common-Input-Ownership-Heuristic (CIOH). Se viene unito con altri cambi tossici, l'utente rischia di perdere la riservatezza poiché ciò collegherà i diversi input dei cicli di coinjoin. Pertanto, deve essere gestito con cautela. Il modo di gestire questo UTXO tossico sarà dettagliato nell'ultima parte di questo articolo, e futuri tutorial copriranno questi metodi più approfonditamente su PlanB Network.

**Passo 3: Il Mix Iniziale**
Dopo che la `Tx0` è completata, gli UTXO equalizzati vengono inviati al conto **premix** del nostro portafoglio, pronti per essere introdotti nel loro primo ciclo di coinjoin, chiamato anche "mix iniziale". Se, come nel nostro esempio, il `Tx0` genera diversi UTXO destinati al mixing, ognuno di essi sarà integrato in un coinjoin iniziale separato.

Al termine di questi primi mix, il conto **premix** sarà vuoto, mentre i nostri UTXO, avendo pagato le commissioni di mining per questo primo coinjoin, saranno esattamente pari all'importo definito dalla pool scelta. Nel nostro esempio, i nostri UTXO iniziali di `108.000 sats` saranno stati ridotti esattamente a `100.000 sats`.
![coinjoin](assets/it/8.webp)
**Passo 4: I Remix**
Dopo il mix iniziale, gli UTXO vengono trasferiti al conto **postmix**. Questo conto raccoglie gli UTXO già mescolati e quelli in attesa di remix. Quando il client Whirlpool è attivo, gli UTXO situati nel conto **postmix** sono automaticamente disponibili per il remix e verranno scelti casualmente per partecipare a questi nuovi cicli.

Come promemoria, i remix sono poi al 100% gratuiti: non sono richieste commissioni di servizio aggiuntive o commissioni di mining. Mantenere gli UTXO nel conto **postmix** mantiene quindi intatto il loro valore e migliora simultaneamente il loro anonset. Ecco perché è importante consentire a questi UTXO di partecipare a più cicli di coinjoin. Non ti costa assolutamente nulla e aumenta i loro livelli di anonimato.

Quando decidi di spendere UTXO mescolati, puoi farlo direttamente da questo conto **postmix**. È consigliabile mantenere gli UTXO mescolati in questo conto per beneficiare dei remix gratuiti e per evitare che lascino il circuito Whirlpool, il che potrebbe diminuire la loro riservatezza.

Come vedremo nel tutorial seguente, esiste anche l'opzione `mix to` che offre la possibilità di inviare automaticamente le tue monete mixate a un altro portafoglio, come un cold wallet, dopo un numero definito di coinjoin.

Dopo aver discusso la teoria, immergiamoci nella pratica con un tutorial sull'uso di Whirlpool tramite il software desktop Sparrow Wallet!

## Tutorial: Coinjoin Whirlpool su Sparrow Wallet
Ci sono numerose opzioni per utilizzare Whirlpool. La prima che voglio presentarvi è l'opzione Sparrow Wallet, un software open-source per la gestione di portafogli Bitcoin per PC.
Usare Sparrow ha il vantaggio di essere abbastanza facile da iniziare, veloce da configurare e richiede solo un computer e una connessione internet. Tuttavia, c'è uno svantaggio notevole: i coinjoin avverranno solo quando Sparrow è avviato e connesso. Questo significa che se vuoi mixare e remixare i tuoi bitcoin 24/7, dovrai tenere costantemente acceso il tuo computer.

### Installa Sparrow Wallet
Per iniziare, avrai ovviamente bisogno del software Sparrow Wallet. Puoi scaricarlo direttamente dal [sito ufficiale](https://sparrowwallet.com/download/) o su [il loro GitHub](https://github.com/sparrowwallet/sparrow/releases).
Prima di installare il software, sarà importante verificare la firma e l'integrità dell'eseguibile appena scaricato. Se desideri maggiori dettagli sul processo di installazione e verifica del software Sparrow, ti consiglio di leggere questo altro tutorial: *[Le Guide di Sparrow Wallet](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*

### Creare un Portafoglio Software
Dopo aver installato il software, dovrai procedere con la creazione di un portafoglio Bitcoin. È importante notare che per partecipare ai coinjoin, l'uso di un portafoglio software (chiamato anche "hot wallet") è essenziale. Pertanto, **non sarà possibile eseguire coinjoin con un portafoglio protetto da un hardware wallet**.

Anche se non è imperativo, nel caso in cui tu preveda di mescolare importi significativi, è altamente raccomandato optare per l'uso di una forte passphrase BIP39 per questo portafoglio.

Per creare un nuovo portafoglio, apri Sparrow, poi clicca sulla scheda `File` e su `Nuovo Portafoglio`.

![sparrow](assets/notext/9.webp)

Scegli un nome per questo portafoglio, per esempio: "Portafoglio Coinjoin". Clicca sul pulsante `Crea Portafoglio`.

![sparrow](assets/notext/10.webp)

Lascia le impostazioni predefinite, poi clicca sul pulsante `Nuovo o Importa Portafoglio Software`.

![sparrow](assets/notext/11.webp)

Quando accedi alla finestra di creazione del portafoglio, ti consiglio di scegliere una sequenza di 12 parole, poiché è ampiamente sufficiente. Seleziona `Genera Nuovo` per generare una nuova frase di recupero, e clicca su `Usa Passphrase` se desideri aggiungere una passphrase BIP39. È importante fare un backup fisico delle tue informazioni di recupero, sia su carta che su un supporto metallico, per garantire la sicurezza dei tuoi bitcoin.

![sparrow](assets/notext/12.webp)
Assicurati della validità del tuo backup della frase di recupero prima di cliccare su `Conferma Backup...`. Sparrow ti chiederà quindi di inserire nuovamente la tua frase per verificare che tu l'abbia presa in nota. Una volta completato questo passaggio, continua cliccando su `Crea Keystore`.
![sparrow](assets/notext/13.webp)

Lascia il percorso di derivazione suggerito come predefinito e premi `Importa Keystore`. Nel mio esempio, il percorso di derivazione differisce leggermente poiché sto usando Testnet per questo tutorial. Il percorso di derivazione che dovrebbe apparire per te è il seguente:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

Dopo ciò, Sparrow mostrerà i dettagli della derivazione del tuo nuovo portafoglio. Nel caso in cui tu abbia impostato una passphrase, è altamente raccomandato annotare la tua `Master fingerprint`. Anche se questa impronta digitale della chiave principale non è un dato sensibile, ti sarà utile per verificare in seguito che stai effettivamente accedendo al portafoglio corretto e per confermare l'assenza di errori nell'inserimento della tua passphrase.

Clicca sul pulsante `Applica`.

![sparrow](assets/notext/15.webp)

Sparrow ti invita a creare una password per il tuo portafoglio. Questa password sarà richiesta per accedervi tramite il software Sparrow Wallet. Scegli una password forte, fai un backup di essa, e poi clicca su `Imposta Password`.

![sparrow](assets/notext/16.webp)

### Ricevere bitcoin
Dopo aver creato il tuo portafoglio, inizialmente avrai un singolo account, con l'indice `0'`. Questo è l'account di **deposito** di cui abbiamo parlato nelle parti precedenti. Questo è l'account al quale dovrai inviare i bitcoin da mixare.
Per fare ciò, seleziona la scheda `Ricevi` sul lato sinistro della finestra. Sparrow genererà automaticamente un nuovo indirizzo vuoto per ricevere bitcoin.

![sparrow](assets/notext/17.webp)

Puoi inserire un'etichetta per questo indirizzo e poi inviare i bitcoin da mescolare ad esso.

![sparrow](assets/notext/18.webp)

### Creazione della Tx0
Una volta che la tua transazione è confermata, puoi poi andare alla scheda `UTXOs`.

![sparrow](assets/notext/19.webp)

Successivamente, scegli l'UTXO o gli UTXO che desideri sottoporre ai cicli di coinjoin. Per selezionare più UTXO contemporaneamente, tieni premuto il tasto `Ctrl` mentre clicchi sugli UTXO della tua scelta.

![sparrow](assets/notext/20.webp)

Poi clicca sul pulsante `Mix Selected` in fondo alla finestra. Se questo pulsante non appare sulla tua interfaccia, è perché sei su un portafoglio protetto con un portafoglio hardware. Devi usare un portafoglio software per eseguire coinjoin con Sparrow.
![sparrow](assets/notext/21.webp)
Si apre una finestra per spiegare come funziona Whirlpool. Questa è una semplificazione di quanto ho spiegato nelle parti precedenti. Clicca su `Avanti` per procedere.

![sparrow](assets/notext/22.webp)

Nella pagina successiva, puoi inserire uno "SCODE" se ne hai uno. Uno SCODE è un codice promozionale che offre uno sconto sulle commissioni di servizio della pool. Samourai Wallet fornisce occasionalmente tali codici ai suoi utenti durante eventi speciali. Ti consiglio di [seguire Samourai Wallet](https://twitter.com/SamouraiWallet) sui social media per non perdere i futuri SCODE.

Nella stessa pagina, dovrai anche impostare la commissione per la `Tx0` ed il tuo primo mix. Questa scelta influenzerà la velocità di conferma della tua transazione preparatoria e del tuo primo coinjoin. Ricorda che sei responsabile delle commissioni di mining per la `Tx0` e il mix iniziale, ma non dovrai pagare commissioni di mining per i remix successivi. Regola il cursore della `Priorità Premix` secondo le tue preferenze, poi clicca su `Avanti`.

![sparrow](assets/notext/23.webp)

In questa nuova finestra, dovrai selezionare la pool che desideri, usando l'elenco a discesa. Nel mio caso, avendo inizialmente selezionato un UTXO di `456 214 sats`, la mia unica scelta possibile è la pool di `100 000 sats`. Questa interfaccia ti informa anche sulle commissioni di servizio da pagare così come il numero di UTXO che saranno integrati nella pool. Se le condizioni ti sembrano soddisfacenti, continua cliccando su `Anteprima Premix`.

![sparrow](assets/notext/24.webp)

Dopo questo passaggio, Sparrow ti chiederà di inserire la password per il tuo portafoglio, quella che hai stabilito quando lo hai creato sul software. Una volta inserita la password, avrai accesso all'anteprima della tua `Tx0`. Sul lato sinistro della tua finestra, vedrai che Sparrow ha generato i diversi account necessari per utilizzare Whirlpool (`Deposito`, `Premix`, `Postmix` e `Badbank`). Avrai anche l'opportunità di visualizzare la struttura della tua `Tx0`, con i diversi output:
- Le commissioni di servizio;
- Gli UTXO equalizzati destinati ad entrare nella pool;
- Il cambio tossico (Doxxic Change).

![sparrow](assets/notext/25.webp)

Se la transazione è di tuo gradimento, clicca su `Broadcast Transaction` per trasmettere la `Tx0`. Altrimenti, hai l'opzione di regolare i parametri di questa `Tx0` selezionando `Clear` per cancellare i dati inseriti e iniziare il processo di creazione da capo.

### Esecuzione dei Coinjoin
Una volta pubblicata la Tx0, troverai i tuoi UTXO pronti per essere mixati nell'account `Premix`.
![sparrow](assets/notext/26.webp)

Una volta che la `Tx0` sarà confermata, i tuoi UTXO saranno registrati presso il coordinatore, e i mix iniziali partiranno automaticamente in successione.

![sparrow](assets/notext/27.webp)

Controllando l'account `Postmix`, osserverai gli UTXO risultanti dai mix iniziali. Questi UTXO rimarranno pronti per successivi remix, che non comporteranno costi aggiuntivi.

![sparrow](assets/notext/28.webp)

Nella colonna `Mixes`, è possibile vedere il numero di coinjoin eseguiti per ciascun UTXO. Come vedremo nelle sezioni seguenti, ciò che conta veramente non è tanto il numero di remix in sé, ma piuttosto gli anonset associati, anche se questi due indicatori sono parzialmente correlati.

![sparrow](assets/notext/29.webp)

Per fermare temporaneamente i coinjoin, basta cliccare su `Stop Mixing`. Avrai l'opzione di riprendere le operazioni in qualsiasi momento selezionando `Start Mixing`.

![sparrow](assets/notext/30.webp)

Per garantire la continua disponibilità dei tuoi UTXO per il remix, è necessario mantenere attivo il software Sparrow. Chiudere il software o spegnere il computer metterà in pausa i coinjoin. Una soluzione per aggirare questo problema è disabilitare le funzioni di sospensione tramite le impostazioni del sistema operativo. Inoltre, Sparrow offre un'opzione per impedire al computer di andare automaticamente in sospensione, che puoi trovare sotto la scheda `Tools` intitolata `Prevent Computer Sleep`.

![sparrow](assets/notext/31.webp)

### Completamento dei coinjoin
Per spendere i tuoi bitcoin mixati, hai diverse opzioni. Il metodo più diretto è accedere all'account `Postmix` e selezionare la scheda `Send`.

![sparrow](assets/notext/32.webp)

In questa sezione, dovrei inserire l'indirizzo di destinazione, l'importo da inviare e le commissioni di transazione, allo stesso modo di qualsiasi altra transazione effettuata con Sparrow Wallet. Se lo desideri, puoi anche sfruttare funzionalità avanzate per la privacy come Stonewall, cliccando sul pulsante `Privacy`.

![sparrow](assets/notext/33.webp)

[-> Scopri di più sulle transazioni Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Se desideri fare una selezione più precisa delle tue monete da spendere, vai alla scheda `UTXOs`. Seleziona gli UTXO che desideri consumare specificamente, quindi premi il pulsante `Send Selected` per avviare la transazione.

![sparrow](assets/notext/34.webp)
Infine, l'opzione `Mix to...` disponibile su Sparrow consente la rimozione automatica di un UTXO selezionato dai cicli di coinjoin, senza incorrere in commissioni aggiuntive. Questa funzionalità permette di determinare un numero di remix dopo i quali l'UTXO non verrà reintegrato nel tuo account `Postmix`, ma verrà invece trasferito direttamente in un altro portafoglio. Questa opzione è spesso utilizzata per inviare automaticamente bitcoin mixati a un cold wallet. Per utilizzare questa opzione, inizia aprendo il portafoglio destinatario insieme al tuo portafoglio coinjoin all'interno del software Sparrow.

![sparrow](assets/notext/35.webp)

Quindi, vai alla scheda `UTXOs`, poi clicca sul pulsante `Mix to...` in fondo alla finestra.

![sparrow](assets/notext/36.webp)

Si apre una finestra, inizia selezionando il portafoglio di destinazione dall'elenco a discesa.

![sparrow](assets/notext/37.webp)

Scegli la soglia di coinjoin oltre la quale il prelievo verrà effettuato automaticamente. Non posso darti un numero esatto di remix da eseguire, poiché varia in base alla tua situazione personale e ai tuoi obiettivi di privacy, ma evita di scegliere una soglia troppo bassa. Ti consiglio di consultare quest'altro articolo per saperne di più sul processo di remixing: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

Puoi lasciare l'opzione `Intervallo di indici` sul suo valore predefinito, `Completo`. Questa funzione consente il mixing simultaneo da client diversi, ma non è ciò che vogliamo fare in questo tutorial. Per finalizzare e attivare l'opzione `Mix to...`, premi `Riavvia Whirlpool`.

![sparrow](assets/notext/38.webp)

Tuttavia, fai attenzione quando utilizzi l'opzione `Mix to`, poiché rimuovere monete mixate dal tuo account `Postmix` può aumentare significativamente il rischio di compromettere la tua privacy. Le ragioni di questo potenziale sono dettagliate nelle sezioni seguenti.

## Come conoscere la qualità dei nostri cicli di coinjoin?
Affinché un coinjoin sia veramente efficace, è essenziale che presenti una buona omogeneità tra gli importi degli input e degli output. Questa uniformità amplifica il numero di possibili interpretazioni agli occhi di un osservatore esterno, aumentando così l'incertezza attorno alla transazione. Per quantificare questa incertezza generata da un coinjoin, si può ricorrere al calcolo dell'entropia della transazione. Per un'esplorazione approfondita di questi indicatori, ti rimando al tutorial: [CALCOLATORE BOLTZMANN](https://planb.network/it/tutorials/privacy/boltzmann-entropy). Il modello Whirlpool è riconosciuto come quello che porta la maggiore omogeneità nei coinjoins.
Successivamente, la performance di diversi cicli di coinjoin viene valutata in base alla dimensione dei gruppi in cui una moneta è nascosta. La dimensione di questi gruppi definisce ciò che viene chiamato gli anonsets. Esistono due tipi di anonsets: il primo valuta la privacy guadagnata contro l'analisi retrospettiva (dal presente al passato) e il secondo, contro l'analisi prospettica (dal passato al presente). Per una spiegazione dettagliata di questi due indicatori, ti invito a consultare il tutorial: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## Come gestire il postmix?
Dopo aver eseguito cicli di coinjoin, la strategia migliore è mantenere i tuoi UTXO nell'account **postmix**, in attesa del loro futuro utilizzo. È addirittura consigliabile lasciarli remixare all'infinito fino a quando non avrai bisogno di spenderli.
Alcuni utenti potrebbero considerare l'idea di trasferire i loro bitcoin mixari in un portafoglio protetto da un hardware wallet. Questo è possibile, ma è importante seguire meticolosamente le raccomandazioni di Samourai Wallet per non compromettere la riservatezza acquisita.
Unire UTXOs è l'errore più frequentemente commesso. È necessario evitare di combinare UTXOs mescolati con UTXOs non mescolati nella stessa transazione, al fine di evitare il CIOH (*Common-Input-Ownership-Heuristic*). Questo richiede una gestione attenta dei propri UTXOs all'interno del portafoglio, specialmente in termini di etichettatura. Oltre al coinjoin, unire UTXOs è generalmente una cattiva pratica che spesso porta a una perdita di privacy se non gestita correttamente.

È anche importante essere cauti nel consolidare UTXOs mixati tra loro. Consolidamenti moderati sono concepibili se i tuoi UTXOs mixati hanno anonset significativi, ma ciò diminuirà inevitabilmente la riservatezza dei tuoi UTXO. Assicurati che i consolidamenti non siano né troppo grandi né effettuati dopo un numero insufficiente di remix, poiché ciò rischia di stabilire collegamenti deducibili tra i tuoi UTXOs prima e dopo i cicli di coinjoin. In caso di dubbio su queste manipolazioni, la pratica migliore è non consolidare gli UTXOs postmix, e trasferirli uno per uno al tuo hardware wallet, generando un nuovo indirizzo vuoto ogni volta. Ancora, ricorda di etichettare correttamente ogni UTXO ricevuto.
Si sconsiglia anche di trasferire i tuoi UTXOs postmix in un portafoglio che utilizza script non comuni. Ad esempio, se entri in Whirlpool da un portafoglio multisig che utilizza script `P2WSH`, c'è poca possibilità che tu venga mescolato con altri utenti che hanno lo stesso tipo di portafoglio originariamente. Se ritiri i tuoi postmix in questo stesso portafoglio multisig, il livello di privacy dei tuoi bitcoin mescolati sarà notevolmente ridotto. Oltre agli script, ci sono molte altre impronte digitali del portafoglio che possono ingannarti.
Come per qualsiasi transazione Bitcoin, è anche importante non riutilizzare gli indirizzi di ricezione. Ogni nuova transazione dovrebbe essere ricevuta su un nuovo indirizzo vuoto.

La soluzione più semplice e sicura è lasciare riposare i tuoi UTXOs mescolati nel loro account **postmix**, permettendo loro di remixare e toccandoli solo per spendere. I portafogli Samourai e Sparrow hanno protezioni aggiuntive contro tutti questi rischi legati all'analisi della catena. Queste protezioni ti aiutano a evitare di fare errori.

## Come gestire il cambio tossico?
Successivamente, devi fare attenzione nella gestione del cambio tossico, il cambio che non ha potuto entrare nella piscina di coinjoin. Questi UTXOs tossici, risultanti dall'uso di Whirlpool, rappresentano un rischio per la tua privacy poiché stabiliscono un collegamento tra te e l'uso del coinjoin. Pertanto, è imperativo gestirli con cura e non combinarli con altri UTXOs, specialmente UTXOs mescolati. Ecco diverse strategie da considerare per utilizzarli:
- **Mescolali in piscine più piccole:** Se il tuo UTXO tossico è abbastanza significativo da entrare da solo in una piscina più piccola, considera di mescolarlo. Questa è spesso la migliore opzione. Tuttavia, è fondamentale non unire diversi UTXOs tossici per accedere a una piscina, poiché ciò potrebbe collegare le tue diverse entrate;
- **Segnali come "non spendibili":** Un altro approccio è non utilizzarli più, segnarli come "non spendibili" nel loro account dedicato e semplicemente Hodl. Questo assicura che non li spendi accidentalmente. Se il valore del bitcoin aumenta, potrebbero emergere nuove piscine più adatte ai tuoi UTXOs tossici.
- **Effettua donazioni:** Considera di fare donazioni, anche modeste, agli sviluppatori che lavorano su Bitcoin e il suo software associato. Puoi anche donare a organizzazioni che accettano BTC. Se gestire i tuoi UTXO tossici sembra troppo complicato, puoi semplicemente liberartene facendo una donazione;
- **Compra Carte Regalo:** Piattaforme come [Bitrefill](https://www.bitrefill.com/) ti permettono di scambiare bitcoin con carte regalo utilizzabili presso vari commercianti. Questo può essere un modo per disfarti dei tuoi UTXO tossici senza perdere il valore associato.
- **Consolidali su Monero:** Samourai Wallet offre ora un servizio di atomic swap tra BTC e XMR. Questo è ideale per gestire gli UTXO tossici consolidandoli su Monero, senza compromettere la tua privacy tramite il CIOH, prima di rimandarli a Bitcoin. Tuttavia, questa opzione può essere costosa in termini di commissioni di mining e del premio dovuto ai vincoli di liquidità.
- **Inviali su Lightning Network:** Trasferire questi UTXO su Lightning Network per beneficiare di commissioni di transazione ridotte è un'opzione che potrebbe essere interessante. Tuttavia, questo metodo potrebbe rivelare certe informazioni a seconda del tuo uso di Lightning e dovrebbe quindi essere praticato con cautela.

Tutorial dettagliati sull'implementazione di queste diverse tecniche saranno presto offerti su PlanB Network.

**Risorse Aggiuntive:**
[Tutorial Video di Sparrow Wallet](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)
[Tutorial Video di Samourai Wallet](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Documentazione di Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Thread su Twitter sui CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Post sul Blog sui CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).
