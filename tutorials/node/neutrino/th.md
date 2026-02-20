---
name: Neutrino
description: คู่มือการติดตั้ง LND Neutrino
---
![image](assets/cover.webp)


## การกำหนดค่า Raspberry Pi กับ LND


### 1. ดาวน์โหลด Raspberry Pi OS Lite


คำแนะนำสำหรับการดาวน์โหลดและติดตั้งภาพบนการ์ด micro SD ใน Windows, Mac และ Linux สามารถพบได้ที่ [หน้านี้](https://www.raspberrypi.org/software/operating-systems/).


### 2. ฟอร์แมตการ์ด SD


ใช้ Raspberry Pi Imager หรือ balenaEtcher.


**หมายเหตุ:** สัญลักษณ์ `$` ใช้เป็นพรอมต์และอนุญาตให้ผู้ใช้ป้อนคำสั่งลงในคอมพิวเตอร์ คำสั่งจะถูกตีความโดย bash ใน Linux สัญลักษณ์ `#` ที่จุดเริ่มต้นของบรรทัดบ่งบอกว่าข้อความต่อไปนี้เป็นความคิดเห็น


### 3. เปิดใช้งาน SSH


ก่อนเริ่มต้น Raspberry Pi ด้วยหน่วยความจำที่ฟอร์แมตแล้ว เราต้องใส่มันเข้าไปในคอมพิวเตอร์และสร้างไฟล์สองไฟล์ที่จะช่วยให้เราสามารถเชื่อมต่อจากระยะไกลได้ โดยใช้คำสั่ง `touch` เราสร้างไฟล์ว่างในพาร์ติชัน /boot เพื่อเปิดใช้งานการเชื่อมต่อ SSH ในการบูตครั้งแรกของ SD card ที่เพิ่งฟอร์แมตใหม่


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. สร้างไฟล์สำหรับการเชื่อมต่อ Wi-Fi


โดยใช้คำสั่ง nano เราสร้างไฟล์ `wpa_supplicant.conf` และเริ่มแก้ไขโดยตรง ในไฟล์นี้ เราจำเป็นต้องคัดลอกการตั้งค่า wifi โดยคัดลอกข้อความระหว่าง START และ END และแก้ไข SSID และรหัสผ่านของ wifi ที่คุณต้องการเชื่อมต่อ


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


### 5. การเชื่อมต่อ


จากนั้น เราใส่การ์ด SD ลงใน Raspberry Pi และเชื่อมต่อ Pi กับแหล่งจ่ายไฟเพื่อเริ่มระบบปฏิบัติการ เราจำเป็นต้องระบุอุปกรณ์บนเครือข่าย และโปรโตคอล mDNS จะกำหนดชื่อ raspberrypi.local ให้กับมัน ลองเชื่อมต่อผ่าน SSH กันเถอะ


```
$ ssh pi@raspberrypi.local
password: raspberry
```


หากมันไม่ทำงาน เราจำเป็นต้องหาว่าเครือข่ายคืออะไร มาหา IP address ที่เราเชื่อมต่อกันเถอะ


```
$ ifconfig
```


ตัวอย่างเช่น ถ้าเป็น 192.168.0.0 ให้ใช้ nmap เพื่อค้นหา Pi.


```
nmap -v 192.168.0.0/24
```


สมมติว่าเราพบ IP ใหม่บนเครือข่ายของเรา ให้เข้าสู่ระบบผ่าน SSH


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. กำหนดค่า Pi


```
$ sudo raspi-config
```


- เลือกตัวเลือก (1) และเปลี่ยนรหัสผ่านสำหรับผู้ใช้ pi.
- เราเลือกตัวเลือก (8) เพื่ออัปเดตเครื่องมือกำหนดค่าเป็นเวอร์ชันล่าสุด
- เราเลือกตัวเลือก (4) เพื่อเลือกเขตเวลาของเรา
- เราเลือกตัวเลือก (7) และจากนั้นขยายระบบไฟล์
- เสร็จสิ้น


### 7. ตอนนี้อัปเดตระบบปฏิบัติการ


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. เพิ่มผู้ใช้บิตคอยน์


```
$ sudo adduser bitcoin
```


### 9. รักษาความปลอดภัย rpi


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


### 10. ติดตั้ง Go


หากคุณไม่ได้ใช้ Raspberry Pi ให้ดาวน์โหลด Go สำหรับสถาปัตยกรรมของคุณ [ที่นี่](https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. คอมไพล์และติดตั้ง LND


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


### 12. สร้างไฟล์ lnd conf


สร้างไฟล์การกำหนดค่า lnd โดยใช้ผู้ใช้ 'bitcoin'


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


### 13. การเริ่มต้นอัตโนมัติของบริการ LND


ในการทำให้ LND เริ่มทำงานหลังจาก rpi บูต เราต้องสร้างไฟล์ .service ใน systemd หากเราเข้าสู่ระบบในฐานะผู้ใช้ bitcoin และต้องการสลับกลับไปยังผู้ใช้ pi เราเพียงแค่พิมพ์ 'exit'


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


เราสามารถดูบันทึกได้โดยการรันคำสั่ง journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. ตอนนี้เราเริ่ม LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. เพิ่มเงินทุนให้กับโหนด


```
$ lncli newaddress p2wkh
```

คุณสามารถส่ง btc ไปยังที่อยู่ที่ส่งคืนโดย LND ได้แล้ว


ด้วยคำสั่งนี้ คุณสามารถตรวจสอบยอดเงินได้:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


เมื่อการทำธุรกรรมได้รับการยืนยันแล้ว เราสามารถเปิดช่องทางได้ หากคุณไม่ทราบว่าจะเปิดช่องทางกับโหนดใด คุณสามารถไปที่ 1ml.com และเลือกโหนดได้


เปิดการเชื่อมต่อไปยังโหนด:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


จากนั้นเปิดช่อง:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


ตรวจสอบกองทุนของเรา:


```
$ lncli walletbalance
$ lncli channelbalance
```


เราสามารถดูช่องที่รอดำเนินการและช่องที่ใช้งานอยู่:


```
$ lncli pendingchannels
$ lncli listchannels
```


ในการชำระใบแจ้งหนี้ Lightning:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


ในการรับชำระเงิน ให้สร้างใบแจ้งหนี้สำหรับจำนวนเงินที่ระบุ:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


เพื่อดูข้อมูลเกี่ยวกับโหนดของฉัน:


```
$ lncli getinfo
```


รายการคำสั่งทั้งหมดสามารถดูได้โดยการรันคำสั่ง lncli:


```
$ lncli
```


สุดท้ายนี้ เพื่อโทรออกไปยัง LND API:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


สิ้นสุดคู่มือ!