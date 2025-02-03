---
term: ELTOO

---
Un protocollo generale per i secondi livelli di Bitcoin che definisce come gestire congiuntamente la proprietà di un UTXO. Eltoo è stato progettato da Christian Decker, Rusty Russell e Olaoluwa Osuntokun, in particolare per risolvere i problemi associati ai meccanismi di negoziazione degli stati del canale Lightning, cioè tra apertura e chiusura. L'architettura Eltoo semplifica il processo di negoziazione introducendo un sistema di gestione lineare degli stati, sostituendo l'approccio consolidato basato sulle penalità con un metodo di aggiornamento più flessibile e meno punitivo. Questo protocollo richiede l'uso di un nuovo tipo di SigHash che permette di ignorare tutti gli input nella firma di una transazione. Questo SigHash è stato inizialmente chiamato `SIGHASH_NOINPUT`, poi `SIGHASH_ANYPREVOUT` (*Qualsiasi uscita precedente*). La sua implementazione è prevista nel BIP118.

> *Eltoo è talvolta indicato anche come "simmetria LN"