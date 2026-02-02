---
name: BIP-39 Passphrase SeedSigner
description: How do I add a passphrase to my SeedSigner wallet?
---

![cover](assets/cover.webp)


A passphrase BIP39 is an optional password which, combined with the mnemonic phrase, provides an additional layer of security for deterministic and hierarchical Bitcoin wallets. In this tutorial, we'll discover together how to set up a passphrase on your Bitcoin wallet used with a SeedSigner.


![Image](assets/fr/01.webp)


## Prerequisites before adding a Passphrase


Before starting this tutorial, if you're not familiar with the passphrase concept, how it works and its implications for your Bitcoin wallet, I strongly recommend that you consult this other theoretical article where I explain everything (this is very important, as using a passphrase without fully understanding how it works can put your bitcoins at risk) :


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Before starting this tutorial, please also make sure that you have already initialized your SeedSigner and generated your mnemonic phrase. If you haven't, and your SeedSigner is brand new, follow the tutorial on Plan ₿ Academy. Once you've completed this step, you can return to this tutorial:


https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## How do I add a passphrase to the SeedSigner?


Adding a passphrase to your wallet managed via SeedSigner creates a completely new wallet, generating an entirely separate set of keys. Consequently, if you already have a wallet containing satss, you will no longer be able to access it with the passphrase, since it generates a completely different wallet.


To apply a passphrase to your SeedSigner, switch on the device and scan your SeedQR as usual. The SeedSigner will then display the fingerprint of your current wallet, corresponding to the one **without passphrase**. The wallet with passphrase will have a different fingerprint.


Click on the `BIP-39 Passphrase` button.


![Image](assets/fr/02.webp)


Then enter the passphrase of your choice in the field provided, using the on-screen keyboard. Be sure to make one or more physical backups (paper or metal): loss of this passphrase will result in permanent loss of access to your bitcoins. **To restore a wallet, both the mnemonic and the passphrase are essential ** If either is lost, your bitcoins will be irretrievably blocked.


Once you've completed your entry, validate by pressing the `KEY3` button at the bottom right of the SeedSigner.


![Image](assets/fr/03.webp)


*In this example, I used the passphrase `pba`. However, in your case, make sure you choose a robust passphrase. To find out how to define an optimum passphrase, please consult this other article:*


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

The SeedSigner then displays the new fingerprint of your passphrase wallet. Make several copies of this fingerprint: it's important when using a wallet with passphrase, as it allows you to check, each time you enter the passphrase, that you haven't made any typing errors and that you're accessing the right wallet.


For example, if in my case I mistakenly write down the passphrase `Pba` when starting the SeedSigner instead of `pba`, this simple change from lower case to upper case will result in the creation of an entirely different wallet from the one I want to access.


This fingerprint poses no risk to the security or confidentiality of your wallet. It does not disclose any information, public or private, about your keys. So, unlike the mnemonic and passphrase, you can save the fingerprint on a digital medium. I recommend that you keep a copy in several places: on a piece of paper, in a password manager, etc.


Once you've saved your fingerprint, click `Done`.


![Image](assets/fr/04.webp)


You then have access to all your wallet's functions, just like on a classic SeedSigner.


![Image](assets/fr/05.webp)


You can now import the keystore into Sparrow Wallet and use your wallet as normal. Each time you restart, you'll need to both scan your SeedQR and re-enter your passphrase using the keyboard, as we did here.


Before you actually use your wallet with passphrase, I strongly recommend that you perform a full empty recovery test. This will allow you to confirm that your backups of the mnemonic phrase and passphrase are valid. To learn how to perform this check, see the following tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895