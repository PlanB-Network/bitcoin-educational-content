---
term: ANCHORS.DAT

---
File used in the Bitcoin Core client to store the IP addresses of outgoing nodes to which a client was connected before being shut down. Anchors.dat is thus created every time the node is stopped and deleted when it is restarted. The nodes whose IP addresses are contained in this file are used to help quickly establish connections when the node is restarted.