---
name: 아시가루 터미널
description: 데스크톱에서 아시가루를 사용하여 코인조인 만들기
---

![cover](assets/cover.webp)



아시가루 터미널은 아시가루 팀이 Sparrow 서버를 개조한 것으로, Whirlpool 코인조인 프로토콜을 구현합니다. 이 소프트웨어는 사무라이 Wallet에서 시작된 작업의 연장선상에 있으며, 특히 자체 관리와 기밀성 보존이라는 기본 원칙을 채택한 Whirlpool GUI를 기반으로 합니다.



이 소프트웨어는 원래 사무라이 팀이 개발한 제로링크 코인조인 프로토콜인 Whirlpool 생태계와의 완전한 통합을 위해 수정 및 최적화한 Sparrow 서버의 fork입니다.



아시가루 터미널은 미니멀한 TUI 인터페이스에서 작동하며 개인용 컴퓨터 또는 전용 서버에 배포할 수 있습니다. Whirlpool와 직접 상호 작용하여 "*Tx0*"를 시작하고, "*예치금*", "*프리믹스*", "*포스트믹스*" 및 "*배드뱅크*" 계정을 관리하고, 자동 리믹스를 수행하여 부품의 기밀성을 강화할 수 있습니다.



요컨대, 아시가루 터미널은 Whirlpool을 사용해 코인조인을 생성하고자 할 때 특히 유용합니다.



이 첫 번째 튜토리얼에서는 아시가루 터미널의 설치와 작동 방법을 안내해드리겠습니다. 두 번째 고급 튜토리얼에서는 실제 코인조인 생성에 대해 다룰 예정입니다.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. 아시가루 터미널 설치



