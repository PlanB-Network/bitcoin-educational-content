---
name: Ntopng
description: Monitor your network with ntopng
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian Duchemin published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


**Whether it's to check network fluidity, to get a clear picture of usage or for performance stats, network flow monitoring is an important part of an enterprise network**. It helps anticipate changes to the infrastructure and helps ensure quality of use for users (also known as QoE for *Quality of Experience*, as opposed to QoS).


To do this, there are many techniques and software/protocols available. Netflow, for example, developed by Cisco, can be used to retrieve IP flow statistics from a Interface, but its use is restricted to compatible equipment.


That's why in this tutorial I'm going to introduce **Ntop** and show you how to use it in your infrastructure to keep an eye on your network usage.


Ntop is open source software that can be installed on any Linux machine. It is free of charge and can collect the following data:



- Bandwidth utilization
- Main customers
- Main destinations
- Protocols used
- Applications used
- Ports used
- Etc.


Now renamed **Ntopng (New Generation)**, it offers many basic functions free of charge. A commercial version is also available, allowing configured alerts to be exported to SIEM-type software, or traffic to be filtered with rules defined directly from the probe.


## II. Prerequisites


The installation of a Ntop probe differs according to the equipment and the environment. So I'm not going to give you a step-by-step guide here, but will outline the various possibilities.


### A. On-board mode


If you have a pfSense, OPNSense or Endian firewall in production, or even a Linux workstation with NFTables, good news! You can install Ntopng directly and start monitoring your interfaces.


The advantage of this technique is that it requires no additional hardware. On the other hand, it increases resource utilization, so make sure you have adequate hardware or a VM of sufficient size (minimum 2 cores and 2BG RAM).


### B. TAP / SPAN mode


A **tap** is **a network device that duplicates the traffic passing through it and sends it to another device.** The advantage of this device is that it doesn't require any modification to the existing infrastructure, and can be placed anywhere to monitor specific network sections, or between the core switch and the edge router to analyze traffic to/from the Internet.


The big disadvantage of this type of equipment is its cost. In today's Gigabit networks, a passive tap can't properly capture network traffic, so you need an active device costing around €200 (minimum).


The **SPAN** mode, also known as **port mirroring**, is used by a switch to forward traffic from one port to another. This is by far my preferred method, as it's simple to set up and, like tap, allows you to monitor a portion of the network or the entire network at will. However, there are two drawbacks: the switch must integrate this function, and its use can increase the processor load on the switch.


### C. Router mode


It's perfectly possible to mount a router under Linux and install ntopng on it. The only drawback to this method is that it will modify your network, either its internal addressing, or the addressing between your "real" router and the one you're adding.


Note: for readers of the article [Create a Wifi router with Raspberry Pi and RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) it's perfectly possible to install ntopng on your Rpi to get accurate statistics!


### D. Bridge mode


An interesting alternative is to use **a Linux machine in bridge mode.** Placed between two pieces of equipment, this allows all traffic to be captured without having to intervene in the configuration of the infrastructure or its equipment. As an old machine can do the job, the cost of this method can also be attractive. Note that to be optimal, the device should have three network cards, two in bridge mode, one to access Interface and SSH. It is possible to use just two cards, but then the device administration traffic will also be captured...


So it's **this last mode that I'm going to use**. For practical reasons, I'll be using virtual machines for the demonstration, but the method remains the same for use on physical machines.


## III. Probe preparation with Interface bridge


For the probe, I choose a **Debian 11** machine in minimal installation.


First step, always the same, update the :


```
apt-get update && apt-get upgrade
```


Then install the **bridge-utils** package, which will allow us to create our bridge:


```
apt-get install bridge-utils
```


Once installed, the first thing to note is the current name of our network cards. Under Debian, this name can take several forms, and we'll need it for configuration.


A simple **ip add** command will return an output with this information:


![Image](assets/fr/016.webp)


Here, I see 3 interfaces:



- Lo**: this is the loopback Interface; it's a virtual Interface that "loops" over the equipment. Basically, this Interface, whose address is 127.0.0.1 (although any address in 127.0.0.0/8 will do, as this range is reserved for this purpose) is used to contact the equipment itself. If you've installed a web site on your workstation (using WAMPP, for example), you've probably used the "*localhost*" address at one time or another to display the site hosted on your own machine. This host name is associated with the address 127.0.0.1 and therefore with the Interface loopback.
- ens33**: this is my first Interface, which received an address here from my DHCP
- ens36**: my second Interface


Now that I have all the information, I can modify the */etc/network/interfaces* file to create my bridge. Here's what it currently looks like (may vary):


```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```


The first part concerns my loopback Interface, which I won't be touching, followed by the Interface ens33. The modifications involve adding my second Interface (ens36) and configuring the bridge with these two interfaces:


```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```


Here are some explanations of these first changes:



- auto *Interface***: will automatically "start" Interface on system startup
- iface *Interface* inet manual** : to use the Interface without any IP address. Like the keyword "static" to define a static IP address or "dhcp" to use dynamic addressing


The modifications continue:


```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```


Here again, a few explanations:



- iface br0 inet static**: here I've defined my Interface bridge (*br0*) with a static address.
- Address, netmask, gateway**: board addressing information
- bridge_ports**: interfaces to be included in the bridge
- bridge_stp**: the Spanning Tree protocol is used when interconnecting switches to detect redundant links and avoid loops. Since a bridge can be inserted between two network paths, it can be the source of a loop, hence the possibility of enabling this protocol. I don't need it here, so I'm disabling it.


