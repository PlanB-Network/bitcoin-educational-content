---
term: AVG. ROUND DURATION

---
The average round duration is an indicator used to estimate the time it takes for a mining pool to find a block, based on the network's difficulty and the pool's hashrate. It is calculated by taking the number of shares expected to find a block and dividing it by the pool's hashrate. For example, if a mining pool has 200 miners, and each generates an average of 4 shares per second, the total computational power of the pool is 800 shares per second:

```text
200 * 4 = 800
```

Assuming that, on average, it takes 1 million shares to find a valid block, the pool's *Avg. Round Duration* would be 1,250 seconds, or about 21 minutes:

```text
1,000,000 / 800 = 1,250
```

In practical terms, this means that, on average, the mining pool should find a block every 21 minutes or so. This indicator fluctuates with changes in the pool's hashrate: an increase in hashrate reduces the *Avg. Round Duration*, while a decrease extends it. It will also fluctuate with each periodic adjustment of the Bitcoin difficulty target (every 2016 blocks). This measure does not take into account blocks found by other pools and focuses solely on the internal performance of the pool being studied.