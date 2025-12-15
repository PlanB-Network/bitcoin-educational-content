---
name: Satochip x SeedSigner
description: How to use a Satochip with your SeedSigner?
---

![cover](assets/cover.webp)


*Thanks to [Crypto Guide](https://www.youtube.com/@CryptoGuide/) for its fork of the SeedSigner firmware for smartcard support, which we will use in this tutorial


---

The Satochip is a wallet smart card-format hardware with an EAL6+ certified security element, one of the highest security standards. It is designed and produced by the Belgian company of the same name: Satochip.


Priced at around €25, the Satochip stands out from the competition for its excellent value for money. Thanks to its secure chip, it offers resistance to physical attacks. What's more, its applet source code is entirely open-source, licensed under *AGPLv3*.


On the other hand, its format imposes certain functional limitations. The main drawback of the Satochip is the absence of an integrated screen: users must therefore sign transactions blindly, relying solely on their computer's display.


To overcome this weakness, a particularly interesting configuration is to use it in conjunction with a SeedSigner. In this setup, communication no longer takes place directly between the computer and the Satochip, but via QR code exchanges between the computer and the SeedSigner. The SeedSigner then acts as a trust screen: it displays the information to be signed, while the signature itself is performed by the Satochip. Unlike conventional SeedSigner use (or even use in combination with Seedkeeper), the seed is never loaded into the SeedSigner. The SeedSigner thus becomes the Satochip's screen, eliminating the risks associated with blind signing.


If we look at the problem the other way round, using the SeedSigner with a Satochip fills a major gap in the SeedSigner: the ability to store and use the seed within a secure element.


In my opinion, this configuration offers several advantages over conventional hardware wallets:


- The Satochip costs around €25, and since the applet is open-source, you can install it yourself on a blank smartcard. You then need to add the cost of the SeedSigner components and the extension for reading smartcards: depending on where you buy this hardware, the total should be between €70 and €100.
- All the software involved in the setup is open-source: the SeedSigner firmware and the Satochip applet.
- You benefit from a certified security element.
- The configuration can be carried out entirely DIY, without recourse to hardware explicitly intended for Bitcoin use, which can provide a form of plausible deniability and resistance to certain external threats (including, depending on the country, state pressure). This is also an interesting solution if access to commercial hardware wallets is restricted or impossible in your region.



## 1. Materials required


To carry out this setup, you will need the following items:


- The usual equipment needed by a classic SeedSigner :
 - a Raspberry Pi Zero with GPIO pins,
 - 1.3" Waveshare screen,
 - a compatible camera,
 - a microSD card.


![Image](assets/fr/01.webp)



- The SeedSigner extension kit, available [from the official Satochip store](https://satochip.io/product/seedsigner-extension-kit/), which lets you read and write to a smartcard directly from your SeedSigner. Another option is to use [an external smartcard reader](https://satochip.io/product/chip-card-reader/), which can be connected by cable to a Micro-USB port on the Raspberry Pi. However, I haven't tested this solution myself;
- [A Satochip](https://satochip.io/product/satochip/), or alternatively a [blank smartcard](https://satochip.io/product/card-for-diy-project/) on which to install the Satochip applet (the extension kit sold by Satochip already includes a blank smartcard). Satochip's extension kit also supports the [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/) format. So you can opt for this format if you prefer.


![Image](assets/fr/02.webp)


For more details on the equipment required to assemble a SeedSigner, please refer to Part 1 of this other tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Install firmware


To use your SeedSigner with a Satochip, you need to install an alternative firmware, different from that of the original SeedSigner, in order to support smart card reading. For this, [I recommend using fork from "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Download [the latest version of the image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) corresponding to the Raspberry Pi model you're using.


![Image](assets/fr/03.webp)


If you don't already have it, download the [Balena Etcher] software (https://etcher.balena.io/), then proceed as follows:


- Insert the microSD card into your computer;
- Launch Etcher ;
- Select the `.zip` file you have just downloaded;
- Select the microSD card as the target;
- Click on `Flash!`.


![Image](assets/fr/04.webp)


Wait until the process is complete: your microSD is now ready for use. You can now move on to assembling your device.


For more details on firmware installation and software verification (a step I strongly recommend you take), see the following tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Assembling the smartcard reader


Start by installing the camera on the Raspberry Pi Zero, carefully inserting it into the camera pin and locking it with the black tab. Then place the Pi on the bottom of the case, making sure to align the ports with the corresponding openings.


![Image](assets/fr/05.webp)


Then attach the smart card reader to the Raspberry Pi Zero's GPIO pins.


![Image](assets/fr/06.webp)


Slide the plastic cover over the smart card reader until it is correctly positioned.


![Image](assets/fr/07.webp)


Then add the screen to the extension's GPIO pins.


![Image](assets/fr/08.webp)


Finally, insert the microSD card containing the firmware into the side port on the Raspberry Pi Zero.


![Image](assets/fr/09.webp)


You can now connect your SeedSigner either via the Raspberry Pi Zero's Micro-USB port, or via the extension's USB-C port. Both options work. Wait a few seconds for startup, then you should see the welcome screen appear.


![Image](assets/fr/10.webp)


For more details on the initial setup of your SeedSigner, I recommend that you consult part 4 of the following tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flash a smartcard with the Satochip applet (optional)


If you already own a Satochip, you can skip this step and go straight to step 4. In this section, we'll look at how to install the Satochip applet on a blank smartcard (DIY method). The applet is simply a small program running on the smartcard that enables us to manage specific functions.


To get started, open the `Tools > Smartcard Tools` menu on your SeedSigner.


![Image](assets/fr/11.webp)


Then select `DIY Tools > Install Applet`.


![Image](assets/fr/12.webp)


Insert your smartcard into the SeedSigner reader, with the chip facing down, and select the `Satochip` applet.


![Image](assets/fr/13.webp)


Please be patient during installation: the process may take several tens of seconds.


![Image](assets/fr/14.webp)


Once the applet has been successfully installed, you can proceed to step 4.


![Image](assets/fr/15.webp)



## 5. Creating and saving seed


### 5.1. Generate seed


Now that you've got all your hardware and software working properly, you can proceed to create your Bitcoin wallet. To do this, plug in your SeedSigner, then generate your seed as with a conventional SeedSigner, either by rolling the dice or by taking a photo:


- Go to the `Tools > Camera / Dice Rolls` menu;
- Then follow the entropy generation process according to the chosen method;
- Finally, back up the seed on physical media and check the backup carefully.


![Image](assets/fr/16.webp)


If you would like to see the details of this procedure, please follow part 5 of this tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Saving the seed on a Seedkeeper


Once the seed has been generated, this is the only time it resides in the SeedSigner's RAM. In my case, I want to save it on a [Seedkeeper](https://satochip.io/product/seedkeeper/), another Satochip product designed to store secrets. I'll use this device as a last resort, in case of loss of my Satochip.


The backup strategy chosen here depends on your preferences, but it's imperative to have at least one copy of your mnemonic phrase, either on physical media (paper or metal) or, as here, in a Seedkeeper. You can also multiply the number of backups as required. For more information on wallet backup strategies, I suggest you read this tutorial :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

To back up your seed on a Seedkeeper, go directly to the `Backup Seed` menu.


![Image](assets/fr/17.webp)


Then insert your Seedkeeper into the smart card reader, and select `To SeedKeeper`.


![Image](assets/fr/18.webp)


Enter your PIN to unlock it.


![Image](assets/fr/19.webp)


Choose a `Label` to easily identify your different secrets stored on Seedkeeper. You can, for example, simply keep the wallet imprint or explicitly indicate `Seed`. The choice depends on your preference and risk.


![Image](assets/fr/20.webp)


If your backup strategy relies solely on this Seedkeeper, I strongly recommend that you run an empty recovery test now, then compare the fingerprints to check that the backup is working.


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

The Seedkeeper PIN code should be as long and random as possible, to prevent brute force attempts in the event of physical compromise of the card. You should also keep a backup copy of this PIN code, stored in a separate location from Seedkeeper. Without this PIN, you won't be able to access the mnemonic stored in Seedkeeper, and your bitcoins will be permanently lost.


### 5.3. Save seed on the Satochip


Now that your wallet has been generated, saved and verified, we'll transfer it to the Satochip. To do this, make sure the seed is loaded into the SeedSigner's RAM. Then go to `Tools > Smartcard Tools > Satochip Functions`.


![Image](assets/fr/21.webp)


Insert your Satochip in the smart card reader, then select `Initialise with Seed`.


![Image](assets/fr/22.webp)


The device prompts you to enter the Satochip PIN code; as the card is new and uninitialized, no PIN exists yet. Enter any code to skip this step (it's not a blocking one).


![Image](assets/fr/23.webp)


The SeedSigner detects that your Satochip has not been initialized. Click `I Understand` to confirm.


![Image](assets/fr/24.webp)


You can then set the Satochip PIN code, from 4 to 16 characters. To reinforce your wallet's security, choose a long, random code: it's the only protection against physical access to your mnemonic phrase.


Remember to save this PIN as soon as it is created, either in a secure password manager or on a physical medium, depending on your personal strategy. In the latter case, be sure never to store the medium containing the PIN in the same place as your Satochip, otherwise protection will become useless. It's important to have a backup copy: **Without this PIN, you won't be able to access your seed, and your bitcoins will be lost forever**.


![Image](assets/fr/25.webp)


The SeedSigner then asks you which seed to import into the Satochip. Select the one whose fingerprint matches the wallet you've just created.


![Image](assets/fr/26.webp)


Your seed is now imported into the Satochip.


![Image](assets/fr/27.webp)


You can now switch off your SeedSigner.


If you would like to use a passphrase BIP39 to enhance the security of your wallet, please see part 6 of this tutorial:


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Import wallet into Sparrow


Now that your wallet is up and running, we'll import its public information (the "*keystore*") into Sparrow Wallet or another wallet management software. This software will be used to create, distribute and track your transactions. However, it won't be able to sign them, as only the Satochip (and any backups) hold the private keys needed for this operation.


### 6.1 Preparing the SeedSigner and Satochip


Insert the microSD card containing the operating system, then switch on your SeedSigner. For the moment, it can't do anything, as it doesn't yet know your seed. You'll have to start by inserting the Satochip into the smart card reader, since it's the one that holds your seed.


From the Home screen, access the `Tools > Smartcard Tools > Satochip Functions` menu.


![Image](assets/fr/28.webp)


Then click on `Export Xpub`.


![Image](assets/fr/29.webp)


Select the wallet type. In our case, it's a single wallet: select `Single Sig`.


![Image](assets/fr/30.webp)


Next comes the choice of scripting standard. Choose the latest: `Native SegWit`.


![Image](assets/fr/31.webp)


Finally, select the `Coordinator`, i.e. the wallet management software you wish to use. Here, we'll be using Sparrow Wallet.


![Image](assets/fr/32.webp)


A warning message appears: this is perfectly normal. The extended public key (`xpub`) allows you to view all the addresses derived from your seed (on the first account). It does not, however, give access to your funds: its disclosure would compromise your privacy, but not the security of your bitcoins. In other words, it allows you to observe your balances, but not to spend them.


Click on `I Understand`.


![Image](assets/fr/33.webp)


Then enter your Satochip's PIN code to unlock it. This is the code you defined and saved in step 5.


![Image](assets/fr/34.webp)


Finally, click on `Export Xpub` if you are satisfied with the information displayed.


![Image](assets/fr/35.webp)


The SeedSigner then generates your xpub in the form of a dynamic QR code, containing all the data you need to manage your wallet in Sparrow Wallet. You can adjust the brightness of the screen using the joystick to make scanning the QR code easier.


### 6.2 Importing a new wallet into Sparrow Wallet


Make sure that the Sparrow Wallet software is installed on your computer. If you don't know how to download it, check its authenticity and install it correctly, see our full tutorial on the subject :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

On your computer, open Sparrow Wallet, then in the menu bar, click `File → Import Wallet`.


![Image](assets/fr/36.webp)


Scroll down to `SeedSigner`, then select `Scan...`. Your webcam will be activated: scan the dynamic QR code displayed on your SeedSigner screen.


![Image](assets/fr/37.webp)


Assign a name to your wallet, then click on `Create Wallet`. Sparrow will then ask you to set a password to lock local access to this wallet. Choose a strong password: it protects your data in Sparrow (public keys, addresses, labels and transaction history). However, this password is not required to restore the wallet in the future: only your mnemonic phrase (and possibly your passphrase) will be.


I recommend that you save this password in a password manager, to avoid losing it.


![Image](assets/fr/38.webp)


Your keystore has been successfully imported.


![Image](assets/fr/39.webp)


Now check that the `Master fingerprint` displayed in Sparrow Wallet matches the one previously found on your SeedSigner.


The SeedSigner will then ask you to scan a random receiving address from your Sparrow wallet to confirm the validity of the import.


![Image](assets/fr/40.webp)


Your Satochip (via SeedSigner) and Sparrow Wallet are now securely connected. Sparrow acts as a complete management interface, while the Satochip remains the only device capable of signing your transactions. You're now ready to receive and send bitcoins in a totally air-gapped configuration.


![Image](assets/fr/41.webp)


## 7. Receiving and sending bitcoins


Your Satochip and Sparrow Wallet are now configured to work together. In this section, we'll explain step by step how to receive and send bitcoins in this mode.


### 7.1 Receiving bitcoins


#### 7.1.1 Generating a reception address


On your computer, open Sparrow Wallet and unlock your `Satochip-SeedSigner` wallet using your password. Check that the software is connected to a server (indicator at bottom right). Then, in the sidebar, click on `Receive`.


![Image](assets/fr/42.webp)


A new Bitcoin address appears. You will find :


- The address in text format (starting with `bc1q...` if you're using P2WPKH, as in this example) ;
- The associated QR code ;
- A `Label` field, useful for tracing your transactions.


I strongly recommend that you add a label to each bitcoin receipt in your wallet. This will help you easily identify the provenance of each UTXO and better manage your privacy. To find out more about this important subject, check out the dedicated training on Plan ₿ Academy :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

To add a label, simply enter a name in the `Label` field, then confirm.


For example:


```txt
Label : Sale of the Raspberry Pi Zero
```


Your address is now associated with this label in all Sparrow sections.


![Image](assets/fr/43.webp)


#### 7.1.2 Address verification on the SeedSigner


Before communicating your receiving address to the payer, it is important to check that it belongs to your seed. This step ensures that your Satochip will then be able to sign transactions associated with this address. It also prevents potential attacks where Sparrow would display a fraudulent address. Bear in mind that Sparrow runs on an insecure environment (your computer), whose attack surface is far greater than that of your Satochip, which is totally isolated. This is why you should never blindly trust the addresses displayed in Sparrow before checking them on your wallet hardware.


In Sparrow, click on the QR code of the address to enlarge it: it will then be displayed full-screen.


![Image](assets/fr/44.webp)


On your SeedSigner, insert the Satochip into the reader, then from the main menu, select `Scan`. Scan the QR code displayed on your computer, then select `Use Satochip card`.


![Image](assets/fr/45.webp)


Then confirm the type of script used (in this case, `Native SegWit`), enter the Satochip PIN code to unlock it, and validate the `xpub` information.


![Image](assets/fr/46.webp)


If the scanned address matches the one derived from your seed, the SeedSigner will display the message: `Address Verified`.


![Image](assets/fr/47.webp)


You can then be sure that the address belongs to your wallet.


#### 7.1.3 Receipt of funds


You can now transmit this address in text form or via its QR code to the person or department who needs to send you satss. Once the transaction has been broadcast on the network, it will appear in the `Transactions` tab of Sparrow Wallet.


![Image](assets/fr/48.webp)


### 7.2 Send bitcoins


Sending bitcoins with the Satochip-SeedSigner configuration involves 3 steps:


- Transaction creation in Sparrow ;
- Signing this transaction on the Satochip, via the SeedSigner ;
- Finally, the transaction is broadcast over the network from Sparrow.


All exchanges between the two devices take place exclusively via QR codes.


#### 7.2.1 Creating the transaction in Sparrow


In Sparrow Wallet, you can create a transaction by clicking on the `Send` tab in the left-hand sidebar. However, I prefer to use the `UTXOs` tab, which allows you to practice *Coin Control*. This method offers precise control over the UTXOs spent, to limit the information revealed during your transactions.


In the `UTXOs` tab, select the coins you wish to spend, then click `Send Selected`.


![Image](assets/fr/49.webp)


Then fill in the transaction fields:


- In `Pay to`, paste the recipient's address or scan their QR code using the camera icon ;
- In `Label`, add a label to trace this expense;
- In `Amount`, enter the amount to be sent;
- Finally, choose the charge rate according to current network conditions (estimates are available at [mempool.space](https://mempool.space/)).


Once you have completed all the fields, review the information carefully, then click on `Create Transaction >>`.


![Image](assets/fr/50.webp)


Check the transaction details one last time for accuracy, then click on `Finalize Transaction for Signing`.


![Image](assets/fr/51.webp)


The transaction is now ready, but has not yet been signed. To display the [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) as a QR code, click on `Show QR`.


![Image](assets/fr/52.webp)


#### 7.2.2 Signing the transaction with Satochip


Switch on your SeedSigner and insert your Satochip as usual. From the home screen, select `Scan`, then scan the QR code displayed on Sparrow.


![Image](assets/fr/53.webp)


Select the `Use Satochip card` option.


![Image](assets/fr/54.webp)


Enter your PIN code to unlock the smartcard.


![Image](assets/fr/55.webp)


The SeedSigner detects that this is a PSBT and displays a summary of the transaction:


   - The amount sent,
   - Destination addresses,
   - Associated transaction costs.


Click on `Review Details` and scrutinize all the information directly on the SeedSigner screen. The most important points to check are the amounts sent, the destination addresses and the transaction fees.


![Image](assets/fr/56.webp)


If all is in order, select `Approve PSBT` to sign the transaction using the Satochip.


![Image](assets/fr/57.webp)


Once the signature is complete, the SeedSigner generates a new QR code containing the signed transaction, ready to be scanned by Sparrow.


#### 7.2.3 Broadcasting the transaction from Sparrow


Now that the transaction is signed and validated, all that remains is to broadcast it on the Bitcoin network so that a miner can include it in a block. In Sparrow, click on `Scan QR`.


![Image](assets/fr/58.webp)


Present the QR code displayed on your SeedSigner (the one containing the signed transaction) to the webcam. Sparrow will then display all the transaction details. Check that all the information is correct, then click on "Broadcast Transaction" to broadcast it on the Bitcoin network.


![Image](assets/fr/59.webp)


Your transaction is now transmitted to the network. You can follow its confirmation in the `Transactions` tab of Sparrow Wallet.


![Image](assets/fr/60.webp)


## 8. Get your wallet back


As we have seen in the previous sections, depending on your security strategy, there are several ways of backing up your recovery phrase in addition to your Satochip :


- Using a classic *SeedQR* with the SeedSigner ;
- By recording the mnemonic phrase on a physical medium;
- Or by storing it on a Seedkeeper, as explained in section 5.2.


In any case, there are 2 main situations in which you need to intervene: loss of the Satochip or loss of the SeedSigner. Let's take a look at how to react in each of these scenarios.


### 8.1. Retrieve your wallet with Satochip


If you still have your Satochip but your SeedSigner is broken or lost, the situation is fairly simple to manage, since your wallet is still in the Satochip.


The best option is to recommend the necessary components and rebuild a new SeedSigner from scratch. As this is a "stateless" device, it doesn't matter whether you're using the same or another SeedSigner: as long as you can insert your Satochip, everything will work normally.


If you don't want to rebuild one, you can also use your Satochip in the classic way, i.e. directly from your computer, without going through the SeedSigner. This method works perfectly, but it considerably reduces the security of your Bitcoin wallet: you lose the "*air-gapped*" isolation and must now sign blind, since the SeedSigner acted as a trusted screen. However, this can be a temporary solution in an emergency, or if you are unable to rebuild a SeedSigner.


To do this, you'll need a USB smart card or NFC reader. Open the wallet you wish to restore in Sparrow, then go to the `Settings` tab and click `Replace`.


![Image](assets/fr/61.webp)


Insert your Satochip in the smart card reader connected to the computer, then click on `Import` next to `Satochip`.


![Image](assets/fr/62.webp)


Finally, enter your smartcard PIN to unlock it. You'll then be able to access your wallet, create transactions and sign them directly using the connected Satochip.


### 8.2. Retrieve your wallet with SeedSigner


The other, more delicate scenario is when you lose access to your Satochip containing the seed: whether it's broken, lost, stolen, or you've forgotten its PIN code. If your Satochip has been stolen or mislaid, we strongly recommend that, once access to your funds has been restored, you immediately transfer your bitcoins to a brand new wallet, generated with a different seed. This ensures that a potential attacker can never gain access to your satss.


To regain access to your wallet and move your funds, simply load your seed into SeedSigner. Depending on the backup media you used, you have several options:



- Enter your mnemonic phrase manually in the `Seeds > Enter 12-word seed` menu.


![Image](assets/fr/63.webp)



- Scan your *SeedQR* by clicking on the `Scan` button on the home page.


![Image](assets/fr/64.webp)



- Or load your seed from a Seedkeeper, via the `Seeds > From SeedKeeper` menu (this is the method I'm using in this tutorial). You'll simply need to enter the Seedkeeper PIN and select the secret to be used as seed on the SeedSigner.


![Image](assets/fr/65.webp)


Once the seed has been loaded into the SeedSigner, whichever method you use, you'll be able to sign one or more scan transactions to move your bitcoins to a new, uncompromised wallet. To find out how to do this, see part 7.2 of the following tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Now you know how to use Satochip to manage your Bitcoin wallet securely in combination with SeedSigner.


If this setup has convinced you, don't hesitate to support the projects that make it possible:


- By purchasing your equipment directly [on the Satochip website](https://satochip.io/shop/);
- By making [a donation to the SeedSigner project](https://seedsigner.com/donate/);
- By subscribing to [Crypto Guide's YouTube channel](https://www.youtube.com/@CryptoGuide/), run by the person who maintains the GitHub repository hosting the modified firmware we used in this tutorial.