---
term: BIP118
---

旨在改进比特币的提案，提出引入两个新的SigHash标志修饰符：`SIGHASH_ANYPREVOUT`和`SIGHASH_ANYPREVOUTANYSCRIPT`。这些功能扩展了比特币交易的能力，特别是在智能合约和像闪电网络这样的覆盖解决方案方面。BIP118将显著地支持Eltoo的使用。`SIGHASH_ANYPREVOUT`的主要优势是允许在多个交易中重用签名，这提供了更多的灵活性。具体来说，这些SigHashes允许一个签名覆盖交易的输入。