---
name: Electrum

description: Full Electrum Guide, from 0 to hero
---

![cover](assets/cover.webp)

Find below a few description sources for Electrum:

- [X](https://twitter.com/ElectrumWallet)
- [Electrum website](https://electrum.org/)
- [Electrum documentation](https://electrum.readthedocs.io/)

Here is what Rogzy thinks about this tutorial:

> I have to say, when i came across this guide i was shocked. Congrats on Arman the Parman for this. It would have been ashame not to host in here and translate it on as many language as possible. Honeslty, tips that dude.

The original post are the following:

![Electrum Desktop Wallet (Mac / Linux) - download, verify, connect to your node.](https://youtu.be/wHmQNcRWdHM)

![Making a Bitcoin transaction with Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Why Electrum?

This is a detailed guide on how to use the Electrum Bitcoin Wallet, with solutions to all its traps and quirks -something I’ve developed after several years of use, and teaching students about Bitcoin security/privacy. Electrum is not the best Bitcoin wallet for the person who wants to keep everything as simple as possible, and preferring to remain at the beginner level. Instead, it’s for the person who is, or aspires to be, a “power” user.

For the new Bitcoiner, it is excellent only if under the supervision of an experienced user to show them the way. If learning to use it alone, it would be safe provided they take their time and use it in a testing environment with only a small number of sats at first. This guide supports that endeavour, but it is also a good reference for anyone else.

**Warning:** this guide is big. Don’t try to do all this in one day. It’s best to save the guide and chip away over time.

## Downloading Electrum

Ideally, use a dedicated Bitcoin computer for your Bitcoin transactions (My guide for this https://armantheparman.com/mint/) _(ALSO available on privacy section)_. It’s fine to practice with small amounts on a “dirty” computer when you’re first learning (who knows how much hidden malware your regular computer has accumulated over the years – you don’t want to expose your Bitcoin wallets to them).

Get Electrum from https://electrum.org/.

Click the Download tab at the top.

Click on the download link that corresponds to your computer. Any Linux or Mac computer can use the Python link (red circle). A Linux computer with an Intel or AMD chip can use the Appimage (green circle; this is like a Windows executable file). A Raspberry Pi device has an ARM microprocessor and can only use the Python version (red circle), not Appimage, even though Pi’s run Linux. The blue circle is for Windows and the Black circle is for Mac.

![image](assets/1.webp)

## Verifying Electrum

The purpose of “verifying” the download is to make sure not a single bit of data has been tampered with. It prevents you from using a “hacked” malicious version of the software. It’s fine to skip this provided you only use the downloaded copy for practicing, i.e. don’t use wallets that hold serious money. Then, once you are ready to use Electrum for your real funds, you should delete your copy and start over, this time verifying your download.

To do this, we use public/private key cryptography tools – gpg, which have written a guide about here (https://armantheparman.com/gpg/). The gpg tool comes with all Linux operating systems. For Mac and Windows, see the gpg link for download instructions.

In addition to downloading the Electrum software, for security, you also need the digital SIGNATURE of the software. This is a string of text (it’s actually a number encoded using text) that the developer produced with his PRIVATE gpg key. Using the gpg program, we can then “test” the SIGNATURE against his PUBLIC key (created from the developer’s private key) which everyone has access to, versus the download FILE.

In other words, with the three inputs (signature, public key, and data file), we get a true or false output to confirm that the file has not been tampered with.

To get the signature, click on the link corresponding to the file you downloaded (see coloured arrows):

![image](assets/2.webp)

Clicking on the link may automatically download the file to your downloads folder, or it may open in the browser. If it opens in the browser, you need to save the file. You can right-click and select “save as”. Depending on the operating system or browser, you may need to right-click on the white space area, not the text.

Below is what the downloaded text looks like. You can see there are multiple signatures – these are signatures by different people. You can verify each or any. I’ll be showing you how to verify just the developer’s.

![image](assets/3.webp)

Next, you need to get ThomasV’s public key – he is the main developer. You can get that directly from him, his Keybase account, Github, or someone else, from a keyserver, or from the Electrum website.

Getting it from the Electrum website is actually the least secure way, because if this website is nefarious (the very thing we are checking for) why are we getting a public key from it (the public key could be fake)?

To keep it simple for now, I’ll show you how to get it from the website anyway, but bear this in mind. Here is the copy (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ) on GitHub which you can compare it to.

Scroll down the page a little to find the link to ThomasV’s public key (red circle below). Click it and download it, or if it opens some text in a browser, right-click to save.

![image](assets/4.webp)

You now have 3 new files, probably all in the downloads folder. It doesn’t matter where they are, but it makes the process easier if you put them all in the same folder.

The three files:

1. The Electrum download
2. The signature file (usually it is the same file name as the Electrum download with a “.asc” addition
3. ThomasV’s public key.

Open a terminal in Mac or Linux, or command prompt (CMD) in Windows.

Navigate to the Downloads directory (or wherever you put the three files). If you have no idea what this means, learn from this short video for Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) and this one for Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Remember that on Linux computers, directory names are case-sensitive.

In the terminal, type this to import ThomasV’s public key into your computer’s “keyring” (the keyring is an abstract concept – it’s actually just a file on your computer):

```bash
gpg --import ThomasV.asc
```

Make sure the file name matches what you have downloaded. Also, notice it’s a double dash not a single dash. Also, note there is a space before and after “–import”. Then hit <enter>.

The file should import. If you get an error, check you are in the directory where the file actually exists. To check what directory you are in (on Mac or Linux), type pwd. To see what files are in the directory you’re in (on Mac or Linux), type ls. You should see the “ThomasV.asc” text file listed, possibly among other files.

Then we run the command to verify the signature.

```bash
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Notice there are 4 “elements” here, each separated by a space. I have bolded the text alternatively to help you see. The four elements are:

1. the gpg program
2. the –verify option
3. the filename of the signature
4. the filename of the program

Of interest, sometimes you can leave off the 4th element and the computer guesses what you mean. I’m not sure, but I believe it only works if the file names only differ by the “asc” at the end.

Don’t just copy the filenames that I have shown here – make sure they match the filename of what you have on your system.

Hit <enter> to run the command. You should see a “good signature from ThomasV” to indicate success. There will be some errors because we don’t have the public keys for the other peoples’ signatures which are contained in the signature file (this system of combining signatures in one file may change in later versions). Also, there is a warning at the bottom that we can ignore (this is alerting us that we haven’t explicitly told the computer we trust the ThomasV public key).

Now we have a verified copy of Electrum which is safe to use.

## Running Electrum

### Running Electrum if using Python

If you downloaded the Python version, this is how to make it work. You’ll see on the download page this:

![image](assets/5.webp)

For Linux, It’s a good idea to first update your system:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Copy the highlighted yellow text, paste it into the terminal, and hit <enter>. You’ll be asked for your password, possibly a confirmation to continue, and then it will install those files (“dependencies”).

You will also need to extract the zipped file to a directory of your choice. You can do this with the graphical user interface, or from the command line (pink highlighted command) – remember your file names may differ. (Note that when we verified the download in the previous section, it was the zip file we verified, not the extracted directory.)

There is an option to “install” using the PIP program, but this is unnecessary, and adds extra steps and installation of files. Just run the program using the terminal to bypass all that.

The steps (Linux) are:

1. navigate to the directory where the files are extracted
2. type: ./run_electrum

On a Mac, the steps are the same but you may need to first install Python3, and use this command to run:

```bash
python3 ./run_electrum
```

Once Electrum is running, the terminal window will remain open. If you close it, it will terminate the Electrum program. Just minimise it while using Electrum.

### Running Electrum with the Appimage

This is a bit easier, but not as easy as a Windows executable file. Depending on the version of Linux your running, by default, Appimage files may have attributes set so that execution is disallowed by the system. We must change this. If your Appimages works, you can skip this step. Navigate to where the file is, using terminal, then run this command:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” gives superuser privileges; “chmod” is a command to change the mode, altering who can read, write, or execute; “ug+x” means we are modifying the user and group to allow execution.

Adjust the filename to match your version.

Then, Electrum will run by double-clicking the Appimage icon.

### Running Electrum with Mac

Just double-click the downloaded file (it is a “drive”). A window will open. Drag the Electrum icon in the window onto your desktop, or wherever you want to keep the program. You can then “eject” the drive, and delete the drive (downloaded file).

To run the program, just double-click it. You may get some Mac-specific “nanny” errors that need to be bypassed.

### Running Electrum with Windows

Despite the fact that I hate Windows most of all, this is the simplest method. Just double-click the executable file to run.

## Start with a dummy wallet

When you first load Electrum, a window will open like this:

![image](assets/6.webp)

We will later select your server manually, but for now, leave the default and auto-connect.

Next, create a dummy wallet – do not ever put funds in this wallet. The purpose of this dummy wallet is to progress through the software and make sure everything is working well prior to you loading up your real wallet. We’re trying to avoid accidentally giving up privacy with a real wallet. If you’re just practicing, the wallet you create can be considered a dummy wallet anyway.

You can leave the name as “default_wallet” or change it to whatever you like, and click next. Later, if you have multiple wallets, you can find them and open them at this stage by first clicking “Choose…”

![image](assets/7.webp)

Choose “Standard wallet” and <Next>:

![image](assets/8.webp)

Then, select “I already have a seed”. I don’t want you to get in the habit of creating an Electrum seed, as it uses its own protocol that is not compatible with other wallets – this is why we don’t click “new seed”.

![image](assets/9.webp)

Go to https://iancoleman.io/bip39/ and create a dummy seed. First, change the word number to 12 (which is common practice), then click “generate” and copy the words in the box to your clipboard.

![image](assets/10.webp)

Then paste the words into Electrum. Here is an example:

![image](assets/11.webp)

Electrum will be looking for words that match its own protocol. We have to bypass that. Click options, and select BIP39 Seed:

![image](assets/12.webp)

The seed then becomes valid. (Before doing this, Electrum was expecting an Electrum seed so this seed was seen as invalid). Before you click next, notice the text that says “Checksum OK”. It is important (for the real wallet you may use later) that you see this before proceeding, as it confirms the validity of the seed you put in. The warning near the bottom can be ignored, it is the Electrum developer’s whinge about BIP39 and their “FUD’ey” claims that their version (which is not compatible with other wallets) is superior.

**A quick detour for an important warning:** the purpose of the checksum is to make sure you have entered your seed without typing errors. The checksum is the final part of the seed (the 12th word ends up being the checksum word) which mathematically is determined by the first part of the seed (11 words). If you were to type something wrong at the start, the checksum word will not mathematically match, and the wallet software will alert you with a warning. This doesn’t mean that the seed can’t be used to create a functional Bitcoin Wallet. Imagine creating a wallet with a typing error, loading the wallet with bitcoin, then one day you may need to restore the wallet, but when you do, you don’t recreate the typing error – you’ll restore the wrong wallet! It is quite dangerous that Electrum will let you proceed to make a wallet if your checksum is invalid, so be warned, it’s your responsibility to make sure. Other wallets will not let you proceed, which is far safer. This is one of the things I mean when I say Electrum is fine to use, once you learn to use it properly (Electrum devs should fix this).

Notice that if you wanted to add a passphrase, the chance to select that is in this options window, right at the top.

After clicking OK, you’ll be taken back to where you typed the seed phrase. If you selected a passphrase option, you DO NOT enter it with the seed words (the prompt for that comes next).

If you didn’t request a passphrase, you’ll see this screen next – more options for your wallet script type and derivation path which you can learn about here (https://armantheparman.com/public-and-private-keys/), but just leave the defaults and proceed.

![image](assets/13.webp)

**For extra info** The first option allows you to choose between:

- legacy (addresses starting with “1”),
- pay-to-script-hash (addresses starting with “3”),
- bech32/native segwit (addresses starting with “bc1q”).

At the time of writing, Electrum does not yet support taproot (addresses starting with “bc1p”). The second option in this window allows you to modify the derivation path. I suggest you never modify this, especially before understanding what it means. People will emphasise the importance of writing the derivation path down so you can recover your wallet if needed, but if you leave it as the default, you’re going to probably be fine, so don’t panic – but it’s still good practice to write the derivation path down.

Next, you’ll be given the option to add a PASSWORD. This is not to be confused with “PASSPHRASE”. A password locks the file on your computer. A passphrase is part of the make-up of the private key. Since this is a dummy wallet, you can leave the password blank and proceed.

![image](assets/14.webp)

You’ll get a pop-up about new version notifications (I suggest you select no). The wallet will then generate itself and be ready to use (but remember, this wallet is destined for deletion, it’s just a dummy wallet).

![image](assets/15.webp)

There are some things I suggest you do to set up the software environment (required only once):

### Change the units to BTC

Go to the top menu, tools –> electrum preferences, and there under the general tab, you’ll find the option to change the “base unit” to BTC.
Enable the Addresses and Coins tab

Go to the top menu, view, and select “show addresses”. Then go back to view and select “show coins”.

### Enable Oneserver

By default, Electrum connects to a random node. It also connects to many other secondary nodes. I’m not sure what data is exchanged with those secondary nodes, but we don’t want it happening, for privacy. Even if you specify a node, e.g. your own node, these multiple other nodes will also be connected, and I am not sure what information is being shared. Regardless, it is easy to prevent. Before I show you how to specify your own node, we will force Electrum to only connect to one server at a time.

**Note:** there is a way to do this by specifying “oneserver” from the command line, but I don’t recommend this way. I will show an alternative that I think is easier in the long run, and more likely not to let you accidentally connect to other nodes.

The reason we are using a dummy wallet is that if we had loaded our real wallet, with our real bitcoin, we would have inadvertently connected to a random node by now (even if we selected “set server manually” at the start, it still connects to these other secondary nodes for some reason (hey Electrum devs, you should fix this). If our wallet was private, this would be a disaster.

We also can’t do the steps I will show you below without first loading up some type of wallet. (We’re going to edit a configuration file that only gets populated and ready for editing once a wallet is loaded).

Now shut down Electrum **(IMPORTANT: if you don’t do this, the following changes you make will be erased)**.

### LINUX/MAC Config File

Open the terminal in Linux or Mac (Windows instructions later):

You should automatically be in the home folder. From there, navigate to the hidden electrum settings folder (this is different to where the application is).

```bash
cd .electrum
```

Notice the dot before “electrum” which indicates it is a hidden folder.

Another way to get there is to type:

```bash
cd ~/.electrum
```

where “~” represents the path of your home directory. You can see the full path of your current directory with the command “pwd“.

Once in the “.electrum” directory, type “nano config” and hit <enter>.

A text editor will open (called nano) with the config file open. The mouse doesn’t work much here. Use the arrow keys to get to the line that says:

```json
"oneserver": false,
```

Change “false” to “true”; and don’t disturb the syntax (don’t delete the comma or semicolon).

Hit <ctrl> x, to exit, then “y” to save, then <enter> which confirms changing without editing the filename.

Now run Electrum again. Then click the circle on the bottom right, which opens the network settings. Then, near the top in the overview tab, you’ll see “connected to 1 node” – this indicates success.

Just below that, you’ll see a text field and the server’s address is in there. You are currently connected to that random node. More on connecting to a node in the next section.

### Windows Config File

The windows config file is a bit harder to find. The directory is: `C:/Users/Parman/AppData/Roaming/Electrum`

Obviously, you have to change “Parman” to your own username for the computer.

In that folder you will find the config file. Open it with a text editor and edit the line:

```json
"oneserver": false,
```

Change “false” to “true”; don’t disturb the syntax (don’t delete the comma or semicolon).

Then save the file and exit.

## Connect Electrum to a node

Next, we want to connect our dummy wallet to a node of our choice. If you are not ready to run a node, you can do one of the following:

1. Connect to a friend’s personal node (requires Tor)
2. Connect to a trusted company’s node
3. Connect to a random node (not recommended).

By the way, here are instructions to run your own node, and these are the reasons why you should. (check out tutorials on the Node section or in our free courses)

### Connect to a friend’s node via Tor (Guide coming soon.)

### Connect to a trusted company’s node

The only reason to do this would be if you must access the blockchain and you don’t have your own node available (or a friend’s).

Let’s connect to Bitaroo’s node – We are told that they are not collecting data. They are a Bitcoin Only exchange, run by a passionate Bitcoiner. Connecting to them involves a little trust, but it is better than connecting to a random node, which could be a surveillance company.

Get to the Network Settings by clicking the circle in the bottom right part of the Wallet’s window (red indicates not connected, green indicates connected, and blue indicates connected via Tor).

![image](assets/16.webp)

Once you click the circle icon, a pop-up window will appear: Your wallet will show “connected to 1 node” since we forced that earlier.

Uncheck the “select server automatically” box, and then in the Server Field, type in Bitaroo’s details as shown:

![image](assets/17.webp)

Close the window, and now we should be connected to Bitaroo’s node. To confirm, the circle should be green. Click it again and check that the server details haven’t changed back to a random node.

### Connect to your own node

If you have your own node that’s great. If you have Bitcoin Core only, and not an Electrum SERVER as well, you won’t yet be able to connect an Electrum WALLET to your node.

**Note that Electrum Server and Electrum Wallet are different things:** the server is software required for Electrum Wallet to be able to communicate the Bitcoin blockchain – I don’t know why it was designed this way – possibly for speed but I could be wrong.

If you run a node software package like MyNode (the one I recommend people to start with), Raspiblitz (recommended as you get more advanced), or Umbrel (I personally don’t yet recommend it as I’ve experienced too many issues), then you will be able to connect your wallet simply by entering the IP address of the computer (Raspberry Pi) running the node, plus a colon, and 50002, as shown in the image in the previous section. (Further down I’ll show you how to find your node’s IP address).

Open the Network settings (click the green or red circle in the bottom right). Uncheck the “select server automatically” box, then enter your IP address as I have done yours will be different, but the colon and “50002” should be the same.

![image](assets/18.webp)

Close the window, and now we should be connected to your node. To confirm, click the circle again and check that the server details haven’t changed back to a random node.

Sometimes, despite doing everything right, seemingly, it refuses to connect. Here are things to try…

- Upgrade to a newer version of Electrum, and your node software;
- Try deleting the cache folder in the “.electrum” directory;
- Try changing the port from 50002 to 50001 in the network settings;
- Use [this guide](https://armantheparman.com/tor/) to connect using Tor as an alternative;
- Reinstall Electrum Server on the node.

## Finding Your Node’s IP Address

An IP address is not something a regular user commonly knows how to look up and use. I’ve helped many people run a node, and then connect their wallets to the node – a stumbling block often seems to be finding its IP address.

For MyNode, you can type in a browser window: `mynode.local`

Sometimes, “mynode.local” doesn’t work (make sure you’re not typing it in a Google search bar. To force the navigation bar to recognise your text as an address and not a search, precede the text with `http://` like this: `http://mynode.local`. If that doesn’t work, try it with an “s”, like this: `https://mynode.local`.

This will access the device, and you can click on the settings link (see my blue “circle” below) to show this screen where the IP address is located:

![image](assets/19.webp)

This page will load and you’ll see the node’s IP (blue “circle”)

![image](assets/20.webp)

Then, in the future, you can type 192.168.0.150, or http://192.168.0.150 into your browser.

For the Raspiblitz (when not connecting a screen), you need a different method (which works for the MyNode as well):

Log in to your router’s webpage – here we will find the IP address of all your connected devices. The router’s webpage will be an IP address that you enter into a web browser. Mine look is:

    http://192.168.0.1

To get the login credentials to the router, you can look it in the user manual or sometimes even on a sticker on the router itself. Look for the username and password. If you can’t find it, try User: “admin” Password: “password”

If you are able to log in, you’ll see your connected devices and from their names, it may be clear which your node is. The IP address will be there.

### If the first two methods fail, the last will work but it’s tedious:

First, find the IP address of any device on your network (the current computer will do).

On a Mac, you’ll find it in Network preferences:

![image](assets/21.webp)

We are interested in the first 4 elements (192.168.0), not the 4th element, the “166” that you see in the image (yours will be different).

For Linux, use the command line:

```bash
ifconfig | grep inet
```

That vertical line is the “pipe” symbol and you’ll find it below the <delete> key. You’ll see some output and an IP address. (Ignore 127.0.0.1 it’s not that, and ignore the netmask)

For Windows, open the command prompt (cmd) and type:

```bash
ipconfig/all
```

and press Enter. The IP address can be found in the output.

That was the easy bit. The hard part is now to find your node’s IP address – we need to brute-force guess. Let’s say for example your computer’s IP address starts with 192.168.0.xxx, then for your node, in a browser, try: `https://192.168.0.2`

The smallest possible number is 2 (0 means any device, and 1 belongs to the router) and the highest, I believe is 255 (this happens to be 11111111 in binary, the largest number held by 1 byte).

One by one, work your way up towards 255. Eventually, you’ll stop at the correct number that loads your MyNode page (or RaspiBlitz page). Then you’ll know what number to enter in your Electrum network settings to connect to your node.

It will look something like this (make sure you include the colon and number afterwards):

![image](assets/22.webp)

**Note** it’s useful to know that these IP addresses are INTERNAL to your home network. Nobody outside can see them and they are not sensitive. They’re kind of like phone extensions in a large organisation directing you to different telephones.

## Delete dummy wallet

Now we have successfully connected to one and only one node. This is how Electrum will load by default from now on. You should now delete the dummy wallet (Menu: file –> delete), in case you accidentally send funds to this insecure wallet (It is insecure because we did not create it in a safe way).

## Make a practice wallet

After deleting the dummy wallet, start again and make a new one, in the same way, only this time, write down the seed words and keep them fairly safe.

It’s a good idea to learn how Electrum works with this practice wallet, without the cumbersome hardware wallet (needed for high security). Only put a small amount of bitcoin in this wallet – Assume you will lose this money. Once proficient, then learn to use Electrum with a hardware wallet.

In the new wallet you’ve created, you’ll see a list of addresses. The green ones are called “receiving addresses”. They are a product of 3 things:

- The seed phrase
- The passphrase
- The derivation path

You new wallet has a set of receiving addresses that can be mathematically and reproducibly created by any software wallet that has the seed, passphrase and derivation path. There are 4.3 billion of them! More than you’ll need. Electrum only shows you the first 20, and then more as you use up the first ones.

More information about bitcoin private keys can be found in this guide.

![image](assets/23.webp)

This is very different to some other wallets which only present 1 address at a time.

Because you entered the seed phrase in creating this wallet, Electrum has the private key for each of the addresses, and spending from these addresses is possible.

Also note that there are yellow addresses, called “change addresses” – These are just another set of addresses from a different mathematical branch (another 4.3 billion of these exist). They are used by the wallet to automatically send excess funds back into the wallet as change. For example, if you take 1.5 bitcoin and spend 0.5 to a merchant, the 1.0 remainder needs to go somewhere. Your wallet will spend it to the next empty yellow change address – otherwise, it goes to the miner! For more information about this (UTXOs) see ![this guide](https://armantheparman.com/utxo/).

Next, go back to the Ian Colman private key website and enter the seed (instead of generating one). You’ll see below the private and public key information changes; everything below is dependent on the things above on the page.

**Remember:** you should “never” enter the seed of your real Bitcoin wallet or a computer, a malware can steal it. We are just using a practice wallet, for learning purposes, so it’s fine for now.

Scroll down and change the derivation path to BIP84 (segwit) to match your Electrum wallet by clicking the BIP84 tab.

![image](assets/24.webp)

Below that, you’ll see the account extended private key and the account extended public key:

![image](assets/25.webp)

Go to Electrum, and compare that they match. There is a menu at the top, wallet –>information:

![image](assets/26.webp)

This pops up:

![image](assets/27.webp)

Notice the two public keys match.

Next, compare the addresses. Go back to Ian Coleman’s site and scroll to the bottom:

![image](assets/28.webp)

Notice they match with the addresses in Electrum.

Now we’ll check the change addresses. Scroll up a bit to the derivation path and change the last 0 to a 1:

![image](assets/29.webp)

Now scroll down and compare the addresses match the yellow addresses in Electrum

Why did we do all this?

We took the seed words and put them through two different independent software programs to make sure they were giving us the same information. This significantly reduces the risk that nefarious code is lurking inside and giving us false private or public keys, or addresses.

The next thing to do is to receive a small test and to spend it within the wallet from one address to another.

## Testing the Wallet (Learn to use it)

Here I’ll show you how to receive a UTXO to your wallet and then move it (spend it) to another address within the wallet. This is a very small amount that we won’t mind risking to lose.

This has a number of purposes.

- It will prove that you have the power to spend coins in the new wallet.
- It will demonstrate how to use the Electrum software to make a spend (and some features), before we add extra complexity for safety (using a hardware wallet or air-gapped computer)
- It will reinforce the idea that you have many addresses to choose from to receive and spend, within the same wallet.

Open your test Electrum Wallet and click the Addresses tab, then right-click the first address and select Copy –> Address:

![image](assets/30.webp)

The address is now in your computer’s memory.

Now go to an exchange where you have some bitcoin, and let’s withdraw a small amount to this address, say 50,000 sats. I’m going to use Coinbase as an example because it’s the most commonly used exchange, even though they are an enemy of Bitcoin, and I’m disgusted to log in to an old abandoned account for this purpose.

Log in, and click the Send/Receive button, which as of today is in the top right corner of the webpage.

![image](assets/31.webp)

I obviously have no funds with Coinbase, but just imagine there are funds here and follow along: Paste the address from Electrum in the “To” field as I have done. You’ll also need to select an amount (I suggest 50,000 sats or so). Do not put an “optional message” – Coinbase is collecting enough of your data (and selling it), there is no need to help them. Finally, click “Continue”. After that I don’t know what other pop-ups you’ll get, you’re on your own, but the method is similar for all exchanges.

![image](assets/32.webp)

Depending on the exchange, you may see the sats in your wallet immediately, or some dealy of hours/days.

Note that Electrum will show you received coins even if they have not been confirmed on the blockchain. The coins you have are being read from a Bitcoin Node’s waiting list, or “mempool”. When it gets on to a block, you’ll see the funds as confirmed.

Now that we have a UTXO in our wallet, we should label it. Only we can see this label, it’s got nothing to do with the public ledger. All our Electrum Labels are only visible on the computer we’re using. We can actually save a file and use it to restore all our labels to a different computer running the same wallet.

### Make a label for a UTXO

I needed a donation to this test wallet, thanks to @Sathoarder for providing me with a live UTXO (10,000 sats), and another person (anon) donated to the same address (5000 sats). Notice there are 15,000 sats in the first address balance, and a total of 2 transactions (far right column). Down the bottom, the Balance is 10,000 sats confirmed, and another 5,000 sats are unconfirmed (still in the mempool).

![image](assets/33.webp)

Now, if we head over to the Coins tab, we can see two “received coins” or UTXOs. They are both in the same address.

![image](assets/34.webp)

Going back to the address tab, if you double-click on the “labels” area next to the address, you’ll be able to enter some text, then hit <enter> to save:

![image](assets/35.webp)

This is good practice so you can keep a track of where your coins came from, if they are KYC-free or not, and how much each UTXO cost you (in case you need to sell and calculate the tax to be stolen from you by your government).

Ideally, you should avoid accumulating multiple coins in the same address. If you do decide to do that (don’t), you can label each coin instead of all of them with the same label using the address method. You can’t actually go to the “coins” tab and edit the labels there (no, that would be too intuitive!). You have to go to the History tab, find the transaction, label that, and then you’ll see the labels in the coin section. Any labels you see in the coins section are from the Address labels OR the history labels, but any history label overrides any address label. To back up your labels to a file, you can export them from the menu at the top, wallet–>lables–>export.

Next, let’s spend the coins from the first address to the second address. Right-click the first address and select “spend from” (This is actually not necessary in this scenario, but imagine we have many coins in many addresses; using this feature, we can force the wallet to only spend the coins we want. If we want to select multiple coins in multiple addresses, we can select the addresses with a left-mouse click while holding the command key, then right-click, and select “spend from”:

![image](assets/36.webp)

Once you do that, there’re be a green bar at the bottom of the wallet window indicating the number of coins you have selected and the total available to spend.

You can also spend individual coins within an address and exclude others in the same address, but this is discouraged because you are leaving coins in an address that has been cryptographically weakened due to the spending of one of the coins (another reason not to put multiple coins in one address, besides for privacy reasons, is that given that you should spend them all if you spend one, this gets expensive unnecessarily). Here’s how to select a single coin from a shared address, but don’t do it:

![image](assets/37.webp)

Now, we have the two coins selected for spending. Next, we decided where to spend them. Let’s send them to the second address. We’ll need to copy the address like so:

![image](assets/38.webp)

Then go to the “Send” tab, and paste the second address in the “pay to” field. No need to add a description; you could, but you can do that later by editing labels. For the amount, select “Max” to spend all the coins we selected. Then click “Pay”, and then click the “advanced” button on the pop-up that appears.

![image](assets/39.webp)

Always click “advanced” at this stage so we can get fine control and check exactly what’s in the transaction. Here is the transaction:

![image](assets/40.webp)

We see two internal white boxes/windows. The top one is the inputs window (which coins are being spent), and the bottom one is the outputs (where the coins are going).

Note, the status (top left) is “unsigned” for now. The “Amount sent” is 0 because the coins are being transferred within the wallet. The fee is 481 sats. Note that if it was 480 sats, the final zero would be dropped off, like this, 0.0000048 and to the tired eye, this can look like 48 sats – be careful (something Electrum devs should fix).

The size of the transaction refers to the data size in bytes, not the amount of bitcoin. The “replace by fee” is on by default, and it allows you to resend the transaction with a higher fee if needed. The LockTime allows you to adjust when the transaction is valid – I haven’t played with that yet, but advise against using it unless you fully understand what you are doing and have had some practice with small amounts.

Down the bottom, we have some fancy mining fee adjustment tools. All you need to do for internal transfers is set it to the minimum fee of 1 sat/byte. Just manually type the number in the Target fee field. To check an appropriate fee for an external payment, you can consult https://mempool.space to see how busy the mempool is, and some suggested fees are displayed.

![image](assets/41.webp)

I have selected 1 sat/byte.

In the input window, we see two entries. The first is the 5000 sat donation. We see on the left its transaction hash (which we can look up on the blockchain). Next to it, there is a “21” – this indicates that it is output labelled 21 in that transaction (it’s actually the 22nd output because the first is labelled zero).

Something to note here: UTXOs exist only inside a transaction. To spend a UTXO we have to reference it, and put that reference into the input of a new transaction. The outputs then become new UTXOs and the old UTXO becomes a STXO (Spent transaction output).

The second line is the 10,000 sat donation. It has a “0” next to the transaction hash that it came from because it is the first (and possibly only) output for that transaction.

In the bottom window, we see our address. Notice the bitcoin total of the inputs don’t quite match the total of the outputs. The difference goes to the miner. The miner looks at the discrepancy in all the transactions in the block it’s trying to mine, and adds that number to its reward. (Mining fees in this way are totally disconnected from the chain of transactions and start a new life).

If we adjust the mining fee, the output value will automatically change.

**It’s worth pointing out here:** note the colour of the addresses in the transaction window. Remember that the green addresses are listed in your address tab. If an address is highlighted green (or yellow) in a transaction window, then Electrum has recognised the address as one of its own. If the address has no highlight, then it is an external address (external to the currently open wallet), and you should check it with extra care.

Once you check everything in the transaction and are sure you are happy with which coins you are spending, and where the coins are going, you can click “finalise.”

![image](assets/42.webp)

After you click “finalise”, you can no longer make edits – If you need to, you have to close this and start again. Notice the “finalise” button has changed to “export”, and new buttons have appeared: “save”, “combine”, “sign” and “broadcast”. The “broadcast” button is greyed out because the transaction is unsigned and so invalid at this stage.

Once you click sign, if you have a password for the wallet you’ll be prompted for that, and then the status (top right) will change from “Unsigned” to “Signed”. Then the “Broadcast” button will be available.

After you broadcast, you can close the transaction window. If you go to the address tab, you’ll now see the first address is empty, and the second address has 1 UTXO.

Note: You’ll see all these changes even before the transaction has been mined to a block, or “confirmed”. This is because Electrum updates balances/transactions based on not just the blockchain data, but the mempool data as well. Not all wallets do this.

Something to point out is that instead of broadcasting, we can save the transaction for later. It can be saved either in the unsigned or signed states.

Click the “export” button (paradoxically, DO NOT click the “save” button), and you will see a number of options. The transaction is encoded with text, and therefore can be saved in a number of ways.

![image](assets/43.webp)

Saving to a QR code is very interesting. If you choose this, a QR will pop up:

![image](assets/44.webp)

You can then take a photo of the QR code. There are a number of things you can do with this, but for now, let’s just say you are loading it back into the wallet later. You can close Electrum, load the wallet again, and go to the menu Tools:

![image](assets/45.webp)

This will load up your computer’s camera. You then show the camera the photo of the QR code in your phone, and this will load the transaction back, exactly as you left it.

It’s not intuitive how to load a saved transactions, so take special note. Loading a transaction is not a “tool” but the option is hidden in the tools menu (another thing the Electrum devs should fix).

A similar process is possible with a transaction saved as a file. Try practicing with either method, within the same wallet. I won’t go through it here but you can use this feature to pass a transaction around between the same wallet on different computers, between multisignature wallets, and to and from hardware wallets. Here are some instructions.

Now, coming back to the “save” button – this is not how to save the transaction text. What this actually does is tell the Electrum wallet to recognise this transaction on the local computer as being submitted as a payment. If you do that by accident, you’ll see the transaction with a little computer icon. You can right-click and delete the transaction – don’t worry, you can’t delete bitcoin this way. Electrum will then forget that this transaction ever happened, and will “refund” the sats back and display the sats in the correct location where they actually exist.

### Change addresses

Change addresses are interesting. You need to understand UTXOs to understand this explanation. If you are spending to an address an amount that is smaller than UTXO, then the leftover bitcoin will go to the miner unless a change output is specified.

You might have a 6.15 bitcoin UTXO and want to spend 0.15 bitcoin to donate to some protesters being oppressed by the tyrannical “democratic” government somewhere in the world. You would then take the 6.15 bitcoin (using the “spend from” function in Electrum), and put it in a transaction.

You’d paste the protestors’ address in the “pay to” field, perhaps you’d put “EndTheFed & WEF” in the “description” field, and for the amount, you’ll put 0.15 bitcoin and click “pay”, then “advanced”.

In the transaction screen, for the input window, you’ll see the 6.15 bitcoin UTXO. For the output window, you’ll see an address that has no highlight (this is the protestors’ address) with 0.15 bitcoin beside it. You’ll also see a yellow address with slightly less than 6.0 bitcoin. This is the change address automatically selected by the wallet from one of its own yellow change addresses. The purpose of the change address is so the wallet can put change coins in them without messing up the availability of the receiving addresses that you may have plans for, or sent invoices for. If they are going to be used later by customers, for example, you don’t want your wallet automatically using them and filling them up. It’s messy and bad for privacy.

Note that as you adjust the mining fee, the change output amount will automatically adjust, not the payment amount.

### Manual change or pay to many

This is a really interesting feature of Electrum. You access it like this.

![image](assets/46.webp)

You can then enter multiple destinations for the UTXO balance you are spending, like this:

![image](assets/47.webp)

Paste the address, type in a comma, then a space, then the amount, then <enter>, then do it again. DO NOT ENTER AMOUNTS IN THE “AMOUNT” WINDOWS – Electrum will populate the total here as you type the individual amounts in the “Pay to” window.

This allows you to manually determine where the change goes (eg a specific address in your wallet, or another wallet), or you can pay many people at once. If your total is not high enough to match the size of the UTXO, Electrum will still create an additional change output for you.

The Pay to Many feature also allows for the possibility to create your own “PayJoins” or “CoinJoins” – outside the scope of this article, but I have a guide here. (https://armantheparman.com/cj/)

## Wallets

I want to demonstrate a Watching Only Wallet using Electrum. To do that, I need to first define “wallet”. There are two ways “wallet” is used in Bitcoin:

- Type A, “wallet” – refers to the software that shows you your addresses and balances, eg Electrum, Blue Wallet, Sparrow Wallet etc.

- Type B, “wallet” – refers to the unique collection of addresses that are associated with the combination of our seed_phrase/passphrase/derivation_path. There are 8.6 billion addresses in any wallet (4.3 billion receiving addresses, and 4.3 billion change addresses). If you change anything in the seed phrase, passphrase, or derivation path, you get an unused wallet with new, and all unique, 8.6 billion empty addresses.

Which type anyone is referring to when using the word “wallet” is obvious in context.

## Watching Wallet – an exercise

It’s not completely obvious what a watching wallet is for, but I’ll start by explaining what it is, how to make a practice one, and then we will come back to its purpose later when I explain more about hardware wallets. (For an in-depth review of how to use a hardware wallet, and various specific brands, see here.)

We’re going to make a dummy regular wallet (this time adding a little more complexity with a passphrase), and then its corresponding watching wallet. If you like you can copy the one I made exactly, or create your own – this wallet is to be discarded; don’t actually use it. Start by generating a 12-word seed using the Ian Coleman website.

Notice the 12 random words in the screenshot below, and that I have entered a passphrase in the passphrase field:

PASSPHRASE: “Craig Wright is a liar and a fraud and belongs in jail. Also, Ross Ulbricht should be released from prison immediately.”

The passphrase can be up to 100 characters long, and ideally should be unambiguous and not too short – The one I have used is just for fun – I generally suggest avoiding uppercase letters and symbols just to reduce your stress in trying combinations if you ever had an issue with remembering your passphrase.

![image](assets/48.webp)

Next, in Electrum, go to the menu file–>new/restore. Type a unique name to create a new wallet and click “next”.

![image](assets/49.webp)

The next steps you should be familiar with by now, so I’ll list them without pictures:

- Standard wallet
- I already have a seed
- Copy and paste the 12 words in the box, or type them in manually.
- Click options and select BIP39, and also click the passphrase checkmark (“extend this seed with custom words”)
- Enter your passphrase exactly as you did on the Ian Coleman page
- Leave the default script semantics and derivation path
- No need to add a password (locks the wallet)

Now go back to the Ian Coleman site, down to the “derivation path” section, and click the “BIP 84” tab to select the same script semantics as the defaults in Electrum (Native Segwit).

![image](assets/50.webp)

The extended private and public keys are just below, and they change when you make changes to the derivation path (or anything else higher up the page).

![image](assets/51.webp)

You will also see “BIP32 extended private/public” keys – these are to be ignored for now.

The Account extended private key can be used to fully regenerate your wallet. The account extended public key, however, can only produce a limited version of the same wallet (watching wallet) – If you put this key in Electrum, it will still produce all the 8.6 billion addresses that the seed or extended private key would have, but there will be no private keys available to Electrum, so no spending is possible. Let’s do it now to demonstrate the point:

Copy the “account extended public key” to the clipboard.

Then go to Electrum, leave the current wallet we made open, and go to file–>new/restore. The process to make the wallet is a little different than before:

- Standard wallet
- Use a master key
- Paste the extended public key in the box and proceed
- No need to enter a passphrase; it’s already part of the extended public key
- No need to enter the script semantics and derivation path
- No need to add a password (locks the wallet)

When the wallet loads, you should notice that exactly the same addresses are loaded as previously when the seed was entered. You should also notice at the very top in the title bar, it says “watching wallet”. This wallet can show you your addresses, and balances (by checking balances via a node), but you are not able to SIGN transactions (because the watching wallet has no private keys).

Then what’s the point of it?

One reason, and not the main one, is that you can potentially observe your wallet and its balance on a computer without exposing your private keys to any malware on the computer.

Another is that it is REQUIRED in order to make payments if you choose to keep your private keys off the computer; I’ll explain:

**Hardware wallets (HWW)** were created so that a device can hold your private keys securely (locked with a PIN), never expose the keys to a computer (even when connected to a computer via a cable), and are themselves unable to connect to the internet. Such a device can not make transactions on its own because all bitcoin transactions start by referencing a UTXO(s) on the blockchain (which is on a node). A wallet must specify which transaction ID the UTXO is in, and which output of the transaction is the one to be spent. Only after specifying the input can a new transaction be created in the first place, let alone signed. Hardware wallets can’t create transactions because they have no access to any UTXOs – they’re not connected to anything!

An extended public key is usually extracted from the HWW, and addresses are then displayed on a computer – many people will be familiar with the Ledger software or Trezor Suite showing addresses and balances on their computer – this is a watching wallet. These programs can create transactions, but they can’t sign. They can only have transactions signed by HWWs that are connected to them. The HWW takes the newly generated transaction from the watching wallet, signs it, and then sends it back to the computer for broadcasting to a node. **The HWW can’t broadcast by itself**, its associated watching wallet does that. In this way, the two wallets (public key wallet on the computer, and private key wallet in the HWW) cooperate to generate, sign, and broadcast, all while making sure the private keys stay isolated and away from an internet-connected device.

## Partially Signed Bitcoin Transactions (PSBTs)

It’s possible for a transaction to be created and saved to a file, later reloaded, signed, saved, later reloaded, and then finally broadcasted – I’m not saying anyone would need to do this; it’s just something that is possible.

Now consider a 3 of 5 multisignature wallet – 5 private keys create a wallet, and 3 are needed to fully sign a transaction (See here to learn more about multisignature wallet keys). It’s possible to have 5 different computers each with one of the five private keys.

Computer one could generate a transaction and sign it. It could then save it to file, and send it by email to Computer 2. Computer 2 can then sign, and could potentially save the file to a QR code, and transmit the QR via a Zoom call to Computer 3 on the other side of the world. Computer 3 can capture the QR, load the transaction into electrum, and sign the transaction. After the first 2 signatures, the transaction was a PSBT (partially signed bitcoin transaction). After the 3rd signature, the transaction became fully signed and valid, ready for broadcasting.

To learn more about PSBTS, see this guide. (https://armantheparman.com/psbt/)

## Using Hardware Wallets with Electrum

I have a guide on using hardware wallets in general, which I think would be important for people who are new to HWWs, to read. (https://armantheparman.com/using-hwws/)

There are also guides on various brands of HWWs connecting to Sparrow Bitcoin Wallet found here. (https://armantheparman.com/hwws/)

This will be my first guide showing how to use a hardware wallet with Electrum – I am going to use the ColdCard hardware wallet to demonstrate. This is not meant to be a detailed guide on the ColdCard specifically, that guide is here. I am just showing Electrum-specific points. (https://armantheparman.com/cc/)

### Connecting via the micro SD card (air-gapped)

Before connecting your real wallet via the ColdCard, I hope you have gone through the earlier steps of loading an Electrum dummy wallet and setting up the network parameters.

Then, on the ColdCard, insert the SD card. I am assuming you have created your seed already. If you are accessing the wallet with a passphrase, apply it now. Scroll down and select the menu Advanced/Tools –>Export Wallet –> Electrum Wallet.

You can scroll down and read the message. It always offers you to select “1” to enter a non-zero account number (something part of the derivation path), but if you followed my advice, you haven’t messed with the default derivation paths so you won’t want a non-zero account number; just press checkmark to continue.

Then select the script semantics. Most people will be selecting “Native Segwit”.

It will say “Electrum wallet file written”, and will display the file name. Make a mental note of it.

Then take the micro SD card out and put it in the computer with Electrum.

Some operating systems will automatically open up the file explorer when you insert the microSD. Many people will see the new wallet file and double-click it, and wonder why it doesn’t work. It’s not a great design. You actually must ignore the file explorer (close it), and open the wallet file using Electrum:

Open Electrum. If it’s already open with some other wallet, select file –> new. We’re looking for this window:

![image](assets/52.webp)

Here’s the trick, it’s not intuitive. Click “choose”. Then navigate the file system on the microSD card and find the wallet file and open it.

Now you have opened up your hardware wallet’s corresponding watching wallet. Nice.

### Connecting via the USB cable.

This way should be easier, but for Linux computers, it’s much harder. Something called “Udev rules” needs to be updated. Here’s how (detailed guide https://armantheparman.com/gpg-articles/ ), and briefly:

It’s a good idea to make sure the system is up to date. Then:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

then...

```bash
python3 -m pip install ckcc-protocol
```

If you get an error make sure pip is installed. You can check with (pip –version), and you can install it with (sudo apt install pythron3-pip)

Create or modify existing, the file, /etc/udev/rules.d/

Like this:

```bash
sudo nano /etc/udev/rules.d
```

A text editor will open. Copy the text from here and paste it into the rules.d file, save and exit.

![image](assets/53.webp)

Then run these commands one after the other:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```

If you get a message “group plugdev” already exists, that’s fine, proceed. After the second command, you’ll get no feedback/reply, just proceed to the third command.

You may need to disconnect and then reconnect the ColdCard to the computer.

If after all of this you are still unable to connect the ColdCard, I would try updating the firmware (guide soon, but for now, you can find instruction’s on the manufacturer’s website).

Next, create a new wallet:

- Standard wallet
- Use a hardware device
- It will scan and detect your ColdCard. Proceed.
- Select the script semantics and derivation path
- Decide if the wallet file should be encrypted (recommended)

### Transactions using the ColdCard

With the cable connected, transactions are easy. Signing transactions will be seamless.

If using the device in an air-gapped way, you manually have to pass the saved transaction between devices using the microSD card. There are some tricks.

After creating a transaction and finalising it, you need to click the export button in the bottom left corner. You’ll see “save to file” which counterintuitively, is not what we want. You actually have to first go to the very last menu option which says “for hardware wallets”, and then, from within that selection, find the other “save to file” and select that. Then save the file to the microSD, take the card out and put it in the ColdCard. Remember that you may need to apply a passphrase to select the correct wallet. The screen will say ready to sign. Click the checkmark, inspect the transaction, and proceed by confirming with the checkmark. Once done, take out the card, and put it back in the computer.

Then we need to open the transaction using electrum. The function is hidden in the menu tools –> load transaction. Navigate the file system and find the file. There will be three files every time you sign. The original saved file that the Watching Wallet made, and two made by the ColdCard (I don’t know why it does this). One will say “signed” and one will say “final”. It’s not intuitive but the “signed” one is not useful, we need to open the “final” transaction.

Once you load that, you can click “broadcast” and the payment will be made.

## Updating Electrum and the Hidden “.electrum” directory

Electrum lives on your computer in two places. There is the application itself, and there is a hidden configuration folder. That folder lives in different places depending on your operating system:

Windows:

```bash
 C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum
```

Mac:

```bash
/Users/your_user_name_goes_here/.electrum
```

Linux:

```bash
/home/your_user_name_goes_here/.electrum
```

Note that `.` before `electrum` in Linux and Mac – that indicates the director is hidden. Also, note that this directory is only created (automatically) once you run Electrum for the first time. The directory contains the electrum configuration file and also the directory that holds any wallets you have saved.

If you delete the Electrum program from your computer, the hidden directory will remain, unless you actively delete that too.

To upgrade electrum, you go through the same procedure as I described at the beginning to download and verify. You will then have two copies of the program on your computer, and you can run either – each program will access the same hidden electrum folder for its configuration and wallet access. All the things we saved, like the base unit, the default node to connect to, other preferences, and access to wallets, will remain because all of that is saved in that folder.

### Moving your Electrum and Wallets to another computer

To do this, you can copy the program files to a USB drive, and also copy the .electrum directory. Then copy or move them to the new computer. You don’t need to verify the program again. Make sure to copy the .electrum directory to the default location (remember to copy it BEFORE running Electrum for the first time on that computer, otherwise an empty default .electrum folder will be populated, and you might get confused).

## Labels

As I explained earlier, on the address tab, there is a label column. You can double-click there and enter notes for yourself (it’s only on your computer, not public, and not on the blockchain).

![image](assets/54.webp)

When moving your Electrum wallet to another computer, you may wish to not lose all these notes. You can back them up to a file using the menu, wallet > labels > export, and then on the new computer, use wallet > labels > import.

## Tips:

If you find this resource useful, and you’d like to support what I do for Bitcoin, you can donate some sats here:

Static Lightning Address: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/
