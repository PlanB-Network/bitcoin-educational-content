---
term: PEER DISCOVERY

---
The process by which nodes in the Bitcoin network connect to other nodes to obtain information. When a Bitcoin node is first launched, it has no information about other nodes in the network. Yet, it must establish connections to synchronize with the blockchain that has the most accumulated work. Several mechanisms are used to discover these peers, in order of priority:


- The node starts by consulting its local `peers.dat` file, which stores information about nodes with which it has previously interacted. If the node is new, this file will be empty, and the process will move to the next step;
- In the absence of information in the `peers.dat` file (which is normal for a newly launched node), the node performs DNS queries to the DNS seeds. These servers provide a list of IP addresses of presumably active nodes to establish connections. The addresses of the DNS seeds are hardcoded in the Bitcoin Core code. This step is usually sufficient to complete the discovery of peers;
- If the DNS seeds do not respond within 60 seconds, the node can then turn to the seed nodes. These are public Bitcoin nodes listed in a static list of nearly a thousand entries integrated directly into the source code of Bitcoin Core. The new node will use this list to establish a first connection to the network and obtain IP addresses of other nodes;
- In the very unlikely case where all the previous methods fail, the node operator always has the option to manually add IP addresses of nodes to establish a first connection.