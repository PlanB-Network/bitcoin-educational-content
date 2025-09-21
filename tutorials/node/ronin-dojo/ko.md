---
name: RoninDojo

description: 로닌도조 Bitcoin 노드 설치 및 사용.
---
***경고: 4월 24일 사무라이 Wallet의 설립자가 체포되고 서버가 압수된 이후, Whirlpool과 같은 로닌도조의 특정 기능은 더 이상 운영되지 않습니다. 그러나 이러한 도구는 향후 몇 주 내에 복원되거나 다른 방식으로 다시 출시될 수 있습니다. 또한, 로닌도조 코드는 압수된 사무라이의 깃랩에서 호스팅되었기 때문에 현재 원격으로 코드를 다운로드할 수 없습니다. 로닌도조 팀은 코드를 다시 게시하기 위해 노력 중입니다*


저희는 이 사건의 전개 상황과 관련 도구의 개발 상황을 면밀히 주시하고 있습니다. 새로운 정보가 입수되는 대로 이 튜토리얼을 업데이트할 예정이니 안심하세요


이 튜토리얼은 교육 및 정보 제공 목적으로만 제공됩니다. 범죄 목적으로 이러한 도구를 사용하는 것을 보증하거나 권장하지 않습니다. 해당 관할 지역의 법률을 준수하는 것은 각 사용자의 책임입니다


이 튜토리얼은 로닌도조 v1 설치에 관한 것입니다. 최신 개선 사항과 기능을 활용하려면 라즈베리파이에 로닌도조 v2를 직접 설치하는 튜토리얼을 참조하는 것이 좋습니다:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Bitcoin 네트워크에 진정으로 참여하려면 자신의 노드를 실행하고 사용하는 것이 필수적입니다. Bitcoin 노드를 운영한다고 해서 사용자에게 금전적인 이득은 없지만, 개인 정보를 보호하고 독립적으로 행동하며 네트워크에 대한 신뢰를 제어할 수 있습니다.


이 글에서는 자체 Bitcoin 노드를 운영할 수 있는 훌륭한 솔루션인 RoninDojo에 대해 자세히 살펴보겠습니다.


### 목차:



- 로닌도장이란 무엇인가요?
- 어떤 하드웨어를 선택해야 하나요?
- 로닌도장을 설치하는 방법은 무엇인가요?
- 로닌도장은 어떻게 사용하나요?
- 결론


Bitcoin 노드의 작동 방식과 역할에 대해 잘 모르신다면 이 글부터 읽어보시기 바랍니다: Bitcoin 노드 - 1/2부: 기술 개념.


![Samourai](assets/1.webp)


## 로닌도장이란 무엇인가요?


Dojo는 사무라이 Bitcoin 팀이 개발한 풀 Wallet 노드 서버입니다. 모든 머신에 자유롭게 설치할 수 있습니다.


로닌도장은 도장 및 기타 다양한 도구를 위한 설치 도우미이자 관리 도구입니다. 로닌도조는 도조의 원래 구현에 다른 많은 도구를 추가하는 동시에 설치와 관리를 더 쉽게 해줍니다.


또한 '플러그 앤 플레이' 하드웨어인 '로닌도조 탄토'를 제공하며, 팀에서 조립한 기계에 로닌도조가 사전 설치되어 있습니다. Tanto는 손을 더럽히고 싶지 않은 사람들에게 적합한 유료 솔루션입니다.


로닌도조의 코드는 오픈 소스이므로 자체 하드웨어에 이 솔루션을 설치할 수도 있습니다. 이 옵션은 비용 효율적이지만 조금 더 많은 조작이 필요하므로 이 글에서 설명하겠습니다.


로닌도장은 도장이기 때문에 Whirlpool CLI을 Bitcoin 노드에 쉽게 통합하여 최상의 CoinJoin 경험을 할 수 있습니다. Whirlpool CLI을 사용하면 개인 컴퓨터를 계속 켜둘 필요 없이 24시간 내내 비트코인을 리믹스할 수 있을 뿐만 아니라 개인 정보 보호도 크게 향상시킬 수 있습니다.


로닌도장은 거래의 프라이버시 수준을 결정하는 볼츠만 계산기, 다양한 Bitcoin 지갑을 노드에 연결하는 일렉트럼 서버, 거래를 비공개로 관찰하는 Mempool 서버 등 도장에 의존하는 다른 많은 도구를 통합하고 있습니다.

이 글에서 소개해드린 엄브렐과 같은 다른 노드 솔루션과 비교했을 때, 로닌도조는 사용자 프라이버시를 최적화하는 "on chain" 솔루션과 도구에 집중하고 있습니다. 따라서 로닌도조는 Lightning Network와의 상호 작용을 허용하지 않습니다.

로닌도조는 엄브렐에 비해 도구 수는 적지만, 비트코인 이용자에게 필수적인 몇 가지 기능은 매우 안정적입니다.


따라서 엄브렐 서버의 모든 기능이 필요하지 않고 Whirlpool 또는 Mempool과 같은 몇 가지 필수 도구가 포함된 간단하고 안정적인 노드만 원한다면 RoninDojo가 좋은 솔루션이 될 수 있습니다.


제 생각에 엄브렐의 개발 초점은 Lightning Network과 다용도 도구에 맞춰져 있습니다. 아직 Bitcoin 노드이지만 멀티태스킹 미니 서버를 만드는 것이 목표입니다. 반면, 로닌도조의 개발 초점은 사무라이 Wallet의 팀과 더 일치하며 비트코인을 위한 필수 도구에 초점을 맞추고 있으며, Bitcoin에서 완전한 독립성과 최적화된 개인 정보 관리를 가능하게 합니다.


