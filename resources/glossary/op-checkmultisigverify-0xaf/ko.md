---
term: OP_CHECKMULTISIGVERIFY (0XAF)
definition: OP_CHECKMULTISIG와 OP_VERIFY를 결합하여 검증에 실패하면 스크립트를 중단함.
---

OP_CHECKMULTISIG`와 `OP_VERIFY`를 결합합니다. OP_CHECKMULTISIG`와 마찬가지로 `N` 서명 중 `M` 서명이 유효한지 확인하기 위해 여러 서명과 공개키가 필요합니다. 그런 다음 `OP_VERIFY`와 마찬가지로 검증에 실패하면 스크립트가 오류와 함께 즉시 중지됩니다. 확인에 성공하면 스택에 값을 푸시하지 않고 스크립트가 계속 진행됩니다. 이 옵코드는 탭스크립트에서 제거되었습니다.