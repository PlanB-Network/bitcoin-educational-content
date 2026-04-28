---
term: OP_CHECKSIGVERIFY (0XAD)
definition: OP_CHECKSIG와 OP_VERIFY를 결합하여 서명이 유효하지 않으면 스크립트를 중단함.
---

OP_CHECKSIG`와 동일한 작업을 수행하지만 서명 검증에 실패하면 스크립트가 즉시 오류와 함께 중단되고 트랜잭션이 무효화됩니다. 검증에 성공하면 스크립트는 스택에 `1`(참) 값을 푸시하지 않고 계속 진행합니다. 요약하면, `OP_CHECKSIGVERIFY`는 `OP_CHECKSIG` 연산에 이어 `OP_VERIFY`를 수행합니다. 이 옵코드는 슈노르 서명을 확인하기 위해 탭스크립트에서 수정되었습니다.