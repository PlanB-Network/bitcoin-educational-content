---
termine: DNS SEEDS
---

Punti di connessione iniziali per i nuovi nodi Bitcoin che si uniscono alla rete. Questi seed, che sono in realtà specifici server DNS, hanno il loro indirizzo permanentemente incorporato nel codice di Bitcoin Core. Quando un nuovo nodo si avvia, contatta questi server per ottenere una lista casuale di indirizzi IP di nodi Bitcoin presumibilmente attivi. Il nuovo nodo può quindi stabilire connessioni con i nodi in questa lista per ottenere le informazioni necessarie per eseguire il suo Initial Block Download (IBD) e sincronizzarsi con la catena che ha il maggior lavoro accumulato. Al 2024, ecco la lista dei DNS seeds di Bitcoin Core e gli individui responsabili della loro manutenzione (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

I DNS seeds rappresentano il secondo metodo, in ordine di priorità, per un nodo Bitcoin di stabilire connessioni. Il primo metodo coinvolge l'utilizzo del file peers.dat che il nodo stesso ha creato. Questo file è naturalmente vuoto nel caso di un nuovo nodo, a meno che l'utente non lo abbia manualmente modificato.

> ► *Nota, i DNS seeds non devono essere confusi con i "seed nodes", che rappresentano la terza via per stabilire connessioni.*