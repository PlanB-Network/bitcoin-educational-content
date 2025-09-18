---
name: Blockstream Green - 2FA
description: Green Wallet에 2/2 Multisig 설정하기
---
![cover](assets/cover.webp)


___


***참고: 2025년 5월부터 2단계 인증(2FA)으로 보호되는 새 계정을 더 이상 활성화할 수 없습니다. 이 기능은 이전에 이 유형의 계정을 활성화한 사용자만 사용할 수 있습니다*


___


Software Wallet는 컴퓨터, 스마트폰 또는 기타 인터넷에 연결된 장치에 설치된 애플리케이션으로, Bitcoin Wallet 키를 관리하고 보호할 수 있게 해줍니다. 따라서 개인 키를 격리하는 하드웨어 지갑과 달리 'Hot' 지갑은 사이버 공격에 잠재적으로 노출된 환경에서 작동하므로 불법 복제 및 도난의 위험이 높아집니다.


소프트웨어 지갑은 특히 일상적인 거래에서 합리적인 양의 비트코인을 관리할 때 사용해야 합니다. 또한 Hardware Wallet에 대한 투자가 불균형적으로 보일 수 있는 제한된 Bitcoin 자산을 가진 분들에게도 흥미로운 옵션이 될 수 있습니다. 하지만 인터넷에 지속적으로 노출되기 때문에 장기 저축이나 거액의 자금을 보관하기에는 안전성이 떨어집니다. 후자의 경우 하드웨어 지갑과 같은 보다 안전한 솔루션을 선택하는 것이 가장 좋습니다.


이 튜토리얼에서는 Blockstream Green의 "*2FA*" 옵션을 사용하여 Wallet의 보안을 개선하는 방법을 보여드리겠습니다.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Blockstream Green 소개


Blockstream Green는 모바일과 데스크톱에서 사용할 수 있는 Software Wallet입니다. 이전에는 *Green Address*으로 알려졌던 이 Wallet은 2016년에 인수된 후 블록스트림 프로젝트가 되었습니다.


Green는 특히 사용하기 쉬운 애플리케이션으로, 초보자도 흥미롭게 사용할 수 있습니다. RBF(*Replace-by-fee*), 토르 연결 옵션, 자체 노드 연결 기능, SPV(*간편 결제 인증*), Coin 태깅 및 제어 등 좋은 Bitcoin Wallet의 모든 필수 기능을 제공합니다.


Blockstream Green은 기본 Blockchain 외에 블록스트림에서 빠른 속도를 위해 개발한 Liquid Network, Bitcoin, Sidechain도 지원합니다. 이 튜토리얼에서는 Bitcoin에만 초점을 맞추었지만, Green에서 Liquid을 사용하는 방법을 배우는 또 다른 튜토리얼도 만들었습니다:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig 옵션(2FA)


Green에서는 클래식 "*싱글시그*"를 만들 수 있습니다 Hot Wallet. 하지만 일상적인 관리를 복잡하게 만들지 않으면서 Hot Wallet의 보안을 강화하는 "*2FA Multisig*" 옵션도 있습니다.


따라서 2/2 Multisig Wallet을 설정하게 되는데, 이는 각 거래에 두 개의 키 서명이 필요하다는 의미입니다. 첫 번째 키는 12단어 또는 24단어 Mnemonic 문구에서 파생되며, 휴대폰의 PIN 코드를 사용하여 로컬로 보호됩니다. 이 키를 완전히 제어할 수 있습니다. 두 번째 키는 블록스트림 서버에서 보관하며 서명에 사용하려면 이메일, SMS, 전화로 받은 코드 또는 이 튜토리얼에서 살펴볼 것처럼 인증 애플리케이션(Authy, Google 인증 등)을 통해 인증이 필요합니다.


