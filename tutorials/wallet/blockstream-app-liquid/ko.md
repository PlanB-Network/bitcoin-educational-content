---
name: Blockstream App - Liquid
description: 블록스트림 앱을 구성하고 Liquid Network을 사용하는 방법
---
![cover](assets/cover.webp)


## 1. 소개


### 1.1 튜토리얼 목표





- 이 튜토리얼에서는 **블록스트림 앱** 모바일 애플리케이션을 사용하여 **Bitcoin Liquid** 포트폴리오, 즉 Bitcoin "Liquid" 사이드 체인에 직접 기록된 트랜잭션을 관리하는 방법을 설명합니다.
- 설치, 초기 구성, Software Wallet 생성, Liquid에서 비트코인을 받고 보내는 작업을 다룹니다.
- 참고: 부록의 다른 튜토리얼에서는 온체인, 시청 전용 및 데스크톱 버전에 대해 설명합니다.



### 1.2 타겟 고객





- 초보자**: 직관적인 모바일 애플리케이션으로 비트코인을 관리하고 Liquid Network를 통합하고자 하는 사용자.
- 중급 사용자**: 온체인 기능과 토르 또는 SPV와 같은 프라이버시 옵션을 이해하고자 하는 분들입니다.



### 1.3 Liquid 소개



