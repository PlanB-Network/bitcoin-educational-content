---
term: Peers.dat
definition: Bitcoin Core file storing information about known peers of the node.
---

Name of the data file used by the Bitcoin Core software to store information about peers (i.e., nodes) in the network with which the user's node has interacted or can potentially interact. It contains details such as IP addresses, port numbers, and various metadata. The nodes present in this list are by default the seed nodes, followed by all other discovered or manually added nodes. This file usually contains a very large list of peers from which the node randomly selects to establish its connections.