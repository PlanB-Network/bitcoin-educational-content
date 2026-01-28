---
name: Voltz
description: 비즈니스를 위한 올인원 Lightning wallet.
---

![cover](assets/cover.webp)



볼츠 플랫폼에 대한 아이디어는 자체 비트코인 wallet 서비스를 제공하고자 하는 비트코인 사용자 그룹에서 나왔습니다. 그 결과 소매점에서 비트코인을 받을 수 있는 완벽한 인프라가 탄생했습니다. 이 튜토리얼에서는 볼츠와 이 플랫폼이 제공하는 비트코인 통합 가능성에 대해 살펴봅니다.



## Voltz 시작하기



매일 송금, 수신, 결제가 가능한 보관용 Lightning wallet를 넘어, 볼츠는 비즈니스에서 비트코인을 POS 또는 마켓플레이스로 통합할 수 있는 다양한 확장 기능을 제공하는 완벽한 플랫폼입니다.



볼츠] 플랫폼(https://www.voltz.com/en)으로 이동하여 '지금 시도하기' 버튼을 클릭하여 계정을 생성합니다.



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ 강력한 영숫자 비밀번호를 설정하여 무차별 암호 대입 공격에 대한 가능성을 높이고, 피싱을 방지하기 위해 로그인 정보를 입력할 때 Voltz 공식 웹사이트에 실제로 접속했는지 확인하는 것이 중요합니다.



볼츠 인터페이스는 LnBits 플랫폼의 인터페이스와 매우 유사합니다.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz는 실제로 LnBits 서버를 기반으로 구축되었으므로 튜토리얼을 확인하여 자체 LnBits 서버를 마운트하고 솔루션을 구축하는 방법을 알아보세요.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

이 플랫폼을 사용하면 여러 포트폴리오를 효율적으로 관리할 수 있습니다. 기본적으로 가입하면 자동으로 Lightning 포트폴리오가 생성됩니다. 하지만 다른 포트폴리오를 추가할 수 있습니다.



![wallets](assets/fr/03.webp)



### 휴대성



볼츠는 웹 인터페이스에만 국한되지 않습니다. **모바일 액세스** 섹션에서 활성 볼츠 wallet를 Zeus 또는 Blue Wallet와 같은 애플리케이션에 연결할 수 있습니다.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

이렇게 하려면 플랫폼에 **LndHub** 확장 프로그램을 설치하고 활성화해야 합니다.



![lndhub](assets/fr/04.webp)



활성 Voltz 포트폴리오를 선택하고 부여하려는 권한에 따라 적절한 QR 코드를 스캔합니다.




- 인보이스 QR 코드는 포트폴리오 내역과 generate 신규 인보이스만 읽을 수 있습니다.
- 관리자 QR 코드를 통해 내역, generate 인보이스를 확인하고 Lightning 인보이스를 결제할 수도 있습니다.



![qrs](assets/fr/05.webp)



이 튜토리얼에서는 Voltz wallet을 Blue Wallet 애플리케이션에 연결합니다.



![connect](assets/fr/06.webp)



포트폴리오가 연결되면 수행된 모든 작업은 Blue Wallet와 Voltz 간에 동기화됩니다. 예를 들어, Blue Wallet에서 송장을 generate으로 전송하면 Voltz에도 기록이 남습니다.



![sync](assets/fr/07.webp)



포트폴리오 구성** 섹션에서는 포트폴리오 이름 사용자 지정, 지급받을 통화 등 최소한의 매개변수를 설정할 수 있습니다.



![config](assets/fr/08.webp)



### 확장 기능



볼츠 플랫폼의 특별한 기능 중 하나는 필요한 확장 기능을 활성화할 수 있는 모듈식 기능입니다. 확장 프로그램 목록은 **확장 프로그램** 메뉴에서 확인할 수 있습니다.



![extensions](assets/fr/09.webp)



이러한 확장 기능 중에는 재고를 관리하고 고객으로부터 결제를 수금하는 데 사용할 수 있는 POS 단말기인 TPoS가 있습니다.



![tpos](assets/fr/10.webp)



POS 단말기에서 다음을 수행할 수 있습니다:




- 고객 및 파트너와 공유할 수 있는 웹 페이지를 만드세요;
- 제품 재고를 관리합니다;
- Lightning 인보이스를 생성합니다;
- Bolt 카드를 통한 현금 결제.



확장 프로그램은 무료 버전과 고급 기능을 위한 유료 버전으로 제공됩니다. POS 단말기를 생성하려면 확장 프로그램 로고 아래의 **열기** 버튼을 클릭한 다음 **새 POS**를 클릭합니다.



![new_tpos](assets/fr/11.webp)



판매 시점의 이름을 정의한 다음, 결제 수금을 위해 Voltz wallet를 단말기에 연결합니다. 팁 활성화** 상자를 체크하여 팁을 활성화할 수 있습니다. 또한 고객에게 영수증을 발행하려면 인보이스 인쇄 옵션을 활성화합니다(이 기능은 아직 개발 중이므로 오작동이 있을 수 있습니다).



POS 단말기에는 해당 국가의 세금을 제품에 직접 적용하려는 경우 세금 구성 기능도 포함되어 있습니다.



![tpos](assets/fr/12.webp)



POS 단말기가 생성되면 사전 구성된 제품 및 서비스를 추가하여 판매자와 고객에게 원활한 결제 및 회계 환경을 제공할 수 있습니다.



![product](assets/fr/13.webp)



제품 이름을 정의하고 이미지를 추가하고 판매 가격을 설정하여 제품을 생성합니다.  더 쉽게 추적할 수 있도록 제품을 분류할 수 있습니다. 특정 제품에 직접 세금을 적용할 수 있습니다. 제품에 세금이 적용되지 않은 경우 POS 단말기 생성 단계에서 구성한 세금이 자동으로 적용됩니다.



![products](assets/fr/14.webp)



가져오기/내보내기** 버튼을 클릭하면 JSON 형식의 제품 목록을 자동으로 가져올 수 있습니다.



![exports](assets/fr/15.webp)



새 탭** 아이콘을 클릭하여 링크를 통해 결제 영역에 액세스하거나 **QR 코드** 아이콘을 클릭하여 QR 코드를 통해 고객과 POS 플랫폼을 공유할 수 있습니다.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



고객은 이 인터페이스에서 카탈로그를 참조하고 결제할 수 있습니다.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



사용 가능한 확장 프로그램 그룹에는 **Invoice** 및 **결제 링크** 확장 프로그램과 같은 도구도 있으며, 이를 사용하면 특정 제품이 포함된 generate 인보이스를 발행하여 POS 단말기를 거치지 않고 분리된 결제를 수금할 수 있습니다.



## 결제 내역 추적



결제** 메뉴에서 볼츠는 다양한 포트폴리오에 대한 결제에 대한 개요를 제공합니다.


으로 결제를 추적할 수 있습니다:




- 상태.
- 레이블: 예를 들어 POS 결제의 경우 **TPOS**, Zeus 및 Blue Wallet 지갑의 모바일 연결을 통한 **lnhub**입니다.
- 컬렉션 포트폴리오.
- 총 수신 및 발신 결제 금액입니다.
- 잘 정의된 기간.



![payments](assets/fr/22.webp)



## 추가 옵션



볼츠는 자체 솔루션을 구축할 수 있는 인프라이기도 합니다. 확장 프로그램** 섹션에서는 Voltz 및 LnBits 에코시스템 내에서 자체 확장 프로그램을 개발하는 방법에 대한 가이드를 확인할 수 있습니다.



![build](assets/fr/23.webp)



에코시스템 외부에서 솔루션을 개발하지만 해당 인프라를 계속 사용하려는 경우 **노드 URL** 섹션에서 이 데이터로 수행할 수 있는 작업의 예와 함께 API 키 및 문서 정보를 확인할 수 있습니다.



Voltz wallet을 사용하여 애플리케이션에서 Lightning 송장을 생성하고, Lightning 송장을 결제하고, 송장을 디코딩 및 확인할 수 있습니다.



![keys](assets/fr/24.webp)



이제 볼츠에 대해 잘 이해하셨을 것입니다. 이 튜토리얼이 재미있으셨다면, 저희 강좌를 통해 비트코인을 비즈니스에 통합하는 가장 좋은 방법과 도구에 대해 자세히 알아보세요: 비즈니스를 위한 Bitcoin.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a