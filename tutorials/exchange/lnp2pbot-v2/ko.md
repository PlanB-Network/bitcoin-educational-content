---
name: LNP2PBot
description: LNP2PBot 및 P2P Bitcoin 거래에 대한 전체 가이드
---
![cover](assets/cover.webp)


## 소개


KYC가 필요 없는 P2P(P2P) 거래소는 사용자의 개인정보와 금융 자율성을 보호하는 데 필수적입니다. 신원 확인 없이 개인 간 직접 거래가 가능하므로 프라이버시를 중시하는 사람들에게 매우 중요합니다. 이론적 개념에 대해 더 깊이 이해하려면 BTC204 과정을 살펴보세요:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bitcoin P2P (P2P) 구매 및 판매는 비트코인을 취득하거나 처분하는 가장 사적인 방법 중 하나입니다. LNP2PBot은 오픈 소스 텔레그램 봇으로, Lightning Network에서 P2P 교환을 용이하게 하여 빠르고 저렴한 비용으로 KYC 없이 거래할 수 있도록 지원합니다.


### 왜 Lnp2pbot을 사용하나요?




- KYC 필요 없음
- Lightning Network의 빠른 트랜잭션
- 저렴한 비용
- 전 세계 어디에서나 액세스 가능한 인기 메시징 애플리케이션인 텔레그램을 통한 간단한 Interface
- 통합 평판 시스템
- 안전한 거래를 위한 자동 에스크로
- 다중 통화 지원
- 활발하고 성장하는 커뮤니티


### 전제 조건


Lnp2pbot을 사용하려면 다음이 필요합니다:


1. Lightning Network Wallet(브리즈, 피닉스 또는 블릭스트 권장)


2. 텔레그램 애플리케이션 설치(https://telegram.org/)


3. 사용자명이 정의된 텔레그램 계정


## 설치 및 구성


### 1. Lightning Wallet 구성하기


호환되는 Lightning Wallet을 설치하는 것으로 시작하세요. 자세한 권장 사항은 다음과 같습니다:


**추천 지갑**




- [브리즈](https://breez.technology):
  - 초보자에게 적합
  - 직관적이고 현대적인 Interface
  - 비수탁(자금에 대한 통제권 보유)
  - Lnp2pbot과 완벽하게 호환됩니다
  - IOS 및 Android에서 사용 가능


아래는 이 Wallet에 대한 튜토리얼 링크입니다:


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [피닉스](https://phoenix.acinq.co) :
  - 간단하고 안정적인
  - 자동 채널 구성
  - BOLT11 송장에 대한 기본 지원
  - 일상적인 거래에 탁월
  - IOS 및 Android에서 사용 가능


아래는 이 Wallet에 대한 튜토리얼 링크입니다:


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [블릭스트](https://blixtwallet.github.io) :
  - 더 기술적이긴 하지만 매우 완벽합니다
  - 고급 구성 옵션
  - 숙련된 사용자에게 적합
  - 오픈 소스
  - Android에서 사용 가능


아래는 이 Wallet에 대한 튜토리얼 링크입니다:


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**다른 지갑에 대한 중요 참고 사항**


⚠️ **중요**: Sats을 판매하기 전에 Wallet이 봇에서 에스크로 시스템으로 사용하는 "보류" 인보이스를 지원하는지 확인하세요.




- Satoshi의 Wallet**: Sats 수령에는 잘 작동하지만 판매가 취소되면 잔액 업데이트가 지연될 수 있습니다.
- Muun**: 봇 라우팅 수수료 한도(최대 0.2%)로 인해 결제가 실패할 수 있으므로 권장하지 않습니다.
- Aqua**: Sats를 받을 수 있지만, 판매 취소 시 잔액 업데이트가 오래 지연될 수 있습니다(최대 48시간).


💡 **팁**: 최적의 경험을 위해 권장 지갑(Breez, Phoenix 또는 Blixt)을 선택하세요.


⚠️ **중요**: 복구 문구를 안전한 곳에 저장하는 것을 잊지 마세요.


### 2. Lnp2pbot 시작하기


1. 봇에 액세스하려면 이 링크를 클릭하세요: [@lnp2pBot](https://t.me/lnp2pbot)


2. 텔레그램이 자동으로 열립니다


3. "시작"을 클릭하거나 "/start" 명령을 보내세요


4. 아직 사용자 아이디가 없는 경우 봇이 사용자 아이디를 만들도록 요청합니다


5. 봇이 초기 구성 과정을 안내합니다


### 3. 커뮤니티 참여하기




- 메인 채널에 가입하세요: [@p2plightning](https://t.me/p2plightning)
- 지원 [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## 비트코인 구매 및 판매


Lnp2pbot에서 23비트코인을 GW하는 방법은 크게 두 가지입니다:


1. 마켓플레이스에서 기존 오퍼를 검색하고 응답하기


2. 나만의 구매 또는 판매 오퍼 만들기


이 가이드에서는 어떻게 :




- 기존 오퍼에서 비트코인 구매
- 나만의 오퍼를 생성하여 비트코인 판매


### 비트코인 구매 방법


**1. 오퍼 찾기 및 선택**


![Sélection d'une offre de vente](assets/fr/01.webp)


(https://t.me/p2plightning)에서 오퍼를 검색하고 관심 있는 광고 아래의 '사토시 구매하기' 버튼을 클릭합니다.


**2. 오퍼 및 금액 확인**


![Validation de l'offre](assets/fr/02.webp)


1. 봇 채팅으로 돌아가기


2. 선택한 오퍼 확인


3. 구매하고자 하는 금액을 법정 화폐로 입력합니다


4. 봇이 사토시 금액에 해당하는 라이트닝 Invoice를 제공하라는 메시지가 표시됩니다


**3. 판매자에게 문의**


![Mise en relation](assets/fr/03.webp)


Invoice가 전송되면 봇이 판매자와 연락을 취합니다.


**4. 판매자와의 커뮤니케이션**


![Chat privé](assets/fr/04.webp)


판매자의 닉네임을 클릭하면 Exchange 법정화폐 결제 세부 정보를 확인할 수 있는 비공개 채팅 채널이 열립니다.


**5. 결제 확인**


![Confirmation du paiement](assets/fr/05.webp)


법정화폐 결제를 완료한 후 봇 채팅에서 `/fiatsent` 명령을 사용합니다. 거래가 완료되면 판매자를 평가할 수 있으며 거래가 완료됩니다.


### 비트코인 판매 방법


**1. 판매 오퍼 만들기**


![Création d'une offre de vente](assets/fr/06.webp)


판매 오퍼를 생성하려면 명령어를 사용하면 됩니다:


`/sell`


그러면 봇이 단계별로 안내해 줍니다:


1. 통화 선택


2. 판매할 사토시의 양을 표시합니다


3. 가격에는 두 가지 옵션이 있습니다:




   - 사토시 수량에 대한 고정 가격 설정
   - 프리미엄(양수 또는 음수) 적용 옵션이 있는 시장 가격을 사용합니다


💡 **팁**: 프리미엄을 사용하면 시장 가격에 따라 가격을 조정할 수 있습니다. 예를 들어 프리미엄이 -1%이면 시장가보다 1% 낮은 가격에 판매한다는 뜻입니다.


**2. 주문 생성 확인**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


주문이 생성되면 `/cancel` 명령어를 사용하여 주문을 취소할 수 있는 옵션이 포함된 확인 메시지가 표시됩니다.


**3. 판매 관리**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- 구매자가 오퍼에 응답하면 결제할 수 있는 QR코드와 Invoice이 포함된 알림을 받게 됩니다.
- 구매자의 프로필과 평판을 확인합니다.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- 구매자의 닉네임을 클릭하면 비공개 토론 채널이 열립니다.
- 구매자에게 법정 화폐 결제 세부 정보를 전달합니다.
- 구매자의 법정 화폐 결제 확인을 기다립니다.
- 계정에 결제 금액이 입금되었는지 확인합니다.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- 릴리스`로 거래를 확인하고 주문을 완료합니다. 구매자를 평가할 수 있는 기회가 주어집니다.


## 모범 사례 및 안전


### 안전 팁




- 소량으로 시작하기
- 항상 사용자의 평판을 확인하세요
- 제안된 결제 방법만 사용하세요
- 모든 커뮤니케이션을 봇 채팅으로 유지
- 민감한 정보를 공유하지 마세요


### 평판 시스템




- 각 사용자에게는 평판 점수가 있습니다
- 성공적인 거래는 점수를 높입니다
- 평판이 좋은 사용자를 선택하세요
- 의심스러운 행동이 있으면 운영자에게 신고하세요


### 분쟁 해결


1. 문제가 발생하면 침착하고 전문성을 유지하세요


2. 분쟁` 명령을 사용하여 티켓을 엽니다


3. 필요한 모든 증빙 자료 제공


4. 진행자를 기다립니다


## 다른 솔루션과의 비교


Lnp2pbot은 Peach, Bisq, HodlHodl, Robosat 등 다른 P2P Exchange 솔루션에 비해 몇 가지 장점과 단점이 있습니다:


### Lnp2pbot의 장점




- KYC가 필요하지 않습니다**: 일부 플랫폼과 달리 Lnp2pbot은 신원 확인이 필요하지 않으므로 사용자 개인정보를 보호할 수 있습니다.
- 빠른 거래**: Lightning Network 덕분에 거래가 거의 즉각적으로 이루어집니다.
- 낮은 수수료**: 기존 거래소보다 거래 비용이 저렴합니다.
- 모바일 가용성**: LNP2PBot은 텔레그램을 통해 접근이 가능하여 모바일 기기에서 쉽게 사용할 수 있습니다.
- 간편한 사용**: Lnp2pbot의 직관적인 Interface은 경험이 적은 사용자도 쉽게 사용할 수 있습니다.


### Lnp2pbot의 단점




- 텔레그램 의존성**: Lnp2pbot을 사용하려면 텔레그램 계정이 필요하므로 모든 사용자에게 적합하지 않을 수 있습니다.
- 유동성 부족**: Bisq와 같은 기존 플랫폼에 비해 유동성이 더 제한적일 수 있습니다.


이에 비해 Bisq와 같은 솔루션은 더 큰 유동성과 데스크톱 Interface를 제공하지만 수수료가 높고 거래 시간이 더 오래 걸릴 수 있습니다. 한편, 호들호들 및 로보샛도 KYC가 필요 없는 거래를 제공하지만 수수료 구조와 인터페이스가 다릅니다.


## 유용한 리소스




- 공식 웹사이트: https://lnp2pbot.com/
- 문서: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- 지원 [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)