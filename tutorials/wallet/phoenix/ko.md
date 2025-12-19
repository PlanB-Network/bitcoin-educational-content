---
name: Phoenix
description: Phoenix Wallet 설치 및 사용
---
![cover](assets/cover.webp)


![video](https://youtu.be/TpwnoPUyumA)


피닉스는 라이트닝 기반 소프트웨어 솔루션을 전문으로 하는 프랑스 회사 ACINQ에서 개발한 자체 보관형 라이트닝 Wallet 및 노드입니다. 비트코인을 제3자가 보관하는 Satoshi의 Wallet와 같은 커스터디 라이트닝 지갑과 달리, 피닉스는 사용자가 자신의 개인 키를 완전히 제어할 수 있습니다.


Phoenix는 휴대폰에 내장된 진정한 라이트닝 노드로 작동하며, ACINQ의 라이트닝 노드와 자동으로 채널을 엽니다. 이 애플리케이션은 모바일 지갑에 최적화된 Kotlin에서 Lightning Network의 크로스 플랫폼 구현인 Lightning-KMP를 기반으로 합니다. 다른 라이트닝 노드 솔루션과 달리 Phoenix는 관리를 크게 간소화합니다. 사용자는 채널 열기 및 닫기를 처리하거나, Bitcoin 노드를 실행하거나, Lightning Network에서 유동성을 관리할 필요가 없습니다. 피닉스는 이러한 모든 기술적 작업을 백그라운드에서 처리합니다.


이 애플리케이션은 모바일 라이트닝 지갑의 사용 편의성과 편리함을 진정한 개인 라이트닝 노드의 보안 및 주권과 결합한 애플리케이션입니다. Phoenix를 사용하면 유동적이고 직관적인 사용자 경험을 즐기면서 Lightning Network를 안전하고 효율적이며 자율적으로 사용할 수 있습니다.


그 대가로 특정 수수료가 부과됩니다:




- 라이트닝을 통해 전송하는 경우 금액의 0.4%에 4Sats 을 더한 금액이 부과됩니다;
- 라이트닝을 통해 현금을 수령해야 하는 경우 금액의 1%가 청구됩니다;
- 각 채널을 여는 데 드는 비용은 1000Sats입니다.


제 생각에 피닉스는 커스터디 라이트닝 지갑과 라이트닝 노드의 수동 관리 사이의 훌륭한 중간 솔루션이라고 생각합니다. 이 애플리케이션은 자신의 LND 또는 코어 라이트닝을 관리하는 세부 사항을 다루고 싶지 않은 초보자와 고급 사용자에게 똑같이 적합합니다. 사용 방법을 알아봅시다!


![Image](assets/fr/01.webp)


## 애플리케이션 설치


애플리케이션 스토어로 이동하여 Phoenix 를 설치합니다:




- Google Play 스토어](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet)에서;
- App Store](https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB)에서.


![Image](assets/fr/02.webp)


애플리케이션을 설치할 수도 있습니다(https://github.com/ACINQ/phoenix/releases)[GitHub 리포지토리에 있는 apk 파일과 함께].


![Image](assets/fr/03.webp)


## 포트폴리오 생성


애플리케이션이 시작되면 "*다음*" 버튼을 클릭하여 프레젠테이션을 건너뛴 다음 "*시작*"을 클릭합니다.


![Image](assets/fr/04.webp)


"*새 Wallet 만들기*"를 선택합니다.


![Image](assets/fr/05.webp)


이제 Lightning Wallet와 노드가 생성되었습니다.


![Image](assets/fr/06.webp)


## Mnemonic 문구 저장


시작하기 전에 12단어 Mnemonic 구문을 저장해야 합니다. 이 문구는 모든 비트코인에 대한 완전하고 제한 없는 액세스를 제공합니다. 이 문구를 알고 있는 사람은 휴대폰에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다.


이 12단어 문구는 휴대폰 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다.


종이에 적거나 보안을 강화하기 위해 스테인리스 스틸에 각인하여 화재, 홍수 또는 붕괴로부터 보호할 수 있습니다. Mnemonic의 매체 선택은 보안 전략에 따라 다르지만, 적당한 양을 포함하는 지출용 Wallet으로 Phoenix를 사용하는 경우에는 종이로도 충분합니다.


Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Interface 상단에 표시되는 "*Wallet 저장...*"이라는 메시지를 클릭합니다.


![Image](assets/fr/07.webp)


그런 다음 "*내 Wallet 저장하기*"를 클릭합니다.


![Image](assets/fr/08.webp)


그런 다음 "*내 키 보기*"를 클릭하고 Mnemonic 문구를 실제 매체에 저장합니다.


![Image](assets/fr/09.webp)


Interface 하단에 있는 두 개의 확인란을 체크하여 백업이 성공적으로 완료되었는지 확인합니다.


![Image](assets/fr/10.webp)


## 애플리케이션 설정


첫 거래를 하기 전에 Interface의 왼쪽 하단에 있는 톱니바퀴 아이콘을 클릭하여 설정을 사용자 지정할 수 있습니다.


![Image](assets/fr/11.webp)


"*표시*" 메뉴에서 애플리케이션 테마, Bitcoin에 사용되는 화폐 단위, 현지 법정 화폐를 선택할 수 있습니다.


![Image](assets/fr/12.webp)


"*결제 옵션*"에서는 Lightning 결제에 대한 다양한 고급 설정을 찾을 수 있습니다. 기본 설정을 그대로 유지할 수 있습니다.


![Image](assets/fr/13.webp)


"*채널 관리*"에서 라이트닝 채널을 개설할 때 지불할 수 있는 최대 수수료를 설정합니다.


![Image](assets/fr/14.webp)


"*접근 제어*" 메뉴에서 인증 시스템을 활성화하여 휴대폰에서 애플리케이션에 대한 액세스를 보호하는 것이 좋습니다. 이렇게 하면 잠금 해제된 휴대폰에 액세스할 수 있는 사람이 Phoenix에 액세스하여 비트코인을 훔치는 것을 방지할 수 있습니다.


![Image](assets/fr/15.webp)


"*일렉트럼 서버*" 메뉴에서 일렉트럼 서버가 있는 경우 해당 서버를 연결하여 트랜잭션을 브로드캐스트할 수 있습니다.


![Image](assets/fr/16.webp)


연결의 기밀성을 강화하려면 "*Tor*" 메뉴에서 Tor를 통한 연결을 활성화하세요. 토어를 사용하면 결제 속도가 약간 느려질 수 있고, 수신 시 Phoenix 애플리케이션을 포그라운드에서 열어두어야 하지만, 개인정보 보호가 크게 향상됩니다.


![Image](assets/fr/17.webp)


## 비트코인 On-Chain 받기


첫 사용 시에는 Phoenix Wallet에 On-Chain 자금을 충전하는 옵션이 있습니다. Lightning에서 직접 첫 입금을 할 수도 있지만(다음 섹션 참조), 두 경우 모두 첫 채널 개설에 대한 추가 수수료가 적용됩니다.


"*수신*" 버튼을 클릭합니다.


![Image](assets/fr/18.webp)


QR 코드를 왼쪽으로 스와이프하면 Bitcoin를 수신하는 Address이 표시됩니다. 해당 Address로 Phoenix에 입금하고자 하는 금액을 전송합니다.


![Image](assets/fr/19.webp)


On-Chain으로 받은 금액은 먼저 Wallet 잔액 아래에 보류 중으로 표시됩니다. 자금을 사용할 수 있으려면 3번의 확인이 필요합니다.


![Image](assets/fr/20.webp)


자금이 입금되면 피닉스는 자동으로 라이트닝 채널을 열어줍니다. 이제 Lightning Network를 통해 비트코인을 주고받을 수 있습니다.


![Image](assets/fr/21.webp)


## 라이트닝을 통해 비트코인 받기


Lightning Network을 통해 Sats를 수신하려면 "*수신*" 버튼을 클릭합니다.


![Image](assets/fr/22.webp)


피닉스가 라이트닝 Invoice를 생성합니다. 이를 스캔하거나 Sats을 전송하려는 사람에게 보낼 수 있습니다.


![Image](assets/fr/23.webp)


"*수정*" 버튼을 클릭하면 Invoice에서 결제자에게 표시되는 설명을 추가하고 결제자가 송금해야 하는 특정 금액을 정의할 수 있습니다.


![Image](assets/fr/24.webp)


위에서 언급한 일반 인보이스는 한 번만 사용할 수 있습니다. 재사용 가능한 결제 옵션의 경우 재사용 가능한 QR 코드를 사용할 수 있습니다(BOLT12 혜택).


![Image](assets/fr/25.webp)


Invoice 또는 BOLT12 오퍼가 결제되면 거래가 라이트닝 Wallet에 표시됩니다.


![Image](assets/fr/26.webp)


## 라이트닝을 통해 비트코인 보내기


이제 Phoenix에 Sats이 설치되었으므로 Lightning Network을 통해 결제할 준비가 되었습니다. "*송신*" 버튼을 클릭하여 시작하세요.


![Image](assets/fr/27.webp)


몇 가지 옵션을 사용할 수 있습니다. "*QR 코드 스캔*"을 클릭하면 Lightning Invoice, BOLT12 오퍼 또는 On-Chain 결제를 위한 수신 Address을 스캔할 수 있습니다.


![Image](assets/fr/28.webp)


Interface 상단의 필드에 있는 키보드를 통해 이 정보를 수동으로 입력하거나 Lightning Address(BOLT12 또는 LNURL)을 입력할 수도 있습니다. "*붙여넣기*" 버튼을 사용하여 정보를 직접 붙여넣을 수도 있습니다.


![Image](assets/fr/29.webp)


이 예에서는 Invoice을 10,000 Sats로 스캔했습니다. 결제하려면 "*결제*"를 클릭하기만 하면 됩니다.


![Image](assets/fr/30.webp)


거래가 완료되었습니다.


![Image](assets/fr/31.webp)


이제 Phoenix를 구성하고 사용하는 방법을 알게 되셨으니 축하드립니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지 손가락을 남겨 주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 공유해 주셔서 감사합니다!


한 단계 더 나아가 나만의 라이트닝 노드를 시작하기 위한 또 다른 혁신적이고 사용하기 쉬운 솔루션인 Alby Hub에 대한 튜토리얼을 확인해 보세요:


https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Lightning Network의 기술적 작동에 대해 자세히 알아보려면 Plan ₿ Academy 에 대한 Fanis Michalakis의 훌륭한 무료 교육을 확인할 수 있습니다:


https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb