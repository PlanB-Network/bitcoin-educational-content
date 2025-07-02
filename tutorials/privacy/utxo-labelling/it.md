---
name: UTXO Labelling
description: Come etichettare correttamente i tuoi UTXO
---
![cover](assets/cover.webp)

In questo tutorial affronteremo tutto ciò che devi sapere sulla cosiddetta "UTXO labelling" nel tuo wallet Bitcoin e sulla gestione degli stessi. Inizieremo con una parte teorica per comprendere appieno questi concetti, prima di passare a una sezione pratica in cui esploreremo come utilizzare concretamente le etichette nei principali wallet Bitcoin.

## Cos'è il Labelling degli UTXO?

Il "Labelling" è una tecnica che permette di aggiungere un’annotazione, o etichetta, a uno specifico UTXO all’interno del proprio wallet Bitcoin. Queste etichette vengono salvate localmente dal software e non sono mai trasmesse sulla rete Bitcoin. Si tratta quindi di uno strumento privato di organizzazione personale.

Ad esempio, se ricevo un UTXO da una transazione P2P effettuata su Bisq con Charles, potrei etichettarlo come Acquisto P2P Bisq con Charles.

Assegnare delle etichette agli UTXO permette di ricordarne facilmente l’origine o l’utilizzo previsto, facilitando la gestione dei fondi e migliorando la propria privacy. Questa pratica diventa ancora più efficace quando viene affiancata alla funzione di ["coin control"](https://planb.network/resources/glossary/coin-control), peculiarità offerta da molti wallet avanzati, e che permette all’utente di scegliere manualmente quali UTXO utilizzare come input in una determinata transazione.

L’uso combinato di etichetta e coin control consente di distinguere con precisione le fonti da cui provengono i fondi, evitando di mescolare UTXO provenienti da contesti diversi. Ciò aiuta a ridurre i rischi legati all’euristica che analizza le proprietà in comune tra gli input (in inglese: Common Input Ownership Heuristic (CIOH)), secondo cui gli input di una transazione sono probabilmente controllati dallo stesso utente, ipotesi che può compromettere seriamente la privacy.

Riprendendo l’esempio di prima: supponiamo di aver ricevuto un UTXO no-KYC tramite Bisq. Vorrei evitare di combinarlo con un UTXO ottenuto, ad esempio, da un exchange centralizzato che richiede la verifica dell’identità (KYC). Assegnando delle etichette distinte a ciascun UTXO, una per l’UTXO no-KYC e un’altra per quello KYC, posso identificarli facilmente e scegliere consapevolmente quale usare per un determinato acquisto, grazie alla funzionalità di coin control.


## Come etichettare correttamente gli UTXO?

Non esiste un metodo universale per etichettare adeguatamente gli UTXO. Sta a te definire un sistema di labelling che ti aiuti a orientarti facilmente nel tuo wallet.
Un criterio fondamentale nel labelling è la provenienza dell'UTXO. Dovresti semplicemente indicare come questo UTXO è arrivato nel tuo wallet. Proviene da un'exchange? Dal pagamento di una fattura da parte di un cliente? Da uno scambio peer-to-peer? O rappresenta il resto di un acquisto? Così, potresti specificare:

- "Prelievo Exchange.com";
- "Pagamento Cliente David";
- "Acquisto P2P Charles";
- "Resto dall'acquisto del divano".
- 
![labelling](assets/it/1.webp)

Per gestire meglio i tuoi UTXO e organizzare in modo più efficiente i fondi nel wallet, puoi aggiungere alle etichette un indicatore che ne evidenzi la funzione. Se hai UTXO destinati a usi diversi e preferisci non mescolarli, puoi includere un identificatore per distinguerli facilmente.

Questi indicatori dipenderanno dai tuoi criteri, come la distinzione tra UTXO KYC (associati alla tua identità) e no-KYC (anonimi), o tra fondi professionali e personali. Riprendendo gli esempi delle etichette precedentemente menzionate:

- "KYC - Prelievo Exchange.com";
- "KYC - Pagamento Cliente David";
- "NO KYC - Acquisto P2P Charles";
- "NO KYC - Resto dall'acquisto del divano".

In ogni caso, tieni presente che un'etichetta valida è quella che saraiin grado di comprendere quando ne avrai bisogno. Se il wallet è principalmente destinato al tenere i fondi di risparmio, potrebbe essere che le etichette siano utili solo tra diversi anni. Assicurati dunque che siano chiare, precise e complete.

È inoltre consigliabile mantenere l'identificatore di un UTXO attraverso le transazioni. Ad esempio, durante un consolidamento di UTXO no-KYC, assicuratevi di contrassegnare l'UTXO risultante non solo come "consolidamento", ma specificamente come "consolidamento no-KYC" per mantenere una traccia chiara dell'origine dell'UTXO.

Infine, non è necessario apporre la data su un'etichetta. La maggior parte dei wallet mostra già la data della transazione, ed è sempre possibile recuperare queste informazioni con un block explorer utilizzando il suo TXID (ID della transazione).

## Tutorial: il labelling su Specter Desktop

Su Specter Desktop, nella schermata principale del tuo wallet, seleziona la scheda "Addresses".

Qui vedrai l’elenco di tutti i tuoi indirizzi, con gli eventuali bitcoin ad essi associati. Di default, gli indirizzi sono identificati dall’indice numerico visualizzato nella colonna "Label". Per modificare un’etichetta:

Clicca sull’etichetta corrente.
Inserisci la nuova etichetta desiderata.
Conferma cliccando sull’icona blu.

L’etichetta apparirà subito nell’elenco.

Puoi anche assegnare un’etichetta in anticipo, quando condividi un indirizzo di ricezione. Per farlo, vai nella scheda "Receive" e inserisci l’etichetta nell’apposito campo prima di generare o condividere l’indirizzo.

## Tutorial: il Labelling su Electrum

Su Electrum, dopo aver effettuato l’accesso, vai nella scheda "History" e clicca sulla transazione a cui vuoi assegnare un’etichetta.

Si aprirà una finestra: clicca sulla casella "Description" e digita l’etichetta desiderata.

Una volta inserita l’etichetta, chiudi la finestra: la modifica verrà salvata automaticamente.

Troverai la tua etichetta associata alla transazione nella colonna "Description" della scheda "History".

Nella scheda "Coins", dove puoi eseguire il controllo degli UTXO, l’etichetta è visualizzata nella colonna "Label".

## Tutorial: Il Labelling su Green Wallet

Nell'app di Green, accedi al tuo wallet e seleziona la transazione che vuoi etichettare. Clicca ora sulla piccola icona della matita per annotare la tua etichetta.

Digita la tua etichetta, poi clicca sul pulsante verde "Save".

Sarai in grado di trovare la tua etichetta sia nei dettagli della transazione che nella schermata principale del tuo wallet.

## Tutorial: Il Labelling su Samourai Wallet

Su Samourai, esistono diversi metodi per assegnare un’etichetta a una transazione.

Il primo metodo consiste nell'aprire il tuo wallet e selezionare la transazione a cui desideri aggiungere un’etichetta. Poi premi il pulsante "Add", situato accanto alla casella "Notes".

Digita la tua etichetta e conferma cliccando sul pulsante blu "Add".

![etichetta](assets/notext/16.webp)

Troverai l’etichetta sia nei dettagli della transazione, sia nella pagina principale del tuo wallet.

![etichetta](assets/notext/17.webp)

Per il secondo metodo, tocca i tre puntini in alto a destra dello schermo, quindi seleziona dal menu l’opzione "Show Unspent Transaction Outputs".

![etichetta](assets/notext/18.webp)

Qui troverai un elenco completo di tutti gli UTXO presenti nel tuo wallet. L’elenco mostrato si riferisce al conto deposito, ma la stessa procedura si applica anche agli account Whirlpool, selezionandoli dal menu dedicato.

Seleziona l’UTXO che desideri etichettare, quindi premi il pulsante "Aggiungi".

![etichetta](assets/notext/19.webp)

Inserisci la tua etichetta e conferma cliccando sul pulsante blu "Add". Troverai quindi l’etichetta sia nei dettagli della transazione che nella pagina principale del tuo wallet.

![etichetta](assets/notext/20.webp)

## Tutorial: il Labelling su Sparrow Wallet

Con il software **Sparrow Wallet**, è possibile assegnare etichette in diversi modi.

Il metodo più semplice è aggiungere un’etichetta in anticipo, quando si comunica un indirizzo di ricezione al mittente. Per farlo, nella scheda "Receive", clicca sul campo "Label" e inserisci l’etichetta desiderata. Questa verrà salvata e sarà visibile in tutto il software non appena i bitcoin verranno ricevuti su quell’indirizzo.

![etichetta](assets/notext/21.webp)

Se hai dimenticato di etichettare l’indirizzo al momento della ricezione, puoi aggiungerne una successivamente tramite la scheda "Transactions". Clicca semplicemente sulla tua transazione all’interno della colonna "Label", poi inserisci l’etichetta desiderata.

![etichetta](assets/notext/22.webp)

Hai anche la possibilità di aggiungere o modificare le etichette dalla scheda "Indirizzi".

![etichetta](assets/notext/23.webp)

Infine, puoi visualizzare le tue etichette anche nella scheda "UTXO". **Sparrow Wallet** aggiunge automaticamente tra parentesi, dopo la tua etichetta, l'origine dell’output. Ciò aiuta a distinguere gli UTXO ricevuti direttamente da quelli di resto.

![etichetta](assets/notext/24.webp)
