---
name: COLDCARD Q - Advanced
description: Using COLDCARD Q's advanced options
---
![cover](assets/cover.webp)

In a previous tutorial, we covered the initial configuration of the COLDCARD Q and its basic functions for beginners. If you've just received your COLDCARD Q and haven't set it up yet, I recommend you start with that tutorial before continuing here:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
This new tutorial is dedicated to COLDCARD Q's advanced options, designed for advanced and paranoid users. In fact, COLDCARDs are distinguished from other hardware wallets by their many advanced security features. Of course, you don't have to use all these options. Just choose the ones that suit your security strategy.

**Warning**, incorrect use of some of these advanced options may result in the loss of your bitcoins or the destruction of your hardware wallet. I therefore strongly recommend that you read the advice and explanations for each option carefully.

Before you start, make sure you have access to a physical backup of your 12- or 24-word mnemonic phrase, and check its validity via the following menu: `Advanced/Tools > Danger Zone > Seed Functions > View Seed Words`.

![CCQ](assets/fr/01.webp)

## The BIP39 passphrase

If you don't know what a BIP39 passphrase is, or if it's not entirely clear to you how it works, I strongly recommend that you take a look at this tutorial beforehand, which covers the theoretical bases needed to understand the risks associated with using a passphrase :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Bear in mind that once you've set up the passphrase on your wallet, your mnemonic alone won't be enough to regain access to your bitcoins. You'll need both the mnemonic and the passphrase. What's more, you'll need to enter the passphrase every time you unlock your COLDCARD Q. This enhances security by making physical access to the COLDCARD and knowledge of the PIN insufficient without the passphrase.

On COLDCARDs, you have two options for managing your passphrase:

1. **Classic entry:** You enter the passphrase manually each time you use your hardware wallet, just as you do with other hardware wallets. COLDCARD Q simplifies this task with its full keyboard.

2. **You can choose to encrypt your passphrase and store it on a microSD card. In this case, you'll need to insert the microSD into the COLDCARD Q each time you use it. Note that this microSD will only work on your COLDCARD Q and is not a backup. It is therefore very important that you also keep a copy of your passphrase on a physical medium, such as paper or metal.

To set your BIP39 passphrase, access the "*Passphrase*" menu.

![CCQ](assets/fr/02.webp)

Enter your passphrase using the keyboard. Be sure to choose a strong passphrase (long and random) and make a physical backup.

![CCQ](assets/fr/03.webp)

Once you've set your passphrase, COLDCARD Q will show you the master key fingerprint of the new wallet associated with this passphrase. Be sure to save this fingerprint. When you re-enter your passphrase when you use your device in the future, you'll be able to check that the fingerprint displayed matches the one you saved. This check ensures that you haven't made a mistake when entering your passphrase.

![CCQ](assets/fr/04.webp)

You can now press "*ENTER*" to apply this passphrase to your mnemonic phrase and activate the new wallet. If you prefer to save this passphrase on a microSD, insert the card in the appropriate slot and press "*1*".

![CCQ](assets/fr/05.webp)

Your passphrase is now applied. The key imprint appears on the home screen and at the top of the screen.

![CCQ](assets/fr/06.webp)

Each time you unlock your COLDCARD Q, you'll need to access the "*Passphrase*" menu and enter your passphrase in the same way as above, to apply it to the mnemonic stored in the device and access the correct Bitcoin wallet.

![CCQ](assets/fr/07.webp)

If you've saved the passphrase on a microSD card, each time you use it, insert it into the COLDCARD and access the "*Passphrase*" menu. Your COLDCARD will load the passphrase directly from the microSD, so you won't need to enter it manually. Click on "*Restore Saved*".

![CCQ](assets/fr/08.webp)

Check that the length and first letter of the loaded passphrase are correct.

![CCQ](assets/fr/09.webp)

Confirm that the fingerprint displayed matches that of your wallet and click on "*Restore*".

![CCQ](assets/fr/10.webp)

Keep in mind that using a passphrase means you'll need to import a new set of keys derived from the combination of your mnemonic phrase and passphrase into your wallet management software (like Sparrow Wallet). To do this, follow the step "*Configure a new wallet on Sparrow*" in this other tutorial :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Unlocking options

COLDCARDs also benefit from a host of options for the device unlocking process. Let's find out more about these advanced options.

### Trick PINs

A Trick PIN is a secondary PIN code distinct from the one defined during initial device configuration. This code is used to trigger specific pre-configured actions as soon as it is entered when the COLDCARD is switched on. You can configure several Trick PINs, each linked to a different action. These features enable you to tailor your COLDCARD to your personal security strategy. They are particularly useful in cases of physical duress, such as during a robbery (commonly referred to in the Bitcoin community as a "*$5 wrench attack*").

To activate a Trick PIN and associate it with an action, access the `Settings > Login Settings > Trick PINs` menu.

![CCQ](assets/fr/11.webp)

Select "*Add New Trick*".

![CCQ](assets/fr/12.webp)

Set the PIN code to be associated with the action and remember to save it.

![CCQ](assets/fr/13.webp)

Then choose the action to be performed automatically each time you enter this Trick PIN. Here's the list of actions available for a PIN:


- "*Brick Self*: This action destroys both COLDCARD Q chips if the Trick PIN is entered, rendering the device totally unusable. It will then be impossible to resell, reuse or even return it to Coinkite. The device will become irretrievably obsolete. This feature can be used in the event of a robbery to convince an assailant that he will never be able to access your bitcoins. **Please note**: without a physical backup of your mnemonic phrase and any passphrase, your bitcoins will be permanently lost.

![CCQ](assets/fr/14.webp)


- "*Wipe Seed*": This menu offers several actions for deleting the seed, i.e. resetting the COLDCARD without destroying it. Unlike the "*Brick Self*" option, it will be possible to reconfigure the device using a backup of your mnemonic phrase. However, without this backup, your bitcoins will be lost. Here are the available options:
 - "*Wipe & Reboot* : Removes the seed and reboots the COLDCARD without displaying any information on the screen.
 - "*Silent Wipe*": Silently wipes the seed, and unlocks the COLDCARD on a random fake wallet as if nothing had happened.
 - "*Wipe -> Wallet*": Removes the seed discreetly and unlocks the COLDCARD on a pre-configured secondary wallet, designed as a bait. This wallet may contain a small portion of your bitcoin savings to satisfy an attacker.
 - "*Say Wiped, Stop*": Deletes the seed and displays the message `Seed is wiped, Stop` on the screen.

![CCQ](assets/fr/15.webp)


- "*Duress Wallet*": With this action, the Trick PIN code unlocks a wallet derived from the seed using the BIP85. This secondary wallet can be used as bait to satisfy an attacker. The COLDCARD acts as if it were the real wallet, but without the master PIN (different from the Trick PIN), the attacker will never be able to access the real wallet. This strategy is designed to make people believe that the wallet linked to the Trick PIN is the only one in existence.

![CCQ](assets/fr/16.webp)


- "*Login Countdown*": This menu groups actions with a countdown before they are executed. **Warning**, some of them may destroy your device or result in the loss of your bitcoins. Here are the available sub-actions:
 - "*Wipe & Countdown* : Clears the seed from the COLDCARD's memory, then starts a one-hour countdown. Without saving your mnemonic or passphrase, your bitcoins will be lost. This option is designed to fool an attacker into thinking that the device will unlock at the end of the countdown, when in fact it will be reset to factory settings.
 - "*Countdown & Brick*": Starts a one-hour countdown, at the end of which the COLDCARD destroys its two secure chips, rendering it permanently unusable. Without backup, your bitcoins will be lost. This action is designed to fool an attacker, who thinks he's waiting for an unlock, when in fact the device will self-destruct.
 - "*Just Countdown* : Triggers a simple one-hour countdown, after which the COLDCARD restarts without any further action. The seed is not deleted and the device remains intact. Be careful not to confuse this action with the "*Login Countdown*" option, discussed in the following sections, which adds a countdown to the main PIN while giving access to the real wallet.

![CCQ](assets/fr/17.webp)


- "*Look Blank*": This action makes the COLDCARD appear empty, giving the impression that the seed has been deleted. In reality, nothing happens and the seed remains intact. This simulates an unused or reset COLDCARD.

![CCQ](assets/fr/18.webp)


- "*Just Reboot* : When the Trick PIN is used, the COLDCARD simply reboots. No other action is performed.

![CCQ](assets/fr/19.webp)


- "*Delta Mode*": This complex action, reserved for experienced users, is designed to counter highly sophisticated duress attacks, whether from a state or a relative with privileged information. When Delta Mode is activated, COLDCARD provides access to the real wallet, enabling an attacker to navigate and verify that it is the correct wallet. However, transaction signatures are blocked, thus preventing any bitcoin transfer. In addition, access to the mnemonic phrase is disabled and any attempt to retrieve it will result in its deletion. To enhance credibility, the Trick PIN used with Delta Mode must share the same prefix as the real PIN (to display the same anti-phishing words), but the suffix must be different.

![CCQ](assets/fr/20.webp)

Once you have selected an action, confirm your choice.

![CCQ](assets/fr/21.webp)

You can then view all configured Trick PINs in the dedicated menu.

![CCQ](assets/fr/22.webp)

By selecting an existing Trick PIN, you can check the associated action. You can also hide it with "*Hide Trick*", making it invisible in the Trick PIN menu. You can delete it by clicking on "*Delete Trick*", or change the PIN code while retaining the associated action with "*Change PIN*".

![CCQ](assets/fr/23.webp)

The "*Add If Wrong*" option, available in the "*Trick PIN*" menu, lets you configure a specific action that is automatically triggered after a certain number of incorrect attempts to enter the master PIN code. The number of attempts allowed can be set during configuration.

### Scramble Keys

The Scramble Keys option allows you to scramble the digits displayed on your keypad buttons when entering your PIN code. This feature protects the confidentiality of your PIN code, even in the event of surveillance by people or cameras.

To activate this option, access the menu `Settings > Login Settings > Scramble Keys`.

![CCQ](assets/fr/24.webp)

Select the "*Scramble Keys*" option.

![CCQ](assets/fr/25.webp)

From now on, when you unlock your COLDCARD Q, the keys on the keypad will be assigned new numbers randomly each time you use them.

![CCQ](assets/fr/26.webp)

### Login Countdown

This option enables you to impose a systematic countdown each time you attempt to unlock your COLDCARD. It can be integrated into your security strategy by delaying access to the device in the event of theft, or by imposing a delay before signing a transaction, for example to protect yourself in the event of a hold-up. However, this countdown applies to all your uses, including when you are legitimately using your COLDCARD, which also obliges you to be patient. Be careful not to confuse this option with the "*Just Countdown*" action, which is only activated when a specific Trick PIN is used.

To configure this option, access the menu `Settings > Login Settings > Login Countdown`.

![CCQ](assets/fr/27.webp)

Select the countdown time. For example, if you select 1 hour, you will have to wait 1 hour for each attempt to unlock the COLDCARD Q.

![CCQ](assets/fr/28.webp)

Each time you unlock, you will be prompted to enter your PIN code.

![CCQ](assets/fr/29.webp)

Then wait for the time set by the countdown.

![CCQ](assets/fr/30.webp)

At the end of the countdown, you'll need to enter your PIN again to access the device.

![CCQ](assets/fr/31.webp)

### Calculator Login

This option allows you to disguise your COLDCARD as a calculator when unlocking. To activate this feature, access the menu `Settings > Login Settings > Calculator Login`.

![CCQ](assets/fr/32.webp)

Activate the option by selecting it.

![CCQ](assets/fr/33.webp)

From now on, every time the device is switched on, a working calculator with basic commands will be displayed.

![CCQ](assets/fr/34.webp)

For example, you can calculate the SHA256 hash of "*Plan B Network*".

![CCQ](assets/fr/35.webp)

To unlock the COLDCARD from calculator mode, start by entering your PIN code prefix followed by a dash. For example, if your PIN code is `00-00` (this code is weak and only an example, so choose a strong PIN code), type `00-`. COLDCARD will then display your two anti-phishing words.

![CCQ](assets/fr/36.webp)

Then enter your full PIN code, separated by a space or a dash, for example: `00 00`.

![CCQ](assets/fr/37.webp)

The COLDCARD will then exit calculator mode and unlock normally.

## Cleanly destroying your COLDCARD

If you are planning to dispose of your COLDCARD Q, for example because you are now using another hardware wallet, it is important to destroy the device correctly. This ensures that no information relating to your wallet can be recovered by a third party.

There are three levels of information destruction, depending on your needs. Before you start, make sure that your wallet has been imported into another hardware wallet, that you have access to all your funds and, above all, that you have your mnemonic phrase and any passphrase, both of which are functional. Without a wallet backup, the destruction of your COLDCARD will result in the loss of your bitcoins.

The first level of destruction consists of deleting only the seed. This option deletes your mnemonic phrase from the COLDCARD's memory, while leaving the device functional. It's ideal if you want to use the COLDCARD Q again at a later date. To delete the seed from memory, access the `Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed` menu.

![CCQ](assets/fr/38.webp)

The second level of destruction consists of permanently disabling the COLDCARD's two secure chips via the software. This action renders the device completely unusable. You won't be able to resell it, reuse it or return it to Coinkite: it will be permanently destroyed. To proceed, follow the steps described in the previous section regarding the "*Brick Me*" PIN, then intentionally enter this PIN when unlocking the COLDCARD.

The third level involves the physical destruction of your COLDCARD Q's secure components. As before, this will render the device irrevocably unusable. To do this, use a drill to make a hole in the two chips on the top right-hand side of the device (once turned upside down), close to the "*SHOOT HERE*" inscription.

**Important precautions** :


- To avoid the risk of electric shock, remove the batteries from the device and unplug it from the mains before handling.
- Wait a few minutes after switching off the unit before starting drilling.
- Wear insulated gloves and safety goggles to ensure your safety.

![CCQ](assets/fr/39.webp)

Once the chips have been punched, do not attempt to reconnect the COLDCARD Q.

Congratulations, you're now up to speed on COLDCARD Q's advanced options!

If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Feel free to share this tutorial on your social networks. Thank you very much!

I also recommend this other tutorial, in which we discuss the use of a direct competitor to CCQ, Ledger Flex :

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a