아시가루 터미널을 설치하려면 토르 네트워크를 통해서만 바이너리가 배포되기 때문에 토르 브라우저가 필요합니다. 아직 설치하지 않았다면 [컴퓨터에 설치](https://www.torproject.org/download/)하세요.



### 1.1. 아시가루 터미널 다운로드



토르 브라우저에서 [Git 저장소의 릴리즈 페이지](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/)로 이동해 운영 체제에 맞는 최신 버전의 아시가루 터미널을 다운로드하세요.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



운영 체제에 맞는 다음 두 개의 파일을 다운로드하세요:




- 바이너리(디비안/우분투의 경우 `ashigaru_terminal_v1.0.0_amd64.deb`, 맥OS의 경우 `.dmg` 또는 윈도우의 경우 `.zip`) ;
- 서명된 해시 파일: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. 아시가루 터미널 확인



장치에서 소프트웨어를 실행하기 전에 소프트웨어의 진위 여부와 무결성을 확인해야 합니다. 이는 비트코인을 손상시키거나 기기를 감염시킬 수 있는 사기 버전을 설치하는 것을 방지하기 때문에 중요한 단계입니다.



새 브라우저 탭을 열고 [키베이스 확인 도구](https://keybase.io/verify)로 이동합니다. 방금 다운로드한 '.txt' 파일의 내용을 제공된 필드에 붙여넣은 다음 '확인' 버튼을 클릭합니다.



![Image](assets/fr/02.webp)



확인 출처를 다양화하기 위해 clearnet [ashigaru.rs](https://ashigaru.rs/download/) 사이트의 `/download` 섹션에 있는 메시지와 비교할 수도 있습니다.



![Image](assets/fr/03.webp)



서명이 유효하면 Keybase는 Ashigaru의 개발자가 파일에 서명했음을 확인하는 메시지를 표시합니다.



![Image](assets/fr/04.webp)



키베이스에 표시된 `ashigarudev` 프로필을 클릭하고 키 지문이 정확히 일치하는지 확인할 수도 있습니다: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



이 단계에서 오류가 나타나면 서명이 유효하지 않은 것입니다. 이 경우 **다운로드한 소프트웨어를 설치하지 마세요**. 처음부터 다시 시작하거나 커뮤니티에 도움을 요청한 후 계속 진행하세요.



Keybase에서 애플리케이션의 인증된 해시를 제공했습니다. 이제 다운로드한 `.deb`, `.zip` 또는 `.dmg` 파일의 해시가 Keybase에서 유효성을 검사한 것과 일치하는지 확인합니다. 이렇게 하려면 [해시 파일 온라인](https://hash-file.online/)으로 이동합니다.



찾아보기...` 버튼을 클릭하고 1.1단계에서 다운로드한 `.deb`, `.zip` 또는 `.dmg` 파일을 선택합니다. 그런 다음 `SHA-256` 해시 함수를 선택하고 `CALCULATE HASH`를 클릭하여 파일에 대한 해시를 generate로 설정합니다.



![Image](assets/fr/06.webp)



그러면 사이트에 소프트웨어 해시가 표시됩니다. Keybase.io에서 확인한 해시와 비교합니다. 두 가지가 완벽하게 일치하면 진위 및 무결성 확인이 성공한 것입니다. 이제 소프트웨어를 사용할 수 있습니다.



![Image](assets/fr/07.webp)



### 1.3 아시가루 터미널 출시





- 데비안 / 우분투



소프트웨어를 설치하려면 다음 명령을 실행합니다:



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



다운로드한 버전에 따라 주문을 수정합니다.



그런 다음 설치를 확인합니다:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



그런 다음 소프트웨어를 실행합니다:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



다운로드하여 확인한 `.zip` 파일을 마우스 오른쪽 버튼으로 클릭한 다음 `모두 추출...`을 선택하여 내용을 추출합니다.



추출이 완료되면 'Ashigaru-terminal.exe' 파일을 더블 클릭하여 소프트웨어를 실행합니다.



![Image](assets/fr/08.webp)



## 2. 아시가루 터미널 시작하기



아시가루 터미널은 터미널에서 직접 실행되는 미니멀한 인터페이스, 즉 TUI(*Text-based User Interface*) 프로그램입니다. 메뉴와 키보드 단축키를 사용하여 상호 작용하지만 실제 클래식 그래픽 환경은 없습니다.



![Image](assets/fr/09.webp)



키보드의 화살표 키를 사용하여 메뉴를 탐색하고 '입력' 키를 눌러 작업을 확인하거나 선택 사항을 확정하면 됩니다.



## 3. 노드를 아시가루 터미널에 연결하기



기본적으로 아시가루 터미널은 공용 Electrum 서버에 연결됩니다. 이는 기밀성 및 주권 측면에서 분명히 위험을 초래합니다. 따라서 자체 Electrum Server에 직접 연결하도록 구성하겠습니다.



이렇게 하려면 '환경설정 > 서버' 메뉴를 엽니다.



![Image](assets/fr/10.webp)



'<< 편집 >` 버튼을 클릭합니다.



![Image](assets/fr/11.webp)



비공개 Electrum Server`를 선택한 다음 `<계속>`을 클릭합니다.



![Image](assets/fr/12.webp)



서버의 URL과 포트를 입력합니다. .onion`으로 토르 주소를 지정할 수 있습니다. 그런 다음 `< 테스트 >`를 클릭해 연결을 확인합니다.



![Image](assets/fr/13.webp)



연결에 성공하면 서버의 세부 정보와 함께 '성공'이라는 메시지가 표시됩니다.



![Image](assets/fr/14.webp)



아직 Bitcoin 노드가 없는 경우 이 과정을 수강하는 것이 좋습니다:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*이 튜토리얼에서는 테스트넷에서 작업 중이므로 Electrs 서버에서 연결을 끊겠습니다. 그러나 작업은 mainnet에서 완전히 동일하게 유지됩니다



## 4. 아시가루 터미널에서 포트폴리오 만들기



이제 소프트웨어가 올바르게 구성되었으므로 Bitcoin 포트폴리오를 추가할 수 있습니다.



두 가지 옵션이 있습니다:




- wallet을 처음부터 새로 생성하여 아시가루 터미널에서만 사용할 수 있습니다. 이 경우 wallet과 상호 작용할 때마다 이 소프트웨어를 열어야 합니다;
- 또는 기존 아시가루 wallet을 휴대폰에서 아시가루 터미널로 직접 가져올 수도 있습니다. 이 방법의 단점은 wallet이 하나가 아닌 두 개의 위험한 환경에 노출되기 때문에 설정의 보안이 약간 떨어진다는 것입니다. 반면에 아시가루 터미널을 계속 실행하여 코인을 섞을 수 있고, 아시가루 모바일 앱을 통해 원격으로 코인을 사용할 수 있다는 장점이 있습니다.



이 튜토리얼에서는 두 번째 방법을 선택하겠습니다. 하지만 완전히 새로운 포트폴리오를 만들고 싶다면 새 니모닉 문구와 새 passphrase를 저장해야 하는 생성 과정만 다를 뿐 절차는 동일하게 유지됩니다.



또한 Ashigaru Terminal에서는 비트코인을 직접 사용할 수 없습니다. 동일한 지갑을 Ashigaru Terminal과 Ashigaru 앱(이 튜토리얼에서 제가 할 방법) 또는 Sparrow Wallet에서 동기화할 수 있습니다.



아시가루 애플리케이션에 아직 wallet이 없는 경우 전용 튜토리얼 을 참조하세요:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

지갑` 메뉴로 이동합니다.



![Image](assets/fr/15.webp)



그런 다음 `wallet 생성/복원...`을 선택합니다. Open Wallet...` 옵션을 사용하면 나중에 아시가루 터미널에 이미 저장된 포트폴리오에 액세스할 수 있습니다.



![Image](assets/fr/16.webp)



포트폴리오에 이름을 지정하세요.



![Image](assets/fr/17.webp)



그런 다음 포트폴리오 유형 'Hot Wallet'를 선택합니다.






![Image](assets/fr/18.webp)



이 단계에서는 초기 선택에 따라 절차가 달라집니다:




- 새 포트폴리오를 처음부터 새로 생성하려면 '<<새 Wallet 생성>>'을 클릭하고 passphrase BIP39를 정의한 다음 니모닉 문구와 passphrase을 물리적 매체에 조심스럽게 저장합니다;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- 아시가루 애플리케이션과 동일한 wallet을 사용하려면 니모닉 문구 12단어와 passphrase BIP39를 해당 필드에 직접 입력하세요. 숫자나 추가 문자 없이 소문자, 전체, 순서대로 공백으로 구분하여 단어를 입력하세요.



이 단계가 완료되면 `< 다음 >`을 클릭합니다.



*참고*: 이 버튼을 클릭할 수 없다면 니모닉 문구가 잘못된 것입니다. 단어가 틀렸거나 철자가 틀린 것이 없는지 주의 깊게 확인하세요.



![Image](assets/fr/19.webp)



그런 다음 비밀번호를 설정해야 합니다. 이 비밀번호는 아시가루 터미널 wallet의 잠금을 해제하고 무단 물리적 접근으로부터 보호하는 데 사용됩니다. 즉, 이 비밀번호가 없어도 니모닉 문구와 passphrase을 가진 사람은 누구나 wallet를 복원하고 비트코인에 액세스할 수 있습니다.



길고 복잡한 임의의 비밀번호를 선택하세요. 사본을 안전한 곳에 보관하세요. 물리적 매체나 안전한 비밀번호 관리자에 보관하는 것이 가장 좋습니다.



완료되면 `< 확인 >`을 클릭합니다.



![Image](assets/fr/20.webp)



## 5. 포트폴리오 사용



그런 다음 액세스할 계정을 선택할 수 있습니다. 지금은 믹스를 시작하지 않았으므로 '입금' 계정에 액세스하겠습니다.



![Image](assets/fr/21.webp)



아시가루 터미널은 Sparrow 서버의 fork이므로 작동 방식은 Sparrow과 동일합니다. 동일한 메뉴를 찾을 수 있습니다:



![Image](assets/fr/22.webp)





- 거래": 이 계정에 연결된 거래 내역을 확인할 수 있습니다. 제 경우에는 동일한 wallet에서 아시가루 애플리케이션으로 일부를 만들었기 때문에 이미 일부가 표시되어 있습니다.



![Image](assets/fr/23.webp)





- 받기`: 입금 계좌에 새 공란 영수증 주소를 생성합니다.



![Image](assets/fr/24.webp)





- 주소`: 계정의 내부 또는 외부 체인에 속한 모든 주소의 목록을 표시합니다.



![Image](assets/fr/25.webp)





- `UTXO`: 사용 가능한 모든 UTXO를 나열합니다.



![Image](assets/fr/26.webp)





- 설정`: 포트폴리오 *설명자*에 액세스할 수 있습니다. seed을 참조하거나 *갭 제한*을 조정하거나 포트폴리오의 생성 날짜를 변경할 수도 있습니다.



![Image](assets/fr/27.webp)



이제 Ashigaru Terminal을 설치하고 사용하는 방법을 알게 되었습니다. 다음 튜토리얼에서는 이 소프트웨어로 coinjoin을 수행하고 "*Postmix*"에서 자금을 관리하는 방법을 알아보겠습니다.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
