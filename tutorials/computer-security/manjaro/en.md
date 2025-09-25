---
name: Manjaro
description: Making the power of Arch Linux more accessible
---
![cover](assets/cover.webp)


Arch Linux is a popular operating system in many fields, thanks to its robustness and stability. However, it can be difficult for novice users to get to grips with. It's precisely to address this problem that **Manjaro** was created: to offer the power of Arch Linux, but with a simpler, more accessible experience, based on an intuitive, easy-to-learn Interface.


## Getting started with Manjaro


One of Manjaro's greatest assets is its **simple and efficient update system**. No need to manage them manually: Manjaro takes care of them for you! An icon in the notification area (location varies according to edition) alerts you when an update is available. All you have to do is follow the instructions, and the process is fast and effortless.


Manjaro also offers a **vast catalog of applications**. Since Manjaro is based on Arch Linux, it benefits from direct access to its official repositories, rich in a variety of software, including proprietary applications. Manjaro slightly delays some Arch Linux updates for additional testing; this improves stability at the cost of a slight delay in new releases. And if this choice isn't enough for you, you can also access the **AUR (*Arch User Repository*)**, a huge library managed by the community. If a program doesn't exist in the official repositories, chances are it's available in the AUR.


Another advantage of Manjaro is that it is **much less resource-hungry** than systems like Windows or macOS. It consumes less RAM and computing power, making it an ideal choice for older or less powerful computers: your machine gains in fluidity and speed, regaining a second youth.


On top of all that, Manjaro is **entirely free**. Unlike Windows or macOS, you don't have to pay anything to install it and get the most out of it. Finally, it offers **enhanced security** thanks to regular, rapid updates, limiting exposure to vulnerabilities. Its active community also ensures that any problems are quickly corrected and effective solutions proposed.


## Discover Manjaro OS


Before you start installing Manjaro, it's important to know that this distribution is available in several editions. Each of these editions offers a unique desktop environment that influences both your workflow and the consumption of system resources. There are three main official editions of Manjaro.


![0_01](assets/fr/01.webp)



- The **KDE Plasma** edition is the most customizable. If you're looking for a system that's both visually elegant and high-performance, KDE Plasma is an excellent choice. This stable desktop environment is ideal for users who want total control and a tailored experience.



- For machines with more limited resources, the **Xfce** edition is the ideal solution. Its Interface is lightweight and intuitive, guaranteeing smooth operation even on older computers. What's more, its layout is reminiscent of Windows, making the transition to Linux easier for new users.



- Finally, the **GNOME** edition offers a totally different approach. Its streamlined design emphasizes productivity and organization through virtual workspaces. This activity-focused workflow is particularly appealing to users already familiar with Linux and looking for a minimalist, highly efficient environment.


### Other Manjaro editions


![0_02](assets/fr/02.webp)


In addition to the official editions, the Manjaro community also offers other versions. These alternative editions are designed to meet specific needs and offer a variety of desktop environments.


The **Cinnamon** edition is an excellent choice if you're just starting out and are looking for a familiar Interface. It has been designed to be easy to use, while retaining the classic conventions of traditional office environments.


For more advanced users, there are editions such as **i3 Window Manager** or **Sway**. Much lighter and faster, they nevertheless require a good command-line mastery to be fully configured and exploited. These environments are ideal for those who want total control over their system, and who place efficiency above all else.


## Technical requirements


For Manjaro to work optimally, your computer must meet a few minimum requirements. We recommend that you have at least :



- A 64-bit (x86_64) processor
- **4 GB RAM recommended (minimum 2 GB)** (see below)
- 30 GB of disk space (more if you create a dedicated `/home` partition)


## Manjaro installation


To download, go to [the official Manjaro website](https://manjaro.org/) and choose the edition that best suits your needs. Once you've downloaded the file, you'll need to create a bootable USB key with the Manjaro ISO image.


Then go to the [Rufus] software website (https://rufus.ie/fr/) and download it. Run the program, plug in your USB key, select the Manjaro ISO image and start flashing. Wait for the process to finish before removing the key. You can then restart your computer.


![0_03](assets/fr/03.webp)


To install Manjaro on your computer, first switch it off completely. Then plug in the USB key, switch the machine back on and access the boot menu or UEFI/BIOS firmware by pressing **F2, F10, F12, Escape** or **Delete** (depending on manufacturer).


Then choose the USB key as the boot device to start the OS installation process.


### Startup screen


The first time you launch Manjaro from the USB key, you'll be taken directly to the installation menu. Before launching the installation, you can change the keyboard layout or the system language.


Then select the **Boot with open source drivers** option to start the Manjaro installation. These open-source drivers are compatible with most hardware and will suffice in most cases. If you have an NVIDIA graphics card, for example, or require higher graphics performance, you can choose **Boot with proprietary drivers**, which uses proprietary drivers.


![0_04](assets/fr/04.webp)


The system will launch in **default live mode**. This allows you to test Manjaro's functionality to see if it suits your needs before installing it permanently. Once ready, click on the **Install Manjaro Linux** option.


Select the desired language for your installation, then click **Next**.


![0_06](assets/fr/06.webp)


Then choose your location to set the correct time zone. At this stage, you can also change the language and date format.


![0_07](assets/fr/07.webp)


Select keyboard layout. A test field is available to check that the keys typed correspond to the expected characters.


![0_08](assets/fr/08.webp)


### Disk partitioning

You have two options for partitioning your disk.



- The first, and simplest, is to erase the entire disk and install Manjaro on it.
- The second allows **manual partitioning**.


![0_09](assets/fr/09.webp)


For a clean installation, we recommend creating at least three partitions:



- A first partition of **516 MB** (primary) for the **boot**.
- A second **2 GB** (logical) partition for **swap**.
- A third partition for your **personal data**.


If you wish to install another system in parallel, you need to divide this last partition and allocate only one part to Manjaro (at least **15 GB** to guarantee proper system operation).

### Creating a user account


Create a user account on the system by filling in the required information. Finally, set the administrator's password (**root**). This administrator is a **super-user** with full rights on the system and the ability to execute advanced commands.


![0_10](assets/fr/10.webp)


### Choose the right office suite


Manjaro lets you choose between **FreeOffice** and **LibreOffice**.



- **LibreOffice** is more complete, with a wider range of software and advanced features.
- **FreeOffice**, on the other hand, is lighter and includes only the essentials: **TextMaker**, **PlanMaker** and **Presentations**.


![0_11](assets/fr/11.webp)


### Configuration summary


A summary screen shows you all the parameters you've set. You can go back to make changes if necessary, without affecting other settings you've already made.


Then click on **Install**, and confirm to start the actual installation.


![0_12](assets/fr/12.webp)


![0_13](assets/fr/13.webp)


### End of installation


At the end of the process, check the **Restart now** box, then click **Done**. The system will reboot and **Manjaro will be ready for use**.


![0_13](assets/fr/14.webp)


## First steps with Manjaro


Installing Manjaro is just the first step. To get the most out of your system, here are a few useful things to know.


### Update the system


Manjaro greatly simplifies updates. To update your packages :


```shell
sudo pacman -Syu
```


This command downloads and installs the latest versions available. We recommend you run it regularly to keep your system **secure and stable**.


### Configuring a development environment


To develop Web applications on Manjaro, install the essential tools in a single command:


```shell
sudo pacman -S nodejs npm git yarn
```


This command installs Node.js and npm to run and manage your JavaScript and TypeScript projects, Git for version management, and Yarn as an alternative package manager.


### Installing a Bitcoin wallet


To manage your bitcoins on Manjaro, you can install **Electrum**, a lightweight and secure wallet :


```shell
sudo pacman -S electrum  # Install Electrum
```


Electrum lets you **receive and send bitcoins** with ease, while offering advanced features such as multiple wallet management and passphrase protection. For a complete guide to using Electrum, check out our dedicated tutorial which explains how to create a wallet, secure your funds and carry out transactions.


https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## Securing your Manjaro system


Security is a crucial aspect of any Linux installation. It's important for you to protect the confidentiality and integrity of your data.


### Firewall configuration


Manjaro includes UFW (*Uncomplicated Firewall*), a program for managing network filter firewalls, but you have to activate it manually:


```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```


![verbose](assets/fr/15.webp)


### Managing user permissions


1. **Create a non-privileged user**


```shell
sudo useradd -m username
sudo passwd username
```


2. **Sudoers file configuration**


```shell
sudo EDITOR=nano visudo
```


Now you're ready to use Manjaro Linux on your machine. Thanks to its **simple installation**, **easy updates**, and **flexibility**, you'll have a powerful, high-performance system, suitable for development, daily use and managing your bitcoins with tools like Electrum.


Manjaro combines **stability, speed and security**, while remaining **entirely free**, making it an ideal choice for beginners and advanced users alike. Take the time to explore its various features and customize your environment to suit your needs. If you'd like more expertise and to discover the Arch Linux system, our tutorial is highly recommended.


https://planb.network/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973