---
termine: ADDRESS REUSE
---

Il riutilizzo degli indirizzi si riferisce alla pratica di usare lo stesso indirizzo di ricezione per bloccare più UTXO, talvolta all'interno di diverse transazioni. I Bitcoin sono tipicamente bloccati utilizzando una coppia di chiavi crittografiche che corrisponde a un indirizzo unico. Poiché la blockchain è pubblica, è facile vedere quali indirizzi sono associati a quanti bitcoin. Nel caso del riutilizzo dello stesso indirizzo per più pagamenti, è ragionevole immaginare che tutti gli UTXO associati appartengano alla stessa entità. Pertanto, il riutilizzo degli indirizzi pone un problema per la privacy dell'utente. Permette collegamenti deterministici tra più transazioni e UTXO, oltre a perpetuare il tracciamento dei fondi sulla catena. Satoshi Nakamoto ha già menzionato questo problema nel suo White Paper:

> "*Come ulteriore firewall, una nuova coppia di chiavi potrebbe essere utilizzata per ogni transazione per impedire che siano collegate a un proprietario comune.*" - Nakamoto, S. (2008). "Bitcoin: Un Sistema di Denaro Elettronico Peer-to-Peer". Consultato su https://bitcoin.org/bitcoin.pdf.

Per preservare la privacy al minimo, è fortemente consigliato utilizzare ogni indirizzo di ricezione solo una volta. Per ogni nuovo pagamento, è opportuno generare un nuovo indirizzo. Anche per gli output di resto, dovrebbe essere utilizzato un nuovo indirizzo. Fortunatamente, grazie ai portafogli deterministici e gerarchici, è diventato molto facile utilizzare una moltitudine di indirizzi. Tutte le coppie di chiavi associate a un portafoglio possono essere facilmente rigenerate dal seed. Questo è anche il motivo per cui il software del portafoglio genera sempre un nuovo indirizzo diverso quando si clicca sul pulsante “Ricevi”.

> ► *In inglese, si chiama "Address Reuse".*