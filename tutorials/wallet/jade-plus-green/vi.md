---
name: Jade Plus - Green
description: Easily configure Jade Plus with Green
---
![cover](assets/cover.webp)

Jade Plus is a Bitcoin-only hardware wallet designed by Blockstream. It is the successor to the classic Jade, with software enhancements, more options and redesigned ergonomics for more intuitive use. This new version boasts a magnificent 1.9-inch LCD screen, with a wider color gamut than its predecessor. Buttons and menu navigation have also been optimized.

The Jade Plus can be used in a number of ways: via a USB-C wired connection, in "*Air-Gap*" mode with a micro SD card (adapter required), via Bluetooth or even by exchanging QR codes thanks to the integrated camera. This hardware wallet is battery-powered.

It is available from $149.99 in the basic black version, and the price can rise by up to $20 for the "*Genesis Grey*" or "*Lunar Silver*" versions. The Jade Plus is therefore an interesting choice, with advanced functionalities comparable to those of high-end hardware wallets such as Coldcard Q or Passport V2, but at a fairly low price, close to mid-range models.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus is compatible with most portfolio management software. Here is a summary of compatibility at the time of writing (January 2025):

| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |

| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

In this tutorial, we'll set up and use the Jade Plus with Blockstream's Green Wallet mobile app via a Bluetooth connection. This setup is ideal for beginners. If you're looking for a more advanced approach, I recommend you take a look at this tutorial where we use the Jade Plus with Sparrow Wallet in QR codes mode:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
## The Jade Plus safety model

The Jade Plus uses a security model based on a "virtual secure element", materialized by a "blind oracle". In concrete terms, this mechanism combines the PIN chosen by the user, a secret hosted on the Jade and a secret held by the oracle (a server maintained by Blockstream), to create an AES-256 key distributed over two entities. During initiation, an ECDH exchange secures communication with the oracle, and encrypts the recovery phrase on the hardware wallet. In practical terms, when you want to access the seed to sign transactions, you need access to :


- To the Jade Plus device itself;
- To PIN to unlock the device ;
- And to the secret of the oracle.

The major advantage of this approach is the absence of a single point of failure at hardware level, since if an attacker ever gains access to your Jade, extracting the keys requires simultaneously compromising the Jade and the oracle. This model also means that Jade Plus is entirely open-source, avoiding the constraints associated with the use of true physical secure elements, such as those used on Ledger, for example.

The disadvantage of this system is that the use of Jade Plus depends on the oracle maintained by Blockstream. If this oracle becomes inaccessible, it is no longer possible to use the hardware wallet directly with the PIN. However, this does not mean that your bitcoins are lost, as they can still be recovered using your recovery phrase, which you can enter in Jade Plus in "*stateless*" mode. To get around this dependency, you can also configure and manage your own oracle server.

## Unboxing the Jade Plus

When you receive your Jade Plus, check that the box and seal are in good condition to ensure that your package has not been opened.

![JADE-PLUS-GREEN](assets/fr/02.webp)

In the box you will find :


- Le Jade Plus;
- USB-C cable;
- Cards to record your mnemonic phrase as words or as "*CompactSeedQR*";
- Some instructions for use ;
- A cord;
- Some stickers.

![JADE-PLUS-GREEN](assets/fr/03.webp)

The device has 4 navigation buttons:


- The button on the bottom right turns the Jade on;
- The large button on the front of the device is used to select an item;
- The two small buttons at the top allow you to navigate left and right;
- You can also select an item by simultaneously clicking on the two buttons at the top of the device.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Setting up a new Bitcoin wallet

Click on the start button.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Click on "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Choose "Begin Setup". The "*Advanced Setup*" option does the same thing, but with access to advanced settings.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Then click on "*Create a New Wallet*" to generate a new seed.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Click on the "*Continue*" button to display your new recovery phrase.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Your Jade Plus displays your 12-word mnemonic phrase. **This mnemonic gives you full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to your Jade Plus. The 12-word phrase restores access to your bitcoins in the event of loss, theft or breakage of your Jade. It is therefore very important to save it carefully and store it in a secure location.

You can write it on the cardboard supplied in the box, or for added security, I recommend engraving it on a stainless steel base to protect it from fire, flood or collapse.

![JADE-PLUS-GREEN](assets/fr/10.webp)

For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
***Obviously, you must never share these words on the Internet, as I do in this tutorial. This sample portfolio will be used only on Testnet and will be deleted at the end of the tutorial

Click on the arrow on the right of the screen to display the following words.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Once you've saved your phrase, Jade Plus asks you to confirm it. Select the correct word according to the order using the buttons at the top of the device, and click the central button to move on to the next word.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Connecting Jade Plus to Green Wallet

In this tutorial, we'll use the Green Wallet application to manage the wallet hosted on the Jade Plus. This method is particularly suitable for beginners. If you'd like to manage your Bitcoin wallet in more detail, you can also use Sparrow Wallet, which we'll cover in a separate tutorial:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
For instructions on installing and setting up the Blockstream Green application, please see the first part of this other tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
Once on the Blockstream Green application, click on the "*Configure a new portfolio*" button.

![JADE-PLUS-GREEN](assets/fr/13.webp)

Select "*On Hardware Wallet*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Activate Bluetooth on your smartphone, then click on the "*Connect your Jade*" button.

![JADE-PLUS-GREEN](assets/fr/15.webp)

Authorize the Green application to access Bluetooth connections.

![JADE-PLUS-GREEN](assets/fr/16.webp)

The application is looking for your Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

On the Jade Plus, click on the "*Bluetooth*" menu.

![JADE-PLUS-GREEN](assets/fr/18.webp)

Select your device on the Green application.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Confirm the pairing code on your Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green offers you a test to ensure that your Jade is genuine. Click on the button to do so.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Confirm on the Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Green confirms that your device is genuine.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Setting the PIN code

Click on the "*Continue*" button to choose your Jade's PIN code.

![JADE-PLUS-GREEN](assets/fr/24.webp)

The PIN code unlocks your Jade. It is therefore a protection against unauthorized physical access. This PIN code is not involved in the derivation of your wallet's cryptographic keys. So, even without access to this PIN code, possession of your 12-word mnemonic phrase will enable you to regain access to your bitcoins. We recommend choosing a PIN code that is as random as possible. And be sure to save this code in a separate location from where your Jade is stored (e.g. in a password manager).

Choose the 6-digit PIN code on your Jade, using the right and left buttons to scroll through the digits, and the middle button to confirm the entry of a digit.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Confirm your PIN a second time.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Your bitcoin wallet has been created.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Create a Bitcoin account

You must now create an account within your portfolio. Click on the "*Create an account*" button.

![JADE-PLUS-GREEN](assets/fr/28.webp)

Choose "*Standard*" if you wish to create a classic single-sig portfolio.

![JADE-PLUS-GREEN](assets/fr/29.webp)

For more information on the "*2FA*" option, you can follow this other tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9
Your account has been created.

![JADE-PLUS-GREEN](assets/fr/30.webp)

If you wish to personalize your Green portfolio, click on the three small dots at top right.

![JADE-PLUS-GREEN](assets/fr/31.webp)

The "*Rename*" option lets you customize the name of your portfolio, which is particularly useful if you manage several portfolios on the same application. The "*Unit*" menu lets you change the basic unit of your portfolio. For example, you can choose to display it in satoshis rather than bitcoins. Finally, the "*Parameters*" menu gives you access to other options. Here, for example, you'll find your extended public key and its descriptor, useful if you're planning to set up a watch-only wallet from your Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

To reconnect to your Jade after switching it off, press the on/off button at the bottom of the device. On the Green application, select your device from the home page:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Then enter the PIN code on your Jade, and you'll be connected again.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Your Jade is unlocked via Blockstream's "virtual secure element" (see the first section of this tutorial). This requires a Bluetooth connection with the Green application. If you encounter difficulties with the Bluetooth connection during unlocking, try dissociating and reassociating the two devices. If the problem persists, you can still unlock your Jade by selecting the "*QR Scan*" option and following the instructions available [on the Blockstream website](https://jadefw.blockstream.com/pinqr/index.html).

Before you receive your first bitcoins in your wallet, **I strongly advise you to perform an empty recovery test**. Make a note of some reference information, such as your xpub or first receiving address, then delete your wallet on the Green app and on the Jade Plus while it's still empty (`Options -> Device -> Factory Reset`). Then try to restore your wallet using your paper backups of the mnemonic phrase. Check that the cookie information generated after the restore matches the one you originally wrote down. If it does, you can rest assured that your paper backups are reliable. To find out more about how to carry out a test recovery, please consult this other tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Receive bitcoins

Now that your Bitcoin wallet is set up, you're ready to receive your first sats! Simply click on the "*Receive*" button on the Green application.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Green displays a reception address, but before using it, it's essential to check it on the Jade to confirm that it actually belongs to our portfolio. To do this, click on the "*Verify on device*" button.

![JADE-PLUS-GREEN](assets/fr/36.webp)

Check on the Jade that the address is the same as on Green, then click on the button to confirm.

![JADE-PLUS-GREEN](assets/fr/37.webp)

You can now share the address with the payer to receive bitcoins in your wallet. When the transaction is broadcast on the network, it will appear in your wallet. Wait until you've received enough confirmations to consider the transaction definitive.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Send bitcoins

With bitcoins in your wallet, you can now also send bitcoins. Click on "*Send*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

On the next page, enter the recipient's address. You can enter it manually or scan a QR code.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Choose the payment amount.

![JADE-PLUS-GREEN](assets/fr/41.webp)

At the bottom of the screen, you can select the fee rate for this transaction. You have the choice of following the application's recommendations or customizing your fees. The higher the fee in relation to other pending transactions, the faster your transaction will be processed. For fee market information, please visit [Mempool.space](https://mempool.space/) in the "*Transaction Fees*" section.

![JADE-PLUS-GREEN](assets/fr/42.webp)

Click on "*Next*" to access the transaction summary screen. Check that the address, amount and charges are correct.

![JADE-PLUS-GREEN](assets/fr/43.webp)

If all goes well, slide the green button at the bottom of the screen to the right to sign and broadcast the transaction on the Bitcoin network.

![JADE-PLUS-GREEN](assets/fr/44.webp)

You are now asked to confirm the transaction on the Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Make sure the recipient's address is correct. Click on the checkmark to confirm.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Check that the charge amount is correct, then validate.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Your transaction has been signed and broadcast from Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Congratulations, you now know how to set up and use the Jade Plus with the Blockstream Green mobile application, via Bluetooth connection. If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thanks for sharing!

To take things a step further, I recommend this tutorial on the Jade Plus, where we configure it with Sparrow Wallet software in QR mode. You'll also learn how to use the advanced settings of your hardware wallet:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262