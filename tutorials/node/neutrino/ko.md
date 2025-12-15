---
name: Neutrino
description: LND 중성미자 설치 가이드
---
![image](assets/cover.webp)


## LND을 사용한 라즈베리 파이 구성


### 1. 라즈베리 파이 OS Lite 다운로드


Windows, Mac 및 Linux에서 마이크로 SD 카드에 이미지를 다운로드하고 설치하는 방법은 [이 페이지](https://www.raspberrypi.org/software/operating-systems/)에서 확인할 수 있습니다.


### 2. SD 카드 포맷


라즈베리 파이 이미저 또는 발레나에처를 사용합니다.


**참고: `$` 기호는 프롬프트로 사용되며 사용자가 컴퓨터에 명령을 입력할 수 있도록 하며, 명령은 Linux에서 bash로 해석됩니다. 한 줄의 시작 부분에 있는 기호 `#`은 다음 텍스트가 주석임을 나타냅니다.


### 3. SSH 사용


포맷된 메모리로 라즈베리 파이를 시작하기 전에 컴퓨터에 삽입하고 원격으로 연결할 수 있는 두 개의 파일을 만들어야 합니다. 터치` 명령을 사용하여 /boot 파티션에 빈 파일을 생성하여 새로 포맷한 SD 카드를 처음 부팅할 때 SSH 연결을 활성화합니다.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Wi-Fi 연결용 파일 만들기


Nano 명령을 사용해 `wpa_supplicant.conf` 파일을 생성하고 직접 편집을 시작합니다. 이 파일에서 와이파이 구성을 복사하고, 시작과 끝 사이에 텍스트를 복사하고, 연결하려는 와이파이의 SSID와 비밀번호를 수정해야 합니다.


```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
ssid="MyNetworkSSID"
psk="password"
}
------ END -------
```


### 5. 연결


그런 다음 SD 카드를 라즈베리 파이에 삽입하고 파이를 전원에 연결하여 운영 체제를 시작합니다. 네트워크에서 이를 식별해야 하며, mDNS 프로토콜은 raspberrypi.local이라는 이름을 할당할 것입니다. SSH를 통해 연결해 보겠습니다.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


작동하지 않으면 네트워크를 찾아야 합니다. 우리가 연결된 IP Address를 찾아보겠습니다.


```
$ ifconfig
```


예를 들어 192.168.0.0인 경우 nmap을 사용하여 파이를 찾습니다.


```
nmap -v 192.168.0.0/24
```


네트워크에서 새 IP를 찾았다고 가정하고 SSH를 통해 들어가 보겠습니다.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Pi 구성


```
$ sudo raspi-config
```


- 옵션(1)을 선택하고 사용자 pi의 비밀번호를 변경합니다.
- 옵션 (8)을 선택하여 구성 도구를 최신 버전으로 업데이트합니다
- 옵션 (4)를 선택하여 시간대를 선택합니다
- 옵션 (7)을 선택한 다음 파일 시스템 확장
- 완료


### 7. 이제 OS를 업데이트하세요


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Bitcoin 사용자 추가


```
$ sudo adduser bitcoin
```


### 9. RPI 보안


```
$ sudo apt install ufw
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'allow SSH from LAN'
$ sudo ufw allow 9735 comment 'allow Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```


### 10. Go 설치


라즈베리 파이를 사용하지 않는 경우 아키텍처를 위한 Go를 다운로드하세요[여기](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. LND 컴파일 및 설치


```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli version 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```


### 12. LND conf 파일 생성


LND 구성 파일을 생성하며, 이 작업은 'Bitcoin' 사용자로 수행해야 합니다


```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```


```
[Application Options]
# enable spontaneous payments
accept-keysend=1

# Public name of the node
alias=YOUR_ALIAS
# Public color in hexadecimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```


### 13. LND 서비스 자동 시작


Rpi 부팅 후 LND을 시작하려면 systemd에 .service 파일을 생성해야 합니다. Bitcoin 사용자로 로그인한 상태에서 파이 사용자로 다시 전환하려면 'exit'를 입력하기만 하면 됩니다


```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```


```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Service execution
###################

ExecStart=/usr/local/bin/lnd


# Process management
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Directory creation and permissions
####################################

# Run as bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```


```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```


Journalctl 명령을 실행하여 로그를 볼 수 있습니다


```
$ sudo journalctl -f -u lnd
```


### 14. 이제 LND을 시작합니다


```
$ sudo su - bitcoin
$ lncli create
```


### 15. 노드에 자금 추가


```
$ lncli newaddress p2wkh
```

이제 LND이 반환한 Address로 비트코인을 보낼 수 있습니다.


이 명령으로 잔액을 확인할 수 있습니다:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


트랜잭션이 확인되면 채널을 개설할 수 있습니다. 채널을 개설할 노드를 모르는 경우 1ml.com으로 이동하여 노드를 선택할 수 있습니다.


노드에 대한 연결을 엽니다:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


그런 다음 채널을 엽니다:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


자금을 확인하세요:


```
$ lncli walletbalance
$ lncli channelbalance
```


보류 중인 채널과 활성 채널을 볼 수 있습니다:


```
$ lncli pendingchannels
$ lncli listchannels
```


번개 Invoice를 지불하려면:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


결제를 받으려면 특정 금액에 대한 Invoice를 생성하세요:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


내 노드에 대한 정보를 보려면 다음과 같이 하세요:


```
$ lncli getinfo
```


전체 명령어 목록은 lncli 명령을 실행하기만 하면 확인할 수 있습니다:


```
$ lncli
```


마지막으로 LND API를 호출합니다:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


가이드 끝!