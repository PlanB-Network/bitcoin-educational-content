---
name: Bacca
description: Ledger 라이브 소프트웨어 없이 Ledger 구성하기
---
![cover](assets/cover.webp)


Ledger를 사용하는 경우, 적어도 초기 장치 구성의 경우 Ledger Live 소프트웨어를 통해 진위 여부를 확인하고 Bitcoin 애플리케이션을 설치해야 한다는 사실을 알고 계실 것입니다. 그러나 이 구성 후에는 많은 비트코인이 Ledger 라이브보다는 Sparrow 또는 Liana와 같은 전문 Bitcoin Wallet 관리 소프트웨어를 사용하는 것을 선호합니다. Ledger는 최신 Bitcoin 기능을 빠르게 포함하는 우수한 하드웨어 지갑을 생산하지만, 소프트웨어가 반드시 비트코인 사용자의 특정 요구에 맞게 조정되지는 않습니다. 실제로 Ledger 라이브에는 알트코인을 위해 설계된 많은 기능이 포함되어 있는 반면, Bitcoin Wallet 관리 전용 옵션은 제한되어 있습니다. 그러나 Sparrow와 Liana의 문제점은 (현재로서는) Ledger에 Bitcoin 애플리케이션을 설치할 수 없다는 것입니다.


Ledger을 처음 구성하는 동안 Ledger Live를 사용하지 않으려면 Bacca 도구(또는 "Ledger 인스톨러")를 사용하면 됩니다. 이 소프트웨어를 사용하면 Bitcoin 애플리케이션을 설치 및 업데이트하고, Ledger의 진위 여부를 확인하고, 나중에 디바이스의 펌웨어를 업데이트할 수도 있습니다. 바카는 체인코드 랩스의 Bitcoin core 개발자이자 [리볼트와 Liana의] 공동 창립자인 앙투안 푸앵소(Darosior)(https://wizardsardine.com/)와 파이스코인러가 만들었습니다.


이 튜토리얼에서는 이 도구를 사용하는 방법을 보여드리므로 Ledger Live 소프트웨어 없이도 Ledger 디바이스를 계속 사용할 수 있습니다. 모든 디바이스에서 작동합니다: 나노 S 클래식, 나노 S 플러스, 나노 X, 플렉스, 스탁스.


---
*이 도구는 상당히 새로운 도구이며 개발자는 아직 **테스트 단계**에 있다고 명시하고 있습니다. 이 도구는 테스트 목적으로만 사용할 것을 권장하며, 실제 Bitcoin Wallet를 호스팅하기 위한 장치에는 사용하지 않는 것이 좋습니다. 이와 관련하여 이 도구 개발자의 권장 사항을 따르는 것이 좋으며, 이는 [GitHub 리포지토리의 README에 명시되어 있습니다(https://github.com/darosior/ledger_installer)]*


---
## 전제 조건


컴퓨터에서 Bacca를 사용하려면 두 가지 도구가 필요합니다:




- Git ;
- Rust.


이미 설치했다면 이 단계를 건너뛸 수 있습니다.


**Linux:**


Linux 배포판에서는 일반적으로 Git이 사전 설치되어 있습니다. 시스템에 Git이 설치되어 있는지 확인하려면 터미널에 다음 명령을 입력하면 됩니다:


```bash
git --version
```


시스템에 Git이 설치되어 있지 않다면 다음 명령어를 사용하여 Debian에 설치하세요:


```bash
sudo apt install git
```


마지막으로 Rust 개발 환경을 설치하려면 명령 을 사용합니다:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Git을 설치하려면 [프로젝트의 공식 웹사이트](https://git-scm.com/)로 이동합니다. 소프트웨어를 다운로드하고 설치 지침을 따릅니다.


![BACCA](assets/fr/01.webp)


공식 웹사이트](https://www.Rust-lang.org/tools/install)에서 Rust를 설치하려면 같은 방법으로 진행하세요.


![BACCA](assets/fr/02.webp)


**MacOS:**


Git이 아직 시스템에 설치되어 있지 않은 경우 터미널을 열고 다음 명령을 실행하여 설치합니다:


```bash
git --version
```


시스템에 Git이 설치되어 있지 않은 경우 Git이 포함된 Xcode를 설치하라는 창이 열립니다. 화면의 안내에 따라 설치를 진행하기만 하면 됩니다.


Rust을 설치하려면 다음 명령을 실행하세요:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## 바카 설치


터미널을 열고 소프트웨어를 저장하려는 폴더로 이동한 다음 다음 명령을 실행합니다:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


소프트웨어 디렉토리로 이동합니다:


```bash
cd ledger_installer
```


그런 다음 Cargo를 사용하여 프로젝트를 컴파일하고 Bacca GUI를 실행합니다:


```bash
cargo run -p ledger_manager_gui
```


이제 Interface 소프트웨어에 액세스할 수 있습니다.


![BACCA](assets/fr/03.webp)


## Ledger 구성


시작하기 전에 Ledger를 처음 사용하는 경우 PIN 코드를 설정하고 복구 문구를 저장했는지 확인하세요. 이러한 초기 단계에는 Ledger Live가 필요하지 않습니다. USB 케이블을 통해 Ledger를 연결하여 전원을 공급하기만 하면 됩니다. 이 두 단계를 어떻게 진행해야 할지 잘 모르겠다면 사용 중인 모델에 맞는 튜토리얼의 시작 부분을 참조하세요:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## 바카 사용


Ledger을 컴퓨터에 연결하고 설정한 PIN 코드를 사용하여 잠금을 해제합니다. Bacca가 자동으로 Ledger을 감지합니다.


![BACCA](assets/fr/04.webp)


Ledger의 진위 여부를 확인하려면 "*확인*" 버튼을 클릭하세요. 계속하려면 Ledger 장치에서 연결을 승인해야 합니다.


![BACCA](assets/fr/05.webp)


그러면 바카에서 Ledger가 정품인지 여부를 알려줍니다. 그렇지 않은 경우 기기가 손상되었거나 위조품임을 나타냅니다. 이 경우 즉시 사용을 중단하세요.


![BACCA](assets/fr/06.webp)


"*앱*" 메뉴에서 Ledger에 이미 설치된 애플리케이션 목록을 확인할 수 있습니다.


![BACCA](assets/fr/07.webp)


Bitcoin 애플리케이션을 설치하려면 "*설치*"를 클릭한 다음 Ledger에 설치를 승인합니다.


![BACCA](assets/fr/08.webp)


애플리케이션이 잘 설치되었습니다.


![BACCA](assets/fr/09.webp)


최신 버전의 Bitcoin 애플리케이션이 설치되어 있지 않은 경우, 바카는 "*최신*" 표시 대신 "*업데이트*" 버튼을 표시합니다. 이 버튼을 클릭하기만 하면 애플리케이션을 업데이트할 수 있습니다.


![BACCA](assets/fr/10.webp)


이제 Ledger가 최신 버전의 Bitcoin 애플리케이션으로 올바르게 구성되었으므로 Ledger 라이브를 거치지 않고도 Sparrow 또는 Liana과 같은 관리 소프트웨어에서 Wallet을 가져와서 사용할 준비가 되었습니다!


이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


또한 소프트웨어를 설치하기 전에 소프트웨어의 무결성과 진위 여부를 확인하는 방법을 설명하는 GnuPG의 이 튜토리얼을 살펴보는 것이 좋습니다. 이는 특히 Liana 또는 Sparrow과 같은 Wallet 관리 소프트웨어를 설치할 때 중요한 작업입니다:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc