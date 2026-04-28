---
name: Wallet of Satoshi - Self-Custody
description: Find out how to configure the self-custody mode of a Wallet of Satoshi portfolio
---

![cover](assets/cover.webp)


***Not your keys, not your coins* is more than a saying, it's a fundamental principle of Bitcoin, which means that if you don't control the **private keys** that unlock your bitcoins, you don't really own them.


Many users generally start with a **custodial wallet**, then migrate to a **self-custodial wallet**, where they control their private keys themselves.

In this tutorial, we won't be introducing you to a new self-custodial wallet. Instead, we'll introduce you to a new feature of ***Wallet of Satoshi*** wallets: **the self-custodial mode**.


The aim of this new integration is to enable users to retain control of their private keys while benefiting from simplicity and a fluid user experience.


Before we get to the heart of the matter, let's take a moment to examine the special self-custody mode offered by Wallet of Satoshi (WoS).


## The special feature of the self-custody mode


The simplicity and fluidity of WoS's self-custody mode eliminates the complexity of opening Lightning channels, administering nodes... But how is this possible?


Wallet of Satoshi's self-custody mode is powered by **Spark**. This is a Layer 2 solution for Bitcoin, created by Lightspark, using **statechains** technology.


As a result, you don't carry out your transactions directly on the Lightning Network. Interactions between the **LN** network and **Spark** take place via **atomic swaps**.


For example, Bob wishes to pay a Lightning invoice using WoS. He transfers his satoshis, but in the background, these are routed to a **Spark Service Provider (SSP)** on Spark, which in turn executes the payment on the Lightning network.


Conversely, Alice wishes to obtain funds directly from its WoS portfolio. In this case, the **SSP** receives sats via LN and immediately credits Alice's portfolio.


So, it's important to note that to benefit from the simplicity and fluidity of WoS, you need to depend on Spark's servers. However, in terms of security, if an SSP becomes malicious or unavailable, you have the **unilateral exit** mechanism, a security measure that allows you to recover your funds on Bitcoin on-chain (even if this can be slow and costly) , guaranteeing a self-custodial experience comparable to that of a private Lightning node.


Taking all these parameters into account, you can then decide how much sats you want to keep in your WoS self-custody.


If you're new to Wallet of Satoshi, you'll naturally need to download the mobile wallet application. However, if you're already using it and want to know how to use the **self-custody mode**, please go straight to the **Self-custody mode configuration** section of this tutorial.


## Getting started with Wallet of Satoshi


Go to your application store and download WoS.


![screen](assets/fr/03.webp)


Open the application once the download is complete and press **Start**.


![screen](assets/fr/04.webp)


You will be redirected to the application's main interface. In fact, when you access WoS for the first time, the portfolio is already functional and systematically opens in custodial mode by default.


![screen](assets/fr/05.webp)


Even if you don't want to use WoS in custodial mode, we recommend that you configure it first. To do so, consult this tutorial.


https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Let's move on to the configuration of our WoS in self-custody.


## Self-custody mode configuration


Click on the hamburger menu (3-bar icon) in the top right-hand corner of the main interface.


![screen](assets/fr/06.webp)


Then, in the menu that appears, click on the **Open Self Custody Wallet** submenu.


![screen](assets/fr/07.webp)


WoS immediately tells you that *self-custody mode comes with a recovery phrase. Also, you are solely responsible for the security of your funds*.


![screen](assets/fr/08.webp)


Check the "**I Understand**" button (1), then press the **Open Self Custody Wallet** button (2), which appears in bright yellow.


![screen](assets/fr/09.webp)


### Creating a self-custodial portfolio


After clicking on the **Open Self Custody Wallet** button, click on the **Create a New Wallet** button.


![screen](assets/fr/10.webp)


WoS will then create a self-custody portfolio for you, again within the same application. You'll be able to switch between **custodial** mode (available in certain regions) and **self-custodial** mode at your convenience and at any time.


![screen](assets/fr/11.webp)


Once created, you will be redirected to the main WoS self-custody interface. You'll notice that there are no differences between the general overview and interfaces of a WoS custody portfolio and those of a WoS self-custody portfolio.


### Saving your mnemonic phrase


Tap on the **Keychain + Backup Wallet** icon located at the top of the screen between the Wallet of Satoshi name and the hamburger menu.


![screen](assets/fr/12.webp)


WoS offers two different ways of saving your 12 words (mnemonic phrase): **backup via Google Drive** and **manual backup**.


Although we suggest manual backup, which is the most secure, we'll also show you how to back up via Google Drive.


#### Backup via Google Drive


Click on the **Google Drive Backup** button.


![screen](assets/fr/13.webp)


If you opt for backup with Google Drive, there's a high risk that your Google account will be compromised. A malicious individual would have access to the file containing your 12 words, and could thus gain access to your wallet.


Adding a password to encrypt the file containing your 12 words is certainly a good way of adding an extra layer of security.


So activate the **Encrypt with a password** button in the advanced options.


![screen](assets/fr/14.webp)


On the new interface that appears, set a strong password, then confirm it again.


![screen](assets/fr/15.webp)


It's important to remember that once you've chosen a password, you must not forget it or lose the medium on which you've written it. If you forget or lose it, you will never again be able to access your 12 words, and therefore your funds.


After choosing your password, select a Google account for the backup, then grant the accesses required by WoS.


![screen](assets/fr/16.webp)


![screen](assets/fr/17.webp)


Wait a few seconds. Bingo! Your backup has been successfully completed.


![screen](assets/fr/18.webp)


You always have the option of making an additional backup by choosing the second backup method: manual backup.

#### Manual backup


If you opt for manual backup, we strongly recommend you consult this tutorial, which explores best practices for backing up your mnemonic phrase securely, so you don't lose access to your bitcoins.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Press the **Manual Backup** button.


![screen](assets/fr/19.webp)


On the following interface, WoS reminds you of a few safety precautions to take into account before proceeding with the manual backup.


Activate the **I understand** button and press the **Next** button.


![screen](assets/fr/20.webp)


You will then be presented with your 12 words. Save them, then click on the **Next** button.


![screen](assets/fr/21.webp)


On this new interface, press the words in the right order.


![screen](assets/fr/22.webp)


Finally, click on the **Next** button. Congratulations! Your backup is now complete.


![screen](assets/fr/23.webp)


## Self-custody portfolio restoration


When you want to recover or restore your WoS self-custody wallet following a change of phone or for any other reason, here are the steps to follow.


To open the WoS portfolio, click on the hamburger menu in the top right-hand corner of the main interface.

In the menu that appears, click on the **Open Self Custody Wallet** submenu.

On the new interface that appears, press the **Restore Existing Wallet** button.


![screen](assets/fr/24.webp)


Choose a restoration method and proceed to the next step.


![screen](assets/fr/25.webp)


### Restore via Google Drive


1. Press the **Restore From Google Drive** button.

2. Select a Google account and let WoS retrieve the recovery data saved on your Google Drive.

3. Then enter your encryption password (if you had previously defined it, of course) from the file containing your 12 words.

4. Wait a few moments for the restoration to take effect, and you'll be able to access your portfolio again.


### Manual restoration


1. Press the **Restore Manually** button.

2. Then enter the 12 words of your mnemonic phrase, writing each word in front of its starting number.

3. Wait a few moments for the restoration to take effect, and you'll be able to access your portfolio again.



### Transferring bitcoins between WoS custody and WoS self-custody


When you have bitcoins (sats) in your WoS custody wallet and create a WoS self-custody wallet, you won't lose your funds. Better still, you can transfer them to your self-custody portfolio and vice versa.


To do so :

You can copy your lightning WoS self-custody address or an invoice you've created.


![screen](assets/fr/26.webp)


Now open your custody wallet and press the **Envoyer** button.


Then paste the address or invoice. Press **Envoyer** a second time.


Go back to your self-custody portfolio and you'll see that you had indeed received the funds.


![screen](assets/fr/27.webp)


## Sending and receiving bitcoins


As for sending and receiving bitcoins in self-custody mode, just like the general overview and interfaces, they are no different from sending and receiving bitcoins via a WoS custody wallet.


Please refer to the basic tutorial on using Wallet of Satoshi on the Plan₿ Network.


https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

You can now configure and operate Wallet of Satoshi yourself in self-custody mode.


If you found this tutorial useful, please leave me a green thumb below. Thank you very much!