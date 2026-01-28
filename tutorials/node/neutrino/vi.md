---
name: Neutrino
description: Hướng dẫn lắp đặt LND Neutrino
---
![image](assets/cover.webp)


## Cấu hình Raspberry Pi với LND


### 1. Tải xuống Raspberry Pi OS Lite


Bạn có thể tìm thấy hướng dẫn tải xuống và cài đặt hình ảnh trên thẻ nhớ micro SD trên Windows, Mac và Linux trên [trang này](https://www.raspberrypi.org/software/operating-systems/).


### 2. Định dạng thẻ SD


Sử dụng Raspberry Pi Imager hoặc balenaEtcher.


**Lưu ý:** Ký hiệu `$` được dùng làm dấu nhắc và cho phép người dùng nhập lệnh vào máy tính. Các lệnh sẽ được bash trên Linux diễn giải. Ký hiệu `#` ở đầu dòng cho biết đoạn văn bản sau là chú thích.


### 3. Bật SSH


Trước khi khởi động Raspberry Pi với bộ nhớ đã được định dạng, chúng ta phải lắp nó vào máy tính và tạo hai tệp cho phép kết nối từ xa. Sử dụng lệnh `touch`, chúng ta tạo một tệp trống trong phân vùng /boot, cho phép kết nối SSH khi khởi động lần đầu thẻ SD mới được định dạng.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Tạo tệp cho kết nối Wi-Fi


Sử dụng lệnh nano, chúng ta tạo tệp `wpa_supplicant.conf` và bắt đầu chỉnh sửa trực tiếp. Trong tệp này, chúng ta cần sao chép cấu hình wifi, sao chép văn bản giữa START và END, và sửa đổi SSID và mật khẩu của wifi bạn muốn kết nối.


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


### 5. Kết nối


Sau đó, chúng ta lắp thẻ SD vào Raspberry Pi và kết nối Pi với nguồn điện để khởi động hệ điều hành. Chúng ta cần xác định nó trên mạng và giao thức mDNS có thể sẽ gán tên raspberrypi.local cho nó. Hãy thử kết nối qua SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Nếu không được, chúng ta cần tìm mạng. Hãy tìm IP Address mà chúng ta đang kết nối.


```
$ ifconfig
```


Ví dụ, nếu là 192.168.0.0, hãy sử dụng nmap để tìm Pi.


```
nmap -v 192.168.0.0/24
```


Giả sử chúng ta tìm thấy một IP mới trên mạng của mình, hãy truy cập qua SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Cấu hình Pi


```
$ sudo raspi-config
```


- Chọn tùy chọn (1) và thay đổi mật khẩu cho người dùng pi.
- Chúng tôi chọn tùy chọn (8) để cập nhật công cụ cấu hình lên phiên bản mới nhất
- Chúng tôi chọn tùy chọn (4) để chọn múi giờ của chúng tôi
- Chúng tôi chọn tùy chọn (7) và sau đó Mở rộng hệ thống tập tin
- Hoàn thành


### 7. Bây giờ hãy cập nhật hệ điều hành


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Thêm người dùng Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Bảo mật rpi


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


### 10. Cài đặt Go


Nếu bạn không sử dụng Raspberry Pi, hãy tải xuống Go cho kiến trúc của bạn [tại đây](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Biên dịch và cài đặt LND


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


### 12. Tạo tệp cấu hình LND


Tạo tệp cấu hình LND, việc này phải được thực hiện bằng người dùng 'Bitcoin'


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


### 13. Tự động khởi động dịch vụ LND


Để khởi động LND sau khi khởi động RPI, chúng ta phải tạo tệp .service trong systemd. Nếu chúng ta đang đăng nhập với tư cách người dùng Bitcoin và muốn chuyển về người dùng Pi, chỉ cần nhập 'exit'.


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


Chúng ta có thể xem nhật ký bằng cách chạy lệnh journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Bây giờ chúng ta bắt đầu LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Thêm tiền vào nút


```
$ lncli newaddress p2wkh
```

Bây giờ bạn có thể gửi btc đến Address được trả về bởi LND.


với lệnh này, bạn có thể kiểm tra số dư:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Sau khi giao dịch được xác nhận, chúng ta có thể mở kênh. Nếu bạn không biết nên mở kênh bằng node nào, bạn có thể truy cập 1ml.com và chọn một node.


Mở kết nối tới một nút:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Sau đó mở một kênh:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Kiểm tra quỹ của chúng tôi:


```
$ lncli walletbalance
$ lncli channelbalance
```


Chúng ta có thể xem các kênh đang chờ xử lý và đang hoạt động:


```
$ lncli pendingchannels
$ lncli listchannels
```


Để trả tiền cho Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Để nhận thanh toán, hãy tạo Invoice với số tiền cụ thể:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Để xem thông tin về nút của tôi:


```
$ lncli getinfo
```


Bạn có thể xem danh sách lệnh đầy đủ bằng cách chạy lệnh lncli:


```
$ lncli
```


Cuối cùng, để thực hiện lệnh gọi tới API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


HẾT hướng dẫn!