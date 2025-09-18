---
name: Sentinel
description: Watch-only wallet이란 무엇이며 어떻게 사용하나요?
---

![cover](assets/cover.webp)


---

**\*경고:** 4월 24일 사무라이 Wallet의 설립자가 체포되고 서버가 압수된 이후에도 센티넬 앱은 계속 작동하지만, **Blockchain 정보 및 방송 거래에 액세스하려면 **자신의 도장을 사용**해야 합니다.\*


저희는 이 사건의 전개 상황과 관련 도구의 개발 상황을 면밀히 주시하고 있습니다. 새로운 정보가 입수되는 대로 이 튜토리얼을 업데이트할 예정이니 안심하세요


이 튜토리얼은 교육 및 정보 제공 목적으로만 제공됩니다. 범죄 목적으로 이러한 도구를 사용하는 것을 보증하거나 권장하지 않습니다. 해당 관할 지역의 법률을 준수하는 것은 각 사용자의 책임입니다


---

> 개인 키를 비공개로 유지하세요.

이 도움말에서는 시계 전용 지갑에 대해 알아야 할 모든 것을 살펴봅니다. 작동 방식에 대해 설명하고 시중에 나와 있는 다양한 애플리케이션을 살펴봅니다. 마지막으로 가장 인기 있는 Watch-only wallet 애플리케이션 중 하나에 대한 자세한 튜토리얼을 제공합니다: 센티널.


## Watch-only wallet란 무엇인가요?


Watch-only wallet 또는 읽기 전용 Wallet은 사용자가 해당 개인 키에 액세스하지 않고도 하나 이상의 특정 Bitcoin 공개 키와 관련된 트랜잭션을 관찰할 수 있도록 설계된 소프트웨어 유형입니다.


이 유형의 애플리케이션은 잔액과 거래 내역 보기 등 Bitcoin Wallet 모니터링에 필요한 데이터만 보관할 뿐, 개인 키에는 액세스할 수 없습니다. 따라서 시계 전용 애플리케이션에서 Wallet에 보관된 비트코인을 사용할 수 없습니다.

![watch-only](assets/en/1.webp)

감시 전용은 일반적으로 Hardware Wallet과 함께 사용됩니다. 이를 통해 인터넷에 연결되지 않은 장치에 Wallet의 개인 키 'Cold'를 저장할 수 있으므로 공격 표면이 최소화되어 잠재적으로 취약한 환경으로부터 개인 키를 격리할 수 있습니다. 반면에 감시 전용 애플리케이션은 Bitcoin Wallet의 확장 공개 키(`xpub`, `zpub` 등)를 독점적으로 저장합니다. 이 부모 키는 연결된 개인 키를 검색할 수 없으므로 결과적으로 비트코인의 사용을 허용하지 않습니다. 그러나 하위 공개 키와 수신 주소를 파생할 수 있습니다. 감시 전용 애플리케이션은 Hardware Wallet에 의해 보호되는 Wallet의 주소에 대한 지식을 통해 Bitcoin 네트워크에서 이러한 거래를 추적하여 사용자가 매번 Hardware Wallet에 연결하지 않고도 잔액과 generate 새 수신 주소를 모니터링할 수 있는 기능을 제공할 수 있습니다.


## 어떤 Watch-only wallet를 사용해야 하나요?


현재 가장 포괄적인 시계 전용 애플리케이션은 사무라이 Wallet 팀이 개발한 [Sentinel](https://sentinel.watch/)입니다. 이 앱은 좋은 Watch-only wallet에 필요한 모든 필수 기능을 포함하고 있습니다:



- 확장 키, 공개 키 및 주소 지원;
- 여러 계정 또는 지갑을 컬렉션으로 구성할 수 있는 기능입니다;
- 비트코인을 직접 사용하지 않고도 Hardware Wallet에서 비트코인을 받을 수 있는 주소 생성;
- 오프라인에서 트랜잭션을 구성하고 브로드캐스트할 수 있는 기능입니다;
- 자체 Bitcoin 노드에 연결할 수 있는 옵션입니다;
- 개인 정보 보호 강화를 위한 토르 통합.

센티널의 고유한 단점은 애플리케이션이 Android 전용이며 다중 서명 지갑을 지원하지 않는다는 점입니다. 따라서 Android 기기를 소유하고 있고 Wallet이 클래식 단일 서명인 경우 Sentinel을 추천합니다.

멀티서명 Wallet을 추적하고자 하는 분들을 위해 제가 아는 한 이러한 유형의 지갑에 시계 전용 모드를 제공하는 애플리케이션은 Blue Wallet이 유일하며, Android와 iOS 모두에서 액세스할 수 있습니다.


센티널의 대안을 찾는 iOS 사용자의 경우, [Green Wallet](https://blockstream.com/Green/) 또는 [Blue Wallet](https://bluewallet.io/watch-only/)가 옵션이 될 수 있지만 시계 전용 기능은 센티널만큼 포괄적이지는 않습니다.

![watch-only](assets/notext/2.webp)


## 센티널 Watch-only wallet는 어떻게 사용하나요?


### 설치 및 설정


먼저 센티널 애플리케이션을 설치합니다. Google Play 스토어 또는 [공식 웹사이트에서 다운로드할 수 있는 APK](https://sentinel.watch/download/)를 사용하여 설치할 수 있습니다.


![watch-only](assets/notext/3.webp)


애플리케이션을 처음 열면 다음 중 하나를 선택할 수 있습니다:



- '도장에 연결'을 클릭합니다;
- '사무라이 서버에 연결'을 클릭합니다.


사무라이 팀이 개발한 Dojo는 독립적으로 설치하거나 [엄브렐](https://umbrel.com/) 및 [로닌도조](https://ronindojo.io/)와 같은 노드 인 박스 솔루션에 클릭 한 번으로 추가할 수 있는 풀 Bitcoin 노드 버전입니다.


[**-> 라즈베리파이에 로닌도조 v2를 설치하는 방법을 알아보세요.**](https://planb.network/tutorials/node/Bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


자신의 도장이 있는 경우, 이 단계에서 연결할 수 있습니다. 이렇게 하면 Bitcoin 네트워크 거래 정보를 확인할 때 최고 수준의 개인정보 보호 혜택을 누릴 수 있습니다.


![watch-only](assets/notext/4.webp)


그렇지 않으면 사무라이의 기본 서버를 선택할 수 있습니다. 토르를 통해 연결할지 여부를 선택할 수도 있습니다.


![watch-only](assets/notext/5.webp)


그러면 Sentinel의 메인 페이지로 이동합니다.


![watch-only](assets/notext/6.webp)


시작하려면 애플리케이션을 설정하면 됩니다. 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 '설정'을 클릭합니다.


![watch-only](assets/notext/7.webp)

'사용자 PIN 코드'를 선택하면 Watch-only wallet에 대한 보안 액세스를 위해 비밀번호를 설정할 수 있습니다. 또한 잔액을 법정화폐로 변환할 때 기준 통화를 변경하거나 '법정화폐 값 숨기기' 옵션을 활성화하여 법정화폐 값을 숨길 수도 있습니다. 보안을 강화하기 위해 '스크린샷 비활성화'를 활성화하면 센티넬 애플리케이션의 스크린샷을 방지하여 외부 화면에 정보가 공개되지 않도록 할 수 있습니다.

![watch-only](assets/notext/8.webp)


이 설정 메뉴에는 센티널을 백업하는 옵션도 있습니다.


### Watch-only wallet 사용


홈페이지에서 파란색 `새로 만들기` 버튼을 눌러 추적할 새 확장 공개키를 추가합니다. 그런 다음 키의 QR 코드를 스캔하거나 'Pubkey 붙여넣기'를 선택해 키(`xpub`, `zpub`...)를 직접 붙여넣을 수 있습니다.


![watch-only](assets/notext/9.webp)


일반적으로 Wallet의 `xpub`은 사용 중인 Wallet 관리 소프트웨어를 통해 직접 액세스할 수 있습니다. 예를 들어 Sparrow로 Hardware Wallet을 관리하는 경우 이 정보는 `설정` 탭의 `키스토어` 섹션 아래에서 확인할 수 있습니다.


![watch-only](assets/notext/10.webp)


Sentinel에 확장 공개 키를 입력하면 애플리케이션에서 새 컬렉션을 만들 수 있습니다. 컬렉션은 함께 구성된 확장 공개 키 집합을 나타냅니다. 이 옵션을 사용하면 모든 '공개키'를 나열할 수 있을 뿐만 아니라 순서대로 분류할 수 있습니다. 예를 들어, 여러 계정(예금, 프리믹스, 포스트믹스...)이 있는 사무라이 Wallet이 있다면 이 모든 계정을 '사무라이' 컬렉션 아래에 모을 수 있습니다. 가족을 위해 관리하는 지갑의 경우 '가족'이라는 이름의 컬렉션을 만들 수 있습니다.


'새 컬렉션 만들기'를 선택합니다. 그런 다음 방금 통합한 확장 키의 이름을 입력합니다. 예를 들어, 사무라이 Wallet의 예금 계좌를 스캔하면 이 키의 이름을 '예금'으로 지정합니다. 저장`을 클릭하여 완료합니다.


![watch-only](assets/notext/11.webp)


그런 다음 이 컬렉션에 이름을 지정하고 화면 오른쪽 상단에 있는 유효성 검사 아이콘을 눌러 컬렉션을 저장합니다. 이제 센티널 홈 화면에 컬렉션이 표시됩니다.


![watch-only](assets/notext/12.webp)


다른 확장 공개키를 추가하려면 '새로 만들기'를 다시 클릭하고 키를 입력합니다.


![watch-only](assets/notext/13.webp)

그러면 이 키를 통합할 컬렉션을 선택하거나 새 컬렉션을 만들라는 메시지가 표시됩니다. 예를 들어, 제 경우에는 Ledger Wallet 전용 컬렉션을 설정했습니다.

![watch-only](assets/notext/14.webp)


컬렉션의 확장 키를 자세히 보려면 해당 키를 클릭하기만 하면 됩니다. 그런 다음 여러 탭을 탐색하여 거래 내역을 볼 수 있습니다.


![watch-only](assets/notext/15.webp)


컬렉션에서 오른쪽 상단의 작은 점 세 개를 탭한 다음 '미사용 출력 보기'를 탭하면 추적된 Wallet이 보유한 UTXO 목록에 액세스할 수 있습니다.


![watch-only](assets/notext/16.webp)


### 센티널에서 비트코인 보내기 및 받기


다른 좋은 Watch-only wallet와 마찬가지로 센티넬을 사용하면 추적된 Wallet에서 비트코인을 받을 수 있는 generate 수신 주소를 생성할 수 있습니다. 하지만 Sentinel은 또 다른 고급 기능인 Partially Signed Bitcoin Transaction(PSBT)의 생성 및 브로드캐스트 기능도 제공합니다. 따라서 개인 키를 보유한 Wallet는 이 트랜잭션에 서명할 수 있으며, 서명이 완료되면 Sentinel에 의해 Bitcoin 네트워크에 브로드캐스트될 수 있습니다. 이 모든 작업을 수행하는 방법을 살펴봅시다.


**주의: Wallet이 직접 확인하지 않은 Address에서 비트코인을 받는 것은 권장하지 않습니다.** Hardware Wallet와 같이 개인 키를 보유한 Wallet이 특정 Address이 소속되어 있음을 명시적으로 확인하지 않은 경우, 이 Address에게 비트코인을 보내는 것은 위험한 행위입니다. 실제로 이러한 확인 없이는 Address이 실제로 Wallet의 소유라는 보장이 없습니다. 따라서 Watch-only wallet의 수신 기능은 송금한 자금이 손실될 수 있다는 점을 염두에 두고 신중하게 사용해야 합니다.


센티널을 통해 비트코인을 받으려면 관심 컬렉션을 선택한 다음 자금을 이체할 확장 공개 키에 해당하는 탭을 클릭합니다.


![watch-only](assets/notext/17.webp)


마지막으로 화면 왼쪽 하단의 화살표 아이콘을 클릭합니다. 그러면 Sentinel에서 빈 수신 Address을 생성합니다. 이를 복사하거나 QR 코드를 사용하여 스캔할 수 있습니다.


![watch-only](assets/notext/18.webp)


센티널에서 generate를 PSBT로 전송하여 지출 거래를 시작하려면 결제하려는 Wallet의 확장 키로 이동하세요. 예를 들어 사무라이 Wallet의 예금 계좌를 예로 들어 보겠습니다. 그런 다음 화면 오른쪽 하단에 있는 화살표 아이콘을 클릭합니다.


![watch-only](assets/notext/19.webp)


거래와 관련된 모든 매개변수를 입력합니다:



- 받는 사람의 Address를 입력합니다(QR코드 아이콘을 클릭하면 이 Address를 스캔할 수 있는 옵션이 있습니다);
- 이 Address으로 전송할 금액을 지정합니다;
- 거래 수수료를 결정합니다.


거래에 필요한 모든 필드를 입력한 후 '서명되지 않은 거래 작성' 버튼을 누릅니다.


![watch-only](assets/notext/20.webp)


그러면 Sentinel이 개인 키에 액세스할 수 없으므로 구성되었지만 서명되지 않은 Bitcoin 트랜잭션을 나타내는 PSBT에 액세스하게 됩니다. 이 트랜잭션을 복사하거나, '.PSBT' 파일로 내보내거나, 애니메이션 QR 코드를 통해 스캔할 수 있는 옵션이 있습니다.


![watch-only](assets/notext/21.webp)


그런 다음 거래에 서명할 개인 키가 있는 Wallet로 이동합니다(사무라이, Hardware Wallet...).


![watch-only](assets/notext/22.webp)


트랜잭션이 서명되면 Sentinel로 돌아와서 브로드캐스트할 수 있습니다. 이렇게 하려면 홈 메뉴에서 오른쪽 상단의 작은 점 세 개를 클릭한 다음 '트랜잭션 브로드캐스트'를 클릭합니다.


![watch-only](assets/notext/23.webp)


서명된 PSBT을 세 가지 방법으로 입력할 수 있습니다:



- 클립보드에서 직접 붙여넣습니다;
- .PSBT` 파일에서 가져옵니다;
- QR 코드를 통해 스캔하면 됩니다.


![watch-only](assets/notext/24.webp)


회색 프레임에 서명된 트랜잭션을 입력한 후, Green '브로드캐스트 트랜잭션' 버튼을 클릭하여 Bitcoin 네트워크에 브로드캐스트할 수 있습니다. 센티널이 txid를 제공합니다.


![watch-only](assets/notext/25.webp)