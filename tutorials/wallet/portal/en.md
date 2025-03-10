---
name: Portal
description: Configuring and using the TwentyTwo-Devices hardware wallet Portal
---
![cover](assets/cover.webp)

Portal is a Bitcoin hardware wallet designed by TwentyTwo Devices, a company specializing in the creation of open-source hardware wallets for bitcoiners. Founded by Alekos Filini, creator of the Magical Bitcoin project ([henceforth named BDK](https://github.com/bitcoindevkit)) and having worked for Blockstream and BHB Network, TwentyTwo Devices aims to focus on user autonomy, simplicity and security.

What sets Portal apart from other hardware wallets on the market is its native integration with smartphones. It works without cables or batteries. It uses NFC technology to power itself and communicate with any compatible mobile wallet. Its intriguing design is conceived for ergonomic use. The round part is placed on the back of the smartphone to reveal a screen where you can check the details of your transactions before signing them with the dedicated button.

![Image](assets/fr/01.webp)

Entirely open-source, the Portal is based on firmware written in Rust and uses BDK (Bitcoin Dev Kit) for key and transaction management. It sells for €89 [on the official website](https://store.twenty-two.xyz/products/portal-hardware-wallet).

At the time of writing, the Portal is compatible with the Nunchuk and Bitcoin Keeper applications. In this tutorial, we'll be configuring it with Nunchuk.

## Unboxing

When you receive your Portal, check that the box and the label sealing it are in good condition. Inside, you'll find your Portal in a sealed pouch.

Make sure the seal is intact to confirm that the pouch has not been opened. The unique number displayed in large letters on the pouch should correspond to the one written in black under the blue seal, to the one on the box label, and to the one that will appear on your screen when you first start up.

![Image](assets/fr/02.webp)

## Nunchuk installation

To manage the wallet hosted on the Portal, we're going to use the Nunchuk application. Download the application from the [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), the [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) or directly via its [file `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).

![Image](assets/fr/03.webp)

If you're using Nunchuk for the first time, the application will prompt you to create an account. For the purposes of this tutorial, it's not necessary to create one. Select "*Continue as guest*" to continue without an account.

![Image](assets/fr/04.webp)

## Portal configuration

On the Nunchuk home screen, click on the "*NFC*" logo at the top of the screen.

![Image](assets/fr/05.webp)

Position your Portal on the back of your smartphone to activate it.

![Image](assets/fr/06.webp)

Nunchuk will recognize your Portal. Then click on "*Continue*".

![Image](assets/fr/07.webp)

To create a new portfolio, select "*Generate seed on Portal*" then click on "*Continue*".

![Image](assets/fr/08.webp)

You can choose between a 12- or 24-word mnemonic phrase. The security offered by both options is similar, so you can opt for the one that's easiest to save, i.e. 12 words.

![Image](assets/fr/09.webp)

You will then be asked to choose a password. The password unlocks your Portal. It therefore provides protection against unauthorized physical access. This password is not involved in the derivation of your wallet's cryptographic keys. So, even without access to this password, possession of your 12- or 24-word mnemonic phrase will enable you to regain access to your bitcoins. It's advisable to choose a password that's as random as possible and long enough. Make sure you save this password in a separate place from where your Portal is stored (e.g. in a password manager).

![Image](assets/fr/10.webp)

Your Portal will display your 12-word mnemonic phrase. This mnemonic gives you full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to your Portal.

The 12-word phrase restores access to your bitcoins in the event of loss, theft or breakage of your Portal. It is therefore very important to save it carefully and store it in a safe place.

You can inscribe it on a piece of paper, or for added security, I recommend engraving it on a stainless steel base to protect it from fire, flood or collapse.

For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

of course, you must never share these words on the Internet, as I'm doing in this tutorial. This sample portfolio will be used only on Testnet and will be deleted at the end of the tutorial.**_

Press the button on your Portal firmly to move on to the next words. Make sure you place your entire finger on the button and hold the pressure for a few seconds, so that the interaction is properly detected.

![Image](assets/fr/11.webp)

Your Portal will then confirm the password you entered in Nunchuk.

![Image](assets/fr/12.webp)

You've now finished configuring your Portal and creating your mnemonic phrase!

![Image](assets/fr/13.webp)

## Bitcoin wallet configuration

On the Nunchuk, click on "*Continue*", still holding your Portal to the back of your phone.

![Image](assets/fr/14.webp)

In this tutorial, I'm going to set up a single-sig portfolio, so I'm selecting this option.

![Image](assets/fr/15.webp)

Use the default account, i.e. the first account in the wallet (number 0). Nunchuk will then ask you to confirm your Portal password to unlock it.

![Image](assets/fr/16.webp)

On the Portal, confirm the export of your xpub to Nunchuk. This allows you to manage the wallet from your smartphone without being able to spend bitcoins without the Portal. Press the button to confirm.

Note that the derivation path indicated in your case will be different from mine, as this tutorial is performed on Testnet.

![Image](assets/fr/17.webp)

Name your portfolio, for example "*Portal*", then click on "*Continue*".

![Image](assets/fr/18.webp)

Nunchuk then presents you with your Descriptor. It's a good idea to make a backup. Although the Descriptor doesn't allow you to spend bitcoins, it does allow you to trace the derivation paths of your keys from your mnemonic phrase in the event of wallet recovery. Keep it in a safe place, because while its leakage may not pose a security problem, it does represent a confidentiality issue.

Click on "*Done*".

![Image](assets/fr/19.webp)

You'll now need to generate the public keys for your Bitcoin wallet. To do this, click on the "*Create new wallet*" button.

![Image](assets/fr/20.webp)

Click again on "*Create new wallet*". Then choose the "*Create a new wallet using existing keys*" option.

![Image](assets/fr/21.webp)

Choose a name for your portfolio and click on "*Continue*".

![Image](assets/fr/22.webp)

Select your Portal as the signing device for this new set of keys, then click on "*Continue*".

![Image](assets/fr/23.webp)

If everything is to your satisfaction, validate the creation.

![Image](assets/fr/24.webp)

You can then save your wallet configuration file. This file contains only your public keys, which means that even if someone accesses it, they won't be able to steal your bitcoins. However, they will be able to track all your transactions. This file therefore only presents a risk to your privacy. In some cases, it may be indispensable for recovering your wallet.

![Image](assets/fr/25.webp)

And that's all there is to it!

![Image](assets/fr/26.webp)

## How can I receive bitcoins with Portal?

To receive bitcoins, select your wallet.

![Image](assets/fr/27.webp)

Before using the generated address, check it on the Portal screen. To do this, click on "*Receive*".

![Image](assets/fr/28.webp)

Click on the three dots, then select "*Verify address via PORTAL*". Then enter your password.

![Image](assets/fr/29.webp)

Position your Portal on the back of your phone, then confirm by pressing the button.

![Image](assets/fr/30.webp)

Make sure that the address displayed on the Portal matches the one on your Nunchuk, then confirm by pressing the button again. If the addresses are identical, you can give this address to the payer.

![Image](assets/fr/31.webp)

Once the payer's transaction has been broadcast, you'll see it appear on your wallet.

![Image](assets/fr/32.webp)

Click on "*View corners*".

![Image](assets/fr/33.webp)

Select your new UTXO.

![Image](assets/fr/34.webp)

Click on the "*+*" next to "*Tags*" to add a tag to your UTXO. This is a good practice, as it helps you remember where your coins come from and optimizes your privacy when spending in the future.

![Image](assets/fr/35.webp)

Select an existing tag or create a new one, then click on "*Save*". You can also create "*collections*" to organize your parts in a more structured way.

![Image](assets/fr/36.webp)

## How do I send bitcoins using Portal?

Now that you have bitcoins in your wallet, you can also send them. To do so, click on the wallet of your choice.

![Image](assets/fr/37.webp)

Click on the "*Send*" button.

![Image](assets/fr/38.webp)

Select the amount to send, then click on "*Continue*".

![Image](assets/fr/39.webp)

Add a "*note*" to your future transaction to remind you of its purpose.

![Image](assets/fr/40.webp)

Then enter the recipient's address in the field provided. You can also scan an address encoded as a QR code by clicking on the icon at the top right of the screen. Then click on the "*Create Transaction*" button.

![Image](assets/fr/41.webp)

Check your transaction details, then click on the "*Sign*" button next to your Portal, and enter your password.

![Image](assets/fr/42.webp)

Place your Portal on the back of your phone. Check that the recipient's address and the amount are correct. If so, press the button to continue.

![Image](assets/fr/43.webp)

Check that the transaction fee is correct, then press the button again to sign your transaction.

![Image](assets/fr/44.webp)

Your transaction has been signed. You can check its details one last time on Nunchuk, then click on the "*Broadcast transaction*" button to broadcast it on the Bitcoin network.

![Image](assets/fr/45.webp)

Your transaction is now awaiting confirmation.

![Image](assets/fr/46.webp)

Congratulations, you've now got the hang of using Portal! If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!

To find out more, take a look at our complete training course on how HD portfolios work:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
