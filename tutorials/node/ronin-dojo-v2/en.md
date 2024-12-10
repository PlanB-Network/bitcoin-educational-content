---
name: RoninDojo v2
description: Installing your RoninDojo v2 Bitcoin node on a Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, certain features of RoninDojo, such as Whirlpool, are no longer operational. However, it is possible that these tools could be reinstated or relaunched differently in the coming weeks. Additionally, since the RoninDojo code was hosted on Samourai's GitLab, which was also seized, it is currently not possible to download the code remotely. The RoninDojo teams are likely working on republishing the code.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

> "*Use Bitcoin with privacy.*"

In a previous tutorial, we had already explained the procedure for installing and using RoninDojo v1. However, over the last year, the RoninDojo teams have launched version 2 of their implementation, which marked a significant turning point in the software's architecture. Indeed, they moved away from the Linux Manjaro distribution in favor of Debian. Consequently, they no longer offer a pre-configured image for automatic installation on Raspberry Pi. But there is still a method for proceeding with a manual installation. This is what I used for my own node, and since then, RoninDojo v2 has been working wonderfully on my Raspberry Pi 4. I am therefore offering a new tutorial on how to manually install RoninDojo v2 on a Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0



## Table of Contents:
- What is RoninDojo?
- Which hardware to choose for installing RoninDojo v2?
- How to assemble the Raspberry Pi 4?
- How to install RoninDojo v2 on a Raspberry Pi 4?
- How to use your RoninDojo v2 node?

## What is RoninDojo?
Dojo is initially a full Bitcoin node implementation, based on Bitcoin Core, and developed by the Samourai Wallet teams. This solution can be installed on any equipment. Unlike other Core implementations, Dojo has been specifically optimized to integrate with the Android application environment of Samourai Wallet. As for RoninDojo, it is a utility designed to facilitate the installation and management of a Dojo, as well as various other complementary tools. In short, RoninDojo enriches the basic implementation of Dojo by integrating a multitude of additional tools, while simplifying its installation and management.

