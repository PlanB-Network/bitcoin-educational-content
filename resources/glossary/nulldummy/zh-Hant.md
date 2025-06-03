---
term: NULLDUMMY
---

在 SegWit Soft Fork 中與 BIP147 一起引入的共識規則，要求在 `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 操作碼中使用的假元素必須是空的位元組陣列 (`OP_0`)。實施這項措施是為了消除可篡改性向量，方法是禁止此元素使用除 `OP_0` 以外的任何值。