---
name: Sats.mobi

description: 텔레그램 접근이 가능한 보관 Wallet
---

![cover](assets/cover.webp)


이 튜토리얼은 _[Bitcoin 캠퍼스](https://linktr.ee/bitcoincampus_)에서 작성했습니다


## Sats.Mobi

샛츠모비는 텔레그램에서 작동하는 Wallet로, Lightning Network(커스터디)의 모든 기능과 더불어 매우 재미있는 기능들을 갖추고 있습니다. 지금은 단종된 라이트닝팁봇의 Fork에서 시작되었으며, 모든 기능을 계승하면서 최신 기능들을 추가하여 더욱 현대화 되었습니다. 라이트닝팁봇과 마찬가지로 Sats.Mobi 역시 오픈 소스 철학을 수용합니다. Wallet는 이 [저장소](https://github.com/massmux/SatsMobiBot)에서 복제하여 독립적으로 구성 및 관리할 수 있습니다.


간단하게 사용하시려면, 텔레그램에서 채팅을 시작하면 봇임을 알 수 있습니다.


## 설정

텔레그램 검색창에서 "satsmobi"를 검색하면, [봇](@SatsMobiBot) 링크가 나타납니다.


**주의**: 텔레그램을 통한 검색에 대해 잘 모르겠다면, 다음 [링크](https://t.me/SatsMobiBot)를 이용하여 봇에 안전하게 접속하세요


![image](assets/it/01.webp)


시작하려면 _START_를 누르기만 하면 됩니다


![image](assets/it/02.webp)


Wallet을 탐색하려면 왼쪽 하단에서 _메뉴_를 선택하면 됩니다.


![image](assets/it/03.webp)


이제 기본 명령어 중 _/help_를 선택합니다.


![image](assets/it/04.webp)


Sats.Mobi는 모든 주요 기능을 나열하는 메시지를 보여주며 우리를 맞이합니다. 시작과 동시에, 봇은 텔레그램에서 선택한 핸들(기본적으로 고유한 핸들)에 연결된 LN Address도 생성했습니다. 이 Wallet으로 Sats을 보내고 받는 명령과 나중에 보게 될 다른 기능들을 볼 수 있습니다. 고급_ 메뉴도 살펴보는 것도 흥미롭습니다


![image](assets/it/05.webp)


Sats.Mobi는 익명의 LN Address도 생성하여 프라이버시를 확보하는 데 사용한다는 점도 주목할 만합니다. 봇은 명령어로 작동합니다. 해당 단어를 클릭하거나 메시지 표시줄에 슬래시 "/"를 입력한 다음 실행하려는 명령을 입력하기만 하면 됩니다. Wallet가 방금 생성된 경우에도 예를 들어 _/transactions_를 선택합니다


![image](assets/it/06.webp)


이 명령은 최신 트랜잭션 목록을 표시하며, 이 경우 0과 같습니다.


![image](assets/it/07.webp)


## Sats 수신

Invoice를 생성하고 Sats을 수신하는 명령은 _/invoice_입니다. Sats.Mobi는 Bitcoin의 가장 작은 단위인 Satoshi으로만 작동하므로 Invoice를 생성하려면 메시지 표시줄에 Sats에 금액을 입력한 후 봇과의 채팅에서 전송해야 합니다.

![image](assets/it/08.webp)


다음 예에서는 210Sats의 금액을 받기로 선택했습니다.


![cover](assets/it/09.webp)


Invoice이 준비될 때까지 잠시 기다리면 문자 및 QR 코드로 확인할 수 있습니다. Invoice을 결제하면 Wallet에 잔액이 표시됩니다. 어떤 이유로 총액이 업데이트되지 않으면 _/balance_를 입력하고 `enter` 키를 누릅니다.


![image](assets/it/10.webp)


## Sats 보내기


Sats은 매우 귀중한 자산이므로 쉽게 포기해서는 안 되지만, Sats.Mobi는 이 부분을 매력적으로 만들어 몇 가지 간단한 테스트(예: 몇 번의 시범 거래)를 수행해도 문제가 되지 않습니다.


### Invoice 지불


Invoice을 결제하는 가장 간단한 방법은 메시지 문자열 `lnbc1xxxxx`를 복사하여 _/pay_ 명령어를 입력한 후 메시지 표시줄에 붙여넣는 것입니다. **올바른 구문**을 사용하려면 명령 뒤에 공백을 남겨야 합니다.


![image](assets/it/11.webp)


Wallet이 확인을 요청하는 메시지를 보냅니다. 결제하기_를 클릭하면 Invoice가 결제됩니다.


![image](assets/it/12.webp)


Sats.Mobi는 효율적이고 잘 연결된 라이트닝 노드에 의존할 수 있으며, 항상 올바른 라우팅을 찾기 때문에 결제 실패가 거의 발생하지 않습니다.


### 모바일에서 간편하게 결제하기


텔레그램에서 브라우징하는 Sats.Mobi는 모바일에서도 사용할 수 있습니다. 모바일로 결제할 때 가장 편리한 기능은 QR코드 스캔이지만, 이 Wallet은 독립형 앱이 아닌 소셜 네트워크에 포함되어 있기 때문에, 설계상 QR코드 스캔 기능이 없습니다. 따라서 Sats.Mobi는 가능한 한 모바일 경험을 용이하게 하도록 프로그래밍되어 있으며, 결제하려는 Invoice의 QR 코드를 촬영한 사진과 같은 이미지를 실제로 디코딩할 수 있습니다.


예를 들어 Invoice를 50Sats으로 지불하고 싶다고 가정해 보겠습니다.


![image](assets/it/20.webp)


이 메시지가 표시되면 관련 QR 코드를 사진으로 찍으면 됩니다.


![image](assets/it/21.webp)


그런 다음 모바일에서 텔레그램을 열고, Sats.Mobi와의 채팅에서 방금 찍은 QR 코드 사진을 첨부합니다


![cover](assets/it/22.webp)


선택되면 봇으로 전송합니다:


![image](assets/it/23.webp)

Sats.Mobi가 사진을 해독하고 정확한 설명과 함께 **즉시 결제 요청**을 표시합니다. 채팅에서 확인을 요청하며, 계속 진행하려면 _/pay_를 눌러야 합니다

![image](assets/it/24.webp)


결제가 처리될 때까지 잠시 기다려주세요.


![image](assets/it/25.webp)


카메라와 통합 스캔 기능을 사용하지 않고도 얻을 수 있는 결과물인 Invoice를 50 Sats에 지불했습니다.


### 텔레그램 그룹 내 Sats.Mobi


![image](assets/it/27.webp)


LNTipBot을 유명하게 만들었고, Sats.Mobi가 텔레그램에 제공하는 기능 중, 그룹 내 구성원들에게 재미있고 상호적인 경험을 제공하는 기능이 있습니다.

소유자는 봇을 그룹 채팅에 초대하고 Sats.Mobi를 관리자로 지정할 수 있습니다. 그 순간부터 회원들이 그룹에 기여한 다른 사용자에게 보상을 줄 수 있기 때문에 재미가 시작됩니다.


- _/tip_은 메시지에 답글을 달아 팁을 추가합니다;
- _/send_는 LN Address 또는 텔레그램 핸들을 수신자로 지정하여 송금합니다;
- 수도꼭지_(_/고급_ 메뉴에 있음)를 클릭하면 그룹에서 가장 빠른 회원이 _/수집_을 클릭하여 일련의 팁을 수집할 수 있습니다;
- (_/advanced_ 메뉴의 _/tipjar_)는 그룹의 사용자에게 보낼 수 있는 다른 유형의 배포를 생성합니다.


이러한 각 명령에는 기본 명령 메뉴에 설명된 구문이 있습니다.


그룹의 소유자가 아닌 경우? 문제없습니다. 설립자에게 Sats.Mobi를 초대하고 그룹의 관리자로 추가해 달라고 요청하면 모든 준비가 완료됩니다!


## POS(판매 시점)


Sats.Mobi가 처음 실행되면 봇은 사용자를 위한 또 다른 기능도 생성합니다: **POS**입니다. '장치'는 사용자가 _/pos_ 명령을 사용하거나 오른쪽 하단의 콘솔에서 관련 버튼을 클릭하여 활성화할 수 있습니다. 사실, POS는 웹 앱으로, 텔레그램 대화창에 팝업으로 열립니다


![image](assets/it/14.webp)


Interface은 왼쪽 상단에 사용자의 개인 텔레그램 핸들이 표시되며, 모든 POS와 마찬가지로 키패드에 금액을 입력하는 방식으로 간단하게 사용할 수 있습니다. 이제 서비스에 대해 21유로를 징수하고 싶다고 가정해 봅시다. Sats.Mobi는 기본적으로 Sats만 관리하기 때문에 머릿속으로 환산하는 것은 쉽지 않습니다. 반대로 POS는 유로를 계정 단위로 표시하면서 동시에 Satoshi로 동등한 금액을 표시합니다.


![image](assets/it/15.webp)

확인_을 클릭하면 QR 코드를 통해 고객에게 보여주거나 인스턴트 메시지를 통해 문자열로 전송할 수 있는 Invoice이 표시되며, 이를 통해 결제할 수 있습니다.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


물론 휴대폰에서도 POS를 사용할 수 있으며, 앞서 설명한 것과 동일한 방식으로 액세스할 수 있습니다.


![image](assets/it/18.webp)


휴대폰 화면에도 잘 표시됩니다:


![image](assets/it/19.webp)


## 추가 기능


앞서 살펴본 바와 같이 Sats.Mobi Wallet의 개념을 결제 수취 및 송금 작업 이상으로 확장하는 다른 기능도 있습니다:


- _/nostr_: Wallet를 Nostr 사용자와 연결하여 잽을 수신합니다;
- _/cashback_: 구매 시 캐시백을 받기 위해 판매자에게 제시할 수 있는 코드를 표시합니다;
- _/buy_: 봇 내에서 안내 절차를 시작하여 Sats를 유로로 구매할 수 있습니다;
- _/activatecard_: Sats.Mobi Wallet을 통해 충전할 수 있고 알림을 활성화할 수 있는 NFC 직불 카드의 활성화를 요청합니다;
- _/link_: 이 Wallet의 리모컨으로 사용할 수 있는 자신의 Zeus 또는 Blue Wallet에 대한 링크를 생성합니다.


## 결론

Sats.Mobi는 사용하기에 즐겁고 재미있는 Wallet으로, LNBits의 고급 기능을 사용하여 LNTipBot에서 경험했던 경험을 되살려줍니다. 하지만 **보관 서비스**라는 점을 기억하는 것이 중요합니다. 따라서 Sats을 아주 소량 보유하는 데 사용해야 하며, Lightning Network 자금을 위한 메인 Wallet이 아닙니다. 또한 500,000 Sats에 해당하는 본질적인 용량 제한이 있으며, 이 한도는 초과하지 않는 것이 좋습니다.


비수탁형 Lightning Network 지갑을 찾고 계신다면 다른 제품을 살펴보는 것이 좋습니다.


---
### 문서


- [깃허브](https://github.com/massmux/SatsMobiBot)
- 동영상](https://www.youtube.com/results?search_query=Sats.mobi) 데모 재생 목록