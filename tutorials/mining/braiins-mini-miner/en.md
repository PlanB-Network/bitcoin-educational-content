---
name: Braiins Mini Miner
description: Making Mining easily from home.
---
![cover](assets/cover.webp)


## Introduction


The Mini Miner braiins BMM 100 is a product created by Mining pool Braiins. This device has an attractive design and is extremely quiet. It produces 1.1 Th/s of computing power and consumes about 40 watts. Unlike other devices, it is not open source, but it is really easy to install, it really only takes a few clicks! The Mini Miner BMM 100 is the first version released. Now version 2 is in production, called BMM 101, which differs from the first one in having a larger display and the presence of Wi-Fi, but the installation procedures are the same.


You can also find much more important information by checking out the complete guide directly on [manufacturer's site](https://braiins.com/hardware/mini-Miner-bmm-100).


## Overview of BMM 100


the device looks like a parallelepiped with a display on the front


![image](assets/en/01.webp)


a fan on the upper side


![image](assets/en/02.webp)


while on the back side we have: the hole for the power, space for an SD card (which might be needed for any updates), a little button that says `IP REPORT` which lets you know the IP address of the mini Miner, which address is needed to access the device dashboard. Once the button is pressed, the IP address is displayed for about 5 seconds, then disappears and the set screen reappears. However, if you need to change some settings, simply mash the button in question again and the IP address will reappear on the screen. Continuing with the list we find an Ethernet port and an access to perform a device reset, for which you will need to grab a pin and hold for 10 seconds in order to reset all the settings of the mini Miner. Finally we find two indicator lights, one green and one red, which indicate to us the status of the Miner.


![image](assets/en/03.webp)


## Connecting the Mini Miner


You will need to connect the device to the internet via ethernet, note that with the new version (BMM 101) this is no longer necessary. Back to this mini Miner, once we locate the location we will need to connect it first to the internet line and then to the power: the device will automatically turn on and show its IP address on the screen.


## Configuration


We need to open a browser and enter the IP address that shows us the mini Miner in the search bar. I remind you that in order to find the device on the network you will have to be local, so you will have to have the computer you are using connected to the same network as the mini Miner. once we enter the IP address we press enter and the login page to the mini Miner's operating system, which is Braiins OS, will appear on the screen.


![image](assets/en/06.webp)


In order to log in you will have to enter `root` as your username, while you can leave the password blank. Click on login and your mini Miner dashboard will appear.


![image](assets/en/07.webp)


## General settings


Let's go to System


![image](assets/en/24.webp)


within the settings we find some general settings such as theme (light or dark), language, time zone, and password change.


![image](assets/en/25.webp)


If we go to "Mini Miner Screen" instead we have the settings of our mini Miner, such as the screen display. We can choose whether to show the time, or the price of Bitcoin, or the screen with the machine status information such as product hash, temperature, watts consumed, and so on. Here it is up to you to choose what you want to see on the screen; we can also change the brightness of the screen, set the night mode, and display the time with 12-hour or 24-hour format.


![image](assets/en/26.webp)


Once you have made changes, click on `Save Changes` and you will see the changes on your device screen


![image](assets/en/27.webp)


## Connection to Mining pool


Now we are not yet operational, because we have to connect to a pool in order to start mining, so we have to go to "Configuration"


![image](assets/en/08.webp)


and the first entry is just `Pools`.


![image](assets/en/09.webp)


Here we will have to decide which pool to use. In this tutorial I will show you two options. The first is to connect us to Mining pool Braiins which is also used by professional miners, as you can see from this tutorial:


https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

The second option is to connect us to a Mining pool that mina in solo, like Public Pool, follow this guide to do so:


https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins pool


To connect to this pool we need to create an account. this pool also makes payments using Lightning Network, so we will be able to receive a few Sats per day. To do this we need to set up a Address lightning on which to receive the rewards. If you do not know how to create an account on braiins pool or how to set up your Address lightning you can follow this guide:


https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Once that is done we are in the Braiins pool dashboard. What we have to do is tell the pool that we want to connect with one of our Miners, so on the left side of the screen you will find a number of entries. We need to go to "workers."


![image](assets/en/04.webp)


and we need to click on the purple button on the right that says "Connect workers."


![image](assets/en/05.webp)


Here comes the window with the information we need to connect our mini Miner to the pool. Here the only change we can make is to choose Stratum V2. To find out what Stratum v2 is see this entry in the [glossary](https://planb.network/en/resources/glossary/stratum-v2).


![image](assets/en/10.webp)


Now we need to copy this string that starts with stratumv2. So we click on the little "copy" symbol, then we go to the dashboard of our mini Miner that we had left in configuration and pools. We click on add new pool


![image](assets/en/11.webp)


and paste the string we copied into the space below Pool URL.


![image](assets/en/12.webp)


Now we need to add username and password. Let's go back to the pool dashboad. Underneath we also have a userID and password. The userID and our username, the one we gave when creating the account, plus the name of the Miner we want to put in. you can decide whether or not to give a name to the device you are connecting to the pool, it is optional, but it is advisable to put it in, so if you connect multiple devices it will be easier to identify them right away. If you don't want to put anything instead you can leave `workerName`.


![image](assets/en/13.webp)


We then go to our mini Miner and enter the username. Here we will enter in my case "finalstepbitcoin" which is my userID, miniminer dot. This is the name I decided to give the device. If you don't want to name it just write userid dot workername. In my case it would be finalstepbitcoin.workername. Once you have entered the username you can choose a password and write it in the blank field. You can also put anithing123, which is the one also shown in the pool screen, but it simply wants to indicate that you can put any password you want.


Once you have entered all the data you have to press the save button on the right (the one shaped like a floppy disk) and in this way you have configured the pool data in the mini Miner.


![image](assets/en/14.webp)


Now you have to go back to the pool dashboard and click on "Connected! Go back."


![image](assets/en/15.webp)


We have connected our mini Miner to the braiins pool! You can now see it in the list of workers. If it does not show up just do a refresh and wait a few moments. Once it appears, verify that it has the status "OK" with a green check mark.


![image](assets/en/17.webp)


if you go back to the dashboard you should start to see movement on the graph and see the Hashrate of our device. This means that the pool is receiving our work and therefore we are for all intents and purposes undermining.


![image](assets/en/16.webp)


### Public Pool


Through this pool one can try one's luck and mine solo, leaning on a pool. In this case we will not receive reward, but we will receive the full reward if we ever manage to mine a block. We will then link to public pool, a Mining-only pool that is completely open source. We open a new window on the browser and go to [web.public-pool.io](https://web.public-pool.io/#/).


![image](assets/en/18.webp)


there goes a page with all the information we need. We then copy there the stratum address


![image](assets/en/19.webp)


then we go back to the dashboard of our mini Miner, go to configuration and to pools, click on add new pool (same process as seen above) and paste the 'stratum address under pool url.


![image](assets/en/20.webp)


Now let's go back to the pool page and see that as the username we have to enter a Bitcoin address, which will be the one on which we will receive the reward in case we undermine a block, then a dot and then the name of our device, as we did previously with Braiins Pool, while the password we can choose ourselves.


![image](assets/en/21.webp)


We go back to the mini Miner and under username we paste an address Bitcoin followed by period and the name, I will put `miniminer`. In the password instead I will put test, you enter whatever you want.


![image](assets/en/22.webp)


Now we save the settings and disable the Braiins pool.


![image](assets/en/23.webp)


Good! We are now mining on public pool!


![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)