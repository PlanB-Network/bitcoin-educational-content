---
name: Peer-to-Peer Bitcoin Buying and Selling Solution
goal: Explore non-KYC solutions for buying and selling Bitcoin
objectives:
  - Understand the different types of KYC, their risks, and benefits
  - Understand the advantages of peer-to-peer buying
  - Implement the solution that fits your needs
  - Improve the management of your UTXO (KYC and non-KYC)
---

# A Journey into the World of Non-KYC

![course poster](assets\btc_205_vignette_presentation_03.png)

Pierre offers us this course that delves into the various existing solutions for buying and selling bitcoins peer-to-peer. Peer-to-peer buying is completely legal and allows for more anonymity, as these solutions are not KYC. KYC (Know Your Customer) is a rule of market regulators (AMF) that requires identification from the customer wishing to buy or sell bitcoin. These rules aim to prevent money laundering, terrorism financing, and tax evasion. At the risk of significant consequences for the user, KYC aims to defend and protect its user, although the opposite effect is often observed.

We will therefore explore the different types of KYC (full KYC type France, KYC Light type Switzerland, and non-KYC type peer-to-peer). Pierre will present more than 6 solutions, so you will have all the cards in hand to discover which one suits you. If you want a KYC solution, know that they are present in the BTC 102 course.

+++

# Introduction

