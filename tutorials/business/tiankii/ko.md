---
name: 티안키
description: 리테일러와 소비자를 위한 라이트닝 도구 모음
---

![cover](assets/cover.webp)



Bitcoin 생태계에서 실시간으로 결제를 수락하는 것은 기업과 개인에게 여전히 큰 과제입니다. 기존 솔루션은 고급 기술 지식이 필요하거나, 복잡한 인프라를 유지해야 하거나, 중개자가 자금을 보유해야 하는 경우가 많습니다. 이러한 상황은 Lightning Network의 기술 발전의 가능성에도 불구하고 일상적인 통화로서 Bitcoin의 대량 채택을 가로막고 있습니다.



2021년에 설립된 살바도르의 기업인 Tiankii는 접근 가능한 모듈식 Bitcoin 인프라를 제공함으로써 이 문제에 대응합니다. 폐쇄적인 에코시스템의 도입을 강요하는 대신, Tiankii는 상호 연결된 도구 세트를 제공하여 누구나 자금 통제권을 희생하지 않고도 Bitcoin Lightning을 비즈니스에 통합할 수 있도록 지원합니다.



## 티안키란 무엇인가요?



### 기원과 철학



나후아틀어로 '모든 사람이 이용할 수 있는 야외 시장'을 뜻하는 티안키는 엘살바도르 최초의 100% Bitcoin 스타트업입니다. Bitcoin가 엘살바도르의 법정 화폐로 채택된 이후 다빈 오테로가 설립한 이 회사는 Bitcoin를 가치 저장 수단에서 일상적인 구매를 위한 거래 가능한 통화로 전환하는 것을 목표로 합니다. 수탁 플랫폼과 달리 티안키는 사용자가 자금에 대한 통제권을 갖고 인프라는 기술적 중개자 역할만 하는 비수탁 방식을 채택하고 있습니다.



### 기술 아키텍처



티안키는 Lightning Network를 기반으로 한 Bitcoin 서비스형 인프라 제공업체로 자리매김하고 있습니다. 이 2계층 기술은 소액 결제와 일상적인 구매를 가능하게 하는 거의 즉각적인 거래를 무시할 수 있는 비용으로 가능하게 합니다.



아키텍처는 세 가지 기둥을 기반으로 합니다:



**라이트닝 우선**: 대용량 트랜잭션에 대한 on-chain 트랜잭션 지원은 유지하면서 속도와 저렴한 비용으로 라이트닝 네트워크를 체계적으로 선호합니다.



**개방형 표준**: 결제 요청을 자동화하기 위해 LNURL, 판독 가능한 이메일 ID를 위한 Lightning Address, 상호 운용 가능한 NFC 결제를 위한 Bolt 카드 사용.



**wallet-애그노스틱 모듈성**: 필요한 전문성과 자율성 수준에 따라 다양한 라이트닝 포트폴리오(LNbits, Blink, BlueWallet) 또는 자체 노드를 연결할 수 있어 최대한의 유연성을 제공합니다.



## 티엔키이 에코시스템 도구



### Bitcoin POS - 매장 내 결제 단말기



이 앱은 스마트폰이나 태블릿을 라이트닝 단말기로 전환합니다. 판매자가 현지 통화로 금액을 입력하면 앱에서 Lightning QR 코드를 생성하거나 Bolt 카드를 수락합니다. 거래는 수수료 없이 즉시 입금되며, 150개 이상의 통화로 자동 변환, 팁 관리 및 판매 내역이 제공됩니다.



### 판매자 대시보드 - 통합 판매 관리



Interface 웹을 중앙 집중화하여 wallet Lightning을 연결하고, 실시간으로 거래를 추적하고, 송장 및 generate 회계 보고서를 발행합니다. 이 플랫폼은 매장 내 결제(POS), 온라인 판매(전자상거래 플러그인) 또는 API 통합 등 모든 채널을 통합합니다. 결제는 선택한 wallet로 수렴됩니다.



