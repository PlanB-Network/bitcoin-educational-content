---
name: WireGuard
description: Debian 및 Windows에서 WireGuard VPN 설정하기
---
![cover](assets/cover.webp)



___



*이 튜토리얼은 [IT-Connect](https://www.it-connect.fr/)에 게시된 플로리안 버넬의 오리지널 콘텐츠를 기반으로 합니다. 라이선스 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 원본 텍스트가 변경되었을 수 있습니다*



___



## I. 프레젠테이션



이 튜토리얼에서는 보안을 무시하지 않으면서 성능을 향상시키는 무료 오픈 소스 VPN 솔루션인 WireGuard를 기반으로 VPN을 구성하는 방법에 대해 알아보세요.



와이어가드는 비교적 최근에 출시된 솔루션으로 2020년 3월부터 안정적인 버전으로 제공되고 있으며, 버전 5.6**부터 **리눅스 커널에 직접 통합되는 영광을 누렸습니다. 그렇다고 해서 다른 버전의 커널을 사용하는 구형 Linux 배포판에서 액세스할 수 없는 것은 아닙니다. 이 글의 마지막 부분에서 살펴볼 수 있듯이, OpenVPN 및 IPSec과 같은 솔루션에 비해 WireGuard는 사용이 더 간단하고 훨씬 빠릅니다.



WireGuard에 대한 몇 가지 핵심 사항:





- 간단하고 가벼우며 매우 효율적입니다!
- UDP 전용 작동(특정 방화벽을 통과할 때 단점이 될 수 있음)
- 클라이언트-서버 모델이 아닌 피어-투-피어 모델에서 작동합니다
- 개인/공개 키를 사용하는 SSH와 동일한 원리로 Exchange 키로 인증합니다
- 여러 알고리즘 사용: ChaCha20을 사용한 대칭 암호화, Poly1305를 사용한 메시지 인증, Curve25519, BLAKE2, SipHash24와 같은 기타 알고리즘 사용
- IPv4 및 IPv6 모두 지원
- 멀티 플랫폼: 윈도우, 리눅스, BSD, 맥OS, 안드로이드, iOS, OpenWRT(그리고 ProtonVPN에서 구현됨)
- 다른 솔루션의 수십만 줄에 비해 코드가 4,000줄에 불과합니다



암호화 부분의 경우, 사용되는 다양한 알고리즘을 직접 선택하고 여러 가지 방법으로 감사하며 해당 분야의 전문 보안 연구원이 검사합니다.



공식 프로젝트 웹사이트: [wireguard.com](https://www.wireguard.com/)



이 소개를 읽고 나서 이 솔루션에 확신이 드셨나요? 이제 남은 것은 계속 읽어보시기만 하면 됩니다!



## II. 랩 와이어가드 다이어그램



와이어가드 설치 실습을 소개하기 전에, 와이어가드를 사용하여 **두 원격 인프라를 상호 연결**하는 것뿐만 아니라 **원격 클라이언트를 회사 네트워크 또는 홈 네트워크와 같은 인프라에 연결**하는 것도 상상할 수 있다는 점을 알아두세요. 이는 최근 튜토리얼 '[Synology의 OpenVPN](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)'에서 살펴본 것처럼 OpenVPN과 같은 맥락입니다.



라우터나 방화벽에 직접 WireGuard를 설정하지 않은 경우, OpenWRT에서 생각할 수 있는 것처럼 포트 포워딩을 설정하여 흐름이 WireGuard 쌍에 도달하도록 해야 합니다.



![Image](assets/fr/034.webp)



이제 제 연구실에 대해 말씀드리고 오늘 무엇을 준비할지 알려드리겠습니다.



저는 데비안 11 머신을 와이어가드 서버로, 윈도우 클라이언트를 와이어가드 VPN 클라이언트로 사용하려고 합니다. 클라이언트-서버 관계에 대해 이야기하는 것은 약간 오해의 소지가 있지만, **WireGuard는 "피어 투 피어"** 모델에서 작동하기 때문입니다. 이는 "클라이언트-사이트" 연결을 설정하려고 할 때 약간 잘못된 이름입니다. 대신 두 쌍 또는 원하는 경우 **두 개의 WireGuard 연결 지점**이 있다고 가정해 보겠습니다. 하나는 Debian 11에 있고 다른 하나는 Windows에 있습니다.



이 두 쌍은 양방향으로 서로 통신할 수 있으므로 내 Windows 컴퓨터에서 Debian 11 컴퓨터의 원격 LAN에 액세스할 수 있으며 그 반대의 경우도 가능합니다. 이 모든 것은 터널 및 WireGuard 피어의 방화벽 구성에 따라 달라집니다.



이 예에서는 다음 사례에 초점을 맞추겠습니다: **홈 네트워크에 연결된 Windows 피어 1에서 회사 네트워크에 액세스하여 WireGuard VPN 터널**을 통해 회사 서버에 액세스하려고 합니다. 그러면 다음과 같은 다이어그램이 나타납니다:



![Image](assets/fr/035.webp)



IP 주소 측면에서 보면 다음과 같습니다:





- 홈 네트워크**: 192.168.1.0/24
- 기업 네트워크**: 192.168.100.0/24
- 와이어가드 터널 네트워크**: 192.168.110.0/24


+ 터널 내 피어 1(Windows)의 IP Address: 192.168.110.2/24


+ 터널 내 피어 2(데비안)의 IP Address: 192.168.110.121/24



여기까지입니다! 이제 구성에 대해 알아보겠습니다!



**참고: 기본적으로 WireGuard는 포트 51820**에서 UDP 모드로 작동합니다



## III WireGuard 서버 설치 및 구성



이 튜토리얼에서는 피어 투 피어이긴 하지만 더 의미 있는 용어인 것 같아서 Windows 머신에는 '클라이언트'라는 용어를, Debian 머신에는 '서버'라는 용어를 사용하겠습니다.



### A. 데비안 11에 와이어가드 설치하기



와이어가드 설치 패키지는 공식 데비안 11 리포지토리에서 사용할 수 있으므로 패키지 캐시를 업데이트하고 설치하기만 하면 됩니다:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



구성 관리에 유용한 명령어에 액세스할 수 있는 다양한 도구와 함께 WireGuard 서버 부분이 설치됩니다.



### B. Interface WireGuard 설치하기



명령 "wg"**를 사용하여 개인 키와 공개 키를 generate해야 하는데, 이는 두 쌍, 즉 서버와 클라이언트(키 쌍도 필요함) 간의 인증에 필수적입니다.



이 명령 시퀀스를 사용하여 개인 키 "**/etc/wireguard/wg-private.key**"와 공개 키 "**/etc/wireguard/wg-public.key**"를 생성합니다:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



공개 키의 값은 콘솔에서 반환됩니다. WireGuard 구성 파일에서 개인 키 값을 **추가**해야 합니다. 이 값을 검색하려면 아래 명령어를 입력하고 값을 복사합니다:



```
sudo cat /etc/wireguard/wg-private.key
```



이제 "**/etc/wireguard/**"에 구성 파일을 생성할 차례입니다. 예를 들어, 이 파일의 이름을 "**wg0.conf**"로 지정할 수 있습니다. 예를 들어, WireGuard와 연결된 Interface 네트워크가 "eth0"와 같은 원칙에 따라 "wg0"가 될 것이라고 생각하면 이 파일의 이름을 "**wg0.conf**"로 지정할 수 있습니다.



```
sudo nano /etc/wireguard/wg0.conf
```



이 파일에서 먼저 다음 콘텐츠를 추가해야 합니다(나중에 다시 돌아와서 완성하겠습니다):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



섹션 `[Interface]`은 서버 부분을 선언하는 데 사용됩니다. 다음은 몇 가지 정보입니다:





- Address**: VPN 터널 내 Interface WireGuard의 IP Address(원격 LAN과 다른 서브넷)
- SaveConfig**: Interface이 활성화되어 있는 동안 구성이 저장(및 보호)됩니다
- ListenPort**: WireGuard의 수신 대기 포트입니다. 이 경우 51820이 기본 포트이지만 사용자 지정할 수 있습니다
- PrivateKey**: 서버의 비공개 키 값(*wg-private.key*)



파일을 저장하고 닫습니다. "**wg-quick**" 명령으로 파일 이름을 지정하여 이 Interface을 시작할 수 있습니다(파일 이름은 wg0.conf이므로 wg0):



```
sudo wg-quick up wg0
```



Debian 11 서버의 IP 주소를 나열하면 구성 파일에 정의된 IP Address와 함께 "wg0"이라는 이름의 새 Interface이 표시됩니다:



```
ip a
```



![Image](assets/fr/027.webp)



같은 맥락에서 "wg show" 명령을 통해 Interface "wg0" 구성을 표시할 수 있습니다:



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



마지막으로 Interface wg0 WireGuard의 자동 시작을 활성화해야 합니다:



```
sudo systemctl enable wg-quick@wg0.service
```



지금은 WireGuard의 서버 측 구성에 대해서는 따로 설명하지 않겠습니다.



### C. IP 포워딩 활성화



Debian 11 머신이 라우터와 같이 서로 다른 네트워크 간, 즉 VPN 네트워크와 로컬 네트워크 간에 패킷을 **라우팅**하려면 [IP 포워딩](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/)을 활성화해야 합니다. 기본적으로 이 기능은 비활성화되어 있습니다.



이 구성 파일을 수정합니다:



```
sudo nano /etc/sysctl.conf
```



파일 끝에 다음 지시문을 추가하고 저장합니다:



```
net.ipv4.ip_forward = 1
```



여기까지가 전부입니다.



### D. IP 마스커레이드 활성화



서버가 패킷을 올바르게 라우팅하고 Windows 컴퓨터에서 원격 LAN에 액세스할 수 있도록 하려면 Debian 서버에서 IP 마스커레이드를 활성화해야 합니다. 이것은 일종의 NAT 활성화입니다. 이 구성은 제가 사용하는 데 익숙한 UFW를 통해 Linux 방화벽에서 수행하겠습니다([Debian의 ufw 튜토리얼](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



아직 UFW가 없고 설정하려는 경우(Nftables를 사용할 수도 있음) 설치부터 시작하세요:



```
sudo apt install ufw
```



우선, 원격 서버에 대한 제어권을 잃지 않도록 SSH를 활성화해야 합니다(포트 번호 조정):



```
sudo ufw allow 22/tcp
```



와이어가드에 사용하는 UDP의 51820 포트도 승인되어야 합니다(다시 포트 번호를 조정하세요):



```
sudo ufw allow 51820/udp
```



다음으로 IP 가장 무도회를 활성화하기 위한 구성을 계속 진행하겠습니다. 이를 위해서는 로컬 네트워크에 연결된 Interface의 이름을 검색해야 합니다. 이름을 모르는 경우 "ip a"를 실행하여 카드의 이름을 확인합니다. 제 경우에는 "**ens192**" 카드입니다.



![Image](assets/fr/036.webp)



이 정보를 사용하겠습니다. 다음 파일을 편집합니다:



```
sudo nano /etc/ufw/before.rules
```



파일 끝에 로컬 방화벽의 NAT 테이블의 POSTROUTING 문자열 내에 **Interface ens192**에서 IP 마스커레이드를 활성화하는 줄을 추가합니다(Interface 이름 변경):



```
# NAT - IP masquerade
*nat*
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



그림이 표시됩니다:



![Image](assets/fr/037.webp)



이 구성 파일을 열어두고 다음 단계로 진행하세요 😉



### E. 와이어가드용 리눅스 방화벽 구성



여전히 동일한 구성 파일에서 회사 네트워크를 "192.168.100.0/24"로 선언하여 이 네트워크에 연결할 수 있도록 합니다. 다음은 추가할 두 개의 규칙입니다(규칙을 함께 그룹화하려면 "*# ok icmp code for FORWARD*" 섹션 뒤에 규칙을 추가하는 것이 좋습니다):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



하나의 호스트(예: "192.168.100.11")에만 권한을 부여하려는 경우 쉽게 인증할 수 있습니다:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



이제 파일을 저장하고 닫을 수 있습니다. 이제 UFW를 활성화하고 서비스를 다시 시작하여 변경 사항을 적용하기만 하면 됩니다:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



이제 Debian 서버 구성의 첫 번째 부분이 완료되었습니다.



## IV. Windows용 WireGuard 클라이언트



와이어가드 클라이언트는 윈도우, 맥OS, 안드로이드 등에서 사용할 수 있습니다.... 좋은 소식입니다. 모든 다운로드는 이 페이지에서 가능합니다: [WireGuard 클라이언트](https://www.wireguard.com/install/). 이 예제에서는 Windows에서 클라이언트를 설정하겠습니다. Linux에서 WireGuard 클라이언트를 설정하려면 Debian 시스템에서 wg0.conf 파일을 생성할 때와 동일한 원칙을 따르세요(모든 NAT 등 제외).



### A. WireGuard Windows 클라이언트 설치하기



실행 파일 또는 MSI 패키지를 다운로드한 후 설치 프로그램을 실행하기만 하면 설치가 완료됩니다!



![Image](assets/fr/038.webp)



### B. WireGuard 프로필 만들기



먼저 소프트웨어를 열어 새 터널을 생성합니다. 이렇게 하려면 "**터널 추가**" 버튼 오른쪽에 있는 화살표를 클릭하고 "**빈 터널 추가**" 버튼을 클릭합니다.



![Image](assets/fr/028.webp)



구성 창이 열립니다. 새 터널 구성이 생성될 때마다 WireGuard는 이 구성과 관련된 개인/공개 키 쌍을 생성합니다. **이 구성에서는 "피어", 즉 원격 서버를 다음과 같이 선언해야 합니다



```
[Interface]
PrivateKey = <la clé privée du PC>
```



이 구성을 완료해야 하며, 특히 이 Interface(*Address*)에서 IP Address을 선언하고 [피어] 블록을 통해 원격 WireGuard 서버를 선언해야 합니다. 아래 이미지에서 Linux 서버 측에서 생성한 구성 파일을 확인할 수 있습니다.



이 네트워크 세그먼트에서 서버의 IP Address "**192.168.110.2**"를 추가하여 `[Interface]` 블록부터 시작하겠습니다. 이렇게 하면



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



다음으로, 세 가지 속성을 가진 '피어' 블록을 선언하여 다음과 같은 구성을 만들어야 합니다:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



사진으로:



![Image](assets/fr/029.webp)



**피어] 블록에 대한 몇 가지 설명:**





- PublicKey**: 와이어가드 데비안 11 서버의 공개 키입니다("*sudo wg*" 명령으로 값을 얻을 수 있습니다)
- 허용된IP**: 이 WireGuard VPN 네트워크를 통해 액세스할 수 있는 IP 주소/서브넷(이 경우 내 WireGuard VPN(*192.168.110.0/24*) 및 원격 LAN(*192.168.100.0/24*) 전용 서브넷)입니다
- 엔드포인트**: 이것은 Debian 11 호스트의 IP Address이며, WireGuard 연결 지점이기 때문입니다(공용 IP Address을 지정해야 합니다)



마지막으로 "**이름**" 필드에 공백 없이 이름을 입력하고 서버에 선언해야 하므로 클라이언트의 공개키를 복사하여 붙여넣습니다. "**등록**"을 클릭합니다.



### C. 와이어가드 서버에서 클라이언트를 선언합니다



이제 Debian 서버로 돌아가서 "**피어**", 즉 Windows PC를 WireGuard 구성에 선언할 차례입니다. 우선, 구성을 수정하기 위해 Interface "wg0"**를 **스토퍼링**해야 합니다:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



그런 다음 이전에 만든 구성 파일을 수정합니다:



```
sudo nano /etc/wireguard/wg0.conf
```



이 파일에서 `[Interface]` 블록 다음에 `[Peer]` 블록을 선언해야 합니다:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



이 [피어] 블록에는 Windows 10 PC의 공개 키(**PublicKey**)와 PC의 Address의 IP Interface(**AllowedIPs**)가 포함되어 있습니다: 서버는 이 WireGuard 터널에서 Windows 클라이언트와만 통신하므로 "**192.168.110.2/32**" 값이 됩니다.



남은 것은 파일을 저장하는 것뿐입니다(*CTRL+O를 누른 다음 Enter를 누른 다음 Nano*를 통해 CTRL+X). Interface "wg0"을 다시 시작합니다:



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



피어 선언이 작동하는지 확인하려면 다음 명령을 사용할 수 있습니다:



```
sudo wg show
```



원격 호스트가 WireGuard 연결을 설정하면 IP Address이 "엔드포인트" 값으로 이동합니다.



![Image](assets/fr/033.webp)



마지막으로 구성 파일을 보호하여 루트 액세스를 제한합니다:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. 첫 번째 WireGuard 연결



이제 구성이 준비되었으므로 Windows PC에서 시작할 수 있습니다. 이렇게 하려면 **WireGuard** 클라이언트에서 **활성화** 버튼을 클릭하세요. 연결이 "끄기"에서 "켜기"로 변경되지만, 그렇다고 해서 작동하는 것은 아닙니다. 이는 모두 구성이 올바른지 여부에 따라 달라집니다. **연결이 설정되면 양쪽에 구성된 Interface WireGuard를 통해 두 시스템이 통신합니다!



![Image](assets/fr/030.webp)



문제가 발생하면 "**로그북**" 탭에서 확인할 수 있습니다. 두 호스트는 연결 상태를 확인하기 위해 정기적으로 Exchange 패킷을 주고받으므로 "*피어 1*에서 킵얼라이브 패킷 수신 중*" 메시지가 표시됩니다.



![Image](assets/fr/031.webp)



WireGuard의 "**저널**" 탭에 아래와 같은 메시지가 표시되면 양쪽에서 선언한 공개 키가 올바른지 확인해야 합니다.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



원격 PC에서 서버 측에 있는 Address WireGuard의 IP Interface과 원격 LAN에 있는 호스트를 핑할 수 있습니다.



![Image](assets/fr/032.webp)



### E. 성능: OpenVPN vs WireGuard



WireGuard VPN에 연결된 원격 PC에서 파일 서버에 액세스하고 [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/)를 통해 파일을 전송하여 전송 속도를 확인할 수 있었습니다. **WireGuard를 사용하면 최대 약 45Mb/s의 속도를 얻을 수 있는데, 와이파이를 사용하고 있기 때문에 매우 좋습니다.**



![Image](assets/fr/025.webp)



동일한 조건에서 이번에는 OpenVPN 연결(UDP)을 통해 동일한 작업을 수행했지만 처리량은 약 3MB/s로 완전히 달라졌습니다. 그 차이는 분명합니다!



![Image](assets/fr/026.webp)



예를 들어 WiFi 연결에서 4G/5G 연결로 전환하는 경우 재연결이 너무 빨라서 끊김이 보이지 않기 때문에 흥미롭습니다.



### F. 보너스: 전체 터널 WireGuard



현재 구성에서는 트래픽의 일부가 VPN을 통해 흐르고 나머지는 인터넷 브라우징을 포함한 고객의 인터넷 연결을 통해 흐릅니다. 모든 트래픽이 VPN 터널을 통과하도록 WireGuard **풀 터널 모드**로 전환하려면 구성을 몇 가지 변경해야 합니다.....



먼저 "resolvconf" 패키지를 설치해야 합니다:



```
sudo apt-get update
sudo apt-get install resolvconf
```



이 작업이 완료되면 Debian 머신에서 "wg0.conf" 프로필을 수정해야 합니다. 즉, Interface를 중지하고 수정한 후 다시 시작해야 합니다.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



다음으로, **[Interface]** 블록에서 사용할 DNS 서버를 추가합니다**. 제 경우에는 실습실의 도메인 컨트롤러를 사용했지만, Debian 머신에 Bind9을 설치하여 로컬 확인자를 사용할 수도 있습니다.



```
DNS = 192.168.100.11
```



파일을 저장한 다음 Interface를 다시 시작합니다:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



마지막으로, Windows 10 워크스테이션의 터널 구성에서 모든 것이 터널을 통과해야 함을 나타내도록 "허용된 IP" 섹션을 수정해야 합니다. 바꾸기:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



작성자:



```
AllowedIPs = 0.0.0.0/0
```



이렇게 하면 "**킬 스위치**" 옵션도 활성화되는 것을 볼 수 있습니다.



![Image](assets/fr/040.webp)



마지막으로 이 전체 터널을 활용하여 소규모 유량 테스트를 수행했으며, 그 결과는 아래와 같습니다:



![Image](assets/fr/039.webp)



WireGuard의 구성은 매우 간단하고 이해하기 쉬우며, 무엇보다도 유지 관리가 쉽습니다. **WireGuard는 VPN의 미래**로 여겨지므로 계속 지켜보는 것이 좋습니다! 또한 성능 측면에서도 상당한 이점을 볼 수 있는데, 이는 OpenVPN에 비해 WireGuard의 큰 장점입니다.



추가 문서:





- [남자 - 명령어](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [남자 - 명령 wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN이 실행 중입니다! 축하합니다!