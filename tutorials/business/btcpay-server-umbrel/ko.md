---
name: BTCPay 서버 - 엄브렐
description: 엄브렐에 BTCPay 서버를 설치 및 사용하여 Bitcoin 및 라이트닝 수락하기
---

![cover](assets/cover.webp)



Bitcoin 생태계에서 결제를 수락하는 것은 판매자와 기업 모두에게 중요한 과제입니다. 기존 솔루션은 은행(신용카드, Stripe, PayPal)이나 Bitcoin(BitPay, 코인베이스 커머스)을 막론하고 상당한 수수료를 부과하고 민감한 비즈니스 데이터를 수집하며 마음대로 거래를 차단하거나 검열할 수 있는 중개자에게 의존합니다. 이러한 의존성은 탈중앙화, 기밀성, 금융 주권이라는 Bitcoin의 기본 원칙에 위배됩니다.



이 문제에 대한 오픈소스 해답으로 BTCPay 서버가 떠오르고 있습니다. 이 자체 호스팅 결제 프로세서는 중개자나 추가 처리 수수료, 개인 정보 침해 없이 자체 Bitcoin 노드를 전문 인프라로 전환합니다. 2017년부터 글로벌 기여자 커뮤니티가 개발한 BTCPay 서버를 사용하면 Bitcoin 및 라이트닝 결제를 지갑으로 직접 받을 수 있으며, 자금에 대한 완전한 통제권을 항상 유지할 수 있습니다.



일반적으로 BTCPay 서버를 설치하려면 고도의 기술력이 필요합니다: 리눅스 서버 구성, 도커 숙달, SSL 인증서 관리 및 네트워크 보안과 같은 고급 기술이 필요합니다. 엄브렐은 Bitcoin 및 라이트닝 노드와 직접 통합된 원클릭 설치로 이러한 접근 방식을 혁신적으로 개선했습니다. 이러한 단순화 덕분에 이전에는 숙련된 기술자의 전유물이었던 작업을 누구나 쉽게 이용할 수 있습니다.



**이해해야 할 중요 사항**: 엄브렐의 BTCPay 서버는 기본적으로 로컬 네트워크에서만 작동합니다. 홈 네트워크에 연결된 모든 기기(컴퓨터, 스마트폰, 태블릿)에서 인보이스를 생성하고, 라이트닝 및 Bitcoin 결제를 수락하고, 계정을 관리할 수 있습니다. 이 구성은 대면 서비스 청구, 대면 결제 관리 또는 로컬 네트워크에서 BTCPay 서버를 사용하는 경우에 이상적입니다. 반면, 인터넷에서 공개적으로 액세스할 수 있는 온라인 스토어에 BTCPay 서버를 통합하려면 공개적으로 노출되는 추가 구성이 필요합니다(이 문제는 튜토리얼 마지막에 다룰 예정입니다).



이 튜토리얼에서는 엄브렐에 BTCPay 서버를 완전히 설치하고, Bitcoin wallet 및 라이트닝 노드를 구성하고, 인보이스를 생성 및 결제하고, 회계 보고를 관리하는 방법을 안내합니다. 로컬 네트워크에서 BTCPay 서버를 효율적으로 사용하는 방법을 알아본 다음, 이커머스 사이트와 통합하려는 경우 공개 디스플레이를 위한 솔루션을 살펴봅니다.



## 전제 조건



이 튜토리얼을 따라하려면 Umbrel을 올바르게 설치 및 구성해야 합니다. 아직 설치하지 않았다면 Umbrel 설치에 대한 튜토리얼을 참조하세요.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin 코어 노드는 블록체인과 완전히 동기화되어야 합니다(엄브렐의 Bitcoin 애플리케이션에서는 100% 동기화). 이 초기 동기화는 하드웨어와 인터넷 연결에 따라 보통 3일에서 2주가 소요됩니다.



즉시 라이트닝 결제를 수락하려면 엄브렐에 LND(Lightning Network Daemon)도 설치해야 합니다. 이 기능을 사용하려면 Umbrel에 LND 설치 및 구성에 대한 튜토리얼을 참조하세요.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

BTCPay 서버, 데이터베이스 및 Lightning 데이터를 위해 최소 50GB의 디스크 여유 공간을 확보하세요. 연결이 끊기지 않도록 이더넷 케이블을 통한 안정적인 인터넷 연결을 강력히 권장합니다.



## 엄브렐에 BTCPay 서버 설치하기



엄브렐 인터페이스(`umbrel.local`)에서 앱스토어에 접속하여 Bitcoin 카테고리에서 "BTCPay 서버"를 검색합니다.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



설치를 클릭합니다. Umbrel은 자동으로 Bitcoin Core 및 LND가 설치되었는지 확인한 다음 배포를 시작합니다(2~5분).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



설치가 완료되면 애플리케이션을 엽니다. 강력한 자격 증명을 사용하여 관리자 계정을 만들어야 합니다.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



계정이 생성되면 BTCPay 서버에서 즉시 첫 번째 스토어를 설정하라는 메시지가 표시됩니다. 비즈니스 이름을 선택하고 기준 통화(EUR, USD 또는 BTC)를 선택합니다.



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## 로컬 네트워크의 BTCPay 서버에 액세스



BTCPay 서버는 로컬 네트워크(WiFi 또는 이더넷)의 모든 기기에서 액세스할 수 있습니다. 브라우저에서 :



```url
http://umbrel.local
```



또는 직접 :



```url
http://umbrel.local:3003
```



**테일스케일을 통한 원격 액세스**: 전 세계 어디에서든 BTCPay 서버에 액세스하려면 Tailscale을 사용하세요. 이 보안 VPN을 사용하면 마치 로컬 네트워크에 있는 것처럼 엄브렐에 연결할 수 있습니다. 엄브렐의 테일스케일 전용 튜토리얼을 참조하세요.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin 포트폴리오 구성



결제를 수락하려면 Bitcoin wallet를 구성해야 합니다. BTCPay 서버는 대시보드에 구성 옵션을 표시합니다.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



wallet Bitcoin을 구성하려면 "지갑" > "Bitcoin"으로 이동합니다.



BTCPay에서 직접 새 포트폴리오를 생성하거나 기존 포트폴리오를 가져오는 두 가지 옵션이 있습니다. 가져오기에는 여러 가지 방법을 사용할 수 있습니다:




- 하드웨어 wallet** 연결(권장): Vault 애플리케이션을 통해 공개 키 가져오기
- wallet 파일 가져오기**(권장): 포트폴리오에서 내보낸 파일을 업로드합니다
- 확장 공개키**를 입력합니다: XPub/YPub/ZPub을 수동으로 입력합니다
- wallet QR코드 스캔** : 블루월렛, 코보 볼트, 패스포트 또는 스펙터 DIY에서 QR 코드를 스캔합니다
- wallet seed**(권장하지 않음)를 입력합니다: 12단어 또는 24단어 복구 문구를 입력합니다



![Options de création de portefeuille](assets/fr/06.webp)



이 튜토리얼에서는 새로운 Hot wallet을 생성할 예정이므로 개인 키는 엄브렐 서버에 저장됩니다. 이 경우 서버에 많은 양을 저장하지 않도록 정기적으로 콜드 wallet으로 자금을 옮기는 것이 좋습니다.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



구성이 완료되면 BTCPay 서버는 wallet이 on-chain 결제를 수락할 준비가 되었는지 확인합니다.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Network 활성화



라이트닝 결제를 즉시 수락하려면 지갑 > 라이트닝으로 이동하세요. 그런 다음 엄브렐에 LND 노드가 이미 설치되어 있으므로 "저장" 버튼을 클릭하기만 하면 BTCPay 서버와 라이트닝 노드 간의 연결이 유효합니다.



![Configuration du nœud Lightning](assets/fr/09.webp)



## 인보이스 생성 및 결제



BTCPay 서버 인터페이스에서 인보이스 > Invoice 생성으로 이동합니다. 금액을 입력하고 설명을 추가한 다음 생성을 클릭합니다.



![Création d'une nouvelle facture](assets/fr/10.webp)



그런 다음 '결제' 버튼을 클릭하여 인보이스를 표시할 수 있습니다. 그러면 BTCPay에서 GW21 주소와 Lightning 인보이스가 포함된 통합 QR코드(BIP30)가 포함된 인보이스를 생성합니다.



![Détails de la facture générée](assets/fr/11.webp)



고객은 호환되는 모든 wallet로 QR 코드를 스캔할 수 있습니다.



![Page de paiement avec QR code](assets/fr/12.webp)



결제가 완료되면 인보이스는 몇 초 만에 Lightning에 대해 '결제 완료'가 됩니다.



![Confirmation de paiement réussi](assets/fr/13.webp)



## 결제 관리 및 추적



'보고' 섹션의 '청구서' 탭에서 날짜, 금액, 상태, 결제 방법 등이 포함된 청구서의 전체 내역을 확인할 수 있습니다. 필요한 경우 내보낼 수 있습니다.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## 스토어 구성



BTCPay 서버를 사용하면 고유한 매개변수로 여러 스토어를 관리할 수 있습니다. 각 스토어는 이커머스 스토어, 실제 판매 시점 또는 서비스 청구와 같은 별도의 비즈니스 엔티티를 나타냅니다.



스토어 설정에는 몇 가지 중요한 섹션이 있습니다:



![Paramètres du magasin](assets/fr/15.webp)





- 일반 설정**: 상점 이름, 기준 통화(BTC, EUR, USD), 인보이스 만료 시간(기본 15분), 필요한 블록체인 확인 횟수
- 환율**: 환율 소스 및 법정통화/Bitcoin 변환 구성
- 결제 모양**: 결제 페이지의 모양(로고, 색상, 맞춤 메시지)을 사용자 지정합니다
- 이메일 설정**: 수령한 결제에 대한 이메일 알림 구성
- 액세스 토큰**: 전자상거래 통합을 위한 API 토큰 관리(WooCommerce, Shopify 등)
- 사용자**: 다양한 권한 수준(소유자, 게스트)으로 스토어에 대한 사용자 액세스 권한을 관리합니다
- 웹후크**: 회계 또는 ERP 시스템과 실시간 동기화를 위한 웹훅 구성



또한 BTCPay 서버는 전자상거래 통합, POS 시스템 및 추가 도구로 기능을 확장하는 플러그인 섹션을 제공합니다.



![Gestion des plugins](assets/fr/16.webp)



## 로컬 사용의 장점과 한계



**엄브렐에 비해 BTCPay 서버의 장점** :




- 완전한 주권: 개인 키와 자금에 대한 독점적 제어, 제3자가 결제를 동결하거나 검열할 수 없음
- 상당한 비용 절감: 기존 프로세서의 2~3%에 비해 Bitcoin 네트워크 비용(라이트닝의 경우 몇 센트)에 불과합니다
- 기밀성 극대화: 타사와의 등록, 신원 확인 또는 데이터 공유 없음
- 오픈 소스 아키텍처는 대규모 개발자 커뮤니티를 통해 투명성, 감사 가능성 및 지속 가능성을 보장합니다
- 고급 기술 없이도 엄브렐을 통해 간편하게 설치 가능



**중요한 제한 사항** :




- 로컬 네트워크 전용**: 엄브렐의 BTCPay 서버는 홈 네트워크에서만 액세스할 수 있습니다. 대면 결제, 프리랜서 서비스 또는 소규모 오프라인 비즈니스에는 적합하지만 공개적으로 액세스할 수 있는 온라인 스토어에는 적합하지 않습니다.
- 완전한 기술 책임: 노드 유지 관리, 정기 백업, 연결 모니터링
- 라이트닝 유동성 관리: 충분한 인바운드 용량을 갖춘 채널 개설 및 관리
- 커뮤니티 문서 및 포럼으로 제한된 지원, 상업용 고객 서비스 부서보다 더 많은 자율성이 요구됨



이러한 로컬 네트워크 제한은 고객이 인터넷 어디에서나 결제 페이지에 액세스할 수 있어야 하는 이커머스 스토어에 BTCPay 서버를 통합하는 데 있어 주요 장애물입니다.



## 모범 사례 및 안전



자동 엄브렐 백업을 활성화하고 외부 미디어(USB 스틱, 하드 디스크, 암호화된 클라우드)에 사본을 저장하세요. Bitcoin 시드(복구 문구)를 물리적으로 분리된 안전한 장소에 보관하세요. 라이트닝 복구를 위해 LND의 channel.backup 파일을 백업하세요.



Bitcoin 코어 동기화, 라이트닝 채널 및 BTCPay 서버 응답을 정기적으로 모니터링합니다. 간단한 주간 테스트: generate 및 몇 가지 사토시에 대한 청구서를 지불합니다. 엄브렐을 최신 상태로 유지합니다(보안 패치, 개선 사항). 주요 업데이트 전에 백업하세요. 전문가용으로 사용하려면 이메일/SMS 알림이 포함된 외부 모니터링(UptimeRobot)을 고려하세요.



## 온라인 스토어에 BTCPay 서버 공개 노출하기



BTCPay 서버를 웹 기반 전자상거래 스토어(WooCommerce, Shopify 등)에 통합하려면 고객이 로컬 네트워크뿐만 아니라 어디에서나 결제 페이지에 액세스할 수 있어야 합니다.



**솔루션: Nginx 프록시 관리자**



Nginx 프록시 관리자(엄브렐 앱스토어에서 사용 가능)를 사용하여 BTCPay 서버를 공개적으로 노출할 수 있습니다. 이 솔루션에는 :




- 도메인 이름(클래식 또는 DuckDNS, No-IP, Afraid.org를 통한 무료)
- 라우터에서 포트 포워딩(포트 80 및 443) 구성하기
- SSL 인증서를 자동으로 관리하는 Nginx 프록시 관리자 설치



이 구성에서는 서버가 인터넷에 노출되므로 추가적인 주의가 필요합니다(강력한 비밀번호, 2FA, 정기 업데이트). 이 전체 절차를 자세히 설명하는 전용 튜토리얼을 준비할 예정입니다.



## 결론



엄브렐의 BTCPay 서버는 Bitcoin 노드의 강력한 성능과 엄브렐의 단순성을 결합하여 모든 사람이 액세스할 수 있는 자체 호스팅 전문 결제 인프라를 구축합니다. 이러한 금융 주권에는 유지 관리 책임이 따르지만, 엄브렐은 처리 수수료 제거, 개인 정보 보호, 검열에 대한 저항, 자금의 완전한 통제와 같은 혜택에 비해 운영 부담을 크게 간소화합니다.



로컬 네트워크 사용은 이미 프리랜서 서비스 청구, 대면 결제, 소규모 오프라인 상점 또는 통제된 환경에서 Bitcoin 및 Lightning을 배우고 실험하는 등 광범위한 애플리케이션에 적용되고 있습니다. 공개 노출이 필요한 이커머스 요구 사항의 경우 Nginx Proxy Manager 솔루션이 있지만 추가 기술 구성이 필요하므로 전용 튜토리얼에서 자세히 설명할 것입니다.



사업을 운영하든, 신생 프로젝트를 운영하든, 단순히 실험을 하든, 엄브렐의 BTCPay 서버는 완전한 재정적 자율성을 제공합니다. 첫 번째 상점, 첫 번째 인보이스, 첫 번째 결제가 여러분의 주권 인프라로 직접 수신되는 것부터 시작됩니다.



## 리소스



### 공식 문서




- [BTCPay 서버 공식 웹사이트](https://btcpayserver.org)
- [BTCPay 서버 전체 문서](https://docs.btcpayserver.org)
- [깃허브 BTCPay 서버](https://github.com/btcpayserver/btcpayserver)
- [테일스케일 문서](https://tailscale.com/kb)


### 커뮤니티 및 지원




- [포럼 BTCPay 서버](https://chat.btcpayserver.org)
- [포럼 엄브렐](https://community.getumbrel.com)
- [레딧 r/BTCPayServer](https://reddit.com/r/BTCPayServer)