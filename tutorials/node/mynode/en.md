---
name: My Node
description: Set up your bitcoin MyNode
---

![image](assets/0.webp)

[My Node](https://mynodebtc.com/) is the easiest, most powerful way to run a Bitcoin and Lightning node! We combine the best open source software with our interface, management, and support so you can easily, privately, and securely use Bitcoin and Lightning.

## Types of Node setups

There are various Node setups. MyNode is excellent. There are many apps that come with it, and even more if you pay for the premium version. It is otherwise very tedious downloading all those apps yourself. The MyNode makes it quite easy as you’ll see.

An alternative and similar option is RaspiBlitz. The GUI is not as nice, and the apps overlap a lot with the apps that come with MyNode, but Raspiblitz is free open source software (FOSS) and MyNode is not quite. Another difference is that MyNode is run in a Docker container. I find Docker daunting and hard to troubleshoot. This is only a problem if you run into errors or bugs. The developer offers help for premium users and there is a Telegram chat group too.

The RaspiBlitz is just multiple programs installed on Linux, without Docker. The external hard drive can easily be attached to another Linux machine with Bitcoin Core, and away you go, should you need.

Another option is to just install Bitcoin Core and an Electrum Server variety (there are several) on an operating system. I have guides for Linux (Raspberry Pi), Mac, and Windows.

## Shopping list

- Raspberry Pi 4, 4Gb memory or 8Gb (4Gb is plenty)
- Official Raspberry Pi Power (Very Important! Don’t get generic, seriously)
- A case for the Pi. FLIRC case is awesome. The entire case is a heat sink and you don’t need a fan, which can be noisy
- 16 Gb microSD card (you need one, but a few are handy)
- A memory card reader (most computers won’t have a slot for a microSD card).
- External SSD 1Tb hard drive.  
  Note: SSD is crucial. don't use portable external hard drive even tho it’s cheaper
- An ethernet cable (to connect to your home router)
- You do not need a monitor

## Download MyNode Image

Navigate to the MyNode website Link

![image](assets/1.webp)

Click `Download Now`

Download the Raspberry Pi 4 version:

![image](assets/2.webp)

It’s a big file:

![image](assets/3.webp)

Download the SHA 256 hashes

![image](assets/4.webp)

Open the terminal on Mac or Linux or Command Prompt for Windows. Type:

```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```

The computer thinks for 20 seconds or so. Then, check that the output hashfile matches the one downloaded from the website in the previous step. If it’s identical, you can proceed.
Flash the SD card

## Download and install Balena Etcher. Link

I was unable to find the digital signature for this. If you know how, please let me know and I’ll update this article.

Etcher is self-explanatory to use. Insert your micro SD card and flash the Raspberry Pi software (.img file) onto the SD card.

![image](assets/5.webp)
![image](assets/6.webp)
![image](assets/7.webp)
![image](assets/8.webp)
![image](assets/9.webp)
![image](assets/10.webp)
![image](assets/11.webp)

Once done, the drive is no longer readable. You may get an error from the operating system, and the drive should disappear from the desktop. Pull out the card.

## Set up the Pi and insert the SD card

The parts (case not shown):

![image](assets/12.webp)
![image](assets/13.webp)

Connect the ethernet cable, and the hard drive USB connector (not power yet). Avoid connecting to the blue-coloured USB ports in the centre. They are USB 3. MyNode recommends you use the USB 2 port, even though the drive may be USB 3 capable.

![image](assets/14.webp)

The micro SD card goes here:

![image](assets/15.webp)

Finally, connect the power:

![image](assets/16.webp)

## Find the IP address of the Pi

You never need a monitor with the MyNode. You do, however, need another computer on the home network. If you’re Pi is not connected by ethernet, and you want to rely on WiFi, finding the IP requires high-level computer skills. Can’t help you, sorry. You need an ethernet connection. (The problem comes from needing access to a monitor and the operating system to connect to the WiFi and enter a password).

Check your router, for a list of all the IPs of all the connected devices.

I typed 192.168.0.1 in the Browser (instructions that came with my router), logged in, and was able to see a device “MyNode” with the IP 192.168.0.18. Note these IP addresses are not publicly visible to the internet (they go through the router first), they are just identifiers for devices on your home network.

Finding the IP is crucial.

**Note:** you can use the terminal on a Mac or Linux machine to find the IP address of all Ethernet connected devices on the home network using the command “arp -a”. The output is not as pretty as what the router will display, but all the information you need is there. If it’s not obvious which is the Pi, perform trial and error.

## SSH into the Pi

You have the option to log in to the device remotely by SSH command, but it is not required (it is if RaspiBlitz Node). I’ll show you how anyway, as it is very handy.

Open a Mac or Linux computer (for Windows, download putty, an SSH tool) and type:

```bash
ssh admin@192.168.0.18
```

Use your own IP address. The user name for the MyNode device is “admin” by default. The password is “bolt” by default.

If you have used your Pi before and switched the micro SD card around, you will get this error:

![image](assets/17.webp)

What you need to do is to navigate to where the “known_hosts” file is and delete it. It’s safe to. The error message shows you the path. For me it was /Users/MyUserName/.ssh/

Don’t forget the “.” before ssh, this indicates it is a hidden directory.

Then try the ssh command again.

This time you’ll see this output:

![image](assets/18.webp)

The file you deleted has been deleted and you are adding a new fingerprint. Type yes and <enter>.

You’ll be asked to enter the password. It is “bolt”

You’ve now got terminal access to the MyNode Pi, without a monitor, and can confirm it’s all loaded smoothly.

![image](assets/19.webp)

## Access via the Web Browser

Open a browser. It needs to be a computer on your home network, you can’t do this from outside. There’s a way, but it’s hard. I haven’t tested it.

Type the IP address in the browser address window. This will happen:

![image](assets/20.webp)

Enter the password “bolt” – change it later.

Then this will happen:

![image](assets/21.webp)

Choose Format Drive

![image](assets/22.webp)

Now we wait.

At some point you will be asked if you want to put in your product key, or use the free “community edition” — I’m going to show the Premium edition. I do recommend paying for the premium version if you can afford it, it’s very worth it.

![image](assets/23.webp)

You’ll then see the progress of blocks downloaded. It takes days:

![image](assets/24.webp)

It’s safe to turn off the machine during the download if you need to. Go to settings and find the button to power off the machine. Don’t just yank the cord, you could corrupt the installation or the hard drive.

Makes sure, early on, go to”Settings” and disable quicksync. It will begin the initial block download from the beginning.

![image](assets/25.webp)

I wanted to proceed with creating the guide, so here is another MyNode I prepared earlier. This is what the page looks like when the blockchain is synced, and several “apps” have been enabled and synced:

![image](assets/26.webp)

Note that Electrum Server needs to sync as well, so as soon as Bitcoin Blockchain is synced, click the button to start that process – takes a day or two. Everything else is enabled in a few minutes once you select to enable it. You can click things and explore. You won’t break anything. If something does break (this happened to me, but I think because I had cheap parts) you’ll have to re-flash and start downloading again. The problem I have with MyNode is that if you need to “re-flash” you end up needing to start the blockchain sync again from scratch. There are technical ways around this, but it’s not easy.

If you want to try another node as well, say a RaspiBlitz, you need an additional SSD external hard drive, and another micro SD card to flash. Otherwise, it’s the same equipment, you just can’t run MyNode and RaspiBlitz simultaneously, obviously. If you want to do that, time to shop for another Raspberry Pi.

Now that you have a node running, use it, don’t just let it sit there doing nothing for you. Follow my article (and video) on how to connect your Electrum Desktop Wallet to Electrum Server and Bitcoin Core here.
