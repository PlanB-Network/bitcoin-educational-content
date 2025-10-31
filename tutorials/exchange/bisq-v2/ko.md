---
name: Bisq 2
description: 비스크 2 사용 및 비트코인 P2P 교환에 대한 전체 가이드
---
![cover](assets/cover.webp)


## 소개


KYC가 필요 없는 P2P(P2P) 거래소는 사용자의 개인정보와 금융 자율성을 보호하는 데 필수적입니다. 신원 확인 없이 개인 간 직접 거래가 가능하므로 프라이버시를 중시하는 사람들에게 매우 중요합니다. 이론적 개념에 대해 더 깊이 이해하려면 BTC204 과정을 살펴보세요:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Bisq 2란 무엇인가요?


Bisq 2는 2024년에 출시된 인기 탈중앙화 Bisq Exchange의 새로운 버전입니다. 이전 버전과 달리 Bisq 2는 여러 Exchange 프로토콜을 지원하도록 개발되어 사용자에게 더 큰 유연성을 제공합니다.


**주요 새 기능:**




- 여러 개인 정보 보호 네트워크 지원(Tor, I2P)
- 개인정보 보호를 위한 다중 ID
- 트레이딩 봇용 REST API
- 여러 Wallet 유형 지원
- BSQ에 의무적으로 예치하는 역할 시스템


이 가이드는 현재 사용 가능한 유일한 프로토콜인 "Bisq Easy"에만 초점을 맞추고 있습니다. 비스크 이지 프로토콜은 Bitcoin 신규 사용자를 위해 특별히 설계되었습니다. 이 프로토콜을 통해 사용자는 탈중앙화된 P2P 플랫폼에서 법정화폐로 비트코인을 사고 팔 수 있습니다. 거래는 미화 600달러(최소 6달러)로 제한되며, Exchange 보안은 BTC 판매자의 평판에 의존합니다. 비스크 이지에는 거래 수수료나 보증금 요건이 없습니다. Bisq Easy는 600 USD(또는 이에 상응하는 금액) 미만의 현금 거래에 대해 Bisq 1을 대체할 것으로 예상됩니다.


**주요 기능:**




- 크로스 플랫폼 데스크톱 애플리케이션
- 여러 Exchange 프로토콜 사용 가능
- 분산형 P2P 네트워크
- 개인 정보 보호에 집중(KYC 없음, 토르 사용)
- 비수탁(자금에 대한 통제권 보유)
- 오픈 소스(AGPL)


### Bisq 1과의 차이점


**구매자의 경우:**




- 보증금 불필요
- 거래 수수료 없음
- Mining 수수료 없음
- 공급업체 평판에 기반한 보안
- 낮은 거래 한도(미화 600달러 상당)


**판매자의 경우:**




- 보증금 불필요
- 평판 구축
- BSQ 소각 또는 BSQ 채권 생성 가능성
- 잠재적으로 더 높은 판매 프리미엄(시장보다 10~15% 높음)


**중요 참고사항: ** Bisq Multisig 프로토콜이 Bisq 2에 구현되면 이전 버전의 Bisq는 단계적으로 폐지될 수 있습니다. 그러나 Bisq 1은 Bisq CAD와 BSQ-BTC 거래소의 관리 도구로 계속 사용될 것입니다.


### Exchange 프로세스




- 오퍼 작성자가 Exchange의 조건을 정의합니다
- 트레이더가 조건(결제 방법 및 가격)에 동의하면 Exchange가 시작됩니다
- 판매자는 은행 정보를 구매자에게 보내고, 구매자는 Bitcoin Address을 판매자에게 보냅니다
- 구매자가 현금으로 결제하고 판매자에게 알림을 보냅니다
- 결제가 완료되면 판매자는 비트코인을 구매자의 Address로 전송합니다
- 구매자가 비트코인을 받으면 Exchange이 완료됩니다


### 중요 규칙




