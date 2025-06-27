---
name: passphrase BIP39 Trezor
description: How do I add a passphrase to my Trezor wallet?
---
![cover](assets/cover.webp)


A passphrase BIP39 is an optional password which, combined with the mnemonic phrase, provides an additional layer of security for deterministic and hierarchical Bitcoin wallets. In this tutorial, we'll discover together how to set up a passphrase on your secure Bitcoin wallet on a Trezor (Safe 3, Safe 5 and Model One).


![Image](assets/fr/01.webp)


Before starting this tutorial, if you're not familiar with the passphrase concept, how it works and its implications for your Bitcoin wallet, I strongly recommend that you consult this other theoretical article where I explain everything (this is very important, as using a passphrase without fully understanding how it works can put your bitcoins at risk) :


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase on Trezor is handled in the classic way if you've opted for the BIP39 standard during configuration (which I recommend if you don't need *Multi-share Backup*). What's special about Trezor is that you can either enter the passphrase directly on the Hardware Wallet, or via your computer's keyboard using the Trezor Suite software. This second option is considerably less secure, as the computer has an immensely larger attack surface than the Hardware Wallet. However, typing a complex passphrase may be faster on a conventional keyboard than on the Hardware Wallet, which could encourage the use of strong passphrases. So it's always better to use a passphrase, even if it has to be typed, than not to use one at all. It is important, however, to remain aware of the increased risk of numerical attacks that this implies.


These options are not available on all Trezor-compatible wallet management software. For example, for the Model One, passphrase can be entered via the keyboard on Sparrow Wallet. For Model T, Safe 3 and Safe 5 models, you must either use Trezor Suite or enter passphrase directly on Hardware Wallet, as the option of entering via Sparrow was disabled by HWI a few years ago.


![Image](assets/fr/02.webp)


In Trezor Suite, you have two different ways of managing passphrase demand. You can activate the "*passphrase*" option in the "*Device*" tab. If enabled, Trezor Suite and all other wallet management software will systematically ask you to enter your passphrase each time you start up. If you prefer a more discreet approach to using a passphrase, you can keep the setting at "*Standard*". In this case, you'll need to manually access your Hardware Wallet's menu in the top left-hand corner, and click on the "*+ passphrase*" button each time you start it up.


Before starting this tutorial, please ensure that you have already initialized your Trezor and generated your mnemonic phrase. If you haven't, and your Trezor is new, follow the model-specific tutorial available on Plan ₿ Network. Once you've completed this step, you can return to this tutorial.


https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Adding a passphrase to a Safe 3 or Safe 5


Once you've created your wallet, saved your mnemonic and set a PIN, you'll be taken to the Trezor Suite home menu. In the top left-hand corner, a window should appear inviting you to activate the passphrase BIP39.


![Image](assets/fr/03.webp)


If this window doesn't appear, you'll need to manually activate the "*passphrase*" option in the "*Device*" settings tab.


![Image](assets/fr/04.webp)


This window asks you to enter your passphrase. Choose a strong passphrase and immediately make a physical backup, on a medium such as paper or metal. In this example, I've chosen the passphrase: `fH3&kL@9mP#2sD5qR!82`. This is an example; however, I recommend you choose a slightly longer passphrase. Between 30 and 40 characters would be ideal (like a good password).


of course, you should never share your passphrase on the Internet, as I do in this tutorial. This example wallet will only be used on Testnet and will be deleted at the end of the tutorial.**_


For more specific recommendations on choosing your passphrase, I invite you once again to consult this other article:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

If you want to enter your passphrase via your computer keyboard, enter it in the field provided, then click on "*Access passphrase Wallet*".


![Image](assets/fr/05.webp)


Your Hardware Wallet will then display your passphrase. Make sure it matches your physical backup (paper or metal) before clicking on the screen to continue.


![Image](assets/fr/06.webp)


This will give you access to your passphrase-protected wallet.


![Image](assets/fr/07.webp)


If you prefer to enhance security by entering your passphrase only on your Trezor, when prompted, click on "*Enter passphrase on Trezor*".


![Image](assets/fr/08.webp)


A T9 keyboard will appear on your Trezor, allowing you to enter your passphrase. Once you've completed your entry, click on the green tick to apply the passphrase to your wallet.


![Image](assets/fr/09.webp)


You will then have access to your passphrase secure wallet.


![Image](assets/fr/10.webp)


To use Sparrow Wallet, the procedure is similar, but for models T, Safe 3 and Safe 5, passphrase must be entered on the Hardware Wallet and not via the computer keyboard.


Whenever Sparrow Wallet requires access to your Trezor, and passphrase has not yet been applied since the last start-up, you'll need to enter it using the T9 keyboard.


![Image](assets/fr/11.webp)


## Adding a passphrase to a Model One


On the Model One, the use of a passphrase BIP39 is almost indispensable. As this device does not incorporate a Secure Element, it is relatively easy to extract sensitive information. It is therefore not resistant to physical attack. However, as the passphrase is not retained on the device after it has been switched off, using a strong (non-bruteable) passphrase can protect you against most known physical attacks on this model.


On the Model One, it's not possible to enter the passphrase directly on the Hardware Wallet. You'll need to enter it via your computer keyboard.


Once you've created your wallet, saved your mnemonic and set a PIN, you'll be taken to the Trezor Suite home menu. In the top left-hand corner, a window inviting you to activate the passphrase BIP39 should appear.


![Image](assets/fr/12.webp)


If this window does not appear, you need to activate the "*passphrase*" option in the "*Device*" tab of the settings.


![Image](assets/fr/13.webp)


This window asks you to enter your passphrase. Choose a strong passphrase and immediately make a physical backup, on a medium such as paper or metal. In this example, I've chosen the passphrase: `fH3&kL@9mP#2sD5qR!82`. This is just an example; however, I recommend that you choose a slightly longer passphrase. Between 30 and 40 characters would be ideal (like a good password).


For more specific recommendations on choosing your passphrase, I invite you once again to consult this other article:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Enter your passphrase in the field provided, then click on the "*Access passphrase Wallet*" button.


![Image](assets/fr/14.webp)


Your Hardware Wallet will display your passphrase. Make sure it matches your physical backup (paper or metal), then click on the right-hand button to continue.


![Image](assets/fr/15.webp)


This will take you to your passphrase-protected wallet.


![Image](assets/fr/16.webp)


To use Sparrow Wallet thereafter, the procedure remains the same. Each time Sparrow requires access to your Hardware Wallet, and the passphrase has not been entered since the device was last started up, you will need to enter it.


![Image](assets/fr/17.webp)


Congratulations, you're now up to speed on using the passphrase BIP39 on Trezor hardware wallets. If you'd like to take your wallet security a step further, check out this tutorial on Trezor's *Multi-share* backup systems (*Shamir's Secret Sharing Scheme*):


https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!