---
name: Ashigaru Terminal
description: Use Ashigaru on desktop to make coinjoins
---

![cover](assets/cover.webp)


Ashigaru Terminal is the Ashigaru team's adaptation of Sparrow Server, which implements the Whirlpool coinjoin protocol. This software is a continuation of the work begun by Samourai Wallet, in particular on Whirlpool GUI, whose fundamental principles it adopts: self-custody and confidentiality preservation.


This software is a fork of Sparrow Server, modified and optimized for full integration with the Whirlpool ecosystem, the ZeroLink coinjoin protocol originally developed by the Samourai teams.


Ashigaru Terminal operates from a minimalist TUI interface and can be deployed on a personal computer or on a dedicated server. It lets you interact directly with Whirlpool to initiate "*Tx0*", manage "*Deposit*", "*Premix*", "*Postmix*" and "*Badbank*" accounts, and perform automatic remixes to reinforce the confidentiality of your parts.


In short, Ashigaru Terminal will be particularly useful if you want to create coinjoins using Whirlpool.


In this first tutorial, I'll take you through the installation and operation of Ashigaru Terminal. A second, more advanced tutorial will then be devoted to the actual creation of coinjoins.


## 1. Install Ashigaru Terminal


To install Ashigaru Terminal, you'll need Tor Browser, as the binaries are only distributed via the Tor network. If you haven't already done so, [install it on your machine](https://www.torproject.org/download/).


### 1.1. download Ashigaru Terminal


From Tor Browser, go to [the releases page of their Git repository](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) to download the latest version of Ashigaru Terminal for your operating system.


```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```


![Image](assets/fr/01.webp)


Download the following 2 files for your operating system:


- The binary (`ashigaru_terminal_v1.0.0_amd64.deb` for Debian/Ubuntu, `.dmg` for macOS or `.zip` for Windows) ;
- The signed hashes file: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.


### 1.2. Check Ashigaru Terminal


Before running the software on your device, you need to check its authenticity and integrity. This is an important step, as it prevents you from installing a fraudulent version that could compromise your bitcoins or infect your machine.


Open a new browser tab and go to [Keybase verification tool](https://keybase.io/verify). Paste the contents of the `.txt` file you've just downloaded into the field provided, then click on the `Verify` button.


![Image](assets/fr/02.webp)


To diversify your sources of verification, you can also compare the message with the one available on the clearnet [ashigaru.rs](https://ashigaru.rs/download/) site, in the `/download` section.


![Image](assets/fr/03.webp)


If the signature is valid, Keybase will display a message confirming that the file has been signed by Ashigaru's developers.


![Image](assets/fr/04.webp)


You can also click on the `ashigarudev` profile displayed by Keybase and check that their key fingerprint matches exactly : `A138 06B1 FA2A 676B`.


![Image](assets/fr/05.webp)


If an error appears at this stage, the signature is invalid. In this case, **do not install the downloaded software**. Start again from the beginning, or ask the community for help before continuing.


Keybase has provided you with the authenticated hash of the application. We'll now check that the hash of the `.deb`, `.zip` or `.dmg` file you've downloaded matches the one validated on Keybase. To do this, go to [HASH FILE ONLINE](https://hash-file.online/).


Click on the `BROWSE...` button and select the `.deb`, `.zip` or `.dmg` file downloaded in step 1.1. Then choose the `SHA-256` hash function, and click on `CALCULATE HASH` to generate the hash for your file.


![Image](assets/fr/06.webp)


The site will then display the software hash. Compare it with the hash you verified on Keybase.io. If the two match perfectly, the authenticity and integrity check has been successful. You can then use the software.


![Image](assets/fr/07.webp)


### 1.3 Launch Ashigaru Terminal



- Debian / Ubuntu


To install the software, run the command :


```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```


Modify the order according to the downloaded version.


Then check the installation:


```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```


Then launch the software:


```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```



- Windows**


Right-click on the `.zip` file you have downloaded and checked, then select `Extract All...` to extract its contents.


Once extraction is complete, double-click on the `Ashigaru-terminal.exe` file to launch the software.


![Image](assets/fr/08.webp)


## 2. Getting started with Ashigaru Terminal


Ashigaru Terminal is a TUI (*Text-based User Interface*) program, i.e. a minimalist interface running directly in the terminal. You interact with it using menus and keyboard shortcuts, but without any real classic graphic environment.


![Image](assets/fr/09.webp)


It's easy to use: use your keyboard's arrow keys to navigate through the menus, and press the `Enter` key to validate an action or confirm a choice.


## 3. Connecting your node to Ashigaru Terminal


By default, Ashigaru Terminal connects to a public Electrum server. This obviously presents risks in terms of confidentiality and sovereignty. So we're going to configure it to connect directly to your own Electrum Server.


To do this, open the `Preferences > Server` menu.


![Image](assets/fr/10.webp)


Click on the `< Edit >` button.


![Image](assets/fr/11.webp)


Select `Private Electrum Server`, then click `<Continue>`.


![Image](assets/fr/12.webp)


Enter the URL and port of your server. You can specify a Tor address in `.onion`. Then click on `< Test >` to verify the connection.


![Image](assets/fr/13.webp)


If the connection is successful, the message `Success` will appear, along with details of your server.


![Image](assets/fr/14.webp)


If you don't yet have a Bitcoin node, I recommend you take this course:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*In my case, for this tutorial, I'm going to disconnect from my Electrs server because I'm working on testnet. However, operation remains strictly identical on mainnet.*


## 4. Create a wallet on Ashigaru Terminal


Now that the software is correctly configured, we can add a Bitcoin wallet.


You have two options:


- You can create a new wallet from scratch and use it exclusively on Ashigaru Terminal. In this case, you will need to open this software each time you wish to interact with your wallet;
- Alternatively, you can import your existing Ashigaru wallet directly from your phone into Ashigaru Terminal. The disadvantage of this method is that it slightly reduces the security of your setup, as your wallet is then exposed to two risky environments instead of one. On the other hand, it offers the advantage of being able to leave Ashigaru Terminal running continuously to mix your coins, while allowing you to spend them remotely via the Ashigaru mobile app.


In this tutorial, we'll opt for the second method. However, if you'd prefer to create an entirely new wallet, the procedure remains the same: the only difference will be during creation, when you'll need to save your new mnemonic phrase and your new passphrase.


Please also note that Ashigaru Terminal does not allow you to spend your bitcoins directly. You can either synchronize the same wallet on Ashigaru Terminal and on the Ashigaru app (which I'll do in this tutorial), or use the `Mix to` option (which we'll look at in the next tutorial) to automatically send your funds to a wallet hardware after a set number of mix cycles.


If you do not yet have a wallet on the Ashigaru application, you can follow the dedicated tutorial :


https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Go to the `Wallets` menu.


![Image](assets/fr/15.webp)


Then select `Create / restore wallet...`. The `Open Wallet...` option lets you access a wallet already saved in Ashigaru Terminal at a later date.


![Image](assets/fr/16.webp)


Give your wallet a name.


![Image](assets/fr/17.webp)


Then choose wallet type `Hot Wallet`.


*Note*: the `Watch-only` option allows you to save the `xpub` of a wallet hardware in order to use the `Mix to` function at a later date. However, this type of wallet obviously cannot participate in coinjoins. We'll come back to this feature in detail in the next tutorial.


![Image](assets/fr/18.webp)


It is at this stage that the procedure differs depending on your initial choice:


- If you wish to create a new wallet from scratch, click on `<Generate New Wallet>`, define a passphrase BIP39, then carefully save your mnemonic phrase and your passphrase on a physical medium ;


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


- If you wish to use the same wallet as your Ashigaru application, enter the 12 words of your mnemonic phrase and your passphrase BIP39 directly into the corresponding fields. Write the words in lower case, whole, in order, separated by a space, without numbers or extra characters.


Once this step is complete, click `< Next >`.


*Note*: If you can't click this button, your mnemonic phrase is invalid. Check carefully that none of the words are incorrect or misspelled.


![Image](assets/fr/19.webp)


You'll then need to set a password. This will be used to unlock your Ashigaru Terminal wallet and protect it against unauthorized physical access. It is not involved in the cryptographic derivation of your keys: in other words, even without this password, anyone with your mnemonic phrase and passphrase will be able to restore your wallet and access your bitcoins.


Choose a long, complex, random password. Keep a copy in a safe place: ideally on a physical medium or in a secure password manager.


Click `< OK >` when you're finished.


![Image](assets/fr/20.webp)


## 5. Using the wallet


You can then choose which account to access. For the moment, we haven't initiated any mixes, so we'll access the `Deposit` account.


![Image](assets/fr/21.webp)


Operation is then identical to that of Sparrow, since Ashigaru Terminal is a fork of Sparrow Server. You'll find the same menus:


![Image](assets/fr/22.webp)



- transactions": allows you to consult the history of transactions linked to this account. In my case, some of them already appear, as I had made some with the Ashigaru application on this same wallet.


![Image](assets/fr/23.webp)



- receive`: generates a new, blank receipt address for placing satss in the deposit account.


![Image](assets/fr/24.webp)



- addresses`: displays a list of all your addresses, whether they belong to your account's internal or external chain.


![Image](assets/fr/25.webp)



- `UTXOs`: lists all your available UTXOs.


![Image](assets/fr/26.webp)



- `Settings`: gives access to your wallet *descriptor*. You can also consult your seed, adjust the *Gap Limit* or change the creation date of your wallet.


![Image](assets/fr/27.webp)


Now you know how to install and use Ashigaru Terminal. In the next tutorial, we'll look at how to create coinjoins with this software, and how to manage backgrounds in "*Postmix*", either via the Ashigaru application, or using the `Mix to` option.