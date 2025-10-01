---
name: Ride The Lightning (RTL)
description: 라이트닝 노드를 관리하려면 RTL(Ride The Lightning)을 사용하세요
---
![cover](assets/cover.webp)


## 1. 소개



**RTL(라이드 더 라이트닝)**은 Interface 노드를 관리하기 위한 완전한 Lightning Network 웹 애플리케이션입니다. 이 자체 호스팅 웹 애플리케이션은 브라우저에서 액세스할 수 있는 라이트닝 **"콕핏"**을 제공합니다. RTL은 모든 주요 라이트닝 구현(LND, 코어 라이트닝/CLN 및 Eclair)에서 작동하며 노드와 채널을 완벽하게 제어할 수 있습니다. 오픈 소스(MIT 라이선스)로 무료로 제공되는 RTL은 여러 턴키 노드 솔루션(RaspiBlitz, MyNode, Umbrel 등)에 기본으로 통합되어 있습니다.



**그래픽 Interface가 없으면 사용자 친화적인 CLI 명령을 통해서만 라이트닝 노드를 관리할 수 있습니다. RTL은 인체공학적 Interface를 통해 이러한 작업을 간소화합니다. 주요 애플리케이션은 다음과 같습니다





- 채널 및 노드 보기 - 대시보드에는 On-Chain 잔액, Lightning 유동성(로컬/원격), 동기화 상태, 노드 별칭 등이 표시됩니다. 채널 목록, 용량, 로컬/원격 배포 및 상태를 볼 수 있습니다. RTL은 상황에 맞는 대시보드를 제공하여 다양한 각도에서 활동을 분석할 수 있습니다.





- 라이트닝 채널 관리** - 클릭 몇 번으로 채널을 열거나 닫을 수 있습니다. RTL을 사용하면 명령 없이도 피어에 연결하여 채널을 열 수 있습니다. 라우팅 수수료를 조정하고, 잔액 점수를 확인하거나, 순환 재조정을 시작하여 채널 간 자금 균형을 재조정할 수 있습니다.





- 추적 및 결제** - RTL은 인보이스를 통해 결제를 전송하고, generate 인보이스를 수신하고, 자세한 내역으로 거래(결제, 라우팅)를 추적하는 등 라이트닝 트랜잭션을 관리합니다. 또한 Interface는 라우팅을 분석하여 어떤 결제가 노드를 통과하는지 확인합니다.





- Wallet On-Chain 관리 및 백업** - On-Chain 탭에서 generate 주소와 트랜잭션을 전송할 수 있습니다. RTL을 사용하면 각 채널 수정에 대한 자동 업데이트와 함께 LND용 SCB 파일을 내보내 채널을 쉽게 저장할 수 있습니다.



간단히 말해, RTL은 Lightning Network를 위한 **강력한 대시보드**로, 매일 노드를 시범 운영할 수 있는 교육용 Interface을 제공합니다. 이 튜토리얼에서는 채널과 결제를 관리하기 위한 설치 및 사용 방법을 안내합니다.



## 2. RTL의 기술적 운영



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



본론으로 들어가기 전에 기술적인 수준에서 RTL이 라이트닝 노드와 상호작용하는 방식**을 간단히 이해하는 것이 유용합니다.



**일반 아키텍처:** RTL은 Node.js(백엔드)와 Angular(프론트엔드)로 구축된 웹 애플리케이션입니다. 구체적으로 설명하자면, RTL은 API를 통해 Lightning 구현과 대화하는 소규모 로컬 웹 서버(기본적으로 포트 3000에서)로 실행됩니다. 유형에 따라 :





- LND**를 사용하면 RTL은 LND의 REST API(포트 8080)를 사용하여 라이트닝 명령을 실행합니다. 연결은 TLS로 보호되며 인증을 위해 LND의 **admin macaroon** 파일이 필요합니다.





- 코어 라이트닝(CLN)**을 사용하면 RTL은 *c-lightning-REST*에서 제공하는 REST API를 사용하거나 `commando` 플러그인을 통해 **액세스 룬**을 사용합니다. 엄브렐과 같은 솔루션은 이러한 Elements를 자동으로 구성합니다.





- 에클레어**를 사용하면 RTL은 구성된 인증 비밀번호를 사용하여 에클레어 REST API에 연결합니다.



**구성 및 보안:** RTL은 웹 포트, 액세스 비밀번호, 노드 연결 정보를 정의하는 JSON 파일(`RTL-Config.json`)을 통해 구성됩니다. Interface 웹은 로그인/비밀번호(기본 `비밀번호` 변경 가능)로 보호되며 2FA를 지원합니다. 기본적으로 RTL은 로컬 HTTP(`http://localhost:3000`)로 실행되지만 원격 액세스의 경우 항상 보안 연결(리버스 프록시, Tor 또는 VPN을 통한 HTTPS)을 사용하세요.



간단히 말해, RTL은 보안 API를 통해 노드에 연결하고, 적절한 액세스 토큰이 필요하며, 자체 보안 Layer을 제공하는 추가 구성 요소입니다. 이 모듈식 아키텍처를 사용하면 하나의 RTL 인스턴스로 **여러 개의 라이트닝 노드를 관리할 수도 있습니다**.



## 3. RTL 설치



RTL은 오픈 소스 소프트웨어로 배포되므로 시스템에 설치하는 방법에는 여러 가지가 있습니다. 이 섹션에서는 수동 설치와 엄브렐을 통한 설치라는 두 가지 주요 접근 방식을 다룹니다.



### 수동 방법



수동 설치는 세밀한 제어를 원하거나 RTL을 사용자 지정 구성에 통합하려는 경우에 적합합니다. 아래 단계는 Linux를 실행하는 LND 노드(예: 라즈베리파이 또는 우분투/데비안을 실행하는 VPS)를 위한 것이지만 CLN/Eclair에서도 유사합니다.



**전제 조건: **동기화된** Bitcoin 노드와 작동 중인 라이트닝 노드(LND, CLN 또는 Eclair)가 머신에 있는지 확인하세요. RTL은 자체적으로 라이트닝 노드를 포함하지 않으며, 기존 노드에 연결합니다. 또한 **Node.js**가 설치되어 있어야 합니다(버전 14 이상 권장). Node -v`로 확인하거나 공식 사이트(https://nodejs.org/en/download/) 또는 패키지 관리자에서 Node를 설치할 수 있습니다.



주요 설치 단계는 다음과 같습니다:



**RTL 코드 다운로드**: 원하는 디렉토리에 공식 RTL GitHub 리포지토리를 복제합니다. 예를 들어



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**종속성 설치**: RTL은 Node.js 애플리케이션이므로 필요한 모듈을 설치해야 합니다. RTL 폴더에서 를 실행합니다:



```bash
npm install --omit=dev --legacy-peer-deps
```



이 명령은 필요한 NPM 패키지를 설치합니다(개발 종속성 무시). 노드 종속성 충돌 가능성을 피하려면 `--legacy-peer-deps` 옵션을 사용하는 것이 좋습니다.



**RTL-Config**: 종속성이 설정되면 구성 파일을 준비합니다. 프로젝트 루트에 있는 `Sample-RTL-Config.json` 파일을 `RTL-Config.json`으로 복사/이름을 바꿉니다. 에서 파일을 엽니다:





- UI 비밀번호**: 보안 비밀번호를 선택하고 (기본 '비밀번호' 대신) `멀티패스`에 입력합니다.
- 포트**: 기본값은 `3000`입니다. 이 포트가 이미 컴퓨터에서 사용 중인 경우 변경할 수 있습니다.
- 노드**: `nodes[0]` 섹션에서 노드에 대한 매개변수를 조정합니다:
     - `lnNode`: 노드에 대한 설명적인 이름(예: `"LND 노드 메종"`).
     - lnImplementation`: `"LND"`(또는 `"CLN"`/`"ECL"` 적절히 사용).
     - '인증'에서:
       - macaroonPath`: LND의 마카롱 관리자가 포함된 폴더의 전체 경로를 지정합니다.
       - configPath`: 노드의 설정 파일 경로(LND의 경우 `LND.conf`).
     - '설정'에서:
       - '법정통화 변환': 법정통화 변환을 원하면 'true'로 설정합니다.
       - 공지되지 않은 채널을 보려면 `unannouncedChannels`: `true`로 설정합니다.
       - 테마 색상` 및 `테마 모드`: Interface 사용자 정의.
       - channelBackupPath`: LND 채널 백업을 위한 경로입니다.
       - lnServerUrl`: 라이트닝 노드의 URL(예: `https://127.0.0.1:8080`).



**RTL 서버를 시작합니다**: RTL 폴더에서 를 실행합니다:



```bash
node rtl
```



애플리케이션이 시작되고 `http://localhost:3000`에서 액세스할 수 있습니다.



**(선택 사항) RTL을 서비스로 실행**합니다: 자동 시작을 위해 systemd 를 생성합니다:



이렇게 하려면




