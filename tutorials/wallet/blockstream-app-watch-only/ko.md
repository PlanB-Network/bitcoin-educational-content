---
name: Blockstream App - Watch-Only
description: 블록스트림 앱에서 Watch-only wallet을 구성하려면 어떻게 해야 하나요?
---

![cover](assets/cover.webp)


## 1. 소개


### 1.1 튜토리얼의 목표





- 이 튜토리얼에서는 **블록스트림 앱** 모바일 애플리케이션의 **워치 전용** 기능을 설정하고 사용하여 개인 키에 액세스하지 않고 Bitcoin Wallet를 모니터링하는 방법을 설명합니다.
- 설치, 초기 구성, 확장 공개키 가져오기, 잔액 및 generate 수신 주소 추적에 사용하는 방법을 다룹니다.
- 참고: 부록에 제공된 다른 튜토리얼은 온체인, Liquid 및 데스크톱 버전을 다룹니다.



### 1.2. 타겟 고객





- 초보자**: 직관적인 모바일 애플리케이션을 통해 Bitcoin 포트폴리오(종종 Hardware Wallet와 연결)를 모니터링하고자 하는 사용자.
- 중급 사용자**: 읽기 전용 포트폴리오를 관리하면서 Tor나 SPV와 같은 개인정보 보호 옵션을 사용하고자 하는 분들.
- Hardware Wallet 소유자**: 기기를 연결하지 않고도 잔액과 generate 주소를 확인할 수 있습니다.
- 기업 및 상점**:
 - 개인 키를 노출하지 않고도 회계 목적으로 거래를 추적할 수 있습니다.
 - 온라인 결제 시스템에서 개인 키를 입력하지 않고도 수신된 거래를 확인할 수 있습니다.
 - 직원이 개인 키에 액세스하지 않고도 새 수신 주소를 generate로 설정할 수 있습니다.
- 단체 및 크라우드 펀딩**: 자금에 대한 접근을 허용하지 않고 기부자에게 잔액을 투명하게 표시합니다.



### 1.3. 감시 전용 소개



감시 전용** Wallet를 사용하면 개인 키에 액세스하지 않고도 Bitcoin Wallet의 거래와 잔액을 모니터링할 수 있습니다. 기존 Wallet와 달리 **확장 공개 키**("**xpub**", "zpub", "ypub" 등)와 같은 공개 데이터만 저장하므로 Blockchain Bitcoin의 수신 주소를 얻고 거래 내역을 추적할 수 있습니다. 개인 키가 없으면 애플리케이션에서 자금을 지급할 수 없으므로 보안이 강화됩니다.



![image](assets/fr/10.webp)



**왜 Watch-only wallet을 사용해야 하나요?





- 보안**: 연결된 장치에서 개인 키를 노출하지 않고 **Hardware Wallet**로 보호되는 포트폴리오를 모니터링하는 데 이상적입니다.
- 편리함**: Hardware Wallet를 연결하지 않고도 잔액과 generate 새 수취인 주소를 확인할 수 있습니다.
- 기밀성**: Tor** 또는 **SPV**와 같은 옵션과 호환되어 타사 서버에 대한 의존성을 제한합니다.
- 사용 사례**: 이동 중 자금 추적, 결제 수취를 위한 주소 생성 또는 개인 키 위험 없이 거래 확인.



![image](assets/fr/01.webp)



### 1.4. 확장 공개 키



확장 공개 키**(xpub, ypub, zpub 등)는 개인 키에 대한 액세스 권한 없이 모든 하위 공개 키와 관련 수신 주소를 생성하는 Bitcoin Wallet에서 파생된 데이터 조각입니다.





- 작동 방식**: 확장 공개 키는 결정론적 프로세스(BIP-32)를 통해 seed 구문에서 생성됩니다. 이는 하위 공개키의 계층 트리를 생성하며, 각 하위 공개키는 수신 Address으로 변환할 수 있습니다. 감시하는 Wallet과 동일한 파생 경로(예: `m/44'/0'/0'`)를 사용하여 Watch-only wallet는 동일한 주소를 생성하므로 자금을 추적하고 새로운 수신 주소를 생성할 수 있습니다.



![image](assets/fr/11.webp)





- 확장된 공개 키 유형
- xpub**: 레거시 포트폴리오("1"로 시작하는 주소, BIP-44) 및 Taproot 포트폴리오("bc1p"로 시작하는 주소, BIP-86)에 사용됩니다.
- ypub**: 호환되는 SegWit 지갑("3"으로 시작하는 주소, BIP-49)을 위해 설계되었습니다.
- zpub**: 네이티브 SegWit 포트폴리오와 연결("bc1q"로 시작하는 주소, BIP-84).
- 기타(tpub, upub, vpub 등): 대체 네트워크(예: Testnet) 또는 특정 표준에 사용됩니다. 예를 들어 **tpub**는 Testnet 네트워크용입니다.





