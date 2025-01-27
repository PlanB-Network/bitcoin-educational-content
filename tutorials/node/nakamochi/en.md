---
name: Nakamochi
description: Node Running Made Easy - How to set up and use Nakamochi Bitcoin and Lightning node.
---

Running your own Bitcoin and Lightning full node no longer needs to be a complex task limited to technical experts. Traditionally, setting up and managing nodes has demanded in-depth knowledge of cryptography, networking, and software development. Nakamochi changes that by making nodes accessible to everyone, regardless of technical background.

With Nakamochi, anyone can set up and operate a node from home, enabling full privacy and financial independence. Running a full node not only secures your own transactions but also contributes to the Bitcoin network’s strength. A decentralized and resilient Bitcoin network relies on a wide distribution of nodes to ensure its security and independence.

### Table of Contents

- What is Nakamochi and How Does It Work?
- Setting up Nakamochi
- About the Lightning Network
- Opening Channels and Making Transactions in the Lightning Network



## What is Nakamochi and How Does It Work?

Nakamochi is a Bitcoin-only full node that supports both the Bitcoin and Lightning networks. It includes an integrated Bitcoin and Lightning wallet, enabling users to run a secure, self-sovereign Bitcoin node while benefiting from the Lightning Network’s speed and low transaction costs.

Your Nakamochi node is managed via a mobile app, [BitBanana (Android)](https://bitbanana.app) and [Zeus (iOS)](https://bitbanana.app), allowing you to control it conveniently from anywhere. These apps act as a remote control for your node, enabling you to pay directly with Bitcoin or Lightning, manage transactions, open or close channels, check balances, and monitor your node’s performance, all with ease.


## Setting up Nakamochi takes just 5 minutes

### Step 1: Plug in and Get Started

1. Connect Nakamochi to power and Wi-Fi.
2. Click on **"Setup New Wallet"** and securely store your 24-word recovery phrase.
3. Use a node management app (Zeus or BitBanana) to connect to your Nakamochi:
   - Open the app and scan the QR code displayed on your Nakamochi.
4. For added security, set a PIN code on your device.

![Connect to power and write down your 24-word seed phrase](assets/en/01.webp)

![Wait until the Blockchain has caught up](assets/en/02.webp)

![Set up new wallet in Lightning Tab](assets/en/03.webp)

![Scan QR Code with Node Management App](assets/en/04.webp)

![For additional safety set a PIN code](asset/en/05.webp)

_Note: Allow your Nakamochi node to sync with the blockchain. This process may take some time depending on your internet connection._



## About the Lightning Network

The Bitcoin Lightning Network revolutionizes Bitcoin transactions by making them faster, cheaper, and more efficient. It’s perfect for everyday use, enabling near-instant payments with minimal fees, ideal for microtransactions like buying a coffee or handling frequent small purchases.
By operating off-chain, Lightning is designed to scale, supporting thousands of transactions per second without overloading the main Bitcoin blockchain. This makes it a key player in Bitcoin’s evolution into a practical, global payment system.
Privacy is another advantage, as transactions on Lightning are routed through private payment channels rather than being recorded directly on the blockchain. This ensures a more discreet way to transact while maintaining Bitcoin’s robust security.



#### Payment Channels Explained

The Lightning Network operates through payment channels, which are connections between two parties allowing multiple transactions without interacting directly with the blockchain. When a channel is open, the balance between the two parties is updated on this second-layer Lightning solution for every transaction, ensuring fast, low-cost payments. Only the channel's opening and closing are recorded on-chain, reducing congestion on the Bitcoin blockchain.This design ensures scalability and privacy, as individual transactions remain unrecorded on the public ledger.

**Example:** Alice and Bob open a channel by committing Bitcoin to it. Alice sends Bitcoins to Bob, and their off-chain balances update instantly without an on-chain record. If Alice then pays Charlie, and Alice has no direct channel to Charlie, the payment can be routed through Bob’s channel to reach Charlie. Routing through intermediary nodes ensures payments even without direct connections, making the network highly efficient.



## Opening Channels and Making Transactions in the Lightning Network

Once your Nakamochi is set up and connected to a node management app, you can begin using the Lightning Network by opening channels and making transactions.

### Opening Channels on Zeus (iOS):

1. Go to the **“Channels”** tab (bottom menu).
2. Click on the **“+”** to open a new channel.
3. Scan or enter the pubkey of the node you want to connect with.
4. Enter the locked amount (choose with your peer or use the minimum fixed amount for well-known nodes).
5. Click on **“Open Channel”**.

![ZEUS Screenshot](asset/en/06.webp)


For more information: [Channels | Zeus Documentation](https://zeusln.app)

### Opening Channels on BitBanana (Android):

1. Open the hamburger menu (left).
2. Go to **“Channels”**.
3. Click on the **“+”** to add/open a new channel.
4. Scan or paste the pubkey.
5. Enter the locked amount (choose with your peer or use the minimum fixed amount for well-known nodes).

![Bitbanana Screenshot](asset/en/07.webp)

For more information: [BitBanana](https://bitbanana.com)

Once your channel is open, payments can be routed through it to other participants in the network. Balances adjust off-chain, ensuring transactions are nearly instant and incur minimal fees.
If you no longer need a channel, you can close it. This action settles the final balance between you and your peer and records it on-chain. Ideally both parties agree and are online for a “cooperative close” (faster and less fees vs. a “forced close” with an unresponsive/offline peer).
Generally, we recommend leaving channels open to reduce costs and increase network reliability and efficiency. By keeping channels open, you minimize on-chain transaction fees, avoid downtime for channel reconnections, and maintain a stable routing capacity for seamless payment processing. This approach fosters a robust and resilient network while enhancing overall user experience and reducing operational overhead.



### Useful Links

- [About Nakamochi](https://nakamochi.io/)
- [Subscribe to Our Newsletter](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)
