---
term: DNS SEEDS

---
Initial connection points for new Bitcoin nodes joining the network. These seeds, which are actually specific DNS servers, have their address permanently embedded in the Bitcoin Core code. When a new node starts, it contacts these servers to obtain a random list of IP addresses of presumably active Bitcoin nodes. The new node can then establish connections with the nodes on this list to obtain the information needed to perform its Initial Block Download (IBD) and synchronize with the chain that has the most accumulated work. As of 2024, here is the list of Bitcoin Core DNS seeds and the individuals responsible for their maintenance (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


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

DNS seeds are the second method, in order of priority, for a Bitcoin node to establish connections. The first method involves using the peers.dat file that the node itself has created. This file is naturally empty in the case of a new node, unless the user has manually modified it.

> ► *Note, DNS seeds should not be confused with "seed nodes," which are the third way to establish connections.*