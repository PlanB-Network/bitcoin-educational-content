---
term: BYZANTINE GENERALS PROBLEM

---
The problem was first formulated by Leslie Lamport, Robert Shostak, and Marshall Pease in the specialized magazine *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) in July 1982. It is used today to illustrate the challenges in terms of decision-making when a distributed system cannot trust any actor.

In this metaphor, a group of Byzantine generals and their respective armies are camped around a city they wish to attack or besiege. The generals are geographically separated from each other and must communicate via messenger to coordinate their strategy. Whether they attack or retreat does not matter, as long as all the generals reach a consensus.

Therefore, we can consider the following requirements:


- Each general must make a decision: attack or retreat (yes or no);
- Once the decision is made, it cannot be changed;
- All generals must agree on the same decision and execute it synchronously.

Moreover, a general can only communicate with another through messages transmitted by a courier, which can be delayed, destroyed, altered, or lost. And even if a message is successfully delivered, one or more generals may choose (for whatever reason) to betray the established trust and send a fraudulent message, sowing chaos.

Applying the dilemma to the context of the Bitcoin blockchain, each general represents a node in the network, needing to reach a consensus on the system's state. In other words, the majority of participants in a distributed network must agree and execute the same action to avoid total failure. The only way to reach a consensus in this type of distributed system is to have at least 2/3 of the network nodes reliable and honest. Therefore, if the majority of the network decides to act maliciously, the system is vulnerable.

> ► *This dilemma is sometimes also called "The Problem of Reliable Broadcast."*