Save the changes and restart the network:


```
systemctl restart networking
```


To check the changes, display the result of the **ip** add command again:


![Image](assets/fr/021.webp)

You can clearly see **my new Interface "*br0*" with the IP address I've assigned to it.** Incidentally, you can also see that my two physical interfaces are indeed "UP", but have no IP address.


## IV. Installing NtopNG


Now that our probe is able to sniff traffic between my network and the router, all that's left to do is install ntopng. To do this, first modify the */etc/apt/sources.list* file and add **contrib** at the end of each line starting with **deb** or **deb-src**.


By default, package sources contain only DFSG (*Debian Free Sotftware Guidelines*) compliant packages, identified by the **main** keyword. You can also add these sources:



- contrib**: packages containing DFSG-compliant software, but using dependencies that are not part of the **main** branch
- non-free**: contains packages that are not DFSG-compliant


Example of a line in /etc/apt/sources.list :


```
deb http://deb.debian.org/debian/ bullseye main
```


So I'll just add the word **contrib** to lines like these.


The rest of the steps are listed on the [NtopNG] site (https://packages.ntop.org/apt/) where, for Debian 11, you need to add the Ntop sources for future installation. This addition is automated by using a :


```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```


Then comes the actual installation phase:


```
apt-get clean all
apt-get update
apt-get install ntopng
```


The first command deletes the cache of the apt package manager. The second will update the package list and the third will install NtopNG.


After installation, the **NtopNG software is directly available on port 3000 of the Debian machine**. So for me it's `http://192.168.1.23:3000`


![Image](assets/fr/022.webp)


NtopNG home page


The default login and password are shown, so all you have to do is enter them!


## V. Using NtopNG


When you first log in, the first thing you'll be asked to do is change the default admin password and language. Unfortunately, French isn't one of them.


You then arrive on the dashboard:


![Image](assets/fr/023.webp)


NtopNG dashboard


Don't get used to this one! If you notice the yellow box at the top of the screen, you'll see the sentence: "*Licence expires in 04:57*". By default, installation launches a trial of the full version of NtopNG, but for a (very) limited time. Once this "countdown" has been reached, the *community* version is activated and the dashboard changes:


![Image](assets/fr/024.webp)


New NtopNG community dashboard


The first thing to do is **check that the correct Interface is listening**. In the top left-hand corner, a drop-down list of available interfaces lets you select the Interface we're interested in here: br0


![Image](assets/fr/025.webp)


Interface selection


The new window displays the "Top Flaw Talkers", i.e. the devices that communicate the most. Here I only have two stations that appear:


![Image](assets/fr/026.webp)


**Source hosts appear on the left, destinations on the right ** This allows you to visualize the use of total bandwidth by each host, and to get an overall view of network traffic. That's not bad, but we can go further...


If I click on "*Hosts*", for example, I get a graph showing the sending and receiving power consumption of each host on my network. Here, for example, I can see that 192.168.1.37 alone accounts for 80% of my traffic:


![Image](assets/fr/027.webp)


If I click on the IP address of the host in question, I'm redirected to a summary page:


![Image](assets/fr/028.webp)


I can see, for example, that it's a VMWare machine (by recognizing the YES of my MAC address), that it's called DESKTOP-GHEBGV1 (so surely a Windows host) AND I have **stats on packets received and sent, as well as the amount of data**.


You'll also notice a new menu at the top of this summary. I suggest you click on "**Apps**" to see what's driving so much traffic:


![Image](assets/fr/017.webp)

Ha, looks like we've got an answer! On the graph on the left, **we see that 76.6% of its traffic is from ... Windows Update**, so this host is downloading updates!


NtopNG uses a technology called DPI for *Deep Packet Inspection*, enabling it to categorize each network flow and define the application (or family of applications) behind it.


To demonstrate, I launch a YouTube video on my host:


![Image](assets/fr/018.webp)


**The traffic was immediately recognized and categorized!


Note: for obvious reasons, this kind of software can raise privacy issues, so be careful to use it under the right conditions. Note also that it is possible to **anonymize results**, the option can be found in **Settings > Preferences > Misc** and is called "**Mask Host IP Address**".


## VI. Detections & alerts


NtopNG is also capable of issuing security alerts on certain feeds. These can be found in the **Alerts** menu, on the left-hand banner. Here, for example, I have a total of 2851 alerts, divided into different severities: Notice, Warning and Error.


![Image](assets/fr/019.webp)


Let's take a look at the high criticality alerts, I've got 17 of them!


Clicking on this figure brings up the details of the alerts. There's nothing alarming here, it's a false positive, the download of updates being categorized as a binary file transfer in an HTTP stream, which could indeed mean an attack.


![Image](assets/fr/020.webp)


However, as I'm using the free version, I can't exclude domains or hosts that are the source of alerts, so you'll have to keep an eye on them to avoid missing out on something much more worrying. NtopNG will generate alerts in the event of :



- Binary file download over HTTP
- Suspicious DNS traffic
- Using a non-standard port
- SQL injection detection
- Cross-Site Scripting (XSS)
- Etc.


## VII. Conclusion


In this tutorial, we have seen **how to set up a probe with NtopNG** enabling us to **analyze our network traffic** to visualize protocol usage and the occupancy of each host, but also detect suspicious traffic.


Unfortunately, I can't cover all the features and possibilities in this article, but feel free to explore!


This solution can be implemented on a permanent basis within an enterprise infrastructure. NtopNG can also export results to an InfluxDB database, enabling you to create your own dashboards with a third-party tool such as Graphana.