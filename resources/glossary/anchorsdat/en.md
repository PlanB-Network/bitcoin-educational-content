---
term: Anchors.dat
definition: A Bitcoin Core file storing IP addresses of nodes the client was connected to before shutdown, to facilitate reconnection on restart.
---

File used in the Bitcoin Core client to store the IP addresses of outbound nodes to which a client was connected before being shut down. Anchors.dat is created every time the node is stopped and deleted when it restarts. The nodes whose IP addresses are contained in this file are used to help quickly establish connections when the node is restarted.


