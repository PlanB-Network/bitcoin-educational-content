---
name: Jade Plus - Sparrow
description: Sparrow wallet을 사용한 제이드 플러스의 고급 구성
---
![cover](assets/cover.webp)


Jade Plus는 블록스트림에서 설계한 Bitcoin 전용 Hardware Wallet입니다. 소프트웨어 개선, 더 많은 옵션, 보다 직관적인 사용을 위해 새롭게 디자인된 인체공학적 설계를 갖춘 클래식 Jade의 후속 제품입니다. 이 새로운 버전은 이전 버전보다 더 넓은 색 영역을 자랑하는 멋진 1.9인치 LCD 화면을 자랑합니다. 버튼과 메뉴 탐색도 최적화되었습니다.


USB-C 유선 연결, 마이크로 SD 카드(어댑터 필요)를 사용한 '*에어 갭*' 모드, 블루투스 또는 통합 카메라 덕분에 QR 코드를 교환하는 등 다양한 방식으로 Jade Plus를 사용할 수 있습니다. Hardware Wallet는 배터리로 작동합니다.


기본 블랙 버전은 $149.99부터 구매할 수 있으며, "*Genesis 그레이*" 또는 "*루나 실버*" 버전은 최대 $20까지 가격이 올라갈 수 있습니다. 따라서 제이드 플러스는 콜드카드 Q나 패스포트 V2와 같은 고급 하드웨어 지갑에 필적하는 고급 기능을 제공하면서도 중급 모델에 가까운 상당히 저렴한 가격으로 흥미로운 선택이 될 것입니다.


![JADE-PLUS-SPARROW](assets/fr/01.webp)


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

이 튜토리얼에서는 QR코드 모드에서 데스크톱 Sparrow wallet 소프트웨어로 Jade Plus의 고급 구성을 설정합니다. 이 구성은 중급 또는 숙련된 사용자에게 이상적입니다. 초보자를 위한 더 간단한 접근 방식을 찾고 있다면 블루투스 연결을 통해 Green Wallet과 함께 Jade Plus를 사용하는 이 튜토리얼을 살펴보는 것이 좋습니다:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## 제이드 플러스 안전 모델


제이드 플러스는 "블라인드 오라클"에 의해 구체화된 "가상 secure element"을 기반으로 하는 보안 모델을 사용합니다. 구체적으로 이 메커니즘은 사용자가 선택한 PIN, Jade에서 호스팅되는 비밀, 오라클(블록스트림에서 관리하는 서버)이 보유한 비밀을 결합하여 두 개 엔티티에 분산된 AES-256 키를 생성합니다. 개시하는 동안 ECDH Exchange는 오라클과의 통신을 보호하고 Hardware Wallet에서 복구 구문을 암호화합니다. 실제로 트랜잭션에 서명하기 위해 seed에 액세스하려면 :




- 제이드 플러스 기기 자체;
- 비밀번호로 이동하여 디바이스 잠금을 해제합니다;
- 그리고 오라클의 비밀에 대해 알아보세요.


이 접근 방식의 가장 큰 장점은 하드웨어 수준에서 단일 장애 지점이 없다는 것입니다. 공격자가 Jade에 액세스하는 경우 키를 추출하려면 Jade와 오라클을 동시에 손상시켜야 하기 때문입니다. 또한 이 모델은 Jade Plus가 완전히 오픈 소스이기 때문에 예를 들어 Ledger에서 사용되는 것과 같은 실제 물리적 보안 Elements 사용과 관련된 제약을 피할 수 있다는 것을 의미합니다.


이 시스템의 단점은 제이드 플러스의 사용이 블록스트림에서 관리하는 오라클에 의존한다는 것입니다. 이 오라클에 액세스할 수 없게 되면 더 이상 PIN으로 Hardware Wallet을 직접 사용할 수 없습니다. 그러나 "*무상태*" 모드에서 제이드 플러스에 입력할 수 있는 복구 문구를 사용하여 비트코인을 복구할 수 있으므로 비트코인이 손실되는 것은 아닙니다. 이러한 종속성을 피하기 위해 자체 오라클 서버를 구성하고 관리할 수도 있습니다.


