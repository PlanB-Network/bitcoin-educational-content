---
name: Lynis
description: Perform a security audit of a Linux machine with Lynis
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Fares CHELLOUG published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


**In this tutorial, we're going to learn how to perform a security audit on a Linux machine using Lynis! For those of you who don't know **Lynis,** it's a small command-line utility that will analyze your server's configuration and make recommendations for **improving the security of your machine.**


Lynis is an open source tool from CISOFY, a company specializing in **system auditing and hardening**. If you want to make progress in hardening Linux and popular services (SSH, Apache2, etc.), Lynis is your ally! Lynis not only tells you what's going wrong, but also provides recommendations to point you in the right direction (and save you time).


**Lynis** works with most Linux distributions, including: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis is aimed at Linux / UNIX users, but is also **macOS** compatible. Very quick to install, there's no dependency management at package level.


It is used for a variety of purposes:



- Safety audits
- Compliance testing (PCI, HIPAA and SOX)
- Tougher system configurations
- Vulnerability detection


The tool is widely used by a wide range of users, including system administrators, IT auditors and pentesters. For analyses, the tool is based on standards such as **CIS Benchmark, NIST, NSA, OpenSCAP** and on official recommendations from **Debian, Gentoo, Red Hat**.


The project is available at this address on **Github**:



- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Download Lynis from CISOFY](https://cisofy.com/lynis/#download)


In this step-by-step tutorial, I'm going to **use a VPS running Debian 12** and I'm going to concentrate on the SSH part, as I'd like to check its configuration and improve it.


## II. Download and installation


There are several ways to download and install Lynis. Choose the one you prefer from the list below.


### A. Installation from Debian repositories


This installation mode allows you to use the **lynis** command from anywhere on the system, unlike installation from source, where you need to be located in the directory.


Connect to your server via SSH and enter the following commands to install Lynis:


```
sudo apt-get update
sudo apt-get install lynis -y
```


This is what you get:


![Image](assets/fr/024.webp)


### B. Download from the official website


You can also download it from the Cisofy website:


```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```


This is what you get:


![Image](assets/fr/032.webp)


Next, we'll unpack the archive using the following command:


```
sudo tar -zxf lynis-3.0.9.tar.gz
```


This is what you get:


![Image](assets/fr/020.webp)


Let's move to the **lynis** folder:


```
cd lynis
```


We can check for updates with the following command:


```
./lynis update info
```


This is what you get:


![Image](assets/fr/023.webp)


### C. Download from GitHub


We'll download **Lynis** from the official GitHub repository, using the following command (*git* must be present on your machine):


```
git clone https://github.com/CISOfy/lynis.git
```


This is what you get:


![Image](assets/fr/060.webp)


## III. Using Lynis


Lynis is present on our machine, so let's learn how to use it!


### A. Main controls and options


To display the available commands, simply enter the following command:


```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```


This is what you get:


![Image](assets/fr/039.webp)


And you also get the following options:


![Image](assets/fr/040.webp)


To display all available commands, enter the following command:


```
sudo lynis show
```


This is what you get:


![Image](assets/fr/022.webp)


If you wish to display all the options, you must enter:


```
sudo lynis show options
```


This is what you get:


![Image](assets/fr/021.webp)


In the rest of this article, we'll learn how to use certain options.


### B. Performing the system audit


We're going to ask **Lynis** to audit our system, highlighting what is correctly configured and what could be improved. To do this, enter the following command:


```
sudo lynis audit system
# ou
./lynis audit system
```


By default, if you are not logged in as root when you run this command, the tool will run with the privileges of the currently logged-in user. Some tests will not be run in this context:


![Image](assets/fr/052.webp)


Here are the tests that will not be performed in this mode:


![Image](assets/fr/051.webp)


Once the command has been executed, the analysis starts. Just wait a moment.


At the end of the audit, you get this (we can see that **Lynis** has correctly identified the **Debian 12** system and will use the **Debian plugin** for the analysis):


![Image](assets/fr/017.webp)


Next, Lynis will list a set of points corresponding to everything he has checked on our system. This is organized by category, as we shall see. It's also worth noting that a color code is used to highlight recommendations:



- Red** for critical elements or best practices not respected (a missing package, for example), i.e. your server does not respect this point
- Yellow** for suggestions or partial compliance with the recommendation (let's say it's a plus to comply with a point highlighted with this color (non-priority))
- Green** for points where your server configuration is compliant
- White**, when neutral


Here, we can see that Lynis recommends installing **fail2ban**:


![Image](assets/fr/057.webp)


In the "**Boot and services**" section, we see that service protection via *systemd* could be improved. On the positive side, Grub2 is present and there are no problems with permissions on:


![Image](assets/fr/029.webp)


Then you have the "**Kernel**" and "**Memory and Processes**" sections:


![Image](assets/fr/037.webp)


Next, the "**Users, Groups and Authentication**" section. The tool informs us of a warning on the permissions of the "**/etc/sudoers.d**" directory. For the moment, we don't know more, but we'll be able to see what the recommendation is at the end of the analysis.


![Image](assets/fr/049.webp)


Here's what you can find in the "**Shells", "Files Systems", and "USB Devices "** sections. Among other things, we can see that there are suggestions on mount points and that USB devices are currently allowed on this machine.


![Image](assets/fr/048.webp)


Next, the sections: "**Name services", "Ports and packages", "Networking".** It indicates here that packages no longer in use could be purged and that there is no utility capable of managing automatic updates.


![Image](assets/fr/058.webp)


We can see that a firewall is activated (and yes, there's iptables!). In addition, we can see that it has found unused rules and that an Apache web server is installed.


![Image](assets/fr/055.webp)


This is followed by an analysis of the web server itself, since the service has been identified.


We can see that it has found **Nginx** configuration files, and that for the SSL/TLS part, the **ciphers** are configured with the use of a protocol that would be insecure. On the other hand, according to Lynis, log management is correct.


![Image](assets/fr/038.webp)


The SSH service is present on my VPS server. Its configuration is analyzed by Lynis. It has to be said that SSH security can easily be improved! We'll be coming back to this area in detail once we've obtained the recommendations.


![Image](assets/fr/026.webp)


Here are the sections **"SNMP Support", "Databases", "PHP", "Squid Support", "LDAP Services", "Logging and files "**.


There's one really important suggestion about log management: it's strongly recommended that you don't just store logs locally on your machine. If the machine were corrupted by an attacker, it's likely that he'd try to erase his traces... So we need to externalize the logs.


![Image](assets/fr/050.webp)


Here, we have the audit of vulnerable services, account management, scheduled tasks and NTP synchronization.it is indicated that the level is low on the banner and identification part: this is understandable, if you display the system version, it gives an indication to a potential attacker. This is the default setting.


It would be interesting to activate **auditd** to have logs in case of **forensic** analysis. The **NTP** is also checked, because to search logs efficiently, it's preferable to have systems on time, which simplifies the search.


![Image](assets/fr/036.webp)


Lynis then looks at cryptographic elements, virtualization, containers and security frameworks. Some sections are empty because there is no correspondence with the machine analyzed. However, we can see that I have two expired SSL certificates and I haven't activated **SELinux**.


![Image](assets/fr/027.webp)


Here too there's room for improvement: there's no anti-virus or anti-malware scanner, and we have suggestions on file permissions.


![Image](assets/fr/028.webp)


Next, Lynis focuses on tightening up Linux kernel configuration (including rules for the IPv4 stack), as well as management of the Linux machine's "Home" directories.


![Image](assets/fr/035.webp)


We've come to the end of the analysis... This last point shows that we would have everything to gain from having ClamAV on this machine.


![Image](assets/fr/030.webp)


## IV. Recommendations


After the audit, it's time to read and analyze the recommendations. This is where we get the recommendations and explanations for each of the tests carried out by Lynis.


Take the SSH recommendations, for example. **For each suggestion, you'll find the recommended parameter and a link that will explain the security point ** It's up to you to decide, depending on your context and usage.


Let's take a look at a few examples of recommendations that directly echo the points highlighted throughout the audit...


### A. Examples of recommendations



- As we saw earlier, NTP is important for time-stamping logs:


![Image](assets/fr/043.webp)



- Lynis also suggests installing the **apt-listbugs** package to get information on critical bugs during package installations via **apt.**


![Image](assets/fr/041.webp)



- The tool suggests we install **needrestart to be able** to see which processes are using an old version of the library and need to be restarted.


![Image](assets/fr/054.webp)



- This suggestion suggests installing **fail2ban** to automatically block hosts that fail to authenticate (notably brute force).


![Image](assets/fr/044.webp)



- To harden system services, he recommends we run the blue command for each service on our machine.


![Image](assets/fr/056.webp)



- He suggests setting expiry dates for all protected account passwords.


![Image](assets/fr/031.webp)



- This suggestion suggests setting minimum and maximum values for the age of a password. Among other things, this will ensure that passwords are changed regularly.


![Image](assets/fr/042.webp)



- We recommend using separate partitions, to limit the impact of disk space problems on one partition.


![Image](assets/fr/047.webp)



- This recommendation suggests disabling USB storage and firewire to prevent data leakage


![Image](assets/fr/033.webp)



- To meet this recommendation, simply install and configure **unnatended-upgrade**, for example.


![Image](assets/fr/053.webp)


### B. Installing recommended packages


To improve system configuration, we're going to install some packages on the machine: some recommended by Lynis, some that I personally recommend.


You'll have a good basis on which to work, as long as you spend a little time configuring them. To do this, refer to the IT-Connect site, other articles on the Web and tool documentation.


```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```


Some information about the installed packages:



- Clamav** is an antivirus.
- unattend-upgrades** will enable you to manage your updates automatically and even reboot the machine or automatically purge old packages, it's fully configurable.
- rkhunter** is an anti-rootkit that scans your file system.
- Fail2ban** will base itself on your log files according to what you give it to read and it will work with **iptables**, for example to ban IP addresses that try to "brute force" your server in SSH.


### C. Recommendations for SSH


Let's take a look at the SSH recommendations. They are listed below. Don't worry, we'll immediately explain how to improve the configuration.


![Image](assets/fr/034.webp)


Let's take a closer look at my current **SSH** configuration in:**/etc/ssh/sshd_config**


![Image](assets/fr/018.webp)


The configuration suggested below can still be optimized, but gives you a good base. *Please note that I've removed a number of comments for greater readability*.


We will:



- Change SSH connection port (forget the default 22)
- Increase the verbosity level of logs, from **INFO to VERBOSE**
- Set **LoginGraceTime** to **2 minutes**


If no connection information is entered within two minutes, the connection is disconnected.



- Activate **strictModes**


Specifies whether "sshd" should check the modes and owner of the user's files as well as the user's home directory before validating a connection. This is normally desirable, because sometimes novices accidentally leave their directory or files fully accessible to everyone. The default is "yes".



- Set **MaxAuthtries** to 3


This represents the number of failed authentication attempts before the communication is closed.



- Set **MaxSessions** to 2


This represents the maximum number of simultaneous sessions.



- Enable public key authentication


```
PubkeyAuthentication yes
```



- Retain password authentication:


```
PasswordAuthentication yes
```


Forbid empty passwords and **Kerberos** authentication, as well as **direct root authentication**


```
PermitEmptyPasswords no
PermitRootLogin no
```


Make sure you have "**PermitRootLogin no", if it's equal to "yes", it's "absolute evil "**.



- Forbid TCP connection redirection


```
AllowTcpForwarding no
```


Indicates whether TCP redirects are allowed, with "yes" as the default setting. Please note: disabling TCP redirects does not enhance security if users have access to a shell, as they can still set up their own redirection tools.



- Prohibit X11 redirection


```
X11Forwarding no
```


Indicates whether X11 redirects are accepted, with "no" as the default setting. Please note: even if X11 redirects are disabled, this does not increase security, as users can still set up their own redirectors. X11 redirection is automatically disabled if **UseLogin** is selected.



- Set the communication timeout between the client and sshd


```
ClientAliveInterval  300
```


Defines a timeout in seconds, after which, if no data is received from the client, the sshd service sends a message requesting a response from the client. By default, this option is set to "0", meaning that these messages are not sent to the client. Only version 2 of the SSH protocol supports this option.


```
ClientAliveCountMax 0
```


According to the [documentation (*man page*) for sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), here's what this option means: "Sets the number of hold messages (see above) to be sent without a response from the client for **sshd**. If this threshold is reached while the hold messages have been sent, **sshd** disconnects the client and terminates the session. It's important to note that these hold messages are very different from the **KeepAlive** option (below). Connection hold messages are sent through the encrypted tunnel, and are therefore not forgeable. TCP-level connection hold enabled by **KeepAlive** is forgeable. The connection hold mechanism is of interest when the client or server needs to know whether the connection is idle."



- Prevent information disclosure by disabling **motd, banner, lastlog**


```
PrintMotd no
```


Specifies whether sshd should show the contents of the "/etc/motd" file when a user logs on in interactive mode. On some systems, this content may also be displayed by the shell, via /etc/profile or a similar file. The default value is "yes".


```
Banner none
```


It is worth noting that in some jurisdictions, sending a message prior to authentication may be a prerequisite for legal protection. The contents of the specified file are transmitted to the remote user before connection authorization is given. This option needs to be configured, as by default no message will be displayed.


In images, this gives:


![Image](assets/fr/019.webp)


### D. Audit score


Finally, let's not forget to check the **Lynis audit score**! We see that **my Hardening score is 63** and that the report file can be viewed in "**/var/log/lynis-report.dat**". There's also the file "**/var/log/lynis.log**".


**In other words, the higher the score, the better! You therefore need to work on your configuration to achieve the highest possible score, while allowing your machine and hosted services to function normally (which means carrying out functional tests).


![Image](assets/fr/046.webp)


Let's take a look at the results on my second server, where I spent a little more time hardening! So it's normal that the score is higher (**76**).


![Image](assets/fr/045.webp)


## V. Lynis automated planning


**Lynis** also offers the option of running its checks via a scheduled task. There is in fact the **"--cronjob "** option, which will run all Lynis tests without the need for validation or user action. You can then very simply create a script that will run **Lynis** and put the output in a time-stamped file with the name of the server in question. Here's a file of this type that you can put in the */etc/cron.daily* folder:


```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```


The **"AUDITOR_NAME "** variable is simply a variable that we'll set in the **"--auditor "** option of **Lynis** so that this name is displayed in the report:


![Image](assets/fr/059.webp)


We're also going to create a few contextual variables that will help us organize ourselves better, such as the host name and date for naming the report and time-stamping it, and the path to the folder in which we want to put our reports.


## VI. Conclusion


Lynis is a very practical tool that will help you save time and be more efficient when you want to know more about the state of a Linux server's configuration, particularly in terms of security. However, don't forget that every modification must be tested before being applied in production, taking into account your own usage and context.


You're probably not going to apply the same configuration for a VPS exposed to the Net, where you only need one SSH connection (because you're the only person connecting), unlike a **bastion** or **scheduler** which will need to multiply **SSH.** connections


Once you've got a configuration that suits you in terms of hardening, it's advisable to adopt an automation tool so that you don't have to redo the tasks manually, as this would be time-consuming and error-prone. For example, you can use **: Puppet, Chef, Ansible, etc...**


Don't forget to communicate with your teams before implementation: you need to make them understand why you're making these changes, not just tell them you're making them. In the end, the aim will be to pass on good practices, and this will increase your chances of success.


Finally, you can also compare **Lynis** with other tools, of which there are several. If you want to move towards centralized management while remaining open source, I recommend the [Wazuh] tool (https://wazuh.com/).


**This tutorial is over, have fun with Lynis!