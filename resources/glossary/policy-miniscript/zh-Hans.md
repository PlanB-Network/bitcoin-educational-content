---
term: 政策

---
这是一种面向用户的高级语言，可在 Miniscript 框架内简单指定UTXO 的解锁条件。策略是对支出规则的抽象描述。它可以编译成 miniscript，与比特币本地脚本语言的操作一一对应。

![](../../dictionnaire/assets/30.webp)

策略语言与迷你脚本语言略有不同。例如，假设一个安全系统的主路径是密钥 A，恢复路径是密钥 B，但时间锁定为一年（约 52560 个区块）。在策略中，这将是

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

一旦编译成 miniscript，就会是这样：

```plaintext
andor(pk(B),older(52560),pk(A))
```

而一旦转换成本地脚本，就会是这样：

```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```