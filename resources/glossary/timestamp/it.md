---
term: ORODATAGGIO
---

Il timestamping, o "Timestamp" in inglese, è un meccanismo che consente di associare un segno temporale preciso a un evento, a un dato o a un messaggio. Nel contesto generale dei sistemi informatici, il timestamping viene utilizzato per determinare l'ordine cronologico delle operazioni e per verificare l'integrità dei dati nel tempo.


Nel caso specifico del Bitcoin, i timestamp vengono utilizzati per stabilire la cronologia delle transazioni e dei blocchi. Ogni blocco in Blockchain contiene un Timestamp che indica l'ora approssimativa della sua creazione. Nel suo Libro Bianco, Satoshi Nakamoto parla addirittura di un "server Timestamp" per descrivere quello che oggi chiameremmo "Blockchain". Il ruolo del timestamping sul Bitcoin è quello di determinare la cronologia delle transazioni, in modo che, senza l'intervento di un'autorità centrale, si possa stabilire quale transazione sia arrivata per prima. Questo meccanismo consente a ciascun utente di verificare l'inesistenza di una transazione nel passato, impedendo così a un utente malintenzionato di effettuare una doppia spesa. Questo meccanismo è giustificato da Satoshi Nakamoto nel suo Libro Bianco con la famosa frase: " *Questo standard si basa sul tempo Unix, che rappresenta il numero totale di secondi trascorsi dal 1° gennaio 1970.


> ► *I timestamp dei blocchi sono relativamente flessibili sul Bitcoin, poiché affinché un Timestamp sia considerato valido, è semplicemente necessario che sia maggiore del tempo mediano degli 11 blocchi che lo precedono (MTP) e minore della mediana dei tempi restituiti dai nodi (network-adjusted time) più 2 ore