블록스트림 실패 시(예: 회사 파산 또는 두 번째 키를 보유한 서버가 파괴되는 경우) 자율성을 보장하기 위해 타임락 메커니즘이 Multisig에 적용됩니다. 이 메커니즘은 약 1년(또는 정확히 51,840블록) 후에 2/2 Multisig을 1/2 Multisig로 변환하며, 그 이후에는 Wallet에 로컬 키만 있으면 비트코인을 사용할 수 있습니다. 따라서 블록스트림 서버나 2단계 인증에 액세스하지 못하는 경우 최대 1년만 기다리면 블록스트림에 의존하지 않고도 애플리케이션에서 비트코인을 자유롭게 사용할 수 있습니다.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


이 방법은 Hot Wallet의 보안을 크게 강화하는 동시에 비트코인을 제어하고 일상적인 사용을 용이하게 합니다. 하지만 2FA의 보안을 유지하기 위해 정기적으로 타임락을 새로 고쳐야 합니다. 2단계 인증으로 자금이 보호되는 360일 카운트다운은 비트코인을 받는 즉시 시작됩니다. 수령 후 360일이 지나도 이 자금을 사용한 거래를 수행하지 않으면 비트코인은 2FA 없이 로컬 키로만 보호됩니다.


이러한 제약으로 인해 2FA 옵션은 정기적인 거래가 타임락을 자동으로 갱신하는 지출 Wallet에 더 적합합니다. 장기 저축 Wallet의 경우, 타임록이 만료되기 전에 매년 본인에게 전면 거래를 해야 하므로 문제가 될 수 있습니다.


이 보안 방법의 또 다른 단점은 소수의 스크립트 템플릿을 사용해야 한다는 것입니다. 즉, 개인정보 보호 관점에서 볼 때 사용자와 동일한 유형의 스크립트를 사용하는 사람은 극소수이므로 외부 관찰자가 Wallet 지문을 쉽게 식별할 수 있습니다. 또한 이러한 스크립트는 크기가 크기 때문에 거래 비용이 더 많이 발생합니다.


2FA 옵션을 사용하지 않고 단순히 "*싱글시그*"를 설정하려는 경우 Wallet을 설정하려면 이 다른 튜토리얼을 참조하시기 바랍니다:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Blockstream Green 소프트웨어 설치 및 구성


첫 번째 단계는 물론 Green 애플리케이션을 다운로드하는 것입니다. 애플리케이션 스토어로 이동합니다:



