---
term: UNIX TIME
---

Unix Time o Timestamp Unix rappresenta il numero di secondi trascorsi dal 1 gennaio 1970, a mezzanotte UTC (Unix Epoch). Questo sistema è utilizzato nei sistemi operativi Unix e derivati per segnare il tempo in modo universale e standardizzato. Consente la sincronizzazione degli orologi e la gestione di eventi basati sul tempo, indipendentemente dai fusi orari.

Nel contesto di Bitcoin, viene utilizzato per l'orologio locale dei nodi, e quindi per il calcolo del NAT (Network-Adjusted Time). Il tempo adattato alla rete è una mediana dei tempi dei nodi calcolata localmente da ciascun nodo, e questo riferimento viene poi utilizzato per verificare la validità dei timestamp dei blocchi. Infatti, affinché un blocco sia accettato da un nodo, il suo timestamp deve essere compreso tra l'MTP (Median Time Past degli ultimi 11 blocchi minati) e il NAT più 2 ore:

```text
MTP < Timestamp Valido < (NAT + 2h)
```

Unix Time è utilizzato anche per stabilire i timelock quando si basano sul tempo reale, piuttosto che su un numero di blocchi.