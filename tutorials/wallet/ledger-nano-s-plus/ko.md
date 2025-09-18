---
name: Ledger Nano S Plus
description: Ledger Nano S Plus 설정 및 사용
---
![cover](assets/cover.webp)


Hardware Wallet는 Bitcoin Wallet의 개인키를 관리하고 보호하는 전용 전자 장치입니다. 인터넷에 연결된 범용 컴퓨터에 설치되는 소프트웨어 지갑(또는 Hot 지갑)과 달리 하드웨어 지갑은 개인 키를 물리적으로 격리할 수 있어 해킹과 도난의 위험을 줄여줍니다.


Hardware Wallet의 주요 목표는 기기의 기능을 최대한 최소화하여 공격 표면을 줄이는 것입니다. 공격 표면이 작다는 것은 잠재적인 공격 벡터, 즉 공격자가 비트코인에 접근하기 위해 악용할 수 있는 시스템의 약점이 적다는 의미이기도 합니다.


특히 비트코인을 절대 금액으로 보유하거나 총 자산의 비율로 보유하는 경우, Hardware Wallet을 사용하여 비트코인을 보호하는 것이 좋습니다.


하드웨어 지갑은 컴퓨터나 스마트폰의 Wallet 관리 소프트웨어와 함께 사용됩니다. 이 소프트웨어는 거래 생성을 관리하지만, 이러한 거래의 유효성을 검사하는 데 필요한 암호화 서명은 Hardware Wallet 내에서만 수행됩니다. 즉, 개인 키가 잠재적으로 취약한 환경에 노출되지 않습니다.


하드웨어 지갑은 사용자를 이중으로 보호합니다: 한편으로는 개인 키를 오프라인으로 유지하여 원격 공격으로부터 비트코인을 보호하고, 다른 한편으로는 일반적으로 키를 추출하려는 시도에 대해 더 나은 물리적 저항력을 제공합니다. 이 두 가지 보안 기준에 따라 시중에 나와 있는 다양한 모델을 판단하고 순위를 매길 수 있습니다.


이 튜토리얼에서는 이러한 솔루션 중 하나인 **Ledger 나노 S 플러스**에 대해 알아볼 것을 제안합니다.


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Ledger 나노 S 플러스 소개


Ledger 나노 S 플러스는 프랑스 회사 Ledger에서 생산한 Hardware Wallet로, 79유로에 판매되고 있습니다.


![NANO S PLUS LEDGER](assets/notext/02.webp)


Nano S Plus에는 하드웨어에 대한 물리적 공격으로부터 고급 보호 기능을 제공하는 CC EAL6+ 인증 칩("*secure element*")이 장착되어 있습니다. 화면과 버튼은 이 칩으로 직접 제어됩니다. 이 칩의 코드가 오픈 소스가 아니기 때문에 이 구성 요소의 무결성에 대한 특정 신뢰가 필요하다는 비판이 종종 제기됩니다. 그럼에도 불구하고 이 요소는 독립적인 전문가의 감사를 받습니다.


사용 측면에서 Ledger 나노 S 플러스는 유선 USB-C 연결을 통해서만 작동합니다.


예를 들어 Ledger은 Taproot이나 미니스크립트와 같은 새로운 Bitcoin 기능을 항상 매우 빠르게 채택한다는 점에서 경쟁사들과 차별화됩니다.

테스트한 결과, Ledger 나노 S 플러스는 뛰어난 엔트리급 Hardware Wallet라는 것을 알게 되었습니다. 합리적인 가격에 높은 수준의 보안을 제공합니다. 같은 가격대의 다른 장치에 비해 가장 큰 단점은 펌웨어 코드가 오픈 소스가 아니라는 사실입니다. 또한 나노 S 플러스의 화면은 Ledger 플렉스나 콜드카드 Q1과 같은 더 비싼 모델에 비해 상대적으로 작습니다. 그럼에도 불구하고 Interface은 매우 잘 설계되어 있어 버튼이 2개이고 화면이 작지만 BIP39 passphrase과 같은 고급 기능을 포함하여 사용하기 쉽습니다. Ledger 나노 S 플러스에는 배터리, 에어 갭 연결, 카메라, 마이크로 SD 포트가 없지만 이 가격대에서 이는 매우 정상입니다.


