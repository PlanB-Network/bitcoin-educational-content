---
term: DER
---

*Distinguished Encoding Rules* 的縮寫。它是規範 [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) 中定義的 ASN.1 編碼規則的嚴格子集，用於以二進位序列對任何類型的資料進行編碼。DER 主要用於特定領域，例如密碼學，在這些領域中，資料必須以標準、可預測的方式編碼。


在 Bitcoin 上，ECDSA 簽署以 DER 格式編碼。它們由兩個 32 位元組的編碼數字 (`r`,`s`)組成。簽章格式由下列 Elements (71 位元組) 組成：


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


與 ：




- 0x30` (1 位元組)：複合結構的識別碼；
- length` (1 位元組)：下列資料的長度 ；
- 0x02` (1 位元組)：資料識別碼類型 `INTEGER` (整數) ；
- `r-length` (1 位元組)：下一個 `r` 值的長度（32 位元組） ；
- r` (32 位元組)： `r` 的值為 big-endian 整數；
- 0x02` (1 位元組)：資料識別碼類型 `INTEGER` (整數) ；
- `s-length` (1 位元組)：下一個 `s` 值的長度（32 位元組） ；
- `s`（32 位元組）：`s` 值為 big-endian 整數。


在 Bitcoin 交易中，DER 簽署的末端會加入一個位元組，以指出所使用的 SigHash 類型。