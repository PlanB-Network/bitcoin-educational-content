---
name: Breez
description: 사용자가 제어할 수 있는 Lightning Wallet.
---

![breez-cover](assets/cover.webp)




자체 보유 지갑은 비트코인을 가장 안전하게 보관할 수 있는 옵션이 되고 있으며, Bitcoin의 라이트닝 오버레이의 강력한 성능과 장점을 활용할 수 있습니다. 브리즈는 이러한 접근 방식 덕분에 이번 지갑 제품군에서 특히 돋보입니다.



## Breez Wallet란 무엇인가요?


Breez는 Breez에서 만든 자체 보관 Wallet로, 비트코인을 관리할 수 있는 동시에 혁신적인 기능을 하나의 애플리케이션에서 모두 제공합니다.


공식 다운로드 플랫폼에서 Android 및 iOS용 Breez Wallet를 다운로드할 수 있습니다. 이 튜토리얼에서는 Android 플랫폼에서 앱에 대한 실습을 진행합니다. 아래에 설명된 전체 프로세스는 iOS에서도 유효합니다.



⚠️ **중요**: 애플리케이션의 진위 여부와 향후 자산의 보안을 보장하기 위해 Google Play 스토어 또는 Apple 스토어와 같은 공식 플랫폼에서 애플리케이션을 다운로드하는 것이 필수적입니다.



여기 Android에서는 **Breez** 애플리케이션이 있습니다(Breez사의 다른 제품인 미스티 브리즈와 혼동하지 마세요).


![breez-wallet-ps](assets/fr/01.webp)



## Wallet 이해하기



Breez는 새 Wallet를 만들거나 기존 Lightning Wallet를 복원할 수 있는 옵션을 제공합니다. 이 튜토리얼에서는 새 Wallet를 만들겠습니다.



![creer-portefeuille](assets/fr/02.webp)



이것이 브리즈의 장점 중 하나입니다. 비트코인을 완전히 제어할 수 있는 열쇠를 가지고 있다는 점입니다. 여러분은 비트코인의 주인입니다.



⚠️ Breez Wallet은 현재 개발 중이므로 당분간은 적당한 금액으로 거래하는 것을 권장합니다.


![test-breez](assets/fr/03.webp)



> 키가 아니라 비트코인이 아닙니다.

Wallet는 Bitcoin 프로토콜과 직접 동기화되며 트랜잭션에 대한 활성 노드를 제공합니다.


![bitcoin-connexion](assets/fr/04.webp)


### 키 저장


Bitcoin/Lightning Wallet을 만들 때 가장 먼저 해야 할 일은 키를 저장하는 것입니다.


메뉴에서 **환경설정**을 아래로 스크롤한 다음 **보안**으로 이동합니다.


Breez를 사용하면 12개의 복구 단어를 Google 드라이브 또는 구성할 수 있는 원격 개인 서버에 저장할 수 있습니다.


그런 다음 **백업 변경** 옵션을 활성화하면 Wallet에 수동으로 저장할 수 있는 키워드가 표시됩니다.


![sécurité](assets/fr/06.webp)


그런 다음 지침에 따라 백업을 확인하고 원격 백업 계정을 Breez Wallet에 연결합니다.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

⚠️ **중요**: Breez Layer에 추가 보안을 추가하려면 PIN 코드를 정의하고 Wallet에 대한 액세스가 승인되었음을 인증하도록 설정할 수 있습니다.



### Breez로 첫 거래하기


브리즈는 애플리케이션에서 직관성을 우선시합니다. Wallet으로 첫 비트코인을 받는 것은 이보다 더 쉬울 수 없습니다. 홈페이지에서 **받기**를 클릭한 다음 비트코인을 받고 싶은 방법을 선택하세요.


Breez는 세 가지 옵션을 제공합니다:




- 라이트닝 또는 **ID** Invoice로 받습니다: generate을 Invoice로 바꾸고 돈을 받습니다.
- Bitcoin Address**를 통해 수신합니다: Bitcoin 메인 네트워크에서 트랜잭션으로 비트코인을 받습니다.
- Bitcoin** 구매하기: 브리즈에는 법정화폐로 직접 Bitcoin을 획득하는 방법이 통합되어 있습니다.



![receive-bitcoin](assets/fr/07.webp)



Invoice에 대한 설명을 입력한 다음 수령하고자 하는 금액을 입력합니다.



⚠️ 브리즈에서 첫 거래를 하려면 **2500 사토시**의 채널 개설 및 유지 수수료를 지불해야 합니다. 대부분의 라이트닝 지갑과 달리 브리즈는 전체 라이트닝 노드 인프라를 제공하므로 비트코인을 자유롭게 관리할 수 있습니다. 사용자는 자신만의 결제 채널을 개설해야 하며, 애플리케이션 내에서 라이트닝 노드와 직접 통신할 수 있는 자유를 누릴 수 있습니다.