제 생각에는 Ledger 나노 S 플러스는 Bitcoin Wallet을 보호하는 데 좋은 옵션이며 초보자와 중급 사용자 모두에게 적합합니다. 하지만 이 가격대에서는 거의 동일한 옵션을 제공하는 Trezor Safe 3를 개인적으로 선호합니다. 제가 보기에 Trezor의 장점은 secure element의 관리입니다. Mnemonic 문구와 키는 오픈 소스 코드로만 관리되지만 여전히 칩 보호의 이점을 누릴 수 있습니다. 트레저의 단점은 Ledger과 달리 새로운 기능을 구현하는 속도가 매우 느리다는 점입니다.


## Ledger 나노 S 플러스는 어떻게 구매하나요?


Ledger 나노 S 플러스는 [공식 웹사이트](https://shop.Ledger.com/products/Ledger-nano-s-plus)에서 구매할 수 있습니다. 오프라인 매장에서 구매하려면 [공인 리셀러 목록](https://www.Ledger.com/reseller)에서도 Ledger 웹사이트를 통해 확인할 수 있습니다.


## 전제 조건


Ledger 나노를 수령한 후 가장 먼저 포장이 개봉되지 않았는지 확인해야 합니다. 포장이 손상되었다면 Hardware Wallet이 손상되어 정품이 아닐 수 있습니다.


상자를 열면 상자 안에 다음 항목이 들어 있습니다:


- Ledger 나노 S 플러스;
- USB-C to USB-A 케이블;
- 사용 설명서;
- Mnemonic 문구를 적을 수 있는 카드입니다.


이 튜토리얼에는 2개의 소프트웨어 애플리케이션이 필요합니다: Ledger을 초기화하기 위한 Ledger Live와 Bitcoin Wallet을 관리하기 위한 Sparrow wallet입니다. 공식 웹사이트에서 [Ledger Live](https://www.Ledger.com/Ledger-live) 및 [Sparrow wallet](https://sparrowwallet.com/download/)를 다운로드하세요.


![NANO S PLUS LEDGER](assets/notext/03.webp)

이 두 소프트웨어 프로그램의 경우, 컴퓨터에 설치하기 전에 (GnuPG를 통해) 진위 여부와 (Hash을 통해) 무결성을 모두 확인할 것을 강력히 권장합니다. 이 작업을 수행하는 방법을 잘 모르겠다면 이 다른 튜토리얼을 참조하세요:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Ledger 나노를 초기화하는 방법은 무엇인가요?


Nano를 Ledger Live 및 Sparrow wallet이 설치된 컴퓨터에 연결합니다. Ledger에서 탐색하려면 왼쪽 버튼을 사용하여 왼쪽으로 이동하고 오른쪽 버튼을 사용하여 오른쪽으로 이동합니다. 옵션을 선택하거나 확인하려면 두 버튼을 동시에 누릅니다.


![NANO S PLUS LEDGER](assets/notext/04.webp)


다양한 소개 페이지를 스크롤한 다음 2개의 버튼을 클릭하여 시작하세요.


![NANO S PLUS LEDGER](assets/notext/05.webp)


"*새 디바이스로 설정*" 옵션을 선택합니다.


![NANO S PLUS LEDGER](assets/notext/06.webp)


Ledger의 잠금을 해제하는 데 사용할 PIN 코드를 선택합니다. 따라서 무단 물리적 액세스로부터 보호할 수 있습니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 사용되지 않습니다. 따라서 이 PIN 코드에 액세스할 수 없더라도 24단어 Mnemonic 문구가 있으면 비트코인에 다시 액세스할 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/07.webp)


가능한 한 무작위로 8자리 PIN을 선택하는 것이 좋습니다. 또한 이 코드를 Ledger Nano S Plus가 저장된 곳과 다른 곳(예: 비밀번호 관리자)에 저장하세요.


버튼을 사용하여 숫자 위로 이동한 다음 두 버튼을 동시에 클릭하여 각 숫자를 선택합니다.


![NANO S PLUS LEDGER](assets/notext/08.webp)


비밀번호를 한 번 더 입력하여 확인합니다.


![NANO S PLUS LEDGER](assets/notext/09.webp)


나노는 복구 문구를 관리하는 방법에 대한 지침을 제공합니다.


**이 Mnemonic 문구는 모든 비트코인에 대한 완전하고 무제한적인 액세스를 제공합니다**. 이 문구를 소유한 사람은 Ledger에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다. 24개의 단어로 구성된 이 문구를 사용하면 Ledger 나노의 분실, 도난 또는 손상 시 비트코인에 대한 액세스를 복원할 수 있습니다. 따라서 안전한 장소에 신중하게 저장하고 보관하는 것이 매우 중요합니다.


Ledger과 함께 제공되는 판지 종이에 적어두거나 화재, 홍수 또는 붕괴의 위험으로부터 보호하기 위해 스테인리스 스틸 매체에 각인하여 더욱 안전하게 보호할 것을 권장합니다.


오른쪽 버튼을 클릭하여 이 지침을 찾아보고 페이지를 건너뛸 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/10.webp)

