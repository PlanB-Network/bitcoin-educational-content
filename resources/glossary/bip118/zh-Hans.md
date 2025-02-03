---
term: BIP118

---
改进比特币的提案旨在引入两个新的 SigHash 标志修改器："SIGHASH_ANYPREVOUT "和 "SIGHASH_ANYPREVOUTANYSCRIPT"。这些功能扩展了比特币交易的功能，尤其是在智能合约和闪电网络等叠加解决方案方面。BIP118 将显著促进 Eltoo 的使用。SIGHASH_ANYPREVOUT "的主要优点是允许在多个交易中重复使用签名，从而提供了更大的灵活性。具体来说，这些 SigHashes 允许使用不涵盖任何事务输入的签名。