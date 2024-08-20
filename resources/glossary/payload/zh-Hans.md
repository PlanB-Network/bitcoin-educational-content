---
term: PAYLOAD
---

在计算的一般上下文中，payload指的是在更大的数据包内携带的基本数据。例如，在比特币的SegWit V0地址中，payload对应于公钥的哈希值，排除了各种元数据（HRP、分隔符、SegWit版本和校验和）。例如，在地址`bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`中，我们有：
* `bc`：人类可读部分（HRP）；
* `1`：分隔符；
* `q`：SegWit版本。这里是版本0；
* `c2eukw7reasfcmrafevp5dhv8635yuqa`：payload，在这里是公钥的哈希值；
* `ys50gj`：校验和。