### Bitcoin 비접촉식 카드(Bolt 카드)



NFC Bolt 카드는 일반 대중을 위해 Bitcoin을 대중화하기 위한 티안키의 주요 혁신입니다. 비접촉식 은행 카드처럼 작동하는 이 카드는 호환되는 단말기에 탭하기만 하면 Bitcoin 라이트닝 구매를 결제할 수 있습니다.



기존 커스터디 솔루션과 달리 이 카드는 상호 운용성을 보장하는 개방형 표준을 따릅니다. 사용자는 IBI 애플리케이션을 통해 자신의 wallet에 연결할 수 있으므로 개인 키를 유지하고 관련 자금을 완벽하게 제어할 수 있습니다. 결제 시 스마트폰을 꺼내거나 인터넷에 연결할 필요 없이 단 1초 만에 결제가 완료됩니다.



이 솔루션은 특히 스마트폰에 익숙하지 않은 사람들을 위한 포용적인 솔루션으로, Bitcoin 경제에 접근 가능한 관문을 제공합니다.



### IBI 앱 - Interface 개별 Bitcoin



IBI 애플리케이션(개인용 Bitcoin Interface)은 Bitcoin Lightning을 매일 사용하고자 하는 개인을 위해 설계되었습니다. 이 애플리케이션의 주요 장점은 이메일 형식으로 읽을 수 있는 결제 식별자(예: alice@ibi.me)인 개인화된 Address Lightning을 생성한다는 점입니다.



이 식별자는 결제 수취를 대폭 간소화합니다. 각 거래마다 새 송장을 generate로 보낼 필요 없이 발신자가 Lightning 주소만 입력하면 됩니다. 또한 이 인터페이스를 통해 Bolt 카드(활성화, 비활성화, 지출 한도)를 관리하고, 다양한 Lightning 지갑을 연결하고, QR 코드를 스캔하여 결제할 수 있습니다.



### 전자상거래 플러그인



바로 사용 가능한 WooCommerce, Shopify 및 Cloudbeds용 통합 기능. 몇 분 안에 설치하여 결제에 Bitcoin Lightning을 추가할 수 있습니다. 혜택: 수수료 없음(신용 카드 2~3% 대비), 즉시 결제, 전 세계 액세스, 지불 거절 제거. 판매자의 연결된 wallet에 직접 결제가 이루어집니다.



### Bitcoin API 및 개발자 도구



Tiankii SDK를 사용하면 자체 노드를 유지 관리하지 않고도 Bitcoin Lightning을 기존 애플리케이션에 통합할 수 있습니다. API는 Google Cloud에서 호스팅되는 강력한 인프라를 통해 송장 생성, 결제 확인 및 대량 메일링을 처리합니다. Command Center는 맞춤형 도메인, 대량 결제, NFC 단말기 및 카드의 중앙 집중식 관리에서 Address Lightning을 통해 조직을 위한 서비스를 완성합니다.



## 설치 및 첫 단계



### 필수 전제 조건



티안키를 사용하려면 복잡한 기술적 전제 조건이 필요하지 않습니다. 애플리케이션은 스마트폰, 태블릿 또는 컴퓨터의 웹 브라우저를 통해 작동합니다. 기본 애플리케이션을 설치할 필요 없이 인터넷에 연결되어 있고 최신 브라우저만 있으면 IBI 또는 판매자 대시보드에 액세스할 수 있습니다.



**개인 사용자(IBI 앱)**의 경우: wallet Lightning이 필요하지 않습니다. 계정을 생성하면 티안키는 백그라운드에서 Liquid 네트워크를 사용하는 노드 없는 구현인 [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html)을 통해 작동하는 Address Lightning을 자동으로 구성합니다. 별도의 기술적 구성 없이 즉시 결제를 받고 보낼 수 있습니다. 이 솔루션은 초보자의 액세스를 대폭 간소화하면서도 자체 관리 기능을 유지합니다.



**판매자용(판매자 대시보드)** : POS 단말기를 사용하고 결제를 받기 위해서는 기존 wallet 라이트닝의 연결이 필수입니다. 티안키는 모바일 지갑(블링크, 스트라이크), 자체 호스팅 솔루션(LNbits, LND/CLN 노드), 웹 지갑(알비) 등 다양한 솔루션을 지원합니다. 자세한 연결 가이드는 이 튜토리얼의 리소스 섹션에서 확인할 수 있습니다.



### 개인 고객용: IBI 앱



**계정 만들기



Accounts.ibi.me로 이동하여 계정을 만듭니다. 이 페이지에서 두 가지 계정 유형 중에서 선택할 수 있습니다: "개인용 '개인 사용' 또는 상업용 '비즈니스 사용'입니다. Bitcoin에서 결제를 받고 보내기 위한 도구에 액세스하려면 "개인용"을 선택합니다.



![Choix du type de compte](assets/fr/01.webp)



'개인 사용'을 선택하면 등록을 완료할 수 있도록 go.ibi.me로 자동 리디렉션됩니다. 이메일, 전화번호 또는 Google, Microsoft 또는 트위터 계정을 사용하여 등록할 수 있습니다. 등록이 완료되면 즉시 IBI 인터페이스에 액세스할 수 있으며, Lightning Address는 이미 작동 중입니다.



![Création du compte](assets/fr/02.webp)



**Interface 메인**



IBI 인터페이스는 잔액을 사토시 및 현지 통화(USD)로 표시합니다. 결제를 받으려면 '받기', QR 코드를 스캔하려면 '스캔', 사토시를 보내려면 '보내기'의 세 가지 버튼으로 상호 작용할 수 있습니다.



![Interface IBI](assets/fr/03.webp)



**결제 받기**



사토시를 받으려면 "받기"를 누르세요. 애플리케이션이 자동으로 QR 코드를 생성하고 개인화된 Address 라이트닝(nom@ibi.me 형식)을 표시합니다. 이 주소 또는 QR 코드를 발신자와 공유하면 자금이 IBI 계정에 즉시 도착합니다.



![Réception avec Lightning Address](assets/fr/04.webp)



잔액이 적립되면 이 사토시를 사용하여 결제할 수 있습니다.



**결제 보내기**



사토시를 보내려면 '보내기'를 누릅니다. 라이트닝 QR 코드를 스캔하거나 라이트닝 Address 대상을 직접 입력할 수 있습니다.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



원하는 금액을 사토시로 입력하고 현지 통화로 동등한 금액을 확인한 다음 결제를 확인합니다.



![Confirmation du montant](assets/fr/07.webp)



성공 알림은 발송 금액, 거래 수수료, 수취인 등의 세부 정보와 함께 발송을 확인합니다.



![Paiement réussi](assets/fr/08.webp)



**계정 관리



설정에서 Bitcoin NFC 카드(Bolt 카드)를 관리할 수 있습니다. 이 인터페이스에서 카드의 지출 한도를 활성화, 비활성화 또는 설정할 수 있습니다.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### 판매자용 판매자 대시보드 및 POS



**비즈니스 계정 생성



Accounts.ibi.me로 이동하여 계정을 생성합니다. '비즈니스용'을 선택하여 판매자 도구에 액세스합니다. 이 계정 유형은 판매자 대시보드 및 POS 단말기에 대한 액세스 권한을 잠금 해제합니다.



'비즈니스용'을 선택하면 판매자 대시보드(pay.tiankii.com)로 자동 리디렉션됩니다. 그러면 수익 추적, 거래 및 결제 도구가 포함된 비즈니스 관리 인터페이스로 이동합니다. 결제 수락을 시작하려면 먼저 페이지 상단의 링크를 클릭하여 wallet Lightning을 연결해야 합니다(이미지의 화살표 참조).



![Dashboard marchand](assets/fr/11.webp)



**wallet 라이트닝** 연결



POS 활성화의 중요한 단계: 결제를 받으려면 wallet Lightning을 연결하세요. 인터페이스는 여러 가지 연결 옵션을 제공합니다. 일부 옵션(Bitcoin 온체인 및 Lightning Network)은 아직 개발 중이며 인터페이스에서 회색으로 표시된다는 점에 유의하시기 바랍니다.



![Options de connexion wallet](assets/fr/12.webp)



이 튜토리얼에서는 Chivo, Blink Wallet 및 Strike와 호환되는 Lightning Address 연결을 사용합니다. 예를 들어 LN 마켓, Alby 또는 기타 호환되는 공급업체에서 구매한 Lightning Address(nom@domaine.com 형식)을 입력합니다.



![Saisie de la Lightning Address](assets/fr/13.webp)



로그인하면 계정이 작동합니다. 이제 POS에 액세스하거나 대시보드로 돌아가 다른 설정을 구성할 수 있습니다.



![Connexion réussie](assets/fr/14.webp)



*결제 링크** *결제 링크



'결제 도구' 메뉴에서는 결제 링크를 생성하고 관리할 수 있는 '결제 요청'에 액세스할 수 있습니다. 이 기능은 기부, 단일 결제, 다중 결제, 콘텐츠 보호를 위한 페이월 등 이메일이나 메시지로 전송할 맞춤형 결제 링크를 생성하는 데 유용합니다. 비즈니스 요구에 맞게 다양한 유형의 링크를 만들 수 있습니다.



![Liens de paiement](assets/fr/15.webp)



**판매 단말기 구성**



스토어 내 결제를 수락하려면 '결제 도구'에서 '판매 단말기' 메뉴에 액세스합니다. 이 섹션에서는 POS 단말기를 생성하고 관리할 수 있습니다(단말기 수는 플랜에 따라 다릅니다. 아래의 부분 유료화 대 비즈니스 플랜 참조). "열기"를 클릭하여 브라우저에서 POS 인터페이스를 엽니다.



![Gestion des terminaux](assets/fr/16.webp)




**판매 생성**



POS 단말기에 판매 금액을 입력할 수 있는 숫자 키패드가 표시됩니다. 현지 통화로 금액을 입력한 다음(예: 500 sats은 630.74 ARS에 해당) "확인"을 눌러 확인합니다.



![Saisie du montant](assets/fr/17.webp)



애플리케이션은 즉시 결제를 위한 Lightning QR코드와 Lightning Address을 생성합니다. 고객은 wallet로 QR 코드를 스캔하거나 NFC 단말기에서 Bolt 카드를 사용할 수 있습니다.



![QR code de paiement](assets/fr/18.webp)



결제가 완료되면 현지 통화와 사토시로 받은 금액이 표시된 확인 화면이 나타납니다. 영수증을 이메일로 보내거나 티켓을 인쇄하거나 즉시 새 판매를 시작할 수 있습니다.



![Paiement encaissé](assets/fr/19.webp)



**모니터링 및 관리**



모든 거래는 판매자 대시보드에 기록됩니다. 기간별 매출, 총 판매 수, 회계에 대한 자세한 내역을 완벽하게 추적할 수 있습니다.



설정 인터페이스에는 여러 가지 구성 탭이 있습니다. "일반 설정" 탭에서는 판매자 프로필과 알림을 관리할 수 있습니다. "사용자" 탭에서는 팀의 판매자 대시보드 액세스 권한을 추가하고 관리할 수 있습니다(플랜에 따라 다중 사용자 관리). "개발 작업 영역" 탭에서는 고급 통합을 위한 API 키에 액세스할 수 있으며, "구독"에서는 구독을 관리할 수 있습니다.



![Paramètres du compte marchand](assets/fr/20.webp)



**프리미엄 대 비즈니스 요금제