seed을 관리하기 위한 또 다른 옵션은 Jade Plus에 등록하지 않는 것입니다. 이 경우 Jade는 서명 장치로만 사용됩니다. 초기화하는 동안 복구 문구를 단어로 저장하는 일반적인 방법 외에도 직접 생성한 QR 코드로도 저장할 수 있습니다. 이렇게 하면 Wallet을 사용할 때마다 Jade의 카메라를 사용하여 seed을 가져올 수 있습니다. 이 옵션은 보안 전략에 따라 고급 사용자에게는 흥미로운 옵션이 될 수 있지만, QR 코드로도 누군가가 자금을 훔칠 수 있기 때문에 seed을 저장하고 보호하는 데 주의해야 합니다. 이 튜토리얼에서 이 옵션을 살펴볼 예정이지만 필수 옵션은 아닙니다.


## 제이드 플러스 개봉하기


제이드 플러스를 받으면 상자와 Seal의 상태가 양호한지 확인하여 패키지가 개봉되지 않았는지 확인하세요.


![JADE-PLUS-SPARROW](assets/fr/02.webp)


상자에서 찾을 수 있습니다:




- 르 제이드 플러스;
- USB-C 케이블;
- Mnemonic 문구를 단어 또는 "*CompactSeedQR*"로 기록할 수 있는 카드입니다;
- 몇 가지 사용 지침 ;
- 코드;
- 스티커 몇 개.


![JADE-PLUS-SPARROW](assets/fr/03.webp)


기기에는 4개의 탐색 버튼이 있습니다:




- 오른쪽 하단의 버튼을 누르면 Jade가 켜집니다;
- 기기 전면의 큰 버튼은 항목을 선택하는 데 사용됩니다;
- 상단에 있는 두 개의 작은 버튼으로 왼쪽과 오른쪽을 탐색할 수 있습니다;
- 디바이스 상단에 있는 두 개의 버튼을 동시에 클릭하여 항목을 선택할 수도 있습니다.


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## 새 Bitcoin Wallet 설정하기


시작 버튼을 클릭합니다.


![JADE-PLUS-SPARROW](assets/fr/05.webp)


"*설정 옥*"을 클릭합니다.


![JADE-PLUS-SPARROW](assets/fr/06.webp)


'고급 설정'을 선택합니다.


![Image](assets/fr/07.webp)


그런 다음 "*새 Wallet 만들기*"를 클릭하여 새 generate를 seed으로 만듭니다. 12단어 또는 24단어 Mnemonic 문구 중에서 선택할 수 있습니다. Wallet의 보안은 두 옵션 모두 동일하게 유지되므로 가장 간단한 옵션, 즉 12단어를 저장하는 것이 더 편리할 수 있습니다.


![Image](assets/fr/08.webp)


"*계속*" 버튼을 클릭하여 새 복구 문구를 표시합니다.


![Image](assets/fr/09.webp)


제이드 플러스는 12단어 Mnemonic 문구를 표시합니다. **이 Mnemonic은 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다. 이 문구를 소유한 사람은 제이드 플러스에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다. 12단어 문구는 제이드 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다**


상자에 동봉된 판지에 적거나, 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 베이스에 각인하여 보안을 강화하는 것이 좋습니다.


![Image](assets/fr/10.webp)


Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

물론 이 튜토리얼에서 하는 것처럼 인터넷에서 이러한 단어를 공유해서는 안 됩니다. 이 샘플 Wallet은 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다.


화면 오른쪽에 있는 화살표를 클릭하면 다음 단어가 표시됩니다.


![Image](assets/fr/11.webp)


