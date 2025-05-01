---
term: COINSWAP
---

Protocollo per il trasferimento segreto di Ownership tra utenti. Questo metodo mira a trasferire il possesso di bitcoin da una persona all'altra, e viceversa, senza che questo Exchange sia esplicitamente visibile sul Blockchain. Coinwap utilizza contratti intelligenti per effettuare il trasferimento senza bisogno di fiducia tra le parti.


Immaginiamo un esempio ingenuo (che non funziona) con Alice e Bob. Alice possiede 1 BTC protetto con la chiave privata $A$ e anche Bob possiede 1 BTC protetto con la chiave privata $B$. In teoria, i due potrebbero comunicare le loro chiavi private tramite un canale di comunicazione esterno per effettuare un trasferimento segreto. Tuttavia, questo metodo ingenuo presenta un rischio elevato in termini di fiducia. Nulla impedisce ad Alice di conservare una copia della chiave privata di $A$ dopo il Exchange e di usarla successivamente per rubare i bitcoin, una volta che la chiave è nelle mani di Bob. Inoltre, non c'è alcuna garanzia che Alice non riceva la chiave privata $B$ di Bob e non trasmetta mai la sua chiave privata $A$ nel Exchange. Questo Exchange si basa quindi su un'eccessiva fiducia tra le parti ed è inefficace nel garantire un trasferimento sicuro e segreto del Ownership.


Per risolvere questi problemi e consentire lo scambio di monete tra parti che non si fidano l'una dell'altra, utilizzeremo sistemi Smart contract che rendono il Exchange "atomico". Questi possono essere HTLC (*Contratti bloccati nel tempo Hash*) o PTLC (*Contratti bloccati nel tempo Point*). Questi due protocolli funzionano in modo simile, utilizzando un sistema di blocco temporale che garantisce che il Exchange sia completato con successo o completamente annullato, proteggendo così l'integrità dei fondi di entrambe le parti. La differenza principale tra HTLC e PTLC è che HTLC utilizza hash e preimmagini per proteggere la transazione, mentre PTLC utilizza le firme degli adattatori.


In uno scenario di scambio di monete con un HTLC o un PTLC tra Alice e Bob, il Exchange avviene in modo sicuro: o ha successo e ciascuno riceve il BTC dell'altro, o fallisce e ciascuno conserva il proprio BTC. In questo modo è impossibile per una delle due parti imbrogliare o rubare il BTC dell'altra.


L'uso delle firme adattatore è particolarmente interessante in questo contesto, in quanto consente di rinunciare agli script tradizionali (un meccanismo talvolta definito "script senza script"). In questo modo si riducono i costi associati al Exchange. Un altro grande vantaggio delle firme adattatore è che non richiedono l'uso di un Hash comune per entrambe le parti della transazione, evitando così la necessità di rivelare un collegamento diretto tra di esse in alcuni tipi di Exchange.