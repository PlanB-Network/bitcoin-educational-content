---
name: Recovery Test
description: How to test your backups to ensure you don't lose your bitcoins?
---
![cover](assets/cover.webp)

When creating a Bitcoin wallet, you are asked to note down a mnemonic phrase, usually consisting of 12 or 24 words. This phrase allows you to recover access to your bitcoins in case of loss, damage, or theft of the device hosting your wallet. Before you start using your new Bitcoin wallet, it's very important to verify the validity of this mnemonic phrase. The best way to do this is by performing a dry-run recovery test.

This test involves simulating a wallet restoration before depositing any bitcoins into it. As long as the wallet is empty, we simulate a situation where the device hosting our keys is lost, and all we have left is our mnemonic phrase to attempt to recover our bitcoins.

![RECOVERY TEST](assets/notext/01.webp)

## What's the purpose?

This testing process allows you to verify that the physical backup of your mnemonic phrase, whether on paper or metal, is functional. A failure during this recovery test signals an error in the backup of the phrase, thereby putting your bitcoins at risk. On the other hand, if the test is successful, it confirms that your mnemonic phrase is fully operational, and you can then secure bitcoins with peace of mind using this wallet.

Performing a dry-run recovery test has a dual advantage. Not only does it allow you to check the accuracy of your mnemonic phrase, but it also gives you the opportunity to familiarize yourself with the wallet recovery process. This way, you'll discover potential difficulties before a real situation presents itself to you. On the day you actually need to recover your wallet, you'll be less stressed, as you'll already know the process, reducing the risk of error. That's why it's important not to neglect this testing step and to take the necessary time to do it correctly.

## What is a recovery test?

The process of the test is quite simple:
- After creating your new Bitcoin wallet, and before depositing your first satoshis, note down a witness information such as an xpub, the first receiving address, or even the master key fingerprint;
- Then, deliberately delete the still empty wallet, for example, by resetting your hardware wallet to factory settings;
- Next, simulate a recovery of your wallet using only the paper backups of your mnemonic phrase and your passphrase if you use one;
- Finally, check if the witness information matches that of the regenerated portfolio. If the information matches, you can be assured of the reliability of your physical backup, and you can then send your first bitcoins to this wallet.
Be careful, during a recovery test, **you must use the same device intended for your final wallet**, in order not to increase the attack surface of your wallet. For example, if you create a wallet on a Trezor Safe 5, make sure to perform the recovery test on this same Trezor Safe 5. It is important not to enter your recovery phrase into any other software, as this would compromise the security provided by your hardware wallet, even if the wallet is still empty.

## How to perform a recovery test?

In this tutorial, I will explain how to perform a recovery test on a Bitcoin software wallet, using Sparrow Wallet (for a hot wallet). However, the process remains the same for any other type of device. Again, **if you are using a hardware wallet, do not perform the recovery test on Sparrow Wallet** (see the previous section).

I have just created a new hot wallet on Sparrow Wallet. At the moment, I have not yet sent any bitcoins to it. It is empty.

![RECOVERY TEST](assets/notext/02.webp)

I have carefully noted my 12-word mnemonic phrase on a piece of paper. And since I want to enhance the security of this wallet, I have also set up a BIP39 passphrase that I have saved on another piece of paper:

```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```

```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```

***Obviously, you should never share your mnemonic phrase and your passphrase on the internet, unlike what I am doing in this tutorial. This example wallet will not be used and will be deleted at the end of the tutorial.***

I will now note down on a draft a witness piece of information from my wallet. You can choose different pieces of information, like the first receiving address, the xpub, or the master key fingerprint. Personally, I recommend choosing the first receiving address. This allows you to verify that you are able to find the complete first derivation path leading to this address.

On Sparrow, click on the "*Addresses*" tab.

![RECOVERY TEST](assets/notext/03.webp)

Then, note down on a piece of paper the very first receiving address of your wallet. In my example, the address is:

```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```

After noting the information, go to the "*File*" menu, then select "*Delete Wallet*". I remind you once again that your Bitcoin wallet must be empty before proceeding with this operation.

![RECOVERY TEST](assets/notext/04.webp)

If your wallet is indeed empty, confirm the deletion of your wallet.

![RECOVERY TEST](assets/notext/05.webp)

Now you need to repeat the wallet creation process, but using our paper backups. Click on the "*File*" menu and then on "*New Wallet*".

![RECOVERY TEST](assets/notext/06.webp)

Enter the name of your wallet again.

![RECOVERY TEST](assets/notext/07.webp)

In the "*Script Type*" menu, you need to choose the same script type as the wallet you previously deleted.

![RECOVERY TEST](assets/notext/08.webp)

Then click on the "*New or Imported Software Wallet*" button.

![RECOVERY TEST](assets/notext/09.webp)

Select the correct number of words for your seed.

![RECOVERY TEST](assets/notext/10.webp)

Enter your mnemonic phrase into the software. If an "*Invalid Checksum*" message appears, this indicates that the backup of your mnemonic phrase is incorrect. You will then have to start the creation of your wallet from scratch, as your recovery test has failed.

![RECOVERY TEST](assets/notext/11.webp)

If you have a passphrase, as in my case, also enter it.

![RECOVERY TEST](assets/notext/12.webp)

Click on "*Create Keystore*", then on "*Import Keystore*".

![RECOVERY TEST](assets/notext/13.webp)

And finally, click on the "*Apply*" button.

![RECOVERY TEST](assets/notext/14.webp)

You can now return to the "*Addresses*" tab.

![RECOVERY TEST](assets/notext/15.webp)

Finally, verify that the first receiving address matches the one you had noted as a witness on your draft.

![RECOVERY TEST](assets/notext/16.webp)

If the receiving addresses match, your recovery test is successful, and you can use your new Bitcoin wallet. If they do not match, this may indicate either an error in the choice of script type, which makes the derivation path incorrect, or a problem with the backup of your mnemonic phrase or your passphrase. In both cases, I strongly recommend starting from scratch and creating a new Bitcoin wallet from the beginning to avoid any risk. This time, take care to note the mnemonic phrase without errors.
Congratulations, you are now up to speed on conducting a recovery test! I advise you to generalize this process for the creation of all your Bitcoin wallets. If you found this tutorial helpful, I would appreciate it if you could leave a thumbs up below. Feel free to share this article on your social networks. Thank you very much!