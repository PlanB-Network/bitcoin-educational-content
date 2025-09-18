---
name: Payjoin - Samourai Wallet
description: 사무라이 PayJoin에서 Wallet 트랜잭션을 수행하는 방법은 무엇인가요?
---
![samourai payjoin cover](assets/cover.webp)


***주의:** 4월 24일 사무라이 Wallet의 설립자가 체포되고 서버가 압수됨에 따라, 사무라이 Wallet의 페이조인 스타우웨이는 두 사용자가 자신의 도장에 연결되어 있는 경우에만 관련 당사자 간에 수동으로 PSBT을 교환하는 방식으로만 작동합니다. Sparrow의 경우, BIP78을 통한 페이조인은 여전히 작동합니다. 그러나 이러한 도구는 몇 주 내에 다시 출시될 가능성이 있습니다. 그 동안에는 이 글을 읽고 Stowaway의 이론적 기능을 이해하실 수 있습니다*


수동으로 밀항을 하려는 경우, 절차는 이 튜토리얼에서 설명한 것과 매우 유사합니다. 가장 큰 차이점은 밀항 거래 유형 선택에 있습니다. '온라인'을 선택하는 대신 '직접/수동'을 클릭하세요. 그런 다음 밀항 거래를 구성하려면 PSBT를 수동으로 Exchange로 설정해야 합니다. 공동 작업자와 물리적으로 가까이 있는 경우 QR 코드를 연속으로 스캔할 수 있습니다. 멀리 떨어져 있는 경우에는 보안 통신 채널을 통해 JSON 파일을 교환할 수 있습니다. 튜토리얼의 나머지 부분은 변경되지 않습니다


저희는 이 사건의 전개 상황과 관련 도구의 개발 상황을 면밀히 주시하고 있습니다. 새로운 정보가 입수되는 대로 이 튜토리얼을 업데이트할 예정이니 안심하세요


이 튜토리얼은 교육 및 정보 제공 목적으로만 제공됩니다. 범죄 목적으로 이러한 도구를 사용하는 것을 보증하거나 권장하지 않습니다. 해당 관할 지역의 법률을 준수하는 것은 각 사용자의 책임입니다


---

> *Blockchain 스파이가 자신이 알고 있다고 생각하는 모든 것을 다시 생각하도록 강요합니다*

PayJoin은 결제 수취인과 협력하여 지출 중 사용자 개인정보 보호를 강화하는 특정 Bitcoin 거래 구조입니다. PayJoin의 설정과 자동화를 용이하게 하는 몇 가지 구현이 있습니다. 이러한 구현 중 가장 잘 알려진 것은 Samourai Wallet 팀에서 개발한 Stowaway입니다. 이 튜토리얼에서는 Samourai Wallet 애플리케이션을 사용하여 Stowaway PayJoin 거래를 수행하는 방법을 설명합니다.


## 스토와이는 어떻게 작동하나요?


앞서 언급했듯이 Samourai Wallet는 "Stowaway"라는 PayJoin 도구를 제공합니다 이 도구는 PC의 Sparrow wallet 소프트웨어 또는 Android의 Samourai Wallet 애플리케이션을 통해 액세스할 수 있습니다. PayJoin을 수행하려면 공동 작업자 역할을 하는 수신자가 Stowaway와 호환되는 소프트웨어, 즉 Sparrow 또는 Samourai를 사용해야 합니다. 이 두 소프트웨어는 상호 운용이 가능하므로 Sparrow wallet와 Samourai Wallet 간 또는 그 반대로 스토와웨이 거래를 할 수 있습니다.


밀항은 사무라이가 "카훗"이라고 부르는 거래 범주에 의존합니다 캐훗은 본질적으로 여러 사용자 간의 협업 트랜잭션으로, off-chain 정보 Exchange이 필요합니다. 현재 사무라이에서 제공하는 캐훗 도구는 두 가지입니다: 스타우어웨이(페이조인)와 스톤월X2(향후 글에서 살펴볼 예정)입니다.


카후트 거래는 사용자 간에 부분적으로 서명된 거래를 교환하는 과정을 거칩니다. 이 과정은 특히 원격으로 수행할 경우 시간이 오래 걸리고 번거로울 수 있습니다. 하지만 다른 사용자와 함께 수동으로 수행할 수 있으므로 공동 작업자가 물리적으로 가까운 경우 편리할 수 있습니다. 실제로는 5개의 QR 코드를 수동으로 교환하여 연속적으로 스캔해야 합니다.


이 과정을 원격으로 수행하면 너무 복잡해집니다. 이 문제를 해결하기 위해 사무라이는 토르 기반의 암호화된 통신 프로토콜인 "소로반"을 개발했습니다 소로반을 사용하면 PayJoin에 필요한 교환이 사용자 친화적인 Interface 뒤에서 자동화됩니다. 이것이 이 글에서 살펴볼 두 번째 방법입니다.


