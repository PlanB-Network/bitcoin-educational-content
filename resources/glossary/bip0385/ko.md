---
term: BIP0385
definition: 디스크립터에서 주소 또는 16진수 형식으로 출력 스크립트를 설명하기 위한 addr(), raw() 함수.
---

Descriptor 함수 `addr(ADDR)`과 `raw(HEX)`를 소개합니다. Addr(ADDR)` 함수는 수신 Address를 사용하여 출력 스크립트를 기술할 수 있고, `raw(HEX)` 함수는 해당 스크립트의 16진수 원시 표현을 사용하여 출력 스크립트를 지정할 수 있습니다. BIP385는 Bitcoin core 버전 0.17에서 다른 모든 Descriptor 관련 BIPs(BIP386 제외)와 함께 구현되었습니다.