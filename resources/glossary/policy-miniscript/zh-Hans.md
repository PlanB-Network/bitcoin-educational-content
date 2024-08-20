---
术语：POLICY (MINISCRIPT)
---

POLICY（最小脚本）是一种高级、面向用户的语言，允许简单地指定在Miniscript框架内可以解锁UTXO的条件。策略是对支出规则的抽象描述。然后，它可以被编译成miniscript，这是与比特币原生脚本语言操作一一对应的。

![](../../dictionnaire/assets/30.png)

策略语言与miniscript语言略有不同。例如，想象一个安全系统，其主路径为密钥A，恢复路径为密钥B，但设置了一年（大约52,560个区块）的时间锁。在策略中，这将是：

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

一旦编译成miniscript，它将是：

```plaintext
andor(pk(B),older(52560),pk(A))
```

一旦转换成原生脚本，它将是：

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