- 구별**: Xpub, ypub 또는 zpub 중 선택은 Address 유형(레거시, SegWit, Taproot 또는 중첩된 SegWit)과 Wallet에서 사용하는 BIP 표준에 따라 달라집니다. 소스 포트폴리오에 필요한 형식을 확인하여 블록스트림 앱과의 호환성을 확인하세요.





- 보안 및 기밀성**: 확장된 공개 키는 자금을 사용할 수 없으므로 보안 측면에서 민감하지 않습니다(개인 키에 액세스할 수 없음). 하지만 모든 공개 주소와 관련 거래 내역이 공개되므로 기밀성 측면에서는 민감합니다.



**권장**: 확장 공개 키를 민감한 정보로 보호하세요.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet 알림





- Hot Wallet**, **Software Wallet**, **Wallet 모바일**, **Software Wallet**: 스마트폰, 컴퓨터 또는 인터넷에 연결된 모든 장치에 설치된 애플리케이션의 모든 이름으로, Bitcoin Wallet의 개인키를 관리하고 보호할 수 있습니다.
- 키를 오프라인에서 격리하는 **하드웨어 지갑**, 일명 **Cold 지갑**과 달리 소프트웨어 지갑은 연결된 환경에서 작동하기 때문에 사이버 공격에 더 취약합니다.





- 권장 사용**:
    - 특히 일일 거래의 경우 적당한 양의 Bitcoin을 관리하는 데 이상적입니다.
    - Hardware Wallet가 불필요하게 느껴질 수 있는 초보자나 자산이 제한적인 사용자에게 적합합니다.





- 제한 사항**: 거액의 자금이나 장기 저축을 보관하기에는 안전성이 떨어집니다. 이 경우 Hardware Wallet를 선택하세요.




## 2. 블록스트림 앱 소개





