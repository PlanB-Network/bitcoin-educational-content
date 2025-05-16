---
term: KNAPSACK 解算器
---

在 0.17 版之前的 Bitcoin Core Wallet 中用於選擇硬幣的舊方法。Knapsack Solver 嘗試透過反覆隨機選擇 UTXO，並按子集將其相加來解決選擇硬幣的問題，目標是使費用和交易大小最小化。此方法後來被 *Branch-and-Bound* 所取代。