티안키는 판매자 대시보드를 위한 두 가지 패키지를 제공합니다. 프리미엄** 플랜(무료)은 단일 판매 시점, 단일 사용자, 월 거래액 1,000달러로 제한, 전자상거래 커넥터 액세스 불가 등 제한이 있는 스타트업에 적합합니다. 비즈니스** 요금제(거래당 0.5% 수수료)는 무제한 단말기, 무제한 사용자, 무제한 거래량, WooCommerce/Shopify/Cloudbeds 플러그인 액세스 및 전용 WhatsApp 알림을 제공합니다.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## 혜택 및 제약 사항



### 하이라이트



**자기 보관**: 개인 키를 보관하고 자금을 완전히 제어할 수 있습니다. 계정 동결이나 타사 플랫폼 파산 위험이 없습니다.



**단순성**: 이메일 주소로 Lightning Address, 간단한 탭으로 NFC 결제, 기술 전문 지식이 필요 없는 직관적인 인터페이스.



**완벽한 에코시스템**: 모든 프로필(개인, 리테일러, 개발자)을 위한 도구로 필요에 맞게 모듈식으로 통합할 수 있습니다.



**전문 규정 준수**: 안전한 클라우드 호스팅, PCI-DSS 준수, 살바도르 규정 준수.



### 제한 사항



**라이트닝 제약 사항**: 영구적인 wallet 연결, 대용량에 대한 유동성 관리, 수신자가 오프라인일 경우 장애 위험 등이 필요합니다. 티엔키는 통합 LSP를 통해 이러한 측면을 완화합니다.



**SaaS 종속성**: 티안키를 사용할 수 없는 경우 인보이스 생성이 일시적으로 불가능합니다(자금은 안전하게 유지됨).



**개인정보**: 티안키는 트랜잭션 메타데이터(금액, 날짜)를 관찰할 수 있습니다. BTCPay 서버와 같은 자체 호스팅 솔루션보다 덜 비공개적입니다.



## 결론



티안키는 잘 설계된 인프라가 어떻게 Bitcoin의 일상 화폐로의 대량 채택을 막는 기술적 장벽을 제거할 수 있는지 보여줍니다. Lightning Network의 힘과 비수탁 접근 방식 및 접근 가능한 도구를 결합함으로써 이 생태계는 금융 주권과 사용 편의성 사이의 균형 잡힌 경로를 제공합니다.



판매자에게 티엔키는 거래 비용을 대폭 절감하는 동시에 새로운 고객층을 확보할 수 있는 기회를 제공합니다. 소비자 입장에서는 라이트닝 Address와 NFC 카드를 통해 기술적 복잡성 없이도 Bitcoin을 실용적인 통화로 전환할 수 있습니다.



Bitcoin의 광범위한 채택은 교육과 시간이 필요한 과제로 남아 있지만, 티안키와 같은 인프라는 기술 도구가 이미 존재한다는 것을 보여줍니다. Bitcoin 결제 간소화라는 미션은 더 이상 먼 미래가 아니라 누구나 도전할 수 있는 현실입니다.



## 리소스



### 공식 문서




- [티엔키이 공식 웹사이트](https://tiankii.com)
- [티엔키이 도움말 센터](https://help.tiankii.com)
- [IBI 신청](https://go.ibi.me)
- [판매자 대시보드](https://pay.tiankii.com)
- [명령 센터](https://cc.ibi.me)



### Wallet 연결 가이드




- [LNbits 연결](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [블루월렛(LNDHub) 연결](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [커넥트알비 Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [커넥트 스트라이크 Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### 커뮤니티




- [Lightning Network Plus](https://lightningnetwork.plus) - 라이트닝 교육 리소스
- [Bitcoin 비치](https://www.bitcoinbeach.com) - 살바도르의 순환 경제 이니셔티브 Bitcoin



### 관련 도구




- [Blink Wallet](https://blink.sv) - Wallet 라이트닝 호환 권장
- [LNbits](https://lnbits.com) - 자체 호스팅 wallet 솔루션
- [표준 Bolt 카드](https://github.com/boltcard) - NFC 카드의 기술 사양