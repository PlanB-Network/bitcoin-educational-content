---
name: LNbits

description: 판매자 계정 플랫폼
---

![presentation](assets/lnbits-intro.webp)

# 회계 시스템


LNbits에는 수신 및 발신 자금을 제어하고, 웹스토어 또는 Hardware Wallet 또는 직접 구축한 ATM과 같은 장치를 연결할 수 있는 다양한 도구가 포함되어 있습니다. 사용자 유형은 다음과 같습니다:


- 자금 관리와 추가 기능을 위해 LNbits를 Interface로 사용하고자 하는 Wallet 소유자.
- Bitcoin 온체인 및 Lightning Network 결제를 수락하고자 하는 온라인 및 오프라인 판매자 또는 서비스 제공업체.
- Lightning Network 애플리케이션을 구축하려는 개발자.
- 회계 목적으로 자신의 노드를 LNbits 시스템과 통합하려는 노드 운영자.
- 사용자마다 요구사항이 모두 다릅니다. 저희는 모든 사용자가 자신에게 가장 적합한 방식으로 기능을 사용할 수 있도록 모듈식 방식으로 LNbits를 구축했습니다.


# Wallet 관리자


LNbits는 노드 관리자가 아닌 무료 오픈소스 회계 시스템입니다. 채널 관리는 LND 또는 c-lightning과 같은 펀딩 소스로 LNbits에 연결된 라이트닝 노드의 도메인입니다. LNbits 시스템의 수퍼유저 또는 관리 사용자는 계정 기능 및 내부 확장 기능의 전반적인 접근성과 구성을 관리할 책임이 있습니다.


LNbits는 사용자와 라이트닝 노드 사이에서 Interface 역할을 하며, 결제 네트워크를 관리하고 상호작용할 수 있는 간단하고 사용자 친화적인 방법을 제공합니다.


노드를 위한 "워드프레스 모듈형 프레임워크"라고 생각하면 됩니다. 다양한 사용 사례에 맞게 결합할 수 있는 확장 기능을 기반으로 하는 관리하기 쉬운 플랫폼입니다.


LNbits를 나만의 은행 재무 관리 소프트웨어라고 생각하세요. 노드는 결제할 수 있는 채널을 제공하며, LNbits는 노드와 함께 제공되는 하나 이상의 라이트닝 Wallet을 실행할 수 있도록 노드를 확장합니다. 이러한 지갑은 반드시 본인 소유일 필요는 없습니다. LN 노드 운영자로서 이미 충분한 채널 유동성과 자금을 보유하고 있으며 이제 친구, 가족, 자신의 상점 또는 기타 일반 상인에게 Bitcoin 은행 서비스를 제공하고자 한다고 가정해 보겠습니다.


노드의 다른 지갑과 모든 노드 유동성에 액세스하지 않고도 노드에서 "은행 계좌"를 개설할 수 있는 간단한 방법을 제공할 수 있습니다. 노드(은행)는 결제(입/출금)를 위한 전송 제공자 역할만 수행합니다.


참고: "고객"이 귀하의 노드에 있는 LNbits 은행 계좌에 입금하는 모든 자금은 귀하의 노드 LN 채널로 바로 이동합니다. 이는 귀하가 실제로 해당 자금의 실제 소유자라는 의미입니다. 여러분은 그들의 자금에 대해 큰 책임을 지게 됩니다. 악의적으로 자금을 가지고 도망치거나, 악의적으로 높은 수수료를 부과하지 마세요. 우리는 법정화폐 은행가들을 엿먹이고 싶지, 서로(Bitcoin 사용자)를 엿먹이고 싶지 않습니다.


# 데모 플랫폼


