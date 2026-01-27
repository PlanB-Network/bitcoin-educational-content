---
name: Pop!_OS
description: Guide to installing Pop!_OS, a Linux distribution
---

![cover](assets/cover.webp)


## Introduction


Pop!OS is a Linux-based operating system developed by **System76**, an American manufacturer specializing in machines for developers, designers and advanced users.


Designed to offer a modern, stable, high-performance environment, Pop!OS is distinguished by a simple experience, powerful tools and a strong focus on productivity.


### Who is System76?


System76 is an American company founded in 2005 and based in Denver, specializing in the manufacture of notebooks, desktops and servers designed specifically for Linux.


Unlike traditional manufacturers, System76 develops machines designed to be open, repairable and oriented towards software freedom.


System76 doesn't just make computers.


The company also develops :


- Pop!OS**, its own Linux-based operating system;
- COSMIC**, the modern, high-performance desktop environment used by Pop!OS ;
- Open Firmware**, an open-source firmware based on Coreboot ;
- tools for developers and designers.


The aim is to offer high-quality hardware and software integration, comparable to the Apple ecosystem, but totally open and centered on Linux.


## A modern, stable and accessible system


Pop!OS builds on the foundations of Ubuntu, giving it excellent stability, broad hardware compatibility and access to a huge software ecosystem.

It provides an elegant interface, the COSMIC desktop, designed to be fluid, intuitive and customizable, even for new users.


## An ideal choice for developers, designers and demanding users


Pop!OS is particularly appreciated by :



- developers (pre-installed tools, advanced tiling management),
- users with Nvidia or AMD graphics cards,
- students and professionals looking for a reliable system,
- windows users wishing to make a simple transition.


It includes automatic tiling, a clear software center and integrated productivity tools to make daily use easier.


## Pop!OS highlights



- Optimized performance** thanks to regular updates.
- Two ISO versions available**: standard and Nvidia-optimized.
- Enhanced security** (LUKS encryption available on installation).
- Interface COSMIC** ergonomic and modern.
- Highly compatible** with Ubuntu and Flatpak software.


## Download POP!OS securely


### 1. Prerequisites


Before downloading and installing POP!OS, there are a few things you need to do to prepare the installation environment correctly.


### Equipment required



- A compatible computer**: Intel or AMD processor, Intel / AMD / Nvidia GPU.
- At least 4 GB RAM** (8 GB recommended for comfortable use).
- 20 GB free space minimum** (40 GB or more recommended).
- A minimum 4 GB USB key** to create the installation media.


### Internet connection


A stable connection is useful for :



- download the ISO image,
- install updates after installation.


Pop!OS can run without a connection, but installation is much smoother over the Internet.


### Data backup


If Pop!OS is to replace or coexist with another system (Windows, Ubuntu, etc.), it is advisable to back up important files before proceeding.


### Check for the presence of a Nvidia GPU (if applicable)


For computers equipped with a Nvidia graphics card, you'll need to download the special ISO image that includes the Nvidia drivers.

This check is very simple:



- by consulting the PC specifications,
- or by looking up the graphics card model in the system settings.


### Download from the official website


