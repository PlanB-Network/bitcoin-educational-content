---
name: Seedkeeper x SeedSigner
description: How do I use Seedkeeper with my SeedSigner?
---

![cover](assets/cover.webp)


*Thanks to the [Satochip](https://satochip.io/) team for agreeing to reuse [their videos](https://www.youtube.com/@satochip/videos) in this tutorial. Thanks also to [Crypto Guide](https://www.youtube.com/@CryptoGuide/) for its fork of the SeedSigner firmware, enabling support for smartcards


---

The SeedSigner is a wallet hardware that you assemble yourself from standard hardware, usually around a Raspberry Pi Zero. This wallet is called "*stateless*": unlike most other models on the market (Coldcard, Trezor, Ledger, etc.), it doesn't store any data in permanent memory, and operates only live from RAM. As a result, your portfolio's seed is never stored on the SeedSigner. Each time you restart, you'll need to fill it in to enable the device to sign your transactions. The most common method is to save your seed as a QR code, which you then scan each time you use it (*SeedQR*).


This approach does, however, present a significant risk: the seed must remain accessible in clear text so that it can be scanned. In the event of theft or intrusion, an attacker could easily get hold of it and steal your bitcoins.


To overcome this weakness, SeedSigner can be combined with [**Seedkeeper**](https://satochip.io/product/seedkeeper/), a smart card developed by Satochip. This enables mnemonic phrases (or other secrets) to be stored in a secure element protected by a PIN code. The Seedkeeper applet is open-source, and its secure element has EAL6+ certification. Used in conjunction with SeedSigner, it offers a very interesting security feature: your keys remain managed entirely off-line, you sign your transactions on a trusted screen, and the seed is physically protected in a smartcard resistant to physical attack.


All you need to complete the installation are the following items:


- The usual equipment needed for a classic SeedSigner: a Raspberry Pi Zero, a Waveshare 1.3" screen, a compatible camera and a microSD card (you'll find more details in the SeedSigner tutorial below);
- The SeedSigner extension kit, available [on the official Satochip store](https://satochip.io/product/seedsigner-extension-kit/), which lets you read and write to the smartcard directly from your SeedSigner. Another option is to use an external smartcard reader, which can be connected by cable to a Micro-USB port on the Raspberry Pi. However, I haven't tested this solution myself;
- A Seedkeeper, or alternatively a blank smartcard on which to install the Seedkeeper applet (the extension kit sold by Satochip already includes a blank smartcard).


![Image](assets/fr/01.webp)


This tutorial covers two scenarios:


- If you already have a Bitcoin portfolio managed via your SeedSigner, simply install the new firmware. You can then continue to use your existing wallet, this time using Seedkeeper for added security.
- If you don't yet have a Bitcoin wallet associated with your SeedSigner, you'll need to follow steps **5** and **6** of the tutorial mentioned below. These sections explain how to generate a mnemonic phrase with the SeedSigner, save it via a *SeedQR*, and then connect this wallet to Sparrow Wallet to manage it. I won't go into these procedures here and **I'm assuming that you already have a working Bitcoin wallet, configured with Sparrow and your SeedSigner**.


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Install firmware


To use your SeedSigner with a Seedkeeper, you need to install an alternative firmware, different from that of the original SeedSigner, in order to support smart card reading. For this, [I recommend using fork from "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Download [the latest version of the image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) corresponding to the Raspberry Pi model you're using.


![Image](assets/fr/02.webp)


If you don't already have it, download the [Balena Etcher] software (https://etcher.balena.io/), then proceed as follows:


- Insert the microSD card into your computer;
- Launch Etcher ;
- Select the `.zip` file you have just downloaded;
- Select the microSD card as the target;
- Click on `Flash!`.


![Image](assets/fr/03.webp)


Wait until the process is complete: your microSD is now ready for use. You can now move on to assembling your device.


For more details on firmware installation and software verification (a step I strongly recommend you take), see the following tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Assembling the smartcard reader


![video](https://youtu.be/jqE8HDMCImA)


Start by installing the camera on the Raspberry Pi Zero, carefully inserting it into the camera pin and locking it with the black tab. Then place the Pi on the bottom of the case, making sure to align the ports with the corresponding openings.


![Image](assets/fr/04.webp)


Then attach the smart card reader to the Raspberry Pi Zero's GPIO pins.


![Image](assets/fr/05.webp)


Slide the plastic cover over the smart card reader until it is correctly positioned.


![Image](assets/fr/06.webp)


Then add the screen to the extension's GPIO pins.


![Image](assets/fr/07.webp)


Finally, insert the microSD card containing the firmware into the side port on the Raspberry Pi Zero.


![Image](assets/fr/08.webp)


You can now connect your SeedSigner either via the Raspberry Pi Zero's Micro-USB port, or via the extension's USB-C port. Both options work. Wait a few seconds for startup, then you should see the welcome screen appear.


![Image](assets/fr/09.webp)


For more details on the initial setup of your SeedSigner, I recommend the following tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flash a smartcard with the Seedkeeper applet (optional)


![video](https://youtu.be/NF4HemyEcOY)


If you already own a Seedkeeper, you can skip this step and go straight to step 4. In this section, we'll look at how to install the Seedkeeper applet on a blank smartcard (DIY method).


To get started, open the `Tools > Smartcard Tools` menu on your SeedSigner.


![Image](assets/fr/10.webp)


Then select `DIY Tools > Install Applet`.


![Image](assets/fr/11.webp)


Insert your smartcard into the SeedSigner reader, chip facing down, then choose the `SeedKeeper` applet.


![Image](assets/fr/12.webp)


Please be patient during installation: the process may take several tens of seconds.


![Image](assets/fr/13.webp)


Once the applet has been successfully installed, you can proceed to step 4.


![Image](assets/fr/14.webp)


## 4. Save an existing SeedQR on Seedkeeper


![video](https://youtu.be/X-vmFHU9Ec8)


Now that your Seedkeeper is operational, you can save your Bitcoin wallet mnemonic on the smartcard. To begin, switch on your SeedSigner as usual, then scan your wallet's *SeedQR* to load it into the device. Once the seed has been imported, simply select `Done`.


![Image](assets/fr/15.webp)


When the seed is loaded, access the `Backup Seed` menu.


![Image](assets/fr/16.webp)


Then insert your Seedkeeper into the SeedSigner drive, and select the `To SeedKeeper` option.


![Image](assets/fr/17.webp)


The SeedSigner will then ask you to enter a PIN code for your Seedkeeper. As this is a blank card, no code has yet been defined. Enter any code to skip this step, then validate.


![Image](assets/fr/18.webp)


SeedSigner detects that Seedkeeper has not yet been initialized (i.e. no password has been set). Click `I Understand` to continue.


![Image](assets/fr/19.webp)


Now choose your Seedkeeper's new PIN code, between 4 and 16 characters. For added security, choose a long, random code: it's the only barrier protecting physical access to your mnemonic phrase.


Remember to save this PIN as soon as it is created, either in a reliable password manager, or on a separate physical medium depending on your strategy. In the latter case, be sure never to keep the medium containing the PIN in the same place as your Seedkeeper, otherwise protection will become ineffective. It's important to have a backup copy: **Without this PIN, you won't be able to access your seed, and your bitcoins will be lost**.


![Image](assets/fr/20.webp)


You can then define a `Label` associated with your mnemonic phrase. This label is useful if you store several secrets on Seedkeeper, so that you can easily identify them.


![Image](assets/fr/21.webp)


Your mnemonic phrase is now saved on the smartcard.


![Image](assets/fr/22.webp)


In terms of security strategy, several approaches are possible, depending on your needs and level of risk exposure. Personally, I recommend that you keep at least 2 copies of your seed:


- This is a first for smartcards, which you can keep easily accessible for everyday operations, such as verifying addresses or signing transactions. This method is practical (as we'll see in part 5) and remains secure thanks to the protection offered by the PIN code, so you can keep it accessible without major risk;
- A second copy of your unencrypted mnemonic phrase, serving as the ultimate backup of your portfolio, to be used only in the event of loss or theft of the Seedkeeper. As this version is unencrypted, it must be kept in a separate, more secure location, to prevent simultaneous compromise of the 2 backups.


Depending on your protection strategy and risk profile, you can also duplicate the seed on several different Seedkeepers, or create several physical copies of the mnemonic. To learn more about these practices, take a look at the following tutorial:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Loading a seed from Seedkeeper


![video](https://youtu.be/ms0Iq_IyaoE)


You can now use your Seedkeeper to load your mnemonic phrase into the SeedSigner at startup, and thus sign your Bitcoin transactions. To begin, switch on your SeedSigner by plugging it in, then open the `Seeds` menu.


![Image](assets/fr/23.webp)


Then select the `From SeedKeeper` option.


![Image](assets/fr/24.webp)


Insert your Seedkeeper into the smart card reader, then enter your PIN code to unlock it. Confirm your entry by pressing the bottom-right confirmation button, `KEY3`.


![Image](assets/fr/25.webp)


Seedkeeper can contain several secrets, so SeedSigner then prompts you to choose the one you wish to load. The label displayed corresponds to the name you defined in step 4. If, as in my case, you have only registered one seed, only one option will be available.


![Image](assets/fr/26.webp)


Your seed is now loaded. Check that this is the correct wallet by comparing the fingerprint displayed on the screen with the one specified in your Sparrow Wallet settings. This fingerprint was also provided when the wallet was first created.


If you're using a passphrase, you can apply it at this stage (see part 6 of this tutorial). Otherwise, simply click on `Done`.


![Image](assets/fr/27.webp)


You can then use your wallet as usual: check your delivery addresses and sign transactions, just like with a classic SeedSigner. To find out more about how to use it, see the dedicated tutorial :


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Using Seedkeeper with a passphrase BIP39


Are you using a passphrase to protect your Bitcoin portfolio? You can also register it in your Seedkeeper, alongside your seed. This solution will enable you to quickly load your wallet onto the SeedSigner, without having to manually enter the passphrase on the small keypad each time you use it.


I find this method particularly interesting, as it allows you to benefit from the security advantages of the passphrase, while eliminating the constraints associated with its day-to-day use. Here's an example of a configuration I'd recommend:


- Keep your seed and passphrase in a Seedkeeper, protected by a strong PIN code (this is important). This backup will enable you to easily use your wallet on a daily basis. If you wish, you can duplicate this information on a second Seedkeeper;
- Also keep a clear copy of your mnemonic and passphrase, on paper or metal. This is your backup of last resort if you lose your Seedkeeper or its PIN. Be sure to store these copies in separate locations, so that they cannot be compromised simultaneously.


In this configuration, if someone gets their hands on your plaintext mnemonic alone, they won't be able to steal anything without knowing the passphrase (provided, of course, that it's strong enough to withstand a brute-force attack). Conversely, if someone discovers your passphrase in plain text, it will remain unusable without the corresponding mnemonic phrase.


Finally, if someone manages to gain physical access to your Seedkeeper containing the seed and passphrase, they won't be able to extract anything without knowing the PIN code. Unlike a passphrase, this code cannot be brute-forced, as the smartcard automatically locks itself after 5 invalid attempts.


The safety of this configuration is therefore based on 2 essential points:


- A **passphrase strong**: it must be long, random and contain a wide variety of characters. Its complexity is not a problem for you, since you'll only have to enter it once on the keyboard during initialization; afterwards, it will be transmitted by Seedkeeper ;
- A **strong PIN code** for Seedkeeper: also random and composed of 16 characters.


To set up this setup, start by loading your passphrase into the SeedSigner in the usual way. You can follow the procedure detailed in this tutorial:


https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Once your portfolio with passphrase has been correctly loaded onto the SeedSigner, open the `Seeds` menu and select the footprint corresponding to this portfolio. Note that this footprint differs from that of the portfolio without passphrase.


![Image](assets/fr/28.webp)


Then click on `Backup Seed`, insert the Seedkeeper into the drive, and select `To SeedKeeper`.


![Image](assets/fr/29.webp)


Enter your PIN to unlock Seedkeeper, then assign a label to this secret. You can leave the fingerprint as the label to maintain some form of plausible deniability, or explicitly state `Passphrase Wallet`, for example.


![Image](assets/fr/30.webp)


Your passphrase portfolio is now registered on Seedkeeper.


![Image](assets/fr/31.webp)


Next time you start up, simply insert your Seedkeeper into the drive, then navigate to `Seeds > From SeedKeeper`.


![Image](assets/fr/32.webp)


Enter your PIN to unlock the smartcard, then select the wallet corresponding to your passphrase.


![Image](assets/fr/33.webp)


Check the passphrase and your wallet imprint, then confirm.


![Image](assets/fr/34.webp)


You can now access your portfolio with passphrase and sign your transactions as you normally would on a SeedSigner.


## 7. Additional options


In the `Tools > Smartcard Tools` menu, you'll find several options for managing your Seedkeeper:



- In the `Common Tools` menu, you can :
 - Check card authenticity;
 - Change PIN code ;
 - Change the labels associated with your secrets ;
 - Disable NFC function (recommended if using chip reader only) ;
 - Perform a factory reset.



- In the `SeedKeeper Functions` menu, you can :
 - Consult the list of registered secrets ;
 - Save a new secret ;
 - Delete an existing secret ;
 - Save or load your descriptors (useful function for multi-sig portfolios).



- In the `DIY Tools` menu, you can :
 - Compiling the Seedkeeper applet ;
 - Install the applet on a blank card ;
 - Delete a Seedkeeper applet to reset it and make it blank again.


Now you know how to use Seedkeeper to back up your portfolio securely in combination with SeedSigner.


If this setup has convinced you, don't hesitate to support the projects that make it possible:


- By purchasing your equipment directly [on the Satochip website](https://satochip.io/shop/);
- By making [a donation to the SeedSigner project](https://seedsigner.com/donate/);
- By subscribing to [Crypto Guide's YouTube channel](https://www.youtube.com/@CryptoGuide/), run by the person who maintains the GitHub repository hosting the modified firmware.