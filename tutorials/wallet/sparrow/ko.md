---
name: Sparrow Wallet
description: Sparrow wallet 설치, 구성 및 사용
---
![cover](assets/cover.webp)


![video](https://youtu.be/yJpvfRl03Tw)


Sparrow wallet는 크레이그 로우가 개발한 자기수탁 Bitcoin Wallet 관리 소프트웨어입니다. 이 오픈 소스 소프트웨어는 다양한 기능과 직관적인 Interface로 비트코인 사용자들에게 호평을 받고 있습니다.


Sparrow을 사용하는 방법에는 두 가지가 있습니다:




- 개인 키가 PC에 저장되는 Hot Wallet과 같은 방식입니다.
- 개인 키가 Hardware Wallet에 보관되는 Cold Wallet 관리자. 이 모드에서 Sparrow은 공개 Wallet 정보만 조작하고, 자금을 추적하고, 주소를 생성하고, 트랜잭션을 생성하지만 이러한 트랜잭션을 유효하게 만들려면 Hardware Wallet 서명이 필요합니다. 따라서 Ledger Live 또는 Trezor Suite와 같은 애플리케이션을 대체할 수 있습니다.


Sparrow는 단일 서명 지갑과 다중 서명 지갑을 지원하며, 여러 지갑을 유동적으로 관리할 수 있습니다. 예를 들어 Ledger에 연결된 하나의 Wallet과 Trezor에 연결된 또 다른 Hot을 동시에 제어할 수 있습니다.


또한 이 소프트웨어는 고급 Coin 제어 기능을 제공하여 거래에 사용할 UTXO를 정확하게 선택하여 기밀성을 최적화할 수 있습니다.


연결 측면에서 Sparrow을 사용하면 일렉트럼 서버를 통해 원격으로 Bitcoin 노드에 연결하거나 Bitcoin core에 연결할 수 있습니다. 아직 자체 노드가 없는 경우 공용 노드를 사용할 수도 있습니다. 원격 연결은 Tor를 통해 이루어집니다.


## Sparrow wallet 설치


Sparrow wallet 공식 다운로드 페이지](https://sparrowwallet.com/download/)로 이동하여 운영 체제에 맞는 소프트웨어 버전을 선택합니다.


![Image](assets/fr/01.webp)


소프트웨어를 설치하기 전에 소프트웨어의 무결성과 진위 여부를 확인하는 것이 중요합니다. 이 작업을 수행하는 방법을 모르는 경우 여기에서 전체 튜토리얼을 확인할 수 있습니다:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow를 설치한 후에는 초기 설명 화면을 건너뛰고 바로 연결 관리 화면으로 이동할 수 있습니다.


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## Bitcoin 네트워크에 연결


Bitcoin 네트워크와 상호 작용하고 트랜잭션을 브로드캐스트하려면 Sparrow을 Bitcoin 노드에 연결해야 합니다. 이 연결을 설정하는 세 가지 주요 방법이 있습니다:



- 🟡 퍼블릭 노드 사용, 즉 이러한 연결을 허용하는 타사 노드에 연결합니다. 자체 Bitcoin 노드가 없는 경우 이 옵션을 사용하면 Sparrow를 빠르게 시작할 수 있습니다. 하지만 연결한 노드가 모든 트랜잭션을 볼 수 있으므로 기밀성이 손상될 수 있습니다. 키를 제어하는 것은 필수적이지만, 자체 노드를 사용하는 것이 더 좋습니다. 따라서 이 옵션은 개인 정보에 대한 위험을 인식하고 이제 막 시작하는 경우에만 사용하세요.
- 🟢 Bitcoin core 노드에 연결하기. 자체 Bitcoin core 노드가 있는 경우 Bitcoin core이 같은 컴퓨터에 설치된 경우 로컬로 또는 원격으로 Sparrow wallet에 연결할 수 있습니다.
- 🔵 일렉트럼 서버를 통한 연결. Umbrel 또는 Start9과 같은 노드 인 어 박스 솔루션의 경우처럼 Bitcoin 노드에 Electrs가 장착되어 있는 경우 Sparrow에서 원격으로 연결할 수 있습니다.


**제삼자를 신뢰할 필요성을 줄이고 기밀성을 최적화하려면 자체 노드에서 Electrs 또는 Bitcoin core를 통한 연결을 사용하는 것이 좋습니다**


### 퍼블릭 노드에 연결 🟡


퍼블릭 노드에 연결하는 방법은 매우 간단합니다. "*퍼블릭 서버*" 탭을 클릭합니다.


![Image](assets/fr/03.webp)


드롭다운 목록에서 노드를 선택합니다.


![Image](assets/fr/04.webp)


그런 다음 "*연결 테스트*"를 클릭합니다.


![Image](assets/fr/05.webp)


연결되면 Sparrow wallet의 오른쪽 하단에 노란색 체크 표시가 나타나 퍼블릭 노드에 연결되었음을 알립니다.


![Image](assets/fr/06.webp)


### Bitcoin core에 연결하기 🟢


Bitcoin 노드에 연결하는 두 번째 방법은 Sparrow을 Bitcoin core에 연결하는 것입니다. Bitcoin core이 동일한 시스템에 설치되어 있는 경우, 인증은 쿠키 파일을 통해 이루어집니다. Bitcoin core이 원격 컴퓨터에 있는 경우 `Bitcoin.conf` 파일에 정의된 비밀번호를 사용해야 합니다.


pruned Bitcoin core 노드를 사용하는 경우, 로컬에 저장된 블록 이전의 트랜잭션이 포함된 Wallet를 복원할 수 없다는 점에 유의하시기 바랍니다. 그러나 Sparrow에서 생성된 새 Wallet의 경우, pruned 노드를 사용하더라도 새 트랜잭션을 볼 수 있으므로 문제가 되지 않습니다.


Bitcoin core 노드를 구성하려면 운영 체제에 따라 다음 튜토리얼 중 하나를 참조하세요:


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Sparrow에서 "*Bitcoin core*" 탭으로 이동합니다.


![Image](assets/fr/07.webp)


**Bitcoin core 로컬 사용:**


Bitcoin core가 컴퓨터에 설치되어 있는 경우 소프트웨어 파일 중 `Bitcoin.conf` 파일을 찾습니다. 이 파일이 없는 경우 직접 만들 수 있습니다. 텍스트 편집기로 파일을 열고 다음 줄을 삽입합니다:


```ini
server=1
```


그런 다음 변경 사항을 저장합니다.


Bitcoin-QT의 Interface 그래픽을 통해 "*설정*" > "*옵션*"으로 이동하여 이 작업을 수행할 수도 있습니다 > "*옵션...*"으로 이동하여 "*RPC 서버 활성화*" 옵션을 활성화할 수도 있습니다.


이러한 변경을 수행한 후에는 소프트웨어를 다시 시작하는 것을 잊지 마세요.


![Image](assets/fr/08.webp)


그런 다음 Sparrow wallet로 돌아가서 쿠키 파일 경로를 입력합니다(운영 체제에 따라 일반적으로 `Bitcoin.conf`와 같은 폴더에 위치):


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


다른 매개변수는 기본값인 URL `127.0.0.1`과 포트 `8332`로 그대로 둔 다음 "*연결 테스트*"를 클릭합니다.


![Image](assets/fr/10.webp)


연결이 설정되었습니다. 오른쪽 하단에 Bitcoin core 노드에 연결되었음을 나타내는 Green 체크 표시가 나타납니다.


![Image](assets/fr/11.webp)


**Bitcoin core 원격 사용 시:**


동일한 네트워크에 연결된 다른 컴퓨터에 Bitcoin core를 설치한 경우, 먼저 소프트웨어 파일 중 `Bitcoin.conf` 파일을 찾습니다. 이 파일이 아직 존재하지 않는다면 직접 만들 수 있습니다. 텍스트 편집기로 이 파일을 열고 다음 줄을 추가합니다:


```ini
server=1
```


파일을 편집한 후에는 운영 체제에 맞는 폴더에 저장해야 합니다:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

이 작업은 Bitcoin-QT Interface 그래픽 Interface을 통해서도 수행할 수 있습니다. "*설정*" 메뉴로 이동한 다음 "*옵션...*"으로 이동하여 해당 상자를 체크하여 "*RPC 서버 활성화*" 옵션을 활성화합니다. Bitcoin.conf` 파일이 없는 경우, "*설정 파일 열기*"를 클릭하여 이 Interface에서 직접 생성할 수 있습니다.


![Image](assets/fr/12.webp)


로컬 네트워크에서 Bitcoin core를 호스팅하는 컴퓨터의 IP Address를 찾습니다. 이를 위해 [Angry IP Scanner](https://angryip.org/)와 같은 도구를 사용할 수 있습니다. 예를 들어 노드의 IP Address가 `192.168.1.18`이라고 가정해 보겠습니다.


Bitcoin.conf` 파일에 다음 줄을 추가하고 `rpcbind=192.168.1.18`을 설정하여 노드의 IP Address과 일치하도록 합니다.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


Bitcoin.conf` 파일에서 원격 연결을 위한 사용자 이름과 비밀번호를 추가합니다. 사용자 아이디는 `loic`으로, 비밀번호는 `my_password`로 바꿔야 합니다:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


파일을 수정하고 저장한 후 Bitcoin-QT 소프트웨어를 재시작합니다.


이제 Sparrow wallet으로 돌아갈 수 있습니다. "*사용자/패스*" 탭으로 이동합니다. Bitcoin.conf` 파일에서 구성한 사용자 이름과 비밀번호를 입력합니다. 다른 매개변수(예: URL `127.0.0.1` 및 포트 `8332`)는 기본값으로 그대로 둡니다. 그런 다음 "*연결 테스트*"를 클릭합니다.


![Image](assets/fr/15.webp)


연결이 설정되었습니다. 오른쪽 하단에 Green 체크 표시가 나타나 Bitcoin core 노드에 연결되었음을 나타냅니다.


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### 일렉트럼 서버에 연결하기 🔵


마지막 연결 옵션은 원격 일렉트럼 서버를 사용하는 것입니다. 이 방법을 사용하면 다른 기기에서 토르를 통해 노드에 연결할 수 있으며, 인덱서를 활용해 Sparrow에서 지갑을 더 빠르게 탐색할 수 있습니다. 클릭 한 번으로 일렉트럼을 설치할 수 있는 엄브렐이나 스타트나인과 같은 노드 인 어 박스 솔루션이 있는 경우 특히 적합합니다.


이렇게 하려면, 일렉트럼 서버의 Tor `.onion' Address를 받으세요. 예를 들어, 엄브렐의 경우 Electrs 애플리케이션에서 찾을 수 있습니다.


![Image](assets/fr/17.webp)


Sparrow wallet에서 "*프라이빗 일렉트럼*" 탭에 액세스합니다.


![Image](assets/fr/18.webp)


제공된 공간에 Tor Address을 입력하세요. 다른 설정은 기본값을 그대로 유지해도 됩니다. 그런 다음 "*연결 테스트*"를 클릭하세요.


![Image](assets/fr/19.webp)


연결이 확인되었습니다. 이 창을 닫으면 오른쪽 하단에 파란색 체크 표시가 나타나 일렉트럼 서버에 연결되었음을 나타냅니다.


![Image](assets/fr/20.webp)


## Hot Wallet 만들기


이제 Sparrow wallet이 Bitcoin 네트워크와 통신하도록 구성되었으므로 첫 번째 Wallet을 만들 준비가 되었습니다. 이 섹션에서는 Hot, 즉 개인 키가 컴퓨터에 저장된 Wallet을 만드는 방법을 안내합니다. 컴퓨터는 인터넷에 연결된 복잡한 기계이므로 매우 큰 공격 표면을 제공합니다. 따라서 Hot는 제한된 양의 비트코인을 보관할 때만 사용해야 합니다. 더 많은 양을 보관하려면 Hardware Wallet이 포함된 안전한 Wallet을 선택하세요. 이것이 여러분이 찾고 있는 것이라면 다음 섹션으로 건너뛰셔도 됩니다.


Hot Wallet을 생성하려면 Sparrow wallet 홈 화면에서 "*파일*" 탭을 클릭한 다음 "*새 Wallet*"을 클릭합니다.


![Image](assets/fr/21.webp)


Wallet의 이름을 입력하고 "*Wallet 만들기*"를 클릭합니다.


![Image](assets/fr/22.webp)


Interface 상단에서 "*단일 서명*" 또는 "*멀티 서명*"을 생성할지 선택할 수 있습니다 Wallet. 바로 아래에서 UTXO를 잠글 스크립트 유형을 선택합니다. 최신 표준을 사용하는 것이 좋습니다: "*Taproot (P2TR)*".


![Image](assets/fr/23.webp)


그런 다음 "*새롭거나 가져온 Software Wallet*"을 클릭합니다.


![Image](assets/fr/24.webp)


거의 모든 Bitcoin Wallet 소프트웨어에서 지원되므로 BIP39 표준을 선택합니다. 다음으로 복구 구문의 길이를 선택합니다. 현재로서는 12단어 구문으로도 충분하며, 두 가지 모두 비슷한 보안을 제공하지만 12단어 구문이 저장하기가 더 간단합니다.


![Image](assets/fr/25.webp)


"*generate 신규*" 버튼을 클릭해 Wallet의 Mnemonic 문구를 generate로 변경합니다. 이 문구를 사용하면 모든 비트코인에 제한 없이 완전히 액세스할 수 있습니다. 이 문구를 소유한 사람은 컴퓨터에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다.


이 12단어 문구는 컴퓨터 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다.


종이에 새기거나 보안을 강화하기 위해 스테인리스 스틸에 각인하여 화재, 홍수 또는 붕괴로부터 보호할 수 있습니다. Mnemonic의 매체 선택은 보안 전략에 따라 다르지만, 적당한 양이 들어 있는 따뜻한 지출용 Sparrow을 사용하는 경우에는 종이로 충분할 것입니다.


Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)


**이 튜토리얼에서는 이 단어를 인터넷에서 절대 공유해서는 안 됩니다. 이 예제 Wallet는 Testnet에서만 사용되며 튜토리얼이 끝날 때 삭제됩니다**


"*passphrase 사용*" 상자를 클릭하여 passphrase BIP39를 추가하도록 선택할 수도 있습니다. 경고: passphrase를 사용하는 것은 매우 유용할 수 있지만 작동 방식을 이해하지 못하면 매우 위험할 수 있습니다. 그렇기 때문에 이 주제에 대한 짧은 이론 기사를 읽어보실 것을 강력히 권장합니다:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Mnemonic과 passphrase을 실제 매체에 저장한 후 "*백업 확인*"을 클릭합니다.


![Image](assets/fr/27.webp)


12개의 단어를 다시 입력하여 올바르게 저장되었는지 확인한 다음 "*키 저장소 만들기*"를 클릭합니다.


![Image](assets/fr/28.webp)


그런 다음 "*키 저장소 가져오기*"를 클릭하여 Mnemonic 문구에서 generate로 Wallet 키를 가져옵니다.


![Image](assets/fr/29.webp)


"*적용*"을 클릭하여 Wallet 생성을 완료합니다.


![Image](assets/fr/30.webp)


Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 설정하세요. 비밀번호를 잊어버리지 않도록 비밀번호 관리자에 보관하는 것이 좋습니다. 이 비밀번호는 키를 생성하는 데 아무런 역할을 하지 않습니다. Sparrow wallet를 통해 Wallet에 액세스하는 데만 사용됩니다. 따라서 이 비밀번호가 없어도 Mnemonic 문구만으로도 BIP39 호환 애플리케이션에서 비트코인을 액세스하는 데 충분합니다.


![Image](assets/fr/31.webp)


이제 Hot Wallet이 생성되었습니다. Hardware Wallet를 Sparrow과 함께 사용할 계획이 없다면 이 튜토리얼의 *비트코인 받기* 섹션으로 건너뛰셔도 됩니다.


## Cold Wallet 관리하기


Sparrow wallet를 사용하는 두 번째 방법은 Hardware Wallet과 함께 Wallet 관리자로 설정하는 것입니다. 이 구성에서는 Bitcoin Wallet의 개인 키는 Hardware Wallet에 독점적으로 유지되고, Sparrow는 공개 정보에만 액세스합니다. 이 접근 방식은 개인 키가 인터넷에 연결되지 않은 보안 칩이 있는 특수 장치에 보관되어 기존 컴퓨터보다 공격 표면이 훨씬 작기 때문에 위에서 설명한 Hot 지갑보다 높은 수준의 보안을 제공합니다.


Hardware Wallet을 Sparrow에 연결하는 방법에는 크게 두 가지가 있습니다:




- 트레저 세이프 3 또는 Ledger 나노 S 플러스와 같은 보급형 모델에 일반적으로 사용되는 케이블로;
- 에어 갭 모드에서, 즉 직접 유선 연결 없이 MicroSD 카드 또는 QR 코드 Exchange을 통해 연결할 수 있습니다.


Sparrow은 이러한 모든 통신 방법을 지원하며 시중에 나와 있는 대부분의 하드웨어 지갑과 호환됩니다.


이 튜토리얼에서는 케이블이 있는 Ledger Nano S를 사용하지만 에어 갭 모드에서도 절차는 비슷합니다. Plan ₿ Network에 대한 전용 튜토리얼에서 Hardware Wallet에 대한 자세한 내용을 확인할 수 있습니다.


시작하기 전에 Hardware Wallet에 Wallet이 이미 구성되어 있는지 확인하세요. 유선 연결을 사용하는 경우 케이블을 통해 컴퓨터에 연결합니다.


소위 "*키스토어*"(Wallet을 관리하는 데 필요한 공개 정보)를 Sparrow wallet로 가져오려면 "*파일*" 탭을 클릭한 다음 "*새 Wallet*"을 클릭합니다.


![Image](assets/fr/32.webp)


Wallet의 이름을 지정하고 "*Wallet 만들기*"를 클릭합니다. 나중에 쉽게 식별할 수 있도록 Hardware Wallet의 이름을 입력하는 것이 좋습니다.


![Image](assets/fr/33.webp)


Interface 상단에서 "*단일 서명*" 또는 "*멀티 서명*" 중에서 선택합니다 Wallet. 이 예에서는 단일 서명 Wallet를 구성하겠습니다.


바로 아래에서 UTXO를 잠글 스크립트 유형을 선택합니다. Hardware Wallet에서 지원하는 경우 "*Taproot(P2TR)*"를 선택하는 것이 좋습니다.


![Image](assets/fr/34.webp)


다음으로 연결 방식에 따라 절차가 달라집니다. 에어 갭 방식을 사용하는 경우 "*에어 갭 Hardware Wallet*"을 선택합니다. 그런 다음 디바이스별 지침을 따릅니다.


![Image](assets/fr/35.webp)


제 경우처럼 케이블 연결을 사용하는 경우에는 "*연결된 Hardware Wallet*"을 선택합니다.


![Image](assets/fr/36.webp)


"*스캔*"을 클릭하여 Sparrow가 장치를 감지하도록 합니다. 디바이스가 연결되어 있고 잠금이 해제되어 있는지 확인하세요. Ledger과 같은 일부 모델의 경우 "*Bitcoin*" 애플리케이션을 열어야 감지를 활성화할 수 있습니다.


![Image](assets/fr/37.webp)


"*키 저장소 가져오기*"를 선택합니다.


![Image](assets/fr/38.webp)


"*적용*"을 클릭하여 Wallet 생성을 완료합니다.


![Image](assets/fr/39.webp)


Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 설정하세요. 이 비밀번호는 공개 키, 주소, 거래 내역을 보호합니다. 비밀번호 관리자에 저장하는 것이 좋습니다. 이 비밀번호는 키를 생성하는 데 아무런 역할을 하지 않습니다. 이 비밀번호가 없어도 BIP39 호환 소프트웨어를 통해 Mnemonic으로 비트코인에 대한 액세스를 복구할 수 있습니다.


![Image](assets/fr/40.webp)


이제 관리 Wallet가 Sparrow에 구성되었습니다.


![Image](assets/fr/41.webp)


## 비트코인 받기


이제 Wallet이 Sparrow에 설정되었으므로 비트코인을 받을 수 있습니다. "*수령*" 메뉴에 액세스하기만 하면 됩니다.


![Image](assets/fr/42.webp)


Sparrow는 Wallet에서 사용하지 않은 첫 번째 Address을 표시합니다. 이 Address에 "*라벨*"을 추가하여 나중에 이 사토시의 출처를 기억할 수 있습니다.


![Image](assets/fr/43.webp)


Hot Wallet를 사용하는 경우, 표시된 Address을 복사하거나 관련 QR 코드를 스캔하여 즉시 사용할 수 있습니다.


Hardware Wallet를 사용하는 경우, 사용하기 전에 디바이스 화면에서 Address를 확인하는 것이 매우 중요합니다. 유선 디바이스의 경우 Hardware Wallet를 연결하고 잠금을 해제한 다음 Sparrow에서 "*Address 표시*"를 클릭합니다. Hardware Wallet에 표시된 Address가 Sparrow에 표시된 것과 일치하는지 확인합니다.


![Image](assets/fr/44.webp)


Hardware Wallet 에어 갭 사용자의 경우, Address 인증은 디바이스 모델에 따라 다릅니다. 정확한 지침은 전용 Plan ₿ Network 튜토리얼을 참조하세요.


결제자가 거래를 브로드캐스트하면 '*거래*' 탭에 해당 거래가 표시되는 것을 확인할 수 있습니다. 이를 클릭하면 txid과 같은 자세한 내용을 확인할 수 있습니다.


![Image](assets/fr/45.webp)


"*주소*" 탭에서 모든 받은 편지함 주소 목록을 확인할 수 있습니다. 이미 사용되었는지 여부와 라벨이 추가되었는지 여부를 확인할 수 있습니다. *수신*" 주소는 "*수신*"을 클릭하면 Sparrow에 표시되는 주소로, 수신 결제를 위한 주소입니다. "*변경*" 주소는 거래에서 Exchange에 사용되며, 즉 입력된 UTXO 중 사용하지 않은 부분을 복구하는 데 사용됩니다.


![Image](assets/fr/46.webp)


"*UTXO*" 탭에는 모든 UTXO, 즉 보유하고 있는 Bitcoin 조각이 표시됩니다. 각 UTXO의 수량과 관련 레이블을 확인할 수 있습니다.


![Image](assets/fr/47.webp)


## 비트코인 보내기


이제 Wallet에 사토시를 몇 개 가지고 계시니, 일부를 보낼 수도 있습니다. 여러 가지 방법이 있지만, 저는 "*송금*" 메뉴로 바로 가기보다는 "*UTXOs*" 메뉴를 사용하여 코인을 더 정확하게 제어하는 것을 추천합니다(*Coin 제어*)(초보자라면 후자로도 충분할 수 있지만).


![Image](assets/fr/48.webp)


이 거래의 입력으로 사용하려는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. 이 방법을 사용하면 비용과 수령 시 적용되는 레이블에 따라 UTXO 중에서 가장 적합한 소스를 선택하여 결제의 기밀성을 최적화할 수 있습니다. 선택한 UTXO의 합계가 송금하려는 금액보다 큰지 확인하세요.


![Image](assets/fr/49.webp)


"*수취인*" 필드에 수취인의 Address을 입력합니다. 카메라 아이콘을 클릭하여 웹캠으로 Address을 스캔할 수도 있습니다. "*+추가*" 버튼을 사용하면 한 번의 거래로 여러 주소를 결제할 수 있습니다.


![Image](assets/fr/50.webp)


거래에 라벨을 추가하여 거래의 목적을 상기시킵니다. 이 레이블은 최종 Exchange과도 연결됩니다.


![Image](assets/fr/51.webp)


이 Address로 송금할 금액을 입력합니다.


![Image](assets/fr/52.webp)


현재 시장 상황에 따라 수수료율을 조정합니다. 절대 수수료 값을 입력하거나 슬라이더를 사용하여 수수료율을 조정하면 됩니다.


![Image](assets/fr/53.webp)


Interface 하단에서 "*효율성*"과 "*개인정보 보호*" 중에서 선택할 수 있습니다. 제 경우에는 UTXO을 하나만 가지고 있기 때문에 "*프라이버시*" 옵션을 사용할 수 없습니다. "*효율성*"은 일반적인 트랜잭션에 해당하며, "*프라이버시*"는 스톤월형 트랜잭션으로, 미니 CoinJoin을 시뮬레이션하여 기밀성을 강화하는 트랜잭션 구조로 체인 분석을 더 복잡하게 만듭니다.


![Image](assets/fr/54.webp)


Sparrow는 입력, 출력 및 거래 수수료를 보여주는 요약 다이어그램을 표시합니다(이 다이어그램에서 제시하는 것과는 달리 수수료는 실제로는 출력이 아닙니다). 모든 것이 만족스럽다면 "*거래 생성*"을 클릭합니다.


![Image](assets/fr/55.webp)


그러면 거래의 Elements를 자세히 설명하는 페이지로 이동합니다. 모든 정보가 정확한지 확인한 다음 "*서명을 위한 거래 마무리*"를 클릭합니다.


![Image](assets/fr/56.webp)


기본 Sighash를 유지하는 것이 중요합니다. 그 이유를 이해하려면 이 교육 과정을 살펴보고 Sighash에 대해 알아야 할 모든 것을 설명하세요:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

다음 화면에서는 사용 중인 Wallet의 유형에 따라 옵션이 달라집니다:




- Hardware Wallet 에어 갭의 경우, "*QR 표시*"를 클릭하여 장치로 서명할 수 있는 PSBT를 표시한 다음 "*스캔 QR*"을 사용하여 서명된 PSBT를 Sparrow에 로드합니다. "*거래 저장*" 옵션도 비슷한 방식으로 작동하지만, 마이크로SD에 교환할 때 사용합니다;
- Hot Wallet의 경우 "*서명*"을 클릭하고 Wallet 비밀번호를 입력하여 서명하기만 하면 됩니다;
- 유선 Hardware Wallet의 경우에도 "*서명*"을 클릭하여 서명되지 않은 트랜잭션을 장치로 전송합니다.


![Image](assets/fr/57.webp)


Hardware Wallet에서 수취인의 Address, 송금 금액 및 요금을 확인합니다. 모든 것이 정확하면 서명을 진행합니다.


트랜잭션이 서명되면 Sparrow에 다시 나타나며, 이후 블록에 포함될 수 있도록 Bitcoin 네트워크에 브로드캐스트할 준비가 됩니다. 모든 것이 정확하다면 "*거래 브로드캐스트*"를 클릭합니다.


![Image](assets/fr/58.webp)


이제 거래가 브로드캐스트되어 확인을 기다리고 있습니다.


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## Sparrow에서 지갑 관리 및 구성하기


"*설정*" 탭에서 Wallet에 대한 자세한 정보를 확인할 수 있습니다:



- 포트폴리오 유형(단일 서명 또는 multi-sig) ;
- 사용된 스크립트 유형 ;
- Wallet에 지정한 이름입니다;
- 마스터 키 각인;
- 바이패스 경로 ;
- 계정의 확장 공개 키입니다.


![Image](assets/fr/60.webp)


"*내보내기*" 버튼을 사용하면 Sparrow에서 설정한 정보를 유지하면서 다른 소프트웨어에서 사용할 수 있도록 Wallet 정보를 내보낼 수 있습니다.


"*계정 추가*" 버튼을 사용하면 Wallet에 계정을 하나 더 추가할 수 있습니다. 계정은 별도의 받은 편지함 주소 집합에 해당합니다. 이 기능은 예를 들어 하나의 Mnemonic 문구로 개인 계정과 비즈니스 계정을 분리하려는 경우에 유용할 수 있습니다.


"*고급*" 버튼을 클릭하면 Sparrow의 Address 검색 사용자 지정 및 Wallet 비밀번호 변경과 같은 고급 설정에 액세스할 수 있습니다.


![Image](assets/fr/61.webp)


Sparrow wallet을 닫으면 Wallet가 자동으로 잠깁니다. 다음에 소프트웨어를 열면 비밀번호로 Wallet의 잠금을 해제하라는 창이 표시됩니다.


![Image](assets/fr/62.webp)


이 창이 열리지 않거나 Sparrow에서 다른 Wallet을 열려면 "*파일*" 탭을 클릭하고 "*Wallet 열기*"를 선택합니다.


![Image](assets/fr/63.webp)


그러면 파일 관리자가 Sparrow가 지갑을 저장하는 폴더로 열립니다. 열려는 Wallet을 선택하고 비밀번호를 입력하면 잠금이 해제됩니다.


![Image](assets/fr/64.webp)


"*설정*" 아래의 "*파일*" 메뉴에서 이전 섹션에서 이미 살펴본 Bitcoin 네트워크 연결 매개변수를 찾을 수 있습니다. 또한 사용되는 단위, 전환을 위한 법정 화폐, 정보 소스 등 다양한 매개변수를 조정할 수 있습니다.


![Image](assets/fr/65.webp)


"*보기*" 탭에서는 사용자 지정 옵션과 Wallet에 대한 트랜잭션 검색을 새로 고치는 "*Refresh Wallet*"와 같은 유용한 명령에 액세스할 수 있습니다.


![Image](assets/fr/66.webp)


"*도구*" 탭에는 다음을 포함한 여러 고급 도구가 그룹화되어 있습니다:



- "*서명/확인 메시지*"를 사용하면 수신 Address의 소유를 증명하거나 서명을 확인할 수 있습니다.
- "*다수에게 보내기*"는 한 번에 여러 수신 주소로 거래를 수행할 수 있는 간소화된 Interface을 제공하여 일괄 송금에 편리합니다.
- "*스윕 개인 키*"를 사용하면 간단한 개인 키로 보호된 비트코인을 검색하여 Sparrow wallet로 전송할 수 있습니다. 이는 HD 지갑 시대 이전인 2010년대 초반 비트코인을 보유한 분들에게 특히 유용할 수 있습니다.
- '다운로드 확인'은 다운로드한 소프트웨어를 장치에 설치하기 전에 무결성과 진위 여부를 확인합니다.
- "*다시 시작하기*"를 사용하면 Testnet 또는 시그넷 네트워크의 지갑으로 전환할 수 있습니다. 이는 실제 가치가 없는 코인으로 테스트 네트워크에 액세스하려는 경우에 유용할 수 있습니다.


![Image](assets/fr/67.webp)


이제 Sparrow wallet 지갑을 매일 관리할 수 있는 훌륭한 도구인 Bitcoin 소프트웨어에 대해 모두 알게 되었습니다.


이 튜토리얼이 유용했다면 아래에 Green 썸네일을 남겨주시면 대단히 감사하겠습니다. 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


또한 Hardware Wallet COLDCARD Q를 Sparrow wallet로 구성하는 방법을 설명하는 이 다른 튜토리얼을 추천합니다:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3