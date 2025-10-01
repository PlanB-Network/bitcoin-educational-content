---
name: Robosats

description: 로보샛 사용 방법
---

![cover](assets/cover.webp)


RoboSats(https://learn.robosats.com/)는 P2P 경험을 단순화하고 라이트닝 홀드 인보이스를 사용하여 보관 및 신뢰 요구 사항을 최소화하는 국가 통화를 위한 간편한 비공개 Exchange Bitcoin 방법입니다.


![video](https://youtu.be/XW_wzRz_BDI)


## 가이드


**참고: 이 가이드는 비트코인의 Q&A(https://bitcoiner.guide/robosats/)에서 가져온 것입니다. 모든 크레딧은 그에게 있으며, [여기](https://bitcoiner.guide/contribute)에서 그를 지원할 수 있습니다. 비트코인Q&A는 Bitcoin 멘토이기도 합니다. 멘토링을 원하시면 그에게 연락하세요!


![image](assets/0.webp)


로보샛 - 간단하고 프라이빗한 라이트닝 기반 P2P Exchange


## 시작하기 전에


### 알아야 할 사항


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## 필요한 사항


### 라이트닝 Wallet


RoboSats는 Lightning 네이티브이므로 채권에 자금을 조달하고 구매한 Sats을 구매자로 받으려면 Lightning Wallet이 필요합니다. RoboSats를 작동시키는 데 사용되는 기술이 모두 호환되는 것은 아니므로 Wallet를 선택할 때 주의해야 합니다.


노드 운영자라면 Zeus가 단연 최고의 선택입니다. 자체 노드가 없는 경우 간단한 설정으로 Lightning에 액세스할 수 있는 크로스 플랫폼 모바일 Wallet인 Phoenix를 적극 추천합니다. 이 가이드 제작에는 Phoenix가 사용되었습니다.


### 일부 Bitcoin


구매자와 판매자는 거래가 성사되기 전에 보증금을 입금해야 합니다. 이는 보통 거래 금액의 3% 정도로 매우 적은 금액이지만, 그럼에도 불구하고 필수 조건입니다.


로보샛을 이용해 첫 Sats을 구매하시나요? 시작하는 데 필요한 소액을 친구에게 빌려주시는 건 어떨까요? 혼자 비행하는 경우, 시작할 수 있는 noKYC Sats을 구할 수 있는 다른 훌륭한 옵션이 있습니다.


### 로보샛에 액세스


당연히 로보샛에 접속해야 합니다! 이를 위한 네 가지 주요 방법이 있습니다:


1. 토르 브라우저를 통해 (권장!)

2. 일반 웹 브라우저를 통해(권장하지 않음!)

3. Android APK를 통해

4. 내 고객


토르 브라우저를 처음 사용하시는 경우, 여기에서 자세히 알아보고 다운로드하세요[여기](https://www.torproject.org/download/).


휴대폰에서 토르를 통해 로보샛에 접속하고자 하는 iOS 사용자를 위한 간단한 참고 사항입니다. 'Onion Browser'는 토르 브라우저가 아닙니다. 대신 오봇 + 사파리 및 오봇 + 덕덕고를 사용하세요.


## Bitcoin 구매


다음 단계는 2023년 5월에 토르 브라우저를 통해 액세스한 0.5.0 버전을 사용하여 수행되었습니다. Android APK를 통해 RoboSats에 액세스하는 사용자도 동일한 단계를 거쳐야 합니다.


이 글을 쓰는 시점에서 로보샛은 여전히 활발히 개발 중이므로 Interface는 향후 약간 변경될 수 있지만 거래를 완료하는 데 필요한 기본 단계는 크게 변경되지 않을 것입니다.


**참고: RoboSats를 처음 로드하면 이 랜딩 페이지가 표시됩니다. 시작을 클릭합니다.


![image](assets/2.webp)


token를 암호화하여 암호화된 메모 앱이나 비밀번호 관리자와 같은 안전한 곳에 보관하세요. 브라우저나 앱이 거래 도중에 종료되는 경우 이 token를 사용해 임시 로봇 ID를 복구할 수 있습니다.


![image](assets/3.webp)


새 로봇 신원을 확인한 다음 계속을 클릭합니다.


![image](assets/4.webp)


오퍼를 클릭하여 주문서를 찾아봅니다. 그런 다음 페이지 상단에서 원하는 대로 필터링할 수 있습니다. 채권 비율과 Exchange 평균 요율에 대한 프리미엄을 반드시 확인하시기 바랍니다.



- '구매' 태그 선택
- 통화 선택
- 결제 방법 선택


![image](assets/5.webp)


**참고: 원하는 오퍼를 클릭합니다. 판매자로부터 구매하고자 하는 금액(선택한 법정통화로)을 입력한 다음 세부 정보를 최종 확인한 후 '주문하기'를 클릭합니다.


판매자가 온라인 상태가 아닌 경우(프로필 이미지에 빨간색 점으로 표시됨) 거래가 평소보다 오래 걸릴 수 있다는 경고 메시지가 표시됩니다. 계속 진행해도 판매자가 제시간에 거래를 진행하지 않으면 낭비한 시간에 대해 판매자의 채권 금액의 50%를 보상받게 됩니다.


![image](assets/6.webp)


다음으로 화면에서 Invoice을 지불하여 거래 채권을 고정해야 합니다. 이것은 Wallet에 동결되는 Invoice 보류입니다. 거래를 완료하지 못한 경우에만 청구됩니다.


![image](assets/7.webp)


라이트닝 Wallet에서 QR 코드를 스캔하고 Invoice을 결제합니다.


![image](assets/8.webp)


다음으로, 표시된 금액에 해당하는 Wallet generate을 Lightning Invoice에 입력한 후 제공된 공간에 붙여넣습니다.


![image](assets/9.webp)


판매자가 거래 금액을 고정할 때까지 기다립니다. 잠금이 완료되면 RoboSats는 자동으로 다음 단계로 이동하여 채팅 창이 열립니다. 안녕하세요라고 인사하고 판매자에게 법정화폐 결제 정보를 요청합니다. 정보가 제공되면 선택한 방법을 통해 결제금을 송금한 다음 RoboSats에서 이를 확인합니다. RoboSats의 모든 채팅은 PGP로 암호화되므로 여러분과 거래 상대방만 메시지를 읽을 수 있습니다.


![image](assets/10.webp)


판매자가 결제 수취를 확인하면 RoboSats는 앞서 제공한 Invoice을 사용하여 자동으로 결제를 해제합니다.


![image](assets/11.webp)


Invoice가 결제되면 거래가 완료되고 채권이 잠금 해제됩니다. 그러면 거래 요약이 표시됩니다.


![image](assets/12.webp)


라이트닝 Wallet가 도착했는지 확인하려면 Sats을 확인하세요.


![image](assets/13.webp)


## 추가 기능


Bitcoin의 명백한 구매 및 판매 외에도 RoboSats에는 알아야 할 몇 가지 다른 기능이 있습니다.

로봇 차고


여러 개의 거래를 동시에 진행하고 싶지만 여러 거래에서 동일한 신원을 공유하고 싶지 않으신가요? 문제 없습니다! 로봇 탭을 클릭하고 로봇을 추가한 다음 다음 주문을 만들거나 받으면 됩니다.


![image](assets/14.webp)


### 주문 생성


다른 사람의 제안을 받아들이는 것은 물론, 직접 로봇을 만들어 다른 로봇이 올 때까지 기다릴 수도 있습니다.



- 만들기 페이지를 엽니다.
- 주문이 Bitcoin를 매수 또는 매도할 것인지 정의합니다.
- 구매/판매하려는 금액과 통화를 입력합니다.
- 사용하고자 하는 결제 수단을 입력합니다.
- 수락하고자 하는 '시장가 대비 프리미엄' %를 입력합니다. 현재 시장가보다 할인된 가격으로 입찰하려면 이 수치가 마이너스일 수 있습니다.
- 주문 생성을 클릭합니다.
- 번개 Invoice을 지불하여 메이커 본드를 잠급니다.
- 주문이 완료되었습니다. 편안히 앉아 주문이 수락될 때까지 기다리세요.


![image](assets/15.webp)


### On-Chain 지급금


로보샛은 라이트닝에 초점을 맞추고 있지만, 구매자는 Sats를 On-Chain Bitcoin Address으로 받을 수 있는 옵션이 있습니다. 구매자는 채권을 락업한 후 이 옵션을 선택할 수 있습니다. On-Chain를 선택하면 구매자에게 수수료 개요가 표시됩니다. 이 서비스의 추가 수수료는 다음과 같습니다:



- RoboSats가 징수하는 스왑 수수료 - 이 수수료는 동적이며 Bitcoin 네트워크의 사용량에 따라 변동합니다.
- 지급 거래에 대한 Mining 수수료 - 이는 구매자가 구성할 수 있습니다.


![image](assets/16.webp)


### P2P 스왑


RoboSats를 사용하면 Sats을 Lightning Wallet로 교환할 수 있습니다. 오퍼 페이지 상단의 스왑 버튼을 클릭하기만 하면 현재 스왑 오퍼를 확인할 수 있습니다.


'스왑 인' 오퍼의 구매자는 On-Chain Bitcoin를 피어에게 보내고 광고된 수수료 및/또는 프리미엄을 뺀 Sats을 내 라이트닝 Wallet로 돌려받습니다. '스왑 아웃' 오퍼의 구매자는 라이트닝을 통해 Sats을 보내고 수수료 및/또는 프리미엄을 뺀 Bitcoin를 On-Chain Address으로 받습니다. 사무라이 또는 Sparrow wallet 사용자는 밀반입 기능을 활용하여 스왑을 완료할 수도 있습니다.


로보샛 스왑 오퍼에는 RBTC, LBTC, WBTC 등 Bitcoin에 대한 고정된 대안 토큰도 포함될 수 있습니다. 이러한 토큰은 모두 다양한 장단점이 있으므로 거래할 때는 각별히 주의해야 합니다. 페깅된 Bitcoin은 Bitcoin이 아닙니다!


![image](assets/17.webp)


### 나만의 로보샛 클라이언트 실행


Umbrel, Citadel 및 Start9 노드 런너는 자체 RoboSats 클라이언트를 노드에 직접 설치할 수 있습니다. 이렇게 하면 다음과 같은 이점이 있습니다:



- 로드 시간이 획기적으로 빨라졌습니다.
- 더 안전하게: 실행하는 RoboSats 클라이언트 앱을 제어할 수 있습니다.
- 모든 브라우저/기기에서 안전하게 RoboSats에 액세스하세요. 로컬 네트워크에 있거나 VPN을 사용하는 경우 TOR을 사용할 필요가 없습니다. 노드 백엔드에서 익명화에 필요한 토렌트를 처리하기 때문입니다.
- 연결할 P2P 마켓 코디네이터를 제어할 수 있습니다(기본값은 robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## 자주 묻는 질문


### 사기를 당해도 되나요?


구매자는 거래에 필요한 법정화폐를 보냈지만 판매자가 Sats를 릴리스하지 않는 경우 분쟁을 제기할 수 있습니다. 이 분쟁 과정에서 법정화폐를 송금했음을 RoboSats 중재자에게 증명하면 판매자가 자금을 에스크로 처리하고 거래 채권이 귀하에게 지급됩니다.

거래를 취소하려면 어떻게 해야 하나요?


채권을 게시한 후 거래 메뉴에서 공동 취소 버튼을 클릭하면 거래를 취소할 수 있습니다. 거래 상대방이 취소를 원하면 수수료가 발생하지 않습니다. 하지만 거래 파트너가 거래를 완료하고 싶어하는데도 취소를 진행하면 거래 채권을 잃게 됩니다.


### 로보샛은 'X' 결제 수단과 함께 사용할 수 있나요?


RoboSats에는 결제수단에 대한 제한이 없습니다. 원하는 결제수단으로 오퍼가 표시되지 않는다면 직접 오퍼를 생성해 보세요!


![image](assets/19.webp)


### 로보샛을 사용하면 나에 대해 무엇을 알게 되나요?


토르 또는 안드로이드 앱을 통해 로보샛을 사용한다면, 전혀 문제가 없습니다! 여기에서 더 자세히 알아보세요.



- 토르는 사용자의 네트워크 개인 정보를 보호합니다.
- PGP 암호화는 거래 채팅을 비공개로 유지합니다.
- 계좌가 없다는 것은 거래당 하나의 로봇을 의미합니다. 즉, 로보샛은 여러 트레이딩을 하나의 실체에 연결할 수 없습니다.


하지만 몇 가지 주의 사항이 있습니다! 라이트닝은 발신자 입장에서는 상당히 비공개적이지만 수신자 입장에서는 그렇지 않습니다. 자신의 라이트닝 노드로 수신하는 경우, 노드 ID는 송장에 공유됩니다. 이 노드 ID를 아는 사람은 누구나 On-Chain 활동을 연결할 수 있는 시작점을 제공합니다. 이는 사용자가 On-Chain 지급을 통해 거래를 받기로 선택한 경우에도 마찬가지입니다.


이를 완화하기 위해 사용자는 라이트닝용 프록시 Wallet 또는 On-Chain용 CoinJoin과 같은 솔루션을 사용할 수 있습니다.


### 페더레이션


현재 로보샛 개발팀이 운영하는 로보샛 코디네이터는 단 한 명입니다. Bitcoin에서는 어떤 형태의 중앙 집중화라도 특정 서비스를 좋아하지 않을 수 있는 정부나 규제 기관의 표적이 되기 쉽습니다.


로보샛은 오픈 소스 프로젝트이기 때문에 누구나 코드를 가져와 자신만의 코디네이터를 운영할 수 있습니다. 이렇게 하면 단일 대상에서 위험을 어느 정도 분산시킬 수 있지만, 이미 얇은 유동성 시장을 파편화시킬 수도 있습니다.


로보샛 팀은 이를 인지하고 연합 모델에 대한 작업을 시작했습니다. 최종 사용자 입장에서는 위에서 설명한 거래 흐름이 크게 달라지지는 않겠지만, 다른 코디네이터를 추가하거나 제거할 수 있는 보기 또는 화면이 추가될 것입니다.


가이드 끝

https://bitcoiner.guide/robosats/