![introduction by Rogzy](https://youtu.be/3AHeKLTK7Sg)

## Explanation & Type of KYC

![explanation of KYC types](https://youtu.be/kDhXoPU1KtM)

KYC, or "Know Your Customer," is a regulatory standard that requires the collection of private customer information, such as their physical address, identification, or bank statements. This practice is common on brokerage platforms, which may require a complete KYC, including detailed information such as identification, a photo, proof of address, salary sheets, etc.
The main objective of KYC is to combat money laundering, terrorism financing, and tax evasion. It is a law put in place by the AMF (Autorité des marchés financiers), the French market regulatory body. However, the application of KYC leads to the centralization of very sensitive databases containing personal user information. This information, having a certain value, can be sold to malicious entities.
In addition, exchange platforms often require an excessive amount of personal information, putting users at risk and increasing compliance costs. These regulatory costs can discourage French businesses and harm their competitiveness on an international scale.

There are three types of KYC, including full KYC which requires a complete and regulated collection of information to access the service. In Switzerland, an alternative called "KYC light" allows for the purchase and sale of bitcoins without providing identification, as long as the purchase amount does not exceed 1000 euros per day. Solutions like Relay allow for the use of this method.

In this context, Swiss authorities can access banking information to investigate individuals considered at risk. Bitcoin delivery addresses are also traceable through the banking system. KYC light is generally considered simpler and less expensive than the French system.

In France, buying bitcoins online requires sending money to a third party, via SEPA transfer or Paypal. For those who prioritize anonymity, security, and privacy, cash purchase solutions for bitcoins are also available. For low volumes, buying bitcoins in cash is a simple and legal option.

To be able to sell 100 euro PLT of bitcoin daily to anyone, regulation by the AMF (Financial Markets Authority) is necessary. In France, this regulation mainly applies to individuals who carry out significant transaction volumes. The other two methods of buying bitcoin include the use of automatic teller machines (ATMs) and exchanges between friends. ATMs are regulated and require identification for transactions over 500 euros. Exchange between friends, on the other hand, offers a more discreet exposure to bitcoin.

These regulatory measures are in place to counter terrorism financing, tax evasion, and money laundering. Bitcoin, as a fully traceable database, makes money laundering particularly difficult. The use of Bitcoin by criminals can be traced, making Bitcoin an ineffective tool for money laundering.

It is important to note that this training presents various alternatives, as well as tools that can be used for malicious or non-malicious purposes. Additionally, it provides explanations on the functioning of order books between makers (order providers) and takers (order takers).

It is also important to note that the information presented here does not endorse any particular solution. It simply presents the available options for a better understanding of the subject. For any additional questions about Bitcoin, do not hesitate to consult online resources such as www.découvrebitcoin.com.

## Comparison of peer-to-peer buying and selling solutions

![Comparison of peer-to-peer buying and selling solutions](https://youtu.be/HiwSjN04Mz0)

P2P Solutions for Buying Bitcoin: Bisq, RoboSat, LNP2PBot, Peach, and HodlHodl

Buying Bitcoin peer-to-peer (P2P) is a preferred option for investors looking to avoid centralized exchange platforms. This part of the course examines different P2P solutions available, including Bisq, RoboSat, LNP2PBot, Peach, and HodlHodl.

Comparison of Advantages and Disadvantages of Different Solutions

Each P2P solution has its own advantages and disadvantages. We provide an overview of the key features of each solution below.

### Bisq

[Bisq](https://bisq.network/) is a non-custodial P2P solution that has a DAO (Decentralized Autonomous Organization) system and uses multisign for dispute management. Its code is open source, which contributes to its robustness and protection of user privacy.

| Advantages                                    | Disadvantages                                                                                          |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| - P2P solution, non-custodial, multisign, DAO | - The application is quite heavy and not very user-friendly, only available on computer                |
| - Robust and secure                           | - Purchase and sale limitations as well as account management with signatures are double-edged swords. |
| - Open source                                 |                                                                                                        |

### RoboSat

[RoboSat](https://learn.robosats.com/) is an easy-to-use, fast solution that operates under TOR and does not require an account. It is open source and uses the Lightning Network to enable fast transactions.

| Advantages                                         | Disadvantages                                                           |
| -------------------------------------------------- | ----------------------------------------------------------------------- |
| - Easy to use                                      | - The protocol is fragile with a single coordinator                     |
| - Low transaction fees                             | - Requires technical knowledge and an understanding of privacy          |
| - Uses the Lightning Network for fast transactions | - The Umbrell application allows for managing one's own client instance |
| - Open source                                      |                                                                         |

### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) is accessible via Telegram for non-KYC Bitcoin purchases. It offers fast transactions through the Lightning Network and low fees.

| Advantages                                        | Disadvantages                                        |
| ------------------------------------------------- | ---------------------------------------------------- |
| - Accessible via Telegram                         | - Less robust and secure than other solutions        |
| - Fast transactions through the Lightning Network | - Less fast and less user-friendly than Robosat      |
| - Low transaction fees                            | - Can be linked to the user's Telegram identity      |
| - Internal dispute management                     | - Lack of liquidity and fragility of the application |
| - Community proposals to limit the trust problem  | - LNP2Pbot must be trusted to manage disputes        |

### Peach

[Peach](https://peachbitcoin.com/) is a mobile application dedicated to Bitcoin trading. It stands out for its simplicity, not requiring the creation of an account to operate. Trades are fast, even in the absence of Lightning Network. In addition, notifications on phones speed up the transaction process.

| Advantages                                              | Disadvantages                                                                                                    |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| - Simplified use: no account creation is necessary.     | - Security and robustness: being linked to a company, peach has potential weaknesses in terms of security.       |
| - Transaction speed: exchanges are fast.                | - Absence of Lightning Network: this technology, which allows faster Bitcoin transactions, is not used by peach. |
| - Notifications: they speed up the transaction process. |                                                                                                                  |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) is a non-custodial solution for Bitcoin exchange. It offers many advantages such as strong liquidity, the possibility of private trades, a referral system, as well as accounts with trade history and a rating system. However, trades are linked to the user's email address and digital identity, stored at HodlHodl. In addition, HodlHodl's source code is not open to the public and the application cannot be used with Tor.

| Advantages                                                                                             | Disadvantages                                                                                                          |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| - Non-custodial: the user remains in possession of their private keys.                                 | - Storage of personal information: the user's email address and digital identity are stored by HodlHodl.               |
| - Liquidity: HodlHodl offers a wide range of exchange possibilities.                                   | - Closed source code: HodlHodl's code is not open to the public.                                                       |
| - Possibility of private trades: the user can choose who to trade with.                                | - Incompatibility with Tor: HodlHodl cannot be used with this privacy-focused network.                                 |
| - Referral system: HodlHodl rewards word-of-mouth.                                                     | - Possibility of forced KYC: in certain situations, HodlHodl may require identification information to retrieve funds. |
| - Trade history and rating system: these features allow for evaluating the reliability of other users. |                                                                                                                        |

## Conclusion on P2P solutions

In summary, each P2P solution has its advantages and disadvantages. Bisq is considered the most robust and secure, but less user-friendly. RoboSat is open source but less robust than Bisq. LNP2PBot is less robust and secure than other solutions, less fast and less user-friendly than RoboSat, but more than Bisq. Peach is the easiest and fastest application to buy Bitcoin without KYC, but there is a company behind it, so weaknesses in terms of security and robustness. HodlHodl is a protocol managed by a company and closed source, so weaknesses in terms of security and robustness, and a bit more complicated than Peach.

Good old cash face-to-face is still a solution for small amounts.

In addition to P2P solutions, there are other cryptocurrency exchange options. kycnot.me offers services such as VPN, VPS, SMS, etc. Bitrefil allows you to buy gift cards. Each solution on [kycnotme](https://kycnot.me/) is presented with its positive and negative points.

# Tutorials on P2P buying/selling solutions

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) is an open source project developed by Reckless Satoshi to privately exchange Bitcoins for national currencies. It simplifies the peer-to-peer experience and uses Lightning invoices to minimize custody and trust needs. To use it, we will need Tor, an anonymous communication network.

The first thing you need to do is download Tor. You can find it on GitHub or directly on the official website at the following address: tor.org/download.
Once Tor is downloaded and installed:

- Press "Connect" to establish the connection.
- Go to the [robosats onion address](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Copy the token to save your identity.

Here are the steps to buy bitcoins with Robosats:

- Check the order book, you can filter by currency and payment method - for example, buy bitcoin in euros with Revolut.
- Before buying, check the offer expiration, the price in euros, and the premium (you can also filter offers by premium).
- Preferably, choose an offer with an active user and with a premium lower than the average.
- Check the order summary with the amount, payment method, premium, order ID, and expiration.
- You can receive your satoshis on a Bitcoin address with a swap-out fee (from LN to BTC-onchain) of around 1% (you can modify the on-chain mining fees).
- Otherwise, create an invoice with an LN wallet from this [list](https://learn.robosats.com/docs/wallets/) and copy the invoice to Robosats.
- Contact the seller via encrypted chat to discuss fiat payment.

Now let's see the steps for selling bitcoins on Robosats:

- Customize your offer by choosing the payment method, premium, expiration time, etc.
- Fidelity Bond Size is the equivalent of a security deposit on BISC. Put 15% or 10% of security deposits to encourage the other party to play fair.
- Lock the satoshis to confirm the creation of the order and avoid spam.
- If someone accepts your sales offer, discuss with the peer to proceed with fiat payment. Once payment is made, the trade is completed and the satoshis are sold!

## BISQ: peer-to-peer buying solution

[Bisq](https://bisq.network/) is a decentralized exchange platform for digital assets, mainly Bitcoin. It allows direct, secure, and private transactions between users worldwide without the need for an intermediary.

🚨 Please exercise caution when using Bisq as it is an advanced solution. It may not be suitable for beginner users. Make sure you have some experience and understanding before getting started. 🚨

We are looking at this solution in detail, here are the tutorial videos:

![part 1](https://tube.nuagelibre.fr/videos/watch/b3885ea9-23e9-4b58-aa3f-401348da85a1)

![part 2](https://tube.nuagelibre.fr/videos/watch/53276305-70d6-4c7f-9df9-e100a82eee16)

For the more resourceful, here is a concise guide outlining the essential steps:

1. Download and Install: Visit the Bisq website and download the application. Install it on your system.
2. Configure Payment Method: Open the application and go to "Account". Add the details of your payment method.
3. Fund Your Bisq Wallet: Click on "Funds" and "Receive Funds" to get your Bisq address. Send Bitcoins to this address.
4. Make a Transaction: Click on "Buy/Sell" and choose the desired transaction. Follow the instructions to complete the transaction.

## 5. Confirm Receipt:

Once you have received payment, confirm it in the Bisq application. This releases the Bitcoin from escrow. Always remember to check all transaction details and only deal with trusted parties.

Here is a complete guide that will walk you through all the steps to use Bisq.

Bisq is a decentralized and secure network that respects your private property. It is non-custodial, meaning you always own your funds. Additionally, Bisq uses a token, BSQ, which allows you to pay lower transaction fees and encourages your participation in the Decentralized Autonomous Organization (DAO). To protect sellers during Bitcoin-fiat transactions, Bisq has implemented a system of signatures and account limits. As a buyer, you will need to obtain a signed account to increase your purchase limit. The signature is also a way to verify the history of traders, ensuring transaction security.

To install Bisq and backup your data, follow these simple steps:

- Go to the bisc.network website to download the software (Screenshot of the download page)
- Verify the integrity of the software using tools such as those provided by Loïc Morel for Windows users.
- Once the installer is verified, launch Bisq, grant necessary permissions, and accept the terms of use. (Screenshot of the terms of use)
- Bisq will connect to the Bitcoin network and itself via Tor, which may take some time.
- Set up your payment account and backup your Secure Identifier (SID) wallet to prevent loss or theft. (Screenshot of the account configuration page)
- Also, set up a password to encrypt your information.

Depending on your operating system, Bisq data will be stored in different locations. You can find them in the "Data Directory" folder. Be careful, if you delete this folder, all your Bisq data will be lost.
To recover your data using a backup:

- Copy the backup folder to the 'user/application support/BISQ' location.
- Rename the backup folder to 'BISQ'.
- Restart Bisq, and all your data should be restored.

Before buying or selling Bitcoin on Bisq, it is crucial to set up your payment account. For example, you can set up an account in your national currency, such as a SEPA account, a REVOLUT account, or a PAYPAL account.
To set up your REVOLUT account:

- Add an account and select REVOLUT from the list of options. (Screenshot of the account options list)
- You can choose different currencies: euro, pound sterling, US dollar, or Swiss franc.
- The maximum transaction duration is one day and the purchase limit is 0.25 Bitcoin.
- Use your personal REVOLUT account name to avoid confusion.
- Make sure to sign your accounts and establish purchase limits for added security.

To buy Bitcoin on BISQ:

- Go to the "Buy" section where you can choose different markets. (Screenshot of the "Buy" section)
- To benefit from reduced fees, we recommend buying BSQ, which you can buy with Bitcoin.
- You can choose from different offers based on price, quantity, payment method, etc.
- To buy BSQ, first deposit Bitcoin into your wallet.
- Choose an offer with a low premium and low quantity for buying BSQ.
- BISQ verifies the validity of the offer and the peer's connection.
- If the seller is not connected, choose another one.
- Check the offer and accept a 5% premium.
- Confirm the fees and BSQ exchange, then wait for transaction confirmation to buy Bitcoins with BSQ.

To sell Bitcoin on BISQ:

- Create a new offer in the "Sell" tab. (Screenshot of the "Sell" tab)
- You can choose to set the number of Bitcoins to sell or the amount in euros you want to receive.
- You can set a premium as a percentage above the market price.
- You can create a sales range or leave the choice to the buyer.
- You can also set a price to stop the offer.
- Choose the minimum deposit amount and transaction fees.
- Fund the order by depositing the Bitcoins for sale, the deposit amount, and the fees.
- Once you have created the offer, wait for a buyer to appear.

Once the buyer has deposited the transaction on BISQ, the Bitcoins are automatically sent to the buyer and you receive the money. The account is verified and signed after a transaction with a signed account.

## LNP2PBOT

![LNp2pbot tutorial](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) is a messaging platform that, with the help of the [Lnp2pbot](https://lnp2pbot.com/) bot, allows you to buy and sell bitcoins quickly and easily. Here's how:

To buy Bitcoins via the LNP2PBOT Bot on Telegram, follow these steps:

- Start by going to the Twitter account of the Lnp2pbot bot and click on the link in the bio. (Screenshot of the Lnp2pbot Twitter account and the link in the bio)
- In Telegram, use the "/buy" or "/sell" commands to post buy or sell orders. (Screenshot of using the "/buy" or "/sell" commands)
- Access the P2P Lightning channel to find buy and sell offers according to your criteria. (Screenshot of the P2P Lightning channel)
- Create a buy offer using the Lnp2pbot bot and the "/buy" command.
- Select the currency of your choice, indicate the amount, the price (with a premium if desired), and choose your payment method.
- Wait until a potential seller contacts you.

To sell Bitcoins via Revolut, here's what you need to do:

- Click on 'sell Satoshi' to open a notification on LNP2PBot. (Screenshot of the 'sell Satoshi' option)
- Receive a Lightning invoice to pay to sell the Satoshis. (Screenshot of the Lightning invoice)
- Wait for the buyer to send an invoice with the satoshis to receive the payments.
- Establish direct contact with the buyer via Telegram to agree on the payment method and exchange necessary information.
- Validate the transaction with a note.

If you want to buy Bitcoins by sending an LN Invoice, follow these steps:

- Copy the invoice and send it to the bot to buy Satoshi.
- Contact the seller to finalize the purchase of bitcoins.
- In case of a problem, propose to wait or try a cancel.
- Cancel the offer and search for a new one if necessary.
- Choose an offer that accepts instant CPA for buying Satoshi.
- Send the invoice and wait for the seller's payment confirmation.
- Once the payment is made, send the confirmation to the bot.
- Wait for the validation of the receipt of euros and the sending of satoshis by the seller.

By using these methods, you can buy and sell bitcoins on Telegram securely.

## Peach Bitcoin

site: https://peachbitcoin.com/

We are looking in detail at this solution in BTC 205 offered by @pivi\_, here are the tutorial videos:

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/) is a Swiss mobile application that allows you to buy and sell bitcoins peer-to-peer. This easy-to-use solution offers an intuitive interface, ideal for cryptocurrency transactions.

The Peach application interface consists of four tabs: buy, sell, history, and settings. (Screenshot of the application interface)
Buying bitcoins on Peach is simplified. To start, you need to create an offer. This is possible by accessing the "buy" tab. (Screenshot of the "buy" tab) Then, browse through the available offers by swiping until you find one that suits you. The accepted payment methods are varied, including bank transfer, online wallet, gift card, and local option. (Screenshot of available payment methods)

Once you have chosen an offer, you can chat with the seller via the application's integrated chat. (Screenshot of the application's chat) After payment, confirmed by the seller, the transaction is complete. The bitcoins are then sent to the buyer, who receives a notification confirming receipt of the funds. (Screenshot of the bitcoin receipt notification)

Peach is a non-custodial application, which means that the bitcoins remain in your possession throughout the process. However, any potential disputes are managed centrally. Therefore, it is crucial to back up transaction information and personal information using the Backup feature. (Screenshot of the Backup feature)

As Peach is still in beta version, some bugs may occur. It is recommended to check all information before concluding a transaction.

In summary, the Peach mobile application offers an accessible solution for buying and selling bitcoins peer-to-peer. Safe and optimal use of Peach is the key to successful transactions.

## Hold Hodl

[HodlHodl](https://hodlhodl.com/) is a decentralized Bitcoin marketplace that prioritizes user control and security. Unlike traditional exchanges, it operates on a peer-to-peer model, allowing for direct exchanges between users. With its multi-signature escrow system, Hodl Hodl guarantees the security of funds during transactions. The platform also supports various payment methods and offers trading options such as contracts for difference (CFD).

![hodlhodl tutorial](https://youtu.be/BDH9jE7kpD8)

In this tutorial, we explain how to buy and sell bitcoins peer-to-peer on the HodlHodl platform.

Before starting to use the HodlHodl platform, some preparation steps are necessary:

- Open the HodlHodl website.
- Create an account using an email address to keep a record of your transactions.
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
- Wait for the bitcoins to be deposited to the multisig address.
- Choose the number of confirmations for the contract.
- Make the agreed-upon payment to the seller and confirm it on HodlHodl.
- Be patient as the deposit duration may be long, depending on the bank used.
- Wait for the seller's confirmation before releasing the bitcoins after the purchase.

Creating an offer to buy or sell bitcoins on HodlHodl is done as follows:

- On the HodlHodl website, indicate the release address for buy offers.
- Enter the amount, price, and payment method.
- You can also add optional features such as transaction limits or a title for the offer.
- Once the offer is created, you can view, edit, duplicate, or delete it as you wish.

## Bonus: Side Shift.AI

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)

Here's a brief tutorial on using [SideShift AI](https://sideshift.ai/), a very useful tool for converting shitcoins to bitcoin. It's the ideal tool for those who have closed all their personal exchanges. No order system is required, and liquidity is available. However, please note that there is a 2.5% transaction fee.

If you bought cryptos in a KYC manner, it is recommended to use Monero to convert these cryptos to bitcoin. Monero offers greater privacy than Bitcoin. For increased security, the CoinJoin operation is also recommended. CoinJoin mixes your transactions with those of other users to complicate the traceability of your transactions.

I would also like to introduce you to an open-source tool for buying and selling bitcoins. This tool allows you to choose from many blockchains. Simply enter your Bitcoin address and select the amount you want to send. There is no need to create an account or connect your wallet to the tool. You can use a fixed rate to send or receive a specific amount. Additionally, this tool also allows for the sale of bitcoins in exchange for USDC.

### Support us

This course, as well as all the content available on this university, has been offered to you for free by our community. To support us, you can share it with others, become a member of the university, and even contribute to its development via GitHub. On behalf of the entire team, thank you!

### Course Rating

A rating system for the course will soon be integrated into this new E-learning platform! In the meantime, thank you very much for taking the course and if you enjoyed it, please consider sharing it with others.

# To go further

## Interview with Steph from Peach Bitcoin

![interview with Steph](https://youtu.be/LRGKD8qNSXw)

Here is a summary of the interview:

Peach Bitcoin is a non-custodial mobile application that allows for peer-to-peer buying and selling of Bitcoin. Currently, the Peach Bitcoin team, based in Switzerland, consists of eight members and is working to evolve the application to also serve as a wallet. Peach Bitcoin's unique model is based on a centralized company structure while maintaining a decentralized order book. Additionally, the application offers an option for cash transactions during in-person meetings.

One of the main advantages of Peach Bitcoin is the level of security it offers to users. The deskrow system with multisignature and time lock is designed to handle disputes and ensure transaction security. Additionally, Peach Bitcoin has priority access to the multisignature money, allowing it to transfer bitcoins to the buyer in case of malicious behavior by the seller. The company plans to integrate all European currencies as well as other payment methods when it launches in open beta in January.

The idea for Peach Bitcoin came from the founder's personal experience in the Bitcoin industry. After discovering Bitcoin in 2017 and attending several meetups and conferences, she became a Bitcoin maximalist and saw the opportunity to create a platform for Bitcoiners to meet and transact in cash. Additionally, the application includes an encrypted chat to communicate with other users, preserving user anonymity.

Currently, Peach Bitcoin is developing several features to make it easier for sellers, including creating an API for sellers, a platform for large sellers, and integrating BTC Pay Server to automate transfers. The application will be launched in open beta in January 2023.

In conclusion, the founder of Peach Bitcoin emphasizes the importance of competition in the Bitcoin ecosystem, as what is good for Bitcoin is beneficial for everyone. She also encourages diversity and inclusion in the Bitcoin industry and beyond.

## Interview with Pierre

![interview with Pierre](https://youtu.be/COoezuJncm8)
Here is a summary of the interview:

This interview concludes the Bitcoin 205 training which addresses the subject of peer-to-peer Bitcoin purchasing solutions. Organized by Pierre, this training aims to educate the French-speaking public on the technical solutions for peer-to-peer Bitcoin purchasing, a field that has been neglected until now. Thanks to the progress made, it is now possible to buy and use Bitcoin while preserving one's privacy, even with a simple phone and the Telegram application.

One of the methods highlighted is the use of CoinJoin with Samouraï to enhance security. This solution minimizes the risks associated with centralized entities holding personal information about Bitcoin users. It is recommended to buy Bitcoins in a non-kyc way, a method that enhances anonymity. In addition, some exchange platforms like Kraken offer lower withdrawal fees than others, which aligns with Bitcoin principles.

Bisq, Robosat, and Peach are presented as democratic solutions for Bitcoin trading. Peach, in particular, is highlighted for its ease of access as a mobile application. However, there are challenges to be overcome, including cryptocurrency regulation and the need to respect certain limits to avoid excessive regulation.

The use of Bitcoin ATM dispensers is also discussed, as they represent an economical method for obtaining non-KYC bitcoins. Depending on local regulations, these dispensers can be installed at home or in public places and can be used to offer bitcoins to loved ones or for payments in bars.

The training emphasizes the importance of education in understanding Bitcoin. It is suggested that Bitcoin can offer a solution in the event of a recession or hyperinflation and that it is important to raise awareness of its potential before it is too late. In addition, it is emphasized that the separation of the state and currency is as essential as the separation of the state and religion.

In conclusion, Bitcoin is presented as a decentralized currency requiring public education and an open mind to be fully understood and used. The training aims to help participants understand the various peer-to-peer purchasing solutions and use these tools to enhance their anonymity and security when using Bitcoin.

## Bonus article on privacy

A great [article](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) by Loïc Morel on KYC and identification.
This in-depth article explores the challenges and solutions for preserving privacy when acquiring and using bitcoins. Loïc deconstructs some misconceptions about KYC (Know Your Customer) identification, details the risks associated with this process, and offers techniques for maintaining transaction anonymity. It is a must-read for those seeking to understand the nuances of privacy in the world of Bitcoin, and to learn how to use tools like CoinJoin, Stonewall, and PayJoin to blur transaction tracing and protect their privacy.
