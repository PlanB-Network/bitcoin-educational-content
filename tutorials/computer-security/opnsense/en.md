---
name: OPNsense
description: How do I install and configure an OPNsense firewall?
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


In this tutorial, we'll be taking a look at the OPNsense open source firewall. We'll look at its main features, the prerequisites, and how to install this FreeBSD-based solution.


Before getting started, you should know that **OPNsense and pfSense are both open source firewalls** based on FreeBSD. We can say that pfSense is OPNsense's big brother of sorts, as the latter is a Fork created in 2015. Finally, it's important to point out that since 2017, **OPNsense has switched to HardenedBSD instead of FreeBSD**. HardenedBSD is an enhanced version of FreeBSD, with advanced security features


OPNsense stands out for its more modern user Interface and **more frequent update cadence**. Indeed, OPNsense's update schedule includes two major releases per year, which are updated every two weeks or so (resulting in minor releases). This follow-up is very interesting in comparison with pfSense, if we look at the community versions of these solutions.


![Image](assets/fr/050.webp)


## II. OPNsense features


OPNsense is an operating system designed to act as a firewall and router, although its features are numerous and can be extended by installing additional packages. Suitable for production use, it is mainly used for network security and flow management.


### A. Main features


Here are some of OPNsense's key features:



- Firewall and NAT**: OPNsense provides advanced stateful firewall functionality with stateful filtering, as well as network address translation (NAT) capabilities.



- DNS/DHCP**: OPNsense can be configured to manage DNS and DHCP services on the network. It can act as a DHCP server, but can also be used as a DNS resolver for machines on the local network. Dnsmasq is also integrated by default.



- VPN**: OPNsense supports several VPN protocols, including IPsec, OpenVPN and WireGuard, enabling secure connections for remote access to mobile workstations or site interconnection.



- Web proxy**: OPNsense includes a web proxy to control and filter Internet access. It can also be used to filter content and manage network access.



- Bandwidth management (QoS)**: OPNsense offers Quality of Service (QoS) management features to prioritize network traffic and better manage network bandwidth.



- Captive portal**: this feature lets you manage user access to the network via an authentication page (local base, vouchers, etc.). It is a feature commonly deployed for public Wi-Fi networks.



- IDS/IPS**: OPNsense integrates Suricata to offer intrusion detection and prevention (IDS/IPS) functions to protect the network against attacks.



- High availability (CARP)**: OPNsense supports CARP (*Common Address Redundancy Protocol*) for high availability between multiple OPNsense firewalls, ensuring that service remains active even in the event of hardware failure.



- Reporting and Monitoring**: OPNsense provides real-time reporting and monitoring tools to track network performance (with NetFlow) and detect potential problems, thanks to the creation of logs. This includes graphics. The Monit tool is integrated into OPNsense and enables supervision of the firewall itself.


### B. Additional packages


This is just an overview of the features offered by OPNsense. In addition, the **package catalog** accessible from the OPNsense administration Interface allows you to **enrich the firewall with additional functionalities**. These include an ACME client, a Wazuh agent, the NTP Chrony service, and Caddy as a reverse proxy.


![Image](assets/fr/051.webp)


## III. OPNsense prerequisites


First of all, you need to decide where you're going to install OPNsense. There are several possible solutions, including installation on :



- A hypervisor as a virtual machine, whether Hyper-V, Proxmox, VMware ESXi, etc.
- A machine as a *bare-metal* system. This could be a mini PC that acts as a firewall.


You can also purchase **an OPNsense rack-mountable appliance** through our online store.


You need to take into account the hardware resources required to run OPNsense. This is detailed on [this documentation page](https://docs.opnsense.org/manual/hardware.html).


**Minimum and recommended resources for production:**


| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Finally, **your resource requirements depend above all on the number of connections to be managed**, and therefore on **your bandwidth requirements**. In addition, you need to **keep in mind the services that will be activated and used** (proxy, intrusion detection, etc...) as they can be CPU and/or RAM-hungry.


You'll also need the OPNsense installation ISO image, which you can download from [the official website](https://opnsense.org/download/). For installation on a VM, select "**dvd**" as the image type to obtain an ISO image (and do what you like with it...). For installation via a bootable USB key, select the "**vga**" option to obtain a "**.img**" file.


![Image](assets/fr/048.webp)


You'll also need a computer for OPNsense administration and testing.


## IV. Target configuration


Our goal is to



- Create an internal virtual network (192.168.10.0/24 - LAN)**, which can access the Internet via the OPNsense firewall. For production use, this could be your local network, cable and/or Wi-Fi.
- Activate and configure NAT** so that VMs in the internal virtual network can access the Internet
- Activate and configure the DHCP server on OPNsense** to distribute an IP configuration to future machines connected to the internal virtual network
- Configure the firewall** to allow only outgoing LAN to WAN flows in HTTP (80) and HTTPS (443).
- Configure the firewall** to allow the virtual LAN to use OPNsense as a DNS resolver (53).


If you are using the Hyper-V platform, this will give you the following representation:


![Image](assets/fr/033.webp)


## V. Installing the OPNsense firewall


### A. Preparing the bootable USB key


The first step is to prepare the installation media: **the bootable USB key with OPNsense**. This is of course optional if you're working in a virtual environment, but in any case you need to download the OPNsense installation ISO image.


After downloading, you get **an archive containing an image in ".img "** format. You can **create a bootable USB stick** with various applications, including **balenaEtcher**: ultra-simple to use. What's more, the application will recognize the image in the archive, so you don't have to decompress it beforehand.



- [Download balenaEtcher](https://etcher.balena.io/)


Once the application is installed, select your image, your USB key and then click on the "Flash! Wait a moment.


![Image](assets/fr/049.webp)


Now you're ready to install.


### B. Installing the OPNsense System


Start up the machine hosting OPNsense. You should see a welcome page similar to the one below. For a few seconds, the screen shown will be visible in the window. Let the process run its course...


![Image](assets/fr/019.webp)


The OPNsense image is loaded onto the machine, so that the system can be accessed in "**live**" mode, i.e. temporarily stored in memory.


![Image](assets/fr/025.webp)


Then you'll come to a Interface similar to the one below. Log in with login "**installer**" and password "**opnsense**". Please note that the keyboard is **QWERTY** at the moment. At this point, we'll **start the OPNsense installation process**.


![Image](assets/fr/026.webp)


A new wizard appears on the screen. The first step is to select the keyboard layout corresponding to your configuration. For an AZERTY keyboard, select the option "**French (accent keys)**" from the list, then double-click**.


![Image](assets/fr/027.webp)


The second step is to select the task to be performed. Here, we're going to perform an installation using the **ZFS file system**. Position yourself on the "**Install (ZFS)**" line and confirm with **Enter**.


![Image](assets/fr/028.webp)


In the third step, select "**stripe**" as our machine is equipped with **only one disk**: there is no redundancy possible to secure the firewall storage and its data. This is particularly relevant when installing on a physical machine to protect against hardware failure of a disk, via the RAID principle.


![Image](assets/fr/029.webp)


In the fourth step, simply press **Enter** to confirm.


![Image](assets/fr/030.webp)


Finally, confirm by selecting "**YES**" and then pressing the **Enter** key.


![Image](assets/fr/031.webp)


Now you'll have to wait while OPNsense is installed... This process takes about 5 minutes.


![Image](assets/fr/032.webp)


Once installation is complete, we can change the "**root**" password before rebooting. Select "**Root Password**", press **Enter** and enter the password "**root**" twice.


![Image](assets/fr/020.webp)


Finally, select "**Complete Install**" and press **Enter**. Take this opportunity to **eject the disk from the VM's DVD drive**. In the VM settings, you can also set the first boot to disk.


![Image](assets/fr/021.webp)


The virtual machine will reboot and load the OPNsense system from disk, since we've just installed it. Log in with the "root" account in the console, and your new password (otherwise, the default password is "**opnsense**").


### D. Linking network interfaces


The screen shown below will appear. Select "**1**" and press **Enter** to associate the machine's network cards with the OPNsense interfaces.


![Image](assets/fr/022.webp)


First, the wizard asks you to configure link aggregation and VLANs. Specify "**n**" to refuse, and each time, validate your answer with **Enter**. Next, you need to assign the two interfaces "**hn0**" and "**hn1**" to the **WAN** and **LAN**. In principle, "**hn0**" corresponds to the WAN and the other Interface to the LAN.


Here's how it works:


![Image](assets/fr/023.webp)


We now have :



- The Interface **LAN** associated with the "**hn1**" network card and with the OPNsense default IP address, i.e. **192.168.1.1/24**.
- The Interface **WAN** associated with the "**hn0**" network card and with an IP address retrieved via **DHCP** on the local network (thanks to our external virtual switch).


By default, the OPNsense administration Interface is only accessible from the LAN Interface, for obvious security reasons. You must therefore connect to the firewall's Interface LAN to perform administration. If this is not possible, you can temporarily administer OPNsense from the WAN. This involves disabling the firewall function.


To do this, switch to shell mode via the "**8**" option and run the following command:


```
pfctl -d
```


![Image](assets/fr/024.webp)


### E. Access to the OPNsense Interface management system


The OPNsense Administration Interface can be accessed via HTTPS, using the IP address of the LAN** Interface (or the WAN). Your browser will take you to a login page. Log in with the "root" account and password you selected earlier.


![Image](assets/fr/034.webp)


Wait a few seconds... You will be prompted to follow a wizard to perform the basic configuration. Click "**Next**" to continue.


![Image](assets/fr/036.webp)


The first step is to define the host name, the domain name, choose the language and define the DNS server(s) to be used for name resolution. Keeping the "**Enable Resolver**" option will allow the firewall to be used as a DNS resolver, which will be useful for the machines in our virtual LAN.


![Image](assets/fr/037.webp)


Proceed to the next step. The wizard gives you the option of **defining an NTP server for date and time synchronization**, although there are already servers configured by default. In addition, it is essential to choose the time zone corresponding to your geographical location (unless you have special requirements).


![Image](assets/fr/038.webp)


Then comes an important step: **configuring the Interface WAN**. Currently, it's configured in DHCP and will remain in this configuration mode, unless you wish to set a static IP address.


![Image](assets/fr/039.webp)


Still on the Interface WAN configuration page, you need to uncheck the "**Block access to private networks via WAN**" option if the network on the WAN side uses private addressing. This will probably be the case if you're running a Lab, and so may prevent you from accessing the Internet.


![Image](assets/fr/040.webp)


Next, you can **define a "root "** password, but this is optional because we've already done it.


![Image](assets/fr/041.webp)


Continue to the end to initiate the configuration reload. If you need to continue taking control via the WAN, restart the above command once this process is complete.


![Image](assets/fr/042.webp)


That's all there is to it!


![Image](assets/fr/035.webp)


### E. DHCP configuration


Our aim is to use the OPNsense DHCP server to distribute IP addresses on the virtual LAN. To do this, we need to access this menu location:


```
Services > ISC DHCPv4 > [LAN]
```


**As you can see, DHCP is already enabled by default on the LAN ** If you're not interested in this service, you should disable it. Although it's already enabled and we want to use it, it's important to review its configuration.


If required, you can change the range of IP addresses to be distributed: **192.168.10.10** to **192.168.10.245**, depending on current settings.


![Image](assets/fr/046.webp)


We can also see that the fields "**DNS servers**", "**Gateway**", "**Domain name**", etc., are empty by default. In fact, there is an automatic inheritance of certain options and default values for these various fields. For example, for the DNS server, the IP address of the Interface LAN will be distributed, enabling the OPNsense firewall to be used as a DNS resolver.


Save the configuration after making any changes, if necessary.


![Image](assets/fr/047.webp)


To test the DHCP server, you need to connect a machine to your firewall's LAN network.


This machine must obtain an IP address from the OPNsense DHCP server, and our machine must have access to the network. Internet access must work. Please note that if you have disabled the firewall function to access OPNsense from the WAN, this will disable NAT, preventing you from accessing the Web.


**Note**: currently issued DHCP leases are visible from the OPNsense administration Interface. To do this, go to the following location: **Services > ISC DHCPv4 > Leases**.


![Image](assets/fr/045.webp)


### F. Configuring NAT and firewall rules


The good news is that we can now access the OPNsense administration Interface from the LAN.


```
https://192.168.1.10
```


After logging on to OPNsense, let's discover the NAT configuration. Go to this location: **Firewall > NAT > Outbound**. Here you can choose between automatic (default) and manual creation of outbound NAT rules.


Choose automatic mode via the "**Automatic generation of outgoing NAT rules**" option and click on "**Save**" (in principle, this configuration is already the active one). In automatic mode, OPNsense itself creates a NAT rule for each of your networks.


![Image](assets/fr/043.webp)


For the time being, all computers connected to the virtual LAN "**192.168.10.0/24**" can access the Internet without restriction. However, our goal is to restrict access to the WAN to HTTP and HTTPS protocols, as well as DNS on the firewall's Interface LAN.


So we need to create firewall rules... Browse the menu as follows: **Firewall > Rules > LAN**.


**By default, there are two rules to authorize all outgoing LAN traffic, in IPv4 and IPv6**. Deactivate these two rules by clicking on the green arrow on the far left, at the beginning of each line.


Then create three new rules to authorize the **LAN network** (i.e. "**LAN net**") to :



- access all destinations using **HTTP**.
- access all destinations with **HTTPS**.
- request **OPNsense** on its **Interface LAN** (i.e. "**LAN address**"), via the **DNS protocol** (this implies using the firewall as DNS), otherwise authorize your DNS resolver via its IP address.


This gives the following result:


![Image](assets/fr/044.webp)


All that remains is to click on "**Apply changes**" to switch the new firewall rules over to production. **Please note that all flows that are not explicitly authorized will be blocked by default


The LAN machine can access the Internet, using HTTP and HTTPS. All other protocols will be blocked.


![Image](assets/fr/018.webp)


## IV. Conclusion


By following this guide, you'll be able to install OPNsense and get started right away. OPNsense offers a wide range of features to secure and manage your network traffic efficiently, and is suitable for use in professional environments.


This installation is just the beginning: feel free to explore the menus and configure other features to adapt OPNsense to your needs.