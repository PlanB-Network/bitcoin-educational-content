---
term: NULLDUMMY

---
与 BIP147 一起引入 SegWit 软分叉的共识规则，要求 `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 操作码中使用的哑元素必须是空字节数组 (`OP_0`)。实施这一措施是为了通过禁止该元素使用除 `OP_0` 以外的任何值来消除可篡改性向量。