---
term: 자동 결제
---

Address 재사용 없이, 상호 작용 없이, 다른 결제와 정적 Address 사이에 가시적인 On-Chain 링크 없이 정적 Bitcoin 주소를 사용하여 결제를 받는 방법. 이 기술을 사용하면 각 거래마다 사용하지 않는 새 수취 주소를 generate로 생성할 필요가 없으므로 수취인이 지급인에게 새 Address를 제공해야 하는 Bitcoin의 일반적인 상호 작용을 피할 수 있습니다.


자동 결제를 사용하면 결제자는 수취인의 공개 키(공개 키 사용 및 스캔 공개 키)와 자신의 개인 키 합계를 generate에 입력으로 사용하여 각 결제에 대해 새로운 Address을 생성합니다. 수취인만이 자신의 개인키를 사용하여 이 결제 Address에 해당하는 개인키를 계산할 수 있습니다. 암호화 키 Exchange 알고리즘인 ECDH(*타원 곡선 디피-헬만*)는 공유 비밀을 설정하는 데 사용되며, 이를 통해 수신 Address과 개인 키(수신자 측에서만)를 도출하는 데 사용됩니다. 수신자가 의도한 자동 결제를 식별하기 위해 수신자는 Blockchain를 스캔하고 프로토콜의 기준에 맞는 각 트랜잭션을 검사해야 합니다. 알림 트랜잭션을 사용하여 결제 채널을 설정하는 BIP47과 달리 자동 결제는 이 단계를 생략하여 트랜잭션을 절약할 수 있습니다. 하지만 수신자가 모든 잠재적 거래를 스캔하여 ECDH를 적용하여 해당 거래가 수신자에게 전달되었는지 확인해야 한다는 단점이 있습니다.


예를 들어, Bob의 정적 Address $B$는 스캔 공개 키와 사용 공개 키의 연결을 나타냅니다:


$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$


이러한 키는 다음 경로에서 간단히 파생됩니다:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


이 정적 Address은 Bob가 게시합니다. Alice은 이를 검색하여 Bob에게 조용한 지불을 합니다. 그녀는 이런 식으로 Bob의 지불금 Address $P_0$를 계산합니다:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$입니다


Where:


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A) $$


With:


- b_{\text{scan}}$: Bob의 스캔 공개키(정적 Address);
- b_{\text{spend}}$: Bob의 지출 공개키(정적 Address)입니다;

**$A$**: 입력(조정)된 공개 키의 합계입니다;


- $a$: 조정의 개인 키, 즉 Alice의 트랜잭션에서 입력으로 소비된 UTXO의 `scriptPubKey`에 사용된 모든 키 쌍의 합계입니다;
- 텍스트{아웃포인트}_L$: Alice의 트랜잭션에서 입력으로 사용되는 가장 작은 UTXO(사전적 의미)입니다;

**‖**: 연결(피연산자를 끝에서 끝까지 연결하는 작업);


- $G$: 타원형 커브 `secp256k1`의 생성점입니다;
- text{Hash}$: BIP0352/SharedSecret` 태그가 붙은 SHA256 Hash 함수입니다;
- $P_0$: Bob에 지불하기 위한 첫 번째 공개 키/고유 Address입니다;

**$0$**: 여러 개의 고유 결제 주소를 generate하는 데 사용되는 정수입니다.


Bob은 이런 식으로 Blockchain을 스캔하여 침묵의 지불을 찾습니다:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$입니다


With:


- b_{\text{scan}}$: Bob의 개인 스캔 키입니다.


자신에게 주소가 지정된 조용한 지불이 포함된 Address으로 $P_0$를 발견하면, Alice이 $P_0$로 보낸 자금을 사용할 수 있는 개인 키인 $p_0$를 계산합니다:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$입니다


With:


- b_{\text{spend}}$: Bob의 개인 지출 키입니다;
- n$: 타원형 곡선 `secp256k1`의 순서입니다.


이 기본 버전 외에도 스캔하는 동안 필요한 작업을 부당하게 늘리지 않고 여러 용도를 분리하기 위해 동일한 기본 정적 Address에서 여러 다른 정적 주소를 generate에 라벨을 사용할 수도 있습니다.