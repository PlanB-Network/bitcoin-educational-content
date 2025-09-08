---
name: Bull Bitcoin Wallet
description: Find out how to use the Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


This guide takes you through the installation, configuration and use of Bull Bitcoin Mobile. You'll learn how to receive and send funds on the three networks: onchain, Liquid and Lightning, and how to transfer your Bitcoin from one network to another. Appendices provide resources and contacts, background information and brief explanations of technical concepts.


## Introduction


**Bull Bitcoin Mobile**, developed by **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel)), is a **self-custodial** Bitcoin wallet, which means you have full control over your private keys and therefore your funds, without depending on a third party. Open-source and rooted in a Cypherpunk philosophy, this Wallet combines simplicity, confidentiality and advanced features such as cross-network swaps and PayJoin support. It lets you manage your bitcoins on three networks: **Bitcoin onchain**, **Liquid** and **Lightning**, each tailored to specific uses.


### Development context


Wallet responds to a major challenge: Bitcoin network charges are unsuitable for small payments, or for opening small self-hosted Lightning channels. The Wallet Bull Bitcoin Mobile offers a self-custodial solution while relying on the 3 major Bitcoin networks:



- Bitcoin network (onchain)**: Ideal for medium- to long-term storage of UTXOs and large-value transactions, where fees are proportionally negligible.
- Liquid network**: Designed for fast (~2 minutes), more confidential (hidden amounts), low-cost transactions, perfect for accumulating small amounts or protecting your privacy.
- Lightning** network: Optimized for instant, low-cost payments, suitable for small- to medium-value daily transactions.


With Bull Bitcoin Mobile, for example, you can accumulate small amounts in the **Liquid** or **Lightning** portfolios and then, once you have reached a significant amount, you can :



- Transfer to the onchain network for secure medium- or long-term storage, having improved confidentiality with Liquid and/or Lightning upstream, and with onchain fees for a single transaction


### Continuous evolution


Wallet is constantly evolving, so don't be surprised if you find discrepancies between this tutorial and your up-to-date application.


- For example, as of 07/19/2025, the **"Buy / Sell / Pay "** buttons are visible but grayed out in the application, as these options, available on Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), will soon be integrated for a unified experience. Their use will remain entirely optional. Many other developments are underway or planned: multi-wallet management, passphrase, compatibility with hardware wallets...
- On the [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), you can check out current topics and upcoming developments. As the project is 100% open-source and "built in public", you can also send us your suggestions and any bugs you encounter.



## 1. Prerequisites


Before you start using **Bull Bitcoin Mobile**, make sure you have the following items:



- Compatible Smartphone**: A **iOS** (iPhone or iPad) or **Android** device
- Internet connection
- Secure backup media**: Write down your **recovery phrase** (12 words) on paper or metal and store it in a safe place.
- Basic knowledge**: A minimum understanding of Bitcoin concepts (addresses, transactions, fees) is useful, although this tutorial explains each step for beginners.


## 2. Installation



- Download the application** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Download from the application store for Android devices
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Download the APK for Android devices directly**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Download via TestFlight for Apple devices
 - Check the developer's name (Bull Bitcoin) to avoid fraudulent applications.
 - Make sure that the downloaded version corresponds to the latest stable version indicated on GitHub.
 - Bull Bitcoin Mobile is **open-source**. To view the code: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)



- Install the application



## 3. Initial configuration


### 3.1 Launch the application :


The application uses a unique 12-word recovery phrase for both portfolios:


 - secure Bitcoin' Wallet**: For transactions on the Bitcoin network (onchain)
 - instant Payments' Wallet**: For instant transactions on Liquid and Lightning networks


On opening, you are prompted to import an existing recovery phrase, or to create a new Wallet :


![image](assets/fr/02.webp)


### 3.2 Recovery phrase :


If you wish to re-use an existing Wallet, click on "**Recover Wallet**" and fill in the 12 words of your recovery phrase.


Otherwise, click on "**Create New Wallet**" :


- Write down your recovery phrase with the utmost care. Write it down on paper or metal and keep it in a safe place (safe deposit box, offline location). This phrase is your only means of accessing your bitcoins in the event of loss of your device or deletion of the application.
- It's also important to note that anyone with this phrase can steal all your bitcoins. Never store it digitally:
 - No screenshot
 - No cloud, email or messaging backups
 - No copy/paste (risk of saving to clipboard)


