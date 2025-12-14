---
name: Phoenixd
description: Phoenixd로 나만의 미니멀한 라이트닝 노드 배포하기
---

![cover](assets/cover.webp)



재정적 자율성은 라이트닝 인프라를 제어할 수 있다는 의미이기도 합니다. Bitcoin 라이트닝을 애플리케이션에 통합하고자 하는 개발자와 기업에게는 자동 유동성 관리 기능을 갖춘 미니멀하고 특화된 라이트닝 노드인 **Phoenixd**가 이상적인 솔루션이 될 수 있습니다.



Phoenixd는 ACINQ에서 개발한 라이트닝 서버로, HTTP API를 통해 라이트닝 결제를 송수신하기 위해 특별히 설계되었습니다. LND이나 코어 라이트닝과 같은 완전한 기능을 갖춘 구현과 달리, Phoenixd는 채널 관리의 모든 복잡성을 추상화하면서 자금의 자체 보호 기능을 유지합니다.



이 튜토리얼에서는 자체 호스팅 인프라와 사용하기 쉬운 API를 사용하여 Phoenixd를 설치, 구성 및 사용하여 Lightning 애플리케이션을 개발하는 방법을 살펴봅니다.



## Phoenixd란 무엇인가요?



Phoenixd는 ACINQ에서 개발한 최소한의 전문화된 라이트닝 노드입니다. Full node의 관리 복잡성 없이 애플리케이션에 Lightning을 통합하고자 하는 개발자와 기업을 위해 설계된 솔루션입니다.



### 작동 원리



**Phoenixd는 자동 유동성을 위해 ACINQ를 LSP(라이트닝 서비스 제공자)로 사용하는 최소한의 라이트닝 노드입니다. 라이트닝 결제를 받으면 자동으로 ACINQ 노드와 채널을 열어 필요한 수신 용량을 할당합니다. 이 "즉각적인" 유동성은 즉각적으로 제공되지만, 수신 금액의 정확히 **1% + Mining 수수료**가 부과됩니다.



**자동화된 관리:** 시스템은 세 가지 주요 Elements를 관리합니다:




- 라이트닝** 채널: 필요에 따라 자동으로 열고, 닫고, 관리
- 수신/발신 유동성**: 스플라이싱 및 채널 개방을 통한 자동 프로비저닝
- 수수료 크레딧** : 채널을 정당화하기에 부족한 소액 결제 금액은 향후 청구에 대비한 충당금으로 저장됩니다



### Phoenixd 혜택



**개인 키(12단어 seed)와 자금은 사용자가 관리합니다. Phoenixd는 키를 공유하지 않고 로컬에서 Wallet를 생성합니다.



**개인 인프라:** Phoenixd는 회원님의 서버에서 실행되므로 자세한 로그, 구성, API 제어에 액세스할 수 있습니다. 더 이상 자금 액세스를 위해 타사 서비스에 의존하지 않아도 됩니다.



**통합 API:** Phoenixd는 다른 서비스와의 통합, 기본 LNURL 지원 및 사용자 지정 애플리케이션 개발을 위한 HTTP API를 제공합니다.



**간편한 통합: ** 간단한 REST API 덕분에 Phoenixd는 라이트닝 결제가 필요한 모든 애플리케이션이나 서비스에 통합할 수 있습니다.



**중요 참고: ** 자동 유동성은 여전히 LSP(라이트닝 서비스 제공자)로서 ACINQ에서 제공합니다. Phoenixd는 자동 채널 관리를 위해 Phoenix 모바일과 동일한 메커니즘을 사용합니다.



## Phoenixd 설치



### 전제 조건



Phoenixd를 사용하려면 몇 가지 기본 명령줄 기술을 갖춘 Linux 환경(Ubuntu/Debian 권장)이 필요합니다. 최적의 성능을 위해서는 다음이 필요합니다:





- Linux 서버**: 안정적인 연결이 가능한 VPS 또는 로컬 머신
- OpenJDK 21** : 자바 런타임 환경
- 안정적인 인터넷 연결**: Lightning Network과의 동기화용
- 도메인 이름** (선택 사항) : API에 대한 안전한 HTTPS 액세스용



### 다운로드 및 설치



