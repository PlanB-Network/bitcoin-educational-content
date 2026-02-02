---
term: BIP0381
definition: 디스크립터에서 레거시 스크립트를 설명하기 위한 pk(), pkh(), sh() 함수.
---

설명자 함수, 특히 `pk(KEY)`(페이투펍키), `pkh(KEY)`(페이투펍키-Hash), `sh(SCRIPT)`(Pay-to-Script-Hash)를 소개합니다. 이러한 함수는 설명자 내에서 레거시 스크립트 유형을 설명하는 방법을 표준화합니다.

BIP381은 Bitcoin core v0.17에서 다른 모든 Descriptor 관련 BIPs(BIP386 제외)와 함께 구현되었습니다.