**Liquid**는 **[블록스트림](https://blockstream.com/Liquid/)**에서 개발한 Bitcoin의 **Sidechain**으로, 더 빠르고 더 많은 Confidential Transactions 및 고급 기능을 제공하면서 메인 Blockchain Bitcoin과 연결되도록 설계되었습니다.



Sidechain는 **양방향 페그**라는 메커니즘을 사용하여 Bitcoin과 병렬로 작동하는 독립적인 Blockchain입니다. 이 시스템은 비트코인을 메인 Blockchain에 고정하여 **Liquid-비트코인(L-BTC)**을 생성하며, 이는 원래 비트코인과 가치의 패리티를 유지하면서 Liquid Network에서 유통되는 토큰입니다. 자금은 언제든지 Blockchain Bitcoin으로 반환할 수 있습니다.



![image](assets/fr/17.webp)






- (1) **페그인**: 비트코인(BTC)은 Liquid 연합에 의해 메인 Blockchain에 고정됩니다. 그 대가로 두 체인 간의 패리티를 보장하는 동등한 양의 Liquid-비트코인(L-BTC)이 Blockchain Liquid에서 발행되어 사용자에게 전송됩니다.





- (2) **독립 트랜잭션**: 트랜잭션은 사용자 요구사항에 따라 메인 Blockchain(BTC)과 Sidechain Liquid(L-BTC)에서 동시에 독립적으로 실행할 수 있습니다.





- (3) **페그아웃**: 사용자가 Liquid-비트코인(L-BTC)을 Liquid 연합으로 다시 전송합니다. 그러면 연합은 메인 Blockchain에서 동일한 양의 비트코인(BTC)을 잠금 해제하고 이를 사용자에게 전송합니다.



Liquid은 블록 검증과 양방향 앵커링을 관리하는 신뢰할 수 있는 참여자(거래소, 공인된 Bitcoin 회사)로 구성된 **연합**에 의존합니다. 탈중앙화되어 채굴자에게 의존하는 Blockchain Bitcoin과 달리 Liquid은 **연합** 네트워크이므로 보안과 거버넌스가 이러한 참여자에게 의존합니다. 이는 탈중앙화에 대한 타협을 의미하지만, 최적화된 성능과 고급 기능을 가능하게 합니다.



![image](assets/fr/18.webp)



##### 왜 Liquid을 사용하나요?





- 속도**: 검증자 연합이 매분 생성하는 블록 덕분에 온체인 거래의 경우 10분 이상 걸리는 것에 비해 Liquid의 거래는 약 **1분** 만에 확정됩니다.
- 강화된 기밀성**: Liquid은 **Confidential Transactions**을 사용하여 전송된 자산의 금액과 유형을 숨겨 거래를 더욱 비공개로 처리합니다(주소는 계속 표시되지만).
- 낮은 수수료**: Liquid를 통한 거래는 일반적으로 수수료가 저렴하여 자주 송금하거나 소액을 송금할 때 이상적입니다.
- 다중 자산**: Liquid은 L-BTC 외에도 특정 애플리케이션에서 사용하기 위해 스테이블코인이나 토큰과 같은 다른 디지털 자산의 발행을 지원합니다.
- 사용 사례**: Liquid는 특히 크로스 플랫폼 거래소, 빠른 결제 또는 스마트 컨트랙트가 필요한 애플리케이션에 적합하며, Bitcoin의 보안과 연결되어 있습니다.



**참고: 이 튜토리얼은 블록스트림 앱을 통한 Liquid 사용에 중점을 두고 있습니다. Liquid Network에 대한 자세한 내용은 부록에서 리소스를 확인할 수 있습니다**



### 1.4. Hot Wallet 알림





- Hot Wallet**, **Software Wallet**, **Wallet 모바일**, **Software Wallet**: 스마트폰, 컴퓨터 또는 인터넷에 연결된 모든 장치에 설치된 애플리케이션의 모든 이름으로, Bitcoin Wallet의 개인키를 관리하고 보호할 수 있습니다.
- 키를 오프라인에서 격리하는 **하드웨어 지갑**, 일명 **Cold 지갑**과 달리 소프트웨어 지갑은 연결된 환경에서 작동하기 때문에 사이버 공격에 더 취약합니다.





- 권장 사용**:
    - 특히 일일 거래의 경우 적당한 양의 Bitcoin를 관리하는 데 이상적입니다.
    - Hardware Wallet이 불필요하게 느껴질 수 있는 초보자나 자산이 제한적인 사용자에게 적합합니다.





- 제한 사항**: 거액의 자금이나 장기 저축을 보관하기에는 안전성이 떨어집니다. 이 경우 Hardware Wallet을 선택하세요.




## 2. 블록스트림 앱 소개





- 블록스트림 앱**은 Bitcoin의 지갑과 자산을 관리하기 위한 모바일(iOS, 안드로이드) 및 데스크톱 애플리케이션입니다. 2016년에 [블록스트림](https://blockstream.com/)이 인수했으며, 이전에는 *Green Address*, 이후 *Blockstream Green*로 명명되었습니다.
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





## 4. Bitcoin 온체인 포트폴리오 만들기



### 4.1. 생성 시작





- 주의**: 카메라나 참관인이 없는 비공개 환경에서 포트폴리오를 설정하세요.
- 홈 화면에서 "시작하기" 를 클릭합니다:



![image](assets/fr/04.webp)





- Cold Wallet**(오프라인 Wallet)을 관리하려는 경우: **"Jade 연결"**을 클릭하여 Hardware Wallet 블록스트림 제이드 또는 기타 호환되는 Cold 지갑을 사용하세요.



![image](assets/fr/05.webp)






- 다음 화면이 나타납니다:



![image](assets/fr/06.webp)






- (1) **"모바일 Wallet 설정"** : 새 Hot Wallet를 생성합니다(Hot Wallet).
- (2) **"백업에서 복원"**: Mnemonic 구문(12단어 또는 24단어)을 사용하여 기존 포트폴리오를 가져옵니다. 경고: 이 문구는 연결된 장치에 노출되어 보안이 무효화되므로 Cold Wallet에서 가져오지 마세요.
- (3) **"보기 전용"**: 기존 읽기 전용 포트폴리오를 가져와서 Mnemonic 문구를 노출하지 않고 잔고(예: Cold Wallet)를 볼 수 있습니다. 부록의 '보기 전용' 튜토리얼을 참조하세요.



**이 튜토리얼에서는**: "모바일 Wallet 설정"**을 클릭하여 Hot Wallet을 생성합니다.


Wallet가 자동으로 생성되고 "My Wallet 5"라는 Wallet 홈 페이지가 표시됩니다:



![image](assets/fr/07.webp)



**중요**: 블록스트림 앱은 12단어 seed 문구를 자동으로 표시하지 않음으로써 Wallet 생성을 간소화했습니다. *이제 한 번의 클릭으로 포트폴리오가 생성되더라도 seed 문구*를 저장하지 않으면 자금에 대한 액세스 권한을 잃을 위험이 있습니다.



### 4.2. seed 문구 저장





- Wallet 홈 화면에서 '보안' 탭을 클릭한 다음 '백업' 프롬프트 또는 '복구 문구' 메뉴를 클릭합니다:



![image](assets/fr/08.webp)



저장할 수 있도록 seed 12단어 문구가 표시됩니다.





- 복구 문구를 최대한 주의해서 적으세요. 종이나 금속에 적어 안전한 장소(안전한 오프라인 장소)에 보관하세요. 이 문구는 장치를 분실하거나 애플리케이션이 삭제된 경우 비트코인에 액세스할 수 있는 유일한 수단입니다.
- 이 문구를 가진 사람은 누구나 여러분의 모든 비트코인을 훔칠 수 있다는 점에 유의하세요. 절대로 디지털 방식으로 보관하지 마세요:
 - 스크린샷 없음
 - 클라우드, 이메일 또는 메시징 백업 없음
 - 복사/붙여넣기 없음(클립보드에 저장할 위험)



**! 이 점이 중요합니다**. 백업에 대한 자세한 내용은 백업 :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. seed 문장 확인



이 Address 문구와 연결된 seed으로 자금을 보내기 전에 12개 단어의 백업을 테스트해야 합니다.


이를 위해 참조를 기록하고, Wallet를 삭제한 다음 백업으로 복원하고 참조가 변경되지 않았는지 확인합니다.





- Wallet 홈 화면에서 "설정" 탭을 클릭한 다음 "Wallet 세부 정보"를 클릭하고 zPub([확장 공개 키](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)를 복사합니다:



![image](assets/fr/09.webp)



참고: '보기 전용' 기능을 위해 zpub Address을 블록스트림 애플리케이션으로 가져올 수 있습니다(부록 참조).





- 애플리케이션을 삭제한 다음 **"백업에서 복원"**을 통해 Mnemonic 문구를 입력하여 Wallet을 복원하고 zpub이 변경되지 않았는지 확인합니다. 그렇다면 백업이 올바른 것이므로 Wallet로 자금을 송금할 수 있습니다.





- 복구 테스트를 수행하는 방법에 대해 자세히 알아보려면 전용 튜토리얼 을 참조하세요:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. 애플리케이션에 대한 액세스 보안



강력한 PIN 코드로 애플리케이션에 대한 액세스를 잠급니다:




- Wallet 홈 화면에서 **"보안"**으로 이동한 다음 **"비밀번호"**를 클릭합니다
- 임의의 6자리 PIN 코드**를 입력하고 확인합니다.



**생체 인식 옵션**: 편의성을 높이기 위해 사용할 수 있지만 강력한 PIN 코드보다 보안성이 떨어집니다(예: 수면 중 지문 또는 얼굴 스캔 등 무단 액세스 위험).



**참고**: PIN은 기기를 보호하지만, 자금 회수에는 seed 문구만 사용할 수 있습니다.





## 5. Liquid Wallet 사용



### 5.1. "L-BTC" 비트코인 받기



Liquid-비트코인(L-BTC)을 받으려면 몇 가지 옵션을 사용할 수 있습니다. 아래에 자세히 설명되어 있는 Liquid를 받는 Address을 공유하여 다른 사람에게 직접 보내달라고 요청할 수 있습니다.



또는 [볼츠와 같은 브릿지](https://boltz.Exchange/)를 사용하여 온체인 또는 L-BTC용 Lightning Network를 통해 비트코인을 Exchange으로 보내세요: Address을 받는 Liquid을 입력하고 원하는 대로 결제한 후 L-BTC를 받습니다.





- 포트폴리오 홈 화면에서 '"**거래**"를 클릭한 다음 **"**받기"**를 클릭합니다.



![image](assets/fr/19.webp)





- 기본적으로 애플리케이션은 빈 **영수증 Address, 온체인**(`bc1q...`로 시작하는 SegWit v0 형식)을 표시합니다. "Bitcoin"을 클릭하여 **Liquid Bitcoin**을 선택합니다:



![image](assets/fr/20.webp)





- 옵션**:
 - (1) 화살표를 클릭하여 이 Address 문장에 연결된 다른 새 seed 문장을 선택합니다.
    - (2) 오른쪽 상단의 점 세 개를 클릭한 다음 "주소 목록"을 클릭하여 이미 사용/표시된 Address 중에서 선택할 수도 있습니다
    - (3) 특정 금액을 요청하려면 오른쪽 상단의 점 3개를 클릭하고 '요청 금액'을 선택한 후 원하는 금액을 입력합니다. QR이 업데이트되고 Address이 Bitcoin 결제 URI로 대체됩니다.



![image](assets/fr/21.webp)





- "**공유**"를 클릭하거나 텍스트를 복사하거나 QR 코드를 스캔하여 Address/URI를 공유하세요.
- 확인**: 오류나 공격(예: 클립보드를 수정하는 멀웨어)을 방지하기 위해 수신자와 공유한 Address를 최대한 확인합니다.



### 5.2. 비트코인 보내기





- 포트폴리오 홈 화면에서 "**거래**"를 클릭한 다음 **"보내기"**를 클릭합니다:



![image](assets/fr/22.webp)





- 세부 정보를 입력합니다:
    - (1) 수신자의 **Address**을 붙이거나 QR 코드를 스캔하여 입력합니다.
    - (2) 송금하는 자산과 송금하는 계좌를 확인합니다.
    - (3) 송금할 **금액**을 입력합니다. 단위를 선택할 수 있습니다: L-BTC, L-사토시, USD, ...



![image](assets/fr/23.webp)





- 확인**:
    - 요약 화면에서 Address, 금액 및 요금을 확인합니다.
    - Address 오류는 돌이킬 수 없는 자금 손실을 초래할 수 있습니다. 클립보드를 수정하는 멀웨어에 주의하세요.



![image](assets/fr/24.webp)





- 확인**: '보내기' 버튼을 밀어 트랜잭션에 서명하고 배포합니다.
- 후속 조치**: Wallet "거래" 탭에서 거래가 "미확인됨", "확인됨", "완료됨"으로 표시됩니다:



![image](assets/fr/25.webp)





- Liquid에서는 2블록 사이의 시간이 1분이므로 거래가 빠르게 확인되고 완료됩니다.




## 부록



### A1. 기타 블록스트림 앱 튜토리얼



온체인 네트워크 사용



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

"보기 전용" 모드에서 Wallet 가져오기 및 추적하기



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

데스크톱 버전



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. 모범 사례



블록스트림 앱**을 안전하고 효율적으로 사용하려면 다음 권장 사항을 따르세요. 이는 **Bitcoin (온체인)**, **Liquid** 및 **라이트닝** 네트워크에서 자금을 보호하고, 거래를 최적화하며, 기밀을 유지하는 데 도움이 될 것입니다.





- 복구 문구**를 보호하세요:
 - 튜토리얼: Mnemonic 구문 저장하기



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 보안 인증**을 사용합니다:
 - 애플리케이션에 대한 액세스를 보호하려면 **강력한 PIN** 또는 **생체인증**(지문 또는 얼굴 인식)을 활성화하세요.
 - PIN 또는 생체 인식 데이터를 공유하지 마세요.





- 개인 정보 보호**:
 - generate은 각 온체인 수신에 대한 새로운 Address 또는 Liquid를 사용하여 Blockchain에서 추적을 제한합니다.
 - "강화된 개인정보 보호", "토르" 및 "SPV" 기능을 활성화합니다.
 - 기밀성을 극대화하려면 퍼블릭 노드를 사용하는 대신 Electrum 서버를 통해 Wallet를 자체 Bitcoin 노드에 연결하세요





- 필요에 가장 적합한 네트워크를 선택하세요**:
- 온체인**: 장기 보관 또는 고액 거래에 선호됩니다(금액 대비 수수료가 무시할 수 있는 수준).
- Liquid**: 기밀성이 강화된 빠르고 저렴한 전송에 사용하세요.
- Lightning**: 소액 송금 시 저렴한 비용으로 즉시 송금할 수 있습니다.





- 항상 배송지 주소를 확인하세요**:
 - 송금하기 전에 Address을 주의 깊게 확인하세요. 잘못된 Address으로 송금한 자금은 영원히 손실됩니다. Address을 손으로 복사/수정하지 말고 복사/붙여넣기 또는 QR코드 스캔을 사용하세요.





- 비용 최적화**:
 - 온체인 트랜잭션의 경우 긴급성과 네트워크 혼잡도에 따라 적절한 수수료(느린, 중간, 빠른)를 선택하세요.
 - 소량의 경우 Liquid 또는 Lightning을 사용하세요.





- 애플리케이션을 최신 상태로 유지




### A3. 추가 리소스





- 공식 링크:**
- [공식 웹사이트](https://blockstream.com/)
- [모바일 애플리케이션 지원](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): 문서 및 채팅
- [깃허브](https://github.com/Blockstream/green_android)





- 블록 탐색기:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
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