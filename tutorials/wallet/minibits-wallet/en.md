---
name: Minibits Wallet
description: Guide for Minibits Wallet
---

![cover](assets/cover.webp)

In this tutorial, I will walk you through setting up Minibits Wallet to use ecash. A powerful privacy-focused payment technology that works alongside Bitcoin. Minibits is an ecash and Lightning wallet that enables instant, cheap, and private value transfers, making it ideal for everyday transactions where privacy matters.

Before we dive into Minibits, let's establish a clear understanding of what ecash is and isn't. Many people confuse ecash with Bitcoin or blockchain technology, but they're fundamentally different concepts.

Ecash is NOT Bitcoin. It doesn't replace your self-custodial Bitcoin wallet but rather complements it. Ecash is NOT a blockchain and does NOT live on any public ledger. Interestingly, ecash is NOT a new technology—it actually predates the worldwide web, with concepts developed in the 1980s and 1990s.

What ecash IS: incredibly private (transactions leave no traceable history), peer-to-peer (direct transfers without intermediaries), and functions as a digital bearer instrument (if you possess it, you control it). A key advantage is that ecash CAN be used offline—either the sender or receiver can be disconnected from the internet during transactions. Ecash CAN be minted by a single party or by a federation of trusted entities, and it IS a perfect complementary technology to Bitcoin, handling small, frequent transactions while Bitcoin serves as the settlement layer.   

Please note that this Minibits setup represents a `custodial solution`, which means you're trusting the Mint operator to manage your funds. This introduces specific risks you must understand before proceeding.

The project displays this important disclaimer:
- This wallet should be used for research purposes only.
- The wallet is a beta version with incomplete functionality and both known and unknown bugs.
- Do not use it with large amounts of ecash.
- The ecash stored in the wallet is issued by the mint
- you trust the mint to back it with bitcoin until you transfer your holdings to another bitcoin lightning wallet.
- The Cashu protocol that the wallet implements has not yet received extensive review or testing.

Treat Minibits like an everyday wallet, not a savings account, and never store significant value here.

## 1️⃣ Setting Up Your Wallet

To begin, visit the [Minibits Website](https://www.minibits.cash/) where you'll find download options for all major platforms. iOS users can download from the [App Store](https://testflight.apple.com/join/defJQgTD), while EU iOS users have the additional option of installing from [Freedom Store](https://freedomstore.io/). Android users can get the app from [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) or download the APK file directly from the [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) page.

When installing Minibits, you'll see introductory screens that explain the basic concepts—you can read through these or skip them if you're already familiar with the technology. Once you've completed these initial steps, you'll be prompted to choose between:
- `Got it, take me to the wallet` for new users or
- `Recover lost wallet` if you're restoring from a backup.

![image](assets/en/01.webp)
After completing the initial setup, you will land on the Home Screen, which has several important elements to note. ① The profile icon in the top corner takes you to your profile page where you can access your Minibits wallet address and select `batch receive` options. ② In the middle of the screen, you'll see the Mints you can use, with the Minibits mint selected by default. ③ The action row below provides options to send ecash or lightning payments, scan a QR code, and receive payments. ④ Finally, the bottom navigation bar contains shortcuts to the Home screen, Transaction History, Contacts, and Settings.

![image](assets/en/02.webp)

## 2️⃣ Manage mints

By default, the Minibits mint is enabled when you start the app. However, one of ecash's strengths is the ability to use multiple mints for increased decentralization and security. To add another mint, navigate to `Settings`, then select `Manage mints`, and finally tap `Add mint`.

[Bitcoinmints.com](Bitcoinmints.com) provides a comprehensive list of available mints with user ratings to help you choose reputable options. Using multiple mints reduces your risk. If one mint experiences issues, your funds on other mints remain accessible.

![image](assets/en/04.webp)

## 3️⃣ Creating a Backup

Backup is arguably the most critical step in the entire setup process. To access the Backup options, navigate to `Settings`-> `Backup` Here you'll find two essential options:
1. `Your seed phrase` which contains `12 words` that allows you to recover your ecash balance in case of device loss. This seed phrase is your master key to all ecash across all mints you've added. Write it down on physical medium (paper or metal) and store it securely in multiple locations. Never store your seed phrase digitally where it could be compromised. Consider visiting this [tutorial](https://planb.academy/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) for best practices for safeguarding your wallet.
2. `Wallet backup` which contains a long backup string.

**Attention**: You will still need your seed phrase when using this backup to recover your wallet.

![image](assets/en/05.webp)

## 4️⃣ Create Minibits wallet address

Next navigate to `Contacts` at the bottom and customize your dedicated `Minibits wallet address` by tapping `Change` -> `Change wallet address`. Enter your preferred address and check availability.

![image](assets/en/07.webp)

After setting your address, you'll be prompted for a small `Donation` to support the project. While this is optional, I strongly recommend considering it if you plan to use the service regularly. Open-source projects like Minibits rely on community support to continue development and maintenance. Even a small contribution helps to ensure the project's longevity.

![image](assets/en/08.webp)

## 5️⃣ Nostr Setup

If you want to tip people you follow on Nostr, you can `Add your npub key` by selecting `Contacts` and then `Public`. This connects your Minibits wallet to the Nostr social network, enabling seamless tipping.

You also have the option to `Use your own profile` by going to `Settings` and then `Privacy` to import your own Nostr address and key. However, be aware that doing this will stop your wallet from communicating with minibits.cash Nostr and LNURL address servers, which disables lightning address features for receiving zaps and payments.

![image](assets/en/09.webp)

## 6️⃣ Receive funds

To initially receive funds, you need to top up your wallet via a lightning invoice. This process is straightforward: tap on `Topup` , enter the `Amount` you want to add, optionally add a `Memo` , and then tap `Create invoice`. You'll then need to pay this invoice using another Lightning wallet, this converts Bitcoin Lightning payments into ecash tokens within your Minibits wallet.

![image](assets/en/10.webp)

## 7️⃣ Send funds

Now that you've funded your wallet, you can send funds in two different ways.

### Send ecash

The first option is to send ecash directly. Tap on `Send` , then select `Send ecash`, enter the `Amount` , and tap `Create token.` This will generate a QR code that you can share with the recipient or have them scan directly with their device. The recipient will see the tokens appear in their wallet almost instantly, with no blockchain fees or confirmation delays.

![image](assets/en/11.webp)

### Pay with Lightning

The second option is to pay via Lightning. Tap on `Send` , then select `Pay with Lightning`. You can choose from your Nostr `contacts`(if you've connected your npub), or enter/paste a Lightning address, invoice, or LNURL pay code using the `Paste` or `scan`option. After`Confirming`the recipient, you'll be prompted to enter the `Amount to Pay`, optionally add a memo, and then tap `Confirm` followed by `Pay now` to complete the Lightning transaction.

![image](assets/en/12.webp)

## 8️⃣ Create a NWC connection

Another powerful feature of Minibits is the ability to create `Nostr Wallet Connect (NWC)` connections, which allow other applications to request payments from your wallet without exposing your private keys.

To set this up, go to `Settings`, then select `Nostr Wallet Connect`, and tap `Add connection`. Name your connection something descriptive to identify both the application and associated user account. Set a reasonable maximal daily limit to control how much can be spent through this connection, then tap `Save` to complete the setup.

This feature is particularly useful for services like Nostr Clients where you want to enable automatic tipping without manually approving each transaction.

![image](assets/en/12.webp)

## 🎯 Conclusion

Minibits provides an accessible entry point into the world of ecash, offering privacy-focused payments that complement your Bitcoin holdings. Remember to always maintain proper backups, consider using multiple mints for redundancy, and only store appropriate amounts in this custodial solution.

For additional resources, check out the Minibits GitHub repository, the official website, and their Telegram channel where the community actively discusses developments and troubleshoots issues
- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Website](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)

The ecash ecosystem is still evolving, but tools like Minibits are making this powerful privacy technology increasingly accessible to everyday users.
