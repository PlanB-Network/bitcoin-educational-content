---
name: 제이드 - Electrum
description: Electrum(데스크톱)에서 Jade 또는 Jade Plus를 사용하는 방법
---

![cover](assets/cover.webp)



이 가이드는 [Bitcoin 워크샵 강의](https://officinebitcoin.it/lezioni/jadeele/index.html)에서 발췌한 것입니다



이 튜토리얼은 제이드 클래식으로 제작되었지만, 제이드 플러스를 사용하는 분들에게도 해당 작업은 유효합니다.



Jade를 초기화한 후 사용을 시작하려면 wallet 디스플레이를 선택하면 됩니다.



Jade는 블록스트림이 사이트에서 지정한 대로 여러 wallet 또는 동반 앱과 함께 사용할 수 있는 기기입니다.



이 튜토리얼에서는 USB 케이블 연결을 통해 Electrum Wallet을 사용하는 단계를 설명합니다.



## 공개 키 전송



초기화된 Jade를 가져와서 켭니다. 전원을 켜면 다음과 같은 화면이 나타납니다:




![img](assets/en/32.webp)



옥 잠금 해제_를 선택하면 기기를 동반 앱에 연결하는 방법을 선택할 수 있는 메뉴가 표시됩니다.



Electrum에서는 USB를 통해서만 Jade를 연결할 수 있으므로 이 방법을 선택하세요.



Electrum을 실행하면 마지막으로 사용한 wallet을 여는 기본 옵션으로 제안이 열립니다.



Jade를 Electrum에 처음 연결하는 경우, _새 지갑 만들기_를 선택한 다음 _끝내기_를 선택합니다.



![img](assets/en/34.webp)



이름 wallet.



![img](assets/en/35.webp)



표준 Wallet를 선택합니다.



![img](assets/en/36.webp)



키 저장소를 선택할 때 반드시 _하드웨어 장치 사용_을 선택해야 합니다.



![img](assets/en/37.webp)



Electrum이 하드웨어 장치 검색을 시작합니다.



![img](assets/en/38.webp)



USB를 컴퓨터에 연결하면(이미 USB C 쪽에서 Jade에 연결되어 있음) wallet 하드웨어가 잠금 모드로 나타납니다. 설정 시 설정한 6자리 PIN을 입력하면 Jade의 잠금이 해제됩니다.




![img](assets/en/39.webp)



잠금 해제된 하드웨어 장치, Electrum가 제이드 감지. 계속하려면 _다음_을 클릭합니다.



![img](assets/en/40.webp)



이 시점에서 Electrum은 정책 스크립트를 설정하라는 메시지를 표시합니다: _Native Segwit_을 선택합니다.



![img](assets/en/41.webp)



제이드에서 wallet에서 Electrum을 표시하기 위해 공개 키를 전송하는 단계가 시작됩니다.



공개 키 내보내기가 완료되면 프로세스가 완료됩니다.



시계 전용이 준비되면 Electrum는 다음 화면으로 완료를 알립니다.



![img](assets/en/42.webp)



wallet이 실제로 생성되고 탐색을 시작할 수 있습니다. _주소_와 _지갑 정보_를 볼 수 있으며, 가장 중요한 것은 오른쪽 하단에서 블록스트림의 장치라는 표시를 볼 수 있다는 것입니다. 블록스트림 로고 옆의 녹색 점은 장치가 켜져 있고 로컬 네트워크에 제대로 연결되어 있음을 나타냅니다.



![img](assets/en/43.webp)



## 거래 수취 및 지출



Electrum, generate의 _Receive_ 메뉴에서 '스크립트펍키'(주소)를 입력해 자금을 받습니다. 항상 적은 금액으로 시작하여 수신+지출 테스트를 해보세요.



![img](assets/en/44.webp)



수능을 받으면 _기록_ 메뉴에서 도착을 확인할 수 있습니다.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



거래가 확인되면 이 UTXO을 사용하여 테스트를 완료할 수 있습니다.



이 비용에는 서명할 때 Jade를 사용하는 것이 포함됩니다.



Electrum의 _Send_ 메뉴로 이동하여 스크립트PubKey를 붙여넣고 잘 확인합니다.



![img](assets/en/47.webp)



완료되면 _결제_를 누릅니다.



거래 창이 열리면 정확한 거래 수수료를 설정하는 것이 중요합니다. 모든 설정을 완료했으면 오른쪽 하단에 있는 _미리 보기_를 클릭합니다.



![img](assets/en/48.webp)



거래 창에는 몇 가지 중요한 세부 정보가 표시되며, 무엇보다도 상태가 가장 먼저 표시됩니다: 서명되지 않음`입니다.



이 단계에서는 옥으로 서명을 붙이려면 클릭해야 하는 _Sign_ 명령도 볼 수 있습니다.



![img](assets/en/49.webp)



이제 디스플레이 wallet과 하드웨어 장치 간의 통신 단계가 시작되며, Electrum는 하드웨어 장치의 지침을 따르고 전원을 켜고 서명할 준비가 되었다는 알림을 보냅니다.



![img](assets/en/50.webp)



**방금 설정한 트랜잭션의 모든 매개변수가 Jade**에도 표시되며, 이를 모두 확인할 수 있습니다.



![img](assets/en/51.webp)



작업을 완료하지 않고 끝내지 않으려면 항상 다음 단계로 연결되는 `→` 화살표에 커서를 놓고 `X`에는 커서를 놓지 마세요.



확인 부분은 수수료 표시로 끝납니다. 이 시점에서 확인은 서명을 하는 것과 동일합니다.



![img](assets/en/52.webp)



잠시 동안 Jade가 작업을 처리하고 완료되면 홈 메뉴로 돌아갑니다.



![img](assets/en/53.webp)



Electrum에서는 '서명되지 않음'에서 '서명됨'으로 변경된 트랜잭션의 상태를 확인할 수 있으며, 이제 _Broadcast_를 클릭하여 트랜잭션을 전파할 수 있습니다.



![img](assets/en/54.webp)



이렇게 테스트가 완료된 wallet은 안전한 보관용 UTXO를 수신하는 데 사용할 수 있습니다.



![img](assets/en/55.webp)



이 가이드는 USB를 통해 연결된 Jade를 wallet 시계 전용으로 사용하는 방법에 대한 예시입니다. Electrum이 전형적인 예시이지만, 다른 wallet 소프트웨어를 선호하실 수도 있습니다. Jade는 공개키를 다른 많은 지갑으로 내보낼 수 있습니다. 이 튜토리얼에서 소개한 유사한 기능을 찾아서 자주 사용하는 컴퍼니 앱에서 사용하는 방법을 찾아보세요.