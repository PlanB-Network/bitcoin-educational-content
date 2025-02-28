---
name: Proton Wallet
description: Installing and using the Proton Bitcoin wallet
---
![cover](assets/cover.webp)

Proton is a Swiss company specializing in digital privacy, founded in 2014 by CERN scientists. Known for its open source solutions, Proton offers a suite of services including Proton Mail, Proton VPN and Proton Drive.

Proton recently introduced Proton Wallet, an open-source, self-custody Bitcoin wallet available as a mobile app or web client, linked to your Proton account. The wallet's functionalities are relatively classic for the moment, with the essential tools expected of a good Bitcoin wallet, such as RBF (*Replace-By-Fee*), tagging, or the ability to add a BIP39 passphrase.

The special feature of this wallet is the ability to send bitcoins using the recipient's email address, for which Proton automatically generates a blank Bitcoin address linked to the user's wallet. Proton plans to add new features in the future, including Lightning and coinjoins (probably using Whirlpool, as suggested by activity on their GitHub repository).

## Create a Proton account

To use Proton Wallet, you need a Proton account. You can create one for free by following the first steps of this tutorial dedicated to creating a Proton mailbox (only the "*Creating a Proton account*" section). Once your account is set up, you can continue with the rest of this tutorial.

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
## Connect to Proton Wallet

Go to [the Proton Wallet website](https://proton.me/wallet) and click on the "*Get Proton Wallet*" button.

![Image](assets/fr/01.webp)

Choose the "*Free*" subscription option, then click on "*Sign In*".

![Image](assets/fr/02.webp)

Enter the email and password associated with your Proton account to log in.

![Image](assets/fr/03.webp)

Your account should now be displayed. Click on "*Start using Proton Wallet now*".

![Image](assets/fr/04.webp)

## Create a Bitcoin wallet

Select the default fiat currency for your account, then click on "*Create new wallet*".

![Image](assets/fr/05.webp)

Your Bitcoin wallet has now been created. You can theoretically start using it immediately, but it's very important to save your mnemonic first. To do this, click on "*Secure your wallet*" in the top right-hand corner of the interface.

![Image](assets/fr/06.webp)

If you haven't already done so on Proton, you will be asked to set up a backup for your account and secure it using a 2FA method. These security measures, although applicable to your entire Proton account, are all the more relevant when your Bitcoin wallet is integrated into it. I strongly recommend that you implement them.

![Image](assets/fr/07.webp)

To save your mnemonic phrase, click on "*Backup this wallet's seed phrase*".

![Image](assets/fr/08.webp)

Enter your Proton password.

![Image](assets/fr/09.webp)

Then click on "*View wallet seed phrase*" to display your wallet's mnemonic phrase.

![Image](assets/fr/10.webp)

Proton Wallet displays your 12-word mnemonic phrase. **This mnemonic gives you full, unrestricted access to all your bitcoins**. Anyone in possession of this phrase can steal your funds, even without access to your Proton account. The 12-word phrase can be used to restore access to your bitcoins if you lose access to your account. It is therefore very important to save it carefully and store it in a secure location.

You can write it on a piece of paper, or for added security, I recommend engraving it on a stainless steel base to protect it from fire, flood or collapse.

![Image](assets/fr/11.webp)

For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
_**Of course, you should never take a picture of these words, unlike what I do in this tutorial.**_

Click on the "*Done*" button once you've saved your phrase.

![Image](assets/fr/12.webp)

## Discover the interface

Proton Wallet's interface is highly intuitive. On the left, you'll find your different wallets and their associated accounts. The "*Primary*" account is your main account. For reasons of confidentiality, bitcoins received via the Proton email address are placed in a separate account, named "*Bitcoin via Email*".

![Image](assets/fr/13.webp)

To add a new account, click on "*Add account*".

![Image](assets/fr/14.webp)

To create a new wallet, click on the "*+*" symbol next to "*Wallets*".

![Image](assets/fr/15.webp)

This is where you can add a BIP39 passphrase to a new wallet.

![Image](assets/fr/16.webp)

To deepen your knowledge of the passphrase, I recommend this tutorial:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
## Receive bitcoins

To receive bitcoins in your wallet, select the desired account on the left of the interface, then click on the "*Receive*" button.

![Image](assets/fr/17.webp)

Proton Wallet then automatically generates a new, blank address.

![Image](assets/fr/18.webp)

Once the transaction has been completed, you'll find it in the "*Transactions*" section. Click on "*+Add*" to assign a label to the transaction.

![Image](assets/fr/19.webp)

## Send bitcoins

Now that you have bitcoins in your wallet, you can send them. Select the account of your choice on the left-hand side of the interface, then click on "*Send*".

![Image](assets/fr/20.webp)

Enter the recipient's Bitcoin address. You can scan a QR code by clicking on the small logo. To send to an e-mail address, enter it directly in this field. Once you've entered the Bitcoin address, click on the little arrow and then on "*Confirm*".

![Image](assets/fr/21.webp)

Enter the amount to be sent, either in fiat currency or in bitcoins, then click on "*Review*".

![Image](assets/fr/22.webp)

Select the transaction fee based on the current market situation.

![Image](assets/fr/23.webp)

Add a label to your transaction, then double-check all the details. If everything is correct, click on "*Confirm and send*" to sign and send the transaction.

![Image](assets/fr/24.webp)

Your transaction will now appear awaiting confirmation in the "*Transactions*" section of your account.

![Image](assets/fr/25.webp)

## Login to the application

In addition to the web client, Proton Wallet is also accessible via a mobile application. By linking the wallet to your Proton account, you can synchronize your wallet between the web client and the mobile app.

Download Proton Wallet from your application store:


- [On the App Store](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [On Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

After installation, click on "*Log in*" and enter your email address and Proton password.

![Image](assets/fr/27.webp)

You'll then have access to your Bitcoin wallet, with the same features as on the web client.

![Image](assets/fr/28.webp)

Congratulations, you now know how to set up and use Proton Wallet. If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thanks for sharing!

To go further, I recommend this tutorial on Jade Plus, Blockstream's latest hardware wallet:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262