---
name: Blue Wallet

description: Bitcoin Radically Simple and Powerful Portfolio
---
![cover](assets/cover.webp)


Getting started with Bitcoin seems to be a big challenge for people who are skeptical about the simplicity of its use. Finding the right tools to ensure this simplicity therefore becomes of paramount importance for better adoption of Bitcoin as a medium of exchange and not just as a store of value.


In this tutorial we'll be taking a look at Blue Wallet, a simple but highly effective Bitcoin wallet that allows you to manage your bitcoins personally and also to create management cooperatives based on [Multisig](https://planb.academy/resources/glossary/multisig) (don't worry, we'll come back to it).




## Getting started with Blue Wallet


Blue Wallet is an open source, self-hoarding Bitcoin wallet that lets you take control of your bitcoins. It is available as a mobile app on both Android and iOS platforms. In this tutorial we'll be basing ourselves on the Android version, however, all the processes that will be developed are equally valid on iOS.


![download](assets/fr/01.webp)


⚠️ Please make sure to download the Blue Wallet Bitcoin Wallet application on an official platform to guarantee its authenticity and protect your bitcoins from possible leaks and hacks.


Once installed, you can create a new wallet and save the 12 recovery words, or import an existing Bitcoin wallet. Find out how to make an efficient backup of your keywords so you don't lose access to your bitcoins.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

With Blue Wallet you can create separate, dedicated Bitcoin wallets. For example, you can have one wallet for your savings and another for your daily expenses, all in the same application.


![home](assets/fr/02.webp)


## Portfolio types


In Blue Wallet, you'll find two native Bitcoin wallet types.


### Bitcoin wallet


If you're used to other Bitcoin wallets like Phoenix or Aqua, you won't be at all out of step on Interface with Blue Wallet's Bitcoin wallet.


https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Blue Wallet's Bitcoin wallet represents the standard wallet in the Bitcoin ecosystem. You can spend bitcoins as long as you are in possession of the recovery words that will provide a valid signature on the network to authenticate that you own the bitcoins.


To create a Bitcoin wallet, click on the **Add now** button, insert the name of your wallet and choose the Bitcoin type.


![bitcoin-wallet](assets/fr/03.webp)


When you click on your Bitcoin wallet preview, you'll be able to view your transaction history and send and receive bitcoins.


⚠️ All transactions in your Bitcoin wallet are on the Bitcoin protocol main chain (Mainnet).



- Receiving bitcoins with the Bitcoin Blue Wallet wallet is intuitive. At the bottom of your screen, click on the **Receive** button. Share the QR code or your Bitcoin address with your sender so they can send you the bitcoins.


You can also configure a predefined amount to specify the amount of Bitcoin you wish to receive.


![receive-bitcoin](assets/fr/04.webp)



- On the **Send** button, send bitcoins to a Bitcoin address, setting the desired amount and validating the transaction.


![send-bitcoin](assets/fr/05.webp)


Blue Wallet lets you configure the parameters of your Bitcoin shipment as you wish.


You can therefore select the transaction fee ratio that suits you if you want to see your transaction quickly validated in a Mempool and included in a block by the miners. Depending on the ratio you choose, miners will prioritize your transaction to a greater or lesser extent. Find out more in our Mempool Space tutorial.


https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)



- With Blue Wallet, you can add multiple recipients to a single shipment.


When you add the Bitcoin address of your first recipient, in the options, click on **Add Recipient**, add the Bitcoin address and then set the amount to be sent to this recipient, and so on. Blue Wallet will dispatch the bitcoins for multiple shipments based on your single action.


![add-recipients](assets/fr/07.webp)


You can remove one or all recipients by clicking on **Remove Recipient** and **Remove All Recipents** respectively.


![remove-recipient](assets/fr/08.webp)



- **Inflate fees**: Have you made a transaction that's taking a long time to be confirmed? By enabling fee inflation you can add additional transaction fees to your pending transaction to speed up its confirmation.


![bumping](assets/fr/09.webp)


### Multisig Portfolio


The Multisig (multi-signature) wallet represents a wallet created from the grouping of a certain number (minimum 2) of Bitcoin wallets. In this type of wallet, depending on the configuration and method chosen, spending bitcoins becomes a collective and cooperative action.


In Blue Wallet, you can create multi-signature wallets for your association, your family, your company. Throughout this section, we'll explore every aspect of this special type of wallet.


Add a new wallet and select type **Multisig Vault** to create a multi-signature wallet.


![multisig-vault](assets/fr/10.webp)


Define the m-de-n configuration in your multi-signature organization by clicking on **Vault Settings**.


⚠️ In an m-of-n configuration, **m** represents the minimum number of signatures required to approve a transaction and **n** the number of wallets in your organization.


Be sure to define a minimum number of signatures (m) for the majority of your organization. For example, a 2-of-3 multi-signature configuration requires two wallets in your organization to sign the transaction before it can be carried out.


❗Defining an m-of-n configuration where n equals m is a big risk. When a member loses access to his wallet you lose the authorization to spend bitcoins in the wallet.


Here are some examples of optimal configurations to ensure security and accessibility to bitcoins:



- 2-de-3 multi signature.



- 5-de-7 multi signature.


![vault-settings](assets/fr/11.webp)


Keep to best practice by selecting the P2WSH format.


❗ **[P2WSH](https://planb.academy/resources/glossary/p2wsh) or Pay to Witness Script Hash** is a locking method that locks your transaction's outgoing bitcoins (Outputs) to the Hash of a custom script that Blue Wallet sets up. The main advantage of this type of locking is that it reduces transaction data size and implicitly allows you to pay lower transaction fees.


Create or import each of the **n** wallets in your configuration. In our tutorial, we'll be using a 2-of-3 multi-signature configuration. Be sure to save the recovery words for each wallet individually.


![vault-keys](assets/fr/12.webp)



- Receive bitcoins


On your Multisig wallet page, you'll find your transaction history and the Receive and Send buttons.


Receiving bitcoins in a multi-signature wallet is the same process as when you are in a standard Bitcoin wallet.



- Send **bitcoins**:


By managing a multi-signature wallet, spending bitcoins becomes a compound action, whether with other people or a second wallet of your own. The single signature of your wallet is no longer sufficient. This adds a layer of security to your bitcoins, because a malicious individual will not be able to spend those bitcoins when he comes into possession of just one of your private keys.


Like the standard Bitcoin wallet of Blue Wallet, you can define multiple recipients in the **Add recipients** option.


When validating your transaction, you'll need a second signature to approve the spending of the bitcoins. Remember, we're in a 2-de-3 multi-signature configuration.


The second wallet signatory, if he or she is also a user, can sign the transaction even if he or she is off the Internet (no Wi-Fi, no mobile data) by scanning the QR code of the [partially signed transaction](https://planb.academy/resources/glossary/psbt) you have just created.


![mutisig-send](assets/fr/13.webp)



- Go further with the **Multi signature** wallet:


On the Interface of your multi-signature wallet, click on the **Manage keys** button.


By forgetting one of the recovery words of one of the signatory wallets (**Forget this seed...**), you notify Blue Wallet to delete the backup of these words from its memory. You will therefore have made an external backup.


![revoke-key](assets/fr/14.webp)


By performing this action, you keep only the public key associated with these recovery words.


⚠️ Keeping only public keys (XPUB) allows you to add an extra level of security to your 2-of-3 multi-signature configuration. Indeed, it could be detrimental to keep all recovery words in one place when your phone is under attack. Attackers with access to only one **VAULT** (keyword) that you use to sign your transactions, won't be able to steal your bitcoins (minimum of 02 signatures required) because public keys can't be used to sign transactions.


## More options with Blue Wallet


### Improving wallet access security


In Settings, the **Security** option lets you define the use of a fingerprint to carry out a transaction, export or delete your wallet. This authenticates the person using your smartphone.


![biometry](assets/fr/15.webp)


## Activate Lightning Network


Lightning Network is no longer natively supported in the Blue Wallet application.


In Settings > **Lightning Settings**, you can manually associate your Lightning wallet when running a Lightning Network Daemon (LND) node. Install the LND Hub, then associate your wallet by entering the link generated by the Hub.


![ln](assets/fr/16.webp)


https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

You've now completed the Blue Wallet tour, ready to use Bitcoin in all its simplicity and power. We recommend that you take the next step, and find out how you can accept bitcoin payments in your shops, thanks to the power of Lightning.


https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06