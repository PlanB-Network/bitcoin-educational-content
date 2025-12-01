---
name: Plan ₿ 아카데미 - Pears 앱
description: Pears에서 Plan ₿ Academy 애플리케이션을 설치하고 사용하는 방법은 무엇인가요?
---

![cover](assets/cover.webp)


Plan ₿ Academy는 강좌, 튜토리얼 및 수천 개의 오픈 소스 리소스를 한데 모은 Bitcoin 전용 최대 교육 데이터베이스라는 사실을 이미 알고 계실 것입니다. 원래 Plan ₿ Academy는 웹사이트였습니다. 하지만 검열 등의 이유로 더 이상 정상적으로 액세스할 수 없게 된다면 어떻게 될까요?


이 튜토리얼에서는 **홀펀치**가 개발하고 **테더**가 지원하는 P2P(P2P) 기술인 **Pears**를 사용하여 검열에 저항하는 방식으로 **Plan ₿ Academy** 플랫폼을 운영하는 방법에 대해 알아보세요.


Pears는 중앙 집중식 웹사이트에 의존하지 않고도 Plan ₿ Academy 플랫폼을 실행할 수 있는 소프트웨어입니다. 이 튜토리얼에서는 Pears를 통해 Plan ₿ Academy에 액세스하기 위해 컴퓨터에 Pears를 설치하는 방법을 설명합니다.


서버, 호스트, 중개자 등 중앙 집중식 인프라에 의존하지 않고 웹 애플리케이션을 배포하고 사용할 수 있도록 하는 것이 Pears의 목표입니다. 즉, 클라우드 제공업체가 문을 닫거나 한 국가가 도메인을 차단하더라도 애플리케이션은 네트워크의 피어들 사이에서 계속 사용할 수 있습니다. 이러한 접근 방식 덕분에 교육 플랫폼인 Plan ₿ Academy는 단일 장애 지점 없이 전 세계에서 계속 액세스할 수 있습니다.


---

**TL;DR:**



- Pears를 설치합니다;



- 다음 명령을 실행하여 요금제 ₿ 아카데미 앱을 실행합니다:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. 배란 무엇인가요?


Pears는 P2P 애플리케이션을 위한 런타임 환경, 개발 도구, 배포 플랫폼의 기능을 동시에 제공합니다. 이 오픈 소스 도구를 사용하면 서버나 인프라 없이 사용자 간에 직접 소프트웨어를 빌드, 공유 및 실행할 수 있습니다. 즉, 중앙 서버에서 애플리케이션을 호스팅하는 대신 각 사용자가 네트워크의 노드가 되어 애플리케이션과 데이터의 일부를 다른 피어와 공유한다는 의미입니다. 전체 시스템이 분산 네트워크를 형성하여 각 인스턴스가 협력하여 서비스 접근성을 유지합니다.


![Image](assets/fr/01.webp)


이 접근 방식은 Holepunch에서 개발한 모듈식 소프트웨어 구성 요소 세트를 기반으로 합니다:



- Hypercore**: 중앙 데이터베이스 없이 데이터 일관성과 보안을 보장하는 분산형 로그입니다.
- Hyperbee**: 데이터를 효율적으로 정리하고 쿼리할 수 있도록 Hypercore 위에 구축된 인덱스입니다.
- Hyperdrive**: 애플리케이션 파일을 저장하고 피어 간에 동기화하는 데 사용되는 분산 파일 시스템입니다.
- 하이퍼스웜** 및 **하이퍼DHT**: 중앙 서버 없이도 전 세계 피어를 검색하고 연결할 수 있는 네트워크 계층입니다.
- Secretstream**: 피어 간의 통신을 보호하는 엔드투엔드 암호화 프로토콜입니다.


이러한 구성 요소를 결합하여 Pears는 모든 사용자가 네트워크에 적극적으로 참여하는 자율적이고 암호화된 분산형 애플리케이션을 만들 수 있습니다. 이러한 탈중앙화된 아키텍처는 인프라 비용, 검열 위험, SPOF(*단일 실패 지점*)를 제거합니다.


홀펀치는 마티아스 부스(Mathias Buus)와 파올로 아르도이노(Paolo Ardoino, 테더의 CEO이자 비트파이넥스의 CTO)가 설립한 회사로, P2P 로직을 Bitcoin 이상으로 확장한다는 사명을 가지고 개발되었습니다. 홀펀치의 야망은 모든 애플리케이션이 허가 없이, 서버 없이, 중개자 없이 작동할 수 있는 "*동료 인터넷*"을 구축하는 것입니다. 홀펀치는 이미 완전한 P2P 화상 회의 및 메시징 앱인 **Keet**의 뒤를 잇고 있습니다.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*이 Pears 설치 튜토리얼은 운영 체제에 따라 여러 섹션으로 나뉘어 있습니다. 사용 중인 환경에 해당하는 섹션으로 바로 이동하여 적절한 지침을 따르세요



