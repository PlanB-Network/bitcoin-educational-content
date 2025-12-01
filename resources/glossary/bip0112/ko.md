---
term: BIP0112
---

Bitcoin 스크립트 언어에 `OP_CHECKSEQUENCEVERIFY`(CSV) 옵코드를 도입합니다. 이 옵코드를 사용하면 블록 수 또는 경과 시간으로 정의된 이전 트랜잭션에서 상대적으로 지연된 후에만 유효한 트랜잭션을 생성할 수 있습니다. oP_CHECKSEQUENCEVERIFY`는 스택 상단의 값을 입력의 `nSequence` 값과 비교합니다.

이 값보다 크고 다른 모든 조건이 충족되면 스크립트가 유효합니다. 사실상 `OP_CHECKSEQUENCEVERIFY`는 입력의 `nSequence` 필드에 허용되는 값을 제한하고, 이는 다시 해당 입력이 포함된 트랜잭션이 블록에서 확인될 수 있는 시기를 제한합니다. BIP112는 2016년 7월 4일 Soft Fork을 통해 BIP68 및 BIP113과 함께 도입되었으며, BIP9 방식을 사용하여 처음으로 활성화되었습니다.