Ledger은 난수 생성기를 사용하여 Mnemonic 문구를 생성합니다. 이 작업을 하는 동안 다른 사람이 지켜보고 있지 않은지 확인하세요. Ledger이 제공하는 문구를 원하는 물리적 매체에 적습니다. 보안 전략에 따라 이 문구를 여러 장 복사하는 것을 고려할 수도 있습니다(단, 중요한 것은 분할하지 말아야 한다는 점입니다). 단어에 번호를 매기고 순차적인 순서를 유지하는 것이 중요합니다.

***이 튜토리얼에서 설명하는 것과는 달리 인터넷에서 이러한 단어를 절대 공유해서는 안 됩니다. 이 예제 Wallet는 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다


![NANO S PLUS LEDGER](assets/notext/11.webp)


다음 단어로 이동하려면 오른쪽 버튼을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/12.webp)


모든 단어가 메모되면 2개의 버튼을 클릭하여 다음 단계로 이동합니다.


![NANO S PLUS LEDGER](assets/notext/13.webp)


"*복구 문구 확인*" 버튼 2개를 클릭한 다음 Mnemonic 문구의 단어를 순서대로 선택하여 올바르게 메모했는지 확인합니다. 왼쪽과 오른쪽 버튼을 사용해 옵션 사이를 탐색한 다음 2개의 버튼을 클릭하여 올바른 단어를 선택합니다. 24번째 단어까지 이 절차를 계속합니다.


![NANO S PLUS LEDGER](assets/notext/14.webp)


확인하려는 문구가 이전 단계에서 Ledger가 제공한 문구와 정확히 일치하면 계속 진행해도 됩니다. 그렇지 않은 경우 Mnemonic 문구의 물리적 백업이 잘못되었음을 나타내므로 프로세스를 다시 시작해야 합니다.


![NANO S PLUS LEDGER](assets/notext/15.webp)


이제 Ledger Nano S Plus에 seed가 올바르게 생성되었습니다. 이 Bitcoin에서 새로운 Wallet을 생성하기 전에 장치 설정을 함께 살펴봅시다.


## Ledger의 설정을 어떻게 수정하나요?


설정에 액세스하려면 2개의 버튼을 몇 초간 길게 누릅니다.


![NANO S PLUS LEDGER](assets/notext/16.webp)


"*설정*" 메뉴를 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/17.webp)


그리고 "*일반*"을 선택합니다.


![NANO S PLUS LEDGER](assets/notext/18.webp)


"*언어*" 메뉴에서 표시 언어를 변경할 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/19.webp)


"*밝기*" 메뉴에서 화면 밝기를 조정할 수 있습니다. 나머지 일반 설정은 현재로서는 관심이 없습니다.


![NANO S PLUS LEDGER](assets/notext/20.webp)


이제 '*보안*' 설정 섹션으로 이동합니다.


![NANO S PLUS LEDGER](assets/notext/21.webp)


"*비밀번호 변경*"을 통해 비밀번호를 변경할 수 있습니다.

![NANO S PLUS LEDGER](assets/notext/22.webp)

"*passphrase*"을 사용하면 BIP39 passphrase을 설정할 수 있습니다. passphrase은 복구 문구와 결합하여 Wallet에 추가적인 Layer의 보안을 제공하는 선택적 비밀번호입니다.


![NANO S PLUS LEDGER](assets/notext/23.webp)


