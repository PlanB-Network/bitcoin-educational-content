---
term: OP_EQUALVERIFY (0X88)

definition: OP_EQUALとOP_VERIFYを組み合わせたもので、値が異なる場合はトランザクションを無効にします。
---
OP_EQUAL` と `OP_VERIFY` の関数を組み合わせたものである。まずスタック上の上位 2 つの値が等しいかどうかをチェックし、その結果が 0 でないことを要求する。OP_EQUALVERIFY` はアドレス検証スクリプトでよく使用される。