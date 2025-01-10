---
name: RoninDojo

description: Installing and using your RoninDojo Bitcoin node.
---
***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, certain features of RoninDojo, such as Whirlpool, are no longer operational. However, it is possible that these tools could be reinstated or relaunched differently in the coming weeks. Additionally, since the RoninDojo code was hosted on Samourai's GitLab, which was also seized, it is currently not possible to download the code remotely. The RoninDojo teams are likely working on republishing the code.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

_This tutorial is dedicated to the installation of RoninDojo v1. To take advantage of the latest improvements and features, I strongly recommend consulting our tutorial dedicated to the direct installation of RoninDojo v2 on your Raspberry Pi:_
https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Running and using your own node is essential to truly participate in the Bitcoin network. While running a Bitcoin node does not bring any financial benefits to the user, it allows them to preserve their privacy, act independently, and have control over their trust in the network.

In this article, we will take a detailed look at RoninDojo, a great solution for running your own Bitcoin node.

### Table of Contents:

- What is RoninDojo?
- What hardware to choose?
- How to install RoninDojo?
- How to use RoninDojo?
- Conclusion

If you are not familiar with how a Bitcoin node works and its role, I recommend starting by reading this article: The Bitcoin Node - Part 1/2: Technical Concepts.

![Samourai](assets/1.webp)

## What is RoninDojo?

Dojo is a full Bitcoin node server developed by the Samourai Wallet team. You can freely install it on any machine.

RoninDojo is an installation assistant and administration tool for Dojo and various other tools. RoninDojo takes the original implementation of Dojo and adds many other tools to it, while also making installation and management easier.

They also offer a "plug-and-play" hardware, the RoninDojo Tanto, with RoninDojo pre-installed on a machine assembled by their team. The Tanto is a paid solution, suitable for those who do not want to get their hands dirty.

The code for RoninDojo is open-source, so it is also possible to install this solution on your own hardware. This option is cost-effective but requires a bit more manipulation, which is what we will do in this article.

RoninDojo is a Dojo, so it allows for easy integration of Whirlpool CLI into your Bitcoin node to have the best possible CoinJoin experience. With Whirlpool CLI, not only can you let your bitcoins remix 24/7 without needing to keep your personal computer on, but you can also greatly improve your privacy.

RoninDojo integrates many other tools that rely on your Dojo, such as the Boltzmann calculator, which determines the privacy level of a transaction, the Electrum server to connect your different Bitcoin wallets to your node, or the Mempool server to privately observe your transactions.
Compared to another node solution like Umbrel, which I presented to you in this article, RoninDojo is deeply focused on "On Chain" solutions and tools that optimize user privacy. Therefore, RoninDojo does not allow interaction with the Lightning Network.
RoninDojo offers fewer tools compared to Umbrel, but the few essential features for a Bitcoiner present on Ronin are incredibly stable.

So if you don't need all the features of an Umbrel server and only want a simple and stable node with a few essential tools like Whirlpool or Mempool, then RoninDojo is probably a good solution for you.

In my opinion, Umbrel's development focus is heavily on the Lightning Network and versatile tools. It is still a Bitcoin node, but the aim is to make it a multitasking mini-server. In contrast, RoninDojo's development focus is more aligned with the teams at Samourai Wallet and focuses on the essential tools for a Bitcoiner, allowing for full independence and optimized management of privacy on Bitcoin.

Please note that setting up a RoninDojo node is slightly more complex than an Umbrel node.

Now that we have been able to paint a picture of RoninDojo, let's see how to set up this node together.

## What hardware to choose?

To choose the machine that hosts and runs RoninDojo, you have several options.