- [Android용](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


안드로이드 사용자의 경우, '.apk' 파일[블록스트림의 깃허브에서 다운로드 가능](https://github.com/Blockstream/green_android/releases)을 통해 애플리케이션을 설치할 수도 있습니다.


![GREEN 2FA MULTISIG](assets/fr/04.webp)


애플리케이션을 실행한 다음 "조건에 동의합니다..." 상자에 체크합니다.


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Green을 처음 열면 구성된 Wallet가 없는 홈 화면이 나타납니다. 나중에 지갑을 만들거나 가져오면 이 Interface에 지갑이 표시됩니다. Wallet를 만들기 전에 필요에 맞게 애플리케이션 설정을 조정하는 것이 좋습니다. "애플리케이션 설정"을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Android에서만 사용할 수 있는 '*개인정보 보호 강화*' 옵션은 스크린샷을 비활성화하고 애플리케이션 미리보기를 숨겨 개인 정보 보호를 강화합니다. 또한 휴대폰이 잠기는 즉시 애플리케이션 액세스를 자동으로 잠그기 때문에 데이터가 노출되기 어렵습니다.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


개인 정보 보호를 강화하고자 하는 분들을 위해, 모든 연결을 암호화하고 활동을 추적하기 어렵게 만드는 네트워크인 토르를 통해 트래픽을 루팅할 수 있는 옵션을 제공합니다. 이 옵션을 사용하면 애플리케이션의 작동 속도가 약간 느려질 수 있지만, 특히 완전한 노드를 사용하지 않는 경우 개인 정보를 보호하기 위해 적극 권장합니다.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


자체 완전한 노드를 보유한 사용자의 경우 Green Wallet은 일렉트럼 서버를 통해 연결할 수 있는 가능성을 제공하여 Bitcoin 네트워크 정보 및 트랜잭션 배포에 대한 완전한 제어를 보장합니다.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


또 다른 대안 기능으로는 "*SPV 검증*" 옵션이 있는데, 이 방법은 Full node의 모든 보증을 제공하지는 않지만 특정 Blockchain 데이터를 직접 검증하여 블록스트림의 기본 노드를 신뢰할 필요성을 줄일 수 있습니다.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


이러한 설정을 필요에 맞게 조정했으면 '*저장*' 버튼을 클릭하고 애플리케이션을 다시 시작합니다.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Blockstream Green에 Bitcoin Wallet 만들기


이제 Bitcoin Wallet을 만들 준비가 되었습니다. "*시작하기*" 버튼을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/12.webp)


로컬 Software Wallet을 만들거나 Hardware Wallet을 통해 Cold Wallet를 관리하는 방법 중 하나를 선택할 수 있습니다. 이 튜토리얼에서는 Hot Wallet를 만드는 데 집중할 것이므로 "*이 장치에서*" 옵션을 선택해야 합니다.


![GREEN 2FA MULTISIG](assets/fr/13.webp)


그런 다음 기존 Bitcoin Wallet를 복원하거나 새로 만들도록 선택할 수 있습니다. 이 튜토리얼에서는 새 Wallet를 만들겠습니다. 그러나 기존 휴대폰을 분실한 경우와 같이 기존 Bitcoin Wallet를 Mnemonic 문구에서 재생성해야 하는 경우에는 두 번째 옵션을 선택해야 합니다.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


그런 다음 12단어 또는 24단어 Mnemonic 문구 중에서 선택할 수 있습니다. 이 문구를 사용하면 휴대폰에 문제가 발생할 경우 호환되는 모든 소프트웨어에서 Wallet에 대한 액세스 권한을 복구할 수 있습니다. 현재로서는 24단어 비밀번호를 선택해도 12단어 비밀번호보다 보안이 더 강화되지 않습니다. 따라서 12단어 Mnemonic 문구를 선택하는 것이 좋습니다.


그러면 Green이 Mnemonic 문구를 제공합니다. 계속하기 전에 감시당하고 있지 않은지 확인하세요. "*복구 문구 표시*"를 클릭하여 화면에 표시합니다.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**이 Mnemonic는 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다**. 이 문구를 소유한 사람은 휴대폰에 물리적으로 액세스하지 않아도 자금을 훔칠 수 있습니다(Green의 2/2 Wallet의 경우 만료된 타임락 또는 2FA가 적용됨).


휴대폰 분실, 도난 또는 파손 시 로컬 키에 대한 액세스를 복원할 수 있습니다. 따라서 디지털이 아닌 물리적 매체에** 신중하게 백업하고 안전한 장소에 보관하는 것이 매우 중요합니다. 종이에 적어두거나, 보안을 강화하기 위해 대형 Wallet의 경우 스테인리스 스틸 지지대에 새겨 화재, 홍수 또는 붕괴의 위험으로부터 보호하는 것이 좋습니다(소량의 비트코인을 보호하도록 설계된 Hot의 경우 간단한 종이 백업으로도 충분할 것입니다).


*물론 이 튜토리얼에서처럼 인터넷에서 이러한 단어를 공유해서는 안 됩니다. 이 샘플 Wallet는 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Mnemonic 문구를 실제 매체에 올바르게 녹음했으면 "*계속*"을 클릭합니다. 그러면 Green Wallet이 Mnemonic 문구의 일부 단어를 확인하여 올바르게 녹음했는지 여부를 묻습니다. 누락된 단어로 빈칸을 채우세요.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Green Wallet의 잠금을 해제하는 데 사용되는 장치의 PIN 코드를 선택합니다. 이는 무단 물리적 액세스로부터 기기를 보호하기 위한 것입니다. 이 PIN 코드는 Wallet의 암호화 키 생성에 관여하지 않습니다. 따라서 이 PIN 코드에 액세스할 수 없더라도 12단어 또는 24단어 Mnemonic 문구를 소지하고 있으면 로컬 키에 다시 액세스할 수 있습니다.


가능한 한 무작위로 6자리 PIN 코드를 선택하는 것이 좋습니다. 이 코드를 잊어버리지 않도록 저장해 두지 않으면 Mnemonic에서 Wallet을 검색해야 합니다. 그런 다음 생체 인식 차단 옵션을 추가하여 매번 비밀번호를 입력하지 않아도 됩니다. 일반적으로 생체 인식은 PIN 자체보다 훨씬 덜 안전합니다. 따라서 기본적으로 이 잠금 해제 옵션을 설정하지 않는 것이 좋습니다.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


비밀번호를 한 번 더 입력하여 확인합니다.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Wallet가 생성될 때까지 기다렸다가 "*계정 만들기*" 버튼을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/20.webp)


