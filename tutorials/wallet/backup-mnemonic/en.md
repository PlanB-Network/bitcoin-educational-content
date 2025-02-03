---
name: Save your mnemonic phrase
description: Discover best practices for safeguarding your Bitcoin wallet
---
![cover](assets/cover.webp)

When you create a new Bitcoin wallet, whether via a software or hardware wallet, you receive a mnemonic phrase consisting of 12 or 24 words. This phrase is very important, as it is the source of the derivation of all the private keys that secure your Bitcoins. It must therefore be carefully safeguarded to guarantee the recovery of your funds in the event of breakage, theft or loss of your wallet medium.

In this tutorial, we'll explore best practices for saving your mnemonic phrase securely, so you don't lose access to your bitcoins.

## Risk awareness

The mnemonic gives you full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to the medium hosting your wallet.

This means, for example, that if you use a Bitcoin wallet on a Ledger, anyone with access to your mnemonic phrase can steal your entire bitcoins, even without having access to the Ledger itself. This is why **you should never share your mnemonic phrase**, whatever the situation.

This phrase is therefore the unique information that enables you to restore access to your bitcoins in the event of loss, theft or damage to the wallet's media. Let's take the Ledger example again: if you lose the device, you can recover your funds by entering your mnemonic phrase on a new Ledger or any other compatible wallet, whether software or hardware.

So it's important to save this phrase with the utmost care and keep it in a secure place, as we'll detail in the following sections.

**Your mnemonic phrase is thus exposed to two main risks: theft and loss**

Theft can occur in two main ways:


- Someone has gained physical access to your backup, for example during a burglary or through a friend;
- You have voluntarily or involuntarily shared your sentence with another person.

To avoid physical theft of your mnemonic phrase backup, it's important to keep it in a secure place. We'll look at this point in detail in the following sections.

When it comes to remote theft attempts, always remember never to share your mnemonic phrase, whatever the situation. Phishing attempts are common: fraudulent e-mails, websites imitating those of official wallets or direct requests via various communication channels. If someone asks you for your passphrase, it's a scam, even in an emergency! It's common for thieves to pose as employees of the manufacturer of your hardware wallet, but be aware that these companies will never ask you for your passphrase, whatever the situation. So be extremely vigilant about any communications you receive, whether by email, telephone, post, social networks or even in person.

When you need to enter your phrase into a hardware wallet or software to restore access to your wallet after a problem with the initial support, take the time to check the authenticity and integrity of the hardware or software you're using. Don't panic, and proceed methodically.

Also, be careful when handling your mnemonic phrase. Make sure you're not being observed by other people or by a camera.

As far as the risk of loss is concerned, this can arise for three main reasons: the loss of the backup medium, its degradation or an error in its rating. We'll take a closer look at how to avoid or minimize these three risks in the following sections.

## The support

To save your recovery phrase, you need to write it down on a physical medium, such as paper or metal. Never use a digital medium: don't save it in a text file, take a picture of it or store it in a password manager. These methods considerably increase the attack surface compared with physical media. The rule is therefore clear: use paper, cardboard or metal to save your phrase.

While writing down your phrase on a simple piece of paper is already good practice, opting for a metal holder, such as stainless steel, offers added security. This type of holder protects your mnemonic phrase from the risks of fire, flood or collapse that can affect the storage location.

For those looking for an economical option for backing up their phrase on metal, [the DIY method of the "*SAFU Ninja*"](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/) is an excellent solution. All you need to do is buy metal washers, a screw and a nut in the shops. Then you engrave the words of your sentence on each washer, making sure to number them, and assemble them on the screw with the nut. This low-cost method already offers good resistance.

![SEED](assets/fr/01.webp)

Image credit: [*SAFU Ninja Review*, Jameson Lopp](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/).

If you prefer to invest in a complete metal backup device, I recommend you take a look at [Jameson Lopp's resistance tests](https://jlopp.github.io/metal-bitcoin-storage-reviews/), which evaluate most of the solutions available on the market. I'd advise you to opt for one-piece brackets, such as a metal plate for engraving, stamping or punching. These devices generally offer much greater resistance than systems using independent letters to be assembled.

If you opt for a paper wallet, you have several options: a simple blank sheet of paper, the cardboard wallet often supplied with your hardware wallet, or our downloadable template which you can print out [by clicking here](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/wallet-backup-sheet/assets/mnemonic-sheet.pdf).

![SEED](assets/fr/02.webp)

## Backup

Now that you've chosen your physical medium, it's time to write down your recovery phrase! To avoid losing your bitcoins, follow these best practices.

First of all, make sure you're not being observed, either by other people or by cameras, as you write down your sentence.

Then take the time to write each word clearly and legibly. You may need to reread your sentence years from now, or someone else may need to do so as part of an inheritance. Careful handwriting is therefore essential.

In theory, it's possible to write only the first 4 letters of each word, because in the list of 2048 words in BIP39, no two words share the same first 4 letters in the same order. However, if your medium has sufficient space, I recommend that you save each word in its entirety. This can be useful in the event of partial media degradation. For example, if you only note `accu` for the word `accuse` and the letter `u` disappears, you may have to choose between `accuse`, `access`, `accident` or `account`. On the other hand, with the whole word, even if one letter is missing, it's still easy to recognize the correct word.

It's also essential to write your words in the right order. If you have your 24 words but don't know their exact sequence, it will be impossible to recover your wallet. Numbering the words is just as important: if the medium is damaged or the words become disorganized, numbering them will enable you to easily put them back in the right order.

![SEED](assets/fr/03.webp)

Furthermore, it's important to understand that, theoretically, the mnemonic phrase alone isn't always enough to regain access to your bitcoins. You also need to know the derivation paths used to generate the keys. If you use a SingleSig wallet with a standard path, it will be relatively simple to recover your keys. However, with a non-standard path, this could become impossible, even in possession of the mnemonic phrase. To avoid this problem, I strongly recommend that you note, on your media, the derivation path of the account you're using. You can find this information in the settings of your wallet software. For example, for a standard Taproot wallet, the default derivation path will be :

```txt
m / 86' / 0' / 0' /
```

![SEED](assets/fr/04.webp)

If you use a multisig wallet or a wallet with complex scripts including recovery keys, such as those offered by the Liana software, it is essential to save your **Output Script Descriptors**. These descriptors contain all the information you need, in addition to the recovery phrases, to regain access to your bitcoins.

You can also enrich your backup with additional information related to your wallet support. For example, note the PIN code used to unlock your hardware wallet, or the anti-phishing words if you use a COLDCARD.

![SEED](assets/fr/05.webp)

On the other hand, if you use a passphrase, make sure you don't write it down on the same medium as your mnemonic phrase. The purpose of the passphrase is to protect your wallet in the event of theft. To find out more about how to use a passphrase, take a look at this complementary tutorial:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Once you've saved your mnemonic phrase on physical media, it's strongly recommended that you perform a recovery test while your newly-created wallet is still empty. This test consists of writing down a sample piece of information, deliberately deleting the empty wallet, then trying to restore it using only your physical backup of the mnemonic phrase. This will enable you to check that your backup is complete and free of input errors. It also allows you to familiarize yourself with the recovery process. This way, if you need to recover in the future, you'll be better prepared and avoid the stress of a first attempt in a real-life situation. To find out more about how to carry out this test, see this other tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
Finally, there's the question of the number of backups. This choice depends entirely on your personal situation. Limiting the number of copies, for example by writing your mnemonic phrase only once on a medium, reduces the risk of theft, but increases the risk of loss. Conversely, making several copies reduces the risk of loss, but increases the risk of theft. So it's up to you to find the right balance for your needs, and determine the number of copies you feel is most appropriate.

## Storage

Now that you've carefully backed up your mnemonic phrase, it's time to choose a suitable storage location. This will depend on your security strategy. In any case, choose a place that's out of sight, where it's unlikely someone will stumble across it, yet accessible for periodic checks. Make sure it's protected from the elements, too, to prevent damage to the substrate.

I would also advise against storing your mnemonic in places where you are not sovereign, such as a safe deposit box at a notary's office or a bank. These options may seem secure, but they imply that you depend on a third party to access your backup, which goes against Bitcoin's fundamental principles.

For added security, I recommend using a tamper-proof plastic pouch or similar sealing system. This will enable you to check that no one has gained access to your phrase. For example, if you store your phrase at home and receive guests, it may be impossible to know whether anyone has seen, memorized or photographed it. A tamper-proof pouch makes this kind of verification simple: if it's intact, you can be sure that your phrase has remained secret. These fully opaque sleeves are available online or in specialized Bitcoin stores.

![SEED](assets/fr/06.webp)

Finally, when your phrase is stored in a tamper-proof envelope, don't forget to note the envelope's unique identifier. This will enable you to verify its authenticity during your checks.

## Time management

Now that your phrase is carefully stored, it's important to set up regular monitoring. Periodically, check that your phrase is still present in its storage location, and that its opaque envelope has not been opened.

During these checks, you can also open the envelope to examine the condition of the substrate. Make sure it is undamaged and that the sentence is still perfectly legible. If you notice any signs of damage, it's best to create a new copy from your hardware wallet. Check that this new copy is functional, then destroy the damaged backup cleanly to avoid any risk of leakage.

Finally, mnemonic phrase management also raises the question of inheritance. This subject will be covered in detail in a future tutorial.

## Going further

To go one step further and further strengthen your security strategy, I recommend that you learn the technical workings of your Bitcoin wallet. By understanding how the various elements interact, as well as their importance and implications, you'll be able to fine-tune your security strategy with full awareness of the risks involved. In particular, if you understand at a technical level what the mnemonic phrase enables, you'll be able to adjust the way you record, store and manage it over time.

That's why I invite you to take the free CYP201 training course offered by Plan ₿ Network. This training course explains in detail all the workings of Bitcoin wallets, enabling you to master the technical aspects essential to effectively securing your funds :

https://planb.network/courses/cyp201
If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!