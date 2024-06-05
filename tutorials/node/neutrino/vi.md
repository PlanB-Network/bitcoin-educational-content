---
name: Neutrino
description: Hướng dẫn cài đặt LND Neutrino
---

# Cấu hình Raspberry Pi với LND

1. Tải Raspberry Pi OS Lite

Tải Raspberry Pi OS Lite, hướng dẫn tải và cài đặt hình ảnh lên thẻ micro SD trên Windows, Mac và Linux có thể tìm thấy trên [trang này](https://www.raspberrypi.org/software/operating-systems/).

2. Định dạng thẻ SD

Định dạng thẻ SD sử dụng Raspberry Pi Imager hoặc balenaEtcher.

> LƯU Ý: Ký hiệu `$` được sử dụng như một dấu nhắc và cho phép người dùng nhập lệnh vào máy tính, các lệnh sẽ được bash trong Linux giải thích. Ký hiệu `#` ở đầu dòng chỉ ra rằng văn bản sau đó là một bình luận.

3. Kích hoạt SSH

Trước khi khởi động Raspberry Pi với bộ nhớ đã được định dạng, chúng ta phải chèn nó vào máy tính và tạo hai tệp sẽ cho phép chúng ta kết nối từ xa. Sử dụng lệnh `touch`, chúng ta tạo một tệp trống trong phân vùng /boot, kích hoạt kết nối SSH trong lần khởi động đầu tiên của thẻ SD mới được định dạng.

```
# LƯU Ý: Nếu thẻ microSD đã được gắn vào /media/microSD, lệnh
# nên là $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Sử dụng lệnh nano

chúng ta tạo tệp wpa_supplicant.conf và bắt đầu chỉnh sửa trực tiếp. Trong tệp này, chúng ta cần sao chép cấu hình wifi, sao chép văn bản giữa START và END, và chỉnh sửa SSID và mật khẩu của wifi mà bạn muốn kết nối.

```
$ nano /boot/wpa_supplicant.conf

------ BẮT ĐẦU -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ KẾT THÚC -------
```

5. Kết nối

Sau đó, chúng ta chèn thẻ SD vào Raspberry Pi và kết nối Pi với nguồn điện để khởi động hệ điều hành. Chúng ta cần xác định nó trên mạng, và giao thức mDNS có khả năng gán tên raspberrypi.local cho nó. Hãy thử kết nối qua SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Nếu không thành công, chúng ta cần tìm ra mạng. Hãy tìm địa chỉ IP mà chúng ta đang kết nối.

```
$ ifconfig
```

Ví dụ, nếu nó là 192.168.0.0, sử dụng nmap để tìm Pi.

```
nmap -v 192.168.0.0/24
```

Giả sử chúng ta tìm thấy một IP mới trên mạng của mình, hãy nhập qua SSH.

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. Cấu hình Pi

```
$ sudo raspi-config
```

- Chọn tùy chọn (1) và thay đổi mật khẩu cho người dùng pi.
- Chúng ta chọn tùy chọn (8) để cập nhật công cụ cấu hình lên phiên bản mới nhất
- Chúng ta chọn tùy chọn (4) để chọn múi giờ của mình
- Chúng ta chọn tùy chọn (7) và sau đó mở rộng hệ thống tệp
- Hoàn thành

  7.- Chúng ta cập nhật OS

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Chúng ta thêm người dùng bitcoin

```
$ sudo adduser bitcoin
```

9.- Chúng ta bảo vệ rpi

```
$ sudo apt install ufw
```
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'cho phép SSH từ LAN'
$ sudo ufw allow 9735 comment 'cho phép Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- Chúng tôi cài đặt go: nếu bạn không sử dụng raspberry pi, tải go cho kiến trúc của bạn tại đây (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # sẽ hiển thị thông điệp sau 'go version go1.13.5 linux/arm'
```

11.- Chúng tôi biên dịch và cài đặt lnd

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

12.- Chúng tôi tạo tệp cấu hình lnd, điều này nên được thực hiện với người dùng 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# kích hoạt thanh toán tự phát
accept-keysend=1

# Tên công khai của nút
alias=TÊN_BIỆT_DANH_CỦA_BẠN
# Màu công khai dưới dạng mã thập lục phân
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# socket gRPC
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Để LND khởi động sau khi rpi khởi động, chúng tôi phải tạo tệp .service trong systemd.
Nếu chúng tôi đang đăng nhập với tư cách là người dùng bitcoin và muốn chuyển lại sang người dùng pi, chúng tôi chỉ cần gõ 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Thực thi dịch vụ
###################

ExecStart=/usr/local/bin/lnd


# Quản lý quy trình
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Tạo thư mục và quyền
####################################

# Chạy với tư cách bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Biện pháp tăng cường bảo mật
####################

# Cung cấp một /tmp và /var/tmp riêng tư.
```
PrivateTmp=true
# Gắn kết /usr, /boot/ và /etc ở chế độ chỉ đọc cho quá trình.
ProtectSystem=full

# Không cho phép quá trình và tất cả các tiến trình con của nó
# có được quyền lợi mới thông qua execve().
NoNewPrivileges=true

# Sử dụng một namespace /dev mới chỉ bao gồm các thiết bị giả API
# như /dev/null, /dev/zero và /dev/random.
PrivateDevices=true

# Từ chối việc tạo các ánh xạ bộ nhớ có thể ghi và thực thi.
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

14. Bây giờ chúng ta bắt đầu lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Thêm tiền vào node của chúng ta

```
$ lncli newaddress p2wkh
```

Gửi btc đến địa chỉ được lnd trả về

Để kiểm tra số dư

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Một khi giao dịch đã được xác nhận, chúng ta có thể mở một kênh. Nếu bạn không biết mở kênh với node nào, bạn có thể truy cập 1ml.com và chọn một node.

Mở kết nối đến một node:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Sau đó mở một kênh

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Kiểm tra số dư của chúng ta

```
$ lncli walletbalance
$ lncli channelbalance
```

Chúng ta có thể xem các kênh đang chờ và kênh hoạt động

```
$ lncli pendingchannels
$ lncli listchannels
```

Để thanh toán một hóa đơn lightning

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Để nhận một khoản thanh toán, tạo một hóa đơn cho một số tiền cụ thể

```
$ lncli addinvoice --memo 'khoản thanh toán đầu tiên của tôi trên LN' --amt 100
```

Để xem thông tin về node của tôi

```
$ lncli getinfo
```

Danh sách đầy đủ các lệnh có thể được xem bằng cách đơn giản chạy lncli

```
$ lncli
```

Cuối cùng, để thực hiện các cuộc gọi đến API lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> KẾT THÚC