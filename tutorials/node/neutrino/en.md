---
name: Neutrino
description: LND Neutrino Installation Guide
---

# Raspberry Pi Configuration with LND

#### 1. Download Raspberry Pi OS Lite
The instructions for downloading and installing the image on a micro SD card in Windows, Mac, and Linux can be found on [this page](https://www.raspberrypi.org/software/operating-systems/).

#### 2. Format the SD Card
use Raspberry Pi Imager or balenaEtcher.

**Note:** The symbol `$` is used as a prompt and allows the user to enter commands into the computer, the commands will be interpreted by bash in Linux. The symbol `#` at the beginning of a line indicates that the following text is a comment.

#### 3. Enable SSH

Before starting the Raspberry Pi with the formatted memory, we must insert it into a computer and create two files that will allow us to connect remotely. Using the `touch` command, we create an empty file in the /boot partition, enabling SSH connection on the first boot of the freshly formatted SD card.

```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```
#### 4. Create file for Wi-Fi connection
Using the nano command we create the `wpa_supplicant.conf` file and directly start editing it. In this file, we need to copy the wifi configuration, copying the text between START and END, and modifying the SSID and password of the wifi you want to connect to.

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

#### 5. Connection
Then, we insert the SD card into the Raspberry Pi and connect the Pi to the power source to start the operating system. We need to identify it on the network, and the mDNS protocol will likely assign the name raspberrypi.local to it. Let's try to connect via SSH.
```
$ ssh pi@raspberrypi.local
password: raspberry
```
If it doesn't work, we need to find out the network. Let's find out the IP address we are connected to.
	
```
$ ifconfig
```
	
For example, if it is 192.168.0.0, use nmap to find the Pi.

```
nmap -v 192.168.0.0/24
```
	
Assuming we find a new IP on our network, let's enter via SSH.
	
```
$ ssh pi@192.168.0.30
password: raspberry
```
	
#### 6. Configure the Pi
```
$ sudo raspi-config
```
- Select option (1) and change the password for the user pi.
- We select option (8) to update the configuration tool to the latest version
- We select option (4) to select our time zone
- We select option (7) and then Expand filesystem
- Finish

#### 7. Now update the OS
```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

#### 8. Add the bitcoin user
```
$ sudo adduser bitcoin
```

#### 9. Secure the rpi

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

#### 10. Install Go
If you are not using a raspberry pi, download go for your architecture [here](https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```

#### 11. Compile and install LND

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

#### 12. Create lnd conf file
Create the lnd configuration file, this should be done with the 'bitcoin' user

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

#### 13. LND service autostart
To make LND start after rpi boot, we must create the .service file in systemd. If we are logged in as a bitcoin user and want to switch back to the pi user, we simply type 'exit'

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

We can view the logs by running the command journalctl

```
$ sudo journalctl -f -u lnd
```

#### 14. Now we start LND

```
$ sudo su - bitcoin
$ lncli create
```

#### 15. Add funds to the node

```
$ lncli newaddress p2wkh
```
You can now send btc to the address returned by LND.

with this command, you can check the balance:

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Once the transaction has been confirmed, we can open a channel. If you don't know which node to open the channel with, you can go to 1ml.com and choose a node.

Open a connection to a node:
```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Then open a channel:
```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Check our funds:
```
$ lncli walletbalance
$ lncli channelbalance
```

We can view the pending and active channels:
```
$ lncli pendingchannels
$ lncli listchannels
```

To pay a lightning invoice:
```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

To receive a payment, create an invoice for a specific amount:
```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```

To view information about my node:
```
$ lncli getinfo
```

The complete list of commands can be seen by simply running the lncli command:
```
$ lncli
```

Finally, to make calls to the LND API:
```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

END of guide!