문구를 저장하면 Jade Plus에서 확인을 요청합니다. 장치 상단의 버튼을 사용하여 순서에 따라 올바른 단어를 선택하고 중앙의 버튼을 클릭하면 다음 단어로 넘어갑니다.


![Image](assets/fr/12.webp)


그러면 두 가지 옵션이 있습니다. 소개에서 설명한 대로 seed을 디바이스에 직접 저장하고 블록스트림의 "*가상 secure element*" 보호 시스템을 사용하여 Wallet에 액세스하거나(옵션 1), seed을 QR 코드로 저장하여 사용할 때마다 스캔하는 방법(옵션 2)을 선택할 수 있습니다.


옵션 1의 경우 "*아니요*"를 선택하고 옵션 2의 경우 "*예*"를 선택합니다.


![Image](assets/fr/13.webp)


### 옵션 1: QR PIN 잠금 해제


옵션 1(CompactSeedQR: "*아니요*")을 선택한 경우 연결 방법 선택으로 바로 이동합니다. 이 튜토리얼에서는 QR코드 교환을 통해 에어 갭 모드에서 장치를 사용하고자 하므로 "*QR*"을 선택합니다.


![Image](assets/fr/27.webp)


"*계속*"을 클릭합니다.


![Image](assets/fr/28.webp)


PIN 코드는 Jade의 잠금을 해제하는 데 사용되며 무단 물리적 접근으로부터 보호합니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 관여하지 않습니다. 따라서 이 PIN 코드에 액세스할 수 없더라도 12단어 Mnemonic 문구를 소지하고 있으면 비트코인에 다시 액세스할 수 있습니다. 가능한 한 무작위로 PIN 코드를 선택하는 것이 좋습니다. 또한 이 코드를 비밀번호 관리자와 같이 제이드가 저장된 곳과 다른 곳에 저장해 두시기 바랍니다.


왼쪽과 오른쪽 버튼을 사용하여 숫자를 스크롤하고 가운데 버튼을 눌러 각 숫자를 확인한 다음, Jade에서 6자리 PIN 코드를 선택합니다.


![Image](assets/fr/29.webp)


비밀번호를 다시 한 번 확인합니다.


![Image](assets/fr/30.webp)


소개에서 설명한 것처럼 seed은 제이드 플러스에 암호화되어 저장됩니다. 암호를 해독하려면 을 제공해야 합니다:




- 유효한 PIN 코드(방금 설정한 것) ;
- 블록스트림이 관리하는 오라클의 비밀.


이 고급 튜토리얼에서는 Sparrow wallet을 사용하여 Bitcoin Wallet을 관리합니다. 하지만 블록스트림의 Green Wallet 소프트웨어와 달리 Sparrow는 블록스트림 서버에 있는 오라클에 액세스할 수 없습니다. 따라서 제이드 플러스를 잠금 해제할 때마다 블록스트림의 웹사이트를 사용하여 오라클 비밀을 검색해야 합니다.


Https://jadefw.blockstream.com/pinqr/index.html 방문하기


"*QR 잠금 해제 시작*"을 클릭합니다.


![Image](assets/fr/31.webp)


제이드 플러스에서 이미 비밀번호를 선택했으므로 "*완료*"를 클릭합니다.


![Image](assets/fr/32.webp)


컴퓨터의 카메라를 사용하여 Jade 화면에 표시된 QR 코드를 스캔하세요.


![Image](assets/fr/33.webp)


다음 화면에 액세스하려면 Jade에서 확인합니다.


![Image](assets/fr/34.webp)


이제 웹사이트에 표시된 QR 코드를 스캔하여 오라클의 비밀을 검색하세요.


![Image](assets/fr/35.webp)


이제 Wallet가 생성되었으므로 다음 단계로 진행하여 "*옵션 2: CompactSeedQR*" 하위 섹션을 건너뛸 수 있습니다.


![Image](assets/fr/36.webp)


시작할 때마다 "*QR 모드*"를 클릭합니다.


