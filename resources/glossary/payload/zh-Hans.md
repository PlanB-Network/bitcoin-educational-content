---
term: 负载

---
在计算的一般情况下，有效载荷指的是较大数据包中的基本数据。例如，在比特币的 SegWit V0 地址中，有效载荷对应的是公钥的哈希值，不包括各种元数据（HRP、分隔符、SegWit 版本和校验和）。例如，在地址 "bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj "中，我们有：


- bc"：人类可读部分（HRP）；
- `1` : 分隔符；
- `q` : SegWit 版本。这里是版本 0；
- c2eukw7reasfcmrafevp5dhv8635yuqa`：有效载荷，这里是公钥的哈希值；
- ys50gj` ：校验和。