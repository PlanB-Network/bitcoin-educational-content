---
name: Blockstream App - Desktop
description: 컴퓨터에서 블록스트림 앱으로 Hardware Wallet을 사용하려면 어떻게 해야 하나요?
---
![cover](assets/cover.webp)



## 1. 소개



### 1.1 튜토리얼 목표





- 이 튜토리얼에서는 컴퓨터에서 **블록스트림 앱**을 사용하여 **Hardware Wallet**으로 **온체인** Wallet를 관리하고, 메인 Blockchain Bitcoin에 기록된 보안 트랜잭션을 활성화하는 방법을 설명합니다.
- 설치, 초기 구성, Hardware Wallet 연결, 온체인 비트코인 수신 및 전송에 대해 설명합니다.
- 참고: 부록의 다른 튜토리얼에서는 Liquid, 시청 전용 및 모바일 애플리케이션에 대해 설명합니다.



### 1.2 타겟 고객





- 초보자**: 안전한 데스크톱 소프트웨어와 Hardware Wallet로 비트코인을 관리하고자 하는 사용자.
- 중급 사용자**: 온체인 트랜잭션과 토르 또는 SPV와 같은 프라이버시 옵션에 Hardware Wallet을 사용하는 방법을 이해하고자 하는 분들입니다.



### 1.3. 하드웨어 지갑의 배경





- Hardware Wallet**, **Cold Wallet**: 개인 키를 오프라인에 저장하는 물리적 장치로, **Hot 지갑**(연결된 장치의 소프트웨어 지갑)과 달리 사이버 공격에 대해 높은 수준의 보안을 제공합니다.
- 권장 사용**:
    - 많은 금액을 확보하거나 장기적으로 저축하는 데 이상적입니다.
    - 연결된 장치와 관련된 위험으로부터 자금을 보호하고자 하는 보안에 중점을 둔 사용자에게 적합합니다.
- 제한 사항**: 잔액, generate 주소를 확인하고 Hardware Wallet 서명 트랜잭션을 브로드캐스트하려면 블록스트림 앱과 같은 소프트웨어가 필요합니다.



## 2. 블록스트림 앱 소개





- 블록스트림 앱**은 Bitcoin의 지갑과 자산을 관리하기 위한 모바일(iOS, 안드로이드) 및 데스크톱 애플리케이션입니다. 2016년 블록스트림에 인수된 후 *GreenAddress*로 불리다가 *Blockstream Green*(2019년)로 이름이 변경되었으며, 현재는 *블록스트림 앱*(2025년)으로 불리고 있습니다.
- 주요 기능**:
- Blockchain Bitcoin의 온체인** 거래.
    - Liquid** 네트워크에서의 거래(빠른 기밀 교환을 위한 Sidechain).
- 키에 액세스하지 않고도 자금을 모니터링할 수 있는 감시 전용** 포트폴리오.
    - 개인 정보 보호 옵션: **Tor**를 통한 연결, Electrum을 통한 **개인 노드** 연결, 타사 노드에 대한 의존성을 줄이기 위한 **SPV** 인증.
    - 미확인 트랜잭션의 속도를 높이기 위한 **Replace-by-fee(RBF)** 기능.
- 호환성**: 블록스트림 제이드**와 같은 하드웨어 지갑을 통합합니다.
- Interface**: 초보자를 위한 직관적인 기능, 전문가를 위한 고급 옵션이 있습니다.
- 참고**: 이 가이드는 데스크톱 버전에서 Hardware Wallet를 사용한 온체인 사용에 중점을 두고 있습니다. 부록으로 제공되는 다른 튜토리얼에서는 모바일 애플리케이션, 온체인, Liquid 및 감시 전용 기능에 대한 사용법을 다룹니다.



## 3. 블록스트림 앱 데스크톱 설치 및 설정



### 3.1. 다운로드





