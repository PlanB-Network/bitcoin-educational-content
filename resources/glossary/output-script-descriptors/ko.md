---
term: 출력 스크립트 설명자
---

출력 스크립트 설명자 또는 간단히 설명자는 출력 스크립트(`scriptPubKey`)를 완전히 설명하는 구조화된 표현식으로, 특정 스크립트와 주고받는 트랜잭션을 추적하는 데 필요한 모든 정보를 제공합니다. 이러한 설명자는 사용된 주소의 구조와 유형에 대한 표준 설명을 통해 HD 지갑의 키 관리를 용이하게 합니다.


설명자의 주요 관심사는 복구 문구 외에 Wallet 복원을 위한 모든 필수 정보를 단일 문자열에 캡슐화할 수 있는 기능에 있습니다. 해당 Mnemonic 구문과 함께 Descriptor을 저장하면 개인 키뿐만 아니라 Wallet의 정확한 구조와 관련 스크립트 매개변수도 복원할 수 있습니다. 실제로 Wallet을 복구하려면 초기 seed뿐만 아니라 하위 키 쌍을 도출하기 위한 특정 인덱스와 Multisig Wallet의 경우 각 요소의 'xpub'에 대한 지식도 필요합니다. 이전에는 이러한 정보를 모두가 암묵적으로 알고 있다고 가정했습니다. 그러나 스크립트가 다양해지고 더 복잡한 구성이 등장하면서 이 정보를 추정하기 어려워져 이러한 데이터를 비공개 및 Hard 대입 정보로 전환할 수 있었습니다. 설명자를 사용하면 복구 구문과 해당 Descriptor만 알면 모든 것을 안정적이고 안전하게 복원할 수 있으므로 프로세스가 크게 간소화됩니다.


Descriptor은 여러 개의 Elements로 구성됩니다:


- 스크립트 함수는 `pk`(페이투펍키), `pkh`(페이투펍키-Hash), `wpkh`(페이투위트니스-펍키-Hash), `sh`(Pay-to-Script-Hash), `wsh`(페이투위트니스-스크립트-Hash), `tr`(Pay-to-Taproot), `multi`(다중 서명), `sortedmulti`(정렬된 키를 사용한 다중 서명) 등입니다;
- 파생 경로, 예를 들어 `[d34db33f/44h/0h/0h]`는 파생 경로와 특정 마스터 키 지문을 나타냅니다;
- 16진수 공개 키 또는 확장 공개 키(`xpub`)와 같은 다양한 형식의 키입니다;
- Descriptor의 무결성을 확인하기 위해 Hash가 앞에 오는 체크섬입니다.


예를 들어 P2WPKH Wallet에 대한 Descriptor은 다음과 같습니다:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/#jy0l7n
r4
```

이 Descriptor에서 파생 함수 `wpkh`는 Pay-to-Witness-Public-Key-Hash 스크립트 유형을 나타냅니다. 그 뒤에는 파생 경로가 포함됩니다:


- cdeab12f`: 마스터 키의 지문입니다;
- 84h`: SegWit v0 주소를 위한 BIP84 용도로 사용됨을 나타냅니다;
- '0h': Mainnet의 BTC 통화임을 나타냅니다;
- '0h': Wallet에서 사용되는 특정 계정 번호를 나타냅니다.


Descriptor에는 이번 Wallet에 사용된 확장 공개 키도 포함되어 있습니다:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


다음으로, `/<0;1>/*` 표기법은 Descriptor이 외부(`0`) 및 내부(`1`) 체인에서 generate 주소를 지정할 수 있음을 명시하며, 와일드카드(`*`)를 사용하면 기존 Wallet 소프트웨어에서 "갭 제한"을 관리하는 것과 유사하게 여러 주소를 구성 가능한 방식으로 순차적으로 파생할 수 있습니다.


마지막으로 `#jy0l7nr4`는 Descriptor의 무결성을 확인하기 위한 체크섬을 나타냅니다.