---
name: KaleidoSwap
description: Advanced guide to RGB asset trading on Lightning Network with KaleidoSwap
---

![cover](assets/cover.webp)

KaleidoSwap is a sophisticated open-source desktop application that bridges the gap between the RGB Protocol and the Lightning Network. It serves as a comprehensive interface for managing RGB Lightning Nodes, interacting with RGB Lightning Service Providers (LSPs) via the LSPS1 specification, and executing atomic swaps of RGB assets.

As a non-custodial solution, KaleidoSwap empowers users to maintain full control over their keys and data. By leveraging the client-side validation paradigm of RGB, it enables private and scalable smart contracts on top of Bitcoin. This tutorial dives into the advanced features of KaleidoSwap, guiding you through the intricacies of "Colored" UTXO management, channel liquidity for specific assets, and the taker-maker trading model, ensuring you can fully utilize this powerful decentralized exchange protocol.

## Installation

KaleidoSwap provides pre-built binaries for major operating systems, but for advanced users, building from source ensures you are running the latest code with your specific configurations.

### Download Binaries

You can download the latest release for your operating system from the [official website](https://kaleidoswap.com/) or the [GitHub releases page](https://github.com/kaleidoswap/desktop-app/releases).

### Installation Methods

1.  **Windows**: Download the `.exe` installer and run it.
2.  **macOS**: Download the `.dmg` file, open it, and drag KaleidoSwap to your Applications folder.
3.  **Linux**: Download the `.AppImage` or `.deb` file and install/run it.


## Node Setup Options

When you first launch KaleidoSwap, you will be presented with the **Connection Screen**. This is the first step in configuring your environment.

![Node Selection Screen](assets/en/01.webp)

You must choose how to connect to the RGB Lightning Network. This choice impacts your level of control and privacy.

### Option 1: Local Node (Recommended for Self-Custody)

**For complete control and privacy**, run a node directly on your machine, see the advantages below:
- **Self-Custodial**: You hold the keys. No third party can freeze your funds or censor your transactions.
- **Privacy**: Your data stays on your device.
- **Independence**: No reliance on external service providers.

If you select **Local Node**, you will be taken to the setup screen where you can create a new wallet or restore an existing one.

![Local Node Setup Screen](assets/en/02.webp)

### Option 2: Remote Node

Connect to a remote RGB Lightning Node (self-hosted on a VPS or a hosted provider).
- **Advantages**: No local resource usage, 24/7 availability.
- **Trade-off**: Requires trusting the host or managing a remote server.

![Remote Node Setup Screen](assets/en/03.webp)

**KaleidoSwap is designed to empower self-custody.** We strongly recommend running your own node—either locally (Option 1) or by self-hosting a remote node—to fully leverage the censorship-resistant properties of Bitcoin and RGB.

## Creating a Wallet

KaleidoSwap manages both Bitcoin and RGB assets. The wallet creation process initializes a keystore that secures your on-chain funds and your Lightning channel states.

Here's the detailed process:
1. Open KaleidoSwap and select **Local Node**.
2. Click on **Create New Wallet**.
3. **Account Setup**: Enter an **Account Name** and select the **Network** (e.g., Bitcoin Mainnet, Testnet, Signet).
4. **Advanced Configuration** (Optional): If you are a power user, you can configure custom RPC endpoints, Indexer URLs, or Proxy settings under "Advanced Settings".
5. Click **Continue**.
6. **Password**: Set a strong password to encrypt your wallet file locally.
7. **Recovery Phrase**: Write down your seed phrase and store it securely.
    - **Critical**: This phrase is needed to recover your on-chain funds and node identity.
    - **Warning**: **Lightning channel states cannot be fully recovered from the seed alone**. You must also maintain Static Channel Backups (SCB) to recover funds locked in channels.

![Wallet Creation Screen](assets/en/04.webp)


## Dashboard Overview

Once your wallet is created, you will be directed to the main **Dashboard**.

![KaleidoSwap Dashboard](assets/en/05.webp)

_Note: The screenshot above shows a wallet that has already been funded and has active channels. A fresh wallet will show zero balances and no active channels until you fund it._

## Funding Your Wallet

To operate with RGB assets, you need to fund your wallet. KaleidoSwap supports depositing both Bitcoin and RGB assets via on-chain transactions or the Lightning Network.

### Depositing Bitcoin

1. Click **Deposit** in the Quick Actions menu.
2. Select **BTC** from the asset list.

![Select BTC Asset](assets/en/06.webp)

3. Choose your deposit method: **On-chain** or **Lightning**.

![BTC Deposit Options](assets/en/07.webp)

- **On-chain**: Scan the QR code or copy the address to send Bitcoin from another wallet.
- **Lightning**: Generate an invoice for the desired amount.

![BTC On-chain Deposit](assets/en/08.webp)

### Depositing RGB Assets & Colored UTXOs

To receive RGB assets (like USDT), you need specific UTXOs available to be "colored" (assigned an asset).

1. Click **Deposit** and select the RGB asset (e.g., USDT). **Important**: If this is the **first time** your node is receiving this specific asset, **leave the Asset ID field empty**. Entering an ID for an unknown asset will cause the node to return an error as it doesn't recognize it yet.
2. Choose **On-chain** or **Lightning**.

![USDT Deposit Options](assets/en/09.webp)

#### On-chain Receive Modes: Witness vs. Blinded

When receiving RGB assets on-chain, you have two privacy modes:

- **Blinded Receive (Recommended for Privacy)**: You provide a "blinded" UTXO to the sender. You are asking the sender to send assets to an existing UTXO that you own, but you obfuscate the actual UTXO identifier. This offers better privacy.
- **Witness Receive**: You provide a standard Bitcoin address. You are asking the sender to create a *new* UTXO for you by sending the assets to that address. This allows the RGB assets to be attached directly to the new UTXO created by the transaction.

#### Lightning Deposit

For Lightning deposits, simply generate an invoice. The RGB asset will be routed to you through your open channels.

![USDT Lightning Invoice](assets/en/10.webp)


## Opening Channels with RGB Assets

To route RGB assets over the Lightning Network, you need a channel with sufficient liquidity and asset allocation. The easiest way to get started is to **Buy a Channel** from an LSP (Lightning Service Provider).

### Buying a Channel from Kaleido LSP

1. Go to the **Channels** tab. You will see options to "Open Channel" (manual) or "Buy Channel" (LSP).
2. Click **Buy Channel**.

![Channels Dashboard](assets/en/11.webp)

3. **Connect to LSP**: The app will connect to the default Kaleido LSP. This provider offers inbound liquidity and supports RGB asset routing.

![Connect to LSP](assets/en/12.webp)

4. **Configure Channel**:
    - **Capacity**: Select the total Bitcoin capacity for the channel.
    - **RGB Allocation**: Choose the RGB asset (e.g., USDT) you want to be able to receive or send. The LSP will ensure the channel is configured to support this asset.

![Configure Channel](assets/en/13.webp)

    -  **RGB Allocation**: Choose the RGB asset (e.g., USDT) you want to be able to receive or send. The LSP will ensure the channel is configured to support this asset.

![RGB Allocation](assets/en/14.webp)

5.  **Payment**: You must pay a fee to the LSP for opening the channel and providing liquidity. You can pay using **Lightning** or **On-chain** Bitcoin. The payment can be made from your internal KaleidoSwap wallet or an external wallet.

![Complete Payment](assets/en/15.webp)

6. Once payment is confirmed, the LSP will initiate the channel opening transaction. You will see an **Order Completed** screen.

![Order Completed](assets/en/16.webp)

7. After confirmation on the blockchain, your channel will be active and ready for RGB transfers.


## Trading: Taker-Maker Model

KaleidoSwap's trading engine operates on a **Taker-Maker model**. You can swap assets manually with a peer or use an Market Maker (LSP).

### Swapping with a Market Maker (LSP)

This is the most common way to trade. You act as the **Taker**, executing orders against the available liquidity provided by the LSP (**Maker**).

1. Navigate to the **Trade** tab and select **Market Maker**.
2. **Enter Amount**: Input the amount of Bitcoin you want to send (or the asset you want to receive). The interface will show the estimated exchange rate and fees.

![Market Maker Swap](assets/en/17.webp)

3. **Confirm Swap**: Review the details, including the exchange rate and the exact amount you will receive. Click **Confirm Swap**.

![Confirm Swap](assets/en/18.webp)

4. **Processing**: The swap is executed atomically on the Lightning Network. You will see a status screen indicating the swap is pending.

![Swap Pending](assets/en/19.webp)

5. **Success**: Once the HTLCs are settled, the swap is complete, and the assets are in your channel.

![Swap Success](assets/en/20.webp)


## Developer API

For developers building on top of KaleidoSwap, the application exposes an API that supports:

- **RGB LSPS1**: For automated liquidity services.
- **Swap API**: For programmatic trading and market making.
- **WebSocket**: For real-time market data subscriptions.

Refer to the [API Documentation](https://docs.kaleidoswap.com/api/introduction) for full endpoints and specifications.

## Conclusion

KaleidoSwap empowers you to leverage the privacy and scalability of RGB assets on the Lightning Network. By understanding Colored UTXOs and channel asset allocation, you can fully utilize this powerful decentralized exchange protocol.