*이 수수료는 Wallet*을 초기화할 때 한 번만 지불하면 되니 안심하세요


![receive-invoice](assets/fr/08.webp)


Invoice가 생성되면 이를 공유하거나 스캔하여 청구서를 결제하고 비트코인을 받을 수 있습니다.



브리즈에 비트코인을 보내는 것은 받는 것만큼이나 직관적입니다.


Breez는 비트코인을 전송할 수 있는 세 가지 옵션을 제공합니다.




- Invoice 또는 사용자 ID**를 붙여넣습니다: 라이트닝 Invoice를 결제합니다.
- 결제에 연결**: 세션을 생성하고 수신자를 세션에 초대하여 비트코인을 전송합니다.
- BTC Address으로 전송합니다: Bitcoin 메인 네트워크에서 트랜잭션.



![send-bitcoins](assets/fr/09.webp)



그런 다음 수취인의 세부 정보를 입력하거나 스캔하여 Invoice 결제를 시작하고 유효성을 검사합니다.



![validate-send](assets/fr/10.webp)



### 이 Wallet의 특별한 기능입니다.


브리즈는 비트코인을 보관하는 직관적인 Wallet을 넘어 혁신적인 생태계입니다.


애플리케이션에서 바로 유용한 서비스를 찾을 수 있습니다.





- 팟캐스트 듣기**: Breez는 팟캐스트 2.0 플레이어로, Bitcoin 기부로 좋아하는 크리에이터를 후원할 수 있습니다.


메뉴에서 **팟캐스트**를 선택한 다음 좋아하는 콘텐츠 크리에이터를 찾아서 찾아서 듣습니다.


![podcasts](assets/fr/11.webp)


기부를 통해 좋아하는 콘텐츠 크리에이터의 작품을 후원하세요.


![boost](assets/fr/12.webp)




- POS**: Breez는 비즈니스에 완벽하게 적응하여 애플리케이션 내에서 POS를 운영할 수 있습니다. 매장의 재고를 관리하고, 고객으로부터 결제를 받고, 모든 구매에 대해 generate 인쇄 가능한 인보이스를 받을 수 있습니다. 또한 Breez에서 지원하는 다양한 통화로 현지 통화를 찾을 수 있습니다.



환경설정 > 법정통화** 메뉴에서 통화를 사용자 지정할 수 있습니다.


![custom-fiat](assets/fr/13.webp)


POS(Point of Sale)** 메뉴에서 스토어에서 판매하는 품목을 구성할 수 있습니다.


![products](assets/fr/14.webp)


재고가 완료되면 해당 제품에 대해 고객에게 쉽게 Invoice를 부여하고 Bitcoin을 비즈니스에 적용할 수 있습니다.


![print-receipe](assets/fr/15.webp)




- 타사 서비스 액세스**: Breez는 Wallet을 벗어나지 않고도 더 많은 작업을 수행할 수 있는 타사 서비스를 통합합니다. 여기에는 Bitrefill, LN Markets, Wavlake, Fold, Fixed Float, The Bitcoin Company, Azteco, Boltz, Geyser, Lightsats, SMS Sats, LN.PIZZA, LNCAL이 포함됩니다.


![apps](assets/fr/16.webp)


### Breez의 강점


Breez는 자율성이 강점입니다. Breez의 인프라는 애플리케이션 내에서 상호 작용할 수 있는 기능 노드를 제공합니다(**개발자** 옵션). 또한 기본 구성을 자율적으로 사용자 지정할 수 있습니다:




- Bitcoin/라이트닝 노드에 연결: 메뉴 **환경설정 > 네트워크**.


![reseau](assets/fr/17.webp)




- 거래 수수료 사용자 지정하기: 메뉴 **환경설정 > 라이트닝 수수료**로 이동합니다.


![fees](assets/fr/18.webp)




- 결제 채널 관리하기: 메뉴 **환경설정 > 채널 닫기**.


![channels](assets/fr/19.webp)



⚠️ **중요**: 변경하기 전에 라이트닝 구성에 대한 경험이 어느 정도 있는 것이 좋습니다. 향후 거래는 수정한 내용에 직접적인 영향을 받으며 비트코인이 손실될 수 있습니다.



경험이 많은 경우 **환경설정>개발자** 메뉴에서 노드와 상호 작용할 수 있습니다.


여기에서 필요한 인수를 추가하여 실행할 수 있는 Lightning 명령줄을 찾을 수 있습니다.


![dev-mode](assets/fr/20.webp)


이제 브리즈 Wallet에 익숙해졌습니다. 이 글이 유용했다면 Green에 엄지손가락을 치켜주세요. 여러분의 의견을 듣고 싶습니다. 여러분의 의견을 기다리겠습니다!