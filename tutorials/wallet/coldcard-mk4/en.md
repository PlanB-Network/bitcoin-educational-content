---
name: COLDCARD Mk4
description: A guide to set up and use a COLDCARD Mk4 with Sparrow Wallet
---

![cover-mk4](assets/cover.webp)

**Hardware wallets** are physical devices made just for storing Bitcoin's private key securely. They store the private keys offline, which means hackers cannot reach them through the internet. Whereas **software wallets** are mainly used for everyday transactions, **hardware wallets** are often used to store larger amounts of bitcoins securely for a long time. When making a Bitcoin transaction using **hardware wallets**, the wallet can sign the transactions inside the device, so the private key is never exposed to internet-connected environments.

In this tutorial, we will explore one of the most popular hardware wallets produced by Coinkite, the Coldcard Mk4. We will take a look on how to set up and use this hardware wallet to perform Bitcoin transactions.

## Coldcard Mk4 Overview

Coldcard Mk4 is a Bitcoin-only hardware wallet manufactured by Coinkite. This device is equipped with a screen, a numeric keypad and a protective sliding cover. In addtion, the device offers several ways to connect and interact, including USB-C, air-gapped operation using a MicroSD card, NFC, and a virtual disk mode. The Mk4 also includes advanced security features such as the BIP39 passphrase and trick PINs, giving users greater control and protection over their Bitcoin.

## Initial Setup: PIN and Anti-Phishing Words

To get started, the Coldcard Mk4 can be purchased directly from [Coinkite's website](https://store.coinkite.com/store). Buyers can also choose to pay using fiat currency or Bitcoin. In addition, you will also need a MicroSD card (4 GB is sufficient) and a power source that can be connected via USB-C cable (the Coldcard Mk4 only has a USB-C power input port). Note that since the Mk4 does not have a built-in battery, it must be connected to the power source at all times while being used.

You will receive your Mk4 in a tamper-evident bag. Please ensure that the bag has not been compromised. If you spot something that may be a problem such as damage or tear on the bag, you can inform Coinkite by sending an email to support@coinkite.com. In addition, you can also find a 12-digit number on the tamper-evident bag, which we will refer to as the Mk4's bag number. This bag number will be used later to verify that the device has not been tampered with during shipping and that it comes directly from Coinkite. The bag number is stored securely in the Coldcard’s secure element using OTP (One-Time-Programmable) flash memory, which means it cannot be changed once programmed. When you turn on the device for the first time, the number displayed on the screen must match the one on the bag. This ensures that the Mk4 you received is the original device from the factory and has not been replaced or modified. While this verification only confirms the integrity of the device at the time of first power-on, the secure element continues to protect your private keys, PIN, and passphrase, making it extremely difficult for any tampering to compromise your Bitcoin. In addition, good practices, such as securing your wallet-related data properly, will be beneficial in the overall security of the Coldcard itself. For further information, you can refer to this [article](https://blog.coinkite.com/understanding-mk4-security-model/) that elaborate Coldcard's security model.

The keypad consists of 10 numeric buttons, an OK (`✓`) button, and a cancel (`✕`) button. Some numeric buttons can also be used for navigation: `5` to navigate up (`^`), `7` to navigate left (`<`), `8` to navigate down `˅`, and `9` to navigate right (`>`).

![01](assets/en/01.webp)

If there are no problems with the packaging, you may open the bag. The Mk4 will come with a wallet backup card that can be used to store information regarding the device's PIN, anti-phishing words, and seedphrase. Follow the following steps for the initialization: 

1. Prepare a piece of paper and a pen.
2. Connect the Mk4 to a power source (USB-C cable) and insert the MicroSD card. 
3. Once the device is powered up for the first time, the screen will display a message regarding Coldcard's Terms of Sale and Use. Navigate down, then press `✓` to continue.
4. Next, a 12-digit number will be displayed on the screen. Check this number against the one on the tamper-evident bag and the additional copy of the bag number that was included in the tamper-evident bag to ensure the device has not been tampered with. If the numbers do not match, contact Coinkite support immediately before proceeding. Otherwise, press `✓` to continue.

![02](assets/en/02.webp)

5. Select `Choose PIN Code`.
6. Navigate down as you read the instructions to proceed to the next step.

![03](assets/en/03.webp)

7. On the Mk4, create and enter the PIN prefix (must be 2 to 6 characters long) and write it down, then press `✓` to continue.
8. Write down the two words displayed at the screen. These are the anti-phishing words. Press `✓` to continue.

![04](assets/en/04.webp)

9. Create and enter the PIN suffix (or rest of PIN, must be 2 to 6 characters long) and write it down. Press `✓` to continue.
10. Reenter your PIN prefix. Press `✓` to continue.

![05](assets/en/05.webp)

11. Check whether the anti-phishing words are the same with the one you wrote on step 8. Press `✓` to continue.
12. Reenter your PIN suffix (or rest of PIN). Press `✓` to continue.

![06](assets/en/06.webp)

13. Your Mk4's PIN and anti-phishing words are now successfully created and stored by the device.

![07](assets/en/07.webp)

Note that Mk4 will always ask you to input your PIN each time you switch your device on. Without this PIN, you are not able to access your Coldcard Mk4. So make sure that you create sufficient backup for the PIN and anti-phishing words.

## Setting up your Wallet

The next step is to set up your wallet. There are three ways for you to do this:
- Creating a new wallet (standard)
- Creating a new wallet with dice rolls
- Importing a wallet

### Creating a new wallet (standard)

To create a new wallet, simply do the following steps.

1. Select `New Wallet` (or `New Seed Words`) > Select `12 Word` or `24 Word (default)` depending on your preference.

![08](assets/en/08.webp)

2. The device will generate 12 or 24 words as your seedphrase based on your choice. Navigate down as you carefully write down each word in the correct order. Then, press `✓` to continue. 

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. The device will ask you to verify your seedphrase by asking the in a random order (for example, `Word 1 is?`, then `Word 5 is?`, then `Word 12 is?`, and so on) and there will be three word choices for each question. Refer to the note from Step 2 and choose the words correctly (by pressing `1`, `2` or `3`, whichever corresponds to the correct word) to complete the wallet creation.

![09](assets/en/09.webp)

4. Mk4 will then ask whether you want to Enable NFC/Tap or not. For now, select `✕` for this option. This can be changed in the settings in the future.
5. Finally, Mk4 will also if you want to disable the USB Port (which can be used for non-airgapped data transfer). For now, select `✓` for this option. This can be changed in the settings in the future.
6. The screen will now display the main menu with `Ready to Sign` at the top. This marks the completion of the wallet creation process.

![10](assets/en/10.webp)

### Creating a new wallet with dice roll

Alternatively, you can also choose to generate the new seedphrase with entropy. Do it if you do not trust Mk4's freshly generated seedphrase.

The procedure on the Coldcard Mk4 is the following:

1. Select `New Wallet` (or `New Seed Words`) > Select `12 Word Dice Roll` or `24 Word Dice Roll` depending on your preference.
2. You will be asked to enter the results of your dice rolls. Each dice roll adds randomness to the wallet creation process, ensuring that your seedphrase is generated in a fully secure and unpredictable way. The minimum number of rolls are 50 for 12-word seedphrase and 99 for 24-word seedphrase. Press `✓` after you have input at least 99 dice roll values.

![11](assets/en/11.webp)

3. The device will generate 12 or 24 words as your seedphrase based on your choice. Navigate down as you carefully write down each word in the correct order. Then, press `✓` to continue. 
4. The device will ask you to verify your seedphrase by asking the in a random order (for example, `Word 1 is?`, then `Word 5 is?`, then `Word 12 is?`, and so on) and there will be three word choices for each question. Refer to the note from Step 3 and choose the words correctly (by pressing `1`, `2` or `3`, whichever corresponds to the correct word) to complete the wallet creation.

![12](assets/en/12.webp)

5. Mk4 will then ask whether you want to Enable NFC/Tap or not. For now, select `✕` for this option. This can be changed in the settings in the future.
6. Finally, Mk4 will also if you want to disable the USB Port (which can be used for non-airgapped data transfer). For now, select `✓` for this option. This can be changed in the settings in the future.
7. The screen will now display the main menu with `Ready to Sign` at the top. This marks the completion of the wallet creation process.

![13](assets/en/13.webp)

### Importing a wallet

The final option is for you to import a wallet. You can do this if you want to recover a wallet from a seedphrase that you already have. You can follow these steps:

1. Select `Import Existing`.
2. Select `24 Words`, `18 Words` or `12 Words`, depending on your seedphrase's word count.

![14](assets/en/14.webp)

3. Coldcard Mk4 will then ask you what each word is in consecutive order. For each word, navigate down or up until you find the write prefix for each word. The device will narrow down the possibilities until you can find the correct word. Do this for the rest of the other words.
4. For the final word, Coldcard Mk4 will display only a limited amount of possible words. If there are no matches, you may have input the words incorrectly. Otherwise, select the word that matches the one on your seedphrase.

![15](assets/en/15.webp)

5. Mk4 will then ask whether you want to Enable NFC/Tap or not. For now, select `✕` for this option. This can be changed in the settings in the future.
6. Finally, Mk4 will also if you want to disable the USB Port (which can be used for non-airgapped data transfer). For now, select `✓` for this option. This can be changed in the settings in the future.
7. The screen will now display the main menu with `Ready to Sign` at the top. This marks the completion of the wallet creation process.

![16](assets/en/16.webp)

Do note that the seedphrase is the only access to recover your wallet. Create a backup of your seedphrase and store it in a secure place. **Not your keys, not your coins**, whoever has your seedphrase has access to your bitcoins!

## Setting up your passphrase

One of the best practices in Bitcoin is to use a passphrase. The passphrase acts as the 13th or 25th word in addition to the seedphrase. What makes it different is that you are able to choose whatever phrase you want, while the seedphrase is selected from a predetermined list of 2048 words. By default, after setting up your wallet, you will start with a wallet with a blank passphrase. To set up a non-blank passphrase, simply do the following steps:

1. Go to `Passphrase`.
2. Navigate down to read the description about passphrase, then press `✓` to proceed.
3. Select `Edit Phrase`.

![17](assets/en/17.webp)

4. Input your passphrase:
   - Press `1` (letters), `2` (numbers) or `3` (symbols) to select the character type.
   - Press `4` to swap between lowercase and uppercase letters (can only be used when inputting letters).
   - Navigate using `^` or `˅` to select the character for your passphrase.
   - Navigate using `<` or `>` to move between characters. You can also use `>` to add spaces.
   - Press `✕` to delete the characters.
   - Press `✓` when you have finished editing the passphrase.
5. Additionally, the other options have the following functionalities:
   - The `Add Word` or `Add Numbers` can be used to append letters/numbers to the passphrase you are currently editing.
   - Press `Clear ALL` to reset the passphrase you are currently editing.
   - Press `CANCEL` to go back to the main menu.
6. Write down your passphrase as a backup.
7. Press `APPLY` to access the wallet with the passphrase you have just set.
8. Mk4 will then display a 8-character long master key fingerprint. This can be regarded as the "ID" of the wallet. Write down this fingerprint and press `✓` to proceed.

![18](assets/en/18.webp)

9. Now, the wallet will display the main menu of the wallet with the passphrase that you have input.
10. It's important to note that a wallet will not tell you that you have input the incorrect passphrase, because each passphrase corresponds to each own wallet with a unique identity (master key fingerprint). Therefore, it’s a good practice to re-enter the same passphrase and check whether it produces the same wallet fingerprint, ensuring that you’ve entered it correctly. To do that, perform Steps 11 to 14.
11. On the main menu, select `Restore Master`, then press `✓`. You are now back in the main menu of the wallet with the blank passphrase.

![19](assets/en/19.webp)

12. Go to `Passphrase` again, then press `✓` to proceed.
13. Reinput the passphrase that you have written down on Step 6, then press `APPLY`.
14. Check the 8-character long master key fingerprint against the one you have written down on Step 8. If both fingerprints does not match, you may have typed mismatched characters. You can select a new passphrase instead and repeat the process from Step 1. But if both fingerprints match, it means that you have input the passphrase correctly.
15. The wallet with your chosen passphrase is ready to be used.

## Exporting the Wallet to Sparrow

Like other hardware wallets, the Coldcard Mk4 cannot be used on its own. It needs to be connected with a software wallet that acts as an interface. The software wallet allows you to view your balance, create transactions, and manage addresses, while the Coldcard securely signs those transactions without ever exposing your private keys. 

In this tutorial, we will use Sparrow Wallet as the interface. The procedure to export the wallet is as follows:

1. Ensure that you have a MicroSD card inserted into the Mk4.
2. Perform the "Setting up your passphrase" steps on the wallet with the passphrase that you want to export. If you want to export the wallet with the blank passphrase, you can skip this step.
3. Go to `Advanced/Tools` > Choose `Export Wallet` > Select `Generic JSON` > Scroll down as you read the instructions, then press `✓`.

![20](assets/en/20.webp)

4. Mk4 now has created a file with a `.json` format in the MicroSD card.

![21](assets/en/21.webp)

5. Remove the MicroSD card from the Coldcard and insert it into the device where Sparrow Wallet is installed.
6. Open Sparrow Wallet.
7. Click on `File`

![22](assets/en/22.webp)

Next, click on `New Wallet`

![23](assets/en/23.webp)

Then, input the name for the wallet

![24](assets/en/24.webp)

After that, click on `Create Wallet`

![25](assets/en/25.webp)

8. Select the `Script Type`.

![26](assets/en/26.webp)

9. On the Keystore section, select `Airgapped Hardware Wallet`.

![27](assets/en/27.webp)

10. Look for Coldcard and click `Import File...`.

![28](assets/en/28.webp)

11. Select the file that was created in Step 4 (the one with the `.json` format).

![29](assets/en/29.webp)

12. On the Mk4, return to the main menu and navigate to `Advanced/Tools` > `View Identity`. Ensure that the fingerprint displayed on the Mk4's screen matches the one on Sparrow Wallet (the Master fingerprint on the Keystore section)
13. Click the `Apply` button on the bottom right corner.

![30](assets/en/30.webp)

14. Optionally, you can also add a password for the exported wallet. This password is required each time you open the Sparrow Wallet application to access the wallet. If you forget the password in the future, you can simply repeat Steps 1-13 and choose a new password.

![31](assets/en/31.webp)

15. The wallet is now successfully exported and ready to be used.

![32](assets/en/32.webp)

## Receiving bitcoin

Next, we’ll learn how to receive Bitcoin using the Mk4. This process is quite simple because you don’t need to use the Mk4 device itself. As long as you’ve already exported your wallet to Sparrow, you can receive Bitcoin directly through Sparrow Wallet. Follow these steps to receive bitcoins with Mk4:

1. Open Sparrow Wallet.
2. Select `Open Wallet` > Choose the wallet file to which you want to receive bitcoin > Enter the password associated with that wallet.

![33](assets/en/33.webp)

3. On Sparrow's interface, click on the `Receive` tab on the left side of the interface.

![34](assets/en/34.webp)

4. An address along with a QR code will appear at the top. You can copy and paste the address or scan the QR code using the wallet you’ll use to send bitcoin to Sparrow Wallet. Optionally, you can type in a label for the bitcoin you receive.

![35](assets/en/35.webp)

5. After you send the bitcoins, on Sparrow's interface, click on the `Transactions` tab on the left side of the interface. You’ll see a new entry at the top of the transaction history, which corresponds to the transaction you just made.

![36](assets/en/36.webp)

6. You can also navigate on the `UTXOs` tab on the left side of the interface to see the bitcoin you just received.

![37](assets/en/37.webp)

## Sending bitcoin

Unlike receiving bitcoins, spending the bitcoins associated with your Coldcard requires you to use the Coldcard for signing the transactions. The procedure of sending bitcoins with Mk4 is as follows:

1. Insert the MicroSD card into the device where your Sparrow Wallet is installed.
2. Open Sparrow Wallet.
3. Select `Open Wallet` > Choose the wallet file you want to use to send bitcoins with > Enter the password associated with that wallet.

![38](assets/en/38.webp)

4. On Sparrow's interface, click on the `Send` tab on the left side of the interface.

![39](assets/en/39.webp)

5. On the `Pay to` tab, enter the address you want to send the bitcoins to.
6. Add a label for the transaction.
7. Enter the amount of bitcoins you want to send.
8. Enter the fee by toggling the `Range` or directly input a number into the `Fee` part.

![40](assets/en/40.webp)

9. On the bottom right corner, click `Create Transaction`.

![41](assets/en/41.webp)

10. You will be brought into a new transaction tab whose name is the label you input on Step 6. Click `Finalize Transaction for Signing`.

![42](assets/en/42.webp)

11. Click `Save Transaction` and save the transaction in the MicroSD card. Rename the file if necessary. This step will save the transaction as a PSBT file.

![43](assets/en/43.webp)

12. Remove the MicroSD card and insert it into your Coldcard Mk4.
13. Turn on your Mk4 by connecting it to a power source.
14. Input your PIN.
15. Go to `Passphrase` and input the passphrase of the wallet you want to use to send the bitcoins with. If you want to use the wallet with the blank passphrase, skip this step.
16. Ensure the master key fingerprint is the same with the one on your Sparrow Wallet. You can check this on Sparrow Wallet's `Settings` tab on the left side of the interface. Then, press `✓` on your Mk4 to proceed. This will take you to the main menu.
17. On Mk4's main menu, select `Ready to Sign`. The screen will display an `OKAY TO SEND?` message. Ensure the amount of the bitcoins you want to send and the receiving address are all correct. Press `✓` to confirm or `✕` to cancel.
18. If there are multiple PSBT files to choose from, Mk4 will display `Choose PSBT file to be signed` message. Press `✓` to continue. Then, select the PSBT file you want to sign by navigating down or up. Perform Step 17 on that transaction.

![44](assets/en/44.webp)

19. Mk4 will now display the `PSBT Signed` message along with the name of the file of the signed PSBT. Press `✓` to continue.
20. Remove the MicroSD card from the Coldcard and insert it into the device where Sparrow Wallet is installed.
21. On Sparrow Wallet, click `Load Transaction`.

![45](assets/en/45.webp)

22. Select the file with the same name as the one created on Step 19.

![46](assets/en/46.webp)

23. Click `Broadcast Transaction`.

![47](assets/en/47.webp)

24. Your transaction has been broadcast and it is being processed. You can go to the `Transactions` tab to view the confirmation status of your transaction.

![48](assets/en/48.webp)

## Firmware Upgrade

### Checking your Firmware Version

Coldcard Mk4's firmware can always be upgraded to a newer version. To check whether your Mk4 has been upgraded to the latest version or not, perform the following steps:
1. Turn on your Mk4 by connecting it to a power source.
2. Input your PIN.
3. Go to `Advanced/Tools` > Select `Upgrade Firmware` > Select `Show Version`. 

![49](assets/en/49.webp)

Check the version displayed on Mk4's screen against the one on [Coinkite's website](https://coldcard.com/downloads). If the version is different, you are able to upgrade the firmware into the newer version.

![50](assets/en/50.webp)

### Upgrading your Firmware

If you want to upgrade the firmware to the latest version, do the following steps:

1. Insert the MicroSD card into your laptop/PC.
2. Go to [Coinkite's website](https://coldcard.com/downloads) and download the latest firmware to your MicroSD card (The red button right of the Mk4 image with the version number on it).

![51](assets/en/51.webp)

You can also download other versions by clicking on `All Files on Mk4` and exploring the version you want to download. The downloaded file will be in `.dfu` format.

![52](assets/en/52.webp)

3. Remove the MicroSD card and insert it into your Mk4.
4. Turn on your Mk4 by connecting it to a power source.
5. Input your PIN.
6. Go to `Advanced/Tools` > Select `Upgrade Firmware` > Select `From MicroSD` > Scroll down as you read the instructions then press `✓`.

![53](assets/en/53.webp)

7. Select the `.dfu` file that you downloaded in Step 2.
8. Coldcard Mk4 will display an `Install this new firmware?` message. Scroll down as you read the instructions then press `✓`.

![54](assets/en/54.webp)

9. Wait for the Mk4 to finish installing the new firmware. Do not disconnect the power source during the installation.
10. Upon completion, Mk4 will restart itself. You may enter your PIN and perform the "Checking your Firmware Version" steps to check whether the firmware has been upgraded or not.

## Advanced Features

### Change your PIN

If you want to change your login PIN, simply perform the following steps:

1. Prepare a pen and a piece of paper.
2. Turn on your Mk4 by connecting it to a power source.
3. Input your PIN.
4. Go to `Settings` > Select `Login Settings` > Select `Change Main PIN`
5. Navigate down as you read the message, then press `✓` to proceed.

![55](assets/en/55.webp)

6. Input your old PIN.
7. Input your new PIN prefix (must be 2 to 6 characters long) and write it down.
8. Mk4 will now display two new anti-phishing words, write them down, then press `✓` to proceed.
9. Input your new PIN suffix (or rest of PIN, must be 2 to 6 characters long) and write it down.

![56](assets/en/56.webp)

10. Reenter your new PIN prefix.
11. Check whether the anti-phishing words match the one you wrote in Step 8.
12. Reenter your new PIN suffix (or rest of PIN).

![57](assets/en/57.webp)

13. Your PIN has successfully been changed.

### Trick PINs - Add New Trick

A Trick PIN is an alternative PIN code distinct from the one you use to set up your Coldcard Mk4 for the very first time. When you turn on your Mk4, you can input the trick PIN(s) instead of your Main PIN to trigger certain actions. To configure the trick PIN in Mk4, you can do the following steps:

1. Prepare a pen and a piece of paper.
2. Turn on your Mk4 by connecting it to a power source.
3. Input your PIN.
4. Go to `Settings` > Select `Login Settings` > Select `Trick PINs` > Select `Add New Trick`.

![58](assets/en/58.webp)

5. Input your trick PIN prefix (must be 2 to 6 characters long) and write it down.
6. Mk4 will now display two new anti-phishing words, write them down, then press `✓` to proceed.
7. Input your trick PIN suffix (or rest of PIN, must be 2 to 6 characters long) and write it down.

![59](assets/en/59.webp)

8. Navigate down or up to select the action you want to pair with the trick PIN you just created. The list of actions are:
    - `Brick Self`, when selected, your Mk4's chips will be destroyed after the PIN is entered, making your Mk4 to be unusable permanently.
    - `Wipe Seed`, you can choose between the following actions:
      - `Wipe & Reboot`: The seed is wiped and Coldcard will reboot after the PIN is entered.
      - `Silent Wipe`: The seed is wiped silently, however Coldcard will act as if the PIN was entered incorrectly.
      - `Wipe -> Wallet`: The seed is wiped silently, and the Coldcard will take you into a duress wallet.
    - `Duress Wallet`, when selected, your Mk4 will lead to a duress wallet after the PIN is entered.
    - `Login Countdown`, you can choose between the folowing actions:
      - `Wipe & Countdown`: The seed is immediately wiped, then Mk4 will begin displaying a countdown.
      - `Countdown & Brick`: The countdown begins and Mk4 will brick itself after the time runs out.
      - `Just Countdown`: Mk4 will begin the countdown and will reboot itself after the time runs out.
    - `Look Blank`, when selected, after the trick PIN is entered, the Coldcard act as if the seedphrase is wiped, but it is in fact still in memory.
    - `Just Reboot`, when selected, Coldcard will reboot itself after the trick PIN is entered.
    - `Delta Mode`, This advanced feature is meant for experienced users and is designed to protect against serious threats, such as coercion by someone with insider knowledge. When Delta Mode is activated, the COLDCARD appears to open the real wallet, allowing the attacker to browse and confirm that it looks genuine. However, it secretly blocks all transaction signing, so no bitcoin can be sent. It also disables access to the seed phrase, and any attempt to view it will erase it completely. To make the fake wallet look more convincing, the Trick PIN used for Delta Mode must start with the same numbers as the real PIN (so it shows the same anti-phishing words) but end differently.
    - `Policy Unlock`, when selected, Single Signer Spending Policy (SSSP) will be disable after the trick PIN is entered.
    - `Policy Unlock & Wipe`, when selected, it pretends to disable SSSP but it will wipe the seedphrase in the process.
9. After you have selected the action you want to pair with the trick PIN, confirm your choice by pressing `✓`. Your trick PIN is successfully configured.
10. In the `Settings` > `Login Settings` > `Trick PINs`, you can see the list of trick PINs you have created and the actions paired with it. You can choose to reconfigure the trick PINs and the actions paired with it. You can also hide or delete it by selecting the PIN then select `Hide Trick` or `Delete Trick`. 

![60](assets/en/60.webp)

### Trick PINs - Add If Wrong

Alternatively, you can add a `Add If Wrong` action that will be triggered after the incorrect PIN is entered certain amount of times. You can configure this by performing the following steps:

1. Turn on your Mk4 by connecting it to a power source.
2. Input your PIN.
3. Go to `Settings` > Select `Login Settings` > Select `Trick PINs` > Select `Add If Wrong`.

![61](assets/en/61.webp)

4. Mk4 will display a message regarding this setting. Navigate down as you read through the explanation, then press `✓` to proceed.
5. Input the number of wrong attempts required to trigger the action. Note: The maximum attempt count is `12`. This is because Mk4 is designed such that when the incorrect PIN is entered `13` times, the device will brick itself, making it unusable permanently. After you input the number, press `✓` to continue.
6. Navigate up or down to select the action. The actions available are as follows:
   - `Wipe, Stop`: The seedphrase is erased and the device shows “Seed is wiped, Stop.”
   - `Wipe & Reboot`: The seedphrase is erased and the device restarts without any message.
   - `Silent Wipe`: The seedphrase is erased quietly and the device behaves like a wrong-PIN attempt (no obvious wipe message).
   - `Brick Self`: The device is permanently disabled and only shows “Bricked.”
   - `Last Chance`: The seedphrase is erased but you get one final PIN attempt; enter the wrong PIN again and the device will be bricked.
   - `Just Reboot`: The device simply restarts and nothing else changes.
   Choose the action you want to apply and press `✓` to proceed

![62](assets/en/62.webp)

7. You will be brought back to the `Settings > Login Settings > Trick PINs` directory. Under the `Trick PINs:`, you will find the list of trick pins along with `WRONG PIN` action. You can also hide or delete it by selecting the PIN then select `Hide Trick` or `Delete Trick`. 

![63](assets/en/63.webp)


## Conclusion

This tutorial has provided the guide on how to set up Mk4, how to conduct Bitcoin transactions with Mk4 and how to use some advanced features of Mk4. It offers secure and flexible ways to store and manage your bitcoins. Its design ensures that private keys never leave the device, while features like passphrases, trick PINs, and air-gapped transactions give users full control over their security setup. It can be paired with Sparrow Wallet for a user-friendly experience to creating, signing, and managing Bitcoin transactions without compromising privacy or security. 

If you wish to explore other functionalities, you can check the documentation on Coinkite's website [here](https://coldcard.com/docs/). I hope you find this tutorial beneficial when you are using your Coldcard Mk4. Thank you and see you next time!
