---
term: Witnessscript
definition: P2WSH 또는 P2SH-P2WSH UTXO에 대한 소비 조건을 정의하는 스크립트로, SegWit에서 redeemScript와 동일한 역할을 함.
---

P2WSH 또는 P2SH-P2WSH UTXO에서 비트코인을 사용할 수 있는 조건을 지정하는 스크립트입니다. 일반적으로 `witnessScript`는 SegWit 표준에 따라 다중서명 Wallet의 조건을 결정합니다. 이러한 스크립트 표준에서 UTXO(출력)의 `scriptPubKey`에는 `witnessScript`의 Hash가 포함되어 있습니다. 이 UTXO을 새 트랜잭션의 입력으로 사용하려면, 보유자는 원본 `witnessScript`를 공개하여 `scriptPubKey`의 지문과 일치한다는 것을 증명해야 합니다. 그런 다음 `witnessScript`는 트랜잭션의 `scriptWitness`에 포함되어야 하며, 여기에는 서명 등 스크립트 검증에 필요한 Elements도 포함되어야 합니다. 따라서 `witnessScript`는 P2SH 트랜잭션에서 `redeemscript`의 SegWit와 동일하지만, `scriptSig`가 아닌 트랜잭션의 증인에 위치한다는 차이점이 있습니다.


> 주의, `witnessScript`를 `scriptWitness`와 혼동해서는 안 됩니다. 위트니스스크립트`는 P2WSH 또는 P2SH-P2WSH UTXO의 지출 조건을 정의하고 그 자체로 스크립트를 구성하는 반면, `scriptWitness`는 모든 SegWit 입력의 위트니스 데이터를 포함합니다*