Ronin also offers [a node-in-box solution, called the "*Tanto*"](https://ronindojo.io/en/products), a device with RoninDojo already installed on a system assembled by their team. The Tanto is a paid option, which may be interesting for those who prefer to avoid technical complications. But since the source code of RoninDojo is open, it is also possible to deploy it on your own hardware. This alternative, more economical, nevertheless requires some additional manipulations, which we will cover in this tutorial.
RoninDojo is a Dojo, thus it allows for easy integration of Whirlpool CLI into your Bitcoin node to provide the best possible coinjoin experience. With Whirlpool CLI, it becomes possible to continuously remix your bitcoins, 24 hours a day, 7 days a week, without requiring your personal computer to remain on.

Beyond Whirlpool CLI, RoninDojo includes a variety of tools to enhance your Dojo's functionalities. Among these, the Boltzmann calculator analyzes the privacy level of your transactions, the Electrum server allows for the connection of your Bitcoin wallets to your node, and the Mempool server enables you to view your transactions locally, without leaking information.

Compared to other node solutions like Umbrel, RoninDojo is clearly focused on on-chain solutions and privacy tools. Unlike Umbrel, RoninDojo does not support setting up a Lightning node nor the integration of more generalist server applications. Although RoninDojo offers fewer versatile tools than Umbrel, it has all the essential functionalities for managing your on-chain activity.

If you do not need generalist functionalities or those related to the Lightning Network as offered by Umbrel, and you are looking for a simple, stable node with essential tools such as Whirlpool or Mempool, RoninDojo could be the ideal solution. While Umbrel tends to become a mini multitasking server oriented towards the Lightning Network and versatility, RoninDojo, in line with the philosophy of Samourai Wallet, focuses on fundamental tools for user privacy.

Now that we have outlined RoninDojo, let's see together how to set up this node.

## What hardware to choose for installing RoninDojo v2?
RoninDojo offers an image for automatic installation of its software on a [RockPro64](https://ronindojo.io/en/download). However, our tutorial focuses on the manual installation procedure on a Raspberry Pi 4. Although the Raspberry Pi 5 has been recently launched, and this tutorial should theoretically be compatible with this new model, I have not yet had the chance to test it personally, and I have found no feedback from the community. As soon as I acquire the Pi 5 and compatible components, I will update this tutorial to keep you informed. In the meantime, I recommend prioritizing the Pi 4, as it works perfectly for my node.
For my part, I run RoninDojo on a Raspberry Pi equipped with 8 GB of RAM. Although some community members have managed to get it working on devices with only 4 GB of RAM, I have not tested this configuration myself. Given the small price difference, it seems wise to opt for the 8 GB RAM version. This could also prove useful if you plan to repurpose your Raspberry Pi for other uses in the future.
It is important to note that the RoninDojo teams have reported frequent issues related to the case and the SSD adapter. I have faced these issues myself. **Therefore, it is strongly recommended to avoid cases equipped with a USB cable for your node's SSD.** Instead, prefer a storage expansion card specifically designed for your Raspberry Pi:

![storage expansion card RPI4](assets/notext/1.webp)

To store the Bitcoin blockchain, you will need an SSD compatible with the storage expansion card you have chosen. Currently (February 2024), we are in a transition phase. It is expected that, in a few months, 1 TB disks will no longer be sufficient to contain the growing size of the blockchain, especially considering the various applications you plan to integrate into your node. Some therefore recommend investing in a 2 TB SSD for peace of mind in the long term. However, with the downward trend in SSD prices year after year, others suggest settling for a 1 TB disk, which should be sufficient for one or two years, arguing that by the time it becomes obsolete, the cost of 2 TB models will probably have decreased. The choice thus depends on your personal preferences. If you plan to keep your RoninDojo for a significant duration and wish to avoid any technical handling in the coming years, the option of a 2 TB SSD seems to be the most prudent, as it offers you a comfortable margin for the future.

In addition, you will need various small components:
- A case equipped with a fan to house your Raspberry Pi and your storage expansion card. Kits including both the SSD expansion card and a compatible case are available online;
- A power cable for your Raspberry Pi;
- A micro SD card of at least 16 GB (although 8 GB could technically suffice, the price difference between 8 and 16 GB cards is often negligible);
- An RJ45 Ethernet cable for network connection.

![node material](assets/notext/2.webp)

## How to assemble the Raspberry Pi 4?
The assembly of your node will vary depending on the chosen hardware, especially the type of case. However, the general outline of the steps to follow remains generally similar in the assembly.
Start by installing your SSD on the storage expansion card, taking care to secure the two locking screws at the back.

![assembly1](assets/notext/3.webp)

Then attach your Raspberry Pi to the expansion card.

![assembly2](assets/notext/4.webp)

Also, attach the fan to the Raspberry Pi.

![assembly3](assets/notext/5.webp)

Connect the various components, paying attention to use the correct pins, referring to the manual of your case. Case manufacturers often offer video tutorials to assist you in the assembly. In my case, I have an additional expansion card equipped with an on/off button. This is not essential for making a Bitcoin node. I mainly use it to have a power button.

If, like me, you have an expansion card equipped with an on/off button, do not forget to install the small "Auto Power On" jumper. This will allow your node to start automatically as soon as it is powered on. This feature is particularly useful in the event of a power outage, as it allows your node to restart by itself, without manual intervention on your part.

![assembly4](assets/notext/6.webp)

Before inserting all the hardware into the case, it is important to check the proper functioning of your Raspberry Pi, the storage expansion card, and the fan by powering them on.

![assembly5](assets/notext/7.webp)

Finally, install your Raspberry Pi in its case. Be aware, a later step will require adding the micro SD card into the appropriate port on the Raspberry Pi. If your case is equipped with an opening that allows you to insert the SD card without having to open it (as is the case with mine illustrated in the photo), you can proceed to close the case now. However, if your case does not have direct access to the micro SD port, you will need to wait until you have prepared the micro SD card to insert it before finalizing the assembly.

![assembly6](assets/notext/8.webp)

## How to install RoninDojo v2 on a Raspberry Pi 4?

### Step 1: Prepare the bootable micro SD
After assembling your hardware, the next step is to install RoninDojo. For this, we will prepare a bootable micro SD card from your computer, by burning the appropriate disk image onto it.
You will need to use the _**Raspberry Pi Imager**_ software, designed to facilitate the downloading, configuring, and writing of operating systems on a micro SD card for use with a Raspberry Pi. Start by installing this software on your personal PC:
- For Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- For Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- For Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Once the software is installed, open it, and insert your micro SD card into your personal computer. From the Raspberry Pi Imager interface, select `CHOOSE OS`:

![choose OS](assets/notext/9.webp)

Next, go to the `Raspberry Pi OS (other)` menu:

![choose OS others](assets/notext/10.webp)

Choose the operating system named `Raspberry Pi OS (Legacy, 64-bit) Lite`, which is `0.3 GB` in size:

![choose OS Legacy Lite](assets/notext/11.webp)

After selecting the operating system, you will be redirected to the main menu of Raspberry Pi Imager. Click on `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Select your micro SD card:

![choose micro sd](assets/notext/13.webp)

After choosing the operating system and the micro SD card, click on `NEXT`:

![choose next](assets/notext/14.webp)

A new window will appear. Select `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

In this window, go to the `GENERAL` tab and make the following settings (which are very important for it to work):
- Enable the option and assign `RoninDojo` as the hostname;
- Enable `Set username and password`, enter `pi` as the username, choose a password, and note this information, as it will be needed later. These credentials are temporary and will be deleted afterward;
- Disable `Configure Wi-Fi`;
- Enable `Set locale settings` and select your time zone as well as the keyboard type corresponding to your computer;

![general settings](assets/notext/16.webp)

In the SERVICES tab, click on the `Enable SSH` box and select `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Also, ensure that in the `OPTIONS` tab, telemetry is disabled:

![options settings](assets/notext/18.webp)

Click on `SAVE`:

![settings save](assets/notext/19.webp)
Confirm by clicking on `YES` to start creating the bootable micro SD card:
![settings yes](assets/notext/20.webp)

A message will inform you that all data on the micro SD card will be erased. Confirm by clicking on `YES` to start the process:

![overwrite micro SD](assets/notext/21.webp)

Wait until the software finishes preparing your micro SD card:

![writing micro SD](assets/notext/22.webp)

When the message indicating the end of the process appears, you can remove the micro SD card from your computer:

![writing micro SD completed](assets/notext/23.webp)

### Step 2: Complete the Node Assembly
You can now insert the micro SD card into the appropriate port of your Raspberry Pi.

![micro SD](assets/notext/24.webp)

Then connect your Raspberry Pi to your router using the Ethernet cable. Finally, turn on your node by connecting the power cable and pressing the power button (if your setup includes one).

### Step 3: Establish an SSH Connection with the Node
First, it is necessary to find the IP address of your node. You have the option to use a tool such as _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ or _[Angry IP Scanner](https://angryip.org/)_, or check the administration interface of your router. The IP address should be in the form `192.168.1.??`. **For all the following commands, replace `[IP]` with the actual IP address of your node**, (removing the brackets).

Launch a terminal.

To remove a possible key already associated with the IP address of your node, execute the command: 
`ssh-keygen -R [IP]`. 

An error following this command is not serious; it simply means that the key does not exist in your list of known hosts (which is rather likely). For example, if the IP of your node is `192.168.1.40`, the command becomes: `ssh-keygen -R 192.168.1.40`.

Next, establish an SSH connection with your node by executing the command: 
`ssh pi@[IP]`.
A message will appear regarding the host's authenticity: `The authenticity of host '[IP]' can't be established.` This indicates that the authenticity of the device you are trying to connect to cannot be verified due to a lack of a known public key. When connecting via SSH to a new host for the first time, this message will always appear. You must respond `yes` to add its public key to your local directory, which will prevent this warning message from appearing during future SSH connections to this node. Therefore, type `yes` and press `enter` to validate.
You will then be asked to enter your password, the one previously set as temporary in step 1. Validate with `enter`. You will then be connected to your node via SSH.

In summary, here are the commands to execute:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Enter the temporary password and validate.

### Step 4: Update and Preparation
You are now connected to your node via an SSH session. On your terminal, the command prompt should be: `pi@RoninDojo:~ $`. To start, update the list of available packages and install updates for existing packages with the following command:
`sudo apt update && sudo apt upgrade -y`

Once the updates are completed, proceed to install *Git* and *Dialog* using the command:
`sudo apt install git dialog -y`

Next, clone the `master` branch of the _RoninOS_ Git repository by executing:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Run the script `customize-image.sh` with the command:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**It is important to let the script run without interruption and to wait patiently for the end of its process**, which takes about 10 minutes. When the message `Setup is complete` appears, you can move on to the next step.

### Step 5: Launching RoninOS
Launch RoninOS with the command:
`sudo systemctl start ronin-setup`

Display the lines of the log file with the command:
`tail -f /home/ronindojo/.logs/setup.logs`

At this stage, **it is important to let RoninOS launch and wait for it** to finish running. This takes about 40 minutes. When `All RoninDojo feature installations complete!` appears, you can proceed to step 6.

### Step 6: Accessing RoninUI and Changing Credentials
After completing the installation, to connect to your node via a browser, ensure that your personal computer is connected to the same local network as your node. If you are using a VPN on your machine, temporarily disable it. To access the node interface in your browser, enter in the URL bar:
- Directly the IP address of your node, for example, `192.168.1.??`;
- Or, type `ronindojo.local`.

Once on the RoninUI homepage, you will be prompted to start the setup. To do this, click on the `Let's start` button.

![lets start](assets/notext/25.webp)

At this stage, RoninUI presents you with your `root` password. It is essential to keep it safe. You can opt for a physical backup, on paper, or save it in a [password manager](https://planb.network/courses/secu101/4/2).

![root password](assets/notext/26.webp)

After saving the `root` password, check the box `I have backed up Root user credentials` and click on `Continue` to proceed.

![confirm root password](assets/notext/27.webp)

The next step involves creating a user password, which will be used both for accessing the RoninUI web interface and for establishing SSH sessions with your node. Choose a strong password and make sure to save it securely. You will need to enter this password twice before clicking on `Finish` to validate. As for the username, it is recommended to keep the default choice, `ronindojo`. If you decide to change it, remember to adjust the commands in the following steps accordingly.

![user credentials](assets/notext/28.webp)

Once these actions are completed, wait for your node to initialize. You will then access the RoninUI web interface. You are almost at the end of the process, only a few small steps left!
![Ronin UI](assets/notext/29.webp)

### Step 7: Remove Temporary Credentials
Open a new terminal on your personal computer and establish an SSH connection with your node using the following command:
`SSH ronindojo@[IP]`

If, for example, the IP address of your node is `192.168.1.40`, the appropriate command will be:
`SSH ronindojo@192.168.1.40`

If you changed your username during the previous step, replacing the default username (`ronindojo`) with another, make sure to use this new name in the command. For example, if you chose `planb` as the username and the IP address is `192.168.1.40`, the command to enter will be:
`SSH planb@192.168.1.40`
You will be asked to enter the user password. Enter it and then press `enter` to validate. You will then access the RoninCLI interface. Use the arrow keys on your keyboard to navigate to the `Exit RoninDojo` option and press `enter` to select it.
![RoninCLI](assets/notext/30.webp)

At this point, you are on your node's terminal, with a command prompt similar to: `ronindojo@RoninDojo:~ $`. To remove the temporary user created during the configuration of the bootable micro SD card, enter the following command and press `enter`:
`sudo deluser --remove-home pi`

You will be prompted to confirm your user password. Enter it and validate by pressing `enter`. Wait for the operation to complete, then use the `exit` command to leave the terminal.

Congratulations! Your RoninDojo v2 node is now configured and ready to use. It will begin its IBD (*Initial Block Download*), proceeding to download and verify the Bitcoin blockchain from the Genesis block. This step involves retrieving all Bitcoin transactions made since January 3, 2009, and takes some time. Once the blockchain is fully downloaded, the indexer will proceed to compress the database. The duration of the IBD can vary considerably. Your RoninDojo node will be fully operational once this process is completed.

**If you are migrating from an old RoninDojo v1 node** to this new version with this tutorial while keeping the same SSD, your node should automatically detect and reuse the existing data on the disk, sparing you the necessity of performing the IBD again. In this case, you will just need to wait for your node to resynchronize with the latest blocks.

### Step 8: "veth* fix"
If you encounter a bug with your RoninDojo v2 on Raspberry Pi, where after a hassle-free installation, your node suddenly becomes unreachable via SSH but recovers after a simple restart, then you need to follow this step 8. This common bug can be easily fixed with a solution developed by the community: the "_veth fix_". This minor correction permanently remedies the abrupt disconnections. Here's how to apply it.

Open a new terminal on your personal computer and establish an SSH connection with your node using the following command: 
`SSH ronindojo@[IP]`

If, for example, your node's IP address is `192.168.1.40`, the appropriate command would be: 
`SSH ronindojo@192.168.1.40`

You will be prompted to enter the user password. Enter it and press `enter` to validate. You will then access the RoninCLI interface. Use your keyboard's arrows to navigate to the `Exit RoninDojo` option and press `enter` to select it.

At this point, you are on your node's terminal, with a command prompt similar to: `ronindojo@RoninDojo:~ $`. To apply the veth* fix, type the following command and press `enter`: 
`sudo nano /etc/dhcpcd.conf`

Confirm your password again and press `enter`.

You will arrive at the `dhcpcd.conf` file. You need to copy the following text, ensuring to include the asterisk, and add it to the bottom of the file: 
`denyinterfaces veth*`

To do this, move to the bottom of the file using the down arrow on your keyboard, then use the right click of your mouse to paste the text on an independent line.

After adding the text, press `ctrl X` to start exiting, followed by `ctrl Y` to confirm saving the changes, and press `enter` to finalize and return to the command prompt. To ensure that the modification has been correctly applied, reopen the `dhcpcd.conf` file using the appropriate command.

To complete the application of the fix, restart your node by executing: 
`sudo reboot now`

At this point, you can close your terminal. Allow the necessary time for your RoninDojo to restart, after which you should be able to reconnect via your browser's graphical interface. This process should fix the encountered bug.

## How to use your RoninDojo v2 node?

### Connecting your wallet software to Electrs
The first use of your freshly installed and synchronized node will be to broadcast your transactions to the Bitcoin network. You will probably want to connect your various wallets to your node in order to broadcast your transactions confidentially. You can do this through Electrum Rust Server (electrs). This application is usually pre-installed on your RoninDojo node. If not, you could manually install it via the RoninCLI interface in `Applications > Manage Applications > Install Electrum Server`.

To obtain the Tor address of your Electrum Server, from the RoninUI web interface, go to:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
You will then need to enter the `Hostname` address ending in `.onion` in your wallet software, accompanied by port `50001`. ![hostname](assets/notext/33.webp)
For example, on Sparrow Wallet, simply go to the tab:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Connecting your wallet software to Samourai Dojo
As an alternative to using Electrs, Dojo allows you to connect your compatible software wallet directly to your RoninDojo node. Wallets like Samourai Wallet and Sentinel offer this functionality.

To establish the connection, you will just need to scan the QR code of your Dojo. To access this QR code via RoninUI, navigate to:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
To link your Samourai Wallet to your Dojo, simply scan this QR code during the app installation:

![Samourai Wallet connection](assets/notext/36.webp)

If you already had a Samourai Wallet before setting up your Ronin Dojo, it is necessary to back up your wallet, uninstall and then reinstall the Samourai Wallet app, before restoring your wallet. Upon launching the reinstalled app, you will have the option to connect to a new Dojo. **Be careful, this process carries the risk of losing your bitcoins if not executed correctly!** Make sure you have the backup of your Samourai wallet in your files and verify the validity of your passphrase via `Settings > Troubleshoot > Passphrase`. It is also important to have a readable backup of your recovery phrase and your passphrase. For more precision in this operation, it is recommended to follow this detailed tutorial: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).

### Using your own Mempool.space block explorer
A block explorer transforms the raw information from the Bitcoin blockchain into a structured and easily readable format. With tools like *Mempool.space*, it is possible to analyze transactions, search for specific addresses, or even consult the average fee rates of the network's mempools in real-time.

However, using online block explorers poses risks to your privacy and involves trust in the data provided by third parties. Indeed, by using these services without going through your own node, you could inadvertently disclose information about your transactions and must rely on the accuracy of the information presented by the site owner.
To mitigate these risks, it is recommended to use your own instance of *Mempool.space* via the Tor network, directly hosted on your node. This solution ensures the preservation of your privacy and the autonomy of your data.
To do this, start by installing *Mempool Space Visualizer* from RoninUI. On the web interface, go to the `Dashboard` tab and click on `Manage` below `Mempool Space`:
`Dashboard > Mempool Space > Manage`
![Manage mempool](assets/notext/37.webp)
Then click on the `Install Mempool visualizer` button:
![install mempool](assets/notext/38.webp)
Confirm your user password:
![password mempool](assets/notext/39.webp)
Wait for the installation to complete, then click again on the `Manage` button:
![Mempool Manage](assets/notext/40.webp)
You will obtain a `.onion` link to access your own instance of *Mempool.space* via the Tor network.
![Mempool link](assets/notext/41.webp)
I advise you to save this link in your favorites on the Tor browser or add it to the Tor Browser app on your smartphone for easy and secure access from anywhere. If you do not yet have the Tor browser, you can download it here: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Using Whirlpool to mix your bitcoins
Your RoninDojo node also integrates _WhirlpoolCLI_, a command-line interface that enables the automation of Whirlpool coinjoins, and _WhirlpoolGUI_, a graphical interface designed to interact with _WhirlpoolCLI_.

Performing a coinjoin via Whirlpool requires that the application used be active to carry out remixes. This condition can be restrictive for those wishing to achieve high levels of anonsets. Indeed, the device hosting the application integrating Whirlpool must remain on continuously. This means that to participate in remixes 24 hours a day, your computer or smartphone must stay turned on with Samourai or Sparrow open continuously. A solution to this constraint is to use _WhirlpoolCLI_ on a machine that is always on, such as a Bitcoin node, allowing your coins to remix without interruption, and without the need to keep another device turned on.

A detailed tutorial is in preparation to guide you step by step through the process of coinjoining with Samourai Wallet and RoninDojo v2, from A to Z.

For a deeper understanding of coinjoin and its use on Bitcoin, I also invite you to consult this other article: Understanding and using coinjoin on Bitcoin, where I detail everything you need to know about this technique.

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
### Using Whirlpool Stat Tool (WST)

After performing coinjoins with Whirlpool, it's useful to precisely evaluate the privacy level achieved for your mixed UTXOs. To do this, you can use the Python tool *Whirlpool Stat Tool*. This tool allows you to measure both the prospective and retrospective scores of your UTXOs, while analyzing their diffusion rate in the pool.

To deepen your understanding of the calculation mechanisms of these anonsets, I recommend reading the article: REMIX - WHIRLPOOL, which details the functioning of these indices.

https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



To access the WST tool, go to RoninCLI. To do this, open a terminal on your personal computer and establish an SSH connection with your node using the following command:
`SSH ronindojo@[IP]`

If, for example, your node's IP address is `192.168.1.40`, the appropriate command would be:
`SSH ronindojo@192.168.1.40`

If you changed your username during step 6, replacing the default username (`ronindojo`) with another, make sure to use this new name in the command. For example, if you chose `planb` as your username and the IP address is `192.168.1.40`, the command to enter would be:
`SSH planb@192.168.1.40`

You will be asked to enter the user password. Enter it and press `enter` to validate. You will then access the RoninCLI interface. Use the arrow keys on your keyboard to navigate to the `Samourai Toolkit` menu and press `enter` to select it:

![Samourai Toolkit](assets/notext/43.webp)

Then select `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Upon initializing WST, the tool will proceed with its automatic installation. Wait during this step. The usage instructions will scroll through. Once the installation is completed, press any key to access the WST terminal:

![WST commands](assets/notext/45.webp)

The following command prompt will be displayed:
`wst#/tmp>`

If you wish to exit this interface and return to the RoninCLI menu, simply enter:
`quit`

First, it's necessary to configure the proxy to use Tor, to ensure confidentiality when extracting data from OXT. Enter the command:
`socks5 127.0.0.1:9050`

Subsequently, proceed to download the pool information containing your transaction:
`download 0001`
Replace `0001` with the denomination code of the pool you are interested in. The denomination codes are as follows on WST:
- Pool 0.5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`

After downloading, load the data by replacing `0001` with your pool's code in this command: `load 0001`

![WST loading](assets/notext/46.webp)

Wait for the loading to complete, which may take a few minutes. Once the data is loaded, to know the anonset scores of your coin, execute the command `score` followed by your TXID (without the brackets):
`score [TXID]`

![WST score](assets/notext/47.webp)

WST will then display the retrospective score (_Backward-looking metrics_), followed by the prospective score (_Forward-looking metrics_). Besides the anonset scores, WST will also indicate the diffusion rate of your transaction within the pool, relative to its anonset.

**It is important to note that the prospective score of your coin should be calculated from the TXID of your initial mix, and not from your most recent mix. Conversely, the retrospective score of a UTXO is calculated from the TXID of the last cycle.**

### Using the Boltzmann Calculator
The Boltzmann calculator is a tool for analyzing a Bitcoin transaction, offering the ability to measure its level of entropy among other advanced metrics. These data provide a quantified assessment of the privacy of a transaction and help identify potential flaws. This tool is already integrated into your RoninDojo node, making it easy to access and use.

Before detailing the procedure for using the Boltzmann Calculator, it is important to understand the meaning of these indicators, their calculation method, and their utility. Although applicable to any Bitcoin transaction, these indicators are particularly useful for assessing the quality of a coinjoin transaction.

**The first indicator** that the software calculates is the total number of possible combinations, indicated under `nb combinations` in the tool. Based on the values of the UTXOs involved, this indicator quantifies the number of ways in which inputs can be associated with outputs. In other words, it determines the number of plausible interpretations a transaction can generate. For example, a coinjoin structured according to the Whirlpool 5x5 model presents `1496` possible combinations:
![combinations](assets/notext/50.webp)
Credit: KYCP

**The second indicator** calculated is the entropy of a transaction, designated by `Entropy`. When a transaction has a high number of possible combinations, it is often more relevant to refer to its entropy. This is defined as the binary logarithm of the number of possible combinations. Here is the formula used:
- $E$: the entropy of the transaction;
- $C$: the number of possible combinations for the transaction.
$$E = \log_2(C)$$

In mathematics, the binary logarithm (base 2 logarithm) corresponds to the inverse operation of raising 2 to a power. In other words, the binary logarithm of $x$ is the exponent to which 2 must be raised to obtain $x$. Therefore, this indicator is expressed in bits. Let's take the example of calculating the entropy for a coinjoin transaction structured according to the Whirlpool 5x5 model, which, as mentioned earlier, offers a number of possible combinations of `1496`:
$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bits}$$

Thus, this coinjoin transaction displays an entropy of 10.5469 bits, which is considered very satisfactory. The higher this value, the more different interpretations the transaction admits, thereby enhancing its level of privacy.

Let's take an additional example with a more conventional transaction, featuring one input and two outputs: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
In the case of this transaction, the only possible interpretation is: `(inp 0) > (Outp 0 ; Outp 1)`. Consequently, its entropy is established at `0`:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bits}$$
**The third indicator** provided by the Boltzmann Calculator is named `Wallet Efficiency`. This indicator assesses the efficiency of the transaction by comparing it to the optimal transaction conceivable in an identical setup. This leads us to discuss the concept of maximum entropy, which corresponds to the highest entropy a specific transaction structure can theoretically achieve. Thus, for a Whirlpool 5x5 coinjoin structure, the maximum entropy is set at `10.5469`. The transaction's efficiency is then calculated by confronting this maximum entropy with the actual entropy of the analyzed transaction. The formula used is as follows:
- $ER$: the actual entropy of the transaction, expressed in bits;
- $EM$: the maximum possible entropy for a given transaction structure, also in bits;
- $Ef$: the efficiency of the transaction, in bits.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bits}$$

This indicator is also expressed as a percentage, its formula is then:
- $CR$: the number of actual possible combinations;
- $CM$: the maximum number of possible combinations with the same structure;
- $Ef$: the efficiency expressed as a percentage.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

An efficiency of `100%` thus indicates that the transaction maximizes its potential for privacy based on its structure.

**The fourth indicator**, the entropy density, or `Entropy Density`, offers a perspective on the entropy relative to each input or output of the transaction. This indicator proves useful for evaluating and comparing the efficiency of transactions of different sizes. To calculate it, simply divide the total entropy of the transaction by the total number of inputs and outputs involved. Taking the example of a Whirlpool 5x5 coinjoin:
- $ED$: the entropy density expressed in bits;
- $E$: the entropy of the transaction expressed in bits;
- $T$: the total number of inputs and outputs in the transaction.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bits}$$
**The fifth piece of information** delivered by the Boltzmann Calculator is the table of matching probabilities between inputs and outputs. This table indicates, through the `Boltzmann score`, the probability that a specific input is connected to a given output. Taking the example of a Whirlpool coinjoin, the probability table would highlight the chances of linkage between each input and output, providing a quantitative measure of the ambiguity or predictability of associations in the transaction:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Here, it is clear that each input has an equal chance of being associated with any output, which reinforces the ambiguity and confidentiality of the transaction. However, in the case of a simple transaction with a single input and two outputs, the situation is different:

| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Here, we see that the probability for each output to come from input 0 is 100%. A lower probability thus translates to greater confidentiality, by diluting the direct links between inputs and outputs.

**The sixth piece of information** provided is the number of deterministic links, complemented by the ratio of these links. This indicator reveals how many connections between the inputs and outputs in the analyzed transaction are indisputable, with a 100% probability. The ratio, in turn, offers a perspective on the weight of these deterministic links within the total links of the transaction.

For example, a Whirlpool-type coinjoin transaction presents no deterministic links, and therefore displays an indicator and ratio of 0%. On the other hand, in our second examined transaction (with one input and two outputs), the indicator is set at 2 and the ratio reaches 100%. Thus, a null indicator signals excellent confidentiality thanks to the absence of direct and indisputable links between inputs and outputs.

**How to access the Boltzmann Calculator on RoninDojo?**
To access the *Boltzmann Calculator* tool, go to RoninCLI. To do this, open a terminal on your personal computer and establish an SSH connection with your node using the following command: `SSH ronindojo@[IP]`

If, for example, your node's IP address is `192.168.1.40`, the appropriate command would be:
`SSH ronindojo@192.168.1.40`

If you changed your username during step 6, replacing the default username (`ronindojo`) with another, make sure to use this new name in the command. For example, if you chose `planb` as your username and the IP address is `192.168.1.40`, the command to enter would be:
`SSH planb@192.168.1.40`

You will be asked to enter the user password. Enter it and then press `enter` to validate. You will then access the RoninCLI interface. Use the arrows on your keyboard to navigate to the `Samourai Toolkit` menu and press `enter` to select it:

![Samourai Toolkit](assets/notext/43.webp)

Then select `Boltzmann Calculator`:

![boltzmann](assets/notext/49.webp)

You will arrive at the software's home page:

![boltzmann home](assets/notext/51.webp)

Enter the TXID of the transaction you wish to study and press the `enter` key:

![boltzmann txid](assets/notext/52.webp)

The calculator then provides you with all the indicators we have previously discussed:

![boltzmann result](assets/notext/53.webp)

### Other features of your RoninDojo v2
Your RoninDojo node integrates various other features. In particular, you have the ability to scan specific information to take it into account. For example, sometimes your Samourai wallet, connected to RoninDojo, may not display the bitcoins you actually hold. If the balance indicates 0 while you are certain to have bitcoins in this wallet, several reasons can explain this situation, such as an error in the derivation paths. But one of the causes can also be that your node is not properly monitoring your addresses. To solve this problem, you can ensure that your node is indeed following your `xpub` using the _xpub tool_. To access this tool via RoninUI, follow the path:
`Maintenance > XPUB Tool`

Enter the `xpub` that is causing the problem and click on the `Check` button to verify this information:
![xpub tool](assets/notext/54.webp)
Ensure that all transactions are properly listed. It is also important to verify that the derivation type used matches that of your wallet. If this is not the case, click on `Retype`, then choose from `BIP44`, `BIP49`, or `BIP84` according to your needs.
Beyond this tool, the `Maintenance` tab of RoninUI is full of other useful features:
- *Transaction Tool*: Allows examining the details of a given transaction;
- *Address Tool*: Allows confirming the tracking of a given address by your Dojo;
- *Rescan Blocks*: Forces your node to perform a new scan of a specified block range.

The `Push Tx` tab is another interesting feature of RoninUI, which enables the broadcasting of a signed transaction on the Bitcoin network. The transaction must be entered in hexadecimal form.

Regarding the other tabs available on your RoninUI dashboard:
- `Apps`: Hosts the Whirlpool application, and will surely be used to integrate new applications in the future;
- `Logs`: Offers real-time access to the event logs of your software;
- `System Info`: Provides general information about your node, such as CPU temperature, storage space usage, or RAM data. You will also find the `Reboot` and `Shut down` options to restart or turn off your node;
- `Settings`: Allows you to change your user password.

There you have it! Thank you for following this tutorial to the end. If you enjoyed it, I encourage you to share it on social media. Furthermore, if you have the opportunity, consider supporting the developers who make these free and open-source software available to our community with a donation: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). To deepen your knowledge of RoninDojo and discover more resources, I highly recommend consulting the links to the external resources mentioned below.

**External resources:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)