**1. Phoenixd** 다운로드



GitHub 릴리스] 페이지(https://github.com/ACINQ/phoenixd/releases)로 이동하여 아키텍처에 맞는 최신 버전을 다운로드하세요:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. 첫 시작



초기화를 위해 Phoenixd를 시작합니다:



```bash
./phoenixd
```



처음 실행하면 "알겠습니다" 를 입력하여 두 가지 중요한 단계를 확인하라는 메시지가 표시됩니다:



**메시지 1 - 백업:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**이 12단어를 저장하세요** - 복구에 대한 유일한 보장입니다.



**메시지 2 - 자동 유동성:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



각 확인에 '이해합니다'를 입력합니다.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd가 처음으로 시작: 백업 확인 및 자동 유동성*을 제공합니다



**3. 서비스 내 구성** (프랑스어로만 제공)



지속적인 운영을 위해 시스템드 를 생성합니다:



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*2m sat*에서 시스템드 및 '자동 유동성'을 통해 Phoenixd 서비스가 활성화 및 운영 중입니다



## 구성 및 보안



### 구성 파일



Phoenixd는 필수 파라미터로 `~/.phoenix/phoenix.conf`를 자동으로 생성합니다:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**주요 매개변수:**




- '자동 유동성': 자동으로 열리는 채널의 크기(기본값: 2M Sats)
- http-password`: API용 관리자 비밀번호(Invoice 생성 및 결제 발송)
- http-password-limited-access`: 제한된 비밀번호(Invoice 생성에만 해당)



### HTTPS를 통한 보안 액세스



기본적으로 Phoenixd API는 로컬 HTTP(`http://127.0.0.1:9740`)를 통해서만 액세스할 수 있습니다. 외부(모바일 애플리케이션, 다른 서버, 웹 통합)에서 노드를 사용하려면 보안 HTTPS 액세스를 구성해야 합니다.



**역방향 프록시 원칙:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx**는 **역방향 프록시** 역할을 합니다. 포트 443에서 인터넷의 HTTPS 요청을 수신하여 로컬(포트 9740)에서 Phoenixd로 리디렉션한 다음 암호화된 응답을 클라이언트로 다시 보냅니다.



**SSL/TLS** 인증서는 디지털 파일로 :




- 서버의 신원 증명**(중간자 공격 방지)
- HTTPS** 암호화 사용: API 비밀번호를 포함한 모든 데이터는 전송 중에 암호화됩니다
- 렛츠 인크립트에서 인증봇 도구를 통해 무료로 발급**합니다



이 구성을 사용하면 다음을 수행할 수 있습니다:




- 인터넷에서 API에 대한 안전한 액세스**
- 전송 중 API** 비밀번호 암호화(일반 텍스트로 전송되는 것을 방지하기 위해)
- Phoenixd**를 HTTPS가 필요한 외부 애플리케이션에 통합하세요
- 금융 API에 대한 보안 표준** 준수



이 HTTPS 역방향 프록시를 nginx로 구성합니다:



**1. Nginx** 구성



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. SSL** 인증서



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### 기능 테스트



Phoenixd가 제대로 작동하는지 확인합니다:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



이러한 명령은 노드의 상태 및 잔액에 대한 JSON 정보를 반환합니다(초기에는 비어 있음).



![Commandes CLI](assets/fr/03.webp)



*Getinfo 및 getbalance 명령으로 노드 상태 확인*



## API 사용



### 첫 번째 수신 테스트



**1. 라이트닝** Invoice 생성



API를 사용하여 첫 번째 Invoice를 만들 수 있습니다:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### 자동 유동성 메커니즘 이해



**기본 원칙: ** 라이트닝 결제를 받을 때, Phoenixd는 때때로 새로운 채널을 개설해야만 결제를 받을 수 있습니다. 이 채널 개설에는 수수료가 발생하며, 수령 금액에서 **자동으로 공제**됩니다.



**100,000 Sats의 구체적인 예시:**



![Premier test de réception](assets/fr/04.webp)



*첫 번째 승인 테스트: Sats 10만 수령, 유동성 비용 공제 후 최종 잔액 Sats 75.561달러*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**수수료 계산: **




- 서비스 요금**: 채널 용량의 1%(2,115,000Sats) = 21,150Sats
- Mining 수수료**: ~3,289 Sats(On-Chain 거래의 경우)
- 합계**: 24,439 Sats 자동 공제됨



**CLI 명령어로 확인:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*결제 송금 후 최종 잔액: 라이트닝 배송 후 257Sats 잔여분*



**소액 결제에 대한 수수료 크레딧: ** 채널 개설을 정당화하기에는 너무 적은 금액(약 2만 5천원 미만)을 받는 경우, 환불되지 않는 '수수료 크레딧'으로 저장됩니다. 이 크레딧은 향후 충분한 금액이 입금될 때 채널 수수료를 지불하는 데 사용됩니다.



**2. 채널 개설 팔로우**



Phoenixd 로그를 확인하세요:



```bash
journalctl -u phoenixd -f
```



채널이 열리고 유동성 수수료가 자동으로 차감되는 것을 확인할 수 있습니다. 수수료는 Mempool Bitcoin 조건에 따라 다르지만 항상 1%의 서비스 수수료와 현재 Mining 수수료가 포함됩니다.



**3. 채널 확인**



```bash
./phoenix-cli listchannels
```



이 명령은 활성 채널의 상태와 잔액을 표시합니다.



### 전체 API 작업



Phoenixd는 포트 9740에 REST API를 노출하여 :



**기본 작업:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**비용 관련 중요 사항:**




- 영수증**: 1% + 자동 유동성 수수료 Mining
- 배송**: 0.gW-27의 경우 4%의 라우팅 수수료



**웹훅: 웹훅을 사용하면 이벤트(결제 수신, Invoice 결제, 채널 오픈 등)가 발생하면 Phoenixd가 애플리케이션에 **자동으로 알림**을 보낼 수 있습니다. 애플리케이션은 Phoenixd에 지속적으로 업데이트를 요청하는 대신 즉각적인 HTTP 알림을 받습니다.



**고객이 주문 금액을 결제하면 온라인 스토어에서 자동으로 알림을 수신하여 거래를 즉시 확인할 수 있습니다.



Phoenix.conf`에서 구성합니다:


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## 고급 애플리케이션



### LNURL 통합



Phoenixd는 고급 통합을 위해 기본적으로 LNURL 프로토콜을 지원합니다:



**LNURL-Pay:** LNURL 호환 서비스 결제


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** LNURL 서비스에서 자금 검색


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** 라이트닝을 통한 서비스 액세스 인증


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### LNbits와 통합



LNbits는 [공식 문서](https://docs.lnbits.org/guide/wallets.html)에 따라 Phoenixd를 펀딩 소스로 사용할 수 있습니다:



**LNbits 구성:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



이 통합을 통해 여러 개의 라이트닝 지갑을 관리하기 위한 웹 기반 Interface을 제공하는 Phoenixd 노드로 구동되는 LNbits 하위 계정을 생성할 수 있습니다.



### 사용자 지정 애플리케이션



포괄적인 REST API 덕분에 :



**전자 상거래: ** 라이트닝 결제를 스토어에 직접 통합합니다


**기부 서비스:** 인보이스 및 자동 웹후크가 포함된 기부 시스템


**소셜 네트워킹 봇:** 팁 기능이 있는 텔레그램/디스크 봇


**페이월 라이트닝:** 라이트닝 요금으로 프리미엄 콘텐츠 이용 가능



## 안전 및 모범 사례



### 액세스 보호



**API 비밀번호: ** 자동 생성된 비밀번호는 Lightning 보관함의 열쇠입니다. 절대 공유하지 마시고, 의심스러운 경우 변경하세요.



**방화벽:** 포트 9740을 인터넷에 직접 열어두지 마세요. 항상 HTTPS와 함께 nginx를 사용하세요.



**인증 강화:** 서버에 대한 액세스를 인증된 장치로만 제한하려면 VPN 또는 Tailscale을 고려하세요.



### 필수 백업



**seed 복구:** 12개의 단어를 서버에서 떨어진 안전한 장소에 저장하세요. 이것이 유일한 복구 보장입니다.



*~/.phoenix 디렉토리:** 채널 상태를 유지하고 복원 속도를 높이려면 이 폴더를 정기적으로 백업하세요(Phoenixd가 종료된 후).



**서비스 복구 코드:** Phoenix로 2FA를 활성화하는 모든 서비스에 대한 백업 코드도 보관하세요.



### 모니터링 및 유지 관리



**모니터링 로그:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**업데이트: ** 새 버전은 [GitHub 릴리스](https://github.com/ACINQ/phoenixd/releases)에서 확인하세요. 업데이트는 바이너리를 교체하고 서비스를 다시 시작하기만 하면 됩니다.



## 대안과의 비교



### 피닉스d 대 피닉스 표준



**피닉스 표준(모바일) :**




- ✅ 즉시 설치, 설정 필요 없음
- ✅ Interface 모바일 직관성
- ✅ Phoenixd와 동일한 자동 저장
- 개발자용 API 없음
- ❌ 상세 로그에 액세스할 수 없음



**Phoenixd(서버) :**




- ✅ 통합을 위한 HTTP API
- ✅ 로그에 대한 전체 액세스 권한
- ✅ 개인 인프라
- ❌ 기술력 필요
- ❌ 서버 유지 관리 필요



**두 회사 모두 자동 유동성을 위해 ACINQ를 LSP로 사용합니다.



### Phoenixd 대 LND/코어 라이트닝



**LND/코어 라이트닝 :**




- ✅ 완벽한 제어, 전체 라이트닝 프로토콜
- ✅ 대규모 커뮤니티, 성숙한 에코시스템
- 복잡한 수동 유동성 관리
- ❌ 큰 학습 곡선



**피닉스드 :**




- ✅ 자동 유동성 관리(예: Phoenix 모바일)
- ✅ 개발자용 API
- ✅ 간소화된 구성
- aCINQ를 LSP로 사용(독립 라우팅 없음)
- 완전한 노드보다 유연성이 떨어짐



## 일반적인 문제 해결



### API 액세스 문제



**인증 실패" 오류:**


1. 파일 `~/.phoenix/phoenix.conf`에서 비밀번호를 확인하세요


2. 인증 형식 `-u:password` 확인


3. Phoenixd가 실행 중인지 확인합니다(`./phoenix-CLI getinfo`)



**연결 시간 초과:**




- Phoenixd가 올바른 포트(9740)에서 수신 대기 중인지 확인합니다
- HTTPS 구성 전 로컬 액세스 테스트
- 로그를 확인합니다: `journalctl -u phoenixd -f`



### 유동성 문제



**결제 금액이 도착하지 않음 :**


1. 양이 최소 임계값(~30k Sats)을 초과하는지 확인합니다


2. 로그를 참조하여 채널 오류 식별


3. 필요한 경우 Phoenixd를 다시 시작합니다



**'비용 크레딧'의 잔액:**


소액 결제는 충당금으로 저장됩니다. 채널 개설을 트리거하고 이 자금을 해제하기 위해 더 큰 금액을 받습니다.



## 결론



Phoenixd는 개발자를 위한 사용 편의성과 기술 주권 사이의 훌륭한 절충안을 제시합니다. 자동 유동성 관리 기능을 갖춘 간단하면서도 강력한 Lightning API를 제공하여 기존 Lightning 노드의 복잡성을 제거합니다.



이 솔루션은 특히 다음을 수행하고자 하는 개발자와 회사에 적합합니다:




- Bitcoin Lightning을 애플리케이션에 통합하세요
- 복잡한 Lightning 채널 관리의 복잡성 피하기
- 자체 호스팅 인프라의 이점
- 간단하고 안정적인 API



Phoenixd를 사용하면 최신 REST API와 기술적 측면의 자동 관리 기능을 통해 나만의 비공개 Lightning 인프라를 구축할 수 있습니다. 프로젝트에서 Lightning 통합을 대중화하는 데 이상적인 솔루션입니다.



## 유용한 리소스



### 공식 문서




- 깃허브 Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - 소스 코드 및 릴리즈
- 피닉스 서버** 사이트: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - 문서 전문
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - 자주 묻는 질문



### 커뮤니티 지원




- 깃허브 이슈** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - 기술 지원
- 트위터 ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - 뉴스 및 공지사항