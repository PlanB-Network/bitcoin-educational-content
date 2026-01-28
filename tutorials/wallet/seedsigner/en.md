---
name: SeedSigner
description: DIY, stateless, affordable and fully air-gapped wallet hardware
---

![cover](assets/cover.webp)


The SeedSigner is an open-source wallet Bitcoin hardware that anyone can build themselves using inexpensive general-purpose electronic components. Unlike commercial products such as the Ledger, Coldcard or Trezor, this is not a ready-to-use device manufactured by a company: it's a community project that allows anyone to create their own device, controlling every step.


The SeedSigner is designed to be 100% ***air-gapped***: it never connects to the Internet, has no Wi-Fi or Bluetooth (in the case of the Raspberry Pi Zero v1.3) and is never connected to a computer to exchange data. Communication is exclusively via a QR code exchange system. In concrete terms, your wallet management software (such as Sparrow Wallet) displays the transaction to be signed in the form of QR codes; you scan them with the SeedSigner's camera, then the device signs the transaction using your private keys temporarily stored in its RAM. Finally, it generates QR codes containing the signed transaction, which you scan with your software to send it to the Bitcoin network.


![Image](assets/fr/001.webp)


SeedSigner is also ***stateless***. In other words, it doesn't save your seed or your private keys permanently, unlike other hardware wallets. Every time you reboot, its memory is completely empty, unless you configure the device to save your settings on a microSD card. You therefore have to re-enter your seed each time you use it, the most practical method being to store it in the form of a QR code, to be scanned at start-up using the SeedSigner's camera. This mode of operation considerably reduces the attack surface: even if a thief steals your device, he won't find any information on it, since it's always empty by default.


Another option for storing your seed and using it with the SeedSigner is to use a *SeedKeeper* smart card in conjunction with a compatible reader. This gives you a very robust *Secure Element* to store your seed, while using the SeedSigner screen to sign transactions. But this particular configuration is the subject of another dedicated tutorial. Here, we'll concentrate on the basic use of the SeedSigner:


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

The SeedSigner project occupies an important place in the Bitcoin ecosystem, as it offers everyone, everywhere in the world, the possibility of benefiting from advanced security to protect their bitcoins. Its main advantage lies in its accessibility: the hardware required can be purchased for less than $50. What's more, it enables people living in restricted countries to build their own wallet hardware from standard computer components, which are easy to find and less subject to regulatory constraints.


But even outside these particular contexts, SeedSigner can be an interesting option for you: it's open-source, works stateless and airgapped, and reduces the attack vectors linked to the supply chain of your wallet hardware.


## 1. Required equipment


To build your SeedSigner, you will need the following components:



- Raspberry Pi Zero
    - Version 1.3 is recommended, as it has neither Wi-Fi nor Bluetooth, ensuring complete isolation.
 - The W and v2 versions are also compatible, but incorporate a Wi-Fi/Bluetooth chip. It is therefore advisable to physically deactivate it by removing the radio module from the card. The operation is relatively simple, but requires precision (fine pliers are sufficient for the Zero W, while a hot pen is needed for the v2 to remove the metal plate that hides the module). I won't go into the details in this tutorial, but you'll find all the instructions in this document: *[Disabling WiFi/Bluetooth by hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Please note: some Raspberry Pi Zero models are sold without pre-soldered GPIO pins. You can either buy a version with integrated pins directly (simplest solution), or buy the pins separately and solder them yourself (more complex solution).
 - Don't forget to include a micro-USB power supply.


![Image](assets/fr/002.webp)



- Waveshare 1.3" screen (240×240 px)** (in French)
    - It's essential to choose this particular model: other similar screens exist, but with a different resolution. Without 240×240 px definition, the display will be unusable.
    - The screen features three buttons and a mini-joystick for user interface.


![Image](assets/fr/003.webp)



- Raspberry Pi Zero**-compatible camera
    - Option 1: the standard camera with a wide gold mat (check compatibility with your housing).
    - Option 2: the more compact "*Zero*" camera, designed specifically for the Pi Zero.


![Image](assets/fr/004.webp)



- MicroSD** card
    - Recommended capacity: between 4 and 32 GB.



- Housing (optional but recommended)** (optional but recommended)** (optional but recommended)** (optional but recommended)**)
    - Protects the device and makes it easy to use.
    - The most popular model is the "*Orange Pill Case*", for which [open-source STL files are available for 3D printing](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Boxes are also available from [independent resellers linked to the project](https://seedsigner.com/hardware/).


![Image](assets/fr/005.webp)


You can buy these components separately or, for greater simplicity, opt for ready-made packs that include all the necessary hardware. Personally, I ordered my pack [on this French site](https://bitcoinbazar.fr/), but you'll also find a list of vendors for each region of the world on [the SeedSigner project hardware page](https://seedsigner.com/hardware/). If you prefer to buy the components individually, they are available on the major e-commerce platforms or in specialist stores.


## 2. Preparing the software


Once you've got your hardware together, you need to prepare the microSD card by installing the SeedSigner system on it. To do this, go to your everyday personal computer, and plug in your microSD intended for SeedSigner.


### 2.1. Download


Go to [the project's official GitHub repository](https://github.com/SeedSigner/seedsigner/releases). On the latest version of the software, download :


- The `.img` image corresponding to your Pi model.
- The `.sha256.txt` file.
- The `.sha256.txt.sig` file.


![Image](assets/fr/006.webp)


Before starting the installation, let's check the software.


### 2.2 Verification under Linux and macOS


Start by importing the official public key of the SeedSigner project directly from Keybase :


```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```


![Image](assets/fr/007.webp)


The terminal should tell you that a key has been imported or updated. Next, run the verification command on the signature file (remember to modify the command according to your version, here `0.8.6.`):


```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```


![Image](assets/fr/008.webp)


If everything is correct, the output should read `Good signature`. This means that the file `.sha256.txt` has been signed by the key you have just imported, and that the signature is valid. Ignore the warning message `WARNING: This key is not certified with a trusted signature`: this is normal, as it's now up to you to check that the key used belongs to the SeedSigner project.


To do this, compare the last 16 characters of the fingerprint displayed with those available on [Keybase.io/SeedSigner](https://keybase.io/seedsigner), on their [official Twitter](https://twitter.com/SeedSigner/status/1530555252373704707), or in the file published on [SeedSigner.com](https://seedsigner.com/keybase.txt). If these identifiers match exactly, you can be sure that the key is indeed that of the project. If in doubt, stop immediately and ask the SeedSigner community (Telegram, X, GitHub...) for help.


When the key has been validated, you can check that the downloaded image has not been modified (remember to modify the command according to your version, here `0.8.6.`):


```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```


![Image](assets/fr/009.webp)



- Under Linux, this command is built-in.
- Warning: macOS versions prior to `Big Sur (11)` do not recognize the `--ignore-missing` option. In this case, remove it and ignore warnings about missing files.


The expected result is an `OK` next to the `.img` file. This confirms that the uploaded image is identical to the one published by the project and has not been modified.


### 2.3 Windows verification


On Windows, the procedure is similar but the commands are different. Start by installing [Gpg4win](https://www.gpg4win.org/) and open the *Kleopatra* application. Import the public key of the SeedSigner project from the URL Keybase :


```
https://keybase.io/seedsigner/pgp_keys.asc
```


![Image](assets/fr/010.webp)


Next, open PowerShell in the folder where your downloaded files are located (`Shift` + right-click > `Open PowerShell here`). Run the following command to check the manifest signature (remember to modify the command according to your version, here `0.8.6.`):


```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```


![Image](assets/fr/011.webp)


If everything is correct, the output should read `Good signature`. This means that the file `.sha256.txt` has been signed by the key you have just imported, and that the signature is valid. Ignore the warning message `WARNING: This key is not certified with a trusted signature`: this is normal, as it's now up to you to check that the key used belongs to the SeedSigner project.


To do this, compare the last 16 characters of the fingerprint displayed with those available on [Keybase.io/SeedSigner](https://keybase.io/seedsigner), on their [official Twitter](https://twitter.com/SeedSigner/status/1530555252373704707), or in the file published on [SeedSigner.com](https://seedsigner.com/keybase.txt). If these identifiers match exactly, you can be sure that the key is indeed that of the project. If in doubt, stop immediately and ask the SeedSigner community (Telegram, X, GitHub...) for help.


Once the key has been validated, you need to check that the image file has not been corrupted. To do this, use the following command in PowerShell :


```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```


Example for a Raspberry Pi Zero 2 (remember to modify the command according to your version, here `0.8.6.`):


```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```


![Image](assets/fr/012.webp)


PowerShell then calculates the SHA256 hash of your image file. Compare this hash with the corresponding value in `seedsigner.0.8.6.sha256.txt`.


- If the two values are strictly identical, the check is successful and you can continue.
- If they differ, the file is corrupted or corrupted. Don't use it, and start the download again.


![Image](assets/fr/013.webp)


Successful verification guarantees that your `.img` file is both authentic (signed by SeedSigner) and unaltered (unmodified). You can then safely move on to the next step.


### 2.4. Flash the image


If you don't already have it, download the [Balena Etcher] software (https://etcher.balena.io/), then :


- Insert the microSD card into your computer.
- Launch Etcher.
- Select the downloaded and verified `.img` file.
- Select microSD card as target.
- Click on `Flash!`.


![Image](assets/fr/014.webp)


Wait until the process is complete: your microSD is ready for use. Now it's time for assembly!


## 3. SeedSigner assembly


Once your microSD card has been prepared and flashed with SeedSigner software, you can proceed with final assembly. Take your time, as some parts are fragile (notably the tablecloth, camera and GPIO pins).


### 3.1 Preparing the housing


First of all, open your case. Check that it's clean and that no residual 3D printing plastic is in the way of the internal fasteners. Look out for :


- Camera location (small circular hole at front).
- The opening for the screen.
- The cut-outs for the Raspberry Pi Zero's micro-USB ports and microSD slot.


### 3.2 Camera installation


Locate the camera ribbon connector on the Raspberry Pi Zero: it's a thin black strip on the side of the board, which can be lifted slightly to open. Lift it up carefully, without forcing it: it should simply tilt a few millimeters.


![Image](assets/fr/015.webp)


Insert the camera cover. The brown/copper part should face downwards. Make sure it is firmly seated in the connector, without twisting.


![Image](assets/fr/016.webp)


Close the black bar to lock the tablecloth (you'll feel a slight click). Gently check that it stays in place and doesn't move.


![Image](assets/fr/017.webp)


Then place the camera module in the appropriate hole in the housing. Depending on the model, it may snap in directly or require a small adhesive strip to hold it in place. The lens must be perfectly aligned, facing outwards.


### 3.3 Installing the Raspberry Pi Zero


If you're using a case, insert the Raspberry Pi Zero board inside. Carefully align the ports with the openings provided.


Then position the Waveshare display on top of the Raspberry Pi Zero. The Pi's GPIO pins should line up perfectly with the display's female connector. Slowly press the display onto the pins, applying even pressure on each side to avoid bending them.


![Image](assets/fr/018.webp)


If you have a case, complete the assembly by adding the front panel and joystick.


Finally, insert the microSD card containing the flashed software into the Raspberry Pi Zero's edge-mounted slot. Make sure it clicks into place.


### 3.4 First start-up


Connect a micro-USB power cable to the dedicated port. Wait about one minute. The SeedSigner logo should appear, followed by the home screen.


![Image](assets/fr/019.webp)


To begin with, check that the various components are working properly by going to the `Settings > I/O test` menu.


![Image](assets/fr/020.webp)


Test all the buttons and make sure they respond correctly. Then click on the `KEY1` button to check that the camera is working as expected. This will take a picture.


![Image](assets/fr/021.webp)


### 3.5 Camera adjustment


Depending on how you've mounted your SeedSigner, the camera may display an inverted image. To correct this, go to `Settings > Advanced > Camera rotation` and select a 180° rotation if necessary.


![Image](assets/fr/022.webp)


If you've changed the camera orientation or wish to change other settings (such as the interface language) at a later date, you'll need to enable persistence of settings on the microSD. Otherwise, your settings will revert to the default every time you reboot, as the Raspberry Pi Zero has no persistent memory.


To do this, open the `Settings > Persistent settings` menu, then select `Enabled`.


![Image](assets/fr/023.webp)


If everything is functional, your SeedSigner is now ready for use!


## 4. SeedSigner settings


Before creating your Bitcoin wallet, let's configure the SeedSigner. As it runs on a Raspberry Pi Zero without persistent memory, its settings are not saved automatically unless you save them on the microSD card. So make sure you've enabled this option, otherwise these settings will be lost on reboot (see step 3.5).


### 4.1 Parameter menu access


Start your SeedSigner and wait for the home screen to appear. Using the joystick, navigate to the `Settings` option, then validate by pressing the central button. You now enter the main settings menu.


![Image](assets/fr/024.webp)


### 4.2 Choosing wallet management software


Then access the `Coordinator software` menu.


![Image](assets/fr/025.webp)


The `Coordinator` refers to the wallet management software with which your SeedSigner will communicate via QR codes. This software is installed either on your computer or on your smartphone. It will enable you to manage your bitcoins, but without ever having access to your private keys. The SeedSigner remains the only device capable of signing your transactions.


The current firmware version supports several programs: Sparrow, Specter, BlueWallet, Nunchuk and Keeper. In my case, I use **Sparrow Wallet**, which I particularly recommend for its simplicity and rich functionality.


If you don't know how to install it, you can follow this tutorial:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Simply select the software of your choice from the menu.


![Image](assets/fr/026.webp)


### 4.3 Units and amount display


In the `Denomination Display` menu, you can choose the unit in which the amounts are displayed:


- `BTC`
- mBTC` (milli-bitcoin, or 0.001 BTC)
- gW-15 (satoshis, or 1/100,000,000 BTC)


The **sats** unit is generally the most practical for small amounts.


![Image](assets/fr/027.webp)


### 4.4 Advanced settings


Now go to the `Advanced` menu. Here you will find several useful options:


- gW-17 network`: to be modified only if you wish to use the SeedSigner on Testnet.
- qR code density`: adjusts the amount of information contained in each QR code. You can leave the default value, unless you find it difficult to read when scanning.
- `Xpub export`: enables or disables the export of your extended public key (`xpub`, `ypub`, `zpub`) to wallet management software via QR code (a function we'll be using later, so leave it enabled for now).
- `Script types`: defines the script types allowed to lock your bitcoins. You don't need to modify this parameter, as the script type will be set directly to Sparrow. Here, only scripts that the SeedSigner is authorized to manipulate are concerned.


### 4.5 Language selection


Finally, in the `Language` menu, you can change the interface language to suit your preference.


![Image](assets/fr/028.webp)


## 5. Creating and saving seed


The seed (or mnemonic phrase) forms the basis of your Bitcoin wallet. It is used to derive your private keys and addresses, and provides access to your funds. SeedSigner offers several methods for generating it, which we'll look at in this section.


Before we begin, a few essential reminders:


- This phrase gives full, unrestricted access to all your bitcoins.** Anyone in possession of this phrase can steal your funds, even without physical access to your SeedSigner ;
- Usually, a 12-word phrase is used to restore a wallet in the event of loss or theft of wallet hardware. But since the SeedSigner is a *stateless* device, it never registers your seed. So your physical backups are not simply backup copies, but **the only way to use your wallet**. If you lose these backups, your bitcoins will be permanently lost. So back them up carefully, on several media and in safe places;
- If you're just starting out, I strongly advise you to read this tutorial for a detailed understanding of the risks involved in managing a mnemonic phrase :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Accessing the seed creation tool


From the SeedSigner home screen, go to the `Tools` menu.


![Image](assets/fr/029.webp)


You will now generate your seed. A seed is simply a large random number. The more randomly it is generated, the more secure it is. SeedSigner offers two ways of doing this:


- camera": seed is generated from the visual noise of a photograph. You take an image of a random environment (object, landscape, face, etc.) whose pixel variations are used to generate entropy. It's a fast method, but not reproducible.
- dice Rolls": you roll dice to create the necessary entropy. It's more time-consuming, but reproducible and therefore verifiable. If you opt for this method, follow the advice in this tutorial (no need to calculate the checksum here, the SeedSigner takes care of that):


https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Creating the seed with the photo


If you choose the photo method, click on `New seed` (with the camera icon), take a picture and validate. Then select the length of your sentence (12 or 24 words), which will appear on the screen for saving. The following steps are identical to part 5.3.


### 5.3 Creating seed with dice


In this tutorial, we use the **Dice Rolls** method. Click on `New seed` (with the dice icon).


![Image](assets/fr/030.webp)


Then choose the length of your mnemonic phrase. 12 words already offer a sufficient level of security, so this is the choice I recommend.


![Image](assets/fr/031.webp)


Roll your dice and enter the resulting numbers using the cursor. Press the center button to validate each entry. If you make a mistake, you can go back. Use several different dice to reduce the influence of any unbalanced dice. Make sure you are not being watched during this operation.


![Image](assets/fr/032.webp)


Once you've entered your 50 throws, the SeedSigner generates your sentence. **Follow the instructions in this tutorial carefully if you're just starting out:**


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Displaying and saving the seed


Carefully write down the words of your mnemonic phrase on a suitable physical support (paper or metal).


![Image](assets/fr/033.webp)


### 5.5 Checking the backup


To avoid any backup errors, SeedSigner asks you to verify your backup. Click on `Verify`.


![Image](assets/fr/034.webp)


Then enter the requested word according to its order in the sentence. For example, here I have to choose the third word in my sentence.


![Image](assets/fr/035.webp)


If you make a mistake, the SeedSigner will inform you, and you'll have to start again, making sure to note your mnemonic phrase when it's given to you. This verification step ensures that your backup is correct and complete. Once validated, the screen will display `Backup Verified`.


![Image](assets/fr/036.webp)


For a more complete restoration test, follow this tutorial :


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Understanding the concept of "stateless device


The SeedSigner is a device without permanent memory. This means that your seed is never stored inside the device (unlike a Ledger, Trezor or Coldcard, for example). As soon as you switch off the power, the seed disappears completely from its RAM. When you restart, the SeedSigner returns to a blank state: you'll then have to give it your seed again, so that it can sign your transactions.


This provides essential protection. Unlike other hardware wallets, SeedSigner is based on a Raspberry Pi Zero, which has no physical protection, including *Secure Element*. But since no sensitive data is stored, even a physically compromised device wouldn't allow an attacker to extract your private keys or spend your bitcoins.


On the other hand, this architecture implies an additional responsibility: without a backup, your funds are definitively lost. That's why I recommend a **double backup**. You already have your recovery phrase: this is your main long-term backup, to be kept in a safe place. Now we're going to create a copy of this phrase in the form of **QR code**.


Each time you use the SeedSigner, you scan this QR code with the device's camera so that it temporarily loads your seed into its memory while you sign your transactions. This second backup, intended for everyday use, must also be kept with the utmost care: anyone in possession of this QR code has full access to your bitcoins.

I also advise you to store your QR code and your mnemonic phrase in two separate locations, to avoid losing everything in the event of a claim.


Finally, a more advanced and secure alternative is to use the SeedSigner with a **SeedKeeper**, which stores the seed in a secure element. To find out more, take a look at this tutorial:


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Write master key fingerprint


Once verification is complete, SeedSigner displays the fingerprint of your wallet's master key. This fingerprint identifies your wallet and ensures that you use the correct recovery phrase in the future. It doesn't reveal any information about your private keys, so you can safely store it on a digital medium. Just make sure you keep an accessible copy and never lose it.


![Image](assets/fr/037.webp)


It's also at this stage that you can add a **passphrase BIP39** to reinforce the security of your wallet. Depending on your backup strategy, this option may be worthwhile, but it also entails risks: if you lose the passphrase, access to your bitcoins will be permanently lost.


https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

If you are not yet familiar with the passphrase concept, I invite you to read this comprehensive tutorial on the subject:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)


### 5.8 Saving the seed in QR format (*SeedQR*)


SeedSigner lets you convert your seed into a paper QR code, called *SeedQR*. This method simplifies reloading your wallet, as it avoids retyping each word manually.


To do this, you'll need a blank paper or metal QR code corresponding to the length of your mnemonic phrase. If you've purchased a complete package for your SeedSigner, the templates are usually included. If not, you can download and print them (or reproduce them by hand) here :


- [12-word format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24-word format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Compact format 12 words](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Compact format 24 words](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)


From your seed screen, select `Backup Seed`.


![Image](assets/fr/039.webp)


Then choose `Export as SeedQR`.


![Image](assets/fr/040.webp)


Then select the desired format (normal or compact) according to the paper template available.


![Image](assets/fr/041.webp)


Click `Begin` to start creating the *SeedQR*. The SeedSigner will then display a series of grids (A1, A2, B1, etc.), each corresponding to a portion of the code.


![Image](assets/fr/042.webp)


Carefully reproduce each black dot on your save sheet, then use the joystick to move on to the next block. Take your time: a simple misalignment can render the QR code unusable.


A few tips:


- Start with a pencil so that you can correct any mistakes, then go back to using a fine black pen once you've finished;
- A well-centered point in the middle of the square is all you need, no need to fill it completely.


![Image](assets/fr/043.webp)


Then click on `Confirm SeedQR`, and scan your QR code to check that it's working correctly.


![Image](assets/fr/044.webp)


If the message `Success` is displayed, your *SeedQR* is valid: you can proceed to the next step.


![Image](assets/fr/045.webp)


**Keep this sheet as strictly as your recovery phrase. Anyone in possession of this QR code can reconstruct your private keys and steal your bitcoins.**


Congratulations, your Bitcoin wallet is now up and running! We'll now import its public components into **Sparrow Wallet** to manage it easily.


## 6. Import wallet into Sparrow


Once your SeedSigner has been set up and your seed correctly generated and saved, the next step is to link this wallet to management software such as Sparrow Wallet. Your seed will always remain offline, as only the public part of your wallet will be transmitted to Sparrow. This will enable the software to display your addresses, transactions and build new transactions, without ever being able to spend your bitcoins. To spend your bitcoins, your SeedSigner will always have to sign the transaction prepared by Sparrow.


### 6.1 Preparing the SeedSigner


Insert the microSD containing the operating system, switch on your SeedSigner, then load the seed you've just created from your backup QR code. On the Home screen, select `Scan`, then scan your SeedQR with the SeedSigner.


![Image](assets/fr/046.webp)


Check that the fingerprint on your master key matches the fingerprint on your wallet. If you're using a passphrase, enter it at this stage.


![Image](assets/fr/047.webp)


This takes you to the menu for your wallet, in my case named `d4149b27`. If you're back at the home screen, select `Seeds`, then choose the print corresponding to your wallet. Then click on `Export Xpub`.


![Image](assets/fr/048.webp)


Select the wallet type. In our case, it's a single wallet: select `Single Sig`.


![Image](assets/fr/049.webp)


Next comes the choice of scripting standard. The latest and most economical in terms of transaction costs is `Taproot`. I therefore advise you to select this standard.


![Image](assets/fr/050.webp)


A warning message will appear. This is normal: this extended public key (`xpub`) allows you to view all the addresses derived from your seed (on the first account). It doesn't allow you to spend your funds, but it does reveal the structure of your wallet. If it ever leaks, it's a problem for your privacy, but not for the security of your bitcoins: it allows you to see them, but not to spend them.


Click `I Understand`, then `Export Xpub` if you are satisfied with the information displayed.


The SeedSigner then generates your xpub in the form of a dynamic QR code containing all the data you need to manage your wallet in Sparrow Wallet.


![Image](assets/fr/051.webp)


You can use the joystick to adjust the screen brightness for easier QR code scanning.


### 6.2 Importing a new wallet into Sparrow Wallet


Make sure you have the Sparrow Wallet software installed on your computer. If you don't know how to download, check and install it correctly, see our full tutorial on the subject:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

On your computer, open Sparrow Wallet, then in the menu bar, click `File → Import Wallet`.


![Image](assets/fr/052.webp)


Scroll down to `SeedSigner`, then select `Scan...`. Your webcam will open: scan the dynamic QR code displayed on your SeedSigner screen.


![Image](assets/fr/053.webp)


Assign a name to your wallet, then click on `Create Wallet`. Sparrow will then ask you to set a password to lock local access to this wallet. Choose a strong password: it protects access to your wallet data in Sparrow (public keys, addresses, labels and transaction history). This password is not needed to restore the wallet at a later date: only your mnemonic phrase (and possibly your passphrase) is required for this purpose.


I recommend that you save this password in a password manager to avoid losing it.


![Image](assets/fr/054.webp)


Your keystore has now been successfully imported.


![Image](assets/fr/055.webp)


Then check that the `Master fingerprint` displayed in Sparrow matches the one previously noted in your SeedSigner.


Your SeedSigner and Sparrow Wallet are now securely linked. Sparrow acts as a complete management interface, while the SeedSigner remains the only device capable of signing your transactions. You're now ready to receive and send bitcoins in a totally air-gapped configuration.


## 7. Receiving and sending bitcoins


Your SeedSigner and Sparrow Wallet are now configured to work together. In this final section, we'll take a look at how to receive and send bitcoins using this configuration.


### 7.1 Receiving bitcoins


#### 7.1.1 Generating a reception address


On your computer, open Sparrow Wallet and unlock your SeedSigner wallet using your password. Make sure the software is connected to a server (notch at bottom right). In the sidebar, click on `Receive`.


![Image](assets/fr/056.webp)


A new Bitcoin address is displayed. You will see :


- The text address (starting with `bc1p...` if you use P2TR like I do),
- The corresponding QR code,
- A `Label` field for tracking your transactions.


I strongly recommend that you add a label to each bitcoin receipt on your wallet. This will allow you to easily identify the provenance of each UTXO and improve your privacy management. To delve deeper into this important topic, you can check out the dedicated training on Plan ₿ Academy :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

To add a label, simply enter a name in the `Label` field, then confirm.


For example:


```txt
Label : Sale of the Raspberry Pi Zero
```


Your address is now associated with this label in all Sparrow sections.


![Image](assets/fr/057.webp)


#### 7.1.2 Address verification on the SeedSigner


Before sharing your receiving address, it is very important to check that it belongs to your seed. This step ensures that your SeedSigner will be able to sign transactions associated with this address. It also protects against possible attacks in which Sparrow displays a fraudulent address. Remember that Sparrow runs on an insecure environment (your computer), which has a much larger attack surface than your SeedSigner, which is totally isolated. That's why you should never blindly believe the receiving addresses presented on Sparrow until you've verified them with your wallet hardware.


On Sparrow, click on the QR code of the address to enlarge it: it will then be displayed full screen.


![Image](assets/fr/058.webp)


On your SeedSigner, from the main menu, select `Scan`. Scan the QR code displayed on your computer screen, then choose the seed corresponding to your wallet (in my case, the `d4149b27` fingerprint).


![Image](assets/fr/059.webp)


If the scanned address matches the one derived from your seed, the SeedSigner screen will display the message: `Address Verified`.


![Image](assets/fr/060.webp)


This confirms that the address belongs to your wallet and that you can confidently receive bitcoins from it.


#### 7.1.3 Receipt of funds


You can now communicate this address (in text or QR code form) to the person or department who needs to send you satss. Once the transaction has been broadcast on the network, it will appear in the `Transactions` tab of Sparrow Wallet.


![Image](assets/fr/061.webp)


### 7.2 Send bitcoins


Sending bitcoins with a SeedSigner is a 3-step process:


- Transaction creation in Sparrow ;
- Signature of the transaction on the SeedSigner ;
- Final distribution of the transaction via Sparrow.


All exchanges between the two devices are made exclusively using QR codes.


#### 7.2.1 Creating the transaction in Sparrow


In Sparrow Wallet, you can click on the `Send` tab in the left-hand sidebar. However, I prefer to use the `UTXOs` tab, which allows you to practice "*Coin Control*". This method gives you precise control over the UTXOs used, so you can control the information you reveal during the transaction.


In the `UTXOs` tab, select the coins you wish to spend, then click `Send Selected`.


![Image](assets/fr/062.webp)


Then fill in the transaction fields:


- In `Pay to`, paste the recipient's address or click on the camera icon to scan the QR code;
- In `Label`, add a label to track this expense;
- In `Amount`, enter the amount to be sent;
- Finally, select the fee rate based on current market conditions (estimates are available at [mempool.space](https://mempool.space/)).


Once the fields have been completed, check the information carefully, then click on `Create Transaction >>`.


![Image](assets/fr/063.webp)


Check the transaction details to make sure everything is correct, then click on `Finalize Transaction for Signing`.


![Image](assets/fr/064.webp)


The transaction is now ready, but not yet signed. To display the [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) as a QR code, click on `Show QR`.


![Image](assets/fr/065.webp)


#### 7.2.2 Signing the transaction with the SeedSigner


Switch on your SeedSigner and scan your SeedQR to access your wallet, as usual. From the home screen, select `Scan`, then scan the QR code displayed on Sparrow.


![Image](assets/fr/066.webp)


Then choose the seed to match your wallet.


![Image](assets/fr/067.webp)


The SeedSigner automatically detects that this is a PSBT and displays a summary of the transaction:


   - The amount sent,
   - Output addresses,
   - Associated transaction costs.


Click on `Review Details` and carefully check all the information directly on the SeedSigner screen. The most important items to check are the amount sent, the recipient's address and the amount of charges applied.


![Image](assets/fr/068.webp)


If everything is correct, select `Approve PSBT` to sign the transaction using the corresponding private key(s).


![Image](assets/fr/069.webp)


Once signed, the SeedSigner generates a new QR code containing the signed transaction, ready to be scanned by Sparrow.


![Image](assets/fr/070.webp)


#### 7.2.3 Broadcasting the transaction from Sparrow


Now that the transaction is valid, it needs to be broadcast on the Bitcoin network, so that it reaches a miner who will add it to a block.


On Sparrow, click on `QR Scan`.


![Image](assets/fr/071.webp)


Present the QR code displayed by your SeedSigner (that of the signed transaction) to the webcam. Sparrow will decode the signature and display the full transaction details. Make a final check that all the information is correct, then click on Broadcast Transaction to broadcast it on the Bitcoin network.


![Image](assets/fr/072.webp)


Your transaction has now been sent to the Bitcoin network. You can follow its progress in the `Transactions` tab of Sparrow Wallet.


![Image](assets/fr/073.webp)


You've now mastered the basics of using SeedSigner. To deepen your knowledge and explore more advanced uses, I invite you to consult the following tutorial:


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[You can also support the development of the SeedSigner open-source project by making a donation in bitcoins!](https://seedsigner.com/donate/)**


*Credit: some of the images in this tutorial come from the [official SeedSigner project website](https://seedsigner.com/) and [GitHub repository](https://github.com/SeedSigner/seedsigner).*