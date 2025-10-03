---
name: Zeus Embedded
description: How to use the Lightning Zeus Embedded wallet
---
![cover-zeus-embedded](assets/cover.webp)


ZEUS is initially a mobile application for remote management of lightning nodes, allowing you to control your node installed on a remote server

But the application also features an "Embedded node".


**It's this facet of the application that we'll be exploring in this tutorial.** This allows anyone to have their own lightning node on mobile, without the need for a dedicated server, in the same way as ACINQ offers its incredible Wallet lightning Phoenix.


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*As a reminder, Lightning is a network that operates in parallel with Bitcoin, enabling bitcoins to be exchanged without having to systematically carry out On-Chain transactions. The result is near-instantaneous transactions, with no need to wait 10 minutes for a block to be validated. This is particularly useful when paying a merchant in the physical world. What's more, Lightning provides a remarkable level of **confidentiality** that the Bitcoin network does not possess natively*.


**Zeus "Integrated "** is aimed at Bitcoiners who want to maximize their privacy and autonomy.

In short, it's **potentially** the Wallet mobile of cypherpunks' dreams. Even if it's still in its infancy (alpha version) and subject to a few bugs, its features are legion, and there's no doubt that it will delight the most intrepid among us, who want maximum control and optionality.


On the other hand, I don't think it's currently suitable for beginners who are unfamiliar with Bitcoin and simply want a simple way of sending/receiving satoshis. Although this may change in the future, as a custody feature via the Cashu (chaumian Ecash) protocol is being implemented for beginners...


## Install the application


Go to [the project website](https://zeusln.com/) to download the application for your smartphone's OS:


![image](assets/fr/01.webp)


![image](assets/fr/02.webp)


## Portfolio creation


Once the application has started, click on the "Quick Start" button to begin creating the Wallet.


![image](assets/fr/03.webp)




A series of initialization screens then appear. Wait a few moments, then wait a few minutes until the node is 100% synchronized via Neutrino.


This may take a few minutes. For information neutrino is a way for mobile wallets to access Blockchain Bitcoin information, without needing to run a full node.


![image](assets/fr/04.webp)




After a few moments, you're ready to go.


![image](assets/fr/05.webp)



## Application setup


Ready, well not quite, because it goes without saying that a Zeus user worthy of the name navigates his Wallet with class and style. So we're going to have to change his avatar.


Click on your avatar in the top right-hand corner of the screen:


![image](assets/fr/06.webp)




Click on the cogwheel, then on the plus "+" :


![image](assets/fr/07.webp)




Select the most beautiful photo of Zeus to represent this Wallet and click on "CHOOSE PICTURE" at the bottom of the screen, then go back by clicking on the arrow at top right.


![image](assets/fr/08.webp)




Finally, give your Wallet a nickname and click on "SAVE Wallet CONFIG" for the change to take effect. Finally, click on the back arrow in the top left-hand corner to return to the home screen.


![image](assets/fr/09.webp)




This time we can really get started.


![image](assets/fr/10.webp)


### Biometrics


To protect access to your Wallet, you can add a PIN/password and activate biometrics.


To do this, go to the Wallet main menu by clicking on the horizontal dashes at top left.


![image](assets/fr/11.webp)




Select "Settings", then "Security" and finally "Set/Change PIN".


![image](assets/fr/12.webp)




Create your PIN, confirm it, and activate biometrics by pressing the corresponding "Biometrics" button.  Return to the main menu, using the arrow at top left.


![image](assets/fr/13.webp)



### Save mnemonic phrase


Once you're back in the main menu, click on "Back up Wallet", then read the warning text which informs you that losing the 24 words you're about to receive is tantamount to losing access to your funds, and that anyone who has these words in addition to you can access your funds. Never give them to anyone.


Select "I UNDERSTAND" at the bottom of the screen. Then click on each of the 24 words to bring them up, and note them carefully.


You can write it on paper, or perhaps, for added security, engrave it on stainless steel to protect it from fire, flood or collapse. The choice of medium for your mnemonic will depend on your security strategy, but if you're using Zeus as an expense wallet containing moderate amounts, paper should be sufficient.


For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)


Once finished, click on "I'VE BACKUP MY 24 WORDS" at the bottom of the screen, and we're back on the home screen, ready to receive our first bitcoins.



## Option 1 - Receive On-Chain bitcoins & open a Lightning channel


**Zeus Embedded** is primarily designed as an embedded lightning node, but it can also be used as a Wallet On-Chain.


To receive On-Chain bitcoins, click on the "On-Chain" button and then on "Receive".

Finally, scan the QR code or copy the Bitcoin address to deposit funds.


![image](assets/fr/15.webp)




Once the funds have been confirmed and credited to your Wallet, you can use them to open a **Lightning channel**. Your Lightning channel is your gateway to the Lightning network, enabling you to exchange bitcoins in a much more confidential and rapid way.