그런 다음 표준 단일 서명 Wallet 또는 2단계 인증(2FA)으로 보호되는 Wallet 중에서 선택할 수 있습니다. 이 튜토리얼에서는 두 번째 옵션을 선택하겠습니다.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


이제 Green 애플리케이션을 사용하여 Bitcoin Multisig Wallet을 생성했습니다!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## 2FA 설정


계정을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


"*2FA를 추가하여 계정 보안 강화*" 버튼을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/24.webp)


그런 다음 2/2 Multisig의 두 번째 키에 액세스하기 위한 인증 방법을 선택할 수 있습니다. 이 튜토리얼에서는 인증 애플리케이션을 사용하겠습니다. 이러한 유형의 애플리케이션에 익숙하지 않다면 Authy 튜토리얼을 참조하시기 바랍니다:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

"*인증자 애플리케이션*"을 선택합니다.


![GREEN 2FA MULTISIG](assets/fr/25.webp)


그러면 Green에 QR 코드와 복구 키가 표시됩니다. 이 키를 사용하면 Authy 애플리케이션 분실 시 2FA에 대한 액세스를 복원할 수 있습니다. 위에서 설명한 대로 타임락이 만료된 후에도 비트코인에 대한 액세스를 복구할 수 있지만, 이 키를 안전하게 백업해 두는 것이 좋습니다.


인증 애플리케이션에서 새 코드를 추가한 다음 Green에서 제공하는 QR 코드를 스캔합니다.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*이 튜토리얼에서 설명하는 것처럼 이 키와 QR 코드를 인터넷에서 절대 공유해서는 안 됩니다. 이 샘플 Wallet는 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다*


"*계속*" 버튼을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/27.webp)


인증 애플리케이션에 있는 6자리 동적 코드를 입력합니다.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


이제 2단계 인증이 활성화되었습니다.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


이 메뉴에서 타임락 기간을 설정할 수도 있습니다. 이 카운트다운은 비트코인을 받는 즉시 시작되며, 타임락이 만료되면 2FA 없이도 로컬 키로만 자금을 사용할 수 있습니다. 기본 기간은 12개월로 설정되어 있지만, 저축형 Wallet의 경우 타임락 갱신 빈도를 최소화하기 위해 15개월을 선택하는 것이 좋습니다. 반대로 지출 Wallet의 경우 일일 거래에 따라 타임락이 자주 갱신되고 2FA에 문제가 발생할 경우 타임락이 짧을수록 대기 시간이 줄어들기 때문에 6개월의 타임락이 더 바람직할 수 있습니다. 가장 적합한 타임락 기간을 결정하는 것은 회원님의 몫입니다.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


이제 이 메뉴를 종료할 수 있습니다. Multisig Wallet이 준비되었습니다!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Blockstream Green에서 Wallet 설정하기


Wallet을 맞춤 설정하려면 오른쪽 상단에 있는 작은 점 3개를 클릭하세요.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


"*이름 바꾸기*" 옵션을 사용하면 Wallet의 이름을 사용자 지정할 수 있으며, 동일한 애플리케이션에서 여러 지갑을 관리하는 경우 특히 유용합니다.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


"*단위*" 메뉴에서는 Wallet의 기본 단위를 변경할 수 있습니다. 예를 들어 비트코인이 아닌 사토시로 표시하도록 선택할 수 있습니다.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


"*설정*" 메뉴에서는 Bitcoin Wallet의 다양한 옵션에 액세스할 수 있습니다.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


예를 들어, 여기에서 확장 공개 키와 *Descriptor*을 찾을 수 있는데, 이 Wallet에서 감시 전용 모드로 Wallet을 설정하려는 경우 유용합니다.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Wallet PIN을 변경하고 생체 인식 연결을 활성화할 수도 있습니다.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Blockstream Green 사용


이제 Bitcoin Wallet이 설정되었으니 첫 번째 Sats를 받을 준비가 되었습니다! "*수신*" 버튼을 클릭하기만 하면 됩니다.


![GREEN 2FA MULTISIG](assets/fr/38.webp)


그러면 Green에 Address를 수신하는 첫 번째 공백이 표시됩니다. 연결된 QR 코드를 스캔하거나 Address를 직접 복사하여 비트코인을 보낼 수 있습니다. 이 유형의 Address는 송금자가 송금할 금액을 지정하지 않습니다. 하지만 특정 금액을 요청하는 generate은 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 "*요청 금액*"을 클릭하고 원하는 금액을 입력하면 됩니다.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


트랜잭션이 네트워크에서 브로드캐스트되면 Wallet에 표시됩니다.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


거래가 확정된 것으로 간주할 수 있을 만큼 충분한 확인을 받을 때까지 기다리세요.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Wallet에 비트코인이 있으면 이제 비트코인을 보낼 수도 있습니다. "*송금*"을 클릭합니다.


![GREEN 2FA MULTISIG](assets/fr/42.webp)


다음 페이지에서 수신자의 Address를 입력합니다. 수동으로 입력하거나 QR 코드를 스캔할 수 있습니다.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


결제 금액을 선택합니다.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


화면 하단에서 이 거래에 대한 수수료율을 선택할 수 있습니다. 애플리케이션의 권장 사항을 따르거나 수수료를 사용자 지정할 수 있습니다. 보류 중인 다른 거래와 비교하여 수수료가 높을수록 거래가 더 빨리 처리됩니다. 수수료 시장 정보는 [Mempool.space](https://Mempool.space/)의 "*거래 수수료*" 섹션에서 확인하시기 바랍니다.


![GREEN 2FA MULTISIG](assets/fr/45.webp)


"*다음*"을 클릭하여 거래 요약 화면에 액세스합니다. Address, 금액 및 요금이 정확한지 확인합니다.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


모든 것이 순조롭게 진행되면 화면 하단의 Green 버튼을 오른쪽으로 밀어서 Bitcoin 네트워크에서 트랜잭션에 서명하고 브로드캐스트합니다.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


이때 인증 코드를 입력해야 블록스트림이 보유한 두 번째 Multisig 키의 잠금을 해제할 수 있습니다. 인증 애플리케이션에 표시된 6자리 코드를 입력합니다.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


이제 거래가 Bitcoin Wallet 대시보드에 표시되어 확인을 기다립니다.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


이제 Blockstream Green의 2FA 옵션을 사용하여 2/2 Multisig Wallet를 쉽게 설정하는 방법을 알게 되었습니다!


이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


또한 Blockstream Green 모바일 애플리케이션에 대한 다른 포괄적인 튜토리얼을 확인하여 Liquid Wallet 을 설정하는 것이 좋습니다:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a