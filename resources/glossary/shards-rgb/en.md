---
term: SHARDS (RGB)
---

In the context of the RGB protocol, a Shard represents a distinct branch within the acyclic directed graph (DAG) that traces the history of a contract's State Transitions. It constitutes a coherent subset of the set of transitions, corresponding, for example, to the sequence of operations required to attest the validity of a particular asset since Genesis. This mechanism makes it possible to isolate specific segments of the overall history, to facilitate client-side verification.