---
name: Labelling UTXO
description: UTXO에 올바르게 라벨을 붙이는 방법은 무엇인가요?
---
![cover](assets/cover.webp)


이 튜토리얼에서는 Bitcoin Wallet의 UTXO 라벨링과 Coin 제어에 대해 알아야 할 모든 것을 알아봅니다. 이러한 개념을 완전히 이해하기 위한 이론적인 부분부터 시작하여 기본 Bitcoin Wallet 소프트웨어에서 라벨을 구체적으로 사용하는 방법을 살펴보는 실습 부분으로 이동합니다.


## UTXO 라벨링이란 무엇인가요?

"라벨링"은 주석 또는 라벨을 Bitcoin Wallet 내의 특정 UTXO에 연결하는 기술입니다. 이러한 주석은 Wallet 소프트웨어에 의해 로컬에 저장되며 Bitcoin 네트워크를 통해 전송되지 않습니다. 따라서 라벨링은 개인 관리를 위한 도구입니다.


예를 들어, 찰스와 Bisq를 통해 P2P 거래에서 UTXO를 받은 경우, 'Bisq P2P 구매 찰스'라는 레이블을 지정할 수 있습니다.


라벨링을 사용하면 UTXO의 출발지 또는 목적지를 기억할 수 있어 자금 관리를 간소화하고 사용자의 개인 정보를 최적화할 수 있습니다. 라벨링은 "Coin 제어" 기능과 함께 사용하면 더욱 유용해집니다. Coin 제어는 양호한 Bitcoin 지갑에서 사용할 수 있는 옵션으로, 사용자가 트랜잭션을 생성할 때 입력으로 사용할 특정 UTXO를 수동으로 선택할 수 있는 기능을 제공합니다.


Coin 제어와 함께 UTXO 라벨링과 함께 Wallet를 사용하면 사용자가 트랜잭션의 UTXO를 정확하게 구분하고 선택할 수 있으므로 다른 출처의 UTXO를 병합하는 것을 방지할 수 있습니다. 이러한 방식은 사용자의 개인정보를 침해할 수 있는 트랜잭션 입력의 공통 Ownership를 제안하는 공통 입력 Ownership 휴리스틱(CIOH)과 관련된 위험을 줄여줍니다.


예를 들어, 제 신원을 알고 있는 규제된 Exchange 플랫폼에서 오는 UTXO과 결합하는 것을 피하고 싶다고 가정해 보겠습니다. KYC가 없는 UTXO과 KYC UTXO에 별도의 라벨을 붙이면 Coin 제어 기능을 사용하여 지출을 충족하기 위한 입력으로 어떤 UTXO을 소비할지 쉽게 식별할 수 있습니다.


## UTXO에 올바른 라벨을 붙이는 방법은 무엇인가요?

모든 사람에게 적합한 보편적인 UTXO 라벨링 방법은 없습니다. Wallet에서 쉽게 길을 찾을 수 있도록 라벨링 시스템을 정의하는 것은 사용자의 몫입니다.

라벨링의 중요한 기준은 UTXO의 출처입니다. Coin가 Wallet에 어떻게 도착했는지 간단히 표시해야 합니다. Exchange 플랫폼에서 온 것입니까? 고객의 청구서 정산? 피어 투 피어 Exchange인가요? 아니면 구매에서 발생한 변경 사항인가요? 따라서 지정할 수 있습니다:


- '출금 Exchange.com`;
- 결제 고객 데이비드`;
- `P2P 구매 찰스`;
- '소파 구매에서 변경'을 클릭합니다.

![labelling](assets/en/1.webp)

UTXO 관리를 세분화하고 Wallet 내에서 자금 분리 전략을 준수하려면 이러한 분리를 반영하는 추가 지표를 사용하여 레이블을 강화할 수 있습니다. Wallet에 혼합하고 싶지 않은 두 가지 범주의 UTXO가 포함되어 있는 경우, 라벨에 마커를 통합하여 이러한 그룹을 명확하게 구분할 수 있습니다.


이러한 구분 표시는 KYC UTXO(신원 확인)과 no-KYC(익명)를 구분하거나 전문 자금과 개인 자금을 구분하는 등 자체 기준에 따라 달라질 수 있습니다. 앞서 언급한 라벨의 예를 들면 다음과 같이 번역할 수 있습니다:


- `KYC - 출금 Exchange.com`;
- 'KYC - 결제 클라이언트 데이비드';
- 'NO KYC - P2P 구매 찰스';
- 'NO KYC - 소파 구매에서 변경'.

![labelling](assets/en/2.webp)

어쨌든 좋은 라벨링은 필요할 때 이해할 수 있는 라벨링이라는 점을 명심하세요. Bitcoin Wallet가 주로 저축을 목적으로 한다면 라벨은 수십 년 후에나 유용할 수 있습니다. 따라서 라벨이 명확하고 정확하며 포괄적인지 확인하세요.


또한 거래 전반에 걸쳐 Coin의 라벨링을 영구적으로 유지하는 것이 좋습니다. 예를 들어, KYC가 없는 UTXO을 통합하는 경우, 결과 UTXO을 단순히 '통합'이 아니라 구체적으로 'KYC 없는 통합'으로 표시하여 Coin의 출처를 명확히 추적할 수 있도록 해야 합니다.


마지막으로, 라벨에 날짜를 표시하는 것은 필수가 아닙니다. 대부분의 Wallet 소프트웨어에는 이미 거래 날짜가 표시되어 있으며, txid을 사용하여 Block explorer에서 언제든지 이 정보를 검색할 수 있습니다.


## 튜토리얼: 스펙터 데스크톱의 라벨링


스펙터 데스크톱에서 Wallet을 연결하고 연 다음 '주소' 탭을 선택합니다.


![labelling](assets/notext/3.webp)

여기에서 모든 주소 목록과 해당 주소에 잠긴 비트코인을 확인할 수 있습니다. 기본적으로 주소는 '레이블' 열 아래의 인덱스로 식별됩니다. 레이블을 변경하려면 레이블을 클릭하고 원하는 레이블을 입력한 다음 파란색 아이콘을 클릭하여 확인하면 됩니다.

![labelling](assets/notext/4.webp)


그러면 라벨이 주소 목록에 표시됩니다.


![labelling](assets/notext/5.webp)


수신 Address를 발신자와 공유할 때 미리 레이블을 지정할 수도 있습니다. 이렇게 하려면 '수신' 탭에 액세스하여 전용 필드에 라벨을 기록합니다.


![labelling](assets/notext/6.webp)


## 튜토리얼: 일렉트럼의 라벨링


일렉트럼 Wallet에서 Wallet에 로그인한 후 '기록' 탭에서 라벨을 할당할 트랜잭션을 클릭합니다.


![labelling](assets/notext/7.webp)


새 창이 열립니다. '설명' 상자를 클릭하고 레이블을 입력합니다.


![labelling](assets/notext/8.webp)


레이블을 입력한 후에는 이 창을 닫을 수 있습니다.


![labelling](assets/notext/9.webp)


라벨이 성공적으로 저장되었습니다. '설명' 탭에서 찾을 수 있습니다.


![labelling](assets/notext/10.webp)


Coin 제어를 수행할 수 있는 `코인` 탭의 `라벨` 열에서 라벨을 찾을 수 있습니다.


![labelling](assets/notext/11.webp)


## 튜토리얼: Green Wallet에 라벨 제작하기


Wallet 앱에서 Wallet에 액세스하여 라벨을 붙이려는 트랜잭션을 선택합니다. 그런 다음 작은 연필 아이콘을 클릭하여 라벨을 메모합니다.


![labelling](assets/notext/12.webp)


라벨을 입력한 다음 Green `저장` 버튼을 클릭합니다.


![labelling](assets/notext/13.webp)


거래 세부 정보와 Wallet의 대시보드에서 라벨을 찾을 수 있습니다.


![labelling](assets/notext/14.webp)


## 튜토리얼: 사무라이 Wallet에 라벨링하기


Samourai Wallet에서는 거래에 라벨을 할당할 수 있는 여러 가지 방법이 있습니다. 첫 번째 방법은 Wallet를 열고 라벨을 추가할 트랜잭션을 선택하는 것부터 시작합니다. 그런 다음 '메모' 상자 옆에 있는 '추가' 버튼을 누릅니다.


![labelling](assets/notext/15.webp)


레이블을 입력하고 파란색 '추가' 버튼을 클릭하여 확인합니다.


![labelling](assets/notext/16.webp)


거래 세부 정보뿐만 아니라 Wallet의 대시보드에서도 레이블을 찾을 수 있습니다.


![labelling](assets/notext/17.webp)

두 번째 방법은 화면 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 '미사용 거래 출력 표시' 메뉴를 클릭합니다.

![labelling](assets/notext/18.webp)


여기에서 Wallet에 있는 모든 UTXO의 종합 목록을 확인할 수 있습니다. 표시된 목록은 내 입금 계좌와 관련된 것이지만, 전용 메뉴에서 탐색하여 Whirlpool 계좌에 대해서도 이 작업을 복제할 수 있습니다.


그런 다음 레이블을 지정하려는 UTXO을 클릭한 다음 '추가' 버튼을 클릭합니다.


![labelling](assets/notext/19.webp)


라벨을 입력하고 파란색 '추가' 버튼을 클릭하여 확인합니다. 그러면 거래 세부 정보와 Wallet의 대시보드에서 라벨을 찾을 수 있습니다.


![labelling](assets/notext/20.webp)


## 튜토리얼: Sparrow wallet의 라벨 제작


Sparrow wallet 소프트웨어를 사용하면 여러 가지 방법으로 라벨을 할당할 수 있습니다. 가장 간단한 방법은 수신 Address을 발신자에게 전달할 때 미리 라벨을 추가하는 것입니다. 이렇게 하려면 `수신` 메뉴에서 `라벨` 필드를 클릭하고 원하는 라벨을 입력합니다. 이는 Address에 비트코인이 수신되는 즉시 소프트웨어 전체에서 보존되고 액세스할 수 있습니다.


![labelling](assets/notext/21.webp)


Address 수령 시 라벨링을 잊어버린 경우에도 나중에 '거래' 메뉴에서 라벨을 추가할 수 있습니다. '라벨' 열에서 거래를 클릭한 다음 원하는 라벨을 입력하기만 하면 됩니다.


![labelling](assets/notext/22.webp)


'주소' 메뉴에서 라벨을 추가하거나 수정하는 옵션도 있습니다.


![labelling](assets/notext/23.webp)


마지막으로 `UTXO` 메뉴에서 라벨을 볼 수 있습니다. Sparrow wallet는 레이블 뒤에 괄호 안에 출력물의 특성을 자동으로 추가하여 변경으로 인한 UTXO와 직접 수신한 UTXO를 구분할 수 있도록 도와줍니다.


![labelling](assets/notext/24.webp)