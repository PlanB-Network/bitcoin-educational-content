---
name: Seed Signer

description: Set up of your Seed signer
---

![cover](assets/cover.webp)

## Material:

**Raspberry Pi Zero (version 1.3)**

For a completely air-gapped solution, make sure to use the version 1.3 with no WiFi or Bluetooth capability, but any Raspberry Pi 2/3/4 or Zero model will work.

Note: Raspberry Pi that those do not usually come with pins attached; the pins will either need to be soldered on, or something called a “GPIO Hammer” can be used.
GPIO Hammer

If your soldering isn’t quite up to scratch, or you just don’t own a soldering iron yet, then you can use “GPIO Hammer” as an alternative to soldering.

**Hat LCD WaveShare 1,3 inches with screen 240 × 240 pixels**

WaveShare LCD Hat 1.3″ 240×240 pxl LCD

**Note:** Choose the Waveshare screen carefully; make sure to purchase the model that has a resolution of 240×240 pixels.

**Camera module compatible with Pi Zero**

Raspberry Pi Camera Aokin/AuviPal 5MP 1080p with OV5647 Sensor Video Camera Module; other brands with the OV5647 sensor module should work as well, but may not be compatible with the Orange Pill enclosure.

**Note:** You will need to have a camera ribbon cable specifically compatible with Raspberry Pi Zero.

**MicroSD card with at least 4 GB of capacity**

extensive resources: https://seedsigner.com/explainers/

## Software:

Software Installation

1. Download the latest “seedsigner_x_x_x.img.zip” file
   latest release
2. Unzip the “seedsigner_x_x_x.img.zip” file
3. Use the Balena Etcher or a similar tool to write the unzipped .img image file to a microsd card
   BALENA ETCHER
4. Install the microsd card in SeedSigner.
   SeedSigner GPG Public Key
   seedsigner_pubkey.gpg

## Tutorial video

_guide taken from Southerbitcoiner, created by Cole_

### A collection of video guides covering SeedSigner: an open source, DIY Hardware Wallet/Signing device

![image](assets/1.webp)

SeedSigner is a Bitcoin Signing Device you can build from scratch. Sounds difficult, but this 4 part series should help you out :) I suggest you watch part 1 and 2, then decide wether you want to use desktop (watch part 3) or a mobile device (watch part 4).

Everything you need to know will be below. Other useful links include SeedSigner's website, their Github, their Keybase, the latest release, and hardware requirements.

### Part 1: How to build a SeedSigner:

In this video I show you how to download and verify the SeedSigner software, what parts are needed, and how to assemble your SeedSigner.

![video](https://youtu.be/mGmNKYOXtxY)

### Part 2: Testing your SeedSigner

Before I used my SeedSigner, I did a few tests to ensure it wasn't doing anything malicious. I thought I would share this step too. Here is how to verify that your SeedSigner exports the correct wallet (xpub), how to verify SeedSigners dice rolls math, and how to verify SeedSigners bip-85 child seeds.

![video](https://youtu.be/34W1IyTyXZE)

### Part 3: How to use SeedSigner with Sparrow Wallet (desktop)

SeedSigner is capable of generating seeds and signing off on bitcoin transactions. But by itself, it is not capable of building transactions. You need to use a wallet "coordinator" with your SeedSigner. This is how to use Sparrow Wallet with your SeedSigner:

![video](https://youtu.be/IQb8dh-VTOg)

Part 4: How to use SeedSigner with Blue Wallet (mobile)

SeedSigner is capable of generating seeds and signing off on bitcoin transactions. But by itself, it is not capable of creating transactions. You need to use a wallet "coordinator" with your SeedSigner. This is how to use Blue Wallet with your SeedSigner:

![video](https://youtu.be/x0Ee35Ct0r4)

Those are all the SeedSigner guides, for now! Let me know if you think I am missing anything. These are on my list for potential videos:

- SeedSigner overall review. Is it a good choice for a signing device? Pros/cons?
- How to use Bip-85 with SeedSigner
- How to be uncle Jim with SeedSigner

Found these valuable? Consider sending a tip to help fund future videos:
https://www.southernbitcoiner.com/donate/
