---
name: Angry IP Scanner
description: A simple way to scan your network
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


How do you scan a Windows network for connected machines quickly and easily? The answer is Angry IP Scanner. This open source project lets you scan a network easily, using an easy-to-use graphical Interface.


This tool can be used by individuals to **scan their local network**, but also by IT professionals for the same purpose. Proof that **this tool is very practical**, it has already been used by **some cybercriminal groups** to scan corporate networks (in the same way as Nmap). A good example is [ransomware group RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). It's still a sound piece of software, but as with other network and security-oriented tools, its use can be abused.


Here, we'll be using it on **Windows 11**, but it's perfectly possible to use it on other versions of **Windows**, as well as on **Linux** and **macOS**.


Less comprehensive than Nmap, **Angry IP** Scanner is still interesting for a quick, basic network analysis, but also because it's within everyone's reach. It will **detect hosts connected to the network** and identify **host names** and **open ports**.


If you want to go further, see the tutorial on Nmap:


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Getting started with Angry IP Scanner


### A. Download and install Angry IP Scanner


You can download the latest version of Angry IP Scanner from the application's official website or from GitHub. We'll use the latter option. Click on the link below and download the EXE version: "**ipscan-3.9.1-setup.exe**".



- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)


![Image](assets/fr/016.webp)


Run the executable to proceed with the installation. There is nothing special to do during installation.


![Image](assets/fr/013.webp)


### B. Run an initial network scan


On first launch, take the time to read the instructions in the "**Getting Started**" window to learn more about how the tool works. By the way, there are several terms to consider:



- Feeder**: module responsible for generating lists of IP addresses to be scanned, from a random IP range or a file with a list of IP addresses.
- Fetcher**: a set of modules for retrieving information about hosts on the network. There are, for example, fetchers to detect MAC addresses, scan ports, detect host names or send HTTP requests.


![Image](assets/fr/018.webp)


To scan an IP subnet, simply enter the **start IP address** and the **end IP address** in the "**IP range**" field (otherwise, change the type on the right). Then click on the "**Start**" button.


![Image](assets/fr/019.webp)


A few tens of seconds later, the result will be visible in the software's Interface. **For each IP address in the range analyzed, you'll see whether Angry IP Scanner has detected a host or not.** A summary will also appear on the screen, indicating the number of active hosts (in this case 6) and the number of hosts with open ports.


![Image](assets/fr/020.webp)


Here, we can see the presence of a host named "**OPNsense.local.domain**", associated with the IP address "**192.168.10.1**" and accessible on **ports 80** and **443** (HTTP and HTTPS). Right-clicking on the host gives access to additional commands, such as pinging, trace route and browser opening via this IP address.


![Image](assets/fr/012.webp)


### C. Add scan ports


By default, **Angry IP Scanner** will scan 3 ports: **80** (HTTP), **443** (HTTPS) and **8080**. You can add more ports to be scanned from the application preferences. Click on the "**Tools**" menu, then on the "**Ports**" tab.


Here, you can modify the port list via the "**Port selection**" option. You can **indicate specific port numbers separated by a comma, or port ranges**. The example below adds two ports: **445** (SMB) and **389** (LDAP). To scan ports from 1 to 1000, enter "**1-1000**". It is not specified whether port scans are performed in TCP, UDP or both.


![Image](assets/fr/021.webp)


If you run the scan again, you're likely to get new information. In the example below, Angry IP Scanner tells me that ports 389 and 445 are open on hosts "**SRV-ADDS-01**" and "**SRV-ADDS-02**", thanks to the new configuration of ports to be scanned.


![Image](assets/fr/022.webp)


**Note**: from the "**Scanner**" menu, you can export scan results to a text file.


If you wish to take the scan further, click on the "**Tools**" menu, then click on "**Fetchers**". This adds "capabilities" to the scan. Simply select a fetcher and move it to the left to activate it. This will add an extra column to the scan result.


![Image](assets/fr/014.webp)


The example below shows the "**NetBIOS info**" and "**Web detection**" functions. The former provides additional information such as the machine's MAC address and domain name, while the latter displays the web page title (which may give some indication of the type of web server or application).


![Image](assets/fr/011.webp)


Finally, from the preferences, you can also change the method used for "**ping**", i.e. to consider whether a host is active or not. Since some hosts don't respond to pings, this allows you to try other methods (UDP packet, TCP port probe, ARP, UDP + TCP combination, etc.).


## III. Conclusion


Simple and effective: Angry IP Scanner detects hosts connected to a network, and lets you configure port scans. In terms of options, it's not as flexible as Nmap, and doesn't go as far, but it's a good start for quick scanning.


If you'd like to use **Nmap** with a graphical Interface, you can use **the Zenmap application** (see overview below).


![Image](assets/fr/015.webp)


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d