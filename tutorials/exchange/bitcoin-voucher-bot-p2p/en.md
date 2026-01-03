---
name: BitcoinVoucherBot P2P
description: How to Buy and Sell Bitcoin P2P with BitcoinVoucherBot
---

![image](assets/cover.webp)


We still hear about BitcoinVoucherBot, a Telegram bot created to purchase Bitcoin without [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) via SEPA bank transfer. Unfortunately, as of November 2025, the BitcoinVoucherBot in its centralized form is no longer available as a service without KYC.


In this guide we will look at how the new implementation works that allows users to buy and sell Bitcoin directly on the new P2P (Peer-To-Peer) marketplace, so no KYC. To counter new restrictions that increasingly threaten digital freedom and privacy, the developers created this extension, giving users the ability to buy and sell Bitcoin with a high degree of anonymity through P2P (Peer-To-Peer). Let's see together how this new exchange method works.


To use the service you will have to make transfers via Lightning Network. So make sure you have a wallet that supports this protocol and allows you to use an "LNURL" or "Lightning Address" to receive and send funds.


Among the supported wallets we can find:



- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial with swap to Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)


Or any wallet that has a "Lightning Address" and generates a Bolt11 invoice. wallets that generate a Bolt12 invoice are not currently supported. For more info see the definition of [Bolt](https://planb.academy/resources/glossary/bolt).


For this tutorial, given its ease of immediate use, we will use Wallet of Satoshi.


**Caution**: Wallet of Satoshi, while popular among beginners, is custodial, with limited control over funds; use it only transiently, transferring immediately to a non-custodial for full sovereignty. As of October 2025, it includes a stable self-custodial mode worldwide on iOS/Android (update the app), with autonomous private keys, switch between modes, custom Lightning addresses, and seed 12-word backup. However, it remains an interim solution until consolidation, preferring wallet non-custodial mature for long-term management.


Very good! Now we can begin our journey, which will guide you step by step in creating your account, managing purchase and sales matches, and using your restricted area.


## Wallet and Enrollment


First, if you don't already have it installed on your smartphone, download Wallet of Satoshi.



- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)


![image](assets/it/01.webp)


If you have never used Wallet of Satoshi and want to understand how it works, I suggest you follow this tutorial so you can activate it properly and back it up safely.


https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Now that your wallet is ready, you can start sending a small amount of sats. Keep in mind that, in order to complete your P2P (Peer-To-Peer) platform enrollment, you will be required to send 1000 sats as a control measure: this is to create a barrier against any phantom match (scam) type attacks, preventing anyone from signing up without any spam filter.


![image](assets/it/02.webp)


We can now open the P2P (Peer-To-Peer) platform to proceed with enrollment. You can log in from desktop PCs or browsers on smartphones, via the Telegram BitcoinVoucherBot or via .onion links to provide an even greater level of privacy.


if you choose to use the Tor .onion link I also recommend "Tor Browser". If you don't know it yet you can learn more about it at this link:


https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Now choose how you want to reach the platform.



- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)


You will be redirected to the main page.


press "Get Starter" to get started right away


![image](assets/it/03.webp)


On the next screen you have to choose a password and enter it (box A), and then repeat it (box B). I recommend that you immediately save this password to a backup medium, which can be on a secure digital device such as "Bitwarden":


https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

or save your password on a paper medium (**warning**: this is not a good solution, it is okay though if intended as a temporary solution).


Check the verification box where you state that you are not a robot (box C). Please note Do not enable RSA encryption unless you know exactly what it is and how it works. You do not need to do anything at this stage. Click on "Generate Avatar" ("Generate Avatar") (box D).


![image](assets/it/04.webp)


Now you have to pay the 1000 sats to complete the enrollment.


1. Starting from the top, first see your randomly generated and extremely important "Avatar ID." Save it carefully, just as I advised you to do with the password.

2. You must then enter your "Lightning Address" in the field below. This will allow you to receive payments if you purchase Bitcoin, or get refunds. If you are using Wallet Of Satoshi you will be able to copy your Address by clicking on receive.

3. Check the verification box where you state that you are not a robot.

4. Make the payment of 1000 sats to get access to your restricted area. If you can't frame it, click on it with your mouse (on PC) or tap on it with your finger (on Browser/Telegram smartphones) to copy the address that you need to paste into Wallet of Satoshi and complete the invoice payment.


![image](assets/it/05.webp)


This is your LNURL Address.


![image](assets/it/06.webp)


Congratulations!!! You have created your Avatar permanently and you can view the summary here. Once again, I recommend that you carefully save both your Avatar and password, as I have suggested before.


Click `I've saved my credentials, continue` (translated as: "I've saved my credentials, continue")


![image](assets/it/07.webp)


You are now in the heart of the platform, where you can view all the trade matches with their details. For a clearer view, below you will see the images inherent in the website from desktop computers.



- "Type" ("Type") defines whether it is a "Sell" ("sell") sale or a "buy" purchase
- "Amount" ("Amount"): indicates how many sats the user is selling if the match is of the "Sell" type, or how many Bitcoin the user is willing to buy if the match is of the "Buy" type.
- "BTC Price with Margin" ("BTC Price with Margin"): shows the price taking into account the margin applied above the marked value.
- "Margin" ("Margin") is the percentage that is applied to the market price, With a minus sign (-) you get a discount on the market price, With a plus sign (+) a premium is applied to the market price.
- "Method" ("Method") indicates by which motodo the user prefers to be paid.
- "Creator" is the unique avatar used by the user on the platform.
- "Rep" (Reputation) The user's reputation level ranges from -5 unreliable to +5 extremely reliable.
- "Status" ("Status"): indicates the status of the match. In the example screenshot, all matches appear to be "Open" ("Open").
- "Expiration" ("Expiration"): shows how much time is left before the match expires and is cancelled if it was not chosen by anyone.


![image](assets/it/08.webp)


At the top right click on your Avatar to access your profile.


![image](assets/it/09.webp)


Here you can see your Avatar name, User ID, creation date, and reputation, which will reflect positively or negatively on your behavior in negotiations.


![image](assets/it/10.webp)


In the Settings section you can view your "Lightning Address," entered during registration, and change it if necessary. You also have the option of creating a Public Key, which as mentioned should be set up only if you have the appropriate skills. It is used to encrypt the messages you will exchange with your counterpart directly from your computer.


The Telegram Notification feature is highly recommended. By activating it, a QR code will appear for you to frame with the Telegram app: this way you will receive real-time notifications about all actions related to your matches, directly in the bot chat on Telegram.


![image](assets/it/11.webp)


Finally, you find your referral section, with the earnings generated by the users you have invited. From here you can use the button to share your link or QR code and, a little further down, view a list of matches to track your reputation along with the corresponding score.


![image](assets/it/12.webp)


## Create an order to Purchase Bitcoin


Enter the Marketplace: from the main navigation bar, click on the cart symbol "Marketplace"("Marketplace") to open the order book. then start a new order: press the "New Order" button ("New Order") to start the process.


![image](assets/it/13.webp)



- Set order details:
- Select the option "Buy Bitcoin"("Buy Bitcoin").
- Enter the amount of sats you want.
- Define the price margin (between -20% and +20% from market value).
- Choose the payment method (Instant SEPA, etc.).
- Indicates preferred currency.
- Confirm Order: click on "Create Order"("Confirm Order") to proceed to the filing stage.


![image](assets/it/14.webp)


Deposit required: a deposit equal to 10% of the total amount, plus a service fee, is required to activate the order.


- Deposit payment: when the order is created, the system automatically generates a Lightning invoice. The deposit is only temporary and is refunded when the order is completed.
- Main features:
- Security deposit: 10% of order value.
- Service fee: cost for using the platform.
- Time limit: You have 5 minutes to make the payment, otherwise the transaction expires.


![image](assets/it/15.webp)


After successful payment, the order will appear in the book and be visible to all users, who can choose and accept it. To create a sell order all you need to do is click on "Sell Bitcoin" ("Sell Bitcoin"), enter the quantity of satoshi you wish to sell, set the margin, select the payment method and currency, then proceed with the 10% deposit as a security deposit. Once completed, your match will be visible in the list.


![image](assets/it/16.webp)


## How to accept an order


1. Sellers can see a list of all available orders in the book.

2. Check the details: each order shows information such as:


  - Quantity of Bitcoin,
  - Margin on price,
  - Payment method,
  - User reputation.


![image](assets/it/17.webp)


3. Click on the order to open the full sheet with all the information.

4. Press on "Sell Bitcoin"("Sell Bitcoin") to accept the proposal.


![image](assets/it/18.webp)


## Deposit required by seller


When the order is accepted, the system generates an invoice for payment. The deposit includes:

- The total amount of the order,

- the service commission.


Deposit payment must be made within the stipulated time limit, otherwise the transaction will not be confirmed.


![image](assets/it/19.webp)


## Sending payment instructions


After the deposit is made, the transaction will appear in the seller's personal dashboard, who must provide the details to the buyer to complete the payment in fiat currency.


1. The seller displays the active transaction in their panel.

2. Click on "Submit Payment Instructions."

3. Enter all necessary information for the fiat payment (IBAN, recipient, address, reason for payment, etc.).

4. Click on "Send Message"("Send Message") to transmit the data to the buyer.


![image](assets/it/20.webp)


## Payment procedure


The buyer receives, within the platform chat, a message with all the necessary data to make the payment in fiat currency:


- Bank details: IBAN with name and address of the seller's account holder.
- Exact amount: exact fiat amount to be transferred.
- Causal/description: text to be included in the transaction.
- Time limit: deadline by which to complete the payment.


The transfer takes place outside the P2P system and must be made through one's banking institution.


⚠️ **Important note:** confirmation on platform should be made only after you have actually arranged the transfer or fiat payment through your bank.


![image](assets/it/21.webp)


## Confirmation of payment fiat


This step is crucial for the buyer and should be performed only after verifying that payment has actually been sent.


1. Receiving data: the buyer has received payment instructions from the seller.

2. Payment execution: fiat transfer is arranged from one's bank account.

3. Verification: check that the operation was processed correctly.

4. Confirm on platform: click on "Confirm fiat payment"("Confirm fiat payment") on the trade page.

The "Confirm Payment fiat" button appears in the transaction section and should only be used after verifying that payment has indeed been sent.


![image](assets/it/22.webp)


The last step in the process is for the seller to confirm receipt of the fiat payment, following which the satss are released to the buyer.


![image](assets/it/23.webp)


## Conclusion


In the hope that this tutorial will help you to use a new method to trade Bitcoins or even just buy them, either for your own store of value or to start bringing daily payments to life. Still, it remains a door to explore to cope with what is about to happen in our digital world.


The noose run by the bodies that control us is tightening, to give birth to an increasingly controlled Internet. By buying P2P, you will keep your purchases in total anonymity, leaving no trace and no follow up repercussions from third parties.