---
name: LNbits Server
description: Phoenixd가 설치된 Ubuntu VPS 또는 Umbrel에 자체 호스팅된 LNbits 서버 설치 및 구성
---

![cover](assets/cover.webp)



LNbits는 모든 라이트닝 백엔드(LND, Core Lightning, Phoenixd)를 완전한 서비스 플랫폼으로 변환하는 오픈 소스 웹 인터페이스입니다. 이 자체 호스팅 솔루션을 사용하면 자금에 대한 완전한 통제권을 유지하면서 여러 라이트닝 포트폴리오를 개별적으로 관리하고, 판매 시점을 배포하고, 기부 시스템이나 청구 서비스를 만들 수 있습니다.



이 튜토리얼에서는 두 가지 설치 방법을 다룹니다: *phoenixd가 포함된 *VPS 우분투**(전체 Bitcoin 노드가 없는 경량 솔루션)와 **엄브렐**(기존 LND 노드와 통합). 개념과 확장 기능을 다루는 Plan ₿ Academy의 일반 LNbits 튜토리얼과 달리, 이 가이드는 단계별 기술 설치 절차에 중점을 두고 있습니다.



## LNbits란 무엇인가요?



LNbits는 기존 백엔드(LND, Core Lightning, Phoenixd)에 연결되는 Python(FastAPI)으로 개발된 라이트닝 계정 시스템입니다. 기존 라이트닝 노드와 달리 LNbits는 자체 API 키로 여러 개의 격리된 포트폴리오를 관리할 수 있는 액세스 가능한 인터페이스를 제공합니다. 가족, 직원 또는 프로젝트를 위한 하위 계정을 만들 수 있으며, 이들에게 모든 자금에 대한 액세스 권한을 부여하지 않아도 됩니다.



분리된 아키텍처는 정보를 SQLite(기본값) 또는 PostgreSQL(프로덕션)에 저장하고, 자금은 Lightning 백엔드에서 계속 관리합니다. 이러한 분리는 이식성을 보장하므로 사용자 데이터의 손실 없이 Phoenixd에서 LND로 마이그레이션할 수 있습니다.



## 주요 기능



엘엔비츠는 다양한 **확장 시스템**을 제공합니다: TPoS(POS), 페이월(콘텐츠 수익화), 이벤트(티켓팅), LndHub(블루월렛용 서버), Bolt 카드(NFC 결제), 분할 결제(자동 배포), 사용자 관리자(인증을 통한 사용자 관리) 등이 있습니다.



대시보드**에는 실시간 잔액, 거래 내역, 청구 도구가 표시됩니다. 각 wallet에는 API 키가 포함된 고유 URL이 있어 기존 로그인 없이도 액세스할 수 있습니다. 3단계 API 키 시스템**(관리자, 인보이스, 읽기 전용)은 안전한 통합을 위해 권한을 세밀하게 제어할 수 있습니다.



LNbits는 기본적으로 **LNURL**(LNURL-pay, LNURL-withdraw, LNURL-auth)을 구현하고 **Lightning Address**을 지원하여 최신 라이트닝 지갑과의 호환성을 보장하고 전문 서비스 배포를 용이하게 합니다.



## 지원 플랫폼



**우분투 VPS**: 전체 Bitcoin 노드가 없는 경량 솔루션. 사전 요구 사항: vCPU 1개, 1~2GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. 공개 노출을 위해 HTTPS + 도메인 이름 필요(LNURL 서비스).



**엄브렐**: 앱 스토어에서 간편하게 설치할 수 있습니다. 전제 조건: 동기화된 LND 및 개방형 채널을 갖춘 기능적인 Umbrel 노드. 자동 구성.



아래는 엄브렐 및 엄브렐 LND 튜토리얼에 대한 링크입니다:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Phoenixd를 사용하여 Ubuntu VPS에 설치하기



### 1단계: VPS 서버 보호



**설치하기 전에**, 기술 규칙에 따라 Ubuntu VPS 서버를 보호해야 합니다. 이 단계는 인프라와 라이트닝 자금을 보호하기 위해 **중요한** 단계입니다.



