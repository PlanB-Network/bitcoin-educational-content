---
term: Nulldummy
definition: OP_CHECKMULTISIG의 더미 요소가 빈 바이트 배열이어야 한다는 규칙.
---

SegWit Soft Fork에서 BIP147과 함께 도입된 합의 규칙으로, `OP_CHECKMULTISIG` 및 `OP_CHECKMULTISIGVERIFY` 옵코드에 사용되는 더미 요소가 빈 바이트 배열(`OP_0`)이어야 합니다. 이 요소에 대해 `OP_0` 이외의 값을 사용할 수 없도록 하여 가변성 벡터를 제거하기 위해 구현된 조치입니다.