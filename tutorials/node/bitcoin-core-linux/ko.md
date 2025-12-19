---
name: Bitcoin Core (Linux)
description: Linux에서 Bitcoin core로 자체 노드 실행하기
---

![cover](assets/cover.webp)


## Bitcoin core로 자체 노드 실행


Bitcoin 및 노드의 개념에 대한 소개와 Linux에 대한 포괄적인 설치 가이드로 보완됩니다.


Bitcoin의 가장 흥미로운 측면 중 하나는 프로그램을 직접 실행하여 네트워크에 세분화된 수준으로 참여할 수 있고 공개 트랜잭션 Ledger를 검증할 수 있다는 것입니다.


오픈소스 프로젝트인 Bitcoin는 2009년부터 무료로 사용 가능하며 공개적으로 배포되었습니다. 시작 후 거의 17년이 지난 지금, Bitcoin는 강력한 유기적 네트워크 효과의 혜택을 누리는 강력하고 멈출 수 없는 디지털 화폐 네트워크가 되었습니다. 그들의 노력과 비전에 대해 Satoshi 나카모토에게 감사를 표할 만합니다. 참고로, 저희는 Bitcoin 백서를 아고라 256에서 호스팅하고 있습니다(참고: 대학에서도).


### 나만의 은행 되기


자체 노드를 운영하는 것은 Bitcoin의 정신을 따르는 사람들에게 필수적인 일이 되었습니다. 다른 사람의 허락을 받지 않고도 처음부터 Blockchain을 다운로드하여 Bitcoin 프로토콜에 따라 A부터 Z까지 모든 트랜잭션을 검증할 수 있습니다.


이 프로그램에는 자체 Wallet도 포함되어 있습니다. 따라서 당사는 중개자나 제3자 없이 나머지 네트워크에 전송하는 트랜잭션을 제어할 수 있습니다. 여러분은 자신의 은행입니다.


따라서 이 글의 나머지 부분은 가장 널리 사용되는 Bitcoin core 소프트웨어 버전인 Bitcoin를 우분투 및 팝!OS와 같은 데비안 호환 Linux 배포판에 설치하는 방법에 대한 안내서입니다. 이 가이드를 따라 개인 주권에 한 걸음 더 가까이 다가가세요.


## 데비안/우분투용 Bitcoin core 설치 가이드


**전제 조건**


- 최소 6GB의 데이터 스토리지(pruned 노드) - 1TB의 데이터 스토리지(Full node)
- 초기 블록 다운로드*(IBD)에는 최소 24시간이 소요될 것으로 예상됩니다. 이 작업은 pruned 노드에서도 필수입니다.
- pruned 노드에서도 IBD에 최대 600GB의 대역폭을 허용합니다.


**참고: 다음 명령은 Bitcoin core 버전 24.1에 미리 정의되어 있습니다.


### 파일 다운로드 및 확인



- [다운로드](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`와 `SHA256SUMS` 및 `SHA256SUMS.asc` 파일(반드시 최신 버전의 소프트웨어를 다운로드해야 합니다)을 다운로드하세요.



- 다운로드한 파일이 있는 디렉터리에서 터미널을 엽니다. 예: `cd ~/Downloads/`.



- Sha256sum --ignore-missing --check SHA256SUMS` 명령을 사용하여 버전 파일의 체크섬이 체크섬 파일에 나열되어 있는지 확인합니다.



- 이 명령의 출력에는 다운로드한 버전 파일 이름 뒤에 `OK`가 포함되어야 합니다. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Sudo apt install git` 명령을 사용하여 git을 설치합니다. 그런 다음 `git clone https://github.com/Bitcoin-core/guix.sigs` 명령을 사용하여 Bitcoin core 서명자의 PGP 키가 포함된 리포지토리를 복제합니다.



- Gpg --import guix.sigs/builder-keys/*` 명령을 사용하여 모든 서명자의 PGP 키를 가져옵니다



- Gpg --verify SHA256SUMS.asc` 명령을 사용하여 서명자의 PGP 키로 체크섬 파일이 서명되었는지 확인합니다.



유효한 각 서명은 다음과 같이 시작하는 줄을 표시합니다: 'gpg: 양호한 서명'으로 시작하는 줄과 다음으로 끝나는 다른 줄이 표시됩니다: `기본 키 지문: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320`(Pieter Wuille의 PGP 키 지문 예시).


**참고💡:** 모든 서명자 키가 '확인'을 반환할 필요는 없습니다. 실제로 하나만 필요할 수도 있습니다. PGP 확인을 위한 자체 유효성 검사 임계값을 결정하는 것은 사용자의 몫입니다.


경고를 무시해도 됩니다:



- '이 키는 신뢰할 수 있는 서명으로 인증되지 않았습니다!



- 서명이 소유자의 것임을 나타내는 표시가 없습니다


### Bitcoin core 그래픽 Interface 설치



- 터미널에서 Bitcoin core 버전 파일이 있는 디렉터리에서 `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` 명령을 사용하여 아카이브에 포함된 파일을 압축 해제합니다.



- Sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*` 명령을 사용하여 이전에 압축을 푼 파일을 설치합니다



- Sudo apt-get install` 명령을 사용하여 필요한 종속성을 설치합니다. `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- 'Bitcoin-qt' 명령을 사용하여 _bitcoin-qt_(Bitcoin core 그래픽 Interface)를 시작합니다.



- pruned 노드를 선택하려면 _Blockchain 스토리지 제한_에 체크하고 저장할 데이터 제한을 구성합니다:


![welcome](assets/fr/02.webp)


### 1부 마무리: 설치 가이드


Bitcoin core을 설치한 후에는 트랜잭션을 검증하고 다른 피어에게 새 블록을 전송하여 Bitcoin 네트워크에 기여할 수 있도록 가능한 한 계속 실행하는 것이 좋습니다.


그러나 수신 및 발신 트랜잭션의 유효성을 검사하기 위해서라도 노드를 간헐적으로 실행하고 동기화하는 것은 여전히 좋은 습관입니다.


![Creation wallet](assets/fr/03.webp)


## Bitcoin core 노드에 토르 구성하기


**참고💡:** 이 가이드는 우분투/데비안 호환 Linux 배포판의 Bitcoin core 24.0.1을 위해 설계되었습니다.


### Bitcoin core용 Tor 설치 및 구성하기


먼저 익명 통신에 사용되는 네트워크인 토르 서비스(The Onion Router)를 설치해야 Bitcoin 네트워크와의 상호 작용을 익명화할 수 있습니다. Tor를 비롯한 온라인 개인정보 보호 도구에 대한 소개는 이 주제에 대한 도움말 문서를 참조하세요.


토어를 설치하려면 터미널을 열고 `sudo apt -y install tor`를 입력하세요. 설치가 완료되면 일반적으로 서비스가 백그라운드에서 자동으로 실행됩니다. Sudo systemctl status tor` 명령으로 제대로 실행되고 있는지 확인하세요. 응답에 `활성: 활성(종료됨)`이 표시되어야 합니다. 이 기능을 종료하려면 `Ctrl+C`를 누르세요.


**팁: ** 어떤 경우든 터미널에서 다음 명령을 사용해 Tor를 시작, 중지 또는 재시작할 수 있습니다:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


다음으로, `Bitcoin-qt` 명령으로 Bitcoin core 그래픽 Interface을 실행해 보겠습니다. 그런 다음 소프트웨어의 자동 기능을 활성화하여 토르 프록시를 통해 연결을 라우팅합니다: _설정 > 네트워크_에서 _SOCKS5 프록시(기본 프록시)를 통해 연결_과 _별도의 SOCKS5 프록시를 사용하여 토르 양파 서비스를 통해 피어에 연결_을 체크합니다.


![option](assets/fr/04.webp)


Bitcoin core는 Tor가 설치되어 있는지 자동으로 감지하고, 설치되어 있다면 기본적으로 IPv4/IPv6 네트워크(클리어넷)를 사용하는 노드에 대한 연결과 더불어 Tor를 사용하는 다른 노드에 대한 아웃바운드 연결을 생성합니다.


**참고💡:** 표시 언어를 프랑스어로 변경하려면 설정의 표시 탭으로 이동하세요.


### 고급 토르 구성(선택 사항)


피어와 연결할 때 토르 네트워크만 사용하도록 Bitcoin core을 구성하여 노드를 통한 익명성을 최적화할 수 있습니다. 그래픽 Interface에는 이를 위한 기본 제공 기능이 없기 때문에 수동으로 구성 파일을 생성해야 합니다. 설정으로 이동한 다음 옵션으로 이동합니다.


![option 2](assets/fr/05.webp)


여기에서 _설정 파일 열기_를 클릭합니다. Bitcoin.conf` 텍스트 파일에 `onlynet=onion` 줄을 추가하고 파일을 저장합니다. 이 명령을 적용하려면 Bitcoin core를 다시 시작해야 합니다.


그런 다음 Bitcoin core이 프록시를 통해 들어오는 연결을 수신할 수 있도록 Tor 서비스를 구성하여 네트워크의 다른 노드가 우리 컴퓨터의 보안을 손상시키지 않고도 우리 노드를 사용하여 Blockchain 데이터를 다운로드할 수 있도록 합니다.


터미널에서 `sudo nano /etc/tor/torrc`를 입력하여 토르 서비스 구성 파일에 액세스하세요. 이 파일에서 `#ControlPort 9051` 줄을 찾아 `#`를 제거하여 활성화합니다. 이제 파일에 두 줄을 새로 추가합니다:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


파일을 저장하는 동안 파일을 종료하려면 `Ctrl+X > Y > Enter`를 누르세요. 터미널로 돌아가서 `sudo systemctl restart tor` 명령을 입력해 토르를 재시작합니다.


이 구성을 사용하면 Bitcoin core는 토르 네트워크(Onion)를 통해서만 네트워크의 다른 노드와 수신 및 발신 연결을 설정할 수 있습니다. 이를 확인하려면 _윈도우_ 탭을 클릭한 다음 _피어_를 클릭하세요.


![Nodes Window](assets/fr/06.webp)


### 추가 리소스


궁극적으로, 토르 네트워크(`온리넷=온리온`)만 사용하면 Sybil Attack에 취약해질 수 있습니다. 그렇기 때문에 일부에서는 이러한 위험을 완화하기 위해 다중 네트워크 구성을 유지하도록 권장합니다. 또한, 앞서 설명한 대로 토르 프록시를 구성하면 모든 IPv4/IPv6 연결은 토르 프록시를 통해 라우팅됩니다.


또는, 토르 네트워크에만 머물면서 Sybil Attack의 위험을 완화하려면, `addnode=trusted_address.onion` 줄을 추가하여 `Bitcoin.conf` 파일에 다른 신뢰할 수 있는 노드의 Address를 추가할 수 있습니다. 여러 개의 신뢰할 수 있는 노드에 연결하려는 경우 이 줄을 여러 번 추가할 수 있습니다.


토르와의 상호작용과 관련된 Bitcoin 노드의 로그를 보려면, `debug=tor`를 `Bitcoin.conf` 파일에 추가하세요. 이제 디버그 로그에 관련 토르 정보가 표시되며, _정보_ 창에서 _디버그 파일_ 버튼으로 확인할 수 있습니다. 터미널에서 `bitcoind -debug=tor` 명령으로 이 로그를 직접 볼 수도 있습니다.


**팁💡:** 여기에 흥미로운 링크가 있습니다:


- [토르와 Bitcoin과의 관계를 설명하는 위키 페이지](https://en.Bitcoin.it/wiki/Tor)
- [제임슨 롭의 Bitcoin core 구성 파일 생성기](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [존 아택의 토르 설정 가이드](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


언제나 그렇듯이 질문이 있으시면 언제든지 Agora256 커뮤니티에 공유해 주세요. 오늘보다 더 나은 내일이 되기 위해 함께 배웁니다!