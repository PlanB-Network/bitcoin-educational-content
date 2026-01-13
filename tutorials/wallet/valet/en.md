---
name: Valet Bitcoin
description: Valet brings non custodial Lightning node into your pocket
---

![cover_valet](assets/cover.webp)


## Introduction

Valet is a Lightweight, self-custodial, Bitcoin and Lightning wallet that offers an easy and convenient onboarding process for beginners. It was specifically tailored to serve Bitcoin communities and circular economies, especially in remote areas.

It is a fork of the **Simple Bitcoin Wallet (SBW)**, with an advanced Hosted Lightning channel feature called **Fiat Channels**, designed to enable anyone accept Lightning payments without volatility risks.

Valet is currently only available for Android devices, and can be downloaded and installed from several open-sourced app stores. However, Valet is **not** hosted on the **Google Play Store** because of developer privacy and KYC concerns.


## Download and Install Valet

Valet can be downloaded as an APK file from the Standard Sats' GitHub page. [Standard Sats](https://standardsats.github.io/) is the company that developed Valet.

👉 To download Valet, visit the Standard Sats [GitHub page](https://github.com/standardsats/valet/releases), and locate the **latest** release (This is often the topmost one).

👉 Go to **Assets** and click on the file with only a **.apk** extension. Your download will start automatically.

![Standard_Sats_GitHub_page_view](assets/en/001.webp)

👉 Once the download is complete, go to your device's **File manager** > **Downloads**, and select the Valet apk file.

![Select_valet_apk](assets/en/002.webp)

👉 Install it, and in a few seconds, your app will be ready and will appear on your home screen.

![valet_icon_on_homescreen](assets/en/003.webp)

Alternatively, you can also download Valet from the **F-Droid** app store. If you don't have the F-Droid app on your device, you can download and install it [here](https://f-droid.org/en/).

👉 On your home screen, open F-Droid and search for **Valet**. Select the first option with a **purple and white icon** from the two options that will appear, and click **Download**.

![F-Droid_icon_on_homescreen](assets/en/004.webp)

![search_and_download_Valet](assets/en/005.webp)

👉 After downloading, click **Install** and follow the on-screen instructions. When the installation is completed, you can launch Valet from F-Droid by clicking **Open**, or launch it from your device's home screen.


## Creating a Bitcoin Wallet

You can set up a Bitcoin wallet on Valet in two simple steps.

👉 Launch Valet from your device's home screen or from the F-Droid app. A wallet setup screen will appear, with two options: **Create New Wallet** and **Restore Existing Wallet**.

👉 Select **Create New Wallet**, and instantly, a new wallet will be created, and you will be redirected to the home page.

![set_up_a\_new_wallet](assets/en/006.webp)


## Backup Your Seed Phrase

👉 On the wallet home page, click on the **Green card** that has an inscription **"Tap to save wallet recovery phrase in case you ever lose or replace your device".**

![seed_phrase_green_card](assets/en/007.webp)

👉 A set of 12 English words will be displayed. Write them down on paper, in the order of 1 to 12, and keep them safe.

![the_seed_phrase](assets/en/008.webp)

### Pay Attention ⚠️:

Pay attention to the following elements:
-   As you already know, Valet is a self-custodial wallet, so your seed phrase is the only access to recovering your Wallet.
-   If you ever lose your seed phrase, you will **never** get access to your wallet.
-   If someone gets your seed phrase, they can irretrievably steal all your Bitcoins.

So, you'll need to write down your 12-word seed phrase and keep it in a safe location. You should never take a screenshot, save it as a draft in your email, or save it on any electronic device that has ever been connected to the internet.

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Receiving and Sending Bitcoins on Valet

Valet is a self-custodial wallet with both on-chain and Lightning Bitcoin capability. This means that you can receive and send Bitcoin out of Valet either via an **On-chain** or via a **Lightning Network**.

However, to be able to receive or send Bitcoin through Lightning, you need to set up a Lightning channel using your on-chain Bitcoins as Liquidity. Or you can buy some Lightning channel liquidity from vendors.


## Generating an On-chain Bitcoin Address

To receive Bitcoin through on-chain, you'll need to generate a Bitcoin address.

👉 On the wallet home page, you will see an **Orange** and a **Purple card**, respectively labeled **Bitcoin** and **Lightning**.

👉 Click on the Orange card labeled **Bitcoin**. You'll be redirected to a screen displaying a Bitcoin address.

![click_on_Bitcoin_card](assets/en/009.webp)

👉 You can **copy** the address and send it to the person who is sending Bitcoins to you, or click the **share** button to send the QR code to the person via social media or other communication channels.

👉 You can also click on the **Edit** button to set the amount of Bitcoins that should be sent to that address.

**Attention:** Like an invoice, the edit feature comes in handy in scenarios where you may want to receive a specific amount of Bitcoins to an address at a point; however, this does not mean that the address cannot receive higher or lower amounts.

👉Click on **More fresh addresses**, to generate new random addresses.

![generating_a\_bitcoin_add](assets/en/010.webp)

👉 You can also generate an on-chain Bitcoin address by clicking on the **Receive** button at the bottom of your wallet home page. Then select **Receive to bitcoin address**, and continue with the same process above.

![click_receieve_button](assets/en/011.webp)

![receive_to_bitcoin_address](assets/en/012.webp)


## Sending Bitcoin via On-chain

Sending out Bitcoin from the Valet wallet via on-chain is a straightforward task.

👉 At the bottom of your wallet's home page, click on the **Send** button, enter the Bitcoin address, or click **Scan**, to scan the address QR code, then click **Ok**.

![click_send_button](assets/en/013.webp)

![enter_bitcoin_add](assets/en/014.webp)

👉 Enter the Bitcoin amount you want to send. You can manually enter an amount in terms of Sats or in Fiat currency terms, or you can click on **Max** to use all your on-chain balance.

👉 You can also adjust the fees you want to pay for the transaction by clicking on the small green box labeled **fee** and then sliding the white dot right or left to increase or decrease the fees, respectively. Click **Ok** to send the transaction.

![enter_amount_and_fee_rate](assets/en/015.webp)


## Setting Up a Lightning Network Channel

As mentioned above, Valet is a self-custodial Bitcoin and Lightning wallet; hence, to be able to send and receive Bitcoin through the Lightning network, you will have to set up a Lightning channel first, following these steps:

👉 On the home screen, click on the **Purple card** labeled **Lightning**. You will be taken to a page with the following options:

-   Scan Node QR
-   Purchase at LNBIG.COM
-   Purchase at BITREFILL.COM
-   Request LN graph resync.

When you select **Purchase from lnbig.com** or **Purchase from bitrefill.com**, you will be redirected to the websites of these companies, where you can purchase an inbound liquidity of several capacities. Ignore the last option **Request LN graph resync** for now.

So our go-to choice here is to **Scan a Node QR**. At this point, you must have decided and obtained the **QR code** of the node you want to open a channel to. You can open channels to any public node of your choice. Check out [1ML](https://1ml.com/) or [Amboss](https://amboss.space/), select any public node of your choice, and scan the associated QR code of the node you chose.

![channel_opening_options](assets/en/016.webp)

👉 You will automatically be redirected to the next page, where you must now fund your channel. Again, self-custodial Lightning network usage requires that you use your Bitcoins to fund a channel. This means that you must have Bitcoins in your on-chain wallet with which to fund the Lightning channel. Please refer to this article by [Hacken](https://hacken.io/discover/lightning-network/), read more about the Lightning network.

![fund_channel](assets/en/017.webp)

👉 Enter the **amount** of Bitcoins you want to fund the channel with, or click on **Max** to use all your on-chain Bitcoin balance. You may adjust the **fee**, or leave the default fee setting, and click **Ok**.

**Attention:** The amount you fund the channel with will be the capacity of your new channel (i.e., the total volume of Sats that can be transacted to and from that channel)

It is also important that you use over **100,000 Sats** as the funding amount when opening a channel. This is because a lot of Lightning nodes require a minimum of 100,000 Sats capacity to open a channel to them. So, to avoid trial and error, simply use amounts higher than that range.

![enter_funding_amount](assets/en/018.webp)

![funding_approval](assets/en/019.webp)

👉 At this point, when you check your wallet home page, you will see that your funding amount has now been moved from the **Bitcoin card** to the **Lightning card**. On your transaction history, you'll see the funding transaction being processed.

![channel_funding_processing](assets/en/020.webp)

👉 If you click on the Lightning card, you will see information showing that your Lightning channel is opening. You will also see the **channel funding transaction** on your list of transactions. Wait for your funding transaction to be confirmed on the blockchain, and your Lightning channel will be ready.

![channel_opening](assets/en/021.webp)

👉 As soon as the funding transaction is confirmed, click on the **Lightning card** on your home page, and you will see the information about your Lightning channel as follows:

- **RANDOM SET OF NUMBERS SEPARATED BY DOTS:** These are the nodes' IP addresses. (IPV4 and IPV6, respectively)
- **CAPACITY:** This is the total volume of Sats that can be sent and received through this channel
- **CAN SEND:** This is the amount of Sats you can send out at this point. You'll notice that it is almost the same figure as the **Capacity**. This is because you have not sent out any payments through the channel.
- **CAN RECEIVE:** This is the number of Sats you can receive to this channel at the moment. (It will be little to nothing at this point because for you to be able to receive, you must first send out some Sats to create an inbound Liquidity)
- **REFUNDABLE:** This displays the amount that gets paid back to your on-chain address when you close your channel. This is also referred to as your **Channel's local balance**. Notice that it is just slightly less than the channel capacity, and this is because when closing a channel, you must pay a fee to publish the closing transaction on the blockchain, just like you did while funding the channel. So the system has deducted the approximated lowest amount you'll pay.)
- **VALUE IN FLIGHT:** When someone sends some sats to your channel, or when you try to send some sats to someone, and for whatever reason, the transaction is delayed, it's often shown in this field.

![channel_info](assets/en/022.webp)

## Sending Sats Through Your Channel

Sending Sats through the Lightning Network is a straightforward task.

👉 At the bottom of the home page, click on **Send**, and **paste** the Lightning invoice (you must have copied it) in the provided field, or click on **Scan** to scan the Lightning invoice QR code.

![click_send_or_scan](assets/en/023.webp)

Most Lightning invoices come with a pre-entered amount to be paid. But in a few cases, it may be an open invoice where you have to fill in the amount.

👉 Enter the amount in **Dollars** or **Sats**, or click on **Max**, to use all the balance on your Lightning channel, and then click **Ok**. As soon as a good path is found, your payment will be sent and completed within a few seconds. Keep an eye on the home page to see if the payment has been completed. It will get a green check mark when it has been completed.

![enter_the_amount](assets/en/024.webp)

## Receiving Sats Through Your Channel

Receiving payments on your Lightning channel is largely dependent on whether you have an inbound Liquidity or not. After opening a channel, you will not be able to receive payments until you have at least sent some Sats to **create inbound liquidity** on the other end of the channel connection. To confirm whether you can receive Sats and the amount of Sats you can receive, check the **Can Receive** field in your channel information. This will show you how many Sats you receive at each point in time.

Now, let's assume you have sent out some Sats from your channel, you now have inbound liquidity, and can receive Sats.

To receive on the Lightning channel, you'll have to generate an invoice. Unlike Bitcoin on-chain, which uses addresses, the Lightning network uses invoices. There are two routes to generate an invoice on Valet.

#### OPTION 1

👉 At the bottom of the home page, click on **Receive**, select **Receive to Lightning invoice**. Fill out the amount to be received in the invoice, and click **Ok**. Copy the invoice or share the QR code with the payer.

![receive_to_channel](assets/en/025.webp)

![fill_invoice_amount](assets/en/026.webp)

![copy_invoice_or_share_QR](assets/en/027.webp)

#### OPTION 2

👉 Click on the purple Lightning card on your wallet home page. Tap anywhere on your channel, and a list of options will pop up. Select **Receive to channel** and enter the amount you are receiving (either in Sats or dollars). You will also see how many Sats you can receive (inbound capacity) when you're filling the invoice. Click **Ok** and copy the invoice or share the QR code with the payer.

![receive_to_channel](assets/en/028.webp)

**Attention:** The first option is a universal option, which means that if you have more than one active channel and you use the first option, the system will automatically select one of your channels for receiving the Sats.

So, in this scenario, the second option is best to use if you want to receive Sats to a particular channel.

### Your Channel Pop-Up Options Explained

When you tap on your channel, the following option fields will be displayed:

![channel_pop_ups](assets/en/029.webp)

**SHARE LIGHTNING CHANNEL DETAILS:** This enables you to share your channel details, such as remote peer ID, local channel ID, Funding transaction, date of creation, etc.

**CLOSE CHANNEL TO WALLET:** You can close your lightning channel whenever you want. To close your channel, the system checks the Bitcoin balance you have on your own side of the channel (remember the **"Can Send"** field, also known as your local balance), and it sends it back to you. In Valet, you get to choose where you want that Bitcoin to be sent when the channel is closed. So, **Close channel to wallet** is one of your two options.

👉 Click this option, and select **Bitcoin**. The channel closure will commence, and your channel Bitcoin balance will be sent back to your wallet's on-chain address.

![close_channel_to_wallet](assets/en/030.webp)

**CLOSE CHANNEL TO ADDRESS:** This is the second option for closing a channel. When you choose this option, you will be prompted to enter a wallet address to which the Bitcoin balance on your channel will be sent. Please note that in this option, you can only scan the QR code of the Bitcoin address you want to close the channel to. Currently, there's no option for manual pasting of the address.

👉 Click on this option, scan the Bitcoin address, and click **Ok**. The channel closure will commence, and your Lightning Bitcoin balance will be sent to the address you scanned.

![scan_address_and_Ok](assets/en/031.webp)

**RECEIVE TO CHANNEL:** This is the same thing as generating an invoice, but in some cases, you may have more than one channel, including Fiat channels (a unique kind of Lightning channel obtainable in the Valet wallet). So, if you have multiple channels open, this option ensures that you can receive payment to a specific channel.

**REFILL FROM OTHER CHANNELS:** This option is a feature that allows you to refill one channel from other existing channels. For instance, if you have 2 different Lightning channels (A and B), and the Bitcoin balance on channel A has depleted, with this option, you can easily and automatically top up the balance of channel A from channel B.

**DIRECT NOT PRIVATE RECEIVE:** This is also an option to generate an invoice to receive payment, but when you use this option, the sender pays you directly. This means that the payment does not hop through different nodes before it reaches you, as a normal Lightning payment does. So, in essence, the sender knows it is you they paid, knows your channel ID, etc. This option can often be used when you are receiving payment from a source you trust and do not need to maintain your privacy.

## Hosted and Fiat Channels

Like many other Bitcoin wallets, Valet is a simple, lightweight Bitcoin and Lightning wallet. But it has a unique Lightning feature that differentiates it from most other Bitcoin wallets. That feature is called **Hosted and Fiat Channels**.

Fiat channels are a type of Lightning implementation that enables easy onboarding and usage of the Lightning network. It is a custodial solution that allows full anonymity, just like with a normal Lightning channel. Fiat channels technology also enables the creation of Bitcoin derivatives on the Lightning network. An example is that with Fiat channels, merchants can accept stable-value Bitcoin payments without worrying about Bitcoin's volatility.

The current implementation of Fiat channels on Valet enables the creation of stable synthetic Fiat currencies backed by Sats. It uses a Host-Client relationship where the Host is any Lightning node offering this service, and the client is the Valet user. It is a custodial solution because all the Sats are on the Host's side; however, invoice generation, tor routing, and preimage generation still happen on the client side as in a normal Lightning channel.

Opening a Fiat channel takes the same process as opening a Lightning channel. The only significant difference is that in this case, the client (Valet user) does not have to commit any liquidity on-chain to create channel capacity. The Host sets the channel capacity and routes all payments for the client.

👉 To open a Fiat channel, click on the purple **Lightning card** on your wallet home page. Select **Scan Node QR** (At this point, you must have identified a Host you want to open a channel to, and obtained the node's QR. An example of a Host node that you can open a Fiat channel to is the SATM node by Standard Sats.)

**Attention:** It is important to note that anyone can be a Host. All you require is to run a Lightning node with the **Fiat channel plugin** and a **Hedging service**. Fiat channels is an open-source project by *Standard Sats*. Read more about it [here](https://github.com/standardsats/fiat-channels-rfc) and [here](https://standardsats.github.io/).

SATM node QR below:

![SATM_node_QR](assets/en/032.webp)

👉 Once you scan the node QR, click on **Request USD fiat channel** or **Request EUR fiat channels** (This is the fiat denomination your Fiat balances will be quoted in). For now, choose USD, and click **OK**. The channel will be opened automatically, and you can start receiving Sats right away. You see, it's that simple!!!

![choose_fiat_denomination](assets/en/033.webp)

![channel_confirmation_prompt](assets/en/034.webp)

👉 Go to your wallet's home page, you will see a **light-green** card labeled **USD**, that is your **Fiat channel**.

![fiat_channel_card](assets/en/035.webp)

**Attention:** When you receive Sats on a Fiat channel, the fiat value of the Sats you received will be locked in as a stable balance, while the Sats volume floats with the Bitcoin price. This solution was designed mostly for merchants who want to accept Sats for payment but do not want to face the volatility challenges of Bitcoin. This helps them maintain stable value at all times, while still being able to transact on the Lightning network, enjoying the global reach and swift settlement of Bitcoin as a medium of exchange on the Lightning Network.

When your Fiat channel is created, here are the following Value fields you'll see and what each of them means:

![fiat_channel_info](assets/en/036.webp)

- **RANDOM SET OF NUMBERS SEPARATED BY DOTS:** These are the nodes' IP addresses. (IPV4 and IPV6, respectively)
- **SERVER RATE:** This is the Bitcoin market price at which the Host is offering the services to you. This will often be slightly different from the predominant market price, because a Host may add a tiny premium. It is entirely up to a Host to decide this rate; hence, this would also vary from Host to Host.
- **FIAT BALANCE:** This is the locked-in stable fiat value of every sat you receive on this channel. Remember, as explained earlier, whenever you receive Sats on your Fiat channel, the fiat value of the Sats at the time of receipt is immediately locked in as a synthetic stable fiat value in this field. Your **Fiat Balance** value does not fluctuate with the Bitcoin market price. Whenever you want to make payments from this channel, you can only send the Sats equivalent of this Fiat balance. So think of this as a digital fiat currency backed by Sats.
- **CAPACITY:** This is the total volume of Sats that can be sent and received through this channel. (This is also set by the Host. And unlike a normal Lightning channel, this capacity can be adjusted by the Host as the case may be.)
- **CAN SEND:** This is the volume of Sats you can send out at each point based on your fiat balance. This is completely different from what you have in a normal Lightning channel, because this value floats with the Bitcoin price. Hence, what you see here is the Sats worth of your Fiat balance at any time based on the **Server Rate**.
- **CAN RECEIVE:** This is the number of Sats you can receive to this channel at the moment. After you create your channel, this value should be the same as the channel capacity.
- **VALUE IN FLIGHT:** When someone sends some sats to your channel, or when you try to send some sats to someone, and for whatever reason, the transaction is delayed, it's often shown in this field.

Here are important things to note about Fiat channels:

- Unlike a normal Lightning channel, when you open a fiat channel, you can immediately start receiving Sats, but you cannot send. You can only send out Sats when you have received Sats.
- At all times, the asset being sent to and from is Sats. The *Fiat Balance* is just a synthetic IOU representation of a Bitcoin value received at any point in time. So, it is not a token creation or a new cryptocurrency.
- The Fiat channel is mostly useful to merchants/businesses who are skeptical about accepting Bitcoin payments due to volatility concerns. It may also be useful to companies that want to pay their workers' salaries in Bitcoin without bearing the consequences of Bitcoin volatility, which can make their salary capital unstable. It may also be useful to individuals who live in an area with predominant Bitcoin usage, but have fixed living costs.
- Notice that there's no field labeled as **REFUNDABLE**. This is because, technically, you cannot close a Fiat channel. You may only stop using a Fiat channel by draining its balance to your normal Lightning channel.

### Your Fiat Channel Pop-Up Options Explained

When you tap on your Fiat Lightning channel, the following fields will be displayed:

![fiat_channel_pop_up](assets/en/037.webp)

**SHARE HOSTED CHANNEL DETAILS:** This enables you to share your Fiat channel details, such as remote peer ID, local channel ID, date of creation, etc.

**EXPORT CHANNEL STATE:** This enables you to export the state of a channel at any point. This is usually useful in fixing channel errors, and a Host may ask that you share this if there's a need for it.

**DRAIN CHANNEL BALANCE:** As mentioned earlier, you cannot technically close a Fiat channel, but you can drain the balance of your channel into your existing normal Lightning channel. This automatically moves the Sat equivalent of your Fiat balance to your normal Lightning channel.

**RECEIVE TO CHANNEL:** This is the same thing as generating an invoice, but in some cases, a user may have more than one Fiat channel with different Hosts, including normal Lightning channels. So, if a user has multiple channels open, this option ensures that they can receive payment to a specific channel.

**REFILL FROM OTHER CHANNELS:** This option is a feature that allows a user refill one channel from other existing channels. So, with this option, you can refill your Fiat channel from a normal channel or other Fiat channels you have, just the same way you could drain.

**DIRECT NOT PRIVATE RECEIVE:** This is also an option to generate an invoice to receive payment, but when you use this option, the sender pays you directly. This means that the payment does not hop through different nodes before it reaches you. So, in essence, the sender knows it is you they paid, knows your channel ID, etc. This option can often be used when you are receiving payment from a source you trust and do not need to maintain your privacy.

## Valet Settings:

Like every other application, Valet has app settings that you may adjust to your taste. You can access the settings page from the home screen.

👉 On the home screen, click on the **Gear** icon located at the top-right corner of the screen to access the settings. Below are the components in the settings section.

![settings_icon](assets/en/038.webp)

**LOCAL CHANNEL BACKUP IS ENABLED:** If this is otherwise **Disabled,** you should enable it because this is the only way you can recover your normal Lightning channels if you uninstall and reinstall Valet. We'll explain this later. So click on this, and give Valet permission to your **media storage** cos that is where the backup file is saved.

![app_permissions](assets/en/039.webp)

![enable_media_access](assets/en/040.webp)

**WHERE TO STORE LOCAL BACKUP:** As long as you gave Valet permission to your storage, this field will automatically be set to store local backups in your **Downloads** folder. But you can change it by clicking here and selecting any folder of your choice.

**MANAGE CHAIN WALLETS** This is a bit technical, and you do not need to bother about this unless you're experienced enough. The default setting here is just fine.

**ADD HARDWARE WALLET:** You should also not bother about this, unless you have a Hardware wallet you want to connect and monitor. With this setting, you can scan and connect your hardware wallet, such as Trezor or Cold Card, and monitor its activities. This is a watch-only feature, which means you cannot perform transactions on the Hardware wallet from here. You can only observe and monitor the wallet activities, balances, etc.

**SET CUSTOM ELECTRUM NODE:** This is also technical, and unless you're knowledgeable enough, you shouldn't bother about this. The default setting is good enough.

**BITCOIN UNITS:** This is how you want your Bitcoin balance to be displayed. The first option displays your balance in Satoshi terms, e.g., 1,000,000 Sats, while the second option displays it in BTC decimal points. e.g. 0.01BTC

**USE PIN AUTHENTICATION** If you check this box, then you'll have to set up a PIN or fingerprint with which you must input to log in to your wallet, and authenticate transactions.

**USE TOR CONNECTION:** If you check this box, your transactions will be routed over the Tor network. It adds an extra layer of privacy but may result in delayed payment throughput, especially for Lightning payments.

**VIEW BIP39 RECOVERY PHRASE:** This is where you can access your 12-word seed phrase for backup. So if you didn't write it down before, or you can't find where you wrote it down, as long as you still have access to your Wallet, you can copy it from here.

**USAGE STATISTICS:** This shows you a summary of all your transactions and activities since the wallet creation

![usage_stats](assets/en/041.webp)

## Wallet Recovery

Valet is a non-custodial wallet, so if you lose your device or uninstall your wallet app, you will need to do a wallet recovery to get back your Bitcoins and Lightning channels. At the beginning of this tutorial, we mentioned the importance of writing down your **12-word seed phrase** because it is the key to recovering your wallet. There are no customer care representatives who can help you get back into your wallet.

There are two important tools needed for recovering your Valet wallet, depending on whether you had an active Lightning channel or not. For a user who did not have an active normal Lightning channel, all they need is their **12-word seed phrase**, following the simple steps below:

👉 Install a new Valet app, and launch/start the app.

👉 Select **Restore Existing Wallet**

![restore_existing_wallet](assets/en/042.webp)

👉 Select **Recovery phrase only**.

![select_recovery_phrase](assets/en/043.webp)

👉 Input your 12-word recovery phrase and click **OK**.

![input_12_words](assets/en/044.webp)

Your wallet will be recovered. In this case, only your on-chain Bitcoin balance will be restored.

However, if you had an active normal Lightning channel and you recover your wallet with only the recovery phrase, your Lightning channel will be force-closed, and any Bitcoin balance you have on it will automatically be sent to your on-chain balance.

The other way to recover your Valet wallet, especially if you had a normal Lightning channel open before you uninstalled Valet, is to **use the local backup file saved on your device, alongside your 12-word seed phrase**. If you use these two, your Lightning channel state will be restored, hence your Lightning channel will not be force-closed.

Here are the steps:

👉 Install a new Valet app, and launch/start the app.

👉 Select **Restore Existing Wallet**.

👉 Select **Backup + Recovery phrase**.

![select_backup_and_recovery_seed](assets/en/045.webp)

👉 Select the Backup file from your phone's file manager. (It is always stored in your **Downloads** folder by default.)

![local_backup_file_in_download_folder](assets/en/046.webp)

Once the correct backup file is selected, a prompt confirming that a **"Backup file is present"** will be displayed, and it will then ask you to enter your 12-word seed phrase.

![enter_12_words](assets/en/047.webp)

👉 Enter your 12-word recovery phrase and click **OK**. You will be taken to your wallet home page.

👉 Wait for the Bitcoin network synchronization (**SYNC**), and the Lightning node synchronization (**LN Sync**) to complete, and your wallet will be fully restored, including your Lightning channels.

![LN_sync](assets/en/048.webp)

## Conclusion

Valet is an exciting wallet solution, with features that make it suitable for onboarding new users. It also has a Fiat channel, a not-so-new technology that ensures integration of fiat-run businesses on the Bitcoin standard.

Download Valet today, and give it a try!!! 🧡
