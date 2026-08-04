---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normalmente, quando firmi una transazione, questa viene automaticamente trasmessa (broadcast) a tutti i nodi della rete Bitcoin. Poi attende di essere minata.

Tuttavia, finché non è inclusa in un blocco, un attaccante che sia entrato in possesso della tua chiave privata potrebbe sostituirla e rubare i fondi. Questo è tipicamente il caso se utilizzi un hardware wallet ColdCard.

Lo strumento Slipstream della società mineraria MARA ti permette di evitare la trasmissione della transazione sulla rete: viene inviata direttamente (e solo) a un miner, che la mantiene privata evitando di esporla sulla rete. La transazione impiegherà probabilmente più tempo per essere minata, ma sarà protetta da un attacco di sostituzione.

Di seguito proponiamo un tutorial che permette agli utenti di [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), così come agli utenti del wallet [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), di utilizzare lo strumento Slipstream del miner MARA tramite la pagina [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Attenzione**: questo strumento è pensato solo per determinati profili, principalmente wallet Liana, wallet miniscript e alcuni tipi di multisig. Wizardsardine **sconsiglia esplicitamente** il suo utilizzo per wallet i cui fondi sono già a rischio critico di furto, ad esempio quelli la cui recovery phrase è stata generata su un dispositivo ColdCard interessato dalla vulnerabilità del generatore di numeri casuali. In quella situazione, la corsa contro l'attaccante si gioca in pochi secondi, e una transazione inviata a un singolo miner impiega molto più tempo per essere confermata rispetto a una trasmessa normalmente. Se questo ti riguarda, leggi prima il nostro tutorial dedicato:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Per gli utenti di Liana

Liana è mantenuto da Wizardsardine, editore della pagina [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), quindi il percorso è diretto: ti basta esportare il file PSBT firmato invece di trasmetterlo.

*Prerequisito: avere fondi sul tuo wallet Liana.*

### Passo 1: crea la tua transazione con Liana

Come al solito, costruisci la tua transazione aggiungendo l'indirizzo di destinazione, la descrizione e l'importo (qui, il massimo disponibile nel wallet).

Per impostare il fee rate:

- seleziona le coin che vuoi spendere cliccando sul piccolo riquadro in basso a sinistra, sotto "Coins selection";
- poi inserisci il fee rate. Ricordati di impostare commissioni molto più alte rispetto al tasso suggerito, come descritto in questa pagina: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Infine, clicca su "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Passo 2: verifica i dettagli della tua transazione

Prima di cliccare su "Sign", verifica i dettagli della tua transazione; in particolare:

- l'importo inviato;
- il numero di satoshi destinati alle commissioni di transazione;
- ma soprattutto, l'indirizzo a cui stai inviando i fondi (ricordati di controllare i primi 5/6 caratteri, gli ultimi 5/6, e 5/6 caratteri al centro dell'indirizzo per evitare attacchi di "address poisoning").

![Checking the transaction details](assets/fr/02.webp)

### Passo 3: seleziona i wallet di firma

Successivamente, seleziona i wallet software e/o hardware con cui devi firmare la tua transazione. Un rapido promemoria: nel caso di un wallet multisig 2-of-2, servono 2 firme su 2.

### Passo 4: esporta il file PSBT della tua transazione

La transazione Bitcoin è ora firmata dalle chiavi appropriate. Non cliccare su "Broadcast", altrimenti verrà condivisa con l'intera rete e, se utilizzi un hardware wallet ColdCard, la tua transazione sarà pubblicamente esposta e i tuoi fondi saranno a rischio.

Ora puoi cliccare su "Export", poi salvare il file PSBT localmente sul tuo computer.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Passo 5: invia la transazione al miner tramite outofband.wizardsardine.com

Ora per i passaggi finali. Per inviare la transazione al miner, non devi fare altro che prendere il file PSBT e trascinarlo nell'area designata.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

La transazione viene quindi visualizzata come mostrato di seguito.

![Transaction in the queue](assets/fr/05.webp)

### Passo 6: invia la transazione tramite Slipstream