The Pop!OS ISO image should be downloaded directly from the official System76 page: [system76.com/pop](https://system76.com/pop/).


This page always offers the most recent version, adapted to your hardware.


![capture](assets/fr/03.webp)


### Choose version: Standard or Nvidia, or Raspberry Pi (ARM64)


Pop!OS is available in three variants:


### Standard version


Recommended for computers using :



- intel or AMD processor;
- an integrated Intel or AMD GPU;
- an AMD Radeon graphics card.


![Utilisation de Balena Etcher](assets/fr/04.webp)


### Nvidia version


Recommended for computers equipped with Nvidia graphics cards.

This image already includes Nvidia drivers, making installation easier and reducing graphics problems.


![Utilisation de Balena Etcher](assets/fr/05.webp)


### Raspberry Pi version (ARM64)


For Raspberry Pi 4 and 400 (ARM processor).

Adapted to ARM architecture, this is a specific version for these mini-computers.


![Utilisation de Balena Etcher](assets/fr/06.webp)


## Create a bootable USB key


You can use several tools, such as Balena Etcher :



- Download and install [Balena Etcher](https://etcher.balena.io/).


![Page de téléchargement Balena Etcher](assets/fr/07.webp)


![Installation de Balena Etcher](assets/fr/08.webp)



- Open Balena Etcher, then select the Pop!OS ISO image.
- Select USB key as destination media.
- Click Flash and wait for the process to finish.


![Utilisation de Balena Etcher](assets/fr/09.webp)


## Installing and securing Pop!OS


### Booting from USB key



- Switch off the computer.
- Plug in the USB key (containing Pop!OS).
- Switch on your computer. On recent PCs, the system should automatically recognize the USB boot key. If this is not the case, reboot by holding down the BIOS/UEFI access key (usually F2, F12 or Delete, depending on the brand).
  - In the BIOS/UEFI menu, select your USB key as the boot device.
  - Save and restart.


### Launching the installation


Once you've selected your bootable USB key as the start-up device, your computer will boot into a Pop!OS Live environment.


Select your language.


![Capture](assets/fr/10.webp)


Select a location.


![Capture](assets/fr/11.webp)


Select a language for keyboard input.


![Capture](assets/fr/12.webp)


Select a keyboard layout.


![Capture](assets/fr/13.webp)


Choose the `Clean Install` option for a standard installation. This is the best option for new Linux users, but be aware that it will delete all the contents of the target drive. Alternatively, you can select `Try Demo Mode` to continue testing Pop!OS in the live environment.


![Capture](assets/fr/14.webp)


Select `Custom (Advanced)` to access GParted. This tool lets you configure advanced features such as dual booting, creating a separate `/home` partition, or placing the `/tmp` partition on a different drive.


Click `Erase and Install` to install Pop!OS on the selected drive.


![Capture](assets/fr/15.webp)


### User account configuration


The next section of the installation program will guide you through the creation of a user account so that you can log on to your new operating system.


Provide a full name (this can include any text of your choice, upper or lower case), as well as a user name (which must be in lower case) :


![Capture](assets/fr/16.webp)


Once the account has been created, you will be prompted to set a new password.


![Capture](assets/fr/17.webp)


### Full disk encryption


System disk encryption is not necessary, but it does guarantee the security of user data in the event that someone gains unauthorized physical access to the device.


The drive can be encrypted using your login password by checking `Encryption password is the same as user account password`. You can also uncheck this box and select `Set Password` at the bottom. Select `Don't Encrypt` to ignore the disk encryption process.


![Capture](assets/fr/18.webp)


If you've chosen the `Set Password` button, you'll see an additional prompt to set your encryption password.


Proceed to the next step in the installation program. Pop!OS will now begin installation on the disk.


![Capture](assets/fr/19.webp)


Once installation is complete, restart your computer and log in to complete the user account configuration process.


If you've changed the boot order to give priority to your Live USB key at startup, switch off the computer completely and remove the installation USB key. If you're in dual-boot mode, press the appropriate keys to access the configuration and select the drive containing the Pop!OS installation.


![Capture](assets/fr/20.webp)


### NVIDIA Graphics


If you have installed from Intel/AMD ISO and your system has a discrete NVIDIA graphics card, or if you have added one at a later date, you will need to manually install the drivers for your card to achieve optimum performance. Run the following command in a command terminal to install the driver:


```bash
sudo apt install system76-driver-nvidia
```


You can also install NVIDIA graphics drivers from the Pop!_Shop.


![Capture](assets/fr/20.webp)


## Installing essential tools


Pop!OS offers a wide range of software via its Pop!Shop, but many essential tools can also be installed via the terminal with `apt` or `flatpak`. Here's how to install the key tools for a complete working environment.


### Terminal installation


| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Installation via Pop! Shop (graphical interface)



- Open **Pop!_Shop** from the main menu.
- Use the search bar to find the applications you want (for example, "Brave").
- Click **Install** for each application.
- Pop!_Shop automatically manages dependencies and updates.


## System update


### Option 1: Via graphical user interface (GUI)


Pop!OS features a simple, intuitive graphical update manager.


1. Click on the **main menu** (icon bottom left).

2. Open **"Pop!_Shop "**.

3. In the Pop!_Shop, click on the **"Updates "** tab.

4. The system will automatically check for available updates.

5. Click on **"Update all "** to start installing updates.

6. Enter your password if requested.

7. Let the process finish, then restart if necessary.


### Option 2: Via terminal


Open a terminal and type :


```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```


### User management


We recommend using a standard user account with sudo rights for day-to-day operations.


To create a new user :


```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```


Log out, then log back in with this new user.


### Graphics driver management



- For Nvidia cards, check that the proprietary drivers are installed:


```bash
sudo apt install system76-driver-nvidia
```



- For AMD/Intel, drivers are generally included by default.


### Activate firewall (UFW)


Pop!OS does not block network traffic by default. Activate UFW to enhance security:


```bash
sudo ufw enable && sudo ufw status verbose
```


### Configure automatic updates


To keep the system up to date without manual intervention:


```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```


### Customize appearance and behavior



- Open **System settings** → **Appearance** to choose a light or dark theme.
- Configure active corners, animations and extensions via the COSMIC manager.
- Adjust the desktop layout to optimize your workflow.


### Configure automatic backup


Pop!OS integrates tools such as Deja Dup for backup:



- Launch **Backup** from the menu.
- Choose an external drive or a network location.
- Schedule regular backups.


### Installing useful GNOME/COSMIC extensions


Here are a few recommended extensions to enhance the user experience:



- Dash to Dock**: application bar always visible.
- GSConnect**: synchronization with Android.
- Clipboard Indicator**: advanced clipboard management.


Install them via :


```bash
sudo apt install gnome-shell-extensions
```


Then activate them in the settings.


### Optimizing memory and swap management


Check your swap status:


```bash
swapon --show
```


If necessary, increase the swap size or configure a swap file :


```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```


Add it to the `/etc/fstab` file for automatic mounting.


## Package and repository management


### Understanding package sources


Pop!OS, based on Ubuntu, uses mainly :



- Official Ubuntu** repositories: for most stable software.
- System76** repositories: for drivers, firmware and specific tools.
- Flatpak**: access a wide range of sandboxed applications.
- Snap** (optional): another universal package format.


---

### Add and manage PPA repositories


To install frequently updated software, certain PPAs (Personal Package Archives) can be added:


```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```


## Conclusion


Pop!OS is a modern, stable Linux distribution suitable for beginners and advanced users alike.


Thanks to its intuitive COSMIC interface and integrated tools, it offers a fluid and productive experience, whether for development, creation or everyday use.


This tutorial covers the key stages: preparation, downloading, installation, initial settings and essential tools.


Feel free to explore Pop!OS further and customize your environment to get the most out of it.