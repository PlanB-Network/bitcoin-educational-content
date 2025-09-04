---
name: Nmap
description: Master Nmap for network mapping and vulnerability scanning
---

![cover](assets/cover.webp)


*This tutorial is based on original content by Mickael Dorigny published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes have been made to the original text.*


___


Welcome to this introductory tutorial to Nmap, designed for anyone wishing to master this powerful network scanning tool. The aim is to provide you with the fundamental knowledge you need to use Nmap effectively on a day-to-day basis.


Nmap is a versatile tool, widely used by IT, network and cybersecurity professionals for diagnostics, network discovery and security auditing. This tutorial is aimed at those who are new to these fields and wish to learn the basics of Nmap. A basic knowledge of system and network administration is recommended.


You'll learn the basics of Nmap, how to perform port scans, identify active hosts on a network, detect service versions and operating systems, perform vulnerability scans, and much more. Each section includes detailed explanations and practical examples to help you master the use of Nmap in a variety of contexts.


By the end of this tutorial, you'll have a solid understanding of Nmap and be able to use it effectively to improve the security and management of your networks. Enjoy your reading.


## 1 - Introduction to Nmap: What is Nmap?


### I. Presentation


In this first section, we'll take a look at the Nmap network scanning tool. We'll look at the key elements you need to know about this tool and how it works in general. This will help us to better understand the rest of the tutorial.


### II. Introducing the Nmap tool


Nmap, for _Network Mapper_, is a free, open-source tool used for **network discovery, mapping and security auditing**. It can also be used for other tasks such as **network inventory, diagnostics or supervision**.


It can determine whether hosts on a targeted network are active and reachable, which network services are exposed, which versions and technologies are in use, and other useful analysis information. Nmap can be used to scan a single service on a specific machine, or across large swathes of the network, up to the entire Internet.


Nmap's strengths are many:



- Powerful and flexible**: Nmap can scan large networks and use advanced detection techniques. It supports UDP, TCP, ICMP, IPv4 and IPv6, and can perform version detection, vulnerability scans or protocol-specific interactions. Its architecture is modular, thanks in particular to NSE (Nmap Scripting Engine) scripts, which we'll look at later in this tutorial.
- Ease of use**: official documentation is abundant and of the highest quality. Numerous community resources are also available to help you get started.
- Popularity and longevity**: Nmap has been a reference in its field since 1998. The current version, at the time of this update, is 7.95. Although other tools exist for specific tasks, Nmap remains a must-have for network mapping and analysis.


**Nmap at the movies**


Nmap is one of the few security tools to have acquired a certain notoriety among the general public. It appears in the film _Matrix Reloaded_, in an emblematic scene where Trinity uses it to hack into a system:


![nmap-image](assets/fr/01.webp)


matrix: Reloaded scene featuring Nmap


He also appears in other cinematographic works.


**Feedback


As a system administrator and then cybersecurity auditor and pentester, **I use Nmap on an almost daily basis** and I **regularly recommend** it to system administrators wishing to strengthen their command of networks and improve their diagnostic capabilities.


### III. High-level operation


Nmap is available for Linux, Windows and macOS. It is mainly written in C, C++ and Lua (for NSE scripts). It is mainly used on the command line, although graphical interfaces such as Zenmap are also available. However, we strongly advise you to start with the command line to better understand how it works.


A simple example:


```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```


This command will be explained in detail later. In this tutorial, we'll be using Nmap on Linux, but its uses are similar on other systems. Under Windows, Nmap relies on the **Npcap** library (replacing the now obsolete WinPcap) to capture and inject network packets.


Nmap is used like a conventional binary, such as `ls` or `ip`. Some advanced features may require elevated rights, as the tool sometimes manipulates packets in unconventional ways to provoke specific reactions on target systems (notably for service or vulnerability detection).


### IV. Impacts of using Nmap


Before using Nmap, it's essential to be aware of its potential impact on networks and systems:



- It can send **thousands or even millions of packets** in a short space of time, which can saturate certain network infrastructures.
- It can generate **malformed or non-standard** packets, likely to disrupt certain equipment (especially industrial systems).
- It can produce **attack-like behavior**, which can trigger alerts in security systems (firewalls, IDS/IPS, etc.).


Generally speaking, **Nmap is a very talkative tool**, as it generates a lot of traffic in order to extract as much information as possible. It is therefore advisable to fully understand how it works before using it on sensitive or production environments.


### V. Conclusion


This section introduces Nmap and its main features. We've seen that it's an essential, powerful and flexible network mapping tool. We've also discussed how it works and the precautions you need to take when using it, to set the scene for the following parts of the tutorial.


## 2 - Why use Nmap?


### I. Presentation


In this section, we'll take a look at the main uses of the Nmap network scanning tool. We'll see that it's a tool that's widely used in many contexts and professions, and that having it in your toolbox and knowing how to master it is definitely a useful skill.


### II. Using Nmap for diagnostics and supervision


Nmap can be used for network diagnostics and, more broadly, for monitoring. In the same way that a ping can be used to determine whether two hosts are communicating, Nmap can be used to quickly determine whether a host is active, or whether a particular service is operational. Thanks to [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), we can obtain precise data concerning a host's response time, the route taken by packets, the response made by a specific service, etc.


The following command and result can be used, for example, to quickly find out whether a web server on host **192.168.1.18** is active and responding correctly:


```
nmap --open -p 80 192.168.1.18
```


![nmap-image](assets/fr/02.webp)


*Use Nmap to retrieve web service status from a remote server.*


So, using Nmap goes further than the famous "ping test" during debugging or diagnostic phases. We'll see later that there are several methods used by Nmap to identify which service is listening on a given port, including its version.


### III. Using Nmap for network mapping


As a _Network Mapper_, network mapping is the main objective of this tool. It can be used within a local network, or across multiple networks, subnets and VLANs, to list all reachable hosts and services. Nmap makes this task much faster and more efficient than any manual method.


For example, the following command can be used to quickly identify active hosts on the **192.168.1.0/24** network:


```
nmap -sn 192.168.1.0/24
```


*Note: the `-sP` option is obsolete and has been replaced by `-sn`.*


![nmap-image](assets/fr/03.webp)


*Using Nmap to discover reachable hosts on a network*


We'll see later that there are several methods used by Nmap to determine whether a host can be considered "active", even if it doesn't a priori expose any services.


### IV. Using Nmap to evaluate a filtering policy


Nmap has the advantage of being factual: its results make it possible to establish concrete findings, unlike any architecture document or filtering policy. It is a key tool for assessing the effectiveness of information system compartmentalization, as it allows you to **verify whether the filtering policy is actually being applied**.


In a corporate network, best practice dictates that systems be segmented according to their role, criticality or location. Filtering rules (often implemented via firewalls) must restrict communications between zones. But these configurations are often complex and prone to errors.


So, to validate that the policy has been respected, nothing beats a concrete test. For example, you can check that sensitive administration services (SSH, WinRM, MSSQL, MySQL, etc.) are not accessible from a user zone.


The use of **Nmap to test the filtering policy** should be systematic before such a policy is put into production. Unfortunately, this check is often neglected.


In my experience, many configuration errors go unnoticed in the absence of validation tests. A simple error in an IP range or a rule oversight can leave a supposedly isolated zone vulnerable.


### V. Using Nmap for security auditing and penetration testing


Nmap has **many useful features for security assessment**, penetration testing (pentests), and unfortunately also for attackers.


Network discovery functions are crucial for an attacker, who needs to understand the network topology after an initial compromise. But Nmap offers much more than this: it integrates a scripting engine, **many of which are dedicated to vulnerability detection**.


For example, this command can be used to check whether an FTP service allows an anonymous connection, without having to connect manually:


```
nmap --script ftp-anon -p 21 192.168.1.18
```


![nmap-image](assets/fr/04.webp)


*Using an NSE script to check for anonymous FTP authentication via Nmap.*


Nmap vulnerability detection is one of the first steps in an audit or penetration test. It enables you to quickly identify certain weak points and optimize your analysis efforts.


But beware: **vulnerability scanning tools have their limits**. Nmap only covers a fraction of threats, and does not guarantee that a system is safe if no problems are detected. It is therefore essential to **understand how the scripts used work** and not to rely solely on their verdict.


### VI. Conclusion


We've seen that mastering Nmap can cover a wide range of use cases, from diagnostics and monitoring to mapping, security policy evaluation and vulnerability scanning. In the next section, we'll get down to the nitty-gritty and install Nmap.



## 3 - Installing and configuring Nmap


### I. Presentation


In this section, we'll learn how to install the Nmap network scan tool on Linux and Windows OS. At the end of this section, we'll have everything we need to start using Nmap for future modules. Finally, we'll see what privileges it may require when used and why.


### II. Installing Nmap under Linux


Nmap was originally designed to run on GNU/Linux operating systems. As a result, and thanks to its longevity and popularity, you'll find it in all the official repositories of the major Unix distributions. In this tutorial, I'll be using a Debian-based operating system [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). But you can use it in exactly the same way from a classic Debian, CentOS, Red Hat or whatever!


Under Debian, to check that Nmap is present in your current repositories, you can use the following command:


```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```


The answer here clearly indicates that the "nmap" package exists in the repositories (here, those of Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). From now on, you can install Nmap via the usual installation commands, nothing disarming for the moment 🙂:


```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```


To check that Nmap is installed correctly, we will display its version:


```
nmap --version
```


Here is the expected result:


![nmap-image](assets/fr/05.webp)


result of displaying the current version of Nmap._


Note the presence in this display of the "libpcap" (_Packet Capture Library_) library and its version. Also used by Wireshark, "libpcap" is used by Nmap to create and manipulate packets and listen to network traffic.


### III Installing Nmap on Windows


To install on a Windows operating system, start by downloading the binary from the official site (and no other!):



- Nmap download page on the official website: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)



You will then need to download the binary named `nmap-<VERSION>-setup.exe`:


![nmap-image](assets/fr/06.webp)


nmap for Windows installation binary download page


Once you have this binary on your system, simply run it to install Nmap. This is a straightforward installation, and you can leave all options as default.


My reflex is to uncheck the "zenmap (GUI Frontend)" box. This is a graphical Interface for Nmap that I don't use and won't be covered in this tutorial, but feel free to try it out once you've mastered the Nmap command-line tool!


![nmap-image](assets/fr/07.webp)


optional deselection of Zenmap when installing Nmap on Windows


At the end of the Nmap installation, a second installation is proposed: that of the "Npcap" library:


![nmap-image](assets/fr/08.webp)


installation of the "Npcap" library when installing Nmap under Windows


This is the library on which Nmap relies to manage network communications, i.e. building, sending and receiving network packets. You've probably already come across this library if you use Wireshark on Windows, since it also uses it and requires installation.