- To do so, click on "MOVE On-Chain FUNDS TO LIGHTNING"


On the next screen, you are asked to open a channel in collaboration with **"Olympus by Zeus "**, the LSP (Lightning Service Provider) favored by Wallet.

For this tutorial, we'll choose this option for simplicity's sake, but it's perfectly possible to open channels with any node on the network.

It is even possible to open several channels in a single transaction by selecting "OPEN ADDITIONAL CHANNEL". *But we'll look into this in an "advanced" version of the **Zeus Embedded** tutorial.*



- Then select the amount you wish to dedicate to this channel. In our case, all our On-Chain funds will be used, so we activate the "Use all possible funds" button.



- Finally, select the "OPEN CHANNEL" button at the bottom of the screen.


![image](assets/fr/16.webp)




Within seconds, the channel is established and we're ready to make our first Lightning transactions. On the home screen, we can see a small clock next to our wallet balance. This is because we'll still need to wait for 3 On-Chain confirmations before the channel is truly functional.


![image](assets/fr/17.webp)




After the 3 confirmations, we notice that our balance is now credited to the Lightning insert.


![image](assets/fr/18.webp)


A small point of detail: when we click on the menu at the bottom of the screen to view the status of our lightning channels, we see that a small part of our balance is not available for spending: we can only spend 208253 satoshis instead of the 210370 we actually have. This is normal, as it's specific to the lightning protocol.


Finally, it should be noted that our partner Olympus reserves the right to close the channel at its own discretion, if it is not being used, for example. To ensure that our channel is maintained, we'll have to pay the LSP (Lightning Service Provider), as we'll see in the next paragraph, through the 2nd way of opening a channel.




## Send bitcoins via Lightning


Now that we've got our channel up and running, let's see how we can use it to pay a Invoice (invoice) lightning.


To do this, click on the "Lightning" button, then on "Send".


![image](assets/fr/19.webp)




On the next screen, copy your Invoice into the dedicated field, or scan it by clicking on the icon at top right. Finally, slide the "Slide to Pay" button to the right to pay.


![image](assets/fr/20.webp)





Wait a few seconds and the Invoice is paid off, and your satoshis have traveled at the speed of light.


![image](assets/fr/21.webp)




Zeus then lets you add a note to denominate your payment, or view the route your satoshis took before reaching their destination (and the charges levied by all intermediate nodes). This is the kind of functionality we love about Wallet.


![image](assets/fr/22.webp)


Note that unlike a Wallet like [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), with Zeus the route is calculated locally and not delegated to a third party (ACINQ in the case of Phoenix). So you're the only one who knows the recipient of the payment. We lose a little efficiency (payments take a little longer to complete, but we gain a lot in terms of privacy).




By clicking on the little arrow at the bottom of the home screen, you can also view our payment history. Here we see in green the 212,121 Sats received for On-Chain, then in red respectively the 211,756 Sats used to open our channel, then the 121,212 satoshis used to pay for our Invoice lightning.


![image](assets/fr/23.webp)




## Option 2 - Receive bitcoins directly on Lightning


Rather than opening a channel manually, as we have just seen, it is possible to receive funds directly via Lightning, even without a pre-existing channel, using Olympus, the Zeus LSP.


- To do this, click on the "Lightning" button on the home screen, then on "Receive".
- Then choose the amount you wish to receive in the "Amount" box and select the "CREATE Invoice" button at the bottom of the screen.


![image](assets/fr/24.webp)




The next screen shows the Invoice to be paid to receive the satoshis. We are told that the LSP will withhold 10,000 Sats if payment is made by Lightning. We'll see later how these channel opening fees are justified.


Pay the Invoice or have someone else pay it, and the channel will be opened automatically, but deducting the 10,000 Sats as agreed.


![image](assets/fr/25.webp)




We are now at the head of 2 lightning channels, whose status can be checked by clicking on the button indicated by the white arrow at the bottom of the home screen.


We can see that, unlike the channel opened from our On-Chain scale, the one opened directly via lightning displays no warning.

As you've paid to set up this channel, the Lightning Service Provider (LSP) undertakes to maintain the channel for 3 months, and offers you "incoming liquidity". On the bottom channel, you can see that reception capacity is 96383 satoshis. The LSP has therefore tied up capital to enable you to receive payments directly after opening the channel.


So the 10,000 Satoshi in fees paid cover: the cost of opening the canal (Bitcoin On-Chain transaction, the guarantee to maintain the canal for 3 months, and the capital lock-up).


![image](assets/fr/26.webp)




Congratulations, you're now ready to use Zeus Embedded, the Wallet mobile lighting system with the most advanced features on the market.




To find out more about the technical operation of Lightning Network, you can find Fanis Michalakis' excellent free Plan ₿ Network training:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb