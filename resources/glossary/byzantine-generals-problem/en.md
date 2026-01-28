---
term: Byzantine generals problem
definition: Problem illustrating the challenges of coordination in a distributed system where actors cannot trust each other.
---

The problem was first formulated by Leslie Lamport, Robert Shostak, and Marshall Pease in the specialized magazine *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) in July 1982. It is used today to illustrate the challenges of decision-making in a distributed system where no participant can be fully trusted.

In this metaphor, a group of Byzantine generals and their respective armies are camped around a city they plan to attack or besiege. The generals are geographically separated from each other and must communicate via messenger to coordinate their strategy. Whether they choose to attack or retreat does not matter, as long as all reach consensus.

The requirements are:
* Each general must make a decision: attack or retreat (yes or no);
*Once the decision is made, it cannot be changed;*
**All generals must agree on the same decision and execute it synchronously.**

However, messages can be delayed, destroyed, altered, or lost. Even if successfully delivered, some generals may be traitors, deliberately sending false or conflicting messages to sow confusion.

In the context of Bitcoin, each general represents a network node that must reach consensus on the system’s state. In other words, the majority of participants in a distributed network must agree and execute the same action to avoid total failure. Traditionally, achieving Byzantine fault-tolerant consensus requires at least two-thirds of the network nodes to be honest. If a majority acts maliciously, the system becomes vulnerable.

> ► *This problem is also sometimes referred to as the “Reliable Broadcast Problem.”*