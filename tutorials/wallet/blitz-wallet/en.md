---
name: Blitz Wallet
description: The simplest Bitcoin wallet.
---

![cover](assets/cover.webp)

User experience is one of the deciding factors when choosing a Bitcoin wallet. In this tutorial, we introduce you to Blitz Wallet, a wallet that places simplicity at the core of its approach: thanks to the integration of the **Spark** protocol, Blitz offers you one of the simplest and most comprehensive Bitcoin wallets on the market, with instant payments and no technical management.

## What is Blitz Wallet?

Blitz Wallet is a **self-custodial** and **open source** Bitcoin wallet that focuses on your sovereignty and a smooth, intuitive user experience.

[Blitz Wallet](https://blitz-wallet.com/) is a mobile application available on Android (Play Store) and iOS (App Store).

Unlike traditional Lightning wallets that require managing payment channels and inbound liquidity, Blitz Wallet relies on the **Spark protocol** to eliminate these technical complexities. The result: instant payments from the very first satoshi received, with no prior configuration needed. Blitz's goal is to make bitcoin payments as simple as a standard payment app, without ever compromising the self-custody of your funds.

Blitz Wallet also supports **human-readable addresses** in the `user@domain.com` format (via LNURL), making it possible to send bitcoins as easily as an email, without having to handle long invoices or QR codes for each transaction.

## Understanding the Spark Protocol

Before getting into the practical steps, it is helpful to understand the technology that powers Blitz Wallet under the hood: the **Spark protocol**.

### What is Spark?

Spark is an open source overlay protocol built on Bitcoin, developed by the Lightspark team. It enables instant, low-cost transactions while preserving the self-custody of your bitcoins.

Unlike the Lightning Network, which relies on **payment channels** between two parties, Spark uses a technology called **statechain**. The fundamental principle is as follows: instead of moving bitcoins on the blockchain with each transaction, Spark transfers the **spending right** from one user to another, without any on-chain movement.

### How does it work?

To understand Spark intuitively, imagine that spending a bitcoin on Spark requires completing a two-piece puzzle:
- One piece is held by the user (for example, Alice).
- The other piece is held by a group of operators called the **Spark Entity (SE)**.

Only the combination of the two matching pieces allows the bitcoins to be spent.

When Alice wants to send her bitcoins to Bob, here is what happens: a new puzzle is jointly created between Bob and the SE. The puzzle keeps the same shape, but the pieces that make it up change. Now it is Bob's piece that matches the SE's piece. Alice's old piece becomes unusable because the SE has destroyed its corresponding piece. Ownership of the bitcoins has changed hands, **without any transaction on the blockchain**.

Bob can then repeat the same process to send these bitcoins to Carol, and so on. Each transfer works by replacing the puzzle pieces, not by moving funds on-chain.

### Why is it secure?

A legitimate question arises: what happens if the SE does not actually destroy its old piece?

The Spark Entity is not a single entity: it is a group of independent operators. The SE's piece is never held by a single operator. Replacing the puzzle requires the cooperation of multiple operators. It only takes **one honest operator** during a transfer to prevent the reactivation of an old puzzle. No single operator can secretly keep an old puzzle active or recreate it later.

Additionally, Spark includes a unilateral exit mechanism: you can always recover your bitcoins on-chain without the cooperation of the SE. This fallback mechanism is an integral part of Spark's architecture and ensures that you are never dependent on the network to access your funds.

### Spark vs Lightning Network

Spark and Lightning are not in competition: they are **complementary**. Blitz Wallet integrates both, allowing you to benefit from the advantages of each.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Technology**                | Statechains                  | Payment channels      |
| **Channel management**        | Not required                 | Required              |
| **Inbound liquidity**         | Not required                 | Required              |
| **Instant transactions**      | Yes                          | Yes                   |
| **Self-custody**              | Yes                          | Yes                   |
| **Lightning compatibility**   | Yes (via atomic swaps)       | Native                |

The Lightning Network remains an excellent protocol for instant payments, but it imposes technical constraints (channel management, inbound liquidity, online node...) that can deter beginners. Spark removes these constraints while remaining compatible with Lightning.

## Installation and Setup

In this tutorial, we use the Android version of Blitz Wallet, but all the processes presented below are also valid on iOS.

![installation](assets/fr/01.webp)

Since Blitz Wallet is a self-custody wallet, you have the choice between **creating a new wallet** or **importing a recovery phrase** (12 or 24 words) from an existing wallet.

Here, we will create a new wallet. Below you will find our recommendations on backing up your recovery phrase:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **IMPORTANT**: These 12 or 24 recovery words are **the only key to access your bitcoins**. Blitz is a self-custodial wallet: neither Blitz nor Spark have access to your recovery phrase or your funds. If you lose these words, you will permanently lose access to your bitcoins. Do not share them with anyone: whoever possesses them can spend your bitcoins.

Then create a **PIN code** to secure access to your wallet.

![setup-wallet](assets/fr/02.webp)

## Getting Started with Blitz

Making transactions with Blitz is more intuitive than with most other Bitcoin wallets. The interface is minimalist and centered around three main actions: send, scan, and receive.

### Receiving bitcoins

To receive bitcoins on your Blitz wallet, tap the **"Down arrow"** icon (↓), enter the amount in satoshis that you wish to receive, add an optional description, and the wallet will generate an invoice that you can share with your sender.

⚠️ **NOTE**: The satoshi (or "sat") is the smallest unit of bitcoin: **1 bitcoin = 100,000,000 satoshis**.

One of the distinctive features of Blitz Wallet is that it supports multiple networks and protocols within the Bitcoin ecosystem:

- **Lightning Network**: One of Bitcoin's overlay layers that enables instant micropayments with very low fees. Ideal for small everyday amounts.

- **Bitcoin (on-chain)**: The main blockchain of the Bitcoin protocol, suited for larger transaction amounts where maximum security and finality are the priority.

- **Liquid Network**: A sidechain of Bitcoin developed by Blockstream, which enables fast and confidential transactions using Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

By default, Blitz generates a Lightning invoice, but you can choose the network on which you want to receive your satoshis by tapping the **"Choose format"** button.

![receive-sats](assets/fr/03.webp)

### Creating contacts

Blitz Wallet simplifies recurring bitcoin payments through its contact system.

In the **Contacts** menu, you can save Blitz usernames or Lightning addresses (LNURL) that you interact with frequently.

You can then send satoshis to these addresses in just a few taps, without having to scan a QR code or manually enter an address each time.

### Sending bitcoins

In addition to the standard methods for sending bitcoin (QR code scan, manual address entry), Blitz offers several convenient options:

- **From Image**: Import a QR code from your photo gallery.
- **From Clipboard**: Paste a previously copied address or invoice.
- **Manual Input**: Directly enter a Bitcoin address, a Lightning invoice, or a human-readable address (for example `user@walletofsatoshi.com`).
- **From your contacts**: Select a pre-saved recipient to send in just a few taps.

In the **Wallet** menu, tap the **"Up arrow"** button (↑), choose your sending method, enter the amount to send, add a description, and confirm the transaction.

The minimum amount for sending is currently **1,000 satoshis**.

![send-bitcoin](assets/fr/05.webp)

## The Blitz Store

Beyond bitcoin transfer operations, Blitz Wallet includes a store where you can spend your bitcoins to purchase digital services directly from the app.

From the main menu, tap the **Store** tab to access the store. You will also find access to the **Bitrefill** platform, which lets you buy gift cards from thousands of merchants around the world, directly with bitcoin.

- **Artificial Intelligence**: Access the latest generative AI models (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) and pay for your credits directly in satoshis. Several plans are available to suit your needs (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonymous SMS**: Send and receive SMS anywhere in the world without revealing your personal phone number. The service is billed in satoshis for each message sent.

![sms-credit](assets/fr/07.webp)

- **WireGuard VPN**: Protect your online privacy by subscribing to a WireGuard VPN plan (weekly, monthly, or quarterly), payable in bitcoin directly from the Blitz store. You simply need to download the WireGuard client app on your device to get started.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet Behind the Scenes: Going Further

Behind Blitz Wallet's ease of use lies a well-designed technical architecture that combines multiple layers of the Bitcoin ecosystem.

### Your Balance Breakdown

Blitz Wallet manages your balance transparently by distributing your funds across different protocols based on needs. When your balance is below 500,000 satoshis, Blitz uses the **Liquid Network** and atomic swaps to provide you with a smooth experience and enable Lightning Network transactions even with small amounts.

This approach ensures a simple onboarding for new users, without them needing to understand the underlying mechanisms. You can view the breakdown of your balance across the different layers in the **Settings > Balance Info** menu.

![balance](assets/fr/09.webp)

### Lightning Mode (optional)

By default, Blitz Wallet uses the Liquid Network and the Spark protocol to provide you with a smooth experience without any technical configuration. However, Blitz gives you the option to enable **Lightning mode**, which will automatically open a payment channel when you reach a balance of **500,000 satoshis** (0.005 BTC).

To enable Lightning mode, go to **Settings**, then in the **Technical Settings** section, tap the **Node Info** option.

![enable-lightning](assets/fr/10.webp)

Thanks to the Spark protocol, this activation is **optional**: Spark already allows you to make Lightning-compatible payments without needing to open a channel or manage inbound liquidity. Native Lightning mode remains useful for advanced users who want to have their own Lightning node integrated within the app.

### Point of Sale (PoS)

Blitz Wallet includes a **point of sale** feature that allows merchants to accept bitcoin payments directly from the app.

In the **Settings > Point-of-sale** menu, you can configure:

- Your store's unique identifier
- The local fiat currency in which to display prices
- Instructions for your employees
- The tipping option for your customers

Your customers simply need to scan the generated QR code to make their bitcoin payment instantly.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Resources used to write this tutorial:
- [Breez](https://breez.technology/) Technology blog: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