다음은 시작하는 데 도움이 되는 자세한 가이드입니다: **[초기 Ubuntu 서버 구성 - 단계별 가이드](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)**(작성자: Daniel P. Costas).



이 가이드에서는 사용자 구성, 보안 SSH, 방화벽(UFW), fail2ban, 자동 업데이트 및 시스템 보안 모범 사례에 대해 설명합니다.



### 2단계: Phoenixd 설치



서버가 안전해지면 Phoenixd를 설치하고 구성해야 합니다. Plan ₿ Academy에서는 설치, seed 세대 및 시스템d 서비스 구성을 다루는 포괄적인 전용 튜토리얼을 제공합니다:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Phoenixd가 실행되면 (`./phoenix-cli getinfo`로 확인), `~/.phoenix/phoenix.conf`에 **HTTP 비밀번호**를 적어두세요 - LNbits를 Phoenixd에 연결하려면 이 비밀번호가 필요합니다.



### LNbits 배포



UV를 설치하고 LNbits를 복제합니다:


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Phoenixd 백엔드를 구성합니다:


```bash
cp .env.example .env && nano .env
```



.env`에 추가합니다:


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



'uv run lnbits --host 0.0.0.0 --port 5000'으로 테스트한 다음 `Wants=phoenixd.service`로 시스템드 서비스를 생성합니다.



## 초기 설정 및 첫 사용



### 슈퍼유저 활성화



.env`에서 관리자 인터페이스를 활성화합니다:


```
LNBITS_ADMIN_UI=true
```



LNbits를 재시작(`sudo systemctl restart lnbits`)하고 슈퍼유저 ID를 검색합니다:


```bash
cat ~/lnbits/data/.super_user
```



관리 패널로 이동하여 `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>`로 이동합니다. '서버' 메뉴에서 펀딩 소스, 확장 프로그램 및 사용자 계정을 구성할 수 있습니다.



### 안전한 계정 만들기



*공개 노출에 **중요**: 인터넷에서 액세스할 수 있는 공개 도메인 이름에 LNbits 인스턴스를 노출하는 경우 사용자 계정의 무료 생성을 비활성화하는 것이 **중요**합니다.



슈퍼유저 관리 인터페이스에서 '설정'으로 이동한 다음 '사용자 관리' 섹션으로 이동합니다. 거기에서 "새 사용자 만들기 허용" 옵션을 찾을 수 있습니다.



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**도메인이름이 있는 공개 전시회의 경우** :




- '새 사용자 생성 허용' 옵션을 비활성화**해야 합니다
- 이 보호 기능이 없으면 인터넷에 있는 누구나 인스턴스에서 계정을 만들 수 있습니다
- 공격자는 사용자 모르게 계정을 생성하고 라이트닝 노드의 유동성을 사용할 수 있습니다
- 슈퍼유저 인터페이스에서 사용자 계정을 수동으로 만들어야 합니다



**로컬 전용** :




