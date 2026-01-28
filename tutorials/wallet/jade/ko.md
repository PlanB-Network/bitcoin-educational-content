---
name: Jade

description: JADE 디바이스 설정 방법
---

![image](assets/cover.webp)


## 튜토리얼 비디오


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

블록스트림 제이드 - 모바일 Bitcoin Hardware Wallet 전체 튜토리얼 작성자: BTCsession


## 전체 글쓰기 가이드


![image](assets/cover2.webp)


### 사전 요구 사항


1. 최신 버전의 Blockstream Green를 다운로드하세요.


2. 이 드라이버를 설치하여 컴퓨터에서 Jade를 인식할 수 있도록 하세요.


### 데스크톱 설정


![full guide](https://youtu.be/0fPVzsyL360)


Blockstream Green을 연 다음 장치 아래에서 블록스트림 로고를 클릭합니다.


![image](assets/1.webp)


제공된 USB 케이블을 사용하여 Jade를 데스크톱에 연결합니다.


**참고: 컴퓨터에서 Jade가 인식되지 않는다면 필요한 드라이버가 설치되어 있는지 확인하고 USB 권한 문제로 인한 문제인지 확인하세요.


Green에 Jade가 나타나면 업데이트 확인을 클릭하고 최신 펌웨어 버전을 선택하여 Jade를 업데이트합니다. 스크롤 휠을 사용하거나 Jade를 토글하여 업데이트를 확인하고 계속 진행합니다. Jade에 여전히 '초기화' 버튼이 표시되는지 확인하세요. 그렇지 않으면 Jade를 설정한 후 업그레이드할 때까지 기다려야 합니다. 필요한 경우 뒤로 버튼을 사용하여 이 화면으로 이동합니다.


![image](assets/2.webp)


Jade의 펌웨어를 업데이트한 후 사용하려는 네트워크 및 보안 정책에서 Jade 설정을 선택합니다.


**팁: 보안 정책은 아래 로그인 화면의 유형 아래에 나와 있습니다. 싱글시그와 Multisig 쉴드 중 어떤 것을 선택할지 잘 모르겠다면 [여기](https://help.blockstream.com/hc/en-us/articles/4403642609433) 가이드를 참조하세요


![image](assets/3.webp)


그런 다음, 새 Wallet을 생성하도록 선택하고 복구 문구를 12단어로 generate으로 선택합니다. 고급을 클릭하면 12단어 및 24단어 복구 문구 옵션이 제공됩니다.


![image](assets/4.webp)


복구 문구를 종이에 오프라인으로 기록하거나 보안을 강화하기 위해 전용 복구 문구 백업 장치를 사용하세요. 그런 다음, Jade 상단의 휠 또는 토글을 사용하여 복구 문구를 확인합니다. 이 단계를 통해 복구 문구를 정확하게 적었는지 확인할 수 있습니다.


![image](assets/5.webp)


6자리 PIN을 설정하고 확인합니다. 이 비밀번호는 Wallet에 로그인할 때마다 블록스트림 제이드의 잠금을 해제하는 데 사용됩니다.


![image](assets/6.webp)


이제 Green 데스크톱 앱에서 Wallet로 이동을 선택하기만 하면 Wallet이 Blockstream Green에서 열리는 것을 볼 수 있습니다. 블록스트림 제이드도 준비되었음을 표시합니다! 이제 Jade를 사용해 Bitcoin 트랜잭션을 주고받을 수 있습니다.


![image](assets/7.webp)


Wallet 사용을 마친 후에는 기기에서 블록스트림 제이드의 연결을 해제하세요. 다음에 블록스트림 제이드에서 Wallet을 사용하려면 기기를 다시 연결하고 지시를 따르기만 하면 됩니다.


출처: https://help.blockstream.com/hc/en-us/articles/17478506300825


### 부록 A - Green Wallet 다운로드 파일 확인


다운로드 확인은 다운로드한 파일이 개발자가 배포한 이후 수정되지 않았는지 확인하는 것을 의미합니다.


다운로드한 파일과 개발자의 공개 키와 함께 서명(개발자의 개인 키로 생성)이 gpg -verify 함수를 통과할 때 TRUE 결과를 반환하는지 확인하여 이를 수행합니다. 다음에서 그 방법을 보여드리겠습니다.


먼저 서명 키를 받습니다:


Linux의 경우 터미널을 열고 다음 명령을 실행합니다(텍스트를 복사하여 붙여넣고 따옴표를 포함해야 합니다):


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


Mac의 경우에도 동일한 작업을 수행하지만 먼저 GPG Suite를 다운로드하여 설치해야 한다는 점이 다릅니다.


Windows의 경우, 동일한 작업을 수행하지만 먼저 GPG4Win을 다운로드하여 설치해야 한다는 점이 다릅니다.


공개 키를 가져왔다는 메시지가 표시됩니다.


![image](assets/9.webp)


이 이미지에는 빈 alt 속성이 있으며, 파일 이름은 image-3-1024x162.webp입니다


다음으로 소프트웨어의 Hash이 포함된 파일을 가져와야 합니다. 이 파일은 블록스트림의 GitHub 페이지에 저장되어 있습니다. 먼저 여기 정보 페이지로 이동하여 "데스크톱" 링크를 클릭합니다. GitHub의 최신 릴리스 페이지로 이동하면 SHA256SUMS.asc 파일에 대한 링크가 표시되며, 이 파일은 우리가 다운로드한 프로그램의 블록스트림 게시 Hash이 포함된 텍스트 문서입니다.


![image](assets/10.webp)


GitHub:


![image](assets/11.webp)


그럴 필요는 없지만, 디스크에 저장한 후 텍스트 편집기를 사용하여 Mac에서 파일을 더 쉽게 열 수 있도록 "SHA256SUMS.asc"의 이름을 "SHA256.txt"로 변경했습니다. 이것이 파일의 내용입니다:


![image](assets/12.webp)


우리가 찾고 있는 텍스트는 맨 위에 있습니다. 다운로드한 파일에 따라 나중에 비교하게 될 해당 Hash 출력물이 있습니다.


문서 하단에는 위의 메시지에 서명한 서명이 포함되어 있으며, 두 개의 파일이 하나로 합쳐져 있습니다.


순서는 중요하지 않지만, Hash을 확인하기 전에 Hash 메시지가 진짜인지(즉, 변조되지 않았는지) 확인하겠습니다.


터미널을 엽니다. SHA256SUMS.asc 파일을 다운로드한 올바른 디렉터리에 있어야 합니다. Linux 및 Mac의 경우 '다운로드' 디렉터리에 다운로드했다고 가정하고 다음과 같은 디렉터리로 변경합니다(대소문자 구분):


```bash
cd Downloads
```


물론 이 명령어 뒤에 <입력>을 눌러야 합니다. Windows의 경우 CMD(명령 프롬프트)를 열고 같은 내용을 입력합니다(대소문자는 구분하지 않음).


Windows와 Mac의 경우 앞서 안내한 대로 각각 GPG4Win과 GPG Suite를 이미 다운로드해야 합니다. Linux의 경우 GPG는 운영 체제와 함께 제공됩니다. 터미널(또는 Windows의 경우 CMD)에서 다음 명령을 입력합니다:


```bash
gpg --verify SHA256SUMS.asc
```


파일 이름의 정확한 철자(빨간색)는 파일을 가져온 날에 따라 다를 수 있으므로 명령이 다운로드한 파일 이름과 일치하는지 확인하세요. 이 출력이 표시되면 신뢰할 수 있는 서명에 대한 경고는 무시하세요. 이는 앞서 가져온 공개 키를 컴퓨터에 수동으로 신뢰한다고 말하지 않았다는 의미일 뿐입니다.


![image](assets/13.webp)


이 이미지에는 빈 alt 속성이 있으며 파일 이름은 image-4-1024x165.webp입니다


이 출력은 서명이 정상임을 확인하며, "info@greenaddress.it"의 개인 키가 데이터(Hash 보고서)에 서명했음을 확신합니다.


이제 다운로드한 zip 파일을 Hash으로 압축하고 게시된 결과와 비교해야 합니다. SHA256SUMS.asc 파일에 "Hash"이라는 텍스트가 약간 있습니다: SHA512"라는 텍스트가 있어 혼란스럽지만, 파일 내부에는 분명히 SHA256 출력이 있으므로 무시하기로 하겠습니다.


Mac과 Linux의 경우 터미널을 열고 zip 파일을 다운로드한 위치로 이동합니다(터미널을 닫지 않았다면 "cd 다운로드"를 다시 입력해야 할 것입니다). 참고로 PWD("인쇄 작업 디렉터리")를 입력하면 현재 어떤 디렉터리에 있는지 확인할 수 있으며, 이 모든 것이 낯설다면 "Linux/Mac/Windows 파일 시스템 탐색 방법"을 검색하여 YouTube 동영상을 시청하는 것이 유용합니다.


파일을 받으려면 다음과 같이 입력합니다:


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


파일 이름이 정확히 무엇인지 확인하고 필요한 경우 위의 파란색 텍스트를 수정해야 합니다.


다음과 같은 출력이 표시됩니다(파일이 제 파일과 다른 경우 귀하의 파일은 다를 수 있습니다):


![image](assets/14.webp)


다음으로, Hash 출력과 SHA256SUMS.asc 파일에 있는 내용을 시각적으로 비교합니다. 일치하면 -> 성공입니다! 축하합니다.


출처: https://armantheparman.com/jade/


### Sparrow에서 사용


Sparrow 사용법을 이미 알고 계신다면 언제나처럼 사용하시면 됩니다:


**참고: 예를 들어 Specter와 동일한 프로세스입니다


여기에 제공된 링크를 사용하여 Sparrow를 다운로드하세요.


![image](assets/14.5.webp)


다음을 클릭하여 설정 가이드를 따라 다양한 연결 옵션에 대해 알아보세요.


![image](assets/15.webp)


원하는 서버를 선택한 다음 새 Wallet 만들기를 선택합니다.


![image](assets/16.webp)


Wallet의 이름을 입력하고 Wallet 생성을 클릭합니다.


![image](assets/17.webp)


원하는 정책 및 스크립트 유형을 선택한 다음 연결된 Hardware Wallet을 선택합니다.


**참고: ** 이전에 블록스트림 제이드 Wallet을 싱글사인 Blockstream Green과 함께 사용한 적이 있고 Sparrow에서 거래를 확인하려면 스크립트 유형이 Green의 자금이 포함된 계좌 유형과 일치하는지 확인해야 합니다. 또한 파생 경로도 일치해야 합니다.


![image](assets/18.webp)


블록스트림 제이드에 연결하고 스캔을 클릭합니다. 그러면 Jade에 비밀번호를 입력하라는 메시지가 표시됩니다.


**팁:** Jade를 연결하기 전에 Blockstream Green 앱이 열려 있지 않은지 확인하세요. Green가 열려 있으면 Sparrow 내에서 Jade가 감지되는 문제가 발생할 수 있습니다.


![image](assets/19.webp)


키 저장소 가져오기를 선택하여 기본 계정의 공개 키를 가져오거나 화살표를 선택하여 사용하려는 파생 경로를 수동으로 선택합니다.


![image](assets/20.webp)


원하는 키를 가져온 후 적용을 클릭합니다.


![image](assets/21.webp)


이제 Wallet을 성공적으로 설정했으며 Sparrow과 블록스트림 제드를 사용하여 Bitcoin의 수신, 저장 및 사용을 시작할 수 있습니다.


**참고: ** 이전에 Blockstream Green을 Multisig 쉴드 Wallet로 사용했던 경우, 새로운 Sparrow wallet에 동일한 잔액이 표시될 것으로 기대하지 마세요. 다른 지갑이기 때문입니다. Multisig Shield Wallet에 다시 액세스하려면 Jade를 Blockstream Green에 다시 연결하기만 하면 됩니다.


![image](assets/22.webp)


출처: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Green 앱


모바일 가이드에 더 관심이 있다면 Blockstream Green와 함께 사용할 수 있습니다



- Green로 블록스트림 제이드 설정 방법 | 블록스트림 제이드 - https://youtu.be/7aacxnc6DHg
- Bitcoin을 Jade Wallet로 받는 방법 | 블록스트림 제이드 - https://youtu.be/CVtcDdiPqLA