---
term: 有用負載
---

在計算的一般情況下，有效負載是較大資料封包中的基本資料。例如，在 SegWit V0 over Bitcoin Address 中，有效負載對應於公開金鑰的 Hash，而不包含各種元資料 (HRP、分隔符、SegWit 版本和校驗和)。例如，在 Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` 中，我們有 ：




- `bc`：人類可讀部分 (HRP) ；
- `1`：分隔符 ；
- `q`:SegWit 版本。這是版本 0；
- `c2eukw7reasfcmrafevp5dhv8635yuqa`：有效負載，在本例中為公開金鑰的 Hash；
- `ys50gj`: checksum.