---
name: Jade Plus - Green
description: Green로 Jade Plus를 쉽게 구성하기
---
![cover](assets/cover.webp)


![video](https://youtu.be/rv_cN7F7-TM)


Jade Plus는 블록스트림에서 설계한 Bitcoin 전용 Hardware Wallet입니다. 소프트웨어 개선, 더 많은 옵션, 보다 직관적인 사용을 위해 새롭게 디자인된 인체공학적 설계를 갖춘 클래식 Jade의 후속 제품입니다. 이 새로운 버전은 이전 버전보다 더 넓은 색 영역을 자랑하는 멋진 1.9인치 LCD 화면을 자랑합니다. 버튼과 메뉴 탐색도 최적화되었습니다.


USB-C 유선 연결, 마이크로 SD 카드(어댑터 필요)를 사용한 '*에어 갭*' 모드, 블루투스 또는 내장 카메라 덕분에 QR 코드를 교환하는 등 다양한 방식으로 Jade Plus를 사용할 수 있습니다. Hardware Wallet는 배터리로 작동합니다.


기본 블랙 버전은 $149.99부터 구매할 수 있으며, "*Genesis 그레이*" 또는 "*루나 실버*" 버전은 최대 $20까지 가격이 올라갈 수 있습니다. 따라서 제이드 플러스는 콜드카드 Q나 패스포트 V2와 같은 고급 하드웨어 지갑에 필적하는 고급 기능을 제공하면서도 중급 모델에 가까운 상당히 저렴한 가격으로 흥미로운 선택이 될 것입니다.


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus는 대부분의 Wallet 관리 소프트웨어와 호환됩니다. 다음은 작성 시점(2025년 1월)의 호환성 요약입니다:


| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

이 튜토리얼에서는 블루투스 연결을 통해 블록스트림의 Green Wallet 모바일 앱으로 제이드 플러스를 설정하고 사용하는 방법을 설명합니다. 이 설정은 초보자에게 이상적입니다. 좀 더 고급 접근 방식을 찾고 있다면 QR코드 모드에서 Sparrow wallet과 함께 Jade Plus를 사용하는 이 튜토리얼을 살펴보는 것이 좋습니다:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## 제이드 플러스 안전 모델


제이드 플러스는 "블라인드 오라클"에 의해 구체화된 "가상 secure element"을 기반으로 하는 보안 모델을 사용합니다. 구체적으로 이 메커니즘은 사용자가 선택한 PIN, Jade에서 호스팅되는 비밀, 오라클(블록스트림에서 관리하는 서버)이 보유한 비밀을 결합하여 두 개 엔티티에 분산된 AES-256 키를 생성합니다. 개시하는 동안 ECDH Exchange는 오라클과의 통신을 보호하고 Hardware Wallet에서 복구 구문을 암호화합니다. 실제로 트랜잭션에 서명하기 위해 seed에 액세스하려면 :




- Jade Plus 기기 자체로;
- 비밀번호로 이동하여 디바이스 잠금을 해제합니다;
- 그리고 오라클의 비밀에 대해 알아보세요.


이 접근 방식의 가장 큰 장점은 하드웨어 수준에서 단일 장애 지점이 없다는 것입니다. 공격자가 Jade에 액세스하는 경우 키를 추출하려면 Jade와 오라클을 동시에 손상시켜야 하기 때문입니다. 또한 이 모델은 Jade Plus가 완전히 오픈 소스이기 때문에 예를 들어 Ledger에서 사용되는 것과 같은 실제 물리적 보안 Elements 사용과 관련된 제약을 피할 수 있다는 것을 의미합니다.


이 시스템의 단점은 제이드 플러스의 사용이 블록스트림에서 관리하는 오라클에 의존한다는 것입니다. 이 오라클에 액세스할 수 없게 되면 더 이상 PIN으로 Hardware Wallet을 직접 사용할 수 없습니다. 그러나 "*무상태*" 모드에서 제이드 플러스에 입력할 수 있는 복구 문구를 사용하여 비트코인을 복구할 수 있으므로 비트코인이 손실되는 것은 아닙니다. 이러한 종속성을 피하기 위해 자체 오라클 서버를 구성하고 관리할 수도 있습니다.


## 제이드 플러스 개봉하기


Jade Plus를 받으면 상자와 Seal의 상태가 양호한지, 패키지가 개봉되지 않았는지 확인하세요.


![JADE-PLUS-GREEN](assets/fr/02.webp)


상자에서 찾을 수 있습니다:




- 르 제이드 플러스;
- USB-C 케이블;
- Mnemonic 문구를 단어 또는 "*CompactSeedQR*"로 기록할 수 있는 카드입니다;
- 몇 가지 사용 지침 ;
- 코드;
- 스티커 몇 개.


![JADE-PLUS-GREEN](assets/fr/03.webp)


기기에는 4개의 탐색 버튼이 있습니다:




- 오른쪽 하단의 버튼을 누르면 Jade가 켜집니다;
- 기기 전면의 큰 버튼은 항목을 선택하는 데 사용됩니다;
- 상단에 있는 두 개의 작은 버튼으로 왼쪽과 오른쪽을 탐색할 수 있습니다;
- 디바이스 상단에 있는 두 개의 버튼을 동시에 클릭하여 항목을 선택할 수도 있습니다.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## 새 Bitcoin Wallet 설정하기


시작 버튼을 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/05.webp)


"*설정 옥*"을 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/06.webp)


"설정 시작"을 선택합니다. "*고급 설정*" 옵션은 동일한 기능을 수행하지만 고급 설정에 액세스할 수 있습니다.


![JADE-PLUS-GREEN](assets/fr/07.webp)


그런 다음 "*새 Wallet 만들기*"를 클릭하여 새 generate을 seed으로 만듭니다.


![JADE-PLUS-GREEN](assets/fr/08.webp)


"*계속*" 버튼을 클릭하여 새 복구 문구를 표시합니다.


![JADE-PLUS-GREEN](assets/fr/09.webp)


제이드 플러스는 12단어 Mnemonic 문구를 표시합니다. **이 Mnemonic는 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다. 이 문구를 소유한 사람은 제이드 플러스에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다. 12단어 문구는 제이드 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다**


상자에 동봉된 판지에 적거나, 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 베이스에 각인하여 보안을 강화하는 것이 좋습니다.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**이 튜토리얼에서처럼 인터넷에서 이 단어를 절대 공유해서는 안 됩니다. 이 샘플 Wallet은 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다**


화면 오른쪽에 있는 화살표를 클릭하면 다음 단어가 표시됩니다.


![JADE-PLUS-GREEN](assets/fr/11.webp)


문구를 저장하면 Jade Plus에서 확인을 요청합니다. 장치 상단의 버튼을 사용하여 순서에 따라 올바른 단어를 선택하고 중앙의 버튼을 클릭하면 다음 단어로 넘어갑니다.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## 제이드 플러스와 Green Wallet 연결하기


이 튜토리얼에서는 Green Wallet 애플리케이션을 사용하여 제이드 플러스에서 호스팅되는 Wallet를 관리합니다. 이 방법은 특히 초보자에게 적합합니다. Bitcoin Wallet를 더 자세히 관리하려면 별도의 튜토리얼에서 다루게 될 Sparrow wallet을 사용할 수도 있습니다:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Blockstream Green 애플리케이션 설치 및 설정에 대한 지침은 이 다른 튜토리얼의 첫 번째 부분을 참조하세요:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Blockstream Green 애플리케이션에서 "*새 Wallet 구성하기*" 버튼을 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/13.webp)


"*온 Hardware Wallet*"을 선택합니다.


![JADE-PLUS-GREEN](assets/fr/14.webp)


스마트폰에서 블루투스를 활성화한 다음 "*Jade 연결*" 버튼을 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/15.webp)


Green 애플리케이션이 블루투스 연결에 액세스할 수 있도록 권한을 부여합니다.


![JADE-PLUS-GREEN](assets/fr/16.webp)


애플리케이션에서 제이드 플러스를 찾고 있습니다.


![JADE-PLUS-GREEN](assets/fr/17.webp)


Jade Plus에서 "*블루투스*" 메뉴를 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/18.webp)


