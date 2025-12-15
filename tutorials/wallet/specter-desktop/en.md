---
name: Specter Desktop
description: Manage your multi-signature Bitcoin wallets in total sovereignty with your own node
---

![cover](assets/cover.webp)


Specter Desktop is an open source application (MIT license) developed by Cryptoadvance since 2019 that facilitates the management of Bitcoin wallets with your hardware wallets (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) and your own Bitcoin infrastructure (Bitcoin Core node or Electrum server). The application excels particularly in multi-signature configurations, enabling you to secure large sums by distributing signing power between several independent hardware wallets.


**In this tutorial, you will learn how to:**


- Install and configure Specter Desktop on your computer (Windows, macOS or Linux)
- Connect Specter to a Electrum server (we'll use Umbrel in this example)
- Create a simple wallet with wallet hardware (Coldcard)
- Receive and send bitcoins with complete sovereignty
- Setting up a 2-on-3 multisignature wallet with several hardware wallets
- Install Specter on an Umbrel server (advanced bonus)


All your transactions will be validated locally via your own infrastructure, without transmitting any information to external servers, guaranteeing your confidentiality and financial sovereignty. Always check transactions on your wallet hardware screen before signing.


## Download and installation


Visit the official Specter Desktop website to download the application.


![Page d'accueil Specter](assets/fr/01.webp)


On the download page, choose the version corresponding to your operating system: macOS, Windows or Linux.


![Téléchargement selon l'OS](assets/fr/02.webp)


Once downloaded, install the application according to your operating system's usual instructions. For macOS, drag the icon into Applications. For Windows, run the installer. For Linux, follow the package instructions.


## Initial configuration


On first launch, Specter Desktop asks you to choose your connection type. You can connect to a Electrum server or to your own Bitcoin Core node.


![Choix du type de connexion](assets/fr/03.webp)


In this example, we'll use a connection to a Electrum server running on Umbrel.


For more information, please refer to our Umbrel tutorial:


https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

This option offers faster synchronization than Bitcoin Core. If you prefer, you can select "Bitcoin Core" and configure the connection to your local node. The following steps remain the same regardless of your choice.


Select "Electrum Connection" then choose "Enter my own" to configure your own Electrum server.


![Configuration Electrum](assets/fr/04.webp)


Enter the address of your Electrum server. In our case with Umbrel, the address will be `umbrel.local` with port `50001`. Click on "Connect" to establish the connection.


Once connected, the welcome screen appears, with a checklist to get you started. You now need to add your hardware wallets.


![Écran d'accueil](assets/fr/05.webp)


## Adding wallet hardware


In the left-hand menu, click on "Add device" to add your wallet hardware.


Specter Desktop supports numerous hardware wallets: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, and many others.


If you'd like to learn more, take a look at our hardware wallet tutorials.


![Sélection du type de hardware wallet](assets/fr/06.webp)


Select your wallet hardware. In this example, we're using a Coldcard MK4.


Below you will find our tutorial for this wallet hardware:


https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

For a Coldcard, you need to export the public keys from the wallet hardware either via a USB connection or a microSD card.


![Import des clés du Coldcard](assets/fr/07.webp)


Follow the instructions displayed to export the keys from your Coldcard. Give your wallet hardware a name (here "MK4 Tuto"). Once the keys have been imported, you can create a wallet with a single key, or add other hardware wallets for a multi-signature wallet.


![Dispositif ajouté](assets/fr/08.webp)


## Portfolio creation


After adding your wallet hardware, click on "Create single key wallet" to create a single-signature wallet.


Give your wallet a name (e.g. "Wallet for tuto") and select the address type. Select "Segwit" to use native bech32 addresses that optimize transaction costs.


![Configuration du portefeuille](assets/fr/09.webp)


Once your wallet has been created, Specter offers to save a backup PDF file containing all the public information needed to restore your wallet (descriptors, extended public keys). This file does not contain your private keys.


![Sauvegarde du portefeuille](assets/fr/10.webp)


## Receive bitcoins


To receive bitcoins, select your wallet in the left-hand menu, then click on the "Receive" tab.


Specter automatically generates a new reception address with a QR code.


![Génération d'une adresse de réception](assets/fr/11.webp)


You can copy the address or scan the QR code. Always check the address on your wallet hardware screen before passing it on to anyone.


## View history and addresses


Once you've received bitcoins, you can view your transactions in the "Transactions" tab.


![Historique des transactions](assets/fr/12.webp)


The "Addresses" tab lets you view all the addresses generated by your wallet, with their usage status and associated amounts.


![Liste des adresses](assets/fr/13.webp)


## Send bitcoins


To send bitcoins, click on the "Send" tab. Enter the recipient's address, the amount to be sent, and check the advanced options if you wish to manually select the UTXOs (coin control).


![Création d'une transaction](assets/fr/14.webp)


Click on "Create Unsigned Transaction" to build the transaction. Specter will then ask you to sign the transaction with your wallet hardware.


![Signature de la transaction](assets/fr/15.webp)


If you're using a Coldcard, you'll have the choice of signing via USB or using the microSD card (air-gapped). Confirm the transaction on your wallet hardware screen, carefully checking the destination address and the amount.


Once the transaction has been signed, you can broadcast it on the Bitcoin network.


![Options de diffusion](assets/fr/16.webp)


Click on "Send transaction" to send the transaction. Specter will confirm that your transaction has been sent, and you can track its status in the Transactions tab.


![Diffusion de la transaction](assets/fr/17.webp)


## Creating and using a multi-signature wallet


One of Specter Desktop's major assets is its ability to simplify the management of multi-signature wallets. A multisig wallet requires several signatures to authorize a transaction, thus eliminating the single point of failure. A 2-on-3 configuration, for example, requires two signatures from three separate hardware wallets to validate any expenditure.


To create a multisig wallet, start by adding all the signing hardware wallets via "Add device". In this example, we'll be using three different hardware wallets: a Coldcard MK4 (already added earlier), a Passport and a Ledger. This diversification of manufacturers strengthens security by avoiding dependence on a single supply chain or firmware.


Here are the links to the Ledger and Passport tutorials:


https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Add the Passport by naming the wallet hardware (e.g. "Passport multi") and importing its keys via microSD card or QR code. Then click on "Continue" to continue.


![Ajout du Passport](assets/fr/23.webp)


Then add the Ledger by connecting it via USB and opening the Bitcoin application on the wallet hardware. Name it (e.g. "ledger multi") and click on "Get via USB" then "Continue" to import its public keys.


![Ajout du Ledger](assets/fr/24.webp)


Once you have registered your three hardware wallets in Specter, click on "Add wallet" and select the "Multiple Signature" option to create a multi-signature wallet.


![Choix du type de wallet](assets/fr/25.webp)


Select the three hardware wallets you wish to include in your multisignature quorum: MK4 Tuto, Passport multi and ledger multi. Click on "Continue" to proceed to the next step.


![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)


Choose your multi-signature configuration. Select "Segwit" as the address type to benefit from optimized fees. The "Required Signatures to Authorize Transactions (m of 3)" parameter lets you define the threshold: for a 2-on-3 configuration, 2 signatures are required. Each wallet hardware displays its corresponding multisig key. Click on "Create wallet" to finalize creation.


![Configuration 2-sur-3 Segwit](assets/fr/27.webp)


Your "Multi tuto" multisignature wallet is now created. Specter immediately recommends that you save the backup PDF file containing the wallet descriptor. Click on "Save Backup PDF" to download this critical file.


![Wallet multisig créé](assets/fr/28.webp)


Specter also lets you export wallet information to each of your hardware wallets via QR code or file. This enables certain hardware wallets (such as Coldcard or Passport) to store multisig configuration directly in their memory.


For Passport, unlock your device then go to "Manage Account" > "Connect Wallet" > "Specter" > "Multisig" > "QR Code", then scan the QR code generated by Specter. Your Passport will then ask you to scan a receiving address from your wallet to validate the multisig configuration.


For the MK4, plug it into your PC and unlock it. Then click on "Save MK4 Tuto file" and save the file to your MK4. The next time you sign your wallet hardware, the MK4 will use this file to finish configuring the multisig.


![Export vers les hardware wallets](assets/fr/29.webp)


For your information, you can access backups at any time from the "Settings" tab of your wallet, then "Export":


![Accès au backup PDF](assets/fr/30.webp)


Day-to-day use remains similar to a simple wallet: you generate receiving addresses as normal. To send bitcoins, go to the "Send" tab, enter the recipient's address and the amount, then click on "Create Unsigned Transaction".


![Création d'une transaction multisig](assets/fr/31.webp)


Specter builds a PSBT (Partially Signed Bitcoin Transaction) and displays "Acquired 0 of 2 signatures". You must now sign with at least two of your three hardware wallets. Click on the first wallet hardware (e.g. "MK4 Tuto") to sign with your Coldcard, then on the second (e.g. "Passport multi") to obtain the second signature required.


![Signature de la transaction](assets/fr/32.webp)


Once you have obtained the 2 required signatures (the interface displays "Acquired 2 of 2 signatures" and "Transaction is ready to send"), click on "Send Transaction" to broadcast the transaction on the Bitcoin network.


![Transaction prête à être diffusée](assets/fr/33.webp)


This multi-signature approach is particularly well suited to companies (several managers need to approve expenditure), families (protection of a multi-generational inheritance), or individuals managing large sums (geographical distribution of hardware wallets to withstand localized disasters).


### The critical importance of multisignature backups


**Please note**: backing up a multisig wallet is fundamentally different from backing up a single wallet. Your recovery phrases (seed phrases) alone are not sufficient to restore a multisig wallet. You must also back up the **output descriptor** (output descriptor), which contains the configuration information for your multisig wallet.


The output descriptor includes essential data: the extended public keys (xpubs) of each co-signer, the signature threshold (2-on-3 in our example), the type of script used (native, nested or legacy Segwit), and the bypass paths for each wallet hardware. Without this descriptor, even if you have two of your three recovery phrases, you won't be able to rebuild your wallet or access your bitcoins. The descriptor lets your software know how to combine the public keys to generate the Bitcoin addresses corresponding to your funds.


Specter Desktop automatically generates a backup PDF file when you create your multisig wallet. This PDF contains the complete descriptor, the fingerprints of each wallet hardware, and all the public information required for restoration. **This file does not contain your private keys** and therefore does not by itself allow you to spend your bitcoins, but it does allow anyone accessing it to see your complete transaction history and balance.


To back up your multisignature configuration correctly, follow this procedure: after creating your wallet, click on the "Settings" tab, then "Export" and select "Save Backup PDF". Create several copies of this PDF: print at least two copies on paper, and also keep an encrypted digital copy. Store one copy of the PDF with each of your recovery phrases, in geographically separate locations.


Engrave your recovery phrases on fireproof and waterproof metal plates to guarantee their longevity. Never underestimate the importance of these backups: if you lose the `~/.specter` folder on your computer AND you lose one of your hardware wallets without a descriptor backup, all your funds will be irretrievably lost, even with a 2-on-3 configuration. Multi-signature redundancy protects against the loss of wallet hardware, but only if you have correctly backed up your wallet's descriptor.


## Advantages and limitations of Specter Desktop


**Benefits**: Optimum confidentiality with complete local validation without third-party servers. Multisignature flexibility for advanced configurations (corporate, family, individual). Extensive hardware wallet support with full interoperability (USB and air-gapped).


**Limitations**: Significant learning curve on advanced Bitcoin concepts (UTXOs, descriptors, derivation paths).


## Best practices


Always check addresses and amounts on your hardware wallet screen before validation, to protect yourself against malware.


Keep PDF backups separate from your seeds. These public descriptors can be stored in a bank vault or encrypted cloud, facilitating recovery without exposing your private keys.


Test recovery on token amounts before using your wallets with large funds. Create, test, delete and restore to validate your procedures.


Keep Specter and your firmware up to date. Distribute your multi-signature co-signers geographically (home/office/nearby) to withstand localized disasters. Use descriptive labels to facilitate accounting and tax returns.


## Bonus: Installation on a Bitcoin server (Umbrel, RaspiBlitz, Start9)


If you already own a Bitcoin server such as Umbrel, RaspiBlitz, MyNode or Start9, you can install Specter Desktop directly from their application store. This approach offers several significant advantages: the application automatically configures itself with your local Bitcoin Core node, it remains accessible 24/7 via a web interface from any device on your network, and you can even access it securely remotely via Tor. Your entire Bitcoin infrastructure is centralized on a single dedicated server, simplifying management and strengthening your sovereignty.


### Installation from the Umbrel App Store


From your Umbrel interface, go to the App Store and search for Specter Desktop. Click on "Install" to launch the installation.


![App Store Umbrel - Specter Desktop](assets/fr/18.webp)


Once installation is complete, open Specter Desktop on your Umbrel. The welcome screen will ask you to choose your connection type. If you're using Specter on your Umbrel, click on "Update settings" to configure the connection.


![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)


Select "Remote Specter USB connection" to enable the use of USB hardware wallets connected to your local computer while using Specter on the remote Umbrel server.


![Configuration Remote Specter USB](assets/fr/20.webp)


Follow the instructions displayed to configure the HWI Bridge. You need to access the device bridge settings and add the domain `http://umbrel.local:25441` to the whitelist. Click on "Update" to save the configuration.


![HWI Bridge Settings](assets/fr/21.webp)


If you'd also like to use your USB hardware wallets from your local computer, download the Specter Desktop application to your machine and set it to "Yes, I run Specter remotely". Click on "Save" to finalize the configuration.


![Configuration connexion remote dans l'app](assets/fr/22.webp)


## Conclusion


Specter Desktop democratizes advanced Bitcoin configurations, making multisignature accessible without sacrificing your sovereignty or confidentiality. For users managing significant amounts of money, it transforms institutional practices into solutions that can be deployed by private individuals.


Although the application requires an initial investment in infrastructure and learning, it offers complete sovereignty: control of the validation infrastructure, physical ownership of keys, and transactions free from third-party surveillance. Whether you're an individual securing your savings, a family creating a multi-generational safe-deposit box, or a company managing cash flow, Specter Desktop is the reference tool for reconciling maximum security and absolute sovereignty.


## Resources


### Official documentation


- [Specter Desktop official website](https://specter.solutions/desktop/)
- [GitHub source code](https://github.com/cryptoadvance/specter-desktop)
- [Complete documentation](https://docs.specter.solutions/)


### Community and support


- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit discussion forum](https://reddit.com/r/specterdesktop/)
- [GitHub bug reports](https://github.com/cryptoadvance/specter-desktop/issues)