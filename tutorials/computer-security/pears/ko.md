---
name: 배
description: Pears에서 애플리케이션을 설치하고 사용하려면 어떻게 해야 하나요?
---

![cover](assets/cover.webp)



이 튜토리얼에서는 **홀펀치**가 개발하고 **테더**가 지원하는 피어투피어(P2P) 기술인 **Pears**에서 애플리케이션을 실행하는 방법을 배워보겠습니다. 목표는 간단합니다. 중앙화된 인프라(서버, 호스트, 중개자)에 의존하지 않고 웹 애플리케이션을 배포하고 사용할 수 있도록 하는 것입니다. 즉, 클라우드 제공업체가 문을 닫거나 국가가 도메인을 차단하더라도 애플리케이션은 네트워크 피어들 사이에서 계속 사용할 수 있습니다.



## 1. 배란 무엇인가요?



Pears는 피어 투 피어 애플리케이션을 위한 런타임 환경, 개발 도구 및 배포 플랫폼입니다. 이 오픈 소스 도구를 사용하면 서버나 인프라 없이 사용자 간에 직접 소프트웨어를 빌드, 공유 및 실행할 수 있습니다. 구체적으로 말하면, 중앙 서버에서 애플리케이션을 호스팅하는 대신 각 사용자가 네트워크 노드가 되어 애플리케이션과 데이터의 일부를 다른 피어와 공유한다는 의미입니다. 전체 시스템은 분산 네트워크를 형성하며, 각 인스턴스는 서비스 접근성을 유지하기 위해 협력합니다.



![Image](assets/fr/01.webp)



이 접근 방식은 Holepunch에서 개발한 모듈식 소프트웨어 브릭 세트를 기반으로 합니다:




- Hypercore**: 중앙 데이터베이스 없이 데이터 일관성과 보안을 보장하는 분산형 로그입니다.
- Hyperbee**: 효율적인 데이터 정리와 검색을 위한 Hypercore 기반의 인덱서입니다.
- Hyperdrive**: 애플리케이션 파일을 저장하고 피어 간에 동기화하는 데 사용되는 분산 파일 시스템입니다.
- 하이퍼스웜** 및 **하이퍼DHT**: 중앙 서버 없이 전 세계 피어 간의 검색 및 연결을 지원하는 네트워크 계층입니다.
- Secretstream**: 두 피어 간의 교환을 보호하기 위한 E2E 암호화 프로토콜입니다.



이러한 구성 요소를 결합하여 Pears는 각 사용자가 네트워크에 적극적으로 참여하는 자율적이고 암호화된 분산형 애플리케이션을 만들 수 있습니다. 이러한 분산형 아키텍처는 인프라 비용, 검열 위험 및 SPOF(*단일 장애 지점*)를 제거합니다.



## 2. 프로젝트의 시작과 철학



홀펀치는 마티아스 부스(Mathias Buus)와 파올로 아르도이노(Tether의 CEO이자 비트파이넥스의 CTO)가 설립한 회사로, 피어 투 피어 로직을 Bitcoin 이상으로 확장한다는 사명을 가지고 개발 중입니다. 이들의 야망은 모든 애플리케이션이 승인 없이, 서버 없이, 중개자 없이 실행될 수 있는 "P2P 인터넷"을 구축하는 것입니다. 홀펀치는 이미 완전한 P2P 화상 회의 및 메시징 애플리케이션인 **Keet**의 뒤를 잇고 있습니다.



*이 Pears 설치 튜토리얼은 운영 체제에 따라 여러 섹션으로 나뉩니다. 사용 중인 환경에 해당하는 섹션으로 바로 이동하여 적절한 지침을 따르세요




- 리눅스(데비안)** → 파트 **3**
- Windows** → 파트 **4**
- macOS** → 파트 **5**



## 3. Linux(Debian)에 Pears를 설치하는 방법



Debian 시스템에 Pears를 설치하는 것은 비교적 간단하지만 몇 가지 전제 조건이 필요하며, 이 섹션에서 자세히 설명합니다.



### 3.1. 시스템 업데이트



무엇보다도 시스템이 최신 상태인지 확인하는 것이 중요합니다.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. 설치 종속성



Pears는 특정 시스템 라이브러리, 특히 베어 자바스크립트 런타임에서 사용하는 `libatomic1`에 의존합니다. 다음 명령어로 설치하세요:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. NVM을 통해 Node.js 및 npm을 설치합니다



Pears는 *Node.js* 패키지 매니저인 *npm*을 통해 배포됩니다. Pears가 작동하기 위해 *Node.js*에 직접적으로 의존하지는 않지만 설치에는 필요합니다. Linux에 *Node.js*를 설치하는 권장 방법은 여러 버전의 Node를 병렬로 관리할 수 있는 *NVM*(*Node 버전 관리자*)입니다.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



그런 다음 터미널을 다시 로드하여 *NVM*을 활성화합니다:



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



NVM*이 설치되어 있는지 확인합니다:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



그런 다음 안정적인 버전의 *Node.js*(예: 현재 LTS)를 설치합니다:



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Node.js* 및 *npm* 설치를 확인합니다:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 npm으로 Pears 설치하기



Npm*을 사용할 수 있게 되면 시스템에 Pears CLI를 전역적으로 설치할 수 있습니다. 그러면 어느 디렉토리에서나 `pear` 명령을 실행할 수 있습니다.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. 배 초기화



설치 후 터미널에서 다음 명령을 실행하면 됩니다:



```bash
pear
```



처음 시작할 때 Pears는 피어 투 피어 네트워크에 연결하여 필요한 구성 요소를 다운로드합니다. 이 과정에는 중앙 서버가 필요하지 않으며 다른 피어에서 직접 파일을 가져옵니다.



![Image](assets/fr/10.webp)



다운로드가 완료되면 명령을 다시 실행하여 모든 것이 제대로 작동하는지 확인합니다:



```bash
pear
```



![Image](assets/fr/11.webp)



모든 것이 올바르게 설치되면 사용 가능한 명령어 목록과 함께 Pears 도움말이 표시됩니다.



### 3.6. 키트로 배 테스트하기



Pears가 완전히 작동하는지 확인하려면 홀펀치의 오픈 소스 메시징 및 화상 회의 소프트웨어인 Keet과 같이 네트워크에서 이미 사용 가능한 P2P 애플리케이션을 실행하면 됩니다.



```bash
pear run pear://keet
```



이 명령은 중앙 서버를 거치지 않고 Pears 네트워크에서 직접 Keet 애플리케이션을 로드합니다. Keet이 올바르게 실행되면 Pears 설치가 완전히 작동하는 것입니다.



![Image](assets/fr/12.webp)



이제 Linux 시스템에서 Pears로 피어 투 피어 애플리케이션을 실행하고 호스팅할 준비가 되었습니다.



## 4. Windows에 Pears를 설치하는 방법



Windows에 Pears를 설치하는 것은 Linux에서와 마찬가지로 쉽지만 몇 가지 특별한 도구가 필요합니다.



*Linux를 사용하는 경우 6단계*로 건너뛸 수 있습니다



### 4.1. 관리자 모드에서 PowerShell을 엽니다



먼저 관리자 권한으로 PowerShell 을 실행합니다:




- 시작 메뉴를 클릭합니다;
- PowerShell 을 입력합니다;
- "*윈도우 파워셸*"을 마우스 오른쪽 버튼으로 클릭합니다;
- "*관리자 권한으로 실행*"을 선택합니다.



![Image](assets/fr/15.webp)



### 4.2. NVS 다운로드



배는 *Node.js* 패키지 매니저인 *npm*을 통해 설치됩니다. Windows에서는 홀펀치에서 권장하는 방법은 *NVS*(*노드 버전 전환기*)를 사용하는 것인데, 이는 이 시스템에서 *NVM*보다 더 안정적입니다.



PowerShell에서 다음 명령을 실행하여 최신 버전의 *NVS*를 설치합니다:



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. Node.js를 설치합니다



설치가 완료되면 PowerShell을 다시 시작하고 다음 명령을 입력합니다:



```powershell
nvs
```



사용 가능한 *Node.js* 버전 목록이 표시됩니다. 키보드의 `a` 키를 눌러 첫 번째 버전을 선택합니다.



![Image](assets/fr/17.webp)



*Node.js*가 설치됩니다.



![Image](assets/fr/18.webp)



### 4.4. 설치 확인



Node.js* 및 *npm*에 액세스할 수 있는지 확인합니다:



```powershell
node -v
npm -v
```



두 명령 모두 버전 번호를 반환해야 합니다.



![Image](assets/fr/19.webp)



### 4.5. Npm으로 Pears 설치하기



Node.js*와 *npm*을 사용할 수 있게 되면 시스템에 **Pears CLI**를 전역적으로 설치합니다:



```powershell
npm install -g pear
```



이렇게 하면 글로벌 *npm* 디렉터리에 `pear` 바이너리가 설치됩니다.



![Image](assets/fr/20.webp)



### 4.6. 배 확인 및 초기화



설치가 완료되면 을 실행합니다:



```powershell
pear
```



처음 실행하면 Pears는 피어 투 피어 네트워크에서 필요한 구성 요소를 자동으로 다운로드합니다. 이 과정은 잠시 걸릴 수 있습니다.



![Image](assets/fr/21.webp)



모든 것이 정상적으로 진행되었다면 사용 가능한 하위 명령(실행, seed, 정보...) 목록이 있는 CLI Pears 도움말 화면이 표시될 것입니다.



### 4.7. 키트로 배 테스트하기



Pears가 완전히 작동하는지 확인하려면 홀펀치의 오픈 소스 메시징 및 화상 회의 소프트웨어인 Keet과 같이 네트워크에서 이미 사용 가능한 P2P 애플리케이션을 실행하면 됩니다.



```bash
pear run pear://keet
```



이 명령은 중앙 서버를 거치지 않고 Pears 네트워크에서 직접 Keet 애플리케이션을 로드합니다. Keet이 올바르게 실행되면 Pears 설치가 완전히 작동하는 것입니다.



![Image](assets/fr/22.webp)



이제 Windows 시스템에서 Pears를 사용하여 피어 투 피어 애플리케이션을 실행하고 호스팅할 준비가 되었습니다.



## 5. MacOS에 Pears를 설치하려면 어떻게 하나요?



MacOS에 Pears를 설치하는 방법은 Linux에 설치하는 방법과 비슷하지만, Apple 환경에 따라 몇 가지 조정이 필요합니다. 이러한 단계를 함께 알아보세요.



*Linux 또는 Windows를 사용 중이고 이미 Pears를 설치한 경우 **6단계**.*로 바로 진행할 수 있습니다



### 5.1. 시스템 요구 사항 확인



설치하기 전에 시스템에 *Xcode 명령줄 도구*가 설치되어 있는지 확인하세요. 이 패키지는 _Node.js_와 그 종속 요소에 필요한 컴파일 도구를 제공합니다.



이렇게 하려면 키보드 단축키 `Cmd + 스페이스 바`를 사용하여 터미널을 연 다음 `Terminal`을 입력하고 `Enter` 키를 누릅니다. 그런 다음 터미널에 이 명령을 입력하여 설치를 시작할 수 있습니다:



```bash
xcode-select --install
```



도구가 이미 시스템에 설치되어 있는 경우 macOS에서 알려줍니다.



### 5.2. NVM 설치



Pears는 *Node.js* 패키지 매니저인 *npm*을 통해 배포됩니다. Pears가 작동하기 위해 *Node.js*에 직접적으로 의존하지는 않지만 설치를 위해 필요합니다. MacOS에서 *Node.js*를 설치하는 권장 방법은 여러 버전의 Node를 동시에 관리할 수 있는 *NVM*(*Node 버전 관리자*)입니다.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



그런 다음 터미널을 다시 로드하여 *NVM*을 활성화합니다:



```bash
source ~/.zshrc
```



Zsh*가 아닌 *bash*를 사용하는 경우 실행합니다:



```bash
source ~/.bashrc
```



그런 다음 *NVM*이 설치되어 있는지 확인합니다:



```bash
nvm --version
```



터미널은 시스템에 설치된 *NVM*의 버전을 반환해야 합니다.



### 5.3. Node.js와 npm을 설치합니다



그런 다음 안정적인 버전의 *Node.js*(예: 현재 LTS)를 설치합니다:



```bash
nvm install --lts
```



설치가 완료되면 설치된 버전을 확인합니다:



```bash
node -v
npm -v
```



두 명령 모두 버전 번호를 반환해야 합니다.



### 5.4 npm으로 Pears 설치하기



Npm*을 사용할 수 있게 되면 시스템에 Pears CLI을 전역적으로 설치할 수 있습니다. 그러면 어느 디렉토리에서나 `pear` 명령을 실행할 수 있습니다.



```bash
npm install -g pear
```



### 5.5. 배 초기화



설치 후 터미널에서 다음 명령을 실행하면 됩니다:



```bash
pear
```



처음 시작할 때 Pears는 피어 투 피어 네트워크에 연결하여 필요한 구성 요소를 다운로드합니다. 이 과정에는 중앙 서버가 필요하지 않으며 다른 피어에서 직접 파일을 가져옵니다.



다운로드가 완료되면 명령을 다시 실행하여 모든 것이 제대로 작동하는지 확인합니다:



```bash
pear
```



모든 것이 올바르게 설치되면 사용 가능한 명령어 목록과 함께 Pears 도움말이 표시됩니다.



### 5.6. 키트로 배 테스트하기



Pears가 완전히 작동하는지 확인하려면 홀펀치의 오픈 소스 메시징 및 화상 회의 소프트웨어인 Keet과 같이 네트워크에서 이미 사용 가능한 P2P 애플리케이션을 실행하면 됩니다.



```bash
pear run pear://keet
```



이 명령은 중앙 서버를 거치지 않고 Pears 네트워크에서 직접 Keet 애플리케이션을 로드합니다. Keet이 올바르게 실행되면 Pears 설치가 완전히 작동하는 것입니다.



이제 macOS 시스템에서 피어투피어 애플리케이션을 실행하고 호스팅할 준비가 되었습니다.



## 6. Pears에서 애플리케이션을 사용하려면 어떻게 해야 하나요?



Pears가 실행되면 다음 명령을 사용하여 원하는 애플리케이션을 바로 실행할 수 있습니다:



```bash
pear run pear://[KEY]
```



사용하려는 애플리케이션 키를 `[KEY]`로 바꾸기만 하면 됩니다.



![Image](assets/fr/13.webp)



Pears에서 Plan ₿ Academy 플랫폼을 실행하는 방법을 알아보려면 이 종합 튜토리얼을 확인하세요:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Pears에서 방금 실행한 Keet 메시징 애플리케이션을 사용하는 방법을 알아보려면 이 튜토리얼 을 확인하세요:



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b