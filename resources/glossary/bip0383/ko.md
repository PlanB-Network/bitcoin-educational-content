---
term: BIP0383
---

설명자에 대한 `multi(NUM, KEY, ..., KEY)` 및 `sortedmulti(NUM, KEY, ..., KEY)` 함수를 소개합니다. 이 함수는 다중 서명 스크립트를 설명하며, `sortedmulti`는 가져오는 동안 공개 키를 사전순으로 정렬하여 호환성을 보장합니다.

BIP383은 Bitcoin core 버전 0.17에서 다른 모든 Descriptor 관련 BIPs(BIP386 제외)와 함께 구현되었습니다.