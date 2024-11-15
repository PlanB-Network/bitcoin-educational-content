---
name: Peer-to-Peer Bitcoin Buying and Selling Solution
goal: Explore non-KYC Bitcoin buying and selling solutions
objectives:
  - Understand the different types of KYC, their risks, and benefits
  - Understand the advantages of peer-to-peer buying
  - Implement the solution that fits your needs
  - Improve the management of your UTXOs (KYC and non-KYC)
---

# A Journey into the World of Non-KYC

Pierre offers us this course that dives into the different existing solutions for buying and selling bitcoins peer-to-peer. Peer-to-peer buying is completely legal and allows for greater anonymity, indeed these solutions are not KYC. KYC (Know Your Customer) is a market regulator rule (AMF) that involves asking for identification from customers wishing to buy or sell bitcoin. These rules aim to prevent money laundering, terrorism financing, and tax evasion. Despite the significant consequences for the user, KYC aims to defend and protect its user, although it's often observed to have the opposite effect.

We will therefore explore the different types of KYC (the full KYC type like in France, the KYC Light type like in Switzerland, and the non-KYC type like peer-to-peer). Pierre will present more than 6 solutions, so you will have all the information needed to discover which one suits you. If you are looking for a KYC solution, note that they are included in the BTC 102 course.

+++

# Introduction
<partId>9aa6ddfd-a257-549f-bb23-f77f1ca5d330</partId>

## Explanation & Type of KYC
<chapterId>13d18e82-0c50-5a7f-97d8-39cf5b4ef085</chapterId>

### Introduction

![introduction by Rogzy](https://youtu.be/3AHeKLTK7Sg)

### Explanation

![explanation of KYC types](https://youtu.be/kDhXoPU1KtM)

KYC, for "Know Your Customer," is a regulatory standard that requires the collection of private information from clients, such as their physical address, identification, or bank statements. This practice is common on brokerage platforms, which may request a complete KYC, including detailed information like an ID, a photo, proof of residence, pay slips, etc.
The primary goal of KYC (Know Your Customer) is to combat money laundering, terrorism financing, and tax evasion. It is a law implemented by the AMF (Autorité des marchés financiers), the regulatory body of the French market. However, the application of KYC leads to the centralization of highly sensitive databases containing users' personal information. This information, having a certain value, can be sold to malicious entities.
Furthermore, exchange platforms often request an excessive amount of personal information, thus putting users at risk and increasing compliance costs. These regulatory costs can discourage French businesses and harm their competitiveness internationally.

There are three types of KYC, including full KYC, which requires a complete and regulated collection of information to access the service. In Switzerland, an alternative called "KYC light" allows the buying and selling of bitcoins without providing an ID, as long as the purchase amount does not exceed 1000 euros per day. Solutions like Relay enable the use of this method.
In this context, Swiss authorities can access banking information to investigate individuals considered at risk. The delivery addresses of bitcoins are also traceable through the banking system. KYC light is generally considered simpler and less costly than the French system.
In France, buying bitcoins online requires sending money to a third party, via SEPA transfer or Paypal. For those who prioritize anonymity, security, and privacy, solutions for buying bitcoins in cash are also available. For small volumes, buying bitcoins in cash is a simple and legal option.

To be able to sell daily PLT of 100 euros of bitcoin to everyone, regulation by the AMF (Autorité des Marchés Financiers) is necessary. In France, this regulation mainly applies to individuals who carry out significant volumes of transactions. The two other methods of buying bitcoin include the use of ATMs and exchanges among friends. ATMs are regulated and require an ID for transactions over 500 euros. Exchange among friends, on the other hand, offers a more discreet exposure to bitcoin.

These regulatory measures are in place to counter terrorism financing, tax evasion, and money laundering. Bitcoin, as a fully traceable database, makes money laundering particularly difficult. The use of Bitcoin by criminals can be traced, making Bitcoin an ineffective tool for money laundering.
It's important to note that this training presents various alternatives, as well as tools that can be used for either malicious or non-malicious purposes. Additionally, it offers explanations on how order books work between makers (order providers) and takers (order receivers).

It is also important to note that the information presented here does not endorse any particular solution. It is simply to present the available options for a better understanding of the subject. For any further questions about Bitcoin, feel free to consult online resources such as www.discoverbitcoin.com.

## Comparison of Peer-to-Peer Buying and Selling Solutions
<chapterId>aad2dccb-0d2c-5533-859b-372b0f10d1ca</chapterId>

![comparison of p2p buying and selling solutions](https://youtu.be/HiwSjN04Mz0)

P2P Solutions for Buying Bitcoin: Bisq, RoboSat, LNP2PBot, Peach, and HodlHodl

Buying Bitcoin on a peer-to-peer (P2P) basis is a preferred option for investors wishing to avoid centralized exchange platforms. This part of the course examines different P2P solutions available, including Bisq, RoboSat, LNP2PBot, Peach, and HodlHodl.
Comparison of the Advantages and Disadvantages of Different Solutions

Each P2P solution has its own advantages and disadvantages. Below is an overview of the key features of each solution.

### Bisq

[Bisq](https://bisq.network/) is a non-custodial P2P solution that features a DAO (Decentralized Autonomous Organization) system and uses multisig for dispute resolution. Its code is open source, which contributes to its robustness and the protection of user privacy.

| Advantages                                     | Disadvantages                                                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| - P2P, non-custodial, multisig, DAO solution | - The application is quite heavy and not very user-friendly, available only on computers                           |
| - Robust and secure                        | - The limitations on buying and selling as well as account management with signatures have a double-edged aspect. |
| - Open source                                 |                                                                                                                     |

### RoboSat

[RoboSat](https://learn.robosats.com/) is an easy-to-use, fast solution operating under TOR and does not require an account. It is open source and uses the Lightning Network for fast transactions.

| Advantages                                                    | Disadvantages                                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| - Easy to use                                          | - The protocol is fragile with only one coordinator                           |
| - Low transaction fees                               | - Requires technical knowledge and an understanding of privacy |
| - Uses the Lightning Network for fast transactions | - The Umbrell application allows managing your own client instance           |
### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) is accessible via Telegram for non-KYC Bitcoin purchases. It offers fast transactions through the Lightning Network and low fees.

| Advantages                                                          | Disadvantages                                                         |
| ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| - Accessible via Telegram                                          | - Less robust and secure than other solutions                        |
| - Speed through the Lightning Network                              | - Slower and less user-friendly than Robosat                         |
| - Low transaction fees                                             | - Can be linked to the user's Telegram identity                      |
| - Internal dispute resolution                                      | - Lack of liquidity and fragility of the application                 |
| - Offers communities to mitigate trust issues                      | - Trust must be placed in LNP2Pbot for dispute resolution            |

### Peach

[Peach](https://peachbitcoin.com/) is a mobile application dedicated to Bitcoin trading. It stands out for its simplicity, not requiring an account to operate. Trades are fast, even without the Lightning Network. Additionally, phone notifications speed up the transaction process.

| Advantages                                                          | Disadvantages                                                                                                                  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| - Simplified use: no account creation is necessary.                | - Security and robustness: being linked to a company, Peach has potential weaknesses in terms of security.                     |
| - Transaction speed: exchanges are fast.                           | - Absence of Lightning Network: this technology, which allows for faster Bitcoin transactions, is not used by Peach.           |
| - Notifications: they speed up the transaction process.            |                                                                                                                                |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) is a non-custodial solution for Bitcoin exchange. It offers numerous advantages such as high liquidity, the possibility of private trades, a referral system, as well as accounts with trade history and a rating system. However, trades are linked to the user's email address and digital identity, stored at HodlHodl. Moreover, the source code of HodlHodl is not open to the public, and the application cannot be used with Tor.

| Advantages                                                                                                                     | Disadvantages                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| - Non-custodial: the user remains in possession of their private keys.                                                        | - Storage of personal information: the user's email address and digital identity are stored by HodlHodl.                        |
| - Liquidity: HodlHodl offers a wide range of exchange possibilities.                                                          | - Closed source code: the code of HodlHodl is not open to the public.                                                           |
| - Private trade options: the user can choose who to trade with. | - Incompatibility with Tor: HodlHodl cannot be used with this privacy-focused network. |
| - Referral system: HodlHodl rewards word-of-mouth. | - Possibility of forced KYC: in certain situations, HodlHodl may require identification information to retrieve funds. |
| - Trade history and rating system: these features allow assessing the reliability of other users. | |

## Conclusion on P2P Solutions
<chapterId>c904985a-78dd-593e-a9c4-bfd1208d10c3</chapterId>

In summary, each P2P solution has its advantages and disadvantages. Bisq is considered the most robust and secure, but less accessible. RoboSat is open source but less robust than Bisq. LNP2PBot is less robust and secure than the other solutions, slower, and less user-friendly than RoboSat, but more so than Bisq. Peach is the easiest and fastest app for buying Bitcoin non-KYC, but it is backed by a company, hence weaknesses in terms of security and robustness. HodlHodl is a protocol managed by a company and is closed source, therefore it has weaknesses in terms of security and robustness, and is slightly more complicated than Peach.

The good old cash face-to-face remains always a solution, for small amounts.
Besides P2P solutions, there are other cryptocurrency exchange options. kycnot.me offers services such as VPN, VPS, SMS, etc. Bitrefil allows buying gift cards. Each solution on [kycnotme](https://kycnot.me/) is presented with its pros and cons.

# Tutorials on P2P buying/selling solutions
<partId>582cee39-f6d0-5fb8-906f-b3e4c9f36fa5</partId>

## Robosats
<chapterId>1f1bd705-fcb3-5e32-8aa7-9ba184488326</chapterId>

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) is an open-source project developed by Reckless Satoshi to privately exchange Bitcoins for national currencies. It simplifies the peer-to-peer experience and uses Lightning invoices to minimize the need for custody and trust. To use it, we will need Tor, an anonymous communication network.

The first thing you need to do is download Tor. You can find it on GitHub or directly on the official website at the following address: tor.org/download.
Once Tor is downloaded and installed:
- Press "Connect" to establish the connection.
- Go to the [Robosats onion address](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Copy the token to save your identity.

Here are the steps for buying bitcoins with Robosats:

- Check the order book, you can filter by currency and payment method - for example, buy bitcoin in euros with Revolut.
- Before buying, check the offer's expiration, the price in euros, and the premium (you can also filter offers by premium).
- Preferably, choose an offer with an active user and a premium lower than average.
- Verify the order summary with the amount, payment method, premium, order ID, and expiration.
- You can receive your satoshis on a bitcoin address with swap-out fees (from LN to BTC-onchain) of about 1% (you can modify the on-chain mining fees).
- Alternatively, create an invoice with an LN wallet from this [list](https://learn.robosats.com/docs/wallets/) and copy the invoice on Robosats.
- Contact the seller via encrypted chat to discuss fiat payment.

Now let's look at the steps for selling bitcoins on Robosats:

- Customize your offer by choosing the payment method, premium, expiration duration, etc.
- Fidelity Bond Size is equivalent to the security deposit on BISQ. Put 15% or 10% security deposits to encourage fair play by the other party.
- Lock the satoshis to confirm the creation of the order and avoid spam.
- If someone accepts your sale offer, discuss with the peer to proceed with the fiat payment. Once the payment is made, the trade is completed, and the sold satoshis are yours!

## BISQ: A peer-to-peer buying solution
<chapterId>28b010ce-0e9b-5f20-a622-fa64629b2d88</chapterId>

[Bisq](https://bisq.network/) is a decentralized exchange platform for digital assets, primarily Bitcoin. It allows for direct, secure, and private transactions between users worldwide without the need for an intermediary.

🚨 Please exercise caution when using Bisq, as it is an advanced solution. It may not be suitable for beginner users. Make sure you have some experience and understanding before getting started. 🚨

We will look in detail at this solution, here are the tutorial videos:
For those more adept, here is a concise guide quickly outlining the essential steps:

1. Download and Install: Visit the Bisq website and download the application. Install it on your system.
2. Set Up Payment Method: Open the application and go to "Account". Add your payment method details.
3. Fund Your Bisq Wallet: Click on "Funds" and then "Receive Funds" to get your Bisq address. Send Bitcoins to this address.
4. Make a Transaction: Click on "Buy/Sell" and choose the desired transaction. Follow the instructions to complete the transaction.
5. Confirm Receipt: Once you have received the payment, confirm it in the Bisq application. This releases the Bitcoin from escrow.

Remember to always check all the details of your transactions and only deal with trusted parties.

Here is now a complete guide that will walk you through all the steps to use Bisq.

BISQ is a decentralized and secure network that respects your privacy. Indeed, it is non-custodial, meaning you always own your funds. Moreover, BISQ uses a token, the BSQ, which allows you to pay lower transaction fees and encourages your participation in the DAO (Decentralized Autonomous Organization). To protect sellers in Bitcoin-fiat transactions, BISQ has implemented a system of signatures and account limits. As a buyer, you will need to obtain a signed account to increase your buying limit. The signature is also a way to verify the trading history of traders, thus ensuring the security of transactions.

To install Bisq and back up your data, follow these simple steps:

- Go to the bisc.network site to download the software (Screenshot of the download page)
- Verify the integrity of the software using tools such as those offered by Loïc Morel for Windows users.
- Once the installer is verified, launch BISQ, grant the necessary permissions, and accept the terms of use. (Screenshot of the terms of use)
- BISQ will connect to the Bitcoin network and itself via Tor, which may take some time.
- Set up your payment account and make backups of your SID (Secure Identifier) of your wallet to prevent any loss or theft. (Screenshot of the account setup page)
- Also, set up a password to encrypt your information.
Depending on your operating system, BISQ data will be stored in different locations. You can find them in the "Data Directory" folder. Be careful, if you delete this folder, all your BISQ data will be lost. To recover your data through a backup:

- Copy the backup folder to the 'user/application support/BISQ' location.
- Rename the backup folder to 'BISQ'.
- Restart BISQ, and all your data should be restored.

Before you start buying or selling Bitcoin on BISQ, it's crucial to set up your payment account. For example, you can set up an account in your national currency, like a SEPA account, a REVOLUT account, or a PAYPAL account. To set up your REVOLUT account:

- Add an account and select REVOLUT from the list of options. (Screenshot of the account options list)
- You can choose different currencies: euro, pound sterling, US dollar, or Swiss franc.
- The maximum transaction duration is one day, and the purchase limit is 0.25 Bitcoin.
- Use your personal REVOLUT account name to avoid any confusion.
- Make sure to sign your accounts and establish purchase limits for more security.

To buy Bitcoin on BISQ:

- Go to the "Buy" section where you can choose from different markets. (Screenshot of the "Buy" section)
- To benefit from reduced fees, we recommend buying BSQ, which you can purchase with Bitcoin.
- You can choose from different offers based on price, quantity, payment method, etc.
- To buy BSQ, first deposit Bitcoin into your wallet.
- Choose an offer with a low premium and a small quantity for buying BSQ.
- BISQ verifies the validity of the offer and the peer connection.
- If the seller is not connected, choose another.
- Check the offer and accept a 5% premium.
- Confirm the fees and the BSQ exchange, then wait for the transaction confirmation to buy Bitcoins with BSQ.

To sell Bitcoin on BISQ:

- Create a new offer in the "Sell" tab. (Screenshot of the "Sell" tab)
- You can choose to set the number of Bitcoins to sell or the amount in euros you wish to receive.
- You can set a premium as a percentage above the market price.
- You can create a selling range or leave the choice to the buyer.
- You can also set a price to stop the offer.
- Choose the minimum deposit amount and transaction fees.
- Fund the order by depositing the Bitcoins to sell, the amount of the security deposit, and the fees.
- Once you have created the offer, wait for a buyer to show up.
Once the buyer has made the transaction deposit on BISQ, the Bitcoins are automatically sent to the buyer, and you receive the money. The account is verified and signed after a transaction with a signed account.
## LNP2PBOT
<chapterId>e3b61150-90e3-5ab4-bc12-4a05879321f5</chapterId>

![LNp2pbot tutorial](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) is a messaging platform that, with the help of the bot [Lnp2pbot](https://lnp2pbot.com/), allows you to buy and sell bitcoins quickly and easily. Here's how to do it:

To buy Bitcoins via the LNP2PBOT on Telegram, follow these steps:

- Start by going to the Lnp2pbot's Twitter account and click on the link in the bio. (Screenshot of the bot's Twitter account and the link in the bio)
- In Telegram, use the "/buy" or "/sell" commands to post buy or sell orders. (Screenshot of using the "/buy" or "/sell" commands)
- Go to the P2P Lightning channel to find buying and selling offers according to your criteria. (Screenshot of the P2P Lightning channel)
- Create a buy offer using the Lnp2pbot and the "/buy" command.
- Select the currency of your choice, indicate the amount, the price (with a premium if desired), and choose your payment method.
- Wait until a potential seller contacts you.

To sell Bitcoins via Revolut, here's what you need to do:

- Click on 'sell Satoshi' to open a notification on LNP2PBot. (Screenshot of the 'sell Satoshi' option)
- Receive a Lightning invoice to pay in order to sell the Satoshis. (Screenshot of the Lightning invoice)
- Wait for the buyer to send an invoice with the satoshis to receive the payments.
- Establish direct contact with the buyer via Telegram to agree on the payment method and exchange the necessary information.
- Validate the transaction with a note.

If you want to buy Bitcoins by sending an LN Invoice, follow these steps:

- Copy the invoice and send it to the bot to buy Satoshi.
- Make contact with the seller to finalize the purchase of bitcoins.
- In case of a problem, suggest waiting or attempting a cancel.
- Cancel the offer and look for a new one if necessary.
- Choose an offer that accepts instant CPAs for the purchase of Satoshi.
- Send the invoice and wait for the seller's payment confirmation.
- Once the payment is made, send the confirmation to the bot.
- Wait for the validation of the receipt of euros and the sending of satoshis by the seller.
Using these methods, you can buy and sell bitcoins on Telegram securely.

## Peach Bitcoin
<chapterId>05e328c4-1003-586e-85c3-65109e3486e1</chapterId>

site: https://peachbitcoin.com/

We take a detailed look at this solution in BTC 205 offered by @pivi\_, here are the tutorial videos:

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/) is a Swiss mobile application that allows buying and selling bitcoins peer-to-peer. This easy-to-use solution offers an intuitive interface, ideal for cryptocurrency transactions.

The Peach application interface consists of four tabs: buy, sell, history, and settings. (Screenshot of the application interface)
Buying bitcoins on Peach is simplified. To start, you need to create an offer. This is possible by accessing the "buy" tab. (Screenshot of the "buy" tab)
Then, browse the available offers by swiping until you find the one that suits you. The accepted payment methods are varied, including bank transfer, online wallet, gift card, and local option. (Screenshot of available payment methods)
Once you have chosen an offer, you can discuss with the seller via the chat integrated into the application. (Screenshot of the application chat)
After the payment, confirmed by the seller, the transaction is complete. The bitcoins are then sent to the buyer, who receives a notification confirming the receipt of funds. (Screenshot of the bitcoin receipt notification)

Peach is a non-custodial application, meaning the bitcoins remain in your possession throughout the process. However, any potential disputes are managed centrally. Therefore, it is crucial to back up transaction-related information and your personal information using the Backup feature. (Screenshot of the Backup feature)
As Peach is still in beta version, some bugs may occur. It is recommended to verify all information before concluding a transaction.
In summary, the Peach mobile application offers an accessible solution for buying and selling bitcoins peer-to-peer. Secure and optimal use of Peach is key to successful transactions.

## Hold Hodl
<chapterId>2c285751-ae9f-54af-8b28-c7c0beac7b43</chapterId>
[HodlHodl](https://hodlhodl.com/) is a decentralized Bitcoin marketplace that prioritizes user control and security. Unlike traditional exchanges, it operates on a peer-to-peer model, allowing direct exchanges between users. Thanks to its multi-signature escrow system, Hodl Hodl ensures the security of funds during transactions. The platform also supports various payment methods and offers trading options such as Contracts for Difference (CFD).
![hodlhodl tutorial](https://youtu.be/BDH9jE7kpD8)

In this tutorial, we explain how to buy and sell bitcoins peer-to-peer on the HodlHodl platform.

Before starting to use the HodlHodl platform, some preparatory steps are necessary:

- Open the HodlHodl website.
- Create an account using an email address to keep a history of your transactions.
- Read the security guide carefully before starting to trade.
- Note that the platform is not open source and retains some of your personal information.

Here is the process to follow to make a purchase on the HodlHodl platform:

- Use the filter function to find offers that suit you.
- Click on the offer that interests you.
- Fill in the necessary fields to accept the contract.
- In our example, we used Revolut as the payment method.

Setting up the multisig contract for the transaction is done as follows on HodlHodl:

- Once the offer is accepted, make the payment via the chosen method (Revolut in our case).
- Create a multisig contract by generating a password.
- Wait for the bitcoins to be deposited at the multisig address.
- Choose the number of confirmations for the contract.
- Make the payment of the agreed amount to the seller and confirm it on HodlHodl.
- Be patient as the deposit duration can be long, depending on the bank used.
- Wait for the seller's confirmation before releasing the bitcoins after the purchase.

Creating a sale or purchase offer for bitcoins on HodlHodl goes as follows:

- On the HodlHodl site, indicate the release address for purchase offers.
- Enter the amount, price, and payment method.
- You can also add optional features like transaction limits or a title for the offer.
- Once the offer is created, you can view, edit, duplicate, or delete it as you wish.

## Bonus: Side Shift.AI
<chapterId>bd1f0844-af1e-53da-9518-b3b22f802276</chapterId>

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)
Here is a brief tutorial on using [SideShift AI](https://sideshift.ai/), a very handy tool for converting shitcoins into bitcoin. It's the ideal tool for those who have closed all their personal exchanges. No order system is needed, and liquidity is available. However, please note that there is a fee of 2.5% per transaction.
If you have purchased cryptos in a KYC manner, it is recommended to use Monero to convert these cryptos into bitcoin. Monero offers superior privacy compared to Bitcoin. For enhanced security, the CoinJoin operation is also recommended. CoinJoin mixes your transactions with those of other users to complicate the traceability of your transactions.

I would also like to introduce you to an open-source tool for buying and selling bitcoins. This tool allows you to choose from many blockchains. You just need to enter your Bitcoin address and select the amount you wish to send. There is no need to create an account or connect your wallet to the tool. You can use a fixed rate to send or receive a specific amount. Moreover, this tool also allows for the sale of bitcoins in exchange for USDC.

### Support Us

This course, as well as all the content present on this university, has been offered to you for free by our community. To support us, you can share it with others, become a member of the university, and even contribute to its development via GitHub. On behalf of the entire team, thank you!

### Rate the Training

A rating system for the training will soon be integrated into this new E-learning platform! In the meantime, thank you very much for following the course, and if you enjoyed it, think about sharing it with those around you.

# To Go Further
<partId>28194543-78b5-5f98-852a-2fc76439ddde</partId>

## Interview with Steph from Peach Bitcoin
<chapterId>76ed1f17-1d0b-5c0f-8726-91ab4e2e2955</chapterId>

![interview with Steph](https://youtu.be/LRGKD8qNSXw)

Here is a summary of the interview:

Peach Bitcoin is a non-custodial mobile application, enabling the peer-to-peer buying and selling of Bitcoin. Currently, the Pitch Bitcoin team, based in Switzerland, includes eight members and is striving to evolve the application to also serve as a wallet. The unique model of Pitch Bitcoin is based on a centralized company structure, while maintaining a decentralized buy and sell ledger. Additionally, the application offers an option for cash transactions during in-person meetings.
One of the main advantages of Pitch Bitcoin is the level of security it offers to users. The escrow system with multisignature and time lock is designed to manage conflicts and ensure the security of transactions. Moreover, Pitch Bitcoin has priority access to the multisignature funds, allowing it to transfer bitcoins to the buyer in case of malicious behavior on the part of the seller. The company plans to integrate all European currencies as well as other payment methods when it launches in open beta in January.

The idea for Pitch Bitcoin was born from its founder's personal experience in the Bitcoin industry. After discovering Bitcoin in 2017 and attending several meetups and conferences, she became a Bitcoin maximalist and saw the opportunity to create a platform for Bitcoiners to meet and conduct cash transactions. Additionally, the application includes encrypted chat for communicating with other users, thus preserving user anonymity.

Currently, Pitch Bitcoin is developing several features to facilitate sellers' work, including the creation of an API for sellers, a platform for large sellers, and the integration of BTC Pay Server to automate transfers. The application will be launched in open beta in January 2023.

To conclude, the founder of Pitch Bitcoin emphasizes the importance of competition in the Bitcoin ecosystem, as what is good for Bitcoin is beneficial for everyone. She also encourages diversity and inclusion in the Bitcoin industry and beyond.

## Interview with Pierre
<chapterId>4e4ba218-01ec-5f3a-bc49-c148bb22ee61</chapterId>

![interview with Pierre](https://youtu.be/COoezuJncm8)

Here is a summary of the interview:
This interview concludes the Bitcoin 205 course, which addresses the topic of peer-to-peer Bitcoin purchasing solutions. Organized by Pierre, this course aims to educate the French-speaking public on the technical solutions for peer-to-peer Bitcoin purchases, an area that has been neglected until now. Thanks to the progress made, it is now possible to buy and use Bitcoin while preserving one's privacy, even with just a phone and the Telegram app.

One of the methods highlighted is the use of CoinJoin with Samourai to enhance security. This solution minimizes the risks associated with centralized entities holding personal information about Bitcoin users. It is recommended to buy Bitcoins non-KYC, a method that strengthens anonymity. Moreover, some exchange platforms like Kraken offer lower withdrawal fees than others, aligning with the principles of Bitcoin.
Bisq, Robosat, and Peach are presented as democratic solutions for Bitcoin trading. Peach, in particular, is highlighted for its ease of access as a mobile application. However, there are challenges to address, including the regulation of cryptocurrencies and the need to respect certain limits to avoid excessive regulation.

The use of Bitcoin ATMs is also discussed; these represent an economical method for obtaining non-KYC bitcoins. Depending on local regulations, these ATMs can be installed at home or in public places and can be used to offer bitcoins to close ones or for payments in bars.

The training emphasizes the importance of education's role in understanding Bitcoin. It is suggested that Bitcoin can offer a solution in case of recession or hyperinflation and that it is important to raise awareness of its potential before it's too late. Moreover, it is highlighted that the separation of state and money is as essential as the separation of state and religion.

In conclusion, Bitcoin is presented as a decentralized currency requiring public education and an open mind to be fully understood and utilized. The training aims to help participants understand the various peer-to-peer purchasing solutions and to use these tools to enhance their anonymity and security when using Bitcoin.

## Evaluate this course
<chapterId>a6410a99-adfc-50fd-a004-8048be620c8a</chapterId>
<isCourseReview>true</isCourseReview>

## Final Exam
<chapterId>38d03a01-ae5f-5c21-acd4-42f18b20c2b4</chapterId>
<isCourseExam>true</isCourseExam>

## Bonus Article on Privacy
<chapterId>9f1aa75a-3031-58b2-9d4a-11a5c4197302</chapterId>

A great [article](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) by Loïc Morel on KYC and the identification

This in-depth article explores the challenges and solutions for preserving privacy when acquiring and using bitcoins. Loïc deconstructs some common misconceptions about KYC (Know Your Customer) identification, details the risks associated with this process, and offers techniques for maintaining the anonymity of transactions. It's a must-read for those looking to understand the nuances of privacy in the Bitcoin world, and to learn how to use tools like CoinJoin, Stonewall, and PayJoin to obscure transaction tracing and thus protect their privacy.