이러한 암호화된 교환을 위해서는 카훗 참여자 간의 연결과 인증이 필요합니다. 따라서 소로반의 커뮤니케이션은 사용자의 Paynyms를 기반으로 합니다. 페이님에 대해 잘 모르신다면 이 글을 참고하여 자세한 내용을 확인하시기 바랍니다: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



간단히 말해, Paynym은 Wallet에 연결된 고유 식별자로, 암호화된 메시징을 비롯한 다양한 기능을 사용할 수 있습니다. Paynym은 식별자와 로봇을 나타내는 그림의 형태로 표시됩니다. 다음은 Testnet에 사용된 예시입니다: ![paynym 사무라이 Wallet](assets/en/1.webp)


**요약: **


- 페이조인_ = 협업 거래의 특정 구조입니다;
- _Stowaway_ = 사무라이 및 Sparrow wallet에서 PayJoin 구현 가능;
- 카후츠_ = 사무라이가 PayJoin 밀항을 포함한 모든 유형의 협력 거래에 부여한 이름입니다;
- _Soroban_ = 토르에서 설정된 암호화된 통신 프로토콜로, 카후츠 거래의 맥락에서 다른 사용자와 협업할 수 있습니다;
- 페이님_ = 카훗 거래를 수행하기 위해 소로반에서 다른 사용자와 통신할 수 있는 Wallet의 고유 식별자입니다.


[**-> PayJoin 트랜잭션과 그 유용성에 대해 자세히 알아보기**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Paynyms 간 연결은 어떻게 설정하나요?


사무라이를 통해 원격 카훗 거래, 특히 PayJoin(밀항)을 진행하려면 협력하려는 사용자를 페이님을 사용해 "팔로우"해야 합니다. 밀항자의 경우, 이는 비트코인을 보내고자 하는 사용자를 팔로우하는 것을 의미합니다.


**이 연결을 설정하는 절차는 다음과 같습니다


시작하려면 PayJoin에 대한 수신자의 Paynym 결제 코드를 받아야 합니다. 사무라이 Wallet 애플리케이션에서 수신자는 화면 왼쪽 상단에 있는 Paynym(작은 로봇)의 아이콘을 탭한 다음 `+...`로 시작하는 Paynym 닉네임을 클릭해야 합니다. 예를 들어, 제 닉네임은 `+namelessmode0aF`입니다. 공동 작업자가 Sparrow wallet을 사용하는 경우 여기를 클릭하여 전용 튜토리얼을 참조하시기 바랍니다.


![connexion paynym samourai](assets/notext/2.webp)


그러면 공동 작업자가 Paynym 페이지로 리디렉션됩니다. 여기에서 공동 작업자는 Paynym 자격 증명을 공유하거나 스캔할 수 있도록 QR 코드를 공유할 수 있습니다. 이렇게 하려면 화면 오른쪽 상단에 있는 작은 '공유' 아이콘을 클릭해야 합니다.

![partager paynym samourai](assets/en/1.webp)


사용자 측에서 Samourai Wallet 애플리케이션을 실행하고 같은 방법으로 "PayNyms" 메뉴에 액세스합니다. PayNym을 처음 사용하는 경우 식별자를 획득해야 합니다.


![demander un paynym](assets/notext/3.webp)


그런 다음 화면 오른쪽 하단의 파란색 '+'를 클릭합니다.

![ajouter paynym collaborateur](assets/notext/4.webp)

그런 다음 '공동 작업자 결제 코드 붙여넣기'를 선택하여 공동 작업자의 결제 코드를 붙여넣거나 'QR코드 스캔'을 눌러 카메라를 열어 QR 코드를 스캔할 수 있습니다.![페이님 식별자 붙여넣기](assets/notext/5.webp)를 누르세요


'SUIVRE' 버튼을 클릭합니다.

![follow paynym](assets/notext/6.webp)

'예'를 클릭하여 확인합니다.

![confirm follow paynym](assets/notext/7.webp)

그러면 소프트웨어가 'SE 연결' 버튼을 제공합니다. 튜토리얼을 위해 이 버튼을 클릭할 필요는 없습니다. 이 단계는 튜토리얼과 관련이 없는 BIP47의 일부로 다른 Paynym에 결제하려는 경우에만 필요합니다.

![connect paynym](assets/notext/8.webp)

수신자의 페이님을 내 페이님이 따라가면 반대 방향으로 이 작업을 반복하여 수신자도 내 페이님을 따라가도록 합니다. 그런 다음 PayJoin를 수행할 수 있습니다.


## 사무라이 Wallet에서 PayJoin은 어떻게 하나요?


이러한 예비 단계를 완료했다면 드디어 PayJoin 트랜잭션을 수행할 준비가 된 것입니다! 이렇게 하려면 비디오 튜토리얼을 따라하세요:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**외부 리소스:**


- https://docs.samourai.io/en/spend-tools#stowaway.