---
term: MALLEABILITÀ (TRANSAZIONE)

---
Si riferisce alla capacità di modificare leggermente la struttura di una transazione Bitcoin, senza alterarne l'effetto, ma cambiando l'identificativo della transazione (*TXID*). Questa proprietà può essere sfruttata in modo malevolo per ingannare le parti interessate sullo stato di una transazione, causando così problemi come la doppia spesa. La malleabilità è stata resa possibile dalla flessibilità della firma digitale utilizzata. Il soft fork SegWit è stato introdotto in particolare per prevenire questa malleabilità delle transazioni Bitcoin, rendendo complicata l'implementazione della Lightning Network. Questo obiettivo viene raggiunto rimuovendo i dati malleabili della transazione dal calcolo del TXID.

> *Anche se raramente, il termine "mutabilità" è talvolta usato per riferirsi allo stesso concetto