As with Linux, you can validate that Nmap is installed by opening a Command Prompt or a [Powershell] terminal (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") and typing the following command:


```
nmap --version
```


Here is the expected result:


![nmap-image](assets/fr/09.webp)


result of displaying the current version of Nmap._


Nmap is now installed on Windows. You can use it in exactly the same way as on Linux, by following this tutorial.


### IV. Local privileges required to use Nmap


But by the way, when using Nmap, **is it necessary to have elevated local privileges on the system?** The answer is: **it depends**.


In its very basic form, i.e. without going very far in using its options, Nmap doesn't necessarily require privileged rights. However, you will soon realize that it is better to use Nmap in a privileged context ("root" under Linux, "administrator" or equivalent under Windows) to be able to use it to its full potential, at the risk of getting an error message like this one:


![nmap-image](assets/fr/10.webp)


error message under Linux when Nmap options require root rights._


Whether on Linux or Windows, there are many cases where Nmap will ask you for privileged access. The main reasons are as follows (non-exhaustive list):



- Constructing "raw" network packets**: Nmap is capable of a wide range of scanning methods, including advanced packet manipulation and construction. This is the case, for example, when we want to perform TCP SYN scans, which don't respect the classic _Three-way handshake_ of TCP exchanges. To do this, Nmap needs to use functions other than those native to operating systems, which only know how to respect good practice in network communications (it calls on the "Npcap" and "libcap" libraries seen above). It's because Nmap doesn't do things in the "standard" way that it's able to deduce certain information about OSes, services and certain vulnerabilities.



- Listen to network traffic**: some of Nmap's options require it to listen to the network in order to retrieve certain information. This action is considered sensitive on operating systems, since it also allows you to listen in on the communications of other applications on the system. Just like Wireshark, Nmap needs specific privileges to do this, which are easier to obtain by being directly in a privileged session.



- Listening on privileged ports**: on operating systems, ports from 0 to 1024 (TCP as well as UDP) are said to be privileged, i.e. they are somehow reserved for very specific uses and therefore protected. Although this is a somewhat obsolete reason today, it is still necessary to have certain privileges to listen on these ports, which Nmap may have to do depending on how it will be used.



- Sending UDP packets:** Similarly, listening to a network application on UDP ports (a stateless protocol) requires privileged rights on operating systems. A privileged session will therefore be required if you wish to perform a UDP scan, for which Nmap will have to listen for a response in order to analyze the replies to its scans.



To be more precise, it is possible, at least under Linux, to run Nmap with all its functions and options without actually being root. This is achieved by granting the right _capabilities_ to the binary. However, this requires advanced manipulation and may not be as practical as running Nmap directly with privileges. Also, this approach is less common and can pose security problems if misconfigured.


However, this is a bit of a departure from our Nmap tutorial, so we'll dispense with it for now.


For the rest of this tutorial, assume that Nmap is always run as "root" (from a shell as "root" or via the "sudo" command), or in an administrator terminal under Windows, even if this is not indicated. Otherwise, you may experience subtle but noticeable differences from the tutorial.


### V. Conclusion


That's it! Nmap is now installed on our operating system and ready to use, requiring no further configuration. This section concludes the introduction and presentation of Nmap. I hope it's made your mouths water, and that you're eager to start practicing.


On a more serious note, we now have a better idea of what the Nmap mapping tool is and what its most common uses are, as well as its limitations. Let's move on!



## 4 - TCP and UDP port scans with Nmap


### I. Presentation


In this section, we'll learn how to perform our first port scans using the Nmap network scanning tool. We'll see how to use it to compile a list of network services exposed on a host, whether using TCP or UDP protocols.


From now on, remember to scan only hosts in a controlled environment for which you have explicit authorization.



- As a reminder: [Penal Code: Chapter III: Attacks on automated data processing systems](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)



**If you don't have one to hand**, I recommend the following free solutions, which are just the thing!



- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Hacking training platform, Hack The Box constantly provides vulnerable systems for you to attack as you see fit. Several hundred systems are available, but a renewed pool of 20 machines is offered free of charge all year round, with access via an OpenVPN VPN.



- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: This platform offers numerous intentionally vulnerable systems for download, which can be used via VirtualBox (also a free solution) or other means. Once downloaded, there's no need for a VPN - everything is local.



Also, you're free to **create a virtual machine** on your favorite operating system and install various services on it as test targets. The advantage here will be that you'll also be able to see what's happening on the server side during a scan, especially with Wireshark, and have a hand in the local firewall when we do more advanced tests.


Let's get practical!


### II. Scanning a host's TCP ports via Nmap


#### A. First TCP port scan with Nmap


We're now going to perform our first scans via Nmap. Our objective here is simple: we want to find out what services are exposed by the web server we've just deployed, to see if there's anything unexpected, such as an administration service that shouldn't be accessible, or the exposure of a port of an application that we thought was decomissioned.


In my example, the host to be scanned has the IP address "192.168.1.18":


```
nmap 192.168.1.18
```


Here is a possible result. We see a classic Nmap return with a lot of information:


![nmap-image](assets/fr/11.webp)


results of a simple TCP scan performed with Nmap._


Taking a quick look at this result, we understand that ports TCP/22 and TCP/80 are accessible on this host.


By default, and if you don't tell it to, Nmap will only scan TCP ports.


#### B. Understanding the results of a simple Nmap scan


Let's go a step further, however, to understand this output: each line is important, firstly to know what has just been done, and secondly to properly interpret the scan results themselves.


The first line is essentially a reminder of the scan version and date (useful for logging and archiving after all!):


```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```


The second line shows the start of scan results for the host "debian.home (192.168.1.19)". This information will be useful when we start scanning several hosts at the same time:


```
Nmap scan report for debian.home (192.168.1.19)
```


The third line tells us that the host in question is "Up", i.e. active:


```
Host is up (0.00022s latency).
```


Finally, Nmap informs us that 998 TCP ports identified as closed are not displayed in the:


```
Not shown: 998 closed tcp ports (conn-refused)
```


This saves us almost 1,000 lines of output looking like:


```
1/tcp closed
2/tcp closed
3/tcp closed
…
```


Thanks to him for sparing us this!


Why 998 "closed" ports? Adding the 2 open ports makes 1000, and that's the number of ports Nmap will scan in its default configuration, not the 65535 existing TCP ports! We'll see later that this is entirely and easily customizable. But if the targeted host has a service listening on a rather exotic port, this "default" scan won't uncover it.


Following this information, we find what is most interesting: a table organized according to the three columns "PORT - STATE - SERVICE":



- The first "PORT" column simply indicates the targeted port/protocol, and it's important here to look at whether it's a TCP port (`<port>/tcp`) or UDP (`<port>/udp`).



- The "STATE" column indicates the status of the network service discovered on this port and determined by Nmap on the basis of the response obtained. This can be "open", "closed", "filtered" or "unknown". We'll see later how Nmap distinguishes between these different states.



- The "SERVICE" column indicates the service exposed on the port in question. Please note, however, that we have not used active service discovery options here. Nmap relies on a local reference between a port/protocol and the supposedly assigned service: the "/etc/services" file



If you take a look at the "/etc/services" file on a Linux system, you'll find a "port/protocol - service" link similar to the one displayed by Nmap:


![nmap-image](assets/fr/12.webp)


extracts the contents of the "/etc/services" file under Linux._


It's important to understand that, for the time being, Nmap hasn't performed any active service discovery. For example, it would have been unable to identify the SSH service behind a TCP/80 port if this had been the case. Hence the importance of knowing how to use the right options - it's coming soon!


Knowing how to interpret Nmap's output is an important part of mastering the tool. The good news is that this output will be largely the same, whatever options you use.


#### C. Under the hood: network analysis via Wireshark


If you take a close look at what's happening on the network Interface of the host scanning the server, or on that of the server itself, Nmap's actions will be much clearer. That's what we're going to do here.


What I can show you here is just part of what's visible in Wireshark. If you want to go further, feel free to do a network capture yourself during a scan, and then browse through what's been captured.


In this test, my scan host (192.168.1.18) and my target host (192.168.1.19) are on the same local network.


Nmap starts by finding out whether the target host is active on the local network by sending an ARP request. If it receives a response, it knows that the host is active and begins its network scan:


![nmap-image](assets/fr/13.webp)


_ARP request issued by Nmap to determine whether a target host is present on the local network._


If the host to be scanned is on a remote network, Nmap starts by sending a ping request and tries to reach some of the most frequently exposed ports (TCP/80, TCP/443):


![nmap-image](assets/fr/14.webp)


ping request issued by Nmap to determine whether a target host is reachable on a remote network


If it obtains a response to any of these tests, it considers the target to be active.


Once Nmap has determined that its target is active, it will try to resolve its domain name with the DNS server configured on the network card:


![nmap-image](assets/fr/15.webp)


dNS resolution on Nmap scan target


Now that Nmap has identified its target and knows it's active, it begins its TCP port scan:


![nmap-image](assets/fr/16.webp)


tCP SYN packet transmission and RST/ACK reception during Nmap scan


To do this, it will, on each TCP port in its default range, **send TCP SYN packets and wait for a response**. In the screenshot above, it receives TCP RST/ACK packets from the scanned server, meaning "move along, nothing to see here" - in other words, these ports are closed. As we saw in the result, this will be the case for most of the ports scanned. With two exceptions:


![nmap-image](assets/fr/17.webp)


response to a TCP SYN packet sent on port 22, active on the scan target


In the screenshot above, we see a TCP SYN/ACK packet sent by the target host**. The port is active and exposes a service. Nmap acknowledges receipt of the response, then terminates the connection (TCP RST/ACK). **This is how it knew that port TCP/22 was active**.


We have seen here that Nmap respects the "Three Way Handshake" when scanning a TCP network. For performance reasons, it is possible to ask it not to respond to the server's return, thus saving several thousand packets when scanning a large network. But we'll look at these options and optimizations later in the tutorial.


We now have a better idea of how to do a TCP scan and what actually happens when it's performed. We've also seen that, by default, Nmap performs a TCP port scan on a limited number of ports.


### III. Scanning UDP ports with Nmap


#### A. First UDP port scan with Nmap


Now let's see how to scan a host's UDP ports. As we've seen, by default Nmap will always scan TCP ports. This can mean missing out on a lot of information if we're not aware of it.


As a reminder, for the purposes of this test, my scan host (192.168.1.18) and my target host (192.168.1.19) are on the same local network.


```
nmap -sU 192.168.1.19
```


Here, the return obtained has the same format as for a TCP scan, but the active services displayed are in `<port>/UDP`, as requested!


![nmap-image](assets/fr/18.webp)


result of a simple UDP scan performed with Nmap._


The "-sU" option is used to tell Nmap that you want to work on UDP, rather than TCP as is the default.


By the way, you'll probably notice that Nmap requires "root" rights for UDP scans, as mentioned earlier in the tutorial.


note: Since the latest versions of Nmap, it is always recommended to run UDP scans with administrator privileges to ensure reliable results, as some features require raw access to network sockets._


UDP scans can take a very long time (1100 seconds to scan 1000 ports in my example), due to the absence of the "Three Way Handshake" in UDP, which means that Nmap will wait for a return for each UDP packet sent, and will determine the port as "closed" only if there is no return after a certain time (timeout). This response from scanned hosts is not systematic and is often limited in terms of the number of responses per second, to avoid certain amplification attacks. This is in contrast to TCP, where there is an immediate response from the scanned host, whether the port is open or closed. We'll see later how to optimize this.


A second difficulty with UDP is **that services don't always respond to incoming packets**, quite simply because this isn't always necessary and it's the principle of UDP. When this is the case, and no ICMP "port unreachable" is received, the service is marked as "open|filtered" by Nmap, as shown in the screenshot above.


#### B. Under the hood: network analysis via Wireshark


As with our TCP scan, let's take a closer look at what happens at network level during a UDP scan using a Wireshark analysis. Nmap's behavior in determining whether a host is active is the same.


The only real difference when scanning UDP is that Nmap won't wait for a "Three Way Handshake", since this mechanism doesn't exist in UDP (stateless protocol):


![nmap-image](assets/fr/19.webp)


uDP packet transmission and ICMP reception (port unreachable) during Nmap scan


We can see on the above screenshot that Nmap will send a large number of UDP packets, and receive for most of them an ICMP "Destination unreachable (Port unreachable)" packet in response. This is normal, as it is the appropriate response defined by [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") when a UDP port is unreachable:


![nmap-image](assets/fr/20.webp)


extract from RFC 1122._


Let's take a closer look at this Wireshark capture, which shows **the three possible scenarios** in UDP:


![nmap-image](assets/fr/21.webp)


network capture during a UDP scan on different ports with Nmap._


The three cases are as follows:



- The first exchange is made up of packets no. 3, 4 and 8, 9. Nmap sends UDP packets on the classic SNMP port and therefore **constructs protocol-compliant packets in advance**. It then obtains a response from the server (packets no. 8 and 9). Result: Nmap has received a response, the service is "open".



- The second exchange consists of packets 6 and 7. Nmap sends an "empty" UDP packet (with no protocol structure) to port UDP/165, and receives an ICMP packet in reply: "Destination unreachable (Port unreachable)". Result: Nmap has received a (negative) response, the host is up, but the service it tried to reach is not operational on this port, which will be marked as "closed".



- The last exchange consists of packet no. 12: Nmap sends an "empty" UDP packet to port UDP/1235. There is no response, not even an explicit refusal from the scanned host. Result: Nmap marks the port as "open|filtered", as it is unable to tell whether this is due to the presence of a firewall, configured not to respond, or to an active UDP service which returns no response anyway (not mandatory in UDP).



Here is the result displayed by Nmap following these three cases:


![nmap-image](assets/fr/22.webp)


possible results of a UDP scan performed via Nmap._


We now have a better idea of how to do a UDP scan and what actually happens when it's performed. So far we've just been using Nmap in a very simple way, without really deciding which ports to scan, but that's about to change!


### IV. Fine-tuning port scanning with Nmap


#### A. Reminder of Nmap's default behavior


As we've seen, Nmap itself chooses the number and ports to scan if you don't specify any options. This is the "default" configuration used by Nmap when you don't tell it exactly what to do. These default options are designed to give an idea of the main ports exposed, these being selected by frequency of exposure (most common or frequent ports) rather than in numerical order (port 1, 2, 3, etc.) and also to avoid starting a scan of the 65535 possible ports if you don't specify the appropriate options, which would be too long and wordy for a "default" use case.


**How are these ports chosen?


The 1000 ports scanned in the default mode are chosen according to their frequency of occurrence. These statistics are maintained by Nmap and updated in the same way as the binary itself and its scripts (modules). You can view these statistics yourself in the "/usr/shares/nmap/nmap-services" file:


![nmap-image](assets/fr/23.webp)


extracted from the file "/usr/shares/nmap/nmap-services"._


Here, in the third column, we see what looks like probabilities (between 0 and 1) or a percentage distribution. This is the frequency of occurrence of each port/protocol pair. We can see that the best-known ports (FTP, SSH, TELNET and SMTP in this extract) have a much higher value than the others.


#### B. Precisely specify target ports for an Nmap scan


However, in the real world, we may need to scan only a specific port, or several ports, or a specific range of ports. Nmap makes it easy to do just that, in a uniform way for both UDP and TCP scans.


**Scan a specific port via Nmap**


If we wish to scan a single port, and not 1000, we can specify this port via Nmap's "-p" or "--port" option:


```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```


As a result, the scan will naturally be much faster and Nmap will only emit the packets needed to detect whether the host is active, and then whether the specified port is reachable. This saves time if you just want to run a quick test to see if the web service on your showcase site is still up.


**Scan multiple ports via Nmap**


In the same way, we can specify several ports to Nmap, using the same option and concatenating the specified ports with a comma:


```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```


Regardless of the order, Nmap will check all these ports, and only those on the targeted host. You'll notice in Nmap's output that it **explicitly tells us all ports and their status**, even if they're "closed". Unlike the default behavior, where this complete output would have taken up far too much space:


![nmap-image](assets/fr/24.webp)


*Result of an Nmap TCP scan on the indicated ports.*


**Scan a range of ports


If the number of ports you wish to scan is too large, you can specify them by range, for example:


```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```


Of course, you can mix and match as you see fit, for example:


```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```


**TCP and UDP port scanning


You can also perform UDP and TCP scans at the same time, on selected ports:


```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```


You'll notice in this last example the presence of "U:" to indicate a UDP port and "T:" to indicate a TCP port. Here is a possible output of this type of scan:


![nmap-image](assets/fr/25.webp)


*Result of a TCP and UDP port scan with Nmap.*


Now that's an interesting way to customize your scans!


**Scan all ports


Finally, it's possible to specify much larger or smaller ranges to Nmap. We have seen that the default list selected by Nmap contains 1000 ports. We can also ask for the top 100 most frequent ports, or the top 200, using the "--top-ports" option:


```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```


Finally, we can ask it to scan all possible ports (all 65535), using the "-p-" notation:


```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```


The latter will take longer, especially with UDP, but you'll be sure not to miss any open ports.


*Note: The "-p-" option is the recommended method for scanning all TCP ports. For UDP scans, it is advisable to limit the number of ports for performance reasons, as complete scans of all UDP ports can take a very long time.*


Later in the tutorial, we'll see how to optimize the speed of Nmap scans to suit our needs, which will be particularly useful for scans on all TCP and UDP ports.


### V. Conclusion


In this section, we've finally got some hands-on practice, so we now know **how to use Nmap in a basic way to scan a host's TCP and UDP ports**. We've also looked in detail at what's happening at network level and **how Nmap determines whether a TCP or UDP port is active or not**. Finally, we know how to finely select the ports we want to scan and **what Nmap's default options actually do**. In what follows, we'll reuse this knowledge and apply it to scanning an entire network, including global mapping and network discovery.



## 5 - Network mapping and discovery with Nmap


### I. Presentation


In this section, we'll learn how to use the Nmap network scan tool to map your network. We'll see how effective it can be in this task, through its various options. Finally, we'll look at different ways of specifying the targets of our scans to Nmap.


In particular, we'll be using what we learned in the previous section about how Nmap determines whether a host is active and reachable.


As mentioned in the introduction to Nmap, this is a Network Mapper. As such, it's the perfect tool for drawing up a list of accessible hosts on a network, whether local or remote.


**Return of the author:**


In fact, as a cybersecurity auditor and pentester, I use Nmap systematically when carrying out internal penetration tests to find out where I am, who my neighbors are on the local network and what other networks are accessible, as well as the systems located on them. My objective is simple: to map the network, determine the size of the information system and, in particular, sketch out its attack surface.


Network mapping can also be useful in the context of network diagnostics, supervision, asset mapping (are you really sure that your IS is made up solely of what's in the Active Directory or in your GLPI/OCS Inventory? It can also be used to detect the presence of Shadow IT in your information system.


### II. Using Nmap to scan a network range


#### A. Discovering a network with an Nmap scan


We'd now like to move up a gear and analyze our entire local network. Nothing could be simpler: all we need to do is reuse the commands we saw in the previous section, but specify a CIDR instead of a simple IP address.


A CIDR (**Classless Inter Domain Routing**) is the "classic" notation for specifying a network range and its extent (using the mask). For example, "192.168.0.0/24" is a "translation" of the decimal mask notation "255.255.255.0".


To use Nmap by specifying a CIDR, we can use it as follows:


```
# Scan a CIDR
nmap 192.168.0.0/24
```


It is also possible, as with ports in the previous section, to specify multiple hosts, multiple networks, or range:


```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```


Here's an example of the results we might get when running a scan on a network:


![nmap-image](assets/fr/26.webp)


results of an Nmap scan to map several networks


In particular, we see several active hosts, and each host section begins with a line like this:


```
Nmap scan report for <name> (<IP>)
```


This allows us to clearly see to which host the following results refer. The very last line is also important:


```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```


We know that, on the networks scanned, Nmap discovered 5 active hosts.


#### B. Under the hood: network analysis via Wireshark


We're now going to take a closer look at what happens at network level during a network discovery performed via Nmap.


As we saw in the previous section, by default Nmap will use the ARP protocol to detect the presence of hosts on the local network:


![nmap-image](assets/fr/27.webp)


aRP packets captured when scanning a local network using Nmap and its default options


It is thus able to detect virtually all hosts on the local network, since the response to an ARP request is generally provided by all hosts active on the network and does not appear suspicious in any way.


For remote networks, Nmap uses a combination of techniques:


![nmap-image](assets/fr/28.webp)


iCMP and TCP packets captured when scanning a remote network using Nmap and its default options


To be more precise, Nmap uses an ICMP echo packet (the classic case of pinging) and an ICMP Timestamp packet, usually used to calculate packet transit times. It hopes to get a response from hosts on remote networks.


But there's more to it than that. You can see in the Wireshark capture above that **TCP SYN** packets are systematically sent on TCP/443 ports of every potential host on the networks to be scanned, as well as **TCP ACK** packets on TCP/80 port.


**Why send TCP packets to ports as part of network discovery?


Sending a SYN packet to a given port allows Nmap to **determine whether a service is listening on that port**. If a host replies to a SYN packet with a SYN/ACK packet, this indicates that it is active and that a service is listening on that port. Nmap therefore tries its luck on this service, **even if no response to the ping has been obtained**.


Sending an ACK packet to a given port allows Nmap to **determine whether a firewall is present on that host**. If a host responds to an ACK packet with an RST (Reset) packet, this indicates that a firewall is probably present on that host and blocking unsolicited traffic. The host thus betrays its presence on the network, even if it has not responded to other requests.


It is important to note, however, that firewall detection using this technique may not be perfectly reliable in all cases. Some hosts may generate RST responses for reasons other than the presence of a firewall, such as specific service or operating system configuration. In addition, modern firewalls can be configured not to respond to discovery attempts of this type.


We've now come a long way and can perform basic network discovery. We're now going to look at a few more options that will give us greater control over Nmap's behavior.


### III. Network discovery without port scanning with Nmap


As you may have noticed, by default Nmap **performs a port scan following its discovery of an active host**, which adds a huge amount of packets and waiting for responses to our scan. If you have 5 hosts on your network, Nmap will try to check the status of around 5,000 ports, which will take longer.


However, it is possible to use Nmap's options to perform **only a discovery of active hosts** on a network, without discovering their services.


If we only want to know which hosts are reachable, without any information on the services and ports they expose, then we can use the "-sn" option to perform **only a scan using ICMP Echo (ping) and ARP requests**. In other words, disable port scanning altogether:


```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```


Here is the result of an Nmap network discovery performed without port scanning:


![nmap-image](assets/fr/29.webp)


Result of a network discovery without port scanning with Nmap.


We have already mentioned the possible limitations of using ICMP alone for host discovery (for remote networks). That's why Nmap also uses a few tricks that can betray the presence of a firewall or specific service on hosts. With the help of options, we can reuse these tricks and even extend them, without having to start again with a complete port scan of every host discovered.


To do this, we'll use the "-PS" (TCP SYN) and "-PA" (TCP ACK) options, which will allow us to specify the ports we wish to join as part of our host discovery, as well as the "-PP" option:


```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```


This scan already ensures that host discovery is a little more complete than with the default options.


We're starting to get quite comprehensive commands, using multiple options. This is because we know how Nmap works and the limitations of its "default" options, which can sometimes cause us to waste time or miss out on important elements. That's the whole point of taking the time to master it!


To detail the options of our last order:



- "`-sn`: disables port scanning for each active host discovered by Nmap.



- "`-PP`: enables ICMP echo (ping scan) for host discovery.



- "`-PS <PORT>`": send a TCP SYN packet on the indicated port(s) to detect any active service betraying the presence of a host that has not responded to the ping.



- "`-PA <PORT>`": send a TCP ACK packet on the port(s) indicated to detect any active firewall betraying the presence of a host that has not responded to the ping.



In the example above, I specify the ports I consider to be the most frequently exposed in my Nmap contexts for the "-PS" option. These different ports will then be tested on each host, not to see if the service they host is really active, but to see if this allows us to discover a host that hasn't responded to our ICMP Echo while still being active (via a response from the service or the host's firewall).


Here's what can be seen in a network capture taken at the time of such a scan, in this case an extract on a single target host:


![nmap-image](assets/fr/30.webp)


packets sent by Nmap during advanced network discovery, without port scanning


We find our TCP SYN packets, our TCP ACK on port TCP/80 and our ICMP echo. Nmap will perform all these tests for each host targeted by our network discovery scan.


### IV. Using a file of assets to target with Nmap


Specifying targets can quickly prove complex in real-life information systems, which can sometimes be made up of dozens or hundreds of networks, subnets and VLANs. This is why it's easier to use a file as a source for Nmap than to specify them one by one on the command line.


To begin with, create a simple file containing one entry per line:


![nmap-image](assets/fr/31.webp)


file containing one target (host or network) per line


Next, we can use all the Nmap options seen so far and specify the "-iL <path/file>" option:


```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```


Nmap will then include in its scan all the targets contained in our file.


If you want to be sure that all your targets will be taken into account, you can use the "-sL -n" option. Nmap will then only interpret the CIDRs and hosts in the file and display them to you, without sending any packets over the network:


```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```


This ensures that the list of hosts to be scanned is accurate.


One last important tip I'd like to share with you concerns **host or network exclusion as part of a scan**. This need to exclude a host may be necessary in a number of cases, particularly if we want to be sure that **a sensitive component of the information system is not disturbed or disrupted by our scans**.


Frequent examples of such needs are when a company owns industrial (PLC) or healthcare equipment. Such equipment is sometimes poorly designed, and not at all intended to receive poorly formatted packets, or too many of them. For obvious reasons of availability or business/human risk, it is preferable to exclude them from testing.


To exclude IP addresses or networks from our scan, we can use Nmap's "--exclude" option, for example:


```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```


In this example, I'm scanning the network "192.168.1.0/24" but excluding the host "192.168.1.140" located there. No packets will be sent by Nmap to this host. Another example with subnet exclusion:


```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```


Similarly, I scan the large network "10.0.0.0/16", but the network "10.0.100.0/24" will not be scanned. Again, I recommend using the "-sL -n" option to get a very clear view of which hosts will be scanned and which will be excluded from the scan, especially if you're operating in a sensitive context.


### V. Network discovery and port scanning


We can now combine what we've learned in this section with what we learned in the previous section about port scan options. By default, we've seen that Nmap will scan the 1000 most frequent ports on every active host it discovers. We've seen how to prevent this behavior if we don't want it, but we can fully control it, and even extend it if it suits our needs.


For example, the following command will check for the presence of a listening service on port TCP/22 on each scanned host:


```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```


Nmap will first perform a network discovery to list the active hosts, and for each of them, check that a service is present on port TCP/22.


In the same way, we can perform a full scan of all TCP ports on every host discovered on the "192.168.0.0/24" network, excluding host "192.168.0.4" for example:


```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```


You're free to combine all the options we've learned so far to suit your own needs.


### VI. Conclusion


In this section, we've seen how to use Nmap to map the network using various options. We now have a fine-tuned understanding of the targets of our scans, as well as Nmap's port scan behavior and host discovery method. And most importantly, we know what Nmap's default behavior and limitations are, and how to use its main options to go further.


In the next section, we'll look at the mechanisms and options for discovering the versions of services and operating systems scanned by Nmap.



## 6 - Detecting service and operating system versions with Nmap


### I. Presentation


In this section, we'll learn how to use Nmap to discover and accurately detect the versions of services and operating systems used by scanned hosts. We'll take a detailed look at how Nmap accomplishes this task, as well as at the tool's limitations to better understand and interpret its results.


As we've seen in previous sections of this tutorial, by default, Nmap won't look to see what service is exposed on the ports it scans and considers open. So if you're listening to a web service on port TCP/22, Nmap will continue to report it as open, but as an `SSH` service. This is because it uses a [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) local to your system to look for a relationship between a port/protocol and the name of a service (the `/etc/services/` file).


In the majority of cases, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) will provide you with the correct information, as it is rare in a production environment to find such cases. However, the remaining cases will be situations where a classic service ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, etc.) is exposed on a non-classic port (e.g. 2022 for an SSH service), in which case Nmap won't find a match in its local database, or one that doesn't match reality, and you'll miss out on important information.


