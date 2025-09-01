---
name: WireGuard
description: Setting up WireGuard VPN on Debian and Windows
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


In this tutorial, we'll learn how to configure a VPN based on WireGuard, a free, open-source VPN solution that boosts performance without neglecting security.


WireGuard is a relatively recent solution, having been available as a stable release since March 2020, and has had the honor of being integrated directly into the **Linux kernel since version 5.6**. This does not prevent it from being accessible from older Linux distributions that use a different version of the kernel. Compared with solutions such as OpenVPN and IPSec, WireGuard is simpler to use and much faster, as we'll see at the end of this article.


Some key points about WireGuard:



- Simple, lightweight and ultra-efficient!
- UDP-only operation (which can be a disadvantage when traversing certain firewalls)
- Works on a peer-to-peer rather than client-server model
- Authentication by key exchange, on the same principle as SSH with private/public keys
- Use of several algorithms: symmetrical encryption with ChaCha20, message authentication with Poly1305, as well as others such as Curve25519, BLAKE2 and SipHash24
- Supports both IPv4 and IPv6
- Multi-platform: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (and implemented in ProtonVPN)
- Only 4,000 lines of code, compared with hundreds of thousands for other solutions


For the cryptographic part, the various algorithms used are hand-picked, audited in several ways, and examined by security researchers specialized in the field.