- 리눅스(데비안)** → 섹션 **2**
- Windows** → 섹션 **3**
- macOS** → 섹션 **4**


## 2. Linux(Debian)에 Pears를 설치하는 방법은 무엇인가요?


Debian에 Pears를 설치하는 것은 비교적 간단하지만 몇 가지 전제 조건이 필요하며, 이 섹션에서 자세히 설명합니다.


### 2.1. 시스템 업데이트


무엇보다도 시스템이 최신 상태인지 확인하는 것이 중요합니다.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. 설치 종속성


Pears는 베어 자바스크립트 런타임 엔진에서 사용하는 `libatomic1`을 비롯한 일부 시스템 라이브러리에 의존합니다. 다음 명령어로 설치하세요:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. NVM을 통해 Node.js 및 npm을 설치합니다


Pears는 *Node.js* 패키지 매니저인 *npm*을 통해 배포됩니다. Pears가 *Node.js*를 실행하는 데 직접적으로 의존하지는 않지만 설치에 필요합니다. Linux에서 *Node.js*를 설치하는 권장 방법은 여러 버전의 Node를 나란히 관리할 수 있는 *NVM*(*Node 버전 관리자*)을 사용하는 것입니다.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


그런 다음 터미널을 다시 로드하여 *NVM*을 활성화합니다:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


NVM*이 제대로 설치되었는지 확인합니다:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


그런 다음 안정적인 버전의 *Node.js*(예: 현재 LTS 버전)를 설치합니다:


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Node.js*와 *npm*이 제대로 설치되었는지 확인합니다:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Npm으로 Pears 설치


Npm*을 사용할 수 있게 되면 시스템에 Pears CLI를 전역적으로 설치할 수 있습니다. 그러면 어느 디렉토리에서나 `pear` 명령을 실행할 수 있습니다.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. 배 초기화


설치 후 터미널에서 다음 명령을 실행하면 됩니다:


```bash
pear
```


처음 시작할 때 Pears는 피어 투 피어 네트워크에 연결하여 필요한 구성 요소를 다운로드합니다. 이 프로세스는 중앙 서버에 의존하지 않고 다른 피어에서 직접 파일을 검색합니다.


![Image](assets/fr/10.webp)


다운로드가 완료되면 명령을 다시 실행하여 모든 것이 작동하는지 확인합니다:


```bash
pear
```


![Image](assets/fr/11.webp)


모든 것이 올바르게 설치되면 사용 가능한 명령어 목록과 함께 Pears 도움말 메뉴가 나타납니다.


### 2.6. 키트로 배 테스트하기


홀펀치에서 개발한 오픈 소스 메시징 및 화상 회의 소프트웨어인 Keet와 같이 네트워크에서 사용 가능한 기존 P2P 애플리케이션을 실행하여 Pears가 완전히 작동하는지 확인할 수 있습니다.


```bash
pear run pear://keet
```


이 명령은 중앙 서버를 사용하지 않고 Pears 네트워크에서 직접 Keet 애플리케이션을 로드합니다. Keet이 올바르게 실행되면 Pears 설치가 완전히 작동한다는 의미입니다.


![Image](assets/fr/12.webp)


이제 Linux 시스템에서 Pears로 피어 투 피어 애플리케이션을 실행하고 호스팅할 준비가 되었습니다.


## 3. Windows에 Pears를 설치하는 방법


Windows에 Pears를 설치하는 방법은 Linux와 마찬가지로 간단하지만 몇 가지 특정 도구가 필요합니다.


*Linux를 사용 중이고 이미 Pears를 설치한 경우 **5단계**.*로 바로 건너뛸 수 있습니다


### 3.1. 관리자 권한으로 PowerShell 열기


먼저 관리자 권한으로 PowerShell을 시작합니다:



- 시작 메뉴를 클릭합니다;
- "PowerShell"을 입력합니다;
- "*Windows PowerShell*"을 마우스 오른쪽 버튼으로 클릭합니다;
- "*관리자 권한으로 실행*"을 선택합니다.


![Image](assets/fr/15.webp)


### 3.2. NVS 다운로드


배는 *Node.js* 패키지 매니저인 *npm*을 통해 설치됩니다. Windows에서는 홀펀치에서 권장하는 방법은 *NVS*(*노드 버전 전환기*)를 사용하는 것인데, 이는 이 시스템에서 *NVM*보다 더 안정적입니다.


PowerShell에서 다음 명령을 실행하여 최신 버전의 *NVS*를 설치합니다:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Node.js 설치


설치 후 PowerShell을 다시 시작한 다음 다음 명령을 입력합니다:


```powershell
nvs
```


사용 가능한 *Node.js* 버전 목록이 표시됩니다. 키보드의 `a` 키를 눌러 첫 번째 버전을 선택합니다.


![Image](assets/fr/17.webp)


*이제 Node.js*가 설치되었습니다.


![Image](assets/fr/18.webp)


### 3.4. 설치 확인


Node.js* 및 *npm*에 액세스할 수 있는지 확인합니다:


```powershell
node -v
npm -v
```


두 명령 모두 버전 번호를 반환해야 합니다.


![Image](assets/fr/19.webp)


### 3.5. Npm으로 Pears 설치


Node.js*와 *npm*을 사용할 수 있게 되면 시스템에 **Pears CLI**을 전역적으로 설치합니다:


```powershell
npm install -g pear
```


이렇게 하면 글로벌 *npm* 디렉터리에 `pear` 바이너리가 설치됩니다.


![Image](assets/fr/20.webp)


### 3.6. 배 확인 및 초기화


설치가 완료되면 실행합니다:


```powershell
pear
```


처음 시작할 때 Pears는 피어 투 피어 네트워크에서 필요한 구성 요소를 자동으로 다운로드합니다. 이 과정은 잠시 걸릴 수 있습니다.


![Image](assets/fr/21.webp)


모든 것이 정상적으로 진행되었다면 사용 가능한 하위 명령(실행, seed, 정보...) 목록이 있는 Pears CLI 도움말 메뉴가 표시되어야 합니다.


### 3.7. 키트로 배 테스트하기


홀펀치에서 개발한 오픈 소스 메시징 및 화상 회의 소프트웨어인 Keet와 같이 네트워크에서 사용 가능한 기존 P2P 애플리케이션을 실행하여 Pears가 완전히 작동하는지 확인할 수 있습니다.


```bash
pear run pear://keet
```


이 명령은 중앙 서버를 사용하지 않고 Pears 네트워크에서 직접 Keet 애플리케이션을 로드합니다. Keet이 성공적으로 시작되면 Pears 설치가 완전히 작동한다는 의미입니다.


![Image](assets/fr/22.webp)


이제 Windows 시스템에서 Pears를 사용하여 피어 투 피어 애플리케이션을 실행하고 호스팅할 준비가 되었습니다.


## 4. MacOS에 Pears를 설치하는 방법


MacOS에 Pears를 설치하는 방법은 Linux와 비슷하지만 Apple의 환경에 따라 몇 가지 조정이 필요합니다. 이 단계를 함께 살펴보겠습니다.


*Linux 또는 Windows를 사용 중이고 이미 Pears를 설치한 경우 **5단계**.*로 바로 건너뛸 수 있습니다


### 4.1. 시스템 전제 조건 확인


설치하기 전에 시스템에 *Xcode 명령줄 도구*가 설치되어 있는지 확인하세요. 이 패키지는 *Node.js*와 그 종속 요소에 필요한 빌드 도구를 제공합니다.


이렇게 하려면 단축키 `Cmd + 스페이스바`를 사용하여 터미널을 열고 `Terminal`을 입력한 다음 `Enter`를 누릅니다. 그런 다음 터미널에서 다음 명령을 실행하여 설치합니다:


```bash
xcode-select --install
```


도구가 이미 시스템에 설치되어 있는 경우 macOS에서 이를 알려줍니다.


### 4.2. NVM 설치


Pears는 *Node.js* 패키지 매니저인 *npm*을 통해 배포됩니다. Pears가 작동하기 위해 *Node.js*에 직접적으로 의존하지는 않지만 설치에는 필요합니다. MacOS에서 *Node.js*를 설치하는 권장 방법은 여러 노드 버전을 동시에 관리할 수 있는 *NVM*(*노드 버전 관리자*)입니다.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


그런 다음 터미널을 다시 로드하여 *NVM*을 활성화합니다:


```bash
source ~/.zshrc
```


Zsh* 대신 *bash*를 사용하는 경우 실행합니다:


```bash
source ~/.bashrc
```


다음으로 *NVM*이 올바르게 설치되었는지 확인합니다:


```bash
nvm --version
```


터미널에 설치된 *NVM* 버전이 표시되어야 합니다.


### 4.3. Node.js 및 npm 설치


그런 다음 안정적인 버전의 *Node.js*(예: 현재 LTS 버전)를 설치합니다:


```bash
nvm install --lts
```


설치가 완료되면 설치된 버전을 확인합니다:


```bash
node -v
npm -v
```


두 명령 모두 버전 번호를 반환해야 합니다.


### 4.4. Npm으로 Pears 설치


Npm*을 사용할 수 있게 되면 시스템에 Pears CLI을 전역적으로 설치할 수 있습니다. 그러면 어느 디렉토리에서나 `pear` 명령을 실행할 수 있습니다.


```bash
npm install -g pear
```


### 4.5. 배 초기화


설치 후 터미널에서 다음 명령을 실행하면 됩니다:


```bash
pear
```


처음 시작할 때 Pears는 피어 투 피어 네트워크에 연결하여 필요한 구성 요소를 다운로드합니다. 이 과정에는 중앙 서버가 필요하지 않으며 다른 피어에서 파일을 직접 검색합니다.


다운로드가 완료되면 명령을 다시 실행하여 모든 것이 작동하는지 확인합니다:


```bash
pear
```


모든 것이 올바르게 설치되면 사용 가능한 명령어 목록과 함께 Pears 도움말 메뉴가 나타납니다.


### 4.6. 키트로 배 테스트하기


Pears가 완전히 작동하는지 확인하기 위해 이미 네트워크에서 사용 가능한 P2P 애플리케이션(예: Holepunch의 오픈 소스 메시징 및 화상 회의 소프트웨어인 Keet)을 실행할 수 있습니다.


```bash
pear run pear://keet
```


이 명령은 중앙 서버를 사용하지 않고 Pears 네트워크에서 직접 Keet 앱을 로드합니다. Keet이 성공적으로 실행되면 Pears 설치가 완전히 작동한다는 의미입니다.


이제 macOS 시스템에서 피어투피어 애플리케이션을 실행하고 호스팅할 준비가 되었습니다.


## 5. 배에서 요금제 ₿ 아카데미를 사용하는 방법


Pears가 설치되어 실행 중이면 P2P 네트워크를 통해 **Plan ₿ Academy** 플랫폼을 바로 실행할 수 있습니다. 터미널에서 다음 명령을 실행하기만 하면 됩니다(Linux, Windows 및 macOS에서도 동일한 명령이 작동합니다):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


로딩이 완료되면 중앙 서버에 의존하지 않고도 기존 웹사이트처럼 사용할 수 있는 Plan ₿ Academy가 Pears 환경 내에서 열립니다.


![Image](assets/fr/14.webp)


## 6. 배에 씨앗을 뿌리는 방법 ₿ 아카데미


Pears 네트워크에서 *seed* 애플리케이션을 재배포한다는 것은 자신의 컴퓨터에서 다른 피어에게 애플리케이션을 재배포하는 것을 의미합니다. 실제로 ₿ 아카데미를 seed으로 설정하면 컴퓨터가 중앙 서버에 의존하지 않고도 다른 사용자가 애플리케이션을 다운로드할 수 있는 데이터 소스가 됩니다.


이 메커니즘은 Pears 네트워크에서 애플리케이션의 복원력과 검열 저항성을 강화합니다. 애플리케이션의 피어 seed가 많을수록 일부 원본 노드가 오프라인 상태가 되더라도 더 많은 가용성과 탈중앙화가 이루어집니다.


Plan ₿ Academy를 배포하려면 다음 명령을 실행하기만 하면 됩니다:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


이 명령이 활성 상태로 유지되는 한 디바이스는 애플리케이션의 파일 배포에 참여합니다. 터미널을 닫으면 공유 프로세스가 중지됩니다.


다시 시작한 후에도 시딩을 계속하려면 백그라운드에서 명령을 실행하거나 시스템 서비스(예: Linux의 systemd 서비스, macOS의 LaunchAgent 또는 Windows의 예약된 작업)를 생성할 수 있습니다. 이러한 방법을 사용하면 시스템 시작 시 Plan ₿ Academy 애플리케이션이 자동으로 시딩을 재개합니다.


Plan ₿ Academy on Pears의 분산 배포에 기여하고 Bitcoin 교육이 진정한 검열에 저항할 수 있도록 도와주셔서 감사합니다!