Green 애플리케이션에서 기기를 선택합니다.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Jade Plus에서 페어링 코드를 확인합니다.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green은 제이드가 진품인지 확인할 수 있는 테스트를 제공합니다. 버튼을 클릭하세요.


![JADE-PLUS-GREEN](assets/fr/21.webp)


제이드에서 확인합니다.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green은 기기가 정품임을 확인합니다.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## PIN 코드 설정


"*계속*" 버튼을 클릭해 제이드의 비밀번호를 선택합니다.


![JADE-PLUS-GREEN](assets/fr/24.webp)


PIN 코드는 제이드의 잠금을 해제합니다. 따라서 무단 물리적 액세스로부터 보호할 수 있습니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 관여하지 않습니다. 따라서 이 PIN 코드에 액세스할 수 없더라도 12단어 Mnemonic 문구를 소지하고 있으면 비트코인에 다시 액세스할 수 있습니다. 가능한 한 무작위로 PIN 코드를 선택하는 것이 좋습니다. 그리고 이 코드를 제이드가 저장된 곳과 별도의 위치(예: 비밀번호 관리자)에 저장하시기 바랍니다.


오른쪽과 왼쪽 버튼을 사용하여 숫자를 스크롤하고 가운데 버튼을 눌러 숫자 입력을 확인한 다음, Jade에서 6자리 PIN 코드를 선택합니다.


![JADE-PLUS-GREEN](assets/fr/25.webp)


비밀번호를 다시 한 번 확인합니다.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Bitcoin Wallet가 생성되었습니다.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Bitcoin 계정 만들기


이제 Wallet 내에서 계정을 만들어야 합니다. "*계정 만들기*" 버튼을 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/28.webp)


클래식 싱글사인 Wallet을 만들려면 "*표준*"을 선택합니다.


![JADE-PLUS-GREEN](assets/fr/29.webp)


'*2FA*' 옵션에 대한 자세한 내용은 다른 튜토리얼을 참조하세요:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

계정이 생성되었습니다.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Green Wallet를 맞춤 설정하려면 오른쪽 상단의 작은 점 세 개를 클릭하세요.


![JADE-PLUS-GREEN](assets/fr/31.webp)


"*이름 바꾸기*" 옵션을 사용하면 Wallet의 이름을 사용자 지정할 수 있으며, 동일한 애플리케이션에서 여러 지갑을 관리할 때 특히 유용합니다. "*단위*" 메뉴에서는 Wallet의 기본 단위를 변경할 수 있습니다. 예를 들어 비트코인이 아닌 사토시로 표시하도록 선택할 수 있습니다. 마지막으로 "*파라미터*" 메뉴에서는 다른 옵션에 액세스할 수 있습니다. 예를 들어, 여기에서 확장된 공개 키와 해당 Descriptor를 확인할 수 있으며, 이는 제이드에서 Watch-only wallet을 설정하려는 경우 유용합니다.


![JADE-PLUS-GREEN](assets/fr/32.webp)


Jade를 끈 후 다시 연결하려면 장치 하단의 켜기/끄기 버튼을 누릅니다. Green 애플리케이션의 홈 페이지에서 디바이스를 선택합니다:


![JADE-PLUS-GREEN](assets/fr/33.webp)


그런 다음 Jade에 있는 PIN 코드를 입력하면 다시 연결됩니다.


![JADE-PLUS-GREEN](assets/fr/34.webp)