- 컴퓨터에서 터미널을 엽니다.
- 다음 명령을 사용하여 새 서비스 파일을 만듭니다(`nano`를 선호하는 편집기로 대체):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- 아래 내용을 복사하여 이 파일에 붙여넣습니다:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- 경로/to/RTL/rtl`을 내 컴퓨터의 `rtl` 파일의 실제 경로로 바꾸고 `<your_user>`를 Linux 사용자 이름으로 바꿉니다.
- 파일을 저장하고 닫습니다.
- 시스템 구성을 다시 로드합니다:


```bash
sudo systemctl daemon-reload
```




- RTL 서비스를 활성화하고 시작합니다:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



이제 머신을 재부팅할 때마다 RTL이 자동으로 시작됩니다. 로 상태를 확인할 수 있습니다:


```bash
sudo systemctl status RTL
```



### 엄브렐을 통한 설치



엄브렐](https://getumbrel.com)을 사용하면 RTL 설치가 훨씬 간단해집니다:





- Interface 엄브렐에 액세스(일반적으로 `http://umbrel.local`를 통해)
- 앱 스토어**로 이동
- "라이드 더 라이트닝" 검색



**중요 참고: 엄브렐 앱 스토어에는 두 개의 별도 RTL 애플리케이션이 있습니다




- 라이트닝을 타다**(LND용): 엄브렐의 기본 라이트닝 노드(LND)와 함께 사용하세요.
- 라이트닝을 타다(코어 라이트닝)**: 엄브렐에 *코어 라이트닝* 애플리케이션을 설치했고 이 노드를 RTL로 관리하려는 경우에만 사용하세요.



*각 RTL 버전은 해당 구현(LND 또는 코어 라이트닝)과 대화하도록 사전 구성되어 있습니다. 라이트닝 노드를 변경하지 않은 경우 기존 LND 버전*을 선택하면 됩니다



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- 설치**를 클릭합니다



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**중요:** 설치 후 RTL에 기본 비밀번호가 표시된 화면이 나타납니다. **이 비밀번호를 복사하여 저장하세요** - Interface RTL에 로그온하려면 이 비밀번호가 필요합니다. 이 비밀번호는 "다시 표시하지 않음" 옵션을 선택하지 않는 한 RTL이 시작될 때마다 표시됩니다.



엄브렐은 자동으로 :




- RTL 다운로드 및 구성
- Lightning 노드에 대한 액세스 구성
- 업데이트 관리
- Interface에 대한 액세스 보안



설치가 완료되면 엄브렐의 *앱* 메뉴에 애플리케이션이 표시됩니다. 라이드 더 라이트닝**을 클릭하여 실행합니다.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



로그인 화면에서 앞서 복사한 비밀번호를 입력합니다. 로그인하면 추가 구성 없이도 엄브렐 대시보드에서 바로 Interface 웹 RTL에 액세스할 수 있습니다!



## 4. Interface RTL 소개 및 사용 방법



이제 RTL이 실행되었으니 Interface 웹과 주요 기능을 살펴보겠습니다. 애플리케이션의 여러 섹션을 통해 전체 개요를 살펴보겠습니다.



### 기본 제어판



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



로그인하자마자 **메인 대시보드**에 액세스하여 라이트닝 노드에 대한 개요를 확인할 수 있습니다. 이 페이지에는 필수 정보가 집중되어 있습니다:




- 총 라이트닝 잔액
- On-Chain 밸런스 사용 가능
- 유동성 분석(수신/발신) 내역
- 라이트닝 노드를 통한 빠른 Sats 송수신 액세스



### 펀드 관리 On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



On-Chain** 탭을 통해 메인 체인에서 직접 비트코인을 관리할 수 있습니다:




- 다른 단위로 잔액 표시(Sats, BTC, USD)
- 전체 거래 목록
- Address 세대 Taproot(P2TR), P2SH(NP2WKH) 또는 Bech32(P2WKH)
- UTXO 관리, 비트코인 수신 및 전송



### 라이트닝: 하위 메뉴에 대한 자세한 설명



Interface RTL에는 Lightning Network 전용 사이드 메뉴가 있어 노드 관리에 필요한 모든 필수 기능을 한데 모았습니다. 다음은 스크린샷 순서대로 각 하위 메뉴의 세부 사항입니다:



#### 1. 피어/채널



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



이 하위 메뉴에서는 다음을 수행할 수 있습니다:




- 연결된 피어와 열려 있거나 대기 중인 라이트닝 채널의 목록을 확인합니다.
- 새 피어를 추가합니다(다른 라이트닝 노드에 연결).
- 기존 채널을 열거나 닫거나 관리하세요.
- 용량, 로컬/원격 잔액, 상태, 거래 내역, 잔고 점수 등 각 채널의 세부 정보를 확인하세요.



