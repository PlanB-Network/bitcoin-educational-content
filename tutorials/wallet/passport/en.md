---
name: Passport - Foundation
description: Configuring and using the Passport hardware wallet in manual mode
---
![cover](assets/cover.webp)

The Passport is a Bitcoin-only hardware wallet, designed by Foundation Devices, an American company founded in April 2020 in Boston.

The Passport "*Batch 2*" we present in this tutorial is the successor to the "*Founder's Edition*". It features a premium design, a high-definition color screen and an ergonomic physical keyboard. It operates in "*Air-Gap*" mode, ensuring that your wallet's private keys remain totally isolated, with exchanges possible via a MicroSD card or QR codes. The device includes a removable 1200 mAh battery.

As for connectivity, the Passport is equipped with a MicroSD port, a USB-C port for charging, and a rear camera for scanning QR codes.

In terms of security, the Passport incorporates a secure element, and the device's source code is entirely open-source. It offers all the features expected of a good Bitcoin hardware wallet. Note that the Passport does not yet support miniscript, but this feature is planned for the second quarter of 2025.

Priced at $199, the Passport is positioned as a high-end hardware wallet, competing with the Coldcard Q, Jade Plus, Tezor Safe 5 and Ledger's top-of-the-range models.

![Image](assets/fr/01.webp)

To manage your secure wallet on a Passport, you have several options. This hardware wallet is compatible with the majority of wallet management software on the market, including Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, among others. In this tutorial, we'll learn how to use it with Sparrow Wallet.

If you're a beginner, the easiest option is to use your Passport with the native Envoy application, developed by Foundation. To find out how to use Envoy with your Passport, check out this other tutorial :

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb
## Unboxing the Passport

When you receive your Passport, make sure the box and seal on the carton are intact to confirm that the package has not been opened. A software verification of the device's authenticity and integrity will also be carried out when it is set up.

![Image](assets/fr/02.webp)

Box contents include :


- Passport;
- A piece of cardboard to write down your mnemonic phrase;
- A USB-C cable for charging ;
- MicroSD card ;
- Two MicroSD to Lightning or USB-C adapters ;
- Stickers.

On the device, you will find :


- A keyboard (1) ;
- USB-C port (2);
- A delete button (3);
- A return button (4) ;
- A confirmation button (5);
- Directional pad (6);
- On/off button (7);
- A status indicator (8);
- MicroSD port (9) ;
- A button to change mode aA1 (10) ;
- A rear camera.

![Image](assets/fr/03.webp)

## Starting Passport

Press the on/off button on the side of the unit to start it up.

![Image](assets/fr/04.webp)

Press the confirmation button to access the next menu.

![Image](assets/fr/05.webp)

In this tutorial, we'll use Sparrow Wallet to manage the Passport-secured wallet. Select "*Manual Setup*".

![Image](assets/fr/06.webp)

Then accept the terms of use.

![Image](assets/fr/07.webp)

The next step is to check your device. This confirms the authenticity of your Passport and ensures that it has not been tampered with in transit. You will be asked to scan a QR code.

![Image](assets/fr/08.webp)

Go to [the official verification site](https://validate.foundationdevices.com/) and select "*Passport*".

![Image](assets/fr/09.webp)

Use your Passport's camera to scan the QR code displayed on the site.

![Image](assets/fr/10.webp)

Your device will then display 4 words.

![Image](assets/fr/11.webp)

Enter these words on the website to confirm the authenticity of your Passport and click on "*Validate*".

![Image](assets/fr/12.webp)

If the message "*Passed*" appears, your hardware wallet is genuine. You can now use it to secure a Bitcoin wallet.

![Image](assets/fr/13.webp)

Confirm the test result on your Passport.

![Image](assets/fr/14.webp)

## Setting the PIN code

Next comes the PIN code step. The PIN code unlocks your Passport. It therefore provides protection against unauthorized physical access. The PIN code is not involved in the derivation of your wallet's cryptographic keys. So even without access to the PIN code, possession of your 12- or 24-word mnemonic phrase will enable you to regain access to your bitcoins.

![Image](assets/fr/15.webp)

We recommend choosing a PIN code that is as random as possible. Also, be sure to save this code in a separate place from where your Passport is stored (e.g. in a password manager).

You can choose a PIN code between 6 and 12 digits. I advise you to make it as long as possible.

Use the keypad to enter your PIN numbers. When you've finished, click on the confirmation button.

![Image](assets/fr/16.webp)

Confirm your PIN a second time.

![Image](assets/fr/17.webp)

Your PIN code has been registered.

![Image](assets/fr/18.webp)

## Update Passport firmware

Your hardware wallet suggests that you update its firmware. I recommend that you update immediately to benefit from the improvements and fixes brought by the latest versions. To continue, click on the confirmation button on the right.

![Image](assets/fr/19.webp)

Your Passport is ready to receive the new firmware via a MicroSD card.

![Image](assets/fr/20.webp)

To do this, use the MicroSD card included in your Passport box (or another one), and insert it into your computer. Download the latest firmware version from [the Foundation documentation site](https://docs.foundation.xyz/firmware-updates/passport/) or [their GitHub repository](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Before installing it on your device, we strongly advise you to check the authenticity and integrity of the downloaded firmware. If you need help with this, consult this tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
After checking the `.bin` file, place it on your MicroSD, then insert it into the Passport. The Passport file explorer will open. Select the file `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Click on "*Select*".

![Image](assets/fr/23.webp)

Then confirm firmware installation.

![Image](assets/fr/24.webp)

Please wait for the update to complete.

![Image](assets/fr/25.webp)

Once the update is complete, enter your PIN code to unlock the device and continue configuration.

![Image](assets/fr/26.webp)

## Create a new Bitcoin wallet

Now it's time to create a new Bitcoin wallet. Click on the confirmation button.

![Image](assets/fr/27.webp)

To create a new wallet, click on "*Create New Seed*".

![Image](assets/fr/28.webp)

You can choose between a 12- or 24-word mnemonic phrase. The security offered by both options is similar, so you can opt for the one that's easiest to save, i.e. 12 words.

![Image](assets/fr/29.webp)

Click on "*Continue*".

![Image](assets/fr/30.webp)

Your Passport will now generate your "*Backup Code*". This is a series of numbers that can be used to decrypt a backup of your wallet stored on a MicroSD. This backup system, specific to Foundation devices, constitutes an additional backup to your mnemonic phrase, but is not compatible with other Bitcoin software.

If you decide to use this "*Backup Code*", be sure to keep it in a different location from your MicroSD containing the encrypted backup of your wallet. You may, however, choose not to use this system if you feel that a good backup of your mnemonic phrase is sufficient.

![Image](assets/fr/31.webp)

Enter your "*Backup Code*" to confirm that you have saved it correctly.

![Image](assets/fr/32.webp)

If a MicroSD has been inserted, the encrypted backup of your wallet has been saved there.

![Image](assets/fr/33.webp)

Your Passport will display your 12-word mnemonic phrase. This mnemonic gives you full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to your Passport.

The 12-word phrase restores access to your bitcoins in the event of loss, theft or breakage of your Passport. It is therefore very important to save it carefully and store it in a secure location.

You can write it on the cardboard supplied in the box, or for added security, I recommend engraving it on a stainless steel base to protect it from fire, flood or collapse.

Click on the confirmation button to see your mnemonic phrase.

![Image](assets/fr/34.webp)

For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
of course, you must never share these words on the Internet, as I'm doing in this tutorial. This sample wallet will be used only on Testnet and will be deleted at the end of the tutorial.**_

Make a physical backup of this sentence.

![Image](assets/fr/35.webp)

Your Passport has been successfully configured. Click on the confirmation button to continue.

![Image](assets/fr/36.webp)

## Menu discovery

Your Passport interface has three main menus:


- "*Account*";
- "*More*";
- "*Settings*".

To navigate between these menus, use the left and right arrows on the directional pad.

### *Account*" menu

In the "*Account*" menu, you'll find the main features of your Bitcoin wallet. You can sign a transaction either via the camera or via the MicroSD port.

![Image](assets/fr/37.webp)

The "*Account Tools*" submenu offers options such as verifying an address, signing a message, or consulting the addresses in your wallet.

![Image](assets/fr/38.webp)

In the "*Manage Account*" submenu, you can connect your Bitcoin wallet to a wallet management software (which we'll cover in the next steps of this tutorial), or view and rename your account.

![Image](assets/fr/39.webp)

### More" menu

In the "*More*" menu, you can create a new account in your wallet, linked to the same mnemonic phrase.

![Image](assets/fr/40.webp)

You can also enter a BIP39 passphrase (see next section) or use a temporary seed.

![Image](assets/fr/41.webp)

### Settings" menu

In the "*Settings*" menu, you'll find all your wallet and device settings.

![Image](assets/fr/42.webp)

The "*Device*" submenu gives you options for customizing screen brightness, setting the delay before auto-lock, changing the PIN code, or renaming the device.

![Image](assets/fr/43.webp)

The "*Backup*" submenu lets you export your encrypted wallet backup, check the validity of an existing backup, or look up your "*Backup Code*" again.

![Image](assets/fr/44.webp)

The "*Firmware*" sub-menu is for updating your Passport's firmware. We recommend that you perform these updates regularly to benefit from the latest fixes and features.

![Image](assets/fr/45.webp)

The "*Bitcoin*" sub-menu lets you change the unit displayed (BTC or satoshis), manage a possible Multisig wallet, or switch to "*Testnet*" mode.

![Image](assets/fr/46.webp)

In "*Advanced*", you can view the words of your mnemonic phrase, perform actions on the inserted MicroSD, reset your Passport to factory settings, or perform an authenticity check, as performed previously.

![Image](assets/fr/47.webp)

You can activate "*Security Words*", a feature that adds a layer of security by displaying two specific words when unlocking the device after entering the first four digits of the PIN code. These words, to be saved during configuration, ensure that the Passport has not been replaced or tampered with. In the event of any discrepancy at a later date, we advise you not to use the device. I advise you to activate this option to prevent most risks of physical compromise of the device.

![Image](assets/fr/48.webp)

Finally, the "*Extensions*" sub-menu lets you activate functions specific to certain uses of the appliance, such as the Whirlpool coinjoin protocol.

![Image](assets/fr/49.webp)

## Add a BIP39 passphrase

Before continuing, if you wish, you can add a BIP39 passphrase. A BIP39 passphrase is an optional password that you can choose freely, and which is added to your mnemonic phrase to reinforce wallet security. With this feature enabled, access to your Bitcoin wallet will require both the mnemonic and the passphrase. Without either, it would be impossible to recover the wallet.

Before configuring this option on your Passport, it is strongly recommended that you read this article to fully understand the theoretical operation of the passphrase and avoid errors that could lead to the loss of your bitcoins:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
To activate it, go to the "*More*" menu and click on "*Enter Passphrase*".

![Image](assets/fr/50.webp)

Enter your passphrase using the aA1 keypad, and make sure you save it one or more times on physical media (paper or metal). For the example, I'm using a very weak passphrase, but you should choose a strong, random passphrase, including all character types and sufficiently long (like a strong password).

![Image](assets/fr/51.webp)

Please note that BIP39 passphrases are case- and typo-sensitive. If you enter a passphrase slightly different from the one initially configured, Passport will not report an error, but will derive another set of cryptographic keys that will not be those in your initial wallet.

It's therefore important, when configuring, to note down somewhere the master key fingerprint you'll be given in the next step. For example, with my passphrase `Plan B Network`, my master key fingerprint is `745D526B`.

![Image](assets/fr/52.webp)

Each time you unlock your Passport, you'll need to return to this menu to enter your passphrase and apply it to your wallet. Passport does not save the passphrase.

Each time you unlock, after writing down the passphrase, check on this confirmation screen that the fingerprint given is the same as the one you wrote down during configuration. If it is, your passphrase is correct and you are accessing the correct Bitcoin wallet. If it's not, you're on the wrong wallet and need to try again, taking care not to make any input errors.

Before you receive your first bitcoins on your wallet, **I strongly advise you to perform an empty recovery test**. Make a note of some reference information, such as your xpub or first receiving address, then delete your wallet on the Passport while it's still empty (`Settings -> Advanced -> Erase Passport`). Then try to restore your wallet using your paper backups of the mnemonic phrase and any passphrase. Check that the cookie information generated after the restore matches the one you originally wrote down. If it does, you can rest assured that your paper backups are reliable. To find out more about how to carry out a test recovery, please consult this other tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
![Image](assets/fr/53.webp)

## Configuring the wallet on Sparrow Wallet

In this tutorial, I'll show you an advanced use of Passport with Sparrow Wallet. However, this hardware wallet is also compatible with Envoy (the Foundation application), Keeper, BlueWallet, Nunchuk, Specter, and many others...

Start by downloading and installing Sparrow Wallet [from the official website](https://sparrowwallet.com/) on your computer, if you haven't already done so.

![Image](assets/fr/54.webp)

Be sure to check the authenticity and integrity of the software before installation. If you don't know how to do this, please consult this tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Once Sparrow Wallet is open, click on the "*File*" tab, then on "*New Wallet*".

![Image](assets/fr/55.webp)

Name your wallet, then click on "*Create Wallet*".

![Image](assets/fr/56.webp)

Select "*Airgapped Hardware Wallet*".

![Image](assets/fr/57.webp)

Click on "*Scan...*" next to the "*Passport*" option. This will open your webcam.

![Image](assets/fr/58.webp)

On your hardware wallet, go to the "*Account*" menu, select the "*Manage Account*" submenu, and click on "*Connect Wallet*".

![Image](assets/fr/59.webp)

In the drop-down list that appears, choose "*Sparrow*".

![Image](assets/fr/60.webp)

Then select "*Single-sig*" for a normal configuration, without multisig.

![Image](assets/fr/61.webp)

Select the "*QR Code*" option.

![Image](assets/fr/62.webp)

Your Passport will then generate dynamic QR codes. Use your computer's webcam to scan them into the Sparrow software.

![Image](assets/fr/63.webp)

You should now see your xpub and your master key fingerprint, which should match the one shown on your Passport when you enter your passphrase. Click on the "*Apply*" button.

![Image](assets/fr/64.webp)

Set a strong password to secure access to your Sparrow Wallet. This password will protect your public keys, addresses, labels and transaction history from unauthorized access. It's a good idea to save this password in a password manager, so you don't forget it.

![Image](assets/fr/65.webp)

Your Passport then prompts you to scan the first reception address to confirm that the import has been successful.

![Image](assets/fr/66.webp)

In Sparrow, go to the "*Receive*" tab and scan the QR code of the first address.

![Image](assets/fr/67.webp)

If the operation is successful, your Passport will display "*Verified*".

![Image](assets/fr/68.webp)

This confirms that the import was successful.

![Image](assets/fr/69.webp)

## Receive bitcoins

Now that your Passport is set up, you're ready to receive your first sats on your new Bitcoin wallet. To do so, on Sparrow, click on the "*Receive*" menu.

![Image](assets/fr/70.webp)

Sparrow will display the first blank receipt address in your wallet. You can add a label.

![Image](assets/fr/71.webp)

Before using it, we'll check the address on the Passport screen to make sure it belongs to our Bitcoin wallet. On Sparrow, you can enlarge the QR code of the address by clicking on it if necessary. In your Passport's "*Account*" menu, select "*Account Tools*".

![Image](assets/fr/72.webp)

Click on "*Verify Address*", then scan the QR code displayed on Sparrow Wallet.

![Image](assets/fr/73.webp)

Make sure that the address displayed on the Passport corresponds exactly to the one shown on Sparrow, and that "*Verified*" appears.

![Image](assets/fr/74.webp)

You can now use it to receive bitcoins. When the transaction is broadcast on the network, it will appear on Sparrow. Wait until you've received enough confirmations to consider the transaction definitive.

![Image](assets/fr/75.webp)

## Send bitcoins

Now that you have a few sats in your wallet, you can also send some. To do so, click on the "*UTXOs*" menu.

![Image](assets/fr/76.webp)

Select the UTXOs you wish to use as inputs for this transaction, then click on "*Send Selected*".

![Image](assets/fr/77.webp)

Enter the recipient's address, a label to remind you of the purpose of the transaction and the amount you wish to send to this address.

![Image](assets/fr/78.webp)

Adjust the fee rate according to current market conditions, then click on "*Create Transaction*".

![Image](assets/fr/79.webp)

Check that all transaction parameters are correct, then click on "*Finalize Transaction for Signing*".

![Image](assets/fr/80.webp)

Click on "*Show QR*" to display the PSBT (*Partially Signed Bitcoin Transaction*). Sparrow has built the transaction, but it still lacks the signatures to unlock the bitcoins used in the input. These signatures can only be performed by the Passport, which hosts your seed giving access to the private keys needed to sign the transaction.

![Image](assets/fr/81.webp)

On your Passport, access the "*Account*" menu and click on "*Sign with QR Code*".

![Image](assets/fr/82.webp)

Scan the PSBT (*Partially Signed Bitcoin Transaction*) displayed on Sparrow Wallet.

![Image](assets/fr/83.webp)

Confirm that the receiving address and the amount sent are correct, then press the confirmation button.

![Image](assets/fr/84.webp)

Check the exchange address. In my example, there is none, as the transaction includes a single output.

![Image](assets/fr/85.webp)

Make sure the fee is the one you have chosen.

![Image](assets/fr/86.webp)

If all the information is correct, click on the confirmation button to sign the transaction.

![Image](assets/fr/87.webp)

On Sparrow Wallet, click on "*Scan QR*" and scan the QR code displayed on your Passport.

![Image](assets/fr/88.webp)

Your signed transaction is now ready to be broadcast on the Bitcoin network and included in a block by a miner. If everything is correct, click on "*Broadcast Transaction*".

![Image](assets/fr/89.webp)

Your transaction has been broadcast and is awaiting confirmation.

![Image](assets/fr/90.webp)

Congratulations, you now know how to configure and use Passport. If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thanks for sharing!

For further information, see our tutorial on Liana software:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04