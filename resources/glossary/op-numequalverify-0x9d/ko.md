---
term: OP_NUMEQUALVERIFY(0x9D)
---

OP_NUMEQUAL`과 `OP_VERIFY` 연산을 결합합니다. 스택에서 가장 위에 있는 두 개의 Elements을 수치적으로 비교합니다. 값이 같으면 `OP_NUMEQUALVERIFY`는 스택에서 참 결과를 제거하고 스크립트 실행을 계속합니다. 값이 같지 않으면 결과는 거짓이고 스크립트는 즉시 실패합니다.