- 공식 웹사이트](https://blockstream.com/app/)로 이동하여 "_지금 다운로드하기_"를 클릭합니다. 사용 중인 운영 체제(Windows, macOS, Linux)에 해당하는 버전을 다운로드합니다.
- 참고**: 사기성 소프트웨어를 피하려면 반드시 공식 출처에서 다운로드하세요.



### 3.2. 초기 구성





- 홈 화면**: 애플리케이션을 처음 열면 Wallet이 구성되지 않은 화면이 표시됩니다. 생성하거나 가져온 포트폴리오는 나중에 여기에 표시됩니다.



![image](assets/fr/02.webp)





- 설정 사용자 지정**: 왼쪽 하단의 설정 아이콘을 클릭하고 아래 옵션을 조정한 다음 Interface을 종료하여 계속 진행합니다.



![image](assets/fr/03.webp)



#### 3.2.1. 일반 매개변수





- 설정 메뉴에서 "**일반**"을 클릭합니다.
- 기능**: 소프트웨어 언어를 변경하고 필요한 경우 실험적 기능을 활성화합니다.



![image](assets/fr/04.webp)



#### 3.2.2. 토르를 통한 연결





- 설정 메뉴에서 "**네트워크**"를 클릭합니다.
- 기능**: 연결을 암호화하는 익명 네트워크인 **Tor**를 통해 네트워크 트래픽을 라우팅합니다.
- 왜? 네트워크(예: 공용 Wi-Fi)를 신뢰할 수 없는 경우 IP Address를 숨기고 개인 정보를 보호하는 데 이상적입니다.
- 단점**: 암호화로 인해 애플리케이션 속도가 느려질 수 있습니다.
- 권장**: 기밀 유지가 우선순위라면 토르를 활성화하되, 연결 속도를 테스트하세요.



![image](assets/fr/05.webp)



#### 3.2.3. 개인 노드에 연결하기





- 설정 메뉴에서 "**맞춤형 서버 및 유효성 검사**"를 클릭합니다.
- 기능**: 일렉트럼 서버**를 통해 **완성된 Bitcoin 노드**에 애플리케이션을 연결합니다.
- 왜? Blockchain 데이터를 완벽하게 제어할 수 있어 블록스트림 서버에 대한 의존성을 제거합니다.
- 전제 조건**: 구성된 Bitcoin 노드.
- 추천**: 최대한의 주권을 원하는 고급 사용자.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV 확인





- 설정 메뉴에서 "**맞춤형 서버 및 유효성 검사**"를 클릭합니다.
- 기능**: 전체 Blockchain을 저장하지 않고 블록 헤더를 다운로드하고 포함 증명(머클)으로 거래를 확인하는 **간소화된 결제 확인(SPV)**을 사용합니다.
- 왜? 블록스트림의 기본 노드에 대한 의존성을 줄이면서 디바이스에는 경량화를 유지합니다.
- 단점**: 일부 정보를 타사 노드에 의존하기 때문에 Full node보다 보안성이 떨어집니다.
- 권장**: 개인 노드를 사용할 수 없지만 최적의 보안을 위해 Full node를 선호하는 경우 SPV를 활성화하세요.



![image](assets/fr/07.webp)



## 4. Hardware Wallet을 블록스트림 앱에 연결하기



### 4.1. 사전 고려 사항



#### 4.1.1. Ledger 사용자의 경우





- Blockstream Green은 Ledger 디바이스(나노 S, 나노 X)에서만 **Bitcoin 레거시** 애플리케이션을 지원합니다.
- 장치를 연결하기 전에 **Ledger Live**에서 따라야 할 단계 :


1. "설정"** → **"실험적 기능"**으로 이동하여 **개발자 모드**를 활성화합니다.


2. "내 Ledger"** → **"앱 카탈로그"**로 이동한 후 **Bitcoin 레거시** 애플리케이션을 설치합니다


3. Blockstream Green를 시작하기 전에 Ledger에서 **Bitcoin 레거시** 애플리케이션을 열어 연결을 설정하세요.




- 참고**: 연결할 때 Ledger이 PIN 코드로 잠금 해제되어 있고 Bitcoin 레거시 애플리케이션이 활성화되어 있는지 확인하세요.



#### 4.1.2 Hardware Wallet 초기화하기





- Hardware Wallet(Ledger, Trezor 또는 블록스트림 제이드)을 한 번도 사용한 적이 없는 경우(Blockstream Green 또는 Ledger Live와 같은 다른 소프트웨어와 함께 사용), 먼저 초기화해야 합니다. 이 단계는 카메라나 옵저버가 없는 안전한 환경에서 수행해야 합니다:


1. **seed 구문 생성 / Mnemonic 구문** (12, 18 또는 24단어): 종이에 주의 깊게 적으세요.


2. **seed 구문 검증**: 확장된 공개키를 확인하는 등 언급된 단어에서 Wallet 가져오기를 테스트합니다. Wallet로 자금을 송금하고 seed 구문을 영구적으로 보호하기 전에 수행해야 합니다.


3. **seed 문구 고정하기**: 문구를 물리적 매체(종이 또는 금속)에 인쇄하여 안전한 장소에 보관하세요. 디지털 방식으로 저장하지 마세요(스크린샷, 클라우드, 이메일 등).




- 중요**: seed 문구는 기기를 분실하거나 오작동하는 경우 자금을 복구할 수 있는 유일한 수단입니다. 액세스 권한이 있는 사람은 누구나 비트코인을 훔칠 수 있습니다.
- seed 문장을 백업하고 확인하기 위한 리소스**를 확인하세요:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. 이 튜토리얼의 구성 :





- Hardware Wallet은 이미 seed 문구와 잠금 PIN 코드로 초기화되어 있다고 가정하겠습니다.
- Hardware Wallet가 블록스트림 앱에 연결되지 않았다고 가정하고 새 계정을 만들어야 합니다. Hardware Wallet를 이미 블록스트림 앱과 함께 사용한 적이 있는 경우, 애플리케이션을 열면 계정이 자동으로 표시됩니다.



### 4.2. 연결 시작





- 홈 화면에서 "**새 Wallet 설정**"을 클릭한 다음 이용 약관을 확인하고 "**시작하기**"를 클릭합니다:



![image](assets/fr/08.webp)





- "**온 Hardware Wallet**" 옵션을 선택합니다:



![image](assets/fr/09.webp)





- 블록스트림 제이드**를 사용 중이라면 해당 버튼을 클릭하세요. 그렇지 않으면 "**다른 하드웨어 장치 연결**"을 선택하세요:



![image](assets/fr/10.webp)





- Hardware Wallet를 USB를 통해 컴퓨터에 연결하고 블록스트림 앱에서 선택합니다:



![image](assets/fr/22.webp)





- 블록스트림 앱이 포트폴리오 정보를 가져오는 동안 잠시 기다려주세요:



![image](assets/fr/23.webp)



### 4.3. 계정 만들기





- Hardware Wallet을 이미 블록스트림 앱과 함께 사용했다면, 가져오기 후 계정이 Interface에 자동으로 표시됩니다. 그렇지 않은 경우 "**계정 만들기**"를 클릭하여 계정을 생성하세요:



![image](assets/fr/24.webp)





- "**표준**"을 선택하면 클래식 Bitcoin 포트폴리오를 구성할 수 있습니다:



![image](assets/fr/25.webp)





- 계정이 생성되면 기본 Interface 포트폴리오에 액세스할 수 있습니다:



![image](assets/fr/26.webp)





## 5. Hardware Wallet과 함께 온체인 Wallet 사용



### 5.1. 비트코인 받기





- 메인 포트폴리오 화면에서 "**수신**"을 클릭합니다:



![image](assets/fr/27.webp)





- 애플리케이션에 **빈 수신 Address**가 표시됩니다. 각 수신마다 새 Address를 사용하면 기밀성이 향상됩니다. "**Address 복사하기**"를 클릭하여 Address를 복사하거나 발신자가 표시된 QR 코드를 스캔하도록 합니다:



![image](assets/fr/12.webp)



**옵션** :




- (1) 화살표를 클릭하여 포트폴리오에 연결된 새 generate으로 이동합니다.
- (2) 특정 금액을 요청하려면 "**추가 옵션**"을 클릭한 다음 "**요청 금액**"을 클릭합니다. QR이 업데이트되고 Address가 다음과 같은 Bitcoin 결제 URI로 대체됩니다: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) 이전 Address을 재사용하려면 "**추가 옵션**"을 클릭한 다음 "**주소 목록**"을 클릭합니다:



![image](assets/fr/14.webp)





- 확인**: 오류나 공격(예: 클립보드를 수정하는 멀웨어)을 피하기 위해 공유 Address을 주의 깊게 확인하세요.
- 트랜잭션이 네트워크에 브로드캐스트되면 Wallet에 표시됩니다. 트랜잭션이 변경되지 않은 것으로 간주하려면 1~6번의 확인을 기다립니다.



![image](assets/fr/28.webp)



### 5.2. 비트코인 보내기





- 기본 포트폴리오 화면에서 "**보내기**"를 클릭합니다.



![image](assets/fr/29.webp)





- 세부 정보를 입력합니다:
    - (1) 선택한 자산이 **Bitcoin**(온체인)인지 확인합니다.
    - (2) 수신자의 **Address**을 붙여넣거나 웹캠으로 QR 코드를 스캔하여 입력합니다.
    - (3) 송금할 **금액**(BTC, 사토시 또는 기타 단위)을 입력합니다.




![image](assets/fr/16.webp)





- 거래 수수료**(선택 사항)를 선택합니다:
 - 긴급도에 따라 제안된 옵션(빠름, 중간, 느림) 중에서 예상 확인 시간과 함께 선택합니다.
 - 사용자 지정 요금의 경우, 바이바이트당 사토시 수를 수동으로 조정합니다. 이는 홈 화면에 표시됩니다. Mempool.space](https://Mempool.space/)도 참조하세요.



![image](assets/fr/17.webp)





- UTXO 수동 선택**(선택 사항): "**Coin 수동 선택**"을 클릭하여 트랜잭션에 사용할 특정 UTXO를 선택합니다.



![image](assets/fr/18.webp)





- 예비 확인**: 요약 화면에서 Address, 금액, 수수료를 확인한 다음 "**거래 확인**"을 클릭합니다. 실제로 거래는 UTXO(사토시)가 인출될 주소와 관련된 비밀 키가 있는 Hardware Wallet로 서명하기 전까지는 네트워크에 공개되지 않습니다.



![image](assets/fr/19.webp)





- 최종 확인 및 서명**: Hardware Wallet** 화면에서 모든 거래 매개변수가 올바른지 확인한 다음 이를 사용해 거래에 서명합니다. Address 오류는 돌이킬 수 없는 자금 손실을 초래할 수 있습니다.





- 브로드캐스트**: 서명이 완료되면 블록스트림 앱은 자동으로 Bitcoin 네트워크에서 트랜잭션을 브로드캐스트합니다.



![image](assets/fr/20.webp)





- 후속 조치**:
 - 거래는 확인될 때까지 Wallet 홈 화면에 '보류 중'으로 표시됩니다.
 - 거래가 확인되지 않은 경우, **Replace-by-fee(RBF)** 기능을 사용하면 수수료를 높여 확인 속도를 높일 수 있습니다(부록 참조).



![image](assets/fr/21.webp)



## 부록



### A1. 기타 블록스트림 튜토리얼





- Liquid Network 사용 :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- 포트폴리오 가져오기 및 추적 "보기 전용" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- 휴대폰에서 블록스트림 앱 사용(Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Replace-by-fee(RBF)에 대한 설명





- 정의**: Replace-by-fee(RBF)은 발신자가 수수료를 높여 **온체인** 거래의 확인을 가속화할 수 있는 Bitcoin 네트워크의 기능입니다.
- 제한**:
    - RBF은 Liquid 또는 라이트닝 거래에는 사용할 수 없습니다.
    - 초기 트랜잭션은 RBF 호환으로 표시되어야 하며, 블록스트림 앱은 이를 자동으로 수행합니다.
- 자세한 내용은 [용어집](https://planb.network/resources/glossary/RBF-replacebyfee)을 참조하세요.



### A3. 모범 사례





- 복구 문구**를 보호하세요:
    - Hardware Wallet의 Mnemonic 문구를 안전한 장소의 물리적 매체(종이, 금속)에 보관하세요.
    - 디지털 방식으로 저장하지 마세요(클라우드, 이메일, 스크린샷).
    - 튜토리얼 : Mnemonic 문구 저장하기 :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- 개인 정보 보호**:





    - generate은 각 온체인 수신에 대한 새로운 Address입니다.
    - Tor** 또는 **SPV**를 활성화하여 추적을 제한합니다.
    - 일렉트럼을 통해 자체 Bitcoin 노드에 연결하여 주권을 최대한 확보하세요.
- 항상 배송지 주소를 확인하세요**:





    - 서명하기 전에 Hardware Wallet 화면에서 Address을 확인하세요.
    - 수동 오류를 방지하려면 복사/붙여넣기 또는 QR 코드를 사용하세요.
- 비용 최적화**:





    - 긴급성 및 네트워크 혼잡도에 따라 요금을 조정합니다([Mempool.space](https://Mempool.space/) 참조).
    - 온체인 보안이 필요하지 않은 빠르고 저렴한 트랜잭션에는 Liquid 또는 라이트닝을 사용하세요.
- 소프트웨어를 업데이트합니다:





    - 최신 기능 및 보안 패치를 통해 블록스트림 앱과 Hardware Wallet 펌웨어를 최신 상태로 유지하세요.



### A4. 추가 리소스





- 공식 링크**:
    - [공식 웹사이트](https://blockstream.com/)
    - [블록스트림 앱 지원](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): 문서 및 채팅
    - [깃허브](https://github.com/Blockstream/green_qt)





- 블록 탐색기**:
    - 온체인 : [Mempool.space](https://Mempool.space/)
    - Liquid: [블록스트림 정보](https://blockstream.info/Liquid)
    - 라이트닝 : [1ML(Lightning Network)](https://1ml.com/)





- 복구 문구 보안하기:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- Liquid Network** :



[용어집](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- Lightning Network**:



[용어집](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb