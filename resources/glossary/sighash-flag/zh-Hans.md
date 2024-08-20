---
term: SIGHASH FLAG
---

比特币交易中的一个参数，决定了交易（输入和输出）的哪些组成部分被相关签名覆盖，从而变得不可更改。SigHash Flag是每个输入的数字签名中添加的一个字节。因此，SigHash Flag的选择直接影响了交易的哪些部分被签名冻结，哪些部分仍然可以被修改。这种机制确保签名根据签名者的意图精确且安全地提交交易数据。有三种主要的SigHash Flag：

- `SIGHASH_ALL` (`0x01`): 签名适用于交易的所有输入和输出，从而完全锁定它们；

- `SIGHASH_NONE` (`0x02`): 签名适用于所有输入，但不适用于任何输出，允许在签名后修改输出；

- `SIGHASH_SINGLE` (`0x03`): 签名覆盖所有输入和仅对应于已签名输入索引的一个输出。

除了这三种SigHash Flag外，修饰符`SIGHASH_ANYONECANPAY` (`0x80`)可以与前述每种类型组合使用。使用这个修饰符时，只有部分输入被签名，留下其他输入可以修改。以下是与修饰符的现有组合：

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): 签名适用于单个输入，同时覆盖交易的所有输出；

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): 签名覆盖单个输入，不承诺任何输出；

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): 签名适用于单个输入，且仅适用于与此输入具有相同索引的输出。

> ► *有时用于“SigHash”的同义词是“Signature Hash Types”。*