블록스트림의 "가상 secure element"(이 튜토리얼의 첫 번째 섹션 참조)를 통해 Jade의 잠금을 해제할 수 있습니다. 이를 위해서는 Green 애플리케이션과 블루투스 연결이 필요합니다. 잠금 해제 중에 블루투스 연결에 문제가 발생하면 두 디바이스의 연결을 해제했다가 다시 연결해 보세요. 문제가 지속되는 경우에도 "*QR 스캔*" 옵션을 선택하고 [블록스트림 웹사이트](https://jadefw.blockstream.com/pinqr/index.html)에서 제공되는 지침에 따라 Jade의 잠금을 해제할 수 있습니다.


Wallet에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub 또는 처음 받은 Address과 같은 몇 가지 참조 정보를 메모한 다음, 아직 비어 있는 상태에서 Green 앱과 제이드 플러스에서 Wallet를 삭제하세요(`옵션 -> 장치 -> 공장 초기화`). 그런 다음 Mnemonic 문구의 종이 백업을 사용하여 Wallet를 복원해 보세요. 복원 후 생성된 쿠키 정보가 원래 기록했던 쿠키 정보와 일치하는지 확인하세요. 일치한다면 종이 백업이 신뢰할 수 있는 것이니 안심해도 됩니다. 테스트 복구를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼 을 참조하세요:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 비트코인 받기


이제 Bitcoin Wallet가 설정되었으니 첫 번째 Sats를 받을 준비가 되었습니다! Green 애플리케이션에서 "*수신*" 버튼을 클릭하기만 하면 됩니다.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green은 수신 Address를 표시하지만, 사용하기 전에 Jade에서 이를 확인하여 실제로 Wallet에 속하는지 확인해야 합니다. 이렇게 하려면 "*기기에서 확인*" 버튼을 클릭하세요.


![JADE-PLUS-GREEN](assets/fr/36.webp)


옥에서 Address이 Green와 동일한지 확인한 다음 버튼을 클릭하여 확인합니다.


![JADE-PLUS-GREEN](assets/fr/37.webp)


이제 Address을 결제자와 공유하여 Wallet에서 비트코인을 받을 수 있습니다. 트랜잭션이 네트워크에 브로드캐스트되면 Wallet에 표시됩니다. 트랜잭션이 확정된 것으로 간주할 만큼 충분한 확인을 받을 때까지 기다리세요.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## 비트코인 보내기


Wallet에 비트코인이 있으면 이제 비트코인을 보낼 수도 있습니다. "*송금*"을 클릭합니다.


![JADE-PLUS-GREEN](assets/fr/39.webp)


다음 페이지에서 수신자의 Address을 입력합니다. 수동으로 입력하거나 QR 코드를 스캔할 수 있습니다.


![JADE-PLUS-GREEN](assets/fr/40.webp)


결제 금액을 선택합니다.


![JADE-PLUS-GREEN](assets/fr/41.webp)


화면 하단에서 이 거래에 대한 수수료율을 선택할 수 있습니다. 애플리케이션의 권장 사항을 따르거나 수수료를 사용자 지정할 수 있습니다. 보류 중인 다른 트랜잭션과 비교하여 수수료가 높을수록 트랜잭션이 더 빨리 처리됩니다. 수수료 시장 정보는 [Mempool.space](https://Mempool.space/)의 "*거래 수수료*" 섹션에서 확인하시기 바랍니다.


![JADE-PLUS-GREEN](assets/fr/42.webp)


"*다음*"을 클릭하여 거래 요약 화면에 액세스합니다. Address, 금액 및 요금이 정확한지 확인합니다.


![JADE-PLUS-GREEN](assets/fr/43.webp)


모든 것이 순조롭게 진행되면 화면 하단의 Green 버튼을 오른쪽으로 밀어서 Bitcoin 네트워크에서 트랜잭션에 서명하고 브로드캐스트합니다.


![JADE-PLUS-GREEN](assets/fr/44.webp)


이제 제이드에서 거래를 확인하라는 메시지가 표시됩니다.


![JADE-PLUS-GREEN](assets/fr/45.webp)


받는 사람의 Address이 올바른지 확인하세요. 확인 표시를 클릭하여 확인합니다.


![JADE-PLUS-GREEN](assets/fr/46.webp)


청구 금액이 정확한지 확인한 다음 유효성을 검사합니다.


![JADE-PLUS-GREEN](assets/fr/47.webp)


거래가 Green에서 서명 및 브로드캐스트되었습니다.


![JADE-PLUS-GREEN](assets/fr/48.webp)


이제 블루투스 연결을 통해 Blockstream Green 모바일 애플리케이션으로 제이드 플러스를 설정하고 사용하는 방법을 알게 되었습니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 공유해 주셔서 감사합니다!


한 단계 더 나아가기 위해 QR 모드에서 Sparrow wallet 소프트웨어로 구성하는 Jade Plus 튜토리얼을 추천합니다. 또한 Hardware Wallet의 고급 설정을 사용하는 방법도 배울 수 있습니다:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262