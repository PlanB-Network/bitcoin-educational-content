---
name: Raspberry Pi Zero
description: How to build a minimal, air-gapped, low-cost computer using a Raspberry Pi Zero and an accessory kit.
---
![cover](assets/cover.webp)


If you've been on the pages of Plan ₿ Network for a while, you've already learned that one of the most advocated security settings, almost a must, **is the management of funds by offline storage of your private keys**.


If you haven't discovered it yet, throughout this tutorial you will find links to open source resources with which to learn more about it.


To manage private keys offline, therefore, one needs a device permanently disconnected from the network, whether it is a [hardware wallet](https://planb.network/resources/glossary/hardware-wallet) or an air-gapped computer, dedicated to this specific function.


How do you do it if, for example, you do not have the ability to purchase hardware that performs only this task, but you do not want to give up this security step?


## The Solution

What if I told you that you could make an offline device in the form of an airgap computer that is the size and weight of a USB flash drive and costs 35 euros? Would you not believe it?


Continue reading.


I'll tell you more: read all the way through. The proposed solution is cheap, but it is not exactly the easiest. First you get the general idea, then you decide to invest some of your time in some personal research and choose, with as much peace of mind as possible, whether and how to proceed.


## Requirements

**1** A [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): the PI Zero (without any suffix) is the basis for building a computer with minimal performance, but it is above all devoid of Wi-Fi and Bluetooth cards, requirements essential for the purpose of this exercise.



- Cost**: about 15.00 at the time of writing this tutorial (August 2025).
- Continuity of production**: Raspberry guarantees production until January 2030.


PI Zero without Wi-Fi and Bluetooth, have unfortunately become virtually unavailable. You may be able to find the PI Zero W and PI Zero 2W alternatives more easily. In this case, you can disable the connection functions by changing the config file. After installing the operating system, you will need to add these items to the config:


```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```


a section of this guide will show you how and where to do it. However, if you really want to be sure, you can find several tutorials on the web for removing the Wi-Fi chip with a small cutter, the kind suitable for working on electronic boards.


**2** A _starter kit_ for Raspberry PI Zero: as is the practice for the Raspberry world, bare bones, with no external case. In addition, the limited resources of such a small board condition the possibilities of connection with the outside world.


When I decided to proceed, I found [this kit](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) full of accessories, to take full advantage of the full potential of the PI Zero. In fact, the kit contains a USB A -> micro USB power supply, a small USB hub, a mini-HDMI -> HDMI adapter, a copper heatsink, and an aluminum outer case. Also provided with the kit are the screws and allen wrench needed to put the PI Zero in the new case.



- Cost**: 19.99 euros.


**3** This tutorial does not require you to spend large budgets on the airgap computer. You should know, however, that you will need a USB keyboard and mouse (strictly wired, avoid Bluetooth) and a monitor. Depending on the input to your monitor, you may need an adapter from mini-HDMI, the only output available on the PI Zero. Finally, look hard for the fact that we all have a non-wireless keyboard and mouse in the house somewhere-it's time to dust them off.


## Extra Budget


**4** You can get the original power supply from Raspberry, costing about 15.00 euros.


**5** I personally opted to use the power supply provided in the _starter kit_, combining it, however, with a USBA → miniUSB so-called `no data` cable, costing 3.70 euros.


**6** A micro SD card, to have a minimum of at least 32 GB mass storage; if industrial quality/level is better.


**7** You will need a system, a USB to micro SD adapter, like the one you see in the picture. Your PI Zero's operating system and its memory will, in fact, work on that media.


![img](assets/it/06.webp)


## Installation of the Operating System

Before closing your PI Zero in the case, I recommend that you install the operating system. You will then be able to check the LED that indicates operation, right off the bat.


To choose and burn the operating system, I opted for the easiest way: using Raspberry`s `PI Imager` tool.


![img](assets/it/01.webp)


Go to the [Raspberry Github](https://github.com/raspberrypi/rpi-imager/releases) to download the latest release of the Imager, choosing the one most suitable for your operating system (v. 1.9.6 at the time of writing). You will notice that next to each asset there is also the hash of the corresponding file. This will be useful for verification.


![img](assets/it/02.webp)


I recommend that you verify the operating system you will be using on your airgap computer, for your own personal peace of mind. This will give you confidence that you are operating with a legitimate (not malicious) version of the Imager and, consequently, Raspi OS.


Do the verification immediately upon download, with your machine you normally use connected to the Internet


Then open the Linux terminal and prepare the download, creating a `raspios` directory useful for working with it.


![img](assets/it/19.webp)


Download the Imager for your Linux distribution with `wget`.


![img](assets/it/20.webp)


Finally, run the file `sha256sum` command and compare the Hash with the one provided by Raspberry in its Github.


![img](assets/it/21.webp)


Or, if you have Windows, open the Power Shell and type the following command:


```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```


![img](assets/it/04.webp)


You will get the Hash which must match the one published on the Raspberry Github.


Once you have verified the download, you can install Imager on your daily computer and open it. Imager is the tool you need to burn the operating system to the micro SD, which will be the "system disk" of PI Zero.


The process is extremely simple: first choose the Raspberry device you are going to use (so pay attention to **your model** of Raspi Zero), then the OS version, and finally the mount point of the micro SD card to flash the OS to.


### First Step


![img](assets/it/03.webp)


### Second Step


![img](assets/it/07.webp)


**Note well**: choose `PI OS 32-bit`, the only one that works with PI Zero.


### Third Step


![img](assets/it/08.webp)


(Be very careful to leave _Exclude System Drive_ selected to avoid being prompted to install Raspi's operating system on your computer.)


When everything is set up, the Imager will ask you if you would like to use custom settings. Choose what you want, or click _No_ to continue with the default options.


![img](assets/it/09.webp)


Confirm that you want to delete the contents of the micro SD


![img](assets/it/10.webp)


The Imager starts flashing the operating system to the micro SD, a scroll bar will notify you of the progress.


![img](assets/it/11.webp)


At the end there is automatic verification, I advise you not to stop it.


![img](assets/it/12.webp)


Finally a message appears on the screen, and if everything was successful, it looks like what you read in the picture.


![img](assets/it/13.webp)


You can now really remove the micro SD from the reader and place it into the PI Zero slot. Power on the small Raspberry and observe the LED: we expect it to be green and to blink, indicating the normal loading of the operating system, and then remain steadily on. If you see other indications, for example if the LED blinks at a regular frequency or is red, consult the FAQ or [the support forum pages](https://forums.raspberrypi.com/).


## First Configuration

The first startup of Raspi OS is a little slower than usual because it has to perform a number of actual installation tasks. But if all has gone well, you will find a welcome screen.


![img](assets/it/14.webp)


Click on _Next_ to set the geographical region, especially for loading the correct keyboard. Pay special attention to the latter.


![img](assets/it/15.webp)


Click on _Next_ and you will be asked to create your user, jot down your credentials and keep them well.


![img](assets/it/16.webp)


The wizard asks you to choose a default web browser, between Chromium and Firefox; it may also ask you about Wi-Fi network settings if you are working with a Zero W or 2W PI. Go ahead and click _Skip_.


At some point you will be prompted to upgrade the on-board software and operating system. Choose _Skip_: for the purposes of this exercise we are in fact building an offline machine, which must remain offline as of this time.


Finally, it may ask you to enable `ssh`, but decline this step as well, since it is a Zero airgap IP.


![img](assets/it/17.webp)


There is not much more to configure. When finished, reboot the Raspberry for the changes to take effect.


![img](assets/it/18.webp)


## A New Computer Airgap

After rebooting, your new airgap computer is ready. PI Zero shows you the new desktop, which you can work with either via GUI or from the command line.


![img](assets/it/22.webp)


### First Steps for PI Zero W or 2W

If you are working with a Raspberry PI Zero W or 2W series, your board has chips for Wi-Fi and Bluetooth on board. During the first setup you skipped the connection configuration, so the PI Zero is not connected to the Internet. Now you can disable the two chips permanently via software.


In fact, Raspi OS provides a `config.txt` file that you can edit to your liking. The `config` is located in the `boot` partition, in the `firmware` directory, and you can edit and save it with `root` privileges.


Open the terminal from the icon on the top left and it becomes `root`.(1)


![img](assets/it/23.webp)


(1) If Raspi OS did not have you create the `root` password during the previous steps, I recommend that you do so now, with the `passwd` command. Having the `root` user move independently of your personal user can prove very convenient in recovery situations.


With the terminal, check for the `config.txt` file and be prepared to edit it with the `nano` editor.


![img](assets/it/24.webp)


The editing should be done at the bottom of the entire `config`, after the words `[All]`. It is at this point that you will add the `dtoverlay` commands shown at the beginning of the tutorial.


![img](assets/it/25.webp)


Save, close, and restart. In the following step we will go to the exploration of the little Raspberry.


## What to Expect from this Device?

Looking at the [technical specifications](https://www.raspberrypi.com/products/raspberry-pi-zero/) from the Raspberry website, the PI Zero has a single-core BCM2835 processor and 512 MB of RAM, therefore it does not appear to be very powerful.


Since the terminal is lighter, we will use the command line to explore system configurations.


When you power up you will see a brief rainbow-colored screen, followed by a welcome message from Raspberry and, in the lower left corner, kernel messages related to booting.


When the PI OS desktop appears, open the terminal and type:


```bash
uname -a
```

This command will show you the kernel version currently in use on the screen, plus other information.


![img](assets/it/26.webp)


You can also see information on CPU and hardware by typing:


```bash
lscpu
```


![img](assets/it/27.webp)


And also see `proc/mem/info`.


![img](assets/it/28.webp)


To find out the version of Debian and the release codename:


``` bash

lsb_release -a

```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```


![img](assets/it/31.webp)


``` bash

df

```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```


![img](assets/it/32.webp)


## Use

Although the performance seems limited (on paper and compared to the power of today's machines) the PI Zero is performant, especially as a terminal.



- First you can go to the main menus and get inspired by the _Add/Remove software_ panel, where you will find a number of utilities to program and practice. Remember that you can also do this from the terminal, but always with `root` privileges.


![img](assets/it/33.webp)



- You can "adopt" this offline device to store a variety of confidential documents, which will remain accessible when needed, without ever being exposed to the Internet.
- You can use this configuration to generate your GPG keys securely.
- You could even use this new "little toy" as an airgap signing device, [by following the advice of Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).


Among the Wallets that I am familiar with, the only one that provides a 32-bit release is Electrum. Well: the Zero IP as we prepared it in this tutorial would allow you to keep the private keys offline the set up for Wallet airgap that we covered in this tutorial:


https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Conclusions

The setup has, probably, one big weakness: the micro SD is a medium that could give problems. It is vulnerable to heavy use; perhaps you already have experience with this, from using it with your phone. After installing all the software you will want to use on the Zero airgap IP, make a good backup of the precious micro SD, using the Raspi OS tool you have available.


![img](assets/it/34.webp)


As your needs grow, and with them your budget possibilities, you can explore other Raspberry or similar solutions. Speaking of memory, for example, the PI 5 offers the possibility of assembling an M2 NVME drive, which is certainly more robust than microSD.


Don't forget to take notes and document every step of utility software installation that you are about to use offline. **sooner or later an updated Raspi OS will come out** that you will definitely want to take advantage of. At that point you will have to delete everything and do it all over again (perhaps with a new micro SD 😂).


The exercise we just did, assuming it is your first experiment as well, you will remember for a long time. It is not always possible to devote hardware to `embedded` operations offline, without neglecting attention to an airgapped machine to turn on and check from time to time.


You got it done, though, congratulations! And you will be able to suggest this solution to all those who need to keep their budgets down.