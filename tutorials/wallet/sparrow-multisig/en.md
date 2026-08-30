---
name: Sparrow Wallet - Multisig
description: Create a multi-signature wallet on Sparrow
---
![cover](assets/cover.webp)


A multi-signature wallet (often called "*Multisig*") is a Bitcoin wallet structure that requires several cryptographic signatures, from different keys, to authorize an expenditure. Unlike a conventional ("*singlesig*") wallet, where a single private key is sufficient to unlock a UTXO, the Multisig is based on an **m-of-n** model: of the _n_ keys associated with the wallet, _m_ must imperatively co-sign each transaction.


This mechanism enables control of a wallet to be shared between several entities or devices. For example, in a 2-of-3 configuration, three independent sets of keys are generated, but only two are needed to release funds. This architecture drastically reduces the risks associated with the compromise or loss of a key: a thief with access to just one key cannot empty the wallet, and a user who loses one can still access his funds with the remaining two.


![Image](assets/fr/01.webp)


However, this greater security comes with greater complexity. Setting up a Multisig wallet requires securing several mnemonic phrases (one per signature factor) and extended public keys ("*xpub*"). Indeed, if you're using a Multisig 2-of-3 wallet, to retrieve the wallet you must either have all three mnemonic phrases, or at least two of the three phrases. But if you only have two of the three phrases, you also need access to the three *xpubs*, without which it will be impossible to retrieve the public keys needed to access the bitcoins they protect.


To summarize, to recover a Multisig wallet, you must :


- Or access all the mnemonic phrases associated with each signature factor;
- Either have the minimum number of mnemonic phrases required by the threshold to be able to sign, and also have access to the xpubs of all the factors in order to retrieve the necessary public keys.


![Image](assets/fr/02.webp)


This management of Multisig wallet backups is facilitated by *Output Script Descriptors*, which group together all the public data required to access the funds. However, this functionality is not yet implemented in all wallet management software.


Multisig is particularly suited to bitcoiners looking for enhanced security or collective management of funds: companies, associations, families, or individual users holding a significant amount of bitcoins. It can be used to create decentralized governance schemes, for example, to distribute signing authority among several managers or team members.


In this tutorial, we'll learn how to create and use a classic multisignature wallet with **Sparrow Wallet**. If you'd like to create a customized multisignature wallet with timelocks, I recommend using Liana instead:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prerequisites


For this tutorial, I'm going to show you how to make a Multisig with [Sparrow Wallet wallet management software](https://sparrowwallet.com/download/). If you haven't yet installed this software, please do so now. If you need help, we also have a detailed tutorial on configuring Sparrow Wallet :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

To set up a multi-signature wallet, you'll need different hardware wallets. For a Multisig 2-de-3, for example, you could use :


- A Trezor Model One;
- Ledger Flex;
- A Passport Core.


![Image](assets/fr/03.webp)


It's a good idea to use different makes of Hardware Wallet in your Multisig configuration. This ensures that if a specific model encounters a serious problem, it won't affect the overall safety of your Multisig. What's more, it allows you to benefit from the specific advantages of each device. For example, in my configuration :



- The Trezor Model One is completely open-source, which makes it possible to verify the seed generation. However, as it is not equipped with a Secure Element, it remains vulnerable to physical attacks;



- The Ledger Flex, on the other hand, benefits from unverifiable proprietary firmware, but incorporates a Secure Element that offers excellent physical protection;



- The Passport Core combines fully open-source firmware, a Secure Element, and air-gapped QR-code exchanges. It is an independent third signer that can verify addresses and sign PSBTs without a USB data connection.


Before configuring your Multisig wallet, make sure that each Hardware Wallet is correctly configured (mnemonic generation and saving, PIN definition). For detailed instructions, you can consult our tutorials for each Hardware Wallet, for example :


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

As we'll see later in this tutorial, it's also possible to integrate into your Multisig configuration a factor which is not associated with a Hardware Wallet, but whose private keys are stored on your PC. This method is obviously less secure than the exclusive use of hardware wallets, but it may be relevant in certain cases. For example, for a Multisig 2-de-3, you could opt for two hardware wallets and one Software Wallet.

> ⚠️ **Coldcard MK3 security notice:** do not create a new seed on an MK3 running firmware earlier than 4.2.0. Seeds generated on earlier firmware must be replaced and the funds moved. This tutorial therefore uses Passport Core as its air-gapped reference signer.


## Creating a Multisig wallet


Open Sparrow Wallet, click on the "*File*" tab, then select "*New Wallet*".


![Image](assets/fr/04.webp)


Assign a name to your multisignature wallet, then click on "*Create Wallet*" to confirm.


![Image](assets/fr/05.webp)


In the "*Policy Type*" drop-down menu, select the "*Multi Signature*" option.