#### 2. 거래



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



이 하위 메뉴에서는 :




- 라이트닝 결제 보내기(Invoice을 통해).
- generate로 이동하고 송장을 관리하여 결제를 받습니다.
- 송금 및 수취한 결제의 전체 내역과 세부 정보(금액, 날짜, 상태, 요금, 건너뛴 횟수 등)를 확인할 수 있습니다.



#### 3. 라우팅



이 하위 메뉴에는 :




- 다른 Lightning Network 사용자를 위해 노드에서 라우팅한 결제.
- 라우팅 통계: 중계된 트랜잭션 수, 수수료 수입, 발생한 오류.
- 고급 분석을 위해 내보낼 수 있는 기록.



#### 4. 연기



이 하위 메뉴는 :




- 라이트닝 노드의 활동에 대한 자세한 보고서입니다.
- 채널, 결제, 수수료, 용량 등에 대한 차트와 표를 확인할 수 있습니다.
- 노드의 성능을 더 잘 이해할 수 있는 도구.



#### 5. 그래프 조회



이 하위 메뉴에서는 다음을 수행할 수 있습니다:




- Lightning Network의 토폴로지를 살펴보세요.
- 특정 노드 또는 채널을 검색합니다.
- 연결 및 전체 네트워크 용량에 대한 정보를 얻습니다.



#### 6. 서명/인증



이 하위 메뉴는 :




- 노드 키로 메시지에 서명하는 기능(Ownership 증명).
- 다른 노드의 메시지를 인증하기 위한 서명 확인.



#### 7. 백업



이 하위 메뉴는 백업 전용 메뉴입니다:




- 채널 백업 파일 내보내기(LND의 경우 SCB).
- 필요한 경우 구성 또는 채널을 복원합니다.
- 백업 보안을 위한 팁.



#### 8. 노드/네트워크



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



이 하위 메뉴에서 찾을 수 있는 항목은 :




- 별칭, 버전, 색상, 동기화 상태 등 라이트닝 노드의 상태에 대한 전체 요약입니다.
- 채널(활성, 대기 중, 닫힘), 총 용량, 연결에 대한 통계입니다.
- 글로벌 Lightning Network와 그 안에서 내 노드의 위치에 대한 정보입니다.



### 서비스: 볼트 스왑



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



볼츠는 개인정보 보호 친화적인 비수탁형 Exchange 서비스로, Lightning Network과 Blockchain Bitcoin(On-Chain) 사이의 비트코인을 변환하는 서비스입니다. 두 가지 유형의 작업을 제공합니다: 리버스 서브마린 스왑(**스왑 아웃**)과 서브마린 스왑(**스왑 인**)입니다.



#### 스왑 아웃(역 잠수함 스왑)



스왑 아웃은 Lightning Network에서 사용 가능한 Satss를 On-Chain 비트코인으로 변환합니다. 이 메커니즘은 노드의 수신 용량이 부족하거나 On-Chain Address에서 자금을 회수하고자 할 때 유용합니다. 프로세스는 다음과 같이 작동합니다:




- 사용자가 교환할 금액을 선택합니다
- 노드가 볼츠에 라이트닝 결제를 전송합니다
- Exchange에서 볼츠는 On-Chain 비트코인의 동등한 금액을 차단합니다
- 거래가 확인되면 사용자는 스왑에 사용된 비밀을 공개하여 자금을 청구할 수 있습니다



이 프로세스는 비수탁 방식으로 진행되며, 볼츠는 사용자의 자금을 보관하지 않습니다.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### 스왑 인(잠수함 스왑)



반면에 스왑 인을 사용하면 On-Chain 자금을 Lightning Network에 다시 주입할 수 있습니다. 이 기능은 채널의 출력 용량을 복원하는 데 특히 유용합니다. 절차는 다음과 같습니다:




- 사용자는 볼츠가 생성한 특정 Address로 비트코인을 전송합니다
- 이 자금은 사용자 노드에서 생성한 라이트닝 Invoice을 지불한 경우에만 볼츠가 해제할 수 있습니다
- Invoice을 지불하면 라이트닝 채널에서 자금을 사용할 수 있어 노드의 출력 용량이 증가합니다



