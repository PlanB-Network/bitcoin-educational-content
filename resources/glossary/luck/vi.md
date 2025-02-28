---
term: LUCK

---
An indicator used in mining pools to measure a pool's performance relative to its theoretical expectations. As its name suggests, it evaluates the pool's luck in finding a block. Luck is calculated by comparing the number of shares theoretically needed to find a valid block, based on the current difficulty of Bitcoin, to the actual number of shares produced to find that block. A number of shares lower than expected indicates good luck, while a higher number indicates bad luck.

By correlating the difficulty on Bitcoin with its number of shares produced each second and the difficulty of each share, the pool can calculate the number of shares that are theoretically necessary to find a valid block. For example, suppose theoretically, it takes 100,000 shares for a pool to find a block. If the pool actually produces 200,000 before finding a block, its luck is 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Conversely, if this pool found a valid block after only producing 50,000 shares, then its luck is 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Luck is an indicator that can only be updated after a block is discovered by the pool, making it a static indicator that is updated periodically.