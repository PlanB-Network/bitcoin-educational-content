---
term: BIP31

---
Proposal aimed at improving the network management mechanisms by Bitcoin nodes. Before BIP31, Bitcoin nodes had no direct way of knowing if their peers were still connected, operational, and not overloaded. BIP31 introduced the use of a `pong` message, in response to a `ping` message, which allows for an active check of connectivity between nodes.