As explained earlier, the simplest choice is to order the Tanto, a plug-and-play machine designed specifically for this purpose. To order yours, go here: [link](https://shop.ronindojo.io/product-category/nodes/).

Since the RoninDojo teams produce open-source code, it is also possible to implement RoninDojo on other machines. You can find the latest versions of the installation wizard on this page: [link](https://ronindojo.io/en/downloads.html), and the latest versions of the code on this page: [link](https://code.samourai.io/ronindojo/RoninDojo).

Personally, I installed it on a Raspberry Pi 4 8GB and everything works perfectly.

However, please note that the RoninDojo teams indicate that there are often problems with the case and SSD adapter. It is therefore not recommended to use a case with a cable for your machine's SSD. Instead, it is preferable to use a storage expansion card specifically designed for your motherboard, such as this one: Raspberry Pi 4 Storage Expansion Card.

Here is an example of how to set up your own RoninDojo node:

- A Raspberry Pi 4.
- A case with a fan.
- A compatible storage expansion card.
- A power cable.
- An industrial micro SD card of 16GB or more.
- A 1TB or larger SSD.
- An RJ45 Ethernet cable, category 8 recommended.

## How to Install RoninDojo?

### Step 1: Prepare the bootable micro SD card.

Once you have assembled your machine, you can begin the installation of RoninDojo. To do this, start by creating a bootable micro SD card by burning the appropriate disk image onto it.

Insert your micro SD card into your personal computer, then go to the official RoninDojo website to download the RoninOS disk image: https://ronindojo.io/en/downloads.html.

Download the disk image that corresponds to your hardware. In my case, I downloaded the "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" image:

![Download RoninOS disk image](assets/2.webp)

Once the image is downloaded, verify its integrity using the corresponding .SHA256 file. I will describe in detail how to do this in this article: How to verify the integrity of Bitcoin software on Windows?

Specific instructions for verifying the integrity of RoninOS are also available on this page: https://wiki.ronindojo.io/en/extras/verify.

To burn this image onto your micro SD card, you can use software such as Balena Etcher, which you can download here: https://www.balena.io/etcher/.

To do this, select the image in Etcher and flash it onto the micro SD card:

![Burn disk image with Etcher](assets/3.webp)

Once the operation is complete, you can insert the bootable micro SD card into the Raspberry Pi and power on the machine.

### Step 2: Configure RoninOS.

RoninOS is the operating system of your RoninDojo node. It is a modified version of Manjaro, a Linux distribution. After starting your machine and waiting a few minutes, you can begin its configuration.

To remotely connect to it, you will need to find the IP address of your RoninDojo machine. To do this, you can, for example, connect to the administration panel of your internet box, or you can also download software such as https://angryip.org/ to scan your local network and find the machine's IP.

Once you have found the IP, you can take control of your machine from another computer connected to the same local network using SSH.

From a computer running macOS or Linux, simply open the terminal. From a computer running Windows, you can use a specialized tool like Putty or directly use Windows PowerShell.

Once the terminal is open, type the following command:
```
ssh root@192.168.?.?
```

Simply replace the two question marks with the IP of your previously found RoninDojo.
Tip: In a Shell, right-click to paste an item.

Next, you will arrive at the Manjaro control panel. Choose the correct keyboard layout using the arrows to change the target in the dropdown list.

![Manjaro Keyboard Configuration](assets/4.webp)

Choose a username and password for your session. Use a strong password and make a safe backup. You can optionally use a weak password during installation, and later easily change it by "copy-pasting" it into RoninUI. This will allow you to use a very strong password without spending too much time manually typing it during the setup of Manjaro.

![Manjaro Username Configuration](assets/5.webp)

Next, you will also be asked to choose a root password. For the root password, enter a strong password directly. You will not be able to change it from RoninUI. Also, remember to securely backup this root password.

Then enter your location and time zone.

![Manjaro Time Zone Configuration](assets/6.webp)

![Manjaro Location Configuration](assets/7.webp)

Next, choose a hostname.

![Manjaro Hostname Configuration](assets/8.webp)

Finally, verify the Manjaro configuration information and confirm.

![Verification of ManjaroOS Configuration Information](assets/9.webp)

### Step 3: Download RoninDojo.

The initial configuration of RoninOS will be done. Once finished, as shown in the screenshot above, the machine will restart. Wait a few moments, then enter the following command to reconnect to your RoninDojo machine:
```
ssh username@192.168.?.?
```

Simply replace "username" with the username you previously chose, and replace the question marks with the IP of your RoninDojo.

Then enter your user password.

In the terminal, it will look like this:

![SSH Connection to RoninOS](assets/10.webp)

You are now connected to your machine, which currently only has RoninOS. Now you need to install RoninDojo on it.

Download the latest version of RoninDojo by entering the following command:
```
git clone https://code.samourai.io/ronindojo/RoninDojo
```

The download will be quick. In the terminal, you will see this:

![Cloning RoninDojo](assets/11.webp)

Wait for the download to finish, then install and access the RoninDojo user interface using the following command:
```
~/RoninDojo/ronin
```

You will be asked to enter your user password:

![Bitcoin Node Password Verification](assets/12.webp)

This command is only necessary the first time you access your RoninDojo. Afterwards, to access RoninCLI via SSH, you will simply need to enter the command [SSH username@192.168.?.?] replacing "username" with your username and entering the IP address of your node. You will be prompted for your user password.

Next, you will see this magnificent animation:

![RoninCLI launch animation](assets/13.webp)

Then you will finally arrive at the RoninDojo CLI user interface.

### Step 4: Install RoninDojo.

From the main menu, navigate to the "System" menu using the arrow keys on your keyboard. Press the enter key to confirm your choice.

![RoninCLI navigation menu to System](assets/14.webp)

Then go to the "System Setup & Install" menu.

![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)

Finally, check "System Setup" and "Install RoninDojo" using the space bar, then select "Accept" to start the installation.

![RoninDojo installation confirmation](assets/16.webp)

Let the installation proceed quietly. In my case, it took about 2 hours. Keep your terminal open during the process.

Occasionally check your terminal, as you will be asked to press a key at certain stages of the installation, like here for example:

![RoninDojo installation in progress](assets/17.webp)

At the end of the installation, you will see the different containers start:

![Node container startup](assets/18.webp)

Then your node will restart. Connect again to RoninCLI for the next step.

![Bitcoin node restart](assets/19.webp)

### Step 5: Download the proof-of-work chain and access RoninUI.

Once the installation is complete, your node will start downloading the Bitcoin proof-of-work chain. This is called the Initial Block Download (IBD). It usually takes between 2 and 14 days depending on your internet connection and device.

You can track the progress of the chain download by accessing the RoninUI web interface.

To access it from a local network, type the following in your browser's address bar:

- Either directly enter the IP address of your machine (192.168.?.?)
- Or enter: ronindojo.local

Remember to disable your VPN if you are using one.

### Possible twist

If you are unable to connect to RoninUI from your browser, check the proper functioning of the application from your Terminal connected to your node via SSH. Connect to the main menu by following the previous steps:

- Type: SSH username@192.168.?.? replacing with your credentials.

- Enter your user password.

Once on the main menu, go to: **RoninUI > Restart**

If the application restarts correctly, it is a problem with the connection from your browser. Check that you are not using a VPN and make sure you are connected to the same network as your node.

If the restart produces an error, try updating the operating system and then reinstalling RoninUI. To update the OS: **System > Software Updates > Update Operating System**

Once the update and restart are complete, reconnect to your node via SSH and reinstall RoninUI: **RoninUI > Re-install**

After downloading RoninUI again, try connecting to RoninUI through your browser.

**Tip:** If you accidentally exit RoninCLI and find yourself on the Manjaro terminal, simply enter the command "ronin" to return directly to the main menu of RoninCLI.

### Web log in

You can also log in to the RoninUI web interface from any network using Tor. To do this, retrieve the Tor address of your RoninUI from RoninCLI: **Credentials > Ronin UI**

Retrieve the Tor address ending in .onion and then log in to Ronin UI by entering this address in your Tor browser. Be careful not to leak your various credentials, as they are sensitive information.

![RoninUI web login interface](assets/20.webp)

Once logged in, you will be asked for your user password. It is the same password you use to log in via SSH.

![RoninUI web interface management panel](assets/21.webp)

We can see the progress of the IBD (Initial Block Download) here. Be patient, you are retrieving all the transactions made on Bitcoin since January 3, 2009.

After downloading the entire blockchain, the indexer will compact the database. This operation takes about 12 hours. You can also track its progress under "Indexer" on RoninUI.

Your RoninDojo node will be fully functional after this:

![Indexer synchronized at 100% functional node](assets/22.webp)

If you want to change the user password to a stronger one, you can do so now from the "Settings" tab. On RoninDojo, there is no additional security layer, so I recommend choosing a truly strong password and taking care of its backup.

## How to use RoninDojo?

Once the chain is downloaded and compacted, you can start enjoying the services offered by your new RoninDojo node. Let's see how to use them.

### Connecting wallet software to electrs.

The first utility of your newly installed and synchronized node will be to broadcast your transactions to the Bitcoin network. Therefore, you will likely want to connect your different wallet management software to it.

You can do this using Electrum Rust Server (electrs). The application is normally pre-installed on your RoninDojo node. If not, you can manually install it from the RoninCLI interface.

Simply go to: **Applications > Manage Applications > Install Electrum Server**

To obtain the Tor address of your Electrum Server, from the RoninCLI menu, go to:
**Credentials > Electrs**

You just have to enter the .onion link in your wallet software. For example, in Sparrow Wallet, go to the tab:
**File > Preferences > Server**

In the server type, select `Private Electrum`, then enter the Tor address of your Electrum Server in the corresponding field. Finally, click on "Test Connection" to test and save your connection.

![Sparrow Wallet connection interface to an electrs](assets/23.webp)

### Connecting wallet software to Samourai Dojo.

Instead of using Electrs, you can also use Samourai Dojo to connect your compatible software wallet to your RoninDojo node. For example, Samourai Wallet offers this option.

To do this, simply scan the connection QR code of your Dojo. To access it from RoninUI, click on the "Dashboard" tab and then on the "Manage" button in the box of your Dojo. You will then be able to see the connection QR codes for your Dojo and BTC-RPC Explorer. To display them, click on "Display values".

![Retrieving the connection QR code to Dojo](assets/24.webp)

To connect your Samourai Wallet to your Dojo, you will need to scan this QR code during the application installation:

![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)

### Using your own Mempool Explorer.

An essential tool for Bitcoiners, the explorer allows you to check various information about the Bitcoin chain. With Mempool, for example, you can check in real-time the fees applied by other users in order to adjust yours accordingly. You can also check the confirmation status of one of your transactions or view the balance of an address.

These explorer tools can expose you to privacy risks and require you to trust a third-party's database. When you use this online tool without going through your own node:

- You risk leaking information about your wallet.

- You trust the website manager for the proof-of-work chain they host.

To avoid these risks, you can use your own Mempool instance on your node via the Tor network. With this solution, not only do you preserve your privacy when using the service, but you also no longer need to trust a provider since you query your own database.

To do this, start by installing Mempool Space Visualizer from RoninCLI:

**Applications > Manage Applications > Install Mempool Space Visualizer**

Once installed, retrieve the link to your Mempool. The Tor address will allow you to access it from any network. Similarly, we retrieve this link via RoninCLI:

**Credentials > Mempool**

![Retrieve Tor Mempool address](assets/26.webp)

Simply enter your Mempool Tor address in the Tor browser to enjoy your own Mempool instance, based on your own data. I recommend adding this Tor address to your favorites for quicker access. You can also create a shortcut on your desktop.

![Mempool Space interface](assets/27.webp)

If you don't have the Tor browser yet, you can download it here: https://www.torproject.org/download/

You can also access it from your smartphone by installing Tor Browser and entering the same address. From anywhere, you can view the state of the Bitcoin chain using your own node.

### Using Whirlpool CLI.

Your RoninDojo node also includes WhirlpoolCLI, a remote command-line interface for automating Whirlpool mixes.

When you perform a CoinJoin with the Whirlpool implementation, the application you are using must remain open in order to execute mixes and remixes. This process can be tedious for users who want to have high anon sets, as the device hosting the application with Whirlpool must constantly remain on. In practical terms, this means that if you want to engage your UTXOs in 24/7 remixes, you will need to keep your personal computer or phone constantly on with the application open.

One solution to this constraint is to use WhirlpoolCLI on a machine that is intended to be constantly on, such as a Bitcoin node. With this, our UTXOs can be remixed 24/7 without the need to keep another machine other than our Bitcoin node running.
WhirlpoolCLI is used with WhirlpoolGUI, a graphical interface to be installed on a personal computer for easy management of Coinjoins. I will explain in detail how to set up Whirlpool CLI with your own dojo in this article: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

To learn more about Coinjoin in general, I explain everything in this article: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Using Whirlpool Stat Tool.

After performing CoinJoins with Whirlpool, you may want to know the actual level of privacy of your mixed UTXOs. Whirlpool Stat Tool allows you to easily do this. With this tool, you can calculate the prospective score and the retrospective score of your mixed UTXOs. To learn more about calculating these Anon Sets and how they work, I recommend reading this section: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

The tool is pre-installed on your RoninDojo. For now, it is only available from RoninCLI. To launch it from the main menu, go to:
**Samourai Toolkit > Whirlpool Stat Tool**

The instructions for use will appear. Once finished, press any key to access the command lines:

![Whirlpool Stats Tool software home](assets/28.webp)

The terminal will display:
**wst#/tmp>**

To exit this interface and return to the RoninCLI menu, simply enter the command:
```
quit
```

To start, we will set the proxy on Tor in order to extract OXT data with complete privacy. Enter the command:
```
socks5 127.0.0.1:9050
```

Then download the data from the pool that contains your transaction:
```
download 0001
```

**Note:** replace `0001` with the pool denomination code that interests you.

The denomination codes are as follows on WST:

- Pool 0.5 bitcoins: 05
- Pool 0.05 bitcoins: 005
- Pool 0.01 bitcoins: 001
- Pool 0.001 bitcoins: 0001

![Downloading data from pool 0001 from OXT](assets/29.webp)

Once the data is downloaded, load it with the command:
```
load 0001
```

**Note:** replace `0001` with the pool denomination code that interests you.

![Loading data from pool 0001](assets/30.webp)
Let the loading process take place, it may take a few minutes. After loading the data, type the score command followed by your TXID (transaction identifier) to obtain its Anon Sets:
```
score TXID
```

**Note:** replace `TXID` with the identifier of your transaction.

![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)

WST will then display the retrospective score (Backward-looking metrics) followed by the prospective score (Forward-looking metrics). In addition to the scores of the Anon Sets, WST also provides you with the diffusion rate of your output in the pool based on the anon set.

Please note that the prospective score of your UTXO is calculated based on the TXID of your initial mix, not your last mix. Conversely, the retrospective score of a UTXO is calculated based on the TXID of the last cycle.

Once again, if you do not understand these concepts of Anon Sets, I recommend reading this part of my article on Coinjoin where I explain everything in detail with diagrams: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Using the Boltzmann calculator.

The Boltzmann calculator is a tool that allows you to easily calculate various advanced metrics on a Bitcoin transaction, including its entropy level. All this data will allow you to quantify the level of privacy of a transaction and detect any potential errors. This tool is pre-installed on your RoninDojo node.

To access it from RoninCLI, connect via SSH, then go to the menu:
**Samourai Toolkit > Boltzmann Calculator**

Before explaining how to use it on RoninDojo, I will explain what these metrics represent, how they are calculated, and what they are used for.

These indicators can be used for any Bitcoin transaction, but they are particularly interesting for studying the quality of a Coinjoin transaction.

1. The first indicator calculated by this software is the number of possible combinations. It is noted on the calculator as "nb combinations". Given the values of the UTXOs, this indicator represents the number of possible mappings from inputs to outputs.

**note:** if you are not familiar with the term `UTXO`, I recommend reading this short article:

> Mechanism of a Bitcoin transaction: UTXO, inputs, and outputs.

In other words, this indicator represents the number of possible interpretations for a given transaction. For example, a Whirlpool 5x5 Coinjoin structure will have a number of possible combinations equal to 1496:

![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)

Credit: KYCP

2. The second calculated indicator is the entropy of a transaction. Since the number of possible combinations can be very high for a transaction, one can choose to use entropy instead. Entropy represents the binary logarithm of the number of possible combinations. Its formula is as follows:

- E: entropy of the transaction.
- C: number of possible combinations for the transaction.

**E = log2(C)**

In mathematics, the binary logarithm (base 2) is the inverse function of the power of 2 function. In other words, the binary logarithm of x is the power to which the number 2 must be raised to obtain the value x.

Thus:

**E = log2(C)**

**C = 2^E**

This indicator is expressed in bits. For example, here is the calculation of the entropy of a Whirlpool 5x5 Coinjoin transaction, with a previously mentioned number of possible combinations equal to 1496:

**C = 1496**

**E = log2(1496)**

**E = 10.5469 bits**

Therefore, this Coinjoin transaction has an entropy of 10.5469 bits, which is very good.

The higher this indicator is, the more different interpretations of the transaction there are, and therefore the more confidential the transaction is.

Let's take another example. Here is a "classic" transaction that has one input and two outputs:

![Bitcoin transaction schema on oxt.me](assets/34.webp)

Credit: OXT

This transaction has only one possible interpretation:

**[(inp 0) > (Outp 0 ; Outp 1)]**

So its entropy will be equal to 0:

**C = 1**,
**E = log2(C)**,
**E = 0**

3. The third indicator returned by the Boltzmann calculator is the efficiency of the Tx called "Wallet Efficiency". This indicator simply allows comparing the input transaction with the best possible transaction in the same configuration.

We will now introduce the concept of maximum entropy, which represents the highest attainable entropy for a given transaction structure. For example, a Whirlpool 5x5 Coinjoin structure will have a maximum entropy of 10.5469. The efficiency indicator compares this maximum entropy with the actual entropy of the input transaction. Its formula is as follows:

- ER: Actual entropy expressed in bits.
- EM: Maximum entropy with the same structure expressed in bits.
- Ef: Efficiency expressed in bits.

**Ef = ER - EM**

**Ef = 10.5469 - 10.5469**

**Ef = 0 bits**

This indicator is also expressed as a percentage, so the formula becomes:

- CR: Actual number of possible combinations.
- CM: Maximum number of possible combinations with the same structure.
- Ef: Efficiency expressed as a percentage.

**Ef = CR/CM**

**Ef = 1496/1496**

**Ef = 100%**

An efficiency of 100% means that this transaction has the highest possible privacy relative to its structure.

4. The fourth calculated indicator is entropy density. It allows us to relate the entropy to each input or output. This indicator can be used to compare the efficiency between transactions of different sizes.

Its calculation is very simple: we divide the transaction's entropy by the number of inputs and outputs present. For example, for a Whirlpool 5x5 Coinjoin, we would have:

    ED: Entropy density expressed in bits.
    E: Transaction entropy expressed in bits.
    T: Total number of inputs and outputs in the transaction.

T = 5 + 5 = 10
ED = E / T
ED = 10.5469 / 10
ED = 1.054 bits

The fifth piece of information provided by the Boltzmann calculator is the probability table of links between inputs and outputs. This table simply gives you the probability (Boltzmann score) that a given input corresponds to a given output.

If we take our example with a Whirlpool Coinjoin, the probability table would be:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Here we can see that each input has an equal probability of being linked to each output.

However, if we take the example of a transaction with one input and two outputs, it would look like this:

| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

In this example, we can see that the probability of each output coming from input 0 is 100%.

The lower this probability, the higher the level of confidentiality.

6. The sixth piece of information that is calculated is the number of deterministic links. The ratio of deterministic links will also be provided. This indicator highlights the number of links between inputs and outputs of the given transaction that have a probability of 100%, meaning they are undeniable.

The ratio indicates the number of deterministic links in the transaction compared to the total number of links.

For example, a Coinjoin Whirlpool transaction has no deterministic links between inputs and outputs. The indicator will be zero and the ratio will also be 0%.

However, for the second transaction studied (1 input and 2 outputs), the indicator is 2 and the ratio is 100%.

Therefore, if this indicator is zero, it indicates good confidentiality.

Now that we have studied the indicators, let's see how to calculate them using this software. From RoninCLI, go to the menu:
**Samourai Toolkit > Boltzmann Calculator**

![Boltzmann Calculator software homepage](assets/35.webp)

Once the software is launched, enter the transaction ID you want to study. You can enter multiple transactions at once by separating them with a comma, then press enter:

![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)

The calculator will then return all the indicators we have seen before:

![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)

Type the command "Quit" to exit the software and return to the RoninCLI menu.

To learn more about the Boltzmann calculator, I recommend reading these articles:

- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf

### Connecting Bisq.

Bisq is a peer-to-peer exchange platform that allows you to buy and sell bitcoins. It is used with a desktop software that runs on Tor and allows you to exchange bitcoins without needing to provide your identity.
Bisq secures peer-to-peer exchanges through a 2/2 multi-signature system. You can use this software with your own RoninDojo node to optimize the privacy of your exchanges and trust the data from your own node's blockchain.

To download the Bisq software, go to their official website: https://bisq.network/

To get started with the software, I recommend reading this page: https://bisq.network/getting-started/

To retrieve the connection link from your RoninDojo, you will need to connect to RoninCLI via SSH. Then go to the menu:
**Applications > Manage Applications**

Enter your password, then check the box with the space key:
**[ ] Enable Bisq Connection**

Confirm your choice. Let your node install, then retrieve the Tor V3 address from:
**Credentials > Bitcoind**

Copy the address under "Bitcoin Daemon".

You can also retrieve your Bitcoind Tor V3 address from the RoninUI interface by simply clicking on "Manage" in the "Bitcoin Core" box on the "Dashboard":

![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)

To connect your node from Bisq, go to the menu:
**Settings > Network Info**

![Access the node connection interface from the Bisq software](assets/39.webp)

Click on the bubble "Use custom Bitcoin Core nodes". Then enter your Bitcoin TorV3 address in the designated box, with the ".onion" but without the "http://".

![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)

Restart the Bisq software. Your node is now connected to your Bisq.

### Other features.

Your RoninDojo node also includes other basic features. You have the ability to scan specific information to ensure that it is taken into account.

For example, it is sometimes possible that your wallet connected to your RoninDojo does not find the bitcoins that belong to you. The balance is 0 even though you are sure that you have bitcoin in this wallet. There are many possible causes to consider, including an error in the derivation paths, and among them, it is also possible that your node is not observing your addresses.

To fix this, you can check that your node is tracking your xpub with the "xpub tool". To access it from RoninUI, go to the menu:
**Maintenance > XPUB Tool**

Enter the problematic xpub and click "Check" to verify this information.

![XPUB Tool from RoninUI](assets/41.webp)

If your xpub is being tracked by the node, you will see this appear:

![XPUB Tool result showing successful analysis](assets/42.webp)

Check that all transactions appear correctly. Also, verify that the derivation type matches that of your wallet. Here we can see that the node interprets this xpub as a BIP44 derivation. If this derivation type does not match that of your wallet, click on the "Retype" button, then select BIP44/BIP49/BIP84 according to your choice:

![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)

If your xpub is not tracked by your node, you will see this screen inviting you to import it:

![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)

You can also use other maintenance tools:

- Transaction Tool: Allows you to observe the details of a specific transaction.
- Address Tool: Allows you to verify that a specific address is being tracked by your Dojo.
- Rescan Blocks: Forces your node to rescan a selected range of blocks.

You will also find the "Push Tx" tool on RoninUI. It allows you to broadcast a signed transaction to the Bitcoin network. It must be entered in hexadecimal format:

![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)

## Conclusion.

We have seen how to install and get started with this wonderful tool that is RoninDojo. It is an excellent choice for running your own Bitcoin node. It is a stable solution that integrates and keeps up to date all the essential tools for a Bitcoiner.

If using the terminal does not scare you and if you do not need tools related to the Lightning Network, then RoninDojo may appeal to you.

If you can, consider donating to the developers who freely produce these open-source software for you: https://donate.ronindojo.io/

To learn more about RoninDojo, I recommend checking out the links in my external resources below.

### Further reading:

- Understanding and using CoinJoin on Bitcoin.
- Hash functions - excerpt from the ebook Bitcoin Démocratisé 1.
- Everything you need to know about the Bitcoin Passphrase.

### External resources:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/

