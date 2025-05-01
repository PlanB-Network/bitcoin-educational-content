---
term: PATHFINDING
---

Process used by a node to determine the optimal path for routing a payment through the Lightning channel network. Pathfinding is carried out by the payer node, which must select the most suitable intermediate nodes to reach the recipient. This choice is based on a number of criteria, such as fees, channel capacity and timelocks.

Pathfinding algorithms build a graph of the network topology from the gossip data and evaluate the various possible routes between the payer and receiver node. These routes are ranked from best to worst according to various criteria. The node then tests these routes until it succeeds in making the payment on one of them.