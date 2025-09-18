---
name: Ubuntu
description: Windows의 대안으로 우분투를 설치하고 사용하기 위한 완벽한 가이드
---
![cover](assets/cover.webp)


## 소개


운영체제(OS)는 컴퓨터의 모든 리소스를 관리하는 주요 소프트웨어입니다. 우분투와 같은 대체 운영 체제를 선택하면 보안, 비용, 개인정보 보호 측면에서 많은 이점을 얻을 수 있습니다.


### 왜 우분투인가?




- 강화된 보안**: Linux 배포판은 보안과 견고함으로 유명합니다
- 비용 없음**: 우분투 및 대부분의 Linux 배포판은 무료입니다
- 대규모 커뮤니티**: 포럼과 튜토리얼을 통해 도움을 줄 준비가 되어 있는 사용자 커뮤니티
- 개인정보 보호**: 투명성 향상을 위한 오픈 소스 시스템
- 단순성**: 사용자 친화적인 Interface 및 사용 편의성
- 풍부한 에코시스템**: 광범위한 오픈 소스 소프트웨어 카탈로그
- 정기 지원**: Canonical의 보안 업데이트


## 설치 및 구성


### 1. 전제 조건


**필요 장비: **




- 최소 12GB의 USB 키
- 사용 가능한 용량이 25GB 이상인 컴퓨터


### 2. 다운로드




- Ubuntu.com/download](https://ubuntu.com/download)로 이동합니다
- 안정 버전 선택(LTS 권장)
- ISO 이미지 다운로드


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3. 부팅 가능한 USB 키 만들기


발레나 에처와 같은 여러 도구를 사용할 수 있습니다:




- 발레나 에처] 다운로드 및 설치(https://etcher.balena.io/)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- Balena Etcher를 연 다음 Ubuntu ISO 이미지를 선택합니다
- 대상 미디어로 USB 키 선택
- 플래시를 클릭하고 프로세스가 완료될 때까지 기다립니다


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. 우분투 설치 및 보안


**4.1 USB 메모리 스틱에서 부팅** (프랑스어)




- 컴퓨터 끄기
- USB 키(우분투 포함)를 연결합니다
- 컴퓨터를 켭니다. 최신 PC의 경우 시스템이 USB 부팅 키를 자동으로 인식해야 합니다. 그렇지 않은 경우 BIOS/UEFI 액세스 키(브랜드에 따라 일반적으로 F2, F12 또는 Delete 키)를 누른 상태로 재부팅하세요
 - BIOS/UEFI 메뉴에서 USB 키를 부팅 장치로 선택합니다
 - 저장하고 다시 시작


**4.2 설치 시작** (프랑스어)


**시작 화면**


USB 키로 부팅할 때 이 화면이 표시되며, 이 화면에서 우분투를 시작할 수 있습니다.


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**언어 선택**


설치 및 시스템에 대해 선호하는 언어를 선택합니다.


![Sélection de la langue](assets/fr/07.webp)


**접근성 옵션**


필요한 경우 접근성 옵션(화면 리더, 고대비 등)을 구성합니다.


![Options d'accessibilité](assets/fr/08.webp)


**키보드 구성**


키보드 레이아웃을 선택합니다. 테스트 필드를 사용하여 키가 구성과 일치하는지 확인할 수 있습니다.


![Configuration du clavier](assets/fr/09.webp)


**네트워크 연결**


설치 중에 Wi-Fi 또는 유선 네트워크에 연결하여 업데이트를 다운로드하세요.


![Configuration réseau](assets/fr/10.webp)


**설치 유형**


설치하지 않고 테스트하려면 "Ubuntu 사용해보기" 또는 "Ubuntu 설치" 중에서 선택합니다.


![Choix du type d'installation](assets/fr/11.webp)


**설치 방법**


대화형 설치를 선택합니다.


![Mode d'installation](assets/fr/12.webp)


**애플리케이션 선택**


기본 설치 또는 확장된 애플리케이션 중에서 선택합니다.


![Sélection des applications](assets/fr/13.webp)


**타사 애플리케이션**


추가 드라이버 및 독점 소프트웨어를 설치할지 여부를 결정합니다.


![Installation applications tierces](assets/fr/14.webp)


**파티션 유형**


두 가지 주요 옵션이 있습니다:




- "디스크 지우고 우분투 설치": 우분투에 전체 디스크를 사용합니다
- "수동 설치: Windows로 듀얼 부팅을 만들거나 파티션을 사용자 지정하세요


![Choix du partitionnement](assets/fr/15.webp)


**사용자 계정 생성**


Ubuntu 계정의 사용자 이름과 비밀번호를 설정합니다.


![Création du compte](assets/fr/16.webp)


**시간대**


시스템 시간을 설정할 지역을 선택합니다.


![Sélection du fuseau horaire](assets/fr/17.webp)


**설치 요약**


최종 설치를 시작하기 전에 모든 선택 사항을 확인하세요. '설치'를 클릭하면 프로세스가 시작됩니다.


![Résumé de l'installation](assets/fr/18.webp)


**4.3 설치 후 Ubuntu 업그레이드** (프랑스어)


시스템을 업데이트하는 것은 새로 설치한 후 중요한 단계입니다. 두 가지 옵션이 있습니다:


**옵션 1: 그래픽 사용자 Interface**을 통한 방법




- 애플리케이션 메뉴에서 '소프트웨어 및 업데이트'를 검색합니다
- 애플리케이션이 사용 가능한 업데이트를 자동으로 확인합니다
- 화면의 안내에 따라 업데이트를 설치하세요


**옵션 2: 터미널을 통해**




- 터미널 열기(Ctrl + Alt + T)
- 다음 명령을 입력하여 사용 가능한 업데이트를 확인합니다:


```bash
sudo apt update
```




- 메시지가 표시되면 비밀번호를 입력합니다
- 업데이트를 설치하려면 다음과 같이 입력합니다:


```bash
sudo apt upgrade
```




- 'Y'를 입력한 다음 Enter 키를 입력하여 설치를 확인합니다


### 5. 기본 작업 찾기


**5.1 인터넷 검색**


기본적으로 시작 표시줄에 Firefox가 있는 경우가 많습니다.


Firefox를 실행하고 브라우징을 시작합니다.


다른 브라우저(Chrome, Brave 등)는 소프트웨어 관리자 또는 .deb 패키지를 통해 설치할 수 있습니다.


**5.2 워드 프로세싱**


우분투에는 LibreOffice 제품군(워드 프로세싱용 Writer)이 함께 제공됩니다.


열려면 다음과 같이 하세요: 활동 > "LibreOffice Writer"를 검색하거나 표시줄에 아이콘이 나타나면 클릭합니다.


다양한 형식(.docx 포함)의 문서를 만들고, 편집하고, 저장할 수 있습니다.


**5.3 애플리케이션 설치**


소프트웨어 관리자('우분투 소프트웨어'라고 함): 애플리케이션 검색 및 설치를 위한 그래픽 Interface.


터미널에서 다음 명령을 사용합니다:


```bash
sudo apt install nom-du-paquet
```


예시:


```bash
sudo apt install vlc
```


### 6. 결론 및 추가 리소스


이제 시스템 보안, 브라우징, 오피스 작업, 소프트웨어 설치, OS 최신 버전 유지 등 일상에서 우분투를 사용할 준비가 되셨습니다!


디지털 생활의 보안을 한 단계 더 강화하려면 개인 정보 보호에 완벽하게 적합하고 우분투 설치를 보완하는 암호화 메시징 서비스를 살펴볼 것을 권장합니다:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2