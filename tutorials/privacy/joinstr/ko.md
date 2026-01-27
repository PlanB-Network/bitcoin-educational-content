---
name: Joinstr
description: 주권적인 Bitcoin 기밀성을 위해 노스트르 네트워크를 통한 탈중앙화 코인조인
---

![cover](assets/cover.webp)



Bitcoin 블록체인의 투명성 덕분에 거래 내역을 추적할 수 있습니다. 코인조인은 여러 개의 동시 거래를 혼합하여 이러한 연결 고리를 끊고 현금과 비슷한 수준의 기밀성을 복원합니다.



그러나 기존 솔루션은 중앙 코디네이터를 단일 장애 지점으로 사용합니다. 와사비와 사무라이는 규제의 압박으로 2024년에 운영을 중단했습니다.



*조정을 위해 탈중앙화된 노스트르 네트워크를 사용하여 이러한 약점을 제거한 것이 바로 *Joinstr**입니다. 이 오픈 소스 애플리케이션은 중앙 기관이 서비스를 검열, 모니터링 또는 중단할 수 없는 진정한 주권 코인 조인을 가능하게 합니다.



## Joinstr이란 무엇인가요?



Joinstr은 노스트르 프로토콜을 조정 인프라로 활용하여 코인조인스 접근 방식을 혁신하는 오픈 소스 도구입니다. 전용 서버가 필요한 중앙 집중식 솔루션과 달리 Joinstr은 분산된 노스트르 릴레이 네트워크에 의존하여 참가자가 피어 간에 직접 조정할 수 있도록 합니다.



**분산형 아키텍처** : 노스트르 네트워크는 중앙 코디네이터를 대체합니다. 참여자는 Nostr 릴레이를 통해 암호화된 공지를 게시하여 "풀"을 생성하거나 참여합니다. 이러한 정보(금액, 참여자, 주소)는 릴레이가 알 수 없으므로 중앙 기관이 코인조인을 모니터링, 검열 또는 필터링할 수 없습니다.



**SIGHASH_ALL|ANYONECANPAY 메커니즘**: Joinstr은 이 Bitcoin 서명 플래그를 활용하여 각 참가자가 모든 출력을 검증하는 동안 자신의 입력에만 서명할 수 있도록 합니다. 각 사용자는 자신의 PSBT를 로컬에서 생성한 다음 Nostr을 통해 배포합니다. 각 사용자는 로컬에서 PSBT를 생성하고 서명한 다음 Nostr을 통해 배포합니다. 비트코인은 최종 서명할 때까지 독점적으로 관리됩니다.



**철학**: Joinstr은 Bitcoin 사이퍼펑크 정신을 따르며 세 가지 목표를 지향합니다: **검열에 대한 저항**(어떤 기관도 서비스를 중단할 수 없음), **완전한 비수탁성**(개인 키를 보관함), **평등 대우**(UTXO를 차별할 수 없음).



### 주요 기능



**유연한 풀**: 고정된 액면가와 달리 모든 사용자가 원하는 정확한 금액과 목표 참가자 수로 풀을 생성할 수 있어 인위적인 분할 없이 UTXO 사용을 최적화할 수 있습니다.



**투명한 수수료**: 조정 수수료가 없습니다. Bitcoin 거래 수수료만 참가자 간에 균등하게 분배됩니다(1인당 몇 천 사토시).



**임시성**: 사용자 데이터가 보관되지 않습니다. 정보는 암호화된 임시 노스트르 메시지를 통해 전송되며, 거래 후 즉시 잊혀집니다.



### 사용 가능한 플랫폼



이 튜토리얼은 현재 유일하게 안정적이고 권장되는 솔루션인 **안드로이드 애플리케이션**에 중점을 두고 있습니다. Electrum 플러그인이 존재하지만 호환성 문제가 있어 불안정합니다. 웹 인터페이스는 개발 중입니다.



## Bitcoin 코어 구성



Joinstr Android를 사용하려면 RPC를 통해 Bitcoin 노드에 연결해야 합니다. 먼저 휴대폰의 연결을 허용하도록 컴퓨터에서 Bitcoin 코어를 구성해야 합니다.



