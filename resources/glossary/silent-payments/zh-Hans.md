---
term: SILENT PAYMENTS (静默支付)

---
使用静态比特币地址接收付款的方法，无需重复使用地址，无需交互，不同付款和静态地址之间也没有可见的链上链接。这种技术无需为每笔交易生成新的、未使用的收款地址，从而避免了比特币中收款人必须向付款人提供新地址的常见互动。

使用静默支付时，付款人使用收款人的公钥（支出公钥和扫描公钥）和自己的私钥总和作为输入，为每笔付款生成一个新地址。只有收款人能用自己的私钥计算出与该付款地址相对应的私钥。加密密钥交换算法，即ECDH（*Elliptic-Curve Diffie-Hellman*），用于建立一个共享秘密，然后用来推导接收地址和私人密钥（仅在收款人一方）。收款人必须扫描区块链，检查符合协议标准的每笔交易，才能识别出针对他们的静默支付。与使用通知交易建立支付渠道的 BIP47 不同，静默支付省去了这一步骤，节省了一笔交易。然而，收款人必须扫描所有潜在交易，通过应用 ECDH 来确定这些交易是否是针对他们的。

例如，Bob 的静态地址 $B$ 代表他的扫描公开密钥和支出公开密钥的连接：

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

这些键可以简单地从以下路径导出：

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

该静态地址由 Bob 发布。Alice 使用它向 Bob 进行静默支付。她用这种方法计算出 Bob 的付款地址 $P_0$：

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

其中 inputHash 如下：

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

参数说明：

* $B_{\text{scan}}$：Bob 的扫描公开密钥（静态地址）；
* $B_{\text{spend}}$：Bob 花费的公开密钥（静态地址）；
* $A$:输入（调整）中的公钥之和；
* $a$:调整后的私钥，即在 Alice 交易中作为输入消耗的 UTXO 的`scriptPubKey`中使用的所有密钥对的总和；
* $\text{outpoint}_L$：用作 Alice 交易输入的最小 UTXO（按词典顺序）；
* $\text{ ‖ }$：连接（将操作数端对端连接起来的操作）；
* $G$:椭圆曲线 `secp256k1` 的生成点；
* $\text{hash}$：标记为 `BIP0352/SharedSecret` 的 SHA256 哈希函数；
* $P_0$:第一个公钥/唯一地址，用于向 Bob 付款；
* $0$:用于生成多个唯一付款地址的整数。

Bob 通过这种方式扫描区块链，找到他的 "静默支付"：

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

其中：

* $b_{\text{scan}}$：Bob 的私人扫描密钥。

如果他发现 $P_0$ 是一个包含寄给他的无声付款的地址，他就会计算出 $p_0$，即允许他使用 Alice 发送给 $P_0$ 的资金的私人密钥：

$$ p_0 = （ b_{text{spend}}+ text{hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

参数说明：

* $b_{\text{spend}}$：Bob 的私人消费密钥；
* $n$：椭圆曲线 `secp256k1` 的阶数。

除了这个基本版本之外，还可以使用标签从同一个基础静态地址生成多个不同的静态地址，其目的是在不显著增加扫描工作量的前提下，实现多用途地址的分离。