현재 Wallet은 24개의 단어로 구성된 Mnemonic 구문에서 생성됩니다. 이 복구 구문은 분실 시 Wallet의 모든 키를 복원할 수 있기 때문에 매우 중요합니다. 그러나 이는 단일 장애 지점(SPOF)을 구성합니다. 이 문구가 손상되면 비트코인이 위험에 처하게 됩니다. 이것이 바로 passphrase가 필요한 이유입니다. 임의로 선택할 수 있는 선택적 암호로, Wallet의 보안을 강화하기 위해 Mnemonic 문구에 추가할 수 있습니다.


passphrase을 PIN 코드와 혼동해서는 안 됩니다. 이는 암호화 키를 생성하는 데 중요한 역할을 합니다. Mnemonic 구문과 함께 작동하여 키가 생성되는 seed을 변경합니다. 따라서 누군가 24단어 구문을 알아내더라도 passphrase이 없으면 자금에 액세스할 수 없습니다. passphrase을 사용하면 기본적으로 고유한 키를 가진 새로운 Wallet이 생성됩니다. passphrase을 조금이라도 수정하면 generate는 다른 Wallet이 됩니다.


passphrase는 비트코인의 보안을 강화하는 매우 강력한 도구입니다. 그러나 Wallet에 대한 액세스 권한을 잃지 않으려면 구현하기 전에 작동 방식을 이해하는 것이 매우 중요합니다. 그렇기 때문에 passphrase를 Ledger에 설정하려는 경우 다른 튜토리얼을 참조하시기 바랍니다:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

"*PIN 잠금*" 메뉴에서는 일정 시간 동안 사용하지 않으면 Ledger의 자동 잠금을 구성하고 활성화할 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/24.webp)


"*화면 보호기*" 메뉴에서는 Ledger Nano의 절전 모드를 조정할 수 있습니다. 화면 보호기는 절전 모드에 해당하는 "*PIN 잠금*" 옵션이 활성화되어 있지 않는 한 깨어날 때 PIN 입력이 필요하지 않습니다. 이 기능은 배터리가 장착된 Ledger Nano X 디바이스의 에너지 소비를 줄이기 위해 특히 유용합니다.


![NANO S PLUS LEDGER](assets/notext/25.webp)


마지막으로 "*장치 재설정*" 메뉴에서 Ledger을 재설정할 수 있습니다. 이 재설정은 비트코인을 보호하는 키가 포함되어 있지 않다고 확신하는 경우에만 진행해야 하며, 자금에 영구적으로 액세스할 수 없게 될 수 있습니다. 이 옵션은 빈 복구 테스트를 수행할 때 유용할 수 있지만, 이에 대해서는 나중에 자세히 설명하겠습니다.


![NANO S PLUS LEDGER](assets/notext/26.webp)

## Bitcoin 애플리케이션은 어떻게 설치하나요?


먼저 컴퓨터에서 Ledger Live 소프트웨어를 실행한 다음 Ledger 나노를 연결하고 잠금을 해제합니다. Ledger Live에서 "*내 Ledger*" 메뉴로 이동합니다. Nano에 대한 액세스 권한을 승인하라는 메시지가 표시됩니다.


![NANO S PLUS LEDGER](assets/notext/27.webp)


두 개의 버튼을 클릭하여 Ledger에서 액세스 권한을 인증합니다.


![NANO S PLUS LEDGER](assets/notext/28.webp)


먼저 Ledger Live에서 "*정품 확인*"이 표시되는지 확인합니다. 이렇게 하면 기기가 정품임을 확인할 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/29.webp)


Ledger Nano의 펌웨어가 최신 버전이 아닌 경우, Ledger Live가 자동으로 업데이트를 제안합니다. 필요한 경우 "*펌웨어 업데이트*"를 클릭한 다음 "*업데이트 설치*"를 클릭하여 설치를 시작하세요. Ledger에서 두 개의 버튼을 클릭하여 확인한 다음 설치가 진행되는 동안 기다립니다.


마지막으로 Bitcoin 애플리케이션을 추가합니다. 이렇게 하려면 Ledger Live에서 "*Bitcoin (BTC)*" 옆의 "*설치*" 버튼을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/30.webp)


애플리케이션이 Nano에 설치됩니다.


![NANO S PLUS LEDGER](assets/notext/31.webp)


