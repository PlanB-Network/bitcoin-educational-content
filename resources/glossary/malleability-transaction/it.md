---
termine: MALLEABILITÀ (TRANSAZIONE)
---

Si riferisce alla capacità di modificare leggermente la struttura di una transazione Bitcoin, senza alterarne l'effetto, ma cambiando l'identificativo della transazione (*TXID*). Questa proprietà può essere sfruttata in modo malevolo per ingannare gli stakeholder riguardo allo stato di una transazione, causando così problemi come il doppio spesa. La malleabilità era resa possibile dalla flessibilità della firma digitale utilizzata. Il soft fork SegWit è stato introdotto appositamente per prevenire questa malleabilità delle transazioni Bitcoin, rendendo complicata l'implementazione della Lightning Network. Ciò viene ottenuto rimuovendo i dati malleabili dalla transazione dal calcolo del TXID.

> ► *Sebbene raro, il termine "mutabilità" è talvolta usato per riferirsi allo stesso concetto.*