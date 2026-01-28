---
term: SIGHASH_ANYPREVOUT
definition: 서명을 특정 UTXO에 종속시키지 않도록 허용하는 SigHash 제안.
---

BIP118과 함께 도입된 Bitcoin의 새로운 시그해시 플래그 수정자 구현을 위한 제안. sIGHASH_ANYPREVOUT`을 사용하면 트랜잭션 관리의 유연성이 향상되며, 특히 Lightning Network의 결제 채널과 Eltoo 업데이트와 같은 고급 애플리케이션에서 더욱 유용합니다. SIGHASH_ANYPREVOUT`을 사용하면 서명이 특정 이전 UTXO(*Any Previous Output*)에 연결되지 않도록 할 수 있습니다. SIGHASH_ALL`과 함께 사용하면 트랜잭션의 모든 출력을 서명할 수 있지만 입력은 서명하지 않을 수 있습니다. 이렇게 하면 특정 조건이 충족되는 한 다른 트랜잭션에 서명을 재사용할 수 있습니다.


> 이 시그해시 수정자 SIGHASH_ANYPREVOUT은 2016년 조셉 푼이 Lightning Network의 개념을 개선하기 위해 처음 제안한 SIGHASH_NOINPUT의 아이디어에서 파생되었습니다.*