---
term: SHARDS (LIGHTNING)
---

In the context of *Multi-Path Payments (MPP)* or *Atomic Multi-Path Payments (AMP)*, a Shard is a fraction of a global payment. Each Shard represents a part of the total payment, which is routed separately via a different route on Lightning.

In MPP, all shards share the same secret, whereas in AMP, each Shard has a unique partial secret. The receiver groups the shards together to reconstitute and finalize the full payment. This mechanism circumvents liquidity limitations on a single channel.