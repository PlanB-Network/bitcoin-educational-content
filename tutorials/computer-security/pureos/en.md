---
name: PureOS
description: The Linux distribution that gives you control over your digital life.
---

![cover](assets/cover.webp)


Protecting personal information in the digital age is a top priority for every Internet user. Companies, organizations and even operating systems are useful sources of information for defining your profile and lifestyle. Choosing the right operating system is the first step in strengthening your online privacy. In this tutorial, we'll be taking a look at PureOS, a privacy-focused Linux distribution.


https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Getting started with PureOS


PureOS is a Debian-based operating system developed by Purism. PureOS is suitable for both IT professionals and users looking for a simple, easy-to-use distribution. It's unique in that it's *Free Software*, and focuses on the protection of its users' personal data by setting up a framework based on the privacy, freedom, security and stability offered by Debian.


### Why choose PureOS?



- Simple, intuitive Interface**: GNOME offers a clear Interface desktop, designed to be easy to use, even for people who are not comfortable with the command line.



- Free**: like most Linux distributions, PureOS is entirely free to use. However, a monthly subscription is available to support developers.



- Security and stability**: PureOS' architecture and operating mode make it a highly secure distribution, guaranteeing data protection and system stability.



- Documentation and active community**: PureOS has clear, accessible documentation and a committed, responsive community, making it easy to solve problems and learn the system step by step.


## Installation and configuration


Installing and configuring PureOS on your computer will require the following minimalist features:


- A USB key of at least 8GB to flash the system.
- 4 GB RAM.
- 30 GB of free space on your hard disk.


Go to the [PureOS official website](https://pureos.net/) then download the ISO image of the operating system according to the architecture of your machine.


To launch PureOS installation, you need to create a bootable USB key using flash software such as [Balena Etcher](https://www.balena.io/etcher).


In three easy steps, you'll get a USB stick booted with the PureOS operating system.



- Plug in the USB key and run the downloaded Balena software.
- Then select the PureOS ISO image
- Choose the USB key as output device, then click on the **Flash** button and wait for the process to finish.


![0_01](assets/fr/01.webp)


Once the USB key has been booted, restart the computer on which you wish to install PureOS.


When booting up, access the BIOS by pressing the `ESC`, `F9` or `F11` key, depending on your machine. Select the USB key as the boot device, then press `ENTER` to confirm.


### Startup screen


PureOS offers several options for starting up its operating system. Choose the **Test or Install PureOS** option to launch the operating system installation.


![0_02](assets/fr/02.webp)


Set the language and keyboard layout you want to use on your computer.


![0_03](assets/fr/03.webp)


![0_04](assets/fr/04.webp)


Allow or deny access to your **geographic location** to applications for personalized recommendations based on your area.


![0_05](assets/fr/05.webp)


You can connect to your existing **NextCloud** account to retrieve data linked to the office suite you're using on another system.


![0_06](assets/fr/06.webp)


A tutorial is provided, but you can close the window if you wish to skip this step.


![0_08](assets/fr/08.webp)


### Launching the installation


Click on the **Activities** menu and explore the applications and tools preinstalled on the system. Click on **Install PureOS** to start installation


![0_09](assets/fr/09.webp)


Set the system language and keyboard layout as required, then configure the hard disk partitioning mode.


![0_10](assets/fr/10.webp)


![0_11](assets/fr/11.webp)


![0_12](assets/fr/12.webp)


![0_13](assets/fr/13.webp)


You have two options for partitioning your hard disk:


- Erase disk**: For a complete installation of PureOS, deleting all pre-existing data on your hard disk.


![0_14](assets/fr/14.webp)



- Manual Partitioning** to create your own scores


⚠️ When you manually create partitions for your operating system, make sure you allocate a minimum 2 GB partition for PureOS operation and then another partition for data.


![0_15](assets/fr/15.webp)


Activate **disk encryption** if you want to secure your data. Enter a strong, complex password.


Associate a user with your operating system by defining a user name and an alphanumeric password of at least 20 characters to reinforce the security of your data.


![0_16](assets/fr/16.webp)


Review the settings you've made and modify them if necessary.


![0_17](assets/fr/17.webp)


Click on **Install** then **Install Now** to confirm that PureOS has been installed on your computer.


![0_18](assets/fr/18.webp)


![0_19](assets/fr/19.webp)


When installation is complete, check the **Restart now** box to restart your computer, then confirm:


- The language.
- Keyboard layout.
- Your NextCloud account (optional).


![0_25](assets/fr/25.webp)


## Updates


Before you start using PureOS, it's essential to update your system. This will enable you to benefit from the latest features and security patches, and ensure greater stability.



- Update via Interface graphic**:

Open the **Software** application, then go to the **Updates** tab. Available updates are automatically displayed. Click **Download**, then **Install** once the download is complete.



- Update via terminal**:

Open the terminal, then enter the following command to update the list of available packages:


```shell
sudo apt update
```


Enter your password and confirm. Then install the updates with:


```shell
sudo apt full-upgrade
```


## PureOS for development


By default, PureOS does not include all the tools needed for development.

You can install them quickly with the following command:


```shell
sudo apt install build-essential git curl
```


This will install the **Git** and **Curl** compilation tools, useful in most development environments.


## PureOS environment


PureOS stands out for its innovative approach to true convergence: a single operating system ensures smooth, seamless operation across a variety of devices, including laptops, tablets, mini-PCs and smartphones.


PureOS applications are designed to be adaptive: they automatically adjust to screen size and input mode (touch or keyboard/mouse). For example, the GNOME Web browser dynamically adapts its Interface to provide an optimal experience on both mobile and desktop devices.


PureOS also includes the **LibreOffice** office suite, which includes:



- Writer**: a complete word processor for creating and editing documents.
- Calc**: a powerful spreadsheet program for managing your data and calculations.
- Impress**: a tool for creating professional presentations.


This free suite lets you work efficiently without having to depend on proprietary software.


PureOS offers a unified, secure and flexible environment, based on a 100% open source distribution that guarantees total control and strict respect for privacy. Its true convergence facilitates the creation of applications compatible with different types of device, such as computers, tablets and smartphones, without the need for complex adaptations.


With native access to essential tools, robust package managers and a rich open-source ecosystem, PureOS simplifies application development, testing and deployment in a secure environment. Its stable architecture and commitment to confidentiality make it a reliable platform for a variety of uses, including Blockchain development, rapid prototyping or production environments.


Discover our course on strengthening your security and protecting your digital privacy.


https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1