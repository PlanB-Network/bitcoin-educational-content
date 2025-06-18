---
term: RGB
---

分散、保密的 Smart contract 系统，旨在与 Bitcoin 和 Lightning Network 协同工作。RGB 以 Client-side Validation 模式运行，将 Contract State 与 Blockchain 的存储分离，只保留加密承诺。这样，完整的状态历史就被保存在链之外，从而提高了可扩展性和保密性。因此，RGB 可以直接在 Bitcoin 上创建复杂的合约，以存储代币、NFT、去中心化身份或 DeFi 解决方案。


在 RGB 上，Single-Use Seal 是一种加密机制，它利用了 Bitcoin 上的 UTXO 只能使用一次的事实，确保了对 Double-spending 的抵御能力。至于令牌的真实性，则通过客户端验证从 Contract 创建到其最新状态的历史状态来保证。