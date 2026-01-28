---
term: BIP0113
---

모든 타임락 연산(`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, `OP_CHECKSEQUENCEVERIFY`)의 평가 방식에 변경을 도입했습니다.

이제 타임록을 이전 블록의 Timestamp이 아닌 마지막 11개 블록의 타임스탬프의 중앙값인 MTP(Median Time Past)와 비교해야 한다고 명시합니다.

이러한 변경은 시스템을 더 예측 가능하게 만들고 채굴자가 시간 기준을 조작하는 것을 방지합니다.

BIP113은 2016년 7월 4일 Soft Fork을 통해 BIP68 및 BIP112와 함께 도입되었으며, BIP9 방식으로 처음으로 활성화되었습니다.