Infine, non devi fare altro che cliccare su "Send" affinché la transazione venga inviata a MARA tramite Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Nel giro di pochi secondi, la transazione passa quindi da "Sending" ad "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Non resta che copiare l'identificatore della transazione (TXID), poi incollarlo su [mempool.space](https://mempool.space/) per osservarne il mining:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Nota bene: la transazione risulterà come "Transaction not found" finché il miner, MARA, non minerà un blocco includendo la tua transazione al suo interno. Questo può richiedere diverse decine di minuti, o anche ore, poiché MARA detiene solo circa il 4,5% dell'hash rate della rete Bitcoin. Al 4 agosto 2026, questo corrisponde a circa un blocco minato ogni 3 ore e 45 minuti.

## Per gli utenti di altri wallet

Se non utilizzi [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) ma vuoi comunque utilizzare lo strumento, ecco un tutorial che utilizza un wallet multisig 2-of-2. Per fare ciò, utilizzeremo il wallet software [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Prerequisito: avere fondi sul tuo wallet Sparrow.*

### Passo 1: crea la tua transazione

Con [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), crea la transazione sul tuo wallet multisig. Ricordati di impostare commissioni molto più alte rispetto al tasso suggerito, come descritto in questa pagina: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Una volta creata, clicca su "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Passo 2: finalizza la tua transazione

Per finalizzare la tua transazione, ora devi firmarla. Per fare ciò, clicca su "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Passo 3: firma la tua transazione con le tue diverse chiavi

Ora arriva il momento di firmare la transazione. Per fare ciò, ti basta firmarla con il wallet o i wallet software o hardware che utilizzi.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Passo 4: scarica la transazione firmata, e non trasmetterla alla rete

La transazione Bitcoin è ora firmata da entrambe le chiavi del nostro multisig 2-of-2. Non cliccare su "Broadcast Transaction", altrimenti verrà condivisa con l'intera rete e, se utilizzi un hardware wallet ColdCard, la tua transazione sarà pubblicamente esposta e i tuoi fondi saranno a rischio.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Passo 5: visualizza lo script della transazione firmata, o scarica il file PSBT

Per visualizzare la transazione Bitcoin firmata, clicca ora su "View Final Transaction". Puoi quindi copiare lo script della transazione Bitcoin firmata:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Se vuoi scaricare il file della transazione, puoi:

- cliccare su "File", poi su "Save transaction…";
- oppure cliccare sul pulsante di connessione di rete in basso a destra (pulsante giallo), poi cliccare su "Save Final Transaction".

La transazione verrà quindi salvata localmente sul tuo computer.

![Saving the final transaction locally](assets/fr/14.webp)

### Passo 6: invia la transazione al miner tramite outofband.wizardsardine.com

Ora per i passaggi finali. Per inviare la transazione al miner, non devi fare altro che:

- andare su [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- incollare lo script della transazione firmata copiato nel passaggio precedente, poi cliccare su "ADD TO QUEUE" qui sotto;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- oppure prendere il file e trascinarlo nell'area designata.

![Dropping the transaction file on the tool](assets/fr/16.webp)

La transazione viene quindi visualizzata come mostrato di seguito.

![Transaction in the queue](assets/fr/17.webp)

Se un messaggio ti avvisa che l'importo totale in ingresso in satoshi della tua transazione è sconosciuto (e che, di conseguenza, il numero di satoshi per le commissioni non può essere calcolato), devi semplicemente inserire manualmente l'importo totale in ingresso in satoshi. Per trovarlo, clicca semplicemente sulla visualizzazione della tua transazione in Sparrow, al centro del diagramma:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Poi inserisci quell'importo (15.904 sats nel nostro esempio) nello strumento [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Infine, verifica che il fee rate sia corretto.

### Passo 7: invia la transazione tramite Slipstream

Infine, non devi fare altro che cliccare su "Send" affinché la transazione venga inviata a MARA tramite Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Nel giro di pochi secondi, la transazione passa quindi da "Sending" ad "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Non resta che copiare l'identificatore della transazione (TXID), poi incollarlo su [mempool.space](https://mempool.space/) per osservarne il mining:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Nota bene: la transazione risulterà come "Transaction not found" finché il miner, MARA, non minerà un blocco includendo la tua transazione al suo interno. Questo può richiedere diverse decine di minuti, o anche ore, poiché MARA detiene solo circa il 4,5% dell'hash rate della rete Bitcoin. Al 4 agosto 2026, questo corrisponde a circa un blocco minato ogni 3 ore e 45 minuti.
