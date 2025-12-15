---
name: StashPay
description: The minimalist Bitcoin wallet for everyone
---

![cover](assets/cover.webp)


User experience is a key factor in the adoption of Bitcoin solutions around the globe. Providing a smooth, simple and technically unencumbered experience is the priority for many wallets and exchange platforms. In this respect, StashPay stands out for its minimalist approach, while at the same time demonstrating the power of Lightning Network.


In this tutorial, we'll take a look at this wallet to find out how it works and how it's ideal for small businesses or solopreneurs.


## Getting started with StashPay


StashPay is a Lightning self-custodial wallet recognized primarily for its minimalist, user-centric user experience.  With this wallet, you don't need any technical knowledge to receive and send your first satoshis.


StashPay is an open-source project developed in React Native and aims to solve the problem of high transaction fees even with transactions on the Bitcoin protocol's main chain. It is available as a mobile app on Android and iOS platforms via download links present on the [website](https://stashpay.me/).


![introduce](assets/fr/01.webp)


It is important to download the Android application from the website, as it is not available on Google Play Store.

When the download is complete, please grant the necessary permissions so that you can install the application on your Android phone.


Once the application has been installed, StashPay will create an initial Bitcoin wallet for you the first time you open it. Before any transaction, we recommend that you make a backup of this wallet. Below, you'll find all our guidelines for ensuring that your recovery phrases are properly backed up.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Access StashPay settings by clicking on the "Settings" icon, then click on the **Create backup** option. Then authorize the display of recovery phrases. Do not copy your recovery phrases to your phone's clipboard, as they may be accessible to other fraudulent applications installed on your mobile.


![backup](assets/fr/02.webp)


You can also retrieve a Bitcoin wallet you're already using by clicking on the **Recover wallet** option and inserting your 12 or 24 recovery words.


### Receive your first satoshis on StashPay


On the home screen, click on the **Receive** button and set an amount greater than the amount specified in red. In our case, we can't receive less than 0.11 USD with the StashPay wallet.


![receive](assets/fr/03.webp)


Once you've defined the amount, you can click on the **Create invoice** button, then scan or copy the invoice to send it to your satoshis sender.


![receive_sats](assets/fr/04.webp)


You can view your transaction history by clicking on the "clock" icon on the home page.


![network_fee](assets/fr/05.webp)


You will have noticed that to receive satoshis you will have to pay a network fee. These fees will be deducted from the satoshis you are about to receive. This is because StashPay is a wallet based on the Breez Development Kit. To receive satoshis with the Lightning node-free implementation of the Kit, Breez will charge the customer (StashPay in our case) `0.25% + 40 satoshis`. Find out more in our Misty Breez tutorial.


https://planb.academy/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Send bitcoins with StashPay


Sending bitcoins with StashPay is fairly intuitive thanks to the minimalist Interface. On the home screen, click on the **Send** button. Scan the QR code or paste the address to which you wish to send satoshis. StashPay will automatically detect the Bitcoin protocol chain to which you wish to send bitcoins.


![send](assets/fr/06.webp)


As StashPay is a wallet based on the Breez Development Kit, it benefits from an interesting advantage: sending bitcoins on the main chain at low cost. Breez uses the Boltz service to carry out transactions between the different chains of the Bitcoin protocol, enabling customers who implement the Development Kit to benefit from this service directly in their application.


https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

However, Breez SDK imposes a minimum amount at which you can send bitcoins to an address on the main chain.


![onchain](assets/fr/07.webp)


You can also send bitcoins using your recipient's Lightning address. Review your transaction details, then confirm by clicking on the **Send** button.


![confirm](assets/fr/08.webp)


## More configurations


In the StashPay settings, you can adjust configurations to personalize your use of the wallet.


StashPay lets you exchange satoshis based on the local currency of your choice. Click on the **Currencies** option, then search for your currency in the list of +113 currencies offered by StashPay.


![currencies](assets/fr/09.webp)


In the **Receive options** menu, you'll find all the settings for receiving bitcoins with StashPay. For example, by selecting **Choose Lightning or Onchain**, enable your wallet to receive bitcoins from the main chain.


![receive-onchain](assets/fr/10.webp)


The **Scan OnChain addresses** option lets you refresh your wallet's balance by checking all the UTXOs (bitcoins you haven't spent yet) linked to your various addresses.


![rescan](assets/fr/11.webp)


The **Export log** menu lists all Breez and Boltz infrastructure actions concerning your transactions and atomic exchanges between the various Bitcoin protocol chains.


![export](assets/fr/12.webp)


You've just got to grips with StashPay's minimalist Bitcoin wallet. If you've found this tutorial useful, we recommend our tutorial on how to get started with Bitcoin and earn your first bitcoins.


https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f