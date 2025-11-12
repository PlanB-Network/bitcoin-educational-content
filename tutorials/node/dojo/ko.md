---
name: 도장
description: 프라이버시 및 자율성을 위한 오픈소스 Bitcoin 노드
---

![cover](assets/cover.webp)



*이 튜토리얼은 [공식 아시가루 문서](https://ashigaru.rs/docs/)를 기반으로 작성되었으며, 제가 이를 이어받아 확장했습니다. 모든 섹션을 다시 작성하여 명확성을 높이고, 초보자를 위한 그림과 자세한 설명을 추가하여 설치 및 사용법을 더 쉽게 이해할 수 있도록 했습니다*



---

도조는 Bitcoin core 노드를 기반으로 특정 프라이버시 지향 Bitcoin 지갑의 백엔드 서버 역할을 하도록 설계된 오픈 소스 프로그램입니다. 과거에는 Whirlpool(CoinJoin), 리코쳇, 스톤월, 페이님과 같은 고급 개인정보 보호 기능을 제공했던 모바일 Wallet인 사무라이 Wallet와 함께 작동하도록 개발되었습니다. 사무라이 Wallet는 개발자가 체포된 후 현재 개발이 중단되었지만, 커뮤니티의 후계자인 **아시가루 Wallet**가 이를 이어받아 Bitcoin를 사용할 때 데이터를 계속 제어하고자 하는 사용자에게 완벽한 경험을 제공하기 위해 도조에 계속 의존하고 있습니다.



![Image](assets/fr/01.webp)



실질적으로 Dojo는 Wallet과 Bitcoin 네트워크 사이의 게이트웨이 역할을 합니다. Dojo가 없으면 경량 모바일 Wallet이 타사 서버에 쿼리하여 UTXO의 상태와 기록을 확인하거나 트랜잭션을 브로드캐스트해야 합니다. 이는 타사 서버에 대한 의존성과 민감한 데이터(사용된 주소, 금액, 결제 빈도 등)의 유출을 의미합니다. Dojo를 사용하면 이 서버를 직접 호스팅하고 자신의 Bitcoin 노드에 직접 연결할 수 있습니다. 이러한 방식으로 모든 포트폴리오 요청은 중개자 없이 사용자가 제어하는 인프라를 통과하므로 기밀성과 주권이 강화됩니다.



## 도장 개설 요건



도장 서버를 설정하는 데 초강력 컴퓨터가 필요하지 않습니다. 보급형 컴퓨터와 안정적인 인터넷 연결, 24시간 내내 계속 켜둘 수 있는 능력이 있는 사람이라면 누구나 도장을 설정할 수 있습니다.



### 머신 유형 선택



를 사용할 수 있습니다:




- 노트북 ;
- 데스크톱 컴퓨터 ;
- 미니 PC(예: 인텔 NUC, 레노버 씬센터 타이니...).



각 옵션에는 장단점이 있습니다:




- 가격: 리퍼브 미니 PC 또는 데스크톱은 새 노트북보다 저렴한 경우가 많습니다.
- 설치 공간: 미니 PC는 공간을 적게 차지합니다.
- Power Supply: 노트북은 배터리가 탑재되어 있어 미니 PC와 달리 전원이 차단되어도 종료되지 않는다는 장점이 있습니다.
- 업그레이드 가능성: 일반적으로 바본으로 메모리를 추가하거나 Hard 디스크를 쉽게 교체할 수 있습니다.



장비 선택에 대한 자세한 내용은 이 강좌를 수강하는 것을 추천합니다:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### 권장 장비



새 컴퓨터를 구입할 필요는 없습니다. 아래 사양의 리퍼브 컴퓨터는 라즈베리 파이와 같은 단일 보드 전자기기보다 훨씬 더 나은 성능을 제공합니다.



**최소 사양:**




- X86-64 아키텍처(64비트 프로세서).
- 2GHz 듀얼 코어 프로세서 이상.
- 최소 8GB RAM.
- 2TB 이상의 NVMe SSD(Bitcoin의 Blockchain 및 필요한 인덱스 저장용).



** 권장 운영 체제: **




- 우분투 24.04 LTS와 같은 데비안 기반 배포판입니다.



**권장 장비:**




- HP 엘리트데스크 / 엘리트북
- Dell OptiPlex
- 레노버 씽크센터 / 씽크패드
- 인텔 NUC
- 등



다른 하드웨어 구성에서도 도장 서버를 실행하는 것은 완벽하게 가능합니다. 그러나 최상의 성능을 얻고 문제를 제한하려면 위의 권장 사항을 따르는 것이 좋습니다.



이 튜토리얼에서는 인텔 펜티엄 듀얼 코어 G4400T 프로세서, 8GB RAM 및 2TB SSD가 장착된 구형 ThinkCentre Tiny를 사용하겠습니다.



## 1 - 우분투 설치



*이미 구성된 장치에 Dojo를 설치하려는 경우 이 단계를 건너뛰고 바로 2단계로 진행할 수 있습니다*



선택한 하드웨어를 준비했으면 이제 운영 체제를 설치할 차례입니다. 거의 모든 데비안 배포판을 사용할 수 있지만, 저희의 목적에 가장 적합한 LTS 버전의 우분투를 선택하는 것이 좋습니다. 따라야 할 단계는 다음과 같습니다:



### 1.1. 부팅 가능한 USB 키를 생성합니다



이미 작동 중인 컴퓨터(평소 사용하는 컴퓨터)에서 [공식 사이트](https://ubuntu.com/download/desktop)에서 Ubuntu LTS ISO 이미지를 다운로드합니다(작성 시점은 `24.04`이지만 다른 버전이 있으면 가장 최신 버전을 사용하세요).



![Image](assets/fr/02.webp)



이 컴퓨터에 8GB 이상의 USB 키를 삽입한 다음 [Balena Etcher](https://etcher.balena.io/) 등의 소프트웨어를 사용하여 부팅 가능한 키를 생성합니다. 방금 다운로드한 우분투 ISO 이미지를 선택하고 USB 키를 대상 장치로 선택한 다음 생성 프로세스를 시작합니다(몇 분 정도 걸릴 수 있으니 조금만 기다려주세요).



![Image](assets/fr/03.webp)



부팅 가능한 USB 키를 전원이 꺼진 컴퓨터(도조를 실행하려는 컴퓨터)에 삽입합니다. 컴퓨터를 시작하고 즉시 키보드에서 **F12** 또는 **F10**을 눌러(모델에 따라 다름) 부팅 메뉴에 액세스합니다. 그런 다음 컴퓨터 부팅 순서에서 USB 키를 우선 순위 장치로 선택합니다.



![Image](assets/fr/04.webp)



### 1.2. 운영 체제 설치



우분투 홈 화면이 나타납니다. "우분투 시도 또는 설치*"를 선택합니다.



![Image](assets/fr/05.webp)



그런 다음 일반적인 Ubuntu 설치 프로세스를 따르세요:




- 언어를 선택합니다.
- 키보드 유형을 선택합니다.
- RJ45 케이블을 통해 연결된 경우 Wi-Fi를 구성할 필요가 없습니다.
- "*우분투 설치*"를 클릭하고 타사 소프트웨어(Wi-Fi 드라이버, 멀티미디어 코덱 등)를 설치하는 옵션을 선택합니다.
- 마법사가 설치 유형을 묻는 메시지가 표시되면 "*디스크 지우기 및 우분투 설치*"를 선택합니다. **경고**: 이 작업을 수행하면 디스크의 내용이 완전히 지워집니다. 선택한 디스크가 Dojo용 NVMe SSD에 해당하는지 주의 깊게 확인하세요.
- 간단한 사용자 이름(예: "*loic*")을 만듭니다.
- 머신에 이름을 지정합니다(예: "*도장 노드*").
- 강력한 비밀번호를 설정하고 안전하게 보관하세요.
- "*로그인 시 비밀번호 요청*" 옵션을 활성화하여 보안을 강화하세요.
- 시간대를 지정한 다음 "*설치*"를 클릭합니다.
- 설치가 완료될 때까지 기다립니다. 완료되면 시스템이 자동으로 다시 시작됩니다.
- 컴퓨터를 다시 시작할 때 USB 설치 키를 제거합니다.



우분투 설치 프로세스에 대한 자세한 내용은 전용 튜토리얼 을 참조하세요:



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. 시스템 업데이트



처음 부팅한 후 ***Ctrl + Alt + T*** 키 조합을 사용하여 터미널을 열고 다음 명령을 실행하여 시스템을 업데이트합니다:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. 별채 설치



Dojo가 제대로 작동하려면 시스템에 특정 소프트웨어 브릭이 있어야 합니다. 이러한 브릭은 소프트웨어 리포지토리, 통신, 아카이브 압축 해제 및 Docker 컨테이너 내부의 Dojo 실행을 관리하는 데 사용됩니다. 이러한 모든 작업은 터미널에서 수행됩니다.



### 2.1. 준비



다음 명령은 개인 폴더로 돌아갑니다. 일련의 설치를 실행하기 전에 이 작업을 수행하는 것이 좋습니다.



```bash
cd ~/
```



소프트웨어를 설치하기 전에 컴퓨터에서 사용 가능한 소프트웨어 데이터베이스가 최신 상태인지 확인하세요. 이렇게 하면 더 이상 사용되지 않는 버전을 설치하는 것을 방지할 수 있습니다.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. 유틸리티 설치



시스템에 몇 가지 도구를 추가해야 합니다:




- `apt-transport-https`: HTTPS를 통해 패킷을 안전하게 다운로드할 수 있습니다
- 'CA-인증서': 암호화된 연결에 필요한 인증서를 관리합니다
- curl`: 인터넷에서 파일을 검색합니다
- `gnupg-agent`: GPG 키 관리용
- 소프트웨어-속성-공통`: APT 리포지토리 조작을 위한 유틸리티를 제공합니다
- 'unzip': ZIP 형식의 파일 압축 해제



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



설치하는 동안 시스템에서 확인을 요청할 수 있습니다. "*Y*" 키를 누른 다음 "*Enter*"를 누릅니다.



![Image](assets/fr/08.webp)



### 2.3. 토르삭스 설치



토르삭스는 토르 네트워크를 통해 특정 명령을 실행할 수 있도록 하여 통신의 기밀성을 향상시킵니다.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. 도커 및 도커 컴포즈를 설치합니다



Dojo는 Docker 컨테이너 안에서 실행됩니다. 즉, 각 서비스가 독립적인 환경에서 격리되어 유지 관리와 보안이 간소화됩니다. 이를 위해서는 여러 컨테이너를 동시에 관리할 수 있는 Docker와 Docker Compose 도구를 설치해야 합니다.



#### 도커 서명 키 추가



Docker는 자체 디지털 서명 키를 제공합니다. 이 키를 추가하면 다운로드한 패키지의 진위 여부를 확인할 수 있습니다.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### 공식 Docker 리포지토리 추가



다음으로 공식 Docker 패키지를 찾을 수 있는 위치를 시스템에 알려야 합니다. 이 명령은 패키지 관리자 구성에 새 리포지토리를 추가합니다.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### 도커 및 도커 컴포즈 설치하기



이제 주요 Docker 구성 요소를 설치할 수 있습니다.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### 사용자 권한 부여



기본적으로 관리자 권한으로 실행된 명령만 Docker를 시작할 수 있습니다. 더 편리하게 사용하려면 현재 사용자를 "*docker*" 그룹에 추가하는 것이 좋습니다. 이렇게 하면 매번 `sudo`를 입력할 필요 없이 Docker를 사용할 수 있습니다.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. 단일 사용자 생성(선택 사항)



시스템의 보안을 강화하려면 Dojo를 실행하기 위한 별도의 사용자를 만드는 것이 좋습니다. 이렇게 분리하면 Dojo에서 보안 문제가 발생하더라도 기본 계정이 직접적으로 손상되지 않으므로 위험이 제한됩니다.



### 3.1. 사용자 계정 생성



다음 명령은 "*dojo*"라는 새 사용자를 만듭니다. 이 사용자는 홈 디렉터리 `/home/dojo`를 갖게 되며 bash 터미널에 액세스할 수 있습니다. 또한 관리자 명령을 실행할 수 있도록 sudo 그룹에 추가됩니다.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. 비밀번호 설정하기



이 계정에 강력한 비밀번호를 지정하는 것이 중요합니다. Bitwarden과 같은 비밀번호 관리자를 사용하여 12~13자 정도의 긴 비밀번호를 설정하는 것이 가장 이상적입니다.



```bash
sudo passwd dojo
```



그러면 시스템에서 선택한 비밀번호를 입력하라는 메시지가 표시되고 다시 한 번 확인합니다.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. 사용자에게 도커 사용 권한 부여



"*dojo*" 사용자가 Dojo를 실행하는 데 필요한 컨테이너를 실행할 수 있도록 하려면, 그를 Docker 그룹에 추가해야 합니다. 이렇게 하면 각 명령 앞에 `sudo`를 붙여야 하는 번거로움을 피할 수 있습니다.



```bash
sudo usermod -aG docker dojo
```



### 3.4. 시스템 재시작



그룹 변경 사항을 적용하려면 컴퓨터를 다시 시작해야 합니다.



```bash
sudo reboot
```



### 3.5. 새 사용자로 로그인



시스템이 다시 시작되면 ***dojo*** 로그인과 앞서 정의한 비밀번호로 로그인합니다. 이후 모든 단계는 이 전용 계정에서 수행해야 합니다.



## 4. 도장 다운로드 및 확인



Dojo를 설치하기 전에 공식 개발자가 제공한 파일인지, 파일이 수정되지 않았는지 확인해야 합니다. 이 단계에서는 파일 진위 여부와 무결성을 확인하기 위해 PGP와 해시를 사용합니다.



### 4.1. 개발자의 PGP 키를 가져옵니다



Tor를 통해 개발자의 공개키를 다운로드하고 로컬 키체인으로 가져옵니다. 이 키는 Dojo 파일과 관련된 서명을 확인하는 데 사용됩니다.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. 최신 버전의 Dojo를 다운로드합니다



Dojo 소스 코드가 포함된 압축 아카이브를 검색합니다. 이 예제에서 가장 최신 버전은 `1.27.0`입니다. 공식 GitHub 리포지토리(https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases)의 최신 버전에 따라 명령을 수정합니다.



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. 지문 및 서명 다운로드



개발자는 아카이브의 디지털 지문이 나열된 파일과 PGP 키로 서명된 파일을 게시합니다. 파일을 다운로드하여 로컬에서 파일을 비교하세요.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. PGP 서명 확인



가져온 키로 지문 파일이 서명되었는지 확인합니다.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



올바른 결과는 키 `E53AD419B242822F19E23C6D3033D463D6E544F6` 및 관련 Address `dojocoder@pm.me`와 함께 유효한 서명을 표시합니다. 키가 인증되지 않았다는 경고가 표시될 수 있지만 무시해도 됩니다.



반면 서명이 유효하지 않은 경우 즉시 설치 프로세스를 중지하고 처음부터 다시 시작하세요.



![Image](assets/fr/17.webp)



### 4.5. 아카이브 무결성 확인



다운로드한 파일의 SHA256 지문을 계산한 다음 지문 파일을 열어 두 값을 비교합니다.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



두 지문이 동일하면 아카이브가 수정되지 않았다는 것을 확인할 수 있습니다. 지문이 다르면 더 이상 진행하지 말고 파일을 삭제하세요.



![Image](assets/fr/18.webp)



### 4.6. 파일 추출 및 정리



인증이 성공적으로 완료되면 아카이브의 압축을 풀고 Dojo 설치 전용 폴더를 준비할 수 있습니다.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. 불필요한 파일 정리



더 이상 필요하지 않은 임시 파일과 아카이브를 삭제하여 환경을 깨끗하게 유지하세요.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. 도장 구성



Dojo는 포트폴리오와 상호 작용하고 Bitcoin 노드를 관리하기 위해 여러 서비스를 한데 모은 백엔드 서버입니다. 구성은 복잡할 수 있지만, 프로젝트에서는 다음 구성 요소를 자동으로 설치하고 구성하는 간소화된 방법을 제공합니다:




- 도장(기본 API)
- Bitcoin core(Bitcoin 노드 완료)
- BTC-RPC 탐색기(웹 Block explorer)
- 풀크럼 인덱서(블록과 트랜잭션의 빠른 인덱싱)
- 토르 네트워크에서 Fulcrum Electrum 서버 이용 가능
- 로컬 네트워크에서 Fulcrum Electrum 서버 사용 가능
- 관리 자격 증명



### 5.1. 관리 자격 증명



다양한 서비스에 대한 액세스를 보호하려면 몇 가지 고유 식별자를 generate으로 설정해야 합니다:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `mysql_root_password`
- mYSQL_USER
- `mysql_password`
- nODE_API_KEY`
- 노드_관리자_키`
- `NODE_JWT_SECRET`



이러한 식별자는 **고유해야 하며(매우 중요합니다. 여러 서비스에 동일한 비밀번호를 사용해서는 안 됩니다), 숫자, 대문자, 소문자(영숫자)로만 구성되어야 하고, 높은 수준의 보안을 위해 40자 내외의 길이를 유지해야 합니다. 다시 한 번 비밀번호 관리자 사용을 강력히 권장합니다.



### 5.2. 구성 파일에 액세스



Dojo 구성 파일은 `conf/` 폴더에 있습니다. 이 디렉토리로 이동합니다:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core 구성



나노 텍스트 편집기로 Bitcoin core 구성 파일을 엽니다:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



이 파일에 생성된 식별자를 입력합니다:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***'your-ID-here'와 'your-password-here'를 자신의 로그인 정보(강력한 비밀번호 사용)로 바꾸세요



Bitcoin core에서 사용하는 캐시 메모리의 크기를 조정하여 성능을 향상시킬 수도 있습니다(사용 가능한 RAM이 많으면 더 많이 사용할 수도 있습니다):



```
BITCOIND_DB_CACHE=2048
```



변경 사항을 저장하고 편집기를 닫으려면 :




- ctrl + X'를 누릅니다
- 유형 `y`
- 를 누른 다음 "*입력*"을 누릅니다



### 5.4. MySQL 구성



그런 다음 MySQL 데이터베이스 구성을 엽니다:



```bash
nano docker-mysql.conf.tpl
```



로그인 정보를 입력하세요:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***'your-ID-here'와 'your-password-here'를 자신의 로그인 정보(강력하고 고유한 비밀번호 사용)로 바꾸세요



같은 방법으로 저장합니다(`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. 풀크럼 인덱서 구성



다음 파일을 엽니다:



```bash
nano docker-indexer.conf.tpl
```



매개 변수를 추가하여 Fulcrum을 활성화하고 Dojo 에 올바르게 통합하십시오:



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



다음으로, 구성에 따라 두 가지 가능성이 있습니다. Dojo가 일상적인 컴퓨터와 별도의 컴퓨터(전용 컴퓨터, 서버 등)에 설치되어 있는 경우, 예를 들어 로컬 네트워크에 해당 IP Address를 입력합니다:



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



컴퓨터의 로컬 IP Address를 찾으려면 다른 터미널을 열고 다음 명령을 입력하세요:



```bash
hostname -I
```



두 번째 가능성: Dojo를 일상적인 개인용 컴퓨터에서 직접 실행하는 경우, 구성 파일에 이미 있는 기본값을 그대로 유지하세요:



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



저장하고 편집기를 종료합니다(`Ctrl + X`, `y`, "*Enter*").



### 5.6. 노드 서비스 구성



마지막으로 기본 도장 서비스의 구성을 엽니다:



```bash
nano docker-node.conf.tpl
```



로그인 정보를 입력하세요:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***`귀하의 비밀번호-여기`를 자신의 자격 증명(강력하고 고유한 비밀번호 사용)으로 바꾸세요



![Image](assets/fr/26.webp)



그런 다음 로컬 인덱서를 활성화합니다:



```
NODE_ACTIVE_INDEXER=local_indexer
```



저장하고 편집기를 종료합니다(`Ctrl + X`, `y`, "*Enter*").



### 5.7. 로그인 관리



구성이 완료되면 생성된 모든 식별자를 저장할 필요는 없습니다. 반드시 저장해야 하는 유일한 식별자는 :



```
NODE_ADMIN_KEY
```



이 로그인을 통해 나중에 도장 관리 도구에 로그인할 수 있습니다. 다른 모든 로그인 정보는 비밀번호 관리자나 손글씨 메모에서 삭제할 수 있습니다. 나중에 다시 불러와야 할 경우 Dojo 구성 파일에서 계속 액세스할 수 있습니다.



## 6. 도장 설치



이 단계에서 Dojo가 머신에 설치되고 시작됩니다. 이 작업은 여러 서비스(Bitcoin core, Fulcrum 인덱서, Dojo 백엔드 등)를 시작하고 Blockchain Bitcoin의 전체 동기화를 시작합니다. 하드웨어와 인터넷 연결에 따라 며칠이 걸릴 수 있습니다.



### 6.1. Docker가 제대로 작동하는지 확인합니다



설치를 시작하기 전에 Docker가 작동 중인지 확인하세요. 다음 명령을 실행합니다:



```bash
docker run hello-world
```



이 명령은 작은 테스트 컨테이너를 다운로드하고 실행합니다. 모든 것이 올바르게 작동하면 다음과 유사한 메시지가 표시됩니다:



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



이 메시지가 표시되지 않으면 먼저 를 사용하여 컴퓨터를 재부팅하세요:



```bash
sudo reboot
```



그런 다음 **dojo** 계정에 다시 로그인하여 테스트 명령을 다시 실행하세요. 오류가 지속되면 Docker가 올바르게 설치되지 않은 것입니다. 이 경우 Docker 설치의 `2.4.` 단계로 돌아가서 각 명령을 주의 깊게 확인하세요.



### 6.2. 도장 설치 디렉토리로 이동합니다



설치에 필요한 스크립트는 `my-dojo` 폴더에 있습니다. 이 디렉토리로 이동합니다:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



L` 명령을 사용하여 `dojo.sh` 파일이 있는지 확인합니다. 이 파일은 Dojo의 설치와 모든 서비스 실행을 자동화하는 메인 스크립트입니다.



![Image](assets/fr/29.webp)



### 6.3. 설치 시작



를 실행하여 설치를 시작하십시오:



```bash
./dojo.sh install
```



Y`를 누른 다음 "*입력*"을 눌러 설치를 확인합니다.



![Image](assets/fr/30.webp)



이 스크립트는 :




- 필요한 Docker 컨테이너를 다운로드하여 실행합니다,
- gW-29를 초기화하고 Blockchain 동기화를 시작합니다,
- fulcrum 인덱서를 시작하여 트랜잭션과 주소를 추적합니다,
- dojo 백엔드 및 해당 API를 활성화합니다.



bitcoind`, `soroban`, `nodejs` 또는 `fulcrum`과 같은 다채로운 참조가 포함된 로그가 꾸준히 스크롤되는 것을 볼 수 있습니다. 이 스크롤은 Dojo가 실행 중이며 다양한 서비스를 실행하기 시작했음을 나타냅니다.



![Image](assets/fr/31.webp)



### 6.4. 종료 로그 표시



로그는 터미널에 실시간으로 표시됩니다. Dojo가 백그라운드에서 실행 중일 때 명령 프롬프트로 돌아가려면 을 입력합니다:



```
Ctrl + C
```



로그 표시를 중지해도 서비스가 중지되지 않으니 걱정하지 마세요. Docker는 백그라운드에서 Dojo를 계속 실행합니다(IBD를 계속 사용하려면 컴퓨터를 중지할 필요가 없습니다).



### 6.5. 초기 블록 다운로드*(IBD) 이해



시작 시 Bitcoin core는 2009년 이후 Blockchain 전체를 다운로드하고 확인해야 합니다. 이 단계를 ***초기 블록 다운로드*(IBD)**라고 합니다. 이 단계는 도장 노드가 각 Bitcoin 블록과 트랜잭션을 독립적으로 검증할 수 있도록 하기 때문에 필수적입니다.



이 동기화 기간은 여러 요인에 따라 달라집니다:




- 프로세서의 성능과 사용 가능한 RAM 메모리 용량에 따라 달라집니다,
- 디스크의 속도입니다,
- 노드가 연결하는 피어의 수와 품질입니다,
- 인터넷 연결 속도입니다.



실제로 이 작업은 일반적으로 **2~7일**이 소요됩니다. 이 기간 동안 기기를 계속 켜두셔도 됩니다. 기기를 오래 켜둘수록 동기화가 더 빨리 완료됩니다. Bitcoin core 로그를 참조하거나 Dojo 유지보수 도구를 설치한 후 정기적으로 동기화 상태를 확인하는 것이 좋습니다(다음 섹션 참조).



IBD에 대한 지식과 더 일반적으로 Bitcoin 노드의 운영 및 역할에 대해 더 깊이 알고 싶다면 이 과정을 살펴보는 것이 좋습니다:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. 동기화 모니터링



Dojo를 처음 설치할 때는 두 가지 주요 작업이 완전히 완료될 때까지 기다려야 합니다: Blockchain Bitcoin(*IBD*)의 완전한 다운로드와 이 Blockchain을 Fulcrum에서 인덱싱하는 작업입니다. 연결 및 컴퓨터 전원에 따라 며칠이 걸릴 수 있습니다. 이 기간 동안 프로세스 진행 상황을 모니터링하여 모든 것이 원활하게 실행되고 있는지 확인할 수 있습니다.



동기화 상태를 모니터링하는 방법에는 두 가지가 있습니다:




- 도장 유지 관리 도구(또는 DMT)를 사용하는데, 이는 간단하지만 IBD 중에 세부 정보를 거의 제공하지 않습니다;
- 기계에서 도장 로그를 직접 참조하여 더 기술적이면서도 훨씬 더 정확합니다.



### 7.1. 도장 유지 관리 도구(DMT)를 통해 확인하세요



도장 유지 관리 도구는 안전한 웹 기반 Interface로, 플랜트의 상태를 모니터링하고 특정 작업을 수행할 수 있습니다. IBD의 진행 상황을 모니터링하는 가장 쉽고 가장 접근하기 쉬운 방법입니다. 초기 동기화 단계에서는 표시되는 정보가 제한될 수 있습니다. 예를 들어, DMT에는 Fulcrum 인덱싱의 자세한 진행 상황이 표시되지 않습니다. 반면에 동기화가 완료되면 DMT에 :




- gW-40의 모든 조명;
- 각 서비스(노드, 인덱서, 도장 DB)에 대해 마지막으로 검증된 블록입니다.



액세스하려면 DMT의 URL을 알고 [토르 브라우저를 통해](https://www.torproject.org/download/) 연결해야 합니다. 이렇게 하려면 터미널을 열고 `/my-dojo` 디렉토리로 이동합니다:



```bash
cd ~/dojo-app/docker/my-dojo
```



그런 다음 다음 명령을 실행합니다:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



그러면 Tor를 통해 도장 연결과 관련된 모든 정보에 액세스할 수 있습니다. 여기서 우리가 관심 있는 것은 다음 URL입니다:



```
Dojo API and Maintenance Tool =
```



네트워크의 모든 기기에서 (원격으로라도) DMT에 액세스하려면, 토르 브라우저를 열고 이 URL 뒤에 `/admin`을 입력하세요. 예를 들어, URL이 `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`인 경우, [Tor 브라우저](https://www.torproject.org/download/) 바에 입력해야 합니다:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **이 Address을 엄격하게 기밀로 유지하십시오



그러면 인증 페이지로 리디렉션됩니다. 앞서 생성한 `NODE_ADMIN_KEY` 비밀번호를 사용하여 DMT에 로그인합니다.



![Image](assets/fr/33.webp)



로그인하면 *도장 관리 도구*에 접속할 수 있습니다! IBD 중 "*Full node*" 메뉴에서 "*최신 블록*" 정보를 확인할 수 있으며, 이를 통해 Bitcoin 노드의 현재 상태를 알 수 있습니다.



![Image](assets/fr/34.webp)



나중에 쉽게 검색할 수 있도록 토르 브라우저에 이 Address를 북마크에 추가하세요.



도장이 완전히 동기화되면 DMT 홈 페이지의 모든 표시기에 Green 체크 ✅가 표시되어야 합니다.



### 7.2. 도장 로그를 통한 인증



IBD의 진행 상황을 추적하는 두 번째 방법은 머신 로그를 직접 참조하는 것입니다. 이 접근 방식은 훨씬 더 정확한 실시간 모니터링을 제공합니다. Bitcoin core의 블록 다운로드 진행 상황과 Fulcrum이 블록을 색인하는 방법을 확인할 수 있습니다.



도장을 호스팅하는 컴퓨터에 연결하고 터미널을 엽니다. 모든 명령은 `my-dojo` 디렉토리에서 실행해야 합니다. 이 폴더에 자신을 위치시킵니다:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core 로그



Bitcoin core 로그를 확인하여 IBD 진행 상황을 추적하세요:



```bash
./dojo.sh logs bitcoind
```



처음에는 블록 헤더의 사전 동기화 단계가 표시됩니다:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



이 수치가 100%에 도달하면 Bitcoin core가 Blockchain의 전체 다운로드를 시작합니다. IBD 진행 상황을 확인할 수 있습니다. 현재 블록 높이를 확인하려면 `height=`로 표시된 값을 확인합니다. IBD 진행률의 백분율을 나타내는 `progress=` 키를 따라갈 수도 있습니다.



![Image](assets/fr/36.webp)



항상 그렇듯이 로그를 닫고 명령 프롬프트로 돌아가려면 `Ctrl + C` 조합을 사용하세요.



#### 지렛대 로그



Bitcoin core이 헤더 사전 동기화를 완료하면 Fulcrum은 Blockchain의 인덱싱을 시작합니다. 로 로그를 확인합니다:



```bash
./dojo.sh logs fulcrum
```



그러면 `높이:` 뒤에 표시된 인덱싱된 마지막 블록의 높이와 인덱싱 진행률도 확인할 수 있습니다.



![Image](assets/fr/37.webp)



### 7.3. 지렛대 데이터베이스 손상



Fulcrum은 특히 강력한 인덱서이지만, 섬세한 데이터베이스 관리로 인해 설치가 복잡할 수 있습니다. 초기 동기화 중에 전원이 차단되거나 갑자기 컴퓨터가 종료되는 경우, 인덱서의 데이터베이스가 손상될 수 있습니다. 예를 들어 다음 로그에서 이를 확인할 수 있습니다:



```bash
fulcrum | The database has been corrupted etc...
```



**참고:** 이 유형의 오류는 곧 출시될 Fulcrum 2.0에서 수정될 예정입니다.



이런 일이 발생하더라도 bitcoind(Bitcoin 노드)에는 아무런 영향이 없습니다. 해당 노드의 IBD는 Fulcrum과 독립적으로 계속 진행됩니다. 그러나 손상된 데이터를 삭제하고 동기화를 처음부터 다시 시작할 때까지 Fulcrum을 사용할 수 없습니다. 작동 방식은 다음과 같습니다:



도장 중지:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Fulcrum 컨테이너와 볼륨만 삭제합니다:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



일반적으로 이름은 `my-dojo_data-fulcrum`이며, 그렇지 않은 경우 이전 명령에서 반환된 이름을 변경합니다.



그런 다음 Dojo를 다시 시작하고 Fulcrum을 처음부터 다시 빌드하세요:



```bash
./dojo.sh upgrade
```



그런 다음 로그를 참조하여 Fulcrum이 제대로 작동하는지 확인할 수 있습니다:



```bash
docker logs -f fulcrum
```




## 8. 도장 유지 관리 도구 사용



Proof of Work가 가장 많은 워프 헤드에 Bitcoin 매듭이 동기화되고 Blockchain이 Fulcrum에 100% 인덱싱되면 도장 사용을 시작할 수 있습니다.



도장은 새 버전이 나올 때마다 정기적으로 개선되는 다양한 기능을 제공합니다. 제 생각에 가장 중요한 두 가지 기능은 다음과 같습니다:




- 아시가루 Wallet를 연결하여 자체 노드를 사용하여 Blockchain 데이터를 참조하고 트랜잭션을 브로드캐스트할 수 있습니다,
- 그리고 제어하지 않는 외부 인스턴스에 데이터를 노출하지 않고도 Blockchain Bitcoin에 대한 정보에 액세스할 수 있는 Block explorer을 제공합니다.



사용 방법을 알아보세요.


### 8.1. 아시가루와 도장 연결



아시가루 Wallet을 도장에 연결하는 방법은 매우 간단합니다. DMT에서 "*페어링*" 메뉴를 열면 됩니다. 아시가루 애플리케이션으로 직접 스캔할 수 있는 QR코드가 나타납니다.



![Image](assets/fr/38.webp)



아시가루 애플리케이션에서 Wallet를 생성하거나 복원한 후 처음 실행하면 "*도장 서버 구성*" 페이지로 리디렉션됩니다. "*스캔 QR*"을 누른 다음 DMT에 표시된 QR 코드를 스캔합니다.



![Image](assets/fr/39.webp)



그런 다음 "*계속*" 버튼을 클릭합니다.



![Image](assets/fr/40.webp)



이제 도장에 연결되었습니다.



![Image](assets/fr/41.webp)



### 8.2. Block explorer 사용



도장은 Block explorer, [BTC-RPC 익스플로러](https://github.com/janoside/btc-RPC-explorer)를 자동으로 설치하여 자체 Bitcoin 노드에서 데이터를 직접 가져옵니다. 익스플로러를 사용하면 이해하기 쉬운 Interface 웹을 통해 Blockchain 및 Mempool의 원시 정보에 액세스할 수 있습니다. 예를 들어 보류 중인 트랜잭션의 상태를 확인하거나, Address의 잔액을 확인하거나, 블록의 구성을 쉽게 살펴볼 수 있습니다.



액세스하려면 브라우저에서 Tor Address을 검색하기만 하면 됩니다. 이렇게 하려면 DMT의 Address을 가져올 때 사용한 것과 동일한 명령을 실행하세요:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



토르를 통해 모든 도장 연결 정보에 액세스할 수 있습니다. 여기서 우리가 관심 있는 것은 다음 URL입니다:



```
Block Explorer =
```



이미 DMT에 연결되어 있는 경우 연결 JSON 내의 '*페어링*' 메뉴에서 이 Address를 찾을 수도 있습니다:



![Image](assets/fr/43.webp)



네트워크의 모든 컴퓨터에서 (원격으로도) 브라우저에 액세스하려면, [Tor 브라우저](https://www.torproject.org/download/)를 열고 방금 검색한 URL을 입력하세요.



⚠️ **이 Address는 엄격하게 기밀로 유지하십시오



그러면 자신의 Block explorer에 액세스할 수 있습니다.



![Image](assets/fr/44.webp)



*이미지 출처: https://ashigaru.rs/.*



거래를 추적하려면 오른쪽 상단의 검색창에 txid을 입력하기만 하면 됩니다.



![Image](assets/fr/45.webp)



*이미지 출처: https://ashigaru.rs/.*



Address과 관련된 동작을 확인하려면 검색창에 Address을 입력하여 같은 방법으로 진행하세요.



![Image](assets/fr/46.webp)



*이미지 출처: https://ashigaru.rs/.*



검색창에 블록의 Hash 또는 높이를 입력하여 세부 정보를 표시할 수도 있습니다.



![Image](assets/fr/47.webp)



*이미지 출처: https://ashigaru.rs/.*



## 9. 도장 유지 관리



### 9.1 도장 중지



특정 데이터베이스, 특히 Fulcrum 인덱서가 손상될 수 있으므로 Dojo의 전원을 갑자기 차단하지 마세요. 전원을 꺼야 하는 경우에는 항상 Dojo를 완전히 종료한 다음 모든 절차가 완료되면 컴퓨터도 꺼야 합니다:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 도장 업데이트



도장은 버그 수정, 안정성 개선, 기능 추가를 위해 정기적으로 업데이트되고 새 버전이 출시됩니다. 따라서 [정기적으로 업데이트를 확인하고](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) 도장을 업데이트하는 것이 중요합니다. 이 과정은 초기 설치와 비슷하지만, 구성을 유지하면서 특정 파일을 사용 가능한 최신 버전으로 교체해야 합니다. 다음은 깨끗하고 안전한 업데이트를 위해 따라야 할 자세한 단계입니다:



현재 도장의 버전을 확인하려면 다음 명령을 실행하세요:



```bash
./dojo.sh version
```



이 단계는 선택 사항이지만, OS를 업데이트하는 것부터 시작하는 것이 좋습니다. 이렇게 하면 비호환성 위험이 줄어들고 Dojo에서 사용하는 종속성을 최신 상태로 유지할 수 있습니다:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Dojo 디렉토리로 이동하여 현재 서비스를 중지합니다:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



그런 다음 시스템을 재부팅하여 새로 시작하세요:



```bash
sudo reboot
```



Dojo는 디지털 서명된 파일과 함께 제공됩니다. 이러한 PGP 서명은 파일이 개발자로부터 왔으며 어떤 방식으로도 변경되지 않았음을 보장합니다. Dojo를 처음 설치할 때와 마찬가지로 업데이트할 때마다 이를 확인하는 것이 중요합니다. 먼저 Tor를 통해 개발자의 공개 키를 다운로드한 다음, 이를 가져옵니다:



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



개인 디렉토리로 돌아갑니다:



```bash
cd ~/
```



Tor를 통해 GitHub에서 최신 버전의 Dojo를 다운로드하세요. 이 예에서는 `1.28.0` 버전입니다(이 글을 쓰는 시점에는 아직 존재하지 않습니다. 이는 단지 예를 보여주기 위한 것입니다). 파일과 링크를 [설치하려는 버전으로] 교체하는 것을 잊지 마세요(https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



또한 PGP 지문과 서명이 포함된 파일을 다운로드합니다(다시 한 번 명령에서 버전을 조정하는 것을 잊지 마세요):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



다운로드한 지문 파일이 개발자 키로 서명되었는지 확인합니다:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



올바른 결과가 표시되어야 합니다:



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



키가 인증되지 않았다는 경고가 표시될 수 있지만 이는 중요하지 않습니다. 반면 서명이 유효하지 않거나 다른 키에 해당하는 경우 더 이상 진행하지 말고 링크를 확인하면서 다시 시작하세요.



그런 다음 아카이브의 SHA256 지문을 계산하고 공식 지문 파일과 비교합니다 :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



두 지문이 완벽하게 일치하면 아카이브가 정품이며 손상되지 않은 것입니다. 다르면 즉시 파일을 삭제하고 계속 진행하지 마세요.



홈 디렉토리에 있는 아카이브의 압축을 풉니다:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



그런 다음 내용을 Dojo 디렉터리에 복사하여 이전 :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



이 작업은 `~/dojo-app/docker/my-dojo/conf`에 있는 구성 파일을 그대로 유지하지만 다른 모든 파일을 업데이트된 버전으로 바꿉니다.



환경을 깨끗하게 유지하려면 불필요한 파일을 삭제하세요 :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Dojo 스크립트 디렉토리로 돌아가서 업데이트 명령을 실행합니다:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



이 명령은 새 파일로 이미지를 다시 빌드한 다음 모든 서비스를 자동으로 다시 시작하도록 Docker에 지시합니다. 프로세스가 끝나면 로그를 확인하여 Bitcoin core, Fulcrum 및 Dojo가 모두 올바르게 작동하는지 확인합니다:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



서비스가 오류 없이 시작되고 로그에 처리 중인 블록이 표시되면 도장이 최신 상태로 운영되고 있는 것입니다.