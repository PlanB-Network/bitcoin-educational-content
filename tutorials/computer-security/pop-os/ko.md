---
name: Pop!_OS
description: Linux 배포판인 Pop!_OS 설치 가이드
---

![cover](assets/cover.webp)



## 소개



Pop!OS는 미국의 개발자, 디자이너 및 고급 사용자를 위한 컴퓨터 전문 제조업체인 **System76**에서 개발한 Linux 기반 운영 체제입니다.



현대적이고 안정적인 고성능 환경을 제공하도록 설계된 Pop!OS는 단순한 사용 환경, 강력한 도구, 생산성에 중점을 둔 것이 특징입니다.



### System76은 누구인가요?



System76은 2005년에 설립되어 덴버에 본사를 둔 미국 회사로, Linux용으로 특별히 설계된 노트북, 데스크톱 및 서버 제조를 전문으로 합니다.



기존 제조업체와 달리 System76은 개방적이고 수리 가능하며 소프트웨어의 자유를 지향하도록 설계된 기계를 개발합니다.



System76은 컴퓨터만 만드는 회사가 아닙니다.



이 회사는 또한 :




- 자체 리눅스 기반 운영체제인 Pop!OS**를 출시했습니다;
- Pop!OS에서 사용하는 최신 고성능 데스크톱 환경인 COSMIC** ;
- 코어부트 기반의 오픈 소스 펌웨어인 오픈 펌웨어**;
- 개발자와 디자이너를 위한 도구입니다.



목표는 Apple 에코시스템에 필적하는 고품질의 하드웨어 및 소프트웨어 통합을 제공하되, 완전히 개방적이고 Linux를 중심으로 하는 것입니다.



## 현대적이고 안정적이며 접근성이 뛰어난 시스템



Pop!OS는 Ubuntu의 기반 위에 구축되어 뛰어난 안정성, 광범위한 하드웨어 호환성, 거대한 소프트웨어 에코시스템에 대한 액세스를 제공합니다.


새로운 사용자도 유연하고 직관적이며 사용자 정의할 수 있도록 설계된 우아한 인터페이스인 COSMIC 데스크톱을 제공합니다.



## 개발자, 디자이너 및 까다로운 사용자를 위한 이상적인 선택



Pop!OS는 특히 :





- 개발자(사전 설치된 도구, 고급 타일링 관리),
- nvidia 또는 AMD 그래픽 카드를 사용하는 사용자,
- 신뢰할 수 있는 시스템을 찾는 학생과 전문가에게 적합합니다,
- 간단한 전환을 원하는 Windows 사용자.



자동 타일링, 깔끔한 소프트웨어 센터, 통합 생산성 도구가 포함되어 있어 일상적인 사용이 더욱 쉬워집니다.



## Pop!OS 주요 기능





- 정기적인 업데이트를 통해 최적화된 성능**을 제공합니다.
- 두 가지 ISO 버전 사용 가능**: 표준 및 Nvidia 최적화.
- 강화된 보안**(설치 시 LUKS 암호화 사용 가능).
- 인체공학적이고 현대적인 Interface COSMIC**.
- Ubuntu 및 Flatpak 소프트웨어와 높은 호환성**을 자랑합니다.



## POP!OS 안전하게 다운로드



### 1. 전제 조건



POP!OS를 다운로드하여 설치하기 전에 설치 환경을 올바르게 준비해야 할 몇 가지 사항이 있습니다.



### 필요한 장비





- 호환되는 컴퓨터**: 인텔 또는 AMD 프로세서, 인텔/AMD/엔비디아 GPU.
- 최소 4GB RAM**(쾌적한 사용을 위해 8GB 권장).
- 최소 20GB의 여유 공간**(40GB 이상 권장).
- 설치 미디어를 생성하기 위한 최소 4GB USB 키**가 필요합니다.



### 인터넷 연결



안정적인 연결은 에 유용합니다:





- iSO 이미지를 다운로드합니다,
- 설치 후 업데이트를 설치합니다.



Pop!OS는 연결 없이도 실행할 수 있지만, 인터넷을 통해 설치하는 것이 훨씬 더 원활합니다.



### 데이터 백업



Pop!OS를 다른 시스템(Windows, Ubuntu 등)으로 대체하거나 공존시킬 경우, 계속 진행하기 전에 중요한 파일을 백업하는 것이 좋습니다.



### Nvidia GPU가 있는지 확인(해당되는 경우)



Nvidia 그래픽 카드가 장착된 컴퓨터의 경우 Nvidia 드라이버가 포함된 특수 ISO 이미지를 다운로드해야 합니다.


이 점검은 매우 간단합니다:





- pC 사양을 참고하세요,
- 를 클릭하거나 시스템 설정에서 그래픽 카드 모델을 조회할 수 있습니다.



### 공식 웹사이트에서 다운로드



Pop!OS ISO 이미지는 공식 System76 페이지에서 직접 다운로드해야 합니다: [system76.com/pop](https://system76.com/pop/).



이 페이지는 항상 사용자의 하드웨어에 맞게 조정된 최신 버전을 제공합니다.



![capture](assets/fr/03.webp)



### 버전을 선택하세요: 표준 또는 엔비디아 또는 라즈베리 파이(ARM64)



Pop!OS는 세 가지 버전으로 제공됩니다:



### 표준 버전



를 사용하는 컴퓨터에 권장됩니다:





- 인텔 또는 AMD 프로세서;
- 통합 인텔 또는 AMD GPU;
- aMD 라데온 그래픽 카드.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia 버전



Nvidia 그래픽 카드가 장착된 컴퓨터에 권장됩니다.


이 이미지에는 이미 Nvidia 드라이버가 포함되어 있어 설치가 더 쉬워지고 그래픽 문제가 줄어듭니다.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 라즈베리 파이 버전(ARM64)



라즈베리 파이 4 및 400(ARM 프로세서)의 경우.


ARM 아키텍처에 맞게 조정된 이 버전은 이러한 미니 컴퓨터를 위한 특정 버전입니다.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## 부팅 가능한 USB 키 만들기



다음과 같은 여러 도구를 사용할 수 있습니다:





- 발레나 에처](https://etcher.balena.io/)를 다운로드하여 설치합니다.



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Balena Etcher를 연 다음 Pop!OS ISO 이미지를 선택합니다.
- 대상 미디어로 USB 키를 선택합니다.
- Flash를 클릭하고 프로세스가 완료될 때까지 기다립니다.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Pop!OS 설치 및 보안



### USB 키로 부팅하기





- 컴퓨터 전원을 끕니다.
- USB 키(Pop!OS 포함)를 연결합니다.
- 컴퓨터를 켭니다. 최신 PC의 경우 시스템이 USB 부팅 키를 자동으로 인식합니다. 그렇지 않은 경우 BIOS/UEFI 액세스 키(브랜드에 따라 보통 F2, F12 또는 Delete 키)를 누른 상태로 재부팅하세요.
  - BIOS/UEFI 메뉴에서 USB 키를 부팅 장치로 선택합니다.
  - 저장하고 다시 시작합니다.



### 설치 시작하기



부팅 가능한 USB 키를 시동 장치로 선택하면 컴퓨터가 Pop!OS Live 환경으로 부팅됩니다.



언어를 선택합니다.



![Capture](assets/fr/10.webp)



위치를 선택합니다.



![Capture](assets/fr/11.webp)



키보드 입력 언어를 선택합니다.



![Capture](assets/fr/12.webp)



키보드 레이아웃을 선택합니다.



![Capture](assets/fr/13.webp)



표준 설치의 경우 '새로 설치' 옵션을 선택합니다. 이 옵션은 Linux를 처음 사용하는 사용자에게 가장 적합하지만, 대상 드라이브의 모든 내용이 삭제된다는 점에 유의하세요. 또는 `데모 모드 시도`를 선택하여 라이브 환경에서 Pop!OS를 계속 테스트할 수 있습니다.



![Capture](assets/fr/14.webp)



사용자 지정(고급)`을 선택해 GParted에 액세스합니다. 이 도구를 사용하면 이중 부팅, 별도의 `/home` 파티션 생성 또는 `/tmp` 파티션을 다른 드라이브에 배치하는 등의 고급 기능을 구성할 수 있습니다.



'지우고 설치'를 클릭하여 선택한 드라이브에 Pop!OS를 설치합니다.



![Capture](assets/fr/15.webp)



### 사용자 계정 구성



설치 프로그램의 다음 섹션에서는 새 운영 체제에 로그온할 수 있도록 사용자 계정 생성 과정을 안내합니다.



전체 이름(대문자 또는 소문자 중 원하는 텍스트 포함)과 사용자 이름(소문자이어야 함)을 입력합니다:



![Capture](assets/fr/16.webp)



계정이 생성되면 새 비밀번호를 설정하라는 메시지가 표시됩니다.



![Capture](assets/fr/17.webp)



### 전체 디스크 암호화



시스템 디스크 암호화는 필수는 아니지만, 누군가가 장치에 무단으로 물리적으로 액세스하는 경우 사용자 데이터의 보안을 보장합니다.



'암호화 비밀번호가 사용자 계정 비밀번호와 동일함'을 체크하면 로그인 비밀번호를 사용하여 드라이브를 암호화할 수 있습니다. 이 상자의 선택을 취소하고 하단의 `비밀번호 설정`을 선택할 수도 있습니다. 디스크 암호화 프로세스를 무시하려면 `암호화 안 함`을 선택합니다.



![Capture](assets/fr/18.webp)



'비밀번호 설정' 버튼을 선택한 경우, 암호화 비밀번호를 설정하라는 메시지가 추가로 표시됩니다.



설치 프로그램의 다음 단계로 진행합니다. 이제 디스크에 Pop!OS 설치가 시작됩니다.



![Capture](assets/fr/19.webp)



설치가 완료되면 컴퓨터를 다시 시작하고 로그인하여 사용자 계정 구성 프로세스를 완료합니다.



시작 시 라이브 USB 키에 우선순위를 부여하도록 부팅 순서를 변경한 경우 컴퓨터를 완전히 끄고 설치 USB 키를 제거하세요. 듀얼 부팅 모드에 있는 경우 적절한 키를 눌러 구성에 액세스하고 Pop!OS 설치가 들어 있는 드라이브를 선택합니다.



![Capture](assets/fr/20.webp)



### NVIDIA 그래픽



인텔/AMD ISO에서 설치한 시스템에 개별 NVIDIA 그래픽 카드가 있거나 나중에 추가한 경우, 최적의 성능을 얻으려면 카드용 드라이버를 수동으로 설치해야 합니다. 명령 터미널에서 다음 명령을 실행하여 드라이버를 설치합니다:



```bash
sudo apt install system76-driver-nvidia
```



Pop!_Shop에서 NVIDIA 그래픽 드라이버를 설치할 수도 있습니다.



![Capture](assets/fr/20.webp)



## 필수 도구 설치



팝!OS는 팝!샵을 통해 다양한 소프트웨어를 제공하지만, 많은 필수 도구는 `apt` 또는 `flatpak`을 통해 터미널을 통해 설치할 수도 있습니다. 완벽한 작업 환경을 위한 주요 도구를 설치하는 방법은 다음과 같습니다.



### 터미널 설치



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### 팝을 통한 설치! Shop(그래픽 인터페이스)을 통해 설치





- 메인 메뉴에서 **Pop!_Shop**을 엽니다.
- 검색창을 사용하여 원하는 애플리케이션을 찾습니다(예: "Brave").
- 각 애플리케이션에 대해 **설치**를 클릭합니다.
- Pop!_Shop은 종속성 및 업데이트를 자동으로 관리합니다.



## 시스템 업데이트



### 옵션 1: 그래픽 사용자 인터페이스(GUI)를 통해



Pop!OS는 간단하고 직관적인 그래픽 업데이트 관리자를 제공합니다.



1. 메인 메뉴**(왼쪽 하단 아이콘)를 클릭합니다.


2. "팝!샵"**을 엽니다.


3. Pop!_Shop에서 **"업데이트"** 탭을 클릭합니다.


4. 시스템에서 사용 가능한 업데이트를 자동으로 확인합니다.


5. 업데이트 설치를 시작하려면 **"모두 업데이트"**를 클릭합니다.


6. 요청이 있는 경우 비밀번호를 입력합니다.


7. 프로세스를 완료한 후 필요한 경우 다시 시작하세요.



### 옵션 2: 터미널을 통해



터미널을 열고 를 입력합니다:



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### 사용자 관리



일상적인 작업에는 sudo 권한이 있는 표준 사용자 계정을 사용하는 것이 좋습니다.



새 사용자를 만들려면 :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



로그아웃했다가 이 새 사용자로 다시 로그인합니다.



### 그래픽 드라이버 관리





- Nvidia 카드의 경우 전용 드라이버가 설치되어 있는지 확인합니다:



```bash
sudo apt install system76-driver-nvidia
```





- AMD/Intel의 경우 일반적으로 드라이버가 기본으로 포함되어 있습니다.



### 방화벽 활성화(UFW)



Pop!OS는 기본적으로 네트워크 트래픽을 차단하지 않습니다. 보안을 강화하려면 UFW를 활성화하세요:



```bash
sudo ufw enable && sudo ufw status verbose
```



### 자동 업데이트 구성



수동 개입 없이 시스템을 최신 상태로 유지할 수 있습니다:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### 모양 및 동작 사용자 지정





- 시스템 설정** → **모양**을 열어 밝거나 어두운 테마를 선택합니다.
- 코스믹 매니저를 통해 활성 코너, 애니메이션 및 확장 기능을 구성하세요.
- 데스크톱 레이아웃을 조정하여 워크플로를 최적화하세요.



### 자동 백업 구성



Pop!OS는 백업용 Deja Dup와 같은 도구를 통합합니다:





- 메뉴에서 **백업**을 실행합니다.
- 외장 드라이브 또는 네트워크 위치를 선택합니다.
- 정기적인 백업을 예약하세요.



### 유용한 GNOME/COSMIC 확장 설치하기



다음은 사용자 환경을 개선하기 위해 권장되는 몇 가지 확장 프로그램입니다:





- 대시 투 도크**: 애플리케이션 바가 항상 표시됩니다.
- GSConnect**: Android와 동기화.
- 클립보드 표시기**: 고급 클립보드 관리.



를 통해 설치합니다:



```bash
sudo apt install gnome-shell-extensions
```



그런 다음 설정에서 활성화합니다.



### 메모리 및 스왑 관리 최적화



스왑 상태를 확인하세요:



```bash
swapon --show
```



필요한 경우 스왑 크기를 늘리거나 스왑 파일을 구성합니다:



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



자동 마운팅을 위해 `/etc/fstab` 파일에 추가합니다.



## 패키지 및 리포지토리 관리



### 패키지 소스 이해



Ubuntu 기반의 Pop!OS는 주로 :





- 공식 Ubuntu** 리포지토리: 가장 안정적인 소프트웨어를 위한 리포지토리입니다.
- System76** 리포지토리: 드라이버, 펌웨어 및 특정 도구용.
- Flatpak**: 다양한 샌드박스 애플리케이션에 액세스하세요.
- Snap**(선택 사항): 또 다른 범용 패키지 형식입니다.



---

### PPA 리포지토리 추가 및 관리



자주 업데이트되는 소프트웨어를 설치하기 위해 특정 PPA(개인 패키지 아카이브)를 추가할 수 있습니다:



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## 결론



Pop!OS는 초보자와 고급 사용자 모두에게 적합한 현대적이고 안정적인 Linux 배포판입니다.



직관적인 COSMIC 인터페이스와 통합 도구 덕분에 개발, 창작, 일상적인 사용 모두에서 유연하고 생산적인 경험을 제공합니다.



이 튜토리얼에서는 준비, 다운로드, 설치, 초기 설정 및 필수 도구 등 주요 단계를 다룹니다.



Pop!OS를 더 자세히 살펴보고 환경을 맞춤 설정하여 최대한 활용하세요.