Fortunately, Nmap offers very precise options and mechanisms for discovering which exact service may be hiding behind an open port. It even has a database of queries and signatures to identify exact technologies and versions. In addition to services, Nmap can also identify the technology used and its version.


That's what we'll be looking at in this section.


### II. How to detect a technology or version


#### A. Reminder of how to identify a technology or version


Identifying a technology and a version involves retrieving the name of the service, CMS, application or software listening on the targeted port. For example, a web page is managed by a CMS (`WordPress`), run by a web service (`Apache`, IIS, Nginx) and hosted by a server (Linux or Windows). But how do you know which web service is running?


The classic methodology for finding out this information is _banner grabbing_, which simply consists of locating where the service in question displays this information and reading the data. Very often, in their default configuration or processing, services display their name and even their version as the first response after a connection.


![nmap-image](assets/fr/32.webp)


display a version as soon as a TCP connection is established by an FTP service


Here we see that a simple TCP connection to this service via `telnet` results in a TCP packet containing its technology and version.


Once you've got an idea of the type of service you're dealing with, you can also send specific commands or requests to that service to extract information from it. These requests/commands can also be sent blindly (without being sure they are the right type of service), in the hope that one of them will provoke a response from the service in question.


In other, more advanced cases, it is necessary to send specific packets to cause a reaction, such as an error, which will provide detailed information on the version or technology used.


As you can imagine, Nmap will use all these techniques to try and identify the exact type of service hosted on a port, as well as the name of its technology and version.


#### B. Understanding Nmap Probes and Matches


To carry out all these checks on each scanned port, Nmap uses a local database which is frequently updated (just like the binary or its modules). This is a text file of several thousand lines: `/usr/share/nmap/nmap-service-probes`.


This file is made up of numerous entries, all organized around two main guidelines:



- The `Probe`: this is the definition of the packet that Nmap will send in an attempt to provoke a reaction from the service to be identified. Think of it as a blind attempt like _Hello? Guten Tag? Hello? Um... Buenos Dias perhaps?_. As soon as the targeted service receives a probe it understands (i.e. speaking the correct protocol), it will respond to Nmap, which will then have confirmation of the type of service it is.



- Match": these are regular expressions that Nmap applies to the response obtained. If sending an HTTP GET request has provoked a response from the service, it will apply dozens of regular expressions to this response to identify the presence of, for example, the word `Apache`, `Nginx`, `Microsoft IIS`, etc.



There are a few other directives for specific cases, but the main ones for understanding how Nmap works and customizing its use are these. To make this theory part more concrete, here's an example:


![nmap-image](assets/fr/33.webp)


example of a Probe in Nmap's `/usr/share/nmap/nmap-service-probes` file


In the first line of this example, we see an easy-to-understand Probe named `GetRequest`. This is a TCP packet containing an empty HTTP GET request to the web service root using HTTP/1.0, followed by a line feed and an empty line.


The `ports` line tells Nmap for which port to send this Probe. This allows you to prioritize tests and save time.


Finally, we have two examples of `match`. The first, for example, will categorize the scanned web service as `ajp13` if the regular expression contained in this line matches the service response received.


To help you understand what Probes can look like, here's a list of some of the Probes you'll find in this file (there are 188 in all at the time of writing this tutorial).


![nmap-image](assets/fr/34.webp)


example of several Probes used by Nmap and present in the file `/usr/share/nmap/nmap-service-probes`._


The first two (called `NULL` and `GenericLines`) are of particular interest here, as they simply send an empty TCP packet or one containing a line break. Server services often announce themselves precisely as soon as a connection is received, without any specific action, command or request from the client.


Here's the case of a slightly more complex _match_:


```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```


The exact regular expression is contained here between the `m|` and the `|`, which delimits any regular expression in this file. Please take the time to read this entire example. You'll notice a selection in the regular expression: `([\d.]+)`, used to isolate a version. This example also defines other elements such as the product name `p/nginx/`, the retrieved version `v/$1/` and the CPE with version `cpe:/a:igor_sysoev:nginx:$1/`.


A CPE (Common Platform Enumeration) is a standardized notation system used to identify and describe software and hardware. This format enables more efficient management of vulnerabilities and security configurations, and above all a unified way of representing them, whatever the product in question. Here are two examples of CPE: `cpe:/o:microsoft:windows_8.1:r1` and `cpe:/a:apache:http_server:2.4.35`


Here we clearly identify their types `o` for OS, `a` for application, vendor, product, and versions.


So, in the event of a _match_ with one of these regular expressions, we'll retrieve not only the name of the service, but also its version and exact CPE, making it easier to find CVEs impacting this version. You'll find this information in Nmap's standard output, and you'll see that it's very useful for other purposes that we'll cover in a few sections.


The exact syntax of _matches_ and, more generally, of the directives in the `/usr/share/nmap/nmap-service-probes` file doesn't stop there, and may seem rather complex if you're not used to manipulating Nmap and its results. However, you should at least keep in mind its existence and general operation, which will come in handy later on when you wish to understand or debug a result, customize a scan or even contribute to Nmap development.


### III. Using Nmap to detect versions


Now we're going to use all this complex _Probe_ and _Match_ mechanics via a simple option: `-sV`. This simply tells Nmap: try to find out exactly which services and versions of ports you've set as open.


```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```


Here's a complete example of the result of such a command:


![nmap-image](assets/fr/35.webp)


results of Nmap's version detection of applications exposed on the network


Here we can see that Nmap has managed to identify all the versions of network services exposed by this target, and displays this information in a new `VERSION` column. It's possible to see quite precise information, even down to the operating system, if this information is part of the recovered signature.


To understand in detail what happens during a vulnerability scan, we can use the `--version-trace` option. This will provide a debug mode view, displaying the _Probe_ that led to the detection:


```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```


As a result, we'll have a lot of information to sort through. Try to identify lines beginning with `Service scan Hard match`. You'll then see lines like these:


```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```


We can clearly see which _Probes_ were used to detect the technology and version (in this case the `NULL` and `GetRequest` _Probes_), as well as the information retrieved.


### IV. Mastering tests and detection accuracy


We're now going to return to a directive in the `/usr/share/nmap/nmap-service-probes` file that we didn't look at earlier:


![nmap-image](assets/fr/36.webp)


probes `rarity` directive in the `/usr/share/nmap/nmap-service-probes`._ file


This directive is used to indicate the rarity (i.e. priority/probability) associated with a _Probe_. This notation from 1 to 9 allows you to control the completeness of the analysis performed by Nmap when sending _Probes_. In Nmap's "notation" system, a rarity of 1 provides information in the vast majority of cases, whereas a rarity of 8 or 9 represents a very special case, specific to a configuration or service that is rarely present.


To be clearer, in a default case, Nmap will send to each service to be identified the _Probes_ that have a rarity from 1 to 7. To give you a better idea of the distribution of _Probes_ by _rarity_, here's their count:


```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```


It may seem counter-intuitive, there are more `rarity` 8 and 9 than the rest. This is precisely because rarity 1 Probes are generic and work in the majority of cases, regardless of the service (remember the `NULL` Probe which simply sends an empty TCP packet). Whereas the more complex Probes are almost unique per service.


If we wish to manually manage the Probes we wish to use in our version scan, we can use the `--version-intensity` option. Here are two examples:


```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```


To finish on this subject, here's an example of _Probe_ 9 and 8:


![nmap-image](assets/fr/37.webp)


examples of Probe at rarity 8 and 9 in the file `/usr/share/nmap/nmap-service-probes`._


These two _Probes_ detect Quake1 and Quake2 servers (the video game). Interesting for the nostalgic side, but unlikely to be of much use in everyday life.


Depending on your needs for precision or speed, remember that this `rarity` principle exists and can influence the result.


### V. Using Nmap to detect operating systems


We'll now look at how Nmap can help us detect the operating systems of hosts scanned and detected on a network. To do this, use Nmap's `-O` (for `OS Scan`) option.


```
# Enable OS Scan
nmap -O 10.10.10.0/24
```


Here's an example of the results. Here, Nmap tells us it's probably a Linux OS, and offers us various statistics concerning its exact version.


![nmap-image](assets/fr/38.webp)


detection of the probability of identification of an operating system by Nmap


To achieve this, Nmap will use a multitude of techniques that work in a very similar way to _Probes_ and _Matches_ for technology and version detection. The main difference is that Nmap will use fairly "low-level" parameters of ICMP, TCP, UDP and other protocols. Here are two test examples for detecting a Microsoft Windows 11 operating system:


![nmap-image](assets/fr/39.webp)


examples of tests performed by Nmap to detect a Windows 11 OS


Let's face it, these tests are very difficult to interpret, and we're not going to try and understand them in depth in the context of an introductory Nmap tutorial. If you'd like to dig deeper into the subject, the file containing this information is `/usr/share/nmap/nmap-os-db`.


However, you need to be aware that OS detection is more a probability established by Nmap than a certainty.


### VI. Conclusion


In this section, we've learned how to use Nmap's options for detecting the technologies, versions and operating systems of scanned hosts and services. We now have a good understanding of how Nmap goes about obtaining this information remotely. We've also reviewed the options for managing verbosity and test accuracy, as well as the tool's limitations on these subjects.


In the next section, we'll learn how to use Nmap's NSE scripts to perform a security analysis of our information system. Take the time to reread the last sections if you need to, and don't hesitate to practice and delve into the bowels of the tool yourself to better master what we've learned so far.



## 7 - Security analysis: detecting vulnerabilities


### I. Presentation


In this section, we'll learn how to use the Nmap network scan tool to detect and analyze vulnerabilities on the targets of our scans. In particular, we'll look at the various options available to accomplish this task, and study the limits of the tool's capabilities in order to better understand and interpret its results.


In this first section, we'll take a look at Nmap's vulnerability scanner, and see how to use the basic vulnerability detection options. In the following sections, we'll take a closer look at how this feature works, and how it can be customized.


### II. Using Nmap to detect vulnerabilities


We now want to use the Nmap network scanner to detect vulnerabilities in the services and systems of our information system. This means that in addition to discovering active hosts, enumerating exposed services and detecting versions and technologies, Nmap will look for vulnerabilities.


To achieve this, Nmap relies on NSE (_Nmap Scripting Engine_) scripts, which can be seen as modules that enable a granular approach to testing.


With the right options, we'll ask Nmap to use its various NSE scripts on each service discovered, enabling us to discover:



- Configuration faults ;



- Additional and more advanced version and OS discoveries ;



- Known vulnerabilities (CVEs) ;



- Weak identifiers ;



- Characteristic elements of a malware infection ;



- Denial of service possibilities ;



- Etc.



As you can see, NSE scripts significantly extend Nmap's capabilities in terms of the network operations it can perform. And this to perform far more advanced tasks than ever before. The good news is that, as usual, these features can be used simply via an option and in a default context. This is what we'll see next.


### III. Example of a vulnerability scan


NSE scripts can be used when using Nmap to scan a single port on a host, all services on that host or all services detected on several networks. We can therefore use the options we're going to see in all the contexts we've studied so far.


To enable vulnerability scanning via a Nmap scan, we need to use the `-sC` option:


```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```


Remember that by default, if you don't specify anything, Nmap will only scan the 1000 most common ports. It won't detect vulnerabilities on the more exotic ports your targets might expose.


Before using this functionality on a production information system, I invite you to continue reading the tutorial. In the following sections, we'll look at how to better control the impact and types of tests that will be run.


By reusing what we've learned previously, we can, for example, be more comprehensive and scan all the TCP ports of a target:


```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```


Here's the result of an Nmap scan using NSE scripts:


![nmap-image](assets/fr/40.webp)


example of the results of a vulnerability scan on a host via Nmap._


Here we see the display of additional information of interest in the context of a vulnerability analysis:



- The FTP service can be accessed anonymously, and is not protected by authentication. The NSE script in charge of this verification tells us so, and even displays part of the FTP service's tree structure. Here we see that we have access to the `C` directory of the Windows system!



- The NSE script in charge of advanced web service retrieval displays the page title, giving us a better idea of what the web service is hosting.



- We also have a mini analysis of the SMB service configuration (scripts `smb2-time`, `smb-security-mode` and `smb2-security-mode`). The information is displayed a little differently, after the network scan result, to make it easier to read. In particular, this information indicates the absence of SMB exchange signatures. This configuration weakness allows the target to be used in an SMB Relay attack, a notable security flaw often exploited in intrusion/cyber-attack tests.



Of course, this is just one example. Nmap has NSE scripts for many services, targeting a wide range of vulnerabilities. We'll take a closer look at these possibilities in the next section.


To conclude this introduction to vulnerability scanning, here is a complete command for network discovery, TCP port scanning, version and vulnerability detection:


```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```


Here's a command that's starting to look like more realistic Nmap use cases!


### IV. Understanding Nmap's limitations in vulnerability scanning


Let's be clear: Nmap is not capable of carrying out a complete penetration test of your information system, or simulating a Red Team operation. It has several limitations that you need to be aware of if you are not to have a false sense of security:



- Limited coverage**: although Nmap's NSE scripts are powerful, their test coverage may be limited compared with other specialized vulnerability discovery tools. Some vulnerabilities may not be covered by the NSE scripts available, such as Active Directory vulnerabilities, exposure of sensitive data or more advanced cases of vulnerable web applications.



- Vulnerability complexity**: certain types of vulnerability may be difficult to detect using NSE scripts due to their complexity. For example, vulnerabilities requiring complex interaction with a remote service may not be detected effectively by Nmap (as in the case of excessive permissions in a file share or a permission control flaw in a web application).



- Passive detection**: Nmap focuses primarily on active scans to detect vulnerabilities, which means it may not effectively detect potential vulnerabilities without establishing an active connection with the target hosts. Vulnerabilities that do not manifest themselves during an active scan may therefore be missed (as in the case of a code injection in a web application).



- Dependency on updates**: Nmap's [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) of NSE scripts is constantly evolving, but there may be a delay between the discovery of a new vulnerability and the addition of a corresponding script to Nmap. As a result, Nmap may not always be up to date with the latest vulnerabilities.



- False positives and false negatives**: as with any security tool, Nmap's NSE scripts can produce false positives (false vulnerability alerts) or false negatives (real vulnerabilities not detected). This is something to bear in mind when analyzing Nmap results.



So it's important to understand what Nmap does and doesn't do, and likewise to know how to interpret its results. In particular, we've seen throughout this tutorial that default options can lead us to miss out on important elements that can be uncovered with careful use.


Whether you're a network system administrator, a security engineer or even a CISO, using Nmap gives you an overview of the security status of an information system. This is an important first step in securing a system, which can be carried out regularly by the IT team. However, it should not replace the intervention and advice of [cybersecurity] experts (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), who will be able to uncover weaknesses far more comprehensively than Nmap.


### V. Conclusion


In this first section of Module 3, we've introduced vulnerability scanning via Nmap. We now know how to use the main option to perform this task, but we also know the limits of the exercise. In the next section, we'll be taking a closer look at this functionality, using NSE scripts to extend Nmap's power tenfold.


## 8 - Using Nmap's NSE scripts


### I. Presentation


In this section, we'll take an in-depth look at NSE (_Nmap Scripting Engine_) scripts. In particular, we'll look at why they're one of the great strengths of this tool, how they work and how to browse and use the many existing scripts.


This section follows on from the previous tutorial, in which we learned how to use Nmap's vulnerability scanning features in a basic way. We will now take a closer look at how [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) works in this respect, so that we can once again carry out more precise and controlled scans.


### II. The concept of Nmap NSE scripts


Nmap's NSE scripts allow you to extend its capabilities in a highly flexible way. They are written in LUA, a scripting language that is easier to handle and access than the C or C# used by Nmap. The advantage of using a LUA script with Nmap rather than a stand-alone tool is that it allows us to take advantage of Nmap's speed of execution and standard features (host, port and version discovery, etc.).


These scripts are organized by category, and a single script may belong to more than one category:


| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Technically, the categories to which a script belongs are indicated directly in its code.


![nmap-image](assets/fr/41.webp)


nSE script categories `ftp-anon`._


This example shows part of the code of the NSE script `ftp-anon.nse`, whose execution we saw in the previous section.


### III. List existing NSE scripts


By default, Nmap's NSE scripts are located in the `/usr/share/nmap/scripts/` directory, with no specific tree structure or hierarchy. Here's an overview of the contents of this directory:


![nmap-image](assets/fr/42.webp)


extracts the contents of the `/usr/share/nmap/scripts/` directory containing NSE scripts._


This directory contains over 5,000 NSE scripts. In most cases, the first part of the script name contains the protocol or category to which it belongs. This enables us to sort the list, for example, if we wish to list all scripts targeting the FTP service:


![nmap-image](assets/fr/43.webp)


list of NSE Nmap scripts with names starting with `ftp-`._


Nmap doesn't really offer an option for browsing and listing its NSE scripts; you can use the command `--script-help` followed by the name of a category or a word:


```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```


However, the output will be the name of each script and its description, which is not optimal if the search brings up several dozen scripts:


![nmap-image](assets/fr/44.webp)


result of using Nmap's `--script-help` command


In my opinion, the most effective method is to use the classic Linux commands in the `/usr/share/nmap/scripts/` directory:


```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```


Feel free to browse the code of the modules that speak to you, to better understand how an NSE script works.


### IV. Using Nmap's NSE scripts


Now we're going to learn how to carry out vulnerability scans by carefully selecting the NSE scripts we're interested in.


#### A. Select scripts by category


To begin with, we can choose to execute all scripts belonging to a specific category. We need to indicate this category or these categories to Nmap with the argument `--script <category>`:


```
# Use default NSE scripts
nmap --script default 10.10.10.152
```


This first command is the equivalent of the `nmap -sC` command. By default, Nmap will select scripts in the `default` category, but that's just for the sake of argument. The next command, for example, will use all scripts in the `discovery` category:


```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```


As we have seen, some categories allow us to quickly identify what the related NSE scripts do (`discovery`, `vuln`, `exploit`), while others define the level of risk, detection or stability of the test performed. If we're in a sensitive context and don't have a good grasp of the different actions performed by our script selection, we can choose to combine the selections to choose only those scripts that are in the `discovery` and `safe` categories:


```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```


If you absolutely and explicitly want to exclude scripts from the `dos` and `intrusive` categories, you can use the following notation:


```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```


Please note that specifying exclusion conditions as above will result in the use of all other categories that are not explicitly excluded. To be fairer, we could specify, for example:


```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```


Here are some examples of how to handle NSE scripts by category, especially when using Nmap for vulnerability analysis in real-life contexts.


#### B. Select scripts as a unit


We can also choose to carry out a single specific test during an analysis, a test corresponding to an NSE script. To do this, we need to specify the name of the script in the `-script <name>` parameter. Taking the `ftp-anon.nse` script example:


```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```


We then have a very precise result:


![nmap-image](assets/fr/45.webp)


result of using the NSE `ftp-anon` script on an FTP port via Nmap._


We see the result of running the `ftp-anon` script on port 21, and no other port, because we specified the `-p 21` option. We could also have performed a basic port scan, executing the `ftp-anon` NSE script only on the FTP services discovered:


```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```


Thus, Nmap would also have executed this anonymous connection test if it had found an FTP service on another port.


For a brief description of what an NSE script does, you can use the `--script-help` option mentioned above:


![nmap-image](assets/fr/46.webp)


help display result for NSE script `sshv1`._


In short, once again we can reuse all the network discovery options, services, versions and technologies we've used up to now!


#### C. Managing script arguments


In the course of using Nmap, you will come across certain NSE scripts that require input arguments in order to function correctly. We'll now look at how to pass arguments to these scripts via Nmap's options.


As an example, let's take the `ssh-brute` script, which allows you to perform a brute force attack on the SSH service.


A classic brute force attack consists of testing several passwords (sometimes millions) in an attempt to authenticate to a specific account. By attempting so many passwords, the attacker bets on the probability that the user has used a weak password in the password dictionary used for the attack.


This script has "default" options, which we could customize to suit our context. In the context of this attack, for example, we can provide Nmap with the list of users and the password dictionary to be used. As far as I know, it's not possible to easily list the arguments required for a script, so the most reliable way is to visit the official Nmap website. A direct link to the documentation for an NSE script can be obtained in response to the `--script-help` option:


![nmap-image](assets/fr/47.webp)


result of displaying help for the NSE `ssh-brute` script with a link to nmap.org._


By clicking on the indicated link, we arrive on this web page of the site [https://nmap.org](https://nmap.org/):


![nmap-image](assets/fr/48.webp)


list of arguments that can be passed to Nmap's `ssh-brute` NSE script


Here we have a clear view of the arguments that can be used, the main ones in our context being `passdb` (file containing a list of passwords) and `userdb` (file containing a list of users). The documentation here refers to internal Nmap libraries, as these brute force mechanisms and associated options are mutualized to be used uniformly across several scripts (`ssh-brute`, `mysql-brute`, `mssql-brute`, etc.) and will therefore have more or less the same arguments:


```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```


As you can see in this last command, we can specify the necessary arguments to an Nmap script using the `--scripts-args key=value,key=value` option. Here's a possible result of the Nmap output when performing an SSH brute force via the `ssh-brute` NSE script:


![nmap-image](assets/fr/49.webp)


result of SSH bruteforce execution via Nmap._


As you can see, the information generated by NSE scripts is prefixed with `NSE: [script name]` in the interactive output (terminal output), making it easier to find. Within the usual display of Nmap results, we simply have a summary indicating whether or not weak identifiers have been discovered (including passwords, remember).


To take things a step further, and to remind you that all this can be used in addition to all the options we've already looked at, here's a command that will discover the `10.10.10.0/24` network, scan the 2000 most frequent TCP ports and run an anonymous access search on FTP services and a brute force campaign on SSH services:


```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```


This is just one example of the many available scripts and their options. But we now have a better idea of how to get to grips with NSE scripts, whether they require arguments and how to pass these arguments to Nmap.


### V. Conclusion


In this section, we've learned how to use Nmap's NSE scripts to perform various tasks. I invite you to take the time to discover the different categories of scripts and the scripts themselves, to see just how many tests they can automate.


For several sections now, we've been accumulating more or less advanced discovery, scan and enumeration options. By now, you should be aware that Nmap's output and results display is starting to become quite extensive, sometimes even too verbose for our terminal. In the next section, we'll learn how to master this output, in particular by storing it in files in various formats.





## 9 - Managing Nmap output data



### I. Presentation


In this section, we'll take a look at the output produced by Nmap, and in particular at the various options for formatting this output. We'll see that Nmap can produce several output formats to suit different needs, and that this too is one of the great strengths of this tool.


By default, Nmap offers a detailed view of the results of the scans and tests it performs. This includes hosts and services scanned, those detected as accessible, the specifics of open ports, their status and version. In addition, details of NSE scripts are also available in the terminal output. However, this output can quickly become voluminous, even with clear formatting of the information, which can make it difficult to find precise information in the results.


### II. Mastering Nmap output formats


#### A. Save scan results in a text file


To make things easier, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) makes it very easy to save its output in a text file. This can be useful for archiving, comparison with other tests, but also for browsing this output with specialized word-processing tools or scripting languages, such as Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, etc. To store Nmap's standard output in a text file, we can use the `-oN <filename>` option (the "N" in "normal"):


```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```


No surprise then, as Nmap will display its usual standard output in our terminal, but also in the specified file.


#### B. Generate Nmap output in condensed format


There's also a second output format in the "text" style that can be easily interpreted by a human: the "greppable" format.


This format was created to provide a "condensed" view of the Nmap output, structured in such a way as to facilitate its processing by tools such as `grep`. Let's look at an example of this type of output:


![nmap-image](assets/fr/50.webp)


