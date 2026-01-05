---
name: Bitcoin Keeper - Inheritance plan
description: Plan your bitcoin transmission with Bitcoin Keeper
---

![cover](assets/cover.webp)


The transfer of Bitcoin assets is one of the challenges most underestimated by holders. Unlike a bank account, where the financial institution can pass on the funds to the rightful heirs, Bitcoin relies entirely on the possession of private keys. A perfectly legitimate legal heir will never be able to access the funds without these keys, while a malicious individual in possession of the secrets will be able to spend them without any formality.


In this second Bitcoin Keeper tutorial, we explore the premium features dedicated to estate planning. The application offers advanced tools for creating Enhanced Vaults, with timed protection mechanisms thanks to Miniscript, as well as accompanying documents to guide your loved ones.


This guide assumes that you have already mastered the basics of Bitcoin Keeper (portfolio creation, classic multisig, adding hardware keys) as explained in our first tutorial :


https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)


## Bitcoin Keeper subscription plans


Bitcoin Keeper operates on a freemium model with three subscription levels offering progressive functionality. To access the plans, go to the **More** tab, then tap on your current plan (default is "Pleb") to open the **Manage Subscription** screen.


![Plans d'abonnement](assets/fr/01.webp)


The **Pleb plan** (free) provides access to the essentials: unlimited creation of single-key and multi-key wallets, compatibility with all major hardware wallets (Coldcard, Trezor, Ledger, Jade, Tapsigner...), coin control, labeling, and connection to a personal Electrum server. This plan is sufficient for standard use and even for classic multi-sig configurations.


The **Hodler plan** (€9.99/month, with 1 month free if paid annually) includes all Pleb features and adds encrypted backups to the cloud (iCloud or Google Drive) to restore your safes on any device, Server Key to add automatic spending policies and 2FA above a certain threshold, and Canary Wallets to detect unauthorized access to your keys.


The **Diamond Hands plan** (€29.99/month, with 1 month free if paid annually) is the complete package for estate planning. It includes the entire Hodler plan and unlocks the Inheritance Key (deferred activation), the Emergency Key (emergency key for recovery in case of loss), the Inheritance Planning tools and documents, and a support call with the Concierge team to validate your configuration. This is the offer for bitcoiners who wish to pass on their inheritance over several generations.


Important point: the vaults you've created will remain accessible even if you switch back to the free plan. Your configurations are based on open standards (BSMS, Miniscript) and operate independently of your subscription.


## Inheritance documents


Once you have activated your Diamond Hands subscription, access the **Inheritance Documents** section from the More tab. Bitcoin Keeper provides five sample documents to structure your estate plan, as well as a tips section:


![Documents d'héritage](assets/fr/02.webp)



- Seed Words Template**: a template for neatly jotting down your recovery phrases in an organized fashion
- Trusted Contacts**: a template for listing the contact details of trusted persons involved in your plan (notary, lawyer, heirs, key keepers)
- Additional Share Key**: a document detailing the technical information for each key: PIN code, derivation path, physical location, device type, and any other information useful for identifying and using the key
- Recovery Instructions**: step-by-step instructions for the heir or beneficiary to recover funds
- Letter to Attorney**: a pre-filled letter that can be adapted for your lawyer or notary


The **Inheritance Tips** section offers practical advice on securing keys for heirs and optimizing your inheritance plan.


Customize these documents to suit your situation, and keep them in a safe place, separate from the keys themselves.


## Configuring Cloud Backup


Before creating your legacy vault, activate cloud backup to protect your configuration files. From the More tab, press **Personal Cloud Backup**.


![Configuration Cloud Backup](assets/fr/03.webp)


Choose a strong password to encrypt your backups. This password protects only the wallet configuration files (not your private keys). Confirm the password and press **Confirm**. Your backups will be stored on your iCloud or Google Drive depending on your device. Press **Backup Now** to launch your first backup.


## Import your hardware keys


For our example, we'll create a 2-of-3 safe with two additional keys (Inheritance and Emergency). Let's start by importing all the necessary keys into the **Keys** tab.


![Import des clés hardware](assets/fr/04.webp)


Press **Add key**, then select **Add key from a hardware** to connect a hardware wallet. Bitcoin Keeper supports many devices: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, and Specter Solutions.


In our configuration, we import :


- 2 **Coldcard** keys (MK4SP and MK4)
- 2 keys **Tapsigner** (Metro and Genesis)


To add a Coldcard, select it from the list and follow the on-screen instructions to export the public key via QR code, file, USB or NFC. For more details on how to use a Coldcard or Tapsigner, please refer to our dedicated tutorials:


https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Once all your keys have been imported, you'll find them in the Keys tab with their custom names.


## Create legacy wallet


Let's move on to trunk creation. From the **Wallets** tab, press **Add Wallet**, select **Bitcoin Wallet**, then **Create Wallet**.


![Création du wallet](assets/fr/05.webp)


Choose the wallet type. For our legacy plan, select **2 of 3 multi-key**. At the bottom of the screen, activate **Enhanced Security Options** then press **Proceed**.


![Options de sécurité avancées](assets/fr/06.webp)


In the Enhanced Security Options popup, check :


- Inheritance Key**: an additional key that will be added to the quorum after a set period of time
- Emergency Key**: a key with deferred total control to recover funds in the event of key loss


Press **Save Changes**. Then select the 3 keys that will make up your wallet from those imported (e.g. Seed Key, Coldcard MK4SP, and Tapsigner Metro).


## Setting special key deadlines


The next screen lets you configure the Emergency Key and Inheritance Key. This is where you define the delays governing the activation of these special keys.


![Configuration des délais](assets/fr/07.webp)


For the **Emergency Key**, select the hardware key that will serve as the ultimate backup (here Coldcard MK4) and choose the activation delay (in our example: 2 years). Unlike the Inheritance Key, the Emergency Key does not add to the quorum: it allows you to **bypass the multisig** completely, and gives you total control over the funds after the time limit has expired. It's your solution of last resort: if several keys are lost or destroyed, this single key allows you to recover everything. It must therefore be protected with the utmost rigor.


For the **Inheritance Key**, select the key intended for the heir (here Coldcard MK4SP) and choose the delay (in our example: 1 year). After one year without movement, this key **will be added to the signature quorum**. In practical terms, your wallet 2-of-3 will become a wallet 2-of-4 once this period has elapsed, enabling the heir to participate in the signature alongside existing keys.


### How do timelocks work?


Bitcoin Keeper uses **absolute timelocks** (CLTV - CheckLockTimeVerify), made possible by Miniscript. Unlike relative timelocks (CSV), which start when each UTXO is received, absolute timelocks work with a **fixed expiration date** defined when the wallet is created.


In concrete terms, if you create a wallet today with a 1-year Inheritance Key, the activation date will be "today + 1 year". All funds deposited in this wallet, whatever their date of deposit, will be accessible via the Inheritance Key on this same date.


The advantage of absolute timelocks is that they allow lead times of over 15 months (the limit of relative CSV timelocks), which explains why Bitcoin Keeper can offer options such as 2 years.


### The refresh mechanism


To prevent the activation of special keys during your lifetime, you must periodically "refresh" your wallet. With absolute timelocks, this involves **recreating the wallet with a new expiration date** pushed into the future, then transferring your funds to this new wallet.


Bitcoin Keeper simplifies this process with an integrated refresh function. The application automatically handles the complexity in the background: you simply follow the guided steps, without having to manually create a new wallet or transfer the funds yourself. Plan this operation on a regular basis, well in advance of the expiration of the shortest timeframe configured. For example, with a 1-year Inheritance Key, refresh every 9-10 months to maintain a safety margin.


## Save and export configuration


Once the wallet has been created, the application reminds you to save the configuration file. **This step is critical**: without this file, your heirs will not be able to reconstitute the wallet multisig.


![Export de la configuration](assets/fr/08.webp)


Press **Backup Wallet Recovery File**. Several export options are available:


- PDF export**: generates a complete document with all wallet information
- Show QR**: displays a QR code to import the configuration on another device
- Airdrop / File Export**: exports the file via the sharing options
- NFC**: share via NFC with a compatible device


Multiply the copies: one at your notary's, one in a bank safe, one encrypted digital version. Your new wallet now appears in the Wallets tab with the tags "Multi-key", "2 of 3", "Inheritance key" and "Emergency key".


## Create a Wallet Canary


The Canary Wallet is an early warning system. The idea: each key used in a wallet multi-key can also be used in a separate wallet single-key. By depositing a small sum on this wallet "canary", any unauthorized movement signals a compromise of the key.


![Canary Wallets](assets/fr/09.webp)


There are two ways to configure a Wallet Canary. From the **More** tab, press **Canary Wallets** in the "Keys and Wallets" section. The screen explains the principle: if someone accesses one of your keys and finds funds in the associated wallet single-key, they will attempt to remove them, which will alert you.


![Configuration Canary depuis une clé](assets/fr/10.webp)


You can also configure the Canary directly from a key. In the **Keys** tab, select a key (e.g. Tapsigner Genesis), press the **Settings** (gear) icon, then **Canary Wallet**. The associated wallet canary opens, ready to receive some surveillance satoshis.


Deposit a small sum (a few thousand satoshis) on each Canary Wallet. If these funds move without your agreement, immediately remove the compromised key from your multisig safes.


## Best practices


**Test your configuration** with a small amount of money before putting a large sum into it. Send a few thousand satoshis to the vault, then try an outgoing spend to check that you've mastered the signing process with each device. Also test importing the configuration file on another phone to make sure the backup works.


**Distribute keys intelligently**. For Tapsigners, hand them over in a sealed envelope with the PIN communicated separately (e.g. in the Recovery Instructions letter stored elsewhere). For classic hardware wallets, keep the device with a trusted third party and the seed on paper or metal with you or another third party. Note the fingerprint of each key and its name in the configuration file to avoid confusion.


**Plan periodic tests** (fire drills). Annually, check that you can rebuild the safe from backups on a blank phone. Test Canary alerts by checking balances. Simulate loss scenarios ("what if I lose the Coldcard?") to confirm that the remaining key combinations are sufficient.


**Don't forget the refresh**. If you've set your Inheritance Key to 1 year, refresh yourself every 9-10 months. This is the price you pay for automatic transmission without third-party intervention.


**Keep the plan up to date**. Any change (replacement of a key, modification of heirs, change of deadline) must be reflected in all backups and documents. Regenerate PDFs after each modification and redistribute new versions.


## Limits and considerations


Despite the power of these tools, it's important to recognize their limitations in order to manage them as effectively as possible.


The **complexity** of a multisig safe with timelocks can be a risk in itself: misconfiguration, misunderstanding by heirs, loss of a critical element among the many components. Bitcoin Keeper simplifies the experience as much as possible, but it remains a technical operation. Only deploy this plan if the amount to be protected justifies it. For small amounts, a simpler plan may suffice.


The **application dependency** is worth thinking about. Although the code is open source and based on open standards (Miniscript, BSMS), certain functionalities rely on the Keeper ecosystem. Keep a copy of the application (Android APK or iOS IPA) and document in your letters to heirs the possibility of using other Miniscript-compatible wallets (such as Liana) to recover funds.


Trusted brokers** introduce a human risk. What happens if an ill-intentioned relative uses the key entrusted to him/her before the deadline? Or if the lawyer misplaces your documents? Choose these people carefully, explain their responsibilities clearly, and have a plan B. Canary Wallets, redundant backups and the very structure of multisig remain your best protection against these hazards.


## Conclusion


Bitcoin Keeper, with its Diamond Hands plan, offers a complete toolbox for estate planning: Enhanced Vaults with timed keys, accompanying documents, Canary Wallets, and personalized support.


It's more than just a technical issue: it's a question of designing the architecture of your estate, intelligently distributing keys and knowledge, and regularly testing the system. A well-designed Bitcoin inheritance plan transforms your satoshis into a real, transferable legacy.