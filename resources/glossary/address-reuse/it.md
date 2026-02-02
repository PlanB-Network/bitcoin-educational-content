---
term: Riutilizzo dell'indirizzo

definition: Una pratica sconsigliata di usare lo stesso indirizzo Bitcoin più volte per ricevere pagamenti, il che danneggia la privacy consentendo il tracciamento dei fondi.
---
Il riutilizzo degli indirizzi si riferisce alla pratica di utilizzare lo stesso indirizzo di ricezione per bloccare più UTXO, a volte nell'ambito di diverse transazioni. I bitcoin sono tipicamente bloccati utilizzando una coppia di chiavi crittografiche che corrisponde a un indirizzo unico. Poiché la blockchain è pubblica, è facile vedere quali indirizzi sono associati a quanti bitcoin. Nel caso di riutilizzo dello stesso indirizzo per più pagamenti, è ragionevole immaginare che tutti gli UTXO associati appartengano alla stessa entità. Pertanto, il riutilizzo degli indirizzi rappresenta un problema per la privacy dell'utente. Permette di creare collegamenti deterministici tra transazioni multiple e UTXO, oltre a perpetuare il tracciamento dei fondi sulla catena. Satoshi Nakamoto aveva già menzionato questo problema nel suo Libro Bianco:

> *Come firewall aggiuntivo, dovrebbe essere utilizzata una nuova coppia di chiavi per ogni transazione, al fine di impedirne il collegamento a un proprietario comune.*

Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Per preservare al minimo la privacy, si consiglia vivamente di utilizzare ogni indirizzo di ricezione una sola volta. Per ogni nuovo pagamento, è opportuno generare un nuovo indirizzo. Anche per le uscite di modifica è opportuno utilizzare un nuovo indirizzo. Fortunatamente, grazie ai portafogli deterministici e gerarchici, è diventato molto semplice utilizzare una moltitudine di indirizzi. Tutte le coppie di chiavi associate a un portafoglio possono essere facilmente rigenerate dal seed. Questo è anche il motivo per cui il software del portafoglio genera sempre un nuovo indirizzo diverso quando si fa clic sul pulsante "Ricevi".
