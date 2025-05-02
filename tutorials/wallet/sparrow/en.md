---
name: Sparrow Wallet
description: Installing, configuring and using Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet is a self-custody Bitcoin wallet management software developed by Craig Raw. This open-source software is appreciated by bitcoiners for its many features and intuitive Interface.

There are two ways to use Sparrow:


- Like a hot wallet, where your private keys are stored on your PC.
- As a cold wallet manager, where private keys are held on a Hardware Wallet. In this mode, Sparrow only manipulates public wallet information, tracks funds, generates addresses, and builds transactions, but the Hardware Wallet signature is required to make these transactions valid. It can therefore replace applications such as Ledger Live or Trezor Suite.

Sparrow supports single-signature and multi-signature wallets, and enables fluid management of multiple wallets. For example, you can simultaneously control one wallet connected to a Ledger, another to a Trezor, and also have a hot wallet.

The software also offers advanced coin control features, allowing you to choose precisely which UTXOs to use in your transactions to optimize your confidentiality.

In terms of connection, Sparrow lets you connect to your own Bitcoin node, either remotely via an Electrum Server, or with Bitcoin Core. It's also possible to use a public node if you don't yet have your own. Remote connections are made via Tor.

## Install Sparrow Wallet

Go to [the official Sparrow Wallet download page](https://sparrowwallet.com/download/) and choose the software version that corresponds to your operating system.

![Image](assets/fr/01.webp)

It's important to check the integrity and authenticity of the software before installing it. If you don't know how to do this, you'll find a complete tutorial here :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Once Sparrow has been installed, you can skip the initial explanatory screens and go straight to the connection management screen.

![Image](assets/fr/02.webp)

![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)


![video](https://youtu.be/IThaolnDgSo)

## Connecting to the Bitcoin network

To interact with the Bitcoin network and broadcast your transactions, Sparrow must be connected to a Bitcoin node. There are three main ways to establish this connection:

- 🟡 Using a public node, i.e. connecting to a third-party node that allows such connections. If you don't have your own Bitcoin node, this option lets you get started with Sparrow quickly. However, the node you connect to will see all your transactions, which could compromise your confidentiality. Having control over your keys is essential, but having your own node is even better. So use this option only if you're just starting out, while being aware of the risks to your privacy.
- 🟢 Connecting to a Bitcoin Core node. If you have your own Bitcoin Core node, you can connect it to Sparrow Wallet, either locally if Bitcoin Core is installed on the same machine, or remotely.
- 🔵 Connection via an Electrum server. If your Bitcoin node is equipped with Electrs, as is the case with node-in-a-box solutions such as Umbrel or Start9, you can connect to it remotely from Sparrow.

**It is preferable to use a connection via Electrs or Bitcoin Core on your own node to reduce the need to trust a third party and optimize your confidentiality**

### Connect to a public node 🟡

Connecting to a public node is very simple. Click on the "*Public Server*" tab.

![Image](assets/fr/03.webp)

Select a node from the drop-down list.

![Image](assets/fr/04.webp)

Then click on "*Test Connection*".

![Image](assets/fr/05.webp)

Once connected, Sparrow Wallet will display a yellow tick in the bottom right-hand corner of Interface to indicate that you are connected to a public node.

![Image](assets/fr/06.webp)

### Connecting to a Bitcoin Core 🟢

The second method of connecting to a Bitcoin node is to link Sparrow to a Bitcoin Core. If Bitcoin Core is installed on the same machine, authentication will be via the cookie file. If Bitcoin Core is on a remote machine, you'll need to use the password defined in the `Bitcoin.conf` file.

Please note that if you use a pruned Bitcoin Core node, you won't be able to restore a wallet containing transactions predating the locally stored blocks. However, for a new wallet created on Sparrow, this won't be a problem: your new transactions will be visible, even with a pruned node.

To configure a Bitcoin Core node, you can consult one of the following tutorials, depending on your operating system:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

On Sparrow, go to the "*Bitcoin Core*" tab.

![Image](assets/fr/07.webp)

**With Bitcoin Core local:**

If Bitcoin Core is installed on your computer, locate the `Bitcoin.conf` file among the software files. If this file does not exist, you can create it. Open it with a text editor and insert the following line:

```ini
server=1
```

Then save your changes.

You can also do this via Bitcoin-QT's Interface graphic by navigating to "*Settings*" > "*Options...*" and activating the "*Enable RPC server*" option.

Don't forget to restart the software after making these changes.

![Image](assets/fr/08.webp)

Then return to Sparrow Wallet and enter the path to your cookie file, usually located in the same folder as `Bitcoin.conf`, depending on your operating system:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Leave the other parameters as default, URL `127.0.0.1` and port `8332`, then click on "*Test Connection*".

![Image](assets/fr/10.webp)

The connection is established. A green tick will appear in the bottom right-hand corner to indicate that you are connected to a Bitcoin Core node.

![Image](assets/fr/11.webp)

**With Bitcoin Core remote:**

If Bitcoin Core is installed on another machine connected to the same network, first locate the `Bitcoin.conf` file among the software files. If this file does not yet exist, you can create it. Open this file with a text editor and add the following line:

```ini
server=1
```

After editing the file, make sure you save it in the appropriate folder for your operating system:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

This operation can also be performed via the Bitcoin-QT Interface graphical interface. Go to the "*Settings*" menu, then "*Options...*", and activate the "*Enable RPC server*" option by checking the corresponding box. If the `Bitcoin.conf` file doesn't exist, you can create it directly from this Interface by clicking on "*Open Configuration File*".

![Image](assets/fr/12.webp)

Find the IP address of the machine hosting Bitcoin Core on your local network. To do this, you can use a tool such as [Angry IP Scanner](https://angryip.org/). Let's assume, for the sake of argument, that the IP address of your node is `192.168.1.18`.

In the `Bitcoin.conf` file, add the following lines, setting `rpcbind=192.168.1.18` to match the IP address of your node.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

In the `Bitcoin.conf` file, add a username and password for remote connections. Be sure to replace `loic` with your username and `my_password` with a strong password:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

After modifying and saving the file, restart the Bitcoin-QT software.

You can now return to Sparrow Wallet. Go to the "*User / Pass*" tab. Enter the username and password you configured in the `Bitcoin.conf` file. Leave the other parameters as default, i.e. URL `127.0.0.1` and port `8332`. Then click on "*Test Connection*".

![Image](assets/fr/15.webp)

The connection is established. A green tick will appear in the bottom right-hand corner to indicate that you are connected to a Bitcoin Core node.

![Image](assets/fr/16.webp)

![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)

### Connecting to an Electrum server 🔵

The final option for connecting is to use a remote Electrum server. This method lets you connect to your node via Tor from another device, and takes advantage of an indexer to browse your wallets on Sparrow more quickly. It's particularly suitable if you have a node-in-a-box solution like Umbrel or Start9, which allow you to install Electrs with a single click.

To do this, obtain the Tor `.onion' address of your Electrum server. With Umbrel, for example, you'll find it in the Electrs application.

![Image](assets/fr/17.webp)

On Sparrow Wallet, access the "*Private Electrum*" tab.

![Image](assets/fr/18.webp)

Enter your Tor address in the space provided. Other settings can remain default. Then click on "*Test Connection*".

![Image](assets/fr/19.webp)

The connection is confirmed. If you close this window, a blue tick will appear in the bottom right-hand corner, indicating that you are connected to an Electrum server.

![Image](assets/fr/20.webp)

## Create a hot wallet

Now that Sparrow Wallet is configured to communicate with the Bitcoin network, you're ready to create your first wallet. This section guides you through the creation of a hot wallet, i.e. a wallet whose private keys are stored on your computer. Since your computer is a complex machine connected to the Internet, it presents a very large attack surface. Consequently, a hot wallet should only be used for limited amounts of bitcoins. To store larger amounts, opt for a secure wallet with a Hardware Wallet. If this is what you're looking for, you can skip ahead to the next section.

To create a hot wallet, from the Sparrow Wallet home screen, click on the "*File*" tab and then on "*New Wallet*".

![Image](assets/fr/21.webp)

Enter a name for your wallet and click on "*Create Wallet*".

![Image](assets/fr/22.webp)

At the top of the Interface, you can choose whether to create a "*Single Signature*" or "*Multi Signature*" wallet. Just below, select the type of script to lock your UTXOs. I recommend you use the latest standard: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Then click on "*New or Imported Software Wallet*".

![Image](assets/fr/24.webp)

Choose the BIP39 standard, as it is supported by virtually all Bitcoin wallet software. Next, choose the length of your recovery phrase. Currently, a 12-word phrase is sufficient, as both offer similar security, but the 12-word phrase is simpler to save.

![Image](assets/fr/25.webp)

Click on the "*generate New*" button to generate your wallet's mnemonic phrase. This phrase gives full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to your computer.

The 12-word phrase restores access to your bitcoins in the event of loss, theft or breakage of your computer. It is therefore very important to save it carefully and store it in a safe place.

You can inscribe it on paper or, for added security, engrave it on stainless steel to protect it from fire, flood or collapse. The choice of medium for your mnemonic will depend on your security strategy, but if you're using Sparrow as a warm spending wallet containing moderate amounts, paper should be sufficient.

For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
![Image](assets/fr/26.webp)

**Obviously, you must never share these words on the Internet, as I do in this tutorial. This example wallet will be used only on the Testnet and will be deleted at the end of the tutorial.**

You can also choose to add a passphrase BIP39 by clicking on the "*Use passphrase*" box. Warning: using a passphrase can be very useful, but if you don't understand how it works, it can be very risky. That's why I strongly advise you to read this short theoretical article on the subject:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Once you've saved your mnemonic and any passphrase to a physical medium, click on "*Confirm Backup*".

![Image](assets/fr/27.webp)

Re-enter your 12 words to confirm that they have been saved correctly, then click on "*Create Keystore*".

![Image](assets/fr/28.webp)

Then click on "*Import Keystore*" to generate your wallet keys from the mnemonic phrase.

![Image](assets/fr/29.webp)

Click on "*Apply*" to finalize wallet creation.

![Image](assets/fr/30.webp)

Set a strong password to secure access to your Sparrow wallet. It's a good idea to keep this password in a password manager, so you don't forget it. Note that this password plays no part in the derivation of your keys. It is only used to access your wallet via Sparrow Wallet. So, even without this password, your mnemonic phrase will suffice to access your bitcoins from any BIP39-compatible application.

![Image](assets/fr/31.webp)

Your hot wallet is now created. You can skip to the *Receiving Bitcoins* section of this tutorial if you don't plan to use a Hardware Wallet with Sparrow.

## Managing a cold wallet

The second way to use Sparrow Wallet is to set it up as a wallet manager with a Hardware Wallet. In this configuration, the private keys of your Bitcoin wallet remain exclusively on the Hardware Wallet, while Sparrow only accesses the public information. This approach offers a higher level of security than the hot wallets discussed above, as the private keys are kept on a specialized device, often with a secure chip, which is not connected to the Internet and therefore presents a much smaller attack surface than a traditional computer.

There are two main ways to connect your Hardware Wallet to Sparrow:


- By cable, commonly used with entry-level models such as Trezor Safe 3 or Ledger Nano S Plus ;
- In Air-Gap mode, i.e. without a direct wired connection, via a MicroSD card or QR code exchange.

Sparrow supports all these communication methods and is compatible with most hardware wallets on the market.

For this tutorial, I'll be using a Ledger Nano S with a cable, but the procedure is similar in Air-Gap mode. You'll find details specific to your Hardware Wallet in its dedicated tutorial on Plan ₿ Network.

Before starting, make sure that the wallet is already configured on your Hardware Wallet. If you're using a wired connection, connect it to your computer via the cable.

To import the so-called "*Keystore*" (the public information needed to manage the wallet) into Sparrow Wallet, click on the "*File*" tab, then on "*New Wallet*".

![Image](assets/fr/32.webp)

Name your wallet and click on "*Create Wallet*". I advise you to enter the name of your Hardware Wallet to identify it easily later.

![Image](assets/fr/33.webp)

At the top of the Interface, choose between a "*Single Signature*" or "*Multi Signature*" wallet. For our example, we'll configure a single-sig wallet.

Just below, select the type of script to lock your UTXOs. If your Hardware Wallet supports it, I suggest you choose "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Next, the procedure differs according to your connection method. If you're using an Air-Gap method, select "*Airgapped Hardware Wallet*". Then follow the instructions specific to your device.

![Image](assets/fr/35.webp)

If you're using a cable connection, as in my case, choose "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Click on "*Scan*" to have Sparrow detect your device. Make sure it's plugged in and unlocked. For some models, such as the Ledger, you'll need to open the "*Bitcoin*" application to enable detection.

![Image](assets/fr/37.webp)

Select "*Import Keystore*".

![Image](assets/fr/38.webp)

Click on "*Apply*" to finalize wallet creation.

![Image](assets/fr/39.webp)

Set a strong password to secure access to your Sparrow wallet. This password will protect your public keys, addresses and transaction history. We recommend that you save it in a password manager. Note that this password plays no part in the derivation of your keys. Even without it, you can recover access to your bitcoins with your mnemonic via any BIP39-compatible software.

![Image](assets/fr/40.webp)

Your management wallet is now configured on Sparrow.

![Image](assets/fr/41.webp)

## Receive bitcoins

Now that your wallet is set up on Sparrow, you can receive bitcoins. Simply access the "*Receive*" menu.

![Image](assets/fr/42.webp)

Sparrow will display the first unused address in your wallet. You can add a "*Label*" to this address to remind you of the origin of these satoshis in the future.

![Image](assets/fr/43.webp)

If you're using a hot wallet, the address displayed can be used immediately, either by copying it or by scanning the associated QR code.

If you're using a Hardware Wallet, it's very important to check the address on the device screen before using it. For wired devices, connect and unlock your Hardware Wallet, then in Sparrow, click on "*Display Address*". Make sure that the address displayed on your Hardware Wallet matches that shown on Sparrow.

![Image](assets/fr/44.webp)

For Hardware Wallet Air-Gap users, address verification varies according to device model. See the dedicated Plan ₿ Network tutorial for precise instructions.

Once the transaction has been broadcast by the payer, you'll see it appear in the "*Transactions*" tab. You can click on it for more details, such as the txid.

![Image](assets/fr/45.webp)

In the "*Addresses*" tab, you'll find a list of all your inbox addresses. You can see if they've already been used and if a label has been added. *Receive*" addresses are those Sparrow shows when you click on "*Receive*" and are intended for incoming payments. The "*Change*" addresses are used for exchange in your transactions, i.e. to recover the unused portion of your UTXOs in inputs.

![Image](assets/fr/46.webp)

The "*UTXOs*" tab shows you all your UTXOs, i.e. the bitcoin fragments you hold. You can see the amount of each UTXO and the associated label.

![Image](assets/fr/47.webp)

## Send bitcoins

Now that you have a few satoshis in your wallet, you also have the option of sending some. Although there are several ways of doing this, I recommend that you use the "*UTXOs*" menu for more precise control over the coins you spend (*coin control*), rather than going directly to the "*Send*" menu (although the latter may suffice if you're a beginner).

![Image](assets/fr/48.webp)

Select the UTXOs you wish to use as inputs for this transaction, then click on "*Send Selected*". This approach allows you to select the most appropriate sources among your UTXOs, according to your expenses and the labels applied when they are received, in order to optimize the confidentiality of your payments. Make sure that the sum of the selected UTXOs is greater than the amount you wish to send.

![Image](assets/fr/49.webp)

Enter the recipient's address in the "*Pay to*" field. You can also scan the address with your webcam by clicking on the camera icon. The "*+Add*" button lets you pay multiple addresses in a single transaction.

![Image](assets/fr/50.webp)

Add a label to your transaction to remind you of its purpose. This label will also be associated with your eventual exchange.

![Image](assets/fr/51.webp)

Enter the amount to be sent to this address.

![Image](assets/fr/52.webp)

Adjust the fee rate according to current market conditions. You can do this by entering an absolute fee value or by adjusting the fee rate with the slider.

![Image](assets/fr/53.webp)

At the bottom of the Interface, you can choose between "*Efficiency*" and "*Privacy*". In my case, the "*Privacy*" option is not available, as I only have one UTXO in this wallet. "*Efficiency*" corresponds to a classic transaction, while "*Privacy*" is a Stonewall-type transaction, a transaction structure that reinforces your confidentiality by simulating a mini-CoinJoin, which makes chain analysis more complex.

![Image](assets/fr/54.webp)

Sparrow displays a summary diagram showing your inputs, outputs and transaction fees (note that fees are not actually an output, contrary to what this diagram suggests). If you're happy with everything, click on "*Create Transaction*".

![Image](assets/fr/55.webp)

This takes you to a page detailing the elements of your transaction. Check that all the information is correct, then click on "*Finalize Transaction for Signing*".

![Image](assets/fr/56.webp)

It's important to keep the default Sighash. To understand why, take a look at this training course, in which I explain everything you need to know about Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
On the next screen, the options vary according to the type of wallet you are using:


- For a Hardware Wallet Air-Gap, click on "*Show QR*" to display a PSBT that you can sign with your device, then load the signed PSBT into Sparrow using "*Scan QR*". The "*Save Transaction*" option works in a similar way, but with exchanges on a microSD ;
- For a hot wallet, simply click on "*Sign*" and enter the wallet password to sign ;
- For a wired Hardware Wallet, also click on "*Sign*" to send the unsigned transaction to your device.

![Image](assets/fr/57.webp)

On your Hardware Wallet, check the recipient's address, the amount sent and the charges. If everything is correct, proceed with the signature.

Once the transaction has been signed, it will reappear in Sparrow, ready to be broadcast on the Bitcoin network for subsequent inclusion in a block. If everything is correct, click on "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Your transaction is now broadcast and awaiting confirmation.

![Image](assets/fr/59.webp)

![video](https://youtu.be/7QCKSPIq0Ac)

## Managing and configuring wallets on Sparrow

In the "*Settings*" tab, you will find detailed information on your wallet, such as :

- Portfolio type (single-sig or multi-sig) ;
- Type of script used ;
- The name you have assigned to the wallet ;
- Master key imprint;
- The bypass path ;
- The account's extended public key.

![Image](assets/fr/60.webp)

The "*Export*" button allows you to export your wallet information so that you can use it in other software while retaining the information set up in Sparrow.

The "*Add Account*" button lets you add an additional account to your wallet. An account corresponds to a separate set of inbox addresses. This feature can be useful, for example, if you wish to separate a personal and a business account, with a single mnemonic phrase.

The "*Advanced*" button gives access to advanced settings, such as customizing Sparrow's address search and changing the wallet password.

![Image](assets/fr/61.webp)

When you close Sparrow Wallet, your wallet locks automatically. The next time you open the software, a window will prompt you to unlock your wallet with its password.

![Image](assets/fr/62.webp)

If this window does not open, or if you wish to open another wallet on Sparrow, click on the "*File*" tab and select "*Open Wallet*".

![Image](assets/fr/63.webp)

This will open your File Manager to the folder where Sparrow stores your wallets. Simply select the wallet you wish to open and enter the password to unlock it.

![Image](assets/fr/64.webp)

In the "*File*" menu under "*Settings*", you'll find the Bitcoin network connection parameters already explored in previous sections. You can also adjust various parameters such as the unit used, fiat currency for conversions, and information sources.

![Image](assets/fr/65.webp)

The "*View*" tab offers customization options and access to some useful commands, such as "*Refresh Wallet*", which refreshes the transaction search for your wallet.

![Image](assets/fr/66.webp)

The "*Tools*" tab groups together several advanced tools, including :

- "*Sign/Verify Message*" allows you to prove possession of a receiving address or verify a signature.
- "*Send To Many*" offers a simplified Interface for performing transactions to multiple receiving addresses at once, which is convenient for batch spending.
- "*Sweep Private Key*" allows you to retrieve bitcoins secured by a simple private key and transfer them to your Sparrow wallet. This can be particularly useful for those with bitcoins dating back to the early 2010s, before the era of HD wallets.
- "Verify Download" verifies the integrity and authenticity of downloaded software before installing it on your device.
- "*Restart In*" allows you to switch to your wallets on Testnet or Signet networks. This can be useful if you wish to access test networks with coins of no real value.

![Image](assets/fr/67.webp)

You now know all about Sparrow Wallet software, an excellent tool for managing your Bitcoin wallets on a daily basis.

If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Feel free to share it on your social networks. Thank you very much!

I also recommend this other tutorial in which I explain how to configure the Hardware Wallet COLDCARD Q with Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3