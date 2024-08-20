---
term: NULLDUMMY
---

在SegWit软分叉中引入的共识规则，由BIP147提出，要求在`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`操作码中使用的虚拟元素必须是一个空字节数组（`OP_0`）。这一措施是为了通过禁止对该元素使用除`OP_0`之外的任何值来消除一个可变性向量。