![Image](assets/fr/06.webp)


In the top right-hand corner, you can now define the total number of keys in your Multisig, as well as the number of co-signers required to authorize an expense. In my example, this is a 2-of-3 scheme.


![Image](assets/fr/07.webp)


At the bottom of the window, Sparrow Wallet displays three "*Keystore*". Each represents a set of keys. Here, I'm using three hardware wallets, so each "*Keystore*" corresponds to one of them. We'll now configure them.


I start with the Passport Core. In the "*Keystore 1*" tab, I choose the "*Airgapped Hardware Wallet*" option.


![Image](assets/fr/08.webp)


On the Passport, open the account you want to use, then select "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". The Passport displays an animated QR code containing its public key information.

In Sparrow, select "*Scan...*" next to "*Passport*" and scan that animated QR code with your computer's webcam. Check the master-key fingerprint shown by Sparrow against the one displayed by the Passport, then import the keystore.

Your Passport xpub has now been imported. Repeat the appropriate procedure for the Ledger Flex and Trezor Model One.


For the Ledger Flex, I select "*Keystore 2*", then click on "*Connected Hardware Wallet*". Make sure the Ledger is connected to the computer, unlocked, and that the Bitcoin application is open.


![Image](assets/fr/15.webp)


Then click on the "*Scan...*" button.


![Image](assets/fr/16.webp)


Next to the name of your hardware wallet, click on "*Import Keystore*".


![Image](assets/fr/17.webp)


The second signatory is now correctly registered in Sparrow Wallet.


![Image](assets/fr/18.webp)


I repeat exactly the same procedure with the Trezor One to finalize the Multisig configuration.


![Image](assets/fr/19.webp)


In my configuration we don't cover this case, but if you want to include a signature via a software wallet in Sparrow (hot wallet) within your Multisig, simply click on the "*New or Imported Software Wallet*" button.


Now that all your signature devices are imported into Sparrow Wallet, you can finalize the creation of Multisig by clicking on "*Apply*".


![Image](assets/fr/20.webp)


Choose a strong password to secure access to your Sparrow Wallet wallet. This password protects your public keys, addresses, labels and transaction history from unauthorized access.


Remember to save this password in a safe place, such as a password manager, to avoid losing it.


![Image](assets/fr/21.webp)


## Backing up a Multisig wallet


We will now save the *Output Script Descriptor* on an independent medium and keep several copies of it.


The *Descriptor* contains all the xpubs in your Multisig wallet, as well as the derivation paths used to generate the keys. Remember what we saw in Part 1: to restore a Multisig wallet, you must either have **all** the mnemonic phrases, or only the minimum number required to reach the signature threshold. However, in the latter case, it is also essential to have **the xpubs** of the missing signatories. The *Descriptor* contains all your Multisig's xpubs.


If this isn't clear, just remember this: to retrieve a Multisig, you need the minimum number of mnemonic phrases for each Hardware Wallet used, depending on the threshold (in my case: 2 phrases), as well as the *Descriptor*.


This *Descriptor* contains no private keys, only public ones. This means that it does not give access to the funds. It is therefore not as critical as mnemonic phrases, which give full access to your bitcoins. The risk with the *Descriptor* is solely related to confidentiality: in the event of compromise, a third party could observe all your transactions, but could not spend your funds.


I strongly recommend that you create several copies of this *Descriptor*, and keep them with each signing device on your Multisig. For example, in my case, I print the *Descriptor* on paper and keep one copy with the Passport, another with the Trezor, and one with the Ledger. I also save this *Descriptor* as a PDF file on three USB sticks, each stored with one of the hardware wallets. In this way, I maximize my chances of never losing this *Descriptor*, and I'm sure of having two copies (one physical and one digital) with each device.


Once your Multisig wallet has been created, Sparrow automatically provides you with this *Descriptor*. Click on the "*Save PDF...*" button to save it both as text and as a QR code.


![Image](assets/fr/22.webp)


You can then print this PDF and copy it to your USB sticks.


![Image](assets/fr/23.webp)


The Passport uses the multisig configuration imported by Sparrow to display and verify the relevant key information during the QR pairing and signing flow. Keep the *Descriptor* independently: it remains essential to recover the wallet if one signer is unavailable.


In addition to saving the *Descriptor*, don't forget to pay particular attention to saving the mnemonic phrases for each of your signature devices. If you're just starting out, I highly recommend that you consult this other tutorial to learn how to save and manage them correctly:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Before receiving your first bitcoins on your Multisig, **I strongly advise you to perform an empty recovery test**. Make a note of some reference information, such as the first receiving address, then reset your hardware wallets while the wallet is still empty. Next, try restoring your Multisig wallet on the Hardware Wallets using your mnemonic phrase paper backups, then on Sparrow using the *Descriptor*. Check that the first address generated after restoration matches the one you originally wrote down. If it does, you can rest assured that your paper backups are reliable.


To learn more about how to perform a recovery test, I suggest you consult this other tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Receive bitcoins on your Multisig


Your wallet is now ready to receive bitcoins. In Sparrow, click on the "*Receive*" tab.


![Image](assets/fr/30.webp)


Before using the address generated by Sparrow Wallet, take the time to check it directly on the screen of your hardware wallets. This will ensure that the address has not been altered, and that your devices hold the private keys needed to spend the associated funds. This helps protect you against a number of attack vectors.


To do this, click on "*Display Address*" to display the address on your Trezor or Ledger, when connected by cable.


![Image](assets/fr/31.webp)


With the Passport, select the multisig account and choose "*Verify Address*". Scan the QR code of the receive address displayed by Sparrow. The Passport confirms on its screen whether the address belongs to the multisig wallet.


Check that the address displayed on each hardware wallet corresponds exactly to the one in Sparrow Wallet. It's advisable to do this just before sharing the address with the payer, to be sure of its integrity.


You can then assign a "*Label*" to this address, to indicate the origin of the bitcoins received. This is a good way of organizing the management of your UTXOs.


![Image](assets/fr/34.webp)


Once this has been verified, you can use the address to receive bitcoins.


![Image](assets/fr/35.webp)


## Sending bitcoins with your Multisig


Now that you've received your first Satss on your Multisig wallet, you can spend them too! In Sparrow, go to the "*Send*" tab to build a new transaction.


![Image](assets/fr/36.webp)


If you wish to use *Coin Control*, i.e. manually select the UTXOs you wish to spend, go to the "*UTXOs*" tab. Choose the UTXOs you wish to spend, then click on "*Send Selected*". You'll be automatically redirected to the "*Send*" tab, with the UTXOs already pre-filled.


![Image](assets/fr/37.webp)


Enter the destination address. Multiple addresses can be added by clicking on "*+ Add*".


![Image](assets/fr/38.webp)


Add a "*Label*" to describe the purpose of this expense, to make it easier to track your transactions.


![Image](assets/fr/39.webp)


Enter the amount to be sent to the selected address.


![Image](assets/fr/40.webp)


Adjust the charge rate according to current network conditions. For example, consult [Mempool.space](https://Mempool.space/) to select a suitable charge level.


After checking all the transaction parameters, click on "*Create Transaction*".


![Image](assets/fr/41.webp)


If you're happy with everything, click on "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


At the bottom of the screen, you'll see that Sparrow is waiting for 2 signatures. This is normal: the wallet used here is a Multisig 2-de-3.


![Image](assets/fr/43.webp)


I start signing with my Passport. In Sparrow, click "*Show QR*" to display the PSBT (*Partially Signed Bitcoin Transaction*) as animated QR codes. On the Passport, select the multisig account and choose "*Sign with QR Code*", then scan the QR code displayed by Sparrow.


On your Hardware Wallet screen, carefully check the transaction parameters: the recipient's address, the amount sent, and the charges. Once the transaction has been confirmed, validate to proceed to signature.


After you approve the transaction, the Passport displays the signed PSBT as animated QR codes. In Sparrow, click "*Scan QR*" and scan those codes with your webcam. The Passport signature is then added. I now use the Ledger for the second required signature: I connect and unlock it, then click "*Sign*" in Sparrow.


![Image](assets/fr/48.webp)


Click on "*Sign*" next to the name of your Hardware Wallet.


![Image](assets/fr/49.webp)


The first time you use your Ledger with this Multisig, Sparrow will ask you to verify the extended public keys (xpubs) of the co-signers. As with the Passport, this step prevents you from signing blindly later on. To validate this information, compare the xpub displayed on the Ledger screen with those provided directly by your other hardware wallets.


![Image](assets/fr/50.webp)


Check the recipient's address, the amount transferred and the transaction fee, then sign the transaction.


![Image](assets/fr/51.webp)


Press the screen to sign.


![Image](assets/fr/52.webp)


Sparrow now has the two signatures needed to release the funds from the Multisig wallet. Check the transaction one last time, and if all goes well, click on "*Broadcast Transaction*" to broadcast it over the network.


![Image](assets/fr/53.webp)


You'll find this transaction in Sparrow Wallet's "*Transactions*" tab.


![Image](assets/fr/54.webp)


Congratulations, you now know how to set up and use a multisignature wallet on Sparrow. If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Please feel free to share this article on your social networks. Thanks for sharing!


To go further, I recommend that you consult this tutorial on another method for increasing the security of your Bitcoin wallet, the passphrase BIP39 :


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
