---
term: ANALYSIS - HEURISTIC
---

In the context of Bitcoin, a heuristic analysis refers to a set of empirical methods used to trace the flow of bitcoins on the blockchain based on observable transaction characteristics. A heuristic is a practical approach to problem-solving, often through approximate methods, which represents a sufficiently good solution to achieve a given goal. These heuristics yield fairly reliable results, but never with absolute precision. In other words, chain analysis always involves a degree of plausibility in its conclusions. For example, one might estimate with varying degrees of confidence that two addresses belong to the same entity, but complete certainty is unattainable. The main goal of chain analysis is to aggregate multiple heuristics to reduce the risk of error. It is essentially a cumulative evidence process that brings us closer to the underlying reality. In this context, internal and external heuristics are differentiated.

Internal heuristics focus on characteristics within an individual transaction. These include features such as UTXO amounts, script types, version numbers, and locktimes. For instance, the round payment heuristic helps identify an output as likely being a payment if its amount is a round number.Internal heuristics often help pinpoint change outputs (i.e., funds returned to the sender), enabling further tracking.

External heuristics, on the other hand, analyze similarities and characteristics beyond the transaction itself. They encompass the entire transaction environment. For example, the reuse of an address across multiple transactions is an external heuristic. The CIOH is also one.
