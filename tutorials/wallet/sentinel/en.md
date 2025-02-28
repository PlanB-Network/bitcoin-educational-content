---
name: Sentinel Watch-Only
description: What is a Watch-Only wallet and how to use it?
---

![cover](assets/cover.webp)

---

**\*WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, the Sentinel app continues to function, but **it is mandatory to use your own Dojo** in order to access blockchain information and broadcast transactions.\*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

> Keep your private keys, private.

In this article, we explore everything you need to know about watch-only wallets. We discuss how they work and examine the different applications available on the market. Finally, we offer a detailed tutorial on one of the most popular watch-only wallet applications: Sentinel.

## What is a Watch-Only Wallet?

A watch-only wallet, or a read-only wallet, is a type of software designed to allow the user to observe transactions associated with one or more specific Bitcoin public keys, without having access to the corresponding private keys.

This type of application only retains the data necessary for monitoring a Bitcoin wallet, including viewing its balance and transaction history, but it does not have access to the private keys. Therefore, it is impossible to spend the bitcoins held in the wallet on the watch-only application.
![watch-only](assets/en/1.webp)
Watch-only is generally used in conjunction with a hardware wallet. This allows for the storage of the wallet's private keys "cold," on a device not connected to the internet, which has a minimal attack surface, isolating the private keys from potentially vulnerable environments. The watch-only application, on the other hand, exclusively stores the extended public key (`xpub`, `zpub`, etc.) of the Bitcoin wallet. This parent key does not allow for the discovery of the associated private keys and, consequently, does not permit the spending of bitcoins. However, it allows for the derivation of child public keys and receiving addresses. With knowledge of the addresses of the wallet secured by the hardware wallet, the watch-only application can track these transactions on the Bitcoin network, offering the user the ability to monitor their balance and generate new receiving addresses, without having to connect their hardware wallet each time.

## Which Watch-Only Wallet to use?

Currently, the most comprehensive watch-only application is [Sentinel](https://sentinel.watch/), developed by the teams at Samourai Wallet. It encompasses all the essential features for a good watch-only wallet:

- Support for extended keys, public keys, and addresses;
- The ability to organize multiple accounts or wallets into collections;
- Generation of addresses to receive bitcoins on one's hardware wallet without requiring its direct use;
- The ability to construct and broadcast transactions offline;
- Option to connect to one's own Bitcoin node;
- Integration of Tor for enhanced privacy.
  The unique drawbacks of Sentinel lie in the fact that the application is exclusively available for Android and it does not support multi-signature wallets. Therefore, if you own an Android device and your wallet is a classic single signature, I recommend Sentinel.
  For those looking to track a multi-signature wallet, Blue Wallet is the only application I know of that offers a watch-only mode for these types of wallets, and it is accessible on both Android and iOS.

For iOS users looking for an alternative to Sentinel, [Green Wallet](https://blockstream.com/green/) or [Blue Wallet](https://bluewallet.io/watch-only/) may be options, although their watch-only functionality is not as comprehensive as Sentinel's.
![watch-only](assets/notext/2.webp)

## How to Use the Sentinel Watch-Only Wallet?

### Installation and Setup

Start by installing the Sentinel application. You can do this either from the Google Play Store or by using the [APK available for download on the official website](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Upon first opening the application, you are given the choice between:

- `Connect to Dojo`;
- `Connect to Samourai's server`.

Dojo, developed by the Samourai team, is a full Bitcoin node version that can be installed standalone or added in one click to node-in-box solutions such as [Umbrel](https://umbrel.com/) and [RoninDojo](https://ronindojo.io/).

[**-> Discover how to install RoninDojo v2 on a Raspberry Pi.**](https://planb.network/fr/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

If you have your own Dojo, you can connect it at this stage. By doing so, you will benefit from the highest level of privacy when checking your Bitcoin network transaction information.

![watch-only](assets/notext/4.webp)

Otherwise, it is possible to opt for Samourai's default server. You can also choose whether to connect via Tor or not.

![watch-only](assets/notext/5.webp)

You will then arrive at the main page of Sentinel.

![watch-only](assets/notext/6.webp)

To get started, you can set up the application. Click on the three small dots in the top right corner, then on `Settings`.

![watch-only](assets/notext/7.webp)
By selecting `User PIN code`, you have the option to set a password to secure access to your watch-only wallet. You also have the ability to change the reference currency for converting your balances into fiat currency, or even to hide fiat values by activating the `Hide fiat values` option. For increased security, you can activate `Disable Screenshots`, which prevents any screenshots of your Sentinel application and thus avoids any disclosure of information on an external screen.
![watch-only](assets/notext/8.webp)

In this settings menu, you also have the option to back up your Sentinel.

### Using the Watch-Only Wallet

From the homepage, press the blue `NEW` button to add a new extended public key to track. You then have the option to scan the QR code of your key, or to directly paste the key (`xpub`, `zpub`...) by selecting `Paste Pubkey`.

![watch-only](assets/notext/9.webp)

Generally, the `xpub` of your wallet is directly accessible via the wallet management software you use. For example, if you manage your hardware wallet with Sparrow, this information is found in the `Settings` tab, under the `Keystore` section.

![watch-only](assets/notext/10.webp)

After entering the extended public key in Sentinel, the application offers you to create a new collection. A collection represents a set of extended public keys organized together. This option gives you the possibility not just to list all your `xpubs`, but to classify them in an orderly manner. For example, if you have a Samourai Wallet with multiple accounts (deposit, premix, postmix...), you can gather all these accounts under the `Samourai` collection. For wallets managed for your family, you might create a collection named `Family`.

Select `Create new collection`. Then enter a name for the extended key you just integrated. For example, if I scan the deposit account of my Samourai wallet, I would name this key `Deposit`. Click on `SAVE` to finalize.

![watch-only](assets/notext/11.webp)

Next, assign a name to this collection and press the validation icon located at the top right of the screen to save the collection. Your collection is now visible on the Sentinel home screen.

![watch-only](assets/notext/12.webp)

If you wish to add another extended public key, click on `NEW` again and enter your key.

![watch-only](assets/notext/13.webp)
You will then be prompted to choose the collection you wish to integrate this key into, or to create a new one. For example, in my case, I've set up a collection specifically for my Ledger wallet.
![watch-only](assets/notext/14.webp)

To see the extended keys of a collection in detail, simply click on it. You can then navigate through the different tabs to view the transaction history.

![watch-only](assets/notext/15.webp)

From a collection, by tapping on the three small dots at the top right, then on `View Unspent Outputs`, you can access a list of UTXOs held by the tracked wallet.

![watch-only](assets/notext/16.webp)

### Sending and Receiving Bitcoins from Sentinel

As with any good watch-only wallet, Sentinel allows you to generate receiving addresses to receive bitcoins on the tracked wallet. But Sentinel also offers another advanced feature: the creation and broadcast of a partially signed Bitcoin transaction (PSBT). Thus, the wallet holding the private keys can sign this transaction, which, once signed, can be broadcast on the Bitcoin network by Sentinel. Let's see how to do all this.

**Caution, it is not recommended to receive bitcoins on a receiving address not verified by the wallet itself.** If the wallet holding the private keys, such as a hardware wallet, has not explicitly confirmed that a certain address is affiliated with it, sending bitcoins to this address is a risky practice. Indeed, without this confirmation, there is no guarantee that the address truly belongs to your wallet. Therefore, the receiving functionality of a watch-only wallet should be used with caution, keeping in mind that the funds sent could potentially be lost.

To receive bitcoins via Sentinel, select the collection of interest, then click on the tab corresponding to the extended public key towards which you wish to transfer funds.

![watch-only](assets/notext/17.webp)

Finally, click on the arrow icon at the bottom left of the screen. Sentinel then generates a blank receiving address for you. You can copy it, or scan it using the QR code.

![watch-only](assets/notext/18.webp)

To generate a PSBT from Sentinel, and thus initiate a spending transaction, go to the extended key of the wallet from which you wish to make the payment. Let's take, for example, my deposit account on my Samourai wallet. Then click on the arrow icon located at the bottom right of the screen.

![watch-only](assets/notext/19.webp)

Enter all the parameters related to your transaction:

- Enter the recipient's address (by clicking on the QR code icon, you have the option to scan this address);
- Specify the amount to send to this address;
- Determine the transaction fees.

Once you have filled in all the necessary fields for your transaction, press the `COMPOSE UNSIGNED TRANSACTION` button.

![watch-only](assets/notext/20.webp)

You will then access the PSBT, which represents a constructed but unsigned Bitcoin transaction, since Sentinel does not have access to your private keys. You have the option to copy this transaction, export it as a `.psbt` file, or scan it via the animated QR code.

![watch-only](assets/notext/21.webp)

Then, go to your wallet that has the private keys to sign the transaction (Samourai, hardware wallet...).

![watch-only](assets/notext/22.webp)

Once the transaction is signed, you can return to Sentinel to broadcast it. To do this, from the home menu, click on the three small dots at the top right, then on `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

You have the option to enter your signed PSBT in three different ways:

- By pasting it directly from your clipboard;
- By importing it from a `.psbt` file;
- By scanning it via a QR code.

![watch-only](assets/notext/24.webp)

Once the signed transaction is entered in the gray frame, you can click on the green `BROADCAST TRANSACTION` button to broadcast it on the Bitcoin network. Sentinel will give you its TXID.

![watch-only](assets/notext/25.webp)