- 인스턴스가 로컬에서만 액세스할 수 있는 경우 이 옵션은 덜 중요합니다(http://localhost:5000)
- 그러나 이 옵션을 비활성화하는 것이 일반적인 안전 수칙입니다



일단 구성이 완료되면 슈퍼유저 관리자만 '사용자' 인터페이스를 통해 새 사용자 계정을 만들 수 있습니다. 이 접근 방식은 누가 라이트닝 인프라에 액세스하고 자금을 사용할 수 있는지 완벽하게 제어할 수 있도록 보장합니다.



### 첫 번째 채널 열기



Phoenixd는 자동 유동성을 통해 채널을 자동으로 관리합니다. LNbits에서 ~30,000 sats의 라이트닝 인보이스를 생성하고 다른 wallet에서 결제합니다. Phoenixd가 자동으로 ACINQ에 채널을 개설합니다. 개설 수수료(~20-23천 sats)가 공제되고, on-chain 확인 후 잔액(~7-10천 sats)이 표시됩니다.



./phoenix-cli getinfo`로 상태를 확인합니다. 그런 다음 채널 개방을 제어하기 위해 자동 유동성을 비활성화(`phoenix.conf`에서 `auto-liquidity=off`)하는 것을 고려하세요.



### 공개 디스플레이 및 HTTPS



**중요**: 공개 표시 시 HTTPS 필수(API 키 보안 + LNURL 호환성). 로컬에서만 사용하려면 이 단계를 건너뛰세요.



**캐디(권장)**: 자동 SSL. sudo apt install -y caddy`, `/etc/caddy/Caddyfile`을 편집합니다:


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


다시 시작합니다: 'sudo systemctl 재시작 캐디'.



**Nginx** : 더 많은 제어. 엔지눅스 인증봇 파이썬3-certbot-nginx`를 설치하고, `/etc/nginx/sites-available/lnbits`를 생성합니다:


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


활성화: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl 재로드 nginx && sudo certbot --nginx -d your-domain.com`



.env`에 추가: `FORWARDED_ALLOW_IPS=*`



## 엄브렐 설치



### 앱 스토어에서 배포



엄브렐 앱 스토어로 이동하여 "LNbits"를 검색한 후 "설치"를 클릭합니다.



![Installation LNbits Umbrel](assets/fr/01.webp)



엄브렐은 필요한 종속성을 자동으로 확인합니다. LNbits를 사용하려면 라이트닝 노드(LND)가 필요합니다. 라이트닝 노드가 이미 작동 중이라면 "LNbits 설치"를 클릭하여 확인합니다.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel은 Docker 이미지를 다운로드하고, LND과의 연결을 자동으로 구성한 후 컨테이너를 시작합니다(2~5분). 설치는 전적으로 백그라운드에서 이루어집니다.



### 초기 슈퍼유저 구성



처음 실행할 때 LNbits는 슈퍼유저 관리자 계정을 만들라는 메시지를 표시합니다. 관리 인터페이스에 대한 액세스를 보호하기 위해 사용자 이름과 보안 비밀번호를 입력합니다.



![Configuration SuperUser](assets/fr/03.webp)



**중요**: 이 슈퍼유저 계정은 LNbits 인스턴스에 대한 모든 권한을 가집니다. 강력한 비밀번호를 선택하고 안전하게 보관하세요.



계정을 생성하면 자동으로 기본 관리 인터페이스로 이동합니다. 엄브렐은 이미 LND을 자금 출처로 설정해 두었으므로 모든 라이트닝 결제는 기존 채널을 통해 이루어집니다.



### 관리자 인터페이스에 액세스



왼쪽 메뉴에서 '설정'을 클릭하여 전체 관리 패널에 액세스합니다.



![Interface Settings](assets/fr/04.webp)



'지갑 관리' 섹션에는 구성에 대한 주요 정보가 표시됩니다:




- 펀딩 소스** : LndBtcRestWallet(LND 엄브렐 노드에 직접 연결)
- 노드 잔액** : 라이트닝 채널에서 사용 가능한 총 유동성
- LNbits 잔액**: LNbits 시스템에 할당된 자금(초기 0sats)



이제 생성한 모든 LNbits 지갑에 대해 엄브렐 노드의 유동성을 직접 활용할 수 있습니다. 추가 구성이 필요하지 않습니다. LNbits는 이미 실행 중입니다.



### 사용자 관리



LNbits의 가장 강력한 기능 중 하나는 각각 비밀번호 인증과 격리된 지갑을 갖춘 여러 독립 사용자를 생성할 수 있다는 점입니다. 이러한 아키텍처를 통해 엄브렐 노드의 유동성을 활용하면서 비즈니스, 가족, 직원, 프로젝트 등 다양한 용도에 따라 완전히 분리된 하위 계정을 제공할 수 있습니다.



사이드 메뉴에서 "사용자"를 클릭하여 사용자 관리에 액세스합니다. '계정 만들기'를 클릭하여 새 사용자를 추가합니다.



![Gestion des utilisateurs](assets/fr/05.webp)



사용자 생성 양식을 작성합니다:




- 사용자 아이디**: 로그인 사용자 이름(예: "satoshi")
- 비밀번호 설정**: 인증 비밀번호를 설정하려면 이 옵션을 활성화합니다
- 비밀번호** 및 **비밀번호 반복**을 입력합니다: 이 사용자의 비밀번호를 설정합니다



![Création utilisateur satoshi](assets/fr/06.webp)



최소한의 구성을 위해 선택 필드(Nostr 공개 키, 이메일, 이름, 성)는 비워 둘 수 있습니다. "계정 만들기"를 클릭하여 확인합니다.



![Confirmation utilisateur créé](assets/fr/07.webp)



이제 새 사용자가 고유 식별자 및 사용자 이름과 함께 사용자 목록에 표시됩니다.



![Liste des utilisateurs](assets/fr/08.webp)



**중요 사항**: 각 사용자는 자신의 비밀번호로 완전히 독립적으로 로그온할 수 있습니다. 슈퍼유저 관리자는 관리 인터페이스를 통해 모든 권한을 보유합니다.



### 사용자 wallet 관리



이제 "satoshi" 사용자가 생성되었으므로 wallet 라이트닝을 할당해야 합니다. 해당 사용자의 wallet 아이콘(두 번째 아이콘)을 클릭한 다음 "새 지갑 만들기"를 클릭합니다.



![Gestion des wallets](assets/fr/09.webp)



wallet의 이름을 지정하라는 대화 상자가 나타납니다. 설명이 포함된 이름(예: "Wallet Of Satoshi")을 입력하고 표시 통화(CUC, USD, EUR 등)를 선택합니다.



![Création wallet](assets/fr/10.webp)



"생성"을 클릭합니다. LNbits는 즉시 이 사용자를 위해 작동하는 wallet 라이트닝을 생성합니다.



![Confirmation wallet créé](assets/fr/11.webp)



이제 두 개의 기존 지갑, 즉 자동으로 생성된 기본 wallet "LNbits wallet"와 새로운 "Satoshi의 Wallet"이 표시됩니다. 사용자 환경을 단순화하기 위해 삭제 아이콘(빨간색 휴지통)을 클릭하여 기본 wallet를 삭제할 수 있습니다.



![Wallet final unique](assets/fr/12.webp)



이제 "satoshi" 사용자는 명확하게 식별되는 하나의 wallet을 갖게 됩니다. 각 wallet 사용자는 기본 LND 노드의 유동성을 사용하면서 완전히 자율적으로 운영됩니다.



**핵심 개념**: 이 모든 지갑은 엄브렐 노드의 글로벌 유동성을 공유합니다. 각 wallet에 대해 새로운 라이트닝 채널을 만들지 않아도 됩니다. LNbits는 기존 라이트닝 인프라 내에서 자금 할당을 관리하는 지능형 회계 계층 역할을 합니다. 이것이 바로 LNbits의 멀티 wallet 시스템의 힘입니다.



### 사용자 로그인



슈퍼유저 계정(오른쪽 상단의 아이콘)에서 로그아웃하고 LNbits 로그인 페이지로 돌아갑니다. 이제 새 사용자의 자격 증명으로 로그인할 수 있습니다.



![Connexion utilisateur satoshi](assets/fr/13.webp)



이전에 정의한 사용자 이름("satoshi")과 비밀번호를 입력한 다음 "로그인"을 클릭합니다. 사용자는 관리 인터페이스에서 완전히 분리된 개인 wallet에 직접 액세스할 수 있습니다.



### Interface 사용자의 wallet



로그인하면 사용자는 전체 wallet Lightning 인터페이스에 액세스합니다.



![Interface wallet utilisateur](assets/fr/14.webp)



인터페이스의 특징은 :




- 현재 잔액**: sats 및 선택한 통화(이 예에서는 CUC)로 표시됩니다
- 주요 작업**: 요청 붙여넣기, 송장 생성, QR 아이콘(빠른 스캔)
- 거래 내역** : 모든 결제 및 영수증 전체 목록
- 오른쪽 패널**: 구성 및 액세스 옵션



### wallet에 대한 모바일 액세스



오른쪽 패널은 특히 실용적인 기능인 wallet에 대한 모바일 액세스를 제공합니다. "모바일 액세스" 섹션을 펼쳐서 사용 가능한 옵션을 확인하세요.



![Mobile Access](assets/fr/15.webp)



LNbits는 스마트폰에서 wallet을 사용할 수 있는 여러 가지 방법을 제공합니다:



**옵션 1: 호환되는 모바일 애플리케이션




- 앱스토어 또는 구글플레이에서 **제우스** 또는 **블루월렛**을 다운로드하세요
- 이 wallet에 대해 LNbits에서 **LndHub** 확장을 활성화합니다
- 모바일 앱으로 LndHub QR 코드를 스캔하여 wallet를 연결합니다



**옵션 2: 모바일 브라우저를 통한 직접 액세스**




- "QR 코드를 사용하여 휴대폰으로 내보내기"에 표시되는 QR 코드에는 통합 인증이 적용된 wallet의 전체 URL이 포함되어 있습니다
- 스마트폰에서 이 QR 코드를 스캔하면 모바일 브라우저에서 바로 wallet을 열 수 있습니다
- 빠른 액세스를 위해 홈 화면에 페이지 추가



**중요 보안**: 이 URL에는 wallet에 대한 전체 액세스를 위한 API 키가 포함되어 있습니다. 절대 공개적으로 공유하지 마세요. 이 QR 코드를 Bitcoin 개인 키와 마찬가지로 취급하세요. 이 QR 코드를 스캔하는 사람은 누구나 wallet에 대한 전체 액세스 권한을 갖게 됩니다.



이 모바일 기능은 자체 호스팅 노드 덕분에 자금에 대한 완전한 주권을 유지하면서 여러분과 친구들을 위한 진정한 라이트닝 wallet 서버로 LNbits 엄브렐 인스턴스를 전환합니다.



### 사용자 액세스 공유



이 다중 사용자 구성의 주요 사용 사례는 **가족 또는 가까운 지인들과 지갑을 공유하는 경우**입니다. 전용 wallet(예시에서는 "satoshi")로 사용자를 생성한 후에는 이 로그인 자격 증명을 신뢰할 수 있는 가족 구성원과 공유할 수 있습니다.



*엄브렐의 *액세스 보안**: 에만 액세스할 수 있으므로 Umbrel에서 LNbits 인스턴스에 대한 액세스는 당연히 보호됩니다:




- 로컬 네트워크**에서: 동일한 WiFi/이더넷 네트워크에 연결된 가족 구성원이 인스턴스에 액세스할 수 있습니다
- VPN을 통해**: 엄브렐 서버에 구성된 Tailscale과 같은 VPN을 사용하는 경우, 권한이 부여된 사용자는 안전한 원격 액세스를 할 수 있습니다



이 이중 보호 계층(네트워크 액세스 + 사용자 인증) 덕분에 Umbrel에서는 "새 사용자 생성 허용" 옵션이 덜 중요합니다. 네트워크 또는 VPN에 이미 액세스 권한이 있는 사람만 로그인 인터페이스에 액세스할 수 있습니다.



**일반적인 시나리오**: "아빠" 계정, "엄마" 계정, "비즈니스" 계정 등을 생성합니다. 각 가족 구성원은 각자의 격리된 wallet Lightning을 보유하면서 엄브렐 노드의 공유 유동성을 활용할 수 있습니다. 사용자 이름과 비밀번호를 공유하기만 하면 로컬 네트워크의 모든 기기에서 또는 Tailscale VPN을 통해 연결할 수 있습니다. 자세한 내용은 Tailscale 전용 튜토리얼을 참조하세요:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 사용 가능한 확장 기능 살펴보기



슈퍼유저 인터페이스로 돌아가서 왼쪽 패널의 '확장 프로그램' 메뉴에 액세스하여 전체 LNbits 확장 프로그램 생태계를 살펴보세요.



![Extensions disponibles](assets/fr/16.webp)



LNbits는 인스턴스를 진정한 Lightning 서비스 플랫폼으로 전환하는 다양한 확장 카탈로그를 제공합니다:





- 주크박스**: sats 기반 주크박스 시스템(Spotify 결제)
- 지원 티켓**: 유료 지원 시스템(질문에 답변하기 위해 SATS 수신)
- TPoS**: 소매업체를 위한 안전한 모바일 POS 단말기
- 사용자 관리자**: 고급 사용자 및 wallet 관리(방금 사용한 것)
- 이벤트**: 이벤트 티켓 판매 및 유효성 검사
- LNURLDevices**: POS 관리, ATM, 커넥티드 스위치
- SMTP**: 사용자가 이메일을 보내고 SATS를 적립할 수 있도록 합니다
- 볼트카드**: Lightning 탭 투 페이 결제를 위한 NFC 카드 프로그래밍하기
- NostrNip5**: 도메인에 NIP5 주소 생성
- 분할 결제**: 여러 지갑 간에 결제를 자동으로 분배



각 확장 프로그램은 이 인터페이스에서 한 번의 클릭으로 활성화할 수 있습니다. '무료'로 표시된 확장 프로그램은 무료이며, 일부는 '유료' 버전으로 제공됩니다. 카탈로그를 살펴보고 비즈니스, 가족 관리, Lightning Network의 기능 실험 등 필요에 맞는 확장 프로그램을 찾아보세요.



## 장점과 한계



**혜택**: 재무 주권(자금/키/데이터의 전체 제어), 아키텍처 유연성(무손실 VPS→full node 마이그레이션), 전문 확장 시스템, 직관적인 인터페이스.



**제한 사항** : 소프트웨어 베타 버전(금액에 대한 주의), 보안은 관리자 책임, 민감한 API 키가 포함된 URL(HTTPS 필수), 다중 사용자 관리에는 관리 책임이 수반됩니다.



## 모범 사례



**백업**: Phoenixd Seed/LND 자격증명, LNbits 데이터베이스, .env 파일. 매일 자동화하고, 프로덕션 서버에서 분리하여 암호화합니다. 정기적으로 복원을 테스트합니다.



**유지 관리**: 정기적으로 업데이트(LNbits, Lightning 백엔드, 운영 체제)를 확인합니다. 주요 업데이트 전에 항상 릴리스 노트를 확인하세요.





- 엄브렐**에서: App Store에서 새 버전을 자동으로 알려줍니다. "확장 프로그램 관리" > "모두 업데이트"를 통해 확장 프로그램을 동기화하세요. Umbrel 자동 백업에 SQLite 데이터베이스가 포함되어 있는지 확인하세요.
- VPS**에서: 'cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits'로 수동으로 업데이트합니다. 시스템 로그 모니터링: sudo journalctl -u lnbits -f`.



## 결론



LNbits 셀프 호스팅은 라이트닝 재정 주권을 위한 구체적인 경로를 제공합니다. VPS+Phoenixd는 빠른 서비스를 위한 경량 솔루션을 제공하며, 기존 Bitcoin 노드와 Umbrel을 완벽하게 통합합니다. 확장 가능한 아키텍처를 통해 단순한 다중 사용자 wallet에서 정교한 비즈니스 사용 사례로 발전할 수 있습니다.



셀프 호스팅은 책임감을 수반합니다: 시드 백업, 액세스 보호, 적당한 양으로 시작하기. 이러한 예방 조치를 통해 LNbits는 탈중앙화와 자율성을 유지하면서 라이트닝 경제를 위한 강력한 솔루션이 될 수 있습니다.



## 리소스



### 공식 문서




- [LNbits 문서](https://docs.lnbits.org)
- [엘엔비츠 깃허브](https://github.com/lnbits/lnbits)
- [피닉스드 깃허브](https://github.com/ACINQ/phoenixd)
- [공식 설치 가이드](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### 커뮤니티 가이드




- [초기 Ubuntu 서버 구성](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) 작성자: Daniel P. Costas(단계별 VPS 보안)
- [우분투 VPS에 LNbits + Phoenixd 설치](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) 작성자 Daniel P. Costas(전체 가이드)
- 악셀의 [클리어넷의 LNbits 서버](https://ereignishorizont.xyz/lnbits-server/en/)
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes