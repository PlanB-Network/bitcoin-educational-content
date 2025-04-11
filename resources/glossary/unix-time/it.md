---
term: TEMPO UNIX

---
Il tempo Unix o Unix Timestamp rappresenta il numero di secondi trascorsi dal 1° gennaio 1970, alla mezzanotte UTC (Unix Epoch). Questo sistema è utilizzato nei sistemi operativi Unix e derivati per scandire il tempo in modo universale e standardizzato. Consente la sincronizzazione degli orologi e la gestione di eventi basati sul tempo, indipendentemente dai fusi orari.

Nel contesto di Bitcoin, viene utilizzato per l'orologio locale dei nodi e quindi per il calcolo del NAT (Network-Adjusted Time). Il tempo aggiustato per la rete è una mediana dei tempi dei nodi calcolati localmente da ciascun nodo, e questo riferimento viene utilizzato per verificare la validità dei timestamp dei blocchi. Infatti, affinché un blocco venga accettato da un nodo, il suo timestamp deve essere compreso tra l'MTP (Median Time Past degli ultimi 11 blocchi estratti) e il NAT più 2 ore:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time viene utilizzato anche per stabilire i timelocks quando sono basati sul tempo reale, piuttosto che su un numero di blocchi.