nmap network scan and output in "greppable" format._


Here, I've performed a network discovery as well as a port scan and an analysis of technologies and versions on a /24 network, then stored the output in a file in "greppable" format. I end up with a file containing 2 lines per active host:



- The first line tells me that such and such a host is _Up_;



- A second line tells me which ports have been scanned, their status and the technology and version information retrieved in a very specific format: `<port>/<status/<protocol>//<service>//<version>/,`



This formatting with a fixed delimiter allows rapid processing by word processing tools such as `grep`, or scripting and programming languages. The following command, for example, enables me to easily retrieve information about host `10.10.10.5` in the case of a huge scan performed by Nmap whose output would be difficult to browse:


```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```


Conversely, I can also easily list all hosts that have port 21 open, as ports and IP are on the same line:


```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```


To generate such output, we need to use the `-oG <filename>.gnmap` option (the "G" in "grep"). By habit, I use the `.gnmap` extension here for such a file, but feel free to use whichever you like:


```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```


This format can be used for a variety of purposes and is particularly useful for rapid scripting/sorting. Nevertheless, it's tending to be abandoned in favor of the format we'll be looking at next.


note: the `-oG` greppable format has been officially deprecated since Nmap 7.90. It can still be used for compatibility. It can still be used for compatibility purposes, but it is recommended that you use the XML or normal format for any development or automated parsing._


#### C. XML format for Nmap output


The last format worth mentioning in this tutorial is XML. Unlike the previous two formats, this one is not designed to be read by humans, but by other tools or scripts.


XML (_eXtensible Markup Language_) is a markup language used to store and transport data, offering a hierarchical structure via custom tags.


Within Nmap, the XML format is used to generate detailed reports on the scans performed, including information on hosts, ports and vulnerabilities detected, as well as additional information not displayed in the standard Nmap output.


To generate an output file in XML format, we need to use the `-oX` option ("O" from "XML"):


```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```


The result is Nmap's standard output in your terminal, as well as a file in XML format in your current directory.


Of course, the XML format is not designed to be read and interpreted by humans. Nevertheless, if you want to do scripting or automated analysis on this format of Nmap output, you still need to have an idea of the tags and structure used. For example, here's part of the content of the XML file created by Nmap, which shows the scan results for 1 host:


![nmap-image](assets/fr/51.webp)


example of an XML record for 1 host during an Nmap scan


There's a lot of information here, and we're particularly interested in the two open ports:


```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```


We understand that this format will facilitate the automated parsing of results, as each piece of information is neatly arranged in a dedicated, named tag or attribute. In particular, we find a piece of information that we haven't come across before: the CPE.


```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```


We briefly mentioned the CPE in section 2 of module 2, and this information is determined in matches during version detection. Nmap uses its service, technology and version detection mechanisms to find the associated CPE.


This allows us to reuse this information with the databases and applications that use it. I'm thinking in particular of the NVD database, which references CVEs. For each CVE, it contains the CPEs affected by the vulnerability. Here's an example of a CVE concerning `a:microsoft:internet_information_services:7.5` from the NVD database:


![nmap-image](assets/fr/52.webp)


presence of a CPE in the details of a CVE in the NVD database


We now have a better understanding of the benefits of this format, which offers a very clear structure of information and contains all the data collected or processed by Nmap.


As a reflex, I systematically save my Nmap scans in all three formats at once. This is made possible by the `-oA <name>` option ("A" for "All"), which will create a `<name>.nmap` file, a `<name>.xml` file and a `<name>.gnmap` file. This way I'm sure I won't run out of anything when I need to go back over the results.


With these three formats, you should have everything you need to save and eventually process Nmap results in an automated way. We'll be using the XML format again in the next section, when we look at using Nmap with other security tools.


#### III. Generating an HTML report from an Nmap scan


The XML format offers many possibilities, not least that of serving as the basis for generating a report in HTML format, which will be more visually pleasing to browse.


To transform a Nmap file in XML format into a web page, we'll use the `xsltproc` tool, which we'll need to install first:


```
# Install the xsltproc tool
sudo apt install xsltproc
```


Once this tool is installed, simply provide it with the XML file to be converted and the name of the HTML report to be generated:


```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```


As a result, we'll have our entire scan nicely structured, with even a few colors and clickable links in the table of contents!


![nmap-image](assets/fr/53.webp)


extract from a Nmap scan report in HTML format generated by xsltproc._


Broadly speaking, the XML file saved by Nmap contains a reference to another file in XSL format:


```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```


Conversion to HTML is therefore a function provided and facilitated by Nmap, `xsltproc` being a common and recognized tool for performing this task (which does not come from the Nmap tool suite).


XSLT (_Extensible Stylesheet Language Transformations_) is a subset of XSL that allows XML data to be displayed on a web page and "transformed", in parallel with XSL styles, into readable, formatted information in HTML format.


source: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_


The level of information in the report is equivalent to that of Nmap's XML format and higher than that of the standard terminal output (_interactive output_).


### IV. Managing Nmap's verbosity level


We'll now take a look at a few options for Debugger Nmap or for tracking its progress.


The first option we should mention is the `-v` option, which increases Nmap's verbosity. Here's an example:


![nmap-image](assets/fr/54.webp)


nmap's verbose output using the `-v`._ option


On a scan targeting many hosts and ports, the terminal output will become difficult to exploit due to the amount of information displayed. For this reason, this option should be used in combination with the options seen previously, which allow you to store Nmap's standard output in a file. Information related to the use of verbosity will not be included in this output file. As you can see from the example above, this verbosity allows you to track Nmap's actions and discoveries clearly and directly. For longer scans where data display may be slow in coming, this avoids being blind to Nmap's current activity and knowing that things are progressing and at what pace. To increase verbosity by a further level, you can use the `-vv` option.


To further track Nmap's activity during its scan, you can use the `--packet-trace` option. With the `-v` option, we get a live log of all open ports discovered by Nmap, whereas with this option, we get a log line for each packet sent to a port. This naturally produces a very verbose output, but allows detailed monitoring of Nmap's activity, here's an example:


![nmap-image](assets/fr/55.webp)


detailed monitoring of Nmap activity via `--packet-trace`._


Again, this information will not be recorded in the output file produced by Nmap if the `-oN`, `-oG`, `-oX` or `-oA` options are used.


Finally, Nmap also offers two debug options: `-d` and `-dd`. These options behave similarly to the `-v` verbosity option, but add additional technical information, such as a summary of technical parameters at the start of the scan:


![nmap-image](assets/fr/56.webp)


timing options are displayed in Nmap's debug view


In the next few sections, we'll take a look at what the "Timing" options are and why it's worth knowing them.


Finally, if you only want to have a basic, synthetic overview of the progress of the Nmap scan, you can use the `--stats-every 5s` option. The "5s" here means 5 seconds and can be modified to suit your needs. This is the frequency at which we will receive feedback from Nmap on its progress:


![nmap-image](assets/fr/57.webp)


information displayed by Nmap's `--stats-every` option


In particular, we can get a percentage of progress, as well as an indication of the phase it's in: host discovery phase via [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), discovery phase of exposed TCP ports, etc. This information can also be obtained in the terminal output by pressing "Enter" during a scan.


However, Nmap isn't very good at estimating how long a task will take, not least because it doesn't know in advance how many hosts and services it will have to scan.


### V. Conclusion


In this section, we've looked at a number of options for saving Nmap scan results in different file formats. This will come in very handy, as in realistic contexts, scan results can take up hundreds or even thousands of lines! We've also seen how to increase Nmap's verbosity level for debugging purposes or to obtain a scan progress report.


The XML format will be particularly useful in the next section, where we'll look at a few tools that can work with Nmap results.



## 10 - Using Nmap with other security tools


### I. Presentation


In this section, we'll take a look at some of the classic uses of Nmap with other free and open source security tools. In particular, we'll use what we've learned in the previous sections to further enhance Nmap's power and efficiency.


The ability to save Nmap scan results in XML makes the data compatible with a host of other tools. As almost all programming and scripting languages today have libraries capable of parsing XML, this makes it much easier to process this data. A number of tools, particularly those geared towards offensive security, have functions for processing the XML format generated by Nmap. Let's take a closer look.


I'm going to mention a few offensive tools without really detailing how they are used or how they work. I'll assume that the reader is familiar with their basic use and that they are already operational. This section will be of particular interest to [cybersecurity] professionals (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), people in training or those who have decided to delve deeper into the subject.


### II. Importing Nmap results into Metasploit


The first tool we're going to look at for reusing Nmap data in offensive security and vulnerability research is Metasploit.


Metasploit is an exploit and attack framework. It is a free solution and a recognized tool that contains a large number of modules written in Ruby or Python. These enable vulnerabilities to be exploited, attacks to be carried out, backdoors to be generated, callbacks to be managed (C&C or Communication and Control functions) and everything to be used uniformly.


In particular, this well-known and widely-used operating framework can work with a postgreSQL [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) in which hosts, ports, services, authentication information and more are stored.



- Official Metasploit documentation: [https://docs.metasploit.com/](https://docs.metasploit.com/)



This is where Nmap and its output come into play, as the XML format of the Nmap output can be easily imported into Metasploit's database to populate its database of hosts and services, which can then be quickly designated as targets for this or that attack.


Once in my Metasploit interactive shell, I start by creating a workspace, a kind of space specific to my environment of the day:


```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```


Once my workspace has been created, we need to validate that communication with the database is operational:


```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```


Finally, we can use the Metasploit `db_import` command to import our Nmap scan in XML format:


```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```


Here's the result of executing all these commands:


![nmap-image](assets/fr/58.webp)


import a Nmap scan in XML format into the Metasploit database


Here you can see that each host is imported, along with its services. This data can then be displayed via the command `services` or `services -p <port>` for a specific service:


![nmap-image](assets/fr/59.webp)


list of services imported from the XML file into the Metasploit database


Finally, we can quickly and easily reuse this data in a module thanks to the `-R` option, which will "convert" the list of services obtained as input for the `RHOSTS` directive, which is used to specify the targets of the attack to be carried out. Here's an example with the `ssh_login` module, which enables you to carry out a brute force attack on [SSH] services (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):


![nmap-image](assets/fr/60.webp)


use the `services -R` option to import the services specified as the target of the attack


This is just a small example of what can be done with Nmap data in Metasploit, but it gives you a small idea of how quickly and easily this information can be reused as part of a penetration test, vulnerability scan or cyber attack. It's also worth mentioning that Nmap can be run directly from Metasploit to import the results into the database (command `db_nmap`), another interesting topic to cover!


### III. Using Nmap with the Aquatone web scanner


The second tool I'd like to introduce in this section on reusing Nmap results for offensive security and vulnerability analysis is Aquatone.


Aquatone is a web scanner designed to efficiently explore web applications on a network. It offers advanced features for web services discovery, sub-domain identification, port analysis and web application fingerprinting. All presented clearly and concisely in HTML, JSON and text reports for easy web security analysis.


As with Metasploit, Aquatone can directly process Nmap's XML format and use it as a target for scanning. In particular, it can extract only the hosts and services of interest (web services) from all the data a Nmap report may contain.



- Tool link: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)



To use Nmap's XML output with Aquatone, simply send the XML file in a pipe that will be consumed by Aquatone. Here's an example:


```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```


Where Aquatone normally performs port discovery on hosts to find web services, in this context it will rely solely on the results of Nmap, which has already performed this operation, thus saving time:


![nmap-image](assets/fr/61.webp)


using Nmap results in XML format with `aquatone`._


For your information, here is an extract from the report produced by Aquatone:


![nmap-image](assets/fr/62.webp)


example of an `aquatone` report


Personally, I often use Aquatone to get a quick overview of the types of websites present on the network, thanks in particular to its screenshot functionality.


Here again, having a complete Nmap report in XML format saves time and makes it easy to reuse in another tool.


### IV. Conclusion


These two examples clearly show that Nmap's XML format makes it easy for other tools to use its results, as it is a structured, easy-to-use data format. There are many other tools capable of processing these results, such as automated reporting tools, graphical representations or more complex, proprietary vulnerability scanners.


Of course, you can also develop your own scripts and tools in Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) or any other language with an XML parsing library to manipulate and reuse Nmap result data as you see fit.


This section brings us to the end of the tutorial module on more advanced use of Nmap, in particular for vulnerability scanning through NSE scripts.


The next section of the tutorial will focus, among other things, on some additional, more technical best practices and tips on the specific scans that Nmap can perform. We'll also take a look at scan performance optimization options, which are particularly useful when scanning large networks.



## 11 - Improving network scan performance


### I. Presentation


In this chapter, we'll learn how to optimize the speed of network scans performed with Nmap by using various specific options. In particular, we'll learn more about the inner workings of Nmap, from _timeout_ management to the tool's pre-saved configurations.


Now that we've had a good look at Nmap's features, let's get to grips with the beast and its power. If you've ever used the tool on large networks, you've probably noticed that some scans can take a long time, despite the tool's power. And with good reason: a simple `nmap` command with a few options can generate millions of packets targeting hundreds of thousands of potential systems and services.


What's more, some network equipment configurations may intentionally impose a slower rate (number of packets per second), at the risk of rejecting your packets or banning your IP address for security reasons.


Depending on the context, it may be worthwhile to try and optimize all this, as we'll see in this chapter.


In any case, you can check the default values of the parameters we are going to look at, as well as whether the options you are going to use have been correctly taken into account, via the Nmap debug (option `-d` seen in a previous chapter):


![nmap-image](assets/fr/63.webp)


view Timing options via Nmap's `-d` option._


### II. Managing the speed of Nmap scans


#### A. Managing parallelization


By default, Nmap uses parallelization in its scans to optimize them, and all the parameters it uses can be modified via various options. However, the cases in which it is actually necessary to modify these parameters are quite rare, so we won't go into them in detail in this tutorial:



- `--min-hostgroup/max-hostgroup <size>`: size of parallel host scan groups.



- `--min-parallelism/max-parallelism <numprobes>`: parallelization of Probes.



- `--scan-delay/--max-scan-delay <time>`: adjusts the delay between Probes.



Just know that they exist and can be used.


#### B. Managing the number of packets per second


By default, Nmap itself adjusts the number of packets per second it sends according to network response. But it is possible to force this setting by defining the high and/or minimum value to follow in terms of number of packets per second. This setting is made using the options `--min-rate <number>` and `--max-rate <number>` where `number` represents a number of packets per second. Example:


```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```


These options allow you to adjust the speed of scans according to your specific needs, either to speed up the process or to limit the bandwidth used. The latter case (limiting the speed of scans) is the one that will most likely lead you to these options, especially if you experience network latency when using Nmap (which is quite rare).


### III. Managing connection failures and timeouts


Another parameter we can play with to optimize the speed of Nmap scans (or guarantee greater accuracy) concerns _timeout_ and _retry_.


For _timeouts_, this is the **no response timeout** after which Nmap will stop waiting for a response and consider the service or host unreachable. For _retry_, this is the **number of successive attempts at an operation** that Nmap will perform before moving on.


As with parallelization, _timeout_ and _retry_ management can be applied to the host or service discovery phases:



- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: specifies the round-trip time of an exchange. Again, this parameter is actually calculated and adapted on the fly during the scan. It's unlikely that you'll need to use it, as Nmap calculates this time on the fly according to network reaction.



- `--max-retries <number>`: limits the number of retransmissions of a packet during port scanning. By default, Nmap can go up to 10 retries for a single service, especially if it finds latencies or losses at network level, but in most cases only one is performed.



- `--host-timeout <time>`: specifies the maximum time Nmap will spend on a host for all its operations, including port scanning, service detection, and any other operations related to that host. If this time interval is exceeded without any response or **completion of operations**, Nmap will abandon this host without displaying any results concerning it, and move on to the next in its list. This allows you to control the maximum time Nmap spends on a given host, avoiding getting stuck on recalcitrant hosts and optimizing overall scan time.



In my day-to-day work, I use the `--max-retries` and `--host-timeout` options to optimize my scans:


```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```


These parameters offer additional flexibility for adjusting scan behavior to specific needs and network conditions. However, you need to be aware of their implications in terms of load on scanned hosts and potential loss of accuracy.


### IV. Use of prepared configurations


The various options we've seen in this chapter can be used individually or as part of the ready-made configurations offered by Nmap. The option that enables these _templates_ (configuration templates) to be used is `-T <number>` or `-T <name>`. There are 5 usable _templates_ levels:


```
-T<0-5>: Set timing template (higher is faster)
```


By default, Nmap uses _template_ 3 (_normal_), which is generally sufficient.


For my part, I generally operate in contexts where I need to be fairly fast (while remaining as complete as possible) and I frequently use the `-T4` option.


```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```


Here is what the debug information for this scan shows us:


![nmap-image](assets/fr/64.webp)


use of `-T4` setup during an Nmap scan


### V. Conclusion


In this chapter, we've looked at various techniques and options you can use to manage Nmap's power, aggressiveness and performance. These options are particularly useful when scanning large networks, and more rarely for stealth purposes.


In the next chapter, we'll take a look at a few best practices for using Nmap and ensuring its safety.



## 12 - Data security and confidentiality when using Nmap


### I. Presentation


In this chapter, we'll look at a number of good practices to be adopted with regard to the security and, above all, the confidentiality of data produced, processed and stored by Nmap.


The use of Nmap within an information system can quickly be categorized as an offensive action. Consequently, a number of precautions need to be taken in order to act within a legal framework, while guaranteeing the security of the intended targets, the data collected and the system used for the scan.


### II. Obtaining appropriate authorizations


Before scanning a network or system, make sure you have obtained the appropriate authorizations. Scanning systems for vulnerabilities (`NSE scripts`) without authorization may be illegal, and may have legal consequences, especially if information system security is not part of your official remit.



- As a reminder: [Penal Code: Chapter III: Attacks on automated data processing systems](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)



### III. Protecting sensitive data


The results produced by Nmap can be considered sensitive, particularly when they contain information about weaknesses in the information system that could be exploited by an attacker. But also when they concern systems that are not accessible to everyone (e.g. sensitive, industrial, healthcare or [backup] information systems (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).


We have also seen that, depending on the NSE scripts used, the NSE scan results of [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) can also contain identifiers.


Thus, a malicious individual who manages to access these scan results will have at hand a map of the information system and a wealth of technical information, without having carried out these actions himself, at the risk of being detected.


It is therefore important to take care not to inappropriately collect or store sensitive information when using Nmap, including, but not limited to, the following:



- Encrypting output data: if you need to store or transmit the results of your Nmap scans, be sure to encrypt them to protect data confidentiality. This will prevent unauthorized interception of sensitive information. Ideally, data should be encrypted as soon as it leaves the system used to perform the scan (a ZIP archive encrypted with a strong password is a very good start).



- Set up access controls: make sure that only authorized people have access to the results of your Nmap scans where they will be stored. Set up appropriate access controls to protect sensitive information from unauthorized access.



- Vigilance when handling data: when transiting, copying or processing scan data, make sure you keep data security under strict control. This means: don't leave them lying around in the `Download` directory of a workstation connected to the Internet, don't let them transit through your internal HTTP file exchange application, don't leave your Notepad open without locking the workstation during your lunch break, etc.



### IV. Managing aggressive scans


As we've seen throughout this tutorial, Nmap can be very verbose at network level. It can also send packets that are not properly formatted, and that do not strictly respect the protocol structure in the network frames and packets it generates. All these actions can have an impact on certain systems and services, sometimes to the point of causing malfunction or saturation of system and network resources.


To avoid any incidents, you need to master Nmap's behavior and know how to adapt it to the context in which it is used, by means of the various options discussed in this tutorial. We won't necessarily use Nmap in the same way on an information system containing industrial [hardware](https://www.it-connect.fr/actualites/actu-materiel/) as in a user network made up of Windows systems protected by a local firewall or in a network core.


Hopefully, the various lessons in this tutorial have taught you how to master and analyze Nmap's behavior, but the best way to learn is by doing. So make sure you're familiar with the Nmap options you'll be using.


### V. Protecting the scan system


In the first chapter, we saw that in most cases, Nmap needs to be run as a `root` or local administrator. This is because it performs network operations, sometimes at a fairly low level, through network libraries, which require high and risky permissions from the point of view of system stability or the confidentiality of other applications.


As a result, Nmap can be seen as a sensitive component of the system on which it is installed. Be sure to use the latest version of Nmap, as older versions may contain known security vulnerabilities. By using an up-to-date version, you can minimize the risks associated with using the tool.


If you have opted to use Nmap not via a session as `root`, but by granting specific privileges to a privileged user so that he has everything he needs to use Nmap (`sudo` or _capabilities_), be aware that Nmap can be used as part of a complete elevation of privilege:


![nmap-image](assets/fr/65.webp)


elevation of Nmap privileges via `sudo`._


Here, I'm using the Nmap command through `sudo`, but this allows me to get an interactive shell as `root` on the system, which wasn't the original goal.


It's also highly inadvisable to install Nmap on systems that aren't designed to perform network scans. I'm thinking in particular of servers or workstations. On the one hand, this would add a potential vector for privilege elevation, but above all it would give the attacker effortless access to an offensive tool.


Finally, the security of the system used for scanning must be ensured more broadly, so that it does not itself become a vector for intrusion or information leakage. As a system administrator, it's better to use a dedicated system, ideally with a limited lifespan, rather than your own workstation.


### VI. Conclusion


In conclusion, make sure you have properly mastered Nmap before using it in real-life or production conditions, and be vigilant when processing and managing its results. It would be a pity to cause damage, leak data or facilitate a compromise, when the initial approach is aimed at improving your company's security.


## 13 - Port scans via TCP: SYN, Connect and FIN


### I. Presentation


In this chapter and the next, we'll take a closer look at the different types of TCP scan available in Nmap, starting with the most commonly used ones: SYN, Connect and FIN scans.


As you may have noticed, Nmap offers several options for TCP scans:


![nmap-image](assets/fr/66.webp)


scanning techniques available in Nmap._


The idea here is to explain some of these methods, to help you understand their differences, their advantages and their limitations. You'll see that, depending on the context or what you want to know, it's better to opt for one option or another.


### II. TCP SYN scan or "Half Open scan


The first type of TCP scan we're going to look at is the `TCP SYN Scan`, also known as the `Half Open Scan`. If you remember the network scans we did after our first port scans, this is the type of scan used by default by [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) when run with root rights.


The translation will help you understand how this scan works. In fact, a TCP SYN scan will send a TCP SYN packet to each targeted port, which is the first packet sent by a client (the one requesting to establish a connection) as part of the famous _Three way handshake_ TCP. Normally, if the port is open on the target server, with a service running behind it, the server will send back a TCP SYN/ACK packet to validate the client's SYN and initialize the TCP connection. This response takes the form of a TCP packet with the SYN and ACK flags set to 1, enabling us to confirm that the port is open and leading to a service.


On the other hand, if the port is closed, the server will send us a `TCP` packet with the RST and ACK flags set to 1 to terminate the connection request, so we'll know that no service seems to be active behind this port:


![nmap-image](assets/fr/67.webp)


tCP SYN Scan behavior diagram for open and closed ports


To get a more concrete view of the `TCP SYN Scan`, I performed a scan of port TCP/80 to a host that had an active web server on this port. Running a network scan with Wireshark, we can see the following flow (scan source: `10.10.14.84`):


![nmap-image](assets/fr/68.webp)


network capture during a TCP SYN scan for an open port


On the first line, we see that the scan source is sending a TCP packet to host `10.10.10.203` on port TCP/80. In this TCP packet, the SYN flag is set to 1 to indicate that this is a TCP connection initialization request.


Then, on the second line, we see that the target responds with a `TCP SYN/ACK`, meaning that it accepts to initialize a connection and therefore to receive streams on port TCP/80. We can therefore deduce that port TCP/80 is open and that a web server is present on the scanned server.


Our host then sends back an RST packet to close the connection, allowing the scanned host not to maintain an open TCP connection waiting for a response. In the case of a scan on many ports, not closing TCP connections could lead to a denial of service, saturating the number of connections waiting to be answered that the server can maintain (see [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))


In Wireshark, you'll be able to see the status of TCP flags for each test we perform. This will show whether the packet is a SYN, SYN/ACK, ACK, etc. packet:


![nmap-image](assets/fr/69.webp)


view a packet's TCP flags in Wireshark (TCP SYN here)


Conversely, I ran the same test between the two machines, but this time scanning a TCP/81 port on which no service is active (scan source: `10.10.14.84`):


![nmap-image](assets/fr/70.webp)


network capture during a TCP SYN scan for a closed port


The scanned host returns a `TCP RST/ACK` in response to my `TCP SYN` when the port is not open.


As mentioned, when running Nmap from a privileged terminal, TCP SYN Scan is the default mode, and can be forced via the `-sS` (`scan SYN`) option:


```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```



The `TCP SYN Scan` is the most commonly used scan for reasons of speed. On the other hand, a client's failure to finalize the _Three Way Handshake_ (i.e. not sending the ACK after the server SYN/ACK) may seem suspicious if it is observed too many times on a server or from the same source on the network. Indeed, the normal behavior of a client after receiving a TCP SYN/ACK packet in response to a TCP SYN is to send an `acknowledgement` (ACK) and then start the exchange.


Nonetheless, it does provide a slightly faster scan, as it doesn't bother sending an ACK for each positive response. The advantage of SYN Scan is its speed, since only one packet is sent per port to be scanned, at the expense of a greater chance of detection.


In addition, TCP SYN scan is able to detect whether a port is filtered (protected) by a firewall. In fact, a firewall in front of the target host can be detected by the way it behaves when it receives a TCP SYN packet on a port it is supposed to protect. It simply won't respond. However, as we've seen, in both cases (open or closed port), there is a response from the host. This third behavior will reveal the presence of a firewall between the scanned host and the machine running the scan. Here's the result Nmap can return when a scanned port is filtered by a firewall:


![nmap-image](assets/fr/71.webp)


nmap display when scanning a filtered port


When we perform a network capture at scan time, we can actually see that no response is given:


![nmap-image](assets/fr/72.webp)


network capture during a TCP SYN scan for a port filtered by a firewall


The difference between a closed port and a filtered port is as follows: a filtered port is a port protected by a firewall, whereas a closed port is a port on which no service is running and which is therefore unable to process our TCP packets. Some types of TCP scan, such as the TCP SYN scan, are able to detect whether a port is filtered, whereas other types of scan cannot.


### III. TCP Connect scan or Full Open scan


The second type of TCP scan is the `TCP Connect scan`, also known as _Full Open Scan_. It works in the same way as the TCP SYN scan, but this time returns a `TCP ACK` after a positive response from the server (a SYN/ACK). This is why it's called `Full Open', as the connection is fully opened and initiated on every port opened during the scan, thus respecting the TCP _Three Way Handshake_:


![nmap-image](assets/fr/73.webp)


tCP Connect Scan behavior diagram for open and closed ports


Here's what can be seen transiting the network during a `TCP Connect scan` targeting an open port:


![nmap-image](assets/fr/74.webp)


network sniffing during a TCP Connect scan for an open port


We can see that the first TCP packet sent is a `TCP SYN` sent by the client, and the server will then reply with a `TCP SYN/ACK`, indicating that the port is open and hosting an active service. To simulate a legitimate client all the way, Nmap will then send a `TCP ACK` back to the server. Conversely, when scanning a closed port:


![nmap-image](assets/fr/75.webp)


network capture during a TCP Connect scan for a closed port


Note that the server response to our `SYN` packet is once again a `TCP RST/ACK` packet, so we can deduce that the port is closed and no services are running on it.


When using Nmap, the `-sT` (`scan Connect`) option is used to perform a TCP Connect Scan. Please note that when Nmap is used from an unprivileged session, this is the default TCP scan mode:


```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```


The `TCP Connect Scan` simulates a more legitimate connection request, with behavior that most closely resembles that of a lambda client, so it's harder to spot a scan on a reduced number of ports. It is, however, slower, as it completely initializes every TCP connection on the open ports of the scanned machine.


An Nmap scan of 10,000 ports will still be easily detectable if network intrusion detection and protection services (IDS, IPS, EDR) are installed. When an attacker wants to keep a low profile, he'll tend to focus on a small number of strategically chosen ports, such as 445 (SMB) or 80 (HTTP), which are often open on servers and present common vulnerabilities.


Since TCP Connect Scan expects a response in both cases, it can also detect the presence of a firewall that might be filtering ports on the target host.


### IV. TCP FIN scan or "Stealth Scan


The `TCP FIN Scan`, also known as _Stealth Scan_, uses the behavior of a client terminating a TCP connection to detect an open port.


In TCP, end of session means sending a TCP packet with the FIN flag set to 1. In a normal exchange, the server ceases all communication with the client (no response). If the server has no active TCP connection with the client, it will send a `RST/ACK`. We can therefore differentiate between open and closed ports by sending `TCP FIN` packets to a set of ports:


![nmap-image](assets/fr/76.webp)


tCP FIN scan behavior diagram for open and closed ports


I again captured the network during a _Stealth scan_ and this is what you see when the scanned port is open:


![nmap-image](assets/fr/77.webp)


network capture during a TCP FIN scan for an open port


We can see that the client sends one or two packets to terminate a TCP connection and that the server doesn't respond. It simply accepts the end of the connection and stops communicating.


Here's what we see now when we scan a closed port:


![nmap-image](assets/fr/78.webp)


network capture during a TCP FIN scan for a closed port


We see that the server sends back a `TCP RST/ACK` packet, so there's a difference in behavior between an open and a closed port, and we're able to list the open ports on a server by sending a TCP FIN packet. Using Nmap, the `-sF` (`scan FIN`) option is used to perform a TCP FIN Scan:


```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```


TCP FIN Scan does not work on Windows hosts, because the OS tends to ignore TCP FIN packets when they are sent to ports that are not open. So if you run a TCP FIN Scan on a Windows host, you'll get the impression that all ports are closed.


That's why it's important to be familiar with several scanning methods, and to understand the difference between them.


Since in either case the TCP FIN will not wait for a response, it will be unable to detect the presence of a firewall between the target host and the scan source.


Here is an example of Nmap's TCP FIN scan result:


![nmap-image](assets/fr/79.webp)


results of a TCP FIN scan by Nmap._


In fact, a non-response from the host on a given port can mean that the port is filtered, but also that it is open and active.


This scan is referred to as "stealth", as it doesn't generate much traffic and generally doesn't cause logging in the targeted systems. It can be used to discreetly discover ports on a network without raising any alarms. However, as mentioned above, its effectiveness can vary depending on the target system, as can its discretion depending on the configuration of security equipment.


### V. Conclusion


So much for the first of two chapters on the different TCP scan types offered by Nmap! In the next chapter, we'll look at the XMAS, Null and ACK TCP scan types, which operate in different ways to detect open ports on a host.




## 14 - Port scans via TCP: XMAS, Null and ACK


### I. Presentation


In this section, we'll continue to explore the various TCP scanning methods offered by Nmap. Here we'll look at the `XMAS`, `Null` and `ACK` methods, which use TCP-specific features to retrieve information on the ports and services open on a given target.


### II. TCP XMAS scan


The XMAS Scan TCP is a little unusual in that it doesn't simulate normal user or machine behavior on a network at all. In fact, XMAS Scan will send TCP packets with flags `URG` (Urgent), `PSH` (Push), and `FIN` (Finish) set to 1, in order to bypass certain firewalls or filtering mechanisms.


The name XMAS comes from the fact that seeing these flags on is unusual. When all three flags are set simultaneously in a TCP packet, it looks like a lit Christmas tree:


![nmap-image](assets/fr/80.webp)


tCP flags used in XMAS scan


Without going into detail about the role of these flags here, it's important to know that when sending a packet with these three flags enabled, an active service behind the target port will not return any packets. On the other hand, if the port is closed, we'll receive a TCP RST/ACK packet. We'll now be able to differentiate between the behavior of an open and a closed port when listing ports on a machine:


![nmap-image](assets/fr/81.webp)


tCP XMAS Scan behavior diagram for open and closed ports


Still following the same logic, a network scan on port TCP/80 of a host with an active web server shows the following behavior when detecting an open port (scan source `10.10.14.84`):


![nmap-image](assets/fr/82.webp)


network capture during a TCP XMAS scan for an open port


We can see that the scan source sends two TCP XMAS packets (with flags `FIN`, `PSH` and `URG` set to 1) to host `10.10.10.203` and that there is no return from the target, indicating that the port is open. Conversely, when performing a `TCP XMAS Scan` on a closed port, the following result is observed:


![nmap-image](assets/fr/83.webp)


network capture during a TCP XMAS scan for a closed port


The response to our TCP packet is then a `TCP RST/ACK`, indicating that the port is closed. To use this technique with Nmap, the `-sX` (`scan XMAS`) option allows you to perform a TCP XMAS Scan:


```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```


It's important to note that the TCP XMAS scan is not able to detect firewalls that may be between the target and the scan machine, unlike some other types of scan such as TCP SYN or Connect. Indeed, an active firewall between the two hosts will ensure that no TCP return is made if the targeted port is filtered (i.e. protected by the firewall). In the event of a non-response, it is therefore impossible to know whether the port is protected by the firewall or open and active. You should also be aware that, like the TCP FIN scan, certain applications or operating systems such as Windows can distort the results of this type of scan.


note: support for XMAS/FIN/NULL scans on recent versions of Windows remains limited, and results may be inconsistent on this type of target. (Update 2025)_


### III. TCP Null scan


In contrast to TCP XMAS scan, TCP Null scan will send TCP scan packets with all flags set to 0. This too is behavior that will never be found in a normal exchange between machines, as sending a TCP packet without a flag is not specified in the RFC describing the TCP protocol. This is why it can be detected more easily.


Like the TCP XMAS scan, this scan can interfere with certain firewalls or filtering modules, allowing packets to pass through:


![nmap-image](assets/fr/84.webp)


tCP Null Scan behavior diagram for open and closed ports


Here's what can be seen on the network during a TCP Null scan on an open port:


![nmap-image](assets/fr/85.webp)


network capture during a TCP Null scan for an open port


The scanning machine sends a flagless packet (`[<None>]` in Wireshark) without any response from the server. Conversely, when the target port is closed:


![nmap-image](assets/fr/86.webp)


network capture during a TCP Null scan for a closed port


To perform a TCP Null scan with Nmap, simply use the `-sN` (`scan Null`) option:


```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```


Since the response when a port is open and when a firewall is active (no server feedback in either case) is identical, TCP Null scan is unable to detect the presence of a firewall. What's more, the firewall may even falsify the result by suggesting that a port is open, since it doesn't respond to TCP packets without flags, even though the port is filtered. This is important information to be aware of when using scans that are unable to differentiate between an open and a filtered (firewall-protected) port, such as `TCP Null`, `XMAS` or `FIN` scans, in order to remain consistent in the interpretation of the results obtained.


### IV. TCP ACK scan


The TCP ACK scan is used to detect the presence of a firewall on the target host or between the target and the scan source.


Unlike other scans, the TCP ACK scan doesn't try to identify which ports are open on the host, but rather whether a filtering system is active, responding for each port with `filtered` or `unfiltered`. Some TCP scans, such as `TCP SYN` or `TCP Connect`, can do both at the same time, while others, such as `TCP FIN` or `TCP XMAS`, cannot determine the presence of filtering at all. This is why the TCP ACK scan can be useful:


![nmap-image](assets/fr/87.webp)


tCP ACK Scan behavior diagram for filtered and unfiltered ports


We'll use Nmap's `-sA` option to perform this type of scan. Here's the result of a TCP ACK scan if the port is filtered, i.e. blocked and protected by a firewall:


![nmap-image](assets/fr/88.webp)


nmap display during TCP ACK Scan._


Example result for a host with a firewall and one without. Nmap returns `filtered` on ports TCP/80 and TCP/81 of host `10.10.10.203`. On a network analysis via Wireshark, the behavior is as follows:


![nmap-image](assets/fr/89.webp)


network capture during a TCP ACK scan for a port not filtered by a firewall


The target machine returns nothing if a firewall is present.


To launch this scan with Nmap, use the `-sA` (`scan ACK`) option:


```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```


### V. Conclusion


We've looked at three different methods of scanning via TCP in addition to those already presented. These different methods are to be used in very specific conditions and contexts, notably in the context of penetration tests or Red Team operations, during which notions of discretion are present.


## 15 - Nmap CheatSheet - Summary of tutorial commands


### I. Presentation


Here's a short summary of Nmap's many commands and use cases, so that you can quickly find and reuse them in everyday use.


### II. Nmap: CheatSheet IT-Connect


Here's a cheatsheet of the commands presented. This page makes it easy to find the most common uses of Nmap.



- Port scan



```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



- Discovering active hosts



```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```


note: The `-sP` option has been obsolete for several years and should be replaced by `-sn`. (Update 2025)_


```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



- Version detection



```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```



- NSE scripts: looking for vulnerabilities



```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



- Nmap output management



```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



- Performance optimization



```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



- TCP scan types



```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```


I hope you find these commands useful. Don't forget to adapt the target of your scans to your context and to refer to the official documentation to fully master the tests performed.


### III. Conclusion


The Nmap tutorial is now complete. You now have the basics you need to use this comprehensive and powerful tool. We strongly advise you to practice on controlled environments (Hack The Box, VulnHub, virtual machines) before using it in production.


Much remains to be explored about the tool's inner workings and advanced features. However, mastery of the commands and concepts presented here will enable you to use Nmap with confidence and relevance.