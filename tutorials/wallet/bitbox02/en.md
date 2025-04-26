---
name: BitBox02

description: Set-up and use a BitBox02
---

![cover](assets/cover.webp)

The BitBox02 (https://bitbox.swiss/) is a Swiss-made physical wallet specifically designed for securing your Bitcoins. Some of its key features include easy backup and restoration using a microSD card, a minimalist and discreet design, and comprehensive support for Bitcoin.

![device](assets/1.webp)

It offers cutting-edge security engineered by experts, featuring a dual-chip design that includes a secure chip. Its source code has been fully audited by security researchers and is entirely open-source. The BitBox02 comes with a simple yet powerful BitBoxApp, which provides secure management of your Bitcoins. It supports full node for Bitcoin and ensures end-to-end encrypted communication between the app and the device. Manufactured in Switzerland, the BitBox02 has earned a positive reputation among its users.

![video](https://youtu.be/sB4b2PbYaj0)

Here are the wallet specifications:

- Connectivity: USB-C
- Compatibility: Windows 7 and later, macOS 10.13 and later, Linux, Android
- Input: Capacitive touch sensors
- Microcontroller: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; True random number generator
- Secure chip: ATECC608B; True random number generator (NIST SP 800-90A/B/C)
- Display: 128 x 64 px white OLED
- Material: Polycarbonate
- Size: 54.5 x 25.4 x 9.6 mm including USB-C plug
- Weight: Device 12g; with packaging and accessories 160g

Download data sheets on their website https://bitbox.swiss/bitbox02/

## How to use the BitBox02 Hardware Wallet

### Setting up the BitBox02

The BitBox02 has a USB-C connection attached to the shell. If your computer uses the regular USB port, you’ll have to use the adaptor that comes with the device.

Connect it to your computer and the device will power on (don’t do it yet).

It has sensors above and below, and it will prompt you to touch the top or bottom to orientate the screen the way you’d like.

![image](assets/2.webp)

### Download the BitBox02 App

Visit https://shiftcrypto.ch/ and click on the “App” link at the top to get to the download page:

![image](assets/3.webp)

Click the blue Download button:

![image](assets/4.webp)

To verify the download (it adds complexity, but recommended, particularly if you store a lot of bitcoin), see Appendix A.

After the download, you can unzip the file. On a mac, just double-click the downloaded file, and a BitBox App icon will appear in your downloads directory. You can drag it to your desktop (or anywhere) for easy access.

Double click the App to run it (it doesn’t get “installed”).

On the Mac, your computer nanny will give you a warning. Just ignore it and click “open”:

![image](assets/5.webp)

You’ll then see this:

![image](assets/6.webp)

Go ahead and connect the device to the computer.

It will show you a pairing code. Check they match, and then touch the sensor to select the checkmark. Then back to the screen, the continue button will become available for you.

![image](assets/7.webp)

You’ll then have the option to create a new seed, or restore a seed. I’ll demonstrate creating a new seed (It’s important to also restore the seed you created to test the quality of your backup, before you load any bitcoin on the wallet).

![image](assets/8.webp)

The device came with a microSD card. Go ahead and insert it if you have’t.

![image](assets/9.webp)

Name your device and click continue, then confirm on the device.

![image](assets/10.webp)

You’ll then be asked to set a password for the device. This is not part of your seed. It is not a passphrase either (that’s part of your seed). It is simply a password to lock the device. When you poweron the device, you’l’l be asked to enter this password each time. You have 10 consecutive failures allowed before the device will wipe itself of all memory, so be careful. The animation on the screen will teach you how to use the devices controls to set the password.

![image](assets/11.webp)

Read the next screen, and check each box, then continue.

![image](assets/12.webp)
![image](assets/13.webp)
![image](assets/14.webp)

And this is how the wallet looks once it’s ready to go.

![image](assets/15.webp)

### NOT SO FAST!!

It’s quite odd, but the BitBox02 is telling us we’re ready to use the device, but it hasn’t promputed us to write down the seed words! The ONLY backup we have is the file saved to the microSD card. This is inadequate. These storage devices do not last forever (due to “bit rot”). We need a paper backup, and duplicates, kept in a safes (as explained in the general how-to-use-hardware-wallets guide)

To get our seed phrase and write it down, go to the “manage device” tab on the left, and then click “show recover words”

![image](assets/16.webp)

You can then go through the confirmation, and the device will present you the words. Write them down neatly, and never let anyone see the words.

![image](assets/17.webp)

After that, you can click on the Bitcoin tab on the left to get your receiving addresses.

![image](assets/18.webp)

It shows one at a time, but at least it lets you choose which address to use from the first 20:

![image](assets/19.webp)

Clicking the blue button will show the full address, and you’ll be prompted to check the address matches the display on the screen. This is good practice to confirm that no malware on your computer is tricking you to send bitcoin to an attacker’s address.

![image](assets/20.webp)

To send bitcoin to this wallet, you can copy the address and paste it into the withdrawal page of the exchange where your coins are. I recommend you send a small test amount first, then practice spending it either back to the exchange or to the second address in your wallet.

For larger amounts, I suggest you create a passphrase (see below). The original wallet (no passphrase) can be used as your decoy wallet (it will need to have a reasonable amount in there for it to be a believable decoy).

### Connect to a node

The BitBox02 will automatically connect to a node. Let’s see where it’s connecting to. Click on the settings tab on the left, and then “connect your own full node”.

![image](assets/21.webp)

And here we can see it’s connecting to shiftcrypto’s node. Not great. We have betrayed all our bitcoin addresses to them, and our IP address (not the seed of course; they can see our addresses/balances, but can’t spend them). We can enter our own node details in this page (beyond the scope of this particular guide), or we can use better software like Sparrow Bitcoin Wallet, Electrum Desktop Wallet, or Specter Desktop. I’ll demonstrate Sparrow Bitcoin Wallet later in the guide.

![image](assets/22.webp)

Add a passphrase

Now that we have set up the device with the BitBox02 App (and revealed our addresses, unavoidable with this particular hardware wallet), we can add a passphrase to our seed phrase. This will allow us to create a new wallet using the same seed, and ShiftCrypto will never see our new addresses. We’ll be connecting this wallet to our own software only.

### Enable Passphrase

Go ahead now and “enable” the passphrase feature (but we’re not setting a passphrase yet). Got o the “manage device” tab, and click on “enable passphrase” (red circle below).

![image](assets/23.webp)

Read through the steps…

![image](assets/24.webp)
![image](assets/25.webp)
![image](assets/26.webp)

Now disconnect the device, and shut down the BitBox02 App

END of the bitbox02 section by Parman.

Your divice is now fully operation to be used on any desktop solution such as specter, sparrow and using the bitbox interface.
