---
term: SEED NODES

---
Static list of public Bitcoin nodes, integrated directly into the source code of Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). This list serves as connection points for new Bitcoin nodes joining the network, but it is only used if the DNS seeds do not provide a response within 60 seconds of their request. In this case, the new Bitcoin node will connect to these seed nodes to establish a first connection to the network and request IP addresses of other nodes. The ultimate goal is to acquire the necessary information to perform the Initial Block Download (IBD) and synchronize with the chain that has the most work accumulated. The list of seed nodes includes nearly 1000 nodes, identified in accordance with the standard established by BIP155. Thus, seed nodes represent the third method of connection to the network for a Bitcoin node, after the possible use of the `peers.dat` file, created by the node itself, and the solicitation of DNS seeds.

> ► *Note, seed nodes should not be confused with "DNS seeds," which are the second method of establishing connections.*