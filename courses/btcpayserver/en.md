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

# Objective 4: BTCPay Server Interface
# Objective 5: BTCPay Server Default Plugins
# Objective 6: Configuring BTCPay Server 