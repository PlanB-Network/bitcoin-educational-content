---
term: 实用负载
---

在计算的一般情况下，有效载荷是较大数据包中的基本数据。例如，在 Bitcoin Address 上的 SegWit V0 中，有效载荷相当于公钥的 Hash，不包含各种元数据（HRP、分隔符、SegWit 版本和校验和）。例如，在 Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` 中，我们有 ：




- bc：人类可读部分（HRP）；
- 1"：分隔符 ；
- `q`:SegWit 版本。这是版本 0；
- c2eukw7reasfcmrafevp5dhv8635yuqa"：有效负载，在本例中是公钥的 Hash；
- `ys50gj`: 校验和。