로닌도장 노드 설정은 엄브렐 노드보다 약간 더 복잡하다는 점에 유의하세요.


이제 로닌도조에 대한 그림을 그릴 수 있었으니 이 노드를 어떻게 설정하는지 함께 살펴봅시다.


## 어떤 하드웨어를 선택해야 하나요?


로닌도장을 호스팅하고 실행하는 머신을 선택하려면 몇 가지 옵션이 있습니다.


앞서 설명한 것처럼 가장 간단한 방법은 이 용도로 특별히 설계된 플러그 앤 플레이 기계인 Tanto를 주문하는 것입니다. 주문하려면 여기를 방문하세요: [링크](https://shop.ronindojo.io/product-category/nodes/).


로닌도조 팀은 오픈 소스 코드를 제작하기 때문에 다른 컴퓨터에서도 로닌도조를 구현할 수 있습니다. 이 페이지에서 최신 버전의 설치 마법사를 찾을 수 있습니다: [링크](https://ronindojo.io/en/downloads.html), 이 페이지에서 최신 버전의 코드를 확인할 수 있습니다: [링크](https://code.samourai.io/ronindojo/RoninDojo).


개인적으로 라즈베리 파이 4 8GB에 설치했는데 모든 것이 완벽하게 작동합니다.


그러나 로닌도조 팀은 케이스와 SSD 어댑터에 문제가 있는 경우가 많다고 지적합니다. 따라서 컴퓨터의 SSD용 케이블이 있는 케이스는 사용하지 않는 것이 좋습니다. 대신, 이와 같이 마더보드용으로 특별히 설계된 스토리지 확장 카드를 사용하는 것이 좋습니다: 라즈베리파이 4 스토리지 확장 카드.


다음은 자신만의 로닌도장 노드를 설정하는 방법의 예시입니다:



- 라즈베리 파이 4.
- 팬이 있는 케이스.
- 호환되는 스토리지 확장 카드.
- 전원 케이블.
- 16GB 이상의 산업용 마이크로 SD 카드.
- 1TB 이상의 SSD.
- RJ45 이더넷 케이블, 카테고리 8 권장.


## 로닌도조를 설치하는 방법?


### 1단계: 부팅 가능한 마이크로 SD 카드를 준비합니다.


기기를 조립했으면 이제 로닌도조 설치를 시작할 수 있습니다. 이렇게 하려면 먼저 적절한 디스크 이미지를 구워 부팅 가능한 마이크로 SD 카드를 만듭니다.


마이크로 SD 카드를 개인용 컴퓨터에 삽입한 다음 공식 RoninDojo 웹사이트로 이동하여 RoninOS 디스크 이미지를 다운로드합니다(https://ronindojo.io/en/downloads.html).


하드웨어에 해당하는 디스크 이미지를 다운로드합니다. 제 경우에는 "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" 이미지를 다운로드했습니다:


![Download RoninOS disk image](assets/2.webp)


이미지가 다운로드되면 해당 .SHA256 파일을 사용하여 이미지의 무결성을 확인합니다. 이 문서에서 이 작업을 수행하는 방법을 자세히 설명하겠습니다: Windows에서 Bitcoin 소프트웨어의 무결성을 확인하는 방법은 무엇인가요?


RoninOS의 무결성을 확인하기 위한 구체적인 지침은 이 페이지(https://wiki.ronindojo.io/en/extras/verify)에서도 확인할 수 있습니다.


이 이미지를 마이크로 SD 카드에 구우려면 여기에서 다운로드할 수 있는 Balena Etcher와 같은 소프트웨어를 사용할 수 있습니다(https://www.balena.io/etcher/).


이렇게 하려면 에처에서 이미지를 선택하고 마이크로 SD 카드에 플래시합니다:


![Burn disk image with Etcher](assets/3.webp)


작업이 완료되면 부팅 가능한 마이크로 SD 카드를 라즈베리파이에 삽입하고 머신의 전원을 켤 수 있습니다.


### 2단계: RoninOS 구성하기.


로닌OS는 로닌도조 노드의 운영체제입니다. 리눅스 배포판인 만자로의 수정 버전입니다. 컴퓨터를 시작하고 몇 분 정도 기다리면 구성을 시작할 수 있습니다.


원격으로 연결하려면, 로닌도조 머신의 IP Address를 찾아야 합니다. 이를 위해 인터넷 박스의 관리 패널에 연결하거나 https://angryip.org/ 같은 소프트웨어를 다운로드하여 로컬 네트워크를 스캔하고 머신의 IP를 찾을 수 있습니다.


IP를 찾으면 SSH를 사용하여 동일한 로컬 네트워크에 연결된 다른 컴퓨터에서 내 컴퓨터를 제어할 수 있습니다.


MacOS 또는 Linux를 실행하는 컴퓨터에서는 터미널을 열기만 하면 됩니다. Windows를 실행하는 컴퓨터에서는 Putty와 같은 특수 도구를 사용하거나 Windows PowerShell을 직접 사용할 수 있습니다.


터미널이 열리면 다음 명령을 입력합니다:

```
ssh root@192.168.?.?
```


물음표 두 개를 이전에 찾은 로닌도장의 IP로 바꾸기만 하면 됩니다.

팁: 셸에서 마우스 오른쪽 버튼을 클릭하여 항목을 붙여넣습니다.


다음으로 Manjaro 제어판으로 이동합니다. 화살표를 사용하여 올바른 키보드 레이아웃을 선택하고 드롭다운 목록에서 대상을 변경합니다.


![Manjaro Keyboard Configuration](assets/4.webp)


세션의 사용자 아이디와 비밀번호를 선택합니다. 강력한 비밀번호를 사용하고 안전한 백업을 만드세요. 설치 중에 선택적으로 약한 비밀번호를 사용하고 나중에 RoninUI에 "복사하여 붙여넣기"하여 쉽게 변경할 수 있습니다. 이렇게 하면 Manjaro를 설치하는 동안 수동으로 비밀번호를 입력하는 데 너무 많은 시간을 소비하지 않고도 매우 강력한 비밀번호를 사용할 수 있습니다.


![Manjaro Username Configuration](assets/5.webp)


다음으로 루트 비밀번호를 선택하라는 메시지가 표시됩니다. 루트 비밀번호는 강력한 비밀번호를 직접 입력하세요. RoninUI에서는 변경할 수 없습니다. 또한 이 루트 비밀번호를 안전하게 백업하는 것을 잊지 마세요.


그런 다음 위치와 시간대를 입력합니다.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


다음으로 호스트 이름을 선택합니다.


![Manjaro Hostname Configuration](assets/8.webp)


마지막으로 Manjaro 구성 정보를 확인하고 확인합니다.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### 3단계: 로닌도조를 다운로드합니다.


RoninOS의 초기 구성이 완료됩니다. 위의 스크린샷과 같이 완료되면 머신이 다시 시작됩니다. 잠시 기다렸다가 다음 명령을 입력하여 RoninDojo 머신에 다시 연결합니다:

```
ssh username@192.168.?.?
```


'사용자 이름'을 이전에 선택한 사용자 이름으로 바꾸고 물음표는 로닌도장의 IP로 바꾸기만 하면 됩니다.


그런 다음 사용자 비밀번호를 입력합니다.


터미널에서는 다음과 같이 표시됩니다:


![SSH Connection to RoninOS](assets/10.webp)


이제 현재 로닌OS만 설치되어 있는 컴퓨터에 연결되었습니다. 이제 로닌도조를 설치해야 합니다.


다음 명령을 입력하여 최신 버전의 로닌도장을 다운로드하세요:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


다운로드가 빠르게 진행됩니다. 터미널에 이렇게 표시됩니다:


![Cloning RoninDojo](assets/11.webp)


다운로드가 완료될 때까지 기다렸다가 다음 명령을 사용하여 RoninDojo 사용자 Interface을 설치하고 액세스합니다:

```
~/RoninDojo/ronin
```


사용자 비밀번호를 입력하라는 메시지가 표시됩니다:


![Bitcoin Node Password Verification](assets/12.webp)


이 명령은 로닌도장에 처음 접속할 때만 필요합니다. 이후 SSH를 통해 RoninCLI에 접속하려면 [SSH username@192.168.?.?] 명령어를 입력한 후 "username"을 사용자 이름으로 바꾸고 노드의 IP Address를 입력하기만 하면 됩니다. 사용자 비밀번호를 입력하라는 메시지가 표시됩니다.


다음으로 이 멋진 애니메이션을 볼 수 있습니다:


![RoninCLI launch animation](assets/13.webp)


그러면 마침내 로닌도장 CLI 사용자 Interface에 도착하게 됩니다.


### 4단계: 로닌도조를 설치합니다.


주 메뉴에서 키보드의 화살표 키를 사용하여 '시스템' 메뉴로 이동합니다. Enter 키를 눌러 선택을 확인합니다.


![RoninCLI navigation menu to System](assets/14.webp)


그런 다음 '시스템 설정 및 설치' 메뉴로 이동합니다.


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


마지막으로 스페이스바를 사용해 '시스템 설정'과 '로닌도조 설치'를 선택한 다음 '수락'을 선택해 설치를 시작합니다.


![RoninDojo installation confirmation](assets/16.webp)


설치가 조용히 진행되도록 합니다. 제 경우에는 2시간 정도 걸렸습니다. 설치하는 동안 단말기를 열어두세요.


예를 들어 여기와 같이 설치의 특정 단계에서 키를 눌러야 하는 경우가 있으므로 가끔 단말기를 확인하세요:


![RoninDojo installation in progress](assets/17.webp)


설치가 끝나면 다른 컨테이너가 시작되는 것을 볼 수 있습니다:


![Node container startup](assets/18.webp)


그러면 노드가 다시 시작됩니다. 다음 단계를 위해 RoninCLI에 다시 연결합니다.


![Bitcoin node restart](assets/19.webp)


### 5단계: Proof-of-Work 체인을 다운로드하고 RoninUI에 액세스합니다.


설치가 완료되면 노드가 Bitcoin Proof-of-Work 체인을 다운로드하기 시작합니다. 이를 초기 블록 다운로드(IBD)라고 합니다. 일반적으로 인터넷 연결과 디바이스에 따라 2일에서 14일 정도 소요됩니다.


체인 다운로드 진행 상황은 RoninUI 웹 Interface에 액세스하여 추적할 수 있습니다.


로컬 네트워크에서 액세스하려면 브라우저의 Address 표시줄에 다음을 입력합니다:



- 머신의 IP Address(192.168.?.?)를 직접 입력하세요
- 또는 다음을 입력하세요


VPN을 사용 중이라면 비활성화하는 것을 잊지 마세요.


### 가능한 반전


브라우저에서 RoninUI에 연결할 수 없는 경우, SSH를 통해 노드에 연결된 터미널에서 애플리케이션이 제대로 작동하는지 확인하세요. 이전 단계에 따라 메인 메뉴에 연결합니다:



- 입력합니다: SSH username@192.168.?.? 사용자 자격 증명으로 대체합니다.



- 사용자 비밀번호를 입력합니다.


메인 메뉴에서 다음으로 이동합니다: **RoninUI > 재시작**으로 이동합니다


애플리케이션이 올바르게 다시 시작되면 브라우저 연결에 문제가 있는 것입니다. VPN을 사용하고 있지 않은지 확인하고 노드와 동일한 네트워크에 연결되어 있는지 확인하세요.


다시 시작해도 오류가 발생하면 운영 체제를 업데이트한 다음 RoninUI를 다시 설치해 보세요. 운영체제를 업데이트하려면 **시스템 > 소프트웨어 업데이트 > 운영 체제 업데이트**로 이동합니다


업데이트 및 재시작이 완료되면 SSH를 통해 노드에 다시 연결하고 RoninUI를 다시 설치합니다: **RoninUI > 재설치**


RoninUI를 다시 다운로드한 후 브라우저를 통해 RoninUI에 연결해 보세요.


**팁: 실수로 RoninCLI를 종료하고 만자로 터미널을 찾은 경우, "ronin" 명령을 입력하면 RoninCLI의 메인 메뉴로 바로 돌아갈 수 있습니다.


### 웹 로그인


토어를 사용하는 모든 네트워크에서 RoninUI 웹 Interface에 로그인할 수도 있습니다. 이렇게 하려면 RoninCLI: **자격증명 > Ronin UI**에서 RoninUI의 Tor Address를 검색합니다


.onion으로 끝나는 Tor Address를 검색한 다음, Tor 브라우저에 이 Address를 입력하여 Ronin UI에 로그인하세요. 다양한 자격 증명은 민감한 정보이므로 유출되지 않도록 주의하세요.


![RoninUI web login interface](assets/20.webp)


로그인하면 사용자 비밀번호를 입력하라는 메시지가 표시됩니다. 이 비밀번호는 SSH를 통해 로그인할 때 사용하는 것과 동일한 비밀번호입니다.


![RoninUI web interface management panel](assets/21.webp)


여기에서 IBD(초기 블록 다운로드)의 진행 상황을 확인할 수 있습니다. 2009년 1월 3일 이후 Bitcoin에서 이루어진 모든 트랜잭션을 검색하고 있으니 잠시만 기다려주세요.


전체 Blockchain을 다운로드한 후 인덱서는 데이터베이스를 압축합니다. 이 작업에는 약 12시간이 소요됩니다. RoninUI의 "인덱서"에서 진행 상황을 추적할 수도 있습니다.


이 작업이 끝나면 로닌도장 노드가 완전히 작동합니다:


![Indexer synchronized at 100% functional node](assets/22.webp)


사용자 비밀번호를 더 강력한 비밀번호로 변경하고 싶다면 지금 '설정' 탭에서 변경할 수 있습니다. 로닌도조에는 추가 보안 Layer이 없기 때문에 정말 강력한 비밀번호를 선택하고 백업을 관리하는 것이 좋습니다.


## 로닌도장은 어떻게 사용하나요?


체인을 다운로드하고 압축하면 새로운 로닌도조 노드에서 제공하는 서비스를 즐길 수 있습니다. 사용 방법을 살펴보겠습니다.


### Wallet 소프트웨어를 일렉트릭에 연결합니다.


새로 설치 및 동기화된 노드의 첫 번째 유틸리티는 트랜잭션을 Bitcoin 네트워크로 브로드캐스트하는 것입니다. 따라서 다른 Wallet 관리 소프트웨어를 여기에 연결하고 싶을 것입니다.


일렉트럼 Rust 서버(electrs)를 사용하여 이 작업을 수행할 수 있습니다. 이 애플리케이션은 일반적으로 RoninDojo 노드에 사전 설치되어 있습니다. 그렇지 않은 경우 RoninCLI Interface에서 수동으로 설치할 수 있습니다.


다음으로 이동하세요: **애플리케이션 > 애플리케이션 관리 > 일렉트럼 서버 설치**로 이동하세요


일렉트럼 서버의 토르 Address를 얻으려면, RoninCLI 메뉴에서 다음으로 이동하세요:

**자격 증명 > Electrs**


Wallet 소프트웨어에 .onion 링크를 입력하기만 하면 됩니다. 예를 들어 Sparrow wallet에서는 탭으로 이동합니다:

**파일 > 환경설정 > 서버**


서버 유형에서 '사설 일렉트럼'을 선택한 다음, 해당 필드에 일렉트럼 서버의 토르 Address을 입력하세요. 마지막으로, "연결 테스트"를 클릭하여 연결을 테스트하고 저장하세요.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Wallet 소프트웨어를 사무라이 도장에 연결합니다.


Electrs를 사용하는 대신 사무라이 도장을 사용하여 호환되는 Software Wallet를 로닌도장 노드에 연결할 수도 있습니다. 예를 들어 사무라이 Wallet은 이 옵션을 제공합니다.


이렇게 하려면 도장의 연결 QR 코드를 스캔하기만 하면 됩니다. RoninUI에서 액세스하려면 "대시보드" 탭을 클릭한 다음 도장 상자에 있는 "관리" 버튼을 클릭합니다. 그러면 도장과 BTC-RPC 익스플로러의 연결 QR 코드를 볼 수 있습니다. 이를 표시하려면 "값 표시"를 클릭합니다.


![Retrieving the connection QR code to Dojo](assets/24.webp)


사무라이 Wallet를 도장에 연결하려면 애플리케이션을 설치하는 동안 이 QR 코드를 스캔해야 합니다:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### 자체 Mempool 탐색기 사용.


비트코인 사용자에게 필수적인 도구인 탐색기를 통해 Bitcoin 체인에 대한 다양한 정보를 확인할 수 있습니다. 예를 들어, Mempool을 사용하면 다른 사용자가 적용한 수수료를 실시간으로 확인하고 그에 따라 자신의 수수료를 조정할 수 있습니다. 또한 거래 중 하나의 승인 상태를 확인하거나 Address의 잔액을 확인할 수도 있습니다.


이러한 탐색기 도구는 개인정보 위험에 노출될 수 있으며 타사의 데이터베이스를 신뢰해야 할 수도 있습니다. 자체 노드를 거치지 않고 이 온라인 도구를 사용하는 경우:



- Wallet에 대한 정보가 유출될 위험이 있습니다.



- 호스팅하는 Proof-of-Work 체인의 웹사이트 관리자를 신뢰합니다.


이러한 위험을 피하기 위해 토르 네트워크를 통해 노드에서 자체 Mempool 인스턴스를 사용할 수 있습니다. 이 솔루션을 사용하면 서비스를 사용할 때 개인 정보를 보호할 수 있을 뿐만 아니라, 자체 데이터베이스를 쿼리하기 때문에 더 이상 제공업체를 신뢰할 필요가 없습니다.


이렇게 하려면 먼저 RoninCLI에서 Mempool 스페이스 비주얼라이저를 설치합니다:


**애플리케이션 > 애플리케이션 관리 > Mempool 스페이스 비주얼라이저 설치**


설치가 완료되면, Mempool에 대한 링크를 검색하세요. 토르 Address는 모든 네트워크에서 접속할 수 있습니다. 마찬가지로 RoninCLI를 통해 이 링크를 검색합니다:


**자격 증명 > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


토르 브라우저에 Mempool 토르 Address를 입력하기만 하면 자신의 데이터에 기반한 나만의 Mempool 인스턴스를 즐길 수 있습니다. 더 빠른 액세스를 위해 즐겨찾기에 토르 Address를 추가하는 것을 추천합니다. 바탕화면에 바로가기를 만들 수도 있습니다.


![Mempool Space interface](assets/27.webp)


아직 Tor 브라우저가 없는 경우, 여기에서 다운로드할 수 있습니다: https://www.torproject.org/download/


스마트폰에서도 토르 브라우저를 설치하고 동일한 Address을 입력해 접속할 수 있습니다. 어디서든 자신의 노드를 사용하여 Bitcoin 체인의 상태를 확인할 수 있습니다.


### Whirlpool CLI 사용.


로닌도조 노드에는 Whirlpool 믹스를 자동화하기 위한 원격 명령줄 Interface인 WhirlpoolCLI도 포함되어 있습니다.


Whirlpool 구현으로 CoinJoin를 수행하는 경우, 믹스 및 리믹스를 실행하려면 사용 중인 애플리케이션이 열려 있어야 합니다. 이 과정은 높은 애니온 세트를 원하는 사용자에게는 지루할 수 있는데, Whirlpool으로 애플리케이션을 호스팅하는 디바이스가 계속 켜져 있어야 하기 때문입니다. 즉, 24시간 리믹스에 UTXO를 사용하려면 애플리케이션이 열려 있는 상태에서 개인용 컴퓨터나 휴대폰을 계속 켜두어야 한다는 뜻입니다.


이러한 제약 조건에 대한 한 가지 해결책은 Bitcoin 노드와 같이 항상 켜져 있어야 하는 머신에서 WhirlpoolCLI를 사용하는 것입니다. 이를 통해 Bitcoin 노드 이외의 다른 시스템을 계속 가동할 필요 없이 24시간 연중무휴로 UTXO를 리믹스할 수 있습니다.

월풀CLI는 코인조인을 쉽게 관리하기 위해 개인용 컴퓨터에 설치하는 그래픽 Interface인 월풀GUI와 함께 사용됩니다. 이 글에서는 Whirlpool CLI을 도장에 설치하는 방법에 대해 자세히 설명하겠습니다: [링크](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


CoinJoin에 대해 전반적으로 자세히 알아보려면 이 문서에서 모든 것을 설명합니다: [링크](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Whirlpool 통계 도구 사용.


Whirlpool로 코인조인을 수행한 후, 혼합 UTXO의 실제 프라이버시 수준을 알고 싶을 수 있습니다. Whirlpool 통계 도구를 사용하면 쉽게 확인할 수 있습니다. 이 도구를 사용하면 혼합 UTXO의 예상 점수와 소급 점수를 계산할 수 있습니다. 이러한 익명 세트 계산과 그 작동 방식에 대해 자세히 알아보려면 이 섹션을 읽어보시기 바랍니다: [링크](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


이 도구는 로닌도장에 사전 설치되어 있습니다. 현재로서는 RoninCLI에서만 사용할 수 있습니다. 메인 메뉴에서 실행하려면 다음으로 이동하세요:

**사무라이 툴킷 > Whirlpool 스탯 도구**


사용 지침이 표시됩니다. 완료되면 아무 키나 눌러 명령줄에 액세스합니다:


![Whirlpool Stats Tool software home](assets/28.webp)


터미널이 표시됩니다:

**WST#/TMP>**


이 Interface을 종료하고 RoninCLI 메뉴로 돌아가려면 명령을 입력하기만 하면 됩니다:

```
quit
```


먼저, 완전한 프라이버시를 유지하면서 OXT 데이터를 추출하기 위해 Tor에서 프록시를 설정합니다. 명령을 입력합니다:

```
socks5 127.0.0.1:9050
```


그런 다음 트랜잭션이 포함된 풀에서 데이터를 다운로드합니다:

```
download 0001
```


**참고: `0001`을 관심 있는 풀 디노미네이션 코드로 바꾸세요.


WST의 디노미네이션 코드는 다음과 같습니다:



- 풀 0.5비트코인: 05
- 풀 0.05 비트코인: 005
- 풀 0.01비트코인: 001
- 풀 0.001비트코인: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


데이터가 다운로드되면 다음 명령을 사용하여 데이터를 로드합니다:

```
load 0001
```


**참고: `0001`을 관심 있는 풀 디노미네이션 코드로 바꾸세요.


![Loading data from pool 0001](assets/30.webp)

몇 분 정도 소요될 수 있으므로 로딩 과정을 기다리세요. 데이터를 로드한 후 점수 명령어와 txid(트랜잭션 식별자)를 입력하면 해당 Anon 세트를 가져올 수 있습니다:

```
score TXID
```


**참고: `txid`을 거래의 식별자로 대체합니다.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


그러면 WST는 소급 점수(소급 지표)와 전망 점수(전망 지표)를 표시합니다. WST는 익명 세트의 점수 외에도 익명 세트를 기반으로 풀에서 내 결과물의 확산 속도도 제공합니다.


UTXO의 예상 점수는 마지막 믹스가 아닌 초기 믹스의 txid를 기준으로 계산된다는 점에 유의하세요. 반대로 UTXO의 소급 점수는 마지막 주기의 txid를 기준으로 계산됩니다.


다시 한 번, Anon 세트의 이러한 개념을 이해하지 못하신다면, 모든 것을 다이어그램으로 자세히 설명하는 CoinJoin에 대한 제 글의 이 부분을 읽어보시기 바랍니다: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### 볼츠만 계산기 사용.


볼츠만 계산기는 엔트로피 수준을 포함한 Bitcoin 트랜잭션의 다양한 고급 지표를 쉽게 계산할 수 있는 도구입니다. 이 모든 데이터를 통해 트랜잭션의 개인정보 보호 수준을 정량화하고 잠재적인 오류를 감지할 수 있습니다. 이 도구는 로닌도조 노드에 사전 설치되어 있습니다.


RoninCLI에서 액세스하려면 SSH를 통해 연결한 다음 메뉴로 이동합니다:

**사무라이 툴킷 > 볼츠만 계산기**


로닌도조에서 사용하는 방법을 설명하기 전에 이러한 지표가 무엇을 나타내는지, 어떻게 계산되는지, 어떤 용도로 사용되는지 설명하겠습니다.


이러한 지표는 모든 Bitcoin 거래에 사용할 수 있지만, 특히 CoinJoin 거래의 품질을 연구하는 데 유용합니다.


1. 이 소프트웨어가 계산하는 첫 번째 지표는 가능한 조합의 수입니다. 계산기에는 "nb 조합"으로 표시됩니다. UTXO의 값이 주어지면 이 지표는 입력에서 출력으로 가능한 매핑의 수를 나타냅니다.


**참고: 'UTXO'이라는 용어에 익숙하지 않으시다면 이 짧은 글을 읽어보시기 바랍니다:


> Bitcoin 트랜잭션의 메커니즘: UTXO, 입력 및 출력.

즉, 이 지표는 주어진 트랜잭션에 대해 가능한 해석의 수를 나타냅니다. 예를 들어, Whirlpool 5x5 CoinJoin 구조의 경우 가능한 조합의 수는 1496개입니다:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


신용: KYCP


2. 두 번째로 계산된 지표는 트랜잭션의 엔트로피입니다. 트랜잭션에서 가능한 조합의 수가 매우 많을 수 있으므로 엔트로피를 대신 사용할 수 있습니다. 엔트로피는 가능한 조합 수의 이진 로그를 나타냅니다. 공식은 다음과 같습니다:



- E: 트랜잭션의 엔트로피.
- C: 트랜잭션에 가능한 조합의 수입니다.


**E = log2(C)**


수학에서 이항 로그(기저 2)는 2함수의 거듭제곱의 역함수입니다. 즉, x의 이항 로그는 값 x를 얻기 위해 숫자 2를 올려야 하는 거듭제곱입니다.


따라서:


**E = log2(C)**


**C = 2^E**


이 지표는 비트 단위로 표시됩니다. 예를 들어, 다음은 앞서 언급한 조합 가능 수가 1496인 Whirlpool 5x5 CoinJoin 트랜잭션의 엔트로피를 계산한 것입니다:


**C = 1496**


**E = log2(1496)**


**E = 10.5469비트**


따라서 이 CoinJoin 트랜잭션의 엔트로피는 10.5469비트로 매우 양호합니다.


이 지표가 높을수록 거래에 대한 다양한 해석이 존재하며, 따라서 거래의 기밀성이 높다는 의미입니다.


다른 예를 들어보겠습니다. 다음은 하나의 입력과 두 개의 출력이 있는 '클래식' 트랜잭션입니다:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


크레딧: OXT


이 트랜잭션은 한 가지 해석만 가능합니다:


**[(inp 0) > (Outp 0 ; Outp 1)]**


따라서 엔트로피는 0이 됩니다:


**C = 1**,

**E = log2(C)**,

**E = 0**


3. 볼츠만 계산기가 반환하는 세 번째 지표는 "Wallet 효율성"이라는 Tx의 효율성입니다. 이 지표를 사용하면 입력 트랜잭션과 동일한 구성에서 가능한 최상의 트랜잭션을 간단히 비교할 수 있습니다.


이제 주어진 트랜잭션 구조에서 달성할 수 있는 가장 높은 엔트로피를 나타내는 최대 엔트로피 개념을 소개하겠습니다. 예를 들어, Whirlpool 5x5 CoinJoin 구조의 최대 엔트로피는 10.5469입니다. 효율성 지표는 이 최대 엔트로피와 입력 트랜잭션의 실제 엔트로피를 비교합니다. 공식은 다음과 같습니다:



- ER: 비트 단위로 표현되는 실제 엔트로피입니다.
- EM: 비트 단위로 표현되는 동일한 구조의 최대 엔트로피.
- Ef: 비트 단위로 표시되는 효율성.


**Ef = ER - EM**


**Ef = 10.5469 - 10.5469**


**Ef = 0비트**


이 지표는 백분율로도 표시되므로 공식은 다음과 같습니다:



- CR: 실제 가능한 조합의 수입니다.
- CM: 동일한 구조로 가능한 최대 조합 수입니다.
- Ef: 백분율로 표시되는 효율성.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


효율성이 100%라는 것은 이 트랜잭션의 구조에 비해 프라이버시 보호 수준이 가장 높다는 것을 의미합니다.


4. 네 번째로 계산된 지표는 엔트로피 밀도입니다. 이를 통해 엔트로피를 각 입력 또는 출력과 연관시킬 수 있습니다. 이 지표는 크기가 다른 트랜잭션 간의 효율성을 비교하는 데 사용할 수 있습니다.


트랜잭션의 엔트로피를 존재하는 입력과 출력의 수로 나누면 계산은 매우 간단합니다. 예를 들어, Whirlpool 5x5 CoinJoin의 경우 다음과 같습니다:


ED: 비트 단위로 표시되는 엔트로피 밀도입니다.

E: 비트 단위로 표현되는 트랜잭션 엔트로피입니다.

T: 트랜잭션의 총 입력 및 출력 수입니다.


T = 5 + 5 = 10

ED = E/T

Ed = 10.5469 / 10

ED = 1.054비트


볼츠만 계산기가 제공하는 다섯 번째 정보는 입력과 출력 사이의 연결 확률 표입니다. 이 표는 단순히 주어진 입력이 주어진 출력에 대응할 확률(볼츠만 점수)을 알려줍니다.


Whirlpool CoinJoin를 예로 들어보면 확률 표는 다음과 같습니다:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


여기서 각 입력이 각 출력에 연결될 확률이 동일하다는 것을 알 수 있습니다.


그러나 하나의 입력과 두 개의 출력이 있는 트랜잭션의 예를 들어보면 다음과 같습니다:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

이 예제에서는 입력 0에서 각 출력이 나올 확률이 100%임을 알 수 있습니다.


이 확률이 낮을수록 개인정보 보호 수준이 높아집니다.


6. 계산되는 여섯 번째 정보는 결정적 링크의 수입니다. 결정적 링크의 비율도 제공됩니다. 이 지표는 주어진 트랜잭션의 입력과 출력 사이의 확률이 100%인, 즉 부인할 수 없는 링크의 수를 강조 표시합니다.


비율은 총 링크 수에 대한 트랜잭션의 결정적 링크 수를 나타냅니다.


예를 들어 CoinJoin Whirlpool 트랜잭션은 입력과 출력 사이에 결정론적 링크가 없습니다. 지표는 0이 되고 비율도 0%가 됩니다.


그러나 연구된 두 번째 거래(입력 1개, 출력 2개)의 경우 지표는 2이고 비율은 100%입니다.


따라서 이 표시기가 0이면 프라이버시가 양호한 상태임을 나타냅니다.


이제 지표를 연구 했으므로이 소프트웨어를 사용하여 지표를 계산하는 방법을 살펴 보겠습니다. RoninCLI에서 메뉴로 이동합니다:

**사무라이 툴킷 > 볼츠만 계산기**


![Boltzmann Calculator software homepage](assets/35.webp)


소프트웨어가 실행되면 학습하려는 transaction ID를 입력합니다. 쉼표로 구분하여 여러 거래를 한 번에 입력한 다음 Enter 키를 누를 수 있습니다:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


그러면 계산기가 이전에 보았던 모든 지표를 반환합니다:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


"종료" 명령을 입력하여 소프트웨어를 종료하고 RoninCLI 메뉴로 돌아갑니다.


볼츠만 계산기에 대해 자세히 알아보려면 다음 기사를 읽어보시기 바랍니다:



- https://medium.com/@laurentmt/소개-볼츠만-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Bisq 연결하기.


비스크는 비트코인을 사고 팔 수 있는 피어투피어 Exchange 플랫폼입니다. 토르에서 실행되는 데스크톱 소프트웨어와 함께 사용되며, 신원을 제공하지 않고도 비트코인을 Exchange으로 거래할 수 있습니다.

비스크는 2/2 다중 서명 시스템을 통해 피어투피어 거래소를 보호합니다. 이 소프트웨어를 자체 로닌도조 노드와 함께 사용하여 거래소의 프라이버시를 최적화하고 자체 노드의 Blockchain 데이터를 신뢰할 수 있습니다.


Bisq 소프트웨어를 다운로드하려면 공식 웹사이트(https://bisq.network/)를 방문하세요


소프트웨어를 시작하려면 이 페이지를 읽어보시기 바랍니다: https://bisq.network/getting-started/


로닌도장에서 연결 링크를 검색하려면 SSH를 통해 로닌CLI에 연결해야 합니다. 그런 다음 메뉴로 이동합니다:

**애플리케이션 > 애플리케이션 관리**


비밀번호를 입력한 다음 스페이스 키로 확인란을 선택합니다:

**[ ] Bisq 연결 활성화**


선택을 확인합니다. 노드를 설치한 다음, 다음에서 Tor V3 Address을 검색합니다:

**자격 증명 > bitcoind**


Address을 "Bitcoin daemon" 아래에 복사합니다.


또한, "대시보드"의 "Bitcoin core" 상자에서 "관리"를 클릭하기만 하면 RoninUI Interface에서 bitcoind Tor V3 Address을 검색할 수 있습니다:


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Bisq에서 노드를 연결하려면 메뉴로 이동합니다:

**설정 > 네트워크 정보**


![Access the node connection interface from the Bisq software](assets/39.webp)


"사용자 지정 Bitcoin core 노드 사용" 풍선을 클릭합니다. 그런 다음 지정된 상자에 ".onion"을 포함하되 ".http://"을 제외한 Bitcoin TorV3 Address을 입력합니다.


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Bisq 소프트웨어를 재시작합니다. 이제 노드가 Bisq에 연결되었습니다.


### 기타 기능.


로닌도장 노드에는 다른 기본 기능도 포함되어 있습니다. 특정 정보를 스캔하여 이를 반영할 수 있는 기능이 있습니다.


예를 들어, 로닌도장에 연결된 Wallet이 내 소유의 비트코인을 찾지 못하는 경우가 있습니다. 이 Wallet에 Bitcoin이 있는 것이 확실한데도 잔액이 0인 경우가 있습니다. 파생 경로의 오류를 포함하여 고려할 수 있는 원인은 여러 가지가 있으며, 그 중 노드가 주소를 관찰하지 않을 수도 있습니다.


이 문제를 해결하려면 "xpub 도구"를 사용하여 노드가 xpub을 추적하고 있는지 확인할 수 있습니다. RoninUI에서 이 도구에 액세스하려면 메뉴로 이동합니다:

**유지보수 > XPUB 도구**


문제가 있는 xpub을 입력하고 "확인"을 클릭하여 이 정보를 확인합니다.


![XPUB Tool from RoninUI](assets/41.webp)


노드에서 xpub을 추적하고 있는 경우 이 표시가 나타납니다:


![XPUB Tool result showing successful analysis](assets/42.webp)


모든 트랜잭션이 올바르게 표시되는지 확인합니다. 또한 파생 유형이 Wallet의 파생 유형과 일치하는지 확인합니다. 여기서 노드가 이 xpub를 BIP44 파생으로 해석하는 것을 볼 수 있습니다. 이 파생 유형이 Wallet의 파생 유형과 일치하지 않으면 "유형 다시 입력" 버튼을 클릭한 다음 원하는 대로 BIP44/BIP49/BIP84를 선택합니다:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


노드에서 xpub을 추적하지 않는 경우 가져오기를 요청하는 이 화면이 표시됩니다:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


다른 유지 관리 도구를 사용할 수도 있습니다:



- 거래 도구: 특정 거래의 세부 정보를 관찰할 수 있습니다.
- Address 도구: 특정 Address이 도장에서 추적되고 있는지 확인할 수 있습니다.
- 블록 재검색: 노드에서 선택한 범위의 블록을 강제로 다시 스캔합니다.


RoninUI에서 "Push Tx" 도구도 찾을 수 있습니다. 이를 통해 서명된 트랜잭션을 Bitcoin 네트워크로 브로드캐스트할 수 있습니다. 16진수 형식으로 입력해야 합니다:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## 결론.


이 멋진 도구인 RoninDojo를 설치하고 시작하는 방법을 살펴봤습니다. 자체 Bitcoin 노드를 실행하는 데 탁월한 선택입니다. 비트코인을 위한 모든 필수 도구를 통합하고 최신 상태로 유지하는 안정적인 솔루션입니다.


터미널을 사용하는 것이 두렵지 않고 Lightning Network과 관련된 도구가 필요하지 않다면 RoninDojo가 매력적일 수 있습니다.


가능하다면 이러한 오픈 소스 소프트웨어를 무료로 제작하는 개발자에게 기부하는 것을 고려해 보세요(https://donate.ronindojo.io/)


로닌도조에 대해 자세히 알아보려면 아래의 외부 리소스 링크를 참조하세요.


### 더 읽어보기:



- CoinJoin에서 Bitcoin 이해하기 및 사용하기.
- Hash 기능 - 전자책 Bitcoin 민주주의 1에서 발췌한 내용입니다.
- Bitcoin passphrase에 대해 알아야 할 모든 것.


### 외부 리소스:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/소개-볼츠만-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/