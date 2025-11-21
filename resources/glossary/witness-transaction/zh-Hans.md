---
term: Witness Transaction
---

在 RGB 协议中，Witness Transaction 指的是围绕包含 Multi Protocol Commitment 的报文（MPC）关闭 Single-Use Seal 的 Bitcoin 事务。这一操作包括使用现有的 UTXO 或创建新的 UTXO，以便锁定写入协议的合约 Commitment。因此，Witness Transaction 是 On-Chain 的证明，证明 RGB Contract 的状态已在特定时间点固定下来。