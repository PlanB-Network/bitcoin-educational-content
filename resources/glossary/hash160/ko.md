---
term: HASH160
---

Bitcoin에서 사용되는 암호화 기능으로, 특히 레거시 및 SegWit v0 수신 주소를 생성하는 데 사용됩니다. 이 함수는 입력에서 연속적으로 실행되는 두 개의 Hash 함수를 결합합니다: 먼저 SHA256, 그다음 RIPEMD160. 따라서 이 함수의 출력은 160비트입니다.


$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$