이제부터는 Wallet을 정기적으로 관리하기 위해 Ledger Live 소프트웨어가 더 이상 필요하지 않습니다. 새 버전이 나오면 가끔 이 소프트웨어로 돌아가 펌웨어를 업데이트할 수 있습니다. 그 외의 모든 작업에는 Bitcoin Wallet을 효과적으로 관리할 수 있는 훨씬 더 포괄적인 도구인 Sparrow wallet를 사용할 것입니다.


![NANO S PLUS LEDGER](assets/notext/32.webp)


## Sparrow으로 새 Bitcoin Wallet을 설정하는 방법은 무엇인가요?


Sparrow wallet를 열고 소개 페이지를 건너뛰고 홈 화면으로 이동합니다. 화면 오른쪽 하단에 있는 스위치를 관찰하여 노드에 올바르게 연결되었는지 확인합니다.


![NANO S PLUS LEDGER](assets/notext/33.webp)


자체 Bitcoin 노드를 사용하는 것을 강력히 권장합니다. 이 튜토리얼에서는 Testnet를 사용하고 있기 때문에 퍼블릭 노드(노란색)를 사용하고 있지만 일반적인 사용에는 로컬 Bitcoin core(Green) 또는 원격 노드에 연결된 Electrum 서버(파란색)를 선택하는 것이 더 좋습니다.


"*파일*" 메뉴를 클릭한 다음 "*새 Wallet*"을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/34.webp)


이 Wallet의 이름을 선택한 다음 "*Wallet 만들기*"를 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/35.webp)


"*스크립트 유형*" 드롭다운 메뉴에서 비트코인을 보호하는 데 사용할 스크립트 유형을 선택합니다. "*Taproot*"를 선택하거나, 사용할 수 없는 경우 "*Native SegWit*"을 선택하는 것이 좋습니다.


![NANO S PLUS LEDGER](assets/notext/36.webp)

"*연결된 Hardware Wallet*" 버튼을 클릭합니다.

![NANO S PLUS LEDGER](assets/notext/37.webp)


아직 잠금을 해제하지 않았다면 Ledger Nano S Plus를 컴퓨터에 연결하고 PIN 코드로 잠금을 해제한 다음 Bitcoin 로고의 버튼 2개를 한 번 클릭하여 "*Bitcoin*" 애플리케이션을 엽니다.


*이 튜토리얼에서는 Bitcoin Testnet 애플리케이션을 사용하지만 절차는 Mainnet*에서도 동일하게 유지됩니다


![NANO S PLUS LEDGER](assets/notext/38.webp)


Sparrow에서 "*스캔*" 버튼을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/39.webp)


그런 다음 "*키 저장소 가져오기*"를 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/40.webp)


이제 첫 번째 계정의 확장 공개키를 포함하여 Wallet의 세부 정보를 확인할 수 있습니다. "*적용*" 버튼을 클릭하여 Wallet 생성을 완료합니다.


![NANO S PLUS LEDGER](assets/notext/41.webp)


Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 선택하세요. 이 비밀번호는 Sparrow에서 Wallet 데이터에 대한 액세스의 보안을 보장하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호하는 데 도움이 됩니다.


이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.


![NANO S PLUS LEDGER](assets/notext/42.webp)


이제 Wallet가 완성되었습니다!


![NANO S PLUS LEDGER](assets/notext/43.webp)


Wallet에서 첫 비트코인을 받기 전에 **드라이런 복구 테스트**를 수행하실 것을 강력히 권장합니다. Xpub과 같은 참조 정보를 메모한 다음 Wallet가 비어 있는 상태에서 Ledger 나노를 초기화하세요. 그 후, 종이 백업을 사용하여 Ledger에서 Wallet를 복원해 보세요. 복원 후 생성된 xpub이 처음에 기록한 것과 일치하는지 확인합니다. 일치한다면 종이 백업이 안정적이라는 것을 확신할 수 있습니다.


복구 테스트를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ledger 나노로 비트코인을 받는 방법은 무엇인가요?


"*수신*" 탭을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/44.webp)


Ledger 나노 S 플러스를 컴퓨터에 연결하고 PIN 코드로 잠금을 해제한 다음 "*Bitcoin*" 애플리케이션을 엽니다.


![NANO S PLUS LEDGER](assets/notext/45.webp)