![Image](assets/fr/37.webp)


"*QR PIN 잠금 해제*"를 선택합니다.


![Image](assets/fr/38.webp)


PIN 코드를 입력합니다.


![Image](assets/fr/39.webp)


그런 다음 [블록스트림 웹사이트](https://jadefw.blockstream.com/pinqr/qrpin.html)로 이동하여 오라클이 있는 Exchange QR 코드를 확인하세요.


![Image](assets/fr/40.webp)


이제 제이드의 잠금이 해제되었습니다.


![Image](assets/fr/41.webp)


### 옵션 2: CompactSeedQR


옵션 2(CompactSeedQR: "*예*"를 선택한 경우, "*예*"를 다시 클릭합니다.


![Image](assets/fr/14.webp)


"*시작*"을 클릭합니다.


![Image](assets/fr/15.webp)


제이드 플러스 상자에 제공된 QR코드 베이스를 사용할 수 있습니다. 12단어 또는 24단어 문장을 선택했는지 여부에 따라 적절한 상자를 선택합니다. 블록스트림 웹사이트(https://help.blockstream.com/hc/article_attachments/41928319071769)에서 템플릿을 인쇄할 수도 있습니다.


제이드 플러스에 QR 코드의 각 영역이 표시됩니다.


![Image](assets/fr/16.webp)


펜을 사용하여 사각형에 색을 칠하고 seed를 QR 코드로 재현합니다. 나중에 Jade Plus 카메라가 스캔할 수 있도록 정확하게 입력하세요. 화살표를 사용하여 다음 영역으로 이동합니다.


![Image](assets/fr/17.webp)


완료되면 "*완료*"를 클릭합니다.


![Image](assets/fr/18.webp)


제이드 플러스로 수제 QR 코드를 스캔하여 유효성을 확인하세요.


![Image](assets/fr/19.webp)


종이 백업이 올바르면 "*계속*"을 클릭합니다.


![Image](assets/fr/20.webp)


이 튜토리얼에서는 QR코드 스캔만을 기반으로 하는 연결 모드를 사용하므로 "*QR*"을 선택합니다.


![Image](assets/fr/21.webp)


옵션 1에서와 같이 CompactSeedQR 백업에 PIN을 추가하도록 선택할 수도 있습니다. 이렇게 하면 PIN과 블록스트림의 "가상 secure element" 시스템을 통해 Wallet에 액세스하거나 CompactSeedQR을 통해 액세스하는 두 가지 방법을 사용할 수 있습니다.


이중 비밀번호 옵션을 선택한 경우 '*PIN*'을 선택하고 옵션 1과 동일한 단계에 따라 비밀번호를 설정합니다.


CompactSeedQR만 계속 사용하려면 "*SeedQR*"을 선택합니다.


![Image](assets/fr/22.webp)


이제 Wallet이 생성되었으므로 다음 단계로 넘어갈 수 있습니다.


![Image](assets/fr/23.webp)


시작할 때마다 "*QR 모드*" 버튼을 클릭한 다음 "*Scan SeedQR*"을 클릭합니다.


![Image](assets/fr/24.webp)


디바이스의 카메라를 사용하여 저장된 seed을 QR 코드로 스캔합니다.


![Image](assets/fr/25.webp)


이제 제이드의 잠금이 해제되었습니다.


![Image](assets/fr/26.webp)


## BIP39 passphrase 추가


BIP39 passphrase은 자유롭게 선택할 수 있는 옵션 비밀번호로, Mnemonic 문구에 추가하여 Wallet 보안을 강화할 수 있습니다. 이 기능을 활성화하면 Bitcoin Wallet에 액세스하려면 Mnemonic과 passphrase이 모두 필요합니다. 둘 중 하나라도 없으면 Wallet을 복구할 수 없습니다.


제이드 플러스에서 이 옵션을 구성하기 전에 이 글을 읽고 passphrase의 이론적 작동을 완전히 이해하고 비트코인 손실로 이어질 수 있는 오류를 방지할 것을 강력히 권장합니다:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jade가 잠겨 있는 상태에서(passphrase는 잠금 해제되지 않은 상태에서만 입력 가능) "*옵션*" 메뉴에 액세스합니다.


![Image](assets/fr/42.webp)


"*BIP39 passphrase*"을 선택합니다.


![Image](assets/fr/43.webp)


"*주파수*" 옵션에서 Jade Plus가 시작될 때마다 passphrase을 입력할지 여부를 선택할 수 있습니다:




- "*비활성화*"는 passphrase 사용을 비활성화합니다;
- "*다음 로그인 전용*"을 선택하면 다음에 시작할 때 이 메뉴로 돌아가서 passphrase에 대한 요청을 활성화해야 합니다. 이 옵션을 사용하면 사용 내역을 공개하지 않을 수 있습니다;
- "*항상 물어보기*"를 사용하면 제이드가 시작될 때마다 passphrase을 체계적으로 물어보게 되어 Wallet이 passphrase으로 보호되고 있음을 알 수 있습니다.


보안 전략에 따라 옵션을 선택하세요. 개인적으로는 "*항상 질문*"을 선택합니다.


![Image](assets/fr/44.webp)


그런 다음 두 가지 방법 중 하나를 선택하여 passphrase를 입력할 수 있습니다:




- "*수동*: 가상 키보드를 사용하면 문자(대문자 및 소문자), 숫자, 기호를 한 글자씩 입력할 수 있습니다. 이는 모든 하드웨어 지갑의 표준 방식입니다;
- "*WordList*": 블록스트림이 Jade를 위해 고안한 특정 방법으로, passphrase 입력 속도를 높이고 엔트로피를 증가시킵니다. 입력하는 동안 시스템이 BIP39 목록에서 단어를 제안하여 잠금 해제가 더 쉬워집니다. 이 방법은 선택한 단어를 공백으로 구분하여 연결하여 자동으로 문장을 생성합니다(예: '포기 능력 가능').


개인적으로는 첫 번째 방법을 사용하는 것이 다른 모든 Wallet 지원에서 볼 수 있는 표준이므로 사용하는 것을 권장합니다.


![Image](assets/fr/45.webp)


그런 다음 홈 화면으로 돌아가서 평소와 같이 PIN 코드 또는 CompactSeedQR(위와 같이)을 사용하여 Wallet의 잠금을 해제할 수 있습니다. 그러면 passphrase를 입력하라는 메시지가 표시됩니다.


![Image](assets/fr/46.webp)


Jade 키보드에 입력하고 실제 미디어(종이 또는 금속)에 하나 이상의 백업을 만들어야 합니다. 이 예에서는 매우 약한 passphrase을 사용하고 있지만 모든 유형의 문자를 포함하며 충분히 긴(강력한 비밀번호처럼) 강력한 임의의 passphrase을 선택해야 합니다.


![Image](assets/fr/47.webp)


passphrase이 유효한지 확인합니다.


![Image](assets/fr/48.webp)


BIP39 암호는 대소문자와 오타에 민감하다는 점에 유의하세요. 처음에 구성한 것과 약간 다른 passphrase를 입력하는 경우, Jade는 오류를 보고하지 않지만 초기 Wallet에 있는 키가 아닌 다른 암호화 키 세트를 도출합니다.


따라서 구성할 때 화면 오른쪽 하단에 있는 마스터 키 지문을 메모해 두는 것이 중요합니다. 예를 들어, 제 passphrase `PBN`의 경우 마스터 키 지문은 `3AD1AE65`입니다.


![Image](assets/fr/49.webp)


passphrase로 Jade의 잠금을 해제할 때마다 지문이 설정할 때 입력한 지문과 동일한지 확인하세요. 일치하면 passphrase가 올바르며 올바른 Bitcoin Wallet에 액세스하고 있는 것입니다. 그렇지 않다면 잘못된 Wallet를 사용하고 있는 것이므로 입력 오류가 발생하지 않도록 주의하면서 다시 시도해야 합니다.


Wallet에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub 또는 처음 받은 Address과 같은 몇 가지 참조 정보를 메모한 다음, 아직 비어 있는 상태에서 제이드 플러스에서 Wallet을 삭제하세요(`옵션 -> 장치 -> 공장 초기화`). 그런 다음 Mnemonic 문구와 passphrase의 종이 백업을 사용하여 Wallet을 복원해 보세요. 복원 후 생성된 쿠키 정보가 원래 기록했던 쿠키 정보와 일치하는지 확인하세요. 일치한다면 종이 백업이 신뢰할 수 있는 것이니 안심해도 됩니다. 테스트 복구를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Sparrow wallet에서 Wallet 구성하기


이 튜토리얼에서는 Sparrow wallet를 사용한 제이드 플러스의 고급 사용법을 소개합니다. 그러나 이 Hardware Wallet은 Liana, 쌍절곤, 스펙터, Green 및 키퍼와 같은 다른 많은 프로그램과 호환됩니다. 이러한 호환성은 연결 방식에 따라 다릅니다: USB, 블루투스 또는 QR 코드(자세한 내용은 소개의 표 참조).


아직 설치하지 않았다면 [공식 웹사이트](https://sparrowwallet.com/)에서 Sparrow wallet를 다운로드하여 컴퓨터에 설치하는 것으로 시작하세요.


![Image](assets/fr/50.webp)


설치하기 전에 소프트웨어의 진위 여부와 무결성을 반드시 확인하세요. 이를 수행하는 방법을 모르는 경우 이 튜토리얼을 참조하세요:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow wallet이 열리면 "*파일*" 탭을 클릭한 다음 "*새 Wallet*"을 클릭합니다.


![Image](assets/fr/51.webp)


Wallet의 이름을 지정한 다음 "*Wallet 만들기*"를 클릭합니다.


![Image](assets/fr/52.webp)


"*에어갭 Hardware Wallet*"를 선택합니다.


![Image](assets/fr/53.webp)


"*스캔...*" 옵션 옆의 "*제이드*"를 클릭합니다.


![Image](assets/fr/54.webp)


제이드 플러스를 잠금 해제하고, 사용 중인 경우 passphrase을 입력합니다. 그런 다음 "*옵션*" 메뉴로 이동하여 "*Wallet*"을 선택한 다음 "*Xpub 내보내기*"를 클릭합니다.


![Image](assets/fr/55.webp)


Jade는 여러 개의 QR 코드를 통해 키스토어를 표시합니다. Sparrow를 사용하여 기기에서 스캔하세요.


![Image](assets/fr/56.webp)


이제 xpub과 마스터 키 지문이 제이드 플러스에 있는 지문과 일치해야 합니다. "*적용*"을 클릭합니다.


![Image](assets/fr/57.webp)


Sparrow wallet에 대한 보안 액세스를 위해 강력한 비밀번호를 설정하세요. 이 비밀번호는 공개 키, 주소, 라벨 및 거래 내역을 무단 액세스로부터 보호합니다. 비밀번호를 잊어버리지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.


![Image](assets/fr/58.webp)


이제 Wallet가 Sparrow에서 올바르게 구성되었습니다.


![Image](assets/fr/59.webp)


## 비트코인 받기


이제 Jade Plus가 구성되었으므로 새 Bitcoin Wallet에서 첫 번째 Sats를 받을 준비가 되었습니다. 그러려면 Sparrow에서 "*수신*" 메뉴를 클릭합니다.


![Image](assets/fr/60.webp)


Sparrow은 Wallet에 첫 번째 빈 수신 Address을 표시합니다.


![Image](assets/fr/61.webp)


사용하기 전에 Jade Plus 화면에서 Bitcoin Wallet과 일치하는지 확인합니다. Jade에서 "*스캔 QR*"을 클릭한 다음 Sparrow에 표시된 Address의 QR 코드를 스캔합니다.


![Image](assets/fr/62.webp)


Jade의 화면에 표시된 Address이 Sparrow wallet에 표시된 것과 일치하는지 확인하세요. 일치하면 확인 표시를 클릭하여 계속 진행하세요.


![Image](assets/fr/63.webp)


그러면 Hardware Wallet는 이 Address이 Wallet의 일부이며 관련 개인키를 보유하고 있음을 확인합니다.


![Image](assets/fr/64.webp)


Address가 제이드에 의해 유효성이 검증되면 이제 이를 사용해 비트코인을 받을 수 있습니다. 트랜잭션이 네트워크에 브로드캐스트되면 Sparrow에 표시됩니다. 트랜잭션이 확정된 것으로 간주할 만큼 충분한 확인을 받을 때까지 기다리세요.


![Image](assets/fr/65.webp)


## 비트코인 보내기


이제 Wallet에 Sats를 몇 개 받았으니 일부도 보낼 수 있습니다. 그러려면 "*UTXO*" 메뉴를 클릭하세요.


![Image](assets/fr/66.webp)


이 트랜잭션의 입력으로 사용하려는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다.


![Image](assets/fr/67.webp)


수취인의 Address, 거래 목적을 알려주는 라벨 및 이 Address으로 송금하려는 금액을 입력합니다.


![Image](assets/fr/68.webp)


현재 시장 상황에 따라 수수료율을 조정한 다음 "*거래 생성*"을 클릭합니다.


![Image](assets/fr/69.webp)


모든 트랜잭션 매개변수가 올바른지 확인한 다음 "*서명을 위한 트랜잭션 마무리*"를 클릭합니다.


![Image](assets/fr/70.webp)


"*QR 표시*"를 클릭하면 PSBT(*Partially Signed Bitcoin Transaction*)가 표시됩니다. Sparrow은 트랜잭션을 구축했지만, 입력에 사용된 비트코인의 잠금을 해제하기 위한 서명이 아직 부족합니다. 이러한 서명은 거래에 서명하는 데 필요한 개인 키에 대한 액세스 권한을 제공하는 seed을 호스팅하는 Jade Plus에서만 수행할 수 있습니다.


![Image](assets/fr/71.webp)


Jade Plus에서 "*스캔 QR*"을 클릭하여 Sparrow에 표시된 PSBT를 스캔합니다.


![Image](assets/fr/72.webp)


배송 Address과 송금 금액이 정확한지 확인한 다음 화살표를 클릭하여 확인합니다.


![Image](assets/fr/73.webp)


수수료 금액이 선택한 금액인지 확인한 다음 Interface의 왼쪽 상단에 있는 체크 아이콘을 클릭하여 거래에 서명합니다.


![Image](assets/fr/74.webp)


Sparrow wallet에서 "*스캔 QR*"을 클릭하고 Jade에 표시된 QR 코드를 스캔합니다.


![Image](assets/fr/75.webp)


이제 서명된 트랜잭션을 Bitcoin 네트워크에서 브로드캐스트할 준비가 되었으며, Miner에 의해 블록에 포함될 것입니다. 모든 것이 정확하다면 "*거래 브로드캐스트*"를 클릭합니다.


![Image](assets/fr/76.webp)


거래가 브로드캐스트되었으며 확인을 기다리는 중입니다.


![Image](assets/fr/77.webp)


이제 QR 모드에서 제이드 플러스를 설정하고 사용하는 방법을 알게 되었습니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지 손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 공유해 주셔서 감사합니다!


더 자세히 알아보려면 Green 모바일 앱으로 블루투스를 통해 Jade Plus를 구성하는 다른 튜토리얼을 추천합니다:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0