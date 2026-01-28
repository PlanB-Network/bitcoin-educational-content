---
term: BIP0118
---

두 가지 새로운 시그해시 플래그 수정자, `SIGHASH_ANYPREVOUT`과 `SIGHASH_ANYPREVOUTANYSCRIPT`를 도입하는 제안서입니다.

이러한 추가 사항은 특히 스마트 컨트랙트 및 Lightning Network과 같은 두 번째 Layer 솔루션에 대한 Bitcoin 거래의 유연성을 확장합니다.

BIP118의 주목할 만한 적용 사례 중 하나는 Eltoo 업데이트 메커니즘을 활성화하는 것입니다.

SIGHASH_ANYPREVOUT`의 가장 큰 장점은 여러 트랜잭션에서 서명을 재사용할 수 있어 더 큰 유연성을 제공한다는 것입니다. 특히 이러한 시그해시 플래그를 사용하면 트랜잭션의 어떤 입력도 커밋하지 않는 서명을 생성할 수 있습니다.