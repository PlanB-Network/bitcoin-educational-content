---
term: 输出脚本描述符

---
输出脚本描述符（或简称描述符）是结构化的表达式，可全面描述输出脚本（`scriptPubKey`），并提供所有必要信息，以跟踪特定脚本的往来交易。这些描述符通过对所使用地址的结构和类型进行标准描述，便于管理 HD 钱包中的密钥。

描述符的主要作用在于，它能将恢复钱包的所有基本信息封装在一个字符串中（除了恢复短语）。通过保存带有相应记忆短语的描述符，不仅可以恢复私钥，还可以恢复钱包的精确结构和相关脚本参数。事实上，恢复钱包不仅需要初始种子的知识，还需要子密钥对推导的特定索引，以及多位钱包中每个因子的 `xpub`。以前，我们认为这些信息是所有人都隐含知道的。然而，随着脚本的多样化和更复杂配置的出现，这些信息可能会变得难以推断，从而将这些数据转化为私人和难以破解的信息。描述符的使用大大简化了这一过程：只需知道恢复短语和相应的描述符，就能可靠、安全地恢复所有内容。

描述符由几个要素组成：


- 脚本函数，如`pk`（Pay-to-PubKey）、`pkh`（Pay-to-PubKey-Hash）、`wpkh`（Pay-to-Witness-PubKey-Hash）、`sh`（Pay-to-Script-Hash）、`wsh`（Pay-to-Witness-Script-Hash）、`tr`（Pay-to-Taproot）、`multi`（Multisignature）和`sortedmulti`（Multisignature with sorted keys）；
- 派生路径，例如，"[d34db33f/44h/0h/0h]"表示派生路径和特定的主密钥指纹；
- 各种格式的密钥，如十六进制公开密钥或扩展公开密钥（`xpub`）；
- 校验和，前面是哈希值，用于验证描述符的完整性。

例如，P2WPKH 钱包的描述符可以如下所示：

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

在该描述符中，派生函数 `wpkh` 表示支付-见证-公钥-哈希脚本类型。其后是包含以下内容的派生路径：


- cdeab12f：主密钥的指纹；
- `84h`：表示使用 BIP84 目的，用于 SegWit v0 地址；
- `0h`：表示它是主网上的 BTC 货币；
- 0h：指钱包中使用的特定账号。

描述符还包括该钱包使用的扩展公钥：

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

接下来，符号 `/<0;1>/*`指定描述符可以从外部链（`0`）和内部链（`1`）生成地址，通配符（`*`）允许以可配置的方式顺序生成多个地址，类似于管理传统钱包软件的 "间隙限制"。

最后，`#jy0l7nr4` 表示校验和，用于验证描述符的完整性。