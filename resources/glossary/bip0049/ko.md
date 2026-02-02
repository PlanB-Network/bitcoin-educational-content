---
term: BIP0049
definition: 파생 경로에서 49' 인덱스를 사용하는 Nested SegWit 주소(P2SH-P2WPKH)를 위한 파생 표준.
---

BIP49는 HD BIP에서 중첩된 generate 주소에 사용되는 파생 방법을 소개하는 유익한 Wallet입니다. 제안된 파생 경로는 목적 수준에서 인덱스 `49'`(강화된 파생)를 사용하여 BIP43 및 BIP44의 표준을 따릅니다. 예를 들어, P2SH-P2WPKH 계정의 첫 번째 Address은 이 경로에서 파생됩니다: `m/49'/0'/0'/0/0`. 중첩된 SegWit 스크립트는 SegWit 출시와 함께 도입되어 사용자가 아직 완전한 SegWit 네이티브가 아닌 지갑에서도 SegWit 기능을 활용할 수 있도록 했습니다.