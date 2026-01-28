---
name: Ledger Flex
description: Ledger Flex 설정 및 사용
---
![cover](assets/cover.webp)


![video](https://youtu.be/V3wnS9_Ieyc)


Hardware Wallet는 Bitcoin Wallet의 개인키를 관리하고 보호하는 전용 전자 장치입니다. 인터넷에 연결된 범용 컴퓨터에 설치되는 소프트웨어 지갑(또는 Hot 지갑)과 달리 하드웨어 지갑은 개인 키를 물리적으로 격리할 수 있어 해킹과 도난의 위험을 줄여줍니다.


Hardware Wallet의 주요 목표는 장치의 기능을 최소화하여 공격 표면을 줄이는 것입니다. 공격 표면이 적다는 것은 잠재적인 공격 벡터, 즉 공격자가 비트코인에 접근하기 위해 악용할 수 있는 시스템의 취약점이 적다는 의미이기도 합니다.


특히 비트코인을 절대 금액으로 보유하거나 총 자산의 비율로 보유하는 경우, Hardware Wallet을 사용하여 비트코인을 보호하는 것이 좋습니다.


하드웨어 지갑은 컴퓨터나 스마트폰의 Wallet 관리 소프트웨어와 함께 사용됩니다. 이 소프트웨어는 트랜잭션 생성을 관리하지만, 트랜잭션의 유효성을 검사하는 데 필요한 암호화 서명은 Hardware Wallet 내에서만 수행됩니다. 즉, 개인 키가 잠재적으로 취약한 환경에 노출되지 않습니다.


하드웨어 지갑은 사용자를 이중으로 보호합니다: 한편으로는 개인 키를 오프라인으로 유지하여 원격 공격으로부터 비트코인을 보호하고, 다른 한편으로는 일반적으로 키를 추출하려는 시도에 대해 더 나은 물리적 저항력을 제공합니다. 이 두 가지 보안 기준에 따라 시중에 나와 있는 다양한 모델을 판단하고 순위를 매길 수 있습니다.


이 튜토리얼에서는 이러한 솔루션 중 하나인 **Ledger Flex**에 대해 알아볼 것을 제안합니다.


![LEDGER FLEX](assets/notext/01.webp)


## Ledger 플렉스 소개


Ledger Flex는 프랑스 회사 Ledger에서 생산한 Hardware Wallet로, 249유로에 판매되고 있습니다.


![LEDGER FLEX](assets/notext/02.webp)


흑백 디스플레이 기술인 대형 E Ink 터치스크린이 특징입니다. 이는 전자 리더기에서 볼 수 있는 것과 동일한 기술입니다. E Ink 화면은 밝은 햇빛 아래에서도 선명하고 가독성 있는 디스플레이를 제공하며, 화면이 정지된 상태에서는 에너지를 거의 소비하지 않거나 전혀 소비하지 않습니다. 흑백 안료 입자가 포함된 마이크로캡슐을 사용하는 방식으로 작동합니다. 전하가 가해지면 흑백 입자가 화면 표면으로 이동하여 텍스트나 이미지를 형성할 수 있습니다.

Ledger Flex에는 CC EAL6+ 인증을 받은 "secure element" 칩이 장착되어 있어 하드웨어에 대한 물리적 공격으로부터 고급 보호 기능을 제공합니다. 화면은 이 칩에 의해 직접 제어됩니다. 이 칩의 코드가 오픈 소스가 아니기 때문에 이 구성 요소의 무결성에 대한 일정 수준의 신뢰가 필요하다는 비판이 있습니다. 그러나 이 요소는 독립적인 전문가의 감사를 받습니다.


사용 측면에서 Ledger Flex는 여러 가지 연결 옵션을 제공합니다: 블루투스, USB-C, NFC. 대형 화면으로 거래 내역을 쉽게 확인할 수 있습니다. 또한 Ledger은 미니스크립트와 같은 새로운 Bitcoin 기능을 빠르게 채택하여 경쟁사 제품들과 차별화됩니다.


테스트 후 제품의 품질에 깊은 인상을 받았습니다. 사용자 경험도 훌륭하고 장치도 직관적입니다. 훌륭한 Hardware Wallet입니다. 그러나 제 생각에는 두 가지 주요 단점이 있습니다. 칩의 코드를 확인할 수 없다는 점과 물론 경쟁사보다 훨씬 높은 가격입니다. 비교를 위해 Foundation의 가장 고급 모델은 199달러, Coinkite는 219.99달러에 판매되며, 대형 터치스크린이 장착된 최신 Trezor는 169유로에 제공됩니다.


## Ledger 플렉스는 어떻게 구매하나요?


Ledger Flex는 [공식 웹사이트](https://shop.Ledger.com/pages/Ledger-flex)에서 구매할 수 있습니다. 오프라인 매장에서 구매하려면 Ledger 웹사이트에서 [공인 리셀러 목록](https://www.Ledger.com/reseller)을 확인할 수도 있습니다.


## 전제 조건


Ledger Flex를 받은 후 첫 번째 단계는 포장이 개봉되지 않았는지 확인하는 것입니다.


![LEDGER FLEX](assets/notext/03.webp)


Ledger의 포장에는 2개의 밀봉 스트립이 포함되어 있어야 합니다. 이 스트립이 없거나 손상된 경우 Hardware Wallet가 손상되었음을 의미하며 정품이 아닐 수 있습니다.


![LEDGER FLEX](assets/notext/04.webp)


상자를 열면 상자 안에 다음 항목이 들어 있습니다:


- Ledger Flex;
- USB-C 케이블;
- 사용 설명서;
- Mnemonic 문구를 적을 수 있는 카드입니다.


![LEDGER FLEX](assets/notext/05.webp)


이 튜토리얼에는 두 가지 소프트웨어가 필요합니다: Ledger Flex를 초기화하기 위한 Ledger Live와 Bitcoin Wallet를 관리하기 위한 Sparrow wallet입니다. 공식 웹사이트에서 [Ledger Live](https://www.Ledger.com/Ledger-live) 및 [Sparrow wallet](https://sparrowwallet.com/download/)을 다운로드하세요.


![LEDGER FLEX](assets/notext/06.webp)

다운로드한 소프트웨어의 진위 여부와 무결성을 확인하는 방법에 대한 튜토리얼을 곧 제공할 예정입니다. Ledger Live 및 Sparrow의 경우 여기에서 확인하실 것을 강력히 권장합니다.

## Ledger 라이브에서 Ledger Flex를 초기화하는 방법은 무엇인가요?


오른쪽 버튼을 몇 초간 눌러 Ledger Flex를 켭니다.


![LEDGER FLEX](assets/notext/07.webp)


다양한 소개 페이지를 스크롤하세요.


![LEDGER FLEX](assets/notext/08.webp)


"*Ledger 라이브 없이 설정*" 옵션을 선택한 다음 "*Ledger 라이브 건너뛰기*" 버튼을 클릭합니다.


![LEDGER FLEX](assets/notext/09.webp)


그러면 Ledger의 이름을 선택하라는 메시지가 표시됩니다. "*이름 설정*"을 클릭한 다음 원하는 이름을 입력합니다.


![LEDGER FLEX](assets/notext/10.webp)


Ledger의 잠금을 해제하는 데 사용할 디바이스의 PIN 코드를 선택합니다. 따라서 무단 물리적 액세스로부터 기기를 보호할 수 있습니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 사용되지 않습니다. 따라서 이 PIN 코드에 액세스할 수 없더라도 24단어 Mnemonic 문구가 있으면 비트코인에 다시 액세스할 수 있습니다.


가능한 한 무작위로 8자리 PIN 코드를 선택하는 것이 좋습니다. 또한 이 코드를 Ledger Flex가 저장된 곳과 다른 곳(예: 비밀번호 관리자)에 저장하세요.


![LEDGER FLEX](assets/notext/11.webp)


비밀번호를 한 번 더 입력하여 확인합니다.


![LEDGER FLEX](assets/notext/12.webp)


그러면 기존 Wallet을 복구할지 아니면 새로 만들지 선택하라는 메시지가 표시됩니다. 이 튜토리얼에서는 처음부터 새 Wallet을 만드는 방법을 다루므로 "*새 Ledger로 설정*" 옵션을 선택하여 새 Mnemonic 문구를 generate로 설정합니다.


![LEDGER FLEX](assets/notext/13.webp)


Flex에서 복구 문구 관리 방법에 대한 지침을 제공합니다.


**이 Mnemonic 문구는 모든 비트코인에 대한 완전하고 제한 없는 액세스를 제공합니다**. 이 문구를 소유한 사람은 Ledger에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다. 24개의 단어로 구성된 이 문구를 통해 Ledger 플렉스의 분실, 도난, 손상 시 비트코인에 대한 액세스를 복원할 수 있습니다. 따라서 안전한 장소에 신중하게 저장하고 보관하는 것이 매우 중요합니다.


Ledger과 함께 제공되는 판지 종이에 적어두거나 화재, 홍수 또는 붕괴의 위험으로부터 보호하기 위해 스테인리스 스틸 매체에 각인하여 보안을 강화하는 것이 좋습니다.


화면을 터치하여 이러한 지침을 탐색하고 페이지를 건너뛸 수 있습니다.


![LEDGER FLEX](assets/notext/14.webp)

Ledger은 난수 생성기를 사용하여 Mnemonic 문구를 생성합니다. 이 작업을 하는 동안 자신을 관찰하고 있지 않은지 확인하세요. Ledger이 제공하는 단어를 원하는 물리적 매체에 적습니다. 보안 전략에 따라 이 문구를 여러 장 복사하는 것도 고려할 수 있습니다(단, 가장 중요한 것은 분할하지 말아야 한다는 점입니다). 단어에 번호를 매기고 순차적인 순서를 유지하는 것이 중요합니다.

***이 튜토리얼에서 설명하는 것과는 달리 인터넷에서 이러한 단어를 공유해서는 안 됩니다. 이 예제 Wallet은 Testnet에서만 사용되며 튜토리얼이 끝날 때 삭제됩니다 ***


![LEDGER FLEX](assets/notext/15.webp)


다음 단어 그룹으로 이동하려면 "*다음*" 버튼을 클릭합니다. 모든 단어를 메모했으면 "*완료*" 버튼을 클릭하여 다음 단계로 진행합니다.


![LEDGER FLEX](assets/notext/16.webp)


"*확인 시작*" 버튼을 클릭한 다음 Mnemonic 문구에서 단어를 순서대로 선택하여 올바르게 메모했는지 확인합니다. 24번째 단어까지 이 절차를 계속합니다.


![LEDGER FLEX](assets/notext/17.webp)


확인하려는 문구가 이전 단계에서 Flex에서 제공한 문구와 정확히 일치하면 계속 진행해도 됩니다. 그렇지 않은 경우 Mnemonic 문구의 물리적 백업이 잘못되었으므로 프로세스를 다시 시작해야 한다는 의미입니다.


![LEDGER FLEX](assets/notext/18.webp)


이제 Ledger Flex에 seed이 올바르게 생성되었습니다. 이 Bitcoin에서 새로운 Wallet를 생성하기 전에 장치 설정을 함께 살펴봅시다.


## Ledger의 설정을 어떻게 수정하나요?


Ledger을 잠그고 잠금 해제하려면 측면 버튼을 누릅니다. 그러면 이전 단계에서 설정한 PIN 코드를 입력하라는 메시지가 표시됩니다.


![LEDGER FLEX](assets/notext/19.webp)


설정에 액세스하려면 디바이스 왼쪽 하단에 있는 톱니바퀴 기호를 클릭합니다.


![LEDGER FLEX](assets/notext/20.webp)


"*이름*" 메뉴에서 Ledger의 이름을 변경할 수 있습니다.


![LEDGER FLEX](assets/notext/21.webp)


"*이 Ledger에 관하여*"에서 Flex에 대한 정보를 확인할 수 있습니다.


![LEDGER FLEX](assets/notext/22.webp)


"*잠금 화면*" 메뉴에서 "*잠금 화면 사진 사용자 지정*"을 선택해 잠금 화면에 표시되는 이미지를 변경할 수 있습니다. 기기의 E Ink 화면 기술 덕분에 배터리 소모 없이 화면을 계속 켤 수 있습니다. E Ink 화면은 정적인 이미지를 유지하기 위해 에너지를 사용하지 않습니다. 그러나 디스플레이가 변경되는 동안에는 에너지를 소비합니다.

"*자동 잠금*" 하위 메뉴에서는 일정 시간 동안 사용하지 않으면 Ledger의 자동 잠금을 구성하고 활성화할 수 있습니다.

![LEDGER FLEX](assets/notext/23.webp)


"*사운드*" 메뉴에서는 Flex의 사운드를 켜거나 끌 수 있습니다. 그리고 "언어" 메뉴에서는 표시 언어를 변경할 수 있습니다.


![LEDGER FLEX](assets/notext/24.webp)


오른쪽 화살표를 클릭하면 다른 설정에 액세스할 수 있습니다. "*비밀번호 변경*"을 클릭하면 비밀번호를 변경할 수 있습니다.


![LEDGER FLEX](assets/notext/25.webp)


'*블루투스*' 및 '*NFC*' 메뉴에서 이러한 통신을 관리할 수 있습니다.


![LEDGER FLEX](assets/notext/26.webp)


"*배터리*"에서는 특히 Ledger의 자동 종료를 설정할 수 있습니다.


![LEDGER FLEX](assets/notext/27.webp)


"*고급*" 섹션에서는 보다 정교한 보안 설정에 액세스할 수 있습니다. 보안을 강화하려면 "*PIN 셔플*" 옵션을 활성화하는 것이 좋습니다. 또한 이 메뉴에서 BIP39 passphrase을 구성할 수 있습니다.


![LEDGER FLEX](assets/notext/28.webp)


passphrase는 복구 문구와 결합하여 Wallet에 추가적인 Layer 보안을 제공하는 옵션 비밀번호입니다.


현재 Wallet는 24개의 단어로 구성된 Mnemonic 구문에서 생성됩니다. 이 복구 구문은 분실 시 Wallet의 모든 키를 복원할 수 있기 때문에 매우 중요합니다. 그러나 이는 단일 장애 지점(SPOF)을 구성합니다. 이것이 손상되면 비트코인은 위험에 처하게 됩니다. 이것이 바로 passphrase이 필요한 이유입니다. 임의로 선택할 수 있는 선택적 암호로, Mnemonic 문구에 추가하여 Wallet의 보안을 강화합니다.


passphrase을 PIN 코드와 혼동해서는 안 됩니다. 이는 암호화 키를 생성하는 데 중요한 역할을 합니다. Mnemonic 구문과 함께 작동하여 키가 생성되는 seed를 수정합니다. 따라서 누군가 24단어 구문을 알아내더라도 passphrase이 없으면 자금에 액세스할 수 없습니다. passphrase을 사용하면 기본적으로 고유한 키를 가진 새로운 Wallet이 생성됩니다. passphrase을 조금이라도 수정하면 generate는 다른 Wallet이 됩니다.


passphrase는 비트코인의 보안을 강화하는 매우 강력한 도구입니다. 그러나 Wallet에 대한 액세스 권한을 잃지 않으려면 구현하기 전에 작동 방식을 이해하는 것이 매우 중요합니다. passphrase 사용 방법은 다른 전용 튜토리얼에서 설명해드리겠습니다.


![LEDGER FLEX](assets/notext/29.webp)


passphrase은 비트코인의 보안을 강화하는 매우 강력한 도구입니다. 그러나 Wallet에 대한 액세스 권한을 잃지 않으려면 구현하기 전에 작동 방식을 이해하는 것이 중요합니다. 그래서 전용 튜토리얼에서 모든 것을 설명해드리고 있습니다:


https://planb.academy/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

마지막으로 마지막 설정 페이지에서 Ledger를 재설정할 수 있습니다. 자금에 영구적으로 액세스하지 못할 수 있으므로 비트코인을 보호하는 키가 포함되어 있지 않다고 확신하는 경우에만 이 재설정을 진행하세요.

![LEDGER FLEX](assets/notext/30.webp)


## Bitcoin 애플리케이션은 어떻게 설치하나요?


먼저 컴퓨터에서 Ledger Live 소프트웨어를 실행한 다음 Ledger Flex를 연결하고 잠금을 해제합니다.


![LEDGER FLEX](assets/notext/31.webp)


Ledger 라이브에서 "*내 Ledger*" 메뉴로 이동합니다. Flex에 대한 액세스 권한을 승인하라는 메시지가 표시됩니다.


![LEDGER FLEX](assets/notext/32.webp)


"*허용*" 버튼을 클릭하여 Ledger에서 액세스 권한을 확인합니다.


![LEDGER FLEX](assets/notext/33.webp)


먼저, Ledger Flex의 펌웨어가 최신 버전이 아닌 경우 Ledger Live가 자동으로 업데이트를 제안합니다. 해당되는 경우 "*펌웨어 업데이트*"를 클릭한 다음 "*업데이트 설치*"를 클릭하여 설치를 시작하세요.


![LEDGER FLEX](assets/notext/34.webp)


Ledger에서 "*설치*" 버튼을 클릭한 다음 설치하는 동안 기다립니다.


![LEDGER FLEX](assets/notext/35.webp)


이제 Ledger Flex의 펌웨어가 최신 버전으로 업데이트되었습니다.


![LEDGER FLEX](assets/notext/36.webp)


원하는 경우 Ledger Flex의 잠금 화면 배경화면을 변경할 수 있습니다. 이렇게 하려면 "*추가 >*"를 클릭하세요.


![LEDGER FLEX](assets/notext/37.webp)


"*컴퓨터에서 업로드*" 버튼을 클릭하고 사진에서 배경화면을 선택합니다.


![LEDGER FLEX](assets/notext/38.webp)


이미지를 자를 수 있습니다.


![LEDGER FLEX](assets/notext/39.webp)


다양한 옵션에서 대비를 선택한 다음 "*대비 확인*"을 클릭합니다.


![LEDGER FLEX](assets/notext/40.webp)


Flex에서 "*사진 로드*" 버튼을 클릭합니다.


![LEDGER FLEX](assets/notext/41.webp)


이미지가 마음에 들면 '*유지*'를 클릭하여 잠금 화면 배경화면으로 설정합니다.


![LEDGER FLEX](assets/notext/42.webp)


마지막으로 Bitcoin 애플리케이션을 추가합니다. 이렇게 하려면 Ledger Live에서 "*Bitcoin (BTC)*" 옆의 "*설치*" 버튼을 클릭합니다.


![LEDGER FLEX](assets/notext/43.webp)


애플리케이션이 Flex에 설치됩니다.


![LEDGER FLEX](assets/notext/44.webp)


이제부터는 Wallet을 정기적으로 관리하기 위해 Ledger Live 소프트웨어가 더 이상 필요하지 않습니다. 새 버전이 나오면 가끔씩 이 소프트웨어로 돌아가 펌웨어를 업데이트하면 됩니다. 그 외의 모든 작업에는 Bitcoin Wallet을 효율적으로 관리할 수 있는 훨씬 더 포괄적인 도구인 Sparrow wallet을 사용할 것입니다.


## Sparrow로 새 Bitcoin Wallet을 설정하는 방법은 무엇인가요?

Sparrow wallet을 열고 소개 페이지를 건너뛰고 홈 화면으로 이동합니다. 화면 오른쪽 하단에 있는 스위치를 확인하여 노드에 제대로 연결되었는지 확인합니다.

![LEDGER FLEX](assets/notext/45.webp)


자체 Bitcoin 노드를 사용하는 것을 강력히 권장합니다. 이 튜토리얼에서는 Testnet을 사용하고 있기 때문에 퍼블릭 노드(노란색)를 사용하고 있지만 일반적인 사용에는 로컬 Bitcoin core(Green) 또는 원격 노드에 연결된 Electrum 서버(파란색)를 선택하는 것이 더 좋습니다.


"*파일*" 메뉴를 클릭한 다음 "*새 Wallet*"를 클릭합니다.


![LEDGER FLEX](assets/notext/46.webp)


이 Wallet의 이름을 선택한 다음 "*Wallet 만들기*"를 클릭합니다.


![LEDGER FLEX](assets/notext/47.webp)


"*스크립트 유형*" 드롭다운 메뉴에서 비트코인을 보호하는 데 사용할 스크립트 유형을 선택합니다. "*Taproot*"를 선택하거나, 사용할 수 없는 경우 "*Native SegWit*"를 선택하는 것이 좋습니다.


![LEDGER FLEX](assets/notext/48.webp)


"*연결된 Hardware Wallet*" 버튼을 클릭합니다.


![LEDGER FLEX](assets/notext/49.webp)


Ledger Flex를 컴퓨터에 연결하고 PIN 코드로 잠금을 해제한 다음 "*Bitcoin*" 애플리케이션을 엽니다. 이 튜토리얼에서는 "*Bitcoin Testnet*" 애플리케이션을 사용하지만, Mainnet의 절차는 동일합니다.


![LEDGER FLEX](assets/notext/50.webp)


Sparrow에서 "*스캔*" 버튼을 클릭합니다.


![LEDGER FLEX](assets/notext/51.webp)


그런 다음 "*키 저장소 가져오기*"를 클릭합니다.


![LEDGER FLEX](assets/notext/52.webp)


이제 첫 번째 계정의 확장 공개키를 포함하여 Wallet의 세부 정보를 확인할 수 있습니다. "*적용*" 버튼을 클릭하여 Wallet 생성을 완료합니다.


![LEDGER FLEX](assets/notext/53.webp)


Sparrow wallet에 대한 보안 액세스를 위해 강력한 비밀번호를 선택하세요. 이 비밀번호는 Sparrow에서 Wallet 데이터에 대한 액세스의 보안을 보장하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호하는 데 도움이 됩니다.


이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.


![LEDGER FLEX](assets/notext/54.webp)


이제 Wallet이 완성되었습니다!


![LEDGER FLEX](assets/notext/55.webp)

Wallet에서 첫 비트코인을 받기 전에 드라이런 복구 테스트를 수행하실 것을 강력히 권장합니다. Xpub과 같은 참조 정보를 메모한 다음 Wallet이 비어 있는 상태에서 Ledger Flex를 초기화하세요. 그런 다음 종이 백업을 사용하여 Ledger에서 Wallet을 복원해 보세요. 복원 후 생성된 xpub이 처음에 기록한 것과 일치하는지 확인합니다. 일치한다면 종이 백업이 안정적이라는 것을 확신할 수 있습니다.


## Ledger Flex로 비트코인을 받는 방법은 무엇인가요?


"*수신*" 탭을 클릭합니다.


![LEDGER FLEX](assets/notext/56.webp)


Ledger Flex를 컴퓨터에 연결하고 PIN 코드로 잠금을 해제한 다음 "*Bitcoin*" 애플리케이션을 엽니다.


![LEDGER FLEX](assets/notext/57.webp)


Sparrow wallet에서 제공한 Address을 사용하기 전에 Ledger Flex의 화면에서 이를 확인하시기 바랍니다. 이를 통해 Sparrow에 표시된 Address이 사기가 아니며, 나중에 이 Address으로 보호된 비트코인을 사용하는 데 필요한 개인키를 Ledger가 실제로 보유하고 있는지 확인할 수 있습니다.


이 확인을 수행하려면 "*Address 표시*" 버튼을 클릭합니다.


![LEDGER FLEX](assets/notext/58.webp)


Ledger Flex에 표시된 Address이 Sparrow wallet에 표시된 것과 일치하는지 확인하세요. 또한 Address을 발신자에게 전달하기 직전에 이 확인을 수행하여 유효성을 확인하는 것이 좋습니다.


![LEDGER FLEX](assets/notext/59.webp)


"*레이블*"을 추가하여 이 Address으로 보호할 비트코인의 출처를 설명할 수 있습니다. 이는 UTXO를 더 잘 관리하는 데 도움이 되는 좋은 습관입니다.


![LEDGER FLEX](assets/notext/60.webp)


라벨링에 대한 자세한 내용은 이 다른 튜토리얼도 참조하세요:


https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

그런 다음 이 Address을 사용하여 비트코인을 받을 수 있습니다.


![LEDGER FLEX](assets/notext/61.webp)


## Ledger Flex로 비트코인을 전송하는 방법은 무엇인가요?


이제 플렉스로 보안이 설정된 Wallet에서 첫 번째 Sats을 받았으니 이제 사용할 수도 있습니다! Ledger를 컴퓨터에 연결하고 잠금을 해제하고 Sparrow wallet을 실행한 다음 "*송금*" 탭으로 이동하여 새 트랜잭션을 생성하세요.


![LEDGER FLEX](assets/notext/62.webp)


"*Coin 제어*", 즉 트랜잭션에서 소비할 UTXO를 구체적으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하고자 하는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭의 동일한 화면으로 리디렉션되지만, 트랜잭션에 대해 이미 UTXO가 선택된 상태로 표시됩니다.

![LEDGER FLEX](assets/notext/63.webp)

목적지 Address을 입력합니다. "*+ 추가*" 버튼을 클릭하여 여러 주소를 입력할 수도 있습니다.


![LEDGER FLEX](assets/notext/64.webp)


이 비용의 목적을 기억하기 위해 "*라벨*"을 표시하세요.


![LEDGER FLEX](assets/notext/65.webp)


이 Address로 송금할 금액을 선택합니다.


![LEDGER FLEX](assets/notext/66.webp)


현재 시장에 따라 거래 수수료율을 조정하세요.


![LEDGER FLEX](assets/notext/67.webp)


트랜잭션의 모든 설정이 올바른지 확인한 다음 "*거래 생성*"을 클릭합니다.


![LEDGER FLEX](assets/notext/68.webp)


모든 것이 만족스럽다면 "*서명을 위한 거래 마무리*"를 클릭합니다.


![LEDGER FLEX](assets/notext/69.webp)


"*서명*"을 클릭합니다.


![LEDGER FLEX](assets/notext/70.webp)


Ledger Flex 옆의 "*서명*"을 클릭합니다.


![LEDGER FLEX](assets/notext/71.webp)


Flex 화면에서 수취인의 Address 수신, 송금액, 수수료 금액 등 거래 설정을 확인합니다.


![LEDGER FLEX](assets/notext/72.webp)


서명하려면 '*서명하려면 길게 누르기*' 버튼을 손가락으로 누릅니다.


![LEDGER FLEX](assets/notext/73.webp)


이제 트랜잭션이 서명되었습니다. "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.


![LEDGER FLEX](assets/notext/74.webp)


Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.


![LEDGER FLEX](assets/notext/75.webp)


이제 Sparrow wallet와 함께 Ledger Flex의 기본 사용법을 익히셨습니다! 향후 튜토리얼에서는 Ledger Flex를 Liana과 함께 사용하여 미니스크립트를 활용하는 방법을 살펴보겠습니다.


이 튜토리얼이 도움이 되었다면 아래에 엄지 손가락을 올려주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!