Sparrow wallet에서 제공한 Address을 사용하기 전에 Ledger의 화면에서 이를 확인합니다. 이렇게 하면 Sparrow에 표시된 Address이 가짜가 아니며, 나중에 이 Address으로 보호된 비트코인을 사용하는 데 필요한 개인 키를 Hardware Wallet에 실제로 보유하고 있는지 확인할 수 있습니다. 이를 통해 여러 유형의 공격을 피할 수 있습니다.

이 확인을 수행하려면 "*Address 표시*" 버튼을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/46.webp)


Address에 표시된 Ledger이 Sparrow wallet에 표시된 것과 일치하는지 확인하세요. 또한 Address를 발신자에게 전달하기 직전에 이 확인을 수행하여 유효성을 확인하는 것이 좋습니다. 버튼을 사용하여 전체 Address를 볼 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/47.webp)


그런 다음 주소가 실제로 동일한 경우 "*승인*"을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/48.webp)


"*라벨*"을 추가하여 이 Address로 보호할 비트코인의 출처를 설명할 수 있습니다. 이는 UTXO를 더 잘 관리하는 데 도움이 되는 좋은 습관입니다.


![NANO S PLUS LEDGER](assets/notext/49.webp)


라벨링에 대한 자세한 내용은 이 다른 튜토리얼도 참조하세요:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

그런 다음 이 Address을 사용하여 비트코인을 받을 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/50.webp)


## Ledger 나노로 비트코인을 전송하는 방법은 무엇인가요?


이제 나노 S 플러스로 보안이 설정된 Wallet에서 첫 번째 Sats을 받았으니 이제 사용할 수도 있습니다! Ledger을 컴퓨터에 연결하고 잠금을 해제하고 Sparrow wallet을 실행한 다음 "*송금*" 탭으로 이동하여 새 트랜잭션을 생성합니다.


![NANO S PLUS LEDGER](assets/notext/51.webp)


"*Coin 제어*"를 수행하려면, 즉 트랜잭션에서 사용할 UTXO를 구체적으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하고자 하는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭의 동일한 화면으로 리디렉션되지만, 트랜잭션에 대해 이미 UTXO가 선택된 상태로 표시됩니다.


![NANO S PLUS LEDGER](assets/notext/52.webp)


목적지 Address를 입력합니다. "*+ 추가*" 버튼을 클릭하여 여러 주소를 입력할 수도 있습니다.


![NANO S PLUS LEDGER](assets/notext/53.webp)


이 지출의 목적을 기억하기 위해 "*라벨*"을 표시하세요.


![NANO S PLUS LEDGER](assets/notext/54.webp)


이 Address으로 송금할 금액을 선택합니다.


![NANO S PLUS LEDGER](assets/notext/55.webp)


현재 시장에 따라 거래 수수료율을 조정합니다.


![NANO S PLUS LEDGER](assets/notext/56.webp)

트랜잭션의 모든 설정이 올바른지 확인한 다음 "*거래 생성*"을 클릭합니다.

![NANO S PLUS LEDGER](assets/notext/57.webp)


모든 것이 괜찮아 보이면 "*서명을 위한 거래 마무리*"를 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/58.webp)


"*서명*"을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/59.webp)


Ledger Nano S Plus 옆의 "*서명*"을 클릭합니다.


![NANO S PLUS LEDGER](assets/notext/60.webp)


Ledger 화면에서 수신자의 Address 수신자, 송금 금액, 수수료 금액 등 거래 설정을 확인합니다.


![NANO S PLUS LEDGER](assets/notext/61.webp)


모든 것이 괜찮아 보이면 "*거래 서명*"의 두 버튼을 눌러 서명합니다.


![NANO S PLUS LEDGER](assets/notext/62.webp)


이제 트랜잭션이 서명되었습니다. 모든 것이 정상인지 다시 확인한 다음 "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.


![NANO S PLUS LEDGER](assets/notext/63.webp)


Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.


![NANO S PLUS LEDGER](assets/notext/64.webp)


이제 Sparrow wallet와 함께 Ledger 나노 S 플러스의 기본 사용법을 익히셨습니다! 향후 튜토리얼에서는 Ledger을 Liana와 함께 사용하여 미니스크립트를 활용하는 방법을 살펴보겠습니다.


이 튜토리얼이 도움이 되었다면 아래에 좋아요를 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


Ledger Flex에 대한 전체 튜토리얼도 확인해 보시기 바랍니다:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a