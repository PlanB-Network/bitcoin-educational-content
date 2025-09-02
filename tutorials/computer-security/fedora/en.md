---
name: Fedora
description: The Linux distribution that provides you with a free, complete and secure workspace.
---


![cover](assets/cover.webp)




Fedora is a free, open-source Linux-based operating system launched in 2003, developed by the **Fedora Project** community and supported by **Red Hat Linux**. It is renowned for its stability, good performance and ease of use, making it an excellent choice for beginners and advanced users alike. The system runs on most modern processor architectures, making it easy to install on virtually any computer. Fedora is also available in several pre-configured editions, called "Fedora Spins" or "Fedora Editions", designed for specific needs (video games, astronomy, development...).


## Fedora Linux architecture


As you read earlier, Fedora is a free operating system based on the Linux kernel. The Linux kernel is the part of the operating system that communicates with the computer hardware and manages system resources such as memory and processing power.


Fedora Linux includes a variety of software tools and applications that are required to run the operating system on top of the Linux kernel. Fedora's modular architecture means that it consists mainly of a collection of individual components that can be easily added, removed or replaced as required. This allows you to shape the operating system using only the resources you need.


Fedora also includes a desktop environment, which is the Interface through which users perform tasks and access applications. Fedora's default desktop environment is GNOME, a user-friendly, easy-to-use and highly customizable desktop environment.


## Why choose Fedora?


Among the multitude of Linux distributions available, Fedora stands out in particular for:



- Modularity**: Compatible with different processor architectures, Fedora can be installed on the majority of computers, even low-powered ones, adapting perfectly to your needs.



- A simple, intuitive Interface**: Fedora combines a modern graphical Interface with a powerful command-line Interface, making it easy to use for all profiles.



- Kernel stability**: Based on Red Hat, Fedora is renowned for the reliability of its updates, especially kernel updates, which are carried out without major bugs thanks to free contributions from a large community.



- Fast, easy installation**: with an image size of just 3 GB, installation is quick and easy, even on machines with limited resources.


## Fedora editions


Depending on your profile and usage, Fedora offers editions to suit your needs. You'll mainly find:



- Fedora Workstation**: Ideal for personal and/or professional use on your computers, this edition is installed with generic utilities such as browsers, an office suite (text editors), and media playback software.



- Fedora Server**: This edition is dedicated to server management. Fedora Server includes a variety of tools to help you deploy and manage servers on your own scale.



- Fedora CoreOS**: Want to easily run and deploy cloud applications? Fedora CoreOS is the edition that gives you the tools to create and manage images with Docker and Kubernets, for example.


In this tutorial, we'll be taking charge of the Fedora Workstation edition. However, the processes detailed below are similar for the other editions.


## Installing and configuring Fedora Workstation


Installing Fedora Workstation requires the following hardware configuration:


- A USB key of at least **8 GB** to boot the operating system.
- At least **40 GB free space** on your computer's hard disk.
- 4 GB RAM** for a smooth experience.


### Download Fedora Workstation


You can download the [Fedora Workstation] edition (https://fedoraproject.org/fr/workstation/download) from the official Fedora project website. Then select the version corresponding to your processor architecture (32-bit - 64-bit) and click on the **Download** icon.


![download](assets/fr/01.webp)


![telecharger](assets/fr/02.webp)

### Create a bootable USB key


To install Fedora, you need to create a bootable USB key using software such as [Balena Etcher](https://etcher.balena.io/).


![flashOs](assets/fr/03.webp)


![flash](assets/fr/04.webp)


Once you've finished installing Balena Etcher, open the application and select the downloaded Fedora Workspace ISO image. Select your USB key as destination media and click on the **Flash** button to start creating the bootable key.


![boot](assets/fr/05.webp)

### Installing Fedora


When you have finished booting your USB key, switch off your computer.

Switch on your computer, then access the BIOS during startup by pressing the `F2`, `F12` or `ESC` key, depending on your computer.


In the boot options, select your USB key as the primary boot device. By confirming this choice, your computer will restart and automatically launch the Fedora installer** present on the USB key.


Once your computer has booted from the USB stick, the **GRUB screen** appears.


At this stage, you have the following options:


- Test media**: This option allows you to check the integrity of the USB stick and ensure that all the dependencies required for a correct installation are present. This is an optional step, but recommended if you have any doubts about the USB stick.


![install](assets/fr/06.webp)


![testing](assets/fr/07.webp)



- Start Fedora**: This launches Fedora in "live" mode, without installation.


On the Fedora desktop (live mode), click on **Install Fedora** (or Install on hard disk) to start the installation process. You can choose to install later and test Fedora without having to install it.


![install-live](assets/fr/08.webp)


The first step is to select Fedora's **installation language** and **keyboard layout**


![language](assets/fr/10.webp)



- Selecting the installation disk:


Choose the hard disk on which you want to install Fedora.


If the disk is empty, Fedora will automatically use all available space. Otherwise, you can customize the partitioning (manual or automatic).


![disk](assets/fr/11.webp)



- Encryption:


At this stage, Fedora suggests encrypting your disk to add an extra layer of security. This ensures that your data can only be read by your Fedora system.


![chiffrement](assets/fr/12.webp)


Before launching the installation, Fedora displays a summary of your choices. Confirm and click on the install button to start Fedora installation.


![resume](assets/fr/13.webp)


During installation, Fedora copies files and configures the system. When finished, the computer reboots automatically.


![installation](assets/fr/14.webp)


### Basic configuration

On first use, you will need to finalize a few settings:


- Change the system language if necessary.


![language](assets/fr/15.webp)



- Select a keyboard layout to suit your preferences.


![keyboard](assets/fr/16.webp)



- Choose your time zone by typing the name of your city in the search bar, then click on the corresponding suggestion.


![timezone](assets/fr/17.webp)



 - Enable or disable access to your position for applications that need it, as well as automatic sending of bug reports.


![location](assets/fr/18.webp)



- Decide whether you want to enable third-party software repositories.


![logs](assets/fr/19.webp)



- Enter your full name and define a username for your account.


![name](assets/fr/20.webp)



- Create a secure password for your session: as long as possible (minimum 20 characters), as random as possible and with a variety of characters (lowercase, uppercase, numbers and symbols). Remember to save your password.


![mdp](assets/fr/21.webp)


Once all these steps have been completed, launch Fedora and start using it immediately, without any further reboot.


![welcome](assets/fr/22.webp)


![start](assets/fr/23.webp)


Once your installation is complete, you can consult your Interface home with a few pre-installed utilities.


![install-now](assets/fr/09.webp)


## Discover the basic tasks


### Browsing the Internet

Fedora's default browser is **Firefox**. It's easy to use and suitable for most needs.

If you prefer another browser, you can install it from the **software manager** or via the **terminal**.

### Word processing

Fedora includes the **LibreOffice** office suite by default, which offers several useful tools:


- Writer** for word processing.
- Calc** for spreadsheets.
- Impress** to create presentations.

## Installing applications

To install new applications, you can use Fedora's **software manager** (called _Software_), which makes installation easy and visual.  However, using the **terminal** is often faster and more accurate.


Before installing any software, always remember to update the **repositories** to make sure you have access to the latest versions available.


Then use the following command to launch the installation of the desired application:

sudo dnf install software_name`

## Updating your operating system

After installation, it's important to update Fedora to take advantage of the latest security patches and software updates.

### Option 1: Via Interface graphic


- Open Fedora **Settings**, then go to the **System** section.
- Click on **Software update**.
- Start downloading updates and wait until the process is complete.


A **restart** may be required once updates have been installed.

### Option 2: Via terminal


- Open a terminal and start by updating the **repositories** to make sure you have the latest versions of:


```shell
sudo dnf check-update
```



- Next, update all installed software with the following command:


```shell
sudo dnf upgrade
```


Now your Fedora system is up to date and ready to use for all your everyday tasks. Discover our tutorial on Linux Mint, another Linux distribution, and how to set up a healthy and secure environment for your Bitcoin transactions.


https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5