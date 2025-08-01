---
name: JoinBot
description: Comprendere e utilizzare JoinBot
---

![DALL·E – samurai robot in a red forest, 3D render](assets/cover.webp)

***ATTENZIONE:** In seguito all'arresto dei fondatori di Samourai Wallet e al sequestro dei loro server il 24 aprile 2024, il servizio JoinBot non è più disponibile. Attualmente, non è più possibile utilizzare questo strumento. Tuttavia, è ancora possibile eseguire Stonewall X2, a condizione di trovare un collaboratore e scambiare manualmente i PSBT. Il servizio potrebbe essere riattivato prossimamente, a seconda dell'evoluzione del caso.*

_Stiamo monitorando attentamente la situazione e gli sviluppi legati agli strumenti associati. Questo tutorial verrà aggiornato non appena saranno disponibili nuove informazioni._

_Questo tutorial è fornito esclusivamente a scopo educativo e informativo. Non approviamo né incoraggiamo l'utilizzo di questi strumenti per finalità illecite. È responsabilità di ciascun utente rispettare le leggi vigenti nella propria giurisdizione._

---

JoinBot è un nuovo strumento introdotto nella suite di Samourai Wallet con l’ultimo aggiornamento 0.99.98f del noto software wallet per Bitcoin. 
Permette di eseguire facilmente una transazione collaborativa per ottimizzare la privacy, senza dover trovare un partner. Questo semplifica l'utilizzo di tecniche avanzate di offuscamento come StonewallX2, rendendole accessibili anche agli utenti meno esperti.

*Un ringraziamento al fantastico Fanis Michalakis per l'idea di utilizzare DALL-E per la miniatura!*

## Che cosa si intende per transazione collaborativa su Bitcoin?

Bitcoin si basa su un registro distribuito e trasparente. Chiunque può tracciare le transazioni degli utenti all'interno di questo sistema di denaro elettronico. Per preservare un buon livello di privacy, un utente Bitcoin può costruire una transazione in modo da permettere diverse interpretazioni plausibili, rendendo difficile stabilire con certezza il collegamento tra input e output.

L'obiettivo non è nascondere direttamente le informazioni, ma confonderle tra molteplici possibilità. Questa strategia viene usata soprattutto nelle transazioni CoinJoin, che aiutano a interrompere la tracciabilità della storia di un UTXO e a rendere più difficile capire come si muovono i fondi. Per raggiungere questo scopo, la transazione viene costruita con più input e output dello stesso importo.

