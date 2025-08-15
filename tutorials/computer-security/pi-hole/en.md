---
name: Pi-Hole
description: An ad blocker for your entire network
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian Duchemin published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


We've all done it as soon as we start up our favorite browser: install an **adblocker** (ad blocker). However, when using the TV browser or an Android device, etc... It's a bit trickier to find something that works. And if there's more than one device in the house, well, you have to repeat the operation for each browser!


In this tutorial, we're going to solve a simple problem**: provide an ad blocker to all the machines on our network and manage it centrally.**


To do this, we will use a tool developed for this purpose: **Pi-Hole**


Pi-Hole is a DNS sinkhole. It will use the DNS requests made by your devices to validate or deny traffic, thus protecting you from addresses and domains known to be distributing advertising, malware and so on.


DNS stands for Domain Name System. So what is a domain name? Well, "it-connect.fr" is just one example. A domain name is a unique identifier for one or more resources, usually administered by a single entity.


The machine name plus the domain name is called FQDN for *Fully Qualified Domain Name*. It allows you to reach a specific machine just by "calling" it. For example, when you type "www.trucmachin.com", you're actually calling the machine "www", which belongs to the domain "trucmachin.com".


Except that our computers don't understand human language, all they understand is binary, so they need an IP address, which is the equivalent of a telephone number, to reach the website.


So every time you enter the name of a website in your browser, or click on a link, your computer first asks a DNS server for the IP address corresponding to that name.


**Pi-Hole will then inspect these requests (there are hundreds of them every day!) and automatically block those known to host advertisements or even malicious files


## II. Installing Pi-Hole


With a name like Pi-Hole, you might rightly assume that you need a Raspberry-Pi... But that's not quite true. **Pi-Hole can be installed on any Linux computer (Debian, Fedora, Rocky, Ubuntu, etc.)


On the other hand, you need to bear in mind that **this device will have to run 24 hours a day for a simple reason: no DNS, no Internet!** The Raspberry is therefore a good idea, since it consumes almost no energy.


To install, simply connect to your Linux machine via SSH and enter the following command as "*root*":


```
curl -sSL https://install.pi-hole.net | bash
```


> **Note**: under normal circumstances, it's not advisable to "hack" a script without first knowing what it does. If you're not sure, go to the page with a browser or download the content as a file.
>

> **Note: on minimal versions of Debian 11, Curl is not installed, so you need to install it manually with the **apt-get install curl** command before typing the above command.

Once the script has run, a series of tests will be performed, and the installation itself will take care of itself:


![Image](assets/fr/019.webp)


Installing Pi-Hole


Once installation is complete, you will be taken to this screen:


![Image](assets/fr/020.webp)


Pi-Hole starter screen


> **Note**: if you're using DHCP on your machine, you'll get a warning message about this. Of course, for proper use, we strongly recommend that you assign a fixed IP to your machine.

Following this screen, you'll get a few information messages, and then you'll be taken to the configuration wizard, which will first ask you which DNS server Pi-Hole will be forwarding requests to. For my part, I've chosen Quad9, which has a user privacy charter.


![Image](assets/fr/021.webp)


DNS selection - Pi-Hole


> **Note: if you're in a company, chances are your current DNS server is the Active Directory domain controller. But don't worry, you can later specify a conditional redirector for a domain of your choice. Typically, you'll be able to redirect any request concerning your local domain to your DNS server.

You'll notice that some choices include a DNSSEC option. Basically, the DNS protocol isn't secure (it wasn't designed with this in mind at the time). DNSSEC solves this problem by adding a layer of security through encryption and signing of exchanges, as explained in the corresponding article: [DNS Security](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)


Any ad blocker relies on one or more lists to do its job. Pi-Hole comes with a single list as standard, so select it and add more later.


![Image](assets/fr/022.webp)


Come the question about Interface web, its installation is optional, as the tool has its own command line for management and visualization. But this Interface is rather pleasant and well done, so I recommend that you install it at the same time:


![Image](assets/fr/023.webp)


If you're installing Pi-Hole on a machine that already has a Web server, you can answer "no" to the following question. Please note, however, that PHP and several modules are required for this to work. Otherwise, **lighttpd will be installed with all the necessary modules**.


![Image](assets/fr/024.webp)


You are then asked if you wish to record DNS requests. **If you'd like to keep a history, set this to yes; otherwise, set this to no, but you'll lose some of the functionality** (see next screen).


![Image](assets/fr/025.webp)


For its Interface web, Pi-Hole uses a function of its own called FTLDNS, which provides an API and generates statistics from DNS requests. This function can include a "privacy" mode that masks the domains requested, the customers behind the request, or both. Handy if you want to do monitoring without infringing on people's privacy, or simply if you want to comply with the relevant regulations in the case of use on a public network.


![Image](assets/fr/026.webp)


Choice of private lifestyle


Once this last question has been answered, the script will do what it's supposed to: download the GitHub repositories and configure Pi-Hole. At the end of the installation, a summary screen will be displayed with the important info:


![Image](assets/fr/027.webp)


Installation summary screen


Make a note of the Interface web password and network information. Now it's time to configure the DHCP service at our current location.


## III. DHCP configuration


In order to function, Pi-Hole needs to "resolve" DNS requests from clients, so they must know that it's the one to send them to. There are several ways of doing this:



- Modify DNS settings in your DHCP server (e.g. your Box)
- Disable this server and use the one provided by Pi-Hole
- Manually modify each device to use Pi-Hole as DNS


I personally choose the first solution. Chances are **you've got a DHCP server where you are** (usually your box). So there's no need to bother.


As there are a large number of possibilities, between the different operators' boxes (which I don't know about all) and those who have their own router, I'm not going to provide a screenshot for these modifications. In any case, you'll need to go to the DHCP settings and modify the "DNS" parameter to include the IP address of your Pi-Hole.


Once this has been done, if any devices have been switched on before, they will have retained the old settings, so you'll need to restart the configuration request.


On Windows workstations, with a command prompt :


```
ipconfig /renew
```


On a Linux workstation :


```
dhclient
```


For all other devices, they must be switched off and on again.


So they should get the right parameters, to check:


```
ipconfig /all
```


In the DNS field, you should have the address of your Pi-Hole, in my case 192.168.1.42 :


![Image](assets/fr/029.webp)


## IV. Using the Interface web Pi-Hole


To facilitate administration, **Pi-Hole** benefits from a well-designed Interface web interface. User-friendly and accessible, it lets you :



- View the number of requests, blocked requests, etc. in real time.
- Manage your Whitelist and Blacklist
- Add static entries, aliases, etc.
- Add lists
- And many other functions!


For my part, I'm going to add a blocking list. As mentioned above, only one list was installed at the same time as Soft. There are many lists for ad sites, but it's best to choose at least one specific to the country you live in. One of the best-known lists is **EasyList**, and one of them is specific to France: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)


To add it, first connect to the Interface admin: **http://<ip_du_PiHole>/admin**


The administrator password has already been generated (see end-of-installation screenshot), so all you need to do is enter it to access Interface :


![Image](assets/fr/030.webp)


Interface from Pi-Hole


We can see, for example, that there are two customers connected to the Pi-Hole, that it has processed 442 requests and that 8 of these have been blocked. These graphs can be a good source of information, especially in a professional context.


To add our list, go to the "**Group Management**" and "**Adlists**" menus:


![Image](assets/fr/031.webp)


We can see our first list "**StevenBlack**", to add ours, copy the link I gave you above and insert it in the field "**Address**", for the description, I choose to put the name of the list:


![Image](assets/fr/032.webp)


Adding a list in Pi-Hole


All that remains is to click on "**Add**" to add it. To activate it, we need to perform an additional step to "warn" Pi-Hole to take over this list. To do this :



- Either use the built-in command line
- Either the Interface web


I personally chose the second one, because if you've looked carefully, the link to the PHP script that performs the update is directly on the page we're on (the word "online"). So all you have to do is click on it, which will take you to a page with only one option:


![Image](assets/fr/033.webp)


The page will display the result of the script once completed, meaning that the list has been taken into account (unless an error message is displayed, of course).


As announced at the start of this tutorial, Pi-Hole also lets you **block domains known to distribute malware. To reinforce this feature, I suggest you also add the regularly updated domain list distributed by Abuse.ch**, which will significantly strengthen the security of your network, available at [this address](https://urlhaus.abuse.ch/downloads/hostfile/).


You can, of course, add any lists you think are relevant, or manage your blacklist manually via the blacklist menu.


## V. Pi-Hole tests


Now that everything is in place, all you have to do is test the solution to make sure it's working properly.


For example, I will try to reach the domain *http://admin.gentbcn.org/* which is on the Abuse.ch list because it is known to host malware:


![Image](assets/fr/034.webp)


Obviously, I've been blocked somewhere. To make sure it's the Pi-Hole that's done the job, we can check the query log in the Interface web "Query Log" to see that it's a block from a list entry:


![Image](assets/fr/035.webp)


## VI. Conclusion


In this tutorial, we've shown you how to set up a DNS server that not only eliminates most of the ads for your browsing comfort, but also adds **a layer of security by blocking phishing and malware-spreading domains**.


All free of charge and economical if installed on a Raspberry-Pi (in terms of power consumption).