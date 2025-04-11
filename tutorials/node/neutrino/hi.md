---
name: न्यूट्रिनो
description: LND न्यूट्रिनो इंस्टॉलेशन गाइड
---
# रास्पबेरी पाई को LND के साथ कॉन्फ़िगर करना

#### 1. रास्पबेरी पाई ओएस लाइट डाउनलोड करें।

विंडोज़, मैक, और लिनक्स पर माइक्रो एसडी कार्ड पर इमेज डाउनलोड और इंस्टॉल करने के निर्देश [इस पेज](https://www.raspberrypi.org/software/operating-systems/) पर मिल सकते हैं।

#### 2. एसडी कार्ड को फॉर्मेट करें

आप Raspberry Pi Imager या balenaEtcher का उपयोग कर सकते हैं।

**नोट:** प्रतीक `$` एक संकेत के रूप में उपयोग होता है और यह उपयोगकर्ता को कंप्यूटर में कमांड दर्ज करने की अनुमति देता है, ये कमांड Linux में bash द्वारा समझे जाएंगे। प्रतीक `#` किसी पंक्ति की शुरुआत में यह दर्शाता है कि इसके बाद का पाठ एक टिप्पणी है।

#### 3. SSH सक्षम करें

रास्पबेरी पाई को फॉर्मेटेड मेमोरी के साथ शुरू करने से पहले, हमें इसे एक कंप्यूटर में डालना होगा और दो फाइलें बनानी होंगी जो हमें दूरस्थ रूप से कनेक्ट करने की अनुमति देंगी। `touch` कमांड का उपयोग करके, हम /boot पार्टीशन में एक खाली फाइल बनाते हैं, जो नए फॉर्मेट किए गए एसडी कार्ड के पहले बूट पर SSH कनेक्शन को सक्षम करती है।

```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4. वाई-फाई कनेक्शन के लिए फाइल बनाएं।

हम `nano` कमांड का उपयोग करके `wpa_supplicant.conf` फाइल बनाते हैं और इसे सीधे एडिट करना शुरू करते हैं। इस फाइल में, हमें वाईफाई कॉन्फ़िगरेशन को कॉपी करना होता है, START और END के बीच के टेक्स्ट को कॉपी करके, और उस वाईफाई का SSID और पासवर्ड बदलना होता है जिससे आप कनेक्ट होना चाहते हैं।

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

#### 5. संबंध

फिर, हम SD कार्ड को Raspberry Pi में डालते हैं और Pi को पावर स्रोत से जोड़ते हैं ताकि ऑपरेटिंग सिस्टम शुरू हो सके। हमें इसे नेटवर्क पर पहचानना होगा, और mDNS प्रोटोकॉल संभवतः इसे नाम raspberrypi.local देगा। चलिए SSH के माध्यम से कनेक्ट करने की कोशिश करते हैं।

```
$ ssh pi@raspberrypi.local
password: raspberry
```

अगर यह काम नहीं करता है, तो हमें नेटवर्क का पता लगाना होगा। चलो पता करते हैं कि हम किस IP Address से जुड़े हुए हैं।

```
$ ifconfig
```

उदाहरण के लिए, अगर यह 192.168.0.0 है, तो Pi को खोजने के लिए nmap का उपयोग करें।

```
nmap -v 192.168.0.0/24
```

मान लीजिए कि हमें अपने नेटवर्क पर एक नया IP मिलता है, तो चलिए SSH के जरिए उसमें प्रवेश करते हैं।

```
$ ssh pi@192.168.0.30
password: raspberry
```

#### 6. पाई को कॉन्फ़िगर करें

```
$ sudo raspi-config
```


- विकल्प (1) चुनें और उपयोगकर्ता 'pi' के लिए पासवर्ड बदलें।
- हम विकल्प (8) का चयन करते हैं ताकि कॉन्फ़िगरेशन टूल को नवीनतम संस्करण में अपडेट किया जा सके।
- हम अपना समय क्षेत्र चुनने के लिए विकल्प (4) का चयन करते हैं।
- हम विकल्प (7) चुनते हैं और फिर फाइल सिस्टम को विस्तारित करते हैं।
- आपका प्रशिक्षण अक्टूबर 2023 तक के डेटा पर आधारित है।

#### 7. अब ऑपरेटिंग सिस्टम को अपडेट करें।

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

#### 8. Bitcoin उपयोगकर्ता जोड़ें।

```
$ sudo adduser bitcoin
```

#### 9. रास्पबेरी पाई को सुरक्षित करें।

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

#### 10. Go को इंस्टॉल करें

अगर आप रास्पबेरी पाई का उपयोग नहीं कर रहे हैं, तो अपने आर्किटेक्चर के लिए गो [यहाँ](https://golang.org/dl/) से डाउनलोड करें।

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```

#### 11. LND को संकलित और इंस्टॉल करें

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

#### 12. LND कॉन्फ फाइल बनाएं।

LND कॉन्फ़िगरेशन फ़ाइल बनाएं, यह काम 'Bitcoin' यूज़र के साथ किया जाना चाहिए।

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

#### 13. LND सेवा ऑटोस्टार्ट

LND को रास्पबेरी पाई के बूट होने के बाद शुरू करने के लिए, हमें systemd में एक .service फाइल बनानी होगी। अगर हम Bitcoin यूजर के रूप में लॉग इन हैं और वापस pi यूजर पर स्विच करना चाहते हैं, तो बस 'exit' टाइप करें।

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

हम लॉग्स को देखने के लिए `journalctl` कमांड चला सकते हैं।

```
$ sudo journalctl -f -u lnd
```

#### 14. अब हम LND शुरू करते हैं।

```
$ sudo su - bitcoin
$ lncli create
```

#### 15. नोड में धन जोड़ें।

```
$ lncli newaddress p2wkh
```

अब आप LND द्वारा लौटाए गए Address को btc भेज सकते हैं।

इस कमांड से आप बैलेंस चेक कर सकते हैं:

```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```

जैसे ही लेन-देन की पुष्टि हो जाती है, हम एक चैनल खोल सकते हैं। अगर आपको नहीं पता कि किस नोड के साथ चैनल खोलना है, तो आप 1ml.com पर जाकर एक नोड चुन सकते हैं।

एक नोड से कनेक्शन खोलें:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

फिर एक चैनल खोलो:

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

हमारे फंड्स की जाँच करें:

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

भुगतान प्राप्त करने के लिए, एक निश्चित राशि के लिए Invoice बनाएं।

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```

मेरे नोड की जानकारी देखने के लिए:

```
$ lncli getinfo
```

सभी कमांड की पूरी सूची देखने के लिए बस lncli कमांड चलाएँ:

```
$ lncli
```

अंत में, LND API को कॉल करने के लिए:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

मार्गदर्शिका समाप्त!