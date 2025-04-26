---
term: SEMI DNS

---
Punti di connessione iniziali per i nuovi nodi Bitcoin che si uniscono alla rete. Questi seed, che sono in realtà specifici server DNS, hanno il loro indirizzo permanentemente incorporato nel codice di Bitcoin Core. Quando un nuovo nodo si avvia, contatta questi server per ottenere un elenco casuale di indirizzi IP di nodi Bitcoin presumibilmente attivi. Il nuovo nodo può quindi stabilire connessioni con i nodi di questo elenco per ottenere le informazioni necessarie a eseguire il suo Initial Block Download (IBD) e a sincronizzarsi con la catena che ha accumulato più lavoro. Al 2024, ecco l'elenco dei semi DNS di Bitcoin Core e dei responsabili della loro manutenzione (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

I semi DNS sono il secondo metodo, in ordine di priorità, con cui un nodo Bitcoin stabilisce le connessioni. Il primo metodo prevede l'utilizzo del file peers.dat creato dal nodo stesso. Questo file è naturalmente vuoto nel caso di un nuovo nodo, a meno che l'utente non lo abbia modificato manualmente.

> *Nota, i semi DNS non devono essere confusi con i "nodi seme", che sono il terzo modo per stabilire le connessioni