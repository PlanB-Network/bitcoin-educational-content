---
term: Sighash_all/sighash_acp
---

시그해시 플래그(`0x81`) 유형과 Bitcoin 트랜잭션 서명에 사용되는 `SIGHASH_ANYONECANPAY` 수정자(`SIGHASH_ACP`)를 결합한 유형입니다. 이 조합은 서명이 모든 출력에 적용되고 트랜잭션의 특정 입력에만 적용되도록 지정합니다. sIGHASH_ALL | SIGHASH_ANYONECANPAY`를 사용하면 다른 참여자가 초기 서명 후 트랜잭션에 추가 입력을 추가할 수 있습니다. 이는 크라우드 펀딩 거래와 같은 협업 시나리오에서 특히 유용하며, 초기 서명자가 커밋한 출력의 무결성을 유지하면서 다른 참여자가 각자의 입력을 추가할 수 있습니다.