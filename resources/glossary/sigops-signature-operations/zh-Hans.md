---
term: SIGOP（签名操作）

---
指验证交易所需的数字签名操作。每个比特币交易可能包含多个输入，每个输入可能需要一个或多个签名才能被视为有效。这些签名的验证是通过使用被称为 "sigops "的特定操作码来完成的。具体来说，这包括 `OP_CHECKSIG`、`OP_CHECKSIGVERIFY`、`OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY`。这些操作给必须验证它们的网络节点带来了一定的工作量。为了防止通过人为增加 sigops 数量来进行 DoS 攻击，协议对每个区块允许的 sigops 数量设置了限制，以确保节点的验证负载保持在可控范围内。该限制目前设定为每个区块最多 80,000 个 sigops。节点按照以下规则进行计数：

在 `scriptPubKey` 中，`OP_CHECKSIG` 和 `OP_CHECKSIGVERIFY` 算作 4 个 sigops。操作码 `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 的计数为 80 个 sigops。事实上，在计数过程中，如果这些操作不属于 SegWit 输入的一部分，它们将乘以 4（因此，对于 P2WPKH，sigops 的数量将为 1）；

在 `redeemScript` 中，操作码 `OP_CHECKSIG` 和 `OP_CHECKSIGVERIFY` 也算作 4 个 sigops， `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 如果在 `OP_n` 之前，则算作 `4n`，否则算作 80 个 sigops；

对于 `witnessScript` 来说，`OP_CHECKSIG` 和 `OP_CHECKSIGVERIFY`值 1 sigop，`OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY`如果是由 `OP_n` 引入的，则计为 `n`，否则为 20 sigops；

在 Taproot 脚本中，sigops 的处理方式与传统脚本不同。Taproot 并不直接计算每个签名操作，而是为每个事务输入引入一个与输入大小成比例的 sigops 预算。该预算为 50 sigops 加上输入见证的字节大小。每次签名操作都会将预算减少 50。如果签名操作的执行使预算降到零以下，则脚本无效。通过这种方法，Taproot 脚本具有更大的灵活性，同时通过将 sigops 与输入权重直接挂钩，还能防止与 sigops 相关的潜在滥用。因此，Taproot 脚本不包括在每块 80,000 个 sigops 的限制内。