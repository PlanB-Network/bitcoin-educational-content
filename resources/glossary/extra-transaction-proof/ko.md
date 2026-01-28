---
term: Extra transaction proof
definition: Tapret 유형의 커밋먼트(commitment)를 검증하기 위한 RGB 프로토콜의 보충 데이터.
---

RGB 프로토콜에서 ETP는 (Taproot의 맥락에서) 타플렛형 Commitment의 유효성을 검사하는 데 필요한 추가 데이터를 통합하는 Anchor의 일부입니다. 여기에는 무엇보다도 Taproot 스크립트와 관련된 내부 공개 키와 *스크립트 경로 지출*에 필요한 특정 정보가 포함됩니다. 따라서 이 구성 요소는 암호화 약정의 정확한 검증을 보장합니다.