- 블록스트림 앱**은 Bitcoin의 포트폴리오와 자산을 관리할 수 있는 모바일(iOS, 안드로이드) 및 데스크톱 애플리케이션입니다. 2016년에 [블록스트림](https://blockstream.com/)이 인수했으며, 이전에는 *Green Address*, 이후 *Blockstream Green*으로 명명되었습니다.
- 주요 기능**:
- Blockchain Bitcoin의 온체인** 트랜잭션.
    - Liquid** 네트워크에서의 거래(빠른 기밀 교환을 위한 Sidechain).
- 키에 액세스하지 않고도 자금을 모니터링할 수 있는 감시 전용** 포트폴리오.
    - 개인 정보 보호 옵션: **Tor**를 통한 연결, Electrum을 통한 **개인 노드** 연결, 타사 노드에 대한 의존성을 줄이기 위한 **SPV** 인증.
    - 미확인 트랜잭션의 속도를 높이기 위한 **Replace-by-fee(RBF)** 기능.
- 호환성**: 블록스트림 제이드**와 같은 하드웨어 지갑을 통합합니다.
- Interface**: 초보자를 위한 직관적인 기능, 전문가를 위한 고급 옵션이 있습니다.
- 참고**: 이 가이드는 온체인 사용에 중점을 두고 있습니다. 부록의 다른 튜토리얼에서는 온체인, 보기 전용 및 데스크톱 버전을 다룹니다.




## 3. 블록스트림 앱 설치 및 구성하기



### 3.1. 다운로드





- Android**의 경우:
    - 구글 플레이 스토어에서 [블록스트림 앱](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)을 다운로드하세요.
    - 대안: 다른 방법: [블록스트림의 공식 깃허브](https://github.com/Blockstream/green_android)에서 제공되는 APK 파일을 통해 설치하세요.
- IOS**의 경우:
    - 앱스토어에서 [블록스트림 앱](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)을 다운로드하세요.
- 참고**: 사기성 애플리케이션을 피하려면 반드시 공식 출처에서 다운로드하세요.



### 3.2. 초기 구성





- 홈 화면**: 애플리케이션을 처음 열면 Wallet이 구성되지 않은 화면이 표시됩니다. 생성하거나 가져온 포트폴리오는 나중에 여기에 표시됩니다.



![image](assets/fr/02.webp)





- 설정 사용자 지정**: "애플리케이션 설정"을 클릭하고 아래 옵션을 조정한 후 "저장"을 클릭하고 애플리케이션을 다시 시작하여 포트폴리오를 생성합니다.



![image](assets/fr/03.webp)



#### 3.2.1. 개인정보 보호 강화(Android 전용)





- 기능**: 스크린샷을 비활성화하고, 작업 관리자에서 애플리케이션 미리보기를 숨기고, 휴대폰이 잠겨 있을 때 액세스를 잠급니다.
- 왜? 무단 물리적 액세스 또는 화면 캡처 멀웨어로부터 데이터를 보호합니다.



#### 3.2.2. 토르를 통한 연결





- 기능**: 연결을 암호화하는 익명 네트워크인 **Tor**를 통해 네트워크 트래픽을 라우팅합니다.
- 왜? 네트워크(예: 공용 Wi-Fi)를 신뢰할 수 없는 경우 IP Address를 숨기고 개인 정보를 보호하는 데 이상적입니다.
- 단점**: 암호화로 인해 애플리케이션 속도가 느려질 수 있습니다.
- 권장**: 기밀 유지가 우선순위라면 토르를 활성화하되, 연결 속도를 테스트하세요.



#### 3.2.3. 개인 노드에 연결하기





- 기능**: 일렉트럼 서버**를 통해 **완성된 Bitcoin 노드**에 애플리케이션을 연결합니다.
- 왜? Blockchain 데이터를 완벽하게 제어하여 블록스트림 서버에 대한 의존성을 제거합니다.
- 전제 조건**: 구성된 Bitcoin 노드.
- 추천**: 최대한의 주권을 원하는 고급 사용자.



#### 3.2.4. SPV 확인





- 기능**: 간소화된 결제 검증(SPV)**을 사용하여 전체 체인을 다운로드하지 않고 특정 Blockchain 데이터를 직접 검증합니다.
- 왜? 블록스트림의 기본 노드에 대한 의존성을 줄이면서 모바일 디바이스에서는 경량화를 유지합니다.
- 단점**: 일부 정보를 타사 노드에 의존하기 때문에 Full node보다 보안성이 떨어집니다.
- 권장**: 개인 노드를 사용할 수 없지만 최적의 보안을 위해 Full node을 선호하는 경우 SPV를 활성화하세요.





## 4. Bitcoin "시청 전용" 포트폴리오 만들기



### 4.1. 확장된 공개 키 복구



Watch-only wallet을 설정하려면 먼저 모니터링할 Wallet의 확장 공개키(xpub, ypub, zpub 등)를 얻어야 합니다. 이 정보는 일반적으로 소프트웨어 또는 Hardware Wallet의 설정 또는 "Wallet 정보" 섹션에서 확인할 수 있습니다.





- 블록스트림 앱의 예시: Wallet 홈 화면에서 "설정"으로 이동한 다음 "Wallet 세부 정보"로 이동하여 zpub를 복사합니다:



![image](assets/fr/09.webp)





- 대안 1: 다음 단계에서 스캔할 수 있는 확장 공개 키가 포함된 QR 코드 generate.
- 대안 2: output descriptor를 제공하는 경우 Wallet을 사용합니다.



### 4.2. Wallet 시계 전용 가져오기





- 주의**: 카메라나 참관인이 없는 비공개 환경에서 포트폴리오를 설정하세요.
- 홈 화면에서 "새 포트폴리오 설정"을 클릭한 다음 "시작하기"를 클릭합니다:



![image](assets/fr/04.webp)





- 다음 화면이 나타납니다:



![image](assets/fr/06.webp)






- (1) **"모바일 Wallet 설정"** : 새로운 Hot Wallet을 생성합니다. 부록의 "블록스트림 앱 - 온체인" 튜토리얼을 참조하세요.
- (2) **"백업에서 복원"**: Mnemonic 구문(12단어 또는 24단어)을 사용하여 기존 포트폴리오를 가져옵니다. 주의: 연결된 장치에 노출되어 보안이 무효화되므로 Cold Wallet에서 이 구문을 가져오지 마세요.
- (3) **"보기 전용"**: 이 튜토리얼에서 관심 있는 옵션입니다.





- 그런 다음 "**단일 서명**"과 "**Bitcoin**" 네트워크를 선택합니다:



![image](assets/fr/12.webp)





- 확장 공개 키(xpub, ypub, zpub 등)를 붙여넣거나 해당 QR 코드를 스캔하거나 output descriptor를 입력합니다. 애플리케이션에 "xpub"가 지정되어 있더라도 ypub, zpub 등의 키도 인증됩니다. 그런 다음 "연결"을 클릭합니다:



![image](assets/fr/13.webp)




### 4.3. Wallet 시계 전용 사용



Watch-only wallet을 가져오면 확장 공개키에서 파생된 주소의 총 잔액과 거래 내역이 표시됩니다. 온체인 트랜잭션만 표시됩니다(Liquid 트랜잭션은 무시됨). Liquid Wallet을 모니터링하려면 이전 단계에서 "Liquid"을 선택하여 가져오기를 반복합니다.





- 잔액 및 내역 보기**: 홈 화면에서 총 잔액과 온체인 거래 내역을 확인할 수 있습니다:



![image](assets/fr/14.webp)





- generate 수신 Address**: "트랜잭션"을 클릭한 다음 "받기"를 클릭해 새로운 온체인 Address을 생성합니다. QR 코드를 통해 공유하거나 복사하여 자금을 받습니다:



![image](assets/fr/15.webp)





- 자금 보내기**: "거래"**를 클릭한 다음 **"보내기"**를 클릭합니다. 입력할 수 있습니다:
 - 수신자의 Address.
 - 거래 금액입니다.
 - 거래 수수료.



하지만 Watch-only wallet에는 개인 키가 보관되어 있지 않으므로 직접 송금할 수 없습니다. 거래에 서명하려면 QR 코드를 스캔하여 Hardware Wallet 또는 Exchange PSBT를 연결하세요(예: Coldcard Q에서 사용 가능한 옵션).



![image](assets/fr/16.webp)





- 참고**: 오류를 방지하기 위해 항상 수신 Address와 거래 내역을 확인하세요. 잘못된 Address로 송금된 자금은 복구할 수 없습니다.




## 부록



### A1. 기타 블록스트림 앱 튜토리얼





- 온체인 네트워크 사용 :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Liquid Network 사용 :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- 데스크톱 버전 :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. 확장된 공개 키





- 용어집 :
 - [확장 공개 키](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- 코스 :
 - [게시된 링크](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. 모범 사례



블록스트림 앱**을 안전하고 효율적으로 사용하려면 다음 권장 사항을 따르세요. 이는 **Bitcoin (온체인)**, **Liquid**, **라이트닝** 네트워크에서 자금을 보호하고 거래를 최적화하며 기밀을 유지하는 데 도움이 될 것입니다.





- 복구 문구**를 보호하세요:
 - 튜토리얼: Mnemonic 구문 저장하기



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 보안 인증**을 사용합니다:
 - 애플리케이션에 대한 액세스를 보호하려면 **강력한 PIN** 또는 **생체인증**(지문 또는 얼굴 인식)을 활성화하세요.
 - PIN 또는 생체 인식 데이터를 공유하지 마세요.





- 개인 정보 보호**:
 - generate은 각 온체인에 대한 새로운 Address 또는 Blockchain의 추적을 제한하기 위한 Liquid 수신입니다.
 - "강화된 개인정보 보호", "토르" 및 "SPV" 기능을 활성화합니다.
 - 기밀성을 극대화하려면 퍼블릭 노드를 사용하는 대신 Electrum 서버를 통해 Wallet를 자체 Bitcoin 노드에 연결하세요





- 필요에 가장 적합한 네트워크를 선택하세요:
- 온체인**: 장기 보관 또는 고액 거래에 선호됩니다(금액 대비 수수료가 무시할 수 있는 수준).
- Liquid**: 기밀성이 강화된 빠르고 저렴한 전송에 사용하세요.
- Lightning**: 소액 송금 시 저렴한 비용으로 즉시 송금할 수 있습니다.





- 항상 배송지 주소를 확인하세요**:
 - 송금하기 전에 Address을 주의 깊게 확인하세요. 잘못된 Address로 송금한 자금은 영원히 손실됩니다. 복사/붙여넣기 또는 QR코드 스캔을 사용하고, 절대 손으로 Address을 복사/수정하지 마세요.





- 비용 최적화**:
 - 온체인 트랜잭션의 경우 긴급성과 네트워크 혼잡도에 따라 적절한 수수료(느린, 중간, 빠른)를 선택하세요.
 - 소량의 경우 Liquid 또는 Lightning을 사용하세요.





- 애플리케이션을 최신 상태로 유지




### A4. 추가 리소스





- 공식 블록스트림 링크:**
- [공식 웹사이트](https://blockstream.com/)
- [모바일 애플리케이션 지원](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): 문서 및 채팅
- [깃허브](https://github.com/Blockstream/green_android)





- 블록 탐색기:**
 - 온체인 **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[블록스트림 정보](https://blockstream.info/Liquid)**
 - 라이트닝: **[1ML (Lightning Network)](https://1ml.com/)**





- 학습 및 튜토리얼:** **[Plan ₿ Network](https://planb.network/)**
  - 복구 문구 보안



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
- [용어집](https://planb.network/fr/resources/glossary/Liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network**:
- [용어집](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb