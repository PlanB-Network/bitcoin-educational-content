---
name: Misty Breez
description: The bowless Lightning wallet.
---

![misty-breez-cover](assets/cover.webp)


![video](https://youtu.be/mibKrTvtlyQ)

Misty Breez is a Lightning self-holding wallet developed by Breez based on their Software Development Kit and the **Liquid** network developed by BlockStream.

It comes with a completely new approach to operating without a Lightning node: a potential **GAME CHANGER** in Bitcoin inter-network transfers.

In this tutorial, we'll describe how this wallet works and give you a complete overview.


## How does Misty Breez work?


Misty Breez is an implementation without a Lightning node as backend. It has been developed on the basis of Breez SDK and Liquid.


Liquid is a parallel layer to the Bitcoin network, offering significant improvements in speed and transaction costs. This layer allows Misty Breez to dispense with a Lightning node and instead use third-party exchange services such as **Boltz** to ensure interoperability between the Liquid network and the Lightning network. Don't hurry, we'll come back to this.


For now, let's start our adventure with the Misty Breez wallet.


## Getting started with Misty Breez


The Misty Breez mobile app is available on official download platforms such as Google Play Store (on Android) and Apple Store (on iOS). You can also be redirected to the right app from the official [Misty Breez] website(https://breez.technology/misty/).


⚠️ Make sure you don't confuse Misty Breez with the Breez wallet.


⚠️ **IMPORTANT**: For the security of your bitcoins, it is essential to download the application from official platforms to ensure its authenticity.


![download-misty-breez](assets/fr/01.webp)


In this tutorial, we'll be starting from an Android device. Nevertheless, each of the steps and specific features detailed in this section apply to iOS.


Upon installation, Misty Breez gives you the option of creating a new wallet or restoring an old Lightning wallet for which you have the recovery words.

In this tutorial, we choose to create a new wallet.


⚠️Misty Breez is currently in the development phase, so we advise you to start with reasonable amounts.


![create-wallet](assets/fr/02.webp)

### Save your recovery words :

One of the first things you should do when creating a new wallet is to back up your 12 recovery words.

Here are some tips on how to back up your backup phrase.


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

To back up your phrases, select the **Preferences > Security** menu, then the **Check your Backup Phrase** option.


![backup](assets/fr/03.webp)

For added security, you can also **create a PIN code** to authenticate access to your wallet.



Find your local currency in the multitude of currencies accepted by Misty Breez. Configure your currency from the **Preferences > Fiat Currencies** menu, then select the currency or currencies you require.


![devises](assets/fr/04.webp)


### Making your first transactions

If you're already familiar with the Breez wallet, you won't be at all put off by Misty Breez's intuitive Interface.


On the Interface **Balance** menu, click on the **Receive** option to create invoices to receive your bitcoins on your wallet.


⚠️ Misty Breez will ask you to activate notifications for the application in your phone's settings to entitle you to a Lightning address.


With Misty Breez, you can :


- Receive bitcoins on the Lightning network from **100 satoshis** up to **25,000,000 satoshis**.
- Receive bitcoins on the Bitcoin main network from **25,000 satoshis**.


![transactions](assets/fr/05.webp)


This is where the magic of Misty Breez begins.

Unlike the Breez wallet, which provides you with a Lightning node and asks you to cover the costs of opening and closing payment channels yourself, Misty Breez doesn't ask you to do anything. As mentioned earlier, Misty Breez doesn't even work on the basis of a Lightning node.


Let's take a closer look behind the scenes.


In reality, you own a Liquid wallet which is associated with your Misty Breez wallet. Logically, you'll be handling L-BTC (Liquid Bitcoin) at fixed rates associated with third-party submarine satoshis conversion services that will enable you to interoperate with the Lightning network.


When you receive a payment on your Misty Breez wallet, your sender sends you satoshis which will go through a conversion service like Boltz (currently used by Misty Breez), to convert the satoshis sent into L-BTC which will be received on your Misty Breez wallet (associated Liquid wallet).

Here's a simplified diagram of the process behind the scenes.


![lnswap-in](assets/fr/06.webp)


Click on the Interface in the **Balance** menu, click on the **Send** option to pay a Lightning invoice.

Insert the Lightning invoice, your recipient's Lightning address or simply scan the QR code on the invoice to make your payment.


![send-bitcoins](assets/fr/07.webp)


Behind the scenes, you enable the Liquid wallet associated with your Misty Breez wallet to convert the equivalent of L-BTC into satoshis via Boltz, then transfer these satoshis to your recipient's Lightning wallet (present on the Lightning network).


![send-bitcoin-bts](assets/fr/08.webp)


This feature of Misty Breez's infrastructure enables users to carry out transactions even when Misty Breez is offline.


For the more experienced, there's also a menu **Preferences > Developers** that gives you a little more detail on :


- The version of the Breez Software Development Kit.
- The public key of your Misty Breez wallet.
- The borrower, the unique identifier derived from the primary public key.
- Your wallet balance.
- Tip Liquid, for sending small amounts of L-BTC.
- The Bitcoin Tip, for sending small amounts of Bitcoin.


You can also perform certain actions, such as synchronizing with the Liquid network, backing up your keys, sharing your activity log and choosing to rescan the Liquid network.


![dev-mode](assets/fr/09.webp)

Congratulations! You now have a good understanding of the Misty Breez wallet and its contribution to Bitcoin inter-network transactions. If you've found this tutorial useful, please give us a green thumb. We'd be delighted to hear from you.


To go further, I also recommend that you discover our tutorial on the Aqua wallet, which works in a similar way to Misty Breez :


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125