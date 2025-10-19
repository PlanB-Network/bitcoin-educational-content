---
name: 케이크 Wallet
description: 케이크 Wallet 및 자동 결제에 대한 튜토리얼
---

![cover](assets/cover.webp)


이 가이드에서는 오픈소스, 비수탁형, 개인정보 보호에 중점을 둔 다중 통화 Wallet인 [**Cake Wallet**](https://cakewallet.com/)에 대해 살펴봅니다(Android, iOS, macOS, Linux 및 Windows에서 사용 가능). Bitcoin에 특화된 개인정보 보호 기능에 대해 자세히 살펴보고, **사일런트 페이먼트**(개선된 On-Chain 개인정보 보호 프로토콜)를 통한 Bitcoin 송금/수신 방법을 안내하며, 비동기 거래를 위한 PayJoin v2의 구현에 대해 살펴볼 예정입니다.


## 🎉 주요 기능



- 재사용 가능한 스텔스 주소로 "PayNyms"라고도 불리는 이전 [BIP 47 결제 코드](https://silentpayments.xyz/docs/comparing-proposals/bip47/)를 개선한 [**자동 결제 (BIP-352)**](https://BIPs.dev/352/). 발신자가 자동 결제 Address을 사용하면 Wallet은 다른 키를 사용하여 고유한 일회성 Address을 파생하고, 이 Address은 고유한 일회성 Taproot Address으로 결합됩니다. Blockchain 기록에는 관련 없는 거래가 표시되므로 수신 결제의 연결이 방지됩니다. 자동 결제는 다음과 같은 다양한 이점을 제공합니다:
    - 재사용 가능한 주소: 각 트랜잭션마다 새로운 generate를 생성할 필요가 없으므로 사용자 경험이 향상되고 개인정보 보호가 강화됩니다
    - 비용 증가가 전혀 없습니다: 자동 결제는 거래 규모나 비용을 증가시키지 않습니다.
    - 익명성 강화: 외부 관찰자는 거래를 자동 결제 Address에 연결할 수 없습니다.
    - 발신자와 수신자의 상호 작용이 필요하지 않습니다: 당사자 간의 커뮤니케이션 없이도 거래가 가능합니다.
    - 각 결제에 대한 고유 주소: 실수로 Address를 재사용할 위험 제거.
    - 서버가 필요하지 않습니다: 전용 서버 없이도 자동 결제가 가능합니다.
- PayJoin v2**는 발신자와 수신자의 입력을 단일 트랜잭션으로 병합하여 트랜잭션 그래프 분석을 간소화합니다. Cake Wallet은 두 가지 중요한 개선 사항을 구현합니다:
    - 비동기 트랜잭션**: 발신자와 수신자가 더 이상 비공개 트랜잭션을 완료하기 위해 동시에 온라인 상태일 필요가 없습니다.
    - 서버리스 통신**: 어느 쪽도 PayJoin 서버를 운영할 필요가 없으므로 주요 기술적 장벽이 제거됩니다.
- Coin 제어**를 사용하면 거래 중에 수동으로 UTXO을 선택할 수 있습니다. 이렇게 하면 발신지가 다른 여러 UTXO를 사용할 때 실수로 주소가 연결되는 것을 방지할 수 있습니다.
- 토르** 지원으로 사용자가 토르 네트워크를 통해 네트워크 트래픽을 라우팅할 수 있습니다
- RBF**(수수료로 대체)을 사용하면 트랜잭션을 전송한 후 수수료를 조정할 수 있습니다.


## 1️⃣ Wallet 설정하기


Cake Wallet은 다양한 플랫폼을 지원합니다. 안드로이드`, `iOS/맥OS`, `리눅스`, `윈도우` 중에서 선택할 수 있습니다.  시작하려면 https://docs.cakewallet.com/get-started/ 를 방문하여 운영 체제를 선택하세요.


![image](assets/en/01.webp)


설치 후 'PIN'(4자리 또는 6자리)을 설정합니다. 그러면 확인하실 수 있습니다:


1. '새 Wallet 만들기'(신규 사용자용)

2. 'Wallet 복원'(기존 지갑의 경우)


![image](assets/en/02.webp)


다음 화면에서 다양한 암호화폐 중에서 선택할 수 있습니다. Bitcoin`을 선택하고 `다음`을 탭한 후 `Wallet 이름`을 입력하면 Wallet을 식별할 수 있습니다. 고급 설정`을 탭하면 다양한 `개인정보 설정`이 나타납니다. 이를 변경합니다:



- Fiat API:** '토르 전용'을 선택합니다(가격 요청을 토르로 라우팅)
- 스왑:** '토르 전용'을 선택합니다(Exchange 트래픽 익명화)


기본적으로 BIP-39 seed 유형이 생성되며, Electrum seed 유형으로 변경할 수 있는 옵션이 있습니다. 파생 경로는 다음과 같습니다:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


추가 보안 Layer을 추가하려면 'passphrase'를 설정할 수 있습니다.  passphrase의 주요 목적은 물리적 공격에 대한 추가 보호 기능을 제공하는 것입니다. 공격자가 seed 문구를 찾더라도 올바른 passphrase가 없으면 Wallet에 액세스할 수 없습니다. 즉, seed 문구만으로는 하나의 Wallet을 나타내지만, seed 문구에 passphrase를 더하면 원본과 전혀 다른 Wallet이 만들어집니다. 이 기능은 또한 passphrase로 보호되는 '비밀 지갑'을 가능하게 하고, 그럴듯한 부인력을 제공합니다. 강압적인 상황에서는 passphrase로 보호되는 Wallet에 더 큰 자산을 안전하게 보관하면서 seed 문구를 공개할 수 있습니다.


이미 자체 노드를 실행 중인 경우, `새 사용자 지정 노드 추가`를 토글하고 `노드 Address`를 제공하여 자체 인프라 내에서 트랜잭션과 블록을 검증합니다. 완료되면 `계속`과 `다음`을 탭하여 Wallet을 생성합니다.


![image](assets/en/03.webp)


다음 화면에는 면책 조항이 표시됩니다:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Mnemonic 문구를 저장하는 모범 사례를 알아보려면 이 튜토리얼을 참조하세요:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

알겠습니다. 내 seed을 보여주세요`를 탭하고 이 단어를 안전한 곳에 저장하세요! 그런 다음 `seed 확인`을 탭하고 확인 후 `Wallet 열기`를 탭합니다.


## 2️⃣ 설정


더 자세히 알아보기 전에 '홈 화면'과 '설정'에 대해 살펴 보겠습니다.


홈 화면에서 다양한 항목이 표시되는 것을 볼 수 있습니다:



- 햄버거 메뉴`를 클릭하면 `설정`으로 이동합니다
- 사용 가능한 잔액
- 자동 결제 카드로 자동 결제 Address로 전송된 거래 스캔을 시작하기 위한 자동 결제 카드
- 개인 정보 보호 및 요금 절약 기능으로 PayJoin 카드를 '활성화'하는 PayJoin 카드
- 하단에는 `Wallet 개요`, `수신`, Bitcoin과 다른 통화 간의 `스왑`, `송금` 및 `구매`에 대한 바로 가기가 있습니다


![image](assets/en/11.webp)


햄버거 메뉴` 아이콘을 탭하면 설정 메뉴가 열립니다. 옵션을 살펴봅시다.


![image](assets/en/05.webp)


### A - 연결 및 동기화 🔗


여기에서 Wallet을 다시 연결하고, 노드를 관리하고, 자체 노드에 연결할 수 있습니다(권장). '자동 결제 스캔'에서는 'BLOCK 높이에서 스캔' 또는 '날짜에서 스캔'을 지정하여 스캔을 사용자 지정할 수 있습니다.


![image](assets/en/06.webp)


'알파' 기능으로 토르 네트워크를 통해 트래픽을 라우팅하기 위해 '내장 토르 활성화' 옵션도 있습니다.


### B - 자동 결제 설정 🔈


홈 화면에서 자동 결제 카드를 토글하여 이 기능을 표시할 수 있습니다. '항상 스캔'을 활성화하면 Wallet이 수신되는 자동 결제를 위해 Blockchain을 지속적으로 모니터링할 수 있습니다. 위에서 설명한 대로 스캔 매개변수를 지정하여 스캔 프로세스를 필요에 맞게 사용자 지정할 수 있습니다.


![image](assets/en/07.webp)


### C - 보안 및 백업 🗝️


Wallet를 보호하기 위해 앱 내 안내에 따라 백업을 생성할 수 있습니다. 이렇게 하면 개인키의 안전한 사본을 확보할 수 있으므로 Wallet를 분실하거나 도난당했을 때 복구할 수 있습니다. 또한 seed 문구와 개인 키를 확인하고, PIN을 변경하고, 생체 인증을 활성화하고, 서명/확인하고, 2FA를 설정하여 Layer을 추가로 보호할 수 있습니다.


![image](assets/en/08.webp)


**참고**: 2025년 9월부터 Android 디바이스에서 지문 생체 인증은 최소 클래스 2 생체 인식 구현과 함께 작동해야 하며, 자세한 내용은 [여기](https://source.android.com/docs/security/features/biometric/measure#biometric-classes)를 참조하세요. 그러나 이 요구 사항은 향후 변경될 수 있습니다.


### D - 개인정보 설정 🔒


또한 Tor를 사용하여 인터넷 연결을 암호화하고 외부 소스에 액세스할 때 개인정보를 보호함으로써 Wallet의 보안을 강화할 수 있습니다. 또한 스크린샷을 방지하여 Wallet 정보를 기밀로 유지하고, 자동 생성 주소를 활성화하여 각 거래마다 새 주소를 생성하며, 구매/판매 작업을 비활성화하여 승인되지 않은 거래를 방지할 수 있습니다. 또한 나중에 검토할 또 다른 개인정보 보호 기능인 'PayJoin 활성화'도 가능합니다.


![image](assets/en/09.webp)


### E - 기타 설정 🔧


기타 설정을 통해 수수료 우선순위를 관리하고 거래의 기본 수수료 수준을 설정할 수 있습니다. 이를 통해 현재 네트워크 사용률을 고려하여 자동 결제와 관련된 거래 수수료를 제어할 수 있습니다.


![image](assets/en/10.webp)


## 3️⃣ 자동 결제를 사용하여 ₿itcoin 받기


Bitcoin 수신에는 몇 가지 옵션과 Address 유형이 있습니다. 'SegWit(P2WPKH)` *(bc1q....로 시작)*가 기본 옵션입니다.  이 예에서는 `자동 결제`를 선택하겠습니다.


자동 결제를 받으려면 먼저 케이크 Wallet에서 '받기' 아이콘을 탭하세요. 그 다음, 받을 금액을 입력합니다. Address 유형을 지정하려면 화면 상단의 '받기'를 다시 탭한 다음 옵션에서 '자동 결제'를 선택합니다.


메인 화면에 재사용 가능한 무음 결제 QR코드와 Address이 표시됩니다. 예상대로 Address은 꽤 긴 편입니다:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


이제 BIP-352 호환 Wallet(예: 파란색 Wallet)를 사용하여 이 QR 코드를 스캔하고 결제를 전송합니다. Wallet가 무음 Address에서 고유한 목적지 Address를 파생하는 것을 확인할 수 있습니다.


![image](assets/en/13.webp)


## 4️⃣ 자동 결제를 사용하여 ₿itcoin 보내기


블루 Wallet은 무음 결제만 '보내기'가 가능하므로, 다른 BIP 352 호환 Wallet을 수신자로 사용합니다. 이 프로세스는 일반 Bitcoin 트랜잭션과 동일합니다.



- 홈 화면에서 '보내기'를 탭합니다
- 재사용 가능한 `sp1qq...` Address을 붙여넣거나 앱 내에서 직접 QR 코드를 스캔하세요.
- 사용 가능한 잔액에서 지출할 금액을 선택합니다
- 화면 하단의 '보내기'를 탭하여 거래를 확인합니다


Sp1qq...` Address을 입력하면 Wallet이 자동으로 해당 `bc1p...` Taproot Address(P2TR)을 도출하여 자동 결제에 사용합니다.


선택적으로 모든 거래에 대해 내부 메모를 작성하고, 수수료 설정을 조정하거나, 'Coin 제어' 기능을 사용하여 거래에 대한 특정 UTXO를 선택할 수 있습니다.


![image](assets/en/14.webp)


오른쪽으로 '스와이프'하여 거래를 확인합니다.


거래를 전송하면 이 연락처를 Address 북에 추가할지 묻는 메시지가 표시됩니다.


![image](assets/en/15.webp)


## 6️⃣ PayJoin


PayJoin가 무엇인지 살펴봅시다(https://docs.cakewallet.com/cryptos/Bitcoin/#PayJoin):


페이조인 v2는 Bitcoin의 개인정보 보호 및 수수료 절감 기능으로, 거래의 발신자와 수신자가 함께 단일 거래를 생성할 수 있습니다. 이 트랜잭션에는 발신자와 수신자 *양쪽*의 입력이 포함되어 있어 Bitcoin에 대한 가장 일반적인 감시 기술을 차단하고 일부 상황에서는 더 나은 확장 및 수수료 절감도 가능합니다._ _


PayJoin에 대해 자세히 알아보려면 다음 튜토리얼을 참조하세요.


https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

PayJoin를 사용하려면 양쪽 모두 PayJoin와 호환되는 Wallet이 필요하며, 수신자는 Coin 또는 Wallet의 출력을 하나 이상 가지고 있어야 합니다. 시작하려면 다음 단계를 따르세요:


1. 햄버거 메뉴`를 탭하고 `개인정보` 버튼을 탭합니다

2. PayJoin 사용` 옵션 토글하기

3.  홈 화면에서 '받기'를 탭하면 PayJoin QR코드와 복사 버튼이 표시됩니다(SegWit 선택 시)


![image](assets/en/16.webp)


## 7️⃣ 기타 기능


여러 통화 '스왑', 다양한 공급업체 연결을 통한 '구매 및 판매' 옵션, 선불 카드나 기프트 카드를 구매할 수 있는 '케이크 페이'와 같은 케이크 전용 프로그램 등 여러 가지 기능이 있습니다.


![image](assets/en/17.webp)


## 🎯 결론


자동 결제(BIP-352) 및 PayJoin v2와 같은 기능 덕분에 실용적인 Bitcoin 프라이버시를 제공하는 Cake Wallet에 대한 리뷰입니다.


자동 결제는 일회용 주소를 재사용 가능한 스텔스 주소로 대체하여 수신 거래의 On-Chain 연동을 방지합니다. 이전 버전의 동기화 문제는 눈에 띄게 개선되었지만, 자동 결제를 스캔하고 감지하는 데 필요한 계산 요구 사항이 일부 증가하여 더 많은 리소스와 대역폭이 필요합니다.


PayJoin v2는 추가 수수료나 중앙 조정 없이 발신자와 수신자 입력을 단일 트랜잭션으로 병합하여 체인 분석에 혼란을 줍니다. 이는 일반적인 입력 Ownership 휴리스틱을 깨는 것으로, 모든 입력이 발신자에게 속한다고 가정할 수 없으므로 상당한 이점이 있습니다.


금융 익명성을 우선시하는 사용자에게는 Cake Wallet가 적합한 옵션입니다. 이 도구는 프라이버시 프로토콜을 핵심 기능에 직접 통합하여 기술적 복잡성 없이 액세스할 수 있습니다. 퍼블릭 블록체인에 대한 감시가 증가함에 따라 이와 같은 도구는 가장 중요한 트랜잭션 프라이버시를 유지하는 데 도움이 됩니다. Wallet 환경 내에서 이러한 표준이 더 광범위하게 구현된다면 환영할 만한 발전이 될 것입니다.


## 📚 리소스


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://BIPs.dev/352/](https://BIPs.dev/352/)


https://PayJoin.org/