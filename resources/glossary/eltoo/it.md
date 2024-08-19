---
termine: ELTOO
---

Un protocollo generale per i secondi strati di Bitcoin che definisce come gestire congiuntamente la proprietà di un UTXO. Eltoo è stato progettato da Christian Decker, Rusty Russell e Olaoluwa Osuntokun, in particolare per risolvere i problemi associati ai meccanismi di negoziazione degli stati dei canali Lightning, ovvero tra l'apertura e la chiusura. L'architettura Eltoo semplifica il processo di negoziazione introducendo un sistema di gestione degli stati lineare, sostituendo l'approccio basato sulle penalità stabilito con un metodo di aggiornamento più flessibile e meno punitivo. Questo protocollo richiede l'uso di un nuovo tipo di SigHash che permette di ignorare tutti gli input nella firma di una transazione. Questo SigHash è stato inizialmente chiamato `SIGHASH_NOINPUT`, poi `SIGHASH_ANYPREVOUT` (*Qualsiasi Output Precedente*). La sua implementazione è prevista nel BIP118.

> ► *Eltoo è talvolta anche riferito come "LN-Symmetry".*