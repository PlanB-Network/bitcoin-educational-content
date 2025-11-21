---
name: Neutrino
description: LND न्यूट्रिनो स्थापना गाइड
---
![image](assets/cover.webp)


## LND के साथ रास्पबेरी पाई कॉन्फ़िगरेशन


### 1. रास्पबेरी पाई ओएस लाइट डाउनलोड करें


विंडोज, मैक और लिनक्स में माइक्रो एसडी कार्ड पर छवि को डाउनलोड करने और स्थापित करने के निर्देश [इस पृष्ठ](https://www.raspberrypi.org/software/operating-systems/) पर पाए जा सकते हैं।


### 2. एसडी कार्ड को फॉर्मेट करें


रास्पबेरी पाई इमेजर या बैलेनाएचर का उपयोग करें।


**नोट:** `$` प्रतीक का उपयोग एक संकेत के रूप में किया जाता है और यह उपयोगकर्ता को कंप्यूटर में कमांड दर्ज करने की अनुमति देता है, कमांड की व्याख्या लिनक्स में bash द्वारा की जाएगी। किसी पंक्ति की शुरुआत में `#` प्रतीक यह दर्शाता है कि निम्नलिखित पाठ एक टिप्पणी है।


### 3. SSH सक्षम करें


रास्पबेरी पाई को फ़ॉर्मेट की गई मेमोरी के साथ शुरू करने से पहले, हमें इसे कंप्यूटर में डालना होगा और दो फ़ाइलें बनानी होंगी जो हमें दूरस्थ रूप से कनेक्ट करने में सक्षम बनाएँगी। `टच` कमांड का उपयोग करके, हम /boot पार्टीशन में एक खाली फ़ाइल बनाते हैं, जिससे नए फ़ॉर्मेट किए गए SD कार्ड के पहले बूट पर SSH कनेक्शन सक्षम हो जाता है।


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. वाई-फाई कनेक्शन के लिए फ़ाइल बनाएँ


नैनो कमांड का इस्तेमाल करके हम `wpa_supplicant.conf` फ़ाइल बनाते हैं और सीधे उसे एडिट करना शुरू करते हैं। इस फ़ाइल में, हमें वाई-फ़ाई कॉन्फ़िगरेशन कॉपी करना होगा, START और END के बीच के टेक्स्ट को कॉपी करना होगा, और उस वाई-फ़ाई का SSID और पासवर्ड बदलना होगा जिससे आप कनेक्ट करना चाहते हैं।


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


### 5. कनेक्शन


फिर, हम एसडी कार्ड को रास्पबेरी पाई में डालते हैं और ऑपरेटिंग सिस्टम शुरू करने के लिए पाई को पावर स्रोत से जोड़ते हैं। हमें इसे नेटवर्क पर पहचानना होगा, और mDNS प्रोटोकॉल संभवतः इसे raspberrypi.local नाम देगा। आइए SSH के माध्यम से कनेक्ट करने का प्रयास करें।


```
$ ssh pi@raspberrypi.local
password: raspberry
```


अगर यह काम नहीं करता है, तो हमें नेटवर्क का पता लगाना होगा। आइए उस IP Address का पता लगाएँ जिससे हम जुड़े हैं।


```
$ ifconfig
```


उदाहरण के लिए, यदि यह 192.168.0.0 है, तो Pi को खोजने के लिए nmap का उपयोग करें।


```
nmap -v 192.168.0.0/24
```


मान लें कि हमें अपने नेटवर्क पर एक नया आईपी मिल गया है, तो आइए SSH के माध्यम से प्रवेश करें।


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Pi को कॉन्फ़िगर करें


```
$ sudo raspi-config
```


- विकल्प (1) का चयन करें और उपयोगकर्ता pi के लिए पासवर्ड बदलें।
- हम कॉन्फ़िगरेशन टूल को नवीनतम संस्करण में अपडेट करने के लिए विकल्प (8) का चयन करते हैं
- हम अपना समय क्षेत्र चुनने के लिए विकल्प (4) चुनते हैं
- हम विकल्प (7) का चयन करते हैं और फिर फाइल सिस्टम का विस्तार करते हैं
- खत्म करना


### 7. अब OS अपडेट करें


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Bitcoin उपयोगकर्ता जोड़ें


```
$ sudo adduser bitcoin
```


### 9. आरपीआई को सुरक्षित करें


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


### 10. गो इंस्टॉल करें


यदि आप रास्पबेरी पाई का उपयोग नहीं कर रहे हैं, तो अपने आर्किटेक्चर के लिए [यहां](https://golang.org/dl/) डाउनलोड करें।


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. LND संकलित और स्थापित करें


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


### 12. LND conf फ़ाइल बनाएँ


LND कॉन्फ़िगरेशन फ़ाइल बनाएँ, यह 'Bitcoin' उपयोगकर्ता के साथ किया जाना चाहिए


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


### 13. LND सेवा ऑटोस्टार्ट


RPI बूट के बाद LND को शुरू करने के लिए, हमें systemd में .service फ़ाइल बनानी होगी। अगर हम Bitcoin उपयोगकर्ता के रूप में लॉग इन हैं और वापस pi उपयोगकर्ता पर स्विच करना चाहते हैं, तो हम बस 'exit' टाइप करते हैं।


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


हम journalctl कमांड चलाकर लॉग देख सकते हैं


```
$ sudo journalctl -f -u lnd
```


### 14. अब हम LND शुरू करते हैं


```
$ sudo su - bitcoin
$ lncli create
```


### 15. नोड में धन जोड़ें


```
$ lncli newaddress p2wkh
```

अब आप LND द्वारा लौटाए गए Address को btc भेज सकते हैं।


इस कमांड से आप शेष राशि की जांच कर सकते हैं:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


लेन-देन की पुष्टि हो जाने के बाद, हम एक चैनल खोल सकते हैं। अगर आपको नहीं पता कि चैनल किस नोड से खोलना है, तो आप 1ml.com पर जाकर एक नोड चुन सकते हैं।


किसी नोड से कनेक्शन खोलें:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


फिर एक चैनल खोलें:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


हमारे फंड की जांच करें:


```
$ lncli walletbalance
$ lncli channelbalance
```


हम लंबित और सक्रिय चैनल देख सकते हैं:


```
$ lncli pendingchannels
$ lncli listchannels
```


लाइटनिंग Invoice का भुगतान करने के लिए:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


भुगतान प्राप्त करने के लिए, किसी विशिष्ट राशि के लिए Invoice बनाएं:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


मेरे नोड के बारे में जानकारी देखने के लिए:


```
$ lncli getinfo
```


कमांडों की पूरी सूची केवल lncli कमांड चलाकर देखी जा सकती है:


```
$ lncli
```


अंत में, LND API पर कॉल करने के लिए:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


गाइड का अंत!