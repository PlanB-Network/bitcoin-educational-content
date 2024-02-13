# Bitcoin and BTCPay Server

Introduction Course BTCPay Server Operator.

AN UNFINISHED STORY

"This Is Lies, My Trust In You Is Broken, I Will Make You Obsolete".

BTCPay Server Foundation

# Introduction Course BTCPay Server Operator. BY Alekos & Bas

## Critical acclaim for Author’s Bitcoin and BTCPay Server

Let's start with what BTCPay Server is and where it came from. We value transparency and certain standards to form trust in the Bitcoin space. A project in the space broke these values. BTCPay Server’s lead developer, Nicolas Dorier, took this personally and made the promise to obsolete them. Here we are many years later and working towards this future, fully open-source, every day.

Nicolas Dorier

"This is lies, my trust in you is broken, I will make you obsolete" .

<hr>

After the words spoken by Nicolas, it was time to start building. Lots of work went into what we now call BTCPay Server. More people wanted to help with this push. The most recognizable are r0ckstardev, MrKukks, Pavlenex, and the first merchant to use the software, astupidmoose.

<hr>

What does open source mean, and what goes into such a project?
FOSS stands for Free & Open-Source Software. The former refers to terms that allow anyone to copy, modify, and even distribute versions (even for profit) of the software. The latter refers to openly sharing the source code, encouraging the public to contribute and improve it.

This brings in experienced users enthusiastic about contributing to the software they already use and derive value from, proving over time to win out in adoption over proprietary software. It is consistent with the Bitcoin ethos that “information longs to be free.” It brings together passionate people who form a community and is simply more fun. Like Bitcoin, FOSS is inevitable.

### Before we begin.
This course consists of multiple parts. Many will be taken care of by your classroom teacher, Demo environments that you get access to, a hosted server for yourself, and possibly a domain name. If you complete this course independently, please be aware that the environments labeled as DEMO won’t be available for you.

**!Note!**

If you follow this course by classroom, server names might differ depending on your classroom setup. Variables in Server names might be different due to this.
### Structure
Every course day has objectives and knowledge assessments. In this textbook, we will cover each of these and have a summary of key features at each lesson block. Illustrations are featured to provide visual feedback and reinforce key concepts in a visual aspect. Objectives are set at the start of each lesson block. These objectives go beyond a checklist. These provide you with a guide into a new skill set. Knowledge Assessments progressively more challenging set up of your BTCPay Server set up.

### What do students receive with the course?
Students will partake in a 3- to 5-day course to better understand Bitcoin and Software by BTCPay Server. With the BTCPay Server Course, a student can understand the basic principles, technically and non-technical of Bitcoin. The extensive training in using Bitcoin through BTCPay Server will allow students to operate their own Bitcoin infrastructure.

### What do Instructors receive with the course?
The BTCPay Server Course instructors can communicate more directly with the project, tailor their course to their needs, and get Free and Open Source course material (Teacher booklet and presentation, Student textbook) and an easy overview to grade the course.

### Important Web addresses or Contact opportunities.
The BTCPay Server Foundation, which allowed Alekos and Bas to write this course, is in Tokyo, japan. The BTCPay Server foundation can be reached through the website listed;
- https://foundation.btcpayserver.org
- join the official chat channels :https://chat.btcpayserver.org

# Table of Contents
1. [Objective 1: Introduction To Bitcoin Day 1.](#objective-1-introduction-to-bitcoin-day-1)
2. [Objective 2: Introducing BTCPay Server.](#objective-2-introducing-btcpay-server)
3. [Objective 3: Introduction to Bitcoin Keys](#objective-3-introduction-to-securing-bitcoin-keys)
4. [Objective 4: BTCPay Server Interface](#objective-4-btcpay-server-interface)
5. [Objective 5: BTCPay Server Default Plugins](#objective-5-btcpay-server-default-plugins)
6. [Objective 6: Configuring BTCPay Server](#objective-6-configuring-btcpay-server)


# Objective 1: Introduction To Bitcoin Day 1.
## Class room exercice - Understanding Bitcoin

Day 1 consists of 1 exercise, which is a classroom exercise; if you take this course yourself, you cannot perform this exercise. To complete this task, The minimum number of people is (9/11).

The exercise starts after watching the introduction “How Bitcoin and the blockchain works” by the BBC.

https://youtu.be/mhE_vvwAiRc

This exercise requires at least nine people to participate. This exercise intends to physically get an idea of how Bitcoin works. By playing each role in the network, you will have an interactive and playful way of learning. This exercise does not involve Lightning Network. See objective (3.4) for Lightning Network.

### Example; Requires 9 / 11 people 
1 - Costumer

1 - Merchant

Others - Bitcoin nodes

**Setup is as follows:**

Customers buys a product from the store with Bitcoin. 

**Scenario 1 - Traditional Banking System**
- Set up:
    - See diagrams/explainer in the attached Figjam - Activity Schematic.
    - Get three student volunteers to play the roles of Customer (Alice), Merchant (Bob), and Bank. 
- Act out the sequence of events:
    - Customer- browsing the store online and finds an item for $25 which they want, and informs the Merchant they would like to purchase
    - Merchant- asks for payment.
    - Customer- sends card information to Merchant
    - Merchant- forwards information to the Bank (identifying both their own and the identity/information) requesting payment of
    - Bank collects information about the Customer and Merchant (Alice and Bob) and checks that the customer’s balance is sufficient.
    - Deducts $25 from Alice’s account, adds $24 to Bob’s account, takes $1 for the service
    - The Merchant receives thumbs-up from Bank and ships the item to the customer. 
- Comments:
    - Bob and Alice must have a relationship with a bank.
    - Bank collects identifying information about both Bob and Alice.
    - Bank takes a cut.
    - Bank must be trusted to custody of each participant’s money all the time.

**Scenario 2 - Bitcoin System**
- Set up:
    - See diagrams/explainer in the attached Figjam - [Activity Schematic](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
    - Replace Bank with nine students who will play the role of a Computer (Bitcoin Nodes/Miners) in a network to replace the Bank.
- Each of the 9 Computers has a complete historical record of all past transactions ever made (thus accurate balances without forgeries), as well as a set of rules:
    - Verify transaction is properly signed (thekeyfitsthelock)
    - Broadcast and receive valid transactions to peers in the network, throw out invalid ones (including any that attempt to spend the same funds twice)
- Update/Add records periodically with new transactions received from “random” computer provided all contents are valid (note: we are ignoring, for now, the Proof of Work component to all this, for simplicity), otherwise reject these and continue as before until the next “random” computer sends an update
    - The proper amount was rewarded if the contents were valid.
- Act out the sequence of events:
    - Customer- browsing the store online and finds an item for $25 which they want, and informs the Merchant they’d like to purchasK Q Merchant- asks for payment by sending the customer an invoice/address from their wallet.
    - Customer- constructs a transaction (sending $25 worth of BTC to an address provided by Merchant) and broadcasts it to the Bitcoin Network.
- Computers- receive the transaction and verify:
    - There is at least $25 of BTC in the address being sent from
    - The transaction is signed properly (“unlocked” by the customer)
    - If not the case, then the transaction will not be propagated through the network, and if so, then it propagates and is held in waiting. 
    - Merchants can check that transaction is pending and waiting.
- One computer is “randomly” chosen to propose to finalize the proposed transaction by broadcasting “a block” containing it; if it checks out, they will receive a BTC reward.
    - OPTIONAL/ADVANCED - instead of randomly selecting a Computer, simulate mining by having Computers roll dice until some predetermined outcome occurs (e.g. first one to roll double sixes is selected)
    - It can also play out what would happen if two Computers win approximately simultaneously, resulting in a chain split.
    - Computers check the validity, update/add records to their ledgers if rules are met, and broadcast block to peers.
    - The randomly chosen computer receives a reward for proposing a valid block.
    - Merchant checks transaction was finalized; thus, funds were received, and the item was sent to the customer.
- Comments:
    - Notice there was no need for a pre-existing banking relationship.
    - No third party needed to facilitate; replaced by code/incentives.
    - No data collection by anyone outside the direct exchange and only the necessary amount must be exchanged between participants (e.g., shipping address).
    - No trust is required between the people (other than the Merchant sending the item), like a cash purchase in many ways.
    - The money is owned directly by the individuals.
    - The Bitcoin ledger is depicted in dollars for simplicity, but in reality, it is BTC.
    - We simulate a single transaction being broadcast, but in reality, multiple transactions are pending in the network, and blocks include thousands of transactions at once. Nodes also check there are no double-spend transactions pending (I would throw all but one out if it were the case).
- Cheating scenarios:
- What if the customer did not have $25 BTC?
    - They would not be able to create the transaction because “unlocking” and “ownership” are the same thing, and computers check transaction is properly signed; otherwise, they reject it
- What if the randomly chosen computer attempts to “change the ledger”?
    - The block would be rejected, as every other computer has a complete history and would notice the change, violating one of their rules.
    - Random Computer would not get a reward, and no transactions from their block would be finalized.

## Knowledge assessment
### KA 1.1 Classroom discussion
Discuss some oversimplifications made in the classroom exercise under the second scenario and describe what the actual Bitcoin system does in more detail.

### KA 1.2 Vocabulary review.
Define the following key terms introduced in the prior section:

Node - __________________________________________________________________________________________________________________________________________________________________________________________

Mempool - _____________________________________________________________________________________________________________________________________________________________________________________

Difficulty Target - ______________________________________________________________________________________________________________________________________________________________________________

Block - ________________________________________________________________________________________________________________________________________________________________________________________


**Discuss meaning of some additional terms as a group:**

Blockchain, Transaction, Double-Spend, Byzantine Generals’ Problem, Mining, Proof of Work (PoW), Hash Function, Block Reward, Blockchain, Longest Chain, 51% Attack, Output, Output Lock, Change, Satoshis, Public/Private Key, Address, Public-Key Cryptography, Digital Signature, Wallet

# Objective 2: Introducing BTCPay Server.

**Understanding BTCPay Server login screen.**

**Managing user account(s)**

**Creating a new store**

## Working with BTCPay Server;

The objective of this course block will be to have a general understanding of BTCPay Server software. In a shared environment, it’s recommended to follow the instructor’s demonstration and follow along with the BTCPay Server Coursebook to follow the teacher. You will learn how to create a wallet through multiple methods. Examples include Hot wallet setups and hardware wallets connected through BTCPay Server Vault. These objectives occur in the Demo environment, displayed and given access to by your course instructor.

If you follow this course by yourself, you can find a list of third-party hosts for Demo purposes at https:// directory.btcpayserver.org/filter/hosts. We strongly advise against using these third- party options as production environments, but they serve the right purposes for an introduction to using Bitcoin and BTCPay Server.

As a BTCPay Server rockstar trainee, you might have previous experience setting up a Bitcoin node. This course will talk specifically tailored to the BTCPay Server Software stack.

Many of the options in BTCPay Server exist in some form or another in other Bitcoin Wallet-related software.

## BTCPay Server Login screen.

![image](assets/en/0.jpeg)
As you are welcomed to the Demo environment, you are asked to ‘Login’ or ‘Create your account.’ Server administrators might turn off the feature of creating new accounts for security reasons. BTCPay Server logos and button colors can be changed because BTCPay Server is Open Source Software. A Third-party host can White-label the software and change the entire look.

## Create an Account window.

![image](assets/en/1.png)
Creating accounts on BTCPay Server requires valid Email address strings; example@email.com would be a valid string for Email.

Password need to be at least 8 characters long, including letters, numbers, and characters. After setting the password once, you will have to verify the typed password to make sure it’s correct to what was typed in the first password field.

When both the Email and Password fields are properly filled in, click on the ‘Create Account’ button. This will save the Email and password on the instructor’s BTCPay Server instance.

**!Note!**

If you follow this course on your own, creating this account would be something you might do on a third-party host; therefore, again, we mention never to use these as production environments but only for training purposes.

## Account Creation by BTCPay Server Administrator.
The Administrator of the BTCPay Server Instance can also create accounts for BTCPay Server. The Administrator of the BTCPay Server instance can click on ‘Server Settings’ (1), click on the ‘Users’ tab (2), and click the “+ Add User” button (3) in the top right of the Users tab. In Objective (4.3), you will learn more about the administrator control of Accounts.

![image](assets/en/2.png)

As an administrator, you would need the user’s Email address and set a standard password. It is advised as Administrator to inform the user that they should change this password before using the account for security reasons. If the Administrator does NOT set a Password and SMTP has been set on the server, the user will receive an email with an invite link to create their account and set the password themselves.

## Objective Example 1;

When following the course by an instructor, follow the link given by the instructor and create your account on the Demo environment provided. Ensure your email address and password are saved securely; you will need these login credentials for the rest of the demo objectives in this course.

Your instructor may have gathered the email address upfront and sent an invitation link before this exercise. If instructed, check your Email.

When taking the course without an instructor, create your account using the BTCPay Server demo environment; go to

https://mainnet.demo.btcpayserver.org/login.

This account should only be used for demonstration/training purposes and never for business.

## Skill Summary:

In this section, you learned the following:
- How to create an account on a hosted server through the interface.
- How a server administrator can manually add users in the server settings.

## Knowledge assessment;

## KA 2.1 Conceptual Review

Give reasons why using a Demo Server is a bad idea for production purposes: _________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Account Management on BTCPay Server

After a store owner has created their account, they can manage it in the Bottom Left of the BTCPay Server UI. Underneath the Account button, there are multiple higher-level settings.
- Dark/Light mode.
- Hide Sensitive Info toggle.
- Manage Account.

## Dark and Light mode.

Users of BTCPay Server can choose between a Light or Dark mode version of the UI. Customer- facing pages won’t change. They use customer- preferred settings regarding dark or light mode.

## Hide Sensitive info toggle.

![image](assets/en/3.png)

The hide sensitive info button brings a quick and simple layer of security. Whenever you need to operate your BTCPay Server, but there might be people lurking over your shoulder in a public space, turn on Hide Sensitive Info, and all the values in BTCPay Server will be hidden. One might be able to look over your shoulder but can no longer see the values you are dealing with.

## Manage Account.

Once the user account has been created, this is where to manage passwords, 2fa, or API kes.

## Manage Account - Account

Optionally update your account with a different Email address. To ensure your email address is correct, BTCPay Server allows you to send a verification email. Click save if the user sets a new email address and confirms the verification worked. The username remains the same as the previous Email.

A user may decide to delete their whole account. This can be done by clicking the delete button on the Account tab.

![image](assets/en/4.png)

**!Note!**

After changing the Email, the username for the account will not change. The previous given Email Address will stay the Login name.

## Manage Account - Password

A student may want to change his password. He can do this by going to the Password tab. Here he is required to type his old password and can change it to a new one.

![image](assets/en/5.png)

## Two-Factor Authentication (2fa)

To limit the consequences of a stolen password, you can use two-factor authentication (2fa), a relatively new security method. You can activate two- factor authentication via the Manage account and the tab for two-factor authentication. You must complete a second step after logging in with your username and password.

BTCPay Server allows for two ways of enabling 2FA, App-based 2FA (Authy, Google, Microsoft authenticators) or through Security devices (FIDO2 or LNURL Auth).

## Two-Factor Authentication - App based

Based on your mobile phone’s Operating System (Android or iOS), users can pick between the following apps;

1. Download a two-factor authenticator;
    - Authy for [Android](https://play.google.com/store/apps/details?id=com.authy.authy) or [iOS](https://apps.apple.com/us/app/authy/id494168017)
    - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) or [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
    - Google Authenticator for [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) or [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. After downloading and installing the Authenticator App.
    - Scan the QR Code provided by BTCPay Server
    - Or enter the generated key by BTCPay Server manually into your Authenticator app.
3. The Authenticator app will provide you with a unique code. Enter the unique code in BTCPay Server to verify the setup, and click verify to complete the process.

![image](assets/en/6.png)

## Skill Summary:

In this section, you learned the following:

- Account management options and the various ways to manage an account on a BTCPay Server instance.
- How to set up app-based 2FA.

## Knowledge assessment;
## KA 2.2 Conceptual Review
Describe how app-based 2FA helps secure your account: ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Create your store wizard.

When a new user logs into BTCPay Server, the environment is empty and needs a first store. The introduction wizard of BTCPay Server will give the user the option to ‘Create your store’ (1). A Store can be seen as a Home for your Bitcoin needs. A new BTCPay Server Node will start with Synching the Bitcoin Blockchain (2). Depending on what infrastructure you run BTCPay Server on, this can range from a few hours to a few days. The instance's current version is shown in the bottom right corner of your BTCPay Server UI. This is useful for reference when troubleshooting.

![image](assets/en/7.png)

## Create your store wizard

Following this course will start with a slightly different screen than the previous page. As your instructor has prepared the Demo environment, the Bitcoin blockchain has been synchronized prior, and therefore you will not see the nodes’ sync status.

A user may decide to delete their whole account. This can be done by clicking the delete button on the Account tab.

![image](assets/en/8.png)

**!Note!**

BTCPay Server account’s can make unlimited amounts of stores. Each store is a wallet or “ home”.

### Objective Example 1;

Start by clicking on “Create your store. “

![image](assets/en/9.png)

This will create your first Home and dashboard for using BTCPay server.
1. After clicking “Create your store,” BTCPay Server will require you to name the store; this can be anything useful to you.

    ![image](assets/en/10.png)

2. A default store currency has to be set next, either a fiat currency or denominated in a Bitcoin / Sats standard. For the demo environment, we will set it to USD.

    ![image](assets/en/11.png)

3. As a last parameter on the store setup, BTCPay Server requires you to set a “Preferred price source” to compare Bitcoin’s price against the current fiat price so your store displays the correct exchange rate between Bitcoin and the store-set fiat currency. We will stick with the default in the Demo example and set this to the Kraken exchange. BTCPay Server uses the Kraken API to check the exchange rates.

    ![image](assets/en/12.png)

4. Now that these store parameters have been set, click on the Create button, and BTCPay Server will create your first store’s dashboard, where the wizard will continue.

    ![image](assets/en/13.png)

Congratulations, you have created your first store, and this rounds up this exercise.

![image](assets/en/14.png)

**!Note!** 

Place Note

### Skill Summary:

In this section, you learned:
- Store creation and configuring a default currency combined with price source preferences.
- Each “Store” is a new home separated from other stores on this installation of BTCPay Server.

# Objective 3: Introduction to Securing Bitcoin Keys
**Understanding Bitcoin Keys Generation**

**Securing keys with hardware wallet**

**Using your Bitcoin keys**

**BTCPay Server Lightning Wallet**

## What is involved in generating bitcoin keys ?

Bitcoin wallets, when created, create a so-called “seed.” In the last objective, you created a “seed.” The series of words generated before are also known as mnemonic phrases. The seed is used to derive individual Bitcoin Keys from and used to send or receive Bitcoin. Seed phrases should never be shared with third parties or untrusted peers.

The seed generation is done along the industry standard known as the “Hierarchical Deterministic (HD)” framework.

![image](assets/en/15.png)

## Addresses

BTCPay Server built to generate a new Address. This alleviates the problem of public key or Address reuse. Using the same Public key makes tracking your entire payment history very easy. Thinking of keys as one-time-use vouchers would significantly improve your privacy. We also use Bitcoin Addresses, do not confuse these with Public keys.

An Address gets derived from the Public key through a “hashing algorithm.” Most wallets and transactions, however, will display Addresses rather than those public keys. Addresses are, in general, shorter than public keys and usually begin with a ‘1’, ‘3’, or ‘bc1’, whereas public keys begin with “02”, “03”, or “04”.
- Addresses starting with “1.....” are still very common addresses. As mentioned in Objective 2.3, these are legacy addresses. This address type is meant for P2PKH transactions. P2Pkh uses Base58 encoding, which makes the address case-sensitive. Its structure is based on the public key with an additional 1 digit as the identifier.

- Addresses starting with “bc1...” are slowly moving into the very common addresses. These are known as (native) SegWit Addresses. These offer a better fee structure than the other mentioned Addresses. Native SegWit Addresses use Bech32 encoding and only allow for lowercase letters.

- Addresses starting with “3...”are commonly still used by exchanges for deposit addresses. These addresses are mentioned in objective 2.3, wrapped or nested SegWit addresses. However, they could also function as a “Multisig Address.” When used as a SegWit address, there are some savings on transaction fees again, less so than Native SegWit. P2SH Addresses use Base58 encoding. This makes it case Sensitive, like the legacy address.

- Addresses starting with “2..”. These are Testnet addresses. They are meant to receive testnet bitcoin (tBTC). You should never mix this up and send Bitcoin to these addresses. For development purposes, you can generate a testnet wallet. There are multiple faucets online to get testnet Bitcoin. Never purchase Testnet Bitcoin. Testnet Bitcoin is mined. This might be a reason for a developer to use Regtest instead. This is a playground environment for developers, missing certain network components. Bitcoin is, however, for development purposes, very useful.

## Public Keys.
Public keys get less used in practice today. Over time bitcoin users have been replacing them with Addresses instead. They do still exist and still get used occasionally. Public keys are, in general, much longer strings than addresses. Just like with addresses, they start with a specific identifier.
- First, “02....” and “03..” Very standard public key identifiers encoded in SEC format. These can be processed and turned into addresses for receiving, used for creating multi-sig addresses, or to verify a signature. Early-day Bitcoin transactions used public keys as part of P2PK transactions.

- HD wallets, however, use a different structure. “Xpub...”, “ypub..” or “zpub...” are called extended public keys rather called xpubs. These keys are used to derive many public keys as it’s part of the HD wallet. As your xpub holds the records of your entire history, meaning past and future transactions, never share these with untrusted parties.

## Skill Summary:

In this section, you learned the following:
- The differences between addresses and public key data types and the benefits of using addresses over public keys.

## Knowledge assessment

Describe the benefit of using fresh addresses for each transaction compared to address reuse or public key methods: ____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Storing Bitcoin Keys.

After generating a seed phrase, the list of 12 - 24 words generated in this book requires proper backups and security, as these words are the only way to recover access to a wallet. The structure of HD wallets and how it generates addresses deterministically using that one seed, all your created addresses will get backed up using this one list of mnemonic words representing your seed or recovery phrase.

Keep your recovery phrase secured. If accessed by someone, specifically with malicious intent, they can move your funds. Keeping the seed safe and secured but also remembering it is mutual to each other. There are several methods to store Bitcoin private keys, each with benefits and disadvantages, either in security, privacy, convenience, or physical means. Due to the importance of private keys, bitcoin users tend to store and safely keep these keys in “self custody” over using “custodial” services like banks. Depending on the user, he has to use either a Cold storage solution or a Hot wallet.

## Hot and Cold storage of bitcoin keys.

Usually, bitcoin wallets are denominated in a Hot Wallet or Cold Wallet. Most trade-offs lie in convenience, ease of use, and security risks. Each of these methods can also be seen in a custodian solution. However, trade-offs here are mostly security and privacy based and go beyond the scope of this course.

## Hot wallet

Hot wallets are the most convenient way of interacting with Bitcoin through mobile, web, or desktop software. The wallet is always connected to the internet, enabling users to send or receive Bitcoin. This, however, is also its weakness, the wallet, as it is always online, is now more vulnerable to attacks by hackers or malware on your device. In BTCPay Server, hot wallets store the private keys on the instance. Anyone accessing your BTCPay Server store could steal funds from this address if malicious. When BTCPay Server runs in a hosted environment, you should always consider this in your security profile and preferably not use a Hot-wallet in such a case. When BTCPay Server is installed on owned hardware, secured and trusted by you, the risk profile lowers significantly, but it never disappears!

## Cold Wallet

Individuals move their Bitcoin into a cold wallet because it can isolate the private keys from the internet. Removing the internet connection from the equation reduces the risk of malware, spyware, and SIM swaps. Cold storage is believed to be superior to hot storage for security and autonomy, so long as adequate precautions are taken to avoid losing the Bitcoin private keys. Cold storage is most suitable for large amounts of Bitcoin, which are not intended to be spent often due to the wallet setup’s complexity.

There are various methods of how to store Bitcoin keys in cold storage, from paper wallets to brain wallets, hardware wallets, or, from the beginning, a wallet file. Most wallets use BIP 39 to generate the seed phrase mentioned in objective (3). However, within the Bitcoin core software, a consensus has yet to be reached on using it. Bitcoin Core software will still generate a Wallet.dat file you need to store in a secure offline location.

## Skill Summary

In this section, you learned:
- The differences between hot and cold wallets in terms of functionality and their trade-offs.

## Knowledge assessment

### KA 3.2 Conceptual Review
What is a wallet: __________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Difference between hot and cold wallets: _________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Describe what is meant by “generating a wallet”: ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## BTCPay Server Wallet.

BTCPay Server consists of the following standard wallet features.

- Transactions 
- Send
- Receive
- Rescan
- Pull Payments
- Payouts
- PSBT
- General settings

## Transactions

Administrators can see the in and outgoing transactions for the on-chain wallet connected to this specific store in the transactions view. Each transaction has a distinction between received and sent. Received will be green and outgoing transactions will be red. Within the BTCPay Server transaction view, administrators will also see a set of standard labels.

| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

## Send

BTCPay server’s send function sends transactions from your BTCPay Server on-chain wallet. BTCPay Server allows for multiple ways of signing your transactions to spend funds. A transaction can be signed with;
- Hardware Wallet
- Wallets supporting PSBT
- HD private key or recovery seeds.
- Hot Wallet

### Hardware wallet.

BTCPay Server has built-in hardware wallet support allowing you to use your hardware wallet with BTCPay Vault without leaking information to third-party apps or servers. The hardware wallet integration within BTCPay Server allows you to import your hardware wallet and spend the incoming funds with a simple confirmation on your device. Your private keys never leave the device, and all funds are being validated against your full node so there is no data leakage.

### Signing with a wallet supporting PSBT

PSBT (Partially Signed Bitcoin transactions) is an interchange format for Bitcoin transactions that still need to be fully signed. PSBT is supported in BTCPay Server and can be signed with compatible hardware and software wallets.

The construction of a fully signed Bitcoin transaction goes through the following steps:
- A PSBT gets constructed with specific inputs and outputs but no signatures
- The exported PSBT can be imported by a wallet that supports this format
- The transaction data can be inspected and signed using the wallet
- The signed PSBT file gets exported from the wallet and imported with BTCPay Server
- BTCPay Server produces the final Bitcoin transaction
- You verify the result and broadcast it to the network

### Signing with HD Private Key or mnemonic seed


If you have created a wallet before using BTCPay Server, you can spend the funds by inputting your private key into an appropriate field. Set a proper “AccountKeyPath” in wallet> Settings; otherwise, you cannot spend.

### Signing with a hot wallet

If you created a new wallet when setting up your store and enabled it as a hot wallet, it will automatically use the seed stored on a server to sign.

## RBF (Replace-By-Fee)

Replace-By-Fee (RBF) is a Bitcoin protocol feature that allows you to replace a previously broadcast transaction (while still unconfirmed). This allows randomizing your wallet’s transaction fingerprint or replacing it with a higher fee rate to move the transaction higher in the queue of confirmation (mining) priority. This will effectively replace the original transaction as the higher fee rate will be prioritized, and once confirmed, invalidate the original one (no double spend).


Press the “Advanced Settings” button to view the RBF options;

![image](assets/en/16.png)

- Randomize for higher privacy - Allows the transaction to be replaced automatically for randomization of transaction fingerprint.
- Yes - Flag transaction for RBF and be replaced explicitly (Not replaced by default, only by input)
- No - Do not allow the transaction to be replaced.

## Coin Selection

Coin selection is an advanced privacy-enhancing feature that allows you to select coins you want to spend when crafting a transaction. For example, paying with coins that are fresh from a conjoin mix.

Coin selection works natively with the wallet labels feature. This lets you label incoming funds for smoother UTXO management and spending.

BTCpay Server also supports BIP-329 for label management. BIP-329 allows for labels on to; if you transfer from a wallet supporting this particular BIP and set labels, BTCPay Server will recognize these and import them. When migrating servers, this information can also be exported and imported into the new environment.

## Receive

When clicking on the receive button in BTCPay Server, it generates an unused address that can be used to receive payments. Administrators may also generate a new address by generating a new “Invoice.”

BTCPay Server will always ask to generate the following available address to avoid address reuse. After clicking “Generate next available BTC Address,” BTCPay Server generated a new address and QR. It also allows you to directly set a Label to the address for better management of your addresses.

![image](assets/en/17.png)

![image](assets/en/18.png)

### Re-scan

The Rescan feature relies on Bitcoin Core 0.17.0’s “Scantxoutset” to scan the current state of the blockchain (called UTXO Set) for coins belonging to the configured derivation scheme. Wallet rescan solves two issues BTCPay Server users experience.

1. Gap limit problem - Most third-party wallets are light wallets that share a node between many users. Light and full node-reliant wallets limit the amount (typically 20) of addresses without balance they track on the blockchain to prevent performance issues. BTCPay Server generates a new address for every invoice. With the above in mind, after BTCPay Server generates 20 consecutive unpaid invoices, the external wallet stops fetching the transactions, assuming no new transactions occurred. Your external wallet won’t show them once invoices are paid on the 21st, 22nd, etc. On the other hand, internally, the BTCPay Server wallet tracks any address it generates along with a much greater gap limit. It does not rely on a third party and can always show a correct balance.
2. The gap limit solution - If your [external/existing wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) allows gap- limit configuration, the easy fix is to increase it. However, the majority of wallets do not allow this. The only wallets that allow gap-limit configuration we know are Electrum, Wasabi, and Sparrow Wallet. Unfortunately, you are likely to encounter a problem with many other wallets. For the best user experience and privacy, consider dropping external wallets and using the BTCPay Server internal wallet.

### BTCPay Server uses “mempoolfullrbf=1”

BTCPay Server uses “mempoolfullrbf=1”; we have added this as default to your BTCPay Server setup. However, we have also made it a fragment you can disable yourself. Without “mempoolfullrbf=1,” if a customer double- spends a payment with a transaction not signaling RBF, the Merchant would only know after confirmation.

An administrator may want to opt out of this setting. By the following string, you can change the set default.

**“”**

**BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"**

**. btcpay-setup.sh -i**

**“”**

## BTCPay Server Wallet settings.

Wallet settings within BTCPay Server give a clear and quick overview of the general settings of your wallet. All these settings are prefilled if the wallet was created with BTCPay Server.

![image](assets/en/19.png)

Wallet settings within BTCPay Server give a clear and quick overview of the general settings of your wallet. All these settings are prefilled if the wallet was created with BTCPay Server. BTCPay Server’s wallet settings start with the wallet status. Is it a Watch-only or Hot wallet? Depending on the wallet type, actions may vary from rescanning the wallet for missing transactions, Pruning old transactions from history, registering the wallet for payment links, or replacing and deleting the current wallet attached to the store. In BTCPay Server’s wallet setting, administrators may set a Label for the wallet for better wallet management. Here the Administrator will also be able to see the Derivation Scheme, account key (xpub), Fingerprint, and Keypath. Payments in wallet settings only have 2 main settings. Payment is invalid if the transaction fails to confirm in (set minutes) after invoice expiration. Consider the invoice confirmed when the payment transaction has X amount of confirmations. Administrators can also set a toggle to show recommended fees at payments or set a manual confirmation target in the number of blocks.

![image](assets/en/20.png)

**!Note!**

If you follow this course on your own, creating this account would be something you might do on a third-party host, therefore again we mention never to use these as production environments, but rather only for training purposes.

## Example
### Set up a Bitcoin Wallet in BTCPay Server

BTCPay Server allows two ways of wallet setup. One way is importing an already existing Bitcoin wallet. The import can be done by Connecting a hardware wallet, importing a Wallet file, entering an Extended public key, Scanning a wallet’s QR code, or the least favorable, entering a previously created Wallet recovery seed by hand. In BTCPay Server, it is also possible to create a new wallet. There are two possible ways of configuring BTCPay Server when generating a new wallet. The hot wallet option in BTCPay Server allows for features like ‘Payjoin’ or ‘Liquid.’ There is, however, a drawback, the recovery seed generated for this Wallet will be stored on the server, where anyone who has Admin control could fetch the recovery seed. As your private key is derived from your recovery seed, a malicious actor could gain access to your current and future funds! To mitigate such risk in BTCPay Server, an Admin can set in Server Settings > Policies > “Allow non-admins to create hot wallets for their stores” to no, as it is per default. To enhance the security of those Hot wallets, the server administrator should enable 2FA authentication on accounts allowed to have Hot wallets. Storing private keys on a public server is dangerous and comes with risks. Some are similar to Lightning Network risks (see objective (3.4) for Lightning Network risks). The second option BTCPay Server offers in generating a new wallet is by creating a Watch-Only wallet. BTCPay Server will generate your private keys once. After the user confirms to have written down their Seed Phrase, BTCPay Server will wipe the private keys from the server. As a result, your store now has a Watch- only wallet connected to it. To spend the funds received on your watch- only Wallet, see objective (3.3) signing with a hardware wallet, either by using BTCPay Server Vault, PSBT(partially signed bitcoin transaction), or, least recommended, manually providing your seed phrase.

You created a new ‘Store’ in the last objective (2.3). The installation wizard will continue by asking to “Set up a wallet” or “Set up a Lightning node.” In this example, you will follow the “Set up a wallet” wizard process(1).

![image](assets/en/21.png)

After clicking “Set up a wallet,” the wizard will continue by requesting how you want to continue; BTCPay Server now offers the option to connect an existing Bitcoin wallet to your new store. If you do not have a wallet, BTCPay Server proposes creating a new one. This example will follow the steps for “create a new wallet” (2). Follow the steps in Example (X:X) to learn how to “Connect an existing wallet” (1).

![image](assets/en/22.png)

**!Note!**

If you take this course in a class room, the current objective and seed we generated is only for educational purposes. There should never be any substantial amount other than required throughout the exercises on these addresses.

1. Continue the “New wallet” wizard by clicking on the “Create a new wallet” button(1).

![image](assets/en/23.png)

2. After clicking “Create a new wallet,” the next window in the wizard will give the options “Hot wallet” and “Watch-only wallet.” If you follow along with an instructor, your environment is a shared Demo, and you can only create a Watch-only wallet. Notice the difference between Fig 2.11. As you are in the Demo environment following along with the instructor, create a “Watch-only wallet” and continue with the “New Wallet” wizard.

![image](assets/en/24.png)

![image](assets/en/25.png)

3. Continuing the new wallet wizard, you are now in the Create BTC watch-only wallet section. Here we get to set the wallet “Address type” BTCPay Server allows you to pick your preferred Address type; as of the writing of this course, it is still recommended to use bech32 addresses. Learn more in detail about addresses in Objective 3.1.
    - Segwit (bech32)
        - Native SegWit are addresses that start with bc1q.
        - Example: bc1qXXXXXXXXXXXXXXXXXXXXXX
    - Legacy
        - Legacy addresses are addresses that start with the number 1.
        - Example: 15e15hXXXXXXXXXXXXXXXXXXXX
    - Taproot (For advanced users)
        - Taproot addresses start with bc1p.
        - Example: bc1pXXXXXXXXXXXXXXXXXXXXXXXX
    - Segwit wrapped
        - Segwit wrapped are addresses that start with 3.
        - Example: 37BBXXXXXXXXXXXXXXX

Choose segwit (recommended) as your preferred wallet address type.

![image](assets/en/26.png)

4. When setting the parameter for the Wallet, BTCPay Server allows the users to set an optional passphrase through BIP39, be sure to confirm your password.

![image](assets/en/27.png)

5. After setting the Wallet’s Address type and possibly setting some advanced options, click Create, and BTCPay Server will generate your new Wallet. Note that this is the last step before generating your Seed phrase. Make sure you only do this in an environment where one might not steal the seed phrase by looking at your screen.

![image](assets/en/28.png)

6. In the following screen of the wizard, BTCPay Server shows you the Recovery seed phrase for your newly generated Wallet; these are the keys to recovering your Wallet and signing transactions. BTCPay Server generates a seed phrase of 12 words. These words will be erased from the server after this setup screen. This Wallet is specifically a Watch-only wallet. It is advised not to store this seed phrase digitally or by photographic image. Users may only go further in the wizard if they acknowledge actively that they wrote down their seed phrase.

![image](assets/en/29.png)

7. After clicking Done and securing the newly generated Bitcoin seed phrase, BTCPay Server will update your store with the attached new Wallet and is ready to receive payments. In the User Interface, in the left navigation menu, notice how Bitcoin is now highlighted and activated under Wallet.

![image](assets/en/30.png)

## Example 1
### Writing down a seed phrase.

This is a very particular and secure moment to use Bitcoin. As mentioned before, only you should have access to or knowledge about your seed phrase. As you follow along with an instructor and classroom, the seed generated should only be used in this course. Too many factors, prying eyes from classmates, unsecure systems, and many others make these keys only educational and untrusted. However, the keys generated should still be stored for course examples. The first method we will use in the current situation, also the least secure one, is writing down the seed phrase in the proper order. A Seed phrase card is in the course material provided to the student or found on BTCPay Server GitHub. We will use this card to write down the words generated in the prior step. Make sure to write them down in the correct order. After you have written them down, check them against what was given by the software to make sure you wrote them down in the correct order. Once you have written it down, click the checkbox stating you have written down your seed phrase properly. See course img2.17

## Example 2
### Storing a seed phrase on a Hardware Wallet.

In this course, we touch on storing a seed phrase on a hardware wallet. Following this course by an instructor might only sometimes include such a device. In the course, guide materials have written a list of hardware wallets provided that would fit this exercise.

We will use BTCPay Server vault and a Blockstream Jade hardware wallet in this example.

You can also follow along by video for reference on connecting a hardware wallet. [BTCPay Server - How to connect your hardware wallet with BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Download BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Make sure you download the correct files for your system. Windows users should download the [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) package, Mac users download the [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), and Linux users should download [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

After installing BTCPay Server Vault, start the software by clicking the icon on your Desktop. When BTCPay Server Vault is installed properly and started for the first time, it will ask permission to be used with Web Applications. It will ask to grant access to the specific BTCPay Server you work with. Accept these conditions. BTCPay Server Vault will now search for the Hardware device. Once the device is found, BTCPay Server will recognize that Vault is running and has fetched your device.

**!Note!**

Do not give your SSH keys or server admin account to anyone else apart from administrators when using a hot wallet. Anyone with access to these accounts will have access to the funds in the Hot Wallet.

## Skill Summary:

In this section, you learned the following:
- The transaction view of the Bitcoin wallet and its various categorizations.
- Various options are available when sending from a Bitcoin wallet, from hardware to hot wallets.
- The gap limit problem faced when using most wallets, and how to correct this.
- How to generate a new Bitcoin wallet within BTCPay Server, including storing the keys in a hardware wallet and backing up the recovery phrase.

In this objective, you have learned how to generate a new Bitcoin wallet within BTCPay Server. We have not yet gone into how to secure or use those keys. In a quick overview of this objective, you have learned how to set up the first store. You have learned how to generate a Bitcoin Recovery Seed phrase.

## Knowledge assessment;
### KA 3.3.1 Practical Review

Describe a method for generating keys and a scheme for securing them, along with the trade-offs/risks of the security scheme: ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## BTCPay Server Wallet - Lightning

When a server administrator provisions a new BTCPay Server instance, he can set up a lightning network implementation, LND, Core Lightning, or Eclair; see objective (6) for more detailed installation instructions.

If followed along by a classroom, connecting a Lightning node to your BTCPay Server works through a Custom node. A user who is not a server administrator on BTCPay Server will not be able to use the internal Lightning node by default. This is to protect the server owner from losing his funds. Server administrators may install a Plugin to give access to their Lightning node through LNBank; this is outside of the scope of this book; read more on LNBank on the official plugin page.

## Connect internal node (server administrator)

The Server Administrator can use BTCPay Server’s internal Lightning Node. Regardless of the Lightning implementation, the connecting to the internal Lightning node is the same.

Goto a previous setup store, and click on the “Lightning” wallet in the left menu. BTCPay Server gives two setup possibilities, Using the Internal node (Server admin only by default) or a custom node (external connection). Server administrators can click on the “Use internal node” option. There is no further configuration required. Click the “save” button and notice the notification stating, “BTC Lightning node updated. “The store has now successfully got Lightning network capabilities.

## Connect external node (server user/ store owner)

As store owners are by default not allowed to use the server administrator Lightning Node. The connection needs to be made to an external node, either a node owned by the store owner prior to a BTCPay Server setup, an LNBank plugin if made available by the server administrator, or a custodian solution like Alby.

Goto a previous setup store, and click “Lightning” underneath wallets in the left menu. As store owners are not allowed to use the internal node by default, this option is grayed out. Using a custom node is the only option by default available for store owners.

BTCPay Server needs connection information; the prior made (or custodian solution) will deliver this information specific to a Lightning implementation. Within the BTCPay Server, Store owners can use the following connections;

- C-lightningviaTCPorUnixdomainsocketconnection.
- Lightning Charge via HTTPS
- Eclair via HTTPS
- LND via the REST proxy
- LNDhub via the REST API

![image](assets/en/31.png)

Click “test connection “to ensure you correctly entered the connection details. After the connection confirms to be good, click save, and BTCPay Server shows the store is updated with a Lightning Node.

## Managing internal Lightning node LND ( Server administrator)

After connecting the internal Lightning Node, server administrators will notice new tiles on the Dashboard (see objective (4.1) for more on dashboard tiles) specifically for Lightning information.

- Lightning Balance
- BTC in channels
    - BTC opening channels
    - BTC local Balance
    - BTC remote balance
    - BTC closing channels
- BTC On-chain
    - BTC confirmed
    - BTC unconfirmed
    - BTC reserved
- Lightning Services
    - Ride the Lightning (RTL).

By clicking either on the Ride the Lightning Logo in the “Lightning services” tile or “Lightning” underneath wallets in the left menu, server administrators can reach RTL for Lightning node management.

**!?Note!?**

Connecting the internal Lightning Node fails - If the internal connection fails, confirm:

1. The Bitcoin on-chain node is fully synchronized
2. The Internal lightning node is "Enabled" under "Lightning" > "Settings" > "BTC Lightning Settings"

If you are unable to connect to your Lightning node, try restarting your server, or read for more details on BTCPay Server official documentation; https://docs.btcpayserver.org/Troubleshooting/ . You cannot accept lightning payments in your store until your Lightning node appears "Online". Try to test your Lightning connection by clicking the "Public Node Info" link

## Lightning wallet

![image](assets/en/32.png)

### Lightning

Within the Lightning wallet option in the left menu bar, server administrators will find easy access to RTL, their Public node Info, and Lightning settings specific to their BTCPay Server store.

### Internal node info

Server administrators can click on the internal node info and glance at their server status ( Online/ Offline) and connection string for Clearnet or Tor.

### Change connection.

If the store owner decides to use
changed within the Lightning Settings - Change connection. Next to the Public Node info store, owners can find this option. It will bring back the initial setup for the external lightning node connection, fill out the new Lightning node information, click save, and update the store with the new node information.

![image](assets/en/33.png)

### Services

If the server administrator decides to install multiple services for the Lightning implementation, they will be listed here. With a standard LND implementation, administrators will have Ride The Lightning (RTL) as a standard tool for node management.

### BTC Lightning wallet settings

After adding the Lightning node to the store in a prior step, within the settings of the Lightning wallet, store owners can still choose to deactivate it for their store by using the Toggle at the top of Lightning settings.

![image](assets/en/34.png)

### Lightning Payment options.

Store owners can set parameters for the following to enhance the Lightning experience for their customers.

- Display Lightning payment amounts in Satoshis.
- Add hop hints for private channels to the Lightning invoice.
- Unify on-chain and Lightning payment URL/QR codes at checkout.
- Set a description template for lightning invoices.

### LNURL

Store owners can choose to either use or not use LNURL. A Lightning Network URL, or LNURL, is a proposed standard for interactions between Lightning Payer and payee. In short, an LNURL is a bech32 encoded url prefixed with lnurl. The Lightning wallet is expected to decode the URL, contact the URL, and await a JSON object with further instructions, most notably a tag defining the behavior of the knurl.

- Enable LNURL
- LNURL Classic Mode
    - For wallet compatibility, Bech32 encoded(classic) vs cleartext URL(upcoming)
- Allow the payee to pass a comment.

## Example 1
### Connect to Lightning with the internal node (Administrator).

This option is only available if you are the Administrator of this instance or if the Administrator has changed the default settings where users can use the internal lightning node.

As an administrator, click on the Lightning Wallet in the left menu bar. BTCPay Server will ask to use one of two options for connecting a Lightning Node, an Internal node, or a custom external node. Click on Use internal node and click on save.

### Managing your Lightning node (RTL)

After connecting to the internal lightning node, BTCPay Server will update and show a notification “BTC Lightning node updated, “confirming you have now connected Lightning to your store.

Managing the lightning node is a task for the Administrator of the server. This involve.

- Manage transaction
- Managing liquidity
    - Inbound liquidity
    - Outbound liquidity
- Managing peers and channels
    - Connected peers
    - Channel fees
    - Channel status
- Making frequent backups of the channel states.
- Checking routing reports
- Alternatively, use services such as Loop.

All lightning node management is as standard done with RTL (assuming you are running on a LND implementation). Administrators can click on their Lightning Wallet in BTCPay Server and find a button to open RTL. The main Dashboard of BTCPay Server is now updated with the Lightning Network Tiles, including quick access to RTL.

## Example 2
### Connect to lightning with Alby.

When connecting with a custodian like Alby, store owners should first create an account, visit: https://getalby.com/

![image](assets/en/35.png)

After creating the Alby account, go to your BTCPay Server store.

Step 1: Click ‘Set up a Lightning node’ on the Dashboard or ‘Lightning’ underneath wallets.

![image](assets/en/36.png)

Step 2. Insert your Wallet connection credentials provided by Alby. On the Dashboard of, Alby, click on Wallet. Here you will find “Wallet Connection Credentials.” Copy these credentials. Paste the credentials from Alby into the Connection configuration field in BTCPay Server.

![image](assets/en/37.png)

Step 3; After providing BTCPay Server with the Connection details, click the “Test Connection “button to ensure the connection is working properly. Notice the “Connection to lightning node successful” message at the top of your screen. This confirms that everything works in order.

![image](assets/en/38.png)

Step 4; Click save, and your store is now connected with a lightning node by Alby.

![image](assets/en/39.png)

**!Note!**

Never trust a custodian Lightning solution to more value than you are willing to lose.

## Skill Summary:

In this section you learned:

- How to connect an internal or external Lightning node
- The contents and function of various Lightning-related tiles in the Dashboard
- How to configure Lightning wallet using Voltage Surge or Alby

## Knowledge assessment;

### KA 3.4.1 Practical Review

Describe some of the various options for connecting a Lightning wallet to your store: ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Objective 4: BTCPay Server Interface

**Dashboard overview**

**BTCPay Server Store settings**

**BTCPay Server Server settings**

**BTCPay Server Payments**

## Dashboard overview

BTCPay Server is a modular software package. However, there are standards that every BTCPay Server will have and the Administrator/users will interact with. Starting with the Dashboard. The main entry point of every BTCPay Server after logging in. The Dashboard gives an overview of how your store is performing, the wallet's current balance, and the last tx’s in the past 7 days. As it is a modular view, Plugins may utilize this view for their benefit and create their tiles on the Dashboard. For this course book, we will only talk about standard plugins/ apps and their respective views throughout BTCPay Server.

## Dashboard Tiles

Within the main view of the BTCPay Server dashboard are a couple of standard tiles available. These tiles are meant for the Store owner or Administrator to manage his store in one overview quickly.

- Wallet balance
- Transaction activity
- Lightning Balance (if Lightning is enabled on
the store)
- Lightning Services (if Lightning is enabled on
the store)
- Recent transactions.
- Recent Invoices
- Current active Crowdfunds
- Store performance / top-selling items.

## Wallet balance

The Wallet Balance tile gives a quick overview of your wallet’s funds and performance. It can be viewed in either BTC or Fiat currency in a Weekly, monthly, or yearly graph.

![image](assets/en/40.png)

## Transaction activity.

Next to the Wallet Balance tile, BTCPay Server shows a quick overview of Payouts pending, the amount of Transactions in the last 7 days, and if your store has issued any refunds. Clicking on the Manage button brings you into management for pending payouts (learn more about payouts in objective (4.4) ).

![image](assets/en/41.png)

## Lightning Balance ( Only visible when Lightning is activated )

When the Administrator has allowed Lightning network access, BTCPay Server dashboard now has a new tile with your Lightning node information. How much BTC is in channels, how this is balanced local or remote (inbound or outbound liquidity) if channels are closing or opening, and how much bitcoin is held on-chain on the lightning node.

![image](assets/en/42.png)

## Lightning Services ( Only visible when lightning is active )

Next to seeing your Lightning balance on BTCPay Server dashboard, administrators will also see the tile for Lightning Services. Here administrators can find quick buttons for tools they use to manage their Lightning node; for example, Ride the Lightning is one of the standard tools with BTCPay Server for Lightning node management.

![image](assets/en/43.png)

## Recent Transactions.

The recent transactions tile will show your store’s most recent transactions. With one click, the Administrator of the BTCPay Server instance can now see the latest transaction and see if attention is needed towards it.

![image](assets/en/44.png)

## Recent invoices

The recent invoices tile shows the 6 latest invoices generated by your BTCPay Server, including Status ( See objective (4.4) for details on invoice statuses ) and invoice amount. The tile also includes a “View all “button to access the full Invoice overview easily.

![image](assets/en/45.png)

## Point Of Sale and Crowdfunds.

As BTCPay Server delivers a set of standard plugins or apps, Point Of Sale and Crowdfund are the two main plugins of BTCPay Server. With every store and wallet, a BTCPay Server user may generate as many Point Of Sales or Crowdfunds as he sees fit. Each will create a new dashboard tile showing the plugins’ performance.

![image](assets/en/46.png)

Notice the slight difference between a Point of Sale and Crowdfund tile. The Administrator sees the top items sold in the Point of Sales tile. In the Crowdfund tile, this becomes Top Perks. Both tiles have quick buttons to manage the respective app and view recent invoices created by top items or top perks.

![image](assets/en/47.png)

**!?Note!?**

Balance graphs and recent transactions are available only for an on-chain payment method. Information about Lightning Network balances and transactions is on the to-do. As of BTCPay Server Version 1.6.0, basic Lightning Network balances are available.

## Skill Summary:

In this section, you learned the following:
- The core layout of tiles on the main landing page is known as the Dashboard.
- A basic understanding of the contents of each tile.

## Knowledge assessment;
### KA 4.1.1 Review

List as many tiles from memory as you can from the Dashboard: ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## BTCPay Server Store settings

Within the BTCPay Server software, we know of 2 types of settings. BTCPay Server Store-specific settings, the settings button found in the left menu bar below the Dashboard, and BTCPay Server settings, found at the bottom of the menu bar right above Account. The BTCPay Server Server-specific settings can only be viewed by Server administrators.

The store settings consist of many tabs to categorize each set of settings.

- General
- Rates
- Checkout Appearance
- Access Tokens
- Users
- Roles
- Webhooks
- Payout Processors
- Emails
- Forms

## BTCPay Server Store settings - General

### General

In the General Settings tab, store owners set their branding and payment defaults. At the initial setup of the store, a store name was given; this will be reflected in the General settings under Store Name. Here the store owner can also set their website to match branding and a Store ID for the Administrator to recognize in the database.

### Branding

As BTCPay Server is FOSS, a store owner can do custom branding to match his store. Set the brand color, store your brand’s logos, and add custom CSS for public/customer-facing pages (Invoices, Payment Requests, Pull payments)

### Payment

In the payments settings, store owners get to set their store default currency (either in Bitcoin or in any fiat currency).

### Allow anyone to create invoices

This setting is meant for developers or builders on top of BTCPay Server. With this setting switched on for your store, it enables the outside world to create invoices on your BTCPay Server instance.

### Add additional Fee (network fee) to invoices

A feature within BTCPay to protect merchants from dust attacks or clients to drive a high cost in fees later on when the merchant needs to move much bitcoin at once. For example, the customer created an invoice for $ 20$ and paid it partially, paying 1$ 20 times until the invoice was fully paid. The merchant now has a larger transaction, increasing the mining cost in case the merchant decides to move those funds later. By default, BTCPay applies an additional network cost to the total invoice amount to cover that expense for the merchant when the invoice is paid in multiple transactions. BTCPay offers several options to customize this protection feature. You can apply a network fee:

- Only if the customer makes more than one payment for the invoice (In the above example, if the customer created an invoice for 20$ and paid 1$, the total invoice due is now 19$ + the network fee. The network fee is applied after the first payment)
- On every payment (including the first payment, in our example, the total will be 20$ + network fee right away, even on the first payment)
- Never add network fee (disables the network fee entirely)

While it protects from dust transactions, it can also reflect negatively on businesses if not communicated properly. Customers may have additional questions and think you are overcharging them.

### Invoice expires if the full amount has not been paid after ?

The invoice timer is set to 15 minutes by default. The timer is a protection mechanism against volatility since it locks the Bitcoin amount according to the Bitcoin to fiat rates. If the customer does not pay the invoice within the defined period, the invoice is considered expired. The invoice is considered “paid” as soon as the transaction is visible on the blockchain (0-confirmations) but considered “complete” when it reaches the number of confirmations the merchant defined (usually, 1-6). The timer is customizable by minutes.

### Consider the invoice paid even if the paid amount is X% less than expected?

When a customer uses an exchange wallet to pay directly for an invoice, the exchange takes a small fee. This means that such an invoice is not considered fully completed. The invoice gets the status “paid partially.” You can set the percentage rate here if a merchant wants to accept underpaid invoices.

## BTCPay Server Store settings - Rates

In BTCPay Server, when an invoice gets generated, it always needs the most up-to-date and accurate Bitcoin to fiat price. When creating a new store in BTCPay Server, administrators get asked to set their preferred price source; after the store is set up, store owners can always change their price source in this tab.

### Advanced rate rule scripting

Mainly used by power users. If toggled on, store owners can create scripts around price behavior and how to charge their customers.

### Testing

A quick testing place for your preferred currency pairs. This also includes a feature to check default currency pairs via REST query.

## BTCPay Server Store settings - Checkout Appearance

The checkout Appearance tab begins with invoice-specific settings and a default payment method and enables specific payment methods when set requirements are met.

### Invoice settings

Default payment methods. BTCPay Server in a standard configuration has three options.

- BTC(on-chain)
- BTC(LNURL-pay)
- BTC(Off-chain)(Lightning)

We can set parameters for our store, where a customer only will interact with Lightning when the price is less than X amount and vice versa for On-chain transactions when X is greater than Y always present the On-chain payment option.

![image](assets/en/48.png)

### Checkout

As of BTCPay Server release 1.7, it was introduced to a new Checkout interface, Checkout V2, as it is called. Since release 1.9 was standardized, administrators and store owners can still set the checkout to the previous release. By using the toggle “Use the classic checkout,” a store owner can set the store back to the previous checkout experience. BTCPay Server also has a select set of presets for Online commerce or an in-store experience.

![image](assets/en/49.png)

When a customer interacts with the store and generates an invoice, there is an expiration time for the invoice. By default BTCPay Server sets this to 5 minutes, and the Administrator can set this to whatever they see fit. The checkout page can further be customized by checking the following parameters:

- Celebrate payment by showing confetti
- Show the store header (Name and logo)
- Show the “Pay in wallet” button
- Unify on-chain and off-chain payments URL/QRs
- Display Lightning payment amounts in Satoshis
- Auto-detect language on checkout

![image](assets/en/50.png)

When Auto-detect language is not set, BTCPay Server, by default, will display English. A store owner can change this default to their preferred language. Click on the Drop down and

![image](assets/en/51.png)

Store owners can set a Custom HTML title to be displayed on the checkout page.

![image](assets/en/52.png)

To ensure the customer knows his payment method, a store owner can explicitly set his checkout always to require the users to choose their preferred payment method. When the invoice is paid for, BTCPay Server allows the customer to return to the webshop. Store owners can set this redirect after the customer has paid automatically.

![image](assets/en/53.png)

### Public receipt

Within the public receipt settings, a store owner can set the receipt pages to the public and show the payment list on the receipt page and the QR code of the receipt for the customer to access it digitally easily.

![image](assets/en/54.png)

## BTCPay Server Store settings - Access Tokens

Access tokens are used for pairing to certain e-commerce integration's or custom build integration's.

![image](assets/en/55.png)

## BTCPay Server Store settings - Users

Store users are where the store owner can manage his staff members, their accounts, and access to the store. After staff members create their accounts, the store owner can add specific users to the store as Guest users or owners. To further define the staffer’s role, refer to the next section on “BTCPay Server Store settings - Roles.”

![image](assets/en/56.png)

## BTCPay Server Store settings - Roles

A store owner might not find the user’s standard roles significant enough. In the custom roles settings, a store owner can define the exact needs for each role in his business.

1. To create a new role, Click the “+ Add role button.“
![image](assets/en/57.png)

2. Enter a Role name, for example, “Cashier. “
![image](assets/en/58.png)

**!?Note!?**

3. Configure the individual permissions for the role.
- Modify your stores.
- Manage exchange accounts linked to your stores.
    - View exchange accounts linked to your stores.
- Manage your pull payments.
- Create pull payments.
    - Create non-approved pull payments.
- Modify invoices.
    - View invoices.
    - Create an invoice.
    - Create invoices from the lightning nodes associated with your stores.
- View your stores.
    - View invoices.
    - View your payment requests.
    - Modify stores’ webhooks.
- Modify your payment requests.
    - View your payment requests.
- Use the lightning nodes associated with your stores.
    - View the lightning invoices associated with your stores.
    - Create invoices from the lightning nodes associated with your stores.
- Deposit funds to exchange accounts linked to your stores.
- Withdraw funds from exchange accounts to your store.
- Trade funds on your store’s exchange accounts.

When the role gets created, the name is fixed and cannot be changed after in the edit mode.

![image](assets/en/59.png)

## BTCPay Server Store settings - Webhooks

Within BTCPay Server, it's reasonably easy to make a new “Webhook”. In the BTCPay Server Store settings - Webhooks tab, a store owner can easily create a new webhook by clicking on the “ + Create Webhook”. Webhooks allow BTCPay Server to send HTTP events related to your store to other servers or ecommerce integrations.

![image](assets/en/60.png)

You're now in the view for creating a Webhook. Make sure you know your Payload URL and paste this into your BTCPay Server. While you pasted the payload URL, underneath it shows the webhook secret. Copy the webhook secret and provide it on the endpoint. When everything has been set, you can toggle in BTCPay Server to Automatical redelivery. We will try to redeliver any failed delivery after 10 seconds, 1 minute, and up to 6 times after 10 minutes. You can toggle between every event or specify the events for your needs. Be sure to enable the webhook and hit the Add webhook to save it.

![image](assets/en/61.png)

Webhooks are not meant to be compatible with Bitpay API. There's two separate IPNs (in BitPay terms: "Instant Payment Notifications") in BTCPay Server.
- Webhookp
- Notifications

Only use Notification URL when you create invoices through Bitpay api.

## BTCPay Server Store settings - Payout Processors

Payout processors work together with the Payouts concept in BTCPay Server. A payout aggregator to batch multiple transactions and send them at once; learn more about payouts in objective (4.4). With payout processors, a store owner can automate the batched payouts. BTCPay Server provides two methods of automated payouts, On-chain and Off- chain (LN).

The store owner can click and configure both payout processors separately. A store owner might only want to run the on-chain processor once every X hours, whereas off-chain might go every few minutes. For On-chain, you may also set a target for which block it should be included. Per default, this is set to 1 (or the next block available). Notice that setting the Off-chain payout processor only has the interval timer and no block target. Lightning network payments are instant.

![image](assets/en/62.png) ![image](assets/en/63.png)

Store owners can only configure the on-chain processor if they have a Hot-wallet connected to their store.

![image](assets/en/64.png)

After setting up a Payout processor, you can quickly remove or modify it by returning to the Payout processor tab in BTCPay Server Store settings.

**!?Note!?**

Payout processor on-chain - The onchain payouts processor can only work on a store configured with a Hot wallet connected. If there is no hot wallet connected, BTCPay Server does not hold the keys to the wallet and won’t be able to automatically process the payouts.

## BTCPay Server Store settings - Emails

BTCPay Server can use Emails for Notifications or, when set correctly, to recover accounts that were made on the instance, as standard BTCPay Server does not send an email when the password is lost, for example.

![image](assets/en/65.png)

Before a store owner can set Email rules to fire off on specific events of his store, we have to set up some basic email settings. BTCPay Server needs these settings to send emails for events based on your store or for password resets.

BTCPay Server made it easier to fill out this information by using the “Quick Fill” Option0
- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

By using the quick fill option, BTCPay Server will pre-populate the fields for the SMTP server and port; now, the store owner only needs to fill out his credentials in an Email address, Login (which is usually equal to your email address), and your password. The advanced option BTCPay Server offers in the email settings is to Disable TLS Certificate security checks; by default, this is Enabled.

![image](assets/en/66.png)

With Email rules, a store owner can set specific events to trigger emails to specific email addresses.
- Invoice Created
- Invoice Received Payment
- Invoice Processing
- Invoice Expired
- Invoice Settled
- Invoice Invalid
- Invoice Payment Settled

If the customer has provided an Email address, these triggers can also send the information to the customer. Store owners can pre-fill the Subject line to make clear why this Email happened and what trigger caused it.

![image](assets/en/67.png)

## BTCPay Server Store settings - Forms

As BTCPay Server does not gather any data, a store owner might want to add a custom form to their checkout experience; this way, the store owner can gather additional information from his customer. BTCPay Server Form builder consists of two parts, a visual and more advanced code view of the forms.

When creating a new form, BTCPay Server opens a new window requesting basic information on what you want your new form to request. At first, the store owner needs to give a clear name to their new form, this name CANNOT be changed after setting it.

![image](assets/en/68.png)

After the store owner gives the form a name, you may also toggle the switch for “Allow form for public use “to ON, and it becomes green. This is so the form gets used in every customer-facing place. For example, if a store owner creates 1 separate invoice not through his Point Of Sale, he might still want to gather the info from the customer; this toggle to ON allows for that info to be gathered.

![image](assets/en/69.png)

Every form starts with at least 1 New form field. A store owner can pick what the type of field should be;

- Text
- Number
- Password
- Email
- URL
- Telephone numbers
- Date
- Hidden fields
- Fieldset
- A text area for open comments.
- Option selector

Every type comes with its parameters to fill. The store owner can set it to his liking. Below the first created field, store owners can keep adding new fields to this one form.

![image](assets/en/70.png)

### Advanced custom forms.

BTCPay Server also allows you to build Forms in code. JSON, in particular. Instead of looking at the editor, store owners can click on the CODE button right next to the editor and get into the code of their Forms. In a field definition, only the following fields can be set; the values of the fields are stored in the metadata of the invoice:

|      Field       | Description                                          |
| ---------------- | ---------------------------------------------------- |
| .fields.constant | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)  |
| .fields.type | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel|
| .fields.options | If .fields.type is select, the list of selectable values     |
| .fields.options.text  | The text displayed for this option |
| .fields.options.value | The value of the field if this option is selected|
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)|
| .fields.name| The JSON property name of the field as it will appear in the invoice's metadata|
| .fields.value | The default value of the field|
| .fields.required| if true, the field will be required|
| .fields.label |The label of the field|
| .fields.helpText | Additional text to provide an explanation for the field.|
| .fields.fields | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address.|

The field name represents the JSON property name that stores the user- provided value in the invoice’s metadata. Some well-known names can be interpreted and modify the invoice’s settings.

|    Field name    | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

You can pre-fill the fields of an invoice automatically by adding query strings to the form’s URL, such as “?your_field=value”.

Here are some use cases for this feature:
- Assisting user input: Pre-fill fields with known customer information to make it easier for them to complete the form. For example, if you already know a customer’s email address, you can pre-fill the email field to save them time.
- Personalization: Customize the form based on customer preferences or segmentation. For instance, if you have different customer tiers, you can pre-fill the form with relevant data, such as their membership level or specific offers.
- Tracking: Track the source of customer visits using hidden fields and pre-filled values. For example, you can create links with pre-filled utm_media values for each marketing channel (e.g., Twitter, Facebook, Email). This helps you analyze the effectiveness of your marketing efforts.
- A/B testing: Pre-fill fields with different values to test different form versions, enabling you to optimize the user experience and conversion rates.

## Skill Summary:

In this section, you learned the following:
- The layout and functions of the tabs in the Store Settings
- A multitude of options for fine-tuning the handling of underlying exchange rates, partial payments, slight underpayments, and more.
- Customize the checkout appearance, including price-dependent main chain vs. Lightning enablement on invoices.
- Manage levels of store access and permissions across roles.
- Configure automated emails and their triggers
- Create custom forms for gathering additional customer information at checkout.

## Knowledge assessment;
### KA 4.2.1 Review

What is the difference between Store Settings and Server Settings: __________________________________________________________________________________________________________________________________________________________________________________________________________________________

### KA 4.2.2 Hypothetical

Describe some options you might select in Checkout Appearance > Invoice Settings, and why: ____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## BTCPay Server - Server settings

BTCPay Server consists of two different settings views. One is dedicated to Store settings and another for Server settings. The latter is only available if you are a Server administrator and not for store owners. Server administrators can add users, create custom roles, configure the email server, set policies, run maintenance tasks, check all services attached to BTCPay Server, upload files to the server, or check Logs.

## BTCPay Server settings - Users

As mentioned in objective (2.1, Account creation by Server administrator), Server Administrators can invite users to their server by adding them to the Users tab.

## BTCPay Server settings - Server wide custom Roles

BTCPay Server knows two sorts of custom roles, the store-specific custom roles (objective 4.2 BTCPay Server Store settings - Roles) and server-wide Custom roles in the BTCPay Server settings. Both hold a similar set of permissions; however, if set through the BTCpay Server Settings - Roles tab, the applied role will be server-wide and apply to multiple stores. Notice a “Server-wide” tag to the custom roles in Server settings.

![image](assets/en/71.png)

## BTCPay Server Server settings - Server wide custom Roles

Server-wide custom roles permission set;
- Modify your stores.
- Manage exchange accounts linked to your stores.
    - View exchange accounts linked to your stores.
- Manage your pull payments.
- Create pull payments.
    - Create non-approved pull payments.
- Modify invoices.
    - View invoices.
    - Create an invoice.
    - Create invoices from the lightning nodes associated with yourstores.
- View your stores.
    - View invoices.
    - View your payment requests.
    - Modify stores’ webhooks.
- Modify your payment requests.
    - View your payment requests.
- Use the lightning nodes associated with your stores.
    - View the lightning invoices associated with your stores.
    - Create invoices from the lightning nodes associated with your stores.
- Deposit funds to exchange accounts linked to your stores.
- Withdraw funds from exchange accounts to your store.
- Trade funds on your store’s exchange accounts.

**!?Note!?**

When the role gets created, the name is fixed and cannot be changed after in the edit mode.

## BTCPay Server settings - Email

The Server-wide Email settings look similar to those in the Store-specific email settings (objective 4.2 BTCPay Server Store settings - Emails). However, this setup handles not only triggers for stores or administrator logs. This Email setup also makes password recovery available on BTCPay Server at Login. It works similarly to the Store-specific settings; administrators can Quickly fill in their Email parameters and enter their email credentials, and the server can now send emails.

![image](assets/en/72.png)

## BTCPay Server settings - Policies

BTCPay Server policy administrators can set some settings on topics like Existing User settings, New Users Settings, Notifications settings, and Maintenance settings. These are meant for registering new users as admin or normal users or even hiding BTCPay Server from search engines by adding to your server header.

![image](assets/en/73.png)

### Existing user Settings

The options available here are separate from custom roles. These extra permissions might make a store or store owner vulnerable to attacks. Policies that may be added to existing users:
- Allow non-admins to use the internal Lightning node in their stores.
    - This would allow store owners to use the server Administrator’s Lightning node and, therefore, his funds! Beware, this is not a solution to giving access to Lightning.
- Allow non-admins to create hot wallets for their stores.
    - This would allow anyone with an account on your BTCPay Server instance to create Hot-wallets and store their recovery seed on the Administrator’s server. This might make the Administrator liable for holding third party their funds!
- Allow non-admins to import hot wallets for their stores.
    - Similar to the previous topic of creating Hot wallets, this policy allows importing a hot wallet, with the same dangers mentioned in the creating hot wallets section.

![image](assets/en/74.png)

### New user settings 

We can set some important settings to manage new users coming to the server. We can set a confirmation email for new registrations, Disable new user creation through the login screen, and restrict non-admins access to user creation over the API.

- Require a confirmation email for registering.
    - The server administrator has to have set up an Email server!
- Disable new user registration on the server
- Disable non-admins access to the user creation API endpoint.

By default, BTCPay Server has toggled on Disable new user registration and turned off the non-admins access to the user creation API endpoint. This is out of a security aspect where no random person who might have found the BTCPay Login of your server can start creating accounts.

![image](assets/en/75.png)

### Notification Settings.

![image](assets/en/76.png)

### Maintenance Settings.

BTCPay Server is an Open Source project that lives on GitHub. Whenever BTCPay Server releases a new version of the software, Administrators can be notified that a new version is available. Administrators may also want to discourage search engines (google, yahoo, duckduckgo) from indexing the BTCPay Server domain. As BTCPay Server is FOSS, developers worldwide might want to create new features; BTCPay Server has an experimental feature when toggled on, and an administrator can use features not meant for production yet, purely for testing purposes.

- Check releases on GitHub and notify when a new BTCPay Server version is available.
- Discourage search engines from indexing this site
- Enable experimental features.

![image](assets/en/77.png)

### Plugins.

BTCPay Server can add Plugins and expand its feature set. The plugins, by default, are loaded from the BTCPay Server plugin-builder repository. An administrator, however, may choose to see plugins in a Pre-release state, and if the plugin developer allows it, the server administrator can now install beta versions of plugins.

![image](assets/en/78.png)

### Customization Settings.

A standard BTCPay Server deployment will be reachable through the domain set up for it at installation. However, a server administrator can remap the root domain and display one of the created apps from a specific store. The Server Administrator can also map specific domains to specific apps.

- Display the app on the website’s root
    - Displays list of possible apps to show on the root domain.

![image](assets/en/79.png)

- Map specific domains to specific apps.
    - When you click to set up a specific domain for specific apps, the Administrator can set as many domains pointed to specific apps as needed.

![image](assets/en/80.png)

### Block explorers.

BTCPay Server, as standard, comes with mempool.space as its Block explorer for transactions. When BTCPay Server generates a new invoice, and there is a transaction tied to it, the store owner can click to open the transaction; BTCPay Server will standard point towards mempool.space as a block explorer; a server Administrator may change this to his preference.

![image](assets/en/81.png)

## BTCPay Server settings - Services

The BTCPay Server settings: Services tab is an overview of components your BTCPay Server uses. The services your BTCPay Server exposes might vary depending on the deployment method.

A BTCPay Server Administrator can click on the “See information “behind each service to open it and set specific settings.

![image](assets/en/82.png)

### LND (gRPC)

BTCPay exposes LND’s GRPC service for outside consumption; you will find connection information in this specific settings menu; compatible wallets are listed here. BTCPay Server also gives a QR code for connection to scan and apply in the mobile wallet.


Server administrators can open more details to see;

- Host details
- Use of SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)

### LND (REST)

BTCPay exposes LND’s REST service for outside consumption; you will find connection information here; compatible wallets are listed here. Among the compatible wallets are Joule, Alby, and ZeusLN. BTCPay Server gives a QR code for connection, scan and apply in the compatible wallet.

- REST Uri
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon

### LND Seed Backup

The LND seed backup is useful to recover funds from your LND wallet in case of a corruption of your Server. As the Lightning node is a Hot-wallet, you can find the confidential seed information on this page.

LND documents the recovery process. See https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md for documentation.

### Ride The Lightning

Ride the Lightning is a Lightning node management tool built as Open Source software. BTCPay Server uses RTL as the Lightning node management component in its stack. BTCPay Server administrators can reach RTL through the Server settings - Services tab or by clicking on the Lightning wallet.

### Full node P2P

Server administrators may want to connect their Bitcoin node to a mobile wallet. This page exposes information to connect remotely to your full node via the P2P protocol. As of writing this book, BTCPay Server lists Blockstream Green and Wasabi wallet as compatible wallets. BTCPay Server gives a QR code for connection, scan and apply in the compatible wallet.

### Full node RPC

This page exposes information to connect remotely to your full node via the RPC protocol.

### SSH

SSH is used for maintenance purposes. BTCPay Server shows the initial connection command to reach your Server and SSH public keys authorized to connect to your Server. Server Administrators might want to turn off SSH changes through the UI of BTCPay Server.

### Dynamic DNS.

Dynamic DNS allows you to have a stable DNS name pointing to your Server, even if your IP address changes regularly. This is recommended if you are hosting BTCPay Server at home and wish to have a clearnet domain to access your Server.

Note that you need to properly configure your NAT and BTCPay Server installation to get the HTTPS certificate.

## BTCPay Server settings - Theme

### Theme.

BTCPay Server, as standard, comes with two themes: Light and Dark modes. These can be switched by Clicking on Account in the bottom left and toggling between Dark theme or Light theme. BTCPay Server administrators may add their theme by providing a custom CSS theme.

Administrators can extend the Light/Dark theme by adding their own custom CSS or setting their custom theme as a full custom.

![image](assets/en/83.png)

### Server Branding

Server administrators can change the BTCPay Server branding by setting a Server-wide branding of your company. As BTCPay Server is FOSS, server administrators can white label the software and change the look to suit their business.

![image](assets/en/84.png)

## BTCPay Server settings - Maintenance

As a server administrator, your users expect you to take good care of the Server. Within BTCPay Server’s Maintenance tab, the admin can do some essential maintenance. Set the domain name to the BTCPay Server instance, Restart or clean up the Server. Possibly most important, run updates.

BTCPay Server is an Open Source project and updates frequently. Every new release is announced by either your BTCPay Server Notifications or on the official Channels BTCPay Server communicates through.

![image](assets/en/85.png)

### Domain name

After BTCPay Server is set up, an administrator might want to change away from his original Domain. Within the Maintenance tab, the administrator can change the Domain. After clicking confirm and setting up the proper DNS records on the Domain, BTCPay Server updates and restarts to return to the new Domain.

![image](assets/en/86.png)

### Restart

Restart BTCPay Server and related services.

![image](assets/en/87.png)

### Clean

BTCPay Server runs with Docker components; with updates, there might be leftovers of Docker images, temp files, etc. Server Administrators can clean this up and recoup space on their environment by running the Clean script.

![image](assets/en/88.png)

### Update

Possibly the most important option in the Maintenance tab. BTCPay Server is built by the community, and therefore, its update cycles are more frequent than most software products. When BTCPay Server has a new release, administrators will be notified in their notification center. By clicking the update button, BTCPay Server will check GitHub for the latest release, update the Server and restart. Before updating, server administrators are always advised to read the release notes distributed through the official channels of BTCPay Server.

![image](assets/en/89.png)

## BTCPay Server settings - Logs

Facing a problem is never fun. This document explains the most common workflow and steps to efficiently identify your issue and solve it yourself or with community help.

Identifying the problem is crucial.

### 1. Replicating the issue
First and foremost, try to determine when the issue happens. Try to replicate the problem. Try to update and restart your Server to verify that you can reproduce your issue. If it describes your issue better, take a screenshot.

### 1.1 Updating the server

Check your version of BTCPay Server if it is much older than the [latest version](https://github.com/btcpayserver/btcpayserver/releases) of BTCPay Server. Updating your Server may resolve the issue.

### 1.2 Restarting the server

Restarting your Server is an easy way to solve many of the most common BTCPay Server issues. You may need to SSH into your Server to restart it.

### 1.3 Restarting a service

You may only need to restart a particular service in your BTCPay Server deployment for some issues. Such as restarting the lets encrypt container to renew the SSL certificate.

sudo su -

cd btcpayserver-docker

docker restart letsencrypt-nginx-proxy-companion

Use docker ps to find the name of a different service you would like to restart.

### 2. Looking through the logs

Logs can provide an essential piece of information. In the following paragraphs, we will describe how to get the log information for various parts of BTCPay.

### 2.1 BTCPay Logs

Since v1.0.3.8, you can easily access BTCPay Server logs from the front end. If you are a server admin, go to Server Settings > Logs and open the logs file. If you do not know what a particular error in the logs means, mention it when troubleshooting.

If you want more detailed logs and are using a Docker deployment, you can view logs of specific Docker containers using the command line. See these [instructions to ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) into an instance of BTCPay running on a VPS.

On the next page, a general list of the container names used for BTCPay Server.

Run the commands below to print logs by container name. Replace the container name to view other container logs.

sudo su -

cd btcpayserver-docker

docker ps

docker logs --tail 100 generated_btcpayserver_1

| Logs for         | Container Name                                       |
| ---------------- | ---------------------------------------------------- |
| BTCPayServer     | generated_btcpayserver_1                             |
| NBXplorer        | generated_nbxplorer_1                                |
| Bitcoind         | btcpayserver_bitcoind                                |
| Postgres         | generated_postgres_1                                 |
| proxy            | letsencrypt-nginx-proxy-companion                    |
| Nginx            | nginx-gen                                            |
| Nginx            | nginx                                                |
| c-lightning      | btcpayserver_clightning_bitcoin                      |
| LND              | btcpayserver_lnd_bitcoin                             |
| RTL              | generated_lnd_bitcoin_rtl_1                          |
| Thunderhub       | generated_bitcoin_thub_1                             |
| LibrePatron      | librepatron                                          |
| Tor              | tor-gen                                              |
| Tor              | tor                                                  |

### 2.2.1 - Lightning Network LND - Docker

There are a few ways to access your LND logs when using Docker. First log in as root:

sudo su -

Navigate to the correct directory:

cd btcpayserver-docker

Find container name:

docker ps

Print logs by container name:

docker logs --tail 100 btcpayserver_lnd_bitcoin

Alternatively, you can quickly print logs by using container ID (only the first unique ID characters are needed, such as the two furthest left characters):

docker logs 'add your container ID '

If for any reason you need more logs

sudo su -

cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/ bitcoin/mainnet/

inside that directory do ls

You will see something like lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz

To access uncompressed logs of those logs do cat lnd.log or if you want another one, use cat lnd.log.15

To access compressed logs in .gzip use gzip -d lnd.log.16.gz (in this case we're accessing lnd.log.16.gz) This should give you a new file, where you can do cat lnd.log.16 . In case the above does not work, you may need to use install gzip first sudo apt-get install gzip

### 2.2.2 - Lightning Network c-lightning - Docker

sudo su -

docker ps

Find the c-lightning container ID.

docker logs 'add your container ID here'

alternatively, use this

docker logs --tail 100 btcpayserver_clightning_bitcoin

You can also get log information with c-lightning cli command.

bitcoin-lightning-cli.sh getlog

### 2.3 - Bitcoin Node Logs

In addition to [looking at logs](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) of your Bitcoind container, you can also use any of the [bitcoin-cli commands](https://developer.bitcoin.org/reference/rpc/index.html)

[(opens new window)](https://developer.bitcoin.org/reference/rpc/index.html) to obtain information from your bitcoin node. BTCPay includes a script to allow you to communicate with your Bitcoin node easily.

Inside the btcpayserver-docker folder, get the blockchain information using your node:

bitcoin-cli.sh getblockchaininfo

## BTCPay Server settings - Files

BTCPay Server has a local file system and uploads Store (product) assets, Logos, and branding directly to the Server. The Server’s file system is only accessible by Server Administrators; store owners can upload their logos/ branding at the store level.

When the Server administrator is in the File Storage tab, it is possible to directly upload to your Server or change the file storage provider to a Local file system or Azure Blob Storage.

![image](assets/en/90.png)

![image](assets/en/91.png)

## Skill Summary:

In this section, you learned the following:

- The difference between Store and Server settings, in particular as they relate to Users, Roles, and Emails
- Set server-wide policies for Lightning or Bitcoin hot wallet use and creation, new user registration, and email notifications.
- <stuff about services, but I did not fully understand this stuff enough to write a skill about it>
- How to add custom themes (instead of simple light/dark options provided) as well as create custom logos
- Perform simple server maintenance tasks via the GUI provided
- Troubleshoot issues, including fetching details for any of the Docker containers or your node
- Manage file storage

## Knowledge assessment;

### KA 4.3.1 Conceptual Review

What is the difference in Roles assigned through Server vs Store Settings, and what describe a potential use for one over the other: __________________________________________________________________________________________________________________________________________________________________________________________________________________

### KA 4.3.2 Practical Review

Describe some possible use cases enabled in the Policies tab: __________________________________________________________________________________________________________________________________________________________________________________________________________________

### KA 4.3.3 Practical Review

Describe some actions an administrator might routinely make in the Maintenance tab: __________________________________________________________________________________________________________________________________________________________________________________________________________________

## Objective 4.4; 
## BTCPay Server - Payments

An invoice is a document the seller issues to a buyer to collect payment.

In BTCPay Server, an invoice represents a document that must be paid within a defined time interval at a fixed exchange rate. Invoices have expiration because they lock the exchange rate within a specified time frame to protect the receiver from price fluctuations.

The core of BTCPay Server is the ability to act as a Bitcoin invoice management system. An invoice is an essential tool for tracking and managing a received payment.

Unless you use a built-in [Wallet](https://docs.btcpayserver.org/Wallet/) to receive payments manually, all payments within a store will be shown on the Invoices page. This page cumulatively sorts payments by date and is a central piece for invoice management and payment troubleshooting.

![image](assets/en/92.png)

## BTCPay Server Store settings - General
### Invoice statuses

The table below lists and describes standard invoice statuses in BTCPay and suggests common actions. Actions are just recommendations. It’s up to users to define the best course of action for their use case and business.

| Invoice Status           | Description                                            | Action                   |
| ------------------------ | ------------------------------------------------------ | ------------------------ |
| New                      | Not paid, invoice timer still has not expired          | None |
| New (paidPartial)        | Paid, not in full, invoice timer still has not expired | None |
| Expired                  | Not paid, invoice timer expired                        | None |
| Expired (paidPartial) ** | Paid, not in full amount, and expired                  | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark invoice as settled or invalid |
| Expired (paidLate)       | Paid, in full amount, after the invoice timer has expired | Contact buyer to arrange a refund or process order if late confirmations are acceptable. |
| Settled (paidOver)       | Paid more than the invoice amount, settled, received sufficient amount of confirmations | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Processing               | Paid in full, but has not received sufficient amount of confirmations specified in the store settings | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Processing (paidOver)    | Paid more than the invoice amount, not received sufficient amount of confirmations | Wait to be settled then contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                  | Paid, in full, received sufficient amount of confirmations in store | Fulfil the order |
| Settled (marked)         | Status was manually changed to settled from an processing or invalid status | Store admin has marked the payment as settled |
| Invalid*                 | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled |
| Invalid (marked)         | Status was manually changed to invalid from a settled or expired status | Store admin has marked the payment as invalid |
| Invalid (paidOver)       | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled |

### Invoice details

The invoice details page contains all information related to an invoice.

Invoice information is created automatically based on invoice status, exchange rate, etc. Product information is created automatically if the invoice was created with product information, such as in the Point of Sale app.

### Invoice filtering


Invoices can be filtered via the quick filters located next to the search button or the advanced filters, which can be toggled by clicking the (Help) link on the top. Users can filter invoices by store, order id, item id, status, or date.

### Invoice export

BTCPay Server Invoices can be exported in CSV or JSON format. For more information about invoice export and accounting.

### Refunding an invoice

If, for any reason, you would like to issue a refund, you can easily create a refund from the invoice view.

### Archiving invoices

As a result of the no address re-use feature of BTCPay Server, it is common to see many expired invoices on your store’s invoice page. To hide them from your view, select them in the list and mark them as archived. Invoices that have been marked as archived are not deleted. Payment to an archived invoice will still be detected by your BTCPay Server (paidLate status). You can view the store’s archived invoices at any time by selecting archived invoices from the search filter dropdown.

### Default Currency

Store default currency, this was set at the store creation wizard

### Allow anyone to create invoice.

You should enable this option if you want to allow the outside world to create invoices in your store. This option is only useful if you're using the payment button or if you are issuing invoices via API or 3rd party HTML website. PoS app is pre-authorised and does not need this enabled for a random visitor to open your POS store and create an invoice.

### Add Additional fee (network fee) to invoice..

- Only if the customer makes more than one payment for the invoice
- On every payment
- Never add network fee

### Invoice expires if the full amount has not been paid after .. Minutes.

The invoice timer is set to 15 minutes by default. The timer is a protection mechanism against the volatility since it locks the cryptocurrency amount according to the crypto to fiat rates. If the customer does not pay the invoice within the defined period, the invoice is considered expired. The invoice is considered "paid" as soon as the transaction is visible on the blockchain (o-confirmations) but considered "complete" when it reaches the number of confirmations the merchant defined (usually, 1-6). The timer is customizable.

### Consider the invoice paid even if the paid amount is ..% less than expected.

In a situation where a customer uses an exchange wallet to pay directly for an invoice, the exchange takes a small amount of fee. This means that such invoice is not considered fully completed. The invoice gets status "paid partially." If a merchant wants to accept underpaid invoices, you can set the percentage rate here

## BTCPay Server Payments - Requests

Payment Requests are a feature that allows BTCPay store owners to create long-lived invoices. Funds are paid to a payment request using the exchange rate at the time of payment. This allows users to make payments at their convenience without negotiating or verifying exchange rates with the store owner at the time of payment.

Users can pay requests in partial payments. The payment request will remain valid until it is paid in full or if the store owner requires an expiration time. Addresses are never re-used. A new address is generated each time the user clicks pay to create an invoice for the payment request.

Store owners can print payment requests (or export invoice data) for record-keeping and accounting. BTCPay automatically labels invoices as Payment Requests in your store’s invoice list.

### Customize Your Payment Requests
- Invoice Amount - Set Requested Payment Amount
- Denomination - Show Requested Amount in Fiat or Cryptocurrency
- Payment Quantity - Allow only single payments or partial payments
- Expiration Time - Allow payments until a date or without expiry
- Description - Text Editor, Data Tables, Embed Photos & Videos
- Appearance - Color and Style with CSS Themes

# Objective 5: BTCPay Server Default Plugins
# Objective 6: Configuring BTCPay Server 