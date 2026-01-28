---
name: Kali
description: Installing Kali Linux on VirtualBox, as a bootable USB stick, or as a dual boot, step by step.
---

![cover-kali](assets/cover.webp)


## Introduction


### Why Kali Linux?


**Kali Linux** is a Linux distribution specialized in IT security.

Here's why we use Kali Linux:



- It is preconfigured with a wide range of pentesting tools (system and network security tests).
- It's **open source and free**, so you can use and modify it freely.
- It's **reliable and secure**, ideal for learning about cybersecurity.
- It allows you to learn how to use Linux in a test-ready environment.
- It can be installed in different ways: **VirtualBox**, **bootable USB key**, or **dual boot**.


## Installation and configuration


### 1. Prerequisites


**Equipment required:**



- 64-bit processor** (Intel or AMD).
- 8 GB RAM minimum** (4 GB may be sufficient for a light installation or VM).
- 50 GB free disk space** to install Kali Linux.
- Internet connection** to download ISO image and updates.
- A minimum 8 GB USB key** to create bootable media (if you want to install Kali on a PC or test it on Live USB).


It is important to back up your data before installing on an existing PC.


### 2. Download



- Go to [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Select the ISO image for your application:
  - Install Image** : for PC installation.
  - Virtual Image**: to install Kali on VirtualBox or VMware.
- Download the ISO image.


![Page de téléchargement Kali](assets/fr/01.webp)


![Sélection de la version Kali](assets/fr/02.webp)


### 3. Create a bootable USB key


You can use several tools, such as Balena Etcher :



- Download and install [Balena Etcher](https://etcher.balena.io/).


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)



- Open Balena Etcher, then select the Kali ISO image.
- Select USB key as destination media.
- Click Flash and wait for the process to finish.


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Installing and securing Kali Linux


#### 4.1 Booting on the USB key



- Switch off the computer.
- Plug in the USB key (containing Kali Linux).
- Switch on your computer. On recent PCs, the system should automatically recognize the USB boot key. If this is not the case, reboot by holding down the BIOS/UEFI access key (usually F2, F12 or Delete, depending on the brand).
  - In the BIOS/UEFI menu, select your USB key as the boot device.
  - Save and restart.


#### 4.2 Launching the installation


##### Startup screen


When booting from the USB stick, the Kali Linux boot screen should appear. Choose between **graphical installation** and **text installation**. In this example, we've opted for graphical installation.


![capture](assets/fr/06.webp)


If you use the **Live** image, you'll see another mode, **Live**, which is also the default startup option.


![Mode Live](assets/fr/07.webp)


##### Language selection


Choose your preferred language for installation and the system.


![Sélection de la langue](assets/fr/08.webp)


Please specify your geographical location.


![Options d'accessibilité](assets/fr/09.webp)


##### Keyboard configuration


Select your keyboard layout. A test field is available to check that the keys correspond to your configuration.


![Configuration du clavier](assets/fr/10.webp)


##### Network connection


The installation will now scan your network interfaces, search for a DHCP service, then prompt you to enter a host name for your system. In the example below, we've entered **"kali "** as the host name.


![Configuration réseau](assets/fr/11.webp)


You can optionally provide a default domain name that this system will use (values can be retrieved from DHCP or if a pre-existing operating system exists).


![Choix du type d'installation](assets/fr/12.webp)


##### User accounts


Next, create the user account for the system (full name, username and a strong password).


![Création d'un utilisateur](assets/fr/13.webp)


![Mode d'installation](assets/fr/14.webp)


![Sélection des applications](assets/fr/15.webp)


##### Time zone


Select your geographical area to set the system time.


![Sélection du fuseau horaire](assets/fr/16.webp)


##### Partitioning type


The installer then scans your disks and displays several options depending on your configuration.


In this guide, we start from a **blank disk**, which gives **four possible choices**.

We're going to select **Guided - use entire disk**, as here we're performing a one-off installation of Kali Linux (single boot). This means that no other operating system will be retained, and the entire disk can be erased.


If your disk already contains data, an additional option **Guided - use largest contiguous free space** may be displayed.


This alternative allows you to install Kali Linux without deleting existing data, making it ideal for dual booting with another system.


In our case, the disk is empty, so this option does not appear.


![Choix du partitionnement](assets/fr/17.webp)


Select the disk to be partitioned.


![capture](assets/fr/18.webp)


Depending on your needs, you can choose to keep all your files in a single partition (default behavior) or have separate partitions for one or more top-level directories.


If you're not sure what you want, choose the **All files in a single partition** option.


![capture](assets/fr/19.webp)


![capture](assets/fr/20.webp)


You will then have one last opportunity to check your disk configuration before the installation program makes any irreversible changes. Once you've clicked on _Continue_, the installation program will launch and installation will be almost complete.


![capture](assets/fr/21.webp)


##### Encrypted LVM


If this option was enabled in the previous step, Kali Linux will now perform a secure hard disk erase before asking you for an LVM password.


Please use a strong password, otherwise a warning about a weak passphrase will be displayed.


##### Proxy information


Kali Linux uses repositories to distribute applications. You'll need to enter the necessary proxy information if your environment uses one.


If you're **not sure** whether to use a proxy, **leave blank**. Entering false information will prevent connection to the repositories.


![capture](assets/fr/22.webp)


##### Metapets


If network access has not been configured, you will need to **further configure** when prompted.


If you are using the **Live** image, the next step will not be displayed.


You can then select the [metapackages](https://www.kali.org/docs/general-use/metapackages/) you wish to install. The default options will install a standard Kali Linux system, so you won't need to modify anything.


![capture](assets/fr/23.webp)


#### Start-up information


Then confirm the installation of the GRUB boot loader.


![capture](assets/fr/24.webp)


##### Restart


Finally, click Continue to restart on your new Kali Linux installation.


![capture](assets/fr/25.webp)


#### 4.3 Updating and configuring Kali Linux after installation


Updating your system is an important step after a new installation. You have two options:


##### Option 1: Via graphical user interface (GUI)


Kali, like Debian/Ubuntu, offers an integrated graphical update manager.


1. Click on the **main menu** (top left or bottom depending on your desktop).

2. Open **"Software Updater "**.

3. The tool will :


    - Check the packages to be updated.
    - You'll see a list (with sizes and versions).
    - Allows you to launch the update with a single click.

4. Enter your administrator password (`sudo`) when prompted.

5. Let it install and restart if necessary.


##### Option 2: Via terminal


Open a terminal and run :


```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```


It is not advisable to use the **root** account for day-to-day work; create a non-root user instead.


In your terminal, type these commands:


```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```


Log out and log back in with the new user.


Let's summarize some basic Kali Linux tasks in a table.


### Basic tasks under Kali Linux



| **Category** | **Basic Task** | **Description / Objective** | **Main Method** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **System Navigation** | Open the terminal | Access Kali's main command line | Click the terminal icon or use `Ctrl + Alt + T` |
| | Browse folders | Move through the system directory tree | `cd /path/to/folder`, `ls` to list files |
| | Create / delete a folder | Organize files | `mkdir folder_name`, `rm -r folder_name` |
| **File Management** | Copy / move a file | Manipulate files in the terminal | `cp file destination`, `mv file destination` |
| | Delete a file | Free up disk space | `rm file_name` |
| | Display content of a text file | Quickly read a file | `cat file.txt`, `less file.txt` |
| **System Management** | Update Kali Linux | Install latest versions and security patches | `sudo apt update && sudo apt full-upgrade -y` |
| | Install software | Add a new tool or utility | `sudo apt install package_name` |
| | Remove software | Clean up the system | `sudo apt remove package_name` |
| | Clean up unnecessary dependencies | Save disk space | `sudo apt autoremove` |
| **Network and Internet** | Verify network connection | Test Internet access | `ping google.com` |
| | Identify IP address | Know your network configuration | `ip a` or `ifconfig` |
| | Change Wi-Fi network | Connect to another access point | Network icon → Select desired Wi-Fi |
| **Accounts and Permissions** | Execute an admin command | Obtain temporary root privileges | `sudo command` |
| | Create a new user | Add a local account | `sudo adduser username` |
| | Change a password | Secure an account | `passwd` |
| **Appearance and Comfort** | Change wallpaper | Personalize the desktop | Right-click on desktop → **Desktop Settings** |
| | Modify theme / icons | Improve readability and aesthetics | Settings → Appearance / Themes |
| **Kali Tools** | Open the tools menu | Explore testing and security tools | **Applications → Kali Linux** menu |
| | Launch a tool (e.g., nmap, wireshark) | Practical discovery of security utilities | `sudo nmap`, `wireshark`, etc. |
| **Help and Documentation** | Get help for a command | Understand a command before using it | `man command` or `command --help` |

## Conclusion


Installing Kali Linux is just the first step in discovering this powerful environment dedicated to cybersecurity. By mastering basic tasks and system management, everyone can begin to explore the built-in tools and understand the inner workings of a Linux system. Kali offers an excellent learning platform, both for reinforcing technical skills and developing a genuine culture of IT security.