Ogni transazione Bitcoin "brucia" i suoi input per generare nuovi output, modificando le condizioni di spesa degli UTXO. Questo è il meccanismo fondamentale con cui i bitcoin vengono trasferiti tra utenti.
(Ne parlo più nel dettaglio nell' articolo: Meccanismo di una transazione Bitcoin: UTXO, input e output).

Una delle modalità per offuscare le tracce all'interno di una transazione è ricorrere a una transazione collaborativa. Come suggerisce il nome, si tratta di un accordo tra più utenti, ciascuno dei quali partecipa con un input e riceve un output nella stessa transazione.

Come accennato, la forma più conosciuta di transazione collaborativa è il Coinjoin. Ad esempio, nel coinjoin del protocollo Whirlpool, ogni transazione coinvolge 5 partecipanti, ognuno con input e output di pari importo.

![Schema di una transazione Coinjoin su Whirlpool](assets/1.webp)

Un osservatore esterno non sarà in grado di stabilire con certezza quale output sia associato a ogni utente che ha fornito un input nella transazione. Ad esempio, considerando l’utente n.°4 (colore viola), possiamo identificare il suo UTXO in input, ma non possiamo sapere quale dei 5 output sia effettivamente il suo. L’informazione non viene nascosta, bensì confusa all’interno di un insieme.
L’utente può quindi negare di possedere un determinato UTXO in output: questo fenomeno è noto come "plausible deniability" (negabilità plausibile) e rappresenta un efficace meccanismo di privacy in un sistema altrimenti trasparente come Bitcoin.

Per saperne di più sul funzionamento di Coinjoin, ti spiego tutto in questo articolo: Comprendere e utilizzare CoinJoin su Bitcoin.

Sebbene il Coinjoin sia molto efficace nel rendere irrintracciabile la cronologia di un UTXO, non è adatto per spendere direttamente i bitcoin. La sua struttura, infatti, richiede input e output di importi predefiniti e identici (al netto delle commissioni di mining).
Tuttavia, la fase di spesa è un momento critico per la privacy: spesso crea un collegamento diretto tra l’identità dell’utente e l’attività visibile sulla blockchain. Per questo motivo è fondamentale usare strumenti di privacy anche durante i pagamenti.
Esistono infatti altre tipologie di transazioni collaborative progettate appositamente per proteggere la privacy al momento della spesa.

## La transazione StonewallX2

Tra le varie modalità di spesa offerte da Samourai Wallet, troviamo la transazione collaborativa StonewallX2. Si tratta di un mini Coinjoin tra due utenti, pensato appositamente per i pagamenti. Per un osservatore esterno, questa transazione genera diverse interpretazioni possibili. Parliamo dunque di "plausible deniability" e, di conseguenza, di maggiore privacy per l’utente.

Questa configurazione collaborativa è disponibile sia su Samourai Wallet sia su Sparrow Wallet, garantendo interoperabilità tra i due software.

Il meccanismo è piuttosto semplice da comprendere. Ecco come funziona in pratica:

- Un utente desidera effettuare un pagamento in bitcoin (ad esempio, presso un commerciante).
- Ottiene l’indirizzo di ricezione del destinatario effettivo (il commerciante).
- Costruisce una transazione con più input: almeno uno di sua proprietà e uno appartenente a un collaboratore esterno.
- La transazione avrà 4 output, di cui 2 dello stesso importo: uno all’indirizzo del commerciante per il pagamento, uno di resto che torna all’utente, un output dello stesso valore del pagamento che va al collaboratore, e un altro output di resto per il collaboratore.

Ad esempio, ecco una tipica transazione StonewallX2 in cui ho effettuato un pagamento di 50.125 sats. Il primo input, pari a 102.588 sats, proviene dal mio portafoglio Samourai. Il secondo input, di 104.255 sats, proviene dal portafoglio del mio collaboratore:


![Schema di una transazione StonewallX2](assets/2.webp)

Possiamo osservare 4 output di cui 2 dello stesso importo per confondere le tracce:

- `50.125` sats che vanno al destinatario effettivo del mio pagamento.
- `52.306` sats che rappresentano il mio resto e quindi tornano a un indirizzo del mio portafoglio.
- `50.125` sats che tornano al mio collaboratore.
- `53 973` sats che tornano ancora al mio collaboratore.

Alla fine dell’operazione, il collaboratore recupera l’intero saldo iniziale (al netto delle commissioni di mining), mentre l’utente avrà effettuato il pagamento al commerciante. Questo tipo di transazione introduce un’elevata entropia, rompendo i collegamenti diretti e evidenti tra il mittente e il destinatario, migliorando così significativamente la privacy.
   
La forza della transazione StonewallX2 sta nel fatto che contrasta una delle regole principali usate dagli analisti della blockchain: l’ipotesi che gli input di una transazione con più input appartengano tutti allo stesso proprietario. In altre parole, in una normale transazione Bitcoin con più input, si presume che appartengano tutti ad un unico utente.
Questo crea un rischio per la privacy, già evidenziato da Satoshi Nakamoto nel suo white paper originale:

> Come ulteriore livello di protezione, si può usare una nuova coppia di chiavi per ogni transazione, in modo da evitare che vengano collegate a un unico proprietario. Tuttavia, il collegamento è inevitabile nelle transazioni con più input, perché queste mostrano necessariamente che gli input appartengono allo stesso proprietario.

Questa è solo una delle tante regole empiriche usate nell’analisi on-chain per creare gruppi di indirizzi collegati tra loro. Se vuoi saperne di più su queste euristiche, ti consiglio questa serie di quattro articoli pubblicata da Samourai Wallet: un’introduzione completa e facile da capire sull’argomento.

La forza della transazione StonewallX2 sta proprio nel mettere in crisi l’euristica della proprietà comune degli input. Un osservatore esterno, infatti, tende a pensare che tutti gli input di una transazione appartengano allo stesso utente. Nel caso di StonewallX2, invece, due persone diverse collaborano volontariamente per creare la transazione. L’analisi del pagamento è dunque deviata, preservando la privacy dell’utente.

Per un osservatore, una transazione StonewallX2 non si distingue da una Stonewall. L’unica differenza reale è che Stonewall non è collaborativa: usa solo gli UTXO di un singolo utente. Tuttavia, nella loro struttura on-chain, Stonewall e StonewallX2 sono identiche. Questo permette molte più interpretazioni della transazione, perché un osservatore esterno non può capire se gli input provengono dalla stessa persona o da due collaboratori.

Il vantaggio di StonewallX2 rispetto a un PayJoin di tipo Stowaway è che può essere usato in qualsiasi situazione. Il vero destinatario del pagamento non contribuisce con input alla transazione. Perciò, una StonewallX2 può essere usata per pagare qualsiasi commerciante che accetta Bitcoin, anche se non usa Samourai o Sparrow.
Di contro, lo svantaggio principale è che serve un collaboratore disposto a usare i propri bitcoin per partecipare al tuo pagamento. Se hai amici con bitcoin disposti ad aiutarti in qualsiasi momento, non è un problema, ma se non conosci altri utenti Samourai Wallet o nessuno è disponibile a collaborare, allora rimani bloccato.

Per risolvere questo limite, Samourai ha introdotto una nuova funzione nell'applicazione: JoinBot.

# Che cos'è JoinBot?

Il principio alla base di JoinBot è semplice: se non riesci a trovare un collaboratore per una transazione StonewallX2, puoi collaborare direttamente con Samourai Wallet.

Questo servizio è particolarmente comodo, soprattutto per chi è alle prime armi, poiché è disponibile 24 ore su 24, 7 giorni su 7. Se devi fare un pagamento urgente e vuoi usare StonewallX2, non devi più contattare un amico o cercare un collaboratore online. Ci pensa JoinBot ad aiutarti.

Un altro vantaggio di JoinBot è che gli UTXO che usa come input provengono esclusivamente da postmix Whirlpool, migliorando la privacy del tuo pagamento. Inoltre, dato che JoinBot è sempre online, dovresti collaborare solo con UTXO che hanno grandi Anonset potenziali.

Ovviamente, JoinBot presenta alcuni compromessi che vale la pena sottolineare:

- Come in una classica transazione StonewallX2, il tuo collaboratore conosce necessariamente gli UTXO usati e la loro destinazione. Nel caso di JoinBot, Samourai conosce i dettagli di questa transazione. Non è detto che sia un problema, ma è importante esserne consapevoli.
- Per evitare spam, Samourai applica una commissione di servizio del 3,5% sull’importo reale della transazione, con un limite massimo di 0,01 BTC. Per esempio, se invii un pagamento reale di 100.000 sats con JoinBot, la commissione sarà di 3.500 sats
- Per utilizzare JoinBot, è necessario avere almeno due UTXO non collegati (non devono condividere uno stesso TxID) disponibili nel proprio wallet.
- In un classico StonewallX2, i costi di mining vengono suddivisi equamente tra i due collaboratori. Con JoinBot, dovrete ovviamente pagare l'intera tariffa di mining.
- Per fare in modo che una transazione JoinBot sia esattamente uguale a una StonewallX2 o Stonewall classica, il pagamento della commissione di servizio avviene tramite una transazione separata. Il rimborso di metà delle commissioni di mining pagate inizialmente da Samourai avviene durante questa seconda transazione.
Per ottimizzare la tua privacy, il pagamento delle commissioni avviene con una transazione strutturata come un PayJoin di tipo Stowaway.

## Come utilizzare JoinBot?

Per effettuare una transazione con JoinBot, è necessario utilizzare Samourai Wallet. Puoi scaricarlo direttamente dal sito ufficiale oppure tramite Google Play Store.

A differenza di altri strumenti sviluppati dal team di Samourai, JoinBot non è ancora disponibile su Sparrow Wallet. Al momento, questo strumento è utilizzabile esclusivamente tramite Samourai.

Scopri passo dopo passo come effettuare una transazione StonewallX2 con JoinBot in questo video:


![Come utilizzare Joinbot](https://youtu.be/80MoMz2Ne5g)

Ecco lo schema della transazione appena effettuata nel video:

![Schema della mia transazione StonewallX2 con JoinBot.](assets/3.webp)

Possiamo notare 5 input:

- 3 input di 100 kilosat provenienti da Samourai (JoinBot).
- 2 input provenienti dal mio wallet personale, di 3.524 sat e 1,8 megasat.

I 4 output della transazione sono:

- 1 di 212.452 sat verso il destinatario effettivo del mio pagamento.
- 1 altro dello stesso importo che ritorna a un indirizzo di Samourai.
- 1 resto che ritorna ancora a Samourai per 87.302 sat. Questo rappresenta la differenza tra il totale dei loro input (300.000 sat) e l'output di offuscamento (212.452 sat) meno le commissioni di mining.
- 1 resto che ritorna a un altro indirizzo del mio wallet. Rappresenta la differenza tra il totale dei miei input e il pagamento effettivo, meno le commissioni di mining.

Promemoria: le commissioni di mining non sono un output esplicito della transazione. Rappresentano semplicemente la differenza tra la somma totale degli input e quella degli output.

## Conclusioni

JoinBot è uno strumento aggiuntivo che offre più scelte e libertà agli utenti Samourai. Permette di fare una transazione collaborativa StonewallX2 direttamente con Samourai come collaboratore migliorando la privacy dell’utente.

Se puoi fare una StonewallX2 classica con un amico, ti consiglio comunque di usare questo metodo. Ma se sei bloccato e non riesci a trovare collaboratori per effettuare un pagamento, puoi contare su JoinBot, disponibile 24 ore su 24, 7 giorni su 7, per collaborare con te.

**Risorse esterne:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin
