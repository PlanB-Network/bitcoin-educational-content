---
name: Bisq Easy Mobile
description: A peer-to-peer trading protocol for new bitcoin users - no intermediaries, no KYC.
---
![cover](assets/cover.webp)

## Introduction

The [Bisq Easy](https://bisq.network/bisq-easy/) trade protocol is designed for [Bisq 2](https://github.com/bisq-network/bisq2), the successor to [Bisq v1](https://github.com/bisq-network/bisq). Bisq 2 will support multiple trade protocols, privacy networks, and identities. It facilitates the purchase of Bitcoin with zero trade fees and no security deposit requirement. It is intended for new Bitcoin buyers seeking a non-KYC option who want to be efficiently onboarded by experienced and knowledgeable sellers who are familiar with the Bisq platform.

Currently, Bisq Easy is the only trade protocol for Bisq 2. More trade protocols are planned for the future. Learn more about Bisq 2 in this tutorial:

https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

This short guide is a complement to the tutorial above on purchasing Bitcoin using the [Bisq Easy Mobile](https://github.com/bisq-network/bisq-mobile) application and Lightning.

## 1️⃣ Getting Started

To begin, download Bisq Easy Mobile from the [download page](https://bisq.network/downloads/). It's recommended to Verify the download. Verification instructions are also available on the [download page](https://bisq.network/downloads/). After installation, you need to accept the `User Agreement`. Next, create a public profile consisting of a `nickname` and avatar (represented by a `bot icon`). With Bisq Easy, you can also create multiple user profiles within one client. After a brief initialization, you will land on the `Home Screen`. The app highlights educational material directly on the main page. Tap `Open Trade Guide` to familiarize yourself with the latest information.

![image](assets/en/01.webp) 

The Trade guide explains everything relevant in easy steps:

- How to trade on Bisq Easy
- How does the trade process work
- What do I need to know about trade rules.

Another important section is **"How safe is it to trade on Bisq Easy?"**

![image](assets/en/08.webp) 

Check the box labeled `I have read and understood` and tap `Finish`.

![image](assets/en/02.webp) 

## 2️⃣ Backup your data

Before we begin, let's take care of some housekeeping tasks and create a `backup` of your data storage file. Go to `More` > `Backup & Restore` to save your profile and trade history. If you lose your device without a backup, your reputation and ongoing trades are unrecoverable. Provide a `Password` to encrypt your backup. 

![image](assets/en/11.webp)

## 3️⃣ Offers

From the `Home screen`, there are two ways to navigate to the offers. Tap `Explore offers` in the middle of the screen or tap `Offers` in the bottom menu. From there, select the `currency` you want to trade in.

![image](assets/en/03.webp) 

Unlike [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), which requires collateral, Bisq Easy relies solely on the reputation of the seller for security. While this approach enables buyers to purchase Bitcoin for the first time without prior ownership, it places a high degree of trust in the seller's ability to deliver Bitcoin after receiving fiat payments. Therefore, the Bisq Easy security model is optimized only for small trade amounts and trades are limited to $600 USD equivalent per transaction to minimize risk. In the `Offerbook` section, select filters for payment methods and settlement in Lightning or Bitcoin (on-chain).

![image](assets/en/04.webp) 

After applying `filters`, select a suitable offer from a reputable trade partner. The seller's pre-selected payment method and settlement type (`Lightning` or `on-chain`) will be displayed. Ensure these match your preferences before proceeding. We select the Lightning ⚡ option here.

![image](assets/en/05.webp) 

Review and confirm the trade details by tapping on `Confirm take offer`. Then a Popup screen confirms that you have successfully taken the offer. Tap Show trade in `Open Trades`. In the Open Trades section, paste your `Lightning invoice` and tap `Send to the seller` to share it. Now Wait for the seller's payment account data. Sellers may take time to respond. Check back periodically for updates in the chat window.

![image](assets/en/06.webp) 

Send a brief greeting in the chat. The seller will share payment details when they come online

![image](assets/en/09.webp) 

Once you've received the necessary payment details from the seller, proceed with completing the payment. Afterward, tap on the `Confirm you made the payment` button, then patiently await confirmation of receipt. ️ ⌛️

Finally, when the seller confirms payment receipt, you must also confirm receipt of the Bitcoin. This completes the purchase using Bisq in Easy Mode. Congratulation! You can now tap on `close the trade` button. 

![image](assets/en/10.webp) 

## 4️⃣ Dispute Resolution on Bisq Easy

If anything goes wrong with your trade, both buyers and sellers can request mediation support.

**What Mediators Can Do:**
• Help facilitate successful trade completion
• Verify fiat, altcoin, and Bitcoin payments
• Cancel trades when necessary
• Report serious rule violations to moderators for potential user bans

**Consequences for Fraudulent Sellers:**
Depending on their reputation type:

- **BSQ Bond Reputation**: The DAO may confiscate their bonded BSQ
- **Onion Address Reputation**: Their Bisq 1 onion address may be banned

**Important Note:** Since all reputation is tied to your user profile, a ban disables your reputation completely.

## 5️⃣ Create your own offer

Instead of taking existing offers, you can create your own buy offer and let sellers come to you. This is the right option if you don't find any offers with the right premium or payment methods in the market you want to trade in, though you'll need to wait for a seller to accept.

From the `Offers screen`, tap the green `+` icon in the bottom right corner. Then select `Buy Bitcoin` and choose your fiat currency.

Set your trade parameters:

- **Fixed amount or Range amount**: Choose a how much you want to spend.
- **Payment method**: Select from available options
- **Settlement**: Choose Lightning ⚡ or ₿ on-chain 

Review your details and tap `Create offer`. Your offer now appears in the `Offerbook`.

![image](assets/en/07.webp) 

*Note: As a buyer on Bisq Easy, you don't need reputation—this is the key advantage. Sellers bear the reputation requirement and risk, which is why they charge premiums. Your offer simply needs to be priced attractively enough for reputable sellers to consider.*

Once published, wait in the `Offerbook` section. When a seller takes your offer, you'll receive a notification. Open the trade in `Open Trades`, where the seller and you able to exchange your payment details. Send your Bitcoin address or Lightning invoice to the seller. After sending fiat, confirm payment. Once the seller confirms receipt, they'll release the Bitcoins to complete the trade.

## 🎯 Conclusion

Bisq Easy enables Bitcoin purchases without collateral, solving the classic chicken-and-egg problem for new buyers. The trade-off is clear: you rely on seller reputation instead of locked funds for security. This trust-based approach explains the typical 5-15% premium, which compensates reputable sellers for their investment in building trust and providing support. While the system limits trades to small amounts to contain potential losses, always stick to sellers with solid reputation scores. For newcomers willing to accept these terms, Bisq Easy offers an easy entry point to Bitcoin.

## 📚 Bisq Easy Mobile Resources

[Github](https://github.com/bisq-network/bisq-mobile) | [Website ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)