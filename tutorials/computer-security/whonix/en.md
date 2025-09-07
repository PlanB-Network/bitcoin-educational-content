---
name: Whonix
description: Preserve your privacy and confidentiality.
---

![cover](assets/cover.webp)


**Whonix** is a Linux distribution based on **Debian**, designed to provide an environment combining **security**, **anonymity** and **privacy**. Easy to learn, and compatible with different interfaces (virtual machines, Qubes OS, Live mode), it includes by default network traffic routing via **Tor**, **double firewall** (one firewall on the Gateway and another on the Workstation), **full protection against IP/DNS leaks** and tools to effectively mask your activity from network observers, including your ISP. More than just an anonymous system, **Whonix** is a complete secure development environment.


## Why choose Whonix?



- Free**: Like most Linux distributions, Whonix is an open-source system licensed completely free of charge. It is developed in open source, with an active and transparent community.
- Privacy, security and anonymity**: Whonix's main objective is to offer an ultra-secure environment, in which all your data is protected and your communications encrypted via the Tor network.
- Easy to use**: Whonix offers an intuitive, pre-configured graphical Interface, suitable even for novice users. No need to be an expert to benefit from advanced protection.
- Ideal environment for secure development**: Whonix lets you develop, test, audit or run programs without ever revealing your real IP address or exposing your browsing or network communication habits.
- Disposable sessions and Live mode**: Whonix can be launched in Live mode or via disposable machines (e.g. via **Qubes OS**), enabling critical tasks to be carried out without leaving persistent traces once the session has ended.
- Relatively simple installation**: Ready-to-use images are supplied for rapid installation in virtual machines (VirtualBox, KVM, Qubes). The system is documented and regularly updated.


## Installation and configuration


Before moving on to Whonix installation, it's essential to note that this distribution **is not yet officially available** as a main system that can be installed directly on the hard disk (in bare metal mode). In other words, you **can't yet install Whonix as a classic host operating system**, like Ubuntu or standard Debian.


However, several editions are available, allowing Whonix to be used **volatile** (Live mode, temporary sessions) or **persistent** (via virtual machines or integration in Qubes OS).


For long-term, stable use, **virtualization is currently the only officially recommended method**. You can run Whonix using **VirtualBox** (Whonix-Gateway and Whonix-Workstation) or integrate it into a system like **Qubes OS**. In this tutorial, we'll focus on a VirtualBox installation.


### Prerequisites


Before you can install Whonix in virtual mode, make sure your machine meets the minimum technical requirements. Virtualization requires certain resources that not all computers can offer. It is therefore essential that your processor supports virtualization technology (Intel VT-x or AMD-V), and that this option is enabled in the BIOS/UEFI.


Here are the recommended specifications for a smooth and stable experience with Whonix:



- Random Access Memory (RAM)**: a minimum of **8 GB** is strongly recommended. The more RAM you have, the more resources you can allocate to the virtual machines (Gateway and Workstation), improving performance.
- Available disk space**: please allow at least 30 GB of free disk space**. This includes the space required for the two virtual machines, system files and any data or snapshots.
- Processor**: a processor with at least **4 physical cores** (8 logical threads) is recommended, especially if you want to run other services or tools in parallel.


### Download Whonix


Whonix is available in several editions, depending on the type of environment you want to use it in. For most users (Windows, Linux or MacOs), the VirtualBox edition is the easiest to set up. You can download the image directly from [the official website](https://www.whonix.org/wiki/VirtualBox).


⚠️ Whonix **is not compatible** with MacBooks using Apple Silicon processors (ARM architecture).


## Installing VirtualBox


To run Whonix, you'll need a **hypervisor** like VirtualBox, Qubes or KVM.


Once you've downloaded the file, install it as you would any other software. Accept the default options unless you have specific requirements. Are you lost? Check out our guide to using VirtualBox.


https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importing Whonix


Once VirtualBox has been installed, you can import the Whonix `.ova` files you downloaded earlier (`Whonix-Gateway-Xfce.ova` and `Whonix-Workstation-Xfce.ova`).


Open VirtualBox, then click on **File → Import appliance**.

Select the corresponding `.ova` file (start with the Gateway).


![0_03](assets/fr/03.webp)


Choose the location where the Whonix virtual machine files will be stored.


![0_04](assets/fr/04.webp)


Accept the terms of use, then launch the import and wait for the process to finish.


![0_05](assets/fr/05.webp)


![0_06](assets/fr/06.webp)

### Whonix configuration


Before starting Whonix, it's important to adjust some **system settings** to ensure better performance:


Select the **Whonix-Workstation-Xfce** virtual machine, then click on **Configuration**.


![0_06](assets/fr/07.webp)


Go to the **System** tab, where the default RAM allocation is 2048 MB. We recommend that you **increase it to 4096 MB (4 GB)** for greater fluidity, especially if you intend to open several applications or work in long sessions. The Gateway can remain at 2048 MB, unless you're using a lot of Tor connections in parallel.


![0_08](assets/fr/08.webp)


### Getting started with Whonix


For Whonix to work properly and securely, **you must follow this startup sequence**:


First, start the **Whonix-Gateway-Xfce** machine. This machine is responsible for routing all traffic through the **Tor** network. Without the gateway running, no traffic will be routed via Tor and you'll lose anonymity.


![0_09](assets/fr/09.webp)


Once the Gateway is fully launched (you'll see Tor connected), you can start **Whonix-Workstation-Xfce**, which will automatically connect via the Gateway.


![0_10](assets/fr/10.webp)


![0_11](assets/fr/11.webp)


### System update


Enter the terminal, insert the following command to update the list of packages:


```shell
sudo apt update
```


Then run the following command to install the available updates:


```shell
sudo apt full-upgrade
```


## Discover Whonix


**Whonix** is a system designed to provide a **secure**, **anonymous** and **confidential** computing environment, ideal for surfing the Internet without compromising your identity or your data. To achieve this, it comes with a number of useful everyday applications designed to reinforce your digital security right from the start.

### KeepassXC


**KeePassXC** is Whonix's integrated password manager. It lets you **create, store and manage** your passwords securely, without having to remember them all manually. Passwords are stored in an **encrypted database**, protected by a master password.


### Tor Browser


**Tor Browser** is Whonix's default web browser. It relies on the **Tor** network, which redirects your traffic through several relays around the world, making it virtually impossible to identify your real IP address.


https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet


**Electrum** is a light and fast Bitcoin wallet, preinstalled on Whonix to let you manage **cryptocurrency transactions** anonymously. It doesn't download the whole Blockchain but uses remote servers to obtain the necessary information, making it much lighter than a full Wallet.


https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix is more than just an operating system: it's a genuine **secure environment** designed to protect your anonymity, your privacy and your sensitive activities. Thanks to its Tor-based architecture, intelligent partitioning between Gateway and Workstation, and pre-installed tools such as Tor Browser, KeePassXC and Electrum, it offers a turnkey solution for anyone wishing to **browse anonymously**, **work securely** or **handle confidential data**.


To strengthen your security on your Unix system, take a look at our tutorial on auditing your machine: check for security holes in your operating system and make sure your data isn't compromised.


https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af