The official project website: [wireguard.com](https://www.wireguard.com/)


Are you convinced by this solution after reading this introduction? All that's left to do is read on!


## II. Lab WireGuard diagram


Before I present my lab for setting up WireGuard, you should know that you can imagine **using WireGuard to interconnect two remote infrastructures**, but also to **connect a remote client to an infrastructure such as a corporate network or your home network**. This is in the same spirit as with OpenVPN, as we saw recently in the tutorial "[OpenVPN on Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".


If WireGuard is not set up directly on the router or firewall, as is conceivable with OpenWRT, you'll need to set up port forwarding so that the flow reaches the WireGuard pair.


![Image](assets/fr/034.webp)


Now I'll tell you about my lab and what we're going to set up today.


I'm going to use a Debian 11 machine as the WireGuard server and a Windows client as the WireGuard VPN client. Although it's a bit misleading to talk about a client-server relationship, because **WireGuard works on a "peer-to-peer "** model. That's a bit of a misnomer when you're trying to set up a "client-to-site" connection. Let's say instead that I'm going to have two pairs or **two WireGuard connection points** if you prefer: one under Debian 11 and the other under Windows.


These two pairs can communicate with each other in both directions, meaning that from my Windows machine I can access the remote LAN of the Debian 11 machine, and vice versa: it all depends on the configuration of the tunnel and the firewall of the WireGuard peer.


In this example, I'll focus on the following case: **from my Windows Peer 1 connected to my home network, I want to access my corporate network in order to access the company's servers via the WireGuard VPN tunnel**. This gives the following diagram:


![Image](assets/fr/035.webp)


In terms of IP addresses, this gives:



- Home network**: 192.168.1.0/24
- Corporate network**: 192.168.100.0/24
- WireGuard tunnel network**: 192.168.110.0/24

+ IP address of Peer 1 (Windows) in the tunnel: 192.168.110.2/24

+ IP address of Peer 2 (Debian) in the tunnel: 192.168.110.121/24


That's all there is to it! Let's get down to configuration!


**Note: by default, WireGuard operates in UDP mode on **port 51820**.


## III WireGuard server installation and configuration


I'm going to use the terms "client" for the Windows machine and "server" for the Debian machine in this tutorial, because even though it's peer-to-peer, it seems more meaningful.


### A. Installing WireGuard on Debian 11


The WireGuard installation package is available in the official Debian 11 repositories, so all we have to do is update the package cache and install it:


```
sudo apt-get update
```


```
sudo apt-get install wireguard
```


![Image](assets/fr/022.webp)


The WireGuard server part will be installed, along with various tools giving access to useful commands for managing the configuration.


### B. Installing a Interface WireGuard


Using the **command "wg "** we need to generate a private key and a public key: essential for authentication between two pairs, i.e. the server and a client (who will also need a key pair).


We will create the private key "**/etc/wireguard/wg-private.key**" and the public key "**/etc/wireguard/wg-public.key**" with this command sequence:


```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```


![Image](assets/fr/023.webp)


The value of the public key will be returned in the console. In the WireGuard configuration file, we need to **add the value of our private key**. To retrieve this value, enter the command below and copy the value:


```
sudo cat /etc/wireguard/wg-private.key
```


It's time to create a configuration file in "**/etc/wireguard/**". For example, we can name this file "**wg0.conf**", if we think that the Interface network associated with WireGuard will be "wg0", on the same principle as "eth0", for example.


```
sudo nano /etc/wireguard/wg0.conf
```


In this file, we must first add the following content (we'll come back to complete it later):


```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```


Section `[Interface]` is used to declare the server part. Here is some information:



- Address**: the IP address of the Interface WireGuard within the VPN tunnel (different subnet from the remote LAN)
- SaveConfig**: the configuration is stored (and protected) for as long as the Interface is active
- ListenPort**: WireGuard's listening port. In this case, 51820 is the default port, but you're welcome to customize it
- PrivateKey**: the value of our server's private key (*wg-private.key*)


Save the file and close it. With the "**wg-quick**" command, we can start this Interface by specifying its name (wg0, as the file is named wg0.conf):


```
sudo wg-quick up wg0
```


If you list the IP addresses of your Debian 11 server, you'll see a new Interface named "wg0" with the IP address defined in the config file:


```
ip a
```


![Image](assets/fr/027.webp)


In the same spirit, we can display the Interface "wg0" configuration via the "wg show" command:


```
sudo wg show wg0
```


![Image](assets/fr/024.webp)


Finally, we need to activate the automatic start-up of our Interface wg0 WireGuard:


```
sudo systemctl enable wg-quick@wg0.service
```


For the moment, we'll leave aside the configuration of WireGuard's server side.


### C. Enable IP Forwarding


For our Debian 11 machine to be able to **route packets between different networks (like a router)**, i.e. between the VPN network and the local network, we need to enable [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). By default, this feature is disabled.


Modify this configuration file:


```
sudo nano /etc/sysctl.conf
```


Add the following directive to the end of the file and save:


```
net.ipv4.ip_forward = 1
```


That's all there is to it.


### D. Enable IP Masquerade


In order for our server to route packets correctly and for the remote LAN to be accessible to the Windows machine, we need to activate IP Masquerade on our Debian server. This is a kind of NAT activation. I'm going to perform this configuration on the Linux firewall through UFW, which I'm used to using ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).


If you don't already have UFW and want to set it up (you can also use Nftables), start by installing:


```
sudo apt install ufw
```


First of all, you need to enable SSH so as not to lose control of the remote server (adapt the port number):


```
sudo ufw allow 22/tcp
```


Port 51820 in UDP must also be authorized, as we use it for WireGuard (again, adapt the port number):


```
sudo ufw allow 51820/udp
```


Next, we'll continue with the configuration to enable IP masquerade. To do this, we need to retrieve the name of the Interface connected to the local network. If you don't know the name, run "ip a" to see the name of the card. In my case, it's the "**ens192**" card.


![Image](assets/fr/036.webp)


We're going to use this information. Edit the following file:


```
sudo nano /etc/ufw/before.rules
```


Add these lines at the end of the file to **enable IP masquerade on the Interface ens192** (adapt the Interface name) within the POSTROUTING string of our local firewall's NAT table:


```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```


The picture shows:


![Image](assets/fr/037.webp)


Keep this configuration file open and proceed to the next step. 😉


### E. Linux firewall configuration for WireGuard


Still in the same configuration file, we're going to declare the corporate network "192.168.100.0/24" so that we can contact it. Here are the two rules to be added (ideally after the "*# ok icmp code for FORWARD*" section to group the rules together):


```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```


If you want to authorize only one host, for example "192.168.100.11", it's easy:


```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```


Now you can save the file and close it. All that remains is to activate UFW and restart the service to apply our changes:


```
sudo ufw enable
```


```
sudo systemctl restart ufw
```


The first part of the Debian server configuration is now complete.


## IV. WireGuard client for Windows


The WireGuard client is available for Windows, macOS, Android, etc... This is great news. All downloads are available on this page: [WireGuard Client](https://www.wireguard.com/install/). In this example, I'm going to set up the client on Windows. To set up the WireGuard client on Linux, follow the same principle as for creating the wg0.conf file on the Debian machine (without all the NAT, etc.).


### A. Installing the WireGuard Windows client


Once you've downloaded the executable or the MSI package, installation is straightforward: just launch the installer, and...voilà, it's done! 🙂


![Image](assets/fr/038.webp)


### B. Create a WireGuard profile


Start by opening the software to create a new tunnel. To do this, click on the arrow to the right of the "**Add tunnel**" button and click on the "**Add empty tunnel**" button.


![Image](assets/fr/028.webp)


A configuration window will open. Each time a new tunnel configuration is created, WireGuard generates a private/public key pair specific to this configuration. **In this configuration, we need to declare the "peer", i.e. the remote server:


```
[Interface]
PrivateKey = <la clé privée du PC>
```


We need to complete this configuration, in particular to declare the IP address on this Interface (*Address*), but also to declare the remote WireGuard server via a [Peer] block. The image below should remind you of the configuration file we created on the Linux server side.


Let's start with the `[Interface]` block, adding the IP address "**192.168.110.2**"; remember that the server has the IP address "**192.168.110.121**" on this network segment. This gives:


```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```


Next, we need to declare the "Peer" block with three properties, resulting in this configuration:


```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```


In pictures:


![Image](assets/fr/029.webp)


**A few explanations about the [Peer] block:



- PublicKey**: this is the public key of the WireGuard Debian 11 server (you can obtain its value with the "*sudo wg*" command)
- AllowedIPs**: these are the IP addresses / subnets accessible via this WireGuard VPN network, in this case the subnet specific to my WireGuard VPN (*192.168.110.0/24*) and my remote LAN (*192.168.100.0/24*)
- Endpoint**: this is the IP address of the Debian 11 host, since this is our WireGuard connection point (you'll need to specify the public IP address)


Finally, enter a name in the "**Name**" field (without spaces) and copy and paste the client's public key, as we'll need to declare it on the server. Click on "**Register**".


### C. Declare client on WireGuard server


It's time to return to the Debian server to declare the "**Peer**", i.e. our Windows PC, in the WireGuard configuration. First of all, we need to **stopper the Interface "wg0"** in order to modify its configuration:


```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```


Next, modify the previously created configuration file:


```
sudo nano /etc/wireguard/wg0.conf
```


In this file, following the `[Interface]` block, we need to declare a `[Peer]` block:


```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```


This [Peer] block contains the Windows 10 PC's public key (**PublicKey**) and the IP address of the PC's Interface (**AllowedIPs**): the server will communicate in this WireGuard tunnel only to contact the Windows client, hence the value "**192.168.110.2/32**".


All that remains is to save the file (*CTRL+O then Enter then CTRL+X via Nano*). Relaunch Interface "wg0":


```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```


To check that the peer declaration works, you can use this command:


```
sudo wg show
```


Once the remote host has set up its WireGuard connection, its IP address will be moved up to the "endpoint" value.


![Image](assets/fr/033.webp)


Finally, we'll secure the configuration files to limit root access:


```
sudo chmod 600 /etc/wireguard/ -R
```


### D. First WireGuard connection


Now that the configuration is ready, we can initiate it from the Windows PC. To do this, in the "**WireGuard**" client, click on the "**Activate**" button: the connection will **change from "Off" to "On "**, but that doesn't mean it will work. It all depends on whether your configuration is correct or not. **When the connection is established, our two machines communicate via the Interface WireGuard configured on each side!


![Image](assets/fr/030.webp)


In the event of a problem, this will be visible in the "**Logbook**" tab. The two hosts will exchange packets regularly to check the status of the connection, hence the "*Receiving keepalive packet from peer 1*" messages.


![Image](assets/fr/031.webp)


If WireGuard's "**Journal**" tab displays a message like the one below, you need to check that the public keys declared on both sides are correct.


```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```


From my remote PC, I can ping the IP address of my Interface WireGuard on the server side, as well as a host on my remote LAN.


![Image](assets/fr/032.webp)


### E. Performance: OpenVPN vs WireGuard


From my remote PC connected to my WireGuard VPN, I was able to access a file server and transfer a file via [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), to see the transfer rate. **With WireGuard, I max out at around 45 Mb/s, which is great, as I'm on WiFi


![Image](assets/fr/025.webp)


Under the same conditions, but via an OpenVPN connection (in UDP) this time, with the same operation, the throughput is totally different: around 3 MB/s. The difference is obvious!


![Image](assets/fr/026.webp)


This is interesting, because if, for example, you switch from a WiFi connection to a 4G/5G connection, the reconnection will be so fast that the interruption won't be visible.


### F. Bonus: full tunnel WireGuard


With the current configuration, part of the traffic flows through the VPN, and the rest through the customer's Internet connection, including Internet browsing. If we want to switch to WireGuard **full tunnel mode**, so that everything passes through the VPN tunnel, we need to make a few changes to our configuration....


First, you need to install the "resolvconf" package on the:


```
sudo apt-get update
sudo apt-get install resolvconf
```


Once this has been done, you need to modify the "wg0.conf" profile on the Debian machine: stop Interface, modify it, and restart.


```
sudo wg-quick down /etc/wireguard/wg0.conf
```


Next, **in the `[Interface]` block, we add the DNS server to be used**. In my case, it's my lab's domain controller, but we could also install Bind9 on the Debian machine to have a local resolver.


```
DNS = 192.168.100.11
```


Save the file, then restart Interface:


```
sudo wg-quick up /etc/wireguard/wg0.conf
```


Finally, in the tunnel configuration on the Windows 10 workstation, you need to modify the "AllowedIPs" section to indicate that everything must pass through the tunnel. Replace:


```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```


By:


```
AllowedIPs = 0.0.0.0/0
```


You can see that this also enables the "**Kill switch*" option.


![Image](assets/fr/040.webp)


Finally, I took advantage of this full tunnel to carry out a small flow test, the results of which are shown below:


![Image](assets/fr/039.webp)


WireGuard's configuration is quite simple and easy to understand, and above all to maintain. **WireGuard is considered to be the future of VPNs**, so we'd better keep a close eye on it! We can also see that the benefit is significant in terms of performance, which is a huge advantage for WireGuard compared with OpenVPN.


Additional documentation:



- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Command wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)


**Your WireGuard VPN is up and running! Congratulations!