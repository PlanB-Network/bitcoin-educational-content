---
term: redeemscript
---

P2SH 출력과 관련된 자금의 잠금을 해제하기 위해 입력이 충족해야 하는 특정 조건을 정의하는 스크립트입니다. P2SH UTXO에서 `scriptPubKey`는 `redeemscript`의 Hash을 포함합니다. 트랜잭션이 이 UTXO를 입력으로 사용하려면, `scriptPubKey`에 포함된 Hash과 일치하는 명확한 `redeemscript`을 제공해야 합니다. 따라서 `redeemscript`은 서명 또는 공개 키와 같이 스크립트의 조건을 충족하는 데 필요한 다른 Elements와 함께 입력의 `scriptSig`에 제공됩니다. 이 캡슐화된 구조는 비트코인이 실제로 사용될 때까지 지출 조건의 세부 사항을 숨길 수 있도록 합니다. 이는 특히 레거시 P2SH 다중 서명 지갑에 사용됩니다.