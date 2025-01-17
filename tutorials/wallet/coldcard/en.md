---
name: Cold Card

description: Creating, backing up, and using a Bitcoin private key with a Coldcard device and Bitcoin Core
---

![cover](assets/cover.webp)

_Creating, backing up, and using a Bitcoin private key with a Coldcard device and Bitcoin Core_

## Complete guide to generating a private key using a Coldcard and using it through the interface of your Bitcoin Core node!

At the core of Bitcoin's network usage lies the concept of asymmetric cryptography: a pair of keys - one private and one public - that encrypt and decrypt data, a concept that ensures the confidentiality of communication.

In the case of Bitcoin, by generating such a pair of private and public keys, we are able to store bitcoins (UTXO or Unspent Transaction Output) and sign transactions to spend them.

Today, there are multiple tools available to facilitate the random generation of a private key and its backup in textual form using BIP 39 - a standard that determines how wallets associate a mnemonic phrase (seed phrase) with encryption keys. More often than not, the mnemonic phrase consists of 12 or 24 words, which must be securely backed up in order to be able to recover a wallet and its bitcoins.

In this article, we will learn how to generate a private key using a Coldcard Mk4, one of the most widely used and secure devices in the world of Bitcoin, using the dice roll method to ensure maximum entropy, and how to use it with Bitcoin Core in an air-gapped manner!

**Note:🧰** Get the following tools to use the guide:

- Coldcard device (Mk3 or Mk4)
- MicroSD card (4GB is sufficient)
- Power-only magnetic USB cable (mini-usb for Mk3, usb-c for Mk4)
- One or more quality dice

## Generating a new mnemonic phrase with a Coldcard

We will start the process of creating a private key from scratch, assuming a freshly unpacked Coldcard on which a PIN has already been set up (follow the steps on the Coldcard during device initialization).

**Note🚨:** To reset the private key of an already configured Coldcard, follow these steps:
_Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed > ✓_

**Attention:** your Coldcard will forget the private key following these steps. Make sure you have properly backed up your mnemonic phrase if you want to be able to recover it later.

## Steps to follow:

Connect to the Coldcard with PIN > New Seed Words > 24 Word Dice Roll

Perform 100 dice rolls, writing down the result obtained from 1 to 6 on the Coldcard after each roll. By practicing this method, you create 256 bytes of entropy, thus favoring the creation of a completely random private key. Coinkite also provides the necessary documentation for independent verification of their entropy generation system.

![Visual Cold Card Screenshot](assets/guide-agora/1.webp)

Once the 100 dice rolls are completed, press ✓ and then write down the 24 words obtained in order. Verify twice and press ✓. Finally, all that remains is to complete the verification test of the 24 words on the Coldcard, and voila, your new private key is created!

Next, choose whether or not to activate the NFC (Mk4) and USB functions by following the displayed steps. Once in the main menu, it is now time to update the device's firmware. Go to Advanced/Tools > Upgrade Firmware > Show Version, and check the official website to validate and download the latest available version. It is advisable to update the Coldcard in order to benefit from maximum security.

Before proceeding, it is recommended to note the Master Key Fingerprint (XFP) associated with the private key. This data allows for quick validation if you are in the correct wallet in the case of recovery, for example. Go to Advanced/Tools > View Identity > Master Key Fingerprint (XFP) and write down the series of eight alphanumeric characters obtained. The XFP can be noted in the same place as the mnemonic phrase, it is not sensitive data.

**Note:💡** it is recommended to test your mnemonic phrase backup in a different software. To do this securely, consult our article Verify the backup of a Bitcoin wallet with Tails in less than 5 minutes.

## Security Bonus: the "Secret Phrase" (optional)

A passphrase (secret phrase) is a great element to add to a wallet configuration in order to add a layer of security to protect your bitcoins. The passphrase acts as a sort of 25th word to the mnemonic phrase. Once added, a completely new wallet is created along with a private key and its associated mnemonic phrase. It is not necessary to write down the new mnemonic phrase, as this wallet can be accessed by combining the initial mnemonic phrase with the chosen passphrase.

The goal is to note the passphrase separately from the mnemonic phrase because an attacker who has access to both items will have access to the funds. On the other hand, an attacker who only has access to one of these items will have no access to the funds, and it is this specific advantage that optimizes the level of security of the wallet configuration.

![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)

## Steps to add a passphrase with Coldcard:

Passphrase > Add Words (recommended) > Apply. The device will display the XFP of the newly generated wallet with the passphrase, which should be noted down with the passphrase for the same reasons mentioned earlier.

**Tip💡** Here there are additional resources related to the passphrase:

