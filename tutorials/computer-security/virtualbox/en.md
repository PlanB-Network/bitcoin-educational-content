---
name: VirtualBox
description: Install VirtualBox on Windows 11 and create your first VM
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian Burnel published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___



## I. Presentation


In this tutorial, we'll learn how to install VirtualBox on Windows 11 to create virtual machines, whether to run Windows 10, Windows 11, Windows Server or a Linux distribution (Debian, Ubuntu, Kali Linux, etc.).


This introductory tutorial to VirtualBox will help you get started with this open source virtualization solution developed by Oracle, which is completely free of charge. Later, other tutorials will be put online to take you deeper into the subject.


When it comes to virtualizing a workstation, whether for testing purposes as part of a project or during your IT studies, VirtualBox is clearly a good solution. It's also an alternative to other solutions such as Hyper-V, which is integrated into Windows 10 and Windows 11 (as well as Windows Server), and VMware Workstation (chargeable) / VMware Workstation Player (free for personal use).


My configuration: **a Windows 11 workstation where I'm going to install VirtualBox**, but you can install VirtualBox on Windows 10 (or an older version), as well as on Linux. As far as virtual machines are concerned, VirtualBox supports a wide range of systems, including Windows (e.g. Windows 10, Windows 11, Windows Server 2022, etc.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, etc.), BSD (PfSense) and macOS.


## II. Download VirtualBox for Windows 11


To download VirtualBox for installation on a Windows machine, there's only one good address: the [official VirtualBox website](https://www.virtualbox.org/wiki/Downloads) in the "**Downloads**" section. Just click on "Windows hosts" to start downloading this executable, which is just over 100 MB in size.


![Image](assets/fr/025.webp)


## III. Installing VirtualBox on Windows 11


### A. Installing VirtualBox


Installing VirtualBox** is straightforward, and the process is the same for all versions of Windows. Start by launching the VirtualBox executable you've just downloaded, then click on "**Next**".


![Image](assets/fr/026.webp)


This installation is customizable, but I recommend that you install all features: which is the case with the default selection. In the image below, you can see various elements, including:



- VirtualBox USB Support** to enable VirtualBox to support USB devices
- VirtualBox Bridged Network** to integrate network support in "Bridge" mode (the virtual machine can connect directly to your local network)
- VirtualBox Host-Only Network** to integrate network support in "Host-Only" mode (the virtual machine can only communicate with your Windows 11 physical host and other virtual machines in this mode)


Click "**Next**" to continue.


![Image](assets/fr/001.webp)


Click on "**Yes**", bearing in mind that **the network will be interrupted for a moment on your Windows 11 machine**, while VirtualBox carries out network modifications to support different network types, including Bridge mode.


![Image](assets/fr/002.webp)


Once you've confirmed, the installation will start... And a "**Do you want to install this device software?**" notification will appear. Check the "**Always trust software from Oracle Corporation**" option and click "**Install**". VirtualBox actually needs to install several drivers on your computer.


![Image](assets/fr/003.webp)


The installation is now complete! Check the option "**Start Oracle VM VirtualBox 6.1.34 after installation**" and click "**Click**" to launch the software.


![Image](assets/fr/004.webp)


### B. Add the extension pack


Still on the official VirtualBox site (see previous link), you can download an official extension pack, accessible under the "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" section by clicking on the "**All supported platforms**" link. This pack will enable you to add additional functionalities to VirtualBox: it's not mandatory to add it, but it can be useful! For example, it includes support for USB 3.0 in VMs, webcam support and disk encryption.


Open VirtualBox, click on "**File**" and then on "**Settings**" in the menu.


![Image](assets/fr/005.webp)


Click on "**Extensions**" on the left (1), then on the "**+**" button on the right (2) to **load the VirtualBox** extension pack you've just downloaded (3).


![Image](assets/fr/006.webp)


Confirm by clicking on the "**Installation**" button.


![Image](assets/fr/007.webp)


Click "**OK**": the official extension pack is now installed on your VirtualBox instance!


![Image](assets/fr/008.webp)


Let's move on to the creation of our first virtual machine.


## IV. Creating your first VirtualBox VM


To create a new virtual machine on VirtualBox, simply click on the "**New**" button to launch the VM creation wizard. Since this is the first time you've started VirtualBox, I'd like to give you a few more details about Interface and the other buttons.



- Settings**: general VirtualBox configuration (default VM folder, update management, language, NAT networks, extensions, etc.)
- Import**: import a virtual appliance in OVF format
- Export**: export an existing virtual machine in OVF format to create a virtual appliance
- Add**: add an existing virtual machine to your VirtualBox inventory, in standard VirtualBox format (.vbox) or XML format


On the left, the "**Tools**" section gives access to **advanced functions, notably for managing the virtual network, but also for managing VM storage**. Under the "**Tools**" entry, your virtual machines will be added later.


![Image](assets/fr/009.webp)


### A. VM creation process


**As a reminder, VirtualBox supports a multitude of operating systems, including Windows, Linux and BSD. In this example, I'm going to create a virtual machine for Windows 11. Several fields need to be filled in:



- Name**: virtual machine name (this is the name that will be displayed in VirtualBox)
- Machine folder**: where to store the virtual machine, knowing that a subfolder with the VM's name will be created at this location
- Type**: the type of operating system, depending on what OS you want to install
- Version**: the version of the system you wish to install, in this case Windows 11, so "**Windows11_64**"


Click "**Next**" to continue.


![Image](assets/fr/010.webp)


Depending on the operating system you select in the previous step, **VirtualBox makes recommendations on the resources to allocate to the virtual machine**. Here, we're talking about the RAM you wish to allocate to the VM. Let's assume 4 GB, because this is indeed recommended for Windows 11, but if you're short of resources, specify 2 GB instead. **Continue


**Note**: the resources allocated to the virtual machine can be modified later.


![Image](assets/fr/011.webp)


As far as the virtual hard disk is concerned, we're starting from scratch, so we need to choose "**Create virtual hard disk now**" so that the VM has storage space to install the operating system and store data. Click on "**Create**".


![Image](assets/fr/012.webp)


VirtualBox supports three different formats for virtual hard disks, which is a major difference compared with other solutions such as VMware and Hyper-V. There are three formats to choose from:



- VDI**, the official VirtualBox format
- VHD**, which is the official Hyper-V format, although the new VHDX format is used more often these days
- VMDX** is the official VMware format for both VMware Workstation and VMware ESXi


To create a virtual machine that will be used only on this VirtualBox instance, choose "**VDI**". On the other hand, if the virtual hard disk is to be attached to a Hyper-V host at a later date, it may be a good idea to start with the VHD format to avoid having to convert it. Click on "**Next**".


![Image](assets/fr/013.webp)


**The virtual disk can be either dynamic or fixed in size**. When it's dynamic, the file that represents **the virtual disk (here a .vdi file) will grow as data is written to the disk** until it reaches its maximum size, but it won't shrink if data is deleted. Conversely, when it is of fixed size, **the total storage space is allocated immediately (and therefore reserved)**, which allows slightly higher performance, but takes longer when the virtual disk is first created.


Personally, for test virtual machines with VirtualBox, I consider the "**Dynamically allocated**" mode to be sufficient.


![Image](assets/fr/014.webp)


**The next step is to specify the size of the virtual disk**, bearing in mind that by default, the disk will be stored in the VM directory (this can be changed at this stage). I've indicated a size of 64 GB to comply with Windows 11 requirements, but here again, a smaller size could be assigned. Click on "**Create**" to create the VM!


![Image](assets/fr/015.webp)


At this point, the VM is in our inventory, it's configured, but the operating system isn't installed. We need to finalize the VM's configuration before starting it up.


### B. Assigning an ISO image to a VirtualBox VM


To install Windows 11, or any other system, we need installation sources. In most cases, we use a disk image in ISO format to install an operating system. **It is necessary to load the Windows 11 ISO image into our VM's virtual DVD drive


Click on the VM in the VirtualBox inventory (1), then on the "**Configuration**" button (2), which gives access to the general configuration of this virtual machine. This menu is used to manage resources (e.g. increase RAM, configure CPU, etc.). Click on "**Storage**" on the left (3), on the DVD drive where it says "**Empty**" for the moment (4) then click on the DVD-shaped icon (5) and "**Choose a disk file**".


![Image](assets/fr/016.webp)


Select the ISO image of the operating system you want to install, then click OK. This is what I get:


![Image](assets/fr/017.webp)


Stay in the "**Configuration**" section of the VM, I still have a few things to explain.


### C. VM network connection


Go to the "**Network**" section on the left. This section lets you manage the virtual machine's network: number of virtual network interfaces (up to 4 per VM), MAC address, and network access mode (NAT, bridge access, internal network, etc.). **If you want your virtual machine to have access to the Internet, select "NAT" or "Bridge Access "**, but this second mode requires a DHCP server to be active on your network, or you'll have to configure an IP address manually.


Note: I'll come back to the network part in more detail in a dedicated article.


![Image](assets/fr/018.webp)


### D. The number of virtual processors


Like a physical computer, a virtual machine needs RAM, a hard disk and a processor to function. When we created the VM, you may have noticed that the wizard didn't include the processor configuration. However, this can be configured at any time via the "**System**" tab, then "**Processor**", where you can choose the number of virtual processors.


Note: the "**Enable VT-x/AMD-v nested**" option is required for nested virtualization.


In my case, the virtual machine has 2 virtual processors:


![Image](assets/fr/019.webp)


**Don't hesitate to have a look at the other sections of the configuration menu.


### E. First boot and OS installation


To start a virtual machine, simply select it in the inventory and click on the "**Start**" button. A second window will open, providing a visual overview of the VM.


![Image](assets/fr/020.webp)


Ouch, I get a nasty error and my virtual machine won't start! The error is "Login failed for virtual machine..." with the following details:


```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```


In fact, this is normal because **the virtualization feature is not enabled on my computer**! To correct this problem, you need to reboot your computer to access the BIOS and enable virtualization.


![Image](assets/fr/021.webp)


Without waiting, I reboot my computer and **press the "SUPPR" key to access the BIOS** (the key may vary depending on the machine, and could be F2, for example) of my ASUS motherboard. To activate virtualization, "SVM Mode" must be enabled in my case. Here again, from one motherboard to another, from one manufacturer to another, the name can change. Look for a function referring to **AMD-V** (for an AMD CPU) or **Intel VT-x** (for an Intel CPU).


![Image](assets/fr/022.webp)


Once this is done, save the modification and restart the physical machine... This time, **VirtualBox can start the virtual machine** and load the Windows ISO image to install the operating system! 🙂


![Image](assets/fr/023.webp)


On our Windows 11 physical host, where VirtualBox is installed, we can see that the Windows 11 virtual machine folder contains various files.



- The VBOX** file (in XML format) corresponding to the VM configuration (RAM, CPU, etc.)
- The VBOX-PREV** file is a backup of the previous configuration
- The VDI** file corresponds to the virtual hard disk in dynamic mode, so it is currently only 13 GB, whereas its maximum size is 64 GB
- The NVRAM** file contains the BIOS state of the virtual machine, which is equivalent to the non-volatile memory of a physical machine


![Image](assets/fr/024.webp)


## V. Conclusion


**VirtualBox is now up and running on our Windows 11 physical machine! All that's left is to take advantage of it and create virtual machines!** I'll come back to installing Windows 11 in a VirtualBox VM in another article. For Windows 10, Windows Server or a Linux distribution (Ubuntu, Debian, etc.), just let us guide you!