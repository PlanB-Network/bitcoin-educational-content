---
term: Label (silent payments)
definition: Silent Payments에서 용도를 분리하기 위해 파생된 정적 주소를 생성하는 데 사용되는 정수입니다.
---

자동 결제 프로토콜 내에서 레이블은 다른 많은 정적 주소를 생성하기 위해 초기 정적 Address을 수정하는 데 사용되는 정수입니다. 이러한 레이블을 사용하면 결제 감지(스캔)를 위한 운영 부담을 과도하게 늘리지 않으면서도 각 용도에 따라 다른 정적 주소를 사용하여 자동 결제를 통해 전송된 결제를 분리할 수 있습니다. Bob는 두 개의 공개 키, 즉 스캔용 $B_{\text{scan}}$과 지출용 $B_{\text{spend}}$로 구성된 정적 Address $B$를 사용합니다. B_{\text{scan}}$의 Hash과 스칼라 곱하기 생성점 $G$를 곱한 정수 $m$을 지출 공개 키 $B_{\text{spend}}$에 추가하여 일종의 새로운 지출 공개 키 $B_m$을 생성합니다:


$$ B_m = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$


예를 들어 첫 번째 키 $B_1$은 이러한 방식으로 얻습니다:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


이제 Bob에 의해 게시된 정적 Address는 $B_{\text{scan}}$과 $B_m$으로 구성됩니다. 예를 들어, 레이블이 $1$인 첫 번째 정적 Address가 됩니다:


$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$


라벨 $0$은 잔돈을 위해 예약되어 있으므로 라벨 $1$부터 시작합니다. Bob가 제공한 레이블이 지정된 정적 Address로 비트코인을 전송하려는 Alice은 $B_{\text{spend}}$ 대신 새로운 $B_1$을 사용해 고유 결제 Address $P_0$을 도출합니다:


$$ P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$입니다


실제로 Alice는 Bob이 제공한 정적 Address의 두 번째 부분, 즉 이 경우 $B_{\text{spend}}$가 아닌 $B_1$ 값을 사용하기 때문에 Bob이 Address이라는 레이블을 가지고 있다는 사실조차 모를 수 있습니다. Bob은 결제를 스캔할 때 항상 이러한 방식으로 $B_{\text{spend}}$와 함께 초기 정적 Address의 값을 사용합니다:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$입니다

그런 다음 각 출력에서 $P_0$에 대해 찾은 값을 하나씩 빼기만 하면 됩니다. 그런 다음 이러한 빼기 결과 중 하나가 Wallet에서 사용하는 레이블 중 하나의 값과 일치하는지 확인합니다. 예를 들어 레이블이 $1$인 출력 #4와 일치한다면, 이 출력은 $B_1$이라는 레이블이 붙은 정적 Address와 연결된 자동 결제임을 의미합니다:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


이는 다음과 같은 이유로 작동합니다:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


이 방법 덕분에 Bob은 기본 정적 Address에서 파생된 여러 정적 주소($B_1$, $B_2$, $B_3$...)를 사용하여($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$) 용도를 적절히 분리할 수 있습니다.


그러나 이러한 정적 주소의 분리는 개인 Wallet 관리 관점에서만 유효할 뿐, 신원 분리는 허용하지 않습니다. 모두 동일한 $B_{\text{scan}}$을 가지고 있기 때문에 모든 정적 주소를 함께 연결하여 단일 엔티티에 속한다고 추론하는 것은 매우 쉽습니다.