- [Here](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) there is the first one by _Trezor_;
- [Here](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) you can find the second one by _Coinkite_;
- And [here](https://armantheparman.com/passphrase/) you will find the last one by _armantheparman_.

## Exporting the wallet to Bitcoin Core

The wallet is now ready to be exported to software in order to interact with the Bitcoin network. In this guide, we will use Bitcoin Core (v24.1).

Refer to our installation and configuration guides for Bitcoin Core:

- **Running your own node with Bitcoin Core:** https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
- **Configuring Tor for a Bitcoin Core node:** https://agora256.com/configuration-tor-bitcoin-core/

First, insert a micro SD card into the Coldcard, then export the wallet for Bitcoin Core by following these steps: Advanced/Tools > Export Wallet > Bitcoin Core. Two files will be written to the micro SD card: bitcoin-core.sig & bitcoin-core.txt. Insert the micro SD card into the computer where Bitcoin Core is installed, and open the .txt file. You will see the line "For wallet with master key fingerprint." Verify that the eight-character XFP matches the one you noted when creating your private key.'
Before following the instructions in the file, let's start by preparing the wallet in the Bitcoin Core interface by following these steps: go to the File tab > Create a wallet. Choose a name for your wallet (interchangeable term with "porte-monnaie" in Core) and check the options Disable private keys, Create an empty wallet, and Wallet descriptors as shown in the image below. Then, press the Create button.

![create a wallet](assets/guide-agora/3.webp)

Once the wallet is created in Bitcoin Core, go to the Window tab > Console and make sure that the selected wallet at the top of the page displays the name of the one you created.

Now, in the .txt file generated by the Coldcard earlier, copy the line starting with importdescriptors, then paste it into the Bitcoin Core console. A response including the line "success": true should be returned.

![nodes window](assets/guide-agora/4.webp)

If the response contains "message": "Ranged descriptors should not have a label", erase the entry "label": "Coldcard xxxx0000" in the copied line from the .txt file, then paste the complete line back into the Bitcoin Core console.

If needed, you can find some help [here](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md) on Coldcard Github.

## Validation of wallet import in Bitcoin Core

To ensure that the operation was successful, it is necessary to validate that the desired wallet has been imported into Bitcoin Core. A simple method to confirm this is to verify that the addresses generated in the Coldcard correspond to the addresses generated in Bitcoin Core.

Bitcoin Core: Receive > Create a new receiving address
Coldcard: Address Explorer > Choose the address starting with bc1q. The Coldcard address 'bc1q' should match the address displayed in Bitcoin Core.
Receiving and sending transactions in 'air-gapped' mode

Receiving a transaction is extremely simple; just press Receive, label the transaction (optional but recommended), and Create a new receiving address. Then, all that's left is to share the address with the sender.

Now, the key element of this Coldcard + Bitcoin Core setup is sending transactions without the Coldcard and its private key being connected to the internet, a method called air-gapped that uses the TBSP (PSBT - Partially Signed Bitcoin Transactions) function of Bitcoin.
Essentially, we use the Bitcoin Core interface to construct a transaction, which we will then export via the micro SD card to the Coldcard for signing, and then return the signed transaction file to Bitcoin Core and broadcast the transaction to the network. We have to do it this way because the wallet imported into Bitcoin Core does not have a private key, only the public key (which allows us to generate our receiving addresses), so it is impossible for us to sign a transaction directly in the software to spend our bitcoins.

Before proceeding, make sure the following options are enabled in Settings > Wallet:

- Enable coin control features
- Spend unconfirmed coins (Optional)
- Enable TBPS checks

![option ](assets/guide-agora/5.webp)

### Steps to send in air-gapped mode:

Send > Inputs > choose the desired utxo, then enter the recipient's address in Pay to. Transaction fee: Choose... > Custom > Enter the transaction fee (Bitcoin Core calculates in sats/kilobyte instead of sat/byte like most alternative wallet solutions. So 4000 sats/kilobyte = 4 sats/byte). Create an unsigned transaction > save the file to your micro SD card and insert it into the Coldcard.

In the Coldcard, press Ready to sign, verify the transaction details, then press ✓ and insert the micro SD card back into the computer once the signed files are generated.

Back in Bitcoin Core, go to the File tab > Load TBSP from file, and enter the signed transaction file .psbt. The PSBT Operations box will appear on the screen, confirming that the transaction is fully signed and ready to be broadcasted. All that's left is to press Broadcast transaction.

![PSBT operations](assets/guide-agora/6.webp)

### Conclusion

The combination of the Coldcard device with Bitcoin Core, on which you run your own node, is powerful. Add to that a private key generated with 100 dice rolls and a secret phrase, and your wallet configuration becomes a sophisticated and robust fortress.

Feel free to contact us to share your comments and questions! Our goal is to share knowledge and increase our understanding day by day.
