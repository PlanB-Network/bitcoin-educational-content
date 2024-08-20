---
term: SIGOPS（签名操作）
---

指的是验证交易所必需的数字签名操作。每个比特币交易都可以包含多个输入，每个输入可能需要一个或多个签名才能被视为有效。这些签名的验证是通过使用特定的操作码（opcode）即“sigops”来完成的。具体来说，这包括`OP_CHECKSIG`、`OP_CHECKSIGVERIFY`、`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`。这些操作对必须验证它们的网络节点施加了一定的工作负载。为了防止通过人为增加sigops数量来进行DoS攻击，协议因此对每个区块允许的sigops数量施加了限制，以确保验证负载对节点来说是可管理的。目前，每个区块的sigops数量上限设定为80,000。为了计数，节点遵循以下规则：

在`scriptPubKey`中，`OP_CHECKSIG`和`OP_CHECKSIGVERIFY`计为4个sigops。操作码`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`计为80个sigops。实际上，在计数时，如果这些操作不是SegWit输入的一部分（对于P2WPKH，sigops的数量因此为1），则这些操作被乘以4；

在`redeemScript`中，操作码`OP_CHECKSIG`和`OP_CHECKSIGVERIFY`也计为4个sigops，`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`如果在`OP_n`之前，则按`4n`计算，否则计为80个sigops；

对于`witnessScript`，`OP_CHECKSIG`和`OP_CHECKSIGVERIFY`值1个sigop，`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`如果由`OP_n`引入，则按`n`计算，否则计为20个sigops；

在Taproot脚本中，sigops的处理方式与传统脚本不同。与直接计算每个签名操作不同，Taproot为每个交易输入引入了一个与该输入大小成比例的sigops预算。这个预算是50个sigops加上输入见证的字节大小。每个签名操作将这个预算减少50。如果执行签名操作后预算降至零以下，则脚本无效。这种方法在Taproot脚本中提供了更多的灵活性，同时通过将sigops直接与输入的权重联系起来，保持了对潜在滥用sigops的保护。因此，Taproot脚本不包括在每个区块80,000 sigops的限制中。