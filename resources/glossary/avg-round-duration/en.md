---
term: Average round duration
definition: An indicator estimating the average time required for a mining pool to find a block, based on its computational power and network difficulty.
---

The average round duration is an indicator used to estimate how long it takes a mining pool to find a block, based on the network's difficulty and the pool's hashrate. It is calculated by dividing the expected number of shares needed to find a valid block by the pool's hashrate. For example, if a mining pool has 200 miners, and each generates an average of 4 shares per second, the total computational power of the pool is 800 shares per second:

```text
200 * 4 = 800
```

Assuming that, on average, it takes 1 million shares to find a valid block, the pool's *Avg. Round Duration* would be 1,250 seconds, or about 21 minutes:

```text
1,000,000 / 800 = 1,250
```

It means that, on average, the pool is expected to find one block every 21 minutes. This indicator fluctuates depending on changes in the pool's hashrate: a hashrate increase reduces the *Avg. Round Duration*, while a decrease extends it. It will also fluctuate with each periodic adjustment of the Bitcoin difficulty target (every 2016 blocks). This measure only reflects the internal performance of the specific pool and does not account for blocks found by other pools.