데모는 [https://legend.lnbits.com](https://legend.lnbits.com)에서 확인할 수 있습니다. 데모는 모든 기능을 갖추고 있으며 Lightning Network와 LNbits 및 LNURL의 기능에 대해 전반적으로 학습하는 데 사용할 수 있습니다. 사용을 막을 수는 없지만 프로덕션 설정에 사용하지 말아 주시기를 부탁드립니다. 저희는 새로운 기능을 테스트하기 위해 서버에서 자주 작업하고 있을 뿐만 아니라, 여러분 자신의 노드와 LNbits를 주권적인 방식으로 실행하도록 권장하고 싶습니다. 노드 운영이 현재로서는 너무 무리라고 생각되신다면, 오픈노드, 루나, 보타지와 같은 클라우드의 커스터디 펀딩 서비스나 텔레그램의 라이트닝 팁봇에 LNbits를 연결할 수 있습니다.


# LNbits 전단지


상인이나 건물 친구에게 몇 가지 기본 정보를 전달하고 싶으신가요? 모두가 사용할 수 있는 첫 번째 전단지를 발표하게 되어 매우 기쁩니다. 크기는 6페이지(2단 접기), 너비 3508, 높이 2480px의 전 세계적으로 일반적인 전단지 형식입니다.


판매자를 위한 LNbits: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


빌더를 위한 LNbits: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# 몇 가지 기본 사항


LNbits는 LNURL 프로토콜을 기반으로 작동하므로 요청은 https://clearnet 링크(자체 서명 인증서 허용되지 않음) 또는 http://v2/v3 onion 링크의 두 가지 형태로 유효합니다. 야생에서 사용할 수 있는 LNURLp/w QR코드 또는 NFC 카드와 같은 LNbits 서비스를 제공하려면 클리어넷(https)으로 LNbits를 열어야 합니다.


LNbits를 설치하기 전에 다음 일반 가이드를 읽고 LNbits가 무엇이며 어떤 가능성을 열어주는지에 대해 이해했는지 확인하세요.



- [LND 가이드](https://docs.lightning.engineering/) | LND 설치하기
- [LND 구성 예제](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND 설정
- [CLN 가이드](https://docs.corelightning.org/docs/installation) | CLN 설치하기
- [LUD](https://github.com/lnurl/luds) LNURL 사양 | [NIP](https://github.com/nostr-protocol/nips) Nostr 사양
- [Watchtower 실행](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | 매우 중요!


특정 사용 사례 시나리오에서 LNbits를 사용하는 자세한 가이드는 여기에서 확인하세요:



- [LNbits 시작하기](https://darthcoin.substack.com/p/getting-started-lnbits) | 서브스택 가이드
- [LNbits로 안전을 위한 할 일](https://youtu.be/i5FQf96e6zg) | 유튜브 동영상
- [Lightning Network의 프라이빗 뱅크](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | 서브스택 가이드
- [친구 및 가족을 위한 관리인 지갑 실행](https://darthcoin.substack.com/p/the-bank-of-lnbits) | 서브스택 가이드
- [소규모 레스토랑/호텔용 LNbits](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | 서브스택 가이드
- [LNbits 스트리머 코파일럿 사용](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | 서브스택 가이드
- [노스트락 마켓 시작하기](https://darthcoin.substack.com/p/lnbits-nostr-market) | 서브스택 가이드
- [학교 프로젝트나 축제 이벤트에 LNbits 사용](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) 서브스택 가이드



# LNbits 설치


## 기본 설치 가이드


LNbits는 모든 Linux OS 머신에 설치할 수 있습니다. 강력한 머신이나 서버가 필요하지 않으며, 데이터베이스를 위한 충분한 RAM 메모리와 약간의 디스크 공간만 있으면 됩니다. BTC/LN 노드(로컬 PC 또는 원격 VPS)와 별도로 실행하거나 노드와 동일한 머신에서 함께 실행하거나 번들 노드 소프트웨어 머신에 이미 설치되어 있을 수 있습니다.


가장 일반적인 패키지 관리자인 poetry와 nix 중에서 선택할 수 있습니다. 기본적으로 LNbits는 SQLite를 데이터베이스로 사용합니다. 부하가 많은 애플리케이션에 권장되는 PostgreSQL을 사용할 수도 있습니다. [다음은 poetry 또는 nix를 사용한 기본 설치 가이드입니다(https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


처음 사용하는 분들을 위해 특정 환경에서 LNbits를 실행하는 방법에 대한 자세한 단계별 가이드를 제공합니다:


- [클리어넷의 LNbits](https://ereignishorizont.xyz/lnbits-server/en/) 작성자: Axel
- [LNbits on a VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [클라우드플레어의 LNbits](https://www.nodeacademy.org/lnbits) 작성자: Leo


Nginx를 사용하여 PostgreSQ, LightningTipBot을 펀딩 소스로 사용하는 VPS에서 도커화된 설정](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)에 대한 동영상도 확인할 수 있습니다.


[더 많은 설치 시나리오는 여기](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server)를 참조하세요.


번들 소프트웨어 노드의 경우, LNbits에 대한 특정 문서를 참조하세요: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


기술적인 부분에 관심이 없고 펀딩 소스를 직접 호스팅하고 싶지 않다면 [LNbits SaaS 버전](https://saas.lnbits.com) (서비스형 소프트웨어)을 사용할 수 있습니다. 기본적으로 클라우드의 LNbits와 비슷하지만 다른 클라우드 솔루션에서는 대부분 제공되지 않는 펀딩 소스(예: 노드, LNbits Wallet, LNtipbot, 가짜 지갑 등)와 환경 변수를 직접 정의할 수 있습니다.


[특정 사용 사례에 대한 LNbits SaaS 사용 방법 상세 가이드](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools)를 참조하세요.


## 자금 출처


LNbits는 노드 관리 소프트웨어가 아니라 LND 또는 CLN 펀딩 소스를 기반으로 하는 LN 중심의 회계 시스템입니다. 처음 설치한 후에는 http://localhost:5000/ 에서 LNbits를 방문하실 수 있습니다.


펀딩 소스를 수정하려면 슈퍼유저 URL로 이동하여 '서버 관리'에서 펀딩 소스를 선택하거나, `.env`에서 `adminUI=TRUE`를 설정한 경우 `LNBITS_BACKEND_WALLET_CLASS`를 필요한 소스로 수정하여 .env 파일을 편집합니다.


디렉터리에 있는 파일을 나열하는 명령을 `ls -a`로 확장하면 lnbits/ 또는 lnbits/apps/data 폴더에서 .env 파일을 찾을 수 있습니다.


원하는 펀딩 소스를 선택하여 추가 패키지를 설치하거나 추가 설정 단계를 수행해야 할 수도 있습니다. 다시 시작하면 새 설정이 활성화됩니다.


LNbits에 어떤 펀딩 소스를 사용할 수 있나요?


LNbits는 다양한 라이트닝 네트워크 펀딩 소스에서 실행할 수 있습니다. 현재 코어라이트닝, LND, LNbits, LNPay, OpenNode를 지원하며, 정기적으로 더 많은 펀딩 소스가 추가되고 있습니다.

유동성이 좋고 좋은 피어가 연결된 소스를 선택하는 것이 중요합니다. 공공 서비스에 LNbits를 사용하면 사용자 결제가 양방향으로 원활하게 이루어질 수 있습니다.


백엔드 Wallet(펀딩 소스)은 '.env' 파일 또는 수퍼유저 계정 내 관리-서버 섹션에서 다음 LNbits 환경 변수를 사용하여 구성할 수 있습니다.

.env 버전을 사용하려면 여기에서 매개 변수를 찾을 수 있습니다:



### CoreLightning


- CLN
  - `lnbits_backend_wallet_class`: **CoreLightningWallet**
  - 코어라이트닝_rpc`: /파일/경로/라이트닝-RPC
- 스파크(c-라이트닝)
  - `lnbits_backend_wallet_class`: **스파크월렛**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND(REST)
  - `lnbits_backend_wallet_class`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `lnd_rest_cert`: /파일/경로/tls.cert
  - lnd_rest_macaroon`: /파일/경로/admin.macaroon 또는 Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND(gRPC)
  - `lnbits_backend_wallet_class`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: 포트
  - `lnd_grpc_cert`: /파일/경로/tls.cert
  - lnd_grpc_macaroon`: /파일/경로/admin.macaroon 또는 Bech64/Hex

대신 AES 암호화 마카롱(자세한 정보)을 사용할 수도 있습니다


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

마카롱을 암호화하려면 `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`를 실행합니다.


### LNbits(또 다른 LNbits 인스턴스)



- 클라우드 서버 또는 자체 홈 서버에서 호스팅되는 LNbits 인스턴스
  - `lnbits_backend_wallet_class`: **엘엔비츠월렛**
  - lnbits_endpoint`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits 레전드 데모 서버 (!! 프로덕션/상업용으로 사용하지 마시고, 테스트용으로만 사용하세요 !!)
  - `lnbits_backend_wallet_class`: **엘엔비츠월렛**
  - lnbits_endpoint`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### 라이트닝 팁봇


텔레그램에서 [라이트닝 팁봇](https://t.me/LightningTipBot)을 연결하려면, 다음 파라미터를 설정해야 합니다:


  - `lnbits_backend_wallet_class`: **LnTipsWallet**
  - lnbits_endpoint`: https://LN.tips
  - `LNBITS_KEY`: 키를 얻으려면, 텔레그램에서 라이트닝팁봇과 비공개 대화에서 /api를 한 번 실행해야 합니다.


또한 이 튜토리얼에서 [vps를 통해 라이트닝팁봇과 함께 LNbits 설치하기](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)를 참조하세요


### IBEX 허브


여기](https://ibexpay.ibexmercado.com/onboard)에 등록한 다음 거기에서 키/토큰을 받으세요(엔드포인트는 https://ibexpay-api.ibexmercado.com).

자세한 내용은 [IBEX API-문서](https://ibexpay-api.readme.io/reference/getting-started-with-your-api)를 참조하세요.


### LNPay

Invoice 리스너가 작동하려면 LNbits에 공개적으로 액세스할 수 있는 URL이 있어야 하며, "Wallet 수신" 이벤트와 함께 `<귀하의 LNbits 호스트>/Wallet/웹훅`을 가리키는 [LNPay 웹훅](https://dashboard.lnpay.co/webhook/)을 설정하고 비밀을 제공하지 않아야 합니다. 설정 `https://mylnbits/Wallet/webhook`은 결제에 대한 알림을 받는 엔드포인트 URL이 됩니다.


  - `lnbits_backend_wallet_class`: **LNPayWallet**
  - lnpay_api_endpoint`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Invoice가 작동하려면 LNbits에 공개적으로 액세스할 수 있는 URL이 있어야 합니다. 웹훅 설정은 선택 사항입니다.


  - `lnbits_backend_wallet_class`: **오픈노드지갑**
  - `opennode_api_endpoint`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby는 LN Wallet 기능을 갖춘 브라우저 확장 프로그램으로, LNbits의 자금 출처로 사용할 수 있는 LNDHUB 계정을 제공합니다. [자세한 내용은 여기를 참조하세요(https://getalby.com/).


Invoice가 작동하려면 LNbits에 공개적으로 액세스할 수 있는 URL이 있어야 합니다. 수동 웹훅 설정은 필요하지 않습니다. 여기에서 generate에 Alby 액세스 token을 설정할 수 있습니다: https://getalby.com/developer/access_tokens/new



- `lnbits_backend_wallet_class`: AlbyWallet
- alby_api_endpoint`: https://api.getalby.com/
- 알비_액세스_토큰`: 알비액세스토큰


## 추가 / 문제 해결 가이드


필요한 경우를 대비하여 몇 가지 추가 지침을 알려드립니다. 화살표를 클릭하면 설명이 펼쳐집니다.


### 킬스위치 🚨


최근 전체 공간뿐만 아니라 LNbits에서도 위험한 버그가 너무 많이 발생하여 이에 대한 조치를 취하기로 결정했습니다. 이제 자금 손실로 이어질 수 있는 취약점이나 버그가 다시 발생할 경우 경고를 받거나 직접 조치를 취하도록 선택할 수 있습니다.


![killswitchn](assets/lnbits-killswitch.webp)


무효로 전환하면 인스턴스의 모든 사용자 유형에 노란색 배너가 표시되며, 오른쪽 위 테마/언어 영역 옆에 "LNbits는 베타 버전입니다"라는 알림이 표시되며, 이는 가장 확실한 힌트로서 문제가 발생했음을 나타냅니다. 창 왼쪽의 Green에서 강조 표시된 새 서버 탭을 살펴보세요.


어떻게 작동하나요? 킬스위치가 활성화되면 LNbits 코어 팀만 사용할 수 있는 비밀 깃허브 리포지토리가 X분 간격(지정 가능)으로 점검됩니다. 이 리포지토리에 취약한 버그가 게시되면 구독한 모든 설치에서 킬스위치를 트리거하는 신호로 작용하여 lnbits 인스턴스가 비어 있는 Wallet을 사용하도록 전환합니다. 클라우드가 해제되고 보안 업데이트를 설치한 경우 서버 관리 섹션을 통해 펀딩 소스를 노드, Wallet 또는 사용 중인 다른 것으로 다시 설정할 수 있습니다. 이 위키에는 무엇을 구성해야 할지 모르는 경우 펀딩 소스 전환에 대한 섹션이 있습니다.



### 관리자와 수퍼유저의 차이점


LNbits 관리자 UI를 사용하면 LNbits 프론트엔드를 통해 LNbits 설정을 변경할 수 있습니다. 이 기능은 기본적으로 비활성화되어 있으며, '.env' 파일에서 환경 변수 `LNBITS_ADMIN_UI=true`를 처음 설정하면 설정이 초기화되어 사용됩니다. 그 이후부터는 데이터베이스의 해당 설정 대신 .env 파일의 설정이 사용됩니다.


### 슈퍼 사용자


관리자 UI에서는 서버에 액세스할 수 있는 슈퍼 유저를 도입하여 펀딩 소스 변경과 같이 서버를 다운시키거나 프론트엔드 및 API를 통해 응답하지 않을 수 있는 설정을 변경할 수 있도록 했습니다. 수퍼 유저는 데이터베이스의 설정 테이블에만 저장됩니다. 설정을 "기본값으로 재설정"하고 다시 시작하면 새로운 수퍼 유저가 생성됩니다. 또한 슈퍼 사용자의 존재 여부를 확인하기 위해 API 경로에 데코레이터를 추가했습니다. 해당 ID는 API와 프론트엔드를 통해 전송되지 않으며 수퍼 유저인지 여부만 부울(예/아니요)로 받습니다.


슈퍼 유저만 "충전" 섹션을 통해 다른 지갑에 사토시를 충전할 수 있습니다.


슈퍼 유저가 생성되면 웹훅을 통해 다른 서비스에 게시할 수도 있습니다. 자세한 정보는 여기 https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`에서 확인하세요


프런트엔드에서 서버 관리 섹션을 열고 테마 -> 사용자 지정 로고를 선택하면 "Wallet 생성" 페이지에 표시되는 상점 이미지를 변경할 수도 있습니다.


### 관리자 사용자


환경 변수: 쉼표로 구분된 사용자 ID 목록인 `LNBITS_ADMIN_USERS`. 관리자 사용자는 관리자 UI에서 설정을 변경할 수 있지만, 펀딩 소스 설정은 서버를 다시 시작해야 하고 서버에 액세스할 수 없게 될 수 있으므로 예외로 합니다. 또한 `LNBITS_ADMIN_EXTENSIONS`에 있는 모든 확장 기능에 액세스할 수 있습니다.


### 허용된 사용자


환경 변수: 쉼표로 구분된 사용자 ID 목록인 `LNBITS_ALLOWED_USERS`. 이러한 사용자를 정의하면 일반인은 더 이상 LNbits를 사용할 수 없게 됩니다. 그러면 정의된 사용자와 관리자만 LNbits 프론트엔드에 액세스할 수 있습니다.




#### LNbits 업데이트

LNbits 로컬 인스턴스의 일반적인 업데이트는 다음 CLI 명령을 복사하여 붙여넣기만 하면 됩니다:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


라스피블리츠나 마이노드를 실행하는 경우에는 추가로

```
sudo systemctl restart lnbits
```

를 서비스 형태로 실행하기 때문입니다.


엄브렐/시타델에서 명령은 다음과 같습니다

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### SQLite에서 PostgreSQL로의 마이그레이션


이미 SQLite 데이터베이스에 LNbits를 설치하여 실행 중인 경우, LNbits를 대규모로 실행할 계획이라면 포스트그레스로 마이그레이션할 것을 적극 권장합니다.


마이그레이션을 쉽게 수행할 수 있는 스크립트가 포함되어 있습니다. Postgres가 이미 설치되어 있어야 하며 사용자의 비밀번호가 있어야 합니다(위의 Postgres 설치 가이드 참조). 또한 마이그레이션을 수행하기 전에 데이터베이스 Schema을 구현하기 위해 Postgres에서 LNbits 인스턴스를 한 번 실행해야 합니다:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

이제 모든 것이 작동하고 마이그레이션되기를 바랍니다... LNbits를 다시 시작하고 모든 것이 제대로 작동하는지 확인합니다.



#### 데이터베이스 백업 및 복원


백업 및 복원 프로세스에 대한 자세한 가이드](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore)를 참조하세요.



#### 내 노드에서 내 LNbits Wallet에 펀딩이 작동하지 않습니다


LNbits의 펀딩 소스인 동일한 노드에서 Sats을 보내려면 LND.conf 파일을 편집해야 합니다.


포함할 매개 변수는 다음과 같습니다: `allow-circular-route=1`입니다


LND.conf의 애플리케이션 옵션 섹션에서 그렇게 하세요. 일부 번들 노드에서는 그렇지 않으면 LND의 시작이 실패할 수 있습니다.


참고: 대신 "충전" 옵션이 있는 새로운 adminUI 확장 프로그램을 사용하여 LNbits 계정에 자금을 추가하는 것이 좋습니다.


#### 오류 426

오류가 발생했습니다: "공개적으로 액세스 가능한 https 도메인 또는 토르를 통해 lnurl을 전송해야 합니다. 426 업그레이드 필요"</summary>


이 오류는 일반적으로 ngnix 터널 뒤에 있는 LNbits가 LNURL Address을 올바르게 전달하지 않기 때문에 발생합니다. LNbits를 중지하고 이 줄을 추가하여 .env 파일을 편집하세요:

전달된_허용_IPS=*`


또한 ngnix 설정을 사용하는 경우 ngnix 구성에 이러한 헤더가 있는지 확인하세요:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### 네트워크 오류

QR을 스캔할 때 'https 오류', '네트워크 오류' 등이 발생했어요</summary>


나쁜 소식이지만, 이는 여러 가지 이유가 있을 수 있는 라우팅 오류입니다. 먼저 [라이트닝 디코더](https://lightningdecoder.com/)로 QR의 LNURL을 확인하여 이상한 점을 발견할 수 있는지 확인하세요. 가장 가능성이 높은 몇 가지 문제와 그 해결책을 시도해 보겠습니다.


LNbits는 Tor를 통해서만 실행되며, lnbits.yourdomain.com과 같은 공개 도메인에서는 열 수 없습니다



- 설정을 이 상태로 유지하려면 .onion URI를 사용하여 LNbits Wallet을 열고 다시 생성하세요. 이렇게 하면 이 .onion URI를 통해서만 액세스할 수 있도록 QR이 생성되므로 토어를 통해서만 액세스할 수 있습니다. 인터넷을 통해서는 연결할 수 없고 홈-LAN 내에서만 연결할 수 있으므로 .local URI에서 해당 QR을 generate로 만들지 마세요.
- 해당 QR을 스캔할 때 사용했던 LN Wallet 앱을 열고 이번에는 토어를 사용합니다(Wallet 앱 설정 참조). 앱에서 토르를 제공하지 않는 경우, 대신 Orbot(Android)을 사용할 수 있습니다. 클리어넷/https용 LNbits를 여는 방법에 대한 자세한 지침은 설치 섹션을 참조하세요.



#### 다른 사람이 내 LNbits에서 지갑을 생성하지 못하도록 차단하기


클리어넷에서 LNbits를 실행하면 기본적으로 모든 사람이 generate을 Wallet로 바꿀 수 있습니다. 노드의 자금이 이러한 지갑에 묶여 있기 때문에 이를 방지하고 싶을 수 있습니다. 이를 방지하는 방법에는 두 가지가 있습니다:


.env` 파일에서 허용되는 사용자 및 확장자를 구성합니다([여기에서 env 예제 참조](https://github.com/lnbits/lnbits/blob/main/.env.example)). .env 파일에 `adminUI=FALSE` 설정을 사용하는 경우에만 작동하며, 그렇지 않은 경우에는 서버 관리 섹션 -> 사용자 -> 허용된 사용자에서 설정해야 합니다. 그 이후에는 다른 모든 사용자는 허용되지 않습니다.




#### Invoice 만료 기간 사용자 지정하기


이제 사용자 지정 만료일을 사용하여 인보이스를 generate로 만들 수 있습니다. 백엔드와 호환됩니다: LndRest지갑, Lnd지갑, CoreLightning지갑, 에클레어지갑, Lnbits지갑, 스파크지갑까지!


.env 파일에서 `LIGHTNING_INVOICE_EXPIRY`를 설정하거나 AdminUI를 사용하여 모든 인보이스에 대한 기본값을 변경할 수 있습니다. 또한 /api/v1/payments 엔드포인트에 JSON 데이터에서 만료를 설정할 수 있는 새 필드가 있습니다.




## Wallet-URL 삭제됨


### 데모 서버의 Wallet legend.lnbits


지갑용 Wallet-URL, Export2phone-QR 또는 LNDhub 사본을 항상 안전한 곳에 보관하세요. LNbits는 분실 시 복구에 도움을 드릴 수 없습니다.


### 자체 펀딩 소스/노드의 Wallet

항상 지갑용 Wallet-URL, Export2phone-QR 또는 LNDhub의 사본을 안전한 곳에 저장하세요. 모든 LNbits 사용자 및 Wallet-ID는 LNbits 사용자 관리자 확장 프로그램 또는 sqlite 데이터베이스에서 찾을 수 있습니다. LNbits 데이터베이스를 편집하거나 읽으려면 LNbits /data 폴더로 이동하여 sqlite.db라는 파일을 찾습니다. 엑셀 또는 [SQLite 브라우저](https://sqlitebrowser.org/)와 같은 전용 SQL 편집기를 사용하여 파일을 열고 편집할 수 있습니다.


또한 CLI을 통해 지갑을 덤프하고 데이터베이스 내의 모든 Wallet를 확인할 수 있습니다.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


출력은 다음과 같이 표시됩니다


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

이 값을 다음과 같은 URL에 넣으려고 합니다


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


여기서 f8a43fc363ea428db5c53b3559935f1f를 이름 앞에 오는 값으로 바꾸고(예제에서는 f8a43fc363ea428db5c53b3559935f1f) 1280ff5910a9c485a782a2376f338b6c가 사용자이고 이름 뒤에 표시되는 값이 되어야 합니다. Sqlite3를 종료하려면


```
.quit
```

#### 라이트닝-Address의 경우 LNURL, 그 반대도 마찬가지입니다


이 [인코더](https://lnurl-codec.netlify.app/) 또는 [이 인코더](https://lightningdecoder.com/)를 사용해 보세요. LNURLp를 결제하거나 확인하려면 [LNurlpay](https://wwww.lnurlpay.com/)를 사용할 수도 있습니다. HTTP가 아닌 HTTPS라고 표시되어야 합니다.



#### 내 LNURLp QR로 결제할 때 사람들이 볼 수 있는 댓글 구성하기

LNURL-p를 생성하면 기본적으로 댓글 상자가 채워지지 않습니다. 즉, 결제에 댓글을 첨부할 수 없습니다.


댓글을 허용하려면 상자의 글자 길이를 1에서 250까지 추가합니다. 숫자를 입력하면 결제 프로세스에 댓글 상자가 표시됩니다. 이미 생성된 LNURL-p를 편집하여 해당 번호를 추가할 수도 있습니다.


![lnbits comments](assets/lnbits-comments.webp)


#### 온체인 BTC를 LNbits에 입금하기

온체인 BTC에서 Exchange Sats로 전환하는 방법은 두 가지가 있습니다(각각 LNbits로 전환).


##### 외부 스왑 서비스를 통해.


LNb에 액세스할 수 없는 다른 사용자는 [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) 또는 [ZigZag](https://zigzag.io/)와 같은 스왑 서비스를 사용할 수 있습니다. 이는 LNbits 인스턴스에서 LNURL/LN 인보이스만 제공하지만, 결제자는 온체인 Sats만 가지고 있어 먼저 해당 Sats을 스왑해야 하는 경우에 유용합니다. 절차는 간단합니다. 사용자가 온체인 비트코인을 스왑 서비스에 전송하고 LNbits의 LNURL/LN Invoice를 스왑 대상자로 제공합니다.


##### 온체인과 볼츠 LNbits 확장 프로그램 사용.


이는 LN 자금 출처에서 LNbits가 "귀하의 Wallet"로 표시하는 LN btc가 아닌 별도의 Wallet라는 점을 명심하시기 바랍니다. 이 온체인 Wallet는 LNbits 볼츠 또는 디지 확장 프로그램을 사용하여 LN 비트코인을 (예: 하드웨어 지갑)으로 스왑하는 데에도 사용할 수 있습니다. LN 결제를 위해 LNbits와 연결된 웹샵을 운영하는 경우, LN의 모든 Sats을 온체인으로 정기적으로 배출하는 것이 매우 편리합니다. 이렇게 하면 LN 채널에 더 많은 공간을 확보하여 새로운 Sats을 받을 수 있습니다.


Bitcoin Hardware Wallet이 없는 사용자를 위한 절차:



- 일렉트럼 또는 Sparrow wallet을 사용하여 새로운 온체인 Wallet을 생성하고 백업 seed를 안전한 장소에 저장합니다.
- Wallet 정보로 이동하여 xpub를 복사합니다.
- LNbits - 온체인 확장으로 이동하여 해당 xpub으로 새 Watch-only wallet를 생성합니다.
- LNbits - Tipjar 확장으로 이동하여 새 Tipjar를 생성합니다. LN Wallet 외에 온체인 옵션도 선택합니다.
- 선택 사항 - LNbits - SatsPay 확장으로 이동하여 온체인 비트코인에 대한 새 청구를 생성합니다. 온체인과 LN 또는 둘 다 중에서 선택할 수 있습니다. 그러면 공유할 수 있는 Invoice이 생성됩니다.
- 선택 사항 - 워드프레스 + 우커머스 페이지에 연결된 LNbits를 사용하는 경우, Watch-only wallet를 생성/연결하여 LN btc 상점 Wallet에 연결하면 고객은 같은 화면에서 두 가지 결제 옵션을 모두 사용할 수 있습니다.


LNbits로 결제를 받으면 거래 로그에는 재개된 유형의 거래만 표시됩니다.


![lnbits payment details](assets/lnbits-payment-details.webp)


거래 개요에서 받은 자금에는 작은 Green 화살표가, 송금한 자금에는 빨간색 화살표가 표시됩니다.


해당 화살표를 클릭하면 세부정보 팝업에 첨부된 메시지와 발신자 이름이 표시되는 경우 발신자 이름이 표시됩니다.


결제 시 이름을 표시하도록 구성하는 것은 현재 LNbits에서는 불가능하며, 수신만 가능합니다. 이는 발신자의 LN Wallet이 [OBW, 블릭스트, 앨비, ZBD, 비트바나나](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents)와 같이 [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md)(nameDesc)을 지원하는 경우에만 가능합니다.


그러면 LNbits 거래의 세부 정보 섹션에 별칭/가명이 표시됩니다(화살표 클릭). 여기에 어떤 이름이라도 입력할 수 있으며, 실제 발신자의 이름과 관련이 없을 수도 있습니다.


![lnbits namedesc](assets/lnbits-namedesc.webp)


Wallet 앱에서 LNbits 계정을 가져오려면 사용하려는 계정/Wallet으로 LNbits를 열고 "확장 프로그램 관리"로 이동하여 LNDHUB 확장 프로그램을 활성화하세요. LNDHUB 확장 프로그램을 열고 사용하려는 Wallet을 선택한 다음 해당 Wallet에 대해 원하는 보안 수준에 따라 "관리자" 또는 "Invoice 전용" QR을 스캔합니다.


제우스](https://zeusln.app/) 또는 [블루월렛](https://bluewallet.io/)을 lndhub 계정의 Wallet 앱으로 사용할 수 있으며, BW는 이러한 Wallet을 두 개 이상 지원합니다.


이 작업을 수행할 때 LN 네트워크 URI를 자신의 노드 중 하나로 설정하는 것이 좋습니다. LNbits 인스턴스가 토르 전용인 경우, 토르가 활성화된 앱도 사용해야 합니다. 또한 이 경우 Tor .onion Address을 통해 LNbits 페이지를 열어야 합니다.


On-Chain 확장에서 ypub를 사용할 때 "지원되지 않는 Hash 유형" 오류가 발생하는 경우, LNbits 인스턴스가 파이썬 3.10을 사용하는지 확인하여 [이 문제](https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python)의 영향을 받을 수 있습니다. 스택오버플로우 답변에 설명된 대로 openssl.cnf를 수정하고 LNbits를 다시 시작하세요.



## LNbits를 사용한 툴링 및 빌드


LNbits는 수많은 사용 사례를 위해 다양한 기기를 프로그래밍하고 연결할 수 있는 모든 종류의 [오픈 API](https://legend.lnbits.com/docs)와 도구를 제공합니다.


메이커비트를 처음 접하는 분이라면 벤 아크의 [메이커비트 프레젠테이션](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos)을 통해 LNbits를 기반으로 가젯을 제작하는 방법을 알아보세요.


### 중요:


- LNbits는 LNURL 프로토콜을 기반으로 작동하며, 요청은 https://clearnet 링크(자체 서명 인증서 허용되지 않음) 또는 http://v2/v3 onion 링크의 두 가지 형태로 유효합니다. 야생에서 사용할 수 있는 LNURLp/w QR코드 또는 NFC 카드와 같은 LNbits 서비스를 제공하려면 LNbits를 clearnet(https)으로 열어야 합니다.
- Esp32에 전원을 공급할 때는 데이터 케이블만 사용하세요. 모든 케이블이 esp에 전원을 공급하는 것 외에 데이터를 지원하는 것은 아닙니다. esp와 함께 제공된 케이블이 전원 전용 케이블인 경우 다음과 같이 하세요
- 다른 장치가 연결된 상태에서 USB 허브를 사용하지 마세요. 이렇게 하면 디버깅에 Hard인 이상한 효과(예: 시작 또는 중지되지 않음)가 발생할 수 있습니다.
- MacOS에서 esp 프로젝트를 구현하려면 UART 브리지 드라이버가 필요합니다. Mac 또는 Linux 시스템에서 드라이버에 문제가 있는 경우 여기에서 드라이버를 찾을 수 있으며, TTGO 디스플레이가 관련된 경우 여기에서 드라이버를 찾을 수 있습니다. Windows를 사용 중이고 연결에 문제가 있는 경우 최신 버전이 작동하지 않으므로 구버전 11.1.0을 다운로드하세요! 또한 여기에서 직렬 터미널을 찾아 연결 상태를 확인할 수 있습니다(전송 속도 115200으로 설정).
- Platform.io를 사용하는 것이 훨씬 더 편하지만(예: 종속성이 자동으로 설치됨), 빌드를 처음 시작하는 사람에게는 Arduino를 사용하는 것을 권장합니다.
- TT-Go 디스플레이 S3: 화면 보호 필름의 탭 색상을 보면 어떤 컨트롤러(ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..)를 사용하여 제작했는지 알 수 있습니다. 직접 프로그래밍했는데 화면에 잘못된 색상, 미러링된 이미지, 가장자리의 픽셀 이탈 등 그래픽이 올바르게 표시되지 않는 경우 디버깅할 수 있도록 보관해 두세요. 이 작업을 수행해야 하는 경우 다양한 디스플레이에 맞게 조정하는 방법에 대한 훌륭한 가이드가 있습니다
- 항상 LNURLl239xx 대신 소문자 lnurl239xx를 사용합니다
- Lightning:lnurl1234xyz를 추가하면 스캔 시 이 Wallet에 대해 사용자 Invoice을 열도록 요청하는 QR이 생성됩니다(iOS에서는 마지막으로 설치된 라이트닝 앱, Android에서는 설정)
- 웹을 통해 esp32를 플래싱하는 경우 해당 브라우저(TL:DR Chrome, Edge 및 Opera)에서만 작동합니다.
- Esp에 대한 이 핀아웃 참조를 참고하세요
- 포스소프트웨어나 포스가이드를 사용할 때는 항상 작성자를 링크하세요. 누구나 아기가 성장하는 모습을 보는 것을 좋아하며, 보는 것만으로도 멋진 빌딩 체인이 시작됩니다:)


프로젝트에 도움이 필요하시면 [메이커비츠 텔레그램 그룹](https://t.me/makerbits)으로 오세요 - 저희가 도와드리겠습니다!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


다음은 LNbits로 구축할 수 있는 몇 가지 프로젝트 카테고리입니다:



- [노스트르 서명 장치](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [아케이드 머신](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [거티](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [노스트르 잽 램프](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [번개 피기](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin 스위치](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [자판기](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [볼티](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [너드마이너](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin 티커](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [로라와 메시 네트워킹](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [도우미 및 리소스](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- ["LNbits로 구동되는" 프로젝트의 더 많은 예는 여기](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits)에서 확인하세요.
- [LNbits 사용 사례](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)