**참고**: Bitcoin Core의 전체 구성에 대한 자세한 내용은 전용 튜토리얼을 참조하세요:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### 네트워크 요구 사항



#### 현지 IP 주소 찾기



Android 휴대폰이 로컬 네트워크의 Bitcoin 노드에 연결할 수 있어야 합니다. 컴퓨터의 IP 주소를 찾습니다:



*macOS**에서** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



간단한 대안:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



*linux**에서** :



```bash
hostname -I | awk '{print $1}'
```



*windows**에서** :



```cmd
ipconfig
```



IPv4 주소 찾기(`192.168.x.x` 또는 `10.0.x.x` 형식)



### RPC 구성



#### bitcoin.conf 편집



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



bitcoin.conf` 파일을 찾습니다:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/라이브러리/애플리케이션 지원/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



즐겨 사용하는 텍스트 편집기로 파일을 열고 이 구성을 추가하여 RPC 서버를 활성화합니다.



**시작을 위한 권장 구성(북마크)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet** 구성(프로덕션용) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**중요** :




- 시그넷은 아직 개발 중(베타 버전)이며 버그가 존재할 수 있으므로 첫 번째 테스트에는 시그넷을 적극 권장**합니다. Signet을 사용하면 실제 자금의 위험 없이 무료로 테스트할 수 있습니다
- 192.168.1.0/24`를 네트워크 서브넷으로 바꿉니다(예: IP가 `192.168.68.57`인 경우 `192.168.68.0/24` 사용)



**보안**: 강력한 비밀번호 생성 :



```bash
openssl rand -base64 32
```



### 초기화



#### 다시 시작하고 확인



1. Bitcoin 코어를 완전히 종료합니다


2. 구성을 적용하려면 다시 시작하세요




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Bitcoin 코어가 처음 시작되면 북마크 블록체인을 다운로드하고 동기화합니다. 이 작업은 mainnet보다 훨씬 빠릅니다(몇 분 밖에 걸리지 않음). 동기화가 완료될 때까지 기다렸다가 계속 진행하시기 바랍니다.



![CRÉATION DE WALLET](assets/fr/04.webp)



동기화가 완료되면 "새 wallet 만들기"를 클릭하여 새 포트폴리오를 만듭니다. 'tuto_joinstr_signet'과 같은 명시적인 이름을 지정합니다.



![WALLET CRÉÉ](assets/fr/05.webp)



이제 wallet가 생성되었으며 테스트를 위해 북마크된 비트코인을 받을 준비가 되었습니다.



#### 북마크된 비트코인 받기(테스트)



북마크에서 Joinstr을 테스트하려면 무료 테스트 비트코인이 필요합니다 :



![SIGNET FAUCET](assets/fr/06.webp)



와 같은 공개 북마크를 사용합니다:




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Bitcoin 코어에서 새 수신 주소('수신' 탭)를 찾아 복사한 후 수도꼭지 양식에 붙여넣습니다. 필요한 경우 보안 문자를 입력합니다. 몇 초 내에 북마크된 비트코인을 무료로 받으실 수 있습니다.



## Android 애플리케이션



### 설치



![APPLICATION ANDROID](assets/fr/07.webp)



Gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)로 이동하여 최신 APK 버전을 다운로드하세요. Android 브라우저에서 파일을 다운로드한 다음 파일을 열어 설치를 시작합니다. 필요한 경우 휴대폰의 보안 설정에서 알 수 없는 출처의 설치를 허용해야 합니다.



### 애플리케이션 구성



![PERMISSIONS VPN](assets/fr/08.webp)



처음 시작할 때 Joinstr 애플리케이션은 기본 제공 VPN을 제어할 수 있는 권한을 요청합니다. 두 권한 요청을 모두 수락하세요: OpenVPN 제어 및 VPN 연결. 이러한 권한은 네트워크 개인 정보를 보호하는 VPN 통합에 필요합니다.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr 애플리케이션은 세 가지 주요 탭으로 구성되어 있습니다:




