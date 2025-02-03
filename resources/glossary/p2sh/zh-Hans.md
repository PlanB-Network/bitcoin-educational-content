---
term: P2SH

---
P2SH 是 *Pay to Script Hash* 的缩写。它是一种标准脚本模式，用于确定UTXO 的消费条件。P2PK 和 P2PKH 脚本的消费条件是预定义的，而 P2SH 不同，它允许在交易脚本中集成任意消费条件和附加功能。

从技术上讲，在 P2SH 交易中，"scriptPubKey "包含 "redeemScript "的加密哈希值，而不是明确的支出条件。这个哈希值是通过 `SHA256` 哈希值获得的。向 P2SH 地址发送比特币时，底层的 "redeemScript "不会显示。交易中只包含它的哈希值。P2SH 地址以 `Base58Check` 编码，并以数字 `3` 开头。当收件人希望使用收到的比特币时，他们必须提供一个与 `scriptPubKey` 中的哈希值相匹配的 `redeemScript` 以及满足该 `redeemScript` 条件的必要数据。例如，在 P2SH 多重签名脚本中，脚本可能需要多个私钥的签名。

P2SH 的使用更具灵活性，因为它允许在发送方不知道细节的情况下构建任意脚本。P2SH 于 2012 年与 BIP16 一起推出。