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

If you are unable to connect to your Lightning node, try restarting your server, or read for more details on BTCPay Server official documentation; https:// docs.btcpayserver.org/Troubleshooting/ . You cannot accept lightning payments in your store until your Lightning node appears "Online". Try to test your Lightning connection by clicking the "Public Node Info" link

# Objective 4: BTCPay Server Interface
# Objective 5: BTCPay Server Default Plugins
# Objective 6: Configuring BTCPay Server 