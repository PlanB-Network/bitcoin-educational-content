---
name: RaspiBlitz
description: Guide to set up your RaspiBlitz
---

![image](assets/0.webp)

The RaspiBlitz is a do-it-yourself Lightning Node (LND and/or Core Lightning) running together with a Bitcoin-Fullnode on a RaspberryPi (1TB SSD) and a nice display for easy setup & monitoring.

RaspiBlitz is mainly targeted for learning how to run your own node decentralized from home - because: Not your Node, Not your Rules. Discover & develop the growing ecosystem of the Lightning Network by becoming a full part of it. Build it as part of a workshop or as a weekend project yourself.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - How To Run A Lightning and Bitcoin Full Node by BTC session

# Parman’s Raspiblitz Setup Guide

The Raspiblitz is an excellent system for running a Bitcoin Node and associated apps. I recommend this and the My Node node to most users (Have two nodes for redundancy ideally.) One major advantage is that the Raspiblitz node is “Free Open Source Software”, unlike MyNode or Umbrel. Why is that important? Vlad Costa explains. You can also run the RaspbiBlitz with a WiFi connection rather then ethernet – here’s a supplemental guide for that. (I haven’t found a way to do this with MyNode).

You can buy a ready made node with an attached mini screen, or you can build it yourself (you don’t need a screen).

The guide on the github page is excellent, but possibly too detailed for a moderately experienced user. My instructions will be more succinct and hopefully easier you follow.

Essentially, the process is very similar to the process of setting up a MyNode node with a Raspberry Pi 4. The Raspiblitz guide suggest you buy a monitor, but you really don’t need one, and I wouldn’t recommend it. You don’t even need an extra keyboard or mouse. Just access the device’s terminal menu via a computer on the same home network, and use the ssh command using terminal. This is possible with Linux/Mac (easy) and a tiny bit harder with Windows.

## Step 1: Buy the equipment.

You need exactly the same equipment that you need to run a MyNode node. You could try one or the other, the only difference is the data on the micro SD card.

- Raspberry Pi 4, 4Gb memory or 8Gb (4Gb is plenty)
- Official Raspberry Pi Power (Very Important! Don’t get generic, seriously)
- A case for the Pi. (FLIRC case is awesome. The entire case is a heat sink and you don’t need a fan, which can be noisy)
- 32 Gb microSD card (you need one, but a few are handy. )
- A memory card reader (most computers won’t have a slot for a microSD card).
- External SSD 1Tb hard drive.
- An ethernet cable (to connect to your home router).

You do not need a monitor (or keyboard or mouse)

Note: This is the wrong hard drive: This is a portable external hard drive. It is not an SSD. SSD is crucial. This is why it’s cheap (Price in AUD)

![image](assets/1.webp)

This is the right type to get:

![image](assets/2.webp)

This is faster, but unnecessarily expensive:

![image](assets/3.webp)

## Step 2: Download Raspiblitz Image

Navigate to the Raspiblitz github website, and find the “download image” link:

![image](assets/4.webp)

The sha-256 hash of the downloaded file is provided on the website. It will change with each update. It you don’t understand what this is about, you should, so I wrote a guide you can read here.

![image](assets/5.webp)

## Step 3: Verify Image

Before proceeding, if you don’t know your way around the file system on the command line, it’s easy to learn, and you should.

Here is a useful video for Linux, but applies to Mac as well.

For Windows, here’s a simple tutorial.

Mac/Linux

Wait for the file to finish downloading (important!), then with terminal open, navigate to where you downloaded the file, and type the following command:
```bash
shasum -a 256 xxxxxxxxxxxxxx
```

where `xxxxxxxxxxxxxx` is the name of the file you just downloaded. If you are not in the directory where that file is, you have to type the full path.

The computer thinks for 20 seconds or so. Check that the output hashfile matches the one downloaded from the website in the previous step. If it’s identical, you can proceed.
Windows

Open the command prompt and navigate to where the file is downloaded, and type this command:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

where `xxxxxxxxxxxxxx` is the name of the file you just downloaded. If you are not in the director where that file is, you have to type the full path.

The computer thinks for 20 seconds or so. Check that the output hashfile matches the one downloaded from the website in the previous step. If it’s identical, you can proceed.

## Step 4: Flash the SD card

You can use Balena Etcher to do this. Download it here.

Etcher is self explanatory to use. Insert your micro SD card and flash the Raspiblitz software (.img file) onto the SD card.

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

Once done, the drive is no longer readable. You may get an error from the operating system, and the drive should disappear from the desktop. Pull out the card.

## Step 5: Set up the Pi and insert the SD card

The parts (case not shown):

![image](assets/10.webp)

![image](assets/11.webp)

Connect the ethernet cable, and the hard drive USB connector (not power yet). Avoid connecting to the blue coloured USB ports in the centre. They are USB 3. Use the USB 2 port, even though the drive may be USB 3 capable (more reliable).

![image](assets/12.webp)

The micro SD card goes here:

![image](assets/13.webp)

Finally, connect the power:

![image](assets/14.webp)

## Step 6: Find the IP address of the Pi

You never need a monitor with the Raspiblitz. You do however, need another computer on the home network. If you’re Pi is not connected by ethernet, and you want to rely on WiFi, finding the IP requires some computer skills. Can’t help you, sorry. You need an ethernet connection. (The problem comes from needing access to a monitor and the operating system to connect the WiFi and enter a password.)

Check you router, for a list of all the IPs of all the connected devices.

I typed 192.168.0.1 in the Browser (instructions that came with my router), logged in, and was able to see my device with the IP 192.168.0.191. Note these IP addresses are not publicly visible to the internet (they go through the router first), they are just identifiers for devices on your home network.

Finding the IP is crucial.

**Note:** you can use the terminal on a Mac or Linux machine to find the IP address of all Ethernet connected devices on the home network using the command “arp -a”. The output is not as pretty as what the router will display, but all the information you need is there. If it’s not obvious which is the Pi, perform trial and error.

## Step 7: SSH into the Pi

Remember to put the SD card into the Pi before switching it on. Wait a few minutes, and then on another Linux/Mac, open the terminal.

For Mac/Linux, in the terminal type:

```bash
ssh admin@You_Pi's_IP_address
```

For Windows, you’ll need to install putty to ssh into the Pi. Type the same command as above.

The first time you do this, or whenever you change the OS of the Pi by switching the SD card, you may or may not get this error…

![image](assets/15.webp)

The way to fix it is to navigate to where the “known_hosts” file is (it tells you in the error message), and delete it. The command is "rm known_hosts"

Then, repeat the ssh command to log in. This will happen…

![image](assets/16.webp)

Type yes (full word) to proceed.

If successful, you’ll be asked for a password. This is not for your computer, but the raspiblitz. The generic password is “raspiblitz”, and youll change that later. The terminal window will turn blue and you’ll have menu options like the old DOS menus. Navige with the arrow keys or mouse.

![image](assets/17.webp)

Follow the prompts, set your passwords, and then it will detect your hard drive and give you the option to format it if needed.

Then you’ll be asked if you want to copy the blockchain data from another source or re-downloaded it. Copying it is a learning process and the instructions are quite good, and good to keep handy….

![image](assets/18.webp)

The simple but slower way is to download the whole chain from scratch…

![image](assets/19.webp)

Lots of text will flash across the terminal screen. You might mistake it for the process of the blockchain download, but it looks like, to me, it’s generating a private key for communication.

Then lightning options appear.

![image](assets/20.webp)

Make a new password to lock your lighting wallet, then a new wallet will be created and you’ll be given 24 words to write down…

![image](assets/21.webp)

Do make sure you write it down and keep it secure. I heard of one person who didn’t because he wasn’t planning to use lightning, but then a year later decided to use it, and opened channels. Then realising his words were not backed up, and I recall it was not possible to extract the words again from the device, he had to close all his channels and start again. He got away with it, but others might not be so lucky.

Following this, a few minutes of text scrolls down the terminal window. Then…

![image](assets/22.webp)

You’ll be logged out of the ssh session. Log back in, this time with your new password, password A. Once in you’ll be asked for password C to unlock your lightning wallet.

Now we wait. See you in 2 weeks. You can close the terminal, it doesn’t do anything to the Pi, it’s just a communication window.

![image](assets/23.webp)

If for whatever reason, you want to shutdown the Pi before the blockchain has finished downloading, that’s fine as long as you do it properly. The blockchain will continue downloading where it left off once you reconnect.

Hit CTRL+c to exit the blue screen. You’ll be accessing the Pi’s Linux terminal. Here you can type “menu” which loads the following screen, and from there you can power off the Pi.

![image](assets/24.webp)

END of the guide

So from now your node si ready to go. If you still help navigate more option, refer to the github for more tutoriel and guide https://github.com/raspiblitz/raspiblitz#feature-documentation
