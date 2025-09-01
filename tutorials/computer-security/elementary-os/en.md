---
name: Elementary OS
description: The ideal replacement for Windows and MacOS
---

![cover](assets/cover.webp)


Elementary OS is an Ubuntu-based operating system, designed to be simple, fast and stable for many everyday uses. It represents a balanced Linux alternative to MacOS and Windows. Its fluid, intuitive and uncluttered graphical Interface makes it easy to learn, even for beginners. It also focuses on ergonomics, security and performance.


https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Why choose Elementary OS



- Simplicity and ease of use**: Elementary OS's graphical Interface is midway between those of MacOs and Windows. This familiarity makes it easy to adopt, even for inexperienced users.



- Security**: Like most Linux distributions, Elementary OS benefits from a high level of security. Regular updates, rights management and the absence of common viruses make it a reliable system.



- Speed**: Elementary OS is a lightweight distribution. It requires few resources, making it fast and suitable for computers with modest configurations.



- Free**: The system is completely free. However, when you download it, you can make a donation to support the developers.



- Active community**: The community around Elementary OS is diverse and responsive. If you run into difficulties, you can easily find help on the forums or social networks.


## Installation and configuration

### Hardware prerequisites


Before starting installation, please ensure that you have the following equipment:



- A **USB key** of at least 12 GB
- RAM** memory of at least 4 GB
- A **hard disk of 20 GB** or more for comfortable use


## Download ISO image


Go to the official operating system website [elementary](https://elementary.io/) and choose an amount to support the project. This step is optional.

If you wish to download the ISO image free of charge, enter 0 in the **"Other "** field and start downloading the system ISO image.


![0_01](assets/fr/01.webp)


## Creating a bootable USB key


Once you've downloaded the ISO image, you'll need to make it bootable on a USB key to proceed with the installation.


Download software such as [Balena Etcher](https://etcher.balena.io/) or a similar tool, then launch the software.

Select the previously downloaded **Elementary OS** ISO image and set your USB key as the target.


Click on the **flash** button to start the process, and wait until the process is complete before removing the USB key.


![0_02](assets/fr/02.webp)


## Key booting and BIOS access


Switch off the computer on which you wish to install Elementary OS, then plug in the USB key.

When your computer starts up, access the BIOS (`ESC`, `F9` or `F11` depending on the brand) and select the USB key as the boot device, then press `Enter` to start the boot process.


## Installing Elementary OS


Installation starts automatically if the USB key is correctly configured.


### Language selection


Select the language in which you wish to install the system. You can also choose a regional variant.


![0_03](assets/fr/03.webp)


![0_04](assets/fr/04.webp)


### Keyboard layout


Select the layout corresponding to your keyboard. A field is provided to check that the keys produce the correct characters.


![0_05](assets/fr/05.webp)


![0_06](assets/fr/06.webp)


### Test mode


Elementary OS lets you test the system before installing it. This mode lets you explore Interface without modifying anything on your hard disk.


### Launching the installation



- Click on **"Erase disk and install "** to install directly on the entire disk.
- Click on **"Custom install "** if you wish to manage partitions manually.


![0_07](assets/fr/07.webp)


### Disc selection


Select the disk on which Elementary OS is to be installed, then click on the Continue button.


![0_08](assets/fr/08.webp)


### Disk encryption


An option allows you to encrypt the disk to **secure your data**. You'll need to set a strong password to activate this protection. However, it is optional.


![0_09](assets/fr/09.webp)


![0_10](assets/fr/10.webp)


### Launching the installation


Before launching the installation, you can authorize the automatic installation of additional hardware drivers, depending on your machine's compatibility.



- Click on "Erase and install" to begin installation.
- Wait until the process is complete.


![0_11](assets/fr/11.webp)


![0_12](assets/fr/12.webp)


### Restart


Once finished, click on the **enter** button to restart, then remove the USB key at the appropriate moment to avoid restarting the installation.


![0_13](assets/fr/13.webp)


## Configuration after installation


After reboot, a few additional steps are required.


![0_14](assets/fr/14.webp)


### Language selection


Confirm or change the system language at login.


![0_15](assets/fr/15.webp)


### Keyboard layout


Make sure the keyboard layout is the one you want.


![0_16](assets/fr/05.webp)


### Creating a user account


Associate a user account with your operating system by defining a username and then securing access to your data with an alphanumeric password of at least 20 characters and symbols.


![0_17](assets/fr/17.webp)


### First connection


When you log on for the first time, Elementary OS lets you personalize your environment with a few basic settings.


![0_18](assets/fr/18.webp)


![0_19](assets/fr/19.webp)


## System update


Before prolonged use, it is important to update the system with the latest patches.

### Option 1: Update via Interface graphics


Enter the **AppCenter** and click on the update icon in the top right-hand corner. Wait for the updates to be listed, then click on **"Update All "** to start installation.


![0_20](assets/fr/20.webp)


![0_21](assets/fr/21.webp)


### Option 2: Update via terminal


You can also perform the update from the command line via your terminal: a recommended option for its accuracy.


```shell
sudo apt update
```


```shell
sudo apt full-upgrade
```


For your first updates, the operating system requires your user password and confirmation to update software packages, even in the Elementary kernel.


## Work environment configuration


Elementary OS includes only the essential tools. To adapt your environment to your needs, especially if you're a developer, we recommend installing additional tools.



- You can add useful dependencies with the following command (to be adapted to your needs):


```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```


This command installs **Git**, **Python 3**, **pip**, **compiler tools**, **wget**, **curl**, **zsh**, **make**, **snapd** and **vscode** to prepare a basic development environment.


Elementary OS is now up and running on your machine. Its philosophy of simplicity, lightness and elegance makes it an excellent choice for both personal and professional use. You get a stable, fluid and uncluttered system, ready to be customized according to your preferences. Whether for development, office use or day-to-day browsing, everything is in place to build an efficient, intuitive and pleasant working environment. Also check out our tutorial on Fedora, an equally simple, robust and modular Linux distribution.


https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0