---
term: Commitment
---

Commitment（密码学意义上的）是一个数学对象，记作 $C$，由对结构化数据 $m$（信息）和随机值 $r$ 的操作确定地推导出来。我们写为：


$$
C = \text{commit}(m, r)
$$


该机制包括两项主要操作：




- 提交：我们对信息 $m$ 和随机 $r$ 应用加密函数，生成 $C$ ；
- 验证：我们使用 $C$、$m$ 信息和 $r$ 值来检查 Commitment 是否正确。函数返回 `True` 或 `False`。


Commitment 必须尊重两个属性：




- 绑定：一定不可能找到产生相同 $C$ 的两个不同信息：


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


例如 ：


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- 隐藏：对 $C$ 的了解不得泄露 $m$ 的内容。


在 RGB 协议中，Commitment 被包含在 Bitcoin 交易中，以证明在特定时间存在某条信息，而不披露信息本身。