---
name: Specter DIY
description: Setup guide for Specter DIY
---

![cover](assets/cover.webp)

## Specter-DIY

> Cypherpunks write code. We know that someone has to write software to defend privacy, and since we can't get privacy unless we all do, we're going to write it.

*A Cypherpunk's Manifesto - Eric Hughes - 9 March 1993*

The idea of the project is to build a hardware wallet from off-the-shelf components.
Even though we have an extension board that puts everything in a nice form-factor and helps you to avoid any soldering, we will continue supporting and maintaining compatibility with standard components.

![image](assets/fr/01.webp)

We also want to keep the project flexible such that it can work on any other set of components with minimal changes. Maybe you want to make a hardware wallet on a different architecture (RISC-V?), with an audio modem as a communication channel - you should be able to do it. It should be easy to add or change functionality of Specter and we try to abstract logical modules as much as we can.

QR codes are a default way for Specter to communicate with the host. QR codes are pretty convenient and allow the user to be in control of the data transmission - every QR code has a very limited capacity and communication happens unidirectionally. And it's airgapped - you don't need to connect the wallet to the computer at any time.

For secret storage we support agnostic mode (wallet forgets all secrets when turned off), reckless mode (stores secrets in flash of the application microcontroller) and secure element integration is coming soon.

Our main focus is multisignature setup with other hardware wallets, but wallet can also work as a single signer. We try to make it compatible with Bitcoin Core where we can - PSBT for unsigned transactions, wallet descriptors for importing/exporting multisig wallets. To communicate with Bitcoin Core easier we are also working on [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - a small python flask server talking to your Bitcoin Core node.

Most of the firmware is written in MicroPython which makes the code easy to audit and change. We use [secp256k1](https://github.com/bitcoin-core/secp256k1) library from Bitcoin Core for elliptic curve calculations and [LittlevGL](https://lvgl.io/) library for GUI.

## Disclaimer

The project has significantly matured, to the extent that the security level of Specter-DIY is now comparable to commercial hardware wallets on the market. We implemented a secure bootloader that verifies firmware upgrades, so you can be sure that only signed firmware can be uploaded to the device after initial setup. However, unlike with commercial signing devices the bootloader has to be installed manually by the user and is not set in the factory of the device vendor. Thus, pay extra attention during the initial firmware installation and make sure you verified PGP signatures and flash the firmware from a secure computer.

If something doesn't work open an issue here or ask a question in our [Telegram group](https://t.me/+VEinVSYkW5TUl5Ai).

## Shopping list for Specter-DIY

Here we describe what to buy, and in assembly next part we explain how to put it together and a few notes about the board - power jumpers, USB ports etc.

### Discovery board

Main part of the device is the developer board:

- STM32F469I-DISCO developer board (i.e. from [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) or [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- **Mini**USB cable
- Standard MicroUSB cable to communicate over USB

Optional but recommended:
- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) with long pin headers like [these](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) or [these](https://www.amazon.com/gp/product/B015KA0RRU/) to connect the scanner to the board (4 pin headers needed).

We are currently working on an extension board that includes a smartcard slot, QR code scanner, battery and a 3d printed case, but it doesn't include the main part — discovery board that you need to order separately. This way supply chain attack is still not an issue as the security-critical components are bought from random electronic store.

You can start using Specter even without any extra components, but you will be able to communicate with it over USB or the built-in SD card slot. Using Specter over USB means it is not airgapped so you lose an important security property.

### QR scanner

For QR code scanner you have several options.

**Option 1. Recommended.** Resonably good scanner from Waveshare (40$)

[Waveshare scanner](https://www.waveshare.com/barcode-scanner-module.htm) - you will need to find a way how to mount it nicely, maybe use some kind of Arduino Prototype shield and some ducktape.

No soldering required, but if you have soldering skills you can make the wallet way nicer ;)

**Option 2.** Very nice scanner from Mikroe but pretty expensive (150$):

[Barcode Click](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)

**Option 3.** Any other QR scanner

You can find some cheap scanners in China. Their quality is often not that great, but you can take a chance. Maybe even ESPcamera would do the job. You only need to connect power, UART (pins D0 and D1), and trigger to D5.

**Option 4.** No scanner. 

Then you can only use Specter with USB / SD Card.

Unless you build your own communication module that uses something else instead of QR codes - audiomodem, bluetooth or whatever else. As soon as it can be triggered and send the data over serial you can do whatever you want.

### Optional components

If you add a tiny powerbank or a battery & power charger/booster, your wallet becomes completely self-contained ;)


## Assembly of Specter-DIY


![video](https://youtu.be/1H7FqG_FmCw)

### Connecting Waveshare Barcode scanner

The wallet firmware will configure the scanner for you on the first run, so no manual preconfiguration is required.

Here is how you connect the scanner to the board:

![image](assets/fr/02.webp)

For convenience you can buy an Arduino Protype shield and solder & mount everything on it (i.e. [this one](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))

### Power management

On the top side of the board there is a jumper that defines where it will take power. You can change position of the jumper and select power source to be one of the USB ports or VIN pin and connect external battery there (should be 5V).

### Enclosure for DIY

Check out the [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures) folder.

### Be creative!

Assemble your own Specter-DIY and send us the pictures (make a pull request or reach out to us).

Check out the [Gallery](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) with Specters assembled by the community!



## Installing the compiled code

With the secure bootloader initial installation of the firmware is slightly different. Upgrades are easier and don't require to connect hardware wallet to the computer.

![video](https://youtu.be/eF4cgK_L6T4)

### Flashing initial firmware

**Note** If you don't want to use binaries from the releases check out the [bootloader documentation](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) that explains how to compile and configure it to use your public keys instead of ours.

- If you are upgrading from versions below `1.4.0` or uploading the firmware for the first time, use the `initial_firmware_<version>.bin` from the [releases](https://github.com/cryptoadvance/specter-diy/releases) page.
	- Verify the signature of the `sha256.signed.txt` file against [Stepan's PGP key](https://stepansnigirev.com/ss-specter-release.asc)
	- Verify the hash of the `initial_firmware_<version>.bin` against the hash stored in the `sha256.signed.txt`
- If you are upgrading from an empty bootloader or you see the bootloader error message that firmware is not valid, check out the next section - Flashing signed Specter firmware.
- Make sure the power jumper of your discovery board is at STLK position
- Connect the discovery board to your computer via the **miniUSB** cable on the top of the board.
    - The board should appear as a removable disk named `DIS_F469NI`.
- Copy the `initial_firmware_<version>.bin` file into the root of the `DIS_F469NI` filesystem.
- When the board is done flashing the firmware the board will reset itself and reboot to the bootloader. Bootloader will check the firmware and boot into the main firmware. If see an error message that no firmware is found - follow the update instructions and upload firmware via SD card.
- Now you can switch the power jumper where you like it and power the board from the powerbank or battery.

Flashing initial firmware via copy-paste of the `.bin` file sometimes fails - often because of the cable, or if you connect the device through a USB hub. In this case you can try a few more times (normally works in 2-3 attempts).

If it fails all the time you can use [stlink](https://github.com/stlink-org/stlink/releases/latest) open-source tool. Install it and type in your terminal: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. It usually works much more reliable.

### Upgrading firmware

- Download the `specter_upgrade_<version>.bin` from the [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Copy this binary to the root of the SD card (FAT-formatted, 32 GB max)
	- Make sure only one `specter_upgrade***.bin` file is in the root directory
- Insert SD card to the SD slot of the discovery board and power on the board
- Bootloader will flash the firmware and will notify you when it's done.
- Reboot the board - you will see Specter-DIY interface now, it will suggest you to select your PIN code

Whenever a new release is out just download the `specter_upgrade_<version>.bin` from the releases, drop it to the SD card and upgrade the device just like in the previous step. Bootloader will make sure only signed firmware can be loaded to the board.

### How to find out firmware version

Go to the `Device settings` menu - it will show the version number under the title of the screen.

## Use Specter-DIY wallet


![video](https://youtu.be/Oysg-hhBusc)


![video](https://youtu.be/XfMr7B_uUIk)


![video](https://youtu.be/BzBlh_knIww)


## Security of Specter-DIY

### Hardware

Display is contolled by application MCU. 

Secure element integration is not there yet - at the moment secrets are also stored on the main MCU. But you can use the wallet without storing the secret - you need to enter your recovery phrase every time. Why to remember long passphrase if you can remember the whole mnemonic?

Device uses external flash to store some files (QSPI), but all user files are signed by the wallet and checked when loaded.

QR scanning functionality is on a separate microcontroller so all image processing happens outside of security-critical MCU. At the moment USB and SD card are still managed by the main MCU, so don't use SD card and USB if you want to reduce attack surface.

### PIN protection (user authentication)

During the first boot a unique secret is generated on the main MCU. This secret allows you to verify that the device was not replaced by a malicious one - when you enter the PIN code you see a list of words that will remain the same while the secret is there.

Your PIN code together with this unique secret are used to generate a decryption key for your Bitcoin keys (if you store them). So if the attacker would be able to bypass PIN screen, decryption will still fail.

If you have locked the firmware (TODO: add instructions link here) it will effectively lock the secret as well, so if the attacker flashes different firmware to the board the secret gets erased and you will be able to recognize it when you start entering PIN code - words sequence will be different.

### Generation of the recovery phrase

This is one of the most important parts of the wallet - to generate the key securely. To do this well we use multiple sources of entropy:

- TRNG of the microcontroller. Proprietary, certified and probably good but we don't trust it
- Touchscreen. Every time you touch the screen we measure the position and the moment when this touch happened (in microcontroller ticks at 180MHz).
- Built-in microphones - not yet. The board has two microphones, so hardware wallet can listen to you and mix in this data to the entropy pool.

All this entropy is hashed together and converted to your recovery phrase. The resulting entropy is always better than any of the individual sources.

### High level logic - wallets

Specter operates as a key storage. It holds HD private keys that can be involved in wallets. Wallets are defined by their descriptors. We support miniscript as well.

Every wallet belongs to a particular network. This means that if you imported a wallet on `testnet` it will not be available on `mainnet` or `regtest` - you need to switch to this network and import the wallet separately.

### Transactions verification

The following rules apply to transactions that wallet will sign:

- if mixed inputs from different wallets are found the user is warned ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- change outputs show the name of the wallet they are sent to
- to use a multisig or miniscript you first need to import the wallet by adding wallet descriptor (over QR, USB or SD card)

## Descriptors support

All normal Bitcoin descriptors work. Aside from that we have a few extensions:

### Multiple branches in descriptors

To save some space in the QR codes we allow adding descriptors with multiple branches in one go. If you want to use `wpkh(xpub/0/*)` for receiving addresses and `wpkh(xpub/1/*)` for change addresses you can combine them in a single descriptor: `wpkh(xpub/{0,1}/*)` - the wallet will treat first index of the `{}` set part as the branch for receiving addresses and the second one as change addresses.

You can also specify more than two branches, and branch indexes can be different for different cosigners, so this descriptor is very weird but totally valid:

```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```

Here for receiving address number 17 the wallet will use the script from `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.

The only requirement is that the number of indexes in all sets is the same (3 in the case above).

### Default derivations

If the descriptor contains master public keys but doesn't contain wildcard derivations, the default derivation `/{0,1}/*` will be added to all extended keys in the descriptor. If at least one of the xpubs has a wildcard derivation the descriptor will not be changed.

The descriptor `wpkh(xpub)` will be converted into `wpkh(xpub/{0,1}/*)`.

### Miniscript

Specter supports miniscript, but doesn't support policy-to-miniscript compilation (because it's way too expensive). We perform some checks on the miniscipt, so only `B` scripts are allowed on the top level and all arguments in sub-miniscripts have to have properties according to the [spec](http://bitcoin.sipa.be/miniscript/).

You can use [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) to generate a descriptor from a policy and then import it to the wallet.

For example, a policy "I can spend now, or in 100 days my wife can spend" can be converted into the wallet like so:

Policy: `or(9@pk(xpubA),and(older(14400),pk(B)))` (my key is 9-times more likely)

Miniscript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`

Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`

As here we don't have any wildcard derivations the default derivations of `/{0,1}/*` will be appended to the xpubs.


---

MIT License

Copyright (c) 2019 cryptoadvance

---
