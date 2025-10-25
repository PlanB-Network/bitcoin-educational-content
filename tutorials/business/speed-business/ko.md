---
name: Speed Wallet - POS
description: Bitcoin 및 스테이블코인 결제를 비즈니스에 쉽게 통합하세요
---
![cover](assets/cover.webp)



Bitcoin의 전 세계적인 채택은 일상 생활에서의 실질적인 사용 사례를 기반으로 합니다. 전 세계의 즉석 상거래에서 Bitcoin를 사용하는 것은 대형 기관과 소규모 기업 모두에서 이러한 채택을 강화합니다. 이 튜토리얼에서는 라이트닝을 통해 Bitcoin 결제를 수락할 수 있는 통합 결제 플랫폼인 Speed Business에 대해 살펴보겠습니다.



![btc-session](https://www.youtube.com/watch?v=ywUNZ_sxr0Q)



## 스피드 비즈니스 시작하기



[스피드 비즈니스](https://www.tryspeed.com/)는 [스피드 Wallet](https://www.speed.app/)가 개발한 플랫폼으로, 모든 판매자가 저렴한 비용으로 즉시 Bitcoin 및 스테이블코인 결제를 통합할 수 있도록 지원합니다.



Speed에는 비즈니스의 재정적 측면을 다루는 다양한 기능이 있습니다. 찾으실 수 있습니다:





- 온라인 결제 구성**: 웹사이트를 통해 고객이 어디에 있든 결제를 받을 수 있습니다.





- 현장 결제**: 매장에서 현금을 수금하는 상점 및 비즈니스에 이상적입니다.





- 인출**: 자산을 원활하게 인출하고 비트코인을 사용하여 고객과 급여를 상환하세요.





- 다른 플랫폼과의 연결**: 결제를 관리하기 위해 외부 도구를 사용하시나요? Speed는 비즈니스를 반영하는 올인원 에코시스템을 위해 이러한 도구를 플랫폼에 연결할 수 있는 기능을 제공합니다.



Speed](https://app.tryspeed.com/register/)에서 계정을 생성하면 비즈니스에 대한 결제 설정이 시작됩니다.



![account-creation](assets/fr/01.webp)



Bitcoin 및 Lightning Network에 대한 경험에 따라 플랫폼을 간소화하는 데 도움을 줄 수 있도록 Speed Wallet에게 정보를 제공하세요



![onboard](assets/fr/02.webp)



Speed에는 통합을 사용자 정의할 수 있는 소프트웨어 개발 키트와 표준 통합을 위한 확장 기능이 함께 제공됩니다.



이 튜토리얼에서는 Speed에서 제공하는 확장 기능을 사용하여 표준 통합 작업을 진행하겠습니다.



Speed는 스토어 관리에 미치는 영향에 대해 걱정할 필요 없이 다양한 기능을 사용해 볼 수 있는 테스트 모드를 제공합니다.



![test-data](assets/fr/03.webp)



테스트 모드를 사용하여 이 튜토리얼에서 다루는 모든 측면을 테스트할 수 있습니다.



테스트 모드를 비활성화할 때는 출금 Wallet을 구성해야 합니다.



![configure-wallet](assets/fr/04.webp)



아직 Bitcoin 및/또는 Lightning Wallet을 소유하고 있지 않다면 [모바일 지갑] 튜토리얼(https://planb.network/tutorials/wallet)을 살펴보는 것을 추천합니다.



https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

⚠️ **중요**: Wallet를 구성할 때 수천 유로 단위의 큰 금액을 받을 때는 **BTC(On-Chain)** 유형을 선택하여 Bitcoin에서 안정적인 확인을 보장하고, 비즈니스에서 즉시 소액 결제를 받으려면 **LN Address** 유형을 선택하세요.



![setup-wallet](assets/fr/05.webp)



그런 다음 Speed에서 보낸 확인 이메일을 사용하여 Wallet의 추가를 확인합니다.



![verfication](assets/fr/06.webp)



자산을 출금할 수 없는 최소 출금 금액과 그 이하의 최소 잔액을 정의합니다.



![payout](assets/fr/07.webp)



## 제품 추가



제품** 섹션에서 스토어에서 판매하는 제품 카탈로그를 추가합니다.



![product-creation](assets/fr/08.webp)



다음**을 눌러 제품 및 기능을 계속 정의합니다.



![product-details](assets/fr/09.webp)



그런 다음 제품의 판매 가격을 정의합니다.



![product-price](assets/fr/10.webp)



이러한 제품을 사용하면 고객이 결제할 수 있도록 generate 결제 링크를 생성할 수 있습니다.



## 결제 받기



Speed Wallet은 비즈니스에서 온라인 또는 현장 결제를 받기 위해 여러 가지 방법을 사용할 수 있는 옵션을 제공합니다.



결제 받기 > 결제** 메뉴에서 받은 결제 내역과 상태(결제됨, 만료됨, 미결제됨, 취소됨)를 확인할 수 있습니다.



![payments](assets/fr/11.webp)





- 결제 링크는 **결제 링크** 옵션에 있으며, 제품에 대한 고유한 결제 페이지를 설정할 수 있습니다.



![checkout-link](assets/fr/12.webp)



필요에 따라 특정 금액의 결제를 받도록 결제 페이지를 구성하고 사용자 지정할 수 있습니다.



![configure-checkout](assets/fr/13.webp)



![finalize-checkout](assets/fr/14.webp)



계정에 설정한 결제 링크 목록은 **결제 링크** 메뉴에서 확인할 수 있습니다.





- 인보이스: Speed를 사용하면 고객에게 generate 견적 및 송장을 발행할 수 있습니다.



![invoices](assets/fr/16.webp)



이미 등록한 고객을 선택하거나 쉽게 직접 생성할 수 있습니다.



통화를 설정하면 해당 통화로 구성된 제품 목록에 액세스할 수 있습니다.



고객이 Invoice을 결제할 수 있도록 PDF 형식, 이메일 또는 스캔할 수 있는 QR코드 링크(현장에서 수거하는 스토어에 적합)를 generate으로 전송할 수 있습니다.



![configure-invoice](assets/fr/17.webp)






- 결제 주소** 메뉴에서는 다양한 금액의 결제를 여러 번 받을 수 있는 라이트닝 Address를 설정할 수 있습니다.



![addresses](assets/fr/19.webp)



⚠️ Speed 이외의 도메인 네임을 추가하여 사용할 수 있습니다. 하지만 처음 사용하는 경우에는 Speed 비즈니스 기술 지원의 모든 전문 지식을 활용하기 위해 표준 구성을 사용하는 것이 좋습니다.





- 원 QR**: 현장 결제에 이상적이며, 비즈니스와 관련된 QR 코드를 생성하여 고객이 제품을 결제할 수 있도록 합니다.



![one-qr](assets/fr/20.webp)



## Speed에서 결제하기



스피드 비즈니스는 비즈니스에 대한 대금을 수금하는 것뿐만 아니라 비즈니스의 전체 재무 측면을 차질 없이 관리할 수 있는 Wallet입니다.



결제 보내기** 메뉴에서 Speed가 제공하는 모든 송금 옵션을 확인할 수 있습니다.





- 즉시 결제**: 즉시 송금 옵션을 사용하면 판매자 계정에서 즉시 비트코인을 안전하게 송금할 수 있습니다.





- generate **인출 링크**를 사용하면 파트너와 공급업체가 온라인에 접속하지 않고도 나중에 결제에 액세스할 수 있습니다.



출금 링크** 옵션에서 새 출금 링크를 생성한 다음 수취인의 거래를 보호하기 위해 통화, 금액, 비밀번호를 정의하여 구성합니다.



![withdrawal-links](assets/fr/21.webp)



⚠️Les 출금 링크는 한 번만 사용할 수 있으며, 각 링크마다 고유한 비밀번호를 설정하는 것이 좋습니다. 그렇지 않으면 링크를 소유한 모든 사람이 출금 링크에 설정된 금액을 출금할 수 있습니다.





- 지급금**: 지급금 메뉴에서 Speed Business 잔액에서 개인 Wallet로 인출을 시작합니다.



![payouts](assets/fr/22.webp)





- 할인**: 보너스를 받을 수 있는 리베이트 옵션을 설정하여 단골 고객을 장려하세요.



![cashbacks](assets/fr/23.webp)



## 익스플로러 스피드 비즈니스



Speed Business는 단일 시스템에서 여러 개의 지갑을 보유할 수 있는 다중 통화 플랫폼입니다.



잔액** 옵션에서 Bitcoin, USDT, USDC 지갑의 잔액을 확인합니다.



![balance](assets/fr/24.webp)



스피드 Wallet과 마찬가지로 **스왑** 메뉴에서 스피드 비즈니스를 사용하면 27개 통화를 최소 Sats 20,000(현재 환율로 약 20달러)에 서로 다른 통화 지갑(BTC, USDT, USDC) 간에 스왑할 수 있습니다.



![swap](assets/fr/25.webp)



송금** 메뉴에서 다른 판매자와 소통하고 Speed ID를 사용하여 비트코인을 쉽게 송금하세요.



![transferts](assets/fr/26.webp)



고객** 메뉴에서 고객(개인 또는 회사) 목록을 저장하고 조회할 수 있습니다.



![customers](assets/fr/27.webp)



Speed의 제휴 프로그램에 참여하여 보상을 받으세요.



파트너** 메뉴에서 판매자를 초대하여 Speed 비즈니스에서 비즈니스를 설정하고 수동 소득을 얻으세요.



![partners](assets/fr/28.webp)



## 비즈니스 웹사이트에 Speed 통합



Speed Business에는 결제 솔루션을 자체 웹사이트에 통합할 수 있는 개발 키트가 있습니다.



개발자** 메뉴에서 공개 키와 개인 키를 생성하여 Speed Wallet API 메서드를 사용합니다.



전체 [문서](https://apidocs.tryspeed.com/reference/introduction)에서 Speed Business의 더 나은 통합에 대해 알아보세요.



![developers](assets/fr/29.webp)



## 비즈니스 맞춤 설정



설정** 메뉴에서 판매자 프로필 및 비즈니스 정보를 구성할 수 있습니다.



비즈니스 설정** 섹션에서





- 이름, 위치, 시간대 등 판매자 계정 세부 정보를 수정합니다.





- 계정 상태** 메뉴에서 계정의 활성화된 권한(결제 받기, Bitcoin, Exchange 보내기, 이체, 출금)을 확인하세요.





- 출금 지갑은 **출금 지갑** 메뉴에서 정의하고 **출금 예약** 메뉴에서 구성합니다.





- 비즈니스의 그래픽 가이드라인을 정의하고 **브랜딩** 메뉴에서 결제 페이지, 이메일, QR코드, 인보이스를 원하는 대로 사용자 지정하세요.





- 결제 방법** 메뉴에서 사용 가능한 통화로 결제 방법을 구성합니다.



![payment-method](assets/fr/30.webp)



⚠️ 허용 오차는 결제가 유효한 것으로 간주되기 위해 Invoice 금액에 대해 허용하는 할인 비율에 해당합니다. 고객이 100달러를 결제해야 하고 허용 오차가 1%인 경우 99달러를 결제하면 100달러의 Invoice이 유효합니다.





이제 Speed에 대해 잘 이해하셨고, Bitcoin를 비즈니스에 통합하고 Bitcoin를 기반으로 지역 순환 경제를 발전시킬 수 있게 되었습니다. 이 튜토리얼이 유용했다면 스위스 Bitcoin Pay 튜토리얼도 유용하게 활용하실 수 있을 것입니다.



https://planb.network/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a