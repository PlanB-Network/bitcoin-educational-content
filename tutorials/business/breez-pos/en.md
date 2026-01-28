---
name: Breez - POS
description: Breez makes it easy to collect bitcoin payments for your business.
---

![cover](assets/cover.webp)


Since the COVID-19 pandemic, contactless digital payments have become widespread, even in the smallest shops. During this period, many businesses have discovered the practicality of bitcoin cash solutions, enabling them to receive payments from all over the world. However, these solutions are sometimes difficult to use or unsuitable for small businesses. In this tutorial, we'll be taking a look at the Breez payment terminal, a solution that stands out for its ease of use, while giving you total control over the management of your bitcoins.


## Install Breez POS


Breez POS is a self-custody service provided by the Breez wallet. The utility of this service is to enable merchants to collect payments via Bitcoin while remaining on a simple interface, very similar to the various Lightning wallets. Breez POS is available on the [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) and [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS) download platforms.


![download](assets/fr/01.webp)


![setup](assets/fr/12.webp)


⚠️ It is important to note that these applications are still under development and that there may be some errors in the use of the functionalities. We recommend moderate use.


With this application, Breez gives you complete control over network configurations and fee settings, while guaranteeing your sovereignty in managing your bitcoins.


You can explore the various Breez wallet options by following our tutorial below. This step will help you better understand the point-of-sale ecosystem and adopt best practices to effectively secure the bitcoins associated with your seed.


https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Using Breez POS


In this tutorial, we'll focus on the "*Point-of-Sale*" section to help you understand how to integrate it as a means of payment in your business.


The point of sale is an integral part of the Breez portfolio and relies primarily on the Lightning Network to collect payments.


In the "*Point of Sale*" menu, you have a direct interface for collecting payments. It is divided into two parts:


### Direct debit


The first part is the direct debit keyboard. This interface is handy for collecting a payment in full when you know your customer's total purchases, or when you don't need a fixed product catalog in your business (e.g. freelance services).


![keyboard](assets/fr/02.webp)


To use the Breez POS for the first time, you'll need to collect a payment of over 2,500 satoshis (around 3 euros at today's exchange rate). This amount, paid only on your first cash-out, represents the cost of creating a payment channel so that you can communicate with other Lightning Network nodes and send and receive satoshis.


![channel_fee](assets/fr/03.webp)

### Product catalog


The second part is the product catalog. This interface is ideal when you have a product catalog with pre-defined prices. Here you can pre-configure your products and then use them to generate invoices to improve the traceability of your cash receipts.


![items](assets/fr/04.webp)


You can manually configure each item from this interface by clicking on the "**Plus**" button and then defining the name, price and an identifier for this item.


![add_items](assets/fr/05.webp)


You can then add it and define its quantity to collect the associated payment.


When your catalog is quite large, it can become complicated to add your products one by one. For this purpose, in the **Preferences > Point of Sale Settings** section, from the "Item list" menu, you can automatically import and export your item list from CSV files.


![import](assets/fr/07.webp)


In this same section, you can define the validity period of your Lightning invoices. From now on, for all your invoices, your customers have `N` seconds to make their payment, failing which you'll have to regenerate a new Lightning invoice.


![invoice_time](assets/fr/08.webp)


As a manager, you can strengthen the security of your bitcoins by adding a password that will be required for all outgoing payments from your wallet. This feature is particularly useful when you're not the only one managing your outlet.


![manager](assets/fr/09.webp)


In the **Transactions** menu, you'll find a list of all the payments you've collected. You can also filter the results over a specific period by clicking on the **Calendar** button.


![transactions](assets/fr/10.webp)


You can also view a daily summary of your sales and the total amount collected by clicking on the **Document** button.


![summary](assets/fr/11.webp)


You now have a complete grasp of the point-of-sale offered by the Breez application for seamless integration of Bitcoin into your business. If you found this tutorial useful, we recommend our tutorial on be-BOP, an e-commerce platform that lets you take payments in bitcoins and monetize your business.


https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa