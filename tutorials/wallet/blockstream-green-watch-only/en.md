---
name: Blockstream Green - Watch-Only
description: Watch-only portfolio configuration
---
![cover](assets/cover.webp)

In this tutorial, you'll discover how to easily set up a "watch-only" portfolio on mobile using the Blockstream Green application.

## What is a Watch-Only Wallet?

A read-only wallet, or "watch-only wallet", is a type of software designed to allow the user to observe transactions associated with one or more specific Bitcoin public keys, without having access to the corresponding private keys.

This type of application stores only the data needed to monitor a Bitcoin wallet, notably to view its balance and transaction history, but it has no access to private keys. As a result, it is impossible to spend Bitcoins held by the wallet on the watch-only application.

![GREEN-WATCH-ONLY](assets/fr/01.webp)

Watch-only is generally used in conjunction with a hardware wallet. This enables the wallet's private keys to be stored securely, on hardware that is not connected to the Internet and has a very small attack surface, thus isolating the private keys from potentially vulnerable environments. The watch-only application, on the other hand, exclusively stores the extended public key (`xpub`, `zpub`, etc.) of the Bitcoin wallet. This parent key cannot be used to find the associated private keys, and therefore cannot be used to spend Bitcoins. However, it does enable the derivation of child public keys and receiving addresses. Thanks to the hardware wallet's knowledge of secure wallet addresses, the watch-only application can track these transactions on the Bitcoin network, enabling the user to monitor his balance and generate new receiving addresses, without having to connect his hardware wallet each time.

In this tutorial, I'd like to introduce you to one of the most popular watch-only mobile wallet solutions: **Blockstream Green**.

![GREEN-WATCH-ONLY](assets/fr/02.webp)

## Introducing Blockstream Green

Blockstream Green is a software application available on mobile and desktop. Formerly known as Green Address, this portfolio became a Blockstream project following its acquisition in 2016.

Green is a very easy-to-use application, making it particularly suitable for beginners. It offers a range of functions, such as management of hot wallets, hardware wallets and Liquid sidechain wallets.

In this tutorial, we'll concentrate solely on creating a watch-only portfolio. To explore other uses of Green, please consult our other dedicated tutorials:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
## Installing and configuring the Blockstream Green application

The first step is of course to download the Green application. Go to your application store:

- [For Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN-WATCH-ONLY](assets/fr/03.webp)

For Android users, you can also install the application via the `.apk` file [available on Blockstream's GitHub](https://github.com/Blockstream/green_android/releases).

![GREEN-WATCH-ONLY](assets/fr/04.webp)

Launch the application, then check the "I accept the conditions...*" box.

![GREEN-WATCH-ONLY](assets/fr/05.webp)

When you open Green for the first time, the home screen appears without a configured portfolio. Later, if you create or import portfolios, they will appear in this interface. Before going on to create a portfolio, I advise you to adjust the application settings to suit your needs. Click on "Application settings".

![GREEN-WATCH-ONLY](assets/fr/06.webp)

The "*Enhanced Privacy*" option, available only on Android, enhances privacy by disabling screenshots and hiding application previews. It also automatically locks application access as soon as your phone is locked, making your data more difficult to expose.

![GREEN-WATCH-ONLY](assets/fr/07.webp)

For those wishing to enhance their privacy, the application offers the option of rooting your traffic via Tor, a network that encrypts all your connections and makes your activities difficult to trace. Although this option may slightly slow down the application's operation, it's highly recommended to protect your privacy, especially if you're not using your own complete node.

![GREEN-WATCH-ONLY](assets/fr/08.webp)

For users who have their own complete node, Green Wallet offers the possibility of connecting to it via an Electrum server, guaranteeing total control over Bitcoin network information and the distribution of transactions.

![GREEN-WATCH-ONLY](assets/fr/09.webp)

Another alternative feature is the "*SPV Verification*" option, which allows you to verify certain blockchain data directly and thus reduce the need to trust Blockstream's default node, although this method does not provide all the guarantees of a full node.

![GREEN-WATCH-ONLY](assets/fr/10.webp)

Once you've adjusted these settings to your needs, click on the "*Save*" button and restart the application.

![GREEN-WATCH-ONLY](assets/fr/11.webp)

## Create a watch-only portfolio on Blockstream Green

You are now ready to create a watch-only portfolio. Click on the "*Get Started*" button.

![GREEN-WATCH-ONLY](assets/fr/12.webp)

You'll be able to choose between several types of wallet. For this tutorial, we want to create a watch-only portfolio, so click on the corresponding button.

![GREEN-WATCH-ONLY](assets/fr/13.webp)

Choose the "Single signature" option.

![GREEN-WATCH-ONLY](assets/fr/14.webp)

Then select "*Bitcoin*". For my part, I'm doing this tutorial on a testnet wallet, but the procedure remains identical on the mainnet.

![GREEN-WATCH-ONLY](assets/fr/15.webp)

You will be asked to provide either an extended public key (`xpub`, `zpub`, etc.) or an output script descriptor.

![GREEN-WATCH-ONLY](assets/fr/16.webp)

You will therefore need to retrieve this information from the wallet you wish to track via your watch-only wallet. The extended public key is not sensitive in terms of security, as it does not allow access to private keys, but it is sensitive for your confidentiality, as it reveals all your public keys and therefore all your Bitcoin transactions.

Let's say you're using Sparrow Wallet to manage your wallet on a hardware wallet, you'll find this information in the "*Settings*" section. Finding this information will depend on the wallet management software you use, but it's usually in the settings.

![GREEN-WATCH-ONLY](assets/fr/17.webp)

Copy your extended public key and enter it in the Green application, then click on "Connect".

![GREEN-WATCH-ONLY](assets/fr/18.webp)

You will then be able to see the balance associated with this key, as well as the transaction history.

![GREEN-WATCH-ONLY](assets/fr/19.webp)

By clicking on "*Receive*", you can generate a receive address to receive bitcoins on your hardware wallet. However, I would advise against using this option without first checking on the hardware wallet screen that it has the private key associated with the generated address, before using it to lock bitcoins. This is a good practice to follow.

![GREEN-WATCH-ONLY](assets/fr/20.webp)

The "*Balayer*" option lets you manually enter a private key to spend funds directly from your Green application. Except in very specific cases, I don't recommend using this function, as it requires you to reveal your private key on a phone, which is far more vulnerable to computer attacks than your hardware wallet.

![GREEN-WATCH-ONLY](assets/fr/21.webp)

So now you know how to easily set up a watch-only wallet on your smartphone! It's a handy tool for monitoring a wallet on a hardware wallet without having to connect and unlock it every time.

If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!

I also recommend you check out this other comprehensive tutorial on the Blockstream Green application to set up a hot wallet:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143