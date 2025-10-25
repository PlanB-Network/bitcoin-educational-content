---
name: Bitcoin Knots
description: Bitcoin Knots 대체 클라이언트로 노드를 시작하려면 어떻게 하나요?
---
![cover](assets/cover.webp)


![video](https://youtu.be/zT4NuAaH3EM)


Bitcoin Knots는 Bitcoin core에서 파생된 Bitcoin 프로토콜의 대체 구현입니다. Luke Dashjr가 설계하고 유지 관리하는 이 프로토콜은 네트워크의 다른 노드와 호환성을 유지하면서 Mempool의 몇 가지 추가 기능과 규칙 조정을 제공합니다. Bitcoin Knots는 Bitcoin Wallet을 통합하지만, 다른 Wallet 소프트웨어와 함께 간단한 Bitcoin 노드로도 사용할 수 있습니다.


## 코어가 아닌 노트를 사용하는 이유는 무엇인가요?


현재 코어는 네트워크에서 Bitcoin 프로토콜의 대부분을 구현하고 있습니다. Bitcoin 프로토콜은 일련의 규칙일 뿐입니다. 이를 적용하려면 소프트웨어가 필요합니다. Bitcoin 프로토콜을 구현하는 소프트웨어를 실행하는 머신을 노드라고 하며, 이러한 모든 노드가 모여 Bitcoin 네트워크를 구성합니다.


Bitcoin의 역사를 통틀어 Satoshi 나카모토가 개발한 초기 소프트웨어에서 파생된 수많은 클라이언트가 등장했습니다. 현재(2025년 3월)는 Bitcoin core이 압도적인 다수를 차지하고 있으며, Bitcoin 네트워크의 노드 중 거의 98%가 이 클라이언트를 사용하고 있습니다.


그러나 대체 소프트웨어도 사용할 수 있습니다. 이는 Bitcoin Cash와 같은 Altcoin 연결 노드가 아니라 실제 Bitcoin 네트워크와 호환되는 대체 클라이언트입니다. 이 중 Bitcoin Knots이 가장 잘 알려져 있습니다. 현재 네트워크의 약 1.4%를 차지하고 있습니다. 다른 대체 고객은 아직 소수에 불과합니다.


![Image](assets/fr/01.webp)


Core 대신 Knots와 같은 대체 클라이언트를 사용하는 데에는 크게 두 가지 이유가 있습니다:




- 기술**: 이러한 클라이언트는 노드에서 어떤 트랜잭션을 수락하고 브로드캐스트할지 결정함으로써 코어에 다양한 옵션을 제공하며, 특히 Mempool 관리 측면에서 중요합니다.
- 정책**: 일부 사람들은 기술적이지 않은 이유로, 특히 코어의 독점을 줄이기 위해 코어의 대안을 지원하기 위해 Knots와 같은 대체 클라이언트를 사용하는 것을 선호합니다. 만약 Core가 손상된다면 견고하고 잘 관리되는 대체 클라이언트가 있을 뿐만 아니라 그 사용법을 아는 것도 유용할 것입니다. 코어 개발자에 대한 신뢰를 잃었거나 다수 고객의 경영진이 마음에 들지 않아서 항의의 목적으로 Knots를 사용하는 사람들도 있습니다.


## Bitcoin Knots는 어떻게 설치하나요?


Bitcoin Knots 공식 웹사이트](https://bitcoinknots.org/#download)로 이동하여 운영 체제용 버전을 다운로드하세요. 소프트웨어 확인을 위해 지문과 서명을 다운로드하는 것을 잊지 마세요. 이 파일은 [Bitcoin Knots GitHub 리포지토리](https://github.com/bitcoinknots/Bitcoin)에서도 다운로드할 수 있습니다.


![Image](assets/fr/02.webp)


컴퓨터에 소프트웨어를 설치하기 전에 소프트웨어의 진위 여부와 무결성을 확인하는 것이 좋습니다. 방법을 모른다면 다른 튜토리얼을 참조하세요:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
소프트웨어가 확인되면 설치 패널에 표시된 단계에 따라 소프트웨어를 설치합니다.


![Image](assets/fr/03.webp)


## IBD 출시


Bitcoin Knots을 처음 실행하면 노드 데이터(Blockchain, UTXO 세트 및 파라미터 포함)가 저장될 로컬 디렉토리를 선택할 수 있습니다.


![Image](assets/fr/04.webp)


가장 최근의 블록만 유지하도록 Blockchain 데이터를 잘라내도록 선택할 수도 있습니다. 이 옵션을 사용하면 노드가 설정된 스토리지 한도 내에서 각 블록을 전체적으로 확인하여 가장 오래된 블록을 점진적으로 제거할 수 있습니다. 디스크 공간이 충분하다면(현재 약 650GB이지만 이 수치는 계속 증가하고 있음) 이 옵션을 선택하지 않은 상태로 두세요. 디스크 공간이 제한되어 있는 경우 가지치기를 활성화하고 허용되는 최대 용량을 지정하세요.


참고: 노드가 pruned이고 복구된 Wallet을 동기화하는 데 사용하는 경우, 로컬에 저장된 가장 오래된 블록 이전의 트랜잭션을 검색할 수 없습니다.


![Image](assets/fr/05.webp)


또 다른 사용 가능한 옵션은 "*유효한 것으로 가정*"입니다. 특정 블록 이전에 블록에 포함된 트랜잭션에 대한 서명 확인을 건너뛰어 초기 동기화 속도를 높입니다.


"*유효한 것으로 가정*"의 목적은 이러한 거래가 네트워크에서 사전에 이미 대규모로 검증되었다고 가정함으로써 보안을 크게 저하시키지 않고 노드의 첫 번째 동기화 속도를 높이는 것입니다. 유일한 단점은 노드가 이전의 Bitcoin 도난을 감지하지 못하지만, 발행된 총 비트코인의 정확성을 보장한다는 것입니다. 노드는 지정된 블록 이후의 모든 트랜잭션 서명을 확인합니다. 이 접근 방식은 네트워크에서 오랫동안 이의 없이 승인된 트랜잭션이 유효할 가능성이 높다는 가정에 기반합니다.


예를 들어, 여기서는 "*유효한 것으로 가정*"이 차단 번호로 설정되어 있습니다. 855 000 `0000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, 2024년 8월 1일에 게시되었습니다. 따라서 IBD 동안 내 노드는 이 블록에서만 전체 서명 검증을 시작합니다.


![Image](assets/fr/06.webp)


그런 다음 "*확인*" 버튼을 클릭해 *초기 블록 다운로드*를 시작합니다. 초기 노드 동기화 중에는 잠시 기다려야 합니다. 나중에 동기화를 다시 시작하려면 소프트웨어를 닫고 컴퓨터 전원을 끄면 됩니다. 다음에 프로그램을 열면 동기화가 문제 없이 다시 시작됩니다.


![Image](assets/fr/07.webp)


## Bitcoin 매듭 설정하기


"*설정*" 탭을 클릭한 다음 "*옵션*"을 선택합니다.


![Image](assets/fr/08.webp)


"*메인*" 탭에서 노드의 주요 매개변수에 액세스합니다:




- "*시작...*"은 컴퓨터가 시작될 때 자동으로 노드를 실행하여 즉시 동기화를 시작합니다;
- "*Prune...*"는 Blockchain을 가지치기를 선택한 경우 저장 용량 제한을 조정합니다;
- "*데이터베이스 캐시...*"는 노드에 허용되는 최대 RAM 용량을 설정합니다;
- 마지막으로, Bitcoin Knots 노드를 다른 Wallet 소프트웨어(예: Sparrow wallet 또는 Liana)에 연결하려면 "*RPC 서버 활성화*"를 활성화합니다.


![Image](assets/fr/09.webp)


"*Wallet*" 탭에서 나중에 Knots에서 생성할 수 있는 통합 Wallet에 대한 설정을 찾을 수 있습니다. RBF 및 Coin 제어를 활성화하는 것이 좋습니다. 사용할 스크립트 유형도 정의할 수 있습니다.


![Image](assets/fr/10.webp)


'*네트워크*' 탭에는 특정 요구에 맞게 조정할 수 있는 네트워크 매개변수가 포함되어 있습니다.


![Image](assets/fr/11.webp)


"*Mempool*" 탭에서는 *메모리 풀*, 즉 메모리에 저장된 미확인 트랜잭션의 관리와 이 기능에 할당된 최대 크기(기본값 300MB)를 구성할 수 있습니다.


![Image](assets/fr/12.webp)


'스팸 필터링' 탭은 Bitcoin Knots 기능입니다. 여기에는 브로드캐스트할 거래를 수락하거나 거부할지 선택할 수 있는 다양한 설정이 있습니다. 주요 목적은 노드 과부하를 방지하면서 이러한 관행을 방지하기 위해 Bitcoin의 특정 한계 사용, 특히 메타 프로토콜을 제한하는 것입니다. 이는 Bitcoin에 대한 개인적인 비전에 따라 정치적 선택입니다.


또한 "*Dust*" 임계값 정의와 같은 일반적인 매개변수도 확인할 수 있습니다.


그러나 이러한 매개변수는 표준화 규칙에만 영향을 미칩니다. 노드는 나머지 Bitcoin 네트워크와 호환성을 유지하기 위해 미확인 트랜잭션이 블록에 포함된 경우에만 계속해서 미확인 트랜잭션을 수락합니다. 이러한 설정은 노드가 미확인 트랜잭션을 처리하고 피어에게 배포하는 방식만 수정합니다. 실제로 Knots는 소수에 속하기 때문에 네트워크의 표준화를 정의하는 것은 Bitcoin core에서 기본적으로 설정된 규칙입니다.


![Image](assets/fr/13.webp)


이 기능을 활성화하려면 "*Mining*" 탭에서 노드가 Mining에 참여할 수 있도록 구성할 수 있습니다.


![Image](assets/fr/14.webp)


마지막으로 '*디스플레이*' 탭은 소프트웨어 언어를 포함하여 Interface 그래픽과 관련된 매개변수와 관련된 탭입니다.


![Image](assets/fr/15.webp)


## Bitcoin Wallet 만들기


초기 동기화가 완료되면 Bitcoin Knots 노드가 완전히 작동합니다. 이제 이 노드를 다른 Wallet 소프트웨어에 연결하거나 내장된 Hot Wallet을 직접 사용할 수 있습니다. 이렇게 하려면 "*새 Wallet 만들기*" 버튼을 클릭합니다.


![Image](assets/fr/16.webp)


Wallet에 이름을 지정하세요. "*Wallet 암호화*"를 클릭하여 passphrase BIP39로 보호할 수도 있습니다. 준비가 완료되면 "*생성*" 버튼을 클릭합니다.


![Image](assets/fr/17.webp)


passphrase BIP39는 Mnemonic 문구 외에 자유롭게 선택할 수 있는 옵션 암호로, Wallet의 보안을 강화하기 위해 사용할 수 있습니다. 이 기능을 구성하기 전에 passphrase의 이론적 작동 방식과 비트코인의 영구적 손실로 이어질 수 있는 실수를 방지하는 방법을 자세히 설명하는 다음 문서를 읽어보시기 바랍니다:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
passphrase 옵션을 활성화한 경우, 강력한 옵션을 선택하고 하나 이상의 안전한 물리적 미디어에 신중하게 저장하세요.


![Image](assets/fr/18.webp)


이제 Bitcoin Wallet가 생성되었습니다.


![Image](assets/fr/19.webp)


## Bitcoin Wallet 백업하기


첫 비트코인을 받기 전이라도 분실 또는 컴퓨터 장애 시 자금을 복구할 수 있도록 Bitcoin Wallet를 백업하는 것이 필수적입니다. 이렇게 하려면 "*파일*" 탭을 클릭한 다음 "*백업 Wallet*"를 클릭하세요.


![Image](assets/fr/20.webp)


이 작업은 모든 비트코인을 복원하는 데 사용할 수 있는 단일 파일을 생성합니다. 따라서 매우 주의하고 안전한 외부 매체에 저장하세요.


## 비트코인 받기


비트코인을 Knots Wallet으로 직접 받으려면 "*수신*" 버튼을 클릭하세요.


![Image](assets/fr/21.webp)


Address에 "*라벨*"을 지정하여 용도를 쉽게 식별하고 향후 *Coin 컨트롤*의 사용을 용이하게 하세요. 이 Address에서 받을 정확한 금액을 미리 정의하거나 결제자에게 메시지를 추가할 수도 있습니다. 매개변수를 설정한 후 "*결제 요청*"을 클릭합니다.


![Image](assets/fr/22.webp)


그러면 Bitcoin Knots에 수신 Address가 표시되며, 이를 복사하거나 스캔하여 결제자에게 보낼 수 있습니다.


![Image](assets/fr/23.webp)


트랜잭션이 브로드캐스트되면 '*거래*' 메뉴에서 트랜잭션의 상태를 바로 확인할 수 있습니다.


![Image](assets/fr/24.webp)


## 비트코인 보내기


이제 Knots Wallet에 비트코인이 들어왔으니 전송할 수 있습니다. 그러려면 "*송금*" 버튼을 클릭합니다.


![Image](assets/fr/25.webp)


"*입력...*" 버튼을 클릭하여 이 거래에 사용하고자 하는 정확한 UTXO을 선택합니다.


![Image](assets/fr/26.webp)


수신자의 Bitcoin Address을 입력합니다.


![Image](assets/fr/27.webp)


이 거래의 목적을 기억하기 위해 레이블을 추가합니다.


![Image](assets/fr/28.webp)


이 Address로 송금할 금액을 입력합니다.


![Image](assets/fr/29.webp)


"*선택...*" 버튼을 클릭하여 현재 네트워크 상태에 따라 거래에 적합한 수수료율을 선택합니다.


![Image](assets/fr/30.webp)


모든 것이 만족스럽다면 '*전송*' 버튼을 클릭합니다. passphrase을 사용하는 경우 이 단계에서 입력하라는 메시지가 표시됩니다.


![Image](assets/fr/31.webp)


트랜잭션 매개변수를 다시 한 번 확인한 다음 모든 것이 올바르면 "*전송*" 버튼을 다시 클릭하여 트랜잭션에 서명하고 배포합니다.


![Image](assets/fr/32.webp)


이제 확인 대기 중인 거래가 '*거래*' 탭에 표시됩니다.


![Image](assets/fr/33.webp)


## 노드를 다른 프로그램에 연결하기


Bitcoin Knots의 Bitcoin Wallet 통합 관리용 Interface은 직관적이지 않고 기능이 상대적으로 제한적입니다. 하지만 Bitcoin Knots 노드를 전용 Wallet 관리 소프트웨어에 연결하여 Blockchain Bitcoin 데이터에 쉽게 액세스하고 트랜잭션을 브로드캐스트할 수 있습니다.


절차는 사용하는 소프트웨어에 따라 다르지만, Bitcoin Knots을 Wallet 소프트웨어와 동일한 컴퓨터에 설치하거나 별도의 컴퓨터에서 실행하는 두 가지 주요 시나리오가 있습니다.


### 로컬 Bitcoin Knots 사용 :


Bitcoin Knots가 컴퓨터에 설치되어 있는 경우 소프트웨어 파일 중 `Bitcoin.conf` 파일을 찾습니다. 이 파일이 없는 경우 직접 만들 수 있습니다. 텍스트 편집기로 파일을 열고 다음 줄을 삽입합니다:


```ini
server=1
```


그런 다음 변경 사항을 저장합니다.


Bitcoin-QT의 Interface 그래픽을 통해서도 "*설정*" > "*옵션*"으로 이동하여 이 작업을 수행할 수 있습니다 > "*옵션...*"으로 이동하여 "*RPC 서버 활성화*" 옵션을 활성화할 수도 있습니다.


이러한 변경을 수행한 후에는 소프트웨어를 다시 시작하는 것을 잊지 마세요.


![Image](assets/fr/34.webp)


그런 다음 Wallet 관리 소프트웨어(예: Sparrow wallet 또는 Liana)로 이동하여 쿠키 파일 경로를 입력합니다(운영 체제에 따라 일반적으로 `Bitcoin.conf`와 같은 폴더에 위치):


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


다른 매개변수는 기본값인 URL `127.0.0.1`과 포트 `8332`로 그대로 둔 다음 "*연결 테스트*"를 클릭합니다.


![Image](assets/fr/36.webp)


### 원격 Bitcoin Knots 사용 :


동일한 네트워크에 연결된 다른 컴퓨터에 Bitcoin Knots를 설치한 경우, 먼저 소프트웨어 파일 중 `Bitcoin.conf` 파일을 찾습니다. 이 파일이 아직 존재하지 않는다면 직접 만들 수 있습니다. 텍스트 편집기로 이 파일을 열고 다음 줄을 추가합니다:


```ini
server=1
```


파일을 편집한 후에는 운영 체제에 맞는 폴더에 저장해야 합니다:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

이 작업은 Bitcoin-QT의 Interface 그래픽을 통해서도 수행할 수 있습니다. "*설정*" 메뉴로 이동한 다음 "*옵션...*"으로 이동하여 해당 상자를 체크하여 "*RPC 서버 활성화*" 옵션을 활성화합니다. 'Bitcoin.conf' 파일이 없는 경우 "*구성 파일 열기*"를 클릭하여 이 Interface에서 직접 생성할 수 있습니다.


![Image](assets/fr/37.webp)


로컬 네트워크에서 Address를 호스팅하는 컴퓨터의 IP Bitcoin Knots를 찾습니다. 이를 위해 [Angry IP Scanner](https://angryip.org/)와 같은 도구를 사용할 수 있습니다. 예를 들어 노드의 IP Address가 `192.168.1.18`이라고 가정해 보겠습니다.


Bitcoin.conf` 파일에 다음 줄을 추가하고 `rpcbind=192.168.1.18`을 설정하여 노드의 IP Address과 일치하도록 합니다.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


또한 원격 연결을 위한 사용자 이름과 비밀번호를 `Bitcoin.conf` 파일에 추가하세요. Loic`을 사용자 이름으로, `my_password`를 강력한 비밀번호로 바꿔야 합니다:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


파일을 수정하고 저장한 후 Bitcoin Knots를 다시 시작합니다.


이제 Wallet 관리 소프트웨어(예: Sparrow wallet 또는 Liana)로 이동할 수 있습니다. Sparrow에서 "*사용자/패스*" 탭으로 이동합니다. 'Bitcoin.conf' 파일에 구성한 사용자 이름과 비밀번호를 입력합니다. 다른 매개변수(예: URL `127.0.0.1` 및 포트 `8332`)는 기본값으로 그대로 둡니다. 그런 다음 "*연결 테스트*"를 클릭합니다.


![Image](assets/fr/40.webp)


연결이 설정되었습니다.


이제 대체 Bitcoin Knots 구현에 대해 모두 알게 되었습니다.


이 튜토리얼이 유용했다면 아래에 Green 엄지 손가락을 남겨주시면 대단히 감사하겠습니다. 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


나만의 라이트닝 노드를 설정하는 방법을 설명하는 이 다른 튜토리얼도 추천합니다:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a