- 홈**: 홈 화면
- 풀**: CoinJoin 풀 생성 및 관리
- 설정**: 애플리케이션 구성



![CONFIGURATION SETTINGS](assets/fr/13.webp)



'설정' 탭에서 설정을 구성합니다:



**1. 노스트르 릴레이**: 풀 조정을 위한 Nostr 릴레이 주소




- 예: `wss://relay.damus.io`
- 기타 추천 릴레이: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **중요**: 모든 참가자는 **동일한 노스트르 릴레이**를 사용하여 동일한 풀을 보고 참여해야 합니다. 다른 릴레이를 사용하면 다른 릴레이에서 생성된 풀을 볼 수 없습니다



**2. 노드 URL**: Bitcoin 노드의 IP 주소(포트 제외)




- 형식: 형식: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC 사용자 이름** : bitcoin.conf의 `rpcuser=`에 설정된 사용자 이름입니다




- 예: `satoshi



**4. RPC 비밀번호** : bitcoin.conf의 `rpcpassword=`에 설정된 비밀번호입니다



**5. RPC 포트** : 네트워크에 따라 RPC 포트




- Mainnet** : `8332`
- 북마크**: `38332`



**6. Wallet**: 혼합할 UTXO가 포함된 Bitcoin 코어 포트폴리오를 선택합니다




- 예: `tuto_joinstr_signet`



**7. VPN 게이트웨이**: Riseup VPN 서버 선택




- 예: '(파리) vpn07-par.riseup.net`
- 기타 이용 가능: 암스테르담, 시애틀 등
- ⚠️ **중요**: 동일한 풀의 모든 참가자는 **동일한 VPN 게이트웨이**를 사용하여 CoinJoin에 참여해야 합니다. 믹싱 라운드 동안 모든 참가자는 네트워크 분석이 참가자를 연관 짓는 것을 방지하기 위해 동일한 출구 IP 주소로 표시되어야 합니다



Joinstr 애플리케이션은 기본적으로 Riseup VPN을 **통합**하여 참가자 간의 조정을 간소화합니다.



**중요** :




- 휴대폰과 컴퓨터가 동일한 로컬 WiFi 네트워크에 있는지 확인하세요
- 풀에 참여할 때 VPN 연결이 자동으로 활성화됩니다
- 모든 매개변수를 설정한 후 **"저장"**을 클릭합니다



## 실용적인 사용



### 풀 생성 또는 가입



![CRÉATION POOL ANDROID](assets/fr/10.webp)



CoinJoin에 참여하려면 두 가지 옵션이 있습니다:



**옵션 1: 새 풀 만들기**



"풀" 탭에서 "새 풀 만들기"를 클릭합니다. BTC 단위(예: 0.002 BTC)와 원하는 참가자 수(최소 2명, 익명성을 높이려면 3~5명 권장)를 지정합니다. 그런 다음 애플리케이션은 다른 사용자가 풀에 참여할 때까지 기다립니다. 필요한 수에 도달하면 출력 등록 프로세스가 자동으로 시작되며, 혼합할 UTXO를 선택하고 "등록"을 클릭해야 합니다.



**⏱️ 중요**: 풀은 **10분** 동안 활동이 없으면 만료됩니다. 필요한 참가자 수에 도달하지 못하면 풀은 자동으로 종료됩니다.



**옵션 2: 기존 풀에 가입**



'다른 풀 보기' 탭에서 다른 사용자가 만든 사용 가능한 풀을 찾아봅니다. 원하는 금액에 해당하는 풀을 선택하고 참여하세요. 다른 참가자와 동일한 Nostr 릴레이 및 VPN 게이트웨이를 구성했는지 확인하세요(구성 섹션 참조).



**UTXO 선택 규칙**: UTXO이 풀 액면가보다 약간 높아야 합니다(+500~+5000 sats 잉여분 사이).



**예시**: 0.002 BTC(200,000 sats) 풀의 경우 200,500에서 205,000 sats 사이의 UTXO을 사용합니다.



![PROCESSUS COINJOIN](assets/fr/11.webp)



입력이 등록되면 애플리케이션은 모든 참가자가 자신의 입력을 등록할 때까지 기다립니다. 모든 입력이 등록되면 PSBT이 생성되고 키로 자동 서명된 다음 다른 참가자의 서명과 결합됩니다. 마지막으로 전체 트랜잭션이 Bitcoin 네트워크에 브로드캐스트됩니다. 브로드캐스트가 완료되면 TXID(트랜잭션 식별자)를 받게 됩니다. Android에서는 PSBT을 수동으로 조작할 필요가 없습니다.



### on-chain 인증



![TRANSACTION MEMPOOL](assets/fr/12.webp)



트랜잭션이 브로드캐스트되면 TXID(트랜잭션 식별자)를 받게 됩니다. Mempool.space](https://mempool.space) 또는 자주 사용하는 브라우저에서 확인합니다. 북마크에서 테스트하려면 [mempool.space/signet](https://mempool.space/signet)을 사용하세요.



관찰할 수 있습니다:





- 엔 항목**: 참가자당 1개(이 예에서는 2개 항목)
- N개의 동일한 출력**: 정확한 액수(여기서는 각각 0.00199800 BTC의 출력 2개)
- 흐름도**: mempool.space는 입력과 출력의 조합을 시각적으로 표시합니다
- 특징** : 트랜잭션은 SegWit, Taproot, RBF 등으로 식별할 수 있습니다.



모든 주요 출력물의 양이 동일하기 때문에 어떤 것이 누구의 것인지 파악하는 것은 **불가능합니다**. 이것이 바로 CoinJoin의 기본 원칙인 출력의 구별 불가능성입니다.



**거래 서명 예시** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**참고**: UTXO가 풀 액면가보다 큰 경우, 외환 출력(잉여)이 발생합니다. 이러한 교환 UTXO는 추적이 가능하며 익명화된 출력과 별도로 관리해야 합니다. 절대로 혼합 출력과 결합하지 마세요.



## CoinJoin 품질 및 익명성 패키지



CoinJoin의 효율성은 트랜잭션에서 생성되는 동일한 값의 출력 수인 **아논셋**으로 측정됩니다. 이 수치가 높을수록 어떤 입력이 어떤 출력에 해당하는지 파악하기가 더 어려워집니다.



Joinstr은 현재 평균 **2~5명의 참가자** 풀을 생성합니다. 이 수치는 와사비(50~100명)나 Whirlpool(5~10명)와 같은 기존의 중앙화된 코디네이터보다 낮지만, 이는 탈중앙화를 위한 대가입니다.



익명성 집합과 그 계산에 대해 자세히 알아보려면** 전체 강좌인 [익명성 집합](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431)을 참조하세요.



### 조인스트라와 다른 코인조인




| 측면 | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **풀당 참가자** | 50-100 | 5-10 | 가변 (P2P) | **2-5** |
| **조정자** | 중앙화 (2024년 폐쇄) | 중앙화 (활성) | P2P maker/taker | **없음 (Nostr)** |
| **검열 저항성** | 약함 | 중간 | 매우 높음 | **매우 높음** |
| **조정 수수료** | 백분율 | 진입 수수료 | 메이커에게 지불 | **없음** |
| **UTXO 차별** | 예 (블랙리스트) | 아니오 | 아니오 | **아니오** |

💡 **기타 활성 CoinJoin 솔루션** :




- Ashigaru**: 중앙화된 코디네이터가 있지만 분산된 방식으로 배포할 수 있는 Whirlpool 프로토콜의 오픈소스 구현. 2024년 사무라이 Wallet가 압수된 후에도 계속 운영됩니다.
- JoinMarket**: '메이커'가 유동성을 제공하고 '테이커'로부터 보상을 받는 메이커/테이커 비즈니스 모델을 기반으로 하는 중앙 코디네이터가 없는 탈중앙화 P2P 솔루션입니다.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**근본적인 트레이드오프**: 조인스트라와 조인마켓은 중앙 코디네이터가 없는 유일한 두 솔루션입니다. JoinMarket은 재정적 인센티브가 있는 P2P 비즈니스 모델을 사용하는 반면, Joinstr은 비용 없는 조정을 위해 Nostr을 사용합니다. Joinstr은 단순성(메이커/테이커 관리 없음)과 조정 수수료가 전혀 없는 대신 즉각적인 대규모 익명성을 희생합니다.



**실용적인 권장 사항**: 소규모 풀을 보완하려면 다른 참가자와 함께 CoinJoin 라운드를 여러 번 연속으로 진행하세요. 라운드 간격을 두고 각 라운드 사이에 Nostr 릴레이를 변경하여 기밀성을 극대화하세요.



이 주제에 대한 자세한 내용은 비트코인 개인정보 보호에 대한 전체 강좌를 참조하세요:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 장점과 한계



### 하이라이트



**향상된 개인 정보 보호**: Nostr 통신 암호화, 참여자 간 공유 VPN, 토르 권장 사용의 조합은 우회하기 어려운 다층 보호 기능을 제공합니다.



**투명하고 최소한의 비용**: 조정 비용 없이 mining 비용만 참여자 간에 공평하게 분담합니다. 운영자가 부과하는 비율은 없습니다.



### 고려해야 할 제약 조건





- 가변 유동성**: 소규모 풀, 참가자가 모일 때까지 기다릴 수 있음
- 프로젝트 진행 중**: 베타 버전 적용 중, 버그 발생 가능. 북마크에서 소량으로 먼저 테스트
- 시빌 공격**: 한 명의 상대가 여러 명의 풀 참가자를 제어할 가능성



## 모범 사례



**UTXO 격리**: 혼합된 UTXO을 혼합되지 않은 UTXO과 결합하지 마세요. 익명화된 결과물에는 별도의 포트폴리오를 사용하세요.



**여러 라운드 필수**: 다른 참가자와 함께 최소 3번의 라운드를 연속으로 진행합니다. 패턴을 피하기 위해 횟수와 시간을 다양하게 조절하세요. 몇 시간 간격으로 라운드를 진행합니다.



**네트워크 보호**: 내장 VPN과 더불어 Tor를 체계적으로 사용하세요. 중요한 세션마다 임시 노스트르 키를 생성하세요.



**조심스럽게 진행 중**: 소량으로 북마크를 시작하세요.



## 결론



노스트르는 진정한 의미의 탈중앙화된 Bitcoin 개인정보 보호 솔루션입니다. 노스트르를 조정에 사용함으로써 중앙 조정자에 대한 의존성을 없애고 사용자 주권을 보존합니다.



**검열에 대한 저항을 중요하게 여기고 작은 풀을 보완하기 위해 CoinJoin를 여러 번 수행할 준비가 되어 있는 사용자를 위한 것입니다.



금융 감시가 강화되는 상황에서 개인 정보 보호를 위한 탈중앙화 도구가 필수적인 요소가 되고 있습니다.



## 리소스



### 공식 문서




- [Joinstr 공식 웹사이트](https://joinstr.xyz)
- [사용자 설명서](https://docs.joinstr.xyz/users/using-joinstr)
- [기술 문서](https://docs.joinstr.xyz/overview/how-does-it-work)
- [깃랩 소스 코드](https://gitlab.com/invincible-privacy/joinstr)
- [안드로이드 애플리케이션](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### 튜토리얼




- [Electrum 플러그인 튜토리얼](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - 무수정 테크의 전체 가이드



### 커뮤니티 및 지원




- [텔레그램 조인스트 그룹](https://t.me/joinstr) - 커뮤니티 지원 및 북마크 코너
- [델빙비트코인에 대한 기술 토론](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### 추가 도구




- [북마크 Faucet](https://signetfaucet.com) - 무료 테스트 비트코인
- [알트 시그넷 Faucet](https://alt.signetfaucet.com) - Faucet 대체품
- [Mempool.space](https://mempool.space) - 개인정보 분석 기능이 있는 Block explorer