**! This point is critical**. For further assistance :


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Securing access :



- Go to settings then click on **PIN Code**.
- Set up a robust **PIN code** to protect access to the application.
- This step is optional, but strongly recommended to prevent anyone with access to your phone from gaining access to your Wallet.


![image](assets/fr/03.webp)


### 3.4 Connection to a personal node (optional):


The Wallet BullBitcoin connects to Electrum servers by default: the first managed by Bull Bitcoin and a secondary server from Blockstream, both of which are considered to keep no logs, reducing the risk of tracking.


For greater confidentiality, you can connect the application to your own Bitcoin node via an Electrum server (instructions available on [BullBitcoin's GitHub](https://github.com/orgs/SatoshiPortal/projects/49) ).



## 4. Receiving funds


Receiving funds with **Bull Bitcoin Mobile** is simple and tailored to your needs, whether you use :


  - the **Bitcoin (onchain)** network for long-term conservation,
  - the **Liquid** network for fast, more confidential transactions,
  - the **Lightning** network for instant, low-value payments.


The application automatically generates Lightning reception or invoice addresses, depending on the network selected. Here's how to proceed for each network.


### 4.1. onchain (Bitcoin network)


On the Home screen, you can :


- or select the **Secure Bitcoin Wallet** then click on "**Receive "** :


![image](assets/fr/04.webp)



- or click on "**Receive "**, and then choose the **Bitcoin** network:


![image](assets/fr/05.webp)


#### 4.1.1. Copy or scan Address only" option disabled (default)


![image](assets/fr/06.webp)



- This gives access to optional advanced parameters. You can specify :
 - An **amount** in BTC, Sats or fiat.
 - A **personal note** to be included in the copy of the URI / QR Code.
 - Activation of **PayJoin** (see Appendix 3 for details), which improves confidentiality by combining sender and recipient entries.



- Example of an automatically generated URI** :


```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```



- Usage**: Copy the URI to share with the sender, or let him scan the QR code.


#### 4.1.2. Copy or scan Address only" option enabled


![image](assets/fr/07.webp)



- With the **"Copy or scan Address only "** option enabled, the application generates a simple Bitcoin address in SegWit (bech32) format.



- Example:


```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```


Even if you enter an amount or a note, they will not be included in the QR code or in the copy of the address



- Usage**: Copy the address to share it with the sender, or let him scan the QR code.


#### 4.1.3. Generating a new address



- Why use a new address for each transaction? This **protects your privacy** by preventing multiple payments from being linked to the same address, and limits the possibilities of tracking on the Blockchain.
 - By default, Bull Bitcoin automatically generates an unused address.**
 - You can force the creation of a new address by clicking on **"New Address"** at the bottom of the screen.
 - All your addresses are linked to your seed phrase: no matter how many addresses you use, your portfolio will display a single balance, and can automatically consolidate funds when a shipment is made.



- Tip: Always use the new address** provided by Bull Bitcoin, unless you have a specific need (e.g. a public address to receive donations).


### 4.2. Liquid


On the Home screen, you can :


- or select the **Instant payments Wallet** then click on **"Receive "** then **"Liquid"** :


![image](assets/fr/08.webp)



- or click on "**Receive "**, and then choose the **Liquid** network:


![image](assets/fr/09.webp)


Once you are on the **"Receive "** screen, copy a Liquid address:



- No amount or note. Example:


```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



- Or by specifying a **amount** (in BTC, Sats or fiat) and/or a **personal note** to be included in the copy of the URI / QR Code. Example:


```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


**Use**: Copy the address/URI to share with the sender, or let him scan the QR code.


### 4.3. Lightning


On the Home screen, you can :


- or select the **Instant payments Wallet** then click on "**Receive "** :


![image](assets/fr/10.webp)



- or click on "**Receive "**, and then choose the **Lightning** network:


![image](assets/fr/11.webp)


#### 4.3.1. Operation, limits and benefits



- Mechanism**: Bull Bitcoin Wallet is a wallet that enables payments to be made and received via Lightning. Funds received via Lightning are stored on the **Liquid** network (in the Wallet Instant Payments) thanks to an automatic swap via **Boltz**. This gives you the ability to interact with Lightning without having to manage liquidity channels, while remaining in self-custody.



- Limits:**
 - A minimum amount** of 100 satoshis (as of 07/19/2025) when you generate the invoice.
 - You pay the costs**, which will be deducted from the amount sent by the sender, unlike receiving with Wallet Lightning native, where only the sender pays the transfer costs in addition to the amount sent. As at 19/07/2025, 47 Sats are deducted from the amount sent.



- Benefits** :
 - Self-custodial**: Your funds remain under your control, stored on the Liquid network.
 - No high onchain fees**: Storage on Liquid avoids costly onchain deposits to open your Lightning channel or add liquidity. These operations can be carried out later, when the amount accumulated on Liquid justifies the fees.



- Tip:** If the sender has Wallet Bull Bitcoin, use the Liquid network directly to avoid swap fees


#### 4.3.2. Generate invoice



- Enter a **amount** (in BTC, Sats or fiat)



- Add a **personal note** which will be integrated into the invoice. If the sender pays the invoice, your Wallet will also include it in the transaction details.



- Invoice validity:** The Lightning invoice is valid for **12 hours**. After this time, it expires and can no longer be paid. A new invoice must be generated.



- Usage**: Copy the invoice to share it with the sender, or let him scan the QR code.



## 5. Sending funds


### 5.1. Basic principle


Either from the home page, or from wallets :


![image](assets/fr/12.webp)


to access the send screen:


![image](assets/fr/13.webp)


**Bull Bitcoin Mobile** makes sending money easy by automatically detecting the network (Bitcoin, Liquid, or Lightning) based on the address or invoice entered (copied or scanned via QR code).


### 5.2. onchain transmission (Bitcoin network)


#### 5.2.1. Send screen


**Action**: Enter or scan a Bitcoin onchain address



- If the amount has not been defined, for example :


```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



- Then you can choose on the send screen :
 - Amount in BTC, sat or fiat. Minimum amount: 546 satoshis on 22/07/2025.
 - An optional note to identify the transaction. Only visible to you, in the transaction details.


![image](assets/fr/14.webp)



- If the amount has already been defined, for example :


```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```


You will then be taken directly to the confirmation screen below.


#### 5.2.2 Confirmation screen


Take the time to check all the parameters, especially the amount, destination address and fees.

Then you can adjust the parameters:


![image](assets/fr/15.webp)


- Fees**: You can choose :
  - Either the execution speed** of your transaction, and the associated fees will be estimated
  - Either the fees**, in Absolute fees (total fees in satoshis) or Relative fees (fees per byte) mode, and the speed of your transaction will be estimated



- Advanced settings** :



 - Replace-by-fee (RBF)** : Activated by default, this function speeds up the transaction by paying a higher fee (see Appendix 4 for details).



 - Manual selection of UTXO**: If your funds are stored at several different Wallet addresses, you can select the addresses from which to send the funds. Why should you do this? With the increasing adoption of Bitcoin, transfer fees are rising. Sending from several addresses with small amounts is more expensive than sending from a single address, but doing it now avoids having to do it later, when fees will be even higher. This is called **consolidation of UTXO.**


![image](assets/fr/16.webp)



- Sending with PayJoin**: If the function has been activated by the recipient who supplied the URI, e.g. :


```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```


Then Bull Bitcoin Mobile will configure the sending by combining your UTXOs with the recipient's UTXOs as input, improving confidentiality (see Appendix 3 for details).


### 5.3. Send to Liquid


#### 5.3.1 Send screen


The **Liquid** network enables fast transactions (~2 minutes thanks to one block per minute), more confidential (masked amounts) than on the onchain network, and with very low fees. Funds are withdrawn from **Instant Payments Wallet**.


**Action**: Enter or scan a Liquid address



- If the amount has not been defined, for example :


```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```


Then you can choose on the send screen :


- Amount in BTC, sat or fiat. No minimum, 1 Satoshi possible;
- An optional note to identify the transaction. Only visible to you, in the transaction details.


![image](assets/fr/17.webp)



- If the amount has already been defined, for example :


```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


You will then be taken directly to the confirmation screen below.


#### 5.3.2 Confirmation screen


Take the time to check all the parameters, especially the amount and destination address.


![image](assets/fr/18.webp)



- Fees**: Proportional to the complexity of the transaction, generally on a 0.1 sat/vB basis, i.e. 20-40 satoshis for a simple transaction (33 Sats at 07/22/2025).


### 5.4. Send to Lightning


#### 5.4.1 Send screen


The **Lightning** network enables instant, low-cost payments for small amounts, ideal for small daily transactions.


**Action**: Enter or scan a Lightning invoice



- If you scan a LN-URL address that lets you set the amount

Example: `orangepeel@walletofsatoshi.com`.

then you can choose on the send screen :


 - Amount in BTC, sat or fiat. Minimum amount of 1000 satoshis on 23/07/2025
 - An optional note to identify the transaction. It will be sent to the recipient.


![image](assets/fr/19.webp)



- If you scan a Lightning invoice that contains a defined amount

Example:


```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```


You will then be taken directly to the confirmation screen below.


Note: amount must be greater than 21 Sats on 07/23/2025


#### 5.4.2 Operation, limits and benefits



- Mechanism**: Funds are drawn from **Instant Payments Wallet** (Liquid) and converted via a **Liquid → Lightning** swap with **Boltz**.



- Limits:**
 - A minimum amount** higher than a Wallet Lightning native (see above)
 - Expenses** plus Liquid → Lightning swap via Boltz



- Benefits** :
 - Self-custodial**: Your funds remain under your control, stored on the Liquid network, and transferable via Lightning if required
 - No high onchain fees**: Storing on Liquid has saved you costly onchain deposits to open your Lightning channel or add liquidity. These operations can be carried out later, when the amount accumulated on Liquid justifies the fees.



- Tip:** If the recipient has Wallet Bull Bitcoin, use the Liquid network directly to avoid swap costs


#### 5.3.3 Confirmation screen


Take the time to check all the parameters, especially the amount and destination address.


![image](assets/fr/20.webp)



## 6. View history


**Bull Bitcoin Mobile** makes it easy to track your transactions on the **Bitcoin (onchain)**, **Liquid**, and **Lightning** networks. The history can be accessed in two ways, and displays detailed information for each type of transaction. You can also check your transactions using external block browsers.


### 6.1. Access history



- Via the home screen** :
 - Click on the **Secure Bitcoin Wallet** to view **onchain** transactions, or on the **Instant Payments Wallet** for **Liquid** and **Lightning** transactions.
 - The history is displayed directly below the portfolio total, filtered according to the type of Wallet selected.


![image](assets/fr/21.webp)



- Via the dedicated page** :
 - On the Home screen, click on the **history symbol** (clock icon or similar).
 - Access a page listing all transactions, with filters by type of action: **Send**, **Receive**, **Swap**, **PayJoin**, **Sell**, **Buy** (note: Sell and Buy are under development and not available at this time, July 20, 2025).


![image](assets/fr/22.webp)


### 6.2. Transaction details


Each transaction displays specific information depending on the network and the type of action (sending or receiving). Here are the details available for a **transaction onchain** :


![image](assets/fr/23.webp)


### 6.3. Checking via block explorer


The list of explorers for the **Bitcoin onchain**, **Liquid** and **Lightning** networks is in Appendix 4.


For **Lightning**, transactions are not visible on public browsers. Check details (including Swap ID for Boltz) in the application.



## 7. Settings


The "Settings" page can be accessed directly from the Bull Bitcoin application home page, and is used to configure and manage various aspects of the portfolio and user experience.


![image](assets/fr/24.webp)



- Wallet Backup**: Displays the portfolio's recovery phrase for secure backup. See section 3. on portfolio creation for best practices in managing and storing the recovery phrase.



- Wallet Details** :
 - Pubkey**: Public key associated with the wallet, used to generate Bitcoin reception addresses.
 - Derivation Path**: Derivation path used to generate wallet addresses from the private key.



- Electrum Server (Bitcoin Node)**: Set up a connection to a customized Bitcoin node for onchain transactions.



- PIN Code**: Activate and/or modify the security code to protect access to the application and wallet functions.



- Currency**: Choose whether to display amounts in BTC or Sats, and the default fiat currency (dollar, euro, etc.).



- Auto Swap Settings**: The _Auto Swap_ function allows you to automate the transfer of your BTC from the **Instant Payments Wallet (Liquid)** to your **Bitcoin On-Chain** wallet, as soon as the amount reaches a threshold you deem high enough to justify the transaction fee.



- Logs**: Viewable activity logs, which can be shared with technical support to facilitate troubleshooting.



- Telegram access for support** : Direct link to the official Telegram channel for user assistance.



- Github access** : Link to the [Bull Bitcoin Github repository](https://github.com/SatoshiPortal) to view open-source code or report problems.



## APPENDICES


### A1. Explanation of PayJoin (P2EP)


![image](assets/fr/25.webp)


**Definition** :


- PayJoin, or **Pay-to-EndPoint (P2EP)**, is a Bitcoin transaction technique that enhances confidentiality on the **onchain** network. It combines sender and receiver entries in a single transaction, making amounts and addresses more difficult to trace.


**Operation:**


- In a PayJoin transaction, the sender and receiver work together via a compatible PayJoin server to generate a joint transaction.
- Instead of only the sender providing entries (UTXO), the receiver also contributes with one of its own UTXOs. This blurs the information visible on the Blockchain: instead of a single entry corresponding to the actual amount, there are now two entries, and the outputs do not directly reflect the amount exchanged.
- The final transaction resembles a standard Bitcoin transaction (multi-input/multi-output), but hides the actual amount sent and the links between addresses thanks to a steganographic structure.


**For use in Bull Bitcoin Mobile**


- Receive** (address supply): PayJoin is enabled by default.
- Send** : The Wallet automatically detects a PayJoin URI and configures the transaction accordingly, for example:


```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```



**Benefits**


- Enhanced confidentiality**: PayJoin invalidates the assumption that all entries in a transaction belong to a single entity. With PayJoin, inputs come from both sender and receiver, breaking this assumption.
- Amount masking** : The actual amount exchanged does not appear directly in the outputs. It is calculated as the difference between the recipient's UTXO inbound and outbound, making the analysis misleading.


**Limits**


- PayJoin requires the sender and receiver to use compatible wallets, otherwise a standard onchain transaction is used.
- The transaction is slightly more complex (more inputs and outputs), resulting in slightly higher costs.
- Although designed to resemble a standard transaction, advanced heuristics (e.g. ambiguous outputs, known PayJoin servers) may lead one to suspect its use, albeit without absolute certainty.


**More info:**


- [Glossary](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)



### A2. Explanation of Replace-by-fee (RBF)


**Definition**: Replace-by-fee (RBF) is a feature of the Bitcoin network that allows the sender to accelerate the confirmation of an **onchain** transaction by agreeing to pay a higher fee.


**Limits** :


- RBF is not available for Liquid or Lightning transactions.
- The initial transaction must be marked as RBF-compatible when it is created, which Bull Bitcoin Mobile does automatically unless disabled.


**More info:**


- [Glossary](https://planb.network/fr/resources/glossary/rbf-replacebyfee)



### A3. Best practices


To use **Bull Bitcoin Mobile** securely and efficiently, follow these recommendations. They will help you protect your funds, optimize your transactions, and preserve your confidentiality on the **Bitcoin (onchain)**, **Liquid**, and **Lightning** networks.



- Secure your recovery phrase** :
 - Tutorial: [Save your mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)



- Use secure authentication** :
 - Activate a **strong PIN** or **biometric authentication** (fingerprint or facial recognition) to protect access to the application.
 - Never share your PIN or biometric data.



- Protect your privacy** :
 - Generate a new address for each onchain or Liquid reception to limit tracing on the Blockchain.
 - Use PayJoin when available to increase confidentiality regarding the amount sent onchain
 - For maximum confidentiality, connect your Wallet to your own Bitcoin node via an Electrum server instead of using the public node



- Choose the network best suited to your needs** :
 - Onchain**: Preferred for long-term custody or large-value transactions (fees negligible in relation to amount).
 - Liquid**: Use for fast, low-cost transfers with enhanced confidentiality.
 - Lightning**: Opt for instant, low-cost transfers for small amounts. If you are two Wallet Bull Bitcoin users, choose Liquid to avoid Lightning <> Liquid swap fees via Boltz.



- Always check shipping addresses** :
 - Before sending funds, check the address carefully. Funds sent to the wrong address are lost forever. Use copy/paste or QR code scanning, never copy/modify an address by hand.



- Optimize costs** :
 - For onchain transactions, choose appropriate fees (slow, medium, fast) according to urgency and network congestion.
 - Use Liquid, or Lightning for small amounts.
 - Activate Replace-by-fee (RBF) (see Appendix 4) for onchain shipments if you anticipate a need to speed up confirmation.



- Keep the application up to date



### A4. Additional resources



- Official links and support:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : support email
 - [Bull Bitcoin official website](https://bullbitcoin.com/) :** Information on Bull Bitcoin services, account creation, access to the application
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** View code, evolution and roadmap, contribute to development...
 - [Account X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Telegram** group for Wallet mobile: group chat with support, see "Settings" page.



- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lightning: **[1ML (Lightning Network)](https://1ml.com/)**



- Learning and tutorials:** **[Plan ₿ Network](https://planb.network/)** :
 - Securing your recovery phrase


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- Liquid Network** :
 - [Glossary](https://planb.network/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Glossary](https://planb.network/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin


#### Company overview


**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, is the oldest non-depository exchange platform dedicated exclusively to Bitcoin, founded in 2013 at the Bitcoin Embassy in Montreal, Canada. Headed by Francis Pouliot, a recognized pioneer in the Bitcoin ecosystem, the company positions itself as a key player in promoting financial sovereignty and user autonomy. Its mission is to enable individuals to regain control of their money by using Bitcoin as a tool for freedom and payment, while rejecting fiat currencies and cryptocurrencies other than Bitcoin.


![image](assets/fr/26.webp)


[Create your account](https://app.bullbitcoin.com/registration/orangepeel) with 0.25% discount on Bitcoin purchases and sales.


#### Values and philosophy


Bull Bitcoin stands out for its commitment to Cypherpunk principles and Bitcoin ethics:



- Exclusive focus on Bitcoin** : The platform is true to the vision of a decentralized, censorship-resistant currency.



- Non-custodian** : Users retain full control of their Bitcoins by sending funds to their own portfolios.



- Confidentiality**: Minimized collection of personal data, with KYC-free purchase options for transactions under 999 USD. Data is protected in accordance with regulations (FINTRAC in Canada, AMF in France).



- Transparency**: No hidden fees, costs are included in the spread (the difference between purchase and sale prices).



- Financial sovereignty**: Bull Bitcoin promotes independence from traditional banking systems and centralized institutions.


#### Main services



- Fiat deposit** : Users can fund their Bull Bitcoin account with fiat currency (CAD, EUR, etc.) via bank transfer or cash/debit card at selected Canadian post offices.



- Purchasing Bitcoin** : Users can purchase Bitcoin which is sent directly to their non-depository portfolio, guaranteeing total control of their funds.



- Scheduled Bitcoin purchase**: Bull Bitcoin offers an automated recurring purchase service (DCA - Dollar Cost Averaging) at regular intervals, drawing on your available balance, with direct transfer of Bitcoins to a user-controlled wallet, reducing the impact of price volatility.


Note that an option called "AutoBuy" allows you to convert your fiats as soon as they touch your Bull Bitcoin balance, and send your Bitcoins to your own wallet. This option can also be combined with a recurring bank transfer scheduled with your bank to make a DCA. This option automates your Bitcoin accumulation without ever having to open the application.




- Buy Bitcoin at a fixed price 'Limit Order'**: Allows you to buy Bitcoin at a price specified in advance by the user, which is automatically executed when the Bull Bitcoin index price reaches or falls below the set limit.



- Selling Bitcoin**: Users can sell their Bitcoins and receive the funds in fiat currency directly into their bank account via bank or SEPA transfer.



- Third-party payments**: Bull Bitcoin enables users to send fiat money to bank accounts from their Bitcoins, completely transparently to the recipient.



- Bull Bitcoin Prime**: Bull Bitcoin Prime is a premium service for high net worth and enterprise customers, offering customized solutions and premium support. This includes access to reduced fees, a dedicated account manager, and tailored corporate services. This service is aimed at institutions, professional traders and corporate clients seeking in-depth expertise and priority treatment.



- Mobile wallet**: Bull Bitcoin offers an open-source, self-custodial mobile wallet, available on Android and iOS, which supports onchain, Liquid and Lightning Network transactions.



- Educational support**: Free guides and personalized coaching to help users create, secure and manage their Bitcoin portfolios, reinforcing financial autonomy.


#### Compliance and safety



- Regulatory**: Registered with FINTRAC (Canada) and AMF (France), Bull Bitcoin complies with KYC/AML requirements.



- Security**: Use of secure portfolios and offline storage recommendations. Personal data is hosted on Bull's Bitcoin infrastructure, which is 100% self-hosted and does not rely on any third party.