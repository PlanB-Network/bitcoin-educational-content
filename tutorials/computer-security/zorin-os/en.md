---
name: Zorin OS
description: Complete guide to installing and using Zorin OS as a modern alternative to Windows
---

![cover](assets/cover.webp)


## Introduction


An operating system (OS) is the fundamental software that enables a computer to function: it manages hardware, software, security and the user interface.

Zorin OS is a Linux distribution designed specifically to ease the transition from Windows, while offering the benefits of open source software: security, stability, privacy and performance.


Based on Ubuntu LTS, Zorin OS combines high software compatibility with a familiar, customizable interface, making it a credible and accessible alternative to Windows.


## Why Zorin OS?



- Interface familiar**: Windows-like appearance (start menu, taskbar)
- Easy transition**: designed for users coming from Windows
- Enhanced security**: Linux architecture, less exposed to viruses
- Respect for privacy**: no intrusive data collection
- Optimized performance**: works well on modest machines
- Ubuntu LTS** base: stability, regular updates and broad compatibility
- Advanced personalization**: via the Zorin Appearance tool.


## Installation and configuration


### 1. Prerequisites


**Equipment required:**



- A USB key of at least **8 GB** (12 GB recommended);
- A computer with at least **25 GB of free disk space**
- Internet connection (recommended).


### 2. Download Zorin OS



- Visit the official website: [https://zorin.com/os](https://zorin.com/os)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)



- Choose **Zorin OS Core** (free version recommended)


![Page de téléchargement Balena Etcher](assets/fr/04.webp)



- Download ISO image


Zorin OS also offers :



- Zorin OS Lite** (older computers)
- Zorin OS Pro** (fee-based, with advanced features and support)


## Creating a bootable USB key


You can use several tools, such as Balena Etcher :



- Download and install [Balena Etcher](https://etcher.balena.io/).
- Open Balena Etcher, then select the Zorin ISO image.
- Select USB key as destination media.
- Click Flash and wait for the process to finish.


![Utilisation de Balena Etcher](assets/fr/05.webp)


## Key booting and BIOS access


Switch off the computer on which you wish to install Zorin OS, then plug in the USB key.

When your computer starts up, access the BIOS (`ESC`, `F9` or `F11` depending on the brand) and select the USB key as the boot device, then press `Enter` to start the boot process.



- On startup, select **Try or Install Zorin OS**.


![capture](assets/fr/08.webp)



- If you have an NVIDIA graphics card, select **Try or Install Zorin OS (modern NVIDIA drivers)**.
- Please wait while the files are checked.


![capture](assets/fr/09.webp)



- In the Zorin OS installer, select the language **French** then click on Install **Zorin OS**.


![capture](assets/fr/10.webp)



- Select keyboard layout.


![capture](assets/fr/11.webp)



- Check the boxes **Download updates during Zorin OS installation** and **Install third-party software for graphics and Wi-Fi hardware and additional media formats**.


![capture](assets/fr/12.webp)



- To install Zorin OS on the entire disk: select **Erase disk and install Zorin OS**.


![capture](assets/fr/14.webp)


To install Zorin OS alongside Windows (dual-boot) :



- Select **Install Zorin OS next to Windows Boot Manager**.


![capture](assets/fr/15.webp)



- If you haven't partitioned your disk, select the disk space you wish to allocate to Zorin OS, then click on **Install now**.


![capture](assets/fr/16.webp)



- Confirm the changes on the disc twice.


![capture](assets/fr/16.webp)


![capture](assets/fr/17.webp)



- Select the geographical area **Paris**.


![capture](assets/fr/18.webp)



- Create your user account and give your computer a name.


![capture](assets/fr/19.webp)



- Please wait while Zorin OS installs.


![capture](assets/fr/20.webp)



- Once installation is complete, click on **Restart Now**.


![capture](assets/fr/21.webp)



- Remove the USB installation key and press Enter.


![capture](assets/fr/22.webp)


## Discovering and using Zorin OS


### First start-up


When you start your computer, you'll be taken to GRUB - the Linux boot manager. By default, **Zorin OS** is selected; after 30 seconds, it starts automatically.


![capture](assets/fr/23.webp)


If you have installed Zorin OS as a dual-boot with Windows, you can boot to Windows by selecting **Windows Boot Manager**.


Log in with your user account :


![capture](assets/fr/24.webp)


On first startup, the **Welcome to Zorin OS** application is launched to help you discover your new operating system.


![capture](assets/fr/25.webp)


![capture](assets/fr/26.webp)


![capture](assets/fr/27.webp)


![capture](assets/fr/28.webp)


![capture](assets/fr/29.webp)


![capture](assets/fr/30.webp)


![capture](assets/fr/31.webp)


![capture](assets/fr/32.webp)




### Update the system


The Update Manager will soon open to let you know that updates are available. Install them by clicking on the **Install now** button.


![capture](assets/fr/33.webp)


You can manually check for updates in the **Software** > Updates application:


![capture](assets/fr/34.webp)


### Personalization


The first thing to do in Zorin OS is to choose the **desktop layout** you're most comfortable with. You'll find layouts similar to those found on Windows (and even more so with the Pro version).


To do this, open **Zorin Appareance** > **Type** :


![capture](assets/fr/35.webp)


Then open **Settings** to customize your system:

**Sound - Settings - Zorin OS


![capture](assets/fr/36.webp)


**Online accounts - Settings - Zorin OS


![capture](assets/fr/37.webp)


### Applications


There are several ways to install applications:



- Software**, the Zorin OS application store. Applications come from several sources: apt, Flatpak and Snap.


![capture](assets/fr/38.webp)


![capture](assets/fr/39.webp)



- apt** install (command line) :


```bash
sudo apt install gparted
```


![capture](assets/fr/40.webp)


For more information on installing applications in Zorin OS, see this page: [Install Apps (zorin.com)](https://zorin.com/help/install-apps/).


### Windows applications


To install Windows applications, start by installing the **zorin-windows-app-support** package via Terminal :


```bash
sudo apt install zorin-windows-app-support
```


For a list of compatible Windows applications and their compatibility levels, see the [Wine Application Database] page (https://appdb.winehq.org/). There you'll find the following badges, corresponding to the level of compatibility (from best to worst): Platinum, Gold, Silver, Bronze and Garbage.


To install a Windows .exe or .msi application, you have two options:



- Open **PlayOnLinux** and click on the **Install** button to browse compatible applications and games.


![capture](assets/fr/41.webp)



- Double-click on the application's **.exe or .msi** file and let the installation program guide you.


![capture](assets/fr/42.webp)


![capture](assets/fr/43.webp)


## Conclusion and additional resources


Zorin OS is a solid, affordable alternative to Windows, combining simplicity, security and privacy.


It enables a smooth transition to Linux, without sacrificing comfort or productivity.


To further protect your digital life, we recommend using privacy-friendly services, especially for encrypted communication:


https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2