![Configuration d'un swap-in](assets/fr/12.webp)



이 두 가지 메커니즘을 통해 라이트닝 채널의 유동성을 효율적으로 관리하면서 사용자의 자금에 대한 주권을 유지할 수 있습니다.



### 구성 및 사용자 지정



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



노드 구성** 탭에서는 사용자 환경을 맞춤 설정할 수 있습니다:




- 공지되지 않은 채널 활성화
- 세일 디스플레이 사용자 지정
- Block explorer 구성
- Interface 조정



### 문서 및 도움말



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



마지막으로 **도움말** 섹션에서는 에 대한 종합적인 문서를 제공합니다:




- 초기 구성
- 피어 및 채널 관리
- 결제 및 거래
- 백업 및 복원
- 보고서 및 통계
- 서명 및 인증
- 노드 및 애플리케이션 매개변수



직관적이고 체계적으로 구성된 이 포괄적인 Interface을 사용하면 기본 작업부터 고급 기능에 이르기까지 Lightning 노드를 효율적으로 관리할 수 있습니다.



## 5. 고급 사용 사례 및 보안



이 섹션에서는 RTL을 더욱 발전시키고 라이트닝 노드를 보호하기 위해 알아야 할 사항을 설명합니다:



### 모니터링 및 문제 해결



노드를 모니터링하려면 RTL 데이터(로그, CSV)를 내보내고 Grafana와 같은 도구에서 확인할 수 있습니다. 문제(결제 차단, 비활성 채널)가 발생하면 LND/CLN 로그를 참조하고 진단 명령어(`lncli listchannels`, `lncli pendingchannels` 등)를 사용하세요. RTL은 라우팅 이벤트 모니터링을 위한 Interface 로그도 제공합니다.



### 안전한 원격 액세스



인터넷에 RTL을 직접 노출하지 마세요. 를 선호합니다:




- 비공개, 암호화된 액세스를 위한 VPN**(예: Tailscale)
- 안전한 익명 액세스를 위한 Tor**
- 구성 방법을 알고 있는 경우에만 역방향 프록시 **HTTPS**(Nginx/Caddy)를 사용하세요



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 모범 안전 사례





- 액세스 보호**: admin.macaroon 또는 RTL 비밀번호를 공유하지 마세요. 민감한 파일에 대한 권한을 제한하세요.
- 정기 백업**: 수정할 때마다 채널 백업 파일(SCB)을 내보내고 노드 외부에 저장합니다.
- 업데이트**: 최신 보안 수정 사항으로 RTL, 노드 및 Umbrel을 최신 상태로 유지하세요.
- 기밀 유지**: 로그와 스크린샷을 공유하기 전에 익명화합니다. 잔액이나 동료 목록을 공개적으로 공유하지 마세요.
- 단일 액세스**: RTL은 다중 사용자가 아닙니다. 관리자 액세스 권한을 공유하지 마세요. 읽기 전용 액세스의 경우 필요한 경우 전용 마카롱을 사용하세요.



이러한 원칙을 적용하면 위험을 크게 제한하고 라이트닝 노드에 대한 통제권을 유지할 수 있습니다.



## 7. 결론



**라이딩 더 라이트닝**은 초보자든 고급 사용자든 Bitcoin/라이트닝 노드를 효과적으로 관리하기 위한 필수 도구입니다. 채널, 결제 및 노드 상태를 제어하기 위한 명확한 Interface를 제공하는 동시에 Lightning Network에 대한 이해를 심화시켜 줍니다.



RTL은 다중 구현 호환성, 고급 기능(리밸런싱, 스왑, 보고서), 교육적 접근 방식이 돋보입니다. 간단한 요구 사항의 경우 Interface 엄브렐 또는 Wallet 모바일로도 충분하지만, 능동적이고 최적화된 노드 관리에는 RTL이 적합합니다.



자세히 알아보려면 :




- 공식 RTL 웹사이트: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- 레딧 r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - 기술 토론, 프로젝트 발표, 피드백 및 교육 리소스 제공
- 엄브렐 커뮤니티 포럼**: [community.getumbrel.com](https://community.getumbrel.com) - Bitcoin/라이트닝 전용 섹션, 일반적인 문제에 대한 가이드 및 해결책을 제공하는 공식 포럼입니다
- Lightning Network 개발자**: [github.com/lightning](https://github.com/lightning) - 개발 및 소스 코드 기여를 위한 공식 GitHub 리포지토리입니다
- 스택 Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - 개발자 및 고급 사용자와의 기술 Q&A



간단히 말해, RTL을 사용하면 모든 기능을 갖춘 최신 Interface에서 라이트닝 노드를 완벽하게 제어할 수 있습니다.



**출처: RTL 공식 웹사이트, RTL GitHub, 엄브렐 앱 스토어, 엄브렐 커뮤니티, 플랜 B 네트워크 리소스.



Lightning Network의 작동 원리를 더 깊이 이해하려면 이 무료 강좌를 수강하는 것도 좋습니다:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb