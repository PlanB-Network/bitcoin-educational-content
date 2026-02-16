---
term: Scriptsig
definition: scriptPubKey 조건을 충족하기 위한 데이터를 제공하는 입력부 요소.
---

입력에 위치한 Bitcoin 트랜잭션의 요소입니다. 스크립트 서명`은 자금이 지출되는 이전 트랜잭션의 `스크립트 공개 키`가 설정한 조건을 충족하는 데 필요한 데이터를 제공합니다. 따라서 `scriptPubKey`를 보완하는 역할을 합니다. 일반적으로 `scriptSig`에는 디지털 서명과 공개 키가 포함됩니다. 서명은 비트코인 소유자가 개인 키를 사용하여 생성하며, UTXO를 사용할 수 있는 권한이 있음을 증명합니다. 이 경우 `scriptSig`는 입력의 소유자가 이전 발신 트랜잭션의 `scriptPubKey`에 지정된 Address과 연결된 공개 키에 해당하는 개인 키를 보유하고 있음을 보여줍니다.


트랜잭션이 확인되면 해당 '스크립트 서명'의 데이터가 해당 '스크립트 퍼브 키'에서 실행됩니다. 결과가 유효하면 자금 지출 조건이 충족되었음을 의미합니다. 트랜잭션의 모든 입력이 해당 `scriptPubKey`를 검증하는 `scriptSig`를 제공하면 트랜잭션이 유효하며 실행을 위해 블록에 추가할 수 있습니다.


예를 들어, 다음은 고전적인 P2PKH '스크립트시그'입니다:


```text
<signature> <public key>
```


해당 `scriptPubKey`가 될 것입니다:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```





> '스크립트시그'는 영어로 '잠금 해제 스크립트'라고도 합니다