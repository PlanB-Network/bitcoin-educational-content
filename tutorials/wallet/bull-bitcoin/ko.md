---
name: Bull Bitcoin Wallet
description: Wallet Bull Bitcoin 사용 방법 알아보기
---

![cover](assets/cover.webp)



이 가이드는 Bull Bitcoin 모바일의 설치, 구성 및 사용 방법을 안내합니다. 온체인, Liquid, 라이트닝의 세 가지 네트워크에서 자금을 받고 보내는 방법과 한 네트워크에서 다른 네트워크로 Bitcoin를 전송하는 방법을 배우게 됩니다. 부록에서는 리소스 및 연락처, 배경 정보, 기술 개념에 대한 간략한 설명을 제공합니다.



## 소개



**Bull Bitcoin](https://www.bullbitcoin.com/)**([계정 만들기](https://app.bullbitcoin.com/registration/orangepeel)에서 개발한 **Bull Bitcoin Mobile**은 **자가 보관** Bitcoin Wallet으로, 제3자에 의존하지 않고 개인 키와 자금을 완전히 제어할 수 있습니다. 오픈 소스이며 Cypherpunk 철학에 뿌리를 둔 이 Wallet은 단순성, 기밀성, 네트워크 간 스왑 및 PayJoin 지원과 같은 고급 기능을 결합한 제품입니다. 세 가지 네트워크에서 비트코인을 관리할 수 있습니다: **Bitcoin 온체인**, **Liquid**, **라이트닝**으로, 각각 특정 용도에 맞게 조정됩니다.



### 개발 컨텍스트



Wallet는 주요 과제에 대응합니다: Bitcoin 네트워크 요금은 소액 결제나 소규모 자체 호스팅 라이트닝 채널 개설에 적합하지 않습니다. Wallet Bull Bitcoin Mobile은 3대 Bitcoin 네트워크에 의존하면서 자체 관리 솔루션을 제공합니다:





- Bitcoin 네트워크(온체인)**: 수수료가 비례적으로 무시할 수 있는 UTXO의 중장기 보관 및 고액 거래에 이상적입니다.
- Liquid Network**: 빠르고(최대 2분), 기밀이 유지되며(숨겨진 금액), 저렴한 비용으로 거래할 수 있도록 설계되어 소액을 모으거나 개인 정보를 보호하는 데 적합합니다.
- Lightning Network**: 즉시 저비용 결제에 최적화되어 있으며, 일일 중소규모 거래에 적합합니다.



예를 들어, Bull Bitcoin 모바일을 사용하면 **Liquid** 또는 **라이트닝** 포트폴리오에 소량을 적립한 다음 상당한 금액에 도달하면 :





- 안전한 중장기 저장을 위해 온체인 네트워크로 전송하고, Liquid 및/또는 라이트닝 업스트림으로 기밀성이 향상되며, 단일 거래에 대한 온체인 수수료가 부과됩니다



### 지속적인 진화



Wallet는 지속적으로 발전하고 있으므로 이 튜토리얼과 최신 애플리케이션 사이에 불일치가 발견되더라도 놀라지 마세요.




- 예를 들어, 2025년 7월 19일 현재 **"구매/판매/결제"** 버튼은 애플리케이션에 표시되지만 회색으로 표시되어 있는데, 이는 Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel)에서 사용할 수 있는 이러한 옵션이 곧 통합된 환경을 위해 통합될 예정이기 때문입니다. 이 옵션은 전적으로 선택 사항으로 남아있을 것입니다. 그 외에도 멀티 Wallet 관리, passphrase, 하드웨어 지갑과의 호환성 등 많은 개발이 진행 중이거나 계획 중입니다...
- 불비트코인 깃허브](https://github.com/orgs/SatoshiPortal/projects/49)에서 현재 주제와 예정된 개발 사항을 확인할 수 있습니다. 이 프로젝트는 100% 오픈소스이며 "공개적으로 구축된" 프로젝트이므로, 여러분의 제안과 발견한 버그를 보내주실 수도 있습니다.




## 1. 전제 조건



Bull Bitcoin Mobile**을 사용하기 전에 다음 항목이 준비되어 있는지 확인하세요:





- 호환 가능한 스마트폰**: IOS**(아이폰 또는 아이패드) 또는 **안드로이드** 기기
- 인터넷 연결
- 백업 미디어를 안전하게 보관하세요**: 종이나 금속에 **복구 문구**(12단어)를 적어 안전한 곳에 보관하세요.
- 기본 지식**: 이 튜토리얼에서는 초보자를 위해 각 단계를 설명하지만, Bitcoin 개념(주소, 거래, 수수료)에 대한 최소한의 이해가 있으면 유용합니다.



## 2. 설치





- 애플리케이션을 다운로드하세요:
- [구글 플레이 스토어](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **안드로이드 기기용 애플리케이션 스토어에서 다운로드**
- [깃허브](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **안드로이드 기기용 APK 직접 다운로드**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) **애플 기기의 경우 테스트플라이트**를 통해 다운로드하세요
 - 사기성 애플리케이션을 피하려면 개발자 이름(Bull Bitcoin)을 확인하세요.
 - 다운로드한 버전이 GitHub에 표시된 최신 안정 버전과 일치하는지 확인합니다.
 - Bull Bitcoin 모바일은 **오픈 소스**입니다. 코드를 보려면: [불비트코인 깃허브](https://github.com/orgs/SatoshiPortal/projects/49)





- 애플리케이션 설치




## 3. 초기 구성



### 3.1 애플리케이션을 실행합니다 :



이 애플리케이션은 두 포트폴리오 모두에 고유한 12단어 복구 문구를 사용합니다:




- 보안 Bitcoin Wallet**: Bitcoin 네트워크(온체인) 트랜잭션의 경우
- 즉시 결제의 Wallet**: Liquid 및 라이트닝 네트워크의 인스턴트 거래용



열면 기존 복구 구문을 가져오거나 새 Wallet 을 만들라는 메시지가 표시됩니다:



![image](assets/fr/02.webp)



### 3.2 복구 문구 :



기존 Wallet를 재사용하려면 "**Wallet 복구**"를 클릭하고 복구 문구 12단어를 입력하세요.



그렇지 않으면 "**새 Wallet 만들기**"를 클릭합니다:




- 복구 문구를 최대한 주의해서 적으세요. 종이나 금속에 적어 안전한 장소(안전 금고, 오프라인 장소)에 보관하세요. 이 문구는 장치를 분실하거나 애플리케이션이 삭제된 경우 비트코인에 액세스할 수 있는 유일한 수단입니다.
- 이 문구를 가진 사람은 누구나 여러분의 모든 비트코인을 훔칠 수 있다는 점에 유의하세요. 절대로 디지털 방식으로 보관하지 마세요:
 - 스크린샷 없음
 - 클라우드, 이메일 또는 메시징 백업 없음
 - 복사/붙여넣기 없음(클립보드에 저장할 위험)



**! 이 점이 중요합니다**. 추가 지원을 받으려면 :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 액세스 보안 :





- 설정으로 이동한 다음 **PIN 코드**를 클릭합니다.
- 애플리케이션에 대한 액세스를 보호하기 위해 강력한 **PIN 코드**를 설정하세요.
- 이 단계는 선택 사항이지만 휴대폰에 액세스할 수 있는 사람이 Wallet에 액세스하는 것을 방지하기 위해 강력히 권장합니다.



![image](assets/fr/03.webp)



### 3.4 개인 노드에 연결(선택 사항):



Wallet 불비트코인은 기본적으로 일렉트럼 서버에 연결되는데, 첫 번째는 Bull Bitcoin에서 관리하는 서버이고 두 번째는 블록스트림의 보조 서버로 로그를 보관하지 않아 추적의 위험을 줄여줍니다.



기밀성을 높이려면 일렉트럼 서버를 통해 애플리케이션을 자체 Bitcoin 노드에 연결할 수 있습니다(지침은 [BullBitcoin의 GitHub](https://github.com/orgs/SatoshiPortal/projects/49)에서 확인할 수 있습니다).




## 4. 자금 수령



를 사용하든 **Bull Bitcoin 모바일**로 자금을 받는 것은 간단하고 필요에 맞게 조정할 수 있습니다:




  - 장기 보존을 위한 **Bitcoin (온체인)** 네트워크를 구축했습니다,
  - gW-41** 네트워크는 더 빠르고 더 많은 Confidential Transactions을 지원합니다,
  - 라이트닝** 네트워크를 통해 저렴한 비용으로 즉시 결제할 수 있습니다.



애플리케이션은 선택한 네트워크에 따라 자동으로 라이트닝 수신 또는 Invoice 주소를 생성합니다. 각 네트워크에 대한 진행 방법은 다음과 같습니다.



### 4.1. 온체인(Bitcoin 네트워크)



홈 화면에서 :




- 를 클릭하거나 **보안 Bitcoin Wallet**를 선택한 다음 "**받기"**를 클릭합니다:



![image](assets/fr/04.webp)





- 를 클릭하거나 "**수신"**을 클릭한 다음 **Bitcoin** 네트워크를 선택합니다:



![image](assets/fr/05.webp)



#### 4.1.1. Address만 복사 또는 스캔" 옵션 비활성화(기본값)



![image](assets/fr/06.webp)





- 이를 통해 고급 매개변수(선택 사항)에 액세스할 수 있습니다. 를 지정할 수 있습니다:
 - BTC, Sats 또는 법정화폐로 **금액**을 입력합니다.
 - URI/QR 코드 사본에 포함할 **개인 메모**를 입력합니다.
 - 발신자와 수신자 항목을 결합하여 기밀성을 향상시키는 **PayJoin**(자세한 내용은 부록 3 참조)를 활성화합니다.





- 자동으로 생성된 URI의 예입니다:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- 사용법**: 발신자와 공유할 URI를 복사하거나 발신자가 QR 코드를 스캔하도록 합니다.



#### 4.1.2. Address만 복사 또는 스캔" 옵션 활성화됨



![image](assets/fr/07.webp)





- "Address만 복사 또는 스캔"** 옵션을 활성화하면 애플리케이션이 Bitcoin(bech32) 형식의 간단한 SegWit Address을 생성합니다.





- 예시:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



금액이나 메모를 입력하더라도 QR코드나 Address 사본에는 포함되지 않습니다





- 사용법**: Address를 복사하여 발신자와 공유하거나 발신자가 QR 코드를 스캔하도록 합니다.



#### 4.1.3. 새 Address 생성





- 왜 각 거래마다 새로운 Address을 사용하나요? 이렇게 하면 여러 결제가 동일한 Address에 연결되는 것을 방지하여 **개인 정보를 보호**하고 Blockchain의 추적 가능성을 제한할 수 있습니다.
- 기본적으로 Bull Bitcoin은 사용하지 않는 Address를 자동으로 생성합니다.
 - 화면 하단의 **"새 Address"**을 클릭하여 새 Address을 강제로 생성할 수 있습니다.
 - 사용하는 주소 수에 관계없이 포트폴리오에 하나의 잔액이 표시되며, 배송이 이루어지면 자동으로 자금을 통합할 수 있습니다.





- 팁: 특별히 필요한 경우(예: 기부를 받기 위한 공개 Address)가 아니라면 항상 Bull Bitcoin에서 제공하는 새 Address을 사용하세요.



### 4.2. Liquid



홈 화면에서 :




- 또는 **즉시 결제 Wallet**을 선택한 다음 **"받기"**를 클릭한 다음 **"Liquid"**을 클릭합니다:



![image](assets/fr/08.webp)





- 를 클릭하거나 "**수신"**을 클릭한 다음 **Liquid** 네트워크를 선택합니다:



![image](assets/fr/09.webp)



"수신"** 화면이 나타나면 Liquid Address를 복사합니다:





- 금액 또는 메모 없음. 예:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- 또는 **금액**(BTC, Sats 또는 법정화폐) 및/또는 **개인 메모**를 지정하여 URI/QR 코드 사본에 포함할 수 있습니다. 예시:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**사용**: Address/URI를 복사하여 발신자와 공유하거나 발신자가 QR 코드를 스캔하도록 합니다.



### 4.3. 번개



홈 화면에서 :




- 를 클릭하거나 **즉시 결제 Wallet**을 선택한 다음 "**받기"**를 클릭합니다:



![image](assets/fr/10.webp)





- 를 클릭하거나 "**수신"**을 클릭한 다음 **라이트닝** 네트워크를 선택합니다:



![image](assets/fr/11.webp)



#### 4.3.1. 운영, 제한 및 혜택





- 메커니즘**: Bull Bitcoin Wallet은 라이트닝을 통해 결제를 하고 받을 수 있는 Wallet입니다. 라이트닝을 통해 받은 자금은 **볼츠**를 통한 자동 스왑 덕분에 **Liquid** 네트워크(Wallet 즉시 결제에)에 저장됩니다. 이를 통해 유동성 채널을 관리할 필요 없이 라이트닝과 상호 작용할 수 있으며, 자체 수탁을 유지할 수 있습니다.





- 제한 사항:**
- 최소 **100 사토시**(2025년 7월 19일 기준)는 generate을 Invoice로 변경할 때 필요합니다.
- 발신자만 송금 금액에 추가로 송금 비용을 지불하는 Wallet 라이트닝 네이티브로 받는 것과는 달리 발신자가 보낸 금액에서 공제되는 비용을 지불합니다. 19/07/2025 기준, 송금액에서 47 Sats이 차감됩니다.





- 혜택**:
- 자기 보관**: 귀하의 자금은 Liquid Network에 저장되어 귀하가 계속 관리할 수 있습니다.
- 높은 온체인 수수료 없음**: Liquid에 저장하면 라이트닝 채널을 열거나 유동성을 추가하기 위해 값비싼 온체인 예치금을 지불하지 않아도 됩니다. 이러한 작업은 나중에 Liquid에 축적된 금액이 수수료를 정당화할 수 있을 때 수행할 수 있습니다.





- 팁: ** 발신자가 Wallet Bull Bitcoin를 가지고 있는 경우, 스왑 수수료를 피하려면 Liquid Network을 직접 사용하세요



#### 4.3.2. generate Invoice





- 금액**(BTC, Sats 또는 법정화폐)을 입력합니다





- Invoice에 통합될 **개인 메모**를 추가합니다. 발신자가 Invoice를 결제하면 Wallet에도 거래 내역에 포함됩니다.





- Invoice 유효기간:** 라이트닝 Invoice은 **12시간** 동안 유효합니다. 이 시간이 지나면 만료되며 더 이상 결제할 수 없습니다. 새로운 Invoice을 생성해야 합니다.





- 사용법**: Invoice를 복사하여 발신자와 공유하거나 발신자가 QR 코드를 스캔하도록 합니다.




## 5. 자금 송금



### 5.1. 기본 원칙



홈페이지 또는 지갑에서 :



![image](assets/fr/12.webp)



을 클릭하여 보내기 화면에 액세스합니다:



![image](assets/fr/13.webp)



**Bull Bitcoin 모바일**은 입력(복사 또는 QR코드를 통해 스캔)한 Address 또는 Invoice를 기반으로 네트워크(Bitcoin, Liquid 또는 Lightning)를 자동으로 감지하여 간편하게 송금할 수 있습니다.



### 5.2. 온체인 전송(Bitcoin 네트워크)



#### 5.2.1. 보내기 화면



**액션**: Bitcoin 온체인 Address 입력 또는 스캔





- 금액이 정의되지 않은 경우 예를 들어 :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- 그런 다음 보내기 화면에서 선택할 수 있습니다:
 - BTC, Sat 또는 법정화폐로 금액 입력. 최소 금액: 22/07/2025에 546 사토시.
 - 거래를 식별하기 위한 선택적 메모입니다. 거래 세부 정보에서 본인만 볼 수 있습니다.



![image](assets/fr/14.webp)





- 금액이 이미 정의되어 있는 경우 예를 들어 :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



그러면 아래의 확인 화면으로 바로 이동합니다.



#### 5.2.2 확인 화면



시간을 내어 모든 매개변수, 특히 금액, 목적지 Address 및 수수료를 확인하세요.


그런 다음 매개변수를 조정할 수 있습니다:



![image](assets/fr/15.webp)




- 수수료**: 선택할 수 있습니다:
  - 거래의 체결 속도**와 관련 수수료가 추정됩니다
- 절대 수수료**(사토시 단위의 총 수수료) 또는 **상대 수수료**(바이트당 수수료) 모드의 수수료와 거래 속도가 추정됩니다





- 고급 설정**:





- Replace-by-fee (RBF)**: 기본적으로 활성화된 이 기능은 더 높은 수수료를 지불하여 트랜잭션 속도를 높여줍니다(자세한 내용은 부록 4 참조).





- UTXO** 수동 선택: 자금이 여러 개의 다른 Wallet 주소에 저장되어 있는 경우 자금을 송금할 주소를 선택할 수 있습니다. 왜 이렇게 해야 하나요? Bitcoin의 채택이 증가함에 따라 송금 수수료가 상승하고 있습니다. 적은 금액으로 여러 주소로 송금하는 것은 하나의 Address으로 송금하는 것보다 비용이 많이 들지만, 지금 하면 나중에 수수료가 더 높아질 때를 피할 수 있습니다. 이를 **UTXO 통합**이라고 합니다.



![image](assets/fr/16.webp)





- PayJoin**로 보내기: URI를 제공한 수신자가 기능을 활성화한 경우(예: :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



그러면 Bull Bitcoin Mobile이 사용자의 UTXO와 수신자의 UTXO를 입력으로 결합하여 전송을 구성하여 기밀성을 향상시킵니다(자세한 내용은 부록 3 참조).



### 5.3. Liquid로 보내기



#### 5.3.1 보내기 화면



Liquid** 네트워크는 온체인 네트워크보다 빠른 거래(분당 한 블록으로 최대 2분)와 더 많은 기밀성(마스크된 금액), 매우 낮은 수수료를 제공합니다. 자금은 **즉시 결제 Wallet**에서 인출됩니다.



**액션**: Liquid 입력 또는 스캔 Address





- 금액이 정의되지 않은 경우 예를 들어 :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



그런 다음 보내기 화면에서 선택할 수 있습니다:




- BTC, 위성 또는 법정 화폐로 표시된 금액. 최소 금액은 없으며, 1Satoshi까지 가능합니다;
- 거래를 식별하기 위한 선택적 메모입니다. 거래 세부 정보에서 본인만 볼 수 있습니다.



![image](assets/fr/17.webp)





- 금액이 이미 정의되어 있는 경우 예를 들어 :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



그러면 아래의 확인 화면으로 바로 이동합니다.



#### 5.3.2 확인 화면



시간을 내어 모든 매개변수, 특히 금액과 목적지 Address를 확인하세요.



![image](assets/fr/18.webp)





- 수수료**: 거래의 복잡성에 비례하며, 일반적으로 0.1 sat/vB 기준, 즉 간단한 거래의 경우 20-40 satoshis (33 Sats, 07/22/2025)입니다.



### 5.4. 라이트닝으로 보내기



#### 5.4.1 보내기 화면



라이트닝** 네트워크는 소액을 즉시 저렴한 비용으로 결제할 수 있어 일일 소액 거래에 이상적입니다.



**액션**: 라이트닝 Invoice을 입력하거나 스캔합니다





- 금액을 설정할 수 있는 LN-URL Address을 스캔하는 경우


예: `orangepeel@walletofsatoshi.com`.


을 클릭한 다음 보내기 화면에서 선택할 수 있습니다:




 - BTC, 사토시 또는 법정화폐로 금액. 23/07/2025 최소 금액 1000 사토시
 - 거래를 식별하기 위한 선택적 메모입니다. 수신자에게 전송됩니다.



![image](assets/fr/19.webp)





- 정의된 양이 포함된 Lightning Invoice을 스캔하는 경우


예시:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



그러면 아래의 확인 화면으로 바로 이동합니다.



참고: 금액은 21/2025/07/23에 21Sats보다 커야 합니다



#### 5.4.2 운영, 제한 및 혜택





- 메커니즘**: 자금은 **즉시 결제 Wallet**(Liquid)에서 인출되고 **볼츠**와 **Liquid → 라이트닝** 스왑을 통해 전환됩니다.





- 제한 사항:**
- Wallet 라이트닝 네이티브보다 **높은 최소 금액**(위 참조)
- 비용** + Liquid → 볼츠를 통한 라이트닝 스왑





- 혜택**:
- 자기 보관**: 귀하의 자금은 귀하가 계속 관리하고 Liquid Network에 보관하며, 필요한 경우 Lightning을 통해 이체할 수 있습니다
- 높은 온체인 수수료 없음**: Liquid에 저장하면 라이트닝 채널을 열거나 유동성을 추가하는 데 비용이 많이 드는 온체인 예치금을 절약할 수 있습니다. 이러한 작업은 나중에 Liquid에 축적된 금액이 수수료를 감당할 수 있을 때 수행할 수 있습니다.





- 팁:** 수신자가 Wallet Bull Bitcoin를 가지고 있는 경우, 스왑 비용을 피하기 위해 Liquid Network을 직접 사용하세요



#### 5.3.3 확인 화면



시간을 내어 모든 매개변수, 특히 금액과 목적지 Address을 확인하세요.



![image](assets/fr/20.webp)




## 6. 기록 보기



**Bull Bitcoin 모바일**을 사용하면 **Bitcoin (온체인)**, **Liquid**, **라이트닝** 네트워크에서 거래를 쉽게 추적할 수 있습니다. 거래 내역은 두 가지 방법으로 액세스할 수 있으며, 각 거래 유형에 대한 자세한 정보를 표시합니다. 외부 블록 브라우저를 사용하여 트랜잭션을 확인할 수도 있습니다.



### 6.1. 액세스 기록





- 홈 화면을 통해**:**
 - 온체인** 거래를 보려면 **보안 Bitcoin Wallet**을 클릭하고, **Liquid** 및 **라이트닝** 거래를 보려면 **즉시 결제 Wallet**을 클릭합니다.
 - 내역은 포트폴리오 합계 바로 아래에 표시되며, 선택한 Wallet의 유형에 따라 필터링됩니다.



![image](assets/fr/21.webp)





- 전용 페이지를 통해**:**
 - 홈 화면에서 **기록 기호**(시계 아이콘 또는 이와 유사한 아이콘)를 클릭합니다.
 - 작업 유형별 필터를 사용해 모든 트랜잭션이 나열된 페이지에 액세스합니다: **보내기**, **받기**, **스왑**, **PayJoin**, **판매**, **구매** (참고: 판매와 구매는 개발 중이며 현재(2025년 7월 20일)는 사용할 수 없습니다).



![image](assets/fr/22.webp)



### 6.2. 거래 세부 정보



각 트랜잭션은 네트워크와 작업 유형(전송 또는 수신)에 따라 특정 정보를 표시합니다. 다음은 **온체인 트랜잭션**에 대해 확인할 수 있는 세부 정보입니다:



![image](assets/fr/23.webp)



### 6.3. Block explorer를 통한 확인



Bitcoin 온체인**, **Liquid** 및 **라이트닝** 네트워크의 탐색기 목록은 부록 4에 있습니다.



라이트닝**의 경우 공개 브라우저에서는 트랜잭션이 표시되지 않습니다. 애플리케이션에서 세부 정보(Boltz의 스왑 ID 포함)를 확인하세요.




## 7. 설정



"설정" 페이지는 Bull Bitcoin 애플리케이션 홈 페이지에서 직접 액세스할 수 있으며 포트폴리오 및 사용자 경험의 다양한 측면을 구성하고 관리하는 데 사용됩니다.



![image](assets/fr/24.webp)





- Wallet 백업**: 안전한 백업을 위한 포트폴리오의 복구 문구를 표시합니다. 복구 문구를 관리하고 저장하는 모범 사례는 포트폴리오 만들기의 3. 섹션을 참조하세요.





- Wallet 세부 정보**:
- Pubkey**: Wallet과 연결된 공개 키로, generate Bitcoin 수신 주소에 사용됩니다.
- 파생 경로**: 개인키에서 generate Wallet 주소로 유도하는 데 사용되는 유도 경로입니다.





- 일렉트럼 서버(Bitcoin 노드)**: 온체인 트랜잭션을 위해 사용자 정의된 Bitcoin 노드에 대한 연결을 설정합니다.





- PIN 코드**: 애플리케이션 및 Wallet 기능에 대한 액세스를 보호하기 위해 보안 코드를 활성화 및/또는 수정합니다.





- 통화**: 금액을 BTC 또는 Sats로 표시할지 여부와 기본 법정통화(달러, 유로 등)를 선택합니다.





- 자동 스왑 설정**: 자동 스왑_ 기능을 사용하면 거래 수수료가 정당하다고 판단되는 임계값에 도달하는 즉시 **즉시 결제 Wallet(Liquid)**에서 **Bitcoin On-Chain** Wallet으로 BTC를 자동으로 이체할 수 있습니다.





- 로그**: 보기 가능한 활동 로그로, 기술 지원팀과 공유하여 문제 해결을 용이하게 할 수 있습니다.





- 지원을 위한 텔레그램 액세스**: 사용자 지원을 위한 공식 텔레그램 채널로 직접 연결되는 링크입니다.





- Github 액세스**: 오픈 소스 코드를 보거나 문제를 신고하려면 [Bull Bitcoin Github 리포지토리](https://github.com/SatoshiPortal)로 이동하세요.




## 부록



### A1. PayJoin(P2EP)에 대한 설명



![image](assets/fr/25.webp)



**정의** :




- PayJoin 또는 P2EP(Pay-to-EndPoint)**는 **온체인** 네트워크에서 기밀성을 강화하는 Bitcoin 트랜잭션 기법입니다. 단일 트랜잭션에 발신자와 수신자 항목을 결합하여 금액과 주소 추적을 더욱 어렵게 만듭니다.



**운영:**




- PayJoin 트랜잭션에서 발신자와 수신자는 호환되는 PayJoin 서버를 통해 generate 공동 트랜잭션으로 함께 작업합니다.
- 발신자만 항목을 제공하는 대신(UTXO), 수신자도 자체 UTXO 중 하나로 기여합니다. 이렇게 하면 Blockchain에 표시되는 정보가 흐려집니다. 실제 금액에 해당하는 단일 항목 대신 두 개의 항목이 표시되고 출력에 교환된 금액이 직접 반영되지 않습니다.
- 최종 트랜잭션은 표준 Bitcoin 트랜잭션(다중 입력/다중 출력)과 비슷하지만, 스테가노그래피 구조 덕분에 실제 전송 금액과 주소 간 링크가 숨겨집니다.



*bull Bitcoin 모바일**에서 사용**




- 수신**(Address Supply): PayJoin은 기본적으로 활성화되어 있습니다.
- Send**: 예를 들어 Wallet은 PayJoin URI를 자동으로 감지하고 그에 따라 트랜잭션을 구성합니다:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**혜택**




- 강화된 기밀성**: PayJoin는 트랜잭션의 모든 항목이 단일 엔터티에 속한다는 가정을 무효화합니다. PayJoin에서는 발신자와 수신자 모두에서 입력이 이루어지므로 이 가정이 깨집니다.
- 금액 마스킹**: 실제 교환된 금액이 출력에 직접 나타나지 않습니다. 수취인의 UTXO 인바운드와 아웃바운드의 차이로 계산되므로 분석에 오해의 소지가 있습니다.



**한도**




- PayJoin는 발신자와 수신자가 호환되는 지갑을 사용해야 하며, 그렇지 않으면 표준 온체인 트랜잭션이 사용됩니다.
- 트랜잭션이 약간 더 복잡해지므로(입력과 출력이 더 많아짐) 비용이 약간 더 높아집니다.
- 표준 거래와 유사하게 설계되었지만, 고급 휴리스틱(예: 모호한 출력, 알려진 PayJoin 서버)으로 인해 절대적인 확신은 없지만 그 사용을 의심하게 될 수 있습니다.



**자세한 정보:**




- [용어집](https://planb.network/fr/resources/glossary/PayJoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Replace-by-fee(RBF)에 대한 설명



**정의**: Replace-by-fee(RBF)은 발신자가 더 높은 수수료를 지불하는 데 동의함으로써 **온체인** 트랜잭션의 확인을 가속화할 수 있는 Bitcoin 네트워크의 기능입니다.



**제한** :




- Liquid 또는 라이트닝 거래에는 RBF를 사용할 수 없습니다.
- 초기 트랜잭션은 생성 시 RBF 호환으로 표시되어야 하며, Bull Bitcoin Mobile은 비활성화하지 않는 한 자동으로 이를 수행합니다.



**자세한 정보:**




- [용어집](https://planb.network/fr/resources/glossary/RBF-replacebyfee)




### A3. 모범 사례



Bull Bitcoin 모바일**을 안전하고 효율적으로 사용하려면 다음 권장 사항을 따르세요. 이는 **Bitcoin (온체인)**, **Liquid**, **라이트닝** 네트워크에서 자금을 보호하고 거래를 최적화하며 기밀을 유지하는 데 도움이 될 것입니다.





- 복구 문구**를 보호하세요:
 - 튜토리얼: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/Wallet/backup/backup-Mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- 보안 인증**을 사용합니다:
 - 애플리케이션에 대한 액세스를 보호하려면 **강력한 PIN** 또는 **생체인증**(지문 또는 얼굴 인식)을 활성화하세요.
 - PIN 또는 생체 인식 데이터를 공유하지 마세요.





- 개인 정보 보호**:
 - generate은 각 온체인에 대한 새로운 Address 또는 Blockchain의 추적을 제한하기 위한 Liquid 수신입니다.
 - 온체인 전송 금액에 대한 기밀성을 높이려면 가능한 경우 PayJoin을 사용하세요
 - 기밀성을 극대화하려면 퍼블릭 노드를 사용하는 대신 Electrum 서버를 통해 Wallet을 자체 Bitcoin 노드에 연결하세요





- 필요에 가장 적합한 네트워크를 선택하세요**:
- 온체인**: 장기 보관 또는 고액 거래에 선호됩니다(금액 대비 수수료가 무시할 수 있는 수준).
- Liquid**: 기밀성이 강화된 빠르고 저렴한 전송에 사용하세요.
- Lightning**: 소액의 경우 즉시 저렴한 비용으로 이체할 수 있습니다. Wallet Bull Bitcoin 사용자 두 명인 경우, 볼츠를 통해 라이트닝 <> Liquid 스왑 수수료를 피하려면 Liquid을 선택하세요.





- 항상 배송지 주소를 확인하세요**:
 - 송금하기 전에 Address을 주의 깊게 확인하세요. 잘못된 Address으로 송금한 자금은 영원히 손실됩니다. 복사/붙여넣기 또는 QR코드 스캔을 사용하고, 절대로 손으로 Address을 복사/수정하지 마세요.





- 비용 최적화**:
 - 온체인 트랜잭션의 경우 긴급성과 네트워크 혼잡도에 따라 적절한 수수료(느린, 중간, 빠른)를 선택하세요.
 - 소량의 경우 Liquid 또는 Lightning을 사용하세요.
 - 확인 속도를 높여야 할 것으로 예상되는 경우 온체인 배송을 위해 Replace-by-fee(RBF)(부록 4 참조)를 활성화하세요.





- 애플리케이션을 최신 상태로 유지




### A4. 추가 리소스





- 공식 링크 및 지원:**
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : 지원 이메일
- [Bull Bitcoin 공식 웹사이트](https://bullbitcoin.com/): **Bull Bitcoin 서비스, 계정 생성, 애플리케이션 접속에 대한 정보**
- [깃허브 불 Bitcoin 모바일](https://github.com/SatoshiPortal/bullbitcoin-mobile): **코드, 진화 및 로드맵을 보고 개발에 기여하세요...**
- [계정 X - 트위터 불 Bitcoin](https://x.com/BullBitcoin_)
- Wallet 모바일용 텔레그램** 그룹: 지원팀과의 그룹 채팅은 "설정" 페이지를 참조하세요.





- 블록 탐색기:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[블록스트림 정보](https://blockstream.info/Liquid)**
 - 라이트닝: **[1ML (Lightning Network)](https://1ml.com/)**





- 학습 및 튜토리얼:** **[Plan ₿ Network](https://planb.network/)**
 - 복구 문구 보안



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
- [용어집](https://planb.network/resources/glossary/Liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network**:
- [용어집](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### 회사 개요



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**은 2013년 캐나다 몬트리올의 Bitcoin 대사관에서 설립된 가장 오래된 비예치형 Exchange 전용 플랫폼입니다. Bitcoin 생태계의 선구자로 인정받는 프란시스 풀리오가 이끄는 이 회사는 금융 주권과 사용자 자율성을 촉진하는 핵심 플레이어로 자리매김하고 있습니다. 이 회사의 사명은 개인이 Bitcoin을 자유와 지불을 위한 도구로 사용함으로써 자신의 돈에 대한 통제권을 되찾고, Bitcoin 이외의 법정화폐와 암호화폐를 거부할 수 있도록 하는 것입니다.



![image](assets/fr/26.webp)



[계정 만들기](https://app.bullbitcoin.com/registration/orangepeel)를 통해 Bitcoin 구매 및 판매 시 0.25% 할인을 받을 수 있습니다.



#### 가치와 철학



Bull Bitcoin는 Commitment~Cypherpunk 원칙과 Bitcoin 윤리가 돋보입니다:





- Bitcoin**에 독점적으로 집중합니다: 이 플랫폼은 탈중앙화되고 검열에 강한 화폐라는 비전에 충실합니다.





- 비수탁자**: 사용자는 자신의 포트폴리오로 자금을 송금하여 비트코인을 완전히 제어할 수 있습니다.





- 기밀 유지**: 개인 데이터 수집 최소화, 999달러 미만의 거래에 대해 KYC가 필요 없는 구매 옵션. 데이터는 규정(캐나다의 FINTRAC, 프랑스의 AMF)에 따라 보호됩니다.





- 투명성**: 숨겨진 수수료 없음, 스프레드(구매 가격과 판매 가격의 차이)에 비용이 포함되지 않습니다.





- 금융 주권**: Bull Bitcoin은 전통적인 은행 시스템과 중앙 집중식 기관으로부터의 독립을 촉진합니다.



#### 주요 서비스





- 법정화폐 입금**: 사용자는 일부 캐나다 우체국에서 은행 송금 또는 현금/직불카드를 통해 법정통화(CAD, EUR 등)로 Bull Bitcoin 계정에 입금할 수 있습니다.





- Bitcoin** 구매하기: 사용자는 비예탁 포트폴리오로 직접 전송되는 Bitcoin를 구매하여 자금에 대한 완전한 통제권을 보장받을 수 있습니다.





- 예약된 Bitcoin 구매**: Bull Bitcoin은 사용자가 제어하는 Wallet로 비트코인을 직접 이체하여 가격 변동성의 영향을 줄이는 자동 반복 구매 서비스(DCA - 달러 비용 평균화)를 일정 간격으로 제공하여 사용 가능한 잔액을 활용합니다.



"자동 구매"라는 옵션을 사용하면 Bull Bitcoin 잔액에 닿는 즉시 비트코인을 전환하고 자신의 Wallet으로 비트코인을 전송할 수 있습니다. 이 옵션은 은행에 예약된 정기 은행 이체와 결합하여 DCA를 만들 수도 있습니다. 이 옵션은 애플리케이션을 열지 않고도 Bitcoin를 자동으로 적립할 수 있습니다.






- 지정가 '지정가 주문'**으로 Bitcoin를 매수하세요: 사용자가 미리 지정한 가격으로 Bitcoin를 매수할 수 있으며, Bull Bitcoin 지수 가격이 설정한 한도에 도달하거나 그 이하로 떨어지면 자동으로 실행됩니다.





- Bitcoin** 판매하기: 사용자는 비트코인을 판매하고 은행 또는 SEPA 송금을 통해 은행 계좌로 직접 법정화폐로 자금을 받을 수 있습니다.





- 제3자 결제**: Bull Bitcoin을 사용하면 사용자가 비트코인에서 은행 계좌로 법정화폐를 수취인에게 완전히 투명하게 송금할 수 있습니다.





- Bull Bitcoin 프라임**: Bull Bitcoin Prime은 고액 자산가 및 기업 고객을 위한 프리미엄 서비스로, 맞춤형 솔루션과 프리미엄 지원을 제공합니다. 여기에는 수수료 할인, 전담 계좌 매니저, 맞춤형 기업 서비스가 포함됩니다. 이 서비스는 심층적인 전문 지식과 우선적 대우를 원하는 기관, 전문 트레이더, 기업 고객을 대상으로 합니다.





- 모바일 Wallet**: Bull Bitcoin는 안드로이드와 iOS에서 사용할 수 있는 오픈소스 자체 관리형 모바일 Wallet을 제공하며, 온체인, Liquid 및 Lightning Network 트랜잭션을 지원합니다.





- 교육 지원**: 무료 가이드와 맞춤형 코칭을 통해 사용자가 Bitcoin 포트폴리오를 생성, 보호 및 관리하여 재정적 자율성을 강화할 수 있도록 지원합니다.



#### 규정 준수 및 안전





- 규제**: FINTRAC(캐나다) 및 AMF(프랑스)에 등록된 Bull Bitcoin은 KYC/AML 요건을 준수합니다.





- 보안**: 보안 포트폴리오 사용 및 오프라인 스토리지 권장 사항. 개인 데이터는 100% 자체 호스팅되며 타사에 의존하지 않는 Bull의 Bitcoin 인프라에서 호스팅됩니다.