- 결제 정보를 교환하기 전에 Exchange은 정당한 사유 없이 취소할 수 있습니다
- 세부 정보를 교환한 후 의무를 이행하지 않으면 추방당할 수 있습니다
- 은행 송금의 경우, **결제 사유에 "Bisq" 또는 "Bitcoin"**이라는 용어를 사용하지 마세요(이로 인해 자금이 동결되거나 수취인 또는 지급인의 은행 계좌가 차단될 수 있습니다)
- 트레이더는 하루에 한 번 이상 로그온하여 프로세스를 따라야 합니다
- 문제가 발생하면 트레이더는 중재자의 서비스를 요청할 수 있습니다


## 설치 및 구성


### 1. Bisq 2 다운로드 및 확인


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Bisq.network](https://bisq.network/downloads/)로 이동합니다
- 사용 중인 운영 체제에 맞는 Bisq 2 버전을 다운로드하세요(페이지 아래로 스크롤)
- 다운로드한 파일의 진위 여부를 확인합니다(적극 권장). 서명 확인에 대한 자세한 가이드는 다음 튜토리얼을 참조하세요:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. 시스템에 따른 설치


사용 중인 운영체제에 맞는 설치 단계를 따라주세요. 설치 중 문제가 발생하면 [비스크 공식 위키](https://bisq.wiki/Downloading_and_installing)에서 자세한 가이드를 참조하세요.


### 3. 첫 시작




- Bisq 2를 실행하고 이용 약관에 동의합니다


![Conditions d'utilisation](assets/fr/01.webp)




- 이름과 아바타를 선택하여 새 프로필 만들기


![Création du profil](assets/fr/02.webp)




- 그런 다음 애플리케이션의 메인 대시보드로 이동하여 첫 비트코인을 구매하거나 판매할 수 있는 Bisq Easy를 실행할 수 있습니다


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. 결제 방법 설정




- 메인 메뉴에서 결제 계정 섹션에 액세스합니다


![Liste des comptes de paiement](assets/fr/04.webp)




- 필수 정보를 입력하여 새 결제수단을 추가합니다


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


결제수단을 미리 구성하는 것은 선택 사항이지만 거래 시 시간을 절약하기 위해 권장합니다. Exchange 파트너에게 연락하여 거래 중에 직접 결제수단을 구성할 수도 있습니다.


### 5. 계정 보안


**데이터 백업:**


Bisq 1과 달리 Bisq 2는 현재 Bitcoin Wallet을 통합하지 않습니다. 따라서 거래는 외부 지갑을 통해 이루어집니다. 그럼에도 불구하고 Bisq 2 데이터 폴더를 정기적으로 백업하는 것이 좋습니다. 데이터 폴더를 찾으려면 [공식 Bisq 위키](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory)를 참조하세요.


**아이덴티티 관리:**


Bisq 2에서는 여러 개의 ID를 만들 수 있습니다. 각 ID는 서로 다른 유형의 거래에 사용할 수 있습니다. ID는 데이터 폴더에 저장됩니다.


## 비트코인 구매 및 판매


### 비트코인 구매 방법


**옵션 1: 기존 오퍼 활용**




- 메인 화면에서 "Bisq Easy", "시작하기" 탭을 선택한 다음 "거래 마법사 시작"을 클릭합니다


![Lancer trade wizard](assets/fr/06.webp)




- "Bitcoin 구매"를 선택하고 통화를 선택합니다


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- 선호하는 결제 방법(SEPA, Revolut 등)을 설정합니다


![Configuration méthodes de paiement](assets/fr/09.webp)




- 이 시점에서 이전 기준에 해당하는 오퍼 목록이 있거나 "오퍼북"으로 이동해야 합니다


![Liste des offres](assets/fr/10.webp)




- 두 번째 경우에는 Interface의 오른쪽 상단에 있는 버튼을 사용하여 오퍼를 표시하고 필터링할 수 있습니다


![Filtres des offres](assets/fr/11.webp)




- 오퍼를 선택한 후에는 결제수단을 선택한 다음 거래 요약을 확인하기만 하면 됩니다


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**옵션 2: 나만의 오퍼 만들기**




- "Bisq Easy"를 선택한 다음 "오퍼북"을 선택합니다
- 거래 쌍 선택(예: BTC/EUR)
- '오퍼 만들기'를 클릭합니다
- 오퍼 생성 마법사를 따릅니다: 금액(고정 또는 범위)을 정의합니다


![Configuration du montant](assets/fr/20.webp)




- 허용되는 결제 방법 선택


![Sélection méthodes de paiement](assets/fr/21.webp)




  - 요약을 확인하고 오퍼를 게시하세요


![Récapitulatif et publication](assets/fr/22.webp)


Exchange가 시작되면 :




- Bitcoin Address 또는 Lightning Invoice을 판매자에게 보내기


![Envoi adresse Bitcoin](assets/fr/15.webp)




- 판매자의 은행 정보 받기


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- 결제하기("Bisq" 또는 "Bitcoin"을 언급하지 않고)
- 판매자에게 결제 사실을 알리기


![Notification paiement](assets/fr/18.webp)




- 비트코인이 도착할 때까지 기다립니다


![Attente réception](assets/fr/19.webp)


### 비트코인은 어떻게 판매하나요?


Bisq 2의 판매 프로세스는 구매 프로세스와 비슷한 논리를 따르며, 주요 단계는 동일하지만 순서는 역순입니다. 직접 판매 오퍼를 만들거나 기존 구매 오퍼에 응답할 수 있습니다. 다음은 프로세스의 다양한 옵션과 단계에 대한 분석입니다:


**옵션 1: 판매 오퍼 만들기**




- "Bisq Easy"를 선택한 다음 "오퍼북"을 선택합니다
- "오퍼 만들기"를 클릭하고 "Bitcoin 판매"를 선택합니다
- 오퍼 구성 :
 - 통화 선택(EUR, USD 등)
 - 허용되는 결제 방법 선택
 - 금액 설정(미화 6~600달러 상당)
 - 가격 설정(고정 또는 시장의 %)
- 세부 정보 확인 및 오퍼 게시


**옵션 2: 기존 오퍼 수용**




- '오퍼북' 탭에서 오퍼 찾아보기
- 통화 및 결제 방법별로 필터링
- 자신에게 맞는 오퍼를 선택하세요
- 세부 정보 확인 및 제안 수락


**판매 프로세스:**


Exchange이 시작되면 :




   - 구매자에게 은행 정보 보내기
   - 구매자의 Bitcoin Address을 기다립니다
   - Address이 유효한지 확인


결제 알림 후 :




   - 계정에 결제 금액이 입금되었는지 확인
   - 금액과 세부 정보가 일치하는지 확인
   - 제공된 Address로 비트코인을 전송하세요
   - 거래 완료로 표시


마무리 :




   - 구매자의 확인을 기다립니다
   - 거래에 대한 피드백 남기기
   - 향후 판매를 위한 평판 구축


**중요 참고사항: 판매자는 지불 거절 위험에 특히 주의를 기울여야 합니다. 안전한 결제수단을 선호하고 비트코인을 송금하기 전에 항상 결제금이 입금되었는지 확인하세요.


## 모범 사례 및 안전


### 안전 팁


**구매자의 경우:**




- 소량으로 시작하기
- 판매자 평판 확인(최소 점수 30,000점)
- 제안된 결제 방법만 사용하세요
- 결제를 보내기 전에 판매자가 활성 상태인지 확인하세요
- Exchange 채팅에 제공된 은행 정보만 사용하세요
- Bisq 2 플랫폼 외부에서 통신하지 마세요
- 결제 증빙 보관
- 민감한 정보는 절대 보내지 마세요


**판매자의 경우:**




- 새 계정을 만들 때 주의하세요
- 지불 거절에 민감한 결제 수단(PayPal, Venmo)을 피하세요
- 계정 세부 정보가 구매자와 일치하는지 확인합니다
- 채팅으로 커뮤니케이션 제한 Bisq 2
- 의심스러운 경우 중재 열기


### 평판 구축(영업 사원용)


Bisq에서 판매자로서의 평판을 높이려면 정기적으로 거래를 진행하고 구매자와 전문적인 커뮤니케이션을 유지하세요. 구매자의 요청에 신속하게 응답하여 긍정적인 경험을 보장하세요. BSQ 본드를 생성하여 플랫폼에 Commitment을 보여줄 수도 있습니다. 이러한 조치를 통해 신뢰를 쌓고 더 많은 구매자를 유치할 수 있습니다.


### 분쟁 해결




- 채팅을 통해 상대방에게 연락하기
- 필요한 경우 분쟁을 시작합니다
- 요청된 모든 증빙 자료 제공
- 중재자의 지시를 따르세요


### 개인정보 보호정책 :




- 등록 또는 중앙 집중식 본인 인증이 필요하지 않습니다
- 모든 연결은 토르 네트워크(그리고 곧 I2P)를 통해 이루어집니다
- 데이터를 저장할 중앙 서버 없음
- 거래 세부 정보는 관련 당사자만 열람할 수 있습니다


### 검열로부터 보호 :




- 완전 분산형 P2P 네트워크
- 토르 네트워크(그리고 곧 I2P)를 사용하여 검열에 저항하기
- 중앙화된 법인이 없는 DAO가 관리하는 오픈 소스 프로젝트


## 장점과 단점


### Bisq 2의 이점




- 최대 프라이버시**: KYC 없음, 토르 사용
- 탈중앙화**: 중앙 서버 없음
- 보안**: 오픈 소스, 비 커스터디 코드
- 직관적인 Interface**: Bisq 1보다 더 간단합니다
- 유연성**: 여러 Exchange 프로토콜


### Bisq 2 단점




- 제한된 유동성** (현재로서는) :
 - 시작 단계의 새로운 프로토콜
 - 사용 가능한 판매 제안이 거의 없습니다
 - 구매자를 찾기 위한 대기 시간이 길어질 수 있음
- 거래 한도**: 거래당 최대 USD 600(비스크 이지 사용 시)
- 데스크톱 전용**: 모바일 애플리케이션 없음


## 향후 프로토콜


현재 사용 가능한 프로토콜은 Bisq Easy가 유일하지만, Bisq 2를 위한 다른 여러 프로토콜이 개발 중입니다:




- 비스크 라이트닝**: Lightning Network에서 다자간 계산 암호화를 사용하는 에스크로 시스템을 기반으로 하는 Exchange 프로토콜입니다.
- Bisq MuSig**: 보증금과 함께 2대2 Multisig를 사용하여 메인 프로토콜을 Bisq 1에서 Bisq 2로 마이그레이션했습니다.
- BSQ 스왑**: BSQ와 BTC 간의 즉각적인 아토믹 스왑.
- Liquid 스왑**: 아토믹 스왑을 통해 Liquid Network(USDT, BTC-L) 자산의 Exchange로 교환.
- 모네로 스왑**: Bitcoin과 모네로 간의 원자 교환.
- Liquid MuSig**: 더 낮은 비용과 더 큰 프라이버시를 위해 L-BTC를 사용하는 Multisig 프로토콜의 버전입니다.
- 잠수함 스왑**: Lightning Network의 Bitcoin과 Bitcoin의 On-Chain 간 교환.
- 스테이블코인 스왑**: Bitcoin와 USD 스테이블코인 간의 원자 교환.
- Multisig 옵션**: On-Chain Multisig 거래에서 BTC를 차단하는 P2P 풋 및 콜 옵션 생성.
- Multisig 오픈 컨트랙트**: 차익거래가 가능한 2대3 Multisig 시스템을 사용하여 맞춤형 조건부 계약을 생성할 수 있습니다.


이러한 프로토콜은 현재 개발 중이며 점진적으로 Bisq 2에 통합되어 사용자의 특정 요구에 따라 더 큰 유연성을 제공할 예정입니다.


## 유용한 리소스




- 공식 웹사이트: [bisq.network](https://bisq.network)
- 문서: [비스크 위키](https://bisq.wiki)
- 지원 [포럼 비스크](https://bisq.community)
- 소스 코드 : [깃허브](https://github.com/bisq-network)